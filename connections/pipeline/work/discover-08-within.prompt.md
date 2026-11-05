# Discovery brief (one set per run)

You map every genuine connection in one *set* of this physics knowledge base. A set is two fields, `A-B`, or one field's *within* links: notes in different subfields of field A. The material for your set is below this brief, already extracted for you:
- the nodes, with one-line summaries;
- explicit cross-links already written in the notes;
- shared curated concepts;
- latent candidate pairs;
- shared papers.

## Steps
1. Work from the material below and your own physics knowledge. Do not run commands or search the folder.
2. Read at most 3 node READMEs (`knowledge/<path>/README.md`), and only where a connection's physics genuinely needs checking. Most runs need none.
3. **Answer** with JSON Lines ONLY: one JSON object per line. No prose, no headings, no code fences. Anything else in your answer is discarded.

## What counts
Include every connection a specialist in either field would recognise as real and non-trivial:
- the same equation or mathematical structure;
- the same mechanism;
- a method, algorithm or instrument that moved across;
- a system both fields study;
- an idea that migrated historically;
- an analogy, with where it breaks.

Exclude generic overlap ("both use differential equations"). Each explicit cross-link in the material becomes a record with `"status": "written"`; everything else is `"new"`. Aim for 12–40 records: dense pairs more, distant pairs fewer, within-field 15–35. Use the most specific nodes (topic over subfield).

## Record schema
`{"a": "<node path, e.g. 08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors>", "b": "<node path>", "name": "<≤60 chars>", "kind": "identity|mechanism|analogy|duality|method transfer|shared object|historical", "status": "written|new", "summary": "<1–2 sentences, ≤45 words: what is shared and how it maps>", "map": "<optional LaTeX of the shared equation or symbol map, ≤200 chars; in JSON write a LaTeX backslash twice, e.g. \\Delta>", "breaks": "<where it fails; required for analogy>", "confidence": "established|current research|proposed", "strength": 3|2|1, "sources": []}`

- **Strength:** 3 = deep or structural, 2 = substantial, 1 = suggestive.
- **Sources:** optional, at most 2 per record, only from a README you read, in the format `Author (Year). \"Exact title\". *Venue* vol, page. [doi:…](https://doi.org/…)`. Citations are verified centrally afterwards.


---

# Your set: 08-within (links between different subfields of Condensed Matter Physics)

