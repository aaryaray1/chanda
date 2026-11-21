You are the quantum-physicist, the specialist for 04 (Quantum Physics) in this physics knowledge base.

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

## Field overview · `knowledge/04-quantum-physics`

> **Specialist:** `quantum-physicist` · **arXiv:** quant-ph, physics.atom-ph, cond-mat.quant-gas, physics.optics · **Literature source:** OpenAlex (citation-ranked) + arXiv (latest)

#### What this field studies
Quantum mechanics replaces definite trajectories with state vectors in Hilbert space, observables with operators, and outcomes with probabilities given by the Born rule. It explains atoms, chemistry, lasers, semiconductors and stars, and it has never failed an experimental test. This branch covers the theory itself, the still-debated question of what it means, the atomic and optical systems where it is tested most precisely, and the technologies — clocks, sensors, quantum computers, quantum networks — that exploit superposition and entanglement directly.

#### Conventions used in this branch
- SI units with $\hbar$ explicit unless stated; atomic units ($\hbar=m_e=e=4\pi\epsilon_0=1$) in atomic physics, flagged when used.
- Dirac notation; $\sigma_{x,y,z}$ Pauli matrices; computational basis $|0\rangle,|1\rangle$ with $Z|0\rangle=|0\rangle$.
- Density matrices $\rho$ for mixed states; fidelity $F(\rho,\sigma)=\left(\mathrm{Tr}\sqrt{\sqrt\rho\,\sigma\sqrt\rho}\right)^2$ (squared convention — say which).

#### Historical spine
1900 Planck quantum · 1905 photoelectric effect (Einstein) · 1913 Bohr atom · 1924 de Broglie waves · 1925 matrix mechanics (Heisenberg, Born, Jordan) · 1926 wave mechanics (Schrödinger), Born rule · 1927 uncertainty principle, Copenhagen · 1928 Dirac equation · 1935 EPR, Schrödinger's cat · 1952 Bohmian mechanics · 1957 Everett · 1960 laser · 1964 Bell's theorem · 1982 Aspect experiments · 1984 BB84, Berry phase · 1994 Shor's algorithm · 1995 BEC, first quantum error-correcting code · 2015 loophole-free Bell tests · 2019 quantum-advantage claims · 2022 Nobel for entanglement experiments · 2024 below-threshold surface-code memory · 2025 Nobel for macroscopic quantum tunnelling in circuits.

#### Canonical textbooks
- Griffiths & Schroeter, *Introduction to Quantum Mechanics* — undergraduate standard.
- Sakurai & Napolitano, *Modern Quantum Mechanics* — graduate standard.
- Cohen-Tannoudji, Diu & Laloë, *Quantum Mechanics* — encyclopedic.
- Nielsen & Chuang, *Quantum Computation and Quantum Information* — the QI reference.
- Foot, *Atomic Physics*; Gerry & Knight, *Introductory Quantum Optics*; Breuer & Petruccione, *The Theory of Open Quantum Systems*.

#### Live frontiers
- Fault-tolerant quantum computing: logical qubits below threshold, magic-state distillation, qLDPC codes.
- Optical clocks at $10^{-18}$ and a redefinition of the SI second.
- Quantum simulation of many-body and lattice-gauge physics with atom arrays.
- Tests of quantum mechanics with ever-larger masses (gravitational decoherence, entanglement via gravity).

#### How the specialist works here
Write the Hamiltonian and Hilbert space first; identify symmetries and conserved quantities; solve exactly where possible, otherwise state the approximation and its small parameter; check normalization, hermiticity, units and limiting cases. Distinguish interpretation-neutral predictions from interpretational claims.

## Atomic, molecular and optical physics · `knowledge/04-quantum-physics/atomic-molecular-and-optical-physics`

#### Overview
AMO physics is where quantum mechanics is tested most precisely and controlled most finely. Lasers cool atoms to nanokelvin, trap them in arrays of light, and interrogate them with $10^{-18}$ fractional precision. Ultracold gases are clean platforms for many-body physics, and atomic clocks and interferometers probe fundamental constants, gravity and dark matter.

#### Conceptual spine
1. Atom–light interaction: two-level atom, Rabi oscillations, AC Stark shift, spontaneous emission.
2. Radiation pressure + Doppler shift → cooling; light shifts → trapping.
3. At phase-space density $n\lambda_{\text{dB}}^3\gtrsim2.612$ bosons condense.
4. Feshbach resonances tune interactions; lattices tune kinetic energy → tunable many-body Hamiltonians.

#### Key equations
$$\Omega_R=\frac{\mathbf d\cdot\mathbf E_0}{\hbar},\qquad U_{\text{dip}}=-\frac{3\pi c^2}{2\omega_0^3}\frac{\Gamma}{\Delta}I(\mathbf r),\qquad k_BT_D=\frac{\hbar\Gamma}{2}$$

#### Open problems
- Redefinition of the SI second with optical clocks; clock networks for geodesy and dark-matter searches.
- Quantum simulation of the doped Fermi–Hubbard model (pseudogap, possible d-wave pairing).
- Electron EDM measurements probing CP violation at tens of TeV.

#### Connections
- [Quantum optics](knowledge/04-quantum-physics/quantum-optics/README.md) · [Neutral-atom qubits](knowledge/04-quantum-physics/quantum-information-and-computation/trapped-ion-and-neutral-atom-qubits/README.md) · [Hubbard model](knowledge/08-condensed-matter/strongly-correlated-electrons/hubbard-model-and-mott-physics/README.md) · [Fundamental constants](knowledge/00-foundations/units-and-constants/fundamental-constants/README.md)

### Atomic clocks and precision measurement · `knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement`

**Scope.** Cesium fountain (SI second), optical lattice clocks (Sr, Yb), single-ion clocks (Al⁺, Yb⁺), nuclear clock in ²²⁹Th, frequency combs, gravitational redshift at mm scales, atom-interferometric gravimetry and measurement of $G$ and $\alpha$, searches for variation of constants and ultralight dark matter.

**Core ideas.**
- Clock stability $\sigma_y\sim\frac{1}{Q}\frac{1}{\sqrt{N\tau}}$: higher frequency (optical vs. microwave) and more atoms win.
- At $10^{-18}$, clocks resolve the GR redshift for 1 cm height differences ($\Delta\nu/\nu=g\Delta h/c^2$).
- Atom interferometers measure inertial forces with phase $\phi=k_{\text{eff}}gT^2$.

**Key equations.**
$$\frac{\Delta\nu}{\nu}=\frac{g\,\Delta h}{c^2}\approx1.1\times10^{-18}\ \text{per cm}$$

**Landmark.** Ludlow et al. (2015) — see [subfield landmarks](knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/README.md).

**See also.** [SI units and the 2019 redefinition](knowledge/00-foundations/units-and-constants/si-units-and-2019-redefinition/README.md) · [Tests of general relativity](knowledge/05-relativity-and-gravitation/general-relativity/tests-of-general-relativity/README.md)

### Atomic structure and spectroscopy · `knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy`

