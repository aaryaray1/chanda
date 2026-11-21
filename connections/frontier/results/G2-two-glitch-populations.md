# G2 results · Are large glitches predictable and small glitches Poisson?

**Tier T** (out-of-sample forecast competition by size class). **Status:** run as registered; refereed on 2026-11-21 ("needs revision"), and revised here.
- **Pre-registration:** `../prereg/G2-two-glitch-populations.md`, commit `6c3a9be`.
- **Code:** `../analysis/g2_two_populations.py`. **Numbers:** `G2-results.json`, plus the sensitivity files `G2-results-thr500-min8.json` and `G2-results-thr100-min6.json`.
- **Post-hoc nulls:** `../analysis/g_nulls.py`, with results in `G-nulls-posthoc.json`.
- **Data:** the 2026-11-20 Jodrell Bank snapshot. Large: Δν/ν ≥ 10⁻⁷, 7 pulsars, 104 forecasts. Small: 7 pulsars, 73 forecasts.

## Answer
**Registered verdicts.** Gains are pulsar-averaged, in nats per forecast, with 90% bootstrap intervals.

| Hypothesis | Result | Verdict |
|---|---|---|
| **H5**, large glitches predictable: renewal over Poisson, large class | +0.195 (−0.054 to +0.471) | not supported (bound includes 0) |
| **H6**, small glitches Poisson-like: renewal over Poisson, small class | −0.057 (−0.148 to +0.031) | supported (upper bound below +0.10) |
| **H7**, contrast, large minus small | +0.251 (−0.015 to +0.544) | not supported, by a hair |
| **H8a**, reservoir sign among large glitches: slope of log wait on log size | positive in 7 of 7 pulsars, sign test p = 0.0078 | supported |
| **H8b**, size improves large-glitch forecasts | +0.035 (−0.135 to +0.199) | inconclusive |

**Zero was the wrong baseline (post hoc, after the referee).** On simulated Poisson sequences with the same counts, the renewal model *loses* to the Poisson model by about 0.16 nats, because it is misspecified for exponential waits. So H5 and H6 tested against the wrong reference. Against the calibrated Poisson null:

| Class | Observed | Poisson-null mean (5–95%) | P(null ≥ observed) |
|---|---|---|---|
| Large | +0.195 | −0.158 (−0.301 to −0.036) | < 0.001 |
| Large, without J1420−6048 | +0.052 | −0.150 (−0.292 to −0.018) | 0.007 |
| Small | −0.057 | −0.159 (−0.314 to −0.019) | 0.11 |

**Reading:**
- **Large glitches** depart clearly from Poisson in their timing, even without J1420−6048. That pulsar, with only 3 forecasts, carries much of the large-class average.
- **Small glitches** are consistent with Poisson.
- **Size adds nothing for small glitches.** The −0.119 cost of conditioning on size is what an uninformative covariate costs: shuffling sizes within each pulsar gives −0.098, with P = 0.66.
- **Untested:** cross-class information, such as time since the last large glitch.
- **Incompleteness:** missed small glitches push the small class toward Poisson, as the registration noted. In Vela, at least, the shortage of small glitches is real rather than a detection effect (Espinoza et al. 2021).

**The reservoir sign among large glitches** (H8a) is positive in all 7 pulsars, and in 14 of 14 with at least 6 per class (p = 6×10⁻⁵). Recovery does not hide large glitches, so detection masking cannot produce this sign. But per pulsar it is robust in J0537−6910, Vela, J1413−6141 and J1740−3015 only:
- J1341−6220's slope is small (+0.095) and flips to −1.0 at the 5×10⁻⁷ threshold.
- J1420−6048 and J2229+6114 flip if one wait is removed.

J0537−6910's wait-scales-with-size law is long known (Middleditch et al. 2006).

**Relation to prior work.** Fuentes, Espinoza & Reisenegger (2019) proposed the same two-trigger picture in-sample, from eight prolific pulsars: deterministic large glitches, random small ones, one reservoir. G2 is an out-of-sample check of it at one fixed threshold, with the calibrated null. It agrees on the two classes. It differs in detail: Fuentes et al. found the size→next-wait correlation positive in 7 of 8 pulsars, all but the Crab.

## Per pulsar
Gain of renewal over Poisson:
- **Large class:** J1420−6048 +1.05 (3 forecasts), J0537−6910 +0.38, J2229+6114 +0.31, J1740−3015 +0.13, J1413−6141 −0.06, J1341−6220 −0.09, Vela −0.36.
- **Small class:** J1341−6220 +0.18, J1740−3015 +0.01, Crab −0.02, J0631+1036 −0.03, J0742−2822 −0.07, J1801−2304 −0.13, J0537−6910 −0.33.

## Why Vela loses (post-hoc diagnostic)
Vela's large glitches are quasi-periodic, and the renewal model wins 11 of its 16 forecasts. Two short waits outweigh those wins:
- **The 1994 double glitch:** 835×10⁻⁹, then 199×10⁻⁹ 32 days later, costing −5.6 nats.
- **1981 to 1982:** a 304-day wait, costing −2.7 nats.

Without the doublet, Vela's large-class gain is close to zero.

## Sensitivity runs (declared)
| Statistic | Primary (10⁻⁷, ≥ 8 per class) | Threshold 5×10⁻⁷ | At least 6 per class |
|---|---|---|---|
| Pulsars, large / small | 7 / 7 | 3 / 8 | 14 / 11 |
| Small: renewal over Poisson, 90% interval | −0.148 to +0.031 | −0.026 to +0.098 | −0.130 to +0.078 |
| Small: size over renewal, 90% interval | −0.214 to −0.054 | −0.247 to −0.013 | −0.156 to −0.029 |
| Large: renewal over Poisson | +0.195 (−0.054 to +0.471) | +0.462 (+0.057 to +0.867)* | +0.093 (−0.271 to +0.415) |
| Large: positive slopes | 7 of 7 (p = 0.0078) | 2 of 3 | 14 of 14 (p = 6×10⁻⁵) |
| Contrast, large minus small, lower bound | −0.015 | −0.024 | −0.262 |

\* That bootstrap is over only 3 pulsars, so it has just 10 distinct resamples. Treat it as indicative only.

## Deviations
None from the registered analysis. The calibrated nulls, the shuffle null and the Vela diagnostic are post hoc.

## Sources
- Fuentes, Espinoza & Reisenegger (2019). "Glitch time series and size distributions in eight prolific pulsars". *A&A* 630, A115. [arXiv:1907.09887](https://arxiv.org/abs/1907.09887)
- Middleditch et al. (2006). "Predicting the Starquakes in PSR J0537-6910". *ApJ* 652, 1531. [arXiv:astro-ph/0605007](https://arxiv.org/abs/astro-ph/0605007)
- Espinoza et al. (2021). "Small glitches and other rotational irregularities of the Vela pulsar". *A&A* 647, A25. [arXiv:2007.02921](https://arxiv.org/abs/2007.02921)
