---
title: Quantum communication and cryptography
summary: Quantum key distribution, teleportation, quantum repeaters and the quantum internet.
query: quantum key distribution; quantum teleportation; quantum repeater
---
# Quantum communication and cryptography
> [Quantum Physics](../../README.md) › [Quantum information](../README.md) · Literature: [papers.md](papers.md)

**Scope.** BB84 and E91 protocols, decoy states, measurement-device-independent and device-independent QKD, satellite QKD (Micius), teleportation, entanglement swapping, quantum repeaters and memories, post-quantum vs. quantum cryptography.

**Core ideas.**
- Eavesdropping disturbs non-orthogonal states (no-cloning), so the error rate bounds the eavesdropper's information.
- Photon loss in fibre grows exponentially with distance; repeaters need entanglement swapping plus quantum memories.
- Security proofs must model real devices — side-channel attacks have broken idealized implementations.

**Key equations.**
$$r_{\text{BB84}}\ge1-2h(Q),\qquad h(x)=-x\log_2x-(1-x)\log_2(1-x),\qquad Q<11\%$$

**Landmarks.** Bennett et al. (1993); Ekert (1991). "Quantum cryptography based on Bell's theorem". *Phys. Rev. Lett.* 67, 661. [doi:10.1103/PhysRevLett.67.661](https://doi.org/10.1103/PhysRevLett.67.661)

**See also.** [Bell nonlocality](../../foundations-of-quantum-mechanics/bell-nonlocality/README.md) · [Integrated and fiber photonics](../../../02-electromagnetism-and-optics/photonics-and-lasers/integrated-and-fiber-photonics/README.md)
