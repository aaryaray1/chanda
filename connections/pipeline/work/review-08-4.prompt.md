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

### Hydride superconductors under pressure · `knowledge/08-condensed-matter/superconductivity/hydride-superconductors-under-pressure`

**Scope.** Ashcroft's metallic-hydrogen idea, chemical precompression, DFT/Eliashberg predictions, H₃S at 203 K (~150 GPa), LaH₁₀ at ~250 K (~170 GPa), diamond-anvil-cell techniques, magnetic measurements under pressure, the retracted carbonaceous sulfur hydride and Lu–N–H claims, ternary hydrides aiming for lower pressure.

**Core ideas.**
- Light hydrogen gives high phonon frequencies and strong coupling — conventional BCS physics pushed to extremes.
- Theory successfully predicted several hydride structures and $T_c$ values before experiment.
- Measurements in tiny pressurized samples are hard; independent replication is essential.

**Key equations.**
$$T_c=\frac{\omega_{\log}}{1.2}\exp\!\left[-\frac{1.04(1+\lambda)}{\lambda-\mu^*(1+0.62\lambda)}\right]\ (\text{Allen–Dynes})$$

**Landmark.** Drozdov et al. (2015) — see [subfield landmarks](knowledge/08-condensed-matter/superconductivity/README.md).

**See also.** [Density functional theory](knowledge/08-condensed-matter/crystals-and-electronic-structure/density-functional-theory/README.md) · [Phonons](knowledge/08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics/README.md)

### Iron-based and nickelate superconductors · `knowledge/08-condensed-matter/superconductivity/iron-based-and-nickelate-superconductors`

**Scope.** LaFeAsO family (2008), 122 and 11 (FeSe) compounds, nematicity, spin-density waves, s± pairing via interpocket spin fluctuations, monolayer FeSe/SrTiO₃, infinite-layer Nd₁₋ₓSrₓNiO₂ films (2019), La₃Ni₂O₇ under pressure (~80 K, 2023), ambient-pressure nickelate thin films, comparison with cuprates.

**Core ideas.**
- Iron superconductors are multi-orbital metals, not Mott insulators — a different route to high $T_c$.
- Sign-changing s± gap between hole and electron pockets is favoured by spin fluctuations.
- Nickelates test whether cuprate-like electronic structure alone suffices for high $T_c$.

**Key equations.**
$$\Delta_h=-\Delta_e\ (s^\pm),\qquad \mathbf Q=(\pi,0)\ \text{nesting vector}$$

**See also.** [Cuprates](knowledge/08-condensed-matter/superconductivity/cuprate-high-tc-superconductors/README.md)

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

# Packet 08-4 (100 records)

