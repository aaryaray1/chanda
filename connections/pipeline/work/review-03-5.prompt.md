You are the statistical-physicist, the specialist for 03 (Thermodynamics and Statistical Mechanics) in this physics knowledge base.

# Specialist review brief (one packet per run)

You are the specialist for the branch named above. Below this brief are your branch's notes (the codex sections for every node in the packet) and the packet itself, one proposed connection per line, each with at least one end in your branch. A first-pass analyst wrote these records quickly. You are the check between them and the published registry, so review every one from **your branch's side**.

**Confirm only a record you would sign as written.** "Basically right" is a revise. A spot check of 30 records confirmed in earlier packets found that about a quarter had a wrong kind, an inflated strength, an overclaim or filler.

## Check every record against all of these
1. **Physics and facts.** Every statement holds: equations, numbers, dates, names, who did what first. Words such as *every*, *only*, *always*, *first*, *exactly* or *proves* must be strictly true; otherwise revise.
2. **Kind.**
   - `identity`: the same law, equation or object in both notes, mapping one to one, with no regime where the match fails. If the record needs a `breaks`, it is not an identity: make it `analogy` or `mechanism`.
   - `mechanism`: the same physical cause at work in both.
   - `method transfer`: a named technique that moved across and did named work there.
   - `shared object`: a system both fields study.
   - `duality`: an exact map between two descriptions of the same physics.
   - `historical`: an idea that migrated from one field to the other.
   - `analogy`: the same form with different physics. `breaks` must name the real point of failure.
3. **Strength.**
   - 3: structural in *both* fields; a graduate course in each would teach the link.
   - 2: a substantial, specific link.
   - 1: suggestive, narrow or one-sided.

   A broad "Y uses X" link is never 3.
4. **Confidence.**
   - `established`: textbook consensus.
   - `current research`: active work, including results that are only numerical or carry caveats.
   - `proposed`: speculative, or disputed in the literature. Say who disputes it in `breaks`.
5. **Content.** The summary must say what maps to what.
   - Generic overlap with no named technique and consequence is trivial. Examples: "both use PDEs", "Y uses statistics", "X is described by continuum theory". Reject it, or revise it into the specific link if you know one.
   - Cut filler such as "links to reviews" or "is important for".
6. **Nodes.** The paths on your side are the most fitting notes.
7. **Duplicates.** Two records may join the same pair of notes with the same idea. Keep the better one, revising it to absorb anything the other adds, and reject the other with `duplicate_of`.

Work from the notes below and your own knowledge. Do not run commands or search the folder. Read a node README only if the notes below are not enough, and at most 3 of them.

## Answer: JSON Lines ONLY
Give one line per packet record, in packet order. No prose, no headings, no code fences; anything else is discarded.
- `{"id": "C0123", "verdict": "confirm"}` when it passes every check as written.
- `{"id": "C0123", "verdict": "revise", "reason": "<≤25 words>", "fix": {"summary": "...", "kind": "...", "confidence": "...", "strength": 2, "breaks": "...", "map": "...", "a": "<better path>", "b": "<better path>"}}`. Include only the fields that change.
- `{"id": "C0123", "verdict": "reject", "reason": "<≤25 words: the physics error, or why it is trivial>"}`.
- `{"id": "C0124", "verdict": "reject", "reason": "duplicate of C0123", "duplicate_of": "C0123"}`.

After the verdicts you may add up to 8 important connections touching your branch that the packet lacks, as `{"verdict": "add", "record": {"a": "<node path>", "b": "<node path>", "name": "<≤60 chars>", "kind": "...", "summary": "<≤45 words>", "map": "...", "breaks": "<required for analogy>", "confidence": "established|current research|proposed", "strength": 3|2|1, "sources": []}}`. Hold additions to the same standard.

Reject physics errors, trivial links and duplicates. A real connection that is mis-stated, mislabelled or over-rated is a revise, not a reject.


---

# Your branch notes: the codex sections for the nodes in this packet

## Field overview · `knowledge/03-thermodynamics-and-statistical-mechanics`

> **Specialist:** `statistical-physicist` · **arXiv:** cond-mat.stat-mech, cond-mat.dis-nn, physics.soc-ph · **Literature source:** OpenAlex + arXiv

#### What this field studies
Thermodynamics gives universal laws for energy, heat and entropy without assuming anything about atoms. Statistical mechanics derives those laws from microscopic dynamics by counting states: $S=k_B\ln W$, and equilibrium probabilities $\propto e^{-E/k_BT}$. Its deepest results concern collective behaviour — phase transitions, universality and the renormalization group — and its frontier is far from equilibrium: driven, living, disordered and learning systems.

#### Conventions used in this branch
- $\beta=1/k_BT$; $Z=\sum e^{-\beta E}$; free energy $F=-k_BT\ln Z$.
- Thermodynamic sign convention: $dU=\delta Q-\delta W$ with $W$ work done *by* the system (physics); chemistry often uses work done *on* the system — state which.
- Critical exponents $\alpha,\beta,\gamma,\delta,\nu,\eta$ with $t=(T-T_c)/T_c$.

#### Historical spine
1824 Carnot · 1840s Joule, energy conservation · 1850–65 Clausius, entropy · 1859–77 Maxwell–Boltzmann kinetic theory, $S=k\ln W$ · 1902 Gibbs ensembles · 1905 Einstein on Brownian motion · 1925 Ising · 1931 Onsager reciprocity · 1944 Onsager solves the 2D Ising model · 1948 Shannon entropy · 1957 Jaynes; Kubo response theory · 1958 Anderson localization · 1961 Landauer principle · 1966 Kadanoff scaling · 1971 Wilson renormalization group · 1973 KT transition · 1979 Parisi replica symmetry breaking · 1997 Jarzynski equality · 2021 Nobel (Parisi) · 2024 Nobel (Hopfield, Hinton).

#### Canonical textbooks
- Schroeder, *An Introduction to Thermal Physics*; Kittel & Kroemer, *Thermal Physics* — undergraduate.
- Callen, *Thermodynamics and an Introduction to Thermostatistics* — axiomatic thermodynamics.
- Pathria & Beale, *Statistical Mechanics*; Huang, *Statistical Mechanics*; Kardar, *Statistical Physics of Particles* / *of Fields*.
- Goldenfeld, *Lectures on Phase Transitions and the Renormalization Group*; Cardy, *Scaling and Renormalization in Statistical Physics*.
- Van Kampen, *Stochastic Processes in Physics and Chemistry*; Peliti & Pigolotti, *Stochastic Thermodynamics*.

#### Live frontiers
- Stochastic thermodynamics of molecular machines and information engines; thermodynamic uncertainty relations.
- Active matter and non-reciprocal interactions.
- Statistical mechanics of deep learning: why overparameterized networks generalize.

#### How the specialist works here
Identify the ensemble that matches the physical constraints, compute $Z$ (or a free energy) before anything else, use symmetry and dimensionality to anticipate phase behaviour, check extensivity and the classical/high-temperature limits, and for dynamics ask whether detailed balance holds.

## Classical thermodynamics · `knowledge/03-thermodynamics-and-statistical-mechanics/classical-thermodynamics`

#### Overview
Thermodynamics is a theory of constraints: no engine beats Carnot, entropy of an isolated system never decreases, absolute zero is unreachable in finitely many steps. It needs no microscopic model, which is why it survived the quantum revolution intact.

#### Key equations
$$dU=T\,dS-p\,dV+\mu\,dN,\qquad \Delta S_{\text{universe}}\ge0,\qquad \eta_{\text{Carnot}}=1-\frac{T_c}{T_h}$$

#### Open problems
- Thermodynamics of small systems and strong system–bath coupling; extending the laws to quantum and information-processing regimes.

