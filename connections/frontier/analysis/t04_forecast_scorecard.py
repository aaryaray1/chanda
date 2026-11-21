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


def anchor(f: dict) -> float:
    return f.get("anchor_catalogue_mjd", f["after_mjd"])  # the same anchor glitch, as dated by the catalogue


def next_glitch(g: list, f: dict, target: str) -> float | None:
    from_now = f["after_mjd"] >= math.floor(f["published_mjd"]) - 1  # forecasts phrased from the publication date
    return next((t for t in epochs(g, target) if t > anchor(f) + (0 if from_now else 2)), None)


def baseline(g: list, f: dict) -> dict | None:
    past = [t for t in epochs(g, f["target"]) if t <= anchor(f) + 1]
    if len(past) < 3:
        return None
    gaps = np.diff(past)
    mu, sd = float(np.mean(gaps)), float(np.std(gaps, ddof=1))
    return {"n_past": len(past), "anchor": past[-1], "mean_wait": mu, "sd_wait": sd, "forecast": past[-1] + mu}


def verdict(f: dict, nxt: float | None) -> dict:
    r: dict = {}
    if nxt is None:
        horizon = {"point": f.get("center", 0) + 2 * f.get("sigma", 0), "interval68": f.get("hi", 0) + (f.get("hi", 0) - f.get("center", 0)),
                   "lower_bound": float("inf"), "window": f.get("before", 0), "window_between": f.get("hi", 0)}[f["kind"]]
        r["verdict"] = "pending" if SNAPSHOT_MJD < horizon else ("false (window passed, none catalogued)" if f["kind"].startswith("window")
                                                                   else "overdue beyond 2σ (or not catalogued)")
        quiet = f.get("no_glitch_until_mjd")  # post hoc (referee round 2): the source's own data show no glitch up to this date
        if f["kind"] == "point" and quiet and quiet > horizon:
            r.update(verdict="overdue beyond 2σ (confirmed by the source's own data)", z_lower_bound=(quiet - f["center"]) / f["sigma"])
        if r["verdict"].startswith("overdue") and f["kind"] == "point":
            r["overdue_at_publication"] = f["published_mjd"] > horizon
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
    elif f["kind"] == "window_between":
        r["verdict"] = "true (inside window)" if f["lo"] <= nxt <= f["hi"] else "false (outside window)"
    return r


def score(f: dict, g: list) -> dict:
    nxt = next_glitch(g, f, f["target"])
    r = {"id": f["id"], "pulsar": f["pulsar"], "kind": f["kind"], "event": f.get("event"), "primary": f.get("primary", True),
         "addendum": f.get("addendum", False), "actual": nxt, "catalogued_glitches": len(g),
         "prospective": None if nxt is None else nxt > f["published_mjd"] - 1,
         "prospective_strict": None if nxt is None else nxt > f["published_mjd"]}
    if "prospective_label" in f:
        r["prospective_label"] = f["prospective_label"]
    r.update(verdict(f, nxt))
    b = baseline(g, f)
    if b:
        r["baseline"] = b
        if f["kind"] == "window":
            r["hp_probability_of_hit"] = 1 - math.exp(-(f["before"] - f["published_mjd"]) / b["mean_wait"])
        if f["kind"] == "lower_bound":
            r["hp_probability_bound_holds_from_anchor"] = math.exp(-(f["bound"] - b["anchor"]) / b["mean_wait"])
            if "data_end_mjd" in f:
                r["hp_probability_bound_holds_given_data_end"] = math.exp(-max(0.0, f["bound"] - f["data_end_mjd"]) / b["mean_wait"])
    if "alt_target" in f:
        alt = next_glitch(g, f, f["alt_target"])
        r["alt_target"] = {"target": f["alt_target"], "actual": alt, **verdict(f, alt)}
    if b and nxt is not None and f["kind"] in ("point", "interval68"):
        r["baseline_error_days"] = nxt - b["forecast"]
        r["forecast_error_days"] = nxt - f["center"]
        r["baseline_z_hp"] = (nxt - b["forecast"]) / b["mean_wait"]
        r["baseline_z_renewal"] = (nxt - b["forecast"]) / b["sd_wait"] if b["sd_wait"] > 0 else None
        r["closer"] = "forecast" if abs(nxt - f["center"]) < abs(nxt - b["forecast"]) else "baseline"
        if f["kind"] == "point" and b["sd_wait"] > 0:  # post hoc (referee): Gaussian log scores, forecast vs renewal baseline
            ls = lambda x, m, s: -0.5 * ((x - m) / s) ** 2 - math.log(s * math.sqrt(2 * math.pi))
            r["logscore_forecast"] = ls(nxt, f["center"], f["sigma"])
            r["logscore_renewal"] = ls(nxt, b["forecast"], b["sd_wait"])
    return r


