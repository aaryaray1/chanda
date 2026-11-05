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

# Packet 00-5 (57 records)

{"id": "C0401", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Fokker–Planck collisions and Monte Carlo operators", "kind": "method transfer", "summary": "Coulomb collisions are a Fokker–Planck diffusion in velocity space, implemented by Monte Carlo binary-collision models (Takizuka–Abe) in PIC, equivalent to a Langevin stochastic process.", "map": "\\partial_t f=-\\partial_v(Af)+\\tfrac12\\partial_v^2(Df)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0402", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "10-plasma-physics/inertial-and-laser-plasmas/inertial-confinement-fusion", "name": "Radiation-hydrodynamics codes for ICF", "kind": "method transfer", "summary": "ICF design relies on multi-physics finite-volume or Lagrangian hydrodynamics coupled to radiation transport and shock-capturing schemes to model implosions and Rayleigh–Taylor growth.", "map": "\\partial_t U+\\nabla\\cdot F(U)=S", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0403", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "10-plasma-physics/inertial-and-laser-plasmas/plasma-wakefield-acceleration", "name": "Particle-in-cell simulation of wakefields", "kind": "method transfer", "summary": "PIC codes, often with boosted frames and quasi-static or envelope reductions, are the primary design tool for wakefield accelerators, whose bubble regime was found through simulation.", "map": "\\nabla\\cdot\\mathbf E=\\rho/\\epsilon_0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0404", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "Divergence-free constraint and conservative MHD solvers", "kind": "method transfer", "summary": "Numerical MHD needs constrained transport, Godunov/Riemann solvers and divergence cleaning to preserve ∇·B=0; these schemes were developed for MHD and spread to astrophysical fluid codes.", "map": "\\nabla\\cdot\\mathbf B=0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0405", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "10-plasma-physics/magnetohydrodynamics/mhd-turbulence", "name": "Spectral direct numerical simulation of MHD turbulence", "kind": "method transfer", "summary": "Pseudo-spectral DNS is the main tool to test anisotropic cascade and critical-balance predictions; resolution limits restrict inertial range and Reynolds number, linking to astrophysical turbulence reviews.", "map": "\\partial_t\\mathbf z^\\pm\\mp\\mathbf V_A\\!\\cdot\\!\\nabla\\mathbf z^\\pm=\\ldots", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0406", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Vlasov solvers and spectral methods", "kind": "method transfer", "summary": "Vlasov–Maxwell is solved by semi-Lagrangian, spectral (Hermite) and discontinuous-Galerkin schemes; recurrence and filamentation in velocity space limit resolution, and symplectic or structure-preserving integrators conserve invariants.", "map": "\\partial_t f+v\\partial_x f+\\frac{qE}{m}\\partial_v f=0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0407", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Boris pusher and symplectic integrators", "kind": "method transfer", "summary": "The Boris algorithm advances charged particles in E and B volume-preservingly with long-term stability, a precursor of modern structure-preserving integrators used in particle-in-cell codes.", "map": "\\mathbf v^{n+1/2}=\\mathbf v^{n-1/2}+\\frac{q\\Delta t}{m}(\\mathbf E+\\bar{\\mathbf v}\\times\\mathbf B)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0408", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Kramers–Kronig dispersion relations in plasma response", "kind": "identity", "summary": "Causality of the plasma dielectric response implies analyticity in the upper half ω-plane and Kramers–Kronig relations linking reactive and dissipative (Landau) parts.", "map": "\\mathrm{Re}\\,\\epsilon(\\omega)-1=\\frac{2}{\\pi}P\\!\\int\\frac{\\omega'\\,\\mathrm{Im}\\,\\epsilon(\\omega')}{\\omega'^2-\\omega^2}d\\omega'", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0409", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Landau contour and plasma dispersion function", "kind": "method transfer", "summary": "Landau damping arises from the pole in the Vlasov dispersion integral; Landau's analytic-continuation prescription (deforming the contour) gives the Fried–Conte plasma dispersion function Z, a Faddeeva/error-function relative.", "map": "\\epsilon(k,\\omega)=1+\\frac{1}{k^2\\lambda_D^2}[1+\\zeta Z(\\zeta)]", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0410", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks", "name": "Diffusive shock acceleration power-law spectrum", "kind": "shared object", "summary": "Diffusive shock acceleration yields a power-law spectrum from a Bessel/Green's-function-type transport problem and compression-ratio dependence; the shared paper reflects asymptotic and special-function methods in acceleration theory.", "map": "f(p)\\propto p^{-3r/(r-1)}", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C0411", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "MHD stability as Sturm–Liouville / self-adjoint problem", "kind": "mechanism", "summary": "Linear ideal MHD is a self-adjoint force operator problem, so the energy principle δW and normal-mode spectrum follow from variational Sturm–Liouville-type theory.", "map": "\\omega^2\\rho\\xi=\\mathbf{F}[\\xi],\\quad \\delta W=-\\tfrac12\\int\\xi\\cdot\\mathbf F[\\xi]", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0412", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Dispersion relations from linearized PDEs", "kind": "method transfer", "summary": "Plasma waves and instabilities are found by Fourier–Laplace transforming linearized fluid or Vlasov equations; the initial-value problem and Green's-function causality (Bers–Briggs) distinguish absolute from convective instability.", "map": "D(k,\\omega)=0,\\quad \\omega=\\omega_r+i\\gamma", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0413", "a": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "Self-adjoint force operator and spectral theorem", "kind": "identity", "summary": "The MHD force operator is Hermitian on a Hilbert space with energy inner product, giving real ω² and a spectrum with discrete and continuous parts (Alfvén and slow continua), with non-normal subtleties in flows.", "map": "\\langle\\eta,F\\xi\\rangle=\\langle F\\eta,\\xi\\rangle", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0414", "a": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Van Kampen modes and continuous spectrum", "kind": "mechanism", "summary": "Van Kampen's treatment of linearized Vlasov uses singular eigenfunctions of a continuous spectrum, with Landau damping appearing as phase mixing; the Vlasov operator is non-self-adjoint in general.", "map": "\\partial_t\\delta f+ikv\\,\\delta f=\\ldots", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0415", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "10-plasma-physics/magnetohydrodynamics/dynamo-theory", "name": "Frozen-in flux as Lie dragging of a 2-form", "kind": "identity", "summary": "Ideal MHD induction is Lie transport of the magnetic flux 2-form, and helicity is a differential-form integral; this geometric view clarifies the Cauchy solution and topological constraints.", "map": "\\partial_t B=\\nabla\\times(v\\times B)\\;\\Leftrightarrow\\;(\\partial_t+\\mathcal L_v)\\,\\mathbf B^{(2)}=0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0416", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Langmuir probes and plasma diagnostics", "kind": "shared object", "summary": "Diagnostics such as Langmuir probes, Thomson scattering and interferometry rely on Debye sheath physics and detector noise limits; probe I–V curves infer density and temperature.", "map": "I=I_{sat}\\left[1-\\exp\\!\\left(\\frac{e(V-V_f)}{k_BT_e}\\right)\\right]", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0417", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "10-plasma-physics/magnetohydrodynamics/mhd-turbulence", "name": "Structure functions and spectral inference of turbulence", "kind": "method transfer", "summary": "Solar wind turbulence exponents are estimated from spacecraft time series using structure functions and power spectra, with finite-sample and intermittency biases requiring statistical care.", "map": "S_p(\\ell)=\\langle|\\delta u(\\ell)|^p\\rangle\\propto\\ell^{\\zeta_p}", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C0418", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "10-plasma-physics/magnetic-confinement-fusion/stellarators", "name": "Quasi-symmetry and conserved canonical momentum", "kind": "identity", "summary": "Quasi-symmetry in stellarators makes |B| symmetric in Boozer coordinates, so a Noether-type canonical momentum is conserved and guiding-centre orbits are confined like in tokamaks; omnigeneity generalizes this.", "map": "B=B(\\psi,M\\theta-N\\varphi)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0419", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "10-plasma-physics/magnetic-confinement-fusion/tokamaks", "name": "Axisymmetry gives conserved toroidal angular momentum", "kind": "identity", "summary": "Toroidal axisymmetry of a tokamak yields conservation of canonical toroidal angular momentum, confining particle orbits and underpinning neoclassical theory; stellarators lack this, hence 3D optimization.", "map": "p_\\varphi=mRv_\\varphi+q\\psi\\ \\text{const}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0420", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "Magnetic helicity and cross-helicity conservation", "kind": "identity", "summary": "Ideal MHD has conserved helicity invariants arising from relabelling symmetry of the fluid Lagrangian (Noether), constraining reconnection, dynamos and turbulent cascades.", "map": "H=\\int\\mathbf A\\cdot\\mathbf B\\,dV", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0421", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Adiabatic invariants from approximate symmetry", "kind": "identity", "summary": "The magnetic moment and other adiabatic invariants are Noether-type conserved quantities of averaged Lagrangians with a slow-variable approximate symmetry; guiding-centre theory uses Lie-transform perturbation of the Hamiltonian structure.", "map": "\\mu=\\frac{m v_\\perp^2}{2B},\\quad J=\\oint p\\,dq", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0422", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "10-plasma-physics/magnetohydrodynamics/dynamo-theory", "name": "Dynamo as symmetry-breaking of field", "kind": "analogy", "summary": "Dynamos spontaneously break symmetries of the flow, such as reflection and time-reversal in geodynamo reversals, and the α-effect needs broken mirror symmetry (helicity); dynamo onset resembles a bifurcation with a growth-rate order parameter.", "map": "\\partial_t \\bar B=\\nabla\\times(\\alpha\\bar B)+\\eta\\nabla^2\\bar B", "breaks": "Dynamo growth is a kinematic linear instability, not an equilibrium ordered phase; no Goldstone modes in the usual sense.", "confidence": "current research", "strength": 2}
{"id": "C0423", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Debye screening and Meissner/Higgs screening", "kind": "analogy", "summary": "Debye screening gives a Yukawa-type potential with length λ_D, analogous to the finite penetration depth of magnetic fields in superconductors and the massive gauge boson range in the Higgs phase.", "map": "\\phi\\propto e^{-r/\\lambda_D}/r\\leftrightarrow e^{-mr}/r", "breaks": "Debye screening is a thermal static effect, not a symmetry-breaking vacuum condensate, and the screening is electric rather than magnetic.", "confidence": "established", "strength": 2}
{"id": "C0424", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Plasma frequency and Higgs/Anderson mass generation", "kind": "analogy", "summary": "Anderson noted that Coulomb long-range interaction turns the gapless Goldstone-like phonon into a gapped plasmon, the prototype of the Higgs mechanism; gauge field gives photon effective mass, as in plasma screening.", "map": "\\omega^2=\\omega_p^2+c^2k^2\\leftrightarrow E^2=m^2+p^2", "breaks": "The plasma has no spontaneously broken local gauge symmetry; the photon mass is an effective in-medium dispersion, with the rest frame privileged.", "confidence": "established", "strength": 2}
{"id": "C0425", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "10-plasma-physics/magnetic-confinement-fusion/turbulent-transport-and-gyrokinetics", "name": "Gyro-Bohm scaling and dimensionless confinement scaling", "kind": "method transfer", "summary": "Tokamak confinement scalings use Kadomtsev's constraint and Buckingham π to reduce parameters to ρ*, β, ν*; gyro-Bohm transport scales as ρ*χ_Bohm, enabling extrapolation to ITER.", "map": "\\chi_{gB}\\sim\\rho_*\\,\\frac{T}{eB}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0426", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "10-plasma-physics/magnetohydrodynamics/magnetic-reconnection", "name": "Sweet–Parker scaling with Lundquist number", "kind": "method transfer", "summary": "The Sweet–Parker inflow rate follows from mass and flux balance, giving a scaling in Lundquist number S; plasmoid instability sets a critical S≈10^4 beyond which rate becomes S-independent.", "map": "v_{in}/V_A\\sim S^{-1/2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0427", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "10-plasma-physics/magnetohydrodynamics/mhd-turbulence", "name": "Kolmogorov-style dimensional spectra for MHD turbulence", "kind": "method transfer", "summary": "Iroshnikov–Kraichnan and Goldreich–Sridhar spectra are derived by constant-flux dimensional arguments and critical balance, extending Kolmogorov scaling to magnetized fluids.", "map": "E(k_\\perp)\\propto\\epsilon^{2/3}k_\\perp^{-5/3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0428", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Plasma parameters as dimensionless groups", "kind": "method transfer", "summary": "Plasma regimes are classified by dimensionless numbers such as the plasma parameter, Lundquist number, beta and normalized gyroradius; similarity scaling lets lab experiments emulate astrophysical plasmas.", "map": "\\Lambda=n\\lambda_D^3,\\quad S=\\frac{LV_A}{\\eta}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0429", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "name": "ML structure prediction and neural force fields", "kind": "method transfer", "summary": "Deep networks predict protein structure from sequence and learn machine-learned potentials for MD, replacing explicit physics with learned surrogates trained on data.", "map": "", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0430", "a": "00-foundations/computational-physics/machine-learning-for-physics", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "ML weather emulators", "kind": "method transfer", "summary": "Neural surrogates trained on reanalysis now match or beat numerical weather prediction at medium range at far lower cost, replacing PDE integration with learned dynamics.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0431", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "11-interdisciplinary-physics/applied-and-device-physics/energy-materials-and-thermoelectrics", "name": "MD of ion transport in electrolytes", "kind": "method transfer", "summary": "MD, including machine-learned potentials, computes ionic conductivity and diffusion in solid electrolytes and battery materials.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0432", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "name": "MD simulation of protein folding and dynamics", "kind": "method transfer", "summary": "Force-field molecular dynamics, enhanced sampling and specialised hardware are used to simulate folding, binding and conformational change of proteins, connecting folding landscapes to integrated equations of motion.", "map": "m\\ddot{\\mathbf r}_i=-\\nabla_i U(\\{\\mathbf r\\})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0433", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "11-interdisciplinary-physics/biophysics/molecular-biophysics-and-protein-folding", "name": "Protein folding as a test case for MD", "kind": "shared object", "summary": "Folding timescales and force-field accuracy drive MD development (thermostats, enhanced sampling), while MD supplies atomistic folding pathways that test energy-landscape theory.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0434", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Trajectories on potential energy surfaces", "kind": "method transfer", "summary": "Classical and ab initio MD trajectories sample reactive events, test transition-state theory and recrossing, and give rate constants via rare-event methods.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0435", "a": "00-foundations/computational-physics/molecular-dynamics", "b": "11-interdisciplinary-physics/chemical-physics/surface-science-and-catalysis", "name": "Ab initio MD of surfaces and catalysis", "kind": "method transfer", "summary": "DFT-based MD and kinetic Monte Carlo model adsorption, diffusion and reactions on catalyst surfaces.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0436", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "Monte Carlo simulation of PET and SPECT", "kind": "method transfer", "summary": "Monte Carlo photon transport (GATE, GEANT4) models scatter, attenuation and detector response, used for system design and image correction in emission tomography.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0437", "a": "00-foundations/computational-physics/monte-carlo-methods", "b": "11-interdisciplinary-physics/medical-physics/radiation-therapy", "name": "Monte Carlo dose calculation", "kind": "method transfer", "summary": "Metropolis-era stochastic sampling of particle transport is the gold standard for dose calculation in photon and proton therapy, tracking showers event by event.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0438", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Symplectic tracking of beams", "kind": "method transfer", "summary": "Long-term particle tracking in rings uses symplectic integrators to preserve phase-space structure over billions of turns, as in celestial mechanics.", "map": "\\mathbf z_{n+1}=M(\\mathbf z_n),\\; M^TJM=J", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0439", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Numerical weather and climate models", "kind": "method transfer", "summary": "Weather and climate models discretise the primitive equations with finite-volume, spectral and semi-implicit schemes; numerical stability and conservation properties are central, and chaos limits predictability.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0440", "a": "00-foundations/computational-physics/numerical-methods-for-odes-and-pdes", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics", "name": "Ocean general circulation modelling", "kind": "method transfer", "summary": "Ocean models rely on finite-volume/difference solvers for stratified rotating flow; numerical diffusion and resolution of eddies control simulated heat uptake and AMOC.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0441", "a": "00-foundations/computational-physics/tensor-network-methods", "b": "11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods", "name": "DMRG for strongly correlated molecules", "kind": "method transfer", "summary": "DMRG, developed for 1D spin chains, was adapted to quantum chemistry as a multireference method for active spaces of transition-metal and other strongly correlated molecules.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0442", "a": "00-foundations/computational-physics/tensor-network-methods", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "MCTDH and tensor-train wavepackets", "kind": "method transfer", "summary": "Multilayer MCTDH for quantum nuclear dynamics on potential energy surfaces is a hierarchical tensor decomposition equivalent to tree tensor networks.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0443", "a": "00-foundations/mathematical-methods/complex-analysis-and-special-functions", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Fourier transform: k-space MRI and Radon slice", "kind": "identity", "summary": "MRI data are samples of the Fourier transform of magnetisation (k-space) and CT sinograms relate to it via the Fourier slice theorem, so image formation is Fourier analysis.", "map": "S(\\mathbf k)=\\int \\rho(\\mathbf r)e^{-i\\mathbf k\\cdot\\mathbf r}d^3r", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0444", "a": "00-foundations/mathematical-methods/differential-equations-and-greens-functions", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Wave equation and Green's functions in seismology", "kind": "mechanism", "summary": "Seismic wavefields are solved as elastic wave equation with Green's functions; source inversion and ambient-noise correlation recover the Green's function between stations.", "map": "\\rho\\ddot u_i=\\partial_j(c_{ijkl}\\partial_k u_l)+f_i", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0445", "a": "00-foundations/mathematical-methods/linear-algebra-and-hilbert-spaces", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Inverse problems in tomographic reconstruction", "kind": "method transfer", "summary": "CT reconstruction (filtered back-projection, iterative, regularised) is a linear inverse problem solved with Fourier slice theorem, SVD and regularisation.", "map": "g=Af,\\; \\hat f=\\arg\\min\\|Af-g\\|^2+\\lambda R(f)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0446", "a": "00-foundations/mathematical-methods/tensors-and-differential-geometry", "b": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "name": "Differential geometry of membranes", "kind": "mechanism", "summary": "Membrane shapes are surfaces whose mean and Gaussian curvature enter the Helfrich bending energy; Gauss–Bonnet makes topology constrain vesicle shape.", "map": "E=\\int\\frac{\\kappa}{2}(2H-c_0)^2+\\bar\\kappa K\\,dA", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0447", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Noise limits and lock-in detection", "kind": "shared object", "summary": "Lock-in detection, shot-noise and thermal-noise limits govern SQUIDs, NV magnetometers and atomic sensors alike.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0448", "a": "00-foundations/measurement-and-data-analysis/detectors-and-instrumentation", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "Scintillators and photodetectors in PET", "kind": "shared object", "summary": "Scintillator crystals, SiPMs and fast timing electronics from particle detectors underpin gamma cameras and time-of-flight PET, with noise and timing resolution as the figures of merit.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0449", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "name": "Statistical inference for single-molecule traces", "kind": "method transfer", "summary": "Hidden Markov models, maximum likelihood and Bayesian change-point analysis extract states and rates from noisy FRET and tweezer trajectories.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0450", "a": "00-foundations/measurement-and-data-analysis/statistical-inference-in-physics", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Detection and attribution as inference", "kind": "method transfer", "summary": "Climate detection and attribution applies optimal fingerprinting, regression and Bayesian inference to separate forced signal from internal variability, analogous to discovery claims in particle physics.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0451", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Point groups and selection rules", "kind": "mechanism", "summary": "Group representations of molecular point groups and SO(3) determine which vibrational, rotational and electronic transitions are allowed in IR, Raman and electronic spectra.", "map": "\\Gamma_i\\otimes\\Gamma_\\mu\\otimes\\Gamma_f\\ni A_1", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0452", "a": "00-foundations/symmetry-and-group-theory/lie-groups-and-representations", "b": "11-interdisciplinary-physics/chemical-physics/quantum-chemistry-methods", "name": "Symmetry adaptation in electronic structure", "kind": "method transfer", "summary": "Spin and spatial point-group symmetry classify molecular states and reduce cost of Hartree–Fock, CI and coupled-cluster calculations.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0453", "a": "00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Liouville and Courant–Snyder invariants", "kind": "mechanism", "summary": "Hamiltonian phase-space structure gives conserved emittance and Courant–Snyder invariant for linear optics, with symplectic maps constraining beam evolution; damping breaks it.", "map": "\\gamma x^2+2\\alpha xx'+\\beta x'^2=\\varepsilon", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0454", "a": "00-foundations/symmetry-and-group-theory/spontaneous-symmetry-breaking", "b": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "name": "Symmetry breaking in developmental patterning", "kind": "analogy", "summary": "Turing-type instabilities and polarity establishment in cells resemble symmetry-breaking bifurcations with order parameters and Goldstone-like soft modes in active matter.", "map": "", "breaks": "Living systems are driven, non-equilibrium and finite, with no true Goldstone theorem or thermodynamic limit.", "confidence": "current research", "strength": 2}
{"id": "C0455", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "name": "Scaling laws in cell and membrane mechanics", "kind": "method transfer", "summary": "Dimensional analysis and scaling fix the bending-rigidity length scales, low-Reynolds-number motility and size dependence of cell mechanics.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0456", "a": "00-foundations/units-and-constants/dimensional-analysis-and-scaling", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Nondimensional numbers in geophysical flow", "kind": "method transfer", "summary": "Rossby, Ekman, Richardson and Reynolds numbers from Buckingham-π analysis identify the regimes of rotating stratified flow, justifying geostrophic and quasi-geostrophic approximations.", "map": "\\mathrm{Ro}=\\frac{U}{fL}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0457", "a": "00-foundations/units-and-constants/si-units-and-2019-redefinition", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Quantum standards realise SI units", "kind": "shared object", "summary": "Josephson and quantum Hall effects realise volt and ohm via h and e; atomic clocks and atom interferometers tie units to invariants of nature.", "map": "V=\\frac{nf}{K_J},\\; K_J=\\frac{2e}{h}", "breaks": "", "confidence": "established", "strength": 3}