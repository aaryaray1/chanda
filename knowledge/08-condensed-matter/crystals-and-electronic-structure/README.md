---
title: Crystals and electronic structure
summary: Periodic solids and their electrons — crystal lattices and diffraction, band theory, phonons, semiconductors, density functional theory, and electronic transport.
query: electronic structure of solids; band theory
---
# Crystals and electronic structure

> Part of [Condensed Matter Physics](../README.md) · Key reviews: [papers.md](papers.md)

## Overview
Translational symmetry organizes electrons and lattice vibrations into bands labelled by crystal momentum. Whether the Fermi level falls in a band or a gap decides metal vs. insulator; small gaps make semiconductors, the basis of electronics. DFT computes band structures from first principles for real materials; transport theory connects bands to measurable conductivities.

## Topics
- [Crystal structure and diffraction](crystal-structure-and-diffraction/README.md) — lattices, reciprocal space, Bragg's law, X-ray and neutron scattering.
- [Band theory and Bloch electrons](band-theory-and-bloch-electrons/README.md) — Bloch's theorem, nearly-free and tight-binding models, Fermi surfaces.
- [Phonons and lattice dynamics](phonons-and-lattice-dynamics/README.md) — vibrations, specific heat, thermal conductivity.
- [Semiconductors](semiconductors/README.md) — doping, carriers, p–n junctions, devices.
- [Density functional theory](density-functional-theory/README.md) — Hohenberg–Kohn, Kohn–Sham, functionals, materials prediction.
- [Electronic transport and mesoscopic physics](electronic-transport-and-mesoscopic-physics/README.md) — Drude, Boltzmann, Landauer, quantized conductance.

## Key equations
$$\psi_{n\mathbf k}(\mathbf r+\mathbf R)=e^{i\mathbf k\cdot\mathbf R}\psi_{n\mathbf k}(\mathbf r),\qquad 2d\sin\theta=n\lambda,\qquad \sigma=\frac{ne^2\tau}{m^*}$$

## Landmark papers
- Bloch (1929). "Über die Quantenmechanik der Elektronen in Kristallgittern". *Z. Phys.* 52, 555. [doi:10.1007/BF01339455](https://doi.org/10.1007/BF01339455)
- Bardeen & Brattain (1948). "The Transistor, A Semi-Conductor Triode". *Phys. Rev.* 74, 230. [doi:10.1103/PhysRev.74.230](https://doi.org/10.1103/PhysRev.74.230)
- Landauer (1957). "Spatial Variation of Currents and Fields Due to Localized Scatterers in Metallic Conduction". *IBM J. Res. Dev.* 1, 223. [doi:10.1147/rd.13.0223](https://doi.org/10.1147/rd.13.0223)
- Hohenberg & Kohn (1964). "Inhomogeneous Electron Gas". *Phys. Rev.* 136, B864. [doi:10.1103/PhysRev.136.B864](https://doi.org/10.1103/PhysRev.136.B864)
- Kohn & Sham (1965). "Self-Consistent Equations Including Exchange and Correlation Effects". *Phys. Rev.* 140, A1133. [doi:10.1103/PhysRev.140.A1133](https://doi.org/10.1103/PhysRev.140.A1133)
- van Wees et al. (1988). "Quantized conductance of point contacts in a two-dimensional electron gas". *Phys. Rev. Lett.* 60, 848. [doi:10.1103/PhysRevLett.60.848](https://doi.org/10.1103/PhysRevLett.60.848)
- Perdew, Burke & Ernzerhof (1996). "Generalized Gradient Approximation Made Simple". *Phys. Rev. Lett.* 77, 3865. [doi:10.1103/PhysRevLett.77.3865](https://doi.org/10.1103/PhysRevLett.77.3865)

## Open problems
- Predictive first-principles theory for strongly correlated materials (where DFT fails).
- Materials discovery at scale with ML-accelerated electronic-structure methods.

## Connections
- [Quantum statistics](../../03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics/README.md) · [Semiconductor devices](../../11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics/README.md) · [Coupled oscillators](../../01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes/README.md)
