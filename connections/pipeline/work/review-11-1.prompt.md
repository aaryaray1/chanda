You are the applied-physicist, the specialist for 11 (Interdisciplinary and Applied Physics) in this physics knowledge base.

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

## Field overview · `knowledge/11-interdisciplinary-physics`

> **Specialist:** `applied-physicist` · **arXiv:** physics.bio-ph, physics.ao-ph, physics.geo-ph, physics.med-ph, physics.chem-ph, physics.acc-ph, physics.app-ph · **Literature source:** OpenAlex (domain-filtered) + arXiv; INSPIRE for accelerators

#### What this field studies
Physical principles and methods applied to other sciences and to technology. Biophysics asks how molecules, cells and organisms obey (and exploit) physical law; climate physics explains Earth's energy balance and circulation; medical physics turns radiation and waves into diagnosis and therapy; chemical physics underpins reactions and spectroscopy; accelerator physics builds the machines that power particle physics and light sources; device physics drives electronics, photovoltaics and quantum sensors.

#### Conventions used in this branch
- Follow the host discipline's units: Gy and Sv (medical), K and W m⁻² (climate), kcal/mol or eV (chemistry), pN and nm (single-molecule), mm-mrad (beams).
- State biological and clinical claims with their evidence level; physics plausibility is not clinical efficacy.
- Climate numbers: cite IPCC AR6 assessed ranges (e.g. equilibrium climate sensitivity "likely" 2.5–4 K).

#### Historical spine
1895 X-rays (Röntgen) · 1896 Arrhenius on CO₂ warming · 1928 Raman effect · 1931–32 cyclotron · 1946 NMR · 1952 Hodgkin–Huxley neuron model · 1953 DNA double helix · 1954 silicon solar cell · 1961 Shockley–Queisser limit · 1967 first radiative–convective climate model · 1971–73 CT and MRI · 1982 STM · 1990 BOLD fMRI · 1992 single-DNA stretching · 2009 hard X-ray FEL (LCLS) · 2021 Nobel for climate modelling (Manabe, Hasselmann) · 2021 AlphaFold · 2024 Nobel Chemistry for protein design and structure prediction.

#### Canonical textbooks
- Nelson, *Biological Physics*; Phillips, Kondev & Theriot, *Physical Biology of the Cell*; Bialek, *Biophysics: Searching for Principles*.
- Pierrehumbert, *Principles of Planetary Climate*; Vallis, *Atmospheric and Oceanic Fluid Dynamics*; Stein & Wysession, *Introduction to Seismology*.
- Hendee & Ritenour, *Medical Imaging Physics*; Khan & Gibbons, *The Physics of Radiation Therapy*.
- Atkins & Friedman, *Molecular Quantum Mechanics*; Szabo & Ostlund, *Modern Quantum Chemistry*.
- Wiedemann, *Particle Accelerator Physics*; Sze & Ng, *Physics of Semiconductor Devices*.

#### Live frontiers
- AI-driven protein structure and design; physics of cellular decision-making.
- Narrowing climate sensitivity with paleoclimate and process understanding; tipping elements (AMOC).
- FLASH radiotherapy; photon-counting CT; low-field and ultra-high-field MRI.
- Perovskite–silicon tandem solar cells beyond 34% efficiency; quantum sensors in navigation and medicine.

#### How the specialist works here
Translate between disciplines carefully: define the physical model, check that scales and units match the system (cells are wet, warm and noisy; Earth is rotating and stratified), estimate dimensionless groups, and separate established mechanism from active hypothesis.

## Accelerator physics · `knowledge/11-interdisciplinary-physics/accelerator-physics`

#### Overview
About 30 000 accelerators operate worldwide — most for medicine and industry, a few for particle physics and photon science. Accelerator physics combines electrodynamics, Hamiltonian dynamics, nonlinear dynamics, superconductivity and plasma physics to produce bright, stable beams. Strong focusing, synchrotron radiation, beam cooling and free-electron lasing are its signature ideas.

#### Key equations
$$x''+K(s)x=0,\qquad \epsilon=\gamma x^2+2\alpha xx'+\beta x'^2,\qquad B\rho\,[\text{T m}]=3.3356\,p\,[\text{GeV}/c]$$

#### Connections
- [Hadron colliders and the LHC](knowledge/06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc/README.md) · [Plasma wakefield acceleration](knowledge/10-plasma-physics/inertial-and-laser-plasmas/plasma-wakefield-acceleration/README.md) · [Radiation from moving charges](knowledge/02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges/README.md)

### Accelerator technology · `knowledge/11-interdisciplinary-physics/accelerator-physics/accelerator-technology`

**Scope.** Electrostatic and RF acceleration, cyclotrons and synchrocyclotrons, linacs and klystrons, normal-conducting high-gradient structures (CLIC), niobium SRF cavities (quality factors $>10^{10}$, nitrogen doping), Nb–Ti, Nb₃Sn and HTS magnets (LHC 8.3 T, HL-LHC 11–12 T), electron and stochastic cooling, ion sources, medical linacs and proton cyclotrons, industrial irradiation.

**Core ideas.**
- RF cavities provide strong oscillating fields synchronized with bunches; SRF minimizes wall losses.
- Collider energy in a fixed tunnel scales with dipole field — magnet technology sets the frontier.
- Cooling (stochastic, electron) made antiproton physics and W/Z discovery possible.

**Key equations.**
$$Q_0=\frac{\omega U}{P_{\text{loss}}},\qquad E_{\text{acc}}\approx\frac{V}{L},\qquad f_{\text{cyc}}=\frac{qB}{2\pi m}$$

**See also.** [Radiation therapy](knowledge/11-interdisciplinary-physics/medical-physics/radiation-therapy/README.md) · [Superconductivity](knowledge/08-condensed-matter/superconductivity/README.md)

### Beam dynamics · `knowledge/11-interdisciplinary-physics/accelerator-physics/beam-dynamics`

**Scope.** Hill's equation and alternating-gradient focusing, transfer matrices, Twiss (Courant–Snyder) parameters, emittance and Liouville, dispersion and chromaticity, tune and resonance diagrams, dynamic aperture, phase stability and synchrotron oscillations, radiation damping and equilibrium emittance, space charge, beam–beam effects, wakefields and instabilities, beam cooling.

**Core ideas.**
- Alternating focusing and defocusing quadrupoles give net focusing in both planes (strong focusing).
- Emittance is conserved in Hamiltonian motion (Liouville); only damping or cooling reduces it.
- Integer and low-order resonances in the tune diagram must be avoided; nonlinear fields create chaos at large amplitudes.

**Key equations.**
$$x(s)=\sqrt{\epsilon\beta(s)}\cos(\psi(s)+\psi_0),\qquad \psi(s)=\int\frac{ds}{\beta(s)},\qquad mQ_x+nQ_y=p\ (\text{resonance})$$

**See also.** [Hamiltonian mechanics](knowledge/01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics/README.md) · [KAM theory](knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos/README.md)

### Synchrotron and FEL light sources · `knowledge/11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources`

**Scope.** Generations of synchrotron sources, brightness and coherence, undulator equation and harmonics, wiggler vs. undulator ($K$ parameter), multi-bend-achromat rings (MAX IV, ESRF-EBS), SASE FEL physics and the Pierce parameter, X-ray FELs (LCLS, European XFEL, SACLA, SwissFEL), seeding and attosecond X-ray pulses, applications in structural biology and materials.

**Core ideas.**
- Undulators make electrons wiggle coherently, concentrating radiation into narrow harmonics.
- In an FEL the radiation bunches the electrons (microbunching), producing exponential gain and laser-like X-rays.
- Diffraction-limited rings push horizontal emittance toward the X-ray wavelength, boosting coherence.

**Key equations.**
$$\lambda_n=\frac{\lambda_u}{2n\gamma^2}\left(1+\frac{K^2}{2}+\gamma^2\theta^2\right),\qquad K=0.934\,B_0[\text{T}]\,\lambda_u[\text{cm}],\qquad L_G\approx\frac{\lambda_u}{4\pi\sqrt3\rho}$$

**See also.** [Radiation from moving charges](knowledge/02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges/README.md) · [Crystal structure and diffraction](knowledge/08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction/README.md)

## Applied and device physics · `knowledge/11-interdisciplinary-physics/applied-and-device-physics`

#### Overview
From the transistor to the solar cell to the atomic magnetometer, device physics turns fundamental effects into technology. Transistors have shrunk to a few nanometres; silicon solar cells approach their detailed-balance limit while perovskite tandems surpass it; quantum sensors exploit coherence to measure fields, rotation and time with record sensitivity.

#### Key equations
$$\eta_{\text{SQ}}^{\max}\approx33.7\%\ (E_g\approx1.34\ \text{eV}),\qquad ZT=\frac{S^2\sigma T}{\kappa},\qquad \delta B\sim\frac{1}{\gamma\sqrt{NT_2t}}$$

#### Connections
- [Semiconductors](knowledge/08-condensed-matter/crystals-and-electronic-structure/semiconductors/README.md) · [Squeezed light and quantum metrology](knowledge/04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology/README.md) · [Heat engines](knowledge/03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/heat-engines-and-efficiency/README.md)

### Energy materials and thermoelectrics · `knowledge/11-interdisciplinary-physics/applied-and-device-physics/energy-materials-and-thermoelectrics`

