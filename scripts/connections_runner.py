#!/usr/bin/env python3
"""Linux runner for the connection pipeline: one budgeted run (lock, recovery, units, ingest, snapshot, Discord findings), or --health."""
from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import fcntl
import importlib.util
import json
import os
import shutil
import signal
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PIPE = ROOT / "connections" / "pipeline"
LOG, LOCK, LOCK_INFO, ALERTS = PIPE / "runs.log", PIPE / ".run.flock", PIPE / "run.lock", PIPE / "alerts.json"
PIPELINE, POSTER = ROOT / "scripts" / "connections_pipeline.py", ROOT / "scripts" / "discord_post.py"
ENV_FILE = Path.home() / ".config" / "chanda" / "env"
SIGNATURE = ("--no-session-persistence", "--strict-mcp-config", "dontAsk")
LEAN = ["--strict-mcp-config", "--disable-slash-commands", "--setting-sources", "project", "--tools", "Read,Grep,Glob"]
SERVICE, TIMER, RESUME, AGENT = "chanda-pipeline.service", "chanda-pipeline.timer", "chanda-pipeline-resume", "chanda-agent.service"

spec = importlib.util.spec_from_file_location("connections_pipeline", PIPELINE)
cp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cp)


def log(msg: str) -> None:
    line = f"{dt.datetime.now():%Y-%m-%d %H:%M:%S}  {msg}"
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(line + "\n")
    print(line, flush=True)


def load_env() -> None:
    for path in (ENV_FILE, Path.home() / ".claude" / "channels" / "discord" / ".env"):
        with contextlib.suppress(OSError):
            for line in path.read_text(encoding="utf-8").splitlines():
                key, sep, value = line.strip().partition("=")
                if sep and key and not key.startswith("#") and value.strip():
                    os.environ.setdefault(key.strip(), value.strip().strip("'\""))


def child_env() -> dict:
    env = {k: v for k, v in os.environ.items() if not k.startswith("DISCORD_")}
    env["PYTHONIOENCODING"] = "utf-8"
    if env.get("ANTHROPIC_API_KEY") and env.get("CHANDA_ALLOW_API_KEY") != "1":
        env.pop("ANTHROPIC_API_KEY")  # in -p mode an API key outranks the subscription and would be billed
    return env


def stop(p: subprocess.Popen) -> None:
    for sig, grace in ((signal.SIGTERM, 10), (signal.SIGKILL, 5)):
        with contextlib.suppress(ProcessLookupError):
            os.killpg(p.pid, sig)
        try:
            p.wait(grace)
            break
        except subprocess.TimeoutExpired:
            continue
    with contextlib.suppress(ProcessLookupError):
        os.killpg(p.pid, signal.SIGKILL)


def run(argv: list[str], minutes: float, stdin: str = "", env: dict | None = None) -> tuple[str, str, int, bool]:
    p = subprocess.Popen(argv, cwd=ROOT, env=env or child_env(), stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, start_new_session=True)
    try:
        o, e = p.communicate(stdin.encode("utf-8"), timeout=minutes * 60)
        timed_out = False
    except subprocess.TimeoutExpired:
        stop(p)
        o, e = p.communicate()
        timed_out = True
    dec = lambda b: (b or b"").decode("utf-8", errors="replace")
    return dec(o), dec(e), -1 if timed_out else p.returncode, timed_out


def py(argv: list[str], minutes: float = 10) -> list[str]:
    o, e, code, _ = run([sys.executable, "-I", str(PIPELINE)] + argv, minutes)
    for w in (x for x in e.splitlines() if x.startswith("warning: ")):
        log(f"pipeline {w}")
    if code != 0:
        tail = ([x for x in e.splitlines() if x.strip()] or ["no output"])[-1]
        raise RuntimeError(f"pipeline '{argv[0]}' failed (exit {code}): {tail}")
    return [x for x in o.splitlines() if x.strip()]


