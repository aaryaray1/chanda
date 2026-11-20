# T03 results · The 2019 glitch-epoch forecasts

**Tier T** (published forecasts scored out-of-sample). **Correction (2026-11-21):** these were not prospective forecasts. All three glitches happened before the paper appeared (arXiv v1, 2019-10-12 = MJD 58768), in April, August and December 2018, but after the paper's data ended. The test is out-of-sample, not a test of a forecast of the future. T04 (`T04-glitch-forecast-scorecard.md`) scores these alongside the genuinely prospective forecasts. **Status:** all three forecasts pass. This is weak evidence for the model. Self-reviewed on 2026-11-20: two sentences of the reading were corrected (see `git log`).
- **Pre-registration:** `../prereg/T03-glitch-epoch-forecasts.md`, commit `883d299`.
- **Data:** the 2026-11-20 Jodrell Bank snapshot (SHA-256 `e811419f…`), the same one T01 used.

## Answer
Melatos & Drummond (2019) forecast the next glitch of three pulsars with a state-dependent Poisson (SDP) model. All three actual glitches fell within the forecasts' two-sigma bands. A homogeneous-Poisson (HP) baseline with the same average rate missed one of them badly: J0631+1036 stayed quiet for 7.2 years after a 394-day average wait, and HP gives z = +5.7. The SDP forecast was closer in two of the three. Three forecasts cannot rank the models (the paper says over 50 glitches per object are needed). They do show that the published uncertainties were honest.

| Pulsar | Last glitch in the paper's data (MJD) | Actual next glitch (MJD) | SDP forecast | SDP z | HP forecast | HP z | Closer |
|---|---|---|---|---|---|---|---|
| J1740−3015 | 57469 | 58241.0 | 57784 ± 257 | +1.78 | 57776.8 ± 307.8 | +1.51 | SDP, by 7 d |
| J0534+2200 (Crab) | 58237 | 58470.7 | 60713 ± 1935 | −1.16 | 58894.2 ± 657.2 | −0.64 | HP, by 1819 d |
| J0631+1036 | 55702 | 58341.7 | 57406 ± 1444 | +0.65 | 56096.0 ± 394.0 | **+5.70** | SDP, by 1310 d |

## Reading
- **The SDP forecast for J0631+1036 was made from data ending at MJD 55702, so it did not see the later silence.** It forecast a long wait anyway: 1704 ± 1444 days after the last glitch, against HP's 394 days. That is because the model's stress state after that glitch implied a low glitch rate. A memoryless process with the historical rate calls the observed 2640-day wait a 1-in-800 event (exp(−2640/394) ≈ 0.0012).
- **The model's forecasts are sharp only when the stress state is pinned down.** For the Crab, the SDP band of ±1935 days was too wide to be useful, and the plain average rate did much better.
- **J0631+1036's silence may be partly missing data.** The 2018 paper suspected unpublished glitches. If any were missed, the true next epoch came earlier than MJD 58342. That would improve the HP baseline's score, and could reverse the SDP-versus-HP comparison for this pulsar.

## Deviation
The pre-registration gives the J1740−3015 HP forecast as 57777.8. The correct value, (57469 − 47003)/34 + 57469, is 57776.8. This one-day slip changes no verdict.

## Sources
- Melatos & Drummond (2019). "Pulsar glitch activity as a state-dependent Poisson process: parameter estimation and epoch prediction". *ApJ* 885, 37. [arXiv:1910.05503](https://arxiv.org/abs/1910.05503)
- Basu et al. (2022). "The Jodrell Bank Glitch Catalogue: 106 new rotational glitches in 70 pulsars". *MNRAS* 510, 4049. [arXiv:2111.06835](https://arxiv.org/abs/2111.06835)
