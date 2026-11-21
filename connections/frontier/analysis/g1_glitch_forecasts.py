#!/usr/bin/env python3
"""G1: out-of-sample forecast competition for pulsar glitch waiting times (CSEP-style information gain), pre-registered."""
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

MIN_GLITCHES = 8  # pulsars in the backtest
MIN_PAST = 4  # waits needed before the first forecast
MIN_PAIRS = 5  # size-wait pairs needed before M3 departs from M1
SNAPSHOT_MJD = 61364  # 2026-11-20
SEED = 20261121
N_BOOT = 20000
N_PERM = 100000
MODELS = ("M0", "M1", "M3")


def betacf(a: float, b: float, x: float) -> float:
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    d = 1.0 / (d if abs(d) > 1e-300 else 1e-300)
    h = d
    for m in range(1, 300):
        m2 = 2 * m
        for aa in (m * (b - m) * x / ((qam + m2) * (a + m2)), -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))):
            d = 1.0 + aa * d
            d = 1.0 / (d if abs(d) > 1e-300 else 1e-300)
            c = 1.0 + aa / c
            c = c if abs(c) > 1e-300 else 1e-300
            h *= d * c
        if abs(d * c - 1.0) < 1e-14:
            break
    return h


def betai(a: float, b: float, x: float) -> float:
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    lbt = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log1p(-x)
    if x < (a + 1.0) / (a + b + 2.0):
        return math.exp(lbt) * betacf(a, b, x) / a
    return 1.0 - math.exp(lbt) * betacf(b, a, 1.0 - x) / b


def t_logpdf(x: float, df: float, loc: float, scale: float) -> float:
    z = (x - loc) / scale
    return (math.lgamma((df + 1) / 2) - math.lgamma(df / 2) - 0.5 * math.log(df * math.pi) - math.log(scale)
            - (df + 1) / 2 * math.log1p(z * z / df))


def t_cdf(x: float, df: float, loc: float, scale: float) -> float:
    z = (x - loc) / scale
    tail = 0.5 * betai(df / 2, 0.5, df / (df + z * z))
    return 1.0 - tail if z > 0 else tail


class Predictive:
    """A predictive distribution for the next waiting time w > 0 (days)."""

    def __init__(self, kind: str, **p):
        self.kind, self.p = kind, p

    def logpdf(self, w: float) -> float:
        p = self.p
        if self.kind == "lomax":
            return math.log(p["n"]) + p["n"] * math.log(p["S"]) - (p["n"] + 1) * math.log(p["S"] + w)
        return t_logpdf(math.log(w), p["df"], p["loc"], p["scale"]) - math.log(w)

    def cdf(self, w: float) -> float:
        p = self.p
        if w <= 0:
            return 0.0
        if self.kind == "lomax":
            return 1.0 - (p["S"] / (p["S"] + w)) ** p["n"]
        return t_cdf(math.log(w), p["df"], p["loc"], p["scale"])

    def quantile(self, q: float, w0: float = 0.0) -> float:
        f0 = self.cdf(w0) if w0 > 0 else 0.0
        target = f0 + q * (1.0 - f0)
        lo, hi = max(w0, 1e-6), max(w0, 1.0) * 2
        while self.cdf(hi) < target and hi < 1e9:
            hi *= 2
        for _ in range(200):
            mid = math.sqrt(lo * hi)
            lo, hi = (mid, hi) if self.cdf(mid) < target else (lo, mid)
        return math.sqrt(lo * hi)


def m0(waits: list[float]) -> Predictive:
    return Predictive("lomax", n=len(waits), S=float(sum(waits)))  # exponential waits, Jeffreys-type rate prior: posterior predictive


def m1(waits: list[float]) -> Predictive:
    y = np.log(waits)
    n = len(y)
    return Predictive("logt", df=n - 1, loc=float(y.mean()), scale=float(y.std(ddof=1)) * math.sqrt(1 + 1 / n))


