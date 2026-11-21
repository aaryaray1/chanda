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

### Gravitational lensing · `knowledge/09-astrophysics-and-cosmology/cosmology/gravitational-lensing`

**Scope.** Deflection angle and the 1919 eclipse test, lens equation, Einstein radius, multiple images and arcs, caustics, time delays and $H_0$, weak lensing shear and convergence, cosmic shear surveys (KiDS, DES, HSC, Euclid), CMB lensing, galaxy–galaxy lensing, microlensing exoplanets and MACHO searches.

**Core ideas.**
- Lensing measures total mass, dark or luminous, without assumptions about dynamics.
- Weak lensing distorts galaxy shapes by ~1%; statistics over millions of galaxies map dark matter.
- Microlensing light curves reveal planets and compact objects too faint to see.

**Key equations.**
$$\hat\alpha=\frac{4GM}{c^2b},\qquad \theta_E=\sqrt{\frac{4GM}{c^2}\frac{D_{ls}}{D_lD_s}},\qquad \boldsymbol\beta=\boldsymbol\theta-\frac{D_{ls}}{D_s}\hat{\boldsymbol\alpha}(\boldsymbol\theta)$$

**See also.** [Tests of GR](knowledge/05-relativity-and-gravitation/general-relativity/tests-of-general-relativity/README.md) · [Geometric optics](knowledge/02-electromagnetism-and-optics/classical-optics/geometric-optics/README.md)

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

### Alternatives: MOND and modified gravity · `knowledge/09-astrophysics-and-cosmology/dark-matter/alternatives-mond-and-modified-gravity`

**Scope.** Milgrom's acceleration scale $a_0\approx1.2\times10^{-10}$ m/s², baryonic Tully–Fisher and the radial acceleration relation, external-field effect, TeVeS and AeST relativistic theories, wide-binary tests (contested results), cluster residual mass problem, CMB peaks and the need for extra degrees of freedom, emergent gravity proposals.

**Core ideas.**
- MOND predicts galaxy rotation curves from baryons alone with one parameter, explaining the baryonic Tully–Fisher relation $M_b\propto v^4$.
- It fails to remove the need for unseen mass in clusters and struggles with the CMB without additional fields.
- GW170817 ruled out several relativistic MOND theories in which gravity and light travel differently.

**Key equations.**
$$\mu\!\left(\frac{|\mathbf a|}{a_0}\right)\mathbf a=\mathbf a_N,\qquad v_\infty^4=GM_ba_0$$

**Landmark.** Milgrom (1983) — see [subfield landmarks](knowledge/09-astrophysics-and-cosmology/dark-matter/README.md).

**See also.** [Modified gravity (GR)](knowledge/05-relativity-and-gravitation/general-relativity/modified-gravity/README.md) · [Philosophy of physics](knowledge/00-foundations/history-and-philosophy-of-physics/philosophy-of-physics/README.md)

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

# Packet 09-1 (100 records)

