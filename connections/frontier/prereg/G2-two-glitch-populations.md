# Pre-registration G2 · Are large glitches predictable and small glitches Poisson?

**Registered:** 2026-11-21, with `../analysis/g2_two_populations.py`. It reuses G1's models and scoring unchanged, and passed its self-test on synthetic data only.

## Why
G1 found that waiting times between glitches of any size are only weakly predictable beyond Poisson. Two of its observations suggest that two kinds of glitch are mixed together:
- Vela is quasi-periodic (CV 0.58), yet the renewal model loses to Poisson there.
- Predictability rises with median glitch size (ρ = +0.39 primary, +0.40 with p = 0.014 in the 30-pulsar sensitivity run).

**Hypothesis.** Large glitches come from a reservoir that refills at a steady rate, so their timing is predictable. Small glitches come from a different, Poisson-like trigger.

The question has a long qualitative history: Vela-like versus Crab-like pulsars, the bimodal glitch-size distribution, and the "compact" versus "extended" modes of Liu et al. (2026). G2 tests it in the time domain, out of sample, and within the same stars.

**A detection effect to rule out.** G1's positive size–wait slopes could come from detection. Post-glitch recovery hides small glitches after large ones, which lengthens the observed wait. Large glitches are not hidden that way, so a positive slope *among large glitches alone* would be physical.

## Data and classes (fixed)
- **Data:** the same snapshot as G1: Jodrell Bank, 2026-11-20, SHA-256 `e811419f…`.
- **Classes:** **large** is Δν/ν ≥ 10⁻⁷ (100 in catalogue units), the same threshold T04 used. **Small** is Δν/ν < 10⁻⁷. Glitches with no size are dropped.
- **Thinning:** each class is its own sequence. A small glitch does not interrupt the large-glitch sequence, and the reverse.
- **Inclusion:** pulsars with at least 8 glitches in the class.
  - **Large, 7 pulsars and 104 forecasts:** J0537−6910 (59), Vela (21), J1341−6220 (20), J1740−3015 (13), J1413−6141 (10), J1420−6048 (8), J2229+6114 (8).
  - **Small, 7 pulsars and 73 forecasts:** Crab (30), J1740−3015 (25), J0631+1036 (15), J1341−6220 (13), J0537−6910 (9), J0742−2822 (8), J1801−2304 (8).
  - Three pulsars are in both classes: J0537−6910, J1341−6220 and J1740−3015.
- **Models, scoring and bootstrap:** G1's, unchanged: M0 Poisson, M1 log-normal renewal, M3 size-conditioned. The statistics are the pulsar-averaged information gain and a pulsar-block bootstrap with 20 000 draws.

## Hypotheses and decision rules (fixed)
- **H5 · large glitches are predictable.** For the large class, the pulsar-averaged IG(M1|M0) > 0, with a one-sided 95% lower bound above 0.
  - *Expected:* supported.
- **H6 · small glitches are Poisson-like.** For the small class, the pulsar-averaged IG(M1|M0) has a 95% upper bound below +0.10 nats per forecast.
  - *Refuted* if its 95% lower bound is above 0.
  - *Expected:* supported. Under a true Poisson process the expected IG is negative, about −0.2 in the self-test.
- **H7 · contrast.** The large-class minus the small-class pulsar-averaged IG(M1|M0) has a 95% lower bound above 0. The two classes are bootstrapped independently.
  - The difference within each of the three pulsars in both classes is reported.
  - *Expected:* supported.
- **H8 · the reservoir signal is physical.** Two parts:
  - (a) Among large glitches only, the full-sample slope of log wait on log size is positive in at least 6 of 7 pulsars. The one-sided sign test is reported: 6 of 7 gives p = 0.0625, 7 of 7 gives p = 0.0078.
  - (b) For the large class, the out-of-sample IG(M3|M1) is reported with its interval. It is *supported* if the lower 95% bound is above 0, and inconclusive otherwise.
  - *Expected:* (a) supported; (b) driven by J0537−6910, which is known to have its wait scale with the preceding glitch's size.

**Calibration** of M1 in each class is reported, as in G1's H4, with no decision rule.

**Declared sensitivity runs:**
- the threshold raised to 5×10⁻⁷ (`--threshold 500`; large class: 3 pulsars);
- at least 6 per class (`--min-per-class 6`).

## What was already seen
- All of G1 (`../results/G1-glitch-predictability.md`), including per-pulsar any-size gains, CVs and slopes.
- The class counts above.
- J0537−6910's 2264-day RXTE–NICER gap, which falls in both its classes.
- **Not computed before this commit:** no class-thinned gain, slope, CV or calibration.

## Limitations
- **Small samples:** seven pulsars per class give coarse bootstrap intervals.
- **A sharp cut:** a single threshold cuts a continuous size distribution. The sensitivity run moves it.
- **Detectability:** small glitches are the class most affected by detection limits and catalogue incompleteness. Missed small glitches thin the small sequence at random, which keeps a Poisson process Poisson but stretches a renewal process toward Poisson. So H6 may be supported partly by incompleteness.
