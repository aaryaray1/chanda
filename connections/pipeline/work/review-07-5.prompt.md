You are the nuclear-physicist, the specialist for 07 (Nuclear Physics) in this physics knowledge base.

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

## Field overview · `knowledge/07-nuclear-physics`

> **Specialist:** `nuclear-physicist` · **arXiv:** nucl-th, nucl-ex, hep-ph (QCD), astro-ph.HE · **Literature source:** INSPIRE-HEP + arXiv (OpenAlex for applied topics)

#### What this field studies
Nuclei are bound states of protons and neutrons held together by the residual strong force, a short-range remnant of QCD. Nuclear physics explains why nuclei have the masses, shapes and lifetimes they do; how stars burn and elements are made; what matter looks like at nuclear and greater densities (neutron stars, quark–gluon plasma); and how fission, fusion and radiation can be used for energy, medicine and measurement.

#### Conventions used in this branch
- Energies in MeV; lengths in fm ($10^{-15}$ m); $\hbar c=197.327$ MeV·fm; nuclear radius $R\approx1.2\,A^{1/3}$ fm.
- Nuclide notation ${}^A_ZX_N$; binding energy per nucleon $B/A\approx8$ MeV (peak ~8.8 MeV at ⁵⁶Fe/⁶²Ni).
- Cross sections in barns ($1\ \text{b}=10^{-28}$ m²); half-life $t_{1/2}=\tau\ln2$.

#### Historical spine
1896 radioactivity (Becquerel) · 1898 polonium, radium (Curies) · 1911 nucleus · 1919 first transmutation · 1928 α-decay tunnelling (Gamow; Gurney–Condon) · 1932 neutron · 1934 Fermi's β-decay theory · 1935 Yukawa pion; semi-empirical mass formula · 1938–39 fission · 1939 Bethe's stellar energy · 1942 first reactor · 1949 shell model (Mayer, Jensen) · 1957 B²FH nucleosynthesis · 1985 halo nuclei · 2000s QGP at RHIC · 2010 proton-radius puzzle; element 117 · 2017 kilonova r-process · 2022 fusion ignition at NIF.

#### Canonical textbooks
- Krane, *Introductory Nuclear Physics*; Martin, *Nuclear and Particle Physics*.
- Bohr & Mottelson, *Nuclear Structure* (2 vols.); Ring & Schuck, *The Nuclear Many-Body Problem*.
- Bertulani, *Nuclear Physics in a Nutshell*; Iliadis, *Nuclear Physics of Stars*; Yagi, Hatsuda & Miake, *Quark–Gluon Plasma*.

#### Live frontiers
- Ab initio theory reaching heavy nuclei (²⁰⁸Pb) with quantified uncertainties.
- FRIB and FAIR: the neutron drip line and r-process nuclei.
- Neutron-star equation of state from NICER radii and GW tidal deformabilities.
- The EIC (construction at Brookhaven) for gluon saturation and proton spin.

#### How the specialist works here
Start from the scales (MeV, fm), identify which degrees of freedom matter (nucleons, clusters, quarks/gluons), use conservation laws (energy, $A$, $Z$, angular momentum, parity) to constrain reactions, compute Q-values from mass excesses, and cite evaluated data (AME, NNDC/ENDF) for numbers.

## Applied nuclear physics · `knowledge/07-nuclear-physics/applied-nuclear-physics`

#### Overview
Fission supplies ~10% of the world's electricity; radioisotopes are used in millions of medical procedures each year; radiation detectors guard borders and date archaeological samples. Applied nuclear physics rests on evaluated nuclear data — cross sections, decay schemes, masses — and on understanding how radiation deposits energy in matter.

#### Key equations
$$k_{\text{eff}}=\eta f p\varepsilon P_{\text{FNL}}P_{\text{TNL}},\qquad I(x)=I_0e^{-\mu x},\qquad 1\ \text{Gy}=1\ \text{J/kg},\quad H=w_RD$$

#### Connections
- [Medical physics](knowledge/11-interdisciplinary-physics/medical-physics/README.md) · [Particle detectors](knowledge/06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers/README.md)

### Nuclear data and isotope production · `knowledge/07-nuclear-physics/applied-nuclear-physics/nuclear-data-and-isotope-production`

**Scope.** Atomic Mass Evaluation (AME), ENSDF and NUBASE decay data, ENDF/JEFF/JENDL cross-section libraries, covariance data and uncertainty, ⁹⁹Mo/⁹⁹ᵐTc supply, cyclotron production of PET isotopes (¹⁸F, ¹¹C, ⁶⁸Ga), theranostic isotopes (¹⁷⁷Lu, ²²⁵Ac), radioisotope thermoelectric generators (²³⁸Pu).

**Core ideas.**
- Applications depend on evaluated, not raw, data: experiments + theory combined with covariances.
- ⁹⁹ᵐTc (6 h half-life, 140 keV γ) is used in ~80% of nuclear-medicine imaging.
- Isotope choice balances half-life, emission type and energy, and production route.

**Key equations.**
$$A(t)=N_{\text{target}}\,\sigma\,\phi\,(1-e^{-\lambda t})\quad(\text{activation during irradiation})$$

**See also.** [Nuclear medicine and PET](knowledge/11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet/README.md)

### Nuclear reactors and energy · `knowledge/07-nuclear-physics/applied-nuclear-physics/nuclear-reactors-and-energy`

**Scope.** Criticality and $k_{\text{eff}}$, neutron life cycle, moderators (H₂O, D₂O, graphite), delayed neutrons and reactor periods, temperature feedback, LWR/PWR/BWR/CANDU, fast breeders, molten-salt and small modular reactors, decay heat (Fukushima), Chernobyl's positive void coefficient, spent fuel and transmutation, Oklo natural reactor.

**Core ideas.**
- A reactor is critical when each fission causes exactly one more on average.
- Delayed neutrons stretch the reactor time constant from ~$10^{-4}$ s to ~seconds–minutes, making control feasible.
- Negative temperature/void coefficients make reactors self-stabilizing; Chernobyl's RBMK lacked this at low power.

**Key equations.**
$$P(t)\approx P_0e^{t/T},\ T\approx\frac{\beta-\rho}{\lambda\rho}\ (\rho<\beta),\qquad \rho=\frac{k-1}{k}$$

**See also.** [Nuclear fission](knowledge/07-nuclear-physics/nuclear-reactions-and-decays/nuclear-fission/README.md)

### Radiation detection and dosimetry · `knowledge/07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry`

