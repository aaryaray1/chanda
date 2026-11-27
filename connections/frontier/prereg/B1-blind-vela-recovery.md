# Pre-registration B1 · Can Vela's early post-glitch recovery forecast its next glitch? A blind test of the vortex-creep relation

**Registered:** 2026-11-27, before any LAT photon was downloaded. The analysis code is written and checked afterwards, and implements exactly the rules below. Checks that cannot depend on the outcome are allowed before scoring: pulse detection in each window, and ν(t) continuity between glitches.

## Why
V1 found that published vortex-creep times to the next glitch t_th track the observed intervals in-sample: within-pulsar ρ = +0.66, and better than the pulsar's own mean in 25 of 34. But those fits used timing data through the next glitch. The one clean forecast made beforehand did worse than the baseline. B1 removes the leakage: the recovery is measured **only from data well before the next glitch**, and the next glitch is predicted from it.

## Model (fixed)
This is the "triangle" interglitch model of Akbal et al. (2017, their Model 1), the simplest vortex-creep form, also used by Gügercinoğlu & Alpar (2020).
- After the exponential transients, the spin-down rate recovers linearly: ν̇(t) = ν̇_post + ν̈_ig (t − t_g), where t_g is the glitch epoch.
- The next glitch is due when ν̇ has recovered to its pre-glitch value ν̇_pre:
  **t₀ = (ν̇_pre − ν̇_post) / ν̈_ig.**
- If ν̈_ig ≤ 0, the model predicts no recovery, and the interval counts as a model failure.

## Data (fixed)
- **Photons:** Fermi-LAT photons within 1° of Vela (RA 08ʰ35ᵐ20.61149ˢ, Dec −45°10′34.8751″, from the 3PC timing model), energies 100 MeV–300 GeV. The cuts are zenith angle < 90° and the event classes the LAT data server returns as "Photon". They come with the matching spacecraft (FT2) files.
- **Time windows**, one query each:
  - Five Fermi-era Vela glitches with an observed successor, at catalogue epochs MJD 55408.8, 56556.0, 57734.5, 58515.6 and 59417.2.
  - Window for each: [t_g − 160 d, t_g + 410 d].
  - **No photon later than t_g + 410 d is used.** The shortest interval is 782 d, so every prediction is made from data ending more than a year before the next glitch.
- **Barycentring**, written for this test with no new packages:
  - Earth's position relative to the solar-system barycentre: JPL Horizons, daily, interpolated.
  - Spacecraft position: FT2, relative to the geocentre.
  - Roemer delay toward Vela, plus the dominant annual TT→TDB term (1.657 ms sin g). Shapiro delay (< 0.1 ms) is neglected.

## Measurement (fixed)
- **ν(t):** for each 14-day window, the barycentric spin frequency is the value maximising the H-test over a frequency grid. ν̇ inside the window is fixed at −1.5487×10⁻¹¹ Hz s⁻¹ (3PC timing model, `J0835-4510_LAT_PKSTZR.par`), and the reference epoch is the window's midpoint. The frequency grid is centred on that model's F0 and F1 plus the catalogue's glitch steps, searched ±5×10⁻⁵ Hz.
- **ν̇_pre:** a quadratic fit to ν(t) over [t_g − 150 d, t_g − 7 d], differentiated at t_g.
- **ν̇_post and ν̈_ig:** a quadratic fit to ν(t) over [t_g + 100 d, t_g + 400 d]. Its linear coefficient extrapolated to t_g gives ν̇_post, and twice its quadratic coefficient gives ν̈_ig.
  - The +100 d start follows Akbal et al. (2017), who fit from 100 d after each glitch, when the exponentials have relaxed.
- **Prediction:** t_pred = t_g + t₀.
- **Outcome:** the next catalogued Vela glitch with Δν/ν ≥ 10⁻⁷, giving t_obs = t_{g+1} − t_g: 1147, 1178, 782, 902 and 1013 d.

## Statistics and decision (fixed)
For each interval, compare the model error e_m = |ln(t₀ / t_obs)| with the baseline error e_b = |ln(t̄ / t_obs)|. Here t̄ is the geometric mean of all *earlier* Vela large-glitch intervals in the catalogue.

| Verdict | Condition |
|---|---|
| **Blind skill supported** | the model beats the baseline in at least 4 of 5 intervals **and** the median e_m < 0.10 |
| **Not supported** | the model beats the baseline in at most 2 of 5 |
| **Inconclusive** | otherwise |

Also reported, without a decision rule: the five blind t₀ next to the published in-sample t_th for the same intervals:
- Gügercinoğlu et al. 2022: 984, 1862, 781 and 769 d;
- Grover et al. 2026: 774.0, 921.6 and 469.1 d.

**Declared sensitivity runs:**
- the post-glitch fit window [60, 400] d and [100, 300] d;
- a 28-day ν window;
- photons above 300 MeV only.

## What is already known
- The five glitch epochs and the intervals, from the catalogue.
- The published t_th values (V1).
- No LAT photon or spin-frequency measurement for these intervals has been inspected.

## Limitations
- **Five intervals give little power.** The decision rule is coarse on purpose.
- **Model form.** The +100 d start and the linear recovery are the simplest published form. Grover et al. fit extra exponentials (τ up to about 300 d), which can bias ν̈ from early data. That is a known risk, and the sensitivity runs show how much it matters.
- **Timing noise.** Vela's timing noise and the approximate barycentring add frequency errors. The barycentring errors are annual and small for ν̇: a 5 ms Roemer error gives about 10⁻¹⁵ Hz s⁻¹, against glitch steps Δν̇ of order 10⁻¹³.
