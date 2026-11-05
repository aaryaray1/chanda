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

### Natural units and the Planck scale · `knowledge/00-foundations/units-and-constants/natural-units-and-planck-scale`

**Scope.** $\hbar=c=1$ (energy is the only dimension), geometrized $G=c=1$, Hartree atomic units, Gaussian vs. SI electromagnetism, Planck length/time/mass/energy/temperature, meaning of the Planck scale for quantum gravity.

**Core ideas.**
- In natural units, $[\text{length}]=[\text{time}]=[\text{energy}]^{-1}$; convert with $\hbar c=197.327$ MeV·fm.
- Planck units combine $G,\hbar,c$: the scale where quantum gravitational effects are expected to be order one.
- Always restore units before quoting a number to a non-specialist.

**Key equations.**
$$\ell_P=\sqrt{\frac{\hbar G}{c^3}}\approx1.616\times10^{-35}\ \text{m},\quad m_P=\sqrt{\frac{\hbar c}{G}}\approx2.176\times10^{-8}\ \text{kg},\quad E_P\approx1.22\times10^{19}\ \text{GeV}$$

**See also.** [Quantum gravity](knowledge/05-relativity-and-gravitation/quantum-gravity/README.md) · [Particle physics conventions](knowledge/06-particle-physics/README.md)

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

# Packet 00-3 (100 records)

