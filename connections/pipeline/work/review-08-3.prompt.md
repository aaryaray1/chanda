You are the condensed-matter-physicist, the specialist for 08 (Condensed Matter Physics) in this physics knowledge base.

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

## Field overview · `knowledge/08-condensed-matter`

> **Specialist:** `condensed-matter-physicist` · **arXiv:** cond-mat.* (str-el, mes-hall, supr-con, mtrl-sci, soft, quant-gas) · **Literature source:** OpenAlex (Physics + Materials Science) + arXiv

#### What this field studies
Condensed matter is the largest branch of physics: it studies how ~$10^{23}$ interacting particles produce emergent behaviour — metals and insulators, superconductors and magnets, topological phases with protected edge states, and soft, squishy, living materials. Its concepts (broken symmetry, quasiparticles, the renormalization group, topology) have flowed into particle physics and quantum information, and its discoveries drive technology from transistors to MRI magnets and hard drives.

#### Conventions used in this branch
- Units: eV for electronic energies, meV for phonons/magnons, K for temperature ($1\ \text{meV}\approx11.6$ K), Tesla for fields; lattice constants in Å.
- Second quantization with $c^\dagger_{i\sigma}$; Bloch states $\psi_{n\mathbf k}(\mathbf r)=e^{i\mathbf k\cdot\mathbf r}u_{n\mathbf k}(\mathbf r)$.
- Conductance quantum $G_0=2e^2/h$; resistance quantum $h/e^2\approx25.8$ kΩ.

#### Historical spine
1912 X-ray diffraction · 1911 superconductivity (Kamerlingh Onnes) · 1928 Bloch's theorem; Heisenberg exchange · 1933 Meissner effect · 1947 transistor · 1957 BCS theory · 1958 Anderson localization · 1962 Josephson effect · 1964–65 DFT · 1972 superfluid ³He · 1980 integer QHE · 1982 fractional QHE · 1986 cuprate superconductivity · 1988 giant magnetoresistance · 2004 graphene · 2005–07 topological insulators · 2008 iron pnictides · 2009 skyrmion lattice · 2015 Weyl semimetals; H₃S at 203 K · 2018 magic-angle graphene · 2019 nickelate superconductivity · 2022–24 altermagnets; fractional quantum anomalous Hall effect.

#### Canonical textbooks
- Kittel, *Introduction to Solid State Physics*; Simon, *The Oxford Solid State Basics* — undergraduate.
- Ashcroft & Mermin, *Solid State Physics* — the classic graduate text.
- Altland & Simons, *Condensed Matter Field Theory*; Girvin & Yang, *Modern Condensed Matter Physics*; Coleman, *Introduction to Many-Body Physics*.
- Tinkham, *Introduction to Superconductivity*; Bernevig & Hughes, *Topological Insulators and Topological Superconductors*; Chaikin & Lubensky, *Principles of Condensed Matter Physics*.

#### Live frontiers
- Room-temperature superconductivity claims — and why careful replication matters (LK-99, 2023; retracted hydride claims).
- Fractional Chern insulators and non-Abelian anyons in moiré materials.
- Altermagnetism: a third magnetic class with spin-split bands and no net magnetization.
- Strange metals and the pseudogap in cuprates.

#### How the specialist works here
Identify the relevant energy scales (bandwidth, interaction, temperature), the symmetries and dimensionality, and whether a weakly interacting (band/Fermi-liquid) picture applies; map the problem to a minimal model; cite experiments with sample details (material, doping, pressure, temperature); treat extraordinary claims with extra scrutiny.

## Crystals and electronic structure · `knowledge/08-condensed-matter/crystals-and-electronic-structure`

#### Overview
Translational symmetry organizes electrons and lattice vibrations into bands labelled by crystal momentum. Whether the Fermi level falls in a band or a gap decides metal vs. insulator; small gaps make semiconductors, the basis of electronics. DFT computes band structures from first principles for real materials; transport theory connects bands to measurable conductivities.

#### Key equations
$$\psi_{n\mathbf k}(\mathbf r+\mathbf R)=e^{i\mathbf k\cdot\mathbf R}\psi_{n\mathbf k}(\mathbf r),\qquad 2d\sin\theta=n\lambda,\qquad \sigma=\frac{ne^2\tau}{m^*}$$

#### Open problems
- Predictive first-principles theory for strongly correlated materials (where DFT fails).
- Materials discovery at scale with ML-accelerated electronic-structure methods.

#### Connections
- [Quantum statistics](knowledge/03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics/README.md) · [Semiconductor devices](knowledge/11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics/README.md) · [Coupled oscillators](knowledge/01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes/README.md)

### Band theory and Bloch electrons · `knowledge/08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons`

**Scope.** Free-electron (Sommerfeld) model, Bloch's theorem, nearly-free-electron gaps at zone boundaries, tight-binding and Wannier functions, effective mass and holes, density of states and van Hove singularities, metals vs. insulators vs. semimetals, Fermi surfaces and quantum oscillations (de Haas–van Alphen), ARPES.

**Core ideas.**
- A full band carries no current; band insulators have an even number of electrons per cell (in the absence of interactions).
- Near band extrema, electrons move as free particles with effective mass $m^*=\hbar^2/(\partial^2E/\partial k^2)$.
- Quantum oscillation frequencies measure extremal Fermi-surface areas (Onsager).

**Key equations.**
$$E(\mathbf k)=\epsilon_0-2t(\cos k_xa+\cos k_ya)\ (\text{2D tight binding}),\qquad \Delta\!\left(\frac1B\right)=\frac{2\pi e}{\hbar A_F}$$

**Landmark.** Bloch (1929) — see [subfield landmarks](knowledge/08-condensed-matter/crystals-and-electronic-structure/README.md).

**See also.** [Band topology](knowledge/08-condensed-matter/topological-matter/band-topology-and-berry-curvature/README.md) · [Linear algebra](knowledge/00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces/README.md)

### Crystal structure and diffraction · `knowledge/08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction`

**Scope.** 14 Bravais lattices, 230 space groups, Miller indices, reciprocal lattice and Brillouin zones, Laue and Bragg conditions, structure factor and systematic absences, Ewald sphere, powder diffraction, neutron scattering (magnetic structure, inelastic spectroscopy), electron diffraction and cryo-EM, quasicrystals (Shechtman).

**Core ideas.**
- Diffraction peaks occur when the scattering vector equals a reciprocal-lattice vector: $\mathbf k'-\mathbf k=\mathbf G$.
- Intensities $\propto|S_{\mathbf G}|^2$ encode the basis; absences reveal centring and screw axes.
- Neutrons see light elements and magnetic moments; X-rays see electron density.

**Key equations.**
$$S_{\mathbf G}=\sum_jf_je^{-i\mathbf G\cdot\mathbf r_j},\qquad \mathbf b_1=2\pi\frac{\mathbf a_2\times\mathbf a_3}{\mathbf a_1\cdot(\mathbf a_2\times\mathbf a_3)}$$

**See also.** [Scattering of light](knowledge/02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light/README.md) · [Synchrotron light sources](knowledge/11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources/README.md)

### Electronic transport and mesoscopic physics · `knowledge/08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics`

**Scope.** Drude model, Wiedemann–Franz law, semiclassical Boltzmann transport, Hall effect and carrier type, magnetoresistance, Landauer–Büttiker formula, quantum point contacts, Aharonov–Bohm rings and universal conductance fluctuations, weak localization, Coulomb blockade, shot noise and fractional charge, hydrodynamic electron flow.

**Core ideas.**
- When the sample is smaller than the phase-coherence length, conductance is a scattering (transmission) problem.
- Each ballistic spin-degenerate channel contributes $2e^2/h$.
- Shot noise reveals the charge of carriers (e*=e/3 in the fractional quantum Hall regime).

**Key equations.**
$$G=\frac{2e^2}{h}\sum_nT_n,\qquad R_H=\frac{1}{nq},\qquad \frac{\kappa}{\sigma T}=\frac{\pi^2}{3}\left(\frac{k_B}{e}\right)^2$$

**See also.** [Kinetic theory](knowledge/03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation/README.md) · [Localization](knowledge/03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/localization-and-disorder/README.md)

### Phonons and lattice dynamics · `knowledge/08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics`

**Scope.** Harmonic approximation and dynamical matrix, acoustic and optical branches, Einstein and Debye models, $T^3$ law, phonon density of states, Umklapp scattering and thermal conductivity, anharmonicity and thermal expansion, soft modes and structural transitions, electron–phonon coupling, Raman and neutron spectroscopy of phonons.

**Core ideas.**
- $N$-atom basis → 3 acoustic and $3N-3$ optical branches.
- At low $T$ only long-wavelength acoustic phonons are excited: $C_V\propto T^3$.
- Electron–phonon coupling gives resistivity in metals and pairing in conventional superconductors.

**Key equations.**
$$C_V=\frac{12\pi^4}{5}Nk_B\left(\frac{T}{\Theta_D}\right)^3\ (T\ll\Theta_D),\qquad \kappa=\frac13C_Vv\ell$$

**See also.** [Coupled oscillators and normal modes](knowledge/01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes/README.md) · [BCS theory](knowledge/08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors/README.md)

### Semiconductors · `knowledge/08-condensed-matter/crystals-and-electronic-structure/semiconductors`

**Scope.** Direct vs. indirect gaps (GaAs vs. Si), intrinsic carrier density, donors and acceptors, Fermi level and mass-action law, drift and diffusion, Einstein relation, recombination (radiative, SRH, Auger), p–n junctions and depletion, Shockley diode equation, heterostructures and 2DEGs, wide-gap materials (GaN, SiC), excitons.

**Core ideas.**
- Carrier density depends exponentially on gap/temperature: $n_i\propto T^{3/2}e^{-E_g/2k_BT}$.
- Doping shifts the Fermi level and controls conductivity over many orders of magnitude.
- Built-in fields at junctions rectify current and separate photo-generated carriers (solar cells).

**Key equations.**
$$np=n_i^2,\qquad I=I_0\left(e^{qV/k_BT}-1\right),\qquad D=\mu\frac{k_BT}{q}$$

**Landmark.** Bardeen & Brattain (1948) — see [subfield landmarks](knowledge/08-condensed-matter/crystals-and-electronic-structure/README.md).

**See also.** [Semiconductor devices and photovoltaics](knowledge/11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics/README.md) · [TMDs and excitons](knowledge/08-condensed-matter/low-dimensional-and-quantum-materials/transition-metal-dichalcogenides-and-excitons/README.md)

## Low-dimensional and quantum materials · `knowledge/08-condensed-matter/low-dimensional-and-quantum-materials`

#### Overview
Isolating graphene in 2004 opened a world of atomically thin crystals that can be stacked like Lego into van der Waals heterostructures. A small twist between layers creates a moiré superlattice whose flat bands make interactions dominant — producing correlated insulators, superconductivity, orbital magnetism and fractional Chern insulators. Quantum dots and nanowires confine electrons in all or some directions, creating artificial atoms and qubit hosts.

#### Key equations
$$E(\mathbf k)=\pm\hbar v_F|\mathbf k|,\ v_F\approx10^6\ \text{m/s};\qquad \lambda_{\text{moiré}}\approx\frac{a}{2\sin(\theta/2)}\approx\frac a\theta$$

#### Open problems
- Pairing mechanism in magic-angle graphene; reproducibility and twist-angle disorder.
- Non-Abelian fractional Chern insulators at zero field.

#### Connections
- [Topological matter](knowledge/08-condensed-matter/topological-matter/README.md) · [BKT transition in 2D](knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/topological-phase-transitions-bkt/README.md) · [Spin qubits](knowledge/04-quantum-physics/quantum-information-and-computation/photonic-and-spin-qubits/README.md)

### Graphene and 2D materials · `knowledge/08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials`

**Scope.** Exfoliation and CVD growth, honeycomb lattice and Dirac cones at K/K′, pseudospin and Berry phase π, half-integer QHE, Klein tunnelling, high mobility in hBN-encapsulated devices, bilayer graphene and tunable gaps, hydrodynamic electron flow, phosphorene, MXenes, 2D magnets (CrI₃), stacking and twistronics.

**Core ideas.**
- Low-energy graphene electrons are massless 2D Dirac fermions with $v_F\approx c/300$.
- Berry phase π shifts Landau levels: $\sigma_{xy}=4(n+\tfrac12)e^2/h$.
- Van der Waals assembly lets materials be combined without lattice matching.

**Key equations.**
$$H=\hbar v_F(\tau_z\sigma_xk_x+\sigma_yk_y),\qquad E_n=\pm v_F\sqrt{2e\hbar B|n|}$$

**See also.** [Topological semimetals](knowledge/08-condensed-matter/topological-matter/topological-semimetals/README.md) · [Quantum Hall effects](knowledge/08-condensed-matter/topological-matter/quantum-hall-effects/README.md)

### Quantum dots and nanostructures · `knowledge/08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures`

**Scope.** Particle-in-a-box confinement and size-dependent gaps, colloidal nanocrystals (Nobel Chemistry 2023), self-assembled InAs dots as single-photon sources, gate-defined dots in GaAs and Si, Coulomb blockade and charge stability diagrams, single-electron transistors, spin qubits and Pauli spin blockade, nanowires and carbon nanotubes, Kondo effect in dots.

**Core ideas.**
- Confinement raises the gap as $\sim1/R^2$: dot colour is set by size.
- Adding one electron costs charging energy $E_C=e^2/C$; transport is blocked unless a level aligns with the leads.
- Dots are "artificial atoms" with tunable shells and couplings.

**Key equations.**
$$E_g(R)\approx E_g^{\text{bulk}}+\frac{\hbar^2\pi^2}{2R^2}\left(\frac{1}{m_e^*}+\frac{1}{m_h^*}\right)-\frac{1.8e^2}{4\pi\epsilon R},\qquad E_C=\frac{e^2}{C_\Sigma}\gg k_BT$$

**See also.** [Photonic and spin qubits](knowledge/04-quantum-physics/quantum-information-and-computation/photonic-and-spin-qubits/README.md) · [Electronic transport](knowledge/08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics/README.md)

### Transition-metal dichalcogenides and excitons · `knowledge/08-condensed-matter/low-dimensional-and-quantum-materials/transition-metal-dichalcogenides-and-excitons`

