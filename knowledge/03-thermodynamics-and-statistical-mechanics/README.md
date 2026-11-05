---
title: Thermodynamics and Statistical Mechanics
summary: Heat, work and entropy; how macroscopic behaviour emerges from microscopic statistics; phase transitions and critical phenomena; non-equilibrium and complex systems.
arxiv: cond-mat.stat-mech
source: openalex
agent: statistical-physicist
---
# Thermodynamics and Statistical Mechanics

> **Specialist:** `statistical-physicist` · **arXiv:** cond-mat.stat-mech, cond-mat.dis-nn, physics.soc-ph · **Literature source:** OpenAlex + arXiv

## What this field studies
Thermodynamics gives universal laws for energy, heat and entropy without assuming anything about atoms. Statistical mechanics derives those laws from microscopic dynamics by counting states: $S=k_B\ln W$, and equilibrium probabilities $\propto e^{-E/k_BT}$. Its deepest results concern collective behaviour — phase transitions, universality and the renormalization group — and its frontier is far from equilibrium: driven, living, disordered and learning systems.

## Branch map
| Branch | What it covers |
|---|---|
| [Classical thermodynamics](classical-thermodynamics/README.md) | The four laws, potentials and Maxwell relations, heat engines, phase equilibria |
| [Equilibrium statistical mechanics](equilibrium-statistical-mechanics/README.md) | Ensembles, quantum statistics, entropy and information, exactly solvable models |
| [Phase transitions and critical phenomena](phase-transitions-and-critical-phenomena/README.md) | Ising models, Landau theory, renormalization group, universality, BKT |
| [Non-equilibrium statistical mechanics](non-equilibrium-statistical-mechanics/README.md) | Kinetic theory, linear response, Langevin/Fokker–Planck, fluctuation theorems, driven systems |
| [Disordered and complex systems](disordered-and-complex-systems/README.md) | Spin glasses, localization, percolation, networks, statistical physics of learning |

## Conventions used in this branch
- $\beta=1/k_BT$; $Z=\sum e^{-\beta E}$; free energy $F=-k_BT\ln Z$.
- Thermodynamic sign convention: $dU=\delta Q-\delta W$ with $W$ work done *by* the system (physics); chemistry often uses work done *on* the system — state which.
- Critical exponents $\alpha,\beta,\gamma,\delta,\nu,\eta$ with $t=(T-T_c)/T_c$.

## Historical spine
1824 Carnot · 1840s Joule, energy conservation · 1850–65 Clausius, entropy · 1859–77 Maxwell–Boltzmann kinetic theory, $S=k\ln W$ · 1902 Gibbs ensembles · 1905 Einstein on Brownian motion · 1925 Ising · 1931 Onsager reciprocity · 1944 Onsager solves the 2D Ising model · 1948 Shannon entropy · 1957 Jaynes; Kubo response theory · 1958 Anderson localization · 1961 Landauer principle · 1966 Kadanoff scaling · 1971 Wilson renormalization group · 1973 KT transition · 1979 Parisi replica symmetry breaking · 1997 Jarzynski equality · 2021 Nobel (Parisi) · 2024 Nobel (Hopfield, Hinton).

## Canonical textbooks
- Schroeder, *An Introduction to Thermal Physics*; Kittel & Kroemer, *Thermal Physics* — undergraduate.
- Callen, *Thermodynamics and an Introduction to Thermostatistics* — axiomatic thermodynamics.
- Pathria & Beale, *Statistical Mechanics*; Huang, *Statistical Mechanics*; Kardar, *Statistical Physics of Particles* / *of Fields*.
- Goldenfeld, *Lectures on Phase Transitions and the Renormalization Group*; Cardy, *Scaling and Renormalization in Statistical Physics*.
- Van Kampen, *Stochastic Processes in Physics and Chemistry*; Peliti & Pigolotti, *Stochastic Thermodynamics*.

## Live frontiers
- Stochastic thermodynamics of molecular machines and information engines; thermodynamic uncertainty relations.
- Active matter and non-reciprocal interactions.
- Statistical mechanics of deep learning: why overparameterized networks generalize.

## How the specialist works here
Identify the ensemble that matches the physical constraints, compute $Z$ (or a free energy) before anything else, use symmetry and dimensionality to anticipate phase behaviour, check extensivity and the classical/high-temperature limits, and for dynamics ask whether detailed balance holds.
