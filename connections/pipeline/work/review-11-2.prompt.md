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

# Packet 11-2 (100 records)

{"id": "C1270", "a": "02-electromagnetism-and-optics/radiation-and-scattering", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Scattering and absorption in climate", "kind": "shared object", "summary": "Rayleigh and Mie scattering and molecular absorption set atmospheric radiative transfer, aerosol forcing, cloud albedo and the greenhouse effect.", "map": "\\frac{dI}{ds}=-\\kappa I+j", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1271", "a": "02-electromagnetism-and-optics/radiation-and-scattering/cherenkov-and-transition-radiation", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "Cherenkov timing in PET", "kind": "method transfer", "summary": "Prompt Cherenkov photons from 511 keV photoelectrons in crystals such as BGO are exploited for sub-100 ps time-of-flight PET timing.", "map": "", "breaks": "", "confidence": "current research", "strength": 1}
{"id": "C1272", "a": "02-electromagnetism-and-optics/radiation-and-scattering/cherenkov-and-transition-radiation", "b": "11-interdisciplinary-physics/medical-physics/radiation-therapy", "name": "Cherenkov light in radiotherapy", "kind": "shared object", "summary": "Cherenkov emission from therapy beams in tissue is used for dose imaging and verification; it is also a nuisance in fibre dosimeters.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1273", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "11-interdisciplinary-physics/accelerator-physics", "name": "Accelerator radiation losses and damping", "kind": "mechanism", "summary": "Synchrotron radiation loss limits ring energy and, via radiation reaction, provides damping and quantum excitation that set equilibrium emittance.", "map": "U_0=\\frac{4\\pi}{3}\\frac{r_e E^4}{\\rho\\,(mc^2)^3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1274", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Light-source design from radiation formulas", "kind": "method transfer", "summary": "Source brightness and spectra are designed using the classical radiation formulas, with coherent enhancement when bunch length falls below the wavelength.", "map": "P_{coh}\\propto N^2 P_1", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1275", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Liénard–Wiechert to undulator radiation", "kind": "identity", "summary": "Bending-magnet and undulator spectra, critical energy and relativistic beaming derive directly from Larmor/Liénard radiation, with $\\gamma$-boosted forward cones.", "map": "\\omega_c=\\tfrac{3}{2}\\gamma^3 c/\\rho,\\;\\theta\\sim 1/\\gamma", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1276", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Raman scattering as inelastic light scattering", "kind": "mechanism", "summary": "Raman spectroscopy is inelastic scattering from polarizability modulation by molecular vibrations, extending Rayleigh scattering from an induced dipole.", "map": "\\mathbf p=\\alpha(Q)\\mathbf E,\\;\\alpha=\\alpha_0+\\alpha'Q", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1277", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Aerosol and cloud scattering in forcing", "kind": "mechanism", "summary": "Aerosol direct and cloud albedo effects are Mie scattering with size-dependent efficiency; the sky's blue and clouds' white arise from the same Rayleigh-to-Mie crossover.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1278", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Compton and Rayleigh scattering in X-ray imaging", "kind": "shared object", "summary": "Compton and Rayleigh scattering govern X-ray attenuation, scatter degradation of radiographs and CT contrast, and dose deposition.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1279", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics", "name": "Light scattering in tissue and diffuse optics", "kind": "shared object", "summary": "Tissue optics relies on Mie/Rayleigh scattering and the diffusion approximation to radiative transfer to image and measure oxygenation in turbid media.", "map": "\\mu_s'=\\mu_s(1-g)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1587", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/heat-engines-and-efficiency", "b": "11-interdisciplinary-physics/applied-and-device-physics", "name": "Thermodynamic limits of energy devices", "kind": "mechanism", "summary": "Thermoelectrics, solar cells and batteries are bounded by second-law efficiency limits; ZT maps to a fraction of Carnot efficiency, and finite-time engine analysis applies.", "map": "\\eta_{max}=\\eta_C\\frac{\\sqrt{1+ZT}-1}{\\sqrt{1+ZT}+T_c/T_h}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1588", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/heat-engines-and-efficiency", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Carnot bounds on solar cell efficiency", "kind": "mechanism", "summary": "Solar cells act as heat engines between the Sun and ambient temperature; the Shockley–Queisser limit and Landsberg/Carnot bounds follow from entropy generation in photon absorption and emission.", "map": "\\eta_C = 1 - T_c/T_h", "breaks": "Photovoltaic conversion is quantum and band-gap limited, not a cyclic engine.", "confidence": "established", "strength": 2}
{"id": "C1589", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/heat-engines-and-efficiency", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Photovoltaics as thermodynamic converters", "kind": "mechanism", "summary": "Detailed balance between absorbed and emitted blackbody radiation sets the SQ limit; thermodynamic treatments give ultimate limits for multijunction and hot-carrier cells.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1590", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/phase-equilibria-and-chemical-potential", "b": "11-interdisciplinary-physics/chemical-physics/surface-science-and-catalysis", "name": "Adsorption isotherms and chemical potential", "kind": "identity", "summary": "Langmuir and BET isotherms follow from equating the chemical potential of adsorbed and gas phases, i.e. a lattice-gas grand canonical calculation.", "map": "\\theta=\\frac{KP}{1+KP}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1591", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/thermodynamic-potentials-and-maxwell-relations", "b": "11-interdisciplinary-physics/applied-and-device-physics/energy-materials-and-thermoelectrics", "name": "Electrochemical potential and battery voltage", "kind": "identity", "summary": "Cell voltage equals the Gibbs free-energy change per charge, with the open-circuit voltage from the chemical potential difference of lithium in the two electrodes.", "map": "\\Delta G=-nFE", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1592", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/complex-networks", "b": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "name": "Network science of biological regulation and spreading", "kind": "shared object", "summary": "Scale-free and small-world network structure describes gene regulation, metabolic and neural networks, and epidemic spreading with vanishing thresholds.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1593", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/localization-and-disorder", "b": "11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics", "name": "Coherent backscattering and weak localization of waves", "kind": "mechanism", "summary": "Weak localization of light in turbid media produces coherent backscattering enhancement, which modifies diffuse optics and speckle statistics in tissue.", "map": "", "breaks": "Strong localization is not reached in tissue; transport is nearly classical diffusion.", "confidence": "established", "strength": 1}
{"id": "C1594", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/percolation", "b": "11-interdisciplinary-physics/applied-and-device-physics/energy-materials-and-thermoelectrics", "name": "Percolation in composite electrodes and electrolytes", "kind": "shared object", "summary": "Ionic and electronic conduction in composite battery electrodes and solid electrolytes depends on percolating pathways with critical thresholds and power-law conductivity.", "map": "\\sigma\\propto(p-p_c)^t", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1595", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/spin-glasses", "b": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "name": "Protein folding funnels and spin-glass landscapes", "kind": "analogy", "summary": "Random-energy-model ideas and the principle of minimal frustration describe folding landscapes; glass transition temperature and funnel gap separate foldable sequences from glassy ones.", "map": "T_f/T_g>1", "breaks": "Evolved proteins are strongly non-random and minimally frustrated, unlike true spin glasses.", "confidence": "established", "strength": 3}
{"id": "C1596", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/statistical-physics-of-learning", "b": "11-interdisciplinary-physics/biophysics", "name": "Statistical physics of neural computation", "kind": "method transfer", "summary": "Hopfield-network and replica methods from spin glasses are used to model neural memory, capacity and learning in neural biophysics.", "map": "H=-\\tfrac12\\sum_{ij}J_{ij}s_is_j", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1597", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/statistical-physics-of-learning", "b": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "name": "Learning theory and protein structure inference", "kind": "method transfer", "summary": "Spin-glass landscape concepts and Boltzmann-machine/Potts inference (direct coupling analysis) link learning theory to protein folding and structure prediction.", "map": "P(\\sigma)\\propto e^{\\sum h_i+\\sum J_{ij}}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1598", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Partition functions in transition-state theory", "kind": "method transfer", "summary": "Eyring transition-state theory writes rate constants as ratios of partition functions, and equilibrium constants follow from molecular partition functions.", "map": "k=\\frac{k_BT}{h}\\frac{Q^\\ddagger}{Q}e^{-E_0/k_BT}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1599", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Information-theoretic limits of quantum metrology", "kind": "analogy", "summary": "Fisher information and Cramér–Rao bounds set measurement precision, mirroring maximum-entropy and information-geometry formulations of statistical mechanics.", "map": "", "breaks": "Quantum Fisher information involves non-commuting observables with no classical-entropy counterpart.", "confidence": "current research", "strength": 1}
{"id": "C1600", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information", "b": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "name": "Information limits in living systems", "kind": "identity", "summary": "Sensing precision, kinetic proofreading and gene regulation are bounded by mutual information and Landauer-type energy costs, using Shannon entropy and maximum entropy models.", "map": "I=S(X)-S(X|Y)", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1601", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Maximum entropy and information in image reconstruction", "kind": "method transfer", "summary": "Maximum-entropy priors and Shannon information underlie regularised image reconstruction and noise-limited image quality in CT and MRI.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1602", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Planck law and Earth's radiative balance", "kind": "mechanism", "summary": "Planck's blackbody spectrum and Stefan–Boltzmann law fix Earth's emission temperature; greenhouse absorption modifies the outgoing spectrum band by band.", "map": "\\sigma T_e^4=S(1-\\alpha)/4", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1603", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "Poisson counting statistics in emission imaging", "kind": "shared object", "summary": "Radioactive decay counts are Poisson fluctuations, so SPECT and PET image noise scales as 1/√N, which governs time-of-flight gains.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1604", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/driven-systems-and-nonequilibrium-steady-states", "b": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "name": "Active and driven matter in living systems", "kind": "shared object", "summary": "Exclusion processes, KPZ growth and active-matter nonequilibrium steady states model molecular traffic, tissue growth, bacterial colonies and collective cell motion.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1605", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/driven-systems-and-nonequilibrium-steady-states", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Self-organized criticality in earthquakes", "kind": "analogy", "summary": "Gutenberg–Richter power-law earthquake statistics and stick-slip fault models such as Burridge–Knopf and OFC are the standard examples of self-organized criticality and avalanche dynamics.", "map": "", "breaks": "Real faults show characteristic-earthquake and aftershock correlations not captured by simple SOC models.", "confidence": "current research", "strength": 2}
{"id": "C1606", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Vlasov-Boltzmann kinetics of charged beams", "kind": "analogy", "summary": "Beam distributions evolve by Vlasov/Fokker–Planck equations in phase space, as in collisionless kinetic theory; Liouville's theorem underlies emittance conservation and cooling is a Fokker–Planck process.", "map": "\\partial_t f+\\{f,H\\}=0", "breaks": "Beams are far from equilibrium, with long-range space-charge and no collision-driven thermalization.", "confidence": "established", "strength": 2}
{"id": "C1607", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "From Boltzmann kinetics to atmospheric fluid equations", "kind": "method transfer", "summary": "Chapman–Enskog reduction of the Boltzmann equation gives the Navier–Stokes transport coefficients used in atmospheric models; mean free path sets the continuum validity.", "map": "\\mathrm{Kn}=\\lambda/L\\ll1", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1608", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation", "b": "11-interdisciplinary-physics/applied-and-device-physics/energy-materials-and-thermoelectrics", "name": "Onsager reciprocity and thermoelectric transport", "kind": "identity", "summary": "Seebeck and Peltier coefficients are related by Onsager reciprocity (Kelvin relation), and ZT follows from the matrix of transport coefficients constrained by the second law.", "map": "\\Pi=TS", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1609", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Fluctuation-dissipation limits on sensor noise", "kind": "identity", "summary": "Thermal noise in SQUIDs, resonators and magnetometers is tied to dissipation by the fluctuation–dissipation theorem (Johnson–Nyquist), setting sensitivity floors.", "map": "S_V=4k_BTR", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1610", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "name": "Langevin dynamics of tethered molecules", "kind": "shared object", "summary": "Optical-tweezer bead and molecule dynamics are overdamped Langevin processes; force spectroscopy, Kramers escape and diffusion analyses use Fokker–Planck theory.", "map": "\\gamma\\dot x=-\\partial_x U+\\sqrt{2\\gamma k_BT}\\,\\xi(t)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1611", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Kramers rate theory and reaction rates", "kind": "mechanism", "summary": "Barrier-crossing rates in solution follow Kramers theory, interpolating between transition-state theory and diffusion-limited regimes with friction.", "map": "k\\propto e^{-E_b/k_BT}", "breaks": "Kramers theory assumes a single reaction coordinate with Markovian friction.", "confidence": "established", "strength": 3}
{"id": "C1612", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Hasselmann stochastic climate model", "kind": "analogy", "summary": "Slow climate variability is modelled as an Ornstein–Uhlenbeck process, with fast weather as noise forcing the slow ocean and ice variables.", "map": "C\\dot T=-\\lambda T+\\xi(t)", "breaks": "Weather noise is not strictly white and the system lacks detailed balance.", "confidence": "established", "strength": 2}
{"id": "C1613", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics", "name": "Diffusion and speckle in diffuse optics", "kind": "mechanism", "summary": "Photon transport in tissue reduces to a diffusion equation from random walks; diffusing-wave spectroscopy and Doppler/speckle techniques probe Brownian motion and blood flow.", "map": "\\partial_t\\phi=D\\nabla^2\\phi-\\mu_a c\\phi", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1614", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-thermodynamics-and-fluctuation-theorems", "b": "11-interdisciplinary-physics/biophysics", "name": "Biophysics as stochastic thermodynamics", "kind": "shared object", "summary": "Cellular sensing, motors and information processing are analysed by entropy production and thermodynamic uncertainty relations, linking precision to dissipation.", "map": "\\mathrm{Var}(J)/\\langle J\\rangle^2\\ge 2/\\Sigma", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1615", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-thermodynamics-and-fluctuation-theorems", "b": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "name": "Fluctuation theorems for molecular machines", "kind": "shared object", "summary": "Molecular motors and folding transitions operate far from equilibrium at kT scale; entropy production and Jarzynski/Crooks relations quantify their dissipation and free energies.", "map": "\\langle e^{-\\beta W}\\rangle=e^{-\\beta\\Delta F}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1616", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-thermodynamics-and-fluctuation-theorems", "b": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "name": "Dissipation cost of kinetic proofreading and sensing", "kind": "mechanism", "summary": "Energy dissipation buys accuracy in proofreading and sensing; entropy production bounds error rates and information rates.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1617", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-thermodynamics-and-fluctuation-theorems", "b": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "name": "Pulling experiments verify Jarzynski and Crooks", "kind": "method transfer", "summary": "Optical-tweezer unfolding of RNA hairpins verified Jarzynski and Crooks relations, recovering equilibrium free energies from nonequilibrium work distributions.", "map": "P_F(W)/P_R(-W)=e^{\\beta(W-\\Delta F)}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1618", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/ising-model-and-lattice-models", "b": "11-interdisciplinary-physics/chemical-physics/surface-science-and-catalysis", "name": "Lattice-gas models of adsorbate ordering", "kind": "identity", "summary": "Adsorbed monolayers map onto Ising lattice gases, with ordering transitions and surface reconstructions in Ising, Potts and universality classes; kinetic Monte Carlo models catalytic kinetics.", "map": "n_i=(1+s_i)/2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1619", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Tipping points and bifurcations in climate", "kind": "analogy", "summary": "Ice-albedo and AMOC bistability resemble Landau free-energy double wells with first-order jumps and hysteresis, and critical slowing down serves as an early-warning signal.", "map": "", "breaks": "Climate is driven and dissipative with no free energy to minimise.", "confidence": "current research", "strength": 1}
{"id": "C1620", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/renormalization-group", "b": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "name": "Polymer scaling and coarse-graining of biomolecules", "kind": "method transfer", "summary": "Renormalization-group scaling gives polymer exponents for unfolded chains, and coarse-grained models of proteins use the same logic of eliminating fast degrees of freedom.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1621", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/topological-phase-transitions-bkt", "b": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "name": "Fluctuating membranes and 2D defect physics", "kind": "analogy", "summary": "Two-dimensional membranes and the hexatic/crystalline phases share 2D melting and defect-unbinding physics, plus thermal-undulation renormalisation of bending rigidity.", "map": "", "breaks": "Membranes have out-of-plane fluctuations and fluid lipid order, so BKT applies only to in-plane ordered layers.", "confidence": "established", "strength": 2}
{"id": "C1894", "a": "04-quantum-physics/atomic-molecular-and-optical-physics", "b": "11-interdisciplinary-physics/accelerator-physics", "name": "Phase-space cooling in beams and atoms", "kind": "analogy", "summary": "Stochastic, electron and laser cooling of stored ion beams parallel atomic laser cooling: both shrink phase-space volume via dissipative coupling, with laser-cooled ion beams bridging them.", "map": "", "breaks": "Liouville's theorem forbids cooling with conservative forces alone; accelerator beams are classical and macroscopically charged.", "confidence": "established", "strength": 2}
{"id": "C1895", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Atomic sensors and clocks", "kind": "shared object", "summary": "Atom interferometers, optical clocks and atomic magnetometers share Ramsey interrogation of coherent atomic superpositions, limited by projection noise and coherence time.", "map": "\\delta\\phi=\\delta\\omega\\,T", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1896", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Quantum gravimetry for geophysics", "kind": "shared object", "summary": "Atom-interferometric gravimeters and clock-based relativistic geodesy measure gravity potential differences, applied to Earth-interior mass changes and hydrology.", "map": "\\Delta f/f=g\\,\\Delta h/c^2", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1897", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "11-interdisciplinary-physics/chemical-physics", "name": "Chemical physics rests on atomic structure", "kind": "historical", "summary": "Atomic level structure, fine/hyperfine coupling and spectroscopy provide the foundation for chemical physics, from orbitals to spectroscopic probes of molecules.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1898", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Atomic to molecular spectroscopy", "kind": "method transfer", "summary": "Selection rules, term structure and spectroscopic techniques from atoms extend to molecular rotational, vibrational and electronic spectra, adding nuclear motion via Born–Oppenheimer separation.", "map": "E=E_{el}+E_{vib}+E_{rot}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1899", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Spectroscopy shared toolkit", "kind": "method transfer", "summary": "Laser spectroscopy techniques, line-shape analysis and selection rules developed for atoms are used on molecules, and ultrafast molecular methods feed back into AMO.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1900", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/laser-cooling-and-trapping", "b": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "name": "Optical trapping: atoms to biomolecules", "kind": "method transfer", "summary": "Gradient-force optical traps developed for cooling and trapping atoms became optical tweezers that manipulate single biomolecules and measure piconewton forces.", "map": "U=-\\tfrac{1}{2}\\alpha |E|^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1901", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/laser-cooling-and-trapping", "b": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "name": "Tweezers return: biophysics to atoms", "kind": "shared object", "summary": "Optical tweezer technology links single-molecule force spectroscopy and neutral-atom tweezer arrays; the same focused-beam dipole trap physics underlies both.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1902", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "b": "11-interdisciplinary-physics/chemical-physics", "name": "Cold-atom simulation of chemical models", "kind": "method transfer", "summary": "Programmable atomic lattices emulate Hubbard and spin-boson-type models relevant to electron transfer and correlated electrons, offering analog simulation of chemical physics Hamiltonians.", "map": "", "breaks": "", "confidence": "proposed", "strength": 1}
{"id": "C1903", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/ultracold-molecules", "b": "11-interdisciplinary-physics/chemical-physics", "name": "Chemical physics and ultracold molecules", "kind": "shared object", "summary": "Molecular structure, potential surfaces and collision theory from chemical physics underpin cooling and control of molecules and controlled ultracold reactions.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1904", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/ultracold-molecules", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Molecular spectroscopy for EDM and cooling", "kind": "method transfer", "summary": "Rovibrational structure and Franck–Condon factors determine which molecules can be laser-cooled, and precision molecular spectroscopy underlies electron-EDM searches.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1905", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/ultracold-molecules", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Ultracold chemistry and reaction dynamics", "kind": "shared object", "summary": "Ultracold molecular collisions probe reactions at the quantum threshold, where single partial waves, resonances and tunnelling dominate over thermal averaging, testing potential energy surfaces.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1906", "a": "04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Decoherence limits sensors", "kind": "mechanism", "summary": "Environmental decoherence sets T2 and thus sensitivity of NV, atomic and SQUID sensors, while sensors also serve as probes of environmental noise spectra; entangled probes are more fragile.", "map": "\\delta B\\propto 1/\\sqrt{T_2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1907", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/lindblad-master-equations", "b": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "name": "Quantum biology and open dynamics", "kind": "analogy", "summary": "Exciton transport in photosynthetic complexes is modelled with open-system master equations, where noise may assist transfer; relevance of coherence is debated.", "map": "", "breaks": "Long-lived coherence claims were contested; biological functional relevance remains unclear.", "confidence": "proposed", "strength": 1}
{"id": "C1908", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/lindblad-master-equations", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Open-system dynamics of molecules", "kind": "method transfer", "summary": "Redfield and Lindblad master equations model electron and energy transfer in solvents, connecting to Marcus theory and system-bath treatments of reaction dynamics.", "map": "\\dot\\rho=-i[H,\\rho]+\\sum_k D[L_k]\\rho", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1909", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-thermodynamics", "b": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "name": "Fluctuation theorems in single molecules", "kind": "mechanism", "summary": "Jarzynski and Crooks relations were verified by pulling single RNA molecules with optical tweezers and extended to quantum systems in trapped-ion experiments.", "map": "\\langle e^{-\\beta W}\\rangle=e^{-\\beta\\Delta F}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1910", "a": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Entanglement and quantum Fisher information", "kind": "identity", "summary": "Metrological gain requires entanglement: the quantum Fisher information exceeding N bounds sensitivity and witnesses multipartite entanglement.", "map": "F_Q>N\\Rightarrow\\text{entangled}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1911", "a": "04-quantum-physics/quantum-information-and-computation/photonic-and-spin-qubits", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "NV centres: qubit and sensor", "kind": "shared object", "summary": "The nitrogen-vacancy centre is both a spin qubit and the leading solid-state nanoscale magnetometer, using identical initialization, microwave control and optical readout.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1912", "a": "04-quantum-physics/quantum-information-and-computation/photonic-and-spin-qubits", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Silicon spin qubits and transistors", "kind": "shared object", "summary": "Quantum-dot spin qubits are implemented in MOSFET-like gate-defined structures, so semiconductor industrial processing and device physics transfer directly.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1913", "a": "04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity", "b": "11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods", "name": "Quantum computing for electronic structure", "kind": "method transfer", "summary": "Phase estimation and variational eigensolvers target molecular ground-state energies, aiming to beat the exponential cost of exact classical full CI.", "map": "H|\\psi\\rangle=E|\\psi\\rangle", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1914", "a": "04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity", "b": "11-interdisciplinary-physics/chemical-physics/surface-science-and-catalysis", "name": "Quantum simulation of catalysts", "kind": "method transfer", "summary": "Strongly correlated active sites such as FeMoco in nitrogenase are prime targets for quantum simulation, where classical DFT struggles.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1915", "a": "04-quantum-physics/quantum-information-and-computation/quantum-error-correction-and-fault-tolerance", "b": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "name": "Kinetic proofreading and error suppression", "kind": "analogy", "summary": "Both biology and fault-tolerant quantum computing suppress error rates by spending energy and repeating checks, reaching lower error through dissipative, multi-step discrimination.", "map": "", "breaks": "Proofreading is classical and thermodynamic; QEC uses syndromes and non-demolition measurement.", "confidence": "proposed", "strength": 1}
{"id": "C1916", "a": "04-quantum-physics/quantum-information-and-computation/superconducting-qubits", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Solid-state device fabrication", "kind": "method transfer", "summary": "Superconducting qubits rely on semiconductor lithography and thin-film fabrication, and cryogenic CMOS control electronics link both; spin qubits are built in silicon MOS devices.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1917", "a": "04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "MRI as spin dynamics", "kind": "identity", "summary": "MRI is nuclear spin-1/2 precession in a magnetic field: Larmor frequency, Bloch equations, RF pulses and relaxation follow directly from angular-momentum algebra.", "map": "\\omega_L=\\gamma B_0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1918", "a": "04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "Spin and positronium physics in PET", "kind": "mechanism", "summary": "Positron annihilation via para-positronium produces back-to-back 511 keV photons, with angular-momentum and parity selection rules fixing the two-photon signature used in PET.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1919", "a": "04-quantum-physics/quantum-mechanics-core/approximation-methods", "b": "11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods", "name": "Perturbation and variational theory in chemistry", "kind": "identity", "summary": "Hartree–Fock, Møller–Plesset and configuration interaction are direct applications of the variational principle and Rayleigh–Schrödinger perturbation theory to many-electron systems.", "map": "E_0\\le\\langle\\psi|H|\\psi\\rangle", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1920", "a": "04-quantum-physics/quantum-mechanics-core/approximation-methods", "b": "11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods", "name": "Quantum chemistry as applied approximation theory", "kind": "identity", "summary": "Basis-set expansions, perturbative corrections and variational optimization in quantum chemistry are the approximation methods of core quantum mechanics at scale.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1921", "a": "04-quantum-physics/quantum-mechanics-core/approximation-methods", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Adiabatic theorem and Born–Oppenheimer", "kind": "identity", "summary": "The Born–Oppenheimer approximation is the adiabatic theorem applied to fast electrons; its breakdown near avoided crossings gives Landau–Zener transitions and nonadiabatic reaction dynamics.", "map": "P=e^{-2\\pi V^2/\\hbar v|\\Delta F|}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1922", "a": "04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems", "b": "11-interdisciplinary-physics/chemical-physics/surface-science-and-catalysis", "name": "Surface science and solvable models", "kind": "mechanism", "summary": "Tunnelling through barriers underlies scanning tunnelling microscopy, and square-well and Morse-type solvable models describe adsorbate binding and vibrations.", "map": "T\\sim e^{-2\\kappa d}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1923", "a": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Berry phase at conical intersections", "kind": "mechanism", "summary": "Conical intersections between potential energy surfaces carry a Berry phase of π, which changes nuclear wavefunction boundary conditions and affects reaction outcomes.", "map": "\\gamma=\\oint \\mathbf{A}\\cdot d\\mathbf{R}=\\pi", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1924", "a": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Instantons and tunnelling rates", "kind": "method transfer", "summary": "Semiclassical instanton theory computes tunnelling-dominated reaction rates and splittings, extending transition-state theory with Euclidean-action saddle points.", "map": "k\\propto e^{-S_E/\\hbar}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1925", "a": "04-quantum-physics/quantum-optics/cavity-optomechanics", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Optomechanical quantum-limited sensing", "kind": "shared object", "summary": "Optomechanical force and displacement sensors operate at the standard quantum limit with squeezed-light backaction evasion, as in LIGO-type and accelerometer devices.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1926", "a": "04-quantum-physics/quantum-optics/quantized-light-and-photon-statistics", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "FEL light statistics and coherence", "kind": "shared object", "summary": "SASE FEL radiation starts from shot noise and has chaotic-like spiky thermal statistics, characterised by g2 coherence functions, with seeded FELs approaching laser coherence.", "map": "g^{(2)}(0)=1+1/M", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1927", "a": "04-quantum-physics/quantum-optics/single-photon-sources-and-detectors", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "Single-photon detection in PET and optics", "kind": "method transfer", "summary": "Photon counting with SiPMs, avalanche photodiodes and fast timing is shared between quantum optics and time-of-flight PET, as is Poisson counting statistics.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1928", "a": "04-quantum-physics/quantum-optics/single-photon-sources-and-detectors", "b": "11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics", "name": "Photon counting in diffuse optics", "kind": "method transfer", "summary": "Time-correlated single-photon counting and SNSPDs enable diffuse optical tomography and fluorescence lifetime imaging in biomedical optics.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1929", "a": "04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology", "b": "11-interdisciplinary-physics/applied-and-device-physics", "name": "Applied devices exploit squeezed light", "kind": "method transfer", "summary": "Device-level sensing and metrology use nonclassical light from quantum optics to reduce shot noise below the standard quantum limit.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1930", "a": "04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Squeezing and entanglement-enhanced sensing", "kind": "method transfer", "summary": "Squeezed and entangled probe states beat the standard quantum limit toward the Heisenberg limit, applied in interferometers, magnetometers and spin ensembles.", "map": "\\Delta\\phi\\sim 1/\\sqrt{N}\\to 1/N", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2129", "a": "05-relativity-and-gravitation/black-holes/black-hole-imaging-and-astrophysical-black-holes", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Synchrotron radiation: light sources and the M87* ring", "kind": "mechanism", "summary": "The EHT's 1.3 mm emission is synchrotron radiation from relativistic electrons gyrating in magnetic fields near the horizon, governed by the same critical-frequency and polarization physics that light sources are engineered around. EHT polarimetry reads the synchrotron polarization pattern to map the geometry of the magnetic field.", "map": "\\nu_c=\\frac{3}{4\\pi}\\gamma^2\\frac{eB}{m_e}\\sin\\alpha", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2130", "a": "05-relativity-and-gravitation/black-holes/black-hole-imaging-and-astrophysical-black-holes", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Fourier-plane imaging: VLBI u-v coverage and MRI k-space", "kind": "method transfer", "summary": "An interferometer measures Fourier components (visibilities) of the sky, and MRI measures k-space samples of the magnetization, so both reconstruct images from sparse Fourier data using regularized or compressed-sensing inversion. Bracewell's projection-slice reconstructions in radio astronomy anticipated the mathematics of CT.", "map": "V(u,v)=\\iint I(x,y)e^{-2\\pi i(ux+vy)}dx\\,dy\\ \\leftrightarrow\\ S(\\mathbf k)=\\int m(\\mathbf r)e^{-2\\pi i\\mathbf k\\cdot\\mathbf r}d\\mathbf r", "breaks": "VLBI lacks absolute phases and must rely on closure quantities, while MRI records complex k-space data directly.", "confidence": "established", "strength": 2}
{"id": "C2131", "a": "05-relativity-and-gravitation/black-holes/black-hole-thermodynamics-and-hawking-radiation", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics", "name": "Wave blocking on currents as a white-hole horizon", "kind": "analogy", "summary": "Surface waves travelling against a strengthening current stop where the current speed equals their group velocity, which in the acoustic-metric picture is a white-hole horizon. Water-tank experiments measured Hawking-like mode conversion with a thermal-like amplitude ratio, and wave blocking at tidal inlets and river mouths is the same effect in the ocean.", "map": "U(x)=-c_g(k)\\ \\Rightarrow\\ \\text{horizon};\\quad T_H=\\frac{\\hbar\\kappa}{2\\pi k_B},\\ \\kappa\\simeq|\\partial_xU|_h", "breaks": "Water waves are strongly dispersive (no exact horizon or Lorentz symmetry) and damped by viscosity, and the experiments probe classical stimulated conversion; the spontaneous quantum emission is far too cold to measure.", "confidence": "current research", "strength": 2}
{"id": "C2132", "a": "05-relativity-and-gravitation/black-holes/schwarzschild-and-kerr-black-holes", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Photon sphere and transition state as unstable bottlenecks", "kind": "analogy", "summary": "The photon sphere is a normally hyperbolic invariant set of unstable orbits that separates capture from escape, like the dividing surface of transition-state theory in reaction dynamics. Its Lyapunov exponent sets the damping of eikonal quasinormal modes in the same way that the curvature of the barrier top sets the imaginary parts of quantized transition-state resonances.", "map": "\\omega_{\\ell n}\\approx\\ell\\Omega_c-i(n+\\tfrac12)\\lambda\\ \\leftrightarrow\\ E_n=V^\\ddagger-i\\hbar\\lambda(n+\\tfrac12)", "breaks": "The black-hole case is a single geodesic or linear wave on a fixed background, with no thermal ensemble or energy redistribution; reaction transition states live in many-dimensional phase space with recrossing and intramolecular energy flow.", "confidence": "proposed", "strength": 2}
{"id": "C2133", "a": "05-relativity-and-gravitation/general-relativity/modified-gravity", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Atom interferometry hunts screened fifth forces", "kind": "method transfer", "summary": "Chameleon and symmetron screening hide a scalar fifth force inside dense bodies behind a thin shell, but individual atoms in an ultra-high-vacuum chamber are unscreened. Atom-interferometric acceleration measurements near a source mass have therefore excluded much of the chameleon parameter space proposed to explain dark energy.", "map": "\\Phi=-\\frac{GM}{r}\\left(1+\\alpha\\,e^{-r/\\lambda}\\right),\\quad \\alpha_{\\rm eff}\\propto\\frac{\\Delta R}{R}\\ (\\text{thin shell})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2134", "a": "05-relativity-and-gravitation/general-relativity/numerical-relativity", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Junk radiation and geostrophic adjustment", "kind": "analogy", "summary": "Both fields evolve hyperbolic equations from initial data that must satisfy elliptic conditions: the Einstein constraints, or geostrophic and nonlinear-normal-mode balance. Data that are off the physical slow manifold shed spurious fast waves (junk radiation in binary simulations, inertia–gravity waves in weather models) that must be discarded before results are trusted, and both fields use Berger–Oliger adaptive mesh refinement.", "map": "", "breaks": "The Einstein constraints are exact identities that the evolution preserves, whereas atmospheric balance is approximate (small Rossby number) and not conserved; junk radiation leaves through the outer boundary, while unbalanced gravity waves can persist and are actively filtered.", "confidence": "proposed", "strength": 1}
{"id": "C2135", "a": "05-relativity-and-gravitation/general-relativity/tests-of-general-relativity", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Clocks and atom interferometers test redshift and the EP", "kind": "method transfer", "summary": "Pound and Rebka first measured gravitational redshift over 22.5 m; optical lattice clocks now resolve it across millimetres. Atom interferometers comparing two isotopes test the weak equivalence principle near 1e-12, and these are the same quantum devices used as gravimeters and timing references.", "map": "\\frac{\\Delta\\nu}{\\nu}=\\frac{g\\,\\Delta h}{c^2}\\approx1.1\\times10^{-16}\\,\\text{m}^{-1};\\quad \\eta=\\frac{2|a_1-a_2|}{|a_1+a_2|}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2136", "a": "05-relativity-and-gravitation/general-relativity/tests-of-general-relativity", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Frame dragging read out by SQUIDs and Sagnac gyroscopes", "kind": "method transfer", "summary": "Gravity Probe B measured geodetic and frame-dragging precession by reading the London moment of spinning superconducting rotors with SQUID magnetometers. Ring-laser and atom-interferometric Sagnac gyroscopes, which are also quantum-sensing devices, have been proposed to detect the Lense–Thirring effect on the ground (GINGER).", "map": "\\Delta\\phi_{\\rm Sagnac}=\\frac{2m}{\\hbar}\\,\\boldsymbol\\Omega\\cdot\\mathbf A;\\quad \\Omega_{\\rm LT}^{\\rm GP\\text{-}B}\\approx39\\ \\text{mas/yr}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2137", "a": "05-relativity-and-gravitation/general-relativity/tests-of-general-relativity", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Relativistic geodesy: clocks measure the geopotential", "kind": "method transfer", "summary": "A clock's rate depends on the gravitational potential, so comparing optical clocks at the 1e-18 level resolves height differences of about 1 cm, turning a GR test into a geodetic probe of Earth's gravity field and mass redistribution. In the other direction, satellite tests of frame dragging (LAGEOS) are limited by how well Earth's mass distribution is modelled.", "map": "\\frac{\\Delta\\nu}{\\nu}=\\frac{\\Delta U}{c^2}:\\ 10^{-18}\\leftrightarrow\\Delta h\\approx1\\ \\text{cm}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2138", "a": "05-relativity-and-gravitation/gravitational-waves/gravitational-wave-theory-and-waveforms", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Earth's normal modes as a gravitational-wave antenna", "kind": "shared object", "summary": "A GW's tidal acceleration drives the quadrupolar modes of an elastic body, the principle of Weber's bar. Dyson (1969) computed Earth's seismic response to a GW, and records of Earth's free oscillations have been used to bound the stochastic GW background; lunar seismic antennas are now proposed for the decihertz band.", "map": "\\ddot\\xi^i=\\tfrac12\\ddot h^{i}{}_{j}\\xi^j\\ \\to\\ \\text{spheroidal }{}_0S_2\\ (T\\approx54\\ \\text{min})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2139", "a": "05-relativity-and-gravitation/gravitational-waves/ground-based-detections", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Squeezed light beats the shot-noise limit in LIGO", "kind": "method transfer", "summary": "LIGO is the largest quantum sensor: shot noise enters through the vacuum at the dark port, so injecting squeezed vacuum (now frequency-dependent) lowers it, the same squeezed-state toolkit used in atomic magnetometers and clocks. The trade-off between shot noise and radiation-pressure noise defines the standard quantum limit that all continuous displacement sensors share.", "map": "\\delta\\phi=\\frac{e^{-r}}{\\sqrt{N}};\\quad h_{\\rm SQL}=\\sqrt{\\frac{8\\hbar}{m\\Omega^2L^2}}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2140", "a": "05-relativity-and-gravitation/gravitational-waves/ground-based-detections", "b": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "name": "Laser-read oscillators in a thermal bath", "kind": "analogy", "summary": "LIGO's test-mass suspensions and an optically trapped bead are both harmonic oscillators in a thermal bath, read out with light, whose displacement noise is fixed by the fluctuation–dissipation theorem. Optical tweezers are calibrated from the Lorentzian Brownian spectrum, and LIGO's thermal-noise budget comes from the mechanical loss entering the same formula.", "map": "S_x(\\omega)=\\frac{4k_BT}{\\omega}\\,\\mathrm{Im}\\,\\chi(\\omega);\\quad S_x^{\\rm bead}(f)=\\frac{k_BT}{\\pi^2\\gamma(f_c^2+f^2)}", "breaks": "LIGO works far above resonance, with tiny structural loss angles and quantum back-action, while a trapped bead is overdamped in water, classical, and probes forces rather than strain.", "confidence": "established", "strength": 1}
{"id": "C2141", "a": "05-relativity-and-gravitation/gravitational-waves/ground-based-detections", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics", "name": "Ocean microseism as a GW-detector noise source", "kind": "mechanism", "summary": "Opposing ocean swells generate pressure fluctuations at twice the wave frequency (the Longuet-Higgins mechanism), which travel through the ground as the 0.1–0.3 Hz secondary microseism. This ground motion dominates the seismic input to LIGO and Virgo and causes lock losses during ocean storms, so it shapes their isolation and control design.", "map": "f_{\\rm microseism}=2f_{\\rm swell}", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C2142", "a": "05-relativity-and-gravitation/gravitational-waves/ground-based-detections", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Newtonian noise and prompt elastogravity signals", "kind": "mechanism", "summary": "Seismic waves compress rock and so change local gravity. In GW detectors this Newtonian noise cannot be shielded and limits sensitivity below about 10 Hz, which is why the Einstein Telescope will be underground and why seismometer arrays are used for subtraction. In seismology the same effect produced prompt elastogravity signals, seen before the P-waves of the 2011 Tohoku earthquake.", "map": "\\delta\\rho=-\\nabla\\cdot(\\rho\\,\\mathbf u),\\quad \\delta\\mathbf g(\\mathbf r)=-G\\int\\frac{\\delta\\rho(\\mathbf r')(\\mathbf r-\\mathbf r')}{|\\mathbf r-\\mathbf r'|^3}d^3r'", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2143", "a": "05-relativity-and-gravitation/gravitational-waves/space-based-and-future-detectors", "b": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "name": "SRF cavities as high-frequency GW detectors", "kind": "method transfer", "summary": "Superconducting RF cavities built for accelerators, with quality factors above 1e10, are being repurposed as heterodyne GW detectors. A passing high-frequency GW deforms the walls and couples to the field, pumping power between two nearly degenerate modes (the MAGO concept) and opening a kHz–GHz window beyond the reach of interferometers.", "map": "\\omega_1-\\omega_0=\\omega_{\\rm g}", "breaks": "", "confidence": "current research", "strength": 1}
{"id": "C2144", "a": "05-relativity-and-gravitation/gravitational-waves/space-based-and-future-detectors", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Atom interferometers: from gravimeters to GW detectors", "kind": "method transfer", "summary": "The light-pulse atom interferometry used in quantum gravimeters and gradiometers is being scaled up into long-baseline gravitational-wave detectors (MAGIS-100, AION) for the 0.1–10 Hz gap between LIGO and LISA. The GW signal is a differential phase between two atom clouds that share the same laser pulses, so the detector is a gradiometer read out like a clock.", "map": "\\Delta\\phi_{\\rm grav}=k_{\\rm eff}\\,g\\,T^2", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2145", "a": "05-relativity-and-gravitation/gravitational-waves/space-based-and-future-detectors", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics", "name": "LISA-style laser ranging weighs the oceans (GRACE-FO)", "kind": "method transfer", "summary": "GRACE Follow-On carries a laser ranging interferometer that flight-tested the heterodyne inter-spacecraft ranging LISA will use. Its nanometre-precision ranging maps time-variable gravity, which measures ocean-bottom pressure, ice-sheet loss and the mass part of sea-level rise; combined with Argo floats it isolates ocean heat uptake.", "map": "\\Delta\\eta_{\\rm sea}=\\Delta\\eta_{\\rm mass}+\\Delta\\eta_{\\rm steric}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2146", "a": "05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft", "b": "11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods", "name": "Tensor networks: DMRG chemistry and MERA holography", "kind": "method transfer", "summary": "Matrix-product-state DMRG is a production quantum-chemistry method for strongly correlated active spaces. Its multiscale relative MERA builds a discrete AdS-like bulk whose minimal cuts give a Ryu–Takayanagi-like entanglement bound, and both methods work because ground-state entanglement obeys area laws.", "map": "S_A=\\frac{\\mathrm{Area}(\\gamma_A)}{4G_N}\\ \\leftrightarrow\\ S_A\\le|\\gamma_A|\\ln\\chi", "breaks": "Molecules lack the scale invariance that makes MERA holographic, and chemical DMRG orders orbitals on a 1D chain rather than building a geometric bulk.", "confidence": "current research", "strength": 1}