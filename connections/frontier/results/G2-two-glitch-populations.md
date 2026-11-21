# G2 results · Are large glitches predictable and small glitches Poisson?

**Tier T** (out-of-sample forecast competition by size class). **Status:** run as registered. Not yet refereed.
- **Pre-registration:** `../prereg/G2-two-glitch-populations.md`, commit `6c3a9be`.
- **Code:** `../analysis/g2_two_populations.py`. **Numbers:** `G2-results.json`, plus the sensitivity files `G2-results-thr500-min8.json` and `G2-results-thr100-min6.json`.
- **Data:** the 2026-11-20 Jodrell Bank snapshot. Large: Δν/ν ≥ 10⁻⁷, 7 pulsars, 104 forecasts. Small: 7 pulsars, 73 forecasts.

## Answer
Gains are in nats per forecast, pulsar-averaged, with 90% bootstrap intervals.

| Hypothesis | Result | Verdict |
|---|---|---|
| **H6**, small glitches Poisson-like: gain of renewal over Poisson, small class | −0.057 (−0.148 to +0.031); upper bound below the registered +0.10 | **supported** |
| **H8a**, reservoir sign among large glitches: slope of log wait on log size | positive in **7 of 7** pulsars, sign test p = 0.0078 | **supported** |
| **H5**, large glitches predictable: gain of renewal over Poisson, large class | +0.195 (−0.054 to +0.471) | not supported |
| **H7**, contrast, large minus small | +0.251 (−0.015 to +0.544) | not supported, by a hair |
| **H8b**, size improves large-glitch forecasts | +0.035 (−0.135 to +0.199) | inconclusive |

The result most worth noting:
- **Small glitches carry no forecast information,** either in their timing or in their size. For small glitches, conditioning on size makes forecasts *worse*: −0.119 (−0.214 to −0.054).
- **Large glitches show the reservoir sign in every pulsar.** A bigger large glitch is followed by a longer wait to the next large one. Post-glitch recovery cannot hide a large glitch, so this sign is not the detection artifact that could explain G1's slopes.

**Both classes are calibrated:**

| Class | KS p | Central 50% | Central 90% |
|---|---|---|---|
| Large | 0.70 | 49 of 104 | 96 of 104 |
| Small | 0.63 | 42 of 73 | 65 of 73 |

**Per pulsar,** the gain of renewal over Poisson:
- **Large class:** J1420−6048 +1.05, J0537−6910 +0.38, J2229+6114 +0.31, J1740−3015 +0.13, J1413−6141 −0.06, J1341−6220 −0.09, Vela −0.36.
- **Small class:** J1341−6220 +0.18, J1740−3015 +0.01, Crab −0.02, J0631+1036 −0.03, J0742−2822 −0.07, J1801−2304 −0.13, J0537−6910 −0.33.
- **Within the three pulsars in both classes,** large minus small: J0537−6910 +0.71, J1740−3015 +0.12, J1341−6220 −0.28.

## Why Vela loses (post-hoc diagnostic)
Vela's large glitches are quasi-periodic, and the renewal model wins 11 of its 16 forecasts. Two short waits outweigh those wins:
- **The 1994 double glitch:** a 199×10⁻⁹ glitch 32 days after an 835×10⁻⁹ one, costing −5.6 nats.
- **1981 to 1982:** a 304-day wait, costing −2.7 nats.

Without the 1994 doublet, Vela's large-class gain is close to zero rather than −0.36. A renewal model cannot produce a quick follow-up after a large event; an earthquake-style aftershock process can. That motivates G3, which tests for aftershocks across the population and is registered separately before any of its statistics were computed.

## Sensitivity runs (declared)
| Statistic | Primary (10⁻⁷, ≥ 8 per class) | Threshold 5×10⁻⁷ | At least 6 per class |
|---|---|---|---|
| Pulsars, large / small | 7 / 7 | 3 / 8 | 14 / 11 |
| Small: renewal over Poisson, 90% interval | −0.148 to +0.031 | −0.026 to +0.098 | −0.130 to +0.078 |
| Small: size over renewal, 90% interval | −0.214 to −0.054 | −0.247 to −0.013 | −0.156 to −0.029 |
| Large: renewal over Poisson | +0.195 (−0.054 to +0.471) | **+0.462 (+0.057 to +0.867)** | +0.093 (−0.271 to +0.415) |
| Large: positive slopes | 7 of 7 (p = 0.0078) | 2 of 3 | **14 of 14 (p = 6×10⁻⁵)** |
| Contrast, large minus small, lower bound | −0.015 | −0.024 | −0.262 |

Robust across all three runs:
- **Small glitches:** their timing is Poisson-like, and their sizes make forecasts worse.
- **Large glitches:** they carry the reservoir sign.
- **Predictability of large-glitch timing:** clears zero only for the largest glitches (5×10⁻⁷: Vela, J1341−6220, J1420−6048).

## Deviations
None. The Vela diagnostic is post hoc and changes no registered number.
