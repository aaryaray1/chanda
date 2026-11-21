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


---

# Packet 08-5 (59 records)

{"id": "C2670", "a": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Two-dimensional plasmons in graphene and 2DEGs", "kind": "mechanism", "summary": "Electrons in graphene and semiconductor 2DEGs support gate-tunable 2D plasmons with omega~sqrt(q), imaged by infrared nano-imaging; drift-driven plasma-wave instabilities in field-effect transistors (Dyakonov-Shur) are the solid-state analogue of streaming instabilities and are used for THz detection.", "map": "\\omega_{2D}^2=\\frac{n_se^2q}{2\\epsilon_0\\bar\\epsilon m^*}\\ (\\text{graphene: }m^*\\to\\hbar k_F/v_F)\\leftrightarrow\\omega_{pe}^2=\\frac{ne^2}{\\epsilon_0m_e}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2671", "a": "08-condensed-matter/low-dimensional-and-quantum-materials/transition-metal-dichalcogenides-and-excitons", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Exciton Mott transition by plasma screening", "kind": "mechanism", "summary": "At high photoexcitation density, screening by free carriers in 2D semiconductors shortens the screening length below the exciton radius, so excitons ionize into an electron-hole plasma with giant band-gap renormalization; this is the Mott criterion for pressure ionization in dense plasmas.", "map": "\\text{Mott: }\\lambda_{\\text{screen}}(n)\\lesssim a_X\\ \\Leftrightarrow\\ n_Ma_X^2\\sim0.1\\ (2D)\\ \\leftrightarrow\\ \\lambda_D\\lesssim a_0\\ (\\text{pressure ionization})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2672", "a": "08-condensed-matter/soft-matter/active-matter", "b": "10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas", "name": "Non-reciprocal forces in complex plasmas and active matter", "kind": "mechanism", "summary": "Ion wakes downstream of levitated dust grains make grain-grain forces non-reciprocal, violating Newton's third law and breaking detailed balance; complex plasmas thus become a model system for the non-reciprocal and odd interactions central to active matter.", "map": "\\mathbf F_{ij}\\neq-\\mathbf F_{ji}\\Rightarrow\\text{no Boltzmann distribution};\\ T_i\\neq T_j\\ \\text{for distinct species}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2673", "a": "08-condensed-matter/soft-matter/colloids-and-granular-matter", "b": "10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas", "name": "Yukawa plasma crystals and colloidal crystals", "kind": "mechanism", "summary": "Charged dust grains in a plasma and charged colloids in an electrolyte both interact by a screened-Coulomb (Yukawa/DLVO) potential, crystallize when the coupling parameter is large, and let melting, defects and phonons be watched particle by particle.", "map": "V(r)=\\frac{Q^2}{4\\pi\\epsilon_0r}e^{-r/\\lambda_D}\\ (\\text{dust})\\leftrightarrow V_{\\text{DLVO}}\\propto\\frac{e^{-\\kappa r}}{r},\\ \\kappa^{-1}=\\text{Debye length of electrolyte}", "breaks": "Dusty plasmas are underdamped, strongly driven and open (charging currents, ion wakes), while colloids are overdamped by the solvent and in thermal equilibrium.", "confidence": "established", "strength": 3}
{"id": "C2674", "a": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "b": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "name": "Quantum Monte Carlo for the warm dense electron gas", "kind": "method transfer", "summary": "Quantum Monte Carlo for the uniform electron gas, which underpins LDA exchange-correlation in condensed matter, was extended to finite temperature (path-integral and configuration PIMC) to give the warm-dense-matter exchange-correlation free energy, fighting the same fermion sign problem.", "map": "f_{xc}(r_s,\\theta),\\ \\theta=k_BT/E_F;\\ \\theta\\to0:\\ \\epsilon_{xc}(r_s)\\ (\\text{Ceperley-Alder, LDA})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2675", "a": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "b": "10-plasma-physics/magnetic-confinement-fusion/tokamaks", "name": "Nb3Sn and NbTi magnets for tokamaks", "kind": "shared object", "summary": "The toroidal and poloidal field coils of ITER, JT-60SA, EAST and KSTAR are low-temperature type-II superconductors (Nb3Sn, NbTi) whose upper critical field, flux pinning and strain sensitivity set the achievable field and hence confinement.", "map": "B_{c2}(\\text{Nb}_3\\text{Sn})\\approx30\\,\\text{T},\\ B_{c2}(\\text{NbTi})\\approx15\\,\\text{T};\\ \\tau_E\\propto B^{0.15}I_p^{0.93}\\ (\\text{IPB98})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2676", "a": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "Frozen-in flux vs Meissner flux expulsion", "kind": "analogy", "summary": "An ideal-MHD plasma is a perfect conductor in which magnetic flux is frozen into the fluid, whereas a superconductor is more than a perfect conductor: London's equation actively expels flux; the contrast is the standard way to show the Meissner effect is thermodynamic, not just zero resistance.", "map": "\\partial_t\\mathbf B=\\nabla\\times(\\mathbf v\\times\\mathbf B)\\ (\\eta\\to0,\\ \\dot{\\mathbf B}=0\\text{ in a static perfect conductor})\\ \\text{vs}\\ \\nabla\\times\\mathbf J_s=-\\frac{n_se^2}{m}\\mathbf B\\Rightarrow\\mathbf B=0", "breaks": "Ideal MHD has no condensate or gap and keeps whatever flux it started with; a superconductor reaches a unique equilibrium with B=0 inside, set by a macroscopic phase.", "confidence": "established", "strength": 1}
{"id": "C2677", "a": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Photon mass: plasma cutoff and Meissner effect", "kind": "historical", "summary": "Transverse light in a plasma obeys omega^2=omega_p^2+c^2k^2, as if photons had mass hbar*omega_p/c^2; Anderson used this plasma analogy to show that in a superconductor the Goldstone mode is absorbed and the photon becomes massive, giving London penetration depth lambda_L=c/omega_p(n_s), the step that became the Higgs mechanism.", "map": "\\omega^2=\\omega_p^2+c^2k^2\\ (\\text{plasma})\\leftrightarrow\\nabla^2\\mathbf B=\\lambda_L^{-2}\\mathbf B,\\ \\lambda_L=c/\\omega_{p,s}=\\sqrt{m/\\mu_0n_se^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2678", "a": "08-condensed-matter/superconductivity/cuprate-high-tc-superconductors", "b": "10-plasma-physics/magnetic-confinement-fusion/burning-plasmas-and-iter", "name": "REBCO high-temperature superconductors for compact tokamaks", "kind": "shared object", "summary": "Rare-earth barium copper oxide (REBCO) cuprate tapes carry high currents at 20 K and above 20 T, allowing compact high-field tokamaks (SPARC, ARC) because fusion power density scales as B^4 at fixed beta; quench protection and neutron degradation of the cuprate are open engineering problems.", "map": "P_{\\text{fus}}/V\\propto\\beta^2B^4,\\ \\beta=\\frac{2\\mu_0\\langle p\\rangle}{B^2}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2679", "a": "08-condensed-matter/superconductivity/hydride-superconductors-under-pressure", "b": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "name": "Dense hydrogen: superconductors and laser-shock experiments", "kind": "shared object", "summary": "The insulator-metal transition of dense hydrogen and deuterium, the root of the metallic-hydrogen and hydride-superconductor programme, is probed both in diamond-anvil cells and in dynamic compression at NIF and the Z machine; the two disagree on the transition pressure, partly because of temperature and DFT functional choices.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2680", "a": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Band topology of magnetized plasma waves", "kind": "method transfer", "summary": "Chern numbers and bulk-boundary correspondence, developed for electronic bands, classify the wave bands of magnetized cold plasmas; a topological gaseous plasmon polariton is predicted at plasma interfaces with a sign change of B or density.", "map": "C_n=\\frac1{2\\pi}\\int\\Omega_n(\\mathbf k)d^2k\\ \\text{for the Maxwell-fluid eigenproblem }\\omega\\psi=H(\\mathbf k)\\psi", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2681", "a": "08-condensed-matter/topological-matter/quantum-hall-effects", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Guiding-centre drift and the Hall effect", "kind": "identity", "summary": "In crossed E and B fields charged particles drift at E x B / B^2 regardless of charge or mass; in a 2D electron gas this drift gives the classical Hall conductivity, and quantized cyclotron orbits (Landau levels) with skipping orbits at edges become the chiral edge states of the quantum Hall effect.", "map": "\\mathbf v_E=\\frac{\\mathbf E\\times\\mathbf B}{B^2}\\Rightarrow\\sigma_{xy}=\\frac{ne}{B}\\to\\nu\\frac{e^2}{h}\\ (n=\\nu eB/h);\\ \\omega_c=\\frac{eB}{m^*}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2682", "a": "08-condensed-matter/crystals-and-electronic-structure", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Band theory behind semiconductor devices", "kind": "method transfer", "summary": "Bloch bands, effective masses, doping and carrier statistics from solid-state theory are the design language of transistors, LEDs and solar cells; device equations (drift-diffusion, Shockley diode, Shockley-Queisser) are band theory plus non-equilibrium carrier kinetics.", "map": "n=N_ce^{-(E_c-E_F)/k_BT},\\ np=n_i^2\\to I=I_0(e^{qV/k_BT}-1)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2683", "a": "08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons", "b": "11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods", "name": "Tight binding as periodic LCAO / Huckel theory", "kind": "identity", "summary": "The tight-binding band model is the molecular-orbital LCAO (Huckel) method applied to a periodic lattice: graphene's pi bands are the infinite-molecule limit of benzene's Huckel orbitals, and Slater-Koster parameters play the role of resonance integrals.", "map": "E(\\mathbf k)=\\epsilon_0+\\sum_{\\mathbf R}t(\\mathbf R)e^{i\\mathbf k\\cdot\\mathbf R}\\leftrightarrow\\text{H\\\"uckel }E=\\alpha+2\\beta\\cos\\frac{2\\pi j}{N}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2684", "a": "08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons", "b": "11-interdisciplinary-physics/chemical-physics/surface-science-and-catalysis", "name": "STM imaging of the local density of states", "kind": "method transfer", "summary": "STM, developed in surface science, measures the sample's local density of states via tunnelling (Tersoff-Hamann); spectroscopic STM became a core probe of band structure, superconducting gaps, vortex cores and quasiparticle interference in quantum materials.", "map": "\\frac{dI}{dV}\\propto\\rho_s(\\mathbf r_0,E_F+eV),\\ I\\propto Ve^{-2\\kappa d},\\ \\kappa=\\sqrt{2m\\phi}/\\hbar", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2685", "a": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Synchrotron and XFEL light for crystallography", "kind": "method transfer", "summary": "Undulator synchrotron and free-electron-laser X-rays provide the brilliance for structure determination, resonant and inelastic scattering, and femtosecond diffraction of solids; Bragg's law and the structure factor are the analysis framework.", "map": "2d\\sin\\theta=n\\lambda,\\ I_{\\mathbf G}\\propto|S_{\\mathbf G}|^2;\\ \\lambda_{\\text{und}}=\\frac{\\lambda_u}{2\\gamma^2}(1+K^2/2)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2686", "a": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "b": "11-interdisciplinary-physics/applied-and-device-physics/energy-materials-and-thermoelectrics", "name": "Superionic conductors for solid-state batteries", "kind": "mechanism", "summary": "Solid electrolytes such as Li10GeP2S12 are superionic crystals in which a rigid anion framework hosts liquid-like Li-ion diffusion through connected sites; crystal structure and its percolating channels set ionic conductivity.", "map": "\\sigma_{\\text{ion}}T=A\\exp(-E_a/k_BT),\\ D=\\tfrac16\\Gamma\\ell^2", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2687", "a": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "b": "11-interdisciplinary-physics/chemical-physics/surface-science-and-catalysis", "name": "Surface crystallography and reconstruction", "kind": "method transfer", "summary": "Surfaces have their own 2D lattices and reciprocal lattices; low-energy electron diffraction and STM reveal reconstructions such as Si(111) 7x7, extending bulk diffraction theory to the 17 wallpaper groups.", "map": "\\mathbf k_\\parallel'-\\mathbf k_\\parallel=\\mathbf G_\\parallel\\ (\\text{LEED, 2D Laue})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2688", "a": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Mantle and core mineral phases behind seismic structure", "kind": "shared object", "summary": "The post-perovskite transition of MgSiO3, found by high-pressure X-ray diffraction and ab initio theory, explains the D'' seismic discontinuity above the core-mantle boundary, and hcp iron's elastic anisotropy explains inner-core seismic anisotropy.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2689", "a": "08-condensed-matter/crystals-and-electronic-structure/density-functional-theory", "b": "11-interdisciplinary-physics/applied-and-device-physics/energy-materials-and-thermoelectrics", "name": "High-throughput DFT for battery and energy materials", "kind": "method transfer", "summary": "Databases of DFT-computed formation energies, voltages and phase stability (Materials Project and successors), now accelerated by machine-learned potentials, screen cathodes, electrolytes and thermoelectrics before synthesis.", "map": "V=-\\frac{\\mu_{\\text{Li}}^{\\text{cathode}}-\\mu_{\\text{Li}}^{\\text{anode}}}{e}\\approx-\\frac{\\Delta E_{\\text{DFT}}}{e\\,\\Delta x}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2690", "a": "08-condensed-matter/crystals-and-electronic-structure/density-functional-theory", "b": "11-interdisciplinary-physics/chemical-physics", "name": "Chemical physics uses condensed-matter DFT", "kind": "method transfer", "summary": "Chemical physics borrows DFT and periodic electronic-structure methods for spectroscopy, reaction barriers and surface chemistry.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2691", "a": "08-condensed-matter/crystals-and-electronic-structure/density-functional-theory", "b": "11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods", "name": "DFT shared by solid-state and quantum chemistry", "kind": "method transfer", "summary": "Kohn-Sham DFT is the workhorse of both communities; chemistry contributed hybrid and dispersion-corrected functionals (B3LYP, M06, DFT-D) while physics contributed plane-wave pseudopotential codes, and both test against wavefunction methods such as coupled cluster.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2692", "a": "08-condensed-matter/crystals-and-electronic-structure/density-functional-theory", "b": "11-interdisciplinary-physics/chemical-physics/surface-science-and-catalysis", "name": "d-band theory and descriptor-based catalyst design", "kind": "method transfer", "summary": "DFT calculations of adsorption energies on metal surfaces, organized by the position of the d-band centre and linear scaling relations, explain why gold is inert and drive computational screening of catalysts through volcano plots.", "map": "\\Delta E_{\\text{ads}}\\approx\\alpha(\\epsilon_d-E_F)+\\beta;\\ \\Delta E_{AH_x}=\\gamma\\Delta E_A+\\xi\\ (\\text{scaling})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2693", "a": "08-condensed-matter/crystals-and-electronic-structure/density-functional-theory", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Ab initio mineral physics of Earth's deep interior", "kind": "method transfer", "summary": "DFT elastic constants and melting curves of iron alloys and silicates at 100-360 GPa supply the seismic velocities, densities and core temperature that seismology alone cannot fix, at conditions difficult to reach in experiments.", "map": "v_P=\\sqrt{(K+\\tfrac43\\mu)/\\rho},\\ v_S=\\sqrt{\\mu/\\rho},\\ C_{ijkl}=\\frac1V\\frac{\\partial^2E}{\\partial\\epsilon_{ij}\\partial\\epsilon_{kl}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2694", "a": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "b": "11-interdisciplinary-physics/applied-and-device-physics/energy-materials-and-thermoelectrics", "name": "Electronic side of thermoelectrics", "kind": "mechanism", "summary": "The thermoelectric figure of merit depends on the Seebeck coefficient and electrical conductivity from Boltzmann transport (Mott formula) and on the electronic thermal conductivity fixed by Wiedemann-Franz; band engineering optimizes the power factor S^2 sigma.", "map": "ZT=\\frac{S^2\\sigma T}{\\kappa_e+\\kappa_L},\\ S=\\frac{\\pi^2k_B^2T}{3e}\\frac{d\\ln\\sigma(E)}{dE}\\Big|_{E_F},\\ \\kappa_e=L\\sigma T", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2695", "a": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Landauer transport in nanoscale transistors", "kind": "method transfer", "summary": "As MOSFET channels shrink to a few nanometres, current is computed as transmission through modes (Landauer-Buttiker, non-equilibrium Green's functions) rather than drift-diffusion; the ballistic limit gives the conductance quantum per mode.", "map": "I=\\frac{2e}{h}\\int T(E)[f_S(E)-f_D(E)]dE,\\ G_{\\text{ball}}=\\frac{2e^2}{h}M", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2696", "a": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "b": "11-interdisciplinary-physics/applied-and-device-physics/energy-materials-and-thermoelectrics", "name": "Phonon engineering for thermoelectrics", "kind": "mechanism", "summary": "High ZT needs low lattice thermal conductivity: strong anharmonicity, Umklapp and boundary scattering of phonons (as in SnSe and nanostructured bulk) suppress kappa_L without hurting electrons.", "map": "\\kappa_L=\\tfrac13C_Vv\\ell,\\ \\ell^{-1}=\\ell_U^{-1}+\\ell_b^{-1}+\\ell_{\\text{pd}}^{-1}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2697", "a": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Raman and infrared spectroscopy of phonons", "kind": "method transfer", "summary": "Molecular vibrational spectroscopy carries over to crystals, where Raman and IR probe zone-centre optical phonons; in graphene the G and 2D Raman bands count layers, measure strain, doping and electron-phonon coupling.", "map": "\\omega_{\\text{Raman}}=\\omega_{\\mathbf q\\approx0},\\ \\text{selection rules from point-group irreps}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2698", "a": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Polaron hopping and Marcus electron transfer", "kind": "identity", "summary": "Small-polaron hopping in solids (Holstein) and Marcus electron transfer in solution are the same theory: an electron moves between sites when vibrational (phonon) fluctuations bring the two diabatic energies into resonance, with reorganization energy equal to twice the polaron binding energy.", "map": "k=\\frac{2\\pi}{\\hbar}|H_{AB}|^2\\frac{e^{-(\\Delta G^\\circ+\\lambda)^2/4\\lambda k_BT}}{\\sqrt{4\\pi\\lambda k_BT}},\\ \\lambda=2E_p\\ (\\text{Holstein})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2699", "a": "08-condensed-matter/crystals-and-electronic-structure/semiconductors", "b": "11-interdisciplinary-physics/applied-and-device-physics", "name": "Device physics built on semiconductor physics", "kind": "shared object", "summary": "Applied device physics (transistors, photovoltaics, sensors, thermoelectrics) rests on semiconductor band structure, doping and carrier transport.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2700", "a": "08-condensed-matter/crystals-and-electronic-structure/semiconductors", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "NV centres: point defects in a wide-gap semiconductor", "kind": "shared object", "summary": "The nitrogen-vacancy centre is a deep point defect in diamond's 5.5 eV gap whose spin triplet ground state is optically initialized and read out at room temperature, making defect physics of semiconductors the basis of nanoscale quantum sensing.", "map": "H=DS_z^2+\\gamma_e\\mathbf B\\cdot\\mathbf S,\\ D/h\\approx2.87\\,\\text{GHz};\\ \\delta B\\sim\\frac{1}{\\gamma C\\sqrt{T_2t}}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2701", "a": "08-condensed-matter/crystals-and-electronic-structure/semiconductors", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Semiconductor physics and semiconductor devices", "kind": "shared object", "summary": "Doped silicon, III-V and wide-gap semiconductors are one object seen twice: condensed matter supplies gaps, mobilities, recombination and junction physics; device physics turns them into MOSFETs, LEDs, lasers and photovoltaics.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2702", "a": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "b": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "name": "Graphene nanopores for single-molecule sensing", "kind": "method transfer", "summary": "A single graphene layer is thinner than the spacing of DNA bases, so ionic current through a graphene nanopore resolves translocating molecules with sub-nanometre thickness, a step toward solid-state sequencing.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2703", "a": "08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Quantum-dot light emitters and photovoltaics", "kind": "method transfer", "summary": "Size-tuned colloidal and perovskite nanocrystals are used in displays (QLEDs), downconverters and solar cells; confinement sets the emission colour and multiple-exciton generation offers a route past the Shockley-Queisser limit.", "map": "E_g(R)\\approx E_g^{\\text{bulk}}+\\frac{\\hbar^2\\pi^2}{2R^2}\\left(\\frac1{m_e^*}+\\frac1{m_h^*}\\right)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2704", "a": "08-condensed-matter/low-dimensional-and-quantum-materials/transition-metal-dichalcogenides-and-excitons", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Two-dimensional semiconductor channels for transistors", "kind": "method transfer", "summary": "Monolayer MoS2 and related TMDs provide atomically thin channels with sizeable gaps, immune to short-channel effects that limit silicon scaling; contact resistance and dielectric integration are the open device problems.", "map": "\\lambda_{\\text{scale}}=\\sqrt{\\frac{\\epsilon_{ch}}{\\epsilon_{ox}}t_{ch}t_{ox}},\\ t_{ch}\\approx0.65\\,\\text{nm}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2705", "a": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "NV magnetometry imaging of 2D magnets", "kind": "method transfer", "summary": "Scanning single-spin (NV) magnetometry images stray fields of atomically thin magnets such as CrI3 quantitatively, resolving layer-dependent magnetization and domains; it is now a standard probe of 2D magnetism and spin textures.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2706", "a": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Crackling noise: Barkhausen jumps and earthquakes", "kind": "analogy", "summary": "Barkhausen noise from domain-wall avalanches in ferromagnets and earthquakes on faults both show power-law size distributions explained by depinning of an elastic interface in a random medium, the 'crackling noise' universality family.", "map": "P(S)\\sim S^{-\\tau}\\ (\\text{Barkhausen }\\tau\\approx1.3\\text{-}1.5)\\leftrightarrow N(>M)\\propto10^{-bM}\\ (\\text{Gutenberg-Richter},\\ b\\approx1)", "breaks": "Fault systems have long-range elastic interactions, healing and inertia that can produce characteristic quakes; universality-class assignments and exponents differ, and magnetic avalanches are tuned by an external field rather than tectonic loading.", "confidence": "established", "strength": 2}
{"id": "C2707", "a": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Rock magnetism and the paleomagnetic record", "kind": "mechanism", "summary": "Remanent magnetization of magnetite-bearing rocks, explained by Neel's theory of thermally activated single-domain grains, records the geomagnetic field; stripes of reversed magnetization on the sea floor confirmed sea-floor spreading and plate tectonics.", "map": "\\tau=\\tau_0\\exp\\left(\\frac{K_uV}{k_BT}\\right)\\ (\\text{Neel relaxation, blocking temperature})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2708", "a": "08-condensed-matter/magnetism/spintronics", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Spintronic memory and read heads in electronics", "kind": "method transfer", "summary": "Giant and tunnelling magnetoresistance moved from discovery to hard-disk read heads within a decade, and spin-transfer-torque MRAM is now embedded in CMOS logic processes as non-volatile memory.", "map": "\\text{TMR}=\\frac{2P_1P_2}{1-P_1P_2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2709", "a": "08-condensed-matter/soft-matter", "b": "11-interdisciplinary-physics/biophysics", "name": "Soft-matter physics of biological materials", "kind": "mechanism", "summary": "Membranes, biopolymers, gels and cytoskeletal networks have energies of order k_BT, so entropic elasticity, fluctuations, self-assembly and viscoelasticity, the core of soft matter, set the mechanics of cells and biomolecules.", "map": "k_BT\\approx4.1\\,\\text{pN nm}\\ (300\\,\\text{K})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2710", "a": "08-condensed-matter/soft-matter/active-matter", "b": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "name": "Cells and tissues as active matter", "kind": "mechanism", "summary": "The actomyosin cortex and epithelial tissues are active gels and active nematics; topological defects in epithelial monolayers localize stress and trigger cell extrusion, the same +1/2 defect physics as in microtubule active nematics.", "map": "\\sigma^{\\text{act}}_{ij}=-\\zeta\\Delta\\mu\\,Q_{ij},\\ Q_{ij}=S(n_in_j-\\tfrac12\\delta_{ij})", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2711", "a": "08-condensed-matter/soft-matter/active-matter", "b": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "name": "Flocking theory and collective animal behaviour", "kind": "mechanism", "summary": "Vicsek and Toner-Tu theories of polar active matter describe starling flocks, fish schools and bacterial swarms; field data showing starlings interact with a fixed number of topological neighbours fed back into active-matter models.", "map": "\\theta_i(t+1)=\\langle\\theta_j\\rangle_{j\\in\\mathcal N_i}+\\eta_i,\\ |\\mathcal N_i|\\approx6\\text{-}7\\ (\\text{topological})", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2712", "a": "08-condensed-matter/soft-matter/colloids-and-granular-matter", "b": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "name": "Brownian colloids as force probes", "kind": "method transfer", "summary": "Optical and magnetic tweezers are calibrated by the Brownian motion of a trapped colloidal bead: equipartition and the Lorentzian power spectrum with Stokes drag give the trap stiffness that turns position into force.", "map": "\\kappa\\langle x^2\\rangle=k_BT,\\ S_x(f)=\\frac{k_BT}{\\pi^2\\gamma(f_c^2+f^2)},\\ \\gamma=6\\pi\\eta a,\\ f_c=\\frac{\\kappa}{2\\pi\\gamma}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2713", "a": "08-condensed-matter/soft-matter/colloids-and-granular-matter", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Granular friction and earthquake faults", "kind": "mechanism", "summary": "Fault gouge is a sheared granular layer: rate-and-state friction, stick-slip instability, dilatancy and shear localization measured on granular materials explain earthquake nucleation and aftershock behaviour.", "map": "\\mu=\\mu_0+a\\ln\\frac{V}{V_0}+b\\ln\\frac{V_0\\theta}{D_c};\\ a-b<0\\Rightarrow\\text{stick-slip}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2714", "a": "08-condensed-matter/soft-matter/glasses-and-jamming", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Phase-change glasses for non-volatile memory", "kind": "mechanism", "summary": "Chalcogenide glasses such as Ge2Sb2Te5 switch in nanoseconds between amorphous and crystalline states with very different resistivity and reflectivity; crystallization kinetics and glass stability are the device physics of phase-change memory.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2715", "a": "08-condensed-matter/soft-matter/glasses-and-jamming", "b": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "name": "Jamming and unjamming of biological tissues", "kind": "mechanism", "summary": "Confluent epithelia undergo a rigidity (jamming) transition controlled by cell shape rather than density, analogous to athermal jamming; unjammed, fluid-like tissue is linked to wound healing, asthma and cancer invasion.", "map": "q=\\frac{P}{\\sqrt A},\\ q^*\\approx3.81\\ (\\text{vertex model rigidity});\\ \\text{jamming: }z_c=2d", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2716", "a": "08-condensed-matter/soft-matter/glasses-and-jamming", "b": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "name": "Rugged energy landscapes: glasses and protein folding", "kind": "method transfer", "summary": "Random-energy and spin-glass landscape ideas developed for glass formers were applied to proteins, giving the folding funnel and the principle of minimal frustration: foldable sequences have a folding temperature well above their glass temperature.", "map": "\\frac{T_f}{T_g}\\gg1\\ (\\text{foldable});\\ T_g\\ \\text{from REM: }S_c(T_g)=0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2717", "a": "08-condensed-matter/soft-matter/liquid-crystals", "b": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "name": "Helfrich elasticity: from liquid crystals to membranes", "kind": "historical", "summary": "Lipid bilayers are two-dimensional smectic-A liquid crystals; Helfrich, co-inventor of the twisted-nematic display, transferred Frank curvature elasticity to membranes, giving the bending energy that predicts red-blood-cell shapes and vesicle fluctuations.", "map": "F_{\\text{Frank}}\\ni\\tfrac12K_1(\\nabla\\cdot\\mathbf n)^2\\to F_{\\text{Helfrich}}=\\oint\\left[\\tfrac\\kappa2(2H-c_0)^2+\\bar\\kappa K\\right]dA,\\ 2H=\\nabla\\cdot\\mathbf n", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2718", "a": "08-condensed-matter/soft-matter/polymers", "b": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "name": "Proteins and nucleic acids as polymers", "kind": "mechanism", "summary": "Polymer physics (random walks, excluded volume, theta collapse, persistence length) gives the baseline for unfolded proteins and DNA; folding is a heteropolymer collapse with sequence-specific interactions.", "map": "R_g\\sim bN^{\\nu},\\ \\nu\\approx0.588\\ (\\text{good solvent, denatured})\\to\\nu=1/3\\ (\\text{compact globule})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2719", "a": "08-condensed-matter/soft-matter/polymers", "b": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "name": "Flory-Huggins phase separation and biomolecular condensates", "kind": "mechanism", "summary": "Membraneless organelles (P granules, nucleoli, stress granules) form by liquid-liquid phase separation of multivalent proteins and RNA, described with Flory-Huggins polymer-solution theory and its sticker-spacer extensions.", "map": "\\frac{\\Delta F_{\\text{mix}}}{k_BT}=\\frac\\phi N\\ln\\phi+(1-\\phi)\\ln(1-\\phi)+\\chi\\phi(1-\\phi),\\ \\chi_c=\\tfrac12(1+N^{-1/2})^2", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2720", "a": "08-condensed-matter/soft-matter/polymers", "b": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "name": "Worm-like chain elasticity of single DNA molecules", "kind": "identity", "summary": "Force-extension curves of single DNA molecules in optical and magnetic tweezers are fitted by the worm-like-chain model of semiflexible polymers, giving a 50 nm persistence length and confirming entropic elasticity at the single-molecule level.", "map": "F=\\frac{k_BT}{P}\\left[\\frac{1}{4(1-x/L)^2}-\\frac14+\\frac xL\\right],\\ P\\approx50\\,\\text{nm}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2721", "a": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "b": "11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods", "name": "DMRG, QMC and coupled cluster across fields", "kind": "method transfer", "summary": "DMRG, invented for 1D spin chains, became a leading method for strongly correlated molecules (active spaces of transition-metal clusters), while coupled cluster and quantum Monte Carlo moved from nuclear and quantum chemistry into solids; agreement across methods is the benchmark standard in both fields.", "map": "|\\psi\\rangle=\\sum\\mathrm{Tr}(A^{s_1}\\cdots A^{s_N})|s_1\\cdots s_N\\rangle\\ (\\text{orbitals as sites});\\ |\\Psi_{CC}\\rangle=e^{\\hat T}|\\Phi_0\\rangle", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2722", "a": "08-condensed-matter/superconductivity", "b": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "name": "Superconductors in accelerators", "kind": "method transfer", "summary": "Accelerators are the largest users of applied superconductivity: NbTi and Nb3Sn dipoles and quadrupoles bend and focus beams, and superconducting niobium RF cavities provide high-gradient, low-loss acceleration.", "map": "B\\rho\\,[\\text{T m}]=3.3356\\,p\\,[\\text{GeV}/c];\\ Q_0=\\omega U/P_{\\text{loss}}\\sim10^{10}\\text{-}10^{11}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2723", "a": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "b": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "name": "BCS surface resistance of SRF cavities", "kind": "mechanism", "summary": "Niobium superconducting RF cavities are limited by the BCS surface resistance from thermally excited quasiparticles, plus residual losses from trapped flux; nitrogen doping and Nb3Sn coatings are gap-engineering responses that raise Q0 and gradient.", "map": "R_s^{\\text{BCS}}\\approx\\frac{A\\omega^2}{T}e^{-\\Delta/k_BT}+R_{\\text{res}},\\ \\Delta_{\\text{Nb}}\\approx1.5\\,\\text{meV};\\ Q_0=G/R_s", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2724", "a": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Superconducting magnets for MRI", "kind": "shared object", "summary": "Clinical MRI scanners use persistent-mode NbTi solenoids at 1.5-7 T; type-II superconductivity with strong flux pinning gives the stable, homogeneous field whose Larmor frequency sets image signal and resolution.", "map": "\\omega_0=\\gamma B_0,\\ \\gamma/2\\pi=42.58\\,\\text{MHz/T};\\ \\text{SNR}\\propto B_0^{\\sim1}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2725", "a": "08-condensed-matter/superconductivity/cuprate-high-tc-superconductors", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Resonant inelastic X-ray scattering of cuprates", "kind": "method transfer", "summary": "High-resolution RIXS at synchrotrons measures paramagnons and charge-density-wave correlations in cuprates; it revealed incommensurate charge order competing with superconductivity in YBCO.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2726", "a": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "SQUID magnetometry", "kind": "method transfer", "summary": "SQUIDs turn flux quantization and Josephson interference into femtotesla magnetometers used for magnetoencephalography, geophysics, rock magnetism and condensed-matter susceptibility measurements.", "map": "I_c(\\Phi)=2I_0\\left|\\cos\\frac{\\pi\\Phi}{\\Phi_0}\\right|,\\ \\Phi_0=h/2e;\\ \\delta B\\sim\\text{fT}/\\sqrt{\\text{Hz}}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2727", "a": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Topological origin of equatorial waves", "kind": "method transfer", "summary": "Applying Chern-number band topology to the rotating shallow-water equations shows that the equatorial Kelvin and Yanai waves are topologically protected edge modes forced by the sign change of the Coriolis parameter at the equator.", "map": "\\text{Coriolis }f=\\beta y\\leftrightarrow\\text{Dirac mass }m(y);\\ C_\\pm=\\pm1\\Rightarrow\\Delta C=2\\ \\text{equatorial modes}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2728", "a": "08-condensed-matter/topological-matter/topological-insulators", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Synchrotron ARPES of topological surface states", "kind": "method transfer", "summary": "Spin- and angle-resolved photoemission with tunable synchrotron light identified the odd number of spin-momentum-locked surface Dirac cones that define 3D topological insulators, and later Fermi arcs in Weyl semimetals.", "map": "E_{\\text{kin}}=h\\nu-\\phi-|E_B|,\\ k_\\parallel=\\sqrt{2mE_{\\text{kin}}}\\sin\\theta/\\hbar", "breaks": "", "confidence": "established", "strength": 2}