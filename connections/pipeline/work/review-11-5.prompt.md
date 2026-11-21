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

# Packet 11-5 (33 records)

{"id": "C2901", "a": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "b": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "name": "Synchrotron crystallography and XFEL structures", "kind": "method transfer", "summary": "Synchrotron macromolecular crystallography, SAXS and XFEL serial femtosecond crystallography supply most protein structures and time-resolved dynamics.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2902", "a": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "X-ray and ultrafast spectroscopy at light sources", "kind": "method transfer", "summary": "Synchrotron and FEL pulses drive X-ray absorption, photoelectron and pump-probe ultrafast spectroscopies of molecules, extending optical multidimensional spectroscopy to X-ray wavelengths.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2903", "a": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "b": "11-interdisciplinary-physics/chemical-physics/surface-science-and-catalysis", "name": "Operando X-ray probes of catalysts and surfaces", "kind": "method transfer", "summary": "Ambient-pressure XPS, grazing-incidence diffraction and XAS at synchrotrons characterise surface structure and working catalysts in situ.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2904", "a": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Synchrotron phase-contrast and microtomography", "kind": "method transfer", "summary": "Synchrotron coherent beams enable phase-contrast imaging and microCT, the research precursor of coherence-based X-ray contrast and CT reconstruction methods.", "map": "", "breaks": "", "confidence": "current research", "strength": 1}
{"id": "C2905", "a": "11-interdisciplinary-physics/applied-and-device-physics/energy-materials-and-thermoelectrics", "b": "11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods", "name": "First-principles design of energy materials", "kind": "method transfer", "summary": "DFT and wavefunction methods predict electrode voltages, ion barriers, thermoelectric band structures and perovskite properties for materials screening.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2906", "a": "11-interdisciplinary-physics/applied-and-device-physics/energy-materials-and-thermoelectrics", "b": "11-interdisciplinary-physics/chemical-physics/surface-science-and-catalysis", "name": "Surface chemistry of electrodes and catalysts", "kind": "shared object", "summary": "Adsorption, interfaces and electrocatalysis govern battery SEI layers, hydrogen storage and fuel cells, linking surface science to energy materials.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2907", "a": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Atom-interferometer gravimetry for geophysics", "kind": "method transfer", "summary": "Atom-interferometric and superconducting gravimeters measure gravity variations used in geodesy, mass transport and subsurface density mapping.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2908", "a": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "MRI and NV/atomic magnetometry share spin resonance", "kind": "mechanism", "summary": "MRI relies on nuclear magnetic resonance and Bloch dynamics; NV and atomic magnetometers use the same spin-precession and Ramsey/spin-echo sequences, and SQUIDs enable ultra-low-field MRI and MEG.", "map": "\\omega_L=\\gamma B", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2909", "a": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Photovoltaic carriers and electron-transfer kinetics", "kind": "analogy", "summary": "Charge separation and recombination in organic and perovskite cells follow Marcus-type electron transfer, paralleling band-based drift-diffusion treatments.", "map": "", "breaks": "Inorganic crystalline cells use delocalised bands rather than hopping.", "confidence": "current research", "strength": 1}
{"id": "C2910", "a": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "Semiconductor photodetectors in PET", "kind": "shared object", "summary": "Silicon photomultipliers and CdZnTe detectors in time-of-flight PET and gamma cameras are semiconductor p-n junction devices operated in avalanche regimes.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2911", "a": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "b": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "name": "Membrane elasticity and protein-lipid coupling", "kind": "shared object", "summary": "Helfrich bending elasticity governs membrane deformation by proteins, channels and motors; mechanosensitive channels bridge molecular structure and membrane mechanics.", "map": "E=\\frac{\\kappa}{2}\\int(2H-c_0)^2dA", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2912", "a": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "b": "11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics", "name": "Elastography and tissue mechanics", "kind": "shared object", "summary": "Ultrasound and MR elastography measure shear-wave speed to infer tissue stiffness, the continuum viscoelasticity that cell and tissue mechanics studies as a driver of mechanotransduction.", "map": "c_s=\\sqrt{\\mu/\\rho}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2913", "a": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "b": "11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods", "name": "Electronic structure meets force fields and ML structure", "kind": "method transfer", "summary": "Quantum chemistry parametrises force fields and QM/MM methods for biomolecules; ML potentials and structure predictors learn from such data.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2914", "a": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Electron transfer in proteins and Marcus theory", "kind": "mechanism", "summary": "Marcus theory of electron transfer governs biological redox chains in respiration and photosynthesis, with reorganisation energy and tunnelling through protein.", "map": "k\\propto e^{-(\\Delta G+\\lambda)^2/4\\lambda k_BT}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2915", "a": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Energy landscapes and rate theory", "kind": "identity", "summary": "Protein folding landscapes and potential energy surfaces share Kramers/transition-state rate theory, barrier crossing and funnel concepts; force spectroscopy uses Bell-Evans extensions.", "map": "k=\\frac{\\omega}{2\\pi}e^{-\\Delta G^\\ddagger/k_BT}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2916", "a": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "b": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "name": "Noise and kinetic proofreading at single molecules", "kind": "shared object", "summary": "Gene-expression noise and kinetic proofreading are stochastic-kinetics ideas observed directly by single-molecule counting and enzyme-turnover measurements.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2917", "a": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Feedbacks and tipping in living and climate systems", "kind": "analogy", "summary": "Feedback loops, bistability and noise-induced transitions describe both gene circuits and climate tipping elements such as AMOC collapse and albedo feedback.", "map": "", "breaks": "Climate has no replicates and poorly constrained dynamics, unlike controlled biological circuits.", "confidence": "proposed", "strength": 1}
{"id": "C2918", "a": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Single-molecule FRET and spectroscopy", "kind": "method transfer", "summary": "Single-molecule fluorescence and FRET descend from molecular spectroscopy: Förster dipole coupling, photophysics, and Raman or single-molecule detection, with time-resolved methods probing conformational dynamics.", "map": "E=\\frac{1}{1+(r/R_0)^6}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2919", "a": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Single-molecule force spectroscopy and barrier crossing", "kind": "mechanism", "summary": "Pulling experiments measure barrier heights and rates of unfolding, interpreted via Kramers theory and Bell-Evans models; Jarzynski and Crooks relations recover free energies.", "map": "k(F)=k_0e^{F x^\\ddagger/k_BT}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2920", "a": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "b": "11-interdisciplinary-physics/medical-physics/radiation-therapy", "name": "Radiation damage to DNA at molecular scale", "kind": "shared object", "summary": "Radiobiology of strand breaks and repair, and LET dependence of carbon ions, connects to single-molecule studies of DNA mechanics and repair enzymes.", "map": "", "breaks": "", "confidence": "current research", "strength": 1}
{"id": "C2921", "a": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "b": "11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics", "name": "Optical tweezers and fluorescence microscopy lineage", "kind": "method transfer", "summary": "Biomedical optics and single-molecule biophysics share fluorescence, interferometric detection and light-scattering techniques; OCT coherence gating parallels interferometric nanoscale tracking.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C2922", "a": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Molecular absorption and the greenhouse effect", "kind": "mechanism", "summary": "Greenhouse forcing arises from vibrational-rotational absorption bands of CO2, H2O and CH4; line strengths and selection rules from spectroscopy feed radiative transfer codes.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2923", "a": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Circulation, convection and cloud feedback", "kind": "mechanism", "summary": "Hadley circulation, convection and jet shifts control water vapour, lapse rate and cloud feedbacks and thus climate sensitivity.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2924", "a": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics", "name": "Geostrophic rotating stratified flow", "kind": "identity", "summary": "Atmosphere and ocean obey the same rotating, stratified primitive equations: geostrophic balance, Rossby waves, Ekman layers and baroclinic instability, with western boundary currents mirroring jets.", "map": "f\\,\\hat z\\times\\mathbf u=-\\frac{1}{\\rho}\\nabla p", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2925", "a": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Geodynamo and rotating convection", "kind": "analogy", "summary": "Core convection in the geodynamo and atmospheric or oceanic convection are rotating, buoyancy-driven flows controlled by Rossby, Ekman and Rayleigh numbers with Taylor-column constraints.", "map": "", "breaks": "Geodynamo includes magnetic Lorentz forces and a much lower Ekman number.", "confidence": "established", "strength": 2}
{"id": "C2926", "a": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics", "name": "Ocean heat uptake and climate response", "kind": "mechanism", "summary": "Ocean heat uptake and AMOC set the transient climate response and delay equilibrium warming given by radiative forcing and feedbacks.", "map": "\\Delta T=\\lambda\\,\\Delta F", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2927", "a": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Tsunami and ocean wave propagation from earthquakes", "kind": "shared object", "summary": "Seafloor earthquakes generate tsunamis and tides and waves share shallow-water wave dynamics, linking source seismology to ocean wave propagation.", "map": "c=\\sqrt{gh}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2928", "a": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Tomography across scales", "kind": "method transfer", "summary": "Seismic travel-time tomography and CT reconstruction solve the same linear inverse problem with regularisation and iterative solvers.", "map": "t=\\int s\\,dl", "breaks": "Seismic rays bend and coverage is sparse, unlike controlled CT geometry.", "confidence": "established", "strength": 2}
{"id": "C2929", "a": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "b": "11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics", "name": "Seismic and ultrasound wave imaging", "kind": "identity", "summary": "Seismic tomography and ultrasound imaging both invert travel times and scattered waves in elastic media; elastography uses shear waves just as seismology does, and full-waveform inversion appears in both.", "map": "\\rho\\ddot u=\\nabla\\cdot\\sigma", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2930", "a": "11-interdisciplinary-physics/medical-physics/medical-imaging", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "Tomographic reconstruction shared by CT and PET", "kind": "identity", "summary": "CT and PET/SPECT both reconstruct images from line integrals via Radon transform, filtered back-projection and iterative statistical methods such as MLEM; PET adds attenuation correction from CT.", "map": "g(\\theta,s)=\\int f\\,dl", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2931", "a": "11-interdisciplinary-physics/medical-physics/medical-imaging", "b": "11-interdisciplinary-physics/medical-physics/radiation-therapy", "name": "Image-guided radiotherapy and treatment planning", "kind": "method transfer", "summary": "CT supplies electron density for dose calculation and cone-beam CT, MRI-linacs and PET guide targeting; image quality and dose trade-offs are shared.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2932", "a": "11-interdisciplinary-physics/medical-physics/medical-imaging", "b": "11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics", "name": "Image quality, SNR and resolution across modalities", "kind": "method transfer", "summary": "Resolution, contrast-to-noise and point-spread/MTF frameworks, plus Fourier-domain k-space and OCT sampling, unify MRI, ultrasound and optical imaging; photoacoustic reconstruction resembles tomography.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2933", "a": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "b": "11-interdisciplinary-physics/medical-physics/radiation-therapy", "name": "Radionuclide therapy and dosimetry", "kind": "shared object", "summary": "Internal dosimetry for radiopharmaceutical therapy uses the same absorbed-dose, Monte Carlo transport and radiobiology as external beam; PET/SPECT quantify the uptake.", "map": "D=\\frac{\\Delta E}{m}", "breaks": "", "confidence": "established", "strength": 2}