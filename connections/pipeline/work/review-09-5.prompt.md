You are the astrophysicist, the specialist for 09 (Astrophysics and Cosmology) in this physics knowledge base.

# Specialist review brief (one packet per run)

You are the specialist for the branch named above. Below this brief are your branch's notes (the codex sections for every node in the packet) and the packet itself, one proposed connection per line, each with at least one end in your branch. A first-pass analyst wrote these records quickly. You are the check between them and the published registry, so review every one from **your branch's side**.

**Confirm only a record you would sign as written.** "Basically right" is a revise. A spot check of 30 records confirmed in earlier packets found that about a quarter had a wrong kind, an inflated strength, an overclaim or filler.

## Check every record against all of these
1. **Physics and facts.** Every statement holds: equations, numbers, dates, names, who did what first. Words such as *every*, *only*, *always*, *first*, *exactly* or *proves* must be strictly true; otherwise revise.
2. **Kind.**
   - `identity`: the same law, equation or object in both notes, mapping one to one, with no regime where the match fails. If the record needs a `breaks`, it is not an identity: make it `analogy` or `mechanism`.
   - `mechanism`: the same physical cause at work in both.
   - `method transfer`: a named technique that moved across and did named work there.
   - `shared object`: a system both fields study.
   - `duality`: an exact map between two descriptions of the same physics.
   - `historical`: an idea that migrated from one field to the other.
   - `analogy`: the same form with different physics. `breaks` must name the real point of failure.
3. **Strength.**
   - 3: structural in *both* fields; a graduate course in each would teach the link.
   - 2: a substantial, specific link.
   - 1: suggestive, narrow or one-sided.

   A broad "Y uses X" link is never 3.
4. **Confidence.**
   - `established`: textbook consensus.
   - `current research`: active work, including results that are only numerical or carry caveats.
   - `proposed`: speculative, or disputed in the literature. Say who disputes it in `breaks`.
5. **Content.** The summary must say what maps to what.
   - Generic overlap with no named technique and consequence is trivial. Examples: "both use PDEs", "Y uses statistics", "X is described by continuum theory". Reject it, or revise it into the specific link if you know one.
   - Cut filler such as "links to reviews" or "is important for".
6. **Nodes.** The paths on your side are the most fitting notes.
7. **Duplicates.** Two records may join the same pair of notes with the same idea. Keep the better one, revising it to absorb anything the other adds, and reject the other with `duplicate_of`.

Work from the notes below and your own knowledge. Do not run commands or search the folder. Read a node README only if the notes below are not enough, and at most 3 of them.

## Answer: JSON Lines ONLY
Give one line per packet record, in packet order. No prose, no headings, no code fences; anything else is discarded.
- `{"id": "C0123", "verdict": "confirm"}` when it passes every check as written.
- `{"id": "C0123", "verdict": "revise", "reason": "<≤25 words>", "fix": {"summary": "...", "kind": "...", "confidence": "...", "strength": 2, "breaks": "...", "map": "...", "a": "<better path>", "b": "<better path>"}}`. Include only the fields that change.
- `{"id": "C0123", "verdict": "reject", "reason": "<≤25 words: the physics error, or why it is trivial>"}`.
- `{"id": "C0124", "verdict": "reject", "reason": "duplicate of C0123", "duplicate_of": "C0123"}`.

After the verdicts you may add up to 8 important connections touching your branch that the packet lacks, as `{"verdict": "add", "record": {"a": "<node path>", "b": "<node path>", "name": "<≤60 chars>", "kind": "...", "summary": "<≤45 words>", "map": "...", "breaks": "<required for analogy>", "confidence": "established|current research|proposed", "strength": 3|2|1, "sources": []}}`. Hold additions to the same standard.

Reject physics errors, trivial links and duplicates. A real connection that is mis-stated, mislabelled or over-rated is a revise, not a reject.


---

# Your branch notes: the codex sections for the nodes in this packet

## Field overview · `knowledge/09-astrophysics-and-cosmology`

> **Specialist:** `astrophysicist` · **arXiv:** astro-ph.CO, .GA, .SR, .HE, .EP, .IM · **Literature source:** INSPIRE-HEP (citation-ranked; strong astro-ph coverage) + arXiv (latest); OpenAlex for exoplanets

#### What this field studies
Astrophysics applies all of physics — gravity, nuclear and particle physics, plasma physics, radiative transfer, statistical mechanics — to the cosmos. Cosmology studies the universe as a whole: its expansion, composition (~5% ordinary matter, ~27% dark matter, ~68% dark energy), origin and fate. Observations now span the electromagnetic spectrum, neutrinos, cosmic rays and gravitational waves, making the universe a laboratory for physics no Earth-based experiment can reach.

#### Conventions used in this branch
- Units: cgs is still common (erg, g cm⁻³); distances in pc ($3.086\times10^{16}$ m), kpc, Mpc; masses in $M_\odot=1.989\times10^{30}$ kg; luminosities in $L_\odot=3.828\times10^{26}$ W.
- Hubble constant $H_0=100h$ km s⁻¹ Mpc⁻¹; redshift $1+z=a_0/a$; magnitudes $m-M=5\log_{10}(d/10\,\text{pc})$.
- Cosmological parameters: quote the dataset (e.g., Planck 2018 TT,TE,EE+lowE+lensing) because values differ between analyses.

#### Historical spine
1838 stellar parallax · 1910s Hertzsprung–Russell diagram · 1912 Leavitt's Cepheid law; cosmic rays · 1917 Einstein's static universe · 1922–27 Friedmann, Lemaître · 1929 Hubble's law · 1931 Chandrasekhar limit · 1933 Zwicky's dark matter · 1939 stellar fusion (Bethe) · 1948 Big Bang nucleosynthesis · 1963 quasars · 1965 CMB · 1967 pulsars · 1970s flat rotation curves · 1981 inflation · 1992 CMB anisotropies (COBE) · 1995 first exoplanet around a Sun-like star · 1998 accelerating expansion · 2013 PeV astrophysical neutrinos · 2015–17 gravitational waves and multi-messenger astronomy · 2022 JWST · 2024–25 DESI hints of evolving dark energy.

