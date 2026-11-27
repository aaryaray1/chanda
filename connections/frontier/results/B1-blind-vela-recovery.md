# B1 results · Can Vela's early post-glitch recovery forecast its next glitch?

**Tier T** (pre-registered blind test on public Fermi-LAT photons). **Status:** run as registered; refereed on 2026-11-27 ("minor revision") and revised here. The registered verdict stands. The interpretation was narrowed, and a systematics section was added.
- **Pre-registration:** `../prereg/B1-blind-vela-recovery.md`, commit `0114c7b`, before any photon was downloaded.
- **Code freeze before scoring:** `c3ed7a1`. It holds `../analysis/b1_vela.py` and `../analysis/fitsmini.py` (numpy only), plus the primary ν(t) in `../data/b1/`.
- **Numbers:** `B1-results.json`. **Post-hoc systematics:** `../analysis/b1_systematics.py` and `B1-systematics-posthoc.json`.
- **Data:** five LAT data-server queries, each 1° around Vela, 100 MeV–300 GeV, with spacecraft files, covering [t_g − 160 d, t_g + 410 d] around the 2010, 2013, 2016, 2019 and 2021 glitches. That is 1.26 million events, 1.06 million after the zenith-angle cut. The pulse is detected in every 14-day window, with H between 2640 and 16 288.
- **Referee checks:**
  - The barycentring is verified: Roemer sign, units, TDB term, Horizons frame, FT2 units and MJDREF.
  - Folds over 56–200 d give a sharp Vela profile, with a main-peak FWHM of 0.02–0.05 cycles.
  - Scoring reproduces exactly.

## Answer
**The constant-ν̈ form of the vortex-creep recovery relation shows no blind skill for Vela, and it predicts every next glitch too early.**

The relation is Akbal et al.'s Model 1: t₀ = (ν̇_pre − ν̇_post)/ν̈, measured from data up to 400 d after each glitch.

| Glitch | Blind t₀ (d) | Observed interval (d) | Model error \|ln\| | Baseline: geometric mean of earlier intervals | Baseline error | Published in-sample t_th |
|---|---|---|---|---|---|---|
| 2010 | 854 | 1147 | 0.296 | 803 | 0.356 | 984 (GU22) |
| 2013 | 950 | 1178 | 0.216 | 821 | 0.361 | 1862 (GU22) |
| 2016 | 690 | 781 | 0.125 | 839 | 0.072 | 781 (GU22), 774 (GR26) |
| 2019 | 813 | 902 | 0.103 | 836 | 0.076 | 769 (GU22), 922 (GR26) |
| 2021 | 518 | 1013 | 0.671 | 839 | 0.188 | 469 (GR26) |

**Registered verdict: not supported.** The model beat the baseline in 2 of 5, with a median error of 0.216 against 0.188. That means no skill was shown; the model is not shown to be significantly worse. The baseline is the geometric mean of Vela's earlier large-glitch intervals, 803–839 d. Their arithmetic mean is about 1010 d, and the baseline is itself early in 4 of 5.

All four declared sensitivity runs agree:

| Run | Model wins (of 5) | Median model error |
|---|---|---|
| Post-glitch fit from 60 d | 2 | 0.32 |
| Fit window 100–300 d | 0 | 0.41 |
| 28-day ν windows | 1 | 0.27 |
| Photons above 300 MeV | 2 | 0.22 |

**Compared like with like (post hoc).** On these same five intervals, the published in-sample t_th, fitted with data through the next glitch, would score 2 of 5 (median 0.159, preferring GU22's values) or 3 of 5 (median 0.153, preferring GR26's) under the same rule. So for Vela the published fits are only modestly better than the blind estimate. The pooled in-sample agreement in V1 (0.093) comes mostly from other pulsars, and V1 itself found that Vela alone does not beat its mean.

**The early bias (post hoc, exploratory).**
- **Every blind t₀ is early:** t_obs/t₀ = 1.34, 1.24, 1.13, 1.11 and 1.96, a median lag of 229 d.
- **Significance:** 5 of 5 gives a two-sided sign-test p = 0.063, and 24 of 25 cases are early across the variants. The direction was noticed after seeing the data.
- **Ranking:** t₀ ranks the intervals in roughly the right order (ρ = +0.70, exact p = 0.12 at n = 5).
- **Measured values:**
  - ν̇_pre from −1.5540 to −1.5565×10⁻¹¹ Hz s⁻¹;
  - Δν̇ from −0.76 to −1.14×10⁻¹³ Hz s⁻¹;
  - ν̈ from 1.1 to 1.8×10⁻²¹ Hz s⁻²;
  - post-fit ν residuals of 3–12 nHz.

