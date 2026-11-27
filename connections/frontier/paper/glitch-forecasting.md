# Pulsar glitches as a forecasting problem: out-of-sample tests of predictability, glitch classes, aftershocks and vortex-creep interglitch times

*Research note from this project's frontier stage, 2026-11-27. Every result below was pre-registered (the plan committed to git before the data were scored) and refereed. The full write-ups, code and commit hashes are linked under Reproducibility. Confidence labels follow the project's conventions.*

## Summary
Pulsar glitch models are increasingly used to forecast when a pulsar will glitch next. We treat that as a forecasting problem and borrow the evaluation method of earthquake forecasting (the CSEP testing centres): every model issues a full predictive distribution before the event, and is scored by its out-of-sample log score. We apply it to the Jodrell Bank glitch catalogue (snapshot 2026-11-20; 736 glitches in 225 pulsars), and to every explicit next-glitch prediction we could find in the literature. Five findings:

1. **Published forecasts.** Of 6 resolved primary forecasts, 2 fell within their stated 1σ; 4 more are overdue, one of them a confirmed miss. That is too few to judge calibration, but the misses are large. *(T04)*
2. **A simple statistical forecast is calibrated.** A two-parameter log-normal renewal model covers 208 of 231 out-of-sample outcomes with its 90% intervals (KS p = 0.55). Against a calibrated Poisson null, glitch timing is significantly non-Poisson, but the gain over a memoryless forecast is small: +0.1 nats per forecast. *(G1; established in direction, current research in size)*
3. **Two kinds of glitch.**
   - Large glitches (Δν/ν ≥ 10⁻⁷) are clearly non-Poisson, and a larger glitch is followed by a longer wait in every pulsar tested (7 of 7; 14 of 14 with a looser cut). Post-glitch recovery cannot hide large glitches, so this sign is physical.
   - Small glitches are consistent with Poisson, and their sizes carry no forward information.
   - This confirms out of sample, at one fixed threshold, a two-trigger picture proposed in-sample by Fuentes et al. (2019). *(G2; current research)*
4. **No aftershocks at catalogue resolution.** Quick follow-up glitches neither cluster after large glitches nor come out smaller, as earthquake aftershocks do. An apparent deficit of quick follow-ups is entirely below about a month, the catalogue's effective resolution. *(G3; current research)*
5. **Vortex-creep "times to the next glitch": partly consistent in hindsight, no blind skill on Vela.**
   - Across 35 published pairs, the model's t_th tracks the observed interval within pulsars (ρ = +0.66) and beats the pulsar's own mean interval in 25 of 34 cases.
   - But glitch size alone tracks the intervals almost as well (ρ = +0.46), and the fits use data through the next glitch.
   - The one clean forecast made beforehand did worse than the pulsar's own mean.
   - **Blind test on Vela (B1).** Measured from Fermi-LAT photons using only data within 410 d after each glitch, the constant-ν̈ form t₀ = (ν̇_pre − ν̇_post)/ν̈ shows no blind skill: it beats Vela's own geometric-mean interval in 2 of 5 (median |ln| error 0.22 against 0.19). It predicts every next glitch early (5 of 5, exploratory).
   - **Why (B2).** In all five intervals t₀ grows as the fit window extends (5 of 5, p = 0.031): Vela's post-glitch recovery slows. Even full-interval fits err by a median of 0.15, close to the published fits on the same intervals (0.15–0.16).
   - *(V1, B1, B2; current research)*

## Data and methods
- **Catalogue.** Jodrell Bank glitch catalogue, snapshot 2026-11-20 (SHA-256 `e811419f…`; Basu et al. 2022 describe the catalogue). Unseen later glitches are reserved for the registered forecasts.
- **Pre-registration.** For each test, the hypotheses, statistic, decision rule, data and code were committed before any statistic was computed on real data. Deviations and post-hoc analyses are labelled in each write-up.
- **Forecast scoring (G1, G2).** At each glitch with at least 4 past waits, three models issue predictive densities for the next wait, each with parameter uncertainty included:
  - Poisson: a Lomax predictive;
  - log-normal renewal: Student-t in log space;
  - size-conditioned: a regression of log wait on log size, with a Student-t predictive.
  - Models are compared by the pulsar-averaged information gain, with a pulsar-block bootstrap.
  - After the referee, gains were also calibrated against simulated Poisson sequences with the same counts. A misspecified renewal model loses about 0.15 nats there, so zero is not the null.
- **Aftershocks (G3).** Quick follow-up: a next glitch within 0.1 of the pulsar's leave-one-out mean wait. The test asks whether such follow-ups favour large first events (within-pulsar permutation), and compares their number with a Poisson null.
- **Meta-analysis (V1).** Pairs of (t_th, t_obs) come from the latest arXiv version of every vortex-creep paper found by a registered search, one pair per glitch. Tracking is within-pulsar Spearman on values normalised by each pulsar's geometric-mean interval. Skill is a sign test against the leave-one-out geometric mean.

