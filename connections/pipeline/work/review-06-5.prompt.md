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

# Packet 06-5 (75 records)

{"id": "C2339", "a": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Plasma frequency as photon mass for axion resonance", "kind": "mechanism", "summary": "In a plasma the photon acquires an effective mass ħω_p, so axion–photon (and dark-photon) conversion is resonant where m_a c² = ħω_p. This underlies radio-line searches for axion dark matter converting in neutron-star magnetospheres, tunable plasma haloscopes that set ω_p with wire metamaterials, and resonant dark-photon production in the Sun. Stellar-plasma emission (Primakoff, plasmon decay) is also behind stellar-cooling bounds on axions and neutrino dipole moments.", "map": "m_ac^2=\\hbar\\omega_p,\\quad \\omega_p=\\sqrt{\\frac{n_ee^2}{\\epsilon_0m_e}}\\ \\Rightarrow\\ \\hbar\\omega_p\\approx37\\,\\mu\\mathrm{eV}\\sqrt{\\frac{n_e}{10^{12}\\,\\mathrm{cm^{-3}}}}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2340", "a": "06-particle-physics/beyond-the-standard-model/baryogenesis-and-matter-antimatter", "b": "10-plasma-physics/magnetohydrodynamics/mhd-turbulence", "name": "Hypermagnetic helicity, the anomaly and inverse cascades", "kind": "mechanism", "summary": "Above the electroweak scale, helical hypercharge magnetic fields source baryon and lepton number through the U(1)_Y anomaly. Their evolution (the inverse helicity cascade in MHD turbulence and helicity decay at the electroweak crossover) can therefore generate or wash out the baryon asymmetry (Giovannini–Shaposhnikov 1998; Kamada–Long 2016).", "map": "\\partial_\\mu j_B^\\mu=\\frac{N_g}{32\\pi^2}\\left(g^2W^a\\tilde W^a-g'^2Y\\tilde Y\\right),\\quad \\int Y\\tilde Y\\,d^4x\\propto\\Delta H_Y", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2341", "a": "06-particle-physics/beyond-the-standard-model/baryogenesis-and-matter-antimatter", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Sphaleron rate set by hot gauge-plasma kinetics", "kind": "mechanism", "summary": "Baryon-violating sphaleron transitions in the hot electroweak plasma run through soft magnetic modes (k ~ g²T) that hard particles overdamp via Landau damping. Arnold–Son–Yaffe and Bödeker showed Γ_sph ∝ α_w^5 T^4 ln(1/α_w); Bödeker's effective theory is a Langevin equation equivalent to Ohmic magnetic diffusion with a colour conductivity. Plasma kinetics thus fixes the rate used in baryogenesis and washout calculations.", "map": "\\Gamma_{sph}\\simeq\\kappa\\,\\alpha_w^5T^4\\ln\\frac{1}{\\alpha_w},\\qquad \\sigma\\,\\partial_t\\mathbf A=-\\mathbf D\\times\\mathbf B+\\boldsymbol\\xi", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2342", "a": "06-particle-physics/beyond-the-standard-model/dark-matter-particle-candidates", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Dark plasmas: instabilities constrain charged dark matter", "kind": "mechanism", "summary": "If dark matter carries charge under a dark U(1) or a millicharge, halos behave as collisionless plasmas. In cluster mergers, Weibel and two-stream instabilities could isotropize and decelerate dark matter far faster than binary scattering, so plasma growth rates rather than cross-sections set Bullet-Cluster-type bounds on the dark fine-structure constant.", "map": "", "breaks": "Whether the instabilities grow and saturate fast enough to transfer momentum is contested; later analyses argued earlier bounds were overestimated. Magnetized dark plasmas also behave differently.", "confidence": "current research", "strength": 1}
{"id": "C2343", "a": "06-particle-physics/beyond-the-standard-model/dark-matter-particle-candidates", "b": "10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks", "name": "Bullet Cluster: plasma shock versus collisionless DM", "kind": "shared object", "summary": "In the merging Bullet Cluster (1E 0657-56) ram pressure slows the X-ray intracluster plasma, which drives a Mach ≈ 3 bow shock, while the lensing mass passes through with the galaxies. The offset is key evidence for collisionless particle dark matter and bounds its self-interaction. The same shock is a laboratory for collisionless-shock physics and electron–ion equilibration.", "map": "\\sigma_{DM}/m\\lesssim1\\ \\mathrm{cm^2\\,g^{-1}},\\quad \\mathcal M_{shock}\\approx3", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2344", "a": "06-particle-physics/beyond-the-standard-model/grand-unification-and-proton-decay", "b": "10-plasma-physics/magnetohydrodynamics/dynamo-theory", "name": "Parker bound: galactic dynamo limits GUT monopoles", "kind": "mechanism", "summary": "Grand unification predicts superheavy 't Hooft–Polyakov monopoles. Monopoles crossing the Galaxy would be accelerated by its magnetic field and drain its energy faster than the galactic dynamo regenerates it (~10^8 yr), which gives the Parker bound on the monopole flux. This dynamo constraint on GUT cosmology, together with the monopole overabundance problem, helped motivate inflation.", "map": "F_M\\lesssim10^{-15}\\ \\mathrm{cm^{-2}\\,s^{-1}\\,sr^{-1}}\\quad(m_M\\lesssim10^{17}\\ \\mathrm{GeV})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2345", "a": "06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "g−2 from cyclotron versus spin precession", "kind": "shared object", "summary": "The muon g−2 storage ring (BNL, Fermilab) measures ω_a = ω_s − ω_c, the beat between spin precession and cyclotron gyration in a uniform 1.45 T field. It uses electrostatic quadrupole focusing and the magic momentum 3.09 GeV/c (γ ≈ 29.3), which cancels the β×E term. Electron g−2 uses one electron in a Penning trap, whose magnetron motion is the E×B drift: single-particle orbit theory as a precision instrument.", "map": "\\boldsymbol\\omega_a=-\\frac{e}{m}\\left[a_\\mu\\mathbf B-\\left(a_\\mu-\\frac{1}{\\gamma^2-1}\\right)\\frac{\\boldsymbol\\beta\\times\\mathbf E}{c}\\right]", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2346", "a": "06-particle-physics/collider-and-experimental-particle-physics/future-colliders", "b": "10-plasma-physics/inertial-and-laser-plasmas", "name": "Laser and beam plasmas as advanced-accelerator R&D", "kind": "method transfer", "summary": "The laser–plasma toolkit (chirped-pulse-amplified lasers, beam–plasma interaction, plasma lenses, wakefield staging) is the advanced-accelerator line in collider strategy studies, and collider luminosity targets translate back into required driver average power, kHz repetition rates and wall-plug efficiency for the plasma community.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2347", "a": "06-particle-physics/collider-and-experimental-particle-physics/future-colliders", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "Beamstrahlung and laser radiation reaction share χ", "kind": "mechanism", "summary": "At linear-collider interaction points the collective field of one nanometre-scale bunch acts on the other like an ultra-intense laser. Particles pinch (disruption), radiate (beamstrahlung) and convert photons to pairs, governed by the same quantum-nonlinearity parameter χ (Υ) that defines the radiation-reaction and QED-plasma regime of multi-PW laser–plasma experiments. Beam–beam codes and QED-PIC codes use the same locally-constant-field emission rates.", "map": "\\chi=\\frac{\\gamma\\,|\\mathbf E_\\perp+\\mathbf v\\times\\mathbf B|}{E_S},\\quad E_S=\\frac{m_e^2c^3}{e\\hbar}\\approx1.32\\times10^{18}\\ \\mathrm{V/m}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2348", "a": "06-particle-physics/collider-and-experimental-particle-physics/future-colliders", "b": "10-plasma-physics/inertial-and-laser-plasmas/plasma-wakefield-acceleration", "name": "Plasma wakefield accelerators as compact collider drivers", "kind": "method transfer", "summary": "Plasma waves sustain accelerating fields near the cold wave-breaking limit, 10–100 GV/m against ~100 MV/m in RF cavities, so laser- or beam-driven wakefield stages are the candidate route to compact multi-TeV lepton colliders; collider requirements (energy spread, emittance preservation, wall-plug efficiency, positron acceleration, staging) define the field's open problems.", "map": "E_0=\\frac{m_ec\\,\\omega_p}{e}\\approx96\\sqrt{n_e[\\mathrm{cm^{-3}}]}\\ \\mathrm{V/m},\\quad \\lambda_p=\\frac{2\\pi c}{\\omega_p}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2349", "a": "06-particle-physics/collider-and-experimental-particle-physics/future-colliders", "b": "10-plasma-physics/magnetic-confinement-fusion/tokamaks", "name": "High-field superconducting magnets: colliders and tokamaks", "kind": "method transfer", "summary": "Collider energy scales as B·R and tokamak fusion power at fixed β as B^4, so both push the same conductors. These are Nb–Ti (LHC, 8.3 T), Nb3Sn (HL-LHC triplets ~11 T, ITER toroidal-field and central-solenoid coils) and REBCO high-temperature superconductors (the 20 T CFS/MIT SPARC model coil, 2021; candidate FCC-hh dipoles and muon-collider solenoids). Both fields share quench protection, stress management and cryogenics.", "map": "E_{beam}\\propto BR,\\qquad P_{fus}\\propto\\beta^2B^4V", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2350", "a": "06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc", "b": "10-plasma-physics/inertial-and-laser-plasmas/plasma-wakefield-acceleration", "name": "AWAKE: proton-driven wakefields from the LHC injectors", "kind": "method transfer", "summary": "AWAKE at CERN sends 400 GeV SPS proton bunches (the LHC injector beam) into a 10 m rubidium plasma; the bunch, far longer than λ_p, undergoes the seeded self-modulation instability into microbunches that resonantly drive a wake, which accelerated injected electrons to ~2 GeV (2018). Proton bunches store ~20–130 kJ, enough in principle for single-stage acceleration to TeV energies.", "map": "\\sigma_z\\gg\\lambda_p\\ \\Rightarrow\\ \\text{self-modulation at }k_p=\\omega_p/c", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2351", "a": "06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Electron cloud and two-stream instability in the LHC", "kind": "mechanism", "summary": "Synchrotron-light photoelectrons multiply by secondary emission into an electron cloud in the LHC beam screen. This non-neutral plasma adds cryogenic heat load and drives the electron–proton two-stream instability, tune shifts and emittance growth. It is analysed with plasma linear-instability theory and particle-in-cell codes, and mitigated by beam scrubbing and low-secondary-yield coatings.", "map": "\\omega_e^2=\\frac{2\\lambda_br_ec^2}{\\sigma_y(\\sigma_x+\\sigma_y)},\\quad \\lambda_b=\\frac{N_b}{\\sqrt{2\\pi}\\,\\sigma_z}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2352", "a": "06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc", "b": "10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks", "name": "Hillas criterion: cosmic accelerators versus colliders", "kind": "analogy", "summary": "Any accelerator must keep the particle's gyroradius inside the accelerating region, so maximum energy scales as field times size. 8.33 T dipoles on a 2.8 km bending radius give the LHC 7 TeV, while the Hillas criterion applied to supernova-remnant, AGN-jet and cluster shocks bounds cosmic-ray energies up to ~10^20 eV (√s ≈ 430 TeV on a proton target).", "map": "E_{max}\\approx Ze\\,\\beta_sc\\,BR\\ \\leftrightarrow\\ p[\\mathrm{GeV}/c]=0.3\\,B[\\mathrm{T}]\\,\\rho[\\mathrm{m}]", "breaks": "Shock acceleration is stochastic: repeated diffusive crossings in turbulent, self-generated fields produce power-law spectra, and β_s≪1 plus radiative or escape losses lower E_max. Colliders accelerate coherently with RF in fixed guide fields and deliver near-monoenergetic beams.", "confidence": "established", "strength": 1}
{"id": "C2353", "a": "06-particle-physics/collider-and-experimental-particle-physics/jets-and-qcd-phenomenology", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Jet quenching as stopping power in a QCD plasma", "kind": "mechanism", "summary": "Energy loss of a fast parton crossing the QGP is computed like charged-particle stopping in a plasma. It has three parts: collisional loss with a Coulomb logarithm cut off by the Debye mass (Bjorken 1982; Braaten–Thoma), a jet transport coefficient q̂ that is a transverse-momentum (Fokker–Planck) diffusion coefficient, and radiative loss with Landau–Pomeranchuk–Migdal coherence (BDMPS).", "map": "-\\frac{dE}{dx}\\Big|_{coll}\\propto\\alpha_s^2T^2\\ln\\frac{ET}{m_D^2}\\ \\leftrightarrow\\ -\\frac{dE}{dx}\\propto\\frac{q^2\\omega_p^2}{v^2}\\ln\\Lambda;\\quad \\hat q=\\frac{\\langle k_\\perp^2\\rangle}{L}", "breaks": "For coloured partons radiative loss dominates and grows as L² (BDMPS). Non-relativistic plasma stopping has no counterpart, since bremsstrahlung there is negligible.", "confidence": "established", "strength": 2}
{"id": "C2354", "a": "06-particle-physics/collider-and-experimental-particle-physics/machine-learning-in-hep", "b": "10-plasma-physics/magnetic-confinement-fusion/tokamaks", "name": "Machine learning for triggers and tokamak control", "kind": "method transfer", "summary": "HEP developed low-latency deep learning for triggers, fast surrogate simulation and anomaly detection; fusion has its counterparts in neural disruption predictors (Kates-Harbeck et al. 2019) and reinforcement-learning magnetic control on TCV (Degrave et al. 2022). Both need microsecond-scale FPGA inference, rare-event detection under class imbalance, and simulation-trained models that survive domain shift to the real machine.", "map": "", "breaks": "", "confidence": "current research", "strength": 1}
{"id": "C2355", "a": "06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers", "b": "10-plasma-physics/low-temperature-and-applied-plasmas/plasma-discharges-and-processing", "name": "Gaseous detectors are controlled Townsend discharges", "kind": "mechanism", "summary": "Geiger and proportional counters, MWPCs, drift chambers, GEMs, Micromegas and RPCs amplify ionization by Townsend avalanches. They must stay below the Raether limit (αd ≈ 20, ~10^8 electrons), where avalanches become streamers and sparks; this is the breakdown physics of gas discharges (Townsend coefficients, Paschen curves, streamer theory). RPCs run deliberately in avalanche or streamer mode, and detector ageing is plasma polymerization, the same chemistry as plasma deposition.", "map": "M=\\exp\\left(\\int\\alpha(E/p)\\,dx\\right),\\qquad \\alpha d\\approx20\\ \\text{(Raether limit)}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2356", "a": "06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers", "b": "10-plasma-physics/space-and-astrophysical-plasmas/magnetospheres-and-space-weather", "name": "Geiger counters discovered the radiation belts", "kind": "historical", "summary": "Van Allen's Geiger–Müller counters on Explorer 1 and 3 (1958) saturated in trapped-particle regions, which is how the radiation belts were discovered. Space-plasma particle instruments descend from nuclear and particle detectors (scintillators, silicon, magnetic spectrometers such as AMS-02). LHC front-end electronics and satellites face the same single-event effects and radiation-hardness engineering.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2357", "a": "06-particle-physics/neutrino-physics/neutrino-experiments-and-sources", "b": "10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks", "name": "Shock-accelerated cosmic rays as neutrino sources", "kind": "mechanism", "summary": "Diffusive shock acceleration gives power-law protons whose pp and pγ collisions make pions. Pion decays yield neutrinos carrying ~5% of the proton energy, with flavor ratio ≈1:1:1 at Earth and a spectrum that tracks the parent. This is the hadronic-source signature IceCube seeks (TXS 0506+056, the Galactic plane), although coronal sources such as NGC 1068 may accelerate by turbulence or reconnection instead.", "map": "\\frac{dN}{dE}\\propto E^{-\\frac{r+2}{r-1}}\\to E^{-2}\\ (r=4),\\qquad E_\\nu\\approx E_p/20", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2358", "a": "06-particle-physics/neutrino-physics/neutrino-oscillations", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "MSW potential and plasma frequency: medium dispersion", "kind": "analogy", "summary": "Coherent forward scattering on electrons gives electron neutrinos the potential V = √2 G_F n_e (Wolfenstein 1978), just as forward scattering of photons on free electrons gives the refractive term ω_p² ∝ n_e. Both shift the dispersion in proportion to electron density, and resonant MSW level crossings (adiabatic or Landau–Zener) parallel mode conversion at resonances in inhomogeneous plasmas.", "map": "V_{CC}=\\sqrt2\\,G_Fn_e\\ \\leftrightarrow\\ n_{ref}^2=1-\\frac{\\omega_p^2}{\\omega^2},\\quad \\omega_p^2=\\frac{n_ee^2}{\\epsilon_0m_e}", "breaks": "The MSW potential is a flavor-dependent weak-interaction effect (~10^-11 eV in the solar core) that acts through mixing rather than giving a mass or cutoff. Photon refraction is electromagnetic and produces a cutoff at ω = ω_p.", "confidence": "established", "strength": 2}
{"id": "C2359", "a": "06-particle-physics/neutrino-physics/neutrino-oscillations", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Neutrino quantum kinetics as matrix-valued Vlasov", "kind": "identity", "summary": "Neutrino transport with oscillations obeys quantum kinetic equations (Sigl–Raffelt 1993) for flavor density matrices. They combine free streaming, a commutator with a self-consistent mean-field Hamiltonian (vacuum, MSW and ν–ν refraction) and collisions. This is the structure of a Vlasov system with a self-consistent field, so mean-field, quasilinear and moment-closure methods transfer from plasma kinetics.", "map": "(\\partial_t+\\mathbf v\\cdot\\nabla)\\varrho=-i[\\mathsf H[\\varrho],\\varrho]+\\mathcal C[\\varrho]\\ \\leftrightarrow\\ (\\partial_t+\\mathbf v\\cdot\\nabla+\\mathbf a\\cdot\\nabla_{\\mathbf v})f=0", "breaks": "There is no momentum-space force term: refraction rotates flavor instead of accelerating particles. The nonlinearity is a flavor-space commutator rather than a velocity-space one.", "confidence": "current research", "strength": 2}
{"id": "C2360", "a": "06-particle-physics/neutrino-physics/neutrino-oscillations", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Fast flavor instability from plasma dispersion relations", "kind": "method transfer", "summary": "In supernova cores and neutron-star mergers, neutrino–neutrino forward scattering makes flavor evolution collective. Linearizing the off-diagonal flavor density matrix gives a dispersion relation whose complex roots signal the fast flavor instability, analysed like a beam–plasma instability (Izaguirre, Raffelt & Tamborra 2017). A crossing in the angular electron-lepton-number distribution plays the role of a bump-on-tail, and Landau-damping and quasilinear-saturation ideas carried over.", "map": "\\det\\Pi^{\\mu\\nu}(\\omega,\\mathbf k)=0,\\quad \\Pi^{\\mu\\nu}=\\eta^{\\mu\\nu}+\\int\\frac{d\\Gamma_{\\mathbf v}}{4\\pi}\\,G_{\\mathbf v}\\frac{v^\\mu v^\\nu}{\\omega-\\mathbf k\\cdot\\mathbf v}", "breaks": "Flavor waves are SU(N) isospin-polarization modes, not charge-density oscillations. All neutrinos move at c, so the angular distribution replaces the velocity distribution.", "confidence": "current research", "strength": 3}
{"id": "C2361", "a": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "b": "10-plasma-physics/magnetohydrodynamics/dynamo-theory", "name": "Chiral magnetic effect as an α-dynamo", "kind": "analogy", "summary": "In a plasma with chiral imbalance μ_5 (early universe, proto-neutron stars, heavy-ion collisions) the anomaly drives a current along B: the chiral magnetic effect. This current enters the induction equation exactly like the mean-field α-effect, giving a chiral dynamo (chiral plasma instability) that amplifies helical fields while the anomaly drains μ_5 (Boyarsky, Fröhlich & Ruchayskiy 2012; Rogachevskii et al. 2017).", "map": "\\mathbf J_{CME}=\\frac{e^2\\mu_5}{2\\pi^2}\\mathbf B;\\quad \\partial_t\\mathbf B=\\nabla\\times(\\mathbf v\\times\\mathbf B+\\alpha_5\\mathbf B)+\\eta\\nabla^2\\mathbf B,\\ \\alpha_5\\leftrightarrow\\alpha", "breaks": "The classical α-effect is a statistical property of helical turbulence. The chiral α is microscopic, fixed by the anomaly coefficient, and decays as chirality-flipping (electron-mass) scattering erases μ_5 at low temperature.", "confidence": "current research", "strength": 2}
{"id": "C2362", "a": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "Magnetic helicity is an abelian Chern–Simons term", "kind": "identity", "summary": "Magnetic helicity H = ∫A·B d³x is the abelian Chern–Simons functional. It measures the linking of field lines (Moffatt 1969) and is exactly conserved in ideal MHD because E·B = 0 (Woltjer 1958). Through the axial anomaly it trades with fermion chirality so that N_5 + (e²/4π²)H is conserved, the bridge behind chiral MHD and anomaly-driven baryogenesis.", "map": "H=\\int\\mathbf A\\cdot\\mathbf B\\,d^3x,\\quad \\frac{dH}{dt}=-2\\int\\mathbf E\\cdot\\mathbf B\\,d^3x,\\quad \\partial_\\mu j_5^\\mu=\\frac{e^2}{2\\pi^2}\\mathbf E\\cdot\\mathbf B", "breaks": "Classical helicity is continuous and conserved only approximately (resistivity, reconnection). Non-abelian Chern–Simons number changes by integers between topologically distinct vacua via instantons and sphalerons.", "confidence": "established", "strength": 3}
{"id": "C2363", "a": "06-particle-physics/quantum-field-theory/canonical-and-path-integral-quantization", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Field-theory action principles for Vlasov–Maxwell", "kind": "method transfer", "summary": "Vlasov–Maxwell is a classical field theory: Low (1958) gave its Lagrangian, and Morrison, Marsden and Weinstein gave its noncanonical Lie–Poisson Hamiltonian structure. Gyrokinetic field theories and structure-preserving variational particle-in-cell schemes derive from such actions, and Martin–Siggia–Rose functional integrals treat plasma-turbulence statistics with the generating-functional machinery of QFT.", "map": "", "breaks": "The Vlasov bracket is noncanonical with Casimir invariants and is never quantized. MSR integrals weight stochastic histories, not quantum amplitudes.", "confidence": "established", "strength": 1}
{"id": "C2364", "a": "06-particle-physics/quantum-field-theory/effective-field-theory", "b": "10-plasma-physics/magnetic-confinement-fusion/turbulent-transport-and-gyrokinetics", "name": "Gyrokinetics as a scale-separated effective theory", "kind": "analogy", "summary": "Gyrokinetics removes fast gyration (ω ≪ Ω_c) with a gyrophase-averaging Lie transform ordered in ρ* = ρ/L, keeps the magnetic moment as an adiabatic invariant, and adds corrections order by order. Structurally this is like integrating out a heavy scale in an EFT such as NRQED or HQET, with ρ* as the power-counting parameter.", "map": "\\epsilon\\sim\\rho_*=\\frac{\\rho_i}{L}\\sim\\frac{\\omega}{\\Omega_i}\\ \\leftrightarrow\\ \\frac{E}{\\Lambda};\\quad \\mu=\\frac{mv_\\perp^2}{2B}\\ \\text{conserved}", "breaks": "Gyrokinetics is a classical asymptotic phase-space reduction with no loops, renormalization or running couplings. Its orderings (δf/f ~ ρ*) are imposed rather than symmetry-protected, and they fail in steep edge pedestals.", "confidence": "proposed", "strength": 1}
{"id": "C2365", "a": "06-particle-physics/quantum-field-theory/effective-field-theory", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "MHD as the effective theory of a one-form symmetry", "kind": "method transfer", "summary": "With no magnetic monopoles, magnetic flux conservation is a one-form global symmetry. Grozdanov, Hofman and Iqbal (2017) recast relativistic dissipative MHD as the hydrodynamic effective theory of that symmetry, organized by a derivative expansion with symmetry-allowed transport coefficients. Frozen-in flux and Alfvén waves then follow from symmetry plus EFT power counting.", "map": "\\partial_\\mu J^{\\mu\\nu}=0,\\quad J^{\\mu\\nu}=\\tfrac12\\epsilon^{\\mu\\nu\\rho\\sigma}F_{\\rho\\sigma}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2366", "a": "06-particle-physics/quantum-field-theory/feynman-diagrams-and-scattering-amplitudes", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "Strong-field QED in the laser–plasma QED regime", "kind": "method transfer", "summary": "At intensities ≳10^23 W/cm² (a0 of a few hundred) plasma electrons reach χ ~ 1, where nonlinear Compton emission and multiphoton Breit–Wheeler pair creation dominate. Their rates are Feynman diagrams in the Furry picture with Volkov-dressed propagators, inserted as Monte Carlo processes in QED-PIC codes. SLAC E-144 first observed them in the 1990s, and Schwinger pair creation at E_S is the non-perturbative limit.", "map": "\\chi_e=\\frac{e\\hbar}{m_e^3c^4}\\sqrt{-(F_{\\mu\\nu}p^\\nu)^2},\\quad a_0=\\frac{eE}{m_ec\\,\\omega}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2367", "a": "06-particle-physics/quantum-field-theory/feynman-diagrams-and-scattering-amplitudes", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Debye-screened potential is the Yukawa potential", "kind": "identity", "summary": "A massive boson's static propagator 1/(k²+m²) Fourier-transforms to the Yukawa potential. A plasma's static longitudinal dielectric function ε(k)=1+1/(k²λ_D²) turns the Coulomb propagator into 1/(k²+λ_D⁻²), giving the same potential with λ_D in place of the Compton wavelength. Hence 'Yukawa systems' for dusty plasmas and the 'Debye mass' of thermal field theory.", "map": "\\frac{q}{4\\pi\\epsilon_0r}e^{-r/\\lambda_D}\\ \\leftrightarrow\\ \\frac{g^2}{4\\pi r}e^{-r/\\lambda_C},\\quad \\lambda_D\\leftrightarrow\\lambda_C=\\frac{\\hbar}{mc}", "breaks": "Debye screening is a collective, temperature-dependent medium effect. It applies to static longitudinal fields only (static magnetic fields are unscreened), needs N_D≫1 for linearity, and has no associated free particle; the Yukawa range comes from the rest mass of a quantum exchanged in vacuum.", "confidence": "established", "strength": 3}
{"id": "C2368", "a": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "b": "10-plasma-physics/magnetohydrodynamics/mhd-turbulence", "name": "Renormalization group for MHD turbulence", "kind": "method transfer", "summary": "Field-theory machinery moved into turbulence theory. Wyld's diagrammatic expansion, Kraichnan-type renormalized closures and Wilsonian RG were applied to randomly forced MHD (Fournier, Sulem & Pouquet 1982) and to magnetized-plasma turbulence, yielding renormalized eddy viscosity and resistivity and infrared fixed points that set inertial-range exponents.", "map": "", "breaks": "There is no small parameter (the ε-expansion is extrapolated to large ε), and mean-field anisotropy (critical balance) and intermittency are not captured.", "confidence": "established", "strength": 1}
{"id": "C2369", "a": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Vacuum polarization as screening, asymptotic freedom", "kind": "analogy", "summary": "A running coupling is a scale-dependent dielectric function. QED vacuum polarization by virtual pairs screens a bare charge so α grows at short distance, as a polarizable medium or plasma screens a test charge. In QCD, gluon self-interaction overcompensates (antiscreening), giving asymptotic freedom.", "map": "\\alpha(Q^2)=\\frac{\\alpha(\\mu^2)}{1-\\frac{\\alpha(\\mu^2)}{3\\pi}\\ln\\frac{Q^2}{\\mu^2}}\\ \\leftrightarrow\\ \\tilde\\phi(k)=\\frac{q}{\\epsilon_0k^2\\,\\epsilon(k)}", "breaks": "Plasma screening comes from real thermal charges and is exponential beyond λ_D. Vacuum screening is Lorentz-invariant, involves only virtual pairs and is merely logarithmic, so the charge is never fully screened. Equilibrium plasmas have no antiscreening counterpart.", "confidence": "established", "strength": 2}
{"id": "C2370", "a": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Coulomb logarithm by dimensional regularization", "kind": "method transfer", "summary": "The Coulomb logarithm reflects a collision integral divergent at both ends: the Boltzmann binary-collision operator diverges at large impact parameter and the Lenard–Balescu collective operator at small. Brown, Preston and Singleton (2005) continued the kinetic equations to d dimensions (Boltzmann for d>3, Lenard–Balescu for d<3) and cancelled the poles at d=3 as in dimensional regularization. This fixes ln Λ, with its constant term, for stopping power and temperature equilibration.", "map": "\\ln\\Lambda=\\ln(\\lambda_D/b_{\\min});\\ \\text{UV and IR }\\tfrac{1}{d-3}\\text{ poles cancel at }d=3", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2371", "a": "06-particle-physics/standard-model/cp-violation", "b": "10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas", "name": "Antimatter non-neutral plasmas enable CPT tests", "kind": "method transfer", "summary": "Antihydrogen for CPT-symmetry tests (ALPHA's 1S–2S line matches hydrogen to ~2×10⁻¹²) is made by merging antiproton and positron non-neutral plasmas in Penning–Malmberg traps. The process relies on one-component-plasma techniques developed for strongly magnetized, strongly coupled non-neutral plasmas: rotating-wall compression, evaporative and cyclotron cooling, and plasma-mode diagnostics.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2372", "a": "06-particle-physics/standard-model/electroweak-theory", "b": "10-plasma-physics/magnetohydrodynamics/dynamo-theory", "name": "Electroweak magnetogenesis as a dynamo seed", "kind": "mechanism", "summary": "Gradients of the Higgs-field phase during electroweak symmetry breaking can generate magnetic fields (Vachaspati 1991), and helical fields from the electroweak or QCD epochs inverse-cascade to larger scales. This is a primordial alternative to the Biermann battery for seeding galactic and cluster dynamos.", "map": "", "breaks": "With m_H = 125 GeV the Standard-Model electroweak transition is a smooth crossover, which weakens bubble-collision magnetogenesis. The surviving field strengths and coherence lengths may also be too small without strong amplification.", "confidence": "proposed", "strength": 1}
{"id": "C2373", "a": "06-particle-physics/standard-model/electroweak-theory", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Plasmon mass and the Anderson–Higgs mechanism", "kind": "historical", "summary": "Transverse electromagnetic waves in a plasma obey ω² = ω_p² + c²k², the dispersion of a massive (Proca) photon. Anderson (1963) used the plasmon and the Meissner effect to argue that a gauge field can gain mass without losing gauge invariance by absorbing the would-be Goldstone mode. Englert–Brout and Higgs made the idea relativistic in 1964, and it gives the W and Z their masses.", "map": "\\omega^2=\\omega_p^2+c^2k^2\\ \\leftrightarrow\\ E^2=m^2c^4+p^2c^2,\\quad \\hbar\\omega_p\\leftrightarrow mc^2,\\quad m_W=\\tfrac12gv", "breaks": "The plasma mass belongs to a thermal medium in a preferred frame (longitudinal and transverse modes differ) and involves no spontaneously broken symmetry: a normal plasma does not screen static magnetic fields. The electroweak mass comes from a Lorentz-invariant vacuum condensate, as in a superconductor's Meissner effect.", "confidence": "established", "strength": 3}
{"id": "C2374", "a": "06-particle-physics/standard-model/quantum-chromodynamics", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Colour Debye screening in the quark–gluon plasma", "kind": "mechanism", "summary": "Free colour charges in the quark–gluon plasma screen chromoelectric fields as electrons and ions screen a test charge, with Debye mass m_D ~ gT. Once the screening length falls below a quarkonium radius the heavy-quark pair unbinds (Matsui–Satz J/ψ suppression), and lattice Polyakov-loop correlators measure the screening.", "map": "m_D^2=g^2T^2\\left(\\frac{N_c}{3}+\\frac{N_f}{6}\\right)\\ \\leftrightarrow\\ \\lambda_D^{-2}=\\frac{n_ee^2}{\\epsilon_0k_BT}\\quad(\\text{QED: }m_D^2=e^2T^2/3)", "breaks": "Chromomagnetic fields are screened only non-perturbatively, at g²T. The coupling is not small near T_c, so perturbative m_D is unreliable, and the plasma is non-abelian, relativistic and quantum.", "confidence": "established", "strength": 3}
{"id": "C2375", "a": "06-particle-physics/standard-model/quantum-chromodynamics", "b": "10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas", "name": "Strongly coupled QGP and strongly coupled Coulomb plasmas", "kind": "analogy", "summary": "The near-perfect-fluid QGP invited comparison with classical strongly coupled plasmas. A coupling parameter Γ (potential over kinetic energy) of order 1–10 puts the sQGP in the liquid range of one-component and Yukawa plasmas. Classical colour molecular dynamics borrowed from OCP simulations reproduces liquid-like transport, and in both systems shear viscosity is lowest near the liquid–gas crossover.", "map": "\\Gamma=\\frac{\\langle q^2/4\\pi\\epsilon_0a\\rangle}{k_BT}\\ \\leftrightarrow\\ \\Gamma_{QGP}\\sim\\frac{C\\alpha_s}{aT}\\sim1\\text{–}10", "breaks": "The QGP is relativistic and quantum (its η/s ≈ 1/4π sits near a conjectured quantum bound with no classical analogue), non-abelian with confinement, and has a running coupling. Dusty plasmas are classical, abelian and strongly damped by neutral gas.", "confidence": "current research", "strength": 2}
{"id": "C2376", "a": "06-particle-physics/standard-model/quantum-chromodynamics", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Hard thermal loops are non-abelian Vlasov theory", "kind": "identity", "summary": "The leading soft-field response of a hot gauge plasma is the hard-thermal-loop effective action of Braaten–Pisarski and Frenkel–Taylor. Linearized Vlasov equations for hard colour-charged quasiparticles reproduce it exactly (Blaizot–Iancu; Kelly, Liu, Lucchesi & Manuel), including gluon plasmons with ω_pl = m_D/√3, Debye screening and Landau damping of space-like (ω<k) gluons.", "map": "(v\\cdot D_x)\\,\\delta n^a=-g\\,\\mathbf v\\cdot\\mathbf E^a\\,\\frac{dn_0}{dk},\\qquad \\omega_{pl}^2=\\frac{m_D^2}{3}", "breaks": "Covariant derivatives make the Vlasov equation non-abelian (colour precession, Wong equations). Beyond leading order, collisions and the soft magnetic scale g²T require Bödeker's effective theory or the lattice.", "confidence": "established", "strength": 3}
{"id": "C2377", "a": "06-particle-physics/standard-model/quantum-chromodynamics", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Chromo-Weibel instability and QGP isotropization", "kind": "mechanism", "summary": "A quark–gluon plasma with an anisotropic momentum distribution, as produced early in heavy-ion collisions, is unstable to magnetic-type Weibel/filamentation modes, just as anisotropic electron plasmas are (Mrówczyński; Romatschke–Strickland; Arnold, Lenaghan & Moore 2003). The chromo-Weibel instability speeds isotropization in weak-coupling bottom-up thermalization.", "map": "", "breaks": "Non-abelian self-interaction changes saturation: growth feeds a cascade to the ultraviolet rather than saturating as in an abelian plasma. At RHIC/LHC couplings its role relative to strong-coupling (holographic) isotropization is debated.", "confidence": "current research", "strength": 2}
{"id": "C2378", "a": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Axion searches as quantum sensing", "kind": "method transfer", "summary": "Axion dark matter is hunted with quantum sensors. Haloscopes convert axions into microwave photons at ν=m_ac²/h, read by near-quantum-limited Josephson amplifiers and by squeezed-state receivers that beat the standard quantum limit. Spin-precession experiments (CASPEr, magnetometer networks) look for the axion field acting as an oscillating pseudo-magnetic field on spins.", "map": "\\mathcal{L}_{a\\gamma}=g_{a\\gamma\\gamma}\\,a\\,\\mathbf E\\cdot\\mathbf B,\\quad h\\nu=m_ac^2,\\quad H_{aN}\\propto g_{aN}\\nabla a\\cdot\\boldsymbol\\sigma", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2379", "a": "06-particle-physics/beyond-the-standard-model/dark-matter-particle-candidates", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Skipper CCDs: semiconductor detectors for sub-GeV dark matter", "kind": "method transfer", "summary": "Sub-GeV dark matter scattering on electrons leaves only a few eV. SENSEI and DAMIC-M use skipper CCDs that read each pixel's charge many times to reach sub-electron noise. Silicon's band gap and pair-creation energy set the threshold, and leakage current and spurious charge are the backgrounds.", "map": "N_e\\approx1+\\left\\lfloor\\frac{E_e-E_{\\rm gap}}{\\varepsilon_{eh}}\\right\\rfloor,\\ E_{\\rm gap}\\approx1.1\\,\\mathrm{eV},\\ \\varepsilon_{eh}\\approx3.8\\,\\mathrm{eV}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2380", "a": "06-particle-physics/beyond-the-standard-model/extra-dimensions-and-hierarchy-problem", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Tabletop force sensors test sub-millimetre gravity", "kind": "method transfer", "summary": "Large extra dimensions (ADD) and light moduli predict Yukawa-like departures from Newton's inverse-square law below ~1 mm. Precision force sensors bound the strength–range (α, λ) plane: torsion balances, and increasingly atom interferometers and levitated or mechanical quantum sensors.", "map": "V(r)=-\\frac{Gm_1m_2}{r}\\left(1+\\alpha\\,e^{-r/\\lambda}\\right)", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2381", "a": "06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Magic momentum: storage-ring dynamics for g−2", "kind": "mechanism", "summary": "Muon g−2 rings run at the magic momentum (γ≈29.3, p≈3.09 GeV/c), where electrostatic-quadrupole focusing drops out of the Thomas–BMT spin precession. Residual betatron oscillations, momentum spread and pitch corrections are the beam-dynamics systematics. J-PARC's planned design instead uses an ultra-cold, low-emittance beam with no electric focusing.", "map": "\\boldsymbol\\omega_a=-\\frac{e}{m}\\left[a_\\mu\\mathbf B-\\left(a_\\mu-\\frac{1}{\\gamma^2-1}\\right)\\frac{\\boldsymbol\\beta\\times\\mathbf E}{c}\\right]", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2382", "a": "06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Muon g−2 as precision spin-precession magnetometry", "kind": "method transfer", "summary": "Muon g−2 measures an anomalous spin-precession frequency ω_a against a storage-ring field mapped at the ~0.1 ppm level or better. The field comes from pulsed proton-NMR probes calibrated to shielded-proton standards, the same phase-accumulation principle used in NMR and atomic magnetometers. Electron g−2 uses single-electron quantum-jump spectroscopy in a Penning trap.", "map": "a_\\mu=\\frac{\\omega_a}{\\tilde\\omega_p'}\\frac{\\mu_p'}{\\mu_e}\\frac{m_\\mu}{m_e}\\frac{g_e}{2},\\quad\\phi=\\gamma Bt", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2383", "a": "06-particle-physics/collider-and-experimental-particle-physics", "b": "11-interdisciplinary-physics/accelerator-physics", "name": "Colliders as accelerator-physics machines", "kind": "shared object", "summary": "Every collider measurement depends on a machine designed with accelerator physics. Magnets and RF set the energy frontier, and luminosity sets the event rate, so a process with cross section σ gives events at rate Lσ. The main collider design choices (hadron vs lepton beams, circular vs linear) are accelerator-physics trade-offs.", "map": "\\dot N=\\mathcal{L}\\,\\sigma,\\quad N_{\\rm ev}=\\sigma\\int\\mathcal{L}\\,dt", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2384", "a": "06-particle-physics/collider-and-experimental-particle-physics", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "CLOUD: accelerator beams test aerosol nucleation", "kind": "method transfer", "summary": "CERN's CLOUD experiment uses a Proton Synchrotron beam as an adjustable cosmic-ray source in an ultra-clean chamber to measure ion-induced nucleation of atmospheric aerosols. It showed that ions boost nucleation from sulphuric-acid and organic vapours. The proposed cosmic-ray–cloud–climate link is contested, and CLOUD's own modelling finds it too weak to explain recent warming.", "map": "", "breaks": "", "confidence": "current research", "strength": 1}
{"id": "C2385", "a": "06-particle-physics/collider-and-experimental-particle-physics/future-colliders", "b": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "name": "Magnet and SRF technology set future-collider reach", "kind": "shared object", "summary": "Accelerator hardware bounds future-collider designs. A ~100 TeV FCC-hh needs ~14–16 T Nb₃Sn or HTS dipoles. FCC-ee, CEPC and ILC rely on high-Q niobium SRF cavities, and CLIC relies on 70–100 MV/m normal-conducting X-band structures. In practice, magnet and cavity R&D decides collider strategy.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2386", "a": "06-particle-physics/collider-and-experimental-particle-physics/future-colliders", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Muon ionization cooling evades Liouville", "kind": "mechanism", "summary": "Muons are produced with large emittance and live 2.2 μs, so a muon collider needs ionization cooling. Energy loss in absorbers removes momentum in all directions, and RF restores only the longitudinal part, so emittance shrinks. Dissipation evades Liouville's theorem, with multiple scattering as the heating term. MICE demonstrated the effect.", "map": "\\frac{d\\epsilon_n}{ds}\\approx-\\frac{\\epsilon_n}{\\beta^2E}\\left|\\frac{dE}{ds}\\right|+\\frac{\\beta_\\perp(13.6\\,\\mathrm{MeV})^2}{2\\beta^3Em_\\mu c^2X_0}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2387", "a": "06-particle-physics/collider-and-experimental-particle-physics/future-colliders", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Synchrotron radiation: collider loss, light-source product", "kind": "identity", "summary": "Light sources turn relativistic Larmor radiation into X-ray beams, and the same radiation is the energy-loss limit of circular e⁺e⁻ colliders. The loss per turn scales as γ⁴/ρ. That is why FCC-ee and CEPC need ~90–100 km rings, why linear colliders are proposed, and why a muon collider radiates (m_e/m_μ)⁴ less.", "map": "U_0=\\frac{e^2\\gamma^4}{3\\epsilon_0\\rho},\\quad U_0[\\mathrm{keV}]\\approx88.5\\,\\frac{E^4[\\mathrm{GeV}]}{\\rho[\\mathrm{m}]}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2388", "a": "06-particle-physics/collider-and-experimental-particle-physics/future-colliders", "b": "11-interdisciplinary-physics/medical-physics/radiation-therapy", "name": "CLIC X-band structures for VHEE FLASH therapy", "kind": "method transfer", "summary": "High-gradient X-band accelerating structures developed for CLIC are being adapted into compact very-high-energy-electron (VHEE, ~100–200 MeV) machines, for example by the CERN–CHUV collaboration. These could deliver ultra-high-dose-rate FLASH radiotherapy to deep tumours.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2389", "a": "06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc", "b": "11-interdisciplinary-physics/accelerator-physics", "name": "Dipole field sets the LHC energy", "kind": "shared object", "summary": "In a fixed tunnel the dipole field sets the beam momentum. 8.33 T Nb–Ti dipoles at 1.9 K on a ~2.8 km bending radius give the design 7 TeV per beam. HL-LHC brings in Nb₃Sn magnets of the 11–12 T class, and hadron colliders beyond it are limited by magnet technology.", "map": "p\\,[\\mathrm{GeV}/c]\\approx0.3\\,B[\\mathrm{T}]\\,\\rho[\\mathrm{m}]", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2390", "a": "06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "LHC luminosity from emittance and beta*", "kind": "identity", "summary": "LHC luminosity is a beam-dynamics quantity. The beam size at the interaction point is σ*=√(εβ*), so luminosity rises with bunch intensity and falls with emittance and β*. Beam–beam tune shifts, crossing-angle geometry and pile-up limit how far it can be pushed, which is the HL-LHC problem.", "map": "\\mathcal{L}=\\frac{n_bN_b^2f_{\\rm rev}\\gamma_r}{4\\pi\\epsilon_n\\beta^*}F,\\quad\\sigma^*=\\sqrt{\\epsilon\\beta^*}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2391", "a": "06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Superconducting magnet industry: Tevatron to MRI", "kind": "historical", "summary": "Clinical MRI uses liquid-helium-cooled Nb–Ti superconducting solenoids, the same conductor technology as hadron-collider dipoles. The Tevatron, the first large superconducting synchrotron, helped create the industrial Nb–Ti cable production behind whole-body MRI magnets. LHC-era Nb₃Sn and HTS development now feeds high-field MRI.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2392", "a": "06-particle-physics/collider-and-experimental-particle-physics/machine-learning-in-hep", "b": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "name": "Symmetry-aware networks for jets and protein structures", "kind": "method transfer", "summary": "Both fields learn from point clouds whose physics has exact symmetries. Jet tagging uses Lorentz-equivariant graph networks, and AlphaFold 2 uses SE(3)-invariant point attention, so each builds the symmetry into the architecture. Diffusion and flow generative models are used both for fast detector simulation and for protein design.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2393", "a": "06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Hybrid pixel detectors from LHC trackers to X-ray beamlines", "kind": "method transfer", "summary": "Hybrid pixel detectors built for LHC tracking (CMS pixel R&D at PSI, the Medipix/Timepix chips) became the noise-free single-photon-counting X-ray detectors, such as PILATUS and EIGER, that now dominate synchrotron diffraction. FEL pulses need integrating detectors instead, because every photon arrives within femtoseconds.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2394", "a": "06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Silicon trackers are reverse-biased p–n diodes", "kind": "shared object", "summary": "Silicon strip and pixel trackers are fully depleted p–n junctions read out by CMOS electronics, so tracker design is device physics: depletion voltage, leakage current, and radiation-induced change of effective doping. Monolithic active pixel sensors such as ALICE ITS2 grew out of commercial CMOS image sensors, and LGADs add avalanche gain for timing.", "map": "W=\\sqrt{\\frac{2\\epsilon_{\\rm Si}V}{qN_{\\rm eff}}}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2395", "a": "06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Muography images geological interiors with cosmic muons", "kind": "method transfer", "summary": "Cosmic-ray muon detectors built from particle-physics technology (scintillators, emulsions, gaseous chambers) measure how much muons are attenuated through volcanoes, mountains and pyramids. The result is a map of density times path length that complements seismic tomography for near-surface structure.", "map": "X=\\int\\rho\\,dl\\ \\text{(opacity from muon survival above }E_{\\min}(X))", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C2396", "a": "06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Photon-counting pixel detectors for spectral CT", "kind": "method transfer", "summary": "Hybrid pixel readout chips from the CERN-hosted Medipix collaboration count single X-ray photons against energy thresholds. Used in CT, they give energy-resolved (spectral) images that separate tissues and contrast agents. Medipix-based MARS scanners have imaged humans, and photon-counting CT is now entering clinical use.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2397", "a": "06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "Scintillators, SiPMs and timing shared by HEP and TOF-PET", "kind": "method transfer", "summary": "A PET scanner is a coincidence-counting particle detector. Dense fast scintillators (LSO/LYSO, studied by CERN's Crystal Clear collaboration), photodetectors from PMTs to SiPMs, and picosecond timing move between the fields in both directions. TOF-PET's ~200 ps coincidence timing informed HEP crystal timing layers such as CMS LYSO+SiPM, and HEP timing R&D now aims at PET.", "map": "e^+e^-\\to2\\gamma\\ (511\\,\\mathrm{keV}),\\quad\\Delta x=\\frac{c\\,\\Delta t_{\\rm CTR}}{2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2398", "a": "06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers", "b": "11-interdisciplinary-physics/medical-physics/radiation-therapy", "name": "Bethe stopping power: dE/dx tagging and the Bragg peak", "kind": "identity", "summary": "Detectors use the Bethe formula to identify particles by ionization energy loss, and the same formula gives charged-particle therapy its Bragg peak. Wilson proposed proton therapy on this basis. HEP transport codes such as Geant4 and FLUKA are now standard for therapy dose calculation.", "map": "-\\frac{dE}{dx}\\propto\\frac{z^2}{\\beta^2}\\left[\\ln\\frac{2m_ec^2\\beta^2\\gamma^2}{I}-\\beta^2\\right]", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2399", "a": "06-particle-physics/neutrino-physics/neutrino-experiments-and-sources", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Geoneutrinos measure Earth's radiogenic heat", "kind": "shared object", "summary": "Antineutrinos from the U and Th decay chains, detected by inverse beta decay in KamLAND and Borexino (soon JUNO), directly measure radiogenic heat production in the crust and mantle. This complements seismic Earth models such as PREM on the question of what powers mantle convection and the geodynamo. ⁴⁰K antineutrinos are below the detection threshold.", "map": "\\bar\\nu_e+p\\to e^++n,\\quad E_\\nu>1.806\\,\\mathrm{MeV}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2400", "a": "06-particle-physics/neutrino-physics/neutrino-mass-and-double-beta-decay", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "SQUID-read microcalorimeters for neutrino mass", "kind": "method transfer", "summary": "Calorimetric neutrino-mass experiments embed ¹⁶³Ho in metallic magnetic calorimeters read by SQUIDs (ECHo) or in transition-edge sensors (HOLMES) to measure the electron-capture endpoint. This complements KATRIN's tritium spectrometer. Project 8 measures tritium β energies from the frequency of their cyclotron radiation.", "map": "f_c=\\frac{eB}{2\\pi\\gamma m_e}\\ (\\text{CRES}),\\quad\\Delta T=E/C\\ (\\text{calorimetry})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2401", "a": "06-particle-physics/neutrino-physics/neutrino-oscillations", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "MSW resonance as a Landau–Zener crossing", "kind": "identity", "summary": "Solar-neutrino flavour conversion is a two-level avoided crossing swept by the density gradient. It follows the same Landau–Zener hopping formula that governs nonadiabatic transitions between molecular potential-energy surfaces. Adiabatic MSW conversion is the case where the system stays on one adiabatic surface.", "map": "P_{\\rm hop}=\\exp\\left(-\\frac{\\pi}{2}\\gamma_r\\right),\\quad\\gamma_r=\\frac{\\Delta m^2\\sin^22\\theta}{2E\\cos2\\theta\\,|d\\ln n_e/dr|}", "breaks": "In molecules the crossing coordinate is a nuclear degree of freedom with its own dynamics and back-reaction, often multidimensional, with conical intersections and geometric phases. For neutrinos the solar density profile fixes the sweep and there is no back-reaction.", "confidence": "established", "strength": 3}
{"id": "C2402", "a": "06-particle-physics/neutrino-physics/neutrino-oscillations", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Neutrino oscillation tomography of Earth's core", "kind": "shared object", "summary": "Atmospheric neutrinos crossing the Earth feel an MSW matter potential set by the electron density, which seismology supplies through PREM. Turned around, future oscillation measurements and IceCube absorption data weigh the core and mantle without seismic waves. They could also constrain the core's composition through its Z/A.", "map": "V_{CC}=\\sqrt2\\,G_Fn_e,\\quad n_e=\\frac{Z}{A}\\frac{\\rho}{m_N}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2403", "a": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Instanton theory of tunnelling reaction rates", "kind": "identity", "summary": "Field theory uses a Euclidean saddle point (the instanton or bounce) for theta-vacuum tunnelling and false-vacuum decay. Chemistry uses the same saddle point in semiclassical and ring-polymer instanton rate theory for hydrogen-atom and proton-transfer tunnelling. It explains large kinetic isotope effects and low-temperature interstellar chemistry.", "map": "k\\simeq A\\,e^{-S_E[\\bar x]/\\hbar},\\quad S_E=\\int d\\tau\\left[\\tfrac12m\\dot x^2+V(x)\\right]", "breaks": "Chemical instantons are periodic orbits on a multidimensional nuclear potential surface with no topological charge. Gauge-theory instantons are classified by winding number and act on field configurations.", "confidence": "established", "strength": 3}
{"id": "C2404", "a": "06-particle-physics/quantum-field-theory/canonical-and-path-integral-quantization", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Ring polymers: imaginary-time path integrals for nuclei", "kind": "method transfer", "summary": "Wick rotation turns a quantum particle's partition function into a classical ring polymer of P beads, the same Euclidean discretization that underlies lattice field theory. Path-integral molecular dynamics and ring-polymer rate theories use it to include zero-point energy and tunnelling of light nuclei in reactions.", "map": "Z_P=\\int\\prod_k dx_k\\,e^{-\\beta_P\\sum_k[\\frac{m}{2\\beta_P^2\\hbar^2}(x_{k+1}-x_k)^2+V(x_k)]},\\ \\beta_P=\\beta/P", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2405", "a": "06-particle-physics/quantum-field-theory/feynman-diagrams-and-scattering-amplitudes", "b": "11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods", "name": "Coupled cluster: field-theory diagrams in chemistry", "kind": "historical", "summary": "Coupled-cluster theory, now quantum chemistry's gold standard as CCSD(T), was brought into chemistry by Čížek using quantum-field-theory tools. These were second quantization, Goldstone/Feynman-type diagrams, and the linked-cluster theorem that guarantees size extensivity. The exponential ansatz itself came from nuclear many-body theory.", "map": "|\\Psi\\rangle=e^{\\hat T}|\\Phi_0\\rangle,\\quad E=\\langle\\Phi_0|e^{-\\hat T}\\hat He^{\\hat T}|\\Phi_0\\rangle", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2406", "a": "06-particle-physics/quantum-field-theory/feynman-diagrams-and-scattering-amplitudes", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "PET runs on QED pair annihilation", "kind": "mechanism", "summary": "PET imaging uses the QED process e⁺e⁻→γγ: annihilation at rest gives two 511 keV photons almost back-to-back, and the pair's leftover momentum adds a small acollinearity. Positrons often form positronium first. Its para (2γ) and ortho (3γ) states have tissue-dependent lifetimes, which positronium-lifetime imaging is starting to use.", "map": "E_\\gamma=m_ec^2=511\\,\\mathrm{keV},\\quad\\tau_{p\\text{-}Ps}\\approx125\\,\\mathrm{ps},\\ \\tau_{o\\text{-}Ps}\\approx142\\,\\mathrm{ns}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2407", "a": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Geometric phase at conical intersections as a gauge field", "kind": "identity", "summary": "Adiabatically eliminating the electrons leaves the nuclei moving in a Berry connection. Around a conical intersection the electronic wavefunction changes sign, a molecular Aharonov–Bohm flux that changes vibronic spectra and reaction product distributions. Degenerate electronic manifolds give a non-abelian (Wilczek–Zee) connection with the structure of a Yang–Mills potential.", "map": "\\mathbf A_{mn}(\\mathbf R)=i\\langle m(\\mathbf R)|\\nabla_{\\mathbf R}n(\\mathbf R)\\rangle,\\quad\\oint\\mathbf A\\cdot d\\mathbf R=\\pi", "breaks": "The gauge field is emergent and kinematic. It has no Yang–Mills kinetic term or dynamics of its own, its gauge freedom is just the phase choice of the electronic states, and it exists only within the adiabatic approximation.", "confidence": "established", "strength": 2}
{"id": "C2408", "a": "06-particle-physics/quantum-field-theory/lattice-field-theory", "b": "11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods", "name": "Quantum-computing targets: lattice gauge theories and molecules", "kind": "method transfer", "summary": "On classical computers, lattice QCD at finite density or in real time runs into the fermion sign problem, and strongly correlated molecules run into exponential Hilbert-space growth. Both are therefore flagship quantum-computing applications. They share fermion-to-qubit encodings, Trotterized Hamiltonian simulation, variational eigensolvers and phase estimation.", "map": "\\langle O\\rangle=\\frac{\\int\\mathcal D\\phi\\,O\\,e^{-S[\\phi]}}{\\int\\mathcal D\\phi\\,e^{-S[\\phi]}},\\quad\\mathrm{Im}\\,S\\neq0\\Rightarrow\\text{sign problem}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2409", "a": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "b": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "name": "Membrane bending rigidity runs like an asymptotically free coupling", "kind": "analogy", "summary": "Thermal undulations make a fluid membrane's bending rigidity fall logarithmically with length scale, just as the coupling of the asymptotically free 2D nonlinear sigma model runs. The membrane persistence length plays the role of the dynamically generated mass gap.", "map": "\\kappa_R(\\ell)=\\kappa-\\frac{3k_BT}{4\\pi}\\ln\\frac{\\ell}{a},\\quad\\xi_p\\sim a\\,e^{4\\pi\\kappa/3k_BT}\\leftrightarrow\\Lambda\\sim\\mu\\,e^{-1/(b_0g^2)}", "breaks": "The fluctuations are thermal, not quantum, and early work disputed the prefactor of the logarithm. Lipid bilayers with κ≈10–20 k_BT have astronomically long persistence lengths, so real membranes never reach the crumpled, confinement-like regime.", "confidence": "established", "strength": 2}
{"id": "C2410", "a": "06-particle-physics/standard-model/cp-violation", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Electron EDM searches in polar molecules", "kind": "method transfer", "summary": "CP violation beyond the Standard Model would give the electron an electric dipole moment. Heavy polar molecules (ThO, HfF⁺, YbF) amplify it with internal effective fields of order 10–100 GV/cm. Precision molecular spin-precession spectroscopy therefore bounds new CP-violating physics at multi-TeV scales and constrains electroweak baryogenesis.", "map": "H_{\\rm EDM}=-d_e\\,\\boldsymbol\\sigma\\cdot\\boldsymbol{\\mathcal E}_{\\rm eff},\\quad\\hbar\\,\\Delta\\omega=2d_e\\mathcal{E}_{\\rm eff}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2411", "a": "06-particle-physics/standard-model/electroweak-theory", "b": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "name": "Stochastic cooling enabled the W and Z discovery", "kind": "historical", "summary": "Van der Meer's stochastic cooling senses a beam's fluctuations with a pickup and corrects them with a kicker. It made dense antiproton beams possible for CERN's SppS collider, where UA1 and UA2 found the W and Z in 1983 and directly confirmed electroweak theory.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2412", "a": "06-particle-physics/standard-model/electroweak-theory", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Parity violation in chiral molecules", "kind": "mechanism", "summary": "Z-boson exchange between electrons and nuclei should give the two mirror-image forms of a chiral molecule slightly different energies. This parity-violating energy difference is predicted to be tiny and has never been measured spectroscopically. Its proposed role in seeding biological homochirality is contested.", "map": "H_{\\rm PV}\\propto G_F\\,Q_W\\{\\boldsymbol\\sigma_e\\cdot\\mathbf p_e,\\delta^3(\\mathbf r)\\},\\quad Q_W\\approx Z(1-4\\sin^2\\theta_W)-N", "breaks": "", "confidence": "proposed", "strength": 1}
{"id": "C2413", "a": "06-particle-physics/standard-model/hadron-spectroscopy-and-exotics", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Born–Oppenheimer picture of quarkonium hybrids", "kind": "analogy", "summary": "Heavy-quark hybrids and some tetraquarks are treated like diatomic molecules. The slow heavy quark–antiquark pair plays the nuclei and the gluon and light-quark fields play the electrons. Lattice static potentials carry diatomic term symbols (Σ_g⁺, Π_u, …), and the heavy pair vibrates on them (Born–Oppenheimer EFT).", "map": "H=\\frac{p^2}{2\\mu}+V_{\\Lambda_\\eta^\\epsilon}(r),\\quad m_Q\\gg\\Lambda_{\\rm QCD}\\leftrightarrow M_{\\rm nuc}\\gg m_e", "breaks": "The scale separation is modest: gluonic excitation gaps are not much larger than charmonium level spacings. The light fields carry colour and confine, and spin and recoil corrections are much larger than in molecules.", "confidence": "current research", "strength": 2}