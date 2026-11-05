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

# Your set: 11-01 (Interdisciplinary and Applied Physics with Classical Mechanics)

## Nodes (62)
- 01-classical-mechanics | The motion of particles, rigid bodies and continua under forces — Newtonian and analytical mechanics, oscillations and waves, nonlinear dynamics and c
- 01-classical-mechanics/analytical-mechanics | Lagrangian and Hamiltonian reformulations of mechanics — generalized coordinates, constraints, phase space, canonical transformations and variational 
- 01-classical-mechanics/analytical-mechanics/canonical-transformations-and-hamilton-jacobi | Changes of phase-space variables that preserve Hamilton's equations, generating functions, action–angle variables and the Hamilton–Jacobi equation.
- 01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics | Phase-space dynamics — Hamilton's equations, Poisson brackets, Liouville's theorem and symplectic structure.
- 01-classical-mechanics/analytical-mechanics/lagrangian-mechanics | Equations of motion from L = T − V in generalized coordinates, holonomic constraints, Lagrange multipliers and cyclic coordinates.
- 01-classical-mechanics/analytical-mechanics/variational-principles | Least action, Fermat's principle, the calculus of variations and their role across physics.
- 01-classical-mechanics/continuum-and-fluid-mechanics | Deformable solids and flowing fluids as continua — elasticity, ideal and viscous flow, turbulence, instabilities and convection, low-Reynolds-number f
- 01-classical-mechanics/continuum-and-fluid-mechanics/elasticity | Stress, strain and elastic response of solids — Hooke's law, elastic moduli, elastic waves, beams, plates and buckling.
- 01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow | Inviscid and viscous fluid dynamics — Euler and Navier–Stokes equations, Bernoulli, vorticity, boundary layers, lift and drag.
- 01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection | How fluid flows become unstable — Rayleigh–Bénard convection, Kelvin–Helmholtz, Rayleigh–Taylor and Plateau–Rayleigh instabilities.
- 01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics | Viscosity-dominated flow — Stokes flow, the scallop theorem and microswimmers, and fluid physics at the micro- and nanoscale.
- 01-classical-mechanics/continuum-and-fluid-mechanics/turbulence | Chaotic, multiscale fluid motion — the energy cascade, Kolmogorov scaling, intermittency, wall turbulence and turbulence modelling.
- 01-classical-mechanics/newtonian-mechanics | Motion under forces — Newton's laws, momentum and energy conservation, central forces and orbits, non-inertial frames, and few-body problems.
- 01-classical-mechanics/newtonian-mechanics/central-forces-and-orbits | Motion in central potentials — Kepler orbits, effective potential, orbital stability, precession and Rutherford scattering.
- 01-classical-mechanics/newtonian-mechanics/conservation-laws | Energy, linear momentum and angular momentum conservation; elastic and inelastic collisions; centre-of-mass frame.
- 01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics | The three-body problem, Lagrange points, orbital resonances, perturbation theory and N-body integration.
- 01-classical-mechanics/newtonian-mechanics/kinematics-and-newtons-laws | Describing motion and relating it to forces — inertial frames, Newton's three laws, friction, drag and free-body analysis.
- 01-classical-mechanics/newtonian-mechanics/non-inertial-frames | Mechanics in accelerating and rotating frames — fictitious forces, Coriolis effects, Foucault pendulum and tides.
- 01-classical-mechanics/nonlinear-dynamics-and-chaos | Dynamical systems beyond linearity — deterministic chaos, bifurcations, KAM theory, solitons, synchronization and pattern formation.
- 01-classical-mechanics/nonlinear-dynamics-and-chaos/bifurcations-and-routes-to-chaos | Qualitative changes in dynamics as parameters vary — saddle-node, pitchfork and Hopf bifurcations, period doubling and Feigenbaum universality.
- 01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos | Sensitive dependence on initial conditions in deterministic systems — Lyapunov exponents, strange attractors and limits of prediction.
- 01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos | The survival of invariant tori under perturbation, mixed phase spaces, resonances and Arnold diffusion in conservative systems.
- 01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems | Localized waves that survive collisions — KdV and nonlinear Schrödinger solitons, inverse scattering, Lax pairs and integrability.
- 01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation | Collective rhythms and spatial order out of equilibrium — Kuramoto synchronization, Turing patterns, reaction–diffusion and convection patterns.
- 01-classical-mechanics/oscillations-and-waves | Harmonic, damped and driven oscillators, coupled oscillators and normal modes, mechanical waves and acoustics, parametric and nonlinear oscillations.
- 01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes | Systems of coupled oscillators, normal-mode analysis, beats, and the transition to waves in chains.
- 01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators | Simple harmonic motion, damping regimes, driven oscillators, resonance and the quality factor.
- 01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics | Waves on strings and in media, sound, dispersion, impedance, reflection and transmission, Doppler effect and acoustic phenomena.
- 01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations | Oscillators with time-varying parameters or nonlinear restoring forces — Mathieu equation, Kapitza pendulum, Duffing and Van der Pol oscillators.
- 01-classical-mechanics/rigid-body-dynamics | Rotation of extended bodies — inertia tensor, Euler's equations, torque-free and heavy tops, gyroscopes and precession.
- 01-classical-mechanics/rigid-body-dynamics/euler-equations-and-tops | Body-frame equations of rotation, torque-free motion, the intermediate-axis instability and the heavy symmetric top.
- 01-classical-mechanics/rigid-body-dynamics/gyroscopes-and-precession | Gyroscopic stability, precession and nutation in technology and nature — from bicycles to the precession of Earth's axis.
- 01-classical-mechanics/rigid-body-dynamics/rotational-dynamics-and-inertia-tensor | Moments and products of inertia, principal axes, rolling motion and rotational kinetic energy.
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