## Nodes (43)
- 08-condensed-matter | The physics of solids, liquids and quantum materials — electronic structure, superconductivity, magnetism, strong correlations, topological matter, 2D
- 08-condensed-matter/crystals-and-electronic-structure | Periodic solids and their electrons — crystal lattices and diffraction, band theory, phonons, semiconductors, density functional theory, and electroni
- 08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons | Electrons in periodic potentials — Bloch's theorem, nearly-free-electron and tight-binding models, band gaps, effective mass, Fermi surfaces.
- 08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction | Bravais lattices, unit cells, reciprocal lattices and Brillouin zones; X-ray, electron and neutron diffraction; quasicrystals.
- 08-condensed-matter/crystals-and-electronic-structure/density-functional-theory | First-principles electronic structure from the electron density — Hohenberg–Kohn theorems, Kohn–Sham equations, exchange–correlation functionals and t
- 08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics | How electrons carry current — Drude and Boltzmann transport, Hall effect, Landauer–Büttiker formalism, quantized conductance, weak localization and sh
- 08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics | Quantized lattice vibrations — dispersion relations, acoustic and optical branches, heat capacity, thermal transport, anharmonicity and electron–phono
- 08-condensed-matter/crystals-and-electronic-structure/semiconductors | Intrinsic and doped semiconductors, carrier statistics, recombination, p–n junctions, heterostructures and the physics behind transistors and LEDs.
- 08-condensed-matter/low-dimensional-and-quantum-materials | Atomically thin and nanoscale materials — graphene and 2D crystals, moiré superlattices and twisted bilayers, transition-metal dichalcogenides and exc
- 08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials | Atomically thin crystals — graphene's Dirac electrons, hexagonal boron nitride, van der Waals heterostructures and the wider family of 2D materials.
- 08-condensed-matter/low-dimensional-and-quantum-materials/moire-materials-and-twisted-bilayers | Superlattices from twisted or lattice-mismatched layers — magic-angle graphene, flat bands, correlated insulators, superconductivity and fractional Ch
- 08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures | Electrons confined in zero and one dimension — gate-defined and self-assembled quantum dots, colloidal nanocrystals, nanowires, Coulomb blockade and s
- 08-condensed-matter/low-dimensional-and-quantum-materials/transition-metal-dichalcogenides-and-excitons | Monolayer semiconductors like MoS₂ and WSe₂ — direct gaps, spin–valley locking, tightly bound excitons, interlayer excitons and exciton condensates.
- 08-condensed-matter/magnetism | Magnetic order in solids — exchange interactions, ferro- and antiferromagnetism, spintronics, frustration and spin liquids, skyrmions and altermagnets
- 08-condensed-matter/magnetism/altermagnetism | A third class of collinear magnets — zero net magnetization like antiferromagnets, but spin-split bands like ferromagnets, set by crystal symmetry.
- 08-condensed-matter/magnetism/exchange-and-magnetic-order | Direct, super- and RKKY exchange, Heisenberg and Ising models, ferro-, antiferro- and ferrimagnetism, domains, magnons and neutron scattering.
- 08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids | Magnets whose interactions cannot all be satisfied — spin ice, kagome and triangular antiferromagnets, resonating valence bonds, Kitaev materials and 
- 08-condensed-matter/magnetism/magnetic-skyrmions-and-textures | Topological spin textures — skyrmions, merons, hopfions — stabilized by Dzyaloshinskii–Moriya interaction; dynamics and device applications.
- 08-condensed-matter/magnetism/spintronics | Using electron spin in devices — giant and tunnelling magnetoresistance, spin-transfer and spin–orbit torques, spin Hall effects and magnonics.
- 08-condensed-matter/soft-matter | Materials easily deformed by thermal fluctuations — polymers, liquid crystals, colloids and granular media, active matter, glasses and jamming.
- 08-condensed-matter/soft-matter/active-matter | Systems of self-propelled units that consume energy — flocking, motility-induced phase separation, active nematics, living and synthetic active materi
- 08-condensed-matter/soft-matter/colloids-and-granular-matter | Micron-scale particles in fluids and athermal grains — Brownian motion, DLVO and depletion forces, colloidal crystals, granular packing, flow and forc
- 08-condensed-matter/soft-matter/glasses-and-jamming | Amorphous solids — supercooled liquids, the glass transition, dynamical heterogeneity, aging, and the jamming transition of athermal packings.
- 08-condensed-matter/soft-matter/liquid-crystals | Fluids with orientational order — nematics, smectics and cholesterics, the Frank elastic theory, topological defects, active nematics and display tech
- 08-condensed-matter/soft-matter/polymers | Long-chain molecules — random walks and excluded volume, Flory theory, scaling, rubber elasticity, entanglement and reptation, polymer solutions and g
- 08-condensed-matter/strongly-correlated-electrons | Electrons whose interactions dominate — Mott insulators and the Hubbard model, Kondo physics and heavy fermions, quantum criticality, topological orde
- 08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order | Phases beyond symmetry breaking — topological ground-state degeneracy, anyons, long-range entanglement, and their use for fault-tolerant quantum compu
- 08-condensed-matter/strongly-correlated-electrons/heavy-fermions-and-kondo-physics | Magnetic impurities and lattices of local moments in metals — the Kondo effect, heavy-fermion metals with enormous effective masses, and Kondo breakdo
- 08-condensed-matter/strongly-correlated-electrons/hubbard-model-and-mott-physics | The Hubbard model, Mott metal–insulator transitions, superexchange antiferromagnetism and the doped Mott insulator.
- 08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods | Computational tools for correlated quantum matter — exact diagonalization, quantum Monte Carlo, DMRG and tensor networks, DMFT, and neural-network sta
- 08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals | Continuous phase transitions at zero temperature, quantum critical fans, non-Fermi liquids and the linear-in-temperature resistivity of strange metals
- 08-condensed-matter/superconductivity | Zero resistance and perfect diamagnetism — BCS theory, cuprate, iron-based and nickelate superconductors, hydrides under pressure, Josephson physics.
- 08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors | Cooper pairing, the BCS ground state and gap, the Meissner effect, London and Ginzburg–Landau theories, type-I and type-II superconductors.
- 08-condensed-matter/superconductivity/cuprate-high-tc-superconductors | Copper-oxide superconductors — doped Mott insulators, d-wave pairing, the pseudogap, charge order and the strange-metal normal state.
- 08-condensed-matter/superconductivity/hydride-superconductors-under-pressure | Hydrogen-rich compounds superconducting near room temperature at megabar pressures — H₃S, LaH₁₀, predictions, measurement challenges and retracted cla
- 08-condensed-matter/superconductivity/iron-based-and-nickelate-superconductors | Iron pnictides and chalcogenides with multi-band s± pairing, and nickelates — infinite-layer thin films and high-pressure Ruddlesden–Popper phases nea
- 08-condensed-matter/superconductivity/josephson-effect-and-squids | Cooper-pair tunnelling between superconductors — DC and AC Josephson effects, flux quantization, SQUID magnetometers and voltage standards.
- 08-condensed-matter/topological-matter | Phases of matter classified by topology — quantum Hall effects, topological insulators and semimetals, topological superconductors and Majorana modes,
- 08-condensed-matter/topological-matter/band-topology-and-berry-curvature | Geometric and topological properties of Bloch bands — Berry connection and curvature, Chern and Z₂ invariants, the tenfold way, and topological quantu
- 08-condensed-matter/topological-matter/quantum-hall-effects | Quantized Hall conductance in 2D electron systems — integer and fractional quantum Hall effects, edge states, and the anomalous quantum Hall effect wi
- 08-condensed-matter/topological-matter/topological-insulators | Insulators with protected metallic boundaries — the quantum spin Hall effect, 3D topological insulators, Z₂ invariants and surface Dirac fermions.
- 08-condensed-matter/topological-matter/topological-semimetals | Gapless topological phases — Weyl and Dirac semimetals, Fermi arcs, chiral anomaly in solids, and nodal-line semimetals.
- 08-condensed-matter/topological-matter/topological-superconductors-and-majoranas | Superconductors with topological order in their quasiparticle bands — the Kitaev chain, Majorana zero modes in nanowires and vortices, braiding and to

