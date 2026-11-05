You are the classical-physicist, the specialist for 01 (Classical Mechanics) in this physics knowledge base.

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

## Field overview · `knowledge/01-classical-mechanics`

> **Specialist:** `classical-physicist` · **arXiv:** physics.class-ph, nlin.CD, nlin.PS, physics.flu-dyn · **Literature source:** OpenAlex + arXiv

#### What this field studies
Classical mechanics describes systems where quantum effects are negligible ($S\gg\hbar$) and speeds are small compared with light. Its three formulations — Newtonian (forces), Lagrangian (action and generalized coordinates) and Hamiltonian (phase space) — are equivalent but suit different problems, and the latter two are the templates for quantum mechanics and field theory. The field is far from closed: chaos, turbulence and pattern formation remain active research frontiers.

#### Conventions used in this branch
- SI units; generalized coordinates $q_i$, momenta $p_i=\partial L/\partial\dot q_i$; overdots are time derivatives.
- Lagrangian $L=T-V$; Hamiltonian $H=\sum p_i\dot q_i-L$; Poisson bracket $\{f,g\}=\sum_i(\partial_{q_i}f\,\partial_{p_i}g-\partial_{p_i}f\,\partial_{q_i}g)$.
- Fluids: Eulerian description, material derivative $D/Dt=\partial_t+\mathbf u\cdot\nabla$.

#### Historical spine
1609–19 Kepler's laws · 1638 Galileo's *Two New Sciences* · 1687 Newton's *Principia* · 1736 Euler's *Mechanica* · 1752 Euler equations of fluids · 1788 Lagrange's *Mécanique analytique* · 1834 Hamilton's principle · 1845 Navier–Stokes · 1883 Reynolds' pipe-flow experiments · 1890 Poincaré and the three-body problem · 1941 Kolmogorov turbulence theory · 1954–63 KAM theorem · 1955 Fermi–Pasta–Ulam–Tsingou · 1963 Lorenz attractor · 1965 solitons · 1978 Feigenbaum universality.

#### Canonical textbooks
- Taylor, *Classical Mechanics*; Kleppner & Kolenkow, *An Introduction to Mechanics* — undergraduate.
- Goldstein, Poole & Safko, *Classical Mechanics*; Landau & Lifshitz, *Mechanics* — graduate standards.
- Arnold, *Mathematical Methods of Classical Mechanics* — the geometric view.
- Strogatz, *Nonlinear Dynamics and Chaos*; Ott, *Chaos in Dynamical Systems*.
- Landau & Lifshitz, *Fluid Mechanics*; Kundu & Cohen, *Fluid Mechanics*; Landau & Lifshitz, *Theory of Elasticity*.

#### Live frontiers
- Turbulence: intermittency, the Navier–Stokes regularity problem, data-driven closure models.
- Active and living fluids; granular flows; non-reciprocal interactions.
- Long-term stability of planetary systems and celestial mechanics with exoplanets.

#### How the specialist works here
Choose coordinates that respect symmetry, identify conserved quantities first, use the Lagrangian for constrained systems and the Hamiltonian for phase-space questions, nondimensionalize fluid problems to see which terms matter, and check every answer against limiting cases (small angles, zero damping, equal masses).

## Analytical mechanics · `knowledge/01-classical-mechanics/analytical-mechanics`

