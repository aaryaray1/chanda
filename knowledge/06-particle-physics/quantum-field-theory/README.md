---
title: Quantum field theory
summary: The framework of particle physics — fields, quantization, perturbation theory, renormalization, gauge symmetry, and non-perturbative methods.
query: quantum field theory
arxiv: hep-th hep-ph hep-lat
---
# Quantum field theory

> Part of [Particle Physics](../README.md) · Key reviews: [papers.md](papers.md)

## Overview
Quantum field theory (QFT) unifies quantum mechanics and special relativity: particles are excitations of fields, and particle number is not conserved. It is the language of the Standard Model, of critical phenomena in statistical physics, and of most of condensed-matter theory. The modern view (Wilson) treats every QFT as an **effective theory** valid below some cutoff, with the renormalization group describing how couplings change with scale.

## Topics
- [Canonical and path-integral quantization](canonical-and-path-integral-quantization/README.md) — two routes from classical fields to quantum ones.
- [Feynman diagrams and scattering amplitudes](feynman-diagrams-and-scattering-amplitudes/README.md) — perturbation theory and modern on-shell methods.
- [Renormalization and running couplings](renormalization-and-running-couplings/README.md) — infinities, counterterms, beta functions.
- [Gauge theories and Yang–Mills](gauge-theories-and-yang-mills/README.md) — local symmetry as the origin of forces.
- [Effective field theory](effective-field-theory/README.md) — separation of scales and power counting.
- [Lattice field theory](lattice-field-theory/README.md) — non-perturbative QFT on a computer.
- [Anomalies, instantons and topology](anomalies-instantons-and-topology/README.md) — quantum violations of classical symmetries.
- [Conformal field theory](conformal-field-theory/README.md) — scale-invariant QFTs and the bootstrap.

## Conceptual spine
1. Fields → canonical commutators or path integral $Z=\int\mathcal{D}\phi\,e^{iS[\phi]}$.
2. Correlation functions → LSZ reduction → S-matrix → cross sections.
3. Loops diverge → regularize (dimensional regularization) → renormalize → couplings run.
4. Gauge invariance fixes interactions; quantization needs gauge fixing and ghosts (Faddeev–Popov).
5. Non-perturbative physics (confinement, instantons, phase transitions) needs lattice, dualities, or bootstrap.

## Key equations
$$\mathcal{L}_{\text{QED}} = \bar\psi(i\gamma^\mu D_\mu - m)\psi - \tfrac14 F_{\mu\nu}F^{\mu\nu},\qquad D_\mu=\partial_\mu+ieA_\mu$$
$$\mu\frac{dg}{d\mu}=\beta(g),\qquad \beta_{\text{YM}}(g) = -\frac{g^3}{16\pi^2}\left(\frac{11}{3}C_A-\frac{4}{3}T_F n_f\right)+\mathcal{O}(g^5)$$

## Landmark papers
- Feynman (1949). "Space-Time Approach to Quantum Electrodynamics". *Phys. Rev.* 76, 769. [doi:10.1103/PhysRev.76.769](https://doi.org/10.1103/PhysRev.76.769)
- Yang & Mills (1954). "Conservation of Isotopic Spin and Isotopic Gauge Invariance". *Phys. Rev.* 96, 191. [doi:10.1103/PhysRev.96.191](https://doi.org/10.1103/PhysRev.96.191)
- 't Hooft & Veltman (1972). "Regularization and renormalization of gauge fields". *Nucl. Phys. B* 44, 189. [doi:10.1016/0550-3213(72)90279-9](https://doi.org/10.1016/0550-3213(72)90279-9)
- Wilson & Kogut (1974). "The renormalization group and the ε expansion". *Phys. Rep.* 12, 75. [doi:10.1016/0370-1573(74)90023-4](https://doi.org/10.1016/0370-1573(74)90023-4)
- Wilson (1974). "Confinement of quarks". *Phys. Rev. D* 10, 2445. [doi:10.1103/PhysRevD.10.2445](https://doi.org/10.1103/PhysRevD.10.2445)
- Weinberg (1979). "Phenomenological Lagrangians". *Physica A* 96, 327. [doi:10.1016/0378-4371(79)90223-1](https://doi.org/10.1016/0378-4371(79)90223-1)

## Open problems
- Rigorous construction of 4D interacting QFTs; the Yang–Mills mass gap (Clay problem).
- Why does the Higgs mass not run to the cutoff (naturalness)?
- Classifying QFTs: which conformal theories exist, and how are they connected by RG flows?

## Connections
- Statistical field theory and critical phenomena: [Renormalization group](../../03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/README.md)
- QFT in curved spacetime and holography: [Quantum gravity](../../05-relativity-and-gravitation/quantum-gravity/README.md)
- Many-body field theory: [Strongly correlated electrons](../../08-condensed-matter/strongly-correlated-electrons/README.md)
