---
title: Electrostatics and magnetostatics
summary: Static electric and magnetic fields — Coulomb and Gauss's laws, Poisson's equation and boundary-value problems, multipole expansions, Biot–Savart, and fields in matter.
query: electrostatics; magnetostatics
---
# Electrostatics and magnetostatics

> Part of [Electromagnetism and Optics](../README.md) · Key reviews: [papers.md](papers.md)

## Overview
When charges and currents don't change in time, electric and magnetic fields decouple. Electrostatics reduces to Poisson's equation for the potential; magnetostatics to Ampère's law for the vector potential. Uniqueness theorems make clever methods (images, separation of variables) rigorous.

## Topics
- [Electrostatics and boundary-value problems](electrostatics-and-boundary-value-problems/README.md) — Poisson/Laplace, method of images, conductors, capacitance.
- [Multipole expansions](multipole-expansions/README.md) — monopole, dipole, quadrupole fields and their uses.
- [Magnetostatics](magnetostatics/README.md) — Biot–Savart, Ampère, vector potential, magnetic dipoles.
- [Fields in matter](fields-in-matter/README.md) — polarization, magnetization, D and H, dielectrics and magnetic materials.

## Key equations
$$\nabla\cdot\mathbf E=\frac{\rho}{\epsilon_0},\quad\nabla\times\mathbf E=0,\quad\nabla^2V=-\frac{\rho}{\epsilon_0};\qquad \nabla\times\mathbf B=\mu_0\mathbf J,\quad \mathbf B(\mathbf r)=\frac{\mu_0}{4\pi}\int\frac{\mathbf J\times\hat{\boldsymbol{\mathscr r}}}{\mathscr r^2}dV'$$

## Open problems
- Electrostatics is "complete", but computational electrostatics of biomolecules and nanodevices (implicit solvents, image charges at interfaces) remains active.

## Connections
- [Green's functions](../../00-foundations/mathematical-methods/differential-equations-and-greens-functions/README.md) · [Magnetism (condensed matter)](../../08-condensed-matter/magnetism/README.md)
