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

# Packet 10-2 (100 records)

{"id": "C1239", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "10-plasma-physics/magnetic-confinement-fusion/tokamaks", "name": "Synchrotron and bremsstrahlung losses in tokamaks", "kind": "shared object", "summary": "Electron cyclotron emission, synchrotron losses and bremsstrahlung from Larmor radiation set power balance and provide temperature diagnostics in fusion plasmas.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1240", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks", "name": "Synchrotron emission from shock-accelerated electrons", "kind": "shared object", "summary": "Relativistic electrons accelerated at shocks radiate synchrotron emission in amplified fields. Power-law spectra reveal the acceleration process in supernova remnants.", "map": "P\\propto\\gamma^2B^2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1241", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "name": "Thomson scattering as plasma diagnostic", "kind": "method transfer", "summary": "Thomson scattering from free electrons is used to measure density, temperature and collective modes in plasmas. X-ray Thomson scattering diagnoses warm dense matter.", "map": "S(k,\\omega),\\ \\alpha=1/(k\\lambda_D)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1242", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Collective Thomson scattering and the dynamic structure factor", "kind": "mechanism", "summary": "Collective Thomson scattering probes the electron and ion-acoustic fluctuation spectrum, which follows from Vlasov dielectric response. Landau damping shapes resonance widths.", "map": "S(k,\\omega)\\propto \\frac{\\mathrm{Im}\\,\\epsilon^{-1}}{\\ldots}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1550", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/heat-engines-and-efficiency", "b": "10-plasma-physics/magnetic-confinement-fusion/burning-plasmas-and-iter", "name": "Fusion power plant as heat engine", "kind": "shared object", "summary": "A fusion reactor's net electricity is bounded by thermal-cycle (Rankine/Carnot) efficiency of the blanket coolant loop, while the plasma energy balance uses Lawson-type gain analogous to engine power balance.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1551", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/phase-equilibria-and-chemical-potential", "b": "10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas", "name": "Plasma phase transitions and crystals", "kind": "shared object", "summary": "Dusty-plasma crystals, Wigner crystallization and the plasma phase transition in dense hydrogen are phase-coexistence problems treated with chemical potential and equation-of-state constructions.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1552", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/thermodynamic-potentials-and-maxwell-relations", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "Magnetic pressure and MHD thermodynamics", "kind": "shared object", "summary": "Ideal MHD closes with adiabatic equation of state and magnetic pressure; plasma beta compares thermal and magnetic pressure, and interchange stability uses entropy-like invariants pV^γ.", "map": "\\beta=\\frac{2\\mu_0 p}{B^2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1553", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/percolation", "b": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "name": "Percolation and insulator–metal transitions", "kind": "analogy", "summary": "Pressure ionization and metallization in dense matter are sometimes modelled with percolation of conducting regions or bound-state clusters.", "map": "", "breaks": "Real metallization is a quantum many-body phenomenon, not purely geometric.", "confidence": "proposed", "strength": 1}
{"id": "C1554", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/percolation", "b": "10-plasma-physics/magnetohydrodynamics/magnetic-reconnection", "name": "Percolation of plasmoids and field lines", "kind": "analogy", "summary": "Field-line connectivity and merging plasmoid chains in reconnection layers have been described with percolation concepts, including Rechester–Rosenbluth-like stochastic field-line transport thresholds.", "map": "", "breaks": "Dynamics and MHD constraints, not static random geometry, control the plasmoid hierarchy.", "confidence": "proposed", "strength": 1}
{"id": "C1555", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "b": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "name": "Equations of state for warm dense matter", "kind": "method transfer", "summary": "HED equations of state are built from free-energy models and ensemble methods (Saha ionization equilibrium, path-integral Monte Carlo, DFT-MD) applied to partially ionized, degenerate matter.", "map": "", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1556", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "Relaxed states and Taylor relaxation", "kind": "method transfer", "summary": "Taylor relaxation finds minimum magnetic energy at fixed helicity, a constrained variational principle like maximum-entropy with conserved quantities, producing force-free states in reversed-field pinches and spheromaks.", "map": "\\nabla\\times\\mathbf B=\\mu\\mathbf B", "breaks": "Relaxation requires turbulent reconnection, not true thermal equilibrium; ergodic hypotheses are heuristic.", "confidence": "established", "strength": 2}
{"id": "C1557", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Debye–Hückel screening", "kind": "identity", "summary": "Debye shielding is the Debye–Hückel mean-field treatment of a Coulomb system in the canonical/grand canonical ensemble: linearized Poisson–Boltzmann gives the screened potential and the leading correlation free-energy correction.", "map": "\\nabla^2\\phi=\\lambda_D^{-2}\\phi,\\; \\lambda_D^2=\\frac{\\varepsilon_0k_BT}{ne^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1558", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "b": "10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas", "name": "Strongly coupled one-component plasma", "kind": "shared object", "summary": "The one-component plasma is a classic liquid-state model with coupling Γ; its Monte Carlo/MD equation of state and freezing near Γ≈175 connect plasma physics to classical liquid theory.", "map": "\\Gamma=\\frac{Q^2}{4\\pi\\varepsilon_0 a k_BT}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1559", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Statistical mechanics in magnetic fields (Bohr–van Leeuwen)", "kind": "identity", "summary": "Classical equilibrium partition function is independent of B, so classical plasmas have no magnetization (Bohr–van Leeuwen); diamagnetic currents are cancelled by boundary orbits, with magnetic moment conservation tied to adiabatic invariants.", "map": "", "breaks": "Applies to thermal equilibrium; nonequilibrium plasmas with adiabatic invariants show strong magnetic effects.", "confidence": "established", "strength": 2}
{"id": "C1560", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "b": "10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks", "name": "Non-Maxwellian tails and nonextensive statistics", "kind": "analogy", "summary": "Space plasmas show kappa distributions with power-law tails, which some interpret via Tsallis nonextensive statistics; alternatively tails arise from acceleration and turbulence.", "map": "", "breaks": "Tsallis interpretation is contested; kinetic acceleration models explain tails without it.", "confidence": "proposed", "strength": 1}
{"id": "C1561", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Gibbs entropy and velocity-space cascade", "kind": "mechanism", "summary": "Free-energy conservation in gyrokinetics combines entropy of fluctuations with field energy, and Landau-damped energy appears as fine-scale velocity structure; coarse-graining sets irreversible heating.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1562", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "name": "Degenerate electrons in HED matter", "kind": "shared object", "summary": "Warm dense matter and ICF fuel compression involve partially degenerate Fermi gases; the Fermi energy versus temperature sets the degeneracy parameter, and Fermi-gas pressure limits compression.", "map": "\\theta=k_BT/E_F,\\; E_F=\\frac{\\hbar^2}{2m}(3\\pi^2n)^{2/3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1563", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "10-plasma-physics/inertial-and-laser-plasmas/inertial-confinement-fusion", "name": "Fermi degeneracy and ICF fuel", "kind": "mechanism", "summary": "ICF compresses fuel on a low adiabat, keeping it near-degenerate to minimise compression work; the adiabat parameter is the ratio of fuel pressure to Fermi pressure.", "map": "\\alpha=P/P_{\\rm Fermi}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1564", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "Radiation and blackbody in laser plasmas", "kind": "shared object", "summary": "Radiation in hohlraums and hot plasmas is a Planck photon gas; indirect-drive ICF relies on x-ray bath near blackbody equilibrium and Stefan–Boltzmann scaling.", "map": "P=\\sigma T^4", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1565", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Plasmons and collective quanta", "kind": "shared object", "summary": "Langmuir waves quantize as plasmons in degenerate electron gases, with the same plasma frequency and Bohm–Pines RPA treatment as in metals; Bose statistics of phonon-like modes applies.", "map": "\\omega_p^2=\\frac{ne^2}{\\varepsilon_0 m}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1566", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Nonequilibrium stat mech and Vlasov kinetics", "kind": "shared object", "summary": "Plasma kinetics is nonequilibrium statistical mechanics of a long-range-interacting gas: the Vlasov equation is the collisionless limit of the BBGKY hierarchy, with Fokker–Planck collisions as the weak-scattering closure.", "map": "\\partial_t f+\\mathbf v\\cdot\\nabla f+\\tfrac{q}{m}(\\mathbf E+\\mathbf v\\times\\mathbf B)\\cdot\\partial_{\\mathbf v}f=C[f]", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1567", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/driven-systems-and-nonequilibrium-steady-states", "b": "10-plasma-physics/magnetic-confinement-fusion/turbulent-transport-and-gyrokinetics", "name": "Avalanches and critical gradient transport", "kind": "analogy", "summary": "Profile stiffness above critical gradients and avalanche-like transport events in tokamaks are compared with sandpile SOC models; zonal flows resemble self-regulating shear.", "map": "", "breaks": "Gyrokinetic turbulence has specific linear thresholds and fluid physics beyond sandpile rules.", "confidence": "current research", "strength": 2}
{"id": "C1568", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/driven-systems-and-nonequilibrium-steady-states", "b": "10-plasma-physics/magnetohydrodynamics/mhd-turbulence", "name": "Nonequilibrium cascades as driven steady states", "kind": "analogy", "summary": "MHD turbulence is a driven dissipative steady state with a constant flux cascade through scales, comparable to scale-invariant nonequilibrium steady states studied in KPZ and driven-diffusive systems.", "map": "", "breaks": "Energy cascades have no detailed-balance structure but also lack the exact stochastic-model solvability.", "confidence": "proposed", "strength": 1}
{"id": "C1569", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/driven-systems-and-nonequilibrium-steady-states", "b": "10-plasma-physics/space-and-astrophysical-plasmas/magnetospheres-and-space-weather", "name": "Self-organized criticality in substorms and flares", "kind": "analogy", "summary": "Avalanche models of self-organized criticality have been applied to solar flares and magnetospheric substorms, whose power-law event statistics resemble sandpile avalanches.", "map": "", "breaks": "Flare and substorm driving and loading are not clearly critical; MHD-based explanations compete.", "confidence": "current research", "strength": 2}
{"id": "C1570", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "10-plasma-physics/magnetic-confinement-fusion/tokamaks", "name": "Collisional transport and neoclassical theory", "kind": "method transfer", "summary": "Collisional transport coefficients in magnetized plasma follow from kinetic theory via Chapman–Enskog/Braginskii closures; neoclassical theory adds trapped-particle effects from toroidal geometry to random-walk diffusion estimates.", "map": "D\\sim\\nu\\,\\Delta x^2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1571", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "10-plasma-physics/plasma-fundamentals", "name": "Plasma fundamentals and Boltzmann kinetics", "kind": "shared object", "summary": "Plasma collision operators (Landau, Lenard–Balescu, Fokker–Planck) are the Coulomb-interaction versions of the Boltzmann collision integral, with a Coulomb logarithm cutoff set by Debye screening.", "map": "\\ln\\Lambda=\\ln(\\lambda_D/b_{\\min})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1572", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Boltzmann equation to Vlasov equation", "kind": "mechanism", "summary": "Vlasov is the Boltzmann equation with the collision term dropped and a self-consistent mean field added; the H-theorem fails for it, yet Landau damping gives effective irreversibility via phase mixing.", "map": "C[f]\\to 0,\\; \\mathbf F\\to q(\\mathbf E[f]+\\mathbf v\\times\\mathbf B[f])", "breaks": "Vlasov is time-reversible and conserves all Casimirs; damping is phase mixing, not entropy production.", "confidence": "established", "strength": 3}
{"id": "C1573", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Landau damping and the H-theorem", "kind": "analogy", "summary": "Both explain relaxation of a distribution function; Boltzmann's is entropy-producing via collisions, Landau's is collisionless via resonant wave-particle energy exchange and phase mixing.", "map": "", "breaks": "Landau damping conserves entropy and is reversible in principle; collisional H-theorem increases entropy.", "confidence": "established", "strength": 2}
{"id": "C1574", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "10-plasma-physics/space-and-astrophysical-plasmas/solar-wind-and-heliosphere", "name": "Collisionless solar wind and Knudsen number", "kind": "shared object", "summary": "Solar wind has large Knudsen number, so Boltzmann-equation exospheric models predict non-Maxwellian electron and ion distributions and heat flux, the origin of Parker-like kinetic closures beyond fluid theory.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1575", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation", "b": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "name": "X-ray Thomson scattering and FDT", "kind": "method transfer", "summary": "XRTS measures the dynamic structure factor of warm dense matter, which by the fluctuation–dissipation theorem encodes density response, temperature (detailed balance) and collective modes.", "map": "S(k,\\omega)=\\frac{-\\hbar}{\\pi n}\\frac{\\mathrm{Im}\\,\\chi}{1-e^{-\\hbar\\omega/k_BT}}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1576", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Conductivity, Kubo formula and Spitzer", "kind": "method transfer", "summary": "Plasma resistivity and transport coefficients can be derived from Kubo formulas, with Spitzer resistivity as the kinetic limit; Onsager symmetry constrains cross-coefficients such as thermoelectric terms.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1577", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Dielectric response, FDT and Landau damping", "kind": "identity", "summary": "The plasma dielectric function is a linear response function; its imaginary part gives Landau damping, and the FDT links it to thermal density fluctuations (dynamic structure factor, collective scattering).", "map": "S(k,\\omega)=\\frac{2k_BT}{\\omega}\\,\\mathrm{Im}\\,\\chi(k,\\omega)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1578", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "10-plasma-physics/magnetic-confinement-fusion/turbulent-transport-and-gyrokinetics", "name": "Random-walk transport and Fokker–Planck", "kind": "method transfer", "summary": "Diffusive transport estimates, Fokker–Planck collision operators and quasilinear theory in plasmas treat turbulent or collisional scattering as a random walk in space or velocity.", "map": "\\partial_t f=\\partial_v\\left(D\\,\\partial_v f\\right)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1579", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Magnetic field-line and particle diffusion", "kind": "mechanism", "summary": "Charged-particle scattering by magnetic fluctuations gives pitch-angle diffusion and cosmic-ray transport; stochastic field lines yield Rechester–Rosenbluth diffusion, a random-walk with correlation length.", "map": "D_{RR}=D_{FL}\\,v_\\parallel", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1580", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks", "name": "Stochastic acceleration and diffusive shock acceleration", "kind": "mechanism", "summary": "Fermi acceleration is a random-walk process in momentum and space; diffusive shock acceleration solves a diffusion–advection equation yielding a universal power-law spectrum.", "map": "f(p)\\propto p^{-3r/(r-1)}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1581", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-thermodynamics-and-fluctuation-theorems", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Entropy production in collisionless plasma", "kind": "analogy", "summary": "Entropy in weakly collisional plasma turbulence is cascaded to fine velocity-space scales (phase-space cascade) and dissipated by collisions, tied to Gibbs-entropy and fluctuation-theorem language.", "map": "", "breaks": "Stochastic thermodynamics assumes Markovian baths; the plasma entropy cascade is deterministic Vlasov phase mixing.", "confidence": "current research", "strength": 2}
{"id": "C1582", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory", "b": "10-plasma-physics/magnetohydrodynamics/dynamo-theory", "name": "Dynamo onset as a bifurcation", "kind": "analogy", "summary": "The dynamo transition at critical magnetic Reynolds number resembles a continuous phase transition with a control parameter and symmetry-breaking order parameter (field amplitude), with saturation by Lorentz-force feedback.", "map": "", "breaks": "No equilibrium free energy; the field has no thermal fluctuation-driven criticality.", "confidence": "current research", "strength": 1}
{"id": "C1583", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Debye screening as mean-field theory", "kind": "mechanism", "summary": "Poisson–Boltzmann is a self-consistent mean-field theory, exact as the number of particles in a Debye sphere grows (plasma parameter large), analogous to the Ginzburg criterion.", "map": "", "breaks": "Fails at strong coupling where Debye sphere holds few particles.", "confidence": "established", "strength": 2}
{"id": "C1584", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Landau theory of instability onset", "kind": "analogy", "summary": "Plasma instabilities near threshold (two-stream, drift waves) show saturation amplitude equations resembling Landau–Ginzburg normal forms, with growth rate crossing zero like a control parameter.", "map": "\\partial_t A=\\gamma A-\\beta|A|^2A", "breaks": "Instabilities are nonequilibrium bifurcations without a free-energy functional.", "confidence": "established", "strength": 2}
{"id": "C1585", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/renormalization-group", "b": "10-plasma-physics/magnetohydrodynamics/mhd-turbulence", "name": "RG and turbulence scaling", "kind": "method transfer", "summary": "Dynamic renormalization group was applied to stirred fluid and MHD turbulence (Forster–Nelson–Stephen, Fournier–Frisch), treating the cascade via scale elimination and fixed points.", "map": "", "breaks": "Results are scheme-dependent and do not reproduce intermittency or anisotropic critical balance reliably.", "confidence": "current research", "strength": 2}
{"id": "C1586", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/topological-phase-transitions-bkt", "b": "10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas", "name": "2D Coulomb systems and melting", "kind": "analogy", "summary": "Two-dimensional dusty-plasma crystals melt via defect unbinding, discussed in KTHNY theory, a BKT-type two-step transition via dislocation and disclination unbinding.", "map": "", "breaks": "Dusty plasmas are driven, dissipative and finite-size, with non-reciprocal forces.", "confidence": "current research", "strength": 2}
{"id": "C1855", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "name": "Atomic structure in dense plasma: IPD and opacity", "kind": "mechanism", "summary": "A dense plasma shifts and broadens atomic levels and lowers ionization thresholds (ionization-potential depression, pressure ionization). XFEL measurements disagreed with the standard Stewart–Pyatt model, and iron opacities measured on the Z machine exceed atomic-model predictions. Both remain unresolved tests of atomic structure in plasmas.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1856", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "10-plasma-physics/magnetic-confinement-fusion/tokamaks", "name": "Atomic spectroscopy as tokamak diagnostics (MSE, CXRS)", "kind": "method transfer", "summary": "Tokamaks read their internal state through atomic physics. The motional Stark effect on neutral-beam H-alpha light gives the current (q) profile. Charge-exchange recombination spectroscopy gives ion temperature and rotation. Impurity line radiation (e.g. tungsten) sets the core radiation losses.", "map": "\\mathbf E_L=\\mathbf v_b\\times\\mathbf B\\Rightarrow\\text{Stark-split }H_\\alpha\\text{ polarization}\\to B_\\theta/B_\\phi\\to q(r)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1857", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas", "name": "Rydberg gases and ultracold plasmas interconvert", "kind": "mechanism", "summary": "Dense Rydberg gases avalanche-ionize on their own into ultracold plasmas. Ultracold plasmas in turn recombine, by three-body recombination, into high-n Rydberg states. So Rydberg-atom structure (how size and binding scale with n) controls both how the plasma forms and how it decays.", "map": "\\nu_{3b}\\propto n_e^2T_e^{-9/2},\\ \\ r_n\\propto n^2a_0,\\ E_n=-\\frac{R_\\infty hc}{n^2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1858", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Antihydrogen: trap plasmas meet precision spectroscopy", "kind": "shared object", "summary": "Antihydrogen is made by merging antiproton and positron plasmas in Penning–Malmberg traps, using rotating-wall compression and evaporative and sympathetic cooling. It is then probed by 1S–2S and hyperfine spectroscopy and compared with hydrogen to test CPT symmetry.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1859", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "name": "Partially degenerate electrons in warm dense matter", "kind": "shared object", "summary": "Warm dense matter sits at θ=k_BT/E_F≈1, where electrons are neither classical nor fully degenerate. The finite-temperature Fermi-gas thermodynamics measured in ultracold Fermi gases sets its pressure. Strong coupling (Γ≈1) leaves no small parameter.", "map": "\\theta=\\frac{k_BT}{E_F},\\ E_F=\\frac{\\hbar^2}{2m}(3\\pi^2n)^{2/3},\\ \\Gamma\\sim1", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1860", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "10-plasma-physics/inertial-and-laser-plasmas/inertial-confinement-fusion", "name": "ICF adiabat: pressure over Fermi-degenerate pressure", "kind": "mechanism", "summary": "ICF designs keep the cold fuel close to a Fermi-degenerate state, because the work needed to compress it scales with degeneracy pressure. The 'adiabat' α=P/P_F measures the entropy that shocks add, and it limits the achievable areal density and gain.", "map": "\\alpha=\\frac{P}{P_F},\\ P_F=\\tfrac25nE_F\\propto\\rho^{5/3}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1861", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "10-plasma-physics/magnetohydrodynamics/magnetic-reconnection", "name": "Quantized-vortex reconnection vs magnetic reconnection", "kind": "analogy", "summary": "Superfluid vortex lines are frozen into the flow (Kelvin's theorem), as magnetic field lines are in a near-ideal plasma (Alfvén's theorem). Both can change topology only by reconnecting in a thin non-ideal region. Vortex reconnections in BECs and helium show X-point geometry and a universal separation law δ∝(t−t₀)^{1/2}.", "map": "\\oint\\mathbf v_s\\cdot d\\mathbf l=\\kappa\\,(h/m)\\ \\leftrightarrow\\ \\int\\mathbf B\\cdot d\\mathbf S=\\text{const (frozen-in)}", "breaks": "Superfluid circulation is quantized, and reconnection happens through the healing-length core of Gross–Pitaevskii dynamics. Magnetic flux is not quantized, and reconnection rates are set by resistivity, Hall/kinetic physics and plasmoids.", "confidence": "established", "strength": 1}
{"id": "C1862", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Debye screening → Thomas–Fermi screening for T≪T_F", "kind": "identity", "summary": "Linear-response screening of a test charge gives the Debye length in a classical plasma and the Thomas–Fermi length in a degenerate electron gas. The degeneracy parameter controls the crossover and separates classical from quantum plasmas (metals, white dwarfs, compressed fuel).", "map": "\\lambda_D^{-2}=\\frac{ne^2}{\\epsilon_0k_BT}\\ \\to\\ \\lambda_{TF}^{-2}=\\frac{3ne^2}{2\\epsilon_0E_F}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1863", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Landau damping of condensate collective modes", "kind": "mechanism", "summary": "At finite temperature, collective oscillations of a trapped Bose gas decay by Landau damping: energy passes resonantly to thermal Bogoliubov excitations at a rate set by the slope of their distribution. This is the same resonance logic as Landau damping of plasma waves.", "map": "E_k-E_i=\\hbar\\omega,\\ \\gamma\\propto\\partial f/\\partial E\\ \\leftrightarrow\\ v=\\omega/k,\\ \\gamma\\propto\\partial f_0/\\partial v", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1864", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Nonlinear Schrödinger: BEC solitons and Langmuir collapse", "kind": "identity", "summary": "The Gross–Pitaevskii equation and the envelope equation for Langmuir waves (Zakharov, with the ponderomotive density cavity) are both cubic nonlinear Schrödinger equations. Both show dark and bright solitons, modulational instability and collapse above a critical norm: the attractive-BEC 'bosenova' corresponds to Langmuir collapse and to laser self-focusing.", "map": "i\\hbar\\partial_t\\psi=\\left(-\\frac{\\hbar^2}{2m}\\nabla^2+g|\\psi|^2\\right)\\psi\\ \\leftrightarrow\\ i\\partial_tE+\\frac{3v_{th}^2}{2\\omega_p}\\nabla^2E=\\frac{\\omega_p}{2}\\frac{\\delta n}{n_0}E", "breaks": "In a plasma, ψ is a classical wave envelope and the nonlinearity comes from the slow ion-acoustic density response, which is instantaneous only in the subsonic limit. In a BEC, ψ is the macroscopic wavefunction with contact interactions.", "confidence": "established", "strength": 2}
{"id": "C1865", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/laser-cooling-and-trapping", "b": "10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas", "name": "Ultracold neutral plasmas from laser-cooled atoms", "kind": "method transfer", "summary": "Photoionizing laser-cooled atoms just above threshold makes neutral plasmas with electron temperatures of a few kelvin and sub-kelvin ions, reaching Γ>1. Disorder-induced heating caps ion coupling near Γ≈2–3; laser-cooling the plasma ions themselves pushes it higher.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1866", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/laser-cooling-and-trapping", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Ioffe–Pritchard atom traps borrow mirror-machine physics", "kind": "historical", "summary": "Magnetic traps hold weak-field-seeking atoms whose magnetic moment adiabatically follows B, just as a mirror holds gyrating particles through μ. The Ioffe–Pritchard trap took the Ioffe-bar minimum-B configuration from mirror fusion to remove the field zero, where Majorana spin flips (non-adiabatic loss) occur.", "map": "U=m_Fg_F\\mu_B|\\mathbf B|\\ \\leftrightarrow\\ U_{eff}=\\mu|\\mathbf B|;\\ \\text{adiabatic if }\\omega_L\\gg|d\\hat{\\mathbf b}/dt|", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1867", "a": "04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Plasma echo ↔ spin echo: phase mixing vs decoherence", "kind": "analogy", "summary": "Landau damping is phase mixing of free-streaming particles and can be undone, which produces plasma echoes, just as a Hahn echo reverses inhomogeneous dephasing (T_2^*) of spins. Collisions play the role of true decoherence (T_2), which no echo can recover.", "map": "\\text{plasma echo at }t=\\frac{k_2\\tau}{k_2-k_1}\\ \\leftrightarrow\\ \\text{Hahn echo at }t=2\\tau", "breaks": "Plasma phase mixing happens in a classical velocity continuum with no entanglement. Quantum decoherence needs system–environment entanglement and selects pointer states, which have no plasma counterpart.", "confidence": "established", "strength": 2}
{"id": "C1868", "a": "04-quantum-physics/foundations-of-quantum-mechanics/measurement-problem-and-interpretations", "b": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "name": "Bohm potential in quantum hydrodynamics of dense plasma", "kind": "method transfer", "summary": "The Madelung (de Broglie–Bohm) rewriting of the Schrödinger equation supplies the 'Bohm potential' term used in quantum hydrodynamic models of dense and warm dense plasmas. Its validity and prefactor beyond the long-wavelength limit are disputed.", "map": "Q=-\\frac{\\hbar^2}{2m}\\frac{\\nabla^2\\sqrt n}{\\sqrt n}", "breaks": "", "confidence": "current research", "strength": 1}
{"id": "C1869", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/floquet-systems-and-time-crystals", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "High-frequency Floquet expansion gives ponderomotive force", "kind": "method transfer", "summary": "The Kapitza/Magnus high-frequency expansion used for Floquet engineering gives, at leading order, the ponderomotive Hamiltonian of laser–plasma theory. Both expansions fail near resonances, where driven heating starts.", "map": "H_{eff}=\\frac{p^2}{2m}+V(x)+\\frac{q^2E_0(x)^2}{4m\\omega^2}+\\dots", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1870", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/non-hermitian-physics", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Instability onset as PT breaking at a Krein collision", "kind": "identity", "summary": "Linearized ideal plasma and fluid systems have a PT-symmetric (G-Hamiltonian) structure. Two-stream and Kelvin–Helmholtz instabilities appear when a positive-action and a negative-action (negative-energy) mode collide at an exceptional point. This is the same PT-breaking transition studied in non-Hermitian photonics.", "map": "\\omega\\in\\mathbb R\\ \\text{(PT unbroken)}\\to(\\omega,\\omega^*)\\ \\text{at EP: Krein collision of }\\pm\\text{-action modes}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1871", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Chirikov overlap: mirror traps to quantum kicked rotor", "kind": "historical", "summary": "Chirikov devised his resonance-overlap criterion (1959) for the breakdown of adiabatic confinement in magnetic mirror traps. It led to the standard map. The map's quantum version, the kicked rotor, shows dynamical localization (realized with cold atoms) and became a founding model of quantum chaos.", "map": "p'=p+K\\sin\\theta,\\ \\theta'=\\theta+p';\\ \\text{global chaos for }K\\gtrsim0.97", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1872", "a": "04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Quantum algorithms for Vlasov and plasma-wave simulation", "kind": "method transfer", "summary": "Linear plasma problems (linearized Vlasov, cold-plasma waves) can be cast as Hamiltonian simulation on qubits, and nonlinear Vlasov dynamics through Koopman–von Neumann or Carleman embeddings. It is still open whether an end-to-end speed-up survives state preparation, readout and nonlinearity.", "map": "", "breaks": "", "confidence": "current research", "strength": 1}
{"id": "C1873", "a": "04-quantum-physics/quantum-information-and-computation/superconducting-qubits", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Transmon frequency = Josephson plasma frequency", "kind": "analogy", "summary": "A transmon's transition frequency is set by the Josephson plasma frequency, named by analogy with Langmuir oscillation. The Josephson (kinetic) inductance resonates with the junction capacitance, as electron inertia (kinetic inductance m/ne²) resonates with the space-charge restoring force to give ω_p.", "map": "\\omega_J=\\frac{\\sqrt{8E_JE_C}}{\\hbar}=\\sqrt{\\frac{2eI_c}{\\hbar C}}\\ \\leftrightarrow\\ \\omega_p=\\sqrt{\\frac{ne^2}{\\epsilon_0m}}", "breaks": "A single junction is a one-degree-of-freedom anharmonic LC oscillator, with no Debye screening and no many-particle collective dynamics. Only in bulk layered superconductors is the Josephson plasma resonance a true collective mode.", "confidence": "established", "strength": 1}
{"id": "C1874", "a": "04-quantum-physics/quantum-information-and-computation/trapped-ion-and-neutral-atom-qubits", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "Paul-trap pseudopotential = ponderomotive potential", "kind": "identity", "summary": "The time-averaged force that holds an ion in an RF Paul trap is the same ponderomotive force that pushes electrons out of an intense laser focus (channel formation, wakefield bubbles). Ion micromotion is the electron's quiver motion.", "map": "\\Phi_{pond}=\\frac{q^2E_0^2}{4m\\omega^2};\\ \\text{Paul: }E_0\\propto r\\Rightarrow\\omega_{sec}=\\frac{qV_0}{\\sqrt2\\,m\\Omega r_0^2}", "breaks": "For a_0\\gtrsim1 the laser case becomes relativistic (cycle-averaged \\gamma), which never happens in ion traps. A Paul trap also needs Mathieu stability (q\\lesssim0.9), a condition with no counterpart in a laser focus.", "confidence": "established", "strength": 3}
{"id": "C1875", "a": "04-quantum-physics/quantum-information-and-computation/trapped-ion-and-neutral-atom-qubits", "b": "10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas", "name": "Laser-cooled ion crystals are strongly coupled plasmas", "kind": "shared object", "summary": "Laser-cooled ions in Paul and Penning traps reach Γ≫175 and form Coulomb crystals. These are one-component plasmas described by the same coupling parameter and Wigner–Seitz radius as dusty-plasma crystals. Their phonon modes are the quantum bus for trapped-ion gates, and 2D Penning-trap crystals are used as Ising simulators.", "map": "\\Gamma=\\frac{q^2}{4\\pi\\epsilon_0ak_BT}\\gtrsim175\\ \\text{(OCP crystal)},\\ a=(3/4\\pi n)^{1/3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1876", "a": "04-quantum-physics/quantum-information-and-computation/trapped-ion-and-neutral-atom-qubits", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Penning trap: cyclotron and E×B magnetron motion", "kind": "shared object", "summary": "Penning traps hold charges using the drifts of plasma single-particle theory: the magnetron mode is the E×B drift in the trap's radial field. The same geometry (the Malmberg–Penning trap) holds non-neutral plasmas and the rotating 2D ion crystals used for quantum simulation.", "map": "\\omega_\\pm=\\frac{\\omega_c}{2}\\pm\\sqrt{\\frac{\\omega_c^2}{4}-\\frac{\\omega_z^2}{2}},\\ \\omega_-\\approx\\frac{\\omega_z^2}{2\\omega_c}=\\frac{E_r}{rB}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1877", "a": "04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin", "b": "10-plasma-physics/magnetic-confinement-fusion/burning-plasmas-and-iter", "name": "Spin-polarized D–T fuel raises the fusion cross section", "kind": "mechanism", "summary": "D–T fusion goes mainly through the J=3/2⁺ resonance of ⁵He. Aligning the deuteron (spin 1) and triton (spin ½) spins puts every pair into J=3/2 and raises the cross section by a factor 3/2. Whether the polarization survives in a reactor plasma is still under study.", "map": "\\sigma_{pol}=\\tfrac32\\,\\sigma_{unpol}\\quad(\\text{statistical weight of }J=3/2:\\ 4/6)", "breaks": "", "confidence": "current research", "strength": 1}
{"id": "C1878", "a": "04-quantum-physics/quantum-mechanics-core/approximation-methods", "b": "10-plasma-physics/inertial-and-laser-plasmas/plasma-wakefield-acceleration", "name": "Tunnel ionization (WKB/ADK) and ionization injection", "kind": "method transfer", "summary": "Quasi-static WKB tunnelling rates (Keldysh/ADK) decide where an intense pulse ionizes a gas. Wakefield accelerators use the steep field threshold of inner-shell tunnel ionization to inject electrons at a chosen phase of the wake (ionization injection).", "map": "\\gamma_K=\\frac{\\omega\\sqrt{2m_eI_p}}{eE},\\quad w\\propto\\exp\\left[-\\frac{4\\sqrt{2m_e}\\,I_p^{3/2}}{3\\hbar eE}\\right]", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1879", "a": "04-quantum-physics/quantum-mechanics-core/approximation-methods", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "MHD energy principle = Rayleigh–Ritz variational principle", "kind": "identity", "summary": "Static ideal MHD has a self-adjoint force operator, so ω² is real, as for a Hermitian spectrum. Stability follows from minimizing δW over trial displacements, the same variational principle that bounds quantum ground-state energies. Equilibrium flows break self-adjointness (Frieman–Rotenberg).", "map": "\\rho\\omega^2\\boldsymbol\\xi=-\\mathbf F(\\boldsymbol\\xi),\\ \\omega^2_{\\min}=\\min_\\xi\\frac{\\delta W}{K}\\ \\leftrightarrow\\ E_0=\\min_\\psi\\frac{\\langle\\psi|H|\\psi\\rangle}{\\langle\\psi|\\psi\\rangle}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1880", "a": "04-quantum-physics/quantum-mechanics-core/approximation-methods", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Mode conversion ↔ Landau–Zener transitions", "kind": "identity", "summary": "Waves in inhomogeneous plasma are traced with WKB/eikonal rays, where cutoffs act as turning points. Where two dispersion branches nearly cross, linear mode conversion reduces to a 2×2 Landau–Zener problem along the ray. It gives the same exponential transmission law, which is used to design RF heating schemes.", "map": "T=e^{-2\\pi\\eta}\\ \\text{(mode conversion)}\\ \\leftrightarrow\\ P_{LZ}=e^{-2\\pi\\Delta^2/\\hbar\\alpha}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1881", "a": "04-quantum-physics/quantum-mechanics-core/approximation-methods", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Adiabatic invariant μ ↔ conserved quantum number", "kind": "identity", "summary": "The magnetic moment μ that makes mirrors work is the gyration action, the classical counterpart of the quantum adiabatic theorem. Under slow change the Landau-level index is conserved, and μ=(n+1/2)|q|ħ/m. Ehrenfest's adiabatic hypothesis made this exact link in the old quantum theory.", "map": "\\mu=\\frac{mv_\\perp^2}{2B}=\\frac{|q|\\hbar}{m}(n+\\tfrac12),\\quad J_\\perp=\\oint p_\\perp dq=2\\pi\\hbar(n+\\tfrac12)", "breaks": "In fusion plasmas n\\sim10^7 for 10 keV electrons at 5 T, so only the classical invariant matters there. Classical μ is conserved only asymptotically (exponentially small breaking), while the quantum theorem needs a spectral gap.", "confidence": "established", "strength": 3}
{"id": "C1882", "a": "04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems", "b": "10-plasma-physics/magnetic-confinement-fusion/burning-plasmas-and-iter", "name": "Gamow tunnelling sets the fusion reactivity", "kind": "mechanism", "summary": "Fusion at 10–20 keV works only because nuclei tunnel through the Coulomb barrier. The barrier-penetration factor times the Maxwellian tail gives the Gamow peak. That peak fixes ⟨σv⟩, the best D–T temperature and the Lawson triple product.", "map": "\\sigma(E)=\\frac{S(E)}{E}e^{-\\sqrt{E_G/E}},\\ E_G=2\\mu c^2(\\pi\\alpha Z_1Z_2)^2,\\ E_0=(E_G(k_BT)^2/4)^{1/3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1883", "a": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Chern numbers of magnetized plasma waves; edge modes", "kind": "method transfer", "summary": "Band-topology ideas built on Berry curvature have been applied to the cold magnetized-plasma dielectric. Its wave bands carry nonzero Chern numbers, and bulk–edge correspondence predicts one-way, backscatter-immune edge waves at plasma boundaries. Experimental confirmation is still pending.", "map": "C_n=\\frac{1}{2\\pi}\\int\\mathcal F_n\\,d^2k\\neq0\\ \\Rightarrow\\ \\text{unidirectional boundary modes}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1884", "a": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Gyrophase anholonomy: geometric phase of gyration", "kind": "identity", "summary": "In guiding-centre theory, the gyrophase picks up a geometric shift when the field direction is carried around a loop (Littlejohn's gyrogauge connection). This is the classical Hannay angle; its quantum counterpart is the Berry phase of a Landau-level state.", "map": "\\Delta\\theta_g=\\oint\\mathbf R\\cdot d\\mathbf x,\\ \\mathbf R=(\\nabla\\hat e_1)\\cdot\\hat e_2\\ \\leftrightarrow\\ \\gamma_B=i\\oint\\langle n|\\nabla n\\rangle\\cdot d\\mathbf R", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1885", "a": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "b": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "name": "Path-integral Monte Carlo for warm dense matter", "kind": "method transfer", "summary": "Imaginary-time path integrals map quantum electrons and ions onto classical ring polymers. This gives first-principles equations of state and the warm-dense uniform electron gas used to build finite-temperature DFT functionals. The fermion sign problem limits the method at low θ and high density.", "map": "Z=\\mathrm{Tr}\\,e^{-\\beta H}=\\int\\mathcal Dx\\,e^{-S_E[x]/\\hbar}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1886", "a": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "b": "10-plasma-physics/magnetic-confinement-fusion/turbulent-transport-and-gyrokinetics", "name": "Wigner–Weyl wave kinetics of drift waves and zonal flows", "kind": "method transfer", "summary": "Phase-space quantum methods (Weyl symbols, Moyal brackets) have been brought in to treat drift-wave turbulence as a gas of 'driftons' interacting with zonal flows. This extends the ray (geometric-optics) wave-kinetic equation so that it captures zonal-flow stability and pattern formation.", "map": "\\partial_tW=\\{\\!\\{\\mathcal H,W\\}\\!\\}\\ \\to\\ \\{\\mathcal H,W\\}\\ \\text{(ray limit)}", "breaks": "", "confidence": "current research", "strength": 1}
{"id": "C1887", "a": "04-quantum-physics/quantum-mechanics-core/postulates-and-formalism", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Wigner–Moyal equation reduces to Vlasov as ħ→0", "kind": "identity", "summary": "Wigner-transforming the von Neumann equation for a mean-field (Hartree) density matrix gives the Wigner–Poisson equation, which becomes the Vlasov equation as ħ→0. Quantum plasma kinetics, quantum Landau damping and the quantum Lenard–Balescu operator are all built on this map.", "map": "\\partial_tW+\\frac{\\mathbf p}{m}\\cdot\\nabla W-\\nabla V\\cdot\\nabla_{\\mathbf p}W=O(\\hbar^2\\nabla^3V\\,\\partial_p^3W)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1888", "a": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "b": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "name": "X-ray Thomson scattering measures S(k,ω)", "kind": "method transfer", "summary": "X-ray Thomson scattering applies first-Born scattering theory to dense plasmas: the measured spectrum is the dynamic structure factor. The Chihara decomposition splits it into bound, free and screening-cloud parts. The scattering parameter decides between the collective (plasmon) and non-collective regimes, and the fit gives T_e, n_e and ionization.", "map": "\\frac{d^2\\sigma}{d\\Omega\\,d\\omega}=\\sigma_T\\frac{k_s}{k_i}S(\\mathbf k,\\omega),\\quad\\alpha=\\frac{1}{k\\lambda_s}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1889", "a": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "b": "10-plasma-physics/low-temperature-and-applied-plasmas/plasma-discharges-and-processing", "name": "Ramsauer–Townsend minimum shapes argon discharges", "kind": "mechanism", "summary": "Ar, Kr and Xe are nearly transparent to electrons of ~0.2–0.7 eV because the s-wave phase shift passes through π. This minimum in the momentum-transfer cross section distorts electron energy distributions, mobility and breakdown in discharges. Partial-wave cross sections are fed into the Boltzmann solvers used for plasma processing.", "map": "\\sigma=\\frac{4\\pi}{k^2}\\sum_l(2l+1)\\sin^2\\delta_l,\\quad\\delta_0(E_{RT})\\approx\\pi\\Rightarrow\\sigma_{min}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1890", "a": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Coulomb logarithm: Rutherford cross section, quantum cutoff", "kind": "mechanism", "summary": "Plasma collision operators (Landau, Lenard–Balescu, Fokker–Planck) integrate the Rutherford cross section over impact parameters. Debye screening cuts the integral off at large distance. At short distance the cutoff is the larger of the classical closest-approach distance and the de Broglie wavelength, and for hot electrons (T_e≳10Z² eV) that is the quantum one.", "map": "\\ln\\Lambda=\\ln\\frac{\\lambda_D}{b_{min}},\\ b_{min}=\\max\\left(\\frac{q_1q_2}{4\\pi\\epsilon_0\\mu v^2},\\frac{\\hbar}{2\\mu v}\\right)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1891", "a": "04-quantum-physics/quantum-optics/cavity-optomechanics", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "Brillouin light–sound coupling: optomechanics vs SBS", "kind": "analogy", "summary": "In stimulated Brillouin scattering, a laser decays into scattered light plus an ion-acoustic wave driven by the ponderomotive force. This is the plasma counterpart of the radiation-pressure or electrostrictive coupling of light to a mechanical mode in Brillouin optomechanics. Both obey the same phase-matched three-wave coupled-mode equations.", "map": "H_{int}=\\hbar g_0a^\\dagger a(b+b^\\dagger)\\ \\leftrightarrow\\ \\omega_0=\\omega_s+\\omega_{ia},\\ \\mathbf k_0=\\mathbf k_s+\\mathbf k_{ia}", "breaks": "Plasma SBS is classical, convective and broadband, with strongly Landau-damped acoustic modes, and it is a loss to suppress. Optomechanics uses discrete high-Q modes run near the quantum ground state.", "confidence": "established", "strength": 2}
{"id": "C1892", "a": "04-quantum-physics/quantum-optics/quantized-light-and-photon-statistics", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Photon in plasma: effective mass ħω_p; plasmons", "kind": "identity", "summary": "Transverse waves in a plasma obey ω²=ω_p²+c²k², a massive Klein–Gordon dispersion. So photons in a plasma act as quasiparticles of mass ħω_p/c², which lets them decay into neutrino pairs in stars. Quantized longitudinal Langmuir oscillations are plasmons.", "map": "\\omega^2=\\omega_p^2+c^2k^2\\ \\leftrightarrow\\ E^2=m_\\gamma^2c^4+p^2c^2,\\ m_\\gamma=\\hbar\\omega_p/c^2", "breaks": "The mass is a medium effect tied to the plasma rest frame, and longitudinal and transverse modes differ. No vacuum gauge symmetry is broken; this is the analogy behind the Anderson–Higgs mechanism, not an identity with it.", "confidence": "established", "strength": 2}
{"id": "C1893", "a": "04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "Plasma parametric decay ↔ parametric down-conversion", "kind": "analogy", "summary": "Stimulated Raman scattering and two-plasmon decay split a pump photon into two daughter waves that match energy and momentum. This is the classical, stimulated limit of the three-wave Hamiltonian that produces squeezed vacuum by parametric down-conversion. Plasma Raman amplifiers use the same gain.", "map": "H=i\\hbar\\kappa(a_p\\,b^\\dagger c^\\dagger-\\text{h.c.}),\\quad\\omega_0=\\omega_s+\\omega_{pe}\\ \\text{(SRS)}", "breaks": "The plasma daughters (Langmuir waves) are heavily damped and grow from thermal noise, so quantum correlations and squeezing are destroyed. Down-conversion uses a nearly lossless χ^(2) crystal starting from vacuum.", "confidence": "established", "strength": 2}
{"id": "C2092", "a": "05-relativity-and-gravitation/black-holes/black-hole-imaging-and-astrophysical-black-holes", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "GRMHD accretion models behind EHT images", "kind": "method transfer", "summary": "Ideal MHD in Kerr spacetime, with MRI-driven disk turbulence and ray-traced synchrotron emission, supplies the model libraries used to score EHT images of M87* and Sgr A*. Polarimetry favours magnetically arrested disks (MAD) over weakly magnetized (SANE) flows.", "map": "\\nabla_\\mu(\\rho u^\\mu)=0,\\ \\nabla_\\mu T^{\\mu\\nu}=0,\\ \\nabla_\\mu{}^*F^{\\mu\\nu}=0,\\ \\phi_{\\rm MAD}=\\Phi_B/\\sqrt{\\dot M r_g^2c}\\approx50\\ (\\text{Gaussian})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2093", "a": "05-relativity-and-gravitation/black-holes/black-hole-imaging-and-astrophysical-black-holes", "b": "10-plasma-physics/magnetohydrodynamics/magnetic-reconnection", "name": "Reconnection flares and plasmoids near horizons", "kind": "mechanism", "summary": "Near-infrared and X-ray flares of Sgr A*, and the orbiting hot spots seen by GRAVITY, are modelled as plasmoids from reconnecting equatorial current sheets during MAD flux eruptions. Electrons accelerated by the reconnection supply the emission.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2094", "a": "05-relativity-and-gravitation/black-holes/black-hole-imaging-and-astrophysical-black-holes", "b": "10-plasma-physics/magnetohydrodynamics/mhd-turbulence", "name": "Interstellar plasma turbulence blurs Sgr A*", "kind": "shared object", "summary": "The image of Sgr A* is broadened by diffractive and refractive scattering in the turbulent ionized interstellar medium, whose Kolmogorov-like density spectrum is the footprint of the MHD cascade. EHT imaging must model the λ² scattering kernel and the refractive substructure.", "map": "\\theta_{\\rm scatt}\\propto\\lambda^2,\\ P_{\\delta n}(k)\\propto k^{-11/3}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2095", "a": "05-relativity-and-gravitation/black-holes/black-hole-imaging-and-astrophysical-black-holes", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Collisionless two-temperature accretion plasma", "kind": "mechanism", "summary": "Hot accretion flows onto Sgr A* and M87* are collisionless because Coulomb collision times exceed inflow times, so ions and electrons decouple. Electron heating by kinetic dissipation (Landau damping of the turbulent cascade, reconnection) sets the observed brightness; EHT models parametrize it with R_high.", "map": "\\frac{T_i}{T_e}=R_{\\rm high}\\frac{\\beta^2}{1+\\beta^2}+R_{\\rm low}\\frac{1}{1+\\beta^2},\\ t_{ei}\\gg t_{\\rm inflow}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2096", "a": "05-relativity-and-gravitation/black-holes/black-hole-imaging-and-astrophysical-black-holes", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Faraday rotation probes horizon-scale plasma", "kind": "mechanism", "summary": "Birefringence of the magnetized plasma rotates the EVPA by RM·λ². Rotation measures of M87* and Sgr A* constrain the accretion rate and field geometry, and internal Faraday rotation scrambles polarization in GRMHD models, which helps tell MAD from SANE flows.", "map": "\\Delta\\chi=\\mathrm{RM}\\,\\lambda^2,\\ \\mathrm{RM}=\\frac{e^3}{8\\pi^2\\epsilon_0m_e^2c^3}\\int n_eB_\\parallel\\,dl", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2097", "a": "05-relativity-and-gravitation/black-holes/black-hole-thermodynamics-and-hawking-radiation", "b": "10-plasma-physics/space-and-astrophysical-plasmas/solar-wind-and-heliosphere", "name": "Transonic winds and acoustic/Alfvén horizons", "kind": "analogy", "summary": "Parker's wind passes through a sonic critical point. This transonic flow is the time-reverse of Bondi accretion, whose sonic surface is an acoustic horizon in Unruh's analogue-gravity sense. The Alfvén critical surface, which Parker Solar Probe crossed in 2021, likewise cuts the outer wind off from the Sun for Alfvén waves.", "map": "v(r_c)=c_s,\\ r_c=\\frac{GM_\\odot}{2c_s^2}\\ \\leftrightarrow\\ |v|=c_s\\ \\text{horizon},\\ k_BT_H=\\frac{\\hbar}{2\\pi}\\left|\\partial_r(v-c_s)\\right|_{r_c}", "breaks": "The wind is an outflow, so its horizon is white-hole-like. Its critical point is set by gravity plus pressure rather than by geometry alone, and a 10⁶ K plasma swamps any analogue Hawking emission; only the classical causal structure carries over.", "confidence": "current research", "strength": 1}
{"id": "C2098", "a": "05-relativity-and-gravitation/black-holes/information-paradox", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "Accelerating plasma mirrors as evaporation analogues", "kind": "analogy", "summary": "Chen & Mourou proposed plasma mirrors, driven by a laser through graded-density plasma along tailored accelerating trajectories, as Fulling–Davies moving mirrors that emit Hawking-like thermal pairs. Correlations between partner photons could then test information loss; this is the AnaBHEL experiment.", "map": "\\text{mirror trajectory }z(t)\\to\\text{Bogoliubov }\\beta_{\\omega\\omega'}\\to\\text{thermal flux at }T=\\frac{\\hbar\\kappa}{2\\pi k_Bc}", "breaks": "A 1+1-dimensional moving mirror has no curvature, greybody factors or backreaction. The real plasma mirror is partly transparent and three-dimensional, and the signal is tiny against laser-plasma backgrounds, so it tests the kinematics of particle creation, not quantum gravity.", "confidence": "proposed", "strength": 2}
{"id": "C2099", "a": "05-relativity-and-gravitation/black-holes/schwarzschild-and-kerr-black-holes", "b": "10-plasma-physics/magnetic-confinement-fusion/tokamaks", "name": "Grad–Shafranov and the relativistic stream equation", "kind": "method transfer", "summary": "Axisymmetric equilibria reduce to one nonlinear elliptic PDE for the poloidal flux: the Grad–Shafranov equation in tokamaks, and its relativistic force-free generalization in Kerr magnetospheres, the Blandford–Znajek stream equation (a relative of the pulsar equation). The free functions Ω_F(ψ) and I(ψ) play the roles of p(ψ) and F(ψ).", "map": "\\Delta^*\\psi=-\\mu_0R^2\\frac{dp}{d\\psi}-F\\frac{dF}{d\\psi}\\ \\leftrightarrow\\ \\text{BZ stream eq. for }\\psi(r,\\theta)\\ \\text{with }\\Omega_F(\\psi),\\,I(\\psi)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2100", "a": "05-relativity-and-gravitation/black-holes/schwarzschild-and-kerr-black-holes", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "Blandford–Znajek: force-free extraction of Kerr spin", "kind": "mechanism", "summary": "A force-free (E·B=0) magnetosphere threading a spinning horizon carries outward Poynting flux paid for by the hole's rotational energy. It is the electromagnetic version of the Penrose process and the standard engine for AGN and GRB jets.", "map": "P_{\\rm BZ}\\approx\\frac{\\kappa}{4\\pi c}\\Phi_B^2\\Omega_H^2\\ (\\text{Gaussian}),\\ \\Omega_H=\\frac{ac}{r_+^2+a^2},\\ \\kappa\\approx0.05", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2101", "a": "05-relativity-and-gravitation/black-holes/schwarzschild-and-kerr-black-holes", "b": "10-plasma-physics/magnetohydrodynamics/magnetic-reconnection", "name": "Reconnection-driven Penrose process in the ergosphere", "kind": "mechanism", "summary": "Fast reconnection mediated by plasmoids inside the ergosphere can put one plasmoid on an orbit with negative energy at infinity and send the other to infinity, extracting spin energy. This reconnection variant of the Penrose process needs near-maximal spin and strong magnetization.", "map": "\\epsilon_-^\\infty<0,\\ \\Delta\\epsilon_+^\\infty>0\\ \\text{for}\\ a\\to GM/c^2\\ \\text{and large}\\ \\sigma_0;\\ v_{\\rm in}\\sim0.1v_A", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2102", "a": "05-relativity-and-gravitation/black-holes/schwarzschild-and-kerr-black-holes", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Black-hole shadow and lensing in a plasma", "kind": "mechanism", "summary": "In a cold plasma a photon behaves like a particle of mass ħω_p/c², so rays follow Synge's dispersive Hamiltonian instead of null geodesics. The photon sphere and the shadow size then depend on frequency: the effect is negligible at EHT's 230 GHz but significant at low radio frequencies.", "map": "g^{\\mu\\nu}k_\\mu k_\\nu+\\omega_p^2/c^2=0,\\ m_{\\rm eff}=\\hbar\\omega_p/c^2,\\ \\omega_p^2=\\frac{n_ee^2}{\\epsilon_0m_e}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2103", "a": "05-relativity-and-gravitation/black-holes/schwarzschild-and-kerr-black-holes", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "GR particle-in-cell simulations of Kerr magnetospheres", "kind": "method transfer", "summary": "Particle-in-cell kinetics with pair creation has been ported to the Kerr metric. These simulations launch Blandford–Znajek jets from first principles and show spark-gap pair discharges near the horizon and kinetic reconnection in the equatorial current sheet.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2104", "a": "05-relativity-and-gravitation/black-holes/schwarzschild-and-kerr-black-holes", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Charged-particle orbits around magnetized black holes", "kind": "shared object", "summary": "Wald's solution for a uniform field in Kerr spacetime allows gyration, drifts and adiabatic invariants to be studied in curved spacetime. The field shifts the ISCO, makes orbits chaotic and enables a magnetic Penrose process for charged particles.", "map": "A_\\mu=\\frac{B_0}{2}(\\psi_\\mu+2a\\,\\eta_\\mu),\\ \\psi=\\partial_\\phi,\\ \\eta=\\partial_t\\ \\text{Killing vectors}", "breaks": "", "confidence": "current research", "strength": 1}
{"id": "C2105", "a": "05-relativity-and-gravitation/black-holes/schwarzschild-and-kerr-black-holes", "b": "10-plasma-physics/space-and-astrophysical-plasmas/magnetospheres-and-space-weather", "name": "Horizon as a unipolar inductor (membrane paradigm)", "kind": "analogy", "summary": "A spinning horizon threaded by magnetic flux acts like a rotating conductor that generates an EMF ~Ω_HΦ, with the circuit closing through the magnetosphere. This is the same unipolar-inductor picture as the Io–Jupiter flux-tube circuit and pulsar magnetospheres; in the membrane paradigm the horizon has a surface resistivity of 377 Ω.", "map": "V\\sim\\frac{\\Omega_H\\Phi}{2\\pi},\\ R_H=\\mu_0c\\approx377\\,\\Omega\\ \\leftrightarrow\\ \\text{Io–Jupiter: }V\\sim vBL", "breaks": "The horizon is a causal boundary, not a material conductor. Its 'resistivity' is a teleological boundary condition fixed by the metric, it carries no real charges, and the energy comes from negative-energy states in the ergosphere rather than from a moving body.", "confidence": "established", "strength": 2}
{"id": "C2106", "a": "05-relativity-and-gravitation/general-relativity/einstein-field-equations", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Gravitating 'plasma': Jeans instability and Einstein–Vlasov", "kind": "analogy", "summary": "The Vlasov–Poisson system for self-gravitating collisionless matter (the Newtonian limit) is plasma kinetics with the sign of the interaction flipped. The squared plasma frequency turns negative, so oscillations become the Jeans instability, and gravitational Landau damping also exists. The relativistic version is the Einstein–Vlasov system.", "map": "\\frac{e^2}{4\\pi\\epsilon_0}\\to-Gm^2:\\ \\omega_p^2\\to-4\\pi G\\rho,\\ \\omega^2=\\omega_p^2+3k^2v_{th}^2\\ \\to\\ \\omega^2=c_s^2k^2-4\\pi G\\rho", "breaks": "With one-sign charge there is no Debye screening and no neutralizing background, hence the Jeans swindle. Self-gravitating systems are non-extensive, have negative heat capacity, and relax violently rather than towards Maxwellians.", "confidence": "established", "strength": 2}
{"id": "C2107", "a": "05-relativity-and-gravitation/general-relativity/modified-gravity", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Chameleon screening vs Debye screening", "kind": "analogy", "summary": "Both cut off a 1/r force through a mass that depends on the environment. Debye shielding by mobile charges gives a Yukawa potential whose length λ_D is set by density and temperature. A chameleon scalar's effective mass grows with ambient density, so fifth forces are Yukawa-suppressed in dense environments.", "map": "\\frac{e^{-r/\\lambda_D}}{r},\\ \\lambda_D^{-2}=\\frac{n e^2}{\\epsilon_0k_BT}\\ \\leftrightarrow\\ \\frac{e^{-m_{\\rm eff}(\\rho)r}}{r},\\ m_{\\rm eff}^2=V_{\\rm eff}''(\\phi_{\\min}(\\rho))", "breaks": "Debye screening is the linear response of charges of both signs. Chameleon screening is a nonlinear self-interaction whose thin-shell suppression depends on the source's Newtonian potential. Vainshtein screening works through derivatives and involves no mass at all, and gravity itself, with one-sign charge, cannot be Debye-screened.", "confidence": "established", "strength": 2}
{"id": "C2108", "a": "05-relativity-and-gravitation/general-relativity/numerical-relativity", "b": "10-plasma-physics/magnetohydrodynamics/dynamo-theory", "name": "Field amplification in neutron-star mergers", "kind": "mechanism", "summary": "The Kelvin–Helmholtz instability at the contact layer of merging neutron stars drives a small-scale turbulent dynamo that amplifies fields toward magnetar strength within milliseconds, and an MRI dynamo follows in the remnant disk. This controls jet launching and outflows like GRB 170817A, but GRMHD resolves it only partly.", "map": "\\sigma_{\\rm KH}\\sim k\\Delta v,\\ B\\to\\gtrsim10^{16}\\,\\text{G in}\\ \\sim\\text{ms}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2109", "a": "05-relativity-and-gravitation/general-relativity/numerical-relativity", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "Constraint damping: ∇·B=0 vs Einstein constraints", "kind": "analogy", "summary": "Both are hyperbolic evolutions that carry elliptic constraints, which hold analytically but drift numerically. Constraint damping in Z4/CCZ4 and generalized-harmonic codes and hyperbolic divergence cleaning in MHD use the same trick: turn the violation into a damped field that propagates away.", "map": "\\partial_t\\psi+c_h^2\\nabla\\cdot\\mathbf B=-\\frac{c_h^2}{c_p^2}\\psi\\ \\leftrightarrow\\ \\partial_t\\Theta\\supset\\frac{\\alpha}{2}\\mathcal H-\\alpha\\kappa_1(2+\\kappa_2)\\Theta", "breaks": "Einstein's constraints generate diffeomorphisms, so their violation mixes with the gauge choice. ∇·B=0 is a topological identity with no gauge content, and constrained transport can enforce it exactly, which has no GR counterpart.", "confidence": "established", "strength": 2}
{"id": "C2110", "a": "05-relativity-and-gravitation/general-relativity/numerical-relativity", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "GRMHD: ideal MHD on a dynamical spacetime", "kind": "method transfer", "summary": "Conservative shock-capturing schemes and constrained transport for ∇·B=0, first developed for Newtonian MHD, were carried into GR codes. The stress–energy of the magnetized fluid, including magnetic pressure and tension, sources Einstein's equations in simulations of neutron-star mergers and collapse.", "map": "T^{\\mu\\nu}=(\\rho h+b^2)u^\\mu u^\\nu+(p+\\tfrac{b^2}{2})g^{\\mu\\nu}-b^\\mu b^\\nu,\\ G_{\\mu\\nu}=8\\pi GT_{\\mu\\nu}/c^4", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2111", "a": "05-relativity-and-gravitation/general-relativity/tests-of-general-relativity", "b": "10-plasma-physics/space-and-astrophysical-plasmas/solar-wind-and-heliosphere", "name": "Coronal plasma in solar-conjunction GR tests", "kind": "method transfer", "summary": "The dispersive delay of the corona and solar wind contaminates measurements of Shapiro delay and light deflection near the Sun. During its 2002 solar conjunction, Cassini's multi-frequency (X/Ka) link cancelled the plasma term and bounded γ−1=(2.1±2.3)×10⁻⁵.", "map": "\\Delta t_{\\rm GR}=(1+\\gamma)\\frac{GM_\\odot}{c^3}\\ln\\frac{4r_er_p}{b^2}\\ \\text{vs}\\ \\Delta t_{\\rm pl}\\propto\\nu^{-2}\\int n_e\\,dl", "breaks": "", "confidence": "established", "strength": 2}