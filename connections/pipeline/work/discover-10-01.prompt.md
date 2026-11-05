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

# Your set: 10-01 (Plasma Physics with Classical Mechanics)

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

## Explicit cross-links already written in the notes (10): each becomes a "written" record
- 01-classical-mechanics/continuum-and-fluid-mechanics -> 10-plasma-physics/magnetohydrodynamics
- 01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection -> 10-plasma-physics/inertial-and-laser-plasmas/inertial-confinement-fusion
- 01-classical-mechanics/continuum-and-fluid-mechanics/turbulence -> 10-plasma-physics/magnetohydrodynamics/mhd-turbulence
- 10-plasma-physics/inertial-and-laser-plasmas -> 01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection
- 10-plasma-physics/inertial-and-laser-plasmas/inertial-confinement-fusion -> 01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection
- 10-plasma-physics/magnetic-confinement-fusion/stellarators -> 01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos
- 10-plasma-physics/magnetic-confinement-fusion/turbulent-transport-and-gyrokinetics -> 01-classical-mechanics/continuum-and-fluid-mechanics/turbulence
- 10-plasma-physics/magnetohydrodynamics -> 01-classical-mechanics/continuum-and-fluid-mechanics
- 10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves -> 01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow
- 10-plasma-physics/magnetohydrodynamics/mhd-turbulence -> 01-classical-mechanics/continuum-and-fluid-mechanics/turbulence

## Shared curated concepts (17)
- Bose–Einstein condensation and superfluidity: Macroscopic occupation of one quantum state — cold atoms, helium, neutron stars, superconductors
- Chaos and nonlinear dynamics: Deterministic unpredictability; ergodicity as the bridge to statistical mechanics
- Confinement and chiral symmetry breaking: QCD's strong coupling generates hadron masses and new phases of matter
- Decoherence and open quantum systems: How environments make quantum systems look classical
- Diffusion, Brownian motion and stochastic processes: Random microscopic kicks produce universal macroscopic laws
- Hydrodynamics and continuum descriptions: Long-wavelength dynamics of conserved densities — from water to quark–gluon plasma
- Hydrostatic and virial equilibrium: Balance of pressure and gravity from stars to clouds to clusters
- Instabilities: Small perturbations that grow — fluids, plasmas, stars, lasers
- Lasers, coherence and stimulated emission: Phase-coherent light from stimulated emission; coherence as an order parameter
- Magnetohydrodynamics, dynamos and reconnection: Conducting fluids carry and amplify magnetic fields — lab, solar, galactic
- Oscillators and resonance: The universal small-oscillation model and its quantum version
- Quasiparticles and collective modes: Interacting systems behave like gases of emergent particles
- Solitons and nonlinear waves: Shape-preserving waves where nonlinearity balances dispersion
- Spin and angular momentum: Rotational structure and its coupling to motion and fields
- Turbulence and cascades: Multiscale chaotic flow in fluids, plasmas, astrophysics and wave systems
- Universality and scaling: Microscopically different systems share exponents near fixed points
- Waves and wave equations: One mathematics for sound, light, matter waves and gravitational waves

## Latent candidate pairs (2)
- 01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation <-> 10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping (score 0.47; shares Instabilities, Oscillators and resonance, Diffusion, Brownian motion and stochastic processes)
- 01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection <-> 10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping (score 0.45; shares Waves and wave equations, Instabilities, Diffusion, Brownian motion and stochastic processes)

## Shared papers (4 note pairs; algorithmic, weak evidence)
- 01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection <-> 10-plasma-physics/inertial-and-laser-plasmas/inertial-confinement-fusion: "Development of the indirect-drive approach to inertial confinement fusion and the target p" (1995)
- 01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics <-> 10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters: "A Model for Collision Processes in Gases. I. Small Amplitude Processes in Charged and Neut" (1954)
- 01-classical-mechanics/continuum-and-fluid-mechanics/turbulence <-> 10-plasma-physics/magnetohydrodynamics/dynamo-theory: "Instability, turbulence, and enhanced transport in accretion disks" (1998)
- 01-classical-mechanics/continuum-and-fluid-mechanics/turbulence <-> 10-plasma-physics/magnetohydrodynamics/mhd-turbulence: "Instability, turbulence, and enhanced transport in accretion disks" (1998)