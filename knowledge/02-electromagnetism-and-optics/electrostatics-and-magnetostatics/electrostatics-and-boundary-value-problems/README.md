---
title: Electrostatics and boundary-value problems
summary: Solving for static fields — Gauss's law, Poisson/Laplace equations, uniqueness, method of images, separation of variables, conductors and capacitance.
query: electrostatics; Poisson equation; method of images
---
# Electrostatics and boundary-value problems
> [Electromagnetism and Optics](../../README.md) › [Electrostatics and magnetostatics](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Coulomb's law, Gauss's law with symmetry, potential and energy, conductors in equilibrium, Dirichlet and Neumann problems, uniqueness theorems, image charges (plane, sphere), separation of variables in Cartesian/spherical/cylindrical coordinates, capacitance, electrostatic energy and forces, Earnshaw's theorem.

**Core ideas.**
- Laplace's equation has no local extrema — so no stable electrostatic trap (Earnshaw); ion traps need RF (Paul) or magnetic fields (Penning).
- Uniqueness lets any guessed solution satisfying the boundary conditions be the solution.
- Energy can be stored in the field: $u=\tfrac12\epsilon_0E^2$.

**Key equations.**
$$\oint\mathbf E\cdot d\mathbf A=\frac{Q_{\text{enc}}}{\epsilon_0},\qquad V(r,\theta)=\sum_\ell\left(A_\ell r^\ell+\frac{B_\ell}{r^{\ell+1}}\right)P_\ell(\cos\theta),\qquad C_{\text{sphere}}=4\pi\epsilon_0R$$

**See also.** [Green's functions](../../../00-foundations/mathematical-methods/differential-equations-and-greens-functions/README.md) · [Trapped-ion qubits](../../../04-quantum-physics/quantum-information-and-computation/trapped-ion-and-neutral-atom-qubits/README.md)
