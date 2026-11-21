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

### Moiré materials and twisted bilayers · `knowledge/08-condensed-matter/low-dimensional-and-quantum-materials/moire-materials-and-twisted-bilayers`

**Scope.** Bistritzer–MacDonald continuum model, magic angle ≈1.1°, flat bands and enhanced interactions, correlated insulators and superconducting domes, orbital ferromagnetism and anomalous Hall effect, twisted TMDs (WSe₂, MoTe₂) as Hubbard simulators, Wigner crystals, fractional quantum anomalous Hall states, rhombohedral multilayer graphene, twist-angle disorder.

**Core ideas.**
- At the magic angle the Dirac velocity vanishes, making kinetic energy small compared with Coulomb energy.
- Gate tuning sweeps filling across entire phase diagrams in a single device.
- Flat Chern bands are lattice analogues of Landau levels — enabling fractional states at zero field.

**Key equations.**
$$\theta_{\text{magic}}\approx\frac{3\sqrt3\,w}{4\pi\hbar v_F/a}\approx1.1^\circ\ (w\approx110\ \text{meV}),\qquad n_s=\frac{8\theta^2}{\sqrt3a^2}\ (\text{full filling})$$

**See also.** [Hubbard model](knowledge/08-condensed-matter/strongly-correlated-electrons/hubbard-model-and-mott-physics/README.md) · [Fractionalization](knowledge/08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order/README.md)

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

### Heavy fermions and Kondo physics · `knowledge/08-condensed-matter/strongly-correlated-electrons/heavy-fermions-and-kondo-physics`

**Scope.** Resistance minimum and Kondo's perturbation theory, Anderson impurity model, Wilson's numerical RG solution, Kondo temperature, Kondo effect in quantum dots, Kondo lattice and Doniach phase diagram (RKKY vs. Kondo), heavy-fermion compounds (CeCu₆, YbRh₂Si₂, CeCoIn₅), unconventional superconductivity, topological Kondo insulators (SmB₆).

**Core ideas.**
- Conduction electrons screen a local moment into a many-body singlet below $T_K$; perturbation theory diverges logarithmically.
- In lattices, coherent Kondo screening produces quasiparticles with masses up to ~1000 $m_e$.
- Competition between Kondo screening and RKKY magnetism drives quantum critical points.

**Key equations.**
$$\rho(T)=\rho_0+aT^5-c_K\ln\frac{T}{D},\qquad \gamma=\frac{C}{T}\propto m^*$$

**See also.** [Quantum criticality](knowledge/08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals/README.md) · [Quantum dots](knowledge/08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures/README.md)

### Hubbard model and Mott physics · `knowledge/08-condensed-matter/strongly-correlated-electrons/hubbard-model-and-mott-physics`

**Scope.** One-band Hubbard model, Mott vs. Slater insulators, Brinkman–Rice and DMFT pictures of the Mott transition, strong-coupling expansion to the $t$–$J$ model, Lieb–Wu exact solution in 1D, spin–charge separation, Nagaoka ferromagnetism, cold-atom quantum simulation, V₂O₃ and organic Mott systems, multi-orbital Hund's metals.

**Core ideas.**
- At half filling and large $U/t$, double occupancy is suppressed: electrons localize, leaving spins that order antiferromagnetically ($J=4t^2/U$).
- The Mott transition is driven by interaction, not by band filling.
- Doping a Mott insulator yields pseudogaps, stripes and (likely) d-wave superconductivity.

**Key equations.**
$$H_{tJ}=-t\sum_{\langle ij\rangle\sigma}\mathcal P(c^\dagger_{i\sigma}c_{j\sigma}+\text{h.c.})\mathcal P+J\sum_{\langle ij\rangle}\left(\mathbf S_i\cdot\mathbf S_j-\tfrac14n_in_j\right)$$

**See also.** [Optical lattices](knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation/README.md) · [Cuprates](knowledge/08-condensed-matter/superconductivity/cuprate-high-tc-superconductors/README.md)

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

# Packet 08-2 (100 records)