def m3(waits: list[float], sizes: list[float | None], s_now: float | None) -> tuple[Predictive, bool]:
    pairs = [(math.log(s), math.log(w)) for s, w in zip(sizes, waits) if s is not None and s > 0]
    if s_now is None or s_now <= 0 or len(pairs) < MIN_PAIRS:
        return m1(waits), False
    x, y = np.array(pairs).T
    m, xbar, ybar = len(x), x.mean(), y.mean()
    sxx = float(((x - xbar) ** 2).sum())
    if sxx <= 0:
        return m1(waits), False
    b = float(((x - xbar) * (y - ybar)).sum()) / sxx
    a = ybar - b * xbar
    se = math.sqrt(float(((y - a - b * x) ** 2).sum()) / (m - 2))
    x0 = math.log(s_now)
    scale = se * math.sqrt(1 + 1 / m + (x0 - xbar) ** 2 / sxx)
    if not scale > 0:
        return m1(waits), False
    return Predictive("logt", df=m - 2, loc=a + b * x0, scale=scale, slope=b), True


def predictives(times: list[float], sizes: list[float | None], k: int) -> dict:
    waits = [times[i + 1] - times[i] for i in range(k)]
    p3, used = m3(waits, sizes[:k], sizes[k])
    return {"M0": m0(waits), "M1": m1(waits), "M3": p3, "m3_used": used}


def backtest(glitches: list[tuple]) -> list[dict]:
    times, sizes = [t for t, s in glitches], [s for t, s in glitches]
    rows = []
    for k in range(MIN_PAST, len(times) - 1):
        pr, w = predictives(times, sizes, k), times[k + 1] - times[k]
        rows.append({"origin_mjd": times[k], "wait": w, "m3_used": pr["m3_used"],
                     **{f"ls_{m}": pr[m].logpdf(w) for m in MODELS}, **{f"pit_{m}": pr[m].cdf(w) for m in MODELS}})
    return rows


def spearman(x: list[float], y: list[float]) -> float:
    rx, ry = np.argsort(np.argsort(x)).astype(float), np.argsort(np.argsort(y)).astype(float)
    return float(np.corrcoef(rx, ry)[0, 1])


def ks_uniform(u: list[float]) -> tuple[float, float]:
    u = np.sort(np.asarray(u))
    n = len(u)
    d = float(max((np.arange(1, n + 1) / n - u).max(), (u - np.arange(n) / n).max()))
    lam = (math.sqrt(n) + 0.12 + 0.11 / math.sqrt(n)) * d
    p = 2 * sum((-1) ** (j - 1) * math.exp(-2 * j * j * lam * lam) for j in range(1, 101))
    return d, min(1.0, max(0.0, p))


def binom_two_sided(k: int, n: int, p: float) -> float:
    pmf = [math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(n + 1)]
    return min(1.0, sum(q for q in pmf if q <= pmf[k] * (1 + 1e-9)))


