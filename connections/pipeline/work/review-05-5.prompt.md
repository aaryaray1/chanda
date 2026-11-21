You are the relativist, the specialist for 05 (Relativity and Gravitation) in this physics knowledge base.

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

## Field overview · `knowledge/05-relativity-and-gravitation`

> **Specialist:** `relativist` · **arXiv:** gr-qc, hep-th, astro-ph.HE, astro-ph.CO · **Literature source:** INSPIRE-HEP (citation-ranked) + arXiv (latest)

#### What this field studies
Special relativity unifies space and time into Minkowski spacetime, with the speed of light invariant. General relativity (GR) makes spacetime dynamical: mass–energy curves it, and free bodies follow geodesics. GR predicts black holes, gravitational waves, gravitational lensing and an expanding universe — all now observed. Its incompatibility with quantum mechanics at the Planck scale motivates quantum gravity: string theory, holography, loop quantum gravity and other approaches.

#### Conventions used in this branch
- **Metric signature $(-,+,+,+)$** (MTW, Wald, Carroll) unless stated; particle physics uses $(+,-,-,-)$. Flag the signature in every derivation.
- **Geometrized units $G=c=1$** in most GR work: $M_\odot\approx1.477$ km $\approx4.93\ \mu$s. Restore units before quoting results.
- Greek indices 0–3, Latin 1–3; Riemann sign conventions differ between texts — follow MTW.

#### Historical spine
1887 Michelson–Morley · 1905 special relativity · 1907 equivalence principle · 1915 Einstein field equations; Mercury's perihelion · 1916 Schwarzschild solution; GW prediction · 1919 eclipse light-bending · 1922–27 Friedmann, Lemaître · 1939 Oppenheimer–Snyder collapse · 1959 Pound–Rebka · 1963 Kerr solution · 1965 Penrose singularity theorem · 1974 Hawking radiation; Hulse–Taylor binary pulsar · 1984 first superstring revolution · 1997 AdS/CFT · 2011 Gravity Probe B · 2015 GW150914 · 2017 GW170817 multi-messenger event · 2019 M87* image · 2022 Sgr A* image · 2023 PTA evidence for nanohertz background.

#### Canonical textbooks
- Taylor & Wheeler, *Spacetime Physics* — special relativity.
- Hartle, *Gravity* — physics-first undergraduate GR; Schutz, *A First Course in General Relativity*.
- Carroll, *Spacetime and Geometry*; Wald, *General Relativity*; Misner, Thorne & Wheeler, *Gravitation*.
- Maggiore, *Gravitational Waves* (2 vols.); Poisson & Will, *Gravity*.
- Polchinski, *String Theory*; Rovelli, *Quantum Gravity*; Birrell & Davies, *Quantum Fields in Curved Space*.

#### Live frontiers
- Precision tests of GR with GW populations, ringdown spectroscopy and EHT.
- The black-hole information problem: islands and replica wormholes.
- Third-generation detectors (Einstein Telescope, Cosmic Explorer) and LISA (adopted 2024).

#### How the specialist works here
State the metric and signature; use symmetries (Killing vectors) to find conserved quantities; compute invariants rather than coordinate-dependent quantities; check the Newtonian limit ($g_{00}\approx-(1+2\Phi/c^2)$) and the flat-space limit; distinguish coordinate from physical singularities.

## Gravitational waves · `knowledge/05-relativity-and-gravitation/gravitational-waves`

#### Overview
Accelerating masses radiate gravitational waves — transverse, quadrupolar strains travelling at $c$. Predicted in 1916, indirectly confirmed by binary pulsars in the 1970s–80s, and directly detected by LIGO on 14 September 2015 (GW150914), they now provide catalogues of hundreds of compact-binary mergers, a standard siren for the Hubble constant, and (via pulsar timing) evidence for a nanohertz background likely from supermassive black-hole binaries.

#### Key equations
$$h_{ij}^{TT}=\frac{2G}{c^4r}\ddot Q_{ij}^{TT},\qquad P=\frac{G}{5c^5}\langle\dddot Q_{ij}\dddot Q^{ij}\rangle,\qquad \mathcal M=\frac{(m_1m_2)^{3/5}}{(m_1+m_2)^{1/5}}$$

#### Open problems
- Origin of the PTA background (SMBH binaries vs. cosmological sources).
- Formation channels of merging black holes; black holes in the pair-instability mass gap.

