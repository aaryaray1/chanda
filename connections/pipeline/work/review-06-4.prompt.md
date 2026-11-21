You are the particle-physicist, the specialist for 06 (Particle Physics) in this physics knowledge base.

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

## Field overview · `knowledge/06-particle-physics`

> **Specialist:** `particle-physicist` · **arXiv:** hep-ph, hep-ex, hep-th, hep-lat · **Literature source:** INSPIRE-HEP (citation-ranked) + arXiv (latest)

#### What this field studies
Particle physics asks what the smallest constituents of matter are and how they interact. The working answer is the **Standard Model (SM)**: a relativistic quantum field theory with gauge group $SU(3)_c\times SU(2)_L\times U(1)_Y$, three generations of quarks and leptons, and a Higgs field whose vacuum expectation value breaks electroweak symmetry. The SM has passed every collider test, but it leaves out gravity, dark matter, neutrino masses (in its minimal form), the matter–antimatter asymmetry and an explanation of its ~19 free parameters. The field is therefore split between **precision tests** of the SM and **searches** for what lies beyond it.

#### Conventions used in this branch
- **Natural units** $\hbar=c=1$; energies in GeV. Restore with $\hbar c = 197.327$ MeV·fm and $\hbar = 6.582\times10^{-25}$ GeV·s.
- **Metric signature** $(+,-,-,-)$ (particle-physics convention). State it explicitly when comparing with GR texts that use $(-,+,+,+)$.
- Cross sections in barns: $1\ \text{pb} = 10^{-36}\ \text{cm}^2$; luminosity in fb$^{-1}$.
- Discovery threshold "5σ" ≈ one-sided p-value $2.9\times10^{-7}$; "evidence" is 3σ.

#### Historical spine
1897 electron (Thomson) · 1911 nucleus (Rutherford) · 1928 Dirac equation · 1932 positron, neutron · 1947–49 QED renormalized (Feynman, Schwinger, Tomonaga, Dyson) · 1956 neutrino detected; parity violation (Lee–Yang, Wu) · 1961–67 electroweak theory (Glashow, Weinberg, Salam) · 1964 quarks (Gell-Mann, Zweig), Higgs mechanism, CP violation · 1973 asymptotic freedom; neutral currents · 1974 J/ψ · 1983 W, Z · 1995 top quark · 1998 neutrino oscillations · 2012 Higgs boson · 2015 LHCb pentaquarks.

#### Canonical textbooks
- Griffiths, *Introduction to Elementary Particles* — undergraduate entry point.
- Thomson, *Modern Particle Physics* — experiment-facing undergraduate/graduate text.
- Peskin & Schroeder, *An Introduction to Quantum Field Theory* — the standard graduate QFT course.
- Schwartz, *Quantum Field Theory and the Standard Model* — modern, phenomenology-heavy.
- Weinberg, *The Quantum Theory of Fields* (3 vols.) — foundational and rigorous.
- Particle Data Group, *Review of Particle Physics* (pdg.lbl.gov) — the reference for every measured number.

#### Live frontiers
- Higgs self-coupling and the shape of the Higgs potential (HL-LHC).
- Neutrino mass ordering and leptonic CP phase (DUNE, Hyper-K, JUNO).
- Muon $g-2$: experiment vs. lattice vs. data-driven hadronic vacuum polarization.
- Dark matter: WIMPs squeezed by xenon experiments; axion searches broadening.
- Next collider choice: FCC-ee, muon collider, linear colliders.

#### How the specialist works here
Start from symmetry and power counting, compute at the lowest order that captures the effect, quote numbers from the PDG, and separate "measured", "SM prediction", and "model-dependent" claims. Use INSPIRE citation counts to find the canonical paper on any topic.

## Beyond the Standard Model · `knowledge/06-particle-physics/beyond-the-standard-model`

#### Overview
The SM is incomplete: it has no dark-matter candidate, no mechanism for the baryon asymmetry, no gravity, no explanation for tiny neutrino masses or the strong-CP problem, and an unexplained hierarchy between the electroweak and Planck scales. BSM physics proposes solutions; experiment (LHC, flavor, EDMs, dark-matter detectors, cosmology) constrains them. Since 2012 the LHC has found no new particles, pushing simple natural SUSY and many composite models to multi-TeV scales.

#### Conceptual spine
1. Identify an SM shortcoming → postulate new symmetry/particles → derive low-energy signatures → confront collider, flavor, astrophysical and cosmological bounds.
2. EFT (SMEFT) gives a model-independent bridge between heavy new physics and precision data.
3. "Naturalness" arguments predict new physics near the TeV scale — the LHC's null results are forcing a re-think.

#### Key equations
$$\delta m_h^2\sim\frac{3y_t^2}{8\pi^2}\Lambda^2\quad(\text{top-loop hierarchy problem}),\qquad m_a\simeq5.7\,\mu\text{eV}\left(\frac{10^{12}\,\text{GeV}}{f_a}\right)$$

#### Open problems
- Is the electroweak scale natural, and if so, where is the new physics?
- What is dark matter? (WIMP, axion, sterile neutrino, primordial black hole, something else)
- What generated the baryon asymmetry $\eta_B\approx6\times10^{-10}$?

#### Connections
- [Dark matter (astrophysics)](knowledge/09-astrophysics-and-cosmology/dark-matter/README.md) · [Cosmology](knowledge/09-astrophysics-and-cosmology/cosmology/README.md) · [String theory](knowledge/05-relativity-and-gravitation/quantum-gravity/string-theory/README.md)

### Axions and the light dark sector · `knowledge/06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector`

**Scope.** Peccei–Quinn mechanism, KSVZ and DFSZ models, misalignment production, haloscopes (ADMX, HAYSTAC), helioscopes (CAST, IAXO), light-shining-through-walls, astrophysical bounds (SN 1987A, stellar cooling), dark photons and kinetic mixing.

**Core ideas.**
- Promote $\theta$ to a dynamical field whose potential relaxes it to zero — the axion is the pseudo-Goldstone boson.
- Coupling to photons $g_{a\gamma\gamma}aF\tilde F$ lets a magnetic field convert axions to photons (resonant cavities).
- Misalignment produces cold axion dark matter for $f_a\sim10^{11\text{–}12}$ GeV, i.e. $m_a\sim\mu$eV.

**Key equations.**
$$\mathcal L\supset\frac{a}{f_a}\frac{g_s^2}{32\pi^2}G\tilde G-\frac{g_{a\gamma\gamma}}{4}aF_{\mu\nu}\tilde F^{\mu\nu}$$

**See also.** [Anomalies and instantons](knowledge/06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology/README.md) · [Direct detection](knowledge/09-astrophysics-and-cosmology/dark-matter/direct-detection/README.md)

### Baryogenesis and the matter–antimatter asymmetry · `knowledge/06-particle-physics/beyond-the-standard-model/baryogenesis-and-matter-antimatter`

**Scope.** Sakharov conditions, sphaleron processes, electroweak baryogenesis and the order of the electroweak phase transition, thermal leptogenesis from heavy Majorana neutrinos, Affleck–Dine mechanism, measurements of $\eta_B$ from BBN and the CMB.

**Core ideas.**
- Need (1) baryon-number violation, (2) C and CP violation, (3) departure from equilibrium.
- In the SM the electroweak transition is a crossover (for $m_h=125$ GeV) and CKM CP violation is too weak — so baryogenesis requires new physics.
- Leptogenesis: CP-violating decays of heavy neutrinos create a lepton asymmetry that sphalerons partially convert to baryons.

**Key equations.**
$$\eta_B=\frac{n_B-n_{\bar B}}{n_\gamma}=(6.1\pm0.1)\times10^{-10},\qquad \Delta B=\Delta L=3\ \text{per sphaleron}$$

