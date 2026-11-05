---
title: Density functional theory
summary: First-principles electronic structure from the electron density — Hohenberg–Kohn theorems, Kohn–Sham equations, exchange–correlation functionals and their limits.
query: density functional theory; exchange-correlation functional; first-principles calculation
openalex_filter: primary_topic.field.id:31|25|16
---
# Density functional theory
> [Condensed Matter Physics](../../README.md) › [Crystals and electronic structure](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Hohenberg–Kohn theorems, Kohn–Sham auxiliary system, LDA, GGA (PBE), meta-GGA (SCAN), hybrid functionals (HSE), DFT+U, van der Waals corrections, band-gap problem, plane waves and pseudopotentials, PAW, TDDFT, GW and DMFT beyond DFT, high-throughput materials databases, ML potentials trained on DFT.

**Core ideas.**
- The ground-state density uniquely determines all properties; the energy is minimized by the true density.
- Kohn–Sham maps the interacting problem onto non-interacting electrons in an effective potential — exact if $E_{xc}$ were known.
- Semi-local functionals underestimate band gaps and fail for strongly correlated (Mott) systems.

**Key equations.**
$$\left[-\frac{\hbar^2}{2m}\nabla^2+v_{\text{ext}}+v_H[n]+v_{xc}[n]\right]\phi_i=\varepsilon_i\phi_i,\qquad n(\mathbf r)=\sum_i^{\text{occ}}|\phi_i|^2$$

**Landmarks.** Hohenberg & Kohn (1964); Kohn & Sham (1965); Perdew, Burke & Ernzerhof (1996) — see [subfield landmarks](../README.md).

**See also.** [Quantum chemistry methods](../../../11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods/README.md) · [Numerical many-body methods](../../strongly-correlated-electrons/numerical-many-body-methods/README.md)
