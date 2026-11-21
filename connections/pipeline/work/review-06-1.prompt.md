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

# Packet 06-1 (100 records)

{"id": "C0247", "a": "00-foundations/computational-physics", "b": "06-particle-physics/quantum-field-theory/lattice-field-theory", "name": "Lattice QCD as a computational-physics workload", "kind": "method transfer", "summary": "Lattice field theory turns the Euclidean path integral into a very high-dimensional integral attacked with the whole computational toolkit: Markov-chain Monte Carlo, Krylov and multigrid solvers for the Dirac operator, and now ML samplers and tensor networks. Lattice QCD has in turn driven dedicated supercomputer design (APE, QCDOC).", "map": "Z=\\int\\mathcal{D}U\\,\\det D[U]\\,e^{-S_g[U]}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0248", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "06-particle-physics/collider-and-experimental-particle-physics/machine-learning-in-hep", "name": "Neural tools shared by physics and HEP", "kind": "method transfer", "summary": "The same neural tools (classifiers, generative surrogates, normalizing flows, graph networks, anomaly detectors) serve physics in general and HEP in particular. In HEP they tag jets, emulate calorimeter showers, run in triggers and power simulation-based inference, and HEP was an early adopter and a main source of benchmark datasets.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0249", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "06-particle-physics/quantum-field-theory/lattice-field-theory", "name": "Hybrid Monte Carlo: molecular dynamics in fictitious time", "kind": "method transfer", "summary": "HMC samples lattice gauge fields with dynamical fermions by adding conjugate momenta, integrating Hamilton's equations with a reversible, volume-preserving leapfrog or Omelyan integrator, and removing the integration error with a Metropolis step. It was invented for lattice QCD and later adopted in Bayesian statistics (NUTS in Stan).", "map": "H=\\tfrac12\\sum\\pi^2+S[\\phi],\\ P_{\\rm acc}=\\min(1,e^{-\\Delta H})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0250", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "06-particle-physics/collider-and-experimental-particle-physics/monte-carlo-event-generators", "name": "Event generators as Monte Carlo integrators", "kind": "method transfer", "summary": "Event generators do importance-sampled (VEGAS-type adaptive) phase-space integration of factorized cross sections, hit-or-miss unweighting into events, and parton showers sampled with the veto algorithm. The shower samples the Sudakov no-emission probability with the same survival-probability logic used to sample radioactive decay times.", "map": "\\Delta(t_0,t)=\\exp\\left[-\\int_t^{t_0}\\frac{dt'}{t'}\\int dz\\,\\frac{\\alpha_s}{2\\pi}P(z)\\right]", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0251", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "06-particle-physics/quantum-field-theory/lattice-field-theory", "name": "Euclidean action as a Boltzmann weight", "kind": "identity", "summary": "After Wick rotation, e^{iS} becomes e^{-S_E}, so lattice QFT is a statistical-mechanics problem sampled by Markov-chain Monte Carlo (heat bath, HMC). It inherits that field's problems: autocorrelation, critical slowing down toward the continuum limit, and the sign problem when the weight is not positive.", "map": "\\langle O\\rangle=\\frac1Z\\int\\mathcal DU\\,O[U]\\,e^{-S_E[U]}\\approx\\frac1N\\sum_{i=1}^NO[U_i]", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0252", "a": "00-foundations/computational-physics/tensor-network-methods", "b": "06-particle-physics/quantum-field-theory/lattice-field-theory", "name": "Tensor networks for lattice gauge theories", "kind": "method transfer", "summary": "In the Hamiltonian formulation, MPS and DMRG simulate 1+1D lattice gauge theories such as the Schwinger model without importance sampling, so they avoid the sign problem at finite density, with a θ term and in real time. Gauss's law can be built into gauge-invariant tensors, and these results benchmark quantum simulators of gauge theories.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0253", "a": "00-foundations/history-and-philosophy-of-physics/history-of-physics", "b": "06-particle-physics", "name": "Particle physics as the archetype of big science", "kind": "historical", "summary": "The path from cosmic-ray and accelerator discoveries to the Standard Model is a central case study in the history of physics. The field also defined 'big science': Lawrence's cyclotron laboratory, CERN (1954) as a model of international collaboration, and LHC collaborations with thousands of authors.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0254", "a": "00-foundations/history-and-philosophy-of-physics/philosophy-of-physics", "b": "06-particle-physics/beyond-the-standard-model/extra-dimensions-and-hierarchy-problem", "name": "Naturalness as an argument form", "kind": "shared object", "summary": "The hierarchy problem rests on naturalness, a fine-tuning argument that philosophy of physics studies as a heuristic. Its past success (the charm-quark mass estimated from K⁰ mixing) and the LHC's null searches for natural new physics have made its epistemic status an open debate.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0255", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2", "name": "Dispersive hadronic vacuum polarization for muon g−2", "kind": "method transfer", "summary": "Analyticity and the optical theorem turn the measured e⁺e⁻→hadrons cross section into the leading hadronic contribution to the muon g−2 through a Kramers–Kronig-type integral. Tensions among the e⁺e⁻ data sets (CMD-3 versus earlier experiments) and with lattice QCD are why this term decides the Standard Model comparison.", "map": "a_\\mu^{\\rm HVP,LO}=\\frac{\\alpha^2}{3\\pi^2}\\int_{s_{\\rm th}}^{\\infty}\\frac{ds}{s}K(s)R(s)", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0256", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "06-particle-physics/quantum-field-theory/conformal-field-theory", "name": "Holomorphy and the Virasoro algebra in 2D CFT", "kind": "identity", "summary": "In two dimensions the conformal maps are exactly the holomorphic functions, so the stress tensor splits into T(z) and T̄(z̄). Radial quantization turns charges into contour integrals, Ward identities and operator-product expansions follow from the residue theorem, and the Virasoro generators are Laurent coefficients.", "map": "L_n=\\oint\\frac{dz}{2\\pi i}z^{n+1}T(z),\\ [L_m,L_n]=(m-n)L_{m+n}+\\frac{c}{12}m(m^2-1)\\delta_{m+n,0}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0257", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "06-particle-physics/quantum-field-theory/feynman-diagrams-and-scattering-amplitudes", "name": "S-matrix analyticity, dispersion relations and cuts", "kind": "method transfer", "summary": "Causality makes scattering amplitudes analytic in the energy variables, so they obey dispersion relations, the relativistic version of Kramers–Kronig. The optical theorem and Cutkosky rules give the discontinuities across branch cuts, and the modern unitarity method rebuilds loop amplitudes from their cuts.", "map": "\\mathcal M(s)=\\frac1\\pi\\int_{s_0}^\\infty ds'\\frac{\\mathrm{Im}\\,\\mathcal M(s')}{s'-s-i\\epsilon},\\ \\mathrm{Im}\\,\\mathcal M(s,0)=2E_{\\rm cm}p_{\\rm cm}\\sigma_{\\rm tot}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0258", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "06-particle-physics/quantum-field-theory/feynman-diagrams-and-scattering-amplitudes", "name": "The Feynman propagator is a Green's function", "kind": "identity", "summary": "The propagator is the Green's function of the Klein–Gordon (or Dirac) operator, with the iε prescription choosing time-ordered boundary conditions, so the Feynman-diagram expansion is a Born series in Green's functions. Differential equations in the kinematic variables are also a main tool for evaluating loop integrals.", "map": "(\\Box+m^2)D_F(x-y)=-i\\delta^4(x-y),\\ \\tilde D_F(p)=\\frac{i}{p^2-m^2+i\\epsilon}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0259", "a": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "b": "06-particle-physics/neutrino-physics/neutrino-oscillations", "name": "Neutrino mixing as a unitary basis change", "kind": "identity", "summary": "Flavour and mass eigenstates are related by the unitary PMNS matrix, so oscillation is the time evolution of a superposition of energy eigenstates. The two-flavour formula is the two-level Rabi formula, and the MSW effect is adiabatic passage through an avoided crossing of the matter Hamiltonian's eigenvalues.", "map": "|\\nu_\\alpha\\rangle=\\sum_iU_{\\alpha i}^*|\\nu_i\\rangle,\\ P_{\\alpha\\to\\beta}=\\sin^22\\theta\\,\\sin^2\\frac{\\Delta m^2L}{4E}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0260", "a": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "b": "06-particle-physics/standard-model/flavor-physics-and-ckm", "name": "CKM matrix from bi-unitary diagonalization of Yukawas", "kind": "identity", "summary": "Quark mass matrices are diagonalized by separate left and right unitary rotations (a singular-value decomposition), and the CKM matrix is the mismatch between the up- and down-type left rotations. Parameter counting leaves (n−1)(n−2)/2 CP phases, one for three generations, and the Jarlskog invariant measures it independently of basis.", "map": "M_q=U_L^q\\,\\mathrm{diag}(m)\\,U_R^{q\\dagger},\\ V=U_L^{u\\dagger}U_L^d,\\ N_\\delta=\\frac{(n-1)(n-2)}{2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0261", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "name": "Instanton number as a Chern class; index theorem", "kind": "identity", "summary": "Instantons are classified by the second Chern (Pontryagin) number of the gauge bundle, and the θ term integrates that characteristic class. The Atiyah–Singer index theorem ties it to the Dirac operator's zero modes, which is the topological content of the axial anomaly.", "map": "Q=\\frac{1}{8\\pi^2}\\int\\mathrm{tr}\\,F\\wedge F\\in\\mathbb Z,\\ n_+-n_-=Q", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0262", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "name": "Gauge fields as connections, field strength as curvature", "kind": "identity", "summary": "A gauge potential is a connection on a principal bundle and the field strength is its curvature, the same structures as the spin connection and Riemann tensor of general relativity. Wilson loops are holonomies, and a Bianchi identity holds in both.", "map": "D_\\mu=\\partial_\\mu-igA_\\mu,\\ F=dA-ig\\,A\\wedge A\\ \\leftrightarrow\\ R=d\\omega+\\omega\\wedge\\omega", "breaks": "The gravitational connection is soldered to the tangent bundle and fixed by the metric; internal gauge connections live on an abstract bundle with no metric to determine them.", "confidence": "established", "strength": 3}
{"id": "C0263", "a": "00-foundations/measurement-and-data-analysis", "b": "06-particle-physics/collider-and-experimental-particle-physics", "name": "Collider physics as measurement at scale", "kind": "method transfer", "summary": "Collider experiments use the full measurement chain: calibration, unfolding of detector response, systematic uncertainties as nuisance parameters, and blind analyses. HEP also produced much of the statistics toolkit physicists now share (Feldman–Cousins intervals, CLs, asymptotic profile-likelihood formulae).", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0264", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "name": "Axion haloscopes at the quantum noise limit", "kind": "method transfer", "summary": "Haloscopes such as ADMX convert dark-matter axions into microwave photons in a magnetized cavity, and the ~10⁻²² W signal makes the scan rate scale as 1/T_sys². Josephson parametric amplifiers at the standard quantum limit, squeezed states (HAYSTAC) and qubit-based photon counting are the enabling detector physics.", "map": "P_{a\\to\\gamma}\\propto g_{a\\gamma\\gamma}^2\\frac{\\rho_a}{m_a}B^2VC\\,Q,\\ k_BT_{\\rm SQL}=\\hbar\\omega", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0265", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "06-particle-physics/collider-and-experimental-particle-physics", "name": "Calibration chains and resolution in collider experiments", "kind": "method transfer", "summary": "Collider experiments apply instrumentation principles at scale: test-beam and in-situ calibration with Z→ee and J/ψ resonances, luminosity from van der Meer beam-separation scans, and electronics noise and pile-up as limits on energy resolution.", "map": "\\frac{\\sigma_E}{E}=\\frac{a}{\\sqrt E}\\oplus\\frac{b}{E}\\oplus c", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0266", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers", "name": "Shared signal chain: sensors, preamps and noise", "kind": "shared object", "summary": "In a particle detector, ionization or light becomes charge, which charge-sensitive preamplifiers amplify and shape, with thermal and shot noise setting the equivalent noise charge. Photomultipliers, SiPMs and silicon sensors are common to both nodes, and triggers are real-time filters working under bandwidth limits.", "map": "\\langle V_n^2\\rangle=4k_BTR\\,\\Delta f,\\ \\langle I_n^2\\rangle=2qI\\,\\Delta f", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0267", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "06-particle-physics/collider-and-experimental-particle-physics", "name": "Profile likelihood, CLs and the 5σ discovery rule", "kind": "method transfer", "summary": "LHC searches are hypothesis tests: profile-likelihood ratios with systematics as nuisance parameters, Wilks/Wald asymptotics giving Z = √q₀, CLs for exclusions, and look-elsewhere corrections, as used in the 2012 Higgs discovery.", "map": "q_0=-2\\ln\\frac{L(0,\\hat{\\hat\\theta})}{L(\\hat\\mu,\\hat\\theta)},\\ Z=\\sqrt{q_0}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0268", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "06-particle-physics/collider-and-experimental-particle-physics/machine-learning-in-hep", "name": "Simulation-based inference and the likelihood-ratio trick", "kind": "method transfer", "summary": "When a simulator yields samples but no tractable likelihood, a classifier trained to separate θ₀ samples from θ₁ samples estimates the likelihood ratio, which by Neyman–Pearson is the optimal test statistic. Neural likelihood-ratio and posterior estimation now replace binned histogram fits in some ATLAS measurements.", "map": "s(x)\\to\\frac{p(x|\\theta_1)}{p(x|\\theta_0)+p(x|\\theta_1)}\\Rightarrow r(x)=\\frac{s(x)}{1-s(x)}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0269", "a": "00-foundations/measurement-and-data-analysis/uncertainty-and-error-propagation", "b": "06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2", "name": "Judging anomalies: systematics and correlated errors", "kind": "method transfer", "summary": "Whether an anomaly is real depends on its uncertainty budget. The muon g−2 comparison turned on the hadronic-vacuum-polarization error (mutually inconsistent e⁺e⁻ data versus lattice QCD, whose 2025 consensus value agrees with experiment), and the CDF W-mass outlier is a case study in combining correlated systematics across experiments.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0270", "a": "00-foundations/symmetry-and-group-theory", "b": "06-particle-physics/standard-model", "name": "The Standard Model as representation theory", "kind": "identity", "summary": "The Standard Model is defined by its gauge group SU(3)×SU(2)×U(1) and by assigning each field to an irreducible representation, while Wigner's unitary Poincaré irreps label particles by mass and spin. Charges, multiplets and allowed couplings follow from group theory.", "map": "G_{\\rm SM}=SU(3)_c\\times SU(2)_L\\times U(1)_Y,\\ Q=T_3+Y", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0271", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "name": "Strong CP problem and the Peccei–Quinn axion", "kind": "mechanism", "summary": "The QCD θ term is P- and T-odd and would give the neutron an electric dipole moment; the bound |d_n| < 1.8×10⁻²⁶ e cm forces |θ̄| ≲ 10⁻¹⁰. The Peccei–Quinn solution makes θ̄ dynamical: the axion, a pseudo-Goldstone boson, relaxes it to zero.", "map": "\\mathcal L_\\theta=\\bar\\theta\\frac{g_s^2}{32\\pi^2}G\\tilde G,\\ d_n\\sim10^{-16}\\bar\\theta\\,e\\,\\mathrm{cm},\\ m_a\\approx5.7\\,\\mu\\mathrm{eV}\\,\\frac{10^{12}\\,\\mathrm{GeV}}{f_a}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0272", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "06-particle-physics/standard-model/cp-violation", "name": "CP violation and the CPT theorem", "kind": "identity", "summary": "CP violation in kaons and B mesons is the experimental side of discrete-symmetry theory, and by the CPT theorem it implies T violation, since observed directly in both systems. With three generations the CKM matrix carries exactly one physical CP phase.", "map": "J=\\mathrm{Im}(V_{us}V_{cb}V_{ub}^*V_{cs}^*)\\approx3\\times10^{-5}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0273", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "06-particle-physics/standard-model/electroweak-theory", "name": "Parity violation built into chiral SU(2)_L", "kind": "historical", "summary": "Lee and Yang's 1956 proposal and Wu's 1957 cobalt-60 experiment showed that the weak interaction violates parity maximally. Electroweak theory encodes this by putting only left-handed fermions in SU(2)_L doublets (V−A currents), so the gauge representations themselves break P and C, while CP survives up to the CKM phase.", "map": "J^\\mu_W=\\bar\\nu\\gamma^\\mu\\frac{1-\\gamma^5}{2}e,\\ \\psi_L\\in\\mathbf2,\\ \\psi_R\\in\\mathbf1", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0274", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "06-particle-physics/beyond-the-standard-model/grand-unification-and-proton-decay", "name": "SU(5) and SO(10) embeddings of the Standard Model", "kind": "identity", "summary": "Grand unification is a group-embedding problem: SU(5) ⊃ SU(3)×SU(2)×U(1) fits one generation into 5̄ ⊕ 10, and SO(10) fits it into a single 16 that includes ν_R. The embedding quantizes hypercharge and fixes sin²θ_W = 3/8 at the unification scale.", "map": "\\bar5\\oplus10\\oplus1=16_{SO(10)},\\ \\sin^2\\theta_W(M_{\\rm GUT})=3/8", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0275", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "06-particle-physics/beyond-the-standard-model/supersymmetry", "name": "Graded Lie algebras evade Coleman–Mandula", "kind": "identity", "summary": "Coleman–Mandula rules out any Lie-group symmetry of the S-matrix that mixes spacetime and internal symmetries non-trivially. Haag–Łopuszański–Sohnius showed that the only loophole is a graded algebra with fermionic generators, which is supersymmetry, whose anticommutator closes on the momentum.", "map": "\\{Q_\\alpha,\\bar Q_{\\dot\\beta}\\}=2\\sigma^\\mu_{\\alpha\\dot\\beta}P_\\mu", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0276", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "06-particle-physics/standard-model/hadron-spectroscopy-and-exotics", "name": "Flavour SU(3) multiplets and colour singlets", "kind": "identity", "summary": "The eightfold way sorts hadrons into flavour-SU(3) octets and decuplets, and the Gell-Mann–Okubo mass formula predicted the Ω⁻. The quark model reads hadrons as colour singlets in tensor products of 3 and 3̄, and the same products list the allowed tetraquark and pentaquark structures.", "map": "3\\otimes\\bar3=8\\oplus1,\\ 3\\otimes3\\otimes3=10\\oplus8\\oplus8\\oplus1", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0277", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "06-particle-physics/standard-model/quantum-chromodynamics", "name": "SU(3) colour Casimirs set QCD dynamics", "kind": "identity", "summary": "Quarks sit in the fundamental and gluons in the adjoint of SU(3), and the group invariants C_F = 4/3, C_A = 3 and T_F = 1/2 fix the β-function, the splitting functions and the colour factors. Gluon self-coupling through the non-abelian structure constants gives asymptotic freedom, and large-N_c expansions treat N as a parameter.", "map": "\\beta_0=\\frac{11}{3}C_A-\\frac43T_Fn_f=11-\\frac23n_f,\\ C_F=\\frac{N^2-1}{2N}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0278", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "name": "Anomalies: Noether currents broken by quantization", "kind": "mechanism", "summary": "A classically conserved Noether current can gain a nonzero divergence from the path-integral measure. The axial anomaly explains π⁰→γγ, and its coefficient is topological: exact at one loop (Adler–Bardeen) and protected from further corrections.", "map": "\\partial_\\mu j_5^\\mu=\\frac{e^2}{16\\pi^2}\\epsilon^{\\mu\\nu\\rho\\sigma}F_{\\mu\\nu}F_{\\rho\\sigma}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0279", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "name": "Gauging a Noether symmetry; Ward identities", "kind": "mechanism", "summary": "Making a global symmetry local forces in a gauge field that couples to the Noether current, and Noether's second theorem says local symmetries give identities rather than new charges. In quantum theory these become the Ward–Takahashi and Slavnov–Taylor identities, which protect charge universality and renormalizability.", "map": "\\mathcal L\\supset-eA_\\mu j^\\mu,\\ \\partial_\\mu j^\\mu=0\\Rightarrow k_\\mu\\mathcal M^\\mu(k)=0,\\ Z_1=Z_2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0280", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "06-particle-physics/standard-model/higgs-boson", "name": "Higgs boson as the amplitude mode of electroweak breaking", "kind": "mechanism", "summary": "A Mexican-hat potential gives the Higgs doublet a vacuum value v = 246 GeV that breaks SU(2)×U(1) to U(1)_em, and three would-be Goldstones become the longitudinal W and Z (Higgs–Anderson mechanism). The leftover custodial SU(2) gives ρ = 1 at tree level, and the Higgs boson is the radial (amplitude) mode.", "map": "V=-\\mu^2|\\phi|^2+\\lambda|\\phi|^4,\\ v=\\mu/\\sqrt{\\lambda}=(\\sqrt2G_F)^{-1/2},\\ m_H=\\sqrt{2\\lambda}\\,v", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0281", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "06-particle-physics/standard-model/quantum-chromodynamics", "name": "Chiral symmetry breaking: pions as pseudo-Goldstones", "kind": "mechanism", "summary": "The quark condensate breaks SU(2)_L×SU(2)_R to SU(2)_V, so pions are pseudo-Goldstone bosons, light because quark masses break the symmetry explicitly. This is Nambu's superconductivity analogy carried into hadron physics, and chiral perturbation theory is its low-energy effective theory.", "map": "\\langle\\bar qq\\rangle\\neq0,\\ m_\\pi^2f_\\pi^2=-(m_u+m_d)\\langle\\bar qq\\rangle", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0282", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "name": "Anomalous dimensions and dimensional transmutation", "kind": "mechanism", "summary": "Quantum loops break naive dimensional analysis: because a renormalization scale μ enters, correlators scale with the engineering dimension plus an anomalous dimension, a case of Barenblatt's incomplete similarity. Classically scale-free QCD likewise generates Λ_QCD, a few hundred MeV, from a dimensionless coupling.", "map": "G(\\lambda x)=\\lambda^{-2(d_0+\\gamma)}G(x),\\ \\Lambda=\\mu\\exp\\left[-\\frac{2\\pi}{\\beta_0\\alpha_s(\\mu)}\\right]", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0283", "a": "00-foundations/units-and-constants/fundamental-constants", "b": "06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2", "name": "Electron g−2, the fine-structure constant and muon g−2", "kind": "shared object", "summary": "With five-loop QED, the electron g−2 gives α to sub-ppb precision, but the two atom-recoil values of α (Cs 2018, Rb 2020) disagree by more than 5σ, which limits that test of QED. The muon g−2 then tests the whole Standard Model, hadronic loops included.", "map": "a_e=\\frac{\\alpha}{2\\pi}-0.328\\left(\\frac{\\alpha}{\\pi}\\right)^2+\\dots", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0284", "a": "00-foundations/units-and-constants/fundamental-constants", "b": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "name": "The fine-structure constant runs", "kind": "identity", "summary": "CODATA's α⁻¹ = 137.035999177 is the Thomson-limit value of a running coupling: vacuum polarization raises α to about 1/128.9 at the Z mass, and the hadronic part of that running comes from a dispersion integral over e⁺e⁻ data. A 'constant' of this kind is a renormalized coupling quoted at a stated scale.", "map": "\\alpha(Q^2)=\\frac{\\alpha(0)}{1-\\Delta\\alpha(Q^2)},\\ \\alpha^{-1}(0)=137.035999177,\\ \\alpha^{-1}(m_Z^2)\\approx128.9", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0285", "a": "00-foundations/units-and-constants/natural-units-and-planck-scale", "b": "06-particle-physics", "name": "Natural units and mass-dimension power counting", "kind": "method transfer", "summary": "With ħ = c = 1, particle physics measures everything in powers of energy and converts back through ħc. The mass dimension of fields and couplings then decides renormalizability, and a coupling of negative dimension, such as G_F = 1.1663787×10⁻⁵ GeV⁻², signals a heavier scale.", "map": "\\hbar c=197.327\\,\\mathrm{MeV\\,fm},\\ (\\hbar c)^2=0.3894\\,\\mathrm{GeV^2\\,mb},\\ [\\mathcal L]=4", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0286", "a": "00-foundations/units-and-constants/natural-units-and-planck-scale", "b": "06-particle-physics/beyond-the-standard-model/extra-dimensions-and-hierarchy-problem", "name": "Planck scale vs weak scale: the hierarchy", "kind": "shared object", "summary": "Natural units turn the hierarchy problem into a ratio of scales, M_Pl = √(ħc/G) ≈ 1.22×10¹⁹ GeV against v = 246 GeV. Large extra dimensions (ADD) lower the fundamental gravity scale to the TeV range by diluting gravity over a volume, while a warped extra dimension (RS) produces the ratio as an exponential.", "map": "M_{\\rm Pl}^2\\sim M_*^{n+2}R^n,\\ m_{\\rm weak}\\sim e^{-k\\pi r_c}M_{\\rm Pl}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0667", "a": "01-classical-mechanics/analytical-mechanics/canonical-transformations-and-hamilton-jacobi", "b": "06-particle-physics/quantum-field-theory/feynman-diagrams-and-scattering-amplitudes", "name": "Eikonal phase as Hamilton's action; orbits from amplitudes", "kind": "method transfer", "summary": "At large impact parameter the scattering amplitude exponentiates into an eikonal phase equal to the classical action, and the deflection angle is its b-derivative, as in Hamilton–Jacobi theory. Modern amplitude methods use this to compute classical two-body dynamics (post-Minkowskian scattering), with the radial action mapping scattering angles onto bound-orbit precession.", "map": "\\mathcal A\\sim\\int d^2b\\,e^{-i\\mathbf q\\cdot\\mathbf b/\\hbar}e^{i\\chi(b)},\\quad \\chi\\simeq S_{\\rm cl}/\\hbar,\\quad \\theta\\simeq-\\frac{\\hbar}{p}\\frac{\\partial\\chi}{\\partial b}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0668", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc", "name": "Liouville's theorem, emittance and beam cooling", "kind": "method transfer", "summary": "Beam optics is Hamiltonian, so phase-space density is conserved and the emittance (phase-space area) is an invariant that sets luminosity, and long-term tracking uses symplectic maps. Lowering emittance takes non-Hamiltonian tricks such as stochastic cooling, which was essential for the SppS W/Z discovery, or electron and ionization cooling.", "map": "\\epsilon=\\frac{1}{\\pi}\\oint p\\,dq\\ \\text{(invariant)},\\quad \\mathcal L=\\frac{N_b^2 n_b f\\gamma}{4\\pi\\epsilon_n\\beta^*}F", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0669", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "06-particle-physics/quantum-field-theory/canonical-and-path-integral-quantization", "name": "Poisson brackets become commutators", "kind": "identity", "summary": "Dirac's rule replaces Poisson brackets by commutators divided by iħ, which turns Hamilton's equations into Heisenberg's. Canonical transformations become unitary ones, and the phase-space generators of symmetries become charge operators; for fields the equal-time bracket of φ and π becomes the canonical commutator.", "map": "\\{A,B\\}\\to\\frac{1}{i\\hbar}[\\hat A,\\hat B],\\quad \\{\\phi(\\mathbf x),\\pi(\\mathbf y)\\}=\\delta^3(\\mathbf x-\\mathbf y)\\to[\\hat\\phi,\\hat\\pi]=i\\hbar\\,\\delta^3", "breaks": "The map is not a homomorphism on all observables. Operator-ordering ambiguities (Groenewold–van Hove theorem) mean it holds exactly only on a restricted algebra, such as polynomials of degree two or less.", "confidence": "established", "strength": 3}
{"id": "C0670", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "name": "Dirac constraints and gauge redundancy", "kind": "method transfer", "summary": "Dirac's theory of constrained Hamiltonian systems is the canonical structure of gauge theory. A_0 acts as a Lagrange multiplier, and Gauss's law is a first-class constraint that generates gauge transformations, so quantization needs either gauge fixing with Dirac brackets or BRST cohomology.", "map": "\\pi^0\\approx0,\\quad G^a=D_i\\pi^{ia}\\approx0,\\quad \\{G^a,G^b\\}=g f^{abc}G^c\\,\\delta^3", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0671", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "06-particle-physics/quantum-field-theory/lattice-field-theory", "name": "Hybrid Monte Carlo: fictitious Hamiltonian dynamics", "kind": "method transfer", "summary": "Lattice QCD with dynamical fermions samples gauge fields by adding fictitious conjugate momenta and integrating Hamilton's equations with a reversible, symplectic leapfrog integrator. Liouville's theorem and reversibility make the Metropolis accept/reject step exact; the method was invented for lattice QCD and later spread into statistics as HMC.", "map": "\\mathcal H=\\tfrac12\\sum\\pi^2+S_E[U],\\quad P_{\\rm acc}=\\min\\left(1,e^{-\\Delta\\mathcal H}\\right)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0672", "a": "01-classical-mechanics/analytical-mechanics/lagrangian-mechanics", "b": "06-particle-physics/quantum-field-theory/canonical-and-path-integral-quantization", "name": "Lagrangian field theory as the input to quantization", "kind": "identity", "summary": "QFT starts from the same Euler–Lagrange machinery with a Lagrangian density: generalized coordinates become field values at each point, their conjugate momenta are promoted to canonical commutators, and cyclic coordinates become conserved charges.", "map": "q_k(t)\\to\\phi(\\mathbf x,t),\\ L\\to\\int d^3x\\,\\mathcal L(\\phi,\\partial_\\mu\\phi),\\ p_k\\to\\pi=\\partial\\mathcal L/\\partial(\\partial_t\\phi)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0673", "a": "01-classical-mechanics/analytical-mechanics/lagrangian-mechanics", "b": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "name": "Minimal coupling and classical color (Wong) dynamics", "kind": "mechanism", "summary": "Under a gauge transformation the velocity-dependent Lagrangian L=½mv²−qφ+qv·A changes only by a total time derivative, which is the classical root of minimal coupling. Making q a color vector that precesses in the field gives Wong's equations, the classical mechanics of a Yang–Mills charge used in transport models of the quark–gluon plasma.", "map": "L\\to L+q\\,\\dot\\chi;\\quad \\frac{dQ^a}{d\\tau}=-g f^{abc}\\frac{dx^\\mu}{d\\tau}A^b_\\mu Q^c", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0674", "a": "01-classical-mechanics/analytical-mechanics/variational-principles", "b": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "name": "Instantons as least-action paths in the inverted potential", "kind": "method transfer", "summary": "Tunneling amplitudes are dominated by stationary points of the Euclidean action, which are classical trajectories in imaginary time, i.e. Newtonian motion in the inverted potential −V. The double-well instanton, Coleman's bounce for false-vacuum decay, and the Yang–Mills instantons that make θ physical are all built this way.", "map": "\\tau=it:\\ m\\frac{d^2x}{d\\tau^2}=+V'(x),\\quad \\Gamma\\propto e^{-S_E/\\hbar}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0675", "a": "01-classical-mechanics/analytical-mechanics/variational-principles", "b": "06-particle-physics/quantum-field-theory/canonical-and-path-integral-quantization", "name": "Stationary phase of the path integral is least action", "kind": "identity", "summary": "The path integral weights every history by e^{iS/ħ}, and as ħ→0 stationary phase selects δS=0, which recovers Hamilton's principle. The phase of the semiclassical propagator is Hamilton's principal function (Van Vleck–Gutzwiller), so the classical action carries over unchanged into QFT.", "map": "\\int\\mathcal D\\phi\\,e^{iS[\\phi]/\\hbar}\\ \\xrightarrow{\\hbar\\to0}\\ \\delta S=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0676", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "06-particle-physics/standard-model/quantum-chromodynamics", "name": "Quark–gluon plasma as a near-perfect viscous fluid", "kind": "method transfer", "summary": "Deconfined QCD matter in heavy-ion collisions flows as an almost ideal relativistic fluid, and viscous hydrodynamics (relativistic Navier–Stokes/Israel–Stewart) turns the initial spatial anisotropy into elliptic flow. Fits require η/s close to the holographic value 1/4π, and Λ polarization shows a vorticity of ~10²² s⁻¹, the most vortical fluid known.", "map": "\\partial_\\mu T^{\\mu\\nu}=0,\\quad T^{\\mu\\nu}=(\\varepsilon+P)u^\\mu u^\\nu-Pg^{\\mu\\nu}+\\pi^{\\mu\\nu},\\quad \\eta/s\\approx\\frac{\\hbar}{4\\pi k_B}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0677", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "06-particle-physics/collider-and-experimental-particle-physics/jets-and-qcd-phenomenology", "name": "QCD parton cascades and turbulent energy cascades", "kind": "analogy", "summary": "A jet's parton shower is a self-similar branching cascade that carries energy from the hard scale to soft scales, like a Richardson cascade. For medium-induced gluon branching the analogy becomes quantitative: democratic branching sets up a scale-independent, Kolmogorov–Zakharov-like flux of energy to soft gluons (Blaizot, Iancu & Mehtar-Tani 2013).", "map": "", "breaks": "A vacuum shower is a quantum branching process driven by soft and collinear logarithms and ends in hadronization. There is no steady forcing or viscous dissipation range, so a true turbulent stationary spectrum exists only for the in-medium cascade.", "confidence": "current research", "strength": 1}
{"id": "C0678", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "06-particle-physics/quantum-field-theory/conformal-field-theory", "name": "Conformal invariance in two-dimensional turbulence", "kind": "method transfer", "summary": "Polyakov (1993) proposed describing 2D turbulence with a non-unitary conformal field theory. Simulations later showed that zero-vorticity isolines in the inverse cascade are SLE₆ curves, the same conformally invariant class as critical percolation hulls (Bernard et al. 2006).", "map": "\\text{vorticity isolines (inverse cascade)}\\ \\sim\\ \\mathrm{SLE}_\\kappa,\\ \\kappa=6", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0679", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "name": "Renormalization group for turbulence and anomalous scaling", "kind": "method transfer", "summary": "Field-theory RG has been applied to randomly stirred Navier–Stokes flow (Forster–Nelson–Stephen, Yakhot–Orszag) to explain Kolmogorov's −5/3 law and to build RNG turbulence models. Intermittency gives anomalous structure-function exponents ζ_p≠p/3, the analogue of anomalous dimensions, but no controlled small parameter is known.", "map": "E(k)=C\\,\\epsilon^{2/3}k^{-5/3},\\quad \\langle\\delta u_\\ell^{\\,p}\\rangle\\propto\\ell^{\\zeta_p},\\quad \\zeta_p\\neq p/3", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0680", "a": "01-classical-mechanics/newtonian-mechanics/central-forces-and-orbits", "b": "06-particle-physics/quantum-field-theory/feynman-diagrams-and-scattering-amplitudes", "name": "Rutherford cross-section: classical = Born = tree level", "kind": "identity", "summary": "For the Coulomb potential, the classical orbit calculation, the quantum Born approximation and the exact quantum result all give the same Rutherford cross-section. In QFT it is the non-relativistic limit of one-photon exchange, the prototype t-channel pole 1/q⁴, with Mott and recoil corrections for spin and kinematics.", "map": "\\frac{d\\sigma}{d\\Omega}=\\left(\\frac{Z_1Z_2\\alpha\\hbar c}{4E}\\right)^2\\frac{1}{\\sin^4(\\theta/2)}\\propto\\frac{1}{q^4}", "breaks": "The coincidence is special to 1/r: for other potentials the classical and Born cross-sections differ, and the exact Coulomb amplitude carries a divergent phase because the force is long-range.", "confidence": "established", "strength": 2}
{"id": "C0681", "a": "01-classical-mechanics/newtonian-mechanics/central-forces-and-orbits", "b": "06-particle-physics/standard-model/quantum-chromodynamics", "name": "From Rutherford's nucleus to deep inelastic partons", "kind": "historical", "summary": "Large-angle scattering that followed the point-charge Rutherford law revealed the nucleus in 1911. The same logic at SLAC in 1968, where structure functions scaled instead of falling like a form factor, revealed point-like partons, which QCD's asymptotic freedom later explained.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0682", "a": "01-classical-mechanics/newtonian-mechanics/conservation-laws", "b": "06-particle-physics/beyond-the-standard-model/dark-matter-particle-candidates", "name": "Elastic-recoil kinematics of dark-matter direct detection", "kind": "mechanism", "summary": "WIMP–nucleus scattering is a two-body elastic collision whose recoil energy peaks when the WIMP and target masses match, which drives the choice of heavy targets (Xe, Ar, Ge) versus light ones for sub-GeV searches. The Earth's orbital velocity adds to the Sun's motion through the halo and produces the predicted annual modulation.", "map": "E_R=\\frac{\\mu^2v^2}{m_N}(1-\\cos\\theta^*),\\quad \\mu=\\frac{m_\\chi m_N}{m_\\chi+m_N}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0683", "a": "01-classical-mechanics/newtonian-mechanics/conservation-laws", "b": "06-particle-physics/neutrino-physics/neutrino-mass-and-double-beta-decay", "name": "Missing energy: from Pauli's neutrino to KATRIN", "kind": "historical", "summary": "Energy and momentum conservation in beta decay led Pauli (1930) to postulate an invisible neutrino, and the same kinematics now measures its mass from the shape of the tritium spectrum near the endpoint (KATRIN). At colliders, missing transverse momentum is how neutrinos and invisible particles are seen.", "map": "\\frac{dN}{dE}\\propto(E_0-E)\\sqrt{(E_0-E)^2-m_\\nu^2}\\quad(E\\to E_0)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0684", "a": "01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics", "b": "06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers", "name": "Orbit determination to track fitting (Kalman filter)", "kind": "method transfer", "summary": "Reconstructing a charged particle's helix in a solenoid from detector hits is an orbit-determination problem. Gauss's least-squares method, devised for Ceres, and the Kalman filter, built for spacecraft navigation, became the standard HEP track and vertex fits, with multiple scattering treated as process noise.", "map": "p_T[\\mathrm{GeV}]=0.3\\,B[\\mathrm T]\\,R[\\mathrm m]", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C0685", "a": "01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics", "b": "06-particle-physics/quantum-field-theory/effective-field-theory", "name": "EFT for the post-Newtonian two-body problem", "kind": "method transfer", "summary": "Non-relativistic GR (Goldberger–Rothstein) treats an inspiralling binary with EFT power counting in v, so integrating out potential gravitons gives the Newtonian and Einstein–Infeld–Hoffmann Lagrangians as Feynman diagrams. Finite-size effects enter as Wilson coefficients (tidal Love numbers), which reorganizes celestial-mechanics perturbation theory with particle-physics tools.", "map": "L=\\tfrac12\\mu v^2+\\frac{G\\mu M}{r}\\left[1+O(v^2)\\right],\\quad v^2\\sim\\frac{GM}{r}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0686", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/bifurcations-and-routes-to-chaos", "b": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "name": "Feigenbaum universality as an RG fixed point", "kind": "method transfer", "summary": "Feigenbaum's constants come from a fixed point of the period-doubling operator acting on maps, which is a Wilson-style renormalization group in function space. The fixed point has one relevant direction (δ) and a rescaling (α), which explains why every unimodal map with a quadratic maximum shares the same exponents.", "map": "\\mathcal Tf(x)=-\\alpha f(f(-x/\\alpha)),\\quad \\mathcal Tg^*=g^*,\\quad \\delta=4.669\\ldots,\\ \\alpha=2.502\\ldots", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0687", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/bifurcations-and-routes-to-chaos", "b": "06-particle-physics/standard-model/higgs-boson", "name": "Pitchfork bifurcation and the Higgs potential", "kind": "analogy", "summary": "The pitchfork normal form is gradient flow in the same quartic potential that the Higgs field has when μ² changes sign, and a bead on a rotating hoop is the textbook mechanical model of spontaneous symmetry breaking. Small oscillations about a Mexican-hat minimum split into a massive radial (Higgs) mode and a flat Goldstone direction.", "map": "\\dot x=rx-x^3=-V'(x),\\ V=-\\tfrac r2x^2+\\tfrac14x^4\\ \\leftrightarrow\\ V(\\phi)=-\\mu^2|\\phi|^2+\\lambda|\\phi|^4", "breaks": "A finite mechanical system has no true symmetry breaking quantum mechanically, since tunneling restores the symmetry; that needs infinite volume. There is also no gauge field to absorb the Goldstone mode, and the electroweak transition in the SM is a thermal crossover, not a bifurcation in time.", "confidence": "established", "strength": 2}
{"id": "C0688", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos", "b": "06-particle-physics/quantum-field-theory/conformal-field-theory", "name": "Lyapunov exponents and the quantum chaos bound", "kind": "analogy", "summary": "Out-of-time-order correlators extend the classical Lyapunov exponent to quantum field theory, because their early-time growth e^{λ_L t} reduces to the classical exponent in the semiclassical limit. In thermal QFT, λ_L is bounded by 2πk_BT/ħ (Maldacena–Shenker–Stanford), and large-c holographic CFTs saturate the bound.", "map": "C(t)=-\\langle[W(t),V]^2\\rangle_\\beta\\sim\\hbar^2e^{\\lambda_Lt},\\quad \\lambda_L\\le\\frac{2\\pi k_BT}{\\hbar}", "breaks": "Classical Lyapunov exponents are unbounded, and the OTOC exponent generally differs from the classical one. A clean exponential window exists only at large N or in the semiclassical regime, and the bound has no classical counterpart.", "confidence": "current research", "strength": 2}
{"id": "C0689", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos", "b": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "name": "Chaos in classical Yang–Mills fields", "kind": "mechanism", "summary": "Spatially homogeneous SU(2) Yang–Mills fields reduce to the almost fully chaotic x²y² Hamiltonian (Matinyan–Savvidy), a Hénon–Heiles-type system. Classical lattice Yang–Mills has positive Lyapunov exponents that scale with g²T, which is used to explain fast entropy production and thermalization of the early glasma in heavy-ion collisions.", "map": "H=\\tfrac12(p_x^2+p_y^2)+\\tfrac12g^2x^2y^2;\\quad \\lambda_{\\max}\\propto g^2T", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0690", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos", "b": "06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc", "name": "Dynamic aperture, resonance overlap and Arnold diffusion", "kind": "method transfer", "summary": "Sextupoles and magnet errors make betatron motion a near-integrable Hamiltonian system. KAM tori bound the stable motion, while Chirikov resonance overlap and slow diffusion set the dynamic aperture and beam lifetime; Laskar's frequency-map analysis, developed for Solar System stability, is now used to design rings.", "map": "H=\\boldsymbol\\nu\\cdot\\mathbf J+\\epsilon\\sum h_{mn}(\\mathbf J)\\cos(m\\phi_x+n\\phi_y),\\quad m\\nu_x+n\\nu_y=p", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0691", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "b": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "name": "Topological solitons, winding numbers and instantons", "kind": "identity", "summary": "Kinks, vortices, monopoles, Skyrmions and Yang–Mills instantons are all finite-energy or finite-action field configurations labeled by homotopy winding numbers and bounded below by Bogomolny bounds. Once quantized, solitons become particles: Coleman showed the sine-Gordon soliton is the massive Thirring fermion, and Skyrmions model baryons.", "map": "Q=\\frac{1}{2\\pi}\\int\\partial_x\\phi\\,dx\\ \\text{(sine-Gordon)};\\quad n=\\frac{g^2}{32\\pi^2}\\int d^4x\\,F\\tilde F\\in\\mathbb Z", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0692", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "b": "06-particle-physics/quantum-field-theory/conformal-field-theory", "name": "Integrability: KdV, Virasoro and 2D field theory", "kind": "identity", "summary": "The second Hamiltonian structure of the KdV equation is the classical Virasoro algebra, and the KdV conserved charges become the quantum integrals of motion of 2D CFT. Lax pairs and inverse scattering carry over to integrable QFTs with factorized S-matrices and to the Bethe-ansatz spin chains that give anomalous dimensions in planar N=4 super-Yang–Mills.", "map": "\\{T(x),T(y)\\}\\propto\\left(\\tfrac{c}{12}\\partial_x^3+2T\\partial_x+T'\\right)\\delta(x-y)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0693", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation", "b": "06-particle-physics/neutrino-physics/neutrino-oscillations", "name": "Synchronized neutrino oscillations from self-interaction", "kind": "analogy", "summary": "When neutrino–neutrino forward scattering dominates the spread of vacuum frequencies Δm²/2E, neutrinos of all energies lock into a common precession at one synchronized frequency, much like mean-field (Kuramoto-type) locking of oscillators with all-to-all coupling. This 'synchronized oscillation' regime matters in supernovae and the early universe.", "map": "\\mu\\gg\\Delta\\omega\\ \\Rightarrow\\ \\omega_{\\rm sync}=\\frac{\\sum_\\omega\\omega\\,\\mathbf P_\\omega\\cdot\\mathbf P}{|\\mathbf P|^2}", "breaks": "The neutrino dynamics is conservative spin precession in a strong collective field, not dissipative phase attraction to a limit cycle, and the locked state can become unstable (bipolar and multi-angle modes).", "confidence": "current research", "strength": 2}
{"id": "C0694", "a": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "b": "06-particle-physics/neutrino-physics/neutrino-oscillations", "name": "Neutrino flavor mixing as coupled pendulums", "kind": "analogy", "summary": "Two coupled pendulums have normal modes rotated by a mixing angle and exchange energy at the beat frequency, which maps onto flavor states as rotated mass eigenstates with P=sin²2θ sin²(Δm²L/4E). Slowly tuning one pendulum through resonance gives adiabatic transfer at an avoided crossing, the MSW effect, with the matter potential playing the role of the detuning.", "map": "\\tan2\\theta=\\frac{2\\kappa}{\\omega_1^2-\\omega_2^2}\\ \\leftrightarrow\\ \\tan2\\theta_m=\\frac{\\sin2\\theta}{\\cos2\\theta-2\\sqrt2G_FN_eE/\\Delta m^2}", "breaks": "Pendulums exchange classical energy, while neutrinos have quantum probability amplitudes. Real symmetric spring couplings cannot produce the CP phase, which needs three flavors and complex mixing, and wave-packet decoherence has no simple mechanical counterpart.", "confidence": "established", "strength": 2}
{"id": "C0695", "a": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "b": "06-particle-physics/quantum-field-theory/canonical-and-path-integral-quantization", "name": "Free fields as infinitely many normal modes", "kind": "identity", "summary": "In the continuum limit a chain of masses and springs, with each mass also tied to the ground by a spring, becomes the Klein–Gordon field, and Fourier normal modes decouple it into independent oscillators. Quantizing each mode gives Fock space, so particles are the quanta of normal modes.", "map": "H=\\sum_{\\mathbf k}\\hbar\\omega_k\\left(a_k^\\dagger a_k+\\tfrac12\\right),\\quad \\omega_k=\\sqrt{\\mathbf k^2+m^2}\\ (\\hbar=c=1)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0696", "a": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "b": "06-particle-physics/standard-model/cp-violation", "name": "Neutral-kaon mixing as coupled damped oscillators", "kind": "analogy", "summary": "K⁰ and K̄⁰ evolve under a non-Hermitian 2×2 Hamiltonian M−iΓ/2, which matches two coupled oscillators whose normal modes (K_S, K_L) have very different damping and beat at Δm. In this picture CP violation is a non-reciprocal coupling between the oscillators, so a mechanical model needs gyroscopic or rotating-frame couplings.", "map": "i\\frac{d}{dt}\\binom{K^0}{\\bar K^0}=\\left(M-\\tfrac{i}{2}\\Gamma\\right)\\binom{K^0}{\\bar K^0},\\quad \\Delta m\\leftrightarrow\\omega_{\\rm beat}", "breaks": "The interference of decay amplitudes into shared final states (ππ), quantum measurement of strangeness, and the CPT structure of M and Γ have no classical analogue.", "confidence": "established", "strength": 2}
{"id": "C0697", "a": "01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators", "b": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "name": "Misalignment: axion field as a Hubble-damped oscillator", "kind": "identity", "summary": "The homogeneous axion field is a damped oscillator with Hubble friction 3H: it stays frozen while overdamped (m_a≪3H) and starts oscillating once m_a~3H. After that its number density is an adiabatic invariant (E/ω) that dilutes as a⁻³ and fixes the cold-dark-matter relic abundance, and large initial angles add pendulum anharmonicity.", "map": "\\ddot\\theta+3H\\dot\\theta+m_a^2(T)\\sin\\theta=0,\\quad n_a=\\rho_a/m_a\\propto a^{-3}", "breaks": "The friction comes from cosmic expansion, not dissipation, so energy redshifts instead of heating a bath, and m_a(T) switches on through QCD effects near the QCD transition.", "confidence": "established", "strength": 2}
{"id": "C0698", "a": "01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators", "b": "06-particle-physics/beyond-the-standard-model/extra-dimensions-and-hierarchy-problem", "name": "Torsion pendulums test large extra dimensions", "kind": "method transfer", "summary": "ADD models with sub-millimeter extra dimensions predict a short-range departure from Newton's inverse-square law. High-Q torsion pendulums limited by thermal noise (Eöt-Wash type) have pushed the allowed Yukawa range down to tens of micrometers, which excludes two large extra dimensions at the millimeter scale.", "map": "V(r)=-\\frac{Gm_1m_2}{r}\\left(1+\\alpha\\,e^{-r/\\lambda}\\right)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0699", "a": "01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators", "b": "06-particle-physics/standard-model/electroweak-theory", "name": "Breit–Wigner lineshape = driven damped resonance", "kind": "identity", "summary": "A resonance's cross-section has the Lorentzian of a driven damped oscillator, with ω²→s, γω→MΓ, Q=M/Γ, and the ringdown time corresponding to the lifetime ħ/Γ. LEP fitted the Z lineshape this way to fix M_Z and Γ_Z, and its invisible width gave three light neutrino species.", "map": "|x|^2\\propto\\frac{1}{(\\omega_0^2-\\omega^2)^2+\\gamma^2\\omega^2}\\ \\leftrightarrow\\ \\sigma(s)\\propto\\frac{1}{(s-M^2)^2+M^2\\Gamma^2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0700", "a": "01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics", "b": "06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers", "name": "Mach cone and Cherenkov cone", "kind": "analogy", "summary": "A charged particle moving faster than light's phase velocity in a medium emits a wavefront cone with the same geometry as the Mach cone of a supersonic body. The cone angle measures β, the principle behind RICH particle identification, threshold counters and Super-K's rings.", "map": "\\sin\\mu=\\frac{c_s}{v}\\ \\leftrightarrow\\ \\cos\\theta_c=\\frac{1}{n\\beta}\\quad(\\theta_c=\\tfrac{\\pi}{2}-\\text{cone half-angle})", "breaks": "Cherenkov light is linear coherent emission from medium polarization, with a dispersive n(ω) that makes the angle and threshold frequency-dependent and the emitted energy tiny (Frank–Tamm). Sonic booms are nonlinear shocks.", "confidence": "established", "strength": 2}
{"id": "C0701", "a": "01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics", "b": "06-particle-physics/standard-model/quantum-chromodynamics", "name": "Lüscher term: zero-point vibrations of the QCD string", "kind": "mechanism", "summary": "The confining flux tube between static quarks vibrates transversely like a string fixed at both ends, and the zero-point energy of its normal modes (ω_n=nπ/r) gives the universal Lüscher correction −π(D−2)/(24r) to the linear potential. Lattice QCD confirms it.", "map": "\\Delta V=\\frac{D-2}{2}\\sum_{n\\ge1}\\frac{n\\pi}{r}\\ \\xrightarrow{\\zeta(-1)=-1/12}\\ -\\frac{\\pi(D-2)}{24r}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0702", "a": "01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations", "b": "06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc", "name": "Hill's equation and alternating-gradient focusing", "kind": "identity", "summary": "Transverse betatron motion in a ring obeys Hill's equation, a parametric oscillator driven by the periodic focusing K(s), so beam stability is a Floquet/Mathieu stability problem. Alternating-gradient focusing stabilizes the beam the way fast driving stabilizes the Kapitza pendulum, tunes must avoid parametric resonances, and the Courant–Snyder invariant is the action of the motion.", "map": "x''+K(s)x=0,\\ K(s+C)=K(s);\\quad x=\\sqrt{2J\\beta(s)}\\cos\\psi(s),\\quad |\\mathrm{Tr}\\,M_{\\rm turn}|<2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0703", "a": "01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations", "b": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "name": "Secular terms and renormalization (Lindstedt to RG)", "kind": "method transfer", "summary": "Naive perturbation theory for the Duffing oscillator produces secular terms that grow like εt, much as loop corrections produce logarithms of the cutoff. Poincaré–Lindstedt removes them by renormalizing the frequency, and the Chen–Goldenfeld–Oono renormalization-group method shows that the RG flow of amplitude and phase is the multiple-scales amplitude equation.", "map": "\\ddot x+x+\\epsilon x^3=0:\\quad x\\approx A\\cos\\omega t,\\ \\ \\omega=1+\\tfrac38\\epsilon A^2+O(\\epsilon^2)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0704", "a": "01-classical-mechanics/rigid-body-dynamics/euler-equations-and-tops", "b": "06-particle-physics/neutrino-physics/neutrino-oscillations", "name": "Flavor pendulum: collective neutrino modes as a top", "kind": "identity", "summary": "In a dense neutrino–antineutrino gas the flavor polarization vectors obey precession equations that reduce exactly to a gyroscopic (spherical) pendulum, a heavy top whose spin is set by the neutrino–antineutrino asymmetry. Bipolar collective flavor conversion in the inverted mass ordering is the inverted pendulum falling over (Hannestad, Raffelt, Sigl & Wong 2006).", "map": "\\dot{\\mathbf P}_\\omega=(\\omega\\mathbf B+\\mu\\mathbf D)\\times\\mathbf P_\\omega\\ \\leftrightarrow\\ \\dot{\\mathbf L}=\\boldsymbol\\tau", "breaks": "The mapping is exact only in the homogeneous, single-angle, two-flavor limit. Multi-angle effects and spatial inhomogeneity (fast flavor instabilities) go beyond the pendulum.", "confidence": "current research", "strength": 2}
{"id": "C0705", "a": "01-classical-mechanics/rigid-body-dynamics/gyroscopes-and-precession", "b": "06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2", "name": "Muon g−2: spin precession of a relativistic gyroscope", "kind": "identity", "summary": "The muon spin in a storage ring precesses like a torqued gyroscope (dS/dt=μ×B), and the experiment measures the difference between the spin and cyclotron frequencies, which is proportional to a_μ. Thomas–BMT precession adds an electric-field term that vanishes at the 'magic' γ≈29.3, which is why the electrostatic focusing does not spoil the measurement.", "map": "\\boldsymbol\\omega_a=-\\frac{e}{m}\\left[a_\\mu\\mathbf B-\\left(a_\\mu-\\frac{1}{\\gamma^2-1}\\right)\\frac{\\boldsymbol\\beta\\times\\mathbf E}{c}\\right]", "breaks": "Spin is intrinsic with g≈2, so the ratio of moment to angular momentum differs from a classical body. Thomas precession is a relativistic kinematic effect, and the spin direction is read out through parity-violating decay.", "confidence": "established", "strength": 2}
{"id": "C0706", "a": "01-classical-mechanics/rigid-body-dynamics/rotational-dynamics-and-inertia-tensor", "b": "06-particle-physics/standard-model/hadron-spectroscopy-and-exotics", "name": "Regge trajectories from a rotating relativistic string", "kind": "mechanism", "summary": "Modeling a meson as a rigid rotating string of tension σ with its ends moving at c, the energy and angular momentum integrals give J=M²/(2πσ), a linear Regge trajectory. With σ≈0.18 GeV² the predicted slope α'≈0.88 GeV⁻² matches the observed ~0.9 GeV⁻².", "map": "E=\\pi\\sigma R,\\quad J=\\tfrac{\\pi}{2}\\sigma R^2\\ \\Rightarrow\\ J=\\alpha'M^2,\\quad \\alpha'=\\frac{1}{2\\pi\\sigma}\\ (\\hbar=c=1)", "breaks": "This is a classical idealization with massless ends: quark masses, the quantum intercept α₀ and string breaking all modify it.", "confidence": "established", "strength": 2}
{"id": "C1054", "a": "02-electromagnetism-and-optics/classical-optics/coherence-and-statistical-optics", "b": "06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc", "name": "HBT intensity interferometry → Bose–Einstein femtoscopy", "kind": "method transfer", "summary": "Hanbury Brown and Twiss measured star sizes from intensity correlations. Goldhaber, Goldhaber, Lee and Pais (1960) found the same Bose–Einstein enhancement for like-sign pions, and LHC experiments now use it to measure femtometre source radii in pp, p–Pb and Pb–Pb collisions.", "map": "C_2(q)=\\frac{\\langle n_1n_2\\rangle}{\\langle n_1\\rangle\\langle n_2\\rangle}=1+\\lambda\\,e^{-q^2R^2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1055", "a": "02-electromagnetism-and-optics/classical-optics/geometric-optics", "b": "06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc", "name": "Beam optics: ray-transfer matrices for magnet lattices", "kind": "method transfer", "summary": "Transverse beam dynamics uses ABCD ray-transfer matrices: drifts are free propagation, quadrupoles are thin lenses, and a FODO cell of alternating converging and diverging lenses gives net focusing (strong focusing). Chromaticity is the beam-optics version of chromatic aberration and is corrected with sextupoles.", "map": "\\begin{pmatrix}x\\\\x'\\end{pmatrix}_{\\rm out}=M\\begin{pmatrix}x\\\\x'\\end{pmatrix}_{\\rm in},\\quad M_Q=\\begin{pmatrix}1&0\\\\-1/f&1\\end{pmatrix},\\ \\frac1f=\\frac{eG\\ell}{p}", "breaks": "A quadrupole focuses in one transverse plane and defocuses in the other, so net focusing needs alternating gradients. Beams also have emittance (Liouville in 6D phase space), space charge and nonlinear resonances, which passive optics lacks.", "confidence": "established", "strength": 2}
{"id": "C1056", "a": "02-electromagnetism-and-optics/classical-optics/interference-and-diffraction", "b": "06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc", "name": "Diffractive elastic pp scattering as Fraunhofer diffraction", "kind": "analogy", "summary": "High-energy elastic pp scattering (TOTEM at 13 TeV) shows a forward peak and a diffraction dip, like the Airy pattern of an absorbing disc in the momentum transfer √(−t). The optical theorem ties the forward amplitude to σ_tot, and a black disc would have σ_el/σ_tot = 1/2.", "map": "\\frac{d\\sigma}{dt}\\propto\\left|\\frac{J_1(R\\sqrt{-t})}{R\\sqrt{-t}}\\right|^2,\\quad \\sigma_{\\rm el}^{\\rm black}=\\tfrac12\\sigma_{\\rm tot}=\\pi R^2", "breaks": "The proton is grey (σ_el/σ_tot ≈ 0.26 at 13 TeV) and grows with energy (Froissart ln²s). Its amplitude has a real part and spin dependence, so a single disc cannot fit the dip depth.", "confidence": "established", "strength": 2}
{"id": "C1057", "a": "02-electromagnetism-and-optics/classical-optics/polarization-and-crystal-optics", "b": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "name": "Axion-induced vacuum birefringence and dichroism", "kind": "mechanism", "summary": "With the coupling g a E·B, only the photon polarization component parallel to an external B mixes with an axion-like particle. A magnetized vacuum therefore becomes dichroic (real conversion) and birefringent (virtual axions), which PVLAS-type polarimeters search for. An oscillating axion background rotates linear polarization; this is the proposed explanation for a ~2–3σ hint of CMB cosmic birefringence.", "map": "-\\tfrac{g_{a\\gamma\\gamma}}{4}aF_{\\mu\\nu}\\tilde F^{\\mu\\nu}=g_{a\\gamma\\gamma}\\,a\\,\\mathbf E\\cdot\\mathbf B\\ \\Rightarrow\\ \\text{only }\\mathbf E_\\gamma\\parallel\\mathbf B_{\\rm ext}\\text{ mixes}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1058", "a": "02-electromagnetism-and-optics/classical-optics/polarization-and-crystal-optics", "b": "06-particle-physics/neutrino-physics/neutrino-oscillations", "name": "Flavour oscillation as birefringence; MSW as adiabatic following", "kind": "analogy", "summary": "Two neutrino flavours behave like two linear polarizations, and the mass eigenstates like the axes of a birefringent plate, so the conversion probability has the same form as light leaking through crossed polarizers. Solar MSW conversion is the analogue of light adiabatically following the axes of a slowly twisted birefringent medium (the Poincaré/Bloch-sphere picture).", "map": "P_{e\\mu}=\\sin^22\\theta\\,\\sin^2\\frac{\\Delta m^2L}{4E}\\ \\leftrightarrow\\ I_\\perp=\\sin^22\\theta\\,\\sin^2\\frac{\\Delta n\\,\\omega L}{2c}", "breaks": "There are three flavours with a CP-violating phase and an absolute mass ordering, while light has only two polarization states. The phase comes from mass differences, not refractive-index differences.", "confidence": "established", "strength": 2}
{"id": "C1059", "a": "02-electromagnetism-and-optics/electrodynamics", "b": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "name": "Maxwell theory as abelian Yang–Mills", "kind": "identity", "summary": "Covariant electrodynamics is the U(1) case of Yang–Mills theory: the same action, field strength and field equations. Yang–Mills adds a commutator term that makes gluons and W bosons self-interacting, while photons do not interact with each other.", "map": "F_{\\mu\\nu}=\\partial_\\mu A_\\nu-\\partial_\\nu A_\\mu-ig[A_\\mu,A_\\nu],\\ \\ D_\\mu F^{\\mu\\nu}=j^\\nu,\\ \\ \\mathcal L=-\\tfrac14\\mathrm{tr}F_{\\mu\\nu}F^{\\mu\\nu}", "breaks": "The non-abelian commutator gives cubic and quartic self-couplings, asymptotic freedom and confinement, none of which classical electromagnetism has.", "confidence": "established", "strength": 3}
{"id": "C1060", "a": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "b": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "name": "Haloscope: axions drive a resonant microwave cavity", "kind": "method transfer", "summary": "In a static field B₀, dark-matter axions act as an oscillating effective current g ȧ B₀. This current drives the TM₀₁₀ mode of a tuned cavity when ω = m_a c²/ħ, as in Sikivie's haloscope (ADMX, HAYSTAC). Sensitivity depends on standard cavity quantities: mode form factor, volume, Q and tuning range.", "map": "P_{a\\to\\gamma}\\approx g_{a\\gamma\\gamma}^2\\frac{\\rho_a}{m_a}B_0^2\\,V\\,C_{010}\\,\\min(Q_L,Q_a)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1061", "a": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "b": "06-particle-physics/beyond-the-standard-model/extra-dimensions-and-hierarchy-problem", "name": "Waveguide cutoff modes = Kaluza–Klein mass tower", "kind": "identity", "summary": "Confining a massless field in compact transverse directions quantizes its transverse momentum. Each guided mode then follows a massive-particle dispersion relation along the free direction, with the cutoff frequency playing the role of the Kaluza–Klein mass.", "map": "\\omega^2=c^2k_z^2+\\omega_{mn}^2\\ \\leftrightarrow\\ E^2=p^2c^2+m_n^2c^4,\\quad m_nc^2=\\hbar\\omega_n,\\ \\omega_n=nc/R", "breaks": "Conducting walls impose Dirichlet/Neumann conditions instead of periodicity, so TE/TM spectra (and the missing TM zero mode) differ from a KK circle, and the waveguide geometry produces no gauge field.", "confidence": "established", "strength": 2}
{"id": "C1062", "a": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "b": "06-particle-physics/collider-and-experimental-particle-physics/future-colliders", "name": "RF cavities accelerate collider beams", "kind": "method transfer", "summary": "Beams gain energy from the longitudinal E field of the TM₀₁₀ mode of resonant cavities. The achievable gradient (~30–40 MV/m for superconducting niobium in the ILC, ~70–100 MV/m for normal-conducting X-band in CLIC) sets the length and cost of linear colliders.", "map": "E_z=E_0J_0(2.405\\,r/R)\\cos\\omega t,\\quad \\omega_{010}=2.405\\,c/R", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1063", "a": "02-electromagnetism-and-optics/electrodynamics/maxwells-equations", "b": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "name": "Axion electrodynamics: modified Maxwell equations", "kind": "identity", "summary": "Adding g a E·B to the Maxwell Lagrangian gives effective charge and current densities proportional to ∇a and ȧ. These are the field equations behind haloscopes, helioscopes and stellar-cooling bounds. The same equations with constant θ = π describe the magnetoelectric response of topological insulators.", "map": "\\nabla\\cdot\\mathbf E=\\rho-g\\nabla a\\cdot\\mathbf B,\\quad \\nabla\\times\\mathbf B-\\dot{\\mathbf E}=\\mathbf J+g(\\dot a\\mathbf B+\\nabla a\\times\\mathbf E)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1064", "a": "02-electromagnetism-and-optics/electrodynamics/maxwells-equations", "b": "06-particle-physics/beyond-the-standard-model/extra-dimensions-and-hierarchy-problem", "name": "Kaluza–Klein: electromagnetism from a fifth dimension", "kind": "historical", "summary": "Five-dimensional general relativity on a small circle reduces to 4D gravity plus Maxwell theory plus a scalar. The off-diagonal metric components g_{μ5} play the role of A_μ, and U(1) gauge transformations are reparametrizations of the circle. This is the ancestor of modern large and warped extra-dimension models.", "map": "g_{\\mu5}\\propto A_\\mu,\\quad \\sqrt{-g^{(5)}}R^{(5)}\\to\\sqrt{-g}\\,\\phi\\left(R-\\tfrac14\\phi^2F_{\\mu\\nu}F^{\\mu\\nu}+\\dots\\right)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1065", "a": "02-electromagnetism-and-optics/electrodynamics/maxwells-equations", "b": "06-particle-physics/beyond-the-standard-model/grand-unification-and-proton-decay", "name": "Magnetic monopoles: Dirac quantization and GUT monopoles", "kind": "shared object", "summary": "A magnetic charge makes Maxwell's equations symmetric, and Dirac showed that a single monopole would force electric charge to be quantized. Breaking a simple GUT group down to U(1)_em necessarily creates 't Hooft–Polyakov monopoles of mass ~M_X/α. Their predicted overabundance helped motivate inflation; MoEDAL and IceCube searches have found none.", "map": "\\nabla\\cdot\\mathbf B=\\rho_m,\\quad qg=2\\pi n\\ (\\hbar=c=1,\\ \\text{HL}),\\quad M_{\\rm mon}\\sim M_X/\\alpha_{\\rm GUT}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1066", "a": "02-electromagnetism-and-optics/electrodynamics/maxwells-equations", "b": "06-particle-physics/quantum-field-theory/canonical-and-path-integral-quantization", "name": "Quantized Maxwell field: the first quantum field theory", "kind": "historical", "summary": "A normal-mode expansion turns the free Maxwell field into independent harmonic oscillators, and quantizing them (Dirac 1927) gives photons. Gauge redundancy forced the Coulomb-gauge, Gupta–Bleuler and later BRST treatments that became the template for quantizing every gauge field.", "map": "H=\\sum_{\\mathbf k,\\lambda=\\pm}\\hbar\\omega_k\\left(a^\\dagger_{\\mathbf k\\lambda}a_{\\mathbf k\\lambda}+\\tfrac12\\right),\\quad [a_{\\mathbf k\\lambda},a^\\dagger_{\\mathbf k'\\lambda'}]=\\delta_{\\mathbf k\\mathbf k'}\\delta_{\\lambda\\lambda'}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1067", "a": "02-electromagnetism-and-optics/electrodynamics/potentials-and-gauge-invariance", "b": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "name": "Gauge transformations and the covariant derivative", "kind": "identity", "summary": "The freedom A→A+∂χ of electromagnetic potentials, paired with a local phase change of charged matter fields, is the gauge principle. Yang and Mills extended it to non-abelian groups, where A becomes a matrix-valued connection and the potentials become the fundamental fields.", "map": "A_\\mu\\to A_\\mu+\\partial_\\mu\\chi,\\ \\ \\psi\\to e^{iq\\chi/\\hbar}\\psi,\\ \\ D_\\mu=\\partial_\\mu-\\tfrac{iq}{\\hbar}A_\\mu\\ \\to\\ D_\\mu=\\partial_\\mu-igA^a_\\mu T^a", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1068", "a": "02-electromagnetism-and-optics/electrodynamics/potentials-and-gauge-invariance", "b": "06-particle-physics/quantum-field-theory/lattice-field-theory", "name": "Aharonov–Bohm phase as the Wilson loop", "kind": "identity", "summary": "The Aharonov–Bohm phase around a solenoid is the holonomy of the U(1) connection. Wilson made these parallel transporters the basic lattice variables (link variables) and used the Wilson loop as the order parameter for confinement (area law).", "map": "U_{x,\\mu}=e^{iagA_\\mu(x)},\\quad W(C)=\\prod_{\\ell\\in C}U_\\ell\\to e^{\\frac{iq}{\\hbar}\\oint_C\\mathbf A\\cdot d\\mathbf l}=e^{iq\\Phi_B/\\hbar}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1069", "a": "02-electromagnetism-and-optics/electrodynamics/relativistic-electrodynamics", "b": "06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2", "name": "Thomas–BMT spin precession and the magic momentum", "kind": "method transfer", "summary": "The muon g−2 experiment measures how much faster the spin precesses (Thomas–BMT equation) than the momentum rotates, in a 1.45 T storage ring with field mapped by proton NMR. At γ = 29.3 (3.094 GeV/c) the motional-E term from electrostatic focusing cancels, so a_μ follows from ω_a and B alone. Fermilab's final result (2025) reached 127 ppb.", "map": "\\boldsymbol\\omega_a=-\\frac{q}{m}\\left[a_\\mu\\mathbf B-\\left(a_\\mu-\\frac{1}{\\gamma^2-1}\\right)\\frac{\\boldsymbol\\beta\\times\\mathbf E}{c}\\right],\\ \\gamma_{\\rm magic}=29.3", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1070", "a": "02-electromagnetism-and-optics/electrodynamics/relativistic-electrodynamics", "b": "06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc", "name": "Weizsäcker–Williams photons in ultraperipheral collisions", "kind": "method transfer", "summary": "Lorentz contraction flattens an ultrarelativistic charge's field into a transverse pancake, equivalent to a flux of quasi-real photons with a spectrum ∝ Z²α/ω. With the Z⁴ enhancement, Pb–Pb ultraperipheral collisions at the LHC act as a photon–photon collider, where light-by-light scattering and γγ→ℓℓ are measured.", "map": "\\frac{dN_\\gamma}{d\\omega}\\simeq\\frac{2Z^2\\alpha}{\\pi\\omega}\\ln\\frac{\\gamma c}{\\omega b_{\\min}},\\quad \\sigma_{\\gamma\\gamma}^{AA}\\propto Z^4", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1071", "a": "02-electromagnetism-and-optics/electrodynamics/relativistic-electrodynamics", "b": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "name": "E·B invariant as the chiral-anomaly density", "kind": "identity", "summary": "The pseudoscalar Lorentz invariant FF̃ ∝ E·B is the U(1) Chern–Pontryagin density. As a total derivative it has no classical effect, but it sources the ABJ anomaly: π⁰→γγ, and chiral charge pumping when E and B are parallel (the chiral magnetic effect).", "map": "\\partial_\\mu j_5^\\mu=-\\frac{e^2}{8\\pi^2}F_{\\mu\\nu}\\tilde F^{\\mu\\nu}=\\frac{e^2}{2\\pi^2}\\,\\mathbf E\\cdot\\mathbf B\\quad(\\hbar=c=1)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1072", "a": "02-electromagnetism-and-optics/electrodynamics/relativistic-electrodynamics", "b": "06-particle-physics/standard-model/electroweak-theory", "name": "The photon as the unbroken U(1)_em combination", "kind": "identity", "summary": "Maxwell theory is the massless U(1) that survives when the Higgs breaks SU(2)_L×U(1)_Y. The electron charge is fixed by g, g′ and the weak mixing angle, and the Z is the orthogonal, massive combination — classical electrodynamics is the low-energy remnant of electroweak theory.", "map": "A_\\mu=\\sin\\theta_W\\,W^3_\\mu+\\cos\\theta_W\\,B_\\mu,\\quad e=g\\sin\\theta_W=g'\\cos\\theta_W,\\quad Q=T_3+Y", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1073", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/electrostatics-and-boundary-value-problems", "b": "06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers", "name": "Shockley–Ramo theorem: signals from weighting fields", "kind": "method transfer", "summary": "The current that a drifting charge induces on a readout electrode (silicon strips and pixels, wire chambers, TPC pads) follows from Green's reciprocity. One solves Laplace's equation with that electrode at unit potential and all others grounded, and the induced current is the charge's velocity dotted into this weighting field.", "map": "i(t)=q\\,\\mathbf v(t)\\cdot\\mathbf E_w(\\mathbf x(t)),\\quad \\nabla^2\\phi_w=0,\\ \\phi_w|_{\\rm readout}=1,\\ \\phi_w|_{\\rm others}=0", "breaks": "", "confidence": "established", "strength": 2}