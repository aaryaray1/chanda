# T01 · Pulsar glitches: superfluid vortex avalanches or stress release?

**Track:** test an existing cross-branch claim (tier T). **Status:** F3 done; F4 pre-registered in `../prereg/T01-glitch-correlations.md`; F5 run, see `../results/T01-glitch-correlations.md`.
**Connections:** C2466 "Pulsar glitches as vortex pinning and creep" (07×08), C2655 "Vortex pinning and creep: flux lines vs pulsar glitches" (08×09), C2459/C2630 (crust band theory and entrainment).

## Claim
Glitches, sudden spin-ups of rotating neutron stars, are collective unpinning events of quantized neutron-superfluid vortices from the crust lattice. This is the physics of flux-line pinning and Anderson–Kim creep in type-II superconductors, moved to a neutron star. Two model families explain the statistics differently:

| Model | Waiting times | Sizes | Size vs the *next* waiting time |
|---|---|---|---|
| Scale-free avalanches (self-organized-criticality-like) | Poisson (exponential) | power law | uncorrelated |
| Stress release (reservoir) | quasi-periodic for big events | peaked or broad | positive correlation |

## What F3 (prior art) changed
The per-pulsar statistics first planned here are published:
- exponential waiting times and scale-free sizes: Melatos, Peralta & Wyithe (2008);
- size and waiting-time distributions with Monte Carlo tests in the eight most prolific pulsars: Fuentes, Espinoza & Reisenegger (2019);
- size–waiting-time correlations: Melatos, Howitt & Fulgenzi (2018).

The 2018 paper unifies the two model families: it treats glitches as a state-dependent Poisson process, in which threshold-triggered avalanches release stress. It ends with falsifiable predictions for data that did not yet exist. Of the 47 papers that cite it, none tests those predictions on post-2018 glitches. So the test was narrowed to them:
- **P1:** no pulsar shows a strong correlation between a glitch's size and the wait *before* it (r₋ ≤ 0.5);
- **P2:** the size–next-wait correlation r₊ rises with −ν̇⟨Δt⟩, the stress added between glitches.

The catalogue has grown from the paper's 482 glitches to about 737, and glitches after MJD 58370 (2018-09-09) are data the predictors did not have.

## Sources
- Melatos, Howitt & Fulgenzi (2018). "Size-waiting-time correlations in pulsar glitches". *ApJ* 863, 196. [arXiv:1809.03064](https://arxiv.org/abs/1809.03064)
- Melatos, Peralta & Wyithe (2008). "Avalanche dynamics of radio pulsar glitches". *ApJ* 672, 1103. [arXiv:0710.1021](https://arxiv.org/abs/0710.1021)
- Fuentes, Espinoza & Reisenegger (2019). "Glitch time series and size distributions in eight prolific pulsars". *A&A* 630, A115. [arXiv:1907.09887](https://arxiv.org/abs/1907.09887)
- Carlin & Melatos (2019). "Autocorrelations in pulsar glitch waiting times and sizes". *MNRAS* 488, 4890. [arXiv:1907.09143](https://arxiv.org/abs/1907.09143)
- Basu et al. (2022). "The Jodrell Bank Glitch Catalogue: 106 new rotational glitches in 70 pulsars". *MNRAS* 510, 4049. [arXiv:2111.06835](https://arxiv.org/abs/2111.06835)
- Liu et al. (2026). "Distinct Modes of Pulsar Glitch Activity Revealed by the Waiting-time–Amplitude Morphology". *ApJ* 1009, 120. [arXiv:2608.28523](https://arxiv.org/abs/2608.28523)

## Why it matters
- It tests whether a condensed-matter mechanism (threshold-triggered release of pinned quantized vortices) quantitatively explains a nuclear-astrophysics phenomenon, with public data.
- Either outcome updates the confidence of four registry connections.
