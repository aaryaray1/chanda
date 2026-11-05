---
title: Newtonian mechanics
summary: Motion under forces — Newton's laws, momentum and energy conservation, central forces and orbits, non-inertial frames, and few-body problems.
query: Newtonian mechanics; classical dynamics
---
# Newtonian mechanics

> Part of [Classical Mechanics](../README.md) · Key reviews: [papers.md](papers.md)

## Overview
Newton's three laws plus a force law (gravity, springs, friction, Lorentz force) predict the motion of everything from projectiles to planets. Conservation laws often give answers without solving the equations of motion, and the two-body problem reduces exactly to a one-body problem in a central potential.

## Topics
- [Kinematics and Newton's laws](kinematics-and-newtons-laws/README.md) — inertial frames, $\mathbf F=m\mathbf a$, free-body diagrams.
- [Conservation laws](conservation-laws/README.md) — energy, momentum, angular momentum; collisions.
- [Central forces and orbits](central-forces-and-orbits/README.md) — Kepler problem, effective potential, scattering.
- [Non-inertial frames](non-inertial-frames/README.md) — rotating frames, Coriolis and centrifugal forces.
- [Few-body and celestial mechanics](few-body-and-celestial-mechanics/README.md) — three-body problem, Lagrange points, orbital resonances.

## Conceptual spine
1. Inertial frames + $\mathbf F_{\text{net}}=d\mathbf p/dt$.
2. Work–energy theorem; conservative forces have potentials $\mathbf F=-\nabla V$.
3. Isolated systems conserve total momentum; central forces conserve angular momentum.
4. Two-body problem → reduced mass $\mu=m_1m_2/(m_1+m_2)$ in a central potential.

## Key equations
$$\mathbf F=\frac{d\mathbf p}{dt},\qquad E=\tfrac12\mu\dot r^2+\frac{L^2}{2\mu r^2}+V(r),\qquad r(\theta)=\frac{a(1-e^2)}{1+e\cos\theta},\quad T^2=\frac{4\pi^2a^3}{G(m_1+m_2)}$$

## Landmark papers
- Chenciner & Montgomery (2000). "A remarkable periodic solution of the three-body problem in the case of equal masses". *Ann. Math.* 152, 881. [arXiv:math/0011268](https://arxiv.org/abs/math/0011268)

## Open problems
- Long-term stability of the Solar System (chaotic on ~5 Myr Lyapunov times; Laskar).
- Classification of periodic orbits in the general three-body problem.

## Connections
- [Analytical mechanics](../analytical-mechanics/README.md) · [Noether's theorem](../../00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws/README.md) · [Special relativity](../../05-relativity-and-gravitation/special-relativity/README.md)