{"id": "C2465", "a": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Neutron-star superfluids and superconducting protons", "kind": "mechanism", "summary": "The same gap equation predicts 1S0 neutron superfluidity in the crust, 3P2 neutron pairing and type-II proton superconductivity with flux tubes in the core; these set neutron-star cooling (pair-breaking neutrino emission), specific heat and rotational dynamics. Dilute neutron matter is close to the unitary Fermi gas.", "map": "k_BT_c\\approx0.57\\Delta_0;\\ \\Delta_{nn}^{1S0}\\sim1\\text{–}3\\ \\text{MeV};\\ \\kappa_p=\\lambda_p/\\xi_p>1/\\sqrt2\\Rightarrow\\text{type II}", "breaks": "Gaps are not measured directly and depend strongly on medium polarization and three-nucleon forces; the protons sit in a neutron superfluid with entrainment, a coupling absent in metals.", "confidence": "established", "strength": 3}
{"id": "C2466", "a": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Pulsar glitches as vortex pinning and creep", "kind": "mechanism", "summary": "Glitches are explained by quantized neutron-superfluid vortices pinned to crust nuclei that unpin collectively, and post-glitch relaxation by thermally activated vortex creep: the Anderson-Kim flux-creep physics of type-II superconductors, carried to neutron stars by Anderson himself.", "map": "\\oint\\mathbf v_s\\cdot d\\mathbf l=\\frac{h}{2m_n}\\leftrightarrow\\Phi_0=\\frac{h}{2e};\\ v_{\\rm creep}\\propto e^{-E_p/k_BT}", "breaks": "Neutron vortices are neutral (no flux, no Lorentz force); pinning energies and whether the crustal superfluid can store enough angular momentum (the entrainment problem) are disputed.", "confidence": "current research", "strength": 2}
{"id": "C2467", "a": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "b": "08-condensed-matter/topological-matter/topological-superconductors-and-majoranas", "name": "3P2 neutron superfluid as triplet p-wave pairing", "kind": "analogy", "summary": "Spin-triplet 3P2 neutron pairing in neutron-star cores has an anisotropic, multicomponent order parameter like superfluid 3He and the p-wave pairing behind topological superconductors, which raises the question of protected surface modes and half-quantum vortices in neutron stars.", "map": "", "breaks": "The 3P2 channel is driven by the tensor and spin-orbit forces with L=1, S=1, J=2 rather than pure p-wave; the gap is uncertain by an order of magnitude and no observable topological signature has been identified.", "confidence": "proposed", "strength": 1}
{"id": "C2468", "a": "07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions", "b": "08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons", "name": "Positron annihilation maps Fermi surfaces and vacancies", "kind": "method transfer", "summary": "Positrons from beta-plus sources (22Na) thermalize in solids and annihilate with electrons; the angular correlation and Doppler broadening of the 511 keV gammas map the electron momentum density (Fermi surfaces), and positron lifetimes identify vacancies.", "map": "\\rho(\\mathbf p)=\\sum_j\\left|\\int e^{-i\\mathbf p\\cdot\\mathbf r}\\psi_+(\\mathbf r)\\psi_j(\\mathbf r)\\,d\\mathbf r\\right|^2;\\ \\Delta\\theta\\approx p_\\perp/m_ec", "breaks": "The positron wavefunction and electron-positron correlations weight the signal non-uniformly, so momentum densities need theory corrections.", "confidence": "established", "strength": 2}
{"id": "C2469", "a": "07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "Cryogenic phonon calorimeters for double-beta and endpoints", "kind": "method transfer", "summary": "0vbb searches (CUORE TeO2 crystals) and electron-capture endpoint measurements use millikelvin calorimeters in which the decay energy becomes phonons; the T^3 Debye heat capacity makes the temperature rise measurable with thermistors or transition-edge sensors.", "map": "\\Delta T=\\frac{E}{C(T)},\\ C\\propto\\left(\\frac{T}{\\Theta_D}\\right)^3;\\ \\Delta E_{\\rm rms}\\approx\\sqrt{k_BT^2C}", "breaks": "Detector physics adds athermal phonon transport and superconducting-sensor physics beyond equilibrium lattice dynamics.", "confidence": "established", "strength": 2}
{"id": "C2470", "a": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-fission", "b": "08-condensed-matter/crystals-and-electronic-structure/density-functional-theory", "name": "Time-dependent DFT of fission and electron dynamics", "kind": "method transfer", "summary": "Microscopic fission dynamics (scission, fragment excitation, neutron emission) is computed with time-dependent superfluid DFT, the nuclear version of the Runge-Gross TDDFT used for electronic excitations and dynamics in materials.", "map": "i\\hbar\\partial_t\\phi_i=h[\\rho(t)]\\phi_i;\\ \\text{TDHFB: }i\\hbar\\partial_t(U,V)=\\mathcal H[\\rho,\\kappa](U,V)", "breaks": "Nuclear TDDFT lacks quantum fluctuations of the collective coordinates (no spontaneous tunnelling) and uses fitted functionals; electronic TDDFT has an external field and adiabatic xc approximations.", "confidence": "current research", "strength": 2}
{"id": "C2471", "a": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-fission", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "Collective tunnelling: fission and Josephson junctions", "kind": "analogy", "summary": "Spontaneous fission and sub-barrier fusion are tunnelling of a collective coordinate coupled to many intrinsic degrees of freedom, the same dissipative macroscopic-tunnelling problem as the phase of a current-biased Josephson junction (Caldeira-Leggett).", "map": "\\Gamma\\propto\\exp\\!\\left[-\\frac2\\hbar\\int\\!\\sqrt{2M(q)(V(q)-E)}\\,dq\\right]\\leftrightarrow\\Gamma\\propto e^{-S_E[\\varphi]/\\hbar}", "breaks": "The nuclear collective inertia M(q) and the barrier come from the same nucleons with level crossings, not an ohmic bath; the coupling is non-Markovian and few-channel.", "confidence": "established", "strength": 2}
{"id": "C2472", "a": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "b": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "name": "Ion channeling, RBS and crystal-blocking lifetimes", "kind": "method transfer", "summary": "Nuclear backscattering and channeling of MeV ions locate impurities and defects in crystals; conversely, crystal blocking of reaction products measures compound-nucleus and fission lifetimes down to ~1e-18 s from the recoil distance travelled before decay.", "map": "\\psi_c\\approx\\sqrt{\\frac{2Z_1Z_2e^2}{Ed}}\\ \\text{(Lindhard critical angle)};\\ \\tau\\sim\\Delta r_\\perp/v_\\perp", "breaks": "Channeling is classical ion optics in a lattice; it gives timing only when recoil displacements are comparable with the Thomas-Fermi screening length.", "confidence": "established", "strength": 2}
{"id": "C2473", "a": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "b": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "name": "Neutron scattering as the probe of structure and magnetism", "kind": "method transfer", "summary": "The nuclear neutron-scattering length (Fermi pseudopotential) and the neutron magnetic moment make reactor and spallation neutrons the standard probe of crystal structure, magnetic order and phonon and magnon dispersions; antiferromagnetic order was first seen this way.", "map": "V(\\mathbf r)=\\frac{2\\pi\\hbar^2}{m_n}b\\,\\delta(\\mathbf r);\\ \\frac{d\\sigma}{d\\Omega}=\\left|\\sum_jb_je^{i\\mathbf Q\\cdot\\mathbf r_j}\\right|^2", "breaks": "b is an empirical nuclear quantity that varies erratically between isotopes (hence isotopic contrast variation), unlike X-ray form factors that scale with Z.", "confidence": "established", "strength": 3}
{"id": "C2474", "a": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "b": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "name": "Random-matrix statistics: compound nuclei and chaotic dots", "kind": "method transfer", "summary": "Random-matrix theory was born for neutron resonances (Wigner, Porter-Thomas), and its reaction-theory machinery (Mahaux-Weidenmüller S-matrix, Ericson fluctuations) became the theory of transport through chaotic quantum dots: conductance fluctuations and the Landauer conductance as S-matrix statistics.", "map": "S=1-2\\pi iW^\\dagger(E-H+i\\pi WW^\\dagger)^{-1}W,\\ H\\in\\text{GOE};\\ G=\\frac{2e^2}{h}\\mathrm{Tr}\\,t^\\dagger t", "breaks": "Nuclear widths probe energy-averaged cross sections of a self-bound system; dot transport adds magnetic-field symmetry classes (GUE), dephasing and Coulomb blockade.", "confidence": "established", "strength": 3}
{"id": "C2475", "a": "07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay", "b": "08-condensed-matter/crystals-and-electronic-structure", "name": "Thorium-229 nuclear clock in wide-gap crystals", "kind": "shared object", "summary": "The 8.4 eV isomer of 229Th has been laser-excited in a CaF2 host: the crystal needs a band gap above the transition to suppress internal conversion, and crystal-field and electric-field-gradient effects split and shift the nuclear line.", "map": "E_{\\rm iso}\\approx8.36\\ \\text{eV}<E_g(\\mathrm{CaF_2})\\approx12\\ \\text{eV};\\ \\Delta E_Q\\propto eQV_{zz}", "breaks": "The crystal is an environment, not part of the transition; defects, radiation damage and temperature-dependent shifts limit clock performance.", "confidence": "current research", "strength": 2}
{"id": "C2476", "a": "07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "Mössbauer effect: recoil-free gamma emission from a lattice", "kind": "mechanism", "summary": "Nuclear gamma rays are emitted and absorbed without recoil because the whole lattice takes the momentum; the recoil-free fraction is the phonon Debye-Waller factor, and Mössbauer spectroscopy reads hyperfine fields, isomer shifts and phonon densities of states in solids.", "map": "f=e^{-k^2\\langle x^2\\rangle};\\ \\text{Debye, }T\\to0:\\ f=\\exp\\!\\left(-\\frac{3E_R}{2k_B\\Theta_D}\\right),\\ E_R=\\frac{E_\\gamma^2}{2Mc^2}", "breaks": "Only low-energy, long-lived gamma transitions (57Fe at 14.4 keV) work, and the nuclear linewidth, not phonon physics, sets the resolution.", "confidence": "established", "strength": 3}
{"id": "C2477", "a": "07-nuclear-physics/nuclear-structure/ab-initio-nuclear-theory", "b": "08-condensed-matter/crystals-and-electronic-structure/density-functional-theory", "name": "Homogeneous-matter QMC as functional input", "kind": "method transfer", "summary": "Electronic DFT rests on the QMC energy of the uniform electron gas (LDA); nuclear functionals are anchored the same way to ab initio neutron-matter equations of state, which fix the isovector part of Skyrme EDFs and their neutron-skin and radius predictions.", "map": "E_{xc}^{\\rm LDA}=\\int n\\,\\epsilon_{xc}^{\\rm HEG}(n)\\,d^3r\\ \\leftrightarrow\\ E_{\\rm EDF}\\ \\text{fitted to}\\ E_{\\rm PNM}(n)/N", "breaks": "The electron gas is Coulombic and the LDA is a controlled local limit; neutron matter has spin-isospin-dependent and three-body forces with theory uncertainties, and the map to finite nuclei is a fit, not an exact limit.", "confidence": "established", "strength": 2}
{"id": "C2478", "a": "07-nuclear-physics/nuclear-structure/ab-initio-nuclear-theory", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "SRG/IMSRG and Wegner flow equations", "kind": "method transfer", "summary": "The similarity renormalization group that softens nuclear forces and the in-medium SRG that decouples nuclear ground states are the continuous unitary flow equations introduced by Wegner and by Glazek and Wilson, which are also used for impurity and lattice models in condensed matter.", "map": "\\frac{dH_s}{ds}=[\\eta_s,H_s],\\ \\eta_s=[H_d,H_s]\\ \\text{(Wegner generator)}", "breaks": "Nuclear SRG must track the induced three- and higher-body forces of a vacuum interaction; CM flows usually start from a fixed lattice Hamiltonian and track induced couplings differently.", "confidence": "established", "strength": 2}
{"id": "C2479", "a": "07-nuclear-physics/nuclear-structure/ab-initio-nuclear-theory", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "Shared quantum Monte Carlo toolkit and sign problem", "kind": "method transfer", "summary": "GFMC/AFDMC and nuclear lattice EFT (auxiliary-field Monte Carlo after a Hubbard-Stratonovich transformation) are the projector and determinant QMC used for Hubbard models; approximate SU(4) Wigner symmetry suppresses the nuclear sign problem as particle-hole symmetry does at half filling, and neural-network states now enter both.", "map": "e^{-\\tau\\frac C2\\rho^2}\\propto\\int ds\\,e^{-\\frac{s^2}{2C\\tau}}e^{-\\tau s\\rho}\\ \\Rightarrow\\ Z=\\int\\mathcal Ds\\,\\det M[s]", "breaks": "Nuclear Hamiltonians have strong spin-isospin and three-body operators that cannot be written as one-body densities, which forces constrained-path approximations; CM lattice models have a simple on-site U.", "confidence": "established", "strength": 3}
{"id": "C2480", "a": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "b": "08-condensed-matter/crystals-and-electronic-structure/density-functional-theory", "name": "Nuclear energy density functionals as Kohn-Sham DFT", "kind": "method transfer", "summary": "Skyrme, Gogny and relativistic mean-field calculations are self-consistent Kohn-Sham-like schemes: nucleon orbitals in a potential that is the functional derivative of an energy density functional fitted to data, extended to pairing through HFB (compare DFT for superconductors).", "map": "h=\\frac{\\delta E[\\rho,\\tau,\\mathbf J,\\tilde\\rho]}{\\delta\\rho},\\ h\\phi_i=\\varepsilon_i\\phi_i\\ \\leftrightarrow\\ v_{\\rm xc}=\\frac{\\delta E_{\\rm xc}[n]}{\\delta n}", "breaks": "Nuclei are self-bound with no external potential, so Hohenberg-Kohn applies only to intrinsic densities; nuclear EDFs break and then restore symmetries and are fitted phenomenologically rather than derived from a known exact functional.", "confidence": "established", "strength": 3}
{"id": "C2481", "a": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "Particle-vibration coupling vs electron-phonon coupling", "kind": "analogy", "summary": "Bohr-Mottelson nuclear field theory couples single nucleons to quantized surface 'phonons' just as electrons couple to lattice phonons; the coupling dresses quasiparticles, fragments strength and adds an induced pairing interaction akin to phonon-mediated BCS glue.", "map": "H_{pv}=\\sum_{\\lambda\\mu}\\kappa_\\lambda k(r)Y^*_{\\lambda\\mu}(\\hat r)(b^\\dagger_{\\lambda\\mu}+b_{\\lambda\\mu})\\leftrightarrow\\sum g_{\\mathbf q}(b^\\dagger_{\\mathbf q}+b_{-\\mathbf q})c^\\dagger c", "breaks": "Nuclear phonons are a few discrete collective modes of the same nucleons: no separate lattice, no Debye cutoff and no Migdal small parameter omega/E_F.", "confidence": "established", "strength": 2}
{"id": "C2482", "a": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures", "name": "Giant dipole resonance and cluster surface plasmon", "kind": "analogy", "summary": "The nuclear giant dipole resonance (protons oscillating against neutrons) and the Mie surface plasmon of metal clusters are both collective dipole modes that exhaust the Thomas-Reiche-Kuhn sum rule, treated with the same RPA and Goldhaber-Teller/Steinwedel-Jensen pictures.", "map": "\\int\\sigma\\,dE=\\frac{2\\pi^2e^2\\hbar}{mc}\\frac{NZ}{A}\\leftrightarrow\\frac{2\\pi^2e^2\\hbar}{m_ec}N_e;\\ E_{\\rm GDR}\\approx80A^{-1/3}\\,\\text{MeV},\\ \\omega_{\\rm Mie}=\\frac{\\omega_p}{\\sqrt3}", "breaks": "The GDR restoring force is the isovector symmetry energy, the plasmon's is Coulomb; Landau damping and escape widths differ in size and origin.", "confidence": "established", "strength": 2}
{"id": "C2483", "a": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures", "name": "Pairing in finite Fermi systems: nuclei and nanograins", "kind": "mechanism", "summary": "Nuclei and nanometre Al grains are both mesoscopic superconductors whose level spacing is comparable to the gap; the exactly solvable Richardson pairing model describes both, and the nuclear odd-even mass effect is the parity effect seen in grain spectroscopy and superconducting single-electron transistors.", "map": "H=\\sum_k\\epsilon_kn_k-G\\sum_{kk'}c^\\dagger_{k\\uparrow}c^\\dagger_{\\bar k\\downarrow}c_{\\bar k'\\downarrow}c_{k'\\uparrow};\\ \\text{crossover at }d/\\Delta\\sim1", "breaks": "Grains have a Coulomb charging energy and an electron bath; nuclei have two particle species, deformation and spin-orbit-split shells, so level statistics and blocking differ.", "confidence": "established", "strength": 2}
{"id": "C2484", "a": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures", "name": "Shell structure and magic numbers in clusters and dots", "kind": "method transfer", "summary": "Alkali-metal clusters show magic numbers 8, 20, 40, 58 and quantum dots show shell filling with Hund's rule; both are understood with nuclear tools (mean-field shells, Strutinsky shell corrections, Nilsson-type deformation). Quantum dots are 'artificial atoms' and clusters 'electronic nuclei'.", "map": "E=E_{\\rm LD}+\\delta E_{\\rm shell},\\ \\delta E=\\sum_i\\epsilon_i-\\tilde E;\\ \\text{2D HO dot: }2,6,12,20\\ \\leftrightarrow\\ \\text{3D HO: }2,8,20,40", "breaks": "Electron systems lack spin-orbit-driven magic numbers (no 28, 50, 82) and are Coulomb-repulsive and externally confined; nuclei are self-bound with short-range forces.", "confidence": "established", "strength": 3}
{"id": "C2485", "a": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "b": "08-condensed-matter/strongly-correlated-electrons", "name": "Landau Fermi-liquid theory of nuclei and nuclear matter", "kind": "method transfer", "summary": "Independent-particle shells survive a strong NN force because the relevant objects are Landau quasiparticles near the Fermi surface; Migdal's theory of finite Fermi systems uses Landau parameters (effective mass, spin-isospin g') as electron Fermi-liquid theory does, and giant resonances are its zero-sound-like modes.", "map": "\\delta E=\\sum_p\\epsilon_p\\delta n_p+\\tfrac12\\sum_{pp'}f_{pp'}\\delta n_p\\delta n_{p'};\\ \\frac{m^*}{m}=1+\\frac{F_1}{3};\\ m^*_N/m\\approx0.7\\text{–}0.9", "breaks": "Nuclei are finite and self-bound with two species and a strong tensor force; quasiparticle lifetimes are short away from the Fermi surface and strength fragmentation is large.", "confidence": "established", "strength": 3}
{"id": "C2486", "a": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "b": "08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals", "name": "Shape phase transitions as finite-size quantum criticality", "kind": "analogy", "summary": "Along isotopic chains nuclei change from spherical to deformed as the control parameter N varies; Landau theory in quadrupole collective coordinates and the critical-point symmetries E(5)/X(5) treat this as a quantum phase transition with finite-N precursors.", "map": "V(\\beta,\\gamma)=a\\beta^2-b\\beta^3\\cos3\\gamma+c\\beta^4;\\ R_{4/2}:2.0\\to3.33", "breaks": "Nuclei never reach a thermodynamic limit, N is discrete, and there is no spatial correlation length, quantum critical fan or non-Fermi-liquid transport.", "confidence": "established", "strength": 2}
{"id": "C2487", "a": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Nuclear pairing is BCS pairing", "kind": "mechanism", "summary": "Odd-even mass staggering, the gap in even-even spectra and reduced moments of inertia follow from the BCS gap equation with a short-range NN attraction near the nuclear Fermi surface; Bohr, Mottelson and Pines carried BCS over to nuclei within a year.", "map": "\\Delta=\\frac{G}{2}\\sum_k\\frac{\\Delta}{E_k},\\ E_k=\\sqrt{(\\epsilon_k-\\lambda)^2+\\Delta^2};\\ \\Delta_{\\rm nucl}\\approx12/\\sqrt A\\ \\text{MeV}", "breaks": "Nuclei hold only ~10 pairs, so BCS particle-number fluctuations matter (projection needed) and the coherence length exceeds the nucleus; the pairing glue is the bare nuclear force, not a retarded phonon.", "confidence": "established", "strength": 3}
{"id": "C2488", "a": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Rotation vs magnetic field: backbending and Meissner", "kind": "analogy", "summary": "The Coriolis force on a rotating nucleus acts on time-reversed pairs as a magnetic field acts on Cooper pairs; pairing quenches the moment of inertia below the rigid value (like Meissner screening), and backbending at high spin is the analogue of the critical field that destroys superconductivity.", "map": "H'=H-\\omega J_x\\leftrightarrow H-\\mu_B\\mathbf B\\cdot\\boldsymbol\\sigma;\\ \\mathcal I<\\mathcal I_{\\rm rigid}\\leftrightarrow\\chi<0;\\ \\omega_c\\leftrightarrow H_c", "breaks": "The cranking 'field' couples to the orbital angular momentum of a finite drop, not to a gauge field; there is no flux expulsion, London length or vortex phase, and the transition is smeared by finite size.", "confidence": "established", "strength": 2}
{"id": "C2594", "a": "08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons", "b": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "name": "Itinerant versus local-moment magnetism", "kind": "mechanism", "summary": "Stoner ferromagnetism and spin-density waves arise from band structure and Fermi surface nesting, contrasting with Heisenberg local moments; RKKY links conduction electrons to local moments.", "map": "I\\,N(E_F)>1,\\ J_{\\rm RKKY}(r)\\propto \\cos(2k_Fr)/r^3", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2595", "a": "08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "Bloch bands to Berry curvature and Chern numbers", "kind": "identity", "summary": "Berry connection defined on Bloch eigenstates over the Brillouin zone gives Chern and Z2 invariants; band theory supplies the Hilbert-space bundle that topology classifies.", "map": "A(\\mathbf{k})=i\\langle u_{\\mathbf{k}}|\\nabla_{\\mathbf{k}}|u_{\\mathbf{k}}\\rangle,\\ C=\\frac{1}{2\\pi}\\int F", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2596", "a": "08-condensed-matter/crystals-and-electronic-structure/density-functional-theory", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "DFT as input to DMFT and QMC", "kind": "method transfer", "summary": "Kohn–Sham band structures supply downfolded tight-binding models for DMFT (DFT+DMFT), and QMC benchmarks exchange–correlation functionals; both address the many-electron problem at different accuracy and cost.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2597", "a": "08-condensed-matter/crystals-and-electronic-structure/density-functional-theory", "b": "08-condensed-matter/superconductivity/hydride-superconductors-under-pressure", "name": "DFT prediction of hydride superconductors", "kind": "method transfer", "summary": "DFT structure search plus linear-response phonons and Eliashberg theory predicted H3S and LaH10 Tc before experiment, a rare first-principles prediction of Tc.", "map": "\\lambda=2\\int\\frac{\\alpha^2F(\\omega)}{\\omega}d\\omega", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2598", "a": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures", "name": "Coulomb blockade and Landauer transport in dots", "kind": "method transfer", "summary": "Quantum-dot conductance is analysed with Landauer–Büttiker and master-equation transport; conductance quantization and resonant tunnelling in mesoscopic wires carry over to dots.", "map": "G=\\frac{2e^2}{h}\\sum_n T_n", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2599", "a": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "b": "08-condensed-matter/topological-matter/quantum-hall-effects", "name": "Landauer–Büttiker edge channels", "kind": "method transfer", "summary": "Landauer–Büttiker formalism with chiral edge channels explains quantized Hall resistance, and quantized conductance in mesoscopic wires shares the same transmission-mode counting.", "map": "R_H=\\frac{h}{\\nu e^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2600", "a": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Phonon-mediated pairing", "kind": "mechanism", "summary": "Electron–phonon coupling gives the retarded attraction behind Cooper pairing; the isotope effect and Debye frequency set Tc prefactors in BCS and Eliashberg theory.", "map": "T_c\\sim\\omega_D\\,e^{-1/N(0)V}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2601", "a": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "b": "08-condensed-matter/superconductivity/hydride-superconductors-under-pressure", "name": "High-frequency hydrogen phonons drive high Tc", "kind": "mechanism", "summary": "Light hydrogen gives very high phonon frequencies and strong electron–phonon coupling, so BCS/Eliashberg Tc scales with the phonon energy scale.", "map": "T_c\\propto\\omega_{\\log}\\,f(\\lambda,\\mu^*)", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2602", "a": "08-condensed-matter/crystals-and-electronic-structure/semiconductors", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/transition-metal-dichalcogenides-and-excitons", "name": "Semiconductor physics in monolayer TMDs", "kind": "shared object", "summary": "TMD monolayers are direct-gap 2D semiconductors where doping, heterojunctions and carrier statistics carry over, but reduced screening gives huge exciton binding energies beyond the 3D Wannier picture.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2603", "a": "08-condensed-matter/crystals-and-electronic-structure/semiconductors", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/transition-metal-dichalcogenides-and-excitons", "name": "Wannier excitons in semiconductors vs TMDs", "kind": "analogy", "summary": "Excitons are hydrogen-like electron–hole bound states in both; TMD monolayers have nonlocal screening that modifies the Rydberg series.", "map": "E_n=-\\frac{\\mu e^4}{2\\hbar^2\\epsilon^2 n^2}", "breaks": "In 2D the dielectric screening is nonlocal (Keldysh), so the hydrogenic series fails for excited states.", "confidence": "established", "strength": 2}
{"id": "C2604", "a": "08-condensed-matter/low-dimensional-and-quantum-materials", "b": "08-condensed-matter/topological-matter", "name": "2D materials as topological platforms", "kind": "shared object", "summary": "Graphene, TMDs and moiré systems host Dirac cones, Chern bands, quantum spin Hall and quantum anomalous Hall states, linking low-dimensional materials to topological classification.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2605", "a": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "b": "08-condensed-matter/topological-matter/quantum-hall-effects", "name": "Relativistic quantum Hall effect in graphene", "kind": "mechanism", "summary": "Dirac electrons in graphene give half-integer quantum Hall plateaus from the zero-energy n=0 Landau level and Berry phase pi.", "map": "\\sigma_{xy}=\\pm 4\\left(n+\\tfrac12\\right)\\frac{e^2}{h},\\ E_n=\\pm v_F\\sqrt{2\\hbar eBn}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2606", "a": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "b": "08-condensed-matter/topological-matter/topological-semimetals", "name": "Graphene as a 2D Dirac semimetal", "kind": "analogy", "summary": "Graphene's Dirac points are the 2D counterpart of 3D Weyl/Dirac nodes; both are linear band crossings with Berry phase and relativistic-like quasiparticles.", "map": "H=v\\,\\boldsymbol{\\sigma}\\cdot\\mathbf{k}", "breaks": "Graphene nodes need C2T and are not topologically protected against gap opening by symmetry-breaking substrates; 3D Weyl nodes are stable monopoles of Berry flux.", "confidence": "established", "strength": 2}
{"id": "C2607", "a": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "b": "08-condensed-matter/topological-matter/topological-semimetals", "name": "Weyl/Dirac nodes and graphene Dirac cones", "kind": "analogy", "summary": "Weyl and Dirac semimetals generalise graphene's Dirac cones to 3D, with Fermi arcs and chiral anomaly replacing edge zero modes and half-integer Hall response.", "map": "H=\\hbar v\\,\\chi\\,\\boldsymbol{\\sigma}\\cdot\\mathbf{k}", "breaks": "Graphene has no Fermi arcs or net chirality per valley pair in the same sense and the nodes are not monopoles.", "confidence": "established", "strength": 2}
{"id": "C2608", "a": "08-condensed-matter/low-dimensional-and-quantum-materials/moire-materials-and-twisted-bilayers", "b": "08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order", "name": "Fractional Chern insulators in moiré bands", "kind": "shared object", "summary": "Flat Chern bands in twisted MoTe2 and graphene host fractional Chern insulators at zero field, lattice analogues of fractional quantum Hall states with anyonic excitations.", "map": "", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2609", "a": "08-condensed-matter/low-dimensional-and-quantum-materials/moire-materials-and-twisted-bilayers", "b": "08-condensed-matter/strongly-correlated-electrons/hubbard-model-and-mott-physics", "name": "Moiré superlattices as tunable Hubbard simulators", "kind": "shared object", "summary": "Twisted TMD bilayers realise triangular-lattice Hubbard models with tunable U/W, showing Mott insulators and superconductivity-like phases; magic-angle graphene correlated insulators arise from flat-band Coulomb repulsion.", "map": "H=-t\\sum c^\\dagger_i c_j+U\\sum n_{i\\uparrow}n_{i\\downarrow}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2610", "a": "08-condensed-matter/low-dimensional-and-quantum-materials/moire-materials-and-twisted-bilayers", "b": "08-condensed-matter/topological-matter/quantum-hall-effects", "name": "Hofstadter bands and Chern bands in moiré systems", "kind": "identity", "summary": "Moiré superlattices produce Hofstadter butterflies at accessible fields and Chern bands with quantized Hall response at zero field, linking Landau levels to flat Chern bands and Wannier diagrams.", "map": "\\sigma_{xy}=C\\,e^2/h,\\ n=C\\,\\phi/\\phi_0+s", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2611", "a": "08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures", "b": "08-condensed-matter/strongly-correlated-electrons/heavy-fermions-and-kondo-physics", "name": "Kondo effect in quantum dots", "kind": "shared object", "summary": "A dot with an odd electron number acts as a tunable Anderson impurity, producing a Kondo resonance and unitary conductance at low T that realises single-impurity Kondo physics in a controlled device.", "map": "T_K\\sim\\sqrt{\\Gamma U}\\,e^{-\\pi|\\epsilon_d(\\epsilon_d+U)|/(2\\Gamma U)}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2612", "a": "08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures", "b": "08-condensed-matter/topological-matter/topological-superconductors-and-majoranas", "name": "Majorana nanowires and dot arrays", "kind": "shared object", "summary": "Semiconductor nanowires with spin–orbit coupling, Zeeman field and proximity superconductivity realise Kitaev-chain physics; quantum dot chains build minimal Kitaev chains and probe zero-bias peaks.", "map": "H=-\\mu\\sum c^\\dagger c-t\\sum(c^\\dagger_jc_{j+1}+\\text{h.c.})+\\Delta\\sum c_jc_{j+1}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2613", "a": "08-condensed-matter/low-dimensional-and-quantum-materials/transition-metal-dichalcogenides-and-excitons", "b": "08-condensed-matter/magnetism/spintronics", "name": "Valleytronics and spin-valley locking vs spintronics", "kind": "analogy", "summary": "Spin–valley locking in TMDs lets valley act as a degree of freedom, analogous to spin; valley Hall effect parallels spin Hall effect via Berry curvature, and magnons and excitons share bosonic transport ideas.", "map": "\\Omega(\\pm K)=\\mp\\Omega,\\ \\mathbf{v}_{\\rm an}\\propto\\mathbf{E}\\times\\boldsymbol{\\Omega}", "breaks": "Valley is not a conserved quantum number against intervalley scattering and lacks a simple torque or conservation law like spin transfer.", "confidence": "current research", "strength": 2}
{"id": "C2614", "a": "08-condensed-matter/magnetism/altermagnetism", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "Altermagnets: spin splitting and anomalous Hall", "kind": "mechanism", "summary": "Symmetry-enforced spin-split bands in altermagnets generate anomalous Hall responses via Berry curvature despite zero net magnetization, connecting magnetic point-group symmetry to band geometry.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2615", "a": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "b": "08-condensed-matter/strongly-correlated-electrons/hubbard-model-and-mott-physics", "name": "Superexchange from the Hubbard model", "kind": "identity", "summary": "At half filling and large U the Hubbard model reduces to the Heisenberg antiferromagnet by second-order virtual hopping, deriving Anderson superexchange.", "map": "J=\\frac{4t^2}{U},\\ H=J\\sum \\mathbf{S}_i\\cdot\\mathbf{S}_j", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2616", "a": "08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids", "b": "08-condensed-matter/soft-matter/glasses-and-jamming", "name": "Spin glasses and structural glasses", "kind": "analogy", "summary": "Frustration and rugged energy landscapes link spin glasses to structural glasses; replica symmetry breaking and random first-order transition theory connect the two.", "map": "", "breaks": "Not stated by the analyst.", "confidence": "established", "strength": 2}
{"id": "C2617", "a": "08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids", "b": "08-condensed-matter/soft-matter/liquid-crystals", "name": "Order-by-disorder and defect physics across spin and nematic systems", "kind": "analogy", "summary": "Both study order-parameter manifolds with topological defects (vortices, hedgehogs, disclinations) classified by homotopy; spin ice and nematics share Coulomb-gas-like defect interactions and degenerate manifolds.", "map": "\\pi_n(M)", "breaks": "Spin liquids are quantum with fractionalized excitations and entanglement, while nematics are classical thermal systems with Frank elasticity.", "confidence": "proposed", "strength": 1}
{"id": "C2618", "a": "08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids", "b": "08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order", "name": "Quantum spin liquids as topologically ordered states", "kind": "shared object", "summary": "Gapped spin liquids host fractionalised spinons and visons with topological ground-state degeneracy; the Kitaev honeycomb model realises Z2 gauge theory with Majorana excitations.", "map": "H=-\\sum_{\\langle ij\\rangle_\\gamma}K_\\gamma\\sigma_i^\\gamma\\sigma_j^\\gamma", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2619", "a": "08-condensed-matter/magnetism/magnetic-skyrmions-and-textures", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "Skyrmion topological Hall effect and emergent fields", "kind": "mechanism", "summary": "Electrons traversing a skyrmion texture acquire a real-space Berry phase, producing an emergent magnetic field and topological Hall effect, the real-space counterpart of momentum-space Berry curvature.", "map": "B_{\\rm em}=\\frac{\\Phi_0}{4\\pi}\\,\\mathbf{n}\\cdot(\\partial_x\\mathbf{n}\\times\\partial_y\\mathbf{n}),\\ N_{sk}=\\frac{1}{4\\pi}\\int \\mathbf{n}\\cdot(\\partial_x\\mathbf{n}\\times\\partial_y\\mathbf{n})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2620", "a": "08-condensed-matter/soft-matter/active-matter", "b": "08-condensed-matter/soft-matter/liquid-crystals", "name": "Active nematics", "kind": "shared object", "summary": "Active nematics combine Frank elasticity and defect dynamics of liquid crystals with active stress, producing spontaneous flows and self-propelled +1/2 disclinations.", "map": "\\sigma^{act}=-\\zeta\\,\\mathbf{Q}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2621", "a": "08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order", "b": "08-condensed-matter/topological-matter/quantum-hall-effects", "name": "FQHE as prototype topological order", "kind": "historical", "summary": "The fractional quantum Hall effect, with Laughlin quasiparticles of fractional charge and statistics, is the archetype of topological order, with chiral edge modes and ground-state degeneracy on a torus.", "map": "\\nu=1/m,\\ q^*=e/m", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2622", "a": "08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order", "b": "08-condensed-matter/topological-matter/topological-superconductors-and-majoranas", "name": "Majorana zero modes as non-Abelian anyons", "kind": "shared object", "summary": "Vortex Majorana modes in p+ip superconductors obey Ising non-Abelian statistics, the basis of topological quantum computation and the Moore–Read fractional quantum Hall analogy.", "map": "", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2623", "a": "08-condensed-matter/strongly-correlated-electrons/heavy-fermions-and-kondo-physics", "b": "08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals", "name": "Heavy-fermion quantum critical points", "kind": "shared object", "summary": "Heavy-fermion metals such as CeCu6-xAux are canonical quantum critical systems, where Kondo breakdown competes with RKKY magnetism in a Doniach phase diagram and yields non-Fermi-liquid behaviour.", "map": "T_K\\sim e^{-1/J\\rho},\\ T_{RKKY}\\sim J^2\\rho", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2624", "a": "08-condensed-matter/strongly-correlated-electrons/hubbard-model-and-mott-physics", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "Numerical solutions of the Hubbard model", "kind": "method transfer", "summary": "DMFT, DQMC, DMRG and tensor networks were developed and benchmarked on the Hubbard model; DMFT captures the Mott transition as a mean-field in infinite dimensions.", "map": "G_{\\rm loc}=\\sum_k[\\omega+\\mu-\\Sigma-\\epsilon_k]^{-1}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2625", "a": "08-condensed-matter/strongly-correlated-electrons/hubbard-model-and-mott-physics", "b": "08-condensed-matter/superconductivity/cuprate-high-tc-superconductors", "name": "Doped Mott insulator and cuprate superconductivity", "kind": "shared object", "summary": "Cuprates are doped Mott insulators described by the Hubbard/t-J model; d-wave pairing emerges from superexchange-driven correlations (RVB).", "map": "H_{tJ}=-t\\sum P c^\\dagger c P+J\\sum(\\mathbf{S}_i\\cdot\\mathbf{S}_j-\\tfrac14 n_in_j)", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2626", "a": "08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals", "b": "08-condensed-matter/superconductivity/cuprate-high-tc-superconductors", "name": "Strange metal normal state of cuprates", "kind": "shared object", "summary": "Optimally doped cuprates show T-linear resistivity and a possible quantum critical point under the superconducting dome; non-Fermi-liquid scattering near Planckian bound.", "map": "\\rho\\sim\\rho_0+AT,\\ \\hbar/\\tau\\sim k_BT", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2627", "a": "08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals", "b": "08-condensed-matter/superconductivity/iron-based-and-nickelate-superconductors", "name": "Unconventional superconductivity near a quantum critical point", "kind": "shared object", "summary": "Iron pnictides show a superconducting dome around a putative antiferromagnetic quantum critical point with T-linear resistivity, suggesting spin-fluctuation pairing as in cuprates and heavy fermions.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2628", "a": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "b": "08-condensed-matter/topological-matter/topological-superconductors-and-majoranas", "name": "BdG quasiparticles and topological superconductivity", "kind": "identity", "summary": "Bogoliubov–de Gennes Hamiltonians of BCS theory carry particle-hole symmetry; for p-wave or engineered pairing their topology yields Majorana modes, as in the Kitaev chain.", "map": "H_{BdG}=\\begin{pmatrix}h&\\Delta\\\\\\Delta^\\dagger&-h^T\\end{pmatrix}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2629", "a": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "b": "08-condensed-matter/topological-matter/topological-superconductors-and-majoranas", "name": "Fractional Josephson effect", "kind": "mechanism", "summary": "Topological Josephson junctions host Majorana-mediated 4π-periodic current-phase relations, a signature that differs from the 2π conventional Josephson effect.", "map": "I(\\phi)\\propto\\sin(\\phi/2)", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2630", "a": "08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Band theory of neutrons in the neutron-star crust", "kind": "method transfer", "summary": "Bragg scattering of unbound superfluid neutrons by the nuclear lattice of the inner crust is computed with Bloch's theorem and band-structure methods; the resulting large neutron effective mass (entrainment) reduces the mobile superfluid fraction and challenges crust-only glitch models.", "map": "\\psi_{nk}(\\mathbf r+\\mathbf R)=e^{i\\mathbf k\\cdot\\mathbf R}\\psi_{nk}(\\mathbf r):\\ \\text{electrons}\\to\\text{free neutrons};\\ m_n^*/m_n\\gg1\\ (\\text{entrainment})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2631", "a": "08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Degenerate Fermi gas: metals and white dwarfs", "kind": "identity", "summary": "The same degenerate Fermi-Dirac electron gas gives the Sommerfeld model of metals and the pressure that supports white dwarfs; Fowler applied Fermi statistics to white dwarfs in 1926, before Sommerfeld applied it to metals, and relativistic kinematics turns P~n^{5/3} into P~n^{4/3}, giving the Chandrasekhar mass.", "map": "E_F=\\frac{\\hbar^2}{2m_e}(3\\pi^2n_e)^{2/3},\\ P=\\tfrac25n_eE_F\\ (n_e\\sim10^{23}\\,\\text{cm}^{-3})\\to P\\propto n_e^{4/3}\\ (\\text{WD},\\ n_e\\sim10^{30})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2632", "a": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets", "name": "Superionic water ice in ice-giant interiors", "kind": "shared object", "summary": "Superionic water, an oxygen crystal through which protons diffuse like a liquid, was predicted by ab initio simulation for Uranus and Neptune and identified in laser-shock experiments by nanosecond X-ray diffraction (fcc ice XVIII); it may explain the ice giants' non-dipolar magnetic fields.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2633", "a": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Coulomb crystallization of white-dwarf cores", "kind": "mechanism", "summary": "Carbon-oxygen ions in a cooling white dwarf freeze into a bcc Coulomb (one-component-plasma) crystal near Gamma~175; Gaia's cooling-sequence pile-up confirmed latent-heat release and phase separation, and the same bcc Coulomb lattice makes up neutron-star crusts.", "map": "\\Gamma=\\frac{Z^2e^2}{4\\pi\\epsilon_0ak_BT}\\approx175\\ (\\text{melting}),\\ a=(3/4\\pi n_i)^{1/3};\\ \\text{bcc, Madelung energy}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2634", "a": "08-condensed-matter/crystals-and-electronic-structure/density-functional-theory", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "DFT and dielectric response for dark-matter scattering", "kind": "method transfer", "summary": "Dark-matter-electron scattering rates in crystals are computed from DFT crystal form factors and, with screening included, from the energy-loss function Im[-1/eps(q,omega)], so electronic-structure codes directly set direct-detection sensitivities.", "map": "\\frac{dR}{d\\omega}\\propto\\int d^3q\\,\\frac{q^2}{e^2}\\,\\mathrm{Im}\\left[\\frac{-1}{\\epsilon(\\mathbf q,\\omega)}\\right]\\eta(v_{\\min})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2635", "a": "08-condensed-matter/crystals-and-electronic-structure/density-functional-theory", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets", "name": "Ab initio equations of state for giant-planet interiors", "kind": "method transfer", "summary": "DFT-based molecular dynamics provides the hydrogen-helium equation of state and the H-He immiscibility ('helium rain') used in Jupiter and Saturn interior models fitted to Juno and Cassini gravity data; DFT exchange-correlation and band-gap errors directly shift the predicted metallization boundary.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2636", "a": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Electron transport in white-dwarf and neutron-star matter", "kind": "method transfer", "summary": "Thermal and electrical conductivities of degenerate stellar matter are computed with the Boltzmann/Ziman theory of metals (electron-phonon Umklapp and electron-impurity scattering, Wiedemann-Franz); crust-cooling curves of accreting neutron stars imply a low-impurity, ordered rather than amorphous crust.", "map": "\\sigma=\\frac{n_ee^2\\tau}{m^*},\\ \\frac{\\kappa}{\\sigma T}=\\frac{\\pi^2k_B^2}{3e^2},\\ \\tau^{-1}=\\tau_{e\\text{-ph}}^{-1}+\\tau_{e\\text{-imp}}^{-1}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2637", "a": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Single-phonon excitations for sub-MeV dark matter", "kind": "mechanism", "summary": "Below ~MeV the dark matter's momentum transfer is below the inverse lattice spacing, so it scatters by creating single acoustic or optical phonons rather than nuclear recoils; polar crystals (GaAs, sapphire) with dark-photon-coupled optical phonons are proposed targets read out by phonon sensors.", "map": "q\\sim m_\\chi v\\lesssim2\\pi/a\\Rightarrow\\text{phonon regime};\\ \\hbar\\omega_q\\sim10\\text{-}100\\,\\text{meV}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2638", "a": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/fast-radio-bursts-and-magnetars", "name": "Crustal shear modes as magnetar QPOs", "kind": "mechanism", "summary": "Quasi-periodic oscillations in magnetar giant-flare tails (tens of Hz) are interpreted as global torsional modes of the crystalline crust, i.e. long-wavelength transverse acoustic phonons of the Coulomb lattice whose speed is set by the shear modulus mu~0.12 n_i Z^2 e^2/a.", "map": "\\omega=v_tk,\\ v_t=\\sqrt{\\mu/\\rho};\\ f_\\ell\\approx\\frac{v_t}{2\\pi R}\\sqrt{(\\ell-1)(\\ell+2)}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2639", "a": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Debye cooling of crystallized white dwarfs", "kind": "mechanism", "summary": "Once a white-dwarf core crystallizes, its ionic heat capacity follows the Debye phonon law and falls as T^3 below Theta_D, so the oldest white dwarfs cool faster ('Debye cooling'), which shapes the faint end of the luminosity function used for cosmochronology.", "map": "C_V=\\frac{12\\pi^4}{5}Nk_B(T/\\Theta_D)^3,\\ \\Theta_D\\sim\\hbar\\omega_{p,i}/k_B,\\ \\omega_{p,i}=\\sqrt{n_iZ^2e^2/\\epsilon_0m_i}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2640", "a": "08-condensed-matter/crystals-and-electronic-structure/semiconductors", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Semiconductor targets for dark-matter electron recoils", "kind": "shared object", "summary": "Silicon and germanium crystals are dark-matter targets: ionization-plus-phonon detectors for nuclear recoils, and single-electron skipper CCDs (SENSEI, DAMIC-M) whose ~1 eV band gap lets sub-GeV dark matter register through electron excitations across the gap.", "map": "E_e\\ge E_g\\approx1.1\\,\\text{eV (Si)};\\ N_{eh}=1+\\lfloor(E_e-E_g)/\\varepsilon\\rfloor,\\ \\varepsilon\\approx3.6\\,\\text{eV}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2641", "a": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "name": "Fullerenes and PAHs: carbon nanostructures in space", "kind": "historical", "summary": "C60 was discovered in laser-vaporization experiments built to mimic carbon-star chemistry, opening the fullerene-nanotube-graphene family of carbon materials; fullerenes were later found in planetary nebulae and C60+ identified as a diffuse-interstellar-band carrier.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2642", "a": "08-condensed-matter/low-dimensional-and-quantum-materials/moire-materials-and-twisted-bilayers", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Wigner crystals and stellar Coulomb crystals", "kind": "analogy", "summary": "Electron Wigner crystals in moire TMD superlattices and the ion crystals of white dwarfs and neutron-star crusts are both one-component plasmas that crystallize in a uniform neutralizing background once Coulomb energy beats kinetic energy (large r_s or large Gamma).", "map": "r_s=a/a_B^*\\gtrsim31\\ (\\text{2D quantum, kinetic}=E_F)\\leftrightarrow\\Gamma\\approx175\\ (\\text{classical, kinetic}=k_BT)", "breaks": "Stellar ions melt classically through thermal fluctuations, while 2D electron Wigner crystals melt quantum mechanically; moire Wigner crystals are pinned to an imposed superlattice and are two-dimensional.", "confidence": "established", "strength": 1}
{"id": "C2643", "a": "08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Emergent monopoles in spin ice and the monopole problem", "kind": "analogy", "summary": "Spin-ice excitations behave as deconfined magnetic monopoles with a Coulomb interaction, a condensed-matter realization of the monopoles whose predicted overproduction at grand-unified transitions motivated inflation.", "map": "", "breaks": "Spin-ice monopoles source the H field (div M), not B; they are emergent quasiparticles with non-quantized, material-set charge, unlike 't Hooft-Polyakov monopoles of a broken gauge group.", "confidence": "established", "strength": 1}
{"id": "C2644", "a": "08-condensed-matter/magnetism/magnetic-skyrmions-and-textures", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "Skyrmions and cosmic textures", "kind": "analogy", "summary": "Magnetic skyrmions and cosmological textures are both non-singular topological solitons of a sphere-valued order parameter classified by homotopy (pi_2 for 2D films, pi_3 for 3D cosmic textures); a collapsing texture was proposed to explain the CMB Cold Spot.", "map": "N_{sk}=\\frac1{4\\pi}\\int\\mathbf m\\cdot(\\partial_x\\mathbf m\\times\\partial_y\\mathbf m)\\,d^2x\\in\\pi_2(S^2)\\leftrightarrow\\pi_3(S^3)\\ \\text{winding}", "breaks": "Skyrmions are static, DMI-stabilized and 2D; cosmic textures are 3D, unstable to collapse by Derrick's theorem and scale with the horizon. The Cold Spot texture interpretation is not established.", "confidence": "proposed", "strength": 1}
{"id": "C2645", "a": "08-condensed-matter/soft-matter/colloids-and-granular-matter", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks", "name": "Dust aggregation: from colloids to planetesimals", "kind": "mechanism", "summary": "The first stage of planet formation is aggregation of micron dust grains by Brownian motion and differential drift into fractal aggregates, followed by compaction, bouncing and fragmentation: the cluster-cluster aggregation and contact mechanics studied in colloids and granular matter.", "map": "D=\\frac{k_BT}{6\\pi\\eta a}\\to t_s=\\frac{\\rho_sa}{\\rho_gv_{th}}\\ (\\text{Epstein});\\ N\\propto R^{d_f},\\ d_f\\approx1.8\\text{-}2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2646", "a": "08-condensed-matter/soft-matter/colloids-and-granular-matter", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics", "name": "Rubble-pile asteroids as granular bodies", "kind": "shared object", "summary": "Most km-sized asteroids (Itokawa, Ryugu, Bennu) are gravitationally bound granular aggregates whose shapes, spin limits, regolith segregation and response to spacecraft contact are governed by granular rheology, friction and weak cohesion.", "map": "\\mu(I)=\\mu_s+\\frac{\\mu_2-\\mu_s}{1+I_0/I};\\ \\text{spin barrier }P\\approx2.2\\,\\text{h (cohesionless)}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2647", "a": "08-condensed-matter/soft-matter/glasses-and-jamming", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks", "name": "Amorphous ices and silicates in disks and dust", "kind": "shared object", "summary": "Interstellar and protoplanetary grains are largely amorphous: vapour-deposited amorphous solid water and glassy silicates whose crystallization (annealing near the star) and glass-transition kinetics record thermal history and control volatile trapping at snow lines.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C2648", "a": "08-condensed-matter/soft-matter/liquid-crystals", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Kibble-Zurek defects: liquid crystals and the early universe", "kind": "analogy", "summary": "Kibble's argument that causally disconnected regions choose independent vacua at a symmetry-breaking transition, leaving strings and monopoles whose overabundance inflation must dilute, was tested by quenching nematic liquid crystals and counting disclinations; Zurek's refinement gives defect density from the quench rate.", "map": "\\pi_1(\\mathcal M)\\neq0\\Rightarrow\\text{strings/disclinations};\\ \\hat\\xi\\sim\\xi_0(\\tau_Q/\\tau_0)^{\\nu/(1+z\\nu)},\\ n\\sim\\hat\\xi^{-2}", "breaks": "Nematic defects form in a dissipative, non-relativistic fluid with no gauge field and coarsen by friction; cosmic defects are relativistic, may be gauge strings, and evolve in an expanding spacetime.", "confidence": "established", "strength": 3}
{"id": "C2649", "a": "08-condensed-matter/soft-matter/liquid-crystals", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Nuclear pasta as a liquid crystal", "kind": "analogy", "summary": "In the neutron-star mantle, competition between nuclear surface tension and long-range Coulomb repulsion produces rod, slab and bubble 'pasta' phases with the symmetries of columnar and smectic liquid crystals (and of block-copolymer microphases); their elasticity is described with liquid-crystal theory.", "map": "F_{\\text{smectic}}=\\tfrac B2(\\partial_zu)^2+\\tfrac{K_1}2(\\nabla_\\perp^2u)^2\\ (\\text{lasagna});\\ \\text{columnar elasticity (spaghetti)}", "breaks": "Pasta is ordered by nuclear plus Coulomb forces at ~1e14 g/cm^3 with no solvent or thermal softness; its elastic constants are MeV-scale and the phases sit in a degenerate electron sea.", "confidence": "current research", "strength": 2}
{"id": "C2650", "a": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "Superconducting detectors for the CMB: TES and MKIDs", "kind": "method transfer", "summary": "CMB experiments (BICEP/Keck, SPT, ACT, Simons Observatory, CMB-S4) use arrays of transition-edge-sensor bolometers biased on the steep R(T) of a superconducting transition, and kinetic-inductance detectors that sense photon pair breaking through the Cooper-pair kinetic inductance.", "map": "\\alpha=\\frac TR\\frac{dR}{dT}\\sim100;\\ L_k\\propto\\mu_0\\lambda_L^2,\\ \\lambda_L^{-2}\\propto n_s;\\ h\\nu>2\\Delta\\ \\text{breaks pairs}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2651", "a": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Cosmic-string formation simulated in superfluid 3He", "kind": "analogy", "summary": "Neutron-absorption hot spots in BCS-paired superfluid 3He re-cool through Tc and nucleate vortex tangles at the rate predicted by the Kibble-Zurek mechanism, a laboratory test of defect formation in early-universe phase transitions with a multicomponent order parameter.", "map": "", "breaks": "3He is a non-relativistic p-wave condensate whose vortices are global (no gauge field), whereas GUT strings are relativistic and typically local; the quench is spatially inhomogeneous, unlike a cosmological transition.", "confidence": "established", "strength": 2}
{"id": "C2652", "a": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Superconducting phonon sensors and targets for dark matter", "kind": "method transfer", "summary": "Cryogenic dark-matter searches (SuperCDMS, CRESST) read athermal phonons from keV nuclear recoils with tungsten transition-edge sensors; superconductors themselves are proposed as targets for keV-mass dark matter because the gap 2Delta~meV sets an ultra-low threshold.", "map": "E_{\\text{th}}\\sim2\\Delta\\approx3.5k_BT_c\\sim\\text{meV}\\ \\text{vs. }E_g\\sim\\text{eV (semiconductor)}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2653", "a": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "name": "Cosmic rays and pair breaking in superconducting devices", "kind": "mechanism", "summary": "Cosmic-ray muons and environmental gamma rays deposit energy in substrates as athermal phonons that break Cooper pairs, causing correlated quasiparticle bursts and error avalanches in superconducting qubits; this is the pair-breaking channel that cryogenic detectors use to see particles.", "map": "N_{qp}\\approx\\eta E_{\\text{dep}}/\\Delta,\\ \\Delta_{\\text{Al}}\\approx0.18\\,\\text{meV}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2654", "a": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Nucleon pairing and neutron-star superfluidity", "kind": "mechanism", "summary": "The BCS gap equation with nuclear instead of phonon attraction gives 1S0 neutron superfluidity in the inner crust and 3P2 neutron and 1S0 proton pairing in the core; pair-breaking-formation neutrino emission just below Tc explains the rapid cooling of the Cas A neutron star.", "map": "\\Delta_k=-\\sum_{k'}V_{kk'}\\frac{\\Delta_{k'}}{2E_{k'}}\\tanh\\frac{E_{k'}}{2k_BT};\\ V:\\text{phonon (meV)}\\to\\text{NN }^1S_0,{}^3P_2\\text{ (MeV)}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2655", "a": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Vortex pinning and creep: flux lines vs pulsar glitches", "kind": "analogy", "summary": "Pulsar glitches are modelled as catastrophic unpinning of quantized neutron-superfluid vortices from the crust lattice, the physics of Abrikosov flux-line pinning and Anderson-Kim thermally activated flux creep in type-II superconductors; post-glitch relaxation is vortex creep.", "map": "\\oint\\mathbf v_s\\cdot d\\mathbf l=h/2m_n\\ (\\text{neutron vortex})\\leftrightarrow\\Phi_0=h/2e\\ (\\text{flux line});\\ \\text{Magnus}\\leftrightarrow\\text{Lorentz force}", "breaks": "Neutron vortices are neutral and feel Magnus rather than Lorentz forces; pinning sites are nuclei of a Coulomb lattice, not material defects, and entrainment couples the superfluid to the crust.", "confidence": "established", "strength": 3}
{"id": "C2656", "a": "08-condensed-matter/superconductivity/hydride-superconductors-under-pressure", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets", "name": "Metallic hydrogen in giant planets", "kind": "shared object", "summary": "Metallic hydrogen, predicted by Wigner and Huntington and proposed by Ashcroft as a high-Tc phonon superconductor (the idea behind hydride superconductors), makes up most of Jupiter's and Saturn's interiors, where its conductivity powers their dynamos; shock and static compression of the insulator-metal transition serve both fields.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2657", "a": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "SQUID multiplexed readout of detector arrays", "kind": "method transfer", "summary": "Kilo- to hundred-thousand-pixel TES arrays for CMB polarimetry are read out with SQUID amplifiers in time-division or microwave (rf-SQUID resonator) multiplexing, exploiting the flux-periodic Josephson response and its low noise.", "map": "V(\\Phi)\\ \\text{periodic in }\\Phi_0=h/2e;\\ \\delta\\Phi\\sim10^{-6}\\Phi_0/\\sqrt{\\text{Hz}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2658", "a": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Josephson parametric amplifiers in axion haloscopes", "kind": "method transfer", "summary": "Axion haloscopes (ADMX, HAYSTAC) detect axion-to-photon conversion in a microwave cavity with Josephson parametric amplifiers operating near the standard quantum limit, and HAYSTAC's squeezed-vacuum readout beats it.", "map": "T_{\\text{sys}}\\gtrsim\\hbar\\omega/k_B\\ (\\text{SQL});\\ \\text{scan rate}\\propto T_{\\text{sys}}^{-2}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2659", "a": "08-condensed-matter/topological-matter/topological-insulators", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Axion quasiparticles in magnetic topological insulators", "kind": "analogy", "summary": "Magnetic topological insulators host a dynamical axion field theta(t) coupling as theta E.B; its quasiparticle (a longitudinal antiferromagnetic magnon mode) is proposed as a tunable meV-scale medium that converts axion dark matter into THz photons.", "map": "\\mathcal L_\\theta=\\frac{\\theta e^2}{2\\pi h}\\mathbf E\\cdot\\mathbf B\\leftrightarrow\\mathcal L_a=g_{a\\gamma\\gamma}\\,a\\,\\mathbf E\\cdot\\mathbf B", "breaks": "The solid-state axion is an emergent collective mode with a material-set mass, not the QCD axion; only the electrodynamic coupling form is shared, and no candidate material is yet confirmed.", "confidence": "proposed", "strength": 2}
{"id": "C2660", "a": "08-condensed-matter/topological-matter/topological-semimetals", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Dirac materials as light dark-matter targets", "kind": "method transfer", "summary": "3D Dirac and Weyl semimetals with meV-scale gaps and weak in-medium screening have been proposed as targets for sub-MeV dark matter scattering or absorption on electrons, with directional sensitivity from anisotropic Dirac cones.", "map": "H_W=\\hbar v_F\\boldsymbol\\sigma\\cdot\\mathbf k,\\ E_g\\to\\text{meV};\\ v_F\\ll c\\ \\text{matches DM kinematics}", "breaks": "", "confidence": "proposed", "strength": 1}
{"id": "C2661", "a": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "b": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "name": "X-ray diffraction and Thomson scattering of shocked matter", "kind": "method transfer", "summary": "Crystallography and inelastic scattering move into high-energy-density physics: nanosecond X-ray diffraction identifies crystal structures in laser-shocked samples, and X-ray Thomson scattering measures the dynamic structure factor S(k,omega), the same quantity inelastic X-ray and neutron scattering measure in solids, to infer temperature and ionization.", "map": "\\frac{d^2\\sigma}{d\\Omega d\\omega}=\\sigma_T\\frac{k_1}{k_0}S(\\mathbf k,\\omega),\\ \\mathbf k=\\mathbf k_1-\\mathbf k_0\\ (\\text{Bragg: }\\mathbf k=\\mathbf G)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2662", "a": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "b": "10-plasma-physics/magnetic-confinement-fusion/burning-plasmas-and-iter", "name": "Neutron damage and defects in fusion materials", "kind": "shared object", "summary": "14 MeV fusion neutrons create displacement cascades (vacancies, interstitials, transmutation helium) in tungsten and steel walls; point-defect and dislocation physics of crystals, measured in dpa, sets component lifetime.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C2663", "a": "08-condensed-matter/crystals-and-electronic-structure/density-functional-theory", "b": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "name": "DFT molecular dynamics for warm dense matter", "kind": "method transfer", "summary": "Equations of state, conductivities and opacities of warm dense matter (solid density, eV temperatures, partially degenerate) are computed with finite-temperature Kohn-Sham DFT molecular dynamics borrowed from electronic-structure theory, with Mermin's finite-T functional and temperature-dependent exchange-correlation.", "map": "\\Omega[n]=F_{\\text{Mermin}}[n]-\\mu N,\\ \\theta=k_BT/E_F\\sim1,\\ \\Gamma\\sim1", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2664", "a": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Boltzmann transport in solids and plasma kinetics", "kind": "identity", "summary": "Semiclassical electron transport in crystals solves the same kinetic equation as plasma physics, with a Lorentz-force streaming term and a collision integral (relaxation-time or Fokker-Planck); Landau damping of plasmons into the electron-hole continuum is the solid-state counterpart of collisionless Landau damping.", "map": "\\partial_tf+\\mathbf v\\cdot\\nabla_{\\mathbf r}f+\\frac{q}{\\hbar}(\\mathbf E+\\mathbf v\\times\\mathbf B)\\cdot\\nabla_{\\mathbf k}f=C[f],\\ \\mathbf v=\\hbar^{-1}\\nabla_{\\mathbf k}\\epsilon_n(\\mathbf k)", "breaks": "Solid-state carriers have band dispersions and Fermi-Dirac statistics with Pauli-blocked collisions and Umklapp; most plasma kinetic theory is classical, collisionless and long-range, with self-consistent Vlasov fields.", "confidence": "established", "strength": 2}
{"id": "C2665", "a": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Helicons and Alfven waves in metals", "kind": "mechanism", "summary": "Compensated or uncompensated metals in a strong magnetic field are solid-state plasmas: they carry low-frequency helicon (whistler) waves, observed in sodium, and Alfven waves in bismuth, with dispersion set by carrier density and B exactly as in magnetized plasmas.", "map": "\\omega_{\\text{helicon}}=\\frac{k^2B}{\\mu_0ne}\\ (\\text{whistler, }\\omega\\ll\\omega_c);\\ v_A=\\frac{B}{\\sqrt{\\mu_0n(m_e^*+m_h^*)}}", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C2666", "a": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Plasmons, ion-acoustic waves and phonons in metals", "kind": "identity", "summary": "The bulk plasmon of a metal is the Langmuir wave of its electron gas, and longitudinal acoustic phonons in a metal are ion plasma oscillations screened by the electrons, exactly the ion-acoustic wave; Bohm and Staver used this to derive the sound speed of metals.", "map": "\\omega_{pe}^2=\\frac{ne^2}{\\epsilon_0m_e};\\ \\omega^2=\\frac{\\Omega_{pi}^2}{1+1/(k\\lambda)^2}\\Rightarrow c_s=\\sqrt{\\tfrac{Zm_e}{3M}}\\,v_F\\ (\\text{Bohm-Staver})\\leftrightarrow\\sqrt{ZT_e/m_i}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2667", "a": "08-condensed-matter/crystals-and-electronic-structure/semiconductors", "b": "10-plasma-physics/low-temperature-and-applied-plasmas/plasma-discharges-and-processing", "name": "Plasma etching and deposition in chip fabrication", "kind": "method transfer", "summary": "Reactive-ion etching, atomic-layer etching and plasma-enhanced CVD shape every semiconductor device; sheath-accelerated ions give anisotropic etches, and EUV lithography light comes from laser-produced tin plasmas.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2668", "a": "08-condensed-matter/crystals-and-electronic-structure/semiconductors", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Debye screening in plasmas and doped semiconductors", "kind": "identity", "summary": "Carriers in a non-degenerate semiconductor are a classical plasma: the extrinsic Debye length sets the width of space-charge regions and the screening of ionized donors, and in the degenerate (metallic) limit it becomes the Thomas-Fermi length, both from linearized Poisson-Boltzmann.", "map": "\\lambda_D=\\sqrt{\\frac{\\epsilon_0k_BT_e}{n_ee^2}}\\leftrightarrow L_D=\\sqrt{\\frac{\\epsilon_s k_BT}{q^2N_D}};\\ \\text{degenerate: }k_{TF}^2=\\frac{e^2}{\\epsilon}g(E_F)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2669", "a": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "b": "10-plasma-physics/plasma-fundamentals", "name": "Dirac fluid: graphene's electron-hole plasma", "kind": "mechanism", "summary": "Near charge neutrality, thermally excited electrons and holes in clean graphene form a strongly interacting two-component relativistic plasma whose hydrodynamic transport violates the Wiedemann-Franz law by more than an order of magnitude.", "map": "\\text{coupling }\\alpha_g=\\frac{e^2}{4\\pi\\epsilon\\hbar v_F}\\sim1;\\ \\tau_{ee}^{-1}\\sim\\alpha_g^2k_BT/\\hbar", "breaks": "", "confidence": "current research", "strength": 2}