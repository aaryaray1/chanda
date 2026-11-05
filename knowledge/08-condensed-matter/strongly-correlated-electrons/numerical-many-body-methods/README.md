---
title: Numerical many-body methods
summary: Computational tools for correlated quantum matter — exact diagonalization, quantum Monte Carlo, DMRG and tensor networks, DMFT, and neural-network states.
query: dynamical mean-field theory; quantum Monte Carlo strongly correlated; DMRG
---
# Numerical many-body methods
> [Condensed Matter Physics](../../README.md) › [Strongly correlated electrons](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Exact diagonalization (Lanczos), determinant and auxiliary-field QMC, sign problem, DMRG and PEPS, dynamical mean-field theory and cluster extensions (DCA, CDMFT), DFT+DMFT for real materials, diagrammatic Monte Carlo, neural-network quantum states, cross-method benchmarks (Simons collaboration).

**Core ideas.**
- No single method works everywhere; agreement between independent methods is the gold standard.
- DMFT is exact in infinite dimensions and captures the Mott transition's local physics.
- The sign problem limits QMC for doped fermions and frustrated magnets.

**Key equations.**
$$G_{\text{loc}}(i\omega_n)=\sum_{\mathbf k}\frac{1}{i\omega_n+\mu-\epsilon_{\mathbf k}-\Sigma(i\omega_n)}\quad(\text{DMFT self-consistency})$$

**Landmark.** Georges et al. (1996) — see [subfield landmarks](../README.md).

**See also.** [Tensor network methods](../../../00-foundations/computational-physics/tensor-network-methods/README.md) · [Monte Carlo methods](../../../00-foundations/computational-physics/monte-carlo-methods/README.md)