**Scope.** Electrochemical potential and open-circuit voltage, intercalation cathodes (LiCoO₂, NMC, LFP), solid-electrolyte interphase, ionic conductivity and solid-state batteries, sodium-ion alternatives, thermoelectric Seebeck and Peltier effects, figure of merit $ZT$, phonon-glass electron-crystal design, nanostructuring to cut thermal conductivity, Wiedemann–Franz trade-offs.

**Core ideas.**
- Cell voltage is the difference in lithium chemical potential between electrodes.
- Good thermoelectrics conduct electricity like crystals but heat like glasses.
- Ion transport in solids is thermally activated hopping — materials design targets low barriers.

**Key equations.**
$$V=-\frac{\mu_{\text{Li}}^{\text{cathode}}-\mu_{\text{Li}}^{\text{anode}}}{e},\qquad \eta_{\text{TE}}^{\max}=\frac{T_h-T_c}{T_h}\frac{\sqrt{1+ZT}-1}{\sqrt{1+ZT}+T_c/T_h}$$

**See also.** [Electronic transport](knowledge/08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics/README.md) · [Phonons](knowledge/08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics/README.md)

### Quantum sensing · `knowledge/11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing`

**Scope.** Ramsey and spin-echo protocols, dynamical decoupling, NV centres in diamond (nanoscale NMR, biological imaging), SERF atomic magnetometers (fT/√Hz, magnetoencephalography), SQUID sensors, atom-interferometric gravimeters, gradiometers and gyroscopes, optical clocks as sensors, quantum-enhanced (squeezed/entangled) sensing, navigation without GPS.

**Core ideas.**
- Phase accumulated by a coherent superposition measures the field: sensitivity improves with coherence time $T_2$ and number of sensors.
- Dynamical decoupling filters noise and selects frequency bands — sensing as spectroscopy.
- Most practical gains come from long coherence and many atoms; entanglement adds a further, smaller boost.

**Key equations.**
$$\phi=\gamma Bt,\qquad \delta B_{\min}\approx\frac{1}{\gamma C\sqrt{\eta\,T_2t}}\ (\text{single NV, Ramsey})$$

**See also.** [Squeezed light and quantum metrology](knowledge/04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology/README.md) · [Atomic clocks](knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement/README.md)

### Semiconductor devices and photovoltaics · `knowledge/11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics`

**Scope.** MOS capacitor and MOSFET operation, threshold voltage, short-channel effects, FinFET and gate-all-around nanosheets, Moore's law and its slowdown, power semiconductors (SiC, GaN), LEDs and efficiency droop, laser diodes, solar-cell I–V curves, fill factor, detailed balance (Shockley–Queisser), silicon PERC/TOPCon/heterojunction cells, perovskite stability, tandem cells (>34%), concentrators.

**Core ideas.**
- A gate voltage creates an inversion channel; subthreshold swing ≥60 mV/decade at room temperature (Boltzmann tyranny).
- Single-junction solar efficiency is limited by thermalization above the gap and transmission below it.
- Stacking junctions with different gaps beats the single-junction limit.

**Key equations.**
$$I_D=\frac{\mu C_{ox}W}{2L}(V_{GS}-V_T)^2\ (\text{saturation}),\qquad S=\ln10\frac{k_BT}{q}\ge60\ \text{mV/dec},\qquad \eta=\frac{FF\,V_{oc}I_{sc}}{P_{\text{in}}}$$

**See also.** [Semiconductors](knowledge/08-condensed-matter/crystals-and-electronic-structure/semiconductors/README.md) · [Heat engines and efficiency](knowledge/03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/heat-engines-and-efficiency/README.md)

## Biophysics · `knowledge/11-interdisciplinary-physics/biophysics`

#### Overview
Living matter operates at energy scales near $k_BT\approx4$ pN·nm, in crowded, fluctuating, far-from-equilibrium conditions. Biophysics uses statistical mechanics, soft-matter physics and precise single-molecule and imaging tools to understand how proteins fold, how motors walk, how membranes bend, how neurons fire and how cells sense and decide — often finding that evolution has pushed systems to physical limits.

#### Key equations
$$k_BT\approx4.1\ \text{pN nm}\approx25.9\ \text{meV}\ (300\ \text{K}),\qquad F=\frac{k_BT}{P}\left[\frac{1}{4(1-x/L)^2}-\frac14+\frac xL\right]\ (\text{worm-like chain})$$

#### Open problems
- Physical principles of intracellular organization (condensates, phase separation).
- How developmental patterning achieves precision despite noise.

#### Connections
- [Soft matter](knowledge/08-condensed-matter/soft-matter/README.md) · [Stochastic thermodynamics](knowledge/03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-thermodynamics-and-fluctuation-theorems/README.md) · [Statistical physics of learning](knowledge/03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/statistical-physics-of-learning/README.md)

### Membranes and cell mechanics · `knowledge/11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics`

**Scope.** Lipid self-assembly, Helfrich bending energy and spontaneous curvature, vesicle shapes and red-blood-cell flicker, membrane tension and pores, ion channels, actin and microtubule networks, active gels, cell crawling and blebbing, traction-force microscopy, mechanosensitive channels (Piezo), tissue fluidity and jamming, cell-scale hydrodynamics.

**Core ideas.**
- Membranes are 2D fluids that resist bending with $\kappa\approx10$–20 $k_BT$.
- The cytoskeleton is an active, non-equilibrium polymer network driven by motors.
- Cells sense stiffness and force — mechanics feeds back on gene expression.

**Key equations.**
$$F_{\text{Helfrich}}=\oint\left[\frac\kappa2(2H-c_0)^2+\bar\kappa K+\sigma\right]dA$$

**Landmark.** Helfrich (1973) — see [subfield landmarks](knowledge/11-interdisciplinary-physics/biophysics/README.md).

**See also.** [Active matter](knowledge/08-condensed-matter/soft-matter/active-matter/README.md) · [Low-Reynolds-number flow](knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics/README.md)

### Molecular biophysics and protein folding · `knowledge/11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding`

**Scope.** Anfinsen's thermodynamic hypothesis, Levinthal paradox, funnelled energy landscapes and minimal frustration, two-state kinetics and φ-value analysis, molecular dynamics of folding (Anton), intrinsically disordered proteins, molecular motors (kinesin, myosin, ATP synthase) and Brownian ratchets, cryo-EM, AlphaFold and protein design.

**Core ideas.**
- Folding is guided by a funnel-shaped landscape, not random search; minimal frustration makes it fast.
- Motors rectify thermal fluctuations using ATP hydrolysis (~20 $k_BT$ per ATP) — efficiency can approach 100% (F₁-ATPase).
- Structure prediction from sequence is now largely solved for single domains; dynamics and function remain hard.

**Key equations.**
$$\Delta G_{\text{fold}}=\Delta H-T\Delta S\sim-5\text{ to }-15\ \text{kcal/mol},\qquad k=k_0e^{-\Delta G^\ddagger/k_BT}$$

**See also.** [Spin glasses (energy landscapes)](knowledge/03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/spin-glasses/README.md) · [Molecular dynamics](knowledge/00-foundations/computational-physics/molecular-dynamics/README.md)

### Physics of living systems · `knowledge/11-interdisciplinary-physics/biophysics/physics-of-living-systems`

**Scope.** Berg–Purcell limit of chemoreception, bacterial chemotaxis, intrinsic and extrinsic noise in gene expression, information theory in signalling, kinetic proofreading, Hodgkin–Huxley and integrate-and-fire neurons, criticality in neural networks, Turing and morphogen-gradient patterning, flocks and swarms, evolution as statistical physics.

**Core ideas.**
- Biological sensing approaches physical limits set by counting statistics of molecules.
- Accuracy costs energy: proofreading spends free energy to beat equilibrium error rates.
- Neurons are excitable nonlinear oscillators; their dynamics are a branch of nonlinear physics.

**Key equations.**
$$\frac{\delta c}{c}\gtrsim\frac{1}{\sqrt{Dac\,\tau}}\ (\text{Berg–Purcell}),\qquad C_m\frac{dV}{dt}=-\sum_ig_i(V-E_i)+I$$

**See also.** [Synchronization and pattern formation](knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation/README.md) · [Entropy and information](knowledge/03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information/README.md)

### Single-molecule biophysics · `knowledge/11-interdisciplinary-physics/biophysics/single-molecule-biophysics`

**Scope.** Optical tweezers (Ashkin, Nobel 2018), magnetic tweezers and torque, AFM force spectroscopy, DNA elasticity and the worm-like chain, overstretching transition, motor stepping with nm/ms resolution, smFRET as a molecular ruler, nanopore sequencing, fluctuation theorems tested with RNA hairpins, super-resolution imaging.

**Core ideas.**
- Ensemble averages hide heterogeneity; single molecules reveal steps, pauses and rare states.
- DNA's persistence length is ~50 nm; at ~65 pN it overstretches.
- FRET efficiency varies as $1/(1+(r/R_0)^6)$, giving distances of 2–10 nm.

**Key equations.**
$$E_{\text{FRET}}=\frac{1}{1+(r/R_0)^6},\qquad \kappa_{\text{trap}}\langle x^2\rangle=k_BT$$

