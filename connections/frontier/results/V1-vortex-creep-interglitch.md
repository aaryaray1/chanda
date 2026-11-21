# V1 results · Do vortex-creep predictions of the time to the next glitch track the observed intervals?

**Tier T** (a pre-registered meta-analysis of published model fits) **plus post-hoc comparisons.** **Status:** run as registered; refereed on 2026-11-21 ("needs revision") and revised here. Two extracted pairs were corrected, and the post-hoc contrast was rewritten.
- **Pre-registration:** `../prereg/V1-vortex-creep-interglitch.md`, commit `71011da`.
- **Extraction and code:** committed before the run, in `5c3540f`: `../data/v1/pairs.json` and `../analysis/v1_meta.py`. **Numbers:** `V1-results.json`, whose `posthoc` key holds the sensitivity runs.
- **Post-hoc contrast:** `../analysis/v1_contrast.py`, with results in `V1-contrast-posthoc.json`.

## Answer
**In-sample, yes.** There are 35 published pairs from 5 papers and 6 pulsars. Each pairs the model's time to the next glitch t_th with the observed interval t_obs. t_th tracks t_obs *within* pulsars, beyond each pulsar's typical rhythm:

| Test (registered) | Result | Verdict |
|---|---|---|
| **H_V1**, within-pulsar tracking: Spearman of normalised t_th against t_obs | ρ = +0.66, one-sided permutation p = 1.5×10⁻⁴ (32 pairs, 4 pulsars) | **supported** |
| **H_V2**, skill against the pulsar's leave-one-out mean interval | model closer in 25 of 34, sign test p = 0.0045; median \|ln ratio\| 0.093 vs 0.186 | **supported** |

**Sensitivity runs:**
- Both hold with each glitch's earliest published value, and with the zero-degrees-of-freedom fit dropped.
- They also hold with Grover et al.'s own t₀ ± 3τ_nl convention (ρ = +0.66, 25 of 34).
- **Adding J0537−6910 (post hoc).** Its paper gives no t_obs, so the 35 t₀ values were mapped to catalogue epochs:
  - pooled ρ = +0.70 to +0.71 over 66 pairs, and the model wins 44–46 of 68;
  - within J0537−6910 the model tracks (ρ = +0.74 to +0.76) but beats the mean in only 19–21 of 34.
- **Within-pulsar ρ:** Vela 0.59, J1023−5746 0.90, J2229+6114 0.40, J1420−6048 0.40.
- **Vela alone** tracks (p = 0.004) but does not beat the mean (11 of 19).

**The tracking is not specific to vortex creep (post hoc).** Glitch size alone tracks the following interval: ρ = +0.46, p = 0.005, over the same 32 pairs. Within Vela, size gives 0.53 against t_th's 0.59, and t_th itself correlates with size at 0.74. That a larger glitch is followed by a longer wait is G2's reservoir sign, and it is long known for J0537−6910. Much of what t_th carries is the glitch size.

**Forecasts made before the next glitch (post hoc, suggestive only).** Only one case is clean, and the model did worse than the pulsar's own earlier mean in all three resolved cases:

| Case | Class | Model error | Own-baseline error |
|---|---|---|---|
| Vela 2019 (arXiv:2011.14788v1) | clean: fitted and posted before the next glitch | 0.16 | 0.11 |
| J2229+6114 2018 (v1) | not clean: a zero-dof fit, stated as a lower bound, which was met | 0.34 | 0.04 |
| Vela 2014 (Akbal et al. v1) | contemporaneous: posted about 6 h after the glitch | 0.52 | 0.23 |

The other cases:
- **Still open:** J1023−5746 and J2111+4606. Both are overdue, or their glitches are missing from the catalogue.
- **Already failed or past when published:** J1420−6048 and J1709−4429. Their predicted dates had passed before posting, so they are not prospective.

**When one glitch was analysed before and after its successor**, the picture is mixed:

| Glitch | Before | After | What changed |
|---|---|---|---|
| J2229+6114, 2018 (same group) | 619 d, error 0.34 | 857 d, error 0.014 | epoch re-dated; data extended through the next glitch; model components changed; a zero-dof fit replaced |
| Vela 2019 | 769 d, error 0.16 | the same group's v2 **kept** 769 d after the outcome and footnoted the miss; Grover et al. (a different team) later gave 921.6 d, error 0.021 | different data and analysis |
| Vela 2013/14 (same group, Akbal v1 → v3) | 1364 d from 2014, error 0.52 | 1553 d from 2013, still **375 d late** (error 0.28); a later paper gave 1862 d (0.46) | re-anchored after the outcome |

