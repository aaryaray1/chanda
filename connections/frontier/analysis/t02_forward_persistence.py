#!/usr/bin/env python3
"""T02: pre-registered, test-later check that the forward size–waiting-time correlations found in T01 persist in glitches unseen on 2026-11-20."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import t01_glitches as t01  # noqa: E402

DATA = t01.HERE.parent / "data" / "t02"
SNAPSHOT = DATA / "snapshot-2026-11-20.json"
PULSARS = ["J1341-6220", "J1413-6141", "J1048-5832", "J1801-2304"]
CONTROL = "J0537-6910"
MATCH_DAYS = 2.0
GAP_FACTOR = 5.0
MIN_PAIRS, MIN_PAIRS_DEADLINE, MIN_PER_PULSAR = 10, 6, 3
DEADLINE_MJD = 63190  # 2031-11-20
ALPHA = 0.05


def is_new(t: float, old: list[float]) -> bool:
    return all(abs(t - o) > MATCH_DAYS for o in old)


def new_pairs(g: list, old: list[float], median_wait: float) -> tuple[np.ndarray, np.ndarray]:
    xs, ws = [], []
    for (t, s), (t2, _) in zip(g, g[1:]):
        if s is None or t2 - t > GAP_FACTOR * median_wait:
            continue
        if is_new(t, old) or is_new(t2, old):
            xs.append(s)
            ws.append(t2 - t)
    return np.array(xs, float), np.array(ws, float)


def stratified(groups: list[tuple[np.ndarray, np.ndarray]], rng: np.random.Generator, b: int = t01.B_PERM) -> dict:
    zs = [(t01.zscore(t01.ranks(s)), t01.zscore(t01.ranks(w))) for s, w in groups]
    obs = sum(float(a @ c) for a, c in zs)
    n = sum(len(a) for a, _ in zs)
    sims = np.zeros(b)
    for a, c in zs:
        for start in range(0, b, 20_000):
            k = min(20_000, b - start)
            sims[start:start + k] += rng.permuted(np.tile(c, (k, 1)), axis=1) @ a
    return {"rho_pooled": obs / n, "n": n, "p_pos": (np.sum(sims >= obs - 1e-9) + 1) / (b + 1),
            "p_neg": (np.sum(sims <= obs + 1e-9) + 1) / (b + 1)}


def analyse(cat: dict, snap: dict, today_mjd: float) -> dict:
    rng = np.random.default_rng(t01.SEED + 2)
    rows, groups = [], []
    for p in PULSARS + [CONTROL]:
        s, w = new_pairs(cat.get(p, []), snap["epochs"][p], snap["median_wait"][p])
        row = {"pulsar": p, "new_pairs": len(s)}
        if len(s) >= 3:
            row["rho"] = round(t01.corr(s, w, True), 3)
        rows.append(row)
        if p in PULSARS and len(s) >= MIN_PER_PULSAR:
            groups.append((s, w))
    n = sum(len(s) for s, _ in groups)
    due = n >= MIN_PAIRS or (today_mjd >= DEADLINE_MJD and n >= MIN_PAIRS_DEADLINE)
    res = {"rows": rows, "pooled_pairs": n, "pulsars_contributing": len(groups), "due": due}
    if due and len(groups) >= 1:
        st = stratified(groups, rng)
        res["test"] = st
        res["verdict"] = "persists" if st["rho_pooled"] > 0 and st["p_pos"] < ALPHA else \
            "reversed" if st["rho_pooled"] < 0 and st["p_neg"] < ALPHA else "inconclusive"
    else:
        res["verdict"] = "insufficient data" if today_mjd >= DEADLINE_MJD else "not yet due"
    return res


def snapshot() -> int:
    cat = t01.parse_jbo((t01.DATA / "gTable.html").read_text(encoding="utf-8", errors="replace"))
    meta = json.loads((t01.DATA / "fetch.json").read_text(encoding="utf-8"))
    snap = {"catalogue_sha256": meta["jbo_sha256"], "fetched": meta["fetched"], "epochs": {}, "median_wait": {}}
    for p in PULSARS + [CONTROL]:
        g = cat[p]
        snap["epochs"][p] = [t for t, _ in g]
        snap["median_wait"][p] = float(np.median(np.diff([t for t, _ in g])))
    DATA.mkdir(parents=True, exist_ok=True)
    SNAPSHOT.write_text(json.dumps(snap, indent=1), encoding="utf-8")
    print(json.dumps({k: v for k, v in snap.items() if k != "epochs"}, indent=1))
    return 0


def selftest() -> int:
    rng = np.random.default_rng(3)
    old = {p: list(np.cumsum(rng.exponential(300, 12)) + 50000) for p in PULSARS + [CONTROL]}
    snap = {"epochs": old, "median_wait": {p: 300.0 for p in old}}
    for strength, expect in ((1.0, "persists"), (0.0, None)):
        cat = {}
        for p, ts in old.items():
            g = [(t, float(rng.lognormal(0, 1))) for t in ts]
            t = ts[-1]
            for _ in range(8):
                s = float(rng.lognormal(0, 1))
                g[-1] = (g[-1][0], s)
                t += 50 + strength * 120 * s + (1 - strength) * rng.exponential(200)
                g.append((t, float(rng.lognormal(0, 1))))
            cat[p] = g
        res = analyse(cat, snap, DEADLINE_MJD)
        print(strength, res["pooled_pairs"], res.get("test", {}).get("rho_pooled"), res["verdict"])
        if expect:
            assert res["verdict"] == expect, res
    print("selftest OK")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("cmd", choices=["snapshot", "selftest", "run"])
    args = ap.parse_args()
    if args.cmd == "snapshot":
        return snapshot()
    if args.cmd == "selftest":
        return selftest()
    import datetime as dt
    DATA.mkdir(parents=True, exist_ok=True)
    sha = t01.fetch(t01.JBO_URL, DATA / "gTable-latest.html")
    cat = t01.parse_jbo((DATA / "gTable-latest.html").read_text(encoding="utf-8", errors="replace"))
    snap = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    today = (dt.date.today() - dt.date(1858, 11, 17)).days
    res = {"run_date": dt.date.today().isoformat(), "catalogue_sha256": sha, **analyse(cat, snap, today)}
    (t01.RESULTS / "T02-results.json").write_text(json.dumps(res, indent=1, default=float), encoding="utf-8")
    print(json.dumps(res, indent=1, default=float))
    return 0


if __name__ == "__main__":
    sys.exit(main())
