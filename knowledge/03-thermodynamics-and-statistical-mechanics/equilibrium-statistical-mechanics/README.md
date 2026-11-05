---
title: Equilibrium statistical mechanics
summary: Deriving thermodynamics from microscopic states — ensembles, partition functions, quantum statistics, entropy and information, exactly solvable models.
query: statistical mechanics; partition function
---
# Equilibrium statistical mechanics

> Part of [Thermodynamics and Statistical Mechanics](../README.md) · Key reviews: [papers.md](papers.md)

## Overview
Given a Hamiltonian, equilibrium statistical mechanics predicts every thermodynamic property via the partition function. Classical and quantum particles differ in how states are counted, which produces Bose condensation, Fermi pressure (holding up white dwarfs) and blackbody radiation. Information theory gives an alternative foundation: equilibrium is the maximum-entropy state consistent with what we know.

## Topics
- [Ensembles and partition functions](ensembles-and-partition-functions/README.md) — microcanonical, canonical, grand canonical.
- [Quantum statistics](quantum-statistics/README.md) — Bose–Einstein and Fermi–Dirac distributions, blackbody radiation, degenerate gases.
- [Entropy and information](entropy-and-information/README.md) — Boltzmann, Gibbs, Shannon entropy; Maxwell's demon; Landauer.
- [Exactly solvable models](exactly-solvable-models/README.md) — 2D Ising, Bethe ansatz, transfer matrices.

## Key equations
$$Z=\sum_ie^{-\beta E_i},\quad F=-k_BT\ln Z,\quad \langle E\rangle=-\frac{\partial\ln Z}{\partial\beta},\quad \langle n_k\rangle=\frac{1}{e^{\beta(\epsilon_k-\mu)}\mp1}$$

## Landmark papers
- Shannon (1948). "A Mathematical Theory of Communication". *Bell Syst. Tech. J.* 27, 379. [doi:10.1002/j.1538-7305.1948.tb01338.x](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x)
- Jaynes (1957). "Information Theory and Statistical Mechanics". *Phys. Rev.* 106, 620. [doi:10.1103/PhysRev.106.620](https://doi.org/10.1103/PhysRev.106.620)
- Landauer (1961). "Irreversibility and Heat Generation in the Computing Process". *IBM J. Res. Dev.* 5, 183. [doi:10.1147/rd.53.0183](https://doi.org/10.1147/rd.53.0183)
- Bérut et al. (2012). "Experimental verification of Landauer's principle linking information and thermodynamics". *Nature* 483, 187. [doi:10.1038/nature10872](https://doi.org/10.1038/nature10872)
- Bethe (1931). "Zur Theorie der Metalle". *Z. Phys.* 71, 205. [doi:10.1007/BF01341708](https://doi.org/10.1007/BF01341708)
- Lieb & Liniger (1963). "Exact Analysis of an Interacting Bose Gas. I. The General Solution and the Ground State". *Phys. Rev.* 130, 1605. [doi:10.1103/PhysRev.130.1605](https://doi.org/10.1103/PhysRev.130.1605)

## Open problems
- Foundations: why do isolated systems reach equilibrium? (Typicality, ETH.)
- Statistical mechanics of long-range interacting systems (gravity) with negative heat capacity.

## Connections
- [Thermalization and ETH](../../04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth/README.md) · [BEC](../../04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases/README.md) · [Compact objects](../../09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects/README.md)
