#!/usr/bin/env python3
"""V1 post hoc (revised after the referee): vortex-creep forecasts made before the next glitch, each against its own baseline; and every case where one glitch was analysed before and after its successor."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
R = ROOT / "results"
SNAP = 61364
PAIRS = json.loads((ROOT / "data" / "v1" / "pairs.json").read_text(encoding="utf-8"))["pairs"]


def own_baseline(pulsar: str, before_mjd: float) -> float | None:
    prev = [p["t_obs"] for p in PAIRS if p["pulsar"] == pulsar and p.get("epoch_mjd", 1e9) < before_mjd]
    return math.exp(sum(map(math.log, prev)) / len(prev)) if prev else None


cases = [  # name, t_th, interval start, outcome MJD or None, class, source
    ("GU20a Vela 2019", 769, 58515.6, 59417.2, "clean: fit and posting before the next glitch", "arXiv:2011.14788v1 (Nov 2020)"),
    ("GU20c J2229+6114 G9", 619, 58396, 59262.0, "not clean: zero-dof fit, stated in v1 as a lower bound ('later than mid June 2020'), which was met",
     "arXiv:2011.14788v1"),
    ("AK17a Vela", 1364, 56922, 57734.5, "contemporaneous: posted about 6 h after the glitch", "arXiv:1612.03805v1"),
    ("GU22d J1023-5746 G7", 862, 58823, None, "prospective, overdue (or a glitch missing from the catalogue)", "arXiv:2011.14788v2"),
    ("GU20b J2111+4606 G2", 2140, 57562, None, "prospective, overdue (or missing from the catalogue)", "arXiv:2011.14788v1"),
    ("LI24b J1420-6048 G8", 823, 58555, None, "already failed at publication: the predicted date (and the paper's own data to MJD 59453) passed before posting", "arXiv:2408.15022v1"),
    ("LI24c J1709-4429 G6", 1850, 58175, None, "already past at publication (predicted MJD 60025, posted 60549)", "arXiv:2408.15022v1"),
]
rows = []
for name, th, t0, out, cls, src in cases:
    r = {"forecast": name, "class": cls, "t_th": th, "source": src}
    pulsar = name.split()[1]
    pulsar = {"Vela": "J0835-4510"}.get(pulsar, pulsar)
    if out:
        t_obs = out - t0
        b = own_baseline(pulsar, t0)
        r.update(t_obs=round(t_obs, 1), abs_ln_error=round(abs(math.log(th / t_obs)), 3),
                 own_baseline_days=round(b, 1) if b else None, baseline_abs_ln_error=round(abs(math.log(b / t_obs)), 3) if b else None)
    else:
        r["t_obs"] = f"> {SNAP - t0:.0f} d if no glitch is missing from the catalogue"
    rows.append(r)
revisions = [
    {"glitch": "J2229+6114, 2018 glitch", "same_group": True, "before": 619, "before_interval": 866, "after": 857, "after_interval": 845,
     "what_changed": "epoch re-dated 58396 -> 58425; data extended from MJD 58865 to 59473 (through the next glitch); nonlinear IA/tau_nl/t0 component dropped; an error-free zero-dof fit replaced",
     "before_source": "arXiv:2011.14788v1", "after_source": "arXiv:2011.14788v2"},
    {"glitch": "Vela 2019 glitch", "same_group": False, "before": 769, "before_interval": 902, "after": 921.6, "after_interval": 902,
     "what_changed": "the same group's v2 (Feb 2022, after the outcome) kept 769 d and footnoted the miss; 921.6 d is Grover et al. (different team, Gugercinoglu co-author) from full-interval radio data with a t0 prior whose initial guess was 'often chosen close to the observed time to the next glitch'",
     "before_source": "arXiv:2011.14788v1", "after_source": "arXiv:2506.02100"},
    {"glitch": "Vela 2013/2014", "same_group": True, "before": 1364, "before_interval": 812.5, "after": 1553, "after_interval": 1178.5,
     "what_changed": "v1 forecast 1364 d from the small 2014 glitch; v3 (after the outcome) re-anchored on 2013 with 1553 d, still 375 d late; GU22 later gave 1862 d for the same interval (error 0.458)",
     "before_source": "arXiv:1612.03805v1", "after_source": "arXiv:1612.03805v3"},
]
for r in revisions:
    r["error_before"] = round(abs(math.log(r["before"] / r["before_interval"])), 3)
    r["error_after"] = round(abs(math.log(r["after"] / r["after_interval"])), 3)
v1 = json.loads((R / "V1-results.json").read_text(encoding="utf-8"))["primary"]["H_V2"]
out = {"note": "post hoc, revised after the referee (2026-11-21); not registered; n = 1-3 per category, so suggestive only",
       "prospective_and_related": rows, "in_sample_median_abs_ln_error": round(v1["median_error_model"], 3),
       "in_sample_baseline_median_abs_ln_error": round(v1["median_error_baseline"], 3), "before_after": revisions}
(R / "V1-contrast-posthoc.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
for r in rows:
    print(r["forecast"], "|", r.get("abs_ln_error"), "vs own baseline", r.get("baseline_abs_ln_error"), "|", r["class"][:60])
for r in revisions:
    print(r["glitch"], r["error_before"], "->", r["error_after"], "same group" if r["same_group"] else "different team")
