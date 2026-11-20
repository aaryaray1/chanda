# T01 results · The 2018 glitch predictions, tested on today's catalogue

**Tier T** (pre-registered test on public data), with prior-art verdict *not found* for this test. **Status:** P1 survives · P2 inconclusive. The referee check (F6) has not been run yet.
- **Pre-registration:** `../prereg/T01-glitch-correlations.md`, committed as `bf6476f` on 2026-11-20 23:15 CET, before any glitch value was read.
- **Code:** `../analysis/t01_glitches.py`. **Numbers:** `T01-results.json`.
- **Data, fetched 2026-11-20 22:15 UTC:**
  - Jodrell Bank Glitch Catalogue, SHA-256 `e811419f…aabeb4`: 736 glitches (733 with a size) in 225 pulsars, 105 of them after MJD 58370;
  - ATNF Pulsar Catalogue v2.9.0, for F1.

## Answer
Melatos, Howitt & Fulgenzi (2018) made two predictions for future data:
- **P1** (no pulsar shows a strong correlation between glitch size and the wait *before* it) **survives**. None of the 10 pulsars with ≥ 10 glitches has a significant backward correlation, and none exceeds the theoretical bound r₋ ≤ 0.5. The two 2018 hints of one have weakened: the Vela pulsar's r₋ fell from 0.60 to 0.43, and the Crab's ρ₋ from 0.46 to 0.20.
- **P2** (the size–next-wait correlation r₊ rises with −ν̇⟨Δt⟩, the stress added between glitches) is **not supported, and not contradicted**. The across-pulsar trend is −0.32 (14 pulsars, p = 0.13) and stays within ±0.3 in every variant.

Strong forward correlations now appear in pulsars across the whole −ν̇⟨Δt⟩ range, not only at its top.

## Pre-registered results
| Test | Result | Verdict |
|---|---|---|
| **Control:** J0537−6910 forward correlation | ρ₊ = 0.931, n = 67, p = 1×10⁻⁵ | pass |
| **H1a:** no significant backward correlation (10 pulsars, per-pulsar α = 2.7×10⁻⁴) | smallest two-sided p = 0.20 (Vela) | survives |
| **H1b:** r₋ ≤ 0.5 | largest r₋ = 0.43 (Vela), p(r₋ > 0.5) = 0.66 | survives |
| **H2:** Spearman(log₁₀ −ν̇⟨Δt⟩, r₊), N ≥ 8 | −0.319, 14 pulsars, one-sided p₊ = 0.87, p₋ = 0.13 | inconclusive |

**Secondary analyses:**
- **H2 variants:** with N ≥ 6, −0.021 (30 pulsars); with ρ₊ in place of r₊, −0.029 (N ≥ 8) and +0.171 (N ≥ 6). All are inconclusive.
- **New data only:** one pulsar has ≥ 6 backward pairs after the cutoff: J0537−6910, timed by NICER, with ρ₋ = −0.17 (n = 20, p = 0.48). The forward correlation persists there (r₊ = 0.92 on 19 new pairs), as Ho et al. (2020) also found. No other pulsar has enough post-2018 glitches for a per-pulsar test.
- **Table 2 targets** (r₊ on all data): J0205+6449 0.91 (8 pairs), J2229+6114 0.33 (9), J1119−6127 0.90 (3). The "low" targets have 3–6 pairs, with r₊ from −0.21 to 0.80. These samples are still too small to rank.
- **Replication of Table 1** (glitches up to MJD 58370):
  - **matches:** J1740−3015 and J1801−2304, to within 0.04;
  - **differs where the catalogue has been revised:** J1341−6220 now lists 33 glitches before the cutoff against the paper's 23, and the Crab and Vela each list one more. Those revisions alone lower the 2018 backward hints: on pre-cutoff data the Vela r₋ is 0.37 and the Crab ρ₋ 0.27.

