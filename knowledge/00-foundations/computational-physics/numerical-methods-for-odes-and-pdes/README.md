---
title: Numerical methods for ODEs and PDEs
summary: Time integrators, symplectic methods, finite differences, finite elements, finite volumes and spectral methods.
query: symplectic integrator; finite element method; spectral method
---
# Numerical methods for ODEs and PDEs
> [Foundations](../../README.md) › [Computational physics](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Explicit/implicit schemes, Runge–Kutta, adaptive step size, stiffness, symplectic (leapfrog/Verlet) integrators, CFL condition, von Neumann stability analysis, finite elements, finite volumes for conservation laws, spectral/pseudospectral methods, multigrid, FFT.

**Core ideas.**
- Order of accuracy, stability and conservation are separate properties; check all three.
- Symplectic integrators conserve a nearby Hamiltonian — no secular energy drift in long orbital runs.
- Explicit wave solvers need $c\Delta t/\Delta x\le1$ (CFL).

**Key equations.**
$$x_{n+1}=x_n+v_n\Delta t+\tfrac12a_n\Delta t^2,\quad v_{n+1}=v_n+\tfrac12(a_n+a_{n+1})\Delta t\ (\text{velocity Verlet})$$

**See also.** [Hamiltonian mechanics](../../../01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics/README.md) · [Turbulence](../../../01-classical-mechanics/continuum-and-fluid-mechanics/turbulence/README.md)
