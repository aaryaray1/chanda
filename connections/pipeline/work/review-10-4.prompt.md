You are the plasma-physicist, the specialist for 10 (Plasma Physics) in this physics knowledge base.

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

## Field overview · `knowledge/10-plasma-physics`

> **Specialist:** `plasma-physicist` · **arXiv:** physics.plasm-ph, physics.space-ph, astro-ph.SR/HE · **Literature source:** OpenAlex + arXiv

#### What this field studies
More than 99% of visible matter is plasma: stars, the solar wind, interstellar gas, lightning, neon signs and fusion reactors. A plasma is an ionized gas in which long-range electromagnetic forces make particles act collectively — shielding charges, supporting a zoo of waves, and becoming unstable in countless ways. Plasma physics spans kinetic theory and fluid (MHD) descriptions, and its grand applied challenge is controlled thermonuclear fusion.

#### Conventions used in this branch
- Temperatures in eV ($1\ \text{eV}\approx11\,600$ K); densities in m⁻³ (fusion) or cm⁻³ (space/astro).
- SI and Gaussian units both common (Chen and Goldston–Rutherford use SI; many astro texts Gaussian) — convert explicitly.
- Subscripts $e$, $i$ for electrons and ions; $\omega_p$ plasma frequency, $\Omega_c$ cyclotron frequency, $\rho$ Larmor radius, $\beta=2\mu_0p/B^2$.

#### Historical spine
1879 "fourth state of matter" (Crookes) · 1923 Debye shielding · 1928 Langmuir names "plasma" · 1942 Alfvén waves · 1946 Landau damping · 1951 stellarator · 1957 Lawson criterion · 1958 solar wind (Parker), Van Allen belts · 1968 T-3 tokamak results · 1979 laser wakefield proposal · 1982 H-mode · 1991 first D–T fusion (JET) · 1997 JET 16 MW · 2004 monoenergetic laser-accelerated electrons · 2016 W7-X operation · 2021 burning plasma at NIF · 2022 NIF ignition (target gain > 1) · 2024 JET final record (69 MJ).

#### Canonical textbooks
- Chen, *Introduction to Plasma Physics and Controlled Fusion* — undergraduate standard.
- Bellan, *Fundamentals of Plasma Physics*; Goldston & Rutherford, *Introduction to Plasma Physics*.
- Freidberg, *Plasma Physics and Fusion Energy*; Wesson, *Tokamaks*.
- Kulsrud, *Plasma Physics for Astrophysics*; Atzeni & Meyer-ter-Vehn, *The Physics of Inertial Fusion*; Lieberman & Lichtenberg, *Principles of Plasma Discharges and Materials Processing*.

#### Live frontiers
- ITER construction and private fusion (high-field HTS tokamaks, stellarators, alternative concepts).
- Repeatable high-gain ignition at NIF and the path to inertial fusion energy.
- Plasma wakefield accelerators for compact colliders and light sources.
- Parker Solar Probe and the heating of the solar corona.

#### How the specialist works here
Compute the dimensionless parameters first ($\ln\Lambda$, $\beta$, $\rho/L$, collisionality, $\omega/\Omega_c$) to decide whether single-particle, kinetic or fluid descriptions apply; check quasi-neutrality and frequency ordering; identify free-energy sources for instabilities; and quote fusion performance with the triple product and $Q$.

## Inertial and laser plasmas · `knowledge/10-plasma-physics/inertial-and-laser-plasmas`

#### Overview
Intense lasers create plasmas at pressures of gigabars and temperatures of keV in nanoseconds. Inertial confinement fusion compresses a fuel capsule so fast that it burns before it flies apart — NIF achieved target gain above 1 in December 2022. At even higher intensities ($>10^{18}$ W/cm²), electrons become relativistic, enabling plasma wakefields with accelerating gradients 1000× those of RF cavities.

#### Key equations
$$a_0=\frac{eE_0}{m_e\omega c}\approx0.85\left(\frac{I\lambda^2}{10^{18}\,\text{W cm}^{-2}\mu\text{m}^2}\right)^{1/2},\qquad E_{\text{wb}}\approx96\sqrt{n_e[\text{cm}^{-3}]}\ \text{V/m}$$

#### Open problems
- High repetition-rate, high-gain targets for inertial fusion energy.
- Beam quality and staging for TeV-class plasma accelerators.

#### Connections
- [Ultrafast optics (CPA)](knowledge/02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics/README.md) · [Future colliders](knowledge/06-particle-physics/collider-and-experimental-particle-physics/future-colliders/README.md) · [Rayleigh–Taylor instability](knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection/README.md)

### High-energy-density physics · `knowledge/10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics`

**Scope.** Warm dense matter (solid density, few-eV temperatures, partially degenerate and strongly coupled), shock and ramp compression, equation-of-state measurements, metallization of hydrogen and planetary interiors (Jupiter, exoplanets), diamond rain, X-ray FEL heating and diagnostics, X-ray Thomson scattering, opacity measurements for stellar interiors, laboratory astrophysics (collisionless shocks, jets).

**Core ideas.**
- Warm dense matter has no small parameter: neither plasma nor condensed-matter approximations work cleanly.
- Ab initio MD with DFT is the workhorse theory; experiments test it.
- Opacity measurements at Z-machine conditions challenged solar models (iron opacity puzzle).

**Key equations.**
$$P\gtrsim1\ \text{Mbar}=10^{11}\ \text{Pa},\qquad \theta=\frac{k_BT}{E_F}\sim1,\quad \Gamma\sim1$$

**Landmark.** Glenzer & Redmer (2009) — see [subfield landmarks](knowledge/10-plasma-physics/inertial-and-laser-plasmas/README.md).

**See also.** [Dusty and strongly coupled plasmas](knowledge/10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas/README.md) · [Density functional theory](knowledge/08-condensed-matter/crystals-and-electronic-structure/density-functional-theory/README.md)

### Inertial confinement fusion · `knowledge/10-plasma-physics/inertial-and-laser-plasmas/inertial-confinement-fusion`

**Scope.** Ablation-driven implosion, indirect drive (hohlraum X-rays) vs. direct drive (OMEGA), convergence ratios ~30–40, hot-spot ignition criterion ($\rho R\gtrsim0.3$ g/cm², $T\gtrsim5$ keV), Rayleigh–Taylor and mix, laser–plasma instabilities in hohlraums, shock ignition and fast ignition, NIF milestones (burning plasma 2021, gain 1.5 in 2022, >4 later), inertial fusion energy.

**Core ideas.**
- Inertia confines: burn must finish in ~100 ps before disassembly.
- Imploding shells are Rayleigh–Taylor unstable; symmetry and smoothness are paramount.
- "Gain >1" refers to fusion yield over laser energy on target, not wall-plug efficiency.

**Key equations.**
$$\tau_{\text{conf}}\sim\frac{R}{4c_s},\qquad \text{burn fraction}\approx\frac{\rho R}{\rho R+6\ \text{g cm}^{-2}}$$

**See also.** [Instabilities and convection](knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection/README.md) · [Burning plasmas](knowledge/10-plasma-physics/magnetic-confinement-fusion/burning-plasmas-and-iter/README.md)

### Laser–plasma interactions · `knowledge/10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions`

**Scope.** Inverse bremsstrahlung, resonance absorption, $\mathbf J\times\mathbf B$ heating, critical density, stimulated Raman and Brillouin scattering, two-plasmon decay, filamentation, relativistic transparency and self-focusing, target-normal sheath acceleration of ions, radiation-pressure acceleration, high-harmonic generation from surfaces, QED-plasma regime and radiation reaction at multi-PW lasers.

**Core ideas.**
- Light penetrates only up to the critical density $n_c=\epsilon_0m_e\omega^2/e^2$ (~$10^{21}$ cm⁻³ at 1 μm).
- For $a_0>1$, electrons oscillate relativistically, changing the plasma's optical properties.
- Parametric instabilities scatter laser energy and generate hot electrons — a key ICF challenge.

**Key equations.**
$$n_c\approx\frac{1.1\times10^{21}}{\lambda[\mu\text{m}]^2}\ \text{cm}^{-3},\qquad T_{\text{hot}}\approx m_ec^2\left(\sqrt{1+a_0^2/2}-1\right)$$

**Landmark.** Wilks et al. (1992) — see [subfield landmarks](knowledge/10-plasma-physics/inertial-and-laser-plasmas/README.md).

**See also.** [Nonlinear optics](knowledge/02-electromagnetism-and-optics/photonics-and-lasers/nonlinear-optics/README.md) · [Radiation from moving charges](knowledge/02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges/README.md)

### Plasma wakefield acceleration · `knowledge/10-plasma-physics/inertial-and-laser-plasmas/plasma-wakefield-acceleration`

**Scope.** Tajima–Dawson concept, laser wakefield (LWFA) and beam-driven (PWFA) schemes, blowout/bubble regime, self-injection and controlled injection, dephasing and depletion lengths, 8 GeV in 20 cm (BELLA), FACET results, AWAKE proton-driven wakes, positron acceleration challenges, staging, compact FELs and radiation sources.

