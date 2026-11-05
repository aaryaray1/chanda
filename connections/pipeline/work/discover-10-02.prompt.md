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

# Your set: 10-02 (Plasma Physics with Electromagnetism and Optics)

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
- 10-plasma-physics | Ionized matter dominated by collective electromagnetic behaviour — plasma fundamentals, magnetohydrodynamics, magnetic and inertial fusion, laser plas
- 10-plasma-physics/inertial-and-laser-plasmas | Plasmas created and driven by intense lasers and particle beams — inertial confinement fusion, laser–plasma interactions, plasma wakefield acceleratio
- 10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics | Matter at pressures above a megabar — warm dense matter, equations of state at extreme conditions, planetary interiors, X-ray Thomson scattering and l
- 10-plasma-physics/inertial-and-laser-plasmas/inertial-confinement-fusion | Fusion by imploding fuel capsules — direct and indirect drive, hot-spot ignition, hydrodynamic instabilities, NIF burning plasma and ignition.
- 10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions | How intense light couples to plasma — collisional and collisionless absorption, parametric instabilities, relativistic self-focusing, ion acceleration
- 10-plasma-physics/inertial-and-laser-plasmas/plasma-wakefield-acceleration | Accelerating particles in plasma waves driven by lasers or particle beams — GV/m–TV/m gradients, bubble regime, beam quality, staging and applications
- 10-plasma-physics/low-temperature-and-applied-plasmas | Weakly ionized, non-equilibrium plasmas used in technology — gas discharges, semiconductor processing, atmospheric-pressure plasmas, plasma medicine a
- 10-plasma-physics/low-temperature-and-applied-plasmas/atmospheric-pressure-plasmas-and-applications | Cold plasmas at atmospheric pressure — dielectric-barrier discharges, plasma jets, plasma–liquid interactions, plasma medicine, agriculture and enviro
- 10-plasma-physics/low-temperature-and-applied-plasmas/plasma-discharges-and-processing | Gas breakdown and discharge regimes, capacitively and inductively coupled RF plasmas, sheaths, plasma etching and deposition in semiconductor manufact
- 10-plasma-physics/magnetic-confinement-fusion | Holding 100-million-degree plasma with magnetic fields — tokamaks, stellarators, turbulent transport, and the path through ITER to burning plasmas and
- 10-plasma-physics/magnetic-confinement-fusion/burning-plasmas-and-iter | Plasmas heated mainly by their own fusion alphas — ITER's goals, alpha-particle physics, power exhaust, materials, tritium breeding and paths to fusio
- 10-plasma-physics/magnetic-confinement-fusion/stellarators | Currentless toroidal confinement using 3D-shaped coils — rotational transform, neoclassical optimization, quasi-symmetry and Wendelstein 7-X.
- 10-plasma-physics/magnetic-confinement-fusion/tokamaks | Toroidal magnetic confinement with a plasma current — equilibrium and safety factor, H-mode and pedestal, ELMs, disruptions, heating and current drive
- 10-plasma-physics/magnetic-confinement-fusion/turbulent-transport-and-gyrokinetics | Why heat leaks out of fusion plasmas — drift-wave turbulence, ion- and electron-temperature-gradient modes, zonal flows, gyrokinetic theory and simula
- 10-plasma-physics/magnetohydrodynamics | Plasmas and conducting fluids as magnetized fluids — ideal MHD and Alfvén waves, magnetic reconnection, dynamos and MHD turbulence.
- 10-plasma-physics/magnetohydrodynamics/dynamo-theory | How flows generate and sustain magnetic fields — kinematic and mean-field dynamos, the α-effect, solar cycle, geodynamo and laboratory dynamos.
- 10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves | The ideal MHD equations, frozen-in magnetic flux, Alfvén and magnetosonic waves, MHD equilibrium and stability (kink, sausage, interchange).
- 10-plasma-physics/magnetohydrodynamics/magnetic-reconnection | Breaking and reconnecting magnetic field lines — Sweet–Parker and Petschek models, Hall and collisionless reconnection, plasmoid instability, solar fl
- 10-plasma-physics/magnetohydrodynamics/mhd-turbulence | Turbulence in magnetized plasmas — Iroshnikov–Kraichnan and Goldreich–Sridhar theories, anisotropic cascades, critical balance, kinetic-scale dissipat
- 10-plasma-physics/plasma-fundamentals | What makes a plasma — Debye shielding and plasma parameters, single-particle motion and drifts, kinetic theory and Landau damping, waves, instabilitie
- 10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters | Quasi-neutrality, Debye screening, plasma frequency, collisionality and the criteria that define a plasma across lab, space and astrophysical regimes.
- 10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas | Plasmas where Coulomb energy rivals thermal energy — dusty-plasma crystals, ultracold neutral plasmas, warm dense matter and one-component plasma mode
- 10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping | Collisionless plasma kinetics — the Vlasov–Maxwell system, Landau damping, velocity-space instabilities, Fokker–Planck collisions and gyrokinetics.
- 10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities | The waves a plasma supports — Langmuir, ion-acoustic, electromagnetic, whistler, Alfvén — and the streaming, drift and parametric instabilities that r
- 10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts | Charged particles in electromagnetic fields — gyration, guiding-centre drifts, adiabatic invariants, magnetic mirrors and radiation belts.
- 10-plasma-physics/space-and-astrophysical-plasmas | Plasmas of the heliosphere and beyond — the solar wind, magnetospheres and space weather, collisionless shocks and cosmic particle acceleration.
- 10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks | Collisionless shocks and particle acceleration in space — diffusive shock acceleration, magnetic-field amplification, supernova remnants and relativis
- 10-plasma-physics/space-and-astrophysical-plasmas/magnetospheres-and-space-weather | Planetary magnetic cavities in the solar wind — magnetopause and bow shock, the Dungey cycle, radiation belts, substorms, aurorae and technological im
- 10-plasma-physics/space-and-astrophysical-plasmas/solar-wind-and-heliosphere | The supersonic outflow from the Sun — Parker's model, fast and slow wind, the Parker spiral, coronal heating, switchbacks and the boundary of the heli

