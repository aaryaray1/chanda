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

### Parton distribution functions · `knowledge/07-nuclear-physics/hadron-and-nucleon-structure/parton-distribution-functions`

**Scope.** DIS kinematics ($x$, $Q^2$, $y$), structure functions $F_1,F_2,F_L$, Callan–Gross relation, Bjorken scaling and its violation, collinear factorization, DGLAP evolution, global fits (CT, MSHT, NNPDF), lattice-QCD moments, nuclear PDFs, PDF uncertainties in LHC predictions.

**Core ideas.**
- $f_i(x,\mu^2)$: probability density for parton $i$ carrying momentum fraction $x$ at resolution scale $\mu$.
- Scaling violations are logarithmic and predicted by perturbative QCD; gluons carry ~half the proton's momentum.
- PDFs are universal: measured in DIS, used at the LHC.

**Key equations.**
$$\int_0^1dx\,x\sum_i f_i(x,\mu^2)=1,\qquad \int_0^1[u(x)-\bar u(x)]dx=2$$

**See also.** [QCD](knowledge/06-particle-physics/standard-model/quantum-chromodynamics/README.md) · [Jets and QCD phenomenology](knowledge/06-particle-physics/collider-and-experimental-particle-physics/jets-and-qcd-phenomenology/README.md)

## Heavy-ion physics · `knowledge/07-nuclear-physics/heavy-ion-physics`

#### Overview
Collisions of gold or lead nuclei at RHIC and the LHC create droplets of quark–gluon plasma at trillions of kelvin — the state of the universe microseconds after the Big Bang. Surprisingly, it behaves as a near-perfect liquid with the lowest viscosity-to-entropy ratio known, flows collectively, and quenches energetic jets. The QCD phase diagram at finite baryon density, including a possible critical point, is probed by beam-energy scans.

#### Key equations
$$\frac{dN}{d\phi}\propto1+2\sum_nv_n\cos[n(\phi-\Psi_n)],\qquad \epsilon_{\text{Bj}}=\frac{1}{\pi R^2\tau_0}\frac{dE_T}{dy},\qquad T_c\approx156\ \text{MeV}$$

#### Open problems
- Does a QCD critical point exist, and where?
- Why do small systems (pp, pPb) show flow-like signals?

#### Connections
- [QCD](knowledge/06-particle-physics/standard-model/quantum-chromodynamics/README.md) · [Holography (η/s)](knowledge/05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft/README.md) · [Early-universe cosmology](knowledge/09-astrophysics-and-cosmology/cosmology/README.md)

### Collective flow and hydrodynamics · `knowledge/07-nuclear-physics/heavy-ion-physics/collective-flow-and-hydrodynamics`

**Scope.** Elliptic ($v_2$) and triangular ($v_3$) flow, event-by-event fluctuations, Glauber and IP-Glasma initial conditions, Israel–Stewart and second-order hydrodynamics, Bayesian extraction of $\eta/s(T)$ and $\zeta/s(T)$, hydrodynamic attractors, flow in pp and pPb, nuclear-structure imaging via flow (deformation of ²³⁸U, ¹²⁹Xe).

**Core ideas.**
- Spatial anisotropy of the overlap region is converted into momentum anisotropy by pressure gradients — only if the medium interacts strongly.
- Triangular flow arises purely from fluctuations, proving event-by-event initial structure.
- Hydrodynamics works surprisingly early (~1 fm/c) — "unreasonable effectiveness" explained by attractors.

**Key equations.**
$$\partial_\mu T^{\mu\nu}=0,\quad T^{\mu\nu}=(\varepsilon+P)u^\mu u^\nu-Pg^{\mu\nu}+\pi^{\mu\nu},\qquad v_n\approx\kappa_n\varepsilon_n$$

**See also.** [Ideal and viscous flow](knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow/README.md) · [Statistical inference](knowledge/00-foundations/measurement-and-data-analysis/statistical-inference-in-physics/README.md)

### Jet quenching · `knowledge/07-nuclear-physics/heavy-ion-physics/jet-quenching`

**Scope.** Radiative (BDMPS-Z, GLV) and collisional energy loss, $R_{AA}$ suppression of high-$p_T$ hadrons, dijet asymmetry at the LHC, jet substructure modification, medium response, heavy-quark dead-cone effect, extraction of $\hat q$ (JET collaboration), Monte Carlo models (JEWEL, MARTINI).

**Core ideas.**
- Hard partons radiate gluons induced by multiple scattering in the medium; radiative loss grows as $L^2$ (coherence).
- $R_{AA}\approx0.2$ at intermediate $p_T$ in central PbPb — a fivefold suppression.
- Jets are tomographic probes of the medium's transport coefficient $\hat q\sim$ few GeV²/fm.

**Key equations.**
$$R_{AA}=\frac{dN_{AA}/dp_T}{\langle N_{\text{coll}}\rangle\,dN_{pp}/dp_T},\qquad \Delta E_{\text{rad}}\propto\alpha_s\hat qL^2$$

**See also.** [Jets and QCD phenomenology](knowledge/06-particle-physics/collider-and-experimental-particle-physics/jets-and-qcd-phenomenology/README.md)

### QCD phase diagram and critical point · `knowledge/07-nuclear-physics/heavy-ion-physics/qcd-phase-diagram-and-critical-point`

**Scope.** Lattice QCD at $\mu_B=0$ (smooth crossover), sign problem at finite $\mu_B$, Taylor expansion and imaginary-$\mu$ methods, conjectured first-order line and critical endpoint, net-proton cumulants and the RHIC Beam Energy Scan, FAIR/NICA programmes, quarkyonic matter, color superconductivity (CFL) at high density, neutron-star cores.

**Core ideas.**
- At zero baryon density the transition is a crossover (Aoki et al. 2006).
- A critical point would produce non-monotonic fluctuations (higher cumulants) as beam energy varies.
- Cold dense QCD (neutron stars) is accessible only via astrophysics and models.

**Key equations.**
$$\kappa\sigma^2=\frac{C_4}{C_2},\qquad \chi_n^B=\frac{\partial^n(P/T^4)}{\partial(\mu_B/T)^n}$$

**Landmark.** Aoki et al. (2006) — see [subfield landmarks](knowledge/07-nuclear-physics/heavy-ion-physics/README.md).

**See also.** [Lattice field theory](knowledge/06-particle-physics/quantum-field-theory/lattice-field-theory/README.md) · [Neutron-star EOS](knowledge/07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state/README.md)

### Quark–gluon plasma · `knowledge/07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma`

**Scope.** Deconfinement and chiral restoration, lattice equation of state, Bjorken energy density, strangeness enhancement, quarkonium suppression and regeneration, thermal photons and dileptons, $\eta/s$ near $1/4\pi$, heavy-quark diffusion, QGP in the early universe (~10 μs).

**Core ideas.**
- Above $T_c\approx156$ MeV hadrons dissolve into a strongly coupled plasma, not a weakly interacting gas.
- Its shear viscosity per entropy is near the holographic bound $\hbar/4\pi k_B$ — a near-perfect fluid.
- Colour screening melts bound states sequentially ($\Upsilon(3S)$ before $\Upsilon(1S)$).

**Key equations.**
$$\frac{\varepsilon}{T^4}\approx\frac{\pi^2}{30}\left(16+\frac{21}{2}n_f\right)\ (\text{ideal QGP}),\qquad \frac\eta s\gtrsim\frac{\hbar}{4\pi k_B}$$

**See also.** [Holography and AdS/CFT](knowledge/05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft/README.md) · [Plasma fundamentals](knowledge/10-plasma-physics/plasma-fundamentals/README.md)

## Nuclear astrophysics · `knowledge/07-nuclear-physics/nuclear-astrophysics`

#### Overview
Hydrogen, helium and lithium were made in the first minutes after the Big Bang; carbon to iron in stellar cores; most heavier elements in the s-process (slow neutron capture in AGB stars) and r-process (rapid capture in neutron-star mergers and perhaps rare supernovae). Neutron stars test nuclear matter at up to several times saturation density. Nuclear astrophysics connects reaction rates, nuclear masses and the equation of state to observations.

#### Key equations
$$4p\to{}^4\text{He}+2e^++2\nu_e+26.7\ \text{MeV},\qquad Y_p\approx\frac{2(n/p)}{1+(n/p)}\approx0.25,\qquad \frac{dP}{dr}=-\frac{G(\varepsilon+P)(m+4\pi r^3P/c^2)}{c^2r(r-2Gm/c^2)}$$

#### Open problems
- The cosmological lithium problem (predicted ⁷Li ~3× observed).
- Relative contributions of mergers vs. collapsars to r-process enrichment.

#### Connections
- [Stellar astrophysics](knowledge/09-astrophysics-and-cosmology/stellar-astrophysics/README.md) · [Multi-messenger astronomy](knowledge/09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/multi-messenger-astronomy/README.md) · [Fusion reactions](knowledge/07-nuclear-physics/nuclear-reactions-and-decays/fusion-reactions/README.md)

### Big Bang nucleosynthesis · `knowledge/07-nuclear-physics/nuclear-astrophysics/big-bang-nucleosynthesis`

**Scope.** Weak freeze-out at $T\approx0.8$ MeV ($n/p\approx1/6$), free-neutron decay to $n/p\approx1/7$, the deuterium bottleneck until $T\approx0.07$ MeV, helium mass fraction $Y_p\approx0.247$, D/H as a baryometer, agreement with CMB $\Omega_bh^2$, the ⁷Li problem, constraints on $N_{\text{eff}}$ and new physics.

**Core ideas.**
- BBN depends essentially on one free parameter — the baryon-to-photon ratio $\eta$.
- D/H from quasar absorbers and $\Omega_bh^2$ from the CMB agree to ~1%, a triumph of standard cosmology.
- Extra relativistic species speed expansion, raising $Y_p$: $N_{\text{eff}}\approx3$ confirmed.

**Key equations.**
$$\frac{n}{p}=e^{-Q/k_BT_f},\ Q=1.293\ \text{MeV};\qquad \eta_{10}=273.9\,\Omega_bh^2$$

**See also.** [Cosmic microwave background](knowledge/09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background/README.md) · [Baryogenesis](knowledge/06-particle-physics/beyond-the-standard-model/baryogenesis-and-matter-antimatter/README.md)

### Neutron-star equation of state · `knowledge/07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state`

**Scope.** Saturation density $n_0\approx0.16$ fm⁻³, symmetry energy and its slope $L$, TOV equation and mass–radius curves, 2 $M_\odot$ pulsars, NICER X-ray pulse-profile radii (~12–13 km), GW170817 tidal deformability, hyperons and the "hyperon puzzle", quark-matter cores, crust physics and glitches, PREX/CREX neutron-skin measurements.