**Scope.** Indirect-to-direct gap crossover in monolayers, K/K′ valleys and valley-selective circular dichroism, spin–valley locking, excitons with binding energies of hundreds of meV, trions and biexcitons, dielectric screening engineering, interlayer excitons in heterobilayers, moiré excitons, single-photon emitters, exciton insulators and condensates.

**Core ideas.**
- Reduced screening in 2D makes excitons ~100× more tightly bound than in bulk semiconductors.
- Broken inversion symmetry plus spin–orbit coupling locks spin to valley — valley pseudospin as information carrier.
- Interlayer excitons are long-lived dipoles, candidates for exciton condensation.

**Key equations.**
$$E_n^{2D}=-\frac{\mu e^4}{2(4\pi\epsilon\epsilon_0)^2\hbar^2(n-\tfrac12)^2}\ (\text{ideal 2D hydrogen}),\qquad \sigma^\pm\leftrightarrow K,K'$$

**Landmark.** Mak et al. (2010) — see [subfield landmarks](knowledge/08-condensed-matter/low-dimensional-and-quantum-materials/README.md).

**See also.** [Semiconductors](knowledge/08-condensed-matter/crystals-and-electronic-structure/semiconductors/README.md) · [Single-photon sources](knowledge/04-quantum-physics/quantum-optics/single-photon-sources-and-detectors/README.md)

## Magnetism · `knowledge/08-condensed-matter/magnetism`

#### Overview
Magnetism in solids is a quantum effect: exchange interactions, which originate in the Pauli principle plus Coulomb repulsion, align or anti-align spins far more strongly than magnetic dipole forces could. Ordered magnets have spin-wave (magnon) excitations; frustrated magnets may avoid order altogether and form quantum spin liquids. Spintronics exploits spin for memory and logic; topological spin textures (skyrmions) and the newly identified altermagnets broaden the field.

#### Key equations
$$H=-\sum_{\langle ij\rangle}J_{ij}\,\mathbf S_i\cdot\mathbf S_j,\qquad \chi=\frac{C}{T-\theta_{CW}},\qquad \hbar\omega_{\mathbf k}\approx Dk^2\ (\text{ferromagnetic magnons})$$

#### Open problems
- Unambiguous experimental identification of a quantum spin liquid.
- Ultrafast and energy-efficient magnetic switching for memory.

#### Connections
- [Ising and Heisenberg models](knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/ising-model-and-lattice-models/README.md) · [Fields in matter](knowledge/02-electromagnetism-and-optics/electrostatics-and-magnetostatics/fields-in-matter/README.md) · [Spin glasses](knowledge/03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/spin-glasses/README.md)

### Exchange and magnetic order · `knowledge/08-condensed-matter/magnetism/exchange-and-magnetic-order`

**Scope.** Origin of exchange (Heitler–London), superexchange and Goodenough–Kanamori rules, RKKY interaction in metals, itinerant (Stoner) ferromagnetism, Curie–Weiss law, mean-field ordering temperatures, Néel order, ferrimagnets, anisotropy and domains, hysteresis, magnons and Bloch $T^{3/2}$ law, inelastic neutron scattering.

**Core ideas.**
- Exchange is electrostatic energy made spin-dependent by antisymmetry of the wavefunction.
- Insulating oxides are usually antiferromagnetic via superexchange through oxygen.
- Domains form to reduce magnetostatic energy; hysteresis comes from domain-wall pinning.

**Key equations.**
$$J_{\text{super}}\approx\frac{4t^2}{U},\qquad M(T)=M(0)\left[1-a\,T^{3/2}\right],\qquad I\,N(E_F)>1\ (\text{Stoner})$$

**Landmark.** Heisenberg (1928) — see [subfield landmarks](knowledge/08-condensed-matter/magnetism/README.md).

**See also.** [Hubbard model](knowledge/08-condensed-matter/strongly-correlated-electrons/hubbard-model-and-mott-physics/README.md) · [Fields in matter](knowledge/02-electromagnetism-and-optics/electrostatics-and-magnetostatics/fields-in-matter/README.md)

### Frustrated magnets and spin liquids · `knowledge/08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids`

**Scope.** Geometric frustration on triangles, kagome and pyrochlore lattices, frustration index $f=|\theta_{CW}|/T_N$, classical spin ice and emergent magnetic monopoles, Anderson's RVB, gapped ($\mathbb Z_2$) and gapless spin liquids, Kitaev honeycomb model and α-RuCl₃, herbertsmithite, emergent gauge fields and fractionalized spinons, thermal Hall controversies.

**Core ideas.**
- Frustration creates huge ground-state degeneracy; quantum fluctuations may then prevent order down to $T=0$.
- Spin liquids are defined by long-range entanglement and fractionalized excitations, not by a local order parameter.
- Kitaev's model is exactly solvable: spins fractionalize into Majorana fermions and $\mathbb Z_2$ fluxes.

**Key equations.**
$$H_K=-\sum_{\langle ij\rangle_\gamma}K_\gamma S_i^\gamma S_j^\gamma,\qquad f=\frac{|\theta_{CW}|}{T_N}\gg1$$

**See also.** [Fractionalization and topological order](knowledge/08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order/README.md) · [Spin glasses](knowledge/03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/spin-glasses/README.md)

### Magnetic skyrmions and textures · `knowledge/08-condensed-matter/magnetism/magnetic-skyrmions-and-textures`

**Scope.** Dzyaloshinskii–Moriya interaction in non-centrosymmetric magnets and interfaces, B20 compounds (MnSi), skyrmion lattices and isolated skyrmions, topological charge, emergent electrodynamics and topological Hall effect, skyrmion Hall effect, current-driven motion, racetrack and neuromorphic concepts, antiferromagnetic skyrmions, 3D textures (hopfions).

**Core ideas.**
- DMI favours canting; competing with exchange it twists spins into helices and skyrmions.
- Skyrmions carry integer winding number — topologically protected against smooth deformations.
- Moving electrons feel an emergent magnetic field from the texture's Berry phase.

**Key equations.**
$$N_{sk}=\frac{1}{4\pi}\int\mathbf m\cdot(\partial_x\mathbf m\times\partial_y\mathbf m)\,dx\,dy,\qquad H_{\text{DM}}=\mathbf D_{ij}\cdot(\mathbf S_i\times\mathbf S_j)$$

**Landmark.** Mühlbauer et al. (2009) — see [subfield landmarks](knowledge/08-condensed-matter/magnetism/README.md).

**See also.** [Geometric phases](knowledge/04-quantum-physics/quantum-mechanics-core/geometric-phases/README.md) · [Solitons (topological)](knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems/README.md)

### Spintronics · `knowledge/08-condensed-matter/magnetism/spintronics`

**Scope.** Spin-polarized transport, GMR (Nobel 2007) and TMR (MgO junctions), spin valves and read heads, spin-transfer torque and STT-MRAM, spin Hall and inverse spin Hall effects, spin–orbit torques, Rashba effect, spin pumping, magnonics, antiferromagnetic spintronics, spin caloritronics.

**Core ideas.**
- Resistance depends on relative magnetization of layers because spin-up and spin-down electrons scatter differently.
- Spin currents can exert torques that switch magnets without external fields.
- Spin–orbit coupling converts charge currents into transverse spin currents (spin Hall effect).

**Key equations.**
$$\text{TMR}=\frac{2P_1P_2}{1-P_1P_2}\ (\text{Jullière}),\qquad \mathbf J_s=\theta_{SH}\frac{\hbar}{2e}\,\hat{\boldsymbol\sigma}\times\mathbf J_c$$

**See also.** [Angular momentum and spin](knowledge/04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin/README.md) · [Altermagnetism](knowledge/08-condensed-matter/magnetism/altermagnetism/README.md)

## Soft matter · `knowledge/08-condensed-matter/soft-matter`

#### Overview
Soft matter — polymers, gels, foams, liquid crystals, colloids, sand, cells — has energy scales comparable to $k_BT$, so thermal fluctuations, entropy and geometry dominate. Structures self-assemble across nanometres to millimetres; responses are viscoelastic and history-dependent. Active matter, made of self-propelled units from bacteria to birds, extends the field far from equilibrium.

#### Key equations
$$R_g\sim bN^\nu,\ \nu_{\text{Flory}}=\frac{3}{d+2};\qquad F_{\text{Frank}}=\tfrac12K_1(\nabla\cdot\mathbf n)^2+\tfrac12K_2(\mathbf n\cdot\nabla\times\mathbf n)^2+\tfrac12K_3|\mathbf n\times\nabla\times\mathbf n|^2$$

#### Open problems
- The glass transition: is there an underlying thermodynamic transition?
- Non-reciprocal and odd (chiral) active materials; design of programmable matter.

#### Connections
- [Low-Reynolds-number flow](knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics/README.md) · [Biophysics](knowledge/11-interdisciplinary-physics/biophysics/README.md) · [Non-equilibrium statistical mechanics](knowledge/03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/README.md)

### Glasses and jamming · `knowledge/08-condensed-matter/soft-matter/glasses-and-jamming`

**Scope.** Viscosity growth and fragility (Angell plot), Vogel–Fulcher–Tammann law, Kauzmann paradox, mode-coupling theory, random first-order transition theory, dynamical facilitation, dynamical heterogeneity, aging and rejuvenation, ultrastable glasses, jamming at $\phi_J\approx0.64$ (random close packing in 3D), isostaticity, soft modes and boson peak.

**Core ideas.**
- A glass is a liquid that fell out of equilibrium: viscosity exceeds ~$10^{12}$ Pa·s and relaxation outlasts experiments.
- Relaxation is spatially heterogeneous — some regions are fast, some frozen.
- At jamming, packings become rigid with exactly the minimum number of contacts (isostatic: $z=2d$).

**Key equations.**
$$\tau=\tau_0\exp\!\left(\frac{DT_0}{T-T_0}\right)\ (\text{VFT}),\qquad z_c=2d$$

**See also.** [Spin glasses](knowledge/03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/spin-glasses/README.md) · [Molecular dynamics](knowledge/00-foundations/computational-physics/molecular-dynamics/README.md)

### Liquid crystals · `knowledge/08-condensed-matter/soft-matter/liquid-crystals`

**Scope.** Thermotropic and lyotropic phases, nematic director and order parameter $Q_{ij}$, Maier–Saupe and Landau–de Gennes theories, Frank elasticity, Fréedericksz transition and twisted-nematic displays, cholesteric pitch and blue phases, smectic layering, disclinations and point defects, active nematics in biology.

**Core ideas.**
- Nematics have orientational but no positional order; $\mathbf n$ and $-\mathbf n$ are equivalent, allowing half-integer defects.
- Electric fields reorient the director above a threshold — the operating principle of LCDs.
- Defect topology (homotopy groups) classifies allowed singularities.

**Key equations.**
$$S=\left\langle\tfrac12(3\cos^2\theta-1)\right\rangle,\qquad E_c=\frac{\pi}{d}\sqrt{\frac{K_1}{\epsilon_0\Delta\epsilon}}\ (\text{Fréedericksz})$$

**See also.** [Polarization and crystal optics](knowledge/02-electromagnetism-and-optics/classical-optics/polarization-and-crystal-optics/README.md) · [Active matter](knowledge/08-condensed-matter/soft-matter/active-matter/README.md)

### Polymers · `knowledge/08-condensed-matter/soft-matter/polymers`

**Scope.** Ideal (Gaussian) chains, persistence length, worm-like chain (DNA), excluded volume and the Flory exponent, theta solvents, blobs and scaling (de Gennes), Flory–Huggins mixing, rubber (entropic) elasticity, Rouse and Zimm dynamics, entanglements and reptation ($\eta\propto N^{3.4}$ experimentally), gels and vitrification, polyelectrolytes.

**Core ideas.**
- Rubber elasticity is entropic: stretching reduces the number of chain configurations, so force grows with temperature.
- Self-avoidance swells chains: $\nu\approx0.588$ in 3D (Flory estimate 3/5).
- Entangled melts relax by snake-like reptation through a tube of neighbours.

**Key equations.**
$$\langle R^2\rangle=Nb^2\ (\text{ideal}),\qquad f=\frac{3k_BT}{Nb^2}R,\qquad \tau_{\text{rep}}\sim N^3$$

**See also.** [Molecular biophysics](knowledge/11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding/README.md) · [Stochastic processes](knowledge/03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics/README.md)

## Strongly correlated electrons · `knowledge/08-condensed-matter/strongly-correlated-electrons`

#### Overview
When Coulomb repulsion $U$ rivals or exceeds the bandwidth $W$, band theory fails: half-filled systems become Mott insulators, magnetic impurities form many-body Kondo singlets, and electrons can fractionalize into excitations carrying fractions of their quantum numbers. Many of the deepest open problems in condensed matter — high-$T_c$ superconductivity, strange metals, spin liquids — live here, and they require non-perturbative numerical and field-theoretic tools.

#### Key equations
$$H_{\text{Hub}}=-t\sum_{\langle ij\rangle\sigma}(c^\dagger_{i\sigma}c_{j\sigma}+\text{h.c.})+U\sum_in_{i\uparrow}n_{i\downarrow},\qquad T_K\sim De^{-1/(J\rho)}$$

#### Open problems
- Ground-state phase diagram of the doped 2D Hubbard model (stripes vs. d-wave superconductivity).
- A theory of the strange metal with Planckian dissipation $\hbar/\tau\sim k_BT$.

#### Connections
- [Optical lattices (quantum simulation)](knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation/README.md) · [Tensor networks](knowledge/00-foundations/computational-physics/tensor-network-methods/README.md) · [Quantum field theory](knowledge/06-particle-physics/quantum-field-theory/README.md)

### Fractionalization and topological order · `knowledge/08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order`

**Scope.** Laughlin quasiparticles with charge $e/3$, anyonic statistics (abelian and non-abelian), topological ground-state degeneracy on a torus, topological entanglement entropy, toric code and $\mathbb Z_2$ gauge theory, Moore–Read state and Ising anyons, symmetry-protected topological phases, anyon interferometry and braiding experiments (2020 onward), fractional Chern insulators.

**Core ideas.**
- Topological order has no local order parameter; it is characterized by degeneracy, anyon content and long-range entanglement.
- Excitations can carry fractional charge and obey braiding statistics between bosons and fermions.
- Non-abelian anyons store quantum information non-locally — the basis of topological quantum computing.

