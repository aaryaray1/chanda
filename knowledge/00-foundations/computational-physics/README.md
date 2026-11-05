---
title: Computational physics
summary: Numerical methods that solve physics problems beyond analytic reach — ODE/PDE solvers, Monte Carlo, molecular dynamics, tensor networks and machine learning.
query: computational physics; numerical simulation
arxiv: physics.comp-ph cond-mat.stat-mech
---
# Computational physics

> Part of [Foundations](../README.md) · Key reviews: [papers.md](papers.md)

## Overview
Simulation is the third pillar of physics alongside theory and experiment. The craft is choosing a method whose errors you understand: discretization error, statistical error, finite-size effects, and the sign problem. Every result needs a convergence test and a check against a known limit.

## Topics
- [Numerical methods for ODEs and PDEs](numerical-methods-for-odes-and-pdes/README.md) — integrators, finite differences/elements, spectral methods.
- [Monte Carlo methods](monte-carlo-methods/README.md) — importance sampling, Markov chains, quantum Monte Carlo.
- [Molecular dynamics](molecular-dynamics/README.md) — integrating Newton's equations for many particles.
- [Tensor network methods](tensor-network-methods/README.md) — DMRG, MPS, PEPS for quantum many-body systems.
- [Machine learning for physics](machine-learning-for-physics/README.md) — surrogates, PINNs, neural quantum states, discovery.

## Conceptual spine
1. Discretize → solve algebraic problem → estimate error → refine until converged.
2. Stochastic methods trade bias for variance; errors fall as $N^{-1/2}$.
3. Exploit structure (symplecticity, sparsity, low entanglement) to beat brute force.

## Key equations
$$\text{Euler: }y_{n+1}=y_n+hf(y_n)\ (\mathcal O(h)),\qquad \text{RK4: }\mathcal O(h^4),\qquad \sigma_{\bar A}=\sqrt{\frac{2\tau_{\text{int}}}{N}}\,\sigma_A$$

## Landmark papers
- Metropolis et al. (1953). "Equation of State Calculations by Fast Computing Machines". *J. Chem. Phys.* 21, 1087. [doi:10.1063/1.1699114](https://doi.org/10.1063/1.1699114)
- Alder & Wainwright (1957). "Phase Transition for a Hard Sphere System". *J. Chem. Phys.* 27, 1208. [doi:10.1063/1.1743957](https://doi.org/10.1063/1.1743957)
- Verlet (1967). "Computer 'Experiments' on Classical Fluids. I. Thermodynamical Properties of Lennard-Jones Molecules". *Phys. Rev.* 159, 98. [doi:10.1103/PhysRev.159.98](https://doi.org/10.1103/PhysRev.159.98)
- Duane et al. (1987). "Hybrid Monte Carlo". *Phys. Lett. B* 195, 216. [doi:10.1016/0370-2693(87)91197-X](https://doi.org/10.1016/0370-2693(87)91197-X)
- White (1992). "Density matrix formulation for quantum renormalization groups". *Phys. Rev. Lett.* 69, 2863. [doi:10.1103/PhysRevLett.69.2863](https://doi.org/10.1103/PhysRevLett.69.2863)
- Schollwöck (2011). "The density-matrix renormalization group in the age of matrix product states". *Ann. Phys.* 326, 96. [arXiv:1008.3477](https://arxiv.org/abs/1008.3477)
- Carleo et al. (2019). "Machine learning and the physical sciences". *Rev. Mod. Phys.* 91, 045002. [arXiv:1903.10563](https://arxiv.org/abs/1903.10563)

## Open problems
- The fermion sign problem (NP-hard in general).
- Trustworthy uncertainty quantification for ML surrogates in physics.

## Connections
- [Lattice field theory](../../06-particle-physics/quantum-field-theory/lattice-field-theory/README.md) · [Density functional theory](../../08-condensed-matter/crystals-and-electronic-structure/density-functional-theory/README.md) · [Numerical relativity](../../05-relativity-and-gravitation/general-relativity/numerical-relativity/README.md)
