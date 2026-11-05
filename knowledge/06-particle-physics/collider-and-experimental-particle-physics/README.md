---
title: Collider and experimental particle physics
summary: Accelerators, detectors, event simulation and data analysis — how particle physics is measured.
query: collider physics; LHC experiments
arxiv: hep-ex physics.ins-det hep-ph
---
# Collider and experimental particle physics

> Part of [Particle Physics](../README.md) · Key reviews: [papers.md](papers.md)

## Overview
Experimental particle physics turns collisions into measurements: accelerators deliver beams, detectors record charged tracks and calorimeter deposits, triggers select ~1 in $10^5$ events, and reconstruction plus simulation turn raw hits into physics objects (electrons, muons, jets, missing energy). The LHC (13.6 TeV, Run 3; HL-LHC from ~2030) dominates the energy frontier.

## Topics
- [Hadron colliders and the LHC](hadron-colliders-and-the-lhc/README.md) — machine, luminosity, pile-up, physics program.
- [Jets and QCD phenomenology](jets-and-qcd-phenomenology/README.md) — jet algorithms, parton showers, substructure.
- [Monte Carlo event generators](monte-carlo-event-generators/README.md) — PYTHIA, Herwig, Sherpa, MadGraph.
- [Particle detectors and triggers](particle-detectors-and-triggers/README.md) — trackers, calorimeters, muon systems.
- [Future colliders](future-colliders/README.md) — FCC, CEPC, ILC, CLIC, muon collider.
- [Machine learning in HEP](machine-learning-in-hep/README.md) — tagging, simulation, anomaly detection.

## Conceptual spine
1. Event rate $=\sigma\times\mathcal L$; integrated luminosity sets statistics.
2. Factorization: $\sigma_{pp\to X}=\sum_{ij}\int f_i f_j\,\hat\sigma_{ij\to X}$ (PDFs × partonic cross section).
3. Reconstruction → selection → background estimation (data-driven where possible) → statistical inference (profile likelihood, CLs).
4. Blind analyses and look-elsewhere corrections guard against false discoveries.

## Key equations
$$N=\sigma\int\mathcal L\,dt,\qquad \sigma_{pp\to X}=\sum_{i,j}\int dx_1dx_2\,f_i(x_1,\mu_F)f_j(x_2,\mu_F)\,\hat\sigma_{ij\to X}(\hat s,\mu_R)$$

## Landmark papers
- Evans & Bryant (2008). "LHC Machine". *JINST* 3, S08001. [doi:10.1088/1748-0221/3/08/S08001](https://doi.org/10.1088/1748-0221/3/08/S08001)
- ATLAS Collaboration (2008). "The ATLAS Experiment at the CERN Large Hadron Collider". *JINST* 3, S08003. [doi:10.1088/1748-0221/3/08/S08003](https://doi.org/10.1088/1748-0221/3/08/S08003)
- CMS Collaboration (2008). "The CMS experiment at the CERN LHC". *JINST* 3, S08004. [doi:10.1088/1748-0221/3/08/S08004](https://doi.org/10.1088/1748-0221/3/08/S08004)
- Cacciari, Salam & Soyez (2008). "The anti-k_t jet clustering algorithm". *JHEP* 04, 063. [arXiv:0802.1189](https://arxiv.org/abs/0802.1189)
- Sjöstrand et al. (2015). "An introduction to PYTHIA 8.2". *Comput. Phys. Commun.* 191, 159. [arXiv:1410.3012](https://arxiv.org/abs/1410.3012)
- Alwall et al. (2014). "The automated computation of tree-level and next-to-leading order differential cross sections, and their matching to parton shower simulations". *JHEP* 07, 079. [arXiv:1405.0301](https://arxiv.org/abs/1405.0301)

## Open problems
- Pile-up of ~200 collisions per crossing at HL-LHC; real-time triggering with ML on FPGAs.
- Theory uncertainties (PDFs, higher orders) now rival experimental ones for precision Higgs and EW measurements.

## Connections
- [Accelerator physics](../../11-interdisciplinary-physics/accelerator-physics/README.md) · [Statistical inference](../../00-foundations/measurement-and-data-analysis/statistical-inference-in-physics/README.md) · [Detectors and instrumentation](../../00-foundations/measurement-and-data-analysis/detectors-and-instrumentation/README.md)
