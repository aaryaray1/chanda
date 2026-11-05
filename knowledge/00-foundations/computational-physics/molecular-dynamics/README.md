---
title: Molecular dynamics
summary: Simulating many interacting particles by integrating their equations of motion — force fields, thermostats and ab initio MD.
query: molecular dynamics simulation; force field; ab initio molecular dynamics
---
# Molecular dynamics
> [Foundations](../../README.md) › [Computational physics](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Lennard-Jones and empirical force fields, Verlet integration, periodic boundaries and Ewald sums, thermostats (Nosé–Hoover, Langevin) and barostats, Car–Parrinello and Born–Oppenheimer ab initio MD, machine-learned interatomic potentials, enhanced sampling (metadynamics).

**Core ideas.**
- Time averages along ergodic trajectories estimate ensemble averages.
- Long-range Coulomb forces need Ewald/PME summation.
- ML potentials give near-DFT accuracy at near-classical cost.

**Key equations.**
$$V_{\text{LJ}}(r)=4\epsilon\left[\left(\frac\sigma r\right)^{12}-\left(\frac\sigma r\right)^6\right]$$

**Landmarks.** Alder & Wainwright (1957); Verlet (1967) — see [subfield landmarks](../README.md).

**See also.** [Molecular biophysics](../../../11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding/README.md) · [Glasses and jamming](../../../08-condensed-matter/soft-matter/glasses-and-jamming/README.md)
