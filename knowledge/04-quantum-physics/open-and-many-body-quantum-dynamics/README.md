---
title: Open and many-body quantum dynamics
summary: Quantum systems coupled to environments or with many interacting parts — master equations, quantum thermodynamics, thermalization, chaos, non-Hermitian and driven systems.
query: open quantum systems; quantum many-body dynamics
arxiv: quant-ph cond-mat.stat-mech cond-mat.quant-gas
---
# Open and many-body quantum dynamics

> Part of [Quantum Physics](../README.md) · Key reviews: [papers.md](papers.md)

## Overview
Real quantum systems leak into their environments, and large isolated systems behave thermally even though their evolution is unitary. This branch studies both: Markovian and non-Markovian open-system dynamics, the thermodynamics of quantum machines, how isolated systems thermalize (or fail to), quantum chaos and information scrambling, and the new phases that appear in periodically driven and non-Hermitian systems.

## Topics
- [Lindblad master equations](lindblad-master-equations/README.md) — Markovian open-system dynamics.
- [Quantum thermodynamics](quantum-thermodynamics/README.md) — heat, work and engines at the quantum scale.
- [Thermalization and ETH](thermalization-and-eth/README.md) — eigenstate thermalization, integrability, many-body localization.
- [Quantum chaos and scrambling](quantum-chaos-and-scrambling/README.md) — random matrices, OTOCs, the chaos bound.
- [Non-Hermitian physics](non-hermitian-physics/README.md) — PT symmetry, exceptional points, skin effect.
- [Floquet systems and time crystals](floquet-systems-and-time-crystals/README.md) — periodically driven phases.

## Conceptual spine
1. Trace out the bath → completely positive dynamics; under Born–Markov assumptions → Lindblad form.
2. Isolated systems: local observables thermalize if eigenstates are thermal (ETH); exceptions are integrable or localized systems.
3. Chaos is diagnosed by level statistics and OTOC growth.
4. Driving and dissipation are design tools, not just nuisances.

## Key equations
$$\dot\rho=-\frac{i}{\hbar}[H,\rho]+\sum_k\gamma_k\left(L_k\rho L_k^\dagger-\tfrac12\{L_k^\dagger L_k,\rho\}\right)$$

## Landmark papers
- Lindblad (1976). "On the generators of quantum dynamical semigroups". *Commun. Math. Phys.* 48, 119. [doi:10.1007/BF01608499](https://doi.org/10.1007/BF01608499)
- Gorini, Kossakowski & Sudarshan (1976). "Completely positive dynamical semigroups of N-level systems". *J. Math. Phys.* 17, 821. [doi:10.1063/1.522979](https://doi.org/10.1063/1.522979)
- Bohigas, Giannoni & Schmit (1984). "Characterization of Chaotic Quantum Spectra and Universality of Level Fluctuation Laws". *Phys. Rev. Lett.* 52, 1. [doi:10.1103/PhysRevLett.52.1](https://doi.org/10.1103/PhysRevLett.52.1)
- Deutsch (1991). "Quantum statistical mechanics in a closed system". *Phys. Rev. A* 43, 2046. [doi:10.1103/PhysRevA.43.2046](https://doi.org/10.1103/PhysRevA.43.2046)
- Srednicki (1994). "Chaos and quantum thermalization". *Phys. Rev. E* 50, 888. [arXiv:cond-mat/9403051](https://arxiv.org/abs/cond-mat/9403051)
- Rigol, Dunjko & Olshanii (2008). "Thermalization and its mechanism for generic isolated quantum systems". *Nature* 452, 854. [arXiv:0708.1324](https://arxiv.org/abs/0708.1324)
- Maldacena, Shenker & Stanford (2016). "A bound on chaos". *JHEP* 08, 106. [arXiv:1503.01409](https://arxiv.org/abs/1503.01409)
- Bender & Boettcher (1998). "Real Spectra in Non-Hermitian Hamiltonians Having PT Symmetry". *Phys. Rev. Lett.* 80, 5243. [arXiv:physics/9712001](https://arxiv.org/abs/physics/9712001)

## Open problems
- Is many-body localization stable in the thermodynamic limit?
- Thermodynamic costs of quantum computation and measurement.

## Connections
- [Non-equilibrium statistical mechanics](../../03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/README.md) · [Black-hole information](../../05-relativity-and-gravitation/black-holes/information-paradox/README.md) · [Decoherence](../foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical/README.md)