**Key equations.**
$$S_A=\alpha L-\gamma,\ \gamma=\ln\mathcal D;\qquad \psi_m=\prod_{i<j}(z_i-z_j)^me^{-\sum|z_i|^2/4\ell_B^2}$$

**See also.** [Quantum error correction](knowledge/04-quantum-physics/quantum-information-and-computation/quantum-error-correction-and-fault-tolerance/README.md) · [Quantum Hall effects](knowledge/08-condensed-matter/topological-matter/quantum-hall-effects/README.md)

### Heavy fermions and Kondo physics · `knowledge/08-condensed-matter/strongly-correlated-electrons/heavy-fermions-and-kondo-physics`

**Scope.** Resistance minimum and Kondo's perturbation theory, Anderson impurity model, Wilson's numerical RG solution, Kondo temperature, Kondo effect in quantum dots, Kondo lattice and Doniach phase diagram (RKKY vs. Kondo), heavy-fermion compounds (CeCu₆, YbRh₂Si₂, CeCoIn₅), unconventional superconductivity, topological Kondo insulators (SmB₆).

**Core ideas.**
- Conduction electrons screen a local moment into a many-body singlet below $T_K$; perturbation theory diverges logarithmically.
- In lattices, coherent Kondo screening produces quasiparticles with masses up to ~1000 $m_e$.
- Competition between Kondo screening and RKKY magnetism drives quantum critical points.

**Key equations.**
$$\rho(T)=\rho_0+aT^5-c_K\ln\frac{T}{D},\qquad \gamma=\frac{C}{T}\propto m^*$$

**See also.** [Quantum criticality](knowledge/08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals/README.md) · [Quantum dots](knowledge/08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures/README.md)

### Numerical many-body methods · `knowledge/08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods`

**Scope.** Exact diagonalization (Lanczos), determinant and auxiliary-field QMC, sign problem, DMRG and PEPS, dynamical mean-field theory and cluster extensions (DCA, CDMFT), DFT+DMFT for real materials, diagrammatic Monte Carlo, neural-network quantum states, cross-method benchmarks (Simons collaboration).

**Core ideas.**
- No single method works everywhere; agreement between independent methods is the gold standard.
- DMFT is exact in infinite dimensions and captures the Mott transition's local physics.
- The sign problem limits QMC for doped fermions and frustrated magnets.

**Key equations.**
$$G_{\text{loc}}(i\omega_n)=\sum_{\mathbf k}\frac{1}{i\omega_n+\mu-\epsilon_{\mathbf k}-\Sigma(i\omega_n)}\quad(\text{DMFT self-consistency})$$

**Landmark.** Georges et al. (1996) — see [subfield landmarks](knowledge/08-condensed-matter/strongly-correlated-electrons/README.md).

**See also.** [Tensor network methods](knowledge/00-foundations/computational-physics/tensor-network-methods/README.md) · [Monte Carlo methods](knowledge/00-foundations/computational-physics/monte-carlo-methods/README.md)

### Quantum criticality and strange metals · `knowledge/08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals`

**Scope.** Quantum phase transitions tuned by pressure, field or doping, quantum–classical mapping ($d\to d+z$), quantum critical fan and $\omega/T$ scaling, Hertz–Millis theory and its breakdown, Fermi-liquid theory and its failure, Planckian dissipation, strange metals in cuprates, heavy fermions and moiré systems, SYK models, deconfined criticality.

**Core ideas.**
- At a QCP, quantum fluctuations replace thermal ones; finite-temperature physics above it is controlled by $T$ alone.
- Fermi liquids have $\rho\propto T^2$; strange metals show $\rho\propto T$ over decades, with scattering rate $\sim k_BT/\hbar$.
- Some QCPs lie beyond the Landau order-parameter paradigm (deconfined criticality).

**Key equations.**
$$\xi\sim|g-g_c|^{-\nu},\quad \Delta\sim|g-g_c|^{z\nu},\qquad \frac{\hbar}{\tau}\approx\alpha k_BT,\ \alpha\sim1$$

**Landmark.** Sachdev & Keimer (2011) — see [subfield landmarks](knowledge/08-condensed-matter/strongly-correlated-electrons/README.md).

**See also.** [Critical exponents](knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/critical-exponents-and-universality/README.md) · [Holography (AdS/CMT)](knowledge/05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft/README.md)

## Superconductivity · `knowledge/08-condensed-matter/superconductivity`

#### Overview
Below a critical temperature many materials lose all DC resistance and expel magnetic fields (Meissner effect). BCS theory (1957) explains conventional superconductors: phonon-mediated attraction binds electrons into Cooper pairs that condense into a macroscopic quantum state. Unconventional superconductors — cuprates (up to 133 K at ambient pressure), iron pnictides, heavy fermions, nickelates — likely pair through magnetic fluctuations, and remain one of physics' great open problems.

#### Key equations
$$\Delta(0)\approx1.764\,k_BT_c,\qquad \lambda_L=\sqrt{\frac{m}{\mu_0n_se^2}},\qquad \Phi_0=\frac{h}{2e}\approx2.07\times10^{-15}\ \text{Wb}$$

#### Open problems
- The pairing mechanism of cuprates and the nature of the pseudogap.
- A route to ambient-pressure room-temperature superconductivity.

#### Connections
- [Spontaneous symmetry breaking](knowledge/00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking/README.md) · [Superconducting qubits](knowledge/04-quantum-physics/quantum-information-and-computation/superconducting-qubits/README.md) · [Higgs mechanism](knowledge/06-particle-physics/standard-model/higgs-boson/README.md)

### BCS theory and conventional superconductors · `knowledge/08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors`

**Scope.** Cooper instability, BCS wavefunction and gap equation, isotope effect, quasiparticle spectrum and coherence factors, London equations and penetration depth, Ginzburg–Landau theory and coherence length, type-I vs. type-II ($\kappa=\lambda/\xi$), Abrikosov vortex lattice, Eliashberg theory and McMillan formula, MgB₂, Nb, Nb₃Sn magnets.

**Core ideas.**
- Any attraction, however weak, binds electron pairs on top of a filled Fermi sea.
- The gap $\Delta$ opens at the Fermi level; quasiparticles cost at least $\Delta$.
- Superconductivity is the Higgs mechanism for the electromagnetic field: photons become massive inside (Meissner effect).

**Key equations.**
$$k_BT_c\approx1.13\,\hbar\omega_De^{-1/N(0)V},\qquad E_{\mathbf k}=\sqrt{\xi_{\mathbf k}^2+\Delta^2},\qquad \kappa=\frac{\lambda}{\xi}\gtrless\frac{1}{\sqrt2}$$

**See also.** [Mean-field and Landau theory](knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory/README.md) · [BEC–BCS crossover](knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases/README.md)

### Cuprate high-Tc superconductors · `knowledge/08-condensed-matter/superconductivity/cuprate-high-tc-superconductors`

**Scope.** CuO₂ planes, parent antiferromagnetic Mott insulators, hole and electron doping, the phase diagram (AF, pseudogap, superconducting dome, strange metal, Fermi liquid), $d_{x^2-y^2}$ gap (phase-sensitive tests), charge-density waves and stripes, ARPES and STM, theories (RVB, spin fluctuations, Hubbard model numerics), record $T_c$ 133 K (Hg-1223, ambient).

**Core ideas.**
- Superconductivity emerges from doping a Mott insulator — not from a conventional metal.
- The gap changes sign around the Fermi surface ($d$-wave), with nodes along the diagonals.
- The pseudogap above $T_c$ and the linear-in-$T$ strange metal are still unexplained.

**Key equations.**
$$\Delta(\mathbf k)=\frac{\Delta_0}{2}(\cos k_xa-\cos k_ya),\qquad \rho(T)\approx\rho_0+AT\ (\text{strange metal})$$

**See also.** [Hubbard model and Mott physics](knowledge/08-condensed-matter/strongly-correlated-electrons/hubbard-model-and-mott-physics/README.md) · [Quantum criticality and strange metals](knowledge/08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals/README.md)

### Josephson effect and SQUIDs · `knowledge/08-condensed-matter/superconductivity/josephson-effect-and-squids`

**Scope.** DC and AC Josephson relations, RCSJ model, Shapiro steps and the Josephson voltage standard, flux quantization, DC and RF SQUIDs (femtotesla sensitivity), macroscopic quantum tunnelling (Nobel 2025), π junctions, Josephson parametric amplifiers, superconducting qubits.

**Core ideas.**
- Supercurrent depends on the phase difference: $I=I_c\sin\varphi$; a voltage makes the phase wind at $2eV/\hbar$.
- Flux through a superconducting loop is quantized in units of $h/2e$ — the "2" proves pairing.
- A junction is a nonlinear, lossless inductor — the essential element of superconducting quantum circuits.

**Key equations.**
$$I=I_c\sin\varphi,\qquad \frac{d\varphi}{dt}=\frac{2eV}{\hbar},\qquad f=\frac{2e}{h}V\approx483.6\ \text{GHz/mV}$$

**Landmark.** Josephson (1962) — see [subfield landmarks](knowledge/08-condensed-matter/superconductivity/README.md).

**See also.** [Superconducting qubits](knowledge/04-quantum-physics/quantum-information-and-computation/superconducting-qubits/README.md) · [SI redefinition](knowledge/00-foundations/units-and-constants/si-units-and-2019-redefinition/README.md)

## Topological matter · `knowledge/08-condensed-matter/topological-matter`

#### Overview
Some properties of electronic states are topological invariants — integers that can't change without closing a gap. The quantum Hall effect (1980) showed conductance quantized to parts per billion; topological insulators (2005–07) extended this to time-reversal-invariant materials with protected surface Dirac cones; Weyl semimetals host monopoles of Berry curvature in momentum space. Topology now guides materials searches across all ~200 000 known crystals.

#### Key equations
$$\sigma_{xy}=\nu\frac{e^2}{h},\qquad C=\frac{1}{2\pi}\int_{\text{BZ}}\Omega_{xy}(\mathbf k)\,d^2k,\qquad H_{\text{surf}}=\hbar v_F(\sigma_xk_y-\sigma_yk_x)$$

#### Open problems
- Conclusive demonstration of non-Abelian braiding of Majorana zero modes (many claims retracted).
- Raising the temperature of the quantum anomalous Hall effect for metrology.

#### Connections
- [Geometric phases](knowledge/04-quantum-physics/quantum-mechanics-core/geometric-phases/README.md) · [Topological photonics](knowledge/02-electromagnetism-and-optics/photonics-and-lasers/topological-photonics/README.md) · [Anomalies](knowledge/06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology/README.md)

### Band topology and Berry curvature · `knowledge/08-condensed-matter/topological-matter/band-topology-and-berry-curvature`

**Scope.** Berry connection and curvature of Bloch states, anomalous velocity and intrinsic anomalous Hall effect, Chern number, Wannier-center/Wilson-loop methods, Haldane model, Altland–Zirnbauer tenfold classification, symmetry indicators, topological quantum chemistry and materials databases, quantum geometric tensor and flat-band superfluid weight.

**Core ideas.**
- Berry curvature acts like a magnetic field in momentum space, deflecting wavepackets.
- Band topology is a property of how Bloch functions twist over the Brillouin zone.
- Symmetry-based indicators classify materials en masse — thousands of topological candidates identified.

**Key equations.**
$$\mathcal A_n(\mathbf k)=i\langle u_{n\mathbf k}|\nabla_{\mathbf k}u_{n\mathbf k}\rangle,\quad \Omega_n=\nabla_{\mathbf k}\times\mathcal A_n,\qquad \dot{\mathbf r}=\frac{1}{\hbar}\nabla_{\mathbf k}E-\dot{\mathbf k}\times\boldsymbol\Omega$$

**See also.** [Geometric phases](knowledge/04-quantum-physics/quantum-mechanics-core/geometric-phases/README.md) · [Topological photonics](knowledge/02-electromagnetism-and-optics/photonics-and-lasers/topological-photonics/README.md)

### Quantum Hall effects · `knowledge/08-condensed-matter/topological-matter/quantum-hall-effects`

**Scope.** Landau levels and degeneracy, plateaus in $\sigma_{xy}$ with vanishing $\sigma_{xx}$, Laughlin's gauge argument, chiral edge states, TKNN invariant, fractional QHE and composite fermions, even-denominator states (5/2), quantum Hall resistance standard, quantum anomalous Hall effect in magnetic TIs, fractional quantum anomalous Hall effect in moiré MoTe₂ and graphene (2023–24).

**Core ideas.**
- Disorder localizes bulk states, so the Hall conductance is set by a topological invariant — independent of sample details.
- Edges carry chiral, dissipationless channels; their number equals the bulk Chern number.
- Fractional states arise from interactions and host fractionally charged anyons.

**Key equations.**
$$E_n=\hbar\omega_c\left(n+\tfrac12\right),\quad \omega_c=\frac{eB}{m^*},\qquad R_{xy}=\frac{h}{\nu e^2},\qquad n_\phi=\frac{eB}{h}$$

**See also.** [Fractionalization and topological order](knowledge/08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order/README.md) · [SI units](knowledge/00-foundations/units-and-constants/si-units-and-2019-redefinition/README.md)

### Topological insulators · `knowledge/08-condensed-matter/topological-matter/topological-insulators`

**Scope.** Time-reversal symmetry and Kramers pairs, $\mathbb Z_2$ invariant, Kane–Mele and BHZ models, HgTe/CdTe quantum wells, 3D TIs (Bi₂Se₃, Bi₂Te₃), spin–momentum-locked surface Dirac cones observed by ARPES, axion electrodynamics and magnetoelectric effect, magnetic TIs (MnBi₂Te₄), higher-order and crystalline TIs.

**Core ideas.**
- Strong spin–orbit coupling can invert bands, creating a topologically non-trivial insulator.
- Kramers degeneracy protects gapless boundary states against non-magnetic disorder (no backscattering).
- The surface hosts an odd number of Dirac cones — impossible in a purely 2D lattice (fermion doubling).

**Key equations.**
$$(-1)^\nu=\prod_{i=1}^{8}\prod_{m}\xi_{2m}(\Gamma_i)\ (\text{Fu–Kane parity formula}),\qquad \mathcal L_\theta=\frac{\theta e^2}{2\pi h}\mathbf E\cdot\mathbf B,\ \theta=\pi$$

**See also.** [Discrete symmetries (Kramers)](knowledge/00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt/README.md) · [Axions](knowledge/06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector/README.md)