**See also.** [Laser cooling and trapping (optical tweezers)](knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/laser-cooling-and-trapping/README.md) · [Fluctuation theorems](knowledge/03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-thermodynamics-and-fluctuation-theorems/README.md)

## Chemical physics · `knowledge/11-interdisciplinary-physics/chemical-physics`

#### Overview
Chemistry is the quantum mechanics of electrons and nuclei. The Born–Oppenheimer approximation separates fast electrons from slow nuclei, yielding potential energy surfaces on which reactions occur. Spectroscopy reads out molecular energy levels; quantum chemistry computes them; reaction dynamics follows nuclei over barriers (now in real time with femtosecond lasers); surface science explains catalysis atom by atom.

#### Key equations
$$\left[\hat T_e+V(\mathbf r;\mathbf R)\right]\psi_n=E_n(\mathbf R)\psi_n,\qquad k(T)=\frac{k_BT}{h}e^{-\Delta G^\ddagger/k_BT}\ (\text{Eyring})$$

#### Connections
- [Atomic structure and spectroscopy](knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy/README.md) · [Density functional theory](knowledge/08-condensed-matter/crystals-and-electronic-structure/density-functional-theory/README.md) · [Ultracold molecules](knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/ultracold-molecules/README.md)

### Molecular spectroscopy · `knowledge/11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy`

**Scope.** Rigid and non-rigid rotors, microwave spectra, harmonic and anharmonic vibrations (Morse), IR selection rules, rotation–vibration bands (P, Q, R branches), Raman selection rules and mutual exclusion, electronic transitions and Franck–Condon factors, fluorescence and phosphorescence, NMR and EPR, 2D IR/electronic spectroscopy, astrochemistry and atmospheric remote sensing.

**Core ideas.**
- Energy scales separate: electronic (eV) ≫ vibrational (0.1 eV) ≫ rotational (meV).
- IR activity needs a changing dipole moment; Raman activity needs a changing polarizability.
- Franck–Condon: electronic transitions are vertical — nuclei don't move during photon absorption.

**Key equations.**
$$E_J=BJ(J+1),\ B=\frac{\hbar^2}{2I};\qquad E_v=\hbar\omega\left(v+\tfrac12\right)-\hbar\omega x_e\left(v+\tfrac12\right)^2$$

**Landmark.** Raman & Krishnan (1928) — see [subfield landmarks](knowledge/11-interdisciplinary-physics/chemical-physics/README.md).

**See also.** [Atomic spectroscopy](knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy/README.md) · [Exoplanet atmospheres](knowledge/09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-atmospheres/README.md)

### Quantum chemistry methods · `knowledge/11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods`

**Scope.** Hartree–Fock and Roothaan–Hall equations, Gaussian basis sets and basis-set extrapolation, electron correlation, MP2, CI and full CI, coupled cluster (CCSD, CCSD(T) "gold standard"), multireference methods (CASSCF, CASPT2), DFT in chemistry, explicitly correlated F12 methods, local correlation, quantum Monte Carlo, quantum algorithms (VQE, phase estimation) for chemistry.

**Core ideas.**
- Hartree–Fock gives ~99% of the energy; the missing correlation energy determines chemistry.
- CCSD(T) achieves ~1 kcal/mol accuracy for single-reference molecules at $\mathcal O(N^7)$ cost.
- Strong correlation (bond breaking, transition metals) needs multireference methods — a target for quantum computers.

**Key equations.**
$$|\Psi_{CC}\rangle=e^{\hat T}|\Phi_0\rangle,\ \hat T=\hat T_1+\hat T_2+\cdots;\qquad E_{\text{corr}}=E_{\text{exact}}-E_{\text{HF}}$$

**See also.** [Approximation methods in QM](knowledge/04-quantum-physics/quantum-mechanics-core/approximation-methods/README.md) · [Ab initio nuclear theory](knowledge/07-nuclear-physics/nuclear-structure/ab-initio-nuclear-theory/README.md)

### Reaction dynamics · `knowledge/11-interdisciplinary-physics/chemical-physics/reaction-dynamics`

**Scope.** Arrhenius and Eyring rate laws, transition-state theory and its corrections (tunnelling, recrossing), RRKM unimolecular theory, Kramers theory in solution, Marcus theory and the inverted region, crossed-molecular-beam experiments, state-to-state dynamics, non-adiabatic dynamics and conical intersections, femtosecond pump–probe, ultracold and quantum-controlled chemistry.

**Core ideas.**
- Rates are set by the free-energy barrier and the attempt frequency; tunnelling matters for light atoms.
- Marcus: electron-transfer rate is maximal when driving force equals reorganization energy, then falls (inverted region).
- Conical intersections funnel excited molecules back to the ground state in femtoseconds (vision, DNA photostability).

**Key equations.**
$$k_{ET}=\frac{2\pi}{\hbar}|H_{AB}|^2\frac{1}{\sqrt{4\pi\lambda k_BT}}\exp\!\left[-\frac{(\Delta G^\circ+\lambda)^2}{4\lambda k_BT}\right]$$

**See also.** [Stochastic processes (Kramers escape)](knowledge/03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics/README.md) · [Ultrafast optics](knowledge/02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics/README.md)

### Surface science and catalysis · `knowledge/11-interdisciplinary-physics/chemical-physics/surface-science-and-catalysis`

**Scope.** Ultra-high vacuum methods, LEED, XPS and photoemission, surface reconstruction, physisorption vs. chemisorption, Langmuir isotherms, Langmuir–Hinshelwood kinetics, STM and AFM (atomic imaging and manipulation), Haber–Bosch and Ertl's mechanisms, Sabatier principle and volcano plots, d-band model, single-atom catalysts, electrocatalysis for hydrogen and CO₂ reduction.

**Core ideas.**
- STM current depends exponentially on tip–sample distance — single-atom resolution.
- Catalysts work best at intermediate adsorption strength (Sabatier) — the volcano plot.
- DFT-computed descriptors now guide catalyst discovery.

**Key equations.**
$$\theta=\frac{KP}{1+KP}\ (\text{Langmuir}),\qquad I\propto Ve^{-2\kappa d},\ \kappa=\frac{\sqrt{2m\phi}}{\hbar}$$

**See also.** [Exactly solvable systems (tunnelling)](knowledge/04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems/README.md) · [Plasma processing](knowledge/10-plasma-physics/low-temperature-and-applied-plasmas/plasma-discharges-and-processing/README.md)

## Earth, atmosphere and climate physics · `knowledge/11-interdisciplinary-physics/earth-atmosphere-and-climate-physics`

#### Overview
Earth is a rotating, stratified, radiatively forced fluid system wrapped around a convecting solid interior. Its climate is set by the balance of absorbed sunlight and emitted infrared; greenhouse gases reduce outgoing infrared and warm the surface. Rotation and stratification organize weather and ocean currents; seismic waves image the interior; the liquid outer core generates the magnetic field.

#### Key equations
$$\frac{S_0}{4}(1-\alpha)=\sigma T_e^4\Rightarrow T_e\approx255\ \text{K},\qquad \Delta F=5.35\ln\frac{C}{C_0}\ \text{W m}^{-2},\qquad \Delta T_{\text{eq}}=\frac{\Delta F}{\lambda}$$

#### Open problems
- Cloud feedbacks — the largest source of spread in climate sensitivity.
- Stability of the AMOC and ice sheets (tipping points).

#### Connections
- [Deterministic chaos (Lorenz)](knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos/README.md) · [Non-inertial frames](knowledge/01-classical-mechanics/newtonian-mechanics/non-inertial-frames/README.md) · [Dynamo theory](knowledge/10-plasma-physics/magnetohydrodynamics/dynamo-theory/README.md)

### Atmospheric dynamics · `knowledge/11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics`

**Scope.** Hydrostatic and geostrophic balance, thermal wind, Rossby number and deformation radius, potential vorticity, Rossby waves, baroclinic instability and mid-latitude storms, Hadley/Ferrel/polar cells, jet streams, moist convection and CAPE, numerical weather prediction and data assimilation, predictability limits (~2 weeks), ML weather models.

**Core ideas.**
- At large scales, pressure-gradient and Coriolis forces balance: winds blow along isobars.
- Baroclinic instability converts the equator-to-pole temperature gradient into weather systems.
- Chaos limits deterministic forecasts to about two weeks; ensembles quantify uncertainty.

**Key equations.**
$$f\hat{\mathbf z}\times\mathbf u_g=-\frac1\rho\nabla p,\quad f=2\Omega\sin\phi,\qquad Ro=\frac{U}{fL},\qquad c_{\text{Rossby}}=-\frac{\beta}{k^2+l^2}$$

**Landmark.** Charney, Fjörtoft & von Neumann (1950) — see [subfield landmarks](knowledge/11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/README.md).

**See also.** [Non-inertial frames](knowledge/01-classical-mechanics/newtonian-mechanics/non-inertial-frames/README.md) · [Turbulence (2D)](knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/turbulence/README.md)

### Climate physics and radiative forcing · `knowledge/11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing`

**Scope.** Radiative transfer and band saturation (logarithmic CO₂ forcing), effective radiating level, radiative–convective equilibrium, feedback parameters, equilibrium and transient climate sensitivity (IPCC AR6 likely 2.5–4 K), ocean heat uptake, aerosols, paleoclimate constraints, energy imbalance (~1 W m⁻²), Hasselmann stochastic climate model, detection and attribution, climate models (CMIP6).

