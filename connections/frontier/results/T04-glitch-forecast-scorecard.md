# T04 results · How good are published pulsar-glitch forecasts?

**Tier T** (published forecasts scored against a public catalogue; compilation). **Revised twice on 2026-11-21 after the referee (F6).** The second round checked every number and asked for text fixes: report the overdue forecasts in the Answer, and treat one of them as a confirmed miss. The first-round verdict was "needs revision". It found a missed failed forecast, double-counted scenarios, wrong prospective labels and two headlines that do not hold. Both headlines are withdrawn; they appear in the title of commit `b121af9`:
- "roughly calibrated": withdrawn. Coverage is low and the sample is too small to judge.
- "a naive renewal baseline beats the Vela forecasts": withdrawn. It rested on two cases, one decided by 22 days.

**Records:**
- **Pre-registration:** `../prereg/T04-glitch-forecast-scorecard.md`, commit `5b6f6a8`.
- **Forecasts with verbatim quotes:** `../data/t04/forecasts.json`. Entries marked `addendum` were added after the referee and are outside the registered pool.
- **Code:** `../analysis/t04_forecast_scorecard.py`. **Numbers:** `T04-results.json`, with two summaries: the registered pool as registered, and the full pool with one forecast per event.
- **Data:** the 2026-11-20 Jodrell Bank snapshot (SHA-256 `e811419f…`).

## Answer
Explicit next-glitch forecasts have been published since 2016 by four groups of methods:
- vortex creep: Akbal et al., Gügercinoğlu et al., Liu et al., and Grover et al.'s second forecast;
- the state-dependent Poisson model: Melatos & Drummond;
- glitch clustering: Zhu et al.;
- Bayesian inference from past intervals: Grover et al.'s main forecast.

**One forecast per event** (14 forecasts). The primary forecast is the paper's main scenario, the one without extra assumptions. Where a paper gives both a point forecast and a window for one event (Zhu et al. 2025), the point forecast counts, because it is the more informative statement. Six primary forecasts have a numeric outcome, and four more are overdue:

| Statistic | Result | If the stated σ were honest |
|---|---|---|
| Within 1σ | 2 of 6 | 4.1 expected; P(≤ 2) = 0.085 |
| Within 2σ | 5 of 6 | 5.7 expected; P(≤ 5) = 0.24 |
| Median z | +0.64 | 0 |
| Σz², post hoc | 18.9 on 6, p = 0.004 | χ² with 6 degrees of freedom |
| Σz² without the one 3.4σ miss, post hoc | 7.6 on 5, p = 0.18 | |
| Overdue beyond 2σ, no catalogued glitch | 4 of the 10 point forecasts past their horizon; one is confirmed by the paper's own data | — |
| Within 2σ, if all four overdue misses are real | 5 of 10 | 9.5 expected |

Coverage is low, and one forecast missed by 3.4σ. Six resolved forecasts are too few to judge calibration. A post-hoc tail test disfavours the stated σ, but it rests on that single miss.

The four overdue forecasts change the picture if they are real misses. Only one is certain: Liu et al.'s J1420−6048 forecast had already failed in the paper's own timing data. The other three may be glitches the catalogue lacks. Among the resolved outcomes there is no detectable early or late bias: the mean z is +0.01 only because the −3.36 miss offsets the positive ones. Counting the overdue forecasts, the misses are four late and one early.

**Sensitivity to the choice of primary.** If Zhu et al.'s 2025 window counts instead of their point forecast, 1 of 5 numeric forecasts lands within 1σ (P = 0.038).

**Forecasts made strictly before their outcome** are few:
- **Resolved:** two numeric ones, Gügercinoğlu et al.'s Vela forecast (z = +1.51) and Zhu et al.'s Crab forecast (z = +0.64).
- **Overdue:** two, Gügercinoğlu et al.'s J2111+4606 and J1023−5746 forecasts, with no catalogued glitch.
- **Windows:** Zhu et al.'s 2025 window came true for any glitch (chance 0.33), but not for a large one. Their January 2026 window for a major glitch failed.