## Deviations from the plan
1. **Parser fix.** The catalogue's J-name column omits the leading "J". The registered parser therefore read only 5 glitches, and the control failed as designed. The fix changes only how rows are recognised (commit after `bf6476f`). No analysis choice changed.
2. **Pearson r is fragile to observing gaps (not a deviation; reported here).** One J0537−6910 wait of 2,264 days spans the gap between RXTE (to 2011) and NICER (from 2017). It drags that pulsar's Pearson r₊ from 0.94 to 0.25, while its Spearman ρ₊ stays at 0.93.
   - **Post-hoc check:** drop waits longer than 5× the pulsar's median. H2 then gives −0.05 (N ≥ 8), +0.17 (N ≥ 6), and with ρ₊ +0.01 and +0.28 (p = 0.08). Excluding the Crab, the authors' stated misfit, gives +0.19 and +0.25.
   - **H1 is unchanged.** The largest backward signal is the Crab's ρ₋ = 0.38 (p = 0.05), well short of the corrected threshold.

## Exploratory (not pre-registered; to be confirmed on future data)
Forward correlations (size against the wait that follows), significant at the single-test three-sigma level (p < 0.0027):

| Pulsar | ρ₊ | Glitches N | p | Earlier status |
|---|---|---|---|---|
| J0537−6910 | 0.93 | 68 | 1×10⁻⁵ | known |
| J1341−6220 | 0.62 | 33 | 8×10⁻⁵ | "arguably" emerging in 2018, at p = 4.8×10⁻³ with N = 23 |
| J1413−6141 | 0.82 | 14 | 4.5×10⁻⁴ | — |
| J1801−2304 | 0.71 | 15 | 2.5×10⁻³ | known |

J1048−5832 follows, with ρ₊ = 0.76 and p = 0.004.

In 2018 only two pulsars reached this level. J1341−6220, J1413−6141 and J1048−5832 sit in the middle and low end of the −ν̇⟨Δt⟩ range, which is the opposite of P2's ordering, unless their critical stress is small.

Fuentes et al. (2019) already reported significant positive forward coefficients in some prolific pulsars, so this is a strengthening, not a discovery. It is the natural pre-registered follow-up: test whether the forward correlations of J1341−6220, J1413−6141 and J1048−5832 persist in glitches after 2026-11-20.

## What it means
- **The model passes one test and fails to show the other.** The state-dependent Poisson framework passes its sharpest qualitative prediction: backward correlations stay weak as data accumulate. Its ranking prediction is not borne out. That is what one expects if the critical stress x_cr, set by the pinning force or crust strength, varies between pulsars, a possibility the authors flagged.
- **That variation can be used.** If x_cr varies, each pulsar's r₊ measures its own x_cr, which is the "turn the prediction around" programme of the paper's §5.
- **Registry connections:** this test cannot tell vortex avalanches from starquakes, because the framework covers both. C2466 and C2655 (vortex pinning, creep and glitches) keep their confidence. The evidence that glitches release stress past a threshold, rather than occurring at random, gets stronger: forward correlations, which are a sign of stored stress, are now significant in four pulsars.

## Sources
- Melatos, Howitt & Fulgenzi (2018). "Size-waiting-time correlations in pulsar glitches". *ApJ* 863, 196. [arXiv:1809.03064](https://arxiv.org/abs/1809.03064)
- Basu et al. (2022). "The Jodrell Bank Glitch Catalogue: 106 new rotational glitches in 70 pulsars". *MNRAS* 510, 4049. [arXiv:2111.06835](https://arxiv.org/abs/2111.06835)
- Fuentes, Espinoza & Reisenegger (2019). "Glitch time series and size distributions in eight prolific pulsars". *A&A* 630, A115. [arXiv:1907.09887](https://arxiv.org/abs/1907.09887)
- Ho et al. (2020). "Return of the Big Glitcher: NICER timing and glitches of PSR J0537−6910". *MNRAS* 498, 4605. [doi:10.1093/mnras/staa2640](https://doi.org/10.1093/mnras/staa2640)
