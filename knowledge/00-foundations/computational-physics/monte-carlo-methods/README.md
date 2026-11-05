---
title: Monte Carlo methods
summary: Stochastic sampling for integrals and statistical systems — importance sampling, Metropolis, cluster algorithms, quantum Monte Carlo.
query: Monte Carlo method; Markov chain Monte Carlo; quantum Monte Carlo
---
# Monte Carlo methods
> [Foundations](../../README.md) › [Computational physics](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Random sampling and $N^{-1/2}$ errors, importance sampling, Metropolis–Hastings, detailed balance, autocorrelation and critical slowing down, Wolff/Swendsen–Wang clusters, parallel tempering, Hybrid Monte Carlo, variational and diffusion QMC, the sign problem.

**Core ideas.**
- High-dimensional integrals: Monte Carlo error is independent of dimension.
- A Markov chain obeying detailed balance with respect to $e^{-\beta E}$ samples the Boltzmann distribution.
- Near critical points, local updates slow down ($\tau\sim\xi^z$); cluster moves cure it for spin models.

**Key equations.**
$$P_{\text{acc}}(x\to x')=\min\!\left(1,e^{-\beta[E(x')-E(x)]}\right)$$

**Landmarks.** Metropolis et al. (1953); Duane et al. (1987) — see [subfield landmarks](../README.md).

**See also.** [Ising model](../../../03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/ising-model-and-lattice-models/README.md) · [Event generators](../../../06-particle-physics/collider-and-experimental-particle-physics/monte-carlo-event-generators/README.md)