Knowing the outcome did not force agreement.

## Reading
- **What is established.** Across Vela, J1023−5746, J2229+6114, J1420−6048 and, post hoc, J0537−6910, the published vortex-creep times to the next glitch line up with the observed intervals within each pulsar. They beat the pulsar's average rhythm in 25 of 34 pairs. As a consistency relation, the pooled data support the model's claim that a glitch comes when the post-glitch recovery is complete. Glitch size alone, though, carries much of the same information.
- **What is not established: forecast skill.**
  - **Fit windows.** Most fits use timing data through to the next glitch: Akbal et al.'s triangle fits, and the full-interval fits of Gügercinoğlu et al., Liu et al. and Grover et al. For t₀ the offset time is set by the recovery slope over that window. Grover et al. state that their t₀ prior's initial guess was "often chosen close to the observed time to the next glitch".
  - **Model choice.** The model components are also chosen glitch by glitch with the outcome known.
  - **This does not make agreement automatic.** t₀ marks when the spin-down rate has recovered. That this coincides with the next glitch is the model's empirical claim, not an identity. There are clear counterexamples: Vela 2013 (1862 d against 1178 d), J1420−6048 G7 and G8, and the Vela 2013/14 revision that stayed 375 d late.
  - **The one partial-data case went the model's way.** Gügercinoğlu & Alpar (2020) used Xu et al.'s fit to the first 416 days after the 2016 Vela glitch and got t₀ = 781 d, against 782 d observed. It was not blind: they wrote after the 2019 glitch.
- **What would settle it.** Fit only the early part of each recovery, blind to the next glitch, then score the predicted interval against the pulsar's own baseline. The timing data for the Fermi-LAT pulsars are public. The two open prospective forecasts (J1023−5746 and J2111+4606), and the registered forecasts in T04 and G2-P, will add cases.

## Deviations
- **Corrected after the referee** (`data/v1/pairs.json` records each correction):
  - J0738−4042 is removed: its pair was the duration of a 2007 timing event, not a time to the next glitch.
  - J2229+6114's 2013 pair now uses the interval to the next glitch, 1628 d. The paper's 975 d is the observed end of the recovery.
  - With these fixes the verdicts are unchanged: ρ went from 0.705 to 0.663, and the win count from 24/34 to 25/34.
- **H_V2's pulsar set.** The registration said pulsars with fewer than 3 pairs enter H_V2. J2111+4606, with a single pair, has no leave-one-out mean, so H_V2 uses the 34 pairs from pulsars with at least 2.
- **J0537−6910.** Excluded by the registered rule, because its paper gives no t_obs or epochs. Its Δ column is the lag from the glitch to the first post-glitch observation (§3). It is included only as a post-hoc sensitivity run, mapped to catalogue glitches 1–45 by number. That mapping is checked: the two glitches the paper could not analyse are the catalogue's two smallest.
- **Post hoc:** the size comparison, the t₀ ± 3τ_nl convention, the J0537−6910 runs, the prospective table and the revision table.

## Sources
- Akbal et al. (2017). "Nonlinear interglitch dynamics, the braking index of the Vela pulsar and the time to the next glitch". *MNRAS* 469, 4183. [arXiv:1612.03805](https://arxiv.org/abs/1612.03805)
- Gügercinoğlu & Alpar (2020). "The 2016 Vela glitch: a key to neutron star internal structure and dynamics". *MNRAS* 496, 2506. [arXiv:2003.08724](https://arxiv.org/abs/2003.08724)
- Gügercinoğlu et al. (2022). "Glitches in four gamma-ray pulsars and inferences on the neutron star structure". *MNRAS* 511, 425. [arXiv:2011.14788](https://arxiv.org/abs/2011.14788)
- Akbal et al. (2021). "Glitch analysis and braking index determination of the unique source PSR J0537-6910". *arXiv preprint*. [arXiv:2106.03341](https://arxiv.org/abs/2106.03341)
- Liu et al. (2024). "A multi-band study of pulsar glitches with Fermi-LAT and Parkes". *arXiv preprint*. [arXiv:2408.15022](https://arxiv.org/abs/2408.15022)
- Grover et al. (2026). "Post-glitch Recovery and the Neutron Star Structure: The Vela Pulsar". *PASA*. [arXiv:2506.02100](https://arxiv.org/abs/2506.02100)