#### Connections
- [Equilibrium statistical mechanics](knowledge/03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/README.md) · [Quantum thermodynamics](knowledge/04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-thermodynamics/README.md) · [Black-hole thermodynamics](knowledge/05-relativity-and-gravitation/black-holes/black-hole-thermodynamics-and-hawking-radiation/README.md)

### Heat engines and efficiency · `knowledge/03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/heat-engines-and-efficiency`

**Scope.** Carnot cycle and theorem, Otto/Diesel/Stirling/Brayton/Rankine cycles, coefficients of performance for refrigerators and heat pumps, exergy, endoreversible thermodynamics and Curzon–Ahlborn efficiency at maximum power, microscopic and quantum heat engines.

**Core ideas.**
- All reversible engines between the same two reservoirs share Carnot's efficiency; real engines produce entropy.
- Maximum power and maximum efficiency are incompatible; at maximum power $\eta\approx1-\sqrt{T_c/T_h}$.
- Heat pumps deliver more heat than the work they use ($\text{COP}=T_h/(T_h-T_c)$ ideally).

**Key equations.**
$$\eta_{\text{Otto}}=1-r^{1-\gamma},\qquad \eta_{\text{CA}}=1-\sqrt{\frac{T_c}{T_h}},\qquad \text{COP}_{\text{fridge}}=\frac{T_c}{T_h-T_c}$$

**See also.** [Quantum thermodynamics](knowledge/04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-thermodynamics/README.md) · [Semiconductor devices and photovoltaics](knowledge/11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics/README.md)

### Phase equilibria and chemical potential · `knowledge/03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/phase-equilibria-and-chemical-potential`

**Scope.** Chemical potential and particle exchange, coexistence conditions ($T$, $p$, $\mu$ equal), Gibbs phase rule, Clausius–Clapeyron, triple and critical points, van der Waals equation and Maxwell construction, latent heat, ideal and non-ideal mixtures, osmotic pressure, law of mass action.

**Core ideas.**
- Particles flow from high to low $\mu$; equilibrium means equal $\mu$ in all phases.
- The slope of a coexistence line is fixed by latent heat and volume change.
- Van der Waals' equation captures liquid–gas criticality qualitatively but gets exponents wrong (mean field).

**Key equations.**
$$\frac{dp}{dT}=\frac{L}{T\Delta v},\qquad F=C-P+2,\qquad \left(p+\frac{an^2}{V^2}\right)(V-nb)=nRT$$

**See also.** [Mean-field and Landau theory](knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory/README.md)

### Thermodynamic potentials and Maxwell relations · `knowledge/03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/thermodynamic-potentials-and-maxwell-relations`

**Scope.** $U(S,V,N)$, $H=U+pV$, $F=U-TS$, $G=H-TS$, grand potential $\Omega=F-\mu N$, natural variables, Maxwell relations, heat capacities $C_V$, $C_p$, compressibilities, thermal expansion, Gibbs–Duhem relation, stability conditions (convexity).

**Core ideas.**
- Each potential is minimized at equilibrium under its natural constraints (e.g., $G$ at fixed $T,p$).
- Maxwell relations follow from equality of mixed second derivatives — they connect hard-to-measure quantities to easy ones.
- Stability requires $C_V>0$ and $\kappa_T>0$.

**Key equations.**
$$\left(\frac{\partial S}{\partial V}\right)_T=\left(\frac{\partial p}{\partial T}\right)_V,\qquad C_p-C_V=\frac{TV\alpha^2}{\kappa_T}$$

**See also.** [Ensembles and partition functions](knowledge/03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions/README.md)

## Disordered and complex systems · `knowledge/03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems`

#### Overview
Quenched randomness — impurities, random couplings, random graphs — produces phenomena absent in clean systems: glassy freezing with rugged energy landscapes, localization of waves, geometric phase transitions in connectivity. The same toolkit (replicas, cavity method, random matrices) now underpins the theory of neural networks, optimization and inference — recognised by the 2021 (Parisi) and 2024 (Hopfield, Hinton) Nobel Prizes.

#### Key equations
$$H_{\text{SK}}=-\frac{1}{\sqrt N}\sum_{i<j}J_{ij}s_is_j,\ J_{ij}\sim\mathcal N(0,J^2);\qquad \overline{\ln Z}=\lim_{n\to0}\frac{\overline{Z^n}-1}{n}$$

#### Open problems
- The nature of the structural glass transition (thermodynamic or purely dynamic?).
- Theory of generalization in overparameterized deep networks.

#### Connections
- [Glasses and jamming](knowledge/08-condensed-matter/soft-matter/glasses-and-jamming/README.md) · [Machine learning for physics](knowledge/00-foundations/computational-physics/machine-learning-for-physics/README.md)

### Complex networks · `knowledge/03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/complex-networks`

**Scope.** Erdős–Rényi graphs and the giant-component transition, small-world networks, preferential attachment and scale-free distributions, clustering and community detection, robustness to random failure vs. targeted attack, epidemic thresholds (SIR/SIS), synchronization on networks, multilayer networks.

**Core ideas.**
- A few shortcuts make path lengths logarithmic in network size (small-world effect).
- Preferential attachment yields $P(k)\sim k^{-3}$; hubs make networks robust to random loss but fragile to attack.
- In scale-free networks with $\gamma\le3$ the epidemic threshold vanishes as $N\to\infty$.

**Key equations.**
$$P(k)\sim k^{-\gamma},\qquad \lambda_c=\frac{\langle k\rangle}{\langle k^2\rangle}$$

**See also.** [Synchronization](knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation/README.md) · [Percolation](knowledge/03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/percolation/README.md)

### Localization and disorder · `knowledge/03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/localization-and-disorder`

**Scope.** Anderson model, mobility edges, scaling theory of localization ("gang of four"), absence of a 2D metal for non-interacting electrons, weak localization and magnetoresistance, localization of light, sound and cold atoms, many-body localization, emergent integrals of motion (l-bits), stability debate.

**Core ideas.**
- Interference of multiply scattered waves can trap them: all states are localized in 1D and 2D for any disorder (orthogonal class).
- 3D has a mobility edge separating localized from extended states.
- Interacting disordered systems may fail to thermalize (MBL); whether this survives in the thermodynamic limit is debated.

**Key equations.**
$$H=\sum_i\epsilon_ic_i^\dagger c_i-t\sum_{\langle ij\rangle}(c_i^\dagger c_j+\text{h.c.}),\ \epsilon_i\in[-W/2,W/2];\qquad \psi(r)\sim e^{-r/\xi}$$

**See also.** [Thermalization and ETH](knowledge/04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth/README.md) · [Electronic transport](knowledge/08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics/README.md)

### Percolation · `knowledge/03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/percolation`

**Scope.** Site and bond percolation, thresholds on lattices ($p_c=1/2$ for 2D square-bond, ≈0.5927 square-site), cluster-size distributions, fractal dimension of the incipient cluster, exponents in 2D (exactly known via SLE/CFT), continuum percolation, explosive percolation, applications to conductivity of composites, porous media, epidemics.

**Core ideas.**
- At $p_c$ a spanning cluster first appears; its size distribution is a power law.
- Percolation is a purely geometric critical phenomenon with its own universality class.
- On networks, percolation describes robustness and epidemic spreading.

**Key equations.**
$$P_\infty\sim(p-p_c)^\beta,\quad \xi\sim|p-p_c|^{-\nu},\qquad \beta_{2D}=\tfrac{5}{36},\ \nu_{2D}=\tfrac43,\ d_f=\tfrac{91}{48}$$

**Landmark.** Broadbent & Hammersley (1957) — see [subfield landmarks](knowledge/03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/README.md).

**See also.** [Critical exponents](knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/critical-exponents-and-universality/README.md) · [Complex networks](knowledge/03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/complex-networks/README.md)

### Spin glasses · `knowledge/03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/spin-glasses`

