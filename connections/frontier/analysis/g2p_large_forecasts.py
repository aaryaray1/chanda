#!/usr/bin/env python3
"""G2-P: register next-large-glitch forecasts (Δν/ν ≥ 1e-7) for the G2 large-class pulsars, model chosen by the G2 backtest."""
from __future__ import annotations

import datetime
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import g1_glitch_forecasts as g1  # noqa: E402
import g2_two_populations as g2  # noqa: E402
import t01_glitches as t01  # noqa: E402

QS = (0.05, 0.16, 0.25, 0.5, 0.75, 0.84, 0.95)


def date(mjd: float) -> str:
    return (datetime.date(1858, 11, 17) + datetime.timedelta(days=round(mjd))).isoformat()


def main() -> int:
    cat = t01.parse_jbo((t01.DATA / "gTable.html").read_text(encoding="utf-8", errors="replace"))
    large = g2.split(cat, g2.THRESHOLD)["large"]
    rows = json.loads((t01.RESULTS / "G2-results.json").read_text(encoding="utf-8"))["backtest_rows"]["large"]
    out = []
    for p, bt in sorted(rows.items()):
        g = large[p]
        times, sizes = [t for t, s in g], [s for t, s in g]
        model = max(g1.MODELS, key=lambda m: sum(r[f"ls_{m}"] for r in bt))
        f = g1.predictives(times, sizes, len(times) - 1)[model]
        w0 = g1.SNAPSHOT_MJD - times[-1]
        cond = {str(q): round(times[-1] + f.quantile(q, w0), 1) for q in QS}
        pr = g1.predictives(times, sizes, len(times) - 1)
        alt = {m: {"conditional_on_none_before_snapshot_mjd": {str(q): round(times[-1] + pr[m].quantile(q, w0), 1) for q in QS},
                   "prob_in_GR25_window_given_none_before_snapshot": round((pr[m].cdf(61506 - times[-1]) - pr[m].cdf(w0)) / (1 - pr[m].cdf(w0)), 4)}
               for m in g1.MODELS}
        out.append({"pulsar": p, "large_glitches": len(times), "all_models": alt, "last_large_mjd": times[-1], "last_large_size_1e-9": sizes[-1], "model": model,
                    "backtest_logscore": {m: round(sum(r[f"ls_{m}"] for r in bt), 2) for m in g1.MODELS},
                    "prob_large_before_snapshot": round(f.cdf(w0), 4),
                    "unconditional_mjd": {str(q): round(times[-1] + f.quantile(q), 1) for q in QS},
                    "conditional_on_none_before_snapshot_mjd": cond,
                    "conditional_median_date": date(cond["0.5"]), "conditional_68pct_dates": [date(cond["0.16"]), date(cond["0.84"])]})
    res = {"registered": "2026-11-21", "snapshot_mjd": g1.SNAPSHOT_MJD, "threshold_1e-9": g2.THRESHOLD, "forecasts": out}
    (t01.RESULTS / "G2P-large-glitch-forecasts.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
    vela = next(r for r in out if r["pulsar"] == "J0835-4510")
    for m, v in vela["all_models"].items():
        c = v["conditional_on_none_before_snapshot_mjd"]
        print(f"Vela {m}: median {date(c['0.5'])}, 68% [{date(c['0.16'])}, {date(c['0.84'])}], P(large glitch by 2027-04-11) = {v['prob_in_GR25_window_given_none_before_snapshot']:.2f}")
    for r in out:
        c = r["conditional_on_none_before_snapshot_mjd"]
        print(f"{r['pulsar']:12} n={r['large_glitches']:2} last={date(r['last_large_mjd'])} {r['model']} P(before snap)={r['prob_large_before_snapshot']:.2f} "
              f"median {r['conditional_median_date']} 68% {r['conditional_68pct_dates']} 90% [{date(c['0.05'])}, {date(c['0.95'])}]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
