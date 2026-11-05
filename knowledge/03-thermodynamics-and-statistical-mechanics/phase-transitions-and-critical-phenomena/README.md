---
title: Phase transitions and critical phenomena
summary: How matter changes phase — order parameters, Ising and lattice models, mean-field and Landau theory, the renormalization group, universality and topological transitions.
query: phase transitions; critical phenomena
---
# Phase transitions and critical phenomena

> Part of [Thermodynamics and Statistical Mechanics](../README.md) · Key reviews: [papers.md](papers.md)

## Overview
At a continuous phase transition, correlations extend over all length scales and microscopic details become irrelevant: magnets, fluids and binary alloys share identical critical exponents (universality). The renormalization group explains why — systems flow to the same fixed points — and is one of the deepest ideas in physics, unifying statistical mechanics with quantum field theory.

## Topics
- [Ising model and lattice models](ising-model-and-lattice-models/README.md) — the paradigm of order–disorder transitions.
- [Mean-field and Landau theory](mean-field-and-landau-theory/README.md) — order-parameter expansions and their limits.
- [Renormalization group](renormalization-group/README.md) — coarse-graining, fixed points, relevant and irrelevant operators.
- [Critical exponents and universality](critical-exponents-and-universality/README.md) — scaling laws, universality classes.
- [Topological phase transitions (BKT)](topological-phase-transitions-bkt/README.md) — vortex unbinding in 2D.

## Conceptual spine
1. Order parameter vanishes in the disordered phase; symmetry determines its form.
2. First-order transitions have latent heat; continuous ones have diverging correlation length $\xi\sim|t|^{-\nu}$.
3. Mean field is exact above the upper critical dimension ($d_c=4$ for Ising).
4. RG: fixed points ↔ universality classes; exponents from eigenvalues of the linearized flow.

## Key equations
$$F_L=\int d^dx\left[\tfrac12(\nabla\phi)^2+\tfrac12r\phi^2+\tfrac{u}{4!}\phi^4\right],\qquad \alpha+2\beta+\gamma=2,\qquad \gamma=\nu(2-\eta),\qquad \nu d=2-\alpha$$

## Landmark papers
- Ising (1925). "Beitrag zur Theorie des Ferromagnetismus". *Z. Phys.* 31, 253. [doi:10.1007/BF02980577](https://doi.org/10.1007/BF02980577)
- Onsager (1944). "Crystal Statistics. I. A Two-Dimensional Model with an Order-Disorder Transition". *Phys. Rev.* 65, 117. [doi:10.1103/PhysRev.65.117](https://doi.org/10.1103/PhysRev.65.117)
- Kadanoff (1966). "Scaling laws for Ising models near Tc". *Physics* 2, 263. [doi:10.1103/PhysicsPhysiqueFizika.2.263](https://doi.org/10.1103/PhysicsPhysiqueFizika.2.263)
- Mermin & Wagner (1966). "Absence of Ferromagnetism or Antiferromagnetism in One- or Two-Dimensional Isotropic Heisenberg Models". *Phys. Rev. Lett.* 17, 1133. [doi:10.1103/PhysRevLett.17.1133](https://doi.org/10.1103/PhysRevLett.17.1133)
- Wilson (1971). "Renormalization Group and Critical Phenomena. I. Renormalization Group and the Kadanoff Scaling Picture". *Phys. Rev. B* 4, 3174. [doi:10.1103/PhysRevB.4.3174](https://doi.org/10.1103/PhysRevB.4.3174)
- Kosterlitz & Thouless (1973). "Ordering, metastability and phase transitions in two-dimensional systems". *J. Phys. C* 6, 1181. [doi:10.1088/0022-3719/6/7/010](https://doi.org/10.1088/0022-3719/6/7/010)

## Open problems
- Analytic 3D Ising exponents (known numerically to high precision via the bootstrap).
- Classification of quantum phase transitions beyond Landau (deconfined criticality).

## Connections
- [Renormalization in QFT](../../06-particle-physics/quantum-field-theory/renormalization-and-running-couplings/README.md) · [Conformal field theory](../../06-particle-physics/quantum-field-theory/conformal-field-theory/README.md) · [Quantum criticality](../../08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals/README.md)