## Results
**T04, published forecasts.**
- **Primary per event** (14 forecasts): 2 of 6 resolved numeric forecasts within 1σ (P = 0.085 if calibrated), 5 of 6 within 2σ.
- **Overdue:** four forecasts, including Liu et al.'s J1420−6048 forecast, which had failed in the paper's own data before publication (z ≥ +4.7).
- **A failed window:** Zhu et al.'s January 2026 window for a major Crab glitch closed with none (the paper was withdrawn as a duplicate).
- **Post hoc:** Σz² = 18.9 on 6 (p = 0.004), driven by one 3.4σ miss.

**G1, predictability** (14 pulsars, 231 forecasts).

| Comparison | Gain, nats per forecast | Calibrated Poisson null |
|---|---|---|
| Renewal over Poisson | +0.098 | −0.152; P(null ≥ obs) < 0.001 |
| Same, without J1420−6048 | +0.025 | −0.147; P = 0.001 |

The renewal model's predictive coverage is 125/231 in its central 50% and 208/231 in its central 90%. Predictability rises with median glitch size: ρ = +0.39 (p = 0.087, primary) and +0.40 (p = 0.014 over 30 pulsars, sensitivity).

**G2, two classes.**

| Class | Pulsars, forecasts | Gain, renewal over Poisson | Calibrated null, P | Size–wait slopes positive |
|---|---|---|---|---|
| Large (≥ 10⁻⁷) | 7, 104 | +0.195 (+0.052 without J1420−6048) | < 0.001 (0.007) | 7 of 7 (p = 0.0078); 14 of 14 with ≥ 6 per class |
| Small | 7, 73 | −0.057 | 0.11 (consistent with Poisson) | size adds nothing (shuffle null P = 0.66) |

The reservoir sign is robust per pulsar in J0537−6910, Vela, J1413−6141 and J1740−3015.

**G3, aftershocks** (33 pulsars, 384 waits).
- There were 15 quick follow-ups against 36.4 expected, but the deficit vanishes once waits under 20–60 days are excluded: 7 against 8.2 at ≥ 60 days (P = 0.41).
- The best-monitored pulsars show none: the Crab 4 against 2.9, Vela 2 against 2.4.
- Quick follow-ups do not favour large first events: mean size percentile 0.41 (p(greater) = 0.89).
- They are not systematically smaller than the first event.

**V1, vortex-creep interglitch times** (35 pairs, 5 papers, 6 pulsars).
- **Tracking:** ρ = +0.66 (p = 1.5×10⁻⁴; 32 pairs in 4 pulsars).
- **Skill:** better than the leave-one-out mean in 25 of 34 (p = 0.0045); median |ln(t_th/t_obs)| 0.093 against 0.186.
- **With J0537−6910**, mapped post hoc: ρ = 0.70–0.71 over 66 pairs. Within J0537−6910 the model tracks but does not beat the mean (19–21 of 34).
- **Glitch size alone:** ρ = +0.46 (p = 0.005); within Vela, t_th and size correlate at 0.74.
- **Before the outcome:** only Vela 2019 is a clean case. Its error, 0.16, is worse than its own baseline's 0.11.
- **Revisions after the outcome are mixed:** J2229+6114 converged; Vela 2019 was kept by the same group; Akbal et al.'s v1 → v3 stayed 375 d late.

## Discussion
- **What is new.**
  - Out-of-sample forecast scoring of glitches, with calibrated nulls, appears not to have been done before (prior-art searches of arXiv, INSPIRE citers of the main forecast papers, OpenAlex, and Semantic Scholar where reachable).
  - G2 turns an in-sample proposal (Fuentes et al. 2019) into an out-of-sample result.
  - G3 is a first population test of an earthquake-style aftershock signature in glitches. Melatos & Warszawski (2009) proposed aftershocks as a discriminant in a size-to-size form; Carlin & Melatos (2019) found no positive size autocorrelation in the five most prolific pulsars.
  - V1 is the first pooled check of vortex-creep interglitch predictions.
- **What it means physically.**
  - The data favour one reservoir with two kinds of trigger: deterministic for large glitches, random for small ones.
  - The vortex-creep claim that a glitch comes when the post-glitch recovery completes is supported as a consistency relation in published fits. Its forecasting value is unproven, and much of its apparent skill is shared with glitch size. In at least one paper the relation is assumed rather than tested (Gügercinoğlu et al. 2025, for J0537−6910).
