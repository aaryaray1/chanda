# Pre-registration G3 · Do pulsar glitches have aftershocks?

**Registered:** 2026-11-21, with `../analysis/g3_aftershocks.py`. It passed its self-test on synthetic data only (mean percentile 0.47 with no dependence, 0.76 with triggering).

## Why
G1 and G2 found the reservoir sign on average: a larger glitch is followed by a longer wait, in 13 of 14 pulsars for any size and in 7 of 7 for large glitches. But G2's post-hoc look at Vela found its forecasts ruined by quick follow-ups. The 1994 double glitch is one: a 199×10⁻⁹ glitch 32 days after an 835×10⁻⁹ one.

In seismology, quick follow-ups after large events are aftershocks. Their number grows with the size of the first event (the productivity law of the epidemic-type aftershock models). If glitches have aftershocks, the glitch process combines two mechanisms:
- a reservoir, which sets the long waits;
- a triggered component, which makes quick follow-ups after large glitches.

**Why the test can be decisive in one direction:**
- Post-glitch recovery hides small glitches after large ones. That removes quick follow-ups after *large* glitches.
- The reservoir picture also predicts long waits after large glitches.

Both effects push the statistic *against* triggering. So a significant excess of quick follow-ups after *large* glitches cannot be produced by detection or by the reservoir. A null or opposite result cannot tell reservoir from masking.

## Data and definitions (fixed)
- **Data:** the 2026-11-20 Jodrell Bank snapshot (SHA-256 `e811419f…`). Pulsars with at least 5 glitches with a known positive size: 34 pulsars.
- **Pairs:** each glitch except a pulsar's last is a "first event". It is paired with the wait w to the pulsar's next glitch, of any size.
- **Normalised wait:** u = w / (that pulsar's mean wait, leaving out w itself).
- **Quick follow-up:** u < 0.1, so the next glitch came within a tenth of the pulsar's typical wait. Under a Poisson process about 9.5% of waits qualify.
- **Size percentile:** each glitch's size rank within its own pulsar, (rank − ½)/N.

## Hypotheses and decision rules (fixed)
- **H9 · triggering (primary).** The mean size percentile of first events that are followed quickly, pooled over pulsars, is above 0.5.
  - **Test:** permute size percentiles among each pulsar's first events, keeping waits fixed; 20 000 permutations, seed 20261123.
  - *Supported* (glitches trigger aftershocks) if the one-sided p for "greater" is below 0.05.
  - If the one-sided p for "less" is below 0.05, *the reservoir or masking direction*: the excess goes the other way, and the test cannot say which of the two causes it.
  - Otherwise *inconclusive*.
  - *Expected:* honestly uncertain. The average slope favours "less". A supported H9 would mean a minority aftershock component on top of the reservoir.
- **H10 · clustering overall.** The number of quick follow-ups is compared with a Poisson null: 5000 simulated exponential sequences with each pulsar's number of waits, normalised the same way.
  - Two-sided reading: an excess means clustering; a deficit means inhibition (reservoir) or masking.
- **H11 · follow-ups are smaller** (descriptive). The median log₁₀ ratio of the follow-up's size to the first event's size, over quick pairs. Seismology's analogue is Båth's law: the largest aftershock is about 1.2 magnitudes smaller than the mainshock.

**Declared sensitivity runs:**
- a quick window of u < 0.05 and of u < 0.2;
- at least 8 glitches per pulsar;
- without J0537−6910, the most prolific pulsar;
- without Vela, the motivating case.

## What was already seen
- G1 and G2 in full: per-pulsar slopes, CVs and gains.
- Vela's 1994 doublet and its 1981–1982 wait, from G2's post-hoc diagnostic.
- Crab glitch clustering at about 2σ (Carlin, Melatos & Vukcevic 2018, arXiv:1810.12458).
- **Not computed before this commit:** no normalised wait, quick-pair count, percentile statistic or Poisson-null comparison on real data.

## Limitations
- **Catalogue conventions.** Two glitches very close in time may be listed as one, or the second may be missed during the first one's recovery. Both remove quick follow-ups.
- **Monitoring gaps** inflate the leave-one-out mean slightly, which makes "quick" a little more permissive.
- **Weighting.** J0537−6910 and Crab pairs dominate the pooled count. The per-pulsar quick counts are reported.
