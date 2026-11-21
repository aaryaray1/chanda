#!/usr/bin/env python3
"""G2: are large glitches predictable and small glitches Poisson? The G1 forecast competition run separately on each size class (pre-registered)."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import g1_glitch_forecasts as g1  # noqa: E402
import t01_glitches as t01  # noqa: E402

THRESHOLD = 100.0  # Δν/ν = 1e-7 in units of 1e-9
MIN_CLASS = 8
SEED = 20261122


def split(cat: dict, thr: float) -> dict:
    return {"large": {p: [x for x in g if x[1] is not None and x[1] >= thr] for p, g in cat.items()},
            "small": {p: [x for x in g if x[1] is not None and x[1] < thr] for p, g in cat.items()}}


def run_class(sub: dict, min_n: int) -> tuple[dict, dict]:
    sel = {p: g for p, g in sub.items() if len(g) >= min_n}
    per = {p: g1.backtest(g) for p, g in sel.items()}
    med = {p: float(np.median([math.log10(s) for t, s in g])) for p, g in sel.items()}
    return per, ({**g1.evaluate(per, med), "descriptives": {p: g1.descriptives(g) for p, g in sel.items()}} if per else {})


def contrast(per_l: dict, per_s: dict) -> dict:
    rng = np.random.default_rng(SEED)
    ml = np.array([np.mean([r["ls_M1"] - r["ls_M0"] for r in rows]) for rows in per_l.values()])
    ms = np.array([np.mean([r["ls_M1"] - r["ls_M0"] for r in rows]) for rows in per_s.values()])
    boot = ml[rng.integers(0, len(ml), (g1.N_BOOT, len(ml)))].mean(1) - ms[rng.integers(0, len(ms), (g1.N_BOOT, len(ms)))].mean(1)
    both = sorted(set(per_l) & set(per_s))
    within = {p: round(float(np.mean([r["ls_M1"] - r["ls_M0"] for r in per_l[p]]) - np.mean([r["ls_M1"] - r["ls_M0"] for r in per_s[p]])), 4) for p in both}
    return {"difference": float(ml.mean() - ms.mean()), "lower95": float(np.quantile(boot, 0.05)), "upper95": float(np.quantile(boot, 0.95)),
            "within_pulsar_large_minus_small": within}


def sign_p(k: int, n: int) -> float:
    return sum(math.comb(n, i) for i in range(k, n + 1)) / 2 ** n


def analyse(cat: dict, thr: float, min_n: int) -> dict:
    cls = split(cat, thr)
    per_l, ev_l = run_class(cls["large"], min_n)
    per_s, ev_s = run_class(cls["small"], min_n)
    out = {"threshold_1e-9": thr, "min_per_class": min_n, "large": ev_l, "small": ev_s}
    if per_l and per_s:
        out["H7_contrast_IG_M1_M0_large_minus_small"] = contrast(per_l, per_s)
    if ev_l:
        slopes = [d["slope_logwait_on_logsize_full"] for d in ev_l["descriptives"].values() if math.isfinite(d["slope_logwait_on_logsize_full"])]
        k = sum(s > 0 for s in slopes)
        out["H8_large_class_slopes"] = {"positive": k, "n": len(slopes), "sign_test_p_one_sided": sign_p(k, len(slopes))}
    out["backtest_rows"] = {"large": per_l, "small": per_s}
    return out


def selftest() -> None:
    rng = np.random.default_rng(3)
    cat = {}
    for i in range(7):
        tl = np.cumsum(rng.lognormal(math.log(900), 0.2, 15))
        ts = np.sort(rng.uniform(0, tl[-1], 15))
        cat[f"S{i}"] = sorted([(float(t), 1000.0) for t in tl] + [(float(t), 5.0) for t in ts])
    res = analyse(cat, THRESHOLD, MIN_CLASS)
    il, is_ = res["large"]["information_gain"]["M1|M0"], res["small"]["information_gain"]["M1|M0"]
    assert il["pulsar_averaged_lower95"] > 0 and is_["pulsar_averaged"] < 0.05, (il, is_)
    assert res["H7_contrast_IG_M1_M0_large_minus_small"]["lower95"] > 0, res["H7_contrast_IG_M1_M0_large_minus_small"]
    assert abs(sign_p(7, 7) - 1 / 128) < 1e-12 and abs(sign_p(6, 7) - 8 / 128) < 1e-12
    print("selftest OK", round(il["pulsar_averaged"], 3), round(is_["pulsar_averaged"], 3))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("cmd", choices=["selftest", "run"])
    ap.add_argument("--threshold", type=float, default=THRESHOLD, help="registered: 100 (1e-7); sensitivity: 500")
    ap.add_argument("--min-per-class", type=int, default=MIN_CLASS, help="registered: 8; sensitivity: 6")
    args = ap.parse_args()
    if args.cmd == "selftest":
        selftest()
        return 0
    raw = (t01.DATA / "gTable.html").read_bytes()
    res = {"catalogue_sha256": hashlib.sha256(raw).hexdigest(), **analyse(t01.parse_jbo(raw.decode("utf-8", errors="replace")), args.threshold, args.min_per_class)}
    tag = "" if (args.threshold, args.min_per_class) == (THRESHOLD, MIN_CLASS) else f"-thr{int(args.threshold)}-min{args.min_per_class}"
    (t01.RESULTS / f"G2-results{tag}.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
    for c in ("large", "small"):
        if res[c]:
            ig = res[c]["information_gain"]
            print(c, res[c]["pulsars"], "pulsars", res[c]["forecasts"], "forecasts")
            for k in ("M1|M0", "M3|M1"):
                v = ig[k]
                print(f"  {k}: avg {v['pulsar_averaged']:+.3f} [{v['pulsar_averaged_ci90'][0]:+.3f}, {v['pulsar_averaged_ci90'][1]:+.3f}] pooled {v['pooled']:+.3f} per {v['per_pulsar']}")
            h = res[c]["H4_calibration_M1"]
            print(f"  calibration KS p {h['ks_p']:.3f}, central50 {h['in_central50']}/{h['n']}, central90 {h['in_central90']}/{h['n']}")
    print("H7", json.dumps(res.get("H7_contrast_IG_M1_M0_large_minus_small")))
    print("H8", json.dumps(res.get("H8_large_class_slopes")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
