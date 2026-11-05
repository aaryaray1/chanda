---
title: Differential equations and Green's functions
summary: Ordinary and partial differential equations of physics, separation of variables, Sturm–Liouville theory and Green's-function solutions.
query: Green's function; Sturm-Liouville; boundary value problem
source: openalex
---
# Differential equations and Green's functions
> [Foundations](../../README.md) › [Mathematical methods](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Linear ODEs, series (Frobenius) solutions, Sturm–Liouville problems, Laplace/Poisson, wave, diffusion and Helmholtz equations, separation of variables, Fourier and Laplace transforms, Green's functions with boundary conditions, retarded/advanced propagators, method of characteristics.

**Core ideas.**
- PDE type (elliptic, hyperbolic, parabolic) determines which boundary/initial data give well-posed problems.
- Sturm–Liouville eigenfunctions form complete orthogonal sets — Fourier series, Legendre, Bessel expansions.
- Causality picks the retarded Green's function for wave problems.

**Key equations.**
$$\nabla^2G=-\delta^3(\mathbf r)\Rightarrow G=\frac{1}{4\pi r},\qquad \left(\nabla^2-\frac{1}{c^2}\partial_t^2\right)G=-\delta^4\Rightarrow G_{\text{ret}}=\frac{\delta(t-r/c)}{4\pi r}$$

**See also.** [Electrostatics and boundary-value problems](../../../02-electromagnetism-and-optics/electrostatics-and-magnetostatics/electrostatics-and-boundary-value-problems/README.md) · [Numerical methods for ODEs and PDEs](../../computational-physics/numerical-methods-for-odes-and-pdes/README.md)
