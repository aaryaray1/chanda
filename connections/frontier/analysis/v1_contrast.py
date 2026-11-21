#!/usr/bin/env python3
"""V1 post hoc: in-sample vortex-creep t_th errors (V1) against the prospective forecasts scored in T04, and before/after revisions."""
import json
import math
from pathlib import Path

R = Path(__file__).resolve().parent.parent / "results"
SNAP = 61364
prospective = [  # model t_th, interval start (paper's anchor), outcome (next glitch MJD or None), source (first arXiv version, before the outcome)
    ("AK17a Vela", 1364, 56922, 57734.5, "arXiv:1612.03805v1; contemporaneous (posted ~6 h after the glitch)"),
    ("GU20a Vela", 769, 58515.6, 59417.2, "arXiv:2011.14788v1"),
    ("GU20c J2229+6114", 619, 58396, 59262.0, "arXiv:2011.14788v1 (paper's epoch for G9; catalogue 58424)"),
    ("LI24b J1420-6048", 823, 58555, None, "arXiv:2408.15022v1; the paper's own data show no glitch to MJD 59453"),
    ("GU22d J1023-5746", 862, 58823, None, "arXiv:2011.14788v2"),
    ("GU20b J2111+4606", 2140, 57562, None, "arXiv:2011.14788v1"),
    ("LI24c J1709-4429", 1850, 58175, None, "arXiv:2408.15022v1"),
]
rows = []
for name, th, t0, out, src in prospective:
    if out:
        rows.append({"forecast": name, "t_th": th, "t_obs": round(out - t0, 1), "abs_ln_error": round(abs(math.log(th / (out - t0))), 3), "source": src})
    else:
        lb_paper = (59453 - t0) if "59453" in src else None
        rows.append({"forecast": name, "t_th": th, "t_obs": f"> {SNAP - t0:.0f} if no glitch is missing from the catalogue",
                     "abs_ln_error_lower_bound_if_catalogue_complete": round(abs(math.log((SNAP - t0) / th)), 3),
                     **({"abs_ln_error_lower_bound_from_paper_data": round(math.log(lb_paper / th), 3)} if lb_paper else {}), "source": src})
resolved = sorted(r["abs_ln_error"] for r in rows if "abs_ln_error" in r)
revisions = [
    {"glitch": "J2229+6114 G9 (2018)", "before": 619, "after": 857, "t_obs": 845, "before_source": "arXiv:2011.14788v1 (Nov 2020)", "after_source": "arXiv:2011.14788v2 (Feb 2022)"},
    {"glitch": "Vela 2019", "before": 769, "after": 921.6, "t_obs": 902, "before_source": "arXiv:2011.14788v1 (Nov 2020; v2 kept 769)", "after_source": "arXiv:2506.02100 (Grover et al. 2025)"},
]
for r in revisions:
    r["error_before"], r["error_after"] = round(abs(math.log(r["before"] / r["t_obs"])), 3), round(abs(math.log(r["after"] / r["t_obs"])), 3)
v1 = json.loads((R / "V1-results.json").read_text(encoding="utf-8"))["primary"]["H_V2"]
out = {"note": "post hoc, after V1; not registered", "prospective": rows, "prospective_resolved_median_abs_ln_error": resolved[len(resolved) // 2],
       "in_sample_median_abs_ln_error": round(v1["median_error_model"], 3), "baseline_median_abs_ln_error": round(v1["median_error_baseline"], 3),
       "before_after_revisions": revisions}
(R / "V1-contrast-posthoc.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
print(json.dumps(out, indent=1))