#### Canonical textbooks
- Carroll & Ostlie, *An Introduction to Modern Astrophysics* — undergraduate standard.
- Kippenhahn, Weigert & Weiss, *Stellar Structure and Evolution*; Binney & Tremaine, *Galactic Dynamics*.
- Ryden, *Introduction to Cosmology*; Dodelson & Schmidt, *Modern Cosmology*; Weinberg, *Cosmology*; Peebles, *Principles of Physical Cosmology*.
- Rybicki & Lightman, *Radiative Processes in Astrophysics*; Longair, *High Energy Astrophysics*; Seager, *Exoplanets*.

#### Live frontiers
- Is dark energy a cosmological constant? (DESI BAO + supernovae hint at evolution, ~3–4σ.)
- The Hubble tension: ~5σ between local distance ladder and early-universe inference.
- JWST's surprisingly bright and massive galaxies at $z>10$.
- Origin of ultra-high-energy cosmic rays and astrophysical neutrinos.

#### How the specialist works here
Estimate scales first (Eddington luminosity, Jeans mass, free-fall and diffusion times), track units carefully between cgs and SI, distinguish observables from model-dependent inferences, state which cosmology/dataset numbers come from, and be explicit about selection effects in surveys.

## Cosmology · `knowledge/09-astrophysics-and-cosmology/cosmology`

#### Overview
The standard model of cosmology, ΛCDM, describes a spatially flat universe that began hot and dense 13.8 billion years ago, expanded and cooled, formed light elements in minutes, released the CMB at 380 000 years, and grew structure from tiny primordial fluctuations — likely produced by inflation. Six parameters fit the CMB, BAO, supernovae and lensing data to percent precision, yet the two dominant components (dark matter and dark energy) are not understood, and a few datasets are now in tension.

#### Key equations
$$H^2=\left(\frac{\dot a}{a}\right)^2=\frac{8\pi G}{3}\rho-\frac{kc^2}{a^2}+\frac{\Lambda c^2}{3},\qquad \frac{\ddot a}{a}=-\frac{4\pi G}{3}\left(\rho+\frac{3p}{c^2}\right)+\frac{\Lambda c^2}{3}$$
$$\Omega_m\approx0.315,\quad\Omega_\Lambda\approx0.685,\quad H_0\approx67.4\ \text{km s}^{-1}\text{Mpc}^{-1}\ (\text{Planck 2018}),\quad n_s\approx0.965$$

#### Open problems
- Nature of dark energy and dark matter; the cosmological-constant problem (~120 orders of magnitude).
- Hubble and $S_8$ tensions — new physics or systematics?
- Primordial gravitational waves ($r<0.036$) — the smoking gun of inflation, not yet seen.

#### Connections
- [General relativity](knowledge/05-relativity-and-gravitation/general-relativity/README.md) · [Big Bang nucleosynthesis](knowledge/07-nuclear-physics/nuclear-astrophysics/big-bang-nucleosynthesis/README.md) · [Baryogenesis](knowledge/06-particle-physics/beyond-the-standard-model/baryogenesis-and-matter-antimatter/README.md) · [Statistical inference](knowledge/00-foundations/measurement-and-data-analysis/statistical-inference-in-physics/README.md)

### Cosmic microwave background · `knowledge/09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background`

**Scope.** Recombination and last scattering ($z\approx1090$), perfect blackbody at 2.7255 K (FIRAS), dipole, $10^{-5}$ anisotropies (COBE, WMAP, Planck), angular power spectrum and acoustic peaks, Silk damping, E- and B-mode polarization, reionization bump, CMB lensing, spectral distortions, ACT/SPT, Simons Observatory and CMB-S4, $N_{\text{eff}}$ and $\sum m_\nu$ constraints.

**Core ideas.**
- Before recombination, photons and baryons oscillated as a fluid; the peaks are snapshots of these sound waves.
- First-peak position ($\ell\approx220$) measures spatial flatness; peak heights measure baryon and matter densities.
- Primordial B-modes would be a signature of inflationary gravitational waves.

**Key equations.**
$$\frac{\Delta T}{T}(\hat n)=\sum_{\ell m}a_{\ell m}Y_{\ell m}(\hat n),\qquad C_\ell=\langle|a_{\ell m}|^2\rangle,\qquad T_0=2.7255\ \text{K}$$

**See also.** [Quantum statistics (blackbody)](knowledge/03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics/README.md) · [Scattering of light (Thomson)](knowledge/02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light/README.md)

### Gravitational lensing · `knowledge/09-astrophysics-and-cosmology/cosmology/gravitational-lensing`

**Scope.** Deflection angle and the 1919 eclipse test, lens equation, Einstein radius, multiple images and arcs, caustics, time delays and $H_0$, weak lensing shear and convergence, cosmic shear surveys (KiDS, DES, HSC, Euclid), CMB lensing, galaxy–galaxy lensing, microlensing exoplanets and MACHO searches.

**Core ideas.**
- Lensing measures total mass, dark or luminous, without assumptions about dynamics.
- Weak lensing distorts galaxy shapes by ~1%; statistics over millions of galaxies map dark matter.
- Microlensing light curves reveal planets and compact objects too faint to see.

**Key equations.**
$$\hat\alpha=\frac{4GM}{c^2b},\qquad \theta_E=\sqrt{\frac{4GM}{c^2}\frac{D_{ls}}{D_lD_s}},\qquad \boldsymbol\beta=\boldsymbol\theta-\frac{D_{ls}}{D_s}\hat{\boldsymbol\alpha}(\boldsymbol\theta)$$

**See also.** [Tests of GR](knowledge/05-relativity-and-gravitation/general-relativity/tests-of-general-relativity/README.md) · [Geometric optics](knowledge/02-electromagnetism-and-optics/classical-optics/geometric-optics/README.md)

## Dark matter · `knowledge/09-astrophysics-and-cosmology/dark-matter`

#### Overview
Rotation curves, cluster dynamics, lensing, the CMB acoustic peaks and the growth of structure all require ~5× more matter than baryons provide. This matter is cold (non-relativistic early on), collisionless to good approximation, and interacts at most feebly with light. Despite decades of searches — underground xenon detectors, gamma-ray telescopes, colliders — its identity is unknown.

