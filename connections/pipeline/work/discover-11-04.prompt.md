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

# Your set: 11-04 (Interdisciplinary and Applied Physics with Quantum Physics)

## Nodes (71)
- 04-quantum-physics | Quantum mechanics and its descendants — formalism and methods, foundations, atomic/molecular/optical physics, quantum optics, quantum information, and
- 04-quantum-physics/atomic-molecular-and-optical-physics | Structure of atoms and molecules, their interaction with light, laser cooling, quantum gases, optical lattices and precision measurement.
- 04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement | Optical lattice and ion clocks, atom interferometry and precision tests of fundamental physics.
- 04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy | Energy levels of atoms — fine and hyperfine structure, QED corrections, selection rules and spectroscopic techniques.
- 04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases | Macroscopic occupation of a single quantum state in dilute atomic gases, superfluidity, and degenerate Fermi gases.
- 04-quantum-physics/atomic-molecular-and-optical-physics/laser-cooling-and-trapping | Using light to slow, cool and confine atoms and particles — Doppler and sub-Doppler cooling, magneto-optical traps, optical tweezers.
- 04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation | Atoms in periodic light potentials as programmable many-body systems — Hubbard models, quantum gas microscopes and analog quantum simulators.
- 04-quantum-physics/atomic-molecular-and-optical-physics/ultracold-molecules | Cooling and controlling molecules — polar molecules, ultracold chemistry, and precision tests such as electron EDM searches.
- 04-quantum-physics/foundations-of-quantum-mechanics | What quantum mechanics says about reality — the measurement problem, interpretations, Bell nonlocality, contextuality and decoherence.
- 04-quantum-physics/foundations-of-quantum-mechanics/bell-nonlocality | Bell's theorem, CHSH inequalities, loophole-free experimental tests and device-independent applications.
- 04-quantum-physics/foundations-of-quantum-mechanics/contextuality | The impossibility of assigning measurement outcomes independent of measurement context — Kochen–Specker theorem and its uses.
- 04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical | How interaction with an environment suppresses interference and selects classical pointer states.
- 04-quantum-physics/foundations-of-quantum-mechanics/measurement-problem-and-interpretations | Why measurements have definite outcomes — Copenhagen, many-worlds, Bohmian mechanics, objective collapse, QBism and relational views.
- 04-quantum-physics/open-and-many-body-quantum-dynamics | Quantum systems coupled to environments or with many interacting parts — master equations, quantum thermodynamics, thermalization, chaos, non-Hermitia
- 04-quantum-physics/open-and-many-body-quantum-dynamics/floquet-systems-and-time-crystals | Periodically driven quantum systems, Floquet engineering of band structures, and discrete time-crystalline order.
- 04-quantum-physics/open-and-many-body-quantum-dynamics/lindblad-master-equations | Markovian dynamics of open quantum systems, quantum trajectories and dissipative state engineering.
- 04-quantum-physics/open-and-many-body-quantum-dynamics/non-hermitian-physics | Effective non-Hermitian Hamiltonians for gain and loss — PT symmetry, exceptional points and the non-Hermitian skin effect.
- 04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling | Signatures of chaos in quantum systems — random-matrix level statistics, out-of-time-order correlators, the chaos bound and black-hole analogies.
- 04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-thermodynamics | Work, heat and entropy for quantum systems; quantum heat engines, resource theories and fluctuation relations.
- 04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth | How isolated quantum systems reach thermal equilibrium, and when they don't — ETH, integrability, many-body localization and scars.
- 04-quantum-physics/quantum-information-and-computation | Information processing with quantum systems — entanglement theory, algorithms, error correction, hardware platforms and quantum communication.
- 04-quantum-physics/quantum-information-and-computation/entanglement-theory | Characterizing, quantifying and manipulating entanglement — separability, entanglement measures, monogamy and entanglement entropy.
- 04-quantum-physics/quantum-information-and-computation/photonic-and-spin-qubits | Qubits encoded in photons (linear-optical and measurement-based schemes) and in electron or nuclear spins in semiconductors and color centers.
- 04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity | What quantum computers can compute efficiently — Shor, Grover, quantum simulation, variational methods, BQP and quantum-advantage experiments.
- 04-quantum-physics/quantum-information-and-computation/quantum-communication-and-cryptography | Quantum key distribution, teleportation, quantum repeaters and the quantum internet.
- 04-quantum-physics/quantum-information-and-computation/quantum-error-correction-and-fault-tolerance | Protecting quantum information from noise — stabilizer codes, the surface code, thresholds, decoders and logical-qubit experiments.
- 04-quantum-physics/quantum-information-and-computation/superconducting-qubits | Qubits built from Josephson-junction circuits — transmons, fluxonium, readout, coherence and multi-qubit processors.
- 04-quantum-physics/quantum-information-and-computation/trapped-ion-and-neutral-atom-qubits | Atomic qubits — ions in Paul traps coupled by phonons, and neutral atoms in tweezer arrays coupled by Rydberg interactions.
- 04-quantum-physics/quantum-mechanics-core | The postulates, the standard solvable systems, angular momentum and spin, approximation methods, scattering theory, path integrals and geometric phase
- 04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin | Orbital and spin angular momentum, SU(2) representations, addition of angular momenta and spin–orbit coupling.
- 04-quantum-physics/quantum-mechanics-core/approximation-methods | Time-independent and time-dependent perturbation theory, variational methods, WKB and the adiabatic theorem.
- 04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems | The harmonic oscillator, hydrogen atom, square wells, barriers and other systems with closed-form solutions.
- 04-quantum-physics/quantum-mechanics-core/geometric-phases | Berry phase, Aharonov–Bohm effect, holonomy and their role in topology of quantum matter.
- 04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics | Feynman's sum over histories, the classical limit, stationary-phase approximations, instantons and semiclassical quantization.
- 04-quantum-physics/quantum-mechanics-core/postulates-and-formalism | Hilbert space, observables, the Born rule, time evolution, pictures, and density matrices.
- 04-quantum-physics/quantum-mechanics-core/scattering-theory | Cross sections, partial-wave analysis, the Born approximation, resonances and the optical theorem.
- 04-quantum-physics/quantum-optics | The quantum theory of light and its interaction with matter — photon statistics, cavity and circuit QED, squeezing, single photons and optomechanics.
- 04-quantum-physics/quantum-optics/cavity-and-circuit-qed | Strong coupling of single emitters to single photon modes, with atoms in optical/microwave cavities and superconducting qubits in resonators.
- 04-quantum-physics/quantum-optics/cavity-optomechanics | Coupling light to mechanical motion via radiation pressure — ground-state cooling, quantum-limited displacement sensing and macroscopic quantum states
- 04-quantum-physics/quantum-optics/quantized-light-and-photon-statistics | Quantization of the electromagnetic field; Fock, coherent and thermal states; coherence functions and non-classical light.
- 04-quantum-physics/quantum-optics/single-photon-sources-and-detectors | Generating and detecting light one quantum at a time — quantum dots, color centers, SPDC, superconducting nanowire detectors.
- 04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology | Reducing quantum noise in one quadrature, entanglement-enhanced sensing and the Heisenberg limit.
- 11-interdisciplinary-physics | Physics applied across science and technology — biophysics, Earth and climate physics, medical physics, chemical physics, accelerator physics, and dev
- 11-interdisciplinary-physics/accelerator-physics | The science of particle accelerators — beam dynamics and focusing, synchrotron and free-electron-laser light sources, and accelerator technology from 
- 11-interdisciplinary-physics/accelerator-physics/accelerator-technology | The hardware of accelerators — RF and superconducting RF cavities, normal and superconducting magnets, sources, cooling techniques, and medical and in
- 11-interdisciplinary-physics/accelerator-physics/beam-dynamics | Motion of particles in accelerators — strong focusing, betatron and synchrotron oscillations, Twiss parameters and emittance, chromaticity, resonances
- 11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources | Accelerator-based X-ray sources — bending magnets, undulators and wigglers, diffraction-limited storage rings, and self-amplified free-electron lasers
- 11-interdisciplinary-physics/applied-and-device-physics | Physics behind technology — semiconductor devices and photovoltaics, quantum sensing and metrology, energy materials, batteries and thermoelectrics.
- 11-interdisciplinary-physics/applied-and-device-physics/energy-materials-and-thermoelectrics | Physics of energy conversion and storage materials — lithium-ion batteries, solid-state electrolytes, thermoelectrics and the figure of merit ZT, hydr
- 11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing | Using quantum coherence to measure — NV-centre and atomic magnetometers, SQUIDs, atom-interferometric gravimeters and gyroscopes, entanglement-enhance
- 11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics | Transistors (MOSFET to gate-all-around), LEDs and lasers, solar cells and the Shockley–Queisser limit, perovskites and tandem cells.
- 11-interdisciplinary-physics/biophysics | Physics of biological systems — protein folding and molecular machines, single-molecule experiments, membranes and cell mechanics, and physics of livi
- 11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics | Mechanics of lipid membranes and cells — bending elasticity, vesicle shapes, the cytoskeleton, motility, mechanotransduction and tissue mechanics.
- 11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding | Physical principles of biomolecules — folding energy landscapes, molecular motors and machines, structure determination and ML structure prediction.
- 11-interdisciplinary-physics/biophysics/physics-of-living-systems | Physical limits and principles in biology — noise in gene expression, limits of sensing, neural dynamics, developmental patterning, kinetic proofreadi
- 11-interdisciplinary-physics/biophysics/single-molecule-biophysics | Watching and manipulating individual biomolecules — optical and magnetic tweezers, single-molecule fluorescence and FRET, nanopores and force spectros
- 11-interdisciplinary-physics/chemical-physics | Physics at the heart of chemistry — molecular spectroscopy, reaction dynamics and rate theory, quantum chemistry methods, surface science and catalysi
- 11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy | Reading molecular structure from light — rotational, vibrational and electronic spectra, Raman scattering, selection rules and ultrafast multidimensio
- 11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods | Computing molecular electronic structure — Hartree–Fock, configuration interaction, perturbation theory, coupled cluster, basis sets and quantum-compu
- 11-interdisciplinary-physics/chemical-physics/reaction-dynamics | How chemical reactions happen — potential energy surfaces, transition-state theory, Marcus electron transfer, crossed molecular beams, conical interse
- 11-interdisciplinary-physics/chemical-physics/surface-science-and-catalysis | Physics and chemistry at surfaces — adsorption isotherms, surface structure and reconstruction, scanning probe microscopy, heterogeneous catalysis and
- 11-interdisciplinary-physics/earth-atmosphere-and-climate-physics | The physics of our planet — atmospheric dynamics, radiative forcing and climate sensitivity, ocean circulation, seismology and the deep Earth.
- 11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics | Fluid dynamics of the rotating, stratified atmosphere — geostrophic balance, Rossby waves, the general circulation, jet streams, convection and weathe
- 11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing | Earth's energy balance — the greenhouse effect, radiative forcing, feedbacks (water vapour, lapse rate, albedo, clouds), climate sensitivity and detec
- 11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics | Physical oceanography — wind-driven gyres and western boundary currents, thermohaline circulation and the AMOC, ocean waves, tides and ocean heat upta
- 11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior | Seismic waves and what they reveal — Earth's layered structure, the inner core, tomography, earthquake physics, plate tectonics and the geodynamo.
- 11-interdisciplinary-physics/medical-physics | Physics for diagnosis and therapy — X-ray CT and MRI, radiation therapy and proton therapy, nuclear medicine and PET, ultrasound and biomedical optics
- 11-interdisciplinary-physics/medical-physics/medical-imaging | Imaging the body — projection radiography, computed tomography and reconstruction, MRI physics and contrast, functional MRI, image quality and dose.
- 11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet | Imaging and therapy with radioactive tracers — gamma cameras and SPECT, positron emission tomography, time-of-flight PET, radiopharmaceuticals and the
- 11-interdisciplinary-physics/medical-physics/radiation-therapy | Treating cancer with ionizing radiation — linac photon therapy, IMRT, proton and carbon-ion therapy and the Bragg peak, radiobiology, dosimetry and FL
- 11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics | Non-ionizing medical imaging — ultrasound echography and Doppler, elastography, optical coherence tomography, photoacoustics and diffuse optics.

