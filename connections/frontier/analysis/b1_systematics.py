#!/usr/bin/env python3
"""Post-hoc systematics for B1/B2 (after the B1 referee): corrected Vela position with proper motion, photon-centroid window epochs, residual-bootstrap t0 errors."""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import b1_vela as b1  # noqa: E402
import t01_glitches as t01  # noqa: E402

RA0 = math.radians((8 + 35 / 60 + 20.61149 / 3600) * 15)
DEC0 = -math.radians(45 + 10 / 60 + 34.8751 / 3600)  # -45.1763542 deg (B1 used -45.1763264, a 0.10" slip)
PMRA, PMDEC, POSEPOCH = -49.68, 29.9, 51544.0  # mas/yr (3PC J0835-4510_LAT_PKSTZR.par)
NEXT = {55408.8: 56556.0, 56556.0: 57734.5, 57734.5: 58515.6, 58515.6: 59417.2, 59417.2: 60429.9}


def nhat(mjd: float) -> np.ndarray:
    yr = (mjd - POSEPOCH) / 365.25
    dec = DEC0 + math.radians(PMDEC * yr / 3.6e6)
    ra = RA0 + math.radians(PMRA * yr / 3.6e6) / math.cos(DEC0)
    return np.array([math.cos(dec) * math.cos(ra), math.cos(dec) * math.sin(ra), math.sin(dec)])


def photons(queries: list[Path], tg: float) -> np.ndarray:
    b1.NHAT = nhat(tg + 0.5 * (NEXT[tg] - tg))
    out = []
    for q in queries:
        tb, e = b1.barycentre(q)
        out.append(tb[e >= 100])
    return np.concatenate(out)


def measure(tb: np.ndarray, tg: float, stop: float) -> list[dict]:
    rows = []
    for side, a0, b0 in (("pre", tg - 160.0, tg), ("post", tg, stop)):
        edges = np.arange(b0, a0 - 1e-9, -b1.WIN)[::-1] if side == "pre" else np.arange(a0, b0 + 1e-9, b1.WIN)
        for a, c in zip(edges[:-1], edges[1:]):
            sel = (tb >= a) & (tb < c)
            if sel.sum() < 200:
                continue
            cen = float(tb[sel].mean())
            r = b1.window_nu(tb[sel], b1.nu_ref(cen), cen)
            r.update(side=side, mid_nominal=0.5 * (a + c))
            rows.append(r)
    return rows


def fit_c(rows: list[dict], tg: float, side: str, lo: float, hi: float, rng=None) -> tuple[float, float]:
    sel = [r for r in rows if r["side"] == side and lo <= r["mid_nominal"] - tg <= hi]
    tau = np.array([(r["mid"] - tg) * 86400.0 for r in sel])
    nu = np.array([r["nu"] for r in sel])
    coef = np.polyfit(tau, nu - nu.mean(), 2)
    if rng is not None:
        res = nu - nu.mean() - np.polyval(coef, tau)
        coef = np.polyfit(tau, np.polyval(coef, tau) + rng.choice(res, len(res)), 2)
    return float(coef[1]), float(2 * coef[0])


def t0(rows: list[dict], tg: float, d: float, rng=None) -> float | None:
    pre1, _ = fit_c(rows, tg, "pre", -150.0, -7.0, rng)
    post1, post2 = fit_c(rows, tg, "post", 100.0, d, rng)
    return (pre1 - post1) / post2 / 86400.0 if post2 > 0 else None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--fermi", required=True, help="folder holding q1..q5 (B1) and r1..r5 (B2) query folders")
    args = ap.parse_args()
    root = Path(args.fermi)
    rng = np.random.default_rng(20261127)
    out = {}
    for k, tg in enumerate(b1.GLITCHES, 1):
        qs = [root / f"q{k}"] + ([root / f"r{k}"] if (root / f"r{k}").exists() else [])
        stop = NEXT[tg] - 7.0 if len(qs) > 1 else tg + 410.0
        rows = measure(photons(qs, tg), tg, stop)
        t_obs = NEXT[tg] - tg
        boot = [t0(rows, tg, 400.0, rng) for _ in range(500)]
        boot = [x for x in boot if x is not None]
        curve = {}
        if len(qs) > 1:
            for d in list(range(300, int(t_obs - 7), 100)) + [t_obs - 7.0]:
                curve[str(d)] = t0(rows, tg, float(d))
        out[str(tg)] = {"t_obs": t_obs, "t0_400": t0(rows, tg, 400.0), "t0_400_boot_sd": float(np.std(boot)), "curve": curve, "windows": len(rows)}
        print(tg, json.dumps(out[str(tg)]), flush=True)
    (t01.RESULTS / "B1-systematics-posthoc.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
