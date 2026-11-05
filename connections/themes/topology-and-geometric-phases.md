---
title: Geometric phases, gauge fields and band topology
summary: The Berry phase of a slowly transported quantum state has the mathematics of a gauge field; integrated over a crystal's Brillouin zone it becomes a quantized Chern number — the quantum Hall conductance — and its monopoles are Weyl points.
fields: 04 08 02 06 01
kind: identity · method transfer
---
# Geometric phases, gauge fields and band topology
> Curated theme · [Connections atlas](../../CONNECTIONS.md) · Kind: identity, method transfer

**The bridge.** A quantum state carried slowly around a closed loop in parameter space returns with an extra phase. That phase depends only on the loop's geometry: it is the flux of the Berry curvature through the loop. The mathematics is a connection and its curvature on a fibre bundle, exactly the mathematics of gauge fields. The Aharonov–Bohm phase is the Berry phase of a charge circling a flux tube.

In a crystal the parameter space is the Brillouin zone, a torus. The Berry curvature of a filled band, integrated over it, is an integer Chern number, and TKNN showed that this number is the quantized Hall conductance. This one idea led to:
- quantum Hall states without Landau levels (Haldane);
- time-reversal-protected $\mathbb Z_2$ insulators (Kane–Mele);
- Weyl semimetals, whose band crossings are monopoles of Berry curvature and carry the chiral anomaly of particle physics into a solid.

*Established.*

**How each branch sees it.**
- **Quantum physics:** [Geometric phases](../../knowledge/04-quantum-physics/quantum-mechanics-core/geometric-phases/README.md) covers the adiabatic theorem, Berry connection and curvature, and the AB effect.
- **Condensed matter:**
  - [Band topology and Berry curvature](../../knowledge/08-condensed-matter/topological-matter/band-topology-and-berry-curvature/README.md).
  - [Quantum Hall effects](../../knowledge/08-condensed-matter/topological-matter/quantum-hall-effects/README.md).
  - [Topological insulators](../../knowledge/08-condensed-matter/topological-matter/topological-insulators/README.md).
  - [Topological semimetals](../../knowledge/08-condensed-matter/topological-matter/topological-semimetals/README.md).
  - [Majoranas](../../knowledge/08-condensed-matter/topological-matter/topological-superconductors-and-majoranas/README.md).
- **Particle physics:** [Anomalies, instantons and topology](../../knowledge/06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology/README.md). The ABJ anomaly reappears in Weyl semimetals as negative longitudinal magnetoresistance.
- **Optics:** The polarization of light has a geometric phase (Pancharatnam). Photonic bands carry Chern numbers too, which is the basis of topological photonics.
- **Classical mechanics:** Classical geometric phases include the Hannay angle. The Foucault pendulum's daily turn of $2\pi\sin(\text{latitude})$ is the holonomy of parallel transport around a circle of latitude.

**Shared structure.**
$$\gamma_n=i\oint\langle n(\mathbf R)|\nabla_{\mathbf R}n(\mathbf R)\rangle\cdot d\mathbf R=\int_S\boldsymbol\Omega_n\cdot d\mathbf S,\qquad \gamma_{AB}=\frac{q\Phi}{\hbar}$$
$$\sigma_{xy}=\frac{e^2}{h}\sum_{n\,\text{occ}}C_n,\qquad C_n=\frac1{2\pi}\int_{\text{BZ}}\Omega^{(n)}_{xy}\,d^2k\in\mathbb Z$$

**Symbol map.**

| Berry geometry | Electromagnetism |
|---|---|
| Berry connection $\mathbf A_n=i\langle n\vert\nabla n\rangle$ | vector potential |
| Berry curvature $\boldsymbol\Omega_n$ | magnetic field |
| level degeneracy point | magnetic monopole (strength ½ for a two-level crossing) |
| Chern-number quantization | Dirac's monopole quantization |

**Where it breaks.**
- *The curvature lives in parameter space.* Berry curvature acts in parameter or momentum space, not real space. It deflects wavepackets through the anomalous velocity, but it is not a magnetic field.
- *Protection has conditions.* It needs a bulk gap, the protecting symmetry and adiabaticity. Disorder or symmetry breaking can remove it, and a zero-bias peak alone does not prove a Majorana.
- *Interactions go beyond band topology.* The fractional quantum Hall effect involves topological order, a many-body notion (see [fractionalization and topological order](../../knowledge/08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order/README.md)).

**Landmarks.**
- Aharonov & Bohm (1959). "Significance of Electromagnetic Potentials in the Quantum Theory". *Phys. Rev.* 115, 485. [doi:10.1103/PhysRev.115.485](https://doi.org/10.1103/PhysRev.115.485)
- Adler (1969). "Axial-Vector Vertex in Spinor Electrodynamics". *Phys. Rev.* 177, 2426. [doi:10.1103/PhysRev.177.2426](https://doi.org/10.1103/PhysRev.177.2426)
- Thouless, Kohmoto, Nightingale & den Nijs (1982). "Quantized Hall Conductance in a Two-Dimensional Periodic Potential". *Phys. Rev. Lett.* 49, 405. [doi:10.1103/PhysRevLett.49.405](https://doi.org/10.1103/PhysRevLett.49.405)
- Berry (1984). "Quantal phase factors accompanying adiabatic changes". *Proc. R. Soc. A* 392, 45. [doi:10.1098/rspa.1984.0023](https://doi.org/10.1098/rspa.1984.0023)
- Haldane (1988). "Model for a Quantum Hall Effect without Landau Levels: Condensed-Matter Realization of the 'Parity Anomaly'". *Phys. Rev. Lett.* 61, 2015. [doi:10.1103/PhysRevLett.61.2015](https://doi.org/10.1103/PhysRevLett.61.2015)
- Kitaev (2001). "Unpaired Majorana fermions in quantum wires". *Phys.-Usp.* 44, 131. [arXiv:cond-mat/0010440](https://arxiv.org/abs/cond-mat/0010440)
- Kane & Mele (2005). "Z2 Topological Order and the Quantum Spin Hall Effect". *Phys. Rev. Lett.* 95, 146802. [arXiv:cond-mat/0506581](https://arxiv.org/abs/cond-mat/0506581)
- Xu et al. (2015). "Discovery of a Weyl fermion semimetal and topological Fermi arcs". *Science* 349, 613. [arXiv:1502.03807](https://arxiv.org/abs/1502.03807)

**Open questions.** What is the complete classification of interacting topological phases? Can non-Abelian anyons be braided reliably for quantum computing? How far can topological ideas transfer to classical waves and mechanical metamaterials?