**Scope.** Hydrogen fine structure (Dirac), Lamb shift (QED), hyperfine structure and the 21-cm line, multi-electron atoms (Hartree–Fock, LS vs. jj coupling, Hund's rules), Zeeman and Stark effects, dipole selection rules, Doppler-free and frequency-comb spectroscopy, Rydberg atoms.

**Core ideas.**
- Fine structure scales as $\alpha^2$ times the Bohr energy; Lamb shift as $\alpha^3\ln\alpha^{-1}$; hyperfine as $(m_e/m_p)\alpha^2$.
- Electric-dipole transitions need $\Delta\ell=\pm1$, $\Delta m=0,\pm1$.
- The frequency comb (Hänsch, Hall) links optical frequencies directly to microwave standards.

**Key equations.**
$$E_{nj}=-\frac{13.6\ \text{eV}}{n^2}\left[1+\frac{\alpha^2}{n^2}\left(\frac{n}{j+\frac12}-\frac34\right)\right],\qquad \nu_{21\,\text{cm}}=1420.405\ \text{MHz}$$

**See also.** [Angular momentum](knowledge/04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin/README.md) · [Molecular spectroscopy](knowledge/11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy/README.md)

### Bose–Einstein condensates and degenerate gases · `knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases`

**Scope.** BEC transition, Gross–Pitaevskii equation, Thomas–Fermi limit, Bogoliubov excitations, vortices and superfluidity, solitons, dipolar gases and supersolids, spinor condensates, degenerate Fermi gases, BEC–BCS crossover and unitary Fermi gas.

**Core ideas.**
- Condensation is a statistical effect for bosons; weak interactions make it a superfluid with linear (phonon) dispersion.
- The GP equation is a nonlinear Schrödinger equation for the condensate wavefunction.
- Near a Feshbach resonance, a Fermi gas crosses over smoothly from BCS pairs to a BEC of molecules.

**Key equations.**
$$k_BT_c=\frac{2\pi\hbar^2}{m}\left(\frac{n}{\zeta(3/2)}\right)^{2/3},\qquad i\hbar\partial_t\psi=\left[-\frac{\hbar^2\nabla^2}{2m}+V+g|\psi|^2\right]\psi,\ g=\frac{4\pi\hbar^2a}{m}$$

**See also.** [Quantum statistics](knowledge/03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics/README.md) · [BCS theory](knowledge/08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors/README.md)

### Laser cooling and trapping · `knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/laser-cooling-and-trapping`

**Scope.** Scattering force, optical molasses, Doppler limit, polarization-gradient (Sisyphus) cooling, recoil limit, magneto-optical trap, evaporative cooling, dipole traps and tweezers, gray molasses, Raman and sideband cooling, laser cooling of molecules.

**Core ideas.**
- Red-detuned light is absorbed preferentially by atoms moving toward the beam → velocity-dependent friction.
- Sisyphus cooling beats the Doppler limit, reaching a few recoil energies.
- Far-detuned light gives conservative potentials $\propto I/\Delta$: atoms are pulled to intensity maxima for red detuning.

**Key equations.**
$$F_{\text{scatt}}=\hbar k\frac{\Gamma}{2}\frac{s}{1+s+(2\delta/\Gamma)^2},\qquad T_{\text{rec}}=\frac{\hbar^2k^2}{mk_B}$$

**See also.** [Optical lattices](knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation/README.md) · [Single-molecule biophysics (tweezers)](knowledge/11-interdisciplinary-physics/biophysics/single-molecule-biophysics/README.md)

## Foundations of quantum mechanics · `knowledge/04-quantum-physics/foundations-of-quantum-mechanics`

#### Overview
Quantum mechanics is unambiguous as a predictive recipe but contested as a description of reality. Foundations research sharpens these questions into theorems (Bell, Kochen–Specker, PBR, Frauchiger–Renner) and experiments (Bell tests, macroscopic superpositions, Wigner's-friend scenarios). Many results here also became resources for quantum information.

#### Conceptual spine
1. Unitary evolution never produces a single definite outcome; the Born rule must be added or derived.
2. Bell: no local hidden-variable theory reproduces quantum correlations — confirmed experimentally.
3. Kochen–Specker: outcomes cannot be non-contextually pre-assigned.
4. Decoherence explains why interference becomes unobservable, but not by itself why one outcome occurs.

#### Key equations
$$|\langle A_0B_0\rangle+\langle A_0B_1\rangle+\langle A_1B_0\rangle-\langle A_1B_1\rangle|\le2\ (\text{local}),\qquad \le2\sqrt2\ (\text{quantum, Tsirelson})$$

#### Open problems
- Is there objective collapse (GRW, Penrose–Diósi), and can gravity-induced decoherence be detected?
- Status of the Born rule in many-worlds; meaning of probability.
- Can gravity entangle masses (tests of the quantum nature of gravity)?

#### Connections
- [Philosophy of physics](knowledge/00-foundations/history-and-philosophy-of-physics/philosophy-of-physics/README.md) · [Entanglement theory](knowledge/04-quantum-physics/quantum-information-and-computation/entanglement-theory/README.md) · [Quantum cryptography](knowledge/04-quantum-physics/quantum-information-and-computation/quantum-communication-and-cryptography/README.md)

### Contextuality · `knowledge/04-quantum-physics/foundations-of-quantum-mechanics/contextuality`

**Scope.** Kochen–Specker theorem, Peres–Mermin square, KCBS inequality, state-independent contextuality, experimental tests with ions and photons, contextuality as a resource for quantum computation (magic states).

**Core ideas.**
- In $\dim\mathcal H\ge3$ no assignment of definite values to all projectors respects functional relations among commuting observables.
- Unlike Bell tests, contextuality needs no spacelike separation — it holds for a single system.
- Contextuality is necessary for universal quantum advantage in magic-state models.

**Key equations.**
$$\text{Peres–Mermin: row products}=+\mathbb 1,\ \text{column products}=+\mathbb 1,+\mathbb 1,-\mathbb 1\ \Rightarrow\ \text{no consistent }\pm1\text{ assignment}$$

**See also.** [Bell nonlocality](knowledge/04-quantum-physics/foundations-of-quantum-mechanics/bell-nonlocality/README.md) · [Quantum algorithms](knowledge/04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity/README.md)

### Decoherence and the quantum-to-classical transition · `knowledge/04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical`

**Scope.** System–environment entanglement, reduced density matrices, pointer states and einselection, decoherence rates for macroscopic superpositions, quantum Darwinism, experiments (cavity QED cat states, fullerene interference), decoherence in qubits ($T_1$, $T_2$).

**Core ideas.**
- Tracing out an environment that records "which-path" information kills off-diagonal coherences in the pointer basis.
- Decoherence is fast for macroscopic objects: rates scale with $(\Delta x/\lambda_{\text{th}})^2$.
- It explains the appearance of classicality, not the selection of a single outcome.

**Key equations.**
$$\rho_S=\begin{pmatrix}|\alpha|^2&\alpha\beta^*\langle E_\downarrow|E_\uparrow\rangle\\ \alpha^*\beta\langle E_\uparrow|E_\downarrow\rangle&|\beta|^2\end{pmatrix},\qquad \langle E_\downarrow|E_\uparrow\rangle\to0$$

**Landmark.** Zurek (2003) — see [subfield landmarks](knowledge/04-quantum-physics/foundations-of-quantum-mechanics/README.md).

**See also.** [Lindblad master equations](knowledge/04-quantum-physics/open-and-many-body-quantum-dynamics/lindblad-master-equations/README.md) · [Superconducting qubits](knowledge/04-quantum-physics/quantum-information-and-computation/superconducting-qubits/README.md)

### Measurement problem and interpretations · `knowledge/04-quantum-physics/foundations-of-quantum-mechanics/measurement-problem-and-interpretations`

**Scope.** Von Neumann measurement chain, Schrödinger's cat, Wigner's friend and extended versions (Frauchiger–Renner, Brukner), Copenhagen, Everett/many-worlds, de Broglie–Bohm pilot wave, GRW/CSL collapse, QBism, relational QM, consistent histories.

**Core ideas.**
- The problem: linear unitary dynamics gives superpositions of pointer states, yet we observe one outcome.
- Interpretations differ in what they add (hidden variables, collapse) or deny (single outcomes, observer-independent facts); most make identical predictions.
- Collapse models are experimentally testable (heating, spontaneous radiation), and bounds are tightening.

**Key equations.**
$$\left(\alpha|{\uparrow}\rangle+\beta|{\downarrow}\rangle\right)|M_0\rangle\ \xrightarrow{U}\ \alpha|{\uparrow}\rangle|M_\uparrow\rangle+\beta|{\downarrow}\rangle|M_\downarrow\rangle$$

**See also.** [Decoherence](knowledge/04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical/README.md) · [Philosophy of physics](knowledge/00-foundations/history-and-philosophy-of-physics/philosophy-of-physics/README.md)

## Open and many-body quantum dynamics · `knowledge/04-quantum-physics/open-and-many-body-quantum-dynamics`

#### Overview
Real quantum systems leak into their environments, and large isolated systems behave thermally even though their evolution is unitary. This branch studies both: Markovian and non-Markovian open-system dynamics, the thermodynamics of quantum machines, how isolated systems thermalize (or fail to), quantum chaos and information scrambling, and the new phases that appear in periodically driven and non-Hermitian systems.

#### Conceptual spine
1. Trace out the bath → completely positive dynamics; under Born–Markov assumptions → Lindblad form.
2. Isolated systems: local observables thermalize if eigenstates are thermal (ETH); exceptions are integrable or localized systems.
3. Chaos is diagnosed by level statistics and OTOC growth.
4. Driving and dissipation are design tools, not just nuisances.

#### Key equations
$$\dot\rho=-\frac{i}{\hbar}[H,\rho]+\sum_k\gamma_k\left(L_k\rho L_k^\dagger-\tfrac12\{L_k^\dagger L_k,\rho\}\right)$$

#### Open problems
- Is many-body localization stable in the thermodynamic limit?
- Thermodynamic costs of quantum computation and measurement.

#### Connections
- [Non-equilibrium statistical mechanics](knowledge/03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/README.md) · [Black-hole information](knowledge/05-relativity-and-gravitation/black-holes/information-paradox/README.md) · [Decoherence](knowledge/04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical/README.md)

### Floquet systems and time crystals · `knowledge/04-quantum-physics/open-and-many-body-quantum-dynamics/floquet-systems-and-time-crystals`

**Scope.** Floquet theorem and quasienergies, high-frequency (Magnus) expansions, Floquet topological insulators, heating and prethermalization in driven systems, discrete time crystals (period doubling robust to perturbations), experiments with ions, NV centers and superconducting processors.

**Core ideas.**
- Periodic drive → effective static Hamiltonian at high frequency; drives can create synthetic gauge fields and topology.
- Generic interacting driven systems heat to infinite temperature, but heating can be exponentially slow (prethermal regime).
- Time crystals spontaneously break discrete time-translation symmetry; equilibrium time crystals are forbidden (no-go theorems).

**Key equations.**
$$|\psi(t)\rangle=e^{-i\varepsilon t/\hbar}|\phi(t)\rangle,\ |\phi(t+T)\rangle=|\phi(t)\rangle;\qquad H_{\text{eff}}\approx\bar H+\frac{1}{\hbar\omega}\sum_{m>0}\frac{[H_m,H_{-m}]}{m}$$

**See also.** [Parametric oscillations](knowledge/01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations/README.md) · [Topological insulators](knowledge/08-condensed-matter/topological-matter/topological-insulators/README.md)

### Lindblad master equations · `knowledge/04-quantum-physics/open-and-many-body-quantum-dynamics/lindblad-master-equations`

**Scope.** Completely positive trace-preserving maps, Kraus operators, GKSL theorem, Born–Markov–secular approximations, optical Bloch equations, quantum jumps and trajectories, non-Markovian dynamics, reservoir engineering, Liouvillian gaps.

**Core ideas.**
- The most general Markovian generator has the GKSL (Lindblad) form; jump operators $L_k$ encode decay, dephasing and pumping.
- Unravelling into stochastic trajectories matches what continuously monitored experiments see.
- Dissipation can be engineered to stabilize useful states (e.g., cat qubits).

**Key equations.**
$$\rho\mapsto\sum_kK_k\rho K_k^\dagger,\ \sum_kK_k^\dagger K_k=\mathbb 1;\qquad T_2\le2T_1$$

**See also.** [Decoherence](knowledge/04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical/README.md) · [Langevin dynamics](knowledge/03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics/README.md)

### Non-Hermitian physics · `knowledge/04-quantum-physics/open-and-many-body-quantum-dynamics/non-hermitian-physics`

**Scope.** PT-symmetric Hamiltonians with real spectra, PT-breaking transitions, exceptional points and enhanced sensing debates, non-Hermitian topology and the skin effect, implementations in photonics, acoustics, electric circuits and post-selected quantum systems.

**Core ideas.**
- Gain/loss described by complex potentials; PT symmetry can still give real eigenvalues in the unbroken phase.
- At an exceptional point eigenvalues and eigenvectors coalesce — spectra respond as $\sqrt\epsilon$ to perturbations.
- The skin effect piles all eigenstates at a boundary, breaking conventional bulk–boundary correspondence.

**Key equations.**
$$H=\begin{pmatrix}\omega+i\gamma&\kappa\\\kappa&\omega-i\gamma\end{pmatrix},\qquad \lambda_\pm=\omega\pm\sqrt{\kappa^2-\gamma^2}$$

**Landmark.** Bender & Boettcher (1998) — see [subfield landmarks](knowledge/04-quantum-physics/open-and-many-body-quantum-dynamics/README.md).

**See also.** [Topological photonics](knowledge/02-electromagnetism-and-optics/photonics-and-lasers/topological-photonics/README.md)

### Quantum chaos and scrambling · `knowledge/04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling`

**Scope.** BGS conjecture, Wigner–Dyson vs. Poisson level spacing, spectral form factor, OTOCs and quantum Lyapunov exponents, the MSS bound $\lambda_L\le2\pi k_BT/\hbar$, SYK model, operator growth, scrambling experiments.

**Core ideas.**
- Classically chaotic systems have quantum spectra with level repulsion matching random-matrix ensembles; integrable ones show Poisson statistics.
- OTOCs $\langle[W(t),V]^\dagger[W(t),V]\rangle$ measure how fast local information spreads.
- Black holes saturate the chaos bound — "fastest scramblers".

**Key equations.**
$$P_{\text{GOE}}(s)\approx\frac{\pi s}{2}e^{-\pi s^2/4},\qquad P_{\text{Poisson}}(s)=e^{-s},\qquad \lambda_L\le\frac{2\pi k_BT}{\hbar}$$

**See also.** [Deterministic chaos](knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos/README.md) · [Information paradox](knowledge/05-relativity-and-gravitation/black-holes/information-paradox/README.md)

### Thermalization and the eigenstate thermalization hypothesis · `knowledge/04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth`

**Scope.** ETH ansatz, quantum quenches, generalized Gibbs ensembles for integrable systems, prethermalization, many-body localization and its stability debate, quantum many-body scars (Rydberg chains), Hilbert-space fragmentation, cold-atom and ion tests.

**Core ideas.**
- ETH: individual energy eigenstates look thermal for local observables, so long-time averages match the microcanonical ensemble.
- Integrable systems relax to a GGE fixed by their extensive conserved quantities.
- Scars and fragmentation are weak ergodicity-breaking mechanisms giving long-lived oscillations.

**Key equations.**
$$\langle E_m|O|E_n\rangle=O(\bar E)\,\delta_{mn}+e^{-S(\bar E)/2}f_O(\bar E,\omega)\,R_{mn}$$

**See also.** [Ensembles and partition functions](knowledge/03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions/README.md) · [Disorder and localization](knowledge/03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/localization-and-disorder/README.md)

## Quantum information and computation · `knowledge/04-quantum-physics/quantum-information-and-computation`

#### Overview
Quantum information treats superposition and entanglement as resources. A quantum computer manipulates $n$ qubits in a $2^n$-dimensional space; for certain problems (factoring, simulating quantum matter) this gives super-polynomial speedups. Noise is the central obstacle: quantum error correction encodes logical qubits in many physical ones, and the threshold theorem guarantees arbitrarily reliable computation if physical error rates are below ~1%.

#### Conceptual spine
1. Qubits, gates (universal sets: Clifford + T), measurement; circuits as unitary products.
2. Entanglement and interference provide computational power; no-cloning forbids copying unknown states.
3. Errors are discretized by syndrome measurement; codes with distance $d$ correct $\lfloor(d-1)/2\rfloor$ errors.
4. Hardware is judged by gate fidelity, coherence, connectivity, speed and scalability.

#### Key equations
$$|\psi\rangle=\sum_{x\in\{0,1\}^n}c_x|x\rangle,\qquad p_L\approx A\left(\frac{p}{p_{\text{th}}}\right)^{\lfloor(d+1)/2\rfloor}$$

#### Open problems
- Which useful problems have provable, practical quantum advantage?
- Overhead reduction: qLDPC codes, magic-state cultivation, better decoders.
- Scaling to millions of physical qubits with manageable wiring, cooling and control.

#### Connections
- [Foundations](knowledge/04-quantum-physics/foundations-of-quantum-mechanics/README.md) · [Topological order and anyons](knowledge/08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order/README.md) · [Josephson junctions](knowledge/08-condensed-matter/superconductivity/josephson-effect-and-squids/README.md) · [Entropy and information](knowledge/03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information/README.md)

### Entanglement theory · `knowledge/04-quantum-physics/quantum-information-and-computation/entanglement-theory`

**Scope.** Separable vs. entangled states, Schmidt decomposition, PPT (Peres–Horodecki) criterion, entanglement witnesses, entropy of entanglement, concurrence, negativity, distillation and bound entanglement, monogamy (CKW), area laws, multipartite entanglement (GHZ vs. W).

**Core ideas.**
- A pure bipartite state is entangled iff its Schmidt rank > 1; its entanglement is the von Neumann entropy of either reduced state.
- LOCC cannot create entanglement — it is a resource that can be converted and consumed (teleportation uses 1 ebit + 2 classical bits per qubit).
- Ground states of gapped local Hamiltonians obey area laws — why tensor networks work.

**Key equations.**
$$S(\rho_A)=-\mathrm{Tr}\,\rho_A\log_2\rho_A,\qquad |\Phi^+\rangle=\tfrac{1}{\sqrt2}(|00\rangle+|11\rangle)$$

**Landmark.** Horodecki et al. (2009) — see [subfield landmarks](knowledge/04-quantum-physics/quantum-information-and-computation/README.md).

**See also.** [Bell nonlocality](knowledge/04-quantum-physics/foundations-of-quantum-mechanics/bell-nonlocality/README.md) · [Tensor network methods](knowledge/00-foundations/computational-physics/tensor-network-methods/README.md)

### Quantum algorithms and complexity · `knowledge/04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity`

**Scope.** Quantum Fourier transform, phase estimation, Shor's factoring, Grover search and amplitude amplification, Hamiltonian simulation (Trotter, qubitization), HHL, VQE and QAOA, BQP and its relation to NP and PH, random-circuit sampling and boson-sampling advantage, dequantization results.

**Core ideas.**
- Exponential speedups come from structure (periodicity, simulation of quantum dynamics), not from "trying all answers".
- Grover's quadratic speedup is optimal for unstructured search.
- Quantum-advantage claims are contested by improved classical simulation; verifiability matters.

**Key equations.**
$$\text{QFT}:|x\rangle\mapsto\frac{1}{\sqrt N}\sum_ye^{2\pi ixy/N}|y\rangle,\qquad T_{\text{Grover}}\approx\frac\pi4\sqrt{N}$$

**See also.** [Quantum chemistry methods](knowledge/11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods/README.md)

### Superconducting qubits · `knowledge/04-quantum-physics/quantum-information-and-computation/superconducting-qubits`

**Scope.** Cooper-pair box → transmon, flux and phase qubits, fluxonium, cQED readout, $T_1$/$T_2$ and loss mechanisms (TLS defects, quasiparticles), tunable couplers, two-qubit gates (CZ, iSWAP, cross-resonance), cryogenic wiring, cosmic-ray-induced correlated errors.

**Core ideas.**
- The Josephson junction is a non-linear inductor, giving an anharmonic oscillator whose two lowest levels form a qubit.
- The transmon ($E_J/E_C\sim50$) is exponentially insensitive to charge noise at the cost of weak anharmonicity.
- Lithographic fabrication makes scaling natural; materials losses limit coherence.

**Key equations.**
$$H=4E_C(\hat n-n_g)^2-E_J\cos\hat\varphi,\qquad \omega_{01}\approx\sqrt{8E_JE_C}-E_C$$

**Landmark.** Koch et al. (2007). "Charge-insensitive qubit design derived from the Cooper pair box". *Phys. Rev. A* 76, 042319. [arXiv:cond-mat/0703002](https://arxiv.org/abs/cond-mat/0703002)

**See also.** [Josephson effect and SQUIDs](knowledge/08-condensed-matter/superconductivity/josephson-effect-and-squids/README.md) · [Cavity and circuit QED](knowledge/04-quantum-physics/quantum-optics/cavity-and-circuit-qed/README.md)

### Trapped-ion and neutral-atom qubits · `knowledge/04-quantum-physics/quantum-information-and-computation/trapped-ion-and-neutral-atom-qubits`

**Scope.** Paul traps, hyperfine and optical qubits, Mølmer–Sørensen gates, QCCD architectures with ion shuttling, optical tweezer arrays, Rydberg blockade gates, atom rearrangement and mid-circuit measurement, logical-qubit demonstrations.

**Core ideas.**
- Atoms are identical, so qubits are naturally uniform with long coherence (seconds to minutes).
- Ions couple via shared motional modes; neutral atoms via the Rydberg blockade within a radius $R_b=(C_6/\hbar\Omega)^{1/6}$.
- Reconfigurable connectivity (shuttling, moving tweezers) enables efficient error-correcting codes.

**Key equations.**
$$V_{\text{Ryd}}(r)=\frac{C_6}{r^6},\qquad C_6\propto n^{11}$$

**Landmark.** Cirac & Zoller (1995). "Quantum Computations with Cold Trapped Ions". *Phys. Rev. Lett.* 74, 4091. [doi:10.1103/PhysRevLett.74.4091](https://doi.org/10.1103/PhysRevLett.74.4091)

**See also.** [Laser cooling and trapping](knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/laser-cooling-and-trapping/README.md) · [Optical lattices](knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation/README.md)

## Quantum mechanics: formalism and methods · `knowledge/04-quantum-physics/quantum-mechanics-core`

#### Overview
The working toolkit of quantum mechanics: states and operators, time evolution, and the handful of exactly solvable models (harmonic oscillator, hydrogen, spin-½) from which almost everything else is built by approximation.

#### Conceptual spine
1. State $|\psi\rangle\in\mathcal H$; observables are Hermitian operators; outcomes are eigenvalues with probability $|\langle a|\psi\rangle|^2$.
2. Unitary evolution $i\hbar\,\partial_t|\psi\rangle=H|\psi\rangle$ between measurements.
3. Non-commuting observables obey uncertainty relations $\sigma_A\sigma_B\ge\frac12|\langle[A,B]\rangle|$.
4. Composite systems use tensor products — the origin of entanglement.

#### Key equations
$$i\hbar\frac{\partial\psi}{\partial t}=\left[-\frac{\hbar^2}{2m}\nabla^2+V\right]\psi,\qquad [\hat x,\hat p]=i\hbar,\qquad \sigma_x\sigma_p\ge\frac{\hbar}{2}$$

#### Open problems
- Efficient methods for strongly interacting many-particle systems (the exponential wall).
- Rigorous control of perturbation series (most are asymptotic, not convergent).

#### Connections
- [Foundations](knowledge/04-quantum-physics/foundations-of-quantum-mechanics/README.md) · [Linear algebra and Hilbert spaces](knowledge/00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces/README.md) · [Quantum field theory](knowledge/06-particle-physics/quantum-field-theory/README.md)

### Angular momentum and spin · `knowledge/04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin`

**Scope.** $[J_i,J_j]=i\hbar\epsilon_{ijk}J_k$, spherical harmonics, spin-½ and Pauli matrices, Stern–Gerlach, Clebsch–Gordan coefficients, Wigner–Eckart theorem, spin–orbit and hyperfine coupling, spin precession (Larmor), spinors and the $4\pi$ rotation.

**Core ideas.**
- Eigenvalues $J^2\to\hbar^2j(j+1)$, $J_z\to\hbar m$ with $j$ integer or half-integer.
- Spin is intrinsic angular momentum with no classical analogue; $g_e\approx2.0023$.
- Selection rules follow from the Wigner–Eckart theorem.

**Key equations.**
$$|j_1-j_2|\le J\le j_1+j_2,\qquad H_{\text{SO}}=\frac{1}{2m_e^2c^2}\frac{1}{r}\frac{dV}{dr}\,\mathbf L\cdot\mathbf S$$

**See also.** [Lie groups and representations](knowledge/00-foundations/symmetry-and-group-theory/lie-groups-and-representations/README.md) · [Spintronics](knowledge/08-condensed-matter/magnetism/spintronics/README.md)

### Approximation methods · `knowledge/04-quantum-physics/quantum-mechanics-core/approximation-methods`

**Scope.** Rayleigh–Schrödinger and degenerate perturbation theory, Stark and Zeeman effects, fine structure, variational principle (helium ground state), WKB and connection formulas, sudden and adiabatic approximations, Fermi's golden rule, Landau–Zener transitions.

**Core ideas.**
- Perturbation theory needs a small dimensionless parameter; degenerate levels must first be diagonalized within the degenerate subspace.
- The variational energy is always an upper bound on the ground-state energy.
- Golden rule: transition rate = $(2\pi/\hbar)|V_{fi}|^2\times$ density of final states.

**Key equations.**
$$E_n^{(2)}=\sum_{m\neq n}\frac{|\langle m|V|n\rangle|^2}{E_n-E_m},\qquad \Gamma_{i\to f}=\frac{2\pi}{\hbar}|\langle f|V|i\rangle|^2\rho(E_f)$$

**See also.** [Scattering theory](knowledge/04-quantum-physics/quantum-mechanics-core/scattering-theory/README.md) · [Quantum chemistry methods](knowledge/11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods/README.md)

### Exactly solvable systems · `knowledge/04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems`

**Scope.** Infinite/finite wells, delta potentials, tunnelling through barriers, harmonic oscillator via ladder operators, coherent states, hydrogen (Coulomb) problem and its hidden SO(4) symmetry, Morse and Pöschl–Teller potentials, supersymmetric QM.

**Core ideas.**
- Ladder operators $a=\sqrt{m\omega/2\hbar}\,(x+ip/m\omega)$ give $E_n=\hbar\omega(n+\tfrac12)$ algebraically.
- Hydrogen's accidental degeneracy in $\ell$ comes from the conserved Runge–Lenz vector.
- Transmission through a barrier falls as $e^{-2\kappa L}$ — basis of tunnelling microscopy and alpha decay.

**Key equations.**
$$E_n^{\text{H}}=-\frac{m_ee^4}{2(4\pi\epsilon_0)^2\hbar^2n^2}=-\frac{13.6\ \text{eV}}{n^2},\qquad a_0=\frac{4\pi\epsilon_0\hbar^2}{m_ee^2}\approx0.529\ \text{Å}$$

**See also.** [Alpha decay](knowledge/07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay/README.md) · [Atomic structure](knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy/README.md)

### Geometric phases · `knowledge/04-quantum-physics/quantum-mechanics-core/geometric-phases`

**Scope.** Adiabatic transport, Berry connection and curvature, Aharonov–Bohm and Aharonov–Casher effects, Pancharatnam phase in optics, non-abelian (Wilczek–Zee) holonomies, links to Chern numbers and the quantum Hall effect.

**Core ideas.**
- A state transported adiabatically around a closed loop in parameter space acquires a gauge-invariant phase that depends only on the loop's geometry.
- The AB effect shows that potentials, not just fields, are physical in quantum mechanics.
- Berry curvature integrated over a Brillouin zone gives integer Chern numbers — the root of topological band theory.

**Key equations.**
$$\gamma_n(C)=i\oint_C\langle n(\mathbf R)|\nabla_{\mathbf R}n(\mathbf R)\rangle\cdot d\mathbf R,\qquad \Delta\phi_{\text{AB}}=\frac{q\Phi_B}{\hbar}$$

**See also.** [Band topology and Berry curvature](knowledge/08-condensed-matter/topological-matter/band-topology-and-berry-curvature/README.md) · [Gauge invariance in EM](knowledge/02-electromagnetism-and-optics/electrodynamics/potentials-and-gauge-invariance/README.md)

### Path integrals and semiclassics · `knowledge/04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics`

**Scope.** Propagator as a sum over paths, time-slicing, Gaussian integrals, stationary phase and the classical limit, Van Vleck–Gutzwiller propagator, Bohr–Sommerfeld quantization, Euclidean path integral and instantons for tunnelling, imaginary-time thermal path integral.

**Core ideas.**
- Each path contributes $e^{iS/\hbar}$; when $S\gg\hbar$, paths near the classical one dominate by stationary phase.
- Imaginary time $t=-i\tau$ turns quantum mechanics into statistical mechanics: $Z=\mathrm{Tr}\,e^{-\beta H}$ is a periodic path integral.
- Tunnelling rates come from Euclidean "bounce/instanton" solutions: $\Gamma\propto e^{-S_E/\hbar}$.

**Key equations.**
$$K(x_b,t_b;x_a,t_a)=\int\mathcal Dx\;e^{\frac{i}{\hbar}\int_{t_a}^{t_b}L(x,\dot x)\,dt},\qquad \oint p\,dq=2\pi\hbar\left(n+\tfrac12\right)$$

**Landmark.** Feynman (1948) — see [subfield landmarks](knowledge/04-quantum-physics/quantum-mechanics-core/README.md).

**See also.** [Canonical and path-integral quantization](knowledge/06-particle-physics/quantum-field-theory/canonical-and-path-integral-quantization/README.md) · [Variational principles](knowledge/01-classical-mechanics/analytical-mechanics/variational-principles/README.md)

### Postulates and formalism · `knowledge/04-quantum-physics/quantum-mechanics-core/postulates-and-formalism`

**Scope.** Kets, bras, operators, spectral decomposition, commutators, Schrödinger/Heisenberg/interaction pictures, density operators, partial trace, POVMs, Gleason's theorem.

**Core ideas.**
- Pure states are rays in $\mathcal H$; mixed states are positive, unit-trace operators $\rho$.
- Expectation values $\langle A\rangle=\mathrm{Tr}(\rho A)$; the reduced state of a subsystem is $\rho_A=\mathrm{Tr}_B\,\rho_{AB}$.
- Generalized measurements (POVMs) cover realistic, imperfect detection.

**Key equations.**
$$\frac{d\langle A\rangle}{dt}=\frac{i}{\hbar}\langle[H,A]\rangle+\left\langle\frac{\partial A}{\partial t}\right\rangle,\qquad \rho(t)=U\rho(0)U^\dagger$$

**See also.** [Measurement problem](knowledge/04-quantum-physics/foundations-of-quantum-mechanics/measurement-problem-and-interpretations/README.md) · [Hilbert spaces](knowledge/00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces/README.md)

### Scattering theory · `knowledge/04-quantum-physics/quantum-mechanics-core/scattering-theory`

**Scope.** Scattering amplitude, differential cross section, Lippmann–Schwinger equation, Born series, partial waves and phase shifts, low-energy scattering length, Breit–Wigner resonances, Feshbach resonances, optical theorem, identical-particle scattering.

**Core ideas.**
- Far from the target $\psi\sim e^{ikz}+f(\theta)e^{ikr}/r$ and $d\sigma/d\Omega=|f|^2$.
- At low energy only s-waves matter; the scattering length $a$ summarizes the interaction (key for cold atoms).
- Unitarity ⇒ optical theorem.

**Key equations.**
$$f(\theta)=\frac1k\sum_\ell(2\ell+1)e^{i\delta_\ell}\sin\delta_\ell\,P_\ell(\cos\theta),\qquad \sigma_{\text{tot}}=\frac{4\pi}{k}\,\mathrm{Im}f(0)$$

**See also.** [Nuclear reactions](knowledge/07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering/README.md) · [Feynman diagrams](knowledge/06-particle-physics/quantum-field-theory/feynman-diagrams-and-scattering-amplitudes/README.md)

## Quantum optics · `knowledge/04-quantum-physics/quantum-optics`

#### Overview
Quantum optics treats the electromagnetic field as a set of quantized harmonic oscillators. It explains photon antibunching, two-photon interference and squeezed light, and underlies laser physics, gravitational-wave detectors operating below the shot-noise limit, and photonic and circuit-based quantum technology.

#### Conceptual spine
1. Field mode ↔ harmonic oscillator; $\hat E\propto a+a^\dagger$.
2. Glauber coherence functions classify light; $g^{(2)}(0)<1$ has no classical explanation.
3. Strong light–matter coupling ($g>\kappa,\gamma$) gives vacuum Rabi splitting and photon-by-photon control.
4. Quantum noise limits measurement; squeezing redistributes it between quadratures.

#### Key equations
$$H_{\text{JC}}=\hbar\omega_ca^\dagger a+\frac{\hbar\omega_a}{2}\sigma_z+\hbar g\left(a\sigma_++a^\dagger\sigma_-\right),\qquad g^{(2)}(0)=\frac{\langle a^{\dagger2}a^2\rangle}{\langle a^\dagger a\rangle^2}$$

#### Open problems
- Deterministic, indistinguishable, high-rate single-photon sources for photonic quantum computing.
- Quantum-limited transduction between microwave and optical photons.

#### Connections
- [Photonics and lasers](knowledge/02-electromagnetism-and-optics/photonics-and-lasers/README.md) · [Gravitational-wave detectors](knowledge/05-relativity-and-gravitation/gravitational-waves/ground-based-detections/README.md)

### Cavity and circuit QED · `knowledge/04-quantum-physics/quantum-optics/cavity-and-circuit-qed`

**Scope.** Jaynes–Cummings model, vacuum Rabi splitting, Purcell effect, dispersive regime and qubit readout, photon blockade, Rydberg atoms in microwave cavities (Haroche), transmons in coplanar resonators, ultrastrong coupling, polaritons.

**Core ideas.**
- Strong coupling: $g\gg\kappa,\gamma$ — coherent exchange of a single excitation before loss.
- Dispersive regime ($|\Delta|\gg g$): cavity frequency shifts by $\pm\chi=\pm g^2/\Delta$ depending on qubit state — quantum non-demolition readout.
- Circuit QED reaches couplings unattainable with atoms, and became the architecture of superconducting quantum computers.

**Key equations.**
$$F_P=\frac{3}{4\pi^2}\left(\frac{\lambda}{n}\right)^3\frac{Q}{V},\qquad H_{\text{disp}}=\hbar(\omega_c+\chi\sigma_z)a^\dagger a+\tfrac12\hbar\omega_a'\sigma_z$$

**See also.** [Superconducting qubits](knowledge/04-quantum-physics/quantum-information-and-computation/superconducting-qubits/README.md)

### Cavity optomechanics · `knowledge/04-quantum-physics/quantum-optics/cavity-optomechanics`

**Scope.** Optomechanical Hamiltonian, dynamical backaction, sideband cooling to the ground state, optomechanically induced transparency, standard quantum limit of position measurement, levitated nanoparticles, mechanical squeezing and entanglement, microwave–optical transduction.

**Core ideas.**
- Cavity frequency depends on mirror position: $\omega_c(x)\approx\omega_c-Gx$, giving a coupling $\hbar g_0a^\dagger a(b+b^\dagger)$.
- Red-detuned driving extracts phonons (cooling); blue-detuned driving amplifies.
- Measurement imprecision and backaction trade off, setting the SQL for continuous position sensing.

**Key equations.**
$$H=\hbar\omega_ca^\dagger a+\hbar\Omega_mb^\dagger b-\hbar g_0a^\dagger a\,(b+b^\dagger),\qquad C=\frac{4g_0^2\bar n_{\text{cav}}}{\kappa\Gamma_m}$$

**Landmark.** Aspelmeyer, Kippenberg & Marquardt (2014) — see [subfield landmarks](knowledge/04-quantum-physics/quantum-optics/README.md).

**See also.** [Harmonic and damped oscillators](knowledge/01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators/README.md)

### Quantized light and photon statistics · `knowledge/04-quantum-physics/quantum-optics/quantized-light-and-photon-statistics`

**Scope.** Mode expansion and vacuum fluctuations, Casimir effect, Fock/coherent/thermal states, Poissonian vs. sub-/super-Poissonian statistics, Hanbury Brown–Twiss experiment, $g^{(1)}$ and $g^{(2)}$, Wigner and P-functions, two-photon (HOM) interference.

**Core ideas.**
- Coherent states (laser light) have Poissonian number statistics and $g^{(2)}(0)=1$; thermal light has $g^{(2)}(0)=2$ (bunching).
- Antibunching ($g^{(2)}(0)<1$) and negative Wigner functions are signatures of non-classical light.
- HOM interference: identical photons on a 50:50 beam splitter always exit together.

**Key equations.**
$$|\alpha\rangle=e^{-|\alpha|^2/2}\sum_n\frac{\alpha^n}{\sqrt{n!}}|n\rangle,\qquad P(n)=e^{-\bar n}\frac{\bar n^n}{n!}$$

**See also.** [Coherence and statistical optics](knowledge/02-electromagnetism-and-optics/classical-optics/coherence-and-statistical-optics/README.md)

### Single-photon sources and detectors · `knowledge/04-quantum-physics/quantum-optics/single-photon-sources-and-detectors`

**Scope.** Heralded sources from SPDC and four-wave mixing, quantum-dot sources in micropillars, color centers (NV, SiV) and 2D-material emitters, metrics (brightness, purity $g^{(2)}(0)$, indistinguishability), SNSPDs, avalanche photodiodes, transition-edge sensors, photon-number resolution.

**Core ideas.**
- Probabilistic sources trade brightness against multi-photon contamination; deterministic emitters avoid this trade-off.
- Indistinguishability (HOM visibility) is essential for multi-photon interference and photonic QC.
- SNSPDs combine >95% efficiency, picosecond jitter and very low dark counts.

**Key equations.**
$$V_{\text{HOM}}=\frac{C_{\max}-C_{\min}}{C_{\max}},\qquad \eta_{\text{sys}}=\eta_{\text{coupling}}\,\eta_{\text{det}}$$

**See also.** [Photonic and spin qubits](knowledge/04-quantum-physics/quantum-information-and-computation/photonic-and-spin-qubits/README.md) · [Quantum dots](knowledge/08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures/README.md)

### Squeezed light and quantum metrology · `knowledge/04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology`

**Scope.** Quadrature operators, squeezed vacuum from parametric down-conversion, standard quantum limit (SQL), Heisenberg limit, quantum Fisher information and Cramér–Rao bound, NOON and GHZ states, spin squeezing, squeezed-light injection in LIGO/Virgo.

**Core ideas.**
- With $N$ independent probes phase uncertainty scales as $1/\sqrt N$ (SQL); entanglement allows $1/N$ (Heisenberg).
- Squeezing reduces noise in one quadrature at the cost of the other; frequency-dependent squeezing handles radiation-pressure noise.
- Loss rapidly degrades entanglement-enhanced schemes, so practical gains are modest but real.

**Key equations.**
$$\Delta X_1\Delta X_2\ge\tfrac14,\qquad \Delta\phi\ge\frac{1}{\sqrt{\nu F_Q}},\qquad F_Q\le N^2$$

**Landmark.** Caves (1981) — see [subfield landmarks](knowledge/04-quantum-physics/quantum-optics/README.md).

**See also.** [Ground-based GW detectors](knowledge/05-relativity-and-gravitation/gravitational-waves/ground-based-detections/README.md) · [Quantum sensing](knowledge/11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing/README.md)


---

# Packet 04-1 (100 records)

{"id": "C0167", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "name": "Neural quantum states and volume-law entanglement", "kind": "method transfer", "summary": "Neural networks such as restricted Boltzmann machines and transformers serve as variational wavefunctions trained by variational Monte Carlo. An MPS's entanglement is capped at ln χ, but these networks can encode volume-law entanglement with polynomially many parameters (Deng, Li & Das Sarma 2017).", "map": "\\psi_\\theta(s)=\\sum_{h}\\exp\\Big(\\sum_ia_is_i+\\sum_jb_jh_j+\\sum_{ij}W_{ij}s_ih_j\\Big)", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0168", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "04-quantum-physics/quantum-mechanics-core/approximation-methods", "name": "Born–Oppenheimer surfaces drive ab initio MD", "kind": "mechanism", "summary": "The Born–Oppenheimer approximation separates electrons from nuclei, with small parameter (m_e/M)^{1/4}. Ab initio and Car–Parrinello MD move classical nuclei on the electronic ground-state energy surface. The approximation fails at conical intersections, where nonadiabatic methods such as surface hopping take over.", "map": "M_I\\ddot{\\mathbf R}_I=-\\nabla_IE_0(\\{\\mathbf R\\}),\\ \\kappa=(m_e/M)^{1/4}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0169", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity", "name": "Amplitude estimation speeds up Monte Carlo quadratically", "kind": "method transfer", "summary": "Amplitude amplification estimates an expectation value to error ε with O(1/ε) oracle calls, against O(1/ε²) samples classically (Montanaro 2015). It is the same 1/√N to 1/N jump as from the standard quantum limit to the Heisenberg limit.", "map": "\\epsilon_{\\rm MC}\\propto N^{-1/2}\\ \\to\\ \\epsilon_{\\rm QAE}\\propto N^{-1}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0170", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "name": "Path-integral quantum Monte Carlo and the sign problem", "kind": "identity", "summary": "Slicing imaginary time turns the quantum partition function into a classical ensemble of ring polymers that Metropolis sampling can handle. This is exact for bosons, but fermion exchange produces negative weights. That is the sign problem, which is NP-hard in general (Troyer–Wiese 2005).", "map": "Z=\\mathrm{Tr}\\,e^{-\\beta H}=\\oint\\mathcal Dx\\,e^{-S_E[x]/\\hbar},\\ x(\\beta\\hbar)=x(0)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0171", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity", "name": "Trotter splitting: symplectic integrators and quantum gates", "kind": "identity", "summary": "Leapfrog and Strang symplectic integrators and split-step Schrödinger solvers use the same operator splitting that compiles e^{-iHt} into gates on a quantum computer. Higher-order Suzuki formulas and their commutator error bounds carry over directly.", "map": "e^{-i(A+B)t}=\\left(e^{-iAt/2n}e^{-iBt/n}e^{-iAt/2n}\\right)^n+O(t^3/n^2)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0172", "a": "00-foundations/computational-physics/tensor-network-methods", "b": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "name": "Area-law entanglement makes MPS and DMRG efficient", "kind": "identity", "summary": "The Schmidt rank across any cut of a matrix product state is at most the bond dimension, so the entanglement entropy obeys S ≤ ln χ. Ground states of gapped 1D Hamiltonians obey an area law (Hastings 2007), so they compress efficiently, and entanglement growth sets the cost of time evolution.", "map": "S_A=-\\mathrm{Tr}\\,\\rho_A\\ln\\rho_A\\le\\ln\\chi", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0173", "a": "00-foundations/computational-physics/tensor-network-methods", "b": "04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity", "name": "Tensor-network contraction vs quantum-advantage claims", "kind": "method transfer", "summary": "After the random-circuit-sampling advantage claims (Arute et al. 2019), tensor-network contraction simulated the same circuits classically far faster than first estimated. The treewidth of a circuit's tensor network sets the classical cost, so tensor networks mark the moving boundary of quantum advantage.", "map": "\\text{exact contraction cost}\\sim2^{O(\\mathrm{tw}(G))}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0174", "a": "00-foundations/history-and-philosophy-of-physics", "b": "04-quantum-physics/foundations-of-quantum-mechanics", "name": "Bohr–Einstein debates and the EPR argument", "kind": "historical", "summary": "The 1927–35 Bohr–Einstein debates and the EPR argument treated completeness and locality as philosophical questions. Bell (1964) turned them into testable inequalities, which is why foundations of QM is where history and philosophy meet the laboratory.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0175", "a": "00-foundations/history-and-philosophy-of-physics/history-of-physics", "b": "04-quantum-physics", "name": "The quantum revolution, 1900–1927", "kind": "historical", "summary": "Blackbody radiation (Planck 1900), the photoelectric effect (Einstein 1905) and atomic spectra with the Bohr model (1913) led to matrix and wave mechanics (1925–26). Spectroscopy drove the experiments, and the episode is the standard case study of theory change.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0176", "a": "00-foundations/history-and-philosophy-of-physics/philosophy-of-physics", "b": "04-quantum-physics/foundations-of-quantum-mechanics", "name": "No-go theorems as experimental metaphysics", "kind": "shared object", "summary": "The Bell, Kochen–Specker and PBR theorems turn questions about hidden variables, locality and the reality of the wavefunction into constraints that experiments can test. Philosophy of physics now argues over which premise to give up, such as measurement independence or outcome independence.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0177", "a": "00-foundations/history-and-philosophy-of-physics/philosophy-of-physics", "b": "04-quantum-physics/foundations-of-quantum-mechanics/measurement-problem-and-interpretations", "name": "Measurement problem and rival interpretations", "kind": "shared object", "summary": "Unitary evolution and definite measurement outcomes conflict. Copenhagen, Everett's relative states, Bohmian mechanics, GRW collapse and QBism resolve this in different ways, and the meaning of Born-rule probability in many worlds is debated in both fields.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0178", "a": "00-foundations/history-and-philosophy-of-physics/philosophy-of-physics", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth", "name": "Typicality and ETH as foundations of statistical mechanics", "kind": "mechanism", "summary": "Philosophy of statistical mechanics asks why equilibrium ensembles work. Canonical typicality (almost every pure state of system plus bath has a thermal reduced state) and ETH (every energy eigenstate looks thermal) answer this for isolated quantum systems without ensembles or the ergodic hypothesis.", "map": "\\langle E_m|O|E_n\\rangle=O(\\bar E)\\delta_{mn}+e^{-S(\\bar E)/2}f_O(\\bar E,\\omega)R_{mn}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0179", "a": "00-foundations/mathematical-methods", "b": "04-quantum-physics/quantum-mechanics-core", "name": "Eigenproblems and special functions of quantum mechanics", "kind": "method transfer", "summary": "Separation of variables, Sturm–Liouville eigenproblems and orthogonal polynomials (Hermite, Laguerre, Legendre) give the textbook spectra. Green's functions, contour integrals and asymptotic methods underpin perturbation theory, scattering and WKB.", "map": "-\\frac{\\hbar^2}{2m}\\psi''+V\\psi=E\\psi\\ \\leftrightarrow\\ (py')'+qy=-\\lambda wy", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0180", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "name": "Saddle points, Stokes lines and instantons", "kind": "identity", "summary": "Semiclassics evaluates the path integral by stationary phase or steepest descent. Airy functions join WKB solutions at turning points, Stokes phenomena control tunnelling exponents, and Wick rotation turns tunnelling into Euclidean instanton saddles.", "map": "\\int\\mathcal Dx\\,e^{iS/\\hbar}\\approx\\sum_{\\rm cl}A_{\\rm cl}\\,e^{iS_{\\rm cl}/\\hbar},\\ t\\to-i\\tau,\\ \\Gamma\\propto e^{-S_E^{\\rm inst}/\\hbar}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0181", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "name": "Analytic S-matrix: poles, resonances, dispersion", "kind": "identity", "summary": "Causality makes partial-wave S-matrices analytic in complex momentum. Bound states are poles on the positive imaginary k axis and resonances are poles below the real axis that give Breit–Wigner peaks. The optical theorem and dispersion relations tie forward amplitudes to total cross sections.", "map": "S_\\ell(k)=e^{2i\\delta_\\ell(k)},\\ \\sigma_{\\rm tot}=\\frac{4\\pi}{k}\\mathrm{Im}f(0),\\ E_{\\rm res}=E_r-i\\Gamma/2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0182", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "name": "Lippmann–Schwinger equation and the Born series", "kind": "identity", "summary": "The outgoing Helmholtz Green's function turns the Schrödinger equation into an integral equation. Iterating it gives the Born series, and its far-field limit gives the scattering amplitude f(θ).", "map": "\\psi=\\phi+G_0^{(+)}V\\psi,\\ G_0^{(+)}(\\mathbf r,\\mathbf r')=-\\frac{m}{2\\pi\\hbar^2}\\frac{e^{ik|\\mathbf r-\\mathbf r'|}}{|\\mathbf r-\\mathbf r'|}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0183", "a": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "b": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "name": "Schmidt decomposition is the singular value decomposition", "kind": "identity", "summary": "Arrange a bipartite pure state's amplitudes as a matrix and its SVD is the Schmidt form. The squared singular values are the eigenvalues of the reduced state, so entanglement entropy and Schmidt rank are matrix invariants. The same SVD truncation drives DMRG.", "map": "\\psi_{ij}=\\sum_kU_{ik}\\sqrt{\\lambda_k}V^*_{jk},\\ |\\psi\\rangle=\\sum_k\\sqrt{\\lambda_k}|u_k\\rangle|v_k\\rangle,\\ S=-\\sum_k\\lambda_k\\ln\\lambda_k", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0184", "a": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "b": "04-quantum-physics/quantum-mechanics-core", "name": "Dirac notation and operator algebra", "kind": "identity", "summary": "The working tools of QM are linear-algebra results: commutators and simultaneous diagonalisation, unitary changes of basis, ladder-operator algebras, and rigged Hilbert spaces for the continuous spectra of position and momentum.", "map": "[x,p]=i\\hbar,\\ a=\\tfrac{1}{\\sqrt2}(x/\\ell+i\\ell p/\\hbar),\\ [a,a^\\dagger]=1", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0185", "a": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "b": "04-quantum-physics/quantum-mechanics-core/postulates-and-formalism", "name": "Spectral theorem as the measurement postulate", "kind": "identity", "summary": "States are rays in a Hilbert space and observables are self-adjoint operators. The spectral theorem supplies the possible outcomes (eigenvalues) and projectors that give the Born rule and state update. Gleason's theorem shows this is the only consistent probability measure for dimension ≥ 3.", "map": "A=\\sum_k a_kP_k,\\ p_k=\\langle\\psi|P_k|\\psi\\rangle,\\ |\\psi\\rangle\\to P_k|\\psi\\rangle/\\sqrt{p_k}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0186", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "name": "Berry phase as holonomy of a U(1) connection", "kind": "identity", "summary": "The Berry connection is a connection on the line bundle of eigenstates over parameter space. Its curvature 2-form integrates to the Berry phase, and over closed surfaces to integer Chern numbers (Simon 1983). The quantum geometric tensor combines the Fubini–Study metric with the Berry curvature.", "map": "A=i\\langle n|dn\\rangle,\\ F=dA,\\ \\gamma_C=\\oint_CA=\\int_SF,\\ Q_{\\mu\\nu}=g_{\\mu\\nu}-\\tfrac i2F_{\\mu\\nu}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0187", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "04-quantum-physics/quantum-information-and-computation/superconducting-qubits", "name": "Quantum-limited amplifiers for qubit readout", "kind": "mechanism", "summary": "Dispersive readout of superconducting qubits needs Josephson parametric or travelling-wave amplifiers that work near the Caves bound: a phase-insensitive amplifier must add at least half a quantum of noise. The same SQUID and Josephson technology reads out cryogenic detectors.", "map": "\\mathcal A\\ge\\tfrac12\\left|1-G^{-1}\\right|\\ \\text{quanta (phase-insensitive)}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0188", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "04-quantum-physics/quantum-optics/single-photon-sources-and-detectors", "name": "Cryogenic sensors as single-photon detectors", "kind": "shared object", "summary": "Cryogenic sensors and the noise analysis of instrumentation have become quantum-optics hardware. Transition-edge sensors resolve photon number with about 95% efficiency, and superconducting nanowire detectors reach about 98% efficiency with few-picosecond jitter. Dark counts and dead time are the other figures of merit.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0189", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology", "name": "Quantum Fisher information and the Cramér–Rao bound", "kind": "identity", "summary": "Optimising the classical Cramér–Rao bound over all quantum measurements gives the quantum Fisher information (Braunstein–Caves 1994). N independent probes give F_Q = N, the standard quantum limit; entangled probes reach up to N², the Heisenberg limit.", "map": "\\Delta\\theta\\ge\\frac{1}{\\sqrt{\\nu F_Q}},\\ F_Q=4\\left(\\langle\\partial_\\theta\\psi|\\partial_\\theta\\psi\\rangle-|\\langle\\psi|\\partial_\\theta\\psi\\rangle|^2\\right)\\le N^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0190", "a": "00-foundations/measurement-and-data-analysis/uncertainty-and-error-propagation", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "name": "Clock uncertainty budgets and Allan deviation", "kind": "method transfer", "summary": "Clock accuracy is quoted as a GUM-style budget of Type B systematic shifts (blackbody, Zeeman, Stark, motional) added in quadrature. Stability is quoted as the Allan deviation, which quantum projection noise ultimately limits. This is how the Al+/Hg+ ratio reached the 17th decimal place.", "map": "\\sigma_y^2(\\tau)=\\tfrac12\\langle(\\bar y_{k+1}-\\bar y_k)^2\\rangle,\\ \\sigma_y^{\\rm QPN}\\approx\\frac{1}{2\\pi\\nu_0T}\\sqrt{\\frac{T_c}{N\\tau}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0191", "a": "00-foundations/symmetry-and-group-theory", "b": "04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin", "name": "Rotation symmetry labels states and selection rules", "kind": "mechanism", "summary": "Rotational invariance of H makes j and m good quantum numbers. The Wigner–Eckart theorem splits every tensor-operator matrix element into a Clebsch–Gordan coefficient times a reduced element, which gives the dipole selection rules.", "map": "\\langle j'm'|T^{(k)}_q|jm\\rangle=\\langle jm;kq|j'm'\\rangle\\langle j'\\|T^{(k)}\\|j\\rangle/\\sqrt{2j'+1}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0192", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "name": "Atomic parity violation and electron EDM searches", "kind": "shared object", "summary": "Z-boson exchange mixes S and P states, so the forbidden Cs 6S–7S transition gains a parity-odd amplitude that measures the weak charge Q_W (Wood et al. 1997). Electron-EDM searches in heavy atoms and polar molecules test T, and hence CP, violation; the best bound is |d_e| < 4.1×10^{-30} e·cm (JILA HfF+, 2023).", "map": "H_{\\rm PV}=\\frac{G_F}{2\\sqrt2}Q_W\\gamma_5\\rho_N(r),\\ H_{\\rm EDM}=-d_e\\,\\boldsymbol\\sigma\\cdot\\mathbf E_{\\rm eff}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0193", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/non-hermitian-physics", "name": "PT symmetry and exceptional points", "kind": "mechanism", "summary": "A non-Hermitian Hamiltonian that commutes with the antiunitary PT operator has a real spectrum while the symmetry is unbroken. At the breaking threshold, eigenvalues and eigenvectors coalesce at an exceptional point: H becomes a non-diagonalisable Jordan block, the eigenvalues meet at a square-root branch point, and the splitting grows as √ε.", "map": "[H,\\mathcal{PT}]=0,\\ H_{\\rm EP}=\\begin{pmatrix}0&1\\\\0&0\\end{pmatrix},\\ \\Delta E\\propto\\sqrt{\\epsilon}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0194", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling", "name": "Dyson's threefold way fixes chaotic level statistics", "kind": "mechanism", "summary": "Spectra of chaotic systems follow random-matrix statistics (Bohigas–Giannoni–Schmit 1984). Antiunitary symmetry picks the ensemble: GOE if T² = +1, GUE if T is broken, GSE if T² = −1. The level-repulsion exponent β is the diagnostic.", "map": "P(s)\\propto s^{\\beta}e^{-c_\\beta s^2}:\\ \\beta=1\\ (T^2=+1),\\ 2\\ (\\text{no }T),\\ 4\\ (T^2=-1)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0195", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin", "name": "Kramers degeneracy from T² = −1 for half-integer spin", "kind": "mechanism", "summary": "Time reversal is antiunitary and acts on spin as Θ = e^{-iπS_y/ħ}K, so Θ² = (−1)^{2S}. With an odd number of electrons, every level is at least doubly degenerate unless a magnetic field breaks T. This is the origin of the protected Kramers pairs in topological insulators.", "map": "\\Theta=e^{-i\\pi S_y/\\hbar}K,\\ \\Theta^2=(-1)^{2S}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0196", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin", "name": "Spin is a projective representation of SO(3)", "kind": "identity", "summary": "Angular-momentum operators obey the su(2) algebra, whose irreducible representations give j = 0, 1/2, 1, …. Half-integer spin exists because SU(2) double-covers SO(3): a 2π rotation multiplies a spinor by −1, as seen in neutron interferometry.", "map": "[J_i,J_j]=i\\hbar\\epsilon_{ijk}J_k,\\ J^2=\\hbar^2j(j+1),\\ e^{-2\\pi iJ_z/\\hbar}=(-1)^{2j}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0197", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems", "name": "Hidden SO(4) symmetry of the hydrogen atom", "kind": "identity", "summary": "On bound states, the angular momentum L and the scaled Runge–Lenz vector K generate so(4) ≅ su(2)⊕su(2). Pauli (1926) used this to obtain the Bohr levels algebraically, and it explains the n² degeneracy across ℓ. SU(3) plays the same role for the 3D isotropic oscillator.", "map": "\\mathfrak{so}(4)\\cong\\mathfrak{su}(2)\\oplus\\mathfrak{su}(2):\\ \\mathbf J_\\pm=\\tfrac12(\\mathbf L\\pm\\mathbf K),\\ j_\\pm=\\tfrac{n-1}{2},\\ \\deg=n^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0198", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "04-quantum-physics/quantum-mechanics-core/postulates-and-formalism", "name": "Quantum Noether: conserved generators commute with H", "kind": "identity", "summary": "By Wigner's theorem, symmetries act as unitary or antiunitary operators. If a continuous symmetry e^{-iθG/ħ} leaves H invariant, then [G,H] = 0 and the distribution of G is conserved. This is the operator form of Noether's theorem: momentum from translations, J from rotations, charge from U(1).", "map": "U^\\dagger HU=H\\Rightarrow[G,H]=0\\Rightarrow\\frac{d}{dt}\\langle G\\rangle=\\frac{i}{\\hbar}\\langle[H,G]\\rangle=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0199", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "name": "BEC breaks U(1); Bogoliubov phonon is the Goldstone mode", "kind": "identity", "summary": "The condensate order parameter ψ = √n e^{iθ} breaks the global phase symmetry that goes with atom-number conservation. The gapless Bogoliubov sound mode is the Goldstone boson, and its sound speed sets the Landau critical velocity for superfluid flow.", "map": "\\hbar\\omega_k=\\sqrt{\\epsilon_k(\\epsilon_k+2gn)},\\ c=\\sqrt{gn/m},\\ g=4\\pi\\hbar^2a/m", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0200", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/floquet-systems-and-time-crystals", "name": "Time crystals break time-translation symmetry", "kind": "mechanism", "summary": "Wilczek's (2012) equilibrium time crystal is ruled out by the Watanabe–Oshikawa no-go theorem. Instead, periodically driven many-body systems, which conserve quasienergy rather than energy, break the discrete Floquet time-translation symmetry and respond at period 2T. Many-body localization or prethermalization protects this order, which has been seen with trapped ions, NV centres and superconducting qubits.", "map": "\\langle O(t+T)\\rangle\\ne\\langle O(t)\\rangle=\\langle O(t+2T)\\rangle,\\ \\varepsilon\\ \\mathrm{mod}\\ \\hbar\\omega", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0201", "a": "00-foundations/units-and-constants", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "name": "The SI second is a caesium hyperfine frequency", "kind": "shared object", "summary": "Since 1967 the second has been defined by fixing the Cs ground-state hyperfine frequency. Time and frequency are the most precisely realised SI quantities, and the metre is traced to them through the fixed value of c.", "map": "\\Delta\\nu_{\\rm Cs}=9\\,192\\,631\\,770\\ \\mathrm{Hz}\\ (\\text{exact})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0202", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "name": "Unitary Fermi gas: universality from a missing scale", "kind": "mechanism", "summary": "At a Feshbach resonance the scattering length diverges and drops out, leaving density as the only scale. Dimensional analysis then forces every observable to be a universal number times its free-Fermi-gas value, the Bertsch parameter ξ being one example. Dilute neutron matter shares the same universality.", "map": "a\\to\\infty:\\ \\frac EN=\\xi\\,\\frac35E_F,\\ \\xi\\approx0.37,\\ T_c\\approx0.17\\,T_F", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0203", "a": "00-foundations/units-and-constants/fundamental-constants", "b": "04-quantum-physics/atomic-molecular-and-optical-physics", "name": "AMO measurements determine α and m_e for CODATA", "kind": "shared object", "summary": "The fine-structure constant comes from atom-recoil interferometry (h/m for Cs and Rb) and from the Penning-trap electron g-factor combined with QED. These AMO inputs dominate the CODATA values of α, R∞ and m_e, and the ~5σ gap between the Cs and Rb values remains unresolved.", "map": "\\alpha^2=\\frac{2R_\\infty}{c}\\frac{A_r(X)}{A_r(e)}\\frac{h}{m_X}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0204", "a": "00-foundations/units-and-constants/fundamental-constants", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "name": "Clock ratios test the constancy of α and m_p/m_e", "kind": "method transfer", "summary": "Different transitions depend on α and μ = m_p/m_e with different sensitivities, so repeated ratios between clocks (Al+/Hg+, Yb+ E3/E2, Cs/Sr) bound present-day drifts at the ~10^{-18} per year level. The same ratios search for ultralight dark matter, which would make the constants oscillate.", "map": "\\frac{d}{dt}\\ln\\frac{\\nu_1}{\\nu_2}=(K_1-K_2)\\frac{\\dot\\alpha}{\\alpha},\\ K_{\\rm Hg^+}\\approx-2.9,\\ K_{\\rm Al^+}\\approx0", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0205", "a": "00-foundations/units-and-constants/fundamental-constants", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "name": "Hydrogen spectroscopy, R∞ and the proton radius", "kind": "shared object", "summary": "The Rydberg constant and the proton charge radius are fitted together to hydrogen and deuterium transition frequencies. The muonic-hydrogen Lamb shift (2010) gave a radius 4% smaller. The puzzle eased once newer hydrogen measurements and CODATA 2018/2022 moved to about 0.84 fm.", "map": "\\Delta E_{nS}^{\\rm size}=\\frac{2(Z\\alpha)^4}{3n^3}\\frac{m_r^3c^4}{\\hbar^2}r_p^2,\\ r_p\\approx0.841\\ \\mathrm{fm}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0206", "a": "00-foundations/units-and-constants/si-units-and-2019-redefinition", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "name": "Optical clocks and redefining the second", "kind": "shared object", "summary": "Optical lattice and ion clocks now beat the Cs primary standard by about 100×. The CIPM roadmap therefore plans an optical redefinition of the second around 2030, continuing the 2019 move to defining units by fixed constants.", "map": "\\delta\\nu/\\nu\\sim10^{-18}\\ (\\text{optical})\\ \\text{vs}\\ 10^{-16}\\ (\\text{Cs fountain})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0580", "a": "01-classical-mechanics/analytical-mechanics", "b": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "name": "Lagrangian generates quantum propagation (Dirac–Feynman)", "kind": "historical", "summary": "Dirac (1933) noticed that the short-time quantum propagator behaves like exp(iS/ħ), with S the classical action. Feynman built the path integral on this, which made the Lagrangian rather than the Hamiltonian the primary object of quantum dynamics.", "map": "K(x_b,t_b;x_a,t_a)=\\int\\mathcal{D}x\\,e^{iS[x]/\\hbar},\\quad S=\\int L(x,\\dot x)\\,dt", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0581", "a": "01-classical-mechanics/analytical-mechanics/canonical-transformations-and-hamilton-jacobi", "b": "04-quantum-physics/foundations-of-quantum-mechanics/measurement-problem-and-interpretations", "name": "Bohmian mechanics as quantum Hamilton–Jacobi theory", "kind": "identity", "summary": "With ψ=R e^{iS/ħ}, the Schrödinger equation is exactly a Hamilton–Jacobi equation plus Bohm's quantum potential Q (Madelung 1927, Bohm 1952). De Broglie–Bohm theory has particles move along v=∇S/m, the characteristics of this equation, which gives a deterministic hidden-variable interpretation.", "map": "\\partial_tS+\\frac{(\\nabla S)^2}{2m}+V+Q=0,\\ \\ Q=-\\frac{\\hbar^2}{2m}\\frac{\\nabla^2R}{R},\\ \\ \\dot{\\mathbf x}=\\frac{\\nabla S}{m}", "breaks": "For many particles Q is nonlocal in configuration space and does not weaken as |ψ| shrinks. The motion is first-order, so initial momenta are not free. The mathematics is exact, but the interpretation is contested.", "confidence": "established", "strength": 2}
{"id": "C0582", "a": "01-classical-mechanics/analytical-mechanics/canonical-transformations-and-hamilton-jacobi", "b": "04-quantum-physics/quantum-mechanics-core/approximation-methods", "name": "WKB: Schrödinger reduces to Hamilton–Jacobi", "kind": "identity", "summary": "Writing ψ=A e^{iS/ħ} turns the Schrödinger equation into the Hamilton–Jacobi equation at leading order, plus a continuity equation for A. Quantizing the action variables J=∮p dq gives the Bohr–Sommerfeld and EBK rules. Ehrenfest argued that action variables were the right quantities to quantize because they are adiabatic invariants.", "map": "\\psi=Ae^{iS/\\hbar}:\\ \\partial_tS+\\frac{(\\nabla S)^2}{2m}+V=\\frac{\\hbar^2}{2m}\\frac{\\nabla^2A}{A};\\ \\ J=\\oint p\\,dq=2\\pi\\hbar(n+\\tfrac12)", "breaks": "It breaks down at turning points and caustics, where A diverges (Airy matching and the Maslov 1/2 repair this), and wherever the de Broglie wavelength changes quickly.", "confidence": "established", "strength": 3}
{"id": "C0583", "a": "01-classical-mechanics/analytical-mechanics/canonical-transformations-and-hamilton-jacobi", "b": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "name": "Hannay angle: classical counterpart of the Berry phase", "kind": "identity", "summary": "When an integrable system's parameters are cycled adiabatically, the action J stays invariant but the conjugate angle picks up a geometric shift, the Hannay angle. Berry showed that it is the semiclassical limit of the Berry phase of the quantum state with the same quantum number.", "map": "\\Delta\\theta_H=-\\frac{\\partial\\gamma_n}{\\partial n}\\Big|_{J=(n+\\frac12)\\hbar},\\quad \\gamma_n=i\\oint\\langle n|\\nabla_{\\mathbf R}n\\rangle\\cdot d\\mathbf R", "breaks": "It requires invariant tori. Chaotic systems have no angle variables, and their adiabatic response takes a different form (geometric magnetism, Berry–Robbins).", "confidence": "established", "strength": 3}
{"id": "C0584", "a": "01-classical-mechanics/analytical-mechanics/canonical-transformations-and-hamilton-jacobi", "b": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "name": "Hamilton's principal function as the semiclassical phase", "kind": "identity", "summary": "In the stationary-phase evaluation of the path integral, the phase is Hamilton's principal function S(x_b,x_a,t), which generates the classical time-evolution map. The prefactor is its mixed second derivative (the Van Vleck–Gutzwiller propagator), and caustics of the classical family add Maslov phases.", "map": "K_{sc}=\\sum_{cl}\\Big|\\det\\frac{-\\partial^2S}{\\partial x_a\\partial x_b}\\Big|^{1/2}\\frac{e^{iS_{cl}/\\hbar-i\\mu\\pi/2}}{(2\\pi i\\hbar)^{d/2}}", "breaks": "It fails near caustics and beyond the Ehrenfest time, where classical paths proliferate (chaos). It also fails where no real classical path exists: tunnelling needs complex or Euclidean paths.", "confidence": "established", "strength": 3}
{"id": "C0585", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "04-quantum-physics/foundations-of-quantum-mechanics/contextuality", "name": "Epistemically restricted Liouville mechanics ≈ Gaussian QM", "kind": "analogy", "summary": "Classical Liouville mechanics with an uncertainty-like limit on what can be known about phase-space points reproduces Gaussian quantum mechanics, including entanglement and teleportation (Bartlett, Rudolph and Spekkens). The genuinely nonclassical resource therefore lies outside it: contextuality, which is equivalent to negativity of the Wigner function.", "map": "\\text{Liouville}+\\text{epistemic restriction}\\ \\cong\\ \\text{Gaussian QM};\\ \\ \\text{contextuality}\\Leftrightarrow W<0", "breaks": "The model cannot reproduce non-Gaussian states or operations, Bell violations or Kochen–Specker contextuality, because it is a noncontextual hidden-variable model by construction.", "confidence": "current research", "strength": 2}
{"id": "C0586", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "04-quantum-physics/quantum-mechanics-core/postulates-and-formalism", "name": "Poisson bracket → commutator (canonical quantization)", "kind": "identity", "summary": "Dirac recognized that Heisenberg's commutators obey the algebra of classical Poisson brackets, so quantization replaces {A,B} with [Â,B̂]/iħ. Hamilton's equations then become the Heisenberg equations of motion, and the Liouville equation becomes the von Neumann equation for the density matrix.", "map": "\\{A,B\\}\\to\\tfrac{1}{i\\hbar}[\\hat A,\\hat B];\\ \\dot A=\\{A,H\\}\\to\\dot{\\hat A}=\\tfrac{i}{\\hbar}[\\hat H,\\hat A];\\ \\partial_t\\rho=\\{H,\\rho\\}\\to i\\hbar\\partial_t\\hat\\rho=[\\hat H,\\hat\\rho]", "breaks": "The map is not exact for all observables. The Groenewold–van Hove theorem rules out a consistent quantization of all polynomials, so operator ordering is ambiguous at O(ħ²).", "confidence": "established", "strength": 3}
{"id": "C0587", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "04-quantum-physics/quantum-optics/quantized-light-and-photon-statistics", "name": "Phase-space QM: Liouville flow to Wigner–Moyal", "kind": "identity", "summary": "The Wigner function is a quasi-probability on classical phase space that evolves by the Liouville equation with the Poisson bracket replaced by the Moyal bracket. Quantum optics describes light with Wigner, Husimi-Q and Glauber–Sudarshan-P distributions; Wigner negativity or a singular P function marks a nonclassical state.", "map": "\\partial_tW=\\{H,W\\}_{\\star}=\\{H,W\\}+O(\\hbar^2\\,\\partial^3H\\,\\partial^3W);\\ \\ W\\ \\text{follows the classical flow exactly if}\\ H\\ \\text{is quadratic}", "breaks": "W can be negative, so it is not a probability. Moyal corrections at O(ħ²) appear for anharmonic Hamiltonians, so classical Liouville flow is exact only for quadratic H (linear optics).", "confidence": "established", "strength": 3}
{"id": "C0588", "a": "01-classical-mechanics/analytical-mechanics/lagrangian-mechanics", "b": "04-quantum-physics/quantum-information-and-computation/superconducting-qubits", "name": "Circuit quantization from the node-flux Lagrangian", "kind": "method transfer", "summary": "Superconducting circuits are quantized by writing a Lagrangian in node fluxes, with capacitive energy as kinetic energy and inductive and Josephson energy as potential energy. A Legendre transform makes the charges the conjugate momenta, and one then imposes [Φ,Q]=iħ. Kirchhoff loops and flux quantization act as holonomic constraints.", "map": "L=\\tfrac12C\\dot\\Phi^2+E_J\\cos\\Big(\\frac{2\\pi\\Phi}{\\Phi_0}\\Big)-\\frac{\\Phi^2}{2L_\\ell},\\ \\ Q=\\frac{\\partial L}{\\partial\\dot\\Phi},\\ \\ [\\hat\\Phi,\\hat Q]=i\\hbar", "breaks": "Dissipative and non-Lagrangian elements (resistors, nonreciprocal gyrators) need a bath or an extended treatment. Offset charges and compact phase variables need care.", "confidence": "established", "strength": 3}
{"id": "C0589", "a": "01-classical-mechanics/analytical-mechanics/variational-principles", "b": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "name": "Least action as stationary phase", "kind": "identity", "summary": "As ħ→0, Hamilton's principle δS=0 is the stationary-phase condition of the sum over e^{iS/ħ}: only paths near the classical one interfere constructively, just as Fermat's principle emerges from Huygens' wave optics. In imaginary time the same logic picks out minima of the Euclidean action (instantons).", "map": "\\hbar\\to0:\\ \\int\\mathcal{D}x\\,e^{iS/\\hbar}\\ \\text{dominated by}\\ \\delta S=0\\ \\Leftrightarrow\\ \\frac{d}{dt}\\frac{\\partial L}{\\partial\\dot x}=\\frac{\\partial L}{\\partial x}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0590", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "name": "Madelung: condensates as inviscid, irrotational fluids", "kind": "identity", "summary": "With ψ=√n e^{iθ}, the Gross–Pitaevskii equation becomes the continuity and Euler equations of an inviscid, irrotational fluid with velocity v=ħ∇θ/m, plus a quantum-pressure term. Kelvin's circulation theorem becomes the topological quantization of circulation around vortex lines, and the Landau criterion sets the critical velocity for dissipation.", "map": "\\mathbf v=\\tfrac{\\hbar}{m}\\nabla\\theta;\\ \\ m\\partial_t\\mathbf v=-\\nabla\\big(\\tfrac12mv^2+V+gn+Q\\big);\\ \\ \\oint\\mathbf v\\cdot d\\mathbf l=\\tfrac{h}{m}\\ell,\\ \\ell\\in\\mathbb Z", "breaks": "The fluid picture fails inside vortex cores and below the healing length ξ, where quantum pressure dominates. At finite temperature a normal component adds viscosity (the two-fluid model).", "confidence": "established", "strength": 3}
{"id": "C0591", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics", "b": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "name": "Low-Re swimming as a gauge holonomy (Shapere–Wilczek)", "kind": "identity", "summary": "At low Reynolds number, a swimmer's net displacement after a cyclic stroke depends only on the loop traced in shape space: it is the holonomy of a gauge connection, as with the Berry phase. For small strokes the displacement is the curvature times the enclosed area, so reciprocal strokes, which enclose no area, cannot swim (Purcell's scallop theorem).", "map": "\\Delta\\mathbf x=\\oint_{\\rm stroke}\\mathcal A(s)\\,ds\\approx\\iint\\mathcal F\\,da,\\ \\ \\mathcal F=d\\mathcal A+\\mathcal A\\wedge\\mathcal A;\\ \\ \\text{reciprocal stroke}\\Rightarrow\\Delta\\mathbf x=0", "breaks": "The connection is non-abelian (it mixes rotations and translations) and comes from the reciprocity of Stokes flow, not from a quantum state. The effect is purely kinematic and dissipative.", "confidence": "established", "strength": 2}
{"id": "C0592", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "name": "Quantum turbulence: Kolmogorov cascades in vortex tangles", "kind": "mechanism", "summary": "Tangles of quantized vortices in superfluid helium and atomic condensates reproduce Kolmogorov's k^{-5/3} spectrum at scales larger than the intervortex spacing. Below that scale, energy moves through vortex reconnections and Kelvin-wave cascades. 2D condensates show inverse cascades and Onsager's negative-temperature vortex clusters.", "map": "E(k)=C\\,\\varepsilon^{2/3}k^{-5/3}\\ \\ (k\\ll\\ell^{-1}),\\qquad \\kappa=h/m", "breaks": "There is no viscosity: energy is dissipated by phonon emission and reconnections at the smallest scales. Quantized circulation also imposes a discrete vortex scale that classical turbulence lacks.", "confidence": "current research", "strength": 2}
{"id": "C0593", "a": "01-classical-mechanics/newtonian-mechanics/central-forces-and-orbits", "b": "04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems", "name": "Kepler–hydrogen: Runge–Lenz vector and hidden SO(4)", "kind": "identity", "summary": "The conserved Laplace–Runge–Lenz vector, which keeps Kepler orbits closed (Bertrand's theorem), enlarges the symmetry of the 1/r problem from SO(3) to SO(4). Pauli (1926) used its quantum version to derive the hydrogen spectrum algebraically, and the same symmetry explains hydrogen's accidental n² degeneracy.", "map": "\\mathbf A=\\mathbf p\\times\\mathbf L-mk\\,\\hat{\\mathbf r};\\ \\ \\mathfrak{so}(4):\\ E_n=-\\frac{mk^2}{2\\hbar^2n^2},\\ g_n=n^2\\ \\ (k=Ze^2/4\\pi\\varepsilon_0)", "breaks": "Any departure from 1/r (relativity, core penetration, spin–orbit coupling) breaks SO(4). Classically the orbits then precess; quantum mechanically the ℓ-levels split.", "confidence": "established", "strength": 3}
{"id": "C0594", "a": "01-classical-mechanics/newtonian-mechanics/central-forces-and-orbits", "b": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "name": "Rutherford scattering: classical = quantum for 1/r", "kind": "identity", "summary": "The Coulomb differential cross section comes out the same from classical orbits, from the first Born approximation and from the exact quantum solution. This accident of the 1/r potential is why Rutherford's classical analysis could reveal the nucleus. For other potentials, features of the classical deflection function (rainbows, glories, orbiting) reappear as stationary-phase points of the partial-wave sum (Ford–Wheeler).", "map": "\\frac{d\\sigma}{d\\Omega}=\\Big(\\frac{Z_1Z_2e^2}{16\\pi\\varepsilon_0E}\\Big)^2\\frac{1}{\\sin^4(\\theta/2)}", "breaks": "In general the classical and quantum cross sections differ. Diffraction and shadow scattering make the quantum total cross section of a hard sphere twice its geometric value at high energy, and identical-particle (Mott) interference has no classical analogue.", "confidence": "established", "strength": 3}
{"id": "C0595", "a": "01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics", "b": "04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity", "name": "Symplectic splitting ↔ Trotter–Suzuki Hamiltonian simulation", "kind": "method transfer", "summary": "Long-term N-body integration splits H into exactly solvable flows (leapfrog, Wisdom–Holman, Yoshida–Suzuki compositions). Digital quantum simulation uses the same product formulas for e^{-iHt}. The error is set by nested Poisson brackets in the classical case and nested commutators in the quantum case.", "map": "e^{\\tau(A+B)}=e^{\\tau A/2}e^{\\tau B}e^{\\tau A/2}+O(\\tau^3[A,[A,B]],\\tau^3[B,[A,B]]);\\ \\ \\{\\cdot,\\cdot\\}\\leftrightarrow\\tfrac{1}{i\\hbar}[\\cdot,\\cdot]", "breaks": "Classical integrators preserve symplecticity, which keeps the energy error bounded; quantum product formulas are exactly unitary. Quantum cost is counted in gates, and the error scales with commutator norms.", "confidence": "established", "strength": 2}
{"id": "C0596", "a": "01-classical-mechanics/newtonian-mechanics/kinematics-and-newtons-laws", "b": "04-quantum-physics/quantum-mechanics-core/postulates-and-formalism", "name": "Ehrenfest theorem: Newton's second law on average", "kind": "identity", "summary": "Expectation values obey m d²⟨x⟩/dt² = −⟨V′(x)⟩, Newton's second law for the centroid of a wave packet. The centroid follows the classical trajectory only when ⟨V′(x)⟩=V′(⟨x⟩): for at most quadratic potentials, or for packets narrow compared with the scale over which the force changes.", "map": "m\\frac{d^2\\langle\\hat x\\rangle}{dt^2}=-\\langle V'(\\hat x)\\rangle\\approx-V'(\\langle\\hat x\\rangle)\\ \\ (\\text{exact iff}\\ V'''=0)", "breaks": "Wave-packet spreading and anharmonicity spoil the agreement after the Ehrenfest time. The theorem does not imply classical behaviour of individual measurement outcomes.", "confidence": "established", "strength": 2}
{"id": "C0597", "a": "01-classical-mechanics/newtonian-mechanics/non-inertial-frames", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "name": "Atom interferometers as gravimeters and Sagnac gyroscopes", "kind": "method transfer", "summary": "Light-pulse atom interferometers turn the classical kinematics of free fall and rotating frames into matter-wave phases. The gravity phase k_eff g T² underlies atomic gravimeters, and the Sagnac phase from Earth's rotation makes atom gyroscopes; when rotation is not the target, the Coriolis terms must be compensated.", "map": "\\Delta\\phi_g=k_{\\rm eff}\\,g\\,T^2,\\qquad \\Delta\\phi_{\\rm Sagnac}=\\frac{2m}{\\hbar}\\,\\boldsymbol\\Omega\\cdot\\mathbf A", "breaks": "For equal area, the matter-wave Sagnac phase exceeds the optical one by mc²/ħω ~ 10^10, but atom interferometers enclose far smaller areas.", "confidence": "established", "strength": 2}
{"id": "C0598", "a": "01-classical-mechanics/newtonian-mechanics/non-inertial-frames", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "name": "Rotation as synthetic magnetism: Coriolis ↔ Lorentz", "kind": "identity", "summary": "In a frame rotating at Ω the Coriolis force has the form of a Lorentz force with qB=2mΩ. Rotating condensates therefore form triangular vortex lattices, like type-II superconductors in a field, and as Ω approaches the trap frequency they enter the lowest-Landau-level regime, which resembles the quantum Hall effect.", "map": "H_{\\rm rot}=\\frac{(\\mathbf p-m\\boldsymbol\\Omega\\times\\mathbf r)^2}{2m}+\\tfrac12m(\\omega_\\perp^2-\\Omega^2)r_\\perp^2,\\qquad q\\mathbf B\\leftrightarrow2m\\boldsymbol\\Omega", "breaks": "The centrifugal term weakens confinement and frees the gas as Ω→ω⊥, which has so far kept rotating gases out of deep fractional-quantum-Hall states. Laser-induced gauge fields avoid this problem.", "confidence": "established", "strength": 2}
{"id": "C0599", "a": "01-classical-mechanics/newtonian-mechanics/non-inertial-frames", "b": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "name": "Foucault pendulum precession as a holonomy", "kind": "identity", "summary": "After one sidereal day, the Foucault pendulum's plane of swing has turned by the solid angle enclosed by its circle of latitude, a holonomy of parallel transport on a sphere. The same geometry gives a spin's Berry phase as −m times the solid angle traced by the field direction.", "map": "\\Delta\\phi_{\\rm F}=\\Omega_{\\rm solid}=2\\pi(1-\\sin\\lambda)\\equiv-2\\pi\\sin\\lambda\\ (\\mathrm{mod}\\ 2\\pi)\\ \\leftrightarrow\\ \\gamma_m=-m\\,\\Omega_{\\rm solid}", "breaks": "Foucault's pendulum transports a real vector (an SO(2) holonomy of the sphere's Levi-Civita connection). Berry's phase is a U(1) phase of a complex state; it scales with m and shows up only relative to another path.", "confidence": "established", "strength": 3}
{"id": "C0600", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling", "name": "BGS conjecture: classical chaos ↔ random-matrix spectra", "kind": "mechanism", "summary": "Whether the classical limit is integrable or chaotic fixes the quantum level statistics: Poisson spacings for integrable motion (Berry–Tabor), Wigner–Dyson level repulsion for fully chaotic motion (Bohigas–Giannoni–Schmit), and intermediate statistics for mixed KAM phase spaces. Periodic-orbit theory explains why.", "map": "P_{\\rm int}(s)=e^{-s}\\ \\ \\text{vs}\\ \\ P_{\\rm GOE}(s)\\approx\\frac{\\pi s}{2}e^{-\\pi s^2/4}", "breaks": "There are exceptions. Arithmetic chaotic systems, such as billiards on special constant-curvature surfaces, show Poisson statistics, and non-generic integrable systems such as harmonic oscillators do not follow Berry–Tabor.", "confidence": "established", "strength": 3}
{"id": "C0601", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/bifurcations-and-routes-to-chaos", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "name": "Bosonic Josephson junction: pendulum bifurcation, self-trapping", "kind": "mechanism", "summary": "The mean-field dynamics of a condensate in a double well, in population imbalance z and relative phase φ, is that of a nonrigid pendulum. Raising the interaction parameter Λ through a bifurcation produces macroscopic quantum self-trapping, observed with rubidium in 2005; the large atom number N plays the role of 1/ħ.", "map": "\\dot z=-\\sqrt{1-z^2}\\sin\\phi,\\ \\ \\dot\\phi=\\Lambda z+\\frac{z\\cos\\phi}{\\sqrt{1-z^2}};\\ \\ \\text{self-trapping for}\\ \\Lambda>\\Lambda_c(z_0,\\phi_0)", "breaks": "At finite N, quantum fluctuations cause collapse and revival and tunnelling between the two self-trapped states. The classical pendulum is only the N→∞ limit.", "confidence": "established", "strength": 2}
{"id": "C0602", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/bifurcations-and-routes-to-chaos", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/floquet-systems-and-time-crystals", "name": "Period doubling vs discrete time-crystalline order", "kind": "analogy", "summary": "Driven dissipative classical systems (Faraday waves, parametrically driven pendula, period-doubling bifurcations) respond robustly at twice the drive period. Discrete time crystals are the many-body quantum version: a period-doubled response that resists drive imperfections and is long-range ordered, seen in trapped ions, NV centres and superconducting processors.", "map": "x(t+2T)=x(t)\\ (\\text{period-2 attractor})\\ \\leftrightarrow\\ \\langle\\hat\\sigma^z_i(nT)\\rangle\\propto(-1)^n", "breaks": "Classical period doubling relies on dissipation into an attractor. Closed quantum time crystals must avoid Floquet heating through many-body localization or prethermalization, and their rigidity is a many-body effect, although classical many-body time crystals in coupled dissipative oscillators have been proposed.", "confidence": "current research", "strength": 2}
{"id": "C0603", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos", "b": "04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical", "name": "Chaos, Ehrenfest time and decoherence", "kind": "mechanism", "summary": "Classical chaos stretches a wave packet exponentially, so an isolated chaotic system stops tracking its classical counterpart after the Ehrenfest time, ~λ⁻¹ln(S/ħ), which for Saturn's moon Hyperion is only decades. Environmental decoherence restores the classical Liouville limit. Zurek and Paz argued that the entropy production rate then becomes independent of ħ and is set by the Lyapunov exponents.", "map": "t_E\\sim\\frac{1}{\\lambda}\\ln\\frac{S}{\\hbar},\\qquad \\dot S_{\\rm vN}\\to\\sum_{\\lambda_i>0}\\lambda_i\\ \\ (\\text{decoherence-dominated regime})", "breaks": "Entropy production at the Lyapunov rate holds in an intermediate range of decoherence strength and is supported numerically, not proven in general.", "confidence": "current research", "strength": 2}
{"id": "C0604", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling", "name": "Lyapunov exponent ↔ OTOC growth and the chaos bound", "kind": "analogy", "summary": "The out-of-time-order correlator is the quantum version of the squared Poisson bracket {x(t),p}², which measures sensitivity to initial conditions. In semiclassical systems it therefore grows as e^{2λt}, with λ the classical Lyapunov exponent, until the scrambling time. Maldacena, Shenker and Stanford bounded the quantum rate by 2πk_BT/ħ.", "map": "C(t)=-\\langle[\\hat W(t),\\hat V]^2\\rangle\\sim\\hbar^2\\{W(t),V\\}^2\\sim\\hbar^2e^{2\\lambda t};\\ \\ \\lambda_L\\le\\frac{2\\pi k_BT}{\\hbar}", "breaks": "Exponential OTOC growth lasts only until t~λ⁻¹ln(1/ħ_eff). It is absent in many chaotic systems with small local Hilbert spaces (spin-1/2 chains), and unstable saddle points in integrable systems produce it without chaos. The thermal bound has no classical counterpart.", "confidence": "current research", "strength": 3}
{"id": "C0605", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth", "name": "Ergodicity: classical mixing vs eigenstate thermalization", "kind": "analogy", "summary": "Classical statistical mechanics rests on chaotic, mixing motion on the energy shell. Its quantum replacement, the eigenstate thermalization hypothesis, holds that individual eigenstates of chaotic Hamiltonians already look thermal; Srednicki derived it from Berry's random-wave conjecture for the eigenfunctions of classically chaotic systems.", "map": "\\langle E_m|\\hat O|E_n\\rangle=O(\\bar E)\\,\\delta_{mn}+e^{-S(\\bar E)/2}f_O(\\bar E,\\omega)R_{mn}", "breaks": "ETH concerns eigenstates, not trajectories, and does not need a classical limit (spin-1/2 chains obey it). Many-body localization and quantum many-body scars, named after Heller's periodic-orbit scars, violate it.", "confidence": "established", "strength": 3}
{"id": "C0606", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling", "name": "Kicked rotor: chaotic diffusion vs dynamical localization", "kind": "analogy", "summary": "Chirikov's standard map loses its last KAM torus near K≈0.97, after which momentum diffuses without bound. The quantum kicked rotor follows this diffusion only up to a break time and then localizes in momentum. Fishman, Grempel and Prange mapped this dynamical localization onto Anderson localization, and it was observed with cold atoms in pulsed optical standing waves.", "map": "p_{n+1}=p_n+K\\sin\\theta_n,\\ \\ \\theta_{n+1}=\\theta_n+p_{n+1};\\ \\ \\langle p^2\\rangle_{\\rm cl}\\approx\\tfrac{K^2}{2}n\\ \\ \\text{vs quantum saturation after}\\ t^*\\propto D/\\hbar_{\\rm eff}^2", "breaks": "Localization is a quantum interference effect with no classical counterpart. Noise or decoherence restores classical diffusion, and at quantum resonances (rational ħ_eff/4π) the energy grows ballistically.", "confidence": "established", "strength": 3}
{"id": "C0607", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos", "b": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "name": "Torus quantization (EBK) and Gutzwiller's periodic-orbit sum", "kind": "identity", "summary": "Einstein (1917) quantized the actions on invariant tori and noted that the rule fails when the tori are destroyed. KAM theory says which tori survive. For fully chaotic motion, Gutzwiller's trace formula, a stationary-phase evaluation of the path integral, replaces torus quantization with a sum over unstable periodic orbits.", "map": "\\oint_{\\gamma_i}\\mathbf p\\cdot d\\mathbf q=2\\pi\\hbar\\big(n_i+\\tfrac{\\mu_i}{4}\\big);\\ \\ \\rho(E)\\approx\\bar\\rho+\\sum_p\\frac{T_p\\cos(S_p/\\hbar-\\nu_p\\pi/2)}{\\pi\\hbar\\,|\\det(M_p-1)|^{1/2}}", "breaks": "Mixed phase spaces need both pictures, plus tunnelling between regular and chaotic regions. The periodic-orbit sum diverges because the number of orbits grows exponentially, so it has to be resummed.", "confidence": "established", "strength": 3}
{"id": "C0608", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "name": "Gross–Pitaevskii = NLS: matter-wave solitons", "kind": "identity", "summary": "In a 1D waveguide the Gross–Pitaevskii equation reduces to the integrable nonlinear Schrödinger equation. Repulsive condensates therefore carry dark solitons and attractive ones bright solitons and soliton trains, all seen in BECs between 1999 and 2002. The same equation governs solitons in optical fibres.", "map": "i\\partial_t\\psi=-\\tfrac12\\partial_x^2\\psi+g|\\psi|^2\\psi\\ (\\hbar=m=1);\\ \\ \\psi_{\\rm dark}=\\sqrt n\\tanh(x/\\sqrt2\\xi),\\ \\ \\xi=\\hbar/\\sqrt{2mgn}", "breaks": "Transverse confinement and the trap break integrability. In 2D and 3D, dark solitons decay into vortices through the snake instability, and attractive 3D condensates collapse. Beyond mean field, the quantum NLS (Lieb–Liniger) is solved by the Bethe ansatz.", "confidence": "established", "strength": 3}
{"id": "C0609", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth", "name": "Integrability blocks thermalization: Lax charges and GGE", "kind": "mechanism", "summary": "Classical integrable systems carry an extensive set of conserved quantities generated by a Lax pair. That is why soliton collisions are elastic and FPUT-type lattices recur instead of equilibrating. Quantum integrable systems (Lieb–Liniger, the quantum NLS) likewise fail to thermalize and relax to a generalized Gibbs ensemble, as the quantum Newton's cradle experiment showed.", "map": "\\dot L=[M,L]\\Rightarrow I_k=\\mathrm{Tr}\\,L^k\\ \\text{conserved};\\ \\ \\hat\\rho_{\\rm GGE}\\propto\\exp\\Big(-\\sum_k\\lambda_k\\hat I_k\\Big)", "breaks": "Quantum conserved charges constrain relaxation only if they are local or quasi-local. In both the classical and quantum cases, weak integrability breaking gives prethermal plateaus and eventually thermalization.", "confidence": "established", "strength": 3}
{"id": "C0610", "a": "01-classical-mechanics/oscillations-and-waves", "b": "04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems", "name": "Harmonic oscillator: normal modes to ladder operators", "kind": "identity", "summary": "Any small oscillation about equilibrium, once reduced to normal modes, quantizes to the quantum harmonic oscillator. The classical complex amplitude becomes the ladder operator a, giving the equally spaced spectrum ħω(n+1/2) that is the template for phonons, photons and quasiparticles.", "map": "H=\\frac{p^2}{2m}+\\tfrac12m\\omega^2x^2=\\hbar\\omega(a^\\dagger a+\\tfrac12),\\quad a=\\sqrt{\\tfrac{m\\omega}{2\\hbar}}\\Big(x+\\tfrac{ip}{m\\omega}\\Big)", "breaks": "The zero-point energy ħω/2 and the discrete exchange of energy have no classical counterpart. The equal level spacing is why the classical and quantum frequencies coincide.", "confidence": "established", "strength": 3}
{"id": "C0611", "a": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "name": "Bogoliubov transformation: normal modes of a condensate", "kind": "method transfer", "summary": "Linearizing about the condensate gives a quadratic bosonic Hamiltonian that a Bogoliubov transformation diagonalizes. This is normal-mode analysis with a symplectic rather than orthogonal transformation, and it yields phonon-like quasiparticles. In traps, the low-lying collective modes (the Kohn dipole mode at the trap frequency, breathing and quadrupole modes) are measured like classical normal modes.", "map": "\\varepsilon_k=\\sqrt{\\epsilon_k(\\epsilon_k+2gn)},\\ \\ \\epsilon_k=\\frac{\\hbar^2k^2}{2m};\\ \\ \\hat b_k=u_k\\hat a_k+v_k\\hat a_{-k}^\\dagger,\\ \\ u_k^2-v_k^2=1", "breaks": "Classical normal-mode analysis has no counterpart to the u,v mixing of creation and annihilation operators, which produces quantum depletion and a two-mode-squeezed ground state.", "confidence": "established", "strength": 2}
{"id": "C0612", "a": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "b": "04-quantum-physics/quantum-information-and-computation/trapped-ion-and-neutral-atom-qubits", "name": "Ion-crystal normal modes as the quantum bus", "kind": "shared object", "summary": "Ions in a linear Paul trap form a Coulomb crystal whose small oscillations split into normal modes (centre of mass, breathing, ...). These quantized modes mediate the Cirac–Zoller and Mølmer–Sørensen entangling gates and set the effective spin–spin couplings used in trapped-ion quantum simulation.", "map": "\\omega_{\\rm COM}=\\omega_z,\\ \\ \\omega_{\\rm br}=\\sqrt3\\,\\omega_z;\\ \\ J_{ij}\\propto\\sum_m\\frac{b_{im}b_{jm}}{\\mu^2-\\omega_m^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0613", "a": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "b": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "name": "Ring-polymer isomorphism for quantum statistics", "kind": "method transfer", "summary": "Discretizing the imaginary-time path integral maps a quantum particle at temperature T onto a classical ring polymer of P beads joined by harmonic springs. Classical molecular dynamics or Monte Carlo (PIMD, RPMD) can then compute quantum equilibrium properties, and the ring's normal modes are used to integrate and thermostat it efficiently.", "map": "Z\\approx\\int\\prod_{i=1}^Pdx_i\\,e^{-\\beta_P\\sum_i[\\frac m2\\omega_P^2(x_{i+1}-x_i)^2+V(x_i)]},\\ \\ \\beta_P=\\beta/P,\\ \\ \\omega_P=\\frac{P}{\\beta\\hbar}", "breaks": "It is exact only for equilibrium statics. Real-time quantum dynamics (RPMD) is an approximation, and fermions bring a sign problem.", "confidence": "established", "strength": 2}
{"id": "C0614", "a": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "b": "04-quantum-physics/quantum-optics/cavity-and-circuit-qed", "name": "Vacuum Rabi splitting vs classical normal-mode splitting", "kind": "analogy", "summary": "Two coupled resonators show an avoided crossing of width 2g, and the classical strong-coupling criterion g>κ,γ is the same as the quantum one. The single-excitation vacuum Rabi doublet of cavity QED matches this classical normal-mode splitting quantitatively.", "map": "\\omega_\\pm=\\omega\\pm g\\ (\\text{linear oscillators})\\ \\ \\text{vs}\\ \\ E_{n,\\pm}=n\\hbar\\omega\\pm\\hbar g\\sqrt n\\ (\\text{Jaynes–Cummings})", "breaks": "The anharmonic √n ladder of a two-level emitter (photon blockade, collapse and revival, number-dependent Rabi frequencies) has no linear classical counterpart. Only that ladder proves quantum strong coupling.", "confidence": "established", "strength": 2}
{"id": "C0615", "a": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "b": "04-quantum-physics/quantum-optics/quantized-light-and-photon-statistics", "name": "Field quantization = quantizing normal modes", "kind": "identity", "summary": "Expanding the electromagnetic field in cavity normal modes turns it into a set of uncoupled harmonic oscillators, just as normal-mode analysis decouples a chain of masses. Quantizing each mode gives photons, Planck's spectrum and vacuum fluctuations.", "map": "H=\\sum_k\\hbar\\omega_k\\big(a_k^\\dagger a_k+\\tfrac12\\big),\\quad \\hat{\\mathbf E}(\\mathbf r)=\\sum_k\\mathcal E_k\\big(a_k\\mathbf u_k(\\mathbf r)+\\mathrm{h.c.}\\big)", "breaks": "Classical equipartition, k_BT per mode, gives the Rayleigh–Jeans catastrophe. Quantizing the mode energies removes it.", "confidence": "established", "strength": 3}
{"id": "C0616", "a": "01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/laser-cooling-and-trapping", "name": "Optical molasses and the MOT as a damped oscillator", "kind": "mechanism", "summary": "Doppler cooling produces a velocity-dependent force F=−βv (hence 'optical molasses'), and the magneto-optical trap adds a restoring force −κx, so trapped atoms are damped, usually overdamped, harmonic oscillators. Random photon recoils supply the fluctuating force, and fluctuation–dissipation sets the Doppler limit.", "map": "m\\ddot x=-\\beta\\dot x-\\kappa x+F_{\\rm rand}(t),\\ \\ k_BT=\\frac{D_p}{\\beta}\\ \\Rightarrow\\ k_BT_D=\\frac{\\hbar\\Gamma}{2}", "breaks": "Sub-Doppler (Sisyphus) cooling and the recoil limit depend on optical pumping between internal states and on quantized photon momentum, which the damped-oscillator picture leaves out.", "confidence": "established", "strength": 2}
{"id": "C0617", "a": "01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/lindblad-master-equations", "name": "Damped oscillator: friction requires a bath", "kind": "mechanism", "summary": "Classical damping γ=ω₀/Q cannot come from a Hamiltonian for the oscillator alone. Quantum mechanically it comes from coupling to a bath (Caldeira–Leggett), which in the Markov limit gives a Lindblad equation with jump operators a and a†. The mean amplitude decays exactly as in the classical case, and fluctuation–dissipation adds thermal and zero-point noise.", "map": "\\dot\\rho=-\\tfrac{i}{\\hbar}[H,\\rho]+\\kappa(\\bar n+1)\\mathcal D[a]\\rho+\\kappa\\bar n\\,\\mathcal D[a^\\dagger]\\rho,\\ \\ \\kappa=\\omega_0/Q,\\ \\ \\langle a\\rangle\\propto e^{-\\kappa t/2}", "breaks": "The Lindblad form needs weak coupling and a Markovian bath. Strongly damped or low-temperature quantum Brownian motion is non-Markovian and has no exact Lindblad description.", "confidence": "established", "strength": 3}
{"id": "C0618", "a": "01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/non-hermitian-physics", "name": "Critical damping is an exceptional point", "kind": "identity", "summary": "Written as a first-order system, the damped oscillator has a non-Hermitian 2×2 dynamical matrix. At critical damping, γ=2ω₀, its eigenvalues and eigenvectors coalesce at an exceptional point, whose Jordan-block signature is the t e^{−γt/2} solution. Coupled gain/loss oscillators undergo their PT-symmetry-breaking transition at the same kind of point.", "map": "\\lambda_\\pm=-\\frac{\\gamma}{2}\\pm\\sqrt{\\frac{\\gamma^2}{4}-\\omega_0^2};\\ \\ \\text{eigenvalues and eigenvectors coalesce at}\\ \\gamma=2\\omega_0;\\ \\ \\delta\\lambda\\propto\\sqrt{\\epsilon}", "breaks": "Non-Hermitian quantum Hamiltonians describe post-selected or mean-field dynamics. Real quantum gain and loss add noise (Lindblad terms), which limits sensing enhanced by exceptional points.", "confidence": "established", "strength": 2}
{"id": "C0619", "a": "01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators", "b": "04-quantum-physics/quantum-optics/cavity-optomechanics", "name": "Mechanical resonator driven into the quantum regime", "kind": "shared object", "summary": "The mechanical element of an optomechanical system is a classical damped, driven oscillator whose frequency and damping are shifted by radiation pressure (optical spring, optical damping). Sideband cooling with κ<ω_m brings its mean phonon number below one, where zero-point motion and measurement backaction become observable.", "map": "m(\\ddot x+\\Gamma_m\\dot x+\\omega_m^2x)=F_{\\rm th}+F_{\\rm rad};\\quad Q_mf_m>k_BT/h\\ \\text{for one coherent oscillation per thermal phonon}", "breaks": "Backaction noise, the standard quantum limit and nonclassical motional states are beyond the classical oscillator, which captures only the mean response.", "confidence": "established", "strength": 3}
{"id": "C0620", "a": "01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators", "b": "04-quantum-physics/quantum-optics/quantized-light-and-photon-statistics", "name": "Coherent states: the quantum oscillator that moves classically", "kind": "identity", "summary": "A classically driven oscillator, or a classical current radiating into a mode, produces a coherent state: a displaced vacuum whose mean position and momentum follow the classical trajectory with constant minimum uncertainty. Glauber made it the reference classical state of light, with Poissonian photon counts.", "map": "|\\alpha(t)\\rangle=|\\alpha_0e^{-i\\omega t}\\rangle,\\ \\ \\langle\\hat x\\rangle=\\sqrt{\\tfrac{2\\hbar}{m\\omega}}|\\alpha_0|\\cos(\\omega t-\\phi),\\ \\ P(n)=e^{-|\\alpha|^2}\\frac{|\\alpha|^{2n}}{n!}", "breaks": "The correspondence holds only for quadratic Hamiltonians, and vacuum-level quadrature noise remains. States with sub-Poissonian statistics or negative Wigner functions have no classical counterpart.", "confidence": "established", "strength": 2}
{"id": "C0621", "a": "01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations", "b": "04-quantum-physics/foundations-of-quantum-mechanics/measurement-problem-and-interpretations", "name": "Walking droplets: a hydrodynamic pilot-wave analogue", "kind": "analogy", "summary": "Droplets bouncing on a bath vibrated vertically just below the Faraday (parametric) threshold are propelled by their own wave field. This macroscopic version of de Broglie's pilot wave shows quantized orbits, tunnelling-like crossings and wave-like statistics.", "map": "", "breaks": "The wave lives in real 3D space, not configuration space, so the system is local and cannot produce entanglement or Bell violations. The early single- and double-slit interference claims (Couder & Fort 2006) were not reproduced in later controlled experiments.", "confidence": "current research", "strength": 2}
{"id": "C0622", "a": "01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/floquet-systems-and-time-crystals", "name": "Mathieu/Kapitza ↔ Floquet theory and high-frequency expansion", "kind": "identity", "summary": "Floquet theory began in classical mechanics, with Hill's lunar equation, Floquet (1883) and the Mathieu equation. The quasienergies of a quantum Floquet Hamiltonian correspond to Floquet exponents, and Kapitza's effective potential for the inverted pendulum is the leading term of the high-frequency expansion used in Floquet engineering.", "map": "x(t+T)=e^{\\mu T}x(t)\\ \\leftrightarrow\\ \\psi(t)=e^{-i\\varepsilon t/\\hbar}\\phi(t),\\ \\phi(t+T)=\\phi(t);\\ \\ U_{\\rm eff}=U+\\frac{\\overline{f^2}}{2m\\omega^2}", "breaks": "The classical parametric instability becomes unbounded Floquet heating in interacting quantum systems. Many-body Floquet phases (time crystals, anomalous Floquet topology) have no single-oscillator counterpart.", "confidence": "established", "strength": 3}
{"id": "C0623", "a": "01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations", "b": "04-quantum-physics/quantum-information-and-computation/superconducting-qubits", "name": "Transmon as quantum pendulum and Duffing oscillator", "kind": "identity", "summary": "The transmon Hamiltonian is a quantum pendulum, and its eigenproblem in the charge basis is the Mathieu equation. Expanded about the minimum it is a weakly anharmonic (Duffing/Kerr) oscillator. Driven Duffing bistability gives bifurcation readout, and parametric pumping gives Josephson parametric amplifiers.", "map": "\\hat H=4E_C(\\hat n-n_g)^2-E_J\\cos\\hat\\varphi\\approx\\sqrt{8E_JE_C}\\,(a^\\dagger a+\\tfrac12)-\\tfrac{E_C}{2}a^{\\dagger2}a^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0624", "a": "01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations", "b": "04-quantum-physics/quantum-information-and-computation/trapped-ion-and-neutral-atom-qubits", "name": "Paul trap: Mathieu stability and Kapitza pseudopotential", "kind": "identity", "summary": "An ion in an RF quadrupole field obeys the Mathieu equation and is confined when (a,q) lies inside the first stability region. Its slow secular motion sits in a ponderomotive pseudopotential, the same averaging that stabilizes Kapitza's inverted pendulum, with residual micromotion at the drive frequency.", "map": "\\frac{d^2u}{d\\xi^2}+(a-2q\\cos2\\xi)u=0,\\ \\ \\xi=\\tfrac{\\Omega t}{2};\\ \\ \\omega_{\\rm sec}\\approx\\tfrac{\\Omega}{2}\\sqrt{a+q^2/2}\\ \\ (|a|,q\\ll1)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0625", "a": "01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations", "b": "04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology", "name": "Degenerate parametric amplification → squeezing", "kind": "mechanism", "summary": "Pumping an oscillator at twice its frequency amplifies one quadrature and de-amplifies the other. Classically this squeezes the thermal noise of a mechanical resonator (Rugar & Grütter 1991). In optics and Josephson circuits the same phase-sensitive gain squeezes vacuum fluctuations, which gravitational-wave interferometers inject to beat the shot-noise limit.", "map": "\\hat X_1\\to e^{r}\\hat X_1,\\ \\ \\hat X_2\\to e^{-r}\\hat X_2;\\ \\ \\Delta X_2^2=\\tfrac14e^{-2r}\\ (\\text{vacuum}:\\ \\tfrac14)", "breaks": "Below threshold, classical parametric squeezing inside a resonator is capped at 3 dB and never goes below zero-point noise. Sub-vacuum noise is the quantum resource.", "confidence": "established", "strength": 3}
{"id": "C0626", "a": "01-classical-mechanics/rigid-body-dynamics/gyroscopes-and-precession", "b": "04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin", "name": "Larmor precession: spin behaves as a gyroscope", "kind": "identity", "summary": "A magnetic moment μ=γS in a field feels a torque that makes its angular momentum precess, like a gyroscope under gravity. Because the spin Hamiltonian is linear in S, the Heisenberg equation for ⟨S⟩ is exactly this classical precession, which is the basis of the Bloch equations, NMR/MRI and spin-qubit control.", "map": "\\frac{d\\langle\\mathbf S\\rangle}{dt}=\\gamma\\langle\\mathbf S\\rangle\\times\\mathbf B\\ \\leftrightarrow\\ \\frac{d\\mathbf L}{dt}=\\boldsymbol\\tau=\\boldsymbol\\Omega_p\\times\\mathbf L;\\ \\ \\omega_L=\\gamma B", "breaks": "Only the mean precesses classically; individual measurements give quantized ±ħ/2. The electron's g≈2 also differs from the gyromagnetic ratio q/2m of a classical rotating charge.", "confidence": "established", "strength": 3}
{"id": "C0970", "a": "02-electromagnetism-and-optics/classical-optics", "b": "04-quantum-physics/quantum-optics/quantized-light-and-photon-statistics", "name": "Classical optics as the coherent-state limit", "kind": "identity", "summary": "Classical wave optics is reproduced exactly by quantized light in coherent states: first-order interference, diffraction and imaging depend only on mode functions and the mean field, so quantum features appear only in photon counting and higher-order correlations.", "map": "|\\alpha\\rangle:\\ \\langle\\hat E^{(+)}\\rangle=\\mathcal E\\,\\alpha\\,u(\\mathbf r)e^{-i\\omega t},\\ g^{(1)}\\ \\text{classical},\\ g^{(2)}=1", "breaks": "Fails for Fock, squeezed and entangled states and for g^(2)(0)<1 (antibunching), which no classical field can produce.", "confidence": "established", "strength": 3}
{"id": "C0971", "a": "02-electromagnetism-and-optics/classical-optics/coherence-and-statistical-optics", "b": "04-quantum-physics/quantum-optics/quantized-light-and-photon-statistics", "name": "Coherence functions: classical to Glauber", "kind": "identity", "summary": "The classical degree of coherence g^(1) and the Hanbury Brown–Twiss intensity correlation g^(2) become Glauber's normally ordered field correlators. Thermal bunching g^(2)(0)=2 appears in both theories; antibunching g^(2)(0)<1 is the purely quantum signature.", "map": "g^{(2)}(\\tau)=\\frac{\\langle\\hat E^-(t)\\hat E^-(t+\\tau)\\hat E^+(t+\\tau)\\hat E^+(t)\\rangle}{\\langle\\hat E^-\\hat E^+\\rangle^2};\\ \\text{classical } g^{(2)}(0)\\ge1", "breaks": "Classical stochastic fields obey g^(2)(0)>=1 and Cauchy–Schwarz inequalities that quantum light can violate.", "confidence": "established", "strength": 3}
{"id": "C0972", "a": "02-electromagnetism-and-optics/classical-optics/geometric-optics", "b": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "name": "Hamilton's optico-mechanical analogy: eikonal ↔ action", "kind": "historical", "summary": "Fermat's principle and the eikonal equation are the short-wavelength limit of wave optics, just as Hamilton–Jacobi mechanics is the ħ→0 limit of quantum mechanics. Schrödinger built wave mechanics by completing Hamilton's analogy, and WKB semiclassics is the eikonal method applied to matter waves.", "map": "|\\nabla\\mathcal S_{\\rm opt}|^2=n^2\\ \\leftrightarrow\\ |\\nabla S|^2=2m(E-V),\\ \\ k_0\\mathcal S_{\\rm opt}\\leftrightarrow S/\\hbar", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0973", "a": "02-electromagnetism-and-optics/classical-optics/interference-and-diffraction", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "name": "Atom interferometry: optical interferometers for atoms", "kind": "analogy", "summary": "Light-pulse atom interferometers copy the Mach–Zehnder geometry, with laser pulses as beam splitters and mirrors, and Ramsey's separated-field method is a two-slit experiment in time. They measure g, rotations and h/m and test the equivalence principle.", "map": "\\Delta\\phi=k_{\\rm eff}gT^2,\\ k_{\\rm eff}\\approx2k;\\ \\ \\text{Ramsey fringe width }\\Delta\\nu\\approx1/2T", "breaks": "Atoms are massive, with quadratic dispersion and internal states. Their phase picks up gravity and photon recoil, and their beam splitters are coherent internal-state transitions rather than passive optics.", "confidence": "established", "strength": 3}
{"id": "C0974", "a": "02-electromagnetism-and-optics/classical-optics/interference-and-diffraction", "b": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "name": "Huygens–Fresnel principle as free-particle propagator", "kind": "identity", "summary": "Fresnel diffraction sums secondary wavelets weighted by e^{ikr}, just as Feynman's path integral sums e^{iS/ħ}. The paraxial Fresnel kernel is the free-particle propagator with z↔t and k↔m/ħ, and stationary phase picks out rays, the optical counterpart of classical paths.", "map": "K=\\sqrt{\\frac{m}{2\\pi i\\hbar t}}e^{\\frac{im(x-x')^2}{2\\hbar t}}\\leftrightarrow h=\\sqrt{\\frac{k}{2\\pi iz}}e^{\\frac{ik(x-x')^2}{2z}},\\ \\frac{m}{\\hbar t}\\leftrightarrow\\frac{k}{z}", "breaks": "The optical 'time' z is a spatial coordinate, and the mapping fails beyond the paraxial, scalar approximation (obliquity factors, vector diffraction).", "confidence": "established", "strength": 3}
{"id": "C0975", "a": "02-electromagnetism-and-optics/classical-optics/interference-and-diffraction", "b": "04-quantum-physics/quantum-optics/single-photon-sources-and-detectors", "name": "Beam splitters: Mach–Zehnder to Hong–Ou–Mandel", "kind": "analogy", "summary": "The beam-splitter unitary is the same for classical field amplitudes and for photon creation operators, so a single photon reproduces classical fringes. Two identical photons bunch (the HOM dip) with visibility up to 100% against a classical maximum of 50%, which is how single-photon sources are certified as indistinguishable.", "map": "\\hat a_1^\\dagger\\to\\frac{\\hat a_3^\\dagger+\\hat a_4^\\dagger}{\\sqrt2},\\ \\hat a_2^\\dagger\\to\\frac{\\hat a_3^\\dagger-\\hat a_4^\\dagger}{\\sqrt2}\\Rightarrow|1,1\\rangle\\to\\frac{|2,0\\rangle-|0,2\\rangle}{\\sqrt2}", "breaks": "Two-photon interference depends on number states and photon indistinguishability; no classical field gives HOM visibility above 50%.", "confidence": "established", "strength": 3}
{"id": "C0976", "a": "02-electromagnetism-and-optics/classical-optics/interference-and-diffraction", "b": "04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology", "name": "Interferometer shot noise and squeezed-vacuum injection", "kind": "mechanism", "summary": "With coherent light, a Michelson or Mach–Zehnder interferometer's phase sensitivity is shot-noise limited at 1/√N. Caves showed this noise enters as vacuum fluctuations through the unused port, so injecting squeezed vacuum there beats the limit, as LIGO and Virgo now do.", "map": "\\Delta\\phi_{\\rm SNL}=\\frac{1}{\\sqrt N}\\to\\frac{e^{-r}}{\\sqrt N},\\ \\ \\Delta\\phi_{\\rm HL}=\\frac{1}{N}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0977", "a": "02-electromagnetism-and-optics/classical-optics/polarization-and-crystal-optics", "b": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "name": "Polarization qubits and polarization entanglement", "kind": "shared object", "summary": "Jones vectors are qubit states and wave plates are SU(2) gates. Photon pairs entangled in polarization are therefore the main platform for entanglement witnesses, state tomography and Bell tests.", "map": "|H\\rangle,|V\\rangle\\to|0\\rangle,|1\\rangle;\\ |\\Phi^+\\rangle=(|HH\\rangle+|VV\\rangle)/\\sqrt2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0978", "a": "02-electromagnetism-and-optics/classical-optics/polarization-and-crystal-optics", "b": "04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin", "name": "Photon spin and orbital angular momentum", "kind": "identity", "summary": "Circularly polarized light carries spin angular momentum ±ħ per photon (Beth 1936), and Laguerre–Gauss beams with phase e^{iℓφ} carry orbital angular momentum ℓħ. Transfer to atoms follows the Δm selection rules, and both degrees of freedom serve as qudit encodings.", "map": "J_z=(\\sigma+\\ell)\\hbar\\ \\text{per photon},\\ \\sigma=\\pm1;\\ \\ \\sigma^\\pm\\text{ light drives }\\Delta m=\\pm1", "breaks": "The massless photon has only helicity ±1 (no m=0 state), and the split into spin and orbital parts is gauge-dependent outside the paraxial regime.", "confidence": "established", "strength": 2}
{"id": "C0979", "a": "02-electromagnetism-and-optics/classical-optics/polarization-and-crystal-optics", "b": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "name": "Pancharatnam phase on the Poincaré sphere", "kind": "identity", "summary": "Pancharatnam (1956) found that light taken around a closed cycle of polarization states gains a phase of minus half the solid angle it encloses on the Poincaré sphere. This is Berry's spin-1/2 phase, found in optics decades earlier, and it is now used in Pancharatnam–Berry geometric-phase metasurfaces.", "map": "\\gamma_{\\rm P}=-\\tfrac12\\Omega_{\\rm PS}\\ \\leftrightarrow\\ \\gamma_B=-\\tfrac12\\Omega\\ (\\text{spin-}\\tfrac12\\text{ on Bloch sphere})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0980", "a": "02-electromagnetism-and-optics/classical-optics/polarization-and-crystal-optics", "b": "04-quantum-physics/quantum-mechanics-core/postulates-and-formalism", "name": "Polarization coherency matrix = qubit density matrix", "kind": "identity", "summary": "The 2×2 coherency matrix of partially polarized light is a density matrix whose Stokes parameters are the Bloch-vector components. The degree of polarization is the Bloch-vector length, wave plates act as unitaries, and depolarizing elements (Mueller matrices) act as quantum channels.", "map": "J=\\tfrac12(S_0\\mathbb 1+\\mathbf S\\cdot\\boldsymbol\\sigma)\\leftrightarrow\\rho=\\tfrac12(\\mathbb 1+\\mathbf r\\cdot\\boldsymbol\\sigma),\\ P=|\\mathbf S|/S_0=|\\mathbf r|", "breaks": "Classical partial polarization is an ensemble average over field fluctuations; beams that are nonseparable in polarization and spatial mode ('classical entanglement') show no nonlocality.", "confidence": "established", "strength": 3}
{"id": "C0981", "a": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling", "name": "Microwave billiards as quantum-chaos simulators", "kind": "method transfer", "summary": "Below the cutoff of the second vertical mode, a flat microwave cavity's TM modes obey the 2D Helmholtz equation, which is the Schrödinger equation of a particle in a hard-wall billiard. Measured resonance spectra test random-matrix level statistics (GOE for chaotic shapes) and wavefunction scarring.", "map": "(\\nabla^2+k^2)E_z=0\\ \\leftrightarrow\\ (\\nabla^2+2mE/\\hbar^2)\\psi=0,\\ \\ E_z|_{\\partial\\Omega}=0", "breaks": "Holds only for the lowest TM modes of thin cavities. Absorption broadens the levels, and time reversal can be broken only by adding ferrites.", "confidence": "established", "strength": 3}
{"id": "C0982", "a": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "b": "04-quantum-physics/quantum-optics/cavity-and-circuit-qed", "name": "Transmission-line resonators as circuit-QED cavities", "kind": "shared object", "summary": "Superconducting coplanar-waveguide resonators, which are classical transmission lines with standing-wave modes, supply the photon modes of circuit QED. Their tiny transverse mode volume makes vacuum fields large enough for a transmon to reach strong coupling.", "map": "\\omega_n=\\frac{n\\pi v_p}{\\ell},\\ v_p=\\frac{1}{\\sqrt{L_\\ell C_\\ell}},\\ \\hat H=\\hbar\\omega_r(\\hat a^\\dagger\\hat a+\\tfrac12),\\ V_{\\rm rms}=\\sqrt{\\hbar\\omega_r/2C}", "breaks": "", "confidence": "established", "strength": 3}