**Core ideas.**
- A plasma wave can sustain fields up to the wave-breaking limit ~100 GV/m at $10^{18}$ cm⁻³.
- Electrons surfing the wake gain energy over cm instead of km.
- Energy spread, emittance and efficiency — not peak energy — limit collider applications.

**Key equations.**
$$\lambda_p=\frac{2\pi c}{\omega_p}\approx33\ \mu\text{m}\left(\frac{10^{18}}{n_e[\text{cm}^{-3}]}\right)^{1/2},\qquad L_d\approx\frac{\lambda_p^3}{\lambda^2}$$

**See also.** [Future colliders](knowledge/06-particle-physics/collider-and-experimental-particle-physics/future-colliders/README.md) · [Accelerator physics](knowledge/11-interdisciplinary-physics/accelerator-physics/README.md)

## Low-temperature and applied plasmas · `knowledge/10-plasma-physics/low-temperature-and-applied-plasmas`

#### Overview
In low-temperature plasmas electrons are hot (1–10 eV) while ions and neutrals stay near room temperature. This non-equilibrium makes them chemically powerful but gentle: they etch nanometre features in every computer chip, deposit coatings, light lamps, sterilize surfaces, and are being explored for wound healing, cancer treatment and nitrogen fixation.

#### Key equations
$$V_b=\frac{Bpd}{\ln(Apd)-\ln\ln(1+1/\gamma_{se})},\qquad T_e\gg T_i\approx T_{\text{gas}}$$

#### Connections
- [Semiconductor devices](knowledge/11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics/README.md) · [Surface science](knowledge/11-interdisciplinary-physics/chemical-physics/surface-science-and-catalysis/README.md)

### Atmospheric-pressure plasmas and applications · `knowledge/10-plasma-physics/low-temperature-and-applied-plasmas/atmospheric-pressure-plasmas-and-applications`

**Scope.** Dielectric-barrier discharges and ozone generation, atmospheric-pressure plasma jets and guided ionization waves, reactive oxygen and nitrogen species (RONS), plasma-activated water, wound healing and cancer studies, sterilization, seed treatment and nitrogen fixation, CO₂ conversion, VOC abatement, plasma-assisted combustion.

**Core ideas.**
- Short pulses and barriers prevent arcing, keeping the gas cold while electrons are hot.
- Biological effects come mainly from RONS chemistry, electric fields and UV.
- Electrified chemistry (plasma catalysis) could replace fossil-heat-driven processes — energy efficiency is the open question.

**Key equations.**
$$e+\text{O}_2\to e+2\text{O},\quad \text{O}+\text{O}_2+M\to\text{O}_3+M$$

**See also.** [Reaction dynamics](knowledge/11-interdisciplinary-physics/chemical-physics/reaction-dynamics/README.md) · [Physics of living systems](knowledge/11-interdisciplinary-physics/biophysics/physics-of-living-systems/README.md)

### Plasma discharges and processing · `knowledge/10-plasma-physics/low-temperature-and-applied-plasmas/plasma-discharges-and-processing`

**Scope.** Townsend avalanche and Paschen curves, glow and arc discharges, sheath physics and ion energy distributions, CCP and ICP reactors, electron energy distributions (non-Maxwellian), plasma chemistry, reactive-ion etching and anisotropy, atomic-layer etching and deposition, PECVD, EUV-lithography source plasmas (tin droplets).

**Core ideas.**
- Breakdown voltage depends on pressure × gap (Paschen): there's a minimum, not a monotonic curve.
- Sheaths accelerate ions perpendicular to the wafer, enabling anisotropic nanoscale etching.
- Electron-impact reactions create radicals at low gas temperature — chemistry without heat.

**Key equations.**
$$\Gamma_i=n_su_B,\ u_B=\sqrt{\frac{k_BT_e}{m_i}}\ (\text{Bohm flux}),\qquad s\approx\lambda_D\left(\frac{2eV_0}{k_BT_e}\right)^{3/4}\ (\text{Child law sheath})$$

**See also.** [Debye shielding and sheaths](knowledge/10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters/README.md)

## Magnetic confinement fusion · `knowledge/10-plasma-physics/magnetic-confinement-fusion`

#### Overview
Magnetic fusion confines a D–T plasma at ~15 keV in toroidal magnetic fields long enough for fusion power to exceed losses. Tokamaks (axisymmetric, plasma current) are the most advanced; stellarators (3D-shaped coils, no current) avoid disruptions. Turbulent transport sets confinement; the H-mode doubles it. ITER (Cadarache) aims for $Q=10$; compact high-field HTS tokamaks and optimized stellarators are pursued by public and private programmes.

#### Key equations
$$nT\tau_E>3\times10^{21}\ \text{keV s m}^{-3}\ (\text{D–T ignition}),\qquad Q=\frac{P_{\text{fus}}}{P_{\text{heat}}},\qquad \beta=\frac{2\mu_0\langle p\rangle}{B^2}$$

#### Open problems
- Avoiding or mitigating disruptions in reactor-scale tokamaks.
- Plasma-facing materials and neutron damage; tritium self-sufficiency.

#### Connections
- [Fusion reactions](knowledge/07-nuclear-physics/nuclear-reactions-and-decays/fusion-reactions/README.md) · [Single-particle motion](knowledge/10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts/README.md)

### Burning plasmas and ITER · `knowledge/10-plasma-physics/magnetic-confinement-fusion/burning-plasmas-and-iter`

**Scope.** Ignition and $Q$ definitions (scientific vs. engineering), alpha heating and alpha-driven Alfvén eigenmodes, ITER design (6.2 m major radius, 5.3 T, 15 MA, $Q=10$ target) and revised schedule, JET D–T records (59 MJ 2021, 69 MJ 2024), divertor heat loads (~10 MW/m²), tungsten walls, neutron damage (dpa), lithium breeding blankets, DEMO, high-field HTS compact tokamaks.

**Core ideas.**
- A burning plasma has alpha heating dominating external heating ($Q\gtrsim5$); ignition is $Q\to\infty$.
- 80% of D–T energy leaves as 14 MeV neutrons, which damage materials and breed tritium from lithium.
- Exhaust and materials, not just confinement, are now the critical path to a power plant.

**Key equations.**
$$P_\alpha=\tfrac14n^2\langle\sigma v\rangle E_\alpha V,\qquad \text{Li-6}+n\to\text{T}+{}^4\text{He}+4.8\ \text{MeV}$$

**Landmark.** ITER Physics Basis (1999) — see [subfield landmarks](knowledge/10-plasma-physics/magnetic-confinement-fusion/README.md).

**See also.** [Nuclear reactors](knowledge/07-nuclear-physics/applied-nuclear-physics/nuclear-reactors-and-energy/README.md) · [Inertial confinement fusion](knowledge/10-plasma-physics/inertial-and-laser-plasmas/inertial-confinement-fusion/README.md)

### Stellarators · `knowledge/10-plasma-physics/magnetic-confinement-fusion/stellarators`

**Scope.** Rotational transform from external coils, steady-state operation without disruptions, neoclassical transport and the $1/\nu$ regime, quasi-axisymmetry, quasi-helical and quasi-isodynamic designs, coil-complexity trade-offs, W7-X results, LHD, HSX, precise quasi-symmetry optimization (2022), private stellarator ventures.

**Core ideas.**
- External 3D coils twist field lines — no plasma current, hence no current-driven disruptions.
- Generic 3D fields lose trapped particles quickly; optimization restores near-symmetry in $|B|$.
- Computational optimization made stellarators competitive again.

**Key equations.**
$$\iota=\frac{1}{q}=\frac{d\psi_p}{d\psi_t},\qquad \text{quasi-symmetry: }|B|=B(\psi,M\theta-N\phi)$$

**See also.** [Tokamaks](knowledge/10-plasma-physics/magnetic-confinement-fusion/tokamaks/README.md) · [KAM theory (magnetic islands)](knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos/README.md)

### Tokamaks · `knowledge/10-plasma-physics/magnetic-confinement-fusion/tokamaks`

**Scope.** Toroidal and poloidal fields, safety factor $q$, Grad–Shafranov equilibrium, divertors, ohmic, neutral-beam and RF heating, L–H transition and edge transport barrier, ELMs and their control, sawteeth and NTMs, disruptions and runaway electrons, Greenwald density limit, scaling laws (IPB98), JET, JT-60SA, KSTAR, EAST, SPARC.

**Core ideas.**
- The plasma current produces the poloidal field that twists field lines to cancel drift-induced charge separation.
- Confinement time scales roughly as $\tau_E\propto I_pR^{2}P^{-0.7}$ (IPB98) — bigger, higher-current devices confine better.
- Stability limits on $q$, $\beta$ and density bound the operating space.

