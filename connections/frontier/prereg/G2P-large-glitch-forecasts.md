# Registration G2-P · Forecasts of the next large glitch, and a Vela head-to-head

**Registered:** 2026-11-21. The numbers are in `../results/G2P-large-glitch-forecasts.json`, from `../analysis/g2p_large_forecasts.py`, which runs on the 2026-11-20 Jodrell Bank snapshot. No outcome after the snapshot was known when this was committed.

## Forecasts
For each of the 7 pulsars in G2's large class (Δν/ν ≥ 10⁻⁷, at least 8 large glitches), the file gives the time of the next large glitch.
- **Model:** the one with the best G2 backtest log score: M3 for J0537−6910, J1413−6141 and J1740−3015; M1 for J1420−6048 and J2229+6114; M0 for Vela and J1341−6220. All three models' forecasts are also stored.
- **Quantiles:** 5, 16, 25, 50, 75, 84 and 95%, as MJD, both unconditional and conditional on no large glitch before MJD 61364.
- **Evaluation:** once a fresh catalogue shows the next large glitch, score its PIT under the conditional forecast, or under the unconditional one if a large glitch is catalogued between the last one used here and the snapshot. Evaluate as a set once at least 4 of the 7 have resolved, or on 2028-11-20.

## Vela head-to-head (resolves by 2027-04-11)
**The outcome:** a Vela glitch with Δν/ν ≥ 10⁻⁷ and an epoch after MJD 61364 (2026-11-20) and no later than MJD 61506 (2027-04-11). Vela is timed daily, and its glitches are announced within days, so the outcome will be known by mid-April 2027.

| Forecaster | P(outcome) |
|---|---|
| Grover et al. (2025): their 68% interval 61249–61506 around 61377.7, read as a split normal | **0.71** |
| Empirical renewal: Vela's own past large waits (4 of the 13 that exceeded the 934 days already elapsed ended within 1076 days) | **0.31** |
| G2 models M0, M1 and M3 (log-normal widened by the 1994 doublet) | **0.13, 0.14, 0.13** |

- **Score:** the log probability each forecaster gave the observed outcome.
  - A glitch in the window favours Grover et al.: −0.35 against −1.18 empirical and −2.0 for the models.
  - No glitch favours the models: −0.14 against −0.37 empirical and −1.23 for Grover et al.
- **Reading:** a Vela glitch inside the window would be evidence that its physics-based timing carries information our statistical models miss.
- **Caveat:** Grover et al.'s forecast is statistical too (Bayesian, from past intervals; see T04), so this compares two statistical readings of the same history.