## Explicit cross-links already written in the notes (21): each becomes a "written" record
- 01-classical-mechanics/continuum-and-fluid-mechanics -> 11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics
- 01-classical-mechanics/continuum-and-fluid-mechanics/elasticity -> 11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior
- 01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics -> 11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics
- 01-classical-mechanics/newtonian-mechanics/non-inertial-frames -> 11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics
- 01-classical-mechanics/nonlinear-dynamics-and-chaos/bifurcations-and-routes-to-chaos -> 11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing
- 01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos -> 11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics
- 01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos -> 11-interdisciplinary-physics/accelerator-physics/beam-dynamics
- 01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics -> 11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior
- 01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics -> 11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics
- 11-interdisciplinary-physics/accelerator-physics/beam-dynamics -> 01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics
- 11-interdisciplinary-physics/accelerator-physics/beam-dynamics -> 01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos
- 11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics -> 01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics
- 11-interdisciplinary-physics/biophysics/physics-of-living-systems -> 01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation
- 11-interdisciplinary-physics/earth-atmosphere-and-climate-physics -> 01-classical-mechanics/newtonian-mechanics/non-inertial-frames
- 11-interdisciplinary-physics/earth-atmosphere-and-climate-physics -> 01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos
- 11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics -> 01-classical-mechanics/continuum-and-fluid-mechanics/turbulence
- 11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics -> 01-classical-mechanics/newtonian-mechanics/non-inertial-frames
- 11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics -> 01-classical-mechanics/nonlinear-dynamics-and-chaos/bifurcations-and-routes-to-chaos
- 11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics -> 01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics
- 11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior -> 01-classical-mechanics/continuum-and-fluid-mechanics/elasticity
- 11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics -> 01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics

## Shared curated concepts (16)
- Active matter and collective behavior: Energy-consuming agents form ordered, flowing phases — from bacteria to birds
- Bose–Einstein condensation and superfluidity: Macroscopic occupation of one quantum state — cold atoms, helium, neutron stars, superconductors
- Chaos and nonlinear dynamics: Deterministic unpredictability; ergodicity as the bridge to statistical mechanics
- Diffusion, Brownian motion and stochastic processes: Random microscopic kicks produce universal macroscopic laws
- Elasticity and continuum mechanics: Continuum response of solids — from metals to neutron-star crusts and cells
- Hamiltonian structure and phase space: Phase-space geometry underlies classical, statistical and quantum dynamics
- Hydrodynamics and continuum descriptions: Long-wavelength dynamics of conserved densities — from water to quark–gluon plasma
- Instabilities: Small perturbations that grow — fluids, plasmas, stars, lasers
- Interference and diffraction: Phase-sensitive superposition, used from crystallography to gravitational-wave detection
- Lasers, coherence and stimulated emission: Phase-coherent light from stimulated emission; coherence as an order parameter
- Magnetohydrodynamics, dynamos and reconnection: Conducting fluids carry and amplify magnetic fields — lab, solar, galactic
- Oscillators and resonance: The universal small-oscillation model and its quantum version
- Quasiparticles and collective modes: Interacting systems behave like gases of emergent particles
- Spin and angular momentum: Rotational structure and its coupling to motion and fields
- Turbulence and cascades: Multiscale chaotic flow in fluids, plasmas, astrophysics and wave systems
- Universality and scaling: Microscopically different systems share exponents near fixed points

## Latent candidate pairs (2)
- 01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations <-> 11-interdisciplinary-physics/accelerator-physics/beam-dynamics (score 0.75; shares Instabilities, Chaos and nonlinear dynamics, Oscillators and resonance)
- 01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics <-> 11-interdisciplinary-physics/accelerator-physics/beam-dynamics (score 0.75; shares Hamiltonian structure and phase space, Chaos and nonlinear dynamics, Oscillators and resonance)

## Shared papers (3 note pairs; algorithmic, weak evidence)
- 01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators <-> 11-interdisciplinary-physics/medical-physics/medical-imaging: "Advances in functional and structural MR image analysis and implementation as FSL" (2004)
- 01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes <-> 11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior: "Preliminary reference earth model" (1981)
- 01-classical-mechanics/rigid-body-dynamics/rotational-dynamics-and-inertia-tensor <-> 11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior: "Preliminary reference earth model" (1981)