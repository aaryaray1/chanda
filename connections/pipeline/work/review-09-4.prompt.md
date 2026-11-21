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

# Packet 09-4 (100 records)

{"id": "C2532", "a": "07-nuclear-physics/nuclear-structure/exotic-nuclei-and-drip-lines", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Nuclear masses fix the outer-crust composition", "kind": "shared object", "summary": "The outer-crust sequence of nuclei (56Fe, 62Ni, ..., 78Ni, 82Zn and beyond toward the drip line) follows from measured and extrapolated masses of neutron-rich nuclei; Penning-trap mass measurements at radioactive-beam facilities move the predicted layers.", "map": "g=\\frac{M(A,Z)c^2}{A}+\\frac{Z}{A}\\mu_e-\\frac43C_M\\frac{Z^{2/3}e^2}{A^{4/3}}n_b^{1/3}\\ \\to\\ \\min", "breaks": "The deeper outer crust needs masses beyond experimental reach, so model mass tables take over.", "confidence": "established", "strength": 2}
{"id": "C2533", "a": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Nuclear structure factors for WIMP-nucleus scattering", "kind": "method transfer", "summary": "Spin-independent and spin-dependent dark-matter rates need nuclear form factors and structure functions computed with the shell model and chiral-EFT currents; the nonrelativistic EFT of direct detection maps each operator onto distinct nuclear responses.", "map": "\\frac{d\\sigma}{dE_R}=\\frac{m_N}{2\\mu^2v^2}\\left[\\sigma_{SI}F^2(q)+\\sigma_{SD}\\frac{S(q)}{S(0)}\\right];\\ \\sigma_{SI}\\propto A^2", "breaks": "Two-body currents and nuclear-structure uncertainties grow at large momentum transfer and for odd-unpaired nuclei.", "confidence": "established", "strength": 3}
{"id": "C2534", "a": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "name": "Giant-dipole photodisintegration of UHE cosmic-ray nuclei", "kind": "mechanism", "summary": "Ultra-high-energy nuclei are destroyed by photodisintegration when CMB and infrared photons, boosted into the nucleus frame, hit the giant dipole resonance; this shapes the composition and cutoff of the UHECR spectrum alongside the GZK pion threshold for protons.", "map": "\\epsilon'=\\Gamma\\epsilon(1-\\cos\\theta)\\approx E_{\\rm GDR}\\approx15\\text{–}25\\ \\text{MeV}\\Rightarrow\\Gamma\\sim10^{9\\text{–}10}", "breaks": "Photonuclear cross sections for unstable intermediate nuclei are model-based, and source composition is degenerate with propagation.", "confidence": "established", "strength": 2}
{"id": "C2630", "a": "08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Band theory of neutrons in the neutron-star crust", "kind": "method transfer", "summary": "Bragg scattering of unbound superfluid neutrons by the nuclear lattice of the inner crust is computed with Bloch's theorem and band-structure methods; the resulting large neutron effective mass (entrainment) reduces the mobile superfluid fraction and challenges crust-only glitch models.", "map": "\\psi_{nk}(\\mathbf r+\\mathbf R)=e^{i\\mathbf k\\cdot\\mathbf R}\\psi_{nk}(\\mathbf r):\\ \\text{electrons}\\to\\text{free neutrons};\\ m_n^*/m_n\\gg1\\ (\\text{entrainment})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2631", "a": "08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Degenerate Fermi gas: metals and white dwarfs", "kind": "identity", "summary": "The same degenerate Fermi-Dirac electron gas gives the Sommerfeld model of metals and the pressure that supports white dwarfs; Fowler applied Fermi statistics to white dwarfs in 1926, before Sommerfeld applied it to metals, and relativistic kinematics turns P~n^{5/3} into P~n^{4/3}, giving the Chandrasekhar mass.", "map": "E_F=\\frac{\\hbar^2}{2m_e}(3\\pi^2n_e)^{2/3},\\ P=\\tfrac25n_eE_F\\ (n_e\\sim10^{23}\\,\\text{cm}^{-3})\\to P\\propto n_e^{4/3}\\ (\\text{WD},\\ n_e\\sim10^{30})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2632", "a": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets", "name": "Superionic water ice in ice-giant interiors", "kind": "shared object", "summary": "Superionic water, an oxygen crystal through which protons diffuse like a liquid, was predicted by ab initio simulation for Uranus and Neptune and identified in laser-shock experiments by nanosecond X-ray diffraction (fcc ice XVIII); it may explain the ice giants' non-dipolar magnetic fields.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2633", "a": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Coulomb crystallization of white-dwarf cores", "kind": "mechanism", "summary": "Carbon-oxygen ions in a cooling white dwarf freeze into a bcc Coulomb (one-component-plasma) crystal near Gamma~175; Gaia's cooling-sequence pile-up confirmed latent-heat release and phase separation, and the same bcc Coulomb lattice makes up neutron-star crusts.", "map": "\\Gamma=\\frac{Z^2e^2}{4\\pi\\epsilon_0ak_BT}\\approx175\\ (\\text{melting}),\\ a=(3/4\\pi n_i)^{1/3};\\ \\text{bcc, Madelung energy}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2634", "a": "08-condensed-matter/crystals-and-electronic-structure/density-functional-theory", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "DFT and dielectric response for dark-matter scattering", "kind": "method transfer", "summary": "Dark-matter-electron scattering rates in crystals are computed from DFT crystal form factors and, with screening included, from the energy-loss function Im[-1/eps(q,omega)], so electronic-structure codes directly set direct-detection sensitivities.", "map": "\\frac{dR}{d\\omega}\\propto\\int d^3q\\,\\frac{q^2}{e^2}\\,\\mathrm{Im}\\left[\\frac{-1}{\\epsilon(\\mathbf q,\\omega)}\\right]\\eta(v_{\\min})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2635", "a": "08-condensed-matter/crystals-and-electronic-structure/density-functional-theory", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets", "name": "Ab initio equations of state for giant-planet interiors", "kind": "method transfer", "summary": "DFT-based molecular dynamics provides the hydrogen-helium equation of state and the H-He immiscibility ('helium rain') used in Jupiter and Saturn interior models fitted to Juno and Cassini gravity data; DFT exchange-correlation and band-gap errors directly shift the predicted metallization boundary.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2636", "a": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Electron transport in white-dwarf and neutron-star matter", "kind": "method transfer", "summary": "Thermal and electrical conductivities of degenerate stellar matter are computed with the Boltzmann/Ziman theory of metals (electron-phonon Umklapp and electron-impurity scattering, Wiedemann-Franz); crust-cooling curves of accreting neutron stars imply a low-impurity, ordered rather than amorphous crust.", "map": "\\sigma=\\frac{n_ee^2\\tau}{m^*},\\ \\frac{\\kappa}{\\sigma T}=\\frac{\\pi^2k_B^2}{3e^2},\\ \\tau^{-1}=\\tau_{e\\text{-ph}}^{-1}+\\tau_{e\\text{-imp}}^{-1}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2637", "a": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Single-phonon excitations for sub-MeV dark matter", "kind": "mechanism", "summary": "Below ~MeV the dark matter's momentum transfer is below the inverse lattice spacing, so it scatters by creating single acoustic or optical phonons rather than nuclear recoils; polar crystals (GaAs, sapphire) with dark-photon-coupled optical phonons are proposed targets read out by phonon sensors.", "map": "q\\sim m_\\chi v\\lesssim2\\pi/a\\Rightarrow\\text{phonon regime};\\ \\hbar\\omega_q\\sim10\\text{-}100\\,\\text{meV}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2638", "a": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/fast-radio-bursts-and-magnetars", "name": "Crustal shear modes as magnetar QPOs", "kind": "mechanism", "summary": "Quasi-periodic oscillations in magnetar giant-flare tails (tens of Hz) are interpreted as global torsional modes of the crystalline crust, i.e. long-wavelength transverse acoustic phonons of the Coulomb lattice whose speed is set by the shear modulus mu~0.12 n_i Z^2 e^2/a.", "map": "\\omega=v_tk,\\ v_t=\\sqrt{\\mu/\\rho};\\ f_\\ell\\approx\\frac{v_t}{2\\pi R}\\sqrt{(\\ell-1)(\\ell+2)}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2639", "a": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Debye cooling of crystallized white dwarfs", "kind": "mechanism", "summary": "Once a white-dwarf core crystallizes, its ionic heat capacity follows the Debye phonon law and falls as T^3 below Theta_D, so the oldest white dwarfs cool faster ('Debye cooling'), which shapes the faint end of the luminosity function used for cosmochronology.", "map": "C_V=\\frac{12\\pi^4}{5}Nk_B(T/\\Theta_D)^3,\\ \\Theta_D\\sim\\hbar\\omega_{p,i}/k_B,\\ \\omega_{p,i}=\\sqrt{n_iZ^2e^2/\\epsilon_0m_i}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2640", "a": "08-condensed-matter/crystals-and-electronic-structure/semiconductors", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Semiconductor targets for dark-matter electron recoils", "kind": "shared object", "summary": "Silicon and germanium crystals are dark-matter targets: ionization-plus-phonon detectors for nuclear recoils, and single-electron skipper CCDs (SENSEI, DAMIC-M) whose ~1 eV band gap lets sub-GeV dark matter register through electron excitations across the gap.", "map": "E_e\\ge E_g\\approx1.1\\,\\text{eV (Si)};\\ N_{eh}=1+\\lfloor(E_e-E_g)/\\varepsilon\\rfloor,\\ \\varepsilon\\approx3.6\\,\\text{eV}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2641", "a": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "name": "Fullerenes and PAHs: carbon nanostructures in space", "kind": "historical", "summary": "C60 was discovered in laser-vaporization experiments built to mimic carbon-star chemistry, opening the fullerene-nanotube-graphene family of carbon materials; fullerenes were later found in planetary nebulae and C60+ identified as a diffuse-interstellar-band carrier.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2642", "a": "08-condensed-matter/low-dimensional-and-quantum-materials/moire-materials-and-twisted-bilayers", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Wigner crystals and stellar Coulomb crystals", "kind": "analogy", "summary": "Electron Wigner crystals in moire TMD superlattices and the ion crystals of white dwarfs and neutron-star crusts are both one-component plasmas that crystallize in a uniform neutralizing background once Coulomb energy beats kinetic energy (large r_s or large Gamma).", "map": "r_s=a/a_B^*\\gtrsim31\\ (\\text{2D quantum, kinetic}=E_F)\\leftrightarrow\\Gamma\\approx175\\ (\\text{classical, kinetic}=k_BT)", "breaks": "Stellar ions melt classically through thermal fluctuations, while 2D electron Wigner crystals melt quantum mechanically; moire Wigner crystals are pinned to an imposed superlattice and are two-dimensional.", "confidence": "established", "strength": 1}
{"id": "C2643", "a": "08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Emergent monopoles in spin ice and the monopole problem", "kind": "analogy", "summary": "Spin-ice excitations behave as deconfined magnetic monopoles with a Coulomb interaction, a condensed-matter realization of the monopoles whose predicted overproduction at grand-unified transitions motivated inflation.", "map": "", "breaks": "Spin-ice monopoles source the H field (div M), not B; they are emergent quasiparticles with non-quantized, material-set charge, unlike 't Hooft-Polyakov monopoles of a broken gauge group.", "confidence": "established", "strength": 1}
{"id": "C2644", "a": "08-condensed-matter/magnetism/magnetic-skyrmions-and-textures", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "Skyrmions and cosmic textures", "kind": "analogy", "summary": "Magnetic skyrmions and cosmological textures are both non-singular topological solitons of a sphere-valued order parameter classified by homotopy (pi_2 for 2D films, pi_3 for 3D cosmic textures); a collapsing texture was proposed to explain the CMB Cold Spot.", "map": "N_{sk}=\\frac1{4\\pi}\\int\\mathbf m\\cdot(\\partial_x\\mathbf m\\times\\partial_y\\mathbf m)\\,d^2x\\in\\pi_2(S^2)\\leftrightarrow\\pi_3(S^3)\\ \\text{winding}", "breaks": "Skyrmions are static, DMI-stabilized and 2D; cosmic textures are 3D, unstable to collapse by Derrick's theorem and scale with the horizon. The Cold Spot texture interpretation is not established.", "confidence": "proposed", "strength": 1}
{"id": "C2645", "a": "08-condensed-matter/soft-matter/colloids-and-granular-matter", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks", "name": "Dust aggregation: from colloids to planetesimals", "kind": "mechanism", "summary": "The first stage of planet formation is aggregation of micron dust grains by Brownian motion and differential drift into fractal aggregates, followed by compaction, bouncing and fragmentation: the cluster-cluster aggregation and contact mechanics studied in colloids and granular matter.", "map": "D=\\frac{k_BT}{6\\pi\\eta a}\\to t_s=\\frac{\\rho_sa}{\\rho_gv_{th}}\\ (\\text{Epstein});\\ N\\propto R^{d_f},\\ d_f\\approx1.8\\text{-}2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2646", "a": "08-condensed-matter/soft-matter/colloids-and-granular-matter", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics", "name": "Rubble-pile asteroids as granular bodies", "kind": "shared object", "summary": "Most km-sized asteroids (Itokawa, Ryugu, Bennu) are gravitationally bound granular aggregates whose shapes, spin limits, regolith segregation and response to spacecraft contact are governed by granular rheology, friction and weak cohesion.", "map": "\\mu(I)=\\mu_s+\\frac{\\mu_2-\\mu_s}{1+I_0/I};\\ \\text{spin barrier }P\\approx2.2\\,\\text{h (cohesionless)}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2647", "a": "08-condensed-matter/soft-matter/glasses-and-jamming", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks", "name": "Amorphous ices and silicates in disks and dust", "kind": "shared object", "summary": "Interstellar and protoplanetary grains are largely amorphous: vapour-deposited amorphous solid water and glassy silicates whose crystallization (annealing near the star) and glass-transition kinetics record thermal history and control volatile trapping at snow lines.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C2648", "a": "08-condensed-matter/soft-matter/liquid-crystals", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Kibble-Zurek defects: liquid crystals and the early universe", "kind": "analogy", "summary": "Kibble's argument that causally disconnected regions choose independent vacua at a symmetry-breaking transition, leaving strings and monopoles whose overabundance inflation must dilute, was tested by quenching nematic liquid crystals and counting disclinations; Zurek's refinement gives defect density from the quench rate.", "map": "\\pi_1(\\mathcal M)\\neq0\\Rightarrow\\text{strings/disclinations};\\ \\hat\\xi\\sim\\xi_0(\\tau_Q/\\tau_0)^{\\nu/(1+z\\nu)},\\ n\\sim\\hat\\xi^{-2}", "breaks": "Nematic defects form in a dissipative, non-relativistic fluid with no gauge field and coarsen by friction; cosmic defects are relativistic, may be gauge strings, and evolve in an expanding spacetime.", "confidence": "established", "strength": 3}
{"id": "C2649", "a": "08-condensed-matter/soft-matter/liquid-crystals", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Nuclear pasta as a liquid crystal", "kind": "analogy", "summary": "In the neutron-star mantle, competition between nuclear surface tension and long-range Coulomb repulsion produces rod, slab and bubble 'pasta' phases with the symmetries of columnar and smectic liquid crystals (and of block-copolymer microphases); their elasticity is described with liquid-crystal theory.", "map": "F_{\\text{smectic}}=\\tfrac B2(\\partial_zu)^2+\\tfrac{K_1}2(\\nabla_\\perp^2u)^2\\ (\\text{lasagna});\\ \\text{columnar elasticity (spaghetti)}", "breaks": "Pasta is ordered by nuclear plus Coulomb forces at ~1e14 g/cm^3 with no solvent or thermal softness; its elastic constants are MeV-scale and the phases sit in a degenerate electron sea.", "confidence": "current research", "strength": 2}
{"id": "C2650", "a": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "Superconducting detectors for the CMB: TES and MKIDs", "kind": "method transfer", "summary": "CMB experiments (BICEP/Keck, SPT, ACT, Simons Observatory, CMB-S4) use arrays of transition-edge-sensor bolometers biased on the steep R(T) of a superconducting transition, and kinetic-inductance detectors that sense photon pair breaking through the Cooper-pair kinetic inductance.", "map": "\\alpha=\\frac TR\\frac{dR}{dT}\\sim100;\\ L_k\\propto\\mu_0\\lambda_L^2,\\ \\lambda_L^{-2}\\propto n_s;\\ h\\nu>2\\Delta\\ \\text{breaks pairs}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2651", "a": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Cosmic-string formation simulated in superfluid 3He", "kind": "analogy", "summary": "Neutron-absorption hot spots in BCS-paired superfluid 3He re-cool through Tc and nucleate vortex tangles at the rate predicted by the Kibble-Zurek mechanism, a laboratory test of defect formation in early-universe phase transitions with a multicomponent order parameter.", "map": "", "breaks": "3He is a non-relativistic p-wave condensate whose vortices are global (no gauge field), whereas GUT strings are relativistic and typically local; the quench is spatially inhomogeneous, unlike a cosmological transition.", "confidence": "established", "strength": 2}
{"id": "C2652", "a": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Superconducting phonon sensors and targets for dark matter", "kind": "method transfer", "summary": "Cryogenic dark-matter searches (SuperCDMS, CRESST) read athermal phonons from keV nuclear recoils with tungsten transition-edge sensors; superconductors themselves are proposed as targets for keV-mass dark matter because the gap 2Delta~meV sets an ultra-low threshold.", "map": "E_{\\text{th}}\\sim2\\Delta\\approx3.5k_BT_c\\sim\\text{meV}\\ \\text{vs. }E_g\\sim\\text{eV (semiconductor)}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2653", "a": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "name": "Cosmic rays and pair breaking in superconducting devices", "kind": "mechanism", "summary": "Cosmic-ray muons and environmental gamma rays deposit energy in substrates as athermal phonons that break Cooper pairs, causing correlated quasiparticle bursts and error avalanches in superconducting qubits; this is the pair-breaking channel that cryogenic detectors use to see particles.", "map": "N_{qp}\\approx\\eta E_{\\text{dep}}/\\Delta,\\ \\Delta_{\\text{Al}}\\approx0.18\\,\\text{meV}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2654", "a": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Nucleon pairing and neutron-star superfluidity", "kind": "mechanism", "summary": "The BCS gap equation with nuclear instead of phonon attraction gives 1S0 neutron superfluidity in the inner crust and 3P2 neutron and 1S0 proton pairing in the core; pair-breaking-formation neutrino emission just below Tc explains the rapid cooling of the Cas A neutron star.", "map": "\\Delta_k=-\\sum_{k'}V_{kk'}\\frac{\\Delta_{k'}}{2E_{k'}}\\tanh\\frac{E_{k'}}{2k_BT};\\ V:\\text{phonon (meV)}\\to\\text{NN }^1S_0,{}^3P_2\\text{ (MeV)}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2655", "a": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Vortex pinning and creep: flux lines vs pulsar glitches", "kind": "analogy", "summary": "Pulsar glitches are modelled as catastrophic unpinning of quantized neutron-superfluid vortices from the crust lattice, the physics of Abrikosov flux-line pinning and Anderson-Kim thermally activated flux creep in type-II superconductors; post-glitch relaxation is vortex creep.", "map": "\\oint\\mathbf v_s\\cdot d\\mathbf l=h/2m_n\\ (\\text{neutron vortex})\\leftrightarrow\\Phi_0=h/2e\\ (\\text{flux line});\\ \\text{Magnus}\\leftrightarrow\\text{Lorentz force}", "breaks": "Neutron vortices are neutral and feel Magnus rather than Lorentz forces; pinning sites are nuclei of a Coulomb lattice, not material defects, and entrainment couples the superfluid to the crust.", "confidence": "established", "strength": 3}
{"id": "C2656", "a": "08-condensed-matter/superconductivity/hydride-superconductors-under-pressure", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets", "name": "Metallic hydrogen in giant planets", "kind": "shared object", "summary": "Metallic hydrogen, predicted by Wigner and Huntington and proposed by Ashcroft as a high-Tc phonon superconductor (the idea behind hydride superconductors), makes up most of Jupiter's and Saturn's interiors, where its conductivity powers their dynamos; shock and static compression of the insulator-metal transition serve both fields.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2657", "a": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "SQUID multiplexed readout of detector arrays", "kind": "method transfer", "summary": "Kilo- to hundred-thousand-pixel TES arrays for CMB polarimetry are read out with SQUID amplifiers in time-division or microwave (rf-SQUID resonator) multiplexing, exploiting the flux-periodic Josephson response and its low noise.", "map": "V(\\Phi)\\ \\text{periodic in }\\Phi_0=h/2e;\\ \\delta\\Phi\\sim10^{-6}\\Phi_0/\\sqrt{\\text{Hz}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2658", "a": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Josephson parametric amplifiers in axion haloscopes", "kind": "method transfer", "summary": "Axion haloscopes (ADMX, HAYSTAC) detect axion-to-photon conversion in a microwave cavity with Josephson parametric amplifiers operating near the standard quantum limit, and HAYSTAC's squeezed-vacuum readout beats it.", "map": "T_{\\text{sys}}\\gtrsim\\hbar\\omega/k_B\\ (\\text{SQL});\\ \\text{scan rate}\\propto T_{\\text{sys}}^{-2}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2659", "a": "08-condensed-matter/topological-matter/topological-insulators", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Axion quasiparticles in magnetic topological insulators", "kind": "analogy", "summary": "Magnetic topological insulators host a dynamical axion field theta(t) coupling as theta E.B; its quasiparticle (a longitudinal antiferromagnetic magnon mode) is proposed as a tunable meV-scale medium that converts axion dark matter into THz photons.", "map": "\\mathcal L_\\theta=\\frac{\\theta e^2}{2\\pi h}\\mathbf E\\cdot\\mathbf B\\leftrightarrow\\mathcal L_a=g_{a\\gamma\\gamma}\\,a\\,\\mathbf E\\cdot\\mathbf B", "breaks": "The solid-state axion is an emergent collective mode with a material-set mass, not the QCD axion; only the electrodynamic coupling form is shared, and no candidate material is yet confirmed.", "confidence": "proposed", "strength": 2}
{"id": "C2660", "a": "08-condensed-matter/topological-matter/topological-semimetals", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Dirac materials as light dark-matter targets", "kind": "method transfer", "summary": "3D Dirac and Weyl semimetals with meV-scale gaps and weak in-medium screening have been proposed as targets for sub-MeV dark matter scattering or absorption on electrons, with directional sensitivity from anisotropic Dirac cones.", "map": "H_W=\\hbar v_F\\boldsymbol\\sigma\\cdot\\mathbf k,\\ E_g\\to\\text{meV};\\ v_F\\ll c\\ \\text{matches DM kinematics}", "breaks": "", "confidence": "proposed", "strength": 1}
{"id": "C2729", "a": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "CMB tests inflationary predictions", "kind": "shared object", "summary": "Near scale-invariant adiabatic Gaussian fluctuations, the spectral tilt and limits on tensor modes from B-mode polarization constrain inflationary models.", "map": "\\Delta_s^2\\propto k^{n_s-1},\\ r=\\Delta_t^2/\\Delta_s^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2730", "a": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "b": "09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao", "name": "Acoustic oscillations as standard ruler", "kind": "identity", "summary": "The same sound horizon at the drag epoch imprinted in the CMB peaks appears as the BAO feature in galaxy clustering, giving a standard ruler across redshift.", "map": "r_s=\\int_{z_d}^\\infty \\frac{c_s\\,dz}{H(z)}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2731", "a": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "b": "09-astrophysics-and-cosmology/dark-matter/astrophysical-evidence-for-dark-matter", "name": "CMB acoustic peaks require non-baryonic matter", "kind": "shared object", "summary": "Relative heights of the acoustic peaks fix the baryon and total matter densities; the third peak demands collisionless dark matter that decoupled potentials from the photon-baryon fluid.", "map": "\\Omega_c h^2\\approx0.12,\\ \\Omega_b h^2\\approx0.022", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2732", "a": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "b": "09-astrophysics-and-cosmology/galaxies/galaxy-clusters", "name": "Sunyaev-Zel'dovich effect", "kind": "mechanism", "summary": "Inverse-Compton scattering of CMB photons by hot intracluster electrons distorts the CMB spectrum, yielding cluster catalogs and pressure profiles.", "map": "\\Delta T/T=y\\,f(x),\\ y=\\int\\frac{k_BT_e}{m_ec^2}n_e\\sigma_T dl", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2733", "a": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "b": "09-astrophysics-and-cosmology/galaxies/high-redshift-universe-and-reionization", "name": "Reionization imprinted on the CMB", "kind": "shared object", "summary": "Thomson scattering from free electrons after reionization gives the optical depth tau and large-angle E-mode polarization bump, plus kinetic SZ, constraining when first galaxies ionized the universe.", "map": "\\tau=\\int n_e\\sigma_T\\,dl", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2734", "a": "09-astrophysics-and-cosmology/cosmology/dark-energy", "b": "09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao", "name": "BAO and DESI dark-energy constraints", "kind": "method transfer", "summary": "BAO distances combined with supernovae and CMB constrain the dark-energy equation of state; DESI hints at evolving w.", "map": "w(a)=w_0+w_a(1-a)", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2735", "a": "09-astrophysics-and-cosmology/cosmology/dark-energy", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients", "name": "Supernova systematics in the dark-energy era", "kind": "shared object", "summary": "Progenitor, host-galaxy and dust effects on Type Ia luminosities limit precision on the dark-energy equation of state, relevant to DESI and Rubin-era samples.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2736", "a": "09-astrophysics-and-cosmology/cosmology/dark-energy", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients", "name": "Type Ia supernovae as standard candles", "kind": "method transfer", "summary": "Type Ia light curves, standardised by width-luminosity corrections, give luminosity distances that revealed cosmic acceleration; stellar explosion physics sets the systematics of the dark-energy inference.", "map": "d_L(z)=(1+z)\\int_0^z \\frac{c\\,dz'}{H(z')}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2737", "a": "09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history", "b": "09-astrophysics-and-cosmology/dark-matter/astrophysical-evidence-for-dark-matter", "name": "Dark matter in the Friedmann budget", "kind": "shared object", "summary": "Evidence from CMB, BBN and structure growth fixes the cold dark matter density parameter in the Friedmann equation that sets expansion history.", "map": "H^2/H_0^2=\\Omega_m a^{-3}+\\Omega_r a^{-4}+\\Omega_\\Lambda", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2738", "a": "09-astrophysics-and-cosmology/cosmology/gravitational-lensing", "b": "09-astrophysics-and-cosmology/cosmology/hubble-tension-and-cosmological-tensions", "name": "Time-delay cosmography and cosmic shear", "kind": "method transfer", "summary": "Strong-lens time delays give H0 independent of the distance ladder, while weak-lensing shear measures S8, the other tension.", "map": "\\Delta t=\\frac{D_{\\Delta t}}{c}\\Delta\\phi", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2739", "a": "09-astrophysics-and-cosmology/cosmology/gravitational-lensing", "b": "09-astrophysics-and-cosmology/dark-matter", "name": "Lensing maps dark matter", "kind": "method transfer", "summary": "Lensing responds to total mass irrespective of luminosity, so strong and weak lensing give direct mass maps and halo profiles, as in the Bullet Cluster and subhalo searches.", "map": "\\kappa=\\Sigma/\\Sigma_{cr}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2740", "a": "09-astrophysics-and-cosmology/cosmology/gravitational-lensing", "b": "09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure", "name": "Lensing probes dark subhalos", "kind": "method transfer", "summary": "Flux-ratio anomalies and gravitational imaging of strong lenses detect low-mass subhalos, constraining warm, fuzzy and self-interacting dark matter on sub-galactic scales.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2741", "a": "09-astrophysics-and-cosmology/cosmology/gravitational-lensing", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-detection", "name": "Microlensing finds planets", "kind": "method transfer", "summary": "Gravitational microlensing, developed for MACHO searches, detects cold and free-floating planets beyond the reach of transits and radial velocity.", "map": "\\theta_E=\\sqrt{\\frac{4GM}{c^2}\\frac{D_{LS}}{D_LD_S}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2742", "a": "09-astrophysics-and-cosmology/cosmology/hubble-tension-and-cosmological-tensions", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients", "name": "Distance ladder and Hubble tension", "kind": "method transfer", "summary": "Cepheid and TRGB calibrated Type Ia supernovae set the local H0 that disagrees with CMB inference; stellar physics systematics are central to the dispute.", "map": "H_0=\\frac{v}{d}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2743", "a": "09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao", "b": "09-astrophysics-and-cosmology/galaxies", "name": "Hierarchical growth from primordial perturbations", "kind": "mechanism", "summary": "Gravitational growth of primordial density perturbations builds halos, filaments and then galaxies; large-scale structure statistics supply the initial conditions for galaxy formation.", "map": "\\ddot\\delta+2H\\dot\\delta=4\\pi G\\bar\\rho\\,\\delta", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2744", "a": "09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao", "b": "09-astrophysics-and-cosmology/galaxies/galaxy-formation-and-evolution", "name": "Galaxy bias links halos to the matter field", "kind": "shared object", "summary": "Galaxy surveys trace the cosmic web only through galaxy formation physics; halo occupation and bias connect observed clustering to the underlying matter power spectrum.", "map": "\\delta_g=b\\,\\delta_m", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2745", "a": "09-astrophysics-and-cosmology/dark-matter", "b": "09-astrophysics-and-cosmology/galaxies", "name": "Dark halos host galaxies", "kind": "shared object", "summary": "Galaxies form within dark-matter halos, whose potentials set rotation curves, scaling relations and merger histories.", "map": "v_c^2=GM(<r)/r", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2746", "a": "09-astrophysics-and-cosmology/dark-matter/alternatives-mond-and-modified-gravity", "b": "09-astrophysics-and-cosmology/galaxies/galaxy-clusters", "name": "Cluster problem for MOND", "kind": "analogy", "summary": "MOND fits rotation curves but needs extra unseen mass in clusters, and the Bullet Cluster lensing offset challenges it.", "map": "", "breaks": "Fails at cluster scales without additional dark components such as sterile neutrinos.", "confidence": "current research", "strength": 2}
{"id": "C2747", "a": "09-astrophysics-and-cosmology/dark-matter/alternatives-mond-and-modified-gravity", "b": "09-astrophysics-and-cosmology/galaxies/galaxy-formation-and-evolution", "name": "Galaxy scaling relations and MOND", "kind": "shared object", "summary": "Baryonic Tully-Fisher and the radial acceleration relation are tight galaxy scaling laws that MOND predicts directly, whereas CDM must reproduce them through feedback.", "map": "v^4=GMa_0", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2748", "a": "09-astrophysics-and-cosmology/dark-matter/astrophysical-evidence-for-dark-matter", "b": "09-astrophysics-and-cosmology/galaxies/galaxy-clusters", "name": "Cluster dynamics, gas and lensing mass", "kind": "shared object", "summary": "Zwicky's virial argument, X-ray hydrostatic gas masses and lensing all show clusters dominated by dark matter, and the Bullet Cluster separates the mass from the baryons.", "map": "M=\\frac{3\\sigma^2 R}{G}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2749", "a": "09-astrophysics-and-cosmology/dark-matter/astrophysical-evidence-for-dark-matter", "b": "09-astrophysics-and-cosmology/galaxies/galaxy-clusters", "name": "Clusters as dark-matter laboratories", "kind": "shared object", "summary": "Cluster mass budgets from X-ray hydrostatic equilibrium, SZ, lensing and galaxy velocities give dark-matter fractions and collisional constraints.", "map": "\\frac{dP}{dr}=-\\rho_{gas}\\frac{GM}{r^2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2750", "a": "09-astrophysics-and-cosmology/dark-matter/astrophysical-evidence-for-dark-matter", "b": "09-astrophysics-and-cosmology/galaxies/the-milky-way", "name": "Galactic dynamics and the local halo", "kind": "shared object", "summary": "Milky Way rotation curve, Gaia stellar streams and escape velocity measure the halo mass and local density, key inputs to direct-detection rates.", "map": "v_c^2=GM(<r)/r", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2751", "a": "09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure", "b": "09-astrophysics-and-cosmology/galaxies/galaxy-formation-and-evolution", "name": "Baryonic feedback vs dark-matter physics", "kind": "mechanism", "summary": "Cusp-core, missing satellites and too-big-to-fail can be solved either by new dark-matter physics or by supernova feedback and reionization suppressing dwarf galaxy formation; the two are degenerate.", "map": "", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2752", "a": "09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure", "b": "09-astrophysics-and-cosmology/galaxies/galaxy-formation-and-evolution", "name": "Dwarf galaxy tests of CDM", "kind": "shared object", "summary": "Dwarf galaxy scaling relations and simulations are the testing ground for CDM versus alternatives, with baryonic physics the key systematic.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2753", "a": "09-astrophysics-and-cosmology/dark-matter/indirect-detection", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "name": "Cosmic-ray backgrounds for dark-matter signals", "kind": "shared object", "summary": "Antiprotons, positrons and gamma rays from dark-matter annihilation must be separated from astrophysical cosmic-ray production and propagation, as in the positron excess and antiproton debates.", "map": "", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2754", "a": "09-astrophysics-and-cosmology/galaxies/active-galactic-nuclei-and-supermassive-black-holes", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/neutrino-astronomy", "name": "AGN as neutrino sources", "kind": "shared object", "summary": "Blazars such as TXS 0506+056 and Seyferts like NGC 1068 are identified IceCube sources; hadronic acceleration in jets and coronae produces neutrinos with gamma rays.", "map": "p+\\gamma\\to\\Delta^+\\to\\pi^+\\to\\nu", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2755", "a": "09-astrophysics-and-cosmology/galaxies/active-galactic-nuclei-and-supermassive-black-holes", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks", "name": "Accretion disk theory shared", "kind": "analogy", "summary": "Shakura-Sunyaev alpha disks and MRI-driven turbulence describe both AGN accretion and protoplanetary disks.", "map": "", "breaks": "Disk temperature, ionization and radiation pressure regimes differ by many orders of magnitude, so MRI activity and dead zones apply differently.", "confidence": "established", "strength": 2}
{"id": "C2756", "a": "09-astrophysics-and-cosmology/galaxies/the-milky-way", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/binary-stars-and-stellar-populations", "name": "Stellar populations as galactic archaeology", "kind": "method transfer", "summary": "Ages, abundances and kinematics of stellar populations, with Gaia, reconstruct the Milky Way's assembly history and star-formation history.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2757", "a": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients", "name": "Supernova remnants accelerate cosmic rays", "kind": "mechanism", "summary": "Diffusive shock acceleration at supernova remnant shocks is the standard origin of Galactic cosmic rays up to the knee.", "map": "dN/dE\\propto E^{-2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2758", "a": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/fast-radio-bursts-and-magnetars", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Magnetars as FRB engines", "kind": "shared object", "summary": "The Galactic magnetar SGR 1935+2154 emitted an FRB-like burst, tying FRBs to highly magnetised neutron stars.", "map": "", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2759", "a": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/gamma-ray-bursts", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/multi-messenger-astronomy", "name": "Short GRBs from neutron-star mergers", "kind": "shared object", "summary": "GW170817 with GRB 170817A and the kilonova established compact mergers as short-GRB progenitors, with off-axis jet physics.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2760", "a": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/gamma-ray-bursts", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients", "name": "Long GRBs and collapsars", "kind": "mechanism", "summary": "Long GRBs accompany broad-lined Type Ic supernovae from collapsing massive stars, linking relativistic jets to core-collapse explosions.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2761", "a": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/multi-messenger-astronomy", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Gravitational waves from compact binaries", "kind": "shared object", "summary": "Neutron-star and black-hole mergers are the gravitational-wave sources; kilonovae probe r-process nucleosynthesis and dense-matter equation of state.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2762", "a": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/neutrino-astronomy", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "name": "Solar neutrinos and neutrino astronomy", "kind": "historical", "summary": "Solar neutrino detection, resolving the solar neutrino problem via oscillations, established the techniques and flavor physics later used in astrophysical neutrino telescopes.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2763", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-atmospheres", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "name": "Radiative transfer in atmospheres", "kind": "method transfer", "summary": "Exoplanet atmosphere retrievals use radiative transfer and opacities developed for stellar atmospheres, and stellar activity and limb darkening contaminate transmission spectra.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2764", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/binary-stars-and-stellar-populations", "name": "Disks around young stars and accretion", "kind": "analogy", "summary": "Viscous accretion disks govern protoplanetary evolution and mass transfer in binaries, sharing alpha-disk transport and angular-momentum redistribution.", "map": "\\nu=\\alpha c_s H", "breaks": "Protoplanetary disks are cool, dusty and partly neutral, so non-ideal MHD and dust dynamics differ from ionized binary disks.", "confidence": "established", "strength": 2}
{"id": "C2765", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "name": "Degeneracy pressure sets remnant masses", "kind": "mechanism", "summary": "Stellar evolution ends in white dwarfs, neutron stars or black holes, and degeneracy pressure support yields the Chandrasekhar and TOV mass limits.", "map": "M_{Ch}\\approx1.4\\,M_\\odot", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2766", "a": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Primordial plasma and Thomson scattering", "kind": "shared object", "summary": "Before recombination the universe was a tightly coupled photon–baryon plasma, whose acoustic oscillations imprint the CMB peaks. Thomson scattering off free electrons sets the optical depth, and reionization polarizes the CMB.", "map": "\\tau=\\int n_e\\sigma_T\\,c\\,dt", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2767", "a": "09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "BAO as sound waves in the primordial plasma", "kind": "analogy", "summary": "Baryon acoustic oscillations are ion-acoustic-like pressure waves in the coupled photon–baryon fluid. The sound horizon is a standard ruler, and Jeans instability parallels plasma streaming and gravitational instabilities.", "map": "c_s^2=\\frac{c^2}{3(1+R)}", "breaks": "Gravity and radiation drag replace electrostatic restoring forces, and there is no Debye-scale dispersion.", "confidence": "established", "strength": 1}
{"id": "C2768", "a": "09-astrophysics-and-cosmology/galaxies/active-galactic-nuclei-and-supermassive-black-holes", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "Magnetically driven AGN jets", "kind": "mechanism", "summary": "Relativistic AGN jets are launched and collimated by magnetic fields threading a black hole or disk, as in Blandford–Znajek and Blandford–Payne. These are force-free and relativistic MHD flows.", "map": "P_{BZ}\\propto \\Omega_H^2\\Phi^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2769", "a": "09-astrophysics-and-cosmology/galaxies/active-galactic-nuclei-and-supermassive-black-holes", "b": "10-plasma-physics/magnetohydrodynamics/magnetic-reconnection", "name": "Reconnection in jets and coronae", "kind": "mechanism", "summary": "Relativistic reconnection and plasmoid chains are invoked for particle acceleration and fast blazar flares, and for heating accretion-disk coronae.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2770", "a": "09-astrophysics-and-cosmology/galaxies/galaxy-clusters", "b": "10-plasma-physics/magnetohydrodynamics/mhd-turbulence", "name": "Turbulence and magnetic fields in clusters", "kind": "mechanism", "summary": "Cluster mergers and AGN drive turbulence that amplifies magnetic fields by a small-scale turbulent dynamo. Radio halos arise from turbulent reacceleration of relativistic electrons.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2771", "a": "09-astrophysics-and-cosmology/galaxies/galaxy-clusters", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Intracluster medium as a weakly collisional plasma", "kind": "shared object", "summary": "The hot, magnetised intracluster medium has long mean free paths, so pressure anisotropy, firehose and mirror instabilities, and suppressed Spitzer conduction require kinetic treatment. Plasma microinstabilities regulate viscosity and heat transport.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2772", "a": "09-astrophysics-and-cosmology/galaxies/high-redshift-universe-and-reionization", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Reionization and the intergalactic plasma", "kind": "shared object", "summary": "Reionization turned the neutral intergalactic medium into a tenuous, ionized plasma. Its free-electron column sets the CMB optical depth and the FRB dispersion measure.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C2773", "a": "09-astrophysics-and-cosmology/galaxies/the-milky-way", "b": "10-plasma-physics/magnetohydrodynamics/dynamo-theory", "name": "Galactic dynamo and seed fields", "kind": "mechanism", "summary": "Galactic magnetic fields of microgauss strength are explained by mean-field αΩ dynamos acting on weak seed fields. Fluctuation dynamos amplify fields in early galaxies, and the seed origin remains open.", "map": "\\partial_t\\mathbf{B}=\\nabla\\times(\\mathbf{u}\\times\\mathbf{B}+\\alpha\\mathbf{B})+\\eta\\nabla^2\\mathbf{B}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2774", "a": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle", "b": "10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks", "name": "Astroparticle sources are astrophysical plasma shocks", "kind": "shared object", "summary": "High-energy astrophysical sources accelerate particles in collisionless shocks and magnetised outflows, so plasma shock physics underlies cosmic-ray, GRB and neutrino source modelling.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2775", "a": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "b": "10-plasma-physics/inertial-and-laser-plasmas/plasma-wakefield-acceleration", "name": "Plasma wakefield acceleration and astrophysical acceleration", "kind": "analogy", "summary": "Wakefield acceleration and cosmic-ray acceleration both push charged particles to high energy in collective plasma fields, and wakefield-type mechanisms are proposed for UHECR. Wakefields are coherent and laminar while Fermi processes are stochastic.", "map": "", "breaks": "Wakefields give deterministic gradients in a driven wave, while Fermi acceleration is statistical scattering across a shock.", "confidence": "proposed", "strength": 1}
{"id": "C2776", "a": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "Alfvén waves scatter cosmic rays", "kind": "mechanism", "summary": "Cosmic rays stream along field lines and resonantly excite Alfvén waves, which scatter them and set the diffusion coefficient. Self-generated waves confine Galactic cosmic rays and feed back in shock precursors.", "map": "\\omega=k_\\parallel v_A,\\ k_\\parallel r_g\\sim1", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2777", "a": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "b": "10-plasma-physics/magnetohydrodynamics/mhd-turbulence", "name": "Turbulent scattering and cosmic-ray transport", "kind": "mechanism", "summary": "Cosmic-ray diffusion in the Galaxy is set by scattering off MHD turbulence. Goldreich–Sridhar anisotropy makes resonant scattering by Alfvénic modes inefficient, so compressive modes and cascade properties matter.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2778", "a": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "b": "10-plasma-physics/space-and-astrophysical-plasmas", "name": "Cosmic rays and heliospheric particle physics", "kind": "shared object", "summary": "Galactic cosmic rays propagate through the turbulent magnetised solar wind and heliosphere, where modulation, diffusion and scattering are plasma processes. The same transport theory applies in the Galaxy.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2779", "a": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "b": "10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks", "name": "Diffusive shock acceleration of cosmic rays", "kind": "mechanism", "summary": "First-order Fermi acceleration at collisionless shocks yields a power-law spectrum p^-(3r/(r-1)) with index near 2 for strong shocks, and explains the cosmic-ray spectrum from supernova remnants. Magnetic-field amplification enables acceleration toward the knee.", "map": "N(E)\\propto E^{-(r+2)/(r-1)},\\ r=4\\Rightarrow E^{-2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2780", "a": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/fast-radio-bursts-and-magnetars", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "FRB emission as coherent plasma processes", "kind": "mechanism", "summary": "FRB models invoke coherent emission from plasma instabilities, maser-like shock emission and magnetospheric reconnection. Propagation through plasma produces dispersion, scattering and Faraday rotation, which make FRBs probes of intergalactic baryons.", "map": "\\omega^2=\\omega_p^2+k^2c^2,\\ \\mathrm{DM}=\\int n_e\\,dl", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2781", "a": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/gamma-ray-bursts", "b": "10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks", "name": "GRB afterglows from relativistic collisionless shocks", "kind": "mechanism", "summary": "GRB afterglow synchrotron emission arises from relativistic collisionless shocks, where Weibel-type instabilities generate magnetic fields and accelerate electrons. PIC simulations of these shocks inform the microphysical parameters ε_B and ε_e.", "map": "", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2782", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-atmospheres", "b": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "name": "Planetary interiors at megabar pressures", "kind": "shared object", "summary": "Giant-planet interiors contain hydrogen, helium and water at megabar pressures, where laser shock experiments measure the equation of state, metallization and demixing. Results feed interior and evolution models.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2783", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks", "b": "10-plasma-physics/magnetohydrodynamics", "name": "Magnetised accretion disks and the MRI", "kind": "mechanism", "summary": "Angular momentum transport in ionised protoplanetary disks is driven by the magnetorotational instability. Nonideal MHD effects (Ohmic, Hall, ambipolar) and disk winds set accretion and dead zones.", "map": "\\omega_{A}=k_z v_A,\\ \\frac{d\\Omega^2}{d\\ln r}<0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2784", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "Disk MRI from ideal-MHD Alfvén dynamics", "kind": "mechanism", "summary": "The MRI is an ideal-MHD instability in which a weak field acts like a spring tying fluid elements in differential rotation, an Alfvén-wave tension effect. It drives disk turbulence and angular momentum transport.", "map": "\\omega^4-\\omega^2(\\kappa^2+2k^2v_A^2)+k^2v_A^2\\left(k^2v_A^2+\\frac{d\\Omega^2}{d\\ln r}\\right)=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2785", "a": "09-astrophysics-and-cosmology/stellar-astrophysics", "b": "10-plasma-physics", "name": "Stellar interiors and atmospheres are plasmas", "kind": "shared object", "summary": "Stars are self-gravitating plasmas. Their equation of state, opacity, transport, convection, magnetism and winds draw on plasma physics, and fusion burning links to laboratory fusion.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2786", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "b": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "name": "Dense matter equations of state in the lab", "kind": "method transfer", "summary": "Laser-driven shocks and X-ray Thomson scattering probe warm dense matter relevant to white-dwarf and giant-planet interiors. Laboratory equations of state calibrate dense-plasma models for compact objects.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2787", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "b": "10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks", "name": "Pulsar wind nebulae and relativistic shocks", "kind": "shared object", "summary": "Pulsar winds terminate in relativistic shocks that accelerate pairs and power synchrotron nebulae such as the Crab. These are testbeds for relativistic shock acceleration and magnetic reconnection in striped winds.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2788", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "b": "10-plasma-physics/magnetic-confinement-fusion/burning-plasmas-and-iter", "name": "Stellar nucleosynthesis and fusion burning", "kind": "analogy", "summary": "Stars burn by thermonuclear fusion with Gamow-peak reaction rates, and fusion devices target the same reactions. Laboratory D-T burning plasmas are self-heated by alphas, like stellar cores.", "map": "\\langle\\sigma v\\rangle\\propto \\exp(-3E_G^{1/3}/(4kT)^{1/3})", "breaks": "Stars confine by gravity at about 10^7 K and long timescales, while devices use magnetic fields at 10^8 K and lack gravitational stability.", "confidence": "established", "strength": 2}
{"id": "C2789", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients", "b": "10-plasma-physics/inertial-and-laser-plasmas/inertial-confinement-fusion", "name": "Rayleigh–Taylor mixing in supernovae and ICF", "kind": "analogy", "summary": "Hydrodynamic instabilities at accelerating interfaces occur in core-collapse explosions and in ICF capsule implosions. Scaled laser experiments reproduce supernova mixing, and the shared physics is Rayleigh–Taylor and Richtmyer–Meshkov growth.", "map": "\\gamma=\\sqrt{A k g}", "breaks": "ICF has ablation stabilization and sharp interfaces, while supernovae involve gravity, neutrinos and nuclear burning.", "confidence": "established", "strength": 2}
{"id": "C2790", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients", "b": "10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks", "name": "Supernova remnant shocks", "kind": "shared object", "summary": "Supernova remnants are the canonical sites of collisionless shocks, with magnetic-field amplification, thin X-ray rims and gamma-ray emission. They are the leading candidate sources of Galactic cosmic rays.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2791", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "b": "10-plasma-physics/magnetohydrodynamics", "name": "Solar magnetism as MHD", "kind": "shared object", "summary": "Sunspots, flux emergence, flares and coronal structure are MHD phenomena. Frozen-in flux, reconnection and Alfvén waves describe the Sun's magnetic activity.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2792", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "b": "10-plasma-physics/magnetohydrodynamics/dynamo-theory", "name": "The solar dynamo and the solar cycle", "kind": "mechanism", "summary": "The 11-year solar cycle is produced by a dynamo in which differential rotation (the Ω-effect) and helical convection (the α-effect) regenerate field. Helioseismology constrains the rotation profile that feeds mean-field models.", "map": "\\partial_t \\mathbf{B}=\\nabla\\times(\\mathbf{u}\\times\\mathbf{B}+\\alpha\\mathbf{B})+\\eta\\nabla^2\\mathbf{B}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2793", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "b": "10-plasma-physics/magnetohydrodynamics/magnetic-reconnection", "name": "Solar flares as reconnection", "kind": "mechanism", "summary": "Solar flares and CMEs release stored magnetic energy by reconnection, per the standard CSHKP model. The Sweet–Parker rate is too slow, which motivated plasmoid and collisionless reconnection.", "map": "v_{in}/v_A\\sim S^{-1/2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2794", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "b": "10-plasma-physics/space-and-astrophysical-plasmas", "name": "Sun to heliosphere", "kind": "shared object", "summary": "The Sun drives the solar wind, coronal mass ejections and space weather. Helioseismology and coronal physics set the boundary conditions for heliospheric plasma models.", "map": "", "breaks": "", "confidence": "established", "strength": 2}