**Against a naive baseline** (the pulsar's last large glitch plus its mean interval), the forecasts were closer in 3 of 6. Two of those wins are weak:
- J1740−3015 was won by 7 days out of about 460.
- The Crab's baseline centre was 4.2 years before Zhu et al. published. Conditioned on no glitch before publication, the baseline misses by −289 d and the forecast by −316 d (post hoc).

A post-hoc Gaussian log score, which also uses the stated σ, favours the forecast in 3 of 6 as well, but not the same three.

**The registered pool, scored as registered** (12 forecasts, all scenarios counted):
- 3 of 7 within 1σ (P = 0.15) and 6 of 7 within 2σ; mean z −0.06; forecast closer in 4 of 7.
- Prospective under the registered rule, with one day of slack: 2 of 4 within 1σ and 3 of 4 within 2σ. Under the strict rule: 1 of 2 and 2 of 2.
- Overdue: 2 (GU20b, GU22d).

## Scorecard
"Counted" says how each forecast enters the summaries. *Primary*: the one forecast per event. *Scenario*: an alternative for the same event, reported but not counted. *Addendum*: added after the referee.

| ID | Pulsar | Forecast (first arXiv version) | Published (MJD) | Next glitch (MJD) | Timing of the outcome | Result | Renewal baseline | Counted |
|---|---|---|---|---|---|---|---|---|
| AK17a | Vela | 58286 ± 164 | 57734.7 | 57734.5 | contemporaneous: v1 posted about 6 h after the glitch; the authors state the forecast predates it | **z = −3.36, outside 2σ** | closer (+161 d vs −552 d) | primary |
| AK17m | Vela | 58235 ± 433, Crab-like persistent-shift scenario | 57734.7 | 57734.5 | contemporaneous | z = −1.16, within 2σ | closer (+161 d vs −501 d) | scenario, addendum |
| AK17b | Vela | 57836 ± 201, large persistent-shift scenario | 57734.7 | 57734.5 | contemporaneous | z = −0.51, within 1σ | forecast closer | scenario |
| MD19a | J1740−3015 | 57784 ± 257 | 58768 | 58241.0 | out-of-sample: before publication, after the data | z = +1.78, within 2σ | forecast closer, by 7 d (457 vs 464) | primary |
| MD19b | Crab | 60713 ± 1935 | 58768 | 58470.7 | out-of-sample | z = −1.16, within 2σ | baseline closer (−424 d vs −2242 d) | primary |
| MD19c | J0631+1036 | 57406 ± 1444 | 58768 | 58341.7 | out-of-sample | z = +0.65, within 1σ | forecast closer | primary |
| GU20a | Vela | 59284.6 ± 88 | 59183 | 59417.2 | prospective | z = +1.51, within 2σ | baseline closer by 22 d (−111 vs +133) | primary |
| GU20b | J2111+4606 | 59702 ± 311 | 59183 | none catalogued | — | registered verdict: overdue beyond 2σ, or not catalogued | — | primary |
| GU20c | J2229+6114 | lower bound: after 59014 | 59183 | 59262.0 | the bound had passed 169 d before publication | true, but uninformative | HP chance the bound holds: 0.58 from the catalogue anchor, 0.87 given the paper's quiet data to 58865, 1 given publication | primary |
| GU22d | J1023−5746 | 59685 ± 97 (v2) | 59611 | none catalogued | — | registered verdict: overdue beyond 2σ, or not catalogued | — | primary |
| ZH25b | Crab | 60504 ± 577 | 60829 | 60872.9 (Δν/ν = 2.3×10⁻⁹) | prospective, but 71% of the forecast's probability had elapsed at publication | z = +0.64, within 1σ. Major reading: pending until 61658 | forecast closer (+369 d vs +1558 d); the baseline centre was 4.2 yr before publication | primary |
| ZH25a | Crab | window: before 61081 | 60829 | 60872.9 | prospective | true for any glitch (HP chance 0.33); false under the major reading | — | scenario: the window edge is ZH25b's upper 1σ edge |
| ZH26 | Crab | window for a *major* glitch: 61057–61283 (Jan–Aug 2026) | 61057 | none | prospective | **false** (window passed, none catalogued; the Crab is timed daily) | — | primary, addendum |
| LI24a | J1028−5819 | 62794 ± 269 | 60549 | none yet | prospective | pending | — | primary, addendum |
| LI24b | J1420−6048 | 59378 ± 16 | 60549 | none | centre passed 1171 d before publication | **overdue beyond 2σ, confirmed**: the paper's own post-glitch timing solution runs to 59453 with no glitch, z ≥ +4.7 | — | primary, addendum |
| LI24c | J1709−4429 | 60025 ± 26 (Table 4; the text gives 1861 d, not 1850 d) | 60549 | none catalogued | centre passed 524 d before publication | registered verdict: overdue, or not catalogued | — | primary, addendum |
| GR25 | Vela | 61377.7, 68% interval 61249–61506 (Bayesian, from past intervals) | 60828 | none yet | prospective | **pending** | 61437 ± 373 | primary |
| GR25vc | Vela | vortex creep: t₀ = 2287 (+160/−480) d after the anchor, so 62717; window 61952–63482 (±3τ_nl) | 60828 | none yet | prospective | pending | — | scenario, addendum |
| GU20e | J1023−5746 | 58750 ± 5, from G6 | 59183 | 58823.0 | postdiction: the same sentence names G7 | z = +14.6 | — | not counted |

## Notes
- **Self-reported scores measure something different.**
  - Gügercinoğlu et al. (2022, v2) report the 2021 Vela glitch as 45 days after their published window. That is correct for the window they published, which ended at MJD 59373. Measured from the central value, the glitch came 133 days late, z = +1.5.
  - Akbal et al. v1 report the December 2016 glitch as 103 days before their large persistent-shift scenario, within its 1σ. The difference is 101.5 days by the catalogue epoch. Their primary forecast missed by 3.4σ. Version 3 replaced the v1 forecasts.
  - An independent scorer should use first-version forecasts and central values.
- **Windows and bounds carry little information unless they are narrow.** Zhu et al.'s 2025 window would have caught a glitch by chance with probability 0.33. GU20c's bound had already passed when it was published.
- **The withdrawn forecast.** Zhu et al. withdrew arXiv:2601.12130 on 2026-06-18, five of the window's seven and a half months in, with no Crab glitch catalogued. The stated reason is administrative: it duplicated arXiv:2506.02925 and should have been posted as its revision. That revision, also of 2026-06-18, does not restate the January forecast. It calls its new size extrapolations "heuristic rather than predictive".
- **Catalogue blind spots.** No glitch after the anchor is catalogued for GU20b, GU22d and LI24c. Whether one occurred is unknown. LI24b is different: the source's own data rule out a glitch near its forecast date. J2111+4606 and J1023−5746 are timed mainly by Fermi-LAT, and the catalogue covers southern pulsars thinly after about 2018 (see T02). The registered verdict, *overdue*, stands, with that caveat. The first version of these results called these forecasts "unresolved, not failed", which was an undeclared change in their favour.
- **The Melatos & Drummond data.** Their last Crab glitch, MJD 58237, shows the sample ran to at least that date. If it was frozen at one date for all three pulsars, 96% of MD19a's forecast probability had passed by then with no J1740−3015 glitch in the sample. A forecast centred before the end of its own data shows that the forecast does not condition on the quiet time since the last glitch.
- **The baselines.** HP and renewal baselines share a centre, so "closer" cannot tell them apart. For an exponential wait, the median (μ ln 2) minimises the absolute error, not the mean, so "closer" handicaps HP.
- **Open forecasts.**
  - GR25: the 68% interval is decided at MJD 61506 (2027-04-11) if no glitch comes first. The registered horizon for *overdue* is 61634. The renewal baseline's centre is 60 days later than the forecast's, so the outcome will barely separate them.
  - GR25vc: its window opens at MJD 61952 (2028-06-30).
  - LI24a: MJD 62794 ± 269 (October 2030).
  - ZH25b under the major reading: pending until MJD 61658 (2027-09-10).
  - Re-score with `t04_forecast_scorecard.py run --catalogue <fresh gTable.html> --snapshot-mjd <MJD>`.

## Deviations
1. **J2229+6114's anchor** is dated MJD 58396(2) in the paper and 58424 in the catalogue (Basu et al. 2022: 58424(6)). The registered 2-day matching rule counted that same glitch as the outcome. The anchor is matched by identity instead: the size and the paper's v2 note leave no doubt it is the same event. The outcome is the next large glitch, at MJD 59262.
2. **Pool additions after the results were read** (addendum; the registered summary excludes them):
   - **ZH26.** It was the second hit for the registered phrase "next glitch". I skipped it because it had been withdrawn. That broke the rule "every explicit forecast found".
   - **AK17m.** Akbal et al. v1 gives three scenarios, and the table had two.
   - **LI24a–c**, from Liu et al. (2024), Table 4. They give "tth" from the last glitch, the same form that admitted GU22d. The paper was fetched one minute after the registration commit and was not declared.
   - **GR25vc**, the vortex-creep forecast in Grover et al. (2025).
   - **GU20e**, listed for completeness and not counted. It is a postdiction, as are the model-versus-observed interval comparisons for earlier glitches in the same papers, and the 2016-to-2019 Vela interval in arXiv:2003.08724.
3. **Counting.** The registered summary counts every scenario as a separate forecast, but the scenarios for one glitch are mutually exclusive. The revised summary counts one forecast per event, the paper's primary.
4. **Prospective label.** The registered code allowed one day of slack, which labelled AK17 prospective. Its v1 was posted about six hours *after* the glitch. The revised summary uses a strict definition: the outcome came after publication.
5. **AK17 anchor.** The registration described AK17 as phrased from the publication date. The paper anchors on "the last observed glitch", in 2014 (MJD 56922; 58286 − 1364 = 57836 − 914 = 56922). The catalogue lists that glitch at Δν/ν = 0.4×10⁻⁹, below the large-glitch class, so the registered baseline still anchors on the 2013 glitch and is unchanged at +161 d. Anchoring at the small 2014 glitch would give −205 d. No verdict changes.
6. **Method label.** GR25 was listed under vortex creep. It is a Bayesian estimate from past intervals.
7. **Post-hoc statistics.** Σz² and the Gaussian log score were added at the referee's request. They are labelled post hoc wherever they appear.
8. **Anchor slack.** The registered code added two days of slack after the anchor unless `after_mjd` equalled the publication date minus one. The revised code applies the slack unless the forecast is phrased from the publication date. No outcome changes.
9. **Confirmed misses** (second round, post hoc). A point forecast with no catalogued outcome is marked *confirmed overdue* when the source's own data show no glitch past centre + 2σ. This applies only to LI24b. It also reports a lower bound on z.
10. **Prospective counts.** The summaries report both the registered rule, with one day of slack, and the strict rule.

## Prior art
- **arXiv:** phrase searches on 2026-11-21 ("next glitch", "glitch time prediction", "predicting the starquakes" and others) found no outcome scorecard of glitch forecasts. Ho et al. (2020) compare stated precisions only. Zhu et al.'s revision self-scores its own forecast.
- **INSPIRE:** the titles and abstracts of all citers were screened: 39 of Akbal et al., 7 of Melatos & Drummond, 36 of Gügercinoğlu et al., 5 of Grover et al., 10 of Liu et al., and none of Zhu et al. None scores published forecasts against outcomes.
- **Not searched:** OpenAlex (it returned "503 Service Unavailable" on 2026-11-21), Semantic Scholar (rate-limited) and ADS. Verdict: *not found* in the sources searched.

## Sources
- Akbal et al. (2017). "Nonlinear interglitch dynamics, the braking index of the Vela pulsar and the time to the next glitch". *MNRAS* 469, 4183. [arXiv:1612.03805](https://arxiv.org/abs/1612.03805)
- Melatos & Drummond (2019). "Pulsar glitch activity as a state-dependent Poisson process: parameter estimation and epoch prediction". *ApJ* 885, 37. [arXiv:1910.05503](https://arxiv.org/abs/1910.05503)
- Gügercinoğlu et al. (2022). "Glitches in four gamma-ray pulsars and inferences on the neutron star structure". *MNRAS* 511, 425. [arXiv:2011.14788](https://arxiv.org/abs/2011.14788)
- Liu et al. (2024). "A multi-band study of pulsar glitches with Fermi-LAT and Parkes". *arXiv preprint*. [arXiv:2408.15022](https://arxiv.org/abs/2408.15022)
- Zhu et al. (2025). "Superfluid Angular Momentum Reservoir Effect in Pulsar Glitches and Crab Pulsar Glitch Time Prediction". *arXiv preprint*. [arXiv:2506.02925](https://arxiv.org/abs/2506.02925)
  - The forecasts are quoted from v1 (2025-06-03; Zhu & Zheng), then titled *Normal Distribution of Crab Pulsar Glitch Activity from a Glitch Cluster Perspective*. The current title is that of v2 (2026-06-18).
- Zhu et al. (2026). "Exploring Superfluid Angular Momentum Reservoir Effect on Pulsar Glitches and Forecasting Next Glitches of the Crab Pulsar". *arXiv preprint*, withdrawn 2026-06-18 as a duplicate of arXiv:2506.02925. [arXiv:2601.12130](https://arxiv.org/abs/2601.12130)
- Grover et al. (2026). "Post-glitch Recovery and the Neutron Star Structure: The Vela Pulsar". *PASA*. [arXiv:2506.02100](https://arxiv.org/abs/2506.02100) · [doi:10.1017/pasa.2026.10155](https://doi.org/10.1017/pasa.2026.10155)
- Basu et al. (2022). "The Jodrell Bank Glitch Catalogue: 106 new rotational glitches in 70 pulsars". *MNRAS* 510, 4049. [arXiv:2111.06835](https://arxiv.org/abs/2111.06835)
