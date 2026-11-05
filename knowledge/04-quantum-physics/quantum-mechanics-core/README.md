---
title: "Quantum mechanics: formalism and methods"
summary: The postulates, the standard solvable systems, angular momentum and spin, approximation methods, scattering theory, path integrals and geometric phases.
query: quantum mechanics
---
# Quantum mechanics: formalism and methods

> Part of [Quantum Physics](../README.md) · Key reviews: [papers.md](papers.md)

## Overview
The working toolkit of quantum mechanics: states and operators, time evolution, and the handful of exactly solvable models (harmonic oscillator, hydrogen, spin-½) from which almost everything else is built by approximation.

## Topics
- [Postulates and formalism](postulates-and-formalism/README.md) — Hilbert space, observables, Born rule, density matrices.
- [Exactly solvable systems](exactly-solvable-systems/README.md) — oscillator, hydrogen, wells and barriers.
- [Angular momentum and spin](angular-momentum-and-spin/README.md) — SU(2), addition of angular momenta, spin–orbit.
- [Approximation methods](approximation-methods/README.md) — perturbation theory, variational method, WKB, adiabatic theorem.
- [Scattering theory](scattering-theory/README.md) — partial waves, Born series, resonances.
- [Path integrals and semiclassics](path-integrals-and-semiclassics/README.md) — Feynman's formulation, stationary phase, tunnelling.
- [Geometric phases](geometric-phases/README.md) — Berry phase, Aharonov–Bohm effect.

## Conceptual spine
1. State $|\psi\rangle\in\mathcal H$; observables are Hermitian operators; outcomes are eigenvalues with probability $|\langle a|\psi\rangle|^2$.
2. Unitary evolution $i\hbar\,\partial_t|\psi\rangle=H|\psi\rangle$ between measurements.
3. Non-commuting observables obey uncertainty relations $\sigma_A\sigma_B\ge\frac12|\langle[A,B]\rangle|$.
4. Composite systems use tensor products — the origin of entanglement.

## Key equations
$$i\hbar\frac{\partial\psi}{\partial t}=\left[-\frac{\hbar^2}{2m}\nabla^2+V\right]\psi,\qquad [\hat x,\hat p]=i\hbar,\qquad \sigma_x\sigma_p\ge\frac{\hbar}{2}$$

## Landmark papers
- Heisenberg (1925). "Über quantentheoretische Umdeutung kinematischer und mechanischer Beziehungen". *Z. Phys.* 33, 879. [doi:10.1007/BF01328377](https://doi.org/10.1007/BF01328377)
- Schrödinger (1926). "Quantisierung als Eigenwertproblem". *Ann. Phys.* 384, 361. [doi:10.1002/andp.19263840404](https://doi.org/10.1002/andp.19263840404)
- Born (1926). "Zur Quantenmechanik der Stoßvorgänge". *Z. Phys.* 37, 863. [doi:10.1007/BF01397477](https://doi.org/10.1007/BF01397477)
- Dirac (1928). "The quantum theory of the electron". *Proc. R. Soc. A* 117, 610. [doi:10.1098/rspa.1928.0023](https://doi.org/10.1098/rspa.1928.0023)
- Feynman (1948). "Space-Time Approach to Non-Relativistic Quantum Mechanics". *Rev. Mod. Phys.* 20, 367. [doi:10.1103/RevModPhys.20.367](https://doi.org/10.1103/RevModPhys.20.367)
- Aharonov & Bohm (1959). "Significance of Electromagnetic Potentials in the Quantum Theory". *Phys. Rev.* 115, 485. [doi:10.1103/PhysRev.115.485](https://doi.org/10.1103/PhysRev.115.485)
- Berry (1984). "Quantal phase factors accompanying adiabatic changes". *Proc. R. Soc. A* 392, 45. [doi:10.1098/rspa.1984.0023](https://doi.org/10.1098/rspa.1984.0023)

## Open problems
- Efficient methods for strongly interacting many-particle systems (the exponential wall).
- Rigorous control of perturbation series (most are asymptotic, not convergent).

## Connections
- [Foundations](../foundations-of-quantum-mechanics/README.md) · [Linear algebra and Hilbert spaces](../../00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces/README.md) · [Quantum field theory](../../06-particle-physics/quantum-field-theory/README.md)