## Explicit cross-links already written in the notes (24): each becomes a "written" record
- 08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons -> 08-condensed-matter/topological-matter/band-topology-and-berry-curvature
- 08-condensed-matter/crystals-and-electronic-structure/density-functional-theory -> 08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods
- 08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics -> 08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors
- 08-condensed-matter/crystals-and-electronic-structure/semiconductors -> 08-condensed-matter/low-dimensional-and-quantum-materials/transition-metal-dichalcogenides-and-excitons
- 08-condensed-matter/low-dimensional-and-quantum-materials -> 08-condensed-matter/topological-matter
- 08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials -> 08-condensed-matter/topological-matter/quantum-hall-effects
- 08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials -> 08-condensed-matter/topological-matter/topological-semimetals
- 08-condensed-matter/low-dimensional-and-quantum-materials/moire-materials-and-twisted-bilayers -> 08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order
- 08-condensed-matter/low-dimensional-and-quantum-materials/moire-materials-and-twisted-bilayers -> 08-condensed-matter/strongly-correlated-electrons/hubbard-model-and-mott-physics
- 08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures -> 08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics
- 08-condensed-matter/low-dimensional-and-quantum-materials/transition-metal-dichalcogenides-and-excitons -> 08-condensed-matter/crystals-and-electronic-structure/semiconductors
- 08-condensed-matter/magnetism/exchange-and-magnetic-order -> 08-condensed-matter/strongly-correlated-electrons/hubbard-model-and-mott-physics
- 08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids -> 08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order
- 08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order -> 08-condensed-matter/topological-matter/quantum-hall-effects
- 08-condensed-matter/strongly-correlated-electrons/heavy-fermions-and-kondo-physics -> 08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures
- 08-condensed-matter/strongly-correlated-electrons/hubbard-model-and-mott-physics -> 08-condensed-matter/superconductivity/cuprate-high-tc-superconductors
- 08-condensed-matter/superconductivity/cuprate-high-tc-superconductors -> 08-condensed-matter/strongly-correlated-electrons/hubbard-model-and-mott-physics
- 08-condensed-matter/superconductivity/cuprate-high-tc-superconductors -> 08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals
- 08-condensed-matter/superconductivity/hydride-superconductors-under-pressure -> 08-condensed-matter/crystals-and-electronic-structure/density-functional-theory
- 08-condensed-matter/superconductivity/hydride-superconductors-under-pressure -> 08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics
- 08-condensed-matter/topological-matter/quantum-hall-effects -> 08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order
- 08-condensed-matter/topological-matter/topological-semimetals -> 08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials
- 08-condensed-matter/topological-matter/topological-superconductors-and-majoranas -> 08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures
- 08-condensed-matter/topological-matter/topological-superconductors-and-majoranas -> 08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order

