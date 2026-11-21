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

### High-redshift universe and reionization · `knowledge/09-astrophysics-and-cosmology/galaxies/high-redshift-universe-and-reionization`

**Scope.** Dark ages and cosmic dawn, Population III stars, Gunn–Peterson troughs in $z>6$ quasars, reionization history from CMB optical depth ($\tau\approx0.054$), Lyman-break and Lyman-α galaxies, JWST photometric and spectroscopic galaxies at $z>10$, UV luminosity functions, 21-cm experiments (EDGES claim, HERA, SKA), early black holes.

**Core ideas.**
- UV photons from the first galaxies reionized intergalactic hydrogen by $z\approx6$.
- Even a tiny neutral fraction absorbs Lyman-α completely — the Gunn–Peterson trough.
- JWST finds more bright early galaxies than many models predicted — tension with feedback or IMF assumptions, not (so far) with ΛCDM.

**Key equations.**
$$\tau_{GP}\approx1.8\times10^5\,h^{-1}\Omega_m^{-1/2}\frac{\Omega_bh^2}{0.02}\left(\frac{1+z}{7}\right)^{3/2}x_{\text{HI}},\qquad \lambda_{21}=21.1\ \text{cm}\ (1+z)$$

**See also.** [CMB](knowledge/09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background/README.md) · [Atomic structure (21-cm)](knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy/README.md)

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

# Packet 09-2 (100 records)

