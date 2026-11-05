---
title: Quantum error correction and fault tolerance
summary: Protecting quantum information from noise — stabilizer codes, the surface code, thresholds, decoders and logical-qubit experiments.
query: quantum error correction; surface code; fault-tolerant quantum computation
---
# Quantum error correction and fault tolerance
> [Quantum Physics](../../README.md) › [Quantum information](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Shor and Steane codes, stabilizer formalism, CSS codes, toric and surface codes, threshold theorem, decoders (MWPM, union-find, neural), lattice surgery, magic-state distillation, bosonic codes (cat, GKP), qLDPC codes, below-threshold experiments (Google 2024), logical processors with atom arrays.

**Core ideas.**
- Measure stabilizers (parity checks) to learn the error syndrome without learning the encoded state.
- Surface code: local checks on a 2D grid, threshold ~1%, logical error suppressed exponentially in distance $d$.
- Clifford gates are cheap; non-Clifford (T) gates need magic states — the dominant overhead.

**Key equations.**
$$[[n,k,d]]:\ \text{surface code}\ [[d^2,1,d]],\qquad \Lambda=\frac{\epsilon_d}{\epsilon_{d+2}}>1\ \text{below threshold}$$

**Landmarks.** Shor (1995); Kitaev (1997, publ. 2003); Google Quantum AI (2024) — see [subfield landmarks](../README.md).

**See also.** [Topological order](../../../08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order/README.md)
