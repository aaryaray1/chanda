# T04 results · How good are published pulsar-glitch forecasts?

**Tier T** (published forecasts scored against a public catalogue; compilation). **Status:**
- 9 forecasts resolved;
- 2 unresolved, because the catalogue does not cover those pulsars;
- 1 still open (Vela, until MJD 61506, 2027-04-11).

**Records:**
- **Pre-registration:** `../prereg/T04-glitch-forecast-scorecard.md`, commit `5b6f6a8`.
- **Forecasts with verbatim quotes:** `../data/t04/forecasts.json`.
- **Code:** `../analysis/t04_forecast_scorecard.py`. **Numbers:** `T04-results.json`.
- **Data:** the 2026-11-20 Jodrell Bank snapshot.

## Answer
Twelve explicit next-glitch forecasts were published between 2016 and 2025, from three modelling schools:
- vortex creep: Akbal et al., Gügercinoğlu et al., Grover et al.;
- the state-dependent Poisson model: Melatos & Drummond;
- glitch clustering: Zhu et al.

**Calibration.** Of the 7 numeric forecasts that can be scored:
- 3 landed within their stated 1σ, against 4.8 expected;
- 6 within 2σ, against 6.7 expected;
- the mean z is −0.06, so there is no systematic early or late bias.

That is consistent with honest uncertainties at this sample size: the binomial probability of ≤ 3 of 7 within 1σ is 0.15 (0.085 if each paper's primary forecast is counted alone).

**Against a naive baseline.** The forecasts beat a renewal baseline (last glitch + mean interval) in 4 of 7. For Vela, the most-studied glitcher, the baseline beat both vortex-creep forecasts made before the glitch they forecast. Glitch-model forecasting has not yet shown an advantage over the pulsar's own average rhythm where that rhythm is regular.

## Scorecard
| ID | Pulsar | Forecast (first arXiv version) | Published (MJD) | Next glitch (MJD) | Prospective? | Result | Renewal baseline |
|---|---|---|---|---|---|---|---|
| AK17a | Vela | 58286 ± 164, primary | 57734 | 57734.5 | yes (same day) | **z = −3.36, outside 2σ** | closer (+161 d vs −552 d) |
| AK17b | Vela | 57836 ± 201, the authors' alternative | 57734 | 57734.5 | yes | z = −0.51, within 1σ | forecast closer |
| MD19a | J1740−3015 | 57784 ± 257 | 58768 | 58241.0 | no (out-of-sample) | z = +1.78, within 2σ | forecast closer, by 7 d |
| MD19b | Crab | 60713 ± 1935 | 58768 | 58470.7 | no (out-of-sample) | z = −1.16, within 2σ | baseline closer |
| MD19c | J0631+1036 | 57406 ± 1444 | 58768 | 58341.7 | no (out-of-sample) | z = +0.65, within 1σ | forecast closer |
| GU20a | Vela | 59284.6 ± 88 | 59183 | 59417.2 | yes | z = +1.51, within 2σ | baseline closer (−111 d vs +133 d) |
| GU20b | J2111+4606 | 59702 ± 311 | 59183 | none catalogued | — | unresolved: the catalogue lists only the 2 glitches in the forecasting paper | — |
| GU20c | J2229+6114 | lower bound: after 59014 | 59183 | 59262.0 | yes | true | HP chance of the bound holding: 0.58 |
| GU22d | J1023−5746 | 59685 ± 97 (v2) | 59611 | none catalogued | — | unresolved: the catalogue stops at the anchor glitch | — |
| ZH25a | Crab | window: before 61081 | 60829 | 60872.9 | yes | true | HP chance of a glitch in the window: 0.33 |
| ZH25b | Crab | 60504 ± 577 | 60829 | 60872.9 | yes | z = +0.64, within 1σ | forecast closer |
| GR25 | Vela | 61377.7, 68% interval 61249–61506 | 60828 | none yet | — | **pending:** the window is open | renewal baseline: 61437 ± 373 |

**Scope.**
- **Prospective:** forecasts whose glitch came after publication. Their numeric results are within 1σ 2 of 4 times and within 2σ 3 of 4 times. The miss is Akbal et al.'s primary forecast, submitted the day Vela glitched; their own alternative scenario was within 1σ.
- **Out-of-sample only:** the three Melatos & Drummond forecasts. Their glitches occurred before publication but after the paper's data ended (see the T03 correction).

## Notes
- **Self-reported versus independent scores.**
  - Gügercinoğlu et al. (2022, v2) describe their Vela forecast as off by "45 days". That is the distance from the edge of the ±88-day band. The glitch came 133 days after the central forecast, at z = +1.5.
  - Akbal et al. v1 reported the December 2016 glitch as arriving "103 days early, well within the 1σ" of their *alternative* scenario. Their primary forecast missed by 3.4σ. Version 3 replaced both forecasts.
  - An independent scorer should use first-version forecasts and central values.
- **Window and bound forecasts carry little information unless they are narrow.** Zhu et al.'s Crab window and Gügercinoğlu et al.'s J2229+6114 bound both came true, but chance alone gave them 33% and 58%.
- **Catalogue blind spots.** Two γ-ray-timed pulsars cannot be scored: their post-2020 glitches are not in the catalogue, and no later glitch paper was found on arXiv. Their verdict is unresolved, not failed.
- **The open forecast.** Grover et al.'s Vela window runs from 2026-07-28 to 2027-04-11. Score it with `t04_forecast_scorecard.py run --catalogue <fresh gTable.html> --snapshot-mjd <MJD>` after MJD 61506. The renewal baseline puts its central date 60 days later (61437 ± 373), so the outcome will barely separate the two.

## Deviation
J2229+6114's anchor glitch is dated MJD 58396(2) in the paper and 58424 in the catalogue (Basu et al. 2022: 58424(6)). The registered 2-day matching rule counted that same glitch as the outcome. The fix matches the anchor by identity: the size and the paper's own v2 note leave no doubt it is the same event. The outcome is now the next large glitch, at MJD 59262.

## Sources
- Akbal et al. (2017). "Nonlinear interglitch dynamics, the braking index of the Vela pulsar and the time to the next glitch". *MNRAS* 469, 4183. [arXiv:1612.03805](https://arxiv.org/abs/1612.03805)
- Melatos & Drummond (2019). "Pulsar glitch activity as a state-dependent Poisson process: parameter estimation and epoch prediction". *ApJ* 885, 37. [arXiv:1910.05503](https://arxiv.org/abs/1910.05503)
- Gügercinoğlu et al. (2022). "Glitches in four gamma-ray pulsars and inferences on the neutron star structure". *MNRAS* 511, 425. [arXiv:2011.14788](https://arxiv.org/abs/2011.14788)
- Zhu et al. (2025). "Superfluid Angular Momentum Reservoir Effect in Pulsar Glitches and Crab Pulsar Glitch Time Prediction". *arXiv preprint*. [arXiv:2506.02925](https://arxiv.org/abs/2506.02925)
- Grover et al. (2025). "Post-glitch Recovery and the Neutron Star Structure: The Vela Pulsar". *arXiv preprint*. [arXiv:2506.02100](https://arxiv.org/abs/2506.02100)
- Basu et al. (2022). "The Jodrell Bank Glitch Catalogue: 106 new rotational glitches in 70 pulsars". *MNRAS* 510, 4049. [arXiv:2111.06835](https://arxiv.org/abs/2111.06835)