**Core ideas.**
- CO₂ raises the effective emission level to colder altitudes, reducing outgoing longwave radiation.
- Doubling CO₂ gives ~3.9 W m⁻² forcing; feedbacks amplify the no-feedback ~1.2 K warming to ~3 K.
- Fast weather noise integrated by a slow ocean produces red-noise climate variability (Hasselmann).

**Key equations.**
$$C\frac{dT}{dt}=\Delta F-\lambda\Delta T+\xi(t),\qquad \text{ECS}=\frac{F_{2\times}}{\lambda}\approx\frac{3.9}{1.3}\approx3\ \text{K}$$

**See also.** [Quantum statistics (blackbody)](knowledge/03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics/README.md) · [Exoplanet atmospheres](knowledge/09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-atmospheres/README.md)

### Ocean physics · `knowledge/11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics`

**Scope.** Ekman transport and pumping, Sverdrup balance, western intensification (Gulf Stream), thermohaline circulation and Stommel's bistability, AMOC monitoring (RAPID array) and weakening debate, mesoscale eddies, internal waves and mixing, surface gravity waves and tsunamis, tides, ENSO dynamics, ocean heat content and sea-level rise.

**Core ideas.**
- Wind stress plus rotation drives transport at right angles to the wind (Ekman).
- The β-effect concentrates return flow into narrow, fast western boundary currents.
- Salt–temperature feedbacks allow multiple equilibria of overturning — a potential tipping point.

**Key equations.**
$$\beta V=\frac{1}{\rho_0}\hat{\mathbf z}\cdot\nabla\times\boldsymbol\tau\ (\text{Sverdrup}),\qquad c=\sqrt{gh}\ (\text{shallow-water waves})$$

**See also.** [Bifurcations and tipping points](knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/bifurcations-and-routes-to-chaos/README.md) · [Mechanical waves](knowledge/01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics/README.md)

### Seismology and Earth's interior · `knowledge/11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior`

**Scope.** Body waves (P, S) and surface waves (Love, Rayleigh), ray paths and travel-time curves, discovery of the core (Oldham, Gutenberg) and inner core (Lehmann 1936), PREM, seismic tomography of slabs and plumes, normal modes of the Earth, earthquake source mechanics and Gutenberg–Richter law, mantle convection and plate tectonics, geodynamo simulations and reversals.

**Core ideas.**
- The S-wave shadow proves the outer core is liquid; refracted P waves revealed a solid inner core.
- Earthquake magnitudes follow a power law: $\log_{10}N=a-bM$, $b\approx1$.
- Convection in the liquid iron outer core sustains Earth's magnetic field.

**Key equations.**
$$v_P=\sqrt{\frac{K+\frac43\mu}{\rho}},\ v_S=\sqrt{\frac\mu\rho},\qquad M_w=\tfrac23\log_{10}M_0-6.07\ (M_0\ \text{in N m})$$

**See also.** [Elasticity](knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/elasticity/README.md) · [Dynamo theory](knowledge/10-plasma-physics/magnetohydrodynamics/dynamo-theory/README.md)

## Medical physics · `knowledge/11-interdisciplinary-physics/medical-physics`

#### Overview
Medical physics turns nearly every branch of physics into clinical tools: X-ray attenuation (radiography, CT), nuclear spin precession (MRI), positron annihilation (PET), acoustics (ultrasound), light scattering (OCT), and ionizing radiation dosimetry for cancer therapy. Safety — dose limits, specific absorption rate, quality assurance — is integral to the discipline.

#### Key equations
$$I=I_0e^{-\int\mu\,dl},\qquad \omega_0=\gamma B_0,\ \frac{\gamma}{2\pi}=42.58\ \text{MHz/T}\ (^1\text{H}),\qquad \text{HU}=1000\frac{\mu-\mu_w}{\mu_w}$$

#### Open problems
- Mechanism of the FLASH effect; adaptive and MR-guided radiotherapy.
- Dose reduction in CT (photon-counting detectors, AI reconstruction) without loss of diagnostic value.

#### Connections
- [Radiation detection and dosimetry](knowledge/07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry/README.md) · [Nuclear data and isotopes](knowledge/07-nuclear-physics/applied-nuclear-physics/nuclear-data-and-isotope-production/README.md) · [Fourier optics and imaging](knowledge/02-electromagnetism-and-optics/classical-optics/fourier-optics-and-imaging/README.md)

### Medical imaging · `knowledge/11-interdisciplinary-physics/medical-physics/medical-imaging`

**Scope.** X-ray production and spectra, attenuation and contrast, CT acquisition and filtered back-projection, iterative and deep-learning reconstruction, photon-counting CT, NMR physics (precession, T1/T2 relaxation, spin echo), MRI gradients and k-space, pulse sequences, BOLD fMRI and diffusion MRI, SNR and resolution, patient dose and SAR.

**Core ideas.**
- CT reconstructs attenuation maps from line integrals — the Radon transform inverted.
- MRI encodes position in precession frequency via field gradients; images are Fourier transforms of k-space data.
- Contrast comes from relaxation-time differences between tissues, not density.

**Key equations.**
$$p(\theta,s)=\int\mu(x,y)\,\delta(x\cos\theta+y\sin\theta-s)\,dx\,dy,\qquad M_z(t)=M_0\left(1-e^{-t/T_1}\right),\quad M_{xy}(t)=M_0e^{-t/T_2}$$

**See also.** [Fourier optics](knowledge/02-electromagnetism-and-optics/classical-optics/fourier-optics-and-imaging/README.md) · [Angular momentum and spin](knowledge/04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin/README.md)

### Nuclear medicine and PET · `knowledge/11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet`

**Scope.** Tracer principle, ⁹⁹ᵐTc gamma cameras and collimators, SPECT, positron annihilation and coincidence detection, scintillators (LSO/LYSO), time-of-flight PET, total-body PET (EXPLORER), PET/CT and PET/MRI, ¹⁸F-FDG metabolism imaging, quantitative SUV, radioligand therapy (¹⁷⁷Lu-PSMA, ²²⁵Ac), dosimetry.

**Core ideas.**
- Two back-to-back 511 keV photons define a line of response; coincidences localize annihilations.
- Time-of-flight (~200 ps) localizes along the line to ~3 cm, improving SNR.
- Same targeting molecule can carry imaging or therapeutic isotopes (theranostics).

**Key equations.**
$$e^++e^-\to2\gamma\ (511\ \text{keV each}),\qquad \Delta x=\frac{c\,\Delta t}{2}$$

**Landmark.** Ter-Pogossian et al. (1975) — see [subfield landmarks](knowledge/11-interdisciplinary-physics/medical-physics/README.md).

**See also.** [Nuclear data and isotope production](knowledge/07-nuclear-physics/applied-nuclear-physics/nuclear-data-and-isotope-production/README.md) · [Radiation detection](knowledge/07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry/README.md)

### Radiation therapy · `knowledge/11-interdisciplinary-physics/medical-physics/radiation-therapy`

**Scope.** Linear accelerators and megavoltage beams, depth–dose curves and build-up, IMRT and VMAT, stereotactic radiosurgery, brachytherapy, proton and heavy-ion therapy (Bragg peak, range uncertainty, RBE), linear–quadratic radiobiology, fractionation, Monte Carlo dose calculation, MR-linacs, ultra-high-dose-rate FLASH.

**Core ideas.**
- Charged particles deposit most energy at the end of their range (Bragg peak), sparing tissue beyond the tumour.
- Fractionation exploits differential repair between normal tissue and tumour (α/β ratios).
- Dose delivery uncertainty of a few percent matters clinically — QA is central.

**Key equations.**
$$S=e^{-(\alpha D+\beta D^2)},\qquad \text{BED}=nd\left(1+\frac{d}{\alpha/\beta}\right),\qquad R_{\text{CSDA}}\approx0.0022\,E^{1.77}\ \text{cm}\ (\text{protons in water, MeV})$$

**See also.** [Radiation detection and dosimetry](knowledge/07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry/README.md) · [Accelerator technology](knowledge/11-interdisciplinary-physics/accelerator-physics/accelerator-technology/README.md)

### Ultrasound and biomedical optics · `knowledge/11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics`

**Scope.** Piezoelectric transducers, acoustic impedance and reflection, attenuation (~0.5 dB/cm/MHz), resolution vs. penetration, beamforming and phased arrays, Doppler and colour flow, elastography, HIFU therapy, OCT (time and Fourier domain), photoacoustic tomography, diffuse optical tomography and near-infrared spectroscopy, tissue optical windows.

**Core ideas.**
- Echo timing gives depth: $z=ct/2$ with $c\approx1540$ m/s in soft tissue.
- Higher frequency → better resolution but stronger attenuation.
- OCT is low-coherence interferometry: axial resolution set by source bandwidth, ~μm.

**Key equations.**
$$f_D=\frac{2f_0v\cos\theta}{c},\qquad \Delta z_{\text{OCT}}=\frac{2\ln2}{\pi}\frac{\lambda_0^2}{\Delta\lambda}$$

**Landmark.** Huang et al. (1991) — see [subfield landmarks](knowledge/11-interdisciplinary-physics/medical-physics/README.md).

