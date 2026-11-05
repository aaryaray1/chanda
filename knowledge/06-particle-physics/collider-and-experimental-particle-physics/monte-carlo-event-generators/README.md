---
title: Monte Carlo event generators
summary: Simulating full collision events from hard scattering through parton showers and hadronization.
query: event generator; parton shower Monte Carlo; hadronization
---
# Monte Carlo event generators
> [Particle Physics](../../README.md) › [Collider & experimental](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Matrix-element generators (MadGraph5_aMC@NLO), general-purpose generators (PYTHIA, Herwig, Sherpa), NLO matching (MC@NLO, POWHEG), merging (CKKW, MLM), hadronization models (Lund string, cluster), underlying event and tuning, detector simulation (Geant4).

**Core ideas.**
- Factorize the event into hard process (fixed order), shower (resummed soft/collinear emissions), hadronization (non-perturbative model), decays.
- Matching avoids double counting between fixed-order and shower emissions.
- Generators are both theory tools and the backbone of every analysis's background model.

**Key equations.**
$$\Delta(t_1,t_2)=\exp\!\left[-\int_{t_2}^{t_1}\frac{dt}{t}\int dz\,\frac{\alpha_s}{2\pi}P(z)\right]\ (\text{Sudakov factor})$$

**Landmarks.** PYTHIA 8.2 (2015); MadGraph5_aMC@NLO (2014) — see [subfield landmarks](../README.md).

**See also.** [Monte Carlo methods](../../../00-foundations/computational-physics/monte-carlo-methods/README.md)
