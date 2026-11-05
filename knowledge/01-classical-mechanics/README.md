---
title: Classical Mechanics
summary: The motion of particles, rigid bodies and continua under forces — Newtonian and analytical mechanics, oscillations and waves, nonlinear dynamics and chaos, fluids and elasticity.
arxiv: physics.class-ph nlin.CD physics.flu-dyn
source: openalex
agent: classical-physicist
---
# Classical Mechanics

> **Specialist:** `classical-physicist` · **arXiv:** physics.class-ph, nlin.CD, nlin.PS, physics.flu-dyn · **Literature source:** OpenAlex + arXiv

## What this field studies
Classical mechanics describes systems where quantum effects are negligible ($S\gg\hbar$) and speeds are small compared with light. Its three formulations — Newtonian (forces), Lagrangian (action and generalized coordinates) and Hamiltonian (phase space) — are equivalent but suit different problems, and the latter two are the templates for quantum mechanics and field theory. The field is far from closed: chaos, turbulence and pattern formation remain active research frontiers.

## Branch map
| Branch | What it covers |
|---|---|
| [Newtonian mechanics](newtonian-mechanics/README.md) | Newton's laws, conservation laws, central forces and orbits, non-inertial frames, few-body problems |
| [Analytical mechanics](analytical-mechanics/README.md) | Lagrangian and Hamiltonian mechanics, canonical transformations, Hamilton–Jacobi, variational principles |
| [Rigid-body dynamics](rigid-body-dynamics/README.md) | Inertia tensor, Euler's equations, tops, gyroscopes and precession |
| [Oscillations and waves](oscillations-and-waves/README.md) | Damped/driven oscillators, normal modes, mechanical waves and acoustics, parametric resonance |
| [Nonlinear dynamics and chaos](nonlinear-dynamics-and-chaos/README.md) | Chaos, bifurcations, KAM theory, solitons, synchronization and patterns |
| [Continuum and fluid mechanics](continuum-and-fluid-mechanics/README.md) | Elasticity, viscous flow, turbulence, convection and instabilities, microfluidics |

## Conventions used in this branch
- SI units; generalized coordinates $q_i$, momenta $p_i=\partial L/\partial\dot q_i$; overdots are time derivatives.
- Lagrangian $L=T-V$; Hamiltonian $H=\sum p_i\dot q_i-L$; Poisson bracket $\{f,g\}=\sum_i(\partial_{q_i}f\,\partial_{p_i}g-\partial_{p_i}f\,\partial_{q_i}g)$.
- Fluids: Eulerian description, material derivative $D/Dt=\partial_t+\mathbf u\cdot\nabla$.

## Historical spine
1609–19 Kepler's laws · 1638 Galileo's *Two New Sciences* · 1687 Newton's *Principia* · 1736 Euler's *Mechanica* · 1752 Euler equations of fluids · 1788 Lagrange's *Mécanique analytique* · 1834 Hamilton's principle · 1845 Navier–Stokes · 1883 Reynolds' pipe-flow experiments · 1890 Poincaré and the three-body problem · 1941 Kolmogorov turbulence theory · 1954–63 KAM theorem · 1955 Fermi–Pasta–Ulam–Tsingou · 1963 Lorenz attractor · 1965 solitons · 1978 Feigenbaum universality.

## Canonical textbooks
- Taylor, *Classical Mechanics*; Kleppner & Kolenkow, *An Introduction to Mechanics* — undergraduate.
- Goldstein, Poole & Safko, *Classical Mechanics*; Landau & Lifshitz, *Mechanics* — graduate standards.
- Arnold, *Mathematical Methods of Classical Mechanics* — the geometric view.
- Strogatz, *Nonlinear Dynamics and Chaos*; Ott, *Chaos in Dynamical Systems*.
- Landau & Lifshitz, *Fluid Mechanics*; Kundu & Cohen, *Fluid Mechanics*; Landau & Lifshitz, *Theory of Elasticity*.

## Live frontiers
- Turbulence: intermittency, the Navier–Stokes regularity problem, data-driven closure models.
- Active and living fluids; granular flows; non-reciprocal interactions.
- Long-term stability of planetary systems and celestial mechanics with exoplanets.

## How the specialist works here
Choose coordinates that respect symmetry, identify conserved quantities first, use the Lagrangian for constrained systems and the Hamiltonian for phase-space questions, nondimensionalize fluid problems to see which terms matter, and check every answer against limiting cases (small angles, zero damping, equal masses).
