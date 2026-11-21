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

### Dark energy · `knowledge/09-astrophysics-and-cosmology/cosmology/dark-energy`

**Scope.** 1998 supernova discovery of acceleration, equation-of-state parameter $w$ and the $w_0$–$w_a$ parametrization, vacuum energy and the cosmological-constant problem, quintessence and phantom fields, modified gravity alternatives, BAO, weak lensing and cluster probes, DESI 2024–25 results favouring evolving $w$ at ~3–4σ in combination with supernovae, Euclid, Rubin and Roman.

**Core ideas.**
- Acceleration requires $w<-1/3$; a cosmological constant has $w=-1$ exactly.
- Naive QFT vacuum energy overshoots the observed value by ~$10^{120}$ — the worst prediction in physics.
- Current data are consistent with Λ at the 2σ level for some combinations but hint at $w_0>-1$, $w_a<0$ for others.

**Key equations.**
$$w(a)=w_0+w_a(1-a),\qquad \rho_\Lambda\approx(2.24\ \text{meV})^4,\qquad q_0=\tfrac12\Omega_m-\Omega_\Lambda\approx-0.53$$

**See also.** [Modified gravity](knowledge/05-relativity-and-gravitation/general-relativity/modified-gravity/README.md) · [Supernovae](knowledge/09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients/README.md)

### FLRW cosmology and expansion history · `knowledge/09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history`

**Scope.** Cosmological principle, FLRW metric and curvature, scale factor and redshift, Friedmann and acceleration equations, equations of state ($w=0,\tfrac13,-1$), radiation–matter equality, comoving, luminosity and angular-diameter distances, age of the universe, horizons, the six ΛCDM parameters and their degeneracies.

**Core ideas.**
- Densities dilute as $a^{-3(1+w)}$: radiation dominates early, matter later, Λ today.
- Distances depend on the integrated expansion history — measuring $d_L(z)$ constrains the components.
- Redshift is expansion of wavelengths, not a Doppler shift in the usual sense.

**Key equations.**
$$ds^2=-c^2dt^2+a^2(t)\left[\frac{dr^2}{1-kr^2}+r^2d\Omega^2\right],\qquad d_L=(1+z)\,c\int_0^z\frac{dz'}{H(z')}$$

**See also.** [Exact solutions (FLRW, de Sitter)](knowledge/05-relativity-and-gravitation/general-relativity/exact-solutions/README.md) · [Statistical inference](knowledge/00-foundations/measurement-and-data-analysis/statistical-inference-in-physics/README.md)

### Hubble tension and cosmological tensions · `knowledge/09-astrophysics-and-cosmology/cosmology/hubble-tension-and-cosmological-tensions`

**Scope.** Distance ladder (parallax → Cepheids → SN Ia; SH0ES $H_0\approx73$), TRGB and JAGB alternatives (CCHP ~70), CMB+ΛCDM inference ($H_0\approx67.4$), BAO+BBN, strong-lensing time delays, gravitational-wave standard sirens, JWST Cepheid checks, early dark energy and other proposed solutions, the $S_8$ weak-lensing tension.

**Core ideas.**
- Local measurements directly measure $H_0$; CMB values are inferred assuming ΛCDM.
- Solutions that change pre-recombination physics shrink the sound horizon — but tend to worsen other fits.
- Independent methods (TRGB, sirens, lensing) are the key arbiters.

**Key equations.**
$$H_0^{\text{SH0ES}}=73.0\pm1.0,\qquad H_0^{\text{Planck}}=67.4\pm0.5\ \text{km s}^{-1}\text{Mpc}^{-1},\qquad S_8=\sigma_8\sqrt{\Omega_m/0.3}$$

**See also.** [Gravitational waves](knowledge/05-relativity-and-gravitation/gravitational-waves/README.md) · [Uncertainty and error propagation](knowledge/00-foundations/measurement-and-data-analysis/uncertainty-and-error-propagation/README.md)

### Inflation · `knowledge/09-astrophysics-and-cosmology/cosmology/inflation`

**Scope.** Horizon, flatness and monopole problems, slow-roll inflation and its parameters, quantum origin of curvature perturbations, scalar spectral index $n_s$ and its running, tensor-to-scalar ratio $r$, Starobinsky/Higgs inflation, reheating, non-Gaussianity ($f_{NL}$), eternal inflation and the multiverse debate, alternatives (bouncing cosmologies).

**Core ideas.**
- ~60 e-folds of near-exponential expansion stretch a causally connected patch beyond today's horizon.
- Quantum fluctuations of the inflaton, frozen outside the horizon, seed nearly scale-invariant adiabatic Gaussian perturbations.
- Observed $n_s\approx0.965$ (slightly red) fits simple models; $r<0.036$ disfavours large-field monomial potentials.