#### Key equations
$$\Omega_ch^2\approx0.120,\qquad \rho_{\text{NFW}}(r)=\frac{\rho_s}{(r/r_s)(1+r/r_s)^2},\qquad \rho_\odot^{\text{DM}}\approx0.3\text{–}0.4\ \text{GeV cm}^{-3}$$

#### Open problems
- What is it? Every major WIMP search so far is null; xenon detectors approach the neutrino fog.
- Do small-scale tensions require non-cold or self-interacting dark matter, or better baryonic physics?

#### Connections
- [Dark-matter particle candidates](knowledge/06-particle-physics/beyond-the-standard-model/dark-matter-particle-candidates/README.md) · [Axions](knowledge/06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector/README.md) · [Gravitational lensing](knowledge/09-astrophysics-and-cosmology/cosmology/gravitational-lensing/README.md)

### Direct detection · `knowledge/09-astrophysics-and-cosmology/dark-matter/direct-detection`

**Scope.** Standard halo model and recoil spectra, spin-independent and spin-dependent cross sections, liquid xenon (LZ, XENONnT, PandaX) and argon (DarkSide) TPCs, cryogenic detectors (SuperCDMS, CRESST), electron-recoil searches for sub-GeV DM, annual modulation and the DAMA/LIBRA controversy (refuted by COSINE, ANAIS), coherent neutrino background ("neutrino fog"), haloscopes for axions.

**Core ideas.**
- WIMP–nucleus elastic scattering deposits keV-scale recoil energies — needs ultra-low background deep underground.
- Rates scale with $A^2$ for coherent spin-independent scattering, favouring heavy targets like xenon.
- Solar and atmospheric neutrinos produce an irreducible background below which discovery becomes statistically hard.

**Key equations.**
$$\frac{dR}{dE_R}=\frac{\rho_\chi}{m_\chi m_N}\int_{v_{\min}}^{\infty}vf(v)\frac{d\sigma}{dE_R}d^3v,\qquad v_{\min}=\sqrt{\frac{m_NE_R}{2\mu^2}}$$

**See also.** [Axions](knowledge/06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector/README.md) · [Radiation detection](knowledge/07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry/README.md)

## Galaxies · `knowledge/09-astrophysics-and-cosmology/galaxies`

#### Overview
Galaxies form when gas cools and condenses inside dark-matter halos that grow hierarchically by mergers. Their stars, gas, dust and central supermassive black holes co-evolve through feedback; the cosmic star-formation rate peaked ~10 Gyr ago (z ≈ 2). Our own Milky Way is now mapped in 6D by Gaia, and JWST is revealing galaxies within 300 Myr of the Big Bang.

#### Key equations
$$M_J\sim\frac{\pi^{5/2}}{6}\frac{c_s^3}{G^{3/2}\rho^{1/2}},\qquad v_c(r)=\sqrt{\frac{GM(<r)}{r}},\qquad M_{\text{BH}}\propto\sigma^{4\text{–}5}$$

#### Open problems
- How did supermassive black holes of $10^9\,M_\odot$ form by $z\approx7$?
- What quenches star formation in massive galaxies?

#### Connections
- [Dark matter](knowledge/09-astrophysics-and-cosmology/dark-matter/README.md) · [Black-hole imaging](knowledge/05-relativity-and-gravitation/black-holes/black-hole-imaging-and-astrophysical-black-holes/README.md) · [Large-scale structure](knowledge/09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao/README.md)

### Active galactic nuclei and supermassive black holes · `knowledge/09-astrophysics-and-cosmology/galaxies/active-galactic-nuclei-and-supermassive-black-holes`

**Scope.** Discovery of quasars, accretion-disk spectra (Shakura–Sunyaev), broad- and narrow-line regions, reverberation mapping, unified model and viewing angle, radio-loud jets and superluminal motion, blazars, $M$–$\sigma$ relation, AGN feedback (quasar and radio modes), high-z quasars, little red dots (JWST), changing-look AGN.

**Core ideas.**
- AGN shine by accretion: efficiency $\eta\sim0.06$–0.4 depending on spin — far beyond fusion's 0.7%.
- Orientation explains much of the zoo (type 1 vs. type 2, blazars when the jet points at us).
- Black-hole masses scale tightly with host-bulge properties, implying co-evolution via feedback.

**Key equations.**
$$L=\eta\dot Mc^2,\qquad M_{\text{BH}}=f\frac{R_{\text{BLR}}\,\Delta v^2}{G},\qquad \beta_{\text{app}}=\frac{\beta\sin\theta}{1-\beta\cos\theta}$$

**See also.** [Black holes](knowledge/05-relativity-and-gravitation/black-holes/README.md) · [Neutrino astronomy (blazars)](knowledge/09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/neutrino-astronomy/README.md)

### Galaxy clusters · `knowledge/09-astrophysics-and-cosmology/galaxies/galaxy-clusters`

**Scope.** Zwicky's virial mass discrepancy, X-ray-emitting intracluster medium (~$10^7$–$10^8$ K), hydrostatic masses, thermal and kinetic SZ effects, weak and strong lensing masses, cool cores and AGN heating, cluster mergers (Bullet Cluster), cluster counts as probes of $\sigma_8$ and $\Omega_m$, scaling relations.

**Core ideas.**
- Mass budget: ~85% dark matter, ~12% hot gas, ~3% stars.
- The SZ effect is redshift-independent in surface brightness — clusters can be found at any distance.
- Cluster abundance is exponentially sensitive to the amplitude of density fluctuations.

**Key equations.**
$$M_{\text{vir}}\approx\frac{3\sigma_v^2R}{G},\qquad \frac{\Delta T}{T_{\text{CMB}}}=-2y,\ y=\frac{\sigma_T}{m_ec^2}\int n_ek_BT_e\,dl$$

**Landmark.** Kravtsov & Borgani (2012) — see [subfield landmarks](knowledge/09-astrophysics-and-cosmology/galaxies/README.md).

