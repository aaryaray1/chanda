---
title: Electrodynamics
summary: Time-dependent fields — Maxwell's equations, electromagnetic waves and waveguides, potentials and gauge invariance, and the relativistic formulation.
query: classical electrodynamics; Maxwell equations
---
# Electrodynamics

> Part of [Electromagnetism and Optics](../README.md) · Key reviews: [papers.md](papers.md)

## Overview
Faraday's induction and Maxwell's displacement current couple $\mathbf E$ and $\mathbf B$ into self-sustaining waves travelling at $c=1/\sqrt{\epsilon_0\mu_0}$. Maxwell's theory was the first relativistic field theory, the first gauge theory, and the model for every field theory since.

## Topics
- [Maxwell's equations](maxwells-equations/README.md) — the four equations, conservation of charge, energy and momentum of fields.
- [Electromagnetic waves and waveguides](electromagnetic-waves-and-waveguides/README.md) — plane waves, reflection/refraction, guided modes, cavities.
- [Potentials and gauge invariance](potentials-and-gauge-invariance/README.md) — scalar and vector potentials, Coulomb and Lorenz gauges.
- [Relativistic electrodynamics](relativistic-electrodynamics/README.md) — field tensor, covariant equations, field transformations.

## Key equations
$$\nabla\cdot\mathbf E=\frac\rho{\epsilon_0},\quad\nabla\cdot\mathbf B=0,\quad\nabla\times\mathbf E=-\frac{\partial\mathbf B}{\partial t},\quad\nabla\times\mathbf B=\mu_0\mathbf J+\mu_0\epsilon_0\frac{\partial\mathbf E}{\partial t}$$
$$\mathbf S=\frac{1}{\mu_0}\mathbf E\times\mathbf B,\qquad u=\frac{\epsilon_0}{2}E^2+\frac{1}{2\mu_0}B^2,\qquad \frac{\partial u}{\partial t}+\nabla\cdot\mathbf S=-\mathbf J\cdot\mathbf E$$

## Landmark papers
- Maxwell (1865). "A Dynamical Theory of the Electromagnetic Field". *Phil. Trans. R. Soc.* 155, 459. [doi:10.1098/rstl.1865.0008](https://doi.org/10.1098/rstl.1865.0008)
- Dirac (1938). "Classical theory of radiating electrons". *Proc. R. Soc. A* 167, 148. [doi:10.1098/rspa.1938.0124](https://doi.org/10.1098/rspa.1938.0124)

## Open problems
- Consistent classical treatment of radiation reaction (runaway solutions of Abraham–Lorentz–Dirac; Landau–Lifshitz approximation) — now tested with ultra-intense lasers.
- The Abraham–Minkowski controversy over light's momentum in media.

## Connections
- [Special relativity](../../05-relativity-and-gravitation/special-relativity/README.md) · [Gauge theories](../../06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills/README.md) · [Plasma waves](../../10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities/README.md)
