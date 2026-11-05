---
title: Rigid-body dynamics
summary: Rotation of extended bodies — inertia tensor, Euler's equations, torque-free and heavy tops, gyroscopes and precession.
query: rigid body dynamics; rotational dynamics
---
# Rigid-body dynamics

> Part of [Classical Mechanics](../README.md) · Key reviews: [papers.md](papers.md)

## Overview
A rigid body has six degrees of freedom: three for its centre of mass and three for orientation. Rotational dynamics is governed by the inertia tensor, and because angular velocity and angular momentum need not be parallel, rotation shows surprising behaviour: wobbling free rotation, the tennis-racket (Dzhanibekov) instability, gyroscopic precession and nutation.

## Topics
- [Rotational dynamics and the inertia tensor](rotational-dynamics-and-inertia-tensor/README.md) — moments of inertia, principal axes, parallel-axis theorem.
- [Euler's equations and tops](euler-equations-and-tops/README.md) — torque-free motion, intermediate-axis instability, the heavy symmetric top.
- [Gyroscopes and precession](gyroscopes-and-precession/README.md) — gyroscopic stability, precession of the equinoxes, applications.

## Key equations
$$\mathbf L=\mathsf I\boldsymbol\omega,\qquad I_{ij}=\int\rho\,(r^2\delta_{ij}-x_ix_j)\,dV,\qquad I_1\dot\omega_1-(I_2-I_3)\omega_2\omega_3=\tau_1$$

## Open problems
- Rigid-body control and attitude dynamics of spacecraft; rattleback and other nonholonomic puzzles.

## Connections
- [Analytical mechanics](../analytical-mechanics/README.md) · [Lie groups (SO(3))](../../00-foundations/symmetry-and-group-theory/lie-groups-and-representations/README.md)