def chi2_sf(x: float, k: int) -> float:
    a, y = k / 2, x / 2
    term = total = 1.0 / math.gamma(a + 1)
    for n in range(1, 500):
        term *= y / (a + n)
        total += term
    return max(0.0, 1.0 - y ** a * math.exp(-y) * total)


def summarise(rows: list[dict], primary_only: bool, registered_pool: bool) -> dict:
    use = [r for r in rows if (r["primary"] or not primary_only) and (not r["addendum"] or not registered_pool)]
    zs = [r for r in use if "z" in r]
    out = {"forecasts": len(use), "scored_numeric": len(zs), "within_1": sum(abs(r["z"]) <= 1 for r in zs),
           "within_2": sum(abs(r["z"]) <= 2 for r in zs),
           "mean_z": float(np.mean([r["z"] for r in zs])) if zs else None, "median_z": float(np.median([r["z"] for r in zs])) if zs else None,
           "forecast_closer": sum(r.get("closer") == "forecast" for r in zs), "with_baseline": sum("closer" in r for r in zs)}
    for key, flag in (("prospective_registered", "prospective"), ("prospective_strict", "prospective_strict")):
        pro = [r for r in zs if r[flag]]
        out.update({f"{key}_numeric": len(pro), f"{key}_within_1": sum(abs(r["z"]) <= 1 for r in pro),
                    f"{key}_within_2": sum(abs(r["z"]) <= 2 for r in pro)})
    over = [r for r in use if r["kind"] == "point" and r["verdict"].startswith("overdue")]
    out.update(overdue_point=len(over), overdue_point_ids=[r["id"] for r in over],
               overdue_point_prospective=sum(not r["overdue_at_publication"] for r in over),
               past_horizon_numeric=len(zs) + len(over))
    if zs:
        s = sum(r["z"] ** 2 for r in zs)
        out["posthoc_sum_z2"] = s
        out["posthoc_sum_z2_p"] = chi2_sf(s, len(zs))
    ls = [r for r in zs if "logscore_forecast" in r]
    if ls:
        out["posthoc_logscore_forecast_wins"] = sum(r["logscore_forecast"] > r["logscore_renewal"] for r in ls)
        out["posthoc_logscore_n"] = len(ls)
    out["verdicts"] = {r["id"]: r["verdict"] for r in use if "z" not in r}
    return out


