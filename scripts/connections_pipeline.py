#!/usr/bin/env python3
"""Resumable connection-discovery pipeline: work queue, ingestion, specialist review packets, finalize, snapshots."""
from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import io
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PIPE = ROOT / "connections" / "pipeline"
DISC, REVIEW, WORK = PIPE / "discovery", PIPE / "review", PIPE / "work"
STATE, CONFIG, MERGED = PIPE / "state.json", PIPE / "config.json", PIPE / "merged.jsonl"
BACKUP, FAILED, LOG = PIPE / "state.json.bak", PIPE / "work" / "failed", PIPE / "runs.log"
REGISTRY = ROOT / "connections" / "registry.jsonl"
PHYSLIB = ROOT / "scripts" / "physlib.py"
INDEX, GRAPH = ROOT / "library" / "index.json", ROOT / "library" / "connections.json"
KINDS = {"identity", "mechanism", "analogy", "duality", "method transfer", "shared object", "historical"}
CONF = {"established", "current research", "proposed"}
FIELDS = [f"{i:02d}" for i in range(12)]
TITLES = {"00": "Foundations", "01": "Classical Mechanics", "02": "Electromagnetism and Optics", "03": "Thermodynamics and Statistical Mechanics",
          "04": "Quantum Physics", "05": "Relativity and Gravitation", "06": "Particle Physics", "07": "Nuclear Physics",
          "08": "Condensed Matter Physics", "09": "Astrophysics and Cosmology", "10": "Plasma Physics", "11": "Interdisciplinary and Applied Physics"}
AGENTS = {"00": "foundations-physicist", "01": "classical-physicist", "02": "em-optics-physicist", "03": "statistical-physicist",
          "04": "quantum-physicist", "05": "relativist", "06": "particle-physicist", "07": "nuclear-physicist",
          "08": "condensed-matter-physicist", "09": "astrophysicist", "10": "plasma-physicist", "11": "applied-physicist"}
ASSIGN = {"00": ["01", "02", "03", "04", "05", "06"], "01": ["02", "03", "04", "05", "06", "07"], "02": ["03", "04", "05", "06", "07", "08"],
          "03": ["04", "05", "06", "07", "08", "09"], "04": ["05", "06", "07", "08", "09", "10"], "05": ["06", "07", "08", "09", "10", "11"],
          "06": ["07", "08", "09", "10", "11"], "07": ["08", "09", "10", "11", "00"], "08": ["09", "10", "11", "00", "01"],
          "09": ["10", "11", "00", "01", "02"], "10": ["11", "00", "01", "02", "03"], "11": ["00", "01", "02", "03", "04"]}
DEFAULT_CONFIG = {"units_per_run": 4, "max_units_per_day": 30, "max_attempts": 4, "review_chunk": 100,
                  "model": {"discovery": "sonnet", "review": ""}, "effort": {"discovery": "medium", "review": "medium"},
                  "last_attempt_model": {"discovery": "opus", "review": ""}, "max_budget_usd": {"discovery": 1.5, "review": 8},
                  "cooldown_minutes": 60, "transient_cooldown_minutes": 15, "interval_hours": 2, "stale_running_hours": 3,
                  "unit_timeout_minutes": 45, "stall_hours": 24, "stage_gate": {}}
MAX_TRANSIENT_REFUNDS, MAX_INTERRUPT_REFUNDS = 6, 2
MONTHS = ("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec")
WEEKDAYS = ("mon", "tue", "wed", "thu", "fri", "sat", "sun")
RECORD_KEYS = ("id", "a", "b", "name", "kind", "status", "summary", "map", "breaks", "confidence", "strength", "sources", "review")
EDITABLE = ("a", "b", "name", "kind", "summary", "map", "breaks", "confidence", "strength", "sources")


def now() -> dt.datetime:
    return dt.datetime.now().replace(microsecond=0)


def out(text: str = "") -> None:
    sys.stdout.write(text + "\n")


def warn(text: str) -> None:
    sys.stderr.write(f"warning: {text}\n")


def parse_time(value) -> dt.datetime | None:
    try:
        return dt.datetime.fromisoformat(str(value)).replace(tzinfo=None) if value else None
    except ValueError:
        return None


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    tmp.write_text(text, encoding="utf-8")
    for _ in range(20):
        try:
            os.replace(tmp, path)
            return
        except PermissionError:
            time.sleep(0.5)  # OneDrive or an editor briefly holds the file
    os.replace(tmp, path)


def config() -> dict:
    cfg = json.loads(json.dumps(DEFAULT_CONFIG))
    try:
        user = json.loads(CONFIG.read_text(encoding="utf-8")) if CONFIG.exists() else {}
    except (OSError, json.JSONDecodeError) as exc:
        warn(f"config.json is unreadable ({exc}); using the defaults")
        user = {}
    for key, value in (user if isinstance(user, dict) else {}).items():
        default = cfg.get(key)
        if isinstance(default, dict) and isinstance(value, dict):
            cfg[key] = {**default, **value}
        elif isinstance(default, (int, float)) and not isinstance(default, bool):
            if isinstance(value, (int, float)) and not isinstance(value, bool) and value > 0:
                cfg[key] = value
            else:
                warn(f"config.json: `{key}` must be a positive number, got {value!r}; using {default}")
        else:
            cfg[key] = value
    return cfg


def load_state() -> dict:
    state = {}
    for path in (STATE, BACKUP):
        if not path.exists():
            continue
        try:
            state = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            if path == STATE:
                shutil.copyfile(STATE, PIPE / f"state.corrupt-{now():%Y%m%d-%H%M%S}.json")
            warn(f"{path.name} is unreadable ({exc})")
            continue
        if path == BACKUP:
            warn("restored the pipeline state from state.json.bak")
            write_text(STATE, json.dumps(state, indent=1, ensure_ascii=False))
        break
    state = state if isinstance(state, dict) else {}
    state.setdefault("units", {})
    state.setdefault("stage", "discovery")
    state.setdefault("completed", [])
    return state