**Key equations.**
$$q(r)=\frac{rB_\phi}{RB_\theta},\qquad n_G=\frac{I_p}{\pi a^2}\ [10^{20}\,\text{m}^{-3},\ \text{MA},\ \text{m}],\qquad \beta_N=\frac{\beta\,aB_0}{I_p}$$

**Landmark.** Wagner et al. (1982) — see [subfield landmarks](knowledge/10-plasma-physics/magnetic-confinement-fusion/README.md).

**See also.** [Ideal MHD](knowledge/10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves/README.md) · [Fusion reactions](knowledge/07-nuclear-physics/nuclear-reactions-and-decays/fusion-reactions/README.md)

### Turbulent transport and gyrokinetics · `knowledge/10-plasma-physics/magnetic-confinement-fusion/turbulent-transport-and-gyrokinetics`

**Scope.** Classical and neoclassical transport, anomalous transport from microturbulence, drift waves, ITG, TEM and ETG modes, critical gradients and stiffness, zonal flows and the Dimits shift, $\mathbf E\times\mathbf B$ shear suppression and transport barriers, gyrokinetic ordering and equations, codes (GENE, GYRO/CGYRO, GS2, XGC), reduced models (TGLF).

**Core ideas.**
- Gradients drive small-scale instabilities with $k_\perp\rho_i\sim1$; resulting turbulence dominates heat loss.
- Zonal flows self-regulate turbulence; sheared flows suppress it, creating barriers (H-mode pedestal).
- Gyrokinetics averages fast gyromotion, reducing 6D kinetics to 5D.

**Key equations.**
$$\chi_{\text{gB}}\sim\frac{\rho_i^2v_{ti}}{L},\qquad \frac{\omega}{\Omega_i}\sim\frac{\rho_i}{L}\sim\frac{\delta f}{f}\ll1\ (\text{gyrokinetic ordering})$$

**See also.** [Vlasov and Landau damping](knowledge/10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping/README.md) · [Turbulence](knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/turbulence/README.md)

## Magnetohydrodynamics · `knowledge/10-plasma-physics/magnetohydrodynamics`

#### Overview
On scales much larger than ion gyroradii and slower than ion cyclotron frequencies, a plasma behaves as a single conducting fluid coupled to the magnetic field. In ideal MHD, field lines are "frozen" into the flow; magnetic tension and pressure produce Alfvén and magnetosonic waves. Non-ideal effects allow reconnection, which releases magnetic energy explosively in solar flares and tokamak disruptions, and dynamos, which generate the fields of planets, stars and galaxies.

#### Key equations
$$\frac{\partial\mathbf B}{\partial t}=\nabla\times(\mathbf v\times\mathbf B)+\eta\nabla^2\mathbf B,\qquad \rho\frac{D\mathbf v}{Dt}=-\nabla p+\frac{(\nabla\times\mathbf B)\times\mathbf B}{\mu_0},\qquad v_A=\frac{B}{\sqrt{\mu_0\rho}}$$

#### Open problems
- Why is reconnection fast (~0.01–0.1 $v_A$) regardless of resistivity?
- Coronal heating: waves, nanoflares, or both?

#### Connections
- [Fluid mechanics](knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/README.md) · [The Sun](knowledge/09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology/README.md) · [Planet formation (MRI)](knowledge/09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks/README.md)

### Dynamo theory · `knowledge/10-plasma-physics/magnetohydrodynamics/dynamo-theory`

**Scope.** Cowling's anti-dynamo theorem, kinematic dynamos, magnetic Reynolds number threshold, mean-field electrodynamics and the α–Ω mechanism, solar cycle (22-year magnetic cycle, butterfly diagram), geodynamo and field reversals, small-scale fluctuation dynamos, galactic dynamos, laboratory sodium experiments (Riga, Karlsruhe, VKS).

**Core ideas.**
- Differential rotation (Ω-effect) stretches poloidal field into toroidal; helical turbulence (α-effect) regenerates poloidal field.
- Dynamos need $R_m=UL/\eta$ above a threshold and must avoid symmetry (Cowling).
- Earth's field reverses irregularly every ~0.1–1 Myr; simulations reproduce reversals.

**Key equations.**
$$\frac{\partial\bar{\mathbf B}}{\partial t}=\nabla\times(\bar{\mathbf v}\times\bar{\mathbf B}+\alpha\bar{\mathbf B})+(\eta+\beta)\nabla^2\bar{\mathbf B},\qquad R_m=\frac{UL}{\eta}$$

**Landmark.** Parker (1955) — see [subfield landmarks](knowledge/10-plasma-physics/magnetohydrodynamics/README.md).

