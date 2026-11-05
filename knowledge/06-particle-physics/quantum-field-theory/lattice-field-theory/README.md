---
title: Lattice field theory
summary: Non-perturbative QFT computed numerically on a discrete Euclidean spacetime lattice; lattice QCD.
query: lattice QCD; lattice gauge theory
arxiv: hep-lat
---
# Lattice field theory
> [Particle Physics](../../README.md) › [Quantum field theory](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Wilson's lattice gauge action, fermion discretizations (Wilson, staggered, domain-wall, overlap), Monte Carlo (HMC), continuum and chiral extrapolations, hadron masses, $\alpha_s$, quark masses, hadronic vacuum polarization for muon $g-2$.

**Core ideas.**
- Euclidean path integral on a hypercubic grid becomes a statistical-mechanics problem sampled by Markov-chain Monte Carlo.
- Gauge links $U_\mu(x)=e^{iagA_\mu(x)}$ keep exact gauge invariance at finite spacing $a$.
- Fermion doubling (Nielsen–Ninomiya) forces trade-offs between chiral symmetry and locality.
- The sign problem blocks finite-density QCD and real-time dynamics.

**Key equations.**
$$S_W=\beta\sum_{x,\mu<\nu}\left(1-\tfrac{1}{N}\,\mathrm{Re\,Tr}\,U_{\mu\nu}(x)\right),\qquad \beta=2N/g^2$$

**Landmark.** Wilson (1974) "Confinement of quarks" — see [subfield landmarks](../README.md).

**Open questions.** Sign problem; precision HVP to settle the muon $g-2$ comparison; quantum simulation of gauge theories.

**See also.** [Monte Carlo methods](../../../00-foundations/computational-physics/monte-carlo-methods/README.md) · [QCD phase diagram](../../../07-nuclear-physics/heavy-ion-physics/qcd-phase-diagram-and-critical-point/README.md)
