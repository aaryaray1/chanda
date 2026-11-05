---
title: Analytical mechanics
summary: Lagrangian and Hamiltonian reformulations of mechanics — generalized coordinates, constraints, phase space, canonical transformations and variational principles.
query: analytical mechanics; Lagrangian mechanics
---
# Analytical mechanics

> Part of [Classical Mechanics](../README.md) · Key reviews: [papers.md](papers.md)

## Overview
Analytical mechanics replaces vector forces with scalar functions (the Lagrangian and Hamiltonian) and a variational principle. Constraints are handled automatically, symmetries reveal conserved momenta, and phase-space geometry (symplectic structure, Liouville's theorem) provides the bridge to statistical mechanics and quantum mechanics.

## Topics
- [Lagrangian mechanics](lagrangian-mechanics/README.md) — Euler–Lagrange equations, constraints, cyclic coordinates.
- [Hamiltonian mechanics](hamiltonian-mechanics/README.md) — phase space, Hamilton's equations, Poisson brackets, Liouville.
- [Canonical transformations and Hamilton–Jacobi theory](canonical-transformations-and-hamilton-jacobi/README.md) — generating functions, action–angle variables.
- [Variational principles](variational-principles/README.md) — least action, Fermat, calculus of variations.

## Conceptual spine
1. Configuration space with generalized coordinates; action $S=\int L\,dt$.
2. $\delta S=0$ ⇒ Euler–Lagrange equations.
3. Legendre transform → Hamiltonian, phase space, symplectic flow.
4. Integrable systems admit action–angle variables; most systems are not integrable.

## Key equations
$$\frac{d}{dt}\frac{\partial L}{\partial\dot q_i}-\frac{\partial L}{\partial q_i}=0,\qquad \dot q_i=\frac{\partial H}{\partial p_i},\ \dot p_i=-\frac{\partial H}{\partial q_i},\qquad \frac{\partial S}{\partial t}+H\!\left(q,\frac{\partial S}{\partial q},t\right)=0$$

## Landmark papers
- Hamilton (1834). "On a General Method in Dynamics". *Phil. Trans. R. Soc.* 124, 247. [doi:10.1098/rstl.1834.0017](https://doi.org/10.1098/rstl.1834.0017)
- Hamilton (1835). "Second Essay on a General Method in Dynamics". *Phil. Trans. R. Soc.* 125, 95. [doi:10.1098/rstl.1835.0009](https://doi.org/10.1098/rstl.1835.0009)

## Open problems
- Geometric integrators and structure-preserving discretizations for constrained and dissipative systems.

## Connections
- [Path integrals](../../04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics/README.md) · [Ensembles (phase space)](../../03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions/README.md) · [Nonlinear dynamics](../nonlinear-dynamics-and-chaos/README.md)
