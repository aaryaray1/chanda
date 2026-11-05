---
title: Postulates and formalism
summary: Hilbert space, observables, the Born rule, time evolution, pictures, and density matrices.
query: density matrix; quantum state; Born rule
---
# Postulates and formalism
> [Quantum Physics](../../README.md) › [QM formalism](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Kets, bras, operators, spectral decomposition, commutators, Schrödinger/Heisenberg/interaction pictures, density operators, partial trace, POVMs, Gleason's theorem.

**Core ideas.**
- Pure states are rays in $\mathcal H$; mixed states are positive, unit-trace operators $\rho$.
- Expectation values $\langle A\rangle=\mathrm{Tr}(\rho A)$; the reduced state of a subsystem is $\rho_A=\mathrm{Tr}_B\,\rho_{AB}$.
- Generalized measurements (POVMs) cover realistic, imperfect detection.

**Key equations.**
$$\frac{d\langle A\rangle}{dt}=\frac{i}{\hbar}\langle[H,A]\rangle+\left\langle\frac{\partial A}{\partial t}\right\rangle,\qquad \rho(t)=U\rho(0)U^\dagger$$

**See also.** [Measurement problem](../../foundations-of-quantum-mechanics/measurement-problem-and-interpretations/README.md) · [Hilbert spaces](../../../00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces/README.md)
