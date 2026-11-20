# T01 results · The 2018 glitch size–waiting-time predictions on the 2026 catalogue

**Tier T** (pre-registered test on public data). **Status:**
- **P1 survives,** though the evidence is mostly in-sample: post-2018 data come from J0537−6910 only, and the test could barely fail.
- **P2 is inconclusive,** because the test was underpowered.
- **Novelty:** *partly known*.
- **Refereed** on 2026-11-21 (F6). This version applies the referee's fixes; see "Revision" at the end.

**Pre-registration:** `../prereg/T01-glitch-correlations.md`, commit `bf6476f`. **Code:** `../analysis/t01_glitches.py`.
- `run` gives the registered tests (`T01-results.json`).
- `posthoc` gives every analysis added afterwards (`T01-posthoc.json`). None of those is pre-registered.

**Data** (fetched 2026-11-20 22:15 UTC; both snapshots are archived in `../data/t01/`):
- **Jodrell Bank Glitch Catalogue:** SHA-256 `e811419f…aabeb4`. The header lists 737 glitches in 226 pulsars. The parser keeps 736 glitches (733 with a size) in 225 pulsars, because AX J1838.0−0655 has no J-name.
- **ATNF Pulsar Catalogue:** v2.9.0, for F1.

## Answer
Melatos, Howitt & Fulgenzi (2018) made two predictions for future data. Neither is refuted, and neither is strongly confirmed.
- **P1** (no pulsar shows a strong correlation between glitch size and the wait *before* it, r₋ ≤ 0.5) **survives** in all 10 pulsars with ≥ 10 glitches. Pooling them gives r₋ = +0.03 (95% CI −0.10 to +0.16), consistent with the paper's typical r₋ ≲ 0.1. Three things limit this:
  - **Most of the data are old:** 84% of the pairs predate the prediction. The only genuinely new per-pulsar test is J0537−6910 (ρ₋ = −0.17, n = 20 post-2018 pairs).
  - **The test could barely fail:** it would have needed r₋ of 0.75 to 0.96, depending on the pulsar.
  - **The 2018 backward hints vanished through catalogue revisions, not new glitches.** The Crab's hint hinges on a single small glitch.
- **P2** (the size–next-wait correlation r₊ rises with −ν̇⟨Δt⟩, the stress added between glitches) is **inconclusive**. The registered trend is −0.32 (14 pulsars). That gives one-sided p = 0.87 in P2's direction, and p = 0.13 for the opposite sign. With 14 pulsars, passing needed a trend of about +0.62. The sample also never reaches the low-stress end of the distribution, where the paper's low-end targets sit.

## Registered results
| Test | Result | Verdict |
|---|---|---|
| **Control:** J0537−6910 forward correlation | ρ₊ = 0.931, n = 67, p ≤ 1×10⁻⁵ (the floor for 10⁵ permutations) | pass |
| **H1a:** no detectable backward correlation, a stronger claim than P1, which allows a weak positive r₋ (10 pulsars, per-pulsar α = 2.7×10⁻⁴) | smallest two-sided p = 0.20 (Vela) | survives |
| **H1b:** r₋ ≤ 0.5, P1's registered bound | largest r₋ = 0.43 (Vela); one-sided p for H₀: r₋ ≤ 0.5 = 0.66 | survives; weak test, see below |
| **H2:** Spearman(log₁₀ −ν̇⟨Δt⟩, r₊), N ≥ 8 | −0.319, 14 pulsars; one-sided p = 0.87 for P2's sign | inconclusive |

**Registered secondary analyses:**
- **H2 variants:** with N ≥ 6, −0.021 (30 pulsars); with ρ₊ in place of r₊, −0.029 (N ≥ 8) and +0.171 (N ≥ 6).
- **H1 on new data only:** J0537−6910, ρ₋ = −0.17 (n = 20, p = 0.48). Its forward correlation also persists in the new data (r₊ = 0.92 on 19 pairs), as Ho et al. (2020) found.
- **Table 2 targets:** too few pairs to rank. J0205+6449 has 8 pairs, J2229+6114 9, and the rest 3–6.
- **Replication of the paper's Table 1** (glitches up to MJD 58370): only 2 of 7 pulsars come close.
  - **J1740−3015** is within 0.07: 36 glitches here against the paper's 35.
  - **J1801−2304** is within 0.04.
  - **J0537−6910's** r₊ drops from 0.93 to 0.25 because of the observing gap described below.
  - **J0631+1036's** r₊ rises from 0.70 to 0.93 (17 glitches against 15).
  - **J1341−6220** now lists 33 glitches before 2018 against the paper's 23.
  - **The Crab and Vela** each gained small glitches through catalogue revisions.

