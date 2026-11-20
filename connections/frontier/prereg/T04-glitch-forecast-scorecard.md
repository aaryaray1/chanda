# Pre-registration T04 · How good are published pulsar-glitch forecasts?

**Registered:** 2026-11-21, with `../data/t04/forecasts.json` and `../analysis/t04_forecast_scorecard.py`.

## Question
Pulsar-glitch models are increasingly used to forecast the date of a pulsar's next glitch:
- the vortex-creep model (Alpar, Gügercinoğlu, Akbal and collaborators);
- the state-dependent Poisson model (Melatos and collaborators);
- glitch clustering (Zhu and collaborators).

Are those forecasts accurate, and are their stated uncertainties honest? If they are calibrated, about 68% of outcomes should fall within 1σ and 95% within 2σ.

## The forecast pool (fixed)
- **What counts:** every explicit forecast found that gives a date for a pulsar's next glitch, with an uncertainty, a window or a bound, in the *first arXiv version* of a paper. All 12 are in `forecasts.json`, each with its verbatim quote and the version it came from.
- **How they were found:** arXiv searches on 2026-11-21 ("next glitch", "predict the next glitch", "glitch prediction", "time of the next glitch", "vortex creep model", "inter-glitch time", "glitch epoch", "next Vela glitch"), and the full text of every candidate.
- **Later versions don't count:** forecasts that appear only in a version posted after the event are excluded. Two examples:
  - Akbal et al. (2017), v3, replaced its v1 forecast after the 12 December 2016 Vela glitch.
  - Gügercinoğlu et al. (2022), v2, re-fitted J2229+6114 after its 2021 glitch.

  J1023−5746's forecast first appears in v2 (MJD 59611), before its forecast epoch but inside its own 1σ window. It is included and flagged.
- **What the forecasts look like:**
  - point forecast (centre ± σ): 9;
  - 68% credible interval: 1 (Grover et al. 2025, for Vela, still open);
  - lower bound: 1;
  - window: 1.

## What was already seen
- **Outcomes reported in the papers themselves:** several forecast papers report their own outcomes in later text:
  - the Vela glitches of 2016-12-12 and 2021-07-23 (in Akbal et al. v1 and Gügercinoğlu et al. v2);
  - the Crab glitches of 2025-07-17 and 2025-08-06 (in Zhu et al. v2);
  - J2229+6114's glitch at MJD 59270 (in Gügercinoğlu et al. v2).
- **The three 2019 forecasts** were already scored in T03.
- **Outcomes not seen:** catalogue epochs for J2111+4606, J1023−5746, and Vela after MJD 60430 were not inspected.

This is a compilation, so pre-registration protects the scoring rule, not ignorance of every outcome. The inclusion rule and the scoring are mechanical, and both are fixed here.

## Scoring (fixed)
- **Outcome:** the first glitch in the 2026-11-20 Jodrell Bank snapshot after the forecast's anchor.
  - The anchor is the last glitch in the forecaster's data, or the publication date for forecasts phrased from "now" (Akbal et al. 2017; Zhu et al. 2025).
  - **Target class:** forecasts of the next "large" glitch (all vortex-creep forecasts) count only glitches with Δν/ν ≥ 10⁻⁷. The others count any glitch.
- **Point forecasts:** z = (actual − centre)/σ.
  - Verdicts: within 1σ, within 2σ, or outside 2σ.
- **Interval forecasts:** z is scaled by the half-width on the side where the outcome falls.
  - Verdict: within the 68% interval if the outcome is inside it.
- **Bounds and windows:** true or false.
  - For a window forecast, also report the homogeneous-Poisson (HP) probability that a glitch falls inside the window by chance. That measures how informative the window is.
- **Pending:** a forecast with no outcome is *pending* while the snapshot date (MJD 61364) is before centre + 2σ (for intervals, hi + the upper half-width). After that it is *overdue*. An overdue result may also mean a glitch that was never catalogued: J2111+4606 and J1023−5746 are timed mainly by Fermi-LAT.
- **Baselines.** Built from the same pulsar's target-class glitches up to the anchor (at least 3 needed). Let μ be the mean wait and s the standard deviation of the waits.
  - **HP:** anchor + μ, with σ = μ.
  - **Renewal:** anchor + μ, with σ = s.

  For each point or interval forecast, record whether the published forecast or the baseline lands closer to the outcome.
- **Summary:**
  - the fraction of resolved numeric forecasts within 1σ and 2σ, overall and for *prospective* forecasts only (the outcome came after publication);
  - the mean z;
  - wins against the baseline.

## Limitations
- **Small pool:** 12 forecasts from 5 papers by 3 groups. Calibration can be judged only coarsely.
- **Catalogue gaps:** the catalogue may lack glitches, especially for γ-ray-only pulsars and for recent years.
- **Not independent:** the forecasts of one model share parameters, and several concern Vela.
