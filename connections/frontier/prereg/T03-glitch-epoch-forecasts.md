# Pre-registration T03 · Did the 2019 glitch-epoch forecasts come true?

**Registered:** 2026-11-20, before the post-2016 epochs of these three pulsars were inspected. T01 read the same catalogue snapshot, but only as per-pulsar correlation coefficients; no epochs of these pulsars were printed.

## The forecasts
Source: Melatos & Drummond (2019). "Pulsar glitch activity as a state-dependent Poisson process: parameter estimation and epoch prediction". *ApJ* 885, 37. [arXiv:1910.05503](https://arxiv.org/abs/1910.05503)

The paper fits a state-dependent Poisson (SDP) model to three Poisson-like glitchers. Its abstract predicts the epoch of the next glitch (one sigma). Its §5 footnote gives the last glitch in its data, T_N:

| Pulsar | N | T₁ (MJD) | T_N (MJD) | Forecast T_{N+1} (MJD) |
|---|---|---|---|---|
| J1740−3015 | 35 | 47003 | 57469 | 57784 ± 256.8 |
| J0534+2200 (Crab) | 28 | 40493 | 58237 | 60713 ± 1935 |
| J0631+1036 | 15 | 50186 | 55702 | 57406 ± 1444 |

T₁ comes from Melatos, Howitt & Fulgenzi (2018), Table 1, which uses the same samples.

## Scoring (fixed)
- **The actual T_{N+1}:** the first epoch in the 2026-11-20 Jodrell Bank snapshot (SHA-256 `e811419f…`) that falls more than 2 days after T_N.
- **Score:** z = (T_actual − T_forecast)/σ. A forecast **passes** if |z| ≤ 2, the criterion the paper applies to its own back-tests.
- **No later glitch catalogued:** the forecast **fails as overdue** if 2026-11-20 (MJD 61364) is past T_forecast + 2σ. Otherwise the result is **undetermined**.
- **Baseline, a homogeneous Poisson (HP) process with the paper's own sample rate:** forecast T_N + ⟨Δt⟩, with ⟨Δt⟩ = (T_N − T₁)/(N − 1) and σ = ⟨Δt⟩. This gives:
  - J1740−3015: 57777.8 ± 307.8;
  - Crab: 58894.2 ± 657.2;
  - J0631+1036: 56096.0 ± 394.0.
- **Head-to-head:** for each pulsar, record which model's forecast is closer to the actual epoch, and its |z|.

## Caveats
- **Three forecasts with wide uncertainties** cannot separate SDP from HP. The paper says over 50 glitches per object are needed for that. This scores the published forecasts; it does not test the model's mechanism.
- **Missing glitches:** a glitch absent from the catalogue may be missed or unpublished, not absent. That matters for J0631+1036, whose published sequence the 2018 paper already flagged as possibly incomplete.
