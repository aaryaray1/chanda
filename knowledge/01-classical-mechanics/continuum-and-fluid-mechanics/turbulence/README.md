---
title: Turbulence
summary: Chaotic, multiscale fluid motion — the energy cascade, Kolmogorov scaling, intermittency, wall turbulence and turbulence modelling.
query: turbulence; turbulent flow; energy cascade
---
# Turbulence
> [Classical Mechanics](../../README.md) › [Continuum and fluid mechanics](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Transition to turbulence (pipe flow, puffs and slugs), Richardson cascade, Kolmogorov 1941 scaling and the −5/3 spectrum, dissipation range, intermittency and anomalous scaling, 2D inverse cascade, wall turbulence and the log law, RANS and LES modelling, DNS, Lagrangian turbulence, ML closures.

**Core ideas.**
- Energy injected at large scales cascades to small scales and is dissipated at the Kolmogorov scale $\eta=(\nu^3/\epsilon)^{1/4}$.
- K41 predicts $E(k)=C\epsilon^{2/3}k^{-5/3}$; higher-order structure functions deviate (intermittency).
- In 2D, energy cascades to large scales — relevant for atmospheres and soap films.

**Key equations.**
$$E(k)=C_K\epsilon^{2/3}k^{-5/3},\qquad \frac{L}{\eta}\sim Re^{3/4},\qquad \frac{\bar u}{u_\tau}=\frac1\kappa\ln\frac{yu_\tau}{\nu}+B$$

**Landmark.** Kolmogorov (1941) — see [subfield landmarks](../README.md).

**See also.** [MHD turbulence](../../../10-plasma-physics/magnetohydrodynamics/mhd-turbulence/README.md) · [Deterministic chaos](../../nonlinear-dynamics-and-chaos/deterministic-chaos/README.md)