## Shared curated concepts (31)
- Anomalies: A classical symmetry broken by quantization; links particle physics to topological matter
- Anyons and fractional statistics: Exchange statistics beyond bosons and fermions in two dimensions
- Berry and geometric phases: Holonomy of a state transported around a loop in parameter space
- Bose–Einstein condensation and superfluidity: Macroscopic occupation of one quantum state — cold atoms, helium, neutron stars, superconductors
- Chaos and nonlinear dynamics: Deterministic unpredictability; ergodicity as the bridge to statistical mechanics
- Decoherence and open quantum systems: How environments make quantum systems look classical
- Density functional methods: Ground-state properties from the density alone — electrons, nuclei, classical fluids
- Diffusion, Brownian motion and stochastic processes: Random microscopic kicks produce universal macroscopic laws
- Dirac, Weyl and Majorana fermions: Relativistic wave equations reappear as emergent low-energy physics in solids
- Discrete symmetries: P, T, C and their violations constrain dynamics from nuclei to topological insulators
- Disorder and localization: Interference in random media halts transport — electrons, light, sound, cold atoms
- Entanglement: Correlations without a classical description; organizes many-body states and spacetime
- Entropy and information: Entropy as missing information, from heat engines to black holes and qubits
- Fermi surfaces and degenerate matter: Pauli blocking sets the low-energy physics of electrons, nucleons and compact stars
- Gauge symmetry: Redundancy of description that fixes the form of interactions
- Glasses, spin glasses and rugged landscapes: Many competing minima — glasses, proteins, optimization, neural networks
- Hydrodynamics and continuum descriptions: Long-wavelength dynamics of conserved densities — from water to quark–gluon plasma
- Interference and diffraction: Phase-sensitive superposition, used from crystallography to gravitational-wave detection
- Ising and lattice models: Minimal models whose behavior is universal across physics and beyond
- Lasers, coherence and stimulated emission: Phase-coherent light from stimulated emission; coherence as an order parameter
- Magnetism and exchange: Quantum exchange produces collective magnetic order
- Mean-field and self-consistent theories: Replace fluctuating neighbours by their average; exact in high dimension or large N
- Pairing and BCS physics: Attractive interactions pair fermions and open a gap — metals, nuclei, neutron stars, cold atoms
- Phase transitions and criticality: Non-analytic change of state; fluctuations at all scales near criticality
- Plasma oscillations, screening and Landau damping: Collective long-range Coulomb physics in plasmas, metals and quark matter
- Quasiparticles and collective modes: Interacting systems behave like gases of emergent particles
- Spin and angular momentum: Rotational structure and its coupling to motion and fields
- Spontaneous symmetry breaking: A ground state with less symmetry than the laws; gapless Goldstone modes or, with gauge fields, massive ones
- Topological defects: Order-parameter singularities classified by homotopy — from liquid crystals to the early universe
- Topological invariants: Integer-valued properties robust to smooth deformation
- Tunnelling and instantons: Classically forbidden transitions dominated by Euclidean saddle points

