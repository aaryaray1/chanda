---
title: Ab initio nuclear theory
summary: Solving the nuclear many-body problem from realistic forces — no-core shell model, coupled cluster, IMSRG, quantum Monte Carlo and lattice EFT.
query: ab initio nuclear structure; coupled-cluster nuclei; no-core shell model
---
# Ab initio nuclear theory
> [Nuclear Physics](../../README.md) › [Nuclear structure](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Green's function Monte Carlo and AFDMC, no-core shell model, coupled-cluster theory, in-medium similarity renormalization group (IMSRG), self-consistent Green's functions, nuclear lattice EFT, similarity RG softening of interactions, emulators and Bayesian uncertainty quantification, reach to ²⁰⁸Pb.

**Core ideas.**
- Exact methods scale exponentially; polynomially scaling methods (CC, IMSRG) extended reach from light to heavy nuclei.
- Softened (SRG-evolved) interactions improve convergence but induce many-body forces.
- Uncertainty quantification has become central: predictions come with theory error bars.

**Key equations.**
$$H=\sum_i\frac{p_i^2}{2m}+\sum_{i<j}V_{ij}+\sum_{i<j<k}V_{ijk},\qquad \frac{dH_s}{ds}=[\eta_s,H_s]\ (\text{SRG/IMSRG})$$

**See also.** [Quantum chemistry methods (coupled cluster)](../../../11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods/README.md) · [Monte Carlo methods](../../../00-foundations/computational-physics/monte-carlo-methods/README.md)
