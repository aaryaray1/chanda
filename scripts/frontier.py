#!/usr/bin/env python3
"""Frontier search: rank unlinked cross-branch topic pairs by link prediction over the connection registry, then measure on arXiv how charted each pair is."""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
import urllib.parse
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import physlib  # noqa: E402

ROOT = physlib.ROOT
REGISTRY = ROOT / "connections" / "registry.jsonl"
OUT = ROOT / "connections" / "frontier"
CANDIDATES = OUT / "candidates.jsonl"
COUNTS = OUT / "arxiv-counts.json"
WEIGHT = {"identity": 1.0, "duality": 1.0, "mechanism": 0.9, "shared object": 0.7, "method transfer": 0.6, "analogy": 0.4, "historical": 0.1}


def load_index() -> dict:
    return {n["path"]: n for n in json.loads((ROOT / "library" / "index.json").read_text(encoding="utf-8"))}


def lineage(path: str) -> list[str]:
    parts = path.split("/")
    return ["/".join(parts[:i]) for i in range(1, len(parts) + 1)]


def mine(fields: list[str], top: int, exclude: list[str] | None = None) -> list[dict]:
    index = load_index()
    recs = [json.loads(l) for l in REGISTRY.read_text(encoding="utf-8").splitlines() if l.strip()]
    adj, linked = defaultdict(list), set()
    for r in recs:
        if "contested" in (r.get("review") or ""):
            continue
        w = WEIGHT.get(r["kind"], 0.3) * r["strength"] / 3 * (0.7 if r["confidence"] == "proposed" else 1.0)
        adj[r["a"]].append((r["b"], w, r))
        adj[r["b"]].append((r["a"], w, r))
        linked.add(frozenset((r["a"], r["b"])))
    score, via = defaultdict(float), defaultdict(list)
    for b, nbrs in adj.items():
        damp = 1 / math.log(2 + len(nbrs))  # Adamic–Adar: a hub topic says little about any one pair
        for i, (x, wx, rx) in enumerate(nbrs):
            for y, wy, ry in nbrs[i + 1:]:
                if x == y or x[:2] == y[:2] or (fields and {x[:2], y[:2]} != set(fields)) or {x[:2], y[:2]} & set(exclude or []):
                    continue
                a, c = sorted((x, y))
                s = wx * wy * damp
                score[(a, c)] += s
                via[(a, c)].append((s, b, rx["name"], ry["name"]))
    out = []
    for (a, c), s in sorted(score.items(), key=lambda kv: -kv[1]):
        if any(frozenset((p, q)) in linked for p in lineage(a) for q in lineage(c)):
            continue
        hops = sorted(via[(a, c)], reverse=True)
        out.append({"a": a, "c": c, "score": round(s, 4), "bridges": len({h[1] for h in hops}),
                    "a_title": index.get(a, {}).get("title", a), "c_title": index.get(c, {}).get("title", c),
                    "via": [{"b": h[1], "a_link": h[2], "c_link": h[3]} for h in hops[:3]]})
        if len(out) >= top:
            break
    return out


def phrases(path: str, index: dict) -> list[str]:
    q = index.get(path, {}).get("query") or index.get(path, {}).get("title") or path.rsplit("/", 1)[-1].replace("-", " ")
    return [p.strip().strip('"') for p in q.split(";") if p.strip()][:3]


def arxiv_count(query: str, cache: dict) -> int:
    if query not in cache:
        url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"search_query": query, "max_results": 1})  # 0 gives HTTP 500
        try:
            m = re.search(r"<opensearch:totalResults[^>]*>(\d+)<", physlib.http_get(url, accept="application/atom+xml"))
        except (OSError, physlib.BudgetExhausted) as exc:
            print(f"  arXiv query failed ({exc}); skipped", flush=True)
            return -1
        cache[query] = int(m.group(1)) if m else -1
        COUNTS.write_text(json.dumps(cache, indent=1), encoding="utf-8")
    return cache[query]


def novelty(cands: list[dict], n: int) -> None:
    index = load_index()
    cache = json.loads(COUNTS.read_text(encoding="utf-8")) if COUNTS.exists() else {}
    side = lambda p: "(" + " OR ".join(f'abs:"{x}"' for x in phrases(p, index)) + ")"
    for c in cands[:n]:
        na, nc = arxiv_count(side(c["a"]), cache), arxiv_count(side(c["c"]), cache)
        both = arxiv_count(f"{side(c['a'])} AND {side(c['c'])}", cache)
        if min(na, nc, both) < 0:
            continue
        c["arxiv"] = {"a": na, "c": nc, "both": both, "overlap": round(both / max(1, min(na, nc)), 4)}
        print(f"  {both:5d} joint / {na:6d} · {nc:6d}  {c['a_title']} ↔ {c['c_title']}", flush=True)
        save(cands)


def save(cands: list[dict]) -> None:
    CANDIDATES.write_text("".join(json.dumps(c, ensure_ascii=False) + "\n" for c in cands), encoding="utf-8")


def show(cands: list[dict]) -> None:
    for i, c in enumerate(cands, 1):
        ax = c.get("arxiv")
        tag = f"arXiv joint {ax['both']} (overlap {ax['overlap']:.3f})" if ax else "arXiv not checked"
        print(f"{i:2d}. [{c['a'][:2]}×{c['c'][:2]}] {c['a_title']} ↔ {c['c_title']} · score {c['score']} · {c['bridges']} bridge(s) · {tag}")
        for v in c["via"][:2]:
            print(f"      via {v['b'].rsplit('/', 1)[-1]}: “{v['a_link']}” + “{v['c_link']}”")


def main() -> int:
    with __import__("contextlib").suppress(AttributeError):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="frontier", description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("mine", help="rank unlinked cross-branch pairs and save them")
    p.add_argument("--fields", nargs=2, default=[], help="restrict to one branch pair, e.g. 05 08")
    p.add_argument("-n", type=int, default=60)
    p.add_argument("--exclude", nargs="*", default=[], help="skip pairs touching these branches, e.g. 00 (method topics are rarely named in abstracts)")
    p = sub.add_parser("novelty", help="add arXiv co-occurrence counts to the top saved candidates (3 s per query)")
    p.add_argument("-n", type=int, default=20)
    sub.add_parser("show", help="print the saved candidates")
    args = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    if args.cmd == "mine":
        cands = mine(args.fields, args.n, args.exclude)
    else:
        cands = [json.loads(l) for l in CANDIDATES.read_text(encoding="utf-8").splitlines() if l.strip()]
        if args.cmd == "novelty":
            novelty(cands, args.n)
    save(cands)
    show(cands)
    return 0


if __name__ == "__main__":
    sys.exit(main())