## Latent candidate pairs (14)
- 08-condensed-matter/low-dimensional-and-quantum-materials/transition-metal-dichalcogenides-and-excitons <-> 08-condensed-matter/magnetism/spintronics (score 0.61; shares Quasiparticles and collective modes, Spin and angular momentum, Bose–Einstein condensation and superfluidity)
- 08-condensed-matter/low-dimensional-and-quantum-materials/moire-materials-and-twisted-bilayers <-> 08-condensed-matter/topological-matter/quantum-hall-effects (score 0.60; shares Anomalies, Disorder and localization, Topological invariants)
- 08-condensed-matter/crystals-and-electronic-structure <-> 08-condensed-matter/magnetism/exchange-and-magnetic-order (score 0.50; shares Ising and lattice models, Mean-field and self-consistent theories, Quasiparticles and collective modes)
- 08-condensed-matter/magnetism <-> 08-condensed-matter/topological-matter/topological-superconductors-and-majoranas (score 0.45; shares Anyons and fractional statistics, Topological defects, Quasiparticles and collective modes)
- 08-condensed-matter/crystals-and-electronic-structure <-> 08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order (score 0.43; shares Ising and lattice models, Entropy and information, Quasiparticles and collective modes, Interference and diffraction)
- 08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids <-> 08-condensed-matter/soft-matter/liquid-crystals (score 0.42; shares Spontaneous symmetry breaking, Topological invariants, Topological defects)
- 08-condensed-matter/magnetism/magnetic-skyrmions-and-textures <-> 08-condensed-matter/topological-matter (score 0.42; shares Berry and geometric phases, Topological invariants, Topological defects)
- 08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids <-> 08-condensed-matter/topological-matter/topological-superconductors-and-majoranas (score 0.41; shares Dirac, Weyl and Majorana fermions, Topological invariants, Topological defects)
- 08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids <-> 08-condensed-matter/topological-matter/topological-semimetals (score 0.41; shares Dirac, Weyl and Majorana fermions, Topological invariants, Topological defects)
- 08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors <-> 08-condensed-matter/topological-matter/topological-superconductors-and-majoranas (score 0.38; shares Pairing and BCS physics, Topological defects, Quasiparticles and collective modes)
- 08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics <-> 08-condensed-matter/soft-matter (score 0.36; shares Hydrodynamics and continuum descriptions, Entropy and information, Diffusion, Brownian motion and stochastic processes)
- 08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order <-> 08-condensed-matter/superconductivity (score 0.35; shares Spontaneous symmetry breaking, Quasiparticles and collective modes, Interference and diffraction)
- 08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids <-> 08-condensed-matter/topological-matter (score 0.35; shares Dirac, Weyl and Majorana fermions, Topological invariants, Topological defects)
- 08-condensed-matter/strongly-correlated-electrons <-> 08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors (score 0.29; shares Fermi surfaces and degenerate matter, Mean-field and self-consistent theories, Bose–Einstein condensation and superfluidity)

## Shared papers (0 note pairs; algorithmic, weak evidence)