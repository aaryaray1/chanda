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

### Precision anomalies and muon g−2 · `knowledge/06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2`

**Scope.** Muon anomalous magnetic moment (BNL E821, Fermilab E989), hadronic vacuum polarization from $e^+e^-$ data vs. lattice QCD, the $R_{K^{(*)}}$ saga (2014–2022 hints, resolved by LHCb 2022), $R_{D^{(*)}}$, the CDF $W$ mass, electron EDM bounds, proton-radius puzzle.

**Core ideas.**
- $a_\mu=(g-2)/2$ probes loops of every particle coupling to the muon; new physics scales as $m_\mu^2/\Lambda^2$.
- The comparison is limited by the theory side: hadronic vacuum polarization dominates the uncertainty, and lattice results (BMW 2020 onward) moved the prediction toward experiment.
- Lesson: many 3–4σ anomalies fade; trust results confirmed by independent methods.

**Key equations.**
$$a_\mu^{\text{QED, 1-loop}}=\frac{\alpha}{2\pi}\ (\text{Schwinger}),\qquad \Delta a_\mu^{\text{NP}}\sim\frac{m_\mu^2}{\Lambda^2}\times\text{couplings}$$

**Landmark.** Aoyama et al. (2020). "The anomalous magnetic moment of the muon in the Standard Model". *Phys. Rep.* 887, 1. [arXiv:2006.04822](https://arxiv.org/abs/2006.04822)

**See also.** [Lattice field theory](knowledge/06-particle-physics/quantum-field-theory/lattice-field-theory/README.md) · [Measurement uncertainty](knowledge/00-foundations/measurement-and-data-analysis/uncertainty-and-error-propagation/README.md)

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

### Future colliders · `knowledge/06-particle-physics/collider-and-experimental-particle-physics/future-colliders`

**Scope.** Higgs factories ($e^+e^-\to ZH$ at 240–250 GeV), Z-pole "Tera-Z" runs, top threshold, 100 TeV hadron collider, multi-TeV muon colliders, plasma-wakefield accelerators, European Strategy for Particle Physics updates.

**Core ideas.**
- Lepton colliders give clean initial states and precise Higgs couplings at the sub-percent level.
- Synchrotron loss $\propto E^4/(m^4R)$ limits circular $e^+e^-$ machines; muons radiate $(m_e/m_\mu)^4\approx5\times10^{-10}$ times less but decay in 2.2 μs.
- Physics case: Higgs couplings, self-coupling, electroweak precision, direct reach for new particles.

**Key equations.**
$$P_{\text{sync}}=\frac{e^2c}{6\pi\epsilon_0}\frac{\gamma^4}{R^2}$$

**See also.** [Plasma wakefield acceleration](knowledge/10-plasma-physics/inertial-and-laser-plasmas/plasma-wakefield-acceleration/README.md) · [Synchrotron radiation](knowledge/02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges/README.md)

### Hadron colliders and the LHC · `knowledge/06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc`

**Scope.** LHC ring (27 km, 8.3 T dipoles), $\sqrt s$ = 7, 8, 13, 13.6 TeV, experiments (ATLAS, CMS, LHCb, ALICE), luminosity and pile-up, HL-LHC upgrade (3000 fb⁻¹), Tevatron legacy (top quark discovery).

**Core ideas.**
- Protons are composite, so the partonic collision energy varies event-by-event; most collisions are soft QCD.
- Discovery reach is set by parton luminosities that fall steeply with mass.
- General-purpose detectors (ATLAS/CMS) vs. specialized (LHCb forward flavor, ALICE heavy ions).

**Key equations.**
$$\mathcal L=\frac{f\,n_b\,N_1N_2}{4\pi\sigma_x\sigma_y}F,\qquad \hat s=x_1x_2s$$

**See also.** [Higgs boson](knowledge/06-particle-physics/standard-model/higgs-boson/README.md) · [Beam dynamics](knowledge/11-interdisciplinary-physics/accelerator-physics/beam-dynamics/README.md)

### Jets and QCD phenomenology · `knowledge/06-particle-physics/collider-and-experimental-particle-physics/jets-and-qcd-phenomenology`

**Scope.** Infrared and collinear (IRC) safety, sequential-recombination algorithms (kt, Cambridge/Aachen, anti-kt), jet energy scale, parton showers and resummation, boosted-object tagging ($W$, top, Higgs), jet grooming (soft drop), quark/gluon discrimination.

**Core ideas.**
- Observables must be IRC safe to be calculable in perturbation theory.
- Anti-kt (distance $d_{ij}=\min(k_{ti}^{-2},k_{tj}^{-2})\Delta R_{ij}^2/R^2$) gives cone-like, IRC-safe jets — the LHC standard.
- Substructure reveals boosted heavy particles decaying into one fat jet.

**Key equations.**
$$d_{ij}=\min\!\left(p_{Ti}^{2p},p_{Tj}^{2p}\right)\frac{\Delta R_{ij}^2}{R^2},\qquad p=-1\ (\text{anti-}k_t)$$

**Landmark.** Cacciari, Salam & Soyez (2008) — see [subfield landmarks](knowledge/06-particle-physics/collider-and-experimental-particle-physics/README.md).

**See also.** [QCD](knowledge/06-particle-physics/standard-model/quantum-chromodynamics/README.md) · [ML in HEP](knowledge/06-particle-physics/collider-and-experimental-particle-physics/machine-learning-in-hep/README.md)

### Machine learning in high-energy physics · `knowledge/06-particle-physics/collider-and-experimental-particle-physics/machine-learning-in-hep`

**Scope.** Graph neural networks and transformers on particle clouds (ParticleNet, ParT), b-tagging, generative models for calorimeter simulation, FPGA inference in triggers, weakly/unsupervised anomaly detection, simulation-based (likelihood-free) inference, foundation models for jets.

**Core ideas.**
- Events are naturally sets/graphs of particles; permutation-invariant architectures fit the data.
- Classifier outputs approximate likelihood ratios (Neyman–Pearson), connecting ML to optimal statistics.
- Systematic uncertainties and simulation–data mismatch are the main obstacles to trusting ML in final results.

**Key equations.**
$$s^*(x)=\frac{p(x|S)}{p(x|S)+p(x|B)}\ \Rightarrow\ \frac{s^*}{1-s^*}=\frac{p(x|S)}{p(x|B)}$$

**See also.** [Machine learning for physics](knowledge/00-foundations/computational-physics/machine-learning-for-physics/README.md) · [Jets](knowledge/06-particle-physics/collider-and-experimental-particle-physics/jets-and-qcd-phenomenology/README.md)

### Monte Carlo event generators · `knowledge/06-particle-physics/collider-and-experimental-particle-physics/monte-carlo-event-generators`

**Scope.** Matrix-element generators (MadGraph5_aMC@NLO), general-purpose generators (PYTHIA, Herwig, Sherpa), NLO matching (MC@NLO, POWHEG), merging (CKKW, MLM), hadronization models (Lund string, cluster), underlying event and tuning, detector simulation (Geant4).

**Core ideas.**
- Factorize the event into hard process (fixed order), shower (resummed soft/collinear emissions), hadronization (non-perturbative model), decays.
- Matching avoids double counting between fixed-order and shower emissions.
- Generators are both theory tools and the backbone of every analysis's background model.

**Key equations.**
$$\Delta(t_1,t_2)=\exp\!\left[-\int_{t_2}^{t_1}\frac{dt}{t}\int dz\,\frac{\alpha_s}{2\pi}P(z)\right]\ (\text{Sudakov factor})$$

**See also.** [Monte Carlo methods](knowledge/00-foundations/computational-physics/monte-carlo-methods/README.md)

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

### Feynman diagrams and scattering amplitudes · `knowledge/06-particle-physics/quantum-field-theory/feynman-diagrams-and-scattering-amplitudes`

**Scope.** Feynman rules, tree and loop amplitudes, cross sections and decay rates, spinor-helicity formalism, BCFW recursion, unitarity methods, the amplituhedron, double copy (gravity = gauge²).

**Core ideas.**
- Each diagram is a term in the perturbative expansion of the S-matrix; vertices come from the interaction Lagrangian.
- Gauge-theory amplitudes are far simpler than their diagram count suggests (Parke–Taylor), motivating on-shell methods that never use off-shell gauge-dependent pieces.
- Generalized unitarity builds loop amplitudes from products of trees.

**Key equations.**
$$d\sigma = \frac{|\mathcal M|^2}{4\sqrt{(p_1\cdot p_2)^2-m_1^2m_2^2}}\,d\Pi_n,\qquad A^{\text{MHV}}_n=\frac{\langle ij\rangle^4}{\langle12\rangle\langle23\rangle\cdots\langle n1\rangle}$$

**Landmark.** Parke & Taylor (1986). "Amplitude for n-Gluon Scattering". *Phys. Rev. Lett.* 56, 2459. [doi:10.1103/PhysRevLett.56.2459](https://doi.org/10.1103/PhysRevLett.56.2459)

**Open questions.** Is there a formulation of QFT in which locality and unitarity are emergent (amplituhedron program)? Precision multi-loop amplitudes for LHC backgrounds.

**See also.** [Jets and QCD phenomenology](knowledge/06-particle-physics/collider-and-experimental-particle-physics/jets-and-qcd-phenomenology/README.md)

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

### CP violation · `knowledge/06-particle-physics/standard-model/cp-violation`

**Scope.** Discovery in neutral kaons (1964), $\epsilon$ and $\epsilon'$, CP violation in mixing vs. decay vs. interference, $B$-factory measurements of $\sin2\beta$, LHCb charm CP violation (2019), Jarlskog invariant, strong-CP problem, leptonic CP violation.

**Core ideas.**
- With three generations the CKM matrix has one irreducible phase → CP violation (Kobayashi–Maskawa).
- All CP violation in the quark sector scales with the Jarlskog invariant $J\approx3\times10^{-5}$ — far too small to explain the cosmic baryon asymmetry.
- CPT is exact in local Lorentz-invariant QFT, so CP violation ⇔ T violation.

**Key equations.**
$$J=\mathrm{Im}(V_{us}V_{cb}V_{ub}^*V_{cs}^*),\qquad \eta_B=\frac{n_B-n_{\bar B}}{n_\gamma}\approx6\times10^{-10}$$

**Landmark.** Christenson, Cronin, Fitch & Turlay (1964). "Evidence for the 2π Decay of the K₂⁰ Meson". *Phys. Rev. Lett.* 13, 138. [doi:10.1103/PhysRevLett.13.138](https://doi.org/10.1103/PhysRevLett.13.138)

**See also.** [Baryogenesis](knowledge/06-particle-physics/beyond-the-standard-model/baryogenesis-and-matter-antimatter/README.md) · [Discrete symmetries and CPT](knowledge/00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt/README.md)

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

# Packet 06-2 (100 records)

{"id": "C1074", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/electrostatics-and-boundary-value-problems", "b": "06-particle-physics/quantum-field-theory/feynman-diagrams-and-scattering-amplitudes", "name": "Coulomb's law as the photon propagator", "kind": "identity", "summary": "The Green's function of Poisson's equation is the Fourier transform of the static one-photon-exchange propagator 1/q². In the Born approximation, tree-level exchange of a massless boson gives the 1/r potential and a massive one gives Yukawa's e^{-mr}/r.", "map": "\\int\\frac{d^3q}{(2\\pi)^3}\\frac{e^{i\\mathbf q\\cdot\\mathbf r}}{\\mathbf q^2+m^2}=\\frac{e^{-mr}}{4\\pi r}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1075", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/fields-in-matter", "b": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "name": "Vacuum polarization: the vacuum as a dielectric", "kind": "analogy", "summary": "Virtual e⁺e⁻ pairs screen a bare charge the way bound charges do in a dielectric, so the effective charge grows at short distances (the Uehling potential). The running α(Q²) behaves like a scale-dependent permittivity, rising from 1/137 to about 1/128 at m_Z.", "map": "\\alpha_{\\rm eff}(Q^2)\\simeq\\frac{\\alpha}{1-\\frac{\\alpha}{3\\pi}\\ln(Q^2/m_e^2)},\\quad \\alpha^{-1}(m_Z)\\approx128", "breaks": "Lorentz invariance forces εμ = 1 for the vacuum (there is no rest frame), the response depends on q² rather than on frequency alone, and the screening is UV-divergent. The bare charge cannot be observed, so it has to be renormalized.", "confidence": "established", "strength": 3}
{"id": "C1076", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/fields-in-matter", "b": "06-particle-physics/standard-model/quantum-chromodynamics", "name": "Asymptotic freedom as vacuum paramagnetism", "kind": "analogy", "summary": "Since εμ = 1 for a relativistic vacuum, antiscreening (ε < 1) is the same thing as paramagnetism (μ > 1). In the Nielsen–Hughes picture, the Pauli paramagnetism of spin-1 gluons outweighs their orbital Landau diamagnetism and quark screening, which gives the sign of the QCD β-function.", "map": "\\epsilon\\mu=1,\\quad \\beta_0\\propto\\sum(-1)^{2s}\\left[(2s)^2-\\tfrac13\\right]\\ \\Rightarrow\\ \\beta_0=\\tfrac{11}{3}C_A-\\tfrac43T_Fn_f", "breaks": "The picture is one-loop and perturbative. It says nothing directly about confinement, and the constant chromomagnetic background it uses is unstable (Nielsen–Olesen).", "confidence": "established", "strength": 2}
{"id": "C1077", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/magnetostatics", "b": "06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers", "name": "Magnetic spectrometry: momentum from track curvature", "kind": "method transfer", "summary": "Collider detectors measure momentum from how much charged tracks bend in solenoid or toroid fields (the 3.8 T CMS solenoid, the ATLAS toroids), designed from Biot–Savart field maps. Because the sagitta shrinks as 1/p, momentum resolution degrades in proportion to p.", "map": "p_T[\\mathrm{GeV}/c]=0.3\\,B[\\mathrm T]\\,R[\\mathrm m],\\quad s\\approx\\frac{0.3\\,BL^2}{8\\,p_T},\\quad \\frac{\\sigma_p}{p}\\propto\\frac{p\\,\\sigma_s}{BL^2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1078", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/magnetostatics", "b": "06-particle-physics/neutrino-physics/neutrino-mass-and-double-beta-decay", "name": "MAC-E filter: adiabatic magnetic collimation (KATRIN)", "kind": "method transfer", "summary": "Tritium β electrons spiral along a field that falls by ~10⁴ from the source to the analysing plane. Adiabatic invariance of the magnetic moment converts transverse into longitudinal energy, so an electrostatic retarding potential becomes a sharp high-pass filter. KATRIN used this to set m_ν < 0.45 eV (90% CL, 2025).", "map": "\\mu=\\frac{E_\\perp}{B}=\\text{const}\\ \\Rightarrow\\ \\frac{\\Delta E}{E}=\\frac{B_{\\min}}{B_{\\max}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1079", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/multipole-expansions", "b": "06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc", "name": "2D multipole expansion of accelerator magnets", "kind": "method transfer", "summary": "Accelerator magnet fields are written as a complex 2D multipole series: dipoles bend, quadrupoles focus, sextupoles correct chromaticity and octupoles damp instabilities. LHC magnet quality is specified by the error coefficients b_n and a_n, in units of 10⁻⁴ at R_ref = 17 mm.", "map": "B_y+iB_x=B_{\\rm ref}\\sum_{n\\ge1}(b_n+ia_n)\\left(\\frac{x+iy}{R_{\\rm ref}}\\right)^{n-1}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1080", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/multipole-expansions", "b": "06-particle-physics/standard-model/cp-violation", "name": "Electric dipole moments as P- and T-odd multipoles", "kind": "mechanism", "summary": "A permanent EDM along a particle's spin is odd under both P and T, so by CPT it signals CP violation. Electron (ACME, JILA) and neutron EDM limits probe CP violation far beyond the tiny CKM-phase prediction and constrain baryogenesis models.", "map": "H=-\\mu\\,\\boldsymbol\\sigma\\cdot\\mathbf B-d\\,\\boldsymbol\\sigma\\cdot\\mathbf E,\\quad P,T:\\ \\boldsymbol\\sigma\\cdot\\mathbf E\\to-\\boldsymbol\\sigma\\cdot\\mathbf E", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1081", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/multipole-expansions", "b": "06-particle-physics/standard-model/hadron-spectroscopy-and-exotics", "name": "E1/M1 radiative transitions in quarkonium", "kind": "method transfer", "summary": "Radiative decays such as ψ(2S)→γχ_cJ (E1) and J/ψ→γη_c (M1) obey the same multipole selection rules and rate formulas as atomic transitions. They were used to map the charmonium and bottomonium spectra and to test potential models.", "map": "\\Gamma(^3S_1\\to\\gamma\\,^3P_J)=\\frac{4}{27}\\,\\alpha\\,e_Q^2\\,(2J+1)\\,\\omega^3\\,|\\langle r\\rangle|^2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1082", "a": "02-electromagnetism-and-optics/photonics-and-lasers/metamaterials-and-plasmonics", "b": "06-particle-physics/standard-model/electroweak-theory", "name": "Plasma frequency as photon mass: Anderson's route to Higgs", "kind": "historical", "summary": "Transverse waves in a plasma obey ω² = ω_p² + c²k², the dispersion relation of a massive photon. From plasmons and the Meissner effect, Anderson (1963) argued that gauge bosons can gain mass without a leftover Goldstone boson. Englert–Brout, Higgs and Guralnik–Hagen–Kibble made this precise, and it became electroweak symmetry breaking.", "map": "\\omega^2=\\omega_p^2+c^2k^2\\ \\leftrightarrow\\ E^2=m^2c^4+p^2c^2,\\quad m_\\gamma c^2=\\hbar\\omega_p\\ \\leftrightarrow\\ m_W=\\tfrac12gv", "breaks": "A plasma picks out a rest frame and breaks Lorentz invariance, and its longitudinal plasmon is not the W's longitudinal mode. The Higgs vacuum is Lorentz-invariant and has a physical scalar left over.", "confidence": "established", "strength": 2}
{"id": "C1083", "a": "02-electromagnetism-and-optics/photonics-and-lasers/nonlinear-optics", "b": "06-particle-physics/quantum-field-theory/effective-field-theory", "name": "Euler–Heisenberg: the QED vacuum as a Kerr medium", "kind": "identity", "summary": "Integrating out the electron leaves four-photon operators suppressed by 1/m_e⁴, which act as a third-order susceptibility χ⁽³⁾ of the vacuum. This predicts light-by-light scattering, observed by ATLAS and CMS in ultraperipheral Pb–Pb collisions, and vacuum birefringence in strong fields, which has not yet been seen in the laboratory.", "map": "\\mathcal L_{EH}=\\frac{2\\alpha^2}{45m_e^4}\\left[(\\mathbf E^2-\\mathbf B^2)^2+7(\\mathbf E\\cdot\\mathbf B)^2\\right]\\ (\\hbar=c=1)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1084", "a": "02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics", "b": "06-particle-physics/quantum-field-theory/feynman-diagrams-and-scattering-amplitudes", "name": "Strong-field QED at the laser intensity frontier", "kind": "shared object", "summary": "Chirped-pulse amplification pushes laser fields toward the Schwinger critical field. Once the normalized amplitude a₀ ≫ 1, multiphoton processes stop being perturbative in the laser field, so nonlinear Compton scattering and multiphoton Breit–Wheeler pair creation (SLAC E144) are computed with laser-dressed Volkov propagators (Furry picture).", "map": "E_S=\\frac{m_e^2c^3}{e\\hbar}\\approx1.3\\times10^{18}\\,\\mathrm{V/m},\\quad a_0=\\frac{eE}{m_e\\omega c},\\quad \\chi\\sim\\frac{\\gamma E}{E_S}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1085", "a": "02-electromagnetism-and-optics/radiation-and-scattering/cherenkov-and-transition-radiation", "b": "06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers", "name": "Cherenkov and transition-radiation particle ID", "kind": "method transfer", "summary": "RICH and DIRC detectors measure β from the Cherenkov angle, which together with the tracker momentum gives the mass and separates π, K and p (LHCb, ALICE, Belle II). Transition-radiation detectors such as the ATLAS TRT separate electrons from pions using the γ-dependence of transition-radiation yield.", "map": "\\cos\\theta_C=\\frac{1}{n\\beta},\\quad m=\\frac{p}{c}\\sqrt{n^2\\cos^2\\theta_C-1},\\quad W_{TR}=\\tfrac13\\alpha\\gamma\\hbar\\omega_p", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1086", "a": "02-electromagnetism-and-optics/radiation-and-scattering/cherenkov-and-transition-radiation", "b": "06-particle-physics/neutrino-physics/neutrino-experiments-and-sources", "name": "Cherenkov light as the neutrino detector", "kind": "method transfer", "summary": "Water and ice detectors (Super-K, SNO, IceCube) see neutrino interactions through the Cherenkov cones of the charged secondaries. A sharp ring marks a muon and a fuzzy ring an electron shower, and the cone direction points back to the source. At EeV energies, coherent Askaryan radio emission from the shower's charge excess takes over (ARA, RNO-G).", "map": "\\cos\\theta_C=\\frac{1}{n\\beta},\\quad \\theta_C\\approx41^\\circ\\ \\text{(water, }\\beta\\to1)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1087", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "06-particle-physics/collider-and-experimental-particle-physics/future-colliders", "name": "Synchrotron loss sets collider size and choice of particle", "kind": "mechanism", "summary": "The relativistic Larmor (Liénard) power of a charge on a circular orbit grows as γ⁴/R², so the energy lost per turn limits circular e⁺e⁻ machines (the size of FCC-ee and CEPC). This pushes designs toward linear colliders or muons, which radiate (m_e/m_μ)⁴ ≈ 5×10⁻¹⁰ times less.", "map": "P=\\frac{e^2c}{6\\pi\\epsilon_0}\\frac{\\gamma^4}{R^2},\\quad U_0=\\frac{e^2\\gamma^4}{3\\epsilon_0R}\\propto\\frac{E^4}{m^4R}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1088", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "06-particle-physics/collider-and-experimental-particle-physics/jets-and-qcd-phenomenology", "name": "Angular ordering from coherent soft radiation", "kind": "analogy", "summary": "In the QED Chudakov effect, a fresh e⁺e⁻ pair radiates soft photons mainly inside its opening angle, because outside it the pair looks neutral and the two amplitudes cancel. The same coherence orders successive gluon emissions in angle, which underlies angular-ordered parton showers and the hump-backed plateau of hadron spectra in jets.", "map": "W_{ij}=\\frac{1-\\cos\\theta_{ij}}{(1-\\cos\\theta_{ik})(1-\\cos\\theta_{jk})}\\ \\Rightarrow\\ \\text{azimuthal average}\\approx0\\text{ for }\\theta_{ik}>\\theta_{ij}", "breaks": "Gluons carry colour and radiate themselves (C_A vs C_F). Colour-interference terms beyond leading N_c and non-global logarithms have no QED counterpart.", "confidence": "established", "strength": 2}
{"id": "C1089", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers", "name": "Bremsstrahlung, radiation length and EM showers", "kind": "mechanism", "summary": "High-energy electrons lose energy by bremsstrahlung (the QED version of radiation from a decelerated charge) and photons convert to pairs over 9X₀/7. Alternating these processes builds an electromagnetic shower whose depth grows like ln E, which is the basis of electromagnetic calorimetry.", "map": "\\frac{dE}{dx}\\Big|_{\\rm brems}=-\\frac{E}{X_0},\\quad \\lambda_{\\rm pair}=\\tfrac97X_0,\\quad t_{\\max}\\approx\\ln\\frac{E}{E_c}-0.5\\ (e^-)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1090", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "06-particle-physics/neutrino-physics/neutrino-mass-and-double-beta-decay", "name": "Cyclotron radiation emission spectroscopy (Project 8)", "kind": "method transfer", "summary": "Single β-decay electrons trapped in a magnetic field emit femtowatt cyclotron radiation, and its relativistic frequency gives their energy. Project 8 measured a first tritium spectrum and neutrino-mass limit this way (2023) and aims for ~40 meV sensitivity with atomic tritium.", "map": "f_c=\\frac{1}{2\\pi}\\frac{eB}{\\gamma m_e}=\\frac{1}{2\\pi}\\frac{eB}{m_e+E_{\\rm kin}/c^2},\\quad P_{\\rm Larmor}\\propto\\frac{e^4B^2\\beta_\\perp^2\\gamma^2}{m_e^2}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1091", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "06-particle-physics/quantum-field-theory/feynman-diagrams-and-scattering-amplitudes", "name": "Soft-photon theorem: classical radiation from sudden kicks", "kind": "identity", "summary": "The low-frequency Liénard–Wiechert spectrum of charges whose velocities change suddenly is exactly Weinberg's soft factor multiplying any QED amplitude. Its 1/ω photon number is the infrared divergence, which Bloch–Nordsieck summation over unresolved soft photons removes.", "map": "\\mathcal M_{n+\\gamma}\\xrightarrow{k\\to0}e\\sum_i\\eta_i\\frac{p_i\\cdot\\epsilon}{p_i\\cdot k}\\,\\mathcal M_n,\\qquad \\frac{dN_\\gamma}{d\\omega}\\propto\\frac{1}{\\omega}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1092", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "name": "Classical self-energy and radiation reaction → mass renormalization", "kind": "historical", "summary": "A point electron's field energy diverges linearly as its radius goes to zero, and Abraham–Lorentz radiation reaction has runaway solutions. QED softens the divergence to a logarithm (Weisskopf 1939, through positron screening) and absorbs it into the observed mass — the first renormalization.", "map": "m_{\\rm obs}=m_0+\\frac{e^2}{6\\pi\\epsilon_0ac^2}\\ (\\text{shell}),\\qquad \\delta m_{\\rm QED}=\\frac{3\\alpha}{4\\pi}m\\ln\\frac{\\Lambda^2}{m^2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1093", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "06-particle-physics/neutrino-physics/neutrino-oscillations", "name": "Coherent forward scattering → refractive index (MSW)", "kind": "identity", "summary": "A medium's refractive index is fixed by the forward scattering amplitude of its scatterers, the same physics as the optical theorem. Wolfenstein applied this to neutrinos: charged-current forward scattering on electrons gives ν_e an extra potential √2 G_F N_e, which changes the effective mixing in the Sun and Earth.", "map": "n-1=\\frac{2\\pi N f(0)}{k^2},\\quad V_{CC}=\\sqrt2\\,G_FN_e,\\quad \\sigma_{\\rm tot}=\\frac{4\\pi}{k}{\\rm Im}f(0)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1094", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "06-particle-physics/quantum-field-theory/feynman-diagrams-and-scattering-amplitudes", "name": "Thomson → Klein–Nishina: Compton scattering at tree level", "kind": "identity", "summary": "The classical Thomson cross-section 8πr_e²/3 is the ω→0 limit of the tree-level QED Klein–Nishina result. The low-energy theorem guarantees this limit holds to all orders, and Compton scattering was the first QED amplitude checked against experiment.", "map": "\\frac{d\\sigma}{d\\Omega}=\\frac{r_e^2}{2}\\Big(\\frac{\\omega'}{\\omega}\\Big)^2\\Big(\\frac{\\omega'}{\\omega}+\\frac{\\omega}{\\omega'}-\\sin^2\\theta\\Big)\\to\\frac{r_e^2}{2}(1+\\cos^2\\theta)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1407", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/localization-and-disorder", "b": "06-particle-physics/standard-model/quantum-chromodynamics", "name": "Random matrices and localization in the Dirac spectrum", "kind": "method transfer", "summary": "Low-lying eigenvalues of the QCD Dirac operator follow chiral random-matrix theory, and the Banks–Casher relation ties the chiral condensate to the spectral density at zero. Above T_c the low modes localize, with an Anderson-type mobility edge, linking chiral restoration to localization.", "map": "\\langle\\bar qq\\rangle=-\\pi\\rho(0)/V;\\ \\text{microscopic }\\rho_s(\\zeta)\\ \\text{universal (chRMT)}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1408", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "b": "06-particle-physics/quantum-field-theory/canonical-and-path-integral-quantization", "name": "Finite-temperature QFT: Matsubara formalism", "kind": "identity", "summary": "A thermal QFT is the Euclidean path integral on a spatial manifold times a circle of circumference ħβ, with bosons periodic and fermions antiperiodic. Matsubara frequencies ω_n=2πn/β or (2n+1)π/β turn the grand partition function into diagrammatic perturbation theory.", "map": "Z=\\mathrm{Tr}\\,e^{-\\beta(H-\\mu N)}=\\int_{\\phi(\\beta)=\\pm\\phi(0)}\\mathcal D\\phi\\,e^{-S_E},\\ \\omega_n=\\frac{2n\\pi}{\\beta}\\ \\text{or}\\ \\frac{(2n+1)\\pi}{\\beta}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1409", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information", "b": "06-particle-physics/quantum-field-theory/conformal-field-theory", "name": "Entanglement entropy and the c-theorem", "kind": "identity", "summary": "In 1+1D CFT the entanglement entropy of an interval is (c/3) ln(ℓ/a), so the central charge is an entropy coefficient. Strong subadditivity of entanglement entropy gives an entropic proof that c decreases along RG flows.", "map": "S(\\ell)=\\frac c3\\ln\\frac\\ell a;\\ C(\\ell)=\\ell\\,S'(\\ell),\\ C'(\\ell)\\le0", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1410", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/exactly-solvable-models", "b": "06-particle-physics/quantum-field-theory", "name": "Integrable field theory: Ising in a field and E8", "kind": "identity", "summary": "The 2D Ising critical point perturbed by a magnetic field is an integrable massive QFT with eight particles whose masses follow the E8 Lie algebra (m₂/m₁=2cos π/5, the golden ratio). Neutron scattering on the Ising-chain magnet CoNb₂O₆ observed the ratio.", "map": "\\frac{m_2}{m_1}=2\\cos\\frac\\pi5=\\varphi\\approx1.618", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1411", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/exactly-solvable-models", "b": "06-particle-physics/quantum-field-theory/conformal-field-theory", "name": "Exactly solvable lattice models as CFTs", "kind": "identity", "summary": "At criticality, exactly solved 2D models (Ising, Potts, vertex models, XXZ chain) are lattice realizations of conformal field theories. Their exponents are conformal weights, and finite-size spectra of transfer matrices give the central charge and scaling dimensions.", "map": "E_0(L)=Lf_\\infty-\\frac{\\pi c v}{6L},\\ E_n-E_0=\\frac{2\\pi v}{L}(h+\\bar h)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1412", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/driven-systems-and-nonequilibrium-steady-states", "b": "06-particle-physics/quantum-field-theory", "name": "Directed percolation is Reggeon field theory", "kind": "historical", "summary": "The field theory of directed percolation is identical to Reggeon field theory, developed in the 1970s for high-energy hadron scattering. Its ε-expansion around d_c=4 transferred directly to absorbing-state transitions.", "map": "\\mathcal L_{RFT}=\\bar\\psi(\\partial_t-D\\nabla^2-r)\\psi+\\tfrac g2(\\bar\\psi\\psi^2-\\bar\\psi^2\\psi)\\leftrightarrow\\text{DP}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1413", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "06-particle-physics/beyond-the-standard-model/baryogenesis-and-matter-antimatter", "name": "Departure from equilibrium in baryogenesis", "kind": "mechanism", "summary": "Sakharov's third condition, departure from thermal equilibrium, is a statement of non-equilibrium statistical mechanics: in equilibrium CPT forces ⟨B⟩=0. Leptogenesis yields are computed from coupled Boltzmann equations for heavy-neutrino decays and washout.", "map": "\\frac{dN_{B-L}}{dz}=-\\epsilon_1D(N_N-N_N^{eq})-WN_{B-L},\\ z=M/T", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1414", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "06-particle-physics/beyond-the-standard-model/dark-matter-particle-candidates", "name": "WIMP freeze-out from the Boltzmann equation", "kind": "method transfer", "summary": "Relic dark-matter abundance comes from a Boltzmann equation in an expanding universe. Annihilation keeps n near equilibrium until the rate n⟨σv⟩ falls below H, after which the comoving density freezes out at Ω h²∝1/⟨σv⟩.", "map": "\\dot n+3Hn=-\\langle\\sigma v\\rangle(n^2-n_{\\text{eq}}^2);\\ \\Omega_\\chi h^2\\approx\\frac{3\\times10^{-27}\\text{cm}^3\\text{s}^{-1}}{\\langle\\sigma v\\rangle}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1415", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "06-particle-physics/neutrino-physics/neutrino-oscillations", "name": "Quantum kinetic equations for dense neutrino gases", "kind": "method transfer", "summary": "In supernovae and the early universe, mixing neutrinos are described by a matrix-valued Boltzmann equation (flavour density matrices with collisions). Collective 'fast flavour' instabilities are analysed with linear-response stability theory, as for plasma waves.", "map": "(\\partial_t+\\mathbf v\\cdot\\nabla)\\varrho_{\\mathbf p}=-i[H_{\\mathbf p},\\varrho_{\\mathbf p}]+C[\\varrho]", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1416", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation", "b": "06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2", "name": "Dispersion relations for hadronic vacuum polarization", "kind": "method transfer", "summary": "Causality and analyticity of the photon vacuum-polarization function give a Kramers–Kronig-type dispersion integral over σ(e⁺e⁻→hadrons). It is the data-driven route to the leading hadronic contribution to muon g−2, the same structure as the susceptibility relations of linear response.", "map": "a_\\mu^{HVP}=\\frac{1}{4\\pi^3}\\int_{s_{th}}^\\infty ds\\,K(s)\\,\\sigma_{e^+e^-\\to\\text{had}}(s)\\leftrightarrow\\chi'(\\omega)=\\frac2\\pi P\\!\\int\\frac{\\omega'\\chi''}{\\omega'^2-\\omega^2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1417", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "06-particle-physics/collider-and-experimental-particle-physics/monte-carlo-event-generators", "name": "Parton showers as Markov processes", "kind": "method transfer", "summary": "A parton shower is a Markov chain in an evolution variable. The Sudakov factor is the no-emission survival probability of a non-homogeneous Poisson process, and DGLAP evolution is a master equation for parton densities, so showers are sampled with veto algorithms from stochastic simulation.", "map": "\\Delta(t_1,t_2)=\\exp\\left[-\\int_{t_2}^{t_1}\\frac{dt}{t}\\int dz\\frac{\\alpha_s}{2\\pi}P(z)\\right]=P(\\text{no emission})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1418", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "06-particle-physics/quantum-field-theory/canonical-and-path-integral-quantization", "name": "Stochastic quantization and Hybrid Monte Carlo", "kind": "method transfer", "summary": "Parisi–Wu stochastic quantization obtains the Euclidean QFT measure e^{-S} as the equilibrium of Langevin dynamics in a fictitious time. Hybrid Monte Carlo, which combines molecular dynamics, momentum refreshment and a Metropolis test, is the workhorse algorithm of lattice QCD.", "map": "\\partial_s\\phi=-\\frac{\\delta S_E}{\\delta\\phi}+\\eta,\\ \\langle\\eta\\eta\\rangle=2\\delta\\Rightarrow P_{s\\to\\infty}[\\phi]\\propto e^{-S_E}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1419", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena", "b": "06-particle-physics/quantum-field-theory", "name": "Euclidean QFT as statistical field theory", "kind": "identity", "summary": "Euclidean QFT in D dimensions is classical statistical mechanics of fields in D dimensions, with e^{-S_E/ħ} as Boltzmann weight. Particle-physics tools (Feynman diagrams, renormalization, instantons) and stat-mech tools (Monte Carlo, high-T expansions, RG) are interchangeable.", "map": "Z=\\int\\mathcal D\\phi\\,e^{-S_E[\\phi]/\\hbar}\\leftrightarrow\\sum e^{-\\beta H},\\ \\hbar\\leftrightarrow k_BT", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1420", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena", "b": "06-particle-physics/quantum-field-theory/conformal-field-theory", "name": "Critical points are conformal field theories", "kind": "identity", "summary": "At a continuous transition, scale invariance plus locality enhances to conformal invariance. The fixed point is a CFT whose operator dimensions are the critical exponents and whose OPE data fix all correlations.", "map": "\\langle\\phi(x)\\phi(0)\\rangle\\sim|x|^{-2\\Delta_\\phi},\\ \\Delta_\\phi=\\frac{d-2+\\eta}{2},\\ \\nu=\\frac{1}{d-\\Delta_\\epsilon}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1421", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena", "b": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "name": "Statistical field theory ↔ renormalizable QFT", "kind": "identity", "summary": "Landau–Ginzburg–Wilson field theory of a critical point is a Euclidean φ⁴ QFT. The correlation length plays the role of inverse mass, and the continuum limit at T_c is a renormalized massless QFT.", "map": "F_L=\\int[\\tfrac12(\\nabla\\phi)^2+\\tfrac12r\\phi^2+\\tfrac u{4!}\\phi^4]\\leftrightarrow S_E,\\ \\xi=m^{-1}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1422", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena", "b": "06-particle-physics/standard-model/electroweak-theory", "name": "Electroweak crossover at T ~ 160 GeV", "kind": "identity", "summary": "Electroweak symmetry is restored at high temperature. Dimensional reduction to a 3D SU(2)-Higgs theory and lattice simulations show that for m_h=125 GeV the transition is a smooth crossover, beyond the endpoint (in the 3D Ising class) of the first-order line. Standard-Model electroweak baryogenesis is therefore ruled out.", "map": "\\text{first order for }m_h\\lesssim72\\ \\text{GeV};\\ T_c\\approx159\\ \\text{GeV crossover (SM)}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1423", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/critical-exponents-and-universality", "b": "06-particle-physics/quantum-field-theory/conformal-field-theory", "name": "Conformal bootstrap determinations of exponents", "kind": "identity", "summary": "Conformal bootstrap constraints (crossing symmetry plus unitarity) fix the 3D Ising, O(N) and other critical exponents to the highest precision available, ν≈0.62999 and η≈0.03630 for Ising, beyond Monte Carlo and the ε-expansion.", "map": "\\Delta_\\sigma=0.5181489(10),\\ \\Delta_\\epsilon=1.412625(10)\\ (3D\\ \\text{Ising})", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1424", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/critical-exponents-and-universality", "b": "06-particle-physics/standard-model/quantum-chromodynamics", "name": "Pisarski–Wilczek: universality of the chiral transition", "kind": "identity", "summary": "With symmetry and an ε-expansion, the QCD chiral transition with two massless flavours is in the 3D O(4) class, while with three massless flavours it must be first order (no infrared-stable fixed point). Physical quark masses turn it into a crossover at T_c≈156 MeV, with O(4) scaling still visible in lattice data.", "map": "SU(2)_L\\times SU(2)_R\\simeq O(4)\\Rightarrow\\text{3D }O(4)\\ \\text{class};\\ N_f=3:\\ \\text{cubic invariant}\\Rightarrow\\text{first order}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1425", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/ising-model-and-lattice-models", "b": "06-particle-physics/quantum-field-theory/conformal-field-theory", "name": "2D Ising as the c=1/2 minimal model", "kind": "identity", "summary": "The 2D Ising critical point is the M(4,3) minimal CFT with c=1/2. Its primaries σ (h=1/16) and ε (h=1/2) give η=1/4 and ν=1 exactly. In 3D the bootstrap places Ising at a kink on the boundary of allowed (Δ_σ, Δ_ε).", "map": "c=\\tfrac12,\\ h_\\sigma=\\tfrac1{16},\\ h_\\epsilon=\\tfrac12\\Rightarrow\\eta=4h_\\sigma=\\tfrac14,\\ \\nu=\\frac{1}{2-2h_\\epsilon}=1", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1426", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/ising-model-and-lattice-models", "b": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "name": "Svetitsky–Yaffe: deconfinement in Z_N spin-model classes", "kind": "identity", "summary": "With the Polyakov loop as order parameter for center symmetry, a continuous deconfinement transition of a (d+1)-dimensional SU(N) gauge theory falls in the universality class of a d-dimensional Z_N spin model. Pure SU(2) in 3+1D deconfines in the 3D Ising class.", "map": "\\langle P\\rangle=\\langle\\tfrac1N\\mathrm{Tr}\\,\\mathcal Te^{i\\oint A_0d\\tau}\\rangle\\sim(T-T_c)^{\\beta_{\\text{Ising}}}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1427", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/ising-model-and-lattice-models", "b": "06-particle-physics/quantum-field-theory/lattice-field-theory", "name": "Lattice gauge theory as statistical mechanics", "kind": "identity", "summary": "Wilson's lattice QCD is a statistical-mechanics model of group-valued link variables. Wegner's Z₂ lattice gauge theory is its Ising prototype with no local order parameter, strong-coupling expansions are high-temperature expansions, and Monte Carlo importance sampling carried over directly.", "map": "S_W=\\beta\\sum_P(1-\\tfrac1N\\mathrm{Re\\,Tr}U_P),\\ \\beta=\\frac{2N}{g^2}\\leftrightarrow\\frac{J}{k_BT}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1428", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory", "b": "06-particle-physics/standard-model/higgs-boson", "name": "Higgs potential as a Landau–Ginzburg free energy", "kind": "identity", "summary": "The Higgs potential has the Landau form with a sign-changing quadratic term. Its vacuum is spontaneously broken order, and coupling to gauge fields gives the Higgs–Anderson mechanism already known from Ginzburg–Landau superconductors.", "map": "V=-\\mu^2|\\phi|^2+\\lambda|\\phi|^4\\ \\leftrightarrow\\ F=a(T-T_c)|\\psi|^2+b|\\psi|^4;\\ m_W=\\tfrac12gv\\leftrightarrow\\lambda_L^{-1}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1429", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory", "b": "06-particle-physics/standard-model/quantum-chromodynamics", "name": "NJL: BCS mean field for chiral symmetry breaking", "kind": "historical", "summary": "Nambu and Jona-Lasinio modelled nucleon mass generation explicitly on the BCS gap equation. The constituent mass is a self-consistent mean field from a four-fermion attraction, with pions as Goldstone modes, and the NJL model remains a mean-field tool for QCD phase diagrams.", "map": "M=m+2G\\langle\\bar qq\\rangle\\ \\leftrightarrow\\ \\Delta=V\\sum_k\\langle c_{-k\\downarrow}c_{k\\uparrow}\\rangle", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1430", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/renormalization-group", "b": "06-particle-physics/beyond-the-standard-model/extra-dimensions-and-hierarchy-problem", "name": "Hierarchy problem as tuning to a critical point", "kind": "analogy", "summary": "The Higgs mass term is the one relevant operator of the Standard Model. Keeping m_h ≪ Λ requires fine-tuning the bare parameter close to its critical value, just as a magnet must be tuned to T_c for ξ≫a. Naturalness asks what symmetry or dynamics does the tuning.", "map": "\\frac{m_h^2}{\\Lambda^2}\\sim\\frac{r-r_c}{\\Lambda^2}\\leftrightarrow\\frac{a^2}{\\xi^2}\\sim|t|^{2\\nu}", "breaks": "A magnet is tuned by an experimenter or by self-organized dynamics. For the Higgs no tuning agent is known (anthropics, SUSY, compositeness and relaxion proposals are all speculative), and the UV cutoff Λ may not exist physically.", "confidence": "established", "strength": 2}
{"id": "C1431", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/renormalization-group", "b": "06-particle-physics/quantum-field-theory/effective-field-theory", "name": "Wilsonian EFT: irrelevant operators and decoupling", "kind": "identity", "summary": "Effective field theory is the RG statement that operators of dimension above D are irrelevant, suppressed by (E/Λ)^{Δ-D}. Decoupling of heavy physics in particle physics and universality at critical points are the same fact.", "map": "\\mathcal L_{\\text{eff}}=\\sum_i\\frac{c_i}{\\Lambda^{\\Delta_i-4}}\\mathcal O_i;\\ y_i=4-\\Delta_i<0\\Rightarrow\\text{irrelevant}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1432", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/renormalization-group", "b": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "name": "Wilson's RG unifies running couplings and critical exponents", "kind": "identity", "summary": "QFT beta functions and the critical-phenomena RG are the same flow in theory space. A Wilson–Fisher fixed point is a zero of β(u), and the anomalous dimensions there are critical exponents, computed by the same diagrams in the ε-expansion.", "map": "\\beta(u)=-\\epsilon u+\\frac{3u^2}{16\\pi^2}\\Rightarrow u^*=\\frac{16\\pi^2\\epsilon}{3},\\ \\nu=\\tfrac12+\\tfrac{\\epsilon}{12}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1433", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/topological-phase-transitions-bkt", "b": "06-particle-physics/quantum-field-theory", "name": "BKT, Coulomb gas and sine-Gordon duality", "kind": "duality", "summary": "The 2D XY vortex gas maps onto the 2D Coulomb gas and the sine-Gordon field theory, which Coleman showed is dual to the massive Thirring model. The Kosterlitz RG equations are the sine-Gordon beta functions, and β²=8π is the BKT point.", "map": "\\mathcal L=\\tfrac12(\\partial\\phi)^2-\\frac{\\alpha}{\\beta^2}\\cos\\beta\\phi;\\ \\frac{4\\pi}{\\beta^2}=1+\\frac{g}{\\pi}\\ (\\text{Thirring}),\\ \\beta^2=8\\pi\\leftrightarrow T_{BKT}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1700", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "b": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "name": "Clocks search for ultralight dark matter", "kind": "method transfer", "summary": "Ultralight scalar dark matter would make fundamental constants oscillate; comparing clocks with different sensitivity to alpha and m_e/m_p detects such oscillations at frequencies set by the DM mass.", "map": "\\frac{\\delta\\alpha}{\\alpha}\\propto\\frac{\\phi_0}{\\Lambda}\\cos(m_\\phi c^2t/\\hbar);\\ \\frac{\\delta(\\nu_1/\\nu_2)}{\\nu_1/\\nu_2}=(K_1-K_2)\\frac{\\delta\\alpha}{\\alpha}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1701", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "name": "Isotope-shift King plots probe new bosons", "kind": "method transfer", "summary": "A new light boson coupling electrons to neutrons would bend the King plot of isotope shifts; precision ion spectroscopy constrains such Yukawa forces at keV-MeV masses.", "map": "\\delta\\nu_i^{AA'}=K_i\\mu_{AA'}+F_i\\delta\\langle r^2\\rangle+\\alpha_{NP}X_i\\gamma_{AA'}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1702", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2", "name": "Electron g-2 and alpha test QED", "kind": "method transfer", "summary": "A single-electron Penning-trap measurement of g/2 and atom-recoil measurements of alpha (Cs, Rb) test QED at the 1e-13 level; their mutual tension is part of the lepton g-2 anomaly landscape.", "map": "a_e=\\frac{\\alpha}{2\\pi}-0.328\\left(\\frac\\alpha\\pi\\right)^2+\\dots;\\ \\alpha^2=\\frac{2R_\\infty}{c}\\frac{h}{m_e}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1703", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "name": "Lamb shift and the birth of renormalization", "kind": "historical", "summary": "The 1947 Lamb shift measurement and Bethe's mass-renormalized calculation launched renormalized QED; hydrogen spectroscopy remains a precision test of bound-state QED.", "map": "\\Delta E_{2S}\\approx\\frac{4\\alpha^5m_ec^2}{3\\pi n^3}\\ln\\frac{1}{\\alpha}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1704", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "06-particle-physics/standard-model/electroweak-theory", "name": "Atomic parity violation measures the weak charge", "kind": "method transfer", "summary": "Z exchange between electrons and the nucleus mixes S and P states; the Cs 6S-7S parity-violating amplitude gives the nuclear weak charge and sin^2 theta_W at low momentum transfer, complementary to colliders.", "map": "Q_W=Z(1-4\\sin^2\\theta_W)-N", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1705", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "b": "06-particle-physics/quantum-field-theory/lattice-field-theory", "name": "Analog quantum simulation of lattice gauge theories", "kind": "method transfer", "summary": "Cold atoms and Rydberg arrays implement Hamiltonian lattice gauge theories with Gauss's law enforced by energy penalties or constraints, accessing real-time dynamics and finite density where Euclidean Monte Carlo has a sign problem.", "map": "H=-J\\sum(\\psi_i^\\dagger U_{i,i+1}\\psi_{i+1}+\\text{h.c.})+\\frac{g^2}{2}\\sum E_i^2;\\ G_i|\\psi\\rangle=0", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1706", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "b": "06-particle-physics/standard-model/higgs-boson", "name": "Higgs amplitude mode in superfluids", "kind": "analogy", "summary": "Near the superfluid-Mott transition, optical-lattice bosons have a gapped amplitude ('Higgs') mode of the order parameter, observed by lattice modulation spectroscopy.", "map": "V(\\psi)=-\\mu|\\psi|^2+\\tfrac u2|\\psi|^4;\\ \\Delta_H\\to0\\ \\text{at the QCP}", "breaks": "No gauge field, so no Higgs mechanism; the amplitude mode can decay into Goldstone pairs and is only well defined near Lorentz-invariant criticality.", "confidence": "established", "strength": 2}
{"id": "C1707", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/ultracold-molecules", "b": "06-particle-physics/standard-model/cp-violation", "name": "Electron EDM in polar molecules", "kind": "method transfer", "summary": "Polar molecules (ThO, HfF+) amplify a lab field into internal effective fields of 10-100 GV/cm; spin-precession measurements bound the electron EDM below 1e-29 e cm, probing CP-violating physics at multi-TeV scales.", "map": "H=-d_e\\,\\mathcal E_{\\rm eff}\\,\\boldsymbol\\sigma\\cdot\\hat n;\\ d_e\\sim e\\,m_e\\,\\frac{\\alpha}{\\pi}\\frac{\\sin\\phi_{CP}}{\\Lambda^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1708", "a": "04-quantum-physics/foundations-of-quantum-mechanics/bell-nonlocality", "b": "06-particle-physics/neutrino-physics/neutrino-oscillations", "name": "Leggett-Garg violation in neutrino oscillations", "kind": "method transfer", "summary": "Temporal (Leggett-Garg) inequalities, the time-domain analogue of Bell tests, are violated by MINOS oscillation data, showing neutrino flavour evolution is incompatible with macrorealism over 735 km.", "map": "K_3=C_{12}+C_{23}-C_{13}\\le1", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1709", "a": "04-quantum-physics/foundations-of-quantum-mechanics/bell-nonlocality", "b": "06-particle-physics/standard-model/flavor-physics-and-ckm", "name": "Entangled neutral mesons and Bell tests", "kind": "shared object", "summary": "Pairs of neutral K or B mesons from phi or Upsilon(4S) decays are produced in flavour-entangled EPR states, used to time-tag CP and flavour measurements and to test Bell-type inequalities with decaying systems.", "map": "|\\psi\\rangle=\\tfrac{1}{\\sqrt2}(|B^0\\bar B^0\\rangle-|\\bar B^0B^0\\rangle)", "breaks": "Decay and lack of free measurement-setting choice prevent loophole-free Bell tests.", "confidence": "current research", "strength": 2}
{"id": "C1710", "a": "04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical", "b": "06-particle-physics/neutrino-physics/neutrino-oscillations", "name": "Wave-packet decoherence of neutrino oscillations", "kind": "mechanism", "summary": "Mass eigenstates in a neutrino wave packet separate over a coherence length, damping oscillations exactly as which-path information kills interference; open-system (Lindblad) models also bound exotic decoherence from new physics.", "map": "L_{\\rm coh}\\sim\\frac{4\\sqrt2E^2}{|\\Delta m^2|}\\sigma_x;\\ P\\to\\tfrac12\\sin^22\\theta", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1711", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/non-hermitian-physics", "b": "06-particle-physics/standard-model/cp-violation", "name": "Kaon mixing is a non-Hermitian two-level system", "kind": "identity", "summary": "The Weisskopf-Wigner effective Hamiltonian of neutral kaons (or B mesons) is the non-Hermitian matrix M - i Gamma/2; its non-orthogonal eigenstates K_S, K_L and their overlap encode CP violation.", "map": "H_{\\rm eff}=M-\\tfrac i2\\Gamma;\\ \\langle K_S|K_L\\rangle\\approx2\\mathrm{Re}\\,\\epsilon", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1712", "a": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "b": "06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc", "name": "Entanglement of top-quark pairs at the LHC", "kind": "method transfer", "summary": "Top-antitop spin correlations reconstructed from decay leptons are a two-qubit density matrix; ATLAS and CMS observed entanglement near threshold using quantum-information witnesses.", "map": "D=-3\\langle\\cos\\varphi\\rangle;\\ D<-1/3\\Rightarrow\\text{entangled}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1713", "a": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "b": "06-particle-physics/quantum-field-theory/conformal-field-theory", "name": "Entanglement entropy measures the central charge", "kind": "identity", "summary": "In a 1+1D CFT the entanglement entropy of an interval grows logarithmically with a coefficient fixed by the central charge, so entanglement diagnoses criticality and universality classes.", "map": "S_A=\\frac c3\\ln\\frac{\\ell}{a}+c'", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1714", "a": "04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity", "b": "06-particle-physics/collider-and-experimental-particle-physics/machine-learning-in-hep", "name": "Quantum machine learning for collider data", "kind": "method transfer", "summary": "Variational quantum classifiers and kernels have been tried on jet tagging and event classification; no advantage over classical deep learning has been demonstrated.", "map": "", "breaks": "", "confidence": "proposed", "strength": 1}
{"id": "C1715", "a": "04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity", "b": "06-particle-physics/collider-and-experimental-particle-physics/monte-carlo-event-generators", "name": "Quantum algorithms for parton showers", "kind": "method transfer", "summary": "Quantum circuits can simulate parton showers including quantum interference between emission histories that classical Markov showers drop.", "map": "", "breaks": "", "confidence": "proposed", "strength": 1}
{"id": "C1716", "a": "04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity", "b": "06-particle-physics/quantum-field-theory/lattice-field-theory", "name": "Digital quantum algorithms for QFT", "kind": "method transfer", "summary": "Hamiltonian-simulation algorithms compute scattering in scalar and gauge field theories in polynomial time, a route around the sign problem of lattice QCD at finite density and real time.", "map": "e^{-iHt}\\approx\\left(\\prod_je^{-iH_jt/n}\\right)^n", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1717", "a": "04-quantum-physics/quantum-information-and-computation/superconducting-qubits", "b": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "name": "Qubit photon counting for dark-photon searches", "kind": "method transfer", "summary": "A transmon dispersively coupled to a cavity counts photons by repeated quantum non-demolition parity measurements, evading the standard quantum limit of linear amplifiers in hidden-photon and axion searches.", "map": "\\chi\\sigma_za^\\dagger a\\ \\Rightarrow\\ \\text{QND number readout}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1718", "a": "04-quantum-physics/quantum-information-and-computation/trapped-ion-and-neutral-atom-qubits", "b": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "name": "Trapped-ion simulation of the Schwinger model", "kind": "method transfer", "summary": "A few trapped-ion qubits simulated real-time pair creation in 1+1D QED after eliminating the gauge field; circuit-QED and tensor-network studies extend this to meson scattering.", "map": "H=w\\sum(\\sigma_n^+\\sigma_{n+1}^-+\\text{h.c.})+\\frac m2\\sum(-1)^n\\sigma_n^z+J\\sum L_n^2", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1719", "a": "04-quantum-physics/quantum-mechanics-core", "b": "06-particle-physics/quantum-field-theory", "name": "Second quantization: QM of many particles is QFT", "kind": "identity", "summary": "Non-relativistic many-body quantum mechanics in Fock space is a free or interacting quantum field theory; relativistic QFT adds Lorentz invariance, antiparticles and particle number non-conservation.", "map": "\\hat\\psi(\\mathbf x)=\\sum_k a_k\\phi_k(\\mathbf x),\\ [a_k,a_{k'}^\\dagger]_\\mp=\\delta_{kk'}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1720", "a": "04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin", "b": "06-particle-physics/neutrino-physics/neutrino-oscillations", "name": "Neutrino flavour as a precessing pseudo-spin", "kind": "identity", "summary": "Two-flavour oscillation is spin-1/2 precession in an effective magnetic field; the oscillation formula is the Rabi formula, and collective oscillations in dense neutrino gases map onto interacting spin models.", "map": "P_{\\alpha\\beta}=\\sin^22\\theta\\sin^2\\frac{\\Delta m^2L}{4E}\\leftrightarrow P=\\frac{\\Omega^2}{\\Omega'^2}\\sin^2\\frac{\\Omega't}{2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1721", "a": "04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin", "b": "06-particle-physics/standard-model/hadron-spectroscopy-and-exotics", "name": "Isospin and flavour multiplets via SU(2) recoupling", "kind": "method transfer", "summary": "Clebsch-Gordan coefficients and the Wigner-Eckart theorem developed for angular momentum organize isospin and flavour multiplets, decay branching ratios and helicity amplitudes of hadrons.", "map": "\\frac{\\Gamma(\\Delta^+\\to p\\pi^0)}{\\Gamma(\\Delta^+\\to n\\pi^+)}=\\frac{|\\langle\\tfrac32\\tfrac12|1\\,0;\\tfrac12\\tfrac12\\rangle|^2}{|\\langle\\tfrac32\\tfrac12|1\\,1;\\tfrac12\\,{-\\tfrac12}\\rangle|^2}=2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1722", "a": "04-quantum-physics/quantum-mechanics-core/approximation-methods", "b": "06-particle-physics/neutrino-physics/neutrino-oscillations", "name": "MSW conversion as an adiabatic level crossing", "kind": "identity", "summary": "Resonant flavour conversion in the Sun is an avoided crossing of matter-dressed mass eigenstates; adiabatic following gives near-complete conversion and the non-adiabatic hopping probability is the Landau-Zener formula.", "map": "P_{\\rm hop}=\\exp\\left(-\\frac{\\pi}{2}\\frac{\\Delta m^2\\sin^22\\theta}{2E\\cos2\\theta\\,|d\\ln n_e/dr|}\\right)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1723", "a": "04-quantum-physics/quantum-mechanics-core/approximation-methods", "b": "06-particle-physics/quantum-field-theory/effective-field-theory", "name": "Schrieffer-Wolff elimination as integrating out", "kind": "identity", "summary": "Adiabatic elimination of high-energy states by second-order perturbation theory (Schrieffer-Wolff) gives effective Hamiltonians, the same logic as integrating out heavy fields; Fermi's four-fermion coupling is W exchange at second order.", "map": "H_{\\rm eff}=PVP+\\sum\\frac{PV|m\\rangle\\langle m|VP}{E-E_m}\\leftrightarrow\\frac{G_F}{\\sqrt2}=\\frac{g^2}{8m_W^2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1724", "a": "04-quantum-physics/quantum-mechanics-core/approximation-methods", "b": "06-particle-physics/quantum-field-theory/feynman-diagrams-and-scattering-amplitudes", "name": "Golden rule and decay widths", "kind": "identity", "summary": "Fermi's golden rule is the non-relativistic form of the relativistic decay-rate and cross-section formulas built from Feynman amplitudes and Lorentz-invariant phase space.", "map": "\\Gamma=\\frac{2\\pi}{\\hbar}|V_{fi}|^2\\rho(E_f)\\leftrightarrow\\Gamma=\\frac{1}{2m}\\int|\\mathcal M|^2d\\Phi_n", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1725", "a": "04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems", "b": "06-particle-physics/beyond-the-standard-model/supersymmetry", "name": "Supersymmetric quantum mechanics", "kind": "historical", "summary": "Witten introduced SUSY QM as a toy model of supersymmetry breaking (Witten index); it became a tool for exactly solvable potentials through shape invariance and partner Hamiltonians.", "map": "H_\\pm=-\\frac{\\hbar^2}{2m}\\frac{d^2}{dx^2}+W^2\\pm\\frac{\\hbar}{\\sqrt{2m}}W'", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1726", "a": "04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems", "b": "06-particle-physics/standard-model/hadron-spectroscopy-and-exotics", "name": "Quarkonium as hydrogen of QCD", "kind": "analogy", "summary": "Charmonium and bottomonium spectra follow from a Schrodinger equation with a Coulomb-plus-linear (Cornell) potential, organized like hydrogen and positronium levels with fine and hyperfine splittings.", "map": "V(r)=-\\frac{4}{3}\\frac{\\alpha_s}{r}+\\sigma r", "breaks": "Confinement (linear term) has no atomic analogue; relativistic corrections and coupled open-flavour channels matter above threshold.", "confidence": "established", "strength": 2}
{"id": "C1727", "a": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "b": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "name": "Theta vacua as Bloch states; WZ terms as Berry phases", "kind": "identity", "summary": "Large gauge transformations make the Yang-Mills vacuum periodic, and theta plays the role of Bloch quasi-momentum in a periodic potential; Wess-Zumino-Witten terms are Berry phases of the low-energy fields.", "map": "|\\theta\\rangle=\\sum_ne^{in\\theta}|n\\rangle\\leftrightarrow\\psi_k(x)=\\sum_ne^{ikna}\\phi(x-na)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1728", "a": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "b": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "name": "Wilson loops are non-abelian holonomies", "kind": "identity", "summary": "The Aharonov-Bohm phase is a U(1) holonomy; Yang-Mills Wilson loops are its non-abelian generalization, and degenerate adiabatic transport produces the same Wilczek-Zee non-abelian connection.", "map": "W(C)=\\mathrm{Tr}\\,\\mathcal P\\exp\\left(ig\\oint_CA\\right);\\ \\Delta\\phi_{AB}=q\\Phi/\\hbar", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1729", "a": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "b": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "name": "Instantons from double wells to QCD", "kind": "method transfer", "summary": "Euclidean instantons that compute tunnelling splitting in a double well become Yang-Mills instantons, which break U(1)_A through the anomaly and mix the theta vacua.", "map": "\\Delta E\\propto e^{-S_E/\\hbar}\\to e^{-8\\pi^2/g^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1730", "a": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "b": "06-particle-physics/quantum-field-theory/canonical-and-path-integral-quantization", "name": "Feynman path integral from particles to fields", "kind": "identity", "summary": "The QFT generating functional is the particle path integral with paths replaced by field configurations; stationary phase gives the classical field equations and Gaussian integrals give propagators and Wick's theorem.", "map": "K=\\int\\mathcal Dx\\,e^{iS[x]/\\hbar}\\to Z[J]=\\int\\mathcal D\\phi\\,e^{i(S[\\phi]+\\int J\\phi)/\\hbar}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1731", "a": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "b": "06-particle-physics/quantum-field-theory/feynman-diagrams-and-scattering-amplitudes", "name": "Born series as tree-level perturbation theory", "kind": "identity", "summary": "The Lippmann-Schwinger Born series is the non-relativistic limit of the Feynman-diagram expansion: first Born approximation equals tree-level one-boson exchange (Yukawa/Coulomb), and the optical theorem is S-matrix unitarity.", "map": "f_{\\rm Born}=-\\frac{m}{2\\pi\\hbar^2}\\tilde V(\\mathbf q)\\leftrightarrow\\mathcal M\\propto\\frac{g^2}{q^2+m^2};\\ \\sigma_{\\rm tot}=\\frac{4\\pi}{k}\\mathrm{Im}f(0)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1732", "a": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "b": "06-particle-physics/standard-model/hadron-spectroscopy-and-exotics", "name": "Near-threshold states and universality", "kind": "mechanism", "summary": "Hadrons near a two-body threshold (deuteron, X(3872)) are governed by a large scattering length, the same universal physics as Feshbach-tuned cold atoms, including Efimov-type three-body effects.", "map": "E_B\\approx\\frac{\\hbar^2}{2\\mu a^2},\\ \\langle r^2\\rangle^{1/2}\\approx a/\\sqrt2\\ (a\\gg r_0)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1733", "a": "04-quantum-physics/quantum-optics/quantized-light-and-photon-statistics", "b": "06-particle-physics/quantum-field-theory/canonical-and-path-integral-quantization", "name": "Quantized EM field as free QFT", "kind": "identity", "summary": "Quantum optics' mode expansion of the field, Fock and coherent states are the canonical quantization of free Maxwell theory; Glauber coherent states are the quantum states closest to classical fields.", "map": "\\hat{\\mathbf A}=\\sum_{k\\lambda}\\sqrt{\\frac{\\hbar}{2\\epsilon_0\\omega_kV}}(a_{k\\lambda}\\boldsymbol\\epsilon e^{i\\mathbf k\\cdot\\mathbf x}+\\text{h.c.})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1734", "a": "04-quantum-physics/quantum-optics/single-photon-sources-and-detectors", "b": "06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers", "name": "Single-photon detectors in particle detectors", "kind": "shared object", "summary": "Calorimeters, Cherenkov and scintillator systems read out light with single-photon-sensitive devices (PMTs, SiPMs, SPAD arrays); quantum-optics detector metrics such as efficiency, dark counts and timing jitter set detector performance.", "map": "\\eta_{\\rm sys}=\\eta_{\\rm coupling}\\eta_{\\rm det};\\ \\sigma_t\\ \\text{(jitter)}", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1735", "a": "04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology", "b": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "name": "Squeezed-state receivers for axion haloscopes", "kind": "method transfer", "summary": "Haloscopes convert axions to microwave photons in a resonant cavity; HAYSTAC injected squeezed vacuum to beat the quantum limit on scan rate, a direct import of quantum metrology.", "map": "P_{a\\to\\gamma}\\propto g_{a\\gamma\\gamma}^2\\frac{\\rho_a}{m_a}B^2VC\\,Q;\\ \\text{scan rate}\\propto1/(\\text{noise})^2", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1966", "a": "05-relativity-and-gravitation/black-holes/black-hole-thermodynamics-and-hawking-radiation", "b": "06-particle-physics/beyond-the-standard-model/dark-matter-particle-candidates", "name": "Primordial black holes as dark matter", "kind": "shared object", "summary": "PBHs are a non-particle dark-matter candidate; Hawking evaporation removes those below about 5e14 g and gamma-ray and CMB limits constrain slightly heavier ones, while lensing and GW limits leave the asteroid-mass window open.", "map": "t_{\\rm evap}\\approx\\frac{5120\\pi G^2M^3}{\\hbar c^4}=t_0\\Rightarrow M\\approx5\\times10^{14}\\ \\text{g}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1967", "a": "05-relativity-and-gravitation/black-holes/schwarzschild-and-kerr-black-holes", "b": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "name": "Black-hole superradiance probes ultralight bosons", "kind": "mechanism", "summary": "A boson whose Compton wavelength matches a Kerr black hole forms hydrogen-like bound states that grow by superradiance while omega < m Omega_H, spinning the hole down; measured BH spins and continuous GW searches exclude axion masses near 1e-13 to 1e-11 eV.", "map": "\\alpha=\\frac{GM\\mu}{\\hbar c}\\sim0.1\\text{--}1,\\quad \\omega<m\\Omega_H,\\quad E_n\\approx\\mu c^2\\left(1-\\frac{\\alpha^2}{2n^2}\\right)\\ (\\text{gravitational atom})", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1968", "a": "05-relativity-and-gravitation/general-relativity/einstein-field-equations", "b": "06-particle-physics/quantum-field-theory", "name": "The cosmological constant problem", "kind": "shared object", "summary": "Lorentz invariance forces vacuum energy to enter the Einstein equations as rho_vac g_munu, so QFT zero-point energy, the Higgs potential and the QCD condensate all contribute to Lambda; naive estimates exceed the observed (2.2 meV)^4 by 50-120 orders of magnitude.", "map": "\\langle T_{\\mu\\nu}\\rangle_{\\rm vac}=-\\rho_{\\rm vac}g_{\\mu\\nu}\\Rightarrow\\Lambda_{\\rm eff}=\\Lambda+8\\pi G\\rho_{\\rm vac}/c^4,\\ \\rho_{\\rm obs}\\approx(2.2\\,\\text{meV})^4", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1969", "a": "05-relativity-and-gravitation/general-relativity/einstein-field-equations", "b": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "name": "Gravity as a gauge theory of the Lorentz group", "kind": "analogy", "summary": "Gauging local Lorentz (Poincare) invariance gives the spin connection as gauge potential and the Riemann tensor as its field strength, so GR in tetrad form shares the fibre-bundle structure of Yang-Mills.", "map": "A_\\mu^a\\leftrightarrow\\omega_\\mu{}^{ab},\\quad F^a_{\\mu\\nu}\\leftrightarrow R_{\\mu\\nu}{}^{ab},\\quad D_\\mu=\\partial_\\mu+\\tfrac12\\omega_\\mu{}^{ab}\\Sigma_{ab}", "breaks": "Not stated by the analyst.", "confidence": "established", "strength": 3}
{"id": "C1970", "a": "05-relativity-and-gravitation/general-relativity/modified-gravity", "b": "06-particle-physics/standard-model/higgs-boson", "name": "Higgs inflation is a scalar-tensor theory", "kind": "identity", "summary": "A large non-minimal coupling xi h^2 R makes the SM Higgs the inflaton; transforming to the Einstein frame flattens the potential into the same plateau as Starobinsky R+R^2 gravity, giving n_s near 0.965 and r near 0.003.", "map": "S=\\int\\sqrt{-g}\\left[\\frac{M_P^2+\\xi h^2}{2}R-\\frac{\\lambda}{4}h^4\\right]\\to V_E\\simeq\\frac{\\lambda M_P^4}{4\\xi^2}\\left(1-e^{-\\sqrt{2/3}\\,\\phi/M_P}\\right)^2", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1971", "a": "05-relativity-and-gravitation/general-relativity/tests-of-general-relativity", "b": "06-particle-physics/beyond-the-standard-model/extra-dimensions-and-hierarchy-problem", "name": "Sub-millimetre tests of the inverse-square law", "kind": "shared object", "summary": "ADD extra dimensions turn Newtonian gravity into a steeper power law below the compactification radius, parametrized as a Yukawa correction; torsion-balance tests of Newton's law below 0.1 mm bound n=2 ADD radii to tens of micrometres.", "map": "V(r)=-\\frac{Gm_1m_2}{r}\\left(1+\\alpha e^{-r/\\lambda}\\right),\\qquad V\\propto r^{-(1+n)}\\ (r\\ll R)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1972", "a": "05-relativity-and-gravitation/gravitational-waves/gravitational-wave-theory-and-waveforms", "b": "06-particle-physics/quantum-field-theory/effective-field-theory", "name": "Worldline EFT (NRGR) for compact binaries", "kind": "method transfer", "summary": "Non-relativistic GR treats compact bodies as point particles on worldlines with finite-size operators (tidal Love numbers) and integrates out potential and radiation gravitons with Feynman diagrams and dimensional regularization, the EFT toolkit of QCD applied to post-Newtonian inspirals.", "map": "S=-m\\int d\\tau+c_E\\int d\\tau\\,E_{\\mu\\nu}E^{\\mu\\nu}+\\dots,\\quad v^2\\sim Gm/r\\ \\text{as expansion parameter}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1973", "a": "05-relativity-and-gravitation/gravitational-waves/gravitational-wave-theory-and-waveforms", "b": "06-particle-physics/quantum-field-theory/feynman-diagrams-and-scattering-amplitudes", "name": "Amplitudes compute post-Minkowskian binary dynamics", "kind": "method transfer", "summary": "On-shell scattering amplitudes, unitarity cuts and the eikonal give the conservative two-body Hamiltonian order by order in G (post-Minkowskian), now at 3PM-5PM, feeding EOB waveform models for LIGO and LISA.", "map": "", "breaks": "Amplitudes give scattering (unbound) orbits most naturally; bound-orbit observables need analytic continuation (B2B maps) and radiation-reaction subtleties remain.", "confidence": "current research", "strength": 3}
{"id": "C1974", "a": "05-relativity-and-gravitation/gravitational-waves/pulsar-timing-arrays", "b": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "name": "Nanohertz GWs from axion domain walls", "kind": "shared object", "summary": "Collapsing domain walls of QCD-coupled axions, cosmic strings and QCD-scale phase transitions all produce stochastic GW backgrounds peaking near nanohertz; PTA spectra are fitted against these alongside supermassive-binary models.", "map": "", "breaks": "The supermassive-black-hole-binary interpretation remains adequate; cosmological fits are not preferred decisively.", "confidence": "current research", "strength": 2}
{"id": "C1975", "a": "05-relativity-and-gravitation/gravitational-waves/pulsar-timing-arrays", "b": "06-particle-physics/beyond-the-standard-model/grand-unification-and-proton-decay", "name": "Cosmic strings from GUT symmetry breaking", "kind": "shared object", "summary": "U(1) factors broken in GUT chains leave cosmic strings (possibly metastable via monopole nucleation) whose loops radiate a broad GW background; PTA amplitudes bound the string tension G mu, constraining breaking scales.", "map": "G\\mu\\sim\\left(\\frac{v}{M_{\\rm Pl}}\\right)^2,\\qquad \\Omega_{\\rm gw}h^2\\propto\\sqrt{G\\mu}\\ (\\text{flat radiation-era plateau})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1976", "a": "05-relativity-and-gravitation/gravitational-waves/space-based-and-future-detectors", "b": "06-particle-physics/beyond-the-standard-model/baryogenesis-and-matter-antimatter", "name": "LISA tests first-order electroweak transitions", "kind": "shared object", "summary": "Electroweak baryogenesis needs a strongly first-order transition; bubble collisions, sound waves and turbulence in that transition produce a GW background peaking near millihertz, squarely in the LISA band.", "map": "f_{\\rm peak}\\approx1.65\\times10^{-5}\\,\\text{Hz}\\,\\frac{\\beta}{H_*}\\frac{T_*}{100\\,\\text{GeV}}\\left(\\frac{g_*}{100}\\right)^{1/6}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1977", "a": "05-relativity-and-gravitation/quantum-gravity", "b": "06-particle-physics/quantum-field-theory", "name": "Graviton as a spin-2 quantum field", "kind": "method transfer", "summary": "Perturbative quantum gravity is QFT applied to the metric: expand g=eta+kappa h, quantize the massless spin-2 field with gauge fixing and ghosts as in Yang-Mills; the coupling kappa^2=32 pi G has mass dimension -2, so the theory is non-renormalizable and needs a UV completion.", "map": "g_{\\mu\\nu}=\\eta_{\\mu\\nu}+\\kappa h_{\\mu\\nu},\\ \\kappa^2=32\\pi G\\ ([\\kappa]=-1)\\ \\leftrightarrow\\ \\text{gauge field }A_\\mu,\\ [e]=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1978", "a": "05-relativity-and-gravitation/quantum-gravity", "b": "06-particle-physics/quantum-field-theory/effective-field-theory", "name": "GR as an effective field theory", "kind": "method transfer", "summary": "Power counting in E/M_Pl makes GR a predictive EFT: the Einstein-Hilbert term is leading, R^2 terms are suppressed, and the long-distance quantum correction to the Newtonian potential is computable and cutoff-independent, exactly like chiral perturbation theory.", "map": "\\mathcal L=\\tfrac{2}{\\kappa^2}R+c_1R^2+c_2R_{\\mu\\nu}R^{\\mu\\nu}+\\dots,\\quad V=-\\tfrac{Gm_1m_2}{r}\\big[1+3\\tfrac{G(m_1+m_2)}{rc^2}+\\tfrac{41}{10\\pi}\\tfrac{G\\hbar}{r^2c^3}\\big]", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1979", "a": "05-relativity-and-gravitation/quantum-gravity", "b": "06-particle-physics/quantum-field-theory/feynman-diagrams-and-scattering-amplitudes", "name": "Double copy: gravity = (gauge theory)^2", "kind": "identity", "summary": "Tree and loop gravity amplitudes are obtained from Yang-Mills amplitudes by replacing colour factors with kinematic numerators that obey the same Jacobi identities (BCJ), generalizing the KLT relations of string theory; the classical double copy maps Coulomb to Schwarzschild.", "map": "\\mathcal A^{\\rm YM}=\\sum_i\\frac{c_in_i}{D_i}\\ \\to\\ \\mathcal M^{\\rm grav}=\\sum_i\\frac{n_i\\tilde n_i}{D_i},\\quad c_i\\to n_i,\\ g\\to\\kappa/2", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1980", "a": "05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft", "b": "06-particle-physics/quantum-field-theory/conformal-field-theory", "name": "AdS/CFT: bulk gravity equals boundary CFT", "kind": "duality", "summary": "Type IIB string theory on AdS5xS5 is conjectured to be exactly N=4 SU(N) super-Yang-Mills; the GKP-Witten dictionary maps bulk fields of mass m to CFT operators of dimension Delta, and the bulk on-shell action to the CFT generating functional.", "map": "Z_{\\rm CFT}[J]=Z_{\\rm grav}[\\phi|_\\partial\\to J],\\quad \\Delta(\\Delta-d)=m^2L^2,\\quad L^4/\\alpha'^2=\\lambda=g_{YM}^2N", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1981", "a": "05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft", "b": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "name": "Wilson loops as minimal string worldsheets", "kind": "duality", "summary": "In AdS/CFT the expectation value of a Yang-Mills Wilson loop is the exponential of minus the regularized area of a string worldsheet ending on the loop, giving the strong-coupling quark-antiquark potential V proportional to -sqrt(lambda)/L.", "map": "\\langle W(C)\\rangle=e^{-S_{\\rm NG}[\\Sigma_C]},\\qquad V(L)=-\\frac{4\\pi^2\\sqrt{2\\lambda}}{\\Gamma(1/4)^4L}", "breaks": "", "confidence": "established", "strength": 2}