**Scope.** Frustration, Edwards–Anderson order parameter, Sherrington–Kirkpatrick mean-field model, replica trick and Parisi's replica-symmetry-breaking solution, ultrametricity, cavity method, aging and memory effects, droplet vs. RSB debate for finite dimensions, optimization (k-SAT) mappings.

**Core ideas.**
- Frustration prevents all bonds being satisfied → exponentially many low-energy states.
- Parisi's solution has a continuous order-parameter function $q(x)$ — proven rigorous (Talagrand).
- Glassy dynamics never equilibrate on experimental times: aging.

**Key equations.**
$$q_{EA}=\overline{\langle s_i\rangle^2},\qquad T_c^{\text{SK}}=J/k_B$$

**See also.** [Frustrated magnets](knowledge/08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids/README.md) · [Statistical physics of learning](knowledge/03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/statistical-physics-of-learning/README.md)

### Statistical physics of learning · `knowledge/03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/statistical-physics-of-learning`

**Scope.** Hopfield associative memory and its storage capacity, Boltzmann machines and energy-based models, Gardner's perceptron capacity, teacher–student models, phase transitions in inference (replica, cavity, approximate message passing), double descent, neural tangent kernel and mean-field limits, diffusion models as non-equilibrium physics, modern Hopfield networks and attention.

**Core ideas.**
- Memories as energy minima: Hopfield networks store $\sim0.138N$ random patterns before catastrophic failure.
- Learning is inference in high dimensions — sharp phase transitions separate learnable from unlearnable regimes.
- Overparameterized networks interpolate data yet generalize; statistical physics gives exact asymptotics in solvable models.

**Key equations.**
$$E=-\frac12\sum_{ij}w_{ij}s_is_j,\ w_{ij}=\frac1N\sum_\mu\xi_i^\mu\xi_j^\mu;\qquad \alpha_c^{\text{Hopfield}}\approx0.138,\ \alpha_c^{\text{perceptron}}=2$$

**See also.** [Machine learning for physics](knowledge/00-foundations/computational-physics/machine-learning-for-physics/README.md) · [Spin glasses](knowledge/03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/spin-glasses/README.md)

## Equilibrium statistical mechanics · `knowledge/03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics`

#### Overview
Given a Hamiltonian, equilibrium statistical mechanics predicts every thermodynamic property via the partition function. Classical and quantum particles differ in how states are counted, which produces Bose condensation, Fermi pressure (holding up white dwarfs) and blackbody radiation. Information theory gives an alternative foundation: equilibrium is the maximum-entropy state consistent with what we know.

#### Key equations
$$Z=\sum_ie^{-\beta E_i},\quad F=-k_BT\ln Z,\quad \langle E\rangle=-\frac{\partial\ln Z}{\partial\beta},\quad \langle n_k\rangle=\frac{1}{e^{\beta(\epsilon_k-\mu)}\mp1}$$

#### Open problems
- Foundations: why do isolated systems reach equilibrium? (Typicality, ETH.)
- Statistical mechanics of long-range interacting systems (gravity) with negative heat capacity.

#### Connections
- [Thermalization and ETH](knowledge/04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth/README.md) · [BEC](knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases/README.md) · [Compact objects](knowledge/09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects/README.md)

### Ensembles and partition functions · `knowledge/03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions`

**Scope.** Ergodic hypothesis and phase-space averages, microcanonical counting, canonical ensemble from system + reservoir, grand canonical ensemble, energy and number fluctuations, equipartition and its failure (quantum freezing of modes), ideal gas, Einstein and Debye solids, two-level systems and negative temperature.

**Core ideas.**
- Ensembles agree in the thermodynamic limit away from phase transitions; fluctuations are relatively $\mathcal O(N^{-1/2})$.
- Equipartition: each quadratic degree of freedom contributes $\tfrac12k_BT$ — until $k_BT<\hbar\omega$.
- Heat capacity measures energy fluctuations: $C_V=\langle\Delta E^2\rangle/k_BT^2$.

**Key equations.**
$$Z_{\text{ideal}}=\frac{1}{N!}\left(\frac{V}{\lambda_{\text{th}}^3}\right)^N,\ \lambda_{\text{th}}=\frac{h}{\sqrt{2\pi mk_BT}};\qquad \mathcal Z=\sum_Ne^{\beta\mu N}Z_N$$

**See also.** [Hamiltonian mechanics (Liouville)](knowledge/01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics/README.md) · [Thermalization](knowledge/04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth/README.md)

### Entropy and information · `knowledge/03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information`

**Scope.** $S=k_B\ln W$, Gibbs entropy $-k_B\sum p\ln p$, Shannon entropy, maximum-entropy principle (Jaynes), relative entropy, Szilard engine, Maxwell's demon and its exorcism, Landauer's erasure bound and its experimental tests, von Neumann entropy, information engines.

**Core ideas.**
- Thermodynamic entropy and Shannon information are the same quantity up to $k_B\ln2$ per bit.
- The demon doesn't violate the second law: erasing its memory costs at least $k_BT\ln2$ per bit.
- Maximum entropy subject to constraints reproduces the Gibbs ensembles.

**Key equations.**
$$H=-\sum_ip_i\log_2p_i,\qquad W_{\text{erase}}\ge k_BT\ln2\approx2.9\times10^{-21}\ \text{J at }300\ \text{K}$$

**See also.** [Entanglement entropy](knowledge/04-quantum-physics/quantum-information-and-computation/entanglement-theory/README.md) · [Black-hole entropy](knowledge/05-relativity-and-gravitation/black-holes/black-hole-thermodynamics-and-hawking-radiation/README.md)

### Quantum statistics · `knowledge/03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics`

**Scope.** Indistinguishability and symmetrization, occupation-number representation, Bose–Einstein and Fermi–Dirac distributions, Planck's law and Stefan–Boltzmann, Debye phonon gas, Fermi energy and degeneracy pressure, Sommerfeld expansion, BEC transition, classical (Maxwell–Boltzmann) limit when $n\lambda^3\ll1$.

**Core ideas.**
- Fermions obey Pauli exclusion → Fermi sea; at $T=0$ the gas still has pressure (white dwarfs, neutron stars).
- Bosons pile into the ground state below $T_c$; photons ($\mu=0$) give Planck's law.
- Electronic heat capacity of metals is linear in $T$ because only states within $k_BT$ of $E_F$ participate.

**Key equations.**
$$u(\nu,T)=\frac{8\pi h\nu^3}{c^3}\frac{1}{e^{h\nu/k_BT}-1},\qquad E_F=\frac{\hbar^2}{2m}(3\pi^2n)^{2/3},\qquad P=\sigma T^4,\ \sigma=\frac{2\pi^5k_B^4}{15c^2h^3}$$

**See also.** [BEC and degenerate gases](knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases/README.md) · [Compact objects](knowledge/09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects/README.md)

## Non-equilibrium statistical mechanics · `knowledge/03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics`

#### Overview
Most of the world is out of equilibrium: currents flow, cells consume energy, the climate is driven by sunlight. Near equilibrium, linear response connects transport to equilibrium fluctuations. Far from it, there is no general free-energy principle — but exact fluctuation theorems constrain entropy production, and stochastic thermodynamics extends heat and work to single trajectories.

#### Key equations
$$m\dot v=-\gamma v+\xi(t),\ \langle\xi(t)\xi(t')\rangle=2\gamma k_BT\delta(t-t');\qquad D=\frac{k_BT}{\gamma}\ (\text{Einstein});\qquad \langle e^{-\beta W}\rangle=e^{-\beta\Delta F}$$

#### Open problems
- A general variational principle for non-equilibrium steady states (if one exists).
- Thermodynamic cost of precision in biology (TURs, kinetic proofreading).

#### Connections
- [Open quantum systems](knowledge/04-quantum-physics/open-and-many-body-quantum-dynamics/README.md) · [Active matter](knowledge/08-condensed-matter/soft-matter/active-matter/README.md) · [Plasma kinetic theory](knowledge/10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping/README.md)

