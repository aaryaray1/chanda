# Pre-registration G1 · How predictable are pulsar glitches? A forecast competition

**Registered:** 2026-11-21, with `../analysis/g1_glitch_forecasts.py`. The code passed its self-test on synthetic data only. No backtest statistic had been computed on real data when this was committed.

## Question
T04 found that the published next-glitch forecasts cover their stated 1σ too rarely. But six resolved forecasts cannot say how predictable glitches actually are. G1 asks three questions:
1. **Predictability.** Do glitch waiting times carry structure that a forecaster can exploit out of sample, beyond a memoryless (Poisson) process?
2. **Mechanism.** Does a glitch's size predict the wait that follows, and in which direction? The two leading pictures predict opposite signs:
   - **Reservoir, or stress release** (the state-dependent Poisson model, vortex creep): a big glitch drains the reservoir, so the next wait is *longer*.
   - **Triggering, as in earthquakes** (the epidemic-type aftershock models of seismology): a big event raises the short-term rate, so the next wait is *shorter*.
3. **Physics gradient.** Is predictability larger in pulsars whose glitches are large (Vela-like) than in those whose glitches are small (Crab-like)?

**Method transfer.** The scoring is the one earthquake forecasting uses (the CSEP testing centres): each model issues a full predictive distribution before the event, and models are ranked by their out-of-sample log score. The information gain is the mean log-score difference, in nats per forecast.

## Data (fixed)
- **Catalogue:** the 2026-11-20 Jodrell Bank glitch catalogue snapshot, `../data/t01/gTable.html` (SHA-256 `e811419f…`), parsed by `t01_glitches.parse_jbo`. It is the same file T01 and T04 used.
- **Backtest set:** every pulsar with at least 8 catalogued glitches. There are 14, giving 231 forecasts. J0537−6910 alone contributes 63.
- **Units:** epochs in MJD, waits in days, sizes Δν/ν in units of 10⁻⁹. All glitches count, of any size.

## Forecast protocol (fixed)
- **Rolling origin.** For a pulsar with glitch epochs t₁ < … < t_N, a forecast is issued at each glitch k with at least 4 past waits. It is a predictive density for the next wait w_k = t_{k+1} − t_k, built only from glitches 1…k and their sizes.
- **Models.** Each is a posterior predictive with a noninformative prior, so parameter uncertainty is included.
  - **M0, Poisson:** exponential waits, with a Lomax predictive.
  - **M1, log-normal renewal:** log w is Student-t with n − 1 degrees of freedom, centred on the mean of past log waits, scale s√(1 + 1/n).
  - **M3, size-conditioned:** a linear regression of log w_j on log s_j over past pairs, giving a Student-t predictive at the current glitch's size. It falls back to M1 if fewer than 5 past pairs exist or the current size is missing.
- **Score.** The log predictive density at the realised wait. IG(A|B) = mean of [log p_A(w) − log p_B(w)].
- **Primary statistic: pulsar-averaged.** Each pulsar's mean IG, then the mean over pulsars, so each pulsar counts equally.
  - **Uncertainty:** a pulsar-block bootstrap, resampling pulsars, with 20 000 draws and seed 20261121.
  - **Secondary statistics:** the forecast-pooled IG, which is the CSEP convention, and the pooled IG without J0537−6910.
- **Synthetic check.** Under a pure Poisson process, IG(M1|M0) is about −0.17 nats (self-test data). A positive IG(M1|M0) is therefore conservative evidence against Poisson.

## Hypotheses and decision rules (fixed)
- **H1 · predictability.** The pulsar-averaged IG(M1|M0) > 0, with the one-sided 95% bootstrap lower bound above 0.
  - *Expected:* supported.
- **H2 · mechanism.** The pulsar-averaged IG(M3|M1) decides whether a glitch's size carries out-of-sample information about the next wait.
  - *Supported* if the lower 95% bound is above 0.
  - *Refuted* if the upper 95% bound is below 0.
  - *Inconclusive* otherwise.
  - The sign of the full-sample slope of log wait on log size is reported per pulsar: positive means reservoir-like, negative means triggering-like.
  - *Expected:* supported, with positive slopes in most pulsars.
