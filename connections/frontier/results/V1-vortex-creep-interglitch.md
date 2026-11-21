# V1 results · Do vortex-creep predictions of the time to the next glitch track the observed intervals?

**Tier T** (pre-registered meta-analysis of published model fits) **plus a post-hoc contrast with prospective forecasts.** **Status:** run as registered; referee pending.
- **Pre-registration:** `../prereg/V1-vortex-creep-interglitch.md`, commit `71011da`.
- **Extraction and code:** committed before the run, in `5c3540f`: `../data/v1/pairs.json` and `../analysis/v1_meta.py`. **Numbers:** `V1-results.json`.
- **Post-hoc contrast:** `../analysis/v1_contrast.py`, with results in `V1-contrast-posthoc.json`.

## Answer
**In-sample, yes.** Across 36 published pairs from 6 papers and 7 pulsars, the model's theoretical time to the next glitch t_th tracks the observed interval t_obs. It does so *within* pulsars, beyond each pulsar's typical rhythm.

| Test (registered) | Result | Verdict |
|---|---|---|
| **H_V1**, within-pulsar tracking: Spearman of normalised t_th against t_obs | ρ = +0.71, one-sided permutation p = 0.0001 (32 pairs, 4 pulsars) | **supported** |
| **H_V2**, skill against the pulsar's leave-one-out mean interval | model closer in 24 of 34, sign test p = 0.012; median error 0.093 vs 0.190 (\|ln ratio\|) | **supported** |

Robustness:
- Both hold with the earliest paper's value for each glitch, and with the zero-degrees-of-freedom fit dropped.
- **Vela alone** (19 pairs): tracking holds (ρ = +0.59, p = 0.004), but the model does not beat the mean (11 of 19).
- **Without Vela:** ρ = +0.80 (p = 0.008), and the model wins 13 of 15.
- Within-pulsar ρ: Vela 0.59, J1023−5746 0.90, J2229+6114 0.40, J1420−6048 0.40.

**Prospectively, no (post hoc).** The same model's forecasts made *before* the next glitch, scored in T04, err much more:

| Set | Median \|ln(t_th / t_obs)\| |
|---|---|
| In-sample pairs (V1) | **0.093** |
| Pulsar's own mean interval (baseline) | 0.190 |
| Prospective forecasts, resolved (3) | **0.34** |

The three resolved prospective forecasts:
- **Vela 2019→2021:** 769 d predicted, 902 d observed (0.16).
- **J2229+6114 2018→2021:** 619 d predicted, 866 d observed (0.34).
- **Akbal et al. 2017 (Vela):** 1364 d predicted, 812 d observed (0.52). This forecast was posted about 6 hours after the glitch.

Four more prospective vortex-creep forecasts have no catalogued outcome. If the catalogue is complete, their errors are at least 0.55–1.23. One of them, Liu et al.'s J1420−6048 forecast, has already failed in the paper's own data.

**When the same glitch was analysed before and after its successor, the estimate moved toward the observed interval** (post hoc):

| Glitch | Before the next glitch | After it | Observed |
|---|---|---|---|
| J2229+6114, 2018 glitch | 619 d (arXiv:2011.14788v1, Nov 2020): error 0.31 | 857 d (v2, Feb 2022): error 0.014 | 845 d |
| Vela 2019 glitch | 769 d (v1, Nov 2020; v2 kept it): error 0.16 | 921.6 d (Grover et al. 2025): error 0.021 | 902 d |

## Reading
- **What the in-sample result shows.** Across Vela, J1023−5746, J2229+6114 and J1420−6048, the time at which the fitted post-glitch recovery would complete lines up with the next glitch: closely, and better than the pulsar's average rhythm. That is the reservoir-refill claim of the vortex-creep model, and the pooled data support it as a *consistency* relation.
- **Why it is not yet a forecast.** The recovery fits use timing data that run up to the next glitch. In the simplest case t₀ is the glitch step in spin-down divided by the interglitch recovery rate, and that rate is fitted over the whole interval. If the spin-down rate has returned to about its pre-glitch value by the next glitch, t₀ then lands near t_obs by construction.
  - The prospective record, about three times worse than in-sample and worse than the naive baseline, fits that reading.
  - So do the two revisions that moved toward the outcome once it was known.
  - Both rest on few cases: 3 resolved forecasts and 2 revisions.
- **What would settle it.** Fit only the first part of each recovery, for example the first half of each interval or a fixed number of days, then predict the rest. The timing data for the Fermi-LAT pulsars are public. The registered forecasts still open will add cases: Liu et al.'s J1028−5819 forecast and Grover et al.'s vortex-creep window for Vela (T04, G2-P).
- **Tone.** This compares in-sample agreement with forecast skill. It is not a claim that the model is wrong. Akbal et al. (2017) and Grover et al. (2025) themselves discuss intervals where the recovery did not complete before the next glitch.

## Deviations
- **H_V2's pulsar set.** The registration said pulsars with fewer than 3 pairs enter H_V2. Two pulsars with a single pair (J2111+4606 and J0738−4042) have no leave-one-out mean, so H_V2 uses the 34 pairs from pulsars with at least 2.
- **J0537−6910.** Excluded by the registered rule (its paper gives no t_obs or epochs). Its "Δ (days)" column is undefined in the text.
- **Post hoc:** the in-sample versus prospective contrast and the before/after revisions.

## Sources
- Akbal et al. (2017). "Nonlinear interglitch dynamics, the braking index of the Vela pulsar and the time to the next glitch". *MNRAS* 469, 4183. [arXiv:1612.03805](https://arxiv.org/abs/1612.03805)
- Gügercinoğlu & Alpar (2020). "The 2016 Vela glitch: a key to neutron star internal structure and dynamics". *MNRAS* 496, 2506. [arXiv:2003.08724](https://arxiv.org/abs/2003.08724)
- Gügercinoğlu et al. (2022). "Glitches in four gamma-ray pulsars and inferences on the neutron star structure". *MNRAS* 511, 425. [arXiv:2011.14788](https://arxiv.org/abs/2011.14788)
- Akbal et al. (2021). "Glitch analysis and braking index determination of the unique source PSR J0537-6910". *arXiv preprint*. [arXiv:2106.03341](https://arxiv.org/abs/2106.03341)
- Liu et al. (2024). "A multi-band study of pulsar glitches with Fermi-LAT and Parkes". *arXiv preprint*. [arXiv:2408.15022](https://arxiv.org/abs/2408.15022)
- Grover et al. (2026). "Post-glitch Recovery and the Neutron Star Structure: The Vela Pulsar". *PASA*. [arXiv:2506.02100](https://arxiv.org/abs/2506.02100)
- Zhou et al. (2022). "New pulse profile variability associated with a glitch of PSR J0738-4042". *MNRAS*. [arXiv:2205.08296](https://arxiv.org/abs/2205.08296) · [doi:10.1093/mnras/stac3355](https://doi.org/10.1093/mnras/stac3355)