**Landmark.** Sakharov (1967; reprinted 1991). "Violation of CP invariance, C asymmetry, and baryon asymmetry of the universe". *Sov. Phys. Usp.* 34, 392. [doi:10.1070/PU1991v034n05ABEH002497](https://doi.org/10.1070/PU1991v034n05ABEH002497)

**See also.** [CP violation](knowledge/06-particle-physics/standard-model/cp-violation/README.md) · [Big Bang nucleosynthesis](knowledge/07-nuclear-physics/nuclear-astrophysics/big-bang-nucleosynthesis/README.md)

### Dark-matter particle candidates · `knowledge/06-particle-physics/beyond-the-standard-model/dark-matter-particle-candidates`

**Scope.** Thermal freeze-out and the "WIMP miracle", freeze-in, asymmetric dark matter, sterile-neutrino DM, axion DM, ultralight (fuzzy) DM, primordial black holes, collider/direct/indirect complementarity.

**Core ideas.**
- Freeze-out gives $\Omega h^2\approx0.12$ when $\langle\sigma v\rangle\approx3\times10^{-26}$ cm³/s — roughly weak-scale cross sections.
- Candidates span ~90 orders of magnitude in mass ($10^{-22}$ eV fuzzy DM to $\sim M_\odot$ PBHs).
- Each mechanism predicts distinct signatures: nuclear recoils, annihilation products, structure suppression, lensing.

**Key equations.**
$$\Omega_\chi h^2\approx\frac{3\times10^{-27}\,\text{cm}^3\,\text{s}^{-1}}{\langle\sigma v\rangle}$$

**Landmark.** Bertone, Hooper & Silk (2005) — see [subfield landmarks](knowledge/06-particle-physics/beyond-the-standard-model/README.md).

**See also.** [Astrophysical evidence for dark matter](knowledge/09-astrophysics-and-cosmology/dark-matter/astrophysical-evidence-for-dark-matter/README.md) · [Supersymmetry](knowledge/06-particle-physics/beyond-the-standard-model/supersymmetry/README.md)

### Extra dimensions and the hierarchy problem · `knowledge/06-particle-physics/beyond-the-standard-model/extra-dimensions-and-hierarchy-problem`

**Scope.** The gauge hierarchy problem, large extra dimensions (ADD), warped geometry (RS1), Kaluza–Klein towers, composite Higgs, relaxion, anthropic/landscape views, short-distance gravity tests.

**Core ideas.**
- With $n$ compact dimensions of size $R$, $M_{\text{Pl}}^2\sim M_*^{n+2}R^n$, so a TeV-scale fundamental gravity scale is possible.
- In RS, an exponential warp factor $e^{-kr_c\pi}$ generates the hierarchy from $\mathcal O(10)$ parameters.
- Signatures: KK gravitons, deviations from $1/r^2$ gravity at sub-mm scales.

**Key equations.**
$$ds^2=e^{-2k|y|}\eta_{\mu\nu}dx^\mu dx^\nu+dy^2,\qquad m_{\text{TeV}}=e^{-kr_c\pi}M_{\text{Pl}}$$

**See also.** [String theory](knowledge/05-relativity-and-gravitation/quantum-gravity/string-theory/README.md) · [Tests of general relativity](knowledge/05-relativity-and-gravitation/general-relativity/tests-of-general-relativity/README.md)

### Grand unification and proton decay · `knowledge/06-particle-physics/beyond-the-standard-model/grand-unification-and-proton-decay`

**Scope.** SU(5) (Georgi–Glashow), SO(10) with right-handed neutrinos, Pati–Salam, charge quantization, running-coupling unification, doublet–triplet splitting, proton-decay channels and Super-Kamiokande limits, magnetic monopoles.

**Core ideas.**
- A single gauge group explains why quark and lepton charges are commensurate ($Q_p=-Q_e$ exactly).
- Couplings nearly meet at $\sim10^{15\text{–}16}$ GeV; with SUSY the meeting is much better.
- Heavy $X,Y$ bosons mediate $p\to e^+\pi^0$; Super-K's $\tau_p>2.4\times10^{34}$ yr rules out minimal SU(5).

**Key equations.**
$$\tau_p\sim\frac{M_X^4}{\alpha_G^2m_p^5}$$

**Landmark.** Georgi & Glashow (1974) — see [subfield landmarks](knowledge/06-particle-physics/beyond-the-standard-model/README.md).

**See also.** [Lie groups](knowledge/00-foundations/symmetry-and-group-theory/lie-groups-and-representations/README.md) · [Running couplings](knowledge/06-particle-physics/quantum-field-theory/renormalization-and-running-couplings/README.md)

### Supersymmetry · `knowledge/06-particle-physics/beyond-the-standard-model/supersymmetry`

**Scope.** SUSY algebra, superfields, the MSSM spectrum (squarks, sleptons, gauginos, higgsinos), soft breaking, R-parity, neutralino dark matter, gauge-coupling unification, simplified-model LHC limits, split and natural SUSY.

**Core ideas.**
- Each SM particle gets a superpartner differing by spin ½; boson and fermion loops cancel the quadratic Higgs-mass sensitivity.
- Unbroken SUSY would mean degenerate partners, so it must be broken — "softly", to preserve the cancellation.
- With R-parity the lightest superpartner is stable: a classic WIMP.
- LHC bounds push gluinos/first-generation squarks above ~2 TeV, creating tension with naturalness.

**Key equations.**
$$\{Q_\alpha,\bar Q_{\dot\beta}\}=2\sigma^\mu_{\alpha\dot\beta}P_\mu,\qquad m_h^2\le m_Z^2\cos^22\beta+\text{loops}\ (\text{MSSM})$$

**Landmark.** Martin, "A Supersymmetry Primer" — see [subfield landmarks](knowledge/06-particle-physics/beyond-the-standard-model/README.md).

**See also.** [Grand unification](knowledge/06-particle-physics/beyond-the-standard-model/grand-unification-and-proton-decay/README.md) · [String theory](knowledge/05-relativity-and-gravitation/quantum-gravity/string-theory/README.md)

## Collider and experimental particle physics · `knowledge/06-particle-physics/collider-and-experimental-particle-physics`

#### Overview
Experimental particle physics turns collisions into measurements: accelerators deliver beams, detectors record charged tracks and calorimeter deposits, triggers select ~1 in $10^5$ events, and reconstruction plus simulation turn raw hits into physics objects (electrons, muons, jets, missing energy). The LHC (13.6 TeV, Run 3; HL-LHC from ~2030) dominates the energy frontier.

#### Conceptual spine
1. Event rate $=\sigma\times\mathcal L$; integrated luminosity sets statistics.
2. Factorization: $\sigma_{pp\to X}=\sum_{ij}\int f_i f_j\,\hat\sigma_{ij\to X}$ (PDFs × partonic cross section).
3. Reconstruction → selection → background estimation (data-driven where possible) → statistical inference (profile likelihood, CLs).
4. Blind analyses and look-elsewhere corrections guard against false discoveries.

#### Key equations
$$N=\sigma\int\mathcal L\,dt,\qquad \sigma_{pp\to X}=\sum_{i,j}\int dx_1dx_2\,f_i(x_1,\mu_F)f_j(x_2,\mu_F)\,\hat\sigma_{ij\to X}(\hat s,\mu_R)$$

#### Open problems
- Pile-up of ~200 collisions per crossing at HL-LHC; real-time triggering with ML on FPGAs.
- Theory uncertainties (PDFs, higher orders) now rival experimental ones for precision Higgs and EW measurements.

#### Connections
- [Accelerator physics](knowledge/11-interdisciplinary-physics/accelerator-physics/README.md) · [Statistical inference](knowledge/00-foundations/measurement-and-data-analysis/statistical-inference-in-physics/README.md) · [Detectors and instrumentation](knowledge/00-foundations/measurement-and-data-analysis/detectors-and-instrumentation/README.md)

### Hadron colliders and the LHC · `knowledge/06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc`

**Scope.** LHC ring (27 km, 8.3 T dipoles), $\sqrt s$ = 7, 8, 13, 13.6 TeV, experiments (ATLAS, CMS, LHCb, ALICE), luminosity and pile-up, HL-LHC upgrade (3000 fb⁻¹), Tevatron legacy (top quark discovery).

**Core ideas.**
- Protons are composite, so the partonic collision energy varies event-by-event; most collisions are soft QCD.
- Discovery reach is set by parton luminosities that fall steeply with mass.
- General-purpose detectors (ATLAS/CMS) vs. specialized (LHCb forward flavor, ALICE heavy ions).

**Key equations.**
$$\mathcal L=\frac{f\,n_b\,N_1N_2}{4\pi\sigma_x\sigma_y}F,\qquad \hat s=x_1x_2s$$

**See also.** [Higgs boson](knowledge/06-particle-physics/standard-model/higgs-boson/README.md) · [Beam dynamics](knowledge/11-interdisciplinary-physics/accelerator-physics/beam-dynamics/README.md)

### Particle detectors and triggers · `knowledge/06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers`

**Scope.** Energy loss (Bethe–Bloch), multiple scattering, radiation length, electromagnetic and hadronic showers, silicon pixel/strip trackers, sampling vs. homogeneous calorimeters, RICH detectors, muon spectrometers, timing detectors (4D tracking), radiation hardness, multi-level triggers.

**Core ideas.**
- Momentum from track curvature: $p_T[\text{GeV}]=0.3\,B[\text{T}]\,R[\text{m}]$.
- Calorimeter resolution $\sigma_E/E=a/\sqrt E\oplus b\oplus c/E$ (stochastic, constant, noise).
- Particle identity from combined signatures: $e$ (track + EM shower), $\gamma$ (EM shower, no track), $\mu$ (penetrates), jets, missing $E_T$ (neutrinos/new particles).

**Key equations.**
$$-\left\langle\frac{dE}{dx}\right\rangle=Kz^2\frac{Z}{A}\frac{1}{\beta^2}\left[\tfrac12\ln\frac{2m_ec^2\beta^2\gamma^2T_{\max}}{I^2}-\beta^2-\frac{\delta(\beta\gamma)}{2}\right]$$

**See also.** [Detectors and instrumentation](knowledge/00-foundations/measurement-and-data-analysis/detectors-and-instrumentation/README.md) · [Radiation detection](knowledge/07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry/README.md)

## Neutrino physics · `knowledge/06-particle-physics/neutrino-physics`

#### Overview
Neutrinos were massless in the original Standard Model. Oscillation experiments since 1998 prove that at least two have mass, which makes neutrino mass the first laboratory evidence for physics beyond the minimal SM. We know the two mass-squared splittings and three mixing angles well; we do not know the absolute mass scale, the mass ordering, the leptonic CP phase, or whether neutrinos are their own antiparticles.

#### Conceptual spine
1. Flavor states $|\nu_\alpha\rangle=\sum_iU^*_{\alpha i}|\nu_i\rangle$ (PMNS matrix).
2. Different masses → relative phases $\Delta m^2_{ij}L/2E$ → oscillation.
3. Matter potential $V=\sqrt2G_Fn_e$ for $\nu_e$ (MSW effect) explains solar neutrinos and gives mass-ordering sensitivity.
4. Mass generation: Dirac Yukawa (tiny couplings) or Majorana mass via seesaw $m_\nu\sim y^2v^2/M$.

#### Key equations
$$\Delta m^2_{21}\approx7.4\times10^{-5}\,\text{eV}^2,\qquad |\Delta m^2_{31}|\approx2.5\times10^{-3}\,\text{eV}^2$$
$$m_{\beta\beta}=\Big|\sum_i U_{ei}^2m_i\Big|,\qquad m_\beta^2=\sum_i|U_{ei}|^2m_i^2$$

#### Open problems
- Normal vs. inverted mass ordering; value of $\delta_{CP}$; octant of $\theta_{23}$.
- Majorana or Dirac? Only $0\nu\beta\beta$ can tell in practice.
- Tension between cosmological bounds on $\sum m_\nu$ and oscillation minimum (~0.06 eV) as surveys tighten.

#### Connections
- [Big Bang nucleosynthesis](knowledge/07-nuclear-physics/nuclear-astrophysics/big-bang-nucleosynthesis/README.md) · [Neutrino astronomy](knowledge/09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/neutrino-astronomy/README.md) · [Beta decay](knowledge/07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions/README.md)

### Neutrino experiments and sources · `knowledge/06-particle-physics/neutrino-physics/neutrino-experiments-and-sources`

**Scope.** Radiochemical (Homestake, GALLEX/SAGE), water Cherenkov (Super-K, Hyper-K), heavy water (SNO), liquid scintillator (KamLAND, Borexino, JUNO), liquid-argon TPCs (DUNE, MicroBooNE), coherent elastic $\nu$-nucleus scattering (COHERENT), SN 1987A, geoneutrinos, CNO solar neutrinos (Borexino 2020).

**Core ideas.**
- Cross sections are tiny ($\sigma\sim10^{-44}$ cm² at MeV), so detectors are huge and deep underground.
- The solar neutrino problem (1968–2002) was solved by flavor conversion, not by solar-model error.
- Accelerator beams allow controlled $\nu_\mu\to\nu_e$ appearance studies of CP violation.

**Key equations.**
$$\bar\nu_e+p\to e^++n\quad(\text{inverse beta decay, threshold }1.8\text{ MeV})$$

**See also.** [Stellar structure (pp chain)](knowledge/09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution/README.md) · [Cherenkov radiation](knowledge/02-electromagnetism-and-optics/radiation-and-scattering/cherenkov-and-transition-radiation/README.md)

### Neutrino mass and neutrinoless double-beta decay · `knowledge/06-particle-physics/neutrino-physics/neutrino-mass-and-double-beta-decay`

**Scope.** Tritium endpoint (KATRIN, Project 8), cosmological $\sum m_\nu$ bounds (Planck, DESI), $0\nu\beta\beta$ searches (KamLAND-Zen, GERDA/LEGEND, CUORE, nEXO), nuclear matrix elements, seesaw mechanisms.

**Core ideas.**
- Kinematic measurements are model-independent but limited to $m_\beta\lesssim0.2$ eV.
- $0\nu\beta\beta$ ($(A,Z)\to(A,Z+2)+2e^-$) violates lepton number by two units and requires Majorana mass; its rate depends on $m_{\beta\beta}$ and a poorly known nuclear matrix element.
- Seesaw: a heavy right-handed Majorana mass $M$ gives $m_\nu\approx m_D^2/M$, naturally tiny.

**Key equations.**
$$\left(T^{0\nu}_{1/2}\right)^{-1}=G^{0\nu}\,|M^{0\nu}|^2\,\frac{m_{\beta\beta}^2}{m_e^2}$$

**Landmark.** KATRIN (2022) — see [subfield landmarks](knowledge/06-particle-physics/neutrino-physics/README.md).

**See also.** [Beta decay](knowledge/07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions/README.md) · [CMB](knowledge/09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background/README.md)

### Neutrino oscillations · `knowledge/06-particle-physics/neutrino-physics/neutrino-oscillations`

**Scope.** Two- and three-flavor oscillation formalism, PMNS parametrization, MSW resonance, solar/atmospheric/reactor/accelerator oscillation data, global fits, mass ordering and $\delta_{CP}$ sensitivity (T2K, NOvA, DUNE, Hyper-K, JUNO).

**Core ideas.**
- Oscillation needs non-degenerate masses and non-trivial mixing; it measures $\Delta m^2$, never absolute masses.
- Oscillation phase scales as $L/E$, setting experiment baselines (reactor ~1 km for $\Delta m^2_{31}$, ~50 km for $\Delta m^2_{21}$).
- In matter, $\nu_e$ forward scattering on electrons shifts effective masses; the adiabatic MSW conversion explains the energy dependence of solar $\nu_e$ survival.

**Key equations.**
$$P(\nu_\alpha\to\nu_\beta)\big|_{2\nu}=\sin^22\theta\,\sin^2\!\left(\frac{1.267\,\Delta m^2[\text{eV}^2]\,L[\text{km}]}{E[\text{GeV}]}\right)$$

**Open questions.** Mass ordering (JUNO, DUNE); $\delta_{CP}$ — T2K and NOvA hint at large CP violation but are not yet decisive.

**See also.** [Neutrino experiments](knowledge/06-particle-physics/neutrino-physics/neutrino-experiments-and-sources/README.md) · [Quantum superposition and decoherence](knowledge/04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical/README.md)

### Sterile neutrinos and anomalies · `knowledge/06-particle-physics/neutrino-physics/sterile-neutrinos-and-anomalies`

**Scope.** LSND and MiniBooNE $\nu_e$ appearance excesses, reactor antineutrino anomaly, gallium anomaly (BEST), MicroBooNE results, 3+1 global fits and appearance/disappearance tension, keV sterile neutrinos as warm dark matter.

**Core ideas.**
- A sterile state with $\Delta m^2\sim1$ eV² would cause short-baseline oscillations.
- Appearance and disappearance data are mutually inconsistent in simple 3+1 models; improved reactor flux calculations removed much of the reactor anomaly.
- Heavy sterile neutrinos are natural in seesaw models and could drive leptogenesis.

**Key equations.**
$$P_{\mu e}^{\text{SBL}}\approx4|U_{e4}|^2|U_{\mu4}|^2\sin^2\!\left(\frac{\Delta m^2_{41}L}{4E}\right)$$

**Open questions.** Origin of the MiniBooNE low-energy excess; persistent gallium deficit.

**See also.** [Dark matter candidates](knowledge/06-particle-physics/beyond-the-standard-model/dark-matter-particle-candidates/README.md)

## Quantum field theory · `knowledge/06-particle-physics/quantum-field-theory`

#### Overview
Quantum field theory (QFT) unifies quantum mechanics and special relativity: particles are excitations of fields, and particle number is not conserved. It is the language of the Standard Model, of critical phenomena in statistical physics, and of most of condensed-matter theory. The modern view (Wilson) treats every QFT as an **effective theory** valid below some cutoff, with the renormalization group describing how couplings change with scale.

#### Conceptual spine
1. Fields → canonical commutators or path integral $Z=\int\mathcal{D}\phi\,e^{iS[\phi]}$.
2. Correlation functions → LSZ reduction → S-matrix → cross sections.
3. Loops diverge → regularize (dimensional regularization) → renormalize → couplings run.
4. Gauge invariance fixes interactions; quantization needs gauge fixing and ghosts (Faddeev–Popov).
5. Non-perturbative physics (confinement, instantons, phase transitions) needs lattice, dualities, or bootstrap.

#### Key equations
$$\mathcal{L}_{\text{QED}} = \bar\psi(i\gamma^\mu D_\mu - m)\psi - \tfrac14 F_{\mu\nu}F^{\mu\nu},\qquad D_\mu=\partial_\mu+ieA_\mu$$
$$\mu\frac{dg}{d\mu}=\beta(g),\qquad \beta_{\text{YM}}(g) = -\frac{g^3}{16\pi^2}\left(\frac{11}{3}C_A-\frac{4}{3}T_F n_f\right)+\mathcal{O}(g^5)$$

#### Open problems
- Rigorous construction of 4D interacting QFTs; the Yang–Mills mass gap (Clay problem).
- Why does the Higgs mass not run to the cutoff (naturalness)?
- Classifying QFTs: which conformal theories exist, and how are they connected by RG flows?

#### Connections
- Statistical field theory and critical phenomena: [Renormalization group](knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/README.md)
- QFT in curved spacetime and holography: [Quantum gravity](knowledge/05-relativity-and-gravitation/quantum-gravity/README.md)
- Many-body field theory: [Strongly correlated electrons](knowledge/08-condensed-matter/strongly-correlated-electrons/README.md)

### Anomalies, instantons and topology · `knowledge/06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology`

**Scope.** Adler–Bell–Jackiw anomaly, $\pi^0\to\gamma\gamma$, gauge-anomaly cancellation in the SM, 't Hooft anomaly matching, instantons, $\theta$ vacua and the strong-CP problem, sphalerons, generalized (higher-form) symmetries.

**Core ideas.**
- A symmetry of the classical action can fail to be a symmetry of the path-integral measure (Fujikawa).
- Gauge anomalies must cancel for consistency — in the SM, quark and lepton charges cancel generation by generation.
- Instantons are finite-action Euclidean solutions labelled by an integer winding number; they make $\theta F\tilde F$ physical.

**Key equations.**
$$\partial_\mu j^\mu_5 = \frac{e^2}{16\pi^2}\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma},\qquad \Gamma(\pi^0\to\gamma\gamma)=\frac{\alpha^2m_\pi^3}{64\pi^3f_\pi^2}$$

