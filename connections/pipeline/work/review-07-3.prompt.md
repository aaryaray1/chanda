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

# Packet 07-3 (100 records)

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
{"id": "C2414", "a": "07-nuclear-physics/applied-nuclear-physics/nuclear-data-and-isotope-production", "b": "07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process", "name": "Mass and decay evaluations drive nucleosynthesis networks", "kind": "method transfer", "summary": "AME masses, NUBASE/ENSDF half-lives, and Maxwellian-averaged (n,γ) cross sections at kT≈30 keV from evaluated libraries feed the s- and r-process reaction networks. Sensitivity studies rank unmeasured masses and half-lives by their effect on abundances, and that ranking steers measurements at radioactive-beam facilities.", "map": "\\langle\\sigma\\rangle_{kT}=\\frac{2}{\\sqrt\\pi}\\frac{\\int\\sigma(E)E\\,e^{-E/kT}dE}{\\int E\\,e^{-E/kT}dE}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2415", "a": "07-nuclear-physics/applied-nuclear-physics/nuclear-data-and-isotope-production", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "name": "Reaction theory feeds evaluated cross-section libraries", "kind": "method transfer", "summary": "Evaluated libraries (ENDF/B, JEFF, JENDL) combine measurements with reaction theory, each with covariances: R-matrix and Breit–Wigner fits in the resolved-resonance region, and Hauser–Feshbach compound-nucleus and optical-model calculations elsewhere. The same activation cross sections set isotope-production yields.", "map": "\\sigma(E)=\\pi\\bar\\lambda^2 g\\,\\frac{\\Gamma_a\\Gamma_b}{(E-E_r)^2+\\Gamma^2/4}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2416", "a": "07-nuclear-physics/applied-nuclear-physics/nuclear-reactors-and-energy", "b": "07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions", "name": "Fission-product beta decay: delayed neutrons, decay heat", "kind": "mechanism", "summary": "About 0.65% of ²³⁵U fission neutrons are β-delayed, emitted after precursor half-lives of about 0.2–56 s, and they stretch reactor kinetics to controllable timescales. β decay of fission products also supplies about 6–7% of full power as decay heat just after shutdown, and the reactor antineutrino flux.", "map": "\\beta_{\\rm eff}\\approx0.0065\\ (^{235}\\mathrm U);\\quad P(t)/P_0\\approx0.066\\,t^{-0.2}\\ (t\\text{ in s})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2417", "a": "07-nuclear-physics/applied-nuclear-physics/nuclear-reactors-and-energy", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-fission", "name": "Fission physics sets reactor criticality", "kind": "mechanism", "summary": "Each fission releases about 200 MeV and about 2.4 prompt neutrons. Reactor multiplication is built from fission and absorption cross sections and ν̄. Pairing energy lets odd-N ²³⁵U fission with thermal neutrons, while ²³⁸U needs fast neutrons above a threshold.", "map": "k_\\infty=\\eta f p\\varepsilon,\\quad \\eta=\\bar\\nu\\,\\sigma_f/\\sigma_a", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2418", "a": "07-nuclear-physics/applied-nuclear-physics/nuclear-reactors-and-energy", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "name": "Neutron moderation and resonance absorption", "kind": "mechanism", "summary": "Reactor physics is applied low-energy neutron reaction theory. Elastic scattering moderates neutrons (mean lethargy gain ξ, equal to 1 for hydrogen), and Breit–Wigner resonances of ²³⁸U set the resonance-escape probability p. Doppler broadening of those resonances gives the prompt negative fuel-temperature coefficient.", "map": "\\xi=1+\\frac{(A-1)^2}{2A}\\ln\\frac{A-1}{A+1}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2419", "a": "07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry", "b": "07-nuclear-physics/heavy-ion-physics/jet-quenching", "name": "Radiative energy loss: QED in matter vs QCD in plasma", "kind": "analogy", "summary": "Medium-induced gluon bremsstrahlung (BDMPS-Z) is the QCD counterpart of radiative energy loss in matter, and it inherits the LPM coherence suppression first found in QED showers. Collisional loss plays the role of Bethe–Bloch ionization.", "map": "\\Delta E_{\\rm QCD}\\simeq\\frac{\\alpha_sC_R}{4}\\hat q L^2\\quad\\text{vs}\\quad -\\left.\\frac{dE}{dx}\\right|_{\\rm QED,rad}=\\frac{E}{X_0}", "breaks": "Radiated gluons carry color and rescatter, so ΔE grows as L² instead of L. The medium is an expanding hot plasma rather than a cold absorber, so q̂ depends on temperature and time instead of being a material constant.", "confidence": "established", "strength": 2}
{"id": "C2420", "a": "07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Gamma-ray arrays map nuclear level schemes", "kind": "method transfer", "summary": "Compton-suppressed HPGe arrays (Gammasphere, and now AGATA and GRETA with γ-ray tracking), with ≈2 keV resolution at 1.33 MeV, resolve high-spin cascades. That resolution is what revealed rotational and superdeformed bands, band crossings and shell evolution, and the arrays are the workhorse instruments of in-beam structure studies.", "map": "E(I)=\\frac{\\hbar^2}{2\\mathcal I}I(I+1),\\quad E_\\gamma=E(I)-E(I-2)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2421", "a": "07-nuclear-physics/hadron-and-nucleon-structure/electron-ion-collider", "b": "07-nuclear-physics/heavy-ion-physics/collective-flow-and-hydrodynamics", "name": "Gluon saturation sets hydrodynamic initial conditions", "kind": "mechanism", "summary": "The color-glass-condensate picture of high-energy nuclei, with a saturation scale Q_s² ∝ A^{1/3}, underlies initial-state models such as IP-Glasma. Their event-by-event geometric fluctuations become the flow harmonics v_n. The EIC will measure nuclear gluon densities and Q_s directly in e–A collisions.", "map": "Q_s^2\\propto A^{1/3}x^{-\\lambda},\\ \\lambda\\approx0.3;\\quad v_n\\propto\\varepsilon_n", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2422", "a": "07-nuclear-physics/hadron-and-nucleon-structure/electron-ion-collider", "b": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "name": "Trace anomaly: nucleon mass and QGP ε−3P", "kind": "identity", "summary": "One operator, the QCD energy-momentum trace including the gluon anomaly, gives both the nucleon mass (an EIC target through threshold J/ψ production) and the QGP interaction measure (ε−3P)/T⁴. Lattice QCD finds the interaction measure peaks just above T_c.", "map": "\\Theta^\\mu_\\mu=\\frac{\\beta(g)}{2g}G^a_{\\mu\\nu}G^{a\\mu\\nu}+\\sum_q m_q\\bar qq;\\ M_N\\propto\\langle N|\\Theta^\\mu_\\mu|N\\rangle,\\ \\varepsilon-3P=\\langle\\Theta^\\mu_\\mu\\rangle_T", "breaks": "The proton-mass decomposition is scheme-dependent, and how threshold J/ψ data relate to the gluon anomaly term is disputed.", "confidence": "current research", "strength": 2}
{"id": "C2423", "a": "07-nuclear-physics/hadron-and-nucleon-structure/nucleon-spin-and-form-factors", "b": "07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions", "name": "g_A links neutron decay to nucleon structure", "kind": "identity", "summary": "g_A = G_A(0) ≈ 1.27 is the nucleon axial form factor at zero momentum transfer. It is measured in neutron-decay asymmetries and computed in lattice QCD. The neutron lifetime depends on g_A and on V_ud, which superallowed 0⁺→0⁺ decays fix independently.", "map": "\\tau_n^{-1}\\propto G_F^2|V_{ud}|^2(1+3g_A^2);\\quad g_A=G_A(Q^2{=}0)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2424", "a": "07-nuclear-physics/hadron-and-nucleon-structure/parton-distribution-functions", "b": "07-nuclear-physics/heavy-ion-physics/jet-quenching", "name": "Nuclear PDFs as the baseline for jet quenching", "kind": "method transfer", "summary": "Hard probes in A–A collisions are computed with collinear factorization. Nuclear PDFs (shadowing, antishadowing, the EMC effect), fixed by p–A and e–A data, remove initial-state effects so that R_AA isolates final-state energy loss in the QGP.", "map": "R_{AA}=\\frac{dN_{AA}/dp_T}{\\langle T_{AA}\\rangle\\,d\\sigma_{pp}/dp_T};\\quad \\sigma=f_A\\otimes f_A\\otimes\\hat\\sigma\\otimes D", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2425", "a": "07-nuclear-physics/hadron-and-nucleon-structure/parton-distribution-functions", "b": "07-nuclear-physics/nuclear-structure/nuclear-forces-and-chiral-eft", "name": "EMC effect tracks short-range NN correlations", "kind": "mechanism", "summary": "The EMC effect is the depletion of nuclear valence-quark distributions at 0.3<x<0.7. Its slope scales linearly across nuclei with the density of short-range-correlated pairs (a_2, from x>1 scattering). Those pairs are mostly np because of the tensor force, which suggests that high-momentum nucleons are the ones modified.", "map": "-\\frac{dR_{\\rm EMC}}{dx}\\propto a_2(A)", "breaks": "A correlation, not a proven cause: mean-field modification models also fit the data.", "confidence": "current research", "strength": 2}
{"id": "C2426", "a": "07-nuclear-physics/heavy-ion-physics/collective-flow-and-hydrodynamics", "b": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "name": "Heavy-ion flow and mergers constrain dense matter", "kind": "shared object", "summary": "Directed and elliptic flow in intermediate-energy heavy-ion collisions constrains the pressure of symmetric nuclear matter at about 2–4.5 n_0. Combined with chiral EFT and astrophysical data, these flow results tighten the neutron-star EOS. Neutron-star mergers reach similar densities and tens-of-MeV temperatures and are modelled with the same relativistic (viscous) hydrodynamics.", "map": "P(n)\\ \\text{at}\\ 2\\!-\\!4.5\\,n_0\\ \\text{(symmetric)}\\ +\\ S(n)\\delta^2\\ \\to\\ P_{\\rm NS}(n)", "breaks": "Collisions probe near-symmetric, hot, transient matter. Neutron stars are cold and very isospin-asymmetric, so the link needs the symmetry energy.", "confidence": "current research", "strength": 3}
{"id": "C2427", "a": "07-nuclear-physics/heavy-ion-physics/collective-flow-and-hydrodynamics", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Imaging nuclear deformation with collective flow", "kind": "method transfer", "summary": "In ultracentral collisions of deformed nuclei (²³⁸U, ¹²⁹Xe) and isobars (⁹⁶Ru/⁹⁶Zr), v₂ grows with the ground-state quadrupole deformation β₂² and is sensitive to triaxiality γ and neutron skins. Hydrodynamic flow thus becomes a snapshot probe of low-energy collective structure.", "map": "\\langle v_2^2\\rangle=a+b\\,\\beta_2^2;\\quad \\langle p_T\\rangle\\ \\text{fluctuations}\\ \\leftrightarrow\\ \\gamma", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2428", "a": "07-nuclear-physics/heavy-ion-physics/qcd-phase-diagram-and-critical-point", "b": "07-nuclear-physics/nuclear-astrophysics/big-bang-nucleosynthesis", "name": "QCD crossover vs inhomogeneous Big Bang nucleosynthesis", "kind": "historical", "summary": "A first-order cosmological QCD transition (~10 μs after the Big Bang) could have left baryon-density inhomogeneities with neutron–proton segregation, and in the 1980s this motivated inhomogeneous BBN. Lattice QCD shows a crossover at T≈155 MeV for small μ_B, and standard homogeneous BBN with the CMB baryon density fits D and ⁴He, so the scenario has lost its motivation.", "map": "T_c\\approx155\\,{\\rm MeV}\\ (t\\sim10\\,\\mu{\\rm s})\\ \\gg\\ T_{\\rm BBN}\\approx0.07\\,{\\rm MeV}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2429", "a": "07-nuclear-physics/heavy-ion-physics/qcd-phase-diagram-and-critical-point", "b": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "name": "Neutron-star cores probe cold dense QCD", "kind": "shared object", "summary": "Lattice QCD cannot reach the low-temperature, high-μ_B corner of the QCD phase diagram (quark-matter cores, color superconductivity, quarkyonic matter) because of the sign problem, and heavy-ion collisions cannot reach it either. Neutron-star masses, radii and tidal deformabilities are the only data there, and a sound speed rising above the conformal value is the sought signature.", "map": "c_s^2=\\partial P/\\partial\\varepsilon;\\ \\text{conformal limit } c_s^2\\to1/3", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2430", "a": "07-nuclear-physics/nuclear-astrophysics/big-bang-nucleosynthesis", "b": "07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions", "name": "Neutron lifetime sets primordial helium", "kind": "mechanism", "summary": "The weak n↔p rates freeze out near T≈0.8 MeV at n/p≈1/6. Free-neutron decay then lowers n/p to about 1/7 before the deuterium bottleneck breaks (T≈0.07 MeV), which gives Y_p≈0.25. τ_n normalizes all the weak rates, so the ~9 s beam–bottle lifetime discrepancy feeds directly into the predicted Y_p.", "map": "Y_p\\approx\\frac{2(n/p)}{1+n/p};\\quad \\Gamma_{n\\leftrightarrow p}\\propto\\tau_n^{-1}T^5", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2431", "a": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "b": "07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions", "name": "Beta equilibrium and Urca cooling in neutron stars", "kind": "mechanism", "summary": "Neutron-star matter sits in β equilibrium (μ_n = μ_p + μ_e), which together with the symmetry energy fixes the proton fraction. Above x_p ≈ 11–15%, direct Urca (n→p e ν̄, e p→n ν) becomes kinematically allowed and cools the star fast; below it only the slower modified Urca process operates.", "map": "\\mu_n-\\mu_p=\\mu_e\\approx4S(n)(1-2x_p);\\quad \\text{dUrca: }k_{F,n}\\le k_{F,p}+k_{F,e}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2432", "a": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "b": "07-nuclear-physics/nuclear-structure/exotic-nuclei-and-drip-lines", "name": "Neutron-rich nuclei form the neutron-star crust", "kind": "shared object", "summary": "The outer crust is a Coulomb lattice of nuclei that become more neutron-rich with depth, from ⁵⁶Fe through N=50 nuclei near ⁷⁸Ni–⁸²Zn to N=82 isotones. Its composition follows from measured and extrapolated masses. The inner crust starts at neutron drip, where S_n→0.", "map": "\\min\\ g(P)=\\mu_b\\ \\text{per baryon};\\quad \\rho_{\\rm drip}\\approx4\\times10^{11}\\,{\\rm g\\,cm^{-3}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2433", "a": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "b": "07-nuclear-physics/nuclear-structure/nuclear-forces-and-chiral-eft", "name": "Chiral-EFT neutron matter anchors the neutron-star EOS", "kind": "method transfer", "summary": "Chiral NN+3N forces, solved with quantum Monte Carlo, many-body perturbation theory or coupled cluster, give the pure-neutron-matter energy with quantified truncation errors up to about 1–2 n_0. This fixes the symmetry energy S_0 and its slope L and predicts R_1.4 ≈ 11–13 km. Three-nucleon forces dominate the uncertainty, and above about 2 n_0 the EOS is extrapolated.", "map": "E(n,\\delta)\\approx E_0(n)+S(n)\\delta^2,\\quad L=3n_0\\,\\partial S/\\partial n|_{n_0}", "breaks": "Chiral EFT breaks down as momenta approach the breakdown scale (~500–600 MeV), so above ~2n_0 it gives no control.", "confidence": "current research", "strength": 3}
{"id": "C2434", "a": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Nuclear pairing and neutron-star superfluidity", "kind": "identity", "summary": "The BCS pairing that causes odd–even mass staggering and reduced rotational moments of inertia in nuclei also makes neutron-star matter superfluid: ¹S₀ neutrons in the inner crust and ³P₂ neutrons in the core. The gaps are of order MeV, and the superfluid controls glitches, the specific heat and neutrino cooling.", "map": "\\Delta_k=-\\sum_{k'}V_{kk'}\\frac{\\Delta_{k'}}{2E_{k'}};\\quad \\Delta_{\\rm nuc}\\approx12/\\sqrt{A}\\,{\\rm MeV}", "breaks": "Finite nuclei are smaller than the coherence length, so pairing there is a mesoscopic, fluctuating condensate. Whether Cas A's cooling shows ³P₂ pairing onset is contested.", "confidence": "established", "strength": 3}
{"id": "C2435", "a": "07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process", "b": "07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions", "name": "Beta-decay half-lives set the r-process clock", "kind": "mechanism", "summary": "β-decay half-lives at the waiting points, often with large first-forbidden contributions, set how fast the flow climbs in Z and shape the abundance peaks. β-delayed neutron emission during freeze-out smooths and shifts the final pattern.", "map": "\\lambda_{\\beta}(Z)\\,Y_Z\\approx\\text{const (steady }\\beta\\text{-flow)};\\quad t_r\\sim\\sum_Z T_{1/2}(Z)/\\ln2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2436", "a": "07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process", "b": "07-nuclear-physics/nuclear-reactions-and-decays/fusion-reactions", "name": "Gamow-peak fusion rates power stellar burning", "kind": "identity", "summary": "Stellar burning rates are Coulomb-barrier tunnelling probabilities folded with a Maxwell–Boltzmann distribution, which gives the Gamow peak. Astrophysical S-factors for the pp chain, CNO cycle, triple-α and ¹²C(α,γ)¹⁶O are measured underground (LUNA) or extrapolated to stellar energies.", "map": "\\langle\\sigma v\\rangle\\propto\\int S(E)\\,e^{-E/kT-\\sqrt{E_G/E}}\\,dE,\\quad E_0=\\left(E_G(kT)^2/4\\right)^{1/3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2437", "a": "07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-fission", "name": "Fission recycling terminates the r-process", "kind": "mechanism", "summary": "In very neutron-rich merger ejecta the r-process reaches A≈250–300, where neutron-induced, β-delayed and spontaneous fission end the flow. The fragments recycle into A≈110–170 and shape the second peak and the rare-earth region. Fission barriers and yields of unmeasured neutron-rich actinides are among the largest nuclear uncertainties.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2438", "a": "07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process", "b": "07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay", "name": "Th/U cosmochronometry of r-process stars", "kind": "method transfer", "summary": "The long-lived r-process actinides ²³²Th (14.0 Gyr) and ²³⁸U (4.47 Gyr) decay through α chains. Their abundances, relative to each other and to stable r-process elements, date old metal-poor stars, and live ²⁴⁴Pu and ⁶⁰Fe in deep-sea crusts time recent nearby nucleosynthesis.", "map": "t=\\frac{\\ln[(\\mathrm{U/Th})_0/(\\mathrm{U/Th})_{\\rm obs}]}{\\lambda_{\\rm U}-\\lambda_{\\rm Th}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2439", "a": "07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process", "b": "07-nuclear-physics/nuclear-structure/ab-initio-nuclear-theory", "name": "Hoyle state: triple-alpha to ab initio", "kind": "shared object", "summary": "In 1953 Hoyle predicted the 7.65 MeV 0⁺ state of ¹²C because carbon could not be made in stars without a resonant triple-α reaction. Its α-cluster structure is a demanding test that nuclear lattice EFT has reproduced, and its energy and radiative width set the stellar carbon/oxygen yield.", "map": "E_{\\rm Hoyle}-3m_\\alpha c^2\\approx0.38\\,{\\rm MeV};\\quad r_{3\\alpha}\\propto\\Gamma_{\\rm rad}\\,T^{-3}e^{-Q/kT}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2440", "a": "07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process", "b": "07-nuclear-physics/nuclear-structure/exotic-nuclei-and-drip-lines", "name": "Drip-line nuclei set the r-process path", "kind": "shared object", "summary": "The r-process runs through very neutron-rich nuclei near the neutron drip line. Their masses (neutron separation energies), shell evolution and half-lives, measured at FRIB, RIBF and FAIR, therefore fix the path and the abundance pattern. In (n,γ)⇄(γ,n) equilibrium, the waiting-point nuclei sit at S_n ≈ 2–3 MeV.", "map": "Y(Z,A{+}1)/Y(Z,A)\\propto n_n\\,T^{-3/2}e^{S_n/kT};\\ S_n=B(A,Z)-B(A-1,Z)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2441", "a": "07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Magic neutron numbers make the r-process peaks", "kind": "mechanism", "summary": "At the closed shells N=50, 82 and 126, neutron separation energies drop just past the closure and β half-lives at the waiting points are long. Matter therefore piles up at A≈80, 130 and 195, the r-process peaks, about 10 mass units below the s-process peaks at the same N. Whether the N=82 and N=126 gaps are quenched far from stability is still debated.", "map": "N_{\\rm magic}=50,82,126\\ \\Rightarrow\\ A^{r}_{\\rm peak}\\approx80,130,195", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2442", "a": "07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions", "b": "07-nuclear-physics/nuclear-structure/ab-initio-nuclear-theory", "name": "Gamow–Teller quenching from two-body currents", "kind": "mechanism", "summary": "Shell-model Gamow–Teller rates have long needed g_A quenched to about 0.75 of its free value. Ab initio calculations with chiral two-body weak currents and many-body correlations reproduce the measured rates without ad hoc quenching. The same framework supplies the nuclear matrix elements for neutrinoless double-beta decay.", "map": "T_{1/2}^{-1}\\propto g_A^2\\,|\\langle f\\|\\sigma\\tau^\\pm\\|i\\rangle|^2;\\ g_A^{\\rm eff}\\approx0.75\\,g_A\\ \\text{(phenomenological)}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2443", "a": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-fission", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Liquid drop plus shell correction: fission barriers", "kind": "mechanism", "summary": "The fission barrier is the deformation energy of a liquid drop (surface against Coulomb) plus a Strutinsky shell correction from single-particle levels in the deformed well. Together they give double-humped barriers, fission isomers, and asymmetric mass splits driven by fragments near doubly magic ¹³²Sn.", "map": "E(\\beta)=E_{\\rm LD}(\\beta)+\\delta E_{\\rm shell}(\\beta)+\\delta E_{\\rm pair}(\\beta)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2444", "a": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-fission", "b": "07-nuclear-physics/nuclear-structure/superheavy-elements", "name": "Fission barriers bound the superheavy landscape", "kind": "mechanism", "summary": "The liquid-drop fissility rises with Z²/A, and the macroscopic fission barrier vanishes near Z≈100. Superheavy nuclei survive only because shell-correction barriers of a few MeV hold them together, and spontaneous fission competes with α decay as the terminating decay mode.", "map": "x=\\frac{E_C}{2E_S}\\approx\\frac{Z^2/A}{(Z^2/A)_{\\rm crit}},\\ (Z^2/A)_{\\rm crit}\\approx50;\\ B_f\\approx B_f^{\\rm LD}(x)+\\delta E_{\\rm shell}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2445", "a": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "b": "07-nuclear-physics/nuclear-structure/exotic-nuclei-and-drip-lines", "name": "Inverse-kinematics reactions reveal halos and shells", "kind": "method transfer", "summary": "Short-lived nuclei are studied as radioactive beams on light targets. Interaction cross sections revealed the ¹¹Li halo, knockout momentum distributions give the orbital ℓ and spectroscopic factors, and transfer and Coulomb breakup map shell evolution near the drip lines.", "map": "\\sigma_I\\approx\\pi(R_P+R_T)^2;\\quad \\Delta p\\sim\\hbar/\\Delta r", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2446", "a": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "b": "07-nuclear-physics/nuclear-structure/nuclear-forces-and-chiral-eft", "name": "NN phase shifts and the effective-range expansion", "kind": "identity", "summary": "Chiral NN potentials are fitted to partial-wave NN scattering phase shifts. The unnaturally large ¹S₀ scattering length (a_np ≈ −23.7 fm) shapes the EFT power counting and gives few-nucleon systems the same low-energy universality seen in cold atoms.", "map": "k\\cot\\delta_0=-\\frac1a+\\frac12r_0k^2+\\dots;\\quad a_{np}(^1S_0)\\approx-23.7\\,{\\rm fm}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2447", "a": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "b": "07-nuclear-physics/nuclear-structure/superheavy-elements", "name": "Fusion–evaporation reactions make superheavy elements", "kind": "method transfer", "summary": "Superheavy elements are made by cold fusion (Pb/Bi targets) or hot fusion (⁴⁸Ca beams on actinide targets). Cross sections of picobarns to femtobarns are the product of capture over the Coulomb barrier, competition from quasifission, and survival against fission while neutrons evaporate from the compound nucleus. Going beyond Z=118 requires ⁵⁰Ti or ⁵⁴Cr beams.", "map": "\\sigma_{\\rm ER}=\\sigma_{\\rm cap}\\,P_{\\rm CN}\\,W_{\\rm sur}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2448", "a": "07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay", "b": "07-nuclear-physics/nuclear-structure/superheavy-elements", "name": "Alpha-decay chains identify superheavy elements", "kind": "method transfer", "summary": "New superheavy elements are identified by correlated α-decay chains that end at known nuclides. Geiger–Nuttall (Gamow tunnelling) systematics turn measured Q_α into half-lives, and kinks in Q_α along the chains reveal shell gaps on the way to the island of stability.", "map": "\\log_{10}T_{1/2}=a\\,\\frac{Z}{\\sqrt{Q_\\alpha}}+b", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2449", "a": "07-nuclear-physics/applied-nuclear-physics/nuclear-reactors-and-energy", "b": "08-condensed-matter/crystals-and-electronic-structure", "name": "Radiation damage in reactor materials", "kind": "mechanism", "summary": "Fast neutrons create displacement cascades in fuel cladding, steels and graphite; point-defect production, swelling, embrittlement and stored Wigner energy are solid-state physics that limits reactor lifetimes and fusion first walls.", "map": "N_d=\\frac{E_{\\rm dam}}{2E_d}\\ \\text{(Kinchin-Pease)};\\ \\text{dpa}=\\sigma_d\\phi t", "breaks": "Displacement counts overestimate surviving defects because of in-cascade recombination, so molecular dynamics is needed.", "confidence": "established", "strength": 2}
{"id": "C2450", "a": "07-nuclear-physics/applied-nuclear-physics/nuclear-reactors-and-energy", "b": "08-condensed-matter/crystals-and-electronic-structure/semiconductors", "name": "Neutron transmutation doping of silicon", "kind": "method transfer", "summary": "Irradiating float-zone silicon in a reactor turns 30Si into 31P by neutron capture and beta decay, giving the most uniform n-type doping available, used for high-power devices and thyristors.", "map": "{}^{30}\\mathrm{Si}(n,\\gamma){}^{31}\\mathrm{Si}\\xrightarrow{\\beta^-,\\,2.6\\,\\mathrm h}{}^{31}\\mathrm P;\\ N_P=N_{30}\\sigma_{\\rm th}\\phi t", "breaks": "Only n-type doping is possible, and the lattice damage has to be annealed.", "confidence": "established", "strength": 2}
{"id": "C2451", "a": "07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry", "b": "08-condensed-matter/crystals-and-electronic-structure/semiconductors", "name": "Semiconductor and scintillator radiation detectors", "kind": "method transfer", "summary": "HPGe and Si detectors are reverse-biased p-n junctions whose energy resolution is set by electron-hole pair statistics (about 3 eV per pair, Fano factor ~0.1); scintillators and halide-perovskite detectors depend on excitons, traps and band gaps.", "map": "w\\approx2.8E_g+0.6\\ \\text{eV};\\ \\frac{\\sigma_E}{E}=2.355\\sqrt{\\frac{Fw}{E}};\\ W_{\\rm dep}=\\sqrt{\\frac{2\\epsilon V}{eN_d}}", "breaks": "Detector-grade operation needs ultrapure crystals with long carrier lifetimes and radiation hardness, priorities different from electronic devices.", "confidence": "established", "strength": 3}
{"id": "C2452", "a": "07-nuclear-physics/heavy-ion-physics/collective-flow-and-hydrodynamics", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "name": "Relativistic viscous hydro in the graphene Dirac fluid", "kind": "identity", "summary": "Near charge neutrality graphene electrons form a Dirac fluid described by the same relativistic viscous hydrodynamics as the QGP, with c replaced by v_F; it was predicted and then measured to be a nearly perfect fluid with low eta/s that violates Wiedemann-Franz.", "map": "\\partial_\\mu T^{\\mu\\nu}=F^{\\nu\\lambda}J_\\lambda,\\ T^{\\mu\\nu}=(\\varepsilon+P)u^\\mu u^\\nu+Pg^{\\mu\\nu}+\\pi^{\\mu\\nu},\\ c\\to v_F\\approx c/300", "breaks": "The graphene fluid is 2D, charged with long-range Coulomb forces, and loses momentum to impurities and phonons; the QGP is an expanding, short-lived drop with no lattice.", "confidence": "current research", "strength": 3}
{"id": "C2453", "a": "07-nuclear-physics/heavy-ion-physics/qcd-phase-diagram-and-critical-point", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Colour superconductivity in dense quark matter", "kind": "mechanism", "summary": "At high baryon density the attractive colour-antitriplet channel makes the quark Fermi surface unstable to BCS pairing; the colour-flavour-locked phase is a colour superconductor in which gluons acquire Meissner masses and chiral symmetry breaks, a candidate for neutron-star cores.", "map": "\\langle q^a_{\\alpha}q^b_{\\beta}\\rangle\\propto\\Delta\\,\\epsilon^{abI}\\epsilon_{\\alpha\\beta I};\\ \\Delta\\sim\\mu g^{-5}e^{-3\\pi^2/\\sqrt2g}\\ \\text{(weak coupling)}", "breaks": "The condensate breaks a non-abelian gauge symmetry and is under control only at asymptotic density; at neutron-star densities it is model-dependent and has no direct experimental confirmation.", "confidence": "established", "strength": 3}
{"id": "C2454", "a": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "b": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "name": "Viscous electron flow and eta/s in metals vs QGP", "kind": "analogy", "summary": "In ultraclean conductors electron-electron collisions dominate and charge flows hydrodynamically (Gurzhi effect, negative nonlocal resistance), giving measured electron viscosities that can be set against QGP eta/s in the same Navier-Stokes framework.", "map": "\\nu=\\eta/\\rho\\approx\\tfrac14v_F\\ell_{ee};\\ \\text{hydro window }\\ell_{ee}\\ll W\\ll\\ell_{\\rm mr}", "breaks": "Fermi-liquid electrons are weakly coupled with a long l_ee, so their eta/s is far above the QGP value; momentum relaxation at boundaries and impurities has no QGP counterpart.", "confidence": "current research", "strength": 2}
{"id": "C2455", "a": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "b": "08-condensed-matter/magnetism/spintronics", "name": "Spin-vorticity: Lambda polarization and Barnett effect", "kind": "mechanism", "summary": "Global Lambda polarization in off-central collisions shows the QGP is the most vortical fluid known; it aligns spins through the same spin-rotation coupling as the Barnett effect and spin hydrodynamic generation in liquid metals.", "map": "H=-\\boldsymbol\\omega\\cdot\\mathbf S;\\ P_\\Lambda\\approx\\frac{\\hbar\\omega}{2k_BT},\\ \\omega\\sim10^{22}\\ \\text{s}^{-1}", "breaks": "QGP polarization is read from the hadronized final state of a ~10 fm/c fluid in local equilibrium; the spintronic versions involve electron spin, spin-orbit coupling and dissipative spin currents.", "confidence": "current research", "strength": 2}