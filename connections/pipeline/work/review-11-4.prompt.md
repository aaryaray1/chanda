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


---

# Packet 11-4 (100 records)

{"id": "C2701", "a": "08-condensed-matter/crystals-and-electronic-structure/semiconductors", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Semiconductor physics and semiconductor devices", "kind": "shared object", "summary": "Doped silicon, III-V and wide-gap semiconductors are one object seen twice: condensed matter supplies gaps, mobilities, recombination and junction physics; device physics turns them into MOSFETs, LEDs, lasers and photovoltaics.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2702", "a": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "b": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "name": "Graphene nanopores for single-molecule sensing", "kind": "method transfer", "summary": "A single graphene layer is thinner than the spacing of DNA bases, so ionic current through a graphene nanopore resolves translocating molecules with sub-nanometre thickness, a step toward solid-state sequencing.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2703", "a": "08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Quantum-dot light emitters and photovoltaics", "kind": "method transfer", "summary": "Size-tuned colloidal and perovskite nanocrystals are used in displays (QLEDs), downconverters and solar cells; confinement sets the emission colour and multiple-exciton generation offers a route past the Shockley-Queisser limit.", "map": "E_g(R)\\approx E_g^{\\text{bulk}}+\\frac{\\hbar^2\\pi^2}{2R^2}\\left(\\frac1{m_e^*}+\\frac1{m_h^*}\\right)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2704", "a": "08-condensed-matter/low-dimensional-and-quantum-materials/transition-metal-dichalcogenides-and-excitons", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Two-dimensional semiconductor channels for transistors", "kind": "method transfer", "summary": "Monolayer MoS2 and related TMDs provide atomically thin channels with sizeable gaps, immune to short-channel effects that limit silicon scaling; contact resistance and dielectric integration are the open device problems.", "map": "\\lambda_{\\text{scale}}=\\sqrt{\\frac{\\epsilon_{ch}}{\\epsilon_{ox}}t_{ch}t_{ox}},\\ t_{ch}\\approx0.65\\,\\text{nm}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2705", "a": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "NV magnetometry imaging of 2D magnets", "kind": "method transfer", "summary": "Scanning single-spin (NV) magnetometry images stray fields of atomically thin magnets such as CrI3 quantitatively, resolving layer-dependent magnetization and domains; it is now a standard probe of 2D magnetism and spin textures.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2706", "a": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Crackling noise: Barkhausen jumps and earthquakes", "kind": "analogy", "summary": "Barkhausen noise from domain-wall avalanches in ferromagnets and earthquakes on faults both show power-law size distributions explained by depinning of an elastic interface in a random medium, the 'crackling noise' universality family.", "map": "P(S)\\sim S^{-\\tau}\\ (\\text{Barkhausen }\\tau\\approx1.3\\text{-}1.5)\\leftrightarrow N(>M)\\propto10^{-bM}\\ (\\text{Gutenberg-Richter},\\ b\\approx1)", "breaks": "Fault systems have long-range elastic interactions, healing and inertia that can produce characteristic quakes; universality-class assignments and exponents differ, and magnetic avalanches are tuned by an external field rather than tectonic loading.", "confidence": "established", "strength": 2}
{"id": "C2707", "a": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Rock magnetism and the paleomagnetic record", "kind": "mechanism", "summary": "Remanent magnetization of magnetite-bearing rocks, explained by Neel's theory of thermally activated single-domain grains, records the geomagnetic field; stripes of reversed magnetization on the sea floor confirmed sea-floor spreading and plate tectonics.", "map": "\\tau=\\tau_0\\exp\\left(\\frac{K_uV}{k_BT}\\right)\\ (\\text{Neel relaxation, blocking temperature})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2708", "a": "08-condensed-matter/magnetism/spintronics", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Spintronic memory and read heads in electronics", "kind": "method transfer", "summary": "Giant and tunnelling magnetoresistance moved from discovery to hard-disk read heads within a decade, and spin-transfer-torque MRAM is now embedded in CMOS logic processes as non-volatile memory.", "map": "\\text{TMR}=\\frac{2P_1P_2}{1-P_1P_2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2709", "a": "08-condensed-matter/soft-matter", "b": "11-interdisciplinary-physics/biophysics", "name": "Soft-matter physics of biological materials", "kind": "mechanism", "summary": "Membranes, biopolymers, gels and cytoskeletal networks have energies of order k_BT, so entropic elasticity, fluctuations, self-assembly and viscoelasticity, the core of soft matter, set the mechanics of cells and biomolecules.", "map": "k_BT\\approx4.1\\,\\text{pN nm}\\ (300\\,\\text{K})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2710", "a": "08-condensed-matter/soft-matter/active-matter", "b": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "name": "Cells and tissues as active matter", "kind": "mechanism", "summary": "The actomyosin cortex and epithelial tissues are active gels and active nematics; topological defects in epithelial monolayers localize stress and trigger cell extrusion, the same +1/2 defect physics as in microtubule active nematics.", "map": "\\sigma^{\\text{act}}_{ij}=-\\zeta\\Delta\\mu\\,Q_{ij},\\ Q_{ij}=S(n_in_j-\\tfrac12\\delta_{ij})", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2711", "a": "08-condensed-matter/soft-matter/active-matter", "b": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "name": "Flocking theory and collective animal behaviour", "kind": "mechanism", "summary": "Vicsek and Toner-Tu theories of polar active matter describe starling flocks, fish schools and bacterial swarms; field data showing starlings interact with a fixed number of topological neighbours fed back into active-matter models.", "map": "\\theta_i(t+1)=\\langle\\theta_j\\rangle_{j\\in\\mathcal N_i}+\\eta_i,\\ |\\mathcal N_i|\\approx6\\text{-}7\\ (\\text{topological})", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2712", "a": "08-condensed-matter/soft-matter/colloids-and-granular-matter", "b": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "name": "Brownian colloids as force probes", "kind": "method transfer", "summary": "Optical and magnetic tweezers are calibrated by the Brownian motion of a trapped colloidal bead: equipartition and the Lorentzian power spectrum with Stokes drag give the trap stiffness that turns position into force.", "map": "\\kappa\\langle x^2\\rangle=k_BT,\\ S_x(f)=\\frac{k_BT}{\\pi^2\\gamma(f_c^2+f^2)},\\ \\gamma=6\\pi\\eta a,\\ f_c=\\frac{\\kappa}{2\\pi\\gamma}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2713", "a": "08-condensed-matter/soft-matter/colloids-and-granular-matter", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Granular friction and earthquake faults", "kind": "mechanism", "summary": "Fault gouge is a sheared granular layer: rate-and-state friction, stick-slip instability, dilatancy and shear localization measured on granular materials explain earthquake nucleation and aftershock behaviour.", "map": "\\mu=\\mu_0+a\\ln\\frac{V}{V_0}+b\\ln\\frac{V_0\\theta}{D_c};\\ a-b<0\\Rightarrow\\text{stick-slip}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2714", "a": "08-condensed-matter/soft-matter/glasses-and-jamming", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Phase-change glasses for non-volatile memory", "kind": "mechanism", "summary": "Chalcogenide glasses such as Ge2Sb2Te5 switch in nanoseconds between amorphous and crystalline states with very different resistivity and reflectivity; crystallization kinetics and glass stability are the device physics of phase-change memory.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2715", "a": "08-condensed-matter/soft-matter/glasses-and-jamming", "b": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "name": "Jamming and unjamming of biological tissues", "kind": "mechanism", "summary": "Confluent epithelia undergo a rigidity (jamming) transition controlled by cell shape rather than density, analogous to athermal jamming; unjammed, fluid-like tissue is linked to wound healing, asthma and cancer invasion.", "map": "q=\\frac{P}{\\sqrt A},\\ q^*\\approx3.81\\ (\\text{vertex model rigidity});\\ \\text{jamming: }z_c=2d", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2716", "a": "08-condensed-matter/soft-matter/glasses-and-jamming", "b": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "name": "Rugged energy landscapes: glasses and protein folding", "kind": "method transfer", "summary": "Random-energy and spin-glass landscape ideas developed for glass formers were applied to proteins, giving the folding funnel and the principle of minimal frustration: foldable sequences have a folding temperature well above their glass temperature.", "map": "\\frac{T_f}{T_g}\\gg1\\ (\\text{foldable});\\ T_g\\ \\text{from REM: }S_c(T_g)=0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2717", "a": "08-condensed-matter/soft-matter/liquid-crystals", "b": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "name": "Helfrich elasticity: from liquid crystals to membranes", "kind": "historical", "summary": "Lipid bilayers are two-dimensional smectic-A liquid crystals; Helfrich, co-inventor of the twisted-nematic display, transferred Frank curvature elasticity to membranes, giving the bending energy that predicts red-blood-cell shapes and vesicle fluctuations.", "map": "F_{\\text{Frank}}\\ni\\tfrac12K_1(\\nabla\\cdot\\mathbf n)^2\\to F_{\\text{Helfrich}}=\\oint\\left[\\tfrac\\kappa2(2H-c_0)^2+\\bar\\kappa K\\right]dA,\\ 2H=\\nabla\\cdot\\mathbf n", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2718", "a": "08-condensed-matter/soft-matter/polymers", "b": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "name": "Proteins and nucleic acids as polymers", "kind": "mechanism", "summary": "Polymer physics (random walks, excluded volume, theta collapse, persistence length) gives the baseline for unfolded proteins and DNA; folding is a heteropolymer collapse with sequence-specific interactions.", "map": "R_g\\sim bN^{\\nu},\\ \\nu\\approx0.588\\ (\\text{good solvent, denatured})\\to\\nu=1/3\\ (\\text{compact globule})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2719", "a": "08-condensed-matter/soft-matter/polymers", "b": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "name": "Flory-Huggins phase separation and biomolecular condensates", "kind": "mechanism", "summary": "Membraneless organelles (P granules, nucleoli, stress granules) form by liquid-liquid phase separation of multivalent proteins and RNA, described with Flory-Huggins polymer-solution theory and its sticker-spacer extensions.", "map": "\\frac{\\Delta F_{\\text{mix}}}{k_BT}=\\frac\\phi N\\ln\\phi+(1-\\phi)\\ln(1-\\phi)+\\chi\\phi(1-\\phi),\\ \\chi_c=\\tfrac12(1+N^{-1/2})^2", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2720", "a": "08-condensed-matter/soft-matter/polymers", "b": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "name": "Worm-like chain elasticity of single DNA molecules", "kind": "identity", "summary": "Force-extension curves of single DNA molecules in optical and magnetic tweezers are fitted by the worm-like-chain model of semiflexible polymers, giving a 50 nm persistence length and confirming entropic elasticity at the single-molecule level.", "map": "F=\\frac{k_BT}{P}\\left[\\frac{1}{4(1-x/L)^2}-\\frac14+\\frac xL\\right],\\ P\\approx50\\,\\text{nm}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2721", "a": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "b": "11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods", "name": "DMRG, QMC and coupled cluster across fields", "kind": "method transfer", "summary": "DMRG, invented for 1D spin chains, became a leading method for strongly correlated molecules (active spaces of transition-metal clusters), while coupled cluster and quantum Monte Carlo moved from nuclear and quantum chemistry into solids; agreement across methods is the benchmark standard in both fields.", "map": "|\\psi\\rangle=\\sum\\mathrm{Tr}(A^{s_1}\\cdots A^{s_N})|s_1\\cdots s_N\\rangle\\ (\\text{orbitals as sites});\\ |\\Psi_{CC}\\rangle=e^{\\hat T}|\\Phi_0\\rangle", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2722", "a": "08-condensed-matter/superconductivity", "b": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "name": "Superconductors in accelerators", "kind": "method transfer", "summary": "Accelerators are the largest users of applied superconductivity: NbTi and Nb3Sn dipoles and quadrupoles bend and focus beams, and superconducting niobium RF cavities provide high-gradient, low-loss acceleration.", "map": "B\\rho\\,[\\text{T m}]=3.3356\\,p\\,[\\text{GeV}/c];\\ Q_0=\\omega U/P_{\\text{loss}}\\sim10^{10}\\text{-}10^{11}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2723", "a": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "b": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "name": "BCS surface resistance of SRF cavities", "kind": "mechanism", "summary": "Niobium superconducting RF cavities are limited by the BCS surface resistance from thermally excited quasiparticles, plus residual losses from trapped flux; nitrogen doping and Nb3Sn coatings are gap-engineering responses that raise Q0 and gradient.", "map": "R_s^{\\text{BCS}}\\approx\\frac{A\\omega^2}{T}e^{-\\Delta/k_BT}+R_{\\text{res}},\\ \\Delta_{\\text{Nb}}\\approx1.5\\,\\text{meV};\\ Q_0=G/R_s", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2724", "a": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Superconducting magnets for MRI", "kind": "shared object", "summary": "Clinical MRI scanners use persistent-mode NbTi solenoids at 1.5-7 T; type-II superconductivity with strong flux pinning gives the stable, homogeneous field whose Larmor frequency sets image signal and resolution.", "map": "\\omega_0=\\gamma B_0,\\ \\gamma/2\\pi=42.58\\,\\text{MHz/T};\\ \\text{SNR}\\propto B_0^{\\sim1}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2725", "a": "08-condensed-matter/superconductivity/cuprate-high-tc-superconductors", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Resonant inelastic X-ray scattering of cuprates", "kind": "method transfer", "summary": "High-resolution RIXS at synchrotrons measures paramagnons and charge-density-wave correlations in cuprates; it revealed incommensurate charge order competing with superconductivity in YBCO.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2726", "a": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "SQUID magnetometry", "kind": "method transfer", "summary": "SQUIDs turn flux quantization and Josephson interference into femtotesla magnetometers used for magnetoencephalography, geophysics, rock magnetism and condensed-matter susceptibility measurements.", "map": "I_c(\\Phi)=2I_0\\left|\\cos\\frac{\\pi\\Phi}{\\Phi_0}\\right|,\\ \\Phi_0=h/2e;\\ \\delta B\\sim\\text{fT}/\\sqrt{\\text{Hz}}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2727", "a": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Topological origin of equatorial waves", "kind": "method transfer", "summary": "Applying Chern-number band topology to the rotating shallow-water equations shows that the equatorial Kelvin and Yanai waves are topologically protected edge modes forced by the sign change of the Coriolis parameter at the equator.", "map": "\\text{Coriolis }f=\\beta y\\leftrightarrow\\text{Dirac mass }m(y);\\ C_\\pm=\\pm1\\Rightarrow\\Delta C=2\\ \\text{equatorial modes}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C2728", "a": "08-condensed-matter/topological-matter/topological-insulators", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Synchrotron ARPES of topological surface states", "kind": "method transfer", "summary": "Spin- and angle-resolved photoemission with tunable synchrotron light identified the odd number of spin-momentum-locked surface Dirac cones that define 3D topological insulators, and later Fermi arcs in Weyl semimetals.", "map": "E_{\\text{kin}}=h\\nu-\\phi-|E_B|,\\ k_\\parallel=\\sqrt{2mE_{\\text{kin}}}\\sin\\theta/\\hbar", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2796", "a": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Blackbody radiation and radiative equilibrium", "kind": "analogy", "summary": "Both rest on Planck blackbody radiation and radiative transfer: the CMB is a relic thermal spectrum, Earth's climate set by balance of absorbed sunlight and outgoing thermal radiation.", "map": "B_\\nu(T)=\\frac{2h\\nu^3}{c^2}\\frac{1}{e^{h\\nu/kT}-1}", "breaks": "The CMB is a decoupled relic freely streaming; Earth's emission is non-equilibrium and gray-body with strong absorption bands.", "confidence": "established", "strength": 2}
{"id": "C2797", "a": "09-astrophysics-and-cosmology/cosmology/gravitational-lensing", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Inverse problems and tomographic reconstruction", "kind": "method transfer", "summary": "Weak-lensing mass maps and CT/MRI reconstruction are regularized linear inverse problems, using Kaiser–Squires-type inversion, Wiener filtering and sparsity priors.", "map": "y=Ax+n", "breaks": "Lensing has sparse noisy sampling and shape noise; CT has controlled acquisition geometry.", "confidence": "established", "strength": 1}
{"id": "C2798", "a": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Quantum sensors for dark matter", "kind": "method transfer", "summary": "Axion and light dark-matter searches use SQUIDs, atomic magnetometers, NV centres, atomic clocks and interferometers; quantum-sensing techniques set sensitivity, including squeezing.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2799", "a": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "Low-background detectors and scintillation", "kind": "method transfer", "summary": "Scintillators, liquid xenon and time-of-flight photodetection developed for particle and dark-matter detection also drive PET detector design; low-noise photosensors cross over.", "map": "", "breaks": "Dark-matter detectors require extreme radiopurity and keV thresholds; PET needs high rate at 511 keV.", "confidence": "established", "strength": 1}
{"id": "C2800", "a": "09-astrophysics-and-cosmology/galaxies/active-galactic-nuclei-and-supermassive-black-holes", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Jets and undulator radiation", "kind": "analogy", "summary": "Relativistic jets emit synchrotron and inverse-Compton radiation, with Doppler boosting; undulators and FELs give coherent, narrow-band versions of the same radiation by accelerated charges.", "map": "", "breaks": "Jet emission is incoherent and broadband; FELs achieve coherence via microbunching.", "confidence": "established", "strength": 2}
{"id": "C2801", "a": "09-astrophysics-and-cosmology/galaxies/galaxy-clusters", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics", "name": "Turbulence in stratified fluids", "kind": "analogy", "summary": "Intracluster gas and the oceans are stratified turbulent fluids, with buoyancy-driven mixing and internal gravity waves described by Brunt–Väisälä frequency.", "map": "N^2=\\frac{g}{\\rho}\\frac{d\\rho}{dz}", "breaks": "Cluster gas is magnetized, weakly collisional plasma with cooling and AGN feedback.", "confidence": "current research", "strength": 1}
{"id": "C2802", "a": "09-astrophysics-and-cosmology/galaxies/the-milky-way", "b": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "name": "Statistical inference of dynamical systems", "kind": "method transfer", "summary": "Galactic archaeology and biophysical data analysis both use Bayesian inference and machine learning on large noisy catalogues; Gaia phase-space modelling parallels inference in living-systems data.", "map": "", "breaks": "The shared element is generic statistical practice.", "confidence": "proposed", "strength": 1}
{"id": "C2803", "a": "09-astrophysics-and-cosmology/galaxies/the-milky-way", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Rossby waves and density waves", "kind": "analogy", "summary": "Both feature large-scale rotating-fluid wave patterns: Rossby waves from the beta effect in atmospheres, and spiral density waves in rotating galactic disks with differential rotation, with analogous dispersion structure.", "map": "", "breaks": "Galactic disks are self-gravitating and collisionless stars; Rossby waves are restoring-force vorticity waves in a fluid.", "confidence": "current research", "strength": 1}
{"id": "C2804", "a": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "b": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "name": "Cosmic accelerators versus machines", "kind": "analogy", "summary": "Diffusive shock acceleration and Fermi mechanisms are natural counterparts of laboratory accelerators; the Hillas criterion parallels the size-times-field limit on achievable energy.", "map": "E_{max}\\sim Z e B R\\beta", "breaks": "Cosmic acceleration is stochastic, shock-based and power-law; machines use coherent, controlled RF fields.", "confidence": "established", "strength": 2}
{"id": "C2805", "a": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Synchrotron radiation in nature and the lab", "kind": "identity", "summary": "Relativistic electrons in magnetic fields emit synchrotron radiation, identical physics in AGN jets, pulsar nebulae and storage-ring light sources, with the same critical-frequency scaling.", "map": "\\omega_c=\\tfrac{3}{2}\\gamma^3\\,\\frac{c}{\\rho}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2806", "a": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Cosmic rays and air showers in the atmosphere", "kind": "shared object", "summary": "Cosmic rays are detected through extensive air showers developing in the atmosphere; cosmic-ray ionisation is also proposed to affect atmospheric electricity and cloud nucleation.", "map": "", "breaks": "Cosmic-ray cloud seeding is weak and disputed.", "confidence": "current research", "strength": 1}
{"id": "C2807", "a": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/cosmic-rays", "b": "11-interdisciplinary-physics/medical-physics/radiation-therapy", "name": "Cosmic-ray and hadron-therapy interactions", "kind": "shared object", "summary": "Heavy-ion transport, nuclear fragmentation and Bragg-peak energy loss are shared: galactic cosmic-ray shielding for astronauts uses the same codes and radiobiology as carbon-ion therapy.", "map": "-\\frac{dE}{dx}\\propto \\frac{Z^2}{\\beta^2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2808", "a": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/fast-radio-bursts-and-magnetars", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Coherent emission from bunched charges", "kind": "analogy", "summary": "FRB models invoke coherent curvature or maser emission from bunched charges, resembling coherent synchrotron radiation and FEL microbunching where power scales as N².", "map": "P_{coh}\\propto N^2 P_1", "breaks": "FRB coherence mechanism is unsettled; FELs rely on a known collective instability.", "confidence": "proposed", "strength": 2}
{"id": "C2809", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Planet spectra as molecular spectroscopy", "kind": "method transfer", "summary": "Identifying planetary atmospheric species relies on laboratory rovibrational line lists and selection rules; the same spectroscopy underlies remote sensing of planets and exoplanets.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2810", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Planetary climate as Earth climate physics", "kind": "shared object", "summary": "Energy balance, greenhouse effect and feedbacks developed for Earth apply to other planets and exoplanets, setting equilibrium temperatures and habitability.", "map": "T_{eq}=T_\\star\\sqrt{R_\\star/2a}\\,(1-A)^{1/4}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2811", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/astrobiology-and-habitability", "b": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "name": "Physical limits of life and biosignatures", "kind": "shared object", "summary": "Habitability asks which physical constraints (energy, chemistry, thermodynamics) permit life; physics of living systems quantifies those limits, such as energy use, noise and information processing.", "map": "", "breaks": "", "confidence": "current research", "strength": 1}
{"id": "C2812", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/astrobiology-and-habitability", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Habitable zone from climate feedbacks", "kind": "mechanism", "summary": "Habitable-zone edges are set by radiative-convective climate physics: runaway greenhouse from water-vapour feedback and ice-albedo snowball transitions, as in Earth climate models.", "map": "S_{eff}\\propto F_{OLR}/(1-A)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2813", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-atmospheres", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Spectroscopic databases serve exoplanet retrievals", "kind": "method transfer", "summary": "Line lists such as HITRAN and ExoMol, from quantum-chemistry and spectroscopy, are essential inputs for interpreting JWST exoplanet spectra.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2814", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-atmospheres", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Transmission spectra as molecular absorption", "kind": "method transfer", "summary": "Exoplanet transmission and emission spectra are decoded using molecular line lists, cross sections and Raman/collision-induced absorption knowledge from molecular spectroscopy.", "map": "\\delta(\\lambda)\\approx (R_p+n H(\\lambda))^2/R_\\star^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2815", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-atmospheres", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Greenhouse and inversion physics on other worlds", "kind": "shared object", "summary": "Greenhouse trapping, lapse rates and temperature inversions explain exoplanet thermal structure just as they do Earth's atmosphere.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2816", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-atmospheres", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Radiative transfer codes from Earth to exoplanets", "kind": "method transfer", "summary": "Radiative-convective models, correlated-k opacities and general circulation models built for Earth climate are reused for exoplanet atmospheres and retrievals.", "map": "", "breaks": "Earth-tuned assumptions (water condensation, near-1 bar) fail for hot Jupiters and non-solar compositions.", "confidence": "established", "strength": 2}
{"id": "C2817", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Astrochemistry in disks", "kind": "shared object", "summary": "Disk chemistry and the delivery of volatiles depend on gas-phase and grain-surface reaction rates, ion-molecule kinetics and snow lines, drawing on reaction-dynamics rate theory.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2818", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks", "b": "11-interdisciplinary-physics/chemical-physics/surface-science-and-catalysis", "name": "Grain-surface chemistry and catalysis", "kind": "mechanism", "summary": "H2 formation and ice mantle chemistry on dust grains proceed via adsorption, diffusion and Langmuir–Hinshelwood reactions, the same surface-science mechanisms as in heterogeneous catalysis.", "map": "", "breaks": "Interstellar grains are at ~10 K with quantum tunnelling, in ultra-low-density gas.", "confidence": "established", "strength": 2}
{"id": "C2819", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Rotating stratified turbulence in disks and atmospheres", "kind": "analogy", "summary": "Protoplanetary-disk vortices, zonal flows and Rossby wave instability parallel geophysical vortices and jets in rotating shear flows; Coriolis dynamics governs both.", "map": "", "breaks": "Disks involve magnetorotational turbulence, dust coupling and self-gravity.", "confidence": "current research", "strength": 2}
{"id": "C2820", "a": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Milankovitch cycles and orbital forcing", "kind": "mechanism", "summary": "Secular orbital perturbations change Earth's eccentricity, obliquity and precession, modulating insolation and driving glacial cycles.", "map": "", "breaks": "Climate response is nonlinear, with ice-sheet feedbacks.", "confidence": "established", "strength": 3}
{"id": "C2821", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Neutron-star asteroseismology and crust elasticity", "kind": "analogy", "summary": "Neutron-star crusts support shear modes and quakes analogous to earthquakes; magnetar giant-flare quasi-periodic oscillations are interpreted as crustal torsional modes, as in seismology.", "map": "", "breaks": "Crust is a Coulomb lattice at nuclear densities with extreme magnetic fields and superfluid coupling.", "confidence": "current research", "strength": 2}
{"id": "C2822", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "Positron annihilation and gamma detection", "kind": "shared object", "summary": "Positron annihilation producing 511 keV photons is used in PET and is observed in the Galactic 511 keV line; gamma-ray instrumentation overlaps with nuclear-medicine detectors, such as Compton cameras.", "map": "e^+e^-\\to\\gamma\\gamma", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2823", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "b": "11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods", "name": "Opacities and equations of state", "kind": "method transfer", "summary": "Stellar and planetary interiors require atomic opacities and equations of state computed with electronic-structure methods, including density functional and molecular dynamics for warm dense matter.", "map": "", "breaks": "Stellar plasmas are partially ionized at high temperature, beyond standard ground-state quantum chemistry.", "confidence": "established", "strength": 2}
{"id": "C2824", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Convection and radiative-convective structure", "kind": "mechanism", "summary": "Stellar envelopes and planetary atmospheres share Schwarzschild/lapse-rate stability criteria and mixing-length convection; the adiabatic gradient decides radiative versus convective layers.", "map": "\\nabla_{rad}>\\nabla_{ad}", "breaks": "Stars have radiation pressure, ionization and nuclear sources; atmospheres have moisture and rotation constraints.", "confidence": "established", "strength": 2}
{"id": "C2825", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Solar forcing of climate", "kind": "shared object", "summary": "Solar luminosity, its variability and the faint young Sun set the incoming flux in Earth's energy balance; solar cycle irradiance variations give a small forcing term.", "map": "S_0=L_\\odot/4\\pi d^2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2826", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Dynamo theory: Sun and geodynamo", "kind": "mechanism", "summary": "Solar and geodynamo both arise from MHD induction in convecting conducting fluid, with rotation and helicity (alpha-omega effect) driving field generation and reversals.", "map": "\\partial_t\\mathbf{B}=\\nabla\\times(\\mathbf{u}\\times\\mathbf{B})+\\eta\\nabla^2\\mathbf{B}", "breaks": "Solar dynamo is turbulent with strong stratification and a 11-yr cycle; geodynamo has low Rossby number and the solid inner core.", "confidence": "established", "strength": 3}
{"id": "C2827", "a": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Helioseismology and seismology inversions", "kind": "method transfer", "summary": "Both infer interior structure from observed wave modes and travel times via inversion: p-modes for the Sun, body and surface waves and normal modes for Earth. Methods and the mathematics of tomography parallel each other.", "map": "\\omega_{nl}\\ \\to\\ c(r),\\rho(r)", "breaks": "Solar modes are stochastically excited acoustic waves in a fluid; Earth has shear waves, discontinuities and sparse source locations.", "confidence": "established", "strength": 3}
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
{"id": "C2892", "a": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "SRF cavities and superconducting magnets with SQUIDs", "kind": "shared object", "summary": "Superconducting technology (niobium, cryogenics, flux control) is shared by accelerator cavities/magnets and SQUID sensors; SRF cavities also serve as quantum and dark-matter sensors.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C2893", "a": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Superconducting magnets in MRI and accelerators", "kind": "shared object", "summary": "NbTi superconducting magnet and cryogenic technology developed for accelerators is the basis of clinical MRI magnets; both need field homogeneity and quench protection.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2894", "a": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "Cyclotron isotope production for PET", "kind": "shared object", "summary": "Medical cyclotrons produce short-lived PET radioisotopes such as 18F and 11C, linking accelerator sources and targets to radiopharmaceutical supply.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2895", "a": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "b": "11-interdisciplinary-physics/medical-physics/radiation-therapy", "name": "Linacs and cyclotrons for radiotherapy", "kind": "shared object", "summary": "Medical linacs, proton cyclotrons and synchrotrons, and superconducting magnets/RF are accelerator technology deployed clinically; the Bragg-peak beam delivery rests on accelerator design.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2896", "a": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "b": "11-interdisciplinary-physics/medical-physics/radiation-therapy", "name": "Radiotherapy demands on accelerator design", "kind": "shared object", "summary": "Radiotherapy drives compact, reliable accelerator design: energy variation, FLASH dose rates, gantry-mounted superconducting magnets for proton and carbon-ion therapy.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C2897", "a": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Resonances and chaos in beams and fluids", "kind": "analogy", "summary": "Nonlinear resonances, Hamiltonian chaos and dynamic aperture in storage rings parallel Rossby-wave resonant interactions and predictability limits in atmospheric flow.", "map": "", "breaks": "Beam dynamics is conservative Hamiltonian; atmosphere is dissipative and forced.", "confidence": "proposed", "strength": 1}
{"id": "C2898", "a": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "b": "11-interdisciplinary-physics/medical-physics/radiation-therapy", "name": "Beam optics in proton therapy gantries", "kind": "method transfer", "summary": "Twiss parameters, emittance and focusing lattices determine spot size, beam transport and pencil-beam scanning in proton and carbon-ion therapy beamlines and gantries.", "map": "\\beta(s),\\ \\epsilon \\to \\sigma=\\sqrt{\\epsilon\\beta}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2899", "a": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "b": "11-interdisciplinary-physics/applied-and-device-physics/energy-materials-and-thermoelectrics", "name": "Synchrotron characterisation of battery materials", "kind": "method transfer", "summary": "Operando X-ray diffraction, absorption and tomography at synchrotrons track phase transformations and degradation in electrodes and solid electrolytes.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C2900", "a": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Free-electron laser vs. stimulated emission lasers", "kind": "analogy", "summary": "FEL gain from SASE microbunching is collective stimulated emission by free electrons, analogous to semiconductor laser gain but without bound-state inversion.", "map": "", "breaks": "FEL gain is classical bunching in an undulator, tunable and not tied to band gaps or carrier recombination.", "confidence": "established", "strength": 1}