**Landmark.** Adler (1969). "Axial-Vector Vertex in Spinor Electrodynamics". *Phys. Rev.* 177, 2426. [doi:10.1103/PhysRev.177.2426](https://doi.org/10.1103/PhysRev.177.2426)

**See also.** [Axions](knowledge/06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector/README.md) · [Topological insulators](knowledge/08-condensed-matter/topological-matter/topological-insulators/README.md)

### Canonical and path-integral quantization · `knowledge/06-particle-physics/quantum-field-theory/canonical-and-path-integral-quantization`

**Scope.** Free and interacting scalar, spinor and vector fields; Fock space; propagators; generating functionals; Wick rotation to Euclidean space.

**Core ideas.**
- Canonical: impose $[\phi(\mathbf x),\pi(\mathbf y)]=i\delta^3(\mathbf x-\mathbf y)$; expand in creation/annihilation operators; fermions use anticommutators (spin–statistics theorem).
- Path integral: $Z[J]=\int\mathcal D\phi\,e^{i\int(\mathcal L+J\phi)}$; correlators are functional derivatives of $Z[J]$; connected diagrams come from $\ln Z$.
- Wick rotation $t\to -i\tau$ maps QFT to statistical field theory — the bridge to lattice methods and critical phenomena.

**Key equations.**
$$\langle 0|T\phi(x)\phi(y)|0\rangle = \int\frac{d^4p}{(2\pi)^4}\frac{i\,e^{-ip\cdot(x-y)}}{p^2-m^2+i\epsilon}$$

**Open questions.** Mathematical definition of the interacting path-integral measure in four dimensions.

**See also.** [Path integrals in QM](knowledge/04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics/README.md) · [Lattice field theory](knowledge/06-particle-physics/quantum-field-theory/lattice-field-theory/README.md)

### Conformal field theory · `knowledge/06-particle-physics/quantum-field-theory/conformal-field-theory`

**Scope.** Conformal group, primary operators, operator product expansion (OPE), 2D CFT and the Virasoro algebra, central charge, minimal models, the numerical conformal bootstrap, CFTs at critical points and as endpoints of RG flows.

**Core ideas.**
- RG fixed points are scale invariant and (usually) conformally invariant; their data (dimensions $\Delta_i$, OPE coefficients) define the theory.
- In 2D the conformal algebra is infinite-dimensional, so many CFTs are exactly solvable.
- Crossing symmetry plus unitarity bounds carve out allowed CFT data — the bootstrap gave the most precise 3D Ising exponents.

**Key equations.**
$$\langle\mathcal O(x)\mathcal O(0)\rangle=\frac{1}{|x|^{2\Delta}},\qquad [L_m,L_n]=(m-n)L_{m+n}+\frac{c}{12}m(m^2-1)\delta_{m+n,0}$$

**Landmark.** Belavin, Polyakov & Zamolodchikov (1984). "Infinite conformal symmetry in two-dimensional quantum field theory". *Nucl. Phys. B* 241, 333. [doi:10.1016/0550-3213(84)90052-X](https://doi.org/10.1016/0550-3213(84)90052-X)

**See also.** [Holography and AdS/CFT](knowledge/05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft/README.md) · [Critical exponents](knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/critical-exponents-and-universality/README.md)

### Effective field theory · `knowledge/06-particle-physics/quantum-field-theory/effective-field-theory`

**Scope.** Decoupling, matching and running, operator bases, Fermi theory, chiral perturbation theory, heavy-quark EFT, soft-collinear EFT, Standard Model EFT (SMEFT), gravity as an EFT.

**Core ideas.**
- Physics at energy $E$ is insensitive to details at $\Lambda\gg E$ except through a tower of local operators suppressed by $(E/\Lambda)^{d-4}$.
- Match the full theory to the EFT at $\mu\sim\Lambda$, then run with the RG to low scales.
- SMEFT parametrizes heavy new physics by dimension-6 operators; global fits to LHC data constrain their coefficients.

**Key equations.**
$$\mathcal L_{\text{eff}} = \mathcal L_{\text{SM}} + \sum_i \frac{c_i}{\Lambda^2}\mathcal O_i^{(6)} + \mathcal O(\Lambda^{-4}),\qquad G_F/\sqrt2=g^2/(8m_W^2)$$

**Landmark.** Weinberg (1979) "Phenomenological Lagrangians" — see [subfield landmarks](knowledge/06-particle-physics/quantum-field-theory/README.md).

**See also.** [Nuclear forces and chiral EFT](knowledge/07-nuclear-physics/nuclear-structure/nuclear-forces-and-chiral-eft/README.md) · [Renormalization](knowledge/06-particle-physics/quantum-field-theory/renormalization-and-running-couplings/README.md)

### Gauge theories and Yang–Mills · `knowledge/06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills`

**Scope.** Abelian and non-abelian gauge invariance, covariant derivatives, field strengths, Faddeev–Popov ghosts, BRST symmetry, Wilson loops, phases of gauge theories (Coulomb, Higgs, confining).

**Core ideas.**
- Demanding invariance under local transformations $\psi\to U(x)\psi$ forces a gauge field $A_\mu$ with $D_\mu=\partial_\mu-igA_\mu^aT^a$.
- Non-abelian fields self-interact (three- and four-gluon vertices), which produces asymptotic freedom.
- Gauge "symmetry" is a redundancy of description; only gauge-invariant quantities are physical.

**Key equations.**
$$F^a_{\mu\nu}=\partial_\mu A^a_\nu-\partial_\nu A^a_\mu+gf^{abc}A^b_\mu A^c_\nu,\qquad \mathcal L_{\text{YM}}=-\tfrac14F^a_{\mu\nu}F^{a\,\mu\nu}$$

**Landmark.** Yang & Mills (1954) — see [subfield landmarks](knowledge/06-particle-physics/quantum-field-theory/README.md).

**Open questions.** Yang–Mills existence and mass gap; analytic understanding of confinement.

**See also.** [Quantum chromodynamics](knowledge/06-particle-physics/standard-model/quantum-chromodynamics/README.md) · [Potentials and gauge invariance in EM](knowledge/02-electromagnetism-and-optics/electrodynamics/potentials-and-gauge-invariance/README.md)

### Lattice field theory · `knowledge/06-particle-physics/quantum-field-theory/lattice-field-theory`

**Scope.** Wilson's lattice gauge action, fermion discretizations (Wilson, staggered, domain-wall, overlap), Monte Carlo (HMC), continuum and chiral extrapolations, hadron masses, $\alpha_s$, quark masses, hadronic vacuum polarization for muon $g-2$.

**Core ideas.**
- Euclidean path integral on a hypercubic grid becomes a statistical-mechanics problem sampled by Markov-chain Monte Carlo.
- Gauge links $U_\mu(x)=e^{iagA_\mu(x)}$ keep exact gauge invariance at finite spacing $a$.
- Fermion doubling (Nielsen–Ninomiya) forces trade-offs between chiral symmetry and locality.
- The sign problem blocks finite-density QCD and real-time dynamics.

**Key equations.**
$$S_W=\beta\sum_{x,\mu<\nu}\left(1-\tfrac{1}{N}\,\mathrm{Re\,Tr}\,U_{\mu\nu}(x)\right),\qquad \beta=2N/g^2$$

**Landmark.** Wilson (1974) "Confinement of quarks" — see [subfield landmarks](knowledge/06-particle-physics/quantum-field-theory/README.md).

**Open questions.** Sign problem; precision HVP to settle the muon $g-2$ comparison; quantum simulation of gauge theories.

**See also.** [Monte Carlo methods](knowledge/00-foundations/computational-physics/monte-carlo-methods/README.md) · [QCD phase diagram](knowledge/07-nuclear-physics/heavy-ion-physics/qcd-phase-diagram-and-critical-point/README.md)

### Renormalization and running couplings · `knowledge/06-particle-physics/quantum-field-theory/renormalization-and-running-couplings`

**Scope.** Regularization (cutoff, Pauli–Villars, dimensional), counterterms, renormalizability and power counting, MS-bar scheme, Callan–Symanzik equation, beta functions, anomalous dimensions, fixed points.

**Core ideas.**
- Divergences are absorbed into a finite number of parameters in renormalizable theories; physical predictions are scheme-independent.
- Couplings depend on the energy scale: QED's $\alpha$ grows ($\approx1/137$ at $q\to0$, $\approx1/128$ at $m_Z$); QCD's $\alpha_s$ shrinks (asymptotic freedom).
- Wilsonian view: integrating out high-momentum modes generates the RG flow; irrelevant operators are suppressed by powers of the cutoff.

**Key equations.**
$$\alpha_s(Q^2)=\frac{\alpha_s(\mu^2)}{1+\frac{\alpha_s(\mu^2)}{4\pi}\beta_0\ln(Q^2/\mu^2)},\qquad \beta_0=11-\tfrac23 n_f$$

**Open questions.** Landau pole of QED/Higgs sector; UV completion of the SM.

**See also.** [Renormalization group in statistical physics](knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/renormalization-group/README.md) · [Effective field theory](knowledge/06-particle-physics/quantum-field-theory/effective-field-theory/README.md)

## Standard Model · `knowledge/06-particle-physics/standard-model`

#### Overview
The Standard Model describes all known non-gravitational interactions with 3 generations of fermions, 12 gauge bosons (8 gluons, $W^\pm$, $Z$, $\gamma$) and one Higgs doublet. Its free parameters (minimal version, massless neutrinos): 6 quark masses, 3 charged-lepton masses, 4 CKM parameters, 3 gauge couplings, 2 Higgs-sector parameters, and $\theta_{\text{QCD}}$ — 19 in total.

#### Conceptual spine
1. Fermions in chiral representations: left-handed doublets, right-handed singlets.
2. Higgs doublet acquires $\langle H\rangle = v/\sqrt2$, $v\approx246$ GeV → $W$, $Z$ masses; Yukawa couplings → fermion masses.
3. Quark mass and weak eigenstates differ → CKM matrix → flavor changing charged currents, CP violation.
4. QCD confines quarks into hadrons at $\Lambda_{\text{QCD}}\sim 200$–300 MeV.
5. Anomaly cancellation ties quark and lepton hypercharges together.

#### Key equations
$$m_W=\tfrac12 g v,\qquad m_Z=\tfrac12\sqrt{g^2+g'^2}\,v,\qquad \cos\theta_W=m_W/m_Z,\qquad e=g\sin\theta_W$$
$$V(H)=-\mu^2H^\dagger H+\lambda(H^\dagger H)^2,\qquad m_h^2=2\lambda v^2$$

#### Open problems
- Origin of the fermion mass hierarchy and mixing patterns (the flavor puzzle).
- Stability of the electroweak vacuum: with $m_h\approx125$ GeV and $m_t\approx173$ GeV the SM vacuum appears metastable.
- Strong-CP problem: why is $|\theta_{\text{QCD}}|\lesssim10^{-10}$?

#### Connections
- [Quantum field theory](knowledge/06-particle-physics/quantum-field-theory/README.md) (the language) · [Beyond the Standard Model](knowledge/06-particle-physics/beyond-the-standard-model/README.md) (what's missing)
- [Spontaneous symmetry breaking](knowledge/00-foundations/symmetry-and-group-theory/README.md) · [Superconductivity](knowledge/08-condensed-matter/superconductivity/README.md) (the Higgs mechanism first appeared as the Meissner effect)

### Electroweak theory · `knowledge/06-particle-physics/standard-model/electroweak-theory`

**Scope.** $SU(2)_L\times U(1)_Y$, weak isospin and hypercharge, $W/Z$ bosons, neutral currents, Weinberg angle, LEP/SLC $Z$-pole measurements, oblique parameters $S,T,U$, global electroweak fits, $W$-mass measurements.

**Core ideas.**
- Only left-handed fermions feel $SU(2)_L$: the weak force is maximally parity violating.
- Electric charge $Q=T_3+Y/2$ emerges after symmetry breaking; the photon is the unbroken combination.
- Loop corrections make the $W$ mass sensitive to $m_t$ and $m_h$ — the top and Higgs masses were predicted before discovery.

**Key equations.**
$$\rho=\frac{m_W^2}{m_Z^2\cos^2\theta_W}=1\ (\text{tree level}),\qquad \sin^2\theta_W^{\text{eff}}\approx0.2315$$

**Open questions.** Tension among $W$-mass measurements (CDF 2022 vs. ATLAS/CMS/LHCb); the nature of the electroweak phase transition in the early universe.

**See also.** [Higgs boson](knowledge/06-particle-physics/standard-model/higgs-boson/README.md) · [Beta decay](knowledge/07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions/README.md)

### Flavor physics and the CKM matrix · `knowledge/06-particle-physics/standard-model/flavor-physics-and-ckm`

**Scope.** CKM matrix and Wolfenstein parametrization, unitarity triangle, $K$, $D$, $B$ and $B_s$ mixing, GIM mechanism, flavor-changing neutral currents (FCNC), rare decays ($B_s\to\mu\mu$, $K\to\pi\nu\bar\nu$), lepton-flavor universality tests.

**Core ideas.**
- Charged-current interactions mix generations through a 3×3 unitary matrix with 3 angles and 1 CP-violating phase.
- FCNCs are absent at tree level (GIM), so rare decays are sensitive to heavy new particles in loops — probing scales far above collider reach.
- The flavor hierarchy $|V_{ub}|\ll|V_{cb}|\ll|V_{us}|$ is unexplained.

**Key equations.**
$$V_{\text{CKM}}\approx\begin{pmatrix}1-\lambda^2/2&\lambda&A\lambda^3(\rho-i\eta)\\-\lambda&1-\lambda^2/2&A\lambda^2\\A\lambda^3(1-\rho-i\eta)&-A\lambda^2&1\end{pmatrix},\quad \lambda\approx0.225$$

**Open questions.** $|V_{ub}|$ and $|V_{cb}|$ inclusive vs. exclusive tensions; first-row CKM unitarity deficit ("Cabibbo angle anomaly").

**See also.** [CP violation](knowledge/06-particle-physics/standard-model/cp-violation/README.md) · [Precision anomalies](knowledge/06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2/README.md)

### Hadron spectroscopy and exotic hadrons · `knowledge/06-particle-physics/standard-model/hadron-spectroscopy-and-exotics`

**Scope.** $SU(3)$ flavor multiplets, quark model, quarkonium ($c\bar c$, $b\bar b$) spectroscopy, $X(3872)$, $Z_c$ states, LHCb pentaquarks $P_c$, $T_{cc}^+$, glueballs and hybrids, molecular vs. compact interpretations.

**Core ideas.**
- Mesons are $q\bar q$, baryons $qqq$ — but QCD allows any color singlet, e.g. $qq\bar q\bar q$ and $qqqq\bar q$.
- Many exotic states sit near two-hadron thresholds, so "hadronic molecule" vs. "compact multiquark" is a central debate.
- Heavy-quark spin symmetry organizes quarkonium-like spectra.

**Key equations.**
$$\text{Gell-Mann–Okubo: } 2(m_N+m_\Xi)=3m_\Lambda+m_\Sigma$$

**Landmark.** Gell-Mann (1964). "A schematic model of baryons and mesons". *Phys. Lett.* 8, 214. [doi:10.1016/S0031-9163(64)92001-3](https://doi.org/10.1016/S0031-9163(64)92001-3)

**See also.** [Lie groups and representations](knowledge/00-foundations/symmetry-and-group-theory/lie-groups-and-representations/README.md) · [QCD](knowledge/06-particle-physics/standard-model/quantum-chromodynamics/README.md)

### Higgs boson · `knowledge/06-particle-physics/standard-model/higgs-boson`

**Scope.** Higgs mechanism, production modes (gluon fusion, VBF, $VH$, $t\bar tH$), decays ($b\bar b$, $WW^*$, $\tau\tau$, $ZZ^*$, $\gamma\gamma$, $\mu\mu$), coupling "kappa" fits, spin–parity, width, di-Higgs production and the trilinear self-coupling.

**Core ideas.**
- Goldstone bosons of the broken symmetry become the longitudinal $W^\pm,Z$ polarizations; one physical scalar remains.
- Couplings to fermions and bosons are proportional to mass — a sharp prediction tested to ~5–10% for third-generation fermions and vector bosons.
- $m_h\approx125.1$ GeV; the potential's shape away from the minimum is still mostly unmeasured.

**Key equations.**
$$g_{hff}=\frac{m_f}{v},\qquad g_{hVV}=\frac{2m_V^2}{v},\qquad \lambda_{hhh}^{\text{SM}}=\frac{m_h^2}{2v^2}\approx0.13$$

**Open questions.** Is the Higgs elementary or composite? Self-coupling measurement at HL-LHC/FCC; Higgs portal to dark sectors.

**See also.** [Electroweak theory](knowledge/06-particle-physics/standard-model/electroweak-theory/README.md) · [Hadron colliders and the LHC](knowledge/06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc/README.md) · [Spontaneous symmetry breaking](knowledge/00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking/README.md)

### Quantum chromodynamics · `knowledge/06-particle-physics/standard-model/quantum-chromodynamics`

**Scope.** Color charge, gluon self-interaction, running of $\alpha_s$, perturbative QCD and factorization, confinement, chiral symmetry breaking and pions as pseudo-Goldstone bosons, hadron masses (mostly from gluon field energy, not quark masses).

**Core ideas.**
- $\alpha_s$ decreases at high momentum transfer ($\alpha_s(m_Z)\approx0.118$), so hard processes are perturbative; at ~1 GeV it is strong.
- Color confinement: only color singlets are observed; the static quark potential rises linearly, $V(r)\approx -\frac{4}{3}\frac{\alpha_s}{r}+\sigma r$ with string tension $\sigma\approx0.18\ \text{GeV}^2$.
- ~99% of the visible mass of the universe comes from QCD dynamics rather than the Higgs.

**Key equations.**
$$\mathcal L_{\text{QCD}}=\sum_q\bar q\,(i\gamma^\mu D_\mu-m_q)\,q-\tfrac14G^a_{\mu\nu}G^{a\,\mu\nu},\qquad m_\pi^2f_\pi^2=-(m_u+m_d)\langle\bar qq\rangle$$

**Open questions.** Analytic proof of confinement; origin of the proton spin; the QCD phase diagram at finite density.

**See also.** [Lattice field theory](knowledge/06-particle-physics/quantum-field-theory/lattice-field-theory/README.md) · [Quark–gluon plasma](knowledge/07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma/README.md) · [Parton distributions](knowledge/07-nuclear-physics/hadron-and-nucleon-structure/parton-distribution-functions/README.md)


---

# Packet 06-4 (100 records)

{"id": "C2239", "a": "06-particle-physics/standard-model/electroweak-theory", "b": "07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions", "name": "Fermi contact theory as low-energy W exchange", "kind": "identity", "summary": "Fermi's four-fermion interaction is the q^2<<m_W^2 limit of W exchange in SU(2)xU(1); maximal parity violation seen in 60Co decay fixed the V-A, left-handed structure of the electroweak theory.", "map": "\\frac{G_F}{\\sqrt2}=\\frac{g^2}{8m_W^2};\\ \\frac{g^2}{q^2-m_W^2}\\to-\\frac{g^2}{m_W^2}\\ (q^2\\ll m_W^2)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2240", "a": "06-particle-physics/standard-model/flavor-physics-and-ckm", "b": "07-nuclear-physics/nuclear-reactions-and-decays", "name": "Nuclear weak decays as flavor probes", "kind": "shared object", "summary": "Nuclear beta decays supply the most precise CKM element |V_ud| and tests of first-row unitarity, which constrains new physics at the 10^-4 level.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2241", "a": "06-particle-physics/standard-model/flavor-physics-and-ckm", "b": "07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions", "name": "V_ud and first-row CKM unitarity", "kind": "shared object", "summary": "Superallowed 0+->0+ ft values give |V_ud| = 0.9737; with |V_us| from kaons the first-row sum falls ~3 sigma short of 1 (Cabibbo angle anomaly), sensitive to the gamma-W box radiative correction.", "map": "\\mathcal Ft=\\frac{K}{2G_F^2|V_{ud}|^2(1+\\Delta_R^V)};\\ |V_{ud}|^2+|V_{us}|^2+|V_{ub}|^2=1-\\delta", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2242", "a": "06-particle-physics/standard-model/hadron-spectroscopy-and-exotics", "b": "07-nuclear-physics/hadron-and-nucleon-structure/nucleon-spin-and-form-factors", "name": "Spin crisis exposes the constituent quark model", "kind": "historical", "summary": "The static quark model that organizes baryon multiplets predicts quarks carry essentially all the proton spin; the EMC result Delta Sigma ~ 0.3 showed that sea quarks, gluons and orbital motion matter.", "map": "\\tfrac12=\\tfrac12\\Delta\\Sigma+\\Delta G+L_q+L_g;\\ \\Delta\\Sigma_{\\text{NRQM}}=1\\ \\text{vs}\\ \\approx0.3\\ (\\text{exp})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2243", "a": "06-particle-physics/standard-model/hadron-spectroscopy-and-exotics", "b": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "name": "Quarkonium melting by color Debye screening", "kind": "mechanism", "summary": "Quarkonia are bound by the Cornell potential; in a QGP color screening shortens its range so states melt sequentially (psi', J/psi, Upsilon), making quarkonium spectra a QGP thermometer.", "map": "V(r)=-\\frac43\\frac{\\alpha_s}{r}+\\sigma r\\ \\to\\ -\\frac43\\frac{\\alpha_s}{r}e^{-m_Dr},\\ m_D\\sim gT", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2244", "a": "06-particle-physics/standard-model/hadron-spectroscopy-and-exotics", "b": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "name": "Hyperon puzzle in neutron-star cores", "kind": "mechanism", "summary": "SU(3) flavor predicts Lambda and Sigma hyperons appear at 2-3 n_0, softening the EOS below what 2 M_sun pulsars allow; hyperon-nucleon and three-baryon forces are the proposed resolution.", "map": "\\mu_\\Lambda=\\mu_n\\ \\text{at onset};\\ M_{\\max}^{\\text{hyp}}\\lesssim1.6M_\\odot\\ \\text{(naive)}\\ \\text{vs}\\ M_{\\text{obs}}\\approx2M_\\odot", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2245", "a": "06-particle-physics/standard-model/hadron-spectroscopy-and-exotics", "b": "07-nuclear-physics/nuclear-structure/nuclear-forces-and-chiral-eft", "name": "Near-threshold exotics as deuteron-like molecules", "kind": "mechanism", "summary": "States such as X(3872) and T_cc+ lie just below two-hadron thresholds, so the same universal shallow-bound-state physics and Weinberg compositeness criterion used for the deuteron applies; meson-exchange forces bind them.", "map": "\\gamma=\\sqrt{2\\mu B}\\ll m_\\pi;\\ a\\approx\\frac{2(1-Z)}{2-Z}\\frac1\\gamma\\ (\\text{Weinberg},\\ Z=\\text{elementariness})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2246", "a": "06-particle-physics/standard-model/quantum-chromodynamics", "b": "07-nuclear-physics/hadron-and-nucleon-structure", "name": "Nucleon structure is non-perturbative QCD", "kind": "shared object", "summary": "The proton's parton content, spin and mass are QCD bound-state properties; nuclear-physics DIS experiments supplied the evidence for quarks and asymptotic freedom.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2247", "a": "06-particle-physics/standard-model/quantum-chromodynamics", "b": "07-nuclear-physics/hadron-and-nucleon-structure/electron-ion-collider", "name": "Gluon saturation and the origin of nucleon mass", "kind": "mechanism", "summary": "Non-linear QCD evolution predicts gluon densities saturate at small x (color glass condensate), and the trace anomaly makes most of the nucleon mass gluonic; both are EIC flagship measurements.", "map": "Q_s^2\\sim A^{1/3}x^{-\\lambda};\\ m_N\\propto\\langle N|\\tfrac{\\beta(g)}{2g}G^2+\\ldots|N\\rangle\\ (\\text{trace anomaly})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2248", "a": "06-particle-physics/standard-model/quantum-chromodynamics", "b": "07-nuclear-physics/hadron-and-nucleon-structure/parton-distribution-functions", "name": "DGLAP evolution of parton distributions", "kind": "identity", "summary": "PDFs are non-perturbative proton matrix elements whose scale dependence is fixed by perturbative QCD splitting functions; Bjorken scaling and its logarithmic violation are asymptotic freedom seen in DIS.", "map": "\\frac{\\partial q(x,\\mu^2)}{\\partial\\ln\\mu^2}=\\frac{\\alpha_s}{2\\pi}\\int_x^1\\frac{dz}{z}P_{qq}(z)q(x/z)+\\ldots", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2249", "a": "06-particle-physics/standard-model/quantum-chromodynamics", "b": "07-nuclear-physics/heavy-ion-physics", "name": "Heavy-ion collisions map QCD matter", "kind": "shared object", "summary": "Heavy-ion programmes at RHIC and the LHC study QCD at high temperature and density: deconfinement, chiral restoration, collective flow and jet quenching.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2250", "a": "06-particle-physics/standard-model/quantum-chromodynamics", "b": "07-nuclear-physics/heavy-ion-physics/qcd-phase-diagram-and-critical-point", "name": "Phases of QCD at finite T and mu_B", "kind": "mechanism", "summary": "QCD's chiral and center symmetries organize its phase diagram: chiral restoration and deconfinement at high T, a conjectured critical point, and color-superconducting (CFL) phases at high density.", "map": "\\langle\\bar qq\\rangle\\to0\\ (T\\gtrsim156\\ \\text{MeV});\\ \\langle qq\\rangle\\neq0\\ (\\mu_B\\gg\\Lambda_{QCD},\\ \\text{CFL})", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2251", "a": "06-particle-physics/standard-model/quantum-chromodynamics", "b": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "name": "Asymptotic freedom implies deconfined matter", "kind": "mechanism", "summary": "Because alpha_s runs to zero at high momentum scales, hot or dense QCD matter deconfines into a quark-gluon plasma; its Stefan-Boltzmann limit counts gluon and quark degrees of freedom.", "map": "\\frac{\\varepsilon}{T^4}\\to\\frac{\\pi^2}{30}\\left(16+\\tfrac{21}{2}n_f\\right),\\ \\alpha_s(Q)\\to0\\ (Q\\sim T\\to\\infty)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2252", "a": "06-particle-physics/standard-model/quantum-chromodynamics", "b": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "name": "Quark matter and pQCD constraints on dense EOS", "kind": "mechanism", "summary": "At asymptotic density perturbative QCD fixes the pressure; interpolating between chiral EFT at n_0 and pQCD at ~40 n_0 under causality constrains the neutron-star EOS and suggests quark-matter cores in massive stars.", "map": "P_{\\text{pQCD}}(\\mu_B)\\ \\text{at}\\ \\mu_B\\approx2.6\\ \\text{GeV};\\ c_s^2\\le1,\\ c_s^2\\to1/3", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2253", "a": "06-particle-physics/standard-model/quantum-chromodynamics", "b": "07-nuclear-physics/nuclear-structure/nuclear-forces-and-chiral-eft", "name": "Pions as pseudo-Goldstone bosons mediate nuclear force", "kind": "mechanism", "summary": "Spontaneous chiral symmetry breaking in QCD makes the pion light; its exchange is the long-range part of the nuclear force (Yukawa), with pion couplings fixed by chiral symmetry (Goldberger-Treiman).", "map": "m_\\pi^2f_\\pi^2=-(m_u+m_d)\\langle\\bar qq\\rangle\\ \\leftrightarrow\\ V_{1\\pi}\\propto\\frac{g_A^2}{4f_\\pi^2}\\frac{(\\sigma_1\\cdot q)(\\sigma_2\\cdot q)}{q^2+m_\\pi^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2254", "a": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "Quantum-limited amplifiers for axion haloscopes", "kind": "method transfer", "summary": "Cavity haloscopes convert axions to microwave photons in a magnet; SQUID and Josephson parametric amplifiers (and squeezing) bring readout to the quantum limit, setting the scan rate in the micro-eV mass range.", "map": "P_{a\\to\\gamma}\\propto g_{a\\gamma\\gamma}^2\\frac{\\rho_a}{m_a}B^2VC\\,Q;\\ \\frac{df}{dt}\\propto\\frac{P^2}{T_{\\text{sys}}^2}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2255", "a": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "b": "08-condensed-matter/topological-matter/topological-insulators", "name": "Axion electrodynamics in topological magnets", "kind": "analogy", "summary": "The theta angle of a TI plays the role of the axion field; in magnetic TIs theta can fluctuate, giving a dynamical 'axion quasiparticle' whose coupling to E.B mirrors the QCD axion's photon coupling and has been proposed for dark-matter detection.", "map": "\\mathcal L=\\frac{\\alpha}{4\\pi^2}\\theta(\\mathbf x,t)\\mathbf E\\cdot\\mathbf B\\ \\leftrightarrow\\ -\\frac{g_{a\\gamma\\gamma}}{4}aF\\tilde F,\\ \\theta\\leftrightarrow a/f_a", "breaks": "The condensed-matter theta is an emergent, lattice-scale field with meV dynamics and no shift symmetry from a QCD anomaly; it cannot solve strong CP or be dark matter itself.", "confidence": "current research", "strength": 2}
{"id": "C2256", "a": "06-particle-physics/beyond-the-standard-model/dark-matter-particle-candidates", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "Sub-MeV dark matter scattering into phonons", "kind": "method transfer", "summary": "Below ~MeV, dark-matter momentum transfers match crystal phonon and magnon scales, so detection relies on condensed-matter response functions (dynamic structure factor, dielectric loss) rather than nuclear recoils.", "map": "\\Gamma\\propto\\int d^3q\\,\\frac{|F_{\\text{DM}}(q)|^2}{q^2}\\,\\mathrm{Im}\\!\\left[\\frac{-1}{\\epsilon(\\mathbf q,\\omega)}\\right]\\ (\\text{dielectric formalism})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2257", "a": "06-particle-physics/beyond-the-standard-model/extra-dimensions-and-hierarchy-problem", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Composite Higgs and top condensation from BCS", "kind": "historical", "summary": "Technicolor and top-quark condensation replace the elementary Higgs by a fermion-pair condensate formed by a gap equation, the BCS template (one author is Bardeen of BCS); the Higgs would be composite.", "map": "\\langle\\bar tt\\rangle\\neq0:\\ m_t\\ \\text{from gap equation},\\ v=246\\ \\text{GeV}\\leftrightarrow\\Delta", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2258", "a": "06-particle-physics/beyond-the-standard-model/grand-unification-and-proton-decay", "b": "08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids", "name": "Emergent magnetic monopoles in spin ice", "kind": "analogy", "summary": "Defects violating the two-in-two-out ice rule behave as deconfined magnetic charges with a Coulomb interaction, a laboratory analogue of the magnetic monopoles predicted by grand unification.", "map": "Q_m=\\pm\\frac{2\\mu}{a_d};\\ V(r)=\\frac{\\mu_0}{4\\pi}\\frac{Q_mQ_m'}{r}", "breaks": "Spin-ice monopoles are sources of H (div B = 0 still holds), their charge is not Dirac-quantized, and they are classical lattice defects rather than 't Hooft-Polyakov solitons of a broken gauge group.", "confidence": "established", "strength": 2}
{"id": "C2259", "a": "06-particle-physics/beyond-the-standard-model/grand-unification-and-proton-decay", "b": "08-condensed-matter/soft-matter/liquid-crystals", "name": "Hedgehogs, strings and the Kibble mechanism", "kind": "analogy", "summary": "Point and line defects in nematics are classified by the same homotopy groups as GUT monopoles and cosmic strings, and quenches through the isotropic-nematic transition test Kibble's defect-formation scenario.", "map": "\\pi_2(SO(3)/O(2))=\\mathbb Z\\ \\leftrightarrow\\ \\pi_2(G/H)=\\pi_1(H)\\ (\\text{monopoles});\\ n_{\\text{def}}\\sim\\xi^{-d}", "breaks": "Nematic defects have no gauge field, energy that scales with system size, and dissipative rather than relativistic dynamics.", "confidence": "established", "strength": 2}
{"id": "C2260", "a": "06-particle-physics/beyond-the-standard-model/supersymmetry", "b": "08-condensed-matter/topological-matter/topological-superconductors-and-majoranas", "name": "Emergent supersymmetry at topological boundaries", "kind": "analogy", "summary": "At the boundary of topological superconductors (or interacting Majorana chains) the critical point can be the tricritical Ising CFT or an N=1 Wess-Zumino theory, with exact emergent supersymmetry between bosonic order parameter and Majorana fermion.", "map": "c=\\tfrac{7}{10}\\ (\\text{tricritical Ising, }\\mathcal N=1\\ \\text{superconformal});\\ \\{Q,\\bar Q\\}\\sim P\\ \\text{emergent}", "breaks": "Supersymmetry is emergent only at fine-tuned criticality and low energy; there is no superpartner spectrum or SUSY breaking scale as in the MSSM.", "confidence": "current research", "strength": 2}
{"id": "C2261", "a": "06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Type-II NbTi magnets bend the LHC beams", "kind": "shared object", "summary": "The LHC's 8.3 T dipoles use NbTi, a type-II superconductor with strong flux pinning, cooled to 1.9 K in superfluid helium; the beam rigidity and the upper critical field set the reachable energy.", "map": "B\\rho=p/e:\\ 7\\ \\text{TeV}\\Rightarrow8.33\\ \\text{T};\\ B<B_{c2}(1.9\\ \\text{K})\\approx13\\ \\text{T (NbTi)}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2262", "a": "06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers", "b": "08-condensed-matter/crystals-and-electronic-structure/semiconductors", "name": "Silicon trackers are reverse-biased p-n junctions", "kind": "method transfer", "summary": "Pixel and strip trackers collect electron-hole pairs (3.6 eV per pair in Si) drifting in the depletion region of a reverse-biased p-n junction; radiation damage (displacement defects, type inversion) is semiconductor defect physics.", "map": "w=\\sqrt{\\frac{2\\epsilon_{Si}(V+V_{bi})}{qN_{\\text{eff}}}};\\ \\langle N_{eh}\\rangle\\approx\\frac{dE/dx\\cdot d}{3.6\\ \\text{eV}}\\approx80\\ \\mu\\text{m}^{-1}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2263", "a": "06-particle-physics/neutrino-physics/neutrino-mass-and-double-beta-decay", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "Cryogenic bolometers for 0nubb", "kind": "method transfer", "summary": "CUORE-type TeO2 crystals at ~10 mK act as calorimeters: the Debye T^3 heat capacity is tiny, so a 2.5 MeV decay raises the temperature measurably and gives keV resolution.", "map": "\\Delta T=\\frac{E}{C(T)},\\ C_V=\\frac{12\\pi^4}{5}Nk_B\\left(\\frac{T}{\\Theta_D}\\right)^3", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2264", "a": "06-particle-physics/neutrino-physics/neutrino-mass-and-double-beta-decay", "b": "08-condensed-matter/topological-matter/topological-superconductors-and-majoranas", "name": "Majorana neutrinos versus Majorana zero modes", "kind": "analogy", "summary": "Both rest on a self-conjugate fermion psi=psi^c (gamma=gamma-dagger): an elementary Majorana neutrino would violate lepton number in 0nubb, while zero-energy Majorana modes bound to vortices or wire ends obey non-abelian exchange statistics.", "map": "\\nu=\\nu^c\\ \\leftrightarrow\\ \\gamma=\\gamma^\\dagger,\\ c=\\tfrac12(\\gamma_1+i\\gamma_2)", "breaks": "Majorana zero modes are not propagating particles; they are non-abelian anyons bound to defects with no momentum or mass. Several condensed-matter Majorana claims have been retracted or reinterpreted, so evidence there is contested.", "confidence": "current research", "strength": 2}
{"id": "C2265", "a": "06-particle-physics/quantum-field-theory", "b": "08-condensed-matter/strongly-correlated-electrons", "name": "Many-body field theory: one language for both", "kind": "method transfer", "summary": "Propagators, Feynman diagrams, Matsubara sums, path integrals and the RG moved from particle QFT into many-body theory (Green's functions, Fermi liquids, Hubbard-Stratonovich), and emergent gauge theories flow back.", "map": "G(\\mathbf k,i\\omega_n)=\\frac{1}{i\\omega_n-\\xi_{\\mathbf k}-\\Sigma(\\mathbf k,i\\omega_n)}\\ \\leftrightarrow\\ \\frac{i}{p^2-m^2-\\Sigma(p^2)}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2266", "a": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "Phase slips and macroscopic tunnelling as instantons", "kind": "method transfer", "summary": "The escape of a current-biased Josephson phase from a tilted-washboard well is a Euclidean bounce, computed with the same instanton methods as false-vacuum decay; dissipation enters through a Caldeira-Leggett bath.", "map": "\\Gamma\\approx Ae^{-S_B/\\hbar},\\ S_B\\propto\\frac{\\Delta U}{\\omega_p}\\ \\leftrightarrow\\ \\Gamma/V\\propto e^{-S_E[\\phi_b]}\\ (\\text{Coleman})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2267", "a": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "b": "08-condensed-matter/topological-matter", "name": "Anomaly inflow and bulk-boundary correspondence", "kind": "identity", "summary": "Gapless boundary modes of topological phases carry 't Hooft anomalies that are cancelled by inflow from the bulk topological response (Callan-Harvey), so the classification of topological matter is a classification of anomalies.", "map": "\\partial_\\mu j^\\mu_{\\text{edge}}=\\frac{e^2}{2\\pi h}\\epsilon^{\\mu\\nu}F_{\\mu\\nu}\\cdot\\tfrac12\\ \\leftrightarrow\\ \\text{bulk Chern-Simons }\\frac{k}{4\\pi}AdA", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2268", "a": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "b": "08-condensed-matter/topological-matter/quantum-hall-effects", "name": "Chern-Simons theory and the parity anomaly", "kind": "identity", "summary": "The quantum Hall response is a Chern-Simons term whose level is the TKNN Chern number; Haldane's honeycomb model realized the 2+1D parity anomaly of a single massive Dirac fermion, the seed of Chern insulators.", "map": "\\mathcal L_{CS}=\\frac{k}{4\\pi}\\epsilon^{\\mu\\nu\\lambda}A_\\mu\\partial_\\nu A_\\lambda\\Rightarrow\\sigma_{xy}=k\\frac{e^2}{h};\\ \\sigma_{xy}^{\\text{Dirac}}=\\tfrac12\\mathrm{sgn}(m)\\tfrac{e^2}{h}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2269", "a": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "b": "08-condensed-matter/topological-matter/topological-insulators", "name": "Theta term and axion electrodynamics of 3D TIs", "kind": "identity", "summary": "The electromagnetic response of a time-reversal-invariant 3D topological insulator is a theta term with theta=pi, the same topological term as QCD's theta and the axion coupling; it implies a half-quantized surface Hall effect and the Witten effect.", "map": "\\mathcal L_\\theta=\\frac{\\theta e^2}{2\\pi h}\\mathbf E\\cdot\\mathbf B=\\frac{\\theta\\alpha}{4\\pi^2}\\mathbf E\\cdot\\mathbf B,\\ \\theta=\\pi;\\ \\sigma_{xy}^{\\text{surf}}=\\tfrac12\\tfrac{e^2}{h}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2270", "a": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "b": "08-condensed-matter/topological-matter/topological-semimetals", "name": "Chiral (ABJ) anomaly in Weyl semimetals", "kind": "identity", "summary": "Parallel E and B pump electrons between Weyl nodes of opposite chirality exactly as the Adler-Bell-Jackiw anomaly; the result is a negative longitudinal magnetoresistance.", "map": "\\frac{dN_\\pm}{dt}=\\pm\\frac{e^2}{h^2}\\mathbf E\\cdot\\mathbf B\\ \\leftrightarrow\\ \\partial_\\mu j_5^\\mu=\\frac{e^2}{16\\pi^2}\\epsilon^{\\mu\\nu\\rho\\sigma}F_{\\mu\\nu}F_{\\rho\\sigma}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2271", "a": "06-particle-physics/quantum-field-theory/canonical-and-path-integral-quantization", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "name": "Graphene's massless 2+1D Dirac fermions", "kind": "identity", "summary": "Near the K points graphene's tight-binding bands obey the massless 2+1D Dirac equation with c replaced by v_F~c/300 and spin replaced by sublattice pseudospin, giving Klein tunnelling, a half-integer Hall sequence and optical absorption pi*alpha.", "map": "H=\\hbar v_F\\,\\boldsymbol\\sigma\\cdot\\mathbf k\\ \\leftrightarrow\\ H_D=c\\,\\boldsymbol\\alpha\\cdot\\mathbf p;\\ \\alpha_g=\\frac{e^2}{4\\pi\\epsilon\\hbar v_F}\\approx2.2,\\ T=1-\\pi\\alpha", "breaks": "Lorentz invariance is only emergent at low energy; the Coulomb interaction is instantaneous (it travels at c, not v_F), so interacting graphene is not a relativistic QFT; valleys double the fermion count.", "confidence": "established", "strength": 3}
{"id": "C2272", "a": "06-particle-physics/quantum-field-theory/canonical-and-path-integral-quantization", "b": "08-condensed-matter/topological-matter/topological-semimetals", "name": "Weyl equation realized in TaAs", "kind": "identity", "summary": "Weyl semimetals host quasiparticles obeying the two-component Weyl equation that elementary physics never confirmed (neutrinos turned out massive); each node is a monopole of Berry curvature with chirality +-1.", "map": "H_W=\\pm\\hbar v_F\\boldsymbol\\sigma\\cdot\\mathbf k\\ \\leftrightarrow\\ i\\bar\\sigma^\\mu\\partial_\\mu\\psi_L=0", "breaks": "Solid-state Weyl nodes can be tilted (type II), anisotropic and offset in energy, since there is no Lorentz symmetry, and their total number is fixed by the lattice.", "confidence": "established", "strength": 3}
{"id": "C2273", "a": "06-particle-physics/quantum-field-theory/conformal-field-theory", "b": "08-condensed-matter/strongly-correlated-electrons/heavy-fermions-and-kondo-physics", "name": "Boundary CFT solves the multichannel Kondo problem", "kind": "method transfer", "summary": "Affleck and Ludwig treated the impurity as a conformal boundary condition of a 1+1D chiral CFT, obtaining the non-Fermi-liquid exponents and residual entropy of the overscreened multichannel Kondo fixed point.", "map": "S_{\\text{imp}}=\\ln\\sqrt2\\ (k=2\\ \\text{channel});\\ \\rho(T)-\\rho(0)\\propto T^{\\Delta}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2274", "a": "06-particle-physics/quantum-field-theory/conformal-field-theory", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "Entanglement scaling reads off the central charge", "kind": "method transfer", "summary": "At a 1+1D critical point the entanglement entropy grows as (c/3) ln L, so DMRG and tensor-network simulations extract CFT central charges and operator dimensions directly from ground states.", "map": "S_A=\\frac{c}{3}\\ln\\frac{L}{a}+c'\\ (\\text{periodic: }c/3,\\ \\text{open: }c/6)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2275", "a": "06-particle-physics/quantum-field-theory/conformal-field-theory", "b": "08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals", "name": "Quantum critical points as CFTs", "kind": "method transfer", "summary": "Many z=1 quantum critical points are described by conformal field theories (e.g. O(N) Wilson-Fisher in 2+1D) whose finite-T response is universal and Planckian (tau ~ hbar/k_BT); holographic CFTs model strongly coupled transport.", "map": "\\frac{\\hbar}{\\tau}\\approx\\alpha k_BT;\\ \\sigma(\\omega,T)=\\frac{e^2}{\\hbar}\\Sigma(\\hbar\\omega/k_BT)\\ (\\text{2+1D CFT})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2276", "a": "06-particle-physics/quantum-field-theory/conformal-field-theory", "b": "08-condensed-matter/topological-matter/quantum-hall-effects", "name": "FQH edges and wavefunctions from CFT", "kind": "identity", "summary": "Edges of quantum Hall states are chiral CFTs, and bulk wavefunctions are CFT conformal blocks: the Laughlin state from a U(1) boson, the Moore-Read Pfaffian from the Ising CFT, whose sigma fields become non-abelian anyons.", "map": "\\Psi_{MR}=\\mathrm{Pf}\\!\\left(\\frac{1}{z_i-z_j}\\right)\\prod_{i<j}(z_i-z_j)^2e^{-\\sum|z|^2/4\\ell_B^2};\\ c_{\\text{edge}}=1\\ (\\text{Laughlin})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2277", "a": "06-particle-physics/quantum-field-theory/effective-field-theory", "b": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "name": "Goldstone EFT: pions and magnons", "kind": "method transfer", "summary": "Chiral perturbation theory's EFT of Goldstone bosons describes magnons: antiferromagnetic magnons are relativistic-like (O(3) sigma model, omega ~ k) while ferromagnetic ones are type-B Goldstones (omega ~ k^2) that count once per pair of broken generators.", "map": "n_A+2n_B=n_{BG}\\ (\\text{Watanabe-Murayama});\\ \\mathcal L=\\tfrac{\\rho_s}{2}(\\partial_\\mu\\mathbf n)^2\\ \\leftrightarrow\\ \\tfrac{f_\\pi^2}{4}\\mathrm{Tr}\\,\\partial U\\partial U^\\dagger", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2278", "a": "06-particle-physics/quantum-field-theory/effective-field-theory", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Fermi-surface EFT: BCS as the marginal instability", "kind": "method transfer", "summary": "Treating the Fermi liquid as an EFT with RG scaling toward the Fermi surface shows only forward and BCS couplings survive, and an attractive BCS coupling is marginally relevant and runs to a gap.", "map": "\\frac{dV_{BCS}}{d\\ln(\\Lambda_0/\\Lambda)}=-N(0)V_{BCS}^2\\Rightarrow\\Delta\\sim\\omega_De^{-1/N(0)|V|}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2279", "a": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "b": "08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids", "name": "Emergent QED in quantum spin ice", "kind": "identity", "summary": "The low-energy theory of a U(1) quantum spin liquid on the pyrochlore lattice is compact U(1) gauge theory: gapless emergent photons with omega ~ k, gapped electric charges (spinons) and magnetic monopoles.", "map": "H_{\\text{eff}}=\\frac{U}{2}\\sum\\mathbf E^2-K\\sum_{\\hexagon}\\cos(\\nabla\\times\\mathbf A),\\ \\omega=c_{\\text{em}}k", "breaks": "The emergent speed of light is ~meV scale and lattice-cut off; the emergent fine-structure constant and charges are not tied to QED's, and Lorentz invariance is only approximate.", "confidence": "current research", "strength": 2}
{"id": "C2280", "a": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "b": "08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order", "name": "Topological order as deconfined lattice gauge theory", "kind": "identity", "summary": "Z2 topological order (toric code, Z2 spin liquids) is the deconfined phase of Wegner's Z2 lattice gauge theory; anyons are its electric charges and fluxes, and the Wilson-loop perimeter law is the condensed-matter signature of deconfinement.", "map": "H_{TC}=-\\sum_vA_v-\\sum_pB_p\\ \\leftrightarrow\\ \\text{Gauss law }A_v=1,\\ B_p=\\prod_{\\square}\\sigma^z\\ (\\text{plaquette})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2281", "a": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Ginzburg-Landau is the abelian Higgs model", "kind": "identity", "summary": "Ginzburg-Landau theory is the abelian Higgs model with charge 2e; Abrikosov vortices are Nielsen-Olesen strings and the type-I/II boundary kappa=1/sqrt2 is the BPS point where vortices do not interact.", "map": "F=|(\\nabla-2ie\\mathbf A)\\psi|^2+a|\\psi|^2+\\tfrac b2|\\psi|^4+\\tfrac{B^2}{2\\mu_0}\\ \\leftrightarrow\\ \\mathcal L_{AH};\\ \\kappa=\\lambda/\\xi=1/\\sqrt2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2282", "a": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "b": "08-condensed-matter/superconductivity/cuprate-high-tc-superconductors", "name": "Emergent gauge fields in the doped Mott insulator", "kind": "method transfer", "summary": "Slave-particle (parton) descriptions of the cuprates split the electron into spinons and holons coupled by an emergent U(1) or SU(2) gauge field, importing gauge-theory confinement and Higgs phases into high-Tc theory.", "map": "c_{i\\sigma}=b_i^\\dagger f_{i\\sigma},\\ \\sum_\\sigma f^\\dagger f+b^\\dagger b=1\\ (\\text{gauge constraint})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2283", "a": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "Berry connection as a gauge field on the Brillouin zone", "kind": "identity", "summary": "The Berry connection is a U(1) (or, for degenerate bands, Wilczek-Zee non-abelian) gauge field over momentum space; Chern numbers are its first Chern class, the same topology as monopole and instanton charges.", "map": "\\mathcal A_n=i\\langle u_n|\\nabla_{\\mathbf k}u_n\\rangle,\\ \\Omega=\\nabla\\times\\mathcal A,\\ C=\\frac{1}{2\\pi}\\int_{BZ}\\Omega\\,d^2k\\in\\mathbb Z", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2284", "a": "06-particle-physics/quantum-field-theory/lattice-field-theory", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "Shared Monte Carlo, sign problem and tensor networks", "kind": "method transfer", "summary": "Lattice QCD and correlated-electron numerics share hybrid/determinant Monte Carlo and the fermion sign problem; tensor networks developed for spin chains now simulate lattice gauge theories at finite density and in real time.", "map": "\\langle O\\rangle=\\frac{\\int O\\det M\\,e^{-S}}{\\int\\det M\\,e^{-S}},\\ \\det M\\ \\text{not positive}\\Rightarrow\\text{sign problem}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2285", "a": "06-particle-physics/quantum-field-theory/lattice-field-theory", "b": "08-condensed-matter/topological-matter/topological-insulators", "name": "Domain-wall fermions are topological boundary states", "kind": "identity", "summary": "Kaplan's domain-wall fermions get lattice chiral fermions as zero modes bound to a mass domain wall in one higher dimension, the same Jackiw-Rebbi mechanism that produces protected surface Dirac cones of topological insulators.", "map": "(i\\gamma^\\mu\\partial_\\mu-m(s))\\psi=0,\\ m(s)\\to\\pm m\\ \\Rightarrow\\ \\psi_0\\propto e^{-\\int^s m(s')ds'}\\ (\\text{chiral zero mode})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2286", "a": "06-particle-physics/quantum-field-theory/lattice-field-theory", "b": "08-condensed-matter/topological-matter/topological-semimetals", "name": "Nielsen-Ninomiya doubling forces paired Weyl nodes", "kind": "identity", "summary": "The no-go theorem that lattice chiral fermions come in pairs of opposite chirality is the reason Weyl nodes in a crystal always appear in pairs, and Nielsen and Ninomiya themselves proposed the crystal chiral anomaly.", "map": "\\sum_{\\text{nodes}}\\chi_i=0\\ (\\text{compact Brillouin zone})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2287", "a": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "name": "Running Fermi velocity in graphene", "kind": "method transfer", "summary": "Coulomb interactions renormalize graphene's Fermi velocity logarithmically, like a running coupling, because alpha_g is marginal; suspended graphene shows the predicted log enhancement near the Dirac point.", "map": "v_F(k)=v_F(\\Lambda)\\left[1+\\frac{\\alpha_g}{4}\\ln\\frac{\\Lambda}{k}\\right]", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2288", "a": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "b": "08-condensed-matter/strongly-correlated-electrons/heavy-fermions-and-kondo-physics", "name": "Kondo temperature as dimensional transmutation", "kind": "identity", "summary": "The antiferromagnetic Kondo coupling is marginally relevant, so it grows at low energy like an asymptotically free coupling and generates a scale T_K exactly as Lambda_QCD emerges; Wilson's numerical RG solved it.", "map": "\\frac{dJ}{d\\ln D}=-\\rho J^2\\Rightarrow T_K\\sim De^{-1/\\rho J}\\ \\leftrightarrow\\ \\Lambda_{QCD}=\\mu\\,e^{-8\\pi^2/(b_0g^2(\\mu))}", "breaks": "Kondo is a 0+1D impurity problem with no gauge field or confinement; the strong-coupling fixed point is a screened singlet (Fermi liquid), not a confined hadron spectrum.", "confidence": "established", "strength": 3}
{"id": "C2289", "a": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "DMRG born from the failure of real-space RG", "kind": "historical", "summary": "White's DMRG replaced Wilson-style energy truncation by density-matrix truncation, turning real-space renormalization into the most accurate 1D many-body method and the seed of tensor-network RG.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2290", "a": "06-particle-physics/standard-model", "b": "08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order", "name": "Could photons and electrons be emergent?", "kind": "analogy", "summary": "String-net condensation produces emergent U(1) gauge bosons and fermionic charges from local bosonic spins, suggesting the Standard Model's gauge fields and fermions might themselves be emergent.", "map": "", "breaks": "No string-net model reproduces chiral fermions, non-abelian SU(3)xSU(2)xU(1), or exact Lorentz invariance; chiral gauge theories resist lattice regularization.", "confidence": "proposed", "strength": 1}
{"id": "C2291", "a": "06-particle-physics/standard-model", "b": "08-condensed-matter/superconductivity", "name": "Higgs mechanism first appeared as the Meissner effect", "kind": "historical", "summary": "The idea that a condensate gives a gauge field mass migrated from superconductivity (London, Nambu, Anderson) to the Standard Model's electroweak sector.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2292", "a": "06-particle-physics/standard-model/higgs-boson", "b": "08-condensed-matter/superconductivity", "name": "Anderson-Higgs mechanism: photon mass = W mass", "kind": "identity", "summary": "A superconductor's Cooper-pair condensate eats the phase Goldstone mode and gives the photon a mass 1/lambda_L (Meissner effect), the same abelian Higgs mechanism that gives W and Z masses from the Higgs vev.", "map": "m_\\gamma c^2=\\frac{\\hbar c}{\\lambda_L},\\ \\lambda_L^{-2}=\\mu_0n_se^2/m\\ \\leftrightarrow\\ m_W=\\tfrac12gv;\\ \\Delta\\leftrightarrow\\langle H\\rangle,\\ 2e\\leftrightarrow g", "breaks": "The SC condensate is a composite of electrons, non-relativistic and in a medium with a preferred frame; the electroweak condensate is (as far as known) elementary and Lorentz invariant, and its gauge group is non-abelian.", "confidence": "established", "strength": 3}
{"id": "C2293", "a": "06-particle-physics/standard-model/higgs-boson", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Higgs amplitude mode in superconductors", "kind": "identity", "summary": "The Higgs boson is the amplitude oscillation of the condensate; superconductors have the same mode at energy 2Delta, observed in Raman and terahertz pump-probe experiments.", "map": "m_h^2=2\\lambda v^2\\ \\leftrightarrow\\ \\omega_H=2\\Delta;\\ \\delta|\\psi|\\ \\text{(amplitude)}\\ \\text{vs}\\ \\delta\\phi\\ \\text{(eaten phase)}", "breaks": "In a superconductor the mode sits at the pair-breaking edge and can decay into quasiparticles; its observation needs coupling via a CDW or nonlinear drive since it is Raman- but not dipole-active.", "confidence": "current research", "strength": 2}
{"id": "C2294", "a": "06-particle-physics/standard-model/quantum-chromodynamics", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Color superconductivity in dense quark matter", "kind": "mechanism", "summary": "At high baryon density attractive one-gluon exchange in the color antitriplet channel makes quarks Cooper-pair near the Fermi surface; in the CFL phase the diquark condensate Higgses all eight gluons (color Meissner effect).", "map": "\\langle q^a_{i\\alpha}q^b_{j\\beta}\\rangle\\propto\\Delta\\,\\epsilon^{abI}\\epsilon_{\\alpha\\beta I}\\ (\\text{CFL});\\ \\Delta\\sim10\\text{-}100\\ \\text{MeV}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2295", "a": "06-particle-physics/standard-model/quantum-chromodynamics", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Confinement as a dual Meissner effect", "kind": "analogy", "summary": "If chromomagnetic monopoles condense, chromoelectric flux is squeezed into tubes just as magnetic flux is in a type-II superconductor, giving a linear quark potential with string tension sigma.", "map": "V(r)\\approx\\sigma r,\\ \\sigma\\approx0.18\\ \\text{GeV}^2\\ \\leftrightarrow\\ \\text{vortex energy per length }\\varepsilon_1\\approx\\frac{\\Phi_0^2}{4\\pi\\mu_0\\lambda^2}\\ln\\kappa", "breaks": "The roles of E and B are swapped, the gauge group is non-abelian, and monopole condensation in QCD is gauge-dependent and unproven analytically.", "confidence": "current research", "strength": 2}
{"id": "C2296", "a": "06-particle-physics/standard-model/quantum-chromodynamics", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "NJL: chiral symmetry breaking modelled on BCS", "kind": "historical", "summary": "Nambu and Jona-Lasinio built dynamical mass generation for nucleons by direct analogy with the BCS gap equation; the massless Goldstone mode of the analogy became the pion, a precursor of QCD chiral symmetry breaking.", "map": "\\Delta=gN(0)\\int_0^{\\omega_D}\\frac{\\Delta\\,d\\xi}{\\sqrt{\\xi^2+\\Delta^2}}\\ \\leftrightarrow\\ M=\\frac{2G}{\\pi^2}\\int_0^\\Lambda\\frac{M\\,p^2dp}{\\sqrt{p^2+M^2}}", "breaks": "", "confidence": "established", "strength": 3}
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