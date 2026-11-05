---
title: Symmetry breaking and the Higgs–Anderson mechanism
summary: A superconductor and the electroweak vacuum are the same kind of state — a condensate that hides a gauge symmetry, gives the gauge field a mass and turns the would-be Goldstone mode into its longitudinal polarization.
fields: 00 03 06 08
kind: mechanism · historical
---
# Symmetry breaking and the Higgs–Anderson mechanism
> Curated theme · [Connections atlas](../../CONNECTIONS.md) · Kind: mechanism, historical

**The bridge.** When a ground state breaks a continuous symmetry, Goldstone's theorem predicts one gapless mode per broken generator. If that symmetry is gauged, the mode does not survive. It becomes the longitudinal polarization of the gauge field, and the field acquires a mass. In a superconductor this is the Meissner effect: inside the condensate the photon is massive, so a static field decays over the London depth $\lambda_L$. In the Standard Model the same mechanism gives the W and Z their masses. Nambu (1960) used the gauge invariance of BCS theory to see the broken symmetry. Anderson (1963) argued that long-range gauge fields remove the massless Goldstone mode, and pointed to particle physics. Englert & Brout and Higgs (1964) wrote the relativistic version. *Established.*

**How each branch sees it.**
- **Foundations:** [Spontaneous symmetry breaking](../../knowledge/00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking/README.md) covers order parameters and Goldstone's theorem.
- **Statistical mechanics:** [Mean-field and Landau theory](../../knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory/README.md). Ginzburg–Landau theory is the static Abelian Higgs model.
- **Condensed matter:** [BCS theory](../../knowledge/08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors/README.md). The condensate of charge-$2e$ Cooper pairs expels flux. In a charged superfluid the phase mode is lifted to the plasma frequency.
- **Particle physics:** [Electroweak theory](../../knowledge/06-particle-physics/standard-model/electroweak-theory/README.md) and the [Higgs boson](../../knowledge/06-particle-physics/standard-model/higgs-boson/README.md). The doublet vacuum expectation value is $v\approx246$ GeV, giving $m_W=gv/2$. The Higgs boson is the condensate's amplitude mode.

**Shared structure.** The Ginzburg–Landau free energy (SI) is
$$F=\int d^3x\left[\frac{|(-i\hbar\nabla-q\mathbf A)\psi|^2}{2m^*}+a|\psi|^2+\frac b2|\psi|^4+\frac{(\nabla\times\mathbf A)^2}{2\mu_0}\right]$$
With $|\psi|^2=n_s$, the cross term $q^2n_s\mathbf A^2/2m^*$ is a photon mass term, giving $\lambda_L^{-2}=\mu_0n_sq^2/m^*$. The relativistic analogue $|D_\mu\phi|^2$ with $\langle\phi\rangle=v/\sqrt2$ contains $\tfrac12q^2v^2A_\mu A^\mu$, so $m_A=qv$ in natural units.

**Symbol map.**

| Superconductor | Higgs sector |
|---|---|
| $\psi$ | $\phi$ |
| $n_s$ | $v^2$ |
| $q=2e$ | gauge coupling |
| $\hbar/(\lambda_Lc)$ | $m_A$ |
| GL amplitude mode at $2\Delta$ | Higgs boson |

**Where it breaks.**
- The superconducting condensate is a composite of Cooper pairs, much larger than the interparticle spacing, and non-relativistic. Whether the Higgs is elementary is open.
- A superconductor has a rest frame. Its amplitude mode sits at the pair-breaking edge $2\Delta$, so it readily decays into quasiparticles and is hard to observe.
- "Breaking a gauge symmetry" is shorthand: a local gauge redundancy cannot break spontaneously (Elitzur's theorem). What is physical is the gauge-invariant mass gap.

**Landmarks.**
- Bardeen, Cooper & Schrieffer (1957). "Theory of Superconductivity". *Phys. Rev.* 108, 1175. [doi:10.1103/PhysRev.108.1175](https://doi.org/10.1103/PhysRev.108.1175)
- Nambu (1960). "Quasi-Particles and Gauge Invariance in the Theory of Superconductivity". *Phys. Rev.* 117, 648. [doi:10.1103/PhysRev.117.648](https://doi.org/10.1103/PhysRev.117.648)
- Goldstone (1961). "Field theories with Superconductor solutions". *Nuovo Cimento* 19, 154. [doi:10.1007/BF02812722](https://doi.org/10.1007/BF02812722)
- Anderson (1963). "Plasmons, Gauge Invariance, and Mass". *Phys. Rev.* 130, 439. [doi:10.1103/PhysRev.130.439](https://doi.org/10.1103/PhysRev.130.439)
- Englert & Brout (1964). "Broken Symmetry and the Mass of Gauge Vector Mesons". *Phys. Rev. Lett.* 13, 321. [doi:10.1103/PhysRevLett.13.321](https://doi.org/10.1103/PhysRevLett.13.321)
- Higgs (1964). "Broken Symmetries and the Masses of Gauge Bosons". *Phys. Rev. Lett.* 13, 508. [doi:10.1103/PhysRevLett.13.508](https://doi.org/10.1103/PhysRevLett.13.508)
- Weinberg (1967). "A Model of Leptons". *Phys. Rev. Lett.* 19, 1264. [doi:10.1103/PhysRevLett.19.1264](https://doi.org/10.1103/PhysRevLett.19.1264)

**Open questions.** Is the Higgs composite, the way a Cooper pair is? What sets the electroweak scale (naturalness)? Can amplitude-mode spectroscopy in quantum materials teach anything about the Higgs potential?
