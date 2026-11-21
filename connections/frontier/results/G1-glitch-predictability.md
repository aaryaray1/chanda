# G1 results · How predictable are pulsar glitches?

**Tier T** (out-of-sample forecast competition on a public catalogue). **Status:** run as registered; refereed on 2026-11-21 ("minor revision"), and revised here. Prior art: the method appears new (F3), the result partly known.
- **Post-hoc nulls:** `../analysis/g_nulls.py`, with results in `G-nulls-posthoc.json`.
- **Pre-registration:** `../prereg/G1-glitch-predictability.md`, commit `a95b9cb`.
- **Code:** `../analysis/g1_glitch_forecasts.py`. **Numbers:** `G1-results.json` (primary) and `G1-results-min6.json` (declared sensitivity run).
- **Data:** the 2026-11-20 Jodrell Bank snapshot (SHA-256 `e811419f…`): 14 pulsars with at least 8 glitches, 231 forecasts.

## Answer
A two-parameter log-normal renewal forecast is **calibrated out of sample**. Its predictive intervals cover what they claim:

| Interval | Coverage | Nominal |
|---|---|---|
| Central 50% | 125 of 231 (54%) | 50% (p = 0.24) |
| Central 90% | 208 of 231 (90%) | 90% (p = 1.0) |
| KS test of the PIT | p = 0.55 | uniform |

T04's published forecasts landed within their 1σ 2 times in 6, but six forecasts are too few to judge calibration. M1's 231 are enough to establish it.

**Registered verdicts,** in nats per forecast:

| Comparison | Pulsar-averaged gain | 90% bootstrap interval | Verdict |
|---|---|---|---|
| H1: renewal over Poisson | +0.098 | −0.012 to +0.240 | not supported (bound includes 0) |
| H2: size-conditioned over renewal | −0.053 | −0.217 to +0.099 | inconclusive |

**Zero was the wrong baseline (post hoc, after the referee).** On simulated Poisson sequences with the same counts, the renewal model *loses* to the Poisson model: the null mean is −0.152 (5–95%: −0.253 to −0.067). The observed +0.098 exceeds all 1000 null draws.
- **Without J1420−6048:** +0.025 against −0.147, P = 0.001. That pulsar contributes 0.075 of the 0.098 with only 3 forecasts, and the median pulsar's gain is +0.010.
- **So glitch timing departs significantly from Poisson.** What is small is how much better this renewal forecast does than a Poisson forecast.
- **Where the gain sits:** J1420−6048, J0537−6910, J1413−6141, J1341−6220 and J2229+6114. Without J0537−6910 the pooled gain is +0.023.

**Does predictability rise with glitch size? (H3, not supported at the registered threshold.)** The Spearman correlation between a pulsar's gain and its median glitch size:
- primary, 14 pulsars: ρ = +0.39, one-sided p = 0.087, so not supported at the registered threshold;
- declared sensitivity, 30 pulsars with at least 6 glitches: ρ = +0.40, p = 0.014.

**The sign of the size–wait relation is reservoir-like almost everywhere, but it barely helps forecasting.**
- The slope of log wait on log size is positive in 13 of 14 pulsars (sign test p = 0.0009) and in 26 of 30 in the sensitivity run (p = 3×10⁻⁵).
- No pulsar has a significant negative slope, the sign triggering would give. Vela's is negative but small (−0.03).
- Fuentes, Espinoza & Reisenegger (2019) found the in-sample correlation positive in 7 of 8 prolific pulsars, all but the Crab. Here the Crab is positive (+0.13) and Vela negative.
- Out of sample, size information pays off only in J0537−6910, J1413−6141, J1048−5832 and J1341−6220.
- Caveat: the slopes are in-sample, and post-glitch recovery hides small glitches after large ones, which also makes the slope positive. G2 separates the two explanations.

**Reading.** Glitch timing is significantly non-Poisson across the population, but a simple renewal forecast gains only about 0.1 nats per forecast over a Poisson one. Honest forecasting is easy: the renewal model is calibrated. Large gains are not, which matches Melatos & Drummond's (2019) in-sample finding that a state-dependent model beats Poisson only modestly. G2 finds where the structure sits: in large glitches.

## Per pulsar
CV is the coefficient of variation of waiting times: below 1 is quasi-periodic, above 1 is clustered. Gains are in nats per forecast.

