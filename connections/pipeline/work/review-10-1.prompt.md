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

# Packet 10-1 (100 records)

{"id": "C0393", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "10-plasma-physics/magnetic-confinement-fusion/stellarators", "name": "Stellarator optimization with differentiable and ML tools", "kind": "method transfer", "summary": "Stellarator coil and shape optimization uses adjoint or automatic differentiation and surrogate models over a large 3D parameter space.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0394", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "10-plasma-physics/magnetic-confinement-fusion/tokamaks", "name": "Disruption prediction and plasma control with ML", "kind": "method transfer", "summary": "Tokamak disruption predictors and deep-RL magnetic controllers (e.g. on TCV) apply ML to real-time control where first-principles models are too slow.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0395", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "10-plasma-physics/magnetic-confinement-fusion/turbulent-transport-and-gyrokinetics", "name": "ML surrogates and control in fusion", "kind": "method transfer", "summary": "Neural surrogates of gyrokinetic fluxes accelerate transport modelling, and reinforcement learning has been used for tokamak shape control and disruption prediction.", "map": "Q\\approx \\mathcal N_\\theta(\\nabla T,\\nabla n,\\hat s,q)", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0396", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "name": "Ab initio MD for warm dense matter", "kind": "method transfer", "summary": "Warm dense matter equations of state and conductivities are computed by finite-temperature DFT-MD and path-integral Monte Carlo, bridging condensed matter methods to plasma conditions.", "map": "F[n,T]=\\min\\ \\text{free-energy functional}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0397", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas", "name": "Strongly coupled plasmas studied by MD", "kind": "shared object", "summary": "The one-component plasma and Yukawa systems are benchmark MD systems, with melting at Γ≈175 (OCP) and dusty-plasma crystals; MD gives transport and equation of state where perturbation theory fails.", "map": "\\Gamma=\\frac{Z^2e^2}{4\\pi\\epsilon_0 a k_BT}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0398", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Particle pushers and MD integrators", "kind": "shared object", "summary": "PIC particle pushing and MD both integrate N-body trajectories with time-reversible Verlet-like schemes; MD with Coulomb forces uses Ewald or PPPM mesh methods also used in PIC.", "map": "\\ddot{\\mathbf r}_i=\\mathbf F_i/m_i", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0399", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "name": "Path-integral Monte Carlo for dense plasmas", "kind": "method transfer", "summary": "Fermionic PIMC and the sign problem constrain what can be computed for hydrogen and electron gases at WDM conditions; restricted and permutation-blocking variants give benchmark equations of state.", "map": "Z=\\mathrm{Tr}\\,e^{-\\beta H}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0400", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "10-plasma-physics/magnetic-confinement-fusion/burning-plasmas-and-iter", "name": "Monte Carlo neutronics and alpha-particle transport", "kind": "method transfer", "summary": "Neutron transport, tritium breeding and shielding in fusion devices use Monte Carlo codes, and Monte Carlo Fokker–Planck operators model fast-alpha slowing down.", "map": "\\partial_t f=C[f]", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0401", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Fokker–Planck collisions and Monte Carlo operators", "kind": "method transfer", "summary": "Coulomb collisions are a Fokker–Planck diffusion in velocity space, implemented by Monte Carlo binary-collision models (Takizuka–Abe) in PIC, equivalent to a Langevin stochastic process.", "map": "\\partial_t f=-\\partial_v(Af)+\\tfrac12\\partial_v^2(Df)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0402", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "10-plasma-physics/inertial-and-laser-plasmas/inertial-confinement-fusion", "name": "Radiation-hydrodynamics codes for ICF", "kind": "method transfer", "summary": "ICF design relies on multi-physics finite-volume or Lagrangian hydrodynamics coupled to radiation transport and shock-capturing schemes to model implosions and Rayleigh–Taylor growth.", "map": "\\partial_t U+\\nabla\\cdot F(U)=S", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0403", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "10-plasma-physics/inertial-and-laser-plasmas/plasma-wakefield-acceleration", "name": "Particle-in-cell simulation of wakefields", "kind": "method transfer", "summary": "PIC codes, often with boosted frames and quasi-static or envelope reductions, are the primary design tool for wakefield accelerators, whose bubble regime was found through simulation.", "map": "\\nabla\\cdot\\mathbf E=\\rho/\\epsilon_0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0404", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "Divergence-free constraint and conservative MHD solvers", "kind": "method transfer", "summary": "Numerical MHD needs constrained transport, Godunov/Riemann solvers and divergence cleaning to preserve ∇·B=0; these schemes were developed for MHD and spread to astrophysical fluid codes.", "map": "\\nabla\\cdot\\mathbf B=0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0405", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "10-plasma-physics/magnetohydrodynamics/mhd-turbulence", "name": "Spectral direct numerical simulation of MHD turbulence", "kind": "method transfer", "summary": "Pseudo-spectral DNS is the main tool to test anisotropic cascade and critical-balance predictions; resolution limits restrict inertial range and Reynolds number, linking to astrophysical turbulence reviews.", "map": "\\partial_t\\mathbf z^\\pm\\mp\\mathbf V_A\\!\\cdot\\!\\nabla\\mathbf z^\\pm=\\ldots", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0406", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Vlasov solvers and spectral methods", "kind": "method transfer", "summary": "Vlasov–Maxwell is solved by semi-Lagrangian, spectral (Hermite) and discontinuous-Galerkin schemes; recurrence and filamentation in velocity space limit resolution, and symplectic or structure-preserving integrators conserve invariants.", "map": "\\partial_t f+v\\partial_x f+\\frac{qE}{m}\\partial_v f=0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0407", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Boris pusher and symplectic integrators", "kind": "method transfer", "summary": "The Boris algorithm advances charged particles in E and B volume-preservingly with long-term stability, a precursor of modern structure-preserving integrators used in particle-in-cell codes.", "map": "\\mathbf v^{n+1/2}=\\mathbf v^{n-1/2}+\\frac{q\\Delta t}{m}(\\mathbf E+\\bar{\\mathbf v}\\times\\mathbf B)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0408", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Kramers–Kronig dispersion relations in plasma response", "kind": "identity", "summary": "Causality of the plasma dielectric response implies analyticity in the upper half ω-plane and Kramers–Kronig relations linking reactive and dissipative (Landau) parts.", "map": "\\mathrm{Re}\\,\\epsilon(\\omega)-1=\\frac{2}{\\pi}P\\!\\int\\frac{\\omega'\\,\\mathrm{Im}\\,\\epsilon(\\omega')}{\\omega'^2-\\omega^2}d\\omega'", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0409", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Landau contour and plasma dispersion function", "kind": "method transfer", "summary": "Landau damping arises from the pole in the Vlasov dispersion integral; Landau's analytic-continuation prescription (deforming the contour) gives the Fried–Conte plasma dispersion function Z, a Faddeeva/error-function relative.", "map": "\\epsilon(k,\\omega)=1+\\frac{1}{k^2\\lambda_D^2}[1+\\zeta Z(\\zeta)]", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0410", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks", "name": "Diffusive shock acceleration power-law spectrum", "kind": "shared object", "summary": "Diffusive shock acceleration yields a power-law spectrum from a Bessel/Green's-function-type transport problem and compression-ratio dependence; the shared paper reflects asymptotic and special-function methods in acceleration theory.", "map": "f(p)\\propto p^{-3r/(r-1)}", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C0411", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "MHD stability as Sturm–Liouville / self-adjoint problem", "kind": "mechanism", "summary": "Linear ideal MHD is a self-adjoint force operator problem, so the energy principle δW and normal-mode spectrum follow from variational Sturm–Liouville-type theory.", "map": "\\omega^2\\rho\\xi=\\mathbf{F}[\\xi],\\quad \\delta W=-\\tfrac12\\int\\xi\\cdot\\mathbf F[\\xi]", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0412", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Dispersion relations from linearized PDEs", "kind": "method transfer", "summary": "Plasma waves and instabilities are found by Fourier–Laplace transforming linearized fluid or Vlasov equations; the initial-value problem and Green's-function causality (Bers–Briggs) distinguish absolute from convective instability.", "map": "D(k,\\omega)=0,\\quad \\omega=\\omega_r+i\\gamma", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0413", "a": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "Self-adjoint force operator and spectral theorem", "kind": "identity", "summary": "The MHD force operator is Hermitian on a Hilbert space with energy inner product, giving real ω² and a spectrum with discrete and continuous parts (Alfvén and slow continua), with non-normal subtleties in flows.", "map": "\\langle\\eta,F\\xi\\rangle=\\langle F\\eta,\\xi\\rangle", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0414", "a": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Van Kampen modes and continuous spectrum", "kind": "mechanism", "summary": "Van Kampen's treatment of linearized Vlasov uses singular eigenfunctions of a continuous spectrum, with Landau damping appearing as phase mixing; the Vlasov operator is non-self-adjoint in general.", "map": "\\partial_t\\delta f+ikv\\,\\delta f=\\ldots", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0415", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "10-plasma-physics/magnetohydrodynamics/dynamo-theory", "name": "Frozen-in flux as Lie dragging of a 2-form", "kind": "identity", "summary": "Ideal MHD induction is Lie transport of the magnetic flux 2-form, and helicity is a differential-form integral; this geometric view clarifies the Cauchy solution and topological constraints.", "map": "\\partial_t B=\\nabla\\times(v\\times B)\\;\\Leftrightarrow\\;(\\partial_t+\\mathcal L_v)\\,\\mathbf B^{(2)}=0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0416", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Langmuir probes and plasma diagnostics", "kind": "shared object", "summary": "Diagnostics such as Langmuir probes, Thomson scattering and interferometry rely on Debye sheath physics and detector noise limits; probe I–V curves infer density and temperature.", "map": "I=I_{sat}\\left[1-\\exp\\!\\left(\\frac{e(V-V_f)}{k_BT_e}\\right)\\right]", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0417", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "10-plasma-physics/magnetohydrodynamics/mhd-turbulence", "name": "Structure functions and spectral inference of turbulence", "kind": "method transfer", "summary": "Solar wind turbulence exponents are estimated from spacecraft time series using structure functions and power spectra, with finite-sample and intermittency biases requiring statistical care.", "map": "S_p(\\ell)=\\langle|\\delta u(\\ell)|^p\\rangle\\propto\\ell^{\\zeta_p}", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C0418", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "10-plasma-physics/magnetic-confinement-fusion/stellarators", "name": "Quasi-symmetry and conserved canonical momentum", "kind": "identity", "summary": "Quasi-symmetry in stellarators makes |B| symmetric in Boozer coordinates, so a Noether-type canonical momentum is conserved and guiding-centre orbits are confined like in tokamaks; omnigeneity generalizes this.", "map": "B=B(\\psi,M\\theta-N\\varphi)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0419", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "10-plasma-physics/magnetic-confinement-fusion/tokamaks", "name": "Axisymmetry gives conserved toroidal angular momentum", "kind": "identity", "summary": "Toroidal axisymmetry of a tokamak yields conservation of canonical toroidal angular momentum, confining particle orbits and underpinning neoclassical theory; stellarators lack this, hence 3D optimization.", "map": "p_\\varphi=mRv_\\varphi+q\\psi\\ \\text{const}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0420", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "Magnetic helicity and cross-helicity conservation", "kind": "identity", "summary": "Ideal MHD has conserved helicity invariants arising from relabelling symmetry of the fluid Lagrangian (Noether), constraining reconnection, dynamos and turbulent cascades.", "map": "H=\\int\\mathbf A\\cdot\\mathbf B\\,dV", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0421", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Adiabatic invariants from approximate symmetry", "kind": "identity", "summary": "The magnetic moment and other adiabatic invariants are Noether-type conserved quantities of averaged Lagrangians with a slow-variable approximate symmetry; guiding-centre theory uses Lie-transform perturbation of the Hamiltonian structure.", "map": "\\mu=\\frac{m v_\\perp^2}{2B},\\quad J=\\oint p\\,dq", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0422", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "10-plasma-physics/magnetohydrodynamics/dynamo-theory", "name": "Dynamo as symmetry-breaking of field", "kind": "analogy", "summary": "Dynamos spontaneously break symmetries of the flow, such as reflection and time-reversal in geodynamo reversals, and the α-effect needs broken mirror symmetry (helicity); dynamo onset resembles a bifurcation with a growth-rate order parameter.", "map": "\\partial_t \\bar B=\\nabla\\times(\\alpha\\bar B)+\\eta\\nabla^2\\bar B", "breaks": "Dynamo growth is a kinematic linear instability, not an equilibrium ordered phase; no Goldstone modes in the usual sense.", "confidence": "current research", "strength": 2}
{"id": "C0423", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Debye screening and Meissner/Higgs screening", "kind": "analogy", "summary": "Debye screening gives a Yukawa-type potential with length λ_D, analogous to the finite penetration depth of magnetic fields in superconductors and the massive gauge boson range in the Higgs phase.", "map": "\\phi\\propto e^{-r/\\lambda_D}/r\\leftrightarrow e^{-mr}/r", "breaks": "Debye screening is a thermal static effect, not a symmetry-breaking vacuum condensate, and the screening is electric rather than magnetic.", "confidence": "established", "strength": 2}
{"id": "C0424", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Plasma frequency and Higgs/Anderson mass generation", "kind": "analogy", "summary": "Anderson noted that Coulomb long-range interaction turns the gapless Goldstone-like phonon into a gapped plasmon, the prototype of the Higgs mechanism; gauge field gives photon effective mass, as in plasma screening.", "map": "\\omega^2=\\omega_p^2+c^2k^2\\leftrightarrow E^2=m^2+p^2", "breaks": "The plasma has no spontaneously broken local gauge symmetry; the photon mass is an effective in-medium dispersion, with the rest frame privileged.", "confidence": "established", "strength": 2}
{"id": "C0425", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "10-plasma-physics/magnetic-confinement-fusion/turbulent-transport-and-gyrokinetics", "name": "Gyro-Bohm scaling and dimensionless confinement scaling", "kind": "method transfer", "summary": "Tokamak confinement scalings use Kadomtsev's constraint and Buckingham π to reduce parameters to ρ*, β, ν*; gyro-Bohm transport scales as ρ*χ_Bohm, enabling extrapolation to ITER.", "map": "\\chi_{gB}\\sim\\rho_*\\,\\frac{T}{eB}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0426", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "10-plasma-physics/magnetohydrodynamics/magnetic-reconnection", "name": "Sweet–Parker scaling with Lundquist number", "kind": "method transfer", "summary": "The Sweet–Parker inflow rate follows from mass and flux balance, giving a scaling in Lundquist number S; plasmoid instability sets a critical S≈10^4 beyond which rate becomes S-independent.", "map": "v_{in}/V_A\\sim S^{-1/2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0427", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "10-plasma-physics/magnetohydrodynamics/mhd-turbulence", "name": "Kolmogorov-style dimensional spectra for MHD turbulence", "kind": "method transfer", "summary": "Iroshnikov–Kraichnan and Goldreich–Sridhar spectra are derived by constant-flux dimensional arguments and critical balance, extending Kolmogorov scaling to magnetized fluids.", "map": "E(k_\\perp)\\propto\\epsilon^{2/3}k_\\perp^{-5/3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0428", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Plasma parameters as dimensionless groups", "kind": "method transfer", "summary": "Plasma regimes are classified by dimensionless numbers such as the plasma parameter, Lundquist number, beta and normalized gyroradius; similarity scaling lets lab experiments emulate astrophysical plasmas.", "map": "\\Lambda=n\\lambda_D^3,\\quad S=\\frac{LV_A}{\\eta}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0819", "a": "01-classical-mechanics/analytical-mechanics/canonical-transformations-and-hamilton-jacobi", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Adiabatic invariants as action variables", "kind": "identity", "summary": "The magnetic moment, bounce invariant J and flux invariant are action integrals of near-periodic motion, conserved to all orders in the slow-variation parameter under averaging.", "map": "J=\\oint p\\,dq,\\ \\mu\\propto J_\\perp", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0820", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Vlasov equation as Liouville flow", "kind": "identity", "summary": "The collisionless Vlasov equation is Liouville's theorem for the single-particle distribution function in phase space, with Poisson-bracket form and Hamiltonian field structure.", "map": "\\partial_t f+\\{f,H\\}=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0821", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Guiding-centre Hamiltonian dynamics", "kind": "method transfer", "summary": "Guiding-centre motion is derived via Hamiltonian and Lagrangian averaging (Littlejohn, Lie-transform perturbation theory), preserving the symplectic structure and giving adiabatic invariants.", "map": "\\mu=\\frac{m v_\\perp^2}{2B}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0822", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "10-plasma-physics/space-and-astrophysical-plasmas/magnetospheres-and-space-weather", "name": "Radiation belts and three adiabatic invariants", "kind": "mechanism", "summary": "Trapped radiation-belt particles carry three adiabatic invariants (μ, J, Φ) from separation of gyro, bounce and drift timescales, a nearly integrable Hamiltonian system; radial diffusion breaks the third.", "map": "\\mu,\\ J,\\ \\Phi", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0823", "a": "01-classical-mechanics/analytical-mechanics/lagrangian-mechanics", "b": "10-plasma-physics/magnetic-confinement-fusion/turbulent-transport-and-gyrokinetics", "name": "Gyrokinetics from Lagrangian field theory", "kind": "method transfer", "summary": "Modern gyrokinetics is derived from a phase-space Lagrangian with Lie-transform and variational methods, ensuring exact conservation laws via Noether's theorem.", "map": "\\delta\\int L\\,dt=0\\Rightarrow\\text{conserved energy}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0824", "a": "01-classical-mechanics/analytical-mechanics/variational-principles", "b": "10-plasma-physics/magnetic-confinement-fusion/tokamaks", "name": "Variational MHD equilibrium and stability", "kind": "method transfer", "summary": "MHD equilibrium extremizes energy at fixed constraints and stability follows from the energy principle δW, a Rayleigh–Ritz variational method; Grad–Shafranov describes axisymmetric equilibria.", "map": "\\delta W[\\boldsymbol\\xi]\\ge0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0825", "a": "01-classical-mechanics/continuum-and-fluid-mechanics", "b": "10-plasma-physics/magnetohydrodynamics", "name": "MHD as continuum mechanics", "kind": "shared object", "summary": "MHD applies continuum conservation laws of mass, momentum and energy to a conducting fluid with added magnetic stress.", "map": "\\rho\\,d\\mathbf{u}/dt=-\\nabla p+\\mathbf{J}\\times\\mathbf{B}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0826", "a": "01-classical-mechanics/continuum-and-fluid-mechanics", "b": "10-plasma-physics/magnetohydrodynamics", "name": "MHD as fluid mechanics plus Lorentz force", "kind": "identity", "summary": "Ideal MHD is Euler or Navier–Stokes flow coupled to induction and the Lorentz force; vorticity and magnetic-field equations share the same frozen-in structure.", "map": "\\partial_t \\mathbf{B}=\\nabla\\times(\\mathbf{u}\\times\\mathbf{B}),\\ \\partial_t \\boldsymbol{\\omega}=\\nabla\\times(\\mathbf{u}\\times\\boldsymbol{\\omega})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0827", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "Alfvén waves as tension waves; Kelvin circulation", "kind": "mechanism", "summary": "Frozen-in flux parallels Kelvin's circulation theorem and vorticity transport; magnetic tension gives Alfvén waves like waves on a string, extending Euler flow.", "map": "v_A=B/\\sqrt{\\mu_0\\rho}", "breaks": "Magnetic field adds anisotropic restoring force, so waves are not isotropic.", "confidence": "established", "strength": 3}
{"id": "C0828", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "10-plasma-physics/space-and-astrophysical-plasmas/solar-wind-and-heliosphere", "name": "Parker wind as transonic nozzle flow", "kind": "analogy", "summary": "Parker's solar wind is a de Laval-nozzle type steady flow with a critical sonic point; gravity and geometry replace the nozzle area change.", "map": "\\left(u-\\frac{c_s^2}{u}\\right)\\frac{du}{dr}=\\frac{2c_s^2}{r}-\\frac{GM}{r^2}", "breaks": "Wind is heated and magnetised, and the solar wind is collisionless with non-fluid effects.", "confidence": "established", "strength": 2}
{"id": "C0829", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "10-plasma-physics/inertial-and-laser-plasmas", "name": "Laser-plasma hydrodynamic instabilities", "kind": "shared object", "summary": "Laser-driven ablation and shock-accelerated interfaces in laser plasmas realise classic interfacial instabilities (RT, RM, KH) under extreme conditions.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0830", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "10-plasma-physics/inertial-and-laser-plasmas/inertial-confinement-fusion", "name": "Rayleigh–Taylor in ICF implosions", "kind": "shared object", "summary": "Rayleigh–Taylor and Richtmyer–Meshkov instabilities at the ablation front and fuel–shell interface limit capsule compression and ignition; classical growth rates are modified by ablation.", "map": "\\gamma=\\sqrt{A k g}-\\beta k v_a", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0831", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "10-plasma-physics/magnetohydrodynamics/dynamo-theory", "name": "Convection-driven dynamos", "kind": "mechanism", "summary": "Rotating Rayleigh–Bénard convection drives geodynamo and solar dynamo flows, with helical convective motions supplying the α-effect.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0832", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "MHD instabilities as magnetised RT/KH", "kind": "mechanism", "summary": "Interchange instability is Rayleigh–Taylor with effective gravity from field curvature; magnetic tension modifies Kelvin–Helmholtz thresholds and Chandrasekhar's magnetised convection.", "map": "\\gamma^2\\sim -g_{eff}\\,\\nabla\\ln p", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0833", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Kinetic vs fluid instability analyses", "kind": "method transfer", "summary": "Normal-mode dispersion analysis and Nyquist criteria developed for plasma kinetic instabilities (two-stream, Penrose) parallel hydrodynamic shear and stratified-flow stability; the two-stream instability resembles Kelvin–Helmholtz.", "map": "D(\\omega,k)=0", "breaks": "Kinetic resonance with particle velocities has no fluid counterpart; fluid models lack velocity-space instabilities.", "confidence": "established", "strength": 1}
{"id": "C0834", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Ion-acoustic and Kelvin–Helmholtz in plasmas", "kind": "shared object", "summary": "Kelvin–Helmholtz and Rayleigh–Taylor instabilities occur at magnetopause and in laser plasmas, with magnetic shear and finite Larmor radius modifying growth.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C0835", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "10-plasma-physics/magnetic-confinement-fusion/turbulent-transport-and-gyrokinetics", "name": "Plasma turbulence and fluid turbulence", "kind": "analogy", "summary": "Drift-wave turbulence has cascades, intermittency and zonal-flow formation analogous to 2D fluid turbulence, mirrored by Hasegawa–Mima and Charney–Hasegawa–Mima equations.", "map": "\\partial_t(\\nabla^2\\phi-\\phi)+\\hat z\\times\\nabla\\phi\\cdot\\nabla(\\nabla^2\\phi)=0", "breaks": "Kinetic effects, resonant wave-particle interaction and non-adiabatic electrons have no fluid analogue.", "confidence": "established", "strength": 3}
{"id": "C0836", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "10-plasma-physics/magnetohydrodynamics/dynamo-theory", "name": "Turbulent dynamo and mean-field theory", "kind": "mechanism", "summary": "Turbulent flows stretch, twist and fold field lines, giving small-scale dynamos and mean-field α-effect; the shared accretion-disk paper links turbulence, MRI and transport.", "map": "\\partial_t\\bar{\\mathbf B}=\\nabla\\times(\\alpha\\bar{\\mathbf B}-\\eta_t\\nabla\\times\\bar{\\mathbf B})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0837", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "10-plasma-physics/magnetohydrodynamics/mhd-turbulence", "name": "Kolmogorov cascade to MHD cascade", "kind": "analogy", "summary": "Hydrodynamic energy cascade and Kolmogorov scaling generalize to MHD via Iroshnikov–Kraichnan and Goldreich–Sridhar theories, with Alfvén-wave interactions and anisotropy.", "map": "E(k)\\sim\\epsilon^{2/3}k^{-5/3}\\ \\to\\ E(k_\\perp)\\sim k_\\perp^{-5/3}", "breaks": "Magnetic field imposes anisotropy and non-local interactions; no isotropic Kolmogorov scaling exists in strong mean field.", "confidence": "established", "strength": 3}
{"id": "C0838", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "10-plasma-physics/magnetohydrodynamics/mhd-turbulence", "name": "MHD turbulence extends Kolmogorov theory", "kind": "analogy", "summary": "Critical balance and anisotropic cascades in MHD turbulence extend Kolmogorov phenomenology, with magnetic energy and cross-helicity as additional invariants.", "map": "k_\\parallel v_A\\sim k_\\perp u_\\perp", "breaks": "Strong mean field makes cascade anisotropic; scaling differs from isotropic Kolmogorov.", "confidence": "established", "strength": 3}
{"id": "C0839", "a": "01-classical-mechanics/newtonian-mechanics/conservation-laws", "b": "10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks", "name": "Shock jump conditions as conservation laws", "kind": "identity", "summary": "Rankine–Hugoniot conditions are mass, momentum and energy conservation across a discontinuity; collisionless shocks satisfy them via field-mediated dissipation instead of collisions.", "map": "[\\rho u]=0,\\ [\\rho u^2+p]=0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0840", "a": "01-classical-mechanics/newtonian-mechanics/non-inertial-frames", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Lorentz force and Coriolis force", "kind": "analogy", "summary": "In a rotating frame the Coriolis force has the same form as the magnetic Lorentz force (Larmor's theorem), giving inertial waves and gyration analogous to cyclotron motion.", "map": "2m\\mathbf{v}\\times\\boldsymbol{\\Omega}\\leftrightarrow q\\mathbf{v}\\times\\mathbf{B}", "breaks": "Coriolis force is mass-proportional and charge-independent; the centrifugal term has no magnetic counterpart.", "confidence": "established", "strength": 2}
{"id": "C0841", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos", "b": "10-plasma-physics/magnetic-confinement-fusion/stellarators", "name": "Field-line flow as Hamiltonian system, KAM surfaces", "kind": "identity", "summary": "Magnetic field lines in toroidal geometry obey Hamiltonian equations with toroidal angle as time. Nested flux surfaces are KAM tori; resonant perturbations create islands and chaotic field lines.", "map": "\\frac{d\\theta}{d\\phi}=\\frac{\\partial H}{\\partial\\psi},\\ \\frac{d\\psi}{d\\phi}=-\\frac{\\partial H}{\\partial\\theta}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0842", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Particle trapping and quasilinear resonance overlap", "kind": "mechanism", "summary": "Nonlinear Landau damping and particle trapping in a wave potential produce pendulum-like islands in phase space; overlapping waves yield Chirikov chaos underlying quasilinear diffusion.", "map": "\\omega_b=\\sqrt{qE k/m}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0843", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Adiabatic invariant breakdown and chaos", "kind": "mechanism", "summary": "Magnetic moment conservation fails via resonance overlap or field-line curvature where gyroradius approaches field scale, producing chaotic scattering in current sheets and tail pitch-angle diffusion.", "map": "\\kappa^2=R_c/\\rho\\sim1", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0844", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "b": "10-plasma-physics/inertial-and-laser-plasmas/plasma-wakefield-acceleration", "name": "Nonlinear wake waves and wave breaking", "kind": "analogy", "summary": "Plasma wakes are nonlinear Langmuir waves whose steepening and wave-breaking limit sets accelerating gradients, comparable to nonlinear wave steepening and soliton formation in dispersive media.", "map": "E_{WB}=\\frac{m c\\,\\omega_p}{e}", "breaks": "Wakefields are driven, relativistic and not integrable; breaking is not soliton formation.", "confidence": "established", "strength": 2}
{"id": "C0845", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Ion-acoustic solitons and KdV", "kind": "shared object", "summary": "Weakly nonlinear ion-acoustic waves reduce to the KdV equation via reductive perturbation, giving solitons; Washimi–Taniuti derivation was a landmark. Alfvén waves yield DNLS.", "map": "u_t+6uu_x+u_{xxx}=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0846", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation", "b": "10-plasma-physics/magnetohydrodynamics/magnetic-reconnection", "name": "Plasmoid chain formation as pattern formation", "kind": "analogy", "summary": "Plasmoid instability of reconnection current sheets spontaneously produces hierarchical island chains from a tearing instability, analogous to pattern-forming instabilities.", "map": "", "breaks": "Tearing is driven by free magnetic energy in a topological change; there is no Turing-type wavelength selection by diffusion.", "confidence": "current research", "strength": 1}
{"id": "C0847", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Landau damping and Kuramoto synchronization", "kind": "mechanism", "summary": "Kuramoto oscillators with a frequency distribution obey a Vlasov-like continuum equation; incoherent-state stability and decay of the order parameter mirror Landau damping, as does the Case–Van Kampen analysis.", "map": "\\partial_t f+\\partial_\\theta(\\omega f)=0\\ \\leftrightarrow\\ \\partial_t f+v\\partial_x f=0", "breaks": "Kuramoto coupling is mean-field on a circle with no spatial structure; Kuramoto-model Landau damping is for non-smooth distributions.", "confidence": "current research", "strength": 2}
{"id": "C0848", "a": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "b": "10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas", "name": "Dust crystal lattice phonons", "kind": "shared object", "summary": "Dusty-plasma crystals support lattice phonons observable by video microscopy; they are screened-Coulomb (Yukawa) chains and lattices with normal modes, allowing atomic-scale dynamics at the particle level.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0849", "a": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Plasma oscillation as collective normal mode", "kind": "analogy", "summary": "Langmuir oscillation at ω_p is a collective harmonic mode of displaced electron sheets, and plasma waves are dispersive normal modes of a continuum of coupled oscillators.", "map": "\\omega_p^2=\\frac{n e^2}{\\epsilon_0 m}", "breaks": "Long-range Coulomb coupling gives non-local dispersion and Landau damping not present in lattice chains.", "confidence": "established", "strength": 2}
{"id": "C0850", "a": "01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "Magnetosonic and acoustic waves", "kind": "analogy", "summary": "Fast magnetosonic waves are sound waves stiffened by magnetic pressure; the Alfvén wave is a string wave along field lines, with dispersion from impedance-like medium properties.", "map": "v_f^2=c_s^2+v_A^2\\ (\\perp)", "breaks": "Anisotropic propagation and three wave branches, unlike isotropic sound.", "confidence": "established", "strength": 2}
{"id": "C0851", "a": "01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "Ponderomotive force and Kapitza pendulum", "kind": "identity", "summary": "A charged particle in a rapidly oscillating field feels an effective ponderomotive potential, the same averaging that stabilizes the Kapitza pendulum's inverted position.", "map": "U_p=\\frac{q^2E^2}{4m\\omega^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0852", "a": "01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Parametric instabilities and Mathieu resonance", "kind": "mechanism", "summary": "Parametric decay instabilities in laser-plasma and plasma waves are three-wave coupled-mode versions of parametric resonance (Mathieu), with pump threshold set by damping.", "map": "\\gamma^2=\\gamma_0^2-\\Gamma_1\\Gamma_2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1209", "a": "02-electromagnetism-and-optics/classical-optics/coherence-and-statistical-optics", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "Partial coherence suppresses instabilities", "kind": "method transfer", "summary": "Random phase plates and induced spatial incoherence reduce speckle-driven filamentation and parametric instabilities in laser plasmas by controlling coherence.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1210", "a": "02-electromagnetism-and-optics/classical-optics/interference-and-diffraction", "b": "10-plasma-physics/magnetic-confinement-fusion/tokamaks", "name": "Interferometry for plasma density", "kind": "method transfer", "summary": "Interferometers measure line-integrated density through the plasma refractive index. Mach–Zehnder and two-colour interferometry are standard on tokamaks and laser plasmas.", "map": "\\Delta\\phi\\propto\\lambda\\int n_e\\,dl", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1211", "a": "02-electromagnetism-and-optics/classical-optics/polarization-and-crystal-optics", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Faraday rotation and magnetized-plasma birefringence", "kind": "mechanism", "summary": "A magnetized plasma is birefringent, with O and X modes and Faraday rotation of linear polarization. Used for polarimetry of tokamak currents and astrophysical fields; matches magneto-optic effects in crystals.", "map": "\\Delta\\psi\\propto\\int n_e B_\\parallel\\,dl", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1212", "a": "02-electromagnetism-and-optics/electrodynamics", "b": "10-plasma-physics/plasma-fundamentals", "name": "Plasma as electrodynamic medium", "kind": "shared object", "summary": "A plasma is a medium with a frequency- and wavevector-dependent dielectric function from free charges. Skin depth, cutoff and reflection by the ionosphere follow from electrodynamics.", "map": "\\epsilon(\\omega)=1-\\omega_p^2/\\omega^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1213", "a": "02-electromagnetism-and-optics/electrodynamics", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Maxwell equations underlying plasma waves", "kind": "identity", "summary": "Plasma waves follow from Maxwell's equations closed with a plasma current response; the dielectric tensor turns the wave equation into the dispersion relations of Langmuir, EM, and whistler modes.", "map": "\\omega^2 = \\omega_p^2 + k^2c^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1214", "a": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "b": "10-plasma-physics/magnetic-confinement-fusion/tokamaks", "name": "Wave heating and current drive", "kind": "method transfer", "summary": "Electron cyclotron, ion cyclotron and lower-hybrid heating rely on waveguide and transmission-line technology, with gyrotrons as sources and wave propagation set by the magnetized-plasma dispersion relation.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1215", "a": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "EM waves in plasma: cutoff and skin depth", "kind": "identity", "summary": "Electromagnetic waves in a plasma have a cutoff at the plasma frequency and evanescent skin depth below it, like waveguide cutoff modes. Plasma-filled waveguides share the same dispersion form.", "map": "\\omega^2=\\omega_p^2+k^2c^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1216", "a": "02-electromagnetism-and-optics/electrodynamics/maxwells-equations", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "MHD as Maxwell with displacement current dropped", "kind": "mechanism", "summary": "MHD uses Ampère's law without displacement current and Faraday's law with Ohm's law. This gives induction equation, frozen-in flux and magnetic pressure and tension from the Maxwell stress tensor.", "map": "\\partial_t\\mathbf{B}=\\nabla\\times(\\mathbf{v}\\times\\mathbf{B})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1217", "a": "02-electromagnetism-and-optics/electrodynamics/maxwells-equations", "b": "10-plasma-physics/magnetohydrodynamics/magnetic-reconnection", "name": "Magnetic energy release and Poynting flux", "kind": "shared object", "summary": "Reconnection converts stored magnetic energy to flow and heat; field energy density and Poynting flux from Maxwell theory account for energy budgets, and Ohm's law breaks flux freezing.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1218", "a": "02-electromagnetism-and-optics/electrodynamics/potentials-and-gauge-invariance", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Gauge choice in gyrokinetics and Vlasov–Maxwell", "kind": "method transfer", "summary": "Vlasov–Maxwell and gyrokinetic theory use scalar and vector potentials, with Coulomb gauge and Lagrangian/Hamiltonian formulations. Gauge invariance underlies canonical momentum conservation and the ponderomotive force.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1219", "a": "02-electromagnetism-and-optics/electrodynamics/relativistic-electrodynamics", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "E×B drift from field transformation", "kind": "identity", "summary": "The E×B drift is the velocity of the frame where E vanishes, following from the Lorentz transformation of fields. Invariants E·B and E²−c²B² determine when such a frame exists.", "map": "\\mathbf{v}=\\mathbf{E}\\times\\mathbf{B}/B^2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1220", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/electrostatics-and-boundary-value-problems", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Debye screening as screened Poisson", "kind": "identity", "summary": "Debye shielding is Poisson's equation with a mobile-charge response, giving the screened (Yukawa) potential rather than Coulomb. Conductors in electrostatics are the infinite-density limit.", "map": "\\nabla^2\\phi=\\lambda_D^{-2}\\phi", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1221", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/fields-in-matter", "b": "10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas", "name": "Dielectric response and screening in dusty plasma", "kind": "analogy", "summary": "Dust grains charge and polarize in the plasma, and screened Coulomb (Yukawa) interactions follow from the dielectric response. Charged dust dynamics ties electrostatics to space plasmas.", "map": "", "breaks": "Dust charge is not fixed; it varies with the plasma currents, and the interaction is non-reciprocal in flowing plasma.", "confidence": "established", "strength": 1}
{"id": "C1222", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/magnetostatics", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Drifts from static field geometry", "kind": "shared object", "summary": "Gradient-B and curvature drifts and magnetic mirrors arise from non-uniform static magnetic fields computed from Biot–Savart and Ampère. Adiabatic invariants link to the magnetic moment of current loops.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1223", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/magnetostatics", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Magnetic fields and guiding-centre motion", "kind": "shared object", "summary": "Lorentz force in static magnetic fields gives gyration, gradient and curvature drifts, and mirror forces. These follow from magnetostatic field geometry and the dipole moment of gyrating charges.", "map": "\\mu = \\frac{m v_\\perp^2}{2B}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1224", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/multipole-expansions", "b": "10-plasma-physics/space-and-astrophysical-plasmas/magnetospheres-and-space-weather", "name": "Dipole field of planetary magnetospheres", "kind": "shared object", "summary": "Planetary fields are expanded in multipoles, with the dipole dominant. The dipole geometry sets L-shells, mirror points and radiation-belt trapping, with the magnetopause deforming it.", "map": "B=B_0 (R_E/r)^3\\sqrt{1+3\\sin^2\\lambda}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1225", "a": "02-electromagnetism-and-optics/photonics-and-lasers", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "Intense lasers driving plasma", "kind": "shared object", "summary": "High-power laser technology (chirped-pulse amplification, ultrashort pulses) supplies the drivers for laser–plasma physics. The plasma then acts as a nonlinear optical medium.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1226", "a": "02-electromagnetism-and-optics/photonics-and-lasers/integrated-and-fiber-photonics", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "Ponderomotive force and Kerr nonlinearity in filaments", "kind": "analogy", "summary": "Relativistic and ponderomotive self-focusing in plasma parallels Kerr self-focusing and filamentation in fibres and bulk media, with critical power thresholds and soliton-like channels.", "map": "P_{cr}\\propto\\lambda^2/n_2", "breaks": "Plasma nonlinearity is non-local and saturates via cavitation; Kerr nonlinearity is local and bound-electron.", "confidence": "established", "strength": 2}
{"id": "C1227", "a": "02-electromagnetism-and-optics/photonics-and-lasers/laser-physics", "b": "10-plasma-physics/inertial-and-laser-plasmas/plasma-wakefield-acceleration", "name": "Plasma as gain medium and X-ray lasers", "kind": "shared object", "summary": "Laser-produced plasmas serve as gain media for soft X-ray lasers via collisional excitation, and free-electron lasers share synchrotron-radiation physics with plasma-accelerator-driven sources.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1228", "a": "02-electromagnetism-and-optics/photonics-and-lasers/metamaterials-and-plasmonics", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "Surface plasmons and resonance absorption", "kind": "analogy", "summary": "Surface plasmon polaritons in metals and resonance absorption at the critical density in laser plasmas both come from a Drude-type epsilon crossing zero, with a resonant collective electron oscillation.", "map": "\\epsilon(\\omega)=1-\\omega_p^2/(\\omega^2+i\\nu\\omega)", "breaks": "Laser plasma is hot, inhomogeneous and nonlinear with density gradients; metal plasmons are cold, linear, bound to sharp interfaces.", "confidence": "established", "strength": 2}
{"id": "C1229", "a": "02-electromagnetism-and-optics/photonics-and-lasers/metamaterials-and-plasmonics", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Drude metal as cold plasma", "kind": "identity", "summary": "The free-electron Drude dielectric function of metals is the cold-plasma dielectric function. Bulk and surface plasmons are Langmuir-type oscillations, and epsilon-near-zero media exploit the plasma cutoff.", "map": "\\omega_p^2=\\frac{ne^2}{\\epsilon_0 m}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1230", "a": "02-electromagnetism-and-optics/photonics-and-lasers/nonlinear-optics", "b": "10-plasma-physics/inertial-and-laser-plasmas/inertial-confinement-fusion", "name": "Laser beam smoothing and cross-beam energy transfer", "kind": "method transfer", "summary": "Optical frequency conversion (KDP harmonics) and beam smoothing deliver uniform UV drive in ICF. Cross-beam energy transfer is a stimulated Brillouin process.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1231", "a": "02-electromagnetism-and-optics/photonics-and-lasers/nonlinear-optics", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "Parametric instabilities as nonlinear optics", "kind": "mechanism", "summary": "Stimulated Raman and Brillouin scattering and two-plasmon decay are three-wave parametric processes, analogous to optical parametric amplification and stimulated scattering in nonlinear media. Relativistic self-focusing parallels Kerr self-focusing.", "map": "\\omega_0=\\omega_s+\\omega_{pl},\\ \\mathbf{k}_0=\\mathbf{k}_s+\\mathbf{k}_{pl}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1232", "a": "02-electromagnetism-and-optics/photonics-and-lasers/topological-photonics", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Topological waves in magnetized plasma", "kind": "analogy", "summary": "Magnetized plasma, with gyrotropic dielectric tensor, breaks time reversal like magneto-optic photonic crystals. Topological edge modes (Parker et al.) can arise in continuous plasma, analogous to photonic quantum Hall.", "map": "", "breaks": "Plasma is continuous and dispersive, so the topological invariant needs regularization and bulk-edge correspondence is subtle.", "confidence": "current research", "strength": 2}
{"id": "C1233", "a": "02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics", "b": "10-plasma-physics/inertial-and-laser-plasmas", "name": "Plasma physics reliance on CPA lasers", "kind": "historical", "summary": "Chirped-pulse amplification, developed in optics, opened petawatt-class plasma experiments, including wakefield acceleration and ion acceleration.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1234", "a": "02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "Ultrafast pulses and relativistic laser-plasma", "kind": "method transfer", "summary": "Chirped-pulse amplification enabled relativistic intensities. High-harmonic generation on solid-plasma surfaces (relativistic oscillating mirror) is the plasma counterpart of gas-phase attosecond HHG.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1235", "a": "02-electromagnetism-and-optics/radiation-and-scattering/cherenkov-and-transition-radiation", "b": "10-plasma-physics/inertial-and-laser-plasmas/plasma-wakefield-acceleration", "name": "Wakefield as Cherenkov wake", "kind": "mechanism", "summary": "A relativistic driver excites a wake in plasma at phase velocity equal to the driver velocity, a Cherenkov-type process. Transition radiation is used to diagnose the accelerated beams.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1236", "a": "02-electromagnetism-and-optics/radiation-and-scattering/cherenkov-and-transition-radiation", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Cherenkov emission as beam-plasma instability", "kind": "mechanism", "summary": "Wave–particle resonance at ω=k·v is the Cherenkov condition. Landau damping and the beam-plasma instability are the collective version of Cherenkov emission of Langmuir waves.", "map": "\\omega=\\mathbf{k}\\cdot\\mathbf{v}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1237", "a": "02-electromagnetism-and-optics/radiation-and-scattering/dipole-radiation-and-antennas", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Antenna coupling and heating of plasma", "kind": "method transfer", "summary": "Antenna and waveguide launching of ion-cyclotron, lower-hybrid and helicon waves uses radiation and coupling theory. Cutoffs and resonances in plasma determine accessibility.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1238", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "Radiation from laser-driven electrons", "kind": "mechanism", "summary": "Electrons oscillating in intense laser fields emit nonlinear Thomson/Compton radiation and radiation-reaction losses. The Larmor and Liénard formulas govern emission and the damping force in ultra-intense regimes.", "map": "P=\\frac{2}{3}\\frac{e^2}{4\\pi\\epsilon_0 c^3}\\gamma^6\\left[\\dot{\\mathbf{a}}^2-\\ldots\\right]", "breaks": "", "confidence": "current research", "strength": 2}