- **H3 · physics gradient.** The Spearman correlation across pulsars between per-pulsar IG(M1|M0) and median log₁₀ glitch size is positive, with a one-sided permutation p < 0.05 (10 000 permutations).
  - *Expected:* supported.
- **H4 · calibration of M1.** M1's probability integral transforms (PIT) are uniform: KS p > 0.05, and coverage of the central 50% and 90% intervals is consistent with nominal (two-sided binomial p > 0.05).
  - *Expected:* roughly calibrated. That would contrast with T04's published forecasts.
  - PIT values within a pulsar are not independent, so the p-values are approximate.

**Sensitivity runs, declared now:**
- the inclusion threshold lowered to 6 glitches (`--min-glitches 6`, 30 pulsars);
- the pooled statistics with and without J0537−6910.

## Prospective forecasts (registered now, tested later)
- **What is forecast.** For every pulsar with at least 5 catalogued glitches, the code issues a next-glitch forecast from the snapshot. It gives quantiles at 5, 25, 50, 75 and 95% as MJD, both unconditional and conditional on no glitch before MJD 61364 (2026-11-20).
- **Model choice.** For pulsars in the backtest, the model with the highest summed backtest log score; otherwise M1. The forecasts are written to `../results/G1-results.json` by the same run that scores the backtest.
- **Evaluation.**
  - **When:** once a fresh catalogue shows a glitch after MJD 61364 in at least 15 of these pulsars, or on 2028-11-20, whichever comes first.
  - **Test:** take the first glitch after 61364 in each pulsar, compute its PIT under the conditional forecast, and test it for uniformity (KS) and for 50% and 90% coverage.
  - **Censoring:** pulsars with no new glitch are compared with the forecast survival probabilities.
- **Caveat.** Pulsars no longer monitored will look overdue. Coverage of southern pulsars after about 2018 is thin (see T02).

## What was already seen
- **T01** computed in-sample Spearman correlations between glitch size and the next wait (r₊) for these pulsars on this snapshot. So H2's in-sample analogue has been seen: strong positive r₊ in J1341−6220, J1413−6141 and J1048−5832, and weak or none in the Crab and J0631+1036.
- **Published:** quasi-periodicity in Vela and J0537−6910.
- **Seen while designing:** the inclusion counts (pulsars with at least 6, 8, 10, 12, 15 and 20 glitches), and that sizes are missing for 3 glitches and never non-positive.
- **Not computed before this commit:** no backtest information gain, no PIT, and no per-pulsar CV or slope on real data.

## Prior art (screen so far; full F3 after the run)
INSPIRE keyword searches on 2026-11-21:
- Carlin, Melatos & Vukcevic (2018), arXiv:1810.12458: Crab glitch epochs cluster at about 2σ (Ripley's K), and step-wise rate changes beat a homogeneous Poisson process (in-sample Bayes factors).
- Zhu & Zheng (2025), arXiv:2501.01862: "glitching clusters" in 27 pulsars, from the coefficient of variation.
- Liu et al. (2026), arXiv:2608.28523: two activity modes from the joint waiting-time–size distribution. The leave-one-out cross-validated AUC is 0.59.
- Melatos & Drummond (2019), arXiv:1910.05503: the state-dependent Poisson model as a better *post factum* predictor than HP for 2 of 3 pulsars.
- Carlin & Melatos (2019), arXiv:1907.09143: autocorrelations of waiting times and sizes.

None reports out-of-sample predictive skill across the population or compares reservoir and triggering models by forecast score. Novelty is judged only after the arXiv, OpenAlex and ADS-equivalent searches in F3.

## Limitations
- **Catalogue completeness.** It varies across decades and observatories. Missed glitches lengthen observed waits and can mimic structure.
- **Weighting.** Pulsars with many glitches dominate the pooled statistic, which is why the primary statistic is pulsar-averaged.
- **Model set.** Three simple models only. A self-exciting (Hawkes) model is not fitted, because 8–68 events per pulsar cannot identify it. The size-conditioned model carries the triggering-versus-reservoir contrast through the sign of its slope.