{"id": "C1156", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/fields-in-matter", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/transition-metal-dichalcogenides-and-excitons", "name": "Rytova–Keldysh screening and 2D exciton binding", "kind": "mechanism", "summary": "Thin-film electrostatics of a polarizable sheet gives a potential that is logarithmic below the screening length r0 and 1/r beyond it. This explains the non-hydrogenic Rydberg series and the ~0.5 eV exciton binding energies of monolayer TMDs. Changing the dielectric surroundings (encapsulation) shifts the gap and the binding energy, an approach called Coulomb engineering.", "map": "V(r)\\propto-\\left[H_0\\!\\left(\\frac{r}{r_0}\\right)-Y_0\\!\\left(\\frac{r}{r_0}\\right)\\right],\\ \\sim\\ln r\\ (r\\ll r_0),\\ \\sim1/r\\ (r\\gg r_0)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1157", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/fields-in-matter", "b": "08-condensed-matter/magnetism", "name": "Quantum origin of dia-, para- and ferromagnetic χ", "kind": "mechanism", "summary": "The susceptibility that fields-in-matter takes as an input is quantum mechanical. By the Bohr–van Leeuwen theorem, classical statistics gives zero magnetization. Condensed matter supplies the actual sources: Landau diamagnetism, Pauli and Curie paramagnetism, and exchange-driven order. For free electrons the Landau term is −1/3 of the Pauli term.", "map": "\\mathbf M=\\chi_m\\mathbf H,\\ \\chi_{\\rm P}=\\mu_0\\mu_B^2g(E_F),\\ \\chi_{\\rm L}=-\\tfrac13\\chi_{\\rm P},\\ \\chi_{\\rm C}=\\frac{C}{T}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1158", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/fields-in-matter", "b": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "name": "Weiss molecular field as mean-field exchange", "kind": "mechanism", "summary": "The fields-in-matter note treats ferromagnetism phenomenologically, through a huge χ and hysteretic M(H). Exchange theory supplies the cause: Weiss's molecular field is the mean field of Heisenberg exchange, which gives a Curie–Weiss susceptibility above T_c and spontaneous magnetization below it.", "map": "H=-J\\sum_{\\langle ij\\rangle}\\mathbf S_i\\cdot\\mathbf S_j\\ \\to\\ \\mathbf B_{\\rm W}=\\lambda\\mathbf M,\\ \\chi=\\frac{C}{T-\\theta_{CW}}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1159", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/fields-in-matter", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Optical gap 2Δ and the Ferrell–Glover–Tinkham sum rule", "kind": "mechanism", "summary": "A superconductor absorbs only above ħω=2Δ (Mattis–Bardeen), and far-infrared measurements of this edge were among the first gap measurements. The spectral weight that disappears from σ1 collapses into a superfluid δ(ω) whose weight fixes the London penetration depth. This links fields-in-matter response theory to the London depth and BCS.", "map": "\\int_{0^+}^{\\infty}[\\sigma_1^n-\\sigma_1^s]d\\omega=\\frac{\\pi n_se^2}{2m}=\\frac{\\pi}{2\\mu_0\\lambda_L^2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1160", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/fields-in-matter", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "Modern theory of polarization: P as a Berry phase", "kind": "identity", "summary": "For a periodic crystal the bulk polarization P is not well defined as a sum of dipoles. It is well defined, up to the polarization quantum eR/Ω, as the Berry phase of the occupied Bloch states (King-Smith–Vanderbilt). Changes in P (piezoelectric, ferroelectric, Thouless pumping) are what DFT computes and what experiments measure.", "map": "\\mathbf P=-\\frac{e}{(2\\pi)^3}\\sum_n\\int_{\\rm BZ}i\\langle u_{n\\mathbf k}|\\nabla_{\\mathbf k}u_{n\\mathbf k}\\rangle\\,d^3k\\ (\\mathrm{mod}\\ e\\mathbf R/\\Omega)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1161", "a": "02-electromagnetism-and-optics/photonics-and-lasers/laser-physics", "b": "08-condensed-matter/crystals-and-electronic-structure/semiconductors", "name": "Diode lasers: inversion between quasi-Fermi levels", "kind": "mechanism", "summary": "In a semiconductor laser, population inversion is a separation of the electron and hole quasi-Fermi levels in a forward-biased p–n junction. Gain appears when the Bernard–Duraffourg condition holds. Double heterostructures and quantum wells confine both carriers and light, and Fermi–Dirac band filling takes the place of two-level atoms.", "map": "E_{F,c}-E_{F,v}>\\hbar\\omega>E_g", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1162", "a": "02-electromagnetism-and-optics/photonics-and-lasers/laser-physics", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/transition-metal-dichalcogenides-and-excitons", "name": "Exciton-polariton lasing without inversion", "kind": "mechanism", "summary": "When excitons couple strongly to microcavity photons they form polaritons, which can condense and emit coherent light with no population inversion: a polariton laser. The large exciton binding energy of TMD monolayers allows room-temperature polaritons, and polariton condensation in TMDs is under active study.", "map": "E_\\pm=\\tfrac12(E_c+E_x)\\pm\\tfrac12\\sqrt{(E_c-E_x)^2+(\\hbar\\Omega_R)^2}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1163", "a": "02-electromagnetism-and-optics/photonics-and-lasers/laser-physics", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Laser threshold as a Ginzburg–Landau transition", "kind": "analogy", "summary": "Near threshold the single-mode laser amplitude obeys a Ginzburg–Landau equation: the field is the order parameter and gain minus loss plays the role of reduced temperature (Haken; DeGiorgio–Scully). Above threshold a U(1) phase is chosen spontaneously, and diffusion of that phase, a Goldstone-like mode, sets the Schawlow–Townes linewidth.", "map": "\\dot E=(g-\\kappa)E-\\beta|E|^2E\\ \\leftrightarrow\\ F=a(T-T_c)|\\psi|^2+\\tfrac b2|\\psi|^4", "breaks": "A laser is driven-dissipative and far from equilibrium, and its noise comes from spontaneous emission, not temperature. With few modes there is no true symmetry breaking, so the phase diffuses and the linewidth is finite. There is no gauge field, hence no Meissner or Higgs counterpart.", "confidence": "established", "strength": 2}
{"id": "C1164", "a": "02-electromagnetism-and-optics/photonics-and-lasers/metamaterials-and-plasmonics", "b": "08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons", "name": "Photonic crystals: Bloch band theory for light", "kind": "method transfer", "summary": "Yablonovitch and John applied Bloch's theorem to Maxwell's equations in periodic dielectrics. The result is photonic band structures, band gaps, defect states and slow-light band edges, computed with the electronic-structure toolkit (plane-wave expansion, tight-binding coupled resonators).", "map": "\\nabla\\times\\frac{1}{\\epsilon(\\mathbf r)}\\nabla\\times\\mathbf H=\\frac{\\omega^2}{c^2}\\mathbf H,\\ \\mathbf H_{\\mathbf k}=e^{i\\mathbf k\\cdot\\mathbf r}\\mathbf u_{\\mathbf k}(\\mathbf r)", "breaks": "The field is a transverse vector field with no interactions and no Pauli exclusion. The eigenvalue is ω² rather than E, and Maxwell scale invariance lets the gap scale with the lattice constant. Full 3D gaps need a high index contrast.", "confidence": "established", "strength": 3}
{"id": "C1165", "a": "02-electromagnetism-and-optics/photonics-and-lasers/metamaterials-and-plasmonics", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "name": "Graphene plasmons and hBN hyperbolic polaritons", "kind": "shared object", "summary": "Graphene is a gate-tunable 2D plasmonic medium with a √q dispersion set by E_F. Near-field microscopy images its plasmons at wavelengths far below the free-space wavelength. Inside its reststrahlen bands hBN is a natural hyperbolic medium (ε_∥ε_⊥<0), so van der Waals heterostructures act as natural metamaterials.", "map": "\\omega_{pl}^2=\\frac{e^2E_F\\,q}{\\pi\\hbar^2\\epsilon_0(\\epsilon_1+\\epsilon_2)},\\ E_F=\\hbar v_F\\sqrt{\\pi n}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1166", "a": "02-electromagnetism-and-optics/photonics-and-lasers/metamaterials-and-plasmonics", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures", "name": "Quantum-dot emission controlled by the local density of states", "kind": "mechanism", "summary": "A quantum dot's spontaneous-emission rate follows the local optical density of states. Photonic band gaps suppress it, and photonic-crystal nanocavities and plasmonic nanoantennas raise it (the Purcell effect). This underlies deterministic single-photon sources and vacuum Rabi splitting with single dots.", "map": "\\Gamma\\propto|\\mathbf d|^2\\rho_{\\rm LDOS}(\\mathbf r,\\omega),\\ F_P=\\frac{3}{4\\pi^2}\\left(\\frac{\\lambda}{n}\\right)^3\\frac{Q}{V}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1167", "a": "02-electromagnetism-and-optics/photonics-and-lasers/nonlinear-optics", "b": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "name": "χ(2) selection rules and SHG as a symmetry probe", "kind": "mechanism", "summary": "χ(2) is a polar third-rank tensor. It vanishes in the 11 centrosymmetric point groups and in 432, leaving the same 20 classes that allow piezoelectricity. SHG therefore detects broken inversion (ferroelectric and other polar orders, surfaces, odd versus even layer number in 2D crystals), and quasi-phase-matching relies on periodically poled ferroelectric domains.", "map": "P_i^{(2\\omega)}=\\epsilon_0\\chi^{(2)}_{ijk}E_jE_k,\\ \\mathcal I:\\chi^{(2)}\\to-\\chi^{(2)}\\Rightarrow\\chi^{(2)}=0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1168", "a": "02-electromagnetism-and-optics/photonics-and-lasers/topological-photonics", "b": "08-condensed-matter/topological-matter", "name": "Haldane–Raghu: quantum Hall physics carried into light", "kind": "historical", "summary": "Haldane and Raghu (2008) carried the Chern-band physics of the quantum Hall effect and Haldane's 1988 lattice model into gyromagnetic photonic crystals. One-way microwave edge states were then seen in YIG (Wang et al. 2009), which founded topological photonics. The field later imported quantum spin Hall, valley Hall, Floquet and higher-order phases.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1169", "a": "02-electromagnetism-and-optics/photonics-and-lasers/topological-photonics", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "Berry curvature and Chern numbers of Maxwell Bloch modes", "kind": "identity", "summary": "The Bloch eigenmodes of the periodic Maxwell operator have a Berry connection and curvature, defined with the ε- or μ-weighted inner product, and their Chern numbers are integers exactly as for electron bands (TKNN). Magneto-optic gyrotropy breaks time reversal in place of a magnetic field, and bulk–edge correspondence fixes the number of one-way edge modes.", "map": "C=\\frac{1}{2\\pi}\\int_{\\rm BZ}\\Omega(\\mathbf k)\\,d^2k\\in\\mathbb Z,\\ \\Omega=\\nabla_{\\mathbf k}\\times i\\langle u_{\\mathbf k}|\\nabla_{\\mathbf k}u_{\\mathbf k}\\rangle,\\ N_{\\rm edge}=\\Delta C", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1170", "a": "02-electromagnetism-and-optics/photonics-and-lasers/topological-photonics", "b": "08-condensed-matter/topological-matter/topological-insulators", "name": "Photonic quantum spin Hall and valley Hall insulators", "kind": "analogy", "summary": "Photonic crystals and coupled-resonator lattices copy the quantum spin Hall effect with a pseudospin. That pseudospin comes from TE/TM degeneracy (ε=μ), C6 crystalline symmetry or the circulation direction in a ring. The result is helical edge states that pass around sharp corners, much like the edges of a Z2 topological insulator.", "map": "H_{\\rm KM}\\leftrightarrow H_{\\rm photonic}(\\sigma_{\\rm pseudo}),\\ \\nu\\in\\mathbb Z_2\\leftrightarrow C_\\uparrow=-C_\\downarrow", "breaks": "Photons are bosons with T^2=+1, so there is no Kramers degeneracy. The protection lasts only while the engineered pseudospin symmetry does, and lattice-scale disorder can couple the edge modes. With no Fermi level, the edge states must be excited at a chosen frequency.", "confidence": "established", "strength": 3}
{"id": "C1171", "a": "02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics", "b": "08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons", "name": "High-harmonic generation in solids probes band structure", "kind": "method transfer", "summary": "Strong-field HHG, first developed in atomic gases, also works in bulk crystals (ZnO and others). There it comes from intraband currents of Bloch-oscillating carriers in nonparabolic bands plus interband recombination, the three-step model adapted to bands. The cutoff grows linearly with field rather than quadratically, and harmonic spectra allow all-optical reconstruction of the band structure.", "map": "\\hbar\\omega_{\\max}^{\\rm solid}\\propto E_0\\ \\text{vs}\\ I_p+3.17U_p\\propto E_0^2,\\ \\omega_B=\\frac{eE_0a}{\\hbar}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1172", "a": "02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics", "b": "08-condensed-matter/magnetism/spintronics", "name": "Ultrafast demagnetization and spintronic THz emitters", "kind": "mechanism", "summary": "Femtosecond pulses demagnetize Ni in under a picosecond (Beaurepaire et al. 1996) and switch ferrimagnets such as GdFeCo all-optically. The ultrafast spin currents involved are converted to charge currents by the inverse spin Hall effect, which makes ferromagnet/heavy-metal bilayers broadband THz emitters. Whether spin-flip scattering or superdiffusive transport dominates is still debated.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1173", "a": "02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics", "b": "08-condensed-matter/superconductivity/cuprate-high-tc-superconductors", "name": "Light-induced transient superconductivity (contested)", "kind": "method transfer", "summary": "Mid-infrared pumping of apical-oxygen phonons in stripe-ordered LESCO and in YBCO produces a transient c-axis optical response resembling superconductivity above T_c, with similar claims for K3C60. The interpretation is contested: heating, inhomogeneity and the analysis of reflectivity are all debated. Reports of transient Meissner-like diamagnetism are recent and unconfirmed.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1174", "a": "02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "Floquet engineering of Chern bands with circular light", "kind": "mechanism", "summary": "A strong circularly polarized drive dresses Bloch bands. In the high-frequency expansion it opens a Haldane-type mass at Dirac points and creates Chern bands (Oka–Aoki). Floquet–Bloch states have been seen on topological-insulator surfaces by tr-ARPES, and a light-induced anomalous Hall effect in graphene. Helical-waveguide photonic Floquet insulators use the same idea.", "map": "H_{\\rm eff}\\approx H_0+\\frac{[H_1,H_{-1}]}{\\hbar\\Omega},\\ \\Delta\\sim\\frac{(ev_FE_0)^2}{\\hbar\\Omega^3}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1175", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "name": "X-ray diffraction as coherent Thomson scattering", "kind": "mechanism", "summary": "X-ray crystallography is Thomson scattering from the electron density, summed coherently over the lattice. The atomic form factor is the Fourier transform of an atom's charge density, Bragg/Laue conditions select the reciprocal-lattice vectors, and the intensity goes as the squared structure factor.", "map": "I(\\mathbf q)\\propto\\frac{d\\sigma_T}{d\\Omega}|F(\\mathbf q)|^2,\\ F(\\mathbf G)=\\sum_jf_je^{i\\mathbf G\\cdot\\mathbf r_j},\\ 2d\\sin\\theta=n\\lambda", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1176", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "Raman and Brillouin scattering as phonon spectroscopy", "kind": "method transfer", "summary": "Inelastic light scattering, with energy and momentum conserved, measures optical phonons near q=0 (Raman, with selection rules set by the point group) and acoustic phonons (Brillouin, whose shift gives the sound velocity). The Stokes/anti-Stokes ratio gives the temperature through the Bose factor. Electrostrictive coupling to the same phonons drives stimulated Brillouin scattering in fibres.", "map": "\\Omega_B=2nv_s\\frac{\\omega}{c}\\sin\\frac{\\theta}{2},\\ \\frac{I_{aS}}{I_S}\\approx e^{-\\hbar\\Omega/k_BT}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1470", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/laws-of-thermodynamics", "b": "08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids", "name": "Spin ice and Pauling's residual entropy", "kind": "identity", "summary": "On the pyrochlore lattice of Dy₂Ti₂O₇ and Ho₂Ti₂O₇, the 'two-in, two-out' rule is Pauling's ice rule for protons in water ice, so the ground state is macroscopically degenerate. Heat-capacity measurements recovered Pauling's residual entropy of $\\frac R2\\ln\\frac32$ per mole of spins, an apparent exception to the third law that only weak residual interactions acting over very long equilibration times can lift.", "map": "S_0=\\frac{R}{2}\\ln\\frac32\\approx1.68\\ \\mathrm{J\\,mol^{-1}\\,K^{-1}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1471", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/phase-equilibria-and-chemical-potential", "b": "08-condensed-matter/soft-matter/active-matter", "name": "Motility-induced phase separation as liquid–gas coexistence", "kind": "analogy", "summary": "Self-propelled particles that slow down where crowded separate into dense and dilute phases without any attraction (motility-induced phase separation). To leading order the dynamics maps onto an effective free energy, giving a spinodal at $d\\ln v/d\\ln\\rho<-1$ and a coexistence that resembles the liquid–gas transition.", "map": "\\frac{d\\ln v(\\rho)}{d\\ln\\rho}<-1\\ \\ (\\text{spinodal}),\\quad \\mu_{\\rm eff}(\\rho)=\\ln\\rho+\\ln v(\\rho)", "breaks": "There is no equilibrium free energy: binodals do not follow a Maxwell construction on $\\mu_{\\rm eff}$, and mechanical pressure need not balance in the usual way. Gradient terms can also produce reverse Ostwald ripening and microphase separation.", "confidence": "current research", "strength": 3}
{"id": "C1472", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems", "b": "08-condensed-matter/soft-matter/glasses-and-jamming", "name": "Jamming as a critical point of disordered packings", "kind": "mechanism", "summary": "Athermal packings jam at the isostatic point, where the mean contact number reaches $z_c=2d$. Above it, excess contacts and shear modulus scale as powers of $\\phi-\\phi_J$, as near a critical point. Liu and Nagel's jamming phase diagram links this to the glass transition, and the infinite-dimensional replica solution ties jamming to marginal stability and full replica-symmetry breaking (the Gardner phase).", "map": "z_c=2d,\\quad \\Delta z\\propto(\\phi-\\phi_J)^{1/2},\\quad G\\propto(\\phi-\\phi_J)^{1/2},\\ B\\approx\\text{const}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1473", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/localization-and-disorder", "b": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "name": "Weak localization and scaling theory in metals", "kind": "mechanism", "summary": "Constructive interference of time-reversed backscattering paths lowers the conductance of disordered metals (weak localization). A magnetic field or dephasing cuts it off, and it leaves universal conductance fluctuations of order $e^2/h$. One-parameter scaling in the dimensionless conductance $g$ predicts that all states localize in 1D and 2D (without spin–orbit coupling) and that 3D has a mobility edge.", "map": "\\beta(g)=\\frac{d\\ln g}{d\\ln L},\\quad \\delta\\sigma_{2D}\\propto-\\frac{e^2}{h}\\ln\\frac{\\ell_\\phi}{\\ell},\\quad \\delta G_{\\rm UCF}\\sim\\frac{e^2}{h}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1474", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/localization-and-disorder", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "Altland–Zirnbauer classes become the tenfold way", "kind": "identity", "summary": "The ten symmetry classes of disordered Hamiltonians, built from time-reversal, particle–hole and chiral symmetry (Altland–Zirnbauer), are the same ten classes that classify gapped topological insulators and superconductors. In each dimension the classes with a nontrivial invariant are those whose boundary modes cannot be Anderson-localized, one of the routes to the periodic table (Schnyder–Ryu–Furusaki–Ludwig, Kitaev).", "map": "\\{\\mathrm{A,AIII,AI,BDI,D,DIII,AII,CII,C,CI}\\}\\times d\\ \\to\\ 0,\\ \\mathbb Z,\\ 2\\mathbb Z,\\ \\mathbb Z_2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1475", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/localization-and-disorder", "b": "08-condensed-matter/topological-matter/quantum-hall-effects", "name": "Quantum Hall plateau transition as Anderson localization", "kind": "mechanism", "summary": "Quantized plateaus need disorder: states in the Landau-level tails are Anderson-localized and leave $\\sigma_{xy}$ unchanged, while only one energy per level is extended. The plateau-to-plateau transition is a localization–delocalization critical point with $\\nu\\approx2.6$ (Chalker–Coddington network), not the classical-percolation value $4/3$, and its width shrinks as $T^{\\kappa}$.", "map": "\\xi\\propto|E-E_c|^{-\\nu},\\ \\nu\\approx2.6;\\quad \\Delta B\\propto T^{\\kappa},\\ \\kappa=\\frac{1}{z\\nu}\\approx0.42", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1476", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/percolation", "b": "08-condensed-matter/soft-matter/polymers", "name": "Gelation is percolation", "kind": "identity", "summary": "Flory–Stockmayer gelation theory is percolation on a Bethe lattice, and the sol–gel transition of crosslinking polymers is a connectivity-percolation threshold, with the gel fraction as order parameter and percolation scaling for the finite clusters. Close to the gel point, 3D percolation exponents replace the Flory–Stockmayer mean-field values (de Gennes, Stauffer).", "map": "p_c=\\frac{1}{f-1}\\ (\\text{Bethe}),\\quad P_{\\rm gel}\\propto(p-p_c)^{\\beta},\\ \\beta_{\\rm MF}=1,\\ \\beta_{3D}\\approx0.42", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1477", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/spin-glasses", "b": "08-condensed-matter/magnetism", "name": "Dilute magnetic alloys: RKKY makes spin glasses", "kind": "mechanism", "summary": "The canonical spin glasses are dilute magnetic alloys (CuMn, AuFe) whose moments couple by RKKY exchange, which oscillates in sign with distance. Random positions therefore give random-sign couplings, the physical basis of the Edwards–Anderson model, and the susceptibility cusp at $T_f$ marks the freezing; insulating spin glasses such as Eu$_x$Sr$_{1-x}$S arise instead from competing ferro- and antiferromagnetic exchange.", "map": "J_{\\rm RKKY}(r)\\propto\\frac{\\cos(2k_Fr)}{(2k_Fr)^3},\\quad H=-\\sum_{\\langle ij\\rangle}J_{ij}\\mathbf S_i\\cdot\\mathbf S_j,\\ J_{ij}\\ \\text{random}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1478", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/spin-glasses", "b": "08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids", "name": "Frustration with and without disorder", "kind": "analogy", "summary": "Both start from frustration: when the couplings around a loop have a negative product, no spin arrangement satisfies all of them, and many low-energy states result. With quenched random couplings the spins freeze into a spin glass with Edwards–Anderson order $q$. Geometric frustration on clean triangular, kagome or pyrochlore lattices can instead give order by disorder, spin ice or a quantum spin liquid, and a little bond disorder often turns such magnets into spin glasses.", "map": "\\prod_{\\langle ij\\rangle\\in\\square}\\mathrm{sgn}\\,J_{ij}=-1,\\quad q_{\\rm EA}=\\overline{\\langle S_i\\rangle^2}", "breaks": "A spin glass needs quenched randomness and freezes into a static random state governed by replica-symmetry breaking. A spin liquid is clean, can stay dynamic down to T=0 and is characterised by long-range entanglement and fractionalized excitations, which have no spin-glass counterpart.", "confidence": "established", "strength": 2}
{"id": "C1479", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/spin-glasses", "b": "08-condensed-matter/soft-matter/glasses-and-jamming", "name": "Spin-glass theory of the structural glass transition", "kind": "analogy", "summary": "Mean-field $p$-spin glasses have a dynamical transition at $T_d$, whose equations coincide with mode-coupling theory of supercooled liquids, and a Kauzmann-like entropy crisis at $T_K$; together these form the random first-order transition theory of glasses (Kirkpatrick, Thirumalai, Wolynes). Aging, rugged landscapes and replica methods carry over, culminating in the exact solution for hard spheres in infinite dimensions.", "map": "T_K<T_d:\\ \\tau\\sim(T-T_d)^{-\\gamma}\\ (\\text{MCT}),\\quad \\tau\\sim\\tau_0e^{A/TS_c(T)}\\ (\\text{Adam–Gibbs})", "breaks": "Structural glasses have no quenched disorder; it is self-generated. The sharp mean-field $T_d$ becomes a crossover in finite dimensions, and the Edwards–Anderson Ising spin glass (full RSB, continuous transition) belongs to a different class from the one-step RSB models that mimic glasses.", "confidence": "current research", "strength": 3}
{"id": "C1480", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information", "b": "08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order", "name": "Topological entanglement entropy", "kind": "identity", "summary": "In a gapped 2D phase the entanglement entropy of a region obeys an area law with a universal constant correction, $S_A=\\alpha L-\\gamma$, where $\\gamma=\\ln\\mathcal D$ is set by the anyons' quantum dimensions (Kitaev–Preskill, Levin–Wen). This information-theoretic quantity detects topological order without a local order parameter; $\\gamma=\\ln2$ for the toric code and $\\mathbb Z_2$ spin liquids.", "map": "S_A=\\alpha|\\partial A|-\\gamma,\\quad \\gamma=\\ln\\mathcal D,\\ \\mathcal D=\\sqrt{\\textstyle\\sum_ad_a^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1481", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/exactly-solvable-models", "b": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "name": "Bethe ansatz and spinons in Heisenberg chains", "kind": "identity", "summary": "Bethe's 1931 solution of the spin-1/2 Heisenberg chain founded the Bethe ansatz; its elementary excitations are spin-1/2 spinons, created in pairs, with the des Cloizeaux–Pearson dispersion. Neutron scattering on chain compounds such as KCuF₃ sees the predicted two-spinon continuum instead of sharp magnons.", "map": "H=J\\sum_i\\mathbf S_i\\cdot\\mathbf S_{i+1},\\quad \\epsilon_s(k)=\\frac{\\pi J}{2}|\\sin k|", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1482", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/exactly-solvable-models", "b": "08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids", "name": "Kitaev honeycomb model and Kitaev materials", "kind": "shared object", "summary": "Kitaev's honeycomb model, with bond-dependent Ising couplings, is solved exactly by writing the spins as Majorana fermions in a static $\\mathbb Z_2$ gauge field; it has gapped and gapless spin liquids and, in a magnetic field, a non-Abelian phase. Jackeli and Khaliullin showed that edge-sharing $j=1/2$ magnets approximate it, launching the search in iridates and α-RuCl₃, whose reported half-quantized thermal Hall effect remains contested.", "map": "H=-\\sum_{\\gamma=x,y,z}K_\\gamma\\sum_{\\langle ij\\rangle_\\gamma}\\sigma_i^\\gamma\\sigma_j^\\gamma,\\quad \\sigma_i^\\gamma=i\\,b_i^\\gamma c_i", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1483", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "08-condensed-matter/crystals-and-electronic-structure", "name": "Degenerate electrons and phonon gas in solids", "kind": "identity", "summary": "Conduction electrons form a degenerate Fermi gas: only a fraction $k_BT/E_F$ near the Fermi surface is excited, giving the Sommerfeld heat capacity $\\gamma T$, Pauli paramagnetism and the Fermi–Dirac carrier statistics of semiconductors. Phonons are a Bose gas with zero chemical potential and give the Debye $T^3$ law, so a metal's low-temperature heat capacity is $\\gamma T+\\beta T^3$.", "map": "C=\\gamma T+\\beta T^3,\\quad \\gamma=\\frac{\\pi^2}{3}k_B^2g(E_F),\\quad \\beta=\\frac{12\\pi^4}{5}\\frac{Nk_B}{\\Theta_D^3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1484", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/transition-metal-dichalcogenides-and-excitons", "name": "Excitons as composite bosons: 2D exciton condensates", "kind": "shared object", "summary": "Interlayer excitons in transition-metal-dichalcogenide double layers are long-lived composite bosons that, at low temperature and density, should Bose-condense, which in 2D means a BKT superfluid. Experiments on TMD double layers report signatures of exciton condensation and excitonic insulators.", "map": "k_BT_{\\rm BKT}=\\frac{\\pi\\hbar^2n_s}{2m_X},\\quad n_Xa_X^2\\ll1", "breaks": "Excitons behave as bosons only when $n_Xa_X^2\\ll1$; at higher density, exchange between their fermionic constituents and screening dissociate them into an electron–hole plasma (the excitonic Mott transition). Disorder and finite lifetime further limit coherence.", "confidence": "current research", "strength": 2}
{"id": "C1485", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "BCS–BEC crossover: Cooper pairs to Bose condensate", "kind": "mechanism", "summary": "Cooper's bound state exists only because the filled Fermi sea blocks the states below $k_F$. As the attraction grows, large overlapping Cooper pairs turn continuously into tightly bound bosonic molecules that Bose-condense, so $T_c$ rises from the exponentially small BCS value to about $0.218\\,T_F$; this crossover was realised with Feshbach-tuned ultracold fermions.", "map": "k_BT_c^{\\rm BEC}=\\frac{2\\pi\\hbar^2}{m_B}\\Big(\\frac{n_B}{\\zeta(3/2)}\\Big)^{2/3}\\ (m_B=2m,\\ n_B=\\tfrac n2),\\quad k_BT_c^{\\rm BCS}\\approx1.13\\,\\hbar\\omega_De^{-1/N(0)V}", "breaks": "A conventional superconductor is not a BEC of preformed pairs: the pair size far exceeds the spacing between pairs, and $T_c$ is set by pair breaking, not by the onset of phase coherence.", "confidence": "established", "strength": 3}
{"id": "C1486", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics", "b": "08-condensed-matter/soft-matter", "name": "Soft matter as the laboratory of stochastic thermodynamics", "kind": "shared object", "summary": "Because soft-matter energies are of order $k_BT$, colloids in optical traps have been used to test the fluctuation theorem, the Jarzynski and Crooks relations and Landauer's erasure bound. Colloidal and polymer glasses show aging and fluctuation–dissipation violations, which are described with an effective temperature.", "map": "\\langle e^{-\\beta W}\\rangle=e^{-\\beta\\Delta F},\\quad \\langle Q_{\\rm erase}\\rangle\\ge k_BT\\ln2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1487", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics", "b": "08-condensed-matter/soft-matter/active-matter", "name": "Active particles break fluctuation–dissipation", "kind": "mechanism", "summary": "Active Brownian particles obey Langevin dynamics plus persistent self-propulsion, so long-time diffusion far exceeds the Stokes–Einstein value and the fluctuation–dissipation theorem fails. Mechanical pressure on a wall can depend on the wall potential, so pressure is not in general a state function.", "map": "D_{\\rm eff}=D_t+\\frac{v_0^2}{d(d-1)D_r}\\quad(\\text{vs. }D=\\mu k_BT)", "breaks": "No single effective temperature exists: trapped-particle distributions, equations of state and fluctuation–dissipation ratios each give a different value, and the steady state depends on dynamical details that equilibrium ignores.", "confidence": "current research", "strength": 2}
{"id": "C1488", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/driven-systems-and-nonequilibrium-steady-states", "b": "08-condensed-matter/soft-matter/active-matter", "name": "Active matter as a driven non-equilibrium steady state", "kind": "mechanism", "summary": "Self-propulsion injects energy at every particle and breaks detailed balance locally, so active fluids are non-equilibrium steady states with nonzero entropy production. Active lattice gases are exclusion processes with persistent hopping, and the signatures of driven systems (currents, long-range correlations, giant number fluctuations $\\Delta N\\propto N^{\\alpha}$ with $\\alpha>1/2$) appear in flocks and active nematics.", "map": "\\dot{\\mathbf r}_i=v_0\\hat{\\mathbf e}(\\theta_i)+\\sqrt{2D_t}\\,\\boldsymbol\\xi_i,\\quad \\dot\\theta_i=\\sqrt{2D_r}\\,\\eta_i,\\quad \\Delta N\\propto N^{\\alpha},\\ \\alpha>\\tfrac12", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1489", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "name": "Boltzmann equation for Bloch electrons", "kind": "identity", "summary": "The semiclassical Boltzmann equation with Bloch velocities, a Fermi–Dirac equilibrium and a relaxation time gives the Drude conductivity, Hall coefficient, thermopower and Wiedemann–Franz law; only states within $k_BT$ of the Fermi surface contribute. Where electron–electron collisions conserve momentum, as in graphene's Dirac fluid, the same kinetic theory gives electron hydrodynamics and violations of Wiedemann–Franz.", "map": "\\partial_tf+\\mathbf v\\cdot\\nabla_{\\mathbf r}f-\\frac{e}{\\hbar}(\\mathbf E+\\mathbf v\\times\\mathbf B)\\cdot\\nabla_{\\mathbf k}f=-\\frac{f-f_0}{\\tau},\\ \\sigma=\\frac{ne^2\\tau}{m^*}", "breaks": "It fails where quantum interference matters (weak localization) and in correlated metals without quasiparticles.", "confidence": "established", "strength": 3}
{"id": "C1490", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "Kinetic theory of the phonon gas", "kind": "identity", "summary": "Lattice heat conduction is the kinetic theory of a phonon gas: the Peierls–Boltzmann equation gives $\\kappa=\\tfrac13C_Vv\\ell$, the dilute-gas formula. Only Umklapp collisions relax crystal momentum, so $\\kappa$ grows exponentially on cooling until boundary scattering takes over; when momentum-conserving normal processes dominate, phonons flow hydrodynamically and carry second sound.", "map": "\\kappa=\\tfrac13C_Vv\\ell,\\quad \\tau_U^{-1}\\propto T^{n}e^{-\\Theta_D/bT}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1491", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation", "b": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "name": "Kubo formula and Johnson–Nyquist noise", "kind": "identity", "summary": "Electrical conductivity is a current–current correlation function (the Kubo or Green–Kubo formula), and the fluctuation–dissipation theorem fixes every resistor's equilibrium voltage noise at $S_V=4k_BTR$ (Johnson–Nyquist). The same Kubo formula, evaluated for Bloch bands, gives TKNN's quantized Hall conductance.", "map": "\\sigma=\\frac{1}{Vk_BT}\\int_0^\\infty\\langle J(t)J(0)\\rangle\\,dt\\ (\\text{classical}),\\quad S_V(\\omega)=4k_BTR", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1492", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation", "b": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "name": "Neutron scattering measures the dynamic susceptibility", "kind": "method transfer", "summary": "The magnetic inelastic neutron cross-section is proportional to the dynamic structure factor $S(\\mathbf q,\\omega)$, which the fluctuation–dissipation theorem equates to the absorptive susceptibility $\\chi''(\\mathbf q,\\omega)$ times a Bose factor. Magnon dispersions, critical scattering near $T_c$ and spinon continua are therefore measured response functions, and detailed balance between $\\pm\\omega$ serves as a built-in check.", "map": "S(\\mathbf q,\\omega)\\propto\\frac{\\chi''(\\mathbf q,\\omega)}{1-e^{-\\hbar\\omega/k_BT}},\\quad S(\\mathbf q,-\\omega)=e^{-\\hbar\\omega/k_BT}S(\\mathbf q,\\omega)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1493", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "08-condensed-matter/soft-matter/colloids-and-granular-matter", "name": "Colloids as Brownian particles; grains as athermal limit", "kind": "shared object", "summary": "Colloidal particles are the Brownian particles of Einstein's 1905 theory and Perrin's experiments: they follow overdamped Langevin dynamics with Stokes–Einstein diffusion, and an optically trapped colloid is a textbook Ornstein–Uhlenbeck process. Granular grains obey the same mechanics with $k_BT$ negligible against gravity, so driving must replace temperature and fluctuation–dissipation no longer holds.", "map": "\\gamma\\dot x=-U'(x)+\\sqrt{2\\gamma k_BT}\\,\\xi(t),\\quad D=\\frac{k_BT}{6\\pi\\eta a}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1494", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "08-condensed-matter/soft-matter/polymers", "name": "Rouse, Zimm and reptation: Langevin dynamics of chains", "kind": "method transfer", "summary": "A polymer modelled as beads joined by entropic springs, each bead obeying overdamped Langevin dynamics, splits into Rouse modes with longest time $\\tau_R\\propto N^2$; hydrodynamic interactions turn this into Zimm scaling $\\tau\\propto N^{3\\nu}$. In entangled melts, de Gennes' reptation treats the chain as a random walker confined to a tube, giving $\\tau_d\\propto N^3$ (experimentally about $N^{3.4}$).", "map": "\\zeta\\dot{\\mathbf R}_n=k(\\mathbf R_{n+1}-2\\mathbf R_n+\\mathbf R_{n-1})+\\mathbf f_n,\\quad \\tau_R\\propto N^2,\\ \\tau_d\\propto N^3", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1495", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "RCSJ junction: Brownian particle in a tilted washboard", "kind": "identity", "summary": "In the resistively and capacitively shunted junction model, the phase difference $\\varphi$ is a damped particle of mass $\\propto C$ in the tilted washboard $U=-E_J\\cos\\varphi-(\\hbar I/2e)\\varphi$, kicked by the shunt's Johnson noise. Thermal switching out of the zero-voltage state is Kramers escape, and below $T^*\\approx\\hbar\\omega_p/2\\pi k_B$ macroscopic quantum tunnelling of $\\varphi$ takes over (Caldeira–Leggett).", "map": "\\left(\\frac{\\hbar}{2e}\\right)^2\\Big(C\\ddot\\varphi+\\frac{\\dot\\varphi}{R}\\Big)+E_J\\sin\\varphi=\\frac{\\hbar}{2e}(I+\\delta I),\\quad \\Gamma\\propto e^{-\\Delta U/k_BT}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1496", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena", "b": "08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals", "name": "Quantum–classical mapping and Hertz–Millis theory", "kind": "identity", "summary": "In imaginary time a quantum transition in $d$ dimensions becomes a classical one in $d+z$ dimensions, so Landau–Ginzburg–Wilson theory, the RG and the Ginzburg criterion carry over. Hertz–Millis theory applies this to metallic magnets: Landau damping gives $z=3$ for ferromagnets and $z=2$ for antiferromagnets, and a quantum critical fan opens above $g_c$, bounded by $k_BT\\sim|g-g_c|^{z\\nu}$.", "map": "S=\\sum_{\\mathbf q,\\omega_n}\\Big(r+q^2+\\frac{|\\omega_n|}{\\Gamma_q}\\Big)|\\phi|^2+u\\!\\int\\!\\phi^4,\\quad d_{\\rm eff}=d+z", "breaks": "Hertz–Millis fails in 2D metals and at Kondo-breakdown transitions, where the fermions cannot be integrated out and local quantum criticality or non-Fermi-liquid physics appears.", "confidence": "established", "strength": 3}
{"id": "C1497", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/critical-exponents-and-universality", "b": "08-condensed-matter/soft-matter/polymers", "name": "Self-avoiding polymers are the n→0 O(n) model", "kind": "identity", "summary": "De Gennes showed that self-avoiding-walk statistics are the $n\\to0$ limit of the $O(n)$ spin model, with $1/N$ playing the role of reduced temperature. A polymer's size exponent is therefore a critical exponent, computable by the $\\epsilon$ expansion and Monte Carlo ($\\nu\\approx0.588$ in 3D, exactly $3/4$ in 2D); Flory's mean-field $3/(d+2)$ is close but not exact.", "map": "R_g\\sim N^{\\nu},\\quad \\nu_{3D}\\approx0.588,\\ \\nu_{2D}=\\tfrac34,\\ \\nu_{\\rm F}=\\frac{3}{d+2};\\quad \\xi\\sim t^{-\\nu}\\leftrightarrow R\\sim N^{\\nu}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1498", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/critical-exponents-and-universality", "b": "08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals", "name": "Quantum critical scaling and ω/T collapse", "kind": "identity", "summary": "A zero-temperature transition has $\\xi\\sim|g-g_c|^{-\\nu}$ and $\\xi_\\tau\\sim\\xi^z$. Above it temperature is the only scale, so responses collapse onto functions of $\\hbar\\omega/k_BT$, and universality classes carry over from classical ones (the transverse-field Ising chain has 2D Ising exponents). Heavy-fermion metals such as CeCu$_{6-x}$Au$_x$ show $\\omega/T$ scaling with anomalous exponents that no known class reproduces.", "map": "\\xi\\sim|g-g_c|^{-\\nu},\\ \\xi_\\tau\\sim\\xi^{z},\\ \\chi''(\\omega,T)=T^{-\\alpha}\\Phi\\!\\left(\\frac{\\hbar\\omega}{k_BT}\\right)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1499", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/ising-model-and-lattice-models", "b": "08-condensed-matter/magnetism", "name": "Mermin–Wagner, anisotropy and order in 2D magnets", "kind": "mechanism", "summary": "The Mermin–Wagner theorem forbids order at $T>0$ in isotropic 2D Heisenberg magnets. Parent cuprates such as La₂CuO₄ therefore show only exponentially growing correlations, $\\xi\\propto e^{2\\pi\\rho_s/k_BT}$, and order through weak interlayer coupling. Ising anisotropy evades the theorem, giving Onsager-class transitions in Rb₂CoF₄ and long-range order in monolayer CrI₃.", "map": "\\xi_{\\rm 2D\\,Heis}\\propto e^{2\\pi\\rho_s/k_BT},\\quad k_BT_N\\sim J_\\perp(\\xi/a)^2,\\quad \\beta_{\\rm 2D\\,Ising}=\\tfrac18", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1500", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/ising-model-and-lattice-models", "b": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "name": "Lattice spin models as effective magnet Hamiltonians", "kind": "identity", "summary": "Exchange between local moments gives the Heisenberg Hamiltonian, and crystal-field or exchange anisotropy reduces it to the Ising or XY models of statistical mechanics, so real magnets are where those models are tested. Neutron and susceptibility data on FeF₂ (3D Ising) and Rb₂CoF₄ (2D Ising), among others, confirm the predicted universality classes.", "map": "H=-\\sum_{\\langle ij\\rangle}J_{ij}\\mathbf S_i\\cdot\\mathbf S_j-D\\sum_i(S_i^z)^2\\ \\xrightarrow{D\\gg J}\\ -J\\sum_{\\langle ij\\rangle}\\sigma_i\\sigma_j", "breaks": "Real moments are quantum: spin-1/2 fluctuations shrink the ordered moment and can destroy order. Dipolar, RKKY or longer-range couplings can also change the universality class.", "confidence": "established", "strength": 3}
{"id": "C1501", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/ising-model-and-lattice-models", "b": "08-condensed-matter/soft-matter/active-matter", "name": "Vicsek flocks: a moving XY model beating Mermin–Wagner", "kind": "analogy", "summary": "The Vicsek model is an XY ferromagnet whose spins are velocities that also move the particles, so alignment is coupled to density by self-advection. Toner and Tu showed that this coupling allows true long-range polar order in 2D, which Mermin–Wagner forbids for the equilibrium XY model.", "map": "\\theta_i(t+1)=\\langle\\theta_j\\rangle_{|\\mathbf r_{ij}|<R}+\\eta\\,\\xi_i,\\quad \\mathbf r_i(t+1)=\\mathbf r_i(t)+v_0\\hat{\\mathbf e}(\\theta_i)", "breaks": "There is no Hamiltonian or Boltzmann weight. The flocking transition is discontinuous, proceeding through travelling bands as a phase-separation scenario, rather than an XY critical point, and setting $v_0\\to0$ recovers the equilibrium XY model without long-range order.", "confidence": "established", "strength": 3}
{"id": "C1502", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory", "b": "08-condensed-matter/soft-matter/liquid-crystals", "name": "Landau–de Gennes theory of liquid crystals", "kind": "identity", "summary": "The nematic order parameter is a traceless symmetric tensor $Q_{ij}$, and because symmetry allows a $\\mathrm{tr}\\,Q^3$ term, Landau theory predicts a first-order isotropic–nematic transition (weakly first order in practice), with Maier–Saupe theory as its microscopic mean-field counterpart. De Gennes mapped the nematic–smectic-A transition, a complex density-wave order parameter coupled to director fluctuations, onto the Ginzburg–Landau theory of superconductors.", "map": "f=\\tfrac a2(T-T^*)\\,\\mathrm{tr}Q^2-\\tfrac b3\\,\\mathrm{tr}Q^3+\\tfrac c4(\\mathrm{tr}Q^2)^2,\\quad Q_{ij}=S(n_in_j-\\tfrac13\\delta_{ij})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1503", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "DMFT: Weiss mean field for quantum lattices", "kind": "method transfer", "summary": "Dynamical mean-field theory replaces a site's lattice environment by a self-consistent, frequency-dependent bath, the quantum analogue of the Weiss molecular field, and is exact in infinite dimensions with hopping scaled as $t\\propto1/\\sqrt d$. Because it keeps all local quantum fluctuations it captures the Mott metal–insulator transition that static mean field misses, and cluster extensions restore short-range spatial correlations.", "map": "h_{\\rm W}=zJ\\langle s\\rangle\\ \\leftrightarrow\\ \\mathcal G_0^{-1}(i\\omega_n)=i\\omega_n+\\mu-\\Delta(i\\omega_n),\\quad \\Sigma(\\mathbf k,\\omega)\\to\\Sigma(\\omega)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1504", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "BCS as mean field; Ginzburg–Landau as its Landau theory", "kind": "identity", "summary": "BCS theory is a self-consistent mean-field decoupling in the pair amplitude $\\Delta$. Gor'kov showed that near $T_c$ it reduces to Ginzburg–Landau theory, a Landau expansion in a complex order parameter minimally coupled to $\\mathbf A$. Because the Ginzburg number of clean low-$T_c$ metals scales as $(k_BT_c/E_F)^4$, the fluctuation region is too narrow to observe and mean-field exponents are effectively exact.", "map": "\\Delta=V\\sum_k\\frac{\\Delta}{2E_k}\\tanh\\frac{E_k}{2k_BT};\\ f=a|\\psi|^2+\\frac b2|\\psi|^4+\\frac{|(-i\\hbar\\nabla-2e\\mathbf A)\\psi|^2}{2m^*}", "breaks": "The order parameter is not gauge-invariant, and fluctuations of $\\mathbf A$ can make the transition weakly first order (Halperin–Lubensky–Ma). In short-coherence-length superconductors a real fluctuation window opens.", "confidence": "established", "strength": 3}
{"id": "C1505", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory", "b": "08-condensed-matter/superconductivity/cuprate-high-tc-superconductors", "name": "Where mean field fails: phase fluctuations in cuprates", "kind": "mechanism", "summary": "Short coherence lengths (1–2 nm), low superfluid density and quasi-2D layering raise the cuprates' Ginzburg number by many orders of magnitude over BCS metals, and YBCO shows 3D-XY critical behaviour near $T_c$. In underdoped samples $T_c$ tracks the superfluid stiffness (Uemura scaling), and a Nernst signal and diamagnetism persist above $T_c$, suggesting that phase fluctuations rather than gap closing set $T_c$ (Emery–Kivelson).", "map": "Gi\\propto\\Big(\\frac{k_BT_c}{\\Delta C\\,\\xi_0^3}\\Big)^2,\\quad k_BT_c\\lesssim\\rho_s(0)\\propto\\frac{n_s}{m^*}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1506", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/renormalization-group", "b": "08-condensed-matter/strongly-correlated-electrons/heavy-fermions-and-kondo-physics", "name": "Wilson's numerical RG solves the Kondo problem", "kind": "method transfer", "summary": "The antiferromagnetic Kondo coupling is marginally relevant: Anderson's poor-man's scaling makes it grow as the bandwidth is reduced, generating the scale $T_K$. Wilson's numerical renormalization group followed this flow nonperturbatively to the screened Fermi-liquid fixed point (Wilson ratio $R_W=2$), the RG's first nonperturbative success outside critical phenomena.", "map": "\\frac{dg}{d\\ln D}=-g^2,\\quad k_BT_K\\sim D\\,e^{-1/g},\\quad g=\\rho J", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1507", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/topological-phase-transitions-bkt", "b": "08-condensed-matter/low-dimensional-and-quantum-materials", "name": "Flat-band stiffness bounds T_BKT in moiré superconductors", "kind": "mechanism", "summary": "A 2D superconductor orders by BKT, so its $T_c$ is bounded by the superfluid stiffness. In magic-angle graphene's flat bands the conventional stiffness, proportional to bandwidth, is tiny, and a quantum-geometric term set by the band's quantum metric (bounded below by its Chern number) is proposed to supply it; recent kinetic-inductance measurements report stiffness consistent with that term.", "map": "k_BT_{\\rm BKT}=\\frac{\\pi}{2}D_s(T_{\\rm BKT}^-),\\quad D_s=D_s^{\\rm conv}+D_s^{\\rm geom},\\ D_s^{\\rm geom}\\propto\\int g_{\\mu\\nu}(\\mathbf k)\\,d^2k", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1508", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/topological-phase-transitions-bkt", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "name": "Mermin–Wagner and BKT physics in atomically thin crystals", "kind": "shared object", "summary": "Two-dimensional superconductors (ion-gated MoS₂, few-layer NbSe₂, oxide interfaces) are analysed as vortex-unbinding transitions, using $V\\propto I^3$ at $T_{\\rm BKT}$ and the universal stiffness jump. In van der Waals magnets, easy-plane anisotropy gives 2D-XY behaviour, while Ising anisotropy (monolayer CrI₃) allows true long-range order despite Mermin–Wagner.", "map": "V\\propto I^{a(T)},\\ a(T_{\\rm BKT})=3;\\quad \\rho_s(T_{\\rm BKT}^-)=\\tfrac{2}{\\pi}k_BT_{\\rm BKT}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1509", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/topological-phase-transitions-bkt", "b": "08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order", "name": "Two meanings of 'topological' order", "kind": "analogy", "summary": "Both go beyond Landau's local order parameter. The BKT transition is the unbinding of vortices, defects classified by $\\pi_1(S^1)=\\mathbb Z$; topological order instead labels gapped $T=0$ phases by ground-state degeneracy and anyons. In both, proliferating point excitations destroy the ordered phase: free vortices above $T_{\\rm BKT}$, and thermally excited anyons in a 2D toric code at any $T>0$.", "map": "F_{\\rm v}=(\\pi J-2k_BT)\\ln\\frac{L}{a}\\quad\\text{vs}\\quad \\mathrm{GSD}_{\\rm torus}=4\\ (\\mathbb Z_2)", "breaks": "The BKT phase is gapless with quasi-long-range order and has neither topological degeneracy nor long-range entanglement. Topological order is a gapped quantum phase that in 2D does not survive any nonzero temperature. 'Topological' refers to real-space defects in one case and to global ground-state structure in the other.", "confidence": "established", "strength": 1}
{"id": "C1766", "a": "04-quantum-physics/atomic-molecular-and-optical-physics", "b": "08-condensed-matter/strongly-correlated-electrons/hubbard-model-and-mott-physics", "name": "Cold atoms as analog Hubbard simulators", "kind": "method transfer", "summary": "Ultracold atoms in optical lattices realize Bose- and Fermi-Hubbard models with tunable U/t, giving clean, disorder-free access to Mott physics and magnetism that motivate condensed-matter questions.", "map": "H=-t\\sum c^\\dagger_{i\\sigma}c_{j\\sigma}+U\\sum n_{i\\uparrow}n_{i\\downarrow}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1767", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "08-condensed-matter/crystals-and-electronic-structure/density-functional-theory", "name": "From Hartree-Fock atoms to density functionals", "kind": "historical", "summary": "Self-consistent-field methods for atoms (Hartree-Fock, Thomas-Fermi, Slater's exchange approximation) led directly to density functional theory for solids.", "map": "v_x^{\\rm Slater}\\propto-n^{1/3}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1768", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/transition-metal-dichalcogenides-and-excitons", "name": "Exciton and polariton condensation", "kind": "mechanism", "summary": "Excitons and exciton-polaritons are composite bosons that condense at high temperature because of their light mass; interlayer TMD excitons are candidate equilibrium exciton condensates.", "map": "k_BT_c\\propto\\frac{\\hbar^2n^{2/3}}{m^*},\\ m^*_{\\rm pol}\\sim10^{-4}m_e", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1769", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "08-condensed-matter/magnetism/spintronics", "name": "Synthetic spin-orbit coupling in quantum gases", "kind": "analogy", "summary": "Raman dressing gives atoms Rashba/Dresselhaus-like spin-orbit coupling, emulating spintronic Hamiltonians in clean, tunable neutral gases.", "map": "H=\\frac{(\\mathbf p-\\hbar k_R\\sigma_z\\hat x)^2}{2m}+\\frac\\Omega2\\sigma_x", "breaks": "Neutral atoms carry no charge current; synthetic SOC comes with heating from spontaneous emission.", "confidence": "established", "strength": 2}
{"id": "C1770", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "BEC-BCS crossover connects pairs and condensates", "kind": "mechanism", "summary": "Feshbach-tuned Fermi gases cross continuously from BCS Cooper pairing to a BEC of tightly bound molecules; the same gap and number equations describe superconductors at weak coupling.", "map": "\\frac{1}{k_Fa}:-\\infty\\ (\\mathrm{BCS})\\to0\\ (\\mathrm{unitary})\\to+\\infty\\ (\\mathrm{BEC});\\ E_k=\\sqrt{\\xi_k^2+\\Delta^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1771", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "08-condensed-matter/superconductivity/cuprate-high-tc-superconductors", "name": "Preformed pairs and the BEC-BCS crossover", "kind": "analogy", "summary": "Short coherence lengths in cuprates place them between BCS and BEC limits; the pseudogap has been compared to preformed pairs above T_c in the cold-atom crossover.", "map": "", "breaks": "Cuprate pairing is d-wave in a doped Mott insulator with competing orders; the cold-atom crossover is s-wave in a clean continuum gas.", "confidence": "current research", "strength": 2}
{"id": "C1772", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "b": "08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons", "name": "Bloch bands in optical lattices", "kind": "identity", "summary": "Atoms in optical lattices obey Bloch's theorem with tight-binding bands and Wannier functions; Bloch oscillations, unobservable in solids because of scattering, are seen directly.", "map": "\\hbar\\dot{\\mathbf k}=\\mathbf F;\\ \\omega_B=Fa/\\hbar", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1773", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/moire-materials-and-twisted-bilayers", "name": "Moire materials as solid-state quantum simulators", "kind": "analogy", "summary": "Twisted bilayers realize tunable lattice models (triangular Hubbard, flat Chern bands) by twist angle and gating, playing the role optical lattices play for atoms.", "map": "", "breaks": "Moire electrons have long-range Coulomb interactions, phonons and disorder; filling and interactions are tuned differently from cold atoms.", "confidence": "current research", "strength": 2}
{"id": "C1774", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "b": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "name": "Superexchange observed with cold atoms", "kind": "mechanism", "summary": "In optical double wells, second-order tunnelling produces superexchange J=4t^2/U between spins, measured in real time.", "map": "J_{\\rm ex}=4t^2/U", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1775", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "b": "08-condensed-matter/strongly-correlated-electrons", "name": "Quantum simulation of correlated-electron problems", "kind": "method transfer", "summary": "Strongly correlated electron problems (doped Hubbard, pseudogap, stripes) that resist numerics are posed to cold-atom simulators, whose measurements now benchmark DMFT, DMRG and QMC.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1776", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "b": "08-condensed-matter/strongly-correlated-electrons/hubbard-model-and-mott-physics", "name": "Superfluid-Mott transition in optical lattices", "kind": "identity", "summary": "Deep optical lattices map exactly onto the Bose-Hubbard model; tuning lattice depth drove the superfluid-Mott insulator quantum phase transition, and quantum gas microscopes now image Hubbard correlations site by site.", "map": "H_{BH}=-J\\sum b_i^\\dagger b_j+\\tfrac U2\\sum n_i(n_i-1);\\ (U/J)_c\\approx29\\ (3D)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1777", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "b": "08-condensed-matter/superconductivity/cuprate-high-tc-superconductors", "name": "Fermi-Hubbard simulators target cuprate physics", "kind": "method transfer", "summary": "Quantum gas microscopes observed long-range antiferromagnetism and then hole-doped correlations in the 2D Fermi-Hubbard model, addressing the doped-Mott-insulator physics of cuprates.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1778", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "b": "08-condensed-matter/topological-matter/quantum-hall-effects", "name": "Chern bands and Hofstadter models with cold atoms", "kind": "method transfer", "summary": "Shaken and laser-assisted-tunnelling optical lattices realized the Haldane and Harper-Hofstadter models, measuring Chern numbers of synthetic quantum-Hall bands.", "map": "H=-J\\sum e^{i2\\pi\\alpha m}a^\\dagger_{m+1,n}a_{m,n}+\\text{h.c.}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1779", "a": "04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures", "name": "Nuclear-spin bath decoherence of dot spins", "kind": "mechanism", "summary": "In GaAs dots the electron spin decoheres through hyperfine coupling to ~1e6 nuclear spins, a central-spin model of system-bath decoherence that drove the move to isotopically purified Si.", "map": "H=g\\mu_BBS_z+\\sum_kA_k\\mathbf S\\cdot\\mathbf I_k", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1780", "a": "04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "Macroscopic quantum tunnelling in Josephson junctions", "kind": "historical", "summary": "Caldeira and Leggett's theory of dissipative tunnelling and the 1985 observation of quantized levels in a current-biased junction showed a macroscopic phase variable obeys quantum mechanics (Nobel 2025).", "map": "\\Gamma\\propto e^{-7.2\\Delta U/\\hbar\\omega_p}\\ (\\text{weak damping})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1781", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/floquet-systems-and-time-crystals", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "name": "Light-induced anomalous Hall effect in graphene", "kind": "method transfer", "summary": "Circularly polarized light opens a Floquet gap at graphene's Dirac points; an anomalous Hall response was measured in ultrafast transport.", "map": "\\Delta_F\\approx\\frac{(ev_FE_0)^2}{\\hbar\\omega^3}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1782", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/floquet-systems-and-time-crystals", "b": "08-condensed-matter/topological-matter/topological-insulators", "name": "Floquet topological insulators", "kind": "method transfer", "summary": "Periodic driving (circularly polarized light) opens topological gaps in trivial bands; Floquet bands carry Chern and anomalous winding invariants beyond static classification.", "map": "H_{\\rm eff}\\approx\\bar H+\\frac{[H_{-1},H_{1}]}{\\hbar\\omega}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1783", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/non-hermitian-physics", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "Non-Hermitian band topology", "kind": "method transfer", "summary": "Gain and loss extend band topology to point and line gaps; spectral winding gives the skin effect and modifies bulk-boundary correspondence, enlarging the tenfold classification.", "map": "w=\\oint\\frac{dk}{2\\pi i}\\partial_k\\ln\\det[H(k)-E_0]", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1784", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/non-hermitian-physics", "b": "08-condensed-matter/topological-matter/topological-semimetals", "name": "Bulk Fermi arcs from exceptional points", "kind": "mechanism", "summary": "Finite quasiparticle lifetimes make the effective Hamiltonian non-Hermitian; Weyl or Dirac nodes split into exceptional rings joined by bulk Fermi arcs.", "map": "H_{\\rm eff}=H_0+\\Sigma(\\omega=0),\\ \\mathrm{Im}\\Sigma\\neq0", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1785", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling", "b": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "name": "Random-matrix theory of quantum transport", "kind": "method transfer", "summary": "Universal conductance fluctuations and weak localization in chaotic cavities follow random-matrix statistics of transmission eigenvalues, the quantum-chaos framework applied to transport.", "map": "\\mathrm{var}\\,G\\sim(e^2/h)^2,\\ \\text{independent of size}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1786", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling", "b": "08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals", "name": "Planckian dissipation and the chaos bound", "kind": "mechanism", "summary": "Strange metals relax at the Planckian rate hbar/tau ~ k_BT, the same scale as the quantum chaos bound; SYK-type models realize both maximal chaos and linear-in-T resistivity.", "map": "\\frac{\\hbar}{\\tau}\\approx\\alpha k_BT\\ \\leftrightarrow\\ \\lambda_L\\le\\frac{2\\pi k_BT}{\\hbar}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1787", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-thermodynamics", "b": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "name": "Quantum of thermal conductance", "kind": "mechanism", "summary": "A single ballistic channel carries at most one heat quantum; mesoscopic conductors serve as quantum heat engines and refrigerators analysed with Landauer heat currents.", "map": "G_Q=\\frac{\\pi^2k_B^2T}{3h}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1788", "a": "04-quantum-physics/quantum-information-and-computation", "b": "08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order", "name": "Topological quantum computation with anyons", "kind": "method transfer", "summary": "Braiding non-Abelian anyons of a topologically ordered phase implements gates protected by topology, turning a condensed-matter phase into a quantum computer architecture.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1789", "a": "04-quantum-physics/quantum-information-and-computation", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "Josephson junction as the nonlinear qubit element", "kind": "shared object", "summary": "The dissipationless nonlinear inductance of a Josephson junction is what makes superconducting circuits anharmonic and hence usable as qubits.", "map": "I=I_c\\sin\\varphi,\\ L_J=\\frac{\\Phi_0}{2\\pi I_c\\cos\\varphi}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1790", "a": "04-quantum-physics/quantum-information-and-computation", "b": "08-condensed-matter/topological-matter/quantum-hall-effects", "name": "Non-Abelian anyons in fractional quantum Hall states", "kind": "method transfer", "summary": "The nu=5/2 state is a candidate Moore-Read phase with Ising anyons; interferometry and braiding there are a proposed route to topological qubits.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1791", "a": "04-quantum-physics/quantum-information-and-computation", "b": "08-condensed-matter/topological-matter/topological-superconductors-and-majoranas", "name": "Majorana zero modes as topological qubits", "kind": "method transfer", "summary": "Majorana zero modes at Kitaev-chain ends store a qubit in nonlocal fermion parity; braiding gives protected Clifford gates. Experimental claims in nanowires remain contested.", "map": "H_K=\\sum[-\\mu c_j^\\dagger c_j-t(c_j^\\dagger c_{j+1}+\\text{h.c.})+\\Delta(c_jc_{j+1}+\\text{h.c.})]", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1792", "a": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "b": "08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order", "name": "Topological entanglement entropy", "kind": "identity", "summary": "Topological order leaves a universal negative constant in the entanglement entropy area law, set by the total quantum dimension of the anyons.", "map": "S_A=\\alpha L-\\gamma,\\ \\gamma=\\ln\\mathcal D", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1793", "a": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "Area laws make DMRG and tensor networks work", "kind": "method transfer", "summary": "Gapped ground states obey entanglement area laws, so matrix-product states with bounded bond dimension represent them faithfully; DMRG is variational optimization over MPS.", "map": "S\\le\\log\\chi;\\ S(\\ell)\\le\\text{const}\\ (1\\mathrm{D\\ gapped})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1794", "a": "04-quantum-physics/quantum-information-and-computation/photonic-and-spin-qubits", "b": "08-condensed-matter/crystals-and-electronic-structure/semiconductors", "name": "Donor and Si/SiGe spin qubits", "kind": "shared object", "summary": "Silicon spin qubits rely on semiconductor physics: donor levels, valley splitting, isotopic purification of Si-28 and CMOS fabrication.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1795", "a": "04-quantum-physics/quantum-information-and-computation/photonic-and-spin-qubits", "b": "08-condensed-matter/low-dimensional-and-quantum-materials", "name": "2D materials as hosts for spin and valley qubits", "kind": "shared object", "summary": "Graphene and TMD quantum dots offer weak hyperfine coupling and valley degrees of freedom as alternative qubit hosts.", "map": "", "breaks": "", "confidence": "current research", "strength": 1}
{"id": "C1796", "a": "04-quantum-physics/quantum-information-and-computation/photonic-and-spin-qubits", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "name": "NV magnetometry images electron hydrodynamics", "kind": "method transfer", "summary": "Nitrogen-vacancy centres used as nanoscale quantum magnetometers imaged the Poiseuille flow profile of the Dirac fluid in graphene.", "map": "\\delta B\\sim\\frac{\\hbar}{g\\mu_B\\sqrt{T_2t}}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1797", "a": "04-quantum-physics/quantum-information-and-computation/photonic-and-spin-qubits", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures", "name": "Gate-defined quantum-dot spin qubits", "kind": "shared object", "summary": "Single electrons confined in gate-defined quantum dots carry spin qubits controlled by exchange (Loss-DiVincenzo); Coulomb blockade and charge sensing come from mesoscopic quantum-dot physics.", "map": "H=g\\mu_B\\mathbf B\\cdot\\mathbf S+J(t)\\mathbf S_1\\cdot\\mathbf S_2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1798", "a": "04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "Quantum algorithms for correlated materials", "kind": "method transfer", "summary": "Phase estimation, VQE and Hamiltonian simulation target ground states and dynamics of Hubbard-type models that classical numerics cannot reach, the leading candidate for quantum advantage.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1799", "a": "04-quantum-physics/quantum-information-and-computation/quantum-error-correction-and-fault-tolerance", "b": "08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order", "name": "Toric code is a topologically ordered phase", "kind": "identity", "summary": "The surface/toric code Hamiltonian is a Z2 topologically ordered phase: logical operators are anyon loops, code distance is system size, and the threshold maps to a disorder phase transition of a random-bond Ising model.", "map": "H=-\\sum_vA_v-\\sum_pB_p;\\ \\text{GSD}=4\\ \\text{on torus}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1800", "a": "04-quantum-physics/quantum-information-and-computation/superconducting-qubits", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "Phonons as qubit resource and error source", "kind": "mechanism", "summary": "Qubits couple coherently to bulk and surface-acoustic phonon modes (quantum acoustodynamics), while phonon bursts from cosmic rays break Cooper pairs and cause chip-wide correlated errors.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1801", "a": "04-quantum-physics/quantum-information-and-computation/superconducting-qubits", "b": "08-condensed-matter/superconductivity", "name": "Superconductors as the material base of qubits", "kind": "shared object", "summary": "Superconducting qubits inherit BCS physics: the gap protects against dissipation, while quasiparticles, two-level defects and surface oxides of Nb/Al/Ta set coherence.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1802", "a": "04-quantum-physics/quantum-information-and-computation/superconducting-qubits", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Quasiparticles limit qubit coherence", "kind": "mechanism", "summary": "Non-equilibrium Bogoliubov quasiparticles above the BCS gap tunnel across junctions and cause relaxation and parity switching; gap engineering and phonon traps suppress them.", "map": "\\Gamma_1^{qp}\\propto x_{qp}\\sqrt{\\frac{2\\Delta}{\\hbar\\omega_q}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1803", "a": "04-quantum-physics/quantum-information-and-computation/superconducting-qubits", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "Transmon Hamiltonian from Josephson physics", "kind": "identity", "summary": "A capacitively shunted Josephson junction is a quantum pendulum; at E_J/E_C ~ 50 the charge dispersion is exponentially suppressed, giving the transmon qubit.", "map": "H=4E_C(\\hat n-n_g)^2-E_J\\cos\\hat\\varphi,\\ \\omega_{01}\\approx\\sqrt{8E_JE_C}-E_C", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1804", "a": "04-quantum-physics/quantum-information-and-computation/trapped-ion-and-neutral-atom-qubits", "b": "08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids", "name": "Rydberg arrays realize a Z2 spin liquid", "kind": "method transfer", "summary": "Rydberg-blockade atom arrays on a ruby lattice prepared a state with topological string order of a Z2 quantum spin liquid, a phase long sought in frustrated magnets.", "map": "H=\\frac\\Omega2\\sum\\sigma^x_i-\\Delta\\sum n_i+\\sum V_{ij}n_in_j", "breaks": "", "confidence": "current research", "strength": 3}