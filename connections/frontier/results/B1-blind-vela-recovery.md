# B1 results · Can Vela's early post-glitch recovery forecast its next glitch?

**Tier T** (pre-registered blind test on public Fermi-LAT photons). **Status:** run as registered; self-checked; independent referee pending.
- **Pre-registration:** `../prereg/B1-blind-vela-recovery.md`, commit `0114c7b`, made before any photon was downloaded.
- **Code freeze before scoring:** `c3ed7a1`. That commit holds `../analysis/b1_vela.py` and `../analysis/fitsmini.py` (numpy only), plus the measured ν(t) in `../data/b1/`.
- **Numbers:** `B1-results.json`.
- **Data:** five LAT data-server queries, each 1° around Vela, 100 MeV–300 GeV, with spacecraft files. Each covers [t_g − 160 d, t_g + 410 d] around the 2010, 2013, 2016, 2019 and 2021 glitches. That is 1.26 million events, of which 1.06 million pass the zenith-angle cut. In every 14-day window the pulse is detected with H between 2640 and 16 288.

## Answer
**No.** Measured blind (no data later than 410 d after each glitch), the vortex-creep recovery relation t₀ = (ν̇_pre − ν̇_post)/ν̈ forecasts Vela's next glitch **worse than Vela's own mean interval**:

| Glitch | Blind t₀ (d) | Observed interval (d) | Model error \|ln\| | Baseline (earlier mean) | Baseline error | Published in-sample t_th |
|---|---|---|---|---|---|---|
| 2010 | 854 | 1147 | 0.296 | 803 | 0.356 | 984 (GU22) |
| 2013 | 950 | 1178 | 0.216 | 821 | 0.361 | 1862 (GU22) |
| 2016 | 690 | 781 | 0.125 | 839 | 0.072 | 781 (GU22), 774 (GR26) |
| 2019 | 813 | 902 | 0.103 | 836 | 0.076 | 769 (GU22), 922 (GR26) |
| 2021 | 518 | 1013 | 0.671 | 839 | 0.188 | 469 (GR26) |

**Registered verdict: not supported.** The model beat the baseline in 2 of 5, with a median error of 0.216 against 0.188. All four declared sensitivity runs agree:

| Run | Model wins (of 5) | Median model error |
|---|---|---|
| Post-glitch fit from 60 d | 2 | 0.32 |
| Fit window 100–300 d | 0 | 0.41 |
| 28-day ν windows | 1 | 0.27 |
| Photons above 300 MeV | 2 | 0.22 |

**What the measurement shows (post hoc).**
- **Every blind prediction is early.** In all five intervals the next glitch came *after* the time at which the early recovery, extrapolated linearly, would complete. Five of five gives a one-sided sign-test p = 0.031. Across all variants, 24 of 25 cases are early.
- **The lag is substantial:** t_obs/t₀ = 1.34, 1.24, 1.13, 1.11 and 1.96, a median of 228 d.
- **The ranking is weak.** t₀ ranks the intervals in roughly the right order (ρ = +0.70), but with five intervals that is not significant (exact p = 0.12).
- **The measured quantities are those of a normal Vela glitch:**
  - ν̇_pre from −1.5540 to −1.5565×10⁻¹¹ Hz s⁻¹;
  - Δν̇ ≈ −1.0×10⁻¹³ Hz s⁻¹;
  - ν̈ from 1.1 to 1.8×10⁻²¹ Hz s⁻²;
  - post-fit ν residuals of 3–12 nHz.

## Reading
- **The in-sample agreement does not survive blinding.**
  - In V1, published fits that span the whole interval matched the observed intervals with a median |ln| error of 0.093.
  - Measured blind, the simplest form of the same relation errs by 0.216. That is worse than Vela's mean interval, and always in the same direction.
  - This is what V1's leakage concern predicted. It does not by itself show which ingredient of the published fits carries the information.
- **Why the blind estimate is early.** The spin-down rate recovers faster in the first ~400 days than its average over the interval. A linear fit to that early stretch therefore overestimates ν̈ and underestimates the recovery time. Two readings fit this, and the data here cannot separate them:
  - **A slower late recovery.** For example, a third exponential with τ of a few hundred days, as Grover et al. fit. A blind multi-component model could then do better than the linear one tested here.
  - **Glitches come later than recovery completion.** Vela would glitch some hundreds of days *after* its spin-down rate has returned to the pre-glitch value, rather than when it does.
  - In both readings, the recovery state measured early does not time the next glitch better than Vela's average rhythm.
- **Scope.**
  - B1 tests the simplest published form of the relation: Akbal et al.'s Model 1, linear from day 100.
  - It does not rule out a richer recovery model that predicts well blind.
  - It moves the burden to that claim. A blind fit of the full vortex-creep model, with exponentials, to the same early data is the natural next test, and the modelling groups are best placed to run it.

## Deviations
None from the registered analysis. Post hoc, and changing no registered number:
- the early bias;
- the rank correlation;
- the physical reading.

## Sources
- Akbal et al. (2017). "Nonlinear interglitch dynamics, the braking index of the Vela pulsar and the time to the next glitch". *MNRAS* 469, 4183. [arXiv:1612.03805](https://arxiv.org/abs/1612.03805)
- Gügercinoğlu et al. (2022). "Glitches in four gamma-ray pulsars and inferences on the neutron star structure". *MNRAS* 511, 425. [arXiv:2011.14788](https://arxiv.org/abs/2011.14788)
- Grover et al. (2026). "Post-glitch Recovery and the Neutron Star Structure: The Vela Pulsar". *PASA*. [arXiv:2506.02100](https://arxiv.org/abs/2506.02100)
- Basu et al. (2022). "The Jodrell Bank Glitch Catalogue: 106 new rotational glitches in 70 pulsars". *MNRAS* 510, 4049. [arXiv:2111.06835](https://arxiv.org/abs/2111.06835)
