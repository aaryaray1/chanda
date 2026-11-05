---
title: Lagrangian mechanics
summary: Equations of motion from L = T − V in generalized coordinates, holonomic constraints, Lagrange multipliers and cyclic coordinates.
query: Lagrangian mechanics; Euler-Lagrange equations; holonomic constraints
---
# Lagrangian mechanics
> [Classical Mechanics](../../README.md) › [Analytical mechanics](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Generalized coordinates, D'Alembert's principle, holonomic and non-holonomic constraints, Lagrange multipliers and constraint forces, cyclic (ignorable) coordinates, velocity-dependent potentials (charged particle: $L=\tfrac12mv^2-q\phi+q\mathbf v\cdot\mathbf A$), small oscillations, Lagrangian field theory.

**Core ideas.**
- Constraint forces drop out when coordinates are chosen to satisfy constraints.
- If $L$ does not depend on $q_k$, its conjugate momentum $p_k$ is conserved.
- Field theories use a Lagrangian density $\mathcal L(\phi,\partial_\mu\phi)$ — the same machinery.

**Key equations.**
$$\frac{d}{dt}\frac{\partial L}{\partial\dot q_k}-\frac{\partial L}{\partial q_k}=\sum_j\lambda_j\frac{\partial f_j}{\partial q_k}\quad(\text{constraints }f_j(q)=0)$$

**See also.** [Variational principles](../variational-principles/README.md) · [Canonical quantization](../../../06-particle-physics/quantum-field-theory/canonical-and-path-integral-quantization/README.md)