**See also.** [Conservation laws (virial theorem)](knowledge/01-classical-mechanics/newtonian-mechanics/conservation-laws/README.md) · [Astrophysical evidence for dark matter](knowledge/09-astrophysics-and-cosmology/dark-matter/astrophysical-evidence-for-dark-matter/README.md)

### The Milky Way · `knowledge/09-astrophysics-and-cosmology/galaxies/the-milky-way`

**Scope.** Thin and thick disks, bar and bulge, stellar halo and accreted streams (Gaia–Enceladus), rotation curve and dark-matter halo mass (~$10^{12}\,M_\odot$), Gaia DR3 astrometry for ~1.8 billion stars, chemical tagging and galactic archaeology, the Local Group, Magellanic Clouds, Sgr A* and S-star orbits, Fermi bubbles.

**Core ideas.**
- Gaia turned galactic dynamics into a 6D phase-space science: positions plus velocities for billions of stars.
- Stellar streams record past mergers and trace the dark-matter potential.
- S-star orbits weigh Sgr A* at ~4.3 million $M_\odot$ and test GR (gravitational redshift, Schwarzschild precession).

**Key equations.**
$$v_\odot\approx233\ \text{km s}^{-1},\ R_\odot\approx8.2\ \text{kpc};\qquad M_{\text{Sgr A}^*}\approx4.3\times10^6\,M_\odot$$

**See also.** [Black-hole imaging](knowledge/05-relativity-and-gravitation/black-holes/black-hole-imaging-and-astrophysical-black-holes/README.md) · [Astrophysical evidence for dark matter](knowledge/09-astrophysics-and-cosmology/dark-matter/astrophysical-evidence-for-dark-matter/README.md)

## High-energy astrophysics and astroparticle physics · `knowledge/09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle`

#### Overview
Nature's accelerators — supernova remnants, AGN jets, gamma-ray bursts, magnetars — produce particles up to $10^{20}$ eV, ten million times the LHC beam energy. They are studied through four messengers: photons (radio to TeV gamma rays), cosmic rays, neutrinos and gravitational waves. Combining them (multi-messenger astronomy) identified neutron-star mergers as kilonova and short-GRB engines and a blazar as a neutrino source.

#### Key equations
$$\frac{dN}{dE}\propto E^{-2}\ (\text{diffusive shock acceleration}),\qquad E_{\max}\sim ZeBRc\beta\ (\text{Hillas}),\qquad E_{\text{GZK}}\approx5\times10^{19}\ \text{eV}$$

#### Open problems
- Sources of ultra-high-energy cosmic rays; the "ankle" and composition puzzles.
- What powers fast radio bursts — are all of them magnetars?

#### Connections
- [Gravitational waves](knowledge/05-relativity-and-gravitation/gravitational-waves/README.md) · [Neutrino physics](knowledge/06-particle-physics/neutrino-physics/README.md) · [Astrophysical plasmas and shocks](knowledge/10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks/README.md)

### Cosmic rays · `knowledge/09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays`

**Scope.** Hess's balloon flights (1912), power-law spectrum ($E^{-2.7}$) with knee (~3 PeV) and ankle (~5 EeV), composition and isotopes (AMS-02, CALET, DAMPE), Galactic propagation and diffusion, supernova remnants as PeVatrons, extensive air showers (Auger, Telescope Array), GZK suppression via $p\gamma_{\text{CMB}}\to\Delta^+$, Amaterasu particle, cosmic-ray anisotropy, muon puzzle in air showers.

**Core ideas.**
- First-order Fermi acceleration at shocks naturally gives $E^{-2}$ source spectra; propagation steepens them.
- Above ~$5\times10^{19}$ eV protons lose energy on CMB photons within ~100 Mpc.
- Charged cosmic rays are deflected by magnetic fields, so arrival directions only weakly point to sources.

**Key equations.**
$$E_{\text{GZK}}\approx\frac{m_\pi(m_\pi+2m_p)c^4}{4E_{\gamma}}\approx6\times10^{19}\ \text{eV},\qquad r_L=\frac{E}{ZeBc}\approx1.1\ \text{kpc}\frac{E/\text{EeV}}{Z\,B/\mu\text{G}}$$

**See also.** [Relativistic kinematics (thresholds)](knowledge/05-relativity-and-gravitation/special-relativity/relativistic-kinematics-and-dynamics/README.md) · [Astrophysical plasmas and shocks](knowledge/10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks/README.md)

### Fast radio bursts and magnetars · `knowledge/09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/fast-radio-bursts-and-magnetars`

**Scope.** Lorimer burst (2007), CHIME/FRB catalogue of thousands, repeating sources (FRB 121102, 20180916B periodicity), host-galaxy localizations, dispersion and rotation measures, the Macquart relation and the missing baryons, SGR 1935+2154's Galactic FRB (2020), magnetar physics (B ~ $10^{14}$–$10^{15}$ G), emission mechanisms (curvature, synchrotron maser).

**Core ideas.**
- Dispersion measure $\propto\int n_e\,dl$ counts free electrons along the path — FRBs weigh the intergalactic medium.
- Brightness temperatures exceed $10^{35}$ K: emission must be coherent.
- At least some FRBs come from magnetars; whether all do is open.

**Key equations.**
$$\Delta t\approx4.15\ \text{ms}\left(\frac{\text{DM}}{\text{pc cm}^{-3}}\right)\left(\frac{\nu}{\text{GHz}}\right)^{-2},\qquad \langle\text{DM}_{\text{IGM}}\rangle\approx1000z\ \text{pc cm}^{-3}$$

**See also.** [Compact objects](knowledge/09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects/README.md) · [Plasma waves (dispersion)](knowledge/10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities/README.md)

## Planetary science and exoplanets · `knowledge/09-astrophysics-and-cosmology/planetary-science-and-exoplanets`

#### Overview
Since 1995, more than 6000 exoplanets have been confirmed. Most stars host planets; the most common types (super-Earths and sub-Neptunes) don't exist in our Solar System. Transit and radial-velocity surveys give sizes and masses; JWST transmission and emission spectroscopy now measures atmospheric chemistry; ALMA images planet-forming disks. The long-term goal: biosignatures on a rocky world in a habitable zone.

