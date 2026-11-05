---
title: Quantum algorithms and complexity
summary: What quantum computers can compute efficiently — Shor, Grover, quantum simulation, variational methods, BQP and quantum-advantage experiments.
query: quantum algorithm; quantum advantage; quantum simulation algorithm
---
# Quantum algorithms and complexity
> [Quantum Physics](../../README.md) › [Quantum information](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Quantum Fourier transform, phase estimation, Shor's factoring, Grover search and amplitude amplification, Hamiltonian simulation (Trotter, qubitization), HHL, VQE and QAOA, BQP and its relation to NP and PH, random-circuit sampling and boson-sampling advantage, dequantization results.

**Core ideas.**
- Exponential speedups come from structure (periodicity, simulation of quantum dynamics), not from "trying all answers".
- Grover's quadratic speedup is optimal for unstructured search.
- Quantum-advantage claims are contested by improved classical simulation; verifiability matters.

**Key equations.**
$$\text{QFT}:|x\rangle\mapsto\frac{1}{\sqrt N}\sum_ye^{2\pi ixy/N}|y\rangle,\qquad T_{\text{Grover}}\approx\frac\pi4\sqrt{N}$$

**Landmarks.** Shor (1997); Grover (1996); Arute et al. (2019) — see [subfield landmarks](../README.md).

**See also.** [Quantum chemistry methods](../../../11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods/README.md)
