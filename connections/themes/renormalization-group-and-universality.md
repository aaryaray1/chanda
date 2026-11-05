---
title: The renormalization group and universality
summary: One idea for two fields — couplings that run with energy in quantum field theory, and critical exponents shared by unrelated systems in statistical mechanics — joined exactly by the Euclidean field theory ↔ statistical model correspondence.
fields: 03 06 08 07 00
kind: identity · method transfer
---
# The renormalization group and universality
> Curated theme · [Connections atlas](../../CONNECTIONS.md) · Kind: identity, method transfer

**The bridge.** Kadanoff's block spins and Wilson's renormalization group (RG) describe how a theory changes when short-distance detail is averaged out. Near a fixed point only a few *relevant* directions survive. In statistical mechanics this explains universality: a liquid–gas critical point and a uniaxial magnet share exponents. In particle physics the same flow is the running of couplings, which makes QCD asymptotically free. It also explains why low-energy physics is described by a few operators (effective field theory). The two uses are one mathematics. A Euclidean field theory in $D$ dimensions *is* a classical statistical model in $D$ dimensions, and the inverse correlation length plays the mass. *Established.*

**How each branch sees it.**
- **Statistical mechanics:**
  - [Renormalization group](../../knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/renormalization-group/README.md): fixed points, relevant and irrelevant operators, the ε-expansion.
  - [Critical exponents and universality](../../knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/critical-exponents-and-universality/README.md).
  - The [Ising model](../../knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/ising-model-and-lattice-models/README.md) as the reference universality class.
- **Particle physics:**
  - [Renormalization and running couplings](../../knowledge/06-particle-physics/quantum-field-theory/renormalization-and-running-couplings/README.md).
  - [Effective field theory](../../knowledge/06-particle-physics/quantum-field-theory/effective-field-theory/README.md).
  - [QCD](../../knowledge/06-particle-physics/standard-model/quantum-chromodynamics/README.md) and asymptotic freedom.
  - [Conformal field theory](../../knowledge/06-particle-physics/quantum-field-theory/conformal-field-theory/README.md): RG fixed points are scale-invariant, and in 2D conformal invariance fixes the Ising exponents exactly.
- **Condensed matter:** [Quantum criticality and strange metals](../../knowledge/08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals/README.md). A quantum critical point in $d$ dimensions flows like a classical model in $d+z$ dimensions.
- **Nuclear physics:** The [QCD critical point](../../knowledge/07-nuclear-physics/heavy-ion-physics/qcd-phase-diagram-and-critical-point/README.md) is conjectured. If it exists, it is expected to fall in the 3D Ising universality class.

**Shared structure.**
$$\mu\frac{dg}{d\mu}=\beta(g),\qquad \beta_{\text{QCD}}(g)=-\frac{g^3}{16\pi^2}\Big(11-\tfrac23n_f\Big)+\mathcal O(g^5)$$
$$t\to b^{\,y_t}t\ \Rightarrow\ \xi(t)=b\,\xi(b^{\,y_t}t)\ \Rightarrow\ \xi\propto|t|^{-\nu},\quad \nu=1/y_t$$

**Symbol map.**

| Statistical mechanics | Field theory |
|---|---|
| reduced temperature $t$ | mass term $m^2$ |
| correlation length $\xi$ | $1/m$ |
| lattice spacing | UV cutoff |
| critical exponents | anomalous dimensions |
| spatial dimension $d$ | Euclidean spacetime dimension $D$ |

**Where it breaks.**
- *Cutoffs.* In statistical mechanics the cutoff is physical (the lattice) and the interest is the infrared. In particle physics it is a regulator, removed or reinterpreted as new physics.
- *Unitarity.* Not every statistical model maps to a unitary QFT. Percolation and polymers are non-unitary.
- *Dynamics.* Real-time dynamics needs a dynamic exponent $z$ and conserved quantities beyond the equilibrium RG. Turbulence's Kolmogorov scaling is corrected by intermittency and is not captured by a simple fixed point.

**Landmarks.**
- Kadanoff (1966). "Scaling laws for Ising models near Tc". *Physics* 2, 263. [doi:10.1103/PhysicsPhysiqueFizika.2.263](https://doi.org/10.1103/PhysicsPhysiqueFizika.2.263)
- Wilson (1971). "Renormalization Group and Critical Phenomena. I. Renormalization Group and the Kadanoff Scaling Picture". *Phys. Rev. B* 4, 3174. [doi:10.1103/PhysRevB.4.3174](https://doi.org/10.1103/PhysRevB.4.3174)
- Gross & Wilczek (1973). "Ultraviolet Behavior of Non-Abelian Gauge Theories". *Phys. Rev. Lett.* 30, 1343. [doi:10.1103/PhysRevLett.30.1343](https://doi.org/10.1103/PhysRevLett.30.1343)
- Politzer (1973). "Reliable Perturbative Results for Strong Interactions?". *Phys. Rev. Lett.* 30, 1346. [doi:10.1103/PhysRevLett.30.1346](https://doi.org/10.1103/PhysRevLett.30.1346)
- Wilson & Kogut (1974). "The renormalization group and the ε expansion". *Phys. Rep.* 12, 75. [doi:10.1016/0370-1573(74)90023-4](https://doi.org/10.1016/0370-1573(74)90023-4)
- Belavin, Polyakov & Zamolodchikov (1984). "Infinite conformal symmetry in two-dimensional quantum field theory". *Nucl. Phys. B* 241, 333. [doi:10.1016/0550-3213(84)90052-X](https://doi.org/10.1016/0550-3213(84)90052-X)

**Open questions.** Is there a non-equilibrium RG as general as the equilibrium one? What is the RG content of strange metals? Does the QCD critical point exist, and where?
