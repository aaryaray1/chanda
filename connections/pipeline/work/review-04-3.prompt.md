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

### Optical lattices and quantum simulation · `knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation`

**Scope.** Standing-wave lattices, band structure and Wannier functions, Bose–Hubbard superfluid–Mott transition, Fermi–Hubbard antiferromagnetism, single-site imaging, synthetic gauge fields, Rydberg-atom arrays as spin simulators, many-body localization experiments.

**Core ideas.**
- Deep lattices map onto Hubbard models with tunnelling $J$ and on-site interaction $U$ controlled by laser intensity and Feshbach fields.
- Quantum gas microscopes resolve individual atoms, giving direct access to correlations.
- Analog simulators address problems (doped Hubbard, real-time dynamics) where classical computation struggles.

**Key equations.**
$$H_{\text{BH}}=-J\sum_{\langle ij\rangle}b_i^\dagger b_j+\frac U2\sum_in_i(n_i-1)-\mu\sum_in_i,\qquad (U/J)_c\approx29\ (3\text{D},\ n=1)$$

**See also.** [Hubbard model and Mott physics](knowledge/08-condensed-matter/strongly-correlated-electrons/hubbard-model-and-mott-physics/README.md) · [Thermalization and ETH](knowledge/04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth/README.md)

### Ultracold molecules · `knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/ultracold-molecules`

**Scope.** Magnetoassociation and STIRAP to ground-state molecules (KRb, NaK), direct laser cooling (SrF, CaF), molecular tweezer arrays, dipolar quantum matter, quantum-state-controlled chemistry, electron EDM experiments (ACME ThO, JILA HfF⁺).

**Core ideas.**
- Rich internal structure (rotation, vibration) makes molecules hard to cool but excellent qubits and sensors.
- Long-range anisotropic dipole–dipole interactions ($\propto1/r^3$) enable new many-body phases.
- Polar molecules amplify the electron EDM by huge internal effective fields (~10–100 GV/cm).

**Key equations.**
$$V_{dd}(\mathbf r)=\frac{d^2}{4\pi\epsilon_0}\frac{1-3\cos^2\theta}{r^3}$$

**See also.** [Reaction dynamics](knowledge/11-interdisciplinary-physics/chemical-physics/reaction-dynamics/README.md) · [CP violation](knowledge/06-particle-physics/standard-model/cp-violation/README.md)

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

### Bell nonlocality · `knowledge/04-quantum-physics/foundations-of-quantum-mechanics/bell-nonlocality`

**Scope.** Local hidden-variable models, Bell and CHSH inequalities, Tsirelson bound, no-signalling, locality/detection/freedom-of-choice loopholes, 2015 loophole-free tests (Delft, Vienna, NIST), device-independent randomness and QKD, network nonlocality.

**Core ideas.**
- Any theory with local causality and measurement independence obeys CHSH $\le2$; quantum mechanics reaches $2\sqrt2$.
- Nonlocal correlations cannot be used to signal faster than light.
- Bell violation certifies randomness and security without trusting the devices.

**Key equations.**
$$S_{\text{QM}}^{\max}=2\sqrt2\ \text{for}\ |\Phi^+\rangle,\ \text{settings }0,\tfrac\pi4\ \text{(A)};\ \tfrac\pi8,-\tfrac\pi8\ \text{(B)}$$

**See also.** [Entanglement theory](knowledge/04-quantum-physics/quantum-information-and-computation/entanglement-theory/README.md)

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

### Quantum thermodynamics · `knowledge/04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-thermodynamics`

**Scope.** Definitions of work in quantum systems (two-point measurement), quantum fluctuation theorems, resource theory of athermality, coherence as a thermodynamic resource, quantum heat engines and refrigerators, Landauer's principle, thermodynamic uncertainty relations.

**Core ideas.**
- Work is not an observable; the two-point-measurement scheme defines its distribution.
- Thermal operations formalize what is achievable without external resources, giving a family of second laws.
- Quantum engines are bounded by Carnot but coherence and correlations change power–efficiency trade-offs.

**Key equations.**
$$\langle e^{-\beta W}\rangle=e^{-\beta\Delta F},\qquad W_{\text{erase}}\ge k_BT\ln2$$

**See also.** [Stochastic thermodynamics](knowledge/03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-thermodynamics-and-fluctuation-theorems/README.md) · [Heat engines](knowledge/03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/heat-engines-and-efficiency/README.md)

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

### Photonic and spin qubits · `knowledge/04-quantum-physics/quantum-information-and-computation/photonic-and-spin-qubits`

**Scope.** KLM scheme, fusion-based and measurement-based photonic QC, GKP states, integrated photonic circuits, gate-defined quantum-dot spin qubits in Si/SiGe, donor spins, NV and SiV centers, spin–photon interfaces, hot-qubit operation above 1 K.

**Core ideas.**
- Photons barely decohere but barely interact; entangling gates are probabilistic and need heralding and resource states.
- Silicon spin qubits are tiny (~100 nm) and CMOS-compatible — attractive for dense integration.
- Color centers combine long-lived nuclear-spin memories with optical links — good network nodes.

**Key equations.**
$$H_{\text{spin}}=g\mu_B\mathbf B\cdot\mathbf S+J\,\mathbf S_1\cdot\mathbf S_2\quad(\text{exchange gate})$$

**See also.** [Single-photon sources](knowledge/04-quantum-physics/quantum-optics/single-photon-sources-and-detectors/README.md) · [Quantum dots](knowledge/08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures/README.md)

### Quantum algorithms and complexity · `knowledge/04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity`

**Scope.** Quantum Fourier transform, phase estimation, Shor's factoring, Grover search and amplitude amplification, Hamiltonian simulation (Trotter, qubitization), HHL, VQE and QAOA, BQP and its relation to NP and PH, random-circuit sampling and boson-sampling advantage, dequantization results.

**Core ideas.**
- Exponential speedups come from structure (periodicity, simulation of quantum dynamics), not from "trying all answers".
- Grover's quadratic speedup is optimal for unstructured search.
- Quantum-advantage claims are contested by improved classical simulation; verifiability matters.

**Key equations.**
$$\text{QFT}:|x\rangle\mapsto\frac{1}{\sqrt N}\sum_ye^{2\pi ixy/N}|y\rangle,\qquad T_{\text{Grover}}\approx\frac\pi4\sqrt{N}$$

**See also.** [Quantum chemistry methods](knowledge/11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods/README.md)

### Quantum communication and cryptography · `knowledge/04-quantum-physics/quantum-information-and-computation/quantum-communication-and-cryptography`

**Scope.** BB84 and E91 protocols, decoy states, measurement-device-independent and device-independent QKD, satellite QKD (Micius), teleportation, entanglement swapping, quantum repeaters and memories, post-quantum vs. quantum cryptography.

**Core ideas.**
- Eavesdropping disturbs non-orthogonal states (no-cloning), so the error rate bounds the eavesdropper's information.
- Photon loss in fibre grows exponentially with distance; repeaters need entanglement swapping plus quantum memories.
- Security proofs must model real devices — side-channel attacks have broken idealized implementations.

**Key equations.**
$$r_{\text{BB84}}\ge1-2h(Q),\qquad h(x)=-x\log_2x-(1-x)\log_2(1-x),\qquad Q<11\%$$

**See also.** [Bell nonlocality](knowledge/04-quantum-physics/foundations-of-quantum-mechanics/bell-nonlocality/README.md) · [Integrated and fiber photonics](knowledge/02-electromagnetism-and-optics/photonics-and-lasers/integrated-and-fiber-photonics/README.md)

### Quantum error correction and fault tolerance · `knowledge/04-quantum-physics/quantum-information-and-computation/quantum-error-correction-and-fault-tolerance`

**Scope.** Shor and Steane codes, stabilizer formalism, CSS codes, toric and surface codes, threshold theorem, decoders (MWPM, union-find, neural), lattice surgery, magic-state distillation, bosonic codes (cat, GKP), qLDPC codes, below-threshold experiments (Google 2024), logical processors with atom arrays.

**Core ideas.**
- Measure stabilizers (parity checks) to learn the error syndrome without learning the encoded state.
- Surface code: local checks on a 2D grid, threshold ~1%, logical error suppressed exponentially in distance $d$.
- Clifford gates are cheap; non-Clifford (T) gates need magic states — the dominant overhead.