def find_claude() -> str:
    for c in (shutil.which("claude"), Path.home() / ".local" / "bin" / "claude", Path.home() / ".claude" / "local" / "claude"):
        if c and Path(c).exists():
            return str(c)
    raise RuntimeError("cannot find the claude executable (install: curl -fsSL https://claude.ai/install.sh | bash)")


def post(text: str) -> None:
    o, e, code, _ = run([sys.executable, "-I", str(POSTER), "--stdin"], 3, text, dict(os.environ))
    if code == 1:
        log(f"discord post failed: {(e.strip().splitlines() or ['no output'])[-1]}")


def notify(key: str, title: str, text: str) -> None:
    today = dt.date.today().isoformat()
    try:
        sent = json.loads(ALERTS.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        sent = {}
    if sent.get(key) == today:
        return
    sent[key] = today
    with contextlib.suppress(OSError):
        cp.write_text(ALERTS, json.dumps(sent, indent=1))
    log(f"ALERT {title}: {text}")
    post(f"⚠️ **{title}**\n{text}")


def systemctl(*argv: str) -> subprocess.CompletedProcess:
    return subprocess.run(["systemctl", "--user", *argv], capture_output=True, text=True)


def next_timer_run() -> dt.datetime | None:
    parts = systemctl("show", TIMER, "-p", "NextElapseUSecRealtime", "--value").stdout.split()
    try:
        return dt.datetime.strptime(" ".join(parts[1:3]), "%Y-%m-%d %H:%M:%S")
    except (ValueError, IndexError):
        return None


def resume_after(until_iso: str) -> None:
    until, regular = cp.parse_time(until_iso), next_timer_run()
    if not until or not regular or until >= regular - dt.timedelta(minutes=10) or not shutil.which("systemd-run"):
        return
    for unit in (f"{RESUME}.timer", f"{RESUME}.service"):
        systemctl("stop", unit)
        systemctl("reset-failed", unit)
    r = subprocess.run(["systemd-run", "--user", f"--unit={RESUME}", f"--on-calendar={until:%Y-%m-%d %H:%M:%S}",
                        "--timer-property=AccuracySec=1min", "systemctl", "--user", "start", SERVICE], capture_output=True, text=True)
    log(f"scheduled a one-off resume run at {until:%Y-%m-%d %H:%M}, right after the limit resets" if r.returncode == 0
        else f"could not schedule a resume run: {r.stderr.strip()[:200]}")


def short(path: str) -> str:
    return str(path or "?").rstrip("/").split("/")[-1]


def findings(units: list[str]) -> str:
    lines = []
    for unit in units:
        if unit.startswith("review-"):
            packet = unit.removeprefix("review-")
            names = {r.get("id"): r.get("name", "") for r in cp.read_jsonl(cp.REVIEW / f"packet-{packet}.jsonl")}
            vs = cp.read_jsonl(cp.REVIEW / f"review-{packet}.jsonl")
            c = Counter(v.get("verdict") for v in vs)
            lines.append(f"**{unit}** · {cp.AGENTS.get(packet[:2], 'specialist')}: {c['confirm']} confirmed, {c['revise']} revised, "
                         f"{c['reject']} rejected, {c['add']} new")
            for v in [v for v in vs if v.get("verdict") == "add"][:3]:
                r = v.get("record") or {}
                lines.append(f"  + {r.get('name', '?')} ({short(r.get('a'))} ↔ {short(r.get('b'))})")
            for v in [v for v in vs if v.get("verdict") == "reject"][:2]:
                lines.append(f"  − {names.get(v.get('id')) or v.get('id')}: {str(v.get('reason', ''))[:160]}")
        else:
            batch = cp.read_jsonl(cp.DISC / f"batch-{unit.removeprefix('discover-')}.jsonl")
            lines.append(f"**{unit}**: {len(batch)} connections")
            lines += [f"  + {r.get('name')} ({short(r.get('a'))} ↔ {short(r.get('b'))})" for r in batch if r.get("strength") == 3][:3]
    status = py(["status", "-n", "0"])
    progress = next((x for x in status if x.startswith("review:")), status[0] if status else "")
    return "\n".join([f"🔭 **Chanda pipeline** · {progress}"] + lines)


def reap_orphans() -> None:
    me = os.getpgrp()
    for proc in Path("/proc").iterdir():
        if not proc.name.isdigit():
            continue
        try:
            text = (proc / "cmdline").read_bytes().replace(b"\0", b" ").decode("utf-8", errors="replace")
            same_dir = Path(os.readlink(proc / "cwd")) == ROOT
            pgid = os.getpgid(int(proc.name))
        except (OSError, ProcessLookupError):
            continue
        if "claude" in text and all(s in text for s in SIGNATURE) and same_dir and pgid != me:
            with contextlib.suppress(ProcessLookupError, PermissionError):
                os.killpg(pgid, signal.SIGKILL)
                log(f"killed an orphaned unit session left by a dead run (pid {proc.name})")


def work(units: int, dry: bool) -> int:
    claude, env = find_claude(), child_env()
    if os.environ.get("ANTHROPIC_API_KEY") and "ANTHROPIC_API_KEY" not in env:
        log("ignoring ANTHROPIC_API_KEY so units use the subscription (set CHANDA_ALLOW_API_KEY=1 to bill the API instead)")
    if not dry:
        reap_orphans()
        for line in py(["recover"]):
            log(line)
    todo, changed, done = [], False, []
    for line in py(["next", "-n", str(units)] + (["--ignore-wait"] if dry else []), 30):
        f = line.split("\t")
        if f[0] == "UNIT":
            todo.append(f)
        elif f[0] == "INFO":
            log(f[1])
            changed = True
        elif f[0] == "WAIT":
            log(f"waiting: {f[1]}")
        elif f[0] == "CAPPED":
            log("daily unit cap reached; resuming tomorrow")
        elif f[0] == "BLOCKED":
            log(f"blocked: {f[1]}")
        elif f[0] == "HANDOFF":
            log(f"handoff: {f[1]}")
            notify("handoff", "Chanda pipeline is gated to another machine", f[1])
            return 0
        elif f[0] == "DONE":
            log("pipeline finished; disabling the timer")
            notify("done", "Chanda: connection pipeline finished",
                   f"{len(cp.read_jsonl(cp.REGISTRY))} connections in connections/registry.jsonl; the map is connections/map.html.")
            if not dry:
                systemctl("disable", "--now", TIMER)
            return 0
        else:
            log(f"unexpected planner output: {line}")
    for f in todo:
        unit, model, effort, budget, timeout = f[1], f[2], f[3], f[4], float(f[5])
        prompt_file = PIPE / "work" / f"{unit}.prompt.md"
        try:
            py(["prompt", unit, "--out", str(prompt_file)])
        except RuntimeError as exc:
            log(f"{unit}: could not build its prompt ({exc}); counting a failed attempt")
            if not dry:
                py(["mark", unit, "running"])
                py(["mark", unit, "failed", "--note", "prompt build failed"])
            continue
        prompt = prompt_file.read_text(encoding="utf-8")
        if dry:
            log(f"DRY {unit} model={model} effort={effort} budget=${budget} timeout={timeout:g}min :: {len(prompt)} chars in {prompt_file}")
            continue
        py(["mark", unit, "running"])
        argv = [claude, "-p", "--permission-mode", "dontAsk", "--no-session-persistence", "--output-format", "json", *LEAN]
        argv += ["--model", model] if model else []
        argv += ["--effort", effort] if effort else []
        argv += ["--max-budget-usd", budget] if budget else []
        argv += ["--allowedTools", "Read", "Grep", "Glob"]
        log(f"start {unit}" + (f" on {model}" if model else "") + (f" at {effort} effort" if effort else ""))
        o, e, code, timed_out = run(argv, timeout, prompt, env)
        out_file, err_file = PIPE / "work" / f"{unit}.out.txt", PIPE / "work" / f"{unit}.err.txt"
        cp.write_text(out_file, o)
        cp.write_text(err_file, e)
        if timed_out:
            log(f"{unit} ran past {timeout:g} min; killed")
        v = ((py(["ingest", unit, str(out_file), "--err", str(err_file)] + (["--timed-out"] if timed_out else [])) or ["ERROR"])[-1]
             .split("\t") + ["", ""])
        log(f"{v[1] or v[0]} (exit {code})")
        if v[0] == "OK":
            changed = True
            done.append(unit)
        elif v[0] == "LIMIT":
            log(f"stopped by a usage limit; cooling down until {v[2]}")
            resume_after(v[2])
            break
        elif v[0] == "AUTH":
            notify("auth", "Chanda: Claude sign-in expired", "On the server run `claude setup-token` and put the token in "
                   "~/.config/chanda/env as CLAUDE_CODE_OAUTH_TOKEN; the next run resumes.")
            break
        elif v[0] == "TRANSIENT":
            log(f"transient API trouble; the pipeline waits until {v[2]}")
            break
    if dry:
        return 0
    if changed:
        try:
            for line in py(["snapshot"], 20):
                log(line)
        except RuntimeError as exc:
            log(f"snapshot failed: {exc}")
            notify("snapshot", "Chanda: snapshot failed", str(exc))
    if done:
        post(findings(done))
    for a in py(["doctor", "--alerts"]):
        x = a.split("\t")
        if x[0] == "ALERT" and len(x) > 2:
            notify(x[1], "Chanda pipeline needs attention", x[2])
    return 0


def one_run(units: int, dry: bool) -> int:
    PIPE.mkdir(parents=True, exist_ok=True)
    if LOG.exists() and LOG.stat().st_size > 2 * 2 ** 20:
        os.replace(LOG, LOG.with_name("runs.log.1"))
    lock = LOCK.open("a")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        log("another run is active; exiting")
        return 0
    try:
        cp.write_text(LOCK_INFO, f"pid {os.getpid()} since {dt.datetime.now():%Y-%m-%dT%H:%M:%S}" + (" (dry run)" if dry else ""))
        return work(units, dry)
    except Exception as exc:
        msg = f"runner error: {exc}"
        with contextlib.suppress(Exception):
            log(msg)
        with contextlib.suppress(Exception):
            notify("runner-error", "Chanda pipeline failed", msg)
        return 1
    finally:
        LOCK_INFO.unlink(missing_ok=True)
        lock.close()


def health(test_discord: bool) -> int:
    rows = []

    def check(level: str, msg: str) -> None:
        rows.append(level)
        print(f"{level:4}  {msg}", flush=True)

    check("OK" if sys.version_info >= (3, 9) else "FAIL", f"python {sys.version.split()[0]} at {sys.executable}")
    check("OK" if shutil.which("python") else "WARN", "`python` is on PATH" if shutil.which("python") else
          "`python` is missing, and CLAUDE.md, agents and skills call `python -I scripts/physlib.py`: sudo apt install python-is-python3")
    try:
        claude = find_claude()
        version = subprocess.run([claude, "--version"], capture_output=True, text=True, timeout=60).stdout.strip()
        check("OK", f"claude {version} at {claude}")
    except (RuntimeError, OSError, subprocess.TimeoutExpired) as exc:
        check("FAIL", str(exc))
    creds = Path.home() / ".claude" / ".credentials.json"
    if os.environ.get("CLAUDE_CODE_OAUTH_TOKEN"):
        check("OK", "CLAUDE_CODE_OAUTH_TOKEN is set (long-lived token for the pipeline)")
    elif creds.exists():
        check("WARN", "the pipeline uses the interactive login, which expires; prefer `claude setup-token` -> ~/.config/chanda/env")
    else:
        check("FAIL", "no Claude sign-in: run `claude setup-token` and put CLAUDE_CODE_OAUTH_TOKEN=... in ~/.config/chanda/env")
    if os.environ.get("ANTHROPIC_API_KEY"):
        check("WARN", "ANTHROPIC_API_KEY is set: the runner drops it for units; unset it so interactive sessions use the subscription")
    if ENV_FILE.exists() and ENV_FILE.stat().st_mode & 0o077:
        check("WARN", f"{ENV_FILE} is readable by others: chmod 600 {ENV_FILE}")
    if shutil.which("systemctl"):
        enabled, active = systemctl("is-enabled", TIMER).stdout.strip(), systemctl("is-active", TIMER).stdout.strip()
        nxt = next_timer_run()
        check("OK" if enabled == "enabled" and active == "active" else "WARN",
              f"timer {TIMER}: {enabled or 'missing'}, {active or 'inactive'}" + (f", next run {nxt:%Y-%m-%d %H:%M}" if nxt else "") +
              ("" if enabled == "enabled" else " (bash scripts/server/setup.sh installs it)"))
        result = systemctl("show", SERVICE, "-p", "Result", "--value").stdout.strip()
        if result and result != "success":
            check("WARN", f"last pipeline service result: {result} (journalctl --user -u {SERVICE} -n 50)")
        if systemctl("is-active", f"{RESUME}.timer").stdout.strip() == "active":
            check("OK", "a one-off resume run is booked for after the usage-limit reset")
        linger = subprocess.run(["loginctl", "show-user", os.environ.get("USER", ""), "-p", "Linger", "--value"],
                                capture_output=True, text=True).stdout.strip()
        check("OK" if linger == "yes" else "WARN", "lingering is on: services run without a login" if linger == "yes" else
              f"lingering is off, so runs stop when you log out: sudo loginctl enable-linger {os.environ.get('USER', '$USER')}")
        agent = systemctl("is-active", AGENT).stdout.strip()
        check("OK" if agent == "active" else "WARN", f"Discord agent session {AGENT}: {agent or 'missing'}" +
              ("" if agent == "active" else " (see docs/SERVER.md, step 5)"))
    else:
        check("WARN", "systemctl not found: schedule `python3 -I scripts/connections_runner.py` yourself")
    o, e, code, _ = run([sys.executable, "-I", str(POSTER), "--test" if test_discord else "--check"], 2, "", dict(os.environ))
    check({0: "OK", 2: "WARN"}.get(code, "FAIL"), (o.strip() or e.strip() or "discord poster gave no output").splitlines()[-1])
    with LOCK.open("a") as fh:
        try:
            fcntl.flock(fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
            if LOCK_INFO.exists():
                check("OK", "run.lock is a leftover from a dead run; harmless, the next run replaces it")
        except BlockingIOError:
            check("OK", "a run is active now: " + (LOCK_INFO.read_text(encoding="utf-8").strip() if LOCK_INFO.exists() else "?"))
    print("--- pipeline doctor", flush=True)
    o, e, code, _ = run([sys.executable, "-I", str(PIPELINE), "doctor"], 5)
    print(o.rstrip() or e.rstrip(), flush=True)
    return 1 if "FAIL" in rows or code else 0


def main() -> int:
    with contextlib.suppress(AttributeError):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="connections_runner", description=__doc__)
    ap.add_argument("--units", type=int, default=0, help="units this run (default: units_per_run)")
    ap.add_argument("--dry-run", action="store_true", help="build prompts and show what would run")
    ap.add_argument("--health", action="store_true", help="check timer, sign-in, executables, Discord, lock and pipeline")
    ap.add_argument("--test-discord", action="store_true", help="with --health: post a test message")
    args = ap.parse_args()
    load_env()
    return health(args.test_discord) if args.health else one_run(args.units, args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
