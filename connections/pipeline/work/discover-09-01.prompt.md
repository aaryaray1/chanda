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

# Your set: 09-01 (Astrophysics and Cosmology with Classical Mechanics)

## Nodes (72)
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
- 09-astrophysics-and-cosmology | The physics of stars, galaxies and the universe as a whole — stellar astrophysics, galaxies, cosmology, dark matter, high-energy and astroparticle phy
- 09-astrophysics-and-cosmology/cosmology | The universe as a physical system — FLRW expansion, the CMB, inflation, dark energy, large-scale structure and BAO, the Hubble tension and gravitation
- 09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background | The relic radiation from recombination — its blackbody spectrum, temperature and polarization anisotropies, acoustic peaks, lensing and the parameters
- 09-astrophysics-and-cosmology/cosmology/dark-energy | The cause of cosmic acceleration — the cosmological constant and its problem, dynamical dark energy, supernova and BAO measurements, and DESI's hints 
- 09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history | Homogeneous, isotropic cosmological models — the FLRW metric, Friedmann equations, cosmic components, distances and the ΛCDM parameters.
- 09-astrophysics-and-cosmology/cosmology/gravitational-lensing | Bending of light by mass — strong lensing and Einstein rings, weak lensing and cosmic shear, microlensing, time-delay cosmography.
- 09-astrophysics-and-cosmology/cosmology/hubble-tension-and-cosmological-tensions | The ~5σ disagreement between local and early-universe determinations of H₀, the S₈ tension, and proposed systematic and new-physics explanations.
- 09-astrophysics-and-cosmology/cosmology/inflation | A period of accelerated expansion in the very early universe — solving the horizon and flatness problems, generating primordial fluctuations, and its 
- 09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao | The cosmic web — growth of density perturbations, the matter power spectrum, galaxy surveys, redshift-space distortions and baryon acoustic oscillatio
- 09-astrophysics-and-cosmology/dark-matter | Non-luminous matter making up ~85% of all matter — astrophysical evidence, direct and indirect detection searches, modified-gravity alternatives and s
- 09-astrophysics-and-cosmology/dark-matter/alternatives-mond-and-modified-gravity | Modified Newtonian dynamics and relativistic extensions as alternatives to particle dark matter — successes on galaxy scales, problems on cluster and 
- 09-astrophysics-and-cosmology/dark-matter/astrophysical-evidence-for-dark-matter | The multiple, independent lines of evidence — galaxy rotation curves, cluster dynamics and lensing, the Bullet Cluster, CMB peaks and structure format
- 09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure | Testing dark-matter models on sub-galactic scales — cusp–core, missing satellites, too-big-to-fail, and self-interacting, warm and fuzzy dark matter.
- 09-astrophysics-and-cosmology/dark-matter/direct-detection | Searching for dark-matter particles scattering in terrestrial detectors — liquid-noble TPCs, cryogenic bolometers, low-mass techniques and the neutrin
- 09-astrophysics-and-cosmology/dark-matter/indirect-detection | Looking for dark-matter annihilation or decay products — gamma rays, cosmic-ray antimatter, neutrinos and X-ray lines from halos and dwarf galaxies.
- 09-astrophysics-and-cosmology/galaxies | How galaxies form and evolve — hierarchical structure formation, the Milky Way, active galactic nuclei and supermassive black holes, galaxy clusters a
- 09-astrophysics-and-cosmology/galaxies/active-galactic-nuclei-and-supermassive-black-holes | Accreting supermassive black holes — quasars, Seyferts and blazars, unified models, relativistic jets, black-hole–galaxy co-evolution and feedback.
- 09-astrophysics-and-cosmology/galaxies/galaxy-clusters | The largest gravitationally bound structures — dark-matter-dominated mass budgets, hot intracluster gas, the Sunyaev–Zel'dovich effect and clusters as
- 09-astrophysics-and-cosmology/galaxies/galaxy-formation-and-evolution | From dark-matter halos to galaxies — gas cooling, star formation, feedback, morphology, scaling relations and cosmological simulations.
- 09-astrophysics-and-cosmology/galaxies/high-redshift-universe-and-reionization | The first stars and galaxies, cosmic dawn, the epoch of reionization, the 21-cm signal and JWST discoveries at z > 10.
- 09-astrophysics-and-cosmology/galaxies/the-milky-way | Our galaxy's structure, dynamics and history — disk, bulge, bar and halo, Gaia's 6D map, galactic archaeology, and the Galactic Centre black hole.
- 09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle | The violent universe and its messengers — cosmic rays, gamma-ray bursts, high-energy neutrinos, multi-messenger events, fast radio bursts and magnetar
- 09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays | Relativistic charged particles from space — the energy spectrum and composition, Galactic and extragalactic sources, diffusive shock acceleration and 
- 09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/fast-radio-bursts-and-magnetars | Millisecond radio flashes from cosmological distances, repeaters and non-repeaters, the magnetar connection, and FRBs as probes of intergalactic baryo
- 09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/gamma-ray-bursts | The most luminous explosions — long GRBs from collapsing massive stars, short GRBs from compact mergers, relativistic jets, fireball physics and after
- 09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/multi-messenger-astronomy | Combining gravitational waves, photons, neutrinos and cosmic rays from the same sources — GW170817, kilonovae, alert networks and what they teach.
- 09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/neutrino-astronomy | Observing the universe with neutrinos — IceCube and KM3NeT, the diffuse astrophysical flux, blazar and Seyfert sources, the Galactic plane and SN 1987
- 09-astrophysics-and-cosmology/planetary-science-and-exoplanets | Planets in our Solar System and around other stars — detection methods, atmospheres, formation in protoplanetary disks, orbital dynamics and habitabil
- 09-astrophysics-and-cosmology/planetary-science-and-exoplanets/astrobiology-and-habitability | Conditions for life beyond Earth — habitable zones, planetary climate and atmospheric retention, biosignature gases, Solar System ocean worlds and the
- 09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-atmospheres | Measuring the composition and structure of exoplanet atmospheres — transmission and emission spectroscopy, phase curves, clouds and hazes, JWST result
- 09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-detection | Finding planets around other stars — radial velocity, transits, microlensing, direct imaging, astrometry and timing; survey demographics.
- 09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks | How planets form — protoplanetary disk physics, dust growth, pebble accretion, core accretion vs. gravitational instability, migration, and ALMA disk 
- 09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics | Orbits and evolution of planets and small bodies — resonances, chaos, the Nice model of giant-planet migration, asteroids, Kuiper belt and comets.
- 09-astrophysics-and-cosmology/stellar-astrophysics | How stars are built, shine, evolve and die — stellar structure, the Sun, supernovae and transients, compact remnants, binaries and stellar populations
- 09-astrophysics-and-cosmology/stellar-astrophysics/binary-stars-and-stellar-populations | Binaries and mass transfer, the initial mass function, star clusters, population synthesis and stellar archaeology.
- 09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects | White dwarfs, neutron stars, pulsars, magnetars and stellar-mass black holes — degenerate matter, maximum masses and observational signatures.
- 09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution | The equations of stellar structure, energy transport, the HR diagram, and evolution from protostar through main sequence to giant phases and remnants.
- 09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients | Stellar explosions and other transients — core-collapse and Type Ia supernovae, light curves, remnants, and time-domain surveys like ZTF and Rubin.
- 09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology | The Sun as the best-studied star — standard solar models, helioseismic inversion of the interior, solar neutrinos, the solar abundance problem and the