### Driven systems and non-equilibrium steady states · `knowledge/03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/driven-systems-and-nonequilibrium-steady-states`

**Scope.** Broken detailed balance and probability currents, totally and partially asymmetric simple exclusion processes (TASEP/ASEP), boundary-driven phase transitions, KPZ universality and Tracy–Widom statistics, directed percolation and absorbing states, self-organized criticality (sandpiles), traffic flow, large-deviation theory.

**Core ideas.**
- NESS probabilities are not Boltzmann-weighted; currents flow even in steady state.
- Large-deviation functions play the role of free energies for time-integrated currents.
- KPZ growth ($h$ exponents $1/3$, $2/3$ in 1+1D) is universal across bacteria colonies, burning paper and liquid crystals.

**Key equations.**
$$\partial_th=\nu\nabla^2h+\frac\lambda2(\nabla h)^2+\eta,\qquad J_{\text{TASEP}}=\rho(1-\rho)$$

**Landmark.** Kardar, Parisi & Zhang (1986) — see [subfield landmarks](knowledge/03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/README.md).

**See also.** [Active matter](knowledge/08-condensed-matter/soft-matter/active-matter/README.md) · [Percolation](knowledge/03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/percolation/README.md)

### Kinetic theory and the Boltzmann equation · `knowledge/03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation`

**Scope.** Maxwell–Boltzmann velocity distribution, pressure from molecular impacts, mean free path, Boltzmann transport equation, collision integral and molecular chaos, H-theorem and Loschmidt's paradox, relaxation-time approximation, Chapman–Enskog derivation of viscosity and conductivity, Boltzmann equation for electrons and phonons.

**Core ideas.**
- Molecular chaos (uncorrelated incoming velocities) introduces irreversibility into time-symmetric dynamics.
- Transport coefficients scale as (velocity) × (mean free path): $\eta\sim\frac13nm\bar v\lambda$ — independent of density for dilute gases.
- The same equation describes electrons in metals and neutrinos in supernovae.

**Key equations.**
$$\frac{\partial f}{\partial t}+\mathbf v\cdot\nabla_{\mathbf r}f+\frac{\mathbf F}{m}\cdot\nabla_{\mathbf v}f=\left(\frac{\partial f}{\partial t}\right)_{\text{coll}},\qquad \lambda=\frac{1}{\sqrt2n\sigma}$$

**See also.** [Vlasov equation](knowledge/10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping/README.md) · [Electronic transport](knowledge/08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics/README.md)

### Linear response and fluctuation–dissipation · `knowledge/03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation`

**Scope.** Response functions and susceptibilities, causality and Kramers–Kronig, Kubo formula for conductivity, Green–Kubo relations, fluctuation–dissipation theorem (classical and quantum), Johnson–Nyquist noise, Onsager reciprocal relations, thermoelectric effects.

**Core ideas.**
- The response to a weak push is determined by spontaneous equilibrium fluctuations of the same quantity.
- Dissipation (imaginary part of $\chi$) and noise are two faces of one coupling to the environment.
- Microscopic reversibility ⇒ symmetric matrix of transport coefficients (Onsager).

**Key equations.**
$$S_x(\omega)=\frac{2k_BT}{\omega}\,\mathrm{Im}\,\chi(\omega),\qquad \sigma=\frac{1}{3Vk_BT}\int_0^\infty\langle\mathbf J(t)\cdot\mathbf J(0)\rangle dt$$

**See also.** [Complex analysis (Kramers–Kronig)](knowledge/00-foundations/mathematical-methods/complex-analysis-and-special-functions/README.md) · [Detectors and noise](knowledge/00-foundations/measurement-and-data-analysis/detectors-and-instrumentation/README.md)

### Stochastic processes and Langevin dynamics · `knowledge/03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics`

**Scope.** Random walks and diffusion, Wiener process, Itô vs. Stratonovich calculus, Langevin and overdamped Langevin equations, Ornstein–Uhlenbeck process, Fokker–Planck and Smoluchowski equations, master equations and detailed balance, Kramers escape rate, first-passage times, Lévy flights and anomalous diffusion.

**Core ideas.**
- Brownian motion: $\langle x^2\rangle=2Dt$; Einstein's relation links $D$ to friction and temperature (used by Perrin to measure $N_A$).
- Fokker–Planck describes the evolving probability density for the same physics as Langevin trajectories.
- Barrier crossing rates are Arrhenius-like: $k\propto e^{-\Delta U/k_BT}$.

**Key equations.**
$$\frac{\partial P}{\partial t}=-\frac{\partial}{\partial x}\left[\frac{F(x)}{\gamma}P\right]+D\frac{\partial^2P}{\partial x^2},\qquad k_{\text{Kramers}}=\frac{\omega_0\omega_b}{2\pi\gamma}e^{-\Delta U/k_BT}$$

**See also.** [Lindblad dynamics (quantum analogue)](knowledge/04-quantum-physics/open-and-many-body-quantum-dynamics/lindblad-master-equations/README.md) · [Single-molecule biophysics](knowledge/11-interdisciplinary-physics/biophysics/single-molecule-biophysics/README.md)

### Stochastic thermodynamics and fluctuation theorems · `knowledge/03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-thermodynamics-and-fluctuation-theorems`

**Scope.** Trajectory-level heat, work and entropy, Jarzynski equality, Crooks fluctuation theorem, Evans–Searles and Gallavotti–Cohen theorems, integral fluctuation theorem, thermodynamic uncertainty relations, speed limits, information engines and feedback (Sagawa–Ueda), experiments with optical traps, RNA pulling and colloids.

**Core ideas.**
- Individual trajectories can have negative entropy production; on average they cannot.
- Jarzynski extracts equilibrium free energies from non-equilibrium work measurements.
- TURs: precision of any current costs dissipation, $\frac{\mathrm{Var}(J)}{\langle J\rangle^2}\ge\frac{2k_B}{\Sigma}$.

**Key equations.**
$$\frac{P_F(W)}{P_R(-W)}=e^{\beta(W-\Delta F)},\qquad \langle e^{-\Delta s_{\text{tot}}/k_B}\rangle=1$$

**See also.** [Quantum thermodynamics](knowledge/04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-thermodynamics/README.md) · [Molecular motors](knowledge/11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding/README.md)

## Phase transitions and critical phenomena · `knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena`

#### Overview
At a continuous phase transition, correlations extend over all length scales and microscopic details become irrelevant: magnets, fluids and binary alloys share identical critical exponents (universality). The renormalization group explains why — systems flow to the same fixed points — and is one of the deepest ideas in physics, unifying statistical mechanics with quantum field theory.

#### Conceptual spine
1. Order parameter vanishes in the disordered phase; symmetry determines its form.
2. First-order transitions have latent heat; continuous ones have diverging correlation length $\xi\sim|t|^{-\nu}$.
3. Mean field is exact above the upper critical dimension ($d_c=4$ for Ising).
4. RG: fixed points ↔ universality classes; exponents from eigenvalues of the linearized flow.

#### Key equations
$$F_L=\int d^dx\left[\tfrac12(\nabla\phi)^2+\tfrac12r\phi^2+\tfrac{u}{4!}\phi^4\right],\qquad \alpha+2\beta+\gamma=2,\qquad \gamma=\nu(2-\eta),\qquad \nu d=2-\alpha$$

#### Open problems
- Analytic 3D Ising exponents (known numerically to high precision via the bootstrap).
- Classification of quantum phase transitions beyond Landau (deconfined criticality).

#### Connections
- [Renormalization in QFT](knowledge/06-particle-physics/quantum-field-theory/renormalization-and-running-couplings/README.md) · [Conformal field theory](knowledge/06-particle-physics/quantum-field-theory/conformal-field-theory/README.md) · [Quantum criticality](knowledge/08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals/README.md)

