You are the foundations-physicist, the specialist for 00 (Foundations) in this physics knowledge base.

# Specialist review brief (one packet per run)

You are the specialist for the branch named above. Below this brief are your branch's notes (the codex sections for every node in the packet) and the packet itself, one proposed connection per line, each with at least one end in your branch. Check every one from **your branch's side**:
- Is the physics right?
- Is the stated kind right (identity, mechanism, analogy, duality, method transfer, shared object, historical)?
- Is the summary accurate, the confidence label honest and the strength fair?
- Are the node paths on your side the most fitting notes?

Work from the notes below and your own knowledge. Do not run commands or search the folder. Read a node README only if the notes below are not enough, and at most 3 of them.

## Answer: JSON Lines ONLY
Give one line per packet record, in packet order. No prose, no headings, no code fences; anything else is discarded.
- `{"id": "C0123", "verdict": "confirm"}` when it is right as written.
- `{"id": "C0123", "verdict": "revise", "reason": "<≤25 words>", "fix": {"summary": "...", "kind": "...", "confidence": "...", "strength": 2, "breaks": "...", "map": "...", "a": "<better path>", "b": "<better path>"}}`. Include only the fields that change.
- `{"id": "C0123", "verdict": "reject", "reason": "<≤25 words: the physics error, or why it is trivial or false>"}`.

After the verdicts you may add up to 8 important connections touching your branch that the packet lacks, as `{"verdict": "add", "record": {"a": "<node path>", "b": "<node path>", "name": "<≤60 chars>", "kind": "...", "summary": "<≤45 words>", "map": "...", "breaks": "<required for analogy>", "confidence": "established|current research|proposed", "strength": 3|2|1, "sources": []}}`.

Be strict but fair. Reject only real errors or trivial links; prefer revise when a connection is real but mis-stated.


---

# Your branch notes: the codex sections for the nodes in this packet

## Field overview · `knowledge/00-foundations`

> **Specialist:** `foundations-physicist` · **arXiv:** math-ph, physics.comp-ph, physics.data-an, physics.hist-ph, physics.ed-ph · **Literature source:** OpenAlex + arXiv

#### What this field studies
Every physics branch rests on the same foundations: the mathematics used to state laws, the symmetries that constrain them, the numerical methods that solve them when pen and paper fail, the statistics that connect them to data, the units in which results are reported, and the history and philosophy that explain why physics looks the way it does. Questions about *how* to solve, estimate, measure or reason belong here; questions about a specific system belong to its field.

#### Conventions used across the knowledge base
- **SI units by default.** Natural units ($\hbar=c=1$) in particle physics, geometrized units ($G=c=1$) in GR, Gaussian units in some EM and plasma texts — always state the system and convert when comparing.
- **Constants:** CODATA 2022 values from NIST, stored in [codata-2022.md](knowledge/00-foundations/units-and-constants/codata-2022.md) and searchable with `python -I scripts/physlib.py constants <name>`.
- **Uncertainties:** quote standard (1σ) uncertainties as $x = 1.234(5)$ or $1.234\pm0.005$; state whether statistical, systematic or combined.
- **Vectors** bold or with arrows; Einstein summation over repeated indices unless noted.

#### Historical spine
1687 *Principia* · 1736–1788 Euler and Lagrange's analytical mechanics · 1822 Fourier analysis · 1828 Green's functions · 1854 Riemannian geometry · 1873 Lie groups · 1918 Noether's theorem · 1925–32 Hilbert space QM (von Neumann) · 1946 ENIAC; 1953 Metropolis Monte Carlo · 1960 Wigner's "unreasonable effectiveness" · 1972 "More is different" · 2019 SI redefinition · 2024 Nobel Prize for physics-inspired neural networks.

#### Canonical textbooks
- Boas, *Mathematical Methods in the Physical Sciences* — undergraduate standard.
- Arfken, Weber & Harris, *Mathematical Methods for Physicists*; Riley, Hobson & Bence, *Mathematical Methods for Physics and Engineering*.
- Georgi, *Lie Algebras in Particle Physics*; Zee, *Group Theory in a Nutshell for Physicists*.
- Press et al., *Numerical Recipes*; Newman, *Computational Physics*; Landau & Binder, *A Guide to Monte Carlo Simulations in Statistical Physics*.
- Taylor, *An Introduction to Error Analysis*; Barlow, *Statistics*; Sivia & Skilling, *Data Analysis: A Bayesian Tutorial*.
- Kuhn, *The Structure of Scientific Revolutions*; Pais, *Subtle is the Lord*; Maudlin, *Philosophy of Physics* (2 vols.).

#### How the specialist works here
Pick the right tool before computing: exploit symmetry, nondimensionalize, estimate orders of magnitude, then solve analytically or numerically with an explicit check (convergence, conservation laws, known limits). For data questions, write the likelihood first.

## Computational physics · `knowledge/00-foundations/computational-physics`

#### Overview
Simulation is the third pillar of physics alongside theory and experiment. The craft is choosing a method whose errors you understand: discretization error, statistical error, finite-size effects, and the sign problem. Every result needs a convergence test and a check against a known limit.

#### Conceptual spine
1. Discretize → solve algebraic problem → estimate error → refine until converged.
2. Stochastic methods trade bias for variance; errors fall as $N^{-1/2}$.
3. Exploit structure (symplecticity, sparsity, low entanglement) to beat brute force.

#### Key equations
$$\text{Euler: }y_{n+1}=y_n+hf(y_n)\ (\mathcal O(h)),\qquad \text{RK4: }\mathcal O(h^4),\qquad \sigma_{\bar A}=\sqrt{\frac{2\tau_{\text{int}}}{N}}\,\sigma_A$$

#### Open problems
- The fermion sign problem (NP-hard in general).
- Trustworthy uncertainty quantification for ML surrogates in physics.

#### Connections
- [Lattice field theory](knowledge/06-particle-physics/quantum-field-theory/lattice-field-theory/README.md) · [Density functional theory](knowledge/08-condensed-matter/crystals-and-electronic-structure/density-functional-theory/README.md) · [Numerical relativity](knowledge/05-relativity-and-gravitation/general-relativity/numerical-relativity/README.md)

### Machine learning for physics · `knowledge/00-foundations/computational-physics/machine-learning-for-physics`

**Scope.** Physics-informed neural networks (PINNs), neural operators, equivariant networks, neural-network quantum states, generative models for sampling (normalizing flows), symbolic regression, ML for experiment control, and the statistical physics of learning (Hopfield, Boltzmann machines).

**Core ideas.**
- Build symmetries and conservation laws into architectures (equivariance) rather than hoping the network learns them.
- PINNs penalize the PDE residual in the loss, combining data and equations.
- ML outputs are hypotheses: validate against held-out physics (limits, conservation, independent simulations).

**Key equations.**
$$\mathcal L=\frac1N\sum_i|u_\theta(x_i)-u_i|^2+\lambda\frac1M\sum_j|\mathcal N u_\theta\,(x_j)|^2$$

**See also.** [Statistical physics of learning](knowledge/03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/statistical-physics-of-learning/README.md) · [ML in HEP](knowledge/06-particle-physics/collider-and-experimental-particle-physics/machine-learning-in-hep/README.md)

### Molecular dynamics · `knowledge/00-foundations/computational-physics/molecular-dynamics`

**Scope.** Lennard-Jones and empirical force fields, Verlet integration, periodic boundaries and Ewald sums, thermostats (Nosé–Hoover, Langevin) and barostats, Car–Parrinello and Born–Oppenheimer ab initio MD, machine-learned interatomic potentials, enhanced sampling (metadynamics).

**Core ideas.**
- Time averages along ergodic trajectories estimate ensemble averages.
- Long-range Coulomb forces need Ewald/PME summation.
- ML potentials give near-DFT accuracy at near-classical cost.

**Key equations.**
$$V_{\text{LJ}}(r)=4\epsilon\left[\left(\frac\sigma r\right)^{12}-\left(\frac\sigma r\right)^6\right]$$

**See also.** [Molecular biophysics](knowledge/11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding/README.md) · [Glasses and jamming](knowledge/08-condensed-matter/soft-matter/glasses-and-jamming/README.md)

### Monte Carlo methods · `knowledge/00-foundations/computational-physics/monte-carlo-methods`

**Scope.** Random sampling and $N^{-1/2}$ errors, importance sampling, Metropolis–Hastings, detailed balance, autocorrelation and critical slowing down, Wolff/Swendsen–Wang clusters, parallel tempering, Hybrid Monte Carlo, variational and diffusion QMC, the sign problem.

**Core ideas.**
- High-dimensional integrals: Monte Carlo error is independent of dimension.
- A Markov chain obeying detailed balance with respect to $e^{-\beta E}$ samples the Boltzmann distribution.
- Near critical points, local updates slow down ($\tau\sim\xi^z$); cluster moves cure it for spin models.

**Key equations.**
$$P_{\text{acc}}(x\to x')=\min\!\left(1,e^{-\beta[E(x')-E(x)]}\right)$$

**See also.** [Ising model](knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/ising-model-and-lattice-models/README.md) · [Event generators](knowledge/06-particle-physics/collider-and-experimental-particle-physics/monte-carlo-event-generators/README.md)

### Numerical methods for ODEs and PDEs · `knowledge/00-foundations/computational-physics/numerical-methods-for-odes-and-pdes`

**Scope.** Explicit/implicit schemes, Runge–Kutta, adaptive step size, stiffness, symplectic (leapfrog/Verlet) integrators, CFL condition, von Neumann stability analysis, finite elements, finite volumes for conservation laws, spectral/pseudospectral methods, multigrid, FFT.

**Core ideas.**
- Order of accuracy, stability and conservation are separate properties; check all three.
- Symplectic integrators conserve a nearby Hamiltonian — no secular energy drift in long orbital runs.
- Explicit wave solvers need $c\Delta t/\Delta x\le1$ (CFL).

**Key equations.**
$$x_{n+1}=x_n+v_n\Delta t+\tfrac12a_n\Delta t^2,\quad v_{n+1}=v_n+\tfrac12(a_n+a_{n+1})\Delta t\ (\text{velocity Verlet})$$

