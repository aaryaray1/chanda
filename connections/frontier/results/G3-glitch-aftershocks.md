# G3 results · Do pulsar glitches have aftershocks?

**Tier T** (pre-registered test on a public catalogue). **Status:** run as registered; refereed on 2026-11-21 ("needs revision"), and revised here. The first version's headline ("a refractory deficit instead") is withdrawn: the deficit is the catalogue's time resolution.
- **Pre-registration:** `../prereg/G3-glitch-aftershocks.md`, commit `0f14460`.
- **Code:** `../analysis/g3_aftershocks.py`. **Numbers:** `G3-results.json`.
- **Post-hoc analyses**, added after the referee: `../analysis/g_nulls.py`, with results in `G-nulls-posthoc.json`.
- **Data:** the 2026-11-20 Jodrell Bank snapshot: 33 pulsars with at least 5 sized glitches, 384 waits.

## Answer
**No resolvable aftershocks.** On scales from about a month up to a tenth of each pulsar's typical wait, the catalogue resolves no aftershock signal:
- Quick follow-ups come at the Poisson rate.
- They do not come preferentially after large glitches.

Below about a month, the catalogue cannot see aftershocks either way.

| Test | Result | Verdict |
|---|---|---|
| **H9**, quick follow-ups (within 0.1 of the typical wait) come after *large* glitches | mean size percentile 0.41 over 15 pairs; p(greater) = 0.89 | **not supported**. With a 0.2 window: 0.36, p(less) = 0.0015 |
| **H10**, number of quick follow-ups against a Poisson process | 15 observed, 36.4 expected | registered reading: a deficit (p < 0.0002), but see below |
| **H11**, follow-ups smaller than the first event | median log₁₀ ratio +0.29 (−0.40 with at least 8 glitches) | **uninformative** (see Reading) |

**The deficit is resolution, not physics (post hoc).** Here are quick follow-ups counted only among waits of at least D days, against the same Poisson null:

| D (days) | Observed | Poisson | P(≤ observed) |
|---|---|---|---|
| 0 | 15 | 36.4 | < 0.001 |
| 14 | 14 | 23.7 | 0.018 |
| 20 | 14 | 20.3 | 0.08 |
| 30 | 11 | 16.1 | 0.11 |
| 45 | 8 | 11.3 | 0.19 |
| 60 | 7 | 8.2 | 0.41 |

The whole deficit lies at waits under 1–2 months. That is the scale of observing cadence, of how closely two glitches can be fitted apart, and of post-glitch recovery.

The best-monitored pulsars show no deficit:

| Pulsar | Quick follow-ups | Poisson | Quick window |
|---|---|---|---|
| Crab | 4 | 2.9 | 66 d |
| Vela | 2 | 2.4 | 81 d |
| J1740−3015 | 3 | 3.6 | 38 d |
| J0537−6910 | 0 | 6.3 | **14 d**, close to its observing cadence; its quasi-periodicity is also long known (Middleditch et al. 2006) |

## Reading
- **What it shows.** Where the catalogue resolves them, quick follow-ups after glitches occur at the Poisson rate. They show no excess after large glitches. Earthquake-like aftershocks would show both: an excess, and a dependence on the first event's size.
- **What it cannot show.**
  - Aftershocks shorter than about a month. Seismic aftershocks follow Omori's law and mostly arrive within days of the mainshock.
  - The repeating-FRB aftershocks found by Totani & Tsuzuki (2023), and in the radio pulses of SGR 1935+2154 (Tsuzuki et al. 2024), act on sub-second to hour scales. These timing catalogues cannot reach them.
  - So the statement is "no aftershocks at the catalogue's resolution", not "glitches are not failures".
- **What it does not discriminate.** A simple starquake (strain builds, then releases) also predicts a quiet interval after each event. So the first version's sentences about superfluid unpinning versus starquakes are withdrawn.
- **The aftershocks proposed for glitch models are a different test.** Melatos & Warszawski (2009) proposed aftershocks to tell coherent noise from vortex avalanches: under coherent noise, an excess of *large* glitches follows a large glitch. That is a size-to-size prediction. Carlin & Melatos (2019) found no positive autocorrelation of consecutive sizes in the five most prolific pulsars; the Crab's is negative, ρ = −0.46. G3 tests the timing signature instead, and finds nothing at the catalogue's resolution. Carlin & Melatos (2021) predict aftershocks after the largest glitches with *longer* waits, which a short window cannot see.
- **Why H11 is uninformative.** Båth's law concerns the largest aftershock of a *large* mainshock. Here the first events are biased small (mean percentile 0.41), and masking favours detecting large follow-ups. The median ratio also changes sign between runs.

**The quick pairs.** There are 15: Crab 4, J1740−3015 3, Vela 2, J0729−1448 2, and one each in J0631+1036, J1048−5832, J1617−5055 and J1826−1334. In three of them a glitch above 10⁻⁷ is followed quickly by a smaller one: Vela 835→199 (1994, 32 d), Vela 1260→0.2 (2021, 62 d) and J1740−3015 659→48 (26 d).

## Deviations
- **Pulsar count.** The registration said 34 pulsars; the registered rule gives 33, because G1's 34 counted glitches without sizes.
- **Unsized glitches.** The registration pairs each glitch with the next one "of any size", but the code drops glitches without a size. Those include J1341−6220's two at MJD 58178 and 58214, 36 days apart. Keeping them leaves the quick count at 15, against 36.6 expected.
- **H11 coincidence.** Its value, 0.289, is the same in four runs, because the windows are nested. In the run with at least 8 glitches it is −0.40.
- **Post-hoc analyses:** the dead-time table and the per-pulsar counts. Neither is registered.

## Sources
- Melatos & Warszawski (2009). "Superfluid vortex unpinning as a coherent noise process, and the scale invariance of pulsar glitches". *ApJ* 700, 1524. [arXiv:0904.2998](https://arxiv.org/abs/0904.2998)
- Carlin & Melatos (2019). "Autocorrelations in pulsar glitch waiting times and sizes". *MNRAS* 488, 4890. [arXiv:1907.09143](https://arxiv.org/abs/1907.09143)
- Carlin & Melatos (2021). "Long-term statistics of pulsar glitches due to history-dependent avalanches". *ApJ* 917, 1. [arXiv:2105.13588](https://arxiv.org/abs/2105.13588)
- Carlin, Melatos & Vukcevic (2019). "Temporal clustering of rotational glitches in the Crab pulsar". *MNRAS* 482, 3736. [arXiv:1810.12458](https://arxiv.org/abs/1810.12458)
- Middleditch et al. (2006). "Predicting the starquakes in PSR J0537-6910". *ApJ* 652, 1531. [arXiv:astro-ph/0605007](https://arxiv.org/abs/astro-ph/0605007)
- Totani & Tsuzuki (2023). "Fast radio bursts trigger aftershocks resembling earthquakes, but not solar flares". *MNRAS* 526, 2795. [arXiv:2306.13612](https://arxiv.org/abs/2306.13612)
- Tsuzuki et al. (2024). "Similarity to earthquakes again: periodic radio pulses of the magnetar SGR 1935+2154 are accompanied by aftershocks like fast radio bursts". *MNRAS*. [arXiv:2401.16758](https://arxiv.org/abs/2401.16758) · [doi:10.1093/mnras/stae965](https://doi.org/10.1093/mnras/stae965)
