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

# Your set: 11-03 (Interdisciplinary and Applied Physics with Thermodynamics and Statistical Mechanics)

## Nodes (58)
- 03-thermodynamics-and-statistical-mechanics | Heat, work and entropy; how macroscopic behaviour emerges from microscopic statistics; phase transitions and critical phenomena; non-equilibrium and c
- 03-thermodynamics-and-statistical-mechanics/classical-thermodynamics | The laws of thermodynamics, thermodynamic potentials and Maxwell relations, heat engines and refrigerators, phase equilibria.
- 03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/heat-engines-and-efficiency | Cyclic conversion of heat to work — Carnot, Otto, Diesel, Stirling and Rankine cycles; refrigerators, heat pumps and finite-time efficiency.
- 03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/laws-of-thermodynamics | Temperature, energy conservation, entropy and the second law, and the unattainability of absolute zero.
- 03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/phase-equilibria-and-chemical-potential | Coexistence of phases, the chemical potential, Gibbs phase rule, Clausius–Clapeyron, phase diagrams, mixtures and chemical equilibrium.
- 03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/thermodynamic-potentials-and-maxwell-relations | Internal energy, enthalpy, Helmholtz and Gibbs free energies, Legendre transforms, Maxwell relations and response functions.
- 03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems | Physics of randomness and emergent complexity — spin glasses, localization, percolation, complex networks and the statistical physics of learning.
- 03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/complex-networks | Statistical physics of networks — random graphs, small worlds, scale-free degree distributions, robustness and spreading processes.
- 03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/localization-and-disorder | How disorder stops transport — Anderson localization, scaling theory, weak localization, and many-body localization in interacting systems.
- 03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/percolation | Geometric phase transitions in random connectivity — percolation thresholds, cluster statistics, fractal geometry and applications.
- 03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/spin-glasses | Magnets with random, frustrated interactions — Edwards–Anderson and SK models, replica symmetry breaking, aging and rugged energy landscapes.
- 03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/statistical-physics-of-learning | Neural networks and inference through statistical mechanics — Hopfield networks, Boltzmann machines, perceptron capacity, and theory of deep learning.
- 03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics | Deriving thermodynamics from microscopic states — ensembles, partition functions, quantum statistics, entropy and information, exactly solvable models
- 03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions | Microcanonical, canonical and grand canonical ensembles, partition functions, equipartition and ensemble equivalence.
- 03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information | Boltzmann, Gibbs and Shannon entropy, maximum-entropy inference, Maxwell's demon, Landauer's principle and the thermodynamics of computation.
- 03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/exactly-solvable-models | Models with closed-form statistical mechanics — 1D and 2D Ising, transfer matrices, Bethe ansatz, Lieb–Liniger and vertex models.
- 03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics | Bose–Einstein and Fermi–Dirac statistics, blackbody radiation, phonons, degenerate Fermi gases and Bose–Einstein condensation.
- 03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics | Systems out of equilibrium — kinetic theory, linear response and fluctuation–dissipation, stochastic dynamics, fluctuation theorems and driven steady 
- 03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/driven-systems-and-nonequilibrium-steady-states | Steady states maintained by currents — exclusion processes, KPZ interface growth, absorbing-state transitions and self-organized criticality.
- 03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation | Gases as many colliding particles — Maxwell–Boltzmann distribution, mean free path, the Boltzmann equation, H-theorem and transport coefficients.
- 03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation | How systems respond to weak perturbations — response functions, Kubo formulas, the fluctuation–dissipation theorem and Onsager reciprocity.
- 03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics | Random processes in physics — Brownian motion, Langevin and Fokker–Planck equations, master equations, first-passage and escape rates.
- 03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-thermodynamics-and-fluctuation-theorems | Thermodynamics of single fluctuating trajectories — Jarzynski equality, Crooks theorem, entropy production and thermodynamic uncertainty relations.
- 03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena | How matter changes phase — order parameters, Ising and lattice models, mean-field and Landau theory, the renormalization group, universality and topol
- 03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/critical-exponents-and-universality | Power-law singularities at critical points, scaling relations, universality classes and their precise numerical values.
- 03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/ising-model-and-lattice-models | The Ising, Potts, XY and Heisenberg models — the canonical systems for studying order, disorder and phase transitions.
- 03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory | Approximating interacting systems by an average field; Landau free-energy expansions in the order parameter; Ginzburg criterion.
- 03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/renormalization-group | Coarse-graining as a flow in the space of theories — block spins, fixed points, relevant/irrelevant operators and the epsilon expansion.
- 03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/topological-phase-transitions-bkt | The Berezinskii–Kosterlitz–Thouless transition — vortex–antivortex unbinding, quasi-long-range order and the universal superfluid jump in 2D.
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