#### Key equations
$$K=\left(\frac{2\pi G}{P}\right)^{1/3}\frac{M_p\sin i}{(M_\star+M_p)^{2/3}}\frac{1}{\sqrt{1-e^2}},\qquad \frac{\Delta F}{F}\approx\left(\frac{R_p}{R_\star}\right)^2$$

#### Open problems
- Do rocky planets around M dwarfs keep atmospheres?
- Origin of the radius valley between super-Earths and sub-Neptunes.

#### Connections
- [Few-body and celestial mechanics](knowledge/01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics/README.md) · [Climate physics](knowledge/11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing/README.md) · [Molecular spectroscopy](knowledge/11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy/README.md)

### Astrobiology and habitability · `knowledge/09-astrophysics-and-cosmology/planetary-science-and-exoplanets/astrobiology-and-habitability`

**Scope.** Classical habitable zone and runaway/maximum greenhouse limits, M-dwarf flares and atmospheric escape, tidal locking, ocean worlds (Europa, Enceladus, Titan) and their missions, biosignature gases (O₂, O₃, CH₄+CO₂ disequilibrium), false positives, technosignatures, Drake equation and Fermi paradox, Habitable Worlds Observatory.

**Core ideas.**
- The habitable zone is where liquid surface water is possible for an Earth-like atmosphere — a necessary, not sufficient, condition.
- Chemical disequilibrium in an atmosphere is a more robust biosignature than any single gas.
- Subsurface oceans greatly expand where life might exist in our own Solar System.

**Key equations.**
$$d_{\text{HZ}}\approx\sqrt{\frac{L_\star}{L_\odot}}\ \text{AU}\times(0.95\text{–}1.67),\qquad T_{\text{eq}}=T_\star\sqrt{\frac{R_\star}{2a}}(1-A)^{1/4}$$

**Landmark.** Kasting, Whitmire & Reynolds (1993) — see [subfield landmarks](knowledge/09-astrophysics-and-cosmology/planetary-science-and-exoplanets/README.md).

**See also.** [Climate physics](knowledge/11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing/README.md) · [Physics of living systems](knowledge/11-interdisciplinary-physics/biophysics/physics-of-living-systems/README.md)

### Exoplanet atmospheres · `knowledge/09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-atmospheres`

**Scope.** Transmission spectra and scale height, secondary-eclipse emission and dayside temperatures, phase curves and heat redistribution, retrieval methods, clouds and hazes flattening spectra, hot Jupiters (H₂O, CO, CO₂, SO₂ photochemistry), sub-Neptunes (K2-18 b debate), rocky planets around M dwarfs (TRAPPIST-1 thermal emission), high-resolution ground-based cross-correlation.

**Core ideas.**
- Transit depth varies with wavelength by ~$2HR_p/R_\star^2$ — puffy, hot atmospheres are easiest.
- JWST detected CO₂ and photochemically produced SO₂ — chemistry is now quantitative.
- Biosignature claims require ruling out abiotic pathways; extraordinary claims need extraordinary data.

**Key equations.**
$$H=\frac{k_BT}{\mu m_Hg},\qquad \delta(\lambda)\approx\frac{R_p^2+2R_pN_HH}{R_\star^2}$$

**See also.** [Molecular spectroscopy](knowledge/11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy/README.md) · [Climate physics](knowledge/11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing/README.md)

### Planet formation and protoplanetary disks · `knowledge/09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks`

**Scope.** Disk structure and accretion (α-viscosity, MRI, winds), dust settling and radial drift, the metre-size barrier, streaming instability and planetesimals, pebble accretion, core accretion for giants vs. disk instability, snow lines, Type I/II migration, ALMA rings and gaps (HL Tau), disk lifetimes (~3–10 Myr), debris disks.

**Core ideas.**
- Dust must grow from μm to km sizes before drag drifts it into the star.
- Giant planets must form within the gas-disk lifetime; core accretion needs ~10 $M_\oplus$ cores.
- Disk substructures (rings, gaps, spirals) may be carved by young planets.

**Key equations.**
$$\nu=\alpha c_sH,\qquad \text{St}=\Omega_K t_s,\qquad M_{\text{iso}}\approx\frac{(2\pi\cdot2\sqrt3\,\Sigma_pa^2)^{3/2}}{(3M_\star)^{1/2}}$$

**See also.** [Low-Reynolds-number flow](knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics/README.md) · [MHD (MRI)](knowledge/10-plasma-physics/magnetohydrodynamics/README.md)

### Solar System dynamics · `knowledge/09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics`

**Scope.** Secular and resonant perturbations, Kirkwood gaps, Trojan asteroids, chaotic diffusion of inner planets (Laskar), Nice model and Late Heavy Bombardment, Grand Tack, Kuiper belt and scattered disk, Oort cloud and comets, Yarkovsky effect, Planet Nine hypothesis, near-Earth-object impact risk (DART mission).

**Core ideas.**
- The inner Solar System is chaotic with ~5 Myr Lyapunov times; Mercury has ~1% chance of destabilizing within 5 Gyr.
- Giant-planet migration reshaped the small-body populations.
- Resonances both protect (Neptune–Pluto 3:2) and destabilize (Kirkwood gaps).

**Key equations.**
$$\frac{P_1}{P_2}\approx\frac{p}{q}\ (\text{mean-motion resonance}),\qquad \lambda_{\text{Lyap}}^{-1}\approx5\ \text{Myr}$$

**See also.** [Few-body and celestial mechanics](knowledge/01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics/README.md) · [KAM theory](knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos/README.md)

## Stellar astrophysics · `knowledge/09-astrophysics-and-cosmology/stellar-astrophysics`

#### Overview
A star is a self-gravitating ball of plasma in hydrostatic equilibrium, powered by nuclear fusion. Mass essentially determines its life: low-mass stars burn for trillions of years and end as white dwarfs; massive stars live a few million years and die as core-collapse supernovae leaving neutron stars or black holes. Stellar physics underpins distance scales, galaxy evolution and nucleosynthesis.