## Explicit cross-links already written in the notes (16): each becomes a "written" record
- 04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy -> 11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy
- 04-quantum-physics/atomic-molecular-and-optical-physics/laser-cooling-and-trapping -> 11-interdisciplinary-physics/biophysics/single-molecule-biophysics
- 04-quantum-physics/atomic-molecular-and-optical-physics/ultracold-molecules -> 11-interdisciplinary-physics/chemical-physics/reaction-dynamics
- 04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity -> 11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods
- 04-quantum-physics/quantum-mechanics-core/approximation-methods -> 11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods
- 04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology -> 11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing
- 11-interdisciplinary-physics/applied-and-device-physics -> 04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology
- 11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing -> 04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement
- 11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing -> 04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology
- 11-interdisciplinary-physics/biophysics/single-molecule-biophysics -> 04-quantum-physics/atomic-molecular-and-optical-physics/laser-cooling-and-trapping
- 11-interdisciplinary-physics/chemical-physics -> 04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy
- 11-interdisciplinary-physics/chemical-physics -> 04-quantum-physics/atomic-molecular-and-optical-physics/ultracold-molecules
- 11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy -> 04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy
- 11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods -> 04-quantum-physics/quantum-mechanics-core/approximation-methods
- 11-interdisciplinary-physics/chemical-physics/surface-science-and-catalysis -> 04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems
- 11-interdisciplinary-physics/medical-physics/medical-imaging -> 04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin

## Shared curated concepts (21)
- Bose–Einstein condensation and superfluidity: Macroscopic occupation of one quantum state — cold atoms, helium, neutron stars, superconductors
- Chaos and nonlinear dynamics: Deterministic unpredictability; ergodicity as the bridge to statistical mechanics
- Density functional methods: Ground-state properties from the density alone — electrons, nuclei, classical fluids
- Diffusion, Brownian motion and stochastic processes: Random microscopic kicks produce universal macroscopic laws
- Disorder and localization: Interference in random media halts transport — electrons, light, sound, cold atoms
- Entanglement: Correlations without a classical description; organizes many-body states and spacetime
- Entropy and information: Entropy as missing information, from heat engines to black holes and qubits
- Hamiltonian structure and phase space: Phase-space geometry underlies classical, statistical and quantum dynamics
- Heat engines and efficiency limits: Thermodynamic bounds on converting energy
- Interference and diffraction: Phase-sensitive superposition, used from crystallography to gravitational-wave detection
- Lasers, coherence and stimulated emission: Phase-coherent light from stimulated emission; coherence as an order parameter
- Mean-field and self-consistent theories: Replace fluctuating neighbours by their average; exact in high dimension or large N
- Non-equilibrium fluctuation theorems: Exact relations for driven small systems
- Oscillators and resonance: The universal small-oscillation model and its quantum version
- Precision measurement and sensing: Pushing measurement to fundamental limits to test fundamental physics
- Quantum simulation and cold atoms: Engineered quantum systems emulate models from condensed matter, nuclear and high-energy physics
- Quasiparticles and collective modes: Interacting systems behave like gases of emergent particles
- Radiation by accelerated charges: One radiation formula powering light sources, astrophysical emission and diagnostics
- Spin and angular momentum: Rotational structure and its coupling to motion and fields
- Tunnelling and instantons: Classically forbidden transitions dominated by Euclidean saddle points
- Universality and scaling: Microscopically different systems share exponents near fixed points