#### Connections
- [Multi-messenger astronomy](knowledge/09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/multi-messenger-astronomy/README.md) · [Hubble tension](knowledge/09-astrophysics-and-cosmology/cosmology/hubble-tension-and-cosmological-tensions/README.md) · [Squeezed light](knowledge/04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology/README.md)

### Space-based and future detectors · `knowledge/05-relativity-and-gravitation/gravitational-waves/space-based-and-future-detectors`

**Scope.** LISA (2.5 Gm arms, mHz band, ESA–NASA, adopted 2024, launch ~2035), TianQin and Taiji, LISA sources (massive-black-hole mergers, extreme-mass-ratio inspirals, Galactic binaries), Einstein Telescope and Cosmic Explorer (×10 sensitivity), DECIGO, atom-interferometer detectors (AION, MAGIS), cosmological backgrounds.

**Core ideas.**
- Different arm lengths target different frequency bands — space removes seismic noise.
- EMRIs map the spacetime of massive black holes with exquisite precision (tests of no-hair).
- 3G detectors would see essentially every stellar-mass binary-black-hole merger in the universe.

**Key equations.**
$$f_{\text{ISCO}}\approx\frac{c^3}{6^{3/2}\pi GM}\approx4.4\ \text{kHz}\left(\frac{M_\odot}{M}\right)$$

**Landmark.** Amaro-Seoane et al. (2017) — see [subfield landmarks](knowledge/05-relativity-and-gravitation/gravitational-waves/README.md).

**See also.** [Atomic clocks and atom interferometry](knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement/README.md)

## Quantum gravity · `knowledge/05-relativity-and-gravitation/quantum-gravity`

#### Overview
GR treated as a quantum field theory is non-renormalizable: it works as an effective theory below the Planck scale but needs a UV completion. Candidate frameworks include string theory (gravitons as closed strings, with AdS/CFT as a non-perturbative definition in some spacetimes), loop quantum gravity (quantized geometry), and asymptotic safety, causal dynamical triangulations and causal sets. No approach yet has decisive experimental support; black-hole thermodynamics and holography act as theoretical consistency tests.

#### Key equations
$$S_{\text{EH}}\to\text{EFT: }\ \mathcal L=\frac{2}{\kappa^2}R+c_1R^2+c_2R_{\mu\nu}R^{\mu\nu}+\cdots,\ \kappa^2=32\pi G;\qquad S=\frac{\text{Area}}{4G\hbar}$$

#### Open problems
- Holography for de Sitter and our (approximately) flat universe.
- Any experimental signature: gravitationally induced entanglement, Lorentz-violation bounds, primordial tensor modes.
- The landscape vs. swampland: which EFTs admit consistent UV completions?

#### Connections
- [Black holes](knowledge/05-relativity-and-gravitation/black-holes/README.md) · [Quantum field theory](knowledge/06-particle-physics/quantum-field-theory/README.md) · [Natural units and the Planck scale](knowledge/00-foundations/units-and-constants/natural-units-and-planck-scale/README.md)

### Holography and AdS/CFT · `knowledge/05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft`

