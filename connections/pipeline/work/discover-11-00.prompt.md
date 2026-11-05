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

# Your set: 11-00 (Interdisciplinary and Applied Physics with Foundations)

## Nodes (59)
- 00-foundations | The shared toolkit of every branch — mathematical methods, symmetry, computational physics, measurement and statistics, units and constants, and the h
- 00-foundations/computational-physics | Numerical methods that solve physics problems beyond analytic reach — ODE/PDE solvers, Monte Carlo, molecular dynamics, tensor networks and machine le
- 00-foundations/computational-physics/machine-learning-for-physics | Neural networks as tools for physics — surrogates, physics-informed networks, neural quantum states, symbolic regression and ML-assisted discovery.
- 00-foundations/computational-physics/molecular-dynamics | Simulating many interacting particles by integrating their equations of motion — force fields, thermostats and ab initio MD.
- 00-foundations/computational-physics/monte-carlo-methods | Stochastic sampling for integrals and statistical systems — importance sampling, Metropolis, cluster algorithms, quantum Monte Carlo.
- 00-foundations/computational-physics/numerical-methods-for-odes-and-pdes | Time integrators, symplectic methods, finite differences, finite elements, finite volumes and spectral methods.
- 00-foundations/computational-physics/tensor-network-methods | Compressing quantum many-body states using their entanglement structure — MPS, DMRG, PEPS, MERA and tensor-network simulation of circuits.
- 00-foundations/history-and-philosophy-of-physics | How physics developed, what its theories say about reality, how explanations and evidence work in physics, and how physics is best learned.
- 00-foundations/history-and-philosophy-of-physics/history-of-physics | The development of physical ideas and institutions — the scientific revolution, classical physics, the quantum and relativity revolutions, big science
- 00-foundations/history-and-philosophy-of-physics/philosophy-of-physics | Conceptual foundations — interpretation of quantum mechanics, the nature of space and time, probability in physics, laws, reduction and emergence.
- 00-foundations/history-and-philosophy-of-physics/physics-education-research | Evidence on how physics is learned — misconceptions, concept inventories, active learning and problem-solving expertise.
- 00-foundations/mathematical-methods | The mathematics physicists use daily — linear algebra and Hilbert spaces, differential equations and Green's functions, complex analysis and special f
- 00-foundations/mathematical-methods/complex-analysis-and-special-functions | Analytic functions, contour integration, dispersion relations, asymptotic methods and the special functions of mathematical physics.
- 00-foundations/mathematical-methods/differential-equations-and-greens-functions | Ordinary and partial differential equations of physics, separation of variables, Sturm–Liouville theory and Green's-function solutions.
- 00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces | Vector spaces, operators, eigenvalue problems, the spectral theorem and infinite-dimensional function spaces.
- 00-foundations/mathematical-methods/tensors-and-differential-geometry | Index notation, manifolds, metrics, connections, curvature and differential forms — the language of relativity and gauge theory.
- 00-foundations/measurement-and-data-analysis | How physical quantities are measured and inferred — uncertainty propagation, statistical inference, detectors and instrumentation.
- 00-foundations/measurement-and-data-analysis/detectors-and-instrumentation | Sensors, signal chains and noise — photodetectors, cryogenic sensors, amplifiers, lock-in detection and the fundamental noise limits.
- 00-foundations/measurement-and-data-analysis/statistical-inference-in-physics | Frequentist and Bayesian methods for parameter estimation, confidence intervals, hypothesis testing and discovery claims.
- 00-foundations/measurement-and-data-analysis/uncertainty-and-error-propagation | Quantifying and combining measurement uncertainties — statistical vs. systematic, the GUM framework, correlations and significant figures.
- 00-foundations/symmetry-and-group-theory | Symmetry as the organizing principle of physics — Lie groups and representations, Noether's theorem, discrete symmetries, spontaneous symmetry breakin
- 00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt | Parity, time reversal and charge conjugation, their violation by the weak interaction, and the CPT theorem.
- 00-foundations/symmetry-and-group-theory/lie-groups-and-representations | Continuous symmetry groups, their algebras and representations — SO(3), SU(2), SU(3), Lorentz and Poincaré.
- 00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws | Every continuous symmetry of the action yields a conserved current — energy, momentum, angular momentum and charge.
- 00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking | Ground states that break symmetries of the laws — order parameters, Goldstone bosons, the Higgs mechanism and emergent order.
- 00-foundations/units-and-constants | The SI system and its 2019 redefinition, CODATA fundamental constants, dimensional analysis and scaling, natural and Planck units.
- 00-foundations/units-and-constants/dimensional-analysis-and-scaling | Using units to check, derive and estimate — Buckingham π theorem, similarity, scaling laws and order-of-magnitude reasoning.
- 00-foundations/units-and-constants/fundamental-constants | Measured constants of nature — CODATA adjustments, the fine-structure constant, G, and searches for their variation.
- 00-foundations/units-and-constants/natural-units-and-planck-scale | Unit systems that set fundamental constants to one — particle-physics, geometrized, atomic and Planck units — and how to convert back.
- 00-foundations/units-and-constants/si-units-and-2019-redefinition | How the kilogram, ampere, kelvin and mole were redefined in terms of exact constants, and how the units are realized.
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

## Explicit cross-links already written in the notes (2): each becomes a "written" record
- 00-foundations/computational-physics/molecular-dynamics -> 11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding
- 11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding -> 00-foundations/computational-physics/molecular-dynamics

## Shared curated concepts (19)
- Bose–Einstein condensation and superfluidity: Macroscopic occupation of one quantum state — cold atoms, helium, neutron stars, superconductors
- Chaos and nonlinear dynamics: Deterministic unpredictability; ergodicity as the bridge to statistical mechanics
- Density functional methods: Ground-state properties from the density alone — electrons, nuclei, classical fluids
- Diffusion, Brownian motion and stochastic processes: Random microscopic kicks produce universal macroscopic laws
- Entanglement: Correlations without a classical description; organizes many-body states and spacetime
- Entropy and information: Entropy as missing information, from heat engines to black holes and qubits
- Glasses, spin glasses and rugged landscapes: Many competing minima — glasses, proteins, optimization, neural networks
- Hamiltonian structure and phase space: Phase-space geometry underlies classical, statistical and quantum dynamics
- Hydrodynamics and continuum descriptions: Long-wavelength dynamics of conserved densities — from water to quark–gluon plasma
- Interference and diffraction: Phase-sensitive superposition, used from crystallography to gravitational-wave detection
- Lasers, coherence and stimulated emission: Phase-coherent light from stimulated emission; coherence as an order parameter
- Machine learning and physics: Learning machines as statistical-physics systems, and as tools for physics
- Mean-field and self-consistent theories: Replace fluctuating neighbours by their average; exact in high dimension or large N
- Monte Carlo and stochastic sampling: Sampling replaces exact enumeration in statistical, quantum and particle physics
- Oscillators and resonance: The universal small-oscillation model and its quantum version
- Precision measurement and sensing: Pushing measurement to fundamental limits to test fundamental physics
- Spin and angular momentum: Rotational structure and its coupling to motion and fields
- Turbulence and cascades: Multiscale chaotic flow in fluids, plasmas, astrophysics and wave systems
- Universality and scaling: Microscopically different systems share exponents near fixed points

## Latent candidate pairs (0)

## Shared papers (0 note pairs; algorithmic, weak evidence)