**See also.** [Mechanical waves and acoustics](knowledge/01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics/README.md) · [Coherence and statistical optics](knowledge/02-electromagnetism-and-optics/classical-optics/coherence-and-statistical-optics/README.md)


---

# Packet 11-1 (100 records)

{"id": "C0429", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "name": "ML structure prediction and neural force fields", "kind": "method transfer", "summary": "Deep networks predict protein structure from sequence and learn machine-learned potentials for MD, replacing explicit physics with learned surrogates trained on data.", "map": "", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0430", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "ML weather emulators", "kind": "method transfer", "summary": "Neural surrogates trained on reanalysis now match or beat numerical weather prediction at medium range at far lower cost, replacing PDE integration with learned dynamics.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0431", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "11-interdisciplinary-physics/applied-and-device-physics/energy-materials-and-thermoelectrics", "name": "MD of ion transport in electrolytes", "kind": "method transfer", "summary": "MD, including machine-learned potentials, computes ionic conductivity and diffusion in solid electrolytes and battery materials.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0432", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "name": "MD simulation of protein folding and dynamics", "kind": "method transfer", "summary": "Force-field molecular dynamics, enhanced sampling and specialised hardware are used to simulate folding, binding and conformational change of proteins, connecting folding landscapes to integrated equations of motion.", "map": "m\\ddot{\\mathbf r}_i=-\\nabla_i U(\\{\\mathbf r\\})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0433", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "name": "Protein folding as a test case for MD", "kind": "shared object", "summary": "Folding timescales and force-field accuracy drive MD development (thermostats, enhanced sampling), while MD supplies atomistic folding pathways that test energy-landscape theory.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0434", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Trajectories on potential energy surfaces", "kind": "method transfer", "summary": "Classical and ab initio MD trajectories sample reactive events, test transition-state theory and recrossing, and give rate constants via rare-event methods.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0435", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "11-interdisciplinary-physics/chemical-physics/surface-science-and-catalysis", "name": "Ab initio MD of surfaces and catalysis", "kind": "method transfer", "summary": "DFT-based MD and kinetic Monte Carlo model adsorption, diffusion and reactions on catalyst surfaces.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0436", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "Monte Carlo simulation of PET and SPECT", "kind": "method transfer", "summary": "Monte Carlo photon transport (GATE, GEANT4) models scatter, attenuation and detector response, used for system design and image correction in emission tomography.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0437", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "11-interdisciplinary-physics/medical-physics/radiation-therapy", "name": "Monte Carlo dose calculation", "kind": "method transfer", "summary": "Metropolis-era stochastic sampling of particle transport is the gold standard for dose calculation in photon and proton therapy, tracking showers event by event.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0438", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Symplectic tracking of beams", "kind": "method transfer", "summary": "Long-term particle tracking in rings uses symplectic integrators to preserve phase-space structure over billions of turns, as in celestial mechanics.", "map": "\\mathbf z_{n+1}=M(\\mathbf z_n),\\; M^TJM=J", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0439", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Numerical weather and climate models", "kind": "method transfer", "summary": "Weather and climate models discretise the primitive equations with finite-volume, spectral and semi-implicit schemes; numerical stability and conservation properties are central, and chaos limits predictability.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0440", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics", "name": "Ocean general circulation modelling", "kind": "method transfer", "summary": "Ocean models rely on finite-volume/difference solvers for stratified rotating flow; numerical diffusion and resolution of eddies control simulated heat uptake and AMOC.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0441", "a": "00-foundations/computational-physics/tensor-network-methods", "b": "11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods", "name": "DMRG for strongly correlated molecules", "kind": "method transfer", "summary": "DMRG, developed for 1D spin chains, was adapted to quantum chemistry as a multireference method for active spaces of transition-metal and other strongly correlated molecules.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0442", "a": "00-foundations/computational-physics/tensor-network-methods", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "MCTDH and tensor-train wavepackets", "kind": "method transfer", "summary": "Multilayer MCTDH for quantum nuclear dynamics on potential energy surfaces is a hierarchical tensor decomposition equivalent to tree tensor networks.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0443", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Fourier transform: k-space MRI and Radon slice", "kind": "identity", "summary": "MRI data are samples of the Fourier transform of magnetisation (k-space) and CT sinograms relate to it via the Fourier slice theorem, so image formation is Fourier analysis.", "map": "S(\\mathbf k)=\\int \\rho(\\mathbf r)e^{-i\\mathbf k\\cdot\\mathbf r}d^3r", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0444", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Wave equation and Green's functions in seismology", "kind": "mechanism", "summary": "Seismic wavefields are solved as elastic wave equation with Green's functions; source inversion and ambient-noise correlation recover the Green's function between stations.", "map": "\\rho\\ddot u_i=\\partial_j(c_{ijkl}\\partial_k u_l)+f_i", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0445", "a": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Inverse problems in tomographic reconstruction", "kind": "method transfer", "summary": "CT reconstruction (filtered back-projection, iterative, regularised) is a linear inverse problem solved with Fourier slice theorem, SVD and regularisation.", "map": "g=Af,\\; \\hat f=\\arg\\min\\|Af-g\\|^2+\\lambda R(f)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0446", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "name": "Differential geometry of membranes", "kind": "mechanism", "summary": "Membrane shapes are surfaces whose mean and Gaussian curvature enter the Helfrich bending energy; Gauss–Bonnet makes topology constrain vesicle shape.", "map": "E=\\int\\frac{\\kappa}{2}(2H-c_0)^2+\\bar\\kappa K\\,dA", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0447", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Noise limits and lock-in detection", "kind": "shared object", "summary": "Lock-in detection, shot-noise and thermal-noise limits govern SQUIDs, NV magnetometers and atomic sensors alike.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0448", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "Scintillators and photodetectors in PET", "kind": "shared object", "summary": "Scintillator crystals, SiPMs and fast timing electronics from particle detectors underpin gamma cameras and time-of-flight PET, with noise and timing resolution as the figures of merit.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0449", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "name": "Statistical inference for single-molecule traces", "kind": "method transfer", "summary": "Hidden Markov models, maximum likelihood and Bayesian change-point analysis extract states and rates from noisy FRET and tweezer trajectories.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0450", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Detection and attribution as inference", "kind": "method transfer", "summary": "Climate detection and attribution applies optimal fingerprinting, regression and Bayesian inference to separate forced signal from internal variability, analogous to discovery claims in particle physics.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0451", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Point groups and selection rules", "kind": "mechanism", "summary": "Group representations of molecular point groups and SO(3) determine which vibrational, rotational and electronic transitions are allowed in IR, Raman and electronic spectra.", "map": "\\Gamma_i\\otimes\\Gamma_\\mu\\otimes\\Gamma_f\\ni A_1", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0452", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods", "name": "Symmetry adaptation in electronic structure", "kind": "method transfer", "summary": "Spin and spatial point-group symmetry classify molecular states and reduce cost of Hartree–Fock, CI and coupled-cluster calculations.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0453", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Liouville and Courant–Snyder invariants", "kind": "mechanism", "summary": "Hamiltonian phase-space structure gives conserved emittance and Courant–Snyder invariant for linear optics, with symplectic maps constraining beam evolution; damping breaks it.", "map": "\\gamma x^2+2\\alpha xx'+\\beta x'^2=\\varepsilon", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0454", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "name": "Symmetry breaking in developmental patterning", "kind": "analogy", "summary": "Turing-type instabilities and polarity establishment in cells resemble symmetry-breaking bifurcations with order parameters and Goldstone-like soft modes in active matter.", "map": "", "breaks": "Living systems are driven, non-equilibrium and finite, with no true Goldstone theorem or thermodynamic limit.", "confidence": "current research", "strength": 2}
{"id": "C0455", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "name": "Scaling laws in cell and membrane mechanics", "kind": "method transfer", "summary": "Dimensional analysis and scaling fix the bending-rigidity length scales, low-Reynolds-number motility and size dependence of cell mechanics.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0456", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Nondimensional numbers in geophysical flow", "kind": "method transfer", "summary": "Rossby, Ekman, Richardson and Reynolds numbers from Buckingham-π analysis identify the regimes of rotating stratified flow, justifying geostrophic and quasi-geostrophic approximations.", "map": "\\mathrm{Ro}=\\frac{U}{fL}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0457", "a": "00-foundations/units-and-constants/si-units-and-2019-redefinition", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Quantum standards realise SI units", "kind": "shared object", "summary": "Josephson and quantum Hall effects realise volt and ohm via h and e; atomic clocks and atom interferometers tie units to invariants of nature.", "map": "V=\\frac{nf}{K_J},\\; K_J=\\frac{2e}{h}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0853", "a": "01-classical-mechanics/analytical-mechanics/canonical-transformations-and-hamilton-jacobi", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Action–angle variables and Courant–Snyder invariant", "kind": "identity", "summary": "The Courant–Snyder transform is a canonical change to action–angle variables for linear betatron motion. The invariant is the action J and the phase advance is the angle.", "map": "2J=\\gamma x^2+2\\alpha xx'+\\beta x'^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0854", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Beam optics as Hamiltonian flow", "kind": "identity", "summary": "Particle motion in accelerators is Hamiltonian, so Liouville's theorem makes emittance conserved. Linear transfer maps are symplectic and Twiss parameters follow from them.", "map": "M^T J M=J,\\;\\epsilon=\\sqrt{\\langle x^2\\rangle\\langle x'^2\\rangle-\\langle xx'\\rangle^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0855", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Classical trajectories and phase-space transition states", "kind": "method transfer", "summary": "Reaction rates are computed from classical Hamiltonian trajectories on potential energy surfaces, and transition-state theory uses phase-space dividing surfaces and invariant manifolds.", "map": "k_{TST}=\\tfrac{k_BT}{h}e^{-\\Delta G^\\ddagger/k_BT}", "breaks": "Tunnelling and non-adiabatic effects need quantum treatment.", "confidence": "established", "strength": 2}
{"id": "C0856", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Hamiltonian treatment of spin dynamics in MRI", "kind": "analogy", "summary": "Spin motion in a magnetic field maps onto a rotating-frame equation that parallels the rigid-body rotation formalism, which is used in pulse sequence design.", "map": "\\dot{\\mathbf M}=\\gamma\\mathbf M\\times\\mathbf B", "breaks": "Relaxation makes the dynamics dissipative, so phase-space volume is not conserved.", "confidence": "established", "strength": 1}
{"id": "C0857", "a": "01-classical-mechanics/analytical-mechanics/variational-principles", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Fermat principle and seismic ray tracing", "kind": "method transfer", "summary": "Seismic travel-time tomography uses Fermat's principle and Snell's law to trace rays through velocity models, with the ray parameter conserved in a spherical Earth.", "map": "p=r\\sin i/v", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0858", "a": "01-classical-mechanics/analytical-mechanics/variational-principles", "b": "11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics", "name": "Fermat's principle in ray-based imaging", "kind": "method transfer", "summary": "Fermat's principle gives ray paths through tissue and in the Earth, used in travel-time and ray-based reconstruction. It underlies delay-and-sum beamforming and sound-speed estimation.", "map": "\\delta\\int n\\,ds=0", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C0859", "a": "01-classical-mechanics/continuum-and-fluid-mechanics", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Navier–Stokes to geophysical fluid dynamics", "kind": "identity", "summary": "Atmospheric dynamics is the Navier–Stokes/Euler system on a rotating, stratified sphere, with the Boussinesq and hydrostatic approximations and geostrophic balance as reductions.", "map": "\\partial_t \\mathbf{u}+\\mathbf{u}\\cdot\\nabla\\mathbf{u}+2\\boldsymbol\\Omega\\times\\mathbf{u}=-\\nabla p/\\rho+\\mathbf{g}+\\nu\\nabla^2\\mathbf{u}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0860", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "name": "Helfrich bending elasticity of membranes", "kind": "mechanism", "summary": "Membrane bending energy is the thin-shell elasticity of plates adapted to fluid bilayers, with curvature energy governing vesicle shapes and buckling-like transitions.", "map": "E=\\tfrac{\\kappa}{2}\\int(2H-c_0)^2dA", "breaks": "The bilayer is a 2D fluid with no shear modulus, unlike solid plates.", "confidence": "established", "strength": 2}
{"id": "C0861", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Earth as an elastic body", "kind": "shared object", "summary": "Seismic waves, free oscillations and mantle stress response use linear elasticity, with viscoelastic extension for postglacial rebound.", "map": "\\rho\\ddot u_i=\\partial_j\\sigma_{ij},\\;\\sigma_{ij}=C_{ijkl}\\varepsilon_{kl}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0862", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Elastic moduli and seismic wave speeds", "kind": "identity", "summary": "Seismic P and S wave speeds follow from the Lamé constants and density of the elastic wave equation. Tomography inverts them to map Earth's interior.", "map": "v_P=\\sqrt{(\\lambda+2\\mu)/\\rho},\\; v_S=\\sqrt{\\mu/\\rho}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0863", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics", "name": "Elastography: tissue stiffness from shear waves", "kind": "method transfer", "summary": "Shear wave elastography measures shear wave speed in tissue to infer the shear modulus, an inverse problem in linear elasticity used to detect tumours and fibrosis.", "map": "\\mu=\\rho c_s^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0864", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics", "name": "Ocean circulation as rotating viscous flow", "kind": "shared object", "summary": "Ekman layers, boundary-layer theory and vorticity dynamics explain wind-driven gyres and western boundary intensification (Stommel and Munk).", "map": "\\beta v=\\tfrac{1}{\\rho}\\hat z\\cdot\\nabla\\times\\boldsymbol\\tau", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0865", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "name": "Plateau–Rayleigh and membrane shape instabilities", "kind": "analogy", "summary": "Surface-tension-driven pearling and tubulation of lipid tubes echo the Plateau–Rayleigh instability, with bending rigidity and membrane tension setting the selected wavelength.", "map": "\\lambda\\sim 2\\pi\\sqrt{\\kappa/\\sigma}", "breaks": "Membranes have bending elasticity and fixed area, unlike simple liquid jets.", "confidence": "current research", "strength": 1}
{"id": "C0866", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Convective instability in the atmosphere", "kind": "mechanism", "summary": "Moist and dry convection and the Rayleigh–Bénard/Lorenz system share a buoyancy-driven instability criterion. Brunt–Väisälä frequency marks stratified stability.", "map": "N^2=-\\tfrac{g}{\\rho}\\tfrac{d\\rho}{dz}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0867", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Mantle convection and the geodynamo", "kind": "shared object", "summary": "Rayleigh–Bénard convection with a Rayleigh-number threshold describes mantle convection driving plate tectonics, and rotating convection in the outer core drives the geodynamo.", "map": "Ra=g\\alpha\\Delta T d^3/(\\nu\\kappa)", "breaks": "Mantle viscosity is strongly temperature-dependent and non-Newtonian, and the core also needs magnetic and rotational effects.", "confidence": "established", "strength": 2}
{"id": "C0868", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics", "b": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "name": "Cell mechanics and viscous microhydrodynamics", "kind": "shared object", "summary": "Vesicle dynamics, cytoplasmic flow and cell crawling combine membrane elasticity with viscous Stokes flow. Dimensionless numbers such as the capillary number control deformation.", "map": "Ca=\\eta\\dot\\gamma R/\\sigma", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0869", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics", "b": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "name": "Stokes flow in cells and membranes", "kind": "shared object", "summary": "Cell motility, cytoplasmic and membrane flows occur at very low Reynolds number. Membrane hydrodynamics (Saffman–Delbrück) and swimming under time-reversal constraints use Stokes flow.", "map": "\\eta\\nabla^2\\mathbf{u}=\\nabla p,\\;\\nabla\\cdot\\mathbf{u}=0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0870", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics", "b": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "name": "Overdamped dynamics and Stokes drag in tweezers", "kind": "shared object", "summary": "Optical and magnetic tweezers experiments operate at low Reynolds number, where Stokes drag on beads sets the calibration and fluctuation-dissipation relations.", "map": "\\gamma=6\\pi\\eta a,\\; D=k_BT/\\gamma", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0871", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Atmospheric turbulence and cascades", "kind": "shared object", "summary": "The atmosphere shows a 3D Kolmogorov cascade at small scales and a quasi-2D inverse energy cascade at synoptic scales. Eddy fluxes need closure in models.", "map": "E(k)\\sim\\varepsilon^{2/3}k^{-5/3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0872", "a": "01-classical-mechanics/newtonian-mechanics/central-forces-and-orbits", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Rutherford scattering and molecular beam collisions", "kind": "method transfer", "summary": "Classical central-force scattering with impact parameter and deflection function underlies crossed-molecular-beam analysis, including rainbow and glory scattering.", "map": "\\Theta(b)=\\pi-2\\int\\frac{b\\,dr/r^2}{\\sqrt{1-b^2/r^2-V/E}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0873", "a": "01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Resonances and N-body methods in accelerators", "kind": "method transfer", "summary": "Resonance overlap, secular perturbation theory and symplectic integrators from celestial mechanics are used for accelerator tracking and long-term stability. Space-charge tracking is an N-body problem.", "map": "\\nu_x m+\\nu_y n=p", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0874", "a": "01-classical-mechanics/newtonian-mechanics/non-inertial-frames", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics", "name": "Rotating-frame physics of the planet", "kind": "mechanism", "summary": "Earth-system flows are best described in the rotating frame. Coriolis effects shape circulation, ocean gyres and inertial oscillations.", "map": "\\mathbf{a}_{rot}=\\mathbf{a}-2\\boldsymbol\\Omega\\times\\mathbf{v}-\\boldsymbol\\Omega\\times(\\boldsymbol\\Omega\\times\\mathbf{r})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0875", "a": "01-classical-mechanics/newtonian-mechanics/non-inertial-frames", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Coriolis force and geostrophic balance", "kind": "mechanism", "summary": "The Coriolis force from Earth's rotation balances pressure gradients to give geostrophic wind and drives cyclone rotation and Rossby waves.", "map": "f\\,\\hat z\\times\\mathbf{u}_g=-\\nabla p/\\rho,\\; f=2\\Omega\\sin\\phi", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0876", "a": "01-classical-mechanics/newtonian-mechanics/non-inertial-frames", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Rossby waves from the beta effect", "kind": "mechanism", "summary": "The variation of the Coriolis parameter with latitude gives a restoring mechanism for planetary Rossby waves and westward phase propagation.", "map": "\\omega=Uk-\\beta k/(k^2+l^2)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0877", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/bifurcations-and-routes-to-chaos", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Tipping points as bifurcations", "kind": "analogy", "summary": "Climate tipping elements (ice-albedo, AMOC) are modelled as saddle-node bifurcations with hysteresis in energy-balance models. Early-warning signals come from critical slowing down.", "map": "C\\dot T=S(1-\\alpha(T))/4-\\epsilon\\sigma T^4", "breaks": "Real climate is forced, noisy and non-autonomous, so rate-induced tipping happens without a classical bifurcation.", "confidence": "current research", "strength": 2}
{"id": "C0878", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/bifurcations-and-routes-to-chaos", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics", "name": "AMOC bistability (Stommel model)", "kind": "mechanism", "summary": "Stommel's two-box model of thermohaline circulation has two stable states joined by saddle-node bifurcations, giving hysteresis and collapse scenarios.", "map": "\\dot S=F-|q(T-S)|S", "breaks": "Box models omit wind-driven and eddy dynamics, so whether the real AMOC is bistable is contested.", "confidence": "current research", "strength": 2}
{"id": "C0879", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics", "name": "Chaos limits climate and weather prediction", "kind": "mechanism", "summary": "Sensitivity to initial conditions bounds weather forecasts, motivating ensemble prediction. Climate is a boundary-value problem about statistics of the attractor.", "map": "\\delta(t)\\sim\\delta_0 e^{\\lambda t}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0880", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Lorenz chaos and weather predictability", "kind": "historical", "summary": "Lorenz's truncated convection model gave the first strange attractor. The result sets the finite predictability horizon of weather (~2 weeks), set by Lyapunov growth of errors.", "map": "\\dot x=\\sigma(y-x),\\;\\dot y=x(\\rho-z)-y,\\;\\dot z=xy-\\beta z", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0881", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "KAM tori and dynamic aperture", "kind": "mechanism", "summary": "Nonlinear magnet errors make betatron motion a perturbed Hamiltonian system. Resonance islands, chaotic layers and surviving KAM tori set the dynamic aperture and beam lifetime.", "map": "H=\\omega_x J_x+\\omega_y J_y+\\epsilon V(J,\\theta)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0882", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics", "name": "Solitons, tsunamis and internal waves", "kind": "shared object", "summary": "Shallow-water KdV solitons describe tsunamis and ocean internal solitary waves, balancing nonlinear steepening against dispersion.", "map": "u_t+6uu_x+u_{xxx}=0", "breaks": "Real waves have dissipation, rotation and variable bathymetry, so exact integrability is lost.", "confidence": "established", "strength": 2}
{"id": "C0883", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation", "b": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "name": "Reaction–diffusion patterning of cell polarity", "kind": "mechanism", "summary": "Cell polarity and motility waves on membranes (Min proteins, Rho GTPases) are excitable or Turing-type reaction–diffusion patterns.", "map": "\\partial_t c=D\\nabla^2 c+f(c)", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0884", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation", "b": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "name": "Turing patterns and Kuramoto sync in biology", "kind": "mechanism", "summary": "Developmental patterning follows Turing reaction–diffusion instabilities, and neural and circadian rhythms follow Kuramoto-type phase locking.", "map": "\\dot\\theta_i=\\omega_i+\\tfrac{K}{N}\\sum_j\\sin(\\theta_j-\\theta_i)", "breaks": "Real gene networks are noisy and finite-sized, and Turing patterns need fine-tuned diffusivity ratios that biology rarely supplies.", "confidence": "current research", "strength": 2}
{"id": "C0885", "a": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Molecular vibrations as normal modes", "kind": "identity", "summary": "Molecular vibrational spectra are the normal modes of coupled atoms on a potential surface, found by diagonalising the mass-weighted Hessian, as for coupled springs.", "map": "\\det(\\mathbf{F}-\\omega^2\\mathbf{M})=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0886", "a": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Earth's free oscillations as normal modes", "kind": "mechanism", "summary": "After large earthquakes the Earth rings in toroidal and spheroidal normal modes. These are the eigenmodes of a continuum coupled-oscillator system and constrain the PREM structure.", "map": "\\mathcal{L}u=-\\omega^2\\rho u", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0887", "a": "01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators", "b": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "name": "Cavity resonance and Q factor in RF cavities", "kind": "identity", "summary": "Accelerator RF cavities are driven resonators characterised by Q and bandwidth, and superconducting cavities reach Q of 10^10 or more. Their response follows the driven damped oscillator.", "map": "Q=\\omega_0 U/P,\\;\\Delta\\omega=\\omega_0/Q", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0888", "a": "01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Larmor precession and resonance in MRI", "kind": "analogy", "summary": "Nuclear spin in MRI follows classical gyroscopic precession and driven resonance, with Bloch-equation relaxation like a damped driven oscillator (T1, T2).", "map": "\\omega_0=\\gamma B_0,\\;\\dot{\\mathbf M}=\\gamma\\mathbf M\\times\\mathbf B-\\ldots", "breaks": "Spin is quantum and the Bloch equations are linear only for ensemble magnetisation.", "confidence": "established", "strength": 2}
{"id": "C0889", "a": "01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics", "name": "Ocean waves, tides and dispersion", "kind": "shared object", "summary": "Surface gravity waves, internal waves and tides obey dispersion relations for fluid waves. The deep-water relation gives dispersive group and phase speeds.", "map": "\\omega^2=gk\\tanh(kh)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0890", "a": "01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Wave propagation in the Earth", "kind": "shared object", "summary": "Seismology applies reflection, refraction, impedance and dispersion of mechanical waves to layered media. Surface waves, free oscillations and travel-time inversion probe structure.", "map": "Z=\\rho v,\\; R=(Z_2-Z_1)/(Z_2+Z_1)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0891", "a": "01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics", "b": "11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics", "name": "Acoustics underlying ultrasound imaging", "kind": "shared object", "summary": "Echography relies on impedance mismatch reflection, attenuation, Doppler shift and beamforming of acoustic waves in tissue. Elastography uses shear wave speed to measure stiffness.", "map": "f_D=2f_0 v\\cos\\theta/c", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0892", "a": "01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics", "b": "11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics", "name": "Medical acoustics: impedance and Doppler", "kind": "shared object", "summary": "Ultrasound transducers, tissue attenuation and Doppler blood-flow measurement are applications of acoustic wave theory.", "map": "I_r/I_i=((Z_2-Z_1)/(Z_2+Z_1))^2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0893", "a": "01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Mathieu/Hill equation and strong focusing", "kind": "identity", "summary": "Betatron motion in an alternating-gradient lattice obeys Hill's equation, a periodically driven oscillator like Mathieu's. Stability bands match parametric resonance, and alternating focusing resembles Kapitza stabilisation.", "map": "x''+K(s)x=0,\\;K(s+L)=K(s)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0894", "a": "01-classical-mechanics/rigid-body-dynamics/gyroscopes-and-precession", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Gyroscope sensing, classical to atomic", "kind": "historical", "summary": "Mechanical gyroscopes sense rotation via angular momentum conservation, and atom-interferometric gyroscopes measure the same Sagnac-type rotation with matter waves at far higher sensitivity.", "map": "\\Delta\\phi=\\tfrac{4\\pi}{\\lambda v}\\,\\boldsymbol\\Omega\\cdot\\mathbf A", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C0895", "a": "01-classical-mechanics/rigid-body-dynamics/gyroscopes-and-precession", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Earth's precession, nutation and inner core", "kind": "shared object", "summary": "Precession and nutation of Earth's axis depend on its moment of inertia and on core structure, so the free core nutation constrains interior properties.", "map": "\\dot\\psi\\propto (C-A)/C", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0896", "a": "01-classical-mechanics/rigid-body-dynamics/rotational-dynamics-and-inertia-tensor", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Moment of inertia constrains density profile", "kind": "shared object", "summary": "Earth's moment of inertia factor (about 0.33) is a global constraint on radial density models such as PREM, showing a centrally condensed structure.", "map": "I=\\int\\rho r^2\\,dV=0.33\\,MR^2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1243", "a": "02-electromagnetism-and-optics/classical-optics", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Optics and imaging theory in medical imaging", "kind": "method transfer", "summary": "Transfer functions, resolution limits and Fourier-based image formation from optics carry over to radiography, CT and MRI image-quality analysis.", "map": "I(\\mathbf{r})=(O*h)(\\mathbf{r})\\;\\Rightarrow\\;\\tilde I=\\tilde O\\,\\mathrm{MTF}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1244", "a": "02-electromagnetism-and-optics/classical-optics/coherence-and-statistical-optics", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Coherence of X-ray sources", "kind": "shared object", "summary": "Diffraction-limited storage rings and FELs are characterized by transverse and longitudinal coherence, with van Cittert–Zernike propagation and emittance matching the diffraction limit $\\lambda/4\\pi$.", "map": "\\epsilon\\to\\lambda/4\\pi", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1245", "a": "02-electromagnetism-and-optics/classical-optics/coherence-and-statistical-optics", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Intensity interferometry and quantum sensing noise", "kind": "analogy", "summary": "Both rely on correlation measurements: Hanbury Brown–Twiss intensity correlations probe photon statistics, while sensor readout in quantum metrology is limited by shot noise and squeezing.", "map": "", "breaks": "Intensity interferometry exploits classical thermal-light bunching, while quantum sensing gains come from nonclassical entanglement or squeezing.", "confidence": "proposed", "strength": 1}
{"id": "C1246", "a": "02-electromagnetism-and-optics/classical-optics/coherence-and-statistical-optics", "b": "11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics", "name": "Coherence in OCT and speckle", "kind": "shared object", "summary": "OCT depth resolution is set by source coherence length (low-coherence interferometry), and speckle statistics govern both optical and ultrasound image texture.", "map": "l_c=\\frac{2\\ln2}{\\pi}\\frac{\\lambda^2}{\\Delta\\lambda}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1247", "a": "02-electromagnetism-and-optics/classical-optics/fourier-optics-and-imaging", "b": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "name": "Super-resolution and single-molecule localization", "kind": "method transfer", "summary": "Single-molecule localization microscopy (PALM/STORM) beats the diffraction limit by fitting the point-spread function of isolated emitters, linking single-molecule fluorescence to Fourier-optics resolution theory.", "map": "\\sigma_{loc}\\approx \\sigma_{PSF}/\\sqrt N", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1248", "a": "02-electromagnetism-and-optics/classical-optics/fourier-optics-and-imaging", "b": "11-interdisciplinary-physics/medical-physics", "name": "Medical imaging as Fourier optics", "kind": "method transfer", "summary": "Medical imaging modalities use transfer-function, sampling and deconvolution ideas first developed in Fourier optics.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1249", "a": "02-electromagnetism-and-optics/classical-optics/fourier-optics-and-imaging", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Fourier imaging: lens, CT and MRI k-space", "kind": "identity", "summary": "A lens performs a spatial Fourier transform; MRI samples k-space directly and CT uses the Fourier slice theorem. Reconstruction is Fourier synthesis with MTF-limited resolution.", "map": "\\tilde f(\\mathbf{k})=\\int f(\\mathbf{r})e^{-i\\mathbf{k}\\cdot\\mathbf{r}}d\\mathbf{r}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1250", "a": "02-electromagnetism-and-optics/classical-optics/fourier-optics-and-imaging", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Image quality via MTF", "kind": "identity", "summary": "Modulation transfer function and noise power spectrum quantify medical image quality exactly as in optical imaging systems.", "map": "\\mathrm{MTF}(\\mathbf{k})=|\\tilde h(\\mathbf{k})|/\\tilde h(0)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1251", "a": "02-electromagnetism-and-optics/classical-optics/geometric-optics", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Beam optics as ray-transfer matrices", "kind": "identity", "summary": "Linear transfer matrices for quadrupoles and drifts mirror ABCD ray matrices; Twiss parameters mirror Gaussian-beam parameters and emittance mirrors etendue.", "map": "\\begin{pmatrix}x\\\\x'\\end{pmatrix}_{out}=M\\begin{pmatrix}x\\\\x'\\end{pmatrix}_{in}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1252", "a": "02-electromagnetism-and-optics/classical-optics/interference-and-diffraction", "b": "11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics", "name": "Interferometry in OCT", "kind": "method transfer", "summary": "OCT uses Michelson low-coherence interferometry to gate backscattered light by path length, and ultrasound beam focusing and arrays rely on the same diffraction and array-factor physics.", "map": "I\\propto 2\\sqrt{I_rI_s}\\cos(2k\\Delta z)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1253", "a": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "b": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "name": "RF cavities as electromagnetic resonators", "kind": "identity", "summary": "Accelerating RF and SRF cavities are resonant waveguide modes; field patterns, Q factor and wall losses follow from cavity electrodynamics.", "map": "Q=\\omega_0 U/P_{loss}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1254", "a": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Absorption and dielectric response in spectroscopy", "kind": "identity", "summary": "Molecular absorption bands are the imaginary part of the dielectric function; Kramers–Kronig relations link absorption and refractive index.", "map": "n(\\omega)-1=\\frac{2}{\\pi}P\\!\\int\\frac{\\omega'\\kappa(\\omega')}{\\omega'^2-\\omega^2}d\\omega'", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1255", "a": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Reflection and absorption of radiation", "kind": "mechanism", "summary": "Fresnel reflection and absorption set surface albedo and emissivity, and skin-depth-like penetration governs microwave remote sensing.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1256", "a": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Seismic and EM wave reflection analogy", "kind": "analogy", "summary": "Seismic P/S reflection and refraction at interfaces follows Snell's law with Zoeppritz amplitudes, paralleling Fresnel coefficients and polarization-dependent reflection.", "map": "", "breaks": "Elastic waves have longitudinal and mode-converted components, so there are more coupled modes than the two EM polarizations.", "confidence": "established", "strength": 2}
{"id": "C1257", "a": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "MRI RF coils and field propagation", "kind": "shared object", "summary": "MRI excitation and detection use RF coils and resonant circuits, and at high field wavelength effects in tissue produce B1 inhomogeneity governed by EM wave propagation.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1258", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/electrostatics-and-boundary-value-problems", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Device electrostatics via Poisson equation", "kind": "identity", "summary": "The depletion region of a p-n junction and MOS gate electrostatics are Poisson boundary-value problems, solved numerically in TCAD.", "map": "\\nabla^2\\phi=-\\rho/\\epsilon", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1259", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/fields-in-matter", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Magnetometry and magnetization response", "kind": "shared object", "summary": "NV-centre and atomic magnetometers and SQUIDs measure the B field of magnetized samples, so interpreting signals needs dipole fields and bound-current models.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1260", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/magnetostatics", "b": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "name": "Accelerator magnets from magnetostatics", "kind": "method transfer", "summary": "Dipole and quadrupole magnet design uses magnetostatic field solutions and multipole expansion of the 2D field, with pole shaping setting harmonic content.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1261", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/multipole-expansions", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Field multipoles and nonlinear beam dynamics", "kind": "mechanism", "summary": "Sextupole and higher multipole errors in magnets drive chromatic and resonant nonlinear beam motion; multipole decomposition of the field organizes these effects.", "map": "B_y+iB_x=B_0\\sum_n (b_n+ia_n)(x+iy)^{n-1}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1262", "a": "02-electromagnetism-and-optics/photonics-and-lasers/integrated-and-fiber-photonics", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Silicon photonics and electronic fabrication", "kind": "method transfer", "summary": "Silicon photonic chips reuse CMOS lithography and materials platforms from semiconductor devices, merging electronic and photonic components.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1263", "a": "02-electromagnetism-and-optics/photonics-and-lasers/laser-physics", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "FEL as a laser without a bound medium", "kind": "analogy", "summary": "SASE FELs amplify radiation through collective microbunching of free electrons, analogous to gain with stimulated emission in lasers, but with no population inversion.", "map": "P\\propto e^{z/L_g}", "breaks": "Gain comes from classical electron bunching, not quantized level inversion; SASE starts from shot noise, with poor temporal coherence.", "confidence": "established", "strength": 2}
{"id": "C1264", "a": "02-electromagnetism-and-optics/photonics-and-lasers/laser-physics", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Semiconductor diode lasers", "kind": "shared object", "summary": "LEDs and diode lasers realize stimulated emission and population inversion in a p-n junction, with cavity feedback setting threshold and linewidth.", "map": "g_{th}=\\alpha_i+\\frac{1}{2L}\\ln\\frac{1}{R_1R_2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1265", "a": "02-electromagnetism-and-optics/photonics-and-lasers/nonlinear-optics", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Multidimensional and nonlinear spectroscopy", "kind": "method transfer", "summary": "Coherent Raman, 2D electronic and vibrational spectroscopies are higher-order nonlinear susceptibility measurements, using pulse sequences and phase matching from nonlinear optics.", "map": "P^{(3)}=\\chi^{(3)}E_1E_2E_3", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1266", "a": "02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Attosecond X-ray FELs and HHG", "kind": "shared object", "summary": "Attosecond pulses are produced both by high-harmonic generation and by FEL pulse-shortening schemes; they serve the same time-resolved spectroscopy of electrons.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1267", "a": "02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Femtochemistry with ultrafast pulses", "kind": "method transfer", "summary": "Femtosecond pump-probe pulses resolve nuclear motion through transition states and conical intersections; attosecond pulses extend this to electronic dynamics.", "map": "S(\\tau)=\\int I_{pump}(t)\\,I_{probe}(t-\\tau)\\,dt", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1268", "a": "02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Reaction dynamics probed by ultrafast optics", "kind": "method transfer", "summary": "Reaction dynamics supplies the wave-packet and potential-surface questions that ultrafast optics answers, including coherent control and conical-intersection passage.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1269", "a": "02-electromagnetism-and-optics/radiation-and-scattering", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Radiation theory behind light sources", "kind": "identity", "summary": "Synchrotron, undulator and FEL emission follow from the radiation of relativistic accelerated charges described by Liénard–Wiechert fields.", "map": "\\frac{dP}{d\\Omega}\\propto \\left|\\hat n\\times[(\\hat n-\\boldsymbol\\beta)\\times\\dot{\\boldsymbol\\beta}]\\right|^2/(1-\\hat n\\cdot\\boldsymbol\\beta)^5", "breaks": "", "confidence": "established", "strength": 3}