**Scope.** Holographic principle ('t Hooft, Susskind), Maldacena's conjecture (Type IIB on AdS₅×S⁵ ↔ N=4 SYM), GKP–Witten dictionary, large-N and strong coupling, holographic entanglement entropy (Ryu–Takayanagi), quantum error correction in the bulk, AdS/QCD and AdS/CMT applications ($\eta/s=1/4\pi$), SYK model and JT gravity.

**Core ideas.**
- A gravitational theory in $d+1$ dimensions is fully encoded in a non-gravitational QFT in $d$ dimensions.
- Strongly coupled boundary physics ↔ weakly curved classical gravity in the bulk.
- Spacetime geometry emerges from boundary entanglement (RT formula).

**Key equations.**
$$Z_{\text{CFT}}[J]=Z_{\text{grav}}[\phi\to J],\qquad S_A=\frac{\text{Area}(\gamma_A)}{4G_N},\qquad \frac{\eta}{s}=\frac{\hbar}{4\pi k_B}$$

**See also.** [Conformal field theory](knowledge/06-particle-physics/quantum-field-theory/conformal-field-theory/README.md) · [Quark–gluon plasma](knowledge/07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma/README.md) · [Entanglement theory](knowledge/04-quantum-physics/quantum-information-and-computation/entanglement-theory/README.md)

### Other approaches to quantum gravity · `knowledge/05-relativity-and-gravitation/quantum-gravity/other-approaches-to-quantum-gravity`

**Scope.** Weinberg's asymptotic safety and functional RG evidence for a UV fixed point, causal dynamical triangulations and emergent 4D geometry, causal-set theory and the prediction of Λ's magnitude, group field theory, emergent gravity proposals, Penrose–Diósi gravitational collapse, Bose–Marletto–Vedral tests of gravity-mediated entanglement.

**Core ideas.**
- Gravity may be non-perturbatively renormalizable with a non-Gaussian UV fixed point.
- Discrete approaches build spacetime from simplices or causally ordered points; continuum emerges at large scales.
- If two masses become entangled via gravity alone, gravity must be quantum — a tabletop experiment within reach of the 2030s.

**Key equations.**
$$k\frac{dg_N}{dk}=(2+\eta_N)g_N\to g_N^*\neq0\ (\text{UV fixed point})$$

**See also.** [Foundations of QM](knowledge/04-quantum-physics/foundations-of-quantum-mechanics/README.md) · [Renormalization group](knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/renormalization-group/README.md)

### QFT in curved spacetime · `knowledge/05-relativity-and-gravitation/quantum-gravity/qft-in-curved-spacetime`

**Scope.** Non-uniqueness of vacuum, Bogoliubov transformations, particle creation in expanding universes, Unruh effect, Hawking effect, renormalized stress–energy $\langle T_{\mu\nu}\rangle$, semiclassical Einstein equations, trace anomaly, quantum origin of inflationary perturbations, analogue gravity.

**Core ideas.**
- Without a global timelike Killing vector there is no preferred notion of "particle".
- A uniformly accelerated observer sees the Minkowski vacuum as thermal at $T_U=\hbar a/2\pi ck_B$.
- Inflation stretches vacuum fluctuations into the seeds of galaxies.

**Key equations.**
$$T_U=\frac{\hbar a}{2\pi ck_B}\approx4\times10^{-21}\ \text{K}\left(\frac{a}{1\,\text{m s}^{-2}}\right),\qquad G_{\mu\nu}=8\pi G\langle\hat T_{\mu\nu}\rangle$$

**Landmark.** Unruh (1976) — see [subfield landmarks](knowledge/05-relativity-and-gravitation/quantum-gravity/README.md).

**See also.** [Hawking radiation](knowledge/05-relativity-and-gravitation/black-holes/black-hole-thermodynamics-and-hawking-radiation/README.md) · [Inflation](knowledge/09-astrophysics-and-cosmology/cosmology/inflation/README.md)

### String theory · `knowledge/05-relativity-and-gravitation/quantum-gravity/string-theory`

**Scope.** Bosonic and superstrings, critical dimensions (26 and 10), the graviton in the closed-string spectrum, five superstring theories, T- and S-duality, M-theory, D-branes, Calabi–Yau compactification, moduli stabilization and flux vacua, the landscape and swampland conjectures, black-hole microstate counting.

**Core ideas.**
- String vibration modes are particles; one massless spin-2 mode is the graviton — gravity is unavoidable.
- Consistency (anomaly cancellation) fixes spacetime dimension and gauge groups.
- Dualities relate weak and strong coupling and different geometries — all five theories are limits of one M-theory.

**Key equations.**
$$S_{\text{NG}}=-\frac{1}{2\pi\alpha'}\int d^2\sigma\sqrt{-\det\partial_aX^\mu\partial_bX_\mu},\qquad \alpha'm^2=N-1\ (\text{open bosonic string})$$

**See also.** [Supersymmetry](knowledge/06-particle-physics/beyond-the-standard-model/supersymmetry/README.md) · [Extra dimensions](knowledge/06-particle-physics/beyond-the-standard-model/extra-dimensions-and-hierarchy-problem/README.md)

## Special relativity · `knowledge/05-relativity-and-gravitation/special-relativity`

#### Overview
Two postulates — the laws of physics are the same in all inertial frames, and light speed is invariant — force space and time to mix under boosts. The result is Minkowski spacetime with invariant interval $ds^2$, mass–energy equivalence, and a cosmic speed limit. Every relativistic theory (QFT, electrodynamics) is built on it.

#### Key equations
$$t'=\gamma\left(t-\frac{vx}{c^2}\right),\ x'=\gamma(x-vt),\ \gamma=\frac{1}{\sqrt{1-v^2/c^2}};\qquad E^2=(pc)^2+(mc^2)^2$$

#### Connections
- [Relativistic electrodynamics](knowledge/02-electromagnetism-and-optics/electrodynamics/relativistic-electrodynamics/README.md) · [Lie groups (Lorentz/Poincaré)](knowledge/00-foundations/symmetry-and-group-theory/lie-groups-and-representations/README.md)

### Lorentz transformations and spacetime · `knowledge/05-relativity-and-gravitation/special-relativity/lorentz-transformations-and-spacetime`

**Scope.** Postulates, relativity of simultaneity, time dilation and length contraction, invariant interval and proper time, spacetime diagrams and light cones, velocity addition, rapidity, twin and ladder paradoxes, Thomas–Wigner rotation, Doppler effect.

**Core ideas.**
- Events, not places or times, are frame-independent; the interval $-c^2\Delta t^2+\Delta\mathbf x^2$ is invariant.
- Boosts along one axis add rapidities: $\tanh\phi=v/c$.
- Paradoxes dissolve once you track which frame defines simultaneity (the travelling twin changes frames).

**Key equations.**
$$\Delta\tau=\frac{\Delta t}{\gamma},\qquad L=\frac{L_0}{\gamma},\qquad u'=\frac{u-v}{1-uv/c^2},\qquad f_{\text{obs}}=f\sqrt{\frac{1+\beta}{1-\beta}}\ (\text{approaching})$$

**See also.** [Relativistic electrodynamics](knowledge/02-electromagnetism-and-optics/electrodynamics/relativistic-electrodynamics/README.md) · [Tensors](knowledge/00-foundations/mathematical-methods/tensors-and-differential-geometry/README.md)

### Relativistic kinematics and dynamics · `knowledge/05-relativity-and-gravitation/special-relativity/relativistic-kinematics-and-dynamics`

**Scope.** Four-velocity and four-momentum, rest energy, massless particles, invariant mass, two-body decays, threshold energies (fixed target vs. collider), Mandelstam variables, relativistic rockets, hyperbolic motion and Rindler horizons, relativistic force.

**Core ideas.**
- $p^\mu p_\mu=-m^2c^2$ in every frame — compute invariants in the easiest frame.
- Colliding beams beat fixed targets: $\sqrt s\approx\sqrt{2mc^2E}$ vs. $2E$.
- Mass is invariant; "relativistic mass" is an outdated concept.

**Key equations.**
$$s=(p_1+p_2)^2c^2,\qquad E_{\text{th}}=\frac{(\sum m_f)^2-m_1^2-m_2^2}{2m_2}c^2\ (\text{fixed target})$$

**See also.** [Hadron colliders](knowledge/06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc/README.md) · [Cosmic rays (GZK cutoff)](knowledge/09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays/README.md)

### Tests of Lorentz invariance · `knowledge/05-relativity-and-gravitation/special-relativity/tests-of-lorentz-invariance`

**Scope.** Michelson–Morley and Kennedy–Thorndike experiments, Ives–Stilwell time dilation, modern optical-cavity tests, atomic-clock comparisons, the Standard-Model Extension (SME) framework, photon-dispersion bounds from gamma-ray bursts, GW170817 speed-of-gravity bound, CPT tests.

**Core ideas.**
- Lorentz violation is parametrized by background tensor fields coupling to SM particles (SME); thousands of coefficients are bounded.
- Quantum-gravity models might violate Lorentz symmetry at $E\sim E_P$; GRB timing probes energy-dependent light speed.
- GW170817 showed $|c_{\text{gw}}-c|/c\lesssim10^{-15}$.

**Key equations.**
$$v(E)\approx c\left(1\pm\xi\frac{E}{E_P}\right),\qquad \Delta t\approx\xi\frac{\Delta E}{E_P}\frac{D}{c}$$

**Landmark.** Mattingly (2005) — see [subfield landmarks](knowledge/05-relativity-and-gravitation/special-relativity/README.md).

**See also.** [Discrete symmetries and CPT](knowledge/00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt/README.md) · [Gamma-ray bursts](knowledge/09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/gamma-ray-bursts/README.md)


---

# Packet 05-5 (16 records)

{"id": "C2144", "a": "05-relativity-and-gravitation/gravitational-waves/space-based-and-future-detectors", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Atom interferometers: from gravimeters to GW detectors", "kind": "method transfer", "summary": "The light-pulse atom interferometry used in quantum gravimeters and gradiometers is being scaled up into long-baseline gravitational-wave detectors (MAGIS-100, AION) for the 0.1–10 Hz gap between LIGO and LISA. The GW signal is a differential phase between two atom clouds that share the same laser pulses, so the detector is a gradiometer read out like a clock.", "map": "\\Delta\\phi_{\\rm grav}=k_{\\rm eff}\\,g\\,T^2", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2145", "a": "05-relativity-and-gravitation/gravitational-waves/space-based-and-future-detectors", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics", "name": "LISA-style laser ranging weighs the oceans (GRACE-FO)", "kind": "method transfer", "summary": "GRACE Follow-On carries a laser ranging interferometer that flight-tested the heterodyne inter-spacecraft ranging LISA will use. Its nanometre-precision ranging maps time-variable gravity, which measures ocean-bottom pressure, ice-sheet loss and the mass part of sea-level rise; combined with Argo floats it isolates ocean heat uptake.", "map": "\\Delta\\eta_{\\rm sea}=\\Delta\\eta_{\\rm mass}+\\Delta\\eta_{\\rm steric}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2146", "a": "05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft", "b": "11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods", "name": "Tensor networks: DMRG chemistry and MERA holography", "kind": "method transfer", "summary": "Matrix-product-state DMRG is a production quantum-chemistry method for strongly correlated active spaces. Its multiscale relative MERA builds a discrete AdS-like bulk whose minimal cuts give a Ryu–Takayanagi-like entanglement bound, and both methods work because ground-state entanglement obeys area laws.", "map": "S_A=\\frac{\\mathrm{Area}(\\gamma_A)}{4G_N}\\ \\leftrightarrow\\ S_A\\le|\\gamma_A|\\ln\\chi", "breaks": "Molecules lack the scale invariance that makes MERA holographic, and chemical DMRG orders orbitals on a 1D chain rather than building a geometric bulk.", "confidence": "current research", "strength": 1}
{"id": "C2147", "a": "05-relativity-and-gravitation/quantum-gravity/other-approaches-to-quantum-gravity", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Gravity-mediated entanglement with NV-spin masses", "kind": "shared object", "summary": "The Bose–Marletto–Vedral proposal puts two microdiamonds, each carrying an NV-centre spin, into Stern–Gerlach spatial superpositions; if gravity alone entangles the spins, gravity cannot be classical. Whether it is feasible is a quantum-sensing question, set by decoherence, Casimir screening and phase readout with NV spins.", "map": "\\Delta\\phi\\sim\\frac{G m^2\\,\\tau}{\\hbar\\,d}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2148", "a": "05-relativity-and-gravitation/quantum-gravity/qft-in-curved-spacetime", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Circular Unruh effect and storage-ring spin polarization", "kind": "analogy", "summary": "Electrons in storage rings polarize themselves through spin-flip synchrotron radiation (the Sokolov–Ternov effect), but the polarization saturates at 92.4%. Bell and Leinaas reinterpreted the leftover depolarization as the spin being excited by an Unruh-like thermal bath set by the electron's enormous proper acceleration.", "map": "P_{\\max}=\\frac{8}{5\\sqrt3}\\approx92.4\\%,\\qquad T_U=\\frac{\\hbar a}{2\\pi ck_B}", "breaks": "Circular motion is not uniform linear acceleration, so the effective bath is non-thermal and mode-dependent; ordinary QED reproduces the result without invoking Unruh, so it is a reinterpretation, not an independent test.", "confidence": "established", "strength": 2}
{"id": "C2149", "a": "05-relativity-and-gravitation/quantum-gravity/string-theory", "b": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "name": "Rigid strings and fluid membranes share a curvature action", "kind": "identity", "summary": "The Nambu–Goto area term plays the role of surface tension, and Polyakov's extrinsic-curvature term for rigid strings is the Canham–Helfrich bending energy. The one-loop softening of bending rigidity (Peliti–Leibler for membranes) is the same calculation as the asymptotic freedom of Polyakov's rigid string, and the Gaussian-curvature term is topological by Gauss–Bonnet.", "map": "F=\\int dA\\left[\\sigma+\\frac\\kappa2(2H-c_0)^2+\\bar\\kappa K\\right],\\quad \\kappa_R=\\kappa-\\frac{3k_BT}{4\\pi}\\ln\\frac\\ell a", "breaks": "Worldsheets fluctuate quantum-mechanically in a Lorentzian target space, while membranes fluctuate thermally in 3D with fixed area, finite size, cytoskeletal anchoring and active noise.", "confidence": "established", "strength": 2}
{"id": "C2150", "a": "05-relativity-and-gravitation/special-relativity/lorentz-transformations-and-spacetime", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Thomas precession sets the spin tune in storage rings", "kind": "identity", "summary": "Thomas–Wigner rotation, which comes from composing non-collinear boosts, enters the Thomas–BMT equation and gives a spin tune of aγ in a ring. At the magic γ≈29.3 the electric-field term cancels, which the muon g−2 storage rings exploit; the CERN muon ring also confirmed muon time dilation at that γ.", "map": "\\boldsymbol\\omega_a=-\\frac qm\\left[a\\mathbf B-\\left(a-\\frac1{\\gamma^2-1}\\right)\\frac{\\boldsymbol\\beta\\times\\mathbf E}{c}\\right],\\ \\nu_s=a\\gamma", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2151", "a": "05-relativity-and-gravitation/special-relativity/lorentz-transformations-and-spacetime", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Undulator resonance from Lorentz contraction and Doppler", "kind": "identity", "summary": "In the electron rest frame the undulator period is contracted to λu/γ and the electron radiates like a dipole. Transforming back to the lab gives a relativistic Doppler upshift of about 2γ and aberration into a 1/γ cone, which yields the λu/2γ² resonance; the same 4γ² upshift drives inverse-Compton sources.", "map": "\\lambda_1=\\frac{\\lambda_u}{2\\gamma^2}\\left(1+\\frac{K^2}{2}+\\gamma^2\\theta^2\\right),\\quad\\theta\\sim\\frac1\\gamma", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2152", "a": "05-relativity-and-gravitation/special-relativity/relativistic-kinematics-and-dynamics", "b": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "name": "Invariant mass: why colliders beat fixed targets", "kind": "historical", "summary": "The available centre-of-mass energy grows only as √E on a fixed target but as 2E in a head-on collision, which drove the move to colliding-beam storage rings. Threshold kinematics also set machine energies: the Bevatron was built to exceed the 5.6 GeV threshold for producing antiprotons.", "map": "\\sqrt s_{\\rm fixed}\\approx\\sqrt{2Em_tc^2},\\ \\sqrt s_{\\rm coll}=2E;\\quad T_{\\rm th}(pp\\to ppp\\bar p)=6m_pc^2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2153", "a": "05-relativity-and-gravitation/special-relativity/relativistic-kinematics-and-dynamics", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Rigidity, phase slip and transition energy", "kind": "identity", "summary": "Relativistic momentum fixes ring optics through the magnetic rigidity, and longitudinal phase stability depends on the slip factor. Its 1/γ² term makes higher-momentum particles arrive early below the transition energy and late above it, and space-charge forces fall as 1/γ² because magnetic attraction cancels electric repulsion.", "map": "B\\rho=\\frac pq,\\quad \\eta=\\alpha_c-\\frac1{\\gamma^2},\\quad \\gamma_t=\\frac1{\\sqrt{\\alpha_c}},\\quad F_{\\rm sc}\\propto\\frac1{\\gamma^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2154", "a": "05-relativity-and-gravitation/special-relativity/relativistic-kinematics-and-dynamics", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Kane two-band model as a semirelativistic Dirac analogue", "kind": "analogy", "summary": "In narrow-gap semiconductors (InSb, HgCdTe) the two-band k·p dispersion is a hyperbola with the same form as E²=m²c⁴+p²c²: half the band gap plays the role of mc², and a band speed u≈10⁶ m/s plays the role of c. This governs the band nonparabolicity and energy-dependent effective mass in infrared detectors and high-mobility transistors.", "map": "\\left(E+\\tfrac{E_g}2\\right)^2=\\left(\\tfrac{E_g}2\\right)^2+u^2\\hbar^2k^2,\\ u=\\sqrt{\\tfrac{E_g}{2m^*}}\\ \\leftrightarrow\\ \\varepsilon^2=m^2c^4+p^2c^2", "breaks": "The limiting speed is a material band parameter, the lattice breaks Lorentz invariance, and remote bands spoil the hyperbola away from the zone centre.", "confidence": "established", "strength": 1}
{"id": "C2155", "a": "05-relativity-and-gravitation/special-relativity/relativistic-kinematics-and-dynamics", "b": "11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods", "name": "Relativistic effects in heavy-element chemistry", "kind": "mechanism", "summary": "Inner electrons of heavy atoms move at v≈Zαc, so relativistic effects contract and stabilize s orbitals and expand d orbitals. This explains gold's colour, liquid mercury and about 1.7 V of the lead-acid cell's 2.1 V; quantum chemistry handles it with Dirac–Coulomb, Douglas–Kroll–Hess or ZORA Hamiltonians, or with relativistic pseudopotentials.", "map": "\\frac{v_{1s}}{c}\\approx Z\\alpha,\\quad \\frac{\\langle r\\rangle_{\\rm rel}}{\\langle r\\rangle_{\\rm nr}}\\approx\\sqrt{1-(Z\\alpha)^2}\\ (\\text{Au: }\\approx0.82)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2156", "a": "05-relativity-and-gravitation/special-relativity/relativistic-kinematics-and-dynamics", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "PET images mass-energy equivalence", "kind": "identity", "summary": "When a positron and an electron annihilate nearly at rest, their rest energy 2mec² becomes two 511 keV photons, emitted back-to-back by momentum conservation, which defines PET's line of response. The residual momentum of positronium blurs this by about 0.5° of acollinearity, and time-of-flight PET locates the event along the line using Δx = cΔt/2.", "map": "E_\\gamma=m_ec^2=511\\ \\text{keV},\\quad \\delta\\theta\\approx\\frac{p_\\perp}{m_ec},\\quad \\Delta x=\\frac{c\\,\\Delta t}{2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2157", "a": "05-relativity-and-gravitation/special-relativity/relativistic-kinematics-and-dynamics", "b": "11-interdisciplinary-physics/medical-physics/radiation-therapy", "name": "Relativistic Bethe stopping power and the Bragg peak", "kind": "mechanism", "summary": "Therapeutic protons (70–250 MeV, β≈0.37–0.61) lose energy according to the relativistic Bethe formula. The 1/β² rise as they slow down produces the Bragg peak, so range–energy tables and proton treatment planning rely on the relativistic relation between momentum and energy.", "map": "-\\frac{dE}{dx}\\propto\\frac{z^2}{\\beta^2}\\left[\\ln\\frac{2m_ec^2\\beta^2\\gamma^2}{I}-\\beta^2\\right]", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C2158", "a": "05-relativity-and-gravitation/special-relativity/tests-of-lorentz-invariance", "b": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "name": "Storage rings as Lorentz-invariance laboratories", "kind": "method transfer", "summary": "Accelerators provide fast, well-controlled clocks and photon beams. Ives–Stilwell spectroscopy of electron-cooled Li+ ions at β≈0.34 in the GSI storage ring tested time dilation at about the 1e-8 level, Compton-edge measurements at ESRF bounded light-speed anisotropy, and LEP synchrotron radiation limits Lorentz-violating coefficients for electrons.", "map": "\\frac{\\nu_p\\nu_a}{\\nu_0^2}=1\\ \\ (\\text{Ives–Stilwell, exact in SR})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2159", "a": "05-relativity-and-gravitation/special-relativity/tests-of-lorentz-invariance", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Clock comparisons and comagnetometers bound the SME", "kind": "method transfer", "summary": "In the Standard-Model Extension, Lorentz violation appears as orientation-dependent energy shifts that oscillate at the sidereal frequency as Earth rotates. Atomic-clock comparisons and spin comagnetometers (He–Xe, K–He SERF) are quantum sensors, and they set the tightest limits on the SME coefficients for matter.", "map": "\\delta\\nu(T)\\propto\\tilde b_{\\perp}\\cos(\\omega_\\oplus T+\\varphi)", "breaks": "", "confidence": "established", "strength": 2}