#### Key equations
$$\frac{dP}{dr}=-\frac{Gm\rho}{r^2},\quad \frac{dm}{dr}=4\pi r^2\rho,\quad \frac{dL}{dr}=4\pi r^2\rho\epsilon,\quad \frac{dT}{dr}=-\frac{3\kappa\rho L}{16\pi acr^2T^3};\qquad L\propto M^{3.5}$$

#### Open problems
- The core-collapse explosion mechanism in 3D (neutrino-driven, magnetorotational).
- Progenitors of Type Ia supernovae (single vs. double degenerate).

#### Connections
- [Nuclear astrophysics](knowledge/07-nuclear-physics/nuclear-astrophysics/README.md) · [Plasma physics](knowledge/10-plasma-physics/README.md) · [Gravitational waves](knowledge/05-relativity-and-gravitation/gravitational-waves/README.md)

### Compact objects · `knowledge/09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects`

**Scope.** Electron degeneracy and the Chandrasekhar limit (~1.4 $M_\odot$), white-dwarf cooling and cosmochronology, neutron-star structure (TOV) and maximum mass (~2.2–2.3 $M_\odot$), pulsars as rotating magnetized neutron stars, millisecond pulsars and recycling, magnetars, X-ray binaries and accretion, stellar black holes and the mass gaps.

**Core ideas.**
- Degeneracy pressure holds white dwarfs and neutron stars up; above a critical mass relativity makes them unstable.
- Pulsar spin-down gives magnetic-field and age estimates; millisecond pulsars are the most precise natural clocks.
- Accretion onto compact objects is the most efficient luminous energy source after annihilation.

**Key equations.**
$$M_{\text{Ch}}\approx1.44\left(\frac{2}{\mu_e}\right)^2M_\odot,\qquad B\approx3.2\times10^{19}\sqrt{P\dot P}\ \text{G},\qquad \tau_c=\frac{P}{2\dot P}$$

**See also.** [Neutron-star equation of state](knowledge/07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state/README.md) · [Black holes](knowledge/05-relativity-and-gravitation/black-holes/README.md) · [Quantum statistics](knowledge/03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics/README.md)

### Stellar structure and evolution · `knowledge/09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution`

**Scope.** Hydrostatic and thermal equilibrium, virial theorem and Kelvin–Helmholtz time, equation of state (ideal gas, radiation, degeneracy), opacity and radiative diffusion, convection (Schwarzschild criterion, mixing-length theory), pp chain and CNO cycle, mass–luminosity relation, main-sequence lifetimes, red giants, helium flash, horizontal branch, AGB, planetary nebulae, massive-star mass loss, MESA stellar-evolution code.

**Core ideas.**
- Stars are thermostats: if fusion runs fast, the core expands and cools, slowing fusion.
- Photons random-walk out of the Sun over ~$10^5$ years.
- Main-sequence lifetime scales as $t\sim10^{10}\,\text{yr}\,(M/M_\odot)^{-2.5}$.

**Key equations.**
$$t_{KH}=\frac{GM^2}{RL}\approx3\times10^7\ \text{yr}\ (\text{Sun}),\qquad \left|\frac{d\ln T}{d\ln P}\right|_{\text{rad}}>\frac{\gamma-1}{\gamma}\Rightarrow\text{convection}$$

**Landmark.** Salpeter (1955) — see [subfield landmarks](knowledge/09-astrophysics-and-cosmology/stellar-astrophysics/README.md).

**See also.** [Fusion reactions](knowledge/07-nuclear-physics/nuclear-reactions-and-decays/fusion-reactions/README.md) · [Stellar nucleosynthesis](knowledge/07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process/README.md)

### The Sun and helioseismology · `knowledge/09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology`

**Scope.** Standard solar model, p-modes and the 5-minute oscillations, helioseismic inversions of sound speed and rotation, tachocline, solar neutrino fluxes (pp, ⁷Be, ⁸B, CNO), solar abundance (metallicity) problem, solar dynamo and the 11-year cycle, asteroseismology of other stars (Kepler, TESS).

**Core ideas.**
- Millions of acoustic modes probe the interior like seismology probes Earth.
- Helioseismology confirmed solar models so well that the solar neutrino deficit had to be particle physics.
- Revised (lower) photospheric abundances disagree with helioseismic sound speeds — an open opacity/abundance problem.

**Key equations.**
$$\nu_{n\ell}\approx\Delta\nu\left(n+\frac\ell2+\epsilon\right),\qquad \Delta\nu\propto\sqrt{\bar\rho}$$

**See also.** [Neutrino experiments (solar neutrinos)](knowledge/06-particle-physics/neutrino-physics/neutrino-experiments-and-sources/README.md) · [Dynamo theory](knowledge/10-plasma-physics/magnetohydrodynamics/dynamo-theory/README.md)


---

# Packet 09-5 (33 records)

