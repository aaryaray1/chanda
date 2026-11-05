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

# Packet 00-4 (100 records)

{"id": "C0301", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "07-nuclear-physics/heavy-ion-physics/collective-flow-and-hydrodynamics", "name": "Bayesian extraction of QGP transport coefficients", "kind": "method transfer", "summary": "Temperature-dependent eta/s and zeta/s are inferred by Bayesian calibration of hydrodynamic models against flow data, with Gaussian-process emulators and posterior uncertainty, the same parameter-estimation machinery used in cosmology.", "map": "p(\\theta|D)\\propto\\exp\\!\\left[-\\tfrac12(y(\\theta)-y_{\\rm exp})^T\\Sigma^{-1}(y(\\theta)-y_{\\rm exp})\\right]p(\\theta)", "breaks": "Posteriors depend on the model family (initial state, freeze-out), so systematic model uncertainty can dominate.", "confidence": "current research", "strength": 2}
{"id": "C0302", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "name": "Bayesian multi-messenger inference of the dense-matter EOS", "kind": "method transfer", "summary": "The neutron-star EOS is inferred by Bayesian combination of chiral-EFT priors, heavy-pulsar masses, NICER pulse profiles and GW tidal deformabilities, using nonparametric (Gaussian-process, neural-network) EOS priors.", "map": "p(\\mathrm{EOS}|d)\\propto p(\\mathrm{EOS})\\prod_ip(d_i|M_i,R_i,\\Lambda_i)\\,p(M_i,R_i|\\mathrm{EOS})", "breaks": "Prior choices at densities without data strongly shape posteriors on the maximum mass and quark-matter questions.", "confidence": "current research", "strength": 2}
{"id": "C0303", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions", "name": "Neutron-lifetime puzzle and combining discrepant data", "kind": "method transfer", "summary": "Beam (about 888 s) and bottle (about 878 s) neutron lifetimes disagree by about 4 sigma; PDG scale factors, Birge ratios and Bayesian treatments of unknown systematics are used to combine them, and the choice matters for BBN and |V_ud|.", "map": "S=\\sqrt{\\chi^2/(N-1)},\\ \\sigma_{\\rm comb}\\to S\\sigma;\\ \\tau_n^{\\rm beam}-\\tau_n^{\\rm bottle}\\approx9\\ \\text{s}", "breaks": "Statistics cannot decide whether a systematic error or new physics (dark decay channels) causes the gap.", "confidence": "current research", "strength": 2}
{"id": "C0304", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "07-nuclear-physics/nuclear-structure/nuclear-forces-and-chiral-eft", "name": "Bayesian EFT truncation errors for nuclear forces", "kind": "method transfer", "summary": "Chiral EFT predictions now carry theory error bars from Bayesian models of the omitted orders in Q/Lambda, treated as random coefficients with a learned scale, an EFT application of statistical inference.", "map": "y_k=y_{\\rm ref}\\sum_{n=0}^kc_nQ^n,\\ \\delta y_k\\approx y_{\\rm ref}\\bar c\\,\\frac{Q^{k+1}}{\\sqrt{1-Q^2}},\\ c_n\\sim\\mathcal N(0,\\bar c^2)", "breaks": "The assumption of natural, independent coefficients may fail when power counting is inconsistent.", "confidence": "current research", "strength": 2}
{"id": "C0305", "a": "00-foundations/measurement-and-data-analysis/uncertainty-and-error-propagation", "b": "07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay", "name": "Radioactive decay as the model Poisson process", "kind": "identity", "summary": "Radioactive decay is the textbook Poisson process: counts have variance equal to the mean, intervals are exponential, and counting statistics, dead-time and background subtraction are the reference examples of uncertainty propagation.", "map": "P(n)=\\frac{\\mu^ne^{-\\mu}}{n!},\\ \\sigma_n=\\sqrt\\mu;\\ \\sigma_{\\rm net}^2=\\frac{N_s}{t_s^2}+\\frac{N_b}{t_b^2}", "breaks": "Detector dead time and electronics make observed counts sub-Poissonian, and very short-lived sources violate stationarity.", "confidence": "established", "strength": 2}
{"id": "C0306", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "07-nuclear-physics/hadron-and-nucleon-structure/nucleon-spin-and-form-factors", "name": "Neutron and nuclear EDMs as tests of T and CP", "kind": "mechanism", "summary": "A permanent electric dipole moment of the neutron or a nucleus violates P and T; the neutron EDM bound underlies the strong CP problem, and octupole-deformed nuclei such as 225Ra enhance Schiff moments by orders of magnitude.", "map": "H=-d\\,\\mathbf E\\cdot\\frac{\\mathbf S}{S}\\ (P\\text{-odd},T\\text{-odd});\\ |d_n|<1.8\\times10^{-26}\\ e\\,\\text{cm}\\Rightarrow|\\bar\\theta|\\lesssim10^{-10}", "breaks": "Converting EDM limits to CP-violating parameters needs nuclear and hadronic matrix elements with large uncertainties.", "confidence": "established", "strength": 2}
{"id": "C0307", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions", "name": "Parity violation in nuclear beta decay", "kind": "historical", "summary": "Wu's 1957 measurement of the electron asymmetry from polarized 60Co showed the weak interaction maximally violates parity, establishing the V-A structure of beta decay.", "map": "W(\\theta)\\propto1+A\\frac{\\langle\\mathbf J\\rangle\\cdot\\mathbf p_e}{JE_e},\\ A=-1\\ \\text{for }^{60}\\mathrm{Co}\\ (\\text{pure GT})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0308", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "07-nuclear-physics/nuclear-structure/nuclear-forces-and-chiral-eft", "name": "Isospin and Wigner SU(4) symmetry of nuclear forces", "kind": "identity", "summary": "Charge independence of nuclear forces makes isospin an SU(2) symmetry with protons and neutrons as a doublet; Wigner's combined spin-isospin SU(4) supermultiplets explain why light-nucleus binding and Gamow-Teller patterns follow the 4-fold degeneracy.", "map": "[T_i,T_j]=i\\epsilon_{ijk}T_k,\\ N=(p,n)\\in\\mathbf2;\\ \\text{SU(4)}\\supset\\text{SU(2)}_S\\otimes\\text{SU(2)}_T,\\ \\mathbf4=(\\tfrac12,\\tfrac12)", "breaks": "Isospin is broken by Coulomb forces and the u-d quark mass difference (~1 percent), and SU(4) is broken strongly by spin-orbit forces in heavier nuclei.", "confidence": "established", "strength": 3}
{"id": "C0309", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Elliott SU(3) and interacting-boson dynamical symmetries", "kind": "identity", "summary": "Collective rotation emerges from the shell model through Elliott's SU(3) for the harmonic oscillator, and the interacting boson model's U(6) group chains U(5), SU(3) and O(6) give the vibrational, rotational and gamma-soft limits of nuclear spectra.", "map": "\\text{U(6)}\\supset\\{\\text{U(5)},\\text{SU(3)},\\text{O(6)}\\}\\supset\\text{O(3)};\\ E_{\\rm SU(3)}\\propto-C_2(\\lambda,\\mu)+\\tfrac34L(L+1)", "breaks": "Real nuclei lie between limits and spin-orbit coupling breaks Elliott SU(3) beyond the sd shell (pseudo- and quasi-SU(3) partly restore it).", "confidence": "established", "strength": 3}
{"id": "C0310", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Seniority and quasispin: pairing as an SU(2) algebra", "kind": "identity", "summary": "Racah's seniority scheme and Kerman's quasispin show that pair creation and annihilation in a j-shell close an SU(2) algebra, which makes the pairing Hamiltonian exactly solvable and explains constant 2+ energies in semi-magic nuclei.", "map": "S^+=\\sum_{m>0}(-1)^{j-m}a^\\dagger_{jm}a^\\dagger_{j-m},\\ [S^+,S^-]=2S^0;\\ E=-G(S(S+1)-S_0(S_0-1))", "breaks": "Seniority is exact only in a single j-shell or with degenerate orbits; multi-j shells and quadrupole forces mix seniorities.", "confidence": "established", "strength": 2}
{"id": "C0311", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions", "name": "Conserved vector current and superallowed ft values", "kind": "mechanism", "summary": "The vector weak current is the Noether current of isospin (CVC), so Fermi matrix elements of superallowed 0+ to 0+ decays are fixed by symmetry; after small isospin-breaking and radiative corrections all ft values agree, which tests CVC and gives |V_ud|.", "map": "\\partial_\\mu V^\\mu_a=0,\\ \\langle0^+|T_\\pm|0^+\\rangle=\\sqrt2;\\ \\mathcal Ft=ft(1+\\delta_R')(1+\\delta_{NS}-\\delta_C)=\\text{const}", "breaks": "Isospin-breaking corrections delta_C are model-dependent and are the leading theory uncertainty.", "confidence": "established", "strength": 3}
{"id": "C0312", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "07-nuclear-physics/heavy-ion-physics/qcd-phase-diagram-and-critical-point", "name": "Chiral restoration and O(4) universality", "kind": "mechanism", "summary": "The QCD transition is chiral-symmetry restoration; Pisarski and Wilczek argued that for two massless flavours it falls in the 3D O(4) universality class, and lattice data at physical masses show a crossover with O(4) scaling remnants.", "map": "\\langle\\bar qq\\rangle\\sim(T_c-T)^\\beta,\\ \\beta_{O(4)}\\approx0.38;\\ \\text{order parameter: }\\Sigma=\\langle\\bar q_Lq_R\\rangle\\in O(4)", "breaks": "Explicit quark masses turn the transition into a crossover, and the U(1)_A anomaly strength affects the universality class.", "confidence": "established", "strength": 3}
{"id": "C0313", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "07-nuclear-physics/nuclear-structure/nuclear-forces-and-chiral-eft", "name": "Pions as Goldstone bosons organize nuclear forces", "kind": "mechanism", "summary": "Spontaneous breaking of QCD's chiral SU(2)xSU(2) symmetry makes pions light pseudo-Goldstone bosons with derivative couplings; this fixes one-pion exchange as the long-range nuclear force and Weinberg's power counting in Q/Lambda_chi.", "map": "SU(2)_L\\times SU(2)_R\\to SU(2)_V;\\ m_\\pi^2f_\\pi^2=-(m_u+m_d)\\langle\\bar qq\\rangle;\\ V_{1\\pi}\\propto\\frac{g_A^2}{f_\\pi^2}\\frac{(\\sigma_1\\cdot q)(\\sigma_2\\cdot q)}{q^2+m_\\pi^2}", "breaks": "Nonperturbative NN binding forces iteration of the potential, and power-counting consistency in that regime is debated.", "confidence": "established", "strength": 3}
{"id": "C0314", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Nuclear deformation and pairing as broken symmetries", "kind": "mechanism", "summary": "Deformed mean fields break rotational symmetry and BCS pairing breaks particle number; in finite nuclei the broken symmetry shows up as rotational bands (Anderson-tower rotations) and pairing rotations, restored by projection.", "map": "E_J=\\frac{\\hbar^2}{2\\mathcal I}J(J+1)\\ \\text{(rotational tower)};\\ E_{\\rm pair\\ rot}\\propto\\frac{(N-N_0)^2}{2\\mathcal I_{\\rm pair}}", "breaks": "A finite system cannot truly break a continuous symmetry; the 'Goldstone modes' are discrete rotational excitations whose spacing shrinks only as A grows.", "confidence": "established", "strength": 3}
{"id": "C0315", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-fission", "name": "Taylor's blast-wave estimate of a fission yield", "kind": "historical", "summary": "G. I. Taylor estimated the energy of the first atomic explosion from photographs of the fireball radius versus time using only dimensional analysis, the classic Taylor-Sedov scaling.", "map": "R(t)\\approx C\\left(\\frac{Et^2}{\\rho}\\right)^{1/5}\\Rightarrow E\\approx\\frac{\\rho R^5}{t^2}\\sim10^{14}\\ \\text{J}", "breaks": "Scaling fixes the yield only up to the dimensionless constant C(gamma), which needs a similarity solution.", "confidence": "established", "strength": 2}
{"id": "C0316", "a": "00-foundations/units-and-constants/fundamental-constants", "b": "07-nuclear-physics/applied-nuclear-physics/nuclear-reactors-and-energy", "name": "Oklo natural reactor bounds varying constants", "kind": "mechanism", "summary": "The 2-billion-year-old Oklo natural fission reactor depleted 149Sm through its 0.1 eV neutron resonance; the resonance position today matches, bounding changes of the fine-structure constant to about 1e-7 over that time.", "map": "\\Delta E_r\\approx\\left(\\frac{\\partial E_r}{\\partial\\alpha}\\right)\\delta\\alpha,\\ |\\Delta E_r|\\lesssim0.1\\ \\text{eV}\\Rightarrow\\left|\\frac{\\delta\\alpha}{\\alpha}\\right|\\lesssim10^{-7}", "breaks": "The bound depends on modelling the reactor's neutron spectrum and temperature and on assuming only alpha varies.", "confidence": "established", "strength": 2}
{"id": "C0317", "a": "00-foundations/units-and-constants/fundamental-constants", "b": "07-nuclear-physics/hadron-and-nucleon-structure/nucleon-spin-and-form-factors", "name": "Proton radius and the Rydberg constant in CODATA", "kind": "shared object", "summary": "The proton charge radius enters hydrogen energy levels, so it is adjusted jointly with the Rydberg constant; the muonic-hydrogen radius (0.84 fm) shifted the CODATA values of both after the proton-radius puzzle.", "map": "\\Delta E_{nS}^{\\rm fs}=\\frac{2}{3n^3}\\frac{(Z\\alpha)^4m_r^3c^4}{\\hbar^2}r_p^2;\\ m_r(\\mu p)/m_r(ep)\\approx186", "breaks": "Electron-scattering extractions depend on form-factor fit extrapolation to Q^2 = 0.", "confidence": "established", "strength": 3}
{"id": "C0318", "a": "00-foundations/units-and-constants/fundamental-constants", "b": "07-nuclear-physics/nuclear-astrophysics/big-bang-nucleosynthesis", "name": "BBN constrains variation of constants", "kind": "mechanism", "summary": "Primordial helium and deuterium are sensitive to the neutron-proton mass difference, deuteron binding, G_F and G at T ~ 1 MeV, so BBN bounds variations of the fine-structure constant, quark masses and Newton's constant over 13.8 Gyr.", "map": "\\frac{n}{p}=e^{-Q/T_f},\\ Q=m_n-m_p\\ (\\text{depends on }\\alpha,m_d-m_u);\\ \\delta Y_p\\propto\\delta Q,\\ \\delta T_f", "breaks": "Correlated variations in unified theories make single-constant bounds model-dependent.", "confidence": "established", "strength": 2}
{"id": "C0319", "a": "00-foundations/units-and-constants/fundamental-constants", "b": "07-nuclear-physics/nuclear-reactions-and-decays/radioactive-decay-and-alpha-decay", "name": "Thorium-229 nuclear clock and variation of alpha", "kind": "mechanism", "summary": "The 8.4 eV 229Th isomer energy results from near-cancellation of MeV-scale Coulomb and nuclear energies, so a nuclear clock is predicted to be orders of magnitude more sensitive to drifts of the fine-structure constant and quark masses than atomic clocks.", "map": "\\frac{\\delta\\omega}{\\omega}=K_\\alpha\\frac{\\delta\\alpha}{\\alpha}+K_q\\frac{\\delta(m_q/\\Lambda_{\\rm QCD})}{m_q/\\Lambda_{\\rm QCD}},\\ |K_\\alpha|\\sim10^3\\text{–}10^4", "breaks": "The enhancement factor depends on the difference of Coulomb energies of two nuclear states, which is uncertain to a factor of a few.", "confidence": "current research", "strength": 2}
{"id": "C0320", "a": "00-foundations/units-and-constants/si-units-and-2019-redefinition", "b": "07-nuclear-physics/applied-nuclear-physics/nuclear-data-and-isotope-production", "name": "Atomic masses, the mole and the 2019 SI", "kind": "shared object", "summary": "Nuclear masses are measured as ratios to 12C (the unified atomic mass unit); Penning-trap mass ratios feed CODATA, and the 28Si-sphere Avogadro determination behind the new kilogram relied on isotopic enrichment and neutron-activation impurity analysis.", "map": "m_u=\\tfrac1{12}m(^{12}\\mathrm C);\\ N_A=\\frac{8V_{\\rm sphere}M(^{28}\\mathrm{Si})}{a^3m_{\\rm sphere}}", "breaks": "Since 2019 the mole is defined by a fixed N_A, so m_u is no longer exactly 1 g/mol divided by N_A.", "confidence": "established", "strength": 2}
{"id": "C0321", "a": "00-foundations/computational-physics", "b": "08-condensed-matter/crystals-and-electronic-structure/density-functional-theory", "name": "DFT as computational physics' largest application", "kind": "method transfer", "summary": "Kohn-Sham DFT with plane waves, pseudopotentials, FFTs and iterative eigensolvers is among the most heavily used computational methods in all of science; numerical analysis (basis convergence, k-point sampling, self-consistency mixing) controls its accuracy.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0322", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "08-condensed-matter/crystals-and-electronic-structure/density-functional-theory", "name": "Machine-learned interatomic potentials trained on DFT", "kind": "method transfer", "summary": "Neural-network and kernel potentials fitted to DFT energies and forces reach near-DFT accuracy at the cost of classical force fields, enabling million-atom, nanosecond simulations of phase transitions, defects and hydrides.", "map": "E=\\sum_iE_i(\\mathbf G_i),\\ \\mathcal L=\\sum(E-E_{\\text{DFT}})^2+w\\sum|\\mathbf F-\\mathbf F_{\\text{DFT}}|^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0323", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "08-condensed-matter/soft-matter/glasses-and-jamming", "name": "Machine-learned structure predicts glassy dynamics", "kind": "method transfer", "summary": "A machine-learned structural order parameter ('softness') trained on local particle environments predicts which particles in a supercooled liquid will rearrange, connecting hidden structure to dynamical heterogeneity.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0324", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "Neural-network quantum states", "kind": "method transfer", "summary": "Neural networks used as variational wavefunctions (restricted Boltzmann machines, then transformers) are optimized by variational Monte Carlo and now compete with DMRG and QMC on frustrated magnets and the doped Hubbard model.", "map": "\\psi_\\theta(\\mathbf s)=\\sum_{\\mathbf h}e^{\\sum_ia_is_i+\\sum_jb_jh_j+\\sum_{ij}W_{ij}h_js_i},\\ E(\\theta)=\\frac{\\langle\\psi_\\theta|H|\\psi_\\theta\\rangle}{\\langle\\psi_\\theta|\\psi_\\theta\\rangle}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0325", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "08-condensed-matter/crystals-and-electronic-structure/density-functional-theory", "name": "Ab initio molecular dynamics", "kind": "method transfer", "summary": "Car-Parrinello and Born-Oppenheimer molecular dynamics integrate nuclear motion on DFT forces computed on the fly, unifying electronic structure with MD for liquids, melting and high-pressure phases.", "map": "M_I\\ddot{\\mathbf R}_I=-\\nabla_{\\mathbf R_I}E_{KS}[\\{\\phi_i\\},\\{\\mathbf R\\}];\\ \\mu\\ddot\\phi_i=-\\frac{\\delta E}{\\delta\\phi_i^*}+\\sum_j\\Lambda_{ij}\\phi_j\\ (\\text{CP})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0326", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "08-condensed-matter/soft-matter/glasses-and-jamming", "name": "Molecular dynamics of supercooled liquids and jamming", "kind": "method transfer", "summary": "Simulations of Lennard-Jones and soft-sphere mixtures supply dynamical heterogeneity, the Kauzmann and mode-coupling tests and jamming criticality, but are limited to ~microsecond times, about 10^-6 of the laboratory glass-transition timescale.", "map": "V_{LJ}=4\\epsilon[(\\sigma/r)^{12}-(\\sigma/r)^6];\\ \\tau_\\alpha\\sim10^{-12}\\to10^{2}\\,\\text{s at }T_g", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0327", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "08-condensed-matter/soft-matter/polymers", "name": "Bead-spring simulations of entangled polymers", "kind": "method transfer", "summary": "The Kremer-Grest bead-spring model showed by MD the crossover from Rouse to reptation dynamics in entangled melts and remains the standard coarse-grained test bed for polymer rheology.", "map": "U_{\\text{FENE}}=-\\tfrac12kR_0^2\\ln[1-(r/R_0)^2]+U_{\\text{WCA}};\\ g_1(t)\\sim t^{1/4}\\ (\\text{reptation regime})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0328", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "name": "Cluster Monte Carlo for magnetic spin models", "kind": "method transfer", "summary": "Critical slowing down in Metropolis simulations of Ising and Heisenberg magnets was beaten by Swendsen-Wang and Wolff cluster updates built on the Fortuin-Kasteleyn mapping; loop and worm algorithms extend this to quantum magnets.", "map": "p_{\\text{bond}}=1-e^{-2\\beta J};\\ \\tau\\sim\\xi^z,\\ z_{\\text{Metropolis}}\\approx2.17\\to z_{SW}\\approx0.25\\ (2D\\ \\text{Ising})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0329", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "Quantum Monte Carlo and the fermion sign problem", "kind": "method transfer", "summary": "Determinant, auxiliary-field and diagrammatic QMC map correlated electrons onto Monte Carlo sampling in imaginary time; for doped fermions and frustrated magnets the weights turn negative and the sign problem makes cost exponential.", "map": "\\langle O\\rangle=\\frac{\\sum_cO_c|w_c|\\,\\mathrm{sgn}\\,w_c}{\\sum_c|w_c|\\,\\mathrm{sgn}\\,w_c},\\ \\langle\\mathrm{sgn}\\rangle\\sim e^{-\\beta N\\Delta f}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0330", "a": "00-foundations/computational-physics/tensor-network-methods", "b": "08-condensed-matter/strongly-correlated-electrons", "name": "Entanglement structure of correlated ground states", "kind": "method transfer", "summary": "Area-law entanglement in gapped correlated phases is what makes tensor-network compression possible; deviations (log corrections at criticality, topological entanglement entropy) diagnose the phase.", "map": "S_A=\\alpha L-\\gamma+\\ldots\\ (2D\\ \\text{gapped}),\\ S_A=\\frac c3\\ln\\ell\\ (1D\\ \\text{critical})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0331", "a": "00-foundations/computational-physics/tensor-network-methods", "b": "08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order", "name": "Topological order as an entanglement pattern", "kind": "method transfer", "summary": "Topological order shows up as a constant negative correction to area-law entanglement, the topological entanglement entropy gamma=ln D, and string-net and toric-code ground states are exact PEPS with virtual symmetries; tensor networks thereby identify topological phases numerically.", "map": "S_A=\\alpha L-\\gamma,\\ \\gamma=\\ln\\mathcal D,\\ \\mathcal D=\\sqrt{\\textstyle\\sum_ad_a^2}\\ (\\text{toric code: }\\ln2)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0332", "a": "00-foundations/computational-physics/tensor-network-methods", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "DMRG and tensor networks for correlated electrons", "kind": "method transfer", "summary": "DMRG, invented for quantum spin chains, is a variational method over matrix product states; PEPS, MERA and their 2D cylinder implementations now give benchmark ground states of Hubbard and frustrated spin models, limited by area-law entanglement growth.", "map": "|\\psi\\rangle=\\sum\\mathrm{Tr}(A^{s_1}\\cdots A^{s_N})|s_1\\ldots s_N\\rangle,\\ S\\le\\log\\chi", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0333", "a": "00-foundations/computational-physics/tensor-network-methods", "b": "08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals", "name": "MERA and entanglement at quantum critical points", "kind": "method transfer", "summary": "Critical ground states violate the area law logarithmically; the multiscale entanglement renormalization ansatz (MERA) captures this with a scale-invariant tensor network that implements real-space RG and resembles a discretized AdS geometry.", "map": "S(\\ell)=\\frac c3\\ln\\frac\\ell a\\ (\\text{1+1D CFT});\\ \\text{MERA layers}\\leftrightarrow\\text{RG scale}\\leftrightarrow\\text{radial AdS coordinate}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0334", "a": "00-foundations/history-and-philosophy-of-physics/philosophy-of-physics", "b": "08-condensed-matter/strongly-correlated-electrons", "name": "Emergence and the limits of reductionism", "kind": "historical", "summary": "Anderson's 'More is different' and Laughlin and Pines' 'Theory of Everything' used broken symmetry, quasiparticles and protected quantization in correlated matter as the central examples in the philosophical debate over emergence and reduction.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0335", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "Kramers-Kronig relations for lattice and optical response", "kind": "identity", "summary": "Causality makes the dielectric and phonon response functions analytic in the upper half-plane, so absorption and dispersion are Hilbert transforms of each other; this links the TO-phonon resonance, reflectivity and the Lyddane-Sachs-Teller relation.", "map": "\\mathrm{Re}\\,\\epsilon(\\omega)-1=\\frac2\\pi\\mathcal P\\int_0^\\infty\\frac{\\omega'\\mathrm{Im}\\,\\epsilon(\\omega')}{\\omega'^2-\\omega^2}d\\omega';\\ \\frac{\\omega_{LO}^2}{\\omega_{TO}^2}=\\frac{\\epsilon(0)}{\\epsilon(\\infty)}", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C0336", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons", "name": "Bloch theorem as Floquet theory of periodic ODEs", "kind": "identity", "summary": "Bloch's theorem is Floquet's 1883 theorem for linear differential equations with periodic coefficients; bands and gaps of the Kronig-Penney and nearly-free-electron models are the stability and instability zones of Hill's and Mathieu's equations.", "map": "\\psi''+[E-V(x)]\\psi=0,\\ V(x+a)=V(x)\\Rightarrow\\psi(x+a)=e^{ika}\\psi(x);\\ |\\tfrac12\\mathrm{Tr}\\,M(E)|\\le1\\Leftrightarrow\\text{band}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0337", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "08-condensed-matter/strongly-correlated-electrons/numerical-many-body-methods", "name": "Many-body Green's functions and DMFT", "kind": "method transfer", "summary": "Correlated-electron theory is built on Matsubara Green's functions and self-energies; DMFT maps the lattice problem onto an impurity whose local Green's function is fixed self-consistently, an operational use of Dyson's equation.", "map": "G^{-1}=G_0^{-1}-\\Sigma;\\ G_{\\text{loc}}(i\\omega_n)=\\sum_{\\mathbf k}[i\\omega_n+\\mu-\\epsilon_{\\mathbf k}-\\Sigma(i\\omega_n)]^{-1}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0338", "a": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "b": "08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons", "name": "Bloch bands as an eigenvalue problem", "kind": "method transfer", "summary": "Band structure is the spectral decomposition of a lattice-translation-invariant Hamiltonian: Bloch's theorem block-diagonalizes it by crystal momentum, leaving finite Hermitian matrices H(k) to diagonalize.", "map": "[H,T_{\\mathbf R}]=0\\Rightarrow H=\\bigoplus_{\\mathbf k}H(\\mathbf k),\\ H(\\mathbf k)u_{n\\mathbf k}=E_n(\\mathbf k)u_{n\\mathbf k}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0339", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "Berry curvature as the curvature of a bundle", "kind": "identity", "summary": "Berry connection and curvature are a U(1) connection and its curvature on the bundle of Bloch states over the Brillouin-zone torus; the Chern number is the first Chern class and the quantum geometric tensor combines a metric with this curvature.", "map": "\\mathcal A=i\\langle u|du\\rangle,\\ \\Omega=d\\mathcal A,\\ C=\\frac1{2\\pi}\\int_{T^2}\\Omega\\in\\mathbb Z;\\ Q_{\\mu\\nu}=g_{\\mu\\nu}-\\tfrac i2\\Omega_{\\mu\\nu}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0340", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "name": "Shot noise and Johnson noise in conductors", "kind": "identity", "summary": "The Johnson-Nyquist and Schottky formulas of instrumentation are limits of mesoscopic noise theory: shot noise reduced by the Fano factor sum T(1-T)/sum T, and measuring it revealed the e/3 charge of fractional quantum Hall quasiparticles.", "map": "S_I=2qIF,\\ F=\\frac{\\sum_nT_n(1-T_n)}{\\sum_nT_n};\\ S_I=4k_BTG\\ (V=0)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0341", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Superconducting cryogenic sensors", "kind": "method transfer", "summary": "Transition-edge sensors, kinetic-inductance detectors and superconducting nanowire single-photon detectors turn the superconducting transition and the small gap into energy-resolving, photon-counting sensors for X-ray, optical and millimetre-wave astronomy and quantum optics.", "map": "\\Delta E_{\\text{FWHM}}\\approx2.355\\sqrt{4k_BT^2C/\\alpha}\\ (\\text{TES})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0342", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "SQUIDs as instrumentation", "kind": "method transfer", "summary": "SQUIDs are the most sensitive magnetic-flux detectors and the readout amplifiers of cryogenic sensor arrays; their noise is set by Josephson-junction physics and can approach the quantum limit.", "map": "S_\\Phi^{1/2}\\sim10^{-6}\\Phi_0/\\sqrt{\\text{Hz}},\\ \\Phi_0=h/2e", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0343", "a": "00-foundations/symmetry-and-group-theory", "b": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "name": "Space groups and representations in crystals", "kind": "method transfer", "summary": "The 230 space groups and their irreducible representations label Bloch bands, phonon branches and selection rules, explain systematic absences in diffraction, and the crystallographic restriction (no 5-fold axes) made quasicrystals a surprise.", "map": "\\{R|\\mathbf t\\}\\psi_{n\\mathbf k}=\\psi_{n,R\\mathbf k};\\ \\text{little group }G_{\\mathbf k}\\ \\text{irreps label bands};\\ 2\\cos(2\\pi/n)\\in\\mathbb Z", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0344", "a": "00-foundations/symmetry-and-group-theory", "b": "08-condensed-matter/strongly-correlated-electrons/fractionalization-and-topological-order", "name": "Topological order as broken higher-form symmetry", "kind": "method transfer", "summary": "Generalized (higher-form) global symmetries act on line and surface operators; deconfined topological phases such as the toric code spontaneously break a 1-form symmetry, extending the symmetry-breaking classification of phases to topological order and its mixed-state versions.", "map": "U_g(\\Sigma^{d-p-1})W(C^p)=e^{i\\alpha\\,\\mathrm{Link}(\\Sigma,C)}W(C^p);\\ \\langle W(C)\\rangle\\sim\\text{perimeter law}\\Rightarrow\\text{broken 1-form}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0345", "a": "00-foundations/symmetry-and-group-theory", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "Topological quantum chemistry via band representations", "kind": "method transfer", "summary": "Induced (band) representations of space groups decide whether a set of bands can come from localized symmetric Wannier orbitals; when they cannot, the bands are topological, which turned representation theory into a high-throughput topology classifier.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0346", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "08-condensed-matter/magnetism/altermagnetism", "name": "Altermagnets break time reversal without magnetization", "kind": "mechanism", "summary": "Altermagnets lift Kramers spin degeneracy by breaking the combined time-reversal-plus-translation symmetry of ordinary antiferromagnets while keeping zero net moment, so T-odd responses (anomalous Hall, spin splitting) appear without stray fields.", "map": "\\Theta t_{1/2}\\ \\text{(AFM, preserved)}\\to\\text{broken};\\ [C_2\\|R]\\ \\text{keeps }\\sum_{\\mathbf k}(E_\\uparrow-E_\\downarrow)=0", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0347", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "The tenfold way from T, C and chiral symmetry", "kind": "identity", "summary": "Gapped free-fermion phases fall into ten Altland-Zirnbauer classes set by whether time reversal T, particle-hole C and chiral S symmetries are present and square to +1 or -1; with dimension this gives the periodic table of topological insulators and superconductors.", "map": "T^2,C^2\\in\\{0,\\pm1\\},\\ S=TC\\Rightarrow10\\ \\text{classes};\\ \\text{e.g. AII }(T^2=-1):\\ \\mathbb Z_2\\ (d=2,3)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0348", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "08-condensed-matter/topological-matter/topological-insulators", "name": "Kramers pairs protect topological insulators", "kind": "mechanism", "summary": "The antiunitary time-reversal operator with Theta^2=-1 forces Kramers degeneracy at time-reversal-invariant momenta, giving the Z2 invariant and protecting the surface Dirac cone against non-magnetic backscattering.", "map": "\\Theta=i\\sigma_yK,\\ \\Theta^2=-1\\Rightarrow\\langle\\psi|\\Theta\\psi\\rangle=0;\\ \\nu\\in\\mathbb Z_2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0349", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "08-condensed-matter/magnetism/altermagnetism", "name": "Spin-group symmetry classification of altermagnets", "kind": "method transfer", "summary": "Altermagnets are defined by spin-group symmetry, in which spin and lattice operations act independently when spin-orbit coupling is negligible; opposite-spin sublattices related by a rotation rather than a translation or inversion give d-, g- or i-wave spin splitting.", "map": "[C_2\\|C_{4z}]\\ \\text{(spin flip }\\otimes\\text{ lattice rotation)}\\Rightarrow E_\\uparrow(\\mathbf k)-E_\\downarrow(\\mathbf k)\\propto k_xk_y", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0350", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "08-condensed-matter/topological-matter/topological-semimetals", "name": "Chiral anomaly breaks a Noether current in Weyl semimetals", "kind": "identity", "summary": "The axial charge of Weyl fermions is conserved classically by Noether's theorem but not quantum mechanically: parallel E and B pump electrons between Weyl nodes of opposite chirality at the Adler-Bell-Jackiw rate, seen as negative longitudinal magnetoresistance.", "map": "\\partial_\\mu j^\\mu_5=\\frac{e^2}{2\\pi^2\\hbar^2c}\\mathbf E\\cdot\\mathbf B\\leftrightarrow\\frac{dN_\\pm}{dt}=\\pm\\frac{e^2}{h^2}\\mathbf E\\cdot\\mathbf B", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0351", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "name": "Magnons as Goldstone bosons and their counting", "kind": "identity", "summary": "Magnons are the Goldstone modes of broken spin-rotation symmetry: antiferromagnets have two linearly dispersing type-A modes, while ferromagnets have one quadratic type-B mode because the broken generators have a non-zero commutator expectation; Mermin-Wagner forbids such order in 2D at T>0.", "map": "n_{NG}=n_{BG}-\\tfrac12\\mathrm{rank}\\,\\rho,\\ \\rho_{ab}=\\lim\\frac{-i}{V}\\langle[Q_a,j_b^0]\\rangle;\\ \\omega\\propto k^2\\ (\\text{FM}),\\ \\omega\\propto k\\ (\\text{AFM})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0352", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "08-condensed-matter/magnetism/frustrated-magnets-and-spin-liquids", "name": "Spin liquids: order without symmetry breaking", "kind": "mechanism", "summary": "Quantum spin liquids are the main counterexample to the Landau paradigm: frustration prevents spontaneous symmetry breaking down to T=0, and the low-energy theory instead has emergent gauge fields and fractionalized spinons, so the phase is classified by topology rather than an order parameter.", "map": "f=|\\theta_{CW}|/T_N\\gg1;\\ \\text{no local }\\langle\\mathbf S_i\\rangle\\neq0,\\ \\text{emergent }\\mathbb Z_2\\text{ or U(1) gauge field}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0353", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "08-condensed-matter/soft-matter/liquid-crystals", "name": "Nematic order, Goldstone modes and homotopy of defects", "kind": "identity", "summary": "A nematic breaks rotational symmetry with order-parameter space RP^2; its director fluctuations are Goldstone modes and its defects are classified by homotopy groups, pi_1(RP^2)=Z_2 allowing half-integer disclinations, which is the general topological theory of defects in ordered media.", "map": "\\mathcal M=SO(3)/D_\\infty=\\mathbb{RP}^2,\\ \\pi_1=\\mathbb Z_2,\\ \\pi_2=\\mathbb Z;\\ Q_{ij}=S(n_in_j-\\tfrac13\\delta_{ij})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0354", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "08-condensed-matter/superconductivity", "name": "Superconductivity as broken U(1) gauge symmetry", "kind": "identity", "summary": "A superconductor is the condensed-matter Higgs phase: a charged condensate with a phase that breaks U(1), whose would-be Goldstone mode is eaten by the photon, giving the Meissner effect and flux quantization.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0355", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "08-condensed-matter/superconductivity/bcs-theory-and-conventional-superconductors", "name": "Ginzburg-Landau theory is the abelian Higgs model", "kind": "identity", "summary": "The Ginzburg-Landau free energy of a superconductor is, term by term, the static abelian Higgs Lagrangian; the coherence length and penetration depth are the inverse Higgs and photon masses, and kappa=lambda/xi separates type I from type II exactly where Nielsen-Olesen strings attract or repel.", "map": "F=\\int\\left[\\frac{|(\\nabla-2ie\\mathbf A/\\hbar)\\psi|^2}{2m^*}+a|\\psi|^2+\\tfrac b2|\\psi|^4+\\frac{B^2}{2\\mu_0}\\right];\\ \\xi^{-1}\\leftrightarrow m_H,\\ \\lambda^{-1}\\leftrightarrow m_\\gamma", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0356", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "08-condensed-matter/soft-matter/polymers", "name": "Scaling arguments in polymer physics", "kind": "method transfer", "summary": "Flory's free-energy balance and de Gennes' blob scaling derive polymer size, osmotic pressure and dynamics from dimensional analysis plus a single exponent, a showcase of scaling reasoning without solving the full model.", "map": "F\\sim\\frac{R^2}{Nb^2}+\\frac{vN^2}{R^d}\\Rightarrow R\\sim N^{3/(d+2)};\\ \\Pi\\sim\\frac{k_BT}{\\xi^3},\\ \\xi\\sim b(cb^3)^{-\\nu/(3\\nu-1)}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0357", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "08-condensed-matter/strongly-correlated-electrons/quantum-criticality-and-strange-metals", "name": "Planckian time from dimensional analysis", "kind": "method transfer", "summary": "At a quantum critical point the only energy scale is temperature, so dimensional analysis gives a relaxation time hbar/k_BT; strange metals saturate this Planckian bound, with measured scattering rates hbar/tau~alpha k_BT and alpha~1.", "map": "\\tau_P=\\frac{\\hbar}{k_BT}\\approx2.5\\times10^{-14}\\,\\text{s}\\ (300\\,\\text{K}),\\ \\rho=\\frac{m^*}{ne^2}\\frac{\\alpha k_BT}{\\hbar}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0358", "a": "00-foundations/units-and-constants/fundamental-constants", "b": "08-condensed-matter/topological-matter/quantum-hall-effects", "name": "Quantum Hall effect measures the fine-structure constant", "kind": "identity", "summary": "von Klitzing introduced the quantized Hall resistance as a determination of alpha, since R_K=h/e^2=mu_0 c/(2 alpha); QHE data entered CODATA adjustments of alpha before the 2019 SI made R_K exact.", "map": "R_K=\\frac{h}{e^2}=\\frac{\\mu_0c}{2\\alpha}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0359", "a": "00-foundations/units-and-constants/si-units-and-2019-redefinition", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "name": "Graphene quantum Hall resistance standards", "kind": "method transfer", "summary": "Epitaxial graphene on SiC shows wide, robust nu=2 plateaus at higher temperature and lower field than GaAs, allowing table-top quantum resistance standards with part-per-billion accuracy.", "map": "E_1-E_0=v_F\\sqrt{2e\\hbar B}\\approx36\\,\\text{meV}\\sqrt{B[\\text{T}]}\\gg\\hbar\\omega_c^{\\text{GaAs}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0360", "a": "00-foundations/units-and-constants/si-units-and-2019-redefinition", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/quantum-dots-and-nanostructures", "name": "Single-electron pumps and the quantum ampere", "kind": "method transfer", "summary": "Coulomb-blockaded quantum dots and metallic islands clocked at frequency f transfer exactly one electron per cycle, realizing I=ef directly from the fixed elementary charge and closing the quantum metrology triangle with Josephson and quantum Hall standards.", "map": "I=nef;\\ V=\\frac{f_J}{K_J},\\ R=R_K\\Rightarrow\\ R_KK_Je=2\\ (\\text{triangle})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0361", "a": "00-foundations/units-and-constants/si-units-and-2019-redefinition", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "Josephson voltage standard and the 2019 SI", "kind": "identity", "summary": "The AC Josephson effect fixes voltage to frequency through K_J=2e/h exactly; with e and h fixed in the 2019 SI, Josephson arrays realize the volt and, with the Kibble balance, the kilogram.", "map": "V_n=n\\frac{f}{K_J},\\ K_J=\\frac{2e}{h}=483\\,597.848\\ldots\\,\\text{GHz/V}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0362", "a": "00-foundations/units-and-constants/si-units-and-2019-redefinition", "b": "08-condensed-matter/topological-matter/quantum-hall-effects", "name": "Quantum Hall resistance standard", "kind": "identity", "summary": "Hall plateaus at R_xy=h/(nu e^2) independent of material and geometry realize the ohm via the von Klitzing constant R_K=h/e^2, exact in the 2019 SI.", "map": "R_K=\\frac{h}{e^2}=25\\,812.807\\ldots\\,\\Omega", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0363", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao", "name": "Simulation-based inference and emulators for LSS", "kind": "method transfer", "summary": "Neural emulators replace expensive N-body or Boltzmann runs, and neural density estimators enable likelihood-free inference from galaxy surveys and weak lensing.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0364", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/supernovae-and-transients", "name": "ML classification of transients", "kind": "method transfer", "summary": "Time-domain surveys such as ZTF and Rubin rely on neural classifiers and anomaly detection to triage millions of alerts and photometrically classify supernovae.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0365", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao", "name": "N-body simulations as gravitational MD", "kind": "method transfer", "summary": "Cosmological N-body codes use the same symplectic leapfrog integrators and force softening as MD, with tree or particle-mesh gravity in place of Lennard-Jones forces.", "map": "\\ddot{\\mathbf{x}}_i=-\\sum_{j\\ne i}\\frac{Gm_j(\\mathbf{x}_i-\\mathbf{x}_j)}{(|\\mathbf{x}_{ij}|^2+\\epsilon^2)^{3/2}}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0366", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "MCMC for CMB parameter estimation", "kind": "method transfer", "summary": "Metropolis-Hastings sampling, as in CosmoMC, explores the multidimensional CMB likelihood. It made six-parameter ΛCDM fits to Planck tractable.", "map": "\\alpha=\\min\\left(1,\\frac{P(\\theta')}{P(\\theta)}\\right)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0367", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "Boltzmann codes for CMB spectra", "kind": "method transfer", "summary": "CAMB and CLASS integrate coupled Einstein–Boltzmann hierarchies for photons, baryons, neutrinos and dark matter. Stiff ODE solvers handle tight coupling before recombination.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0368", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "09-astrophysics-and-cosmology/galaxies/galaxy-formation-and-evolution", "name": "Hydrodynamic solvers in cosmological simulations", "kind": "method transfer", "summary": "Finite-volume, AMR and SPH schemes evolve gas with gravity in galaxy-formation simulations. Subgrid models for cooling, star formation and feedback supply the physics that is not resolved.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0369", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics", "name": "Symplectic integrators for orbital dynamics", "kind": "historical", "summary": "Wisdom–Holman mapping splits the Hamiltonian into Kepler and perturbation parts. It enabled long-term chaos studies of planetary orbits and the Nice model.", "map": "H=H_{\\rm Kepler}+\\epsilon H_{\\rm int}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0370", "a": "00-foundations/history-and-philosophy-of-physics/philosophy-of-physics", "b": "09-astrophysics-and-cosmology/dark-matter/alternatives-mond-and-modified-gravity", "name": "Dark matter vs modified gravity as theory choice", "kind": "analogy", "summary": "The MOND versus particle dark matter debate mirrors Neptune versus Vulcan: anomalies can be absorbed by new matter or new laws. It engages Lakatosian research programmes and underdetermination.", "map": "", "breaks": "Unlike Vulcan, the dark-matter hypothesis has independent evidence from the CMB and the Bullet Cluster, and MOND struggles with clusters.", "confidence": "established", "strength": 2}
{"id": "C0371", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "Spherical harmonics and Legendre expansion of the CMB", "kind": "identity", "summary": "The temperature sky is expanded in spherical harmonics, and the angular power spectrum is the rotation-invariant variance. Statistical isotropy makes the C_ℓ the full description of Gaussian fluctuations.", "map": "\\frac{\\delta T}{T}=\\sum a_{\\ell m}Y_{\\ell m},\\ C_\\ell=\\langle|a_{\\ell m}|^2\\rangle", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0372", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "09-astrophysics-and-cosmology/galaxies/the-milky-way", "name": "Special functions in galactic potentials", "kind": "method transfer", "summary": "Galactic potentials and Poisson solutions in disk geometry use Bessel functions, Legendre expansions and elliptic integrals. They underpin mass models fitted to Gaia kinematics.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C0373", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao", "name": "Poisson equation and the growth of perturbations", "kind": "mechanism", "summary": "Linear perturbations obey a damped-oscillator-like ODE sourced by the Poisson equation. Green's-function solutions yield growth factors and the transfer function that shapes the matter power spectrum.", "map": "\\ddot\\delta+2H\\dot\\delta=4\\pi G\\bar\\rho\\,\\delta", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0374", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "name": "Stellar structure as a nonlinear boundary-value problem", "kind": "mechanism", "summary": "Hydrostatic equilibrium, mass continuity, energy generation and transport form coupled ODEs with boundary conditions at centre and surface. The Lane–Emden equation is the polytropic special case.", "map": "\\frac{1}{\\xi^2}\\frac{d}{d\\xi}\\left(\\xi^2\\frac{d\\theta}{d\\xi}\\right)=-\\theta^n", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0375", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history", "name": "FLRW as a maximally symmetric spacetime", "kind": "identity", "summary": "The FLRW metric is the warped product of time with a maximally symmetric 3-space of constant curvature k. Friedmann equations follow from the Einstein tensor evaluated on it.", "map": "ds^2=-dt^2+a^2\\left[\\frac{dr^2}{1-kr^2}+r^2d\\Omega^2\\right]", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0376", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "09-astrophysics-and-cosmology/cosmology/gravitational-lensing", "name": "Lensing as geodesic deflection in curved spacetime", "kind": "identity", "summary": "Null geodesics in a weak-field metric give the deflection angle, and the lens equation maps it to image positions. Shear and convergence are components of the Jacobian of the lens map.", "map": "\\hat\\alpha=\\frac{4GM}{c^2 b},\\quad A_{ij}=\\delta_{ij}-\\partial_i\\partial_j\\psi", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0377", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "TES bolometers and CMB polarimetry", "kind": "method transfer", "summary": "CMB experiments such as ACT, SPT and BICEP use transition-edge-sensor arrays limited by photon and thermal noise, with SQUID multiplexed readout.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0378", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Cryogenic sensors and low-background detectors", "kind": "method transfer", "summary": "Transition-edge sensors, bolometers and low-noise readout, developed for general detector physics, enable sub-GeV dark-matter searches. Noise floors and background rejection set the reach.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0379", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "09-astrophysics-and-cosmology/cosmology", "name": "Cosmology as statistical inference", "kind": "method transfer", "summary": "Cosmology has a single observable universe, so cosmic variance, MCMC chains, Fisher forecasts and Bayesian evidence are the core tools for extracting parameters and testing models.", "map": "F_{ij}=-\\langle\\partial_i\\partial_j\\ln L\\rangle", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0380", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history", "name": "Bayesian inference of ΛCDM parameters", "kind": "method transfer", "summary": "Cosmological parameters are fitted by Bayesian posterior sampling over likelihoods built from CMB, BAO and supernova data, with priors and model comparison deciding between ΛCDM extensions.", "map": "P(\\theta|d)\\propto L(d|\\theta)\\,\\pi(\\theta)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0381", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history", "name": "Priors, degeneracies and model selection in ΛCDM", "kind": "method transfer", "summary": "Parameter degeneracies (e.g. Ωm–H0, w0–wa) and prior choices shape cosmological constraints. Information criteria and Bayes factors adjudicate extensions such as curvature or dynamical dark energy.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0382", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "09-astrophysics-and-cosmology/dark-matter/direct-detection", "name": "Profile likelihood and exclusion limits", "kind": "method transfer", "summary": "Direct-detection limits use profile-likelihood tests, CLs and the Feldman–Cousins construction. Background-dominated searches face the look-elsewhere effect and the neutrino fog.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0383", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-detection", "name": "Detection statistics for exoplanet signals", "kind": "method transfer", "summary": "Planet detection uses periodograms, false-alarm probabilities, MCMC orbit fits and Bayesian model comparison for the number of planets. Noise from stellar activity requires Gaussian-process modelling.", "map": "\\ln B_{10}=\\ln\\frac{Z_1}{Z_0}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0384", "a": "00-foundations/measurement-and-data-analysis/uncertainty-and-error-propagation", "b": "09-astrophysics-and-cosmology/cosmology/hubble-tension-and-cosmological-tensions", "name": "Systematics budgets in the H0 tension", "kind": "shared object", "summary": "The H0 tension's significance depends on how statistical and systematic errors, covariances and calibration chains (Cepheids, TRGB) are propagated. Distance-ladder error budgets are an applied GUM-style case.", "map": "\\sigma_{H_0}^2=\\sum_{ij}\\frac{\\partial H_0}{\\partial x_i}\\frac{\\partial H_0}{\\partial x_j}C_{ij}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0385", "a": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "b": "09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history", "name": "CP violation and the baryon asymmetry", "kind": "mechanism", "summary": "Sakharov's conditions require C and CP violation, baryon-number violation and departure from equilibrium to generate the matter–antimatter asymmetry. The Standard Model's CP violation is far too small.", "map": "\\eta=\\frac{n_B}{n_\\gamma}\\approx6\\times10^{-10}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0386", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "09-astrophysics-and-cosmology/dark-matter/indirect-detection", "name": "Particle-physics symmetries behind annihilation signals", "kind": "shared object", "summary": "Annihilation channels and spectra depend on the gauge representation and quantum numbers of the dark-matter candidate, as for a WIMP in SU(2)_L multiplets. These fix branching fractions to gamma rays and antimatter.", "map": "", "breaks": "", "confidence": "current research", "strength": 1}
{"id": "C0387", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history", "name": "Broken time translation and energy in an expanding universe", "kind": "mechanism", "summary": "FLRW has no timelike Killing vector, so total energy is not conserved. Radiation redshifts as a⁻⁴ and the cosmological constant does work, though local ∇_μT^{μν}=0 persists.", "map": "\\dot\\rho+3H(\\rho+p)=0", "breaks": "Only the global energy notion fails; local covariant conservation holds.", "confidence": "established", "strength": 2}
{"id": "C0388", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "name": "Solar oscillations as normal modes", "kind": "analogy", "summary": "Helioseismic p-modes are standing waves of the solar cavity, described by spherical-harmonic eigenfunctions. Frequencies invert to give the sound-speed profile, as in a spectral problem for an oscillator.", "map": "", "breaks": "The Sun is a non-ideal, rotating, convective cavity, so modes are damped and stochastically excited, and rotation splits the degenerate m levels.", "confidence": "established", "strength": 1}
{"id": "C0389", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Inflaton as an order parameter", "kind": "analogy", "summary": "A scalar field rolling in a potential mirrors the order parameter of a symmetry-breaking transition. The same potential structure underlies Higgs-like phase transitions, topological defects and old/new inflation.", "map": "V(\\phi)=\\tfrac{\\lambda}{4}(\\phi^2-v^2)^2", "breaks": "Inflation requires slow roll on a flat plateau, which is not generic for SSB potentials, and the inflaton has no established particle identity.", "confidence": "current research", "strength": 2}
{"id": "C0390", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "name": "Homology and mass–luminosity scaling", "kind": "method transfer", "summary": "Dimensional and homology arguments give stellar scalings such as L∝M³ for radiative stars and the Eddington luminosity, together with the Chandrasekhar mass from fundamental constants.", "map": "M_{\\rm Ch}\\sim\\left(\\frac{\\hbar c}{G}\\right)^{3/2}\\frac{1}{m_p^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0391", "a": "00-foundations/units-and-constants/fundamental-constants", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "Constraints on varying constants from the CMB", "kind": "shared object", "summary": "A different fine-structure constant or electron mass at recombination shifts the recombination epoch and alters peak positions. Planck data and quasar absorption spectra bound such variation.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0392", "a": "00-foundations/units-and-constants/natural-units-and-planck-scale", "b": "09-astrophysics-and-cosmology/cosmology/dark-energy", "name": "Cosmological constant problem across Planck scales", "kind": "shared object", "summary": "Planck-unit estimates of the vacuum energy exceed the observed dark-energy density by about 120 orders of magnitude. The mismatch is the sharpest naturalness problem.", "map": "\\rho_\\Lambda\\sim10^{-123}\\,\\rho_{\\rm Pl}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0393", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "10-plasma-physics/magnetic-confinement-fusion/stellarators", "name": "Stellarator optimization with differentiable and ML tools", "kind": "method transfer", "summary": "Stellarator coil and shape optimization uses adjoint or automatic differentiation and surrogate models over a large 3D parameter space.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0394", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "10-plasma-physics/magnetic-confinement-fusion/tokamaks", "name": "Disruption prediction and plasma control with ML", "kind": "method transfer", "summary": "Tokamak disruption predictors and deep-RL magnetic controllers (e.g. on TCV) apply ML to real-time control where first-principles models are too slow.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0395", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "10-plasma-physics/magnetic-confinement-fusion/turbulent-transport-and-gyrokinetics", "name": "ML surrogates and control in fusion", "kind": "method transfer", "summary": "Neural surrogates of gyrokinetic fluxes accelerate transport modelling, and reinforcement learning has been used for tokamak shape control and disruption prediction.", "map": "Q\\approx \\mathcal N_\\theta(\\nabla T,\\nabla n,\\hat s,q)", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0396", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "name": "Ab initio MD for warm dense matter", "kind": "method transfer", "summary": "Warm dense matter equations of state and conductivities are computed by finite-temperature DFT-MD and path-integral Monte Carlo, bridging condensed matter methods to plasma conditions.", "map": "F[n,T]=\\min\\ \\text{free-energy functional}", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0397", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas", "name": "Strongly coupled plasmas studied by MD", "kind": "shared object", "summary": "The one-component plasma and Yukawa systems are benchmark MD systems, with melting at Γ≈175 (OCP) and dusty-plasma crystals; MD gives transport and equation of state where perturbation theory fails.", "map": "\\Gamma=\\frac{Z^2e^2}{4\\pi\\epsilon_0 a k_BT}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0398", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Particle pushers and MD integrators", "kind": "shared object", "summary": "PIC particle pushing and MD both integrate N-body trajectories with time-reversible Verlet-like schemes; MD with Coulomb forces uses Ewald or PPPM mesh methods also used in PIC.", "map": "\\ddot{\\mathbf r}_i=\\mathbf F_i/m_i", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0399", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "name": "Path-integral Monte Carlo for dense plasmas", "kind": "method transfer", "summary": "Fermionic PIMC and the sign problem constrain what can be computed for hydrogen and electron gases at WDM conditions; restricted and permutation-blocking variants give benchmark equations of state.", "map": "Z=\\mathrm{Tr}\\,e^{-\\beta H}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0400", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "10-plasma-physics/magnetic-confinement-fusion/burning-plasmas-and-iter", "name": "Monte Carlo neutronics and alpha-particle transport", "kind": "method transfer", "summary": "Neutron transport, tritium breeding and shielding in fusion devices use Monte Carlo codes, and Monte Carlo Fokker–Planck operators model fast-alpha slowing down.", "map": "\\partial_t f=C[f]", "breaks": "", "confidence": "established", "strength": 2}