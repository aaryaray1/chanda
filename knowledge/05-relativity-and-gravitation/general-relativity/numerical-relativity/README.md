---
title: Numerical relativity
summary: Solving Einstein's equations on supercomputers — 3+1 formulations, gauge choices, binary black-hole and neutron-star mergers, waveform catalogues.
query: numerical relativity; binary black hole simulation; BSSN
---
# Numerical relativity
> [Relativity and Gravitation](../../README.md) › [General relativity](../README.md) · Literature: [papers.md](papers.md)

**Scope.** ADM and BSSN/CCZ4 formulations, generalized harmonic gauge, moving-puncture and excision methods, constraint damping, adaptive mesh refinement, the 2005 breakthrough, GRMHD for neutron-star mergers and accretion, waveform catalogues (SXS), surrogate models, critical collapse (Choptuik scaling).

**Core ideas.**
- Split spacetime into space + time; evolve spatial metric and extrinsic curvature with constraint equations monitored.
- The 2005 breakthroughs (generalized harmonic and moving punctures) made binary-black-hole merger simulations routine.
- Simulations calibrate the waveform models used to analyse LIGO–Virgo data.

**Key equations.**
$$\partial_t\gamma_{ij}=-2\alpha K_{ij}+D_i\beta_j+D_j\beta_i,\qquad R+K^2-K_{ij}K^{ij}=16\pi\rho\ (\text{Hamiltonian constraint})$$

**Landmark.** Pretorius (2005) — see [subfield landmarks](../README.md).

**See also.** [Gravitational-wave waveforms](../../gravitational-waves/gravitational-wave-theory-and-waveforms/README.md) · [Numerical methods](../../../00-foundations/computational-physics/numerical-methods-for-odes-and-pdes/README.md)