**Scope.** Photon interactions (photoelectric, Compton, pair production), charged-particle stopping and Bragg peak, neutron detection (³He, BF₃, scintillators), ionization chambers, proportional and Geiger counters, scintillators and photomultipliers/SiPMs, HPGe spectroscopy, Fano factor, dosimetry quantities (Gy, Sv, kerma), background radiation (~3 mSv/yr), ALARA.

**Core ideas.**
- Photon attenuation is exponential; dominant process depends on energy and $Z$.
- Energy resolution is limited by counting statistics of information carriers (better for semiconductors than scintillators).
- Equivalent dose weights absorbed dose by radiation type ($w_R=20$ for α particles).

**Key equations.**
$$\frac{\sigma_E}{E}=2.355\sqrt{\frac{F\,w}{E}},\qquad \sigma_{\text{PE}}\propto\frac{Z^{4\text{–}5}}{E^{3.5}}$$

**See also.** [Particle detectors](knowledge/06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers/README.md) · [Radiation therapy](knowledge/11-interdisciplinary-physics/medical-physics/radiation-therapy/README.md)

## Hadron and nucleon structure · `knowledge/07-nuclear-physics/hadron-and-nucleon-structure`

#### Overview
Deep inelastic scattering in 1968–69 at SLAC revealed point-like constituents inside the proton (partons = quarks and gluons). Today the proton is mapped in momentum (PDFs), position–momentum (GPDs, TMDs) and spin; its mass comes mostly from gluon dynamics; its charge radius was at the centre of a decade-long puzzle; and the EIC will image its gluon fields.

#### Key equations
$$F_2(x,Q^2)=\sum_qe_q^2\,x\,[q(x)+\bar q(x)],\qquad \frac{\partial q(x,\mu^2)}{\partial\ln\mu^2}=\frac{\alpha_s}{2\pi}\int_x^1\frac{dz}{z}P_{qq}(z)\,q\!\left(\frac xz\right)+\cdots$$

#### Open problems
- Decomposition of proton spin into quark spin, gluon spin and orbital angular momentum.
- Gluon saturation at small $x$ and the color-glass condensate.

#### Connections
- [Quantum chromodynamics](knowledge/06-particle-physics/standard-model/quantum-chromodynamics/README.md) · [Hadron colliders](knowledge/06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc/README.md)

### Electron–Ion Collider · `knowledge/07-nuclear-physics/hadron-and-nucleon-structure/electron-ion-collider`

**Scope.** EIC design (polarized electrons on polarized protons and ions up to U, $\sqrt s$ = 20–140 GeV, luminosity $10^{33-34}$ cm⁻²s⁻¹), ePIC detector, physics programme: gluon saturation, nuclear PDFs, GPDs/TMDs, spin decomposition, hadronization in nuclei; HERA legacy.

**Core ideas.**
- At small $x$ gluon densities grow until recombination balances splitting — saturation scale $Q_s^2\propto A^{1/3}x^{-\lambda}$.
- Nuclei amplify saturation effects (larger $A$), making eA collisions the cleanest probe.
- Polarized beams enable precision measurements of $\Delta G$ and orbital angular momentum.

**Key equations.**
$$Q_s^2(x,A)\sim A^{1/3}\left(\frac{x_0}{x}\right)^{\lambda},\ \lambda\approx0.3$$

**Landmark.** Accardi et al. (2016) — see [subfield landmarks](knowledge/07-nuclear-physics/hadron-and-nucleon-structure/README.md).

**See also.** [Hadron colliders](knowledge/06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc/README.md)

### Nucleon spin and form factors · `knowledge/07-nuclear-physics/hadron-and-nucleon-structure/nucleon-spin-and-form-factors`

**Scope.** EMC "spin crisis" (quarks carry ~30% of the spin), gluon polarization from RHIC, Ji sum rule and orbital angular momentum, GPDs and DVCS, TMDs and Sivers effect, Sachs form factors $G_E,G_M$, polarization-transfer vs. Rosenbluth discrepancy and two-photon exchange, muonic-hydrogen proton radius (0.84 fm) vs. older 0.88 fm.

**Core ideas.**
- Proton spin $\tfrac12=\tfrac12\Delta\Sigma+\Delta G+L_q+L_g$; quark spin is only part of the budget.
- Muonic hydrogen measures the radius ~200× more sensitively than ordinary hydrogen because the muon orbits closer.
- New electron-scattering and hydrogen data now favour the small radius — the puzzle is largely resolved.

**Key equations.**
$$\langle r_E^2\rangle=-6\frac{dG_E}{dQ^2}\Big|_{Q^2=0},\qquad J_q=\tfrac12\int x\,[H_q(x,\xi,0)+E_q(x,\xi,0)]\,dx$$

**See also.** [Atomic structure and spectroscopy](knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy/README.md) · [Precision anomalies](knowledge/06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2/README.md)

## Nuclear reactions and decays · `knowledge/07-nuclear-physics/nuclear-reactions-and-decays`

#### Overview
Unstable nuclei decay by emitting α particles (tunnelling), electrons/positrons and neutrinos (weak interaction), or photons (electromagnetic de-excitation). Reactions — from elastic scattering to fission and fusion — are characterized by Q-values, cross sections and resonances. Their measurement and modelling underlie energy production, stellar physics and nuclear technology.

#### Key equations
$$N(t)=N_0e^{-\lambda t},\qquad Q=\left(\sum m_i-\sum m_f\right)c^2,\qquad \sigma(E)=\frac{S(E)}{E}e^{-2\pi\eta},\ \eta=\frac{Z_1Z_2e^2}{4\pi\epsilon_0\hbar v}$$

#### Open problems
- The neutron-lifetime puzzle: beam (~888 s) vs. bottle (~878 s) methods disagree by ~4σ.
- Microscopic theory of fission dynamics and fragment yields.

#### Connections
- [Scattering theory](knowledge/04-quantum-physics/quantum-mechanics-core/scattering-theory/README.md) · [Flavor physics and CKM](knowledge/06-particle-physics/standard-model/flavor-physics-and-ckm/README.md) · [Fusion plasmas](knowledge/10-plasma-physics/magnetic-confinement-fusion/README.md)

### Beta decay and weak interactions · `knowledge/07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions`

**Scope.** β⁻, β⁺ and electron capture, Fermi and Gamow–Teller transitions, $ft$ values, Kurie plots and the tritium endpoint, superallowed $0^+\to0^+$ decays and $|V_{ud}|$, neutron lifetime (beam vs. bottle), parity violation (Wu), double-β decay, quenching of $g_A$.

**Core ideas.**
- Pauli's neutrino (1930) rescued energy conservation; Fermi's contact theory is the low-energy limit of $W$ exchange.
- Superallowed $ft$ values are nucleus-independent after corrections (CVC) → precise $|V_{ud}|$.
- Nuclear β decay tests CKM unitarity at the $10^{-4}$ level.