**Core ideas.**
- The EOS determines a one-to-one mass–radius relation via the TOV equation.
- 2 $M_\odot$ stars require a stiff EOS; tidal deformability from GW170817 rules out the stiffest.
- Neutron-skin thickness of ²⁰⁸Pb correlates with neutron-star radii through $L$.

**Key equations.**
$$\Lambda=\frac23k_2\left(\frac{c^2R}{GM}\right)^5,\qquad E(n,\delta)\approx E_0(n)+S(n)\delta^2,\ \delta=\frac{n_n-n_p}{n}$$

**Landmark.** Demorest et al. (2010) — see [subfield landmarks](knowledge/07-nuclear-physics/nuclear-astrophysics/README.md).

**See also.** [Compact objects](knowledge/09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects/README.md) · [Ground-based GW detections](knowledge/05-relativity-and-gravitation/gravitational-waves/ground-based-detections/README.md)

### Stellar nucleosynthesis and the r-process · `knowledge/07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process`

**Scope.** pp chains and CNO cycle, triple-alpha and the Hoyle state, C/Ne/O/Si burning, nuclear statistical equilibrium and the iron peak, s-process in AGB stars, r-process sites (neutron-star mergers, collapsars, magnetorotational supernovae), the kilonova AT2017gfo, p-process, i-process, actinide-boost stars.

**Core ideas.**
- Beyond iron, fusion is endothermic; heavier nuclei form by neutron capture.
- s-process: captures slower than β decay, path along the valley of stability; r-process: captures faster, path near the neutron drip line.
- Lanthanide-rich ejecta are opaque, giving kilonovae their red, week-long glow.

**Key equations.**
$$3\,{}^4\text{He}\to{}^{12}\text{C}+7.27\ \text{MeV}\ (\text{via the }7.65\ \text{MeV Hoyle state}),\qquad \tau_n\ll\tau_\beta\ (\text{r}),\ \tau_n\gg\tau_\beta\ (\text{s})$$

**See also.** [Supernovae](knowledge/09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients/README.md) · [Exotic nuclei](knowledge/07-nuclear-physics/nuclear-structure/exotic-nuclei-and-drip-lines/README.md)

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

### Nuclear forces and chiral EFT · `knowledge/07-nuclear-physics/nuclear-structure/nuclear-forces-and-chiral-eft`

**Scope.** One-pion exchange and the tensor force, deuteron properties, phenomenological potentials (Argonne v18, CD-Bonn), chiral EFT power counting (Weinberg), LO–N⁴LO forces, three-nucleon forces, regulator dependence, pionless EFT and universality, lattice QCD calculations of nuclear forces.

**Core ideas.**
- At momenta $Q\ll\Lambda_\chi\sim1$ GeV, nuclear forces are an expansion in $Q/\Lambda_\chi$ with pions as explicit degrees of freedom.
- Three-nucleon forces appear naturally at N²LO and are essential for binding and saturation.
- EFT provides systematic uncertainty estimates from truncation of the expansion.

**Key equations.**
$$V_{1\pi}(\mathbf q)=-\frac{g_A^2}{4f_\pi^2}\boldsymbol\tau_1\cdot\boldsymbol\tau_2\frac{(\boldsymbol\sigma_1\cdot\mathbf q)(\boldsymbol\sigma_2\cdot\mathbf q)}{q^2+m_\pi^2}$$

**See also.** [Effective field theory](knowledge/06-particle-physics/quantum-field-theory/effective-field-theory/README.md) · [Lattice field theory](knowledge/06-particle-physics/quantum-field-theory/lattice-field-theory/README.md)

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

### Superheavy elements · `knowledge/07-nuclear-physics/nuclear-structure/superheavy-elements`

**Scope.** Cold and hot fusion–evaporation reactions, ⁴⁸Ca beams on actinide targets, elements 113–118 (nihonium to oganesson), cross sections at the picobarn level, α-decay chains, shell-correction energies, predicted island of stability near $Z\approx114$–120, $N\approx184$, relativistic effects in superheavy chemistry, attempts at elements 119/120.

**Core ideas.**
- Without shell effects, nuclei beyond $Z\approx104$ would fission instantly; shell corrections create a fission barrier.
- Production rates are a few atoms per week; identification relies on correlated decay chains.
- Relativistic electrons change chemistry (e.g., Og may not behave as a noble gas).

**Key equations.**
$$Z^2/A\gtrsim50\ \Rightarrow\ \text{no liquid-drop fission barrier}$$

**Landmark.** Oganessian et al. (2010) — see [subfield landmarks](knowledge/07-nuclear-physics/nuclear-structure/README.md).

**See also.** [Nuclear fission](knowledge/07-nuclear-physics/nuclear-reactions-and-decays/nuclear-fission/README.md)


---

# Packet 07-2 (100 records)

