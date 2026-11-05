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

# Your set: 11-02 (Interdisciplinary and Applied Physics with Electromagnetism and Optics)

## Nodes (58)
- 02-electromagnetism-and-optics | Electric and magnetic fields, Maxwell's equations, electromagnetic radiation and scattering, classical optics, and modern photonics and lasers.
- 02-electromagnetism-and-optics/classical-optics | Light as rays and waves — geometric optics, interference and diffraction, polarization, Fourier optics and imaging, coherence.
- 02-electromagnetism-and-optics/classical-optics/coherence-and-statistical-optics | Temporal and spatial coherence, the Wiener–Khinchin and van Cittert–Zernike theorems, speckle and intensity interferometry.
- 02-electromagnetism-and-optics/classical-optics/fourier-optics-and-imaging | Imaging as spatial-frequency filtering — transfer functions, the diffraction limit, holography, phase imaging and super-resolution microscopy.
- 02-electromagnetism-and-optics/classical-optics/geometric-optics | Ray optics — reflection, refraction, lenses and mirrors, optical instruments, aberrations and ray-transfer matrices.
- 02-electromagnetism-and-optics/classical-optics/interference-and-diffraction | Superposition of light waves — double slits, thin films, interferometers, Fraunhofer and Fresnel diffraction, gratings.
- 02-electromagnetism-and-optics/classical-optics/polarization-and-crystal-optics | Polarization states of light, Jones and Stokes formalisms, birefringence, wave plates, optical activity and electro-optic effects.
- 02-electromagnetism-and-optics/electrodynamics | Time-dependent fields — Maxwell's equations, electromagnetic waves and waveguides, potentials and gauge invariance, and the relativistic formulation.
- 02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides | Plane waves, polarization, reflection and refraction (Fresnel), skin depth, waveguide modes, resonant cavities and transmission lines.
- 02-electromagnetism-and-optics/electrodynamics/maxwells-equations | The four laws of classical electromagnetism, the displacement current, charge conservation, and field energy and momentum.
- 02-electromagnetism-and-optics/electrodynamics/potentials-and-gauge-invariance | Scalar and vector potentials, gauge transformations, Coulomb and Lorenz gauges, retarded potentials and the physical role of potentials.
- 02-electromagnetism-and-optics/electrodynamics/relativistic-electrodynamics | Covariant formulation of electromagnetism — the field-strength tensor, four-current, field transformations and invariants.
- 02-electromagnetism-and-optics/electrostatics-and-magnetostatics | Static electric and magnetic fields — Coulomb and Gauss's laws, Poisson's equation and boundary-value problems, multipole expansions, Biot–Savart, and
- 02-electromagnetism-and-optics/electrostatics-and-magnetostatics/electrostatics-and-boundary-value-problems | Solving for static fields — Gauss's law, Poisson/Laplace equations, uniqueness, method of images, separation of variables, conductors and capacitance.
- 02-electromagnetism-and-optics/electrostatics-and-magnetostatics/fields-in-matter | Polarization, magnetization, bound charges and currents, the auxiliary fields D and H, dielectric and magnetic response, boundary conditions.
- 02-electromagnetism-and-optics/electrostatics-and-magnetostatics/magnetostatics | Magnetic fields of steady currents — Biot–Savart and Ampère's laws, the vector potential, magnetic dipoles and forces on currents.
- 02-electromagnetism-and-optics/electrostatics-and-magnetostatics/multipole-expansions | Expanding fields of localized sources in monopole, dipole, quadrupole and higher terms; spherical harmonics and their physical applications.
- 02-electromagnetism-and-optics/photonics-and-lasers | Generating and engineering light — laser physics, nonlinear optics, ultrafast and attosecond optics, integrated and fiber photonics, metamaterials and
- 02-electromagnetism-and-optics/photonics-and-lasers/integrated-and-fiber-photonics | Guiding light in fibres and on chips — optical fibres, silicon and lithium-niobate photonics, microresonators and Kerr frequency combs.
- 02-electromagnetism-and-optics/photonics-and-lasers/laser-physics | How lasers work — stimulated emission, population inversion, gain media, optical cavities, linewidth and mode-locking.
- 02-electromagnetism-and-optics/photonics-and-lasers/metamaterials-and-plasmonics | Engineered electromagnetic media — negative index, cloaking, metasurfaces, surface plasmon polaritons and photonic crystals.
- 02-electromagnetism-and-optics/photonics-and-lasers/nonlinear-optics | Intensity-dependent optical response — harmonic generation, phase matching, the Kerr effect, self-phase modulation, parametric amplification and optic
- 02-electromagnetism-and-optics/photonics-and-lasers/topological-photonics | Band topology for light — one-way edge states immune to backscattering, photonic quantum Hall and Floquet analogues.
- 02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics | Femtosecond and attosecond light pulses — generation, chirped-pulse amplification, high-harmonic generation and time-resolved spectroscopy of electron
- 02-electromagnetism-and-optics/radiation-and-scattering | How accelerated charges radiate and how light scatters — dipole radiation, synchrotron and bremsstrahlung, Rayleigh/Mie/Thomson scattering, Cherenkov 
- 02-electromagnetism-and-optics/radiation-and-scattering/cherenkov-and-transition-radiation | Radiation by charges moving faster than light in a medium, and radiation emitted when charges cross boundaries between media.
- 02-electromagnetism-and-optics/radiation-and-scattering/dipole-radiation-and-antennas | Radiation from oscillating electric and magnetic dipoles, radiation patterns, antenna arrays and radiation resistance.
- 02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges | Liénard–Wiechert fields, the Larmor and Liénard formulas, synchrotron radiation, bremsstrahlung and radiation reaction.
- 02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light | Thomson, Rayleigh, Mie and Compton scattering — why the sky is blue, clouds are white, and how scattering diagnoses matter.
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
- 02-electromagnetism-and-optics/classical-optics -> 11-interdisciplinary-physics/medical-physics/medical-imaging
- 02-electromagnetism-and-optics/classical-optics/fourier-optics-and-imaging -> 11-interdisciplinary-physics/medical-physics/medical-imaging
- 02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics -> 11-interdisciplinary-physics/chemical-physics/reaction-dynamics
- 02-electromagnetism-and-optics/radiation-and-scattering -> 11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources
- 02-electromagnetism-and-optics/radiation-and-scattering -> 11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing
- 02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges -> 11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources
- 11-interdisciplinary-physics/accelerator-physics -> 02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges
- 11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources -> 02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges
- 11-interdisciplinary-physics/chemical-physics/reaction-dynamics -> 02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics
- 11-interdisciplinary-physics/medical-physics -> 02-electromagnetism-and-optics/classical-optics/fourier-optics-and-imaging
- 11-interdisciplinary-physics/medical-physics/medical-imaging -> 02-electromagnetism-and-optics/classical-optics/fourier-optics-and-imaging
- 11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics -> 02-electromagnetism-and-optics/classical-optics/coherence-and-statistical-optics

