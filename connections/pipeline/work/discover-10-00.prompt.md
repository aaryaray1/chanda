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

# Your set: 10-00 (Plasma Physics with Foundations)

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

## Explicit cross-links already written in the notes (0): each becomes a "written" record

## Shared curated concepts (15)
- Bose–Einstein condensation and superfluidity: Macroscopic occupation of one quantum state — cold atoms, helium, neutron stars, superconductors
- Chaos and nonlinear dynamics: Deterministic unpredictability; ergodicity as the bridge to statistical mechanics
- Decoherence and open quantum systems: How environments make quantum systems look classical
- Density functional methods: Ground-state properties from the density alone — electrons, nuclei, classical fluids
- Diffusion, Brownian motion and stochastic processes: Random microscopic kicks produce universal macroscopic laws
- Hydrodynamics and continuum descriptions: Long-wavelength dynamics of conserved densities — from water to quark–gluon plasma
- Lasers, coherence and stimulated emission: Phase-coherent light from stimulated emission; coherence as an order parameter
- Linear response and fluctuation–dissipation: Response to a small push is fixed by equilibrium fluctuations
- Mean-field and self-consistent theories: Replace fluctuating neighbours by their average; exact in high dimension or large N
- Oscillators and resonance: The universal small-oscillation model and its quantum version
- Phase transitions and criticality: Non-analytic change of state; fluctuations at all scales near criticality
- Spin and angular momentum: Rotational structure and its coupling to motion and fields
- Turbulence and cascades: Multiscale chaotic flow in fluids, plasmas, astrophysics and wave systems
- Universality and scaling: Microscopically different systems share exponents near fixed points
- Waves and wave equations: One mathematics for sound, light, matter waves and gravitational waves

## Latent candidate pairs (0)

## Shared papers (2 note pairs; algorithmic, weak evidence)
- 00-foundations/mathematical-methods/complex-analysis-and-special-functions <-> 10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks: "An introduction to the theory of diffusive shock acceleration of energetic particles in te" (1983)
- 00-foundations/computational-physics <-> 10-plasma-physics/magnetohydrodynamics: "Interstellar Turbulence I: Observations and Processes" (2004)