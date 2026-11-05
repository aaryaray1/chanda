---
title: Quantum information and computation
summary: Information processing with quantum systems — entanglement theory, algorithms, error correction, hardware platforms and quantum communication.
query: quantum computing; quantum information
arxiv: quant-ph cs.ET
openalex_filter: primary_topic.field.id:31|17
---
# Quantum information and computation

> Part of [Quantum Physics](../README.md) · Key reviews: [papers.md](papers.md)

## Overview
Quantum information treats superposition and entanglement as resources. A quantum computer manipulates $n$ qubits in a $2^n$-dimensional space; for certain problems (factoring, simulating quantum matter) this gives super-polynomial speedups. Noise is the central obstacle: quantum error correction encodes logical qubits in many physical ones, and the threshold theorem guarantees arbitrarily reliable computation if physical error rates are below ~1%.

## Topics
- [Entanglement theory](entanglement-theory/README.md) — measures, monogamy, entanglement entropy.
- [Quantum algorithms and complexity](quantum-algorithms-and-complexity/README.md) — Shor, Grover, simulation, BQP, quantum advantage.
- [Quantum error correction and fault tolerance](quantum-error-correction-and-fault-tolerance/README.md) — stabilizer codes, surface code, thresholds.
- [Superconducting qubits](superconducting-qubits/README.md) — transmons, fluxonium, cQED processors.
- [Trapped-ion and neutral-atom qubits](trapped-ion-and-neutral-atom-qubits/README.md) — ions in Paul traps, Rydberg atom arrays.
- [Photonic and spin qubits](photonic-and-spin-qubits/README.md) — linear optics, quantum dots, NV centers.
- [Quantum communication and cryptography](quantum-communication-and-cryptography/README.md) — QKD, teleportation, repeaters, networks.

## Conceptual spine
1. Qubits, gates (universal sets: Clifford + T), measurement; circuits as unitary products.
2. Entanglement and interference provide computational power; no-cloning forbids copying unknown states.
3. Errors are discretized by syndrome measurement; codes with distance $d$ correct $\lfloor(d-1)/2\rfloor$ errors.
4. Hardware is judged by gate fidelity, coherence, connectivity, speed and scalability.

## Key equations
$$|\psi\rangle=\sum_{x\in\{0,1\}^n}c_x|x\rangle,\qquad p_L\approx A\left(\frac{p}{p_{\text{th}}}\right)^{\lfloor(d+1)/2\rfloor}$$

## Landmark papers
- Bennett et al. (1993). "Teleporting an unknown quantum state via dual classical and Einstein-Podolsky-Rosen channels". *Phys. Rev. Lett.* 70, 1895. [doi:10.1103/PhysRevLett.70.1895](https://doi.org/10.1103/PhysRevLett.70.1895)
- Shor (1997). "Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer". *SIAM J. Comput.* 26, 1484. [arXiv:quant-ph/9508027](https://arxiv.org/abs/quant-ph/9508027)
- Shor (1995). "Scheme for reducing decoherence in quantum computer memory". *Phys. Rev. A* 52, R2493. [doi:10.1103/PhysRevA.52.R2493](https://doi.org/10.1103/PhysRevA.52.R2493)
- Grover (1996). "A fast quantum mechanical algorithm for database search". [arXiv:quant-ph/9605043](https://arxiv.org/abs/quant-ph/9605043)
- Kitaev (1997; published 2003). "Fault-tolerant quantum computation by anyons". *Ann. Phys.* 303, 2. [arXiv:quant-ph/9707021](https://arxiv.org/abs/quant-ph/9707021)
- Horodecki et al. (2009). "Quantum entanglement". *Rev. Mod. Phys.* 81, 865. [arXiv:quant-ph/0702225](https://arxiv.org/abs/quant-ph/0702225)
- Preskill (2018). "Quantum Computing in the NISQ era and beyond". *Quantum* 2, 79. [arXiv:1801.00862](https://arxiv.org/abs/1801.00862)
- Arute et al. (2019). "Quantum supremacy using a programmable superconducting processor". *Nature* 574, 505. [arXiv:1910.11333](https://arxiv.org/abs/1910.11333)
- Google Quantum AI (2024). "Quantum error correction below the surface code threshold". *Nature* 638, 920. [arXiv:2408.13687](https://arxiv.org/abs/2408.13687)

## Open problems
- Which useful problems have provable, practical quantum advantage?
- Overhead reduction: qLDPC codes, magic-state cultivation, better decoders.
- Scaling to millions of physical qubits with manageable wiring, cooling and control.

## Connections
- [Foundations](../foundations-of-quantum-mechanics/README.md) · [Topological order and anyons](../../08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order/README.md) · [Josephson junctions](../../08-condensed-matter/superconductivity/josephson-effect-and-squids/README.md) · [Entropy and information](../../03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information/README.md)
