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

### Optical lattices and quantum simulation · `knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation`

**Scope.** Standing-wave lattices, band structure and Wannier functions, Bose–Hubbard superfluid–Mott transition, Fermi–Hubbard antiferromagnetism, single-site imaging, synthetic gauge fields, Rydberg-atom arrays as spin simulators, many-body localization experiments.

**Core ideas.**
- Deep lattices map onto Hubbard models with tunnelling $J$ and on-site interaction $U$ controlled by laser intensity and Feshbach fields.
- Quantum gas microscopes resolve individual atoms, giving direct access to correlations.
- Analog simulators address problems (doped Hubbard, real-time dynamics) where classical computation struggles.

**Key equations.**
$$H_{\text{BH}}=-J\sum_{\langle ij\rangle}b_i^\dagger b_j+\frac U2\sum_in_i(n_i-1)-\mu\sum_in_i,\qquad (U/J)_c\approx29\ (3\text{D},\ n=1)$$

**See also.** [Hubbard model and Mott physics](knowledge/08-condensed-matter/strongly-correlated-electrons/hubbard-model-and-mott-physics/README.md) · [Thermalization and ETH](knowledge/04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth/README.md)

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

# Packet 04-2 (100 records)

{"id": "C0983", "a": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "b": "04-quantum-physics/quantum-optics/quantized-light-and-photon-statistics", "name": "Cavity and waveguide modes become photon modes", "kind": "identity", "summary": "To quantize the field, expand it in the classical normal modes of the cavity or waveguide (Helmholtz solutions obeying the boundary conditions) and promote each mode amplitude to a harmonic-oscillator operator. Mode shapes, mode volumes and dispersion carry over unchanged.", "map": "\\hat{\\mathbf E}=\\sum_k i\\sqrt{\\hbar\\omega_k/2\\epsilon_0}\\,\\mathbf u_k\\hat a_ke^{-i\\omega_kt}+\\text{h.c.},\\ (\\nabla^2+\\omega_k^2/c^2)\\mathbf u_k=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0984", "a": "02-electromagnetism-and-optics/electrodynamics/maxwells-equations", "b": "04-quantum-physics/quantum-optics/cavity-optomechanics", "name": "Field momentum and radiation pressure in optomechanics", "kind": "mechanism", "summary": "The momentum carried by electromagnetic fields (Poynting vector, Maxwell stress tensor) pushes on a reflector with radiation pressure 2P/c. In a cavity this force scales with the intracavity photon number, which gives the optomechanical coupling used to cool, squeeze and entangle mechanical motion.", "map": "\\mathbf g=\\epsilon_0\\mathbf E\\times\\mathbf B,\\ F=\\frac{2P}{c}\\to\\hat F=\\hbar G\\hat a^\\dagger\\hat a,\\ G=\\frac{\\omega_c}{L},\\ g_0=Gx_{\\rm zpf}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0985", "a": "02-electromagnetism-and-optics/electrodynamics/potentials-and-gauge-invariance", "b": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "name": "Aharonov–Bohm phase as holonomy of the potential", "kind": "identity", "summary": "The vector potential is a U(1) connection: a charge that encircles a flux picks up the phase q∮A·dl/ħ even where B=0. Berry's phase is the same holonomy, taken for a connection on parameter space.", "map": "\\varphi_{AB}=\\frac{q}{\\hbar}\\oint\\mathbf A\\cdot d\\mathbf l=\\frac{q\\Phi}{\\hbar}\\ \\leftrightarrow\\ \\gamma_B=\\oint\\mathcal A\\cdot d\\mathbf R,\\ \\mathcal A=i\\langle n|\\nabla_R n\\rangle", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0986", "a": "02-electromagnetism-and-optics/electrodynamics/relativistic-electrodynamics", "b": "04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin", "name": "Spin–orbit coupling from field transformations", "kind": "mechanism", "summary": "An electron moving through an atom's electric field sees a magnetic field B'=−v×E/c² in its rest frame, which couples to its spin. Relativistic Thomas precession halves the naive result, giving the fine-structure term that the Dirac equation yields directly.", "map": "\\mathbf B'\\approx-\\frac{\\mathbf v\\times\\mathbf E}{c^2},\\ \\ H_{SO}=\\frac{1}{2m^2c^2}\\frac{1}{r}\\frac{dV}{dr}\\,\\mathbf L\\cdot\\mathbf S\\ (g=2,\\ \\text{Thomas }\\tfrac12)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0987", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/electrostatics-and-boundary-value-problems", "b": "04-quantum-physics/quantum-information-and-computation/trapped-ion-and-neutral-atom-qubits", "name": "Earnshaw's theorem and the RF Paul trap", "kind": "mechanism", "summary": "Laplace's equation rules out a static 3D potential minimum for a charge (Earnshaw's theorem). Ion traps therefore use an oscillating quadrupole whose time-averaged ponderomotive pseudopotential confines the ion, and designing the electrodes is an electrostatic boundary-value problem.", "map": "\\Phi=\\frac{U+V\\cos\\Omega t}{2r_0^2}(x^2+y^2-2z^2),\\ \\nabla^2\\Phi=0;\\ \\Psi_{\\rm pseudo}=\\frac{q^2|\\nabla\\Phi_{\\rm RF}|^2}{4m\\Omega^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0988", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/fields-in-matter", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "name": "Lorentz oscillator and quantum oscillator strengths", "kind": "historical", "summary": "The classical Lorentz model of a bound electron gives the dielectric function and Rayleigh's ω^4 law. Quantum mechanics keeps its form, placing resonances at transition frequencies weighted by oscillator strengths that obey the Thomas–Reiche–Kuhn sum rule. Kramers–Heisenberg dispersion theory led directly to Heisenberg's matrix mechanics.", "map": "\\alpha(\\omega)=\\frac{e^2}{m}\\sum_n\\frac{f_{n0}}{\\omega_{n0}^2-\\omega^2-i\\gamma_n\\omega},\\ \\sum_nf_{n0}=Z,\\ \\epsilon=1+N\\alpha/\\epsilon_0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0989", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/multipole-expansions", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "name": "Multipole order sets atomic selection rules", "kind": "mechanism", "summary": "Expanding the atom–field coupling in multipoles gives E1, M1, E2… transitions. Their angular-momentum and parity selection rules follow from each multipole's spherical-tensor rank, and each higher order is suppressed by about (ka)^2. The resulting narrow 'forbidden' lines serve as clock transitions.", "map": "E\\ell:\\ |\\Delta J|\\le\\ell,\\ \\pi_f\\pi_i=(-1)^\\ell;\\ \\ M\\ell:\\ \\pi_f\\pi_i=(-1)^{\\ell+1};\\ \\ \\Gamma_{E2}/\\Gamma_{E1}\\sim(ka_0)^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0990", "a": "02-electromagnetism-and-optics/photonics-and-lasers", "b": "04-quantum-physics/atomic-molecular-and-optical-physics", "name": "Lasers as the enabling toolkit of AMO physics", "kind": "method transfer", "summary": "Narrow-linewidth, tunable, stabilized lasers made laser cooling, optical trapping, precision spectroscopy and coherent control of atoms possible. In return, atomic references stabilize laser frequencies.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0991", "a": "02-electromagnetism-and-optics/photonics-and-lasers", "b": "04-quantum-physics/quantum-optics", "name": "Photonic devices as quantum-optical hardware", "kind": "shared object", "summary": "The laser is itself a quantum-optical system: spontaneous-emission noise sets its Schawlow–Townes linewidth, and above threshold it emits near-coherent light. Photonic components (nonlinear crystals, waveguides, cavities) are the building blocks of quantum light sources and circuits.", "map": "\\Delta\\nu_{\\rm laser}\\approx\\frac{\\pi h\\nu(\\Delta\\nu_c)^2}{P_{\\rm out}}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0992", "a": "02-electromagnetism-and-optics/photonics-and-lasers/integrated-and-fiber-photonics", "b": "04-quantum-physics/quantum-information-and-computation/photonic-and-spin-qubits", "name": "Integrated linear optics as photonic quantum processors", "kind": "method transfer", "summary": "Classical integrated-photonics parts (directional couplers, thermo-optic phase shifters, Mach–Zehnder meshes that realize any unitary) become photonic qubit gates. They underpin linear-optical (KLM) and fusion-based architectures and boson-sampling machines.", "map": "\\hat a^\\dagger_{{\\rm out},i}=\\sum_jU_{ij}\\hat a^\\dagger_{{\\rm in},j},\\ U\\in U(N)\\ \\text{from }N(N-1)/2\\ \\text{MZIs}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0993", "a": "02-electromagnetism-and-optics/photonics-and-lasers/integrated-and-fiber-photonics", "b": "04-quantum-physics/quantum-information-and-computation/quantum-communication-and-cryptography", "name": "Telecom fibre and photonic chips for QKD", "kind": "method transfer", "summary": "Quantum key distribution and entanglement distribution run on low-loss 1550 nm telecom fibre with integrated transmitters and receivers. Fibre transmission falls exponentially with distance, which caps repeaterless key rates and motivates quantum repeaters.", "map": "\\eta=10^{-\\alpha L/10},\\ \\alpha\\approx0.2\\,\\text{dB/km};\\ R\\le-\\log_2(1-\\eta)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0994", "a": "02-electromagnetism-and-optics/photonics-and-lasers/laser-physics", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "name": "Frequency combs and stabilized lasers for optical clocks", "kind": "method transfer", "summary": "A mode-locked laser's pulse train is a comb of exactly spaced lines that links optical clock transitions to countable microwave frequencies. Pound–Drever–Hall locking to ultrastable cavities gives the sub-hertz-linewidth lasers that interrogate lattice and ion clocks.", "map": "\\nu_n=nf_{\\rm rep}+f_{\\rm ceo},\\ \\ f_{\\rm rep}=v_g/2L", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0995", "a": "02-electromagnetism-and-optics/photonics-and-lasers/laser-physics", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/laser-cooling-and-trapping", "name": "Laser radiation pressure: Doppler cooling and traps", "kind": "method transfer", "summary": "A narrow-linewidth laser tuned below resonance exerts a velocity-dependent scattering force that Doppler-cools atoms to T_D=ħΓ/2k_B. Intense far-detuned beams instead give conservative dipole potentials, the basis of optical traps and tweezers.", "map": "F=\\hbar k\\frac{\\Gamma}{2}\\frac{s}{1+s+4\\delta^2/\\Gamma^2},\\ k_BT_D=\\frac{\\hbar\\Gamma}{2},\\ U_{\\rm dip}\\propto\\frac{\\Gamma I}{\\delta}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0996", "a": "02-electromagnetism-and-optics/photonics-and-lasers/laser-physics", "b": "04-quantum-physics/quantum-optics/cavity-and-circuit-qed", "name": "Optical resonators: laser cavity to strong coupling", "kind": "shared object", "summary": "The Fabry–Pérot resonator that gives a laser its feedback becomes, at small mode volume and high finesse, a cavity where one atom and one photon exchange energy faster than either decays. The same Q/V figure of merit sets the Purcell factor.", "map": "g=\\frac{d}{\\hbar}\\sqrt{\\frac{\\hbar\\omega}{2\\epsilon_0V}},\\ C=\\frac{4g^2}{\\kappa\\gamma},\\ F_P=\\frac{3}{4\\pi^2}\\left(\\frac{\\lambda}{n}\\right)^3\\frac{Q}{V}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0997", "a": "02-electromagnetism-and-optics/photonics-and-lasers/laser-physics", "b": "04-quantum-physics/quantum-optics/quantized-light-and-photon-statistics", "name": "Einstein A/B and laser photon statistics", "kind": "mechanism", "summary": "Einstein's A/B ratio, derived from Planck's law, says spontaneous emission is stimulated emission driven by the vacuum's one photon per mode. Below threshold a laser emits thermal-like light with g^(2)(0)=2; above threshold its output is near-Poissonian coherent light with g^(2)(0)→1.", "map": "\\frac{A_{21}}{B_{21}}=\\frac{8\\pi h\\nu^3}{c^3}=h\\nu\\,\\rho_{\\rm modes}(\\nu),\\ \\bar n_{\\rm th}=\\frac{1}{e^{h\\nu/k_BT}-1},\\ g^{(2)}(0):2\\to1", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0998", "a": "02-electromagnetism-and-optics/photonics-and-lasers/metamaterials-and-plasmonics", "b": "04-quantum-physics/quantum-information-and-computation/superconducting-qubits", "name": "Superconducting circuits as microwave metamaterials", "kind": "method transfer", "summary": "Josephson-junction arrays and high-kinetic-inductance lines are lumped-element metamaterials with engineered dispersion. Dispersion engineering (band gaps, resonant phase matching) underlies Josephson travelling-wave parametric amplifiers, Purcell filters and band-gap waveguides coupled to transmons.", "map": "\\epsilon,\\mu\\to C_\\ell,\\ L_\\ell(\\Phi)\\ \\text{per unit length},\\ v_p=1/\\sqrt{L_\\ell C_\\ell},\\ L_J=\\frac{\\Phi_0}{2\\pi I_c\\cos\\varphi}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0999", "a": "02-electromagnetism-and-optics/photonics-and-lasers/metamaterials-and-plasmonics", "b": "04-quantum-physics/quantum-optics/cavity-and-circuit-qed", "name": "Photonic band gaps and nanocavities in cavity QED", "kind": "mechanism", "summary": "A photonic band gap suppresses spontaneous emission by removing optical modes. Photonic-crystal and plasmonic nanocavities with tiny mode volumes enhance it (Purcell effect) and reach strong coupling with single quantum dots or molecules: cavity QED in engineered media.", "map": "\\Gamma\\propto|\\mathbf d\\cdot\\mathbf E|^2\\rho_{\\rm LDOS}(\\omega),\\ \\ g\\propto V^{-1/2},\\ \\ F_P\\propto Q/V", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1000", "a": "02-electromagnetism-and-optics/photonics-and-lasers/nonlinear-optics", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "name": "Kerr NLSE in fibres ↔ Gross–Pitaevskii equation", "kind": "analogy", "summary": "Pulses in a Kerr fibre and a BEC's mean-field dynamics obey the same cubic nonlinear Schrödinger equation. Bright and dark solitons, modulational instability, self-focusing collapse and four-wave mixing all have matter-wave counterparts, and 'fluids of light' show superfluid-like flow.", "map": "i\\partial_zA=\\frac{\\beta_2}{2}\\partial_T^2A-\\gamma|A|^2A\\leftrightarrow i\\hbar\\partial_t\\psi=-\\frac{\\hbar^2}{2m}\\nabla^2\\psi+g|\\psi|^2\\psi;\\ \\gamma>0\\leftrightarrow g<0", "breaks": "In fibres the evolution variable is distance and 'space' is retarded time. BECs have traps, quantum depletion and true 3D collapse, and optical fluids are driven-dissipative rather than in equilibrium.", "confidence": "established", "strength": 3}
{"id": "C1001", "a": "02-electromagnetism-and-optics/photonics-and-lasers/nonlinear-optics", "b": "04-quantum-physics/quantum-information-and-computation/superconducting-qubits", "name": "Josephson junctions as microwave Kerr nonlinearities", "kind": "method transfer", "summary": "The Josephson cosine potential is a lossless microwave nonlinearity: expanded about its minimum, its quartic Kerr term makes the transmon an anharmonic oscillator. Pumped junctions work as parametric amplifiers and frequency converters, carrying four-wave mixing, phase matching and squeezing over to circuits.", "map": "-E_J\\cos\\varphi\\approx-E_J+\\frac{E_J}{2}\\varphi^2-\\frac{E_J}{24}\\varphi^4\\Rightarrow H_{\\rm Kerr}=-\\frac{E_C}{2}\\hat b^{\\dagger2}\\hat b^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1002", "a": "02-electromagnetism-and-optics/photonics-and-lasers/nonlinear-optics", "b": "04-quantum-physics/quantum-optics/single-photon-sources-and-detectors", "name": "SPDC: heralded single photons and entangled pairs", "kind": "mechanism", "summary": "Spontaneous parametric down-conversion is vacuum-seeded χ(2) difference-frequency generation: a pump photon splits into signal and idler photons, with phase matching enforcing energy and momentum conservation. Detecting one photon heralds the other, and type-II phase matching yields polarization-entangled pairs.", "map": "\\omega_p=\\omega_s+\\omega_i,\\ \\mathbf k_p=\\mathbf k_s+\\mathbf k_i\\,(+2\\pi/\\Lambda\\ \\text{QPM}),\\ H\\propto\\chi^{(2)}\\hat a_p\\hat a_s^\\dagger\\hat a_i^\\dagger+\\text{h.c.}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1003", "a": "02-electromagnetism-and-optics/photonics-and-lasers/nonlinear-optics", "b": "04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology", "name": "Parametric down-conversion as a squeezing source", "kind": "mechanism", "summary": "A degenerate χ(2) parametric amplifier (an OPO below threshold) produces squeezed vacuum through its two-photon Hamiltonian, and Kerr χ(3) media also squeeze. These sources are now injected into gravitational-wave interferometers.", "map": "H=\\frac{i\\hbar\\kappa}{2}(\\hat a^{\\dagger2}-\\hat a^2)\\Rightarrow\\Delta X_{\\rm sq}=\\tfrac12e^{-r},\\ \\Delta X_{\\rm anti}=\\tfrac12e^{r},\\ r=\\kappa t", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1004", "a": "02-electromagnetism-and-optics/photonics-and-lasers/topological-photonics", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/floquet-systems-and-time-crystals", "name": "Helical waveguide arrays as Floquet topological insulators", "kind": "method transfer", "summary": "In coupled waveguide arrays the paraxial equation makes propagation distance z act as time. Helically modulated waveguides therefore form a periodically driven lattice whose Floquet bands carry (anomalous) topology and chiral edge states, Floquet engineering demonstrated first with light.", "map": "i\\partial_z\\psi_n=-\\sum_m\\kappa_{nm}(z)\\psi_m,\\ \\kappa(z+Z)=\\kappa(z),\\ H_F=\\frac{i}{Z}\\ln U(Z)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1005", "a": "02-electromagnetism-and-optics/photonics-and-lasers/topological-photonics", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/non-hermitian-physics", "name": "Gain/loss photonics: PT symmetry and exceptional points", "kind": "shared object", "summary": "Optical lattices and resonators with engineered gain and loss are the main experimental platform for PT-symmetric Hamiltonians, exceptional points, the non-Hermitian skin effect and topological lasers. There the paraxial wave equation plays the role of a Schrödinger equation with a complex potential.", "map": "n(x)=n_R(x)+in_I(x),\\ n_R(x)=n_R(-x),\\ n_I(x)=-n_I(-x)\\Rightarrow\\mathcal{PT}\\text{-symmetric }H", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1006", "a": "02-electromagnetism-and-optics/photonics-and-lasers/topological-photonics", "b": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "name": "Berry curvature and Chern numbers of photonic bands", "kind": "identity", "summary": "Bloch modes of photonic crystals carry the same Berry connection and curvature as electronic bands. Breaking time reversal with magneto-optic media gives nonzero Chern numbers and chiral, backscattering-immune edge modes.", "map": "\\mathcal A_n=i\\langle u_{n\\mathbf k}|\\nabla_{\\mathbf k}u_{n\\mathbf k}\\rangle_\\epsilon,\\ C=\\frac{1}{2\\pi}\\int_{\\rm BZ}\\Omega\\,d^2k\\in\\mathbb Z,\\ N_{\\rm edge}=\\Delta C", "breaks": "The photonic inner product is ε-weighted, and with no Fermi level there is no quantized Hall conductance, only bulk–edge mode counting.", "confidence": "established", "strength": 3}
{"id": "C1007", "a": "02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics", "b": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "name": "High-harmonic generation as a sum over quantum orbits", "kind": "method transfer", "summary": "The three-step recollision model of HHG is a semiclassical evaluation of the strong-field path integral. Saddle points of the action give complex 'quantum orbits' whose classical return energy produces the I_p+3.17U_p cutoff, and the imaginary part of the ionization time encodes tunnelling.", "map": "\\hbar\\omega_{\\max}=I_p+3.17U_p,\\ U_p=\\frac{e^2E_0^2}{4m\\omega^2},\\ \\partial_{t,t',\\mathbf p}S=0,\\ \\gamma_K=\\sqrt{I_p/2U_p}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1008", "a": "02-electromagnetism-and-optics/radiation-and-scattering/cherenkov-and-transition-radiation", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "name": "Cherenkov emission and the Landau critical velocity", "kind": "analogy", "summary": "A source moving faster than the phase velocity of a medium's waves radiates them (Cherenkov emission). The Landau criterion for superfluidity is the same kinematic condition for emitting Bogoliubov excitations, so an obstacle dragged through a BEC faster than v_c≈c_s leaves a Cherenkov-like phonon wake.", "map": "\\cos\\theta_C=\\frac{1}{n\\beta}\\ (v>c/n)\\ \\leftrightarrow\\ v>v_c=\\min_p\\frac{\\varepsilon(p)}{p},\\ \\varepsilon(p)=\\sqrt{c_s^2p^2+(p^2/2m)^2}", "breaks": "The Bogoliubov dispersion is nonlinear, so the threshold is min ε/p rather than a constant phase velocity and the wake is not a simple cone. In practice, vortex nucleation sets a lower critical velocity.", "confidence": "established", "strength": 2}
{"id": "C1009", "a": "02-electromagnetism-and-optics/radiation-and-scattering/dipole-radiation-and-antennas", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "name": "Larmor dipole power ↔ Einstein A coefficient", "kind": "identity", "summary": "An atomic transition's spontaneous-emission rate equals the classical Larmor power of a dipole oscillating with amplitude 2|d_12|, divided by ħω. This is the correspondence principle at its sharpest, and it fixes natural linewidths and lifetimes.", "map": "\\bar P=\\frac{\\omega^4d_0^2}{12\\pi\\epsilon_0c^3}\\overset{d_0=2|d_{12}|}{\\longrightarrow}A_{21}=\\frac{\\bar P}{\\hbar\\omega}=\\frac{\\omega^3|d_{12}|^2}{3\\pi\\epsilon_0\\hbar c^3}", "breaks": "A classical dipole decays continuously; quantum emission happens in discrete jumps, needs vacuum fluctuations to start from an energy eigenstate, and never occurs from the ground state.", "confidence": "established", "strength": 3}
{"id": "C1010", "a": "02-electromagnetism-and-optics/radiation-and-scattering/dipole-radiation-and-antennas", "b": "04-quantum-physics/quantum-optics/single-photon-sources-and-detectors", "name": "Purcell effect: classical dipole power = quantum rate", "kind": "identity", "summary": "At weak coupling, any photonic environment changes a quantum emitter's decay rate by exactly the factor it changes a classical dipole's radiated power. Both are set by the local density of optical states (the dyadic Green's function), which guides nanoantenna and cavity design for bright single-photon sources.", "map": "\\frac{\\Gamma}{\\Gamma_0}=\\frac{P}{P_0}=\\frac{6\\pi c}{\\omega}\\,\\hat{\\mathbf n}\\cdot\\mathrm{Im}\\,\\mathbf G(\\mathbf r_0,\\mathbf r_0;\\omega)\\cdot\\hat{\\mathbf n}", "breaks": "Fails at strong coupling (vacuum Rabi splitting, non-exponential decay) and says nothing about photon statistics.", "confidence": "established", "strength": 3}
{"id": "C1011", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems", "name": "Larmor collapse of the classical atom", "kind": "historical", "summary": "By the Larmor formula, a classical electron orbiting a proton radiates and spirals in within about 10^-11 s. This instability of Rutherford's atom forced Bohr's quantization, and it is resolved by the stationary states of the quantum hydrogen atom.", "map": "P=\\frac{e^2a^2}{6\\pi\\epsilon_0c^3},\\ \\ \\tau_{\\rm collapse}=\\frac{a_0^3}{4r_e^2c}\\approx1.6\\times10^{-11}\\,\\text{s}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1012", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "name": "Mie partial waves, optical theorem, Born approximation", "kind": "identity", "summary": "Mie theory expands the scattered field in vector spherical harmonics with coefficients a_n, b_n, exactly as quantum partial-wave analysis uses phase shifts δ_l. The optical theorem began as optical extinction, and Rayleigh–Gans scattering is the first Born approximation.", "map": "\\sigma_{\\rm ext}=\\frac{4\\pi}{k}\\mathrm{Im}\\,f(0);\\ \\sigma_l\\propto(2l+1)\\sin^2\\delta_l\\leftrightarrow\\sigma_{\\rm sca}=\\frac{2\\pi}{k^2}\\sum_n(2n+1)(|a_n|^2+|b_n|^2)", "breaks": "Light is a vector field: there are two multipole families (TE and TM) and no monopole term, so the Mie sum starts at n=1.", "confidence": "established", "strength": 3}
{"id": "C1333", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-thermodynamics", "name": "Thermodynamics extended to quantum systems", "kind": "identity", "summary": "Quantum thermodynamics keeps the laws (energy balance, Clausius inequality, Carnot bound) but defines work and heat for density matrices and open-system maps. Coherence and entanglement act as additional resources or costs.", "map": "dU=\\mathrm{Tr}(\\dot\\rho H)+\\mathrm{Tr}(\\rho\\dot H)=\\dot Q+\\dot W;\\ \\Delta S\\ge\\beta Q", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1334", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/heat-engines-and-efficiency", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-thermodynamics", "name": "Quantum heat engines and refrigerators", "kind": "identity", "summary": "Otto, Carnot and absorption cycles run with qubits, oscillators and spins as working media; the Carnot bound survives with thermal baths. Non-thermal (squeezed, coherent) reservoirs can exceed η_C because they are not heat in the classical sense.", "map": "\\eta_{\\text{Otto}}^{\\text{qubit}}=1-\\omega_c/\\omega_h\\le\\eta_C", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1335", "a": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/laws-of-thermodynamics", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-thermodynamics", "name": "Third law and second laws in the quantum regime", "kind": "identity", "summary": "The unattainability principle has been derived and quantified for quantum systems: cooling time diverges as T→0, with a bound set by the bath's density of states. For small systems the second law splits into a family of single-shot conditions.", "map": "t\\gtrsim\\left(\\frac{1}{T}\\right)^{\\alpha}\\ \\text{to reach }T", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1336", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/localization-and-disorder", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "name": "Anderson localization and MBL in cold atoms", "kind": "shared object", "summary": "Optical speckle and quasiperiodic lattices made matter-wave Anderson localization directly visible (exponential density profiles), and interacting fermions in quasiperiodic lattices kept memory of an initial density wave, the first MBL signature.", "map": "n(z)\\propto e^{-2|z|/\\xi_{\\text{loc}}};\\ \\text{imbalance }I(t\\to\\infty)>0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1337", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/localization-and-disorder", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/floquet-systems-and-time-crystals", "name": "MBL-protected discrete time crystals", "kind": "mechanism", "summary": "Generic periodically driven many-body systems heat to infinite temperature. MBL prevents this and allows period-doubled spatiotemporal order, the discrete time crystal, which is stable to perturbations of the drive.", "map": "\\langle\\sigma^z_i(nT)\\rangle\\propto(-1)^n\\ \\text{for}\\ t\\to\\infty", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1338", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/localization-and-disorder", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/non-hermitian-physics", "name": "Hatano–Nelson: non-Hermitian localization from flux lines", "kind": "historical", "summary": "Non-Hermitian quantum mechanics as a field grew from the statistical mechanics of flux lines pinned by columnar defects in superconductors. An imaginary vector potential (tilted field) delocalizes Anderson states, the first non-Hermitian localization transition and the ancestor of the non-Hermitian skin effect.", "map": "H=\\sum_j[-\\tfrac t2(e^{g}c_{j+1}^\\dagger c_j+e^{-g}c_j^\\dagger c_{j+1})+\\epsilon_jn_j]", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1339", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/localization-and-disorder", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling", "name": "Level statistics: Poisson vs Wigner–Dyson", "kind": "identity", "summary": "Spectral statistics diagnose both Anderson/MB localization and quantum chaos: localized states give Poisson level spacings, and ergodic or extended states give random-matrix (GOE) repulsion. The ratio ⟨r⟩ is the standard order parameter for the MBL transition.", "map": "\\langle r\\rangle_{\\text{Poisson}}\\approx0.386,\\ \\langle r\\rangle_{\\text{GOE}}\\approx0.531", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1340", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/localization-and-disorder", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth", "name": "Many-body localization as ETH failure", "kind": "mechanism", "summary": "MBL is the main known mechanism by which an interacting, non-integrable quantum system violates ETH. Eigenstates have area-law entanglement and Poisson level statistics, and local memory survives forever.", "map": "S_A^{\\text{MBL}}\\sim L^{d-1}\\ \\text{vs}\\ S_A^{\\text{ETH}}\\sim L^d", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1341", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/percolation", "b": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "name": "Measurement-induced transitions and percolation", "kind": "identity", "summary": "In monitored random circuits, the zeroth Rényi entanglement entropy maps exactly onto a minimal cut through a percolation cluster. The measurement-induced volume-to-area-law transition therefore becomes classical percolation in this limit, and higher Rényi entropies flow to distinct non-percolation classes.", "map": "S_0(A)=\\min\\text{-cut on bond-percolated circuit},\\ p_c^{(0)}=p_c^{\\text{perc}}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1342", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/percolation", "b": "04-quantum-physics/quantum-information-and-computation/photonic-and-spin-qubits", "name": "Percolation thresholds for photonic cluster states", "kind": "method transfer", "summary": "Probabilistic fusion gates build random lattices of entangled photons, and a cluster state usable for universal measurement-based computation exists only above the bond-percolation threshold. Renormalizing the percolated lattice yields a regular resource, so loss tolerance is a percolation problem.", "map": "p_{\\text{fusion}}>p_c^{\\text{bond}}\\Rightarrow\\text{spanning cluster}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1343", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/spin-glasses", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling", "name": "SYK model began as a quantum spin glass", "kind": "historical", "summary": "The Sachdev–Ye random all-to-all Heisenberg magnet, introduced to study a quantum spin-glass/spin-liquid transition, became (as SYK) the canonical maximally chaotic quantum system. Random couplings, large-N and replica tools come straight from spin-glass theory.", "map": "H_{SYK}=\\sum J_{ijkl}\\chi_i\\chi_j\\chi_k\\chi_l,\\ \\overline{J^2}\\propto J^2/N^3;\\ \\lambda_L=2\\pi k_BT/\\hbar", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1344", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/spin-glasses", "b": "04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity", "name": "Spin-glass ground states and quantum annealing", "kind": "method transfer", "summary": "NP-hard optimization problems map onto spin-glass (Ising) ground-state searches. Quantum annealing replaces thermal fluctuations with a transverse field, and RSB landscapes and small gaps at first-order transitions limit its speedup.", "map": "H(s)=-(1-s)\\Gamma\\sum\\sigma^x_i+s\\,H_{\\text{Ising}}[\\sigma^z]", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1345", "a": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/spin-glasses", "b": "04-quantum-physics/quantum-information-and-computation/quantum-error-correction-and-fault-tolerance", "name": "Toric-code threshold as a random-bond Ising transition", "kind": "identity", "summary": "Optimal decoding of the surface code under independent bit-flip noise maps onto the 2D random-bond Ising model on the Nishimori line. The error threshold p_c≈10.9% is that model's ordering transition, and spin-glass replica tools now analyze qLDPC codes.", "map": "e^{-2\\beta J}=\\frac{p}{1-p}\\ (\\text{Nishimori line}),\\ p_c\\approx0.109", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1346", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "name": "Quantum gases as statistical-mechanics laboratories", "kind": "shared object", "summary": "Dilute ultracold Bose and Fermi gases realize textbook equilibrium statistical mechanics (ideal and weakly interacting BE/FD gases, BEC, degenerate Fermi pressure) with tunable interactions and traps.", "map": "k_BT_c=\\frac{2\\pi\\hbar^2}{m}\\left(\\frac{n}{\\zeta(3/2)}\\right)^{2/3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1347", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth", "name": "Why isolated quantum systems look thermal", "kind": "mechanism", "summary": "ETH supplies the quantum-mechanical foundation that equilibrium statistical mechanics assumes. Individual energy eigenstates already give microcanonical expectation values for few-body observables, so ergodicity is not needed.", "map": "\\langle E_m|O|E_n\\rangle=O(\\bar E)\\delta_{mn}+e^{-S(\\bar E)/2}f_O(\\bar E,\\omega)R_{mn}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1348", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "name": "Negative absolute temperature in optical lattices", "kind": "shared object", "summary": "A Bose–Hubbard gas with an upper-bounded energy spectrum (via band truncation and attractive U) was prepared at negative temperature, the textbook two-level-system case realized for motional degrees of freedom. It also revived the Gibbs-vs-Boltzmann entropy debate.", "map": "\\frac1T=\\frac{\\partial S}{\\partial E}<0\\ \\text{when}\\ E>E_{S_{\\max}}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1349", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth", "name": "Ensemble equivalence from eigenstate thermalization", "kind": "identity", "summary": "Under ETH the diagonal ensemble of a quench equals the microcanonical ensemble, which by ensemble equivalence equals the canonical one for local observables. Integrable systems need a generalized Gibbs ensemble instead.", "map": "\\sum_n|c_n|^2O_{nn}=\\langle O\\rangle_{\\text{mc}}(E)+O(e^{-S/2})", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1350", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "b": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "name": "Canonical typicality from entanglement", "kind": "identity", "summary": "For almost every pure state of a large system plus bath with fixed total energy, the reduced state of a small subsystem is close to canonical. Entanglement with the bath, not ensemble averaging over ignorance, explains the canonical ensemble.", "map": "\\mathrm{Tr}_B|\\psi\\rangle\\langle\\psi|\\approx\\frac{e^{-\\beta H_S}}{Z_S}\\ \\text{for typical}\\ |\\psi\\rangle\\in\\mathcal H_R", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1351", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "b": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "name": "Wick rotation: Z as an imaginary-time path integral", "kind": "identity", "summary": "Tr e^{-βH} is a Feynman path integral over paths periodic in imaginary time with period βħ. Quantum statistical mechanics in d dimensions is therefore classical statistical mechanics of polymers or fields in d+1 dimensions, which is the basis of path-integral Monte Carlo for helium.", "map": "Z=\\mathrm{Tr}\\,e^{-\\beta H}=\\oint\\mathcal Dx\\,e^{-S_E[x]/\\hbar},\\ \\tau\\in[0,\\beta\\hbar),\\ t=-i\\tau", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1352", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-thermodynamics", "name": "Landauer, demons and quantum resource theories", "kind": "identity", "summary": "Landauer erasure, Szilard engines and Maxwell demons generalize to qubits, where entanglement and coherence change the bookkeeping (negative conditional entropy can allow work extraction during erasure). Resource theories of athermality replace the free energy with a family of Rényi free energies for single-shot processes.", "map": "W_{\\text{erase}}\\ge k_BT\\ln2\\cdot S(A|B);\\ F_\\alpha=k_BT\\,D_\\alpha(\\rho\\|\\gamma)-k_BT\\ln Z", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1353", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth", "name": "Thermal entropy as eigenstate entanglement entropy", "kind": "identity", "summary": "In a thermalizing pure state, a subsystem's entanglement entropy equals the thermodynamic entropy at the effective temperature (volume law). This was measured in a quantum gas microscope, where entanglement entropy became thermal entropy.", "map": "S_{vN}(\\rho_A)\\approx s(\\beta)\\,|A|\\ \\text{for}\\ |A|\\ll|A^c|", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1354", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information", "b": "04-quantum-physics/quantum-information-and-computation", "name": "Information is physical: qubits and thermodynamics", "kind": "identity", "summary": "Quantum information inherits Shannon theory and Landauer's principle. Reversible unitary gates dissipate nothing in principle, but resetting ancillas and measurement records costs at least k_BT ln2 per bit.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1355", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information", "b": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "name": "Shannon, von Neumann and entanglement entropy", "kind": "identity", "summary": "The von Neumann entropy of a reduced density matrix is the quantum Shannon entropy and measures entanglement for pure bipartite states. It reduces to Gibbs entropy for thermal states.", "map": "S(\\rho_A)=-\\mathrm{Tr}\\rho_A\\ln\\rho_A\\ \\to\\ -\\sum_ip_i\\ln p_i\\ (\\text{diagonal }\\rho)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1356", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information", "b": "04-quantum-physics/quantum-information-and-computation/quantum-communication-and-cryptography", "name": "Shannon theory in quantum key distribution", "kind": "method transfer", "summary": "QKD security and channel capacities are written in entropies inherited from Shannon. The BB84 key rate uses the binary entropy h(Q), and the Holevo bound and quantum relative entropy generalize classical mutual information.", "map": "r\\ge1-2h(Q),\\ \\chi=S(\\textstyle\\sum p_i\\rho_i)-\\sum p_iS(\\rho_i)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1357", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/exactly-solvable-models", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth", "name": "Integrability, GGE and the quantum Newton's cradle", "kind": "mechanism", "summary": "Bethe-ansatz-integrable systems such as the Lieb–Liniger gas have extensively many conserved charges and do not thermalize to a Gibbs state. Trapped 1D Bose gases (the quantum Newton's cradle, Tonks–Girardeau gases) showed this, and the steady state is a generalized Gibbs ensemble.", "map": "\\rho_{GGE}=Z^{-1}e^{-\\sum_k\\lambda_k\\hat I_k}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1358", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "name": "Blackbody radiation shift in optical clocks", "kind": "shared object", "summary": "The ambient Planck field Stark-shifts clock transitions by an amount ∝T⁴. It is a leading systematic of optical lattice clocks and has driven cryogenic clocks with fractional BBR uncertainty near 10^{-20}.", "map": "\\Delta\\nu_{BBR}\\propto\\Delta\\alpha_0\\langle E^2\\rangle\\propto T^4", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1359", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "name": "Bose–Einstein condensation from quantum statistics to atoms", "kind": "identity", "summary": "The BEC critical temperature from Bose–Einstein statistics, nλ³=ζ(3/2), was realized in 1995 in dilute alkali gases. Trapped gases modify the density of states (T_c∝N^{1/3}ω) but test the same counting.", "map": "n\\lambda_{T_c}^3=\\zeta(3/2)\\approx2.612;\\ k_BT_c=0.94\\hbar\\bar\\omega N^{1/3}\\ (\\text{harmonic trap})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1360", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "04-quantum-physics/quantum-mechanics-core/postulates-and-formalism", "name": "Indistinguishability and the symmetrization postulate", "kind": "identity", "summary": "Bose and Fermi statistics follow from the symmetrization postulate for identical particles, and Gibbs' 1/N! (the resolution of the mixing paradox) is its classical limit. Thermal states are density operators ρ=e^{-βH}/Z in the postulates' formalism.", "map": "|\\psi\\rangle\\in\\mathrm{Sym}^N\\mathcal H\\ \\text{or}\\ \\wedge^N\\mathcal H\\ \\Rightarrow\\ \\langle n_k\\rangle=(e^{\\beta(\\epsilon_k-\\mu)}\\mp1)^{-1}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1361", "a": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "b": "04-quantum-physics/quantum-optics/quantized-light-and-photon-statistics", "name": "Thermal light: Bose–Einstein photon statistics", "kind": "identity", "summary": "A single mode of blackbody radiation has a Bose–Einstein (geometric) photon-number distribution with variance n̄²+n̄, which is the origin of Hanbury Brown–Twiss bunching g²(0)=2. Coherent states are Poissonian, so photon statistics distinguish thermal from laser light.", "map": "P(n)=\\frac{\\bar n^n}{(1+\\bar n)^{n+1}},\\ \\bar n=(e^{\\hbar\\omega/k_BT}-1)^{-1},\\ g^{(2)}(0)=2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1362", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics", "name": "Classical and quantum non-equilibrium dynamics", "kind": "identity", "summary": "Master equations, linear response and fluctuation theorems carry over from classical stochastic systems to open and closed quantum many-body systems. The Lindblad equation is the quantum Markov master equation.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1363", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/driven-systems-and-nonequilibrium-steady-states", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "name": "KPZ superdiffusion in quantum spin chains", "kind": "analogy", "summary": "Infinite-temperature spin transport in the isotropic Heisenberg chain is superdiffusive with z=3/2, and the spin profile matches the KPZ scaling function. This was observed with a quantum gas microscope.", "map": "\\langle S^z_x(t)S^z_0(0)\\rangle\\sim t^{-2/3}f_{KPZ}(x/t^{2/3})", "breaks": "Classical KPZ comes from a noisy, non-integrable growth equation. In the integrable Heisenberg chain the higher moments of the transferred magnetization deviate from Tracy–Widom, so only part of the KPZ phenomenology carries over.", "confidence": "current research", "strength": 2}
{"id": "C1364", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/driven-systems-and-nonequilibrium-steady-states", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/lindblad-master-equations", "name": "Boundary-driven quantum NESS and matrix products", "kind": "identity", "summary": "Boundary-driven Lindblad spin chains are the quantum counterpart of boundary-driven exclusion processes. Their steady states can be solved by matrix-product ansätze like Derrida's ASEP solution, giving exact currents and quantum NESS phase diagrams.", "map": "\\rho_\\infty\\propto S S^\\dagger,\\ S=\\langle0|\\mathbf L_1\\cdots\\mathbf L_n|0\\rangle", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1365", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "b": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "name": "Transport coefficients from scattering cross sections", "kind": "method transfer", "summary": "The Boltzmann collision integral takes its input from quantum scattering theory: dσ/dΩ fixes the mean free path, and Chapman–Enskog transport cross sections fix viscosity and conductivity. In ultracold gases the s-wave σ=8πa² sets thermalization and evaporative cooling.", "map": "\\eta=\\frac{5}{16}\\frac{\\sqrt{\\pi mk_BT}}{\\Omega^{(2,2)}},\\ \\Omega^{(2,2)}\\propto\\int(1-\\cos^2\\theta)\\frac{d\\sigma}{d\\Omega}d\\Omega", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1366", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth", "name": "ETH implies the fluctuation–dissipation theorem", "kind": "identity", "summary": "The smooth function f_O(E,ω) in the ETH ansatz fixes both the spectral function and the symmetrized correlator of O. Their ratio is the equilibrium FDT at the temperature of the eigenstate, so single eigenstates satisfy the FDT.", "map": "S_{OO}(\\omega)=4\\pi|f_O(\\bar E,\\omega)|^2\\cosh(\\beta\\omega/2)\\cdots;\\ \\chi''(\\omega)\\propto\\tanh(\\beta\\omega/2)S(\\omega)", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1367", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation", "b": "04-quantum-physics/quantum-optics/cavity-optomechanics", "name": "Thermal noise and cooling of mechanical oscillators", "kind": "identity", "summary": "A mechanical resonator's thermal force noise follows from the FDT applied to its susceptibility, and cavity sideband cooling engineers a colder effective bath. The asymmetry between Stokes and anti-Stokes sidebands (∝ n̄+1 vs n̄) is the quantum FDT, used as a primary thermometer.", "map": "S_{FF}(\\omega)=\\frac{2k_BT}{\\omega}\\mathrm{Im}\\chi^{-1}(\\omega)\\cdots;\\ \\frac{S(-\\Omega_m)}{S(+\\Omega_m)}=\\frac{\\bar n}{\\bar n+1}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1368", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation", "b": "04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology", "name": "Quantum FDT and the standard quantum limit", "kind": "identity", "summary": "The quantum FDT, with ħω coth(ħω/2k_BT) in place of 2k_BT, gives zero-point noise that sets the standard quantum limit of linear amplifiers and interferometers. Squeezing redistributes this noise between quadratures and cannot remove it.", "map": "S_x(\\omega)=\\hbar\\coth\\frac{\\hbar\\omega}{2k_BT}\\,\\mathrm{Im}\\chi(\\omega);\\ \\Delta X_1\\Delta X_2\\ge\\tfrac14", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1369", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/laser-cooling-and-trapping", "name": "Doppler cooling as Brownian motion in light", "kind": "identity", "summary": "Optical molasses is a Langevin system: radiation pressure provides linear friction and random spontaneous-emission recoils provide momentum diffusion. The Einstein relation k_BT=D_p/α gives the Doppler limit k_BT_D=ħΓ/2.", "map": "\\dot p=-\\alpha p+\\xi,\\ \\langle\\xi\\xi\\rangle=2D_p\\delta;\\ k_BT=D_p/\\alpha\\ \\Rightarrow\\ k_BT_D=\\hbar\\Gamma/2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1370", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical", "name": "Caldeira–Leggett: quantum Brownian motion", "kind": "identity", "summary": "A particle linearly coupled to an Ohmic bath of oscillators obeys the classical Langevin equation at high T, but in quantum form it decoheres spatial superpositions at a rate ∝ γ(Δx/λ_th)². Classical friction and quantum decoherence come from one bath spectral density.", "map": "J(\\omega)=\\eta\\omega;\\ \\tau_D^{-1}=\\gamma\\frac{2mk_BT(\\Delta x)^2}{\\hbar^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1371", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/lindblad-master-equations", "name": "Lindblad equation as the quantum master equation", "kind": "identity", "summary": "The Lindblad equation is the quantum version of the Pauli master equation and Fokker–Planck dynamics. Its diagonal part in the energy basis is a classical rate equation with detailed balance, and quantum trajectories are a stochastic unravelling like Langevin paths.", "map": "\\dot\\rho=-i[H,\\rho]+\\sum_k\\gamma_k(L_k\\rho L_k^\\dagger-\\tfrac12\\{L_k^\\dagger L_k,\\rho\\})\\ \\to\\ \\dot p_n=\\sum_m(W_{nm}p_m-W_{mn}p_n)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1372", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "b": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "name": "Kramers escape and instanton tunnelling rates", "kind": "method transfer", "summary": "Kramers' thermal escape rate and the Langer–Coleman–Caldeira–Leggett imaginary-time instanton rate are two limits of one rate theory. Below the crossover temperature T_0=ħω_b/2πk_B, macroscopic quantum tunnelling replaces activation, as observed in Josephson junctions.", "map": "\\Gamma_{\\text{th}}\\propto e^{-\\Delta U/k_BT}\\ (T>T_0);\\ \\Gamma_{\\text{q}}\\propto e^{-S_B/\\hbar}\\ (T<T_0),\\ T_0=\\hbar\\omega_b/2\\pi k_B", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1373", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-thermodynamics-and-fluctuation-theorems", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/lindblad-master-equations", "name": "Quantum-jump stochastic thermodynamics", "kind": "method transfer", "summary": "Unravelling Lindblad dynamics into quantum-jump trajectories assigns heat to each emitted or absorbed quantum. Full-counting statistics of these currents obey Gallavotti–Cohen symmetries and TURs (with quantum corrections), mirroring classical stochastic thermodynamics.", "map": "\\ln\\frac{P(+Q)}{P(-Q)}=(\\beta_c-\\beta_h)Q\\ (\\text{steady-state heat FT})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1374", "a": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-thermodynamics-and-fluctuation-theorems", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-thermodynamics", "name": "Quantum fluctuation theorems", "kind": "identity", "summary": "Jarzynski and Crooks relations hold for closed quantum systems when work is defined by two projective energy measurements. Strong coupling and coherence complicate the definition of heat.", "map": "\\langle e^{-\\beta W}\\rangle_{\\text{TPM}}=e^{-\\beta\\Delta F}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1375", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/critical-exponents-and-universality", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "name": "Kibble–Zurek measurement of BEC critical exponents", "kind": "method transfer", "summary": "Quenching a homogeneous Bose gas through T_c freezes in defects and coherence domains whose size scales as τ_Q^{ν/(1+zν)}. This measured ν≈0.5 and z≈1.4 in homogeneous gases, and trapped-gas correlation-length measurements gave ν≈0.67 (3D XY).", "map": "\\xi\\sim\\tau_Q^{\\nu/(1+z\\nu)}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1376", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/critical-exponents-and-universality", "b": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "name": "Entanglement entropy at quantum critical points", "kind": "identity", "summary": "At a 1+1D quantum critical point the ground-state entanglement entropy grows as (c/3) ln L, so the central charge that labels the universality class can be read off from entanglement. Gapped phases obey an area law instead.", "map": "S_A=\\frac c3\\ln\\frac L a+c'\\ (\\text{critical}),\\ S_A\\to\\text{const}\\ (\\text{gapped, 1D})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1377", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/ising-model-and-lattice-models", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "name": "Cold atoms as analog simulators of lattice models", "kind": "method transfer", "summary": "Bose–Hubbard and Fermi–Hubbard models in optical lattices realize lattice models from statistical mechanics with tunable couplings, including the superfluid–Mott transition and antiferromagnetic Ising and Heisenberg correlations. Quantum gas microscopes measure spin correlations site by site.", "map": "H_{BH}=-J\\sum b_i^\\dagger b_j+\\tfrac U2\\sum n_i(n_i-1);\\ (U/J)_c\\approx29\\ (3D)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1378", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/ising-model-and-lattice-models", "b": "04-quantum-physics/quantum-information-and-computation/trapped-ion-and-neutral-atom-qubits", "name": "Rydberg and ion arrays as programmable Ising magnets", "kind": "method transfer", "summary": "Rydberg-blockade tweezer arrays and trapped-ion chains implement transverse-field and long-range Ising models with hundreds of spins. Slow sweeps through their quantum critical points measure Kibble–Zurek scaling, which gives ν and z.", "map": "H=\\tfrac\\Omega2\\sum\\sigma^x_i-\\Delta\\sum n_i+\\sum\\frac{C_6}{r_{ij}^6}n_in_j;\\ \\xi_{KZ}\\sim\\tau_Q^{\\nu/(1+z\\nu)}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1379", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/ising-model-and-lattice-models", "b": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "name": "Quantum–classical mapping: TFIM ↔ (d+1)D Ising", "kind": "identity", "summary": "Suzuki–Trotter decomposition maps the d-dimensional transverse-field Ising model at T=0 onto an anisotropic (d+1)-dimensional classical Ising model. The quantum critical point therefore sits in the (d+1)D Ising class, with imaginary time acting as an extra dimension and z=1.", "map": "e^{-\\beta H_{TFIM}}\\to\\prod e^{K_\\tau s_{i,\\tau}s_{i,\\tau+1}+K s_{i,\\tau}s_{j,\\tau}},\\ \\tanh K_\\tau=e^{-2\\Delta\\tau\\Gamma}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1380", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "name": "Gross–Pitaevskii and BCS–BEC crossover as mean field", "kind": "identity", "summary": "The Gross–Pitaevskii equation is the Hartree mean-field theory of a condensate, with the macroscopic wavefunction as Landau order parameter. For fermions, BCS mean-field theory with a self-consistent chemical potential interpolates from BCS pairs to molecular BEC across a Feshbach resonance.", "map": "i\\hbar\\partial_t\\psi=[-\\tfrac{\\hbar^2}{2m}\\nabla^2+V+g|\\psi|^2]\\psi\\ \\leftrightarrow\\ \\delta F_{GL}/\\delta\\psi^*=0", "breaks": "GP mean field fails in 1D and near unitarity, where fluctuations and beyond-mean-field (Lee–Huang–Yang) corrections matter.", "confidence": "established", "strength": 2}
{"id": "C1381", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory", "b": "04-quantum-physics/quantum-optics/cavity-and-circuit-qed", "name": "Dicke superradiance as an exact mean-field transition", "kind": "identity", "summary": "Atoms coupled to one cavity mode interact all-to-all, so the Dicke/Hepp–Lieb superradiant transition is mean-field exact. A BEC in a pumped cavity realized it as self-organization into a checkerboard lattice, an open-system phase transition with a Landau order parameter ⟨a⟩.", "map": "\\lambda_c=\\frac12\\sqrt{\\omega\\omega_0},\\ \\langle a\\rangle\\propto(\\lambda-\\lambda_c)^{1/2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1382", "a": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/topological-phase-transitions-bkt", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "name": "BKT transition in 2D atomic gases", "kind": "shared object", "summary": "Quasi-2D trapped Bose gases show the BKT transition directly: interference contrast reveals quasi-long-range phase coherence below T_BKT, and free vortices proliferate above it. Uniform-box gases later confirmed the universal superfluid-density jump.", "map": "\\rho_s(T_{BKT}^-)=\\frac{2mk_BT_{BKT}}{\\pi\\hbar^2}\\ (n_s\\lambda^2=4)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1622", "a": "04-quantum-physics/atomic-molecular-and-optical-physics", "b": "04-quantum-physics/quantum-optics", "name": "Shared core: the driven two-level atom", "kind": "shared object", "summary": "Rabi oscillations, optical Bloch equations, dressed states and resonance fluorescence are common to both. AMO uses them to cool, trap and probe atoms; quantum optics uses them to make and characterize non-classical light (antibunching, the Mollow triplet).", "map": "\\Omega=\\mathbf d\\cdot\\mathbf E_0/\\hbar,\\quad \\Gamma=\\frac{\\omega^3|d|^2}{3\\pi\\epsilon_0\\hbar c^3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1623", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "b": "04-quantum-physics/quantum-information-and-computation/trapped-ion-and-neutral-atom-qubits", "name": "Quantum-logic spectroscopy: ion QC gates run clocks", "kind": "method transfer", "summary": "Phonon-bus gates developed for trapped-ion quantum computing let a logic ion read out a clock ion that lacks a cycling transition, giving Al+ clocks at the 10^-18 level. Entanglement-enhanced and tweezer-array clocks now also run on quantum-computing hardware.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1624", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "b": "04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology", "name": "Projection noise and spin squeezing in atomic clocks", "kind": "method transfer", "summary": "Ramsey spectroscopy with N uncorrelated atoms is limited by quantum projection noise, the atomic counterpart of photon shot noise in interferometers. Spin-squeezed or entangled atoms, the analogue of injecting squeezed light, push clocks and atom interferometers below the standard quantum limit toward the Heisenberg limit.", "map": "\\Delta\\phi_{\\rm SQL}=1/\\sqrt N,\\ \\Delta\\phi_{\\rm H}=1/N,\\ \\xi_R^2=\\frac{N(\\Delta J_\\perp)^2}{|\\langle\\mathbf J\\rangle|^2}", "breaks": "In clocks the local-oscillator noise and Dick effect often dominate over projection noise, so squeezing gains are smaller than ideal.", "confidence": "current research", "strength": 3}
{"id": "C1625", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin", "name": "Atomic term structure from angular-momentum coupling", "kind": "identity", "summary": "Atomic levels are labelled by coupled angular momenta (LS or jj coupling). Clebsch–Gordan algebra and the Wigner–Eckart theorem give the fine and hyperfine intervals, Landé g-factors and electric-dipole selection rules.", "map": "E_{\\rm SO}\\propto\\tfrac12[J(J+1)-L(L+1)-S(S+1)];\\ \\Delta J=0,\\pm1\\ (0\\not\\to0),\\ \\Delta m_J=0,\\pm1", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1626", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems", "name": "Exact hydrogen spectrum underpins atomic spectroscopy", "kind": "identity", "summary": "The Coulomb problem gives the Bohr levels, with an accidental l-degeneracy from hidden SO(4) symmetry. Fine structure, the Lamb shift and hyperfine splitting are perturbations of this exact spectrum, and quantum defects extend it to alkali Rydberg series.", "map": "E_n=-\\frac{hcR_\\infty}{n^2},\\quad E_{n\\ell}\\approx-\\frac{hcR_\\infty}{(n-\\delta_\\ell)^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1627", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "04-quantum-physics/quantum-information-and-computation/superconducting-qubits", "name": "Bosonic Josephson junction vs Cooper-pair box", "kind": "analogy", "summary": "A condensate in a double well follows a two-mode Bose–Hubbard Hamiltonian that maps onto the junction Hamiltonian behind charge qubits and transmons: number imbalance plays the role of Cooper-pair number and relative phase the role of φ. Josephson plasma oscillations are observed, and ring condensates with weak links form atomtronic SQUIDs.", "map": "U\\hat n^2-JN\\cos\\hat\\varphi\\ \\leftrightarrow\\ 4E_C\\hat n^2-E_J\\cos\\hat\\varphi,\\quad \\hat n=\\tfrac{N_L-N_R}{2}", "breaks": "Atoms are neutral and conserve total number, so there is no 2e charging, gate charge or electromagnetic environment. Large population imbalance gives nonlinear self-trapping. Large N and slow (Hz–kHz) dynamics mean the atomic junction is not a practical qubit.", "confidence": "established", "strength": 2}
{"id": "C1628", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "name": "s-wave scattering length sets condensate interactions", "kind": "identity", "summary": "At ultracold energies only s-wave scattering survives, so interactions reduce to a contact pseudopotential g = 4πħ²a/m in the Gross–Pitaevskii equation. Feshbach resonances, a bound-state resonance of partial-wave theory, tune a through zero and infinity, enabling the BEC–BCS crossover and Feshbach molecules.", "map": "g=\\frac{4\\pi\\hbar^2a}{m},\\quad a(B)=a_{\\rm bg}\\left(1-\\frac{\\Delta}{B-B_0}\\right)", "breaks": "The contact pseudopotential fails near resonance, where na³ is not small and three-body losses and effective-range terms matter.", "confidence": "established", "strength": 3}
{"id": "C1629", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/laser-cooling-and-trapping", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/lindblad-master-equations", "name": "Quantum trajectories grew out of laser-cooling theory", "kind": "historical", "summary": "The optical Bloch equations of a driven two-level atom are the prototype Lindbladian and set the Doppler limit. The Monte Carlo wave-function unraveling (Dalibard, Castin, Mølmer; alongside Carmichael and Zoller's group) was developed in this community, and simulations of sub-Doppler and sub-recoil cooling were among its first uses.", "map": "k_BT_D=\\frac{\\hbar\\Gamma}{2},\\quad H_{\\rm eff}=H-\\frac{i\\hbar}{2}\\sum_kL_k^\\dagger L_k", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1630", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/laser-cooling-and-trapping", "b": "04-quantum-physics/quantum-information-and-computation/trapped-ion-and-neutral-atom-qubits", "name": "Laser cooling and tweezers prepare atomic qubits", "kind": "method transfer", "summary": "Doppler and resolved-sideband cooling bring trapped ions to the motional ground state that phonon-bus gates need. MOT loading and optical tweezers with atom rearrangement assemble defect-free neutral-atom qubit arrays.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1631", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/laser-cooling-and-trapping", "b": "04-quantum-physics/quantum-optics/cavity-optomechanics", "name": "Resolved-sideband cooling of ions and mechanical modes", "kind": "mechanism", "summary": "Red-detuned driving scatters photons mainly into the anti-Stokes sideband, removing one phonon per photon. The same rate-equation theory sets the minimum occupancy of trapped ions and of radiation-pressure-cooled membranes, and levitated nanoparticles in optical tweezers join the two fields.", "map": "\\Gamma\\leftrightarrow\\kappa,\\ \\nu_{\\rm trap}\\leftrightarrow\\Omega_m;\\quad \\bar n_{\\min}\\approx\\left(\\frac{\\kappa}{4\\Omega_m}\\right)^2\\ (\\kappa\\ll\\Omega_m)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1632", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth", "name": "Lattice-gas quenches test thermalization and MBL", "kind": "shared object", "summary": "Bose- and Fermi-Hubbard gases in optical lattices are isolated, tunable many-body systems. Their quench dynamics directly test ETH, prethermalization and many-body localization, which was seen in quasi-periodic lattices.", "map": "H=-J\\sum_{\\langle ij\\rangle}a_i^\\dagger a_j+\\tfrac U2\\sum_i n_i(n_i-1)+\\sum_i\\epsilon_i n_i", "breaks": "Finite size, finite times and residual heating or atom loss stop experiments from settling thermodynamic-limit questions such as whether MBL is stable.", "confidence": "current research", "strength": 3}
{"id": "C1633", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "b": "04-quantum-physics/quantum-information-and-computation/trapped-ion-and-neutral-atom-qubits", "name": "Atom arrays as digital qubits and analog simulators", "kind": "shared object", "summary": "The same neutral atoms in lattices or tweezer arrays serve as digital qubits, with Rydberg-blockade gates, and as analog simulators of Ising and Hubbard models. Both rely on site-resolved fluorescence imaging, as in quantum-gas microscopes.", "map": "", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1634", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "b": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "name": "Synthetic gauge fields and Chern bands for neutral atoms", "kind": "method transfer", "summary": "Neutral atoms gain an artificial vector potential, either as the Berry connection of dressed internal states or as Peierls phases from laser-assisted or shaken-lattice tunnelling. This produced Hofstadter and Haldane Chern bands, whose Berry curvature and Chern numbers are measured from transverse drift and Thouless pumping.", "map": "\\mathbf A=i\\hbar\\langle\\chi|\\nabla\\chi\\rangle,\\quad C=\\frac{1}{2\\pi}\\int_{\\rm BZ}\\Omega(\\mathbf k)\\,d^2k", "breaks": "The fields are engineered through driving, which causes heating, and spontaneous emission limits lifetimes. Without disorder, leads or a Fermi sea they show no clean quantized Hall plateau.", "confidence": "established", "strength": 3}
{"id": "C1635", "a": "04-quantum-physics/foundations-of-quantum-mechanics/bell-nonlocality", "b": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "name": "Bell violation certifies entanglement", "kind": "mechanism", "summary": "Any violation of a Bell inequality certifies entanglement without trusting the devices, and the Tsirelson bound caps the quantum value. The converse fails: some entangled states, such as certain Werner states, admit local hidden-variable models, so nonlocality and entanglement are distinct resources.", "map": "|\\langle\\mathcal B_{\\rm CHSH}\\rangle|\\le2\\ (\\text{LHV}),\\ \\le2\\sqrt2\\ (\\text{QM})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1636", "a": "04-quantum-physics/foundations-of-quantum-mechanics/bell-nonlocality", "b": "04-quantum-physics/quantum-information-and-computation/quantum-communication-and-cryptography", "name": "Bell violation as a security certificate (E91, DI-QKD)", "kind": "method transfer", "summary": "Ekert's protocol uses a CHSH violation to bound an eavesdropper's information. Device-independent QKD and certified randomness turn loophole-free Bell tests into security proofs that do not trust the hardware.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1637", "a": "04-quantum-physics/foundations-of-quantum-mechanics/contextuality", "b": "04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity", "name": "Contextuality as the resource behind quantum speedup", "kind": "mechanism", "summary": "Clifford circuits on stabilizer states are classically simulable (Gottesman–Knill); universality comes from injecting magic states. For odd-prime-dimensional qudits, contextuality is necessary for magic-state universality; for qubits the link is subtler.", "map": "", "breaks": "For qubits, state-independent contextuality already exists within the classically simulable stabilizer theory, so contextuality is not a clean sufficient marker there.", "confidence": "current research", "strength": 2}
{"id": "C1638", "a": "04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical", "b": "04-quantum-physics/open-and-many-body-quantum-dynamics/lindblad-master-equations", "name": "Lindblad dephasing is the dynamics of decoherence", "kind": "mechanism", "summary": "Tracing out the environment under the Born–Markov approximation gives a Lindblad equation. Its dephasing term damps coherences between pointer states exponentially, at a rate set by their separation, which quantifies einselection.", "map": "L=\\sqrt\\gamma\\,\\hat x:\\ \\dot\\rho_{ij}=-\\tfrac{\\gamma}{2}(x_i-x_j)^2\\rho_{ij}", "breaks": "Non-Markovian or strongly coupled environments give decoherence that is not of Lindblad form, with memory effects and coherence revivals.", "confidence": "established", "strength": 3}
{"id": "C1639", "a": "04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical", "b": "04-quantum-physics/quantum-information-and-computation/quantum-error-correction-and-fault-tolerance", "name": "Error correction and DFS undo decoherence", "kind": "mechanism", "summary": "Error correction treats decoherence as a channel with Kraus operators E_k and recovers the encoded state when the Knill–Laflamme conditions hold. Collective environment coupling gives decoherence-free subspaces, the passive limit of the same algebra, where protected code spaces replace pointer states.", "map": "P\\,E_i^\\dagger E_j\\,P=c_{ij}P", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1640", "a": "04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical", "b": "04-quantum-physics/quantum-information-and-computation/superconducting-qubits", "name": "Qubit T1 and T2 as measured decoherence", "kind": "shared object", "summary": "Superconducting circuits are macroscopic quantum systems whose coherence is limited by TLS defects, quasiparticles, and flux and charge noise, so T1/T2 measurements and noise spectroscopy are direct studies of decoherence. The transmon design suppresses charge-noise dephasing exponentially.", "map": "1/T_2=1/(2T_1)+1/T_\\phi;\\ \\epsilon_1\\propto e^{-\\sqrt{8E_J/E_C}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1641", "a": "04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical", "b": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "name": "Influence functional and Caldeira–Leggett decoherence", "kind": "method transfer", "summary": "Integrating a harmonic bath out of the path integral gives the Feynman–Vernon influence functional. For an ohmic bath at high temperature this yields the Caldeira–Leggett master equation and the standard estimate that a superposition of separation Δx decoheres faster than it relaxes by a factor (Δx/λ_th)².", "map": "\\tau_D^{-1}\\simeq\\gamma\\left(\\frac{\\Delta x}{\\lambda_{\\rm th}}\\right)^2,\\quad \\lambda_{\\rm th}=\\frac{\\hbar}{\\sqrt{2mk_BT}}", "breaks": "Valid only for high temperature and ohmic, Markovian baths. At low temperature the master equation is not of Lindblad form and needs corrections.", "confidence": "established", "strength": 3}