**See also.** [Hamiltonian mechanics](knowledge/01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics/README.md) · [Turbulence](knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/turbulence/README.md)

### Tensor network methods · `knowledge/00-foundations/computational-physics/tensor-network-methods`

**Scope.** Matrix product states and operators, DMRG, TEBD for time evolution, PEPS for 2D, MERA and holography, bond dimension and truncation error, tensor-network contraction for simulating quantum circuits.

**Core ideas.**
- Area-law entanglement makes ground states of gapped 1D systems efficiently representable by MPS.
- DMRG variationally optimizes an MPS — the most accurate method for 1D quantum systems.
- Time evolution grows entanglement, limiting accessible times.

**Key equations.**
$$|\psi\rangle=\sum_{\{s\}}\mathrm{Tr}\left(A^{s_1}A^{s_2}\cdots A^{s_N}\right)|s_1s_2\cdots s_N\rangle,\qquad S\le\log\chi$$

**See also.** [Entanglement theory](knowledge/04-quantum-physics/quantum-information-and-computation/entanglement-theory/README.md) · [Numerical many-body methods](knowledge/08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods/README.md)

## History and philosophy of physics · `knowledge/00-foundations/history-and-philosophy-of-physics`

#### Overview
History explains why physics has the concepts it has; philosophy examines what those concepts mean (space, time, probability, causation, laws, emergence) and how theories are confirmed. Physics education research applies the methods of physics to how physics is learned — and finds that interactive engagement beats lecturing.

#### Connections
- [Foundations of quantum mechanics](knowledge/04-quantum-physics/foundations-of-quantum-mechanics/README.md) · [Spontaneous symmetry breaking (emergence)](knowledge/00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking/README.md)

### History of physics · `knowledge/00-foundations/history-and-philosophy-of-physics/history-of-physics`

**Scope.** Galileo and Newton, energy and thermodynamics in the 19th century, Maxwell's unification, the 1905 *annus mirabilis*, the old and new quantum theory, nuclear physics and the Manhattan Project, the postwar particle zoo and the Standard Model, big science (CERN, LIGO), women and under-represented groups in physics history.

**Core ideas.**
- Revolutions rarely discard old theories — they find their domain of validity (Newton as the $v\ll c$, $S\gg\hbar$ limit).
- Experiment and instrumentation (spectroscopy, cloud chambers, accelerators, lasers) drove most conceptual change.
- Read primary sources: the original papers are often clearer about motivation than textbooks.

**Key equations.** $E=mc^2$ (1905), $E=h\nu$ (1900/1905), $\lambda=h/p$ (1924) — each marked a conceptual turn.

**See also.** Historical spines in each field README, e.g. [Particle Physics](knowledge/06-particle-physics/README.md), [Quantum Physics](knowledge/04-quantum-physics/README.md).

### Philosophy of physics · `knowledge/00-foundations/history-and-philosophy-of-physics/philosophy-of-physics`

**Scope.** Substantivalism vs. relationism about spacetime, the hole argument, the arrow of time and the past hypothesis, probability in statistical mechanics and QM, the measurement problem, gauge as redundancy, reduction vs. emergence, scientific realism, underdetermination, naturalness and fine-tuning arguments.

**Core ideas.**
- Microscopic laws are (nearly) time-symmetric; the thermodynamic arrow traces to a low-entropy early universe.
- Gauge symmetries are descriptive redundancy — only gauge-invariant quantities are physical.
- "More is different": higher-level laws can be autonomous even when reducible in principle.

**Key equations.** $S=k_B\ln W$ — the bridge between microscopic counting and macroscopic irreversibility.

**See also.** [Measurement problem](knowledge/04-quantum-physics/foundations-of-quantum-mechanics/measurement-problem-and-interpretations/README.md) · [Laws of thermodynamics](knowledge/03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/laws-of-thermodynamics/README.md)

## Mathematical methods · `knowledge/00-foundations/mathematical-methods`

#### Overview
Most of physics reduces to a few mathematical structures: vector spaces and their operators (quantum mechanics, normal modes), linear differential equations and their Green's functions (electrostatics, waves, diffusion), analytic functions (dispersion relations, contour integrals), and tensors on manifolds (relativity, continuum mechanics). Fluency here is what makes the rest of the tree readable.

#### Conceptual spine
1. Linearity → superposition → expand in eigenfunctions of a self-adjoint operator.
2. Green's function = response to a point source; solution = source convolved with it.
3. Analyticity ↔ causality (Kramers–Kronig).
4. Coordinate-free (tensor) statements are the ones with physical meaning.

