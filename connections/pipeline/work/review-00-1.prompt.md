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

### Physics education research · `knowledge/00-foundations/history-and-philosophy-of-physics/physics-education-research`

**Scope.** Common preconceptions (impetus, "force implies motion", current consumed in circuits), concept inventories (FCI, BEMA), normalized gain, interactive engagement and peer instruction, expert vs. novice problem solving, representations (diagrams, graphs), lab instruction, equity in physics learning.

**Core ideas.**
- Students arrive with coherent but incorrect intuitive models; instruction must confront them explicitly.
- Interactive-engagement courses roughly double normalized gain compared with traditional lectures.
- Experts organize knowledge by principles (conservation laws), novices by surface features (inclined planes).

**Key equations.**
$$\langle g\rangle=\frac{\%\text{post}-\%\text{pre}}{100-\%\text{pre}}\quad(\text{Hake's normalized gain})$$

**See also.** How the agent tutors: `.claude/skills/explain-concept/SKILL.md` applies these findings.

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

# Packet 00-1 (100 records)

{"id": "C0001", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "name": "PINNs and neural operators learn PDE solution maps", "kind": "method transfer", "summary": "Physics-informed networks put the residual of the differential equation and its boundary conditions into the loss. Neural operators (DeepONet, Fourier neural operator) learn the whole solution map f↦u, a nonlinear generalization of the Green's-function integral operator, written as a kernel integral or a spectral multiplier.", "map": "u(x)=\\int G(x,x')f(x')dx'\\to u=\\mathcal G_\\theta[f];\\ \\mathcal L\\supset\\lambda\\|\\mathcal N u_\\theta\\|^2", "breaks": "Unlike a Green's function, the learned operator carries no guarantee of causality, conservation or accuracy outside its training distribution.", "confidence": "current research", "strength": 2}
{"id": "C0002", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "name": "Learned likelihood ratios and simulation-based inference", "kind": "method transfer", "summary": "A classifier trained to separate samples from two hypotheses learns their likelihood ratio, the Neyman–Pearson optimal test statistic. Neural density estimators learn posteriors straight from simulators, so frequentist and Bayesian inference work even when the likelihood is intractable, as in collider, cosmology and gravitational-wave analyses.", "map": "s^*(x)=\\frac{p_1(x)}{p_0(x)+p_1(x)}\\Rightarrow\\frac{p_1}{p_0}=\\frac{s^*}{1-s^*}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0003", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "name": "Equivariant networks built from group representations", "kind": "method transfer", "summary": "Group-equivariant networks build symmetry into the architecture. Convolutions are generalized to E(3)/SE(3) or lattice gauge groups, and features transform in irreducible representations coupled by Clebsch–Gordan products. They are used in molecular force fields and in gauge-equivariant flows for lattice QCD, where they need far less data and keep the symmetry exact.", "map": "f(\\rho_{\\rm in}(g)x)=\\rho_{\\rm out}(g)f(x)\\ \\forall g;\\ V_{l_1}\\otimes V_{l_2}=\\bigoplus_{l=|l_1-l_2|}^{l_1+l_2}V_l", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0004", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "name": "Buckingham π as a prior for symbolic regression", "kind": "method transfer", "summary": "Symbolic-regression systems that rediscover physical laws (e.g. AI Feynman) apply the π theorem first, cutting the number of independent variables before searching formula space. Surrogates fed dimensionless groups generalize across scales, the same way similarity lets wind-tunnel results transfer.", "map": "f(q_1,\\dots,q_n)=0\\to F(\\Pi_1,\\dots,\\Pi_{n-k})=0", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0005", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "name": "Which conservation laws an MD run actually keeps", "kind": "mechanism", "summary": "Pair forces obey Newton's third law, so velocity Verlet conserves total momentum to round-off. Periodic boundaries break rotational invariance, so angular momentum is not conserved. Nosé–Hoover thermostats break energy conservation on purpose but conserve an extended Hamiltonian, and drift in any of these quantities flags a bug or too large a time step.", "map": "\\sum_i\\mathbf F_i=0\\Rightarrow\\mathbf P=\\text{const};\\ H_{\\rm NH}=H+\\tfrac{Q}{2}\\zeta^2+gk_BT\\int_0^t\\zeta\\,dt'", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0006", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "00-foundations/history-and-philosophy-of-physics/history-of-physics", "name": "Monte Carlo as a product of Los Alamos big science", "kind": "historical", "summary": "Ulam, von Neumann and Metropolis developed statistical sampling for neutron-transport problems at Los Alamos, and the 1953 Metropolis algorithm ran on the MANIAC computer. Simulation, a third way between theory and experiment, grew directly out of wartime big science and the first electronic computers.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0007", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "name": "Sign problem: deforming path integrals into ℂ", "kind": "method transfer", "summary": "With complex weights (finite-density QCD, real-time path integrals, frustrated fermions), importance sampling breaks down. Picard–Lefschetz theory moves the integration contour onto steepest-descent thimbles where the phase is constant, and complex Langevin complexifies the fields. Both carry saddle-point methods from complex analysis into Monte Carlo.", "map": "Z=\\int dx\\,e^{-S(x)}=\\sum_\\sigma n_\\sigma\\int_{\\mathcal J_\\sigma}dz\\,e^{-S(z)},\\ \\mathrm{Im}\\,S|_{\\mathcal J_\\sigma}=\\text{const}", "breaks": "Thimbles still interfere with each other, and complex Langevin can converge to wrong answers. The general sign problem is NP-hard, so these are only partial cures.", "confidence": "current research", "strength": 2}
{"id": "C0008", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "name": "Feynman–Kac: random walks solve diffusion-type PDEs", "kind": "identity", "summary": "The Feynman–Kac formula writes the solution of the imaginary-time Schrödinger or diffusion equation, a Green's-function propagator, as an average over Brownian paths. Diffusion and Green's-function quantum Monte Carlo use it to project out ground states, and walk-on-spheres solves Laplace and Poisson problems.", "map": "\\partial_\\tau\\psi=\\tfrac12\\nabla^2\\psi-V\\psi\\Rightarrow\\psi(x,\\tau)=\\mathbb E_x\\!\\left[e^{-\\int_0^\\tau V(B_s)ds}\\psi_0(B_\\tau)\\right]", "breaks": "For fermions the walkers' weights change sign, so the method needs a fixed-node approximation.", "confidence": "established", "strength": 3}
{"id": "C0009", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "name": "MCMC: Boltzmann samplers became posterior samplers", "kind": "method transfer", "summary": "Set $E(\\theta)=-\\ln[L(D|\\theta)\\pi(\\theta)]$ and $\\beta=1$, and the Metropolis chain, built for Boltzmann weights, samples the Bayesian posterior. This drives cosmological and global particle-physics fits. Hybrid Monte Carlo, invented for lattice QCD, became the default sampler in Bayesian software (Stan's NUTS is a variant).", "map": "e^{-\\beta E}\\to p(\\theta|D)\\propto L(D|\\theta)\\pi(\\theta);\\ P_{\\rm acc}=\\min\\left(1,\\frac{p(\\theta'|D)}{p(\\theta|D)}\\right)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0010", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "00-foundations/measurement-and-data-analysis/uncertainty-and-error-propagation", "name": "Monte Carlo propagation of distributions (GUM-S1)", "kind": "method transfer", "summary": "When the measurement model is strongly nonlinear or the inputs are non-Gaussian, the first-order law of propagation fails. GUM Supplement 1 replaces it with Monte Carlo: sample the input distributions, push each sample through the model and read the coverage interval off the output distribution.", "map": "u_c^2(y)=\\mathbf c^TV_x\\mathbf c\\ \\to\\ y^{(k)}=f(x^{(k)}),\\ x^{(k)}\\sim p(x)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0011", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "name": "Analytic PDE structure underpins numerical schemes", "kind": "method transfer", "summary": "The same boundary- and initial-value problems are solved analytically (separation of variables, Sturm–Liouville eigenbases, Green's functions) and numerically. Spectral methods expand in those eigenfunctions, finite elements are Galerkin projections of the weak form, and well-posedness reappears as numerical stability.", "map": "\\text{consistency}+\\text{stability}\\iff\\text{convergence (Lax)};\\ u=\\int G f\\,dx'\\leftrightarrow u=A_h^{-1}f_h", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0012", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "name": "Discrete Noether theorem for variational integrators", "kind": "mechanism", "summary": "Integrators derived from a discrete action inherit its symmetries: a discrete Noether theorem makes them conserve the corresponding momenta exactly. Because they are symplectic, they also conserve a modified Hamiltonian over exponentially long times, so energy errors stay bounded instead of drifting.", "map": "\\tilde H=H+\\Delta t^pH_{p+1}+\\dots;\\ |H(t)-H(0)|=O(\\Delta t^p)\\ \\text{for}\\ t\\lesssim e^{c/\\Delta t}", "breaks": "Energy itself is not exactly conserved, because a fixed step breaks continuous time-translation symmetry. Adaptive step sizes destroy the symplectic guarantee.", "confidence": "established", "strength": 3}
{"id": "C0013", "a": "00-foundations/computational-physics/tensor-network-methods", "b": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "name": "MPS as iterated SVD; bond dimension bounds entanglement", "kind": "identity", "summary": "A matrix product state is built from repeated Schmidt (singular-value) decompositions of the state vector. Keeping the χ largest singular values is the optimal low-rank approximation (Eckart–Young), χ caps the bipartite entanglement, and DMRG is a Lanczos-type variational eigenproblem on this manifold.", "map": "|\\psi\\rangle=\\sum_{k=1}^{\\chi}s_k|L_k\\rangle|R_k\\rangle,\\ S=-\\sum_k s_k^2\\ln s_k^2\\le\\ln\\chi", "breaks": "Efficient only for area-law states. Volume-law states, such as those after long quenches, need χ exponential in system size.", "confidence": "established", "strength": 3}
{"id": "C0014", "a": "00-foundations/history-and-philosophy-of-physics", "b": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "name": "Broken symmetry as the paradigm of emergence", "kind": "shared object", "summary": "Anderson's 'More is different' uses spontaneous symmetry breaking as its central example of emergence: a ground state can lack the symmetry of the laws, and rigidity, order parameters and Goldstone modes follow. Philosophers debate whether this is genuine emergence, because strict SSB needs the infinite-volume limit.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0015", "a": "00-foundations/history-and-philosophy-of-physics/history-of-physics", "b": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "name": "SSB migrated from superconductivity to particle physics", "kind": "historical", "summary": "Nambu (1960–61) took the BCS ground state and the puzzle of its gauge invariance as the template for spontaneously broken symmetry in particle physics, and Goldstone generalized the massless mode. Anderson (1963) and Englert–Brout, Higgs and Guralnik–Hagen–Kibble (1964) then showed how gauge fields evade it, a textbook case of an idea crossing from condensed matter.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0016", "a": "00-foundations/history-and-philosophy-of-physics/philosophy-of-physics", "b": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "name": "Gleason and Kochen–Specker: Born rule and contextuality", "kind": "identity", "summary": "Two interpretive questions are settled as theorems about Hilbert space. Gleason: for dim ≥ 3, every additive probability measure on projectors has the form Tr(ρP), so the Born rule follows from the lattice of subspaces. Kochen–Specker: no noncontextual assignment of definite values to all projectors exists, which constrains hidden-variable interpretations.", "map": "\\mu(P)=\\mathrm{Tr}(\\rho P)\\ \\ (\\dim\\mathcal H\\ge3)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0017", "a": "00-foundations/history-and-philosophy-of-physics/philosophy-of-physics", "b": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "name": "Hole argument: diffeomorphisms and gauge redundancy", "kind": "shared object", "summary": "General covariance makes a metric and its pullback by a diffeomorphism physically equivalent. Einstein's hole argument turns this into the substantivalism–relationism debate, settled in practice by treating only diffeomorphism-invariant quantities as observable. The fibre-bundle view of gauge fields gets the same reading: only holonomies and curvature are physical ('gauge as redundancy').", "map": "(M,g)\\sim(M,\\phi^*g)\\ \\forall\\phi\\in\\mathrm{Diff}(M)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0018", "a": "00-foundations/history-and-philosophy-of-physics/philosophy-of-physics", "b": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "name": "Arrow of time vs. microscopic T violation", "kind": "shared object", "summary": "The fundamental laws are T-invariant except for the weak interaction, where CP violation together with CPT implies T violation. Philosophers of physics stress that this small, Hamiltonian-level asymmetry does not explain the thermodynamic arrow, which instead traces to a low-entropy initial state (the past hypothesis).", "map": "\\text{CPT exact},\\ \\epsilon_K\\neq0\\Rightarrow T\\ \\text{violated}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0019", "a": "00-foundations/history-and-philosophy-of-physics/philosophy-of-physics", "b": "00-foundations/units-and-constants/natural-units-and-planck-scale", "name": "Are c, ħ, G fundamental or just unit conversions?", "kind": "shared object", "summary": "Natural units set c, ħ, G and k_B to 1, which shows that dimensionful constants act largely as unit conversions. Only dimensionless combinations such as α or m_p/m_e are unit-independent and can be meaningfully tested for variation. How many dimensionful constants are fundamental (three, two or none) is still debated, notably in the Duff–Okun–Veneziano 'trialogue'.", "map": "\\alpha=\\frac{e^2}{4\\pi\\varepsilon_0\\hbar c}\\ \\text{(unit-free)};\\ \\ell_P=\\sqrt{\\hbar G/c^3}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0020", "a": "00-foundations/history-and-philosophy-of-physics/physics-education-research", "b": "00-foundations/measurement-and-data-analysis/uncertainty-and-error-propagation", "name": "Point vs. set paradigms of measurement in learning", "kind": "shared object", "summary": "PER finds that many students treat a single reading as 'the true value' (point paradigm) instead of seeing a measurement as a distribution summarized by a best estimate and an uncertainty (set paradigm). Lab curricula built on the GUM framework target this shift, so uncertainty is both a metrology topic and a documented learning difficulty.", "map": "\\bar x\\pm s/\\sqrt N", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C0021", "a": "00-foundations/mathematical-methods", "b": "00-foundations/symmetry-and-group-theory", "name": "Symmetry acts through linear representations", "kind": "identity", "summary": "Symmetry groups act on state spaces through linear, usually unitary or projective, representations. Group theory in physics therefore runs on the mathematical-methods toolkit: Hilbert-space operators and eigenproblems, special functions as representation bases, and differential geometry for Lie groups and gauge connections.", "map": "U(g_1)U(g_2)=e^{i\\phi(g_1,g_2)}U(g_1g_2),\\ [H,U(g)]=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0022", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "name": "Causal transfer functions: Kramers–Kronig, Bode, Nyquist", "kind": "identity", "summary": "A causal, stable signal chain has a transfer function analytic in a half-plane, so its gain and phase are tied together (Kramers–Kronig, Bode). The Nyquist criterion, the argument principle applied to the loop gain, decides whether a feedback amplifier or phase-locked loop oscillates. Bode's relations limit how much feedback a front end can have over a given bandwidth.", "map": "\\mathrm{Re}\\,\\chi(\\omega)=\\frac1\\pi\\mathcal P\\!\\int\\frac{\\mathrm{Im}\\,\\chi(\\omega')}{\\omega'-\\omega}d\\omega';\\ Z=N_{\\rm cw}+P", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0023", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "name": "Special functions as representation matrix elements", "kind": "identity", "summary": "The classical special functions are matrix elements or bases of Lie-group representations: spherical harmonics and Legendre polynomials for SO(3), Wigner D-functions for SU(2), Bessel functions for the Euclidean group E(2), Hermite functions for the Heisenberg–Weyl group. Their addition theorems, recursions and orthogonality follow from group multiplication, ladder operators and Peter–Weyl.", "map": "D^{l}_{m0}(\\alpha,\\beta,\\gamma)=\\sqrt{\\tfrac{4\\pi}{2l+1}}\\,Y_l^{m*}(\\beta,\\alpha)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0024", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "name": "Lie groups were invented to integrate ODEs", "kind": "historical", "summary": "Sophus Lie built the theory of continuous groups in the 1870s to do for differential equations what Galois theory did for polynomials. Each one-parameter point symmetry lowers an ODE's order by one, and symmetry reductions of PDEs give similarity solutions and separable coordinates. The algebraic core of that programme became the Lie theory physics uses today.", "map": "X=\\xi\\partial_x+\\eta\\partial_y,\\ \\mathrm{pr}^{(n)}X\\,\\Delta\\big|_{\\Delta=0}=0\\Rightarrow\\text{order }n\\to n-1", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0025", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "name": "Self-similar solutions: scaling turns PDEs into ODEs", "kind": "mechanism", "summary": "When a problem has no intrinsic scale, dimensional analysis forces a similarity form that reduces the PDE to an ODE: the heat kernel, the Blasius boundary layer, the Taylor–Sedov blast wave. In second-kind (intermediate) asymptotics the exponents are not fixed by dimensions and come out as eigenvalues of the reduced problem.", "map": "u=\\frac{Q}{\\sqrt{Dt}}F\\!\\left(\\frac{x}{\\sqrt{Dt}}\\right);\\ R(t)\\approx(Et^2/\\rho)^{1/5}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0026", "a": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "b": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "name": "Wigner's theorem: time reversal is antiunitary", "kind": "identity", "summary": "By Wigner's theorem every quantum symmetry is unitary or antiunitary, and time reversal must be antiunitary, T=UK. For half-integer spin T²=−1, so ψ and Tψ are orthogonal with equal energy, and every level of a T-invariant Hamiltonian is at least doubly degenerate (Kramers). The same antiunitary structure fixes the random-matrix and topological symmetry classes.", "map": "T=UK,\\ T^2=-1\\Rightarrow\\langle\\psi|T\\psi\\rangle=0\\Rightarrow\\text{Kramers doublets}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0027", "a": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "b": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "name": "Schur's lemma: symmetry dictates degeneracy", "kind": "identity", "summary": "By Schur's lemma, an operator that commutes with an irreducible representation is a multiple of the identity on it. Symmetry-protected degeneracies therefore equal irrep dimensions (2l+1 for SO(3)) and eigenbases are labelled by Casimirs. The Wigner–Eckart theorem reduces tensor-operator matrix elements to Clebsch–Gordan coefficients, which gives the selection rules.", "map": "[H,D(g)]=0\\ \\forall g\\Rightarrow H|_{V_\\lambda}=E_\\lambda\\mathbb 1;\\ \\langle j'm'|T^k_q|jm\\rangle\\propto\\langle jm;kq|j'm'\\rangle", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0028", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "name": "Gauge fields are Lie-algebra-valued connections", "kind": "identity", "summary": "A Lie group is a manifold whose tangent space at the identity is its Lie algebra. A gauge potential is a Lie-algebra-valued connection one-form on a principal G-bundle, and the field strength is its curvature. Yang–Mills theory and gravity therefore share connections, parallel transport and curvature (holonomy = Wilson loop).", "map": "F=dA+A\\wedge A,\\ F_{\\mu\\nu}=\\partial_\\mu A_\\nu-\\partial_\\nu A_\\mu+[A_\\mu,A_\\nu]\\leftrightarrow R^\\rho{}_{\\sigma\\mu\\nu}", "breaks": "Gravity's connection is soldered to the tangent bundle and fixed by the metric, and its action is not of Yang–Mills type.", "confidence": "established", "strength": 3}
{"id": "C0029", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "name": "Killing vectors turn ∇·T=0 into conserved charges", "kind": "mechanism", "summary": "In curved spacetime, ∇_μT^{μν}=0 gives no integral conservation law by itself. Only an isometry (a Killing vector ξ) makes J^μ=T^{μν}ξ_ν a conserved current with a global charge, which is Noether's theorem in geometric form. The contracted Bianchi identity is the identity Noether's second theorem attaches to diffeomorphism invariance, which resolved Hilbert and Klein's 1918 energy puzzle.", "map": "\\nabla_{(\\mu}\\xi_{\\nu)}=0,\\ \\nabla_\\mu T^{\\mu\\nu}=0\\Rightarrow\\nabla_\\mu(T^{\\mu\\nu}\\xi_\\nu)=0;\\ \\nabla_\\mu G^{\\mu\\nu}\\equiv0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0030", "a": "00-foundations/measurement-and-data-analysis", "b": "00-foundations/units-and-constants", "name": "Metrology: value × unit ± uncertainty, traceable to SI", "kind": "shared object", "summary": "A complete measurement result is a number times an SI unit plus an uncertainty. Traceability links any instrument through an unbroken calibration chain to the unit definitions, and since the 2019 redefinition that chain ends at exact constants rather than artefacts.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0031", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "00-foundations/symmetry-and-group-theory/discrete-symmetries-and-cpt", "name": "EDM and CPT tests as noise-limited precision measurements", "kind": "shared object", "summary": "Two kinds of experiment are limited by sensor noise: searches for permanent electric dipole moments (the neutron, the electron in polar molecules), which would violate P and T, and CPT tests comparing particles with antiparticles in Penning traps or by antihydrogen spectroscopy. Their reach on new CP violation is set by magnetometry, spin-precession readout and cryogenic trap techniques.", "map": "H=-(\\mu\\mathbf B+d\\mathbf E)\\cdot\\hat{\\mathbf S},\\ \\delta d\\sim\\frac{\\hbar}{2E\\tau\\sqrt N}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0032", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "00-foundations/units-and-constants/si-units-and-2019-redefinition", "name": "Josephson and QHE standards realize volt, ohm, kilogram", "kind": "shared object", "summary": "Quantum electrical devices turn the exact h and e into units: Josephson arrays give voltages nf/K_J and quantum Hall bars give resistances R_K/i. The Kibble balance balances mechanical against electrical power measured with both, which realizes the 2019 kilogram from h.", "map": "K_J=2e/h,\\ R_K=h/e^2;\\ mgv=UI\\Rightarrow m\\propto h", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0033", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "00-foundations/units-and-constants/fundamental-constants", "name": "CODATA adjustment as generalized least squares", "kind": "method transfer", "summary": "CODATA recommended values come from a linearized generalized least-squares fit of well over a hundred correlated experimental and theoretical inputs. Consistency is checked with the Birge ratio and normalized residuals, and discrepant inputs get expanded uncertainties. The roughly 5σ disagreement between the Cs and Rb atom-recoil values of α is the kind of tension this step has to absorb.", "map": "\\hat\\theta=(A^TV^{-1}A)^{-1}A^TV^{-1}q,\\ R_B=\\sqrt{\\chi^2/\\nu}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0034", "a": "00-foundations/measurement-and-data-analysis/uncertainty-and-error-propagation", "b": "00-foundations/units-and-constants", "name": "Unit realizations carry GUM uncertainty budgets", "kind": "shared object", "summary": "Each realization of an SI unit reports a GUM budget of Type A and Type B components: the Kibble balance or silicon-sphere XRCD for the kilogram, acoustic-gas or Johnson-noise thermometry for the kelvin. Traceability carries that uncertainty down the calibration chain into every measurement.", "map": "u_c^2(y)=\\sum_{i,j}c_ic_j\\,u(x_i,x_j),\\ c_i=\\partial f/\\partial x_i", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0035", "a": "00-foundations/measurement-and-data-analysis/uncertainty-and-error-propagation", "b": "00-foundations/units-and-constants/fundamental-constants", "name": "CODATA uncertainties, correlations and exact constants", "kind": "shared object", "summary": "CODATA values carry standard uncertainties plus a correlation matrix, because many constants derive from shared inputs. Since 2019 h, e, k and N_A are exact, so their former uncertainty now sits in μ0, ε0, the molar mass constant and the mass of the old prototype kilogram.", "map": "u_r(h)=0;\\ \\mu_0=\\frac{2\\alpha h}{e^2c}\\Rightarrow u_r(\\mu_0)=u_r(\\alpha)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0036", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "01-classical-mechanics/analytical-mechanics/variational-principles", "name": "Energy-based neural PDE solvers (Deep Ritz)", "kind": "method transfer", "summary": "Networks can minimize the variational energy of a mechanics problem instead of a residual, turning the principle of minimum potential energy into the training objective.", "map": "u_\\theta=\\arg\\min_\\theta\\int\\big[\\tfrac12\\epsilon(u_\\theta):\\mathsf C:\\epsilon(u_\\theta)-f\\cdot u_\\theta\\big]dV", "breaks": "", "confidence": "current research", "strength": 1}
{"id": "C0037", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "name": "Physics-informed networks for Navier–Stokes", "kind": "method transfer", "summary": "PINNs penalize the Navier–Stokes residual in the loss to reconstruct velocity and pressure from sparse data; flow problems are the main testbed for scientific-ML surrogates.", "map": "\\mathcal L=\\|u_\\theta-u\\|^2+\\lambda\\|\\partial_tu_\\theta+u_\\theta\\cdot\\nabla u_\\theta+\\nabla p_\\theta/\\rho-\\nu\\nabla^2u_\\theta\\|^2", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0038", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "name": "Molecular dynamics integrates Hamilton's equations", "kind": "method transfer", "summary": "MD is numerical Hamiltonian mechanics for N particles; Nosé's extended Hamiltonian adds a thermostat variable so that the deterministic flow samples the canonical ensemble.", "map": "H_{\\rm N}=\\sum\\frac{p_i^2}{2ms^2}+V(q)+\\frac{p_s^2}{2Q}+gk_BT\\ln s", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0039", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos", "name": "Lyapunov instability underlies MD ergodicity", "kind": "mechanism", "summary": "Many-particle MD trajectories are chaotic with positive Lyapunov exponents, so individual trajectories are irreproducible after picoseconds while time averages converge to ensemble averages; chaos is what makes MD statistics robust.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C0040", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "name": "Hamiltonian (hybrid) Monte Carlo", "kind": "method transfer", "summary": "HMC proposes moves by integrating fictitious Hamiltonian dynamics with leapfrog; time reversibility and Liouville volume preservation make the Metropolis correction exact.", "map": "H(x,p)=\\tfrac12p^2+S(x),\\quad P_{\\rm acc}=\\min(1,e^{-\\Delta H})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0041", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "name": "Symplectic integrators ↔ Hamiltonian flow", "kind": "method transfer", "summary": "Leapfrog/Verlet and other symplectic schemes are exact flows of a nearby 'shadow' Hamiltonian, so they preserve phase-space volume and show no secular energy drift; the integrator inherits the symplectic structure of Hamilton's equations.", "map": "\\tilde H=H+h^2H_2+\\dots,\\quad \\Phi_h^*\\omega=\\omega,\\ \\omega=dp\\wedge dq", "breaks": "Backward-error bound holds only for fixed step size; adaptive steps or dissipation destroy the shadow Hamiltonian.", "confidence": "established", "strength": 3}
{"id": "C0042", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "01-classical-mechanics/analytical-mechanics/variational-principles", "name": "Variational integrators and Ritz–Galerkin", "kind": "method transfer", "summary": "Discretizing the action rather than the equations gives variational integrators that are automatically symplectic and momentum-conserving (discrete Noether); finite elements are Ritz minimization of an energy functional.", "map": "S_d=\\sum_kL_d(q_k,q_{k+1}),\\quad D_2L_d(q_{k-1},q_k)+D_1L_d(q_k,q_{k+1})=0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0043", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "name": "Finite elements born in structural elasticity", "kind": "historical", "summary": "The finite element method grew out of structural and elasticity analysis (Courant's 1943 variational triangles, 1950s aircraft stress analysis) and is a Ritz–Galerkin minimization of the elastic energy.", "map": "K\\mathbf u=\\mathbf f,\\quad K_{ij}=\\int\\nabla\\phi_i:\\mathsf C:\\nabla\\phi_j\\,dV", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0044", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "name": "DNS and spectral solvers ↔ turbulence", "kind": "method transfer", "summary": "Direct numerical simulation must resolve from the integral scale L down to the Kolmogorov scale η, so grid points grow as Re^{9/4}; pseudospectral FFT methods and LES closures are the workhorses of turbulence research.", "map": "N\\sim(L/\\eta)^3\\sim Re^{9/4}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0045", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics", "name": "N-body integrators ↔ celestial mechanics", "kind": "method transfer", "summary": "Long-term Solar System integrations use symplectic map methods (Wisdom–Holman splitting into Kepler drift plus interaction kick) and regularization for close encounters.", "map": "H=H_{\\rm Kep}+H_{\\rm int},\\ \\ e^{hL_H}\\approx e^{\\frac h2L_{\\rm int}}e^{hL_{\\rm Kep}}e^{\\frac h2L_{\\rm int}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0046", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos", "name": "Lyapunov spectra and shadowing in numerics", "kind": "method transfer", "summary": "Lyapunov exponents are computed by tangent-map integration with repeated QR (Gram–Schmidt) reorthonormalization; the shadowing lemma justifies trusting chaotic numerical orbits statistically even though each diverges from the true one.", "map": "\\lambda_i=\\lim_{n\\to\\infty}\\frac1n\\sum_k\\ln|R^{(k)}_{ii}|", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0047", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos", "name": "Standard map = leapfrog kicked rotor", "kind": "identity", "summary": "Chirikov's standard map is the symplectic-Euler discretization of a pendulum and the exact flow of the kicked rotor; KAM theory explains why symplectic integrators keep invariant tori and stay stable for exponentially long times.", "map": "p_{n+1}=p_n+K\\sin\\theta_n,\\ \\theta_{n+1}=\\theta_n+p_{n+1}", "breaks": "Correspondence with the continuous pendulum holds only for small step K; for K≳1 the map's global chaos is a discretization artifact.", "confidence": "established", "strength": 3}
{"id": "C0048", "a": "00-foundations/history-and-philosophy-of-physics/history-of-physics", "b": "01-classical-mechanics/newtonian-mechanics/central-forces-and-orbits", "name": "Rutherford scattering discovered the nucleus", "kind": "historical", "summary": "Rutherford's classical Coulomb-orbit cross-section, fitted to Geiger–Marsden α data, revealed the atomic nucleus; the same formula happens to be exact in quantum mechanics.", "map": "\\frac{d\\sigma}{d\\Omega}=\\Big(\\frac{kq_1q_2}{4E}\\Big)^2\\frac{1}{\\sin^4(\\theta/2)}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0049", "a": "00-foundations/history-and-philosophy-of-physics/philosophy-of-physics", "b": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "name": "Liouville, recurrence and the arrow of time", "kind": "shared object", "summary": "Time-reversal-invariant Hamiltonian flow preserves phase-space volume, so fine-grained Gibbs entropy is constant and Poincaré recurrence holds; irreversibility needs coarse-graining plus a low-entropy past.", "map": "\\frac{d}{dt}\\int\\rho\\ln\\rho\\,d\\Gamma=0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0050", "a": "00-foundations/history-and-philosophy-of-physics/physics-education-research", "b": "01-classical-mechanics/newtonian-mechanics/kinematics-and-newtons-laws", "name": "Force Concept Inventory ↔ Newton's laws", "kind": "shared object", "summary": "Newton's three laws are the content probed by the Force Concept Inventory; PER shows students hold impetus-like preconceptions, and interactive engagement roughly doubles the normalized gain.", "map": "\\langle g\\rangle=\\frac{\\%post-\\%pre}{100-\\%pre}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0051", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "name": "Conformal maps for 2D potential flow and lift", "kind": "identity", "summary": "Planar irrotational incompressible flow is an analytic complex potential; Joukowski conformal maps generate airfoils and the Blasius contour integral gives the Kutta–Joukowski lift.", "map": "W(z)=\\phi+i\\psi,\\ \\ u-iv=W'(z),\\quad L=\\rho U\\Gamma", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0052", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos", "name": "Small divisors and analytic estimates in KAM", "kind": "method transfer", "summary": "Lindstedt perturbation series diverge because of small denominators k·ω; KAM proves torus survival for Diophantine frequencies by Newton iteration with Cauchy estimates on shrinking complex analyticity strips.", "map": "|\\mathbf k\\cdot\\boldsymbol\\omega|\\ge\\frac{\\gamma}{|\\mathbf k|^\\tau}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0053", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "name": "Inverse scattering via analytic scattering data", "kind": "method transfer", "summary": "The inverse scattering transform solves KdV and NLS by mapping initial data to scattering data analytic in the spectral parameter, reconstructed through a Riemann–Hilbert (Gelfand–Levitan) problem; solitons are bound-state poles.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C0054", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators", "name": "Damped oscillator response ↔ causality and Kramers–Kronig", "kind": "identity", "summary": "The driven damped oscillator's susceptibility has poles only in the lower half ω-plane because the response is causal, so its real and imaginary parts obey Kramers–Kronig; its impulse response is the retarded Green's function.", "map": "\\chi(\\omega)=\\frac{1}{\\omega_0^2-\\omega^2-i\\gamma\\omega},\\quad G(t)=\\theta(t)\\frac{e^{-\\gamma t/2}\\sin\\omega_dt}{\\omega_d}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0055", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "01-classical-mechanics/analytical-mechanics/canonical-transformations-and-hamilton-jacobi", "name": "Hamilton–Jacobi PDE ↔ method of characteristics", "kind": "identity", "summary": "The Hamilton–Jacobi equation is a first-order nonlinear PDE whose characteristics are exactly Hamilton's equations; complete integrals give generating functions of canonical transformations.", "map": "\\partial_tS+H(q,\\partial_qS)=0\\ \\leftrightarrow\\ \\dot q=\\partial_pH,\\ \\dot p=-\\partial_qH", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0056", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics", "name": "Stokeslet = Green's function of Stokes flow", "kind": "identity", "summary": "The Oseen tensor (Stokeslet) is the Green's function of the Stokes equations; boundary-integral, slender-body and hydrodynamic-interaction methods superpose it.", "map": "u_i=G_{ij}F_j,\\quad G_{ij}=\\frac{1}{8\\pi\\mu}\\Big(\\frac{\\delta_{ij}}{r}+\\frac{x_ix_j}{r^3}\\Big)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0057", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics", "name": "Acoustic waves ↔ retarded Green's function", "kind": "identity", "summary": "Sound radiated by sources is the source convolved with the retarded Green's function of the wave equation; Huygens' sharp-front principle holds in odd spatial dimensions.", "map": "\\Big(\\nabla^2-\\frac1{c^2}\\partial_t^2\\Big)G=-\\delta^4,\\quad G_{\\rm ret}=\\frac{\\delta(t-r/c)}{4\\pi r}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0058", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations", "name": "Floquet theory of the Mathieu equation", "kind": "identity", "summary": "Parametric resonance is governed by Floquet–Hill theory of linear ODEs with periodic coefficients; Mathieu characteristic exponents define the instability tongues near ω = 2ω₀/n.", "map": "\\ddot x+\\omega_0^2[1+h\\cos2\\omega_0t]x=0,\\ x(t+T)=e^{\\mu T}x(t)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0059", "a": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "b": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "name": "Poisson brackets ↔ commutators; Koopman–von Neumann", "kind": "identity", "summary": "Dirac's rule {f,g} → [f̂,ĝ]/iħ maps Hamiltonian mechanics onto Hilbert-space operators; conversely Koopman–von Neumann write classical mechanics as unitary evolution on L²(phase space).", "map": "\\{f,g\\}\\to\\frac{1}{i\\hbar}[\\hat f,\\hat g],\\quad i\\partial_t\\psi=\\hat L\\psi,\\ \\hat L=-i\\{\\cdot,H\\}", "breaks": "Groenewold–van Hove: no quantization map preserves all brackets beyond quadratic polynomials.", "confidence": "established", "strength": 2}
{"id": "C0060", "a": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "b": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "name": "Normal modes = generalized eigenproblem", "kind": "identity", "summary": "Small oscillations about equilibrium reduce to the symmetric generalized eigenproblem Kv = ω²Mv; normal modes are the orthogonal eigenvectors guaranteed by the spectral theorem.", "map": "K\\mathbf v_n=\\omega_n^2M\\mathbf v_n,\\quad \\mathbf v_m^TM\\mathbf v_n=\\delta_{mn}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0061", "a": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "b": "01-classical-mechanics/rigid-body-dynamics/rotational-dynamics-and-inertia-tensor", "name": "Principal axes = spectral theorem for the inertia tensor", "kind": "identity", "summary": "The inertia tensor is real symmetric, so it has orthogonal eigenvectors (principal axes) and real eigenvalues (principal moments); rotational kinetic energy is diagonal in that basis.", "map": "\\mathsf I\\mathbf e_k=I_k\\mathbf e_k,\\quad T=\\tfrac12\\sum_kI_k\\omega_k^2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0062", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "name": "Phase space as a symplectic manifold", "kind": "identity", "summary": "Phase space is the cotangent bundle T*Q with symplectic 2-form ω = dp∧dq; Hamilton's equations are ι_X ω = dH, Poisson brackets come from ω^{-1}, and Liouville's theorem is conservation of the volume form ω^n.", "map": "\\iota_{X_H}\\omega=dH,\\quad \\mathcal L_{X_H}\\omega=0,\\quad \\{f,g\\}=\\omega^{ij}\\partial_if\\partial_jg", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0063", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "name": "Strain compatibility = flat metric; defects = torsion and curvature", "kind": "identity", "summary": "Saint-Venant compatibility is the vanishing Riemann tensor of the deformed metric g = δ + 2ε; in the geometric theory of defects dislocations are torsion and disclinations curvature of a material connection.", "map": "g_{ij}=\\delta_{ij}+2\\epsilon_{ij},\\quad R_{ijkl}[g]=0\\Leftrightarrow\\text{compatible strain}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0064", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "01-classical-mechanics/newtonian-mechanics/non-inertial-frames", "name": "Fictitious forces as connection coefficients", "kind": "identity", "summary": "Coriolis and centrifugal forces are the Christoffel symbols of rotating coordinates in flat space; writing Newton's law covariantly prefigures the equivalence principle.", "map": "\\ddot x^i+\\Gamma^i_{jk}\\dot x^j\\dot x^k=F^i/m", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0065", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators", "name": "Resonant sensors: Q, bandwidth and thermal force noise", "kind": "shared object", "summary": "Mechanical and electrical resonators used as sensors are driven damped oscillators; Q sets the bandwidth f₀/Q and the lock-in readout, and via fluctuation–dissipation the thermal force-noise floor.", "map": "S_F=4k_BTm\\gamma,\\qquad \\Delta f=f_0/Q", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0066", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics", "name": "Least squares born from orbit determination", "kind": "historical", "summary": "Gauss developed least squares and the normal error law to recover the orbit of Ceres (1801–1809); χ² fitting of orbital elements remains the template for parameter estimation.", "map": "\\hat\\theta=\\arg\\min\\sum_i\\frac{(y_i-f(t_i;\\theta))^2}{\\sigma_i^2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0067", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "01-classical-mechanics/newtonian-mechanics/central-forces-and-orbits", "name": "Kepler's hidden SO(4) and the Runge–Lenz vector", "kind": "identity", "summary": "The conserved Laplace–Runge–Lenz vector together with L generates SO(4) for bound Kepler orbits, explaining closed ellipses (Bertrand) and, once quantized, the n² degeneracy of hydrogen (Pauli 1926).", "map": "\\mathbf A=\\mathbf p\\times\\mathbf L-mk\\hat{\\mathbf r},\\quad \\{A_i,A_j\\}=-2mH\\epsilon_{ijk}L_k", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0068", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "name": "KdV hierarchies ↔ infinite-dimensional Lie algebras", "kind": "identity", "summary": "Integrable soliton equations come in hierarchies attached to Kac–Moody algebras (Drinfeld–Sokolov); the Lax pair is a flat connection in a loop algebra and tau functions carry representations of infinite-dimensional groups.", "map": "\\dot L=[M,L],\\quad \\partial_tU-\\partial_xV+[U,V]=0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0069", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "01-classical-mechanics/rigid-body-dynamics", "name": "Rotation group SO(3) ↔ rigid-body motion", "kind": "identity", "summary": "A rigid body's configuration space is SO(3); Euler's equations are the Lie–Poisson equations on so(3)*, and the inertia tensor defines a left-invariant metric whose geodesics are torque-free motions.", "map": "\\dot{\\mathbf L}=\\mathbf L\\times\\boldsymbol\\omega,\\ \\ \\{L_i,L_j\\}=\\epsilon_{ijk}L_k", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0070", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "01-classical-mechanics/analytical-mechanics/variational-principles", "name": "Invariance of the action → Noether currents", "kind": "identity", "summary": "Noether's theorem is a statement about the variational principle: a continuous transformation leaving the action invariant up to a boundary term yields a conserved quantity; cyclic coordinates are the simplest case.", "map": "\\delta L=\\frac{dK}{dt}\\Rightarrow Q=\\frac{\\partial L}{\\partial\\dot q}\\delta q-K,\\ \\dot Q=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0071", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "name": "Kelvin circulation from particle-relabelling symmetry", "kind": "identity", "summary": "In the Lagrangian (Euler–Poincaré) formulation of ideal fluids, invariance under relabelling of fluid particles is a Noether symmetry whose charge is circulation; Kelvin's theorem and potential-vorticity conservation follow.", "map": "\\frac{d}{dt}\\oint_{C(t)}\\mathbf u\\cdot d\\mathbf l=0", "breaks": "Exact only for ideal barotropic fluids; viscosity and baroclinic torques break it.", "confidence": "established", "strength": 2}
{"id": "C0072", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "01-classical-mechanics/newtonian-mechanics", "name": "Newtonian mechanics as symmetry consequences", "kind": "identity", "summary": "The Galilean symmetry group of Newtonian mechanics (translations, rotations, boosts) fixes its conserved quantities; the Galilean boost charge gives uniform centre-of-mass motion.", "map": "\\mathbf K=M\\mathbf R_{cm}-t\\mathbf P,\\ \\ d\\mathbf K/dt=0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0073", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "01-classical-mechanics/newtonian-mechanics/conservation-laws", "name": "Noether's theorem ↔ energy, momentum, angular momentum", "kind": "identity", "summary": "The conservation laws of Newtonian mechanics are the Noether charges of time translation, space translation and rotation invariance of the action.", "map": "\\partial L/\\partial t=0\\Rightarrow E=\\dot q\\,\\partial L/\\partial\\dot q-L\\ \\text{conserved}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0074", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "name": "Integrability = enough conserved charges in involution", "kind": "identity", "summary": "Liouville–Arnold integrability needs n Poisson-commuting conserved quantities; KdV has infinitely many, generated by commuting symmetry flows, which is why solitons survive collisions.", "map": "\\{I_j,I_k\\}=0,\\quad I_n[u]=\\int P_n(u,u_x,\\dots)dx", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0075", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "name": "Elasticity as the Goldstone theory of broken translations", "kind": "mechanism", "summary": "A crystal breaks continuous translations; continuum elasticity is the effective theory of the corresponding Goldstone fields (displacements), and its sound waves are the Goldstone modes.", "map": "F=\\int\\big(\\tfrac\\lambda2\\epsilon_{kk}^2+\\mu\\epsilon_{ij}\\epsilon_{ij}\\big),\\quad \\omega=v_{L,T}k", "breaks": "Broken rotations give no independent Goldstone modes (inverse Higgs); amorphous solids are elastic without long-range order.", "confidence": "established", "strength": 2}
{"id": "C0076", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "01-classical-mechanics/nonlinear-dynamics-and-chaos/bifurcations-and-routes-to-chaos", "name": "Pitchfork bifurcation = Landau symmetry breaking", "kind": "identity", "summary": "The normal form of a Z2-symmetric pitchfork is gradient flow on a φ⁴ potential; the supercritical branch is mean-field spontaneous symmetry breaking with exponent 1/2.", "map": "\\dot x=rx-x^3=-\\partial_xV,\\ V=-\\tfrac r2x^2+\\tfrac14x^4\\Rightarrow x^*=\\pm\\sqrt r", "breaks": "No fluctuations or thermodynamic limit, so only mean-field exponents; Hopf bifurcations break time translation rather than an internal symmetry.", "confidence": "established", "strength": 2}
{"id": "C0077", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation", "name": "Kuramoto sync and Turing patterns as symmetry breaking", "kind": "analogy", "summary": "Kuramoto synchronization is a U(1)-breaking transition with order parameter re^{iψ} and mean-field exponent 1/2; Turing patterns spontaneously break translation symmetry.", "map": "re^{i\\psi}=\\frac1N\\sum_je^{i\\theta_j},\\quad r\\propto(K-K_c)^{1/2}", "breaks": "Driven-dissipative attractors with no free energy or detailed balance; the phase mode diffuses rather than propagating, and noise can restore the symmetry.", "confidence": "established", "strength": 2}
{"id": "C0078", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "name": "Galileo's square–cube law", "kind": "historical", "summary": "Galileo's 1638 argument that beam strength scales as L² while weight scales as L³ is the first scaling law and limits the size of animals and structures; Euler buckling follows the same logic.", "map": "\\frac{\\text{strength}}{\\text{weight}}\\propto L^{-1},\\quad P_{cr}=\\frac{\\pi^2EI}{L^2}", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C0079", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "name": "Buckingham π ↔ Reynolds similarity", "kind": "method transfer", "summary": "Dimensional analysis reduces drag and flow problems to functions of a few dimensionless groups (Re, Ma, Fr), which is the basis of wind-tunnel scaling and dynamic similarity.", "map": "F_D=\\tfrac12\\rho v^2L^2\\,C_D(Re,Ma),\\quad Re=\\rho vL/\\mu", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0080", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics", "name": "Re ≪ 1 regime and the scallop theorem", "kind": "method transfer", "summary": "At Re ≪ 1 inertia drops out and Stokes flow is linear and instantaneous, so reciprocal strokes give no net swimming (Purcell's scallop theorem); scaling arguments set what microswimmers can do.", "map": "Re=\\frac{\\rho UL}{\\mu}\\sim10^{-5}\\ (\\text{bacterium}),\\quad \\mu\\nabla^2\\mathbf u=\\nabla p", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0081", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "name": "Kolmogorov 1941 from dimensional analysis", "kind": "method transfer", "summary": "If the inertial range depends only on the dissipation rate ε and wavenumber k, dimensional analysis fixes the −5/3 spectrum and the Kolmogorov scale; intermittency corrections are the anomalous part beyond dimensional reasoning.", "map": "E(k)=C_K\\epsilon^{2/3}k^{-5/3},\\quad \\eta=(\\nu^3/\\epsilon)^{1/4}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0082", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "02-electromagnetism-and-optics/photonics-and-lasers/integrated-and-fiber-photonics", "name": "Photonic neural-network hardware and ML inverse design", "kind": "method transfer", "summary": "Any N×N unitary factorizes into a mesh of Mach–Zehnder interferometers (Reck and Clements decompositions). Programmable silicon-photonic meshes can therefore perform the matrix–vector products of neural-network inference optically. In the other direction, adjoint-gradient and neural-network inverse design produce non-intuitive waveguide, coupler and metasurface geometries.", "map": "U(N)=D\\prod_{(m,n)}T_{mn}(\\theta,\\phi),\\quad \\#T_{mn}=\\frac{N(N-1)}{2}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0083", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/electrostatics-and-boundary-value-problems", "name": "Ewald summation: electrostatics on a periodic lattice", "kind": "method transfer", "summary": "Periodic simulations need the Coulomb energy of an infinite lattice of images, a conditionally convergent sum. Ewald splits 1/r into a short-range erfc part summed in real space and a smooth part summed in Fourier space. The leftover surface-dipole term depends on the dielectric condition at infinity; tin-foil boundaries (ε'=∞) are the usual choice.", "map": "\\frac{1}{r}=\\frac{\\mathrm{erfc}(\\kappa r)}{r}+\\frac{\\mathrm{erf}(\\kappa r)}{r};\\quad \\text{PME/P}^3\\text{M: }O(N\\log N)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0084", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "name": "Monte Carlo radiative transfer through turbid media", "kind": "method transfer", "summary": "Multiple scattering of light in clouds, tissue and dust is simulated as random walks of photon packets. Free paths are drawn from the extinction coefficient and scattering angles from a Mie or Henyey–Greenstein phase function. This solves the radiative transfer equation statistically where the diffusion approximation fails.", "map": "s=-\\ln\\xi/\\mu_t,\\quad p_{\\rm HG}(\\cos\\theta)=\\frac{1-g^2}{2(1+g^2-2g\\cos\\theta)^{3/2}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0085", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "02-electromagnetism-and-optics/electrodynamics/maxwells-equations", "name": "Yee's FDTD scheme for Maxwell's curl equations", "kind": "method transfer", "summary": "The finite-difference time-domain method staggers E and H by half a cell in space and half a step in time (leapfrog). The discrete curls then conserve the discrete divergence of B exactly, and of D given charge conservation, a discrete-exterior-calculus structure. Stability obeys the CFL bound. FDTD and edge-element finite elements are the workhorses of photonics and antenna design.", "map": "c\\,\\Delta t\\le\\Big(\\frac{1}{\\Delta x^2}+\\frac{1}{\\Delta y^2}+\\frac{1}{\\Delta z^2}\\Big)^{-1/2},\\quad \\nabla_h\\cdot(\\nabla_h\\times\\,\\cdot\\,)\\equiv0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0086", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "02-electromagnetism-and-optics/photonics-and-lasers/nonlinear-optics", "name": "Split-step Fourier solution of the fibre NLSE", "kind": "method transfer", "summary": "Pulse propagation in a Kerr fibre obeys the nonlinear Schrödinger equation, solved by operator splitting. Dispersion is applied exactly in the Fourier domain and self-phase modulation in the time domain; Strang splitting makes the scheme second order. This norm-preserving pseudospectral method also underlies Lugiato–Lefever simulations of Kerr combs and solitons.", "map": "\\partial_zA=-\\frac{i\\beta_2}{2}\\partial_T^2A+i\\gamma|A|^2A,\\quad A(z+h)\\approx e^{h\\hat D/2}e^{h\\hat N}e^{h\\hat D/2}A(z)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0087", "a": "00-foundations/history-and-philosophy-of-physics/history-of-physics", "b": "02-electromagnetism-and-optics/electrodynamics/maxwells-equations", "name": "Maxwell's unification and the speed of light", "kind": "historical", "summary": "With the displacement current, Maxwell (1865) derived transverse waves travelling at 1/√(ε₀μ₀). That speed matched both Weber and Kohlrausch's measured ratio of electromagnetic to electrostatic units and the speed of light, so light became an electromagnetic wave. Hertz's 1887–88 experiments confirmed it, making this the archetype of unification in physics.", "map": "c=\\frac{1}{\\sqrt{\\epsilon_0\\mu_0}}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0088", "a": "00-foundations/history-and-philosophy-of-physics/history-of-physics", "b": "02-electromagnetism-and-optics/electrodynamics/relativistic-electrodynamics", "name": "Electrodynamics of moving bodies gave special relativity", "kind": "historical", "summary": "Einstein's 1905 paper opens with the magnet–conductor asymmetry of Maxwell–Lorentz electrodynamics. He resolved it by making the Lorentz transformations, which already leave Maxwell's equations invariant, the kinematics of space and time. Minkowski's 1908 tensor form then made E and B frame-dependent parts of one object, so relativity grew out of electrodynamics rather than mechanics.", "map": "F'^{\\mu\\nu}=\\Lambda^\\mu{}_\\alpha\\Lambda^\\nu{}_\\beta F^{\\alpha\\beta}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0089", "a": "00-foundations/history-and-philosophy-of-physics/philosophy-of-physics", "b": "02-electromagnetism-and-optics/electrodynamics/potentials-and-gauge-invariance", "name": "Are potentials real? Gauge and the Aharonov–Bohm effect", "kind": "shared object", "summary": "The Aharonov–Bohm phase shows that charged quanta respond to A where B vanishes. This forces a choice: gauge-dependent potentials acting locally, gauge-invariant loop holonomies acting nonlocally, or nonlocal field interactions. It is the main test case for whether gauge symmetry is mere redundancy of description or physically significant.", "map": "\\Delta\\varphi_{AB}=\\frac{q}{\\hbar}\\oint\\mathbf A\\cdot d\\mathbf l=\\frac{q\\Phi_B}{\\hbar}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0090", "a": "00-foundations/history-and-philosophy-of-physics/philosophy-of-physics", "b": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "name": "Radiation reaction and consistency of classical ED", "kind": "shared object", "summary": "The Abraham–Lorentz–Dirac equation for a radiating point charge is third order, with runaway solutions and pre-acceleration, and the point charge's self-energy diverges. Whether classical electrodynamics of point particles is even consistent, and how to read the reduced-order Landau–Lifshitz fix, is debated in philosophy of physics. Strong-field laser experiments now probe the same question.", "map": "m\\dot u^\\mu=qF^{\\mu\\nu}u_\\nu+\\frac{q^2}{6\\pi\\epsilon_0c^3}\\Big(\\ddot u^\\mu+\\frac{\\dot u_\\nu\\dot u^\\nu}{c^2}u^\\mu\\Big)", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0091", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "02-electromagnetism-and-optics/classical-optics/geometric-optics", "name": "Rays as the stationary-phase limit; Airy caustics", "kind": "identity", "summary": "Geometric optics is the stationary-phase asymptotics of the diffraction integral as k→∞: rays are the stationary points of the optical path. Where two rays merge, the method fails at a caustic. The intensity there follows the Airy function, as in Airy's rainbow theory, which is where catastrophe optics begins.", "map": "\\int e^{ik\\phi(x)}dx\\sim\\sqrt{\\frac{2\\pi}{k|\\phi''|}}e^{ik\\phi(x_0)\\pm i\\pi/4},\\ \\phi'(x_0)=0;\\ \\text{fold caustic: }I\\propto\\mathrm{Ai}^2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0092", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/electrostatics-and-boundary-value-problems", "name": "Conformal mapping for 2D electrostatics", "kind": "method transfer", "summary": "In two dimensions the potential is the real part of an analytic complex potential w(z), whose level curves are equipotentials and field lines. Conformal maps, including Schwarz–Christoffel, carry a solved geometry into edges, slots and fringing-field capacitors. It is the same tool used for 2D potential flow.", "map": "w(z)=\\Phi+i\\Psi,\\ \\nabla^2\\Phi=0,\\ E_x-iE_y=-\\frac{dw}{dz}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0093", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/fields-in-matter", "name": "Kramers–Kronig: causality makes ε(ω) analytic", "kind": "identity", "summary": "Polarization cannot come before the field that causes it, so the susceptibility is analytic in the upper half ω-plane. The dispersive and absorptive parts of ε(ω) are then Hilbert transforms of each other. Lorentz-oscillator models satisfy this; conductors need the DC-conductivity pole treated separately. Kronig (1926) and Kramers (1927) first derived the relations for the dispersion of light and X-rays.", "map": "\\mathrm{Re}\\,\\epsilon(\\omega)-1=\\frac{2}{\\pi}\\mathcal P\\!\\int_0^\\infty\\frac{\\omega'\\,\\mathrm{Im}\\,\\epsilon(\\omega')}{\\omega'^2-\\omega^2}d\\omega'", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0094", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/multipole-expansions", "name": "Legendre generating function is the multipole expansion", "kind": "identity", "summary": "Expanding the Coulomb kernel 1/|r−r'| in powers of r_</r_> generates the Legendre polynomials, and the addition theorem turns them into spherical harmonics. Multipole moments are just the source's expansion coefficients in these eigenfunctions of the angular Laplacian.", "map": "\\frac{1}{|\\mathbf r-\\mathbf r'|}=\\sum_l\\frac{r_<^l}{r_>^{l+1}}P_l(\\cos\\gamma)=\\sum_{lm}\\frac{4\\pi}{2l+1}\\frac{r_<^l}{r_>^{l+1}}Y_{lm}^*(\\Omega')Y_{lm}(\\Omega)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0095", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "02-electromagnetism-and-optics/classical-optics/interference-and-diffraction", "name": "Huygens–Fresnel principle as a Green's-function integral", "kind": "identity", "summary": "Kirchhoff diffraction comes from applying Green's theorem to the Helmholtz equation with the outgoing Green's function e^{ikr}/r. This turns Huygens' secondary wavelets into an exact representation. Kirchhoff's boundary conditions are inconsistent, which the Rayleigh–Sommerfeld Dirichlet Green's function repairs. Fresnel and Fraunhofer diffraction are its paraxial and far-field limits.", "map": "U(P)=\\frac{1}{4\\pi}\\oint_S\\left[U\\,\\partial_n\\frac{e^{iks}}{s}-\\frac{e^{iks}}{s}\\,\\partial_nU\\right]dS", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0096", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "name": "Waveguide and cavity modes as Sturm–Liouville eigenproblems", "kind": "identity", "summary": "In a hollow metal guide the longitudinal field obeys the transverse Helmholtz equation, with Dirichlet conditions for TM modes (E_z=0) and Neumann conditions for TE modes (∂_nH_z=0). The eigenvalues set the cutoff frequencies. The complete orthogonal eigenfunctions are the modes into which any guided field expands, like a drum head.", "map": "(\\nabla_t^2+\\gamma_{mn}^2)\\psi=0,\\quad k_z^2=\\frac{\\omega^2}{c^2}-\\gamma_{mn}^2,\\quad \\omega_c=c\\,\\gamma_{mn}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0097", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "02-electromagnetism-and-optics/electrodynamics/potentials-and-gauge-invariance", "name": "Retarded potentials from the wave-equation Green's function", "kind": "identity", "summary": "In Lorenz gauge each potential obeys a sourced wave equation, so V and A are ρ and J convolved with the retarded Green's function of the d'Alembertian. Causality selects G_ret over G_adv. Coulomb gauge trades this for an instantaneous Poisson Green's function for V.", "map": "\\Box A^\\mu=\\mu_0J^\\mu,\\ G_{\\rm ret}=\\frac{\\delta(t-t'-|\\mathbf r-\\mathbf r'|/c)}{4\\pi|\\mathbf r-\\mathbf r'|}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0098", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics", "name": "Statics as Poisson problems for V and A", "kind": "identity", "summary": "Electrostatics, and magnetostatics in Coulomb gauge, both reduce to Poisson equations: one for V and one for each Cartesian component of A. Coulomb's law and the Biot–Savart law are therefore both the sources convolved with the same Green's function 1/(4πr).", "map": "\\nabla^2V=-\\rho/\\epsilon_0,\\ \\nabla^2\\mathbf A=-\\mu_0\\mathbf J\\Rightarrow\\mathbf A=\\mu_0\\int G\\,\\mathbf J\\,d^3r',\\ G=\\frac{1}{4\\pi|\\mathbf r-\\mathbf r'|}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0099", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/electrostatics-and-boundary-value-problems", "name": "Coulomb potential as the Laplacian's Green's function", "kind": "identity", "summary": "The point-charge potential is the free-space Green's function of the Laplacian. Dirichlet and Neumann Green's functions, the method of images and separation of variables (via Sturm–Liouville completeness) are the general PDE tools applied to conductors. Uniqueness follows from the elliptic type of the problem.", "map": "\\nabla^2G=-\\delta^3(\\mathbf r-\\mathbf r'),\\ G_D|_S=0:\\ \\Phi=\\frac{1}{\\epsilon_0}\\int\\rho\\,G_D\\,d^3r'-\\oint_S\\Phi\\,\\partial_{n'}G_D\\,da'", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0100", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "name": "Liénard–Wiechert fields and Dirac's radiation reaction", "kind": "identity", "summary": "Evaluating the retarded Green's function on a point charge's worldline gives the Liénard–Wiechert potentials; the 1−n̂·β factor is the Jacobian of the retarded-time delta function. Dirac took the radiation-reaction field to be half the retarded minus half the advanced field, a combination that is regular at the charge.", "map": "V=\\frac{q}{4\\pi\\epsilon_0}\\left[\\frac{1}{(1-\\hat{\\mathbf n}\\cdot\\boldsymbol\\beta)R}\\right]_{\\rm ret},\\quad F_{\\rm rad}=\\tfrac12(F_{\\rm ret}-F_{\\rm adv})", "breaks": "", "confidence": "established", "strength": 3}