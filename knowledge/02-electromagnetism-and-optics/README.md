---
title: Electromagnetism and Optics
summary: Electric and magnetic fields, Maxwell's equations, electromagnetic radiation and scattering, classical optics, and modern photonics and lasers.
arxiv: physics.class-ph physics.optics
source: openalex
agent: em-optics-physicist
---
# Electromagnetism and Optics

> **Specialist:** `em-optics-physicist` · **arXiv:** physics.class-ph, physics.optics, physics.app-ph · **Literature source:** OpenAlex + arXiv

## What this field studies
Maxwell's four equations, with the Lorentz force law, describe all classical electric, magnetic and optical phenomena — from capacitors to radio, from rainbows to lasers. Light is an electromagnetic wave; optics is electromagnetism at wavelengths from ~400 to ~700 nm (and beyond). Modern photonics engineers light in structured materials, generates attosecond pulses, and carries the world's data through optical fibre.

## Branch map
| Branch | What it covers |
|---|---|
| [Electrostatics and magnetostatics](electrostatics-and-magnetostatics/README.md) | Gauss/Poisson, boundary-value problems, multipoles, Biot–Savart, fields in matter |
| [Electrodynamics](electrodynamics/README.md) | Maxwell's equations, EM waves and waveguides, potentials and gauges, covariant form |
| [Radiation and scattering](radiation-and-scattering/README.md) | Dipole radiation, radiation from moving charges, scattering of light, Cherenkov radiation |
| [Classical optics](classical-optics/README.md) | Geometric optics, interference/diffraction, polarization, Fourier optics, coherence |
| [Photonics and lasers](photonics-and-lasers/README.md) | Lasers, nonlinear and ultrafast optics, integrated photonics, metamaterials, topological photonics |

## Conventions used in this branch
- **SI units** by default ($\epsilon_0$, $\mu_0$, $c^2=1/\epsilon_0\mu_0$). Jackson and many plasma/astro texts use **Gaussian** units: $\mathbf F=q(\mathbf E+\frac{\mathbf v}{c}\times\mathbf B)$, $\nabla\cdot\mathbf E=4\pi\rho$. Always state which.
- Time-harmonic fields as $\mathrm{Re}[\mathbf E_0e^{i(\mathbf k\cdot\mathbf r-\omega t)}]$ (physics convention); engineers use $e^{j\omega t}$ — signs of imaginary parts flip.
- Refractive index $n=\sqrt{\epsilon_r\mu_r}$; complex $\tilde n=n+i\kappa$ with absorption.

## Historical spine
1785 Coulomb's law · 1820 Ørsted, Biot–Savart, Ampère · 1831 Faraday's induction · 1865 Maxwell's dynamical theory · 1887 Hertz detects radio waves · 1897 Larmor formula · 1905 special relativity from electrodynamics · 1934 Cherenkov radiation · 1948 holography · 1960 the laser · 1961 second-harmonic generation · 1966 low-loss optical fibre proposed · 1985 chirped-pulse amplification · 2000 negative-index metamaterials · 2001 attosecond pulses · 2009 topological photonic edge states · 2023 Nobel Prize for attosecond physics.

## Canonical textbooks
- Griffiths, *Introduction to Electrodynamics* — undergraduate standard.
- Jackson, *Classical Electrodynamics* — the graduate reference (Gaussian in 2nd ed., SI in early chapters of 3rd).
- Zangwill, *Modern Electrodynamics* — modern graduate alternative.
- Hecht, *Optics*; Born & Wolf, *Principles of Optics*; Saleh & Teich, *Fundamentals of Photonics*; Boyd, *Nonlinear Optics*; Siegman, *Lasers*.

## Live frontiers
- Attosecond science and petahertz electronics.
- Integrated photonics for quantum and AI hardware; frequency microcombs.
- Topological, non-Hermitian and time-varying photonic media.

## How the specialist works here
Exploit symmetry (Gauss, Ampère), choose the right potential formulation and gauge, check boundary conditions at every interface, verify with energy conservation (Poynting) and limiting cases ($\omega\to0$, far field, $v\ll c$), and be explicit about units.
