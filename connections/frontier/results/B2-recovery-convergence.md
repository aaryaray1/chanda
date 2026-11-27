# B2 results · Does the vortex-creep recovery time depend on where the data end?

**Tier T** (pre-registered, on public Fermi-LAT photons). **Status:** run as registered; self-checked; the B1 referee's systematics are applied post hoc (see the systematics section).
- **Pre-registration:** `../prereg/B2-recovery-convergence.md`, commit `5edb1c0`, made after B1's results and before any photon later than t_g + 410 d was downloaded.
- **Freeze before scoring:** `7b0466b`. It holds `../analysis/b2_convergence.py`, which reuses B1's frozen pipeline unchanged, and the extension measurements `../data/b1/nu_ext_*.json`.
- **Numbers:** `B2-results.json`.
- **Data:** five more LAT queries extend each Vela interval to t_{g+1} − 7 d. That adds 206 fourteen-day windows, with H between 921 and 23 367 and no search-edge hits.

## Answer
**The recovery slows, in every interval.** The linear-recovery estimate t₀ grows as the fit includes more of the interval:

| Glitch | t₀ (d) at D = 300 | 400 | 500 | 700 | Full interval | Observed | Published in-sample t_th |
|---|---|---|---|---|---|---|---|
| 2010 | 764 | 854 | 1002 | 1055 | **1050** | 1147 | 984 (GU22) |
| 2013 | 783 | 950 | 1100 | 1370 | **1749** | 1178 | 1862 (GU22) |
| 2016 | 652 | 690 | 648 | 661 | **674** | 781 | 781 (GU22), 774 (GR26) |
| 2019 | 663 | 813 | 850 | 924 | **922** | 902 | 769 (GU22), 922 (GR26) |
| 2021 | 514 | 518 | 544 | 603 | **658** | 1013 | 469 (GR26) |

Registered verdicts:

| Hypothesis | Result | Verdict |
|---|---|---|
| **H_B2a**, drift: t₀ at full window > t₀ at 300 d | 5 of 5 (one-sided sign test p = 0.031) | **supported** |
| **H_B2b**, agreement only at the end: full window closer than 400 d in at least 4 of 5, with median error ≤ 0.10 | closer in 3 of 5; median \|ln(t₀/t_obs)\| = 0.148 | **not supported** |

**Pre-stated reading for this combination:** *"the recovery slows, but even full-window fits do not reproduce the intervals."*

## Reading
- **The recovery slows over the interval.** The rate at which Vela's spin-down recovers after a glitch falls as the interval goes on, so a constant ν̈ is the wrong description. This is the blind form of what the B1 referee found by comparing B1 with Akbal et al.'s full-interval Model-1 fit for 2010 (their ν̈ of 0.86×10⁻²¹ against B1's early 1.43×10⁻²¹ Hz s⁻²). It explains B1's early bias.
- **Even full-interval fits do not time the glitches.** With all the data up to a week before the next glitch, the median error is 0.148, close to the 0.15–0.16 the published Vela fits score on these intervals. So:
  - the relation "glitch when the linear recovery completes" does not hold well for Vela, with any data window;
  - it does not become accurate just because the outcome is inside the fit window;
  - it overshoots for 2013 (1749 d against 1178 d) and undershoots for 2016 and 2021.
- **The pipeline reproduces published fits where the methods match.** The full-interval value for 2019 (922 d) equals Grover et al.'s 921.6 d. The value for 2013 (1749 d) is near Gügercinoğlu et al.'s 1862 d.
- **What remains open.** A model with a decelerating recovery, such as an added long exponential, could in principle be fitted blind and tested. The drift shows why that is hard: the late recovery rate is not visible in early data.

## Systematics (post hoc)
The B1 referee's corrections are applied in `../analysis/b1_systematics.py` (`B1-systematics-posthoc.json`): the corrected Vela position with proper motion, and photon-centroid window epochs.
- **H_B2a** still holds: t₀ rises in 5 of 5, from 300-d to full-interval values of 781→1044, 819→1738, 598→687, 585→917 and 535→647 d.
- **H_B2b** still fails: the median full-interval error is 0.129, above the registered 0.10.

## Deviations
None from the registered analysis. The systematics section is post hoc.

## Sources
- Akbal et al. (2017). "Nonlinear interglitch dynamics, the braking index of the Vela pulsar and the time to the next glitch". *MNRAS* 469, 4183. [arXiv:1612.03805](https://arxiv.org/abs/1612.03805)
- Gügercinoğlu et al. (2022). "Glitches in four gamma-ray pulsars and inferences on the neutron star structure". *MNRAS* 511, 425. [arXiv:2011.14788](https://arxiv.org/abs/2011.14788)
- Grover et al. (2026). "Post-glitch Recovery and the Neutron Star Structure: The Vela Pulsar". *PASA*. [arXiv:2506.02100](https://arxiv.org/abs/2506.02100)