{"id": "C1511", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/laws-of-thermodynamics", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "name": "Virial thermostat: stars heat up as they lose energy", "kind": "mechanism", "summary": "For a star in hydrostatic equilibrium the virial theorem gives total energy E=−K, so radiating energy away makes it contract and heat up (Kelvin–Helmholtz contraction). The same negative heat capacity keeps nuclear burning self-regulating: excess energy expands and cools the core.", "map": "E=-K=\\tfrac12W,\\ t_{\\rm KH}\\sim\\frac{GM^2}{RL}\\approx3\\times10^7\\,{\\rm yr}\\ (\\odot)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1512", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/phase-equilibria-and-chemical-potential", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "Saha equation and cosmic recombination", "kind": "identity", "summary": "Chemical equilibrium μ_p+μ_e=μ_H between ideal gases gives the Saha equation. Photons outnumber baryons by 1/η≈1.6×10⁹, so hydrogen only recombines near k_BT≈0.3 eV, far below the 13.6 eV binding energy, and this sets the last-scattering surface.", "map": "\\frac{x_e^2}{1-x_e}=\\frac{1}{n_b}\\left(\\frac{m_ek_BT}{2\\pi\\hbar^2}\\right)^{3/2}e^{-B/k_BT}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1513", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/phase-equilibria-and-chemical-potential", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Metastable and coexisting phases as dark-matter detectors", "kind": "method transfer", "summary": "Bubble chambers such as PICO keep a fluorocarbon superheated, as a metastable liquid. A nuclear recoil that deposits enough energy inside the critical radius nucleates a bubble (Seitz theory), and the threshold is tuned so electron recoils do not. Dual-phase xenon TPCs run at liquid–vapour coexistence so that drifted electrons are pulled into the gas, where they produce the S2 signal.", "map": "r_c=\\frac{2\\sigma}{p_v-p_l},\\ W=\\frac{16\\pi\\sigma^3}{3(p_v-p_l)^2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1514", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/phase-equilibria-and-chemical-potential", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/astrobiology-and-habitability", "name": "Clausius–Clapeyron runaway greenhouse sets the HZ inner edge", "kind": "mechanism", "summary": "Water-vapour pressure rises exponentially with temperature, so warming adds more greenhouse gas. Once the atmosphere is mostly steam, outgoing thermal radiation saturates near 280 W m⁻² (the Simpson–Nakajima limit) and the oceans evaporate. This defines the inner edge of the habitable zone.", "map": "\\frac{d\\ln e_s}{dT}=\\frac{L_v}{R_vT^2},\\ {\\rm OLR}_{\\max}\\approx280\\,{\\rm W\\,m^{-2}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1515", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/phase-equilibria-and-chemical-potential", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-atmospheres", "name": "Condensation curves and equilibrium chemistry in exoplanets", "kind": "method transfer", "summary": "Clouds form where a species' partial pressure meets its Clausius–Clapeyron saturation curve along the atmosphere's pressure–temperature profile: silicate and iron clouds on hot giants, KCl and Na₂S on cooler ones. Baseline compositions come from minimizing the Gibbs free energy. JWST spectra are read as departures from that baseline caused by vertical quenching and photochemistry.", "map": "\\frac{d\\ln p_{\\rm sat}}{dT}=\\frac{L}{RT^2},\\ \\min_{\\{n_i\\}}G=\\sum_in_i\\mu_i", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1516", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/phase-equilibria-and-chemical-potential", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "White-dwarf crystallization and phase separation", "kind": "mechanism", "summary": "The core of a cooling white dwarf is a Coulomb plasma that freezes when the coupling Γ reaches about 175. Latent heat, plus oxygen sinking as the carbon–oxygen mixture phase-separates (a binary-mixture phase diagram), slows the cooling. Gaia sees this as a pile-up in the white-dwarf cooling sequence.", "map": "\\Gamma=\\frac{Z^2e^2}{a\\,k_BT}\\approx175\\ \\text{(Gaussian units)}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1517", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/thermodynamic-potentials-and-maxwell-relations", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "name": "Adiabatic gradient, Γ₁ and stellar stability", "kind": "identity", "summary": "Stellar stability criteria are thermodynamic response functions. Convection starts when the radiative gradient exceeds ∇_ad (Schwarzschild criterion), and partial ionization lowers both ∇_ad and Γ₁. A star is dynamically unstable if its pressure-weighted Γ₁ drops below 4/3, and helioseismology measures Γ₁ inside the Sun to test the equation of state.", "map": "\\nabla_{\\rm ad}=\\left(\\frac{\\partial\\ln T}{\\partial\\ln P}\\right)_S,\\ \\Gamma_1=\\left(\\frac{\\partial\\ln P}{\\partial\\ln\\rho}\\right)_S,\\ \\langle\\Gamma_1\\rangle>\\tfrac43", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1518", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/thermodynamic-potentials-and-maxwell-relations", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients", "name": "Γ₁<4/3 instabilities: core collapse and pair instability", "kind": "mechanism", "summary": "Some processes absorb energy without raising the pressure: iron photodisintegration and electron capture in collapsing cores, and electron–positron pair creation in very massive oxygen cores. They push Γ₁ below 4/3 and trigger collapse. Pair instability produces (pulsational) pair-instability supernovae and a predicted black-hole mass gap.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1519", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/percolation", "b": "09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao", "name": "Friends-of-friends halos and cosmic-web percolation", "kind": "method transfer", "summary": "The friends-of-friends halo finder links particles closer than b≈0.2 times the mean separation, so its halos are continuum-percolation clusters. Percolation statistics of over- and underdense regions were also an early quantitative test of the cosmic web's connected, filamentary topology.", "map": "\\ell_{\\rm link}=b\\,\\bar n^{-1/3},\\ b\\approx0.2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1520", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/percolation", "b": "09-astrophysics-and-cosmology/galaxies/high-redshift-universe-and-reionization", "name": "Reionization as percolation of ionized bubbles", "kind": "method transfer", "summary": "Ionized regions around early galaxies grow and merge until they form a spanning cluster. Simulations and upcoming 21-cm maps are interpreted by treating this overlap phase as a percolation transition, using cluster-size and topology statistics.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1521", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Degenerate-matter equation of state for compact stars", "kind": "mechanism", "summary": "Counting states of indistinguishable fermions in the grand-canonical ensemble gives a pressure that survives at T=0; this equation of state, with Sommerfeld finite-temperature and ionic heat-capacity corrections, sets white-dwarf structure and cooling ages.", "map": "P=-\\Omega/V,\\ \\Omega=-k_BT\\sum_k\\ln\\left(1+e^{-(\\epsilon_k-\\mu)/k_BT}\\right)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1522", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "b": "09-astrophysics-and-cosmology/galaxies/high-redshift-universe-and-reionization", "name": "21-cm spin temperature as a two-level Boltzmann ratio", "kind": "mechanism", "summary": "The populations of hydrogen's two hyperfine levels define a spin temperature through the Boltzmann factor. T_s is a weighted mean of the CMB, gas-kinetic and Lyman-α colour temperatures (Wouthuysen–Field coupling). The 21-cm signal appears in absorption when T_s is below T_CMB and in emission when it is above.", "map": "\\frac{n_1}{n_0}=3e^{-T_*/T_s},\\ T_*=0.068\\,{\\rm K},\\ \\delta T_b\\propto1-\\frac{T_\\gamma}{T_s}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1523", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/binary-stars-and-stellar-populations", "name": "Negative heat capacity and gravothermal catastrophe in clusters", "kind": "mechanism", "summary": "The virial theorem gives self-gravitating systems a negative heat capacity, which the canonical ensemble cannot represent (ensembles become inequivalent). A core that loses heat to its halo contracts and gets hotter, so isothermal spheres are unstable once the centre-to-edge density ratio exceeds 709. Globular clusters therefore undergo core collapse, which binary heating halts.", "map": "2K+W=0\\Rightarrow E=-K,\\ C=\\frac{dE}{dT}<0;\\ \\rho_c/\\rho_e>709", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1524", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information", "b": "09-astrophysics-and-cosmology/dark-matter/alternatives-mond-and-modified-gravity", "name": "Entropic/emergent gravity as a MOND-like alternative", "kind": "mechanism", "summary": "Verlinde proposed that gravity is an entropic force arising from information on holographic screens. He later proposed that de Sitter entropy adds an 'apparent dark matter' force that scales like MOND, with a₀~cH₀. The idea is speculative and contested.", "map": "", "breaks": "It has no accepted derivation from microphysics, and key steps assume Newton's law. Its galaxy-scale predictions are under strain from dwarf-galaxy, cluster and Solar System tests.", "confidence": "proposed", "strength": 1}
{"id": "C1525", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information", "b": "09-astrophysics-and-cosmology/galaxies/galaxy-formation-and-evolution", "name": "Lynden-Bell violent relaxation as maximum-entropy statistics", "kind": "analogy", "summary": "Lynden-Bell maximized the coarse-grained entropy of a collisionless system whose fine-grained phase-space density is conserved. That incompressibility acts like an exclusion principle and gives a Fermi–Dirac-like distribution. It explains why rapid collapse gives every star the same velocity dispersion regardless of mass.", "map": "\\bar f(\\epsilon)=\\frac{\\eta}{e^{\\beta(\\epsilon-\\mu)}+1}", "breaks": "Relaxation stops before it is complete as the potential settles. The predicted equilibria have infinite mass, and simulated (NFW-like) halos do not follow Lynden-Bell's distribution.", "confidence": "established", "strength": 2}
{"id": "C1526", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "CMB as a Bose–Einstein photon gas", "kind": "identity", "summary": "The CMB is the most precisely measured Planck spectrum (FIRAS, T0=2.7255 K). Expansion redshifts frequency and temperature together, so the Bose–Einstein form survives. Late energy release would leave a chemical-potential (μ) distortion, now bounded at |μ|<9×10⁻⁵.", "map": "n(\\nu)=\\frac{1}{e^{h\\nu/k_BT+\\mu}-1},\\quad T\\propto a^{-1}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1527", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history", "name": "Thermal history: g_*, entropy conservation, relic neutrinos", "kind": "identity", "summary": "In the radiation era the universe is a quantum ideal gas of relativistic species. Energy and entropy densities count boson degrees of freedom, with fermions weighted by 7/8, and comoving entropy is conserved. Electron–positron annihilation heats photons but not the already decoupled neutrinos, giving T_ν/T_γ=(4/11)^{1/3} and N_eff≈3.044.", "map": "\\rho=\\frac{\\pi^2}{30}g_*T^4,\\ s=\\frac{2\\pi^2}{45}g_{*s}T^3,\\ sa^3={\\rm const}\\Rightarrow\\frac{T_\\nu}{T_\\gamma}=\\left(\\frac{4}{11}\\right)^{1/3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1528", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure", "name": "Fuzzy dark matter as a degenerate Bose field", "kind": "mechanism", "summary": "Ultralight bosons (m~10⁻²² eV) have such large occupation numbers that they behave as a classical wave obeying the Schrödinger–Poisson equations. Their kiloparsec de Broglie wavelengths form solitonic, condensate-like cores, and gravitational relaxation can condense Bose stars. Claims that all axion dark matter forms one coherent BEC are disputed.", "map": "\\frac{\\lambda_{\\rm dB}}{2\\pi}=\\frac{\\hbar}{mv}\\approx1.9\\,{\\rm kpc}\\,\\frac{10^{-22}\\,{\\rm eV}}{mc^2}\\,\\frac{10\\,{\\rm km\\,s^{-1}}}{v}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1529", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Fermi degeneracy pressure and the Chandrasekhar limit", "kind": "identity", "summary": "Electron degeneracy pressure P∝n^{5/3} softens to P∝n^{4/3} once electrons are relativistic. An n=3 polytrope then has a single allowed mass, the Chandrasekhar limit. The same Fermi-gas physics for neutrons, plus nuclear forces, sets the maximum mass of neutron stars.", "map": "P\\propto n^{4/3}\\Rightarrow M_{\\rm Ch}\\simeq\\frac{3.10}{(\\mu_e m_u)^2}\\left(\\frac{\\hbar c}{G}\\right)^{3/2}\\approx\\frac{5.8}{\\mu_e^2}M_\\odot", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1530", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "name": "Degenerate cores and the helium flash", "kind": "mechanism", "summary": "In low-mass red giants the helium core is electron-degenerate, so its pressure barely depends on temperature. When helium ignites, the core heats without expanding, which defeats the virial thermostat, and the runaway helium flash continues until degeneracy is lifted. At the other extreme, blackbody radiation pressure dominates in massive stars.", "map": "P_e\\propto\\rho^{5/3}\\ (T\\text{-independent}),\\ P_{\\rm rad}=\\tfrac13aT^4", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1531", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/driven-systems-and-nonequilibrium-steady-states", "b": "09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao", "name": "Adhesion model: Zel'dovich flow as Burgers/KPZ", "kind": "identity", "summary": "Adding a small viscosity to the Zel'dovich approximation gives the Burgers equation for the comoving velocity, which a Cole–Hopf transform linearizes. Written for the velocity potential it is the noiseless KPZ equation, and its shocks reproduce the sheets, filaments and nodes of the cosmic web.", "map": "\\partial_D\\mathbf u+(\\mathbf u\\cdot\\nabla)\\mathbf u=\\nu\\nabla^2\\mathbf u,\\ \\mathbf u=-\\nabla h:\\ \\partial_Dh=\\tfrac12|\\nabla h|^2+\\nu\\nabla^2h", "breaks": "The viscosity is artificial. Matter sticks inside shocks, so there is no shell crossing or virialization within halos, and the randomness comes from initial conditions rather than from KPZ's noise.", "confidence": "established", "strength": 2}
{"id": "C1532", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/driven-systems-and-nonequilibrium-steady-states", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "name": "Solar flares as self-organized-criticality avalanches", "kind": "analogy", "summary": "Flare energies follow a power law across many decades. Lu and Hamilton modelled the coronal magnetic field as a slowly driven sandpile whose reconnection avalanches reproduce that distribution, which made flares a leading astrophysical example of self-organized criticality.", "map": "", "breaks": "Waiting-time statistics show memory and clustering that simple SOC does not predict, and the power-law index varies. A power law alone does not prove criticality, and the underlying physics is MHD reconnection.", "confidence": "current research", "strength": 2}
{"id": "C1533", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "Boltzmann hierarchy, Silk damping, non-equilibrium recombination", "kind": "method transfer", "summary": "CMB anisotropies come from solving the linearized photon Boltzmann equation with a Thomson collision term (the multipole hierarchy in CAMB/CLASS). The photons' finite mean free path lets the photon–baryon fluid diffuse, which erases the small-scale peaks (Silk damping). Peebles' rate equation shows that recombination lags behind Saha equilibrium.", "map": "\\frac{df_\\gamma}{d\\eta}=C[f_\\gamma],\\ \\lambda_D\\sim\\sqrt{\\lambda_{\\rm mfp}\\,c\\,t}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1534", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure", "name": "SIDM halos as a conducting gas, then gravothermal collapse", "kind": "mechanism", "summary": "With σ/m~1 cm² g⁻¹, dark-matter self-scattering conducts heat like a dilute gas. It first builds an isothermal core, which addresses the cusp–core problem. Because the core has negative heat capacity, it can then undergo gravothermal collapse as globular clusters do, a process now invoked for unusually dense subhalos.", "map": "\\lambda_{\\rm mfp}=\\frac{1}{\\rho\\,(\\sigma/m)}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1535", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "09-astrophysics-and-cosmology/dark-matter/indirect-detection", "name": "Thermal freeze-out sets the relic annihilation cross-section", "kind": "mechanism", "summary": "Integrating the Boltzmann equation over momenta gives a rate equation for the dark-matter number density. Annihilations freeze out once n⟨σv⟩ falls below H, at m/T≈20–25. Matching the observed Ω_DM fixes the 'thermal' ⟨σv⟩≈3×10⁻²⁶ cm³ s⁻¹ that gamma-ray searches in dwarf galaxies aim to test.", "map": "\\dot n+3Hn=-\\langle\\sigma v\\rangle(n^2-n_{\\rm eq}^2),\\ \\Omega h^2\\approx\\frac{3\\times10^{-27}\\,{\\rm cm^3\\,s^{-1}}}{\\langle\\sigma v\\rangle}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1536", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "09-astrophysics-and-cosmology/galaxies/the-milky-way", "name": "Collisionless Boltzmann and Jeans equations for the Galaxy", "kind": "method transfer", "summary": "Two-body relaxation times are far longer than the Galaxy's age, so stars obey the collisionless Boltzmann (Vlasov) equation. Its velocity moments, the Jeans equations, turn Gaia kinematics into a measurement of the local dark-matter density. The Gaia phase spiral is a collisionless system caught partway through phase mixing.", "map": "\\partial_tf+\\mathbf v\\cdot\\nabla f-\\nabla\\Phi\\cdot\\partial_{\\mathbf v}f=0,\\ t_{\\rm relax}\\approx\\frac{N}{8\\ln N}t_{\\rm cross}", "breaks": "There is no collision term and so no H-theorem: the system relaxes by phase mixing and violent relaxation, not toward a Maxwellian.", "confidence": "established", "strength": 3}
{"id": "C1537", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients", "name": "Neutrino trapping and diffusion in core collapse", "kind": "mechanism", "summary": "Above about 10¹² g cm⁻³ the neutrino mean free path (∝E_ν⁻²) is far smaller than the core, so neutrinos are trapped. They leak out by diffusion from a neutrinosphere over about 10 s, with nearly Fermi–Dirac spectra. Supernova simulations solve the Boltzmann transport equation for them, and the ~13 s neutrino burst from SN 1987A confirmed the timescale.", "map": "t_{\\rm diff}\\sim\\frac{R^2}{\\lambda_\\nu c},\\ \\lambda_\\nu\\propto\\rho^{-1}E_\\nu^{-2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1538", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "name": "Gamow peak: Maxwellian tail times tunnelling", "kind": "mechanism", "summary": "A thermonuclear rate is the Maxwell–Boltzmann distribution multiplied by the Coulomb-tunnelling probability. The product peaks at the Gamow energy, about 6 keV for the pp reaction in the solar core where k_BT≈1.35 keV. The resulting steep temperature dependence, for example a ⁸B neutrino flux ∝T_c^{~24}, makes solar neutrinos a sensitive thermometer of the core.", "map": "\\langle\\sigma v\\rangle\\propto\\int S(E)\\,e^{-E/k_BT-\\sqrt{E_G/E}}\\,dE,\\ E_0=\\left(\\tfrac14E_G(k_BT)^2\\right)^{1/3}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1539", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Stochastic inflation: inflaton Langevin dynamics", "kind": "method transfer", "summary": "Averaged over a Hubble patch, the inflaton gets a random kick of size H/2π per e-fold from modes crossing the horizon. It therefore obeys a Langevin equation, and its probability distribution a Fokker–Planck equation. This underlies eternal inflation and the first-passage (stochastic-δN) predictions of non-Gaussian tails that matter for primordial black holes.", "map": "\\frac{d\\phi}{dN}=-\\frac{V'}{3H^2}+\\frac{H}{2\\pi}\\xi(N),\\ P_{\\rm eq}\\propto e^{-8\\pi^2V/3H^4}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1540", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao", "name": "Excursion sets: halo mass function as first passage", "kind": "method transfer", "summary": "Smoothing the linear density field on ever smaller scales makes δ perform a random walk in the variance S=σ²(M). The halo mass function is the distribution of first crossings of the collapse barrier δ_c≈1.686, which reproduces Press–Schechter including its ad hoc factor of 2.", "map": "f(S)\\,dS=\\frac{\\delta_c}{\\sqrt{2\\pi}}S^{-3/2}e^{-\\delta_c^2/2S}\\,dS", "breaks": "The walk is Markovian only for a sharp-k filter. Realistic filters and ellipsoidal collapse need non-Markovian corrections and moving barriers.", "confidence": "established", "strength": 3}
{"id": "C1541", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "09-astrophysics-and-cosmology/galaxies/galaxy-clusters", "name": "Kompaneets equation and the Sunyaev–Zel'dovich effect", "kind": "identity", "summary": "Repeated Compton scattering off Maxwellian electrons makes photons diffuse in frequency according to a Fokker–Planck equation, the Kompaneets equation. Its n² stimulated-emission term makes the steady state a Bose–Einstein distribution. In hot cluster gas it shifts CMB photons to higher frequency, producing the thermal SZ y-distortion used to find clusters.", "map": "\\frac{\\partial n}{\\partial y}=\\frac{1}{x^2}\\frac{\\partial}{\\partial x}\\left[x^4\\left(\\frac{\\partial n}{\\partial x}+n+n^2\\right)\\right],\\ y=\\int\\frac{k_BT_e}{m_ec^2}n_e\\sigma_T\\,dl", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1542", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "name": "Diffusive shock acceleration as a random walk with escape", "kind": "mechanism", "summary": "Charged particles scattered by magnetic turbulence random-walk back and forth across a shock. Each crossing cycle gives a fixed fractional energy gain, and each cycle carries a fixed probability of escaping downstream. The competition produces a power law, E⁻² for a strong shock; energy-dependent diffusion through the Galaxy then steepens it to the observed ~E⁻²·⁷.", "map": "\\frac{dN}{dE}\\propto E^{-(r+2)/(r-1)}\\to E^{-2}\\ (r=4)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1543", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks", "name": "Dust coagulation: Smoluchowski kinetics and Brownian growth", "kind": "method transfer", "summary": "Grain growth in protoplanetary disks is modelled with the Smoluchowski coagulation equation. Collision kernels come from Brownian motion for small grains and from turbulence and drift for larger ones. Gas drag in the Epstein (kinetic) regime sets the stopping time and Stokes number, which control settling, radial drift and the bouncing and fragmentation barriers.", "map": "t_s=\\frac{\\rho_sa}{\\rho_gv_{\\rm th}},\\ \\Delta v_{\\rm BM}=\\sqrt{\\frac{8k_BT(m_1+m_2)}{\\pi m_1m_2}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1544", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/binary-stars-and-stellar-populations", "name": "Fokker–Planck stellar dynamics: relaxation, friction, evaporation", "kind": "method transfer", "summary": "Chandrasekhar treated the cumulative effect of weak stellar encounters as Brownian motion: a Fokker–Planck equation with a drag term (dynamical friction) and a velocity-diffusion term. In star clusters this drives mass segregation and the evaporation of stars scattered above the escape speed, about 0.7% of a Maxwellian per relaxation time.", "map": "\\frac{d\\mathbf v_M}{dt}=-\\frac{4\\pi G^2M\\rho\\ln\\Lambda}{v_M^3}\\left[{\\rm erf}X-\\frac{2X}{\\sqrt\\pi}e^{-X^2}\\right]\\mathbf v_M", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1545", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "name": "Radiative diffusion as a photon random walk", "kind": "mechanism", "summary": "Inside a star a photon travels only up to about a centimetre before it is scattered or absorbed, so energy moves by diffusion. Fick's law with a Rosseland-mean opacity gives the radiative temperature gradient. Escaping the solar core takes 10⁴–10⁵ yr, compared with R/c≈2 s for a straight path.", "map": "F=-\\frac{4acT^3}{3\\kappa\\rho}\\frac{dT}{dr},\\ t_{\\rm diff}\\sim\\frac{R^2}{\\lambda c}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1546", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "name": "Stochastically excited p-modes as noise-driven oscillators", "kind": "mechanism", "summary": "Solar acoustic modes are damped and also driven by random forcing from convection near the surface. Each behaves like a Langevin oscillator whose power spectrum is a Lorentzian with a linewidth set by the damping rate. This model is the basis of mode fitting in helioseismology and in asteroseismology of solar-like stars.", "map": "\\ddot x+2\\eta\\dot x+\\omega_0^2x=f(t)\\Rightarrow P(\\omega)\\propto\\frac{1}{(\\omega-\\omega_0)^2+\\eta^2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1547", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/critical-exponents-and-universality", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Kibble–Zurek defect formation and the monopole problem", "kind": "mechanism", "summary": "When a symmetry breaks, causally disconnected regions pick independent vacua, leaving at least one defect per correlation volume; Zurek fixed the frozen correlation length using critical exponents. GUT monopoles made this way would overclose the universe, a key motivation for inflation. The scaling has been tested in superfluid helium, liquid crystals and cold atoms.", "map": "\\hat\\xi\\sim\\xi_0\\left(\\frac{\\tau_Q}{\\tau_0}\\right)^{\\nu/(1+z\\nu)}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1548", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Old inflation as a supercooled first-order transition", "kind": "historical", "summary": "Guth's inflation began as supercooling of a GUT phase transition. A Landau-type finite-temperature potential with a metastable false vacuum drives exponential expansion, which bubble nucleation was meant to end. The bubbles never percolate, so 'new' slow-roll inflation replaced the scenario.", "map": "V(\\phi,T)=D(T^2-T_0^2)\\phi^2-ET\\phi^3+\\tfrac{\\lambda}{4}\\phi^4", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1549", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/renormalization-group", "b": "09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao", "name": "Effective field theory of large-scale structure", "kind": "method transfer", "summary": "Integrating out the non-linear short-scale modes leaves an effective fluid. Its stress tensor has cutoff-dependent coefficients, such as the sound speed c_s², fixed by matching, exactly as in Wilsonian renormalization. Renormalized and time-RG perturbation theories resum loops to push predictions to mildly non-linear scales.", "map": "P_{\\rm EFT}(k)=P_{\\rm lin}+P_{1\\text{-loop}}-2c_s^2k^2P_{\\rm lin}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1826", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "b": "09-astrophysics-and-cosmology/cosmology/dark-energy", "name": "Atom interferometry constrains screened dark energy", "kind": "method transfer", "summary": "Atoms in a high vacuum are unscreened test masses; interferometers near a source mass bound chameleon-type dark-energy forces.", "map": "a_{\\rm cham}\\ \\text{bounded at}\\ \\sim10^{-6}g", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1827", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "b": "09-astrophysics-and-cosmology/dark-matter", "name": "Clock networks as dark-matter detectors", "kind": "method transfer", "summary": "Networks of atomic clocks and magnetometers could detect transient frequency shifts from passing topological-defect dark matter, or oscillations from ultralight fields.", "map": "\\delta\\nu/\\nu\\propto\\phi^2/\\Lambda^2\\ \\text{during defect crossing}", "breaks": "", "confidence": "proposed", "strength": 2}
{"id": "C1828", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-detection", "name": "Astrocombs calibrate radial-velocity planet searches", "kind": "method transfer", "summary": "Optical frequency combs, developed for clock metrology, give spectrographs absolute, evenly spaced calibration lines for cm/s radial-velocity precision needed for Earth analogues.", "map": "\\nu_n=n f_{\\rm rep}+f_{\\rm ceo};\\ K_\\oplus\\approx0.09\\ \\mathrm{m/s}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1829", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "09-astrophysics-and-cosmology/cosmology", "name": "Quasar absorption tests of varying alpha", "kind": "method transfer", "summary": "Relative wavelengths of metal absorption lines in quasar spectra, with laboratory sensitivity coefficients, constrain cosmic variation of the fine-structure constant; reported variations remain contested.", "map": "\\omega_z=\\omega_0+q\\left[\\left(\\frac{\\alpha_z}{\\alpha_0}\\right)^2-1\\right]", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1830", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "Hydrogen atomic physics sets recombination", "kind": "mechanism", "summary": "Recombination is delayed beyond Saha equilibrium because Lyman-alpha photons are trapped; the 2s-1s two-photon decay and Lyman-alpha redshifting control the last-scattering surface and thus the CMB acoustic scale.", "map": "\\frac{dx_e}{dt}=-C\\left[\\alpha_Bnx_e^2-\\beta_B(1-x_e)e^{-h\\nu_\\alpha/k_BT}\\right],\\ C=\\frac{\\Lambda_{2s1s}+\\Lambda_\\alpha}{\\Lambda_{2s1s}+\\Lambda_\\alpha+\\beta_B}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1831", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "09-astrophysics-and-cosmology/dark-matter/astrophysical-evidence-for-dark-matter", "name": "21-cm rotation curves trace dark halos", "kind": "method transfer", "summary": "Neutral-hydrogen 21-cm emission extends rotation curves far beyond stellar disks, where flat curves give the cleanest galactic evidence for dark matter.", "map": "v_c^2=GM(<r)/r=\\text{const}\\Rightarrow M\\propto r", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1832", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "09-astrophysics-and-cosmology/galaxies/galaxy-clusters", "name": "Highly charged ion spectroscopy of cluster gas", "kind": "method transfer", "summary": "X-ray lines of He- and H-like iron give temperature, abundance and turbulent velocity of intracluster gas; Hitomi's resolved Fe XXV lines measured low turbulence in Perseus.", "map": "\\sigma_v^2=\\sigma_{\\rm th}^2+\\sigma_{\\rm turb}^2,\\ \\sigma_{\\rm th}=\\sqrt{k_BT/m_{\\rm Fe}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1833", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "09-astrophysics-and-cosmology/galaxies/high-redshift-universe-and-reionization", "name": "21-cm hyperfine line and Lyman-alpha probe reionization", "kind": "method transfer", "summary": "The hydrogen hyperfine transition, its spin temperature set by collisions and Lyman-alpha pumping (Wouthuysen-Field), maps neutral gas at cosmic dawn; Gunn-Peterson Lyman-alpha absorption marks the end of reionization.", "map": "\\nu_{21}=1420.405\\ \\mathrm{MHz};\\ \\delta T_b\\propto x_{\\rm HI}\\left(1-\\frac{T_{\\rm CMB}}{T_S}\\right)\\sqrt{1+z}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1834", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/multi-messenger-astronomy", "name": "Lanthanide atomic data for kilonova spectra", "kind": "method transfer", "summary": "Kilonova light curves and spectra depend on the dense line forests of lanthanides and on identified features such as Sr II, requiring atomic-structure calculations of open f-shell ions.", "map": "", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1835", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-atmospheres", "name": "Line lists for exoplanet atmosphere spectra", "kind": "method transfer", "summary": "Interpreting transmission and emission spectra needs ro-vibrational line lists of H2O, CH4, CO2 and metal atoms computed from molecular quantum mechanics.", "map": "\\delta(\\lambda)\\approx\\frac{R_p^2+2R_pN_HH}{R_\\star^2},\\ \\sigma(\\lambda)\\ \\text{from line lists}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1836", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "name": "Atomic opacities and the solar abundance problem", "kind": "method transfer", "summary": "Stellar interiors depend on computed atomic opacities; measured iron opacity at solar-interior conditions exceeds theory, a candidate resolution of the mismatch between helioseismology and low solar metal abundances.", "map": "\\nabla_{\\rm rad}=\\frac{3\\kappa LP}{16\\pi acGMT^4}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1837", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure", "name": "Fuzzy dark matter as a cosmic matter wave", "kind": "analogy", "summary": "Ultralight bosonic dark matter obeys the Schrodinger-Poisson system, a Gross-Pitaevskii equation with self-gravity; galaxy halos develop solitonic cores and granular interference like condensates.", "map": "i\\hbar\\partial_t\\psi=-\\frac{\\hbar^2}{2m}\\nabla^2\\psi+m\\Phi\\psi,\\ \\nabla^2\\Phi=4\\pi Gm|\\psi|^2", "breaks": "Interaction is long-range self-gravity rather than contact scattering; occupation is classical and not reached by thermal condensation; no trap or superfluid flow measurement.", "confidence": "current research", "strength": 3}
{"id": "C1838", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Fermi pressure from trapped atoms to white dwarfs", "kind": "mechanism", "summary": "Degeneracy pressure measured in trapped Fermi gases is the same Pauli effect that supports white dwarfs and neutron stars against gravity.", "map": "P=\\frac{(3\\pi^2)^{2/3}\\hbar^2}{5m}n^{5/3}\\ \\text{(non-relativistic)}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1839", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Superfluid vortices and pulsar glitches", "kind": "mechanism", "summary": "Neutron-star interiors are superfluid; rotation is carried by quantized vortices whose sudden unpinning from the crust is the leading explanation of pulsar glitches, the physics of vortex lattices in rotating BECs.", "map": "\\oint\\mathbf v_s\\cdot d\\mathbf l=\\frac{h}{2m_n};\\ n_v=\\frac{4m_n\\Omega}{h}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1840", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/ultracold-molecules", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks", "name": "Cold molecular collisions and astrochemistry", "kind": "mechanism", "summary": "Interstellar chemistry at 10-100 K proceeds by barrierless ion-molecule reactions and tunnelling, the same low-temperature collision physics that cold-molecule experiments resolve state by state.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1841", "a": "04-quantum-physics/foundations-of-quantum-mechanics/bell-nonlocality", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Cosmological Bell inequalities", "kind": "method transfer", "summary": "Bell-type observables built from primordial correlators could in principle reveal the quantum origin of structure, though decaying modes make realistic tests extremely hard.", "map": "", "breaks": "", "confidence": "proposed", "strength": 1}
{"id": "C1842", "a": "04-quantum-physics/foundations-of-quantum-mechanics/bell-nonlocality", "b": "09-astrophysics-and-cosmology/galaxies/active-galactic-nuclei-and-supermassive-black-holes", "name": "Quasars choose settings in cosmic Bell tests", "kind": "method transfer", "summary": "Light from high-redshift quasars emitted billions of years ago set measurement bases in a Bell test, pushing any freedom-of-choice loophole back to the early universe.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1843", "a": "04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Quantum-to-classical transition of cosmic fluctuations", "kind": "mechanism", "summary": "Large squeezing makes primordial fluctuations effectively classical stochastic fields, and environmental decoherence selects field amplitude as pointer basis; whether a quantum signature survives is debated.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1844", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/lindblad-master-equations", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "Density-matrix kinetics of relic neutrinos", "kind": "method transfer", "summary": "Neutrino decoupling with oscillations and collisions is computed with matrix-valued quantum kinetic equations, giving N_eff = 3.044 used in CMB fits.", "map": "\\dot\\rho_p=-i[H_p,\\rho_p]+C[\\rho]", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1845", "a": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients", "name": "Many-body entanglement in collective neutrino oscillations", "kind": "method transfer", "summary": "Neutrino-neutrino forward scattering in supernovae makes flavour evolution an interacting spin model; quantum-information tools quantify entanglement beyond mean-field treatments.", "map": "H=\\sum_p\\omega_p\\mathbf B\\cdot\\mathbf J_p+\\frac{\\mu}{N}\\sum_{p,q}(1-\\cos\\theta_{pq})\\mathbf J_p\\cdot\\mathbf J_q", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1846", "a": "04-quantum-physics/quantum-mechanics-core/approximation-methods", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "name": "WKB asymptotics of solar oscillations", "kind": "method transfer", "summary": "High-order p-mode frequencies follow from JWKB analysis of the wave equation in the solar cavity, giving the large-separation formula used to invert sound speed.", "map": "\\nu_{n\\ell}\\approx\\Delta\\nu\\left(n+\\frac\\ell2+\\epsilon\\right),\\ \\Delta\\nu=\\left(2\\int_0^R\\frac{dr}{c_s}\\right)^{-1}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1847", "a": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Bounce instantons and false-vacuum decay", "kind": "method transfer", "summary": "The Euclidean bounce that computes tunnelling rates in quantum mechanics gives bubble nucleation in field theory and gravity, central to old and eternal inflation and vacuum stability.", "map": "\\Gamma/V\\approx Ae^{-B/\\hbar},\\ B=S_E[\\phi_{\\rm bounce}]-S_E[\\phi_{\\rm fv}]", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1848", "a": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "b": "09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure", "name": "Partial-wave cross sections of self-interacting dark matter", "kind": "method transfer", "summary": "Velocity-dependent self-interaction cross sections for Yukawa potentials are computed by partial-wave and Born methods; resonant and classical regimes control halo cores.", "map": "\\sigma_T=\\frac{4\\pi}{k^2}\\sum_\\ell(\\ell+1)\\sin^2(\\delta_{\\ell+1}-\\delta_\\ell)", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1849", "a": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "b": "09-astrophysics-and-cosmology/dark-matter/indirect-detection", "name": "Sommerfeld enhancement of dark-matter annihilation", "kind": "mechanism", "summary": "Slow dark-matter particles exchanging a light mediator have enhanced annihilation, the wavefunction-at-origin factor of Coulomb or Yukawa scattering, with resonances from near-threshold bound states.", "map": "S=\\frac{\\pi\\alpha/v}{1-e^{-\\pi\\alpha/v}}\\ (\\text{Coulomb})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1850", "a": "04-quantum-physics/quantum-optics/cavity-optomechanics", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Mechanical quantum sensors for dark matter", "kind": "method transfer", "summary": "Levitated and clamped mechanical sensors operated near the quantum limit can detect impulses or oscillating forces from heavy or ultralight dark matter.", "map": "", "breaks": "", "confidence": "proposed", "strength": 2}
{"id": "C1851", "a": "04-quantum-physics/quantum-optics/quantized-light-and-photon-statistics", "b": "09-astrophysics-and-cosmology/cosmology/dark-energy", "name": "Zero-point energy and the cosmological-constant problem", "kind": "shared object", "summary": "Summing field-mode zero-point energies to a high cutoff predicts a vacuum energy far above the observed dark-energy density; the Casimir effect does not settle the issue because it measures energy differences.", "map": "\\rho_{\\rm vac}\\sim\\int^{\\Lambda}\\frac{d^3k}{(2\\pi)^3}\\frac{\\hbar\\omega_k}{2}\\sim\\frac{\\Lambda^4}{16\\pi^2}\\gg\\rho_\\Lambda\\approx(2.24\\ \\mathrm{meV})^4", "breaks": "Casimir forces arise from charge fluctuations and do not measure absolute vacuum energy; renormalization makes the naive cutoff estimate unphysical.", "confidence": "established", "strength": 2}
{"id": "C1852", "a": "04-quantum-physics/quantum-optics/quantized-light-and-photon-statistics", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "name": "Intensity interferometry from stars to quantum optics", "kind": "historical", "summary": "Hanbury Brown and Twiss measured stellar diameters from intensity correlations; explaining the photon bunching behind the effect led Glauber to the quantum theory of optical coherence.", "map": "g^{(2)}(\\tau)=1+|g^{(1)}(\\tau)|^2\\ \\text{(thermal light)}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1853", "a": "04-quantum-physics/quantum-optics/single-photon-sources-and-detectors", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Superconducting photon sensors for sub-GeV dark matter", "kind": "method transfer", "summary": "SNSPDs and transition-edge sensors developed for single-photon counting have meV thresholds, letting them detect electron recoils or absorption from light dark matter.", "map": "E_{\\rm th}\\sim\\mathrm{meV};\\ m_\\chi\\gtrsim\\mathrm{keV}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1854", "a": "04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Primordial perturbations are squeezed states", "kind": "identity", "summary": "Inflation stretches vacuum fluctuations into extremely squeezed two-mode states of opposite-momentum modes; the growing mode's phase coherence underlies CMB acoustic peaks.", "map": "|\\psi_k\\rangle=\\frac{1}{\\cosh r_k}\\sum_n(-e^{2i\\phi_k}\\tanh r_k)^n|n_{\\mathbf k},n_{-\\mathbf k}\\rangle,\\ r_k\\sim\\ln(aH/k)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2045", "a": "05-relativity-and-gravitation/black-holes", "b": "09-astrophysics-and-cosmology/galaxies/active-galactic-nuclei-and-supermassive-black-holes", "name": "Spinning black holes power AGN jets", "kind": "mechanism", "summary": "AGN engines are accreting Kerr black holes (Lynden-Bell 1969). In the Blandford–Znajek process, an electromagnetic version of the Penrose process, magnetic field lines threading the frame-dragged horizon extract its rotational energy and launch relativistic jets.", "map": "P_{\\rm BZ}\\approx\\frac{\\kappa}{4\\pi c}\\Phi_B^2\\Omega_H^2,\\quad \\Omega_H=\\frac{ac}{r_+^2+a^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2046", "a": "05-relativity-and-gravitation/black-holes", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Stellar-mass black holes as end states of collapse", "kind": "shared object", "summary": "Above the maximum neutron-star mass (~2.2–2.3 M_sun) no pressure can halt collapse, so heavy stellar cores become Kerr black holes. X-ray binaries such as Cyg X-1 are where the GR geometry meets measured masses, spins inferred from the ISCO, and the lower mass gap at 2–5 M_sun.", "map": "M>M_{\\rm TOV}^{\\max}\\approx2.2\\,M_\\odot\\ \\Rightarrow\\ r_+=\\frac{GM}{c^2}\\left(1+\\sqrt{1-\\chi^2}\\right)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2047", "a": "05-relativity-and-gravitation/black-holes/black-hole-imaging-and-astrophysical-black-holes", "b": "09-astrophysics-and-cosmology/cosmology/gravitational-lensing", "name": "Black-hole shadow as extreme gravitational lensing", "kind": "identity", "summary": "The EHT ring is the strong-deflection limit of lensing. Rays with impact parameters near b_c=√27 GM/c² wind around the photon sphere, forming the shadow edge and nested photon subrings, each demagnified by ~e^{−π} in Schwarzschild. The same deflection law gives Einstein rings in the weak-field limit.", "map": "b_c=\\sqrt{27}\\,\\frac{GM}{c^2},\\quad \\hat\\alpha(b)\\to\\infty\\ \\text{as}\\ b\\to b_c^+", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2048", "a": "05-relativity-and-gravitation/black-holes/black-hole-imaging-and-astrophysical-black-holes", "b": "09-astrophysics-and-cosmology/galaxies", "name": "Black-hole demographics and host-galaxy scaling", "kind": "shared object", "summary": "Nearly every massive galaxy hosts a central black hole whose mass tracks its bulge, as in the M–σ relation. Black-hole masses from horizon-scale imaging and from stellar and gas dynamics calibrate these scaling relations, from Sgr A* to M87*.", "map": "M_\\bullet\\propto\\sigma^{\\sim4\\text{–}5}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2049", "a": "05-relativity-and-gravitation/black-holes/black-hole-imaging-and-astrophysical-black-holes", "b": "09-astrophysics-and-cosmology/galaxies/active-galactic-nuclei-and-supermassive-black-holes", "name": "M87*: horizon-scale image of an AGN engine", "kind": "shared object", "summary": "The EHT image of M87*, the core of a radio-loud AGN with a kiloparsec jet, shows a ~42 μas ring that matches the Kerr shadow of a 6.5×10⁹ M_sun black hole. GRMHD accretion and jet models are scored directly against the image and its polarisation.", "map": "\\theta_{\\rm sh}\\approx2\\sqrt{27}\\,\\frac{GM}{c^2D}\\approx40\\,\\mu{\\rm as}\\ (\\text{M87}^*)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2050", "a": "05-relativity-and-gravitation/black-holes/black-hole-imaging-and-astrophysical-black-holes", "b": "09-astrophysics-and-cosmology/galaxies/the-milky-way", "name": "Sgr A*: the Galactic Centre black hole", "kind": "shared object", "summary": "Decades of S-star orbits weigh Sgr A* at ~4×10⁶ M_sun, and in 2022 the EHT imaged it as a ~52 μas ring consistent with a Kerr shadow. The two methods give independent mass-to-distance ratios, and they agree.", "map": "\\theta_{\\rm sh}\\approx2\\sqrt{27}\\,\\frac{GM}{c^2D}\\approx50\\,\\mu{\\rm as}\\ (\\text{Sgr A}^*)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2051", "a": "05-relativity-and-gravitation/black-holes/black-hole-thermodynamics-and-hawking-radiation", "b": "09-astrophysics-and-cosmology/cosmology/dark-energy", "name": "de Sitter horizon thermodynamics", "kind": "identity", "summary": "In a Λ-dominated universe each observer has a cosmological event horizon with the Gibbons–Hawking temperature ħH/(2πk_B) and an area entropy, obeying the same laws as black-hole horizons. For our H₀ this gives T~10⁻³⁰ K and S~10¹²² k_B, the maximum entropy of the observable universe.", "map": "T_{\\rm dS}=\\frac{\\hbar H}{2\\pi k_B},\\quad S_{\\rm dS}=\\frac{k_BA}{4\\ell_P^2}=\\frac{\\pi k_Bc^5}{G\\hbar H^2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2052", "a": "05-relativity-and-gravitation/black-holes/black-hole-thermodynamics-and-hawking-radiation", "b": "09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure", "name": "Hawking evaporation bounds primordial-black-hole DM", "kind": "mechanism", "summary": "Primordial black holes lighter than ~5×10¹¹ kg would have evaporated by today, and slightly heavier ones would still emit Hawking gamma rays and e±. Gamma-ray, 511 keV-line and CMB data therefore exclude PBHs as all of the dark matter below ~10¹⁴ kg, leaving the asteroid-mass window open.", "map": "T_H=\\frac{\\hbar c^3}{8\\pi GMk_B},\\quad \\tau\\sim\\frac{5120\\pi G^2M^3}{\\hbar c^4}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2053", "a": "05-relativity-and-gravitation/black-holes/schwarzschild-and-kerr-black-holes", "b": "09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure", "name": "Black-hole superradiance constrains ultralight bosons", "kind": "mechanism", "summary": "Bosons whose Compton wavelength is comparable to a Kerr black hole's size form gravitational 'atoms' that grow by superradiance while ω<mΩ_H, draining the hole's spin. Measured spins of stellar and supermassive black holes exclude some ultralight-boson mass ranges, and the clouds should emit monochromatic gravitational waves.", "map": "\\omega<m\\Omega_H,\\quad \\alpha=\\frac{GM\\mu}{\\hbar c}\\sim0.1\\text{–}1", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2054", "a": "05-relativity-and-gravitation/black-holes/schwarzschild-and-kerr-black-holes", "b": "09-astrophysics-and-cosmology/galaxies/active-galactic-nuclei-and-supermassive-black-holes", "name": "ISCO sets the radiative efficiency of accretion", "kind": "mechanism", "summary": "A thin accretion disk radiates the binding energy at the innermost stable circular orbit. Its efficiency η=1−E_ISCO rises from 5.7% for Schwarzschild (r=6GM/c²) to 42% for maximal prograde Kerr. Soltan's argument, comparing integrated quasar light with the relic SMBH mass density, uses η to infer typical spins.", "map": "\\eta=1-\\sqrt{1-\\frac{2GM}{3c^2r_{\\rm ISCO}}},\\quad r_{\\rm ISCO}\\in[1,6]\\,GM/c^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2055", "a": "05-relativity-and-gravitation/general-relativity", "b": "09-astrophysics-and-cosmology/cosmology", "name": "Cosmology is GR applied to the whole universe", "kind": "identity", "summary": "Modern cosmology is general relativity with a homogeneous, isotropic source. The Einstein equations with Λ and the FLRW ansatz give the Friedmann equations that ΛCDM fits to CMB, BAO and supernova data, so every cosmological test is also a large-scale test of GR.", "map": "G_{\\mu\\nu}+\\Lambda g_{\\mu\\nu}=\\frac{8\\pi G}{c^4}T_{\\mu\\nu}\\Rightarrow H^2=\\frac{8\\pi G}{3}\\rho-\\frac{kc^2}{a^2}+\\frac{\\Lambda c^2}{3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2056", "a": "05-relativity-and-gravitation/general-relativity", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "TOV equation and the neutron-star maximum mass", "kind": "identity", "summary": "Relativistic hydrostatic equilibrium, the Tolman–Oppenheimer–Volkoff equation from the Einstein equations with a perfect-fluid source, sets neutron-star structure. Because pressure itself gravitates, every equation of state has a maximum mass, and the Buchdahl bound caps compactness at 2GM/(Rc²) < 8/9.", "map": "\\frac{dP}{dr}=-\\frac{G(\\rho+P/c^2)(m+4\\pi r^3P/c^2)}{r^2(1-2Gm/rc^2)}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2057", "a": "05-relativity-and-gravitation/general-relativity/einstein-field-equations", "b": "09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao", "name": "Structure growth from linearised Einstein equations", "kind": "identity", "summary": "Cosmological perturbation theory is the Einstein equations linearised about FLRW. In Newtonian gauge the 00 component gives a Poisson equation for the Bardeen potential, and sub-horizon matter obeys a growth equation whose solution D(a) and growth rate f≈Ω_m^{0.55} are what BAO and RSD surveys measure.", "map": "\\ddot\\delta+2H\\dot\\delta=4\\pi G\\bar\\rho\\,\\delta,\\quad \\nabla^2\\Phi=4\\pi Ga^2\\bar\\rho\\,\\delta,\\quad f\\approx\\Omega_m^{0.55}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2058", "a": "05-relativity-and-gravitation/general-relativity/exact-solutions", "b": "09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history", "name": "FLRW metric: the exact solution behind expansion", "kind": "identity", "summary": "The Friedmann–Lemaître–Robertson–Walker metric is the exact solution for a homogeneous, isotropic universe, and de Sitter is its Λ-dominated limit. Its scale factor a(t) defines redshift, the distance measures and the expansion history H(z) that cosmology fits.", "map": "ds^2=-c^2dt^2+a(t)^2\\left[\\frac{dr^2}{1-kr^2}+r^2d\\Omega^2\\right],\\quad 1+z=\\frac{a_0}{a}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2059", "a": "05-relativity-and-gravitation/general-relativity/modified-gravity", "b": "09-astrophysics-and-cosmology/cosmology/dark-energy", "name": "Dark energy or modified gravity?", "kind": "shared object", "summary": "Cosmic acceleration can sit on the right side of Einstein's equations, as a dark-energy fluid with w≈−1, or on the left, as f(R), Horndeski or massive gravity. The two are degenerate in H(z) and are told apart by the growth of structure and lensing; any modification must also be screened to pass Solar-System tests.", "map": "G_{\\mu\\nu}=\\frac{8\\pi G}{c^4}(T_{\\mu\\nu}+T^{\\rm DE}_{\\mu\\nu})\\ \\leftrightarrow\\ G_{\\mu\\nu}+X_{\\mu\\nu}[g,\\phi]=\\frac{8\\pi G}{c^4}T_{\\mu\\nu}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2060", "a": "05-relativity-and-gravitation/general-relativity/modified-gravity", "b": "09-astrophysics-and-cosmology/cosmology/gravitational-lensing", "name": "Gravitational slip: lensing vs dynamics tests GR", "kind": "method transfer", "summary": "Light responds to Φ+Ψ, while galaxies and peculiar velocities respond to Ψ alone. GR without anisotropic stress requires Φ=Ψ, so combining weak lensing with redshift-space distortions (the E_G statistic, slip η, μ–Σ parametrisations) tests modified gravity on Mpc–Gpc scales.", "map": "\\eta\\equiv\\Phi/\\Psi=1\\ (\\text{GR}),\\quad \\text{lensing}\\propto\\nabla^2(\\Phi+\\Psi),\\ \\text{dynamics}\\propto\\nabla\\Psi", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2061", "a": "05-relativity-and-gravitation/general-relativity/modified-gravity", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Starobinsky R² inflation is f(R) gravity", "kind": "identity", "summary": "The action f(R)=R+R²/(6M²) is conformally equivalent to GR plus a scalar field with a plateau potential. It drives inflation with n_s≈1−2/N and r≈12/N², inside Planck's preferred region, so the earliest successful inflation model is a modified-gravity theory.", "map": "f(R)=R+\\frac{R^2}{6M^2}\\Leftrightarrow V(\\phi)=\\frac34M^2M_{\\rm Pl}^2\\left(1-e^{-\\sqrt{2/3}\\,\\phi/M_{\\rm Pl}}\\right)^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2062", "a": "05-relativity-and-gravitation/general-relativity/modified-gravity", "b": "09-astrophysics-and-cosmology/dark-matter/alternatives-mond-and-modified-gravity", "name": "MOND needs a relativistic modified-gravity completion", "kind": "mechanism", "summary": "MOND modifies Newtonian dynamics below a₀≈1.2×10⁻¹⁰ m s⁻². To predict lensing and the CMB it needs a relativistic completion such as TeVeS or AeST, which places it among scalar–vector–tensor modified-gravity theories. GW170817 falsified the original TeVeS, which had gravitons and photons travelling on different metrics.", "map": "g=\\sqrt{g_N a_0}\\ (g_N\\ll a_0)\\ \\Rightarrow\\ v_\\infty^4=GMa_0", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2063", "a": "05-relativity-and-gravitation/general-relativity/modified-gravity", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/multi-messenger-astronomy", "name": "GW170817's speed of gravity prunes dark-energy models", "kind": "method transfer", "summary": "The 1.7 s delay between GW170817 and GRB 170817A over ~40 Mpc fixes the speed of gravity to within ~10⁻¹⁵ of c. That eliminates the Horndeski and beyond-Horndeski dark-energy models whose tensor speed differs from c on cosmological backgrounds, including quartic and quintic galileons.", "map": "-3\\times10^{-15}<\\frac{c_g-c}{c}<7\\times10^{-16}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2064", "a": "05-relativity-and-gravitation/general-relativity/tests-of-general-relativity", "b": "09-astrophysics-and-cosmology/cosmology/gravitational-lensing", "name": "Light deflection: from 1919 eclipse to lensing", "kind": "identity", "summary": "The GR deflection angle 4GM/(c²b), twice the Newtonian value and weighted by the PPN factor (1+γ)/2, is the kernel of the lens equation. The 1919 eclipse test grew into Einstein rings, cosmic shear and time-delay cosmography, and comparing lensing with dynamics tests γ on galactic scales.", "map": "\\hat\\alpha=\\frac{1+\\gamma}{2}\\frac{4GM}{c^2b},\\quad \\boldsymbol\\beta=\\boldsymbol\\theta-\\frac{D_{ls}}{D_s}\\hat{\\boldsymbol\\alpha}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2065", "a": "05-relativity-and-gravitation/general-relativity/tests-of-general-relativity", "b": "09-astrophysics-and-cosmology/galaxies/the-milky-way", "name": "S2's orbit tests GR near Sgr A*", "kind": "method transfer", "summary": "Adaptive-optics astrometry and spectroscopy of the star S2 detected the combined gravitational redshift and transverse Doppler shift at its 2018 pericentre, and later the prograde Schwarzschild precession of its orbit. This carries tests of GR to the potential of a 4×10⁶ M_sun black hole.", "map": "\\Delta\\phi=\\frac{6\\pi GM}{c^2a(1-e^2)}\\approx12'\\ \\text{per orbit (S2)}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2066", "a": "05-relativity-and-gravitation/general-relativity/tests-of-general-relativity", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics", "name": "Solar-System ephemerides as tests of GR", "kind": "method transfer", "summary": "Mercury's anomalous 43″ per century perihelion advance was GR's first success. Modern planetary ephemerides, built from radar, spacecraft tracking and lunar laser ranging, must include 1PN terms, and their fits bound the PPN parameters β and γ to ~10⁻⁵ along with the Nordtvedt effect and Ġ/G.", "map": "\\Delta\\phi=\\frac{2+2\\gamma-\\beta}{3}\\,\\frac{6\\pi GM}{c^2a(1-e^2)}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2067", "a": "05-relativity-and-gravitation/general-relativity/tests-of-general-relativity", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Binary pulsars: strong-field GR laboratories", "kind": "shared object", "summary": "Pulsars in tight binaries, such as the Hulse–Taylor system and the Double Pulsar, yield post-Keplerian parameters: periastron advance, Shapiro delay and orbital decay. These test GR's quadrupole formula to better than 0.1% and weigh neutron stars, including the ~2 M_sun Shapiro-delay masses that constrain the equation of state.", "map": "\\dot P_b=-\\frac{192\\pi G^{5/3}}{5c^5}\\left(\\frac{P_b}{2\\pi}\\right)^{-5/3}\\frac{m_pm_c\\,f(e)}{(m_p+m_c)^{1/3}}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2068", "a": "05-relativity-and-gravitation/general-relativity/tests-of-general-relativity", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "name": "Solar oblateness and the perihelion test", "kind": "historical", "summary": "The Sun's quadrupole J₂ also advances Mercury's perihelion. Dicke and Goldenberg's 1967 oblateness claim (J₂~2.5×10⁻⁵) would have spoiled GR's 43″ and favoured Brans–Dicke theory. Helioseismic inversions of solar rotation later fixed J₂≈2.2×10⁻⁷, a negligible correction.", "map": "\\Delta\\phi_{J_2}=\\frac{3\\pi J_2R_\\odot^2}{a^2(1-e^2)^2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2069", "a": "05-relativity-and-gravitation/gravitational-waves", "b": "09-astrophysics-and-cosmology/cosmology/hubble-tension-and-cosmological-tensions", "name": "Standard sirens: H₀ without a distance ladder", "kind": "method transfer", "summary": "A compact-binary waveform gives the luminosity distance directly from its amplitude and chirp, with no distance-ladder calibration. With a host-galaxy redshift, GW170817 gave H₀=70^{+12}_{−8} km s⁻¹ Mpc⁻¹. Tens to hundreds of sirens could become an independent arbiter of the Hubble tension.", "map": "h\\propto\\frac{(G\\mathcal M_z)^{5/3}(\\pi f)^{2/3}}{c^4d_L},\\quad \\mathcal M_z=(1+z)\\mathcal M", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2070", "a": "05-relativity-and-gravitation/gravitational-waves", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle", "name": "Compact mergers as high-energy engines", "kind": "shared object", "summary": "The compact-object mergers that GW detectors see also produce short GRBs and kilonovae, and are candidate sources of neutrinos and cosmic rays. GW triggers therefore drive joint searches with gamma-ray, X-ray and neutrino observatories.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2071", "a": "05-relativity-and-gravitation/gravitational-waves", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/multi-messenger-astronomy", "name": "GW170817 opened GW multi-messenger astronomy", "kind": "shared object", "summary": "The binary-neutron-star merger GW170817 was followed 1.7 s later by GRB 170817A and then by a kilonova across the spectrum. This one event confirmed that neutron-star mergers make short GRBs and produce r-process elements.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2072", "a": "05-relativity-and-gravitation/gravitational-waves", "b": "09-astrophysics-and-cosmology/stellar-astrophysics", "name": "Pair-instability gap in the BH mass spectrum", "kind": "mechanism", "summary": "Stellar evolution predicts few black holes between ~50 and ~130 M_sun, because pair-instability supernovae disrupt helium cores in that range. GW catalogues test this prediction. GW190521's ~85 M_sun component lies inside the gap, pointing to hierarchical mergers or uncertain ¹²C(α,γ) rates.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2073", "a": "05-relativity-and-gravitation/gravitational-waves/gravitational-wave-theory-and-waveforms", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "Primordial gravitational waves and CMB B-modes", "kind": "mechanism", "summary": "Tensor perturbations, the gravitational waves from inflation, create a quadrupolar anisotropy at last scattering. Thomson scattering turns it into curl-type B-mode polarisation, which scalar modes cannot make at linear order. The tensor-to-scalar ratio is bounded to r<0.036, and lensing B-modes are the main foreground.", "map": "r=\\frac{P_t}{P_\\zeta},\\quad h_{ij}^{TT}\\to C_\\ell^{BB}\\propto r", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2074", "a": "05-relativity-and-gravitation/gravitational-waves/ground-based-detections", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/multi-messenger-astronomy", "name": "GW alerts and sky localisation for follow-up", "kind": "method transfer", "summary": "A three-detector LIGO–Virgo–KAGRA network triangulates a merger from arrival-time differences and issues low-latency alerts. GW170817's 28 deg² error region let optical telescopes find its kilonova in NGC 4993 within 11 hours.", "map": "\\Delta t_{ij}=\\frac{\\mathbf d_{ij}\\cdot\\hat{\\mathbf n}}{c}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2075", "a": "05-relativity-and-gravitation/gravitational-waves/ground-based-detections", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/binary-stars-and-stellar-populations", "name": "Binary-evolution channels behind GW mergers", "kind": "mechanism", "summary": "Isolated binary evolution (mass transfer, common envelope, supernova kicks) and dynamical assembly in clusters predict different merger rates, mass ratios and spin–orbit alignments. GW catalogues weigh these channels through rates and effective spins. The Peters inspiral time sets which binaries merge within a Hubble time.", "map": "t_{\\rm merge}=\\frac{5}{256}\\frac{c^5a^4}{G^3m_1m_2(m_1+m_2)}\\ (e=0)", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2076", "a": "05-relativity-and-gravitation/gravitational-waves/ground-based-detections", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Tidal deformability measures neutron-star radii", "kind": "method transfer", "summary": "In a neutron-star inspiral the tidal Love number enters the GW phase at 5PN order. GW170817 bounded the tidal deformability of a 1.4 M_sun star to Λ≲800, implying radii of ~11–13 km and ruling out the stiffest nuclear equations of state.", "map": "\\Lambda=\\frac23k_2\\left(\\frac{c^2R}{GM}\\right)^5,\\quad \\delta\\Psi_{\\rm tidal}\\propto\\tilde\\Lambda\\,(v/c)^{5}\\ \\text{rel. to 0PN}", "breaks": "", "confidence": "established", "strength": 3}