{"id": "C0363", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao", "name": "Simulation-based inference and emulators for LSS", "kind": "method transfer", "summary": "Neural emulators replace expensive N-body or Boltzmann runs, and neural density estimators enable likelihood-free inference from galaxy surveys and weak lensing.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0364", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients", "name": "ML classification of transients", "kind": "method transfer", "summary": "Time-domain surveys such as ZTF and Rubin rely on neural classifiers and anomaly detection to triage millions of alerts and photometrically classify supernovae.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0365", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao", "name": "N-body simulations as gravitational MD", "kind": "method transfer", "summary": "Cosmological N-body codes use the same symplectic leapfrog integrators and force softening as MD, with tree or particle-mesh gravity in place of Lennard-Jones forces.", "map": "\\ddot{\\mathbf{x}}_i=-\\sum_{j\\ne i}\\frac{Gm_j(\\mathbf{x}_i-\\mathbf{x}_j)}{(|\\mathbf{x}_{ij}|^2+\\epsilon^2)^{3/2}}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0366", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "MCMC for CMB parameter estimation", "kind": "method transfer", "summary": "Metropolis-Hastings sampling, as in CosmoMC, explores the multidimensional CMB likelihood. It made six-parameter ΛCDM fits to Planck tractable.", "map": "\\alpha=\\min\\left(1,\\frac{P(\\theta')}{P(\\theta)}\\right)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0367", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "Boltzmann codes for CMB spectra", "kind": "method transfer", "summary": "CAMB and CLASS integrate coupled Einstein–Boltzmann hierarchies for photons, baryons, neutrinos and dark matter. Stiff ODE solvers handle tight coupling before recombination.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0368", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "09-astrophysics-and-cosmology/galaxies/galaxy-formation-and-evolution", "name": "Hydrodynamic solvers in cosmological simulations", "kind": "method transfer", "summary": "Finite-volume, AMR and SPH schemes evolve gas with gravity in galaxy-formation simulations. Subgrid models for cooling, star formation and feedback supply the physics that is not resolved.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0369", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics", "name": "Symplectic integrators for orbital dynamics", "kind": "historical", "summary": "Wisdom–Holman mapping splits the Hamiltonian into Kepler and perturbation parts. It enabled long-term chaos studies of planetary orbits and the Nice model.", "map": "H=H_{\\rm Kepler}+\\epsilon H_{\\rm int}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0370", "a": "00-foundations/history-and-philosophy-of-physics/philosophy-of-physics", "b": "09-astrophysics-and-cosmology/dark-matter/alternatives-mond-and-modified-gravity", "name": "Dark matter vs modified gravity as theory choice", "kind": "analogy", "summary": "The MOND versus particle dark matter debate mirrors Neptune versus Vulcan: anomalies can be absorbed by new matter or new laws. It engages Lakatosian research programmes and underdetermination.", "map": "", "breaks": "Unlike Vulcan, the dark-matter hypothesis has independent evidence from the CMB and the Bullet Cluster, and MOND struggles with clusters.", "confidence": "established", "strength": 2}
{"id": "C0371", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "Spherical harmonics and Legendre expansion of the CMB", "kind": "identity", "summary": "The temperature sky is expanded in spherical harmonics, and the angular power spectrum is the rotation-invariant variance. Statistical isotropy makes the C_ℓ the full description of Gaussian fluctuations.", "map": "\\frac{\\delta T}{T}=\\sum a_{\\ell m}Y_{\\ell m},\\ C_\\ell=\\langle|a_{\\ell m}|^2\\rangle", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0372", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "09-astrophysics-and-cosmology/galaxies/the-milky-way", "name": "Special functions in galactic potentials", "kind": "method transfer", "summary": "Galactic potentials and Poisson solutions in disk geometry use Bessel functions, Legendre expansions and elliptic integrals. They underpin mass models fitted to Gaia kinematics.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C0373", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao", "name": "Poisson equation and the growth of perturbations", "kind": "mechanism", "summary": "Linear perturbations obey a damped-oscillator-like ODE sourced by the Poisson equation. Green's-function solutions yield growth factors and the transfer function that shapes the matter power spectrum.", "map": "\\ddot\\delta+2H\\dot\\delta=4\\pi G\\bar\\rho\\,\\delta", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0374", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "name": "Stellar structure as a nonlinear boundary-value problem", "kind": "mechanism", "summary": "Hydrostatic equilibrium, mass continuity, energy generation and transport form coupled ODEs with boundary conditions at centre and surface. The Lane–Emden equation is the polytropic special case.", "map": "\\frac{1}{\\xi^2}\\frac{d}{d\\xi}\\left(\\xi^2\\frac{d\\theta}{d\\xi}\\right)=-\\theta^n", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0375", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history", "name": "FLRW as a maximally symmetric spacetime", "kind": "identity", "summary": "The FLRW metric is the warped product of time with a maximally symmetric 3-space of constant curvature k. Friedmann equations follow from the Einstein tensor evaluated on it.", "map": "ds^2=-dt^2+a^2\\left[\\frac{dr^2}{1-kr^2}+r^2d\\Omega^2\\right]", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0376", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "09-astrophysics-and-cosmology/cosmology/gravitational-lensing", "name": "Lensing as geodesic deflection in curved spacetime", "kind": "identity", "summary": "Null geodesics in a weak-field metric give the deflection angle, and the lens equation maps it to image positions. Shear and convergence are components of the Jacobian of the lens map.", "map": "\\hat\\alpha=\\frac{4GM}{c^2 b},\\quad A_{ij}=\\delta_{ij}-\\partial_i\\partial_j\\psi", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0377", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "TES bolometers and CMB polarimetry", "kind": "method transfer", "summary": "CMB experiments such as ACT, SPT and BICEP use transition-edge-sensor arrays limited by photon and thermal noise, with SQUID multiplexed readout.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0378", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Cryogenic sensors and low-background detectors", "kind": "method transfer", "summary": "Transition-edge sensors, bolometers and low-noise readout, developed for general detector physics, enable sub-GeV dark-matter searches. Noise floors and background rejection set the reach.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0379", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "09-astrophysics-and-cosmology/cosmology", "name": "Cosmology as statistical inference", "kind": "method transfer", "summary": "Cosmology has a single observable universe, so cosmic variance, MCMC chains, Fisher forecasts and Bayesian evidence are the core tools for extracting parameters and testing models.", "map": "F_{ij}=-\\langle\\partial_i\\partial_j\\ln L\\rangle", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0380", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history", "name": "Bayesian inference of ΛCDM parameters", "kind": "method transfer", "summary": "Cosmological parameters are fitted by Bayesian posterior sampling over likelihoods built from CMB, BAO and supernova data, with priors and model comparison deciding between ΛCDM extensions.", "map": "P(\\theta|d)\\propto L(d|\\theta)\\,\\pi(\\theta)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0381", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history", "name": "Priors, degeneracies and model selection in ΛCDM", "kind": "method transfer", "summary": "Parameter degeneracies (e.g. Ωm–H0, w0–wa) and prior choices shape cosmological constraints. Information criteria and Bayes factors adjudicate extensions such as curvature or dynamical dark energy.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0382", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Profile likelihood and exclusion limits", "kind": "method transfer", "summary": "Direct-detection limits use profile-likelihood tests, CLs and the Feldman–Cousins construction. Background-dominated searches face the look-elsewhere effect and the neutrino fog.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0383", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-detection", "name": "Detection statistics for exoplanet signals", "kind": "method transfer", "summary": "Planet detection uses periodograms, false-alarm probabilities, MCMC orbit fits and Bayesian model comparison for the number of planets. Noise from stellar activity requires Gaussian-process modelling.", "map": "\\ln B_{10}=\\ln\\frac{Z_1}{Z_0}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0384", "a": "00-foundations/measurement-and-data-analysis/uncertainty-and-error-propagation", "b": "09-astrophysics-and-cosmology/cosmology/hubble-tension-and-cosmological-tensions", "name": "Systematics budgets in the H0 tension", "kind": "shared object", "summary": "The H0 tension's significance depends on how statistical and systematic errors, covariances and calibration chains (Cepheids, TRGB) are propagated. Distance-ladder error budgets are an applied GUM-style case.", "map": "\\sigma_{H_0}^2=\\sum_{ij}\\frac{\\partial H_0}{\\partial x_i}\\frac{\\partial H_0}{\\partial x_j}C_{ij}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0385", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history", "name": "CP violation and the baryon asymmetry", "kind": "mechanism", "summary": "Sakharov's conditions require C and CP violation, baryon-number violation and departure from equilibrium to generate the matter–antimatter asymmetry. The Standard Model's CP violation is far too small.", "map": "\\eta=\\frac{n_B}{n_\\gamma}\\approx6\\times10^{-10}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0386", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "09-astrophysics-and-cosmology/dark-matter/indirect-detection", "name": "Particle-physics symmetries behind annihilation signals", "kind": "shared object", "summary": "Annihilation channels and spectra depend on the gauge representation and quantum numbers of the dark-matter candidate, as for a WIMP in SU(2)_L multiplets. These fix branching fractions to gamma rays and antimatter.", "map": "", "breaks": "", "confidence": "current research", "strength": 1}
{"id": "C0387", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history", "name": "Broken time translation and energy in an expanding universe", "kind": "mechanism", "summary": "FLRW has no timelike Killing vector, so total energy is not conserved. Radiation redshifts as a⁻⁴ and the cosmological constant does work, though local ∇_μT^{μν}=0 persists.", "map": "\\dot\\rho+3H(\\rho+p)=0", "breaks": "Only the global energy notion fails; local covariant conservation holds.", "confidence": "established", "strength": 2}
{"id": "C0388", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "name": "Solar oscillations as normal modes", "kind": "analogy", "summary": "Helioseismic p-modes are standing waves of the solar cavity, described by spherical-harmonic eigenfunctions. Frequencies invert to give the sound-speed profile, as in a spectral problem for an oscillator.", "map": "", "breaks": "The Sun is a non-ideal, rotating, convective cavity, so modes are damped and stochastically excited, and rotation splits the degenerate m levels.", "confidence": "established", "strength": 1}
{"id": "C0389", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Inflaton as an order parameter", "kind": "analogy", "summary": "A scalar field rolling in a potential mirrors the order parameter of a symmetry-breaking transition. The same potential structure underlies Higgs-like phase transitions, topological defects and old/new inflation.", "map": "V(\\phi)=\\tfrac{\\lambda}{4}(\\phi^2-v^2)^2", "breaks": "Inflation requires slow roll on a flat plateau, which is not generic for SSB potentials, and the inflaton has no established particle identity.", "confidence": "current research", "strength": 2}
{"id": "C0390", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "name": "Homology and mass–luminosity scaling", "kind": "method transfer", "summary": "Dimensional and homology arguments give stellar scalings such as L∝M³ for radiative stars and the Eddington luminosity, together with the Chandrasekhar mass from fundamental constants.", "map": "M_{\\rm Ch}\\sim\\left(\\frac{\\hbar c}{G}\\right)^{3/2}\\frac{1}{m_p^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0391", "a": "00-foundations/units-and-constants/fundamental-constants", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "Constraints on varying constants from the CMB", "kind": "shared object", "summary": "A different fine-structure constant or electron mass at recombination shifts the recombination epoch and alters peak positions. Planck data and quasar absorption spectra bound such variation.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0392", "a": "00-foundations/units-and-constants/natural-units-and-planck-scale", "b": "09-astrophysics-and-cosmology/cosmology/dark-energy", "name": "Cosmological constant problem across Planck scales", "kind": "shared object", "summary": "Planck-unit estimates of the vacuum energy exceed the observed dark-energy density by about 120 orders of magnitude. The mismatch is the sharpest naturalness problem.", "map": "\\rho_\\Lambda\\sim10^{-123}\\,\\rho_{\\rm Pl}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0782", "a": "01-classical-mechanics/analytical-mechanics/canonical-transformations-and-hamilton-jacobi", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics", "name": "Action-angle variables and Delaunay elements", "kind": "method transfer", "summary": "Hamilton–Jacobi theory yields Delaunay and Poincaré action-angle variables, the basis of canonical perturbation theory, averaging and Hamiltonian maps for planetary dynamics.", "map": "L=\\sqrt{GMa},\\; G=L\\sqrt{1-e^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0783", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "09-astrophysics-and-cosmology/dark-matter/astrophysical-evidence-for-dark-matter", "name": "Collisionless Boltzmann equation from Liouville", "kind": "identity", "summary": "Liouville's theorem gives the collisionless Boltzmann equation, which underlies Jeans equations and mass estimates from stellar and galaxy dynamics, including rotation curves and velocity dispersions.", "map": "\\frac{df}{dt}=\\partial_t f+\\mathbf v\\cdot\\nabla f-\\nabla\\Phi\\cdot\\partial_{\\mathbf v}f=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0784", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure", "name": "Phase-space density constraints on halos", "kind": "mechanism", "summary": "Liouville conservation of coarse-grained phase-space density limits how dense a halo core can be, giving Tremaine–Gunn bounds on warm and fermionic dark matter.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0785", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics", "name": "Symplectic integrators for long-term orbits", "kind": "method transfer", "summary": "Liouville's theorem and symplectic structure motivate Wisdom–Holman integrators that preserve phase-space volume and bound energy error over Gyr integrations.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0786", "a": "01-classical-mechanics/analytical-mechanics/lagrangian-mechanics", "b": "09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history", "name": "Newtonian cosmology and minisuperspace action", "kind": "analogy", "summary": "Friedmann equations follow from Newtonian energy conservation of a test shell, and from a minisuperspace Lagrangian in the scale factor.", "map": "\\dot a^2/a^2=\\tfrac{8\\pi G}{3}\\rho-\\tfrac{k}{a^2}\\;\\leftrightarrow\\; \\tfrac12 v^2-\\tfrac{GM}{r}=E", "breaks": "Pressure gravitates and k is geometry in GR; the Newtonian derivation lacks this and fails for radiation and dark energy without ad hoc input.", "confidence": "established", "strength": 2}
{"id": "C0787", "a": "01-classical-mechanics/analytical-mechanics/lagrangian-mechanics", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Scalar field as particle in a potential", "kind": "analogy", "summary": "Inflaton dynamics map to a particle rolling in a potential with Hubble friction; slow roll is the overdamped limit.", "map": "\\ddot\\phi+3H\\dot\\phi+V'(\\phi)=0", "breaks": "Fluctuations are quantum fields on curved space; the point-particle picture misses perturbation generation.", "confidence": "established", "strength": 2}
{"id": "C0788", "a": "01-classical-mechanics/analytical-mechanics/lagrangian-mechanics", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/binary-stars-and-stellar-populations", "name": "Roche potential in mass transfer", "kind": "shared object", "summary": "The restricted three-body effective potential in a rotating frame defines Roche lobes and the L1 point, governing mass transfer and contact binaries.", "map": "\\Phi_R=-\\frac{GM_1}{r_1}-\\frac{GM_2}{r_2}-\\tfrac12\\Omega^2 \\varpi^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0789", "a": "01-classical-mechanics/analytical-mechanics/variational-principles", "b": "09-astrophysics-and-cosmology/cosmology/gravitational-lensing", "name": "Fermat's principle in gravitational lensing", "kind": "identity", "summary": "Lensing images are stationary points of the time-delay surface (geometric plus Shapiro delay), giving the lens equation and time-delay cosmography.", "map": "t(\\theta)=\\frac{D_\\Delta}{c}\\left[\\tfrac12(\\theta-\\beta)^2-\\psi(\\theta)\\right]", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0790", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "09-astrophysics-and-cosmology/galaxies/active-galactic-nuclei-and-supermassive-black-holes", "name": "Accretion flows as viscous fluid dynamics", "kind": "shared object", "summary": "Accretion disks around black holes are viscous shear flows, and Bondi accretion is a spherical ideal-flow solution, as in the Navier–Stokes and Euler problems.", "map": "\\dot M=4\\pi\\lambda\\rho_\\infty (GM)^2/c_s^3", "breaks": "Angular momentum transport needs MHD turbulence (MRI), not molecular viscosity, and relativity matters near the hole.", "confidence": "established", "strength": 2}
{"id": "C0791", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/gamma-ray-bursts", "name": "Shock and blast-wave hydrodynamics", "kind": "method transfer", "summary": "Sedov–Taylor and Blandford–McKee blast waves are self-similar solutions of the Euler equations, applied to GRB afterglows, supernova remnants and the shocks that accelerate cosmic rays.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0792", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao", "name": "Jeans instability and structure growth", "kind": "mechanism", "summary": "Gravitational collapse of perturbations is the Jeans instability of a self-gravitating fluid, the fluid-mechanics seed of the growth of cosmic structure, modified by expansion drag.", "map": "\\ddot\\delta+2H\\dot\\delta=4\\pi G\\rho\\,\\delta", "breaks": "Dark matter is collisionless, so a fluid description holds only approximately, and nonlinear collapse needs N-body treatment.", "confidence": "established", "strength": 3}
{"id": "C0793", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "name": "Convection in stellar interiors", "kind": "shared object", "summary": "Rayleigh–Bénard-type instability sets the Schwarzschild criterion for convection in stars, handled with mixing-length theory.", "map": "\\nabla_{\\rm rad}>\\nabla_{\\rm ad}", "breaks": "Stellar convection is highly turbulent, compressible and stratified, at huge Rayleigh numbers beyond lab regimes.", "confidence": "established", "strength": 2}
{"id": "C0794", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks", "name": "Dust-gas drag in disks and Stokes drag", "kind": "mechanism", "summary": "Small dust grains in protoplanetary disks couple to gas through Stokes or Epstein drag, setting stopping times and radial drift; the same viscous-drag physics governs low-Re flow.", "map": "t_s=\\frac{m v}{F_{\\rm drag}},\\; F=6\\pi\\mu a v", "breaks": "Disk gas is often rarefied (Epstein regime, mean free path > grain size), unlike continuum Stokes flow.", "confidence": "established", "strength": 2}
{"id": "C0795", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks", "name": "Disk turbulence and angular momentum transport", "kind": "mechanism", "summary": "Turbulent viscosity (alpha prescription) drives accretion in protoplanetary disks and concentrates dust in vortices and eddies, controlling planetesimal formation.", "map": "\\nu=\\alpha c_s H", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0796", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/binary-stars-and-stellar-populations", "name": "Turbulent fragmentation and the IMF", "kind": "mechanism", "summary": "Supersonic turbulence in molecular clouds, with a Kolmogorov-like cascade, shapes the density distribution and fragmentation, and thus the stellar initial mass function.", "map": "", "breaks": "Gravity, magnetic fields and feedback also matter; whether turbulence alone sets the IMF is debated.", "confidence": "current research", "strength": 2}
{"id": "C0797", "a": "01-classical-mechanics/newtonian-mechanics/central-forces-and-orbits", "b": "09-astrophysics-and-cosmology/dark-matter/alternatives-mond-and-modified-gravity", "name": "MOND modifies Newtonian dynamics", "kind": "analogy", "summary": "MOND modifies the Newtonian force law below an acceleration scale, reproducing flat rotation curves and the Tully–Fisher relation without dark matter.", "map": "\\mu(a/a_0)\\,a=g_N,\\; v^4=GMa_0", "breaks": "Fails to account for cluster masses and CMB peaks without extra components, and needs a relativistic completion.", "confidence": "current research", "strength": 2}
{"id": "C0798", "a": "01-classical-mechanics/newtonian-mechanics/central-forces-and-orbits", "b": "09-astrophysics-and-cosmology/dark-matter/astrophysical-evidence-for-dark-matter", "name": "Rotation curves from Newtonian orbits", "kind": "method transfer", "summary": "Circular-orbit balance gives velocity profiles; flat curves at large radius imply M(<r) growing linearly with r, which signals dark matter.", "map": "v^2=\\frac{GM(<r)}{r}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0799", "a": "01-classical-mechanics/newtonian-mechanics/central-forces-and-orbits", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics", "name": "Kepler orbits and precession in the Solar System", "kind": "shared object", "summary": "Kepler problem, effective potential and perturbed-orbit precession underlie planetary and small-body orbits; secular perturbations produce apsidal and nodal precession.", "map": "U_{\\rm eff}=\\frac{L^2}{2mr^2}-\\frac{GMm}{r}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0800", "a": "01-classical-mechanics/newtonian-mechanics/conservation-laws", "b": "09-astrophysics-and-cosmology/galaxies/galaxy-clusters", "name": "Cluster collisions and conserved quantities", "kind": "shared object", "summary": "Merging clusters (e.g. Bullet Cluster) are analysed with momentum and energy conservation and collision kinematics, constraining collisionless dark matter versus shocked gas.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0801", "a": "01-classical-mechanics/newtonian-mechanics/conservation-laws", "b": "09-astrophysics-and-cosmology/galaxies/galaxy-clusters", "name": "Virial theorem and cluster mass", "kind": "method transfer", "summary": "Energy and momentum conservation lead to the virial theorem, used to estimate cluster dynamical masses from galaxy velocity dispersions (Zwicky's missing mass).", "map": "2\\langle T\\rangle+\\langle U\\rangle=0,\\; M\\sim \\frac{\\sigma^2 R}{G}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0802", "a": "01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets", "name": "Planetary systems as few-body problems", "kind": "shared object", "summary": "Planetary system architecture, stability and resonances are treated with the N-body problem, perturbation theory and numerical integration.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0803", "a": "01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-detection", "name": "Lagrange points and Trojans in exoplanet systems", "kind": "shared object", "summary": "Restricted three-body equilibria define Trojan configurations and co-orbital planets, searched for in exoplanet timing and transit data.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C0804", "a": "01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-detection", "name": "Timing and RV signals from N-body dynamics", "kind": "method transfer", "summary": "Transit-timing variations and radial-velocity multi-planet fits are inverse N-body problems; mean-motion resonances amplify TTVs, allowing masses to be inferred from perturbations.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0805", "a": "01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics", "name": "Resonances and N-body Solar System evolution", "kind": "method transfer", "summary": "Mean-motion and secular resonances, symplectic N-body integrators and perturbation theory are the working tools of Solar System dynamics.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0806", "a": "01-classical-mechanics/newtonian-mechanics/non-inertial-frames", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-atmospheres", "name": "Coriolis force and atmospheric circulation", "kind": "mechanism", "summary": "Rotating-frame dynamics sets hot-Jupiter and terrestrial jet and wave structure, via Rossby numbers and geostrophic balance.", "map": "\\mathrm{Ro}=\\frac{U}{fL}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0807", "a": "01-classical-mechanics/newtonian-mechanics/non-inertial-frames", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics", "name": "Tides and Coriolis in planetary systems", "kind": "mechanism", "summary": "Tidal forces from non-inertial frame analysis drive tidal locking, orbital migration and Roche limits; Coriolis force shapes planetary atmospheres and rotating-frame Hill dynamics.", "map": "F_{\\rm tide}\\sim \\frac{2GMm\\,r}{d^3}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0808", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/binary-stars-and-stellar-populations", "name": "Chaos in N-body stellar dynamics", "kind": "mechanism", "summary": "Exponential sensitivity in few-body encounters and cluster dynamics limits N-body predictability, so ensembles are used for population synthesis.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C0809", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos", "b": "09-astrophysics-and-cosmology/galaxies/the-milky-way", "name": "Orbits and resonances in the Galactic potential", "kind": "method transfer", "summary": "Action-angle methods and resonance structure describe stellar orbits in barred potentials; bar resonances produce moving groups and phase-space features seen in Gaia.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0810", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics", "name": "KAM tori and chaos in planetary stability", "kind": "mechanism", "summary": "Long-term stability of planetary orbits is a KAM question: resonance overlap produces chaotic zones, Kirkwood gaps and Lyapunov times of order millions of years for the Solar System.", "map": "\\text{resonance overlap: } \\Delta\\omega_{\\rm res}\\gtrsim \\delta\\omega_{\\rm spacing}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0811", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "b": "09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure", "name": "Fuzzy dark matter solitons", "kind": "shared object", "summary": "Ultralight scalar dark matter obeys a Schrödinger–Poisson system whose ground state is a stable soliton core in halos, tied to nonlinear Schrödinger structure.", "map": "i\\hbar\\partial_t\\psi=-\\frac{\\hbar^2}{2m}\\nabla^2\\psi+m\\Phi\\psi", "breaks": "Poisson coupling is nonlocal, so the system is not integrable like the cubic NLS and solitons are not exact.", "confidence": "current research", "strength": 2}
{"id": "C0812", "a": "01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "Driven damped oscillator and acoustic peaks", "kind": "identity", "summary": "Photon-baryon plasma modes obey a forced, damped oscillator equation, with gravity driving, baryon loading shifting the zero point, and Silk damping suppressing high multipoles.", "map": "\\ddot\\Theta+\\frac{\\dot c_s^2}{}\\,k^2\\Theta=F(\\Phi)", "breaks": "Damping is from photon diffusion at finite mean free path, not a simple friction term; the system is also relativistic.", "confidence": "established", "strength": 3}
{"id": "C0813", "a": "01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "name": "Normal modes of the Sun", "kind": "shared object", "summary": "Solar p-modes and g-modes are the normal modes of a stratified self-gravitating sphere, and helioseismology inverts mode frequencies to infer interior structure.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0814", "a": "01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics", "b": "09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao", "name": "Baryon acoustic oscillations as sound waves", "kind": "mechanism", "summary": "BAO are sound waves in the pre-recombination plasma that froze at the drag epoch, leaving a standard ruler equal to the sound horizon.", "map": "r_s=\\int_0^{t_d}\\frac{c_s\\,dt}{a}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0815", "a": "01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Parametric resonance in preheating", "kind": "mechanism", "summary": "After inflation, the oscillating inflaton drives daughter fields through Mathieu-equation parametric resonance, producing explosive particle production.", "map": "\\ddot\\chi_k+\\left[k^2+g^2\\Phi^2\\sin^2(mt)\\right]\\chi_k=0", "breaks": "Backreaction and rescattering end the resonance, so the linear Mathieu analysis fails when occupation grows.", "confidence": "established", "strength": 2}
{"id": "C0816", "a": "01-classical-mechanics/rigid-body-dynamics/euler-equations-and-tops", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics", "name": "Spin-orbit dynamics and chaotic tumbling", "kind": "mechanism", "summary": "Intermediate-axis instability and spin-orbit coupling give chaotic rotation of irregular moons such as Hyperion, and spin-orbit resonances like Mercury's 3:2.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0817", "a": "01-classical-mechanics/rigid-body-dynamics/euler-equations-and-tops", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Rigid rotation, free precession and pulsars", "kind": "mechanism", "summary": "Euler's equations for torque-free bodies describe free precession of neutron stars, and rotational dynamics governs pulsar spin-down and glitches, though the superfluid interior complicates a rigid-body model.", "map": "", "breaks": "Neutron stars have superfluid interiors and elastic crusts, so a single rigid body fails.", "confidence": "current research", "strength": 2}
{"id": "C0818", "a": "01-classical-mechanics/rigid-body-dynamics/gyroscopes-and-precession", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/astrobiology-and-habitability", "name": "Axial precession and obliquity climate cycles", "kind": "mechanism", "summary": "Torque-driven precession and obliquity variations (Milankovitch cycles) modulate insolation; obliquity stability, enforced by a large moon, affects habitability.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1177", "a": "02-electromagnetism-and-optics/classical-optics/coherence-and-statistical-optics", "b": "09-astrophysics-and-cosmology/galaxies/active-galactic-nuclei-and-supermassive-black-holes", "name": "VLBI and EHT as van Cittert–Zernike imaging", "kind": "method transfer", "summary": "Radio interferometry measures visibilities that are Fourier components of source brightness, per van Cittert–Zernike; the EHT imaged the M87 and Sgr A* shadows from sparse coverage.", "map": "V(u,v)=\\iint I(l,m)e^{-2\\pi i(ul+vm)}\\,dl\\,dm", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1178", "a": "02-electromagnetism-and-optics/classical-optics/coherence-and-statistical-optics", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-detection", "name": "Interferometry and direct imaging of exoplanets", "kind": "method transfer", "summary": "Van Cittert–Zernike coherence underlies interferometric imaging and nulling, while coronagraphs use diffraction control and apodization to suppress starlight for direct imaging.", "map": "\\gamma_{12}\\propto\\mathcal{F}[I(\\mathbf{s})]", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1179", "a": "02-electromagnetism-and-optics/classical-optics/coherence-and-statistical-optics", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "name": "Hanbury Brown–Twiss stellar intensity interferometry", "kind": "historical", "summary": "Intensity correlations measured by Hanbury Brown and Twiss gave stellar angular diameters, founding photon-statistics optics and being revived with Cherenkov telescope arrays.", "map": "g^{(2)}(\\tau)=1+|g^{(1)}(\\tau)|^2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1180", "a": "02-electromagnetism-and-optics/classical-optics/fourier-optics-and-imaging", "b": "09-astrophysics-and-cosmology/galaxies/the-milky-way", "name": "Diffraction limit and adaptive optics at the Galactic Centre", "kind": "method transfer", "summary": "Telescope resolution is set by the diffraction limit, and adaptive optics corrects atmospheric phase errors to track stellar orbits around Sgr A*.", "map": "\\theta\\approx1.22\\lambda/D", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1181", "a": "02-electromagnetism-and-optics/classical-optics/geometric-optics", "b": "09-astrophysics-and-cosmology/cosmology/gravitational-lensing", "name": "Lensing as geometric optics in curved spacetime", "kind": "analogy", "summary": "Light follows null geodesics, equivalent to rays in a medium with effective refractive index n = 1 − 2Φ/c²; the lens equation and Fermat's principle mirror thin-lens optics.", "map": "n=1-\\frac{2\\Phi}{c^2},\\quad \\delta t=\\tfrac{1}{2}|\\theta-\\beta|^2-\\psi", "breaks": "Lenses have no focal point (the deflection is not linear in impact parameter), and the lens is an extended mass whose profile fixes the images; strong-field lensing leaves the geometric-optics limit.", "confidence": "established", "strength": 3}
{"id": "C1182", "a": "02-electromagnetism-and-optics/classical-optics/geometric-optics", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients", "name": "Telescope optics and survey instruments", "kind": "method transfer", "summary": "Aberration theory and wide-field optical design set the imaging performance of survey telescopes like ZTF and Rubin used for transient discovery.", "map": "\\theta\\approx1.22\\lambda/D", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1183", "a": "02-electromagnetism-and-optics/classical-optics/interference-and-diffraction", "b": "09-astrophysics-and-cosmology/cosmology/gravitational-lensing", "name": "Wave optics of lensing and fringes", "kind": "analogy", "summary": "Lensing of coherent waves (FRBs, gravitational waves) shows interference between images, and diffraction from point lenses gives fringes when wavelength approaches the Schwarzschild radius, as in Fresnel optics.", "map": "F(w)=\\frac{1}{\\pi}\\int d^2x\\,e^{i w T(x,y)}", "breaks": "Geometric optics is recovered only for w much greater than 1; strong dependence on lens profile and no analogue of aberration-free focusing.", "confidence": "current research", "strength": 2}
{"id": "C1184", "a": "02-electromagnetism-and-optics/classical-optics/polarization-and-crystal-optics", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "Stokes parameters and E/B polarization", "kind": "method transfer", "summary": "CMB polarization is described with Stokes Q and U, decomposed into curl-free E and divergence-free B modes, a spin-2 field analogous to optical polarization states.", "map": "Q\\pm iU=\\sum a_{\\pm2,\\ell m}\\,{}_{\\pm2}Y_{\\ell m}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1185", "a": "02-electromagnetism-and-optics/classical-optics/polarization-and-crystal-optics", "b": "09-astrophysics-and-cosmology/galaxies/active-galactic-nuclei-and-supermassive-black-holes", "name": "Faraday rotation and polarimetry of jets", "kind": "mechanism", "summary": "Birefringence of magnetized plasma rotates linear polarization as λ², letting radio polarimetry measure magnetic fields in jets, the Galaxy and intergalactic gas.", "map": "\\chi=\\chi_0+\\mathrm{RM}\\,\\lambda^2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1186", "a": "02-electromagnetism-and-optics/classical-optics/polarization-and-crystal-optics", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/fast-radio-bursts-and-magnetars", "name": "FRB dispersion and Faraday rotation as plasma probes", "kind": "mechanism", "summary": "Plasma refractive index gives frequency-dependent delay (dispersion measure) and Faraday rotation, which together weigh intergalactic baryons and magnetic fields along FRB sightlines.", "map": "t\\propto \\mathrm{DM}\\,\\nu^{-2},\\quad n^2=1-\\omega_p^2/\\omega^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1187", "a": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/fast-radio-bursts-and-magnetars", "name": "Wave propagation in cold plasma", "kind": "identity", "summary": "The cold-plasma dispersion relation of EM waves, with cutoff at the plasma frequency, gives FRB pulse delay and scattering broadening by turbulent plasma.", "map": "\\omega^2=\\omega_p^2+c^2k^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1188", "a": "02-electromagnetism-and-optics/electrodynamics/maxwells-equations", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "name": "Solar magnetic fields and MHD", "kind": "mechanism", "summary": "Maxwell's equations with induction and Ampère's law in the low-frequency limit give magnetohydrodynamics for solar fields, flux freezing and reconnection driving flares.", "map": "\\partial_t\\mathbf{B}=\\nabla\\times(\\mathbf{v}\\times\\mathbf{B})+\\eta\\nabla^2\\mathbf{B}", "breaks": "Displacement current is dropped and ideal conductivity assumed; reconnection requires non-ideal terms.", "confidence": "established", "strength": 2}
{"id": "C1189", "a": "02-electromagnetism-and-optics/electrodynamics/relativistic-electrodynamics", "b": "09-astrophysics-and-cosmology/galaxies/active-galactic-nuclei-and-supermassive-black-holes", "name": "Relativistic beaming and Doppler boosting", "kind": "mechanism", "summary": "Lorentz transformations of fields and radiation give aberration and Doppler boosting of jet emission, explaining superluminal motion and blazar brightness.", "map": "\\delta=\\frac{1}{\\Gamma(1-\\beta\\cos\\theta)},\\quad S_\\nu\\propto\\delta^{3+\\alpha}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1190", "a": "02-electromagnetism-and-optics/photonics-and-lasers/integrated-and-fiber-photonics", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-detection", "name": "Laser frequency combs for radial velocity", "kind": "method transfer", "summary": "Laser frequency combs and microresonator Kerr combs give precise wavelength calibration for spectrographs, targeting cm/s radial-velocity precision needed for Earth-like planets.", "map": "f_n=n f_{rep}+f_{ceo}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1191", "a": "02-electromagnetism-and-optics/photonics-and-lasers/laser-physics", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/binary-stars-and-stellar-populations", "name": "Astrophysical masers and lasers", "kind": "mechanism", "summary": "Population inversion and stimulated emission occur naturally as masers in star-forming regions and evolved-star envelopes, with narrow bright lines used for distances and kinematics.", "map": "I_\\nu\\propto e^{|\\tau_\\nu|},\\ \\tau_\\nu<0", "breaks": "Masers lack an optical cavity and are single-pass amplifiers, with no mode selection or coherence like a laser.", "confidence": "established", "strength": 2}
{"id": "C1192", "a": "02-electromagnetism-and-optics/radiation-and-scattering", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle", "name": "Radiation processes power high-energy sources", "kind": "shared object", "summary": "Synchrotron, bremsstrahlung and inverse-Compton emission from relativistic charges, derived from Liénard–Wiechert fields, underlie GRBs, AGN jets, cosmic-ray signatures and FRBs.", "map": "P=\\frac{2}{3}\\frac{q^2 \\gamma^4 a_\\perp^2}{4\\pi\\epsilon_0 c^3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1193", "a": "02-electromagnetism-and-optics/radiation-and-scattering/cherenkov-and-transition-radiation", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "name": "Air-Cherenkov detection of cosmic rays", "kind": "method transfer", "summary": "Cherenkov light from air showers triggered by cosmic rays and gamma rays is imaged by IACTs such as H.E.S.S. and CTA, reconstructing primary energy and direction.", "map": "\\theta_c\\approx\\sqrt{2(n-1)}\\sim1^\\circ", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1194", "a": "02-electromagnetism-and-optics/radiation-and-scattering/cherenkov-and-transition-radiation", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/neutrino-astronomy", "name": "Cherenkov light detects neutrinos", "kind": "method transfer", "summary": "IceCube and KM3NeT detect Cherenkov light from relativistic charged secondaries of neutrino interactions in ice and water, using the cos θ = 1/(nβ) cone to reconstruct direction.", "map": "\\cos\\theta_c=\\frac{1}{n\\beta}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1195", "a": "02-electromagnetism-and-optics/radiation-and-scattering/cherenkov-and-transition-radiation", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/neutrino-astronomy", "name": "Neutrino telescopes rely on the Cherenkov effect", "kind": "shared object", "summary": "The Frank–Tamm photon yield and the refractive-index dispersion of ice and seawater set the light output and detector response of neutrino telescopes.", "map": "\\frac{dN}{dx\\,d\\lambda}=\\frac{2\\pi\\alpha}{\\lambda^2}\\left(1-\\frac{1}{n^2\\beta^2}\\right)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1196", "a": "02-electromagnetism-and-optics/radiation-and-scattering/dipole-radiation-and-antennas", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Pulsar spin-down as magnetic dipole radiation", "kind": "identity", "summary": "A rotating magnetic dipole radiates at the rotation frequency, giving the braking index n=3 and characteristic age estimates for pulsars.", "map": "\\dot\\Omega=-K\\Omega^3", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1197", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "09-astrophysics-and-cosmology/galaxies/active-galactic-nuclei-and-supermassive-black-holes", "name": "Synchrotron emission from AGN jets", "kind": "shared object", "summary": "Relativistic electrons spiraling in jet magnetic fields emit beamed synchrotron radiation, giving power-law spectra, high polarization and Doppler boosting in blazars.", "map": "\\nu_c\\propto\\gamma^2 B,\\quad P\\propto\\gamma^2 B^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1198", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/gamma-ray-bursts", "name": "Synchrotron afterglow and fireball emission", "kind": "mechanism", "summary": "GRB afterglows are synchrotron emission from shock-accelerated electrons in a decelerating relativistic blast wave, with broken power-law spectra whose breaks map to electron energy and magnetic field.", "map": "\\nu_m\\propto\\gamma_m^2 B\\Gamma", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1199", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Pulsar and magnetar radiation", "kind": "mechanism", "summary": "Pulsar magnetic-dipole braking uses the dipole radiation formula, and coherent curvature and synchrotron emission from magnetospheric particles produce radio and gamma-ray pulses.", "map": "P=\\frac{\\mu_0 B^2R^6\\Omega^4\\sin^2\\alpha}{6\\pi c^3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1200", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients", "name": "Synchrotron in supernova remnants", "kind": "shared object", "summary": "Radio and X-ray synchrotron emission from electrons accelerated at remnant shocks reveals magnetic field amplification and particle acceleration, linking to cosmic-ray origin.", "map": "P\\propto\\gamma^2B^2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1201", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "Photon–baryon tight coupling via Thomson", "kind": "mechanism", "summary": "Thomson scattering couples photons to baryons before recombination, producing the acoustic oscillations; the visibility function and Silk damping follow from the scattering mean free path.", "map": "\\tau=\\int n_e\\sigma_T\\,c\\,dt", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1202", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "Thomson scattering polarizes the CMB", "kind": "mechanism", "summary": "Thomson scattering of anisotropic radiation by free electrons, with its dipole angular dependence, generates CMB linear polarization (E modes) at recombination and reionization.", "map": "\\frac{d\\sigma}{d\\Omega}=\\frac{3\\sigma_T}{8\\pi}|\\hat\\epsilon\\cdot\\hat\\epsilon'|^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1203", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "09-astrophysics-and-cosmology/galaxies/active-galactic-nuclei-and-supermassive-black-holes", "name": "Eddington limit and Compton coronae in AGN", "kind": "mechanism", "summary": "Thomson-limited radiation pressure caps accretion luminosity, and Comptonization of disk photons in hot coronae produces AGN X-ray power-law spectra.", "map": "L_{Edd}=\\frac{4\\pi G M m_p c}{\\sigma_T}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1204", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "09-astrophysics-and-cosmology/galaxies/galaxy-clusters", "name": "Sunyaev–Zel'dovich inverse-Compton scattering", "kind": "mechanism", "summary": "CMB photons Compton-scattered by hot intracluster electrons gain energy, distorting the blackbody spectrum; the Kompaneets treatment of Compton scattering yields the thermal SZ signal used to find clusters.", "map": "\\frac{\\Delta T}{T}=y\\left(x\\coth\\frac{x}{2}-4\\right),\\ y=\\int\\frac{k T_e}{m_ec^2}\\sigma_T n_e\\,dl", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1205", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "name": "Inverse Compton and synchrotron cooling of cosmic rays", "kind": "mechanism", "summary": "Relativistic electrons lose energy by synchrotron and inverse-Compton scattering on CMB and starlight, steepening spectra and producing TeV gamma rays, which limits the lifetime of cosmic-ray electrons.", "map": "\\dot E\\propto\\gamma^2\\left(U_B+U_{rad}\\right)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1206", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/gamma-ray-bursts", "name": "Compton scattering in relativistic outflows", "kind": "mechanism", "summary": "Inverse-Compton and Thomson scattering set photospheric opacity and high-energy afterglow components in GRB fireballs; the Thomson optical depth fixes the compactness constraint on Lorentz factors.", "map": "\\tau_T=n\\sigma_T R", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1207", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-atmospheres", "name": "Rayleigh and Mie scattering in exoplanet hazes", "kind": "mechanism", "summary": "Rayleigh slopes and Mie scattering by clouds and hazes shape transmission spectra, muting molecular features and giving blue-slope signatures, as for Earth's blue sky.", "map": "\\sigma_R\\propto\\lambda^{-4}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1208", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "name": "Electron-scattering opacity and Eddington limit", "kind": "mechanism", "summary": "Thomson scattering opacity sets radiation pressure in stellar interiors and the Eddington luminosity limiting massive stars and accretion.", "map": "L_{Edd}=\\frac{4\\pi G M m_p c}{\\sigma_T}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1510", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/laws-of-thermodynamics", "b": "09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history", "name": "First law in a comoving volume gives the fluid equation", "kind": "identity", "summary": "Applying dU=−p dV adiabatically to a comoving volume gives the cosmological continuity equation, so each component's equation of state w=p/ρ fixes ρ∝a^{-3(1+w)}. A cosmological constant (w=−1) keeps its density fixed as the volume grows; its negative pressure balances the energy books.", "map": "d(\\rho a^3)=-p\\,d(a^3)\\Rightarrow\\dot\\rho+3H(\\rho+p)=0,\\ \\rho\\propto a^{-3(1+w)}", "breaks": "", "confidence": "established", "strength": 2}