{"id": "C2795", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "b": "10-plasma-physics/space-and-astrophysical-plasmas/solar-wind-and-heliosphere", "name": "Parker wind and coronal heating", "kind": "shared object", "summary": "The corona, with its heating problem, is the base of the Parker wind. Alfvén-wave turbulence and reconnection are candidate heaters, and the transonic wind solution follows from hydrodynamic equations.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2796", "a": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Blackbody radiation and radiative equilibrium", "kind": "analogy", "summary": "Both rest on Planck blackbody radiation and radiative transfer: the CMB is a relic thermal spectrum, Earth's climate set by balance of absorbed sunlight and outgoing thermal radiation.", "map": "B_\\nu(T)=\\frac{2h\\nu^3}{c^2}\\frac{1}{e^{h\\nu/kT}-1}", "breaks": "The CMB is a decoupled relic freely streaming; Earth's emission is non-equilibrium and gray-body with strong absorption bands.", "confidence": "established", "strength": 2}
{"id": "C2797", "a": "09-astrophysics-and-cosmology/cosmology/gravitational-lensing", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Inverse problems and tomographic reconstruction", "kind": "method transfer", "summary": "Weak-lensing mass maps and CT/MRI reconstruction are regularized linear inverse problems, using Kaiser–Squires-type inversion, Wiener filtering and sparsity priors.", "map": "y=Ax+n", "breaks": "Lensing has sparse noisy sampling and shape noise; CT has controlled acquisition geometry.", "confidence": "established", "strength": 1}
{"id": "C2798", "a": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Quantum sensors for dark matter", "kind": "method transfer", "summary": "Axion and light dark-matter searches use SQUIDs, atomic magnetometers, NV centres, atomic clocks and interferometers; quantum-sensing techniques set sensitivity, including squeezing.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2799", "a": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "Low-background detectors and scintillation", "kind": "method transfer", "summary": "Scintillators, liquid xenon and time-of-flight photodetection developed for particle and dark-matter detection also drive PET detector design; low-noise photosensors cross over.", "map": "", "breaks": "Dark-matter detectors require extreme radiopurity and keV thresholds; PET needs high rate at 511 keV.", "confidence": "established", "strength": 1}
{"id": "C2800", "a": "09-astrophysics-and-cosmology/galaxies/active-galactic-nuclei-and-supermassive-black-holes", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Jets and undulator radiation", "kind": "analogy", "summary": "Relativistic jets emit synchrotron and inverse-Compton radiation, with Doppler boosting; undulators and FELs give coherent, narrow-band versions of the same radiation by accelerated charges.", "map": "", "breaks": "Jet emission is incoherent and broadband; FELs achieve coherence via microbunching.", "confidence": "established", "strength": 2}
{"id": "C2801", "a": "09-astrophysics-and-cosmology/galaxies/galaxy-clusters", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics", "name": "Turbulence in stratified fluids", "kind": "analogy", "summary": "Intracluster gas and the oceans are stratified turbulent fluids, with buoyancy-driven mixing and internal gravity waves described by Brunt–Väisälä frequency.", "map": "N^2=\\frac{g}{\\rho}\\frac{d\\rho}{dz}", "breaks": "Cluster gas is magnetized, weakly collisional plasma with cooling and AGN feedback.", "confidence": "current research", "strength": 1}
{"id": "C2802", "a": "09-astrophysics-and-cosmology/galaxies/the-milky-way", "b": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "name": "Statistical inference of dynamical systems", "kind": "method transfer", "summary": "Galactic archaeology and biophysical data analysis both use Bayesian inference and machine learning on large noisy catalogues; Gaia phase-space modelling parallels inference in living-systems data.", "map": "", "breaks": "The shared element is generic statistical practice.", "confidence": "proposed", "strength": 1}
{"id": "C2803", "a": "09-astrophysics-and-cosmology/galaxies/the-milky-way", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Rossby waves and density waves", "kind": "analogy", "summary": "Both feature large-scale rotating-fluid wave patterns: Rossby waves from the beta effect in atmospheres, and spiral density waves in rotating galactic disks with differential rotation, with analogous dispersion structure.", "map": "", "breaks": "Galactic disks are self-gravitating and collisionless stars; Rossby waves are restoring-force vorticity waves in a fluid.", "confidence": "current research", "strength": 1}
{"id": "C2804", "a": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "b": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "name": "Cosmic accelerators versus machines", "kind": "analogy", "summary": "Diffusive shock acceleration and Fermi mechanisms are natural counterparts of laboratory accelerators; the Hillas criterion parallels the size-times-field limit on achievable energy.", "map": "E_{max}\\sim Z e B R\\beta", "breaks": "Cosmic acceleration is stochastic, shock-based and power-law; machines use coherent, controlled RF fields.", "confidence": "established", "strength": 2}
{"id": "C2805", "a": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Synchrotron radiation in nature and the lab", "kind": "identity", "summary": "Relativistic electrons in magnetic fields emit synchrotron radiation, identical physics in AGN jets, pulsar nebulae and storage-ring light sources, with the same critical-frequency scaling.", "map": "\\omega_c=\\tfrac{3}{2}\\gamma^3\\,\\frac{c}{\\rho}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2806", "a": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Cosmic rays and air showers in the atmosphere", "kind": "shared object", "summary": "Cosmic rays are detected through extensive air showers developing in the atmosphere; cosmic-ray ionisation is also proposed to affect atmospheric electricity and cloud nucleation.", "map": "", "breaks": "Cosmic-ray cloud seeding is weak and disputed.", "confidence": "current research", "strength": 1}
{"id": "C2807", "a": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "b": "11-interdisciplinary-physics/medical-physics/radiation-therapy", "name": "Cosmic-ray and hadron-therapy interactions", "kind": "shared object", "summary": "Heavy-ion transport, nuclear fragmentation and Bragg-peak energy loss are shared: galactic cosmic-ray shielding for astronauts uses the same codes and radiobiology as carbon-ion therapy.", "map": "-\\frac{dE}{dx}\\propto \\frac{Z^2}{\\beta^2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2808", "a": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/fast-radio-bursts-and-magnetars", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Coherent emission from bunched charges", "kind": "analogy", "summary": "FRB models invoke coherent curvature or maser emission from bunched charges, resembling coherent synchrotron radiation and FEL microbunching where power scales as N².", "map": "P_{coh}\\propto N^2 P_1", "breaks": "FRB coherence mechanism is unsettled; FELs rely on a known collective instability.", "confidence": "proposed", "strength": 2}
{"id": "C2809", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Planet spectra as molecular spectroscopy", "kind": "method transfer", "summary": "Identifying planetary atmospheric species relies on laboratory rovibrational line lists and selection rules; the same spectroscopy underlies remote sensing of planets and exoplanets.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2810", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Planetary climate as Earth climate physics", "kind": "shared object", "summary": "Energy balance, greenhouse effect and feedbacks developed for Earth apply to other planets and exoplanets, setting equilibrium temperatures and habitability.", "map": "T_{eq}=T_\\star\\sqrt{R_\\star/2a}\\,(1-A)^{1/4}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2811", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/astrobiology-and-habitability", "b": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "name": "Physical limits of life and biosignatures", "kind": "shared object", "summary": "Habitability asks which physical constraints (energy, chemistry, thermodynamics) permit life; physics of living systems quantifies those limits, such as energy use, noise and information processing.", "map": "", "breaks": "", "confidence": "current research", "strength": 1}
{"id": "C2812", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/astrobiology-and-habitability", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Habitable zone from climate feedbacks", "kind": "mechanism", "summary": "Habitable-zone edges are set by radiative-convective climate physics: runaway greenhouse from water-vapour feedback and ice-albedo snowball transitions, as in Earth climate models.", "map": "S_{eff}\\propto F_{OLR}/(1-A)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2813", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-atmospheres", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Spectroscopic databases serve exoplanet retrievals", "kind": "method transfer", "summary": "Line lists such as HITRAN and ExoMol, from quantum-chemistry and spectroscopy, are essential inputs for interpreting JWST exoplanet spectra.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2814", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-atmospheres", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Transmission spectra as molecular absorption", "kind": "method transfer", "summary": "Exoplanet transmission and emission spectra are decoded using molecular line lists, cross sections and Raman/collision-induced absorption knowledge from molecular spectroscopy.", "map": "\\delta(\\lambda)\\approx (R_p+n H(\\lambda))^2/R_\\star^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2815", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-atmospheres", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Greenhouse and inversion physics on other worlds", "kind": "shared object", "summary": "Greenhouse trapping, lapse rates and temperature inversions explain exoplanet thermal structure just as they do Earth's atmosphere.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2816", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-atmospheres", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Radiative transfer codes from Earth to exoplanets", "kind": "method transfer", "summary": "Radiative-convective models, correlated-k opacities and general circulation models built for Earth climate are reused for exoplanet atmospheres and retrievals.", "map": "", "breaks": "Earth-tuned assumptions (water condensation, near-1 bar) fail for hot Jupiters and non-solar compositions.", "confidence": "established", "strength": 2}
{"id": "C2817", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Astrochemistry in disks", "kind": "shared object", "summary": "Disk chemistry and the delivery of volatiles depend on gas-phase and grain-surface reaction rates, ion-molecule kinetics and snow lines, drawing on reaction-dynamics rate theory.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2818", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks", "b": "11-interdisciplinary-physics/chemical-physics/surface-science-and-catalysis", "name": "Grain-surface chemistry and catalysis", "kind": "mechanism", "summary": "H2 formation and ice mantle chemistry on dust grains proceed via adsorption, diffusion and Langmuir–Hinshelwood reactions, the same surface-science mechanisms as in heterogeneous catalysis.", "map": "", "breaks": "Interstellar grains are at ~10 K with quantum tunnelling, in ultra-low-density gas.", "confidence": "established", "strength": 2}
{"id": "C2819", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Rotating stratified turbulence in disks and atmospheres", "kind": "analogy", "summary": "Protoplanetary-disk vortices, zonal flows and Rossby wave instability parallel geophysical vortices and jets in rotating shear flows; Coriolis dynamics governs both.", "map": "", "breaks": "Disks involve magnetorotational turbulence, dust coupling and self-gravity.", "confidence": "current research", "strength": 2}
{"id": "C2820", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Milankovitch cycles and orbital forcing", "kind": "mechanism", "summary": "Secular orbital perturbations change Earth's eccentricity, obliquity and precession, modulating insolation and driving glacial cycles.", "map": "", "breaks": "Climate response is nonlinear, with ice-sheet feedbacks.", "confidence": "established", "strength": 3}
{"id": "C2821", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Neutron-star asteroseismology and crust elasticity", "kind": "analogy", "summary": "Neutron-star crusts support shear modes and quakes analogous to earthquakes; magnetar giant-flare quasi-periodic oscillations are interpreted as crustal torsional modes, as in seismology.", "map": "", "breaks": "Crust is a Coulomb lattice at nuclear densities with extreme magnetic fields and superfluid coupling.", "confidence": "current research", "strength": 2}
{"id": "C2822", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "Positron annihilation and gamma detection", "kind": "shared object", "summary": "Positron annihilation producing 511 keV photons is used in PET and is observed in the Galactic 511 keV line; gamma-ray instrumentation overlaps with nuclear-medicine detectors, such as Compton cameras.", "map": "e^+e^-\\to\\gamma\\gamma", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2823", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "b": "11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods", "name": "Opacities and equations of state", "kind": "method transfer", "summary": "Stellar and planetary interiors require atomic opacities and equations of state computed with electronic-structure methods, including density functional and molecular dynamics for warm dense matter.", "map": "", "breaks": "Stellar plasmas are partially ionized at high temperature, beyond standard ground-state quantum chemistry.", "confidence": "established", "strength": 2}
{"id": "C2824", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Convection and radiative-convective structure", "kind": "mechanism", "summary": "Stellar envelopes and planetary atmospheres share Schwarzschild/lapse-rate stability criteria and mixing-length convection; the adiabatic gradient decides radiative versus convective layers.", "map": "\\nabla_{rad}>\\nabla_{ad}", "breaks": "Stars have radiation pressure, ionization and nuclear sources; atmospheres have moisture and rotation constraints.", "confidence": "established", "strength": 2}
{"id": "C2825", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Solar forcing of climate", "kind": "shared object", "summary": "Solar luminosity, its variability and the faint young Sun set the incoming flux in Earth's energy balance; solar cycle irradiance variations give a small forcing term.", "map": "S_0=L_\\odot/4\\pi d^2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2826", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Dynamo theory: Sun and geodynamo", "kind": "mechanism", "summary": "Solar and geodynamo both arise from MHD induction in convecting conducting fluid, with rotation and helicity (alpha-omega effect) driving field generation and reversals.", "map": "\\partial_t\\mathbf{B}=\\nabla\\times(\\mathbf{u}\\times\\mathbf{B})+\\eta\\nabla^2\\mathbf{B}", "breaks": "Solar dynamo is turbulent with strong stratification and a 11-yr cycle; geodynamo has low Rossby number and the solid inner core.", "confidence": "established", "strength": 3}
{"id": "C2827", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Helioseismology and seismology inversions", "kind": "method transfer", "summary": "Both infer interior structure from observed wave modes and travel times via inversion: p-modes for the Sun, body and surface waves and normal modes for Earth. Methods and the mathematics of tomography parallel each other.", "map": "\\omega_{nl}\\ \\to\\ c(r),\\rho(r)", "breaks": "Solar modes are stochastically excited acoustic waves in a fluid; Earth has shear waves, discontinuities and sparse source locations.", "confidence": "established", "strength": 3}