**Key equations.**
$$ft=\frac{K}{G_F^2|V_{ud}|^2(1+\Delta_R)\,2},\qquad \frac{d\Gamma}{dE_e}\propto F(Z,E_e)\,p_eE_e(E_0-E_e)^2$$

**See also.** [Electroweak theory](knowledge/06-particle-physics/standard-model/electroweak-theory/README.md) · [Neutrino mass](knowledge/06-particle-physics/neutrino-physics/neutrino-mass-and-double-beta-decay/README.md)

### Fusion reactions · `knowledge/07-nuclear-physics/nuclear-reactions-and-decays/fusion-reactions`

**Scope.** Coulomb barrier and Gamow factor, astrophysical S-factor, Gamow peak and window, thermonuclear reactivity $\langle\sigma v\rangle$, D–T, D–D, D–³He and p–¹¹B reactions, electron screening, underground measurements (LUNA), muon-catalysed fusion.

**Core ideas.**
- Fusion at stellar temperatures (keV) proceeds by tunnelling far below the barrier (~MeV).
- The Gamow peak is where the falling Maxwellian tail meets the rising tunnelling probability.
- D–T has the largest reactivity at achievable temperatures (~10–20 keV), releasing 17.6 MeV (14.1 MeV neutron).

**Key equations.**
$$\mathrm{D}+\mathrm{T}\to{}^4\mathrm{He}\,(3.5\ \text{MeV})+n\,(14.1\ \text{MeV}),\qquad E_0=\left[\left(\frac{\pi\alpha Z_1Z_2k_BT}{\sqrt2}\right)^2\mu c^2\right]^{1/3}$$

**Landmark.** Bosch & Hale (1992) — see [subfield landmarks](knowledge/07-nuclear-physics/nuclear-reactions-and-decays/README.md).

**See also.** [Tokamaks](knowledge/10-plasma-physics/magnetic-confinement-fusion/tokamaks/README.md) · [Stellar structure](knowledge/09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution/README.md)

### Nuclear fission · `knowledge/07-nuclear-physics/nuclear-reactions-and-decays/nuclear-fission`

**Scope.** Discovery (Hahn–Strassmann, Meitner–Frisch), Bohr–Wheeler liquid-drop theory, fissility, double-humped barriers and shape isomers, spontaneous vs. induced fission, asymmetric mass distributions, prompt and delayed neutrons, energy release (~200 MeV), microscopic time-dependent DFT descriptions.

**Core ideas.**
- Surface tension resists deformation; Coulomb repulsion favours it; fission occurs when deformation energy wins.
- Even-$A$ fissile nuclei (²³⁵U + n → ²³⁶U*) gain pairing energy on neutron capture, so thermal neutrons suffice.
- Delayed neutrons (~0.65% for ²³⁵U) make reactors controllable.

**Key equations.**
$$x=\frac{E_C^{(0)}}{2E_S^{(0)}}\approx\frac{Z^2/A}{50},\qquad E_{\text{fission}}\approx200\ \text{MeV}$$

**See also.** [Nuclear reactors](knowledge/07-nuclear-physics/applied-nuclear-physics/nuclear-reactors-and-energy/README.md)

### Nuclear reactions and scattering · `knowledge/07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering`

**Scope.** Kinematics and Q-values, elastic and inelastic scattering, Rutherford and Mott scattering, optical-model potentials, compound-nucleus reactions and Hauser–Feshbach theory, direct reactions (stripping, pickup, knockout), Breit–Wigner resonances, neutron capture and thermal cross sections, transfer reactions for spectroscopy.

**Core ideas.**
- Compound nucleus: projectile energy is shared, the system "forgets" its formation, decays statistically.
- Direct reactions happen in one step and probe single-particle structure.
- Neutron cross sections at thermal energies often follow $1/v$ and have sharp resonances in the eV–keV range.

**Key equations.**
$$\sigma_{\text{BW}}(E)=\frac{\pi}{k^2}g\frac{\Gamma_a\Gamma_b}{(E-E_R)^2+\Gamma^2/4},\qquad Q=T_f-T_i$$

**See also.** [Scattering theory](knowledge/04-quantum-physics/quantum-mechanics-core/scattering-theory/README.md) · [Nuclear data](knowledge/07-nuclear-physics/applied-nuclear-physics/nuclear-data-and-isotope-production/README.md)

### Radioactive decay and alpha decay · `knowledge/07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay`

**Scope.** Decay constants and half-lives, activity (Bq), Bateman equations and secular equilibrium, radiometric dating, Gamow tunnelling theory of α decay, Geiger–Nuttall law, cluster radioactivity, γ decay and multipolarity, internal conversion, isomers (²²⁹ᵐTh nuclear clock), electron capture.

**Core ideas.**
- Decay is memoryless: constant probability per unit time.
- α-decay half-lives span >20 orders of magnitude for a factor ~2 change in energy — exponential sensitivity of tunnelling.
- In a chain, daughters reach secular equilibrium with a long-lived parent: $\lambda_1N_1=\lambda_2N_2$.

**Key equations.**
$$t_{1/2}=\frac{\ln2}{\lambda},\qquad \log_{10}t_{1/2}=a\frac{Z}{\sqrt{Q_\alpha}}+b\ (\text{Geiger–Nuttall}),\qquad P\approx e^{-2\int_R^{r_c}\sqrt{2\mu(V-E)}\,dr/\hbar}$$

**See also.** [Exactly solvable systems (tunnelling)](knowledge/04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems/README.md) · [Superheavy elements](knowledge/07-nuclear-physics/nuclear-structure/superheavy-elements/README.md)

## Nuclear structure · `knowledge/07-nuclear-physics/nuclear-structure`

#### Overview
Nuclear structure explains masses, radii, spins, shapes and excitations of ~3300 known nuclides (of perhaps 7000–8000 bound ones). Two pictures coexist: independent nucleons in a mean field (shell model, with magic numbers 2, 8, 20, 28, 50, 82, 126) and collective motion of the whole nucleus (rotations, vibrations, deformation). Modern theory derives both from nuclear forces rooted in QCD.

#### Key equations
$$B(A,Z)=a_VA-a_SA^{2/3}-a_C\frac{Z(Z-1)}{A^{1/3}}-a_A\frac{(A-2Z)^2}{A}+\delta(A,Z),\qquad V(r)\sim-g^2\frac{e^{-m_\pi r}}{r}$$

#### Open problems
- Where exactly is the neutron drip line beyond oxygen/fluorine/neon?
- Three-nucleon forces and their role in saturation and shell evolution.