def main() -> int:
    global SNAPSHOT_MJD
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("cmd", choices=["selftest", "run"])
    ap.add_argument("--catalogue", default=str(t01.DATA / "gTable.html"), help="a Jodrell Bank gTable.html; default the 2026-11-20 snapshot")
    ap.add_argument("--snapshot-mjd", type=float, default=SNAPSHOT_MJD, help="the date the catalogue was fetched, for pending/overdue")
    args = ap.parse_args()
    forecasts = json.loads(FORECASTS.read_text(encoding="utf-8"))
    if args.cmd == "selftest":
        g = [(50000.0 + 400 * i, 500.0) for i in range(10)]
        f = {"id": "x", "pulsar": "Jtest", "published_mjd": 52000, "after_mjd": 51600, "target": "large", "kind": "point", "center": 52100, "sigma": 100}
        r = score(f, g)
        assert r["actual"] == 52000 and abs(r["z"] + 1) < 1e-9 and r["verdict"] == "within 1σ", r
        assert r["prospective"] is True and r["prospective_strict"] is False, r  # glitch on the publication day: registered yes, strict no
        assert score(dict(f, published_mjd=51999.5), g)["prospective_strict"] is True
        r = score(dict(f, kind="window", before=52100, after_mjd=51999, published_mjd=51999), g)
        assert r["verdict"].startswith("true"), r
        r = score(dict(f, kind="window_between", lo=52300, hi=52500), g)
        assert r["actual"] == 52000 and r["verdict"] == "false (outside window)", r
        assert score(dict(f, kind="window_between", lo=51900, hi=52100), g)["verdict"] == "true (inside window)"
        r = score(dict(f, after_mjd=53600, center=54000), g)
        assert r["verdict"] == "overdue beyond 2σ (or not catalogued)" and r["overdue_at_publication"] is False, r
        r = score(dict(f, after_mjd=53600, center=54000, no_glitch_until_mjd=54500), g)
        assert r["verdict"].startswith("overdue beyond 2σ (confirmed") and abs(r["z_lower_bound"] - 5) < 1e-9, r
        mixed = [(50000.0 + 400 * i, 500.0 if i % 2 else 5.0) for i in range(10)]
        r = score(dict(f, target="any", alt_target="large", after_mjd=50000, center=50400, sigma=50, published_mjd=50450), mixed)
        assert r["actual"] == 50400 and r["alt_target"]["actual"] == 50400, r
        r = score(dict(f, target="any", alt_target="large", after_mjd=50400, center=50800, sigma=50, published_mjd=50850), mixed)
        assert r["actual"] == 50800 and r["alt_target"]["actual"] == 51200, r
        r = score(dict(f, kind="lower_bound", bound=53900, after_mjd=53600, data_end_mjd=53800), g)
        assert abs(r["hp_probability_bound_holds_given_data_end"] - math.exp(-100 / 400)) < 1e-9, r
        rows = [score(dict(f, id=k, primary=pr, addendum=ad, center=c, after_mjd=an), g) for k, pr, ad, c, an in
                (("a", True, False, 52100, 51600), ("b", False, False, 52000, 51600), ("c", True, True, 52500, 51600), ("d", True, False, 54000, 53600))]
        s1, s2 = summarise(rows, primary_only=False, registered_pool=True), summarise(rows, primary_only=True, registered_pool=False)
        assert (s1["forecasts"], s1["scored_numeric"], s1["within_1"], s1["overdue_point"], s1["past_horizon_numeric"]) == (3, 2, 2, 1, 3), s1
        assert (s2["forecasts"], s2["scored_numeric"], s2["within_2"], s2["overdue_point"], s2["overdue_point_ids"]) == (3, 2, 1, 1, ["d"]), s2
        assert abs(chi2_sf(18.92, 6) - 0.0043) < 0.0005, chi2_sf(18.92, 6)
        print("selftest OK")
        return 0
    SNAPSHOT_MJD = args.snapshot_mjd
    cat = t01.parse_jbo(Path(args.catalogue).read_text(encoding="utf-8", errors="replace"))
    rows = [score(f, cat.get(f["pulsar"], [])) for f in forecasts]
    res = {"snapshot_mjd": SNAPSHOT_MJD, "rows": rows,
           "summary_registered_pool_all": summarise(rows, primary_only=False, registered_pool=True),
           "summary_full_pool_primary_per_event": summarise(rows, primary_only=True, registered_pool=False)}
    name = "T04-results.json" if args.catalogue == str(t01.DATA / "gTable.html") else f"T04-results-{int(SNAPSHOT_MJD)}.json"
    (t01.RESULTS / name).write_text(json.dumps(res, indent=1, default=float), encoding="utf-8")
    for r in rows:
        extra = f"z={r['z']:+.2f}" if "z" in r else ""
        print(f"{r['id']:6} {r['pulsar']:11} {'P' if r['primary'] else 's'}{'+' if r['addendum'] else ' '} actual={r['actual']} strict-prosp={r['prospective_strict']} {extra} -> {r['verdict']}"
              + (f" | closer: {r['closer']}" if "closer" in r else "")
              + (f" | LS fc {r['logscore_forecast']:.2f} vs base {r['logscore_renewal']:.2f}" if "logscore_forecast" in r else "")
              + (f" | HP P(hit) {r['hp_probability_of_hit']:.2f}" if "hp_probability_of_hit" in r else "")
              + (f" | alt[{r['alt_target']['target']}]: {r['alt_target']['verdict']}" if "alt_target" in r else ""))
    for k in ("summary_registered_pool_all", "summary_full_pool_primary_per_event"):
        print(k, json.dumps(res[k], indent=1, default=float))
    return 0


if __name__ == "__main__":
    sys.exit(main())