## Latent candidate pairs (4)
- 04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical <-> 11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing (score 0.64; shares Entanglement, Interference and diffraction, Lasers, coherence and stimulated emission)
- 04-quantum-physics/quantum-information-and-computation <-> 11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing (score 0.57; shares Entanglement, Interference and diffraction, Diffusion, Brownian motion and stochastic processes, Lasers, coherence and stimulated emission)
- 04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation <-> 11-interdisciplinary-physics/chemical-physics (score 0.45; shares Quantum simulation and cold atoms, Tunnelling and instantons, Lasers, coherence and stimulated emission)
- 04-quantum-physics/atomic-molecular-and-optical-physics <-> 11-interdisciplinary-physics/accelerator-physics (score 0.35; shares Hamiltonian structure and phase space, Oscillators and resonance, Lasers, coherence and stimulated emission)

## Shared papers (3 note pairs; algorithmic, weak evidence)
- 04-quantum-physics/quantum-mechanics-core/postulates-and-formalism <-> 11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods: "Development of the Colle-Salvetti correlation-energy formula into a functional of the elec" (1988)
- 04-quantum-physics/quantum-information-and-computation/entanglement-theory <-> 11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing: "Quantum sensing" (2017)
- 04-quantum-physics/quantum-information-and-computation <-> 11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing: "Ultrastrong coupling between light and matter" (2019)