| Pulsar | Glitches | Forecasts | CV | Median log₁₀(Δν/ν×10⁹) | Gain, renewal over Poisson | Gain, size over renewal | Slope, log wait on log size |
|---|---|---|---|---|---|---|---|
| J0537−6910 | 68 | 63 | 1.90* | +2.40 | +0.255 | +0.305 | +0.415 |
| J1740−3015 | 38 | 33 | 1.08 | +1.27 | −0.003 | −0.004 | +0.156 |
| J1341−6220 | 35 | 30 | 0.56 | +2.29 | +0.140 | +0.125 | +0.169 |
| J0534+2200 (Crab) | 32 | 27 | 1.31 | +0.73 | +0.017 | −0.092 | +0.126 |
| J0835−4510 (Vela) | 26 | 21 | 0.58 | +3.29 | −0.198 | −0.060 | −0.032 |
| J0631+1036 | 17 | 12 | 1.27 | +0.88 | −0.101 | +0.035 | +0.192 |
| J1801−2304 | 15 | 10 | 0.64 | +1.91 | −0.029 | −0.015 | +0.245 |
| J1413−6141 | 14 | 9 | 0.78 | +2.49 | +0.195 | +0.526 | +0.372 |
| J1048−5832 | 12 | 7 | 0.86 | +2.17 | −0.052 | +0.382 | +0.295 |
| J2229+6114 | 10 | 5 | 0.58 | +2.72 | +0.121 | −0.045 | +0.211 |
| J0205+6449 | 9 | 4 | 0.81 | +2.72 | +0.004 | −0.946 | +0.317 |
| J0742−2822 | 9 | 4 | 0.78 | +0.26 | −0.111 | −0.326 | +0.173 |
| J1420−6048 | 8 | 3 | 0.20 | +3.12 | +1.052 | −0.080 | +0.039 |
| J1841−0524 | 8 | 3 | 0.58 | +2.11 | +0.083 | −0.553 | +0.251 |

\* J0537−6910's longest "wait", 2264 d (MJD 55819–58083), is the gap between the RXTE and NICER missions, not a quiet spell. Without it the CV is 0.53, its known quasi-periodic value. The registered analysis keeps the gap, as it keeps every catalogue gap. This penalises every model at that forecast and widens M1 for later ones.

**Vela.** Vela has a low CV (0.58), yet the renewal model loses to Poisson there. The likely reason is that the any-size target mixes Vela's quasi-periodic large glitches with occasional small ones, such as the 0.4×10⁻⁹ glitch of 2014. Those make short waits that a renewal fit to the large-glitch rhythm calls very unlikely. G2's large-only target tests this.

## Prospective forecasts (registered, to be tested)
The run issued next-glitch forecasts for all 34 pulsars with at least 5 glitches (`prospective_forecasts` in `G1-results.json`). They use M1 for 25 pulsars, M0 for 5 and M3 for 4. Examples, as the conditional median and 5–95% range in MJD:
- **Crab:** 61905, range 61397–66263.
- **Vela:** 61957, range 61407–64048.
- **J1740−3015:** 61636, range 61384–62576.
- **J2229+6114:** 61885, range 61430–63492.

**Evaluation, as amended before any evaluation data exist.** Several pulsars almost certainly glitched between their last catalogued glitch and the snapshot, so a forecast conditional on "no glitch since" is mis-specified for them. The rule:
- **Pulsars with P(glitch before the snapshot) > 0.95** under their forecast: J0205+6449, J0537−6910, J0631+1036, J1023−5746, J1341−6220, J1413−6141, J1420−6048, J1708−4008, J1801−2451, J1814−1744, J1841−0524, J1952+3252 and J2301+5852 (13 pulsars).
  - **Primary evaluation:** the *unconditional* forecast, scored against the first glitch after the last catalogued one, as a fresh catalogue shows it, whatever its date.
- **All other pulsars:** the registered *conditional* evaluation stays primary.
- **Test, for both:** KS uniformity of the PIT and coverage of the central 50% and 90% intervals, each judged at p > 0.05, once 15 pulsars have resolved or on 2028-11-20.
- **Caveat:** the missing glitches may already be published, so for the 13 the test is blind but partly retrospective.

## Deviations
- **The evaluation amendment above.** It was added after the run but before any evaluation data exist.
- **Post hoc:** the Poisson-null calibration, the J1420−6048 influence check, the J0537−6910 gap and the Vela reading. None changes a registered number.

## Limitations
- **Monitoring gaps** count as waits, as J0537−6910 shows. The catalogue carries no monitoring spans.
- **Bootstrap intervals** over 14 pulsars are coarse. Pooled statistics are dominated by J0537−6910 (63 of 231 forecasts).
- **The slope's sign** is in-sample and open to a detection-selection effect.

## Sources
- Fuentes, Espinoza & Reisenegger (2019). "Glitch time series and size distributions in eight prolific pulsars". *A&A* 630, A115. [arXiv:1907.09887](https://arxiv.org/abs/1907.09887)
- Melatos & Drummond (2019). "Pulsar glitch activity as a state-dependent Poisson process: parameter estimation and epoch prediction". *ApJ* 885, 37. [arXiv:1910.05503](https://arxiv.org/abs/1910.05503)
- Middleditch et al. (2006). "Predicting the Starquakes in PSR J0537-6910". *ApJ* 652, 1531. [arXiv:astro-ph/0605007](https://arxiv.org/abs/astro-ph/0605007)