**Key equations.**
$$[[n,k,d]]:\ \text{surface code}\ [[d^2,1,d]],\qquad \Lambda=\frac{\epsilon_d}{\epsilon_{d+2}}>1\ \text{below threshold}$$

**See also.** [Topological order](knowledge/08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order/README.md)

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

# Packet 04-3 (100 records)

{"id": "C1642", "a": "04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical", "b": "04-quantum-physics/quantum-optics/cavity-and-circuit-qed", "name": "Watching field cat states decohere in a cavity", "kind": "historical", "summary": "Rydberg-atom cavity QED prepared superpositions of coherent fields with different phases and measured their coherence decay. The decay sped up with the separation of the two components, as decoherence theory predicts. Circuit QED later turned such microwave cats into bosonic qubits.", "map": "\\langle\\alpha|\\rho|\\beta\\rangle\\propto\\exp\\left(-\\tfrac{\\kappa t}{2}|\\alpha-\\beta|^2\\right)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1643", "a": "04-quantum-physics/foundations-of-quantum-mechanics/measurement-problem-and-interpretations", "b": "04-quantum-physics/quantum-mechanics-core/postulates-and-formalism", "name": "Two dynamics in the postulates: the measurement problem", "kind": "identity", "summary": "The textbook postulates combine unitary Schrödinger evolution with a projection (Born-rule) postulate for measurement. The tension between the two is the measurement problem, and interpretations differ by which postulate they drop, reinterpret or modify (many-worlds, Bohm, collapse models, QBism).", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1644", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/floquet-systems-and-time-crystals", "b": "04-quantum-physics/quantum-mechanics-core/approximation-methods", "name": "High-frequency (Magnus) expansion gives Floquet Hamiltonians", "kind": "method transfer", "summary": "Time-dependent perturbation theory in 1/ω (Magnus or van Vleck expansion) gives an effective static Floquet Hamiltonian. It explains Kapitza stabilization, coherent destruction of tunnelling and engineered Peierls phases, and its breakdown signals heating toward infinite temperature.", "map": "H_F=H_0+\\frac{1}{\\hbar\\omega}\\sum_{m\\ge1}\\frac{[H_m,H_{-m}]}{m}+O(\\omega^{-2})", "breaks": "In interacting many-body systems the series is only asymptotic. It holds for prethermal times that grow exponentially in ω/J.", "confidence": "established", "strength": 2}
{"id": "C1645", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/lindblad-master-equations", "b": "04-quantum-physics/quantum-optics/cavity-and-circuit-qed", "name": "Quantum jumps observed in cavity and circuit QED", "kind": "shared object", "summary": "Cavity damping and spontaneous emission are the canonical Lindblad dissipators. Continuous photon counting and homodyne readout in cavity and circuit QED record individual quantum trajectories, from photon-number jumps in a Rydberg-atom cavity to the mid-flight reversal of a transmon's jump.", "map": "\\mathcal D[\\sqrt\\kappa\\,a]\\rho,\\quad \\gamma_{\\rm Purcell}\\approx\\kappa\\frac{g^2}{\\Delta^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1646", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/non-hermitian-physics", "b": "04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology", "name": "Exceptional-point sensing versus quantum noise limits", "kind": "mechanism", "summary": "Near an order-n exceptional point, eigenvalue splitting responds to a perturbation as ε^{1/n}, which seems to promise sensors with diverging susceptibility. Quantum-noise analyses find the signal-to-noise gain largely cancels because eigenvector coalescence (the Petermann factor) amplifies noise too, so EP-enhanced metrology remains contested.", "map": "\\Delta\\omega\\propto\\epsilon^{1/n}\\ (\\text{order-}n\\ \\text{EP}),\\quad K_{\\rm Petermann}\\to\\infty", "breaks": "The square-root response exists only in the eigenfrequencies. Once fundamental quantum noise is included, the Fisher information per resource does not diverge.", "confidence": "current research", "strength": 2}
{"id": "C1647", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling", "b": "04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity", "name": "Random-circuit sampling rests on Porter–Thomas statistics", "kind": "mechanism", "summary": "Quantum-advantage experiments sample from deep random circuits whose output probabilities follow the Porter–Thomas distribution of chaotic, Haar-like states. Cross-entropy benchmarking relies on this random-matrix statistics, and classical spoofing algorithms exploit departures from it.", "map": "P(p)=Ne^{-Np}\\ (N=2^n),\\quad F_{\\rm XEB}=N\\langle p(x_i)\\rangle-1", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1648", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling", "b": "04-quantum-physics/quantum-information-and-computation/quantum-error-correction-and-fault-tolerance", "name": "Scrambling as encoding: Hayden–Preskill and random codes", "kind": "mechanism", "summary": "Chaotic dynamics spreads local information into nonlocal correlations, which is what an error-correcting encoding does. OTOC decay measures this spreading, Hayden–Preskill decoding treats black-hole scrambling as a code, and random circuits produce near-optimal codes.", "map": "F(t)=\\langle W^\\dagger(t)V^\\dagger W(t)V\\rangle,\\quad \\lambda_L\\le\\frac{2\\pi k_BT}{\\hbar}", "breaks": "Scrambling unitaries are generic codes with no efficient decoder. Practical fault tolerance needs structured codes such as stabilizer or surface codes with local checks.", "confidence": "current research", "strength": 2}
{"id": "C1649", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling", "b": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "name": "Gutzwiller trace formula: periodic orbits to spectra", "kind": "method transfer", "summary": "Stationary-phase evaluation of the trace of the propagator writes the density of states of a chaotic system as a sum over classical periodic orbits. Berry's diagonal approximation and Sieber–Richter orbit pairs then reproduce random-matrix form factors, explaining the Bohigas–Giannoni–Schmit universality.", "map": "\\rho(E)\\approx\\bar\\rho(E)+\\frac{1}{\\pi\\hbar}\\sum_p\\frac{T_p}{|\\det(M_p-1)|^{1/2}}\\cos\\left(\\frac{S_p}{\\hbar}-\\frac{\\mu_p\\pi}{2}\\right)", "breaks": "The orbit sum diverges exponentially. Beyond the Heisenberg time it needs resummation, and it only applies in the semiclassical limit.", "confidence": "established", "strength": 3}
{"id": "C1650", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth", "b": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "name": "Eigenstate entanglement: volume law vs area law", "kind": "identity", "summary": "In ETH systems the entanglement entropy of a small subsystem in a mid-spectrum eigenstate equals the thermal entropy (a volume law, as in Page's random states). Many-body-localized eigenstates obey an area law and show logarithmic entanglement growth after quenches, so entanglement scaling diagnoses the phase.", "map": "S_A=-{\\rm Tr}\\,\\rho_A\\ln\\rho_A\\approx s_{\\rm th}(E)|A|\\ (\\text{ETH}),\\quad S_A\\propto|\\partial A|\\ (\\text{MBL})", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1651", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth", "b": "04-quantum-physics/quantum-information-and-computation/trapped-ion-and-neutral-atom-qubits", "name": "Many-body scars discovered in Rydberg atom arrays", "kind": "shared object", "summary": "Quenches in a 51-atom Rydberg-blockaded chain showed long-lived revivals from the Néel state. These are explained by quantum many-body scars of the PXP model, a weak ETH violation by a tower of non-thermal eigenstates; ion chains have probed MBL and prethermal dynamics in the same way.", "map": "H_{\\rm PXP}=\\Omega\\sum_iP_{i-1}X_iP_{i+1}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1652", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth", "b": "04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems", "name": "Integrable systems relax to generalized Gibbs ensembles", "kind": "mechanism", "summary": "Bethe-ansatz and free-fermion models (Lieb–Liniger, XXZ) have extensively many local conserved charges, so after a quench they violate ETH and relax to a generalized Gibbs ensemble. The quantum Newton's cradle showed a near-integrable 1D Bose gas failing to thermalize.", "map": "\\rho_{\\rm GGE}=Z^{-1}\\exp\\Big(-\\sum_k\\lambda_k\\hat I_k\\Big)", "breaks": "Weak integrability breaking causes prethermalization to the GGE followed by slow true thermalization.", "confidence": "established", "strength": 3}
{"id": "C1653", "a": "04-quantum-physics/quantum-information-and-computation/photonic-and-spin-qubits", "b": "04-quantum-physics/quantum-optics/single-photon-sources-and-detectors", "name": "Indistinguishable single photons fuel photonic qubits", "kind": "method transfer", "summary": "Linear-optical (KLM) and measurement-based photonic computing need on-demand, indistinguishable photons (high Hong–Ou–Mandel visibility) and efficient detectors. Quantum dots and color centers serve both as photon sources and as spin–photon interfaces for spin qubits.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1654", "a": "04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity", "b": "04-quantum-physics/quantum-mechanics-core/approximation-methods", "name": "Adiabatic theorem becomes adiabatic quantum computing", "kind": "method transfer", "summary": "A problem's answer is encoded in the ground state of H_P and reached by slowly interpolating from an easy H_0. The adiabatic theorem sets the runtime by the minimum gap. This model is polynomially equivalent to the circuit model and underlies quantum annealing.", "map": "H(s)=(1-s)H_0+sH_P,\\quad T\\gg\\frac{\\hbar\\max_s\\|\\partial_sH\\|}{\\Delta_{\\min}^2}", "breaks": "Exponentially small gaps at first-order transitions remove any speedup. Open-system annealers also depart from ideal adiabatic evolution.", "confidence": "established", "strength": 3}
{"id": "C1655", "a": "04-quantum-physics/quantum-information-and-computation/quantum-communication-and-cryptography", "b": "04-quantum-physics/quantum-optics/single-photon-sources-and-detectors", "name": "Photon sources and detectors set QKD security and reach", "kind": "mechanism", "summary": "Attenuated lasers emit multiphoton pulses that are open to photon-number-splitting attacks; decoy states or true single-photon sources counter this. Detector efficiency, dark counts and jitter limit key rate and distance, and detector-blinding attacks motivated measurement-device-independent QKD.", "map": "P(n\\ge2)\\approx\\mu^2/2\\ \\text{(weak coherent pulse)},\\quad R\\propto\\eta_{\\rm ch}\\eta_{\\rm det}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1656", "a": "04-quantum-physics/quantum-information-and-computation/superconducting-qubits", "b": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "name": "Macroscopic quantum tunnelling of the Josephson phase", "kind": "historical", "summary": "Instanton (bounce) calculations of escape from a metastable well, including Caldeira–Leggett dissipation, predicted the tunnelling rate of a current-biased Josephson junction. The 1980s observation of macroscopic quantum tunnelling and level quantization in junctions founded phase qubits and, later, transmons.", "map": "\\Gamma\\approx a_q\\frac{\\omega_p}{2\\pi}\\exp\\left(-\\frac{36\\,\\Delta U}{5\\hbar\\omega_p}\\right)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1657", "a": "04-quantum-physics/quantum-information-and-computation/superconducting-qubits", "b": "04-quantum-physics/quantum-optics/cavity-and-circuit-qed", "name": "Circuit QED: a transmon is a Jaynes–Cummings atom", "kind": "identity", "summary": "A transmon coupled to a microwave resonator realizes the Jaynes–Cummings Hamiltonian at strong coupling. In the dispersive regime the qubit-state-dependent cavity shift gives QND readout, and the resonator acts as a bus for two-qubit gates.", "map": "H=\\hbar\\omega_r a^\\dagger a+\\tfrac{\\hbar\\omega_q}{2}\\sigma_z+\\hbar g(a\\sigma_++a^\\dagger\\sigma_-),\\ \\chi\\simeq g^2/\\Delta", "breaks": "The transmon's weak anharmonicity means higher levels change the dispersive shift (χ = g²α/[Δ(Δ+α)]), so the two-level-atom picture is only approximate.", "confidence": "established", "strength": 3}
{"id": "C1658", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "b": "05-relativity-and-gravitation/general-relativity/tests-of-general-relativity", "name": "Clocks resolve the gravitational redshift", "kind": "method transfer", "summary": "Optical lattice and ion clocks at 1e-18 measure the GR redshift over cm (now sub-mm) heights, turning a classic GR test into a table-top AMO measurement and enabling chronometric geodesy.", "map": "\\Delta\\nu/\\nu=g\\Delta h/c^2\\approx1.1\\times10^{-18}\\ \\mathrm{per\\ cm}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1659", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "b": "05-relativity-and-gravitation/general-relativity/tests-of-general-relativity", "name": "Quantum tests of the equivalence principle", "kind": "method transfer", "summary": "Matter-wave interferometry tests free-fall universality and gravitational phase shifts with quantum probes: the COW neutron experiment, then dual-species atom interferometers comparing isotopes.", "map": "\\phi=k_{\\rm eff}gT^2;\\ \\eta=2|g_1-g_2|/(g_1+g_2)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1660", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "b": "05-relativity-and-gravitation/gravitational-waves/pulsar-timing-arrays", "name": "Atomic time underlies pulsar timing", "kind": "shared object", "summary": "Pulsar arrival times are referenced to atomic time; clock-standard errors appear as a monopolar correlated residual distinct from the quadrupolar Hellings-Downs signature, and pulsar ensembles can cross-check atomic time scales.", "map": "\\Gamma_{\\rm clock}(\\zeta)=1\\ \\text{vs}\\ \\Gamma_{\\rm HD}(\\zeta)", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1661", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "b": "05-relativity-and-gravitation/gravitational-waves/space-based-and-future-detectors", "name": "Atom interferometers and clocks as GW detectors", "kind": "method transfer", "summary": "Proposed mid-band (0.01-10 Hz) detectors replace laser arms by light-pulse atom interferometry or clock comparisons between distant ensembles, using single-photon transitions to cancel laser phase noise.", "map": "\\Delta\\phi\\sim\\omega_A hL/c;\\ \\delta\\nu/\\nu\\sim h", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1662", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "b": "05-relativity-and-gravitation/special-relativity/tests-of-lorentz-invariance", "name": "Clock comparisons as Lorentz-symmetry tests", "kind": "method transfer", "summary": "Ion and lattice clocks and entangled ion pairs bound Standard-Model-Extension coefficients through sidereal modulation of transition frequencies; clock pairs also measured time dilation at m/s speeds.", "map": "\\delta\\nu(t)\\propto c^{e}_{\\mu\\nu}\\langle p^\\mu p^\\nu\\rangle\\ \\text{modulated at }\\omega_\\oplus", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1663", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "05-relativity-and-gravitation/black-holes/black-hole-thermodynamics-and-hawking-radiation", "name": "Acoustic horizons and analogue Hawking radiation", "kind": "analogy", "summary": "Bogoliubov phonons in a flowing BEC propagate on an acoustic metric; where flow exceeds sound speed a horizon forms and thermal, entangled phonon pairs are emitted. Curated in the analogue-gravity theme.", "map": "T_H=\\frac{\\hbar}{2\\pi k_B}\\left|\\partial_x(c_s-v)\\right|_{\\rm hor}", "breaks": "Kinematics only: no Einstein dynamics or backreaction; Bogoliubov dispersion breaks Lorentz invariance at the healing length; nK signals sit on thermal noise.", "confidence": "current research", "strength": 3}
{"id": "C1664", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "05-relativity-and-gravitation/quantum-gravity/qft-in-curved-spacetime", "name": "BEC simulators of cosmological particle creation", "kind": "analogy", "summary": "Rapidly expanding ring BECs and modulated condensates emulate particle creation in expanding spacetimes and Unruh radiation, testing QFT-in-curved-spacetime kinematics with phonons.", "map": "\\ddot\\chi_k+c_s^2(t)k^2a^{-2}(t)\\chi_k=0", "breaks": "Effective metric only; condensate dissipation and nonlinearity have no curved-spacetime counterpart.", "confidence": "current research", "strength": 2}
{"id": "C1665", "a": "04-quantum-physics/foundations-of-quantum-mechanics", "b": "05-relativity-and-gravitation/quantum-gravity/other-approaches-to-quantum-gravity", "name": "Quantum foundations meets quantum gravity", "kind": "historical", "summary": "Tabletop tests of the quantum nature of gravity (gravity-induced entanglement, gravitational collapse) grew out of foundations research and tie the measurement problem to the quantum status of spacetime.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1666", "a": "04-quantum-physics/foundations-of-quantum-mechanics/bell-nonlocality", "b": "05-relativity-and-gravitation/special-relativity/lorentz-transformations-and-spacetime", "name": "Bell tests need spacelike separation", "kind": "shared object", "summary": "Bell's local causality is defined by light cones; loophole-free tests choose settings and record outcomes at spacelike separation, and no-signalling keeps quantum nonlocality compatible with relativity.", "map": "|\\mathbf x_A-\\mathbf x_B|>c|t_A-t_B|", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1667", "a": "04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical", "b": "05-relativity-and-gravitation/general-relativity/tests-of-general-relativity", "name": "Proper-time which-path decoherence", "kind": "mechanism", "summary": "A clock in superposition at two heights records which-path proper time, so interferometric visibility drops; gravitational time dilation gives a universal decoherence for composite systems with internal dynamics.", "map": "V=|\\langle\\tau_1|\\tau_2\\rangle|,\\ \\Delta\\tau=g\\Delta h\\,t/c^2", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1668", "a": "04-quantum-physics/foundations-of-quantum-mechanics/measurement-problem-and-interpretations", "b": "05-relativity-and-gravitation/quantum-gravity/other-approaches-to-quantum-gravity", "name": "Gravitational objective collapse (Penrose-Diosi)", "kind": "mechanism", "summary": "Superpositions of distinct mass distributions are proposed to collapse at a rate set by the gravitational self-energy of their difference: a dynamical answer to the measurement problem, testable with massive superpositions.", "map": "\\tau\\approx\\hbar/E_\\Delta,\\ E_\\Delta\\sim Gm^2/R", "breaks": "", "confidence": "proposed", "strength": 2}
{"id": "C1669", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics", "b": "05-relativity-and-gravitation/black-holes/information-paradox", "name": "Black-hole evaporation as an open quantum system", "kind": "method transfer", "summary": "Treating hole plus radiation as a bipartite quantum system lets open-system and entropy tools (reduced density matrices, Renyi entropies, replica trick) diagnose unitarity; the Page curve is the radiation's entanglement entropy.", "map": "S_{\\rm rad}=-\\mathrm{Tr}\\rho_R\\ln\\rho_R,\\ \\rho_R=\\mathrm{Tr}_{BH}|\\Psi\\rangle\\langle\\Psi|", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1670", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/non-hermitian-physics", "b": "05-relativity-and-gravitation/gravitational-waves/gravitational-wave-theory-and-waveforms", "name": "Quasinormal modes as non-Hermitian spectra", "kind": "identity", "summary": "Outgoing boundary conditions make the black-hole perturbation operator non-self-adjoint; quasinormal modes are resonances whose pseudospectrum shows the spectral instability familiar from non-Hermitian physics.", "map": "\\omega_n\\in\\mathbb C;\\ \\sigma_\\epsilon(L)=\\{\\omega:\\|(L-\\omega)^{-1}\\|>1/\\epsilon\\}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1671", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling", "b": "05-relativity-and-gravitation/black-holes/information-paradox", "name": "Black holes as fastest scramblers", "kind": "mechanism", "summary": "Black holes scramble information in a time ~ (beta/2pi) ln S and saturate the Maldacena-Shenker-Stanford bound on the OTOC Lyapunov exponent; Hayden-Preskill shows information thrown in after the Page time re-emerges after one scrambling time.", "map": "\\lambda_L\\le2\\pi k_BT/\\hbar;\\ t_*\\sim\\frac{\\hbar\\beta}{2\\pi}\\ln S", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1672", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling", "b": "05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft", "name": "SYK model and near-AdS2 gravity", "kind": "duality", "summary": "The Sachdev-Ye-Kitaev model of N Majoranas with random all-to-all couplings is maximally chaotic, and its low-energy Schwarzian sector matches Jackiw-Teitelboim gravity in near-AdS2: a solvable bridge between quantum chaos and holography.", "map": "H=\\sum J_{ijkl}\\chi_i\\chi_j\\chi_k\\chi_l;\\ \\lambda_L\\to2\\pi T\\ (\\beta J\\gg1)", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1673", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-thermodynamics", "b": "05-relativity-and-gravitation/black-holes/black-hole-thermodynamics-and-hawking-radiation", "name": "Bekenstein bound from relative entropy", "kind": "method transfer", "summary": "Quantum-information thermodynamics (positivity of relative entropy) gives a precise statement and proof of the Bekenstein bound and underpins the generalized second law.", "map": "S(\\rho\\|\\sigma)\\ge0\\Rightarrow\\Delta S\\le\\Delta\\langle K\\rangle", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1674", "a": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "b": "05-relativity-and-gravitation/black-holes/black-hole-thermodynamics-and-hawking-radiation", "name": "Entanglement area law and black-hole entropy", "kind": "mechanism", "summary": "Tracing out field modes inside a surface gives an entanglement entropy proportional to its area with a cutoff-dependent coefficient, a candidate microscopic contribution to the Bekenstein-Hawking entropy.", "map": "S_{\\rm ent}\\approx cA/\\epsilon^2\\leftrightarrow S_{BH}=A/4\\ell_P^2", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1675", "a": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "b": "05-relativity-and-gravitation/black-holes/information-paradox", "name": "Page curve, monogamy and the firewall", "kind": "identity", "summary": "Page's typical-subsystem entropy gives the rise and fall of radiation entropy; monogamy of entanglement forbids late Hawking modes being maximally entangled with both early radiation and interior partners (the AMPS firewall).", "map": "\\langle S_A\\rangle\\approx\\ln m-\\frac{m}{2n}\\ (m\\le n);\\ S_{AB}+S_{BC}\\ge S_A+S_C", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1676", "a": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "b": "05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft", "name": "Ryu-Takayanagi: entanglement equals area", "kind": "duality", "summary": "Boundary entanglement entropy of a region equals the minimal bulk surface area in Planck units; entanglement builds connected spacetime, and MERA tensor networks give a discrete toy bulk.", "map": "S_A=\\mathrm{Area}(\\gamma_A)/4G_N\\hbar", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1677", "a": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "b": "05-relativity-and-gravitation/quantum-gravity/other-approaches-to-quantum-gravity", "name": "Gravity-mediated entanglement witness (BMV)", "kind": "identity", "summary": "LOCC cannot create entanglement, so if two masses in superposition become entangled through gravity alone, gravity cannot act as a classical channel; the proposed test is a direct application of entanglement monotonicity.", "map": "\\Delta\\phi=Gm^2\\Delta t/\\hbar d;\\ E(\\rho)\\ \\text{non-increasing under LOCC}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1678", "a": "04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity", "b": "05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft", "name": "Holographic complexity", "kind": "method transfer", "summary": "Quantum circuit complexity is conjectured to be dual to the growing volume or action of the black-hole interior (complexity = volume or action).", "map": "\\mathcal C=I_{\\rm WdW}/\\pi\\hbar", "breaks": "", "confidence": "proposed", "strength": 2}
{"id": "C1679", "a": "04-quantum-physics/quantum-information-and-computation/quantum-communication-and-cryptography", "b": "05-relativity-and-gravitation/black-holes/black-hole-imaging-and-astrophysical-black-holes", "name": "Quantum repeaters for VLBI baselines", "kind": "method transfer", "summary": "Distributing entanglement between telescopes would allow optical interferometry with arbitrarily long baselines without transporting photons, a possible extension of EHT-style imaging to optical wavelengths.", "map": "", "breaks": "", "confidence": "proposed", "strength": 1}
{"id": "C1680", "a": "04-quantum-physics/quantum-information-and-computation/quantum-error-correction-and-fault-tolerance", "b": "05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft", "name": "Holographic codes: bulk locality as QEC", "kind": "duality", "summary": "Bulk operators in AdS/CFT can be reconstructed on many boundary subregions, exactly as logical operators of an erasure-correcting code; perfect-tensor (HaPPY) codes reproduce RT and entanglement-wedge reconstruction.", "map": "\\mathcal H_{\\rm bulk}\\hookrightarrow\\mathcal H_{\\rm code}\\subset\\mathcal H_{\\rm CFT};\\ \\text{RT}\\leftrightarrow\\text{min-cut}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1681", "a": "04-quantum-physics/quantum-information-and-computation/superconducting-qubits", "b": "05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft", "name": "Wormhole teleportation on quantum processors", "kind": "method transfer", "summary": "Quantum processors have emulated SYK-like teleportation protocols interpreted as traversable wormholes; the 2022 superconducting-processor claim is contested because the learned Hamiltonian may not be holographic.", "map": "", "breaks": "", "confidence": "proposed", "strength": 1}
{"id": "C1682", "a": "04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin", "b": "05-relativity-and-gravitation/quantum-gravity/loop-quantum-gravity", "name": "SU(2) recoupling builds spin networks", "kind": "method transfer", "summary": "Loop quantum gravity labels spin-network edges by SU(2) irreps and nodes by intertwiners; the area spectrum is the SU(2) Casimir and spin-foam amplitudes use 6j symbols from angular-momentum recoupling.", "map": "A=8\\pi\\gamma\\ell_P^2\\sum_i\\sqrt{j_i(j_i+1)}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1683", "a": "04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin", "b": "05-relativity-and-gravitation/special-relativity/lorentz-transformations-and-spacetime", "name": "Spinors, Lorentz group and Thomas precession", "kind": "identity", "summary": "Spin-1/2 is a representation of SL(2,C), the double cover of the Lorentz group; Thomas precession (a Wigner rotation) supplies the factor 1/2 in atomic spin-orbit coupling, and the Dirac equation gives g=2 and fine structure.", "map": "H_{SO}=\\frac{g-1}{2m^2c^2}\\frac1r\\frac{dV}{dr}\\mathbf L\\cdot\\mathbf S", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1684", "a": "04-quantum-physics/quantum-mechanics-core/approximation-methods", "b": "05-relativity-and-gravitation/black-holes/black-hole-thermodynamics-and-hawking-radiation", "name": "Hawking radiation as WKB tunnelling", "kind": "method transfer", "summary": "The emission rate can be computed as a semiclassical tunnelling probability across the horizon; energy conservation gives small non-thermal corrections.", "map": "\\Gamma\\sim e^{-2\\mathrm{Im}S}=e^{-\\beta\\omega(1-\\omega/2M)}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1685", "a": "04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems", "b": "05-relativity-and-gravitation/gravitational-waves/gravitational-wave-theory-and-waveforms", "name": "Poschl-Teller and WKB models of ringdown", "kind": "method transfer", "summary": "Black-hole perturbations obey a Schrodinger-like Regge-Wheeler/Zerilli equation; replacing the barrier by an exactly solvable Poschl-Teller potential, or expanding it by WKB, gives the quasinormal ringdown frequencies.", "map": "\\psi''+[\\omega^2-V(r_*)]\\psi=0,\\ V\\approx V_0\\,\\mathrm{sech}^2\\alpha r_*", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1686", "a": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "b": "05-relativity-and-gravitation/general-relativity/einstein-field-equations", "name": "Berry connection vs Levi-Civita connection", "kind": "analogy", "summary": "The Berry phase is the holonomy of a U(1) connection on parameter space, as a vector's rotation after parallel transport is the holonomy of the Levi-Civita connection; both are connections with curvature on fibre bundles.", "map": "\\gamma=\\oint\\mathcal A\\cdot d\\mathbf R=\\iint\\Omega\\leftrightarrow\\delta V^\\mu=-\\tfrac12R^\\mu{}_{\\nu\\alpha\\beta}V^\\nu dA^{\\alpha\\beta}", "breaks": "Berry curvature is a non-dynamical abelian field on Hilbert-space parameters; spacetime curvature is a dynamical SO(3,1) connection fixed by Einstein's equations.", "confidence": "established", "strength": 2}
{"id": "C1687", "a": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "b": "05-relativity-and-gravitation/general-relativity/tests-of-general-relativity", "name": "Gravitational Aharonov-Bohm effect", "kind": "mechanism", "summary": "Atom interferometers measured a gravitational phase shift on wavepackets that feel no net gravitational force, the gravitational counterpart of the Aharonov-Bohm effect.", "map": "\\Delta\\phi=\\frac{m}{\\hbar}\\oint V\\,dt", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1688", "a": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "b": "05-relativity-and-gravitation/black-holes/black-hole-thermodynamics-and-hawking-radiation", "name": "Euclidean path integral gives the Hawking temperature", "kind": "method transfer", "summary": "Wick-rotating the black-hole metric and demanding regularity at the horizon forces periodic imaginary time, identical to the thermal path-integral period; the Euclidean action gives the partition function and entropy.", "map": "\\tau\\sim\\tau+\\beta,\\ \\beta=2\\pi/\\kappa;\\ Z=e^{-I_E}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1689", "a": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "b": "05-relativity-and-gravitation/quantum-gravity", "name": "No-boundary wavefunction of the universe", "kind": "method transfer", "summary": "Hartle and Hawking define the state of the universe as a Euclidean path integral over compact geometries, transplanting semiclassical and instanton machinery from QM to quantum cosmology.", "map": "\\Psi[h_{ij}]=\\int_{\\rm compact}\\mathcal Dg\\,e^{-I_E[g]/\\hbar}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1690", "a": "04-quantum-physics/quantum-mechanics-core/postulates-and-formalism", "b": "05-relativity-and-gravitation/quantum-gravity/loop-quantum-gravity", "name": "Problem of time and relational evolution", "kind": "mechanism", "summary": "Canonical quantum gravity imposes the Wheeler-DeWitt constraint H|Psi>=0, so there is no external time; the Page-Wootters mechanism recovers Schrodinger dynamics as correlations between a clock subsystem and the rest.", "map": "\\hat H|\\Psi\\rangle=0;\\ |\\psi(t)\\rangle\\propto\\langle t|_C|\\Psi\\rangle", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1691", "a": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "b": "05-relativity-and-gravitation/black-holes/schwarzschild-and-kerr-black-holes", "name": "Black-hole scattering and partial waves", "kind": "method transfer", "summary": "Wave scattering off Schwarzschild and Kerr holes uses partial-wave phase shifts, greybody factors and absorption cross sections from quantum scattering theory; rotating holes superradiantly amplify modes with omega < m Omega_H.", "map": "\\sigma_{\\rm abs}=\\frac{\\pi}{\\omega^2}\\sum_\\ell(2\\ell+1)|T_\\ell|^2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1692", "a": "04-quantum-physics/quantum-optics", "b": "05-relativity-and-gravitation/gravitational-waves/ground-based-detections", "name": "Standard quantum limit of interferometry", "kind": "shared object", "summary": "A GW interferometer is a quantum-optical measurement whose sensitivity is set by the trade-off between photon shot noise and radiation-pressure back-action, the standard quantum limit.", "map": "h_{\\rm SQL}(f)=\\sqrt{8\\hbar/m(2\\pi f)^2L^2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1693", "a": "04-quantum-physics/quantum-optics/cavity-and-circuit-qed", "b": "05-relativity-and-gravitation/quantum-gravity/qft-in-curved-spacetime", "name": "Dynamical Casimir effect in circuit QED", "kind": "mechanism", "summary": "Modulating a superconducting resonator's boundary condition with a SQUID at GHz rates creates photon pairs from vacuum, the same parametric particle creation as moving mirrors and cosmological particle production.", "map": "\\omega_{\\rm drive}=2\\omega_{\\rm cav}\\Rightarrow\\text{photon pairs}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1694", "a": "04-quantum-physics/quantum-optics/cavity-optomechanics", "b": "05-relativity-and-gravitation/gravitational-waves/ground-based-detections", "name": "LIGO mirrors as optomechanical systems", "kind": "shared object", "summary": "Interferometer test masses are radiation-pressure-coupled oscillators: optical springs, parametric instabilities, ponderomotive squeezing and feedback cooling of 10 kg mirrors toward the motional ground state are cavity optomechanics at kg scale.", "map": "H_{\\rm int}=-\\hbar g_0a^\\dagger a(b+b^\\dagger)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1695", "a": "04-quantum-physics/quantum-optics/cavity-optomechanics", "b": "05-relativity-and-gravitation/quantum-gravity/other-approaches-to-quantum-gravity", "name": "Optomechanical probes of Planck-scale physics", "kind": "method transfer", "summary": "Quantum-optical control of massive oscillators can bound deformed canonical commutators (minimal-length models) and test gravity-related collapse in macroscopic superpositions.", "map": "[x,p]=i\\hbar\\left(1+\\beta_0p^2/(M_Pc)^2\\right)", "breaks": "", "confidence": "proposed", "strength": 2}
{"id": "C1696", "a": "04-quantum-physics/quantum-optics/quantized-light-and-photon-statistics", "b": "05-relativity-and-gravitation/quantum-gravity/qft-in-curved-spacetime", "name": "Unruh-DeWitt detector is a two-level atom", "kind": "identity", "summary": "The detector used to define Unruh and Hawking radiation is a two-level system coupled to a quantum field, the atom-field model of quantum optics; accelerated detectors see thermal photon statistics.", "map": "H_I=\\lambda\\mu(\\tau)\\phi(x(\\tau));\\ T_U=\\hbar a/2\\pi ck_B", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1697", "a": "04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology", "b": "05-relativity-and-gravitation/gravitational-waves", "name": "Quantum metrology for GW astronomy", "kind": "method transfer", "summary": "Gravitational-wave science drives squeezing at audio frequencies and filter-cavity development; the detectors are the most sensitive deployed quantum-enhanced instruments.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1698", "a": "04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology", "b": "05-relativity-and-gravitation/gravitational-waves/ground-based-detections", "name": "Squeezed-light injection in GW detectors", "kind": "method transfer", "summary": "Injecting squeezed vacuum into the dark port lowers shot noise below the standard quantum limit; frequency-dependent squeezing also cuts radiation-pressure noise. Used in LIGO and Virgo observing runs since 2019.", "map": "S_{\\rm shot}\\to e^{-2r}S_{\\rm shot}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1699", "a": "04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology", "b": "05-relativity-and-gravitation/quantum-gravity/qft-in-curved-spacetime", "name": "Unruh/Hawking vacuum as two-mode squeezing", "kind": "identity", "summary": "The Bogoliubov transformation between Minkowski and Rindler (or in and out) modes is exactly a two-mode squeezing operator; the Minkowski vacuum is a two-mode squeezed state across the horizon, thermal on either side.", "map": "|0_M\\rangle=\\prod_k\\frac{1}{\\cosh r_k}\\sum_n\\tanh^nr_k|n\\rangle_L|n\\rangle_R,\\ \\tanh r=e^{-\\pi\\omega c/a}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1700", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "b": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "name": "Clocks search for ultralight dark matter", "kind": "method transfer", "summary": "Ultralight scalar dark matter would make fundamental constants oscillate; comparing clocks with different sensitivity to alpha and m_e/m_p detects such oscillations at frequencies set by the DM mass.", "map": "\\frac{\\delta\\alpha}{\\alpha}\\propto\\frac{\\phi_0}{\\Lambda}\\cos(m_\\phi c^2t/\\hbar);\\ \\frac{\\delta(\\nu_1/\\nu_2)}{\\nu_1/\\nu_2}=(K_1-K_2)\\frac{\\delta\\alpha}{\\alpha}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1701", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "name": "Isotope-shift King plots probe new bosons", "kind": "method transfer", "summary": "A new light boson coupling electrons to neutrons would bend the King plot of isotope shifts; precision ion spectroscopy constrains such Yukawa forces at keV-MeV masses.", "map": "\\delta\\nu_i^{AA'}=K_i\\mu_{AA'}+F_i\\delta\\langle r^2\\rangle+\\alpha_{NP}X_i\\gamma_{AA'}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1702", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2", "name": "Electron g-2 and alpha test QED", "kind": "method transfer", "summary": "A single-electron Penning-trap measurement of g/2 and atom-recoil measurements of alpha (Cs, Rb) test QED at the 1e-13 level; their mutual tension is part of the lepton g-2 anomaly landscape.", "map": "a_e=\\frac{\\alpha}{2\\pi}-0.328\\left(\\frac\\alpha\\pi\\right)^2+\\dots;\\ \\alpha^2=\\frac{2R_\\infty}{c}\\frac{h}{m_e}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1703", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "name": "Lamb shift and the birth of renormalization", "kind": "historical", "summary": "The 1947 Lamb shift measurement and Bethe's mass-renormalized calculation launched renormalized QED; hydrogen spectroscopy remains a precision test of bound-state QED.", "map": "\\Delta E_{2S}\\approx\\frac{4\\alpha^5m_ec^2}{3\\pi n^3}\\ln\\frac{1}{\\alpha}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1704", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "06-particle-physics/standard-model/electroweak-theory", "name": "Atomic parity violation measures the weak charge", "kind": "method transfer", "summary": "Z exchange between electrons and the nucleus mixes S and P states; the Cs 6S-7S parity-violating amplitude gives the nuclear weak charge and sin^2 theta_W at low momentum transfer, complementary to colliders.", "map": "Q_W=Z(1-4\\sin^2\\theta_W)-N", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1705", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "b": "06-particle-physics/quantum-field-theory/lattice-field-theory", "name": "Analog quantum simulation of lattice gauge theories", "kind": "method transfer", "summary": "Cold atoms and Rydberg arrays implement Hamiltonian lattice gauge theories with Gauss's law enforced by energy penalties or constraints, accessing real-time dynamics and finite density where Euclidean Monte Carlo has a sign problem.", "map": "H=-J\\sum(\\psi_i^\\dagger U_{i,i+1}\\psi_{i+1}+\\text{h.c.})+\\frac{g^2}{2}\\sum E_i^2;\\ G_i|\\psi\\rangle=0", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1706", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "b": "06-particle-physics/standard-model/higgs-boson", "name": "Higgs amplitude mode in superfluids", "kind": "analogy", "summary": "Near the superfluid-Mott transition, optical-lattice bosons have a gapped amplitude ('Higgs') mode of the order parameter, observed by lattice modulation spectroscopy.", "map": "V(\\psi)=-\\mu|\\psi|^2+\\tfrac u2|\\psi|^4;\\ \\Delta_H\\to0\\ \\text{at the QCP}", "breaks": "No gauge field, so no Higgs mechanism; the amplitude mode can decay into Goldstone pairs and is only well defined near Lorentz-invariant criticality.", "confidence": "established", "strength": 2}
{"id": "C1707", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/ultracold-molecules", "b": "06-particle-physics/standard-model/cp-violation", "name": "Electron EDM in polar molecules", "kind": "method transfer", "summary": "Polar molecules (ThO, HfF+) amplify a lab field into internal effective fields of 10-100 GV/cm; spin-precession measurements bound the electron EDM below 1e-29 e cm, probing CP-violating physics at multi-TeV scales.", "map": "H=-d_e\\,\\mathcal E_{\\rm eff}\\,\\boldsymbol\\sigma\\cdot\\hat n;\\ d_e\\sim e\\,m_e\\,\\frac{\\alpha}{\\pi}\\frac{\\sin\\phi_{CP}}{\\Lambda^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1708", "a": "04-quantum-physics/foundations-of-quantum-mechanics/bell-nonlocality", "b": "06-particle-physics/neutrino-physics/neutrino-oscillations", "name": "Leggett-Garg violation in neutrino oscillations", "kind": "method transfer", "summary": "Temporal (Leggett-Garg) inequalities, the time-domain analogue of Bell tests, are violated by MINOS oscillation data, showing neutrino flavour evolution is incompatible with macrorealism over 735 km.", "map": "K_3=C_{12}+C_{23}-C_{13}\\le1", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1709", "a": "04-quantum-physics/foundations-of-quantum-mechanics/bell-nonlocality", "b": "06-particle-physics/standard-model/flavor-physics-and-ckm", "name": "Entangled neutral mesons and Bell tests", "kind": "shared object", "summary": "Pairs of neutral K or B mesons from phi or Upsilon(4S) decays are produced in flavour-entangled EPR states, used to time-tag CP and flavour measurements and to test Bell-type inequalities with decaying systems.", "map": "|\\psi\\rangle=\\tfrac{1}{\\sqrt2}(|B^0\\bar B^0\\rangle-|\\bar B^0B^0\\rangle)", "breaks": "Decay and lack of free measurement-setting choice prevent loophole-free Bell tests.", "confidence": "current research", "strength": 2}
{"id": "C1710", "a": "04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical", "b": "06-particle-physics/neutrino-physics/neutrino-oscillations", "name": "Wave-packet decoherence of neutrino oscillations", "kind": "mechanism", "summary": "Mass eigenstates in a neutrino wave packet separate over a coherence length, damping oscillations exactly as which-path information kills interference; open-system (Lindblad) models also bound exotic decoherence from new physics.", "map": "L_{\\rm coh}\\sim\\frac{4\\sqrt2E^2}{|\\Delta m^2|}\\sigma_x;\\ P\\to\\tfrac12\\sin^22\\theta", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1711", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/non-hermitian-physics", "b": "06-particle-physics/standard-model/cp-violation", "name": "Kaon mixing is a non-Hermitian two-level system", "kind": "identity", "summary": "The Weisskopf-Wigner effective Hamiltonian of neutral kaons (or B mesons) is the non-Hermitian matrix M - i Gamma/2; its non-orthogonal eigenstates K_S, K_L and their overlap encode CP violation.", "map": "H_{\\rm eff}=M-\\tfrac i2\\Gamma;\\ \\langle K_S|K_L\\rangle\\approx2\\mathrm{Re}\\,\\epsilon", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1712", "a": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "b": "06-particle-physics/collider-and-experimental-particle-physics/hadron-colliders-and-the-lhc", "name": "Entanglement of top-quark pairs at the LHC", "kind": "method transfer", "summary": "Top-antitop spin correlations reconstructed from decay leptons are a two-qubit density matrix; ATLAS and CMS observed entanglement near threshold using quantum-information witnesses.", "map": "D=-3\\langle\\cos\\varphi\\rangle;\\ D<-1/3\\Rightarrow\\text{entangled}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1713", "a": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "b": "06-particle-physics/quantum-field-theory/conformal-field-theory", "name": "Entanglement entropy measures the central charge", "kind": "identity", "summary": "In a 1+1D CFT the entanglement entropy of an interval grows logarithmically with a coefficient fixed by the central charge, so entanglement diagnoses criticality and universality classes.", "map": "S_A=\\frac c3\\ln\\frac{\\ell}{a}+c'", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1714", "a": "04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity", "b": "06-particle-physics/collider-and-experimental-particle-physics/machine-learning-in-hep", "name": "Quantum machine learning for collider data", "kind": "method transfer", "summary": "Variational quantum classifiers and kernels have been tried on jet tagging and event classification; no advantage over classical deep learning has been demonstrated.", "map": "", "breaks": "", "confidence": "proposed", "strength": 1}
{"id": "C1715", "a": "04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity", "b": "06-particle-physics/collider-and-experimental-particle-physics/monte-carlo-event-generators", "name": "Quantum algorithms for parton showers", "kind": "method transfer", "summary": "Quantum circuits can simulate parton showers including quantum interference between emission histories that classical Markov showers drop.", "map": "", "breaks": "", "confidence": "proposed", "strength": 1}
{"id": "C1716", "a": "04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity", "b": "06-particle-physics/quantum-field-theory/lattice-field-theory", "name": "Digital quantum algorithms for QFT", "kind": "method transfer", "summary": "Hamiltonian-simulation algorithms compute scattering in scalar and gauge field theories in polynomial time, a route around the sign problem of lattice QCD at finite density and real time.", "map": "e^{-iHt}\\approx\\left(\\prod_je^{-iH_jt/n}\\right)^n", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1717", "a": "04-quantum-physics/quantum-information-and-computation/superconducting-qubits", "b": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "name": "Qubit photon counting for dark-photon searches", "kind": "method transfer", "summary": "A transmon dispersively coupled to a cavity counts photons by repeated quantum non-demolition parity measurements, evading the standard quantum limit of linear amplifiers in hidden-photon and axion searches.", "map": "\\chi\\sigma_za^\\dagger a\\ \\Rightarrow\\ \\text{QND number readout}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1718", "a": "04-quantum-physics/quantum-information-and-computation/trapped-ion-and-neutral-atom-qubits", "b": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "name": "Trapped-ion simulation of the Schwinger model", "kind": "method transfer", "summary": "A few trapped-ion qubits simulated real-time pair creation in 1+1D QED after eliminating the gauge field; circuit-QED and tensor-network studies extend this to meson scattering.", "map": "H=w\\sum(\\sigma_n^+\\sigma_{n+1}^-+\\text{h.c.})+\\frac m2\\sum(-1)^n\\sigma_n^z+J\\sum L_n^2", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1719", "a": "04-quantum-physics/quantum-mechanics-core", "b": "06-particle-physics/quantum-field-theory", "name": "Second quantization: QM of many particles is QFT", "kind": "identity", "summary": "Non-relativistic many-body quantum mechanics in Fock space is a free or interacting quantum field theory; relativistic QFT adds Lorentz invariance, antiparticles and particle number non-conservation.", "map": "\\hat\\psi(\\mathbf x)=\\sum_k a_k\\phi_k(\\mathbf x),\\ [a_k,a_{k'}^\\dagger]_\\mp=\\delta_{kk'}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1720", "a": "04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin", "b": "06-particle-physics/neutrino-physics/neutrino-oscillations", "name": "Neutrino flavour as a precessing pseudo-spin", "kind": "identity", "summary": "Two-flavour oscillation is spin-1/2 precession in an effective magnetic field; the oscillation formula is the Rabi formula, and collective oscillations in dense neutrino gases map onto interacting spin models.", "map": "P_{\\alpha\\beta}=\\sin^22\\theta\\sin^2\\frac{\\Delta m^2L}{4E}\\leftrightarrow P=\\frac{\\Omega^2}{\\Omega'^2}\\sin^2\\frac{\\Omega't}{2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1721", "a": "04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin", "b": "06-particle-physics/standard-model/hadron-spectroscopy-and-exotics", "name": "Isospin and flavour multiplets via SU(2) recoupling", "kind": "method transfer", "summary": "Clebsch-Gordan coefficients and the Wigner-Eckart theorem developed for angular momentum organize isospin and flavour multiplets, decay branching ratios and helicity amplitudes of hadrons.", "map": "\\frac{\\Gamma(\\Delta^+\\to p\\pi^0)}{\\Gamma(\\Delta^+\\to n\\pi^+)}=\\frac{|\\langle\\tfrac32\\tfrac12|1\\,0;\\tfrac12\\tfrac12\\rangle|^2}{|\\langle\\tfrac32\\tfrac12|1\\,1;\\tfrac12\\,{-\\tfrac12}\\rangle|^2}=2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1722", "a": "04-quantum-physics/quantum-mechanics-core/approximation-methods", "b": "06-particle-physics/neutrino-physics/neutrino-oscillations", "name": "MSW conversion as an adiabatic level crossing", "kind": "identity", "summary": "Resonant flavour conversion in the Sun is an avoided crossing of matter-dressed mass eigenstates; adiabatic following gives near-complete conversion and the non-adiabatic hopping probability is the Landau-Zener formula.", "map": "P_{\\rm hop}=\\exp\\left(-\\frac{\\pi}{2}\\frac{\\Delta m^2\\sin^22\\theta}{2E\\cos2\\theta\\,|d\\ln n_e/dr|}\\right)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1723", "a": "04-quantum-physics/quantum-mechanics-core/approximation-methods", "b": "06-particle-physics/quantum-field-theory/effective-field-theory", "name": "Schrieffer-Wolff elimination as integrating out", "kind": "identity", "summary": "Adiabatic elimination of high-energy states by second-order perturbation theory (Schrieffer-Wolff) gives effective Hamiltonians, the same logic as integrating out heavy fields; Fermi's four-fermion coupling is W exchange at second order.", "map": "H_{\\rm eff}=PVP+\\sum\\frac{PV|m\\rangle\\langle m|VP}{E-E_m}\\leftrightarrow\\frac{G_F}{\\sqrt2}=\\frac{g^2}{8m_W^2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1724", "a": "04-quantum-physics/quantum-mechanics-core/approximation-methods", "b": "06-particle-physics/quantum-field-theory/feynman-diagrams-and-scattering-amplitudes", "name": "Golden rule and decay widths", "kind": "identity", "summary": "Fermi's golden rule is the non-relativistic form of the relativistic decay-rate and cross-section formulas built from Feynman amplitudes and Lorentz-invariant phase space.", "map": "\\Gamma=\\frac{2\\pi}{\\hbar}|V_{fi}|^2\\rho(E_f)\\leftrightarrow\\Gamma=\\frac{1}{2m}\\int|\\mathcal M|^2d\\Phi_n", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1725", "a": "04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems", "b": "06-particle-physics/beyond-the-standard-model/supersymmetry", "name": "Supersymmetric quantum mechanics", "kind": "historical", "summary": "Witten introduced SUSY QM as a toy model of supersymmetry breaking (Witten index); it became a tool for exactly solvable potentials through shape invariance and partner Hamiltonians.", "map": "H_\\pm=-\\frac{\\hbar^2}{2m}\\frac{d^2}{dx^2}+W^2\\pm\\frac{\\hbar}{\\sqrt{2m}}W'", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1726", "a": "04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems", "b": "06-particle-physics/standard-model/hadron-spectroscopy-and-exotics", "name": "Quarkonium as hydrogen of QCD", "kind": "analogy", "summary": "Charmonium and bottomonium spectra follow from a Schrodinger equation with a Coulomb-plus-linear (Cornell) potential, organized like hydrogen and positronium levels with fine and hyperfine splittings.", "map": "V(r)=-\\frac{4}{3}\\frac{\\alpha_s}{r}+\\sigma r", "breaks": "Confinement (linear term) has no atomic analogue; relativistic corrections and coupled open-flavour channels matter above threshold.", "confidence": "established", "strength": 2}
{"id": "C1727", "a": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "b": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "name": "Theta vacua as Bloch states; WZ terms as Berry phases", "kind": "identity", "summary": "Large gauge transformations make the Yang-Mills vacuum periodic, and theta plays the role of Bloch quasi-momentum in a periodic potential; Wess-Zumino-Witten terms are Berry phases of the low-energy fields.", "map": "|\\theta\\rangle=\\sum_ne^{in\\theta}|n\\rangle\\leftrightarrow\\psi_k(x)=\\sum_ne^{ikna}\\phi(x-na)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1728", "a": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "b": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "name": "Wilson loops are non-abelian holonomies", "kind": "identity", "summary": "The Aharonov-Bohm phase is a U(1) holonomy; Yang-Mills Wilson loops are its non-abelian generalization, and degenerate adiabatic transport produces the same Wilczek-Zee non-abelian connection.", "map": "W(C)=\\mathrm{Tr}\\,\\mathcal P\\exp\\left(ig\\oint_CA\\right);\\ \\Delta\\phi_{AB}=q\\Phi/\\hbar", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1729", "a": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "b": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "name": "Instantons from double wells to QCD", "kind": "method transfer", "summary": "Euclidean instantons that compute tunnelling splitting in a double well become Yang-Mills instantons, which break U(1)_A through the anomaly and mix the theta vacua.", "map": "\\Delta E\\propto e^{-S_E/\\hbar}\\to e^{-8\\pi^2/g^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1730", "a": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "b": "06-particle-physics/quantum-field-theory/canonical-and-path-integral-quantization", "name": "Feynman path integral from particles to fields", "kind": "identity", "summary": "The QFT generating functional is the particle path integral with paths replaced by field configurations; stationary phase gives the classical field equations and Gaussian integrals give propagators and Wick's theorem.", "map": "K=\\int\\mathcal Dx\\,e^{iS[x]/\\hbar}\\to Z[J]=\\int\\mathcal D\\phi\\,e^{i(S[\\phi]+\\int J\\phi)/\\hbar}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1731", "a": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "b": "06-particle-physics/quantum-field-theory/feynman-diagrams-and-scattering-amplitudes", "name": "Born series as tree-level perturbation theory", "kind": "identity", "summary": "The Lippmann-Schwinger Born series is the non-relativistic limit of the Feynman-diagram expansion: first Born approximation equals tree-level one-boson exchange (Yukawa/Coulomb), and the optical theorem is S-matrix unitarity.", "map": "f_{\\rm Born}=-\\frac{m}{2\\pi\\hbar^2}\\tilde V(\\mathbf q)\\leftrightarrow\\mathcal M\\propto\\frac{g^2}{q^2+m^2};\\ \\sigma_{\\rm tot}=\\frac{4\\pi}{k}\\mathrm{Im}f(0)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1732", "a": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "b": "06-particle-physics/standard-model/hadron-spectroscopy-and-exotics", "name": "Near-threshold states and universality", "kind": "mechanism", "summary": "Hadrons near a two-body threshold (deuteron, X(3872)) are governed by a large scattering length, the same universal physics as Feshbach-tuned cold atoms, including Efimov-type three-body effects.", "map": "E_B\\approx\\frac{\\hbar^2}{2\\mu a^2},\\ \\langle r^2\\rangle^{1/2}\\approx a/\\sqrt2\\ (a\\gg r_0)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1733", "a": "04-quantum-physics/quantum-optics/quantized-light-and-photon-statistics", "b": "06-particle-physics/quantum-field-theory/canonical-and-path-integral-quantization", "name": "Quantized EM field as free QFT", "kind": "identity", "summary": "Quantum optics' mode expansion of the field, Fock and coherent states are the canonical quantization of free Maxwell theory; Glauber coherent states are the quantum states closest to classical fields.", "map": "\\hat{\\mathbf A}=\\sum_{k\\lambda}\\sqrt{\\frac{\\hbar}{2\\epsilon_0\\omega_kV}}(a_{k\\lambda}\\boldsymbol\\epsilon e^{i\\mathbf k\\cdot\\mathbf x}+\\text{h.c.})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1734", "a": "04-quantum-physics/quantum-optics/single-photon-sources-and-detectors", "b": "06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers", "name": "Single-photon detectors in particle detectors", "kind": "shared object", "summary": "Calorimeters, Cherenkov and scintillator systems read out light with single-photon-sensitive devices (PMTs, SiPMs, SPAD arrays); quantum-optics detector metrics such as efficiency, dark counts and timing jitter set detector performance.", "map": "\\eta_{\\rm sys}=\\eta_{\\rm coupling}\\eta_{\\rm det};\\ \\sigma_t\\ \\text{(jitter)}", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1735", "a": "04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology", "b": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "name": "Squeezed-state receivers for axion haloscopes", "kind": "method transfer", "summary": "Haloscopes convert axions to microwave photons in a resonant cavity; HAYSTAC injected squeezed vacuum to beat the quantum limit on scan rate, a direct import of quantum metrology.", "map": "P_{a\\to\\gamma}\\propto g_{a\\gamma\\gamma}^2\\frac{\\rho_a}{m_a}B^2VC\\,Q;\\ \\text{scan rate}\\propto1/(\\text{noise})^2", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1736", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "b": "07-nuclear-physics/nuclear-structure", "name": "Thorium-229 nuclear clock", "kind": "shared object", "summary": "The 8.4 eV isomer of Th-229 has been laser-excited and frequency-referenced to a Sr clock, opening a nuclear optical clock highly sensitive to variations of alpha and the strong-interaction scale.", "map": "E_{\\rm iso}\\approx8.36\\ \\mathrm{eV};\\ \\frac{\\delta\\nu}{\\nu}\\approx K\\frac{\\delta\\alpha}{\\alpha},\\ |K|\\gg1", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1737", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "07-nuclear-physics/hadron-and-nucleon-structure/nucleon-spin-and-form-factors", "name": "Proton radius from hydrogen and muonic hydrogen", "kind": "method transfer", "summary": "The finite proton size shifts S levels; muonic-hydrogen Lamb-shift spectroscopy gave r_p = 0.84 fm, 4% below earlier e-p values, and newer hydrogen spectroscopy largely agrees, resolving most of the proton-radius puzzle.", "map": "\\Delta E_{\\rm fs}=\\frac{2}{3n^3}\\frac{(Z\\alpha)^4m_r^3c^4}{\\hbar^2c^2}\\langle r_p^2\\rangle\\,\\delta_{\\ell0}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1738", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay", "name": "Multipole selection rules for atomic and nuclear photons", "kind": "method transfer", "summary": "Gamma transitions in nuclei obey the same multipole selection rules and Wigner-Eckart structure as atomic E1/M1/E2 lines; Weisskopf estimates and conversion electrons parallel atomic radiative and Auger channels.", "map": "|J_i-J_f|\\le L\\le J_i+J_f;\\ \\pi_i\\pi_f=(-1)^L\\ (EL)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1739", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "07-nuclear-physics/nuclear-structure/exotic-nuclei-and-drip-lines", "name": "Laser spectroscopy of exotic-nucleus radii and moments", "kind": "method transfer", "summary": "Isotope shifts and hyperfine structure measured by collinear laser spectroscopy give charge radii, spins and moments of short-lived nuclei, revealing halos and shell evolution far from stability.", "map": "\\delta\\nu^{AA'}=K\\frac{m_{A'}-m_A}{m_Am_{A'}}+F\\,\\delta\\langle r^2\\rangle^{AA'}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1740", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "07-nuclear-physics/nuclear-structure/nuclear-forces-and-chiral-eft", "name": "Nuclear anapole moments from atomic parity violation", "kind": "method transfer", "summary": "The nuclear-spin-dependent part of Cs parity violation revealed the nuclear anapole moment, a probe of the parity-violating nucleon-nucleon (weak meson-exchange) interaction.", "map": "H_{\\rm PV}\\propto\\kappa_a\\,\\boldsymbol\\alpha\\cdot\\mathbf I\\,\\rho(r)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1741", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "07-nuclear-physics/nuclear-structure/superheavy-elements", "name": "Laser spectroscopy of superheavy atoms", "kind": "method transfer", "summary": "Atom-at-a-time resonance ionization spectroscopy of nobelium measures level energies where relativistic effects reshape atomic structure, testing relativistic many-body theory and giving nuclear moments.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}