def evaluate(per: dict[str, list[dict]], sizes_med: dict[str, float]) -> dict:
    rng = np.random.default_rng(SEED)
    names = sorted(per)
    diff = {f"{a}|{b}": {p: np.array([r[f"ls_{a}"] - r[f"ls_{b}"] for r in per[p]]) for p in names}
            for a, b in (("M1", "M0"), ("M3", "M1"), ("M3", "M0"))}
    out = {"pulsars": len(names), "forecasts": sum(len(per[p]) for p in names), "information_gain": {}}
    idx = rng.integers(0, len(names), size=(N_BOOT, len(names)))
    for key, d in diff.items():
        means = np.array([d[p].mean() for p in names])
        sums, counts = np.array([d[p].sum() for p in names]), np.array([len(d[p]) for p in names])
        boot_avg, boot_pool = means[idx].mean(axis=1), sums[idx].sum(axis=1) / counts[idx].sum(axis=1)
        no37 = [i for i, p in enumerate(names) if p != "J0537-6910"]
        out["information_gain"][key] = {
            "pulsar_averaged": float(means.mean()), "pulsar_averaged_lower95": float(np.quantile(boot_avg, 0.05)),
            "pulsar_averaged_ci90": [float(np.quantile(boot_avg, 0.05)), float(np.quantile(boot_avg, 0.95))],
            "pooled": float(sums.sum() / counts.sum()), "pooled_lower95": float(np.quantile(boot_pool, 0.05)),
            "pooled_without_J0537": float(sums[no37].sum() / counts[no37].sum()),
            "per_pulsar": {p: round(float(m), 4) for p, m in zip(names, means)},
            "pulsars_positive": int((means > 0).sum())}
    ig = [out["information_gain"]["M1|M0"]["per_pulsar"][p] for p in names]
    med = [sizes_med[p] for p in names]
    rho = spearman(med, ig)
    perm = np.array([spearman(rng.permutation(med).tolist(), ig) for _ in range(N_PERM // 10)])
    out["H3_spearman_IG_vs_median_log_size"] = {"rho": rho, "p_one_sided": float((perm >= rho - 1e-12).mean()), "n_perm": len(perm)}
    pit = [r["pit_M1"] for p in names for r in per[p]]
    d, pks = ks_uniform(pit)
    in50 = sum(0.25 <= u <= 0.75 for u in pit)
    in90 = sum(0.05 <= u <= 0.95 for u in pit)
    out["H4_calibration_M1"] = {"n": len(pit), "ks_D": d, "ks_p": pks, "in_central50": in50, "in_central90": in90,
                                "p_central50": binom_two_sided(in50, len(pit), 0.5), "p_central90": binom_two_sided(in90, len(pit), 0.9),
                                "pit_deciles": np.histogram(pit, bins=10, range=(0, 1))[0].tolist()}
    return out


def descriptives(glitches: list[tuple]) -> dict:
    times, sizes = [t for t, s in glitches], [s for t, s in glitches]
    waits = np.diff(times)
    pairs = [(math.log(s), math.log(w)) for s, w in zip(sizes[:-1], waits) if s is not None and s > 0]
    x, y = np.array(pairs).T
    b = float(((x - x.mean()) * (y - y.mean())).sum() / ((x - x.mean()) ** 2).sum())
    return {"n_glitches": len(times), "cv_wait": float(waits.std(ddof=1) / waits.mean()),
            "median_log10_size": float(np.median([math.log10(s) for s in sizes if s is not None and s > 0])),
            "slope_logwait_on_logsize_full": b}


def prospective(cat: dict, per_scores: dict) -> list[dict]:
    rows = []
    for p, g in sorted(cat.items()):
        if len(g) < MIN_PAST + 1:
            continue
        times, sizes = [t for t, s in g], [s for t, s in g]
        k = len(times) - 1
        pr = predictives(times, sizes, k)
        sc = per_scores.get(p)
        model = max(MODELS, key=lambda m: sum(r[f"ls_{m}"] for r in sc)) if sc and len(sc) >= 3 else "M1"
        f, w0 = pr[model], SNAPSHOT_MJD - times[-1]
        qs = (0.05, 0.25, 0.5, 0.75, 0.95)
        rows.append({"pulsar": p, "n_glitches": len(times), "last_glitch_mjd": times[-1], "model": model,
                     "unconditional_mjd": {str(q): round(times[-1] + f.quantile(q), 1) for q in qs},
                     "prob_glitch_before_snapshot": round(f.cdf(w0), 4) if w0 > 0 else 0.0,
                     "conditional_on_none_before_snapshot_mjd": {str(q): round(times[-1] + f.quantile(q, w0), 1) for q in qs}})
    return rows


def selftest() -> None:
    assert abs(t_cdf(0.0, 5, 0, 1) - 0.5) < 1e-12 and abs(t_cdf(2.015048, 5, 0, 1) - 0.95) < 1e-5
    assert abs(t_cdf(-1.812461, 10, 0, 1) - 0.05) < 1e-5
    xs = np.linspace(-30, 30, 200001)
    assert abs(np.trapz(np.exp([t_logpdf(x, 3, 1, 2) for x in xs]), xs) - 1) < 2e-3
    pr = m0([100.0] * 5)
    ws = np.linspace(1e-3, 1e6, 2000001)
    assert abs(np.trapz(np.exp([pr.logpdf(w) for w in ws[::50]]), ws[::50]) - 1) < 1e-2
    assert abs(pr.cdf(pr.quantile(0.3)) - 0.3) < 1e-9
    q = m1([50.0, 80, 120, 90])
    assert abs(q.cdf(q.quantile(0.8, 200)) - (q.cdf(200) + 0.8 * (1 - q.cdf(200)))) < 1e-9  # conditional quantile
    d, p = ks_uniform(list(np.random.default_rng(1).uniform(size=500)))
    assert p > 0.01, (d, p)
    rng = np.random.default_rng(7)
    poisson = {f"P{i}": list(zip(np.cumsum(rng.exponential(300, 30)), [10.0] * 30)) for i in range(8)}
    periodic = {f"Q{i}": list(zip(np.cumsum(rng.lognormal(math.log(300), 0.15, 30)), [10.0] * 30)) for i in range(8)}
    sz = rng.lognormal(3, 1.5, 31)
    reservoir = {f"R{i}": list(zip(np.cumsum(np.r_[0, 5 * sz[:-1] * rng.lognormal(0, 0.2, 30)]), sz)) for i in range(8)}
    for name, cat, expect in (("poisson", poisson, "M1|M0<=0.05"), ("periodic", periodic, "M1|M0>0.3"), ("reservoir", reservoir, "M3|M1>0.3")):
        per = {p: backtest(g) for p, g in cat.items()}
        res = evaluate(per, {p: 1.0 + i for i, p in enumerate(per)})
        ig = res["information_gain"]
        if expect == "M1|M0<=0.05":
            assert ig["M1|M0"]["pulsar_averaged"] <= 0.05 and res["H4_calibration_M1"]["ks_p"] > 0.001, (name, ig["M1|M0"], res["H4_calibration_M1"])
        elif expect == "M1|M0>0.3":
            assert ig["M1|M0"]["pulsar_averaged"] > 0.3, (name, ig["M1|M0"])
        else:
            assert ig["M3|M1"]["pulsar_averaged"] > 0.3, (name, ig["M3|M1"])
    print("selftest OK")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("cmd", choices=["selftest", "run"])
    ap.add_argument("--catalogue", default=str(t01.DATA / "gTable.html"))
    ap.add_argument("--min-glitches", type=int, default=MIN_GLITCHES, help="registered: 8; sensitivity: 6")
    args = ap.parse_args()
    if args.cmd == "selftest":
        selftest()
        return 0
    raw = Path(args.catalogue).read_bytes()
    cat = t01.parse_jbo(raw.decode("utf-8", errors="replace"))
    sel = {p: g for p, g in cat.items() if len(g) >= args.min_glitches}
    per = {p: backtest(g) for p, g in sel.items()}
    desc = {p: descriptives(g) for p, g in sel.items()}
    res = {"catalogue_sha256": hashlib.sha256(raw).hexdigest(), "snapshot_mjd": SNAPSHOT_MJD,
           "evaluation": evaluate(per, {p: desc[p]["median_log10_size"] for p in sel}), "descriptives": desc,
           "m3_used_fraction": sum(r["m3_used"] for p in per for r in per[p]) / sum(len(per[p]) for p in per),
           "prospective_forecasts": prospective(cat, per), "backtest_rows": per}
    res["min_glitches"] = args.min_glitches
    name = "G1-results.json" if args.min_glitches == MIN_GLITCHES and args.catalogue == str(t01.DATA / "gTable.html") else f"G1-results-min{args.min_glitches}.json"
    (t01.RESULTS / name).write_text(json.dumps(res, indent=1), encoding="utf-8")
    print(json.dumps(res["evaluation"], indent=1))
    for p, d in sorted(desc.items(), key=lambda x: -x[1]["n_glitches"]):
        print(f"{p:12} n={d['n_glitches']:3} CV={d['cv_wait']:.2f} med log10 size={d['median_log10_size']:+.2f} slope={d['slope_logwait_on_logsize_full']:+.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