{"id": "C1123", "a": "02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics", "b": "07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay", "name": "VUV frequency comb for the Th-229 nuclear clock", "kind": "method transfer", "summary": "The 8.36 eV isomer of 229Th was excited with VUV lasers in 2024 and resolved with a VUV frequency comb made by cavity-enhanced seventh-harmonic generation of an infrared comb. The comb measured the transition's frequency ratio to the 87Sr optical clock and resolved its nuclear electric-quadrupole splitting in a CaF2 host. This makes a nuclear transition a candidate optical clock with enhanced sensitivity to variations of fundamental constants.", "map": "E_{\\rm iso}\\approx8.356\\ \\mathrm{eV}\\ (\\lambda\\approx148.4\\ \\mathrm{nm});\\ \\ \\nu=q\\,(nf_{\\rm rep}+f_0),\\ q=7", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1124", "a": "02-electromagnetism-and-optics/radiation-and-scattering/cherenkov-and-transition-radiation", "b": "07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry", "name": "Cherenkov and transition-radiation detectors", "kind": "method transfer", "summary": "Cherenkov emission (cosθ_C = 1/nβ, Frank–Tamm photon yield) and transition radiation (yield ∝ γ) are the basis of threshold counters, ring-imaging Cherenkov detectors and TRDs. These identify electrons, pions and other hadrons in nuclear-physics spectrometers and the EIC's ePIC detector, and water-Cherenkov detectors use the same light to detect neutrinos. The Cherenkov angle gives β, which together with momentum gives the particle's mass.", "map": "\\cos\\theta_C=\\frac{1}{n\\beta},\\ \\ \\frac{d^2N}{dx\\,d\\lambda}=\\frac{2\\pi\\alpha}{\\lambda^2}\\Big(1-\\frac{1}{\\beta^2n^2}\\Big),\\ \\ W_{\\rm TR}=\\tfrac13\\alpha\\hbar\\omega_p\\gamma", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1125", "a": "02-electromagnetism-and-optics/radiation-and-scattering/dipole-radiation-and-antennas", "b": "07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay", "name": "Gamma-decay multipolarity is multipole radiation", "kind": "identity", "summary": "Nuclear γ transitions are classified as electric and magnetic 2^L-pole radiation and follow the selection rules of classical multipole radiation (EL parity (-1)^L, ML parity (-1)^(L+1)). Weisskopf single-particle estimates are the antenna formulas with nuclear transition moments inserted, and each extra multipole order costs a factor of about (kR)^2 ~ 10^-3–10^-5. That suppression is why high-L or very low-energy transitions give long-lived isomers such as the 8.4 eV M1 isomer of 229Th.", "map": "\\lambda(\\sigma L)=\\frac{8\\pi(L+1)}{\\hbar L[(2L+1)!!]^2}\\Big(\\frac{E_\\gamma}{\\hbar c}\\Big)^{2L+1}B(\\sigma L)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1126", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry", "name": "Bremsstrahlung, radiation length and showers", "kind": "mechanism", "summary": "Above the critical energy, electrons lose energy mainly by bremsstrahlung in nuclear Coulomb fields, the relativistic radiation of a decelerated charge. The radiation length X0 then sets how electromagnetic showers develop in calorimeters. Because the radiative-to-collisional loss ratio grows roughly as EZ, β shielding puts low-Z material first.", "map": "-\\Big(\\frac{dE}{dx}\\Big)_{\\rm rad}=\\frac{E}{X_0},\\ \\ E_c\\approx\\frac{610\\ \\mathrm{MeV}}{Z+1.24}\\ (\\text{solids})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1127", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "07-nuclear-physics/hadron-and-nucleon-structure/electron-ion-collider", "name": "Synchrotron radiation and Sokolov–Ternov polarization", "kind": "mechanism", "summary": "Synchrotron power scales as γ^4/ρ^2; it limits the energy of electron storage rings and sets the EIC electron ring at up to 18 GeV. Spin-flip synchrotron emission self-polarizes stored electrons antiparallel to the field (Sokolov–Ternov, 92.4%), which HERA exploited. The EIC needs both helicities and self-polarization is slow, so it instead refreshes bunches from a polarized source while fighting radiative depolarization.", "map": "P=\\frac{e^2c\\gamma^4}{6\\pi\\epsilon_0\\rho^2},\\ \\ P_{\\rm ST}=\\frac{8}{5\\sqrt3}\\approx92.4\\%", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1128", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "07-nuclear-physics/heavy-ion-physics/jet-quenching", "name": "LPM suppression and QCD radiative energy loss", "kind": "analogy", "summary": "When the formation time of a radiated quantum exceeds the mean free path, successive scatterings act coherently and suppress the radiation; for bremsstrahlung in dense matter this is the Landau–Pomeranchuk–Migdal effect. The BDMPS-Z and GLV radiative energy loss of quarks and gluons in the QGP is its non-Abelian version, governed by the transport coefficient q̂.", "map": "t_f\\simeq\\frac{2\\omega}{k_\\perp^2}>\\lambda_{\\rm mfp};\\ \\ \\Delta E_{\\rm BDMPS}\\simeq\\frac{\\alpha_sC_R}{4}\\hat qL^2\\ \\ (\\hbar=c=1)", "breaks": "The radiated gluon carries colour and rescatters itself, which gives ΔE ∝ q̂L^2 rather than the QED scaling. The medium is also a rapidly expanding, strongly coupled plasma rather than a static solid.", "confidence": "established", "strength": 3}
{"id": "C1129", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions", "name": "Cyclotron radiation spectroscopy of tritium β electrons", "kind": "method transfer", "summary": "Project 8 measures β-electron energies from the frequency of their cyclotron radiation, f_c = eB/2πγm_e (~26 GHz near 1 T), picked up in a waveguide; the signal power is the Larmor power of a circulating charge. The goal is the neutrino mass from the tritium endpoint, and the experiment has already set a first tritium limit.", "map": "f_c=\\frac{eB}{2\\pi\\gamma m_e},\\ \\ \\gamma=1+\\frac{K}{m_ec^2},\\ \\ P=\\frac{e^2\\omega_c^2v_\\perp^2\\gamma^4}{6\\pi\\epsilon_0c^3}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1130", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "07-nuclear-physics/applied-nuclear-physics/nuclear-data-and-isotope-production", "name": "Laser Compton backscattering gamma sources", "kind": "method transfer", "summary": "Backscattering laser or FEL photons off relativistic electrons (inverse Compton scattering) produces tunable, quasi-monoenergetic, highly polarized MeV γ beams, as at HIγS. These beams are used to measure photonuclear cross sections and giant resonances, and for nuclear resonance fluorescence assays that identify specific isotopes.", "map": "E_\\gamma^{\\max}\\approx\\frac{4\\gamma^2E_L}{1+4\\gamma E_L/m_ec^2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1131", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry", "name": "Photon attenuation: photoelectric, Compton, pair", "kind": "identity", "summary": "Gamma-ray detection and shielding rest on the photon–matter cross sections of light-scattering theory: photoabsorption, Compton scattering with the Klein–Nishina cross section (which reduces to Thomson's σ_T at low energy), and pair production. Together these set the exponential attenuation coefficient μ(E,Z). The Compton edge and continuum seen in every γ spectrum follow directly from Compton kinematics.", "map": "\\frac{d\\sigma}{d\\Omega}=\\frac{r_e^2}{2}\\epsilon^2(\\epsilon+\\epsilon^{-1}-\\sin^2\\theta),\\ \\ \\epsilon=\\frac{E'}{E}=\\Big[1+\\frac{E}{m_ec^2}(1-\\cos\\theta)\\Big]^{-1}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1132", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "07-nuclear-physics/hadron-and-nucleon-structure/nucleon-spin-and-form-factors", "name": "Compton scattering off the nucleon: Thomson to DVCS", "kind": "identity", "summary": "Real Compton scattering off the nucleon has the low-energy structure of light scattering: a Thomson amplitude fixed by charge and mass, then a Rayleigh-like ω^2 term set by the electric and magnetic polarizabilities. The values α_E ≈ 11×10^-4 fm^3 and β_M ≈ 2.5×10^-4 fm^3 show the proton is a very stiff object. Deeply virtual Compton scattering is the same process in the Bjorken limit, where it accesses GPDs and the Ji spin sum rule.", "map": "f\\approx-\\frac{e^2}{4\\pi\\epsilon_0Mc^2}\\boldsymbol\\epsilon\\cdot\\boldsymbol\\epsilon'+\\frac{\\omega^2}{c^2}\\big[\\alpha_E\\boldsymbol\\epsilon\\cdot\\boldsymbol\\epsilon'+\\beta_M(\\hat k\\times\\boldsymbol\\epsilon)\\cdot(\\hat k'\\times\\boldsymbol\\epsilon')\\big]", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1133", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "07-nuclear-physics/hadron-and-nucleon-structure/parton-distribution-functions", "name": "Compton profiles and Bjorken scaling", "kind": "analogy", "summary": "X-ray Compton profiles and Bjorken scaling in deep inelastic scattering are both impulse-approximation results. At large momentum transfer the probe scatters off quasi-free constituents, so the cross section depends on a single scaling variable and measures their momentum distribution: J(p_z) for electrons, q(x) for quarks. y-scaling in quasi-elastic electron–nucleus scattering is the intermediate case, for nucleons.", "map": "J(p_z)=\\int n(\\mathbf p)\\,dp_x\\,dp_y\\ \\leftrightarrow\\ F_2(x)=\\sum_qe_q^2\\,x\\,q(x)", "breaks": "Partons are confined and relativistic, so the scaling variable is a light-cone momentum fraction and the final state hadronizes instead of escaping. QCD radiation also produces logarithmic scaling violations (DGLAP), which atomic Compton profiles do not have.", "confidence": "established", "strength": 2}
{"id": "C1134", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "name": "Optical model as nuclear Mie scattering", "kind": "analogy", "summary": "Elastic nucleon–nucleus scattering is described by a complex potential whose imaginary part absorbs flux into other channels. This is the quantum counterpart of Mie scattering by a sphere with a complex refractive index: both use partial-wave series, separate elastic from absorption cross sections and obey the optical theorem. The name 'optical model' (the 'cloudy crystal ball') comes directly from this analogy.", "map": "\\nabla^2\\psi+k^2n^2\\psi=0\\ \\leftrightarrow\\ n^2(\\mathbf r)=1-\\frac{U(\\mathbf r)}{E},\\ U=-(V+iW)f(r);\\ \\ \\sigma_{\\rm tot}=\\frac{4\\pi}{k}{\\rm Im}f(0)", "breaks": "Mie theory is vectorial, with two coefficient series a_n and b_n for polarization, and uses a local, energy-independent index. The nuclear potential is scalar plus spin–orbit, energy-dependent and nonlocal, and the long-range Coulomb field distorts the partial waves of charged projectiles.", "confidence": "established", "strength": 3}
{"id": "C1434", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/heat-engines-and-efficiency", "b": "07-nuclear-physics/applied-nuclear-physics/nuclear-reactors-and-energy", "name": "Reactors as heat sources for Rankine cycles", "kind": "shared object", "summary": "Fission reactors and fusion plants are heat sources whose electrical efficiency (~33% for LWRs, more for high-temperature designs) is bounded by Carnot at the coolant outlet temperature and achieved with Rankine or Brayton cycles. Decay heat after shutdown is a thermodynamic safety problem.", "map": "\\eta\\le1-T_c/T_h,\\ T_h^{\\text{PWR}}\\approx590\\ \\text{K}\\Rightarrow\\eta_C\\approx0.49,\\ \\eta_{\\text{real}}\\approx0.33", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1435", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/phase-equilibria-and-chemical-potential", "b": "07-nuclear-physics/heavy-ion-physics/qcd-phase-diagram-and-critical-point", "name": "Nuclear liquid–gas transition and the QCD phase diagram", "kind": "identity", "summary": "Strongly interacting matter has two first-order lines ending in Ising-class critical points: the nuclear liquid–gas transition (T_c≈15–18 MeV, near saturation density, from van der Waals-like nucleon interactions) and the conjectured chiral/deconfinement line at high μ_B. Multifragmentation caloric curves show a liquid–gas plateau, and coexistence follows the Gibbs conditions in (T, μ_B).", "map": "\\frac{dP}{dT}\\Big|_{\\text{coex}}=\\frac{\\Delta s}{\\Delta n_B};\\ T_c^{LG}\\approx15\\text{–}18\\ \\text{MeV},\\ \\mu_B\\approx0.92\\ \\text{GeV}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1436", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/phase-equilibria-and-chemical-potential", "b": "07-nuclear-physics/nuclear-astrophysics/big-bang-nucleosynthesis", "name": "Nuclear statistical equilibrium and the deuterium bottleneck", "kind": "identity", "summary": "Early-universe abundances follow the Saha/law-of-mass-action equation μ_A=Zμ_p+Nμ_n. Deuterium is suppressed until T≈0.07 MeV, well below its 2.2 MeV binding energy, because the photon-to-baryon ratio η⁻¹~10⁹ is huge (entropy wins).", "map": "\\frac{n_d}{n_pn_n}=\\frac34\\left(\\frac{4\\pi\\hbar^2}{m_Nk_BT}\\right)^{3/2}e^{B_d/k_BT}\\Rightarrow\\frac{n_d}{n_p}\\sim\\eta\\left(\\frac{T}{m_N}\\right)^{3/2}e^{B_d/T}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1437", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/phase-equilibria-and-chemical-potential", "b": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "name": "Gibbs vs Maxwell constructions and nuclear pasta", "kind": "identity", "summary": "With two conserved charges (baryon number and electric charge), a first-order hadron–quark or liquid–gas transition in a star can form a mixed phase under the Gibbs conditions instead of a sharp Maxwell interface. In the inner crust, Coulomb frustration of phase separation produces 'pasta' phases (rods, slabs).", "map": "\\mu_B^{I}=\\mu_B^{II},\\ \\mu_Q^{I}=\\mu_Q^{II},\\ P^{I}=P^{II}\\ (\\text{Gibbs});\\ \\text{global }Q=0", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1438", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/phase-equilibria-and-chemical-potential", "b": "07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process", "name": "r-process waiting points as Saha equilibrium", "kind": "identity", "summary": "In the hot, neutron-rich r-process, (n,γ)⇌(γ,n) equilibrium along each isotopic chain is a Saha equation. Neutron density and temperature fix the waiting-point nuclei through their neutron separation energies, and β-decays then move material to higher Z.", "map": "\\frac{Y(Z,A+1)}{Y(Z,A)}=n_n\\frac{G_{A+1}}{2G_A}\\left(\\frac{2\\pi\\hbar^2}{m_uk_BT}\\right)^{3/2}e^{S_n/k_BT}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1439", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/phase-equilibria-and-chemical-potential", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Liquid-drop model: nuclei as droplets of nuclear liquid", "kind": "analogy", "summary": "The semi-empirical mass formula is the leptodermous (volume plus surface) expansion of a droplet of saturated, incompressible liquid. The volume term is the bulk chemical potential, and the surface term is a surface tension σ≈1 MeV/fm², the same capillarity that sets nucleation barriers.", "map": "B=a_VA-a_SA^{2/3}-\\cdots\\ \\leftrightarrow\\ G=-\\Delta\\mu N+4\\pi r^2\\sigma,\\ a_S=4\\pi r_0^2\\sigma", "breaks": "Nuclei have only ~10–300 constituents, so curvature and shell corrections (magic numbers) are comparable to surface terms. The 'liquid' is a quantum Fermi liquid with pairing, not a classical van der Waals fluid.", "confidence": "established", "strength": 2}
{"id": "C1440", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "name": "Random-matrix theory born in compound nuclei", "kind": "historical", "summary": "Wigner introduced random matrices to model the dense resonances of compound nuclei. Level-spacing repulsion (Wigner surmise) and Porter–Thomas width distributions became, after Dyson's classification, a core tool of disordered and complex systems: mesoscopic transport, localization and spin glasses.", "map": "P(s)=\\frac{\\pi s}{2}e^{-\\pi s^2/4};\\ P(\\Gamma)\\propto\\Gamma^{-1/2}e^{-\\Gamma/2\\langle\\Gamma\\rangle}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1441", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/percolation", "b": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "name": "Colour-string percolation as a deconfinement model", "kind": "analogy", "summary": "In string-percolation models, colour flux tubes from nucleon–nucleon collisions overlap as discs in the transverse plane. Deconfinement is identified with 2D continuum percolation of these discs at a critical density, which predicts the onset of collective effects with centrality.", "map": "\\eta_c=\\frac{N_s\\pi r_0^2}{\\pi R^2}\\approx1.13\\ (\\text{2D disc percolation})", "breaks": "Percolation is purely geometric and has no thermodynamics; the QCD transition at μ_B=0 is an analytic crossover with no diverging length. Connectivity of strings is not equivalent to deconfinement or thermalization.", "confidence": "current research", "strength": 1}
{"id": "C1442", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "b": "07-nuclear-physics/heavy-ion-physics/qcd-phase-diagram-and-critical-point", "name": "Baryon-number cumulants as grand-canonical susceptibilities", "kind": "identity", "summary": "Lattice QCD and heavy-ion phenomenology use the grand-canonical relation between pressure derivatives and conserved-charge fluctuations: χ_n^B are cumulants of net baryon number. Real μ_B gives a complex Boltzmann weight (the sign problem), so lattice works by Taylor expansion or imaginary μ. Experiment must correct for global charge conservation, a canonical-ensemble effect.", "map": "\\chi_n^B=\\frac{\\partial^n(P/T^4)}{\\partial(\\mu_B/T)^n}=\\frac{\\langle(\\delta N_B)^n\\rangle_c}{VT^3};\\ \\frac{\\chi_4}{\\chi_2}=\\kappa\\sigma^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1443", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "b": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "name": "Statistical hadronization and the thermal model", "kind": "method transfer", "summary": "Hadron yields across species and collision energies follow a grand-canonical hadron-resonance-gas partition function with just T_ch≈156 MeV and μ_B(√s), which coincides with the lattice crossover. In small systems strangeness is suppressed because exact canonical conservation, not grand-canonical averaging, applies (ensemble inequivalence).", "map": "\\langle N_i\\rangle=\\frac{g_iV}{2\\pi^2}\\int\\frac{p^2dp}{e^{(E_i-\\mu_BB_i-\\mu_SS_i)/T}\\pm1}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1444", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "name": "Compound-nucleus decay as microcanonical evaporation", "kind": "identity", "summary": "Bohr's compound nucleus 'forgets' how it formed and decays statistically. Weisskopf evaporation and Hauser–Feshbach theory compute decay widths from detailed balance and level densities, so emission spectra are Maxwellian with a nuclear temperature T=(∂ln ρ/∂E)^{-1}. This is microcanonical statistical mechanics of a ~100-body system.", "map": "P(\\epsilon)d\\epsilon\\propto\\sigma_{\\text{inv}}\\,\\epsilon\\,\\rho(E^*-B-\\epsilon)\\,d\\epsilon\\approx\\epsilon\\,e^{-\\epsilon/T}d\\epsilon", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1445", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information", "b": "07-nuclear-physics/hadron-and-nucleon-structure/parton-distribution-functions", "name": "Parton entanglement entropy at small x", "kind": "identity", "summary": "Kharzeev and Levin proposed that the entanglement entropy between probed and unprobed regions of a proton at small x is S=ln(xG(x)), saturating the maximum for a dipole cascade. Hadron multiplicities measured in DIS are then compared with this entropy.", "map": "S_{\\text{ent}}=\\ln\\left[xG(x,Q^2)\\right]\\ (\\text{small }x)", "breaks": "", "confidence": "proposed", "strength": 1}
{"id": "C1446", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/exactly-solvable-models", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Richardson's exact solution of the pairing model", "kind": "identity", "summary": "The reduced BCS pairing Hamiltonian for a finite set of levels is exactly solvable by Bethe-ansatz-type Richardson equations (Richardson–Gaudin integrability). It describes pairing in nuclei and ultrasmall superconducting grains beyond mean field, where BCS breaks down as Δ approaches the level spacing.", "map": "\\frac1G-\\sum_k\\frac{1}{2\\epsilon_k-E_\\nu}+\\sum_{\\mu\\ne\\nu}\\frac{2}{E_\\mu-E_\\nu}=0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1447", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "name": "Stefan–Boltzmann limit of the quark–gluon gas", "kind": "identity", "summary": "An ideal QGP is a relativistic Bose (gluons) plus Fermi (quarks) gas, ε/T⁴=(π²/30)(16+(21/2)n_f), and the jump in degrees of freedom across T_c signals deconfinement. Lattice EOS reaches only ~80% of this at a few T_c, a sign of strong coupling.", "map": "\\frac{\\varepsilon}{T^4}=\\frac{\\pi^2}{30}\\left(16+\\frac{21}{2}n_f\\right),\\ \\text{hadron gas}\\ \\approx3\\ (\\text{pions})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1448", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "name": "Neutron degeneracy pressure and β-equilibrium", "kind": "identity", "summary": "Neutron-star matter is a degenerate Fermi system. Oppenheimer and Volkoff found that an ideal neutron Fermi gas supports at most ~0.7 M_⊙, and the observed 2 M_⊙ stars require repulsive interactions. Equilibrium composition follows from μ_n=μ_p+μ_e at T≈0.", "map": "P=\\frac{\\hbar^2}{15\\pi^2m}(3\\pi^2)^{5/3}n^{5/3}\\ (NR);\\ \\mu_n=\\mu_p+\\mu_e,\\ M_{\\max}^{\\text{ideal}}\\approx0.7M_\\odot", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1449", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "name": "Fermi-gas nuclear level densities", "kind": "identity", "summary": "Bethe's level-density formula treats the nucleus as a degenerate Fermi gas. The Sommerfeld expansion gives E*=aT² and S=2aT, so ρ(E)∝exp(2√(aE)) with a≈A/8 MeV⁻¹. These level densities feed Hauser–Feshbach rates for reactors and the r-process.", "map": "S=2\\sqrt{aE^*},\\ \\rho(E^*)\\approx\\frac{\\sqrt\\pi}{12a^{1/4}E^{*5/4}}e^{2\\sqrt{aE^*}},\\ a=\\frac{\\pi^2}{6}g(\\epsilon_F)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1450", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/driven-systems-and-nonequilibrium-steady-states", "b": "07-nuclear-physics/applied-nuclear-physics/nuclear-reactors-and-energy", "name": "Chain reactions as critical branching processes", "kind": "identity", "summary": "A neutron chain reaction is a Galton–Watson branching process, and criticality k_eff=1 is its critical point, mean-field directed percolation (an absorbing-state transition with the zero population absorbing). Reactor-noise methods (Feynman-α, Rossi-α) use the diverging fluctuations near k=1 to measure subcriticality.", "map": "\\langle N_{g+1}\\rangle=k\\langle N_g\\rangle,\\ \\frac{\\mathrm{Var}(C)}{\\langle C\\rangle}-1=Y(T)\\propto\\frac{1}{(1-k_p)^2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1451", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/driven-systems-and-nonequilibrium-steady-states", "b": "07-nuclear-physics/hadron-and-nucleon-structure/electron-ion-collider", "name": "Gluon saturation as FKPP travelling fronts", "kind": "identity", "summary": "The Balitsky–Kovchegov equation for gluon saturation is in the universality class of the FKPP reaction–diffusion equation, so the saturation scale is the position of a pulled front in ln(1/x) and geometric scaling is front translation. Noise corrections (Brunet–Derrida) carry over from front-propagation statistics.", "map": "\\partial_tu=\\partial_x^2u+u-u^2\\ (\\text{FKPP})\\leftrightarrow\\partial_YN=\\bar\\alpha\\chi(-\\partial_L)N-\\bar\\alpha N^2;\\ Q_s^2\\propto e^{\\lambda Y}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1452", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "07-nuclear-physics/applied-nuclear-physics/nuclear-reactors-and-energy", "name": "Neutron transport is a linear Boltzmann equation", "kind": "identity", "summary": "Reactor physics solves the linear Boltzmann transport equation for neutron angular flux, with scattering, absorption and fission sources. Its P₁/diffusion approximation (Fick's law, diffusion length) and Fermi age theory of moderation are Chapman–Enskog-type reductions.", "map": "\\frac{1}{v}\\partial_t\\psi+\\hat\\Omega\\cdot\\nabla\\psi+\\Sigma_t\\psi=\\int\\Sigma_s\\psi\\,d\\Omega'dE'+\\frac{\\chi}{4\\pi}\\int\\nu\\Sigma_f\\phi\\,dE';\\ \\mathbf J=-D\\nabla\\phi", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1453", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "07-nuclear-physics/heavy-ion-physics/collective-flow-and-hydrodynamics", "name": "From kinetic theory to viscous relativistic hydrodynamics", "kind": "method transfer", "summary": "Second-order (Israel–Stewart) viscous hydrodynamics, the standard model of heavy-ion flow, is derived from the relativistic Boltzmann equation by Grad's moment method. Hadronic afterburners (UrQMD, SMASH) are Boltzmann transport, and the hydro-to-kinetic switch uses Cooper–Frye sampling of a local Jüttner distribution.", "map": "\\tau_\\pi\\dot\\pi^{\\mu\\nu}+\\pi^{\\mu\\nu}=2\\eta\\sigma^{\\mu\\nu}+\\cdots;\\ \\eta\\approx\\tfrac13n\\bar p\\lambda_{\\text{mfp}}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1454", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "07-nuclear-physics/nuclear-astrophysics/big-bang-nucleosynthesis", "name": "Neutron–proton freeze-out as rate competition", "kind": "mechanism", "summary": "The n/p ratio tracks its equilibrium value e^{-Q/T} until weak rates Γ∝G_F²T⁵ fall below the Hubble rate H∝T²/M_Pl at T_f≈0.8 MeV. That fixes Y_p≈0.25, a textbook example of kinetic freeze-out from a Boltzmann rate equation.", "map": "\\frac{dX_n}{dt}=-\\lambda_{np}X_n+\\lambda_{pn}(1-X_n);\\ \\Gamma(T_f)=H(T_f)\\Rightarrow(n/p)_f=e^{-Q/T_f}\\approx1/6", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1455", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "07-nuclear-physics/nuclear-reactions-and-decays/fusion-reactions", "name": "Gamow peak: Maxwell–Boltzmann tail times tunnelling", "kind": "identity", "summary": "Thermonuclear reaction rates are Maxwell–Boltzmann averages of the cross section. The falling exponential tail times the rising Gamow tunnelling factor gives a sharp peak at E₀ ≫ k_BT, so stellar burning and fusion-plasma reactivities ⟨σv⟩ sample only the far tail of the distribution.", "map": "\\langle\\sigma v\\rangle=\\sqrt{\\frac{8}{\\pi\\mu}}(k_BT)^{-3/2}\\int S(E)e^{-E/k_BT-\\sqrt{E_G/E}}dE,\\ E_0=(E_Gk_B^2T^2/4)^{1/3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1456", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation", "b": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "name": "Kubo transport coefficients of the QGP", "kind": "identity", "summary": "QGP shear and bulk viscosities, conductivity and heavy-quark diffusion are defined by Kubo formulas. Lattice QCD obtains them from Euclidean correlators by inverting to spectral functions, an ill-posed analytic continuation, and flow data give η/s≈1–2 × ħ/4πk_B, near the holographic value.", "map": "\\eta=\\lim_{\\omega\\to0}\\frac{\\rho_{xy,xy}(\\omega)}{\\omega};\\ G_E(\\tau)=\\int\\frac{d\\omega}{\\pi}\\rho(\\omega)\\frac{\\cosh\\omega(\\tau-\\beta/2)}{\\sinh(\\omega\\beta/2)}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1457", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Giant resonances as nuclear linear response", "kind": "identity", "summary": "Giant dipole and monopole resonances are the nucleus's linear response to an external field. RPA is the time-dependent mean-field susceptibility, and energy-weighted sum rules (Thomas–Reiche–Kuhn) are f-sum rules fixed by commutators, as for conductivity or dielectric response.", "map": "\\sum_n(E_n-E_0)|\\langle n|D|0\\rangle|^2=\\frac{\\hbar^2}{2m}\\frac{NZ}{A}\\cdot\\frac{9}{4\\pi}e^2\\ (\\text{TRK});\\ \\chi=\\chi_0/(1-V\\chi_0)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1458", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry", "name": "Fano factor: sub-Poisson ionization statistics", "kind": "identity", "summary": "The number of ion pairs or electron–hole pairs created by a stopped particle fluctuates less than Poisson (Fano factor F≈0.1 in Ge), because total energy is fixed, as with microcanonical fluctuations. F sets the intrinsic energy resolution of gas and semiconductor detectors.", "map": "\\mathrm{Var}(N)=F\\langle N\\rangle,\\ \\frac{\\sigma_E}{E}=2.355\\sqrt{\\frac{Fw}{E}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1459", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "07-nuclear-physics/heavy-ion-physics/jet-quenching", "name": "Jet transverse-momentum broadening as diffusion", "kind": "identity", "summary": "A fast parton crossing the plasma takes random transverse kicks, so its transverse momentum random-walks: ⟨k_⊥²⟩=q̂L, with q̂ a momentum-diffusion coefficient. The coherent sum of induced radiation over this random walk gives the BDMPS ΔE∝q̂L² energy loss.", "map": "\\langle k_\\perp^2\\rangle=\\hat qL,\\ \\hat q=\\rho\\int d^2q_\\perp q_\\perp^2\\frac{d\\sigma}{d^2q_\\perp};\\ \\Delta E\\propto\\alpha_s\\hat qL^2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1460", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "name": "Heavy quarks as Brownian particles in the QGP", "kind": "identity", "summary": "Charm and bottom quarks (M≫T) diffuse through the plasma like Brownian particles. A Langevin equation with drag η_D and momentum-diffusion κ obeys the Einstein relation η_D=κ/2MT, and the spatial diffusion coefficient 2πTD_s is extracted from heavy-flavour R_AA and v₂.", "map": "\\frac{dp_i}{dt}=-\\eta_Dp_i+\\xi_i,\\ \\langle\\xi_i\\xi_j\\rangle=\\kappa\\delta_{ij}\\delta(t-t');\\ D_s=\\frac{2T^2}{\\kappa}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1461", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-fission", "name": "Kramers escape theory was built for nuclear fission", "kind": "historical", "summary": "Kramers' 1940 theory of thermally activated escape over a barrier was motivated by Bohr–Wheeler fission and treated the fissioning nucleus as a Brownian particle in a viscous medium. Nuclear dissipation still appears as the Kramers factor that reduces fission rates and enhances pre-scission neutron emission.", "map": "\\Gamma_f=\\Gamma_{BW}\\left(\\sqrt{1+\\gamma^2}-\\gamma\\right),\\ \\gamma=\\beta/2\\omega_b;\\ \\Gamma_{BW}=\\frac{1}{2\\pi\\rho}\\int\\rho^*(E-B_f-\\epsilon)d\\epsilon", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1462", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay", "name": "Radioactive decay as a Poisson process", "kind": "identity", "summary": "Decay is a memoryless Markov process: counts are Poisson, waiting times exponential, and decay chains obey Bateman's linear master equations. Counting statistics and dead-time corrections in nuclear detectors use the same stochastic-process tools.", "map": "P(n;t)=\\frac{(\\lambda Nt)^n}{n!}e^{-\\lambda Nt};\\ \\dot N_i=\\lambda_{i-1}N_{i-1}-\\lambda_iN_i\\ (\\text{Bateman})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1463", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Shape phase transitions in finite nuclei", "kind": "identity", "summary": "As nucleon number changes, nuclei go from spherical vibrators to deformed rotors through quantum shape phase transitions. Their Landau-theory description uses the quadrupole deformation as order parameter, and analytic critical-point symmetries such as X(5) and E(5) describe nuclei at the transition, which finite size rounds into crossovers.", "map": "V(\\beta)=a\\beta^2-b\\beta^3\\cos3\\gamma+c\\beta^4;\\ R_{4/2}:2.0\\to2.91\\ (X5)\\to3.33", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1464", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/critical-exponents-and-universality", "b": "07-nuclear-physics/heavy-ion-physics/qcd-phase-diagram-and-critical-point", "name": "QCD critical point in the 3D Ising class", "kind": "identity", "summary": "A QCD critical endpoint, if it exists, lies in the 3D Ising (Z₂) universality class. (T, μ_B) map linearly onto Ising (t, h), and net-proton cumulant ratios scale with powers of ξ (κσ²∝ξ⁷), so beam-energy scans hunt for non-monotonic kurtosis. Finite-size scaling of cumulants is used to locate it.", "map": "\\langle\\delta N^4\\rangle_c\\propto\\xi^7,\\ \\langle\\delta N^3\\rangle_c\\propto\\xi^{4.5};\\ (T,\\mu_B)\\mapsto(t,h)_{\\text{Ising}}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1465", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory", "b": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "name": "Relativistic mean-field theory of dense matter", "kind": "method transfer", "summary": "The Walecka σ–ω model replaces meson fields by their mean values, a Hartree mean-field theory in the spirit of Weiss. It reproduces nuclear saturation and gives a stiff neutron-star EOS, and Skyrme and RMF density functionals remain the main EOS inputs beyond ab initio densities.", "map": "M^*=M-g_\\sigma\\bar\\sigma,\\ \\bar\\omega=\\frac{g_\\omega}{m_\\omega^2}n_B;\\ \\varepsilon=\\frac{g_\\omega^2}{2m_\\omega^2}n_B^2+\\cdots", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1466", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "BCS pairing in nuclei", "kind": "mechanism", "summary": "Odd–even mass staggering, gaps in even–even spectra and reduced moments of inertia show that nucleons pair as in a superconductor. A BCS/Bogoliubov mean field with Δ≈12/√A MeV describes it, and the gap equation is the Landau–Ginzburg/BCS mean field of 03 applied to a finite Fermi system.", "map": "\\Delta=G\\sum_k u_kv_k,\\ E_k=\\sqrt{(\\epsilon_k-\\lambda)^2+\\Delta^2};\\ \\Delta\\approx12/\\sqrt A\\ \\text{MeV}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1467", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/renormalization-group", "b": "07-nuclear-physics/hadron-and-nucleon-structure/parton-distribution-functions", "name": "DGLAP evolution as a renormalization-group equation", "kind": "identity", "summary": "Q² dependence of parton distributions is the RG running of twist-2 operator matrix elements. Mellin moments scale with anomalous dimensions γ_n, exactly like scaling operators near a fixed point, and Bjorken scaling is the free-field fixed point of asymptotically free QCD.", "map": "\\frac{\\partial f_n(Q^2)}{\\partial\\ln Q^2}=-\\frac{\\alpha_s}{4\\pi}\\gamma_nf_n,\\ f_n=\\int x^{n-1}f(x)dx", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1468", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/renormalization-group", "b": "07-nuclear-physics/nuclear-structure/ab-initio-nuclear-theory", "name": "SRG and V_low-k: Wilsonian RG for nuclear forces", "kind": "method transfer", "summary": "The similarity renormalization group (and IMSRG) is a continuous unitary RG flow that decouples high- and low-momentum states, the Wilsonian idea of integrating out short distances while keeping observables. It makes nuclear many-body calculations converge and generates induced three-body forces, the analogue of irrelevant couplings generated under RG.", "map": "\\frac{dH_s}{ds}=[\\eta_s,H_s],\\ \\eta_s=[T_{\\text{rel}},H_s];\\ \\lambda=s^{-1/4}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1469", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/renormalization-group", "b": "07-nuclear-physics/nuclear-structure/nuclear-forces-and-chiral-eft", "name": "Efimov physics as an RG limit cycle", "kind": "identity", "summary": "Renormalizing the three-boson problem with contact interactions needs a three-body force whose coupling runs periodically in ln Λ: an RG limit cycle rather than a fixed point. This produces discrete scale invariance and the Efimov ratio 22.7, seen in cold atoms, light nuclei and halo systems.", "map": "H(\\Lambda e^{n\\pi/s_0})=H(\\Lambda),\\ s_0\\approx1.00624,\\ E_{n+1}/E_n=e^{-2\\pi/s_0}\\approx1/515", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1736", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "b": "07-nuclear-physics/nuclear-structure", "name": "Thorium-229 nuclear clock", "kind": "shared object", "summary": "The 8.4 eV isomer of Th-229 has been laser-excited and frequency-referenced to a Sr clock, opening a nuclear optical clock highly sensitive to variations of alpha and the strong-interaction scale.", "map": "E_{\\rm iso}\\approx8.36\\ \\mathrm{eV};\\ \\frac{\\delta\\nu}{\\nu}\\approx K\\frac{\\delta\\alpha}{\\alpha},\\ |K|\\gg1", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1737", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "07-nuclear-physics/hadron-and-nucleon-structure/nucleon-spin-and-form-factors", "name": "Proton radius from hydrogen and muonic hydrogen", "kind": "method transfer", "summary": "The finite proton size shifts S levels; muonic-hydrogen Lamb-shift spectroscopy gave r_p = 0.84 fm, 4% below earlier e-p values, and newer hydrogen spectroscopy largely agrees, resolving most of the proton-radius puzzle.", "map": "\\Delta E_{\\rm fs}=\\frac{2}{3n^3}\\frac{(Z\\alpha)^4m_r^3c^4}{\\hbar^2c^2}\\langle r_p^2\\rangle\\,\\delta_{\\ell0}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1738", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay", "name": "Multipole selection rules for atomic and nuclear photons", "kind": "method transfer", "summary": "Gamma transitions in nuclei obey the same multipole selection rules and Wigner-Eckart structure as atomic E1/M1/E2 lines; Weisskopf estimates and conversion electrons parallel atomic radiative and Auger channels.", "map": "|J_i-J_f|\\le L\\le J_i+J_f;\\ \\pi_i\\pi_f=(-1)^L\\ (EL)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1739", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "07-nuclear-physics/nuclear-structure/exotic-nuclei-and-drip-lines", "name": "Laser spectroscopy of exotic-nucleus radii and moments", "kind": "method transfer", "summary": "Isotope shifts and hyperfine structure measured by collinear laser spectroscopy give charge radii, spins and moments of short-lived nuclei, revealing halos and shell evolution far from stability.", "map": "\\delta\\nu^{AA'}=K\\frac{m_{A'}-m_A}{m_Am_{A'}}+F\\,\\delta\\langle r^2\\rangle^{AA'}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1740", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "07-nuclear-physics/nuclear-structure/nuclear-forces-and-chiral-eft", "name": "Nuclear anapole moments from atomic parity violation", "kind": "method transfer", "summary": "The nuclear-spin-dependent part of Cs parity violation revealed the nuclear anapole moment, a probe of the parity-violating nucleon-nucleon (weak meson-exchange) interaction.", "map": "H_{\\rm PV}\\propto\\kappa_a\\,\\boldsymbol\\alpha\\cdot\\mathbf I\\,\\rho(r)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1741", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "07-nuclear-physics/nuclear-structure/superheavy-elements", "name": "Laser spectroscopy of superheavy atoms", "kind": "method transfer", "summary": "Atom-at-a-time resonance ionization spectroscopy of nobelium measures level energies where relativistic effects reshape atomic structure, testing relativistic many-body theory and giving nuclear moments.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1742", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "07-nuclear-physics/heavy-ion-physics/collective-flow-and-hydrodynamics", "name": "Elliptic flow of unitary gases and the QGP", "kind": "analogy", "summary": "Strongly interacting Fermi gases released from anisotropic traps expand elliptically like the QGP's elliptic flow; both are nearly perfect fluids with eta/s near hbar/4 pi k_B.", "map": "\\eta/s\\gtrsim\\hbar/4\\pi k_B;\\ v_2\\leftrightarrow\\text{aspect-ratio inversion}", "breaks": "Non-relativistic vs relativistic hydrodynamics; scales differ by ~1e19 in temperature; the QGP has gauge degrees of freedom and a crossover, the gas has none.", "confidence": "established", "strength": 3}
{"id": "C1743", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "07-nuclear-physics/heavy-ion-physics/qcd-phase-diagram-and-critical-point", "name": "Cold-atom analogues of colour superfluidity", "kind": "analogy", "summary": "Three-component Fermi gases with attractive interactions can form colour-superfluid and trion ('baryon') phases, an analogue of colour superconductivity and confinement in the dense QCD phase diagram.", "map": "", "breaks": "No gauge field or gluon dynamics; trion formation is not confinement; densities map only qualitatively.", "confidence": "proposed", "strength": 1}
{"id": "C1744", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "name": "Unitary Fermi gas and dilute neutron matter", "kind": "mechanism", "summary": "The neutron-neutron scattering length (-18.5 fm) far exceeds the effective range, so low-density neutron matter is close to the unitary Fermi gas realized at Feshbach resonances; the measured Bertsch parameter benchmarks neutron-star crust EOS calculations.", "map": "E/N=\\xi\\,\\tfrac35E_F,\\ \\xi\\approx0.37;\\ k_F|a_{nn}|\\gg1\\gg k_Fr_e", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1745", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process", "name": "Hoyle state as an alpha-particle condensate", "kind": "analogy", "summary": "The 7.65 MeV Hoyle state of carbon-12 that enables triple-alpha burning has been described as a dilute gas of alpha clusters occupying one orbital, a nuclear analogue of a Bose condensate.", "map": "", "breaks": "Only three or four bosons with Pauli effects among constituent nucleons; the condensate fraction is model dependent and debated.", "confidence": "current research", "strength": 1}
{"id": "C1746", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "name": "Feshbach resonances: from nuclear reactions to cold atoms", "kind": "historical", "summary": "Feshbach developed closed-channel resonance theory for nuclear reactions; the same coupled-channel physics, tuned by magnetic field, became the main tool for controlling interactions in ultracold gases.", "map": "a(B)=a_{bg}\\left(1-\\frac{\\Delta}{B-B_0}\\right)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1747", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "BCS pairing in nuclei and Fermi gases", "kind": "mechanism", "summary": "Odd-even mass staggering and moments of inertia reflect BCS-like pairing in finite nuclei, the same gap equation as in BEC-BCS-crossover Fermi gases, with the cold-atom crossover a tunable laboratory for the regime. See the pairing-across-scales theme.", "map": "\\Delta=-\\sum_k V_{kk'}\\frac{\\Delta}{2E_k},\\ \\Delta_{\\rm nuc}\\approx12A^{-1/2}\\,\\mathrm{MeV}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1748", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Scissors modes in deformed nuclei and BECs", "kind": "analogy", "summary": "The scissors mode, a counter-rotation of proton and neutron clouds discovered in deformed nuclei, was predicted and observed in anisotropic BECs as a signature of superfluid irrotational flow.", "map": "\\omega_{\\rm sc}=\\sqrt{\\omega_x^2+\\omega_y^2}\\ \\text{(superfluid BEC)}", "breaks": "In nuclei the mode is a proton-neutron relative rotation in a finite fermion system; in a BEC it is the tilt oscillation of a single bosonic superfluid.", "confidence": "established", "strength": 2}
{"id": "C1749", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/laser-cooling-and-trapping", "b": "07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions", "name": "Laser-trapped radioactive atoms for weak-interaction tests", "kind": "method transfer", "summary": "Magneto-optical and dipole traps hold short-lived radioactive atoms nearly at rest, so recoiling nuclei and beta-neutrino angular correlations can be measured cleanly to search for scalar and tensor weak currents.", "map": "\\frac{d\\Gamma}{d\\Omega}\\propto1+a_{\\beta\\nu}\\frac{\\mathbf p_e\\cdot\\mathbf p_\\nu}{E_eE_\\nu}+b\\frac{m_e}{E_e}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1750", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/lindblad-master-equations", "b": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "name": "Quarkonium in the QGP as an open quantum system", "kind": "method transfer", "summary": "Heavy quark-antiquark pairs coupled to the QGP bath obey Lindblad equations derived from pNRQCD, describing screening, dissociation and regeneration of quarkonia beyond rate equations.", "map": "\\dot\\rho=-i[H,\\rho]+\\sum_n(C_n\\rho C_n^\\dagger-\\tfrac12\\{C_n^\\dagger C_n,\\rho\\})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1751", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "name": "Random-matrix theory began with nuclear resonances", "kind": "historical", "summary": "Wigner and Dyson introduced random matrices to model neutron-resonance spacings in heavy nuclei; the nuclear data ensemble later anchored the Bohigas-Giannoni-Schmit link between classical chaos and Wigner-Dyson statistics.", "map": "P_{\\rm GOE}(s)\\approx\\frac{\\pi s}{2}e^{-\\pi s^2/4};\\ \\text{Porter-Thomas widths}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1752", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth", "b": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "name": "Thermalization of an isolated QCD system", "kind": "mechanism", "summary": "Heavy-ion collisions pose the isolated-system thermalization problem at strong coupling: how a far-from-equilibrium gluon state reaches hydrodynamic behaviour in ~1 fm/c, with links to prethermalization and non-thermal fixed points studied in cold atoms.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1753", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "name": "Compound nucleus as a thermalizing system", "kind": "mechanism", "summary": "Bohr's compound nucleus forgets how it was formed and decays statistically, an early instance of an isolated many-body quantum system thermalizing; Hauser-Feshbach and evaporation theory use nuclear temperature.", "map": "\\sigma_{ab}=\\sigma_{\\rm CN}(a)\\frac{\\Gamma_b}{\\Gamma};\\ \\rho(E)\\propto e^{2\\sqrt{aE}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1754", "a": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "b": "07-nuclear-physics/hadron-and-nucleon-structure/parton-distribution-functions", "name": "Entanglement entropy in deep inelastic scattering", "kind": "method transfer", "summary": "The parton distribution probed at small x has been interpreted as the entanglement entropy between the probed region and the rest of the proton, linking DIS multiplicities to quantum information.", "map": "S(x)\\approx\\ln[xG(x)]", "breaks": "", "confidence": "proposed", "strength": 1}
{"id": "C1755", "a": "04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity", "b": "07-nuclear-physics/nuclear-structure/ab-initio-nuclear-theory", "name": "Quantum computing of nuclear ground states", "kind": "method transfer", "summary": "Variational quantum eigensolvers computed the deuteron binding energy from pionless/chiral EFT Hamiltonians on cloud processors, a first step toward quantum simulation of nuclear many-body problems.", "map": "E(\\theta)=\\langle\\psi(\\theta)|H_{\\rm EFT}|\\psi(\\theta)\\rangle\\ge E_0", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1756", "a": "04-quantum-physics/quantum-information-and-computation/superconducting-qubits", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Odd-even pairing effects in nuclei and SC islands", "kind": "mechanism", "summary": "Small superconducting islands show an even-odd ground-state energy difference from an unpaired quasiparticle, the same blocking effect behind nuclear odd-even mass staggering; quasiparticle poisoning of charge qubits is its device consequence.", "map": "\\Delta E_{\\rm odd-even}\\approx\\Delta\\ (\\text{gap});\\ E_{\\rm odd}-E_{\\rm even}=\\Delta-k_BT\\ln N_{\\rm eff}", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1757", "a": "04-quantum-physics/quantum-information-and-computation/trapped-ion-and-neutral-atom-qubits", "b": "07-nuclear-physics/nuclear-structure/exotic-nuclei-and-drip-lines", "name": "Penning-trap mass spectrometry", "kind": "method transfer", "summary": "Ion-trap techniques measure masses of exotic nuclei to 1e-8 or better via cyclotron frequencies, fixing separation energies, shell gaps and drip lines.", "map": "\\nu_c=\\frac{qB}{2\\pi m};\\ S_n=B(A,Z)-B(A-1,Z)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1758", "a": "04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Spin-orbit coupling and magic numbers", "kind": "method transfer", "summary": "A strong nuclear spin-orbit term splits j=l+-1/2 levels and reproduces the magic numbers; jj-coupling, Clebsch-Gordan and Wigner-Eckart machinery from atomic physics then organizes shell-model states.", "map": "V_{ls}(r)\\,\\mathbf l\\cdot\\mathbf s:\\ \\Delta E=\\frac{\\hbar^2}{2}(2l+1)\\langle V_{ls}\\rangle", "breaks": "Same operator algebra but different physics: nuclear spin-orbit is a strong-interaction effect, ~20x larger relative to level spacing, with inverted ordering relative to atomic fine structure.", "confidence": "established", "strength": 3}
{"id": "C1759", "a": "04-quantum-physics/quantum-mechanics-core/approximation-methods", "b": "07-nuclear-physics/nuclear-reactions-and-decays/fusion-reactions", "name": "WKB tunnelling and the Gamow peak", "kind": "mechanism", "summary": "Thermonuclear fusion proceeds by WKB tunnelling through the Coulomb barrier; the product of Maxwell-Boltzmann tail and penetrability gives the Gamow peak that sets stellar and fusion-reactor rates.", "map": "E_0=\\left[\\left(\\frac{\\pi\\alpha Z_1Z_2k_BT}{\\sqrt2}\\right)^2\\mu c^2\\right]^{1/3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1760", "a": "04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems", "b": "07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay", "name": "Alpha decay as Coulomb-barrier tunnelling", "kind": "mechanism", "summary": "Gamow and Gurney-Condon explained alpha decay as tunnelling through the Coulomb barrier; the barrier-penetration factor gives the Geiger-Nuttall law spanning 20+ orders of magnitude in half-life.", "map": "P\\approx\\exp\\left(-\\frac2\\hbar\\int_R^{r_c}\\sqrt{2\\mu(V-E)}dr\\right);\\ \\log t_{1/2}=a\\frac{Z}{\\sqrt{Q_\\alpha}}+b", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1761", "a": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-fission", "name": "Least-action paths for spontaneous fission", "kind": "method transfer", "summary": "Spontaneous-fission lifetimes are computed as imaginary-time tunnelling along least-action paths in a multidimensional collective space, an instanton/WKB calculation with a coordinate-dependent inertia.", "map": "S=\\int_{s_1}^{s_2}\\sqrt{2\\mathcal M(s)[V(s)-E]}\\,ds/\\hbar,\\ T_{1/2}\\propto e^{2S}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1762", "a": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "b": "07-nuclear-physics/nuclear-reactions-and-decays", "name": "Coulomb wavefunctions and the Gamow factor", "kind": "identity", "summary": "Charged-particle reaction rates factor into a smooth astrophysical S-factor and the Sommerfeld/Gamow penetrability that comes from exact Coulomb scattering wavefunctions at the origin.", "map": "\\sigma(E)=\\frac{S(E)}{E}e^{-2\\pi\\eta},\\ \\eta=\\frac{Z_1Z_2e^2}{4\\pi\\epsilon_0\\hbar v}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1763", "a": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "name": "Partial waves, resonances and the optical model", "kind": "method transfer", "summary": "Nuclear reaction theory is applied quantum scattering theory: phase shifts and partial waves, Breit-Wigner compound resonances, the complex optical potential (absorption via Im V), and R-matrix fits of cross sections.", "map": "\\sigma_{\\rm BW}=\\frac{\\pi}{k^2}g\\frac{\\Gamma_a\\Gamma_b}{(E-E_R)^2+\\Gamma^2/4};\\ U=V+iW", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1764", "a": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "b": "07-nuclear-physics/nuclear-structure/nuclear-forces-and-chiral-eft", "name": "Large scattering length: pionless EFT and cold atoms", "kind": "mechanism", "summary": "Pionless EFT for nucleons and the effective theory of Feshbach-tuned atoms share universal large-scattering-length physics: shallow dimers (deuteron), the three-body parameter and Efimov-like states in nuclei and halos.", "map": "f(k)=\\frac{1}{-1/a+r_ek^2/2-ik};\\ E_B\\approx\\hbar^2/ma^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1765", "a": "04-quantum-physics/quantum-optics/single-photon-sources-and-detectors", "b": "07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry", "name": "Photon-counting detectors shared with radiation detection", "kind": "shared object", "summary": "Scintillation and gamma spectroscopy rely on single-photon-sensitive photodetectors (PMTs, SiPMs), while transition-edge-sensor microcalorimeters developed for quantum optics give eV resolution for gamma and X-ray lines.", "map": "\\frac{\\sigma_E}{E}=2.355\\sqrt{\\frac{Fw}{E}}", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C2003", "a": "05-relativity-and-gravitation/black-holes/black-hole-thermodynamics-and-hawking-radiation", "b": "07-nuclear-physics/heavy-ion-physics/qcd-phase-diagram-and-critical-point", "name": "Hawking-Page transition as deconfinement", "kind": "duality", "summary": "In AdS, thermal gas and large black holes exchange dominance at the Hawking-Page temperature; holographically this is the confinement-deconfinement transition of the boundary gauge theory, with free energy jumping from O(N^0) to O(N^2).", "map": "", "breaks": "Holographic transition is first-order at large N; QCD with physical quarks is a crossover at mu_B=0.", "confidence": "established", "strength": 2}
{"id": "C2004", "a": "05-relativity-and-gravitation/general-relativity/einstein-field-equations", "b": "07-nuclear-physics/hadron-and-nucleon-structure/nucleon-spin-and-form-factors", "name": "Gravitational form factors and proton pressure", "kind": "shared object", "summary": "Matrix elements of the QCD energy-momentum tensor, the source of gravity, define the proton's gravitational form factors A, B, D; Ji's sum rule gives quark angular momentum and the D-term gives the internal pressure, extracted from deeply virtual Compton scattering.", "map": "\\langle p'|T^{\\mu\\nu}|p\\rangle\\ni A(t)\\bar P^\\mu\\bar P^\\nu+\\tfrac{D(t)}{4}(\\Delta^\\mu\\Delta^\\nu-g^{\\mu\\nu}\\Delta^2),\\quad J_q=\\tfrac12[A_q(0)+B_q(0)]", "breaks": "Direct graviton scattering is unmeasurable; extraction relies on GPD models and dispersion relations, so the pressure profile is model dependent.", "confidence": "current research", "strength": 2}
{"id": "C2005", "a": "05-relativity-and-gravitation/general-relativity/einstein-field-equations", "b": "07-nuclear-physics/heavy-ion-physics/collective-flow-and-hydrodynamics", "name": "Israel-Stewart causal hydrodynamics", "kind": "method transfer", "summary": "First-order (Navier-Stokes) relativistic viscous hydrodynamics is acausal and unstable; Israel and Stewart's second-order theory, built for relativistic fluids in GR, relaxes the shear tensor over a time tau_pi and underlies modern heavy-ion hydrodynamics.", "map": "\\tau_\\pi\\dot\\pi^{\\langle\\mu\\nu\\rangle}+\\pi^{\\mu\\nu}=-2\\eta\\sigma^{\\mu\\nu}+\\dots,\\quad \\nabla_\\mu T^{\\mu\\nu}=0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2006", "a": "05-relativity-and-gravitation/general-relativity/einstein-field-equations", "b": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "name": "TOV equation: GR hydrostatics of nuclear matter", "kind": "identity", "summary": "The Einstein equations for a static perfect-fluid sphere give the Tolman-Oppenheimer-Volkoff equation; each nuclear EOS P(epsilon) maps to a unique mass-radius curve and maximum mass, so 2 M_sun pulsars rule out soft EOSs.", "map": "\\frac{dP}{dr}=-\\frac{G(\\varepsilon+P)(m+4\\pi r^3P/c^2)}{c^2r(r-2Gm/c^2)}\\ \\leftarrow\\ G_{\\mu\\nu}=8\\pi GT_{\\mu\\nu}^{\\rm fluid}/c^4", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2007", "a": "05-relativity-and-gravitation/general-relativity/modified-gravity", "b": "07-nuclear-physics/nuclear-astrophysics/big-bang-nucleosynthesis", "name": "BBN constrains G and extra gravitational fields", "kind": "method transfer", "summary": "The neutron-proton freeze-out temperature depends on the expansion rate H proportional to sqrt(G rho); primordial helium and deuterium bound any change of G between BBN and today to roughly 10-20% and limit scalar-tensor and extra-radiation models.", "map": "H^2=\\frac{8\\pi G}{3}\\rho_{\\rm rad},\\quad \\frac{\\Gamma_{np}}{H}\\sim\\left(\\frac{T}{0.8\\,\\text{MeV}}\\right)^3,\\quad \\Delta Y_p\\simeq0.08\\,\\frac{\\Delta G}{G}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2008", "a": "05-relativity-and-gravitation/general-relativity/numerical-relativity", "b": "07-nuclear-physics/heavy-ion-physics/qcd-phase-diagram-and-critical-point", "name": "Mergers probe a hadron-quark phase transition", "kind": "shared object", "summary": "Neutron-star merger remnants reach several times saturation density at T of tens of MeV, a region of the QCD phase diagram heavy-ion collisions cannot reach; a strong first-order transition shifts the post-merger GW frequency away from the hadronic f2-radius relation.", "map": "", "breaks": "Post-merger signals at kHz are below current sensitivity; the signature requires third-generation detectors.", "confidence": "current research", "strength": 2}
{"id": "C2009", "a": "05-relativity-and-gravitation/general-relativity/numerical-relativity", "b": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "name": "Merger simulations with nuclear EOS", "kind": "method transfer", "summary": "GR hydrodynamic simulations of binary neutron-star mergers with tabulated finite-temperature nuclear EOSs predict prompt-collapse thresholds, remnant lifetimes and the post-merger f2 frequency, which correlates with stellar radius.", "map": "f_2\\approx\\text{few kHz},\\quad f_2\\propto\\sqrt{M/R^3};\\quad M_{\\rm thr}\\approx k\\,M_{\\rm max}^{\\rm TOV},\\ k\\sim1.3\\text{--}1.7", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2010", "a": "05-relativity-and-gravitation/general-relativity/numerical-relativity", "b": "07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process", "name": "Merger ejecta and electron fraction from NR", "kind": "method transfer", "summary": "Which nuclei a merger makes depends on the ejecta electron fraction Y_e, set by shock heating and neutrino irradiation in NR simulations with neutrino transport; dynamical ejecta (Y_e < 0.25) make the third r-process peak, disk winds lighter elements.", "map": "", "breaks": "Nucleosynthesis yields are sensitive to neutrino transport approximations and to unmeasured masses of very neutron-rich nuclei.", "confidence": "current research", "strength": 2}
{"id": "C2011", "a": "05-relativity-and-gravitation/general-relativity/tests-of-general-relativity", "b": "07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay", "name": "Mossbauer gamma lines measured gravitational redshift", "kind": "method transfer", "summary": "Pound and Rebka resolved a fractional shift of 2.5e-15 over 22.5 m by using the recoil-free 14.4 keV nuclear gamma transition of Fe-57, whose natural linewidth made the nuclear transition a clock fine enough to see gravity.", "map": "\\frac{\\Delta\\nu}{\\nu}=\\frac{gh}{c^2}=2.5\\times10^{-15}\\ (h=22.5\\ \\text{m}),\\quad \\Gamma/E_\\gamma\\approx3\\times10^{-13}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2012", "a": "05-relativity-and-gravitation/general-relativity/tests-of-general-relativity", "b": "07-nuclear-physics/nuclear-structure", "name": "Equivalence-principle tests weigh nuclear binding", "kind": "shared object", "summary": "Eotvos-type and MICROSCOPE tests compare materials whose mass-energy differs in nuclear binding and Coulomb energy fractions; a violating dilaton couples to these 'charges', so nuclear structure (B/A, Z(Z-1)/A^{4/3}) sets what an EP test probes.", "map": "\\eta=2\\frac{|a_A-a_B|}{a_A+a_B},\\quad \\frac{m_g}{m_i}=1+\\sum_k\\eta_k\\frac{E_k}{mc^2}\\ (k=\\text{strong, EM, weak})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2013", "a": "05-relativity-and-gravitation/gravitational-waves/gravitational-wave-theory-and-waveforms", "b": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "name": "Love numbers enter the 5PN waveform phase", "kind": "shared object", "summary": "The quadrupole induced by the companion's tidal field, Q = -lambda E, adds a term scaling as Lambda (v/c)^10 to the inspiral phase; computing k_2 needs a perturbed TOV solution, so EOS physics enters waveform models directly.", "map": "Q_{ij}=-\\lambda\\mathcal E_{ij},\\ \\lambda=\\tfrac{2}{3G}k_2R^5,\\quad \\delta\\Psi(f)=-\\tfrac{39}{2}\\tilde\\Lambda\\,x^{5/2}\\,(\\ldots),\\ x=(\\pi GMf/c^3)^{2/3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2014", "a": "05-relativity-and-gravitation/gravitational-waves/ground-based-detections", "b": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "name": "Tidal deformability from GW170817", "kind": "shared object", "summary": "Tidal deformation of inspiralling neutron stars shifts the GW phase; GW170817 bounded the combined tidal deformability and hence radii near 11-13 km, excluding the stiffest nuclear equations of state.", "map": "\\Lambda=\\tfrac23k_2\\left(\\frac{c^2R}{GM}\\right)^5,\\quad \\tilde\\Lambda_{\\rm GW170817}\\lesssim720,\\ R_{1.4}\\approx11.9^{+1.4}_{-1.4}\\ \\text{km}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2015", "a": "05-relativity-and-gravitation/gravitational-waves/ground-based-detections", "b": "07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process", "name": "GW170817 kilonova as an r-process site", "kind": "shared object", "summary": "The GW-localized merger GW170817 produced a kilonova whose red, lanthanide-rich emission powered by r-process decay showed that neutron-star mergers make heavy elements, tying nuclear masses and beta rates to GW sources.", "map": "L(t)\\propto M_{\\rm ej}\\,\\dot\\epsilon(t),\\ \\dot\\epsilon\\propto t^{-1.3};\\quad M_{\\rm ej}\\sim0.05\\,M_\\odot", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2016", "a": "05-relativity-and-gravitation/gravitational-waves/space-based-and-future-detectors", "b": "07-nuclear-physics/nuclear-astrophysics/big-bang-nucleosynthesis", "name": "BBN bound on primordial GW backgrounds", "kind": "shared object", "summary": "Any primordial GW background present before BBN is extra radiation and raises N_eff; the light-element abundances cap its integrated energy density, a benchmark that LISA and PTA cosmological interpretations must respect.", "map": "\\int\\Omega_{\\rm gw}(f)h^2\\,d\\ln f\\lesssim5.6\\times10^{-6}\\,\\Delta N_{\\rm eff}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2017", "a": "05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft", "b": "07-nuclear-physics/heavy-ion-physics", "name": "Holographic thermalization of heavy-ion collisions", "kind": "duality", "summary": "Colliding gravitational shock waves in AdS5 form a black brane within about 1/T, modelling rapid hydrodynamization of the fireball; horizon formation plays the role of thermalization.", "map": "", "breaks": "Infinite-coupling, infinite-N model; real collisions have weak-coupling early stages (glasma) and finite N.", "confidence": "current research", "strength": 2}
{"id": "C2018", "a": "05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft", "b": "07-nuclear-physics/heavy-ion-physics/collective-flow-and-hydrodynamics", "name": "Fluid/gravity correspondence", "kind": "duality", "summary": "Slowly varying black branes in AdS5 are dual to solutions of relativistic viscous hydrodynamics; the bulk Einstein equations order by order in gradients yield the transport coefficients of second-order hydrodynamics used in heavy-ion codes.", "map": "\\partial_\\mu T^{\\mu\\nu}=0,\\ T^{\\mu\\nu}=(\\varepsilon+P)u^\\mu u^\\nu+Pg^{\\mu\\nu}-2\\eta\\sigma^{\\mu\\nu}+\\dots\\ \\leftrightarrow\\ \\text{boosted black brane}(u^\\mu(x),T(x))", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2019", "a": "05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft", "b": "07-nuclear-physics/heavy-ion-physics/jet-quenching", "name": "Trailing strings and holographic jet quenching", "kind": "duality", "summary": "A heavy quark crossing a strongly coupled plasma is a string trailing into a black-brane horizon; the drag force and jet quenching parameter q-hat follow in closed form, giving estimates comparable to RHIC/LHC energy-loss data.", "map": "\\frac{dp}{dt}=-\\frac{\\pi\\sqrt\\lambda}{2}T^2\\frac{v}{\\sqrt{1-v^2}},\\qquad \\hat q=\\frac{\\pi^{3/2}\\Gamma(3/4)}{\\Gamma(5/4)}\\sqrt\\lambda\\,T^3", "breaks": "N=4 SYM rather than QCD, and the perturbative early-time regime of jets is missing.", "confidence": "current research", "strength": 2}
{"id": "C2020", "a": "05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft", "b": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "name": "eta/s = 1/4pi from black-brane horizons", "kind": "duality", "summary": "Shear viscosity of a strongly coupled plasma equals the absorption of gravitons by a black-brane horizon; for every two-derivative gravity dual eta/s = hbar/4pi k_B, close to the small eta/s extracted from RHIC/LHC flow.", "map": "\\frac{\\eta}{s}=\\frac{\\hbar}{4\\pi k_B}\\quad(\\sigma_{\\rm abs}(0)=A_H\\Rightarrow\\eta=\\tfrac{A_H}{16\\pi G},\\ s=\\tfrac{A_H}{4G})", "breaks": "N=4 SYM is conformal, supersymmetric and large-N; QCD near T_c is none of these, and the 1/4pi value is violated by higher-curvature corrections.", "confidence": "current research", "strength": 3}
{"id": "C2021", "a": "05-relativity-and-gravitation/quantum-gravity/qft-in-curved-spacetime", "b": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "name": "Hadronization as Unruh radiation", "kind": "analogy", "summary": "Thermal hadron yields with a universal T near 160 MeV in e+e-, pp and AA have been modelled as Unruh radiation from quarks decelerated by the string tension at a confinement horizon, with T = a/2pi and a ~ sqrt(sigma).", "map": "T_U=\\frac{\\hbar a}{2\\pi ck_B},\\ a\\simeq\\sqrt{2\\pi\\sigma}\\Rightarrow T\\approx\\sqrt{\\sigma/2\\pi}\\approx170\\ \\text{MeV}", "breaks": "The confinement 'horizon' is not a spacetime horizon; universal thermal yields also follow from statistical hadronization without any Unruh mechanism.", "confidence": "proposed", "strength": 1}
{"id": "C2022", "a": "05-relativity-and-gravitation/special-relativity/lorentz-transformations-and-spacetime", "b": "07-nuclear-physics/heavy-ion-physics/collective-flow-and-hydrodynamics", "name": "Rapidity and Bjorken boost-invariant flow", "kind": "method transfer", "summary": "Lorentz boosts along the beam add rapidities, so a boost-invariant expansion depends only on proper time tau; Bjorken's solution of relativistic hydrodynamics gives the initial energy-density estimate used in every heavy-ion analysis.", "map": "\\tau=\\sqrt{t^2-z^2},\\ \\eta_s=\\tanh^{-1}(z/t),\\ v_z=z/t;\\quad \\varepsilon\\propto\\tau^{-4/3},\\ \\epsilon_{\\rm Bj}=\\frac{1}{\\pi R^2\\tau_0}\\frac{dE_T}{dy}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2023", "a": "05-relativity-and-gravitation/special-relativity/relativistic-kinematics-and-dynamics", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "name": "Q-values and the direct test of E=mc^2", "kind": "shared object", "summary": "Nuclear reaction energetics are mass-energy equivalence in action: Q = (sum m_i - sum m_f)c^2; comparing neutron-capture gamma energies with Penning-trap mass differences verified E=mc^2 to 4e-7.", "map": "Q=\\Big(\\sum m_i-\\sum m_f\\Big)c^2,\\qquad 1-\\frac{\\Delta mc^2}{E_\\gamma}=(-1.4\\pm4.4)\\times10^{-7}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2024", "a": "05-relativity-and-gravitation/special-relativity/tests-of-lorentz-invariance", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Hughes-Drever tests with nuclear spins", "kind": "method transfer", "summary": "Nuclear magnetic resonance of nuclei with J > 1/2 (Li-7, and modern He-3/Xe-129 comagnetometers) searches for quadrupole splitting varying with sidereal orientation; shell-model wavefunctions convert the bounds into limits on proton and neutron SME coefficients near 1e-30 GeV.", "map": "", "breaks": "Interpreting a bound requires a nuclear model of which nucleons carry the spin, adding model dependence.", "confidence": "established", "strength": 2}