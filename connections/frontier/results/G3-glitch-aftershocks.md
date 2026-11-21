# G3 results · Do pulsar glitches have aftershocks?

**Tier T** (pre-registered test on a public catalogue). **Status:** run as registered. Not yet refereed; prior art for the comparison with earthquakes and FRBs is still to be checked.
- **Pre-registration:** `../prereg/G3-glitch-aftershocks.md`, commit `0f14460`.
- **Code:** `../analysis/g3_aftershocks.py`. **Numbers:** `G3-results.json`.
- **Data:** the 2026-11-20 Jodrell Bank snapshot: 33 pulsars with at least 5 sized glitches, 384 waits.

## Answer
**No.** Glitches show none of the three signatures of aftershocks:

| Test | Result | Verdict |
|---|---|---|
| **H10**, quick follow-ups (within 0.1 of the typical wait) against a Poisson process | **15 observed, 36.4 expected**; p(deficit) < 0.0002 (0 of 5000 simulations) | **a strong deficit**, the opposite of clustering |
| **H9**, do quick follow-ups come after *large* glitches? | mean size percentile 0.41 (15 pairs); p(greater) = 0.89 | **not supported** |
| **H11**, are follow-ups smaller, as in Båth's law? | median log₁₀ ratio, follow-up over first event: +0.29 | **no**: follow-ups are as large or larger |

The deficit holds in every declared sensitivity run:

| Run | Quick follow-ups | Poisson expectation | Mean size percentile before them |
|---|---|---|---|
| Primary, u < 0.1 | 15 | 36.4 | 0.41 (p(less) = 0.11) |
| u < 0.05 | 5 | 18.7 | 0.36 |
| u < 0.2 | 39 | 68.8 | **0.36 (p(less) = 0.0015)** |
| At least 8 glitches | 11 | 27.1 | 0.49 |
| Without J0537−6910 | 15 | 30.1 | 0.41 |
| Without Vela | 13 | 34.1 | 0.43 |

With the wider window, quick follow-ups come preferentially after *small* glitches. That is the direction both the reservoir and recovery masking predict, and the opposite of triggering.

**The 15 quick pairs** are spread thinly: Crab 4, J1740−3015 3, Vela 2, J0729−1448 2, and one each in J0631+1036, J1048−5832, J1617−5055 and J1826−1334. J0537−6910 has none. Vela's 1994 double glitch, which motivated G3, is one of only two pairs in which a glitch above 10⁻⁷ is quickly followed by a smaller one.

## Reading
- **What it shows.** Pulsar glitches have a refractory period: after a glitch, the next one is 2.4 times less likely to come quickly than a memoryless process allows. They do not have the triggered, size-dependent, smaller-follow-up behaviour of earthquake aftershocks.
- **The cross-branch point.** Earthquakes show aftershocks. So, reportedly, do bursts from repeating FRB sources (to be checked in F3). Those are crust or magnetosphere failures. Glitches, which do not show them, are not failures of that kind. That fits the standard picture of glitches as superfluid vortex unpinning, which refills a reservoir. It contradicts the starquake trigger sometimes proposed for small Crab glitches, at least in its simplest form.
- **What it cannot tell apart.** Part of the deficit may be observational: post-glitch recovery can hide a small follow-up for weeks. G2 points to a physical part: among large glitches alone, which recovery does not hide, the reservoir sign held in 7 of 7 pulsars. A clean refractory test on large follow-ups only is the natural next step. It needs more large-glitch pairs than this catalogue has.

## Deviations
- **Pulsar count.** The registration said 34 pulsars. The registered rule, at least 5 glitches with a known positive size, gives 33. G1's 34 counted glitches without sizes. Nothing else changes.
- **H11 coincidence.** Its value, 0.289, is the same in three runs. That is not a bug: the windows are nested, and the same pair sits at the median of each.
