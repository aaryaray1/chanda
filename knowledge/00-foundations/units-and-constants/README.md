---
title: Units, constants and dimensional analysis
summary: The SI system and its 2019 redefinition, CODATA fundamental constants, dimensional analysis and scaling, natural and Planck units.
query: SI units; fundamental physical constants
arxiv: physics.atom-ph physics.gen-ph
---
# Units, constants and dimensional analysis

> Part of [Foundations](../README.md) · Key reviews: [papers.md](papers.md) · **Full CODATA 2022 table:** [codata-2022.md](codata-2022.md)

## Overview
Since 20 May 2019 all seven SI base units are defined by fixing exact values of seven constants ($\Delta\nu_{\text{Cs}}$, $c$, $h$, $e$, $k_B$, $N_A$, $K_{cd}$). Other constants (e.g. $G$, $\alpha$, $m_e$) are measured, and CODATA publishes adjusted recommended values. Dimensional analysis — checking and exploiting units — is the cheapest error check in physics.

## Topics
- [SI units and the 2019 redefinition](si-units-and-2019-redefinition/README.md) — the seven defining constants.
- [Fundamental constants](fundamental-constants/README.md) — CODATA, the fine-structure constant, $G$, tests of constancy.
- [Dimensional analysis and scaling](dimensional-analysis-and-scaling/README.md) — Buckingham π, scaling laws, Fermi estimates.
- [Natural units and the Planck scale](natural-units-and-planck-scale/README.md) — $\hbar=c=1$, geometrized, atomic and Planck units.

## Key exact values (SI 2019)
$$c=299\,792\,458\ \text{m s}^{-1},\quad h=6.626\,070\,15\times10^{-34}\ \text{J s},\quad e=1.602\,176\,634\times10^{-19}\ \text{C}$$
$$k_B=1.380\,649\times10^{-23}\ \text{J K}^{-1},\quad N_A=6.022\,140\,76\times10^{23}\ \text{mol}^{-1},\quad \Delta\nu_{\text{Cs}}=9\,192\,631\,770\ \text{Hz}$$

Look up any other value with `python -I scripts/physlib.py constants "<name>"` (e.g. `constants "fine-structure"`).

## Landmark papers
- Buckingham (1914). "On Physically Similar Systems; Illustrations of the Use of Dimensional Equations". *Phys. Rev.* 4, 345. [doi:10.1103/PhysRev.4.345](https://doi.org/10.1103/PhysRev.4.345)
- Robinson & Schlamminger (2016). "The watt or Kibble balance: a technique for implementing the new SI definition of the unit of mass". *Metrologia* 53, A46. [doi:10.1088/0026-1394/53/5/A46](https://doi.org/10.1088/0026-1394/53/5/A46)
- Stock et al. (2019). "The revision of the SI—the result of three decades of progress in metrology". *Metrologia* 56, 022001. [doi:10.1088/1681-7575/ab0013](https://doi.org/10.1088/1681-7575/ab0013)
- Tiesinga et al. (2021). "CODATA recommended values of the fundamental physical constants: 2018". *Rev. Mod. Phys.* 93, 025010. [doi:10.1103/RevModPhys.93.025010](https://doi.org/10.1103/RevModPhys.93.025010)
- Morel et al. (2020). "Determination of the fine-structure constant with an accuracy of 81 parts per trillion". *Nature* 588, 61. [doi:10.1038/s41586-020-2964-7](https://doi.org/10.1038/s41586-020-2964-7)

## Open problems
- The Newtonian constant $G$ is known only to ~22 ppm, with mutually inconsistent measurements.
- The 5σ disagreement between Cs- and Rb-based determinations of $\alpha$.
- Redefinition of the second with optical clocks.

## Connections
- [Atomic clocks](../../04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement/README.md) · [Uncertainty](../measurement-and-data-analysis/uncertainty-and-error-propagation/README.md)