## Explicit cross-links already written in the notes (11): each becomes a "written" record
- 02-electromagnetism-and-optics/electrodynamics -> 10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities
- 02-electromagnetism-and-optics/electrostatics-and-magnetostatics/magnetostatics -> 10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts
- 02-electromagnetism-and-optics/photonics-and-lasers -> 10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions
- 02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics -> 10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions
- 10-plasma-physics/inertial-and-laser-plasmas -> 02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics
- 10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions -> 02-electromagnetism-and-optics/photonics-and-lasers/nonlinear-optics
- 10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions -> 02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges
- 10-plasma-physics/plasma-fundamentals -> 02-electromagnetism-and-optics/electrodynamics
- 10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters -> 02-electromagnetism-and-optics/electrostatics-and-magnetostatics/electrostatics-and-boundary-value-problems
- 10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities -> 02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides
- 10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts -> 02-electromagnetism-and-optics/electrostatics-and-magnetostatics/magnetostatics

## Shared curated concepts (11)
- Bose–Einstein condensation and superfluidity: Macroscopic occupation of one quantum state — cold atoms, helium, neutron stars, superconductors
- Hydrodynamics and continuum descriptions: Long-wavelength dynamics of conserved densities — from water to quark–gluon plasma
- Lasers, coherence and stimulated emission: Phase-coherent light from stimulated emission; coherence as an order parameter
- Linear response and fluctuation–dissipation: Response to a small push is fixed by equilibrium fluctuations
- Oscillators and resonance: The universal small-oscillation model and its quantum version
- Quasiparticles and collective modes: Interacting systems behave like gases of emergent particles
- Radiation by accelerated charges: One radiation formula powering light sources, astrophysical emission and diagnostics
- Radiation, blackbody and radiative transfer: Matter–light equilibrium, from the CMB to climate
- Solitons and nonlinear waves: Shape-preserving waves where nonlinearity balances dispersion
- Spin and angular momentum: Rotational structure and its coupling to motion and fields
- Waves and wave equations: One mathematics for sound, light, matter waves and gravitational waves

## Latent candidate pairs (1)
- 02-electromagnetism-and-optics/photonics-and-lasers/metamaterials-and-plasmonics <-> 10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions (score 0.64; shares Quasiparticles and collective modes, Oscillators and resonance, Lasers, coherence and stimulated emission)

## Shared papers (3 note pairs; algorithmic, weak evidence)
- 02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light <-> 10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics: "Model-free Rayleigh weight from x-ray Thomson scattering measurements" (2024)
- 02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges <-> 10-plasma-physics/inertial-and-laser-plasmas/inertial-confinement-fusion: "Development of the indirect-drive approach to inertial confinement fusion and the target p" (1995)
- 02-electromagnetism-and-optics/electrostatics-and-magnetostatics <-> 10-plasma-physics/space-and-astrophysical-plasmas: "CHARGED DUST DYNAMICS IN THE SOLAR SYSTEM" (1996)