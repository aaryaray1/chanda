---
title: Deterministic chaos
summary: Sensitive dependence on initial conditions in deterministic systems — Lyapunov exponents, strange attractors and limits of prediction.
query: deterministic chaos; Lyapunov exponent; strange attractor
---
# Deterministic chaos
> [Classical Mechanics](../../README.md) › [Nonlinear dynamics](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Lorenz system, logistic map, double pendulum, Lyapunov spectra, strange attractors and fractal dimensions, Poincaré sections, symbolic dynamics, ergodicity and mixing, shadowing, time-series embedding (Takens), chaos control.

**Core ideas.**
- Chaos needs nonlinearity and at least three dimensions for continuous flows (one for maps).
- Errors grow like $e^{\lambda t}$, so the prediction horizon grows only logarithmically with initial precision.
- Strange attractors are fractal sets with zero volume but infinite length of trajectories.

**Key equations.**
$$t_{\text{pred}}\approx\frac{1}{\lambda_{\max}}\ln\frac{\Delta_{\text{tol}}}{\delta_0},\qquad D_{KY}=k+\frac{\sum_{i\le k}\lambda_i}{|\lambda_{k+1}|}$$

**Landmarks.** Lorenz (1963); Ott, Grebogi & Yorke (1990) — see [subfield landmarks](../README.md).

**See also.** [Quantum chaos](../../../04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling/README.md) · [Atmospheric dynamics](../../../11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics/README.md)
