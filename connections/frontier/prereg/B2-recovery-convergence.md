# Pre-registration B2 · Does the vortex-creep recovery time depend on where the data end?

**Registered:** 2026-11-27, after B1's results and before any photon later than t_g + 410 d was downloaded. B2 reuses B1's frozen pipeline (`analysis/b1_vela.py`, commit `c3ed7a1`) unchanged. A new script `analysis/b2_convergence.py` only extends the fit window.

## Why
Two earlier results pull in opposite directions:
- **B1:** the recovery relation t₀ = (ν̇_pre − ν̇_post)/ν̈, measured blind from data within 400 d after each Vela glitch, predicted every next glitch too early (5 of 5).
- **V1:** published fits that use data through the next glitch agree with the observed intervals (median |ln| error 0.093).

One explanation covers both. If the recovery slows over the interval, then a linear fit's ν̈ falls and t₀ rises as the fit window extends. The fitted t₀ then reaches the observed interval only when the data reach the next glitch. In-sample agreement would be partly set by where the data stop, not predicted.

**B2 tests that directly** on the same five intervals.

## Data (fixed)
- **The new stretches:** the rest of each interval, from t_g + 410 d to t_{g+1} − 7 d, fetched like B1's data (five LAT queries, 1°, 100 MeV–300 GeV, spacecraft files):
  - 2010: 55818–56549
  - 2013: 56966–57728
  - 2016: 58145–58509
  - 2019: 58926–59410
  - 2021: 59828–60423
- **Measurement:** B1's 14-day H-test windows, unchanged, continuing B1's post-glitch window grid.

## Statistics (fixed)
- **The fit.** For each interval, fit a quadratic to ν(t) over [t_g + 100 d, t_g + D] for each D in {300, 400, 500, …} in 100-d steps, plus the last D = t_obs − 7 d. Then t₀(D) = (ν̇_pre − ν̇_post(D))/ν̈(D), with ν̇_pre from B1.
- **H_B2a, drift.** t₀ grows as the window extends: t₀(D_last) > t₀(300) in each interval.
  - *Supported* if this holds in 5 of 5 intervals (one-sided sign test, p = 0.031).
  - *Refuted* if it holds in at most 2.
- **H_B2b, agreement only at the end.** The full-window estimate matches the outcome better than the 400-d estimate: |ln(t₀(D_last)/t_obs)| < |ln(t₀(400)/t_obs)| in at least 4 of 5, **and** the median |ln(t₀(D_last)/t_obs)| ≤ 0.10. That is V1's in-sample level.
- **Pre-stated readings:**

| H_B2a | H_B2b | Reading |
|---|---|---|
| supported | supported | the in-sample agreement is largely a data-window effect |
| supported | not supported | the recovery slows, but even full-window fits do not reproduce the intervals |
| refuted | — | t₀ is stable, so B1's early estimates are the relation's real predictions, and Vela glitches well after it has recovered |

**Also reported:** the curve t₀(D) for each interval, and the full-window t₀ next to the published in-sample t_th.

## What is already known
- All of B1, including that the blind t₀ is early in 5 of 5 intervals and the ν(t) series up to t_g + 410 d.
- The glitch epochs and the published t_th.
- **Not inspected:** any photon later than t_g + 410 d.

## Limitations
- **One model form.** The linear-recovery (quadratic ν) form is the one tested. Drift is its signature of a recovery that is not linear, and a richer model might absorb it.
- **Overlapping windows.** The t₀(D) for one interval share data, so they are not independent. The sign test counts intervals, not windows.
