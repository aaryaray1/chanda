#!/usr/bin/env python3
"""B1: blind test of the vortex-creep recovery relation on Vela, from Fermi-LAT photons (pre-registered; numpy only)."""
from __future__ import annotations

import argparse
import json
import math
import sys
import urllib.parse
import urllib.request
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fitsmini  # noqa: E402
import t01_glitches as t01  # noqa: E402

DATA = t01.HERE.parent / "data" / "b1"
RA, DEC = math.radians(128.8358812), math.radians(-45.1763264)  # 3PC: 08:35:20.61149, -45:10:34.8751
NHAT = np.array([math.cos(DEC) * math.cos(RA), math.cos(DEC) * math.sin(RA), math.sin(DEC)])
F0, F1, PEPOCH = 11.188185028329053976, -1.5487253474641025133e-11, 56401.0  # 3PC J0835-4510_LAT_PKSTZR.par
C_KM = 299792.458
GLITCHES = [55408.8, 56556.0, 57734.5, 58515.6, 59417.2]  # catalogue epochs, MJD
WIN = 14.0
SEARCH = 5e-5


def horizons(mjd0: float, mjd1: float) -> np.ndarray:
    path = DATA / f"earth_ssb_{int(mjd0)}_{int(mjd1)}.csv"
    if not path.exists():
        q = {"format": "text", "COMMAND": "'399'", "EPHEM_TYPE": "'VECTORS'", "CENTER": "'500@0'", "START_TIME": f"'JD {mjd0 + 2400000.5}'",
             "STOP_TIME": f"'JD {mjd1 + 2400000.5}'", "STEP_SIZE": "'1 d'", "VEC_TABLE": "'1'", "REF_PLANE": "'FRAME'", "OUT_UNITS": "'KM-S'",
             "CSV_FORMAT": "'YES'", "VEC_CORR": "'NONE'", "TIME_TYPE": "'TDB'"}
        url = "https://ssd.jpl.nasa.gov/api/horizons.api?" + urllib.parse.urlencode(q)
        req = urllib.request.Request(url, headers={"User-Agent": "chanda-frontier/1.0"})
        with urllib.request.urlopen(req, timeout=120) as r:
            text = r.read().decode()
        body = text.split("$$SOE")[1].split("$$EOE")[0]
        DATA.mkdir(parents=True, exist_ok=True)
        path.write_text(body.strip() + "\n", encoding="utf-8")
    rows = [line.split(",") for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    return np.array([[float(r[0]) - 2400000.5, float(r[2]), float(r[3]), float(r[4])] for r in rows])  # MJD(TDB), x, y, z km


def interp4(tab: np.ndarray, t: np.ndarray) -> np.ndarray:
    i = np.clip(np.searchsorted(tab[:, 0], t) - 2, 0, len(tab) - 4)
    out = np.zeros((len(t), 3))
    for k in range(4):
        w = np.ones_like(t)
        for j in range(4):
            if j != k:
                w *= (t - tab[i + j, 0]) / (tab[i + k, 0] - tab[i + j, 0])
        out += w[:, None] * tab[i + k, 1:4]
    return out


def barycentre(query: Path) -> tuple[np.ndarray, np.ndarray]:
    ph = next(query.glob("*_PH*.fits"))
    sc = next(query.glob("*_SC*.fits"))
    ev = fitsmini.read_table(ph, "EVENTS", ["TIME", "ENERGY", "ZENITH_ANGLE"])
    mjdref = float(fitsmini.keyword(ph, "EVENTS", "MJDREFI")) + float(fitsmini.keyword(ph, "EVENTS", "MJDREFF"))
    keep = ev["ZENITH_ANGLE"] < 90
    met, energy = ev["TIME"][keep].astype(float), ev["ENERGY"][keep].astype(float)
    s = fitsmini.read_table(sc, "SC_DATA", ["START", "SC_POSITION"])
    order = np.argsort(s["START"])
    st, pos = s["START"][order].astype(float), s["SC_POSITION"][order].astype(float) / 1000.0  # m -> km
    sc_km = np.column_stack([np.interp(met, st, pos[:, k]) for k in range(3)])
    tt = mjdref + met / 86400.0
    earth = interp4(horizons(math.floor(tt.min()) - 3, math.ceil(tt.max()) + 3), tt)
    roemer = (earth + sc_km) @ NHAT / C_KM
    g = np.radians(357.53 + 0.98560028 * (tt + 2400000.5 - 2451545.0))
    einstein = 0.001657 * np.sin(g) + 0.000014 * np.sin(2 * g)
    return tt + (roemer + einstein) / 86400.0, energy


def nu_ref(t: float) -> float:
    cat = t01.parse_jbo((t01.DATA / "gTable.html").read_text(encoding="utf-8", errors="replace"))["J0835-4510"]
    steps = sum((s or 0) * 1e-9 * F0 * (1 if PEPOCH < tg <= t else -1 if t < tg <= PEPOCH else 0) for tg, s in cat)
    return F0 + F1 * (t - PEPOCH) * 86400.0 + steps


def zm(phase: np.ndarray, m: int) -> np.ndarray:
    """Z^2_k for k = 1..m for each row of phases (trials x photons)."""
    out = []
    n = phase.shape[1]
    for k in range(1, m + 1):
        a = 2 * np.pi * k * phase
        out.append((np.cos(a).sum(axis=1) ** 2 + np.sin(a).sum(axis=1) ** 2) * 2.0 / n)
    return np.cumsum(np.array(out), axis=0)


def htest(phase: np.ndarray, m: int = 20) -> np.ndarray:
    z = zm(phase, m)
    return np.max(z - 4 * np.arange(1, m + 1)[:, None] + 4, axis=0)


def window_nu(t_mjd: np.ndarray, centre: float, mid: float) -> dict:
    dt = (t_mjd - mid) * 86400.0
    fold = 0.5 * F1 * dt ** 2
    coarse = centre + np.arange(-SEARCH, SEARCH + 1e-12, 1e-7)
    best_c = []
    for chunk in np.array_split(coarse, max(1, len(coarse) // 50)):
        ph = (chunk[:, None] * dt[None, :] + fold[None, :]) % 1.0
        best_c.append((zm(ph, 2)[-1], chunk))
    zc = np.concatenate([b[0] for b in best_c])
    nu_c = np.concatenate([b[1] for b in best_c])[int(np.argmax(zc))]
    fine = nu_c + np.arange(-3e-7, 3e-7 + 1e-15, 2e-9)
    ph = (fine[:, None] * dt[None, :] + fold[None, :]) % 1.0
    h = htest(ph)
    k = int(np.argmax(h))
    return {"mid": mid, "n": int(len(dt)), "nu": float(fine[k]), "H": float(h[k]), "z2_coarse_peak": float(zc.max()),
            "edge": bool(abs(nu_c - centre) > 0.95 * SEARCH)}


def measure(query: Path, tg: float, emin: float = 100.0, win: float = WIN) -> list[dict]:
    tb, energy = barycentre(query)
    tb = tb[energy >= emin]
    rows = []
    for side, start, stop in (("pre", tg - 160.0, tg), ("post", tg, tg + 410.0)):
        edges = np.arange(stop, start - 1e-9, -win)[::-1] if side == "pre" else np.arange(start, stop + 1e-9, win)
        for a, b in zip(edges[:-1], edges[1:]):
            sel = (tb >= a) & (tb < b)
            if sel.sum() < 200:
                continue
            mid = 0.5 * (a + b)
            r = window_nu(tb[sel], nu_ref(mid), mid)
            r["side"] = side
            rows.append(r)
    return rows


def fit(rows: list[dict], tg: float, side: str, lo: float, hi: float) -> dict:
    sel = [r for r in rows if r["side"] == side and lo <= r["mid"] - tg <= hi]
    tau = np.array([(r["mid"] - tg) * 86400.0 for r in sel])
    nu = np.array([r["nu"] for r in sel])
    c2, c1, c0 = np.polyfit(tau, nu - nu.mean(), 2)
    resid = nu - nu.mean() - np.polyval([c2, c1, c0], tau)
    return {"n": len(sel), "nudot_at_tg": float(c1), "nuddot": float(2 * c2), "rms_resid": float(resid.std())}


PUBLISHED = {55408.8: {"GU22": 984}, 56556.0: {"GU22": 1862}, 57734.5: {"GU22": 781, "GR26": 774.0}, 58515.6: {"GU22": 769, "GR26": 921.6},
             59417.2: {"GR26": 469.1}}  # in-sample t_th (V1)


def score_one(tg: float, rows: list[dict], cat: list, post=(100.0, 400.0)) -> dict:
    large = [t for t, s in cat if s and s >= 100]
    nxt = next(t for t in large if t > tg + 2)
    prev = [b - a for a, b in zip(large, large[1:]) if b <= tg + 2]
    base = math.exp(np.mean(np.log(prev)))
    pre, pst = fit(rows, tg, "pre", -150.0, -7.0), fit(rows, tg, "post", *post)
    t_obs = nxt - tg
    out = {"glitch": tg, "t_obs": t_obs, "baseline": base, "e_baseline": abs(math.log(base / t_obs)), "pre": pre, "post": pst,
           "published_t_th": PUBLISHED.get(tg, {})}
    if pst["nuddot"] <= 0:
        out.update(t0=None, e_model=float("inf"), note="nuddot <= 0: no recovery predicted (model failure)")
    else:
        t0 = (pre["nudot_at_tg"] - pst["nudot_at_tg"]) / pst["nuddot"] / 86400.0
        out.update(t0=t0, e_model=abs(math.log(t0 / t_obs)) if t0 > 0 else float("inf"))
    out["model_wins"] = out["e_model"] < out["e_baseline"]
    return out


def verdict(res: list[dict]) -> dict:
    wins = sum(r["model_wins"] for r in res)
    med = float(np.median([r["e_model"] for r in res]))
    v = "blind skill supported" if wins >= 4 and med < 0.10 else ("not supported" if wins <= 2 else "inconclusive")
    return {"model_wins": wins, "n": len(res), "median_e_model": med, "median_e_baseline": float(np.median([r["e_baseline"] for r in res])), "verdict": v}


def score() -> dict:
    cat = t01.parse_jbo((t01.DATA / "gTable.html").read_text(encoding="utf-8", errors="replace"))["J0835-4510"]
    out = {}
    for name, tag, post in (("primary", "", (100.0, 400.0)), ("post_60_400", "", (60.0, 400.0)), ("post_100_300", "", (100.0, 300.0)),
                            ("window_28d", "_e100_w28", (100.0, 400.0)), ("emin_300MeV", "_e300_w14", (100.0, 400.0))):
        res = []
        for tg in GLITCHES:
            f = DATA / f"nu_{int(tg)}{tag}.json"
            if f.exists():
                res.append(score_one(tg, json.loads(f.read_text(encoding="utf-8")), cat, post))
        if res:
            out[name] = {"intervals": res, **verdict(res)}
    return out


def selftest() -> None:
    rng = np.random.default_rng(0)
    mid, nu0 = 57000.0, 11.1875
    t = mid + rng.uniform(-7, 7, 4000)
    dt = (t - mid) * 86400
    keep = rng.uniform(size=len(t)) < 0.5 + 0.45 * np.cos(2 * np.pi * (nu0 * dt + 0.5 * F1 * dt ** 2))
    r = window_nu(t[keep], nu0 + 2e-5, mid)
    assert abs(r["nu"] - nu0) < 5e-8, r  # statistical precision ~ 1/(T sqrt(Z2)) ~ 3e-8 Hz for this broad synthetic profile
    rows = [{"side": "post", "mid": 57000 + d, "nu": 11.1 + (-1.55e-11) * d * 86400 + 0.5 * 1e-21 * (d * 86400) ** 2} for d in range(100, 401, 14)]
    f = fit(rows, 57000.0, "post", 100, 400)
    assert abs(f["nuddot"] - 1e-21) < 1e-24 and abs(f["nudot_at_tg"] + 1.55e-11) < 1e-15, f
    print("selftest OK", r["nu"] - nu0, f["nuddot"])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("cmd", choices=["selftest", "measure", "score"])
    ap.add_argument("--query")
    ap.add_argument("--glitch", type=float)
    ap.add_argument("--emin", type=float, default=100.0)
    ap.add_argument("--win", type=float, default=WIN)
    args = ap.parse_args()
    if args.cmd == "selftest":
        selftest()
        return 0
    if args.cmd == "score":
        res = score()
        (t01.RESULTS / "B1-results.json").write_text(json.dumps(res, indent=1, default=float), encoding="utf-8")
        for name, r in res.items():
            print(name, {k: v for k, v in r.items() if k != "intervals"})
            for x in r["intervals"]:
                print(f"   tg {x['glitch']}: t0 {x['t0'] if x['t0'] is None else round(x['t0'], 1)} vs t_obs {x['t_obs']:.0f} (base {x['baseline']:.0f})"
                      f" e_m {x['e_model']:.3f} e_b {x['e_baseline']:.3f} published {x['published_t_th']}")
        return 0
    rows = measure(Path(args.query), args.glitch, args.emin, args.win)
    tag = f"{int(args.glitch)}" + ("" if (args.emin, args.win) == (100.0, WIN) else f"_e{int(args.emin)}_w{int(args.win)}")
    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / f"nu_{tag}.json").write_text(json.dumps(rows, indent=1), encoding="utf-8")
    for r in rows:
        print(f"{r['side']:4} mid {r['mid']:.1f} n {r['n']:6d} H {r['H']:8.1f} nu-ref {r['nu'] - nu_ref(r['mid']):+.3e} edge {r['edge']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
