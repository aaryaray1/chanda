#!/usr/bin/env python3
"""T01: pre-registered test of the size–waiting-time predictions of Melatos, Howitt & Fulgenzi (2018) on the Jodrell Bank glitch catalogue."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html as htmllib
import json
import math
import re
import sys
import urllib.request
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data" / "t01"
RESULTS = HERE.parent / "results"
JBO_URL = "https://www.jb.man.ac.uk/pulsar/glitches/gTable.html"
ATNF_URL = ("https://www.atnf.csiro.au/research/pulsar/psrcat/proc_form.php?JName=JName&F1=F1&startUserDefined=true&sort_attr=jname"
            "&sort_order=asc&condition=&pulsar_names=&ephemeris=short&style=Short+without+errors&no_value=*&state=query"
            "&table_bottom.x=0&table_bottom.y=0")
CUTOFF_MJD = 58370.0  # arXiv v1 of Melatos et al. (2018): 2018-09-09
SEED, B_PERM = 20261120, 100_000
N_H1, N_H2, N_H2_LOOSE, N_NEW = 10, 8, 6, 6
SIGMA3 = 0.0027
CONTROL = "J0537-6910"
TOP = ["J0205+6449", "J0537-6910", "J1119-6127", "J2229+6114"]  # Table 2 top half; the authors exclude J0534+2200
BOTTOM = ["J0528+2200", "J1814-1744", "J1902+0615", "J1957+2831", "J2225+6535"]
TABLE1 = {"J0534+2200": (27, -0.075, 0.328, 0.024, 0.464), "J0537-6910": (42, 0.927, 0.159, 0.931, 0.164),
          "J0631+1036": (15, 0.701, -0.091, 0.156, -0.145), "J0835-4510": (21, 0.407, 0.603, 0.358, 0.398),
          "J1341-6220": (23, 0.293, -0.082, 0.578, -0.145), "J1740-3015": (35, 0.298, -0.065, 0.264, -0.180),
          "J1801-2304": (13, 0.764, -0.024, 0.804, -0.042)}  # N, r+, r−, ρ+, ρ− on the full historical set


def jname(s: str) -> str:
    return s.replace("−", "-").replace("–", "-").strip()


def num(s: str) -> float | None:
    s = htmllib.unescape(s).replace("−", "-").strip()
    if not s or s[0] in "<>~?" or "?" in s:
        return None
    m = re.match(r"[-+]?(\d+\.?\d*|\.\d+)([eE][-+]?\d+)?", s)
    return float(m.group(0)) if m else None


def parse_jbo(text: str) -> dict[str, list[tuple[float, float | None]]]:
    clean = lambda c: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", c)).strip()
    out: dict[str, list[tuple[float, float | None]]] = {}
    for row in re.findall(r"<tr[^>]*>(.*?)</tr>", text, re.S | re.I):
        cells = [clean(c) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.S | re.I)]
        if len(cells) < 7:
            continue
        name = jname(cells[2] if cells[2].startswith("J") else "J" + cells[2])  # the catalogue's J-name column omits the "J"
        if not re.fullmatch(r"J\d{4}[+-]\d{2,4}[A-Za-z]?", name):
            continue
        mjd = num(cells[4])
        if mjd is None or mjd < 30000:
            continue
        size = num(cells[6])
        out.setdefault(name, []).append((mjd, size if size is not None and size > 0 else None))
    return {k: sorted(v) for k, v in out.items()}


def parse_atnf(text: str) -> dict[str, float]:
    pre = " ".join(re.findall(r"<pre[^>]*>(.*?)</pre>", text, re.S | re.I)) or text
    f1 = {}
    for m in re.finditer(r"^\s*\d+\s+(J\S+)\s+(\S+)\s*$", re.sub(r"<[^>]+>", "", pre), re.M):
        v = num(m.group(2))
        if v is not None:
            f1[jname(m.group(1))] = v
    return f1


def n_sized(g: list) -> int:
    return sum(1 for _, s in g if s is not None)


def pairs(g: list, direction: str, after: float | None = None) -> tuple[np.ndarray, np.ndarray]:
    xs, ts = [], []
    for i, (t, s) in enumerate(g):
        j = i + 1 if direction == "+" else i - 1
        if s is None or not 0 <= j < len(g) or (after is not None and t <= after):
            continue
        xs.append(s)
        ts.append(abs(g[j][0] - t))
    return np.array(xs, float), np.array(ts, float)


def ranks(a: np.ndarray) -> np.ndarray:
    order = np.argsort(a, kind="mergesort")
    r, vals, i = np.empty(len(a)), a[order], 0
    while i < len(a):
        j = i
        while j + 1 < len(a) and vals[j + 1] == vals[i]:
            j += 1
        r[order[i:j + 1]] = (i + j) / 2 + 1
        i = j + 1
    return r


def zscore(a: np.ndarray) -> np.ndarray:
    sd = a.std()
    return (a - a.mean()) / sd if sd > 0 else np.zeros_like(a)


def corr(x: np.ndarray, y: np.ndarray, spearman: bool) -> float:
    if spearman:
        x, y = ranks(x), ranks(y)
    return float(np.mean(zscore(x) * zscore(y)))


def perm_p(x: np.ndarray, y: np.ndarray, spearman: bool, rng: np.random.Generator, b: int = B_PERM) -> dict:
    if spearman:
        x, y = ranks(x), ranks(y)
    zx, zy = zscore(x), zscore(y)
    obs = float(np.mean(zx * zy))
    ge = le = 0
    for start in range(0, b, 20_000):
        k = min(20_000, b - start)
        sims = rng.permuted(np.tile(zy, (k, 1)), axis=1) @ zx / len(zx)
        ge += int(np.sum(sims >= obs - 1e-12))
        le += int(np.sum(sims <= obs + 1e-12))
    p_hi, p_lo = (ge + 1) / (b + 1), (le + 1) / (b + 1)
    return {"stat": obs, "p_pos": p_hi, "p_neg": p_lo, "p_two": min(1.0, 2 * min(p_hi, p_lo))}


def fisher_bound(r: float, n: int, bound: float = 0.5) -> float:
    if n <= 3 or abs(r) >= 1:
        return 0.0 if r >= 1 else 1.0
    z = (math.atanh(r) - math.atanh(bound)) * math.sqrt(n - 3)
    return 0.5 * math.erfc(z / math.sqrt(2))  # one-sided p for r > bound


def fisher_combine(ps: list[float]) -> float:
    if not ps:
        return float("nan")
    x = -2 * sum(math.log(max(p, 1e-300)) for p in ps)
    term, total = 1.0, 1.0
    for i in range(1, len(ps)):
        term *= (x / 2) / i
        total += term
    return min(1.0, math.exp(-x / 2) * total)  # chi-square survival with 2k degrees of freedom


def per_pulsar(g: list, rng: np.random.Generator, after: float | None = None) -> dict:
    row = {}
    for d in "+-":
        s, w = pairs(g, d, after)
        key = "fwd" if d == "+" else "bwd"
        row[f"n_{key}"] = len(s)
        if len(s) >= 4:
            row[f"r_{key}"] = corr(s, w, False)
            sp = perm_p(s, w, True, rng)
            row[f"rho_{key}"], row[f"p_{key}"] = sp["stat"], sp
    return row


def analyse(cat: dict, f1: dict) -> dict:
    rng = np.random.default_rng(SEED)
    res: dict = {"n_pulsars": len(cat), "n_glitches": sum(len(g) for g in cat.values()),
                 "n_sized": sum(n_sized(g) for g in cat.values()), "cutoff_mjd": CUTOFF_MJD,
                 "n_new": sum(1 for g in cat.values() for t, _ in g if t > CUTOFF_MJD)}
    g0 = cat.get(CONTROL, [])
    s, w = pairs(g0, "+")
    pc = perm_p(s, w, True, rng) if len(s) >= 4 else {"stat": float("nan"), "p_pos": 1.0}
    res["control"] = {"pulsar": CONTROL, "n": len(s), "rho_fwd": pc["stat"], "p": pc["p_pos"],
                      "pass": bool(pc["stat"] >= 0.8 and pc["p_pos"] < 1e-4)}
    h1 = {k: g for k, g in cat.items() if n_sized(g) >= N_H1}
    k_h1, rows = len(h1), []
    for name, g in sorted(h1.items()):
        row = {"pulsar": name, "N": n_sized(g), **per_pulsar(g, rng)}
        if "r_bwd" in row:
            row["p_bound"] = fisher_bound(row["r_bwd"], row["n_bwd"])
            row["sig_bwd"] = row["p_bwd"]["p_two"] < SIGMA3 / k_h1
            row["exceeds_bound"] = row["p_bound"] < SIGMA3 / k_h1
        rows.append(row)
    res["H1"] = {"K": k_h1, "alpha_each": SIGMA3 / max(1, k_h1), "rows": rows,
                 "H1a_refuted": any(r.get("sig_bwd") for r in rows), "H1b_refuted": any(r.get("exceeds_bound") for r in rows)}
    new_rows, ps = [], []
    for name, g in sorted(cat.items()):
        s, w = pairs(g, "-", CUTOFF_MJD)
        if len(s) >= N_NEW:
            sp = perm_p(s, w, True, rng)
            new_rows.append({"pulsar": name, "n": len(s), "rho_bwd": sp["stat"], "r_bwd": corr(s, w, False), "p_two": sp["p_two"]})
            ps.append(sp["p_two"])
    res["H1_new"] = {"rows": new_rows, "fisher_p": fisher_combine(ps)}
    for label, nmin, after in (("H2", N_H2, None), ("H2_loose", N_H2_LOOSE, None), ("H2_new", N_NEW, CUTOFF_MJD)):
        xs, ys, ys_rho, names, missing = [], [], [], [], []
        for name, g in sorted(cat.items()):
            s, w = pairs(g, "+", after)
            if (n_sized(g) if after is None else len(s)) < nmin or len(s) < 4:
                continue
            if name not in f1 or f1[name] >= 0:
                missing.append(name)
                continue
            mean_wait = (g[-1][0] - g[0][0]) / (len(g) - 1) * 86400.0
            xs.append(math.log10(-f1[name] * mean_wait))
            ys.append(corr(s, w, False))
            ys_rho.append(corr(s, w, True))
            names.append(name)
        xs, ys, ys_rho = np.array(xs), np.array(ys), np.array(ys_rho)
        out = {"n": len(xs), "missing_f1": missing,
               "points": [{"pulsar": n, "log10_nudot_wait_hz": round(x, 3), "r_fwd": round(y, 3), "rho_fwd": round(z, 3)}
                          for n, x, y, z in zip(names, xs, ys, ys_rho)]}
        if len(xs) >= 5:
            out["primary"] = perm_p(xs, ys, True, rng)
            out["rho_version"] = perm_p(xs, ys_rho, True, rng)
            p = out["primary"]
            out["verdict"] = "supported" if p["stat"] > 0 and p["p_pos"] < 0.01 else \
                "contradicted" if p["stat"] < 0 and p["p_neg"] < 0.01 else "inconclusive"
        res[label] = out
    targets = []
    for name in TOP + BOTTOM:
        g = cat.get(name, [])
        row = {"pulsar": name, "half": "top" if name in TOP else "bottom", "N": n_sized(g)}
        for tag, after in (("all", None), ("new", CUTOFF_MJD)):
            s, w = pairs(g, "+", after)
            row[f"n_{tag}"] = len(s)
            if len(s) >= 3:
                row[f"r_fwd_{tag}"] = round(corr(s, w, False), 3)
        targets.append(row)
    res["table2_targets"] = targets
    rep = []
    for name, (n, rp, rm, rhop, rhom) in TABLE1.items():
        g = [x for x in cat.get(name, []) if x[0] <= CUTOFF_MJD]
        row = {"pulsar": name, "N_paper": n, "N_here": n_sized(g), "paper": [rp, rm, rhop, rhom]}
        sf, wf = pairs(g, "+")
        sb, wb = pairs(g, "-")
        if len(sf) >= 4 and len(sb) >= 4:
            row["here"] = [round(corr(sf, wf, False), 3), round(corr(sb, wb, False), 3), round(corr(sf, wf, True), 3),
                           round(corr(sb, wb, True), 3)]
        rep.append(row)
    res["table1_replication"] = rep
    return res


def gapless(s: np.ndarray, w: np.ndarray, g: list, factor: float = 5.0) -> tuple[np.ndarray, np.ndarray]:
    med = float(np.median(np.diff([t for t, _ in g])))  # median of all consecutive waits of the pulsar
    keep = w <= factor * med
    return s[keep], w[keep]


def posthoc(cat: dict, f1: dict) -> dict:
    """Analyses added after the run (referee, 2026-11-21); none is pre-registered."""
    rng = np.random.default_rng(SEED + 3)
    out: dict = {}
    h1 = {k: g for k, g in cat.items() if n_sized(g) >= N_H1}
    k_h1 = len(h1)
    zcrit = 2.0 ** 0.5 * _erfcinv(2 * SIGMA3 / k_h1)  # one-sided normal quantile for alpha = 0.0027/K
    comp, rows, zs, ws = {"pairs": 0, "post_cutoff": 0, "by_pulsar": {}}, [], [], []
    for name, g in sorted(h1.items()):
        s, w = pairs(g, "-")
        sn, _ = pairs(g, "-", CUTOFF_MJD)
        comp["pairs"] += len(s)
        comp["post_cutoff"] += len(sn)
        comp["by_pulsar"][name] = {"pairs": len(s), "post_cutoff": len(sn), "last_epoch": g[-1][0]}
        r, n = corr(s, w, False), len(s)
        r_min = math.tanh(math.atanh(0.5) + zcrit / math.sqrt(n - 3))  # smallest r- that would have refuted H1b
        sg, wg = gapless(s, w, g)
        sp = perm_p(sg, wg, True, rng)
        rows.append({"pulsar": name, "n": n, "r_bwd": r, "min_detectable_r_vs_0.5": r_min,
                     "p_vs_0.1": fisher_bound(r, n, 0.1), "gapless_rho_bwd": sp["stat"], "gapless_p_two": sp["p_two"],
                     "gapless_r_bwd": corr(sg, wg, False), "gapless_n": len(sg)})
        zs.append(math.atanh(r))
        ws.append(n - 3)
    zbar = sum(z * w for z, w in zip(zs, ws)) / sum(ws)
    se = 1 / math.sqrt(sum(ws))
    q = sum(w * (z - zbar) ** 2 for z, w in zip(zs, ws))
    out["H1_composition"] = comp
    out["H1_rows"] = rows
    out["H1_pooled_fixed_effect"] = {"r": math.tanh(zbar), "ci95": [math.tanh(zbar - 1.96 * se), math.tanh(zbar + 1.96 * se)],
                                     "Q": q, "df": len(zs) - 1}
    grid = []
    for stat in ("r", "rho"):
        for nmin in (N_H2, N_H2_LOOSE):
            for crab in (True, False):
                xs, ys = [], []
                for name, g in sorted(cat.items()):
                    if n_sized(g) < nmin or (not crab and name == "J0534+2200") or name not in f1 or f1[name] >= 0:
                        continue
                    s, w = gapless(*pairs(g, "+"), g)
                    if len(s) < 4:
                        continue
                    xs.append(math.log10(-f1[name] * (g[-1][0] - g[0][0]) / (len(g) - 1) * 86400.0))
                    ys.append(corr(s, w, stat == "rho"))
                p = perm_p(np.array(xs), np.array(ys), True, rng)
                grid.append({"y": stat, "N_min": nmin, "crab": crab, "n": len(xs), "spearman": p["stat"], "p_pos": p["p_pos"],
                             "p_neg": p["p_neg"]})
    out["H2_gapless_grid"] = grid
    xs, ys = [], []
    for name, g in sorted(cat.items()):
        s, w = pairs(g, "-")
        if n_sized(g) >= N_H2 and len(s) >= 4 and name in f1 and f1[name] < 0:
            xs.append(math.log10(-f1[name] * (g[-1][0] - g[0][0]) / (len(g) - 1) * 86400.0))
            ys.append(corr(s, w, False))
    p = perm_p(np.array(xs), np.array(ys), True, rng)
    out["P1_ranking_unregistered"] = {"n": len(xs), "spearman_X_rbwd": p["stat"], "p_neg_predicted": p["p_neg"]}
    xall = []
    for name, g in cat.items():
        if n_sized(g) >= 4 and name in f1 and f1[name] < 0:
            xall.append((math.log10(-f1[name] * (g[-1][0] - g[0][0]) / (len(g) - 1) * 86400.0), name))
    xall.sort()
    out["X_percentiles_N4"] = {name: round(100 * i / (len(xall) - 1), 1) for i, (_, name) in enumerate(xall)
                               if name in ("J0537-6910", "J1341-6220", "J1413-6141", "J1048-5832", "J1801-2304")}
    out["X_percentiles_N4"]["n"] = len(xall)
    return out


def _erfcinv(y: float) -> float:
    lo, hi = 0.0, 10.0
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if math.erfc(mid) > y else (lo, mid)
    return (lo + hi) / 2


def fetch(url: str, path: Path) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "chanda-frontier/1.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        raw = resp.read()
    path.write_bytes(raw)
    return hashlib.sha256(raw).hexdigest()


def synthetic(rng: np.random.Generator) -> tuple[str, str]:
    rows, f1 = [], []
    for k in range(30):
        name = CONTROL if k == 0 else f"J{1000 + k:04d}+{k:04d}"
        n = 40 if k == 0 else int(rng.integers(6, 30))
        sizes = np.exp(rng.normal(2, 1.5, n))
        waits = 50 + 30 * sizes / sizes.mean() + rng.normal(0, 5, n) if k == 0 else rng.exponential(400, n)
        t = 50000 + np.concatenate([[0], np.cumsum(np.abs(waits[:-1]))])
        for i in range(n):
            size = "" if rng.random() < 0.05 else ("-0.5" if rng.random() < 0.02 else f"{sizes[i]:.3f}")
            rows.append(f"<tr><td></td><td>B{k}</td><td>{name}</td><td>{i + 1}</td><td>{t[i]:.3f}</td><td>0.1</td>"
                        f"<td>{size}</td><td>0.1</td><td>1.0</td><td>0.1</td><td>ref</td></tr>")
        f1.append(f"{k + 1}  {name}  {-10 ** rng.uniform(-15, -10):.3e}")
    return "<table>" + "".join(rows) + "</table>", "<pre>\n" + "\n".join(f1) + "\n</pre>"


def summary(res: dict) -> str:
    h1, lines = res["H1"], []
    lines.append(f"{res['n_glitches']} glitches ({res['n_sized']} with a positive size) in {res['n_pulsars']} pulsars; "
                 f"{res['n_new']} after MJD {CUTOFF_MJD:.0f}")
    c = res["control"]
    lines.append(f"control {c['pulsar']}: rho+ = {c['rho_fwd']:.3f} (n={c['n']}, p={c['p']:.2g}) -> {'PASS' if c['pass'] else 'FAIL'}")
    lines.append(f"H1: {h1['K']} pulsars with N>={N_H1}; per-pulsar alpha {h1['alpha_each']:.2g}; "
                 f"H1a (no significant backward correlation) {'REFUTED' if h1['H1a_refuted'] else 'survives'}; "
                 f"H1b (r- <= 0.5) {'REFUTED' if h1['H1b_refuted'] else 'survives'}")
    for r in h1["rows"]:
        if "r_bwd" in r:
            lines.append(f"  {r['pulsar']:12} N={r['N']:3d}  r-={r['r_bwd']:+.3f} rho-={r['rho_bwd']:+.3f} p2={r['p_bwd']['p_two']:.2g} "
                         f"p(r->0.5)={r['p_bound']:.2g} | r+={r.get('r_fwd', float('nan')):+.3f} rho+={r.get('rho_fwd', float('nan')):+.3f} "
                         f"p+={r['p_fwd']['p_pos'] if 'p_fwd' in r else float('nan'):.2g}")
    lines.append(f"H1 new data only: {len(res['H1_new']['rows'])} pulsars, Fisher combined p = {res['H1_new']['fisher_p']:.3g}")
    for label in ("H2", "H2_loose", "H2_new"):
        h = res[label]
        if "primary" in h:
            p = h["primary"]
            lines.append(f"{label}: {h['n']} pulsars, Spearman(log -nudot<dt>, r+) = {p['stat']:+.3f}, p+ = {p['p_pos']:.3g}, "
                         f"p- = {p['p_neg']:.3g} -> {h['verdict']} (rho+ version {h['rho_version']['stat']:+.3f}, p+ {h['rho_version']['p_pos']:.3g})")
        else:
            lines.append(f"{label}: only {h['n']} pulsars; not tested")
    return "\n".join(lines)


def main() -> int:
    with __import__("contextlib").suppress(AttributeError):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("cmd", choices=["selftest", "fetch", "run", "posthoc"])
    args = ap.parse_args()
    if args.cmd == "selftest":
        jbo, atnf = synthetic(np.random.default_rng(1))
        cat, f1 = parse_jbo(jbo), parse_atnf(atnf)
        res = analyse(cat, f1)
        print(summary(res))
        assert res["control"]["pass"], "the planted forward correlation was not found"
        assert len(f1) == 30 and len(cat) == 30
        print("selftest OK")
        return 0
    if args.cmd == "fetch":
        meta = {"fetched": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                "jbo_sha256": fetch(JBO_URL, DATA / "gTable.html"), "atnf_sha256": fetch(ATNF_URL, DATA / "atnf-f1.html")}
        (DATA / "fetch.json").write_text(json.dumps(meta, indent=1), encoding="utf-8")
        print(json.dumps(meta, indent=1))
        return 0
    cat = parse_jbo((DATA / "gTable.html").read_text(encoding="utf-8", errors="replace"))
    f1 = parse_atnf((DATA / "atnf-f1.html").read_text(encoding="utf-8", errors="replace"))
    if args.cmd == "posthoc":
        ph = posthoc(cat, f1)
        (RESULTS / "T01-posthoc.json").write_text(json.dumps(ph, indent=1, default=float), encoding="utf-8")
        print(json.dumps(ph, indent=1, default=float))
        return 0
    res = analyse(cat, f1)
    res["fetch"] = json.loads((DATA / "fetch.json").read_text(encoding="utf-8"))
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "T01-results.json").write_text(json.dumps(res, indent=1, default=float), encoding="utf-8")
    print(summary(res))
    return 0


if __name__ == "__main__":
    sys.exit(main())
