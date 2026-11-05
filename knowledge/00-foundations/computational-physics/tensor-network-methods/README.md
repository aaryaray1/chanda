---
title: Tensor network methods
summary: Compressing quantum many-body states using their entanglement structure — MPS, DMRG, PEPS, MERA and tensor-network simulation of circuits.
query: tensor network; matrix product state; density matrix renormalization group
---
# Tensor network methods
> [Foundations](../../README.md) › [Computational physics](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Matrix product states and operators, DMRG, TEBD for time evolution, PEPS for 2D, MERA and holography, bond dimension and truncation error, tensor-network contraction for simulating quantum circuits.

**Core ideas.**
- Area-law entanglement makes ground states of gapped 1D systems efficiently representable by MPS.
- DMRG variationally optimizes an MPS — the most accurate method for 1D quantum systems.
- Time evolution grows entanglement, limiting accessible times.

**Key equations.**
$$|\psi\rangle=\sum_{\{s\}}\mathrm{Tr}\left(A^{s_1}A^{s_2}\cdots A^{s_N}\right)|s_1s_2\cdots s_N\rangle,\qquad S\le\log\chi$$

**Landmarks.** White (1992); Schollwöck (2011) — see [subfield landmarks](../README.md).

**See also.** [Entanglement theory](../../../04-quantum-physics/quantum-information-and-computation/entanglement-theory/README.md) · [Numerical many-body methods](../../../08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods/README.md)