{"id": "C0201", "a": "00-foundations/units-and-constants", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "name": "The SI second is a caesium hyperfine frequency", "kind": "shared object", "summary": "Since 1967 the second has been defined by fixing the Cs ground-state hyperfine frequency. Time and frequency are the most precisely realised SI quantities, and the metre is traced to them through the fixed value of c.", "map": "\\Delta\\nu_{\\rm Cs}=9\\,192\\,631\\,770\\ \\mathrm{Hz}\\ (\\text{exact})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0202", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/bose-einstein-condensates-and-degenerate-gases", "name": "Unitary Fermi gas: universality from a missing scale", "kind": "mechanism", "summary": "At a Feshbach resonance the scattering length diverges and drops out, leaving density as the only scale. Dimensional analysis then forces every observable to be a universal number times its free-Fermi-gas value, the Bertsch parameter ξ being one example. Dilute neutron matter shares the same universality.", "map": "a\\to\\infty:\\ \\frac EN=\\xi\\,\\frac35E_F,\\ \\xi\\approx0.37,\\ T_c\\approx0.17\\,T_F", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0203", "a": "00-foundations/units-and-constants/fundamental-constants", "b": "04-quantum-physics/atomic-molecular-and-optical-physics", "name": "AMO measurements determine α and m_e for CODATA", "kind": "shared object", "summary": "The fine-structure constant comes from atom-recoil interferometry (h/m for Cs and Rb) and from the Penning-trap electron g-factor combined with QED. These AMO inputs dominate the CODATA values of α, R∞ and m_e, and the ~5σ gap between the Cs and Rb values remains unresolved.", "map": "\\alpha^2=\\frac{2R_\\infty}{c}\\frac{A_r(X)}{A_r(e)}\\frac{h}{m_X}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0204", "a": "00-foundations/units-and-constants/fundamental-constants", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "name": "Clock ratios test the constancy of α and m_p/m_e", "kind": "method transfer", "summary": "Different transitions depend on α and μ = m_p/m_e with different sensitivities, so repeated ratios between clocks (Al+/Hg+, Yb+ E3/E2, Cs/Sr) bound present-day drifts at the ~10^{-18} per year level. The same ratios search for ultralight dark matter, which would make the constants oscillate.", "map": "\\frac{d}{dt}\\ln\\frac{\\nu_1}{\\nu_2}=(K_1-K_2)\\frac{\\dot\\alpha}{\\alpha},\\ K_{\\rm Hg^+}\\approx-2.9,\\ K_{\\rm Al^+}\\approx0", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0205", "a": "00-foundations/units-and-constants/fundamental-constants", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-structure-and-spectroscopy", "name": "Hydrogen spectroscopy, R∞ and the proton radius", "kind": "shared object", "summary": "The Rydberg constant and the proton charge radius are fitted together to hydrogen and deuterium transition frequencies. The muonic-hydrogen Lamb shift (2010) gave a radius 4% smaller. The puzzle eased once newer hydrogen measurements and CODATA 2018/2022 moved to about 0.84 fm.", "map": "\\Delta E_{nS}^{\\rm size}=\\frac{2(Z\\alpha)^4}{3n^3}\\frac{m_r^3c^4}{\\hbar^2}r_p^2,\\ r_p\\approx0.841\\ \\mathrm{fm}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0206", "a": "00-foundations/units-and-constants/si-units-and-2019-redefinition", "b": "04-quantum-physics/atomic-molecular-and-optical-physics/atomic-clocks-and-precision-measurement", "name": "Optical clocks and redefining the second", "kind": "shared object", "summary": "Optical lattice and ion clocks now beat the Cs primary standard by about 100×. The CIPM roadmap therefore plans an optical redefinition of the second around 2030, continuing the 2019 move to defining units by fixed constants.", "map": "\\delta\\nu/\\nu\\sim10^{-18}\\ (\\text{optical})\\ \\text{vs}\\ 10^{-16}\\ (\\text{Cs fountain})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0207", "a": "00-foundations/computational-physics", "b": "05-relativity-and-gravitation/general-relativity/numerical-relativity", "name": "Scientific computing toolkit powers numerical relativity", "kind": "method transfer", "summary": "Numerical relativity is a flagship application of large-scale scientific computing: adaptive mesh refinement, high-order finite-difference and multidomain spectral solvers, constraint damping and parallel HPC turned the Einstein equations into working codes, culminating in the 2005 binary-black-hole breakthrough.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0208", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "05-relativity-and-gravitation/gravitational-waves/ground-based-detections", "name": "Machine learning for GW searches, glitches and inference", "kind": "method transfer", "summary": "Convolutional networks detect compact-binary signals and classify instrumental glitches (Gravity Spy), normalizing-flow simulation-based inference gives full posteriors in seconds, and ML surrogates of numerical-relativity waveforms speed up parameter estimation, complementing matched filtering and stochastic sampling.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0209", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "05-relativity-and-gravitation/gravitational-waves/ground-based-detections", "name": "MCMC and nested sampling for GW source parameters", "kind": "method transfer", "summary": "Posteriors over the ~15 parameters of a compact binary are sampled with Markov-chain Monte Carlo and nested sampling (LALInference, Bilby), direct descendants of the Metropolis algorithm; nested sampling also yields the Bayesian evidence used for model selection and tests of GR.", "map": "p(\\theta|d)\\propto\\mathcal L(d|\\theta)\\pi(\\theta),\\quad \\mathcal L\\propto e^{-\\frac12(d-h(\\theta)|d-h(\\theta))}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0210", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "05-relativity-and-gravitation/quantum-gravity/other-approaches-to-quantum-gravity", "name": "Monte Carlo over geometries: causal dynamical triangulations", "kind": "method transfer", "summary": "Causal dynamical triangulations define the gravitational path integral as a sum over causal simplicial geometries, Wick-rotated and sampled by Markov-chain Monte Carlo as in lattice field theory; simulations find a phase with an extended de Sitter-like 4D geometry whose spectral dimension runs from ~4 at large scales to ~2 at short scales.", "map": "Z=\\sum_T\\frac{1}{C_T}\\,e^{-S_{\\rm Regge}[T]}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0211", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "05-relativity-and-gravitation/general-relativity/numerical-relativity", "name": "Well-posed hyperbolic formulations and PDE integrators", "kind": "method transfer", "summary": "The Einstein equations become a stable initial-value problem only in strongly hyperbolic formulations (generalized harmonic, BSSN with moving punctures); they are then evolved by method-of-lines Runge–Kutta with finite differences plus AMR or spectral methods, with constraint damping controlling constraint growth.", "map": "\\partial_t u=A^i(u)\\,\\partial_i u+S(u),\\ \\text{well-posed iff strongly hyperbolic}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0212", "a": "00-foundations/computational-physics/tensor-network-methods", "b": "05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft", "name": "MERA and holographic codes as discrete AdS", "kind": "analogy", "summary": "In a tensor network, a boundary region's entropy is bounded by the number of bonds a minimal cut crosses times log χ, a discrete Ryu–Takayanagi formula; MERA's renormalization direction resembles a hyperbolic slice of AdS (Swingle), and holographic codes built from perfect tensors model bulk reconstruction as quantum error correction.", "map": "S_A\\le|\\gamma_A|\\log\\chi\\ \\leftrightarrow\\ S_A=\\frac{\\mathrm{Area}(\\gamma_A)}{4G_N}", "breaks": "Exact RT behaviour holds only for special (stabilizer or random) networks with flat entanglement spectra; there is no sub-AdS locality or Einstein dynamics, and MERA's emergent geometry has been argued to be closer to de Sitter or light-cone than to a spatial AdS slice.", "confidence": "current research", "strength": 3}
{"id": "C0213", "a": "00-foundations/history-and-philosophy-of-physics/philosophy-of-physics", "b": "05-relativity-and-gravitation/general-relativity/einstein-field-equations", "name": "Hole argument and the meaning of general covariance", "kind": "historical", "summary": "Einstein's 1913 hole argument, in which diffeomorphism-related solutions agree outside a region but differ inside it, seemed to make generally covariant field equations indeterministic; its resolution (spacetime points have no identity apart from the metric) let Einstein accept general covariance in 1915 and started the modern substantivalism–relationism debate.", "map": "g_{\\mu\\nu}\\ \\text{and}\\ \\phi^*g_{\\mu\\nu}\\ \\text{represent the same physical state}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0214", "a": "00-foundations/history-and-philosophy-of-physics/philosophy-of-physics", "b": "05-relativity-and-gravitation/quantum-gravity/loop-quantum-gravity", "name": "Problem of time in canonical quantum gravity", "kind": "shared object", "summary": "Canonical quantization of GR gives a Hamiltonian constraint (the Wheeler–DeWitt equation) with no external time, the 'frozen formalism'; loop quantum gravity and philosophy of physics both face the task of defining dynamics through relational observables and of saying what change means in a timeless theory.", "map": "\\hat{\\mathcal H}\\,\\Psi=0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0215", "a": "00-foundations/mathematical-methods", "b": "05-relativity-and-gravitation/general-relativity", "name": "GR as a showcase of mathematical-physics methods", "kind": "method transfer", "summary": "GR brings many mathematical methods together: the Einstein equations as a constrained nonlinear hyperbolic PDE system, Green's-function solutions of linearized gravity, perturbation expansions (post-Newtonian, black-hole perturbation theory) and spin-weighted spherical harmonics for radiation.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0216", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "05-relativity-and-gravitation/black-holes/black-hole-thermodynamics-and-hawking-radiation", "name": "Euclidean periodicity fixes the Hawking temperature", "kind": "identity", "summary": "Wick-rotating the Schwarzschild metric gives a smooth Euclidean geometry only if imaginary time is periodic with period 2πc/κ; since thermal Green's functions are periodic in imaginary time (KMS condition), that period is ħ/k_BT, which is the Hawking temperature (Gibbons–Hawking).", "map": "\\tau\\sim\\tau+\\frac{2\\pi c}{\\kappa}=\\frac{\\hbar}{k_BT_H}\\ \\Rightarrow\\ k_BT_H=\\frac{\\hbar\\kappa}{2\\pi c}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0217", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "05-relativity-and-gravitation/gravitational-waves/gravitational-wave-theory-and-waveforms", "name": "Ringdown quasinormal modes as Green's-function poles", "kind": "identity", "summary": "Black-hole ringdown is a sum of quasinormal modes: complex frequencies at the poles of the perturbation Green's function in the lower half ω-plane (plus a branch cut that gives late-time tails), computed by Leaver's continued fractions or WKB; they depend only on mass and spin, which enables black-hole spectroscopy.", "map": "h\\sim\\sum_n A_n e^{-i\\omega_n t},\\quad GM\\omega_{220}/c^3\\approx0.374-0.089i\\ (\\text{Schwarzschild})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0218", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "05-relativity-and-gravitation/quantum-gravity/string-theory", "name": "String worldsheets as Riemann surfaces", "kind": "identity", "summary": "Perturbative string amplitudes are integrals over moduli spaces of Riemann surfaces; worldsheet conformal invariance makes the theory a 2D CFT, worked with holomorphic functions, contour-integral operator product expansions and modular invariance of the torus amplitude.", "map": "T(z)T(w)\\sim\\frac{c/2}{(z-w)^4}+\\frac{2T(w)}{(z-w)^2}+\\frac{\\partial T(w)}{z-w}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0219", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "05-relativity-and-gravitation/gravitational-waves/gravitational-wave-theory-and-waveforms", "name": "Retarded Green's function yields the quadrupole formula", "kind": "identity", "summary": "In Lorenz gauge, linearized gravity is a sourced wave equation for the trace-reversed perturbation; the same retarded Green's function as in electrodynamics gives the far-zone field and hence the quadrupole formula for gravitational radiation.", "map": "\\Box\\bar h_{\\mu\\nu}=-\\frac{16\\pi G}{c^4}T_{\\mu\\nu},\\quad \\bar h_{ij}\\approx\\frac{2G}{c^4r}\\ddot I_{ij}(t-r/c)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0220", "a": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "b": "05-relativity-and-gravitation/black-holes/information-paradox", "name": "Random-subsystem entropy gives the Page curve", "kind": "method transfer", "summary": "Averaging subsystem entanglement entropy over Haar-random pure states in a finite-dimensional Hilbert space gives nearly maximal entropy for the smaller factor; applied to a black hole plus its radiation, this gives the Page curve (radiation entropy rises, then falls after the Page time), which unitarity requires and Hawking's calculation misses.", "map": "\\langle S_A\\rangle\\simeq\\ln m-\\frac{m}{2n}\\quad(m\\le n,\\ \\dim\\mathcal H=mn)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0221", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "05-relativity-and-gravitation/black-holes/schwarzschild-and-kerr-black-holes", "name": "Singularity theorems and global causal structure", "kind": "method transfer", "summary": "Global Lorentzian geometry (the Raychaudhuri focusing equation, trapped surfaces, conformal compactification into Penrose diagrams) proves that a trapped surface plus an energy condition implies geodesic incompleteness, so black-hole singularities are generic rather than artifacts of symmetry.", "map": "\\frac{d\\theta}{d\\lambda}=-\\tfrac12\\theta^2-\\sigma_{ab}\\sigma^{ab}+\\omega_{ab}\\omega^{ab}-R_{ab}k^ak^b", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0222", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "05-relativity-and-gravitation/general-relativity", "name": "Lorentzian geometry is the language of gravity", "kind": "identity", "summary": "GR models gravity as curvature of a Lorentzian manifold: free fall is geodesic motion, the equivalence principle is local flatness in normal coordinates, and tidal forces are the Riemann tensor acting through geodesic deviation.", "map": "\\frac{D^2\\xi^\\mu}{d\\tau^2}=-R^\\mu{}_{\\nu\\rho\\sigma}u^\\nu\\xi^\\rho u^\\sigma", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0223", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "05-relativity-and-gravitation/general-relativity/einstein-field-equations", "name": "Contracted Bianchi identity fixes the Einstein tensor", "kind": "identity", "summary": "The contracted Bianchi identity makes the Einstein tensor identically divergence-free, so it can consistently be set equal to a conserved stress–energy tensor; the field equations are a statement in Riemannian geometry about Ricci curvature.", "map": "\\nabla_\\mu G^{\\mu\\nu}\\equiv0,\\quad G_{\\mu\\nu}+\\Lambda g_{\\mu\\nu}=\\frac{8\\pi G}{c^4}T_{\\mu\\nu}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0224", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "05-relativity-and-gravitation/general-relativity/exact-solutions", "name": "Petrov classification and algebraically special metrics", "kind": "method transfer", "summary": "Classifying the Weyl tensor by its principal null directions (Petrov types, Newman–Penrose formalism) organizes the exact solutions; Kerr found the rotating black hole by searching for algebraically special vacuum metrics, and the Goldberg–Sachs theorem links that degeneracy to shear-free null congruences.", "map": "\\Psi_0=\\Psi_1=\\Psi_3=\\Psi_4=0,\\ \\Psi_2\\neq0\\ (\\text{type D: Schwarzschild, Kerr})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0225", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "05-relativity-and-gravitation/general-relativity/modified-gravity", "name": "Lovelock's theorem defines the routes to modified gravity", "kind": "identity", "summary": "In four dimensions the only symmetric, divergence-free rank-2 tensor built from the metric and its first two derivatives is a combination of G_μν and g_μν; every modified-gravity theory escapes this by adding fields (scalar-tensor, Horndeski), higher derivatives (f(R)), extra dimensions or nonlocality.", "map": "E_{\\mu\\nu}[g,\\partial g,\\partial^2g],\\ \\nabla^\\mu E_{\\mu\\nu}=0\\ \\Rightarrow\\ E_{\\mu\\nu}=aG_{\\mu\\nu}+b\\,g_{\\mu\\nu}\\ (D=4)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0226", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "05-relativity-and-gravitation/gravitational-waves/ground-based-detections", "name": "Template-bank metric on the waveform manifold", "kind": "method transfer", "summary": "The fractional SNR lost between neighbouring templates defines a Riemannian metric on source-parameter space, and template banks are lattices laid out with this metric; the related Fisher information matrix gives forecast parameter uncertainties.", "map": "1-\\mathcal M\\approx g_{ij}\\Delta\\theta^i\\Delta\\theta^j,\\ g_{ij}=-\\tfrac12\\partial_i\\partial_j\\mathcal M;\\ \\Gamma_{ij}=(\\partial_ih|\\partial_jh)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0227", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "05-relativity-and-gravitation/quantum-gravity/loop-quantum-gravity", "name": "Ashtekar connection variables recast GR as gauge theory", "kind": "method transfer", "summary": "Rewriting canonical GR with an SU(2) connection and a densitized triad (Ashtekar, later Ashtekar–Barbero) gives it a Yang–Mills-like phase space; holonomies of the connection and fluxes of the triad are the basic variables quantized in loop quantum gravity.", "map": "\\{A^i_a(x),E^b_j(y)\\}=8\\pi G\\gamma\\,\\delta^b_a\\delta^i_j\\delta^3(x-y)\\ (c=1)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0228", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "05-relativity-and-gravitation/special-relativity/lorentz-transformations-and-spacetime", "name": "Lorentz transformations as isometries of Minkowski metric", "kind": "identity", "summary": "Minkowski's reformulation makes Lorentz transformations the isometries of a flat metric of Lorentzian signature; four-vectors and tensors make laws manifestly covariant, and GR reuses the same machinery for curved metrics.", "map": "x'^\\mu=\\Lambda^\\mu{}_\\nu x^\\nu,\\quad \\Lambda^T\\eta\\Lambda=\\eta", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0229", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "05-relativity-and-gravitation/black-holes/black-hole-imaging-and-astrophysical-black-holes", "name": "VLBI: heterodyne receivers, maser clocks and correlators", "kind": "method transfer", "summary": "The Event Horizon Telescope is an Earth-sized interferometer: each station down-converts 1.3 mm signals with heterodyne receivers and time-stamps them with hydrogen-maser clocks, and correlators combine the recordings into visibilities whose diffraction limit resolves the ~40 μas ring; imaging is then an ill-posed inverse problem solved with regularized and Bayesian methods.", "map": "\\theta\\approx\\lambda/D=1.3\\,\\text{mm}/1.27\\times10^4\\,\\text{km}\\approx21\\,\\mu\\text{as}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0230", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "05-relativity-and-gravitation/gravitational-waves/ground-based-detections", "name": "Standard quantum limit and squeezed light in GW detectors", "kind": "shared object", "summary": "Interferometric GW detectors are limited by fundamental instrument noise: photon shot noise and radiation-pressure noise combine into the standard quantum limit, thermal noise follows the fluctuation–dissipation theorem, and injecting squeezed vacuum (frequency-dependent since O4) beats the shot-noise limit.", "map": "S_h^{\\rm SQL}(f)=\\frac{8\\hbar}{m(2\\pi f)^2L^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0231", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "05-relativity-and-gravitation/gravitational-waves/ground-based-detections", "name": "Matched filtering and Bayesian inference of GW signals", "kind": "method transfer", "summary": "GW detection is a likelihood-ratio test built on a noise-weighted inner product (matched filtering against template banks); significance comes from time-slide background estimation, and source parameters from Bayesian posteriors.", "map": "(a|b)=4\\,\\mathrm{Re}\\int\\frac{\\tilde a\\,\\tilde b^*}{S_n(f)}df,\\quad \\ln\\Lambda=(d|h)-\\tfrac12(h|h)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0232", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "05-relativity-and-gravitation/gravitational-waves/pulsar-timing-arrays", "name": "Hellings–Downs correlation and Bayesian evidence in PTAs", "kind": "method transfer", "summary": "A stochastic GW background makes timing residuals correlated between pulsar pairs according to the Hellings–Downs curve; PTA collaborations weigh evidence for it with Bayes factors and frequentist statistics against common-spectrum red noise, reaching ~3–4σ significance in 2023.", "map": "\\Gamma(\\zeta)=\\tfrac12-\\tfrac{x}{4}+\\tfrac32x\\ln x,\\quad x=\\frac{1-\\cos\\zeta}{2}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0233", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "05-relativity-and-gravitation/special-relativity/tests-of-lorentz-invariance", "name": "CPT tests double as Lorentz-invariance tests", "kind": "mechanism", "summary": "The CPT theorem follows from Lorentz invariance plus locality, and in local interacting QFT CPT violation implies Lorentz violation; so kaon mass differences, antihydrogen spectroscopy and Penning-trap particle–antiparticle comparisons constrain Lorentz-violating coefficients of the Standard-Model Extension.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0234", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "05-relativity-and-gravitation/quantum-gravity/holography-and-ads-cft", "name": "AdS isometries equal the boundary conformal group", "kind": "identity", "summary": "The isometry group of AdS_{d+1} is SO(d,2), exactly the conformal group of d-dimensional Minkowski space (extended to PSU(2,2|4) for AdS5×S5 and N=4 SYM); this symmetry match underlies the bulk-field/boundary-operator dictionary, where bulk mass fixes the operator's scaling dimension.", "map": "\\mathrm{Isom}(AdS_{d+1})=SO(d,2)=\\mathrm{Conf}(\\mathbb R^{1,d-1}),\\quad \\Delta(\\Delta-d)=m^2L^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0235", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "05-relativity-and-gravitation/quantum-gravity/loop-quantum-gravity", "name": "SU(2) spin networks and the quantized area spectrum", "kind": "identity", "summary": "LQG states are spin networks, graphs whose edges carry SU(2) irreducible representations j and whose nodes carry intertwiners; the area operator is diagonal on them with eigenvalues fixed by the SU(2) Casimir, so area is discrete.", "map": "\\hat A\\,|s\\rangle=8\\pi\\gamma\\,\\ell_P^2\\sum_i\\sqrt{j_i(j_i+1)}\\,|s\\rangle", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0236", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "05-relativity-and-gravitation/special-relativity", "name": "Special relativity is Poincaré invariance", "kind": "identity", "summary": "Special relativity says physics is invariant under the Poincaré group; Wigner's unitary irreducible representations classify particles by mass and spin, and the double cover SL(2,C) of the Lorentz group gives spinors.", "map": "SO^+(1,3)\\cong SL(2,\\mathbb C)/\\mathbb Z_2,\\quad P^\\mu P_\\mu=-m^2c^2\\ (\\text{Casimir})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0237", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "05-relativity-and-gravitation/black-holes/schwarzschild-and-kerr-black-holes", "name": "Killing symmetries give conserved orbital constants", "kind": "identity", "summary": "Each Killing vector of a black-hole metric gives a quantity conserved along geodesics (energy from ∂_t, angular momentum from ∂_φ), and Komar integrals define mass and spin; Kerr also has a Killing tensor that gives the Carter constant, a hidden symmetry that makes geodesic motion integrable.", "map": "\\nabla_{(\\mu}\\xi_{\\nu)}=0\\Rightarrow u^\\mu\\xi_\\mu=\\text{const};\\quad K_{\\mu\\nu}u^\\mu u^\\nu=\\mathcal C", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0238", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "05-relativity-and-gravitation/general-relativity/einstein-field-equations", "name": "Diffeomorphism invariance gives local conservation", "kind": "identity", "summary": "Diffeomorphism invariance of the matter action implies covariant conservation of the stress–energy tensor, and invariance of the Einstein–Hilbert action implies the Bianchi identity (Noether's second theorem); globally conserved energy exists only with Killing vectors or asymptotic symmetries.", "map": "\\delta_\\xi S_m=0\\ \\Rightarrow\\ \\nabla_\\mu T^{\\mu\\nu}=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0239", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "05-relativity-and-gravitation/gravitational-waves/gravitational-wave-theory-and-waveforms", "name": "No local gravitational energy; GW energy as averaged or boundary charge", "kind": "mechanism", "summary": "Because diffeomorphisms are a local gauge symmetry, Noether's second theorem gives no gauge-invariant local energy density for gravity; GW energy is defined only by averaging over wavelengths (Isaacson tensor) or as charges at null infinity, where the Bondi mass decreases as waves escape and BMS supertranslation charges are tied to the gravitational memory effect.", "map": "t^{\\rm GW}_{\\mu\\nu}=\\frac{c^4}{32\\pi G}\\left\\langle\\partial_\\mu h^{TT}_{ij}\\,\\partial_\\nu h_{TT}^{ij}\\right\\rangle", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0240", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "05-relativity-and-gravitation/special-relativity/tests-of-lorentz-invariance", "name": "Spontaneous Lorentz violation in the SME", "kind": "mechanism", "summary": "Lorentz symmetry could break spontaneously, with a vector or tensor field acquiring a vacuum expectation value that picks out a frame (Kostelecký–Samuel, bumblebee models); the Standard-Model Extension parametrizes the resulting background coefficients, and the associated Nambu–Goldstone modes have been proposed as photons or gravitons.", "map": "\\langle B_\\mu\\rangle=b_\\mu\\neq0\\ \\Rightarrow\\ \\mathcal L\\supset-b_\\mu\\bar\\psi\\gamma_5\\gamma^\\mu\\psi", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0241", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "05-relativity-and-gravitation/general-relativity/numerical-relativity", "name": "Scale-free vacuum GR: one simulation serves all masses", "kind": "mechanism", "summary": "The vacuum Einstein equations have no intrinsic length scale, so binary-black-hole simulations are run in units of total mass M and rescale to any mass: times and lengths scale as GM/c^3 and GM/c^2, and strain is (GM/c^2)/D times a universal function. Matter breaks this scaling, which is why neutron-star mergers must be simulated separately for each equation of state.", "map": "t\\to\\lambda t,\\ x\\to\\lambda x,\\ M\\to\\lambda M:\\quad f_{\\rm GW}\\propto\\frac{c^3}{GM},\\ h\\propto\\frac{GM}{c^2D}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0242", "a": "00-foundations/units-and-constants/fundamental-constants", "b": "05-relativity-and-gravitation/general-relativity/tests-of-general-relativity", "name": "Constancy of constants tests the equivalence principle", "kind": "mechanism", "summary": "Local position invariance, part of the Einstein equivalence principle, requires dimensionless constants such as α and m_p/m_e to be the same everywhere and at all times; atomic-clock comparisons, the Oklo natural reactor and quasar spectra bound their drift, and any variation would generically also violate the weak equivalence principle.", "map": "|\\dot\\alpha/\\alpha|\\lesssim10^{-18}\\,\\text{yr}^{-1}\\ (\\text{optical-clock comparisons})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0243", "a": "00-foundations/units-and-constants/natural-units-and-planck-scale", "b": "05-relativity-and-gravitation/black-holes/black-hole-thermodynamics-and-hawking-radiation", "name": "Black-hole entropy is horizon area in Planck units", "kind": "identity", "summary": "Bekenstein–Hawking entropy is a quarter of the horizon area counted in Planck areas, and the Hawking temperature combines ħ, c, G and k_B; it is the clearest formula in which all four constants appear together, which is why black holes serve as a quantum-gravity laboratory.", "map": "S_{BH}=\\frac{k_Bc^3A}{4G\\hbar}=k_B\\frac{A}{4\\ell_P^2},\\quad T_H=\\frac{\\hbar c^3}{8\\pi GMk_B}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0244", "a": "00-foundations/units-and-constants/natural-units-and-planck-scale", "b": "05-relativity-and-gravitation/quantum-gravity", "name": "Planck scale marks where quantum gravity is order one", "kind": "shared object", "summary": "Combining G, ħ and c gives the Planck length, time and energy, where gravitational and quantum effects are both order one; every quantum-gravity programme is organized around this scale, and its ~10^15 gap above LHC energies is why direct tests are so hard.", "map": "\\ell_P=\\sqrt{\\hbar G/c^3}\\approx1.6\\times10^{-35}\\,\\text{m},\\ E_P=\\sqrt{\\hbar c^5/G}\\approx1.2\\times10^{19}\\,\\text{GeV}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0245", "a": "00-foundations/units-and-constants/natural-units-and-planck-scale", "b": "05-relativity-and-gravitation/special-relativity/tests-of-lorentz-invariance", "name": "Planck-suppressed dispersion and GRB time-of-flight bounds", "kind": "mechanism", "summary": "If quantum gravity changes photon dispersion at order E/E_P, high-energy photons from distant gamma-ray bursts arrive with energy-dependent delays proportional to E/E_P times the light-travel time; Fermi-LAT timing of GRB 090510 pushed the linear-order scale beyond E_P, so the Planck scale itself is now an experimentally probed quantity.", "map": "E^2=p^2c^2\\left(1\\pm\\xi\\frac{E}{E_P}\\right),\\quad \\Delta t\\approx\\xi\\frac{E}{E_P}\\frac{D}{c}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0246", "a": "00-foundations/units-and-constants/si-units-and-2019-redefinition", "b": "05-relativity-and-gravitation/general-relativity/tests-of-general-relativity", "name": "SI second as proper time; relativistic geodesy", "kind": "shared object", "summary": "The SI second is a proper time realized by clocks, so International Atomic Time is referred to an equipotential surface and corrected for gravitational redshift; optical clocks now resolve centimetre height differences, which turns the GR redshift into a geodesy tool and a requirement for any optical redefinition of the second.", "map": "\\frac{\\Delta\\nu}{\\nu}=\\frac{g\\,\\Delta h}{c^2}\\approx1.09\\times10^{-16}\\ \\text{per metre}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0247", "a": "00-foundations/computational-physics", "b": "06-particle-physics/quantum-field-theory/lattice-field-theory", "name": "Lattice QCD as a computational-physics workload", "kind": "method transfer", "summary": "Lattice field theory turns the Euclidean path integral into a very high-dimensional integral attacked with the whole computational toolkit: Markov-chain Monte Carlo, Krylov and multigrid solvers for the Dirac operator, and now ML samplers and tensor networks. Lattice QCD has in turn driven dedicated supercomputer design (APE, QCDOC).", "map": "Z=\\int\\mathcal{D}U\\,\\det D[U]\\,e^{-S_g[U]}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0248", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "06-particle-physics/collider-and-experimental-particle-physics/machine-learning-in-hep", "name": "Neural tools shared by physics and HEP", "kind": "method transfer", "summary": "The same neural tools (classifiers, generative surrogates, normalizing flows, graph networks, anomaly detectors) serve physics in general and HEP in particular. In HEP they tag jets, emulate calorimeter showers, run in triggers and power simulation-based inference, and HEP was an early adopter and a main source of benchmark datasets.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0249", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "06-particle-physics/quantum-field-theory/lattice-field-theory", "name": "Hybrid Monte Carlo: molecular dynamics in fictitious time", "kind": "method transfer", "summary": "HMC samples lattice gauge fields with dynamical fermions by adding conjugate momenta, integrating Hamilton's equations with a reversible, volume-preserving leapfrog or Omelyan integrator, and removing the integration error with a Metropolis step. It was invented for lattice QCD and later adopted in Bayesian statistics (NUTS in Stan).", "map": "H=\\tfrac12\\sum\\pi^2+S[\\phi],\\ P_{\\rm acc}=\\min(1,e^{-\\Delta H})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0250", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "06-particle-physics/collider-and-experimental-particle-physics/monte-carlo-event-generators", "name": "Event generators as Monte Carlo integrators", "kind": "method transfer", "summary": "Event generators do importance-sampled (VEGAS-type adaptive) phase-space integration of factorized cross sections, hit-or-miss unweighting into events, and parton showers sampled with the veto algorithm. The shower samples the Sudakov no-emission probability with the same survival-probability logic used to sample radioactive decay times.", "map": "\\Delta(t_0,t)=\\exp\\left[-\\int_t^{t_0}\\frac{dt'}{t'}\\int dz\\,\\frac{\\alpha_s}{2\\pi}P(z)\\right]", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0251", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "06-particle-physics/quantum-field-theory/lattice-field-theory", "name": "Euclidean action as a Boltzmann weight", "kind": "identity", "summary": "After Wick rotation, e^{iS} becomes e^{-S_E}, so lattice QFT is a statistical-mechanics problem sampled by Markov-chain Monte Carlo (heat bath, HMC). It inherits that field's problems: autocorrelation, critical slowing down toward the continuum limit, and the sign problem when the weight is not positive.", "map": "\\langle O\\rangle=\\frac1Z\\int\\mathcal DU\\,O[U]\\,e^{-S_E[U]}\\approx\\frac1N\\sum_{i=1}^NO[U_i]", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0252", "a": "00-foundations/computational-physics/tensor-network-methods", "b": "06-particle-physics/quantum-field-theory/lattice-field-theory", "name": "Tensor networks for lattice gauge theories", "kind": "method transfer", "summary": "In the Hamiltonian formulation, MPS and DMRG simulate 1+1D lattice gauge theories such as the Schwinger model without importance sampling, so they avoid the sign problem at finite density, with a θ term and in real time. Gauss's law can be built into gauge-invariant tensors, and these results benchmark quantum simulators of gauge theories.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0253", "a": "00-foundations/history-and-philosophy-of-physics/history-of-physics", "b": "06-particle-physics", "name": "Particle physics as the archetype of big science", "kind": "historical", "summary": "The path from cosmic-ray and accelerator discoveries to the Standard Model is a central case study in the history of physics. The field also defined 'big science': Lawrence's cyclotron laboratory, CERN (1954) as a model of international collaboration, and LHC collaborations with thousands of authors.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0254", "a": "00-foundations/history-and-philosophy-of-physics/philosophy-of-physics", "b": "06-particle-physics/beyond-the-standard-model/extra-dimensions-and-hierarchy-problem", "name": "Naturalness as an argument form", "kind": "shared object", "summary": "The hierarchy problem rests on naturalness, a fine-tuning argument that philosophy of physics studies as a heuristic. Its past success (the charm-quark mass estimated from K⁰ mixing) and the LHC's null searches for natural new physics have made its epistemic status an open debate.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0255", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2", "name": "Dispersive hadronic vacuum polarization for muon g−2", "kind": "method transfer", "summary": "Analyticity and the optical theorem turn the measured e⁺e⁻→hadrons cross section into the leading hadronic contribution to the muon g−2 through a Kramers–Kronig-type integral. Tensions among the e⁺e⁻ data sets (CMD-3 versus earlier experiments) and with lattice QCD are why this term decides the Standard Model comparison.", "map": "a_\\mu^{\\rm HVP,LO}=\\frac{\\alpha^2}{3\\pi^2}\\int_{s_{\\rm th}}^{\\infty}\\frac{ds}{s}K(s)R(s)", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0256", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "06-particle-physics/quantum-field-theory/conformal-field-theory", "name": "Holomorphy and the Virasoro algebra in 2D CFT", "kind": "identity", "summary": "In two dimensions the conformal maps are exactly the holomorphic functions, so the stress tensor splits into T(z) and T̄(z̄). Radial quantization turns charges into contour integrals, Ward identities and operator-product expansions follow from the residue theorem, and the Virasoro generators are Laurent coefficients.", "map": "L_n=\\oint\\frac{dz}{2\\pi i}z^{n+1}T(z),\\ [L_m,L_n]=(m-n)L_{m+n}+\\frac{c}{12}m(m^2-1)\\delta_{m+n,0}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0257", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "06-particle-physics/quantum-field-theory/feynman-diagrams-and-scattering-amplitudes", "name": "S-matrix analyticity, dispersion relations and cuts", "kind": "method transfer", "summary": "Causality makes scattering amplitudes analytic in the energy variables, so they obey dispersion relations, the relativistic version of Kramers–Kronig. The optical theorem and Cutkosky rules give the discontinuities across branch cuts, and the modern unitarity method rebuilds loop amplitudes from their cuts.", "map": "\\mathcal M(s)=\\frac1\\pi\\int_{s_0}^\\infty ds'\\frac{\\mathrm{Im}\\,\\mathcal M(s')}{s'-s-i\\epsilon},\\ \\mathrm{Im}\\,\\mathcal M(s,0)=2E_{\\rm cm}p_{\\rm cm}\\sigma_{\\rm tot}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0258", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "06-particle-physics/quantum-field-theory/feynman-diagrams-and-scattering-amplitudes", "name": "The Feynman propagator is a Green's function", "kind": "identity", "summary": "The propagator is the Green's function of the Klein–Gordon (or Dirac) operator, with the iε prescription choosing time-ordered boundary conditions, so the Feynman-diagram expansion is a Born series in Green's functions. Differential equations in the kinematic variables are also a main tool for evaluating loop integrals.", "map": "(\\Box+m^2)D_F(x-y)=-i\\delta^4(x-y),\\ \\tilde D_F(p)=\\frac{i}{p^2-m^2+i\\epsilon}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0259", "a": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "b": "06-particle-physics/neutrino-physics/neutrino-oscillations", "name": "Neutrino mixing as a unitary basis change", "kind": "identity", "summary": "Flavour and mass eigenstates are related by the unitary PMNS matrix, so oscillation is the time evolution of a superposition of energy eigenstates. The two-flavour formula is the two-level Rabi formula, and the MSW effect is adiabatic passage through an avoided crossing of the matter Hamiltonian's eigenvalues.", "map": "|\\nu_\\alpha\\rangle=\\sum_iU_{\\alpha i}^*|\\nu_i\\rangle,\\ P_{\\alpha\\to\\beta}=\\sin^22\\theta\\,\\sin^2\\frac{\\Delta m^2L}{4E}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0260", "a": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "b": "06-particle-physics/standard-model/flavor-physics-and-ckm", "name": "CKM matrix from bi-unitary diagonalization of Yukawas", "kind": "identity", "summary": "Quark mass matrices are diagonalized by separate left and right unitary rotations (a singular-value decomposition), and the CKM matrix is the mismatch between the up- and down-type left rotations. Parameter counting leaves (n−1)(n−2)/2 CP phases, one for three generations, and the Jarlskog invariant measures it independently of basis.", "map": "M_q=U_L^q\\,\\mathrm{diag}(m)\\,U_R^{q\\dagger},\\ V=U_L^{u\\dagger}U_L^d,\\ N_\\delta=\\frac{(n-1)(n-2)}{2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0261", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "name": "Instanton number as a Chern class; index theorem", "kind": "identity", "summary": "Instantons are classified by the second Chern (Pontryagin) number of the gauge bundle, and the θ term integrates that characteristic class. The Atiyah–Singer index theorem ties it to the Dirac operator's zero modes, which is the topological content of the axial anomaly.", "map": "Q=\\frac{1}{8\\pi^2}\\int\\mathrm{tr}\\,F\\wedge F\\in\\mathbb Z,\\ n_+-n_-=Q", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0262", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "name": "Gauge fields as connections, field strength as curvature", "kind": "identity", "summary": "A gauge potential is a connection on a principal bundle and the field strength is its curvature, the same structures as the spin connection and Riemann tensor of general relativity. Wilson loops are holonomies, and a Bianchi identity holds in both.", "map": "D_\\mu=\\partial_\\mu-igA_\\mu,\\ F=dA-ig\\,A\\wedge A\\ \\leftrightarrow\\ R=d\\omega+\\omega\\wedge\\omega", "breaks": "The gravitational connection is soldered to the tangent bundle and fixed by the metric; internal gauge connections live on an abstract bundle with no metric to determine them.", "confidence": "established", "strength": 3}
{"id": "C0263", "a": "00-foundations/measurement-and-data-analysis", "b": "06-particle-physics/collider-and-experimental-particle-physics", "name": "Collider physics as measurement at scale", "kind": "method transfer", "summary": "Collider experiments use the full measurement chain: calibration, unfolding of detector response, systematic uncertainties as nuisance parameters, and blind analyses. HEP also produced much of the statistics toolkit physicists now share (Feldman–Cousins intervals, CLs, asymptotic profile-likelihood formulae).", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0264", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "name": "Axion haloscopes at the quantum noise limit", "kind": "method transfer", "summary": "Haloscopes such as ADMX convert dark-matter axions into microwave photons in a magnetized cavity, and the ~10⁻²² W signal makes the scan rate scale as 1/T_sys². Josephson parametric amplifiers at the standard quantum limit, squeezed states (HAYSTAC) and qubit-based photon counting are the enabling detector physics.", "map": "P_{a\\to\\gamma}\\propto g_{a\\gamma\\gamma}^2\\frac{\\rho_a}{m_a}B^2VC\\,Q,\\ k_BT_{\\rm SQL}=\\hbar\\omega", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0265", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "06-particle-physics/collider-and-experimental-particle-physics", "name": "Calibration chains and resolution in collider experiments", "kind": "method transfer", "summary": "Collider experiments apply instrumentation principles at scale: test-beam and in-situ calibration with Z→ee and J/ψ resonances, luminosity from van der Meer beam-separation scans, and electronics noise and pile-up as limits on energy resolution.", "map": "\\frac{\\sigma_E}{E}=\\frac{a}{\\sqrt E}\\oplus\\frac{b}{E}\\oplus c", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0266", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "06-particle-physics/collider-and-experimental-particle-physics/particle-detectors-and-triggers", "name": "Shared signal chain: sensors, preamps and noise", "kind": "shared object", "summary": "In a particle detector, ionization or light becomes charge, which charge-sensitive preamplifiers amplify and shape, with thermal and shot noise setting the equivalent noise charge. Photomultipliers, SiPMs and silicon sensors are common to both nodes, and triggers are real-time filters working under bandwidth limits.", "map": "\\langle V_n^2\\rangle=4k_BTR\\,\\Delta f,\\ \\langle I_n^2\\rangle=2qI\\,\\Delta f", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0267", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "06-particle-physics/collider-and-experimental-particle-physics", "name": "Profile likelihood, CLs and the 5σ discovery rule", "kind": "method transfer", "summary": "LHC searches are hypothesis tests: profile-likelihood ratios with systematics as nuisance parameters, Wilks/Wald asymptotics giving Z = √q₀, CLs for exclusions, and look-elsewhere corrections, as used in the 2012 Higgs discovery.", "map": "q_0=-2\\ln\\frac{L(0,\\hat{\\hat\\theta})}{L(\\hat\\mu,\\hat\\theta)},\\ Z=\\sqrt{q_0}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0268", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "06-particle-physics/collider-and-experimental-particle-physics/machine-learning-in-hep", "name": "Simulation-based inference and the likelihood-ratio trick", "kind": "method transfer", "summary": "When a simulator yields samples but no tractable likelihood, a classifier trained to separate θ₀ samples from θ₁ samples estimates the likelihood ratio, which by Neyman–Pearson is the optimal test statistic. Neural likelihood-ratio and posterior estimation now replace binned histogram fits in some ATLAS measurements.", "map": "s(x)\\to\\frac{p(x|\\theta_1)}{p(x|\\theta_0)+p(x|\\theta_1)}\\Rightarrow r(x)=\\frac{s(x)}{1-s(x)}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0269", "a": "00-foundations/measurement-and-data-analysis/uncertainty-and-error-propagation", "b": "06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2", "name": "Judging anomalies: systematics and correlated errors", "kind": "method transfer", "summary": "Whether an anomaly is real depends on its uncertainty budget. The muon g−2 comparison turned on the hadronic-vacuum-polarization error (mutually inconsistent e⁺e⁻ data versus lattice QCD, whose 2025 consensus value agrees with experiment), and the CDF W-mass outlier is a case study in combining correlated systematics across experiments.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0270", "a": "00-foundations/symmetry-and-group-theory", "b": "06-particle-physics/standard-model", "name": "The Standard Model as representation theory", "kind": "identity", "summary": "The Standard Model is defined by its gauge group SU(3)×SU(2)×U(1) and by assigning each field to an irreducible representation, while Wigner's unitary Poincaré irreps label particles by mass and spin. Charges, multiplets and allowed couplings follow from group theory.", "map": "G_{\\rm SM}=SU(3)_c\\times SU(2)_L\\times U(1)_Y,\\ Q=T_3+Y", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0271", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "06-particle-physics/beyond-the-standard-model/axions-and-light-dark-sector", "name": "Strong CP problem and the Peccei–Quinn axion", "kind": "mechanism", "summary": "The QCD θ term is P- and T-odd and would give the neutron an electric dipole moment; the bound |d_n| < 1.8×10⁻²⁶ e cm forces |θ̄| ≲ 10⁻¹⁰. The Peccei–Quinn solution makes θ̄ dynamical: the axion, a pseudo-Goldstone boson, relaxes it to zero.", "map": "\\mathcal L_\\theta=\\bar\\theta\\frac{g_s^2}{32\\pi^2}G\\tilde G,\\ d_n\\sim10^{-16}\\bar\\theta\\,e\\,\\mathrm{cm},\\ m_a\\approx5.7\\,\\mu\\mathrm{eV}\\,\\frac{10^{12}\\,\\mathrm{GeV}}{f_a}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0272", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "06-particle-physics/standard-model/cp-violation", "name": "CP violation and the CPT theorem", "kind": "identity", "summary": "CP violation in kaons and B mesons is the experimental side of discrete-symmetry theory, and by the CPT theorem it implies T violation, since observed directly in both systems. With three generations the CKM matrix carries exactly one physical CP phase.", "map": "J=\\mathrm{Im}(V_{us}V_{cb}V_{ub}^*V_{cs}^*)\\approx3\\times10^{-5}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0273", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "06-particle-physics/standard-model/electroweak-theory", "name": "Parity violation built into chiral SU(2)_L", "kind": "historical", "summary": "Lee and Yang's 1956 proposal and Wu's 1957 cobalt-60 experiment showed that the weak interaction violates parity maximally. Electroweak theory encodes this by putting only left-handed fermions in SU(2)_L doublets (V−A currents), so the gauge representations themselves break P and C, while CP survives up to the CKM phase.", "map": "J^\\mu_W=\\bar\\nu\\gamma^\\mu\\frac{1-\\gamma^5}{2}e,\\ \\psi_L\\in\\mathbf2,\\ \\psi_R\\in\\mathbf1", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0274", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "06-particle-physics/beyond-the-standard-model/grand-unification-and-proton-decay", "name": "SU(5) and SO(10) embeddings of the Standard Model", "kind": "identity", "summary": "Grand unification is a group-embedding problem: SU(5) ⊃ SU(3)×SU(2)×U(1) fits one generation into 5̄ ⊕ 10, and SO(10) fits it into a single 16 that includes ν_R. The embedding quantizes hypercharge and fixes sin²θ_W = 3/8 at the unification scale.", "map": "\\bar5\\oplus10\\oplus1=16_{SO(10)},\\ \\sin^2\\theta_W(M_{\\rm GUT})=3/8", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0275", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "06-particle-physics/beyond-the-standard-model/supersymmetry", "name": "Graded Lie algebras evade Coleman–Mandula", "kind": "identity", "summary": "Coleman–Mandula rules out any Lie-group symmetry of the S-matrix that mixes spacetime and internal symmetries non-trivially. Haag–Łopuszański–Sohnius showed that the only loophole is a graded algebra with fermionic generators, which is supersymmetry, whose anticommutator closes on the momentum.", "map": "\\{Q_\\alpha,\\bar Q_{\\dot\\beta}\\}=2\\sigma^\\mu_{\\alpha\\dot\\beta}P_\\mu", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0276", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "06-particle-physics/standard-model/hadron-spectroscopy-and-exotics", "name": "Flavour SU(3) multiplets and colour singlets", "kind": "identity", "summary": "The eightfold way sorts hadrons into flavour-SU(3) octets and decuplets, and the Gell-Mann–Okubo mass formula predicted the Ω⁻. The quark model reads hadrons as colour singlets in tensor products of 3 and 3̄, and the same products list the allowed tetraquark and pentaquark structures.", "map": "3\\otimes\\bar3=8\\oplus1,\\ 3\\otimes3\\otimes3=10\\oplus8\\oplus8\\oplus1", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0277", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "06-particle-physics/standard-model/quantum-chromodynamics", "name": "SU(3) colour Casimirs set QCD dynamics", "kind": "identity", "summary": "Quarks sit in the fundamental and gluons in the adjoint of SU(3), and the group invariants C_F = 4/3, C_A = 3 and T_F = 1/2 fix the β-function, the splitting functions and the colour factors. Gluon self-coupling through the non-abelian structure constants gives asymptotic freedom, and large-N_c expansions treat N as a parameter.", "map": "\\beta_0=\\frac{11}{3}C_A-\\frac43T_Fn_f=11-\\frac23n_f,\\ C_F=\\frac{N^2-1}{2N}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0278", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "06-particle-physics/quantum-field-theory/anomalies-instantons-and-topology", "name": "Anomalies: Noether currents broken by quantization", "kind": "mechanism", "summary": "A classically conserved Noether current can gain a nonzero divergence from the path-integral measure. The axial anomaly explains π⁰→γγ, and its coefficient is topological: exact at one loop (Adler–Bardeen) and protected from further corrections.", "map": "\\partial_\\mu j_5^\\mu=\\frac{e^2}{16\\pi^2}\\epsilon^{\\mu\\nu\\rho\\sigma}F_{\\mu\\nu}F_{\\rho\\sigma}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0279", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills", "name": "Gauging a Noether symmetry; Ward identities", "kind": "mechanism", "summary": "Making a global symmetry local forces in a gauge field that couples to the Noether current, and Noether's second theorem says local symmetries give identities rather than new charges. In quantum theory these become the Ward–Takahashi and Slavnov–Taylor identities, which protect charge universality and renormalizability.", "map": "\\mathcal L\\supset-eA_\\mu j^\\mu,\\ \\partial_\\mu j^\\mu=0\\Rightarrow k_\\mu\\mathcal M^\\mu(k)=0,\\ Z_1=Z_2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0280", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "06-particle-physics/standard-model/higgs-boson", "name": "Higgs boson as the amplitude mode of electroweak breaking", "kind": "mechanism", "summary": "A Mexican-hat potential gives the Higgs doublet a vacuum value v = 246 GeV that breaks SU(2)×U(1) to U(1)_em, and three would-be Goldstones become the longitudinal W and Z (Higgs–Anderson mechanism). The leftover custodial SU(2) gives ρ = 1 at tree level, and the Higgs boson is the radial (amplitude) mode.", "map": "V=-\\mu^2|\\phi|^2+\\lambda|\\phi|^4,\\ v=\\mu/\\sqrt{\\lambda}=(\\sqrt2G_F)^{-1/2},\\ m_H=\\sqrt{2\\lambda}\\,v", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0281", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "06-particle-physics/standard-model/quantum-chromodynamics", "name": "Chiral symmetry breaking: pions as pseudo-Goldstones", "kind": "mechanism", "summary": "The quark condensate breaks SU(2)_L×SU(2)_R to SU(2)_V, so pions are pseudo-Goldstone bosons, light because quark masses break the symmetry explicitly. This is Nambu's superconductivity analogy carried into hadron physics, and chiral perturbation theory is its low-energy effective theory.", "map": "\\langle\\bar qq\\rangle\\neq0,\\ m_\\pi^2f_\\pi^2=-(m_u+m_d)\\langle\\bar qq\\rangle", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0282", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "name": "Anomalous dimensions and dimensional transmutation", "kind": "mechanism", "summary": "Quantum loops break naive dimensional analysis: because a renormalization scale μ enters, correlators scale with the engineering dimension plus an anomalous dimension, a case of Barenblatt's incomplete similarity. Classically scale-free QCD likewise generates Λ_QCD, a few hundred MeV, from a dimensionless coupling.", "map": "G(\\lambda x)=\\lambda^{-2(d_0+\\gamma)}G(x),\\ \\Lambda=\\mu\\exp\\left[-\\frac{2\\pi}{\\beta_0\\alpha_s(\\mu)}\\right]", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0283", "a": "00-foundations/units-and-constants/fundamental-constants", "b": "06-particle-physics/beyond-the-standard-model/precision-anomalies-and-muon-g-2", "name": "Electron g−2, the fine-structure constant and muon g−2", "kind": "shared object", "summary": "With five-loop QED, the electron g−2 gives α to sub-ppb precision, but the two atom-recoil values of α (Cs 2018, Rb 2020) disagree by more than 5σ, which limits that test of QED. The muon g−2 then tests the whole Standard Model, hadronic loops included.", "map": "a_e=\\frac{\\alpha}{2\\pi}-0.328\\left(\\frac{\\alpha}{\\pi}\\right)^2+\\dots", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0284", "a": "00-foundations/units-and-constants/fundamental-constants", "b": "06-particle-physics/quantum-field-theory/renormalization-and-running-couplings", "name": "The fine-structure constant runs", "kind": "identity", "summary": "CODATA's α⁻¹ = 137.035999177 is the Thomson-limit value of a running coupling: vacuum polarization raises α to about 1/128.9 at the Z mass, and the hadronic part of that running comes from a dispersion integral over e⁺e⁻ data. A 'constant' of this kind is a renormalized coupling quoted at a stated scale.", "map": "\\alpha(Q^2)=\\frac{\\alpha(0)}{1-\\Delta\\alpha(Q^2)},\\ \\alpha^{-1}(0)=137.035999177,\\ \\alpha^{-1}(m_Z^2)\\approx128.9", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0285", "a": "00-foundations/units-and-constants/natural-units-and-planck-scale", "b": "06-particle-physics", "name": "Natural units and mass-dimension power counting", "kind": "method transfer", "summary": "With ħ = c = 1, particle physics measures everything in powers of energy and converts back through ħc. The mass dimension of fields and couplings then decides renormalizability, and a coupling of negative dimension, such as G_F = 1.1663787×10⁻⁵ GeV⁻², signals a heavier scale.", "map": "\\hbar c=197.327\\,\\mathrm{MeV\\,fm},\\ (\\hbar c)^2=0.3894\\,\\mathrm{GeV^2\\,mb},\\ [\\mathcal L]=4", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0286", "a": "00-foundations/units-and-constants/natural-units-and-planck-scale", "b": "06-particle-physics/beyond-the-standard-model/extra-dimensions-and-hierarchy-problem", "name": "Planck scale vs weak scale: the hierarchy", "kind": "shared object", "summary": "Natural units turn the hierarchy problem into a ratio of scales, M_Pl = √(ħc/G) ≈ 1.22×10¹⁹ GeV against v = 246 GeV. Large extra dimensions (ADD) lower the fundamental gravity scale to the TeV range by diluting gravity over a volume, while a warped extra dimension (RS) produces the ratio as an exponential.", "map": "M_{\\rm Pl}^2\\sim M_*^{n+2}R^n,\\ m_{\\rm weak}\\sim e^{-k\\pi r_c}M_{\\rm Pl}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0287", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "07-nuclear-physics/nuclear-structure/ab-initio-nuclear-theory", "name": "Emulators and neural-network states for nuclear theory", "kind": "method transfer", "summary": "Eigenvector continuation and other reduced-basis emulators make Bayesian calibration of ab initio models affordable, and neural-network quantum states and NN-extrapolated no-core shell-model energies bring machine learning into the nuclear many-body problem.", "map": "H(\\theta)\\to N_{ij}=\\langle\\psi_i|H(\\theta)|\\psi_j\\rangle,\\ \\text{solve }Nc=EMc\\ \\text{in span}\\{\\psi(\\theta_k)\\}", "breaks": "Emulators interpolate within the training region and can fail where the ground state changes character.", "confidence": "current research", "strength": 2}
{"id": "C0288", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "name": "Molecular dynamics of nuclear pasta and crust", "kind": "method transfer", "summary": "Classical and quantum molecular dynamics with screened-Coulomb plus nuclear potentials simulate millions of nucleons to find pasta shapes, defects, crust breaking strain and transport coefficients.", "map": "V_{np}=ae^{-r^2/\\Lambda}+[b\\mp c]e^{-r^2/2\\Lambda};\\ V_{pp}\\ni\\frac{e^2}{r}e^{-r/\\lambda_e}", "breaks": "Semiclassical potentials miss shell effects and quantum degeneracy that can change pasta phase boundaries.", "confidence": "current research", "strength": 2}
{"id": "C0289", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "07-nuclear-physics/applied-nuclear-physics/nuclear-reactors-and-energy", "name": "Monte Carlo was invented for neutron transport", "kind": "historical", "summary": "Ulam, von Neumann and Metropolis created the Monte Carlo method in 1946-49 to follow neutron chains in fissile assemblies; today MC neutron transport (MCNP, Serpent, OpenMC) computes reactor k_eff and the Metropolis algorithm spread across physics.", "map": "k_{\\rm eff}=\\frac{N_{\\rm gen+1}}{N_{\\rm gen}};\\ p(s)=\\Sigma_te^{-\\Sigma_ts}\\Rightarrow s=-\\frac{\\ln\\xi}{\\Sigma_t}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0290", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry", "name": "Monte Carlo radiation transport for detectors and dose", "kind": "method transfer", "summary": "Detector response, shielding and dose are computed with Monte Carlo transport of photons, electrons, neutrons and ions (Geant4, FLUKA, MCNP), sampling interaction cross sections particle by particle.", "map": "P(\\text{interaction }i)=\\frac{\\Sigma_i}{\\Sigma_t};\\ \\text{dose}=\\frac{1}{m}\\sum E_{\\rm dep};\\ \\sigma_{\\rm stat}\\propto N^{-1/2}", "breaks": "Accuracy is limited by cross-section data and condensed-history approximations for charged particles.", "confidence": "established", "strength": 2}
{"id": "C0291", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "07-nuclear-physics/heavy-ion-physics/jet-quenching", "name": "Monte Carlo jet-quenching event generators", "kind": "method transfer", "summary": "Medium-modified parton showers (JEWEL, MARTINI, MATTER/LBT in JETSCAPE) sample in-medium splitting and scattering stochastically inside an evolving QGP, extending collider event generators to heavy-ion jets.", "map": "\\Delta(t_1,t_2)=\\exp\\!\\left[-\\int_{t_2}^{t_1}\\frac{dt}{t}\\int dz\\,\\frac{\\alpha_s}{2\\pi}(P(z)+\\Delta P_{\\rm med}(z,\\hat q))\\right]", "breaks": "Medium response and quantum interference (LPM) effects are implemented approximately and differ between generators.", "confidence": "current research", "strength": 1}
{"id": "C0292", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "07-nuclear-physics/nuclear-structure/ab-initio-nuclear-theory", "name": "Quantum Monte Carlo for nuclei", "kind": "method transfer", "summary": "Variational and Green's-function Monte Carlo and auxiliary-field diffusion Monte Carlo solve light nuclei and neutron matter by stochastic projection in imaginary time, sampling spin-isospin and spatial configurations.", "map": "|\\Psi_0\\rangle\\propto\\lim_{\\tau\\to\\infty}e^{-(H-E_T)\\tau}|\\Psi_T\\rangle;\\ \\sigma\\propto N^{-1/2}", "breaks": "The fermion sign problem forces constrained-path or fixed-node approximations as A grows.", "confidence": "established", "strength": 3}
{"id": "C0293", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "07-nuclear-physics/heavy-ion-physics/collective-flow-and-hydrodynamics", "name": "Shock-capturing solvers for relativistic hydrodynamics", "kind": "method transfer", "summary": "Heavy-ion hydrodynamics codes (MUSIC and others) solve second-order viscous relativistic hydro with finite-volume, Kurganov-Tadmor shock-capturing schemes shared with astrophysical and numerical relativity codes.", "map": "\\partial_tu+\\partial_xF(u)=0;\\ \\text{KT: }\\frac{du_j}{dt}=-\\frac{H_{j+1/2}-H_{j-1/2}}{\\Delta x}", "breaks": "Viscous relativistic hydro needs Israel-Stewart-type relaxation equations to remain causal, beyond standard conservation-law solvers.", "confidence": "established", "strength": 2}
{"id": "C0294", "a": "00-foundations/computational-physics/tensor-network-methods", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Entanglement and DMRG in the nuclear shell model", "kind": "method transfer", "summary": "Mode entanglement between proton and neutron orbitals is low in many nuclei, which motivates DMRG and tensor-network truncations of shell-model spaces and entanglement-guided orbital ordering borrowed from quantum chemistry.", "map": "S_{\\rm vN}=-\\mathrm{Tr}\\rho_A\\ln\\rho_A;\\ \\text{DMRG cost}\\sim\\chi^3,\\ \\chi\\sim e^{S}", "breaks": "Nuclear orbitals have no natural 1D ordering and long-range quadrupole correlations raise entanglement, so DMRG gains are smaller than in 1D lattices.", "confidence": "current research", "strength": 1}
{"id": "C0295", "a": "00-foundations/history-and-philosophy-of-physics/history-of-physics", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-fission", "name": "Fission and the birth of big science", "kind": "historical", "summary": "The 1938-39 discovery and interpretation of fission (Hahn, Strassmann, Meitner, Frisch) led within six years to reactors and weapons, the Manhattan Project and the national-laboratory system that reshaped how physics is organized and funded.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0296", "a": "00-foundations/history-and-philosophy-of-physics/history-of-physics", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "name": "Rutherford scattering and discovery of the nucleus", "kind": "historical", "summary": "Rutherford's 1911 analysis of alpha scattering revealed the nucleus and founded both nuclear physics and the scattering method that runs through particle and condensed-matter physics.", "map": "\\frac{d\\sigma}{d\\Omega}=\\left(\\frac{zZe^2}{16\\pi\\epsilon_0E}\\right)^2\\frac{1}{\\sin^4(\\theta/2)}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0297", "a": "00-foundations/history-and-philosophy-of-physics/philosophy-of-physics", "b": "07-nuclear-physics/nuclear-structure/nuclear-forces-and-chiral-eft", "name": "Nuclear EFT as a case study of levels and emergence", "kind": "historical", "summary": "Chiral EFT is a worked example in philosophy of physics of how autonomous effective levels relate to a deeper theory: nuclear physics is derivable from QCD in principle yet is organized by its own degrees of freedom, power counting and low-energy constants.", "map": "", "breaks": "Philosophical readings (autonomy versus reduction) differ, and the derivation from QCD is only partial via lattice matching.", "confidence": "established", "strength": 1}
{"id": "C0298", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "name": "Resonances as S-matrix poles and Coulomb functions", "kind": "identity", "summary": "Nuclear resonances are poles of the S-matrix on the unphysical sheet (Breit-Wigner, R-matrix, Gamow states), and charged-particle reactions and alpha decay use Coulomb wave functions and the Gamow factor from the analytic structure of the Coulomb problem.", "map": "S_\\ell(E)\\approx e^{2i\\delta_\\ell^{\\rm bg}}\\frac{E-E_R-i\\Gamma/2}{E-E_R+i\\Gamma/2};\\ C_0^2(\\eta)=\\frac{2\\pi\\eta}{e^{2\\pi\\eta}-1}", "breaks": "Threshold effects and overlapping resonances make pole extraction model-dependent.", "confidence": "established", "strength": 2}
{"id": "C0299", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "07-nuclear-physics/nuclear-structure/ab-initio-nuclear-theory", "name": "Self-consistent Green's functions and optical potentials", "kind": "method transfer", "summary": "The self-consistent Green's function method computes nuclear spectral functions from Dyson's equation, and its self-energy is a microscopic nucleon-nucleus optical potential, uniting structure and reaction theory with propagator mathematics.", "map": "G=G^0+G^0\\Sigma^\\star G,\\ \\Sigma^\\star(\\mathbf r,\\mathbf r';E)\\leftrightarrow U_{\\rm opt}(E);\\ S(k,E)=-\\tfrac1\\pi\\mathrm{Im}G", "breaks": "Truncations (ADC(n)) and three-body forces limit accuracy, and the optical potential's imaginary part needs a large model space.", "confidence": "established", "strength": 2}
{"id": "C0300", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry", "name": "Shared detector electronics and noise limits", "kind": "method transfer", "summary": "Nuclear spectroscopy defined the charge-sensitive preamplifier, pulse shaping, photomultiplier and SiPM readout and the Fano and series/parallel noise analysis now generic to instrumentation.", "map": "ENC^2=\\frac{a}{\\tau}C_{\\rm in}^2+b\\tau+c;\\ \\sigma_E^2=FwE+\\sigma_{\\rm el}^2", "breaks": "Optimal shaping depends on detector capacitance and leakage; the noise model is generic but parameters are detector-specific.", "confidence": "established", "strength": 2}