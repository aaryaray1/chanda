#!/usr/bin/env python3
"""Score the registered glitch forecasts (G1, G2-P and the Vela head-to-head) against a fresh Jodrell Bank catalogue."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import g1_glitch_forecasts as g1  # noqa: E402
import g2_two_populations as g2  # noqa: E402
import t01_glitches as t01  # noqa: E402

SCORING = t01.HERE.parent / "data" / "scoring"
SNAP = t01.DATA / "gTable.html"
UNCONDITIONAL_P = 0.95  # G1 amendment: above this, the unconditional forecast is primary
VELA_WINDOW = (61364.0, 61506.0)


def mjd_today() -> float:
    return float((dt.date.today() - dt.date(1858, 11, 17)).days)


def first_new(old: list[tuple], new: list[tuple], after: float) -> tuple | None:
    olds = [t for t, s in old]
    return next(((t, s) for t, s in new if t > after + 2 and all(abs(t - o) > 2 for o in olds)), None)


def score_one(g_old: list[tuple], g_new: list[tuple], model: str, today: float, uncond_primary: bool) -> dict:
    times, sizes = [t for t, s in g_old], [s for t, s in g_old]
    f = g1.predictives(times, sizes, len(times) - 1)[model]
    last, w0 = times[-1], g1.SNAPSHOT_MJD - times[-1]
    nxt = first_new(g_old, g_new, last)
    r = {"last_mjd": last, "model": model, "primary": "unconditional" if uncond_primary else "conditional"}
    if nxt is None:
        r.update(status="open", survival_now=round(1 - f.cdf(max(today - last, 1e-6)), 4))
        return r
    w = nxt[0] - last
    r.update(next_mjd=nxt[0], next_size=nxt[1], pit_unconditional=round(f.cdf(w), 4))
    if uncond_primary:
        r.update(status="resolved", pit=r["pit_unconditional"])
    elif nxt[0] > g1.SNAPSHOT_MJD:
        f0 = f.cdf(w0)
        r.update(status="resolved", pit=round((f.cdf(w) - f0) / (1 - f0), 4))
    else:
        r.update(status="catalogue lag (glitch before the snapshot, missing from it); conditional forecast not applicable")
    return r


def summarise(rows: dict) -> dict:
    pits = [r["pit"] for r in rows.values() if r.get("status") == "resolved"]
    out = {"resolved": len(pits), "open": sum(r["status"] == "open" for r in rows.values()), "pits": pits}
    if len(pits) >= 3:
        out["ks_D_p"] = g1.ks_uniform(pits)
        out["in_central50"] = sum(0.25 <= u <= 0.75 for u in pits)
        out["in_central90"] = sum(0.05 <= u <= 0.95 for u in pits)
    return out


def score(old_cat: dict, new_cat: dict, today: float) -> dict:
    res: dict = {"today_mjd": today}
    reg1 = json.loads((t01.RESULTS / "G1-results.json").read_text(encoding="utf-8"))["prospective_forecasts"]
    rows = {}
    for f in reg1:
        p = f["pulsar"]
        rows[p] = score_one(old_cat[p], new_cat.get(p, []), f["model"], today, f["prob_glitch_before_snapshot"] > UNCONDITIONAL_P)
    res["G1"] = {"rows": rows, "summary": summarise(rows)}
    reg2 = json.loads((t01.RESULTS / "G2P-large-glitch-forecasts.json").read_text(encoding="utf-8"))
    old_l, new_l = g2.split(old_cat, g2.THRESHOLD)["large"], g2.split(new_cat, g2.THRESHOLD)["large"]
    rows2 = {f["pulsar"]: score_one(old_l[f["pulsar"]], new_l.get(f["pulsar"], []), f["model"], today, f["prob_large_before_snapshot"] > UNCONDITIONAL_P)
             for f in reg2["forecasts"]}
    res["G2P"] = {"rows": rows2, "summary": summarise(rows2)}
    probs = reg2["vela_head_to_head"]["probabilities"]
    hit = next((t for t, s in new_l.get("J0835-4510", []) if VELA_WINDOW[0] < t <= VELA_WINDOW[1]), None)
    outcome = True if hit else (False if today > VELA_WINDOW[1] + 30 else None)  # a month's grace for the catalogue to catch up
    res["vela_head_to_head"] = {"outcome": outcome, "glitch_mjd": hit,
                                "log_scores": None if outcome is None else {k: round(math.log(v if outcome else 1 - v), 3) for k, v in probs.items()}}
    return res


def selftest() -> None:
    old = t01.parse_jbo(SNAP.read_text(encoding="utf-8", errors="replace"))
    new = {p: list(g) for p, g in old.items()}
    new["J0835-4510"].append((61400.0, 2000.0))
    new["J0534+2200"].append((61500.0, 5.0))
    r = score(old, new, 61520.0)
    v = r["vela_head_to_head"]
    assert v["outcome"] is True and v["glitch_mjd"] == 61400.0 and v["log_scores"]["GR25_split_normal"] > v["log_scores"]["M0"], v
    assert r["G1"]["rows"]["J0835-4510"]["status"] == "resolved" and r["G1"]["rows"]["J0534+2200"]["status"] == "resolved", r["G1"]["rows"]["J0835-4510"]
    assert r["G2P"]["rows"]["J0835-4510"]["status"] == "resolved" and 0 <= r["G2P"]["rows"]["J0835-4510"]["pit"] <= 1
    r0 = score(old, old, 61520.0)
    assert r0["G1"]["summary"]["resolved"] == 0 and r0["vela_head_to_head"]["outcome"] is None
    print("selftest OK", r["G2P"]["rows"]["J0835-4510"]["pit"], v["log_scores"])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("cmd", choices=["selftest", "run"])
    ap.add_argument("--catalogue", help="a fresh gTable.html; default: fetch the live catalogue into data/scoring/")
    args = ap.parse_args()
    if args.cmd == "selftest":
        selftest()
        return 0
    if args.catalogue:
        path = Path(args.catalogue)
    else:
        path = SCORING / f"gTable-{dt.date.today().isoformat()}.html"
        t01.fetch(t01.JBO_URL, path)
    raw = path.read_bytes()
    old = t01.parse_jbo(SNAP.read_text(encoding="utf-8", errors="replace"))
    res = {"catalogue": str(path), "sha256": hashlib.sha256(raw).hexdigest(),
           **score(old, t01.parse_jbo(raw.decode("utf-8", errors="replace")), mjd_today())}
    out = t01.RESULTS / f"scoring-{dt.date.today().isoformat()}.json"
    out.write_text(json.dumps(res, indent=1, default=float), encoding="utf-8")
    for k in ("G1", "G2P"):
        s = res[k]["summary"]
        print(f"{k}: {s['resolved']} resolved, {s['open']} open", {kk: v for kk, v in s.items() if kk not in ("resolved", "open")})
        for p, r in res[k]["rows"].items():
            if r["status"] != "open":
                print(f"   {p:12} {r['status']} next {r.get('next_mjd')} pit {r.get('pit')} (unconditional {r.get('pit_unconditional')})")
    print("Vela head-to-head:", json.dumps(res["vela_head_to_head"]))
    print(f"T04 and T02 have their own runs: t04_forecast_scorecard.py run --catalogue {path} --snapshot-mjd {mjd_today():.0f}; t02_forward_persistence.py run")
    return 0


if __name__ == "__main__":
    sys.exit(main())