## What limits the P1 result
- **Composition.** Of 255 backward pairs, 40 involve a glitch after MJD 58370, and J0537−6910 supplies 20 of those. J0631+1036, J1341−6220 and J1413−6141 have no catalogued glitch after 2018 at all.
- **Power.** These are the smallest r₋ values that would have refuted H1b at the registered threshold:

  | J0537 | J1740 | Crab | J1341 | Vela | J0631 | J1801 | J1413 | J1048 | J2229 |
  |---|---|---|---|---|---|---|---|---|---|
  | 0.75 | 0.82 | 0.83 | 0.83 | 0.86 | 0.91 | 0.92 | 0.93 | 0.94 | 0.96 |

  Against the paper's sharper r₋ ≲ 0.1, Vela gives one-sided p = 0.046, which is not significant after correction.
- **The vanished 2018 hints come from revisions, not new data.**
  - **Crab:** the post-1985 backward correlation of 2018 (r₋ = 0.69, three sigma) is now −0.07 on pre-2018 data. That change comes entirely from one 2.2×10⁻⁹ glitch at MJD 57839.8, which splits the 6-year wait before the 2017 giant glitch. Removing it restores r₋ = 0.69.
  - **Vela:** its r₋ fell from 0.60 to 0.37 through revisions of pre-2018 data, and the post-2018 glitches raise it again to 0.43.

  Pearson r₋ on sizes that span four decades rests on single events.
- **Contrary evidence for the Crab.** Zhu et al. (2025) group five decades of Crab glitches, up to 2025, into clusters. They find that cluster size correlates more strongly with the *preceding* wait than with the following one. That is a backward correlation at the cluster level. It depends on how the clusters are chosen, so it is contested rather than a refutation, but it means "backward correlations stay weak" holds only per glitch.
- **The paper's other P1 statement was not registered.** The paper also predicts that the highest of the low r₋ values lie at the low-stress end. On these data the trend has the wrong sign but is not significant: Spearman(X, r₋) = +0.09 (n = 14; one-sided p = 0.63 for the predicted negative sign). This is reported as exploratory.

## What limits the P2 result
- **Pearson r₊ is driven by outliers.** J0631+1036 has r₊ = 0.93 but ρ₊ = 0.21. On the control pulsar, the registered statistic gives r₊ = 0.25 because of a single 2,264-day wait spanning the gap between RXTE (to 2011) and NICER (from 2017).
- **A post-hoc grid (`posthoc`) drops waits longer than 5 × the pulsar's median wait** (⟨Δt⟩ not recomputed). It gives Spearman(X, r₊) for all 8 variants:

  | Correlation used | Sample | With the Crab | Without the Crab |
  |---|---|---|---|
  | r₊ | N ≥ 8 | −0.05 | +0.19 |
  | r₊ | N ≥ 6 | +0.17 | +0.25 |
  | ρ₊ | N ≥ 8 | +0.01 | +0.26 |
  | ρ₊ | N ≥ 6 | +0.28 (p = 0.08) | **+0.37 (p = 0.03)** |

  One of 8 variants reaches p < 0.05. After choosing among 8, that is not evidence. It hints that a better-powered test might favour P2 once gaps are removed and the Crab, which the authors call a misfit, is set aside.
- **Interpretation.** P2 is untested at useful power. Pulsar-to-pulsar variation in x_cr or β is one possible explanation of the null result, alongside low power and outliers. In the paper, r₊ steps with α, so a measured r₊ bounds the combination β^{1/2} x_cr from one side (§5, eq. 9). It does not measure x_cr.

## Exploratory: forward correlations (not registered; no registry update)
Size against the wait that follows, in pulsars with ≥ 10 glitches. Under the 10-pulsar Bonferroni rule used for H1 (α = 2.7×10⁻⁴, one-sided), two pulsars survive:
- **J0537−6910:** ρ₊ = 0.93, p ≤ 10⁻⁵ (known);
- **J1341−6220:** ρ₊ = 0.62, p = 8×10⁻⁵. In 2018 it was "arguably" emerging at p = 4.8×10⁻³ with N = 23. The 10 extra glitches are all pre-2018 events that were catalogued later.

These do not survive:
- **J1413−6141:** ρ₊ = 0.82, p = 4.5×10⁻⁴. No glitch is catalogued after 2017.
- **J1801−2304:** ρ₊ = 0.71, one-sided p = 2.5×10⁻³.
- **J1048−5832:** ρ₊ = 0.76, p = 4×10⁻³.