## Shared curated concepts (14)
- Bose–Einstein condensation and superfluidity: Macroscopic occupation of one quantum state — cold atoms, helium, neutron stars, superconductors
- Disorder and localization: Interference in random media halts transport — electrons, light, sound, cold atoms
- Elasticity and continuum mechanics: Continuum response of solids — from metals to neutron-star crusts and cells
- Entanglement: Correlations without a classical description; organizes many-body states and spacetime
- Hydrodynamics and continuum descriptions: Long-wavelength dynamics of conserved densities — from water to quark–gluon plasma
- Interference and diffraction: Phase-sensitive superposition, used from crystallography to gravitational-wave detection
- Lasers, coherence and stimulated emission: Phase-coherent light from stimulated emission; coherence as an order parameter
- Machine learning and physics: Learning machines as statistical-physics systems, and as tools for physics
- Oscillators and resonance: The universal small-oscillation model and its quantum version
- Precision measurement and sensing: Pushing measurement to fundamental limits to test fundamental physics
- Quasiparticles and collective modes: Interacting systems behave like gases of emergent particles
- Radiation by accelerated charges: One radiation formula powering light sources, astrophysical emission and diagnostics
- Radiation, blackbody and radiative transfer: Matter–light equilibrium, from the CMB to climate
- Spin and angular momentum: Rotational structure and its coupling to motion and fields

## Latent candidate pairs (0)

## Shared papers (1 note pairs; algorithmic, weak evidence)
- 02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics <-> 11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources: "Terawatt-attosecond hard X-ray free-electron laser at high repetition rate" (2024)