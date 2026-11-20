# Pre-registration T01 · Do pulsar glitches follow the 2018 size–waiting-time predictions?

**Registered:** 2026-11-20, before any glitch value was read. The commit containing this file and `../analysis/t01_glitches.py` timestamps the plan.
**Card:** `../cards/T01-pulsar-glitch-avalanches.md`. **Results:** `../results/T01-*.{md,json}` (written after the run).

## What was seen before registration
- **Jodrell Bank catalogue:** on 2026-11-20 it was downloaded three times:
  1. to check that it was reachable and count its table rows (758);
  2. to read its column header and title text, with digits masked;
  3. to show its row structure, also with digits masked.

  No glitch epoch or size was printed, and every copy was deleted afterwards.
- **ATNF Pulsar Catalogue (v2.9.0):** queried once, for the spin-down rate ν̇ of PSR J0537−6910, to test the query format.
- **Published results,** which are prior knowledge: Table 1 and Table 2 of the source paper (the values are in the analysis script), and the abstracts of the papers listed under prior art.

## The predictions under test
Source: Melatos, Howitt & Fulgenzi (2018). "Size-waiting-time correlations in pulsar glitches". *ApJ* 863, 196. [arXiv:1809.03064](https://arxiv.org/abs/1809.03064)

The paper models glitches as a state-dependent Poisson process: stress builds as the star spins down and is released in threshold-triggered avalanches. Its §5 states two predictions "for the future, when more data become available":
- **P1:** "no glitching pulsar will exhibit a strong s–Δt₋ correlation, either now or in the future". Its eq. A31 gives r₋ ≤ 0.5 for separable kernels, and r₋ ≲ 0.1 for typical parameters.
- **P2:** a high forward correlation r₊ goes with a high −ν̇⟨Δt⟩ (the stress added between glitches). The top half of its Table 2 (J0205+6449, J0537−6910, J1119−6127, J2229+6114) are "good r₊ targets". The authors exclude the Crab, a known misfit.

**Notation:**
- s = Δν/ν is the glitch size;
- Δt₊ is the wait to the next glitch, Δt₋ the wait since the previous one;
- r is the Pearson correlation and ρ the Spearman rank correlation.

**New data:** the paper used 482 glitches. Glitches with epoch after MJD 58370 (2018-09-09, its arXiv submission date) cannot have been in its data set.

## Prior art (F3), 2026-11-20
All 47 works that OpenAlex lists as citing the paper were screened by title. Those that analyse glitch statistics were read by abstract, and Liu et al. (2026) in full.
- **The same statistics were published before:**
  - Fuentes, Espinoza & Reisenegger (2019) computed r₊ for the 8 pulsars with ≥ 10 glitches, on data up to about 2019;
  - Carlin & Melatos (2019) studied autocorrelations;
  - Liu et al. (2026) classified 22 pulsars by the shape of their size–waiting-time distribution (349 glitches, Jodrell Bank cross-matched with ATNF). They do not compute per-pulsar r± or test the 2018 predictions.
- **Not found:** a test of P1 and P2 against the glitches recorded after 2018.
- **Verdict:** the statistics are known; testing P1 and P2 on post-prediction data is not found. A positive or negative outcome is a test of a published prediction on data the predictors did not have.

## Data and definitions (fixed)
- **Glitches:** the Jodrell Bank Glitch Catalogue (`gTable.html`), downloaded once by `t01_glitches.py fetch`, with its SHA-256 recorded. Cite Basu et al. (2022) as the catalogue requests.
- **Spin-down rates:** ATNF Pulsar Catalogue F1, fetched in the same step.
- **Fields used:** J-name, epoch (MJD) and Δν/ν.
  - An entry with a missing, non-numeric, upper-limit or non-positive Δν/ν keeps its epoch but has no size. Anti-glitches are handled this way.
  - Nothing else is excluded: no pulsar type, no observatory, no time span.
- **Pairs:** for glitch *i* with a size, the forward pair is (sᵢ, tᵢ₊₁ − tᵢ) and the backward pair is (sᵢ, tᵢ − tᵢ₋₁).
- **Pulsar size:** N is the number of a pulsar's glitches that have a size.
- **⟨Δt⟩** = (t_last − t_first)/(n_epochs − 1). ν̇ is ATNF F1. The predictor is X = log₁₀(−ν̇⟨Δt⟩/Hz).
- **Statistics:**
  - **p-values:** permutation p-values with 100,000 permutations; sizes are shuffled against waits within a pulsar, and across pulsars for H2. The seed is 20261120.
  - **Bound test:** the Fisher-z test of r₋ against 0.5.
  - **Combining pulsars:** Fisher's method.

## Tests and decision rules
| | Test | Sample | Rule |
|---|---|---|---|
| **Control** | J0537−6910 shows the known strong forward correlation | full | Must give ρ₊ ≥ 0.8 with p < 10⁻⁴. If it fails, the data or code are wrong, and H1 and H2 are not interpreted until that is explained. |
| **H1a** (P1, weak form) | No pulsar has a significant backward correlation | pulsars with N ≥ 10, full | Refuted if any pulsar's two-sided Spearman p < 0.0027/K. K is the number of pulsars tested (three sigma, Bonferroni). |
| **H1b** (P1, bound) | r₋ ≤ 0.5 in every pulsar | same | Refuted if any pulsar's one-sided Fisher-z p for r₋ > 0.5 is < 0.0027/K |
| **H2** (P2) | Across pulsars, r₊ rises with X | pulsars with N ≥ 8, full | Spearman(X, r₊). **Supported** if positive with one-sided p < 0.01. **Contradicted** if negative with one-sided p < 0.01. Otherwise **inconclusive**. |

**Secondary analyses** are reported, but none is a test by itself:
- H1 on new data only: backward pairs whose glitch is after MJD 58370, for pulsars with ≥ 6 such pairs, combined by Fisher's method;
- H2 with N ≥ 6;
- H2 on new forward pairs only, for pulsars with ≥ 6;
- H2 with ρ₊ in place of r₊;
- the r₊ values of the Table 2 targets, on the full data and on the new data;
- a replication of Table 1 on glitches up to MJD 58370, to check that the data and code agree with the paper.

## Known limitations
- **Missed glitches:** the catalogue misses small glitches, and observing gaps lengthen some waits.
- **Uneven coverage:** coverage differs between observatories and over the decades.
- **Small samples:** many pulsars have few glitches, so per-pulsar r₊ is noisy. That weakens H2 but does not bias its sign.
- **Assumptions of P2:** P2 assumes that the critical stress x_cr is similar from pulsar to pulsar. The authors call this unlikely, so a null H2 is weak evidence against the model.
- **Deviations:** any departure from this plan is reported, with its reason, in the results file.