**Caveats:**
- **Exchangeability:** the permutation tests assume exchangeable pairs. Glitch sizes can be serially correlated (the Crab's size autocorrelation is ρ = −0.46; Carlin & Melatos 2019), so p-values near 10⁻³ are approximate.
- **Selection effects** can create a positive r₊. Post-glitch recovery hides small glitches, and observing gaps lengthen waits.
- **Rival models:** Carlin & Melatos (2020) predict ρ₊ > 0.25 in every pulsar from Brownian stress accumulation. A forward correlation shows that size and wait are not independent; it does not single out the state-dependent Poisson model.
- **A second published prediction, checked after the fact.** Carlin & Melatos (2020) predict ρ₊ > 0.25 in all pulsars. With 2020 data they found J1740−3015 and J0631+1036 inconsistent with it, and the Crab and J1341−6220 consistent only if small glitches are missing. On the 2026 catalogue (values already seen in T01, so exploratory):
  - J1740−3015: ρ₊ = 0.37 (n = 37 pairs), now above 0.25;
  - J0631+1036: 0.21 (n = 16);
  - Crab: 0.14 (n = 31);
  - J1341−6220: 0.62 (n = 32), now above 0.25.

  With standard errors near 0.2, none of these is significantly below 0.25. A pre-registered test of this prediction would need data unseen on 2026-11-20, which T02's machinery can supply.
- **Where they sit:** the correlated pulsars are mid-distribution in −ν̇⟨Δt⟩. Among 51 pulsars with N ≥ 4 they sit at percentiles J1801 28, J1341 44, J1413 46 and J1048 58, with J0537 at 92. P2 expects the strongest r₊ at the top, and three of these are not near it.

**Follow-up:** whether these persist in glitches unseen on 2026-11-20 is pre-registered as T02 (`../prereg/T02-forward-persistence.md`). It counts unseen glitches, not only later ones, because these southern pulsars are uncatalogued after about 2017–18.

## Prior art
- **Partly known.** The full-sample statistics were published by Melatos et al. (2018), Fuentes et al. (2019) and Carlin & Melatos (2020; data up to 2018).
- **Not found:** a per-glitch test of P1 and P2 on post-2018 data.
- **The screen was weak.** It covered 47 OpenAlex citers by title, plus abstracts of those that looked relevant. That missed Zhu et al. (2025), whose title does not mention correlations. A full abstract screen of the citers in INSPIRE and ADS is still to do.

## Registry
**No confidence change** for C2466 or C2655 (vortex pinning and glitches). The registered tests cannot distinguish vortex avalanches from starquakes, and the forward-correlation evidence is exploratory.

## Revision (2026-11-21, after the F6 referee)
The first version (`f752941`) overstated four things:
- **The out-of-sample character:** it called the 2018 hints' disappearance an effect of new data. It was catalogue revision, including one Crab glitch.
- **The power of H1b,** which it did not quantify.
- **The forward correlations:** it called four pulsars three-sigma; two survive correction. It also used them to strengthen a registry claim.
- **The P2 reading:** "opposite ordering", and "r₊ measures x_cr".

It also reported the post-hoc gap check selectively, omitting the +0.37 (p = 0.03) variant, without code, and it missed the contrary Zhu et al. (2025). All of this is corrected above. The post-hoc analyses are now reproducible with `t01_glitches.py posthoc`, and both data snapshots are archived.

## Sources
- Melatos, Howitt & Fulgenzi (2018). "Size-waiting-time correlations in pulsar glitches". *ApJ* 863, 196. [arXiv:1809.03064](https://arxiv.org/abs/1809.03064)
- Basu et al. (2022). "The Jodrell Bank Glitch Catalogue: 106 new rotational glitches in 70 pulsars". *MNRAS* 510, 4049. [arXiv:2111.06835](https://arxiv.org/abs/2111.06835)
- Fuentes, Espinoza & Reisenegger (2019). "Glitch time series and size distributions in eight prolific pulsars". *A&A* 630, A115. [arXiv:1907.09887](https://arxiv.org/abs/1907.09887)
- Carlin & Melatos (2019). "Autocorrelations in pulsar glitch waiting times and sizes". *MNRAS* 488, 4890. [arXiv:1907.09143](https://arxiv.org/abs/1907.09143)
- Carlin & Melatos (2020). "Long-term statistics of pulsar glitches triggered by a Brownian stress accumulation process". *MNRAS* 494, 3383. [arXiv:2004.00168](https://arxiv.org/abs/2004.00168)
- Ho et al. (2020). "Return of the Big Glitcher: NICER timing and glitches of PSR J0537−6910". *MNRAS* 498, 4605. [doi:10.1093/mnras/staa2640](https://doi.org/10.1093/mnras/staa2640)
- Zhu et al. (2025). "Superfluid Angular Momentum Reservoir Effect in Pulsar Glitches and Crab Pulsar Glitch Time Prediction". *arXiv preprint*. [arXiv:2506.02925](https://arxiv.org/abs/2506.02925)