#### Key equations
$$\mathcal L G(\mathbf x,\mathbf x')=\delta(\mathbf x-\mathbf x'),\qquad u(\mathbf x)=\int G(\mathbf x,\mathbf x')f(\mathbf x')\,d\mathbf x'$$
$$\oint_Cf(z)\,dz=2\pi i\sum\mathrm{Res}f,\qquad \mathrm{Re}\,\chi(\omega)=\frac1\pi\,\mathcal P\!\!\int\frac{\mathrm{Im}\,\chi(\omega')}{\omega'-\omega}d\omega'$$

#### Open problems
- Rigorous foundations for quantum field theory (constructive QFT, path-integral measures).
- Global regularity of 3D Navier–Stokes (Clay problem).

#### Connections
- [Symmetry and group theory](knowledge/00-foundations/symmetry-and-group-theory/README.md) · [Quantum mechanics formalism](knowledge/04-quantum-physics/quantum-mechanics-core/README.md) · [General relativity](knowledge/05-relativity-and-gravitation/general-relativity/README.md)

### Complex analysis and special functions · `knowledge/00-foundations/mathematical-methods/complex-analysis-and-special-functions`

**Scope.** Cauchy–Riemann conditions, residue theorem, branch cuts, conformal maps (2D potential flow, electrostatics), Kramers–Kronig relations, steepest descent and saddle-point methods, gamma and zeta functions, Legendre, Bessel, Hermite, Laguerre functions, hypergeometric functions.

**Core ideas.**
- Real integrals often become easy as contour integrals closed in the complex plane.
- Causal response functions are analytic in the upper half-plane → real and imaginary parts are linked.
- Special functions are eigenfunctions of the Laplacian (or similar operators) in separable coordinates.

**Key equations.**
$$\Gamma(z+1)=z\Gamma(z),\quad n!\approx\sqrt{2\pi n}\left(\frac ne\right)^n,\qquad \int_{-\infty}^{\infty}e^{-ax^2}dx=\sqrt{\pi/a}$$

**See also.** [Linear response](knowledge/03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation/README.md)

### Differential equations and Green's functions · `knowledge/00-foundations/mathematical-methods/differential-equations-and-greens-functions`

**Scope.** Linear ODEs, series (Frobenius) solutions, Sturm–Liouville problems, Laplace/Poisson, wave, diffusion and Helmholtz equations, separation of variables, Fourier and Laplace transforms, Green's functions with boundary conditions, retarded/advanced propagators, method of characteristics.

**Core ideas.**
- PDE type (elliptic, hyperbolic, parabolic) determines which boundary/initial data give well-posed problems.
- Sturm–Liouville eigenfunctions form complete orthogonal sets — Fourier series, Legendre, Bessel expansions.
- Causality picks the retarded Green's function for wave problems.

**Key equations.**
$$\nabla^2G=-\delta^3(\mathbf r)\Rightarrow G=\frac{1}{4\pi r},\qquad \left(\nabla^2-\frac{1}{c^2}\partial_t^2\right)G=-\delta^4\Rightarrow G_{\text{ret}}=\frac{\delta(t-r/c)}{4\pi r}$$

**See also.** [Electrostatics and boundary-value problems](knowledge/02-electromagnetism-and-optics/electrostatics-and-magnetostatics/electrostatics-and-boundary-value-problems/README.md) · [Numerical methods for ODEs and PDEs](knowledge/00-foundations/computational-physics/numerical-methods-for-odes-and-pdes/README.md)

### Linear algebra and Hilbert spaces · `knowledge/00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces`

**Scope.** Inner products, orthonormal bases, Gram–Schmidt, Hermitian and unitary operators, diagonalization, singular value decomposition, tensor products, $L^2$ function spaces, completeness relations, bounded vs. unbounded operators, rigged Hilbert spaces (for continuum states).

**Core ideas.**
- Self-adjoint operators have real eigenvalues and complete orthogonal eigenbases (spectral theorem) — observables in QM, normal modes in mechanics.
- Commuting operators share eigenbases; this is how quantum numbers are chosen.
- Tensor products of spaces describe composite systems; dimension multiplies.

**Key equations.**
$$A=\sum_n\lambda_n|n\rangle\langle n|,\qquad \sum_n|n\rangle\langle n|=\mathbb 1,\qquad \dim(\mathcal H_A\otimes\mathcal H_B)=\dim\mathcal H_A\cdot\dim\mathcal H_B$$

**See also.** [Postulates and formalism of QM](knowledge/04-quantum-physics/quantum-mechanics-core/postulates-and-formalism/README.md) · [Normal modes](knowledge/01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes/README.md)

### Tensors and differential geometry · `knowledge/00-foundations/mathematical-methods/tensors-and-differential-geometry`

**Scope.** Covariant and contravariant indices, metric tensor, Christoffel symbols, covariant derivative, parallel transport, geodesics, Riemann/Ricci tensors, Killing vectors, differential forms and Stokes' theorem, fibre bundles (gauge fields as connections).

**Core ideas.**
- Tensor equations true in one coordinate system are true in all.
- Curvature measures the failure of parallel transport around closed loops.
- Gauge fields are connections on fibre bundles; field strengths are their curvature — the same structure as gravity.

**Key equations.**
$$\nabla_\mu V^\nu=\partial_\mu V^\nu+\Gamma^\nu_{\mu\lambda}V^\lambda,\qquad \Gamma^\lambda_{\mu\nu}=\tfrac12g^{\lambda\sigma}(\partial_\mu g_{\sigma\nu}+\partial_\nu g_{\sigma\mu}-\partial_\sigma g_{\mu\nu})$$

**See also.** [Einstein field equations](knowledge/05-relativity-and-gravitation/general-relativity/einstein-field-equations/README.md) · [Gauge theories](knowledge/06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills/README.md)

## Measurement and data analysis · `knowledge/00-foundations/measurement-and-data-analysis`

#### Overview
A measurement is only as meaningful as its uncertainty. This branch covers the statistics of estimating parameters and testing hypotheses (frequentist and Bayesian), propagating errors, separating statistical from systematic effects, and the instruments that transduce physical quantities into data.

#### Conceptual spine
1. Model the measurement: $x=\mu+\text{noise}$; write the likelihood $L(\theta)=p(\text{data}|\theta)$.
2. Estimate (maximum likelihood or posterior), then quote an interval with its coverage or credibility.
3. Systematics enter as nuisance parameters — profile or marginalize them.
4. Blind analyses and pre-registration prevent bias; replication is the final check.

#### Key equations
$$\sigma_f^2=\sum_{i,j}\frac{\partial f}{\partial x_i}\frac{\partial f}{\partial x_j}V_{ij},\qquad \chi^2=\sum_i\frac{(y_i-f(x_i;\theta))^2}{\sigma_i^2},\qquad q_0=-2\ln\frac{L(0,\hat{\hat\theta})}{L(\hat\mu,\hat\theta)}$$

#### Open problems
- Reproducibility and the "look-elsewhere effect" in large searches.
- Uncertainty quantification for machine-learned analyses.

#### Connections
- [Collider and experimental physics](knowledge/06-particle-physics/collider-and-experimental-particle-physics/README.md) · [Units and constants](knowledge/00-foundations/units-and-constants/README.md)

### Detectors and instrumentation · `knowledge/00-foundations/measurement-and-data-analysis/detectors-and-instrumentation`

**Scope.** Transducers, Johnson–Nyquist and shot noise, 1/f noise, signal-to-noise ratio, bandwidth, lock-in amplification, phase-sensitive detection, photodiodes and photomultipliers, bolometers and transition-edge sensors, SQUID readout, quantum-limited amplifiers, calibration.

**Core ideas.**
- Fundamental noise floors: thermal ($4k_BTR\Delta f$), shot ($2qI\Delta f$), quantum (half a photon per mode).
- Modulating the signal and demodulating (lock-in) moves it away from 1/f noise.
- Every instrument needs a calibration chain traceable to SI standards.

**Key equations.**
$$\langle V_n^2\rangle=4k_BTR\,\Delta f,\qquad \langle I_n^2\rangle=2qI\,\Delta f$$

**See also.** [Particle detectors](knowledge/06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers/README.md) · [Josephson junctions and SQUIDs](knowledge/08-condensed-matter/superconductivity/josephson-effect-and-squids/README.md)

### Statistical inference in physics · `knowledge/00-foundations/measurement-and-data-analysis/statistical-inference-in-physics`

**Scope.** Likelihood principle, maximum-likelihood estimators, Fisher information and Cramér–Rao bound, Neyman confidence belts, Feldman–Cousins, CLs, profile likelihood and Wilks' theorem, Bayesian posteriors and priors, MCMC sampling, model comparison (Bayes factors, AIC/BIC), look-elsewhere effect, simulation-based inference.

**Core ideas.**
- Frequentist intervals have guaranteed coverage; Bayesian intervals express degrees of belief given a prior — report which.
- Wilks: $-2\ln\lambda$ is asymptotically $\chi^2$-distributed, giving fast significance estimates.
- Searching many places inflates false positives; correct for trials.

**Key equations.**
$$p(\theta|D)=\frac{p(D|\theta)p(\theta)}{p(D)},\qquad \mathrm{Var}(\hat\theta)\ge\frac{1}{I(\theta)},\qquad Z=\sqrt{q_0}$$

**See also.** [Cosmological parameter inference](knowledge/09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history/README.md)

### Uncertainty and error propagation · `knowledge/00-foundations/measurement-and-data-analysis/uncertainty-and-error-propagation`

**Scope.** Random vs. systematic errors, Type A and Type B evaluations (GUM), standard and expanded uncertainty, linear error propagation with covariances, Monte Carlo propagation, weighted means, outlier handling, significant figures in reporting.

**Core ideas.**
- Independent uncertainties add in quadrature; correlated ones need the covariance matrix.
- Relative uncertainties add in quadrature for products and quotients.
- The weighted mean of measurements $x_i\pm\sigma_i$ has weights $1/\sigma_i^2$; a large $\chi^2$/dof signals underestimated errors.

**Key equations.**
$$\bar x=\frac{\sum x_i/\sigma_i^2}{\sum1/\sigma_i^2},\qquad \sigma_{\bar x}=\left(\sum\frac1{\sigma_i^2}\right)^{-1/2},\qquad \frac{\sigma_{xy}}{xy}=\sqrt{\left(\frac{\sigma_x}{x}\right)^2+\left(\frac{\sigma_y}{y}\right)^2}$$

**See also.** [Statistical inference](knowledge/00-foundations/measurement-and-data-analysis/statistical-inference-in-physics/README.md) · [Fundamental constants](knowledge/00-foundations/units-and-constants/fundamental-constants/README.md)

## Symmetry and group theory · `knowledge/00-foundations/symmetry-and-group-theory`

#### Overview
Symmetries determine conservation laws (Noether), classify particles and states (representation theory), restrict allowed interactions (gauge principle, selection rules) and, when broken spontaneously, produce massless Goldstone modes, the Higgs mechanism and most phases of matter. "More is different": broken symmetry is how emergent order arises.

#### Conceptual spine
1. Symmetry = transformation leaving the action invariant.
2. Continuous symmetries → conserved charges; their generators form a Lie algebra.
3. Physical states carry irreducible representations — particles are labelled by mass and spin (Wigner).
4. Ground states can break a symmetry the laws respect → order parameter, Goldstone bosons, or (if gauged) massive gauge bosons.

#### Key equations
$$\partial_\mu j^\mu=0,\quad j^\mu=\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\delta\phi-K^\mu,\qquad [T^a,T^b]=if^{abc}T^c$$

#### Open problems
- Generalized (higher-form, non-invertible) symmetries and their classification of phases.
- Why the observed gauge group is $SU(3)\times SU(2)\times U(1)$.

#### Connections
- [Standard Model](knowledge/06-particle-physics/standard-model/README.md) · [Phase transitions](knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/README.md) · [Angular momentum and spin](knowledge/04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin/README.md)

### Discrete symmetries and CPT · `knowledge/00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt`

**Scope.** Parity and intrinsic parity, the τ–θ puzzle, Wu experiment, C and CP violation, antiunitary time reversal and Kramers degeneracy, CPT theorem (Lüders–Pauli), CPT tests with antihydrogen and neutral kaons, T-violation and EDMs.

**Core ideas.**
- Weak interactions violate P and C maximally; CP is violated weakly.
- Time reversal is antiunitary; for half-integer spin $\Theta^2=-1$ → Kramers doublets (key for topological insulators).
- Any local, Lorentz-invariant QFT with a Hermitian Hamiltonian is CPT invariant.

**Key equations.**
$$P:\ \mathbf x\to-\mathbf x,\quad T:\ t\to-t\ (\text{antiunitary}),\qquad \Theta^2=(-1)^{2s}$$

**See also.** [CP violation](knowledge/06-particle-physics/standard-model/cp-violation/README.md) · [Topological insulators](knowledge/08-condensed-matter/topological-matter/topological-insulators/README.md)

### Lie groups and representations · `knowledge/00-foundations/symmetry-and-group-theory/lie-groups-and-representations`

**Scope.** Generators and structure constants, Casimir operators, roots and weights, Young tableaux, tensor-product decompositions, SU(2) ≅ double cover of SO(3), SU(3) flavor and color, Lorentz group and spinors, Poincaré group and Wigner's classification.

**Core ideas.**
- A Lie group is locally determined by its algebra; representations are classified by highest weights.
- Multiplets of particles are irreducible representations (isospin doublets, the baryon octet and decuplet).
- Particles = unitary irreps of the Poincaré group, labelled by mass and spin/helicity.

**Key equations.**
$$\mathbf 3\otimes\bar{\mathbf 3}=\mathbf 8\oplus\mathbf 1,\qquad \mathbf 3\otimes\mathbf 3\otimes\mathbf 3=\mathbf{10}\oplus\mathbf 8\oplus\mathbf 8\oplus\mathbf 1$$

**Landmark.** Wigner (1939) — see [subfield landmarks](knowledge/00-foundations/symmetry-and-group-theory/README.md).

**See also.** [Hadron spectroscopy](knowledge/06-particle-physics/standard-model/hadron-spectroscopy-and-exotics/README.md) · [Angular momentum](knowledge/04-quantum-physics/quantum-mechanics-core/angular-momentum-and-spin/README.md)

### Noether's theorem and conservation laws · `knowledge/00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws`

**Scope.** Noether's first and second theorems, time translation → energy, space translation → momentum, rotation → angular momentum, internal U(1) → charge, energy–momentum tensor, conservation in GR (no global energy in general), Ward identities in quantum theory.

**Core ideas.**
- Global continuous symmetries give conserved currents; local (gauge) symmetries give constraints/identities (second theorem).
- In GR, energy conservation is local ($\nabla_\mu T^{\mu\nu}=0$); a global conserved energy needs a timelike Killing vector.
- Quantum anomalies can spoil classical conservation laws.

**Key equations.**
$$Q=\int d^3x\,j^0,\qquad \frac{dQ}{dt}=0;\qquad T^{\mu\nu}=\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\partial^\nu\phi-\eta^{\mu\nu}\mathcal L$$

**Landmark.** Noether (1918) — see [subfield landmarks](knowledge/00-foundations/symmetry-and-group-theory/README.md).

**See also.** [Conservation laws in mechanics](knowledge/01-classical-mechanics/newtonian-mechanics/conservation-laws/README.md) · [Anomalies](knowledge/06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology/README.md)

### Spontaneous symmetry breaking · `knowledge/00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking`

**Scope.** Order parameters, degenerate vacua, Goldstone's theorem, counting of Goldstone modes (type A/B), Anderson–Higgs mechanism, Mermin–Wagner theorem, symmetry breaking in magnets, crystals, superfluids and superconductors, explicit vs. spontaneous breaking (pions).

**Core ideas.**
- A Hamiltonian symmetric under $G$ can have ground states invariant only under $H\subset G$; the vacuum manifold is $G/H$.
- Each broken continuous generator gives a gapless mode — unless the symmetry is gauged, in which case the gauge boson becomes massive.
- No continuous symmetry breaking at $T>0$ in $d\le2$ with short-range interactions (Mermin–Wagner).

**Key equations.**
$$V(\phi)=-\mu^2|\phi|^2+\lambda|\phi|^4\Rightarrow|\langle\phi\rangle|=\sqrt{\mu^2/2\lambda}$$

**See also.** [Higgs boson](knowledge/06-particle-physics/standard-model/higgs-boson/README.md) · [Mean-field and Landau theory](knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory/README.md)

## Units, constants and dimensional analysis · `knowledge/00-foundations/units-and-constants`

#### Overview
Since 20 May 2019 all seven SI base units are defined by fixing exact values of seven constants ($\Delta\nu_{\text{Cs}}$, $c$, $h$, $e$, $k_B$, $N_A$, $K_{cd}$). Other constants (e.g. $G$, $\alpha$, $m_e$) are measured, and CODATA publishes adjusted recommended values. Dimensional analysis — checking and exploiting units — is the cheapest error check in physics.

#### Key exact values (SI 2019)
$$c=299\,792\,458\ \text{m s}^{-1},\quad h=6.626\,070\,15\times10^{-34}\ \text{J s},\quad e=1.602\,176\,634\times10^{-19}\ \text{C}$$
$$k_B=1.380\,649\times10^{-23}\ \text{J K}^{-1},\quad N_A=6.022\,140\,76\times10^{23}\ \text{mol}^{-1},\quad \Delta\nu_{\text{Cs}}=9\,192\,631\,770\ \text{Hz}$$

Look up any other value with `python -I scripts/physlib.py constants "<name>"` (e.g. `constants "fine-structure"`).

#### Open problems
- The Newtonian constant $G$ is known only to ~22 ppm, with mutually inconsistent measurements.
- The 5σ disagreement between Cs- and Rb-based determinations of $\alpha$.
- Redefinition of the second with optical clocks.

#### Connections
- [Atomic clocks](knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement/README.md) · [Uncertainty](knowledge/00-foundations/measurement-and-data-analysis/uncertainty-and-error-propagation/README.md)

### Dimensional analysis and scaling · `knowledge/00-foundations/units-and-constants/dimensional-analysis-and-scaling`

**Scope.** Dimensional homogeneity, Buckingham π theorem, dimensionless groups (Reynolds, Mach, Froude, Péclet, Rayleigh), similarity and self-similar solutions (Taylor's blast wave), allometric scaling, Fermi problems, order-of-magnitude physics.

**Core ideas.**
- A physical law relating $n$ quantities with $k$ independent dimensions can be written in terms of $n-k$ dimensionless groups.
- Dimensionless numbers decide which physics dominates (inertia vs. viscosity, etc.).
- An estimate to within a factor of a few, with its logic stated, beats an exact answer to the wrong problem.

**Key equations.**
$$Re=\frac{\rho vL}{\mu},\qquad R(t)\approx\left(\frac{Et^2}{\rho}\right)^{1/5}\ (\text{Taylor–Sedov blast wave})$$

**Landmark.** Buckingham (1914) — see [subfield landmarks](knowledge/00-foundations/units-and-constants/README.md).

**See also.** [Viscous flow](knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow/README.md)

### Fundamental constants · `knowledge/00-foundations/units-and-constants/fundamental-constants`

**Scope.** CODATA least-squares adjustments, $\alpha$ from atom recoil (Cs, Rb) and electron $g-2$, Rydberg constant and the proton radius, $G$ measurements (torsion balances, atom interferometry), dimensionless vs. dimensionful constants, quasar and clock bounds on time variation.

**Core ideas.**
- Only dimensionless combinations (e.g. $\alpha\approx1/137.036$, $m_p/m_e\approx1836.15$) have unit-independent meaning.
- Precision comparisons of $\alpha$ from different methods are stringent tests of QED.
- Current bounds: $|\dot\alpha/\alpha|\lesssim10^{-18}$ per year from optical clocks.

**Key equations.**
$$\alpha=\frac{e^2}{4\pi\epsilon_0\hbar c},\qquad R_\infty=\frac{\alpha^2m_ec}{2h}$$

**See also.** [Precision anomalies](knowledge/06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2/README.md)

### SI units and the 2019 redefinition · `knowledge/00-foundations/units-and-constants/si-units-and-2019-redefinition`

**Scope.** Retirement of the International Prototype Kilogram, Kibble (watt) balance and X-ray crystal density (Avogadro sphere) realizations, quantum electrical standards (Josephson voltage, quantum Hall resistance), Boltzmann-constant thermometry, mise en pratique, CGPM decisions.

**Core ideas.**
- Fixing $h$ defines the kilogram; a Kibble balance equates mechanical and electrical power measured with quantum standards.
- Josephson ($K_J=2e/h$) and von Klitzing ($R_K=h/e^2$) constants are now exact.
- Units are realized by any method consistent with the defining constants.

**Key equations.**
$$mgv=UI\ (\text{Kibble balance}),\qquad K_J=\frac{2e}{h}\approx483\,597.8\ \text{GHz/V},\qquad R_K=\frac{h}{e^2}\approx25\,812.807\ \Omega$$

**See also.** [Quantum Hall effects](knowledge/08-condensed-matter/topological-matter/quantum-hall-effects/README.md) · [Josephson effect](knowledge/08-condensed-matter/superconductivity/josephson-effect-and-squids/README.md)


---

# Packet 00-2 (100 records)

{"id": "C0101", "a": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "b": "02-electromagnetism-and-optics/classical-optics/polarization-and-crystal-optics", "name": "Jones calculus and the polarization coherency matrix", "kind": "identity", "summary": "Fully polarized light is a vector in C², and optical elements are 2×2 complex matrices that compose by multiplication. Partially polarized light is described by the Hermitian positive coherency matrix, which is mathematically a qubit density matrix, with the degree of polarization playing the role of purity. Birefringent principal axes are the eigenvectors of the symmetric dielectric tensor.", "map": "\\mathbf E_{\\rm out}=M_n\\cdots M_1\\mathbf E_{\\rm in},\\ J=\\langle\\mathbf E\\mathbf E^\\dagger\\rangle,\\ P=\\sqrt{1-\\frac{4\\det J}{(\\mathrm{tr}J)^2}}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0102", "a": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "b": "02-electromagnetism-and-optics/photonics-and-lasers/metamaterials-and-plasmonics", "name": "Photonic bands as a Hermitian eigenvalue problem", "kind": "identity", "summary": "For lossless periodic dielectrics the master equation for H is a Hermitian eigenproblem, so frequencies are real, modes are orthogonal and a variational principle holds. Bloch's theorem then gives photonic bands and gaps, the same spectral theory as electrons in crystals. Unlike the electron case it acts on a transverse vector field with no intrinsic length scale, so scaling a crystal by s scales its frequencies by 1/s.", "map": "\\nabla\\times\\left(\\frac{1}{\\epsilon(\\mathbf r)}\\nabla\\times\\mathbf H\\right)=\\frac{\\omega^2}{c^2}\\mathbf H,\\quad \\mathbf H_{\\mathbf k}=e^{i\\mathbf k\\cdot\\mathbf r}\\mathbf u_{\\mathbf k}(\\mathbf r)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0103", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "02-electromagnetism-and-optics/electrodynamics/potentials-and-gauge-invariance", "name": "The vector potential as a U(1) connection", "kind": "identity", "summary": "The gauge potential is a connection on a U(1) bundle and F is its curvature. Gauge transformations are changes of local section, and the Aharonov–Bohm phase is the connection's holonomy around a loop. A Dirac monopole is a topologically nontrivial bundle that needs two patches (Wu–Yang), and consistency between the patches quantizes charge.", "map": "A\\to A+d\\lambda,\\ F=dA,\\ e^{i(q/\\hbar)\\oint A}=e^{iq\\Phi_B/\\hbar},\\ \\frac{1}{2\\pi}\\int_{S^2}\\frac{q}{\\hbar}F\\in\\mathbb Z", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0104", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "02-electromagnetism-and-optics/electrodynamics/relativistic-electrodynamics", "name": "Maxwell's equations as dF=0 and d⋆F=J", "kind": "identity", "summary": "In differential-form language the field strength is the exact 2-form F=dA. The homogeneous Maxwell equations are the Bianchi identity dF=0, and the sourced ones are d⋆F=⋆J. The integral laws are Stokes' theorem, the metric enters only through the Hodge star, and charge conservation follows from d²=0.", "map": "F=dA,\\quad dF=0,\\quad d{\\star}F=\\mu_0{\\star}J,\\quad d{\\star}J=0\\ (d^2=0)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0105", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "02-electromagnetism-and-optics/photonics-and-lasers/metamaterials-and-plasmonics", "name": "Transformation optics: geometry as an effective medium", "kind": "method transfer", "summary": "Maxwell's equations keep their form under any coordinate map if ε and μ are replaced by transformed tensors. A desired ray geometry, such as a cloak or a concentrator, is therefore designed as a coordinate transformation and built from anisotropic metamaterials. Equivalently, rays follow geodesics of an optical metric (Fermat's principle), the same mathematics that lets a medium mimic curved spacetime.", "map": "\\epsilon'^{ij}=\\frac{\\Lambda^i{}_a\\Lambda^j{}_b\\,\\epsilon^{ab}}{\\det\\Lambda},\\ \\mu'^{ij}\\ \\text{likewise},\\ \\Lambda^i{}_a=\\partial x'^i/\\partial x^a", "breaks": "Ideal cloaks need singular, impedance-matched and strongly dispersive ε and μ, so causality and losses confine real devices to narrow bands or ray-only (carpet) versions.", "confidence": "established", "strength": 3}
{"id": "C0106", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "02-electromagnetism-and-optics/radiation-and-scattering/dipole-radiation-and-antennas", "name": "Johnson–Nyquist noise and antenna temperature", "kind": "identity", "summary": "A matched single-mode antenna inside a blackbody enclosure delivers k_BTΔf to its load. That is exactly the available Johnson–Nyquist noise of a resistor at temperature T; Nyquist himself derived it from a transmission line in equilibrium. Radio astronomers therefore quote received power as an antenna or brightness temperature, with the radiation resistance acting as a resistor whose noise is the sky.", "map": "P=k_BT\\,\\Delta f,\\ \\langle V^2\\rangle=4k_BTR\\,\\Delta f,\\ T_A=\\frac{1}{\\Omega_A}\\int T_B(\\Omega)P_n(\\Omega)\\,d\\Omega\\ (h\\nu\\ll k_BT)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0107", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "02-electromagnetism-and-optics/classical-optics/fourier-optics-and-imaging", "name": "Super-resolution localization as parameter estimation", "kind": "method transfer", "summary": "PALM and STORM beat the diffraction limit through statistics rather than better optics. Isolated emitters are fitted by maximum likelihood, and the Cramér–Rao bound puts localization precision at about the PSF width divided by √N photons. Fisher-information analysis also shows that intensity imaging loses the ability to resolve two incoherent points as they merge ('Rayleigh's curse'), which mode-sorting measurements avoid.", "map": "\\sigma_{\\rm loc}\\gtrsim\\frac{s_{\\rm PSF}}{\\sqrt N},\\quad \\mathrm{Var}(\\hat\\theta)\\ge\\frac{1}{N\\,\\mathcal I(\\theta)}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0108", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "02-electromagnetism-and-optics/classical-optics/polarization-and-crystal-optics", "name": "Faraday rotation (T-odd) vs optical activity (P-odd)", "kind": "mechanism", "summary": "Both effects rotate linear polarization. Natural optical activity comes from chirality (broken parity) and is reciprocal, so it undoes itself on retro-reflection. Faraday rotation is driven by the T-odd magnetic field and is nonreciprocal, so it doubles on the return pass. This symmetry difference is why optical isolators need magneto-optics.", "map": "\\mathbf D=\\epsilon\\mathbf E+i\\epsilon_0\\mathbf G\\times\\mathbf E,\\quad \\mathbf G\\propto\\mathbf k\\ (\\text{activity, }\\mathcal P\\text{-odd})\\ \\text{or}\\ \\mathbf G\\propto\\mathbf B\\ (\\text{Faraday, }\\mathcal T\\text{-odd})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0109", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "02-electromagnetism-and-optics/photonics-and-lasers/nonlinear-optics", "name": "Inversion symmetry forbids second-order nonlinearity", "kind": "mechanism", "summary": "Under parity both P and E change sign, so every even-order susceptibility vanishes in a centrosymmetric medium. Second-harmonic generation therefore needs non-centrosymmetric crystals, such as the quartz in Franken's experiment or LiNbO₃. SHG is used as a probe of broken inversion at surfaces, at interfaces and in ferroelectric order.", "map": "P_i=\\epsilon_0\\chi^{(2)}_{ijk}E_jE_k;\\ \\mathcal P:\\ \\mathbf P\\to-\\mathbf P,\\ \\mathbf E\\to-\\mathbf E\\Rightarrow\\chi^{(2)}=-\\chi^{(2)}=0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0110", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "02-electromagnetism-and-optics/photonics-and-lasers/topological-photonics", "name": "T-breaking and absent Kramers protection for photons", "kind": "mechanism", "summary": "Photonic Chern insulators with one-way edge modes need broken time reversal, from gyromagnetic or time-modulated media. Photons are bosons with Θ²=+1, so they lack the Kramers degeneracy that protects electronic Z₂ topological insulators. Photonic 'quantum spin Hall' analogues instead use engineered pseudo-spins, which symmetry-breaking defects can couple.", "map": "\\Theta_{\\rm photon}^2=+1\\ \\text{vs}\\ \\Theta_{\\rm electron}^2=-1;\\ \\#\\text{edge modes}=C=\\frac{1}{2\\pi}\\int_{BZ}\\Omega\\,d^2k", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0111", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "02-electromagnetism-and-optics/classical-optics/polarization-and-crystal-optics", "name": "Poincaré sphere: SU(2) on Jones vectors, SO(3) on Stokes", "kind": "identity", "summary": "Lossless polarization optics act on Jones vectors as SU(2), up to a global phase. The 2-to-1 homomorphism maps this to SO(3) rotations of the Stokes vector on the Poincaré sphere, the same structure as spin-½ on the Bloch sphere. A closed loop on the sphere gives the Pancharatnam geometric phase, equal to half the enclosed solid angle.", "map": "U=e^{-i\\theta\\,\\hat{\\mathbf n}\\cdot\\boldsymbol\\sigma/2}\\mapsto R_{\\hat{\\mathbf n}}(\\theta)\\in SO(3),\\ \\mathbf S\\propto\\mathbf E^\\dagger\\boldsymbol\\sigma\\mathbf E,\\ |\\gamma_P|=\\Omega/2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0112", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "02-electromagnetism-and-optics/electrodynamics/relativistic-electrodynamics", "name": "The field tensor as the (1,0)⊕(0,1) Lorentz representation", "kind": "identity", "summary": "Under the Lorentz group, F_{μν} splits into self-dual and anti-self-dual parts, the Riemann–Silberstein vectors E±icB, which transform as (1,0) and (0,1). Its two invariants are E²−c²B² and E·B. In Wigner's classification the photon is the massless helicity ±1 representation of the Poincaré group.", "map": "\\mathbf F_\\pm=\\mathbf E\\pm ic\\mathbf B\\in(1,0),(0,1);\\ F_{\\mu\\nu}F^{\\mu\\nu}=2(B^2-E^2/c^2),\\ F_{\\mu\\nu}\\tilde F^{\\mu\\nu}\\propto\\mathbf E\\cdot\\mathbf B", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0113", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/multipole-expansions", "name": "Multipole moments as irreducible SO(3) tensors", "kind": "identity", "summary": "The 2l+1 spherical moments of order l form an irreducible representation of the rotation group, so a rank-l Cartesian moment reduces to its symmetric traceless part. The Wigner–Eckart theorem then gives the selection rules for multipole radiation. It also forbids moments of order l>2j in a state of angular momentum j, so a spin-½ particle has no quadrupole moment.", "map": "q_{lm}=\\int r^lY_{lm}^*(\\Omega)\\rho\\,d^3r\\ \\text{transforms under }D^{(l)}(R);\\ \\langle j\\|T^{(l)}\\|j\\rangle=0\\ \\text{for}\\ l>2j", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0114", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "02-electromagnetism-and-optics/classical-optics/polarization-and-crystal-optics", "name": "Spin and orbital angular momentum of light", "kind": "identity", "summary": "Rotational invariance gives the electromagnetic field a conserved angular momentum. For paraxial beams it splits into a spin part fixed by circular polarization (±ħ per photon, seen as torque on a wave plate by Beth in 1936) and an orbital part from helical phase fronts (ℓħ in Laguerre–Gauss beams). For general fields the split is gauge-sensitive and still debated.", "map": "\\mathbf J=\\epsilon_0\\!\\int\\mathbf r\\times(\\mathbf E\\times\\mathbf B)\\,d^3r=\\epsilon_0\\!\\int\\big[E_i(\\mathbf r\\times\\nabla)A_i+\\mathbf E\\times\\mathbf A\\big]d^3r\\ (\\text{Coulomb gauge})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0115", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "02-electromagnetism-and-optics/electrodynamics/maxwells-equations", "name": "Conservation laws of electrodynamics as Noether currents", "kind": "identity", "summary": "The continuity equation is the Noether current of the U(1) phase symmetry of charged matter. Poynting's theorem and the Maxwell stress tensor are components of the field's (Belinfante-symmetrized) energy–momentum tensor, which comes from spacetime translations. By Noether's second theorem, local gauge invariance makes charge conservation an identity that Maxwell's equations themselves require.", "map": "\\partial_\\mu J^\\mu=0\\ (\\Leftarrow\\partial_\\mu\\partial_\\nu F^{\\mu\\nu}\\equiv0),\\quad \\partial_\\mu T^{\\mu\\nu}_{\\rm EM}=-F^{\\nu\\lambda}J_\\lambda", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0116", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "02-electromagnetism-and-optics/photonics-and-lasers/nonlinear-optics", "name": "Phase matching as momentum conservation", "kind": "mechanism", "summary": "Translation invariance of a homogeneous crystal conserves photon momentum in wave mixing, so efficient conversion needs Δk=0, usually reached through birefringence. Quasi-phase-matching deliberately reduces continuous to discrete translation symmetry with periodic poling. Momentum is then conserved only up to the grating's reciprocal vector.", "map": "\\omega_3=\\omega_1+\\omega_2\\ (\\text{time transl.}),\\ \\Delta k=k_3-k_1-k_2=0\\ \\to\\ \\Delta k=\\frac{2\\pi m}{\\Lambda}\\ (\\text{QPM})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0117", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/fields-in-matter", "name": "Plasma frequency as photon mass: Anderson's Higgs route", "kind": "analogy", "summary": "In a collisionless Drude medium, transverse light obeys ω²=ω_p²+c²k², a massive Klein–Gordon dispersion. The long-range Coulomb force lifts the would-be acoustic density mode to the plasmon at ω_p. Anderson used this plasma picture to argue that a gauge field can gain mass by absorbing a would-be Goldstone mode, the core of the Higgs–Anderson mechanism.", "map": "\\epsilon(\\omega)=1-\\frac{\\omega_p^2}{\\omega^2}\\Rightarrow\\omega^2=\\omega_p^2+c^2k^2,\\quad m_\\gamma^{\\rm eff}=\\hbar\\omega_p/c^2", "breaks": "A normal plasma has no condensate and no broken symmetry. A collisionless plasma only freezes in static magnetic flux, like a perfect conductor, while a superconductor expels it (Meissner effect) because its photon mass comes from a phase-coherent condensate. With collisions, static fields penetrate fully.", "confidence": "established", "strength": 2}
{"id": "C0118", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "02-electromagnetism-and-optics/photonics-and-lasers/laser-physics", "name": "Laser threshold as spontaneous U(1) phase breaking", "kind": "analogy", "summary": "Near threshold the single-mode field amplitude obeys a Landau-like equation. Below threshold only zero field is stable; above it there is a ring of states with fixed amplitude and arbitrary phase. The phase is then a Goldstone-like soft mode, and its diffusion under spontaneous-emission noise sets the Schawlow–Townes linewidth.", "map": "\\dot a=(g-\\kappa)a-\\beta|a|^2a+\\xi(t),\\ |a|^2=\\frac{g-\\kappa}{\\beta},\\ \\Delta\\nu_{\\rm ST}\\propto\\frac{h\\nu(\\Delta\\nu_c)^2}{P}", "breaks": "A laser is an open, driven-dissipative system rather than an equilibrium ground state. A single mode is effectively zero-dimensional, so the phase diffuses freely (finite linewidth). There is no true long-range order or thermodynamic singularity, only a crossover that sharpens with photon number.", "confidence": "established", "strength": 3}
{"id": "C0119", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "name": "Rayleigh's λ⁻⁴ law from dimensional analysis", "kind": "method transfer", "summary": "Rayleigh (1871) argued that for a particle much smaller than the wavelength, the scattered amplitude is proportional to its volume and falls off as 1/r. Dimensional consistency then forces a 1/λ² factor in amplitude, hence λ⁻⁴ in intensity, which is why the sky is blue. It is the textbook example of a scaling argument.", "map": "\\frac{I_s}{I_0}\\propto\\frac{V^2}{r^2\\lambda^4}\\quad(2\\pi a/\\lambda\\ll1)", "breaks": "It holds only for size parameter 2πa/λ≪1 and away from resonances. For a≳λ the full Mie solution, with its resonances and nearly wavelength-independent scattering, takes over (white clouds).", "confidence": "established", "strength": 2}
{"id": "C0120", "a": "00-foundations/units-and-constants/fundamental-constants", "b": "02-electromagnetism-and-optics/photonics-and-lasers/laser-physics", "name": "Mode-locked frequency combs as rulers for constants", "kind": "method transfer", "summary": "A mode-locked laser emits a comb of evenly spaced frequencies, and f–2f self-referencing fixes its offset. This links optical frequencies to the caesium microwave standard, enabling hydrogen spectroscopy for the Rydberg constant and optical-clock limits on drifts of α. Earlier laser frequency and wavelength measurements had already led to fixing c exactly in 1983.", "map": "f_n=n\\,f_{\\rm rep}+f_{\\rm ceo},\\quad f_{\\rm ceo}=2f_n-f_{2n}\\ (f\\text{-}2f\\ \\text{self-referencing})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0121", "a": "00-foundations/units-and-constants/si-units-and-2019-redefinition", "b": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/magnetostatics", "name": "Ampere redefinition: μ0 became a measured constant", "kind": "historical", "summary": "Until 2019 the ampere was defined by the magnetostatic force between parallel wires, which fixed μ0=4π×10⁻⁷ N A⁻² exactly. Fixing e and h instead makes μ0 a measured quantity tied to the fine-structure constant. CODATA 2022 gives μ0=1.256 637 061 27(20)×10⁻⁶ N A⁻², within 1σ of the old exact value.", "map": "\\frac{F}{L}=\\frac{\\mu_0I_1I_2}{2\\pi d}\\ (\\text{pre-2019 def.}),\\qquad \\mu_0=\\frac{2\\alpha h}{e^2c}\\ (\\text{post-2019})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0122", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems", "name": "Spin-glass methods for learning and inference", "kind": "method transfer", "summary": "Replica, cavity and message-passing methods built for spin glasses and random constraint satisfaction became tools for analysing and designing learning and inference algorithms, such as belief and survey propagation and loss-landscape studies. In the other direction, ML is now used to detect order in disordered systems.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0123", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/statistical-physics-of-learning", "name": "Learning machines as statistical-mechanical systems", "kind": "shared object", "summary": "Neural networks are both a tool for physics (surrogates, neural quantum states) and an object studied by statistical mechanics. Hopfield nets and Boltzmann machines are Ising-type energy models, and their capacity and generalization are computed with replica and cavity methods.", "map": "E(\\mathbf s)=-\\tfrac12\\sum_{ij}J_{ij}s_is_j,\\quad P(\\mathbf s)\\propto e^{-E(\\mathbf s)/T}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0124", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "name": "Diffusion models: Langevin dynamics run backwards", "kind": "method transfer", "summary": "Diffusion generative models add noise with an Ornstein–Uhlenbeck (forward Fokker–Planck) process. They generate samples by integrating the time-reversed SDE, whose drift contains the learned score $\\nabla\\log p_t$, a construction taken from non-equilibrium statistical physics.", "map": "dx=-\\tfrac12\\beta x\\,dt+\\sqrt\\beta\\,dW;\\quad dx=[f-g^2\\nabla_x\\log p_t]\\,dt+g\\,d\\bar W", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0125", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/renormalization-group", "name": "Deep networks as renormalization (analogy)", "kind": "analogy", "summary": "Mehta and Schwab mapped stacked restricted Boltzmann machines onto Kadanoff block-spin variational RG, which suggests that network depth performs coarse-graining. Later information-theoretic schemes used neural networks to learn the relevant RG variables directly.", "map": "", "breaks": "The mapping is exact only for one particular variational RG. Trained networks need not follow an RG flow and impose no scale invariance or fixed-point structure, and supervised nets discard information for reasons unrelated to scale.", "confidence": "current research", "strength": 2}
{"id": "C0126", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "name": "Thermostats and ergodic averages realise ensembles", "kind": "method transfer", "summary": "Plain MD samples the microcanonical ensemble through time averages along an ergodic trajectory. Nosé–Hoover extended dynamics and Langevin thermostats are built so that the physical variables are canonically distributed, and barostats give NPT.", "map": "\\dot p=F-\\zeta p,\\quad \\dot\\zeta=\\frac{1}{Q}\\Big(\\sum\\frac{p^2}{m}-gk_BT\\Big)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0127", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "name": "MD discovers long-time tails beyond Boltzmann", "kind": "method transfer", "summary": "Alder and Wainwright's MD showed that a fluid's velocity autocorrelation decays as a power law, not exponentially as the Boltzmann equation's molecular-chaos assumption predicts. The cause is correlated vortex backflow, which also makes Green–Kubo transport coefficients diverge in 2D.", "map": "C_v(t)=\\langle v(t)\\cdot v(0)\\rangle\\sim t^{-d/2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0128", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/percolation", "name": "Fortuin–Kasteleyn clusters behind Swendsen–Wang", "kind": "identity", "summary": "The q-state Potts partition function equals a random-cluster model that reduces to bond percolation at q=1. Swendsen–Wang and Wolff algorithms flip exactly these FK clusters, so the Ising transition is a percolation transition of FK clusters.", "map": "Z_{\\rm Potts}\\propto\\sum_{A\\subseteq E}p^{|A|}(1-p)^{|E|-|A|}q^{k(A)},\\quad p=1-e^{-\\beta J}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0129", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/spin-glasses", "name": "Parallel tempering and simulated annealing", "kind": "method transfer", "summary": "Rugged spin-glass landscapes trap local Monte Carlo, which led to replica-exchange (parallel tempering) swaps between temperatures. The transfer also ran the other way: simulated annealing turned the slow cooling of a frustrated system into a general optimization algorithm.", "map": "P_{\\rm swap}=\\min\\big(1,e^{(\\beta_i-\\beta_j)(E_i-E_j)}\\big)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0130", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "name": "Path-integral Monte Carlo of Bose and Fermi statistics", "kind": "method transfer", "summary": "Imaginary-time path integrals turn quantum particles into classical ring polymers. Bose statistics enter as permutation cycles whose winding gives the superfluid fraction of He-4 at the λ point, while Fermi antisymmetry produces negative weights: the sign problem.", "map": "Z=\\frac{1}{N!}\\sum_P(\\pm1)^{P}\\!\\int\\! dR\\,\\rho(R,PR;\\beta),\\quad \\rho_s/\\rho=\\frac{m\\langle W^2\\rangle L^2}{3\\hbar^2\\beta N}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0131", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "name": "MCMC is a master equation with detailed balance", "kind": "identity", "summary": "A Metropolis or Glauber chain is a discrete-time master equation whose stationary state is the Boltzmann weight, and its relaxation is a genuine stochastic (model-A) dynamics. Langevin and hybrid Monte Carlo sample by integrating Langevin or Hamiltonian dynamics.", "map": "W(x\\to x')\\,e^{-\\beta E(x)}=W(x'\\to x)\\,e^{-\\beta E(x')}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0132", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-thermodynamics-and-fluctuation-theorems", "name": "Annealed importance sampling equals Jarzynski equality", "kind": "identity", "summary": "Averaging exponentiated work over non-equilibrium switching runs to estimate a free-energy difference is Jarzynski's equality. Statistics independently introduced the same estimator as annealed importance sampling, and in both the variance is controlled by the dissipated work.", "map": "\\langle e^{-\\beta W}\\rangle=e^{-\\beta\\Delta F}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0133", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/critical-exponents-and-universality", "name": "Finite-size scaling extraction of critical exponents", "kind": "method transfer", "summary": "Monte Carlo gets precise critical exponents from finite-size scaling: Binder-cumulant crossings locate $T_c$, and histogram reweighting maps observables continuously in $T$. Monte Carlo values for 3D Ising now agree with the conformal bootstrap to about four significant figures.", "map": "\\chi_L=L^{\\gamma/\\nu}\\,\\tilde\\chi\\big((T-T_c)L^{1/\\nu}\\big),\\quad U_L=1-\\frac{\\langle m^4\\rangle}{3\\langle m^2\\rangle^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0134", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/ising-model-and-lattice-models", "name": "Metropolis and cluster sampling of lattice models", "kind": "method transfer", "summary": "Markov-chain Monte Carlo that obeys detailed balance with respect to $e^{-\\beta H}$ is the standard numerical route to Ising, Potts, XY and Heisenberg thermodynamics. Swendsen–Wang and Wolff cluster moves remove the critical slowing down that local updates suffer.", "map": "P_{\\rm acc}=\\min(1,e^{-\\beta\\Delta E}),\\quad \\tau\\sim\\xi^{z},\\ z_{\\rm local}\\approx2,\\ z_{\\rm cluster}\\ll2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0135", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "name": "Lattice Boltzmann: kinetic theory as fluid solver", "kind": "method transfer", "summary": "Discretizing the Boltzmann equation with a BGK collision term on a velocity lattice gives a local, highly parallel CFD scheme. A Chapman–Enskog expansion shows that it reproduces Navier–Stokes, with the viscosity set by the relaxation time.", "map": "f_i(\\mathbf x+\\mathbf c_i\\Delta t,t+\\Delta t)-f_i=-\\tfrac1\\tau(f_i-f_i^{\\rm eq}),\\quad \\nu=c_s^2(\\tau-\\tfrac12)\\Delta t", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0136", "a": "00-foundations/computational-physics/tensor-network-methods", "b": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/renormalization-group", "name": "DMRG and tensor RG as renormalization", "kind": "method transfer", "summary": "DMRG grew out of Wilson's numerical RG by keeping the most heavily weighted density-matrix eigenstates. Tensor RG, Baxter-style corner transfer matrices and MERA coarse-grain classical partition functions and quantum states, carrying out real-space RG flows with controlled truncation and giving scaling dimensions at fixed points.", "map": "Z=\\mathrm{tTr}\\prod T_{ijkl}\\ \\xrightarrow{\\text{SVD, keep }\\chi}\\ T'_{i'j'k'l'}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0137", "a": "00-foundations/history-and-philosophy-of-physics/history-of-physics", "b": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "name": "Blackbody and heat capacities launched quantum theory", "kind": "historical", "summary": "Planck's 1900 fit to blackbody radiation required energy quanta $h\\nu$ and gave the first accurate $k_B$ and $N_A$. Einstein's 1907 quantized-oscillator heat capacity then explained the low-T failure of Dulong–Petit, and Bose's 1924 counting led to Bose–Einstein statistics.", "map": "u(\\nu,T)=\\frac{8\\pi h\\nu^3}{c^3}\\frac{1}{e^{h\\nu/k_BT}-1}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0138", "a": "00-foundations/history-and-philosophy-of-physics/history-of-physics", "b": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "name": "Brownian motion proved atoms real", "kind": "historical", "summary": "Einstein's 1905 theory tied the diffusion constant of a suspended particle to $k_BT$ and viscosity, and Perrin's 1908–09 measurements of it gave Avogadro's number and settled the atomic debate. Langevin's 1908 equation founded the theory of stochastic differential equations.", "map": "D=\\frac{k_BT}{6\\pi\\eta a},\\quad \\langle x^2\\rangle=2Dt", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0139", "a": "00-foundations/history-and-philosophy-of-physics/philosophy-of-physics", "b": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/laws-of-thermodynamics", "name": "Arrow of time and the second law", "kind": "shared object", "summary": "The second law is philosophy's central example of an irreversible macroscopic law resting on time-symmetric microdynamics. The standard reductive account combines $S=k_B\\ln W$ with a low-entropy initial condition (the past hypothesis), and the status of that account is still debated.", "map": "S=k_B\\ln W,\\quad \\Delta S_{\\rm isolated}\\ge0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0140", "a": "00-foundations/history-and-philosophy-of-physics/philosophy-of-physics", "b": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information", "name": "Maxwell's demon and Landauer: is information physical?", "kind": "shared object", "summary": "In the Bennett–Landauer account, Maxwell's demon is defeated by the $k_BT\\ln2$ cost of erasing its memory. Philosophers such as Earman and Norton dispute whether Landauer's principle is independently established, even though experiments have confirmed the erasure bound.", "map": "W_{\\rm erase}\\ge k_BT\\ln2\\ \\text{per bit}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0141", "a": "00-foundations/history-and-philosophy-of-physics/philosophy-of-physics", "b": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation", "name": "H-theorem and the Loschmidt–Zermelo objections", "kind": "shared object", "summary": "Boltzmann's H-theorem derives a monotonic entropy increase from the Boltzmann equation. Loschmidt's reversal objection and Zermelo's recurrence objection traced the time asymmetry to the molecular-chaos assumption (Stosszahlansatz), now the standard case study of irreversibility emerging from reversible laws.", "map": "H=\\int f\\ln f\\,d^3v,\\quad \\frac{dH}{dt}\\le0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0142", "a": "00-foundations/history-and-philosophy-of-physics/philosophy-of-physics", "b": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/critical-exponents-and-universality", "name": "Universality, emergence and the thermodynamic limit", "kind": "shared object", "summary": "Phase transitions are non-analyticities that exist only in the $N\\to\\infty$ limit, and universality makes critical exponents independent of microscopic detail. Both are the main case studies in the reduction-versus-emergence and multiple-realizability debates, from Anderson's 'More is different' to Batterman.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0143", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation", "name": "Kramers–Kronig relations from causality", "kind": "identity", "summary": "Causality makes the response function $\\chi(\\omega)$ analytic in the upper half-plane. Contour integration then gives the Kramers–Kronig relations between its reactive and dissipative parts, plus sum rules, and analytic continuation from Matsubara frequencies gives real-time response.", "map": "\\chi'(\\omega)=\\frac{1}{\\pi}\\mathcal P\\!\\int\\frac{\\chi''(\\omega')}{\\omega'-\\omega}\\,d\\omega'", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0144", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/ising-model-and-lattice-models", "name": "Lee–Yang zeros: transitions as complex zeros of Z", "kind": "method transfer", "summary": "For finite N the partition function is a polynomial in the fugacity with no positive real zeros. The Lee–Yang circle theorem places every zero of the ferromagnetic Ising model on $|z|=1$, and a transition appears where the zeros pinch the real axis as $N\\to\\infty$; Fisher zeros do the same in complex β.", "map": "Z_N(z)\\propto\\prod_k(z-z_k),\\quad |z_k|=1,\\quad z=e^{-2\\beta h}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0145", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation", "name": "Response functions are retarded Green's functions", "kind": "identity", "summary": "The Kubo formula writes the susceptibility as a retarded commutator Green's function, so linear response is a Green's-function convolution with the force. Causality enters through $\\theta(t)$, and the poles give the normal modes and their damping.", "map": "\\chi_{AB}(t)=\\tfrac{i}{\\hbar}\\theta(t)\\langle[A(t),B(0)]\\rangle,\\quad \\delta\\langle A\\rangle(t)=\\int\\chi(t-t')F(t')\\,dt'", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0146", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-processes-and-langevin-dynamics", "name": "Fokker–Planck propagators as Green's functions", "kind": "identity", "summary": "The transition probability of Brownian motion is the Green's function (heat kernel) of the diffusion or Fokker–Planck operator. First-passage and escape problems are solved with images, Laplace transforms and Sturm–Liouville eigenmodes, and the symmetrized Fokker–Planck operator maps onto a Schrödinger operator.", "map": "\\partial_tP=D\\nabla^2P,\\quad G(\\mathbf r,t)=(4\\pi Dt)^{-d/2}e^{-r^2/4Dt}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0147", "a": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "b": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/exactly-solvable-models", "name": "Transfer-matrix eigenvalues give the free energy", "kind": "identity", "summary": "With local couplings, $Z=\\mathrm{Tr}\\,T^N$, so the free energy comes from the largest transfer-matrix eigenvalue and the correlation length from the ratio of the top two. Perron–Frobenius makes the top eigenvalue unique, which rules out a 1D transition at T>0, and Onsager solved 2D Ising by diagonalizing its transfer matrix.", "map": "f=-k_BT\\ln\\lambda_0,\\quad \\xi^{-1}=\\ln(\\lambda_0/\\lambda_1)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0148", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/laws-of-thermodynamics", "name": "Carathéodory: second law as integrability of δQ", "kind": "method transfer", "summary": "In Carathéodory's formulation, heat is an inexact Pfaffian 1-form. The axiom that every state has adiabatically inaccessible neighbours implies the form is integrable, and its integrating factor yields absolute temperature and entropy from differential geometry alone.", "map": "\\delta Q\\wedge d(\\delta Q)=0\\ \\Rightarrow\\ \\delta Q_{\\rm rev}=T\\,dS", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0149", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "name": "Canonical energy fluctuations limit microcalorimeters", "kind": "mechanism", "summary": "A microcalorimeter or bolometer weakly linked to a bath has canonical energy fluctuations $\\langle\\Delta E^2\\rangle=k_BT^2C$. This thermodynamic-fluctuation noise sets the ultimate resolution of transition-edge sensors, which is why they operate near 0.1 K with tiny heat capacity.", "map": "\\langle\\Delta E^2\\rangle=k_BT^2C,\\quad \\mathrm{NEP}^2\\simeq4k_BT^2G", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0150", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation", "name": "Johnson–Nyquist noise as fluctuation–dissipation", "kind": "identity", "summary": "The thermal noise floor $4k_BTR\\Delta f$ of every resistor and amplifier is the fluctuation–dissipation theorem applied to a circuit. The theorem's quantum form adds the zero-point term behind the half-photon-per-mode limit of linear amplifiers.", "map": "S_V(\\omega)=2R\\hbar\\omega\\coth\\frac{\\hbar\\omega}{2k_BT}\\ \\xrightarrow{\\hbar\\omega\\ll k_BT}\\ 4k_BTR", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0151", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/statistical-physics-of-learning", "name": "Phase transitions in high-dimensional inference", "kind": "method transfer", "summary": "Planted (teacher–student) problems such as community detection, compressed sensing and perceptron learning are disordered systems, and replica or cavity calculations give their Bayes-optimal error. They show sharp detectability and algorithmic-hardness thresholds, and Bayes-optimal inference sits on the Nishimori line, where replica symmetry holds.", "map": "", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0152", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/entropy-and-information", "name": "Maximum entropy: statistical mechanics as inference", "kind": "identity", "summary": "Jaynes showed that the Gibbs ensembles are the maximum-Shannon-entropy distributions consistent with measured averages, so inference and statistical mechanics share the exponential family. In Bayesian terms the evidence plays the role of a partition function and $-\\ln$(evidence) that of a free energy.", "map": "\\max_p\\Big[-\\sum p\\ln p\\Big]\\ \\text{s.t.}\\ \\langle E\\rangle\\ \\Rightarrow\\ p\\propto e^{-\\beta E}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0153", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/stochastic-thermodynamics-and-fluctuation-theorems", "name": "Cramér–Rao bound and thermodynamic uncertainty", "kind": "mechanism", "summary": "The thermodynamic uncertainty relation bounds the relative precision of any current by the entropy produced. It follows from the Cramér–Rao inequality applied to a perturbed path ensemble, so dissipation plays the role of the Fisher information that limits precision.", "map": "\\frac{\\mathrm{Var}(J)}{\\langle J\\rangle^2}\\ge\\frac{2k_B}{\\Sigma}\\quad\\leftrightarrow\\quad \\mathrm{Var}(\\hat\\theta)\\ge\\frac{1}{\\mathcal I(\\theta)}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0154", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory", "name": "Variational Bayes is mean-field theory", "kind": "identity", "summary": "Fitting a factorized approximate posterior by maximizing the evidence lower bound is the Gibbs–Bogoliubov–Feynman variational principle of naive mean-field theory. Belief propagation corresponds to the Bethe approximation, and the TAP equations add the Onsager reaction term.", "map": "F\\le F_0+\\langle H-H_0\\rangle_0\\ \\Leftrightarrow\\ \\ln p(D)\\ge\\mathbb E_q[\\ln p(D,\\theta)]-\\mathbb E_q[\\ln q]", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0155", "a": "00-foundations/symmetry-and-group-theory", "b": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "name": "Permutation symmetry gives Bose and Fermi statistics", "kind": "identity", "summary": "Identical particles carry a one-dimensional representation of the permutation group $S_N$: symmetric for bosons, antisymmetric for fermions. These give Bose–Einstein and Fermi–Dirac occupation numbers, and in 2D the braid group also allows anyons.", "map": "\\bar n(\\epsilon)=\\frac{1}{e^{\\beta(\\epsilon-\\mu)}\\mp1}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0156", "a": "00-foundations/symmetry-and-group-theory", "b": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena", "name": "Symmetry classifies phases and transitions", "kind": "mechanism", "summary": "Phases differ by which subgroup $H\\subset G$ of the symmetry group the state keeps, and the order parameter transforms in a representation of $G$. Together with the dimension, $G$ and $H$ fix the allowed Landau free energy, the order-parameter manifold $G/H$ and its defects, and the universality class.", "map": "G\\to H,\\quad \\mathcal M=G/H,\\quad \\text{defects}\\sim\\pi_n(G/H)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0157", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/linear-response-and-fluctuation-dissipation", "name": "Onsager reciprocity from time-reversal invariance", "kind": "mechanism", "summary": "Time-reversal symmetry of the microscopic dynamics implies the Onsager–Casimir relations among transport coefficients, such as the Kelvin relation between the Peltier and Seebeck coefficients. The relations carry sign factors for T-odd variables and require reversing magnetic fields.", "map": "L_{ij}(\\mathbf B)=\\epsilon_i\\epsilon_j\\,L_{ji}(-\\mathbf B),\\quad \\Pi=TS", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0158", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/exactly-solvable-models", "name": "Virasoro symmetry solves 2D critical models", "kind": "method transfer", "summary": "At 2D critical points, scale invariance grows into the infinite-dimensional Virasoro algebra. Its unitary minimal-model representations give exact exponents, e.g. Ising with $c=1/2$, $\\eta=1/4$, $\\nu=1$, which match Onsager's lattice solution.", "map": "[L_m,L_n]=(m-n)L_{m+n}+\\tfrac{c}{12}m(m^2-1)\\delta_{m+n,0}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0159", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/critical-exponents-and-universality", "name": "Order-parameter symmetry labels universality classes", "kind": "mechanism", "summary": "A universality class is fixed by the dimension and the order parameter's symmetry group: Z2 (Ising), O(2) (XY, He-4), O(3) (Heisenberg) or S_q (Potts). The representation content of a perturbation, such as cubic anisotropy, decides whether it is relevant.", "map": "d=3:\\ \\nu_{\\mathbb Z_2}\\approx0.630,\\ \\nu_{O(2)}\\approx0.672,\\ \\nu_{O(3)}\\approx0.711", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0160", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions", "name": "Conserved charges fix the Gibbs ensemble", "kind": "mechanism", "summary": "Each Noether charge (energy, U(1) particle number, momentum) enters the equilibrium ensemble with its own Lagrange multiplier ($\\beta$, $\\beta\\mu$, $\\beta\\mathbf v$). Integrable systems, which have extensively many conserved quantities, relax instead to a generalized Gibbs ensemble.", "map": "\\rho=Z^{-1}e^{-\\beta(H-\\mu N-\\mathbf v\\cdot\\mathbf P)}\\ \\to\\ \\rho_{\\rm GGE}=Z^{-1}e^{-\\sum_k\\lambda_kI_k}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0161", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/spin-glasses", "name": "Replica symmetry breaking vs. ordinary SSB", "kind": "analogy", "summary": "Parisi's solution of the SK model breaks the permutation symmetry among $n\\to0$ replicas. The Edwards–Anderson overlap then acts as an order parameter for frozen random order, as ergodicity splits into many pure states.", "map": "q_{EA}=\\overline{\\langle s_i\\rangle^2},\\quad P(q)\\ \\text{non-trivial}", "breaks": "No symmetry of the physical Hamiltonian breaks: replica symmetry exists only inside the $n\\to0$ formalism, and the pure states are not related by any group action. Whether finite-dimensional spin glasses follow RSB or the droplet picture is still disputed.", "confidence": "established", "strength": 2}
{"id": "C0162", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/quantum-statistics", "name": "BEC as broken U(1); Goldstone modes set low-T laws", "kind": "mechanism", "summary": "Bose–Einstein condensation is off-diagonal long-range order, a broken global U(1) phase whose Goldstone mode is the Bogoliubov phonon. More generally, Goldstone dispersion sets low-T power laws: linear phonons give Debye $C\\propto T^3$, and quadratic ferromagnetic magnons give Bloch $\\Delta M\\propto T^{3/2}$.", "map": "\\lim_{|r-r'|\\to\\infty}\\langle\\hat\\psi^\\dagger(r)\\hat\\psi(r')\\rangle=n_0\\neq0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0163", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/mean-field-and-landau-theory", "name": "Landau free energy is the symmetry-breaking potential", "kind": "identity", "summary": "The Landau expansion and the Mexican-hat (Higgs) potential are the same symmetric quartic, and its minimum moves off the origin when the quadratic coefficient changes sign. Mean-field theory then gives $m\\propto(T_c-T)^{1/2}$, and the Ginzburg criterion says when fluctuations invalidate it.", "map": "f=a(T-T_c)m^2+bm^4\\ \\leftrightarrow\\ V=-\\mu^2|\\phi|^2+\\lambda|\\phi|^4", "breaks": "Landau theory is a thermal free energy with a T-dependent coefficient, valid above the upper critical dimension. When the symmetry is gauged there is no local gauge-invariant order parameter (Elitzur's theorem) and the Goldstone modes are absorbed by the gauge field.", "confidence": "established", "strength": 3}
{"id": "C0164", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/topological-phase-transitions-bkt", "name": "Mermin–Wagner and quasi-long-range order", "kind": "mechanism", "summary": "In 2D, Goldstone fluctuations forbid continuous symmetry breaking at T>0 (Mermin–Wagner), but the XY model still has a transition. Vortices, classified by $\\pi_1(U(1))=\\mathbb Z$, unbind at $T_{\\rm BKT}$ and separate power-law from exponential correlations.", "map": "\\langle e^{i(\\theta_r-\\theta_0)}\\rangle\\sim r^{-\\eta(T)},\\quad \\eta(T_{\\rm BKT})=\\tfrac14", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0165", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/renormalization-group", "name": "Anomalous dimensions: where naive scaling fails", "kind": "mechanism", "summary": "Dimensional analysis and generalized homogeneity (Widom scaling) predict power laws, but near criticality the microscopic cutoff never drops out, so exponents pick up anomalous dimensions; Barenblatt calls this incomplete similarity. The RG computes them as eigenvalues at a fixed point.", "map": "G(r)\\sim r^{-(d-2+\\eta)}=r^{-(d-2)}(r/a)^{-\\eta};\\ f(t,h)=b^{-d}f(b^{y_t}t,b^{y_h}h)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0166", "a": "00-foundations/units-and-constants/si-units-and-2019-redefinition", "b": "03-thermodynamics-and-statistical-mechanics/classical-thermodynamics/laws-of-thermodynamics", "name": "Kelvin redefined by fixing the Boltzmann constant", "kind": "shared object", "summary": "Thermodynamic temperature, defined through the second law by Kelvin's Carnot scale, has been realized since 2019 by fixing $k_B$ exactly. The fixed value came from primary thermometry based on statistical mechanics: acoustic gas thermometry ($u^2=\\gamma k_BT/m$), dielectric-constant gas thermometry and Johnson-noise thermometry.", "map": "k_B=1.380649\\times10^{-23}\\,\\mathrm{J\\,K^{-1}}\\ \\text{(exact)},\\quad \\eta_{\\rm Carnot}=1-T_c/T_h", "breaks": "", "confidence": "established", "strength": 3}
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