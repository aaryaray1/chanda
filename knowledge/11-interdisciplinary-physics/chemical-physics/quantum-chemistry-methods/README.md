---
title: Quantum chemistry methods
summary: Computing molecular electronic structure — Hartree–Fock, configuration interaction, perturbation theory, coupled cluster, basis sets and quantum-computing approaches.
query: coupled cluster theory; Hartree-Fock; electron correlation methods
---
# Quantum chemistry methods
> [Interdisciplinary and Applied Physics](../../README.md) › [Chemical physics](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Hartree–Fock and Roothaan–Hall equations, Gaussian basis sets and basis-set extrapolation, electron correlation, MP2, CI and full CI, coupled cluster (CCSD, CCSD(T) "gold standard"), multireference methods (CASSCF, CASPT2), DFT in chemistry, explicitly correlated F12 methods, local correlation, quantum Monte Carlo, quantum algorithms (VQE, phase estimation) for chemistry.

**Core ideas.**
- Hartree–Fock gives ~99% of the energy; the missing correlation energy determines chemistry.
- CCSD(T) achieves ~1 kcal/mol accuracy for single-reference molecules at $\mathcal O(N^7)$ cost.
- Strong correlation (bond breaking, transition metals) needs multireference methods — a target for quantum computers.

**Key equations.**
$$|\Psi_{CC}\rangle=e^{\hat T}|\Phi_0\rangle,\ \hat T=\hat T_1+\hat T_2+\cdots;\qquad E_{\text{corr}}=E_{\text{exact}}-E_{\text{HF}}$$

**Landmarks.** Roothaan (1951); Čížek (1966); Raghavachari et al. (1989) — see [subfield landmarks](../README.md).

**See also.** [Approximation methods in QM](../../../04-quantum-physics/quantum-mechanics-core/approximation-methods/README.md) · [Ab initio nuclear theory](../../../07-nuclear-physics/nuclear-structure/ab-initio-nuclear-theory/README.md)