- **Limitations.**
  - Catalogue incompleteness and monitoring gaps (J0537−6910's 2011–2017 gap counts as a wait).
  - Small numbers of pulsars per class.
  - A single size threshold.
  - Pulsar-block bootstraps over 7–14 pulsars.
  - In V1, the fits use data spanning the interval, and model components are chosen with the outcome known.

## Decisive next tests
1. **Blind vortex-creep fits.** *Done for the simplest model form, on Vela (B1, `../results/B1-blind-vela-recovery.md`): not supported, with a systematic early bias. Still open: a blind fit of the full multi-component model.*
   - **The test:** fit only the first part of each post-glitch recovery (for example, half the interval) and forecast the rest. Score against the pulsar's own baseline.
   - **What it needs:** Fermi-LAT photons and spacecraft files, plus photon timing (PINT). The 3PC timing models are public, but they carry one global ν̈ and timing-noise terms, so they cannot substitute for the per-interval fits.
   - **The alternative:** the modelling groups could run their own fits truncated at a fixed time, blind to the next glitch.
2. **Registered forecasts.** Next-glitch forecasts for 34 pulsars (G1) and next-large-glitch forecasts for 7 (G2-P) are registered.
   - A head-to-head for Vela resolves by **2027-04-11**. The probability of a large glitch after 2026-11-20 and by then: Grover et al. 0.71, Vela's own past waits 0.31, our renewal models 0.13.
   - `analysis/score_registered.py run` scores everything against the live catalogue. As of 2026-11-27 no new glitch has been catalogued.
3. **A merged catalogue.** A de-duplicated Jodrell Bank and ATNF compilation would allow a refractory test on large follow-ups only, which recovery masking cannot affect.

## Reproducibility
Write-ups in `../results/`:
- T04: `T04-glitch-forecast-scorecard.md`, registered `5b6f6a8`, revised `bc81173` and `7d39a96`.
- G1: `G1-glitch-predictability.md`, registered `a95b9cb`.
- G2: `G2-two-glitch-populations.md`, registered `6c3a9be`.
- G3: `G3-glitch-aftershocks.md`, registered `0f14460`.
- Post-hoc nulls: `G-nulls-posthoc.json`.
- V1: `V1-vortex-creep-interglitch.md`, registered `71011da`, extraction `5c3540f`, revised `25c2431`.
- Forecast registration: `../prereg/G2P-large-glitch-forecasts.md`, `df1f37a`.

The code is in `../analysis/` and uses only the standard library and numpy.

## References
- Akbal et al. (2017). "Nonlinear interglitch dynamics, the braking index of the Vela pulsar and the time to the next glitch". *MNRAS* 469, 4183. [arXiv:1612.03805](https://arxiv.org/abs/1612.03805)
- Basu et al. (2022). "The Jodrell Bank Glitch Catalogue: 106 new rotational glitches in 70 pulsars". *MNRAS* 510, 4049. [arXiv:2111.06835](https://arxiv.org/abs/2111.06835)
- Carlin & Melatos (2019). "Autocorrelations in pulsar glitch waiting times and sizes". *MNRAS* 488, 4890. [arXiv:1907.09143](https://arxiv.org/abs/1907.09143)
- Fuentes, Espinoza & Reisenegger (2019). "Glitch time series and size distributions in eight prolific pulsars". *A&A* 630, A115. [arXiv:1907.09887](https://arxiv.org/abs/1907.09887)
- Grover et al. (2026). "Post-glitch Recovery and the Neutron Star Structure: The Vela Pulsar". *PASA*. [arXiv:2506.02100](https://arxiv.org/abs/2506.02100)
- Gügercinoğlu & Alpar (2020). "The 2016 Vela glitch: a key to neutron star internal structure and dynamics". *MNRAS* 496, 2506. [arXiv:2003.08724](https://arxiv.org/abs/2003.08724)
- Gügercinoğlu et al. (2022). "Glitches in four gamma-ray pulsars and inferences on the neutron star structure". *MNRAS* 511, 425. [arXiv:2011.14788](https://arxiv.org/abs/2011.14788)
- Gügercinoğlu et al. (2025). "Braking index of the frequently glitching PSR J0537-6910". *A&A* 706, A216. [arXiv:2506.22936](https://arxiv.org/abs/2506.22936)
- Liu et al. (2024). "A multi-band study of pulsar glitches with Fermi-LAT and Parkes". *arXiv preprint*. [arXiv:2408.15022](https://arxiv.org/abs/2408.15022)
- Melatos & Drummond (2019). "Pulsar glitch activity as a state-dependent Poisson process: parameter estimation and epoch prediction". *ApJ* 885, 37. [arXiv:1910.05503](https://arxiv.org/abs/1910.05503)
- Melatos & Warszawski (2009). "Superfluid vortex unpinning as a coherent noise process, and the scale invariance of pulsar glitches". *ApJ* 700, 1524. [arXiv:0904.2998](https://arxiv.org/abs/0904.2998)
- Middleditch et al. (2006). "Predicting the Starquakes in PSR J0537-6910". *ApJ* 652, 1531. [arXiv:astro-ph/0605007](https://arxiv.org/abs/astro-ph/0605007)
- Zhu et al. (2026). "Exploring Superfluid Angular Momentum Reservoir Effect on Pulsar Glitches and Forecasting Next Glitches of the Crab Pulsar". *arXiv preprint*, withdrawn 2026-06-18 as a duplicate of arXiv:2506.02925. [arXiv:2601.12130](https://arxiv.org/abs/2601.12130)
