#!/usr/bin/env python3
"""G3: do pulsar glitches have aftershocks? Quick follow-up glitches versus the size of the glitch before them (pre-registered)."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import t01_glitches as t01  # noqa: E402

MIN_GLITCHES = 5
QUICK = 0.1  # a follow-up within 10% of the pulsar's typical wait
SEED = 20261123
N_PERM = 20000
N_NULL = 5000


def pairs(cat: dict, min_n: int, exclude: tuple = ()) -> dict:
    """Per pulsar: (size percentile of the glitch, wait to the next / leave-one-out mean wait, size, next size)."""
    out = {}
    for p, g in cat.items():
        g = [(t, s) for t, s in g if s is not None and s > 0]
        if len(g) < min_n or p in exclude:
            continue
        t = np.array([x[0] for x in g])
        s = np.array([x[1] for x in g])
        w = np.diff(t)
        loo = (w.sum() - w) / (len(w) - 1)
        ranks = np.argsort(np.argsort(s)).astype(float)
        pct = (ranks + 0.5) / len(s)
        out[p] = {"pct": pct[:-1], "u": w / loo, "size": s[:-1], "next_size": s[1:]}
    return out


def mean_pct_quick(d: dict, quick: float) -> tuple[float, int]:
    v = np.concatenate([x["pct"][x["u"] < quick] for x in d.values()])
    return (float(v.mean()) if len(v) else float("nan")), int(len(v))


def perm_test(d: dict, quick: float, rng) -> dict:
    obs, n = mean_pct_quick(d, quick)
    if n == 0:
        return {"mean_percentile": None, "n_quick": 0}
    masks = {p: x["u"] < quick for p, x in d.items()}
    sims = np.empty(N_PERM)
    for i in range(N_PERM):
        tot = 0.0
        for p, x in d.items():
            m = masks[p]
            if m.any():
                tot += rng.permutation(x["pct"])[m].sum()
        sims[i] = tot / n
    return {"mean_percentile": obs, "n_quick": n, "p_greater": float((sims >= obs - 1e-12).mean()),
            "p_less": float((sims <= obs + 1e-12).mean()), "null_mean": float(sims.mean())}


def poisson_null(d: dict, quick: float, rng) -> dict:
    obs = sum(int((x["u"] < quick).sum()) for x in d.values())
    sims = np.empty(N_NULL)
    for i in range(N_NULL):
        c = 0
        for x in d.values():
            w = rng.exponential(1.0, len(x["u"]))
            c += int((w < quick * (w.sum() - w) / (len(w) - 1)).sum())
        sims[i] = c
    return {"observed_quick": obs, "waits": sum(len(x["u"]) for x in d.values()), "poisson_mean": float(sims.mean()),
            "p_excess": float((sims >= obs).mean()), "p_deficit": float((sims <= obs).mean())}


def analyse(cat: dict, min_n: int, quick: float, exclude: tuple = ()) -> dict:
    rng = np.random.default_rng(SEED)
    d = pairs(cat, min_n, exclude)
    res = {"pulsars": len(d), "waits": sum(len(x["u"]) for x in d.values()), "quick": quick,
           "H9_size_percentile_before_quick_followups": perm_test(d, quick, rng), "H10_quick_followups_vs_poisson": poisson_null(d, quick, rng)}
    q = [(p, float(x["size"][i]), float(x["next_size"][i]), float(x["u"][i])) for p, x in d.items() for i in np.flatnonzero(x["u"] < quick)]
    res["quick_pairs"] = [{"pulsar": p, "size": a, "next_size": b, "u": round(u, 4)} for p, a, b, u in q]
    if q:
        res["H11_median_log10_size_ratio_followup_over_first"] = float(np.median([math.log10(b / a) for _, a, b, _ in q]))
        res["by_pulsar_quick_counts"] = {p: int((x["u"] < quick).sum()) for p, x in d.items() if (x["u"] < quick).any()}
    return res


def selftest() -> None:
    rng = np.random.default_rng(5)
    base, trig = {}, {}
    for i in range(30):
        t = np.cumsum(rng.exponential(500, 12))
        s = rng.lognormal(3, 2, 12)
        base[f"B{i}"] = list(zip(t.tolist(), s.tolist()))
        ev = []
        for tt, ss in zip(t, s):
            ev.append((float(tt), float(ss)))
            if ss > np.quantile(s, 0.75):
                ev.append((float(tt + rng.uniform(1, 20)), float(ss * 0.05)))
        trig[f"T{i}"] = sorted(ev)
    rb = analyse(base, MIN_GLITCHES, QUICK)["H9_size_percentile_before_quick_followups"]
    rt = analyse(trig, MIN_GLITCHES, QUICK)["H9_size_percentile_before_quick_followups"]
    assert rb["p_greater"] > 0.01 and rt["p_greater"] < 0.001 and rt["mean_percentile"] > 0.7, (rb, rt)
    print("selftest OK", round(rb["mean_percentile"], 3), round(rt["mean_percentile"], 3))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("cmd", choices=["selftest", "run"])
    args = ap.parse_args()
    if args.cmd == "selftest":
        selftest()
        return 0
    raw = (t01.DATA / "gTable.html").read_bytes()
    cat = t01.parse_jbo(raw.decode("utf-8", errors="replace"))
    res = {"catalogue_sha256": hashlib.sha256(raw).hexdigest(), "primary": analyse(cat, MIN_GLITCHES, QUICK),
           "sensitivity": {"quick_0.05": analyse(cat, MIN_GLITCHES, 0.05), "quick_0.2": analyse(cat, MIN_GLITCHES, 0.2),
                           "min_glitches_8": analyse(cat, 8, QUICK), "without_J0537": analyse(cat, MIN_GLITCHES, QUICK, ("J0537-6910",)),
                           "without_Vela": analyse(cat, MIN_GLITCHES, QUICK, ("J0835-4510",))}}
    (t01.RESULTS / "G3-results.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
    for name, r in [("primary", res["primary"])] + list(res["sensitivity"].items()):
        h9, h10 = r["H9_size_percentile_before_quick_followups"], r["H10_quick_followups_vs_poisson"]
        print(f"{name:15} pulsars {r['pulsars']} waits {r['waits']} | H9 mean pct {h9['mean_percentile']} (n={h9['n_quick']}) p> {h9.get('p_greater')} p< {h9.get('p_less')}"
              f" | H10 quick {h10['observed_quick']} vs Poisson {h10['poisson_mean']:.1f} p_excess {h10['p_excess']:.4f} p_deficit {h10['p_deficit']:.4f}"
              f" | H11 {r.get('H11_median_log10_size_ratio_followup_over_first')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
