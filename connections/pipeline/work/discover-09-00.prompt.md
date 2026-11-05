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

# Your set: 09-00 (Astrophysics and Cosmology with Foundations)

## Nodes (69)
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

## Explicit cross-links already written in the notes (6): each becomes a "written" record
- 00-foundations/measurement-and-data-analysis/statistical-inference-in-physics -> 09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history
- 09-astrophysics-and-cosmology/cosmology -> 00-foundations/measurement-and-data-analysis/statistical-inference-in-physics
- 09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history -> 00-foundations/measurement-and-data-analysis/statistical-inference-in-physics
- 09-astrophysics-and-cosmology/cosmology/hubble-tension-and-cosmological-tensions -> 00-foundations/measurement-and-data-analysis/uncertainty-and-error-propagation
- 09-astrophysics-and-cosmology/dark-matter/alternatives-mond-and-modified-gravity -> 00-foundations/history-and-philosophy-of-physics/philosophy-of-physics
- 09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-detection -> 00-foundations/measurement-and-data-analysis/statistical-inference-in-physics

## Shared curated concepts (12)
- Bose–Einstein condensation and superfluidity: Macroscopic occupation of one quantum state — cold atoms, helium, neutron stars, superconductors
- Chaos and nonlinear dynamics: Deterministic unpredictability; ergodicity as the bridge to statistical mechanics
- Diffusion, Brownian motion and stochastic processes: Random microscopic kicks produce universal macroscopic laws
- Emergence: The whole has laws its parts do not — the organizing theme of many-body physics
- Equations of state: Pressure–density relations connect microphysics to stars, nuclei and the cosmos
- Hydrodynamics and continuum descriptions: Long-wavelength dynamics of conserved densities — from water to quark–gluon plasma
- Noether symmetries and conservation: Continuous symmetry ⇔ conserved charge
- Oscillators and resonance: The universal small-oscillation model and its quantum version
- Scattering theory: Probing structure by what comes out — from atoms to quarks to galaxies
- Statistical inference: How evidence is weighed — from discovery claims to cosmological parameters
- Vacuum energy and fluctuations: The quantum vacuum has structure, with measurable and cosmological consequences
- Waves and wave equations: One mathematics for sound, light, matter waves and gravitational waves

## Latent candidate pairs (0)

## Shared papers (2 note pairs; algorithmic, weak evidence)
- 00-foundations/computational-physics/monte-carlo-methods <-> 09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background: "Cosmological parameters from CMB and other data: A Monte Carlo approach" (2002)
- 00-foundations/measurement-and-data-analysis/uncertainty-and-error-propagation <-> 09-astrophysics-and-cosmology/cosmology/hubble-tension-and-cosmological-tensions: "A Comprehensive Measurement of the Local Value of the Hubble Constant with 1 km s$^{−1}$ M" (2022)