## Reading
- **Why the blind estimate is early: the recovery slows.**
  - Akbal et al. (2017) fitted the same Model 1, also from +100 d but up to the next glitch. For the 2010 interval their ν̈ is 0.86×10⁻²¹ Hz s⁻² (from Ω̈ = 5.4×10⁻²¹ rad s⁻³), against B1's early 1.43×10⁻²¹. Their glitch steps agree with ours (9.5 against 10.5×10⁻¹⁴ Hz s⁻¹). Their t_g is 1281 d, 134 d *late*. Only the end of the fit window differs, so a constant ν̈ is the wrong description.
  - B2 confirms this blind in all five intervals: t₀ grows as the fit window extends (`B2-recovery-convergence.md`). The early-time recovery is faster than the late-time recovery, and the linear extrapolation from early data finishes too soon.
  - This disfavours the alternative reading, that Vela glitches long after full recovery, at least for 2010.
- **What B1 establishes.** For Vela, the recovery state measurable in the first ~400 days does not time the next glitch better than Vela's own average rhythm, under the constant-ν̈ model. It does not rule out a richer recovery model that predicts well blind.

## Systematics (post hoc, after the referee)
- **Position.** The frozen code used Dec −45.1763264°, a 0.10″ conversion slip (it should be −45.1763542°), and ignored Vela's proper motion (−49.7, +29.9 mas/yr from epoch MJD 51544). This gives annual Roemer errors of 1.5–3.1 ms, which move ν̈ by up to about 9%.
- **Window epochs.** With ν̇ fixed in the fold and the epoch at the window midpoint, windows with uneven photon coverage are biased. For example, the 2013 window at +133 d had photons only in its last 3 days.
- **Corrected** (true position with proper motion, photon-centroid epochs, the registered window membership): t₀ = 889, 892, 648, 767 and 536 d. Still 2 of 5, median error 0.255, all five early.
- **Statistical errors:** residual-bootstrap errors on t₀(400) are ±19, ±22, ±14, ±25 and ±8 d. Those are white-noise only; timing noise makes the true errors larger. Systematics add up to about ±50 d. The 2019 interval is early at only about 1.8σ when both are combined.
- **The 2014 glitch.** The 2013 post-glitch window contains the MJD 56922 glitch (Δν/ν = 4×10⁻¹⁰, at +366 d). Removing its step moves t₀ by +14 to +17 d.
- **None of these changes the verdict or the early bias.**

## Deviations
- **The sensitivity ν(t) files** were not part of the freeze. They were first committed in `588cda4`, and are reproducible from the frozen code.
- **The skip of windows with fewer than 200 photons** was not registered. It drops one pre-glitch window in 2019.
- **The 2016 interval** is 781.1 d, not 782 d as the registration states.
- **Corrections in this revision.** The first version of this file:
  - said the in-sample agreement "does not survive blinding", comparing a pooled six-pulsar figure with five Vela intervals;
  - said the two physical readings could not be separated;
  - called the post-hoc sign test one-sided with p = 0.031.

  All three are corrected above.

## Sources
- Akbal et al. (2017). "Nonlinear interglitch dynamics, the braking index of the Vela pulsar and the time to the next glitch". *MNRAS* 469, 4183. [arXiv:1612.03805](https://arxiv.org/abs/1612.03805)
- Gügercinoğlu et al. (2022). "Glitches in four gamma-ray pulsars and inferences on the neutron star structure". *MNRAS* 511, 425. [arXiv:2011.14788](https://arxiv.org/abs/2011.14788)
- Grover et al. (2026). "Post-glitch Recovery and the Neutron Star Structure: The Vela Pulsar". *PASA*. [arXiv:2506.02100](https://arxiv.org/abs/2506.02100)
- Basu et al. (2022). "The Jodrell Bank Glitch Catalogue: 106 new rotational glitches in 70 pulsars". *MNRAS* 510, 4049. [arXiv:2111.06835](https://arxiv.org/abs/2111.06835)
