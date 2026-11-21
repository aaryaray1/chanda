# Pre-registration V1 · Do vortex-creep predictions of the time to the next glitch track the observed intervals?

**Registered:** 2026-11-21, before the full data extraction. The analysis code is written after the extraction and implements exactly the statistics below.

## Question
Fits of the vortex-creep model to post-glitch recovery give a theoretical time to the next glitch, t_th (in some papers t₀, the time at which the nonlinear creep regions recouple). Papers report it next to the observed interval t_obs and describe the agreement as "qualitative", "good" or "excellent", one pulsar at a time. Nobody appears to have pooled the pairs.

**What V1 asks.** Across all published pairs, does t_th carry information about the interval *beyond the pulsar's typical interglitch time*? Every model gets the scale right, because J0537−6910 glitches about every 100 days and Vela about every 1000. The physics claim is that the recovery after each glitch sets when the *next* one comes. That claim predicts that t_th tracks which intervals are long and which are short.

## Inclusion (fixed)
- **What counts:** every pair of (t_th or t₀, t_obs) for the *same* glitch, reported as a vortex-creep prediction for the time to the next glitch. Only pairs where the paper states t_obs, or where t_obs follows from glitch epochs the paper lists, are included. Predictions with no observed next glitch are excluded; T04 scored those.
- **Papers found by the search of 2026-11-21:**
  - arXiv search: "vortex creep time to the next glitch", "vortex creep glitch prediction", "vortex creep post-glitch recovery", "time to the next glitch".
  - INSPIRE: abstracts mentioning "vortex creep", since 2015.
  - Candidates:
    - Akbal et al. 2017, arXiv:1612.03805 (Vela);
    - Gügercinoğlu & Alpar 2020, arXiv:2003.08724 (Vela 2016);
    - Gügercinoğlu et al. 2020/2022, arXiv:2011.14788 (Vela, J1023−5746, J2111+4606, J2229+6114);
    - Akbal et al. 2021, arXiv:2106.03341 (J0537−6910);
    - Liu et al. 2024, arXiv:2408.15022 (J1028−5819, J1420−6048, J1509−5850, J1709−4429, J1718−3825);
    - Zhou et al. 2024, arXiv:2408.09204 (J1522−5735);
    - Grover et al. 2025, arXiv:2506.02100 (Vela);
    - Liu et al. 2025, arXiv:2512.04972 (J1718−3718);
    - Wang et al. 2026, arXiv:2608.19555 (J1637−4642);
    - Zhou et al. 2022, arXiv:2205.08296 (J0738−4042).
  - Papers with no pairs are listed as screened.
- **Version:** the latest arXiv version of each paper, because these are model fits rather than forecasts.
- **One pair per glitch (primary):** where several papers give t_th for the same glitch, the most recent paper's value counts. The earliest paper's value is a sensitivity run.

## Statistics (fixed)
For pulsar p with N_p ≥ 3 included pairs, let m_p be the geometric mean of its t_obs. The pair's normalised values are x = ln(t_th / m_p) and y = ln(t_obs / m_p).

- **H_V1, tracking.** The pooled Spearman correlation between x and y over all pairs is positive, with a one-sided permutation p < 0.05. The permutation shuffles t_th within each pulsar, 20 000 times, seed 20261125.
  - This is the primary test: it asks whether t_th predicts the *deviation* of an interval from that pulsar's typical one.
- **H_V2, skill against a baseline.** For each pair, compare the model error e_m = |ln(t_th/t_obs)| with the baseline error e_b = |ln(t̄/t_obs)|, where t̄ is the geometric mean of the pulsar's *other* t_obs (leave one out).
  - *Supported* if e_m < e_b in more than half the pairs, by a one-sided sign test with p < 0.05.
  - The medians of e_m and e_b are reported.
- **Pulsars with fewer than 3 pairs** are reported but enter only H_V2. Their m_p is too poorly defined for H_V1.

## What was already seen
While building T04 and its referee fixes, I read a handful of pairs:
- J1023−5746 G1–G6, from arXiv:2011.14788v1: t_th = 1110, 620, 1102, 484 and 548 d;
- Vela: 984, 1862, 781 and 769 d;
- J1709−4429 in Liu et al. 2024: 1680 and 1861 d;
- Grover et al. 2025: t₀ = 2287.1 and 469.11 d.

I checked several against their t_obs in the papers' own words ("excellent agreement", "qualitative agreement"). No pooled statistic has been computed.

## Limitations
- **Possible leakage.** The recovery fits use data up to the next glitch, so t_th may be partly constrained by t_obs, especially when the recovery is extrapolated. Pairs flagged by the paper as extrapolated or degenerate (for example zero degrees of freedom) are marked, and a sensitivity run drops them.
- **One school.** These papers come from one modelling school. A pooled positive result is evidence for the model's internal consistency on these data, not an independent forecast test. That was T04.