**See also.** [Seismology and Earth's interior](knowledge/11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior/README.md) · [The Sun](knowledge/09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology/README.md)

### Ideal MHD and Alfvén waves · `knowledge/10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves`

**Scope.** Derivation from two-fluid equations, ideal Ohm's law, Alfvén's frozen-flux theorem, magnetic pressure and tension, shear Alfvén and fast/slow magnetosonic waves, force-free fields, Grad–Shafranov equilibrium, energy principle, kink, sausage, interchange and ballooning instabilities, Kruskal–Shafranov limit.

**Core ideas.**
- Perfectly conducting fluids carry field lines with them; topology is conserved.
- Magnetic force = pressure gradient $-\nabla(B^2/2\mu_0)$ + tension $(\mathbf B\cdot\nabla)\mathbf B/\mu_0$.
- Plucked field lines oscillate as strings with tension $B^2/\mu_0$ — Alfvén waves.

**Key equations.**
$$\nabla p=\mathbf J\times\mathbf B,\qquad \omega=k_\parallel v_A,\qquad q(a)=\frac{aB_\phi}{RB_\theta}>1\ (\text{Kruskal–Shafranov})$$

**Landmark.** Alfvén (1942) — see [subfield landmarks](knowledge/10-plasma-physics/magnetohydrodynamics/README.md).

**See also.** [Tokamaks](knowledge/10-plasma-physics/magnetic-confinement-fusion/tokamaks/README.md) · [Ideal and viscous flow](knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow/README.md)

### Magnetic reconnection · `knowledge/10-plasma-physics/magnetohydrodynamics/magnetic-reconnection`

**Scope.** Current sheets and X-points, Sweet–Parker rate $\propto S^{-1/2}$, Petschek's slow shocks, Hall reconnection and the ion/electron diffusion regions, plasmoid-mediated fast reconnection, guide fields, particle acceleration, solar flares and CMEs, magnetospheric substorms, sawtooth crashes in tokamaks, laboratory experiments (MRX), NASA's MMS mission.

**Core ideas.**
- Resistivity alone gives rates far too slow for flares ($S\sim10^{12}$); collisionless (Hall) physics or plasmoids make reconnection fast.
- Rates of ~0.1 $v_A$ appear universally in simulations and observations.
- Reconnection converts magnetic energy into heat, flows and non-thermal particles.

**Key equations.**
$$\frac{v_{\text{in}}}{v_A}\sim S^{-1/2},\ S=\frac{\mu_0Lv_A}{\eta};\qquad \frac{v_{\text{in}}}{v_A}\sim0.1\ (\text{fast, collisionless})$$

**See also.** [Magnetospheres and space weather](knowledge/10-plasma-physics/space-and-astrophysical-plasmas/magnetospheres-and-space-weather/README.md)

### MHD turbulence · `knowledge/10-plasma-physics/magnetohydrodynamics/mhd-turbulence`

**Scope.** Elsässer variables, Iroshnikov–Kraichnan $k^{-3/2}$ spectrum, Goldreich–Sridhar critical balance and $k_\perp^{-5/3}$, dynamic alignment, imbalanced turbulence, kinetic Alfvén waves and dissipation range, intermittency, turbulent heating of the solar wind, interstellar scintillation, cosmic-ray transport.

**Core ideas.**
- Only counter-propagating Alfvén wave packets interact, so turbulence is inherently anisotropic: eddies elongate along the field.
- Critical balance: linear (Alfvén) and nonlinear times are comparable at every scale.
- At ion scales the cascade transitions to kinetic physics where dissipation heats ions and electrons unequally.

**Key equations.**
$$\mathbf z^\pm=\mathbf v\pm\frac{\mathbf B}{\sqrt{\mu_0\rho}},\qquad E(k_\perp)\propto k_\perp^{-5/3},\quad k_\parallel\propto k_\perp^{2/3}$$

**Landmark.** Goldreich & Sridhar (1995) — see [subfield landmarks](knowledge/10-plasma-physics/magnetohydrodynamics/README.md).

**See also.** [Turbulence](knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/turbulence/README.md) · [Solar wind](knowledge/10-plasma-physics/space-and-astrophysical-plasmas/solar-wind-and-heliosphere/README.md)

## Plasma fundamentals · `knowledge/10-plasma-physics/plasma-fundamentals`

#### Overview
A plasma must be large compared with the Debye length, contain many particles per Debye sphere, and oscillate faster than it collides. Within those conditions, three levels of description apply: individual particles gyrating and drifting in fields, kinetic distributions obeying the Vlasov equation, and fluids. Collective waves and instabilities are the hallmark of plasma behaviour.

#### Key equations
$$\lambda_D=\sqrt{\frac{\epsilon_0k_BT_e}{n_ee^2}},\qquad \omega_{pe}=\sqrt{\frac{n_ee^2}{\epsilon_0m_e}},\qquad \Lambda=4\pi n\lambda_D^3\gg1,\qquad \Omega_c=\frac{qB}{m}$$

#### Connections
- [Kinetic theory (Boltzmann)](knowledge/03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation/README.md) · [Electrodynamics](knowledge/02-electromagnetism-and-optics/electrodynamics/README.md) · [Quark–gluon plasma](knowledge/07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma/README.md)

### Debye shielding and plasma parameters · `knowledge/10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters`

**Scope.** Saha ionization equilibrium, Debye–Hückel screening, quasi-neutrality, plasma criteria ($L\gg\lambda_D$, $N_D\gg1$, $\omega_p\tau\gg1$), Coulomb collisions and the Coulomb logarithm, Spitzer resistivity, sheaths and the Bohm criterion, parameter maps from interstellar gas to white-dwarf interiors.

**Core ideas.**
- Mobile charges screen any test charge beyond ~$\lambda_D$; on larger scales plasma is quasi-neutral.
- Coulomb collisions are dominated by many small-angle deflections, giving $\ln\Lambda\sim10$–20.
- Hotter plasmas collide less ($\nu\propto nT^{-3/2}$) — fusion plasmas are nearly collisionless.

**Key equations.**
$$\phi(r)=\frac{q}{4\pi\epsilon_0r}e^{-r/\lambda_D},\qquad \eta_{\text{Spitzer}}\approx5\times10^{-5}\frac{Z\ln\Lambda}{T_e[\text{eV}]^{3/2}}\ \Omega\,\text{m}$$

**See also.** [Electrostatics](knowledge/02-electromagnetism-and-optics/electrostatics-and-magnetostatics/electrostatics-and-boundary-value-problems/README.md)

### Dusty and strongly coupled plasmas · `knowledge/10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas`

**Scope.** Coupling parameter $\Gamma$, one-component plasma, Yukawa systems, dust charging, plasma crystals and melting observed particle-by-particle, microgravity experiments (PK-4 on the ISS), ultracold neutral plasmas, dense astrophysical plasmas (white-dwarf interiors), ion crystals in traps.

**Core ideas.**
- When $\Gamma=\frac{q^2}{4\pi\epsilon_0ak_BT}>1$, plasmas behave like liquids; at $\Gamma\approx175$ the OCP crystallizes.
- Micrometre dust grains acquire thousands of electron charges and form visible crystals.
- Strongly coupled plasmas link plasma physics with condensed matter and soft matter.

**Key equations.**
$$\Gamma=\frac{Z^2e^2}{4\pi\epsilon_0ak_BT},\ a=\left(\frac{3}{4\pi n}\right)^{1/3};\qquad V(r)=\frac{Q^2}{4\pi\epsilon_0r}e^{-r/\lambda_D}$$

**See also.** [Colloids](knowledge/08-condensed-matter/soft-matter/colloids-and-granular-matter/README.md) · [High-energy-density physics](knowledge/10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics/README.md)

### Kinetic theory, Vlasov and Landau damping · `knowledge/10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping`

**Scope.** Klimontovich and BBGKY derivations, Vlasov–Poisson and Vlasov–Maxwell systems, linear response and the plasma dielectric function, Landau contour and damping, nonlinear Landau damping (Mouhot–Villani), Bernstein–Greene–Kruskal modes, Lenard–Balescu and Fokker–Planck collision operators, particle-in-cell simulation, gyrokinetic reduction.

**Core ideas.**
- Without collisions, waves still damp: resonant particles near the phase velocity exchange energy with the wave.
- Damping depends on the slope of the distribution at $v=\omega/k$; a positive slope (beam) drives instability instead.
- Landau damping is phase mixing — reversible in principle (plasma echoes).

**Key equations.**
$$\frac{\partial f}{\partial t}+\mathbf v\cdot\nabla f+\frac{q}{m}(\mathbf E+\mathbf v\times\mathbf B)\cdot\nabla_{\mathbf v}f=0,\qquad \gamma\approx\frac{\pi}{2}\frac{\omega_p^3}{k^2}\frac{\partial f_0}{\partial v}\Big|_{v=\omega/k}$$

**Landmark.** Malmberg & Wharton (1964) — see [subfield landmarks](knowledge/10-plasma-physics/plasma-fundamentals/README.md).

**See also.** [Kinetic theory and Boltzmann equation](knowledge/03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation/README.md) · [Gyrokinetics](knowledge/10-plasma-physics/magnetic-confinement-fusion/turbulent-transport-and-gyrokinetics/README.md)

### Plasma waves and instabilities · `knowledge/10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities`

**Scope.** Bohm–Gross Langmuir waves, ion-acoustic waves, EM waves and cutoff at $\omega_p$ (ionospheric reflection), magnetized waves (O, X, R, L, whistlers, CMA diagram), lower-hybrid and Bernstein waves, two-stream and Buneman instabilities, Weibel and firehose/mirror instabilities, drift waves, parametric instabilities.

**Core ideas.**
- EM waves below $\omega_{pe}$ cannot propagate — the ionosphere reflects AM radio; dense plasmas reflect lasers.
- Instabilities need free energy (beams, anisotropy, gradients) and a coupling mechanism.
- Dispersion of radio waves in plasma ($\omega^2=\omega_p^2+c^2k^2$) lets astronomers measure electron columns (pulsars, FRBs).

**Key equations.**
$$\omega^2=\omega_{pe}^2+3k^2v_{th}^2,\qquad \omega^2=\omega_{pe}^2+c^2k^2,\qquad \frac{\omega}{k}=c_s=\sqrt{\frac{k_BT_e}{m_i}}$$

**See also.** [EM waves](knowledge/02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides/README.md) · [Fast radio bursts (dispersion)](knowledge/09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/fast-radio-bursts-and-magnetars/README.md)

### Single-particle motion and drifts · `knowledge/10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts`

**Scope.** Larmor radius and cyclotron motion, guiding-centre approximation, $\mathbf E\times\mathbf B$, gradient, curvature and polarization drifts, magnetic moment as adiabatic invariant, magnetic mirrors and loss cones, second and third invariants, trapped particles in the Van Allen belts and tokamak banana orbits, Penning traps.

**Core ideas.**
- $\mathbf E\times\mathbf B$ drift is charge- and mass-independent — the whole plasma moves.
- Gradient and curvature drifts are charge-dependent, producing currents (ring current).
- Slowly varying fields conserve $\mu=mv_\perp^2/2B$; particles reflect where $B$ is strong enough.

**Key equations.**
$$\mathbf v_E=\frac{\mathbf E\times\mathbf B}{B^2},\qquad \mathbf v_{\nabla B}=\frac{mv_\perp^2}{2qB^3}\mathbf B\times\nabla B,\qquad \sin^2\theta_{\text{loss}}=\frac{B_{\min}}{B_{\max}}$$

**See also.** [Magnetostatics](knowledge/02-electromagnetism-and-optics/electrostatics-and-magnetostatics/magnetostatics/README.md) · [Magnetospheres](knowledge/10-plasma-physics/space-and-astrophysical-plasmas/magnetospheres-and-space-weather/README.md)

## Space and astrophysical plasmas · `knowledge/10-plasma-physics/space-and-astrophysical-plasmas`

#### Overview
Space is a natural plasma laboratory with in situ measurements no lab can match. The Sun's corona expands supersonically as the solar wind, carrying its magnetic field outward; it shapes planetary magnetospheres, drives aurorae and geomagnetic storms, and ends at the heliopause, now crossed by both Voyagers. Collisionless shocks — from Earth's bow shock to supernova remnants — accelerate particles to cosmic-ray energies.

#### Key equations
$$\left(v-\frac{c_s^2}{v}\right)\frac{dv}{dr}=\frac{2c_s^2}{r}-\frac{GM_\odot}{r^2},\qquad r_c=\frac{GM_\odot}{2c_s^2},\qquad r_{mp}\approx\left(\frac{B_0^2}{2\mu_0\rho_{sw}v_{sw}^2}\right)^{1/6}R_E$$

#### Open problems
- How the corona is heated to >1 MK and the wind accelerated.
- Forecasting geomagnetic storms days ahead.

#### Connections
- [Cosmic rays](knowledge/09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays/README.md) · [Magnetic reconnection](knowledge/10-plasma-physics/magnetohydrodynamics/magnetic-reconnection/README.md) · [The Sun](knowledge/09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology/README.md)

### Astrophysical plasmas and shocks · `knowledge/10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks`

**Scope.** Rankine–Hugoniot jump conditions, collisionless shock structure mediated by fields and waves, quasi-parallel vs. quasi-perpendicular shocks, first-order Fermi (diffusive shock) acceleration and the $E^{-2}$ spectrum, Bell's cosmic-ray-driven instability and field amplification, supernova-remnant shells, relativistic shocks in GRBs and pulsar wind nebulae, magnetic reconnection as an accelerator, PIC simulations.

**Core ideas.**
- Collisionless shocks dissipate energy through electromagnetic fields since mean free paths exceed system sizes.
- Particles scattering back and forth across a shock gain energy each cycle, producing a universal power law.
- Accelerated particles amplify the magnetic field ahead of the shock, enabling PeV energies.

**Key equations.**
$$\frac{\rho_2}{\rho_1}=\frac{(\gamma+1)M^2}{(\gamma-1)M^2+2}\to4,\qquad N(E)\propto E^{-\frac{r+2}{r-1}}=E^{-2}\ (r=4)$$

**Landmark.** Blandford & Ostriker (1978) — see [subfield landmarks](knowledge/10-plasma-physics/space-and-astrophysical-plasmas/README.md).

**See also.** [Cosmic rays](knowledge/09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays/README.md) · [Gamma-ray bursts](knowledge/09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/gamma-ray-bursts/README.md)

### Magnetospheres and space weather · `knowledge/10-plasma-physics/space-and-astrophysical-plasmas/magnetospheres-and-space-weather`

**Scope.** Chapman–Ferraro cavity, bow shock and magnetosheath, dayside and nightside reconnection (Dungey cycle), magnetotail and substorms, ring current and Dst index, Van Allen radiation belts and wave–particle acceleration, aurorae, ionosphere, Carrington event (1859), Starlink losses (2022), May 2024 storm, Jupiter's and Saturn's magnetospheres, forecasting.

**Core ideas.**
- Southward interplanetary field reconnects with Earth's field, driving convection and storms.
- Radiation-belt electrons are energized by chorus waves and lost by scattering into the atmosphere.
- Space weather affects satellites, GPS, power grids and astronaut safety.

**Key equations.**
$$\Phi_{PC}\approx v_{sw}B_sL_{\text{eff}},\qquad \text{Dst}\propto-E_{\text{ring current}}\ (\text{Dessler–Parker–Sckopke})$$

**Landmark.** Dungey (1961) — see [subfield landmarks](knowledge/10-plasma-physics/space-and-astrophysical-plasmas/README.md).

**See also.** [Single-particle drifts and mirrors](knowledge/10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts/README.md) · [Magnetic reconnection](knowledge/10-plasma-physics/magnetohydrodynamics/magnetic-reconnection/README.md)

### Solar wind and heliosphere · `knowledge/10-plasma-physics/space-and-astrophysical-plasmas/solar-wind-and-heliosphere`

**Scope.** Parker's isothermal wind and critical point, fast (coronal holes, ~750 km/s) and slow (~400 km/s) wind, Parker spiral, coronal mass ejections, wave vs. nanoflare heating, Parker Solar Probe (switchbacks, Alfvén surface crossing 2021), Solar Orbiter, termination shock and heliopause (Voyager 1 2012, Voyager 2 2018).

**Core ideas.**
- Hot coronal gas cannot be held in hydrostatic equilibrium — it must flow, becoming supersonic beyond a few solar radii.
- The rotating Sun winds the frozen-in field into an Archimedean spiral.
- The corona is ~200× hotter than the photosphere; the energy source is magnetic.

**Key equations.**
$$\tan\psi=\frac{\Omega_\odot r}{v_{sw}}\approx1\ \text{at 1 AU},\qquad \dot M_\odot\approx2\times10^{-14}\,M_\odot\ \text{yr}^{-1}$$

**See also.** [MHD turbulence](knowledge/10-plasma-physics/magnetohydrodynamics/mhd-turbulence/README.md)


---

# Packet 10-4 (98 records)

{"id": "C2678", "a": "08-condensed-matter/superconductivity/cuprate-high-tc-superconductors", "b": "10-plasma-physics/magnetic-confinement-fusion/burning-plasmas-and-iter", "name": "REBCO high-temperature superconductors for compact tokamaks", "kind": "shared object", "summary": "Rare-earth barium copper oxide (REBCO) cuprate tapes carry high currents at 20 K and above 20 T, allowing compact high-field tokamaks (SPARC, ARC) because fusion power density scales as B^4 at fixed beta; quench protection and neutron degradation of the cuprate are open engineering problems.", "map": "P_{\\text{fus}}/V\\propto\\beta^2B^4,\\ \\beta=\\frac{2\\mu_0\\langle p\\rangle}{B^2}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2679", "a": "08-condensed-matter/superconductivity/hydride-superconductors-under-pressure", "b": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "name": "Dense hydrogen: superconductors and laser-shock experiments", "kind": "shared object", "summary": "The insulator-metal transition of dense hydrogen and deuterium, the root of the metallic-hydrogen and hydride-superconductor programme, is probed both in diamond-anvil cells and in dynamic compression at NIF and the Z machine; the two disagree on the transition pressure, partly because of temperature and DFT functional choices.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2680", "a": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Band topology of magnetized plasma waves", "kind": "method transfer", "summary": "Chern numbers and bulk-boundary correspondence, developed for electronic bands, classify the wave bands of magnetized cold plasmas; a topological gaseous plasmon polariton is predicted at plasma interfaces with a sign change of B or density.", "map": "C_n=\\frac1{2\\pi}\\int\\Omega_n(\\mathbf k)d^2k\\ \\text{for the Maxwell-fluid eigenproblem }\\omega\\psi=H(\\mathbf k)\\psi", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2681", "a": "08-condensed-matter/topological-matter/quantum-hall-effects", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Guiding-centre drift and the Hall effect", "kind": "identity", "summary": "In crossed E and B fields charged particles drift at E x B / B^2 regardless of charge or mass; in a 2D electron gas this drift gives the classical Hall conductivity, and quantized cyclotron orbits (Landau levels) with skipping orbits at edges become the chiral edge states of the quantum Hall effect.", "map": "\\mathbf v_E=\\frac{\\mathbf E\\times\\mathbf B}{B^2}\\Rightarrow\\sigma_{xy}=\\frac{ne}{B}\\to\\nu\\frac{e^2}{h}\\ (n=\\nu eB/h);\\ \\omega_c=\\frac{eB}{m^*}", "breaks": "", "confidence": "established", "strength": 2}
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
{"id": "C2795", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "b": "10-plasma-physics/space-and-astrophysical-plasmas/solar-wind-and-heliosphere", "name": "Parker wind and coronal heating", "kind": "shared object", "summary": "The corona, with its heating problem, is the base of the Parker wind. Alfvén-wave turbulence and reconnection are candidate heaters, and the transonic wind solution follows from hydrodynamic equations.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2828", "a": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "b": "10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas", "name": "Strongly coupled plasma models for HED matter", "kind": "method transfer", "summary": "One-component plasma, Yukawa fluids and molecular-dynamics results from dusty and ultracold plasmas supply structure factors and transport coefficients used to interpret X-ray Thomson scattering and equations of state.", "map": "S(k),\\ \\Gamma", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2829", "a": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "b": "10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas", "name": "Warm dense matter as strongly coupled plasma", "kind": "shared object", "summary": "Warm dense matter sits at coupling parameter Gamma of order 1 and degeneracy of order 1, the regime where one-component plasma models and dusty-plasma analogues apply. HED experiments probe this regime.", "map": "\\Gamma = \\frac{Z^2 e^2}{4\\pi\\epsilon_0 a k_B T}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2830", "a": "10-plasma-physics/inertial-and-laser-plasmas/inertial-confinement-fusion", "b": "10-plasma-physics/magnetic-confinement-fusion/burning-plasmas-and-iter", "name": "Alpha self-heating and ignition in ICF and MCF", "kind": "shared object", "summary": "Both routes aim at burning plasmas dominated by alpha heating, with ignition set by alpha deposition exceeding losses. They differ in the confinement mechanism: inertia, with a rho-R criterion, versus magnetic fields, with a nTtau criterion.", "map": "n T \\tau_E \\gtrsim 3\\times10^{21}\\ \\mathrm{keV\\,s\\,m^{-3}}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2831", "a": "10-plasma-physics/inertial-and-laser-plasmas/inertial-confinement-fusion", "b": "10-plasma-physics/magnetic-confinement-fusion/burning-plasmas-and-iter", "name": "Burning-plasma physics across confinement schemes", "kind": "analogy", "summary": "Alpha heating, thermal-instability feedback and the Lawson criterion are shared concepts. Fuel assembly by compression is replaced by long-pulse steady confinement.", "map": "", "breaks": "ICF burn lasts about 100 ps and is limited by hydrodynamic disassembly. MCF burn is quasi-steady and limited by transport, MHD stability and exhaust.", "confidence": "established", "strength": 2}
{"id": "C2832", "a": "10-plasma-physics/inertial-and-laser-plasmas/inertial-confinement-fusion", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "Rayleigh–Taylor instability in ICF and MHD interchange", "kind": "analogy", "summary": "Rayleigh–Taylor growth at the ablation front and in the hot spot parallels the interchange instability, where bad field curvature acts as effective gravity.", "map": "\\gamma^2=A k g", "breaks": "Ablation stabilises ICF RT growth. The interchange instability is set by field-line curvature and pressure gradient, not by an acceleration.", "confidence": "established", "strength": 2}
{"id": "C2833", "a": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "b": "10-plasma-physics/inertial-and-laser-plasmas/plasma-wakefield-acceleration", "name": "Ponderomotive force in wakefields", "kind": "mechanism", "summary": "The ponderomotive force of a laser pulse expels electrons and excites the wake. Relativistic self-focusing and channeling guide the pulse.", "map": "F_p=-\\frac{e^2}{4m\\omega^2}\\nabla E^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2834", "a": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "b": "10-plasma-physics/low-temperature-and-applied-plasmas/plasma-discharges-and-processing", "name": "Collisional absorption and ionization", "kind": "mechanism", "summary": "Collisional (inverse bremsstrahlung) heating of electrons by an oscillating field and the resulting ionization avalanche follow the same physics in RF discharges and laser-produced plasmas.", "map": "\\nu_{ei}\\propto Z n_e T_e^{-3/2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2835", "a": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Parametric instabilities in laser plasmas", "kind": "mechanism", "summary": "Stimulated Raman and Brillouin scattering and two-plasmon decay are three-wave couplings of light with Langmuir and ion-acoustic waves. They limit laser coupling in ICF.", "map": "\\omega_0=\\omega_s+\\omega_{pl}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2836", "a": "10-plasma-physics/inertial-and-laser-plasmas/plasma-wakefield-acceleration", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Wakefields as driven Langmuir waves", "kind": "identity", "summary": "A wakefield is a driven plasma oscillation at the plasma frequency with phase velocity equal to the driver velocity. The wave-breaking field sets the scale of the accelerating gradient.", "map": "E_0=\\frac{m c\\,\\omega_p}{e}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2837", "a": "10-plasma-physics/low-temperature-and-applied-plasmas/atmospheric-pressure-plasmas-and-applications", "b": "10-plasma-physics/low-temperature-and-applied-plasmas/plasma-discharges-and-processing", "name": "Streamer and dielectric-barrier breakdown", "kind": "mechanism", "summary": "Townsend avalanche and streamer breakdown in atmospheric DBDs and jets follow the same Paschen breakdown physics as low-pressure processing discharges, but at much higher pd and collisionality.", "map": "V_b=f(pd)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2838", "a": "10-plasma-physics/low-temperature-and-applied-plasmas/plasma-discharges-and-processing", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Debye sheaths in processing plasmas", "kind": "mechanism", "summary": "Debye shielding sets the sheath thickness at electrodes and wafers. The Bohm criterion and Child–Langmuir law determine ion energy and flux in etching and deposition.", "map": "\\lambda_D=\\sqrt{\\epsilon_0 k_B T_e/ n e^2},\\ J=\\tfrac{4}{9}\\epsilon_0\\sqrt{2e/M}\\,V^{3/2}/s^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2839", "a": "10-plasma-physics/magnetic-confinement-fusion", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Guiding-centre drifts in toroidal confinement", "kind": "mechanism", "summary": "Grad-B and curvature drifts in a torus cause vertical charge separation, so a rotational transform is needed. Trapped-particle banana orbits arise from the mirror force and adiabatic invariants, and they set neoclassical transport.", "map": "\\mu=\\frac{m v_\\perp^2}{2B},\\ \\mathbf v_d\\propto \\frac{\\mathbf B\\times\\nabla B}{B^3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2840", "a": "10-plasma-physics/magnetic-confinement-fusion/stellarators", "b": "10-plasma-physics/magnetohydrodynamics/dynamo-theory", "name": "Laboratory and fusion dynamo relaxation", "kind": "analogy", "summary": "Reversed-field pinch and spheromak relaxation show a dynamo-like conversion of helicity. Stellarators avoid the dynamo by using external coils.", "map": "", "breaks": "Stellarators are not dynamos. The mapping applies to the RFP and spheromak, not to stellarator confinement.", "confidence": "established", "strength": 1}
{"id": "C2841", "a": "10-plasma-physics/magnetic-confinement-fusion/stellarators", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Quasi-symmetry and omnigeneity from guiding-centre motion", "kind": "identity", "summary": "Quasi-symmetry makes the guiding-centre Hamiltonian depend on |B| only through a symmetric combination, so a conserved canonical momentum confines particles as in a tokamak. Omnigeneity confines trapped orbits.", "map": "B=B(\\psi,M\\theta-N\\varphi)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2842", "a": "10-plasma-physics/magnetic-confinement-fusion/tokamaks", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "Alfvén physics in tokamaks", "kind": "mechanism", "summary": "Alfvén waves and continuum damping underlie fast-ion-driven Alfvén eigenmodes, and frozen-in flux constrains tokamak equilibria and disruption dynamics.", "map": "v_A=B/\\sqrt{\\mu_0\\rho}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2843", "a": "10-plasma-physics/magnetic-confinement-fusion/tokamaks", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "MHD equilibrium and stability of tokamaks", "kind": "shared object", "summary": "Grad–Shafranov equilibrium, the safety factor, and kink, ballooning and interchange stability come from ideal MHD energy principles. They set the Troyon beta limit and the Kruskal–Shafranov current limit.", "map": "\\nabla p=\\mathbf J\\times\\mathbf B,\\ q\\gtrsim1", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2844", "a": "10-plasma-physics/magnetic-confinement-fusion/tokamaks", "b": "10-plasma-physics/magnetohydrodynamics/magnetic-reconnection", "name": "Sawteeth, tearing modes and disruptions", "kind": "mechanism", "summary": "Sawtooth crashes, neoclassical tearing modes and the thermal and current quench of disruptions involve resistive reconnection and magnetic island formation. The Kadomtsev model is a reconnection model.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2845", "a": "10-plasma-physics/magnetic-confinement-fusion/turbulent-transport-and-gyrokinetics", "b": "10-plasma-physics/magnetohydrodynamics/mhd-turbulence", "name": "Gyrokinetic codes for astrophysical turbulence", "kind": "method transfer", "summary": "Gyrokinetic theory built for tokamak drift waves was adapted to astrophysical plasmas, for example the Alfvénic cascade in the solar wind, using the same low-frequency anisotropic ordering.", "map": "k_\\parallel\\ll k_\\perp,\\ \\omega\\ll\\Omega_i", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2846", "a": "10-plasma-physics/magnetic-confinement-fusion/turbulent-transport-and-gyrokinetics", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Gyrokinetics from Vlasov theory", "kind": "method transfer", "summary": "Gyrokinetics is the Vlasov–Maxwell system averaged over gyro-phase using adiabatic invariants. It keeps Landau-type wave-particle resonances and drives drift-wave turbulence and zonal flows.", "map": "\\partial_t f+\\mathbf v\\cdot\\nabla f+\\tfrac{q}{m}(\\mathbf E+\\mathbf v\\times\\mathbf B)\\cdot\\partial_{\\mathbf v}f=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2847", "a": "10-plasma-physics/magnetic-confinement-fusion/turbulent-transport-and-gyrokinetics", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Landau resonance in drift-wave transport", "kind": "mechanism", "summary": "Landau damping and the resonant wave-particle energy exchange set the growth and saturation of ITG and TEM modes. Collisionless zonal-flow damping, the Rosenbluth–Hinton residual, is also a kinetic effect.", "map": "\\omega=\\mathbf k\\cdot\\mathbf v", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2848", "a": "10-plasma-physics/magnetohydrodynamics/dynamo-theory", "b": "10-plasma-physics/space-and-astrophysical-plasmas/magnetospheres-and-space-weather", "name": "Geodynamo as the source of the magnetosphere", "kind": "shared object", "summary": "Earth's magnetic field, produced by the geodynamo, forms the magnetospheric cavity. Its dipole nature sets the radiation belts and the aurora geometry.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2849", "a": "10-plasma-physics/magnetohydrodynamics/dynamo-theory", "b": "10-plasma-physics/space-and-astrophysical-plasmas/solar-wind-and-heliosphere", "name": "Solar dynamo and the heliospheric field", "kind": "mechanism", "summary": "The solar dynamo generates the cycle-varying field that the wind drags out into the Parker spiral and the heliospheric current sheet. The cycle modulates wind structure and space weather.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2850", "a": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "MHD waves as the low-frequency limit of plasma waves", "kind": "identity", "summary": "Alfvén and magnetosonic waves are the low-frequency fluid limits of the kinetic cold-plasma dispersion relation, which includes whistlers and ion cyclotron waves at higher frequency.", "map": "\\omega=k_\\parallel v_A", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2851", "a": "10-plasma-physics/magnetohydrodynamics/magnetic-reconnection", "b": "10-plasma-physics/space-and-astrophysical-plasmas", "name": "Reconnection across space plasmas", "kind": "shared object", "summary": "Reconnection powers solar flares, coronal mass ejections and magnetospheric substorms. It also appears in the heliospheric current sheet and in particle acceleration in astrophysical sources.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2852", "a": "10-plasma-physics/magnetohydrodynamics/magnetic-reconnection", "b": "10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks", "name": "Relativistic reconnection as particle accelerator", "kind": "mechanism", "summary": "Relativistic reconnection in pulsar winds, jets and magnetar flares accelerates non-thermal particles through X-point and plasmoid dynamics. It competes with diffusive shock acceleration.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2853", "a": "10-plasma-physics/magnetohydrodynamics/magnetic-reconnection", "b": "10-plasma-physics/space-and-astrophysical-plasmas/magnetospheres-and-space-weather", "name": "Dayside and tail reconnection in the Dungey cycle", "kind": "shared object", "summary": "Reconnection at the magnetopause and in the magnetotail drives the Dungey cycle, substorms and flux transfer events. MMS directly observed the electron diffusion region.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2854", "a": "10-plasma-physics/magnetohydrodynamics/magnetic-reconnection", "b": "10-plasma-physics/space-and-astrophysical-plasmas/magnetospheres-and-space-weather", "name": "Space weather driven by reconnection", "kind": "mechanism", "summary": "Southward interplanetary magnetic field opens the magnetosphere via dayside reconnection. This loads the tail and drives geomagnetic storms.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2855", "a": "10-plasma-physics/magnetohydrodynamics/mhd-turbulence", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Kinetic dissipation of MHD cascades", "kind": "mechanism", "summary": "At ion and electron scales the MHD cascade becomes a kinetic Alfvén wave cascade. Landau damping, in the form of transit-time damping, and cyclotron resonance remove energy, with a gyrokinetic description such as the one used in tokamaks.", "map": "", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2856", "a": "10-plasma-physics/magnetohydrodynamics/mhd-turbulence", "b": "10-plasma-physics/space-and-astrophysical-plasmas/solar-wind-and-heliosphere", "name": "Solar wind as an MHD turbulence laboratory", "kind": "shared object", "summary": "In situ spacecraft measurements of solar wind fluctuations test anisotropic Alfvénic cascade theories such as Goldreich–Sridhar and critical balance. The spectrum and its kinetic-scale break are also linked to coronal heating.", "map": "E(k_\\perp)\\propto k_\\perp^{-5/3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2857", "a": "10-plasma-physics/magnetohydrodynamics/mhd-turbulence", "b": "10-plasma-physics/space-and-astrophysical-plasmas/solar-wind-and-heliosphere", "name": "Turbulent heating of the corona and wind", "kind": "mechanism", "summary": "Alfvén-wave turbulence cascades energy to ion-kinetic scales, where it heats ions by cyclotron or stochastic processes. This is a leading explanation for coronal and solar wind heating.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2858", "a": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "b": "10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks", "name": "Streaming instabilities in shocks and cosmic rays", "kind": "mechanism", "summary": "Weibel, Bell and cosmic-ray streaming instabilities amplify magnetic fields and scatter particles at collisionless shocks, enabling diffusive shock acceleration.", "map": "\\gamma\\sim k v_{cr}\\sqrt{n_{cr}/n_i}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2859", "a": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "b": "10-plasma-physics/space-and-astrophysical-plasmas/magnetospheres-and-space-weather", "name": "Adiabatic invariants and radiation belts", "kind": "mechanism", "summary": "Gyration, bounce and drift motion with conserved adiabatic invariants trap particles in the van Allen belts. Violating an invariant by ULF waves or substorm injection drives radial transport and acceleration.", "map": "\\mu,\\ J,\\ \\Phi", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2860", "a": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "b": "10-plasma-physics/space-and-astrophysical-plasmas/magnetospheres-and-space-weather", "name": "Ring current and drifts", "kind": "mechanism", "summary": "The ring current is the westward drift of ions and eastward drift of electrons, driven by gradient and curvature drifts in the dipole field. It depresses the surface field in storms, measured by Dst.", "map": "\\mathbf v_{\\nabla B}=\\frac{m v_\\perp^2}{2qB^3}\\mathbf B\\times\\nabla B", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2861", "a": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "High-pressure equations of state for planetary cores", "kind": "shared object", "summary": "Laser-shock and diamond-anvil experiments measure iron's equation of state and melting at core pressures, calibrating seismically inferred inner-core density and temperature.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2862", "a": "10-plasma-physics/inertial-and-laser-plasmas/inertial-confinement-fusion", "b": "11-interdisciplinary-physics/medical-physics/radiation-therapy", "name": "Charged-particle stopping power", "kind": "shared object", "summary": "Alpha and ion energy deposition in dense plasma and Bragg-peak dose deposition in tissue both follow Bethe-type stopping physics, with plasma screening modifying stopping in hot targets.", "map": "", "breaks": "Free-electron collective response in plasmas changes stopping relative to bound-electron tissue.", "confidence": "established", "strength": 1}
{"id": "C2863", "a": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "b": "11-interdisciplinary-physics/accelerator-physics", "name": "Laser-driven particle and radiation sources", "kind": "shared object", "summary": "Intense lasers in plasma drive electron and ion beams and betatron or undulator-like radiation, producing compact versions of accelerator and light-source outputs.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2864", "a": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Radiation by accelerated charges", "kind": "identity", "summary": "Betatron radiation in plasma, relativistic Thomson scattering and undulator radiation all derive from the Liénard–Liparticle radiation formula for accelerated relativistic charges.", "map": "K=\\gamma\\,\\beta_\\perp\\ \\text{(wiggler parameter)}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2865", "a": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "b": "11-interdisciplinary-physics/medical-physics/radiation-therapy", "name": "Laser-driven ion acceleration for proton therapy", "kind": "shared object", "summary": "Target-normal sheath acceleration produces MeV-scale protons from laser-irradiated foils, targeted at Bragg-peak therapy, though current energies and reproducibility fall short.", "map": "", "breaks": "", "confidence": "current research", "strength": 1}
{"id": "C2866", "a": "10-plasma-physics/inertial-and-laser-plasmas/plasma-wakefield-acceleration", "b": "11-interdisciplinary-physics/accelerator-physics", "name": "Accelerator physics applied to plasma acceleration", "kind": "method transfer", "summary": "Emittance, beta-function matching, energy spread and staging from conventional beam dynamics are the figures of merit for plasma-accelerated beams.", "map": "\\sigma_r=\\sqrt{\\epsilon\\beta},\\ \\beta_m=\\sqrt{2\\gamma}/k_p", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2867", "a": "10-plasma-physics/inertial-and-laser-plasmas/plasma-wakefield-acceleration", "b": "11-interdisciplinary-physics/accelerator-physics", "name": "Plasma wakefields as compact accelerators", "kind": "shared object", "summary": "Plasma wakefield accelerators replace RF cavities with plasma waves sustaining GV/m gradients; beam dynamics, emittance and staging concepts from accelerator physics govern their beam quality.", "map": "E_{wb}=m_e c\\,\\omega_p/e", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2868", "a": "10-plasma-physics/inertial-and-laser-plasmas/plasma-wakefield-acceleration", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Betatron oscillations in ion channel", "kind": "identity", "summary": "Beam electrons in the plasma ion-channel focusing field undergo betatron oscillations with the same envelope equations as strong focusing lattices, with focusing strength set by plasma density.", "map": "\\omega_\\beta=\\omega_p/\\sqrt{2\\gamma}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2869", "a": "10-plasma-physics/inertial-and-laser-plasmas/plasma-wakefield-acceleration", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Plasma-driven free-electron lasers", "kind": "method transfer", "summary": "Plasma-accelerated beams and betatron emission are being used to drive FELs and X-ray sources, but the FEL's tight emittance and energy-spread demands challenge plasma beams.", "map": "\\rho_{FEL}\\propto (I/\\gamma^3\\sigma^2)^{1/3}", "breaks": "Plasma beams' percent-level energy spread typically exceeds the FEL Pierce parameter tolerance.", "confidence": "current research", "strength": 2}
{"id": "C2870", "a": "10-plasma-physics/inertial-and-laser-plasmas/plasma-wakefield-acceleration", "b": "11-interdisciplinary-physics/medical-physics/radiation-therapy", "name": "Compact accelerators for radiotherapy", "kind": "shared object", "summary": "Laser-plasma ion and electron beams are proposed as compact sources for proton therapy and FLASH radiotherapy, but stability and energy spread remain limiting.", "map": "", "breaks": "", "confidence": "proposed", "strength": 1}
{"id": "C2871", "a": "10-plasma-physics/low-temperature-and-applied-plasmas", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Plasma processing for device fabrication", "kind": "method transfer", "summary": "Plasma etching, deposition and ion implantation-related processes pattern and build transistors and solar cells; sheath physics sets ion energy and anisotropy of etched features.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2872", "a": "10-plasma-physics/low-temperature-and-applied-plasmas", "b": "11-interdisciplinary-physics/chemical-physics/surface-science-and-catalysis", "name": "Plasma–surface interactions and plasma catalysis", "kind": "shared object", "summary": "Plasma radicals and ions adsorb, react and sputter at surfaces, linking discharge physics to adsorption, surface reactions and plasma-assisted catalysis.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2873", "a": "10-plasma-physics/low-temperature-and-applied-plasmas/atmospheric-pressure-plasmas-and-applications", "b": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "name": "Plasma medicine and biological response", "kind": "shared object", "summary": "Cold atmospheric plasmas deliver reactive oxygen and nitrogen species to cells and tissue, so biological sensing and response physics determines therapeutic and toxic outcomes.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2874", "a": "10-plasma-physics/low-temperature-and-applied-plasmas/atmospheric-pressure-plasmas-and-applications", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Non-equilibrium plasma chemistry and reaction kinetics", "kind": "mechanism", "summary": "Electron-impact dissociation, vibrational excitation and radical reactions in cold plasmas follow state-resolved rate theory and potential-energy-surface concepts, with electron temperature far above gas temperature.", "map": "k(T_e)=\\int \\sigma(E)\\,v\\,f(E)\\,dE", "breaks": "Rate theories assuming a single Boltzmann temperature fail when electron and gas temperatures differ strongly.", "confidence": "established", "strength": 2}
{"id": "C2875", "a": "10-plasma-physics/low-temperature-and-applied-plasmas/plasma-discharges-and-processing", "b": "11-interdisciplinary-physics/chemical-physics/surface-science-and-catalysis", "name": "Surface chemistry underlying plasma etching", "kind": "shared object", "summary": "Etch and deposition rates and selectivity are set by adsorption, ion-enhanced surface reactions and sputter yields studied in surface science.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2876", "a": "10-plasma-physics/magnetic-confinement-fusion/burning-plasmas-and-iter", "b": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "name": "Neutral beam injectors as ion accelerators", "kind": "method transfer", "summary": "Neutral beam heating of fusion plasmas relies on ion source, electrostatic acceleration and neutraliser technology developed in accelerator physics.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2877", "a": "10-plasma-physics/magnetic-confinement-fusion/stellarators", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Hamiltonian field-line flow and storage-ring dynamics", "kind": "analogy", "summary": "Magnetic field lines in toroidal devices form a Hamiltonian system with islands and KAM surfaces, as do particle orbits in storage rings with nonlinear resonances.", "map": "H(\\psi,\\theta,\\phi)\\ \\leftrightarrow\\ H(J,\\varphi,s)", "breaks": "Field-line flow has no physical particle dynamics, and rotational transform plays the role of tune.", "confidence": "established", "strength": 2}
{"id": "C2878", "a": "10-plasma-physics/magnetic-confinement-fusion/tokamaks", "b": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "name": "Superconducting magnets and RF technology", "kind": "method transfer", "summary": "Tokamaks and accelerators share superconducting magnet technology (Nb3Sn, NbTi, HTS) and RF heating or klystron sources, with cross-fertilised cryogenics and power systems.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2879", "a": "10-plasma-physics/magnetic-confinement-fusion/turbulent-transport-and-gyrokinetics", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Drift waves and Rossby waves", "kind": "identity", "summary": "Drift waves in magnetized plasma obey the Hasegawa–Mima equation, mathematically identical to the Charney–Hasegawa–Mima quasi-geostrophic equation, with zonal flows paralleling atmospheric jets.", "map": "\\partial_t(\\nabla^2\\phi-\\phi)+v_*\\partial_y\\phi+J(\\phi,\\nabla^2\\phi)=0", "breaks": "Plasma drift waves involve adiabatic electron response and finite Larmor radius, with no direct atmospheric counterpart.", "confidence": "established", "strength": 3}
{"id": "C2880", "a": "10-plasma-physics/magnetohydrodynamics/dynamo-theory", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics", "name": "Planetary dynamos in Earth science", "kind": "shared object", "summary": "Earth's field generation and reversals are a dynamo problem in rotating convecting conducting fluid, linking geophysics to MHD dynamo theory.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2881", "a": "10-plasma-physics/magnetohydrodynamics/dynamo-theory", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Rotating convective flows and quasi-geostrophy", "kind": "analogy", "summary": "Core convection under rapid rotation is Taylor–Proudman constrained, mirroring geostrophic balance and Rossby-wave dynamics in the atmosphere, with Lorentz force replacing part of the Coriolis balance.", "map": "2\\boldsymbol\\Omega\\times\\mathbf u=-\\nabla p/\\rho", "breaks": "Magnetic field and Lorentz force alter the force balance (magnetostrophic), and there is no atmospheric analogue of induction.", "confidence": "established", "strength": 2}
{"id": "C2882", "a": "10-plasma-physics/magnetohydrodynamics/dynamo-theory", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics", "name": "Rotating stratified turbulence", "kind": "analogy", "summary": "Ocean and core flows both exhibit rotation-dominated turbulence with inverse cascades and large-scale coherent structures, offering shared numerical and scaling tools.", "map": "", "breaks": "Core flows are electrically conducting with Lorentz feedback, absent in oceans.", "confidence": "current research", "strength": 1}
{"id": "C2883", "a": "10-plasma-physics/magnetohydrodynamics/dynamo-theory", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Geodynamo and the liquid outer core", "kind": "shared object", "summary": "Earth's magnetic field is sustained by convective dynamo action in the liquid iron outer core, whose structure and inner-core growth are constrained by seismology.", "map": "\\partial_t\\mathbf B=\\nabla\\times(\\mathbf u\\times\\mathbf B)+\\eta\\nabla^2\\mathbf B", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2884", "a": "10-plasma-physics/magnetohydrodynamics/dynamo-theory", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Seismic constraints on dynamo core", "kind": "shared object", "summary": "Seismic models give core radius, inner-core size and density jump, supplying boundary conditions and energy budget for geodynamo simulations.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2885", "a": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Alfvén waves and Rossby waves", "kind": "analogy", "summary": "Magnetic tension restoring Alfvén waves parallels the Coriolis restoring force of inertial and Rossby waves, and both reduce to similar dispersion structures in rotating or magnetized media.", "map": "\\omega=k_\\parallel v_A\\ \\leftrightarrow\\ \\omega=2\\Omega k_\\parallel/k", "breaks": "Alfvén waves are non-dispersive, while Rossby and inertial waves are strongly dispersive and anisotropic differently.", "confidence": "established", "strength": 1}
{"id": "C2886", "a": "10-plasma-physics/magnetohydrodynamics/mhd-turbulence", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Turbulent cascades in anisotropic media", "kind": "analogy", "summary": "Anisotropic MHD cascades and quasi-2D geostrophic turbulence both develop strong anisotropy and inverse or dual transfers under a strong organizing field or rotation.", "map": "", "breaks": "MHD has forward energy cascade in 3D with critical balance, differing from atmospheric inverse energy cascade.", "confidence": "current research", "strength": 1}
{"id": "C2887", "a": "10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Space charge and beam plasma physics", "kind": "analogy", "summary": "Intense charged beams behave as non-neutral plasmas with Debye length, plasma frequency, space-charge tune shift and Coulomb-crystal ordering in cooled ion beams.", "map": "\\omega_p^2=\\frac{n q^2}{\\epsilon_0 m\\gamma^3}", "breaks": "Beams are non-neutral and lack quasi-neutrality, so screening and collective response differ from true plasmas.", "confidence": "established", "strength": 2}
{"id": "C2888", "a": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Vlasov description of beams", "kind": "identity", "summary": "Collective beam dynamics uses the Vlasov equation in phase space, with Landau damping of coherent modes via tune spread, equivalent to plasma Landau damping.", "map": "\\partial_t f+\\dot q\\,\\partial_q f+\\dot p\\,\\partial_p f=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2889", "a": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Beam instabilities as streaming instabilities", "kind": "mechanism", "summary": "Two-stream, Weibel and head-tail or microwave instabilities in beams share the kinetic-instability machinery of plasma physics, including Landau damping used to stabilise bunches.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2890", "a": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Ionospheric and radiative propagation in plasma", "kind": "shared object", "summary": "Electromagnetic wave propagation in ionised media, with plasma frequency cutoff, underlies ionospheric reflection and remote sensing, alongside atmospheric radiative physics.", "map": "n^2=1-\\omega_p^2/\\omega^2", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C2891", "a": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Adiabatic invariants and magnetic focusing", "kind": "mechanism", "summary": "Gyration, mirror trapping and adiabatic invariants in plasma map onto betatron motion, Courant–Snyder invariants and magnetic confinement in storage rings and traps.", "map": "\\mu=\\frac{p_\\perp^2}{2mB}\\ \\leftrightarrow\\ J=\\oint p\\,dq", "breaks": "Accelerator lattices use alternating-gradient focusing with no plasma-style collective response.", "confidence": "established", "strength": 2}