## Explicit cross-links already written in the notes (7): each becomes a "written" record
- 01-classical-mechanics/newtonian-mechanics/central-forces-and-orbits -> 09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics
- 01-classical-mechanics/newtonian-mechanics/conservation-laws -> 09-astrophysics-and-cosmology/galaxies/galaxy-clusters
- 09-astrophysics-and-cosmology/galaxies/galaxy-clusters -> 01-classical-mechanics/newtonian-mechanics/conservation-laws
- 09-astrophysics-and-cosmology/planetary-science-and-exoplanets -> 01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics
- 09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks -> 01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics
- 09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics -> 01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics
- 09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics -> 01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos

## Shared curated concepts (14)
- Bose–Einstein condensation and superfluidity: Macroscopic occupation of one quantum state — cold atoms, helium, neutron stars, superconductors
- Chaos and nonlinear dynamics: Deterministic unpredictability; ergodicity as the bridge to statistical mechanics
- Diffusion, Brownian motion and stochastic processes: Random microscopic kicks produce universal macroscopic laws
- Elasticity and continuum mechanics: Continuum response of solids — from metals to neutron-star crusts and cells
- Hydrodynamics and continuum descriptions: Long-wavelength dynamics of conserved densities — from water to quark–gluon plasma
- Hydrostatic and virial equilibrium: Balance of pressure and gravity from stars to clouds to clusters
- Instabilities: Small perturbations that grow — fluids, plasmas, stars, lasers
- Magnetohydrodynamics, dynamos and reconnection: Conducting fluids carry and amplify magnetic fields — lab, solar, galactic
- Noether symmetries and conservation: Continuous symmetry ⇔ conserved charge
- Oscillators and resonance: The universal small-oscillation model and its quantum version
- Scattering theory: Probing structure by what comes out — from atoms to quarks to galaxies
- Solitons and nonlinear waves: Shape-preserving waves where nonlinearity balances dispersion
- Topological defects: Order-parameter singularities classified by homotopy — from liquid crystals to the early universe
- Waves and wave equations: One mathematics for sound, light, matter waves and gravitational waves

## Latent candidate pairs (0)

## Shared papers (2 note pairs; algorithmic, weak evidence)
- 01-classical-mechanics/continuum-and-fluid-mechanics/turbulence <-> 09-astrophysics-and-cosmology/stellar-astrophysics/binary-stars-and-stellar-populations: "Galactic stellar and substellar initial mass function" (2003)
- 01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics <-> 09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics: "Solar system dynamics" (1999)