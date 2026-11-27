#!/usr/bin/env python3
"""B2: does the recovery-time estimate t0 depend on where the data end? Extends B1's frozen pipeline (b1_vela.py, unchanged) to the full interval."""
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

NEXT = {55408.8: 56556.0, 56556.0: 57734.5, 57734.5: 58515.6, 58515.6: 59417.2, 59417.2: 60429.9}


def measure_ext(q_b1: Path, q_new: Path, tg: float) -> list[dict]:
    t1, e1 = b1.barycentre(q_b1)
    t2, e2 = b1.barycentre(q_new)
    tb = np.concatenate([t1[e1 >= 100], t2[e2 >= 100]])
    stop = NEXT[tg] - 7.0
    rows, k = [], 29  # B1's post grid ends at the edge t_g + 406 d
    while tg + b1.WIN * (k + 1) <= stop:
        a, b = tg + b1.WIN * k, tg + b1.WIN * (k + 1)
        sel = (tb >= a) & (tb < b)
        if sel.sum() >= 200:
            mid = 0.5 * (a + b)
            r = b1.window_nu(tb[sel], b1.nu_ref(mid), mid)
            r["side"] = "post"
            rows.append(r)
        k += 1
    return rows


def t0_curve(rows: list[dict], tg: float) -> list[dict]:
    t_obs = NEXT[tg] - tg
    pre = b1.fit(rows, tg, "pre", -150.0, -7.0)
    ds = list(range(300, int(t_obs - 7), 100)) + [t_obs - 7.0]
    out = []
    for d in ds:
        pst = b1.fit(rows, tg, "post", 100.0, float(d))
        t0 = (pre["nudot_at_tg"] - pst["nudot_at_tg"]) / pst["nuddot"] / 86400.0 if pst["nuddot"] > 0 else None
        out.append({"D": float(d), "n_windows": pst["n"], "nuddot": pst["nuddot"], "t0": t0})
    return out


def score() -> dict:
    res, rises, closer, last_err = [], 0, 0, []
    for tg in b1.GLITCHES:
        base = json.loads((b1.DATA / f"nu_{int(tg)}.json").read_text(encoding="utf-8"))
        ext = json.loads((b1.DATA / f"nu_ext_{int(tg)}.json").read_text(encoding="utf-8"))
        curve = t0_curve(base + ext, tg)
        t_obs = NEXT[tg] - tg
        first = next(c for c in curve if c["D"] == 300)
        d400 = next(c for c in curve if c["D"] == 400)
        last = curve[-1]
        rise = last["t0"] is not None and first["t0"] is not None and last["t0"] > first["t0"]
        e_last = abs(math.log(last["t0"] / t_obs)) if last["t0"] and last["t0"] > 0 else float("inf")
        e400 = abs(math.log(d400["t0"] / t_obs)) if d400["t0"] and d400["t0"] > 0 else float("inf")
        rises += rise
        closer += e_last < e400
        last_err.append(e_last)
        res.append({"glitch": tg, "t_obs": t_obs, "curve": curve, "rises": rise, "e_400": e400, "e_last": e_last,
                    "published_t_th": b1.PUBLISHED.get(tg, {})})
    a = "supported" if rises == 5 else ("refuted" if rises <= 2 else "inconclusive")
    med = float(np.median(last_err))
    b = "supported" if closer >= 4 and med <= 0.10 else "not supported"
    return {"intervals": res, "H_B2a_rises": rises, "H_B2a": a, "H_B2b_closer_at_end": closer, "H_B2b_median_e_last": med, "H_B2b": b}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("cmd", choices=["measure", "score"])
    ap.add_argument("--b1query")
    ap.add_argument("--newquery")
    ap.add_argument("--glitch", type=float)
    args = ap.parse_args()
    if args.cmd == "measure":
        rows = measure_ext(Path(args.b1query), Path(args.newquery), args.glitch)
        (b1.DATA / f"nu_ext_{int(args.glitch)}.json").write_text(json.dumps(rows, indent=1), encoding="utf-8")
        print(f"{len(rows)} windows, H {min(r['H'] for r in rows):.0f}-{max(r['H'] for r in rows):.0f}, edge hits {sum(r['edge'] for r in rows)}, "
              f"last mid {rows[-1]['mid'] - args.glitch:.0f} d")
        return 0
    res = score()
    (t01.RESULTS / "B2-results.json").write_text(json.dumps(res, indent=1, default=float), encoding="utf-8")
    for x in res["intervals"]:
        print(f"tg {x['glitch']}: t_obs {x['t_obs']:.0f} | " + ", ".join(f"D{c['D']:.0f}:{c['t0']:.0f}" if c["t0"] else f"D{c['D']:.0f}:none" for c in x["curve"])
              + f" | e400 {x['e_400']:.3f} e_last {x['e_last']:.3f} | published {x['published_t_th']}")
    print({k: v for k, v in res.items() if k != "intervals"})
    return 0


if __name__ == "__main__":
    sys.exit(main())
