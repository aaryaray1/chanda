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

# Your set: 09-within (links between different subfields of Astrophysics and Cosmology)

## Nodes (39)
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

## Explicit cross-links already written in the notes (19): each becomes a "written" record
- 09-astrophysics-and-cosmology/cosmology/dark-energy -> 09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients
- 09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao -> 09-astrophysics-and-cosmology/galaxies/galaxy-formation-and-evolution
- 09-astrophysics-and-cosmology/dark-matter -> 09-astrophysics-and-cosmology/cosmology/gravitational-lensing
- 09-astrophysics-and-cosmology/dark-matter/astrophysical-evidence-for-dark-matter -> 09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background
- 09-astrophysics-and-cosmology/dark-matter/astrophysical-evidence-for-dark-matter -> 09-astrophysics-and-cosmology/galaxies/galaxy-clusters
- 09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure -> 09-astrophysics-and-cosmology/cosmology/gravitational-lensing
- 09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure -> 09-astrophysics-and-cosmology/galaxies/galaxy-formation-and-evolution
- 09-astrophysics-and-cosmology/dark-matter/indirect-detection -> 09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays
- 09-astrophysics-and-cosmology/galaxies -> 09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao
- 09-astrophysics-and-cosmology/galaxies -> 09-astrophysics-and-cosmology/dark-matter
- 09-astrophysics-and-cosmology/galaxies/active-galactic-nuclei-and-supermassive-black-holes -> 09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/neutrino-astronomy
- 09-astrophysics-and-cosmology/galaxies/galaxy-clusters -> 09-astrophysics-and-cosmology/dark-matter/astrophysical-evidence-for-dark-matter
- 09-astrophysics-and-cosmology/galaxies/galaxy-formation-and-evolution -> 09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure
- 09-astrophysics-and-cosmology/galaxies/high-redshift-universe-and-reionization -> 09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background
- 09-astrophysics-and-cosmology/galaxies/the-milky-way -> 09-astrophysics-and-cosmology/dark-matter/astrophysical-evidence-for-dark-matter
- 09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/fast-radio-bursts-and-magnetars -> 09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects
- 09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-detection -> 09-astrophysics-and-cosmology/cosmology/gravitational-lensing
- 09-astrophysics-and-cosmology/stellar-astrophysics/binary-stars-and-stellar-populations -> 09-astrophysics-and-cosmology/galaxies/the-milky-way
- 09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients -> 09-astrophysics-and-cosmology/cosmology/dark-energy

## Shared curated concepts (14)
- Bose–Einstein condensation and superfluidity: Macroscopic occupation of one quantum state — cold atoms, helium, neutron stars, superconductors
- Compact objects: Matter at extreme density and gravity — where nuclear, particle, GR and astro meet
- Dark matter: Unseen mass connecting cosmology, particle physics and precision detectors
- Diffusion, Brownian motion and stochastic processes: Random microscopic kicks produce universal macroscopic laws
- Gravitational waves: Ripples of spacetime as a new messenger
- Hydrodynamics and continuum descriptions: Long-wavelength dynamics of conserved densities — from water to quark–gluon plasma
- Hydrostatic and virial equilibrium: Balance of pressure and gravity from stars to clouds to clusters
- Inflation and early-universe physics: Field theory and statistical physics applied to the first instants
- Instabilities: Small perturbations that grow — fluids, plasmas, stars, lasers
- Magnetohydrodynamics, dynamos and reconnection: Conducting fluids carry and amplify magnetic fields — lab, solar, galactic
- Neutrinos: Weakly interacting probes from reactors, the Sun, supernovae and the early universe
- Nucleosynthesis: How the elements formed, linking nuclear rates to stellar and cosmic histories
- Radiation, blackbody and radiative transfer: Matter–light equilibrium, from the CMB to climate
- Statistical inference: How evidence is weighed — from discovery claims to cosmological parameters

## Latent candidate pairs (1)
- 09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/multi-messenger-astronomy <-> 09-astrophysics-and-cosmology/stellar-astrophysics (score 0.67; shares Nucleosynthesis, Gravitational waves, Neutrinos)

## Shared papers (0 note pairs; algorithmic, weak evidence)