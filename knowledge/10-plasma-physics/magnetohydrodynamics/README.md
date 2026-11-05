---
title: Magnetohydrodynamics
summary: Plasmas and conducting fluids as magnetized fluids — ideal MHD and Alfvén waves, magnetic reconnection, dynamos and MHD turbulence.
query: magnetohydrodynamics; MHD
arxiv: physics.plasm-ph astro-ph.SR physics.flu-dyn
---
# Magnetohydrodynamics

> Part of [Plasma Physics](../README.md) · Key reviews: [papers.md](papers.md)

## Overview
On scales much larger than ion gyroradii and slower than ion cyclotron frequencies, a plasma behaves as a single conducting fluid coupled to the magnetic field. In ideal MHD, field lines are "frozen" into the flow; magnetic tension and pressure produce Alfvén and magnetosonic waves. Non-ideal effects allow reconnection, which releases magnetic energy explosively in solar flares and tokamak disruptions, and dynamos, which generate the fields of planets, stars and galaxies.

## Topics
- [Ideal MHD and Alfvén waves](ideal-mhd-and-alfven-waves/README.md) — frozen-in flux, waves, equilibrium and stability.
- [Magnetic reconnection](magnetic-reconnection/README.md) — Sweet–Parker, fast reconnection, plasmoids, MMS.
- [Dynamo theory](dynamo-theory/README.md) — kinematic and mean-field dynamos, solar and geodynamo.
- [MHD turbulence](mhd-turbulence/README.md) — Alfvénic cascades, anisotropy, solar-wind turbulence.

## Key equations
$$\frac{\partial\mathbf B}{\partial t}=\nabla\times(\mathbf v\times\mathbf B)+\eta\nabla^2\mathbf B,\qquad \rho\frac{D\mathbf v}{Dt}=-\nabla p+\frac{(\nabla\times\mathbf B)\times\mathbf B}{\mu_0},\qquad v_A=\frac{B}{\sqrt{\mu_0\rho}}$$

## Landmark papers
- Alfvén (1942). "Existence of Electromagnetic-Hydrodynamic Waves". *Nature* 150, 405. [doi:10.1038/150405d0](https://doi.org/10.1038/150405d0)
- Parker (1955). "Hydromagnetic Dynamo Models". *Astrophys. J.* 122, 293. [doi:10.1086/146087](https://doi.org/10.1086/146087)
- Parker (1957). "Sweet's mechanism for merging magnetic fields in conducting fluids". *J. Geophys. Res.* 62, 509. [doi:10.1029/JZ062i004p00509](https://doi.org/10.1029/JZ062i004p00509)
- Balbus & Hawley (1991). "A Powerful Local Shear Instability in Weakly Magnetized Disks. I. Linear Analysis". *Astrophys. J.* 376, 214. [doi:10.1086/170270](https://doi.org/10.1086/170270)
- Goldreich & Sridhar (1995). "Toward a theory of interstellar turbulence. 2: Strong Alfvénic turbulence". *Astrophys. J.* 438, 763. [doi:10.1086/175121](https://doi.org/10.1086/175121)
- Burch et al. (2016). "Electron-scale measurements of magnetic reconnection in space". *Science* 352, aaf2939. [doi:10.1126/science.aaf2939](https://doi.org/10.1126/science.aaf2939)

## Open problems
- Why is reconnection fast (~0.01–0.1 $v_A$) regardless of resistivity?
- Coronal heating: waves, nanoflares, or both?

## Connections
- [Fluid mechanics](../../01-classical-mechanics/continuum-and-fluid-mechanics/README.md) · [The Sun](../../09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology/README.md) · [Planet formation (MRI)](../../09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks/README.md)
