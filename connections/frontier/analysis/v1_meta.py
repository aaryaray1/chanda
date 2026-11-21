#!/usr/bin/env python3
"""V1: do vortex-creep predictions of the time to the next glitch track the observed intervals? (pre-registered meta-analysis)"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
PAIRS = HERE.parent / "data" / "v1" / "pairs.json"
RESULTS = HERE.parent / "results"
SEED = 20261125
N_PERM = 20000


def spearman(x, y) -> float:
    rx, ry = np.argsort(np.argsort(x)).astype(float), np.argsort(np.argsort(y)).astype(float)
    return float(np.corrcoef(rx, ry)[0, 1])


def analyse(pairs: list[dict]) -> dict:
    rng = np.random.default_rng(SEED)
    by = {}
    for p in pairs:
        by.setdefault(p["pulsar"], []).append(p)
    big = {k: v for k, v in by.items() if len(v) >= 3}
    xs, ys, groups = [], [], []
    for k, v in big.items():
        m = math.exp(np.mean([math.log(p["t_obs"]) for p in v]))
        xs += [math.log(p["t_th"] / m) for p in v]
        ys += [math.log(p["t_obs"] / m) for p in v]
        groups += [k] * len(v)
    xs, ys, groups = np.array(xs), np.array(ys), np.array(groups)
    rho = spearman(xs, ys)
    idx = {g: np.flatnonzero(groups == g) for g in big}
    sims = np.empty(N_PERM)
    for i in range(N_PERM):
        xp = xs.copy()
        for g, ii in idx.items():
            xp[ii] = xs[rng.permutation(ii)]
        sims[i] = spearman(xp, ys)
    within = {g: round(spearman(xs[ii], ys[ii]), 3) for g, ii in idx.items()}
    em, eb, rows = [], [], []
    for k, v in by.items():
        if len(v) < 2:
            continue
        for j, p in enumerate(v):
            others = [q["t_obs"] for i, q in enumerate(v) if i != j]
            base = math.exp(np.mean(np.log(others)))
            a, b = abs(math.log(p["t_th"] / p["t_obs"])), abs(math.log(base / p["t_obs"]))
            em.append(a)
            eb.append(b)
            rows.append({"pulsar": k, "glitch": p["glitch"], "e_model": round(a, 4), "e_baseline": round(b, 4)})
    wins = sum(a < b for a, b in zip(em, eb))
    n = len(em)
    p_sign = sum(math.comb(n, i) for i in range(wins, n + 1)) / 2 ** n
    return {"H_V1": {"pairs": int(len(xs)), "pulsars": len(big), "spearman_rho": rho, "p_one_sided": float((sims >= rho - 1e-12).mean()),
                     "within_pulsar_rho": within},
            "H_V2": {"pairs": n, "model_wins": wins, "sign_test_p_one_sided": p_sign,
                     "median_error_model": float(np.median(em)), "median_error_baseline": float(np.median(eb)), "rows": rows},
            "reported_only": {k: v for k, v in by.items() if len(v) < 2}}


def selftest() -> None:
    rng = np.random.default_rng(1)
    good, bad = [], []
    for k in range(4):
        obs = rng.lognormal(math.log(800), 0.3, 8)
        good += [{"pulsar": f"P{k}", "glitch": str(i), "t_obs": float(o), "t_th": float(o * rng.lognormal(0, 0.05))} for i, o in enumerate(obs)]
        bad += [{"pulsar": f"P{k}", "glitch": str(i), "t_obs": float(o), "t_th": float(800 * rng.lognormal(0, 0.3))} for i, o in enumerate(obs)]
    rg, rb = analyse(good), analyse(bad)
    assert rg["H_V1"]["p_one_sided"] < 0.001 and rg["H_V2"]["sign_test_p_one_sided"] < 0.001, rg["H_V1"]
    assert rb["H_V1"]["p_one_sided"] > 0.01, rb["H_V1"]
    print("selftest OK", round(rg["H_V1"]["spearman_rho"], 3), round(rb["H_V1"]["spearman_rho"], 3))


def main() -> int:
    if sys.argv[1:] == ["selftest"]:
        selftest()
        return 0
    d = json.loads(PAIRS.read_text(encoding="utf-8"))
    P = d["pairs"]
    early = [{**p, "t_th": p["earliest"].get("t_th", p["t_th"]), "t_obs": p["earliest"].get("t_obs", p["t_obs"])} if "earliest" in p else p for p in P]
    res = {"primary": analyse(P), "sensitivity": {"earliest_paper": analyse(early), "drop_flagged": analyse([p for p in P if "flag" not in p]),
                                                  "vela_only": analyse([p for p in P if p["pulsar"] == "J0835-4510"]),
                                                  "without_vela": analyse([p for p in P if p["pulsar"] != "J0835-4510"])}}
    (RESULTS / "V1-results.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
    for name, r in [("primary", res["primary"])] + list(res["sensitivity"].items()):
        h1, h2 = r["H_V1"], r["H_V2"]
        print(f"{name:15} V1: rho {h1['spearman_rho']:+.3f} p {h1['p_one_sided']:.4f} (pairs {h1['pairs']}, within {h1['within_pulsar_rho']})"
              f" | V2: model wins {h2['model_wins']}/{h2['pairs']} p {h2['sign_test_p_one_sided']:.4f} median err model {h2['median_error_model']:.3f} vs base {h2['median_error_baseline']:.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
