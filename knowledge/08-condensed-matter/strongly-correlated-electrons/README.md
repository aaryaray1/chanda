---
title: Strongly correlated electrons
summary: Electrons whose interactions dominate — Mott insulators and the Hubbard model, Kondo physics and heavy fermions, quantum criticality, topological order and the numerics to tackle them.
query: strongly correlated electrons
arxiv: cond-mat.str-el
---
# Strongly correlated electrons

> Part of [Condensed Matter Physics](../README.md) · Key reviews: [papers.md](papers.md)

## Overview
When Coulomb repulsion $U$ rivals or exceeds the bandwidth $W$, band theory fails: half-filled systems become Mott insulators, magnetic impurities form many-body Kondo singlets, and electrons can fractionalize into excitations carrying fractions of their quantum numbers. Many of the deepest open problems in condensed matter — high-$T_c$ superconductivity, strange metals, spin liquids — live here, and they require non-perturbative numerical and field-theoretic tools.

## Topics
- [Hubbard model and Mott physics](hubbard-model-and-mott-physics/README.md) — the minimal model of correlated electrons.
- [Heavy fermions and Kondo physics](heavy-fermions-and-kondo-physics/README.md) — local moments screened by conduction electrons.
- [Quantum criticality and strange metals](quantum-criticality-and-strange-metals/README.md) — phase transitions at T = 0 and non-Fermi liquids.
- [Fractionalization and topological order](fractionalization-and-topological-order/README.md) — anyons, ground-state degeneracy, long-range entanglement.
- [Numerical many-body methods](numerical-many-body-methods/README.md) — DMFT, QMC, DMRG, tensor networks, exact diagonalization.

## Key equations
$$H_{\text{Hub}}=-t\sum_{\langle ij\rangle\sigma}(c^\dagger_{i\sigma}c_{j\sigma}+\text{h.c.})+U\sum_in_{i\uparrow}n_{i\downarrow},\qquad T_K\sim De^{-1/(J\rho)}$$

## Landmark papers
- Mott (1949). "The Basis of the Electron Theory of Metals, with Special Reference to the Transition Metals". *Proc. Phys. Soc. A* 62, 416. [doi:10.1088/0370-1298/62/7/303](https://doi.org/10.1088/0370-1298/62/7/303)
- Hubbard (1963). "Electron correlations in narrow energy bands". *Proc. R. Soc. A* 276, 238. [doi:10.1098/rspa.1963.0204](https://doi.org/10.1098/rspa.1963.0204)
- Kondo (1964). "Resistance Minimum in Dilute Magnetic Alloys". *Prog. Theor. Phys.* 32, 37. [doi:10.1143/PTP.32.37](https://doi.org/10.1143/PTP.32.37)
- Wilson (1975). "The renormalization group: Critical phenomena and the Kondo problem". *Rev. Mod. Phys.* 47, 773. [doi:10.1103/RevModPhys.47.773](https://doi.org/10.1103/RevModPhys.47.773)
- Laughlin (1983). "Anomalous Quantum Hall Effect: An Incompressible Quantum Fluid with Fractionally Charged Excitations". *Phys. Rev. Lett.* 50, 1395. [doi:10.1103/PhysRevLett.50.1395](https://doi.org/10.1103/PhysRevLett.50.1395)
- Wen (1990). "Topological orders in rigid states". *Int. J. Mod. Phys. B* 4, 239. [doi:10.1142/S0217979290000139](https://doi.org/10.1142/S0217979290000139)
- Georges, Kotliar, Krauth & Rozenberg (1996). "Dynamical mean-field theory of strongly correlated fermion systems and the limit of infinite dimensions". *Rev. Mod. Phys.* 68, 13. [doi:10.1103/RevModPhys.68.13](https://doi.org/10.1103/RevModPhys.68.13)
- Lee, Nagaosa & Wen (2006). "Doping a Mott insulator: Physics of high-temperature superconductivity". *Rev. Mod. Phys.* 78, 17. [arXiv:cond-mat/0410445](https://arxiv.org/abs/cond-mat/0410445)
- Sachdev & Keimer (2011). "Quantum criticality". *Physics Today* 64, 29. [arXiv:1102.4628](https://arxiv.org/abs/1102.4628)

## Open problems
- Ground-state phase diagram of the doped 2D Hubbard model (stripes vs. d-wave superconductivity).
- A theory of the strange metal with Planckian dissipation $\hbar/\tau\sim k_BT$.

## Connections
- [Optical lattices (quantum simulation)](../../04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation/README.md) · [Tensor networks](../../00-foundations/computational-physics/tensor-network-methods/README.md) · [Quantum field theory](../../06-particle-physics/quantum-field-theory/README.md)