#### Overview
Analytical mechanics replaces vector forces with scalar functions (the Lagrangian and Hamiltonian) and a variational principle. Constraints are handled automatically, symmetries reveal conserved momenta, and phase-space geometry (symplectic structure, Liouville's theorem) provides the bridge to statistical mechanics and quantum mechanics.

#### Conceptual spine
1. Configuration space with generalized coordinates; action $S=\int L\,dt$.
2. $\delta S=0$ ⇒ Euler–Lagrange equations.
3. Legendre transform → Hamiltonian, phase space, symplectic flow.
4. Integrable systems admit action–angle variables; most systems are not integrable.

#### Key equations
$$\frac{d}{dt}\frac{\partial L}{\partial\dot q_i}-\frac{\partial L}{\partial q_i}=0,\qquad \dot q_i=\frac{\partial H}{\partial p_i},\ \dot p_i=-\frac{\partial H}{\partial q_i},\qquad \frac{\partial S}{\partial t}+H\!\left(q,\frac{\partial S}{\partial q},t\right)=0$$

#### Open problems
- Geometric integrators and structure-preserving discretizations for constrained and dissipative systems.

#### Connections
- [Path integrals](knowledge/04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics/README.md) · [Ensembles (phase space)](knowledge/03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/ensembles-and-partition-functions/README.md) · [Nonlinear dynamics](knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/README.md)

### Canonical transformations and Hamilton–Jacobi theory · `knowledge/01-classical-mechanics/analytical-mechanics/canonical-transformations-and-hamilton-jacobi`

**Scope.** Generating functions $F_1$–$F_4$, symplectic condition, infinitesimal canonical transformations and generators, Hamilton–Jacobi equation and separation of variables, Hamilton's characteristic function, action–angle variables, adiabatic invariants, Liouville–Arnold integrability.

**Core ideas.**
- Choose new variables in which the Hamiltonian is trivial; the Hamilton–Jacobi equation finds the generating function that does this.
- Action variables $J=\oint p\,dq$ are adiabatic invariants — the classical seed of Bohr–Sommerfeld quantization.
- An $n$-degree-of-freedom system with $n$ commuting integrals moves on invariant tori.

**Key equations.**
$$J=\oint p\,dq,\qquad \omega=\frac{\partial H}{\partial J},\qquad \theta(t)=\omega t+\theta_0$$

**See also.** [KAM theory](knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos/README.md) · [Semiclassics](knowledge/04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics/README.md)

### Hamiltonian mechanics · `knowledge/01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics`

**Scope.** Legendre transform, Hamilton's equations, phase portraits, Poisson brackets and constants of motion, Liouville's theorem, symplectic form, Hamiltonian flows, Noether in Hamiltonian form, Poincaré recurrence, Dirac's constrained Hamiltonian systems.

**Core ideas.**
- $H$ is conserved if it has no explicit time dependence; it equals the energy for natural systems.
- Phase-space volume is conserved (Liouville) — the basis of statistical mechanics.
- Poisson brackets become commutators in quantum mechanics: $\{f,g\}\to\frac{1}{i\hbar}[\hat f,\hat g]$.

**Key equations.**
$$\frac{df}{dt}=\{f,H\}+\frac{\partial f}{\partial t},\qquad \frac{\partial\rho}{\partial t}+\{\rho,H\}=0$$

**See also.** [Canonical transformations](knowledge/01-classical-mechanics/analytical-mechanics/canonical-transformations-and-hamilton-jacobi/README.md) · [Symplectic integrators](knowledge/00-foundations/computational-physics/numerical-methods-for-odes-and-pdes/README.md)

### Lagrangian mechanics · `knowledge/01-classical-mechanics/analytical-mechanics/lagrangian-mechanics`

**Scope.** Generalized coordinates, D'Alembert's principle, holonomic and non-holonomic constraints, Lagrange multipliers and constraint forces, cyclic (ignorable) coordinates, velocity-dependent potentials (charged particle: $L=\tfrac12mv^2-q\phi+q\mathbf v\cdot\mathbf A$), small oscillations, Lagrangian field theory.

**Core ideas.**
- Constraint forces drop out when coordinates are chosen to satisfy constraints.
- If $L$ does not depend on $q_k$, its conjugate momentum $p_k$ is conserved.
- Field theories use a Lagrangian density $\mathcal L(\phi,\partial_\mu\phi)$ — the same machinery.

**Key equations.**
$$\frac{d}{dt}\frac{\partial L}{\partial\dot q_k}-\frac{\partial L}{\partial q_k}=\sum_j\lambda_j\frac{\partial f_j}{\partial q_k}\quad(\text{constraints }f_j(q)=0)$$

**See also.** [Variational principles](knowledge/01-classical-mechanics/analytical-mechanics/variational-principles/README.md) · [Canonical quantization](knowledge/06-particle-physics/quantum-field-theory/canonical-and-path-integral-quantization/README.md)

### Variational principles · `knowledge/01-classical-mechanics/analytical-mechanics/variational-principles`

**Scope.** Euler–Lagrange equation of the calculus of variations, brachistochrone and catenary, isoperimetric problems, Hamilton's principle, Maupertuis' principle, Fermat's principle in optics, geodesics, action in field theory, stationary (not always minimal) action.

**Core ideas.**
- Physical paths make the action stationary; whether it is a minimum depends on conjugate points.
- The same variational structure gives geodesics (GR), light rays (optics) and field equations.
- Quantum mechanics explains why: stationary-phase dominance in the path integral.

**Key equations.**
$$\delta\int_{t_1}^{t_2}L(q,\dot q,t)\,dt=0,\qquad \delta\int n(\mathbf r)\,ds=0\ (\text{Fermat})$$

**Landmark.** Hamilton (1834) — see [subfield landmarks](knowledge/01-classical-mechanics/analytical-mechanics/README.md).

**See also.** [Path integrals](knowledge/04-quantum-physics/quantum-mechanics-core/path-integrals-and-semiclassics/README.md) · [Geometric optics](knowledge/02-electromagnetism-and-optics/classical-optics/geometric-optics/README.md)

## Continuum and fluid mechanics · `knowledge/01-classical-mechanics/continuum-and-fluid-mechanics`

#### Overview
When length scales are large compared with molecular spacing, matter is described by continuous fields — density, velocity, stress. Solids resist deformation elastically; fluids flow, governed by the Navier–Stokes equations. Dimensionless numbers (Reynolds, Rayleigh, Mach, Péclet) tell which effects dominate. Turbulence — chaotic, multiscale flow — remains one of the great unsolved problems of classical physics.

#### Key equations
$$\rho\left(\frac{\partial\mathbf u}{\partial t}+\mathbf u\cdot\nabla\mathbf u\right)=-\nabla p+\mu\nabla^2\mathbf u+\mathbf f,\qquad \nabla\cdot\mathbf u=0,\qquad Re=\frac{UL}{\nu}$$

#### Open problems
- Existence and smoothness of 3D Navier–Stokes solutions (Clay Millennium problem).
- Predictive theory of turbulent transition in pipes and boundary layers.

#### Connections
- [Magnetohydrodynamics](knowledge/10-plasma-physics/magnetohydrodynamics/README.md) · [Atmospheric dynamics](knowledge/11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics/README.md) · [Soft matter](knowledge/08-condensed-matter/soft-matter/README.md)

### Elasticity · `knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/elasticity`

**Scope.** Strain and stress tensors, generalized Hooke's law, Young's modulus, shear and bulk moduli, Poisson's ratio, P- and S-waves, Euler–Bernoulli beams, plate theory, Euler buckling, fracture mechanics basics, elasticity of thin sheets and crumpling.

**Core ideas.**
- Isotropic linear elasticity has two independent constants (e.g. Lamé $\lambda,\mu$).
- Longitudinal waves are faster than transverse waves; liquids carry no shear waves (Earth's liquid outer core).
- Slender structures fail by buckling at loads far below material strength.

**Key equations.**
$$\sigma_{ij}=\lambda\,\epsilon_{kk}\delta_{ij}+2\mu\,\epsilon_{ij},\qquad v_P=\sqrt{\frac{\lambda+2\mu}{\rho}},\ v_S=\sqrt{\frac\mu\rho},\qquad P_{\text{cr}}=\frac{\pi^2EI}{(KL)^2}$$

**See also.** [Seismology](knowledge/11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior/README.md) · [Phonons](knowledge/08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics/README.md)

### Ideal and viscous flow · `knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow`

**Scope.** Continuity, Euler equations, Bernoulli's theorem, potential flow, circulation and Kelvin's theorem, vorticity dynamics, lift (Kutta–Joukowski), Navier–Stokes, Poiseuille and Couette flow, Prandtl boundary layer, flow separation, drag crisis, compressible flow and shocks.

**Core ideas.**
- Inviscid theory predicts zero drag (d'Alembert's paradox); thin viscous boundary layers resolve it.
- Bernoulli holds along streamlines of steady, inviscid, incompressible flow — not "equal transit time" for lift.
- Vortex stretching is how 3D flows transfer energy to small scales.

**Key equations.**
$$p+\tfrac12\rho v^2+\rho gz=\text{const},\qquad Q=\frac{\pi R^4\Delta p}{8\mu L},\qquad \delta(x)\approx5\sqrt{\frac{\nu x}{U}}$$

**Landmark.** Reynolds (1883) — see [subfield landmarks](knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/README.md).

**See also.** [Turbulence](knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/turbulence/README.md) · [Dimensional analysis](knowledge/00-foundations/units-and-constants/dimensional-analysis-and-scaling/README.md)

### Instabilities and convection · `knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection`

**Scope.** Linear stability analysis, Rayleigh–Bénard convection and the critical Rayleigh number, Boussinesq approximation, Kelvin–Helmholtz (shear) instability, Rayleigh–Taylor (heavy over light), Plateau–Rayleigh jet breakup, Taylor–Couette flow, Saffman–Taylor fingering, convection in stars and planets.

**Core ideas.**
- Convection starts when buoyancy beats viscous and thermal diffusion: $Ra>Ra_c\approx1708$ (rigid boundaries).
- Rayleigh–Taylor mixing limits inertial-confinement fusion and shapes supernova remnants.
- Linear growth rates come from perturbations $\propto e^{ikx+\sigma t}$.

**Key equations.**
$$Ra=\frac{g\beta\Delta TL^3}{\nu\kappa},\qquad \sigma_{\text{RT}}=\sqrt{Agk},\ A=\frac{\rho_h-\rho_l}{\rho_h+\rho_l}$$

**Landmark.** Rayleigh (1916) — see [subfield landmarks](knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/README.md).

**See also.** [Inertial confinement fusion](knowledge/10-plasma-physics/inertial-and-laser-plasmas/inertial-confinement-fusion/README.md) · [Pattern formation](knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation/README.md)

### Low-Reynolds-number flow and microfluidics · `knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics`

**Scope.** Stokes equations and their reversibility, Stokes drag, scallop theorem, flagellar propulsion, hydrodynamic interactions between particles, lubrication theory, electrokinetics, droplet microfluidics, mixing at low Re, capillarity and wetting.

**Core ideas.**
- At $Re\ll1$ inertia is irrelevant: flow responds instantly and is time-reversible.
- Reciprocal strokes produce no net swimming (scallop theorem); microorganisms use rotating or travelling-wave flagella.
- Surface tension and viscosity dominate at small scales; mixing requires chaotic advection.

**Key equations.**
$$\mu\nabla^2\mathbf u=\nabla p,\qquad F_{\text{Stokes}}=6\pi\mu aU$$

**See also.** [Active matter](knowledge/08-condensed-matter/soft-matter/active-matter/README.md) · [Cellular biophysics](knowledge/11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics/README.md)

### Turbulence · `knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/turbulence`

**Scope.** Transition to turbulence (pipe flow, puffs and slugs), Richardson cascade, Kolmogorov 1941 scaling and the −5/3 spectrum, dissipation range, intermittency and anomalous scaling, 2D inverse cascade, wall turbulence and the log law, RANS and LES modelling, DNS, Lagrangian turbulence, ML closures.

**Core ideas.**
- Energy injected at large scales cascades to small scales and is dissipated at the Kolmogorov scale $\eta=(\nu^3/\epsilon)^{1/4}$.
- K41 predicts $E(k)=C\epsilon^{2/3}k^{-5/3}$; higher-order structure functions deviate (intermittency).
- In 2D, energy cascades to large scales — relevant for atmospheres and soap films.

**Key equations.**
$$E(k)=C_K\epsilon^{2/3}k^{-5/3},\qquad \frac{L}{\eta}\sim Re^{3/4},\qquad \frac{\bar u}{u_\tau}=\frac1\kappa\ln\frac{yu_\tau}{\nu}+B$$

**Landmark.** Kolmogorov (1941) — see [subfield landmarks](knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/README.md).

**See also.** [MHD turbulence](knowledge/10-plasma-physics/magnetohydrodynamics/mhd-turbulence/README.md) · [Deterministic chaos](knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos/README.md)

## Newtonian mechanics · `knowledge/01-classical-mechanics/newtonian-mechanics`

#### Overview
Newton's three laws plus a force law (gravity, springs, friction, Lorentz force) predict the motion of everything from projectiles to planets. Conservation laws often give answers without solving the equations of motion, and the two-body problem reduces exactly to a one-body problem in a central potential.

#### Conceptual spine
1. Inertial frames + $\mathbf F_{\text{net}}=d\mathbf p/dt$.
2. Work–energy theorem; conservative forces have potentials $\mathbf F=-\nabla V$.
3. Isolated systems conserve total momentum; central forces conserve angular momentum.
4. Two-body problem → reduced mass $\mu=m_1m_2/(m_1+m_2)$ in a central potential.

#### Key equations
$$\mathbf F=\frac{d\mathbf p}{dt},\qquad E=\tfrac12\mu\dot r^2+\frac{L^2}{2\mu r^2}+V(r),\qquad r(\theta)=\frac{a(1-e^2)}{1+e\cos\theta},\quad T^2=\frac{4\pi^2a^3}{G(m_1+m_2)}$$

#### Open problems
- Long-term stability of the Solar System (chaotic on ~5 Myr Lyapunov times; Laskar).
- Classification of periodic orbits in the general three-body problem.

#### Connections
- [Analytical mechanics](knowledge/01-classical-mechanics/analytical-mechanics/README.md) · [Noether's theorem](knowledge/00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws/README.md) · [Special relativity](knowledge/05-relativity-and-gravitation/special-relativity/README.md)

### Central forces and orbits · `knowledge/01-classical-mechanics/newtonian-mechanics/central-forces-and-orbits`

**Scope.** Reduced mass, effective potential, Binet equation, conic-section orbits, Kepler's laws, Laplace–Runge–Lenz vector, Bertrand's theorem, apsidal precession, Hohmann transfers and gravity assists, Rutherford scattering cross section.

**Core ideas.**
- Angular momentum conservation confines motion to a plane and gives Kepler's second law.
- Only $1/r$ and $r^2$ potentials have all bound orbits closed (Bertrand) — perturbations cause precession.
- Mercury's anomalous 43″/century perihelion advance was the first test of GR.

**Key equations.**
$$\frac{d^2u}{d\theta^2}+u=-\frac{\mu}{L^2u^2}F(1/u),\ u=\frac1r;\qquad \frac{d\sigma}{d\Omega}=\left(\frac{kq_1q_2}{4E}\right)^2\frac{1}{\sin^4(\theta/2)}$$

**See also.** [Tests of general relativity](knowledge/05-relativity-and-gravitation/general-relativity/tests-of-general-relativity/README.md) · [Solar-system dynamics](knowledge/09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics/README.md)

### Conservation laws · `knowledge/01-classical-mechanics/newtonian-mechanics/conservation-laws`

**Scope.** Work–energy theorem, conservative forces and potential energy, power, impulse, centre of mass, elastic and inelastic collisions, coefficient of restitution, angular momentum and torque, virial theorem.

**Core ideas.**
- Momentum is conserved in every collision of an isolated system; kinetic energy only in elastic ones.
- Analyse collisions in the centre-of-mass frame, then transform back.
- Virial theorem for bound $V\propto r^n$ systems: $2\langle T\rangle=n\langle V\rangle$ — used for galaxy-cluster masses.

**Key equations.**
$$W=\Delta T,\qquad \boldsymbol\tau=\frac{d\mathbf L}{dt},\qquad v_1'=\frac{m_1-m_2}{m_1+m_2}v_1\ (\text{1D elastic, target at rest})$$

**See also.** [Noether's theorem](knowledge/00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws/README.md) · [Galaxy clusters](knowledge/09-astrophysics-and-cosmology/galaxies/galaxy-clusters/README.md)

### Few-body and celestial mechanics · `knowledge/01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics`

**Scope.** Restricted three-body problem, Jacobi constant, Lagrange points L1–L5 and their stability, Poincaré's non-integrability, choreographies (figure-eight orbit), mean-motion resonances, secular perturbation theory, symplectic N-body integrators, Solar-System chaos.

**Core ideas.**
- The general three-body problem has no closed-form solution and generically shows chaos (Poincaré, 1890).
- L4/L5 are stable when the mass ratio is below ~1/25 (Trojan asteroids, JWST is at L2 — unstable, station-kept).
- Resonances shape planetary systems: Kirkwood gaps, Laplace resonance of Io–Europa–Ganymede.

**Key equations.**
$$C_J=n^2(x^2+y^2)+2\left(\frac{\mu_1}{r_1}+\frac{\mu_2}{r_2}\right)-(\dot x^2+\dot y^2+\dot z^2)$$

**Landmark.** Chenciner & Montgomery (2000) — see [subfield landmarks](knowledge/01-classical-mechanics/newtonian-mechanics/README.md).

**See also.** [KAM theory](knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos/README.md) · [Numerical methods](knowledge/00-foundations/computational-physics/numerical-methods-for-odes-and-pdes/README.md)

### Non-inertial frames · `knowledge/01-classical-mechanics/newtonian-mechanics/non-inertial-frames`

**Scope.** Linearly accelerating frames, rotating frames, centrifugal, Coriolis and Euler forces, Foucault pendulum, deflection of projectiles, weather systems and geostrophic balance, tidal forces, the equivalence principle as a bridge to GR.

**Core ideas.**
- In a frame rotating at $\boldsymbol\omega$, $d/dt|_{\text{in}}=d/dt|_{\text{rot}}+\boldsymbol\omega\times$.
- Coriolis force deflects moving bodies (right in the Northern Hemisphere) and organizes cyclones.
- Tides come from the gradient of gravity across a body, not gravity itself.

**Key equations.**
$$m\ddot{\mathbf r}=\mathbf F-2m\boldsymbol\omega\times\dot{\mathbf r}-m\boldsymbol\omega\times(\boldsymbol\omega\times\mathbf r)-m\dot{\boldsymbol\omega}\times\mathbf r,\qquad \Omega_{\text{Foucault}}=\Omega_\oplus\sin\lambda$$

**See also.** [Atmospheric dynamics](knowledge/11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics/README.md) · [Equivalence principle](knowledge/05-relativity-and-gravitation/general-relativity/tests-of-general-relativity/README.md)

## Nonlinear dynamics and chaos · `knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos`

#### Overview
Deterministic systems with as few as three variables can be unpredictable in practice because of exponential sensitivity to initial conditions. Nonlinear dynamics classifies how systems change behaviour as parameters vary (bifurcations), how order survives in Hamiltonian systems (KAM), how nonlinearity can stabilize waves (solitons), and how coupled units synchronize or form patterns.

#### Conceptual spine
1. Phase-space flows; fixed points and linear stability (eigenvalues of the Jacobian).
2. Bifurcations change the qualitative structure as parameters cross critical values.
3. Chaos: positive Lyapunov exponent, bounded attractor, fractal structure.
4. Dissipative (attractors) vs. conservative (KAM, mixed phase space) dynamics.

#### Key equations
$$\dot x=\sigma(y-x),\ \dot y=x(\rho-z)-y,\ \dot z=xy-\beta z;\qquad x_{n+1}=rx_n(1-x_n);\qquad \lambda=\lim_{t\to\infty}\frac1t\ln\frac{|\delta\mathbf x(t)|}{|\delta\mathbf x_0|}$$

#### Open problems
- Predictability limits of weather and climate; data-driven forecasting of chaotic systems.
- Arnold diffusion rates in realistic many-dimensional Hamiltonian systems.

#### Connections
- [Quantum chaos](knowledge/04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling/README.md) · [Turbulence](knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/turbulence/README.md) · [Complex networks](knowledge/03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/complex-networks/README.md)

### Bifurcations and routes to chaos · `knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/bifurcations-and-routes-to-chaos`

**Scope.** Normal forms, saddle-node, transcritical, pitchfork and Hopf bifurcations, hysteresis, period-doubling cascade, Feigenbaum constants, intermittency (Pomeau–Manneville), quasiperiodic route (Ruelle–Takens–Newhouse), tipping points in climate and ecology.

**Core ideas.**
- Near a bifurcation, dynamics reduce to a universal low-dimensional normal form.
- Period-doubling cascades in any unimodal map converge geometrically with $\delta=4.669\ldots$ — a renormalization-group universality.
- Critical slowing down precedes saddle-node "tipping points".

**Key equations.**
$$\delta=\lim_{n\to\infty}\frac{r_n-r_{n-1}}{r_{n+1}-r_n}=4.6692\ldots,\qquad \alpha=2.5029\ldots$$

**See also.** [Renormalization group](knowledge/03-thermodynamics-and-statistical-mechanics/phase-transitions-and-critical-phenomena/renormalization-group/README.md) · [Climate physics](knowledge/11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing/README.md)

### Deterministic chaos · `knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos`

**Scope.** Lorenz system, logistic map, double pendulum, Lyapunov spectra, strange attractors and fractal dimensions, Poincaré sections, symbolic dynamics, ergodicity and mixing, shadowing, time-series embedding (Takens), chaos control.

**Core ideas.**
- Chaos needs nonlinearity and at least three dimensions for continuous flows (one for maps).
- Errors grow like $e^{\lambda t}$, so the prediction horizon grows only logarithmically with initial precision.
- Strange attractors are fractal sets with zero volume but infinite length of trajectories.

**Key equations.**
$$t_{\text{pred}}\approx\frac{1}{\lambda_{\max}}\ln\frac{\Delta_{\text{tol}}}{\delta_0},\qquad D_{KY}=k+\frac{\sum_{i\le k}\lambda_i}{|\lambda_{k+1}|}$$

**See also.** [Quantum chaos](knowledge/04-quantum-physics/open-and-many-body-quantum-dynamics/quantum-chaos-and-scrambling/README.md) · [Atmospheric dynamics](knowledge/11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics/README.md)

### KAM theory and Hamiltonian chaos · `knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos`

**Scope.** Near-integrable Hamiltonians, the KAM theorem (Kolmogorov 1954, Arnold 1963, Moser 1962), Poincaré–Birkhoff theorem, resonance islands and chaotic seas, Chirikov standard map and resonance overlap, Hénon–Heiles, Arnold diffusion, stability of the Solar System, particle accelerator dynamic aperture.

**Core ideas.**
- Most invariant tori with sufficiently irrational frequency ratios survive small perturbations.
- Resonant tori break into island chains with chaotic layers; chaos spreads as perturbation grows (Chirikov criterion).
- In ≥3 degrees of freedom, tori don't separate phase space — slow Arnold diffusion is possible.

**Key equations.**
$$p_{n+1}=p_n+K\sin\theta_n,\ \theta_{n+1}=\theta_n+p_{n+1}\ (\text{standard map; global chaos for }K\gtrsim0.97)$$

**Landmark.** Hénon & Heiles (1964) — see [subfield landmarks](knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/README.md).

**See also.** [Beam dynamics](knowledge/11-interdisciplinary-physics/accelerator-physics/beam-dynamics/README.md) · [Few-body mechanics](knowledge/01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics/README.md)

### Solitons and integrable systems · `knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems`

**Scope.** Korteweg–de Vries, nonlinear Schrödinger and sine-Gordon equations, inverse scattering transform, Lax pairs, infinitely many conservation laws, optical solitons in fibres, solitons in BECs, rogue waves, topological solitons (kinks, vortices).

**Core ideas.**
- Solitons balance dispersion against nonlinearity, keeping their shape.
- Integrable PDEs are linearized by inverse scattering — the nonlinear analogue of Fourier transforms.
- Soliton collisions only shift phases; identity is preserved.

**Key equations.**
$$u_t+6uu_x+u_{xxx}=0,\qquad u(x,t)=\frac c2\,\mathrm{sech}^2\!\left[\frac{\sqrt c}{2}(x-ct-x_0)\right]$$

**See also.** [Nonlinear optics](knowledge/02-electromagnetism-and-optics/photonics-and-lasers/nonlinear-optics/README.md) · [Exactly solvable models](knowledge/03-thermodynamics-and-statistical-mechanics/equilibrium-statistical-mechanics/exactly-solvable-models/README.md)

### Synchronization and pattern formation · `knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation`

**Scope.** Phase oscillators and the Kuramoto model, Huygens' clocks, firefly and neuronal synchrony, chimera states, Turing instability, reaction–diffusion (Belousov–Zhabotinsky), Swift–Hohenberg equation, amplitude equations, convection rolls, spiral waves.

**Core ideas.**
- Coupled oscillators with spread frequencies synchronize above a critical coupling $K_c=2/(\pi g(0))$.
- Diffusion can destabilize a uniform state if an inhibitor diffuses faster than an activator (Turing).
- Near onset, patterns obey universal amplitude equations (Ginzburg–Landau type).

**Key equations.**
$$\dot\theta_i=\omega_i+\frac KN\sum_j\sin(\theta_j-\theta_i),\qquad re^{i\psi}=\frac1N\sum_je^{i\theta_j}$$

**See also.** [Active matter](knowledge/08-condensed-matter/soft-matter/active-matter/README.md) · [Convection](knowledge/01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection/README.md)

## Oscillations and waves · `knowledge/01-classical-mechanics/oscillations-and-waves`

#### Overview
Near any stable equilibrium, motion is approximately harmonic — which is why the harmonic oscillator appears in every branch of physics. Coupled oscillators have normal modes; in the continuum limit they become waves governed by the wave equation, with dispersion, reflection, interference and resonance.

#### Key equations
$$\ddot x+2\gamma\dot x+\omega_0^2x=\frac{F_0}{m}\cos\omega t,\qquad A(\omega)=\frac{F_0/m}{\sqrt{(\omega_0^2-\omega^2)^2+4\gamma^2\omega^2}},\qquad \frac{\partial^2u}{\partial t^2}=v^2\nabla^2u$$

#### Open problems
- Energy harvesting and vibration control with nonlinear and metamaterial resonators.

#### Connections
- [Phonons](knowledge/08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics/README.md) · [Electromagnetic waves](knowledge/02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides/README.md) · [Quantum harmonic oscillator](knowledge/04-quantum-physics/quantum-mechanics-core/exactly-solvable-systems/README.md)

### Coupled oscillators and normal modes · `knowledge/01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes`

**Scope.** Small-oscillation theory with mass and stiffness matrices, generalized eigenvalue problem, normal coordinates, beats and energy exchange, monatomic and diatomic chains, dispersion relations, acoustic and optical branches, Fermi–Pasta–Ulam–Tsingou recurrence.

**Core ideas.**
- $\mathsf M\ddot{\mathbf q}+\mathsf K\mathbf q=0$ → modes from $\det(\mathsf K-\omega^2\mathsf M)=0$; any motion is a superposition of modes.
- A chain of $N$ masses has $N$ modes; as $N\to\infty$ they become waves with $\omega(k)$.
- FPUT showed that weak nonlinearity need not thermalize quickly — a seed of soliton theory.

**Key equations.**
$$\omega(k)=2\sqrt{\frac{K}{m}}\left|\sin\frac{ka}{2}\right|\quad(\text{monatomic chain})$$

**See also.** [Phonons](knowledge/08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics/README.md) · [Solitons](knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems/README.md)

### Harmonic and damped oscillators · `knowledge/01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators`

**Scope.** Simple harmonic motion, pendulum (small-angle and exact period), energy in oscillators, under-, critically and over-damped motion, driven oscillators, resonance, phase lag, Q factor and linewidth, transients, Green's function of the oscillator, RLC circuit analogue.

**Core ideas.**
- Small oscillations about any minimum have $\omega^2=V''(x_0)/m$.
- $Q=\omega_0/(2\gamma)$: number of radians for energy to drop by $1/e$; resonance FWHM $\approx\omega_0/Q$.
- At resonance the response lags the drive by $\pi/2$ and power absorption peaks.

**Key equations.**
$$x(t)=Ae^{-\gamma t}\cos(\omega_dt+\phi),\ \omega_d=\sqrt{\omega_0^2-\gamma^2};\qquad T_{\text{pend}}\approx2\pi\sqrt{\frac Lg}\left(1+\frac{\theta_0^2}{16}\right)$$

**See also.** [Cavity optomechanics](knowledge/04-quantum-physics/quantum-optics/cavity-optomechanics/README.md) · [Coupled oscillators](knowledge/01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes/README.md)

### Mechanical waves and acoustics · `knowledge/01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics`

**Scope.** Wave equation on strings and in fluids/solids, standing waves and harmonics, phase and group velocity, dispersion, impedance and reflection coefficients, sound speed and intensity (dB), Doppler effect and shock waves (Mach cones), room and musical acoustics, ultrasound, acoustic metamaterials.

**Core ideas.**
- Wave speed is set by restoring stiffness over inertia: $v=\sqrt{T/\mu}$ (string), $v=\sqrt{B/\rho}$ (fluid).
- At an interface, impedance mismatch sets reflection; matching layers minimize it (ultrasound gel).
- Group velocity $d\omega/dk$ carries energy; it differs from phase velocity in dispersive media.

**Key equations.**
$$v_{\text{sound}}=\sqrt{\frac{\gamma RT}{M}},\qquad R=\left(\frac{Z_2-Z_1}{Z_2+Z_1}\right)^2,\qquad f'=f\frac{v+v_o}{v-v_s}$$

**See also.** [Medical ultrasound](knowledge/11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics/README.md) · [Seismology](knowledge/11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior/README.md)

### Parametric and nonlinear oscillations · `knowledge/01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations`

**Scope.** Parametric resonance (swings, Faraday waves), Mathieu equation and stability tongues, Kapitza's inverted pendulum, Duffing oscillator (hysteresis, jump phenomena), Van der Pol limit cycles and relaxation oscillations, Poincaré–Lindstedt and multiple-scales methods.

**Core ideas.**
- Modulating a parameter at twice the natural frequency pumps energy exponentially (parametric instability).
- Fast vertical driving can stabilize the inverted pendulum (effective potential).
- Nonlinearity makes frequency amplitude-dependent and allows self-sustained limit cycles.

**Key equations.**
$$\ddot x+\omega_0^2[1+h\cos(2\omega_0t)]x=0,\qquad \ddot x-\mu(1-x^2)\dot x+x=0\ (\text{Van der Pol})$$

**See also.** [Floquet systems](knowledge/04-quantum-physics/open-and-many-body-quantum-dynamics/floquet-systems-and-time-crystals/README.md) · [Bifurcations](knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/bifurcations-and-routes-to-chaos/README.md)

## Rigid-body dynamics · `knowledge/01-classical-mechanics/rigid-body-dynamics`

#### Overview
A rigid body has six degrees of freedom: three for its centre of mass and three for orientation. Rotational dynamics is governed by the inertia tensor, and because angular velocity and angular momentum need not be parallel, rotation shows surprising behaviour: wobbling free rotation, the tennis-racket (Dzhanibekov) instability, gyroscopic precession and nutation.

#### Key equations
$$\mathbf L=\mathsf I\boldsymbol\omega,\qquad I_{ij}=\int\rho\,(r^2\delta_{ij}-x_ix_j)\,dV,\qquad I_1\dot\omega_1-(I_2-I_3)\omega_2\omega_3=\tau_1$$

#### Open problems
- Rigid-body control and attitude dynamics of spacecraft; rattleback and other nonholonomic puzzles.

#### Connections
- [Analytical mechanics](knowledge/01-classical-mechanics/analytical-mechanics/README.md) · [Lie groups (SO(3))](knowledge/00-foundations/symmetry-and-group-theory/lie-groups-and-representations/README.md)

### Euler's equations and tops · `knowledge/01-classical-mechanics/rigid-body-dynamics/euler-equations-and-tops`

**Scope.** Euler's equations in the body frame, Euler angles, torque-free symmetric top and free precession (Chandler wobble), Poinsot construction, stability about principal axes (tennis-racket theorem), heavy symmetric top: precession and nutation, sleeping top.

**Core ideas.**
- Rotation about the axes of largest and smallest moment is stable; about the intermediate axis it is unstable.
- A torque-free symmetric body's $\boldsymbol\omega$ precesses about its symmetry axis in the body frame.
- The heavy top has three integrals ($E$, $L_z$, $L_3$) and is integrable.

**Key equations.**
$$\Omega_{\text{free}}=\frac{I_3-I_1}{I_1}\omega_3,\qquad \Omega_{\text{prec}}\approx\frac{Mg\ell}{I_3\omega_3}\ (\text{fast top})$$

**See also.** [Gyroscopes and precession](knowledge/01-classical-mechanics/rigid-body-dynamics/gyroscopes-and-precession/README.md) · [Bifurcations](knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/bifurcations-and-routes-to-chaos/README.md)

### Gyroscopes and precession · `knowledge/01-classical-mechanics/rigid-body-dynamics/gyroscopes-and-precession`

**Scope.** Gyroscopic precession under torque, nutation, gyrocompasses, ring-laser and MEMS gyroscopes, bicycle and spinning-projectile stability, precession of Earth's axis (26 000-year cycle), relativistic precession (Thomas, geodetic, frame dragging — Gravity Probe B).

**Core ideas.**
- Torque changes $\mathbf L$ perpendicular to itself → precession rather than falling.
- Earth's equatorial bulge plus lunar/solar torques give the precession of the equinoxes.
- In GR, gyroscopes precess due to spacetime curvature (geodetic) and rotation (Lense–Thirring).

**Key equations.**
$$\boldsymbol\tau=\boldsymbol\Omega\times\mathbf L,\qquad \Omega_{\text{geodetic}}=\frac32\frac{(GM)^{3/2}}{c^2r^{5/2}}$$

**See also.** [Tests of general relativity](knowledge/05-relativity-and-gravitation/general-relativity/tests-of-general-relativity/README.md)

### Rotational dynamics and the inertia tensor · `knowledge/01-classical-mechanics/rigid-body-dynamics/rotational-dynamics-and-inertia-tensor`

**Scope.** Fixed-axis rotation, torque and angular acceleration, moments of inertia of standard bodies, parallel- and perpendicular-axis theorems, inertia tensor and principal axes, rotational kinetic energy, rolling without slipping.

**Core ideas.**
- The inertia tensor is symmetric, so there is always an orthogonal set of principal axes.
- Rolling without slipping: $v=\omega R$; kinetic energy splits into translational and rotational parts.
- A body rolling down an incline is slowed by its rotational inertia factor $I/(MR^2)$.

**Key equations.**
$$T=\tfrac12\boldsymbol\omega^{T}\mathsf I\boldsymbol\omega,\qquad I=I_{\text{cm}}+Md^2,\qquad a_{\text{roll}}=\frac{g\sin\theta}{1+I/MR^2}$$

**See also.** [Euler's equations](knowledge/01-classical-mechanics/rigid-body-dynamics/euler-equations-and-tops/README.md)


---

# Packet 01-4 (100 records)

{"id": "C0712", "a": "01-classical-mechanics/analytical-mechanics/variational-principles", "b": "07-nuclear-physics/nuclear-structure/ab-initio-nuclear-theory", "name": "Rayleigh–Ritz: from vibrating plates to nuclei", "kind": "method transfer", "summary": "The variational bound used throughout ab initio nuclear theory (variational Monte Carlo, truncated-basis no-core shell model, Hartree–Fock references) descends from Rayleigh's quotient for the frequencies of vibrating systems and Ritz's 1909 method for elastic plates. The quantum Rayleigh–Ritz principle is the same eigenvalue minimization.", "map": "\\omega_0^2\\le\\frac{\\mathbf x^{T}K\\mathbf x}{\\mathbf x^{T}M\\mathbf x}\\ \\leftrightarrow\\ E_0\\le\\frac{\\langle\\psi|H|\\psi\\rangle}{\\langle\\psi|\\psi\\rangle}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0713", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "07-nuclear-physics/hadron-and-nucleon-structure/nucleon-spin-and-form-factors", "name": "Pressure and shear inside the proton", "kind": "analogy", "summary": "The gravitational form factors of the energy–momentum tensor (including the D-term) are read as a continuum-mechanics stress tensor: a radial pressure p(r) and shear force s(r) inside the proton, with von Laue's equilibrium condition ∫p r² dr = 0 and a mechanical radius. First extractions came from deeply virtual Compton scattering, and the EIC will map them.", "map": "T^{ij}(\\mathbf r)=s(r)\\left(\\hat r^i\\hat r^j-\\tfrac13\\delta^{ij}\\right)+p(r)\\delta^{ij},\\ \\int_0^\\infty r^2p(r)\\,dr=0", "breaks": "Local 3D densities of a relativistic, recoiling bound state depend on the frame (Breit frame vs light front), and whether p(r) is a physical pressure is debated.", "confidence": "current research", "strength": 2}
{"id": "C0714", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "name": "Love numbers: from Earth tides to Lambda", "kind": "historical", "summary": "The tidal deformability measured from GW170817's inspiral phase is built on the Love number k_2, which A. E. H. Love introduced for the elastic tidal response of the Earth. For a neutron star k_2 measures how centrally condensed the fluid is, so the measurement bounds EOS stiffness and radius.", "map": "Q_{ij}=-\\lambda\\mathcal E_{ij},\\ \\lambda=\\frac{2k_2R^5}{3G},\\ \\Lambda=\\frac23k_2\\left(\\frac{c^2R}{GM}\\right)^5", "breaks": "The neutron-star k_2 is a relativistic fluid response computed from perturbed TOV equations. Crust rigidity contributes negligibly, unlike the Earth's elastic Love numbers.", "confidence": "established", "strength": 2}
{"id": "C0715", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "name": "Neutron-star crust as an elastic solid", "kind": "shared object", "summary": "The neutron-star crust is a Coulomb crystal whose shear modulus is set by the nuclear charges and lattice spacing. Its elastic response governs starquakes and crust breaking, the largest 'mountain' that could radiate continuous gravitational waves, and the torsional shear modes proposed for magnetar-flare QPOs.", "map": "\\mu\\approx0.12\\,\\frac{n_N(Ze)^2}{4\\pi\\epsilon_0a},\\ \\omega_\\ell\\approx\\sqrt{(\\ell-1)(\\ell+2)}\\,\\frac{\\sqrt{\\mu/\\rho}}{R}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0716", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "07-nuclear-physics/heavy-ion-physics/collective-flow-and-hydrodynamics", "name": "Heavy-ion fireballs as relativistic viscous fluids", "kind": "method transfer", "summary": "Navier–Stokes hydrodynamics, made relativistic and causal (Israel–Stewart, second order), is the standard model of the heavy-ion fireball: pressure gradients turn the almond-shaped overlap into elliptic flow v_2, and fits to v_n extract the shear viscosity much as viscous damping is measured in a classical flow. Bjorken's boost-invariant expansion is an exact similarity solution of these equations.", "map": "\\partial_t(\\rho v_i)+\\partial_j\\Pi_{ij}=0\\leftrightarrow\\partial_\\mu T^{\\mu\\nu}=0;\\ \\eta(\\partial_iv_j+\\partial_jv_i)\\leftrightarrow\\pi^{\\mu\\nu}=2\\eta\\sigma^{\\mu\\nu}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0717", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "07-nuclear-physics/heavy-ion-physics/qcd-phase-diagram-and-critical-point", "name": "QCD critical point in the liquid–gas dynamic class", "kind": "identity", "summary": "Near the conjectured QCD critical point the slow modes are diffusive baryon density coupled to shear flow, exactly as at a liquid–gas critical point. That places it in Hohenberg–Halperin Model H, with the same critical slowing down, divergent conductivity and bulk-viscosity peak, and fluctuating hydrodynamics is used to predict the proton-cumulant signals.", "map": "\\tau_{\\rm relax}\\sim\\xi^{z},\\ z\\approx3\\ (\\text{Model H, as for a classical liquid–gas critical point})", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0718", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "name": "Perfect liquid: eta/s of the QGP vs ordinary fluids", "kind": "analogy", "summary": "Shear viscosity, defined by Newton's law of viscous stress, is compared across fluids through η/s, the relativistic analogue of kinematic viscosity. The QGP sits near ħ/4πk_B, about an order of magnitude below helium, nitrogen or water at their minima, which makes it the most nearly ideal (Euler) fluid known.", "map": "\\frac{\\eta}{s}\\approx\\frac{1}{4\\pi}\\frac{\\hbar}{k_B}\\ (\\text{QGP})\\ \\leftrightarrow\\ \\nu=\\eta/\\rho\\ (\\text{classical})", "breaks": "Kinetic theory gives η ∼ ρ v̄ λ (mean free path), which loses meaning at strong coupling where there are no quasiparticles. The 1/4π value is a holographic result for idealized gauge theories, not a proven lower bound.", "confidence": "established", "strength": 2}
{"id": "C0719", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-fission", "name": "Irrotational and viscous liquid-drop fission dynamics", "kind": "method transfer", "summary": "The descent from saddle to scission is modelled as flow of an incompressible nuclear fluid. Irrotational (Werner–Wheeler) flow gives the collective inertia, and adding two-body viscosity through Navier–Stokes (Davies–Sierk–Nix) slows the descent, stretches the neck and lowers fragment kinetic energies. Measured kinetic energies and prescission neutrons calibrate the dissipation.", "map": "M_{ij}(q)\\ \\text{from}\\ \\tfrac12\\rho\\int|\\nabla\\phi|^2dV,\\quad \\dot E_{\\rm diss}=\\tfrac{\\eta}{2}\\int(\\partial_iv_j+\\partial_jv_i)^2dV", "breaks": "Nuclear dissipation is mostly one-body (nucleons hitting the moving surface), not two-body viscosity, because the nucleon mean free path is comparable to the nuclear size.", "confidence": "established", "strength": 2}
{"id": "C0720", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "07-nuclear-physics/nuclear-astrophysics/stellar-nucleosynthesis-and-the-r-process", "name": "Convective mixing sets s- and i-process yields", "kind": "mechanism", "summary": "Neutron-capture nucleosynthesis depends on classical fluid instabilities. In AGB stars, partial mixing at convective boundaries forms the ¹³C pocket that powers the main s-process, convective-reactive ingestion of hydrogen into helium-burning zones drives the i-process, and in core-collapse supernovae Rayleigh–Taylor fingers carry fresh ⁵⁶Ni outward, as seen in SN 1987A.", "map": "N^2=\\frac{g}{H_P}(\\nabla_{\\rm ad}-\\nabla)<0\\Rightarrow\\text{convection},\\ \\sigma_{\\rm RT}=\\sqrt{\\mathcal A gk}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0721", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-fission", "name": "Fission as Rayleigh's charged-drop instability", "kind": "identity", "summary": "Bohr–Wheeler fission is Rayleigh's instability of a charged liquid drop: surface tension restores and Coulomb repulsion drives the quadrupole mode, and the sphere loses stability when E_C = 2E_S (fissility x = 1). Because the liquid-drop barrier vanishes for the heaviest nuclei, they survive only through shell corrections, and the final neck rupture parallels Rayleigh–Plateau pinch-off.", "map": "x=\\frac{E_C^{(0)}}{2E_S^{(0)}}\\approx\\frac{Z^2/A}{50}=1\\ \\leftrightarrow\\ Q_R^2=64\\pi^2\\epsilon_0\\sigma R^3\\ (\\text{Rayleigh, conducting drop})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0722", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics", "b": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "name": "Heavy quarks as Brownian particles in the QGP", "kind": "analogy", "summary": "Charm and bottom quarks (M ≫ T) random-walk through the QGP like colloids in a viscous liquid. A Langevin equation with drag and momentum diffusion, tied together by the Einstein relation, describes their thermalization, and the spatial diffusion coefficient extracted from heavy-flavour R_AA and v_2 is a key transport parameter.", "map": "\\frac{d\\mathbf p}{dt}=-\\gamma\\mathbf p+\\boldsymbol\\xi(t),\\ D_s=\\frac{k_BT}{M\\gamma}\\ \\leftrightarrow\\ D=\\frac{k_BT}{6\\pi\\eta a}", "breaks": "Stokes drag 6πηa assumes a continuum fluid around a large sphere. The heavy quark is pointlike, comparable to the medium's interparticle spacing, and its drag comes from colour interactions with relativistic corrections, not from viscous boundary layers.", "confidence": "established", "strength": 2}
{"id": "C0723", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "07-nuclear-physics/heavy-ion-physics/jet-quenching", "name": "Jet energy loss as a wave-turbulent gluon cascade", "kind": "analogy", "summary": "Medium-induced radiation from a jet in the QGP becomes a cascade of democratic gluon branchings. It carries energy at a constant rate from the leading parton to soft gluons and into the medium, with a Kolmogorov–Zakharov fixed-point spectrum, which explains why the lost energy reappears at large angles.", "map": "D(x)\\propto x^{-1/2}\\ (\\text{KZ fixed point})\\ \\leftrightarrow\\ E(k)\\propto k^{-5/3}", "breaks": "The cascade is in the energy fraction x of a branching process, not in a 3D velocity field. Its flux is set by \\hat q and the path length, and the inertial range ends at the medium temperature.", "confidence": "current research", "strength": 2}
{"id": "C0724", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "07-nuclear-physics/heavy-ion-physics/quark-gluon-plasma", "name": "Turbulent cascade in early QGP thermalization", "kind": "analogy", "summary": "Before hydrodynamics applies, the over-occupied gluon fields left by the collision thermalize through a self-similar, constant-flux energy cascade toward high momenta. This is a Kolmogorov–Zakharov-type wave turbulence (a non-thermal fixed point), the same idea as the Richardson–Kolmogorov cascade in fluids.", "map": "E(k)\\propto\\varepsilon^{2/3}k^{-5/3}\\ \\leftrightarrow\\ f(t,p)=t^{\\alpha}f_s(t^{\\beta}p)", "breaks": "The cascade runs in the momentum space of weakly coupled classical gluon fields. Its exponents come from the kinetic collision term, not K41's −5/3, and there are no spatial eddies and no Navier–Stokes nonlinearity.", "confidence": "current research", "strength": 2}
{"id": "C0725", "a": "01-classical-mechanics/newtonian-mechanics/central-forces-and-orbits", "b": "07-nuclear-physics/applied-nuclear-physics/radiation-detection-and-dosimetry", "name": "Bohr's classical stopping power", "kind": "method transfer", "summary": "Bohr's 1913 stopping theory is impulse-approximation Coulomb scattering: a fast ion passing an electron at impact parameter b gives it Δp = 2Ze²/(4πε0 b v). Integrating over b between a close-collision cutoff and the adiabatic cutoff v/ω gives the logarithmic energy loss that Bethe later made quantum, the basis of range–energy relations, Bragg peaks and detector response.", "map": "-\\frac{dE}{dx}=\\frac{4\\pi n_eZ^2e^4}{(4\\pi\\epsilon_0)^2m_ev^2}\\ln\\frac{b_{\\max}}{b_{\\min}},\\ b_{\\max}\\approx\\frac{v}{\\omega}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0726", "a": "01-classical-mechanics/newtonian-mechanics/central-forces-and-orbits", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "name": "Rutherford scattering: a hyperbolic orbit found the nucleus", "kind": "historical", "summary": "Geiger–Marsden α scattering was explained by classical hyperbolic orbits in a repulsive 1/r potential. Rutherford's cross section is also exact in quantum mechanics, deviations from it still show where the nuclear force begins (closest approach, Coulomb barrier), and for heavy ions with Sommerfeld parameter η ≫ 1 classical trajectories stay quantitative.", "map": "\\frac{d\\sigma}{d\\Omega}=\\left(\\frac{Z_1Z_2e^2}{16\\pi\\epsilon_0E}\\right)^2\\frac{1}{\\sin^4(\\theta/2)},\\ \\eta=\\frac{Z_1Z_2e^2}{4\\pi\\epsilon_0\\hbar v}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0727", "a": "01-classical-mechanics/newtonian-mechanics/central-forces-and-orbits", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Shell structure from closed classical orbits", "kind": "mechanism", "summary": "By Bertrand's theorem only the oscillator and Kepler potentials have every bound orbit closed, and that classical degeneracy is why the oscillator gives large shell gaps at 2, 8, 20, 40. In realistic wells, periodic-orbit theory (Balian–Bloch, Strutinsky, the Gutzwiller trace formula) writes the oscillating level density, the shell correction behind magic numbers and superheavy stability, as a sum over the shortest closed orbits.", "map": "\\delta g(E)=\\sum_{\\rm po}A_{\\rm po}\\cos\\left(\\frac{S_{\\rm po}}{\\hbar}-\\sigma_{\\rm po}\\frac\\pi2\\right),\\ S_{\\rm po}=\\oint\\mathbf p\\cdot d\\mathbf q", "breaks": "Spin–orbit coupling, essential for the magic numbers 28, 50, 82 and 126, needs spin-dependent extensions of the trace formula.", "confidence": "established", "strength": 2}
{"id": "C0728", "a": "01-classical-mechanics/newtonian-mechanics/conservation-laws", "b": "07-nuclear-physics/applied-nuclear-physics/nuclear-reactors-and-energy", "name": "Neutron moderation by elastic-collision kinematics", "kind": "identity", "summary": "Slowing fission neutrons to thermal energy is pure two-body elastic-collision kinematics. Momentum and energy conservation fix the maximum fractional energy loss on a nucleus of mass number A and the mean logarithmic decrement ξ, which is why light nuclei moderate best: about 18 collisions on hydrogen against about 115 on carbon to go from 2 MeV to 0.025 eV.", "map": "\\frac{E'_{\\min}}{E}=\\alpha=\\left(\\frac{A-1}{A+1}\\right)^2,\\ \\xi=1+\\frac{\\alpha\\ln\\alpha}{1-\\alpha},\\ n=\\frac{\\ln(E_0/E)}{\\xi}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0729", "a": "01-classical-mechanics/newtonian-mechanics/conservation-laws", "b": "07-nuclear-physics/nuclear-reactions-and-decays/beta-decay-and-weak-interactions", "name": "Neutrino invented to save conservation laws", "kind": "historical", "summary": "The continuous β spectrum, together with the spin–statistics bookkeeping of the nuclei, seemed to break conservation of energy and angular momentum, and Bohr considered giving up energy conservation. Pauli instead postulated a light neutral spin-½ particle, which Fermi built into his theory of β decay: a conservation law predicting a particle.", "map": "Q=T_e+T_{\\bar\\nu}+T_{\\rm rec},\\ \\textstyle\\sum\\mathbf p=0,\\ \\Delta J\\ \\text{balanced only with a spin-}\\tfrac12\\ \\bar\\nu", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0730", "a": "01-classical-mechanics/newtonian-mechanics/conservation-laws", "b": "07-nuclear-physics/nuclear-structure", "name": "Chadwick weighed the neutron with collision kinematics", "kind": "historical", "summary": "Chadwick identified the neutron by comparing the maximum recoil velocities of hydrogen and nitrogen nuclei struck by the unknown radiation. Head-on elastic-collision kinematics gave a neutral particle with about the proton's mass, and ruled out the γ-ray hypothesis, which needed implausibly high photon energies.", "map": "u_{\\max}=\\frac{2m}{m+M}v\\Rightarrow\\frac{u_H}{u_N}=\\frac{m+14m_p}{m+m_p}\\Rightarrow m\\approx m_p", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0731", "a": "01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics", "b": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "name": "Neutron-star masses from binary orbits", "kind": "method transfer", "summary": "Every neutron-star mass that constrains the EOS comes from binary celestial mechanics: Keplerian elements and the mass function, plus post-Keplerian effects (periastron advance, Shapiro delay) to break degeneracies. Demorest et al. used the Shapiro delay to measure a 2 M_⊙ pulsar, which rules out soft EOSs.", "map": "f(M)=\\frac{4\\pi^2(a_p\\sin i)^3}{GP_b^2}=\\frac{(M_c\\sin i)^3}{(M_p+M_c)^2}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0732", "a": "01-classical-mechanics/newtonian-mechanics/non-inertial-frames", "b": "07-nuclear-physics/heavy-ion-physics/collective-flow-and-hydrodynamics", "name": "Vortical fireball: spin polarization from rotation", "kind": "mechanism", "summary": "Off-central collisions carry enormous orbital angular momentum, and the fluid's thermal vorticity (about 10^22 s^-1, the most vortical fluid known) polarizes Λ hyperons along it. The equilibrium density matrix is the rotating-frame one, so spin aligns with ω as in the Barnett effect.", "map": "\\rho\\propto e^{-(H-\\boldsymbol\\omega\\cdot\\mathbf J)/k_BT},\\ P_\\Lambda\\approx\\frac{\\hbar\\omega}{2k_BT}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0733", "a": "01-classical-mechanics/newtonian-mechanics/non-inertial-frames", "b": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "name": "r-modes: Coriolis-restored waves that spin stars down", "kind": "mechanism", "summary": "The r-modes of a rotating star are Rossby waves with the Coriolis force as their restoring force. Gravitational radiation drives them unstable (Chandrasekhar–Friedman–Schutz) unless the shear and bulk viscosity of dense matter damp them, so the observed spins of fast pulsars constrain neutron-star viscosity and composition.", "map": "\\omega_{\\rm rot}=\\frac{2m\\Omega}{\\ell(\\ell+1)},\\ \\omega_{\\rm inertial}=-\\frac{(\\ell-1)(\\ell+2)}{\\ell(\\ell+1)}m\\Omega", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0734", "a": "01-classical-mechanics/newtonian-mechanics/non-inertial-frames", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Cranking model: nuclei in the rotating frame", "kind": "method transfer", "summary": "Inglis's cranking model solves the nucleon problem in a frame rotating at ω. Its Routhian H' = H − ωJ_x contains the Coriolis and centrifugal terms and yields moments of inertia, and the Coriolis force breaking high-j pairs and aligning their spins explains backbending in yrast bands.", "map": "H'=H-\\omega J_x,\\ \\mathcal I^{(1)}=\\frac{\\langle J_x\\rangle}{\\omega}\\ \\leftrightarrow\\ \\mathbf F_{\\rm Cor}=-2m\\boldsymbol\\Omega\\times\\mathbf v", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0735", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/bifurcations-and-routes-to-chaos", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-fission", "name": "Rotating-drop shape bifurcations (Maclaurin–Jacobi)", "kind": "analogy", "summary": "A rotating charged liquid drop follows the classical sequence of rotating fluid masses. Oblate axisymmetric shapes bifurcate into triaxial Jacobi-like shapes at a critical angular momentum, and the fission barrier vanishes at higher spin. Cohen, Plasil and Swiatecki mapped these sequences for nuclei, and a Jacobi shape transition has been reported in hot, fast-rotating nuclei through GDR splitting.", "map": "\\text{oblate}\\xrightarrow{L>L_{\\rm J}}\\text{triaxial (Jacobi)}\\xrightarrow{L>L_{\\rm II}}B_f\\to0", "breaks": "Surface tension replaces self-gravity, so the sequences differ quantitatively from the Maclaurin–Jacobi ones. Quantized angular momentum, shell effects (superdeformed bands) and pairing modify the classical drop.", "confidence": "established", "strength": 2}
{"id": "C0736", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-fission", "name": "Wall-formula dissipation needs chaotic nucleon billiards", "kind": "mechanism", "summary": "One-body dissipation treats nucleons as a gas bouncing inside a moving container (the wall-and-window formula of Błocki, Swiatecki and co-workers). Classical billiard simulations showed that the full wall-formula damping holds only when particle motion in the container shape is chaotic and is much weaker for integrable shapes, which ties fission damping to classical chaos.", "map": "\\dot E=\\rho\\bar v\\oint\\dot n^2\\,dS\\ (\\text{full strength only for chaotic billiards})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0737", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos", "b": "07-nuclear-physics/nuclear-reactions-and-decays/nuclear-reactions-and-scattering", "name": "Compound-nucleus resonances and quantum chaos", "kind": "historical", "summary": "Neutron-resonance spacings in compound nuclei (the Nuclear Data Ensemble) follow the Wigner–Dyson GOE statistics that Wigner introduced for nuclei. The Bohigas–Giannoni–Schmit conjecture ties such spectra to classically chaotic Hamiltonian dynamics, while regular (KAM-integrable) systems give Poisson statistics, so the 'forgetting' assumed by Bohr's compound nucleus and Hauser–Feshbach theory is an ergodicity statement.", "map": "P_{\\rm GOE}(s)\\approx\\frac{\\pi s}{2}e^{-\\pi s^2/4}\\ (\\text{chaotic})\\ \\text{vs}\\ P(s)=e^{-s}\\ (\\text{integrable})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0738", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "b": "07-nuclear-physics/nuclear-structure/nuclear-forces-and-chiral-eft", "name": "Skyrmions: baryons as topological solitons", "kind": "analogy", "summary": "In the Skyrme model, which the large-N_c limit of QCD motivates, the chiral pion Lagrangian supports stable topological solitons whose winding number is baryon number. Nucleons, nuclei and nuclear matter appear as classical field configurations quantized through their collective rotations, carrying the soliton idea from classical nonlinear waves into the strong force.", "map": "B=\\frac{1}{24\\pi^2}\\int d^3x\\,\\epsilon^{ijk}{\\rm Tr}(L_iL_jL_k)\\in\\mathbb Z,\\ L_i=U^\\dagger\\partial_iU", "breaks": "Skyrmions are topological solitons, not integrable ones: there is no inverse scattering and they deform when they interact. The model overbinds light nuclei and has been superseded quantitatively by chiral EFT.", "confidence": "established", "strength": 2}
{"id": "C0739", "a": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Surface vibrations: Rayleigh drop modes quantized", "kind": "analogy", "summary": "Quadrupole and octupole phonons in vibrational nuclei are the quantized normal modes of a charged liquid drop's surface, R(θ,φ) = R_0[1 + Σ α_λμ Y_λμ]. The restoring constant combines surface tension and Coulomb terms as in Rayleigh's capillary-oscillation analysis, which predicts two-phonon 0+, 2+, 4+ triplets near 2ħω.", "map": "C_\\lambda=(\\lambda-1)(\\lambda+2)R_0^2\\sigma-\\frac{3(\\lambda-1)}{2\\pi(2\\lambda+1)}\\frac{Z^2e^2}{4\\pi\\epsilon_0R_0}", "breaks": "Measured mass parameters exceed irrotational-flow values, many supposedly vibrational nuclei miss the harmonic two-phonon pattern, and shell structure rather than surface tension sets most low-lying collectivity.", "confidence": "established", "strength": 2}
{"id": "C0740", "a": "01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Superdeformation from 2:1 oscillator resonance", "kind": "mechanism", "summary": "In the deformed (Nilsson) oscillator, whenever ω_⊥:ω_z is a ratio of small integers the classical orbits close into Lissajous figures and the quantum levels bunch into degenerate shells. The 2:1 resonance produces the superdeformed magic numbers and 3:1 gives hyperdeformation, the same commensurability that makes classical oscillator orbits periodic.", "map": "E=\\hbar\\omega_\\perp(n_\\perp+1)+\\hbar\\omega_z(n_z+\\tfrac12),\\ \\omega_\\perp:\\omega_z=2:1\\Rightarrow\\text{degenerate shells}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0741", "a": "01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Giant resonances as acoustic modes of nucleon fluids", "kind": "analogy", "summary": "In the giant dipole resonance protons oscillate against neutrons. Goldhaber–Teller model it as two rigid spheres sloshing (E ∝ A^{-1/6}), Steinwedel–Jensen as a standing sound wave of isovector density in a fixed sphere (E ∝ A^{-1/3}), and the data interpolate between them; the isoscalar monopole breathing mode measures nuclear incompressibility.", "map": "E_{\\rm SJ}\\propto A^{-1/3},\\ E_{\\rm GT}\\propto A^{-1/6};\\ E_{\\rm GMR}=\\hbar\\sqrt{K_A/(m\\langle r^2\\rangle)}", "breaks": "Nuclear sound is zero sound of a Fermi liquid (Fermi-surface distortion at ωτ ≫ 1), not collisional first sound, and the resonances are Landau-damped into particle–hole states.", "confidence": "established", "strength": 2}
{"id": "C0742", "a": "01-classical-mechanics/rigid-body-dynamics/euler-equations-and-tops", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Wobbling: quantized precession of a triaxial top", "kind": "analogy", "summary": "A triaxial nucleus with three distinct moments of inertia is a quantum asymmetric top. Bohr–Mottelson wobbling is the quantized small-amplitude precession of the rotation axis about the axis of largest inertia, the stable branch of Euler's tennis-racket analysis, and wobbling bands have been seen in odd-A Lu isotopes.", "map": "\\omega_{\\rm wob}=\\omega_{\\rm rot}\\sqrt{\\frac{(\\mathcal I_1-\\mathcal I_2)(\\mathcal I_1-\\mathcal I_3)}{\\mathcal I_2\\mathcal I_3}}\\ \\leftrightarrow\\ \\text{Euler small-oscillation frequency}", "breaks": "The moment hierarchy is set by quantum (irrotational-like) flow. An aligned high-j quasiparticle (transverse wobbling) changes the classical stability criterion, and some wobbling assignments are disputed.", "confidence": "established", "strength": 2}
{"id": "C0743", "a": "01-classical-mechanics/rigid-body-dynamics/rotational-dynamics-and-inertia-tensor", "b": "07-nuclear-physics/nuclear-astrophysics/neutron-star-equation-of-state", "name": "Neutron-star moment of inertia and glitches", "kind": "shared object", "summary": "Pulsar spin-down, glitches and binary spin–orbit precession are rotational dynamics of a two-component body. A glitch transfers angular momentum from a superfluid component to the crust, so the crust's share of the moment of inertia constrains the EOS, and EOS-insensitive I–Love–Q relations tie the moment of inertia to tidal deformability and quadrupole.", "map": "I_c\\Delta\\Omega_c=-I_s\\Delta\\Omega_s,\\ \\frac{I_{\\rm crust}}{I}\\gtrsim0.014\\ (\\text{Vela}),\\ \\dot E_{\\rm rot}=I\\Omega\\dot\\Omega", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0744", "a": "01-classical-mechanics/rigid-body-dynamics/rotational-dynamics-and-inertia-tensor", "b": "07-nuclear-physics/nuclear-structure/shell-model-and-collective-models", "name": "Rotational bands: the quantized rotor and its inertia", "kind": "analogy", "summary": "Deformed nuclei show bands E_J = ħ²J(J+1)/2𝓘, the spectrum of a quantized free rotor with E(4+)/E(2+) = 10/3. The moment of inertia is the classical quantity, and its measured value, which lies between the irrotational-flow and rigid-body values, directly probes nuclear superfluidity.", "map": "E_J=\\frac{\\hbar^2}{2\\mathcal I}J(J+1)\\leftrightarrow T=\\frac{L^2}{2I},\\quad \\mathcal I_{\\rm irr}<\\mathcal I_{\\rm exp}<\\mathcal I_{\\rm rig}", "breaks": "There is no collective rotation about a symmetry axis (quantum indistinguishability). 𝓘 is far from rigid: pairing reduces it to roughly 30–50% of the rigid value, and it changes with spin (Coriolis anti-pairing, backbending).", "confidence": "established", "strength": 3}
{"id": "C0745", "a": "01-classical-mechanics/analytical-mechanics/canonical-transformations-and-hamilton-jacobi", "b": "08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons", "name": "Onsager quantization of cyclotron orbits", "kind": "identity", "summary": "Quantum oscillations follow from Bohr-Sommerfeld quantization of semiclassical cyclotron orbits on the Fermi surface: the action variable of the orbit fixes allowed k-space areas, so dHvA and SdH frequencies measure extremal Fermi-surface cross sections.", "map": "J=\\oint p\\,dq=2\\pi\\hbar(n+\\gamma)\\Rightarrow A_k=\\frac{2\\pi eB}{\\hbar}(n+\\gamma),\\ \\Delta(1/B)=\\frac{2\\pi e}{\\hbar A_F}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0746", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "Berry curvature deforms semiclassical phase space", "kind": "identity", "summary": "Semiclassical Bloch electrons with Berry curvature obey non-canonical Hamiltonian dynamics: the anomalous velocity appears and Liouville's phase-space volume is not conserved unless weighted by (1+e B.Omega/hbar), which corrects the density of states.", "map": "\\dot{\\mathbf r}=\\frac1\\hbar\\nabla_{\\mathbf k}E-\\dot{\\mathbf k}\\times\\boldsymbol\\Omega,\\ \\hbar\\dot{\\mathbf k}=-e(\\mathbf E+\\dot{\\mathbf r}\\times\\mathbf B);\\ D=1+\\frac e\\hbar\\mathbf B\\cdot\\boldsymbol\\Omega", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0747", "a": "01-classical-mechanics/continuum-and-fluid-mechanics", "b": "08-condensed-matter/soft-matter", "name": "Continuum mechanics of soft materials", "kind": "method transfer", "summary": "Soft matter is described at long wavelengths by continuum theories (viscoelastic fluids, gels, nematic hydrodynamics, granular rheology) built on the conservation laws and constitutive-relation framework of continuum mechanics.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0748", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "name": "Dislocations as topological defects of elastic crystals", "kind": "mechanism", "summary": "Plastic deformation of crystals proceeds by motion of dislocations, line defects labelled by a Burgers vector, whose long-range stress fields are solutions of continuum elasticity; their unbinding drives KTHNY two-dimensional melting.", "map": "\\oint d\\mathbf u=\\mathbf b;\\ \\sigma_{\\text{screw}}=\\frac{\\mu b}{2\\pi r};\\ \\tau_{\\text{Peierls}}\\ll\\mu/30\\ (\\text{ideal strength})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0749", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "Elastic waves as long-wavelength acoustic phonons", "kind": "identity", "summary": "Acoustic phonon branches at small k are the elastic waves of continuum elasticity: their slopes are the longitudinal and transverse sound speeds fixed by elastic constants, which phonon dispersion measurements determine.", "map": "\\omega=v_{L,T}k\\ (k\\to0),\\ v_L=\\sqrt{(\\lambda+2\\mu)/\\rho},\\ v_T=\\sqrt{\\mu/\\rho};\\ \\rho\\omega^2u_i=C_{ijkl}k_jk_lu_k", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0750", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "08-condensed-matter/soft-matter/colloids-and-granular-matter", "name": "Contact mechanics, force chains and the Janssen effect", "kind": "mechanism", "summary": "Static granular packs transmit stress through heterogeneous force chains between Hertzian contacts; frictional wall support saturates pressure with depth in silos (Janssen effect), so granular stress cannot be treated as hydrostatic.", "map": "F=\\tfrac43E^*\\sqrt{R^*}\\delta^{3/2}\\ (\\text{Hertz});\\ p(z)=p_\\infty(1-e^{-z/\\lambda}),\\ \\lambda=\\frac{R}{2\\mu_wK}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0751", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "08-condensed-matter/soft-matter/glasses-and-jamming", "name": "Maxwell counting and isostatic jamming", "kind": "historical", "summary": "Maxwell's 1864 constraint counting for the rigidity of frames gives the isostatic contact number z=2d at the jamming transition; above jamming, shear modulus and excess contacts grow as power laws of compression.", "map": "N_{\\text{zero}}=dN-\\tfrac12zN\\Rightarrow z_c=2d;\\ G\\sim(\\phi-\\phi_J)^{1/2},\\ z-z_c\\sim(\\phi-\\phi_J)^{1/2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0752", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "08-condensed-matter/soft-matter/liquid-crystals", "name": "Frank orientational elasticity and liquid-crystal elastomers", "kind": "analogy", "summary": "Frank theory is an elasticity for the director field (splay, twist, bend) instead of displacements; coupling it to a rubber network gives liquid-crystal elastomers with 'soft elasticity' and large reversible actuation.", "map": "F_{\\text{Frank}}=\\tfrac12K_1(\\nabla\\cdot\\mathbf n)^2+\\tfrac12K_2(\\mathbf n\\cdot\\nabla\\times\\mathbf n)^2+\\tfrac12K_3|\\mathbf n\\times\\nabla\\times\\mathbf n|^2\\leftrightarrow\\tfrac12C_{ijkl}\\epsilon_{ij}\\epsilon_{kl}", "breaks": "The director is a unit headless vector, so Frank elasticity has topological defects and no restoring force for uniform rotations; a fluid nematic has zero shear modulus, unlike a solid.", "confidence": "established", "strength": 2}
{"id": "C0753", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "08-condensed-matter/soft-matter/polymers", "name": "Rubber elasticity: entropic springs to neo-Hookean solids", "kind": "identity", "summary": "Each network strand is an entropic Gaussian spring, so averaging over strands gives the neo-Hookean strain-energy function of finite-strain continuum elasticity with shear modulus n k_B T, explaining why rubber stiffens on heating.", "map": "f=\\frac{3k_BT}{Nb^2}R\\Rightarrow W=\\tfrac12nk_BT(\\lambda_1^2+\\lambda_2^2+\\lambda_3^2-3),\\ G=nk_BT", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0754", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "Topological mechanics of isostatic lattices", "kind": "method transfer", "summary": "Band topology applied to the compatibility matrix of Maxwell (isostatic) lattices predicts floppy zero modes localized on particular edges, an index theorem for mechanical metamaterials analogous to the SSH chain.", "map": "N_0-N_S=dN-N_B;\\ \\text{topological polarization }\\mathbf R_T=\\sum_i n_i\\mathbf a_i\\ (\\text{winding of }\\det C(\\mathbf k))", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0755", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "08-condensed-matter/low-dimensional-and-quantum-materials/graphene-and-2d-materials", "name": "Electron hydrodynamics in graphene", "kind": "mechanism", "summary": "When electron-electron collisions dominate over impurity and phonon scattering, electrons in clean graphene flow as a viscous fluid obeying Navier-Stokes-like equations, producing negative nonlocal resistance from backflow whirlpools and Poiseuille profiles.", "map": "\\eta\\nabla^2\\mathbf u-\\frac{m}{\\tau}\\mathbf u=\\nabla p+ne\\mathbf E;\\ \\ell_{ee}\\ll W\\ll\\ell_{mr},\\ \\nu=v_F\\ell_{ee}/4", "breaks": "", "confidence": "current research", "strength": 3}
{"id": "C0756", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "08-condensed-matter/soft-matter/colloids-and-granular-matter", "name": "mu(I) rheology: granular matter as a viscoplastic fluid", "kind": "method transfer", "summary": "Dense granular flows obey a local friction law in which the effective friction depends on the inertial number; inserted into continuum momentum equations it predicts flows on inclines, in silos and in rotating drums.", "map": "\\tau=\\mu(I)P,\\ \\mu(I)=\\mu_s+\\frac{\\mu_2-\\mu_s}{1+I_0/I},\\ I=\\frac{\\dot\\gamma d}{\\sqrt{P/\\rho_s}}\\Rightarrow\\eta_{\\text{eff}}=\\frac{\\mu(I)P}{\\dot\\gamma}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0757", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "08-condensed-matter/soft-matter/liquid-crystals", "name": "Nematodynamics: anisotropic viscous flow", "kind": "mechanism", "summary": "Ericksen-Leslie theory couples the Navier-Stokes equations to director rotation, giving three Miesowicz viscosities, flow alignment and backflow; it controls display switching times and active-nematic hydrodynamics.", "map": "\\sigma_{ij}=-p\\delta_{ij}+\\alpha_1n_in_jn_kn_lA_{kl}+\\alpha_2n_iN_j+\\ldots+\\alpha_4A_{ij}+\\ldots;\\ \\gamma_1\\dot{\\mathbf n}=\\mathbf h-\\gamma_2\\mathsf A\\mathbf n", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0758", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "08-condensed-matter/soft-matter/liquid-crystals", "name": "Electroconvection in nematics", "kind": "mechanism", "summary": "Above a threshold voltage nematic layers develop convection rolls (Williams domains) through the Carr-Helfrich mechanism, an anisotropic analogue of Rayleigh-Benard convection and a classic system for pattern formation and spatiotemporal chaos.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0759", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics", "b": "08-condensed-matter/soft-matter", "name": "Colloids, polymers and swimmers in Stokes flow", "kind": "mechanism", "summary": "Soft-matter dynamics is overdamped: colloid diffusion, polymer Rouse-Zimm dynamics and microswimming are governed by Stokes drag and long-range hydrodynamic interactions (Oseen tensor).", "map": "\\mathbf F=6\\pi\\mu a\\mathbf U,\\ \\mathsf O(\\mathbf r)=\\frac{1}{8\\pi\\mu r}(\\mathbb 1+\\hat{\\mathbf r}\\hat{\\mathbf r})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0760", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics", "b": "08-condensed-matter/soft-matter/active-matter", "name": "Microswimmers at low Reynolds number", "kind": "mechanism", "summary": "Bacteria and synthetic swimmers live at Re~1e-5, where Purcell's scallop theorem forbids reciprocal strokes and Stokesian far fields (pusher/puller force dipoles) set their collective hydrodynamics and active stresses.", "map": "\\mu\\nabla^2\\mathbf u=\\nabla p,\\ \\mathbf u_{\\text{dipole}}\\propto\\frac{p}{8\\pi\\mu r^2}[3(\\hat{\\mathbf e}\\cdot\\hat{\\mathbf r})^2-1]\\hat{\\mathbf r}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0761", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics", "b": "08-condensed-matter/soft-matter/colloids-and-granular-matter", "name": "Stokes drag and diffusion of colloids", "kind": "identity", "summary": "Colloid diffusion follows from Stokes drag via the Einstein relation, and sedimentation, hydrodynamic interactions and lubrication forces between colloids are low-Reynolds-number flow problems.", "map": "D=\\frac{k_BT}{6\\pi\\eta a};\\ v_{\\text{sed}}=\\frac{2\\Delta\\rho ga^2}{9\\eta};\\ Pe=\\frac{va}{D}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0762", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "08-condensed-matter/soft-matter/active-matter", "name": "Active turbulence versus inertial turbulence", "kind": "analogy", "summary": "Dense bacterial suspensions and active nematics show chaotic mesoscale vortices with power-law energy spectra at Reynolds numbers far below 1, driven by active stress rather than inertia.", "map": "E(k)\\sim k^{-5/3}\\ (\\text{Kolmogorov, inertial})\\ \\text{vs}\\ E(k)\\ \\text{power laws set by active length }\\ell_a=\\sqrt{K/|\\zeta|}", "breaks": "Energy is injected at every scale by active stress and dissipated by viscosity, with no inertial cascade; the vortex size is set by an active length, and spectral exponents are not universal.", "confidence": "current research", "strength": 2}
{"id": "C0763", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "08-condensed-matter/soft-matter/polymers", "name": "Polymer drag reduction and elastic turbulence", "kind": "mechanism", "summary": "Dilute long polymers reduce turbulent drag by up to ~80% (Toms effect) by suppressing near-wall vortices, and in viscous flows polymer elasticity alone drives chaotic 'elastic turbulence' at Reynolds numbers far below 1.", "map": "Wi=\\lambda\\dot\\gamma\\gg1,\\ Re\\ll1\\Rightarrow\\text{elastic turbulence};\\ \\text{Virk asymptote }U^+=11.7\\ln y^+-17", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0764", "a": "01-classical-mechanics/newtonian-mechanics/conservation-laws", "b": "08-condensed-matter/soft-matter/colloids-and-granular-matter", "name": "Inelastic collisions and granular gases", "kind": "mechanism", "summary": "Grains collide with a restitution coefficient below 1, so a granular gas loses energy in every collision; the resulting homogeneous cooling (Haff's law) and clustering instability follow from momentum conservation with kinetic-energy loss.", "map": "v_n'=-e\\,v_n,\\ \\Delta E=-\\tfrac14m(1-e^2)v_n^2;\\ T(t)=\\frac{T_0}{(1+t/\\tau_0)^2}\\ (\\text{Haff})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0765", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos", "b": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "name": "Chaotic billiards and mesoscopic conductance fluctuations", "kind": "mechanism", "summary": "Ballistic quantum dots whose classical shape gives chaotic trajectories show universal conductance fluctuations and weak-localization lineshapes governed by random-matrix theory, while regular (integrable) shapes do not; classical chaos thus controls quantum transport statistics.", "map": "\\mathrm{var}\\,G\\sim(e^2/h)^2,\\ \\delta G(B)\\ \\text{Lorentzian, width}\\propto\\sqrt{\\gamma_{\\text{esc}}}\\ (\\text{chaotic})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0766", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos", "b": "08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction", "name": "Frenkel-Kontorova model and the standard map", "kind": "identity", "summary": "Ground states of the Frenkel-Kontorova model of an incommensurate adsorbate or modulated crystal correspond to orbits of an area-preserving twist map; Aubry's pinning transition, where the incommensurate phase locks to the lattice, is the breakup of a KAM torus, and the devil's staircase of commensurate phases follows.", "map": "E=\\sum_n\\left[\\tfrac12(u_{n+1}-u_n-\\mu)^2+\\frac{K}{(2\\pi)^2}(1-\\cos2\\pi u_n)\\right]\\Rightarrow p_{n+1}=p_n+\\frac{K}{2\\pi}\\sin2\\pi u_n", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0767", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "FPUT anharmonic lattice and the discovery of solitons", "kind": "historical", "summary": "The 1955 Fermi-Pasta-Ulam-Tsingou simulation of an anharmonic atomic chain failed to thermalize its phonon modes; Zabusky and Kruskal's continuum limit, the KdV equation, explained the recurrence and introduced the soliton.", "map": "m\\ddot x_n=K(x_{n+1}-2x_n+x_{n-1})[1+\\alpha(x_{n+1}-x_{n-1})]\\to u_t+6uu_x+u_{xxx}=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0768", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "b": "08-condensed-matter/magnetism/magnetic-skyrmions-and-textures", "name": "Magnetic skyrmions as topological solitons", "kind": "identity", "summary": "Skyrmions are localized, particle-like solutions of the nonlinear micromagnetic field equations, stable because of an integer winding number, the topological-soliton class first introduced by Skyrme for nucleons.", "map": "N_{sk}=\\frac1{4\\pi}\\int\\mathbf m\\cdot(\\partial_x\\mathbf m\\times\\partial_y\\mathbf m)\\,d^2x\\in\\mathbb Z", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0769", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "Fluxons in long Josephson junctions are sine-Gordon solitons", "kind": "identity", "summary": "The phase difference along a long Josephson junction obeys the sine-Gordon equation; its kink solitons are fluxons carrying one flux quantum, which move relativistically at the Swihart velocity and underlie flux-flow oscillators.", "map": "\\lambda_J^2\\varphi_{xx}-\\omega_p^{-2}\\varphi_{tt}=\\sin\\varphi\\Rightarrow\\varphi=4\\arctan\\exp\\frac{x-vt}{\\lambda_J\\sqrt{1-v^2/\\bar c^2}}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0770", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "SSH domain-wall solitons and topological zero modes", "kind": "identity", "summary": "Domain walls between the two dimerization patterns of polyacetylene are solitons that bind a mid-gap zero mode with fractional charge or reversed spin-charge relation; the SSH chain is now the prototype 1D topological insulator (Jackiw-Rebbi index).", "map": "\\Delta(x)=\\Delta_0\\tanh(x/\\xi)\\Rightarrow\\text{zero mode }\\psi_0\\propto e^{-\\int|\\Delta|/\\hbar v_F};\\ \\nu=\\frac1{2\\pi}\\oint d\\arg h(k)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0771", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation", "b": "08-condensed-matter/soft-matter/active-matter", "name": "Flocking as synchronization in space", "kind": "analogy", "summary": "Alignment of headings in the Vicsek model is Kuramoto-like phase synchronization of self-propelled oscillators, with the twist that particles move and so couplings change; both show noise-driven order-disorder transitions.", "map": "\\dot\\theta_i=\\omega_i+\\frac KN\\sum_j\\sin(\\theta_j-\\theta_i)\\leftrightarrow\\theta_i(t+1)=\\langle\\theta_j\\rangle_{|r_{ij}|<R}+\\eta_i", "breaks": "Vicsek particles move, so the coupling network changes with the order itself, giving density bands and giant number fluctuations that have no counterpart in fixed-network Kuramoto models; their order parameter is a vector, not a phase.", "confidence": "established", "strength": 2}
{"id": "C0772", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "Synchronization of Josephson-junction arrays", "kind": "mechanism", "summary": "Series arrays of current-biased junctions coupled through a shared load map onto the Kuramoto model and phase-lock, the route to coherent microwave emission; Shapiro steps are Arnold-tongue frequency locking of a junction to an external drive.", "map": "\\langle V\\rangle=n\\frac{hf}{2e}\\ (\\text{Shapiro});\\ \\dot\\theta_i=\\omega_i+\\frac KN\\sum_j\\sin(\\theta_j-\\theta_i)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0773", "a": "01-classical-mechanics/oscillations-and-waves", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "Phonons as quantized normal modes", "kind": "identity", "summary": "Phonons are the quantized normal modes of the crystal's coupled harmonic oscillators; each mode contributes hbar*omega(n+1/2), giving Debye and Einstein heat capacities.", "map": "H=\\sum_{\\mathbf k,s}\\hbar\\omega_s(\\mathbf k)(a^\\dagger_{\\mathbf ks}a_{\\mathbf ks}+\\tfrac12)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0774", "a": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "b": "08-condensed-matter/crystals-and-electronic-structure", "name": "Normal-mode analysis behind lattice dynamics", "kind": "method transfer", "summary": "Translation symmetry turns the classical normal-mode problem of N coupled oscillators into Bloch-labelled branches, the same diagonalization used for electrons in periodic potentials.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0775", "a": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "b": "08-condensed-matter/crystals-and-electronic-structure/phonons-and-lattice-dynamics", "name": "Monatomic and diatomic chains to phonon branches", "kind": "identity", "summary": "The dispersion of a mass-spring chain is the phonon dispersion of a 1D crystal; a two-atom basis splits it into acoustic and optical branches with a gap at the zone boundary, and the dynamical matrix generalizes this to 3D.", "map": "\\omega(k)=2\\sqrt{K/m}\\,|\\sin(ka/2)|;\\ \\det[D(\\mathbf k)-\\omega^2\\mathbb 1]=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0776", "a": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "b": "08-condensed-matter/topological-matter/band-topology-and-berry-curvature", "name": "Mechanical topological insulators from coupled oscillators", "kind": "method transfer", "summary": "Arrays of coupled pendula or resonators engineered to mimic a quantum spin Hall Hamiltonian show helical edge modes, demonstrating that band topology is a property of linear wave equations, not of electrons.", "map": "\\ddot{\\mathbf x}=-D\\mathbf x,\\ D(\\mathbf k)\\simeq\\omega_0^2\\mathbb 1+H_{\\text{BHZ}}(\\mathbf k);\\ \\omega^2\\leftrightarrow E", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0777", "a": "01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators", "b": "08-condensed-matter/crystals-and-electronic-structure/electronic-transport-and-mesoscopic-physics", "name": "Drude and Lorentz models as damped driven oscillators", "kind": "identity", "summary": "The optical conductivity of metals (free carriers) and insulators (bound oscillators, phonons, excitons) is the response of a driven damped harmonic oscillator, with resonance width set by scattering rate.", "map": "m\\ddot x+\\frac m\\tau\\dot x+m\\omega_0^2x=-eE_0e^{-i\\omega t}\\Rightarrow\\sigma(\\omega)=\\frac{ne^2\\tau/m}{1-i\\omega\\tau(1-\\omega_0^2/\\omega^2)}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0778", "a": "01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics", "b": "08-condensed-matter/crystals-and-electronic-structure/band-theory-and-bloch-electrons", "name": "Phononic crystals: Bloch bands for sound", "kind": "identity", "summary": "Periodic elastic composites have acoustic band structures and complete band gaps computed with Bloch's theorem, the classical-wave analogue of electronic band theory that underlies acoustic metamaterials.", "map": "\\mathbf u(\\mathbf r+\\mathbf R)=e^{i\\mathbf k\\cdot\\mathbf R}\\mathbf u(\\mathbf r);\\ \\text{gap at }k=\\pi/a\\ \\text{when impedance contrast }Z_1\\neq Z_2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0779", "a": "01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations", "b": "08-condensed-matter/superconductivity/josephson-effect-and-squids", "name": "Josephson junction as a driven nonlinear pendulum", "kind": "identity", "summary": "In the RCSJ model the junction phase is a damped, driven pendulum, giving hysteresis, Shapiro steps and chaos; pumping its nonlinear inductance makes a Duffing-type parametric amplifier used for quantum-limited readout.", "map": "\\frac{\\hbar C}{2e}\\ddot\\varphi+\\frac{\\hbar}{2eR}\\dot\\varphi+I_c\\sin\\varphi=I\\leftrightarrow mL^2\\ddot\\theta+\\gamma\\dot\\theta+mgL\\sin\\theta=\\tau;\\ \\omega_p=\\sqrt{2eI_c/\\hbar C}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0780", "a": "01-classical-mechanics/rigid-body-dynamics/gyroscopes-and-precession", "b": "08-condensed-matter/magnetism/spintronics", "name": "Magnetization precession as gyroscopic motion", "kind": "identity", "summary": "The Landau-Lifshitz-Gilbert equation is the torque equation of a gyroscope for spin angular momentum: the magnetization precesses about the effective field and relaxes through Gilbert damping, while spin-transfer torque acts as an additional applied torque.", "map": "\\frac{d\\mathbf M}{dt}=-\\gamma\\mathbf M\\times\\mathbf H_{\\text{eff}}+\\frac\\alpha M\\mathbf M\\times\\frac{d\\mathbf M}{dt}\\leftrightarrow\\boldsymbol\\tau=\\boldsymbol\\Omega\\times\\mathbf L", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0781", "a": "01-classical-mechanics/rigid-body-dynamics/rotational-dynamics-and-inertia-tensor", "b": "08-condensed-matter/magnetism/exchange-and-magnetic-order", "name": "Einstein-de Haas and Barnett effects", "kind": "mechanism", "summary": "Reversing a ferromagnet's magnetization makes the free body rotate (Einstein-de Haas), and rotating a body magnetizes it (Barnett), because total spin plus rigid-body angular momentum is conserved; these measured the electron g-factor and now enable ultrafast demagnetization studies.", "map": "\\Delta L_{\\text{body}}=-\\Delta S=-\\frac{2m_e}{ge}\\Delta M V;\\ \\mathbf M=\\chi\\frac{\\boldsymbol\\Omega}{\\gamma}\\ (\\text{Barnett})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0782", "a": "01-classical-mechanics/analytical-mechanics/canonical-transformations-and-hamilton-jacobi", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics", "name": "Action-angle variables and Delaunay elements", "kind": "method transfer", "summary": "Hamilton–Jacobi theory yields Delaunay and Poincaré action-angle variables, the basis of canonical perturbation theory, averaging and Hamiltonian maps for planetary dynamics.", "map": "L=\\sqrt{GMa},\\; G=L\\sqrt{1-e^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0783", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "09-astrophysics-and-cosmology/dark-matter/astrophysical-evidence-for-dark-matter", "name": "Collisionless Boltzmann equation from Liouville", "kind": "identity", "summary": "Liouville's theorem gives the collisionless Boltzmann equation, which underlies Jeans equations and mass estimates from stellar and galaxy dynamics, including rotation curves and velocity dispersions.", "map": "\\frac{df}{dt}=\\partial_t f+\\mathbf v\\cdot\\nabla f-\\nabla\\Phi\\cdot\\partial_{\\mathbf v}f=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0784", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure", "name": "Phase-space density constraints on halos", "kind": "mechanism", "summary": "Liouville conservation of coarse-grained phase-space density limits how dense a halo core can be, giving Tremaine–Gunn bounds on warm and fermionic dark matter.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0785", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics", "name": "Symplectic integrators for long-term orbits", "kind": "method transfer", "summary": "Liouville's theorem and symplectic structure motivate Wisdom–Holman integrators that preserve phase-space volume and bound energy error over Gyr integrations.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0786", "a": "01-classical-mechanics/analytical-mechanics/lagrangian-mechanics", "b": "09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history", "name": "Newtonian cosmology and minisuperspace action", "kind": "analogy", "summary": "Friedmann equations follow from Newtonian energy conservation of a test shell, and from a minisuperspace Lagrangian in the scale factor.", "map": "\\dot a^2/a^2=\\tfrac{8\\pi G}{3}\\rho-\\tfrac{k}{a^2}\\;\\leftrightarrow\\; \\tfrac12 v^2-\\tfrac{GM}{r}=E", "breaks": "Pressure gravitates and k is geometry in GR; the Newtonian derivation lacks this and fails for radiation and dark energy without ad hoc input.", "confidence": "established", "strength": 2}
{"id": "C0787", "a": "01-classical-mechanics/analytical-mechanics/lagrangian-mechanics", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Scalar field as particle in a potential", "kind": "analogy", "summary": "Inflaton dynamics map to a particle rolling in a potential with Hubble friction; slow roll is the overdamped limit.", "map": "\\ddot\\phi+3H\\dot\\phi+V'(\\phi)=0", "breaks": "Fluctuations are quantum fields on curved space; the point-particle picture misses perturbation generation.", "confidence": "established", "strength": 2}
{"id": "C0788", "a": "01-classical-mechanics/analytical-mechanics/lagrangian-mechanics", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/binary-stars-and-stellar-populations", "name": "Roche potential in mass transfer", "kind": "shared object", "summary": "The restricted three-body effective potential in a rotating frame defines Roche lobes and the L1 point, governing mass transfer and contact binaries.", "map": "\\Phi_R=-\\frac{GM_1}{r_1}-\\frac{GM_2}{r_2}-\\tfrac12\\Omega^2 \\varpi^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0789", "a": "01-classical-mechanics/analytical-mechanics/variational-principles", "b": "09-astrophysics-and-cosmology/cosmology/gravitational-lensing", "name": "Fermat's principle in gravitational lensing", "kind": "identity", "summary": "Lensing images are stationary points of the time-delay surface (geometric plus Shapiro delay), giving the lens equation and time-delay cosmography.", "map": "t(\\theta)=\\frac{D_\\Delta}{c}\\left[\\tfrac12(\\theta-\\beta)^2-\\psi(\\theta)\\right]", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0790", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "09-astrophysics-and-cosmology/galaxies/active-galactic-nuclei-and-supermassive-black-holes", "name": "Accretion flows as viscous fluid dynamics", "kind": "shared object", "summary": "Accretion disks around black holes are viscous shear flows, and Bondi accretion is a spherical ideal-flow solution, as in the Navier–Stokes and Euler problems.", "map": "\\dot M=4\\pi\\lambda\\rho_\\infty (GM)^2/c_s^3", "breaks": "Angular momentum transport needs MHD turbulence (MRI), not molecular viscosity, and relativity matters near the hole.", "confidence": "established", "strength": 2}
{"id": "C0791", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/gamma-ray-bursts", "name": "Shock and blast-wave hydrodynamics", "kind": "method transfer", "summary": "Sedov–Taylor and Blandford–McKee blast waves are self-similar solutions of the Euler equations, applied to GRB afterglows, supernova remnants and the shocks that accelerate cosmic rays.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0792", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao", "name": "Jeans instability and structure growth", "kind": "mechanism", "summary": "Gravitational collapse of perturbations is the Jeans instability of a self-gravitating fluid, the fluid-mechanics seed of the growth of cosmic structure, modified by expansion drag.", "map": "\\ddot\\delta+2H\\dot\\delta=4\\pi G\\rho\\,\\delta", "breaks": "Dark matter is collisionless, so a fluid description holds only approximately, and nonlinear collapse needs N-body treatment.", "confidence": "established", "strength": 3}
{"id": "C0793", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/stellar-structure-and-evolution", "name": "Convection in stellar interiors", "kind": "shared object", "summary": "Rayleigh–Bénard-type instability sets the Schwarzschild criterion for convection in stars, handled with mixing-length theory.", "map": "\\nabla_{\\rm rad}>\\nabla_{\\rm ad}", "breaks": "Stellar convection is highly turbulent, compressible and stratified, at huge Rayleigh numbers beyond lab regimes.", "confidence": "established", "strength": 2}
{"id": "C0794", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks", "name": "Dust-gas drag in disks and Stokes drag", "kind": "mechanism", "summary": "Small dust grains in protoplanetary disks couple to gas through Stokes or Epstein drag, setting stopping times and radial drift; the same viscous-drag physics governs low-Re flow.", "map": "t_s=\\frac{m v}{F_{\\rm drag}},\\; F=6\\pi\\mu a v", "breaks": "Disk gas is often rarefied (Epstein regime, mean free path > grain size), unlike continuum Stokes flow.", "confidence": "established", "strength": 2}
{"id": "C0795", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/planet-formation-and-protoplanetary-disks", "name": "Disk turbulence and angular momentum transport", "kind": "mechanism", "summary": "Turbulent viscosity (alpha prescription) drives accretion in protoplanetary disks and concentrates dust in vortices and eddies, controlling planetesimal formation.", "map": "\\nu=\\alpha c_s H", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0796", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/binary-stars-and-stellar-populations", "name": "Turbulent fragmentation and the IMF", "kind": "mechanism", "summary": "Supersonic turbulence in molecular clouds, with a Kolmogorov-like cascade, shapes the density distribution and fragmentation, and thus the stellar initial mass function.", "map": "", "breaks": "Gravity, magnetic fields and feedback also matter; whether turbulence alone sets the IMF is debated.", "confidence": "current research", "strength": 2}
{"id": "C0797", "a": "01-classical-mechanics/newtonian-mechanics/central-forces-and-orbits", "b": "09-astrophysics-and-cosmology/dark-matter/alternatives-mond-and-modified-gravity", "name": "MOND modifies Newtonian dynamics", "kind": "analogy", "summary": "MOND modifies the Newtonian force law below an acceleration scale, reproducing flat rotation curves and the Tully–Fisher relation without dark matter.", "map": "\\mu(a/a_0)\\,a=g_N,\\; v^4=GMa_0", "breaks": "Fails to account for cluster masses and CMB peaks without extra components, and needs a relativistic completion.", "confidence": "current research", "strength": 2}
{"id": "C0798", "a": "01-classical-mechanics/newtonian-mechanics/central-forces-and-orbits", "b": "09-astrophysics-and-cosmology/dark-matter/astrophysical-evidence-for-dark-matter", "name": "Rotation curves from Newtonian orbits", "kind": "method transfer", "summary": "Circular-orbit balance gives velocity profiles; flat curves at large radius imply M(<r) growing linearly with r, which signals dark matter.", "map": "v^2=\\frac{GM(<r)}{r}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0799", "a": "01-classical-mechanics/newtonian-mechanics/central-forces-and-orbits", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics", "name": "Kepler orbits and precession in the Solar System", "kind": "shared object", "summary": "Kepler problem, effective potential and perturbed-orbit precession underlie planetary and small-body orbits; secular perturbations produce apsidal and nodal precession.", "map": "U_{\\rm eff}=\\frac{L^2}{2mr^2}-\\frac{GMm}{r}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0800", "a": "01-classical-mechanics/newtonian-mechanics/conservation-laws", "b": "09-astrophysics-and-cosmology/galaxies/galaxy-clusters", "name": "Cluster collisions and conserved quantities", "kind": "shared object", "summary": "Merging clusters (e.g. Bullet Cluster) are analysed with momentum and energy conservation and collision kinematics, constraining collisionless dark matter versus shocked gas.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0801", "a": "01-classical-mechanics/newtonian-mechanics/conservation-laws", "b": "09-astrophysics-and-cosmology/galaxies/galaxy-clusters", "name": "Virial theorem and cluster mass", "kind": "method transfer", "summary": "Energy and momentum conservation lead to the virial theorem, used to estimate cluster dynamical masses from galaxy velocity dispersions (Zwicky's missing mass).", "map": "2\\langle T\\rangle+\\langle U\\rangle=0,\\; M\\sim \\frac{\\sigma^2 R}{G}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0802", "a": "01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets", "name": "Planetary systems as few-body problems", "kind": "shared object", "summary": "Planetary system architecture, stability and resonances are treated with the N-body problem, perturbation theory and numerical integration.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0803", "a": "01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-detection", "name": "Lagrange points and Trojans in exoplanet systems", "kind": "shared object", "summary": "Restricted three-body equilibria define Trojan configurations and co-orbital planets, searched for in exoplanet timing and transit data.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C0804", "a": "01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-detection", "name": "Timing and RV signals from N-body dynamics", "kind": "method transfer", "summary": "Transit-timing variations and radial-velocity multi-planet fits are inverse N-body problems; mean-motion resonances amplify TTVs, allowing masses to be inferred from perturbations.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0805", "a": "01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics", "name": "Resonances and N-body Solar System evolution", "kind": "method transfer", "summary": "Mean-motion and secular resonances, symplectic N-body integrators and perturbation theory are the working tools of Solar System dynamics.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0806", "a": "01-classical-mechanics/newtonian-mechanics/non-inertial-frames", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/exoplanet-atmospheres", "name": "Coriolis force and atmospheric circulation", "kind": "mechanism", "summary": "Rotating-frame dynamics sets hot-Jupiter and terrestrial jet and wave structure, via Rossby numbers and geostrophic balance.", "map": "\\mathrm{Ro}=\\frac{U}{fL}", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0807", "a": "01-classical-mechanics/newtonian-mechanics/non-inertial-frames", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics", "name": "Tides and Coriolis in planetary systems", "kind": "mechanism", "summary": "Tidal forces from non-inertial frame analysis drive tidal locking, orbital migration and Roche limits; Coriolis force shapes planetary atmospheres and rotating-frame Hill dynamics.", "map": "F_{\\rm tide}\\sim \\frac{2GMm\\,r}{d^3}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0808", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/binary-stars-and-stellar-populations", "name": "Chaos in N-body stellar dynamics", "kind": "mechanism", "summary": "Exponential sensitivity in few-body encounters and cluster dynamics limits N-body predictability, so ensembles are used for population synthesis.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C0809", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos", "b": "09-astrophysics-and-cosmology/galaxies/the-milky-way", "name": "Orbits and resonances in the Galactic potential", "kind": "method transfer", "summary": "Action-angle methods and resonance structure describe stellar orbits in barred potentials; bar resonances produce moving groups and phase-space features seen in Gaia.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0810", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics", "name": "KAM tori and chaos in planetary stability", "kind": "mechanism", "summary": "Long-term stability of planetary orbits is a KAM question: resonance overlap produces chaotic zones, Kirkwood gaps and Lyapunov times of order millions of years for the Solar System.", "map": "\\text{resonance overlap: } \\Delta\\omega_{\\rm res}\\gtrsim \\delta\\omega_{\\rm spacing}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0811", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "b": "09-astrophysics-and-cosmology/dark-matter/dark-matter-small-scale-structure", "name": "Fuzzy dark matter solitons", "kind": "shared object", "summary": "Ultralight scalar dark matter obeys a Schrödinger–Poisson system whose ground state is a stable soliton core in halos, tied to nonlinear Schrödinger structure.", "map": "i\\hbar\\partial_t\\psi=-\\frac{\\hbar^2}{2m}\\nabla^2\\psi+m\\Phi\\psi", "breaks": "Poisson coupling is nonlocal, so the system is not integrable like the cubic NLS and solitons are not exact.", "confidence": "current research", "strength": 2}