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


---

# Packet 04-4 (100 records)

{"id": "C1742", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "07-nuclear-physics/heavy-ion-physics/collective-flow-and-hydrodynamics", "name": "Elliptic flow of unitary gases and the QGP", "kind": "analogy", "summary": "Strongly interacting Fermi gases released from anisotropic traps expand elliptically like the QGP's elliptic flow; both are nearly perfect fluids with eta/s near hbar/4 pi k_B.", "map": "\\eta/s\\gtrsim\\hbar/4\\pi k_B;\\ v_2\\leftrightarrow\\text{aspect-ratio inversion}", "breaks": "Non-relativistic vs relativistic hydrodynamics; scales differ by ~1e19 in temperature; the QGP has gauge degrees of freedom and a crossover, the gas has none.", "confidence": "established", "strength": 3}
{"id": "C1743", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "07-nuclear-physics/heavy-ion-physics/qcd-phase-diagram-and-critical-point", "name": "Cold-atom analogues of colour superfluidity", "kind": "analogy", "summary": "Three-component Fermi gases with attractive interactions can form colour-superfluid and trion ('baryon') phases, an analogue of colour superconductivity and confinement in the dense QCD phase diagram.", "map": "", "breaks": "No gauge field or gluon dynamics; trion formation is not confinement; densities map only qualitatively.", "confidence": "proposed", "strength": 1}
{"id": "C1744", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "name": "Unitary Fermi gas and dilute neutron matter", "kind": "mechanism", "summary": "The neutron-neutron scattering length (-18.5 fm) far exceeds the effective range, so low-density neutron matter is close to the unitary Fermi gas realized at Feshbach resonances; the measured Bertsch parameter benchmarks neutron-star crust EOS calculations.", "map": "E/N=\\xi\\,\\tfrac35E_F,\\ \\xi\\approx0.37;\\ k_F|a_{nn}|\\gg1\\gg k_Fr_e", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1745", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process", "name": "Hoyle state as an alpha-particle condensate", "kind": "analogy", "summary": "The 7.65 MeV Hoyle state of carbon-12 that enables triple-alpha burning has been described as a dilute gas of alpha clusters occupying one orbital, a nuclear analogue of a Bose condensate.", "map": "", "breaks": "Only three or four bosons with Pauli effects among constituent nucleons; the condensate fraction is model dependent and debated.", "confidence": "current research", "strength": 1}
{"id": "C1746", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "name": "Feshbach resonances: from nuclear reactions to cold atoms", "kind": "historical", "summary": "Feshbach developed closed-channel resonance theory for nuclear reactions; the same coupled-channel physics, tuned by magnetic field, became the main tool for controlling interactions in ultracold gases.", "map": "a(B)=a_{bg}\\left(1-\\frac{\\Delta}{B-B_0}\\right)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1747", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "BCS pairing in nuclei and Fermi gases", "kind": "mechanism", "summary": "Odd-even mass staggering and moments of inertia reflect BCS-like pairing in finite nuclei, the same gap equation as in BEC-BCS-crossover Fermi gases, with the cold-atom crossover a tunable laboratory for the regime. See the pairing-across-scales theme.", "map": "\\Delta=-\\sum_k V_{kk'}\\frac{\\Delta}{2E_k},\\ \\Delta_{\\rm nuc}\\approx12A^{-1/2}\\,\\mathrm{MeV}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1748", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Scissors modes in deformed nuclei and BECs", "kind": "analogy", "summary": "The scissors mode, a counter-rotation of proton and neutron clouds discovered in deformed nuclei, was predicted and observed in anisotropic BECs as a signature of superfluid irrotational flow.", "map": "\\omega_{\\rm sc}=\\sqrt{\\omega_x^2+\\omega_y^2}\\ \\text{(superfluid BEC)}", "breaks": "In nuclei the mode is a proton-neutron relative rotation in a finite fermion system; in a BEC it is the tilt oscillation of a single bosonic superfluid.", "confidence": "established", "strength": 2}
{"id": "C1749", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/laser-cooling-and-trapping", "b": "07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions", "name": "Laser-trapped radioactive atoms for weak-interaction tests", "kind": "method transfer", "summary": "Magneto-optical and dipole traps hold short-lived radioactive atoms nearly at rest, so recoiling nuclei and beta-neutrino angular correlations can be measured cleanly to search for scalar and tensor weak currents.", "map": "\\frac{d\\Gamma}{d\\Omega}\\propto1+a_{\\beta\\nu}\\frac{\\mathbf p_e\\cdot\\mathbf p_\\nu}{E_eE_\\nu}+b\\frac{m_e}{E_e}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1750", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/lindblad-master-equations", "b": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "name": "Quarkonium in the QGP as an open quantum system", "kind": "method transfer", "summary": "Heavy quark-antiquark pairs coupled to the QGP bath obey Lindblad equations derived from pNRQCD, describing screening, dissociation and regeneration of quarkonia beyond rate equations.", "map": "\\dot\\rho=-i[H,\\rho]+\\sum_n(C_n\\rho C_n^\\dagger-\\tfrac12\\{C_n^\\dagger C_n,\\rho\\})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1751", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "name": "Random-matrix theory began with nuclear resonances", "kind": "historical", "summary": "Wigner and Dyson introduced random matrices to model neutron-resonance spacings in heavy nuclei; the nuclear data ensemble later anchored the Bohigas-Giannoni-Schmit link between classical chaos and Wigner-Dyson statistics.", "map": "P_{\\rm GOE}(s)\\approx\\frac{\\pi s}{2}e^{-\\pi s^2/4};\\ \\text{Porter-Thomas widths}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1752", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth", "b": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "name": "Thermalization of an isolated QCD system", "kind": "mechanism", "summary": "Heavy-ion collisions pose the isolated-system thermalization problem at strong coupling: how a far-from-equilibrium gluon state reaches hydrodynamic behaviour in ~1 fm/c, with links to prethermalization and non-thermal fixed points studied in cold atoms.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1753", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/thermalization-and-eth", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "name": "Compound nucleus as a thermalizing system", "kind": "mechanism", "summary": "Bohr's compound nucleus forgets how it was formed and decays statistically, an early instance of an isolated many-body quantum system thermalizing; Hauser-Feshbach and evaporation theory use nuclear temperature.", "map": "\\sigma_{ab}=\\sigma_{\\rm CN}(a)\\frac{\\Gamma_b}{\\Gamma};\\ \\rho(E)\\propto e^{2\\sqrt{aE}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1754", "a": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "b": "07-nuclear-physics/hadron-and-nucleon-structure/parton-distribution-functions", "name": "Entanglement entropy in deep inelastic scattering", "kind": "method transfer", "summary": "The parton distribution probed at small x has been interpreted as the entanglement entropy between the probed region and the rest of the proton, linking DIS multiplicities to quantum information.", "map": "S(x)\\approx\\ln[xG(x)]", "breaks": "", "confidence": "proposed", "strength": 1}
{"id": "C1755", "a": "04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity", "b": "07-nuclear-physics/nuclear-structure/ab-initio-nuclear-theory", "name": "Quantum computing of nuclear ground states", "kind": "method transfer", "summary": "Variational quantum eigensolvers computed the deuteron binding energy from pionless/chiral EFT Hamiltonians on cloud processors, a first step toward quantum simulation of nuclear many-body problems.", "map": "E(\\theta)=\\langle\\psi(\\theta)|H_{\\rm EFT}|\\psi(\\theta)\\rangle\\ge E_0", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1756", "a": "04-quantum-physics/quantum-information-and-computation/superconducting-qubits", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Odd-even pairing effects in nuclei and SC islands", "kind": "mechanism", "summary": "Small superconducting islands show an even-odd ground-state energy difference from an unpaired quasiparticle, the same blocking effect behind nuclear odd-even mass staggering; quasiparticle poisoning of charge qubits is its device consequence.", "map": "\\Delta E_{\\rm odd-even}\\approx\\Delta\\ (\\text{gap});\\ E_{\\rm odd}-E_{\\rm even}=\\Delta-k_BT\\ln N_{\\rm eff}", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1757", "a": "04-quantum-physics/quantum-information-and-computation/trapped-ion-and-neutral-atom-qubits", "b": "07-nuclear-physics/nuclear-structure/exotic-nuclei-and-drip-lines", "name": "Penning-trap mass spectrometry", "kind": "method transfer", "summary": "Ion-trap techniques measure masses of exotic nuclei to 1e-8 or better via cyclotron frequencies, fixing separation energies, shell gaps and drip lines.", "map": "\\nu_c=\\frac{qB}{2\\pi m};\\ S_n=B(A,Z)-B(A-1,Z)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1758", "a": "04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Spin-orbit coupling and magic numbers", "kind": "method transfer", "summary": "A strong nuclear spin-orbit term splits j=l+-1/2 levels and reproduces the magic numbers; jj-coupling, Clebsch-Gordan and Wigner-Eckart machinery from atomic physics then organizes shell-model states.", "map": "V_{ls}(r)\\,\\mathbf l\\cdot\\mathbf s:\\ \\Delta E=\\frac{\\hbar^2}{2}(2l+1)\\langle V_{ls}\\rangle", "breaks": "Same operator algebra but different physics: nuclear spin-orbit is a strong-interaction effect, ~20x larger relative to level spacing, with inverted ordering relative to atomic fine structure.", "confidence": "established", "strength": 3}
{"id": "C1759", "a": "04-quantum-physics/quantum-mechanics-core/approximation-methods", "b": "07-nuclear-physics/nuclear-reactions-and-decays/fusion-reactions", "name": "WKB tunnelling and the Gamow peak", "kind": "mechanism", "summary": "Thermonuclear fusion proceeds by WKB tunnelling through the Coulomb barrier; the product of Maxwell-Boltzmann tail and penetrability gives the Gamow peak that sets stellar and fusion-reactor rates.", "map": "E_0=\\left[\\left(\\frac{\\pi\\alpha Z_1Z_2k_BT}{\\sqrt2}\\right)^2\\mu c^2\\right]^{1/3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1760", "a": "04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems", "b": "07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay", "name": "Alpha decay as Coulomb-barrier tunnelling", "kind": "mechanism", "summary": "Gamow and Gurney-Condon explained alpha decay as tunnelling through the Coulomb barrier; the barrier-penetration factor gives the Geiger-Nuttall law spanning 20+ orders of magnitude in half-life.", "map": "P\\approx\\exp\\left(-\\frac2\\hbar\\int_R^{r_c}\\sqrt{2\\mu(V-E)}dr\\right);\\ \\log t_{1/2}=a\\frac{Z}{\\sqrt{Q_\\alpha}}+b", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1761", "a": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-fission", "name": "Least-action paths for spontaneous fission", "kind": "method transfer", "summary": "Spontaneous-fission lifetimes are computed as imaginary-time tunnelling along least-action paths in a multidimensional collective space, an instanton/WKB calculation with a coordinate-dependent inertia.", "map": "S=\\int_{s_1}^{s_2}\\sqrt{2\\mathcal M(s)[V(s)-E]}\\,ds/\\hbar,\\ T_{1/2}\\propto e^{2S}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1762", "a": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "b": "07-nuclear-physics/nuclear-reactions-and-decays", "name": "Coulomb wavefunctions and the Gamow factor", "kind": "identity", "summary": "Charged-particle reaction rates factor into a smooth astrophysical S-factor and the Sommerfeld/Gamow penetrability that comes from exact Coulomb scattering wavefunctions at the origin.", "map": "\\sigma(E)=\\frac{S(E)}{E}e^{-2\\pi\\eta},\\ \\eta=\\frac{Z_1Z_2e^2}{4\\pi\\epsilon_0\\hbar v}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1763", "a": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "name": "Partial waves, resonances and the optical model", "kind": "method transfer", "summary": "Nuclear reaction theory is applied quantum scattering theory: phase shifts and partial waves, Breit-Wigner compound resonances, the complex optical potential (absorption via Im V), and R-matrix fits of cross sections.", "map": "\\sigma_{\\rm BW}=\\frac{\\pi}{k^2}g\\frac{\\Gamma_a\\Gamma_b}{(E-E_R)^2+\\Gamma^2/4};\\ U=V+iW", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1764", "a": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "b": "07-nuclear-physics/nuclear-structure/nuclear-forces-and-chiral-eft", "name": "Large scattering length: pionless EFT and cold atoms", "kind": "mechanism", "summary": "Pionless EFT for nucleons and the effective theory of Feshbach-tuned atoms share universal large-scattering-length physics: shallow dimers (deuteron), the three-body parameter and Efimov-like states in nuclei and halos.", "map": "f(k)=\\frac{1}{-1/a+r_ek^2/2-ik};\\ E_B\\approx\\hbar^2/ma^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1765", "a": "04-quantum-physics/quantum-optics/single-photon-sources-and-detectors", "b": "07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry", "name": "Photon-counting detectors shared with radiation detection", "kind": "shared object", "summary": "Scintillation and gamma spectroscopy rely on single-photon-sensitive photodetectors (PMTs, SiPMs), while transition-edge-sensor microcalorimeters developed for quantum optics give eV resolution for gamma and X-ray lines.", "map": "\\frac{\\sigma_E}{E}=2.355\\sqrt{\\frac{Fw}{E}}", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1766", "a": "04-quantum-physics/atomic-molecular-and-optical-physics", "b": "08-condensed-matter/strongly-correlated-electrons/hubbard-model-and-mott-physics", "name": "Cold atoms as analog Hubbard simulators", "kind": "method transfer", "summary": "Ultracold atoms in optical lattices realize Bose- and Fermi-Hubbard models with tunable U/t, giving clean, disorder-free access to Mott physics and magnetism that motivate condensed-matter questions.", "map": "H=-t\\sum c^\\dagger_{i\\sigma}c_{j\\sigma}+U\\sum n_{i\\uparrow}n_{i\\downarrow}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1767", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "08-condensed-matter/crystals-and-electronic-structure/density-functional-theory", "name": "From Hartree-Fock atoms to density functionals", "kind": "historical", "summary": "Self-consistent-field methods for atoms (Hartree-Fock, Thomas-Fermi, Slater's exchange approximation) led directly to density functional theory for solids.", "map": "v_x^{\\rm Slater}\\propto-n^{1/3}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1768", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/transition-metal-dichalcogenides-and-excitons", "name": "Exciton and polariton condensation", "kind": "mechanism", "summary": "Excitons and exciton-polaritons are composite bosons that condense at high temperature because of their light mass; interlayer TMD excitons are candidate equilibrium exciton condensates.", "map": "k_BT_c\\propto\\frac{\\hbar^2n^{2/3}}{m^*},\\ m^*_{\\rm pol}\\sim10^{-4}m_e", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1769", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "08-condensed-matter/magnetism/spintronics", "name": "Synthetic spin-orbit coupling in quantum gases", "kind": "analogy", "summary": "Raman dressing gives atoms Rashba/Dresselhaus-like spin-orbit coupling, emulating spintronic Hamiltonians in clean, tunable neutral gases.", "map": "H=\\frac{(\\mathbf p-\\hbar k_R\\sigma_z\\hat x)^2}{2m}+\\frac\\Omega2\\sigma_x", "breaks": "Neutral atoms carry no charge current; synthetic SOC comes with heating from spontaneous emission.", "confidence": "established", "strength": 2}
{"id": "C1770", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "BEC-BCS crossover connects pairs and condensates", "kind": "mechanism", "summary": "Feshbach-tuned Fermi gases cross continuously from BCS Cooper pairing to a BEC of tightly bound molecules; the same gap and number equations describe superconductors at weak coupling.", "map": "\\frac{1}{k_Fa}:-\\infty\\ (\\mathrm{BCS})\\to0\\ (\\mathrm{unitary})\\to+\\infty\\ (\\mathrm{BEC});\\ E_k=\\sqrt{\\xi_k^2+\\Delta^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1771", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "08-condensed-matter/superconductivity/cuprate-high-tc-superconductors", "name": "Preformed pairs and the BEC-BCS crossover", "kind": "analogy", "summary": "Short coherence lengths in cuprates place them between BCS and BEC limits; the pseudogap has been compared to preformed pairs above T_c in the cold-atom crossover.", "map": "", "breaks": "Cuprate pairing is d-wave in a doped Mott insulator with competing orders; the cold-atom crossover is s-wave in a clean continuum gas.", "confidence": "current research", "strength": 2}
{"id": "C1772", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "b": "08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons", "name": "Bloch bands in optical lattices", "kind": "identity", "summary": "Atoms in optical lattices obey Bloch's theorem with tight-binding bands and Wannier functions; Bloch oscillations, unobservable in solids because of scattering, are seen directly.", "map": "\\hbar\\dot{\\mathbf k}=\\mathbf F;\\ \\omega_B=Fa/\\hbar", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1773", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/moire-materials-and-twisted-bilayers", "name": "Moire materials as solid-state quantum simulators", "kind": "analogy", "summary": "Twisted bilayers realize tunable lattice models (triangular Hubbard, flat Chern bands) by twist angle and gating, playing the role optical lattices play for atoms.", "map": "", "breaks": "Moire electrons have long-range Coulomb interactions, phonons and disorder; filling and interactions are tuned differently from cold atoms.", "confidence": "current research", "strength": 2}
{"id": "C1774", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "b": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "name": "Superexchange observed with cold atoms", "kind": "mechanism", "summary": "In optical double wells, second-order tunnelling produces superexchange J=4t^2/U between spins, measured in real time.", "map": "J_{\\rm ex}=4t^2/U", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1775", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "b": "08-condensed-matter/strongly-correlated-electrons", "name": "Quantum simulation of correlated-electron problems", "kind": "method transfer", "summary": "Strongly correlated electron problems (doped Hubbard, pseudogap, stripes) that resist numerics are posed to cold-atom simulators, whose measurements now benchmark DMFT, DMRG and QMC.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1776", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "b": "08-condensed-matter/strongly-correlated-electrons/hubbard-model-and-mott-physics", "name": "Superfluid-Mott transition in optical lattices", "kind": "identity", "summary": "Deep optical lattices map exactly onto the Bose-Hubbard model; tuning lattice depth drove the superfluid-Mott insulator quantum phase transition, and quantum gas microscopes now image Hubbard correlations site by site.", "map": "H_{BH}=-J\\sum b_i^\\dagger b_j+\\tfrac U2\\sum n_i(n_i-1);\\ (U/J)_c\\approx29\\ (3D)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1777", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "b": "08-condensed-matter/superconductivity/cuprate-high-tc-superconductors", "name": "Fermi-Hubbard simulators target cuprate physics", "kind": "method transfer", "summary": "Quantum gas microscopes observed long-range antiferromagnetism and then hole-doped correlations in the 2D Fermi-Hubbard model, addressing the doped-Mott-insulator physics of cuprates.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1778", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/optical-lattices-and-quantum-simulation", "b": "08-condensed-matter/topological-matter/quantum-hall-effects", "name": "Chern bands and Hofstadter models with cold atoms", "kind": "method transfer", "summary": "Shaken and laser-assisted-tunnelling optical lattices realized the Haldane and Harper-Hofstadter models, measuring Chern numbers of synthetic quantum-Hall bands.", "map": "H=-J\\sum e^{i2\\pi\\alpha m}a^\\dagger_{m+1,n}a_{m,n}+\\text{h.c.}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1779", "a": "04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures", "name": "Nuclear-spin bath decoherence of dot spins", "kind": "mechanism", "summary": "In GaAs dots the electron spin decoheres through hyperfine coupling to ~1e6 nuclear spins, a central-spin model of system-bath decoherence that drove the move to isotopically purified Si.", "map": "H=g\\mu_BBS_z+\\sum_kA_k\\mathbf S\\cdot\\mathbf I_k", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1780", "a": "04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "Macroscopic quantum tunnelling in Josephson junctions", "kind": "historical", "summary": "Caldeira and Leggett's theory of dissipative tunnelling and the 1985 observation of quantized levels in a current-biased junction showed a macroscopic phase variable obeys quantum mechanics (Nobel 2025).", "map": "\\Gamma\\propto e^{-7.2\\Delta U/\\hbar\\omega_p}\\ (\\text{weak damping})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1781", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/floquet-systems-and-time-crystals", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "name": "Light-induced anomalous Hall effect in graphene", "kind": "method transfer", "summary": "Circularly polarized light opens a Floquet gap at graphene's Dirac points; an anomalous Hall response was measured in ultrafast transport.", "map": "\\Delta_F\\approx\\frac{(ev_FE_0)^2}{\\hbar\\omega^3}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1782", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/floquet-systems-and-time-crystals", "b": "08-condensed-matter/topological-matter/topological-insulators", "name": "Floquet topological insulators", "kind": "method transfer", "summary": "Periodic driving (circularly polarized light) opens topological gaps in trivial bands; Floquet bands carry Chern and anomalous winding invariants beyond static classification.", "map": "H_{\\rm eff}\\approx\\bar H+\\frac{[H_{-1},H_{1}]}{\\hbar\\omega}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1783", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/non-hermitian-physics", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "Non-Hermitian band topology", "kind": "method transfer", "summary": "Gain and loss extend band topology to point and line gaps; spectral winding gives the skin effect and modifies bulk-boundary correspondence, enlarging the tenfold classification.", "map": "w=\\oint\\frac{dk}{2\\pi i}\\partial_k\\ln\\det[H(k)-E_0]", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1784", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/non-hermitian-physics", "b": "08-condensed-matter/topological-matter/topological-semimetals", "name": "Bulk Fermi arcs from exceptional points", "kind": "mechanism", "summary": "Finite quasiparticle lifetimes make the effective Hamiltonian non-Hermitian; Weyl or Dirac nodes split into exceptional rings joined by bulk Fermi arcs.", "map": "H_{\\rm eff}=H_0+\\Sigma(\\omega=0),\\ \\mathrm{Im}\\Sigma\\neq0", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1785", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling", "b": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "name": "Random-matrix theory of quantum transport", "kind": "method transfer", "summary": "Universal conductance fluctuations and weak localization in chaotic cavities follow random-matrix statistics of transmission eigenvalues, the quantum-chaos framework applied to transport.", "map": "\\mathrm{var}\\,G\\sim(e^2/h)^2,\\ \\text{independent of size}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1786", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling", "b": "08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals", "name": "Planckian dissipation and the chaos bound", "kind": "mechanism", "summary": "Strange metals relax at the Planckian rate hbar/tau ~ k_BT, the same scale as the quantum chaos bound; SYK-type models realize both maximal chaos and linear-in-T resistivity.", "map": "\\frac{\\hbar}{\\tau}\\approx\\alpha k_BT\\ \\leftrightarrow\\ \\lambda_L\\le\\frac{2\\pi k_BT}{\\hbar}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1787", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-thermodynamics", "b": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "name": "Quantum of thermal conductance", "kind": "mechanism", "summary": "A single ballistic channel carries at most one heat quantum; mesoscopic conductors serve as quantum heat engines and refrigerators analysed with Landauer heat currents.", "map": "G_Q=\\frac{\\pi^2k_B^2T}{3h}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1788", "a": "04-quantum-physics/quantum-information-and-computation", "b": "08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order", "name": "Topological quantum computation with anyons", "kind": "method transfer", "summary": "Braiding non-Abelian anyons of a topologically ordered phase implements gates protected by topology, turning a condensed-matter phase into a quantum computer architecture.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1789", "a": "04-quantum-physics/quantum-information-and-computation", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "Josephson junction as the nonlinear qubit element", "kind": "shared object", "summary": "The dissipationless nonlinear inductance of a Josephson junction is what makes superconducting circuits anharmonic and hence usable as qubits.", "map": "I=I_c\\sin\\varphi,\\ L_J=\\frac{\\Phi_0}{2\\pi I_c\\cos\\varphi}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1790", "a": "04-quantum-physics/quantum-information-and-computation", "b": "08-condensed-matter/topological-matter/quantum-hall-effects", "name": "Non-Abelian anyons in fractional quantum Hall states", "kind": "method transfer", "summary": "The nu=5/2 state is a candidate Moore-Read phase with Ising anyons; interferometry and braiding there are a proposed route to topological qubits.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1791", "a": "04-quantum-physics/quantum-information-and-computation", "b": "08-condensed-matter/topological-matter/topological-superconductors-and-majoranas", "name": "Majorana zero modes as topological qubits", "kind": "method transfer", "summary": "Majorana zero modes at Kitaev-chain ends store a qubit in nonlocal fermion parity; braiding gives protected Clifford gates. Experimental claims in nanowires remain contested.", "map": "H_K=\\sum[-\\mu c_j^\\dagger c_j-t(c_j^\\dagger c_{j+1}+\\text{h.c.})+\\Delta(c_jc_{j+1}+\\text{h.c.})]", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1792", "a": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "b": "08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order", "name": "Topological entanglement entropy", "kind": "identity", "summary": "Topological order leaves a universal negative constant in the entanglement entropy area law, set by the total quantum dimension of the anyons.", "map": "S_A=\\alpha L-\\gamma,\\ \\gamma=\\ln\\mathcal D", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1793", "a": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "Area laws make DMRG and tensor networks work", "kind": "method transfer", "summary": "Gapped ground states obey entanglement area laws, so matrix-product states with bounded bond dimension represent them faithfully; DMRG is variational optimization over MPS.", "map": "S\\le\\log\\chi;\\ S(\\ell)\\le\\text{const}\\ (1\\mathrm{D\\ gapped})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1794", "a": "04-quantum-physics/quantum-information-and-computation/photonic-and-spin-qubits", "b": "08-condensed-matter/crystals-and-electronic-structure/semiconductors", "name": "Donor and Si/SiGe spin qubits", "kind": "shared object", "summary": "Silicon spin qubits rely on semiconductor physics: donor levels, valley splitting, isotopic purification of Si-28 and CMOS fabrication.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1795", "a": "04-quantum-physics/quantum-information-and-computation/photonic-and-spin-qubits", "b": "08-condensed-matter/low-dimensional-and-quantum-materials", "name": "2D materials as hosts for spin and valley qubits", "kind": "shared object", "summary": "Graphene and TMD quantum dots offer weak hyperfine coupling and valley degrees of freedom as alternative qubit hosts.", "map": "", "breaks": "", "confidence": "current research", "strength": 1}
{"id": "C1796", "a": "04-quantum-physics/quantum-information-and-computation/photonic-and-spin-qubits", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "name": "NV magnetometry images electron hydrodynamics", "kind": "method transfer", "summary": "Nitrogen-vacancy centres used as nanoscale quantum magnetometers imaged the Poiseuille flow profile of the Dirac fluid in graphene.", "map": "\\delta B\\sim\\frac{\\hbar}{g\\mu_B\\sqrt{T_2t}}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1797", "a": "04-quantum-physics/quantum-information-and-computation/photonic-and-spin-qubits", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures", "name": "Gate-defined quantum-dot spin qubits", "kind": "shared object", "summary": "Single electrons confined in gate-defined quantum dots carry spin qubits controlled by exchange (Loss-DiVincenzo); Coulomb blockade and charge sensing come from mesoscopic quantum-dot physics.", "map": "H=g\\mu_B\\mathbf B\\cdot\\mathbf S+J(t)\\mathbf S_1\\cdot\\mathbf S_2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1798", "a": "04-quantum-physics/quantum-information-and-computation/quantum-algorithms-and-complexity", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "Quantum algorithms for correlated materials", "kind": "method transfer", "summary": "Phase estimation, VQE and Hamiltonian simulation target ground states and dynamics of Hubbard-type models that classical numerics cannot reach, the leading candidate for quantum advantage.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1799", "a": "04-quantum-physics/quantum-information-and-computation/quantum-error-correction-and-fault-tolerance", "b": "08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order", "name": "Toric code is a topologically ordered phase", "kind": "identity", "summary": "The surface/toric code Hamiltonian is a Z2 topologically ordered phase: logical operators are anyon loops, code distance is system size, and the threshold maps to a disorder phase transition of a random-bond Ising model.", "map": "H=-\\sum_vA_v-\\sum_pB_p;\\ \\text{GSD}=4\\ \\text{on torus}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1800", "a": "04-quantum-physics/quantum-information-and-computation/superconducting-qubits", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "Phonons as qubit resource and error source", "kind": "mechanism", "summary": "Qubits couple coherently to bulk and surface-acoustic phonon modes (quantum acoustodynamics), while phonon bursts from cosmic rays break Cooper pairs and cause chip-wide correlated errors.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1801", "a": "04-quantum-physics/quantum-information-and-computation/superconducting-qubits", "b": "08-condensed-matter/superconductivity", "name": "Superconductors as the material base of qubits", "kind": "shared object", "summary": "Superconducting qubits inherit BCS physics: the gap protects against dissipation, while quasiparticles, two-level defects and surface oxides of Nb/Al/Ta set coherence.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1802", "a": "04-quantum-physics/quantum-information-and-computation/superconducting-qubits", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Quasiparticles limit qubit coherence", "kind": "mechanism", "summary": "Non-equilibrium Bogoliubov quasiparticles above the BCS gap tunnel across junctions and cause relaxation and parity switching; gap engineering and phonon traps suppress them.", "map": "\\Gamma_1^{qp}\\propto x_{qp}\\sqrt{\\frac{2\\Delta}{\\hbar\\omega_q}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1803", "a": "04-quantum-physics/quantum-information-and-computation/superconducting-qubits", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "Transmon Hamiltonian from Josephson physics", "kind": "identity", "summary": "A capacitively shunted Josephson junction is a quantum pendulum; at E_J/E_C ~ 50 the charge dispersion is exponentially suppressed, giving the transmon qubit.", "map": "H=4E_C(\\hat n-n_g)^2-E_J\\cos\\hat\\varphi,\\ \\omega_{01}\\approx\\sqrt{8E_JE_C}-E_C", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1804", "a": "04-quantum-physics/quantum-information-and-computation/trapped-ion-and-neutral-atom-qubits", "b": "08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids", "name": "Rydberg arrays realize a Z2 spin liquid", "kind": "method transfer", "summary": "Rydberg-blockade atom arrays on a ruby lattice prepared a state with topological string order of a Z2 quantum spin liquid, a phase long sought in frustrated magnets.", "map": "H=\\frac\\Omega2\\sum\\sigma^x_i-\\Delta\\sum n_i+\\sum V_{ij}n_in_j", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1805", "a": "04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin", "b": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "name": "Exchange from spin algebra and Pauli exclusion", "kind": "mechanism", "summary": "Heisenberg exchange arises because the Coulomb energy depends on the singlet or triplet spin state through antisymmetry; addition of spin angular momenta gives the S1.S2 form.", "map": "H=-J\\,\\mathbf S_1\\cdot\\mathbf S_2,\\ \\mathbf S_1\\cdot\\mathbf S_2=\\tfrac12[S(S+1)-\\tfrac32]", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1806", "a": "04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin", "b": "08-condensed-matter/magnetism/spintronics", "name": "Spin angular momentum as a transport degree of freedom", "kind": "method transfer", "summary": "Spintronics transports and manipulates spin angular momentum: spin precession, spin-orbit coupling (Rashba/Dresselhaus) and spin-transfer torque are the quantum mechanics of spin applied to devices.", "map": "\\dot{\\mathbf S}=\\gamma\\mathbf S\\times\\mathbf B;\\ H_R=\\alpha(\\boldsymbol\\sigma\\times\\mathbf k)\\cdot\\hat z", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1807", "a": "04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems", "b": "08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids", "name": "Kitaev honeycomb model and Kitaev materials", "kind": "method transfer", "summary": "Kitaev's exactly solvable honeycomb model has a Z2 spin-liquid ground state with Majorana excitations; it motivates the search in alpha-RuCl3 and iridates.", "map": "H_K=-\\sum_{\\langle ij\\rangle_\\gamma}K_\\gamma S_i^\\gamma S_j^\\gamma", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1808", "a": "04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems", "b": "08-condensed-matter/topological-matter/quantum-hall-effects", "name": "Landau levels are harmonic-oscillator levels", "kind": "identity", "summary": "A charged particle in a uniform field maps onto a harmonic oscillator, giving Landau levels; filling them gives the integer quantum Hall plateaus.", "map": "E_n=\\hbar\\omega_c(n+\\tfrac12),\\ \\omega_c=eB/m^*", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1809", "a": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "b": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "name": "Aharonov-Bohm oscillations in mesoscopic rings", "kind": "mechanism", "summary": "Phase-coherent electrons in metal rings show conductance oscillations with flux period h/e, a direct transport measurement of the Aharonov-Bohm phase.", "map": "\\Delta\\Phi=h/e", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1810", "a": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "name": "Berry phase pi of graphene's Dirac electrons", "kind": "mechanism", "summary": "Pseudospin winding gives graphene electrons a pi Berry phase, producing the half-integer quantum Hall sequence and suppressed backscattering.", "map": "\\sigma_{xy}=4\\frac{e^2}{h}(n+\\tfrac12)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1811", "a": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "b": "08-condensed-matter/magnetism/magnetic-skyrmions-and-textures", "name": "Emergent electromagnetism of skyrmions", "kind": "mechanism", "summary": "Electrons adiabatically following a skyrmion texture acquire a real-space Berry phase that acts as an emergent magnetic flux of one quantum per skyrmion, giving the topological Hall effect.", "map": "b_z=\\frac{\\hbar}{2e}\\mathbf m\\cdot(\\partial_x\\mathbf m\\times\\partial_y\\mathbf m)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1812", "a": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "b": "08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order", "name": "Anyon statistics as Berry phases", "kind": "identity", "summary": "Exchanging two quasiparticles adiabatically gives a Berry phase; for Laughlin quasiholes it equals pi times the filling, so fractional statistics is a geometric phase.", "map": "\\gamma_{\\rm exch}=\\pi\\nu\\ (\\nu=1/m)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1813", "a": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "b": "08-condensed-matter/topological-matter", "name": "Geometric phases organize topological matter", "kind": "historical", "summary": "Berry's 1984 phase gave condensed matter a unified language for polarization, anomalous Hall effects and topological phases.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1814", "a": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "Chern number is integrated Berry curvature", "kind": "identity", "summary": "The Hall conductance of a filled band equals the Brillouin-zone integral of Berry curvature (TKNN); geometric-phase concepts define all band-topological invariants.", "map": "\\sigma_{xy}=\\frac{e^2}{h}\\frac{1}{2\\pi}\\int_{\\rm BZ}\\Omega_{xy}d^2k", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1815", "a": "04-quantum-physics/quantum-mechanics-core/geometric-phases", "b": "08-condensed-matter/topological-matter/topological-semimetals", "name": "Weyl points as Berry-curvature monopoles", "kind": "identity", "summary": "Berry's degeneracy monopole is realized in crystals: Weyl nodes are sources of Berry flux with integer charge, giving Fermi arcs and the chiral anomaly.", "map": "\\oint_S\\Omega\\cdot d\\mathbf S=2\\pi\\chi,\\ \\chi=\\pm1", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1816", "a": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "Path-integral quantum Monte Carlo", "kind": "method transfer", "summary": "Imaginary-time path integrals map quantum many-body systems onto classical polymers, sampled by Monte Carlo; bosonic exchange appears as permutation cycles (superfluid helium).", "map": "Z=\\mathrm{Tr}e^{-\\beta H}=\\int\\mathcal Dx\\,e^{-S_E[x]/\\hbar}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1817", "a": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "b": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "name": "Born approximation behind diffraction", "kind": "identity", "summary": "X-ray, electron and neutron diffraction are first-Born scattering: the cross section is the Fourier transform of the scattering density, and inelastic neutron scattering measures the dynamic structure factor.", "map": "\\frac{d^2\\sigma}{d\\Omega dE}\\propto\\frac{k_f}{k_i}S(\\mathbf q,\\omega)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1818", "a": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "b": "08-condensed-matter/strongly-correlated-electrons/heavy-fermions-and-kondo-physics", "name": "Kondo effect as resonant scattering", "kind": "mechanism", "summary": "Below T_K conduction electrons scatter off the Kondo singlet with phase shift pi/2, the unitary limit; the Friedel sum rule ties the phase shift to the screened charge.", "map": "\\delta_0=\\pi/2;\\ G=\\frac{2e^2}{h}\\sin^2\\delta_0\\ (\\text{Kondo dot})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1819", "a": "04-quantum-physics/quantum-optics/cavity-and-circuit-qed", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures", "name": "Cavity QED with quantum dots", "kind": "shared object", "summary": "Single quantum dots in photonic-crystal nanocavities reach strong coupling with vacuum Rabi splitting, the solid-state realization of Jaynes-Cummings physics.", "map": "g>\\kappa,\\gamma", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1820", "a": "04-quantum-physics/quantum-optics/cavity-and-circuit-qed", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/transition-metal-dichalcogenides-and-excitons", "name": "Strong coupling of excitons to cavity photons", "kind": "mechanism", "summary": "Excitons in microcavities reach strong coupling, forming polaritons with vacuum Rabi splitting, the Jaynes-Cummings physics of cavity QED with a collective emitter.", "map": "E_\\pm=\\frac{E_x+E_c}{2}\\pm\\sqrt{g^2N+\\delta^2/4}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1821", "a": "04-quantum-physics/quantum-optics/cavity-optomechanics", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "Mechanical resonators are engineered phonons", "kind": "shared object", "summary": "Optomechanical resonators are phonon modes of nanostructures; phononic band gaps, Brillouin scattering and two-level-system damping are lattice-dynamics physics.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1822", "a": "04-quantum-physics/quantum-optics/quantized-light-and-photon-statistics", "b": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "name": "Electron quantum optics", "kind": "method transfer", "summary": "Single-electron sources, quantum point contacts as beam splitters and edge channels as waveguides let electronic HOM and HBT experiments mirror photon statistics; shot noise is the fermionic g2.", "map": "S_I=2eI\\,F,\\ F=\\frac{\\sum T_n(1-T_n)}{\\sum T_n}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1823", "a": "04-quantum-physics/quantum-optics/single-photon-sources-and-detectors", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures", "name": "Quantum-dot single-photon sources", "kind": "shared object", "summary": "Self-assembled semiconductor quantum dots are two-level emitters that, embedded in micropillars, give bright, pure and indistinguishable single photons.", "map": "g^{(2)}(0)\\ll1;\\ V_{\\rm HOM}\\to1", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1824", "a": "04-quantum-physics/quantum-optics/single-photon-sources-and-detectors", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/transition-metal-dichalcogenides-and-excitons", "name": "Quantum emitters in 2D semiconductors", "kind": "shared object", "summary": "Strain- and defect-localized excitons in monolayer WSe2 act as single-photon emitters, linking 2D-material excitonics to quantum-optical sources.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1825", "a": "04-quantum-physics/quantum-optics/single-photon-sources-and-detectors", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Superconducting single-photon detectors", "kind": "shared object", "summary": "SNSPDs and transition-edge sensors use photon-induced breaking of superconductivity (hotspots, steep R(T)) to count photons with high efficiency and low jitter.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1826", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "b": "09-astrophysics-and-cosmology/cosmology/dark-energy", "name": "Atom interferometry constrains screened dark energy", "kind": "method transfer", "summary": "Atoms in a high vacuum are unscreened test masses; interferometers near a source mass bound chameleon-type dark-energy forces.", "map": "a_{\\rm cham}\\ \\text{bounded at}\\ \\sim10^{-6}g", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1827", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "b": "09-astrophysics-and-cosmology/dark-matter", "name": "Clock networks as dark-matter detectors", "kind": "method transfer", "summary": "Networks of atomic clocks and magnetometers could detect transient frequency shifts from passing topological-defect dark matter, or oscillations from ultralight fields.", "map": "\\delta\\nu/\\nu\\propto\\phi^2/\\Lambda^2\\ \\text{during defect crossing}", "breaks": "", "confidence": "proposed", "strength": 2}
{"id": "C1828", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-detection", "name": "Astrocombs calibrate radial-velocity planet searches", "kind": "method transfer", "summary": "Optical frequency combs, developed for clock metrology, give spectrographs absolute, evenly spaced calibration lines for cm/s radial-velocity precision needed for Earth analogues.", "map": "\\nu_n=n f_{\\rm rep}+f_{\\rm ceo};\\ K_\\oplus\\approx0.09\\ \\mathrm{m/s}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1829", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "09-astrophysics-and-cosmology/cosmology", "name": "Quasar absorption tests of varying alpha", "kind": "method transfer", "summary": "Relative wavelengths of metal absorption lines in quasar spectra, with laboratory sensitivity coefficients, constrain cosmic variation of the fine-structure constant; reported variations remain contested.", "map": "\\omega_z=\\omega_0+q\\left[\\left(\\frac{\\alpha_z}{\\alpha_0}\\right)^2-1\\right]", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1830", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "Hydrogen atomic physics sets recombination", "kind": "mechanism", "summary": "Recombination is delayed beyond Saha equilibrium because Lyman-alpha photons are trapped; the 2s-1s two-photon decay and Lyman-alpha redshifting control the last-scattering surface and thus the CMB acoustic scale.", "map": "\\frac{dx_e}{dt}=-C\\left[\\alpha_Bnx_e^2-\\beta_B(1-x_e)e^{-h\\nu_\\alpha/k_BT}\\right],\\ C=\\frac{\\Lambda_{2s1s}+\\Lambda_\\alpha}{\\Lambda_{2s1s}+\\Lambda_\\alpha+\\beta_B}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1831", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "09-astrophysics-and-cosmology/dark-matter/astrophysical-evidence-for-dark-matter", "name": "21-cm rotation curves trace dark halos", "kind": "method transfer", "summary": "Neutral-hydrogen 21-cm emission extends rotation curves far beyond stellar disks, where flat curves give the cleanest galactic evidence for dark matter.", "map": "v_c^2=GM(<r)/r=\\text{const}\\Rightarrow M\\propto r", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1832", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "09-astrophysics-and-cosmology/galaxies/galaxy-clusters", "name": "Highly charged ion spectroscopy of cluster gas", "kind": "method transfer", "summary": "X-ray lines of He- and H-like iron give temperature, abundance and turbulent velocity of intracluster gas; Hitomi's resolved Fe XXV lines measured low turbulence in Perseus.", "map": "\\sigma_v^2=\\sigma_{\\rm th}^2+\\sigma_{\\rm turb}^2,\\ \\sigma_{\\rm th}=\\sqrt{k_BT/m_{\\rm Fe}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1833", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "09-astrophysics-and-cosmology/galaxies/high-redshift-universe-and-reionization", "name": "21-cm hyperfine line and Lyman-alpha probe reionization", "kind": "method transfer", "summary": "The hydrogen hyperfine transition, its spin temperature set by collisions and Lyman-alpha pumping (Wouthuysen-Field), maps neutral gas at cosmic dawn; Gunn-Peterson Lyman-alpha absorption marks the end of reionization.", "map": "\\nu_{21}=1420.405\\ \\mathrm{MHz};\\ \\delta T_b\\propto x_{\\rm HI}\\left(1-\\frac{T_{\\rm CMB}}{T_S}\\right)\\sqrt{1+z}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1834", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/multi-messenger-astronomy", "name": "Lanthanide atomic data for kilonova spectra", "kind": "method transfer", "summary": "Kilonova light curves and spectra depend on the dense line forests of lanthanides and on identified features such as Sr II, requiring atomic-structure calculations of open f-shell ions.", "map": "", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1835", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-atmospheres", "name": "Line lists for exoplanet atmosphere spectra", "kind": "method transfer", "summary": "Interpreting transmission and emission spectra needs ro-vibrational line lists of H2O, CH4, CO2 and metal atoms computed from molecular quantum mechanics.", "map": "\\delta(\\lambda)\\approx\\frac{R_p^2+2R_pN_HH}{R_\\star^2},\\ \\sigma(\\lambda)\\ \\text{from line lists}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1836", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "name": "Atomic opacities and the solar abundance problem", "kind": "method transfer", "summary": "Stellar interiors depend on computed atomic opacities; measured iron opacity at solar-interior conditions exceeds theory, a candidate resolution of the mismatch between helioseismology and low solar metal abundances.", "map": "\\nabla_{\\rm rad}=\\frac{3\\kappa LP}{16\\pi acGMT^4}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C1837", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure", "name": "Fuzzy dark matter as a cosmic matter wave", "kind": "analogy", "summary": "Ultralight bosonic dark matter obeys the Schrodinger-Poisson system, a Gross-Pitaevskii equation with self-gravity; galaxy halos develop solitonic cores and granular interference like condensates.", "map": "i\\hbar\\partial_t\\psi=-\\frac{\\hbar^2}{2m}\\nabla^2\\psi+m\\Phi\\psi,\\ \\nabla^2\\Phi=4\\pi Gm|\\psi|^2", "breaks": "Interaction is long-range self-gravity rather than contact scattering; occupation is classical and not reached by thermal condensation; no trap or superfluid flow measurement.", "confidence": "current research", "strength": 3}
{"id": "C1838", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Fermi pressure from trapped atoms to white dwarfs", "kind": "mechanism", "summary": "Degeneracy pressure measured in trapped Fermi gases is the same Pauli effect that supports white dwarfs and neutron stars against gravity.", "map": "P=\\frac{(3\\pi^2)^{2/3}\\hbar^2}{5m}n^{5/3}\\ \\text{(non-relativistic)}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1839", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Superfluid vortices and pulsar glitches", "kind": "mechanism", "summary": "Neutron-star interiors are superfluid; rotation is carried by quantized vortices whose sudden unpinning from the crust is the leading explanation of pulsar glitches, the physics of vortex lattices in rotating BECs.", "map": "\\oint\\mathbf v_s\\cdot d\\mathbf l=\\frac{h}{2m_n};\\ n_v=\\frac{4m_n\\Omega}{h}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1840", "a": "04-quantum-physics/atomic-molecular-and-optical-physics/ultracold-molecules", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks", "name": "Cold molecular collisions and astrochemistry", "kind": "mechanism", "summary": "Interstellar chemistry at 10-100 K proceeds by barrierless ion-molecule reactions and tunnelling, the same low-temperature collision physics that cold-molecule experiments resolve state by state.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1841", "a": "04-quantum-physics/foundations-of-quantum-mechanics/bell-nonlocality", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Cosmological Bell inequalities", "kind": "method transfer", "summary": "Bell-type observables built from primordial correlators could in principle reveal the quantum origin of structure, though decaying modes make realistic tests extremely hard.", "map": "", "breaks": "", "confidence": "proposed", "strength": 1}