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

### Density functional theory · `knowledge/08-condensed-matter/crystals-and-electronic-structure/density-functional-theory`

**Scope.** Hohenberg–Kohn theorems, Kohn–Sham auxiliary system, LDA, GGA (PBE), meta-GGA (SCAN), hybrid functionals (HSE), DFT+U, van der Waals corrections, band-gap problem, plane waves and pseudopotentials, PAW, TDDFT, GW and DMFT beyond DFT, high-throughput materials databases, ML potentials trained on DFT.

**Core ideas.**
- The ground-state density uniquely determines all properties; the energy is minimized by the true density.
- Kohn–Sham maps the interacting problem onto non-interacting electrons in an effective potential — exact if $E_{xc}$ were known.
- Semi-local functionals underestimate band gaps and fail for strongly correlated (Mott) systems.

**Key equations.**
$$\left[-\frac{\hbar^2}{2m}\nabla^2+v_{\text{ext}}+v_H[n]+v_{xc}[n]\right]\phi_i=\varepsilon_i\phi_i,\qquad n(\mathbf r)=\sum_i^{\text{occ}}|\phi_i|^2$$

**See also.** [Quantum chemistry methods](knowledge/11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods/README.md) · [Numerical many-body methods](knowledge/08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods/README.md)

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

### Altermagnetism · `knowledge/08-condensed-matter/magnetism/altermagnetism`

**Scope.** Spin-group symmetry classification, sublattices related by rotation (not translation or inversion), d-, g- and i-wave spin splitting, candidate materials (RuO₂ — contested, MnTe, CrSb, KV₂Se₂O), ARPES confirmation (2024), anomalous Hall effect without net magnetization, spin-splitter torques, potential for fast, stray-field-free spintronics.

**Core ideas.**
- In altermagnets opposite-spin sublattices are connected by a rotation, so bands are spin-split in momentum space with alternating sign.
- Net magnetization vanishes, yet time-reversal symmetry is broken in the band structure.
- Splittings can reach hundreds of meV — non-relativistic, unlike spin–orbit effects.

**Key equations.**
$$E_\uparrow(\mathbf k)-E_\downarrow(\mathbf k)\propto k_xk_y\ (d\text{-wave}),\qquad \sum_{\mathbf k}\left[E_\uparrow-E_\downarrow\right]=0$$

**See also.** [Spintronics](knowledge/08-condensed-matter/magnetism/spintronics/README.md) · [Lie groups and symmetry](knowledge/00-foundations/symmetry-and-group-theory/lie-groups-and-representations/README.md)

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

### Active matter · `knowledge/08-condensed-matter/soft-matter/active-matter`

**Scope.** Vicsek model and Toner–Tu theory of flocks, active Brownian particles, motility-induced phase separation, active nematics and turbulence (microtubule–kinesin), bacterial suspensions, Janus colloids, odd elasticity and non-reciprocal interactions, entropy production in active systems, robotic swarms.

**Core ideas.**
- Energy injected at the particle level breaks detailed balance; equilibrium no-go theorems (Mermin–Wagner) can be evaded — 2D flocks order.
- Self-propelled particles slow down in crowds, causing phase separation without attraction.
- Active stresses destabilize nematic order, producing chaotic "active turbulence" at low Reynolds number.

**Key equations.**
$$\dot{\mathbf r}_i=v_0\hat{\mathbf e}(\theta_i)+\sqrt{2D_t}\boldsymbol\xi_i,\qquad \theta_i(t+1)=\langle\theta_j\rangle_{|r_{ij}|<R}+\eta_i\ (\text{Vicsek})$$

**See also.** [Synchronization and pattern formation](knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation/README.md) · [Driven systems](knowledge/03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/driven-systems-and-nonequilibrium-steady-states/README.md)

### Colloids and granular matter · `knowledge/08-condensed-matter/soft-matter/colloids-and-granular-matter`

**Scope.** Brownian motion and Stokes–Einstein diffusion, DLVO theory, depletion attraction (Asakura–Oosawa), hard-sphere freezing at $\phi\approx0.494$, colloidal glasses and gels, self-assembly with patchy particles, granular matter: force chains, Janssen effect in silos, segregation (Brazil-nut effect), granular flow rheology ($\mu(I)$), dilatancy.

**Core ideas.**
- Colloids are "big atoms" — slow and visible, so phase transitions can be watched in real space.
- Purely entropic hard spheres crystallize: ordering increases free volume per particle.
- Grains are athermal; temperature is irrelevant, friction and geometry dominate.

**Key equations.**
$$D=\frac{k_BT}{6\pi\eta a},\qquad \mu(I)=\mu_s+\frac{\mu_2-\mu_s}{1+I_0/I},\ I=\frac{\dot\gamma d}{\sqrt{P/\rho}}$$

**See also.** [Stochastic processes](knowledge/03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics/README.md) · [Glasses and jamming](knowledge/08-condensed-matter/soft-matter/glasses-and-jamming/README.md)

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


---

# Packet 08-1 (100 records)

