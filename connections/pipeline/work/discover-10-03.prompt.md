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

# Your set: 10-03 (Plasma Physics with Thermodynamics and Statistical Mechanics)

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

## Explicit cross-links already written in the notes (4): each becomes a "written" record
- 03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics -> 10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping
- 03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation -> 10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping
- 10-plasma-physics/plasma-fundamentals -> 03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation
- 10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping -> 03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation

## Shared curated concepts (17)
- Bose–Einstein condensation and superfluidity: Macroscopic occupation of one quantum state — cold atoms, helium, neutron stars, superconductors
- Chaos and nonlinear dynamics: Deterministic unpredictability; ergodicity as the bridge to statistical mechanics
- Compact objects: Matter at extreme density and gravity — where nuclear, particle, GR and astro meet
- Decoherence and open quantum systems: How environments make quantum systems look classical
- Diffusion, Brownian motion and stochastic processes: Random microscopic kicks produce universal macroscopic laws
- Hydrodynamics and continuum descriptions: Long-wavelength dynamics of conserved densities — from water to quark–gluon plasma
- Kinetic theory and transport: Distribution-function dynamics between microscopic and hydrodynamic scales
- Linear response and fluctuation–dissipation: Response to a small push is fixed by equilibrium fluctuations
- Mean-field and self-consistent theories: Replace fluctuating neighbours by their average; exact in high dimension or large N
- Phase transitions and criticality: Non-analytic change of state; fluctuations at all scales near criticality
- Plasma oscillations, screening and Landau damping: Collective long-range Coulomb physics in plasmas, metals and quark matter
- Quantum simulation and cold atoms: Engineered quantum systems emulate models from condensed matter, nuclear and high-energy physics
- Quasiparticles and collective modes: Interacting systems behave like gases of emergent particles
- Radiation, blackbody and radiative transfer: Matter–light equilibrium, from the CMB to climate
- Solitons and nonlinear waves: Shape-preserving waves where nonlinearity balances dispersion
- Universality and scaling: Microscopically different systems share exponents near fixed points
- Waves and wave equations: One mathematics for sound, light, matter waves and gravitational waves

## Latent candidate pairs (1)
- 03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation <-> 10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping (score 0.42; shares Linear response and fluctuation–dissipation, Kinetic theory and transport, Diffusion, Brownian motion and stochastic processes)

## Shared papers (1 note pairs; algorithmic, weak evidence)
- 03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation <-> 10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters: "A Model for Collision Processes in Gases. I. Small Amplitude Processes in Charged and Neut" (1954)