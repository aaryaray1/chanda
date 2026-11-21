#!/usr/bin/env python3
"""Post-hoc null calibrations for G1-G3, added after the referee (2026-11-21): Poisson-null IG, size-shuffle null, dead-time view of G3."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import g1_glitch_forecasts as g1  # noqa: E402
import g2_two_populations as g2  # noqa: E402
import g3_aftershocks as g3  # noqa: E402
import t01_glitches as t01  # noqa: E402

SEED = 20261124
N_SIM = 1000


def ig_avg(per: dict, a: str, b: str) -> float:
    return float(np.mean([np.mean([r[f"ls_{a}"] - r[f"ls_{b}"] for r in rows]) for rows in per.values()]))


def poisson_null(counts: list[int], rng) -> np.ndarray:
    out = np.empty(N_SIM)
    for i in range(N_SIM):
        per = {k: g1.backtest(list(zip(np.cumsum(rng.exponential(1.0, n)).tolist(), [1.0] * n))) for k, n in enumerate(counts)}
        out[i] = ig_avg(per, "M1", "M0")  # IG is invariant to the rate, so unit-rate sequences suffice
    return out


def shuffle_null(sel: dict, rng, n_sim: int = 300) -> np.ndarray:
    out = np.empty(n_sim)
    for i in range(n_sim):
        per = {}
        for p, g in sel.items():
            s = [x[1] for x in g]
            per[p] = g1.backtest(list(zip([x[0] for x in g], rng.permutation(s).tolist())))
        out[i] = ig_avg(per, "M3", "M1")
    return out


def summary(obs: float, null: np.ndarray) -> dict:
    return {"observed": round(obs, 4), "null_mean": round(float(null.mean()), 4), "null_p05_p95": [round(float(np.quantile(null, q)), 4) for q in (0.05, 0.95)],
            "p_null_ge_observed": float((null >= obs).mean()), "n_sim": len(null)}


def waits_by_pulsar(cat: dict) -> dict:
    out = {}
    for p, g in cat.items():
        g = [(t, s) for t, s in g if s is not None and s > 0]  # G3's inclusion rule
        if len(g) >= g3.MIN_GLITCHES:
            out[p] = np.diff([t for t, s in g])
    return out


def quick_count(w: np.ndarray, d: float) -> int:
    loo = (w.sum() - w) / (len(w) - 1)
    return int(((w < g3.QUICK * loo) & (w >= d)).sum())


def deadtime(cat: dict, rng, n_sim: int = 2000) -> dict:
    W = waits_by_pulsar(cat)
    out = {}
    for d in (0, 14, 20, 30, 45, 60):
        obs = sum(quick_count(w, d) for w in W.values())
        sims = np.array([sum(quick_count(rng.exponential(w.mean(), len(w)), d) for w in W.values()) for _ in range(n_sim)])
        out[str(d)] = {"observed": obs, "poisson_mean": round(float(sims.mean()), 2), "p_le_observed": float((sims <= obs).mean())}
    per = {}
    for p in ("J0534+2200", "J0835-4510", "J0537-6910", "J1740-3015"):
        w = W[p]
        sims = [quick_count(rng.exponential(w.mean(), len(w)), 0) for _ in range(n_sim)]
        per[p] = {"observed": quick_count(w, 0), "poisson_mean": round(float(np.mean(sims)), 2), "quick_window_days": round(float(g3.QUICK * w.mean()), 1)}
    return {"by_min_wait_days": out, "by_pulsar": per}


def main() -> int:
    rng = np.random.default_rng(SEED)
    cat = t01.parse_jbo((t01.DATA / "gTable.html").read_text(encoding="utf-8", errors="replace"))
    res = {"note": "post hoc, after the G1-G3 referee; not part of any pre-registration"}
    sel = {p: g for p, g in cat.items() if len(g) >= g1.MIN_GLITCHES}
    per = {p: g1.backtest(g) for p, g in sel.items()}
    res["G1_any_size"] = summary(ig_avg(per, "M1", "M0"), poisson_null([len(g) for g in sel.values()], rng))
    no20 = {p: v for p, v in per.items() if p != "J1420-6048"}
    res["G1_any_size_without_J1420"] = summary(ig_avg(no20, "M1", "M0"), poisson_null([len(g) for p, g in sel.items() if p != "J1420-6048"], rng))
    cls = g2.split(cat, g2.THRESHOLD)
    for c in ("large", "small"):
        s2 = {p: g for p, g in cls[c].items() if len(g) >= g2.MIN_CLASS}
        pc = {p: g1.backtest(g) for p, g in s2.items()}
        res[f"G2_{c}"] = summary(ig_avg(pc, "M1", "M0"), poisson_null([len(g) for g in s2.values()], rng))
        if c == "large":
            res["G2_large_without_J1420"] = summary(ig_avg({p: v for p, v in pc.items() if p != "J1420-6048"}, "M1", "M0"),
                                                    poisson_null([len(g) for p, g in s2.items() if p != "J1420-6048"], rng))
        if c == "small":
            res["G2_small_size_shuffle_IG_M3_M1"] = summary(ig_avg(pc, "M3", "M1"), shuffle_null(s2, rng))
    res["G3_deadtime"] = deadtime(cat, rng)
    (t01.RESULTS / "G-nulls-posthoc.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
    print(json.dumps(res, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