def save_state(state: dict) -> None:
    try:
        json.loads(STATE.read_text(encoding="utf-8"))
        write_text(BACKUP, STATE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        pass
    write_text(STATE, json.dumps(state, indent=1, ensure_ascii=False))


def read_jsonl(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines() if path.exists() else []:
        line = line.strip()
        if line.startswith("{"):
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return rows


def write_jsonl(path: Path, rows: list[dict]) -> None:
    write_text(path, "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))


def json_objects(text: str) -> list[dict]:
    dec, rows, i = json.JSONDecoder(), [], 0
    while (i := text.find("{", i)) != -1:
        try:
            obj, i = dec.raw_decode(text, i)
        except json.JSONDecodeError:
            i += 1
            continue
        if isinstance(obj, dict):
            rows.append(obj)
    return rows


def clean_path(p) -> str:
    return str(p or "").strip().strip("/").removeprefix("knowledge/").removesuffix("/README.md").strip("/")


def node_ok(p: str) -> bool:
    return bool(p) and (ROOT / "knowledge" / p / "README.md").exists()


def problems_of(rec: dict) -> list[str]:
    issues = [f"missing `{k}`" for k in ("a", "b", "name", "kind", "status", "summary", "confidence", "strength") if rec.get(k) in (None, "")]
    for key in ("a", "b"):
        if rec.get(key) and not node_ok(clean_path(rec[key])):
            issues.append(f"`{key}` is not a node path: {rec[key]}")
    if clean_path(rec.get("a")) == clean_path(rec.get("b")):
        issues.append("a == b")
    if rec.get("kind") not in KINDS:
        issues.append(f"bad kind {rec.get('kind')!r}")
    if rec.get("confidence") not in CONF:
        issues.append(f"bad confidence {rec.get('confidence')!r}")
    if rec.get("status") not in ("written", "new"):
        issues.append("status must be written|new")
    if rec.get("strength") not in (1, 2, 3):
        issues.append("strength must be 1|2|3")
    if rec.get("kind") == "analogy" and not rec.get("breaks"):
        issues.append("analogy needs `breaks`")
    return issues


def normalize(rec: dict) -> dict | None:
    rec = dict(rec)
    rec["a"], rec["b"] = clean_path(rec.get("a")), clean_path(rec.get("b"))
    if not (node_ok(rec["a"]) and node_ok(rec["b"])) or rec["a"] == rec["b"]:
        return None
    if rec["b"] < rec["a"]:
        rec["a"], rec["b"] = rec["b"], rec["a"]
    rec["kind"] = rec.get("kind") if rec.get("kind") in KINDS else "analogy"
    rec["confidence"] = rec.get("confidence") if rec.get("confidence") in CONF else "proposed"
    rec["strength"] = rec.get("strength") if rec.get("strength") in (1, 2, 3) else 1
    rec["status"] = rec.get("status") if rec.get("status") in ("written", "new") else "new"
    rec["sources"] = [s for s in rec.get("sources") or [] if isinstance(s, str) and s.strip()][:3]
    for key in ("name", "summary", "map", "breaks"):
        rec[key] = str(rec.get(key) or "").strip()
    if not rec["breaks"] and rec["kind"] == "analogy":
        rec["breaks"] = "Not stated by the analyst."
    return rec if rec["name"] and rec["summary"] else None


def name_key(rec: dict) -> tuple:
    return rec["a"], rec["b"], re.sub(r"\W+", "", rec["name"].lower())


def discovery_units() -> list[str]:
    return [f"discover-{h}-{p}" if p != h else f"discover-{h}-within" for h, ps in ASSIGN.items() for p in ps + [h]]


def unit_pair(unit: str) -> tuple[str, str]:
    _, a, b = unit.split("-", 2)
    return tuple(sorted((a, a if b == "within" else b)))


def discovery_records() -> list[dict]:
    rows = []
    for path in sorted(DISC.glob("batch-*.jsonl")):
        rows += read_jsonl(path)
    return rows


def covered_pairs() -> Counter:
    cov = Counter()
    for r in discovery_records():
        a, b = clean_path(r.get("a"))[:2], clean_path(r.get("b"))[:2]
        if a in TITLES and b in TITLES:
            cov[tuple(sorted((a, b)))] += 1
    return cov


def review_units() -> list[str]:
    return sorted(f"review-{p.stem.removeprefix('packet-')}" for p in REVIEW.glob("packet-*.jsonl"))


def unit_done(unit: str, cov: Counter | None = None) -> bool:
    if unit.startswith("discover-"):
        return bool((cov if cov is not None else covered_pairs()).get(unit_pair(unit)))
    return bool(read_jsonl(REVIEW / f"review-{unit.removeprefix('review-')}.jsonl"))


def runnable(unit: str, state: dict, cfg: dict) -> bool:
    info = state["units"].get(unit, {})
    if info.get("attempts", 0) >= cfg["max_attempts"] and info.get("status") != "running":
        return False
    if info.get("status") == "running":
        started = dt.datetime.fromisoformat(info.get("updated", "2000-01-01T00:00:00"))
        return now() - started > dt.timedelta(hours=cfg["stale_running_hours"])
    return True


def completed_today(state: dict) -> int:
    today = now().date().isoformat()
    return sum(1 for c in state["completed"] if c.get("at", "").startswith(today))


def exhausted(state: dict, cfg: dict, units: list[str]) -> list[str]:
    return [u for u in units if state["units"].get(u, {}).get("attempts", 0) >= cfg["max_attempts"]
            and state["units"].get(u, {}).get("status") != "running"]


def waiting(state: dict) -> str:
    t = now()
    pause = state.get("paused")
    if isinstance(pause, dict):
        until = parse_time(pause.get("until"))
        if until is None or until > t:
            return "paused" + (f" until {until:%Y-%m-%d %H:%M}" if until else "") + (f": {pause['reason']}" if pause.get("reason") else "")
        state.pop("paused")
        save_state(state)
    until = parse_time(state.get("cooldown_until"))
    if until and t < until < t + dt.timedelta(days=8):
        return f"cooling down until {until:%Y-%m-%d %H:%M} ({state.get('cooldown_reason', 'usage limit')})"
    if "cooldown_until" in state:
        state.pop("cooldown_until")
        state.pop("cooldown_reason", None)
        save_state(state)
    return ""


def gate(state: dict, cfg: dict) -> tuple[str, str]:
    rule = (cfg.get("stage_gate") or {}).get(state["stage"])
    if not isinstance(rule, dict):
        return "", ""
    where = str(rule.get("platform") or "").lower()
    if where and not sys.platform.startswith(where):
        return "HANDOFF", f"the {state['stage']} stage runs on {where}, not on this {sys.platform} machine (config.json stage_gate)"
    start = parse_time(rule.get("not_before"))
    if start and now() < start:
        return "WAIT", f"the {state['stage']} stage is held until {start:%Y-%m-%d %H:%M} (config.json stage_gate)"
    return "", ""


def cmd_status(args) -> int:
    state, cfg, cov = load_state(), config(), covered_pairs()
    disc = discovery_units()
    done = [u for u in disc if unit_done(u, cov)]
    out(f"stage: {state['stage']} · discovery {len(done)}/{len(disc)} sets · {sum(cov.values())} raw records · "
        f"completed today {completed_today(state)}/{cfg['max_units_per_day']}")
    wait = waiting(state)
    if wait:
        out(f"waiting: {wait}")
    held = gate(state, cfg)[1]
    if held:
        out(f"gated: {held}")
    revs = review_units()
    if revs:
        out(f"review: {sum(1 for u in revs if unit_done(u))}/{len(revs)} packets reviewed")
    if REGISTRY.exists():
        rows = read_jsonl(REGISTRY)
        out(f"registry: {len(rows)} connections ({sum(1 for r in rows if 'checked by' in r.get('review', ''))} specialist-checked)")
    pending = [u for u in (disc if state["stage"] == "discovery" else revs) if not unit_done(u, cov)]
    for u in pending[: args.n]:
        info = state["units"].get(u, {})
        out(f"  {u:22} {info.get('status', 'todo'):9} attempts {info.get('attempts', 0)}  {info.get('note', '')[:70]}")
    return 0


def advance(state: dict) -> None:
    cov = covered_pairs()
    if state["stage"] == "discovery" and all(unit_done(u, cov) for u in discovery_units()):
        prepare()
        state["stage"] = "review"
    if state["stage"] == "review" and review_units() and all(unit_done(u) for u in review_units()):
        finalize()
        state["stage"] = "done"
    save_state(state)


def cmd_next(args) -> int:
    state, cfg = load_state(), config()
    wait = "" if args.ignore_wait else waiting(state)
    if wait:
        out(f"WAIT\t{wait}")
        return 0
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        advance(state)
    for line in buf.getvalue().splitlines():
        if line.strip():
            out(f"INFO\t{line.strip()}")
    if state["stage"] == "done":
        out("DONE")
        return 0
    kind, why = gate(state, cfg)
    if kind == "HANDOFF" or kind and not args.ignore_wait:
        out(f"{kind}\t{why}")
        return 0
    budget =min(args.n or cfg["units_per_run"], max(0, cfg["max_units_per_day"] - completed_today(state)))
    if budget == 0:
        out("CAPPED")
        return 0
    cov, stage = covered_pairs(), state["stage"]
    pending = [u for u in (discovery_units() if stage == "discovery" else review_units()) if not unit_done(u, cov)]
    picked = [u for u in pending if runnable(u, state, cfg)][:budget]
    stuck = exhausted(state, cfg, pending)
    if stuck and not picked:
        out(f"BLOCKED\t{len(stuck)} unit(s) used all {cfg['max_attempts']} attempts: {', '.join(stuck)}. "
            "Retry them with `python -I scripts/connections_pipeline.py reset --exhausted`.")
    elif not picked:
        out(f"WAIT\tnothing runnable: {len(pending)} pending unit(s) are still marked running")
    for u in picked:
        model = stage_setting(cfg, "model", stage)
        if state["units"].get(u, {}).get("attempts", 0) + 1 >= cfg["max_attempts"]:
            model = stage_setting(cfg, "last_attempt_model", stage) or model
        out("\t".join(["UNIT", u, model, stage_setting(cfg, "effort", stage), stage_setting(cfg, "max_budget_usd", stage),
                       str(cfg["unit_timeout_minutes"])]))
    return 0


def stage_setting(cfg: dict, key: str, stage: str) -> str:
    value = cfg.get(key) or ""
    return str((value.get(stage) or "") if isinstance(value, dict) else value)


def subfield(path: str) -> str:
    return "/".join(path.split("/")[:2])


def discovery_context(a: str, b: str) -> str:
    index = json.loads(INDEX.read_text(encoding="utf-8"))
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    within, codes = a == b, {a, b}

    def in_set(x: str, y: str) -> bool:
        if within:
            return x[:2] == y[:2] == a and subfield(x) != subfield(y)
        return {x[:2], y[:2]} == codes

    nodes = [n for n in index if n["path"][:2] in codes]
    lines = [f"## Nodes ({len(nodes)})"] + [f"- {n['path']} | {n.get('summary', '')[:150]}" for n in nodes]
    links = [(s, d) for s, d in graph["edges"] if in_set(s, d)]
    lines += ["", f"## Explicit cross-links already written in the notes ({len(links)}): each becomes a \"written\" record"]
    lines += [f"- {s} -> {d}" for s, d in links]
    concepts = defaultdict(set)
    for path, names in graph["node_concepts"].items():
        if path[:2] in codes:
            for c in names:
                concepts[c].add(subfield(path) if within else path[:2])
    shared = sorted(c for c, where in concepts.items() if len(where) > 1)
    lines += ["", f"## Shared curated concepts ({len(shared)})"]
    lines += [f"- {c}: {graph['concepts'].get(c, {}).get('idea', '')}" for c in shared]
    latent = sorted((r for k in ("latent_across", "latent_within") for r in graph[k] if in_set(r["a"], r["b"])), key=lambda r: -r["score"])
    lines += ["", f"## Latent candidate pairs ({len(latent)})"]
    lines += [f"- {r['a']} <-> {r['b']} (score {r['score']:.2f}; shares {', '.join(r['shared'][:6])})" for r in latent[:30]]
    lit = [r for r in graph["shared_literature"] if in_set(r["a"], r["b"])]
    lines += ["", f"## Shared papers ({len(lit)} note pairs; algorithmic, weak evidence)"]
    for r in lit[:20]:
        top = max(r["papers"], key=lambda p: p.get("citations", 0))
        lines.append(f"- {r['a']} <-> {r['b']}: \"{top['title'][:90]}\" ({top.get('year')})")
    return "\n".join(lines)


def codex_excerpt(field: str, paths: set) -> str:
    slug = next(p.name for p in (ROOT / "knowledge").iterdir() if p.name.startswith(field + "-"))
    codex = ROOT / ".claude" / "skills" / f"codex-{slug}" / "SKILL.md"
    if not codex.exists():
        return ""
    wanted = {"/".join(p.split("/")[:k]) for p in paths for k in range(1, p.count("/") + 2)}
    blocks, keep, skip = [], False, False
    for line in codex.read_text(encoding="utf-8").splitlines():
        if re.match(r"#{1,3} ", line):
            m = re.search(r"`knowledge/([^`]+)`", line)
            keep = bool(m) and m.group(1).strip("/") in wanted
        if re.match(r"#{1,4} ", line) or line.startswith("**"):
            skip = line.startswith(("**Literature index", "**Landmarks", "#### Landmark papers"))
        if keep and not skip and (line.strip() or (blocks and blocks[-1].strip())):
            blocks.append(line)
    return "\n".join(blocks)


def unit_prompt(unit: str) -> str:
    if unit.startswith("discover-"):
        _, a, b = unit.split("-", 2)
        b = a if b == "within" else b
        scope = f"{a}-within (links between different subfields of {TITLES[a]})" if a == b else f"{a}-{b} ({TITLES[a]} with {TITLES[b]})"
        return "\n\n".join([(PIPE / "brief-discovery.md").read_text(encoding="utf-8"), "---", f"# Your set: {scope}",
                            discovery_context(a, b)])
    packet = unit.removeprefix("review-")
    field = packet.split("-")[0]
    rows = read_jsonl(REVIEW / f"packet-{packet}.jsonl")
    mine = {r[s] for r in rows for s in ("a", "b") if r[s][:2] == field}
    excerpt = codex_excerpt(field, mine) or "(No codex found: Read the README of any node you need to check.)"
    shown = "\n".join(json.dumps({k: v for k, v in r.items() if k not in ("sources", "status")}, ensure_ascii=False) for r in rows)
    return "\n\n".join([f"You are the {AGENTS[field]}, the specialist for {field} ({TITLES[field]}) in this physics knowledge base.",
                        (PIPE / "brief-review.md").read_text(encoding="utf-8"), "---",
                        f"# Your branch notes: the codex sections for the nodes in this packet", excerpt, "---",
                        f"# Packet {packet} ({len(rows)} records)", shown])


def cmd_prompt(args) -> int:
    text = unit_prompt(args.unit)
    if len(text) < 2000 or "# Your set" not in text and "# Packet" not in text:
        sys.stderr.write(f"prompt for {args.unit} looks broken ({len(text)} chars); not writing it\n")
        return 1
    if args.out:
        write_text(Path(args.out), text)
    else:
        out(text)
    return 0


def cmd_mark(args) -> int:
    state = load_state()
    info = state["units"].setdefault(args.unit, {"attempts": 0})
    if args.status == "running":
        info["attempts"] = info.get("attempts", 0) + 1
    if args.status == "limit":
        info["attempts"] = max(0, info.get("attempts", 0) - 1)
    info["status"] = "failed" if args.status == "limit" else args.status
    info["updated"] = now().isoformat()
    if args.note:
        info["note"] = args.note
    if args.status == "done":
        state["completed"].append({"unit": args.unit, "at": now().isoformat()})
    save_state(state)
    return 0


def cmd_recover(args) -> int:
    state = load_state()
    fixed = [u for u, info in state["units"].items() if info.get("status") == "running"]
    for unit in fixed:
        info = state["units"][unit]
        info["interrupted"] = info.get("interrupted", 0) + 1
        refund = info["interrupted"] <= MAX_INTERRUPT_REFUNDS
        if refund:
            info["attempts"] = max(0, info.get("attempts", 1) - 1)
        info.update({"status": "failed", "updated": now().isoformat(),
                     "note": f"interrupted: the run ended before the unit finished (#{info['interrupted']})"})
        out(f"recovered {unit}: the previous run ended while it was running" + ("" if refund else "; counted as an attempt"))
    if fixed:
        save_state(state)
    return 0


def cmd_reset(args) -> int:
    state, cfg = load_state(), config()
    units = exhausted(state, cfg, list(state["units"])) if args.exhausted else args.units
    for unit in units:
        state["units"][unit] = {"attempts": 0, "status": "todo", "updated": now().isoformat(), "note": "reset by hand"}
        out(f"reset {unit}")
    if args.cooldown and state.pop("cooldown_until", None):
        state.pop("cooldown_reason", None)
        out("cleared the cooldown")
    save_state(state)
    return 0


def cmd_pause(args) -> int:
    state = load_state()
    until = now() + dt.timedelta(hours=args.hours) if args.hours else None
    state["paused"] = {"until": until.isoformat() if until else "", "reason": args.reason, "at": now().isoformat()}
    save_state(state)
    out("paused" + (f" until {until:%Y-%m-%d %H:%M}" if until else " until `resume`"))
    return 0


def cmd_resume(args) -> int:
    state = load_state()
    was = state.pop("paused", None)
    save_state(state)
    out("resumed" if was else "was not paused")
    return 0


def last_log_time() -> dt.datetime | None:
    try:
        with LOG.open("rb") as fh:
            fh.seek(max(0, LOG.stat().st_size - 4000))
            lines = fh.read().decode("utf-8", errors="replace").splitlines()
    except OSError:
        return None
    for line in reversed(lines):
        stamp = parse_time(line[:19].replace(" ", "T"))
        if stamp:
            return stamp
    return None


def health(state: dict, cfg: dict) -> list[tuple[str, str, str]]:
    t, rows = now(), []
    add = lambda level, key, msg: rows.append((level, key, msg))
    stage, cov = state["stage"], covered_pairs()
    pool = discovery_units() if stage == "discovery" else review_units() if stage == "review" else []
    pending = [u for u in pool if not unit_done(u, cov)]
    add("OK", "progress", f"stage {stage}: {len(pool) - len(pending)}/{len(pool)} units done, {len(pending)} pending, "
                          f"{completed_today(state)}/{cfg['max_units_per_day']} today")
    wait = waiting(state)
    if wait:
        add("WARN" if wait.startswith("paused") else "OK", "wait", wait)
    held = gate(state, cfg)[1]
    if held:
        add("OK", "gate", held)
        wait = wait or held
    running = [u for u in pool if state["units"].get(u, {}).get("status") == "running"]
    if running:
        add("WARN", "running", f"marked running: {', '.join(running)} (normal only while a run is active; the next run recovers them)")
    stuck = exhausted(state, cfg, pending)
    if stuck:
        add("FAIL", "blocked", f"{len(stuck)} unit(s) used all {cfg['max_attempts']} attempts: {', '.join(stuck)}. "
                               "Retry with `python -I scripts/connections_pipeline.py reset --exhausted`")
    shaky = [u for u in pending if u not in stuck and state["units"].get(u, {}).get("attempts", 0) >= 2]
    if shaky:
        add("WARN", "retrying", "failed twice or more: " + ", ".join(f"{u} ({state['units'][u].get('note', '')[:50]})" for u in shaky))
    capped = [u for u, i in state["units"].items() if "budget" in i.get("note", "")]
    if capped:
        add("WARN", "budget", f"hit the per-unit budget cap: {', '.join(capped)}; raise `max_budget_usd` in config.json if this repeats")
    last = max((parse_time(c.get("at")) for c in state["completed"]), default=None, key=lambda d: d or dt.datetime.min)
    if stage != "done" and last and t - last > dt.timedelta(hours=cfg["stall_hours"]) and not wait:
        add("FAIL", "stalled", f"no unit has completed since {last:%Y-%m-%d %H:%M}; see runs.log and `doctor`")
    logged = last_log_time()
    if stage != "done" and logged and not held and t - logged > dt.timedelta(hours=2 * cfg["interval_hours"] + 1):
        add("WARN", "quiet", f"nothing logged since {logged:%Y-%m-%d %H:%M}: the PC was off or asleep, or the task isn't firing")
    for path in sorted(DISC.glob("batch-*.jsonl")):
        rows_in = read_jsonl(path)
        valid = sum(1 for r in rows_in if normalize(r))
        if not valid:
            add("FAIL", f"batch:{path.name}", f"{path.name} has no valid records")
        elif valid < 0.7 * len(rows_in):
            add("WARN", f"batch:{path.name}", f"{path.name}: only {valid}/{len(rows_in)} records are valid")
    if stage in ("review", "done"):
        packets = review_units()
        add("OK", "review", f"{sum(1 for u in packets if unit_done(u))}/{len(packets)} review packets reviewed")
        if not MERGED.exists():
            add("FAIL", "merged", "merged.jsonl is missing; run `python -I scripts/connections_pipeline.py prepare`")
    reg = read_jsonl(REGISTRY)
    add("OK" if reg else "WARN", "registry", f"registry: {len(reg)} connections" + (" (final)" if stage == "done" else " (interim)"))
    free = shutil.disk_usage(ROOT).free / 2 ** 30
    if free < 1:
        add("WARN", "disk", f"only {free:.1f} GB free on the project drive")
    failures = list(FAILED.glob("*.txt")) if FAILED.exists() else []
    if failures:
        newest = max(failures, key=lambda p: p.stat().st_mtime)
        add("OK", "failures", f"{len(failures)} failed session output(s) kept in work/failed (newest {newest.name})")
    return rows


def cmd_doctor(args) -> int:
    rows = health(load_state(), config())
    if args.alerts:
        for level, key, msg in rows:
            if level == "FAIL":
                out(f"ALERT\t{key}\t{msg}")
        return 0
    for level, _, msg in rows:
        out(f"{level:4}  {msg}")
    return 1 if any(level == "FAIL" for level, _, _ in rows) else 0


def read_or_empty(path) -> str:
    try:
        return Path(path).read_text(encoding="utf-8", errors="replace") if path and Path(path).exists() else ""
    except OSError:
        return ""


def session_output(stdout: str) -> tuple[dict | None, str, str]:
    wraps = [o for o in json_objects(stdout) if o.get("type") == "result"]
    if not wraps:
        return None, stdout, ""
    wrap = wraps[-1]
    u = wrap.get("usage") or {}
    k = lambda key: f"{(u.get(key) or 0) / 1000:.0f}k"
    usage = (f"{wrap.get('num_turns', '?')} turns, {k('input_tokens')} in + {k('cache_creation_input_tokens')} cache-write + "
             f"{k('cache_read_input_tokens')} cache-read, {k('output_tokens')} out, ~${wrap.get('total_cost_usd') or 0:.2f}")
    return wrap, str(wrap.get("result") or ""), usage


def reset_time(msg: str) -> dt.datetime | None:
    m = re.search(r"resets?\s+(?:in\s+)?(?:(?P<hrs>\d+)\s*h\w*\s*)?(?:(?P<mins>\d+)\s*m\w*)?", msg, re.I)
    if m and (m["hrs"] or m["mins"]) and re.search(r"resets?\s+in\b", msg, re.I):
        return now() + dt.timedelta(hours=int(m["hrs"] or 0), minutes=int(m["mins"] or 0))
    m = re.search(r"resets?\s+(?:at\s+|on\s+)?(?:(?P<wd>mon|tue|wed|thu|fri|sat|sun)\w*,?\s+)?(?:(?P<mon>[a-z]{3})\w*\.?\s+(?P<day>\d{1,2}),?\s+"
                  r"(?:at\s+)?)?(?P<h>\d{1,2})(?::(?P<mi>\d{2}))?\s*(?P<ap>am|pm)?\s*(?:\((?P<tz>[A-Za-z_]+/[A-Za-z_/+-]+)\))?", msg, re.I)
    if not m or not (m["ap"] or m["mi"]) or (m["mon"] and m["mon"].lower() not in MONTHS):
        return None
    hour = int(m["h"]) % 12 + (12 if (m["ap"] or "").lower() == "pm" else 0) if m["ap"] else int(m["h"])
    if hour > 23:
        return None
    zone = None
    if m["tz"]:
        try:
            from zoneinfo import ZoneInfo
            zone = ZoneInfo(m["tz"])
        except Exception:
            zone = None
    base = dt.datetime.now(zone).replace(tzinfo=None, microsecond=0) if zone else now()
    target = base.replace(hour=hour, minute=int(m["mi"] or 0), second=0)
    if m["mon"]:
        target = target.replace(month=MONTHS.index(m["mon"].lower()) + 1, day=int(m["day"]))
        if target < base - dt.timedelta(days=1):
            target = target.replace(year=target.year + 1)
    elif m["wd"]:
        target += dt.timedelta(days=(WEEKDAYS.index(m["wd"].lower()) - target.weekday()) % 7)
        if target <= base:
            target += dt.timedelta(days=7)
    elif target <= base:
        target += dt.timedelta(days=1)
    return target.replace(tzinfo=zone).astimezone().replace(tzinfo=None) if zone else target


def classify(wrap: dict | None, stdout: str, stderr: str, timed_out: bool) -> tuple[str, str]:
    if timed_out:
        return "ERROR", "killed at the unit timeout"
    if wrap and not wrap.get("is_error"):
        sub = str(wrap.get("subtype") or "success")
        return ("OK", "") if sub == "success" else ("ERROR", f"session ended with {sub}")
    status = (wrap or {}).get("api_error_status")
    hay = " ".join([str((wrap or {}).get(k) or "") for k in ("result", "api_error", "subtype", "terminal_reason")] +
                   ([] if wrap else [stdout[:4000]]) + [stderr[-4000:]])
    if status in (401, 403) or re.search(r"not logged in|/login|authentication_error|oauth token|invalid api key|token has expired|"
                                         r"unauthori[sz]ed|invalid_grant", hay, re.I):
        return "AUTH", "Claude sign-in failed"
    if re.search(r"usage_limit|hit your .{0,40}limit|usage limit|limit reached|limit · resets|resets \d", hay, re.I):
        return "LIMIT", (wrap or {}).get("result") or "usage limit"
    if status == 429 or status in (408, 409, 529) or (isinstance(status, int) and status >= 500) or re.search(
            r"overloaded|rate.?limit|too many requests|connection error|ECONNRESET|ECONNREFUSED|ETIMEDOUT|ENOTFOUND|EAI_AGAIN|"
            r"socket hang up|fetch failed|network|service unavailable|internal server error|bad gateway", hay, re.I):
        return "TRANSIENT", re.sub(r"\s+", " ", hay).strip()[:160]
    if wrap and "budget" in hay.lower():
        return "ERROR", "hit the per-unit budget cap"
    return "ERROR", re.sub(r"\s+", " ", hay).strip()[:160] or "the session produced no result"


def archive_failure(unit: str, stdout: str, stderr: str, why: str) -> None:
    FAILED.mkdir(parents=True, exist_ok=True)
    write_text(FAILED / f"{unit}-{dt.datetime.now():%Y%m%d-%H%M%S-%f}.txt", f"# {unit}: {why}\n\n## stdout\n{stdout}\n\n## stderr\n{stderr}\n")
    for old in sorted(FAILED.glob("*.txt"), key=lambda p: p.stat().st_mtime)[:-40]:
        old.unlink(missing_ok=True)


def cmd_ingest(args) -> int:
    stdout, stderr = read_or_empty(args.file), read_or_empty(args.err)
    wrap, result, usage = session_output(stdout)
    kind, detail = classify(wrap, stdout, stderr, args.timed_out)
    state, cfg = load_state(), config()
    info = state["units"].setdefault(args.unit, {"attempts": 1})
    if kind in ("LIMIT", "AUTH", "TRANSIENT"):
        refund = kind != "TRANSIENT" or info.get("transient", 0) < MAX_TRANSIENT_REFUNDS
        info["transient"] = info.get("transient", 0) + (kind == "TRANSIENT")
        if refund:
            info["attempts"] = max(0, info.get("attempts", 1) - 1)
        until = None
        if kind == "LIMIT":
            reset = reset_time(detail)
            until = max(reset + dt.timedelta(minutes=3), now() + dt.timedelta(minutes=10)) if reset else \
                now() + dt.timedelta(minutes=cfg["cooldown_minutes"])
        elif kind == "TRANSIENT":
            until = now() + dt.timedelta(minutes=cfg["transient_cooldown_minutes"])
        if until:
            state["cooldown_until"], state["cooldown_reason"] = until.isoformat(), f"{kind.lower()}: {detail[:80]}"
        note = {"LIMIT": "usage limit", "AUTH": "sign-in expired", "TRANSIENT": f"transient API error: {detail[:80]}"}[kind]
        info.update({"status": "failed", "updated": now().isoformat(), "note": note})
        save_state(state)
        if kind != "LIMIT":
            archive_failure(args.unit, stdout, stderr, note)
        out("\t".join([kind, f"{args.unit}: {note}" + ("" if refund else " (counted as an attempt: too many transient errors)"),
                       until.isoformat() if until else ""]))
        return 0
    raw = json_objects(result)
    if args.unit.startswith("discover-"):
        pair = unit_pair(args.unit)
        kept, seen = [], set()
        for rec in raw:
            rec = normalize(rec)
            if rec and tuple(sorted((rec["a"][:2], rec["b"][:2]))) == pair and name_key(rec) not in seen:
                seen.add(name_key(rec))
                kept.append({k: rec.get(k, "") for k in RECORD_KEYS if k not in ("id", "review")})
        ok = len(kept) >= 3
        if ok:
            write_jsonl(DISC / f"batch-{args.unit.removeprefix('discover-')}.jsonl", kept)
        note = f"{len(kept)} valid of {len(raw)} records"
    else:
        packet = args.unit.removeprefix("review-")
        ids = {r["id"] for r in read_jsonl(REVIEW / f"packet-{packet}.jsonl")}
        verdicts = [v for v in raw if (v.get("id") in ids and v.get("verdict") in ("confirm", "revise", "reject")) or
                    (v.get("verdict") == "add" and isinstance(v.get("record"), dict))]
        covered = {v["id"] for v in verdicts if v.get("id")}
        ok = bool(ids) and len(covered) >= 0.6 * len(ids)
        if ok:
            write_jsonl(REVIEW / f"review-{packet}.jsonl", verdicts)
        note = f"{len(covered)}/{len(ids)} verdicts, {sum(1 for v in verdicts if v.get('verdict') == 'add')} additions"
    note += f" · {detail}" if detail else ""
    note += f" · {usage}" if usage else ""
    info.update({"status": "done" if ok else "failed", "updated": now().isoformat(), "note": note})
    if ok:
        state["completed"].append({"unit": args.unit, "at": now().isoformat()})
    else:
        archive_failure(args.unit, stdout, stderr, note)
    save_state(state)
    out(f"{'OK' if ok else 'FAILED'}\t{args.unit}: {'done' if ok else 'failed'} ({note})")
    return 0


def cmd_check(args) -> int:
    rows, bad = read_jsonl(Path(args.file)), 0
    for i, rec in enumerate(rows, 1):
        issues = problems_of(rec)
        if issues:
            bad += 1
            out(f"record {i}: " + "; ".join(issues))
    out(f"{len(rows)} records, {bad} with problems.")
    return 1 if bad else 0


def merged_discovery() -> list[dict]:
    merged, seen = [], set()
    for rec in discovery_records():
        rec = normalize(rec)
        if rec and name_key(rec) not in seen:
            seen.add(name_key(rec))
            merged.append(rec)
    merged.sort(key=lambda r: (r["a"][:2], r["b"][:2], r["a"], r["b"], r["name"]))
    return merged


def prepare() -> None:
    merged = merged_discovery()
    for i, rec in enumerate(merged, 1):
        rec["id"] = f"C{i:04d}"
    write_jsonl(MERGED, merged)
    chunk = config()["review_chunk"]
    for old in REVIEW.glob("packet-*.jsonl"):
        old.unlink()
    for f in FIELDS:
        packet = [{k: r[k] for k in RECORD_KEYS if k != "review"} for r in merged if f in (r["a"][:2], r["b"][:2])]
        for k in range(0, len(packet), chunk):
            write_jsonl(REVIEW / f"packet-{f}-{k // chunk + 1}.jsonl", packet[k:k + chunk])
    out(f"prepared {len(merged)} connections into {len(review_units())} review packets")


def online() -> bool:
    probes = ("https://export.arxiv.org/api/query?id_list=1207.7214&max_results=1", "https://api.crossref.org/works/10.1103/PhysRev.108.1175")
    for url in probes:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "physlib-pipeline/1.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                if resp.status != 200:
                    return False
        except OSError:
            return False
    return True


def rebuild_tree(check: bool) -> str:
    run = subprocess.run([sys.executable, "-I", str(PHYSLIB), "tree"] + (["--check"] if check else []), cwd=ROOT,
                         capture_output=True, text=True, encoding="utf-8")
    if run.returncode != 0 and not check:
        tail = (run.stderr or run.stdout).strip().splitlines()[-1:] or ["no output"]
        raise RuntimeError(f"tree rebuild failed (exit {run.returncode}): {tail[0][:200]}")
    return (run.stdout.strip().splitlines() or [""])[-1]


def verify_sources(records: list[dict]) -> set:
    lines, where = [], []
    for rec in records:
        for j, src in enumerate(rec["sources"]):
            lines.append("- " + src.replace("\n", " "))
            where.append((rec["id"], j))
    if not lines:
        return set()
    if not online():
        raise RuntimeError("arXiv or Crossref is unreachable, so citations can't be verified; finalize retries next run")
    run = subprocess.run([sys.executable, "-I", str(PHYSLIB), "verify", "--stdin"], input="\n".join(lines), capture_output=True,
                         text=True, encoding="utf-8", cwd=ROOT)
    summary = re.search(r"(\d+)/(\d+) references passed", run.stdout)
    if run.returncode not in (0, 1) or not summary:
        raise RuntimeError(f"citation check did not complete (exit {run.returncode}): {(run.stderr or run.stdout).strip()[-300:]}")
    passed, total = map(int, summary.groups())
    if total >= 20 and passed < 0.5 * total and not online():
        raise RuntimeError(f"only {passed}/{total} citations verified and the network dropped; finalize retries next run")
    out(summary.group(0))
    bad = {where[int(m.group(1)) - 1] for m in re.finditer(r"(?:NOT_FOUND|TITLE_MISMATCH|YEAR_MISMATCH)\s+\S+?:(\d+)\s", run.stdout)}
    return bad | {w for w, line in zip(where, lines) if not re.search(r"\[(?:arXiv|doi):", line, re.I)}


def finalize(force: bool = False) -> None:
    merged = {r["id"]: r for r in read_jsonl(MERGED)}
    verdicts, additions = defaultdict(list), []
    for path in sorted(REVIEW.glob("review-*.jsonl")):
        field = path.stem.removeprefix("review-").split("-")[0]
        for v in read_jsonl(path):
            if v.get("verdict") == "add":
                rec = normalize(dict(v["record"], status="new"))
                if rec:
                    rec["review"] = f"added by the {AGENTS[field]}"
                    additions.append(rec)
            elif v.get("id") in merged:
                verdicts[v["id"]].append(dict(v, field=field))
    kept, rejected = [], []
    for rid, rec in merged.items():
        sides = {rec["a"][:2], rec["b"][:2]}
        vs = [v for v in verdicts.get(rid, []) if v["field"] in sides]
        for v in vs:
            if v.get("verdict") == "revise":
                for key, value in (v.get("fix") or {}).items():
                    if key in EDITABLE and value not in (None, ""):
                        rec[key] = value
        rec = normalize(rec) or rec
        rejects = [v for v in vs if v.get("verdict") == "reject"]
        confirms = [v for v in vs if v.get("verdict") in ("confirm", "revise")]
        if rejects and not confirms:
            rejected.append({"id": rid, "name": rec["name"], "why": "; ".join(str(v.get("reason", "")) for v in rejects)})
            continue
        notes = []
        if rejects:
            rec["confidence"], rec["strength"] = "proposed", 1
            notes.append("contested — " + "; ".join(f"{AGENTS[v['field']]}: {v.get('reason', '')}" for v in rejects))
        checked = sorted({AGENTS[v["field"]] for v in confirms})
        revised = sorted({AGENTS[v["field"]] for v in vs if v.get("verdict") == "revise"})
        notes.append(("checked by " + " and ".join(checked) + (f" (revised by {', '.join(revised)})" if revised else ""))
                     if checked else "not reviewed by a specialist")
        rec["review"] = "; ".join(notes)
        kept.append(rec)
    seen, next_id = {name_key(r) for r in kept}, len(merged) + 1
    for rec in additions:
        if name_key(rec) not in seen:
            seen.add(name_key(rec))
            rec["id"] = f"C{next_id:04d}"
            next_id += 1
            kept.append(rec)
    bad = verify_sources(kept)
    for rec in kept:
        rec["sources"] = [s for j, s in enumerate(rec["sources"]) if (rec["id"], j) not in bad]
    kept.sort(key=lambda r: r["id"])
    if len(kept) < 0.5 * len(merged) and not force:
        raise RuntimeError(f"finalize would keep only {len(kept)} of {len(merged)} connections; check review/ and then run "
                           "`python -I scripts/connections_pipeline.py finalize --force`")
    write_jsonl(REGISTRY, [{k: r.get(k, "") for k in RECORD_KEYS} for r in kept])
    write_text(PIPE / "rejected.json", json.dumps(rejected, indent=1, ensure_ascii=False))
    out(f"tree check: {rebuild_tree(check=True)}")
    out(f"finalized: {len(kept)} connections in the registry, {len(rejected)} rejected, {len(bad)} unverifiable sources dropped")


def cmd_snapshot(args) -> int:
    state = load_state()
    if state["stage"] == "done":
        out("pipeline finished; registry is final")
        return 0
    rows = merged_discovery()
    for i, rec in enumerate(rows, 1):
        rec["id"] = f"I{i:04d}"
        rec["review"] = "interim: not yet reviewed by a specialist"
    old = len(read_jsonl(REGISTRY))
    if old and len(rows) < 0.9 * old:
        sys.stderr.write(f"snapshot would shrink the registry from {old} to {len(rows)} connections; leaving it as it is\n")
        return 1
    write_jsonl(REGISTRY, [{k: r.get(k, "") for k in RECORD_KEYS} for r in rows])
    rebuild_tree(check=False)
    out(f"snapshot: interim registry of {len(rows)} connections; map and codices rebuilt")
    return 0


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass
    parser = argparse.ArgumentParser(prog="connections_pipeline", description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("status")
    p.add_argument("-n", type=int, default=15)
    p.set_defaults(func=cmd_status)
    p = sub.add_parser("next", help="print UNIT<TAB>unit<TAB>model<TAB>effort<TAB>budget<TAB>timeout lines, or INFO, WAIT, HANDOFF, BLOCKED, CAPPED, DONE")
    p.add_argument("-n", type=int, default=0)
    p.add_argument("--ignore-wait", action="store_true", help="ignore a pause or cooldown (dry runs)")
    p.set_defaults(func=cmd_next)
    p = sub.add_parser("prompt", help="the full headless prompt for a unit: brief + pre-built context")
    p.add_argument("unit")
    p.add_argument("--out", help="write it to this file instead of stdout")
    p.set_defaults(func=cmd_prompt)
    p = sub.add_parser("mark")
    p.add_argument("unit")
    p.add_argument("status", choices=["running", "done", "failed", "limit"])
    p.add_argument("--note", default="")
    p.set_defaults(func=cmd_mark)
    p = sub.add_parser("ingest", help="classify a unit's session output and file its records; prints OK|FAILED|LIMIT|AUTH|TRANSIENT<TAB>msg<TAB>until")
    p.add_argument("unit")
    p.add_argument("file")
    p.add_argument("--err", default="", help="the session's stderr")
    p.add_argument("--timed-out", action="store_true")
    p.set_defaults(func=cmd_ingest)
    sub.add_parser("recover", help="reset units left 'running' by a run that died (the runner calls this under its lock)").set_defaults(func=cmd_recover)
    p = sub.add_parser("reset", help="give units fresh attempts")
    p.add_argument("units", nargs="*")
    p.add_argument("--exhausted", action="store_true", help="every unit that used all its attempts")
    p.add_argument("--cooldown", action="store_true", help="also clear a usage-limit cooldown")
    p.set_defaults(func=cmd_reset)
    p = sub.add_parser("pause", help="stop scheduled runs from doing work")
    p.add_argument("--hours", type=float, default=0)
    p.add_argument("--reason", default="")
    p.set_defaults(func=cmd_pause)
    sub.add_parser("resume", help="undo pause").set_defaults(func=cmd_resume)
    p = sub.add_parser("doctor", help="health check of the pipeline state, outputs and progress")
    p.add_argument("--alerts", action="store_true", help="print only actionable failures as ALERT<TAB>key<TAB>msg")
    p.set_defaults(func=cmd_doctor)
    p = sub.add_parser("check", help="validate a discovery JSONL file")
    p.add_argument("file")
    p.set_defaults(func=cmd_check)
    p = sub.add_parser("snapshot", help="interim registry from discovery so far + rebuild map and codices")
    p.set_defaults(func=cmd_snapshot)
    sub.add_parser("prepare").set_defaults(func=lambda a: prepare() or 0)
    p = sub.add_parser("finalize")
    p.add_argument("--force", action="store_true", help="write the registry even if most connections were rejected")
    p.set_defaults(func=lambda a: finalize(a.force) or 0)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
