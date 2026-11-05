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

# Packet 01-5 (85 records)

{"id": "C0812", "a": "01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators", "b": "09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background", "name": "Driven damped oscillator and acoustic peaks", "kind": "identity", "summary": "Photon-baryon plasma modes obey a forced, damped oscillator equation, with gravity driving, baryon loading shifting the zero point, and Silk damping suppressing high multipoles.", "map": "\\ddot\\Theta+\\frac{\\dot c_s^2}{}\\,k^2\\Theta=F(\\Phi)", "breaks": "Damping is from photon diffusion at finite mean free path, not a simple friction term; the system is also relativistic.", "confidence": "established", "strength": 3}
{"id": "C0813", "a": "01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/the-sun-and-helioseismology", "name": "Normal modes of the Sun", "kind": "shared object", "summary": "Solar p-modes and g-modes are the normal modes of a stratified self-gravitating sphere, and helioseismology inverts mode frequencies to infer interior structure.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0814", "a": "01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics", "b": "09-astrophysics-and-cosmology/cosmology/large-scale-structure-and-bao", "name": "Baryon acoustic oscillations as sound waves", "kind": "mechanism", "summary": "BAO are sound waves in the pre-recombination plasma that froze at the drag epoch, leaving a standard ruler equal to the sound horizon.", "map": "r_s=\\int_0^{t_d}\\frac{c_s\\,dt}{a}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0815", "a": "01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations", "b": "09-astrophysics-and-cosmology/cosmology/inflation", "name": "Parametric resonance in preheating", "kind": "mechanism", "summary": "After inflation, the oscillating inflaton drives daughter fields through Mathieu-equation parametric resonance, producing explosive particle production.", "map": "\\ddot\\chi_k+\\left[k^2+g^2\\Phi^2\\sin^2(mt)\\right]\\chi_k=0", "breaks": "Backreaction and rescattering end the resonance, so the linear Mathieu analysis fails when occupation grows.", "confidence": "established", "strength": 2}
{"id": "C0816", "a": "01-classical-mechanics/rigid-body-dynamics/euler-equations-and-tops", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/solar-system-dynamics", "name": "Spin-orbit dynamics and chaotic tumbling", "kind": "mechanism", "summary": "Intermediate-axis instability and spin-orbit coupling give chaotic rotation of irregular moons such as Hyperion, and spin-orbit resonances like Mercury's 3:2.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0817", "a": "01-classical-mechanics/rigid-body-dynamics/euler-equations-and-tops", "b": "09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects", "name": "Rigid rotation, free precession and pulsars", "kind": "mechanism", "summary": "Euler's equations for torque-free bodies describe free precession of neutron stars, and rotational dynamics governs pulsar spin-down and glitches, though the superfluid interior complicates a rigid-body model.", "map": "", "breaks": "Neutron stars have superfluid interiors and elastic crusts, so a single rigid body fails.", "confidence": "current research", "strength": 2}
{"id": "C0818", "a": "01-classical-mechanics/rigid-body-dynamics/gyroscopes-and-precession", "b": "09-astrophysics-and-cosmology/planetary-science-and-exoplanets/astrobiology-and-habitability", "name": "Axial precession and obliquity climate cycles", "kind": "mechanism", "summary": "Torque-driven precession and obliquity variations (Milankovitch cycles) modulate insolation; obliquity stability, enforced by a large moon, affects habitability.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0819", "a": "01-classical-mechanics/analytical-mechanics/canonical-transformations-and-hamilton-jacobi", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Adiabatic invariants as action variables", "kind": "identity", "summary": "The magnetic moment, bounce invariant J and flux invariant are action integrals of near-periodic motion, conserved to all orders in the slow-variation parameter under averaging.", "map": "J=\\oint p\\,dq,\\ \\mu\\propto J_\\perp", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0820", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Vlasov equation as Liouville flow", "kind": "identity", "summary": "The collisionless Vlasov equation is Liouville's theorem for the single-particle distribution function in phase space, with Poisson-bracket form and Hamiltonian field structure.", "map": "\\partial_t f+\\{f,H\\}=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0821", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Guiding-centre Hamiltonian dynamics", "kind": "method transfer", "summary": "Guiding-centre motion is derived via Hamiltonian and Lagrangian averaging (Littlejohn, Lie-transform perturbation theory), preserving the symplectic structure and giving adiabatic invariants.", "map": "\\mu=\\frac{m v_\\perp^2}{2B}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0822", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "10-plasma-physics/space-and-astrophysical-plasmas/magnetospheres-and-space-weather", "name": "Radiation belts and three adiabatic invariants", "kind": "mechanism", "summary": "Trapped radiation-belt particles carry three adiabatic invariants (μ, J, Φ) from separation of gyro, bounce and drift timescales, a nearly integrable Hamiltonian system; radial diffusion breaks the third.", "map": "\\mu,\\ J,\\ \\Phi", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0823", "a": "01-classical-mechanics/analytical-mechanics/lagrangian-mechanics", "b": "10-plasma-physics/magnetic-confinement-fusion/turbulent-transport-and-gyrokinetics", "name": "Gyrokinetics from Lagrangian field theory", "kind": "method transfer", "summary": "Modern gyrokinetics is derived from a phase-space Lagrangian with Lie-transform and variational methods, ensuring exact conservation laws via Noether's theorem.", "map": "\\delta\\int L\\,dt=0\\Rightarrow\\text{conserved energy}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0824", "a": "01-classical-mechanics/analytical-mechanics/variational-principles", "b": "10-plasma-physics/magnetic-confinement-fusion/tokamaks", "name": "Variational MHD equilibrium and stability", "kind": "method transfer", "summary": "MHD equilibrium extremizes energy at fixed constraints and stability follows from the energy principle δW, a Rayleigh–Ritz variational method; Grad–Shafranov describes axisymmetric equilibria.", "map": "\\delta W[\\boldsymbol\\xi]\\ge0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0825", "a": "01-classical-mechanics/continuum-and-fluid-mechanics", "b": "10-plasma-physics/magnetohydrodynamics", "name": "MHD as continuum mechanics", "kind": "shared object", "summary": "MHD applies continuum conservation laws of mass, momentum and energy to a conducting fluid with added magnetic stress.", "map": "\\rho\\,d\\mathbf{u}/dt=-\\nabla p+\\mathbf{J}\\times\\mathbf{B}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0826", "a": "01-classical-mechanics/continuum-and-fluid-mechanics", "b": "10-plasma-physics/magnetohydrodynamics", "name": "MHD as fluid mechanics plus Lorentz force", "kind": "identity", "summary": "Ideal MHD is Euler or Navier–Stokes flow coupled to induction and the Lorentz force; vorticity and magnetic-field equations share the same frozen-in structure.", "map": "\\partial_t \\mathbf{B}=\\nabla\\times(\\mathbf{u}\\times\\mathbf{B}),\\ \\partial_t \\boldsymbol{\\omega}=\\nabla\\times(\\mathbf{u}\\times\\boldsymbol{\\omega})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0827", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "Alfvén waves as tension waves; Kelvin circulation", "kind": "mechanism", "summary": "Frozen-in flux parallels Kelvin's circulation theorem and vorticity transport; magnetic tension gives Alfvén waves like waves on a string, extending Euler flow.", "map": "v_A=B/\\sqrt{\\mu_0\\rho}", "breaks": "Magnetic field adds anisotropic restoring force, so waves are not isotropic.", "confidence": "established", "strength": 3}
{"id": "C0828", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "10-plasma-physics/space-and-astrophysical-plasmas/solar-wind-and-heliosphere", "name": "Parker wind as transonic nozzle flow", "kind": "analogy", "summary": "Parker's solar wind is a de Laval-nozzle type steady flow with a critical sonic point; gravity and geometry replace the nozzle area change.", "map": "\\left(u-\\frac{c_s^2}{u}\\right)\\frac{du}{dr}=\\frac{2c_s^2}{r}-\\frac{GM}{r^2}", "breaks": "Wind is heated and magnetised, and the solar wind is collisionless with non-fluid effects.", "confidence": "established", "strength": 2}
{"id": "C0829", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "10-plasma-physics/inertial-and-laser-plasmas", "name": "Laser-plasma hydrodynamic instabilities", "kind": "shared object", "summary": "Laser-driven ablation and shock-accelerated interfaces in laser plasmas realise classic interfacial instabilities (RT, RM, KH) under extreme conditions.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0830", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "10-plasma-physics/inertial-and-laser-plasmas/inertial-confinement-fusion", "name": "Rayleigh–Taylor in ICF implosions", "kind": "shared object", "summary": "Rayleigh–Taylor and Richtmyer–Meshkov instabilities at the ablation front and fuel–shell interface limit capsule compression and ignition; classical growth rates are modified by ablation.", "map": "\\gamma=\\sqrt{A k g}-\\beta k v_a", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0831", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "10-plasma-physics/magnetohydrodynamics/dynamo-theory", "name": "Convection-driven dynamos", "kind": "mechanism", "summary": "Rotating Rayleigh–Bénard convection drives geodynamo and solar dynamo flows, with helical convective motions supplying the α-effect.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0832", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "MHD instabilities as magnetised RT/KH", "kind": "mechanism", "summary": "Interchange instability is Rayleigh–Taylor with effective gravity from field curvature; magnetic tension modifies Kelvin–Helmholtz thresholds and Chandrasekhar's magnetised convection.", "map": "\\gamma^2\\sim -g_{eff}\\,\\nabla\\ln p", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0833", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Kinetic vs fluid instability analyses", "kind": "method transfer", "summary": "Normal-mode dispersion analysis and Nyquist criteria developed for plasma kinetic instabilities (two-stream, Penrose) parallel hydrodynamic shear and stratified-flow stability; the two-stream instability resembles Kelvin–Helmholtz.", "map": "D(\\omega,k)=0", "breaks": "Kinetic resonance with particle velocities has no fluid counterpart; fluid models lack velocity-space instabilities.", "confidence": "established", "strength": 1}
{"id": "C0834", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Ion-acoustic and Kelvin–Helmholtz in plasmas", "kind": "shared object", "summary": "Kelvin–Helmholtz and Rayleigh–Taylor instabilities occur at magnetopause and in laser plasmas, with magnetic shear and finite Larmor radius modifying growth.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C0835", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "10-plasma-physics/magnetic-confinement-fusion/turbulent-transport-and-gyrokinetics", "name": "Plasma turbulence and fluid turbulence", "kind": "analogy", "summary": "Drift-wave turbulence has cascades, intermittency and zonal-flow formation analogous to 2D fluid turbulence, mirrored by Hasegawa–Mima and Charney–Hasegawa–Mima equations.", "map": "\\partial_t(\\nabla^2\\phi-\\phi)+\\hat z\\times\\nabla\\phi\\cdot\\nabla(\\nabla^2\\phi)=0", "breaks": "Kinetic effects, resonant wave-particle interaction and non-adiabatic electrons have no fluid analogue.", "confidence": "established", "strength": 3}
{"id": "C0836", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "10-plasma-physics/magnetohydrodynamics/dynamo-theory", "name": "Turbulent dynamo and mean-field theory", "kind": "mechanism", "summary": "Turbulent flows stretch, twist and fold field lines, giving small-scale dynamos and mean-field α-effect; the shared accretion-disk paper links turbulence, MRI and transport.", "map": "\\partial_t\\bar{\\mathbf B}=\\nabla\\times(\\alpha\\bar{\\mathbf B}-\\eta_t\\nabla\\times\\bar{\\mathbf B})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0837", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "10-plasma-physics/magnetohydrodynamics/mhd-turbulence", "name": "Kolmogorov cascade to MHD cascade", "kind": "analogy", "summary": "Hydrodynamic energy cascade and Kolmogorov scaling generalize to MHD via Iroshnikov–Kraichnan and Goldreich–Sridhar theories, with Alfvén-wave interactions and anisotropy.", "map": "E(k)\\sim\\epsilon^{2/3}k^{-5/3}\\ \\to\\ E(k_\\perp)\\sim k_\\perp^{-5/3}", "breaks": "Magnetic field imposes anisotropy and non-local interactions; no isotropic Kolmogorov scaling exists in strong mean field.", "confidence": "established", "strength": 3}
{"id": "C0838", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "10-plasma-physics/magnetohydrodynamics/mhd-turbulence", "name": "MHD turbulence extends Kolmogorov theory", "kind": "analogy", "summary": "Critical balance and anisotropic cascades in MHD turbulence extend Kolmogorov phenomenology, with magnetic energy and cross-helicity as additional invariants.", "map": "k_\\parallel v_A\\sim k_\\perp u_\\perp", "breaks": "Strong mean field makes cascade anisotropic; scaling differs from isotropic Kolmogorov.", "confidence": "established", "strength": 3}
{"id": "C0839", "a": "01-classical-mechanics/newtonian-mechanics/conservation-laws", "b": "10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks", "name": "Shock jump conditions as conservation laws", "kind": "identity", "summary": "Rankine–Hugoniot conditions are mass, momentum and energy conservation across a discontinuity; collisionless shocks satisfy them via field-mediated dissipation instead of collisions.", "map": "[\\rho u]=0,\\ [\\rho u^2+p]=0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0840", "a": "01-classical-mechanics/newtonian-mechanics/non-inertial-frames", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Lorentz force and Coriolis force", "kind": "analogy", "summary": "In a rotating frame the Coriolis force has the same form as the magnetic Lorentz force (Larmor's theorem), giving inertial waves and gyration analogous to cyclotron motion.", "map": "2m\\mathbf{v}\\times\\boldsymbol{\\Omega}\\leftrightarrow q\\mathbf{v}\\times\\mathbf{B}", "breaks": "Coriolis force is mass-proportional and charge-independent; the centrifugal term has no magnetic counterpart.", "confidence": "established", "strength": 2}
{"id": "C0841", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos", "b": "10-plasma-physics/magnetic-confinement-fusion/stellarators", "name": "Field-line flow as Hamiltonian system, KAM surfaces", "kind": "identity", "summary": "Magnetic field lines in toroidal geometry obey Hamiltonian equations with toroidal angle as time. Nested flux surfaces are KAM tori; resonant perturbations create islands and chaotic field lines.", "map": "\\frac{d\\theta}{d\\phi}=\\frac{\\partial H}{\\partial\\psi},\\ \\frac{d\\psi}{d\\phi}=-\\frac{\\partial H}{\\partial\\theta}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0842", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Particle trapping and quasilinear resonance overlap", "kind": "mechanism", "summary": "Nonlinear Landau damping and particle trapping in a wave potential produce pendulum-like islands in phase space; overlapping waves yield Chirikov chaos underlying quasilinear diffusion.", "map": "\\omega_b=\\sqrt{qE k/m}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0843", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Adiabatic invariant breakdown and chaos", "kind": "mechanism", "summary": "Magnetic moment conservation fails via resonance overlap or field-line curvature where gyroradius approaches field scale, producing chaotic scattering in current sheets and tail pitch-angle diffusion.", "map": "\\kappa^2=R_c/\\rho\\sim1", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0844", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "b": "10-plasma-physics/inertial-and-laser-plasmas/plasma-wakefield-acceleration", "name": "Nonlinear wake waves and wave breaking", "kind": "analogy", "summary": "Plasma wakes are nonlinear Langmuir waves whose steepening and wave-breaking limit sets accelerating gradients, comparable to nonlinear wave steepening and soliton formation in dispersive media.", "map": "E_{WB}=\\frac{m c\\,\\omega_p}{e}", "breaks": "Wakefields are driven, relativistic and not integrable; breaking is not soliton formation.", "confidence": "established", "strength": 2}
{"id": "C0845", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Ion-acoustic solitons and KdV", "kind": "shared object", "summary": "Weakly nonlinear ion-acoustic waves reduce to the KdV equation via reductive perturbation, giving solitons; Washimi–Taniuti derivation was a landmark. Alfvén waves yield DNLS.", "map": "u_t+6uu_x+u_{xxx}=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0846", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation", "b": "10-plasma-physics/magnetohydrodynamics/magnetic-reconnection", "name": "Plasmoid chain formation as pattern formation", "kind": "analogy", "summary": "Plasmoid instability of reconnection current sheets spontaneously produces hierarchical island chains from a tearing instability, analogous to pattern-forming instabilities.", "map": "", "breaks": "Tearing is driven by free magnetic energy in a topological change; there is no Turing-type wavelength selection by diffusion.", "confidence": "current research", "strength": 1}
{"id": "C0847", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Landau damping and Kuramoto synchronization", "kind": "mechanism", "summary": "Kuramoto oscillators with a frequency distribution obey a Vlasov-like continuum equation; incoherent-state stability and decay of the order parameter mirror Landau damping, as does the Case–Van Kampen analysis.", "map": "\\partial_t f+\\partial_\\theta(\\omega f)=0\\ \\leftrightarrow\\ \\partial_t f+v\\partial_x f=0", "breaks": "Kuramoto coupling is mean-field on a circle with no spatial structure; Kuramoto-model Landau damping is for non-smooth distributions.", "confidence": "current research", "strength": 2}
{"id": "C0848", "a": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "b": "10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas", "name": "Dust crystal lattice phonons", "kind": "shared object", "summary": "Dusty-plasma crystals support lattice phonons observable by video microscopy; they are screened-Coulomb (Yukawa) chains and lattices with normal modes, allowing atomic-scale dynamics at the particle level.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0849", "a": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Plasma oscillation as collective normal mode", "kind": "analogy", "summary": "Langmuir oscillation at ω_p is a collective harmonic mode of displaced electron sheets, and plasma waves are dispersive normal modes of a continuum of coupled oscillators.", "map": "\\omega_p^2=\\frac{n e^2}{\\epsilon_0 m}", "breaks": "Long-range Coulomb coupling gives non-local dispersion and Landau damping not present in lattice chains.", "confidence": "established", "strength": 2}
{"id": "C0850", "a": "01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "Magnetosonic and acoustic waves", "kind": "analogy", "summary": "Fast magnetosonic waves are sound waves stiffened by magnetic pressure; the Alfvén wave is a string wave along field lines, with dispersion from impedance-like medium properties.", "map": "v_f^2=c_s^2+v_A^2\\ (\\perp)", "breaks": "Anisotropic propagation and three wave branches, unlike isotropic sound.", "confidence": "established", "strength": 2}
{"id": "C0851", "a": "01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "Ponderomotive force and Kapitza pendulum", "kind": "identity", "summary": "A charged particle in a rapidly oscillating field feels an effective ponderomotive potential, the same averaging that stabilizes the Kapitza pendulum's inverted position.", "map": "U_p=\\frac{q^2E^2}{4m\\omega^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0852", "a": "01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Parametric instabilities and Mathieu resonance", "kind": "mechanism", "summary": "Parametric decay instabilities in laser-plasma and plasma waves are three-wave coupled-mode versions of parametric resonance (Mathieu), with pump threshold set by damping.", "map": "\\gamma^2=\\gamma_0^2-\\Gamma_1\\Gamma_2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0853", "a": "01-classical-mechanics/analytical-mechanics/canonical-transformations-and-hamilton-jacobi", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Action–angle variables and Courant–Snyder invariant", "kind": "identity", "summary": "The Courant–Snyder transform is a canonical change to action–angle variables for linear betatron motion. The invariant is the action J and the phase advance is the angle.", "map": "2J=\\gamma x^2+2\\alpha xx'+\\beta x'^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0854", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Beam optics as Hamiltonian flow", "kind": "identity", "summary": "Particle motion in accelerators is Hamiltonian, so Liouville's theorem makes emittance conserved. Linear transfer maps are symplectic and Twiss parameters follow from them.", "map": "M^T J M=J,\\;\\epsilon=\\sqrt{\\langle x^2\\rangle\\langle x'^2\\rangle-\\langle xx'\\rangle^2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0855", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Classical trajectories and phase-space transition states", "kind": "method transfer", "summary": "Reaction rates are computed from classical Hamiltonian trajectories on potential energy surfaces, and transition-state theory uses phase-space dividing surfaces and invariant manifolds.", "map": "k_{TST}=\\tfrac{k_BT}{h}e^{-\\Delta G^\\ddagger/k_BT}", "breaks": "Tunnelling and non-adiabatic effects need quantum treatment.", "confidence": "established", "strength": 2}
{"id": "C0856", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Hamiltonian treatment of spin dynamics in MRI", "kind": "analogy", "summary": "Spin motion in a magnetic field maps onto a rotating-frame equation that parallels the rigid-body rotation formalism, which is used in pulse sequence design.", "map": "\\dot{\\mathbf M}=\\gamma\\mathbf M\\times\\mathbf B", "breaks": "Relaxation makes the dynamics dissipative, so phase-space volume is not conserved.", "confidence": "established", "strength": 1}
{"id": "C0857", "a": "01-classical-mechanics/analytical-mechanics/variational-principles", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Fermat principle and seismic ray tracing", "kind": "method transfer", "summary": "Seismic travel-time tomography uses Fermat's principle and Snell's law to trace rays through velocity models, with the ray parameter conserved in a spherical Earth.", "map": "p=r\\sin i/v", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0858", "a": "01-classical-mechanics/analytical-mechanics/variational-principles", "b": "11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics", "name": "Fermat's principle in ray-based imaging", "kind": "method transfer", "summary": "Fermat's principle gives ray paths through tissue and in the Earth, used in travel-time and ray-based reconstruction. It underlies delay-and-sum beamforming and sound-speed estimation.", "map": "\\delta\\int n\\,ds=0", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C0859", "a": "01-classical-mechanics/continuum-and-fluid-mechanics", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Navier–Stokes to geophysical fluid dynamics", "kind": "identity", "summary": "Atmospheric dynamics is the Navier–Stokes/Euler system on a rotating, stratified sphere, with the Boussinesq and hydrostatic approximations and geostrophic balance as reductions.", "map": "\\partial_t \\mathbf{u}+\\mathbf{u}\\cdot\\nabla\\mathbf{u}+2\\boldsymbol\\Omega\\times\\mathbf{u}=-\\nabla p/\\rho+\\mathbf{g}+\\nu\\nabla^2\\mathbf{u}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0860", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "name": "Helfrich bending elasticity of membranes", "kind": "mechanism", "summary": "Membrane bending energy is the thin-shell elasticity of plates adapted to fluid bilayers, with curvature energy governing vesicle shapes and buckling-like transitions.", "map": "E=\\tfrac{\\kappa}{2}\\int(2H-c_0)^2dA", "breaks": "The bilayer is a 2D fluid with no shear modulus, unlike solid plates.", "confidence": "established", "strength": 2}
{"id": "C0861", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Earth as an elastic body", "kind": "shared object", "summary": "Seismic waves, free oscillations and mantle stress response use linear elasticity, with viscoelastic extension for postglacial rebound.", "map": "\\rho\\ddot u_i=\\partial_j\\sigma_{ij},\\;\\sigma_{ij}=C_{ijkl}\\varepsilon_{kl}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0862", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Elastic moduli and seismic wave speeds", "kind": "identity", "summary": "Seismic P and S wave speeds follow from the Lamé constants and density of the elastic wave equation. Tomography inverts them to map Earth's interior.", "map": "v_P=\\sqrt{(\\lambda+2\\mu)/\\rho},\\; v_S=\\sqrt{\\mu/\\rho}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0863", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics", "name": "Elastography: tissue stiffness from shear waves", "kind": "method transfer", "summary": "Shear wave elastography measures shear wave speed in tissue to infer the shear modulus, an inverse problem in linear elasticity used to detect tumours and fibrosis.", "map": "\\mu=\\rho c_s^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0864", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics", "name": "Ocean circulation as rotating viscous flow", "kind": "shared object", "summary": "Ekman layers, boundary-layer theory and vorticity dynamics explain wind-driven gyres and western boundary intensification (Stommel and Munk).", "map": "\\beta v=\\tfrac{1}{\\rho}\\hat z\\cdot\\nabla\\times\\boldsymbol\\tau", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0865", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "name": "Plateau–Rayleigh and membrane shape instabilities", "kind": "analogy", "summary": "Surface-tension-driven pearling and tubulation of lipid tubes echo the Plateau–Rayleigh instability, with bending rigidity and membrane tension setting the selected wavelength.", "map": "\\lambda\\sim 2\\pi\\sqrt{\\kappa/\\sigma}", "breaks": "Membranes have bending elasticity and fixed area, unlike simple liquid jets.", "confidence": "current research", "strength": 1}
{"id": "C0866", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Convective instability in the atmosphere", "kind": "mechanism", "summary": "Moist and dry convection and the Rayleigh–Bénard/Lorenz system share a buoyancy-driven instability criterion. Brunt–Väisälä frequency marks stratified stability.", "map": "N^2=-\\tfrac{g}{\\rho}\\tfrac{d\\rho}{dz}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0867", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Mantle convection and the geodynamo", "kind": "shared object", "summary": "Rayleigh–Bénard convection with a Rayleigh-number threshold describes mantle convection driving plate tectonics, and rotating convection in the outer core drives the geodynamo.", "map": "Ra=g\\alpha\\Delta T d^3/(\\nu\\kappa)", "breaks": "Mantle viscosity is strongly temperature-dependent and non-Newtonian, and the core also needs magnetic and rotational effects.", "confidence": "established", "strength": 2}
{"id": "C0868", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics", "b": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "name": "Cell mechanics and viscous microhydrodynamics", "kind": "shared object", "summary": "Vesicle dynamics, cytoplasmic flow and cell crawling combine membrane elasticity with viscous Stokes flow. Dimensionless numbers such as the capillary number control deformation.", "map": "Ca=\\eta\\dot\\gamma R/\\sigma", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0869", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics", "b": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "name": "Stokes flow in cells and membranes", "kind": "shared object", "summary": "Cell motility, cytoplasmic and membrane flows occur at very low Reynolds number. Membrane hydrodynamics (Saffman–Delbrück) and swimming under time-reversal constraints use Stokes flow.", "map": "\\eta\\nabla^2\\mathbf{u}=\\nabla p,\\;\\nabla\\cdot\\mathbf{u}=0", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0870", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics", "b": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "name": "Overdamped dynamics and Stokes drag in tweezers", "kind": "shared object", "summary": "Optical and magnetic tweezers experiments operate at low Reynolds number, where Stokes drag on beads sets the calibration and fluctuation-dissipation relations.", "map": "\\gamma=6\\pi\\eta a,\\; D=k_BT/\\gamma", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0871", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Atmospheric turbulence and cascades", "kind": "shared object", "summary": "The atmosphere shows a 3D Kolmogorov cascade at small scales and a quasi-2D inverse energy cascade at synoptic scales. Eddy fluxes need closure in models.", "map": "E(k)\\sim\\varepsilon^{2/3}k^{-5/3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0872", "a": "01-classical-mechanics/newtonian-mechanics/central-forces-and-orbits", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Rutherford scattering and molecular beam collisions", "kind": "method transfer", "summary": "Classical central-force scattering with impact parameter and deflection function underlies crossed-molecular-beam analysis, including rainbow and glory scattering.", "map": "\\Theta(b)=\\pi-2\\int\\frac{b\\,dr/r^2}{\\sqrt{1-b^2/r^2-V/E}}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0873", "a": "01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Resonances and N-body methods in accelerators", "kind": "method transfer", "summary": "Resonance overlap, secular perturbation theory and symplectic integrators from celestial mechanics are used for accelerator tracking and long-term stability. Space-charge tracking is an N-body problem.", "map": "\\nu_x m+\\nu_y n=p", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0874", "a": "01-classical-mechanics/newtonian-mechanics/non-inertial-frames", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics", "name": "Rotating-frame physics of the planet", "kind": "mechanism", "summary": "Earth-system flows are best described in the rotating frame. Coriolis effects shape circulation, ocean gyres and inertial oscillations.", "map": "\\mathbf{a}_{rot}=\\mathbf{a}-2\\boldsymbol\\Omega\\times\\mathbf{v}-\\boldsymbol\\Omega\\times(\\boldsymbol\\Omega\\times\\mathbf{r})", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0875", "a": "01-classical-mechanics/newtonian-mechanics/non-inertial-frames", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Coriolis force and geostrophic balance", "kind": "mechanism", "summary": "The Coriolis force from Earth's rotation balances pressure gradients to give geostrophic wind and drives cyclone rotation and Rossby waves.", "map": "f\\,\\hat z\\times\\mathbf{u}_g=-\\nabla p/\\rho,\\; f=2\\Omega\\sin\\phi", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0876", "a": "01-classical-mechanics/newtonian-mechanics/non-inertial-frames", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Rossby waves from the beta effect", "kind": "mechanism", "summary": "The variation of the Coriolis parameter with latitude gives a restoring mechanism for planetary Rossby waves and westward phase propagation.", "map": "\\omega=Uk-\\beta k/(k^2+l^2)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0877", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/bifurcations-and-routes-to-chaos", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Tipping points as bifurcations", "kind": "analogy", "summary": "Climate tipping elements (ice-albedo, AMOC) are modelled as saddle-node bifurcations with hysteresis in energy-balance models. Early-warning signals come from critical slowing down.", "map": "C\\dot T=S(1-\\alpha(T))/4-\\epsilon\\sigma T^4", "breaks": "Real climate is forced, noisy and non-autonomous, so rate-induced tipping happens without a classical bifurcation.", "confidence": "current research", "strength": 2}
{"id": "C0878", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/bifurcations-and-routes-to-chaos", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics", "name": "AMOC bistability (Stommel model)", "kind": "mechanism", "summary": "Stommel's two-box model of thermohaline circulation has two stable states joined by saddle-node bifurcations, giving hysteresis and collapse scenarios.", "map": "\\dot S=F-|q(T-S)|S", "breaks": "Box models omit wind-driven and eddy dynamics, so whether the real AMOC is bistable is contested.", "confidence": "current research", "strength": 2}
{"id": "C0879", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics", "name": "Chaos limits climate and weather prediction", "kind": "mechanism", "summary": "Sensitivity to initial conditions bounds weather forecasts, motivating ensemble prediction. Climate is a boundary-value problem about statistics of the attractor.", "map": "\\delta(t)\\sim\\delta_0 e^{\\lambda t}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0880", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/atmospheric-dynamics", "name": "Lorenz chaos and weather predictability", "kind": "historical", "summary": "Lorenz's truncated convection model gave the first strange attractor. The result sets the finite predictability horizon of weather (~2 weeks), set by Lyapunov growth of errors.", "map": "\\dot x=\\sigma(y-x),\\;\\dot y=x(\\rho-z)-y,\\;\\dot z=xy-\\beta z", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0881", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "KAM tori and dynamic aperture", "kind": "mechanism", "summary": "Nonlinear magnet errors make betatron motion a perturbed Hamiltonian system. Resonance islands, chaotic layers and surviving KAM tori set the dynamic aperture and beam lifetime.", "map": "H=\\omega_x J_x+\\omega_y J_y+\\epsilon V(J,\\theta)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0882", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics", "name": "Solitons, tsunamis and internal waves", "kind": "shared object", "summary": "Shallow-water KdV solitons describe tsunamis and ocean internal solitary waves, balancing nonlinear steepening against dispersion.", "map": "u_t+6uu_x+u_{xxx}=0", "breaks": "Real waves have dissipation, rotation and variable bathymetry, so exact integrability is lost.", "confidence": "established", "strength": 2}
{"id": "C0883", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation", "b": "11-interdisciplinary-physics/biophysics/membranes-and-cell-mechanics", "name": "Reaction–diffusion patterning of cell polarity", "kind": "mechanism", "summary": "Cell polarity and motility waves on membranes (Min proteins, Rho GTPases) are excitable or Turing-type reaction–diffusion patterns.", "map": "\\partial_t c=D\\nabla^2 c+f(c)", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C0884", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation", "b": "11-interdisciplinary-physics/biophysics/physics-of-living-systems", "name": "Turing patterns and Kuramoto sync in biology", "kind": "mechanism", "summary": "Developmental patterning follows Turing reaction–diffusion instabilities, and neural and circadian rhythms follow Kuramoto-type phase locking.", "map": "\\dot\\theta_i=\\omega_i+\\tfrac{K}{N}\\sum_j\\sin(\\theta_j-\\theta_i)", "breaks": "Real gene networks are noisy and finite-sized, and Turing patterns need fine-tuned diffusivity ratios that biology rarely supplies.", "confidence": "current research", "strength": 2}
{"id": "C0885", "a": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Molecular vibrations as normal modes", "kind": "identity", "summary": "Molecular vibrational spectra are the normal modes of coupled atoms on a potential surface, found by diagonalising the mass-weighted Hessian, as for coupled springs.", "map": "\\det(\\mathbf{F}-\\omega^2\\mathbf{M})=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0886", "a": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Earth's free oscillations as normal modes", "kind": "mechanism", "summary": "After large earthquakes the Earth rings in toroidal and spheroidal normal modes. These are the eigenmodes of a continuum coupled-oscillator system and constrain the PREM structure.", "map": "\\mathcal{L}u=-\\omega^2\\rho u", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0887", "a": "01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators", "b": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "name": "Cavity resonance and Q factor in RF cavities", "kind": "identity", "summary": "Accelerator RF cavities are driven resonators characterised by Q and bandwidth, and superconducting cavities reach Q of 10^10 or more. Their response follows the driven damped oscillator.", "map": "Q=\\omega_0 U/P,\\;\\Delta\\omega=\\omega_0/Q", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0888", "a": "01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Larmor precession and resonance in MRI", "kind": "analogy", "summary": "Nuclear spin in MRI follows classical gyroscopic precession and driven resonance, with Bloch-equation relaxation like a damped driven oscillator (T1, T2).", "map": "\\omega_0=\\gamma B_0,\\;\\dot{\\mathbf M}=\\gamma\\mathbf M\\times\\mathbf B-\\ldots", "breaks": "Spin is quantum and the Bloch equations are linear only for ensemble magnetisation.", "confidence": "established", "strength": 2}
{"id": "C0889", "a": "01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/ocean-physics", "name": "Ocean waves, tides and dispersion", "kind": "shared object", "summary": "Surface gravity waves, internal waves and tides obey dispersion relations for fluid waves. The deep-water relation gives dispersive group and phase speeds.", "map": "\\omega^2=gk\\tanh(kh)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0890", "a": "01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Wave propagation in the Earth", "kind": "shared object", "summary": "Seismology applies reflection, refraction, impedance and dispersion of mechanical waves to layered media. Surface waves, free oscillations and travel-time inversion probe structure.", "map": "Z=\\rho v,\\; R=(Z_2-Z_1)/(Z_2+Z_1)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0891", "a": "01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics", "b": "11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics", "name": "Acoustics underlying ultrasound imaging", "kind": "shared object", "summary": "Echography relies on impedance mismatch reflection, attenuation, Doppler shift and beamforming of acoustic waves in tissue. Elastography uses shear wave speed to measure stiffness.", "map": "f_D=2f_0 v\\cos\\theta/c", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0892", "a": "01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics", "b": "11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics", "name": "Medical acoustics: impedance and Doppler", "kind": "shared object", "summary": "Ultrasound transducers, tissue attenuation and Doppler blood-flow measurement are applications of acoustic wave theory.", "map": "I_r/I_i=((Z_2-Z_1)/(Z_2+Z_1))^2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0893", "a": "01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Mathieu/Hill equation and strong focusing", "kind": "identity", "summary": "Betatron motion in an alternating-gradient lattice obeys Hill's equation, a periodically driven oscillator like Mathieu's. Stability bands match parametric resonance, and alternating focusing resembles Kapitza stabilisation.", "map": "x''+K(s)x=0,\\;K(s+L)=K(s)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0894", "a": "01-classical-mechanics/rigid-body-dynamics/gyroscopes-and-precession", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Gyroscope sensing, classical to atomic", "kind": "historical", "summary": "Mechanical gyroscopes sense rotation via angular momentum conservation, and atom-interferometric gyroscopes measure the same Sagnac-type rotation with matter waves at far higher sensitivity.", "map": "\\Delta\\phi=\\tfrac{4\\pi}{\\lambda v}\\,\\boldsymbol\\Omega\\cdot\\mathbf A", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C0895", "a": "01-classical-mechanics/rigid-body-dynamics/gyroscopes-and-precession", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Earth's precession, nutation and inner core", "kind": "shared object", "summary": "Precession and nutation of Earth's axis depend on its moment of inertia and on core structure, so the free core nutation constrains interior properties.", "map": "\\dot\\psi\\propto (C-A)/C", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0896", "a": "01-classical-mechanics/rigid-body-dynamics/rotational-dynamics-and-inertia-tensor", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Moment of inertia constrains density profile", "kind": "shared object", "summary": "Earth's moment of inertia factor (about 0.33) is a global constraint on radial density models such as PREM, showing a centrally condensed structure.", "map": "I=\\int\\rho r^2\\,dV=0.33\\,MR^2", "breaks": "", "confidence": "established", "strength": 2}