**Key equations.**
$$\epsilon=\frac{M_P^2}{2}\left(\frac{V'}{V}\right)^2,\quad \eta=M_P^2\frac{V''}{V},\qquad n_s-1\approx2\eta-6\epsilon,\quad r\approx16\epsilon$$

**See also.** [QFT in curved spacetime](knowledge/05-relativity-and-gravitation/quantum-gravity/qft-in-curved-spacetime/README.md) · [Loop quantum cosmology](knowledge/05-relativity-and-gravitation/quantum-gravity/loop-quantum-gravity/README.md)

### Large-scale structure and BAO · `knowledge/09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao`

**Scope.** Linear growth $\delta\propto D(a)$, transfer function and matter power spectrum, $\sigma_8$, non-linear collapse and halo models, N-body simulations, galaxy bias, BAO standard ruler (~150 Mpc), redshift-space distortions and $f\sigma_8$, 2dF, SDSS/BOSS/eBOSS, DESI, Euclid, intensity mapping.

**Core ideas.**
- Sound waves in the early plasma imprint a preferred separation between galaxies — a standard ruler calibrated by the CMB.
- Peculiar velocities distort clustering along the line of sight, measuring the growth rate of structure.
- Combining geometry (BAO) and growth (RSD, lensing) separates dark energy from modified gravity.

**Key equations.**
$$\ddot\delta+2H\dot\delta-4\pi G\bar\rho\delta=0,\qquad r_d=\int_{z_d}^\infty\frac{c_s(z)}{H(z)}dz\approx147\ \text{Mpc}$$

**See also.** [Galaxy formation](knowledge/09-astrophysics-and-cosmology/galaxies/galaxy-formation-and-evolution/README.md) · [Gravitational lensing](knowledge/09-astrophysics-and-cosmology/cosmology/gravitational-lensing/README.md)

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

### Astrophysical evidence for dark matter · `knowledge/09-astrophysics-and-cosmology/dark-matter/astrophysical-evidence-for-dark-matter`

**Scope.** Zwicky's Coma cluster, flat rotation curves (Rubin, Bosma), X-ray cluster masses, strong and weak lensing masses, the Bullet Cluster offset between gas and mass, CMB third acoustic peak, BBN baryon density vs. total matter, growth of structure from $10^{-5}$ to today, dwarf spheroidal galaxies as DM-dominated systems.

**Core ideas.**
- Flat rotation curves imply $M(<r)\propto r$ far beyond the visible disk.
- The Bullet Cluster shows mass (lensing) separated from most baryons (X-ray gas) — hard to mimic with modified gravity.
- The CMB requires non-baryonic matter: baryons alone can't grow structure fast enough after recombination.

**Key equations.**
$$v_c^2=\frac{GM(<r)}{r}=\text{const}\Rightarrow\rho\propto r^{-2},\qquad \frac{\Omega_c}{\Omega_b}\approx5.4$$

**See also.** [Galaxy clusters](knowledge/09-astrophysics-and-cosmology/galaxies/galaxy-clusters/README.md) · [CMB](knowledge/09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background/README.md)

### Dark-matter small-scale structure · `knowledge/09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure`

**Scope.** NFW cusps vs. observed cores, missing satellites and the discovery of ultra-faint dwarfs, too-big-to-fail, diversity of rotation curves, baryonic feedback solutions, self-interacting DM ($\sigma/m\sim1$ cm²/g), warm DM and Lyman-α forest bounds, fuzzy DM ($m\sim10^{-22}$ eV) and solitonic cores, stellar streams and strong-lens substructure as probes, primordial black holes.

**Core ideas.**
- CDM predicts cuspy, abundant subhalos; observations show fewer, cored small galaxies — but feedback can redistribute DM.
- The free-streaming length or de Broglie wavelength of alternative DM suppresses small-scale power.
- Subhalo detection via lensing and stream gaps tests the CDM mass function directly.

**Key equations.**
$$\lambda_{\text{dB}}=\frac{h}{mv}\approx1.2\ \text{kpc}\left(\frac{10^{-22}\,\text{eV}}{m}\right)\left(\frac{100\ \text{km/s}}{v}\right)$$

**See also.** [Galaxy formation](knowledge/09-astrophysics-and-cosmology/galaxies/galaxy-formation-and-evolution/README.md) · [Gravitational lensing](knowledge/09-astrophysics-and-cosmology/cosmology/gravitational-lensing/README.md)

### Direct detection · `knowledge/09-astrophysics-and-cosmology/dark-matter/direct-detection`

**Scope.** Standard halo model and recoil spectra, spin-independent and spin-dependent cross sections, liquid xenon (LZ, XENONnT, PandaX) and argon (DarkSide) TPCs, cryogenic detectors (SuperCDMS, CRESST), electron-recoil searches for sub-GeV DM, annual modulation and the DAMA/LIBRA controversy (refuted by COSINE, ANAIS), coherent neutrino background ("neutrino fog"), haloscopes for axions.

**Core ideas.**
- WIMP–nucleus elastic scattering deposits keV-scale recoil energies — needs ultra-low background deep underground.
- Rates scale with $A^2$ for coherent spin-independent scattering, favouring heavy targets like xenon.
- Solar and atmospheric neutrinos produce an irreducible background below which discovery becomes statistically hard.

**Key equations.**
$$\frac{dR}{dE_R}=\frac{\rho_\chi}{m_\chi m_N}\int_{v_{\min}}^{\infty}vf(v)\frac{d\sigma}{dE_R}d^3v,\qquad v_{\min}=\sqrt{\frac{m_NE_R}{2\mu^2}}$$

**See also.** [Axions](knowledge/06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector/README.md) · [Radiation detection](knowledge/07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry/README.md)

### Indirect detection · `knowledge/09-astrophysics-and-cosmology/dark-matter/indirect-detection`

**Scope.** J-factors and halo profiles, Fermi-LAT dwarf spheroidal limits reaching the thermal cross section for $m_\chi\lesssim100$ GeV, Galactic Centre GeV excess (DM vs. millisecond pulsars), AMS-02 positron and antiproton spectra, 3.5 keV X-ray line debate, IceCube neutrinos from the Sun, CTA prospects, CMB energy-injection bounds.

**Core ideas.**
- Flux $\propto\langle\sigma v\rangle\rho^2$ integrated along the line of sight — dense, nearby, DM-dominated targets are best.
- Astrophysical backgrounds (pulsars, cosmic-ray interactions) can mimic signals; morphology and spectra discriminate.
- Dwarf galaxies are clean (few baryons) and give the most robust limits.

**Key equations.**
$$\frac{d\Phi}{dE}=\frac{\langle\sigma v\rangle}{8\pi m_\chi^2}\frac{dN}{dE}\,J,\qquad J=\int_{\Delta\Omega}\int_{\text{l.o.s.}}\rho^2\,dl\,d\Omega$$

**Landmark.** Hooper & Goodenough (2011) — see [subfield landmarks](knowledge/09-astrophysics-and-cosmology/dark-matter/README.md).

**See also.** [Cosmic rays](knowledge/09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays/README.md) · [Dark-matter candidates](knowledge/06-particle-physics/beyond-the-standard-model/dark-matter-particle-candidates/README.md)

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

### Galaxy formation and evolution · `knowledge/09-astrophysics-and-cosmology/galaxies/galaxy-formation-and-evolution`

**Scope.** Halo mass function and merger trees, gas cooling and the two-stage theory, star-formation laws (Kennicutt–Schmidt), stellar and AGN feedback, quenching and the red sequence, Hubble/morphological sequence, Tully–Fisher and Faber–Jackson relations, galaxy mergers, semi-analytic models, hydrodynamical simulations (Illustris, EAGLE, FIRE), cosmic star-formation history.

**Core ideas.**
- Baryons cool inside dark halos; feedback regulates star formation so that only a few percent of baryons become stars.
- The stellar-to-halo mass ratio peaks at Milky-Way-like halos (~$10^{12}\,M_\odot$).
- Simulations must model "subgrid" physics (star formation, feedback) — results depend on calibration.

**Key equations.**
$$\Sigma_{\text{SFR}}\propto\Sigma_{\text{gas}}^{1.4},\qquad L\propto v_{\max}^4\ (\text{Tully–Fisher})$$

**See also.** [Dark-matter small-scale structure](knowledge/09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure/README.md) · [Pulsar timing arrays (SMBH binaries)](knowledge/05-relativity-and-gravitation/gravitational-waves/pulsar-timing-arrays/README.md)

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

### Gamma-ray bursts · `knowledge/09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/gamma-ray-bursts`

**Scope.** Discovery by Vela satellites, BATSE isotropy and cosmological origin, long (collapsar) vs. short (merger) classes, GRB–supernova connection, fireball and internal/external shock models, afterglows and jet breaks, Lorentz factors $\Gamma\sim100$–1000, GRB 170817A, GRB 221009A ("BOAT"), TeV afterglow detections, Lorentz-invariance tests.

**Core ideas.**
- Isotropic-equivalent energies up to $10^{47}$ J imply narrow, ultra-relativistic jets.
- The compactness problem forces bulk Lorentz factors in the hundreds.
- Short GRBs accompany neutron-star mergers, as GW170817 confirmed.

**Key equations.**
$$t_{\text{obs}}\approx\frac{R}{2\Gamma^2c},\qquad \theta_j\approx\frac{1}{\Gamma(t_{\text{jet}})}$$

**See also.** [Tests of Lorentz invariance](knowledge/05-relativity-and-gravitation/special-relativity/tests-of-lorentz-invariance/README.md) · [Multi-messenger astronomy](knowledge/09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/multi-messenger-astronomy/README.md)

### Multi-messenger astronomy · `knowledge/09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/multi-messenger-astronomy`

**Scope.** GW170817 + GRB 170817A + kilonova AT2017gfo, localization and follow-up campaigns, r-process heavy elements, speed of gravity, standard-siren $H_0$, neutron-star EOS from tidal deformability, neutrino–gamma coincidences, SNEWS for Galactic supernovae, alert infrastructures (GCN, AMON), Rubin and next-generation follow-up.

**Core ideas.**
- Independent messengers break degeneracies: GWs give distance and masses; light gives redshift and environment.
- A 1.7 s delay between GW and gamma rays over 40 Mpc constrains $|c_{\text{gw}}-c|/c<10^{-15}$.
- Coordinated, fast follow-up is as important as detector sensitivity.

**Key equations.**
$$\frac{|\Delta v|}{c}\lesssim\frac{c\,\Delta t}{D}=\frac{1.7\ \text{s}\times c}{40\ \text{Mpc}}\approx4\times10^{-16}$$

**Landmark.** LIGO, Virgo et al. (2017) — see [subfield landmarks](knowledge/09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/README.md).

**See also.** [Ground-based GW detections](knowledge/05-relativity-and-gravitation/gravitational-waves/ground-based-detections/README.md) · [r-process](knowledge/07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process/README.md)

### Neutrino astronomy · `knowledge/09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/neutrino-astronomy`

**Scope.** Cubic-kilometre Cherenkov telescopes (IceCube, KM3NeT, Baikal-GVD), tracks vs. cascades, diffuse astrophysical flux (2013), TXS 0506+056 blazar (2017), NGC 1068 Seyfert (2022), Galactic-plane neutrinos (2023), KM3-230213A at ~220 PeV (2025), flavour ratios, SN 1987A's 25 neutrinos, radio detection of EeV neutrinos.

**Core ideas.**
- Neutrinos escape dense sources and travel undeflected — pointing straight back to hadronic accelerators.
- Pion decay links neutrinos to gamma rays: $\pi^\pm\to\mu\nu\to e\nu\nu\nu$, $\pi^0\to\gamma\gamma$.
- Event rates are small; statistical source identification requires years of data.

**Key equations.**
$$p+\gamma\to\Delta^+\to n+\pi^+,\qquad E_\nu\approx\frac{E_p}{20}$$

**See also.** [Neutrino experiments](knowledge/06-particle-physics/neutrino-physics/neutrino-experiments-and-sources/README.md) · [Cherenkov radiation](knowledge/02-electromagnetism-and-optics/radiation-and-scattering/cherenkov-and-transition-radiation/README.md)

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

### Exoplanet detection · `knowledge/09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-detection`

**Scope.** Doppler spectroscopy (HARPS, ESPRESSO, ~10 cm/s goal), transit surveys (Kepler, TESS, PLATO), transit-timing variations, gravitational microlensing (OGLE, Roman), direct imaging and coronagraphy, Gaia astrometry, pulsar timing, stellar activity as noise, occurrence rates and the radius valley.

**Core ideas.**
- Each method has biases: RV and transits favour close-in planets; microlensing and imaging favour wide orbits.
- Transit depth gives radius; RV gives mass — together they give density and composition.
- An Earth twin induces only ~9 cm/s RV on the Sun — below stellar jitter.

**Key equations.**
$$K_\oplus\approx0.09\ \text{m/s},\qquad K_{\text{Jup}}\approx12.5\ \text{m/s},\qquad P_{\text{transit}}\approx\frac{R_\star}{a}$$

**See also.** [Gravitational lensing](knowledge/09-astrophysics-and-cosmology/cosmology/gravitational-lensing/README.md) · [Statistical inference](knowledge/00-foundations/measurement-and-data-analysis/statistical-inference-in-physics/README.md)

### Planet formation and protoplanetary disks · `knowledge/09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks`

**Scope.** Disk structure and accretion (α-viscosity, MRI, winds), dust settling and radial drift, the metre-size barrier, streaming instability and planetesimals, pebble accretion, core accretion for giants vs. disk instability, snow lines, Type I/II migration, ALMA rings and gaps (HL Tau), disk lifetimes (~3–10 Myr), debris disks.

**Core ideas.**
- Dust must grow from μm to km sizes before drag drifts it into the star.
- Giant planets must form within the gas-disk lifetime; core accretion needs ~10 $M_\oplus$ cores.
- Disk substructures (rings, gaps, spirals) may be carved by young planets.

**Key equations.**
$$\nu=\alpha c_sH,\qquad \text{St}=\Omega_K t_s,\qquad M_{\text{iso}}\approx\frac{(2\pi\cdot2\sqrt3\,\Sigma_pa^2)^{3/2}}{(3M_\star)^{1/2}}$$

**See also.** [Low-Reynolds-number flow](knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics/README.md) · [MHD (MRI)](knowledge/10-plasma-physics/magnetohydrodynamics/README.md)

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

### Binary stars and stellar populations · `knowledge/09-astrophysics-and-cosmology/stellar-astrophysics/binary-stars-and-stellar-populations`

**Scope.** Visual, spectroscopic and eclipsing binaries as mass scales, Roche lobes and mass transfer, common-envelope evolution, X-ray binaries, formation channels of gravitational-wave sources, the initial mass function (Salpeter, Kroupa, Chabrier), open and globular clusters, isochrone ages, population synthesis (Bruzual–Charlot), Population I/II/III, Gaia astrometry.

**Core ideas.**
- Most massive stars are in binaries that interact — binary evolution changes stellar fates.
- The IMF is approximately universal: $dN/dM\propto M^{-2.35}$ above ~1 $M_\odot$.
- Cluster colour–magnitude diagrams give ages via main-sequence turnoffs.

**Key equations.**
$$\frac{r_L}{a}\approx\frac{0.49q^{2/3}}{0.6q^{2/3}+\ln(1+q^{1/3})}\ (\text{Eggleton}),\qquad \xi(M)\propto M^{-2.35}$$

**Landmark.** Salpeter (1955) — see [subfield landmarks](knowledge/09-astrophysics-and-cosmology/stellar-astrophysics/README.md).

**See also.** [Ground-based GW detections](knowledge/05-relativity-and-gravitation/gravitational-waves/ground-based-detections/README.md) · [The Milky Way](knowledge/09-astrophysics-and-cosmology/galaxies/the-milky-way/README.md)

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

### Supernovae and transients · `knowledge/09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients`

**Scope.** Spectroscopic classification (Ia, Ib/c, II), core collapse and neutrino-driven explosions, SN 1987A neutrinos, Type Ia thermonuclear explosions of white dwarfs and the Phillips relation, radioactive ⁵⁶Ni → ⁵⁶Co → ⁵⁶Fe powering light curves, superluminous supernovae, tidal disruption events, kilonovae, supernova remnants and cosmic-ray acceleration, time-domain surveys (ZTF, Rubin LSST).

**Core ideas.**
- Core collapse releases ~$3\times10^{46}$ J, 99% in neutrinos; only ~1% goes into the explosion.
- Type Ia supernovae are standardizable candles: brighter ones decline more slowly.
- Light curves are powered by radioactive decay — late-time slopes match the ⁵⁶Co half-life (77 d).

**Key equations.**
$$E_{\text{grav}}\approx\frac{3}{5}\frac{GM_{\text{NS}}^2}{R_{\text{NS}}}\approx3\times10^{46}\ \text{J},\qquad L(t)\propto e^{-t/\tau_{\text{Co}}}$$

**See also.** [Dark energy (SN Ia cosmology)](knowledge/09-astrophysics-and-cosmology/cosmology/dark-energy/README.md) · [r-process](knowledge/07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process/README.md)

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

# Packet 09-3 (100 records)

{"id": "C2077", "a": "05-relativity-and-gravitation/gravitational-waves/pulsar-timing-arrays", "b": "09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure", "name": "Pulsar timing probes ultralight dark matter", "kind": "mechanism", "summary": "Ultralight scalar ('fuzzy') dark matter has an oscillating pressure that makes the metric potentials oscillate at f=2mc²/h, in the nHz band for m~10⁻²³ eV, leaving coherent PTA residuals. PTAs also bound dark-matter substructure through the Doppler and Shapiro shifts of passing clumps.", "map": "f=\\frac{2mc^2}{h}\\approx4.8\\,{\\rm nHz}\\left(\\frac{m}{10^{-23}\\,{\\rm eV}}\\right)", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2078", "a": "05-relativity-and-gravitation/gravitational-waves/pulsar-timing-arrays", "b": "09-astrophysics-and-cosmology/galaxies/galaxy-formation-and-evolution", "name": "nHz background from supermassive-black-hole binaries", "kind": "mechanism", "summary": "Hierarchical galaxy mergers pair up central black holes into binaries, whose combined inspiral predicts a nanohertz background with h_c∝f^{-2/3}. The amplitude PTAs reported in 2023 constrains SMBH mass functions, merger rates and how binaries get past the final-parsec problem.", "map": "h_c(f)=A\\left(\\frac{f}{1\\,{\\rm yr}^{-1}}\\right)^{-2/3},\\quad A\\sim2\\text{–}3\\times10^{-15}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2079", "a": "05-relativity-and-gravitation/gravitational-waves/pulsar-timing-arrays", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-detection", "name": "Pulsar timing found the first exoplanets", "kind": "method transfer", "summary": "The timing model PTAs use fits pulse arrival times for Rømer delays, spin-down and noise. Applied to PSR B1257+12, it left periodic residuals that Wolszczan and Frail attributed to Earth-mass planets, the first confirmed exoplanets. The same residual analysis now searches for nanohertz gravitational waves.", "map": "\\Delta t_R=\\frac{a_p\\sin i}{c}\\sin\\left(\\frac{2\\pi t}{P_{\\rm orb}}+\\phi\\right)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2080", "a": "05-relativity-and-gravitation/gravitational-waves/pulsar-timing-arrays", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Millisecond pulsars as a galactic GW detector", "kind": "method transfer", "summary": "Millisecond pulsars, spun up by accretion in binaries, are clocks stable to ~100 ns over decades. PTAs turn an ensemble of them into a galaxy-sized detector whose arms are pulsar–Earth baselines. Intrinsic spin noise and dispersion-measure variations are the main systematics.", "map": "\\Gamma(\\zeta)=\\frac32x\\ln x-\\frac x4+\\frac12,\\ x=\\frac{1-\\cos\\zeta}{2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2081", "a": "05-relativity-and-gravitation/gravitational-waves/space-based-and-future-detectors", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients", "name": "Gravitational waves from core-collapse supernovae", "kind": "shared object", "summary": "A Galactic core-collapse supernova should emit a GW burst from proto-neutron-star oscillations, convection and SASI, with h~10⁻²¹–10⁻²² at 10 kpc. Current detectors reach only the Milky Way. Third-generation detectors such as Einstein Telescope would extend that reach and, alongside the neutrino burst, probe the explosion mechanism.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2082", "a": "05-relativity-and-gravitation/quantum-gravity/loop-quantum-gravity", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Loop quantum cosmology bounce before inflation", "kind": "mechanism", "summary": "Loop quantum cosmology replaces the big-bang singularity with a bounce at ρ_c≈0.41 ρ_Pl, using an effective Friedmann equation. The bounce sets pre-inflationary initial conditions and can suppress low-ℓ CMB power. These signatures depend on the model and are unconfirmed.", "map": "H^2=\\frac{8\\pi G}{3}\\rho\\left(1-\\frac{\\rho}{\\rho_c}\\right),\\quad \\rho_c\\approx0.41\\,\\rho_{\\rm Pl}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2083", "a": "05-relativity-and-gravitation/quantum-gravity/qft-in-curved-spacetime", "b": "09-astrophysics-and-cosmology/cosmology/dark-energy", "name": "Vacuum energy and the cosmological constant problem", "kind": "identity", "summary": "Lorentz invariance forces the renormalised vacuum stress tensor into the form ⟨T_μν⟩=−ρ_vac c² g_μν, which gravitates exactly like Λ. Naive estimates of ρ_vac exceed the observed ~6×10⁻²⁷ kg m⁻³, about (2.3 meV)⁴, by up to ~120 orders of magnitude: the cosmological constant problem.", "map": "\\langle T_{\\mu\\nu}\\rangle_{\\rm vac}=-\\rho_{\\rm vac}c^2g_{\\mu\\nu}\\ \\Rightarrow\\ \\Lambda_{\\rm eff}=\\Lambda+\\frac{8\\pi G}{c^2}\\rho_{\\rm vac}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2084", "a": "05-relativity-and-gravitation/quantum-gravity/qft-in-curved-spacetime", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Quantum vacuum fluctuations seed cosmic structure", "kind": "mechanism", "summary": "Inflationary perturbations are QFT on a quasi-de Sitter background. Bunch–Davies vacuum fluctuations of the inflaton and the graviton are stretched beyond the horizon and freeze, becoming the nearly scale-invariant scalar spectrum (n_s≈0.965) and a tensor spectrum set by H/M_Pl.", "map": "P_\\zeta=\\frac{H^2}{8\\pi^2\\epsilon M_{\\rm Pl}^2},\\quad P_t=\\frac{2H^2}{\\pi^2M_{\\rm Pl}^2}\\ (\\hbar=c=1)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2085", "a": "05-relativity-and-gravitation/special-relativity/lorentz-transformations-and-spacetime", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "CMB dipole: our motion through the relic radiation", "kind": "mechanism", "summary": "A Lorentz boost turns an isotropic blackbody into a blackbody whose temperature depends on direction. The 3.36 mK CMB dipole implies the Solar System moves at ~370 km/s, and Planck detected the accompanying aberration and Doppler modulation of the small-scale anisotropies. The CMB frame is a cosmological rest frame, not a violation of relativity.", "map": "T(\\theta)=\\frac{T_0}{\\gamma(1-\\beta\\cos\\theta)},\\quad \\beta\\approx1.23\\times10^{-3}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2086", "a": "05-relativity-and-gravitation/special-relativity/lorentz-transformations-and-spacetime", "b": "09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history", "name": "Cosmological redshift vs special-relativistic Doppler", "kind": "analogy", "summary": "At low z the cosmological redshift looks like a Doppler shift with v≈cz, and any FLRW redshift can be built from infinitesimal Doppler shifts parallel-transported along the photon path. The recession velocity in Hubble's law is not a Lorentz velocity, however.", "map": "1+z=\\frac{a_0}{a_e}\\ \\text{vs}\\ 1+z=\\sqrt{\\frac{1+\\beta}{1-\\beta}}", "breaks": "Recession speeds v=Hd exceed c beyond the Hubble sphere, and z records the expansion between emission and reception, not a relative velocity in one inertial frame. Converting z to a velocity with the SR formula gives wrong distances at z≳0.5.", "confidence": "established", "strength": 1}
{"id": "C2087", "a": "05-relativity-and-gravitation/special-relativity/lorentz-transformations-and-spacetime", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "name": "Cosmic-ray muons: time dilation observed", "kind": "historical", "summary": "Muons produced by cosmic rays ~15 km up reach sea level only because their 2.2 μs lifetime is dilated by γ~10–50. Rossi and Hall's 1941 measurement of muon flux against altitude was one of the first direct confirmations of relativistic time dilation.", "map": "N(h)=N_0\\exp\\left(-\\frac{h}{\\gamma\\beta c\\tau_\\mu}\\right),\\quad \\tau_\\mu=2.197\\,\\mu{\\rm s}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2088", "a": "05-relativity-and-gravitation/special-relativity/relativistic-kinematics-and-dynamics", "b": "09-astrophysics-and-cosmology/galaxies/active-galactic-nuclei-and-supermassive-black-holes", "name": "Superluminal motion and Doppler boosting in jets", "kind": "mechanism", "summary": "Jet components moving at β≈1 close to our line of sight show apparent transverse speeds up to γβc, observed up to tens of c. Their flux is boosted by a high power of the Doppler factor δ, which is why blazars dominate the extragalactic gamma-ray sky.", "map": "\\beta_{\\rm app}=\\frac{\\beta\\sin\\theta}{1-\\beta\\cos\\theta},\\quad \\delta=\\frac{1}{\\gamma(1-\\beta\\cos\\theta)},\\quad S_\\nu\\propto\\delta^{3+\\alpha}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2089", "a": "05-relativity-and-gravitation/special-relativity/relativistic-kinematics-and-dynamics", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "name": "Threshold kinematics: the GZK cutoff", "kind": "identity", "summary": "Cosmic-ray protons above ~5×10¹⁹ eV photoproduce pions on CMB photons. The threshold follows from the invariant s, and at Lorentz factors γ~10¹¹ these losses limit proton horizons to ~100 Mpc, which explains the observed flux suppression.", "map": "s=(m_p+m_\\pi)^2c^4\\Rightarrow E_{\\rm th}=\\frac{m_\\pi(2m_p+m_\\pi)c^4}{4E_\\gamma}\\ (\\text{head-on})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2090", "a": "05-relativity-and-gravitation/special-relativity/relativistic-kinematics-and-dynamics", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/gamma-ray-bursts", "name": "Compactness problem demands Γ≳100 outflows", "kind": "mechanism", "summary": "Millisecond GRB variability implies a tiny source, whose MeV photon density would be opaque to γγ→e⁺e⁻. The emitter must move with bulk Lorentz factor Γ≳100: beaming lowers comoving photon energies below pair threshold and enlarges the inferred emission radius by Γ².", "map": "R\\lesssim2\\Gamma^2c\\,\\delta t,\\quad E_1E_2(1-\\cos\\theta_{12})\\ge2(m_ec^2)^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2091", "a": "05-relativity-and-gravitation/special-relativity/tests-of-lorentz-invariance", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/gamma-ray-bursts", "name": "GRB photon timing bounds Lorentz violation", "kind": "method transfer", "summary": "Quantum-gravity-motivated dispersion, v≈c(1−ξE/E_QG), would delay high-energy photons from cosmological GRBs relative to low-energy ones. Fermi-LAT timing of GRB 090510 pushed the linear-order scale E_QG past the Planck energy.", "map": "\\Delta t\\approx\\frac{\\xi\\,\\Delta E}{E_{\\rm QG}}\\int_0^z\\frac{(1+z')\\,dz'}{H(z')}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2297", "a": "06-particle-physics/beyond-the-standard-model", "b": "09-astrophysics-and-cosmology/cosmology", "name": "Early universe as the testing ground for BSM physics", "kind": "shared object", "summary": "Three cosmological facts need physics beyond the Standard Model: dark matter, the baryon asymmetry and inflation. In the thermal history, interaction rates are compared with the Hubble rate, and this tests BSM masses and couplings against Ω_c, η_B, N_eff and the primordial spectrum.", "map": "\\Gamma(T)\\sim H(T)=1.66\\sqrt{g_*}\\,T^2/M_{Pl}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2298", "a": "06-particle-physics/beyond-the-standard-model", "b": "09-astrophysics-and-cosmology/dark-matter", "name": "Dark matter requires physics beyond the Standard Model", "kind": "shared object", "summary": "No Standard Model particle can be the astrophysical dark matter, because neutrinos are too light and too hot. Its gravitational evidence is therefore the strongest empirical case for new particles, and each BSM model maps to its own direct, indirect, collider and structure-formation signatures.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2299", "a": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "b": "09-astrophysics-and-cosmology/dark-matter", "name": "Misalignment axions as cold dark matter", "kind": "mechanism", "summary": "After the QCD transition, the axion field starts oscillating from a misaligned initial angle, and these coherent oscillations redshift like cold matter. For f_a~10¹¹–10¹² GeV they give the observed density, which ties the strong-CP solution to galactic halos.", "map": "\\Omega_ah^2\\approx0.12\\,\\theta_i^2\\left(\\frac{f_a}{9\\times10^{11}\\,\\mathrm{GeV}}\\right)^{7/6}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2300", "a": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "b": "09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure", "name": "Ultralight axions as fuzzy dark matter", "kind": "mechanism", "summary": "An axion-like field with m~10⁻²² eV has a kpc-scale de Broglie wavelength, so halos grow solitonic cores with interference granules and small-scale power is suppressed. Lyman-α and dwarf-galaxy kinematics now push m≳10⁻²¹–10⁻²⁰ eV, which squeezes the original small-scale motivation.", "map": "i\\hbar\\partial_t\\psi=-\\frac{\\hbar^2}{2m}\\nabla^2\\psi+m\\Phi\\psi,\\quad\\nabla^2\\Phi=4\\pi Gm|\\psi|^2", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2301", "a": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Axion haloscopes as direct detection of wave-like DM", "kind": "shared object", "summary": "Through the aFF̃ coupling, galactic-halo axions convert to microwave photons inside a magnetised resonant cavity (ADMX, HAYSTAC). The local dark-matter density and the halo velocity dispersion set the signal power and the line width.", "map": "P\\propto g_{a\\gamma\\gamma}^2\\frac{\\rho_{DM}}{m_a}B_0^2VC\\min(Q_L,Q_a),\\quad h\\nu\\simeq m_ac^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2302", "a": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "name": "Stellar energy-loss bounds on light particles", "kind": "method transfer", "summary": "Any light, weakly coupled particle made in a stellar plasma escapes freely and carries energy away. The red-giant-branch tip, horizontal-branch star counts (R-parameter) and white-dwarf cooling bound g_aγγ≲0.66×10⁻¹⁰ GeV⁻¹, g_ae~10⁻¹³ and the neutrino magnetic moment, rivalling laboratory searches.", "map": "\\epsilon_x\\lesssim10\\,\\mathrm{erg\\,g^{-1}\\,s^{-1}}\\ \\text{(red-giant core before He flash)}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2303", "a": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients", "name": "SN 1987A burst duration bounds new particles", "kind": "method transfer", "summary": "SN 1987A's ~10 s neutrino signal shows the proto-neutron star cooled by neutrino diffusion. Extra free-streaming emission of axions, dark photons or sterile neutrinos would have shortened it, which bounds axion–nucleon couplings (m_a≲10–20 meV) and leaves a 'trapping' window open for strongly coupled heavier particles.", "map": "\\epsilon_x\\lesssim10^{19}\\,\\mathrm{erg\\,g^{-1}\\,s^{-1}}\\ \\text{at}\\ \\rho\\approx3\\times10^{14}\\,\\mathrm{g\\,cm^{-3}},\\ T\\approx30\\,\\mathrm{MeV}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2304", "a": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "name": "Solar axions, helioscopes and solar-model limits", "kind": "shared object", "summary": "Primakoff conversion of thermal photons in the ~1.3 keV solar core makes a keV axion flux, which helioscopes (CAST, IAXO) reconvert to X-rays by pointing a magnet at the Sun. Helioseismology and solar neutrino fluxes independently cap the extra energy loss at about 0.1 L_⊙.", "map": "P_{a\\to\\gamma}=\\left(\\frac{g_{a\\gamma\\gamma}BL}{2}\\right)^2\\quad(qL\\ll1)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2305", "a": "06-particle-physics/beyond-the-standard-model/baryogenesis-and-matter-antimatter", "b": "09-astrophysics-and-cosmology/cosmology", "name": "Baryon asymmetry: measured by cosmology, explained by BSM", "kind": "shared object", "summary": "Cosmology measures η_B≈6.1×10⁻¹⁰, and BBN and the CMB agree on it. Particle physics must generate this value through Sakharov's conditions: B violation, C and CP violation, and a departure from equilibrium supplied by the expansion or by a first-order phase transition.", "map": "\\eta_B=\\frac{n_B-n_{\\bar B}}{n_\\gamma}\\approx6.1\\times10^{-10}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2306", "a": "06-particle-physics/beyond-the-standard-model/baryogenesis-and-matter-antimatter", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "CMB acoustic peaks measure the baryon asymmetry", "kind": "shared object", "summary": "Baryon loading changes the relative heights of the odd and even acoustic peaks, which fixes Ω_b h²≈0.0224 and hence η_B≈6.1×10⁻¹⁰. Every baryogenesis mechanism (electroweak, leptogenesis, Affleck–Dine) must reproduce this target, and BBN deuterium cross-checks it independently.", "map": "\\eta_B\\approx273.9\\times10^{-10}\\,\\Omega_bh^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2307", "a": "06-particle-physics/beyond-the-standard-model/dark-matter-particle-candidates", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "CMB limits on dark-matter annihilation at recombination", "kind": "mechanism", "summary": "Dark matter annihilating around z~600–1000 injects energy that ionises hydrogen and broadens last scattering. Planck bounds p_ann below 3.2×10⁻²⁸ cm³ s⁻¹ GeV⁻¹, excluding s-wave thermal relics below about 10–30 GeV with no dependence on halo modelling.", "map": "p_{ann}=f_{eff}\\frac{\\langle\\sigma v\\rangle}{m_\\chi}<3.2\\times10^{-28}\\,\\mathrm{cm^3\\,s^{-1}\\,GeV^{-1}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2308", "a": "06-particle-physics/beyond-the-standard-model/dark-matter-particle-candidates", "b": "09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history", "name": "Relic abundance from Boltzmann freeze-out", "kind": "mechanism", "summary": "Thermal relics follow a Boltzmann equation on the FRW background, and annihilation stops once n⟨σv⟩ drops below H at x_f=m/T_f≈20–25. The relic density therefore depends on the expansion rate and g_*: weak-scale ⟨σv⟩ gives Ωh²≈0.12, while freeze-in or non-standard expansion such as early matter domination shifts the answer.", "map": "\\dot n+3Hn=-\\langle\\sigma v\\rangle\\left(n^2-n_{eq}^2\\right)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2309", "a": "06-particle-physics/beyond-the-standard-model/dark-matter-particle-candidates", "b": "09-astrophysics-and-cosmology/dark-matter", "name": "Astrophysics brackets the dark-matter mass range", "kind": "shared object", "summary": "Candidates span about 90 orders of magnitude in mass, and astrophysics sets the edges. Tremaine–Gunn phase-space packing in dwarfs needs fermions heavier than roughly 0.1–1 keV, galaxy-scale de Broglie wavelengths bound bosons from below at m≳10⁻²¹ eV, and microlensing limits compact-object dark matter.", "map": "\\lambda_{dB}=\\frac{h}{mv}\\approx0.5\\,\\mathrm{kpc}\\,\\frac{10^{-22}\\,\\mathrm{eV}}{m}\\,\\frac{250\\,\\mathrm{km\\,s^{-1}}}{v}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2310", "a": "06-particle-physics/beyond-the-standard-model/dark-matter-particle-candidates", "b": "09-astrophysics-and-cosmology/dark-matter/astrophysical-evidence-for-dark-matter", "name": "Astrophysical evidence fixes candidate properties", "kind": "shared object", "summary": "Rotation curves, cluster lensing, the Bullet Cluster and the CMB require a non-baryonic component with Ω_c h²≈0.12 that is cold or at most warm and collisionless or only weakly self-interacting. Every particle candidate must meet these constraints.", "map": "\\Omega_ch^2=0.120\\pm0.001,\\quad\\sigma/m\\lesssim1\\,\\mathrm{cm^2\\,g^{-1}}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2311", "a": "06-particle-physics/beyond-the-standard-model/dark-matter-particle-candidates", "b": "09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure", "name": "DM microphysics imprinted on small-scale structure", "kind": "mechanism", "summary": "Each candidate leaves its own small-scale mark: warm dark matter free-streams, fuzzy dark matter has a quantum-pressure Jeans scale, and self-interacting dark matter thermalises halo cores. The Lyman-α forest, Milky Way satellites, lensing substructure and stellar streams turn these imprints into bounds on particle mass and cross section.", "map": "k_J=(16\\pi G\\rho a^4)^{1/4}(m/\\hbar)^{1/2},\\quad\\sigma/m\\sim1\\,\\mathrm{cm^2\\,g^{-1}}\\ \\text{for SIDM cores}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2312", "a": "06-particle-physics/beyond-the-standard-model/dark-matter-particle-candidates", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "WIMP–nucleus elastic scattering rate", "kind": "mechanism", "summary": "The nuclear-recoil spectrum folds the particle cross section, coherently enhanced as A² for spin-independent couplings, with the local halo density and velocity distribution. Liquid-xenon TPCs (LZ, XENONnT) now exclude σ_SI below 10⁻⁴⁷ cm² near 30–40 GeV.", "map": "\\frac{dR}{dE_R}=\\frac{\\rho_\\chi\\sigma_0F^2(q)}{2m_\\chi\\mu_N^2}\\int_{v>v_{min}}\\frac{f(\\mathbf v)}{v}d^3v,\\quad\\sigma_0\\propto A^2\\mu_N^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2313", "a": "06-particle-physics/beyond-the-standard-model/dark-matter-particle-candidates", "b": "09-astrophysics-and-cosmology/dark-matter/indirect-detection", "name": "Thermal-relic cross section predicts annihilation signals", "kind": "mechanism", "summary": "The ⟨σv⟩≈3×10⁻²⁶ cm³/s that sets the relic density also predicts today's annihilation flux of γ-rays, positrons, antiprotons and neutrinos from dense regions, and Fermi-LAT dwarf limits exclude thermal s-wave WIMPs below about 100 GeV in the bb̄ channel. The Galactic Center excess is a candidate signal, disputed because millisecond pulsars could explain it.", "map": "\\frac{d\\Phi}{dE}=\\frac{\\langle\\sigma v\\rangle}{8\\pi m_\\chi^2}\\frac{dN}{dE}\\int_{\\Delta\\Omega}\\!\\int_{los}\\rho^2\\,dl\\,d\\Omega", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2314", "a": "06-particle-physics/beyond-the-standard-model/extra-dimensions-and-hierarchy-problem", "b": "09-astrophysics-and-cosmology/cosmology/dark-energy", "name": "Cosmological-constant and Higgs-mass naturalness", "kind": "analogy", "summary": "Both are UV-sensitivity problems of effective field theory. Vacuum-energy corrections scale as Λ_UV⁴ against an observed (2.3 meV)⁴, just as Higgs-mass corrections scale as Λ_UV², and the same remedies (SUSY, extra dimensions, relaxation, anthropic selection) are tried on both.", "map": "\\delta m_H^2\\sim\\frac{\\Lambda_{UV}^2}{16\\pi^2},\\quad\\delta\\rho_{vac}\\sim\\frac{\\Lambda_{UV}^4}{16\\pi^2}\\ \\text{vs}\\ \\rho_\\Lambda^{obs}\\approx(2.3\\,\\mathrm{meV})^4", "breaks": "TeV-scale SUSY or compositeness can cancel δm_H², but no known symmetry cancels vacuum energy while letting SUSY be broken. The cosmological-constant problem is still ~60 orders of magnitude off with a TeV cutoff, and it involves gravity directly.", "confidence": "established", "strength": 2}
{"id": "C2315", "a": "06-particle-physics/beyond-the-standard-model/grand-unification-and-proton-decay", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "GUT monopole problem motivated inflation", "kind": "historical", "summary": "Breaking a simple GUT group down to a subgroup containing U(1)_em leaves nontrivial π₂ of the vacuum manifold. The Kibble mechanism then makes about one monopole per horizon volume, enough to overclose the universe, and Guth designed inflation partly to dilute them. GUT-scale vacuum energy remains a natural inflation scale, with V^{1/4}≲1.4×10¹⁶ GeV from r<0.036.", "map": "\\pi_2(G/H)=\\pi_1(H)\\supseteq\\mathbb Z\\ \\text{when}\\ H\\supset U(1)_{em},\\quad V^{1/4}=\\left(\\tfrac{3\\pi^2}{2}A_sr\\right)^{1/4}M_P", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2316", "a": "06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Collider vs direct-detection complementarity", "kind": "method transfer", "summary": "In simplified-mediator and Higgs-portal models the same couplings set both LHC missing-energy rates (mono-jet, invisible Higgs decays with BR<0.107) and nuclear-recoil rates. Collider limits therefore map onto the σ_SI–m_χ plane and dominate below a few GeV, where recoils are too soft to detect.", "map": "\\sigma_{SI}^{h\\text{-portal}}=\\frac{\\lambda_{h\\chi}^2f_N^2\\mu^2m_N^2}{4\\pi m_h^4m_\\chi^2}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2317", "a": "06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "name": "LHC data calibrate air-shower hadronic models", "kind": "method transfer", "summary": "Ultra-high-energy cosmic rays collide at √s≈430 TeV per nucleon pair, so reading composition from X_max and muon counts means extrapolating hadronic models (EPOS-LHC, Sibyll, QGSJET) tuned at the LHC, including forward LHCf data and the 2025 oxygen runs. The observed muon excess in air showers, the 'muon puzzle', points to mismodelled forward hadron production.", "map": "\\sqrt{s}\\approx\\sqrt{2m_pE}\\approx430\\,\\mathrm{TeV}\\ \\ (E=10^{20}\\,\\mathrm{eV})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2318", "a": "06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "name": "Cosmic rays as particle physics's first beam", "kind": "historical", "summary": "Before accelerators, cloud chambers and emulsions exposed to cosmic rays revealed the positron (1932), the muon (1936), the pion (1947) and strange particles. The detector lineage now runs the other way: collider-style silicon trackers, calorimeters and magnetic spectrometers fly as AMS-02, DAMPE and Fermi-LAT.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2319", "a": "06-particle-physics/neutrino-physics", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle", "name": "Pion decay links neutrinos, γ-rays and cosmic rays", "kind": "mechanism", "summary": "Accelerated hadrons hitting gas or photons make pions. Charged pions decay to neutrinos with E_ν≈E_p/20 and neutral pions to γ-rays with E_γ≈E_p/10, so decay kinematics tie the neutrino, γ-ray and cosmic-ray fluxes of TXS 0506+056, NGC 1068 and the Galactic plane together.", "map": "\\pi^+\\to\\mu^+\\nu_\\mu\\to e^+\\nu_e\\bar\\nu_\\mu\\nu_\\mu,\\quad\\pi^0\\to\\gamma\\gamma", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2320", "a": "06-particle-physics/neutrino-physics", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/neutrino-astronomy", "name": "Neutrino astronomy runs on particle-physics neutrinos", "kind": "shared object", "summary": "Neutrino telescopes need particle-physics inputs: cross sections, oscillation parameters and flavour identification. In return they supply natural beams at TeV–PeV energies and Mpc–Gpc baselines that no accelerator reaches, which test oscillations, neutrino decay and Lorentz invariance.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2321", "a": "06-particle-physics/neutrino-physics/neutrino-experiments-and-sources", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Neutrino fog: CEvNS in dark-matter detectors", "kind": "shared object", "summary": "Coherent elastic neutrino–nucleus scattering, first observed by COHERENT, gives nuclear recoils that look like WIMP recoils. Solar ⁸B neutrinos mimic a ~6 GeV WIMP and atmospheric and DSNB neutrinos set a 'fog' that slows sensitivity gains; XENONnT and PandaX-4T reported first ~2.6–2.7σ indications of ⁸B CEvNS in 2024.", "map": "\\frac{d\\sigma}{dE_R}=\\frac{G_F^2m_N}{4\\pi}Q_W^2\\left(1-\\frac{m_NE_R}{2E_\\nu^2}\\right)F^2(q),\\quad Q_W\\approx N-(1-4\\sin^2\\theta_W)Z", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2322", "a": "06-particle-physics/neutrino-physics/neutrino-experiments-and-sources", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/neutrino-astronomy", "name": "Water-Cherenkov detection scaled to km³ telescopes", "kind": "method transfer", "summary": "IceCube, KM3NeT and Baikal-GVD reuse the Kamiokande/Super-K water-Cherenkov technique at gigaton scale in ice or sea water. The same detectors treat atmospheric neutrinos as background for astronomy and as signal for oscillation physics (DeepCore, ORCA).", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2323", "a": "06-particle-physics/neutrino-physics/neutrino-experiments-and-sources", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "name": "pp-chain and CNO neutrinos test stellar fusion", "kind": "shared object", "summary": "Hydrogen burning makes stars neutrino sources, and the measured pp, ⁷Be, ⁸B and CNO fluxes confirm the stellar energy source directly. Neutrino energy losses (plasma, pair and Urca processes) drive late stellar evolution.", "map": "4p\\to{}^4\\mathrm{He}+2e^++2\\nu_e+26.7\\,\\mathrm{MeV}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2324", "a": "06-particle-physics/neutrino-physics/neutrino-experiments-and-sources", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients", "name": "Core-collapse supernova neutrinos", "kind": "shared object", "summary": "About 99% of the ~3×10⁵³ erg released in core collapse leaves as neutrinos of all flavours over ~10 s. Kamiokande-II, IMB and Baksan caught about 25 events from SN 1987A, confirming the picture, and Super-K-Gd, JUNO, DUNE and IceCube now await a Galactic burst and the diffuse supernova neutrino background.", "map": "E_b\\approx\\frac{3}{5}\\frac{GM_{NS}^2}{R_{NS}}\\approx3\\times10^{53}\\,\\mathrm{erg}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2325", "a": "06-particle-physics/neutrino-physics/neutrino-experiments-and-sources", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "name": "Solar neutrinos and the standard solar model", "kind": "shared object", "summary": "Solar neutrino fluxes from Homestake to Borexino tested the standard solar model, and SNO showed the deficit came from flavour conversion, not from the model. Helioseismology independently confirmed the model's sound-speed profile, and Borexino's CNO flux now probes the solar metallicity problem.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2326", "a": "06-particle-physics/neutrino-physics/neutrino-mass-and-double-beta-decay", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "CMB bounds on the sum of neutrino masses", "kind": "shared object", "summary": "Massive relic neutrinos turn from radiation into matter after recombination, which changes the early ISW effect and the CMB lensing potential. Planck bounds Σm_ν below about 0.12 eV, which complements the model-independent kinematic tritium bound from KATRIN.", "map": "\\Omega_\\nu h^2=\\frac{\\sum m_\\nu}{93.14\\,\\mathrm{eV}}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2327", "a": "06-particle-physics/neutrino-physics/neutrino-mass-and-double-beta-decay", "b": "09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao", "name": "Neutrino free-streaming suppresses matter clustering", "kind": "mechanism", "summary": "Relic neutrinos do not cluster below their free-streaming scale, so small-scale matter power drops by ΔP/P≈−8f_ν. With BAO fixing the expansion history, DESI DR1 plus CMB gives Σm_ν<0.072 eV (95%), pressing against the 0.059 eV minimum for normal ordering.", "map": "\\frac{\\Delta P}{P}\\approx-8f_\\nu,\\quad f_\\nu=\\Omega_\\nu/\\Omega_m", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2328", "a": "06-particle-physics/neutrino-physics/neutrino-oscillations", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/neutrino-astronomy", "name": "Astrophysical neutrino flavour ratios", "kind": "method transfer", "summary": "Over cosmic baselines oscillations average out, so a pion-decay source ratio of 1:2:0 arrives at Earth as about 1:1:1. IceCube's measured flavour composition, including ν_τ candidates and a Glashow-resonance event near 6.3 PeV, tests the source mechanism and new physics such as neutrino decay or Lorentz violation.", "map": "\\bar P_{\\alpha\\beta}=\\sum_i|U_{\\alpha i}|^2|U_{\\beta i}|^2", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2329", "a": "06-particle-physics/neutrino-physics/neutrino-oscillations", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients", "name": "Collective neutrino flavour conversion in supernovae", "kind": "mechanism", "summary": "Near a proto-neutron star, ν–ν forward scattering makes flavour evolution a nonlinear many-body problem, with spectral swaps and fast flavour instabilities. These may change neutrino heating behind the shock and r-process conditions, but how much they matter for the explosion is unresolved.", "map": "H_{\\mathbf p}=\\frac{\\Delta m^2}{2E}B+\\sqrt2G_Fn_eL+\\sqrt2G_F\\!\\int\\!(1-\\cos\\theta_{\\mathbf{pq}})(\\rho_{\\mathbf q}-\\bar\\rho_{\\mathbf q})\\,d\\mathbf q", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2330", "a": "06-particle-physics/neutrino-physics/neutrino-oscillations", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "name": "MSW resonance in the solar density profile", "kind": "mechanism", "summary": "Coherent forward scattering on solar electrons adds the potential √2 G_F n_e, so ⁸B neutrinos cross the resonance adiabatically and leave as ν₂ with P_ee≈sin²θ₁₂≈0.3. Low-energy pp neutrinos keep the vacuum-averaged P_ee≈0.55, and Borexino measured the transition between the two.", "map": "\\sqrt2G_Fn_e^{res}=\\frac{\\Delta m^2_{21}\\cos2\\theta_{12}}{2E}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2331", "a": "06-particle-physics/neutrino-physics/sterile-neutrinos-and-anomalies", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "N_eff limits on light sterile neutrinos", "kind": "shared object", "summary": "An eV-scale sterile neutrino with the mixing suggested by the LSND, MiniBooNE and gallium anomalies would be thermalised before BBN, adding ΔN_eff≈1 and ~1 eV to Σm_ν. Planck's N_eff=2.99±0.17 and mass bounds exclude it unless self-interactions or lepton asymmetries suppress production; extra dark radiation as a Hubble-tension fix is proposed but disfavoured.", "map": "\\rho_r=\\left[1+\\frac78\\left(\\frac{4}{11}\\right)^{4/3}N_{eff}\\right]\\rho_\\gamma", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2332", "a": "06-particle-physics/neutrino-physics/sterile-neutrinos-and-anomalies", "b": "09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure", "name": "keV sterile neutrinos as warm dark matter", "kind": "shared object", "summary": "A keV sterile neutrino produced by oscillations (Dodelson–Widrow) or resonantly (Shi–Fuller) is warm dark matter whose free-streaming suppresses dwarf-scale power. Lyman-α and satellite counts combined with X-ray limits on ν_s→νγ exclude non-resonant production, and the claimed 3.5 keV line remains contested.", "map": "\\Gamma_{\\nu_s\\to\\nu\\gamma}=\\frac{9\\alpha G_F^2}{1024\\pi^4}\\sin^22\\theta\\,m_s^5", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2333", "a": "06-particle-physics/quantum-field-theory/effective-field-theory", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Effective field theory of inflation", "kind": "method transfer", "summary": "Inflationary perturbations are treated as the Goldstone mode π of broken time translations, with operators ordered by derivatives as in chiral perturbation theory. A reduced sound speed predicts f_NL^equil∝(1−c_s²)/c_s², and heavy fields leave oscillatory 'cosmological collider' signals in the squeezed bispectrum.", "map": "S_\\pi=\\int d^4x\\sqrt{-g}\\,\\frac{-M_P^2\\dot H}{c_s^2}\\left[\\dot\\pi^2-c_s^2\\frac{(\\partial_i\\pi)^2}{a^2}\\right]+\\dots", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2334", "a": "06-particle-physics/quantum-field-theory/effective-field-theory", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "EFT tower for dark-matter–nucleus scattering", "kind": "method transfer", "summary": "Direct-detection rates come from an EFT chain. Mediator-scale operators run down to quark and gluon operators, nucleon matrix elements (σ_πN, spin fractions) and chiral EFT match them to nucleons, and the result is a basis of Galilean-invariant non-relativistic operators — the same tower used for flavour physics and nuclear forces.", "map": "\\mathcal O_1=1_\\chi1_N,\\ \\mathcal O_4=\\vec S_\\chi\\cdot\\vec S_N,\\ \\dots\\ \\text{from}\\ i\\vec q,\\ \\vec v^{\\perp},\\ \\vec S_\\chi,\\ \\vec S_N", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2335", "a": "06-particle-physics/quantum-field-theory/lattice-field-theory", "b": "09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history", "name": "Lattice QCD crossover in the early universe", "kind": "shared object", "summary": "Lattice QCD shows the quark–hadron transition near 156 MeV is a smooth crossover, so it leaves no bubbles and no strong gravitational-wave signal. The lattice equation of state supplies g_*(T), and the topological susceptibility χ(T) feeds WIMP and axion relic-abundance calculations.", "map": "T_{pc}\\approx156.5\\pm1.5\\,\\mathrm{MeV},\\quad\\rho=\\frac{\\pi^2}{30}g_*(T)T^4", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2336", "a": "06-particle-physics/standard-model/electroweak-theory", "b": "09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history", "name": "Weak freeze-out sets neutrino decoupling and n/p", "kind": "mechanism", "summary": "Weak rates Γ≈G_F²T⁵ fall below the Hubble rate at T≈1 MeV, so neutrinos decouple. Electron–positron annihilation then heats the photons, giving T_ν=(4/11)^{1/3}T_γ and N_eff=3.044, and the frozen n/p≈1/7 fixes primordial helium Y_p≈0.25; the Fermi constant thereby shapes the expansion history.", "map": "G_F^2T^5\\sim\\frac{T^2}{M_{Pl}}\\Rightarrow T_{dec}\\sim(G_F^2M_{Pl})^{-1/3}\\approx1\\,\\mathrm{MeV}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2337", "a": "06-particle-physics/standard-model/higgs-boson", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Higgs inflation and electroweak vacuum stability", "kind": "mechanism", "summary": "With a large nonminimal coupling ξ|H|²R (ξ~10⁴), the measured Higgs can act as the inflaton and gives Starobinsky-like predictions n_s≈0.965 and r≈0.003. Conversely, the running Higgs quartic turns negative near 10¹⁰–10¹¹ GeV, so the metastable electroweak vacuum constrains the Hubble scale during inflation and reheating.", "map": "S\\supset\\int\\!\\sqrt{-g}\\,\\frac{M_P^2+\\xi h^2}{2}R,\\quad n_s\\approx1-\\frac{2}{N},\\ r\\approx\\frac{12}{N^2}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2338", "a": "06-particle-physics/standard-model/quantum-chromodynamics", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Dense QCD and the neutron-star equation of state", "kind": "shared object", "summary": "Neutron-star cores reach several times nuclear saturation density, where QCD is nonperturbative and lattice QCD fails because of the sign problem. Masses ≳2 M_⊙, NICER radii and GW170817 tidal deformability constrain the equation of state, testing hyperons, deconfined quark matter and colour superconductivity, while perturbative QCD bounds the high-density end.", "map": "\\frac{dP}{dr}=-\\frac{G(\\epsilon+P)(m+4\\pi r^3P)}{r^2(r-2Gm)}\\quad(c=1)", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2489", "a": "07-nuclear-physics/applied-nuclear-physics/nuclear-data-and-isotope-production", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "name": "Evaluated reaction-rate libraries for stellar models", "kind": "method transfer", "summary": "Stellar evolution and explosion codes use evaluated thermonuclear rate compilations (REACLIB, NACRE) built from nuclear data and Hauser-Feshbach theory, so evaluation and covariance methods from nuclear data propagate into stellar predictions.", "map": "N_A\\langle\\sigma v\\rangle=\\exp\\!\\left[a_0+\\sum_{i=1}^5a_iT_9^{(2i-5)/3}+a_6\\ln T_9\\right]", "breaks": "Many network rates are theoretical; uncertainties are correlated and often lack covariance information.", "confidence": "established", "strength": 2}
{"id": "C2490", "a": "07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Low-background radiation detectors for dark matter", "kind": "method transfer", "summary": "Dark-matter direct detection uses nuclear-physics detector technology (scintillators, HPGe, noble-liquid ionization) and radiation-protection-grade background control; nuclear-recoil quenching and gamma/neutron backgrounds are nuclear-physics problems.", "map": "E_{\\rm ee}=\\mathcal L(E_{nr})E_{nr}\\ \\text{(Lindhard quenching)}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2491", "a": "07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle", "name": "Nuclear radiation detectors as gamma-ray telescopes", "kind": "method transfer", "summary": "MeV gamma-ray astronomy (nuclear lines, GRBs) uses nuclear-spectroscopy detectors: NaI and BGO scintillators, HPGe spectrometers (INTEGRAL/SPI) and Compton telescopes, with the same photoelectric/Compton/pair physics and activation backgrounds.", "map": "\\cos\\theta=1-m_ec^2\\left(\\frac1{E_2}-\\frac1{E_1+E_2}\\right)\\ \\text{(Compton imaging)};\\ \\frac{\\sigma_E}{E}=2.355\\sqrt{\\frac{Fw}{E}}", "breaks": "Space instruments face cosmic-ray activation and must reject a large instrumental background.", "confidence": "established", "strength": 2}
{"id": "C2492", "a": "07-nuclear-physics/hadron-and-nucleon-structure/parton-distribution-functions", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/neutrino-astronomy", "name": "PDFs set ultra-high-energy neutrino cross sections", "kind": "method transfer", "summary": "The neutrino-nucleon cross section above ~10 TeV is deep-inelastic scattering dominated by small-x sea quarks and gluons; IceCube's Earth-absorption measurement agrees with PDF-based predictions, and small-x uncertainty (and saturation) sets the high-energy event rate.", "map": "\\frac{d^2\\sigma_{\\nu N}}{dx\\,dy}=\\frac{2G_F^2ME_\\nu}{\\pi}\\frac{M_W^4}{(Q^2+M_W^2)^2}[xq(x,Q^2)+x\\bar q(x,Q^2)(1-y)^2];\\ \\sigma\\propto E^{0.36}", "breaks": "At the highest energies the relevant x lies below HERA's reach, so predictions extrapolate DGLAP or invoke saturation.", "confidence": "established", "strength": 2}
{"id": "C2493", "a": "07-nuclear-physics/heavy-ion-physics", "b": "09-astrophysics-and-cosmology/cosmology", "name": "QGP epoch of the early universe", "kind": "shared object", "summary": "The universe was a quark-gluon plasma until ~10 microseconds, when it cooled through the QCD crossover at T_c ~ 156 MeV; heavy-ion collisions recreate that matter, and the lattice equation of state measured there fixes the early-universe expansion rate through that epoch.", "map": "t\\approx\\frac{2.4\\,\\text{s}}{\\sqrt{g_*}}\\left(\\frac{\\text{MeV}}{T}\\right)^2\\Rightarrow t(T_c)\\sim10\\ \\mu\\text{s}", "breaks": "Heavy-ion fireballs have mu_B > 0 at lower energies, are tiny and expand in ~10 fm/c, and are not in global equilibrium; the cosmic transition is at mu_B ~ 0 and expands over microseconds.", "confidence": "established", "strength": 2}
{"id": "C2494", "a": "07-nuclear-physics/heavy-ion-physics", "b": "09-astrophysics-and-cosmology/dark-matter/indirect-detection", "name": "Antinuclei: coalescence and absorption for dark matter", "kind": "method transfer", "summary": "Antideuterons and antihelium in cosmic rays would be a near background-free dark-matter signature; coalescence parameters measured in heavy-ion and pp collisions and ALICE's antihelium absorption cross sections set both the expected signal and the cosmic-ray background.", "map": "E_A\\frac{d^3N_A}{dp_A^3}=B_A\\left(E_p\\frac{d^3N_p}{dp_p^3}\\right)^A", "breaks": "Coalescence depends on source size, which differs between Galactic dark-matter annihilation and collider systems.", "confidence": "current research", "strength": 2}
{"id": "C2495", "a": "07-nuclear-physics/heavy-ion-physics/qcd-phase-diagram-and-critical-point", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Quark-matter cores in massive neutron stars", "kind": "shared object", "summary": "Model-agnostic EOS inference combining perturbative QCD at high density with nuclear EFT at low density finds the speed of sound and polytropic index in the cores of ~2-solar-mass stars consistent with deconfined quark matter.", "map": "\\gamma=\\frac{d\\ln P}{d\\ln\\varepsilon}<1.75\\ \\text{(quark-like)};\\ c_s^2=\\frac{dP}{d\\varepsilon}", "breaks": "The criterion is a heuristic; hadronic matter with a peaked sound speed can mimic it, so the claim is contested.", "confidence": "current research", "strength": 2}
{"id": "C2496", "a": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "b": "09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history", "name": "Lattice QCD equation of state and early-universe g_*", "kind": "method transfer", "summary": "The lattice QCD equation of state and susceptibilities, tested against heavy-ion data, give the effective degrees of freedom g_*(T) and g_*s(T) through the QCD crossover, which enter relic-abundance and axion-density calculations.", "map": "\\rho=\\frac{\\pi^2}{30}g_*(T)T^4,\\ s=\\frac{2\\pi^2}{45}g_{*s}(T)T^3;\\ g_*:\\ 61.75\\to17.25\\ \\text{across }T_c", "breaks": "Cosmic use needs mu_B ~ 0 and full equilibrium, where lattice QCD is reliable; heavy-ion data mainly validate it.", "confidence": "established", "strength": 2}
{"id": "C2497", "a": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "name": "QGP-like collectivity and the air-shower muon puzzle", "kind": "mechanism", "summary": "Air showers contain more muons than hadronic models predict; strangeness enhancement and core-corona collectivity seen in high-multiplicity LHC collisions, implemented in models such as EPOS, are candidate explanations, linking QGP signatures to cosmic-ray composition.", "map": "N_\\mu\\propto A^{1-\\beta}(E/A)^{\\beta},\\ \\beta\\approx0.9;\\ \\text{energy fraction to }\\pi^0\\ \\text{sets }N_\\mu", "breaks": "Air showers involve forward-rapidity, light-ion collisions beyond collider coverage, so the extrapolation is uncertain.", "confidence": "current research", "strength": 2}
{"id": "C2498", "a": "07-nuclear-physics/nuclear-astrophysics", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/multi-messenger-astronomy", "name": "Neutron-star mergers as nuclear laboratories", "kind": "shared object", "summary": "Binary neutron-star mergers tie nuclear physics to multi-messenger signals: the EOS sets the inspiral tidal phase and remnant fate, and r-process nucleosynthesis powers the kilonova.", "map": "\\tilde\\Lambda\\ \\text{from GW phase}\\ \\leftrightarrow\\ P(\\varepsilon);\\ L_{\\rm KN}(t)\\propto\\dot\\epsilon_{\\rm r}(t)\\approx t^{-1.3}", "breaks": "Mergers mix nuclear uncertainties with GR-MHD and neutrino transport uncertainties, so inferences are model-dependent.", "confidence": "established", "strength": 3}
{"id": "C2499", "a": "07-nuclear-physics/nuclear-astrophysics", "b": "09-astrophysics-and-cosmology/stellar-astrophysics", "name": "Nuclear burning powers stars and builds elements", "kind": "mechanism", "summary": "Thermonuclear reaction rates set the luminosity, lifetime and composition of stars at every stage, from pp burning through silicon burning and explosive nucleosynthesis.", "map": "\\epsilon_{\\rm nuc}=\\sum\\frac{\\rho X_iX_j}{m_im_j}\\langle\\sigma v\\rangle_{ij}Q_{ij};\\ L=\\int\\epsilon_{\\rm nuc}\\,dm", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2500", "a": "07-nuclear-physics/nuclear-astrophysics/big-bang-nucleosynthesis", "b": "09-astrophysics-and-cosmology/cosmology", "name": "Expansion rate versus weak freeze-out in BBN", "kind": "mechanism", "summary": "Primordial abundances are set where the Friedmann expansion rate overtakes the weak n-p conversion rate (T ~ 0.8 MeV) and the deuterium bottleneck opens (T ~ 0.07 MeV); BBN is therefore a test of cosmology at MeV temperatures, constraining N_eff and new physics.", "map": "\\Gamma_{np}\\sim G_F^2T^5\\approx H=\\sqrt{\\frac{8\\pi^3g_*}{90}}\\frac{T^2}{M_{\\rm Pl}}\\Rightarrow T_f\\approx0.8\\ \\text{MeV}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2501", "a": "07-nuclear-physics/nuclear-astrophysics/big-bang-nucleosynthesis", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "Baryon density from BBN and CMB agree", "kind": "shared object", "summary": "Deuterium from quasar absorbers gives Omega_b h^2 through BBN at ~1 percent, matching the CMB acoustic-peak value: two physically independent measurements of the same baryon-to-photon ratio, minutes and 380 kyr after the Big Bang.", "map": "\\eta_{10}=273.9\\,\\Omega_bh^2;\\ \\Omega_bh^2|_{\\rm BBN+D/H}\\approx0.022\\approx\\Omega_bh^2|_{\\rm CMB}", "breaks": "The BBN value depends on nuclear rates (d(p,gamma)3He) and D/H systematics; the CMB value depends on the LambdaCDM fit.", "confidence": "established", "strength": 3}
{"id": "C2502", "a": "07-nuclear-physics/nuclear-astrophysics/big-bang-nucleosynthesis", "b": "09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history", "name": "BBN tests the Friedmann equation at MeV temperatures", "kind": "mechanism", "summary": "BBN abundances measure the radiation-dominated expansion rate H(T) and g_*, testing the Friedmann equation and the relativistic-species content 1-1000 s after the Big Bang, the earliest direct probe of the expansion history.", "map": "H^2=\\frac{8\\pi G}{3}\\frac{\\pi^2}{30}g_*T^4;\\ N_{\\rm eff}=2.9\\pm0.3\\ \\text{(BBN)}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2503", "a": "07-nuclear-physics/nuclear-astrophysics/big-bang-nucleosynthesis", "b": "09-astrophysics-and-cosmology/cosmology/hubble-tension-and-cosmological-tensions", "name": "BBN plus BAO gives a CMB-independent H0", "kind": "method transfer", "summary": "Deuterium-calibrated BBN fixes the baryon density, which sets the sound horizon for BAO without CMB anisotropies; the resulting H0 agrees with Planck, so the Hubble tension is not a CMB-specific systematic. BBN also limits early-dark-energy and extra-radiation fixes through N_eff.", "map": "r_d=\\int_{z_d}^\\infty\\frac{c_s(z)}{H(z)}dz,\\ c_s=\\frac{c}{\\sqrt{3(1+3\\rho_b/4\\rho_\\gamma)}};\\ \\Delta Y_p\\approx0.013\\Delta N_{\\rm eff}", "breaks": "The result inherits LambdaCDM late-time assumptions and the d(p,gamma) rate uncertainty.", "confidence": "current research", "strength": 2}
{"id": "C2504", "a": "07-nuclear-physics/nuclear-astrophysics/big-bang-nucleosynthesis", "b": "09-astrophysics-and-cosmology/dark-matter/astrophysical-evidence-for-dark-matter", "name": "BBN baryon budget demands non-baryonic dark matter", "kind": "mechanism", "summary": "BBN limits baryons to Omega_b ~ 0.05, while dynamics, lensing and the CMB need Omega_m ~ 0.3; most matter must therefore be non-baryonic, one of the strongest independent arguments for particle dark matter.", "map": "\\frac{\\Omega_c}{\\Omega_b}\\approx5.4;\\ \\Omega_bh^2\\approx0.022\\ll\\Omega_mh^2\\approx0.14", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2505", "a": "07-nuclear-physics/nuclear-astrophysics/big-bang-nucleosynthesis", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "name": "Lithium problem: primordial or stellar depletion?", "kind": "mechanism", "summary": "Standard BBN predicts 7Li/H about three times the Spite plateau in metal-poor halo stars; whether the gap is nuclear (7Be destruction rates), stellar (atomic diffusion and mixing in stellar atmospheres) or new physics is unresolved, with stellar depletion now favoured.", "map": "(\\mathrm{Li/H})_{\\rm BBN}\\approx5\\times10^{-10}\\ \\text{vs}\\ (\\mathrm{Li/H})_{\\rm Spite}\\approx1.6\\times10^{-10}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2506", "a": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Neutron stars as dark-matter detectors", "kind": "analogy", "summary": "Dark matter captured by scattering on neutron-star nucleons would heat old neutron stars; the capture rate uses the same dark-matter-nucleon cross section as direct detection, with neutron-star nuclear matter and Pauli blocking replacing the target nucleus.", "map": "C\\propto\\frac{\\rho_\\chi}{m_\\chi}\\sigma_{\\chi n}\\frac{v_{\\rm esc}^2}{v_\\chi}N_n;\\ T_{\\rm NS}\\sim1700\\ \\text{K}", "breaks": "Capture in dense matter involves strong-interaction medium effects and relativistic kinematics, and no candidate star has been observed at the required temperature.", "confidence": "proposed", "strength": 1}
{"id": "C2507", "a": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/fast-radio-bursts-and-magnetars", "name": "Magnetar crusts: starquakes, QPOs and outbursts", "kind": "mechanism", "summary": "Magnetar bursts, giant flares and possibly FRBs are driven by crust stresses from evolving 1e15 G fields; crust breaking strain, shear modulus and seismic modes from nuclear and crust physics set burst energetics and QPO frequencies.", "map": "E_{\\rm el}\\sim\\mu\\,\\epsilon_{\\rm br}^2V_{\\rm crust}/2;\\ f_{\\rm torsional}\\approx\\frac{v_t}{2\\pi R}\\sqrt{\\ell(\\ell+1)}\\sim20\\text{–}100\\ \\text{Hz}", "breaks": "Whether FRBs come from crust events or from magnetospheric or wind processes is unresolved.", "confidence": "current research", "strength": 2}
{"id": "C2508", "a": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/gamma-ray-bursts", "name": "Maximum mass from merger remnants and short GRBs", "kind": "mechanism", "summary": "Whether a merger remnant collapses promptly, after a delay, or survives as a magnetar depends on the maximum neutron-star mass; the GW170817 short GRB and kilonova energetics argued for delayed collapse, suggesting M_max of about 2.2-2.3 solar masses.", "map": "M_{\\rm thr}\\approx kM_{\\rm max},\\ k\\sim1.3\\text{–}1.7;\\ M_{\\rm TOV}\\lesssim2.2\\text{–}2.3\\,M_\\odot", "breaks": "The argument depends on interpreting the kilonova ejecta and jet energetics, which are model-dependent.", "confidence": "current research", "strength": 2}
{"id": "C2509", "a": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/multi-messenger-astronomy", "name": "Tidal deformability from GW170817 constrains the EOS", "kind": "shared object", "summary": "The GW170817 inspiral phase measured the binary tidal deformability, limiting neutron-star radii to ~11-13 km and excluding the stiffest nuclear EOS; joint analyses with NICER and nuclear data now bound pressure at twice saturation density.", "map": "\\Lambda=\\frac23k_2\\left(\\frac{c^2R}{GM}\\right)^5;\\ \\tilde\\Lambda_{1.4}\\lesssim800\\Rightarrow R_{1.4}\\lesssim13.5\\ \\text{km}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2510", "a": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Dense-matter EOS sets neutron-star masses and radii", "kind": "shared object", "summary": "The TOV equation turns the nuclear EOS into a mass-radius curve; 2-solar-mass pulsars, NICER radii and GW tidal deformabilities constrain matter up to several times saturation density.", "map": "\\frac{dP}{dr}=-\\frac{G(\\varepsilon+P)(m+4\\pi r^3P/c^2)}{c^2r(r-2Gm/c^2)},\\ \\frac{dm}{dr}=\\frac{4\\pi r^2\\varepsilon}{c^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2511", "a": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients", "name": "EOS in core collapse and proto-neutron stars", "kind": "mechanism", "summary": "Core bounce, proto-neutron-star contraction, neutrino-driven explosion and black-hole formation depend on the finite-temperature nuclear EOS (stiffness, symmetry energy, nuclear statistical equilibrium composition).", "map": "\\rho_{\\rm bounce}\\gtrsim n_0m_N\\approx2.7\\times10^{14}\\ \\text{g cm}^{-3};\\ \\Gamma_{\\rm ad}>4/3\\ \\text{halts collapse}", "breaks": "Supernova EOS tables need finite temperature and proton fraction 0.05-0.5, beyond the cold beta-equilibrium EOS of neutron stars.", "confidence": "established", "strength": 2}
{"id": "C2512", "a": "07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process", "b": "09-astrophysics-and-cosmology/galaxies/galaxy-formation-and-evolution", "name": "Nucleosynthesis yields drive galactic chemical evolution", "kind": "mechanism", "summary": "Galaxy-formation simulations and chemical-evolution models use stellar and explosive yields (alpha elements from core collapse, Fe from Ia, s from AGB, r from mergers) as inputs; alpha/Fe ratios then clock star-formation histories.", "map": "\\frac{d(\\Sigma_gZ_i)}{dt}=-Z_i\\psi+\\int\\psi(t-\\tau)\\,y_i(m)\\,\\phi(m)\\,dm+\\cdots", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2513", "a": "07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process", "b": "09-astrophysics-and-cosmology/galaxies/the-milky-way", "name": "Galactic archaeology of r-process-enhanced stars", "kind": "shared object", "summary": "Europium-rich metal-poor halo stars, the actinide-boost class and the single-event enrichment of the dwarf galaxy Reticulum II test which sites (rare, prolific mergers or collapsars) made the Milky Way's r-process elements and when.", "map": "[\\mathrm{Eu/Fe}]\\ \\text{vs}\\ [\\mathrm{Fe/H}];\\ \\text{universal pattern }56<Z<76", "breaks": "Merger delay times and natal kicks complicate the link between abundance trends and sites.", "confidence": "current research", "strength": 2}
{"id": "C2514", "a": "07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/fast-radio-bursts-and-magnetars", "name": "Magnetar giant flares as r-process sites", "kind": "mechanism", "summary": "Delayed MeV gamma-ray emission after the 2004 SGR 1806-20 giant flare matches radioactive decay of freshly synthesized r-process nuclei in baryon-loaded ejecta, suggesting magnetars contribute a few percent of the r-process.", "map": "", "breaks": "Single-event evidence; the ejecta mass and Y_e are inferred from models.", "confidence": "current research", "strength": 2}
{"id": "C2515", "a": "07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/gamma-ray-bursts", "name": "Collapsars as r-process sites", "kind": "mechanism", "summary": "Neutron-rich accretion-disk outflows in collapsars (the engines of long GRBs) may make r-process material comparable to mergers, which would explain early-galaxy enrichment; near-infrared follow-up of long GRBs is testing this.", "map": "Y_e<0.25\\Rightarrow\\text{lanthanides};\\ \\tau_n\\ll\\tau_\\beta", "breaks": "Disk-outflow Y_e depends on neutrino transport and magnetic physics that simulations do not yet agree on.", "confidence": "current research", "strength": 2}
{"id": "C2516", "a": "07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/multi-messenger-astronomy", "name": "Kilonova AT2017gfo and r-process nucleosynthesis", "kind": "shared object", "summary": "The optical-infrared kilonova after GW170817 was powered by radioactive decay of freshly made r-process nuclei, and its red component showed lanthanide-rich ejecta, the first direct identification of an r-process site.", "map": "\\kappa_{\\rm lanth}\\sim10\\ \\text{cm}^2\\text{g}^{-1}\\gg\\kappa_{\\rm Fe};\\ t_{\\rm peak}\\approx\\sqrt{\\frac{\\kappa M}{4\\pi vc}}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2517", "a": "07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/binary-stars-and-stellar-populations", "name": "s-process in AGB stars and barium/CEMP binaries", "kind": "mechanism", "summary": "Barium stars and carbon-enhanced metal-poor (CEMP-s) stars got their s-process overabundances by mass transfer from an AGB companion, so binary populations map the s-process yields and neutron exposures of extinct AGB stars.", "map": "^{13}\\mathrm C(\\alpha,n)^{16}\\mathrm O,\\ ^{22}\\mathrm{Ne}(\\alpha,n)^{25}\\mathrm{Mg};\\ \\tau_0=\\int n_nv_T\\,dt", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2518", "a": "07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "name": "Stellar evolution drives s-process and burning stages", "kind": "mechanism", "summary": "Burning stages (H, He, C, Ne, O, Si) follow core contraction; thermal pulses in AGB stars release neutrons via 13C(alpha,n) and 22Ne(alpha,n) for the s-process, and the triple-alpha rate through the Hoyle state sets the C/O ratio.", "map": "3\\alpha\\to{}^{12}\\text{C}\\ (E_{\\rm Hoyle}=7.65\\ \\text{MeV});\\ \\tau_n\\gg\\tau_\\beta\\ (s)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2519", "a": "07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients", "name": "Supernovae as nucleosynthesis sites", "kind": "mechanism", "summary": "Core-collapse supernovae make the alpha elements and iron-peak nuclei through explosive burning and the nu-p and weak r-process; thermonuclear (Ia) supernovae make most of the iron. Ordinary core-collapse ejecta fail to reach the third r-process peak.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2520", "a": "07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Urca processes and neutrino cooling of compact stars", "kind": "mechanism", "summary": "Neutron stars cool by direct and modified Urca beta processes whose rates depend on the proton fraction and pairing; accreting crusts hold Urca shells, and electron capture onto nuclei sets white-dwarf and crust compositions.", "map": "n\\to pe\\bar\\nu_e,\\ pe\\to n\\nu_e;\\ \\text{direct Urca if }x_p\\gtrsim0.11;\\ \\epsilon_{\\rm dU}\\propto T^6,\\ \\epsilon_{\\rm mU}\\propto T^8", "breaks": "The proton fraction and pairing gaps in the core are uncertain, so cooling curves constrain them only jointly.", "confidence": "established", "strength": 2}
{"id": "C2521", "a": "07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients", "name": "Electron capture and weak rates in core collapse", "kind": "mechanism", "summary": "Electron captures on iron-group and neutron-rich nuclei (Gamow-Teller strength from the shell model) deleptonize the collapsing core and set the homologous-core mass, shock energy and neutrino signal of core-collapse supernovae.", "map": "\\lambda_{\\rm EC}=\\frac{\\ln2}{K}\\sum_{if}\\frac{(2J_i+1)e^{-E_i/kT}}{G}B_{if}(GT)\\,\\Phi_{if}(T,\\rho Y_e);\\ Y_e:0.42\\to0.30", "breaks": "Gamow-Teller strength of hot, neutron-rich nuclei far from stability is only partly measured; tables extrapolate shell-model and QRPA results.", "confidence": "established", "strength": 3}
{"id": "C2522", "a": "07-nuclear-physics/nuclear-reactions-and-decays/fusion-reactions", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets", "name": "Deuterium burning separates brown dwarfs from planets", "kind": "mechanism", "summary": "The deuterium-burning mass limit (~13 Jupiter masses) is the conventional boundary between giant planets and brown dwarfs; it is set by when the core reaches the D(p,gamma)3He Gamow window before electron degeneracy halts contraction.", "map": "\\mathrm{D}+p\\to{}^3\\mathrm{He}+\\gamma\\ (5.5\\ \\text{MeV});\\ M_{\\rm D}\\approx13M_J", "breaks": "The limit depends on helium and deuterium fraction and metallicity; formation mode, not burning, may be the better planet criterion.", "confidence": "established", "strength": 1}
{"id": "C2523", "a": "07-nuclear-physics/nuclear-reactions-and-decays/fusion-reactions", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "name": "Gamow-peak fusion sets stellar structure", "kind": "mechanism", "summary": "Stellar energy generation is set by sub-barrier fusion at the Gamow peak; the steep temperature dependence of the CNO cycle versus pp chain decides convective cores and the main-sequence mass-luminosity relation.", "map": "\\langle\\sigma v\\rangle\\propto\\int S(E)e^{-E/k_BT-\\sqrt{E_G/E}}dE;\\ \\epsilon_{pp}\\propto T^4,\\ \\epsilon_{\\rm CNO}\\propto T^{18}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2524", "a": "07-nuclear-physics/nuclear-reactions-and-decays/fusion-reactions", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients", "name": "Carbon fusion rate and thermonuclear ignition", "kind": "mechanism", "summary": "Carbon ignition in white dwarfs (Type Ia supernovae), carbon flashes and X-ray superbursts depend on the low-energy 12C+12C fusion rate, whose resonant structure below 2 MeV remains uncertain.", "map": "E_0\\approx1.5\\ \\text{MeV at }T_9=0.5;\\ \\text{ignition when }\\epsilon_{\\rm nuc}>\\epsilon_\\nu", "breaks": "Laboratory data stop above the Gamow window, and electron screening in dense plasmas modifies the rate.", "confidence": "current research", "strength": 2}
{"id": "C2525", "a": "07-nuclear-physics/nuclear-reactions-and-decays/fusion-reactions", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "name": "Solar neutrinos measure pp-chain and CNO burning", "kind": "mechanism", "summary": "Neutrino fluxes from the pp chain (pp, 7Be, 8B) and the first detection of CNO neutrinos test laboratory fusion cross sections in the solar core; the CNO flux bears on the solar metallicity (abundance) problem raised by helioseismology.", "map": "\\Phi_{\\rm 8B}\\propto S_{17}S_{34}^{0.8}T_c^{24};\\ \\Phi_{\\rm CNO}\\propto Z_{\\rm CN}\\,S_{1,14}", "breaks": "Interpreting fluxes needs neutrino oscillation (MSW) parameters and the solar model's opacities.", "confidence": "established", "strength": 3}
{"id": "C2526", "a": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-fission", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/multi-messenger-astronomy", "name": "Fission yields shape r-process patterns and kilonovae", "kind": "mechanism", "summary": "Fission of the heaviest r-process nuclei recycles material to the second peak, shapes the rare-earth abundances and, through 254Cf, can dominate late-time kilonova heating; fission barriers and yields far from stability are a major r-process uncertainty.", "map": "\\text{fission recycling: }A\\gtrsim250\\to2\\times(A\\sim130);\\ ^{254}\\mathrm{Cf}\\ t_{1/2}=60.5\\ \\text{d}", "breaks": "Barriers and fragment yields of neutron-rich actinides come from models without measurements.", "confidence": "current research", "strength": 2}
{"id": "C2527", "a": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Coherent neutrino-nucleus scattering and the neutrino fog", "kind": "mechanism", "summary": "Coherent elastic neutrino-nucleus scattering, observed by COHERENT, gives nuclear recoils indistinguishable from WIMP signals; solar 8B and atmospheric neutrinos thus form the neutrino fog of direct detection, with rates set by the weak charge and neutron form factor.", "map": "\\frac{d\\sigma}{dT}=\\frac{G_F^2M}{4\\pi}Q_W^2\\left(1-\\frac{MT}{2E_\\nu^2}\\right)F^2(q),\\ Q_W\\approx N-(1-4\\sin^2\\theta_W)Z", "breaks": "The neutrino background is irreducible only for the same recoil spectrum; directionality and target complementarity partly separate it.", "confidence": "established", "strength": 2}
{"id": "C2528", "a": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "name": "Cosmic-ray spallation and Li-Be-B production", "kind": "mechanism", "summary": "Spallation of cosmic-ray C, N, O on interstellar H and He makes Li, Be and B; secondary-to-primary ratios such as B/C measure the grammage traversed and calibrate Galactic propagation, so they rest on nuclear fragmentation cross sections.", "map": "\\frac{dN_s}{dX}=\\sum_p\\frac{\\sigma_{p\\to s}}{m}N_p-\\frac{N_s}{\\lambda_s};\\ \\frac{\\mathrm B}{\\mathrm C}\\propto X(E)\\propto E^{-\\delta}", "breaks": "Fragmentation cross sections are known to only 10-20 percent, which now limits AMS-02 propagation analyses.", "confidence": "established", "strength": 3}
{"id": "C2529", "a": "07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/multi-messenger-astronomy", "name": "Radioactive heating of kilonova ejecta", "kind": "mechanism", "summary": "Kilonovae are powered by the summed beta decays and fission of thousands of r-process nuclei, giving a heating rate close to t^-1.3; the luminosity therefore measures ejected r-process mass.", "map": "\\dot\\epsilon(t)\\approx10^{10}\\left(\\frac{t}{1\\,\\text{d}}\\right)^{-1.3}\\ \\text{erg g}^{-1}\\text{s}^{-1}", "breaks": "Thermalization efficiency and the uncertain beta-decay rates and masses of neutron-rich nuclei limit the mass inference to a factor of a few.", "confidence": "established", "strength": 3}
{"id": "C2530", "a": "07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks", "name": "26Al heating and chronometry of the early Solar System", "kind": "mechanism", "summary": "Excess 26Mg in meteoritic inclusions shows live 26Al (t1/2 = 0.72 Myr) was present when the first solids formed; its decay heat melted and differentiated planetesimals, and short-lived radionuclides give Myr-resolution chronologies of disk evolution.", "map": "\\left(\\frac{^{26}\\mathrm{Al}}{^{27}\\mathrm{Al}}\\right)_0\\approx5\\times10^{-5};\\ \\Delta t=\\frac{1}{\\lambda}\\ln\\frac{R_0}{R}", "breaks": "Dating assumes 26Al was homogeneously distributed in the disk, which is debated.", "confidence": "established", "strength": 2}
{"id": "C2531", "a": "07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients", "name": "Radioactive 56Ni-56Co decay powers supernova light curves", "kind": "mechanism", "summary": "Type Ia and stripped-envelope supernova light curves are powered by 56Ni -> 56Co -> 56Fe decay (6.1 d and 77 d), so the peak luminosity measures the nickel mass (Arnett's rule) and the tail follows the cobalt half-life; 44Ti maps in Cas A trace explosion asymmetry.", "map": "^{56}\\mathrm{Ni}\\xrightarrow{6.1\\,\\rm d}{}^{56}\\mathrm{Co}\\xrightarrow{77\\,\\rm d}{}^{56}\\mathrm{Fe};\\ L_{\\rm peak}\\approx\\dot E_{\\rm Ni}(t_{\\rm peak});\\ L_{\\rm tail}\\propto e^{-t/111\\,\\rm d}", "breaks": "Gamma-ray escape and positron trapping make the deposited luminosity differ from the decay luminosity at late times.", "confidence": "established", "strength": 3}