{"id": "C0321", "a": "00-foundations/computational-physics", "b": "08-condensed-matter/crystals-and-electronic-structure/density-functional-theory", "name": "DFT as computational physics' largest application", "kind": "method transfer", "summary": "Kohn-Sham DFT with plane waves, pseudopotentials, FFTs and iterative eigensolvers is among the most heavily used computational methods in all of science; numerical analysis (basis convergence, k-point sampling, self-consistency mixing) controls its accuracy.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0322", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "08-condensed-matter/crystals-and-electronic-structure/density-functional-theory", "name": "Machine-learned interatomic potentials trained on DFT", "kind": "method transfer", "summary": "Neural-network and kernel potentials fitted to DFT energies and forces reach near-DFT accuracy at the cost of classical force fields, enabling million-atom, nanosecond simulations of phase transitions, defects and hydrides.", "map": "E=\\sum_iE_i(\\mathbf G_i),\\ \\mathcal L=\\sum(E-E_{\\text{DFT}})^2+w\\sum|\\mathbf F-\\mathbf F_{\\text{DFT}}|^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0323", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "08-condensed-matter/soft-matter/glasses-and-jamming", "name": "Machine-learned structure predicts glassy dynamics", "kind": "method transfer", "summary": "A machine-learned structural order parameter ('softness') trained on local particle environments predicts which particles in a supercooled liquid will rearrange, connecting hidden structure to dynamical heterogeneity.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0324", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "Neural-network quantum states", "kind": "method transfer", "summary": "Neural networks used as variational wavefunctions (restricted Boltzmann machines, then transformers) are optimized by variational Monte Carlo and now compete with DMRG and QMC on frustrated magnets and the doped Hubbard model.", "map": "\\psi_\\theta(\\mathbf s)=\\sum_{\\mathbf h}e^{\\sum_ia_is_i+\\sum_jb_jh_j+\\sum_{ij}W_{ij}h_js_i},\\ E(\\theta)=\\frac{\\langle\\psi_\\theta|H|\\psi_\\theta\\rangle}{\\langle\\psi_\\theta|\\psi_\\theta\\rangle}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0325", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "08-condensed-matter/crystals-and-electronic-structure/density-functional-theory", "name": "Ab initio molecular dynamics", "kind": "method transfer", "summary": "Car-Parrinello and Born-Oppenheimer molecular dynamics integrate nuclear motion on DFT forces computed on the fly, unifying electronic structure with MD for liquids, melting and high-pressure phases.", "map": "M_I\\ddot{\\mathbf R}_I=-\\nabla_{\\mathbf R_I}E_{KS}[\\{\\phi_i\\},\\{\\mathbf R\\}];\\ \\mu\\ddot\\phi_i=-\\frac{\\delta E}{\\delta\\phi_i^*}+\\sum_j\\Lambda_{ij}\\phi_j\\ (\\text{CP})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0326", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "08-condensed-matter/soft-matter/glasses-and-jamming", "name": "Molecular dynamics of supercooled liquids and jamming", "kind": "method transfer", "summary": "Simulations of Lennard-Jones and soft-sphere mixtures supply dynamical heterogeneity, the Kauzmann and mode-coupling tests and jamming criticality, but are limited to ~microsecond times, about 10^-6 of the laboratory glass-transition timescale.", "map": "V_{LJ}=4\\epsilon[(\\sigma/r)^{12}-(\\sigma/r)^6];\\ \\tau_\\alpha\\sim10^{-12}\\to10^{2}\\,\\text{s at }T_g", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0327", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "08-condensed-matter/soft-matter/polymers", "name": "Bead-spring simulations of entangled polymers", "kind": "method transfer", "summary": "The Kremer-Grest bead-spring model showed by MD the crossover from Rouse to reptation dynamics in entangled melts and remains the standard coarse-grained test bed for polymer rheology.", "map": "U_{\\text{FENE}}=-\\tfrac12kR_0^2\\ln[1-(r/R_0)^2]+U_{\\text{WCA}};\\ g_1(t)\\sim t^{1/4}\\ (\\text{reptation regime})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0328", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "name": "Cluster Monte Carlo for magnetic spin models", "kind": "method transfer", "summary": "Critical slowing down in Metropolis simulations of Ising and Heisenberg magnets was beaten by Swendsen-Wang and Wolff cluster updates built on the Fortuin-Kasteleyn mapping; loop and worm algorithms extend this to quantum magnets.", "map": "p_{\\text{bond}}=1-e^{-2\\beta J};\\ \\tau\\sim\\xi^z,\\ z_{\\text{Metropolis}}\\approx2.17\\to z_{SW}\\approx0.25\\ (2D\\ \\text{Ising})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0329", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "Quantum Monte Carlo and the fermion sign problem", "kind": "method transfer", "summary": "Determinant, auxiliary-field and diagrammatic QMC map correlated electrons onto Monte Carlo sampling in imaginary time; for doped fermions and frustrated magnets the weights turn negative and the sign problem makes cost exponential.", "map": "\\langle O\\rangle=\\frac{\\sum_cO_c|w_c|\\,\\mathrm{sgn}\\,w_c}{\\sum_c|w_c|\\,\\mathrm{sgn}\\,w_c},\\ \\langle\\mathrm{sgn}\\rangle\\sim e^{-\\beta N\\Delta f}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0330", "a": "00-foundations/computational-physics/tensor-network-methods", "b": "08-condensed-matter/strongly-correlated-electrons", "name": "Entanglement structure of correlated ground states", "kind": "method transfer", "summary": "Area-law entanglement in gapped correlated phases is what makes tensor-network compression possible; deviations (log corrections at criticality, topological entanglement entropy) diagnose the phase.", "map": "S_A=\\alpha L-\\gamma+\\ldots\\ (2D\\ \\text{gapped}),\\ S_A=\\frac c3\\ln\\ell\\ (1D\\ \\text{critical})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0331", "a": "00-foundations/computational-physics/tensor-network-methods", "b": "08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order", "name": "Topological order as an entanglement pattern", "kind": "method transfer", "summary": "Topological order shows up as a constant negative correction to area-law entanglement, the topological entanglement entropy gamma=ln D, and string-net and toric-code ground states are exact PEPS with virtual symmetries; tensor networks thereby identify topological phases numerically.", "map": "S_A=\\alpha L-\\gamma,\\ \\gamma=\\ln\\mathcal D,\\ \\mathcal D=\\sqrt{\\textstyle\\sum_ad_a^2}\\ (\\text{toric code: }\\ln2)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0332", "a": "00-foundations/computational-physics/tensor-network-methods", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "DMRG and tensor networks for correlated electrons", "kind": "method transfer", "summary": "DMRG, invented for quantum spin chains, is a variational method over matrix product states; PEPS, MERA and their 2D cylinder implementations now give benchmark ground states of Hubbard and frustrated spin models, limited by area-law entanglement growth.", "map": "|\\psi\\rangle=\\sum\\mathrm{Tr}(A^{s_1}\\cdots A^{s_N})|s_1\\ldots s_N\\rangle,\\ S\\le\\log\\chi", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0333", "a": "00-foundations/computational-physics/tensor-network-methods", "b": "08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals", "name": "MERA and entanglement at quantum critical points", "kind": "method transfer", "summary": "Critical ground states violate the area law logarithmically; the multiscale entanglement renormalization ansatz (MERA) captures this with a scale-invariant tensor network that implements real-space RG and resembles a discretized AdS geometry.", "map": "S(\\ell)=\\frac c3\\ln\\frac\\ell a\\ (\\text{1+1D CFT});\\ \\text{MERA layers}\\leftrightarrow\\text{RG scale}\\leftrightarrow\\text{radial AdS coordinate}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0334", "a": "00-foundations/history-and-philosophy-of-physics/philosophy-of-physics", "b": "08-condensed-matter/strongly-correlated-electrons", "name": "Emergence and the limits of reductionism", "kind": "historical", "summary": "Anderson's 'More is different' and Laughlin and Pines' 'Theory of Everything' used broken symmetry, quasiparticles and protected quantization in correlated matter as the central examples in the philosophical debate over emergence and reduction.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0335", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "Kramers-Kronig relations for lattice and optical response", "kind": "identity", "summary": "Causality makes the dielectric and phonon response functions analytic in the upper half-plane, so absorption and dispersion are Hilbert transforms of each other; this links the TO-phonon resonance, reflectivity and the Lyddane-Sachs-Teller relation.", "map": "\\mathrm{Re}\\,\\epsilon(\\omega)-1=\\frac2\\pi\\mathcal P\\int_0^\\infty\\frac{\\omega'\\mathrm{Im}\\,\\epsilon(\\omega')}{\\omega'^2-\\omega^2}d\\omega';\\ \\frac{\\omega_{LO}^2}{\\omega_{TO}^2}=\\frac{\\epsilon(0)}{\\epsilon(\\infty)}", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C0336", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons", "name": "Bloch theorem as Floquet theory of periodic ODEs", "kind": "identity", "summary": "Bloch's theorem is Floquet's 1883 theorem for linear differential equations with periodic coefficients; bands and gaps of the Kronig-Penney and nearly-free-electron models are the stability and instability zones of Hill's and Mathieu's equations.", "map": "\\psi''+[E-V(x)]\\psi=0,\\ V(x+a)=V(x)\\Rightarrow\\psi(x+a)=e^{ika}\\psi(x);\\ |\\tfrac12\\mathrm{Tr}\\,M(E)|\\le1\\Leftrightarrow\\text{band}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0337", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "Many-body Green's functions and DMFT", "kind": "method transfer", "summary": "Correlated-electron theory is built on Matsubara Green's functions and self-energies; DMFT maps the lattice problem onto an impurity whose local Green's function is fixed self-consistently, an operational use of Dyson's equation.", "map": "G^{-1}=G_0^{-1}-\\Sigma;\\ G_{\\text{loc}}(i\\omega_n)=\\sum_{\\mathbf k}[i\\omega_n+\\mu-\\epsilon_{\\mathbf k}-\\Sigma(i\\omega_n)]^{-1}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0338", "a": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "b": "08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons", "name": "Bloch bands as an eigenvalue problem", "kind": "method transfer", "summary": "Band structure is the spectral decomposition of a lattice-translation-invariant Hamiltonian: Bloch's theorem block-diagonalizes it by crystal momentum, leaving finite Hermitian matrices H(k) to diagonalize.", "map": "[H,T_{\\mathbf R}]=0\\Rightarrow H=\\bigoplus_{\\mathbf k}H(\\mathbf k),\\ H(\\mathbf k)u_{n\\mathbf k}=E_n(\\mathbf k)u_{n\\mathbf k}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0339", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "Berry curvature as the curvature of a bundle", "kind": "identity", "summary": "Berry connection and curvature are a U(1) connection and its curvature on the bundle of Bloch states over the Brillouin-zone torus; the Chern number is the first Chern class and the quantum geometric tensor combines a metric with this curvature.", "map": "\\mathcal A=i\\langle u|du\\rangle,\\ \\Omega=d\\mathcal A,\\ C=\\frac1{2\\pi}\\int_{T^2}\\Omega\\in\\mathbb Z;\\ Q_{\\mu\\nu}=g_{\\mu\\nu}-\\tfrac i2\\Omega_{\\mu\\nu}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0340", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "name": "Shot noise and Johnson noise in conductors", "kind": "identity", "summary": "The Johnson-Nyquist and Schottky formulas of instrumentation are limits of mesoscopic noise theory: shot noise reduced by the Fano factor sum T(1-T)/sum T, and measuring it revealed the e/3 charge of fractional quantum Hall quasiparticles.", "map": "S_I=2qIF,\\ F=\\frac{\\sum_nT_n(1-T_n)}{\\sum_nT_n};\\ S_I=4k_BTG\\ (V=0)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0341", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Superconducting cryogenic sensors", "kind": "method transfer", "summary": "Transition-edge sensors, kinetic-inductance detectors and superconducting nanowire single-photon detectors turn the superconducting transition and the small gap into energy-resolving, photon-counting sensors for X-ray, optical and millimetre-wave astronomy and quantum optics.", "map": "\\Delta E_{\\text{FWHM}}\\approx2.355\\sqrt{4k_BT^2C/\\alpha}\\ (\\text{TES})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0342", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "SQUIDs as instrumentation", "kind": "method transfer", "summary": "SQUIDs are the most sensitive magnetic-flux detectors and the readout amplifiers of cryogenic sensor arrays; their noise is set by Josephson-junction physics and can approach the quantum limit.", "map": "S_\\Phi^{1/2}\\sim10^{-6}\\Phi_0/\\sqrt{\\text{Hz}},\\ \\Phi_0=h/2e", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0343", "a": "00-foundations/symmetry-and-group-theory", "b": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "name": "Space groups and representations in crystals", "kind": "method transfer", "summary": "The 230 space groups and their irreducible representations label Bloch bands, phonon branches and selection rules, explain systematic absences in diffraction, and the crystallographic restriction (no 5-fold axes) made quasicrystals a surprise.", "map": "\\{R|\\mathbf t\\}\\psi_{n\\mathbf k}=\\psi_{n,R\\mathbf k};\\ \\text{little group }G_{\\mathbf k}\\ \\text{irreps label bands};\\ 2\\cos(2\\pi/n)\\in\\mathbb Z", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0344", "a": "00-foundations/symmetry-and-group-theory", "b": "08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order", "name": "Topological order as broken higher-form symmetry", "kind": "method transfer", "summary": "Generalized (higher-form) global symmetries act on line and surface operators; deconfined topological phases such as the toric code spontaneously break a 1-form symmetry, extending the symmetry-breaking classification of phases to topological order and its mixed-state versions.", "map": "U_g(\\Sigma^{d-p-1})W(C^p)=e^{i\\alpha\\,\\mathrm{Link}(\\Sigma,C)}W(C^p);\\ \\langle W(C)\\rangle\\sim\\text{perimeter law}\\Rightarrow\\text{broken 1-form}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0345", "a": "00-foundations/symmetry-and-group-theory", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "Topological quantum chemistry via band representations", "kind": "method transfer", "summary": "Induced (band) representations of space groups decide whether a set of bands can come from localized symmetric Wannier orbitals; when they cannot, the bands are topological, which turned representation theory into a high-throughput topology classifier.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0346", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "08-condensed-matter/magnetism/altermagnetism", "name": "Altermagnets break time reversal without magnetization", "kind": "mechanism", "summary": "Altermagnets lift Kramers spin degeneracy by breaking the combined time-reversal-plus-translation symmetry of ordinary antiferromagnets while keeping zero net moment, so T-odd responses (anomalous Hall, spin splitting) appear without stray fields.", "map": "\\Theta t_{1/2}\\ \\text{(AFM, preserved)}\\to\\text{broken};\\ [C_2\\|R]\\ \\text{keeps }\\sum_{\\mathbf k}(E_\\uparrow-E_\\downarrow)=0", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0347", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "The tenfold way from T, C and chiral symmetry", "kind": "identity", "summary": "Gapped free-fermion phases fall into ten Altland-Zirnbauer classes set by whether time reversal T, particle-hole C and chiral S symmetries are present and square to +1 or -1; with dimension this gives the periodic table of topological insulators and superconductors.", "map": "T^2,C^2\\in\\{0,\\pm1\\},\\ S=TC\\Rightarrow10\\ \\text{classes};\\ \\text{e.g. AII }(T^2=-1):\\ \\mathbb Z_2\\ (d=2,3)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0348", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "08-condensed-matter/topological-matter/topological-insulators", "name": "Kramers pairs protect topological insulators", "kind": "mechanism", "summary": "The antiunitary time-reversal operator with Theta^2=-1 forces Kramers degeneracy at time-reversal-invariant momenta, giving the Z2 invariant and protecting the surface Dirac cone against non-magnetic backscattering.", "map": "\\Theta=i\\sigma_yK,\\ \\Theta^2=-1\\Rightarrow\\langle\\psi|\\Theta\\psi\\rangle=0;\\ \\nu\\in\\mathbb Z_2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0349", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "08-condensed-matter/magnetism/altermagnetism", "name": "Spin-group symmetry classification of altermagnets", "kind": "method transfer", "summary": "Altermagnets are defined by spin-group symmetry, in which spin and lattice operations act independently when spin-orbit coupling is negligible; opposite-spin sublattices related by a rotation rather than a translation or inversion give d-, g- or i-wave spin splitting.", "map": "[C_2\\|C_{4z}]\\ \\text{(spin flip }\\otimes\\text{ lattice rotation)}\\Rightarrow E_\\uparrow(\\mathbf k)-E_\\downarrow(\\mathbf k)\\propto k_xk_y", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0350", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "08-condensed-matter/topological-matter/topological-semimetals", "name": "Chiral anomaly breaks a Noether current in Weyl semimetals", "kind": "identity", "summary": "The axial charge of Weyl fermions is conserved classically by Noether's theorem but not quantum mechanically: parallel E and B pump electrons between Weyl nodes of opposite chirality at the Adler-Bell-Jackiw rate, seen as negative longitudinal magnetoresistance.", "map": "\\partial_\\mu j^\\mu_5=\\frac{e^2}{2\\pi^2\\hbar^2c}\\mathbf E\\cdot\\mathbf B\\leftrightarrow\\frac{dN_\\pm}{dt}=\\pm\\frac{e^2}{h^2}\\mathbf E\\cdot\\mathbf B", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0351", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "name": "Magnons as Goldstone bosons and their counting", "kind": "identity", "summary": "Magnons are the Goldstone modes of broken spin-rotation symmetry: antiferromagnets have two linearly dispersing type-A modes, while ferromagnets have one quadratic type-B mode because the broken generators have a non-zero commutator expectation; Mermin-Wagner forbids such order in 2D at T>0.", "map": "n_{NG}=n_{BG}-\\tfrac12\\mathrm{rank}\\,\\rho,\\ \\rho_{ab}=\\lim\\frac{-i}{V}\\langle[Q_a,j_b^0]\\rangle;\\ \\omega\\propto k^2\\ (\\text{FM}),\\ \\omega\\propto k\\ (\\text{AFM})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0352", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids", "name": "Spin liquids: order without symmetry breaking", "kind": "mechanism", "summary": "Quantum spin liquids are the main counterexample to the Landau paradigm: frustration prevents spontaneous symmetry breaking down to T=0, and the low-energy theory instead has emergent gauge fields and fractionalized spinons, so the phase is classified by topology rather than an order parameter.", "map": "f=|\\theta_{CW}|/T_N\\gg1;\\ \\text{no local }\\langle\\mathbf S_i\\rangle\\neq0,\\ \\text{emergent }\\mathbb Z_2\\text{ or U(1) gauge field}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0353", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "08-condensed-matter/soft-matter/liquid-crystals", "name": "Nematic order, Goldstone modes and homotopy of defects", "kind": "identity", "summary": "A nematic breaks rotational symmetry with order-parameter space RP^2; its director fluctuations are Goldstone modes and its defects are classified by homotopy groups, pi_1(RP^2)=Z_2 allowing half-integer disclinations, which is the general topological theory of defects in ordered media.", "map": "\\mathcal M=SO(3)/D_\\infty=\\mathbb{RP}^2,\\ \\pi_1=\\mathbb Z_2,\\ \\pi_2=\\mathbb Z;\\ Q_{ij}=S(n_in_j-\\tfrac13\\delta_{ij})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0354", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "08-condensed-matter/superconductivity", "name": "Superconductivity as broken U(1) gauge symmetry", "kind": "identity", "summary": "A superconductor is the condensed-matter Higgs phase: a charged condensate with a phase that breaks U(1), whose would-be Goldstone mode is eaten by the photon, giving the Meissner effect and flux quantization.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0355", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Ginzburg-Landau theory is the abelian Higgs model", "kind": "identity", "summary": "The Ginzburg-Landau free energy of a superconductor is, term by term, the static abelian Higgs Lagrangian; the coherence length and penetration depth are the inverse Higgs and photon masses, and kappa=lambda/xi separates type I from type II exactly where Nielsen-Olesen strings attract or repel.", "map": "F=\\int\\left[\\frac{|(\\nabla-2ie\\mathbf A/\\hbar)\\psi|^2}{2m^*}+a|\\psi|^2+\\tfrac b2|\\psi|^4+\\frac{B^2}{2\\mu_0}\\right];\\ \\xi^{-1}\\leftrightarrow m_H,\\ \\lambda^{-1}\\leftrightarrow m_\\gamma", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0356", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "08-condensed-matter/soft-matter/polymers", "name": "Scaling arguments in polymer physics", "kind": "method transfer", "summary": "Flory's free-energy balance and de Gennes' blob scaling derive polymer size, osmotic pressure and dynamics from dimensional analysis plus a single exponent, a showcase of scaling reasoning without solving the full model.", "map": "F\\sim\\frac{R^2}{Nb^2}+\\frac{vN^2}{R^d}\\Rightarrow R\\sim N^{3/(d+2)};\\ \\Pi\\sim\\frac{k_BT}{\\xi^3},\\ \\xi\\sim b(cb^3)^{-\\nu/(3\\nu-1)}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0357", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals", "name": "Planckian time from dimensional analysis", "kind": "method transfer", "summary": "At a quantum critical point the only energy scale is temperature, so dimensional analysis gives a relaxation time hbar/k_BT; strange metals saturate this Planckian bound, with measured scattering rates hbar/tau~alpha k_BT and alpha~1.", "map": "\\tau_P=\\frac{\\hbar}{k_BT}\\approx2.5\\times10^{-14}\\,\\text{s}\\ (300\\,\\text{K}),\\ \\rho=\\frac{m^*}{ne^2}\\frac{\\alpha k_BT}{\\hbar}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0358", "a": "00-foundations/units-and-constants/fundamental-constants", "b": "08-condensed-matter/topological-matter/quantum-hall-effects", "name": "Quantum Hall effect measures the fine-structure constant", "kind": "identity", "summary": "von Klitzing introduced the quantized Hall resistance as a determination of alpha, since R_K=h/e^2=mu_0 c/(2 alpha); QHE data entered CODATA adjustments of alpha before the 2019 SI made R_K exact.", "map": "R_K=\\frac{h}{e^2}=\\frac{\\mu_0c}{2\\alpha}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0359", "a": "00-foundations/units-and-constants/si-units-and-2019-redefinition", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "name": "Graphene quantum Hall resistance standards", "kind": "method transfer", "summary": "Epitaxial graphene on SiC shows wide, robust nu=2 plateaus at higher temperature and lower field than GaAs, allowing table-top quantum resistance standards with part-per-billion accuracy.", "map": "E_1-E_0=v_F\\sqrt{2e\\hbar B}\\approx36\\,\\text{meV}\\sqrt{B[\\text{T}]}\\gg\\hbar\\omega_c^{\\text{GaAs}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0360", "a": "00-foundations/units-and-constants/si-units-and-2019-redefinition", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures", "name": "Single-electron pumps and the quantum ampere", "kind": "method transfer", "summary": "Coulomb-blockaded quantum dots and metallic islands clocked at frequency f transfer exactly one electron per cycle, realizing I=ef directly from the fixed elementary charge and closing the quantum metrology triangle with Josephson and quantum Hall standards.", "map": "I=nef;\\ V=\\frac{f_J}{K_J},\\ R=R_K\\Rightarrow\\ R_KK_Je=2\\ (\\text{triangle})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0361", "a": "00-foundations/units-and-constants/si-units-and-2019-redefinition", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "Josephson voltage standard and the 2019 SI", "kind": "identity", "summary": "The AC Josephson effect fixes voltage to frequency through K_J=2e/h exactly; with e and h fixed in the 2019 SI, Josephson arrays realize the volt and, with the Kibble balance, the kilogram.", "map": "V_n=n\\frac{f}{K_J},\\ K_J=\\frac{2e}{h}=483\\,597.848\\ldots\\,\\text{GHz/V}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0362", "a": "00-foundations/units-and-constants/si-units-and-2019-redefinition", "b": "08-condensed-matter/topological-matter/quantum-hall-effects", "name": "Quantum Hall resistance standard", "kind": "identity", "summary": "Hall plateaus at R_xy=h/(nu e^2) independent of material and geometry realize the ohm via the von Klitzing constant R_K=h/e^2, exact in the 2019 SI.", "map": "R_K=\\frac{h}{e^2}=25\\,812.807\\ldots\\,\\Omega", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0745", "a": "01-classical-mechanics/analytical-mechanics/canonical-transformations-and-hamilton-jacobi", "b": "08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons", "name": "Onsager quantization of cyclotron orbits", "kind": "identity", "summary": "Quantum oscillations follow from Bohr-Sommerfeld quantization of semiclassical cyclotron orbits on the Fermi surface: the action variable of the orbit fixes allowed k-space areas, so dHvA and SdH frequencies measure extremal Fermi-surface cross sections.", "map": "J=\\oint p\\,dq=2\\pi\\hbar(n+\\gamma)\\Rightarrow A_k=\\frac{2\\pi eB}{\\hbar}(n+\\gamma),\\ \\Delta(1/B)=\\frac{2\\pi e}{\\hbar A_F}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0746", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "Berry curvature deforms semiclassical phase space", "kind": "identity", "summary": "Semiclassical Bloch electrons with Berry curvature obey non-canonical Hamiltonian dynamics: the anomalous velocity appears and Liouville's phase-space volume is not conserved unless weighted by (1+e B.Omega/hbar), which corrects the density of states.", "map": "\\dot{\\mathbf r}=\\frac1\\hbar\\nabla_{\\mathbf k}E-\\dot{\\mathbf k}\\times\\boldsymbol\\Omega,\\ \\hbar\\dot{\\mathbf k}=-e(\\mathbf E+\\dot{\\mathbf r}\\times\\mathbf B);\\ D=1+\\frac e\\hbar\\mathbf B\\cdot\\boldsymbol\\Omega", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0747", "a": "01-classical-mechanics/continuum-and-fluid-mechanics", "b": "08-condensed-matter/soft-matter", "name": "Continuum mechanics of soft materials", "kind": "method transfer", "summary": "Soft matter is described at long wavelengths by continuum theories (viscoelastic fluids, gels, nematic hydrodynamics, granular rheology) built on the conservation laws and constitutive-relation framework of continuum mechanics.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0748", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "name": "Dislocations as topological defects of elastic crystals", "kind": "mechanism", "summary": "Plastic deformation of crystals proceeds by motion of dislocations, line defects labelled by a Burgers vector, whose long-range stress fields are solutions of continuum elasticity; their unbinding drives KTHNY two-dimensional melting.", "map": "\\oint d\\mathbf u=\\mathbf b;\\ \\sigma_{\\text{screw}}=\\frac{\\mu b}{2\\pi r};\\ \\tau_{\\text{Peierls}}\\ll\\mu/30\\ (\\text{ideal strength})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0749", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "Elastic waves as long-wavelength acoustic phonons", "kind": "identity", "summary": "Acoustic phonon branches at small k are the elastic waves of continuum elasticity: their slopes are the longitudinal and transverse sound speeds fixed by elastic constants, which phonon dispersion measurements determine.", "map": "\\omega=v_{L,T}k\\ (k\\to0),\\ v_L=\\sqrt{(\\lambda+2\\mu)/\\rho},\\ v_T=\\sqrt{\\mu/\\rho};\\ \\rho\\omega^2u_i=C_{ijkl}k_jk_lu_k", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0750", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "08-condensed-matter/soft-matter/colloids-and-granular-matter", "name": "Contact mechanics, force chains and the Janssen effect", "kind": "mechanism", "summary": "Static granular packs transmit stress through heterogeneous force chains between Hertzian contacts; frictional wall support saturates pressure with depth in silos (Janssen effect), so granular stress cannot be treated as hydrostatic.", "map": "F=\\tfrac43E^*\\sqrt{R^*}\\delta^{3/2}\\ (\\text{Hertz});\\ p(z)=p_\\infty(1-e^{-z/\\lambda}),\\ \\lambda=\\frac{R}{2\\mu_wK}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0751", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "08-condensed-matter/soft-matter/glasses-and-jamming", "name": "Maxwell counting and isostatic jamming", "kind": "historical", "summary": "Maxwell's 1864 constraint counting for the rigidity of frames gives the isostatic contact number z=2d at the jamming transition; above jamming, shear modulus and excess contacts grow as power laws of compression.", "map": "N_{\\text{zero}}=dN-\\tfrac12zN\\Rightarrow z_c=2d;\\ G\\sim(\\phi-\\phi_J)^{1/2},\\ z-z_c\\sim(\\phi-\\phi_J)^{1/2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0752", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "08-condensed-matter/soft-matter/liquid-crystals", "name": "Frank orientational elasticity and liquid-crystal elastomers", "kind": "analogy", "summary": "Frank theory is an elasticity for the director field (splay, twist, bend) instead of displacements; coupling it to a rubber network gives liquid-crystal elastomers with 'soft elasticity' and large reversible actuation.", "map": "F_{\\text{Frank}}=\\tfrac12K_1(\\nabla\\cdot\\mathbf n)^2+\\tfrac12K_2(\\mathbf n\\cdot\\nabla\\times\\mathbf n)^2+\\tfrac12K_3|\\mathbf n\\times\\nabla\\times\\mathbf n|^2\\leftrightarrow\\tfrac12C_{ijkl}\\epsilon_{ij}\\epsilon_{kl}", "breaks": "The director is a unit headless vector, so Frank elasticity has topological defects and no restoring force for uniform rotations; a fluid nematic has zero shear modulus, unlike a solid.", "confidence": "established", "strength": 2}
{"id": "C0753", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "08-condensed-matter/soft-matter/polymers", "name": "Rubber elasticity: entropic springs to neo-Hookean solids", "kind": "identity", "summary": "Each network strand is an entropic Gaussian spring, so averaging over strands gives the neo-Hookean strain-energy function of finite-strain continuum elasticity with shear modulus n k_B T, explaining why rubber stiffens on heating.", "map": "f=\\frac{3k_BT}{Nb^2}R\\Rightarrow W=\\tfrac12nk_BT(\\lambda_1^2+\\lambda_2^2+\\lambda_3^2-3),\\ G=nk_BT", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0754", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "Topological mechanics of isostatic lattices", "kind": "method transfer", "summary": "Band topology applied to the compatibility matrix of Maxwell (isostatic) lattices predicts floppy zero modes localized on particular edges, an index theorem for mechanical metamaterials analogous to the SSH chain.", "map": "N_0-N_S=dN-N_B;\\ \\text{topological polarization }\\mathbf R_T=\\sum_i n_i\\mathbf a_i\\ (\\text{winding of }\\det C(\\mathbf k))", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0755", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "name": "Electron hydrodynamics in graphene", "kind": "mechanism", "summary": "When electron-electron collisions dominate over impurity and phonon scattering, electrons in clean graphene flow as a viscous fluid obeying Navier-Stokes-like equations, producing negative nonlocal resistance from backflow whirlpools and Poiseuille profiles.", "map": "\\eta\\nabla^2\\mathbf u-\\frac{m}{\\tau}\\mathbf u=\\nabla p+ne\\mathbf E;\\ \\ell_{ee}\\ll W\\ll\\ell_{mr},\\ \\nu=v_F\\ell_{ee}/4", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0756", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "08-condensed-matter/soft-matter/colloids-and-granular-matter", "name": "mu(I) rheology: granular matter as a viscoplastic fluid", "kind": "method transfer", "summary": "Dense granular flows obey a local friction law in which the effective friction depends on the inertial number; inserted into continuum momentum equations it predicts flows on inclines, in silos and in rotating drums.", "map": "\\tau=\\mu(I)P,\\ \\mu(I)=\\mu_s+\\frac{\\mu_2-\\mu_s}{1+I_0/I},\\ I=\\frac{\\dot\\gamma d}{\\sqrt{P/\\rho_s}}\\Rightarrow\\eta_{\\text{eff}}=\\frac{\\mu(I)P}{\\dot\\gamma}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0757", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "08-condensed-matter/soft-matter/liquid-crystals", "name": "Nematodynamics: anisotropic viscous flow", "kind": "mechanism", "summary": "Ericksen-Leslie theory couples the Navier-Stokes equations to director rotation, giving three Miesowicz viscosities, flow alignment and backflow; it controls display switching times and active-nematic hydrodynamics.", "map": "\\sigma_{ij}=-p\\delta_{ij}+\\alpha_1n_in_jn_kn_lA_{kl}+\\alpha_2n_iN_j+\\ldots+\\alpha_4A_{ij}+\\ldots;\\ \\gamma_1\\dot{\\mathbf n}=\\mathbf h-\\gamma_2\\mathsf A\\mathbf n", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0758", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "08-condensed-matter/soft-matter/liquid-crystals", "name": "Electroconvection in nematics", "kind": "mechanism", "summary": "Above a threshold voltage nematic layers develop convection rolls (Williams domains) through the Carr-Helfrich mechanism, an anisotropic analogue of Rayleigh-Benard convection and a classic system for pattern formation and spatiotemporal chaos.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0759", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics", "b": "08-condensed-matter/soft-matter", "name": "Colloids, polymers and swimmers in Stokes flow", "kind": "mechanism", "summary": "Soft-matter dynamics is overdamped: colloid diffusion, polymer Rouse-Zimm dynamics and microswimming are governed by Stokes drag and long-range hydrodynamic interactions (Oseen tensor).", "map": "\\mathbf F=6\\pi\\mu a\\mathbf U,\\ \\mathsf O(\\mathbf r)=\\frac{1}{8\\pi\\mu r}(\\mathbb 1+\\hat{\\mathbf r}\\hat{\\mathbf r})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0760", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics", "b": "08-condensed-matter/soft-matter/active-matter", "name": "Microswimmers at low Reynolds number", "kind": "mechanism", "summary": "Bacteria and synthetic swimmers live at Re~1e-5, where Purcell's scallop theorem forbids reciprocal strokes and Stokesian far fields (pusher/puller force dipoles) set their collective hydrodynamics and active stresses.", "map": "\\mu\\nabla^2\\mathbf u=\\nabla p,\\ \\mathbf u_{\\text{dipole}}\\propto\\frac{p}{8\\pi\\mu r^2}[3(\\hat{\\mathbf e}\\cdot\\hat{\\mathbf r})^2-1]\\hat{\\mathbf r}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0761", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics", "b": "08-condensed-matter/soft-matter/colloids-and-granular-matter", "name": "Stokes drag and diffusion of colloids", "kind": "identity", "summary": "Colloid diffusion follows from Stokes drag via the Einstein relation, and sedimentation, hydrodynamic interactions and lubrication forces between colloids are low-Reynolds-number flow problems.", "map": "D=\\frac{k_BT}{6\\pi\\eta a};\\ v_{\\text{sed}}=\\frac{2\\Delta\\rho ga^2}{9\\eta};\\ Pe=\\frac{va}{D}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0762", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "08-condensed-matter/soft-matter/active-matter", "name": "Active turbulence versus inertial turbulence", "kind": "analogy", "summary": "Dense bacterial suspensions and active nematics show chaotic mesoscale vortices with power-law energy spectra at Reynolds numbers far below 1, driven by active stress rather than inertia.", "map": "E(k)\\sim k^{-5/3}\\ (\\text{Kolmogorov, inertial})\\ \\text{vs}\\ E(k)\\ \\text{power laws set by active length }\\ell_a=\\sqrt{K/|\\zeta|}", "breaks": "Energy is injected at every scale by active stress and dissipated by viscosity, with no inertial cascade; the vortex size is set by an active length, and spectral exponents are not universal.", "confidence": "current research", "strength": 2}
{"id": "C0763", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "08-condensed-matter/soft-matter/polymers", "name": "Polymer drag reduction and elastic turbulence", "kind": "mechanism", "summary": "Dilute long polymers reduce turbulent drag by up to ~80% (Toms effect) by suppressing near-wall vortices, and in viscous flows polymer elasticity alone drives chaotic 'elastic turbulence' at Reynolds numbers far below 1.", "map": "Wi=\\lambda\\dot\\gamma\\gg1,\\ Re\\ll1\\Rightarrow\\text{elastic turbulence};\\ \\text{Virk asymptote }U^+=11.7\\ln y^+-17", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0764", "a": "01-classical-mechanics/newtonian-mechanics/conservation-laws", "b": "08-condensed-matter/soft-matter/colloids-and-granular-matter", "name": "Inelastic collisions and granular gases", "kind": "mechanism", "summary": "Grains collide with a restitution coefficient below 1, so a granular gas loses energy in every collision; the resulting homogeneous cooling (Haff's law) and clustering instability follow from momentum conservation with kinetic-energy loss.", "map": "v_n'=-e\\,v_n,\\ \\Delta E=-\\tfrac14m(1-e^2)v_n^2;\\ T(t)=\\frac{T_0}{(1+t/\\tau_0)^2}\\ (\\text{Haff})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0765", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos", "b": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "name": "Chaotic billiards and mesoscopic conductance fluctuations", "kind": "mechanism", "summary": "Ballistic quantum dots whose classical shape gives chaotic trajectories show universal conductance fluctuations and weak-localization lineshapes governed by random-matrix theory, while regular (integrable) shapes do not; classical chaos thus controls quantum transport statistics.", "map": "\\mathrm{var}\\,G\\sim(e^2/h)^2,\\ \\delta G(B)\\ \\text{Lorentzian, width}\\propto\\sqrt{\\gamma_{\\text{esc}}}\\ (\\text{chaotic})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0766", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos", "b": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "name": "Frenkel-Kontorova model and the standard map", "kind": "identity", "summary": "Ground states of the Frenkel-Kontorova model of an incommensurate adsorbate or modulated crystal correspond to orbits of an area-preserving twist map; Aubry's pinning transition, where the incommensurate phase locks to the lattice, is the breakup of a KAM torus, and the devil's staircase of commensurate phases follows.", "map": "E=\\sum_n\\left[\\tfrac12(u_{n+1}-u_n-\\mu)^2+\\frac{K}{(2\\pi)^2}(1-\\cos2\\pi u_n)\\right]\\Rightarrow p_{n+1}=p_n+\\frac{K}{2\\pi}\\sin2\\pi u_n", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0767", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "FPUT anharmonic lattice and the discovery of solitons", "kind": "historical", "summary": "The 1955 Fermi-Pasta-Ulam-Tsingou simulation of an anharmonic atomic chain failed to thermalize its phonon modes; Zabusky and Kruskal's continuum limit, the KdV equation, explained the recurrence and introduced the soliton.", "map": "m\\ddot x_n=K(x_{n+1}-2x_n+x_{n-1})[1+\\alpha(x_{n+1}-x_{n-1})]\\to u_t+6uu_x+u_{xxx}=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0768", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "b": "08-condensed-matter/magnetism/magnetic-skyrmions-and-textures", "name": "Magnetic skyrmions as topological solitons", "kind": "identity", "summary": "Skyrmions are localized, particle-like solutions of the nonlinear micromagnetic field equations, stable because of an integer winding number, the topological-soliton class first introduced by Skyrme for nucleons.", "map": "N_{sk}=\\frac1{4\\pi}\\int\\mathbf m\\cdot(\\partial_x\\mathbf m\\times\\partial_y\\mathbf m)\\,d^2x\\in\\mathbb Z", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0769", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "Fluxons in long Josephson junctions are sine-Gordon solitons", "kind": "identity", "summary": "The phase difference along a long Josephson junction obeys the sine-Gordon equation; its kink solitons are fluxons carrying one flux quantum, which move relativistically at the Swihart velocity and underlie flux-flow oscillators.", "map": "\\lambda_J^2\\varphi_{xx}-\\omega_p^{-2}\\varphi_{tt}=\\sin\\varphi\\Rightarrow\\varphi=4\\arctan\\exp\\frac{x-vt}{\\lambda_J\\sqrt{1-v^2/\\bar c^2}}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0770", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "SSH domain-wall solitons and topological zero modes", "kind": "identity", "summary": "Domain walls between the two dimerization patterns of polyacetylene are solitons that bind a mid-gap zero mode with fractional charge or reversed spin-charge relation; the SSH chain is now the prototype 1D topological insulator (Jackiw-Rebbi index).", "map": "\\Delta(x)=\\Delta_0\\tanh(x/\\xi)\\Rightarrow\\text{zero mode }\\psi_0\\propto e^{-\\int|\\Delta|/\\hbar v_F};\\ \\nu=\\frac1{2\\pi}\\oint d\\arg h(k)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0771", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation", "b": "08-condensed-matter/soft-matter/active-matter", "name": "Flocking as synchronization in space", "kind": "analogy", "summary": "Alignment of headings in the Vicsek model is Kuramoto-like phase synchronization of self-propelled oscillators, with the twist that particles move and so couplings change; both show noise-driven order-disorder transitions.", "map": "\\dot\\theta_i=\\omega_i+\\frac KN\\sum_j\\sin(\\theta_j-\\theta_i)\\leftrightarrow\\theta_i(t+1)=\\langle\\theta_j\\rangle_{|r_{ij}|<R}+\\eta_i", "breaks": "Vicsek particles move, so the coupling network changes with the order itself, giving density bands and giant number fluctuations that have no counterpart in fixed-network Kuramoto models; their order parameter is a vector, not a phase.", "confidence": "established", "strength": 2}
{"id": "C0772", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "Synchronization of Josephson-junction arrays", "kind": "mechanism", "summary": "Series arrays of current-biased junctions coupled through a shared load map onto the Kuramoto model and phase-lock, the route to coherent microwave emission; Shapiro steps are Arnold-tongue frequency locking of a junction to an external drive.", "map": "\\langle V\\rangle=n\\frac{hf}{2e}\\ (\\text{Shapiro});\\ \\dot\\theta_i=\\omega_i+\\frac KN\\sum_j\\sin(\\theta_j-\\theta_i)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0773", "a": "01-classical-mechanics/oscillations-and-waves", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "Phonons as quantized normal modes", "kind": "identity", "summary": "Phonons are the quantized normal modes of the crystal's coupled harmonic oscillators; each mode contributes hbar*omega(n+1/2), giving Debye and Einstein heat capacities.", "map": "H=\\sum_{\\mathbf k,s}\\hbar\\omega_s(\\mathbf k)(a^\\dagger_{\\mathbf ks}a_{\\mathbf ks}+\\tfrac12)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0774", "a": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "b": "08-condensed-matter/crystals-and-electronic-structure", "name": "Normal-mode analysis behind lattice dynamics", "kind": "method transfer", "summary": "Translation symmetry turns the classical normal-mode problem of N coupled oscillators into Bloch-labelled branches, the same diagonalization used for electrons in periodic potentials.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0775", "a": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "Monatomic and diatomic chains to phonon branches", "kind": "identity", "summary": "The dispersion of a mass-spring chain is the phonon dispersion of a 1D crystal; a two-atom basis splits it into acoustic and optical branches with a gap at the zone boundary, and the dynamical matrix generalizes this to 3D.", "map": "\\omega(k)=2\\sqrt{K/m}\\,|\\sin(ka/2)|;\\ \\det[D(\\mathbf k)-\\omega^2\\mathbb 1]=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0776", "a": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "Mechanical topological insulators from coupled oscillators", "kind": "method transfer", "summary": "Arrays of coupled pendula or resonators engineered to mimic a quantum spin Hall Hamiltonian show helical edge modes, demonstrating that band topology is a property of linear wave equations, not of electrons.", "map": "\\ddot{\\mathbf x}=-D\\mathbf x,\\ D(\\mathbf k)\\simeq\\omega_0^2\\mathbb 1+H_{\\text{BHZ}}(\\mathbf k);\\ \\omega^2\\leftrightarrow E", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0777", "a": "01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators", "b": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "name": "Drude and Lorentz models as damped driven oscillators", "kind": "identity", "summary": "The optical conductivity of metals (free carriers) and insulators (bound oscillators, phonons, excitons) is the response of a driven damped harmonic oscillator, with resonance width set by scattering rate.", "map": "m\\ddot x+\\frac m\\tau\\dot x+m\\omega_0^2x=-eE_0e^{-i\\omega t}\\Rightarrow\\sigma(\\omega)=\\frac{ne^2\\tau/m}{1-i\\omega\\tau(1-\\omega_0^2/\\omega^2)}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0778", "a": "01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics", "b": "08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons", "name": "Phononic crystals: Bloch bands for sound", "kind": "identity", "summary": "Periodic elastic composites have acoustic band structures and complete band gaps computed with Bloch's theorem, the classical-wave analogue of electronic band theory that underlies acoustic metamaterials.", "map": "\\mathbf u(\\mathbf r+\\mathbf R)=e^{i\\mathbf k\\cdot\\mathbf R}\\mathbf u(\\mathbf r);\\ \\text{gap at }k=\\pi/a\\ \\text{when impedance contrast }Z_1\\neq Z_2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0779", "a": "01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "Josephson junction as a driven nonlinear pendulum", "kind": "identity", "summary": "In the RCSJ model the junction phase is a damped, driven pendulum, giving hysteresis, Shapiro steps and chaos; pumping its nonlinear inductance makes a Duffing-type parametric amplifier used for quantum-limited readout.", "map": "\\frac{\\hbar C}{2e}\\ddot\\varphi+\\frac{\\hbar}{2eR}\\dot\\varphi+I_c\\sin\\varphi=I\\leftrightarrow mL^2\\ddot\\theta+\\gamma\\dot\\theta+mgL\\sin\\theta=\\tau;\\ \\omega_p=\\sqrt{2eI_c/\\hbar C}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0780", "a": "01-classical-mechanics/rigid-body-dynamics/gyroscopes-and-precession", "b": "08-condensed-matter/magnetism/spintronics", "name": "Magnetization precession as gyroscopic motion", "kind": "identity", "summary": "The Landau-Lifshitz-Gilbert equation is the torque equation of a gyroscope for spin angular momentum: the magnetization precesses about the effective field and relaxes through Gilbert damping, while spin-transfer torque acts as an additional applied torque.", "map": "\\frac{d\\mathbf M}{dt}=-\\gamma\\mathbf M\\times\\mathbf H_{\\text{eff}}+\\frac\\alpha M\\mathbf M\\times\\frac{d\\mathbf M}{dt}\\leftrightarrow\\boldsymbol\\tau=\\boldsymbol\\Omega\\times\\mathbf L", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0781", "a": "01-classical-mechanics/rigid-body-dynamics/rotational-dynamics-and-inertia-tensor", "b": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "name": "Einstein-de Haas and Barnett effects", "kind": "mechanism", "summary": "Reversing a ferromagnet's magnetization makes the free body rotate (Einstein-de Haas), and rotating a body magnetizes it (Barnett), because total spin plus rigid-body angular momentum is conserved; these measured the electron g-factor and now enable ultrafast demagnetization studies.", "map": "\\Delta L_{\\text{body}}=-\\Delta S=-\\frac{2m_e}{ge}\\Delta M V;\\ \\mathbf M=\\chi\\frac{\\boldsymbol\\Omega}{\\gamma}\\ (\\text{Barnett})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1135", "a": "02-electromagnetism-and-optics/classical-optics/coherence-and-statistical-optics", "b": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "name": "Coherent backscattering, speckle and weak localization", "kind": "mechanism", "summary": "Time-reversed paths in a disordered medium interfere constructively. For light this gives the coherent-backscattering cone; for electrons it gives the weak-localization correction to the resistance. Universal conductance fluctuations are electronic speckle, a sample-specific fingerprint. Hanbury Brown–Twiss correlations reappear as electron antibunching and shot noise.", "map": "\\text{CBS cone}\\ \\Delta\\theta\\sim\\frac{\\lambda}{2\\pi\\ell}\\leftrightarrow\\delta\\sigma_{WL}\\propto-\\frac{e^2}{h}\\ln\\frac{L_\\phi}{\\ell},\\ \\delta G_{\\rm UCF}\\sim\\frac{e^2}{h}", "breaks": "Light has no Fermi statistics, and for it absorption and moving scatterers play the role of dephasing. 3D Anderson localization of light has not been convincingly shown, and claims for TiO2 powders are contested.", "confidence": "established", "strength": 3}
{"id": "C1136", "a": "02-electromagnetism-and-optics/classical-optics/fourier-optics-and-imaging", "b": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "name": "The phase problem: crystallography and phase retrieval", "kind": "method transfer", "summary": "A far-field diffraction pattern is the squared Fourier transform of the scattering density, so the phase is lost. Crystallography's Patterson and direct methods and optics' iterative phase retrieval (Gerchberg–Saxton, Fienup) attack the same problem. Combined with oversampling they gave coherent diffractive imaging at synchrotrons and XFELs, and Gabor invented holography for electron microscopy.", "map": "I(\\mathbf q)=|\\tilde\\rho(\\mathbf q)|^2\\Leftrightarrow P(\\mathbf r)=\\int\\rho(\\mathbf r')\\rho(\\mathbf r'+\\mathbf r)\\,d^3r'", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1137", "a": "02-electromagnetism-and-optics/classical-optics/geometric-optics", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "name": "Electron optics: Snell's law and Veselago lens at p–n junctions", "kind": "analogy", "summary": "Ballistic Dirac electrons crossing a graphene p–n junction refract according to Snell's law with an effective index ∝ ±k_F. On the hole side the index is negative, so a p–n junction acts as a Veselago lens (Cheianov–Fal'ko–Altshuler). Klein tunnelling sets the angle-dependent transmission, and focusing has been seen in hBN-encapsulated devices.", "map": "k_{F1}\\sin\\theta_1=k_{F2}\\sin\\theta_2,\\ n_{\\rm eff}\\propto\\pm\\sqrt{|n|}", "breaks": "λ_F is comparable to device features, so ray optics is only approximate. Smooth junctions collimate electrons toward normal incidence instead of imaging. Pseudospin conservation (Klein tunnelling) has no optical counterpart, and disorder and electron–electron scattering limit coherence.", "confidence": "current research", "strength": 2}
{"id": "C1138", "a": "02-electromagnetism-and-optics/classical-optics/interference-and-diffraction", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "SQUID double slit and Josephson Fraunhofer pattern", "kind": "identity", "summary": "A DC SQUID is a two-slit interferometer for the condensate, and the critical current of one wide junction in a field follows the single-slit Fraunhofer pattern. In general I_c(Φ) is the modulus of the Fourier transform of the critical-current density J_c(x), and Fourier-optics inversion (Dynes–Fulton) uses this to image supercurrent paths.", "map": "I_c^{\\rm SQUID}=2I_0|\\cos(\\pi\\Phi/\\Phi_0)|,\\ I_c^{\\rm JJ}=I_{c0}\\left|\\frac{\\sin(\\pi\\Phi/\\Phi_0)}{\\pi\\Phi/\\Phi_0}\\right|", "breaks": "The phase belongs to a macroscopic condensate, not to a light field, and the junction dynamics are nonlinear. The pattern is distorted by self-screening (β_L≳1) and by a Josephson length λ_J shorter than the junction. The measured quantity is a critical current, not an intensity.", "confidence": "established", "strength": 3}
{"id": "C1139", "a": "02-electromagnetism-and-optics/classical-optics/interference-and-diffraction", "b": "08-condensed-matter/topological-matter/quantum-hall-effects", "name": "Electron quantum optics with quantum Hall edge channels", "kind": "method transfer", "summary": "Chiral quantum Hall edge channels serve as lossless one-way beam paths and quantum point contacts as tunable beam splitters. Together they build electronic Mach–Zehnder and Fabry–Pérot interferometers, which show Aharonov–Bohm oscillations and electronic Hanbury Brown–Twiss and Hong–Ou–Mandel effects. Fabry–Pérot interferometry has also measured the braiding phase of ν=1/3 anyons.", "map": "\\phi_{AB}=2\\pi\\frac{\\Phi}{\\Phi_0^{(e)}},\\ \\Phi_0^{(e)}=\\frac{h}{e},\\ \\theta_{\\rm braid}(\\nu=1/3)=\\frac{2\\pi}{3}", "breaks": "Electrons are fermions, so they antibunch and obey Pauli exclusion. Coulomb charging effects dominate small Fabry–Pérot devices, and interactions between edge channels cause dephasing and energy relaxation, which limit visibility in a way photons do not.", "confidence": "current research", "strength": 2}
{"id": "C1140", "a": "02-electromagnetism-and-optics/classical-optics/polarization-and-crystal-optics", "b": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "name": "Neumann's principle: crystal system fixes optical class", "kind": "mechanism", "summary": "The dielectric tensor must be invariant under the crystal's point group. Cubic crystals are optically isotropic; tetragonal, trigonal and hexagonal ones are uniaxial; orthorhombic, monoclinic and triclinic ones are biaxial. Birefringence and the optic axes therefore act as structural probes, as in polarizing microscopy of minerals.", "map": "\\epsilon_{ij}=R_{ik}R_{jl}\\epsilon_{kl}\\ \\forall R\\in G:\\ \\text{cubic}\\to\\epsilon\\mathbb 1,\\ \\text{uniaxial}\\to(\\epsilon_o,\\epsilon_o,\\epsilon_e)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1141", "a": "02-electromagnetism-and-optics/classical-optics/polarization-and-crystal-optics", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/transition-metal-dichalcogenides-and-excitons", "name": "Valley-selective circular dichroism in TMD monolayers", "kind": "mechanism", "summary": "Broken inversion in MoS2- and WSe2-type monolayers gives opposite Berry curvature and orbital moment at the K and K' valleys. With C3 symmetry this makes σ+ light excite only K and σ− only K'. Helicity therefore writes and reads valley polarization (valleytronics) and reveals the valley Zeeman splitting.", "map": "\\eta(\\mathbf k)=\\frac{|P_+|^2-|P_-|^2}{|P_+|^2+|P_-|^2}\\approx\\pm1\\ \\text{at}\\ K,K'", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1142", "a": "02-electromagnetism-and-optics/classical-optics/polarization-and-crystal-optics", "b": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "name": "Magneto-optics: Faraday and Kerr rotation read M", "kind": "method transfer", "summary": "Magnetization makes the dielectric tensor gyrotropic, with an antisymmetric off-diagonal part proportional to M. The two circular polarizations then see different indices, rotating linear polarization in transmission (Faraday) and reflection (MOKE). Kerr microscopy images domains and skyrmions, and garnet ferrimagnets are used in optical isolators.", "map": "\\epsilon=\\begin{pmatrix}\\epsilon&ig\\\\-ig&\\epsilon\\end{pmatrix},\\ g\\propto M,\\ \\theta_F\\approx\\frac{\\pi gL}{n\\lambda}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1143", "a": "02-electromagnetism-and-optics/classical-optics/polarization-and-crystal-optics", "b": "08-condensed-matter/soft-matter/liquid-crystals", "name": "Nematics as field-switchable birefringent wave plates", "kind": "shared object", "summary": "A nematic is a uniaxial birefringent medium with its optic axis along the director. Jones-calculus retardation between crossed polarizers, switched by the field-driven Fréedericksz transition, is how every LCD works. Cholesterics add selective Bragg reflection of one circular polarization, and q-plates with a patterned director imprint Pancharatnam–Berry phases.", "map": "\\Gamma=\\frac{2\\pi\\Delta n\\,d}{\\lambda},\\ \\Delta n=n_e-n_o,\\ I=I_0\\sin^2 2\\theta\\,\\sin^2\\frac{\\Gamma}{2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1144", "a": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "b": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "name": "Quantized conductance as electron-waveguide mode counting", "kind": "analogy", "summary": "In the Landauer–Büttiker picture a point contact is an electron waveguide. Each transverse mode that rises above cutoff as the contact widens adds 2e²/h to the conductance, just as TE/TM modes open in a metal waveguide.", "map": "G=\\frac{2e^2}{h}\\sum_nT_n,\\ N=\\lfloor 2W/\\lambda_F\\rfloor\\leftrightarrow k_\\perp=n\\pi/W", "breaks": "Electrons are fermions filled up to E_F, so only modes at the Fermi energy carry current and the contact resistance h/(2e²N) is intrinsic. Spin degeneracy and interactions (the 0.7 anomaly) have no counterpart in a lossless EM waveguide.", "confidence": "established", "strength": 3}
{"id": "C1145", "a": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "name": "Graphene's universal πα absorption", "kind": "mechanism", "summary": "Interband transitions of massless Dirac electrons give a frequency-independent sheet conductivity e²/4ħ. Putting it into the Fresnel transmission of a conducting sheet shows that a suspended monolayer absorbs πα≈2.3% of visible light, so a transmission measurement reads off the fine-structure constant.", "map": "\\sigma_0=\\frac{e^2}{4\\hbar},\\ T=\\left(1+\\frac{\\sigma_0}{2\\epsilon_0c}\\right)^{-2}\\approx1-\\pi\\alpha", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1146", "a": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "Long Josephson junction as a superconducting stripline", "kind": "shared object", "summary": "A long Josephson junction is a parallel-plate transmission line that carries a slow Swihart mode. Its nonlinear phase obeys the sine-Gordon equation, whose kink solitons are fluxons each carrying one flux quantum. Superconducting coplanar resonators and junction-embedded transmission lines are the microwave hardware of circuit QED and traveling-wave parametric amplifiers.", "map": "\\lambda_J^2\\varphi_{xx}-\\omega_p^{-2}\\varphi_{tt}=\\sin\\varphi,\\ \\bar c=\\omega_p\\lambda_J\\ll c", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1147", "a": "02-electromagnetism-and-optics/electrodynamics/maxwells-equations", "b": "08-condensed-matter/topological-matter/topological-insulators", "name": "Axion electrodynamics in topological insulators", "kind": "mechanism", "summary": "A 3D topological insulator adds a θE·B term to the Maxwell Lagrangian, with θ=π fixed by time reversal. This gives a quantized magnetoelectric effect, image magnetic monopoles and a half-quantized surface Hall conductance once T is broken at the surface. THz Faraday and Kerr rotations quantized in units of α are the observable signature.", "map": "\\mathcal L_\\theta=\\frac{\\theta e^2}{2\\pi h}\\mathbf E\\cdot\\mathbf B,\\ \\theta=\\pi,\\ \\sigma_{xy}^{\\rm surf}=\\frac{e^2}{2h}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1148", "a": "02-electromagnetism-and-optics/electrodynamics/potentials-and-gauge-invariance", "b": "08-condensed-matter/magnetism/magnetic-skyrmions-and-textures", "name": "Emergent electromagnetism of skyrmions", "kind": "mechanism", "summary": "A conduction electron whose spin follows a magnetic texture picks up a Berry phase that acts as an emergent vector potential. Each skyrmion carries one emergent flux quantum h/e, which produces the topological Hall effect, and moving skyrmions induce an emergent electric field.", "map": "b_z=\\frac{\\hbar}{2e}\\,\\mathbf n\\cdot(\\partial_x\\mathbf n\\times\\partial_y\\mathbf n),\\ \\int b_z\\,d^2r=\\frac{h}{e}N_{sk}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1149", "a": "02-electromagnetism-and-optics/electrodynamics/potentials-and-gauge-invariance", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "London equation: the vector potential gives the photon a mass", "kind": "mechanism", "summary": "In a superconductor the supercurrent is proportional to the vector potential, which is gauge invariant only once the condensate phase gradient is included. Combined with Ampère's law this expels B over the London depth (the Meissner effect): a frequency-independent counterpart of the skin depth, and the condensed-matter case of the Anderson–Higgs mechanism.", "map": "\\mathbf J_s=-\\frac{n_se^2}{m}\\mathbf A,\\ \\nabla^2\\mathbf B=\\frac{\\mathbf B}{\\lambda_L^2},\\ \\lambda_L=\\sqrt{\\frac{m}{\\mu_0n_se^2}}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1150", "a": "02-electromagnetism-and-optics/electrodynamics/potentials-and-gauge-invariance", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "Gauge-invariant phase difference and flux quantization", "kind": "identity", "summary": "Josephson physics depends on the gauge-invariant phase difference, in which the line integral of the vector potential enters as an Aharonov–Bohm-type phase. Fluxoid quantization in units of h/2e follows, and so does the fact that SQUIDs read out the loop integral of A. The AC Josephson relation ties voltage to frequency, which is the basis of the voltage standard.", "map": "\\gamma=\\Delta\\phi-\\frac{2\\pi}{\\Phi_0}\\int\\mathbf A\\cdot d\\mathbf l,\\ \\Phi_0=\\frac{h}{2e},\\ f=\\frac{2eV}{h}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1151", "a": "02-electromagnetism-and-optics/electrodynamics/relativistic-electrodynamics", "b": "08-condensed-matter/topological-matter/topological-semimetals", "name": "Chiral anomaly driven by the invariant E·B", "kind": "mechanism", "summary": "Parallel E and B pump charge between Weyl nodes of opposite chirality at a rate set by the Lorentz invariant E·B (the dual-field invariant of covariant electrodynamics), through the chiral lowest Landau level. This is the Adler–Bell–Jackiw anomaly in a crystal (Nielsen–Ninomiya), and it predicts negative longitudinal magnetoresistance, which current-jetting artefacts complicate.", "map": "\\partial_tn_\\chi=\\chi\\frac{e^2}{4\\pi^2\\hbar^2}\\mathbf E\\cdot\\mathbf B,\\ \\mathbf E\\cdot\\mathbf B=-\\tfrac{c}{4}F_{\\mu\\nu}\\tilde F^{\\mu\\nu}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1152", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics", "b": "08-condensed-matter/magnetism", "name": "Magnetostatic energy, demagnetizing fields and domains", "kind": "mechanism", "summary": "Describing a magnetized body by its bound magnetic charges and currents gives the demagnetizing field and its dipolar self-energy. That energy produces shape anisotropy and, balanced against exchange and crystalline anisotropy, breaks ferromagnets into domains and stabilizes bubble and dipolar-skyrmion textures.", "map": "\\mathbf H_d=-N\\mathbf M,\\ E_d=-\\frac{\\mu_0}{2}\\int\\mathbf M\\cdot\\mathbf H_d\\,dV,\\ \\rho_m=-\\nabla\\cdot\\mathbf M", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1153", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/electrostatics-and-boundary-value-problems", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures", "name": "Coulomb blockade from dot capacitance", "kind": "mechanism", "summary": "Adding one electron to a quantum dot costs the charging energy e²/2C. C and the dot–gate capacitance matrix come from electrostatic boundary-value problems, and gate-defined dots are designed with Poisson/Laplace solvers. Blockade needs E_C≫k_BT and tunnel resistances well above h/e², and the capacitances set the shape of the Coulomb diamonds.", "map": "E_C=\\frac{e^2}{2C},\\ C_{\\rm disk}=8\\epsilon r,\\ k_BT\\ll E_C,\\ R_t\\gg h/e^2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1154", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/fields-in-matter", "b": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "name": "Drude: one response function for optics and DC transport", "kind": "identity", "summary": "The Drude permittivity of fields-in-matter and the Drude conductivity of transport are the same causal response function. The DC resistivity, the plasma edge in reflectivity and the free-carrier absorption are three views of it. Kramers–Kronig relations and the f-sum rule let infrared spectra be read as transport.", "map": "\\sigma(\\omega)=\\frac{ne^2\\tau/m^*}{1-i\\omega\\tau},\\ \\epsilon(\\omega)=1+\\frac{i\\sigma}{\\epsilon_0\\omega}=1-\\frac{\\omega_p^2}{\\omega^2+i\\omega/\\tau}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1155", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/fields-in-matter", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "Lorentz oscillator = polar optical phonon (LST relation)", "kind": "identity", "summary": "The Lorentz-oscillator permittivity of an ionic crystal is the response of its polar optical phonons. The macroscopic field splits LO from TO modes (Lyddane–Sachs–Teller relation), gives total reflection in the reststrahlen band between them, and mixes phonons with photons into phonon-polaritons.", "map": "\\epsilon(\\omega)=\\epsilon_\\infty\\frac{\\omega_{LO}^2-\\omega^2}{\\omega_{TO}^2-\\omega^2},\\ \\frac{\\omega_{LO}^2}{\\omega_{TO}^2}=\\frac{\\epsilon(0)}{\\epsilon(\\infty)}", "breaks": "", "confidence": "established", "strength": 3}