#### Connections
- [Effective field theory](knowledge/06-particle-physics/quantum-field-theory/effective-field-theory/README.md) · [Neutron-star equation of state](knowledge/07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state/README.md)

### Ab initio nuclear theory · `knowledge/07-nuclear-physics/nuclear-structure/ab-initio-nuclear-theory`

**Scope.** Green's function Monte Carlo and AFDMC, no-core shell model, coupled-cluster theory, in-medium similarity renormalization group (IMSRG), self-consistent Green's functions, nuclear lattice EFT, similarity RG softening of interactions, emulators and Bayesian uncertainty quantification, reach to ²⁰⁸Pb.

**Core ideas.**
- Exact methods scale exponentially; polynomially scaling methods (CC, IMSRG) extended reach from light to heavy nuclei.
- Softened (SRG-evolved) interactions improve convergence but induce many-body forces.
- Uncertainty quantification has become central: predictions come with theory error bars.

**Key equations.**
$$H=\sum_i\frac{p_i^2}{2m}+\sum_{i<j}V_{ij}+\sum_{i<j<k}V_{ijk},\qquad \frac{dH_s}{ds}=[\eta_s,H_s]\ (\text{SRG/IMSRG})$$

**See also.** [Quantum chemistry methods (coupled cluster)](knowledge/11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods/README.md) · [Monte Carlo methods](knowledge/00-foundations/computational-physics/monte-carlo-methods/README.md)

### Exotic nuclei and drip lines · `knowledge/07-nuclear-physics/nuclear-structure/exotic-nuclei-and-drip-lines`

**Scope.** Neutron halos (¹¹Li, ¹¹Be), two-proton radioactivity, island of inversion near $N=20$, new magic numbers ($N=32,34$), disappearance of $N=28$ shell closure, drip-line locations (known to $Z\approx10$ for neutrons), radioactive beams at FRIB, RIKEN RIBF, FAIR, ISOLDE.

**Core ideas.**
- Weakly bound neutrons tunnel far beyond the core: ¹¹Li is as large as ²⁰⁸Pb.
- Shell gaps evolve with neutron excess because of tensor and three-nucleon forces.
- The neutron drip line is far from stability and largely unexplored above $Z\approx10$ — critical for r-process modelling.

**Key equations.**
$$S_n=B(A,Z)-B(A-1,Z),\qquad \text{drip line: }S_n\to0$$

**Landmark.** Tanihata et al. (1985) — see [subfield landmarks](knowledge/07-nuclear-physics/nuclear-structure/README.md).

**See also.** [r-process](knowledge/07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process/README.md)

### Shell model and collective models · `knowledge/07-nuclear-physics/nuclear-structure/shell-model-and-collective-models`

**Scope.** Mean-field potentials (Woods–Saxon, harmonic oscillator), strong spin–orbit splitting and magic numbers, configuration-interaction shell model, pairing and odd–even effects, liquid-drop model, Bohr–Mottelson collective model, rotational bands ($E\propto J(J+1)$), shape coexistence, Nilsson model, energy density functionals.

**Core ideas.**
- Spin–orbit coupling (Mayer, Haxel–Jensen–Suess) reproduces magic numbers beyond 20.
- Deformed nuclei rotate collectively; spectra follow $E_J=\frac{\hbar^2}{2\mathcal I}J(J+1)$.
- Pairing makes even–even ground states $0^+$ and produces odd–even mass staggering.

**Key equations.**
$$V(r)=-\frac{V_0}{1+e^{(r-R)/a}}+V_{ls}(r)\,\mathbf l\cdot\mathbf s,\qquad \frac{E(4^+)}{E(2^+)}=\frac{10}{3}\ (\text{rigid rotor})$$

**Landmark.** Mayer (1949) — see [subfield landmarks](knowledge/07-nuclear-physics/nuclear-structure/README.md).

**See also.** [Angular momentum coupling](knowledge/04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin/README.md)


---

# Packet 07-5 (38 records)