### Topological semimetals · `knowledge/08-condensed-matter/topological-matter/topological-semimetals`

**Scope.** Weyl nodes as Berry-curvature monopoles, Nielsen–Ninomiya pairing, Fermi-arc surface states, TaAs family, type-II Weyl (WTe₂), Dirac semimetals (Na₃Bi, Cd₃As₂), chiral anomaly and negative longitudinal magnetoresistance, nodal-line and multifold fermions, Kramers–Weyl fermions, nonlinear Hall effect.

**Core ideas.**
- Breaking inversion or time reversal splits a Dirac point into Weyl points of opposite chirality.
- Each Weyl node carries Chern number ±1; arcs connect their surface projections.
- Parallel E and B pump electrons between nodes — the solid-state version of the ABJ anomaly.

**Key equations.**
$$H_W=\pm\hbar v_F\,\boldsymbol\sigma\cdot\mathbf k,\qquad \frac{dN_\pm}{dt}=\pm\frac{e^2}{h^2}\mathbf E\cdot\mathbf B$$

**Landmark.** Xu et al. (2015) — see [subfield landmarks](knowledge/08-condensed-matter/topological-matter/README.md).

**See also.** [Anomalies](knowledge/06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology/README.md) · [Graphene (2D Dirac)](knowledge/08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials/README.md)

### Topological superconductors and Majoranas · `knowledge/08-condensed-matter/topological-matter/topological-superconductors-and-majoranas`

**Scope.** Bogoliubov–de Gennes formalism and particle–hole symmetry, Kitaev chain, p-wave pairing, semiconductor–superconductor nanowires (InAs/Al), zero-bias peaks and their non-topological mimics (Andreev bound states), topological gap protocol, vortex Majoranas in Fe(Te,Se), minimal Kitaev chains in quantum dots, tetron/measurement-based topological qubits.

**Core ideas.**
- A Majorana zero mode is its own antiparticle ($\gamma=\gamma^\dagger$); two of them form one non-local fermion.
- Braiding Majoranas implements Clifford gates topologically.
- Zero-bias conductance peaks alone are not proof — several high-profile claims were retracted.

**Key equations.**
$$H_K=\sum_j\left[-\mu c_j^\dagger c_j-t(c_j^\dagger c_{j+1}+\text{h.c.})+\Delta(c_jc_{j+1}+\text{h.c.})\right],\quad |\mu|<2t\ \Rightarrow\ \text{topological}$$

**Landmark.** Kitaev (2001) — see [subfield landmarks](knowledge/08-condensed-matter/topological-matter/README.md).

**See also.** [Topological order](knowledge/08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order/README.md) · [Quantum dots](knowledge/08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures/README.md)


---

# Packet 08-3 (100 records)

