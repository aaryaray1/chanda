---
title: Disordered and complex systems
summary: Physics of randomness and emergent complexity — spin glasses, localization, percolation, complex networks and the statistical physics of learning.
query: disordered systems; spin glass; complex systems
arxiv: cond-mat.dis-nn physics.soc-ph nlin.AO
openalex_filter: primary_topic.field.id:31|17|26
---
# Disordered and complex systems

> Part of [Thermodynamics and Statistical Mechanics](../README.md) · Key reviews: [papers.md](papers.md)

## Overview
Quenched randomness — impurities, random couplings, random graphs — produces phenomena absent in clean systems: glassy freezing with rugged energy landscapes, localization of waves, geometric phase transitions in connectivity. The same toolkit (replicas, cavity method, random matrices) now underpins the theory of neural networks, optimization and inference — recognised by the 2021 (Parisi) and 2024 (Hopfield, Hinton) Nobel Prizes.

## Topics
- [Spin glasses](spin-glasses/README.md) — frustration, replica symmetry breaking, rugged landscapes.
- [Localization and disorder](localization-and-disorder/README.md) — Anderson localization, many-body localization.
- [Percolation](percolation/README.md) — connectivity transitions on random lattices.
- [Complex networks](complex-networks/README.md) — small worlds, scale-free graphs, epidemics.
- [Statistical physics of learning](statistical-physics-of-learning/README.md) — Hopfield networks, Boltzmann machines, high-dimensional inference.

## Key equations
$$H_{\text{SK}}=-\frac{1}{\sqrt N}\sum_{i<j}J_{ij}s_is_j,\ J_{ij}\sim\mathcal N(0,J^2);\qquad \overline{\ln Z}=\lim_{n\to0}\frac{\overline{Z^n}-1}{n}$$

## Landmark papers
- Anderson (1958). "Absence of Diffusion in Certain Random Lattices". *Phys. Rev.* 109, 1492. [doi:10.1103/PhysRev.109.1492](https://doi.org/10.1103/PhysRev.109.1492)
- Broadbent & Hammersley (1957). "Percolation processes: I. Crystals and mazes". *Math. Proc. Camb. Phil. Soc.* 53, 629. [doi:10.1017/S0305004100032680](https://doi.org/10.1017/S0305004100032680)
- Edwards & Anderson (1975). "Theory of spin glasses". *J. Phys. F* 5, 965. [doi:10.1088/0305-4608/5/5/017](https://doi.org/10.1088/0305-4608/5/5/017)
- Sherrington & Kirkpatrick (1975). "Solvable Model of a Spin-Glass". *Phys. Rev. Lett.* 35, 1792. [doi:10.1103/PhysRevLett.35.1792](https://doi.org/10.1103/PhysRevLett.35.1792)
- Parisi (1979). "Infinite Number of Order Parameters for Spin-Glasses". *Phys. Rev. Lett.* 43, 1754. [doi:10.1103/PhysRevLett.43.1754](https://doi.org/10.1103/PhysRevLett.43.1754)
- Hopfield (1982). "Neural networks and physical systems with emergent collective computational abilities". *Proc. Natl. Acad. Sci.* 79, 2554. [doi:10.1073/pnas.79.8.2554](https://doi.org/10.1073/pnas.79.8.2554)
- Ackley, Hinton & Sejnowski (1985). "A Learning Algorithm for Boltzmann Machines". *Cognitive Science* 9, 147. [doi:10.1207/s15516709cog0901_7](https://doi.org/10.1207/s15516709cog0901_7)
- Watts & Strogatz (1998). "Collective dynamics of 'small-world' networks". *Nature* 393, 440. [doi:10.1038/30918](https://doi.org/10.1038/30918)
- Barabási & Albert (1999). "Emergence of Scaling in Random Networks". *Science* 286, 509. [doi:10.1126/science.286.5439.509](https://doi.org/10.1126/science.286.5439.509)
- Basko, Aleiner & Altshuler (2006). "Metal–insulator transition in a weakly interacting many-electron system with localized single-particle states". *Ann. Phys.* 321, 1126. [arXiv:cond-mat/0506617](https://arxiv.org/abs/cond-mat/0506617)

## Open problems
- The nature of the structural glass transition (thermodynamic or purely dynamic?).
- Theory of generalization in overparameterized deep networks.

## Connections
- [Glasses and jamming](../../08-condensed-matter/soft-matter/glasses-and-jamming/README.md) · [Machine learning for physics](../../00-foundations/computational-physics/machine-learning-for-physics/README.md)
