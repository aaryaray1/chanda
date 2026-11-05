---
title: Nonlinear dynamics and chaos
summary: Dynamical systems beyond linearity — deterministic chaos, bifurcations, KAM theory, solitons, synchronization and pattern formation.
query: nonlinear dynamics; chaos theory
arxiv: nlin.CD nlin.PS nlin.SI nlin.AO
---
# Nonlinear dynamics and chaos

> Part of [Classical Mechanics](../README.md) · Key reviews: [papers.md](papers.md)

## Overview
Deterministic systems with as few as three variables can be unpredictable in practice because of exponential sensitivity to initial conditions. Nonlinear dynamics classifies how systems change behaviour as parameters vary (bifurcations), how order survives in Hamiltonian systems (KAM), how nonlinearity can stabilize waves (solitons), and how coupled units synchronize or form patterns.

## Topics
- [Deterministic chaos](deterministic-chaos/README.md) — Lyapunov exponents, strange attractors, predictability.
- [Bifurcations and routes to chaos](bifurcations-and-routes-to-chaos/README.md) — period doubling, Feigenbaum universality, intermittency.
- [KAM theory and Hamiltonian chaos](kam-theory-and-hamiltonian-chaos/README.md) — invariant tori, chaotic seas, Arnold diffusion.
- [Solitons and integrable systems](solitons-and-integrable-systems/README.md) — KdV, inverse scattering, Lax pairs.
- [Synchronization and pattern formation](synchronization-and-pattern-formation/README.md) — Kuramoto model, Turing patterns.

## Conceptual spine
1. Phase-space flows; fixed points and linear stability (eigenvalues of the Jacobian).
2. Bifurcations change the qualitative structure as parameters cross critical values.
3. Chaos: positive Lyapunov exponent, bounded attractor, fractal structure.
4. Dissipative (attractors) vs. conservative (KAM, mixed phase space) dynamics.

## Key equations
$$\dot x=\sigma(y-x),\ \dot y=x(\rho-z)-y,\ \dot z=xy-\beta z;\qquad x_{n+1}=rx_n(1-x_n);\qquad \lambda=\lim_{t\to\infty}\frac1t\ln\frac{|\delta\mathbf x(t)|}{|\delta\mathbf x_0|}$$

## Landmark papers
- Lorenz (1963). "Deterministic Nonperiodic Flow". *J. Atmos. Sci.* 20, 130. [doi:10.1175/1520-0469(1963)020<0130:DNF>2.0.CO;2](https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2)
- Hénon & Heiles (1964). "The applicability of the third integral of motion: Some numerical experiments". *Astron. J.* 69, 73. [doi:10.1086/109234](https://doi.org/10.1086/109234)
- Zabusky & Kruskal (1965). "Interaction of 'Solitons' in a Collisionless Plasma and the Recurrence of Initial States". *Phys. Rev. Lett.* 15, 240. [doi:10.1103/PhysRevLett.15.240](https://doi.org/10.1103/PhysRevLett.15.240)
- Gardner, Greene, Kruskal & Miura (1967). "Method for Solving the Korteweg-deVries Equation". *Phys. Rev. Lett.* 19, 1095. [doi:10.1103/PhysRevLett.19.1095](https://doi.org/10.1103/PhysRevLett.19.1095)
- May (1976). "Simple mathematical models with very complicated dynamics". *Nature* 261, 459. [doi:10.1038/261459a0](https://doi.org/10.1038/261459a0)
- Feigenbaum (1978). "Quantitative universality for a class of nonlinear transformations". *J. Stat. Phys.* 19, 25. [doi:10.1007/BF01020332](https://doi.org/10.1007/BF01020332)
- Ott, Grebogi & Yorke (1990). "Controlling chaos". *Phys. Rev. Lett.* 64, 1196. [doi:10.1103/PhysRevLett.64.1196](https://doi.org/10.1103/PhysRevLett.64.1196)
- Cross & Hohenberg (1993). "Pattern formation outside of equilibrium". *Rev. Mod. Phys.* 65, 851. [doi:10.1103/RevModPhys.65.851](https://doi.org/10.1103/RevModPhys.65.851)
- Strogatz (2000). "From Kuramoto to Crawford: exploring the onset of synchronization in populations of coupled oscillators". *Physica D* 143, 1. [doi:10.1016/S0167-2789(00)00094-4](https://doi.org/10.1016/S0167-2789(00)00094-4)

## Open problems
- Predictability limits of weather and climate; data-driven forecasting of chaotic systems.
- Arnold diffusion rates in realistic many-dimensional Hamiltonian systems.

## Connections
- [Quantum chaos](../../04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling/README.md) · [Turbulence](../continuum-and-fluid-mechanics/turbulence/README.md) · [Complex networks](../../03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/complex-networks/README.md)
