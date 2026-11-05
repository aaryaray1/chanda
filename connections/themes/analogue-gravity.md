---
title: Analogue gravity — horizons in fluids and condensates
summary: Sound in a flowing fluid propagates on an effective curved spacetime; where the flow outruns sound there is a horizon that should emit thermal phonons — a laboratory test of the kinematics behind Hawking radiation.
fields: 05 04 01 03
kind: analogy
---
# Analogue gravity — horizons in fluids and condensates
> Curated theme · [Connections atlas](../../CONNECTIONS.md) · Kind: analogy

**The bridge.** Unruh (1981) showed that small perturbations of an inviscid, irrotational, barotropic flow obey the wave equation of a massless field in an effective *acoustic metric*. Where the flow speed exceeds the sound speed, sound cannot escape upstream: this is a sonic horizon. Hawking's derivation uses only the kinematics of fields on a background with a horizon, not Einstein's equations. So such a horizon should radiate thermal phonons, at a temperature set by the velocity gradient there.

Analogues therefore test the robustness of Hawking radiation, including the *trans-Planckian problem*. In a fluid the short-distance physics is known: dispersion sets in at the healing length. Bose–Einstein condensates are the cleanest platform, and a 2016 experiment reported spontaneous Hawking radiation together with its entanglement. *Kinematic correspondence: established. Experimental observation: current research, with its interpretation debated.*

**How each branch sees it.**
- **Relativity:**
  - [Black-hole thermodynamics and Hawking radiation](../../knowledge/05-relativity-and-gravitation/black-holes/black-hole-thermodynamics-and-hawking-radiation/README.md).
  - [QFT in curved spacetime](../../knowledge/05-relativity-and-gravitation/quantum-gravity/qft-in-curved-spacetime/README.md).
- **Classical mechanics:** [Ideal and viscous flow](../../knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow/README.md) supplies the acoustic metric from the linearized Euler equations.
- **AMO physics:** [BECs and degenerate gases](../../knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases/README.md). Bogoliubov phonons play the quantum field, and the healing length sets the cutoff.
- **Statistical mechanics:** [Entropy and information](../../knowledge/03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information/README.md). What a thermal spectrum, and the entanglement across a horizon, mean.

**Shared structure.**
$$ds^2=\frac{\rho}{c_s}\Big[-c_s^2\,dt^2+(d\mathbf x-\mathbf v\,dt)^2\Big],\qquad T=\frac{\hbar\kappa}{2\pi k_B},\qquad \kappa=\Big|\frac{d(|v|-c_s)}{dx}\Big|_{\text{horizon}}\ \text{(1D flow)}$$
The Schwarzschild case is $\kappa=c^4/(4GM)$ in units where $T=\hbar\kappa/(2\pi ck_B)$, which gives $T_H=\hbar c^3/(8\pi GMk_B)$.

**Symbol map.**

| Fluid or condensate | Gravity |
|---|---|
| sound speed $c_s$ | light speed $c$ |
| flow velocity $\mathbf v$ | shift vector (frame dragging into the hole) |
| sonic horizon | event horizon |
| velocity gradient $\kappa$ | surface gravity |
| phonons | quantum fields |
| healing length | Planck length (trans-Planckian physics) |

**Where it breaks.**
- *Kinematics only.* The acoustic metric is set by the flow, which obeys fluid equations, not Einstein's. Backreaction and black-hole dynamics are not reproduced.
- *Lorentz violation.* Bogoliubov dispersion breaks Lorentz invariance at short scales. Remarkably, the thermal flux survives.
- *Weak signals.* Temperatures are around nK and sit on top of thermal and technical noise, so separating the spontaneous signal is hard. Entropy and information analogues are not obviously meaningful.

**Landmarks.**
- Hawking (1975). "Particle creation by black holes". *Commun. Math. Phys.* 43, 199. [doi:10.1007/BF02345020](https://doi.org/10.1007/BF02345020)
- Unruh (1976). "Notes on black-hole evaporation". *Phys. Rev. D* 14, 870. [doi:10.1103/PhysRevD.14.870](https://doi.org/10.1103/PhysRevD.14.870)
- Unruh (1981). "Experimental Black-Hole Evaporation?". *Phys. Rev. Lett.* 46, 1351. [doi:10.1103/PhysRevLett.46.1351](https://doi.org/10.1103/PhysRevLett.46.1351)
- Barceló, Liberati & Visser (2005). "Analogue Gravity". *Living Rev. Relativ.* 8, 12. [arXiv:gr-qc/0505065](https://arxiv.org/abs/gr-qc/0505065)
- Steinhauer (2016). "Observation of quantum Hawking radiation and its entanglement in an analogue black hole". *Nature Phys.* 12, 959. [arXiv:1510.00621](https://arxiv.org/abs/1510.00621)

**Open questions.** Can analogue experiments settle the role of short-distance physics in Hawking radiation? Can they be extended to backreaction, superradiance and cosmological particle creation? What, if anything, do they say about information loss?