## Explicit cross-links already written in the notes (12): each becomes a "written" record
- 03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/heat-engines-and-efficiency -> 11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics
- 03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics -> 11-interdisciplinary-physics/biophysics/single-molecule-biophysics
- 03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-thermodynamics-and-fluctuation-theorems -> 11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding
- 11-interdisciplinary-physics/applied-and-device-physics -> 03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/heat-engines-and-efficiency
- 11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics -> 03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/heat-engines-and-efficiency
- 11-interdisciplinary-physics/biophysics -> 03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/statistical-physics-of-learning
- 11-interdisciplinary-physics/biophysics -> 03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-thermodynamics-and-fluctuation-theorems
- 11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding -> 03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/spin-glasses
- 11-interdisciplinary-physics/biophysics/physics-of-living-systems -> 03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information
- 11-interdisciplinary-physics/biophysics/single-molecule-biophysics -> 03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-thermodynamics-and-fluctuation-theorems
- 11-interdisciplinary-physics/chemical-physics/reaction-dynamics -> 03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics
- 11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing -> 03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics

## Shared curated concepts (20)
- Active matter and collective behavior: Energy-consuming agents form ordered, flowing phases — from bacteria to birds
- Bose–Einstein condensation and superfluidity: Macroscopic occupation of one quantum state — cold atoms, helium, neutron stars, superconductors
- Chaos and nonlinear dynamics: Deterministic unpredictability; ergodicity as the bridge to statistical mechanics
- Diffusion, Brownian motion and stochastic processes: Random microscopic kicks produce universal macroscopic laws
- Disorder and localization: Interference in random media halts transport — electrons, light, sound, cold atoms
- Entanglement: Correlations without a classical description; organizes many-body states and spacetime
- Entropy and information: Entropy as missing information, from heat engines to black holes and qubits
- Glasses, spin glasses and rugged landscapes: Many competing minima — glasses, proteins, optimization, neural networks
- Hamiltonian structure and phase space: Phase-space geometry underlies classical, statistical and quantum dynamics
- Heat engines and efficiency limits: Thermodynamic bounds on converting energy
- Hydrodynamics and continuum descriptions: Long-wavelength dynamics of conserved densities — from water to quark–gluon plasma
- Interference and diffraction: Phase-sensitive superposition, used from crystallography to gravitational-wave detection
- Machine learning and physics: Learning machines as statistical-physics systems, and as tools for physics
- Mean-field and self-consistent theories: Replace fluctuating neighbours by their average; exact in high dimension or large N
- Monte Carlo and stochastic sampling: Sampling replaces exact enumeration in statistical, quantum and particle physics
- Non-equilibrium fluctuation theorems: Exact relations for driven small systems
- Quantum simulation and cold atoms: Engineered quantum systems emulate models from condensed matter, nuclear and high-energy physics
- Quasiparticles and collective modes: Interacting systems behave like gases of emergent particles
- Radiation, blackbody and radiative transfer: Matter–light equilibrium, from the CMB to climate
- Universality and scaling: Microscopically different systems share exponents near fixed points

## Latent candidate pairs (2)
- 03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/statistical-physics-of-learning <-> 11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding (score 0.69; shares Glasses, spin glasses and rugged landscapes, Disorder and localization, Diffusion, Brownian motion and stochastic processes)
- 03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics <-> 11-interdisciplinary-physics/biophysics/physics-of-living-systems (score 0.47; shares Active matter and collective behavior, Entropy and information, Diffusion, Brownian motion and stochastic processes)

## Shared papers (1 note pairs; algorithmic, weak evidence)
- 03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/phase-equilibria-and-chemical-potential <-> 11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods: "Self-Consistent Equations Including Exchange and Correlation Effects" (1965)