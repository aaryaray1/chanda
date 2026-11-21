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

# Packet 04-5 (89 records)

{"id": "C1842", "a": "04-quantum-physics/foundations-of-quantum-mechanics/bell-nonlocality", "b": "09-astrophysics-and-cosmology/galaxies/active-galactic-nuclei-and-supermassive-black-holes", "name": "Quasars choose settings in cosmic Bell tests", "kind": "method transfer", "summary": "Light from high-redshift quasars emitted billions of years ago set measurement bases in a Bell test, pushing any freedom-of-choice loophole back to the early universe.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1843", "a": "04-quantum-physics/foundations-of-quantum-mechanics/decoherence-and-quantum-to-classical", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Quantum-to-classical transition of cosmic fluctuations", "kind": "mechanism", "summary": "Large squeezing makes primordial fluctuations effectively classical stochastic fields, and environmental decoherence selects field amplitude as pointer basis; whether a quantum signature survives is debated.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1844", "a": "04-quantum-physics/open-and-many-body-quantum-dynamics/lindblad-master-equations", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "Density-matrix kinetics of relic neutrinos", "kind": "method transfer", "summary": "Neutrino decoupling with oscillations and collisions is computed with matrix-valued quantum kinetic equations, giving N_eff = 3.044 used in CMB fits.", "map": "\\dot\\rho_p=-i[H_p,\\rho_p]+C[\\rho]", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1845", "a": "04-quantum-physics/quantum-information-and-computation/entanglement-theory", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients", "name": "Many-body entanglement in collective neutrino oscillations", "kind": "method transfer", "summary": "Neutrino-neutrino forward scattering in supernovae makes flavour evolution an interacting spin model; quantum-information tools quantify entanglement beyond mean-field treatments.", "map": "H=\\sum_p\\omega_p\\mathbf B\\cdot\\mathbf J_p+\\frac{\\mu}{N}\\sum_{p,q}(1-\\cos\\theta_{pq})\\mathbf J_p\\cdot\\mathbf J_q", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1846", "a": "04-quantum-physics/quantum-mechanics-core/approximation-methods", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "name": "WKB asymptotics of solar oscillations", "kind": "method transfer", "summary": "High-order p-mode frequencies follow from JWKB analysis of the wave equation in the solar cavity, giving the large-separation formula used to invert sound speed.", "map": "\\nu_{n\\ell}\\approx\\Delta\\nu\\left(n+\\frac\\ell2+\\epsilon\\right),\\ \\Delta\\nu=\\left(2\\int_0^R\\frac{dr}{c_s}\\right)^{-1}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1847", "a": "04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Bounce instantons and false-vacuum decay", "kind": "method transfer", "summary": "The Euclidean bounce that computes tunnelling rates in quantum mechanics gives bubble nucleation in field theory and gravity, central to old and eternal inflation and vacuum stability.", "map": "\\Gamma/V\\approx Ae^{-B/\\hbar},\\ B=S_E[\\phi_{\\rm bounce}]-S_E[\\phi_{\\rm fv}]", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1848", "a": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "b": "09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure", "name": "Partial-wave cross sections of self-interacting dark matter", "kind": "method transfer", "summary": "Velocity-dependent self-interaction cross sections for Yukawa potentials are computed by partial-wave and Born methods; resonant and classical regimes control halo cores.", "map": "\\sigma_T=\\frac{4\\pi}{k^2}\\sum_\\ell(\\ell+1)\\sin^2(\\delta_{\\ell+1}-\\delta_\\ell)", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1849", "a": "04-quantum-physics/quantum-mechanics-core/scattering-theory", "b": "09-astrophysics-and-cosmology/dark-matter/indirect-detection", "name": "Sommerfeld enhancement of dark-matter annihilation", "kind": "mechanism", "summary": "Slow dark-matter particles exchanging a light mediator have enhanced annihilation, the wavefunction-at-origin factor of Coulomb or Yukawa scattering, with resonances from near-threshold bound states.", "map": "S=\\frac{\\pi\\alpha/v}{1-e^{-\\pi\\alpha/v}}\\ (\\text{Coulomb})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1850", "a": "04-quantum-physics/quantum-optics/cavity-optomechanics", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Mechanical quantum sensors for dark matter", "kind": "method transfer", "summary": "Levitated and clamped mechanical sensors operated near the quantum limit can detect impulses or oscillating forces from heavy or ultralight dark matter.", "map": "", "breaks": "", "confidence": "proposed", "strength": 2}
{"id": "C1851", "a": "04-quantum-physics/quantum-optics/quantized-light-and-photon-statistics", "b": "09-astrophysics-and-cosmology/cosmology/dark-energy", "name": "Zero-point energy and the cosmological-constant problem", "kind": "shared object", "summary": "Summing field-mode zero-point energies to a high cutoff predicts a vacuum energy far above the observed dark-energy density; the Casimir effect does not settle the issue because it measures energy differences.", "map": "\\rho_{\\rm vac}\\sim\\int^{\\Lambda}\\frac{d^3k}{(2\\pi)^3}\\frac{\\hbar\\omega_k}{2}\\sim\\frac{\\Lambda^4}{16\\pi^2}\\gg\\rho_\\Lambda\\approx(2.24\\ \\mathrm{meV})^4", "breaks": "Casimir forces arise from charge fluctuations and do not measure absolute vacuum energy; renormalization makes the naive cutoff estimate unphysical.", "confidence": "established", "strength": 2}
{"id": "C1852", "a": "04-quantum-physics/quantum-optics/quantized-light-and-photon-statistics", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "name": "Intensity interferometry from stars to quantum optics", "kind": "historical", "summary": "Hanbury Brown and Twiss measured stellar diameters from intensity correlations; explaining the photon bunching behind the effect led Glauber to the quantum theory of optical coherence.", "map": "g^{(2)}(\\tau)=1+|g^{(1)}(\\tau)|^2\\ \\text{(thermal light)}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1853", "a": "04-quantum-physics/quantum-optics/single-photon-sources-and-detectors", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Superconducting photon sensors for sub-GeV dark matter", "kind": "method transfer", "summary": "SNSPDs and transition-edge sensors developed for single-photon counting have meV thresholds, letting them detect electron recoils or absorption from light dark matter.", "map": "E_{\\rm th}\\sim\\mathrm{meV};\\ m_\\chi\\gtrsim\\mathrm{keV}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1854", "a": "04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Primordial perturbations are squeezed states", "kind": "identity", "summary": "Inflation stretches vacuum fluctuations into extremely squeezed two-mode states of opposite-momentum modes; the growing mode's phase coherence underlies CMB acoustic peaks.", "map": "|\\psi_k\\rangle=\\frac{1}{\\cosh r_k}\\sum_n(-e^{2i\\phi_k}\\tanh r_k)^n|n_{\\mathbf k},n_{-\\mathbf k}\\rangle,\\ r_k\\sim\\ln(aH/k)", "breaks": "", "confidence": "established", "strength": 3}
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