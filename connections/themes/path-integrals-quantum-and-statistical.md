---
title: Path integrals — quantum amplitudes and partition functions
summary: Rotating time to imaginary values turns Feynman's sum over histories into a Boltzmann-weighted partition function, so quantum field theory in D dimensions becomes classical statistical mechanics in D dimensions — the basis of lattice QCD, quantum Monte Carlo and instanton physics.
fields: 04 03 06 00
kind: identity · method transfer
---
# Path integrals — quantum amplitudes and partition functions
> Curated theme · [Connections atlas](../../CONNECTIONS.md) · Kind: identity, method transfer

**The bridge.** Feynman's path integral writes a quantum amplitude as a sum over histories, each weighted by $e^{iS/\hbar}$. Setting $t=-i\tau$ (the Wick rotation) turns the weight into $e^{-S_E/\hbar}$, which is a Boltzmann factor. This yields two exact equivalences:
- **QM at finite temperature.** A quantum system at temperature $T$ is a path integral over histories periodic in imaginary time, with period $\hbar\beta$.
- **QFT as statistical mechanics.** A quantum field theory in $D$ Euclidean dimensions is a classical statistical model in $D$ dimensions. A quantum chain in $d$ dimensions maps to a classical model in $d+1$, e.g. the transverse-field Ising chain and the 2D classical Ising model.

Uses:
- Wilson's lattice gauge theory makes QCD a Monte Carlo problem.
- Quantum Monte Carlo is the same trick applied to quantum many-body systems.
- Tunnelling rates come from Euclidean saddle points (instantons).

*Established.*

**How each branch sees it.**
- **Quantum physics:** [Path integrals and semiclassics](../../knowledge/04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics/README.md).
- **Statistical mechanics:**
  - [Ensembles and partition functions](../../knowledge/03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions/README.md).
  - [Ising and lattice models](../../knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/ising-model-and-lattice-models/README.md).
- **Particle physics:**
  - [Canonical and path-integral quantization](../../knowledge/06-particle-physics/quantum-field-theory/canonical-and-path-integral-quantization/README.md).
  - [Lattice field theory](../../knowledge/06-particle-physics/quantum-field-theory/lattice-field-theory/README.md).
  - [Anomalies, instantons and topology](../../knowledge/06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology/README.md).
- **Foundations:** [Monte Carlo methods](../../knowledge/00-foundations/computational-physics/monte-carlo-methods/README.md), which sample $e^{-S_E}$ by importance sampling.

**Shared structure.**
$$\langle x_f|e^{-iHt/\hbar}|x_i\rangle=\int\mathcal Dx\;e^{iS[x]/\hbar}\quad\xrightarrow{\;t=-i\tau\;}\quad Z=\operatorname{Tr}e^{-\beta H}=\oint_{x(0)=x(\hbar\beta)}\mathcal Dx\;e^{-S_E[x]/\hbar}$$

**Symbol map.**

| Quantum field theory | Statistical mechanics |
|---|---|
| Euclidean action $S_E$ | energy functional $H$ |
| $\hbar$ | $k_BT$ (sets the size of fluctuations) |
| extent of imaginary time, $\hbar\beta$ | thickness of the classical slab |
| mass gap | inverse correlation length |
| tunnelling instanton | domain wall / droplet |

**Where it breaks.**
- *The sign problem.* With fermions at finite density, frustrated magnets or real-time dynamics, the weights are complex or not positive and Monte Carlo fails. QCD at finite baryon density is the flagship example.
- *Analytic continuation.* Recovering real-frequency spectra from imaginary-time data is ill-posed.
- *The reverse map needs reflection positivity.* Not every statistical model is a unitary quantum theory.

**Landmarks.**
- Feynman (1948). "Space-Time Approach to Non-Relativistic Quantum Mechanics". *Rev. Mod. Phys.* 20, 367. [doi:10.1103/RevModPhys.20.367](https://doi.org/10.1103/RevModPhys.20.367)
- Wilson (1974). "Confinement of quarks". *Phys. Rev. D* 10, 2445. [doi:10.1103/PhysRevD.10.2445](https://doi.org/10.1103/PhysRevD.10.2445)
- Wilson & Kogut (1974). "The renormalization group and the ε expansion". *Phys. Rep.* 12, 75. [doi:10.1016/0370-1573(74)90023-4](https://doi.org/10.1016/0370-1573(74)90023-4)

**Open questions.** Can the sign problem be solved in general? It is believed NP-hard for generic models, though special structure helps. Can quantum computers simulate real-time and finite-density QCD where Monte Carlo cannot?
