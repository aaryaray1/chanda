#!/usr/bin/env python3
"""T04: score every published, explicit pulsar next-glitch forecast against the Jodrell Bank catalogue (pre-registered scoring rules)."""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import t01_glitches as t01  # noqa: E402

FORECASTS = t01.HERE.parent / "data" / "t04" / "forecasts.json"
LARGE = 100.0  # Δν/ν ≥ 1e-7 in the catalogue's units of 1e-9
SNAPSHOT_MJD = 61364  # 2026-11-20


def epochs(g: list, target: str) -> list[float]:
    return [t for t, s in g if target == "any" or (s is not None and s >= LARGE)]


def baseline(g: list, f: dict) -> dict | None:
    past = [t for t in epochs(g, f["target"]) if t <= f["after_mjd"] + 1]
    if len(past) < 3:
        return None
    gaps = np.diff(past)
    mu, sd = float(np.mean(gaps)), float(np.std(gaps, ddof=1))
    return {"n_past": len(past), "anchor": past[-1], "mean_wait": mu, "sd_wait": sd, "forecast": past[-1] + mu}


def score(f: dict, g: list) -> dict:
    nxt = next((t for t in epochs(g, f["target"]) if t > f["after_mjd"] + (2 if f["after_mjd"] != f["published_mjd"] - 1 else 0)), None)
    r = {"id": f["id"], "pulsar": f["pulsar"], "kind": f["kind"], "actual": nxt,
         "prospective": None if nxt is None else nxt > f["published_mjd"] - 1, "catalogued_glitches": len(g)}
    b = baseline(g, f)
    if b:
        r["baseline"] = b
    if nxt is None:
        horizon = {"point": f.get("center", 0) + 2 * f.get("sigma", 0), "interval68": f.get("hi", 0) + (f.get("hi", 0) - f.get("center", 0)),
                   "lower_bound": float("inf"), "window": f.get("before", 0)}[f["kind"]]
        r["verdict"] = "pending" if SNAPSHOT_MJD < horizon else ("fail (window passed, none catalogued)" if f["kind"] == "window"
                                                                   else "overdue beyond 2σ (or not catalogued)")
        return r
    if f["kind"] == "point":
        z = (nxt - f["center"]) / f["sigma"]
        r.update(z=z, verdict="within 1σ" if abs(z) <= 1 else "within 2σ" if abs(z) <= 2 else "outside 2σ")
    elif f["kind"] == "interval68":
        half = (f["hi"] - f["center"]) if nxt >= f["center"] else (f["center"] - f["lo"])
        z = (nxt - f["center"]) / half
        r.update(z=z, verdict="within 68% interval" if f["lo"] <= nxt <= f["hi"] else ("within 2× interval" if abs(z) <= 2 else "outside 2× interval"))
    elif f["kind"] == "lower_bound":
        r["verdict"] = "true (after bound)" if nxt > f["bound"] else "false (before bound)"
    elif f["kind"] == "window":
        r["verdict"] = "true (inside window)" if nxt < f["before"] else "false (after window)"
        if b:
            w = f["before"] - f["published_mjd"]
            r["hp_probability_of_hit"] = 1 - math.exp(-w / b["mean_wait"])
    if b and f["kind"] in ("point", "interval68"):
        r["baseline_error_days"] = nxt - b["forecast"]
        r["forecast_error_days"] = nxt - f["center"]
        r["baseline_z_hp"] = (nxt - b["forecast"]) / b["mean_wait"]
        r["baseline_z_renewal"] = (nxt - b["forecast"]) / b["sd_wait"] if b["sd_wait"] > 0 else None
        r["closer"] = "forecast" if abs(nxt - f["center"]) < abs(nxt - b["forecast"]) else "baseline"
    return r


def summarise(rows: list[dict]) -> dict:
    zs = [r for r in rows if "z" in r]
    out = {"scored_numeric": len(zs), "within_1": sum(abs(r["z"]) <= 1 for r in zs), "within_2": sum(abs(r["z"]) <= 2 for r in zs),
           "mean_z": float(np.mean([r["z"] for r in zs])) if zs else None,
           "forecast_closer": sum(r.get("closer") == "forecast" for r in zs), "with_baseline": sum("closer" in r for r in zs)}
    pro = [r for r in zs if r["prospective"]]
    out["prospective_numeric"] = len(pro)
    out["prospective_within_1"] = sum(abs(r["z"]) <= 1 for r in pro)
    out["prospective_within_2"] = sum(abs(r["z"]) <= 2 for r in pro)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("cmd", choices=["selftest", "run"])
    args = ap.parse_args()
    forecasts = json.loads(FORECASTS.read_text(encoding="utf-8"))
    if args.cmd == "selftest":
        g = [(50000.0 + 400 * i, 500.0) for i in range(10)]
        f = {"id": "x", "pulsar": "Jtest", "published_mjd": 52000, "after_mjd": 51600, "target": "large", "kind": "point", "center": 52100, "sigma": 100}
        r = score(f, g)
        assert r["actual"] == 52000 and abs(r["z"] + 1) < 1e-9 and r["verdict"] == "within 1σ" and r["prospective"], r
        r = score(dict(f, kind="window", before=52100), g)
        assert r["verdict"].startswith("true"), r
        r = score(dict(f, after_mjd=53600, center=54000), g)
        assert r["verdict"] in ("pending", "overdue beyond 2σ (or not catalogued)"), r
        print("selftest OK")
        return 0
    cat = t01.parse_jbo((t01.DATA / "gTable.html").read_text(encoding="utf-8", errors="replace"))
    rows = [score(f, cat.get(f["pulsar"], [])) for f in forecasts]
    res = {"snapshot_mjd": SNAPSHOT_MJD, "rows": rows, "summary": summarise(rows)}
    (t01.RESULTS / "T04-results.json").write_text(json.dumps(res, indent=1, default=float), encoding="utf-8")
    for r in rows:
        extra = f"z={r['z']:+.2f}" if "z" in r else ""
        print(f"{r['id']:6} {r['pulsar']:11} actual={r['actual']} prospective={r['prospective']} {extra} -> {r['verdict']}"
              + (f" | closer: {r['closer']} (baseline z_HP {r['baseline_z_hp']:+.2f})" if "closer" in r else "")
              + (f" | HP P(hit) {r['hp_probability_of_hit']:.2f}" if "hp_probability_of_hit" in r else ""))
    print(json.dumps(res["summary"], indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
