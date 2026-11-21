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

# Packet 06-3 (100 records)

{"id": "C1982", "a": "05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft", "b": "06-particle-physics/standard-model/quantum-chromodynamics", "name": "Holographic QCD and confinement", "kind": "duality", "summary": "Confinement maps to a bulk geometry that caps off: in Witten's model the confinement-deconfinement transition is the Hawking-Page transition, Wilson loops are minimal string worldsheets with area law, and AdS/QCD models fit Regge trajectories.", "map": "", "breaks": "QCD is not conformal in the UV, has N=3 and no supersymmetry; holographic QCD lacks asymptotic freedom and has no known exact string dual.", "confidence": "current research", "strength": 2}
{"id": "C1983", "a": "05-relativity-and-gravitation/quantum-gravity/loop-quantum-gravity", "b": "06-particle-physics/quantum-field-theory/lattice-field-theory", "name": "Spin networks are gauge-invariant Wilson-loop states", "kind": "method transfer", "summary": "Ashtekar variables make GR an SU(2) connection theory; LQG states are holonomies (Wilson lines) on graphs labelled by spins, the same gauge-invariant basis used in Hamiltonian (Kogut-Susskind) lattice gauge theory, but on graphs that are not embedded in a fixed metric.", "map": "h_e[A]=\\mathcal P\\exp\\int_eA,\\ \\ \\Psi_{\\Gamma,j}=\\prod_e D^{j_e}(h_e)\\cdot\\iota_v\\ \\leftrightarrow\\ \\text{Kogut-Susskind link states}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1984", "a": "05-relativity-and-gravitation/quantum-gravity/other-approaches-to-quantum-gravity", "b": "06-particle-physics/quantum-field-theory/lattice-field-theory", "name": "CDT: lattice Monte Carlo for spacetime", "kind": "method transfer", "summary": "Causal dynamical triangulations regularize the gravitational path integral on simplicial lattices, sample it by Monte Carlo after Wick rotation, and seek a continuum limit at a second-order transition, the lattice-QCD strategy applied to geometry; a 4D de Sitter-like phase emerges.", "map": "Z=\\sum_T\\frac{1}{C_T}e^{-S_{\\rm Regge}[T]}\\ \\leftrightarrow\\ Z=\\int\\mathcal DU\\,e^{-S_W[U]};\\ \\text{continuum limit at a 2nd-order point}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1985", "a": "05-relativity-and-gravitation/quantum-gravity/other-approaches-to-quantum-gravity", "b": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "name": "Asymptotic safety: a UV fixed point for gravity", "kind": "method transfer", "summary": "Wilsonian and functional RG methods from QFT show evidence that Newton's dimensionless coupling g=Gk^2 flows to a non-Gaussian UV fixed point, making gravity non-perturbatively renormalizable, the gravitational analogue of asymptotic freedom with a non-zero fixed point.", "map": "k\\frac{dg}{dk}=(2+\\eta_N)g\\to g^*\\neq0\\quad\\leftrightarrow\\quad \\mu\\frac{d\\alpha_s}{d\\mu}=-\\frac{\\beta_0}{2\\pi}\\alpha_s^2\\to0", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1986", "a": "05-relativity-and-gravitation/quantum-gravity/other-approaches-to-quantum-gravity", "b": "06-particle-physics/standard-model/higgs-boson", "name": "Asymptotic safety predicted the Higgs mass", "kind": "shared object", "summary": "Requiring the SM plus gravity to be asymptotically safe forces the Higgs quartic near zero at the Planck scale, predicting m_h of about 126 GeV with a few-GeV uncertainty two years before the 125 GeV discovery.", "map": "", "breaks": "The prediction depends on assumed signs of gravitational anomalous dimensions; it is the same boundary condition as near-criticality of the SM vacuum and is not unique to asymptotic safety.", "confidence": "current research", "strength": 1}
{"id": "C1987", "a": "05-relativity-and-gravitation/quantum-gravity/qft-in-curved-spacetime", "b": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "name": "Trace and gravitational anomalies fix Hawking flux", "kind": "mechanism", "summary": "Regularization breaks classical conformal and diffeomorphism symmetry just as it breaks axial symmetry (ABJ): the trace anomaly sources <T_mu^mu> in curved space, and demanding cancellation of the near-horizon gravitational anomaly reproduces the Hawking flux.", "map": "\\langle T^\\mu{}_\\mu\\rangle=c\\,W^2-a\\,E_4+\\dots\\ \\leftrightarrow\\ \\partial_\\mu j_5^\\mu=\\frac{e^2}{16\\pi^2}\\epsilon^{\\mu\\nu\\rho\\sigma}F_{\\mu\\nu}F_{\\rho\\sigma}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1988", "a": "05-relativity-and-gravitation/quantum-gravity/qft-in-curved-spacetime", "b": "06-particle-physics/quantum-field-theory/canonical-and-path-integral-quantization", "name": "Bogoliubov transformations and vacuum ambiguity", "kind": "method transfer", "summary": "Canonical field quantization carries over to curved spacetime, but without a global timelike Killing vector the mode split into positive and negative frequency is not unique; in- and out-vacua related by Bogoliubov coefficients give particle creation (cosmological, Hawking, Unruh).", "map": "a^{\\rm out}_k=\\alpha_ka^{\\rm in}_k+\\beta_k^*a^{\\rm in\\dagger}_{-k},\\quad |\\alpha_k|^2-|\\beta_k|^2=1,\\quad \\langle N_k\\rangle=|\\beta_k|^2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1989", "a": "05-relativity-and-gravitation/quantum-gravity/qft-in-curved-spacetime", "b": "06-particle-physics/standard-model/higgs-boson", "name": "Higgs vacuum metastability in curved spacetime", "kind": "shared object", "summary": "With m_h=125 GeV and m_t=173 GeV the Higgs quartic runs negative near 1e10-1e11 GeV, so the electroweak vacuum is metastable; gravitational corrections to the bounce (Coleman-De Luccia) and Higgs fluctuations during inflation decide whether our vacuum survives.", "map": "\\Gamma\\sim e^{-B},\\ B=\\frac{8\\pi^2}{3|\\lambda(\\mu)|}\\ (\\text{flat});\\quad \\text{inflation safe if }H\\lesssim\\Lambda_{\\rm inst}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1990", "a": "05-relativity-and-gravitation/quantum-gravity/string-theory", "b": "06-particle-physics/beyond-the-standard-model", "name": "String compactifications as BSM model building", "kind": "method transfer", "summary": "Calabi-Yau, orbifold and brane-world compactifications generate gauge groups, chiral matter, axions, moduli and hidden sectors; BSM phenomenology inherits candidates (axiverse, moduli, GUT-like groups) and constraints (swampland conjectures) from string vacua.", "map": "", "breaks": "The landscape of vacua is so large that few sharp low-energy predictions follow; no compactification uniquely reproduces the SM.", "confidence": "current research", "strength": 2}
{"id": "C1991", "a": "05-relativity-and-gravitation/quantum-gravity/string-theory", "b": "06-particle-physics/beyond-the-standard-model/extra-dimensions-and-hierarchy-problem", "name": "Compactified dimensions and the hierarchy problem", "kind": "shared object", "summary": "String theory needs six extra dimensions; large (ADD) or warped (Randall-Sundrum) extra dimensions lower the fundamental gravity scale to TeV, and the RS warp factor is a slice of AdS5, so hierarchy models and holography share one geometry.", "map": "M_{\\rm Pl}^2\\simeq M_*^{n+2}R^n\\ (\\text{ADD}),\\qquad m_{\\rm TeV}=e^{-kr_c\\pi}M_{\\rm Pl}\\ (\\text{RS, AdS}_5\\ \\text{slice})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1992", "a": "05-relativity-and-gravitation/quantum-gravity/string-theory", "b": "06-particle-physics/beyond-the-standard-model/supersymmetry", "name": "Superstrings require supersymmetry", "kind": "shared object", "summary": "Removing the bosonic-string tachyon and including fermions requires worldsheet supersymmetry, which with GSO projection yields spacetime supersymmetry; superstring compactifications are the main UV source of SUSY and supergravity model building.", "map": "", "breaks": "Low-scale (TeV) SUSY is not predicted by string theory; the SUSY-breaking scale is unconstrained and LHC has not seen superpartners.", "confidence": "established", "strength": 2}
{"id": "C1993", "a": "05-relativity-and-gravitation/quantum-gravity/string-theory", "b": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "name": "Green-Schwarz anomaly cancellation", "kind": "mechanism", "summary": "The same consistency principle that fixes SM hypercharges (gauge anomaly cancellation) fixes superstring gauge groups: gauge and gravitational anomalies of 10D supergravity cancel only for SO(32) or E8xE8 via the Green-Schwarz counterterm.", "map": "I_{12}\\propto(\\mathrm{tr}R^2-\\mathrm{tr}F^2)X_8\\ \\text{iff}\\ \\dim G=496;\\qquad \\textstyle\\sum_{\\rm SM}Y^3=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1994", "a": "05-relativity-and-gravitation/quantum-gravity/string-theory", "b": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "name": "D-brane open strings give Yang-Mills", "kind": "identity", "summary": "The massless modes of open strings ending on N coincident D-branes are a U(N) gauge field plus adjoint scalars; their low-energy action is (super) Yang-Mills, so gauge theories arise as brane worldvolume theories, the starting point of AdS/CFT and brane-world model building.", "map": "S_{\\rm Dp}\\to-\\frac{1}{4g_{YM}^2}\\int d^{p+1}x\\,\\mathrm{Tr}F^2,\\quad g_{YM}^2\\propto g_s\\ell_s^{p-3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1995", "a": "05-relativity-and-gravitation/quantum-gravity/string-theory", "b": "06-particle-physics/standard-model/hadron-spectroscopy-and-exotics", "name": "String theory born from hadron Regge trajectories", "kind": "historical", "summary": "The Veneziano amplitude was invented to fit linearly rising Regge trajectories of mesons; reinterpreted as vibrating strings, it predicted a massless spin-2 state that became the graviton once QCD took over the strong interaction.", "map": "J=\\alpha(0)+\\alpha'm^2\\ (\\text{Regge}),\\qquad \\alpha'\\approx0.9\\ \\text{GeV}^{-2}\\ \\text{(hadrons)}\\to\\ell_s^2\\ \\text{(strings)}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1996", "a": "05-relativity-and-gravitation/quantum-gravity/string-theory", "b": "06-particle-physics/standard-model/quantum-chromodynamics", "name": "Large-N planar diagrams equal string genus expansion", "kind": "identity", "summary": "In 't Hooft's large-N limit Feynman diagrams of SU(N) gauge theory organize by the genus of the surface they tile, weighted N^(2-2g), the same topological expansion as closed-string perturbation theory with g_s ~ 1/N; this is the structural root of gauge/string duality.", "map": "\\mathcal F=\\sum_{g}N^{2-2g}f_g(\\lambda),\\ \\lambda=g_{YM}^2N\\ \\leftrightarrow\\ \\sum_g g_s^{2g-2}F_g,\\ g_s\\sim1/N", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1997", "a": "05-relativity-and-gravitation/special-relativity", "b": "06-particle-physics/quantum-field-theory", "name": "Particles as unitary irreps of the Poincare group", "kind": "identity", "summary": "Wigner's classification defines an elementary particle as an irreducible unitary representation of the Poincare group, labelled by mass and spin (or helicity for m=0); spinor-helicity and little-group scaling in modern amplitudes are the same construction.", "map": "P^\\mu P_\\mu=-m^2c^2,\\ W^\\mu W_\\mu=m^2c^2\\hbar^2s(s+1);\\quad m=0:\\ \\text{little group }ISO(2)\\Rightarrow h=\\pm s", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1998", "a": "05-relativity-and-gravitation/special-relativity/relativistic-kinematics-and-dynamics", "b": "06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc", "name": "Invariant mass and collider kinematics", "kind": "method transfer", "summary": "Collider physics runs on four-momentum invariants: resonance discovery by invariant-mass peaks, sqrt(s) of colliding beams versus fixed targets, rapidity and transverse momentum as boost-friendly variables, and partonic s-hat = x1 x2 s.", "map": "m^2c^4=(\\textstyle\\sum E)^2-|\\sum\\mathbf pc|^2,\\quad \\hat s=x_1x_2s,\\quad y=\\tfrac12\\ln\\frac{E+p_z}{E-p_z}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1999", "a": "05-relativity-and-gravitation/special-relativity/tests-of-lorentz-invariance", "b": "06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2", "name": "Muon storage rings test time dilation", "kind": "shared object", "summary": "The muon g-2 storage ring runs at the magic gamma=29.3, where the Thomas-BMT spin precession decouples from electric focusing; the dilated muon lifetime there confirmed SR time dilation to about 1e-3.", "map": "\\tau_{\\rm lab}=\\gamma\\tau_0,\\ \\gamma_{\\rm magic}=\\sqrt{1+1/a_\\mu}\\approx29.3;\\quad \\boldsymbol\\omega_a=-\\tfrac{e}{m}\\left[a_\\mu\\mathbf B-\\left(a_\\mu-\\tfrac{1}{\\gamma^2-1}\\right)\\tfrac{\\boldsymbol\\beta\\times\\mathbf E}{c}\\right]", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2000", "a": "05-relativity-and-gravitation/special-relativity/tests-of-lorentz-invariance", "b": "06-particle-physics/neutrino-physics/neutrino-experiments-and-sources", "name": "Neutrino speed bounds and the OPERA error", "kind": "shared object", "summary": "Neutrino time of flight from SN1987A and long-baseline beams bounds |v-c|/c; the 2011 OPERA superluminal claim was traced to a faulty fibre connection, and superluminal neutrinos would lose energy by e+e- pair emission.", "map": "\\delta=\\frac{v_\\nu^2}{c^2}-1:\\ \\Gamma(\\nu\\to\\nu e^+e^-)\\propto G_F^2E^5\\delta^3;\\quad |\\delta v/c|_{\\rm SN1987A}\\lesssim2\\times10^{-9}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2001", "a": "05-relativity-and-gravitation/special-relativity/tests-of-lorentz-invariance", "b": "06-particle-physics/standard-model", "name": "Standard-Model Extension as an EFT of Lorentz violation", "kind": "method transfer", "summary": "The SME adds every Lorentz-violating operator built from SM fields contracted with fixed background tensors (a_mu, b_mu, c_munu, ...), turning clock, cavity, meson and astrophysical tests into bounds on a common coefficient table.", "map": "\\mathcal L_{\\rm SME}=\\mathcal L_{\\rm SM}-a_\\mu\\bar\\psi\\gamma^\\mu\\psi-b_\\mu\\bar\\psi\\gamma_5\\gamma^\\mu\\psi+\\tfrac i2c_{\\mu\\nu}\\bar\\psi\\gamma^\\mu\\overleftrightarrow{D}^\\nu\\psi+\\dots", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2002", "a": "05-relativity-and-gravitation/special-relativity/tests-of-lorentz-invariance", "b": "06-particle-physics/standard-model/cp-violation", "name": "CPT violation requires Lorentz violation", "kind": "shared object", "summary": "In an interacting unitary QFT, CPT violation implies Lorentz violation, so neutral-kaon and B-meson CPT interferometry bound the CPT-odd SME coefficients a_mu with sidereal-time modulation.", "map": "\\delta_K\\simeq i\\sin\\phi_{SW}e^{i\\phi_{SW}}\\gamma_K\\,\\beta^\\mu\\Delta a_\\mu/\\Delta m", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2160", "a": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "b": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "name": "Peccei-Quinn axion couples through the QCD anomaly", "kind": "mechanism", "summary": "The axion is the pseudo-Goldstone boson of an anomalous U(1)_PQ. The anomaly couples it to G G-tilde exactly like the theta term, so its instanton-generated potential relaxes the effective theta-bar to zero. Its photon coupling is likewise fixed by the electromagnetic anomaly coefficient E/N.", "map": "\\mathcal L\\supset\\left(\\bar\\theta+\\frac{a}{f_a}\\right)\\frac{g_s^2}{32\\pi^2}G^a_{\\mu\\nu}\\tilde G^{a\\mu\\nu}+\\frac{g_{a\\gamma}}{4}aF\\tilde F", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2161", "a": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "b": "06-particle-physics/standard-model/quantum-chromodynamics", "name": "Strong CP problem and axion mass from QCD topology", "kind": "mechanism", "summary": "QCD allows a CP-violating theta-bar = theta + arg det M_q, and the neutron EDM bound forces |theta-bar| below about 1e-10: the strong CP problem the axion solves. The axion mass is set by QCD's topological susceptibility, m_a^2 f_a^2 = chi_top, and lattice results for chi_top(T) fix the axion relic abundance from misalignment.", "map": "\\bar\\theta=\\theta+\\arg\\det M_q\\lesssim10^{-10};\\ m_a^2f_a^2=\\chi_{\\rm top},\\ m_a\\approx5.7\\,\\mu{\\rm eV}\\left(\\frac{10^{12}\\,{\\rm GeV}}{f_a}\\right)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2162", "a": "06-particle-physics/beyond-the-standard-model/baryogenesis-and-matter-antimatter", "b": "06-particle-physics/neutrino-physics/neutrino-mass-and-double-beta-decay", "name": "Leptogenesis and Majorana neutrino mass", "kind": "mechanism", "summary": "In thermal leptogenesis, the heavy Majorana neutrinos of the seesaw decay CP-asymmetrically and sphalerons convert the resulting lepton asymmetry into baryons. Seeing neutrinoless double-beta decay would establish the lepton-number violation and Majorana nature leptogenesis needs, but would not fix its high-scale CP phases.", "map": "m_\\nu\\simeq m_D^2/M_R,\\ Y_B=\\tfrac{28}{79}Y_{B-L};\\ M_1\\gtrsim10^9\\,{\\rm GeV}\\ (\\text{Davidson-Ibarra})", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2163", "a": "06-particle-physics/beyond-the-standard-model/baryogenesis-and-matter-antimatter", "b": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "name": "Sphalerons: B+L violation from the electroweak anomaly", "kind": "mechanism", "summary": "Through the SU(2) anomaly, baryon and lepton number change whenever the Chern-Simons number changes ('t Hooft). Tunneling is negligible today, but thermal sphalerons are fast above the electroweak scale. They supply Sakharov's B violation and convert lepton asymmetries into baryons while conserving B-L.", "map": "\\partial_\\mu j_B^\\mu=\\partial_\\mu j_L^\\mu=\\frac{N_f}{32\\pi^2}\\left(g^2W\\tilde W-g'^2B\\tilde B\\right),\\ \\Delta B=\\Delta L=N_f\\Delta N_{CS}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2164", "a": "06-particle-physics/beyond-the-standard-model/baryogenesis-and-matter-antimatter", "b": "06-particle-physics/standard-model/cp-violation", "name": "CKM CP violation is too weak for the baryon asymmetry", "kind": "mechanism", "summary": "Sakharov's second condition needs C and CP violation. The CKM phase provides it, but at the electroweak scale its effect is suppressed by the Jarlskog invariant times quark-mass differences to about 1e-20, far below eta_B of about 6e-10, so a new CP-violating source is required.", "map": "J\\prod_{i<j}(m_{u_i}^2-m_{u_j}^2)(m_{d_i}^2-m_{d_j}^2)/T_{EW}^{12}\\sim10^{-20}\\ll\\eta_B\\approx6\\times10^{-10}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2165", "a": "06-particle-physics/beyond-the-standard-model/baryogenesis-and-matter-antimatter", "b": "06-particle-physics/standard-model/electroweak-theory", "name": "Electroweak phase transition and baryogenesis", "kind": "mechanism", "summary": "Electroweak baryogenesis needs a strongly first-order transition, so that sphalerons switch off inside expanding bubbles. Lattice studies show the SM transition is a smooth crossover (near 160 GeV) for m_h above about 70 GeV. A 125 GeV Higgs therefore rules out SM electroweak baryogenesis and points to extended scalar sectors that colliders can test.", "map": "v(T_c)/T_c\\gtrsim1\\ (\\text{no washout});\\ \\text{SM: crossover at }T\\approx160\\,{\\rm GeV}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2166", "a": "06-particle-physics/beyond-the-standard-model/dark-matter-particle-candidates", "b": "06-particle-physics/neutrino-physics/sterile-neutrinos-and-anomalies", "name": "keV sterile neutrinos as warm dark matter", "kind": "shared object", "summary": "A keV-mass gauge-singlet neutrino produced by oscillations (Dodelson-Widrow) or resonantly is a warm dark-matter candidate. X-ray searches for nu_s -> nu gamma and small-scale structure constrain it, and the 3.5 keV line claim is contested and unconfirmed. The eV-scale steriles invoked for the short-baseline anomalies are a separate mass range.", "map": "\\Gamma_{\\nu_s\\to\\nu\\gamma}=\\frac{9\\alpha G_F^2}{1024\\pi^4}\\sin^22\\theta\\,m_s^5", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2167", "a": "06-particle-physics/beyond-the-standard-model/extra-dimensions-and-hierarchy-problem", "b": "06-particle-physics/quantum-field-theory/conformal-field-theory", "name": "Warped extra dimension dual to a composite-Higgs CFT", "kind": "duality", "summary": "By the AdS/CFT dictionary, a Randall-Sundrum slice of AdS5 with an IR brane is dual to a strongly coupled, nearly conformal 4D theory that confines at the TeV scale. KK modes map to composite resonances, the IR-brane Higgs to a composite Higgs, and the warp factor to the RG scale (Arkani-Hamed-Porrati-Randall 2001).", "map": "z\\leftrightarrow1/\\mu,\\ \\text{IR brane}\\leftrightarrow\\Lambda_{\\rm comp}\\sim{\\rm TeV},\\ m_{\\rm KK}\\leftrightarrow m_\\rho,\\ \\Delta=2+\\sqrt{4+m^2L^2}", "breaks": "The duality is derived only for large-N theories with string duals such as N=4 SYM. The CFT dual to a phenomenological RS model is not known explicitly, so the map is a heuristic dictionary.", "confidence": "current research", "strength": 2}
{"id": "C2168", "a": "06-particle-physics/beyond-the-standard-model/extra-dimensions-and-hierarchy-problem", "b": "06-particle-physics/standard-model/higgs-boson", "name": "Hierarchy problem: the unprotected Higgs mass", "kind": "mechanism", "summary": "The Higgs mass term is the SM's only relevant operator and no symmetry protects it, so heavy thresholds feed into m_H^2. Large and warped extra dimensions, compositeness and SUSY are the proposed cures, and LHC null results sharpen the puzzle into the little hierarchy problem.", "map": "\\delta m_H^2\\simeq-\\frac{3y_t^2}{8\\pi^2}\\Lambda^2;\\ \\text{ADD: }M_{\\rm Pl}^2\\sim M_*^{n+2}R^n;\\ \\text{RS: }m_{\\rm TeV}=e^{-kr_c\\pi}M_{\\rm Pl}", "breaks": "In dimensional regularization no Lambda^2 appears; the physical issue is sensitivity to the masses of heavy new particles, and naturalness is a criterion, not a law.", "confidence": "established", "strength": 3}
{"id": "C2169", "a": "06-particle-physics/beyond-the-standard-model/grand-unification-and-proton-decay", "b": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "name": "Gauge-coupling unification from RG running", "kind": "mechanism", "summary": "GUTs predict that the three SM gauge couplings meet at one scale. With SM coefficients, one-loop running misses a single meeting point; with MSSM coefficients the couplings meet near 2e16 GeV. That scale sets M_X and so the proton lifetime.", "map": "\\alpha_i^{-1}(\\mu)=\\alpha_i^{-1}(m_Z)-\\frac{b_i}{2\\pi}\\ln\\frac{\\mu}{m_Z};\\ b^{\\rm SM}=(\\tfrac{41}{10},-\\tfrac{19}{6},-7),\\ b^{\\rm MSSM}=(\\tfrac{33}{5},1,-3)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2170", "a": "06-particle-physics/beyond-the-standard-model/grand-unification-and-proton-decay", "b": "06-particle-physics/standard-model/electroweak-theory", "name": "sin^2 theta_W = 3/8 at the unification scale", "kind": "mechanism", "summary": "Embedding SU(3)xSU(2)xU(1) in SU(5) fixes the hypercharge normalization, g_1 = sqrt(5/3) g', so sin^2 theta_W = 3/8 at the unification scale. Running down to m_Z gives about 0.21 in the SM and close to the measured 0.2312 in the MSSM. The same embedding explains charge quantization (Q_d = Q_e/3).", "map": "\\sin^2\\theta_W=\\frac{g'^2}{g^2+g'^2}\\Big|_{M_{\\rm GUT}}=\\frac38\\ \\to\\ 0.2312\\ (m_Z,\\overline{\\rm MS})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2171", "a": "06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2", "b": "06-particle-physics/quantum-field-theory/feynman-diagrams-and-scattering-amplitudes", "name": "QED to five loops in the lepton g-2", "kind": "method transfer", "summary": "The Schwinger term alpha/2pi began the precision testing of perturbative QFT. The QED part of the lepton anomalous moment is now known to tenth order (12,672 diagrams; Aoyama, Kinoshita, Nio). The electron g-2 therefore measures alpha at the sub-ppb level, while the muon g-2 uncertainty is dominated by non-perturbative hadronic loops.", "map": "a_\\ell^{\\rm QED}=\\sum_{n=1}^{5}C_n\\left(\\frac{\\alpha}{\\pi}\\right)^n,\\ C_1=\\tfrac12,\\ C_2^{(e)}=-0.3285\\dots", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2172", "a": "06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2", "b": "06-particle-physics/quantum-field-theory/lattice-field-theory", "name": "Lattice HVP settles the muon g-2 comparison", "kind": "method transfer", "summary": "Hadronic vacuum polarization limits the SM prediction of a_mu. Lattice QCD (BMW 2020 onward) puts it above the e+e- dispersive value and closer to experiment, and the 2025 Theory Initiative update, which adopts lattice HVP, agrees with the final Fermilab result. The tension within the e+e- data (CMD-3 vs earlier experiments) is still unexplained.", "map": "a_\\mu^{\\rm HVP,LO}=\\alpha^2\\int_0^\\infty dt\\,K(t)\\,G_{\\rm em}(t)\\ \\ (\\text{Euclidean vector correlator})", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2173", "a": "06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2", "b": "06-particle-physics/standard-model/electroweak-theory", "name": "W mass: precision electroweak test and the CDF outlier", "kind": "shared object", "summary": "The W mass follows from G_F, alpha and m_Z plus loop corrections Delta r that depend on the top and Higgs masses, which makes it a sharp new-physics probe (through the oblique T parameter). CDF's 2022 value sits about 7 sigma above the SM, but ATLAS (2024) and CMS (2024) agree with the SM, so CDF is treated as an unresolved outlier.", "map": "m_W^2\\left(1-\\frac{m_W^2}{m_Z^2}\\right)=\\frac{\\pi\\alpha}{\\sqrt2G_F}(1+\\Delta r);\\ m_W^{\\rm SM}\\approx80357\\,{\\rm MeV}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2174", "a": "06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2", "b": "06-particle-physics/standard-model/flavor-physics-and-ckm", "name": "B anomalies as tests of lepton-flavor universality", "kind": "shared object", "summary": "The lepton-universality ratios R_K(*) and R_D(*) in B decays were the flagship flavor anomalies. LHCb's 2022 reanalysis brought R_K(*) back to the SM, while R_D(*) is still about 3 sigma high. The case shows how flavor observables are judged against CKM-based predictions.", "map": "R_K=\\frac{\\mathcal B(B\\to K\\mu\\mu)}{\\mathcal B(B\\to Kee)}\\approx1\\ ({\\rm SM}),\\ R_{D^{(*)}}=\\frac{\\mathcal B(B\\to D^{(*)}\\tau\\nu)}{\\mathcal B(B\\to D^{(*)}\\ell\\nu)}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2175", "a": "06-particle-physics/beyond-the-standard-model/supersymmetry", "b": "06-particle-physics/standard-model/higgs-boson", "name": "SUSY Higgs mass bound and the 125 GeV Higgs", "kind": "mechanism", "summary": "Boson-fermion loop cancellation removes the quadratic sensitivity of m_H^2, and the MSSM predicts a light Higgs with m_h <= m_Z |cos 2beta| at tree level. Reaching 125 GeV needs large stop loop corrections, from multi-TeV stops or maximal mixing, which is in tension with naturalness.", "map": "m_h^{\\rm tree}\\le m_Z|\\cos2\\beta|;\\ \\Delta m_h^2\\simeq\\frac{3m_t^4}{2\\pi^2v^2}\\left[\\ln\\frac{M_S^2}{m_t^2}+\\frac{X_t^2}{M_S^2}\\left(1-\\frac{X_t^2}{12M_S^2}\\right)\\right]", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2176", "a": "06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc", "b": "06-particle-physics/standard-model/higgs-boson", "name": "The LHC discovered and now measures the Higgs", "kind": "shared object", "summary": "ATLAS and CMS discovered the 125 GeV Higgs in 2012, mainly via gluon fusion with H->gamma gamma and ZZ*->4l. The LHC now fits coupling modifiers kappa_i, which agree with the SM at the 5-10% level, and bounds the Higgs self-coupling through HH production.", "map": "\\sigma\\cdot{\\rm BR}=\\frac{\\kappa_{\\rm prod}^2\\kappa_{\\rm dec}^2}{\\kappa_H^2}(\\sigma\\cdot{\\rm BR})_{\\rm SM};\\ m_H\\approx125\\,{\\rm GeV}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2177", "a": "06-particle-physics/collider-and-experimental-particle-physics/jets-and-qcd-phenomenology", "b": "06-particle-physics/quantum-field-theory/effective-field-theory", "name": "Soft-collinear EFT resums jet and event-shape logs", "kind": "method transfer", "summary": "SCET separates hard, collinear and soft modes with power counting lambda ~ p_T/Q and proves factorization theorems for jet observables. The RG evolution of each factor resums Sudakov double logarithms. It is used for thrust-based alpha_s fits, jet vetoes and jet mass.", "map": "\\frac{d\\sigma}{d\\tau}=H(Q,\\mu)\\,J\\otimes J\\otimes S(\\mu),\\ \\text{resumming }\\alpha_s^nL^{2n}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2178", "a": "06-particle-physics/collider-and-experimental-particle-physics/jets-and-qcd-phenomenology", "b": "06-particle-physics/quantum-field-theory/feynman-diagrams-and-scattering-amplitudes", "name": "Collinear factorization of amplitudes gives jets", "kind": "method transfer", "summary": "In soft and collinear limits, QCD amplitudes factorize into lower-point amplitudes times universal splitting functions, which makes infrared-safe jet rates computable (Sterman-Weinberg). Spinor-helicity and unitarity methods supply the multi-parton NLO and NNLO matrix elements behind multi-jet predictions.", "map": "|\\mathcal M_{n+1}|^2\\xrightarrow{i\\parallel j}\\frac{8\\pi\\alpha_s}{s_{ij}}\\hat P_{ij}(z)\\,|\\mathcal M_n|^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2179", "a": "06-particle-physics/collider-and-experimental-particle-physics/jets-and-qcd-phenomenology", "b": "06-particle-physics/standard-model/quantum-chromodynamics", "name": "Jets are the observable form of QCD partons", "kind": "shared object", "summary": "Jets trace hard quarks and gluons through showering and hadronization. IR-safe algorithms such as anti-kT make them calculable in perturbative QCD, and jet rates, event shapes and 4-jet angular correlations measure alpha_s and the SU(3) color factors.", "map": "C_F=\\tfrac43,\\ C_A=3,\\ C_A/C_F=\\tfrac94\\ (\\text{LEP 4-jet});\\ \\alpha_s(m_Z)\\approx0.118", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2180", "a": "06-particle-physics/collider-and-experimental-particle-physics/machine-learning-in-hep", "b": "06-particle-physics/quantum-field-theory/lattice-field-theory", "name": "Normalizing flows for lattice gauge-field sampling", "kind": "method transfer", "summary": "Generative models from HEP machine learning, notably gauge-equivariant normalizing flows (Albergo, Kanwar, Shanahan and collaborators), are trained to sample lattice field configurations directly. The aim is to beat critical slowing down and topological freezing near the continuum limit. The same flow technology also drives phase-space sampling in event generators.", "map": "q_\\theta(U)=r\\big(f_\\theta^{-1}(U)\\big)\\left|\\det\\frac{\\partial f_\\theta^{-1}}{\\partial U}\\right|\\approx\\frac{e^{-S(U)}}{Z},\\ \\text{reweighted or Metropolis-corrected}", "breaks": "Flows are not yet competitive with HMC at physical QCD volumes, and their training cost grows steeply with lattice volume.", "confidence": "current research", "strength": 2}
{"id": "C2181", "a": "06-particle-physics/collider-and-experimental-particle-physics/monte-carlo-event-generators", "b": "06-particle-physics/standard-model/quantum-chromodynamics", "name": "Parton showers and string hadronization model QCD", "kind": "method transfer", "summary": "Parton showers implement DGLAP evolution as a Markov chain with Sudakov no-emission probabilities. Hadronization uses either the Lund string, a linear confining flux tube that breaks by Schwinger-like q-qbar tunneling, or cluster models built on preconfinement.", "map": "\\Delta(t_0,t)=\\exp\\!\\left[-\\int_{t_0}^{t}\\frac{dt'}{t'}\\!\\int\\!dz\\frac{\\alpha_s}{2\\pi}P(z)\\right],\\ P_{q\\bar q}\\propto e^{-\\pi m_\\perp^2/\\kappa}", "breaks": "Shower kernels follow from QCD factorization, but hadronization models are phenomenological, with parameters tuned to data rather than derived from QCD.", "confidence": "established", "strength": 3}
{"id": "C2182", "a": "06-particle-physics/neutrino-physics/neutrino-mass-and-double-beta-decay", "b": "06-particle-physics/quantum-field-theory/effective-field-theory", "name": "Weinberg operator: neutrino mass at dimension 5 in SMEFT", "kind": "mechanism", "summary": "Weinberg's (LH)(LH)/Lambda is the only dimension-5 operator built from SM fields, and it gives Majorana neutrino masses m_nu ~ v^2/Lambda. A mass near 0.05 eV then points to Lambda of 1e14-1e15 GeV. Seesaw types I-III are its tree-level UV completions, and neutrinoless double-beta decay tests its Delta L = 2.", "map": "\\frac{c}{\\Lambda}(\\bar L^c\\tilde H^*)(\\tilde H^\\dagger L)\\ \\to\\ m_\\nu\\sim\\frac{c\\,v^2}{\\Lambda},\\ \\text{type I: }\\frac{c}{\\Lambda}=\\frac{y^2}{M_R}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2183", "a": "06-particle-physics/neutrino-physics/neutrino-oscillations", "b": "06-particle-physics/standard-model/electroweak-theory", "name": "MSW effect from charged-current forward scattering", "kind": "mechanism", "summary": "Coherent forward scattering of nu_e on electrons through W exchange adds a potential sqrt2 G_F n_e that changes the effective mixing; the flavor-universal Z-exchange term cancels for active neutrinos. The adiabatic MSW resonance explains the energy dependence of solar nu_e survival (SNO, Borexino) and gives long-baseline experiments sensitivity to the mass ordering.", "map": "V_{CC}=\\sqrt2G_Fn_e;\\ \\text{resonance: }2\\sqrt2G_Fn_eE=\\Delta m^2\\cos2\\theta", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2184", "a": "06-particle-physics/neutrino-physics/neutrino-oscillations", "b": "06-particle-physics/standard-model/flavor-physics-and-ckm", "name": "PMNS and CKM: the same unitary mixing structure", "kind": "identity", "summary": "PMNS and CKM are both 3x3 unitary matrices that arise because mass and weak-interaction bases are misaligned. They share the parametrization (three angles and one Dirac phase, plus two Majorana phases for PMNS) and the Jarlskog invariant that controls CP violation. T2K, NOvA, DUNE and Hyper-K measure leptonic CP violation as the difference between nu_mu->nu_e and the antineutrino channel.", "map": "J=c_{12}s_{12}c_{23}s_{23}c_{13}^2s_{13}\\sin\\delta;\\ J_{\\rm CKM}\\approx3\\times10^{-5},\\ J_{\\rm PMNS}^{\\max}\\approx0.033", "breaks": "CKM angles are small and hierarchical while PMNS angles are large. Neutrino masses may be Majorana (seesaw) rather than Yukawa. Matter effects mimic a CP asymmetry in long-baseline data.", "confidence": "established", "strength": 3}
{"id": "C2185", "a": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "b": "06-particle-physics/standard-model/electroweak-theory", "name": "Gauge-anomaly cancellation fixes SM charges", "kind": "mechanism", "summary": "SU(3)xSU(2)xU(1) is consistent only because gauge and mixed gauge-gravitational anomalies cancel within each generation, quarks against leptons. This requires N_c = 3 and the observed hypercharges, and it implies charge quantization. Witten's global SU(2) anomaly further requires an even number of doublets.", "map": "\\mathrm{Tr}[Y^3]=\\mathrm{Tr}[Y]=0,\\ \\mathrm{Tr}_{SU(2)}[Y]=N_c\\cdot\\tfrac16-\\tfrac12=0\\Rightarrow N_c=3", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2186", "a": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "b": "06-particle-physics/standard-model/quantum-chromodynamics", "name": "Axial anomaly: eta' mass and pi0 -> gamma gamma", "kind": "mechanism", "summary": "QCD has no ninth Goldstone boson because the anomaly and instantons break U(1)_A ('t Hooft). The Witten-Veneziano relation ties the eta' mass to the topological susceptibility, and the pi0 -> gamma gamma rate, fixed by the anomaly coefficient, confirms N_c = 3.", "map": "\\partial_\\mu j_5^\\mu=\\frac{N_fg_s^2}{16\\pi^2}G\\tilde G;\\ m_{\\eta'}^2\\approx\\frac{2N_f\\chi_{\\rm top}}{f_\\pi^2};\\ \\Gamma_{\\pi^0\\to\\gamma\\gamma}\\propto N_c^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2187", "a": "06-particle-physics/quantum-field-theory/effective-field-theory", "b": "06-particle-physics/standard-model/electroweak-theory", "name": "Fermi theory as the EFT of W exchange; SMEFT", "kind": "identity", "summary": "Fermi's four-fermion contact interaction is the low-energy limit of W exchange. It violates unitarity below about 1 TeV, which pointed to the weak scale. It is the template for SMEFT, where dimension-6 operators suppressed by Lambda^2 parametrize heavy new physics in electroweak and Higgs data.", "map": "\\frac{G_F}{\\sqrt2}=\\frac{g^2}{8m_W^2};\\ \\mathcal L_{\\rm SMEFT}=\\mathcal L_{\\rm SM}+\\sum_i\\frac{C_i}{\\Lambda^2}O_i^{(6)}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2188", "a": "06-particle-physics/quantum-field-theory/effective-field-theory", "b": "06-particle-physics/standard-model/flavor-physics-and-ckm", "name": "Weak effective Hamiltonian and Wilson coefficients", "kind": "method transfer", "summary": "Flavor-changing decays are computed with a weak effective Hamiltonian obtained by integrating out W, Z and top. The operator product expansion separates short-distance Wilson coefficients, run from m_W to m_b with anomalous dimensions, from long-distance hadronic matrix elements. New physics shows up as shifts such as C_9 and C_10 in b -> s l l.", "map": "\\mathcal H_{\\rm eff}=-\\frac{4G_F}{\\sqrt2}V_{tb}V_{ts}^*\\sum_iC_i(\\mu)\\,O_i(\\mu)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2189", "a": "06-particle-physics/quantum-field-theory/effective-field-theory", "b": "06-particle-physics/standard-model/quantum-chromodynamics", "name": "Chiral perturbation theory: EFT of QCD's Goldstones", "kind": "method transfer", "summary": "Spontaneous breaking of SU(3)_L x SU(3)_R to SU(3)_V makes the pions, kaons and eta pseudo-Goldstone bosons. Chiral perturbation theory (Weinberg, Gasser-Leutwyler) is the EFT that expands in p/Lambda_chi, with Lambda_chi of about 4 pi f_pi, roughly 1 GeV. Its leading term gives the GMOR relation.", "map": "\\mathcal L_2=\\frac{f^2}{4}{\\rm Tr}(\\partial_\\mu U\\partial^\\mu U^\\dagger)+\\frac{f^2B}{2}{\\rm Tr}(MU^\\dagger+UM^\\dagger)\\Rightarrow m_\\pi^2=B(m_u+m_d)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2190", "a": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "b": "06-particle-physics/standard-model/quantum-chromodynamics", "name": "QCD is SU(3) Yang-Mills coupled to quarks", "kind": "identity", "summary": "QCD is the non-abelian Yang-Mills theory for SU(3) color. The general gauge-theory machinery supplies gluon self-interactions (from the structure constants), Faddeev-Popov ghosts and the sign of the one-loop beta function, as well as the confining phase and the theta vacua.", "map": "G^a_{\\mu\\nu}=\\partial_\\mu A^a_\\nu-\\partial_\\nu A^a_\\mu+g_sf^{abc}A^b_\\mu A^c_\\nu,\\ a=1,\\dots,8", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2191", "a": "06-particle-physics/quantum-field-theory/lattice-field-theory", "b": "06-particle-physics/standard-model/flavor-physics-and-ckm", "name": "Lattice decay constants and form factors fix CKM", "kind": "method transfer", "summary": "Extracting CKM elements needs hadronic inputs that only lattice QCD supplies at percent precision: decay constants (f_K/f_pi, f_B), the kaon bag parameter B_K for epsilon_K, and B->D* and B->pi form factors for |V_cb| and |V_ub|. FLAG averages feed the unitarity-triangle fits, and the first-row unitarity deficit depends on these inputs.", "map": "\\frac{\\Gamma(K\\to\\mu\\nu)}{\\Gamma(\\pi\\to\\mu\\nu)}\\propto\\frac{|V_{us}|^2}{|V_{ud}|^2}\\frac{f_K^2}{f_\\pi^2};\\ |V_{ud}|^2+|V_{us}|^2+|V_{ub}|^2=1", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2192", "a": "06-particle-physics/quantum-field-theory/lattice-field-theory", "b": "06-particle-physics/standard-model/hadron-spectroscopy-and-exotics", "name": "Hadron spectrum and exotics from lattice QCD", "kind": "method transfer", "summary": "Lattice QCD reproduces the light hadron spectrum at the percent level (BMW 2008) and, with QED added, the neutron-proton mass splitting. Resonances and exotic candidates (X(3872), T_cc, hybrids) are studied by mapping finite-volume energy levels to scattering amplitudes with the Lüscher method.", "map": "p\\cot\\delta_0(p)=\\frac{2}{\\sqrt\\pi L}Z_{00}\\!\\left(1;\\left(\\frac{pL}{2\\pi}\\right)^2\\right)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2193", "a": "06-particle-physics/quantum-field-theory/lattice-field-theory", "b": "06-particle-physics/standard-model/quantum-chromodynamics", "name": "Lattice QCD: QCD defined and solved non-perturbatively", "kind": "method transfer", "summary": "Wilson's lattice gauge action gives QCD a non-perturbative definition. Monte Carlo sampling of the Euclidean path integral then yields what perturbation theory cannot reach: the string tension and linear confining potential, hadron masses, quark masses and alpha_s.", "map": "S_W=\\beta\\sum_{x,\\mu<\\nu}\\left(1-\\tfrac13\\mathrm{Re\\,Tr}\\,U_{\\mu\\nu}\\right),\\ \\beta=6/g^2;\\ \\langle W(C)\\rangle\\sim e^{-\\sigma A}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2194", "a": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "b": "06-particle-physics/standard-model/higgs-boson", "name": "Running Higgs quartic: electroweak vacuum metastability", "kind": "mechanism", "summary": "With m_h = 125 GeV and m_t of about 172.5 GeV, NNLO running drives the Higgs quartic lambda negative near 1e10-1e11 GeV. The electroweak vacuum is therefore metastable, with a lifetime far beyond the age of the universe. The conclusion depends sensitively on m_t and alpha_s.", "map": "\\beta_\\lambda=\\frac{1}{16\\pi^2}\\left(24\\lambda^2+12\\lambda y_t^2-6y_t^4+\\dots\\right),\\ V\\supset\\lambda(H^\\dagger H)^2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2195", "a": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "b": "06-particle-physics/standard-model/quantum-chromodynamics", "name": "Asymptotic freedom and dimensional transmutation", "kind": "mechanism", "summary": "The one-loop beta function of SU(3) with six flavors is negative, so alpha_s falls logarithmically at high Q (Gross-Wilczek and Politzer, 1973). The classically scale-free theory also generates the hadronic scale Lambda_QCD, a few hundred MeV, from a dimensionless coupling.", "map": "\\alpha_s(Q^2)=\\frac{4\\pi}{\\beta_0\\ln(Q^2/\\Lambda^2)},\\ \\beta_0=11-\\tfrac23n_f,\\ \\alpha_s(m_Z)\\approx0.118", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2196", "a": "06-particle-physics/beyond-the-standard-model", "b": "07-nuclear-physics/nuclear-astrophysics/big-bang-nucleosynthesis", "name": "BBN as a probe of BSM physics", "kind": "method transfer", "summary": "Light-element abundances constrain extra relativistic species (N_eff), late-decaying particles, MeV-scale thermal dark matter and time-varying constants; BBN is the earliest laboratory for new physics.", "map": "\\Delta Y_p\\approx0.013\\,\\Delta N_{\\text{eff}};\\ H^2=\\frac{8\\pi G}{3}\\frac{\\pi^2}{30}g_*T^4", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2197", "a": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "b": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "name": "Axion emission from nucleon bremsstrahlung", "kind": "shared object", "summary": "Axion bounds from SN 1987A and neutron-star cooling rest on nuclear physics: NN bremsstrahlung rates, dense-matter EOS and superfluid gaps set how fast axions drain energy from hot nuclear matter.", "map": "N+N\\to N+N+a;\\ \\epsilon_a\\propto g_{aN}^2\\,T^{4\\text{-}6}\\ (\\text{degenerate})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2198", "a": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "name": "Nuclear transitions as dark-boson searches", "kind": "shared object", "summary": "Excited-nucleus decays via internal pair creation can reveal light bosons; the ATOMKI 8Be/4He anomaly ('X17', ~17 MeV) prompted protophobic dark-photon models but is unconfirmed and contested (MEG II found no signal).", "map": "^8\\text{Be}^*\\to{}^8\\text{Be}+X(\\to e^+e^-),\\ m_X\\approx17\\ \\text{MeV}", "breaks": "", "confidence": "proposed", "strength": 1}
{"id": "C2199", "a": "06-particle-physics/beyond-the-standard-model/baryogenesis-and-matter-antimatter", "b": "07-nuclear-physics/nuclear-astrophysics/big-bang-nucleosynthesis", "name": "Baryon-to-photon ratio from BBN deuterium", "kind": "shared object", "summary": "Baryogenesis must produce the eta_B that BBN measures from the primordial D/H ratio (and the CMB confirms); BBN is the earliest direct test of any baryogenesis model.", "map": "\\eta_B=\\frac{n_B-n_{\\bar B}}{n_\\gamma}\\approx6.1\\times10^{-10}\\ (\\text{BBN D/H}),\\ \\eta_{10}=273.9\\,\\Omega_bh^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2200", "a": "06-particle-physics/beyond-the-standard-model/dark-matter-particle-candidates", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Nuclear structure factors for WIMP scattering", "kind": "method transfer", "summary": "Spin-dependent WIMP-nucleus cross sections need the proton and neutron spin content of each target nucleus, computed with the shell model; spin-independent rates need nuclear form factors and the coherent A^2 enhancement.", "map": "\\sigma_{SD}\\propto\\frac{J+1}{J}\\left[a_p\\langle S_p\\rangle+a_n\\langle S_n\\rangle\\right]^2;\\ \\sigma_{SI}\\propto A^2|F(q)|^2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2201", "a": "06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2", "b": "07-nuclear-physics/hadron-and-nucleon-structure/nucleon-spin-and-form-factors", "name": "Proton radius puzzle as a precision anomaly", "kind": "shared object", "summary": "The muonic-hydrogen proton radius disagreed with e-p data by ~5 sigma, a case study for judging precision anomalies (now largely resolved toward 0.84 fm); hadronic structure also limits the muon g-2 prediction.", "map": "\\langle r_E^2\\rangle=-6\\,dG_E/dQ^2|_0;\\ r_p^{\\mu H}=0.84\\ \\text{fm vs } 0.88\\ \\text{fm (old e-p)}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2202", "a": "06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2", "b": "07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions", "name": "Neutron lifetime beam-bottle discrepancy", "kind": "shared object", "summary": "Beam (~888 s) and bottle (~878 s) neutron lifetimes disagree by ~4 sigma; proposed dark decay channels are tested like other precision anomalies, and the lifetime also feeds BBN and V_ud.", "map": "\\tau_n^{\\text{beam}}-\\tau_n^{\\text{bottle}}\\approx9\\ \\text{s};\\ \\tau_n^{-1}\\propto G_F^2|V_{ud}|^2(1+3g_A^2)", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2203", "a": "06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc", "b": "07-nuclear-physics/hadron-and-nucleon-structure", "name": "Proton structure as input to every LHC cross section", "kind": "shared object", "summary": "LHC rates factorize into partonic cross sections convolved with PDFs measured in DIS; PDF uncertainties now limit precision Higgs and W-mass measurements.", "map": "\\sigma_{pp\\to X}=\\sum_{ij}\\int dx_1dx_2\\,f_i(x_1,\\mu_F)f_j(x_2,\\mu_F)\\hat\\sigma_{ij\\to X}(x_1x_2s)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2204", "a": "06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc", "b": "07-nuclear-physics/hadron-and-nucleon-structure/electron-ion-collider", "name": "Next QCD collider after HERA and the LHC", "kind": "shared object", "summary": "The EIC extends HERA's ep programme to polarized and nuclear beams; its small-x gluon and nuclear PDF measurements feed LHC and heavy-ion predictions, and it reuses collider accelerator and detector technology.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2205", "a": "06-particle-physics/collider-and-experimental-particle-physics/jets-and-qcd-phenomenology", "b": "07-nuclear-physics/hadron-and-nucleon-structure/parton-distribution-functions", "name": "DGLAP kernels are parton-shower kernels", "kind": "identity", "summary": "The splitting functions P(z) that evolve PDFs in ln mu^2 are the same kernels that generate collinear emissions in parton showers and jet evolution (space-like vs time-like evolution).", "map": "\\text{PDF: }\\partial_{\\ln\\mu^2}f=\\tfrac{\\alpha_s}{2\\pi}P\\otimes f\\ \\leftrightarrow\\ \\text{shower: }dP=\\tfrac{\\alpha_s}{2\\pi}\\tfrac{dt}{t}P(z)dz", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2206", "a": "06-particle-physics/collider-and-experimental-particle-physics/jets-and-qcd-phenomenology", "b": "07-nuclear-physics/heavy-ion-physics/jet-quenching", "name": "Jets as tomographic probes of the QGP", "kind": "method transfer", "summary": "IRC-safe jet algorithms, substructure and grooming developed for pp physics are applied in PbPb collisions; medium-induced radiation modifies the vacuum shower and the pp jets serve as the baseline for R_AA.", "map": "R_{AA}=\\frac{dN_{AA}/dp_T}{\\langle N_{\\text{coll}}\\rangle dN_{pp}/dp_T},\\ \\Delta E\\propto\\alpha_s\\hat qL^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2207", "a": "06-particle-physics/collider-and-experimental-particle-physics/monte-carlo-event-generators", "b": "07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry", "name": "Geant4 transport for detectors and dose", "kind": "method transfer", "summary": "Geant4, built for HEP detector simulation, is a standard transport code for nuclear detector response and dosimetry, sharing the same cross-section libraries and showering physics.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C2208", "a": "06-particle-physics/collider-and-experimental-particle-physics/monte-carlo-event-generators", "b": "07-nuclear-physics/heavy-ion-physics/collective-flow-and-hydrodynamics", "name": "Collectivity and hadronization in small systems", "kind": "shared object", "summary": "High-multiplicity pp collisions show flow-like correlations and strangeness enhancement once thought unique to nuclear collisions; event generators add core-corona or rope hadronization to describe them.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2209", "a": "06-particle-physics/collider-and-experimental-particle-physics/monte-carlo-event-generators", "b": "07-nuclear-physics/heavy-ion-physics/jet-quenching", "name": "Quenching models built on vacuum parton showers", "kind": "method transfer", "summary": "Jet-quenching Monte Carlos (JEWEL, MARTINI, JETSCAPE) embed PYTHIA-type showers in an evolving medium, adding medium-induced splittings and recoils to the Sudakov evolution.", "map": "\\Delta(t_1,t_2)=\\exp[-\\int\\tfrac{dt}{t}\\int dz\\tfrac{\\alpha_s}{2\\pi}(P^{\\text{vac}}+P^{\\text{med}})]", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2210", "a": "06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers", "b": "07-nuclear-physics/applied-nuclear-physics", "name": "Shared radiation-detector toolkit", "kind": "method transfer", "summary": "Applied nuclear physics (reactor instrumentation, dosimetry, isotope assay) and collider experiments use the same detector families and the same interaction physics; technology flows both ways.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C2211", "a": "06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers", "b": "07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry", "name": "Same stopping-power physics and detector technologies", "kind": "method transfer", "summary": "Bethe-Bloch energy loss, scintillators, gas counters and silicon sensors are common to collider detectors and nuclear radiation detection; HEP trackers and calorimeters descend from nuclear counters and feed back into dosimetry instruments.", "map": "-\\langle dE/dx\\rangle=Kz^2\\frac{Z}{A}\\frac{1}{\\beta^2}[\\ldots]\\ \\text{(both)};\\ \\sigma_E/E=a/\\sqrt{E}\\ \\leftrightarrow\\ 2.355\\sqrt{Fw/E}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2212", "a": "06-particle-physics/neutrino-physics", "b": "07-nuclear-physics/nuclear-astrophysics/big-bang-nucleosynthesis", "name": "Neutrino decoupling, N_eff and n/p freeze-out", "kind": "mechanism", "summary": "Weak n<->p conversions with neutrinos freeze out at T~0.8 MeV and set Y_p; the number of light neutrino species (N_eff) changes the expansion rate and hence the helium yield.", "map": "\\frac{n}{p}=e^{-Q/k_BT_f},\\ Q=1.293\\ \\text{MeV};\\ \\Gamma_{n\\leftrightarrow p}\\sim G_F^2T^5\\approx H\\propto\\sqrt{g_*}T^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2213", "a": "06-particle-physics/neutrino-physics", "b": "07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions", "name": "Pauli's neutrino and Fermi's beta decay", "kind": "historical", "summary": "The neutrino was invented to save energy conservation in beta decay and first detected via inverse beta decay at a reactor; beta spectra remain the key laboratory window on neutrino properties.", "map": "\\frac{d\\Gamma}{dE_e}\\propto F(Z,E_e)\\,p_eE_e(E_0-E_e)^2\\ \\leftrightarrow\\ \\bar\\nu_e+p\\to e^++n", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2214", "a": "06-particle-physics/neutrino-physics/neutrino-experiments-and-sources", "b": "07-nuclear-physics/applied-nuclear-physics/nuclear-reactors-and-energy", "name": "Reactors as the strongest terrestrial antineutrino source", "kind": "shared object", "summary": "Fission-fragment beta decays make ~6 antineutrinos per fission (~2x10^20 per second per GW_th); reactors gave the first neutrino detection, theta_13 (Daya Bay) and the JUNO ordering programme, and allow reactor monitoring.", "map": "\\bar\\nu_e+p\\to e^++n\\ (E_{\\text{th}}=1.8\\ \\text{MeV});\\ \\dot N_{\\bar\\nu}\\approx2\\times10^{20}\\ \\text{s}^{-1}\\,\\text{GW}_{\\text{th}}^{-1}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2215", "a": "06-particle-physics/neutrino-physics/neutrino-experiments-and-sources", "b": "07-nuclear-physics/nuclear-reactions-and-decays/fusion-reactions", "name": "Solar neutrinos measure pp-chain and CNO rates", "kind": "shared object", "summary": "Solar neutrino fluxes are predicted from fusion S-factors (pp, 7Be(p,gamma)8B, 3He+4He) and measured by Borexino, SNO and Super-K, including the first CNO neutrinos; they test solar fusion and oscillations together.", "map": "\\sigma(E)=\\frac{S(E)}{E}e^{-2\\pi\\eta};\\ \\Phi_{^8\\text{B}}\\propto S_{17}\\,T_c^{\\sim24}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2216", "a": "06-particle-physics/neutrino-physics/neutrino-experiments-and-sources", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "name": "Neutrino-nucleus cross sections and CEvNS", "kind": "shared object", "summary": "Accelerator oscillation measurements are limited by neutrino-nucleus interaction models (quasi-elastic, meson production, final-state interactions); coherent elastic scattering grows as N^2 through the nuclear weak charge.", "map": "\\frac{d\\sigma}{dT}\\simeq\\frac{G_F^2M}{4\\pi}Q_W^2\\left(1-\\frac{MT}{2E_\\nu^2}\\right)F^2(q),\\ Q_W=N-(1-4\\sin^2\\theta_W)Z", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2217", "a": "06-particle-physics/neutrino-physics/neutrino-mass-and-double-beta-decay", "b": "07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions", "name": "Tritium endpoint and double-beta decay", "kind": "shared object", "summary": "Absolute neutrino mass comes from the shape of the tritium beta spectrum near its endpoint (KATRIN), and Majorana nature from nuclear 0nubb decay; both are nuclear weak decays read as neutrino measurements.", "map": "\\frac{d\\Gamma}{dE}\\propto(E_0-E)\\sqrt{(E_0-E)^2-m_\\beta^2};\\ (T^{0\\nu}_{1/2})^{-1}=G^{0\\nu}|M^{0\\nu}|^2m_{\\beta\\beta}^2/m_e^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2218", "a": "06-particle-physics/neutrino-physics/neutrino-mass-and-double-beta-decay", "b": "07-nuclear-physics/nuclear-structure/ab-initio-nuclear-theory", "name": "Ab initio 0nubb matrix elements with uncertainties", "kind": "method transfer", "summary": "Turning a 0nubb half-life limit into m_bb needs |M^0nu|, which shell-model, QRPA and EDF calculations disagree on by 2-3x; ab initio methods with chiral EFT now give matrix elements with error bars, and two-body currents explain g_A quenching.", "map": "m_{\\beta\\beta}=m_e\\left[G^{0\\nu}|M^{0\\nu}|^2T^{0\\nu}_{1/2}\\right]^{-1/2}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2219", "a": "06-particle-physics/neutrino-physics/neutrino-oscillations", "b": "07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process", "name": "Neutrino flavor conversion sets Y_e in r-process sites", "kind": "mechanism", "summary": "In supernovae and merger remnants, nu_e and anti-nu_e captures on nucleons set the electron fraction Y_e of ejecta; collective and fast flavor conversions can shift Y_e and so the r-process yields.", "map": "\\nu_e+n\\to p+e^-,\\ \\bar\\nu_e+p\\to n+e^+\\ \\Rightarrow\\ Y_e;\\ H=H_{\\text{vac}}+\\sqrt2G_F(n_e+n_{\\nu\\nu})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2220", "a": "06-particle-physics/neutrino-physics/sterile-neutrinos-and-anomalies", "b": "07-nuclear-physics/applied-nuclear-physics/nuclear-data-and-isotope-production", "name": "Reactor anomaly traced to fission beta spectra", "kind": "shared object", "summary": "The reactor antineutrino anomaly came from converted fission beta spectra (Huber-Mueller); improved nuclear data and summation calculations removed much of it, and the 5 MeV bump is a nuclear-data feature, not oscillation.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2221", "a": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "b": "07-nuclear-physics/hadron-and-nucleon-structure/nucleon-spin-and-form-factors", "name": "Axial anomaly in the proton spin puzzle", "kind": "mechanism", "summary": "The flavor-singlet axial current is anomalous, so the quark-spin fraction Delta Sigma measured in polarized DIS mixes with gluon polarization; this anomaly is central to interpreting the EMC spin crisis.", "map": "\\partial_\\mu j_5^\\mu=\\frac{n_f\\alpha_s}{4\\pi}G\\tilde G\\ \\Rightarrow\\ a_0=\\Delta\\Sigma-n_f\\frac{\\alpha_s}{2\\pi}\\Delta G", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2222", "a": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "b": "07-nuclear-physics/hadron-and-nucleon-structure/nucleon-spin-and-form-factors", "name": "Neutron EDM as the observable of theta", "kind": "mechanism", "summary": "The theta term is a P- and T-odd topological term that induces a neutron electric dipole moment; the measured bound gives |theta| < 10^-10, the strong-CP problem the axion solves.", "map": "d_n\\approx(10^{-16}\\text{-}10^{-15})\\,\\bar\\theta\\ e\\,\\text{cm};\\ |d_n|<1.8\\times10^{-26}\\,e\\,\\text{cm}\\Rightarrow|\\bar\\theta|\\lesssim10^{-10}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2223", "a": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "b": "07-nuclear-physics/heavy-ion-physics/qcd-phase-diagram-and-critical-point", "name": "Topology and U(1)_A at the QCD transition", "kind": "mechanism", "summary": "Instanton-induced U(1)_A breaking controls the order of the chiral transition, the topological susceptibility sets the temperature-dependent axion mass, and sphaleron-driven chirality imbalance motivates chiral-magnetic-effect searches.", "map": "\\vec J=\\frac{e^2\\mu_5}{2\\pi^2}\\vec B\\ (\\text{CME});\\ \\chi_{\\text{top}}(T)=m_a^2(T)f_a^2", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2224", "a": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "b": "07-nuclear-physics/nuclear-structure", "name": "Baryons as Skyrmions", "kind": "mechanism", "summary": "In the large-N chiral Lagrangian, baryons are topological solitons whose winding number is baryon number (the Wess-Zumino-Witten term fixes their fermionic statistics); Skyrmion models describe nucleons and light nuclei.", "map": "B=\\frac{1}{24\\pi^2}\\int d^3x\\,\\epsilon^{ijk}\\mathrm{Tr}(U^\\dagger\\partial_iU\\,U^\\dagger\\partial_jU\\,U^\\dagger\\partial_kU)\\in\\mathbb Z", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2225", "a": "06-particle-physics/quantum-field-theory/conformal-field-theory", "b": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "name": "Conformal plasmas as QGP benchmarks", "kind": "analogy", "summary": "Strongly coupled conformal plasmas (N=4 SYM via holography) give eta/s=1/4pi, close to the QGP value; QCD's trace anomaly (epsilon-3P)/T^4 measures how far the real plasma is from conformal.", "map": "\\frac{\\eta}{s}=\\frac{\\hbar}{4\\pi k_B}\\ (\\text{CFT}_{\\text{hol}});\\ \\frac{\\varepsilon-3P}{T^4}=0\\ (\\text{CFT})\\ \\text{vs peak near }T_c\\ (\\text{QCD})", "breaks": "N=4 SYM is supersymmetric, conformal and large-N with no confinement, no chiral symmetry breaking and no running coupling; QCD is strongly non-conformal near T_c.", "confidence": "current research", "strength": 2}
{"id": "C2226", "a": "06-particle-physics/quantum-field-theory/effective-field-theory", "b": "07-nuclear-physics/nuclear-structure", "name": "EFT organizes the nuclear many-body problem", "kind": "method transfer", "summary": "Nuclear structure theory is now built from a hierarchy of EFTs (chiral, pionless, halo), each with power counting and quantified truncation errors, as in particle-physics EFT.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2227", "a": "06-particle-physics/quantum-field-theory/effective-field-theory", "b": "07-nuclear-physics/nuclear-structure/exotic-nuclei-and-drip-lines", "name": "Halo EFT and universality of weak binding", "kind": "method transfer", "summary": "Halo nuclei near the drip lines have a separation energy far below the core excitation scale, so a halo EFT with the core as a point particle applies, with universal (Efimov-like) features for two-neutron halos.", "map": "R_{\\text{halo}}\\sim\\frac{1}{\\sqrt{2\\mu S_n}}\\gg R_{\\text{core}};\\ \\text{expansion in }R_{\\text{core}}/R_{\\text{halo}}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2228", "a": "06-particle-physics/quantum-field-theory/effective-field-theory", "b": "07-nuclear-physics/nuclear-structure/nuclear-forces-and-chiral-eft", "name": "Chiral EFT as Weinberg's power counting for nuclei", "kind": "method transfer", "summary": "Weinberg's phenomenological-Lagrangian program (chiral perturbation theory) was carried into nuclear physics as chiral EFT, organizing nucleon-nucleon and three-nucleon forces in powers of Q/Lambda_chi.", "map": "\\mathcal L_{\\text{eff}}=\\sum_i\\frac{c_i}{\\Lambda^{d_i-4}}\\mathcal O_i\\ \\leftrightarrow\\ V=\\sum_\\nu(Q/\\Lambda_\\chi)^\\nu V^{(\\nu)},\\ \\Lambda_\\chi\\sim m_\\rho", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2229", "a": "06-particle-physics/quantum-field-theory/lattice-field-theory", "b": "07-nuclear-physics/hadron-and-nucleon-structure/nucleon-spin-and-form-factors", "name": "Lattice QCD for g_A, spin and gravitational form factors", "kind": "method transfer", "summary": "Lattice QCD computes the nucleon axial charge, quark and gluon spin and orbital contributions, and gravitational form factors (pressure and shear distributions) from first principles.", "map": "J_q=\\tfrac12[A_q(0)+B_q(0)];\\ g_A=1.27\\ (\\text{lattice and exp})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2230", "a": "06-particle-physics/quantum-field-theory/lattice-field-theory", "b": "07-nuclear-physics/hadron-and-nucleon-structure/parton-distribution-functions", "name": "Large-momentum effective theory puts PDFs on the lattice", "kind": "method transfer", "summary": "Light-cone PDFs cannot be computed in Euclidean time, but equal-time quasi-PDFs in a highly boosted nucleon can, and are matched to PDFs perturbatively (LaMET); lattice results now complement global fits.", "map": "\\tilde q(x,P_z)=\\int\\frac{dz}{4\\pi}e^{ixP_zz}\\langle P|\\bar\\psi(z)\\gamma^z W\\psi(0)|P\\rangle=C\\otimes q+\\mathcal O(\\Lambda^2/P_z^2)", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2231", "a": "06-particle-physics/quantum-field-theory/lattice-field-theory", "b": "07-nuclear-physics/heavy-ion-physics/qcd-phase-diagram-and-critical-point", "name": "Lattice QCD finds the crossover at T_c~156 MeV", "kind": "method transfer", "summary": "Euclidean lattice Monte Carlo establishes that the physical-mass QCD transition at mu_B=0 is a crossover and computes the equation of state and susceptibilities used to search for a critical point; the sign problem blocks large mu_B.", "map": "\\chi_n^B=\\frac{\\partial^n(P/T^4)}{\\partial(\\mu_B/T)^n}\\Big|_{\\mu_B=0}\\ (\\text{Taylor expansion on the lattice})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2232", "a": "06-particle-physics/quantum-field-theory/lattice-field-theory", "b": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "name": "Lattice equation of state drives QGP hydrodynamics", "kind": "method transfer", "summary": "Lattice QCD thermodynamics provides the QGP equation of state, speed of sound and trace anomaly used as input to relativistic hydrodynamic simulations of heavy-ion collisions.", "map": "\\frac{\\varepsilon-3P}{T^4}=T\\frac{\\partial}{\\partial T}\\frac{P}{T^4};\\ c_s^2=\\frac{dP}{d\\varepsilon}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2233", "a": "06-particle-physics/quantum-field-theory/lattice-field-theory", "b": "07-nuclear-physics/nuclear-structure/ab-initio-nuclear-theory", "name": "Nuclear lattice EFT reuses lattice Monte Carlo", "kind": "method transfer", "summary": "Nuclear lattice EFT discretizes chiral-EFT nucleons on a Euclidean space-time lattice and samples auxiliary fields by Monte Carlo, inheriting lattice-QCD algorithms and the fermion sign problem.", "map": "Z=\\mathrm{Tr}\\,e^{-\\beta H}=\\int\\mathcal D\\sigma\\,\\det M[\\sigma]\\,e^{-S[\\sigma]}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2234", "a": "06-particle-physics/quantum-field-theory/lattice-field-theory", "b": "07-nuclear-physics/nuclear-structure/nuclear-forces-and-chiral-eft", "name": "Lattice QCD computes nucleon-nucleon interactions", "kind": "method transfer", "summary": "Lattice QCD extracts two-baryon scattering from finite-volume energy levels (Luscher's method) and fixes chiral-EFT low-energy constants, connecting nuclear forces to QCD.", "map": "p\\cot\\delta_0(p)=\\frac{1}{\\pi L}S\\!\\left(\\left(\\tfrac{pL}{2\\pi}\\right)^2\\right)\\ (\\text{Luscher})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2235", "a": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "b": "07-nuclear-physics/nuclear-structure/ab-initio-nuclear-theory", "name": "SRG/IMSRG as Wilsonian RG for nuclei", "kind": "method transfer", "summary": "Similarity renormalization group evolution decouples high- and low-momentum modes of nuclear Hamiltonians, the nuclear realization of Wilson's integrating-out; induced many-body forces play the role of generated irrelevant operators.", "map": "\\frac{dH_s}{ds}=[\\eta_s,H_s]\\ \\leftrightarrow\\ \\mu\\frac{dg_i}{d\\mu}=\\beta_i(g)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2236", "a": "06-particle-physics/standard-model/cp-violation", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Octupole-deformed nuclei amplify T violation", "kind": "mechanism", "summary": "Nuclear Schiff moments induced by CP-odd nucleon interactions are enhanced by orders of magnitude in octupole-deformed nuclei with parity doublets (225Ra, 227Ac), making atomic EDM searches sensitive probes of hadronic CP violation.", "map": "S\\propto\\frac{\\langle\\Psi_0|\\hat S|\\bar\\Psi_0\\rangle\\langle\\bar\\Psi_0|V_{PT}|\\Psi_0\\rangle}{E_+-E_-},\\ \\Delta E_\\pm\\ \\text{small (parity doublet)}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2237", "a": "06-particle-physics/standard-model/electroweak-theory", "b": "07-nuclear-physics/heavy-ion-physics/qcd-phase-diagram-and-critical-point", "name": "Both Standard Model transitions are crossovers", "kind": "mechanism", "summary": "Lattice studies show that at physical masses the electroweak transition (m_h=125 GeV) and the QCD transition are both smooth crossovers, which removes the SM's own departure from equilibrium for baryogenesis and for primordial relics.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2238", "a": "06-particle-physics/standard-model/electroweak-theory", "b": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "name": "Z-boson exchange measures the neutron skin", "kind": "method transfer", "summary": "Parity-violating electron scattering couples to the weak charge, which is carried mostly by neutrons (Q_W^p ~ 1-4 sin^2 theta_W ~ 0.07); PREX-II's 208Pb neutron skin constrains the symmetry-energy slope L and neutron-star radii.", "map": "A_{PV}\\approx\\frac{G_FQ^2}{4\\sqrt2\\pi\\alpha}\\frac{Q_W F_W(Q^2)}{ZF_{ch}(Q^2)};\\ R_n-R_p\\leftrightarrow L", "breaks": "", "confidence": "current research", "strength": 2}