### Ising model and lattice models · `knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/ising-model-and-lattice-models`

**Scope.** Ising model in 1D/2D/3D, Peierls argument, lattice-gas and binary-alloy mappings, Potts, XY and Heisenberg models, O(n) universality, transverse-field Ising (quantum), Monte Carlo studies, Ising machines and optimization.

**Core ideas.**
- 1D Ising: no transition at $T>0$; 2D: exact transition (Onsager); 3D: no exact solution.
- The Peierls argument shows long-range order survives at low $T$ in $d\ge2$ for discrete symmetries.
- Many optimization problems map onto finding Ising ground states.

**Key equations.**
$$H=-J\sum_{\langle ij\rangle}s_is_j-h\sum_is_i,\qquad \beta_{2D}=\tfrac18,\ \nu_{2D}=1,\ \gamma_{2D}=\tfrac74$$

**See also.** [Monte Carlo methods](knowledge/00-foundations/computational-physics/monte-carlo-methods/README.md) · [Exchange and magnetic order](knowledge/08-condensed-matter/magnetism/exchange-and-magnetic-order/README.md)

### Mean-field and Landau theory · `knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory`

**Scope.** Weiss mean-field theory of magnets, Bragg–Williams, Landau expansion and symmetry, first- vs. second-order transitions, tricritical points, Ginzburg–Landau theory of superconductors, Ginzburg criterion for fluctuation importance, mean-field exponents.

**Core ideas.**
- Write the most general analytic free energy allowed by symmetry; minimize it.
- A cubic term (allowed by symmetry) makes the transition first order.
- Mean field ignores fluctuations: exact for $d>4$ (Ising), wrong exponents below.

**Key equations.**
$$F=a(T-T_c)\phi^2+b\phi^4\Rightarrow\phi\propto(T_c-T)^{1/2};\qquad \beta=\tfrac12,\ \gamma=1,\ \delta=3,\ \alpha=0\ (\text{MF})$$

**See also.** [Spontaneous symmetry breaking](knowledge/00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking/README.md) · [BCS theory](knowledge/08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors/README.md)

### Renormalization group · `knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/renormalization-group`

**Scope.** Kadanoff block spins, Wilson's momentum-shell RG, fixed points and their stability, relevant/irrelevant/marginal operators, Gaussian and Wilson–Fisher fixed points, $\epsilon=4-d$ expansion, real-space RG, functional RG, connection to QFT renormalization.

**Core ideas.**
- Coarse-graining maps a Hamiltonian to a new one; repeated, couplings flow toward fixed points.
- Near a fixed point, perturbations scale as $b^{y_i}$: $y>0$ relevant (tuning parameters like $T-T_c$), $y<0$ irrelevant (microscopic details).
- Universality = many microscopic models in the basin of one fixed point.

**Key equations.**
$$\nu=\frac1{y_t},\qquad \nu=\frac12+\frac{\epsilon}{12}+\mathcal O(\epsilon^2)\ (\text{Ising},\ n=1)$$

**See also.** [Running couplings in QFT](knowledge/06-particle-physics/quantum-field-theory/renormalization-and-running-couplings/README.md) · [Feigenbaum universality](knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/bifurcations-and-routes-to-chaos/README.md)

### Topological phase transitions (BKT) · `knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/topological-phase-transitions-bkt`

**Scope.** 2D XY model, spin waves and power-law correlations, vortex energetics, Kosterlitz RG equations, universal jump of superfluid stiffness, experiments in helium films, superconducting films and Josephson arrays, cold-atom 2D gases, KTHNY melting of 2D crystals.

**Core ideas.**
- Mermin–Wagner forbids true long-range order, but 2D XY systems have quasi-long-range order with power-law correlations at low $T$.
- Above $T_{\text{BKT}}$ free vortices proliferate (entropy beats energy, both $\propto\ln L$).
- Superfluid stiffness jumps universally: $\rho_s(T_{\text{BKT}}^-)=\frac{2}{\pi}k_BT_{\text{BKT}}$ (in suitable units).

**Key equations.**
$$F_{\text{vortex}}=(\pi J-2k_BT)\ln\frac La\Rightarrow k_BT_{\text{BKT}}\approx\frac{\pi J}{2}\ (\text{bare})$$

**Landmark.** Kosterlitz & Thouless (1973) — see [subfield landmarks](knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/README.md).

**See also.** [Fractionalization and topological order](knowledge/08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order/README.md) · [Graphene and 2D materials](knowledge/08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials/README.md)


---

# Packet 03-5 (66 records)