{"id": "C1805", "a": "04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin", "b": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "name": "Exchange from spin algebra and Pauli exclusion", "kind": "mechanism", "summary": "Heisenberg exchange arises because the Coulomb energy depends on the singlet or triplet spin state through antisymmetry; addition of spin angular momenta gives the S1.S2 form.", "map": "H=-J\\,\\mathbf S_1\\cdot\\mathbf S_2,\\ \\mathbf S_1\\cdot\\mathbf S_2=\\tfrac12[S(S+1)-\\tfrac32]", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1806", "a": "04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin", "b": "08-condensed-matter/magnetism/spintronics", "name": "Spin angular momentum as a transport degree of freedom", "kind": "method transfer", "summary": "Spintronics transports and manipulates spin angular momentum: spin precession, spin-orbit coupling (Rashba/Dresselhaus) and spin-transfer torque are the quantum mechanics of spin applied to devices.", "map": "\\dot{\\mathbf S}=\\gamma\\mathbf S\\times\\mathbf B;\\ H_R=\\alpha(\\boldsymbol\\sigma\\times\\mathbf k)\\cdot\\hat z", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1807", "a": "04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems", "b": "08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids", "name": "Kitaev honeycomb model and Kitaev materials", "kind": "method transfer", "summary": "Kitaev's exactly solvable honeycomb model has a Z2 spin-liquid ground state with Majorana excitations; it motivates the search in alpha-RuCl3 and iridates.", "map": "H_K=-\\sum_{\\langle ij\\rangle_\\gamma}K_\\gamma S_i^\\gamma S_j^\\gamma", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1808", "a": "04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems", "b": "08-condensed-matter/topological-matter/quantum-hall-effects", "name": "Landau levels are harmonic-oscillator levels", "kind": "identity", "summary": "A charged particle in a uniform field maps onto a harmonic oscillator, giving Landau levels; filling them gives the integer quantum Hall plateaus.", "map": "E_n=\\hbar\\omega_c(n+\\tfrac12),\\ \\omega_c=eB/m^*", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1809", "a": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "b": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "name": "Aharonov-Bohm oscillations in mesoscopic rings", "kind": "mechanism", "summary": "Phase-coherent electrons in metal rings show conductance oscillations with flux period h/e, a direct transport measurement of the Aharonov-Bohm phase.", "map": "\\Delta\\Phi=h/e", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1810", "a": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "name": "Berry phase pi of graphene's Dirac electrons", "kind": "mechanism", "summary": "Pseudospin winding gives graphene electrons a pi Berry phase, producing the half-integer quantum Hall sequence and suppressed backscattering.", "map": "\\sigma_{xy}=4\\frac{e^2}{h}(n+\\tfrac12)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1811", "a": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "b": "08-condensed-matter/magnetism/magnetic-skyrmions-and-textures", "name": "Emergent electromagnetism of skyrmions", "kind": "mechanism", "summary": "Electrons adiabatically following a skyrmion texture acquire a real-space Berry phase that acts as an emergent magnetic flux of one quantum per skyrmion, giving the topological Hall effect.", "map": "b_z=\\frac{\\hbar}{2e}\\mathbf m\\cdot(\\partial_x\\mathbf m\\times\\partial_y\\mathbf m)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1812", "a": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "b": "08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order", "name": "Anyon statistics as Berry phases", "kind": "identity", "summary": "Exchanging two quasiparticles adiabatically gives a Berry phase; for Laughlin quasiholes it equals pi times the filling, so fractional statistics is a geometric phase.", "map": "\\gamma_{\\rm exch}=\\pi\\nu\\ (\\nu=1/m)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1813", "a": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "b": "08-condensed-matter/topological-matter", "name": "Geometric phases organize topological matter", "kind": "historical", "summary": "Berry's 1984 phase gave condensed matter a unified language for polarization, anomalous Hall effects and topological phases.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1814", "a": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "Chern number is integrated Berry curvature", "kind": "identity", "summary": "The Hall conductance of a filled band equals the Brillouin-zone integral of Berry curvature (TKNN); geometric-phase concepts define all band-topological invariants.", "map": "\\sigma_{xy}=\\frac{e^2}{h}\\frac{1}{2\\pi}\\int_{\\rm BZ}\\Omega_{xy}d^2k", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1815", "a": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "b": "08-condensed-matter/topological-matter/topological-semimetals", "name": "Weyl points as Berry-curvature monopoles", "kind": "identity", "summary": "Berry's degeneracy monopole is realized in crystals: Weyl nodes are sources of Berry flux with integer charge, giving Fermi arcs and the chiral anomaly.", "map": "\\oint_S\\Omega\\cdot d\\mathbf S=2\\pi\\chi,\\ \\chi=\\pm1", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1816", "a": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "Path-integral quantum Monte Carlo", "kind": "method transfer", "summary": "Imaginary-time path integrals map quantum many-body systems onto classical polymers, sampled by Monte Carlo; bosonic exchange appears as permutation cycles (superfluid helium).", "map": "Z=\\mathrm{Tr}e^{-\\beta H}=\\int\\mathcal Dx\\,e^{-S_E[x]/\\hbar}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1817", "a": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "b": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "name": "Born approximation behind diffraction", "kind": "identity", "summary": "X-ray, electron and neutron diffraction are first-Born scattering: the cross section is the Fourier transform of the scattering density, and inelastic neutron scattering measures the dynamic structure factor.", "map": "\\frac{d^2\\sigma}{d\\Omega dE}\\propto\\frac{k_f}{k_i}S(\\mathbf q,\\omega)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1818", "a": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "b": "08-condensed-matter/strongly-correlated-electrons/heavy-fermions-and-kondo-physics", "name": "Kondo effect as resonant scattering", "kind": "mechanism", "summary": "Below T_K conduction electrons scatter off the Kondo singlet with phase shift pi/2, the unitary limit; the Friedel sum rule ties the phase shift to the screened charge.", "map": "\\delta_0=\\pi/2;\\ G=\\frac{2e^2}{h}\\sin^2\\delta_0\\ (\\text{Kondo dot})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1819", "a": "04-quantum-physics/quantum-optics/cavity-and-circuit-qed", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures", "name": "Cavity QED with quantum dots", "kind": "shared object", "summary": "Single quantum dots in photonic-crystal nanocavities reach strong coupling with vacuum Rabi splitting, the solid-state realization of Jaynes-Cummings physics.", "map": "g>\\kappa,\\gamma", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1820", "a": "04-quantum-physics/quantum-optics/cavity-and-circuit-qed", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/transition-metal-dichalcogenides-and-excitons", "name": "Strong coupling of excitons to cavity photons", "kind": "mechanism", "summary": "Excitons in microcavities reach strong coupling, forming polaritons with vacuum Rabi splitting, the Jaynes-Cummings physics of cavity QED with a collective emitter.", "map": "E_\\pm=\\frac{E_x+E_c}{2}\\pm\\sqrt{g^2N+\\delta^2/4}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1821", "a": "04-quantum-physics/quantum-optics/cavity-optomechanics", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "Mechanical resonators are engineered phonons", "kind": "shared object", "summary": "Optomechanical resonators are phonon modes of nanostructures; phononic band gaps, Brillouin scattering and two-level-system damping are lattice-dynamics physics.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1822", "a": "04-quantum-physics/quantum-optics/quantized-light-and-photon-statistics", "b": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "name": "Electron quantum optics", "kind": "method transfer", "summary": "Single-electron sources, quantum point contacts as beam splitters and edge channels as waveguides let electronic HOM and HBT experiments mirror photon statistics; shot noise is the fermionic g2.", "map": "S_I=2eI\\,F,\\ F=\\frac{\\sum T_n(1-T_n)}{\\sum T_n}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1823", "a": "04-quantum-physics/quantum-optics/single-photon-sources-and-detectors", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures", "name": "Quantum-dot single-photon sources", "kind": "shared object", "summary": "Self-assembled semiconductor quantum dots are two-level emitters that, embedded in micropillars, give bright, pure and indistinguishable single photons.", "map": "g^{(2)}(0)\\ll1;\\ V_{\\rm HOM}\\to1", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1824", "a": "04-quantum-physics/quantum-optics/single-photon-sources-and-detectors", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/transition-metal-dichalcogenides-and-excitons", "name": "Quantum emitters in 2D semiconductors", "kind": "shared object", "summary": "Strain- and defect-localized excitons in monolayer WSe2 act as single-photon emitters, linking 2D-material excitonics to quantum-optical sources.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1825", "a": "04-quantum-physics/quantum-optics/single-photon-sources-and-detectors", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Superconducting single-photon detectors", "kind": "shared object", "summary": "SNSPDs and transition-edge sensors use photon-induced breaking of superconductivity (hotspots, steep R(T)) to count photons with high efficiency and low jitter.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2025", "a": "05-relativity-and-gravitation/black-holes/black-hole-thermodynamics-and-hawking-radiation", "b": "08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order", "name": "Area laws: black-hole and entanglement entropy", "kind": "analogy", "summary": "Entanglement entropy of a field across a surface scales with its area, as does Bekenstein-Hawking entropy; in gapped topological phases the area law has a universal constant correction -gamma = -ln D, the same diagnostic used for long-range entanglement.", "map": "S_{\\rm ent}=\\alpha\\frac{A}{\\epsilon^2}-\\gamma\\ \\leftrightarrow\\ S_{\\rm BH}=\\frac{k_BA}{4\\ell_P^2}", "breaks": "The entanglement coefficient alpha is cutoff-dependent; matching 1/4G needs renormalization of Newton's constant, while gamma has no BH counterpart.", "confidence": "established", "strength": 2}
{"id": "C2026", "a": "05-relativity-and-gravitation/black-holes/black-hole-thermodynamics-and-hawking-radiation", "b": "08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals", "name": "SYK: strange metal and near-extremal black hole", "kind": "duality", "summary": "The Sachdev-Ye-Kitaev model of randomly interacting fermions, rooted in a random-magnet spin fluid, has an extensive zero-temperature entropy and emergent reparametrization symmetry matching near-extremal charged black holes and JT gravity in AdS2; it also maximizes chaos.", "map": "S(T\\to0)=Ns_0\\ \\leftrightarrow\\ S_{\\rm BH}=\\frac{A_{\\rm ext}}{4G},\\quad \\text{Schwarzian }-\\frac{N\\alpha_S}{J}\\int\\{f,\\tau\\}\\,d\\tau,\\ \\lambda_L=2\\pi T/\\hbar", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2027", "a": "05-relativity-and-gravitation/black-holes/black-hole-thermodynamics-and-hawking-radiation", "b": "08-condensed-matter/topological-matter/topological-semimetals", "name": "Type-II Weyl cones as analogue horizons", "kind": "analogy", "summary": "A tilted Weyl cone is a Weyl fermion in an effective Painleve-Gullstrand metric whose shift vector is the tilt; where the tilt exceeds the Fermi velocity (type I to type II) the cone tips over like light cones at a horizon, and Hawking-like tunnelling has been proposed at such interfaces.", "map": "H=\\hbar\\mathbf t\\cdot\\mathbf k+\\hbar v_F\\boldsymbol\\sigma\\cdot\\mathbf k\\ \\leftrightarrow\\ ds^2=-c^2dt^2+(d\\mathbf x-\\mathbf v\\,dt)^2,\\ |\\mathbf t|=v_F\\ \\text{at horizon}", "breaks": "No Einstein dynamics or backreaction; lattice cutoff, disorder and electron interactions are not small, and the emitted 'temperature' would be tiny.", "confidence": "proposed", "strength": 2}
{"id": "C2028", "a": "05-relativity-and-gravitation/black-holes/information-paradox", "b": "08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals", "name": "Chaos bound and Planckian dissipation", "kind": "analogy", "summary": "Black holes saturate the bound on the Lyapunov exponent of out-of-time-order correlators and are the fastest scramblers; strange metals show a transport rate near the same Planckian scale k_B T/hbar, suggesting a common bound on dissipation in matter without quasiparticles.", "map": "\\lambda_L\\le\\frac{2\\pi k_BT}{\\hbar}\\ \\leftrightarrow\\ \\frac{\\hbar}{\\tau}=\\alpha k_BT,\\ \\alpha\\sim1", "breaks": "No theorem ties lambda_L to the momentum-relaxation rate that sets resistivity; the chaos bound is rigorous, the transport 'bound' is empirical and has counterexamples.", "confidence": "current research", "strength": 2}
{"id": "C2029", "a": "05-relativity-and-gravitation/general-relativity/einstein-field-equations", "b": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "name": "Dislocations as torsion, disclinations as curvature", "kind": "analogy", "summary": "The continuum theory of crystal defects is Riemann-Cartan geometry: the Burgers vector is the closure failure (torsion) and the Frank angle the rotation holonomy (curvature); a disclination line has the conical metric of a cosmic string.", "map": "b^a=\\oint e^a{}_\\mu dx^\\mu=\\iint T^a\\ (\\text{torsion}),\\quad \\Omega=\\iint R\\ (\\text{curvature});\\ ds^2=dr^2+\\alpha^2r^2d\\phi^2+dz^2", "breaks": "Euclidean signature and elastic energy replace the Einstein-Hilbert action; the 'geometry' is a bookkeeping device with no propagating gravitons.", "confidence": "established", "strength": 2}
{"id": "C2030", "a": "05-relativity-and-gravitation/general-relativity/einstein-field-equations", "b": "08-condensed-matter/topological-matter/quantum-hall-effects", "name": "Hall viscosity and gravitational response", "kind": "method transfer", "summary": "Coupling a quantum Hall fluid to a background spatial metric and spin connection defines Hall viscosity eta_H = hbar s-bar n/2 and the Wen-Zee shift on curved surfaces; Luttinger's fictitious gravitational potential likewise defines thermal-Hall response.", "map": "\\eta_H=\\tfrac12\\hbar\\bar s\\,n,\\quad N_\\phi=\\nu^{-1}N-\\mathcal S\\ (\\text{sphere}),\\quad \\mathcal L_{\\rm WZ}\\propto\\frac{\\nu\\bar s}{2\\pi}\\omega\\wedge dA", "breaks": "The background metric is a probe, not dynamical gravity, and the fluid is non-relativistic.", "confidence": "current research", "strength": 2}
{"id": "C2031", "a": "05-relativity-and-gravitation/general-relativity/tests-of-general-relativity", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "Gravity Probe B gyroscopes read by SQUIDs", "kind": "method transfer", "summary": "Gravity Probe B measured geodetic and frame-dragging precession of niobium-coated quartz rotors through the London moment of the spinning superconductor, read out by SQUID magnetometers at milliarcsecond resolution.", "map": "\\mathbf B_L=-\\frac{2m_e}{e}\\boldsymbol\\omega\\approx-1.14\\times10^{-11}\\ \\text{T}\\,\\frac{\\omega}{\\text{rad s}^{-1}};\\ \\Omega_{\\rm geo}=6606\\ \\text{mas/yr},\\ \\Omega_{\\rm LT}=39\\ \\text{mas/yr}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2032", "a": "05-relativity-and-gravitation/gravitational-waves/gravitational-wave-theory-and-waveforms", "b": "08-condensed-matter/topological-matter/quantum-hall-effects", "name": "Chiral 'graviton' modes of FQH liquids", "kind": "analogy", "summary": "Haldane's geometric picture gives a fractional quantum Hall fluid a dynamical unimodular intrinsic metric; its long-wavelength fluctuation is a spin-2 chiral mode (GMP magnetoroton), whose chirality has been probed with circularly polarized Raman scattering, like a GW helicity-2 mode.", "map": "", "breaks": "The mode is gapped, non-relativistic and lives on a lattice-free 2D fluid without diffeomorphism invariance; it is spin-2 only in the sense of its rotation quantum number.", "confidence": "current research", "strength": 1}
{"id": "C2033", "a": "05-relativity-and-gravitation/gravitational-waves/ground-based-detections", "b": "08-condensed-matter/soft-matter/glasses-and-jamming", "name": "Amorphous mirror coatings limit LIGO thermal noise", "kind": "shared object", "summary": "In the most sensitive LIGO band the floor is Brownian thermal noise of the amorphous Ta2O5/SiO2 mirror coatings, set via fluctuation-dissipation by their mechanical loss angle, which comes from two-level systems in the glass.", "map": "S_x(f)=\\frac{2k_BT}{\\pi^2f^2}\\frac{W_{\\rm diss}}{F_0^2},\\quad W_{\\rm diss}\\propto\\phi_{\\rm coat}\\ (\\text{loss angle})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2034", "a": "05-relativity-and-gravitation/gravitational-waves/pulsar-timing-arrays", "b": "08-condensed-matter/soft-matter/liquid-crystals", "name": "Liquid crystals test cosmic-string network scaling", "kind": "analogy", "summary": "Cosmic-string GW backgrounds rest on the Kibble mechanism and scaling of string networks; quenched nematic liquid crystals form and coarsen string networks that can be filmed, giving laboratory checks of defect formation and scaling.", "map": "", "breaks": "Nematic strings move dissipatively, not relativistically (no Nambu-Goto dynamics), and do not radiate gravitational waves; loop production and GW spectra cannot be tested this way.", "confidence": "established", "strength": 1}
{"id": "C2035", "a": "05-relativity-and-gravitation/gravitational-waves/space-based-and-future-detectors", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "Cryogenic crystalline test masses", "kind": "shared object", "summary": "KAGRA uses 20 K sapphire and Einstein Telescope/LIGO Voyager plan cryogenic silicon test masses, chosen for low phonon loss and for silicon's vanishing thermal expansion near 123 K, which kills thermoelastic noise.", "map": "S_x^{\\rm TE}\\propto\\frac{\\alpha^2(1+\\sigma)^2k_BT^2\\kappa}{\\rho^2C^2\\omega^2},\\quad \\alpha_{\\rm Si}(123\\ \\text{K})=0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2036", "a": "05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "name": "Dirac-fluid hydrodynamics near the KSS bound", "kind": "method transfer", "summary": "Near charge neutrality graphene electrons form a nearly relativistic Dirac fluid with small eta/s and violated Wiedemann-Franz law; relativistic and holographic hydrodynamics developed for the QGP and black branes describe its transport.", "map": "", "breaks": "Graphene is weakly coupled (alpha_g of order 1 but with log running), has disorder and phonons, and has no gravity dual.", "confidence": "current research", "strength": 2}
{"id": "C2037", "a": "05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "MERA tensor networks as discrete AdS", "kind": "method transfer", "summary": "The multiscale entanglement renormalization ansatz built for critical spin chains has a hyperbolic network geometry; minimal cuts through it reproduce Ryu-Takayanagi, so condensed-matter numerics became a toy model of emergent bulk space and holographic codes.", "map": "S_A\\le|\\gamma_A|\\log\\chi\\ \\leftrightarrow\\ S_A=\\frac{\\text{Area}(\\gamma_A)}{4G_N};\\quad S_A\\sim\\frac c3\\log\\ell\\ (1+1\\text{D CFT})", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2038", "a": "05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft", "b": "08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals", "name": "Holographic strange metals (AdS/CMT)", "kind": "duality", "summary": "Charged black branes model compressible quantum-critical matter without quasiparticles: horizon geometry sets T-linear resistivity, Planckian relaxation and non-Fermi-liquid spectral functions in bottom-up holographic models.", "map": "", "breaks": "No known microscopic lattice Hamiltonian has a controlled gravity dual; large-N and strong coupling are assumptions, and bottom-up models fit rather than derive cuprate data.", "confidence": "current research", "strength": 2}
{"id": "C2039", "a": "05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft", "b": "08-condensed-matter/superconductivity", "name": "Holographic superconductors: hairy black holes", "kind": "duality", "summary": "Below a critical temperature a charged black brane becomes unstable to growing charged scalar hair; the boundary dual is a condensate that breaks U(1), with an optical-conductivity gap and a gap-to-Tc ratio larger than BCS.", "map": "m_{\\rm eff}^2=m^2-q^2\\Phi^2g^{tt}<m_{\\rm BF}^2\\ \\Rightarrow\\ \\langle\\mathcal O\\rangle\\propto(1-T/T_c)^{1/2},\\ \\omega_g/T_c\\approx8", "breaks": "The boundary U(1) is global, not dynamical, so there is no Meissner effect without extra gauging; mean-field exponents follow from large N.", "confidence": "current research", "strength": 2}
{"id": "C2040", "a": "05-relativity-and-gravitation/quantum-gravity/other-approaches-to-quantum-gravity", "b": "08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order", "name": "Emergent gauge fields and gravity from many-body order", "kind": "analogy", "summary": "String-net condensation in lattice spin models gives emergent photons and fermions, raising the question of whether gravity can emerge the same way; emergent-gravity programmes (Volovik, Wen) use topological order as a template.", "map": "", "breaks": "Weinberg-Witten forbids a massless spin-2 particle from a Lorentz-covariant conserved stress tensor, and emergent Lorentz invariance is not exact on a lattice; no model yields Einstein gravity.", "confidence": "proposed", "strength": 2}
{"id": "C2041", "a": "05-relativity-and-gravitation/quantum-gravity/qft-in-curved-spacetime", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "name": "Strained graphene: Dirac fields in curved space", "kind": "analogy", "summary": "Low-energy graphene electrons obey a 2+1D Dirac equation; strain and ripples enter as pseudo-gauge fields and a position-dependent tetrad, so curved-space Dirac methods describe pseudo-Landau levels in nanobubbles and suggest Hawking/Unruh analogues.", "map": "i\\gamma^ae_a{}^\\mu(\\partial_\\mu+\\Gamma_\\mu-iA^{\\rm s}_\\mu)\\psi=0,\\quad A^{\\rm s}\\propto\\beta(u_{xx}-u_{yy},-2u_{xy})/a", "breaks": "v_F is 1e6 m/s, not c; Coulomb interactions are instantaneous, valleys carry opposite pseudo-fields, and the 'metric' is not dynamical.", "confidence": "current research", "strength": 2}
{"id": "C2042", "a": "05-relativity-and-gravitation/quantum-gravity/qft-in-curved-spacetime", "b": "08-condensed-matter/topological-matter/topological-semimetals", "name": "Mixed axial-gravitational anomaly in Weyl semimetals", "kind": "mechanism", "summary": "The chiral anomaly of Weyl fermions has a gravitational piece proportional to the curvature, which via Luttinger's temperature-as-gravitational-potential maps to a thermal-gradient term; positive magneto-thermoelectric conductance in NbP was reported as its signature.", "map": "\\nabla_\\mu j_5^\\mu=\\frac{e^2}{16\\pi^2}\\epsilon FF-\\frac{1}{384\\pi^2}\\epsilon^{\\mu\\nu\\rho\\sigma}R^\\alpha{}_{\\beta\\mu\\nu}R^\\beta{}_{\\alpha\\rho\\sigma}", "breaks": "Thermal-transport signals have competing phonon and conventional explanations; the anomaly attribution is contested.", "confidence": "current research", "strength": 2}
{"id": "C2043", "a": "05-relativity-and-gravitation/special-relativity/lorentz-transformations-and-spacetime", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "name": "Emergent Lorentz boosts with c -> v_F in graphene", "kind": "analogy", "summary": "Graphene's massless Dirac Hamiltonian is invariant under boosts with v_F replacing c; boosting away an in-plane E field predicts the collapse of Landau levels when E/B reaches v_F, as in E x B drift with E > cB.", "map": "\\beta=\\frac{E}{v_FB},\\quad E_n=\\pm\\sqrt{2e\\hbar v_F^2B|n|}\\,(1-\\beta^2)^{3/4}\\to0\\ \\text{as}\\ \\beta\\to1", "breaks": "Emergent symmetry only at low energy: trigonal warping, lattice and instantaneous Coulomb interaction break it.", "confidence": "established", "strength": 2}
{"id": "C2044", "a": "05-relativity-and-gravitation/special-relativity/lorentz-transformations-and-spacetime", "b": "08-condensed-matter/magnetism/spintronics", "name": "Spin-orbit coupling and Thomas precession", "kind": "mechanism", "summary": "An electron moving through an electric field sees a magnetic field B' = -v x E/c^2 in its rest frame; with the Thomas precession factor 1/2 this gives the spin-orbit coupling behind Rashba, Dresselhaus and spin Hall effects used in spintronics.", "map": "H_{\\rm SO}=\\frac{\\hbar}{4m^2c^2}\\boldsymbol\\sigma\\cdot(\\nabla V\\times\\mathbf p),\\quad H_R=\\alpha_R(\\boldsymbol\\sigma\\times\\mathbf k)\\cdot\\hat z", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2254", "a": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "Quantum-limited amplifiers for axion haloscopes", "kind": "method transfer", "summary": "Cavity haloscopes convert axions to microwave photons in a magnet; SQUID and Josephson parametric amplifiers (and squeezing) bring readout to the quantum limit, setting the scan rate in the micro-eV mass range.", "map": "P_{a\\to\\gamma}\\propto g_{a\\gamma\\gamma}^2\\frac{\\rho_a}{m_a}B^2VC\\,Q;\\ \\frac{df}{dt}\\propto\\frac{P^2}{T_{\\text{sys}}^2}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2255", "a": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "b": "08-condensed-matter/topological-matter/topological-insulators", "name": "Axion electrodynamics in topological magnets", "kind": "analogy", "summary": "The theta angle of a TI plays the role of the axion field; in magnetic TIs theta can fluctuate, giving a dynamical 'axion quasiparticle' whose coupling to E.B mirrors the QCD axion's photon coupling and has been proposed for dark-matter detection.", "map": "\\mathcal L=\\frac{\\alpha}{4\\pi^2}\\theta(\\mathbf x,t)\\mathbf E\\cdot\\mathbf B\\ \\leftrightarrow\\ -\\frac{g_{a\\gamma\\gamma}}{4}aF\\tilde F,\\ \\theta\\leftrightarrow a/f_a", "breaks": "The condensed-matter theta is an emergent, lattice-scale field with meV dynamics and no shift symmetry from a QCD anomaly; it cannot solve strong CP or be dark matter itself.", "confidence": "current research", "strength": 2}
{"id": "C2256", "a": "06-particle-physics/beyond-the-standard-model/dark-matter-particle-candidates", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "Sub-MeV dark matter scattering into phonons", "kind": "method transfer", "summary": "Below ~MeV, dark-matter momentum transfers match crystal phonon and magnon scales, so detection relies on condensed-matter response functions (dynamic structure factor, dielectric loss) rather than nuclear recoils.", "map": "\\Gamma\\propto\\int d^3q\\,\\frac{|F_{\\text{DM}}(q)|^2}{q^2}\\,\\mathrm{Im}\\!\\left[\\frac{-1}{\\epsilon(\\mathbf q,\\omega)}\\right]\\ (\\text{dielectric formalism})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2257", "a": "06-particle-physics/beyond-the-standard-model/extra-dimensions-and-hierarchy-problem", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Composite Higgs and top condensation from BCS", "kind": "historical", "summary": "Technicolor and top-quark condensation replace the elementary Higgs by a fermion-pair condensate formed by a gap equation, the BCS template (one author is Bardeen of BCS); the Higgs would be composite.", "map": "\\langle\\bar tt\\rangle\\neq0:\\ m_t\\ \\text{from gap equation},\\ v=246\\ \\text{GeV}\\leftrightarrow\\Delta", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2258", "a": "06-particle-physics/beyond-the-standard-model/grand-unification-and-proton-decay", "b": "08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids", "name": "Emergent magnetic monopoles in spin ice", "kind": "analogy", "summary": "Defects violating the two-in-two-out ice rule behave as deconfined magnetic charges with a Coulomb interaction, a laboratory analogue of the magnetic monopoles predicted by grand unification.", "map": "Q_m=\\pm\\frac{2\\mu}{a_d};\\ V(r)=\\frac{\\mu_0}{4\\pi}\\frac{Q_mQ_m'}{r}", "breaks": "Spin-ice monopoles are sources of H (div B = 0 still holds), their charge is not Dirac-quantized, and they are classical lattice defects rather than 't Hooft-Polyakov solitons of a broken gauge group.", "confidence": "established", "strength": 2}
{"id": "C2259", "a": "06-particle-physics/beyond-the-standard-model/grand-unification-and-proton-decay", "b": "08-condensed-matter/soft-matter/liquid-crystals", "name": "Hedgehogs, strings and the Kibble mechanism", "kind": "analogy", "summary": "Point and line defects in nematics are classified by the same homotopy groups as GUT monopoles and cosmic strings, and quenches through the isotropic-nematic transition test Kibble's defect-formation scenario.", "map": "\\pi_2(SO(3)/O(2))=\\mathbb Z\\ \\leftrightarrow\\ \\pi_2(G/H)=\\pi_1(H)\\ (\\text{monopoles});\\ n_{\\text{def}}\\sim\\xi^{-d}", "breaks": "Nematic defects have no gauge field, energy that scales with system size, and dissipative rather than relativistic dynamics.", "confidence": "established", "strength": 2}
{"id": "C2260", "a": "06-particle-physics/beyond-the-standard-model/supersymmetry", "b": "08-condensed-matter/topological-matter/topological-superconductors-and-majoranas", "name": "Emergent supersymmetry at topological boundaries", "kind": "analogy", "summary": "At the boundary of topological superconductors (or interacting Majorana chains) the critical point can be the tricritical Ising CFT or an N=1 Wess-Zumino theory, with exact emergent supersymmetry between bosonic order parameter and Majorana fermion.", "map": "c=\\tfrac{7}{10}\\ (\\text{tricritical Ising, }\\mathcal N=1\\ \\text{superconformal});\\ \\{Q,\\bar Q\\}\\sim P\\ \\text{emergent}", "breaks": "Supersymmetry is emergent only at fine-tuned criticality and low energy; there is no superpartner spectrum or SUSY breaking scale as in the MSSM.", "confidence": "current research", "strength": 2}
{"id": "C2261", "a": "06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Type-II NbTi magnets bend the LHC beams", "kind": "shared object", "summary": "The LHC's 8.3 T dipoles use NbTi, a type-II superconductor with strong flux pinning, cooled to 1.9 K in superfluid helium; the beam rigidity and the upper critical field set the reachable energy.", "map": "B\\rho=p/e:\\ 7\\ \\text{TeV}\\Rightarrow8.33\\ \\text{T};\\ B<B_{c2}(1.9\\ \\text{K})\\approx13\\ \\text{T (NbTi)}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2262", "a": "06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers", "b": "08-condensed-matter/crystals-and-electronic-structure/semiconductors", "name": "Silicon trackers are reverse-biased p-n junctions", "kind": "method transfer", "summary": "Pixel and strip trackers collect electron-hole pairs (3.6 eV per pair in Si) drifting in the depletion region of a reverse-biased p-n junction; radiation damage (displacement defects, type inversion) is semiconductor defect physics.", "map": "w=\\sqrt{\\frac{2\\epsilon_{Si}(V+V_{bi})}{qN_{\\text{eff}}}};\\ \\langle N_{eh}\\rangle\\approx\\frac{dE/dx\\cdot d}{3.6\\ \\text{eV}}\\approx80\\ \\mu\\text{m}^{-1}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2263", "a": "06-particle-physics/neutrino-physics/neutrino-mass-and-double-beta-decay", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "Cryogenic bolometers for 0nubb", "kind": "method transfer", "summary": "CUORE-type TeO2 crystals at ~10 mK act as calorimeters: the Debye T^3 heat capacity is tiny, so a 2.5 MeV decay raises the temperature measurably and gives keV resolution.", "map": "\\Delta T=\\frac{E}{C(T)},\\ C_V=\\frac{12\\pi^4}{5}Nk_B\\left(\\frac{T}{\\Theta_D}\\right)^3", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2264", "a": "06-particle-physics/neutrino-physics/neutrino-mass-and-double-beta-decay", "b": "08-condensed-matter/topological-matter/topological-superconductors-and-majoranas", "name": "Majorana neutrinos versus Majorana zero modes", "kind": "analogy", "summary": "Both rest on a self-conjugate fermion psi=psi^c (gamma=gamma-dagger): an elementary Majorana neutrino would violate lepton number in 0nubb, while zero-energy Majorana modes bound to vortices or wire ends obey non-abelian exchange statistics.", "map": "\\nu=\\nu^c\\ \\leftrightarrow\\ \\gamma=\\gamma^\\dagger,\\ c=\\tfrac12(\\gamma_1+i\\gamma_2)", "breaks": "Majorana zero modes are not propagating particles; they are non-abelian anyons bound to defects with no momentum or mass. Several condensed-matter Majorana claims have been retracted or reinterpreted, so evidence there is contested.", "confidence": "current research", "strength": 2}
{"id": "C2265", "a": "06-particle-physics/quantum-field-theory", "b": "08-condensed-matter/strongly-correlated-electrons", "name": "Many-body field theory: one language for both", "kind": "method transfer", "summary": "Propagators, Feynman diagrams, Matsubara sums, path integrals and the RG moved from particle QFT into many-body theory (Green's functions, Fermi liquids, Hubbard-Stratonovich), and emergent gauge theories flow back.", "map": "G(\\mathbf k,i\\omega_n)=\\frac{1}{i\\omega_n-\\xi_{\\mathbf k}-\\Sigma(\\mathbf k,i\\omega_n)}\\ \\leftrightarrow\\ \\frac{i}{p^2-m^2-\\Sigma(p^2)}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2266", "a": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "Phase slips and macroscopic tunnelling as instantons", "kind": "method transfer", "summary": "The escape of a current-biased Josephson phase from a tilted-washboard well is a Euclidean bounce, computed with the same instanton methods as false-vacuum decay; dissipation enters through a Caldeira-Leggett bath.", "map": "\\Gamma\\approx Ae^{-S_B/\\hbar},\\ S_B\\propto\\frac{\\Delta U}{\\omega_p}\\ \\leftrightarrow\\ \\Gamma/V\\propto e^{-S_E[\\phi_b]}\\ (\\text{Coleman})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2267", "a": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "b": "08-condensed-matter/topological-matter", "name": "Anomaly inflow and bulk-boundary correspondence", "kind": "identity", "summary": "Gapless boundary modes of topological phases carry 't Hooft anomalies that are cancelled by inflow from the bulk topological response (Callan-Harvey), so the classification of topological matter is a classification of anomalies.", "map": "\\partial_\\mu j^\\mu_{\\text{edge}}=\\frac{e^2}{2\\pi h}\\epsilon^{\\mu\\nu}F_{\\mu\\nu}\\cdot\\tfrac12\\ \\leftrightarrow\\ \\text{bulk Chern-Simons }\\frac{k}{4\\pi}AdA", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2268", "a": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "b": "08-condensed-matter/topological-matter/quantum-hall-effects", "name": "Chern-Simons theory and the parity anomaly", "kind": "identity", "summary": "The quantum Hall response is a Chern-Simons term whose level is the TKNN Chern number; Haldane's honeycomb model realized the 2+1D parity anomaly of a single massive Dirac fermion, the seed of Chern insulators.", "map": "\\mathcal L_{CS}=\\frac{k}{4\\pi}\\epsilon^{\\mu\\nu\\lambda}A_\\mu\\partial_\\nu A_\\lambda\\Rightarrow\\sigma_{xy}=k\\frac{e^2}{h};\\ \\sigma_{xy}^{\\text{Dirac}}=\\tfrac12\\mathrm{sgn}(m)\\tfrac{e^2}{h}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2269", "a": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "b": "08-condensed-matter/topological-matter/topological-insulators", "name": "Theta term and axion electrodynamics of 3D TIs", "kind": "identity", "summary": "The electromagnetic response of a time-reversal-invariant 3D topological insulator is a theta term with theta=pi, the same topological term as QCD's theta and the axion coupling; it implies a half-quantized surface Hall effect and the Witten effect.", "map": "\\mathcal L_\\theta=\\frac{\\theta e^2}{2\\pi h}\\mathbf E\\cdot\\mathbf B=\\frac{\\theta\\alpha}{4\\pi^2}\\mathbf E\\cdot\\mathbf B,\\ \\theta=\\pi;\\ \\sigma_{xy}^{\\text{surf}}=\\tfrac12\\tfrac{e^2}{h}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2270", "a": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "b": "08-condensed-matter/topological-matter/topological-semimetals", "name": "Chiral (ABJ) anomaly in Weyl semimetals", "kind": "identity", "summary": "Parallel E and B pump electrons between Weyl nodes of opposite chirality exactly as the Adler-Bell-Jackiw anomaly; the result is a negative longitudinal magnetoresistance.", "map": "\\frac{dN_\\pm}{dt}=\\pm\\frac{e^2}{h^2}\\mathbf E\\cdot\\mathbf B\\ \\leftrightarrow\\ \\partial_\\mu j_5^\\mu=\\frac{e^2}{16\\pi^2}\\epsilon^{\\mu\\nu\\rho\\sigma}F_{\\mu\\nu}F_{\\rho\\sigma}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2271", "a": "06-particle-physics/quantum-field-theory/canonical-and-path-integral-quantization", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "name": "Graphene's massless 2+1D Dirac fermions", "kind": "identity", "summary": "Near the K points graphene's tight-binding bands obey the massless 2+1D Dirac equation with c replaced by v_F~c/300 and spin replaced by sublattice pseudospin, giving Klein tunnelling, a half-integer Hall sequence and optical absorption pi*alpha.", "map": "H=\\hbar v_F\\,\\boldsymbol\\sigma\\cdot\\mathbf k\\ \\leftrightarrow\\ H_D=c\\,\\boldsymbol\\alpha\\cdot\\mathbf p;\\ \\alpha_g=\\frac{e^2}{4\\pi\\epsilon\\hbar v_F}\\approx2.2,\\ T=1-\\pi\\alpha", "breaks": "Lorentz invariance is only emergent at low energy; the Coulomb interaction is instantaneous (it travels at c, not v_F), so interacting graphene is not a relativistic QFT; valleys double the fermion count.", "confidence": "established", "strength": 3}
{"id": "C2272", "a": "06-particle-physics/quantum-field-theory/canonical-and-path-integral-quantization", "b": "08-condensed-matter/topological-matter/topological-semimetals", "name": "Weyl equation realized in TaAs", "kind": "identity", "summary": "Weyl semimetals host quasiparticles obeying the two-component Weyl equation that elementary physics never confirmed (neutrinos turned out massive); each node is a monopole of Berry curvature with chirality +-1.", "map": "H_W=\\pm\\hbar v_F\\boldsymbol\\sigma\\cdot\\mathbf k\\ \\leftrightarrow\\ i\\bar\\sigma^\\mu\\partial_\\mu\\psi_L=0", "breaks": "Solid-state Weyl nodes can be tilted (type II), anisotropic and offset in energy, since there is no Lorentz symmetry, and their total number is fixed by the lattice.", "confidence": "established", "strength": 3}
{"id": "C2273", "a": "06-particle-physics/quantum-field-theory/conformal-field-theory", "b": "08-condensed-matter/strongly-correlated-electrons/heavy-fermions-and-kondo-physics", "name": "Boundary CFT solves the multichannel Kondo problem", "kind": "method transfer", "summary": "Affleck and Ludwig treated the impurity as a conformal boundary condition of a 1+1D chiral CFT, obtaining the non-Fermi-liquid exponents and residual entropy of the overscreened multichannel Kondo fixed point.", "map": "S_{\\text{imp}}=\\ln\\sqrt2\\ (k=2\\ \\text{channel});\\ \\rho(T)-\\rho(0)\\propto T^{\\Delta}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2274", "a": "06-particle-physics/quantum-field-theory/conformal-field-theory", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "Entanglement scaling reads off the central charge", "kind": "method transfer", "summary": "At a 1+1D critical point the entanglement entropy grows as (c/3) ln L, so DMRG and tensor-network simulations extract CFT central charges and operator dimensions directly from ground states.", "map": "S_A=\\frac{c}{3}\\ln\\frac{L}{a}+c'\\ (\\text{periodic: }c/3,\\ \\text{open: }c/6)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2275", "a": "06-particle-physics/quantum-field-theory/conformal-field-theory", "b": "08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals", "name": "Quantum critical points as CFTs", "kind": "method transfer", "summary": "Many z=1 quantum critical points are described by conformal field theories (e.g. O(N) Wilson-Fisher in 2+1D) whose finite-T response is universal and Planckian (tau ~ hbar/k_BT); holographic CFTs model strongly coupled transport.", "map": "\\frac{\\hbar}{\\tau}\\approx\\alpha k_BT;\\ \\sigma(\\omega,T)=\\frac{e^2}{\\hbar}\\Sigma(\\hbar\\omega/k_BT)\\ (\\text{2+1D CFT})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2276", "a": "06-particle-physics/quantum-field-theory/conformal-field-theory", "b": "08-condensed-matter/topological-matter/quantum-hall-effects", "name": "FQH edges and wavefunctions from CFT", "kind": "identity", "summary": "Edges of quantum Hall states are chiral CFTs, and bulk wavefunctions are CFT conformal blocks: the Laughlin state from a U(1) boson, the Moore-Read Pfaffian from the Ising CFT, whose sigma fields become non-abelian anyons.", "map": "\\Psi_{MR}=\\mathrm{Pf}\\!\\left(\\frac{1}{z_i-z_j}\\right)\\prod_{i<j}(z_i-z_j)^2e^{-\\sum|z|^2/4\\ell_B^2};\\ c_{\\text{edge}}=1\\ (\\text{Laughlin})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2277", "a": "06-particle-physics/quantum-field-theory/effective-field-theory", "b": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "name": "Goldstone EFT: pions and magnons", "kind": "method transfer", "summary": "Chiral perturbation theory's EFT of Goldstone bosons describes magnons: antiferromagnetic magnons are relativistic-like (O(3) sigma model, omega ~ k) while ferromagnetic ones are type-B Goldstones (omega ~ k^2) that count once per pair of broken generators.", "map": "n_A+2n_B=n_{BG}\\ (\\text{Watanabe-Murayama});\\ \\mathcal L=\\tfrac{\\rho_s}{2}(\\partial_\\mu\\mathbf n)^2\\ \\leftrightarrow\\ \\tfrac{f_\\pi^2}{4}\\mathrm{Tr}\\,\\partial U\\partial U^\\dagger", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2278", "a": "06-particle-physics/quantum-field-theory/effective-field-theory", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Fermi-surface EFT: BCS as the marginal instability", "kind": "method transfer", "summary": "Treating the Fermi liquid as an EFT with RG scaling toward the Fermi surface shows only forward and BCS couplings survive, and an attractive BCS coupling is marginally relevant and runs to a gap.", "map": "\\frac{dV_{BCS}}{d\\ln(\\Lambda_0/\\Lambda)}=-N(0)V_{BCS}^2\\Rightarrow\\Delta\\sim\\omega_De^{-1/N(0)|V|}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2279", "a": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "b": "08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids", "name": "Emergent QED in quantum spin ice", "kind": "identity", "summary": "The low-energy theory of a U(1) quantum spin liquid on the pyrochlore lattice is compact U(1) gauge theory: gapless emergent photons with omega ~ k, gapped electric charges (spinons) and magnetic monopoles.", "map": "H_{\\text{eff}}=\\frac{U}{2}\\sum\\mathbf E^2-K\\sum_{\\hexagon}\\cos(\\nabla\\times\\mathbf A),\\ \\omega=c_{\\text{em}}k", "breaks": "The emergent speed of light is ~meV scale and lattice-cut off; the emergent fine-structure constant and charges are not tied to QED's, and Lorentz invariance is only approximate.", "confidence": "current research", "strength": 2}
{"id": "C2280", "a": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "b": "08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order", "name": "Topological order as deconfined lattice gauge theory", "kind": "identity", "summary": "Z2 topological order (toric code, Z2 spin liquids) is the deconfined phase of Wegner's Z2 lattice gauge theory; anyons are its electric charges and fluxes, and the Wilson-loop perimeter law is the condensed-matter signature of deconfinement.", "map": "H_{TC}=-\\sum_vA_v-\\sum_pB_p\\ \\leftrightarrow\\ \\text{Gauss law }A_v=1,\\ B_p=\\prod_{\\square}\\sigma^z\\ (\\text{plaquette})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2281", "a": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Ginzburg-Landau is the abelian Higgs model", "kind": "identity", "summary": "Ginzburg-Landau theory is the abelian Higgs model with charge 2e; Abrikosov vortices are Nielsen-Olesen strings and the type-I/II boundary kappa=1/sqrt2 is the BPS point where vortices do not interact.", "map": "F=|(\\nabla-2ie\\mathbf A)\\psi|^2+a|\\psi|^2+\\tfrac b2|\\psi|^4+\\tfrac{B^2}{2\\mu_0}\\ \\leftrightarrow\\ \\mathcal L_{AH};\\ \\kappa=\\lambda/\\xi=1/\\sqrt2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2282", "a": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "b": "08-condensed-matter/superconductivity/cuprate-high-tc-superconductors", "name": "Emergent gauge fields in the doped Mott insulator", "kind": "method transfer", "summary": "Slave-particle (parton) descriptions of the cuprates split the electron into spinons and holons coupled by an emergent U(1) or SU(2) gauge field, importing gauge-theory confinement and Higgs phases into high-Tc theory.", "map": "c_{i\\sigma}=b_i^\\dagger f_{i\\sigma},\\ \\sum_\\sigma f^\\dagger f+b^\\dagger b=1\\ (\\text{gauge constraint})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2283", "a": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "Berry connection as a gauge field on the Brillouin zone", "kind": "identity", "summary": "The Berry connection is a U(1) (or, for degenerate bands, Wilczek-Zee non-abelian) gauge field over momentum space; Chern numbers are its first Chern class, the same topology as monopole and instanton charges.", "map": "\\mathcal A_n=i\\langle u_n|\\nabla_{\\mathbf k}u_n\\rangle,\\ \\Omega=\\nabla\\times\\mathcal A,\\ C=\\frac{1}{2\\pi}\\int_{BZ}\\Omega\\,d^2k\\in\\mathbb Z", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2284", "a": "06-particle-physics/quantum-field-theory/lattice-field-theory", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "Shared Monte Carlo, sign problem and tensor networks", "kind": "method transfer", "summary": "Lattice QCD and correlated-electron numerics share hybrid/determinant Monte Carlo and the fermion sign problem; tensor networks developed for spin chains now simulate lattice gauge theories at finite density and in real time.", "map": "\\langle O\\rangle=\\frac{\\int O\\det M\\,e^{-S}}{\\int\\det M\\,e^{-S}},\\ \\det M\\ \\text{not positive}\\Rightarrow\\text{sign problem}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2285", "a": "06-particle-physics/quantum-field-theory/lattice-field-theory", "b": "08-condensed-matter/topological-matter/topological-insulators", "name": "Domain-wall fermions are topological boundary states", "kind": "identity", "summary": "Kaplan's domain-wall fermions get lattice chiral fermions as zero modes bound to a mass domain wall in one higher dimension, the same Jackiw-Rebbi mechanism that produces protected surface Dirac cones of topological insulators.", "map": "(i\\gamma^\\mu\\partial_\\mu-m(s))\\psi=0,\\ m(s)\\to\\pm m\\ \\Rightarrow\\ \\psi_0\\propto e^{-\\int^s m(s')ds'}\\ (\\text{chiral zero mode})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2286", "a": "06-particle-physics/quantum-field-theory/lattice-field-theory", "b": "08-condensed-matter/topological-matter/topological-semimetals", "name": "Nielsen-Ninomiya doubling forces paired Weyl nodes", "kind": "identity", "summary": "The no-go theorem that lattice chiral fermions come in pairs of opposite chirality is the reason Weyl nodes in a crystal always appear in pairs, and Nielsen and Ninomiya themselves proposed the crystal chiral anomaly.", "map": "\\sum_{\\text{nodes}}\\chi_i=0\\ (\\text{compact Brillouin zone})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2287", "a": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "name": "Running Fermi velocity in graphene", "kind": "method transfer", "summary": "Coulomb interactions renormalize graphene's Fermi velocity logarithmically, like a running coupling, because alpha_g is marginal; suspended graphene shows the predicted log enhancement near the Dirac point.", "map": "v_F(k)=v_F(\\Lambda)\\left[1+\\frac{\\alpha_g}{4}\\ln\\frac{\\Lambda}{k}\\right]", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2288", "a": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "b": "08-condensed-matter/strongly-correlated-electrons/heavy-fermions-and-kondo-physics", "name": "Kondo temperature as dimensional transmutation", "kind": "identity", "summary": "The antiferromagnetic Kondo coupling is marginally relevant, so it grows at low energy like an asymptotically free coupling and generates a scale T_K exactly as Lambda_QCD emerges; Wilson's numerical RG solved it.", "map": "\\frac{dJ}{d\\ln D}=-\\rho J^2\\Rightarrow T_K\\sim De^{-1/\\rho J}\\ \\leftrightarrow\\ \\Lambda_{QCD}=\\mu\\,e^{-8\\pi^2/(b_0g^2(\\mu))}", "breaks": "Kondo is a 0+1D impurity problem with no gauge field or confinement; the strong-coupling fixed point is a screened singlet (Fermi liquid), not a confined hadron spectrum.", "confidence": "established", "strength": 3}
{"id": "C2289", "a": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "DMRG born from the failure of real-space RG", "kind": "historical", "summary": "White's DMRG replaced Wilson-style energy truncation by density-matrix truncation, turning real-space renormalization into the most accurate 1D many-body method and the seed of tensor-network RG.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2290", "a": "06-particle-physics/standard-model", "b": "08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order", "name": "Could photons and electrons be emergent?", "kind": "analogy", "summary": "String-net condensation produces emergent U(1) gauge bosons and fermionic charges from local bosonic spins, suggesting the Standard Model's gauge fields and fermions might themselves be emergent.", "map": "", "breaks": "No string-net model reproduces chiral fermions, non-abelian SU(3)xSU(2)xU(1), or exact Lorentz invariance; chiral gauge theories resist lattice regularization.", "confidence": "proposed", "strength": 1}
{"id": "C2291", "a": "06-particle-physics/standard-model", "b": "08-condensed-matter/superconductivity", "name": "Higgs mechanism first appeared as the Meissner effect", "kind": "historical", "summary": "The idea that a condensate gives a gauge field mass migrated from superconductivity (London, Nambu, Anderson) to the Standard Model's electroweak sector.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2292", "a": "06-particle-physics/standard-model/higgs-boson", "b": "08-condensed-matter/superconductivity", "name": "Anderson-Higgs mechanism: photon mass = W mass", "kind": "identity", "summary": "A superconductor's Cooper-pair condensate eats the phase Goldstone mode and gives the photon a mass 1/lambda_L (Meissner effect), the same abelian Higgs mechanism that gives W and Z masses from the Higgs vev.", "map": "m_\\gamma c^2=\\frac{\\hbar c}{\\lambda_L},\\ \\lambda_L^{-2}=\\mu_0n_se^2/m\\ \\leftrightarrow\\ m_W=\\tfrac12gv;\\ \\Delta\\leftrightarrow\\langle H\\rangle,\\ 2e\\leftrightarrow g", "breaks": "The SC condensate is a composite of electrons, non-relativistic and in a medium with a preferred frame; the electroweak condensate is (as far as known) elementary and Lorentz invariant, and its gauge group is non-abelian.", "confidence": "established", "strength": 3}
{"id": "C2293", "a": "06-particle-physics/standard-model/higgs-boson", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Higgs amplitude mode in superconductors", "kind": "identity", "summary": "The Higgs boson is the amplitude oscillation of the condensate; superconductors have the same mode at energy 2Delta, observed in Raman and terahertz pump-probe experiments.", "map": "m_h^2=2\\lambda v^2\\ \\leftrightarrow\\ \\omega_H=2\\Delta;\\ \\delta|\\psi|\\ \\text{(amplitude)}\\ \\text{vs}\\ \\delta\\phi\\ \\text{(eaten phase)}", "breaks": "In a superconductor the mode sits at the pair-breaking edge and can decay into quasiparticles; its observation needs coupling via a CDW or nonlinear drive since it is Raman- but not dipole-active.", "confidence": "current research", "strength": 2}
{"id": "C2294", "a": "06-particle-physics/standard-model/quantum-chromodynamics", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Color superconductivity in dense quark matter", "kind": "mechanism", "summary": "At high baryon density attractive one-gluon exchange in the color antitriplet channel makes quarks Cooper-pair near the Fermi surface; in the CFL phase the diquark condensate Higgses all eight gluons (color Meissner effect).", "map": "\\langle q^a_{i\\alpha}q^b_{j\\beta}\\rangle\\propto\\Delta\\,\\epsilon^{abI}\\epsilon_{\\alpha\\beta I}\\ (\\text{CFL});\\ \\Delta\\sim10\\text{-}100\\ \\text{MeV}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2295", "a": "06-particle-physics/standard-model/quantum-chromodynamics", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Confinement as a dual Meissner effect", "kind": "analogy", "summary": "If chromomagnetic monopoles condense, chromoelectric flux is squeezed into tubes just as magnetic flux is in a type-II superconductor, giving a linear quark potential with string tension sigma.", "map": "V(r)\\approx\\sigma r,\\ \\sigma\\approx0.18\\ \\text{GeV}^2\\ \\leftrightarrow\\ \\text{vortex energy per length }\\varepsilon_1\\approx\\frac{\\Phi_0^2}{4\\pi\\mu_0\\lambda^2}\\ln\\kappa", "breaks": "The roles of E and B are swapped, the gauge group is non-abelian, and monopole condensation in QCD is gauge-dependent and unproven analytically.", "confidence": "current research", "strength": 2}
{"id": "C2296", "a": "06-particle-physics/standard-model/quantum-chromodynamics", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "NJL: chiral symmetry breaking modelled on BCS", "kind": "historical", "summary": "Nambu and Jona-Lasinio built dynamical mass generation for nucleons by direct analogy with the BCS gap equation; the massless Goldstone mode of the analogy became the pion, a precursor of QCD chiral symmetry breaking.", "map": "\\Delta=gN(0)\\int_0^{\\omega_D}\\frac{\\Delta\\,d\\xi}{\\sqrt{\\xi^2+\\Delta^2}}\\ \\leftrightarrow\\ M=\\frac{2G}{\\pi^2}\\int_0^\\Lambda\\frac{M\\,p^2dp}{\\sqrt{p^2+M^2}}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2449", "a": "07-nuclear-physics/applied-nuclear-physics/nuclear-reactors-and-energy", "b": "08-condensed-matter/crystals-and-electronic-structure", "name": "Radiation damage in reactor materials", "kind": "mechanism", "summary": "Fast neutrons create displacement cascades in fuel cladding, steels and graphite; point-defect production, swelling, embrittlement and stored Wigner energy are solid-state physics that limits reactor lifetimes and fusion first walls.", "map": "N_d=\\frac{E_{\\rm dam}}{2E_d}\\ \\text{(Kinchin-Pease)};\\ \\text{dpa}=\\sigma_d\\phi t", "breaks": "Displacement counts overestimate surviving defects because of in-cascade recombination, so molecular dynamics is needed.", "confidence": "established", "strength": 2}
{"id": "C2450", "a": "07-nuclear-physics/applied-nuclear-physics/nuclear-reactors-and-energy", "b": "08-condensed-matter/crystals-and-electronic-structure/semiconductors", "name": "Neutron transmutation doping of silicon", "kind": "method transfer", "summary": "Irradiating float-zone silicon in a reactor turns 30Si into 31P by neutron capture and beta decay, giving the most uniform n-type doping available, used for high-power devices and thyristors.", "map": "{}^{30}\\mathrm{Si}(n,\\gamma){}^{31}\\mathrm{Si}\\xrightarrow{\\beta^-,\\,2.6\\,\\mathrm h}{}^{31}\\mathrm P;\\ N_P=N_{30}\\sigma_{\\rm th}\\phi t", "breaks": "Only n-type doping is possible, and the lattice damage has to be annealed.", "confidence": "established", "strength": 2}
{"id": "C2451", "a": "07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry", "b": "08-condensed-matter/crystals-and-electronic-structure/semiconductors", "name": "Semiconductor and scintillator radiation detectors", "kind": "method transfer", "summary": "HPGe and Si detectors are reverse-biased p-n junctions whose energy resolution is set by electron-hole pair statistics (about 3 eV per pair, Fano factor ~0.1); scintillators and halide-perovskite detectors depend on excitons, traps and band gaps.", "map": "w\\approx2.8E_g+0.6\\ \\text{eV};\\ \\frac{\\sigma_E}{E}=2.355\\sqrt{\\frac{Fw}{E}};\\ W_{\\rm dep}=\\sqrt{\\frac{2\\epsilon V}{eN_d}}", "breaks": "Detector-grade operation needs ultrapure crystals with long carrier lifetimes and radiation hardness, priorities different from electronic devices.", "confidence": "established", "strength": 3}
{"id": "C2452", "a": "07-nuclear-physics/heavy-ion-physics/collective-flow-and-hydrodynamics", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "name": "Relativistic viscous hydro in the graphene Dirac fluid", "kind": "identity", "summary": "Near charge neutrality graphene electrons form a Dirac fluid described by the same relativistic viscous hydrodynamics as the QGP, with c replaced by v_F; it was predicted and then measured to be a nearly perfect fluid with low eta/s that violates Wiedemann-Franz.", "map": "\\partial_\\mu T^{\\mu\\nu}=F^{\\nu\\lambda}J_\\lambda,\\ T^{\\mu\\nu}=(\\varepsilon+P)u^\\mu u^\\nu+Pg^{\\mu\\nu}+\\pi^{\\mu\\nu},\\ c\\to v_F\\approx c/300", "breaks": "The graphene fluid is 2D, charged with long-range Coulomb forces, and loses momentum to impurities and phonons; the QGP is an expanding, short-lived drop with no lattice.", "confidence": "current research", "strength": 3}
{"id": "C2453", "a": "07-nuclear-physics/heavy-ion-physics/qcd-phase-diagram-and-critical-point", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Colour superconductivity in dense quark matter", "kind": "mechanism", "summary": "At high baryon density the attractive colour-antitriplet channel makes the quark Fermi surface unstable to BCS pairing; the colour-flavour-locked phase is a colour superconductor in which gluons acquire Meissner masses and chiral symmetry breaks, a candidate for neutron-star cores.", "map": "\\langle q^a_{\\alpha}q^b_{\\beta}\\rangle\\propto\\Delta\\,\\epsilon^{abI}\\epsilon_{\\alpha\\beta I};\\ \\Delta\\sim\\mu g^{-5}e^{-3\\pi^2/\\sqrt2g}\\ \\text{(weak coupling)}", "breaks": "The condensate breaks a non-abelian gauge symmetry and is under control only at asymptotic density; at neutron-star densities it is model-dependent and has no direct experimental confirmation.", "confidence": "established", "strength": 3}
{"id": "C2454", "a": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "b": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "name": "Viscous electron flow and eta/s in metals vs QGP", "kind": "analogy", "summary": "In ultraclean conductors electron-electron collisions dominate and charge flows hydrodynamically (Gurzhi effect, negative nonlocal resistance), giving measured electron viscosities that can be set against QGP eta/s in the same Navier-Stokes framework.", "map": "\\nu=\\eta/\\rho\\approx\\tfrac14v_F\\ell_{ee};\\ \\text{hydro window }\\ell_{ee}\\ll W\\ll\\ell_{\\rm mr}", "breaks": "Fermi-liquid electrons are weakly coupled with a long l_ee, so their eta/s is far above the QGP value; momentum relaxation at boundaries and impurities has no QGP counterpart.", "confidence": "current research", "strength": 2}
{"id": "C2455", "a": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "b": "08-condensed-matter/magnetism/spintronics", "name": "Spin-vorticity: Lambda polarization and Barnett effect", "kind": "mechanism", "summary": "Global Lambda polarization in off-central collisions shows the QGP is the most vortical fluid known; it aligns spins through the same spin-rotation coupling as the Barnett effect and spin hydrodynamic generation in liquid metals.", "map": "H=-\\boldsymbol\\omega\\cdot\\mathbf S;\\ P_\\Lambda\\approx\\frac{\\hbar\\omega}{2k_BT},\\ \\omega\\sim10^{22}\\ \\text{s}^{-1}", "breaks": "QGP polarization is read from the hadronized final state of a ~10 fm/c fluid in local equilibrium; the spintronic versions involve electron spin, spin-orbit coupling and dissipative spin currents.", "confidence": "current research", "strength": 2}
{"id": "C2456", "a": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "b": "08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals", "name": "Planckian dissipation: QGP and strange metals", "kind": "analogy", "summary": "The QGP's eta/s near hbar/(4 pi k_B) and the strange-metal scattering rate hbar/tau of order k_BT are both 'Planckian' transport set by hbar and T alone, and gauge/gravity duality has been applied to both as a model of strongly coupled matter without quasiparticles.", "map": "\\frac{\\eta}{s}\\gtrsim\\frac{\\hbar}{4\\pi k_B}\\ \\leftrightarrow\\ \\frac{\\hbar}{\\tau}\\approx\\alpha k_BT,\\ \\alpha\\sim1", "breaks": "Strange-metal resistivity needs momentum relaxation by the lattice and disorder, while eta/s is a momentum-conserving diffusivity; the KSS value is not a proven bound, and holographic models are neither QCD nor cuprates.", "confidence": "current research", "strength": 2}
{"id": "C2457", "a": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Chiral condensate modelled on the BCS gap (NJL)", "kind": "historical", "summary": "Nambu and Jona-Lasinio built dynamical chiral symmetry breaking by direct analogy with BCS: the quark mass gap is a fermion-pair condensate, and its melting at the QCD crossover is the chiral-restoration signature studied in heavy-ion collisions.", "map": "m^*=m_0-2G\\langle\\bar qq\\rangle\\ \\leftrightarrow\\ \\Delta=-V\\sum_k\\langle c_{-k\\downarrow}c_{k\\uparrow}\\rangle", "breaks": "The chiral condensate pairs particles with antiparticles and breaks a global, not a gauge, symmetry, so it gives Goldstone pions instead of a Meissner effect; the QCD transition is a crossover.", "confidence": "established", "strength": 2}
{"id": "C2458", "a": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "b": "08-condensed-matter/topological-matter/topological-semimetals", "name": "Chiral anomaly: CME in QGP and Weyl semimetals", "kind": "identity", "summary": "The axial anomaly that would drive a current along B in a chirally imbalanced QGP (the chiral magnetic effect) is the same anomaly equation behind the negative longitudinal magnetoresistance of Weyl and Dirac semimetals, where the effect is observed; in heavy-ion collisions the isobar run found no signal beyond background.", "map": "\\partial_\\mu j_5^\\mu=\\frac{e^2}{2\\pi^2\\hbar^2c}\\mathbf E\\cdot\\mathbf B;\\ \\mathbf j=\\frac{e^2}{2\\pi^2}\\mu_5\\mathbf B", "breaks": "In the QGP the imbalance comes from gluon topological fluctuations and B lasts ~0.1 fm/c; in Weyl metals it is pumped by parallel E and B and relaxed by internode scattering, and lattice Weyl nodes come in pairs (Nielsen-Ninomiya).", "confidence": "current research", "strength": 3}
{"id": "C2459", "a": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "b": "08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons", "name": "Band theory of dripped neutrons in the inner crust", "kind": "method transfer", "summary": "Free neutrons in the inner crust move in the periodic potential of the nuclear lattice, so Bloch band structure gives them an effective mass and entrainment by the crust; band calculations find most neutrons entrained, which feeds the glitch angular-momentum budget.", "map": "\\psi_{n\\mathbf k}(\\mathbf r+\\mathbf R)=e^{i\\mathbf k\\cdot\\mathbf R}\\psi_{n\\mathbf k}(\\mathbf r);\\ n_n^{c}\\propto\\sum_{n\\mathbf k}|\\nabla_{\\mathbf k}\\epsilon_{n\\mathbf k}|^2\\delta(\\epsilon-\\mu)", "breaks": "Pairing, with a gap comparable to band splittings, smears band effects and is often neglected in band calculations; that is the main open question.", "confidence": "current research", "strength": 2}
{"id": "C2460", "a": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "b": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "name": "Neutron-star crust as a bcc Coulomb crystal", "kind": "shared object", "summary": "The outer crust is a body-centred-cubic lattice of neutron-rich nuclei in a degenerate relativistic electron gas; its composition follows from minimizing Madelung plus nuclear energies, and inner-crust calculations use the Wigner-Seitz cell method taken from solid-state physics.", "map": "E_L=-C_M\\frac{Z^2e^2}{a},\\ C_M^{\\rm bcc}\\approx0.8959;\\ \\Gamma=\\frac{Z^2e^2}{ak_BT}>175\\Rightarrow\\text{crystal}", "breaks": "The lattice 'atoms' are bare nuclei in a uniform relativistic electron gas (no chemical bonding), and the inner crust is penetrated by a neutron superfluid.", "confidence": "established", "strength": 2}
{"id": "C2461", "a": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "b": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "name": "Crust transport: conductivity, impurities and field decay", "kind": "method transfer", "summary": "Crust thermal and electrical conductivities are computed with metal transport theory (electron-phonon and electron-impurity scattering, Wiedemann-Franz); crust cooling after accretion outbursts shows a well-ordered, high-conductivity lattice, while a disordered pasta layer would be highly resistive.", "map": "\\kappa=\\frac{\\pi^2k_B^2T}{3e^2}\\sigma;\\ \\nu_{ei}^{\\rm imp}\\propto Q_{\\rm imp}=\\langle(Z-\\langle Z\\rangle)^2\\rangle", "breaks": "The electrons are ultra-relativistic and fields reach 1e15 G, so magnetized quantum transport goes beyond terrestrial regimes.", "confidence": "current research", "strength": 2}
{"id": "C2462", "a": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "Crust elasticity, phonons and magnetar oscillations", "kind": "mechanism", "summary": "The crust shear modulus and breaking strain come from the lattice dynamics of the Coulomb crystal (molecular dynamics gives a strain of ~0.1, far above terrestrial metals); crust torsional modes are candidates for magnetar-flare QPOs, and crust strength limits the mountains that would radiate gravitational waves.", "map": "\\mu_{\\rm eff}\\approx0.12\\,\\frac{n_iZ^2e^2}{a};\\ v_t=\\sqrt{\\mu/\\rho};\\ C_V^{\\rm lattice}\\propto T^3", "breaks": "Phonons of a Coulomb crystal in a compressible electron background have a plasma-frequency longitudinal branch, unlike the acoustic phonons of ordinary solids; superfluid neutrons add mixed modes.", "confidence": "current research", "strength": 2}
{"id": "C2463", "a": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "b": "08-condensed-matter/soft-matter/liquid-crystals", "name": "Nuclear pasta as liquid-crystal-like matter", "kind": "analogy", "summary": "Rod and slab pasta phases have orientational and partial positional order like columnar and smectic liquid crystals, so their elasticity and topological defects (screw dislocations in slabs) are described with liquid-crystal elastic theory; this sets the pasta shear modulus and viscosity.", "map": "F_{\\rm el}=\\tfrac12B(\\partial_zu)^2+\\tfrac12K(\\nabla_\\perp^2u)^2\\ \\text{(smectic-like slabs)}", "breaks": "Pasta units are nuclear clusters ordered by Coulomb frustration, not anisotropic molecules; there is no molecular director and thermal fluctuations are weak.", "confidence": "current research", "strength": 2}
{"id": "C2464", "a": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "b": "08-condensed-matter/soft-matter/polymers", "name": "Nuclear pasta and block-copolymer microphase separation", "kind": "analogy", "summary": "Pasta phases (spheres, rods, slabs, gyroid-like and inverted) come from competition between nuclear surface tension and long-range Coulomb energy; block-copolymer melts show the same morphology sequence because the Ohta-Kawasaki functional has the same short-range plus Coulomb-kernel structure.", "map": "F=\\sigma\\!\\int\\!dA+\\frac{\\alpha}{2}\\!\\iint\\!\\delta\\phi(\\mathbf r)G(\\mathbf r-\\mathbf r')\\delta\\phi(\\mathbf r'),\\ \\nabla^2G=-\\delta", "breaks": "Pasta is cold, quantum-degenerate matter with shell effects and electron screening; copolymer morphology is set by chain entropy and connectivity at finite temperature, and kinetics and defects differ.", "confidence": "established", "strength": 2}