{"id": "C2556", "a": "07-nuclear-physics/nuclear-reactions-and-decays/fusion-reactions", "b": "10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas", "name": "Pycnonuclear fusion in strongly coupled plasmas", "kind": "mechanism", "summary": "In white-dwarf interiors and accreted neutron-star crusts (Gamma >> 1) fusion proceeds by zero-point tunnelling between neighbouring lattice ions; the enhancement factors are computed with one-component-plasma Monte Carlo free energies.", "map": "\\Gamma=\\frac{Z^2e^2}{4\\pi\\epsilon_0ak_BT}\\gg1;\\ \\ln f=\\frac{F_{\\rm ex}(Z_1)+F_{\\rm ex}(Z_2)-F_{\\rm ex}(Z_1+Z_2)}{k_BT}", "breaks": "Pycnonuclear rates are uncertain by orders of magnitude because of lattice dynamics, impurities and quantum effects.", "confidence": "established", "strength": 2}
{"id": "C2557", "a": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "Laser-plasma ion and neutron sources for nuclear physics", "kind": "method transfer", "summary": "Intense laser-plasma interactions accelerate MeV ions and produce bremsstrahlung and neutron bursts that drive nuclear reactions, isotope production and photonuclear experiments with ultrashort, ultradense pulses.", "map": "E_{\\max}^{\\rm TNSA}\\sim2T_{\\rm hot}\\ln^2(\\cdots),\\ T_{\\rm hot}\\approx m_ec^2(\\sqrt{1+a_0^2/2}-1)", "breaks": "Laser-driven beams have broad spectra and low repetition rates compared with accelerators.", "confidence": "current research", "strength": 1}
{"id": "C2558", "a": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "b": "10-plasma-physics/magnetic-confinement-fusion/burning-plasmas-and-iter", "name": "Tritium breeding and neutron transport in blankets", "kind": "mechanism", "summary": "A D-T power plant must breed its tritium from lithium blankets: 6Li(n,t)alpha and 7Li(n,n't)alpha cross sections, neutron multiplication by Be or Pb (n,2n) and transport set the tritium breeding ratio, which must exceed 1.", "map": "^6\\mathrm{Li}+n\\to\\mathrm T+\\alpha+4.8\\ \\text{MeV};\\ \\mathrm{TBR}=\\frac{\\dot N_{\\rm T,bred}}{\\dot N_{\\rm T,burned}}>1.05", "breaks": "Blanket designs depend on evaluated cross sections with nontrivial uncertainties for 14 MeV neutrons and on engineering coverage losses.", "confidence": "established", "strength": 2}
{"id": "C2559", "a": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "b": "10-plasma-physics/magnetohydrodynamics/magnetic-reconnection", "name": "Nuclear gamma-ray lines from flare-accelerated ions", "kind": "mechanism", "summary": "Reconnection-accelerated protons and alphas in solar flares hit the solar atmosphere and excite nuclear lines (4.44 MeV 12C, 6.13 MeV 16O) and the 2.223 MeV neutron-capture line, which measure the ion spectrum and composition of reconnection acceleration.", "map": "p+{}^{12}\\mathrm C\\to p'+{}^{12}\\mathrm C^*(4.44);\\ n+p\\to d+\\gamma(2.223\\ \\text{MeV})", "breaks": "Line yields fold together acceleration, transport and target geometry, so the inferred ion spectrum is model-dependent.", "confidence": "established", "strength": 2}
{"id": "C2560", "a": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "BUU/Vlasov transport for heavy-ion reactions", "kind": "method transfer", "summary": "Intermediate-energy heavy-ion collisions are simulated with Boltzmann-Uehling-Uhlenbeck transport: a Vlasov equation in the nuclear mean field plus a Pauli-blocked collision term; giant resonances appear as nuclear zero sound with Landau damping.", "map": "\\partial_tf+\\frac{\\mathbf p}{m}\\cdot\\nabla_rf-\\nabla_rU[f]\\cdot\\nabla_pf=I_{\\rm coll}[f(1-f)]", "breaks": "Nuclear transport uses a self-consistent short-range mean field rather than long-range Coulomb fields, and Pauli blocking with quantum fluctuations makes it semiclassical at best.", "confidence": "established", "strength": 3}
{"id": "C2561", "a": "07-nuclear-physics/nuclear-structure/exotic-nuclei-and-drip-lines", "b": "10-plasma-physics/low-temperature-and-applied-plasmas/plasma-discharges-and-processing", "name": "ECR plasma ion sources for radioactive beams", "kind": "method transfer", "summary": "Electron-cyclotron-resonance plasma ion sources and charge breeders produce the highly charged ions that drive and reaccelerate radioactive-beam facilities (FRIB, ISOLDE), applying magnetized discharge plasma physics to exotic-nucleus production.", "map": "\\omega=\\omega_{ce}=\\frac{eB}{m_e};\\ n_e\\tau_i\\ \\text{sets attainable charge state}", "breaks": "ECR sources are engineered for high charge states, a regime far from processing plasmas.", "confidence": "established", "strength": 1}
{"id": "C2562", "a": "07-nuclear-physics/applied-nuclear-physics", "b": "11-interdisciplinary-physics/medical-physics", "name": "Applied nuclear physics underpins medical physics", "kind": "method transfer", "summary": "Radiotherapy, nuclear medicine and radiation protection rest on nuclear data, radiation-matter interactions and detector physics developed in applied nuclear physics.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2563", "a": "07-nuclear-physics/applied-nuclear-physics/nuclear-data-and-isotope-production", "b": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "name": "Medical cyclotrons and isotope production", "kind": "method transfer", "summary": "Lawrence's cyclotron was built for nuclear reactions and today's compact medical cyclotrons and linacs make PET and SPECT isotopes; yields follow from excitation functions, beam current and target stopping power.", "map": "Y=\\frac{I}{ze}\\frac{N_A\\rho}{A}\\int_{E_{\\rm out}}^{E_{\\rm in}}\\frac{\\sigma(E)}{dE/dx}dE;\\ f_{\\rm cyc}=\\frac{qB}{2\\pi m}", "breaks": "Target cooling and chemistry, not beam physics, often limit practical yields.", "confidence": "established", "strength": 3}
{"id": "C2564", "a": "07-nuclear-physics/applied-nuclear-physics/nuclear-data-and-isotope-production", "b": "11-interdisciplinary-physics/applied-and-device-physics/energy-materials-and-thermoelectrics", "name": "Radioisotope thermoelectric generators", "kind": "method transfer", "summary": "RTGs convert 238Pu alpha-decay heat (0.57 W/g, 87.7 yr half-life) into electricity with thermoelectric couples; mission power follows from the decay law multiplied by the thermoelectric efficiency set by ZT.", "map": "P_{\\rm el}(t)=\\eta_{\\rm TE}P_0e^{-\\lambda t},\\ \\eta_{\\rm TE}=\\frac{T_h-T_c}{T_h}\\frac{\\sqrt{1+ZT}-1}{\\sqrt{1+ZT}+T_c/T_h}", "breaks": "Thermocouple degradation, not only isotope decay, sets RTG lifetime.", "confidence": "established", "strength": 2}
{"id": "C2565", "a": "07-nuclear-physics/applied-nuclear-physics/nuclear-data-and-isotope-production", "b": "11-interdisciplinary-physics/medical-physics", "name": "Evaluated nuclear data for medical applications", "kind": "method transfer", "summary": "Medical isotope choice, activity calculations and dose models need evaluated half-lives, decay schemes, emission spectra and production cross sections from nuclear data libraries.", "map": "A(t)=N_{\\rm target}\\sigma\\phi(1-e^{-\\lambda t})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2566", "a": "07-nuclear-physics/applied-nuclear-physics/nuclear-data-and-isotope-production", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "Isotope production for nuclear medicine and PET", "kind": "mechanism", "summary": "PET and SPECT depend on producing short-lived isotopes (18F, 11C, 68Ga, 99mTc) and theranostic pairs (177Lu, 225Ac) through reactions chosen by cross section, yield, purity and half-life.", "map": "^{18}\\mathrm O(p,n)^{18}\\mathrm F\\ (t_{1/2}=110\\ \\text{min});\\ ^{99}\\mathrm{Mo}\\to{}^{99m}\\mathrm{Tc}\\ (6\\ \\text{h},\\ 140\\ \\text{keV})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2567", "a": "07-nuclear-physics/applied-nuclear-physics/nuclear-reactors-and-energy", "b": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "name": "Accelerator-driven subcritical systems", "kind": "method transfer", "summary": "A high-power proton accelerator driving a spallation target can sustain a subcritical reactor (k_eff < 1) for transmutation of minor actinides, so beam reliability replaces delayed-neutron control.", "map": "P_{\\rm th}\\propto\\frac{k_{\\rm eff}}{1-k_{\\rm eff}}\\frac{I_pY_{\\rm sp}E_f}{\\nu};\\ Y_{\\rm sp}\\approx30\\ n/p\\ \\text{at 1 GeV}", "breaks": "Beam trips cause thermal cycling, and accelerator reliability requirements are beyond present machines.", "confidence": "current research", "strength": 1}
{"id": "C2568", "a": "07-nuclear-physics/applied-nuclear-physics/nuclear-reactors-and-energy", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "Reactor production of 99Mo and supply security", "kind": "shared object", "summary": "Most 99Mo for 99mTc generators comes from fission of uranium targets in a handful of research reactors; reactor outages caused global shortages and drove conversion to low-enriched targets and accelerator routes.", "map": "^{235}\\mathrm U(n,f)\\to{}^{99}\\mathrm{Mo}\\ (Y\\approx6.1\\%),\\ t_{1/2}=66\\ \\text{h}", "breaks": "Supply is a logistics and policy issue as much as a nuclear-physics one.", "confidence": "established", "strength": 2}
{"id": "C2569", "a": "07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry", "b": "11-interdisciplinary-physics/medical-physics", "name": "Radiation detection and dosimetry in the clinic", "kind": "method transfer", "summary": "Clinical dosimetry (ionization chambers, calibration protocols, Gy and Sv) and imaging detectors are nuclear radiation-detection physics applied to patients.", "map": "D=\\frac{dE}{dm},\\ H=w_RD", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2570", "a": "07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Photon-interaction physics and detectors in CT", "kind": "method transfer", "summary": "CT contrast and dual-energy material decomposition use the same photoelectric versus Compton Z-dependence that governs nuclear gamma spectroscopy, and photon-counting CT uses CdTe detectors from radiation-detection physics.", "map": "\\mu(E)=\\rho N_A/A\\,[\\sigma_{\\rm PE}(Z,E)+\\sigma_C(E)],\\ \\sigma_{\\rm PE}\\propto Z^{4\\text{–}5}E^{-3.5}", "breaks": "Clinical CT energies (20-140 keV) sit below most nuclear gamma lines, and image quality is set by reconstruction and dose trade-offs.", "confidence": "established", "strength": 2}
{"id": "C2571", "a": "07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "PET and SPECT detectors are nuclear gamma detectors", "kind": "method transfer", "summary": "Gamma cameras and PET scanners use scintillators (LSO/LYSO, NaI), photomultipliers or SiPMs and coincidence timing from nuclear spectroscopy; time-of-flight PET localizes annihilation along the line of response.", "map": "\\Delta x=\\frac{c\\,\\Delta t}{2};\\ \\frac{\\sigma_E}{E}\\propto\\frac{1}{\\sqrt{N_{\\rm phe}}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2572", "a": "07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry", "b": "11-interdisciplinary-physics/medical-physics/radiation-therapy", "name": "Bragg peak and dosimetry in radiation therapy", "kind": "mechanism", "summary": "Charged-particle stopping (Bethe formula, Bragg peak) and photon interaction physics determine depth-dose curves; dosimetry calibration underlies treatment delivery.", "map": "-\\frac{dE}{dx}\\propto\\frac{z^2Z}{A\\beta^2}\\left[\\ln\\frac{2m_ec^2\\beta^2\\gamma^2}{I}-\\beta^2\\right];\\ R_{\\rm CSDA}\\approx0.0022E^{1.77}\\ \\text{cm}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2573", "a": "07-nuclear-physics/hadron-and-nucleon-structure/electron-ion-collider", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "EIC accelerator design: crab cavities, cooling, polarization", "kind": "method transfer", "summary": "Reaching 1e34 luminosity with polarized beams at the EIC requires beam-dynamics advances: crab-crossing to recover luminosity at a large crossing angle, strong hadron cooling against intra-beam scattering, and spin-preserving lattices.", "map": "\\mathcal L=\\frac{fn_bN_eN_p}{4\\pi\\sigma_x\\sigma_y}H_{hg};\\ \\theta_c=25\\ \\text{mrad compensated by crab cavities}", "breaks": "Physics goals impose polarization and acceptance constraints that conflict with pure luminosity optimization.", "confidence": "current research", "strength": 2}
{"id": "C2574", "a": "07-nuclear-physics/hadron-and-nucleon-structure/nucleon-spin-and-form-factors", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Spin dynamics of polarized beams", "kind": "method transfer", "summary": "Proton-spin measurements need polarized beams kept polarized through acceleration; spin precession follows the Thomas-BMT equation, depolarizing resonances occur when the spin tune G gamma meets betatron or orbit harmonics, and Siberian snakes cancel them at RHIC.", "map": "\\frac{d\\mathbf S}{dt}=\\frac{e}{\\gamma m}\\mathbf S\\times\\left[(1+G\\gamma)\\mathbf B_\\perp+(1+G)\\mathbf B_\\parallel\\right];\\ G\\gamma=k\\pm Q_y", "breaks": "Spin and orbit dynamics are coupled nonlinearly; the analogy to betatron resonances holds only near isolated resonances.", "confidence": "established", "strength": 2}
{"id": "C2575", "a": "07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "Positron emission physics sets PET resolution", "kind": "mechanism", "summary": "PET imaging is beta-plus decay followed by positron thermalization and annihilation; the beta endpoint energy sets the positron range (18F 0.6 mm vs 82Rb ~6 mm) and residual momentum gives annihilation non-collinearity, the two physical limits on PET resolution.", "map": "\\frac{d\\Gamma}{dE_e}\\propto F(-Z,E)p_eE_e(E_0-E_e)^2;\\ \\delta\\theta\\approx0.5^\\circ\\Rightarrow\\delta x\\approx0.0022D", "breaks": "The positron range depends on tissue density and on the full beta spectrum, not only the endpoint.", "confidence": "established", "strength": 3}
{"id": "C2576", "a": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-fission", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Fission rates as transition-state and Kramers escape", "kind": "identity", "summary": "The Bohr-Wheeler fission width is transition-state theory over the fission saddle, and Kramers' escape-rate theory of chemical reactions, applied to nuclear viscosity, explains measured fission delays and pre-scission neutron excess.", "map": "\\Gamma_f^{BW}=\\frac{1}{2\\pi\\rho(E)}\\int\\rho^*(E-B_f-\\epsilon)d\\epsilon\\ \\leftrightarrow\\ k_{\\rm TST};\\ \\Gamma_K=\\Gamma_{BW}\\left(\\sqrt{1+\\gamma^2}-\\gamma\\right)", "breaks": "Nuclear dissipation is one-body (wall friction) and temperature-dependent, and the 'reaction coordinate' is a collective shape, not an atomic distance.", "confidence": "established", "strength": 3}
{"id": "C2577", "a": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "b": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "name": "Neutron scattering contrast variation in biophysics", "kind": "method transfer", "summary": "The opposite-sign coherent scattering lengths of H and D let small-angle neutron scattering and neutron crystallography 'match out' parts of protein complexes and membranes and locate hydrogen atoms and protonation states.", "map": "b_{\\rm H}=-3.74\\ \\text{fm},\\ b_{\\rm D}=+6.67\\ \\text{fm};\\ \\Delta\\rho=\\rho_{\\rm molecule}-\\rho_{\\rm solvent}(x_{D_2O})", "breaks": "Large incoherent scattering from hydrogen adds background, and deuteration can perturb biological samples.", "confidence": "established", "strength": 2}
{"id": "C2578", "a": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Compound-nucleus evaporation and RRKM unimolecular decay", "kind": "analogy", "summary": "Weisskopf's statistical evaporation of compound nuclei and RRKM theory of unimolecular dissociation share one structure: decay rates are ratios of level densities of transition and parent states, and both show Ericson-type fluctuations when levels overlap.", "map": "\\Gamma_c=\\frac{1}{2\\pi\\rho_C(E)}\\sum\\int T_c(\\epsilon)\\rho_R(E-S-\\epsilon)d\\epsilon\\ \\leftrightarrow\\ k(E)=\\frac{N^\\ddagger(E-E_0)}{h\\rho(E)}", "breaks": "Nuclear level densities come from fermionic excitations with pairing and shells; molecular ones are vibrational and rotational, with conservation of angular momentum handled differently.", "confidence": "established", "strength": 2}
{"id": "C2579", "a": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "b": "11-interdisciplinary-physics/chemical-physics/surface-science-and-catalysis", "name": "Ion-beam analysis of surfaces and thin films", "kind": "method transfer", "summary": "Rutherford backscattering, elastic recoil detection, nuclear reaction analysis (15N resonance for hydrogen) and PIXE use nuclear scattering and reactions to measure surface composition and depth profiles quantitatively.", "map": "K=\\left[\\frac{\\sqrt{M_2^2-M_1^2\\sin^2\\theta}+M_1\\cos\\theta}{M_1+M_2}\\right]^2;\\ ^1\\mathrm H(^{15}\\mathrm N,\\alpha\\gamma)^{12}\\mathrm C\\ \\text{at }6.385\\ \\text{MeV}", "breaks": "Depth resolution is limited by energy straggling, and lateral resolution is poor compared with scanning probes.", "confidence": "established", "strength": 2}
{"id": "C2580", "a": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "b": "11-interdisciplinary-physics/medical-physics/radiation-therapy", "name": "Boron neutron capture therapy", "kind": "mechanism", "summary": "BNCT delivers a thermal-neutron field to tumours loaded with 10B; the 10B(n,alpha)7Li reaction deposits ~2.3 MeV within one cell diameter, so the nuclear cross section and short ion ranges give cellular-level targeting.", "map": "^{10}\\mathrm B+n_{\\rm th}\\to{}^7\\mathrm{Li}+\\alpha+2.31\\ \\text{MeV}\\ (94\\%);\\ \\sigma_{\\rm th}=3840\\ \\text{b};\\ R_\\alpha\\approx9\\ \\mu\\text{m}", "breaks": "Clinical dose depends on boron biodistribution and accelerator-based epithermal neutron sources rather than on nuclear data alone.", "confidence": "established", "strength": 2}
{"id": "C2581", "a": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "b": "11-interdisciplinary-physics/medical-physics/radiation-therapy", "name": "Nuclear interactions in proton and ion therapy", "kind": "mechanism", "summary": "Therapeutic proton and carbon beams undergo nuclear reactions that fragment the beam, deposit dose beyond the Bragg peak and produce prompt gammas and positron emitters (11C, 15O) used for in-vivo range verification.", "map": "^{16}\\mathrm O(p,pn)^{15}\\mathrm O,\\ ^{12}\\mathrm C(p,pn)^{11}\\mathrm C;\\ \\text{prompt }\\gamma:\\ 4.44,\\ 6.13\\ \\text{MeV}", "breaks": "Nuclear cross sections for therapy-relevant fragments are known only to 10-20 percent, limiting range-verification accuracy.", "confidence": "established", "strength": 2}
{"id": "C2582", "a": "07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Nuclear resonant scattering at synchrotrons and XFELs", "kind": "method transfer", "summary": "Synchrotron radiation replaced radioactive sources for Mössbauer spectroscopy (nuclear forward scattering, 57Fe at 14.4 keV), and an XFEL resonantly excited the 12.4 keV clock isomer of 45Sc, bringing narrow nuclear transitions into X-ray quantum optics.", "map": "\\Gamma_{\\rm nuc}\\sim\\text{neV}\\ \\text{vs}\\ \\Delta E_{\\rm SR}\\sim\\text{meV};\\ \\text{time-gating separates delayed nuclear signal}", "breaks": "Only a few low-lying isomers are accessible, and the photon flux in a neV bandwidth is tiny.", "confidence": "current research", "strength": 2}
{"id": "C2583", "a": "07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Alpha-particle soft errors in integrated circuits", "kind": "mechanism", "summary": "Alpha particles from trace U and Th in chip packaging and solder deposit charge along their tracks and flip memory bits, a reliability problem found in 1979; cosmic-ray neutrons cause the same single-event upsets via nuclear recoils.", "map": "Q_{\\rm dep}=\\frac{e\\,\\Delta E}{3.6\\ \\text{eV}}\\ \\text{(Si)};\\ \\text{upset if }Q_{\\rm coll}>Q_{\\rm crit}\\sim\\text{fC}", "breaks": "Upset rates depend on device geometry and charge collection, which scale differently at each technology node.", "confidence": "established", "strength": 2}
{"id": "C2584", "a": "07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Radiocarbon, Suess effect and cosmogenic climate proxies", "kind": "method transfer", "summary": "Dilution of atmospheric 14C by fossil carbon (the Suess effect) fingerprints fossil-fuel CO2, and cosmogenic 14C and 10Be records reconstruct past solar activity for climate attribution.", "map": "^{14}\\mathrm N(n,p)^{14}\\mathrm C;\\ \\Delta^{14}\\mathrm C\\ \\text{falls as fossil (14C-free) CO}_2\\ \\text{is added}", "breaks": "Cosmogenic production also depends on the geomagnetic field and on carbon-cycle exchange, which must be modelled.", "confidence": "established", "strength": 2}
{"id": "C2585", "a": "07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics", "name": "Radioactive tracers of ocean circulation", "kind": "method transfer", "summary": "Bomb-produced 14C and tritium-3He ages and natural radiocarbon measure ocean ventilation and deep-water ages (about 1000 yr for the deep Pacific), constraining overturning circulation and ocean heat and carbon uptake.", "map": "\\tau=\\frac{1}{\\lambda}\\ln\\left(1+\\frac{[^3\\mathrm{He}]}{[^3\\mathrm H]}\\right),\\ t_{1/2}(^3\\mathrm H)=12.3\\ \\text{yr};\\ t_{1/2}(^{14}\\mathrm C)=5730\\ \\text{yr}", "breaks": "Tracer ages are mixtures of water-mass ages, so interpretation needs transit-time distributions.", "confidence": "established", "strength": 2}
{"id": "C2586", "a": "07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Geoneutrinos and Earth's radiogenic heat", "kind": "shared object", "summary": "Decays of 238U, 232Th and 40K supply roughly half of Earth's ~47 TW surface heat flow, driving mantle convection and the geodynamo; KamLAND and Borexino geoneutrino fluxes measure this budget directly.", "map": "H_{\\rm rad}=\\sum_iN_i\\lambda_iQ_i^{\\rm heat};\\ \\bar\\nu_e+p\\to e^++n\\ (E_{\\rm th}=1.8\\ \\text{MeV, misses }^{40}\\text{K})", "breaks": "Inverse beta decay cannot see 40K neutrinos, and mantle versus crust contributions remain uncertain.", "confidence": "established", "strength": 2}
{"id": "C2587", "a": "07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "Decay chains in generators and alpha theranostics", "kind": "mechanism", "summary": "Radionuclide generators (99Mo/99mTc, 68Ge/68Ga) work by transient or secular equilibrium in Bateman decay chains, and targeted alpha therapy with 225Ac must track recoiling daughters along the decay chain.", "map": "A_2(t)=\\frac{\\lambda_2}{\\lambda_2-\\lambda_1}A_1(0)\\left(e^{-\\lambda_1t}-e^{-\\lambda_2t}\\right);\\ \\lambda_1\\ll\\lambda_2\\Rightarrow A_2\\to A_1", "breaks": "Daughter recoil energies (~100 keV) break chemical bonds, so the chain can leave the targeting molecule, which simple Bateman bookkeeping ignores.", "confidence": "established", "strength": 3}
{"id": "C2588", "a": "07-nuclear-physics/nuclear-structure/ab-initio-nuclear-theory", "b": "11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods", "name": "Coupled cluster: from nuclei to chemistry and back", "kind": "historical", "summary": "Coupled-cluster theory was invented for nuclear matter (Coester, Kümmel), developed into the gold standard of quantum chemistry (Cizek, CCSD(T)), and returned to nuclear physics for medium-mass nuclei with chiral forces.", "map": "|\\Psi\\rangle=e^{T}|\\Phi_0\\rangle,\\ T=T_1+T_2+\\cdots;\\ \\langle\\Phi_{ij}^{ab}|e^{-T}He^{T}|\\Phi_0\\rangle=0", "breaks": "Nuclear CC must handle three-nucleon forces and self-bound centre-of-mass motion, while chemistry has a fixed nuclear frame and Coulomb-only interactions.", "confidence": "established", "strength": 3}
{"id": "C2589", "a": "07-nuclear-physics/nuclear-structure/exotic-nuclei-and-drip-lines", "b": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "name": "Radioactive-beam facilities as accelerator systems", "kind": "method transfer", "summary": "Exotic-nucleus research is enabled by accelerator technology: FRIB's superconducting heavy-ion linac, projectile-fragment separators and ISOL post-accelerators deliver drip-line nuclei at rates set by beam power and separator acceptance.", "map": "B\\rho=\\frac{p}{q}\\ [\\text{T m}]=3.3356\\frac{p\\,[\\text{GeV}/c]}{q/e};\\ \\text{FRIB: }400\\ \\text{kW},\\ 200\\ \\text{MeV/u U}", "breaks": "Production cross sections, not accelerator physics, set the ultimate reach toward the drip line.", "confidence": "established", "strength": 2}
{"id": "C2590", "a": "07-nuclear-physics/nuclear-structure/exotic-nuclei-and-drip-lines", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Halo nuclei and helium trimers: weak-binding universality", "kind": "mechanism", "summary": "Two-neutron halo nuclei (6He, 11Li) and the helium dimer and trimer are both governed by large scattering lengths, so their sizes and Efimov-type three-body states follow universal few-body laws; the excited He trimer is an observed Efimov state.", "map": "\\langle r^2\\rangle\\approx\\frac{\\hbar^2}{4\\mu S_n}\\ (S_n\\to0);\\ E_{n+1}/E_n\\to e^{-2\\pi/s_0},\\ e^{\\pi/s_0}=22.7", "breaks": "Halo nuclei have Pauli-blocked cores and finite-range corrections, and no excited Efimov state of a nucleus has been seen.", "confidence": "established", "strength": 2}
{"id": "C2591", "a": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Nuclear and molecular rotational bands", "kind": "historical", "summary": "Bohr and Mottelson's collective model borrowed the molecular separation of intrinsic and rotational motion: deformed nuclei show E proportional to J(J+1) bands like diatomic rotors, with moments of inertia between irrotational and rigid values.", "map": "E_J=\\frac{\\hbar^2}{2\\mathcal I}J(J+1)\\ \\leftrightarrow\\ E_J=BJ(J+1),\\ B=\\frac{\\hbar^2}{2I}", "breaks": "Nuclei have no heavy constituents to rotate; collective rotation emerges from the same nucleons, so the adiabatic separation is approximate and pairing reduces the moment of inertia.", "confidence": "established", "strength": 3}
{"id": "C2592", "a": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "b": "11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods", "name": "Shell model as configuration interaction (quantum chemistry)", "kind": "method transfer", "summary": "The nuclear shell model is configuration interaction in a valence space, diagonalized with the same Lanczos and m-scheme techniques as full CI in quantum chemistry; both face exponential basis growth and use truncation, effective operators and now quantum algorithms.", "map": "|\\Psi\\rangle=\\sum_\\alpha c_\\alpha|\\Phi_\\alpha\\rangle,\\ H\\mathbf c=E\\mathbf c;\\ \\dim\\sim\\binom{N_{\\rm orb}}{N_p}\\binom{N_{\\rm orb}}{N_n}", "breaks": "Shell-model interactions are effective, renormalized valence-space operators with isospin; chemistry CI uses bare Coulomb integrals in Gaussian bases.", "confidence": "established", "strength": 2}
{"id": "C2593", "a": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Nuclear magnetic moments behind MRI", "kind": "shared object", "summary": "MRI images the precession of nuclear spins; the Larmor frequencies of 1H, 13C, 19F, 23Na and 31P come from nuclear magnetic moments (Schmidt-line shell-model values plus core polarization), first measured by Rabi's resonance method.", "map": "\\omega_0=\\gamma B_0,\\ \\gamma=\\frac{g\\mu_N}{\\hbar};\\ \\frac{\\gamma_p}{2\\pi}=42.58\\ \\text{MHz/T},\\ g_p=5.586", "breaks": "MRI contrast comes from relaxation and chemistry of the environment (T1, T2), not from nuclear structure.", "confidence": "established", "strength": 2}