{"id": "C1556", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "Relaxed states and Taylor relaxation", "kind": "method transfer", "summary": "Taylor relaxation finds minimum magnetic energy at fixed helicity, a constrained variational principle like maximum-entropy with conserved quantities, producing force-free states in reversed-field pinches and spheromaks.", "map": "\\nabla\\times\\mathbf B=\\mu\\mathbf B", "breaks": "Relaxation requires turbulent reconnection, not true thermal equilibrium; ergodic hypotheses are heuristic.", "confidence": "established", "strength": 2}
{"id": "C1557", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Debye–Hückel screening", "kind": "identity", "summary": "Debye shielding is the Debye–Hückel mean-field treatment of a Coulomb system in the canonical/grand canonical ensemble: linearized Poisson–Boltzmann gives the screened potential and the leading correlation free-energy correction.", "map": "\\nabla^2\\phi=\\lambda_D^{-2}\\phi,\\; \\lambda_D^2=\\frac{\\varepsilon_0k_BT}{ne^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1558", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "b": "10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas", "name": "Strongly coupled one-component plasma", "kind": "shared object", "summary": "The one-component plasma is a classic liquid-state model with coupling Γ; its Monte Carlo/MD equation of state and freezing near Γ≈175 connect plasma physics to classical liquid theory.", "map": "\\Gamma=\\frac{Q^2}{4\\pi\\varepsilon_0 a k_BT}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1559", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Statistical mechanics in magnetic fields (Bohr–van Leeuwen)", "kind": "identity", "summary": "Classical equilibrium partition function is independent of B, so classical plasmas have no magnetization (Bohr–van Leeuwen); diamagnetic currents are cancelled by boundary orbits, with magnetic moment conservation tied to adiabatic invariants.", "map": "", "breaks": "Applies to thermal equilibrium; nonequilibrium plasmas with adiabatic invariants show strong magnetic effects.", "confidence": "established", "strength": 2}
{"id": "C1560", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "b": "10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks", "name": "Non-Maxwellian tails and nonextensive statistics", "kind": "analogy", "summary": "Space plasmas show kappa distributions with power-law tails, which some interpret via Tsallis nonextensive statistics; alternatively tails arise from acceleration and turbulence.", "map": "", "breaks": "Tsallis interpretation is contested; kinetic acceleration models explain tails without it.", "confidence": "proposed", "strength": 1}
{"id": "C1561", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Gibbs entropy and velocity-space cascade", "kind": "mechanism", "summary": "Free-energy conservation in gyrokinetics combines entropy of fluctuations with field energy, and Landau-damped energy appears as fine-scale velocity structure; coarse-graining sets irreversible heating.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1562", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "name": "Degenerate electrons in HED matter", "kind": "shared object", "summary": "Warm dense matter and ICF fuel compression involve partially degenerate Fermi gases; the Fermi energy versus temperature sets the degeneracy parameter, and Fermi-gas pressure limits compression.", "map": "\\theta=k_BT/E_F,\\; E_F=\\frac{\\hbar^2}{2m}(3\\pi^2n)^{2/3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1563", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "10-plasma-physics/inertial-and-laser-plasmas/inertial-confinement-fusion", "name": "Fermi degeneracy and ICF fuel", "kind": "mechanism", "summary": "ICF compresses fuel on a low adiabat, keeping it near-degenerate to minimise compression work; the adiabat parameter is the ratio of fuel pressure to Fermi pressure.", "map": "\\alpha=P/P_{\\rm Fermi}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1564", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "Radiation and blackbody in laser plasmas", "kind": "shared object", "summary": "Radiation in hohlraums and hot plasmas is a Planck photon gas; indirect-drive ICF relies on x-ray bath near blackbody equilibrium and Stefan–Boltzmann scaling.", "map": "P=\\sigma T^4", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1565", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Plasmons and collective quanta", "kind": "shared object", "summary": "Langmuir waves quantize as plasmons in degenerate electron gases, with the same plasma frequency and Bohm–Pines RPA treatment as in metals; Bose statistics of phonon-like modes applies.", "map": "\\omega_p^2=\\frac{ne^2}{\\varepsilon_0 m}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1566", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Nonequilibrium stat mech and Vlasov kinetics", "kind": "shared object", "summary": "Plasma kinetics is nonequilibrium statistical mechanics of a long-range-interacting gas: the Vlasov equation is the collisionless limit of the BBGKY hierarchy, with Fokker–Planck collisions as the weak-scattering closure.", "map": "\\partial_t f+\\mathbf v\\cdot\\nabla f+\\tfrac{q}{m}(\\mathbf E+\\mathbf v\\times\\mathbf B)\\cdot\\partial_{\\mathbf v}f=C[f]", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1567", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/driven-systems-and-nonequilibrium-steady-states", "b": "10-plasma-physics/magnetic-confinement-fusion/turbulent-transport-and-gyrokinetics", "name": "Avalanches and critical gradient transport", "kind": "analogy", "summary": "Profile stiffness above critical gradients and avalanche-like transport events in tokamaks are compared with sandpile SOC models; zonal flows resemble self-regulating shear.", "map": "", "breaks": "Gyrokinetic turbulence has specific linear thresholds and fluid physics beyond sandpile rules.", "confidence": "current research", "strength": 2}
{"id": "C1568", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/driven-systems-and-nonequilibrium-steady-states", "b": "10-plasma-physics/magnetohydrodynamics/mhd-turbulence", "name": "Nonequilibrium cascades as driven steady states", "kind": "analogy", "summary": "MHD turbulence is a driven dissipative steady state with a constant flux cascade through scales, comparable to scale-invariant nonequilibrium steady states studied in KPZ and driven-diffusive systems.", "map": "", "breaks": "Energy cascades have no detailed-balance structure but also lack the exact stochastic-model solvability.", "confidence": "proposed", "strength": 1}
{"id": "C1569", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/driven-systems-and-nonequilibrium-steady-states", "b": "10-plasma-physics/space-and-astrophysical-plasmas/magnetospheres-and-space-weather", "name": "Self-organized criticality in substorms and flares", "kind": "analogy", "summary": "Avalanche models of self-organized criticality have been applied to solar flares and magnetospheric substorms, whose power-law event statistics resemble sandpile avalanches.", "map": "", "breaks": "Flare and substorm driving and loading are not clearly critical; MHD-based explanations compete.", "confidence": "current research", "strength": 2}
{"id": "C1570", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "10-plasma-physics/magnetic-confinement-fusion/tokamaks", "name": "Collisional transport and neoclassical theory", "kind": "method transfer", "summary": "Collisional transport coefficients in magnetized plasma follow from kinetic theory via Chapman–Enskog/Braginskii closures; neoclassical theory adds trapped-particle effects from toroidal geometry to random-walk diffusion estimates.", "map": "D\\sim\\nu\\,\\Delta x^2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1571", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "10-plasma-physics/plasma-fundamentals", "name": "Plasma fundamentals and Boltzmann kinetics", "kind": "shared object", "summary": "Plasma collision operators (Landau, Lenard–Balescu, Fokker–Planck) are the Coulomb-interaction versions of the Boltzmann collision integral, with a Coulomb logarithm cutoff set by Debye screening.", "map": "\\ln\\Lambda=\\ln(\\lambda_D/b_{\\min})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1572", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Boltzmann equation to Vlasov equation", "kind": "mechanism", "summary": "Vlasov is the Boltzmann equation with the collision term dropped and a self-consistent mean field added; the H-theorem fails for it, yet Landau damping gives effective irreversibility via phase mixing.", "map": "C[f]\\to 0,\\; \\mathbf F\\to q(\\mathbf E[f]+\\mathbf v\\times\\mathbf B[f])", "breaks": "Vlasov is time-reversible and conserves all Casimirs; damping is phase mixing, not entropy production.", "confidence": "established", "strength": 3}
{"id": "C1573", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Landau damping and the H-theorem", "kind": "analogy", "summary": "Both explain relaxation of a distribution function; Boltzmann's is entropy-producing via collisions, Landau's is collisionless via resonant wave-particle energy exchange and phase mixing.", "map": "", "breaks": "Landau damping conserves entropy and is reversible in principle; collisional H-theorem increases entropy.", "confidence": "established", "strength": 2}
{"id": "C1574", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "10-plasma-physics/space-and-astrophysical-plasmas/solar-wind-and-heliosphere", "name": "Collisionless solar wind and Knudsen number", "kind": "shared object", "summary": "Solar wind has large Knudsen number, so Boltzmann-equation exospheric models predict non-Maxwellian electron and ion distributions and heat flux, the origin of Parker-like kinetic closures beyond fluid theory.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1575", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation", "b": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "name": "X-ray Thomson scattering and FDT", "kind": "method transfer", "summary": "XRTS measures the dynamic structure factor of warm dense matter, which by the fluctuation–dissipation theorem encodes density response, temperature (detailed balance) and collective modes.", "map": "S(k,\\omega)=\\frac{-\\hbar}{\\pi n}\\frac{\\mathrm{Im}\\,\\chi}{1-e^{-\\hbar\\omega/k_BT}}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1576", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Conductivity, Kubo formula and Spitzer", "kind": "method transfer", "summary": "Plasma resistivity and transport coefficients can be derived from Kubo formulas, with Spitzer resistivity as the kinetic limit; Onsager symmetry constrains cross-coefficients such as thermoelectric terms.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1577", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Dielectric response, FDT and Landau damping", "kind": "identity", "summary": "The plasma dielectric function is a linear response function; its imaginary part gives Landau damping, and the FDT links it to thermal density fluctuations (dynamic structure factor, collective scattering).", "map": "S(k,\\omega)=\\frac{2k_BT}{\\omega}\\,\\mathrm{Im}\\,\\chi(k,\\omega)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1578", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "10-plasma-physics/magnetic-confinement-fusion/turbulent-transport-and-gyrokinetics", "name": "Random-walk transport and Fokker–Planck", "kind": "method transfer", "summary": "Diffusive transport estimates, Fokker–Planck collision operators and quasilinear theory in plasmas treat turbulent or collisional scattering as a random walk in space or velocity.", "map": "\\partial_t f=\\partial_v\\left(D\\,\\partial_v f\\right)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1579", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Magnetic field-line and particle diffusion", "kind": "mechanism", "summary": "Charged-particle scattering by magnetic fluctuations gives pitch-angle diffusion and cosmic-ray transport; stochastic field lines yield Rechester–Rosenbluth diffusion, a random-walk with correlation length.", "map": "D_{RR}=D_{FL}\\,v_\\parallel", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1580", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks", "name": "Stochastic acceleration and diffusive shock acceleration", "kind": "mechanism", "summary": "Fermi acceleration is a random-walk process in momentum and space; diffusive shock acceleration solves a diffusion–advection equation yielding a universal power-law spectrum.", "map": "f(p)\\propto p^{-3r/(r-1)}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1581", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-thermodynamics-and-fluctuation-theorems", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Entropy production in collisionless plasma", "kind": "analogy", "summary": "Entropy in weakly collisional plasma turbulence is cascaded to fine velocity-space scales (phase-space cascade) and dissipated by collisions, tied to Gibbs-entropy and fluctuation-theorem language.", "map": "", "breaks": "Stochastic thermodynamics assumes Markovian baths; the plasma entropy cascade is deterministic Vlasov phase mixing.", "confidence": "current research", "strength": 2}
{"id": "C1582", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory", "b": "10-plasma-physics/magnetohydrodynamics/dynamo-theory", "name": "Dynamo onset as a bifurcation", "kind": "analogy", "summary": "The dynamo transition at critical magnetic Reynolds number resembles a continuous phase transition with a control parameter and symmetry-breaking order parameter (field amplitude), with saturation by Lorentz-force feedback.", "map": "", "breaks": "No equilibrium free energy; the field has no thermal fluctuation-driven criticality.", "confidence": "current research", "strength": 1}
{"id": "C1583", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Debye screening as mean-field theory", "kind": "mechanism", "summary": "Poisson–Boltzmann is a self-consistent mean-field theory, exact as the number of particles in a Debye sphere grows (plasma parameter large), analogous to the Ginzburg criterion.", "map": "", "breaks": "Fails at strong coupling where Debye sphere holds few particles.", "confidence": "established", "strength": 2}
{"id": "C1584", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Landau theory of instability onset", "kind": "analogy", "summary": "Plasma instabilities near threshold (two-stream, drift waves) show saturation amplitude equations resembling Landau–Ginzburg normal forms, with growth rate crossing zero like a control parameter.", "map": "\\partial_t A=\\gamma A-\\beta|A|^2A", "breaks": "Instabilities are nonequilibrium bifurcations without a free-energy functional.", "confidence": "established", "strength": 2}
{"id": "C1585", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/renormalization-group", "b": "10-plasma-physics/magnetohydrodynamics/mhd-turbulence", "name": "RG and turbulence scaling", "kind": "method transfer", "summary": "Dynamic renormalization group was applied to stirred fluid and MHD turbulence (Forster–Nelson–Stephen, Fournier–Frisch), treating the cascade via scale elimination and fixed points.", "map": "", "breaks": "Results are scheme-dependent and do not reproduce intermittency or anisotropic critical balance reliably.", "confidence": "current research", "strength": 2}
{"id": "C1586", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/topological-phase-transitions-bkt", "b": "10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas", "name": "2D Coulomb systems and melting", "kind": "analogy", "summary": "Two-dimensional dusty-plasma crystals melt via defect unbinding, discussed in KTHNY theory, a BKT-type two-step transition via dislocation and disclination unbinding.", "map": "", "breaks": "Dusty plasmas are driven, dissipative and finite-size, with non-reciprocal forces.", "confidence": "current research", "strength": 2}
{"id": "C1587", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/heat-engines-and-efficiency", "b": "11-interdisciplinary-physics/applied-and-device-physics", "name": "Thermodynamic limits of energy devices", "kind": "mechanism", "summary": "Thermoelectrics, solar cells and batteries are bounded by second-law efficiency limits; ZT maps to a fraction of Carnot efficiency, and finite-time engine analysis applies.", "map": "\\eta_{max}=\\eta_C\\frac{\\sqrt{1+ZT}-1}{\\sqrt{1+ZT}+T_c/T_h}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1588", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/heat-engines-and-efficiency", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Carnot bounds on solar cell efficiency", "kind": "mechanism", "summary": "Solar cells act as heat engines between the Sun and ambient temperature; the Shockley–Queisser limit and Landsberg/Carnot bounds follow from entropy generation in photon absorption and emission.", "map": "\\eta_C = 1 - T_c/T_h", "breaks": "Photovoltaic conversion is quantum and band-gap limited, not a cyclic engine.", "confidence": "established", "strength": 2}
{"id": "C1589", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/heat-engines-and-efficiency", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Photovoltaics as thermodynamic converters", "kind": "mechanism", "summary": "Detailed balance between absorbed and emitted blackbody radiation sets the SQ limit; thermodynamic treatments give ultimate limits for multijunction and hot-carrier cells.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1590", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/phase-equilibria-and-chemical-potential", "b": "11-interdisciplinary-physics/chemical-physics/surface-science-and-catalysis", "name": "Adsorption isotherms and chemical potential", "kind": "identity", "summary": "Langmuir and BET isotherms follow from equating the chemical potential of adsorbed and gas phases, i.e. a lattice-gas grand canonical calculation.", "map": "\\theta=\\frac{KP}{1+KP}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1591", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/thermodynamic-potentials-and-maxwell-relations", "b": "11-interdisciplinary-physics/applied-and-device-physics/energy-materials-and-thermoelectrics", "name": "Electrochemical potential and battery voltage", "kind": "identity", "summary": "Cell voltage equals the Gibbs free-energy change per charge, with the open-circuit voltage from the chemical potential difference of lithium in the two electrodes.", "map": "\\Delta G=-nFE", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1592", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/complex-networks", "b": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "name": "Network science of biological regulation and spreading", "kind": "shared object", "summary": "Scale-free and small-world network structure describes gene regulation, metabolic and neural networks, and epidemic spreading with vanishing thresholds.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1593", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/localization-and-disorder", "b": "11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics", "name": "Coherent backscattering and weak localization of waves", "kind": "mechanism", "summary": "Weak localization of light in turbid media produces coherent backscattering enhancement, which modifies diffuse optics and speckle statistics in tissue.", "map": "", "breaks": "Strong localization is not reached in tissue; transport is nearly classical diffusion.", "confidence": "established", "strength": 1}
{"id": "C1594", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/percolation", "b": "11-interdisciplinary-physics/applied-and-device-physics/energy-materials-and-thermoelectrics", "name": "Percolation in composite electrodes and electrolytes", "kind": "shared object", "summary": "Ionic and electronic conduction in composite battery electrodes and solid electrolytes depends on percolating pathways with critical thresholds and power-law conductivity.", "map": "\\sigma\\propto(p-p_c)^t", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1595", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/spin-glasses", "b": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "name": "Protein folding funnels and spin-glass landscapes", "kind": "analogy", "summary": "Random-energy-model ideas and the principle of minimal frustration describe folding landscapes; glass transition temperature and funnel gap separate foldable sequences from glassy ones.", "map": "T_f/T_g>1", "breaks": "Evolved proteins are strongly non-random and minimally frustrated, unlike true spin glasses.", "confidence": "established", "strength": 3}
{"id": "C1596", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/statistical-physics-of-learning", "b": "11-interdisciplinary-physics/biophysics", "name": "Statistical physics of neural computation", "kind": "method transfer", "summary": "Hopfield-network and replica methods from spin glasses are used to model neural memory, capacity and learning in neural biophysics.", "map": "H=-\\tfrac12\\sum_{ij}J_{ij}s_is_j", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1597", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/statistical-physics-of-learning", "b": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "name": "Learning theory and protein structure inference", "kind": "method transfer", "summary": "Spin-glass landscape concepts and Boltzmann-machine/Potts inference (direct coupling analysis) link learning theory to protein folding and structure prediction.", "map": "P(\\sigma)\\propto e^{\\sum h_i+\\sum J_{ij}}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1598", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Partition functions in transition-state theory", "kind": "method transfer", "summary": "Eyring transition-state theory writes rate constants as ratios of partition functions, and equilibrium constants follow from molecular partition functions.", "map": "k=\\frac{k_BT}{h}\\frac{Q^\\ddagger}{Q}e^{-E_0/k_BT}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1599", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Information-theoretic limits of quantum metrology", "kind": "analogy", "summary": "Fisher information and Cramér–Rao bounds set measurement precision, mirroring maximum-entropy and information-geometry formulations of statistical mechanics.", "map": "", "breaks": "Quantum Fisher information involves non-commuting observables with no classical-entropy counterpart.", "confidence": "current research", "strength": 1}
{"id": "C1600", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information", "b": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "name": "Information limits in living systems", "kind": "identity", "summary": "Sensing precision, kinetic proofreading and gene regulation are bounded by mutual information and Landauer-type energy costs, using Shannon entropy and maximum entropy models.", "map": "I=S(X)-S(X|Y)", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1601", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Maximum entropy and information in image reconstruction", "kind": "method transfer", "summary": "Maximum-entropy priors and Shannon information underlie regularised image reconstruction and noise-limited image quality in CT and MRI.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1602", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Planck law and Earth's radiative balance", "kind": "mechanism", "summary": "Planck's blackbody spectrum and Stefan–Boltzmann law fix Earth's emission temperature; greenhouse absorption modifies the outgoing spectrum band by band.", "map": "\\sigma T_e^4=S(1-\\alpha)/4", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1603", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "Poisson counting statistics in emission imaging", "kind": "shared object", "summary": "Radioactive decay counts are Poisson fluctuations, so SPECT and PET image noise scales as 1/√N, which governs time-of-flight gains.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1604", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/driven-systems-and-nonequilibrium-steady-states", "b": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "name": "Active and driven matter in living systems", "kind": "shared object", "summary": "Exclusion processes, KPZ growth and active-matter nonequilibrium steady states model molecular traffic, tissue growth, bacterial colonies and collective cell motion.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1605", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/driven-systems-and-nonequilibrium-steady-states", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Self-organized criticality in earthquakes", "kind": "analogy", "summary": "Gutenberg–Richter power-law earthquake statistics and stick-slip fault models such as Burridge–Knopf and OFC are the standard examples of self-organized criticality and avalanche dynamics.", "map": "", "breaks": "Real faults show characteristic-earthquake and aftershock correlations not captured by simple SOC models.", "confidence": "current research", "strength": 2}
{"id": "C1606", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Vlasov-Boltzmann kinetics of charged beams", "kind": "analogy", "summary": "Beam distributions evolve by Vlasov/Fokker–Planck equations in phase space, as in collisionless kinetic theory; Liouville's theorem underlies emittance conservation and cooling is a Fokker–Planck process.", "map": "\\partial_t f+\\{f,H\\}=0", "breaks": "Beams are far from equilibrium, with long-range space-charge and no collision-driven thermalization.", "confidence": "established", "strength": 2}
{"id": "C1607", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "From Boltzmann kinetics to atmospheric fluid equations", "kind": "method transfer", "summary": "Chapman–Enskog reduction of the Boltzmann equation gives the Navier–Stokes transport coefficients used in atmospheric models; mean free path sets the continuum validity.", "map": "\\mathrm{Kn}=\\lambda/L\\ll1", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1608", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation", "b": "11-interdisciplinary-physics/applied-and-device-physics/energy-materials-and-thermoelectrics", "name": "Onsager reciprocity and thermoelectric transport", "kind": "identity", "summary": "Seebeck and Peltier coefficients are related by Onsager reciprocity (Kelvin relation), and ZT follows from the matrix of transport coefficients constrained by the second law.", "map": "\\Pi=TS", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1609", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Fluctuation-dissipation limits on sensor noise", "kind": "identity", "summary": "Thermal noise in SQUIDs, resonators and magnetometers is tied to dissipation by the fluctuation–dissipation theorem (Johnson–Nyquist), setting sensitivity floors.", "map": "S_V=4k_BTR", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1610", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "name": "Langevin dynamics of tethered molecules", "kind": "shared object", "summary": "Optical-tweezer bead and molecule dynamics are overdamped Langevin processes; force spectroscopy, Kramers escape and diffusion analyses use Fokker–Planck theory.", "map": "\\gamma\\dot x=-\\partial_x U+\\sqrt{2\\gamma k_BT}\\,\\xi(t)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1611", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Kramers rate theory and reaction rates", "kind": "mechanism", "summary": "Barrier-crossing rates in solution follow Kramers theory, interpolating between transition-state theory and diffusion-limited regimes with friction.", "map": "k\\propto e^{-E_b/k_BT}", "breaks": "Kramers theory assumes a single reaction coordinate with Markovian friction.", "confidence": "established", "strength": 3}
{"id": "C1612", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Hasselmann stochastic climate model", "kind": "analogy", "summary": "Slow climate variability is modelled as an Ornstein–Uhlenbeck process, with fast weather as noise forcing the slow ocean and ice variables.", "map": "C\\dot T=-\\lambda T+\\xi(t)", "breaks": "Weather noise is not strictly white and the system lacks detailed balance.", "confidence": "established", "strength": 2}
{"id": "C1613", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics", "name": "Diffusion and speckle in diffuse optics", "kind": "mechanism", "summary": "Photon transport in tissue reduces to a diffusion equation from random walks; diffusing-wave spectroscopy and Doppler/speckle techniques probe Brownian motion and blood flow.", "map": "\\partial_t\\phi=D\\nabla^2\\phi-\\mu_a c\\phi", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1614", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-thermodynamics-and-fluctuation-theorems", "b": "11-interdisciplinary-physics/biophysics", "name": "Biophysics as stochastic thermodynamics", "kind": "shared object", "summary": "Cellular sensing, motors and information processing are analysed by entropy production and thermodynamic uncertainty relations, linking precision to dissipation.", "map": "\\mathrm{Var}(J)/\\langle J\\rangle^2\\ge 2/\\Sigma", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1615", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-thermodynamics-and-fluctuation-theorems", "b": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "name": "Fluctuation theorems for molecular machines", "kind": "shared object", "summary": "Molecular motors and folding transitions operate far from equilibrium at kT scale; entropy production and Jarzynski/Crooks relations quantify their dissipation and free energies.", "map": "\\langle e^{-\\beta W}\\rangle=e^{-\\beta\\Delta F}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1616", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-thermodynamics-and-fluctuation-theorems", "b": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "name": "Dissipation cost of kinetic proofreading and sensing", "kind": "mechanism", "summary": "Energy dissipation buys accuracy in proofreading and sensing; entropy production bounds error rates and information rates.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1617", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-thermodynamics-and-fluctuation-theorems", "b": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "name": "Pulling experiments verify Jarzynski and Crooks", "kind": "method transfer", "summary": "Optical-tweezer unfolding of RNA hairpins verified Jarzynski and Crooks relations, recovering equilibrium free energies from nonequilibrium work distributions.", "map": "P_F(W)/P_R(-W)=e^{\\beta(W-\\Delta F)}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1618", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/ising-model-and-lattice-models", "b": "11-interdisciplinary-physics/chemical-physics/surface-science-and-catalysis", "name": "Lattice-gas models of adsorbate ordering", "kind": "identity", "summary": "Adsorbed monolayers map onto Ising lattice gases, with ordering transitions and surface reconstructions in Ising, Potts and universality classes; kinetic Monte Carlo models catalytic kinetics.", "map": "n_i=(1+s_i)/2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1619", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Tipping points and bifurcations in climate", "kind": "analogy", "summary": "Ice-albedo and AMOC bistability resemble Landau free-energy double wells with first-order jumps and hysteresis, and critical slowing down serves as an early-warning signal.", "map": "", "breaks": "Climate is driven and dissipative with no free energy to minimise.", "confidence": "current research", "strength": 1}
{"id": "C1620", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/renormalization-group", "b": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "name": "Polymer scaling and coarse-graining of biomolecules", "kind": "method transfer", "summary": "Renormalization-group scaling gives polymer exponents for unfolded chains, and coarse-grained models of proteins use the same logic of eliminating fast degrees of freedom.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1621", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/topological-phase-transitions-bkt", "b": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "name": "Fluctuating membranes and 2D defect physics", "kind": "analogy", "summary": "Two-dimensional membranes and the hexatic/crystalline phases share 2D melting and defect-unbinding physics, plus thermal-undulation renormalisation of bending rigidity.", "map": "", "breaks": "Membranes have out-of-plane fluctuations and fluid lipid order, so BKT applies only to in-plane ordered layers.", "confidence": "established", "strength": 2}