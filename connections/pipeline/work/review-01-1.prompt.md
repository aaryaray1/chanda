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

### Kinematics and Newton's laws · `knowledge/01-classical-mechanics/newtonian-mechanics/kinematics-and-newtons-laws`

**Scope.** Position/velocity/acceleration in Cartesian and polar coordinates, projectile motion, Newton's laws, contact forces, static and kinetic friction, linear and quadratic drag, terminal velocity, variable-mass systems (rockets), Galilean relativity.

**Core ideas.**
- The first law defines inertial frames; the second gives dynamics; the third gives momentum conservation.
- Draw a free-body diagram for each body; constraints supply extra equations.
- Drag is linear ($bv$) at low Reynolds number and quadratic ($\tfrac12C_D\rho Av^2$) at high.

**Key equations.**
$$\mathbf a=(\ddot r-r\dot\theta^2)\hat{\mathbf r}+(r\ddot\theta+2\dot r\dot\theta)\hat{\boldsymbol\theta},\qquad \Delta v=v_e\ln\frac{m_0}{m_f}\ (\text{rocket})$$

**See also.** [Conservation laws](knowledge/01-classical-mechanics/newtonian-mechanics/conservation-laws/README.md) · [Physics education research (misconceptions)](knowledge/00-foundations/history-and-philosophy-of-physics/physics-education-research/README.md)

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

# Packet 01-1 (100 records)

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
{"id": "C0458", "a": "01-classical-mechanics/analytical-mechanics", "b": "01-classical-mechanics/newtonian-mechanics", "name": "Newton to Lagrange via d'Alembert's principle", "kind": "identity", "summary": "For workless (ideal) constraints and potential forces, d'Alembert's principle of virtual work turns Newton's second law into the Euler–Lagrange equations in generalized coordinates and eliminates the constraint forces. Hamilton's principle restates the same dynamics as a variational principle.", "map": "\\sum_i(\\mathbf F_i-m_i\\ddot{\\mathbf r}_i)\\cdot\\delta\\mathbf r_i=0\\Rightarrow\\frac{d}{dt}\\frac{\\partial L}{\\partial\\dot q_k}=\\frac{\\partial L}{\\partial q_k}", "breaks": "Friction and nonholonomic constraints need Rayleigh dissipation functions or Lagrange multipliers; nonholonomic systems do not follow from a naive variational principle.", "confidence": "established", "strength": 3}
{"id": "C0459", "a": "01-classical-mechanics/analytical-mechanics", "b": "01-classical-mechanics/nonlinear-dynamics-and-chaos", "name": "Liouville–Arnold integrability and its generic failure", "kind": "identity", "summary": "An n-degree-of-freedom Hamiltonian with n independent integrals in involution moves quasi-periodically on invariant tori and has action–angle variables. Poincaré showed that generic systems lack such integrals, and the mixed regular–chaotic phase space that remains is the conservative half of nonlinear dynamics.", "map": "\\{F_i,F_j\\}=0\\ (i,j=1,\\dots,n)\\Rightarrow H=H(\\mathbf J),\\ \\dot{\\boldsymbol\\theta}=\\partial H/\\partial\\mathbf J", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0460", "a": "01-classical-mechanics/analytical-mechanics", "b": "01-classical-mechanics/rigid-body-dynamics", "name": "Rigid bodies as Lagrangian systems on SO(3)", "kind": "method transfer", "summary": "A body's orientation is a point of SO(3). With Euler angles as generalized coordinates, the heavy symmetric top's Lagrangian has cyclic φ and ψ, whose conjugate momenta L_z and L_3 (plus energy) make the top integrable and reduce it to one-dimensional motion in θ in an effective potential.", "map": "L=\\tfrac{I_1}{2}(\\dot\\theta^2+\\dot\\phi^2\\sin^2\\theta)+\\tfrac{I_3}{2}(\\dot\\psi+\\dot\\phi\\cos\\theta)^2-Mg\\ell\\cos\\theta", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0461", "a": "01-classical-mechanics/analytical-mechanics/canonical-transformations-and-hamilton-jacobi", "b": "01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos", "name": "Small divisors in canonical perturbation theory", "kind": "method transfer", "summary": "Canonical perturbation theory removes a perturbation with a generating function whose Fourier coefficients carry small divisors k·ω, which blow up at resonances. KAM replaces the divergent series with a superconvergent Newton iteration of canonical transformations. It converges for Diophantine frequencies and nondegenerate H_0, so most tori persist.", "map": "H=H_0(\\mathbf J)+\\epsilon H_1(\\mathbf J,\\boldsymbol\\theta),\\quad S_{1,\\mathbf k}=\\frac{iH_{1,\\mathbf k}(\\mathbf J)}{\\mathbf k\\cdot\\boldsymbol\\omega(\\mathbf J)}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0462", "a": "01-classical-mechanics/analytical-mechanics/canonical-transformations-and-hamilton-jacobi", "b": "01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators", "name": "Adiabatic invariant E/ω of a slowly varied oscillator", "kind": "identity", "summary": "In action–angle variables the oscillator's action is J=E/ω. When the frequency changes slowly compared with the period, J is an adiabatic invariant, with exponentially small changes for smooth variation. This was Einstein's 1911 Solvay answer to Lorentz's slowly shortened pendulum, and it is the classical root of Bohr–Sommerfeld quantization.", "map": "J=\\frac{1}{2\\pi}\\oint p\\,dq=\\frac{E}{\\omega},\\quad \\Delta J\\to0\\ \\text{as}\\ \\dot\\omega/\\omega^2\\to0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0463", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "name": "Point vortices: x and y as conjugate variables", "kind": "identity", "summary": "Kirchhoff showed that N point vortices in 2D ideal flow obey Hamilton's equations, with Γ_i x_i conjugate to y_i and a logarithmic interaction Hamiltonian. Configuration space is phase space, so a bounded domain has finite phase volume. Onsager used this to find negative-temperature states in which like-signed vortices cluster, a precursor of the 2D inverse cascade.", "map": "\\Gamma_i\\dot x_i=\\frac{\\partial H}{\\partial y_i},\\ \\Gamma_i\\dot y_i=-\\frac{\\partial H}{\\partial x_i},\\ H=-\\frac{1}{4\\pi}\\sum_{i<j}\\Gamma_i\\Gamma_j\\ln r_{ij}^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0464", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "01-classical-mechanics/newtonian-mechanics/central-forces-and-orbits", "name": "Kepler's hidden SO(4) symmetry", "kind": "identity", "summary": "The Laplace–Runge–Lenz vector is conserved for the 1/r potential. Together with L, its Poisson brackets close on so(4) for bound orbits, which makes Kepler motion superintegrable. This explains why bound orbits close and why the energy depends on only one combination of the actions.", "map": "\\mathbf A=\\mathbf p\\times\\mathbf L-mk\\hat{\\mathbf r},\\ \\{L_i,A_j\\}=\\epsilon_{ijk}A_k,\\ \\{A_i,A_j\\}=-2mH\\epsilon_{ijk}L_k", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0465", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos", "name": "Liouville's theorem: conservative vs dissipative chaos", "kind": "mechanism", "summary": "Hamiltonian flow preserves phase-space volume (Liouville), so Lyapunov exponents come in ± pairs and attractors cannot exist; chaos instead fills chaotic seas on the energy shell. Dissipative flows contract volume onto strange attractors, e.g. the Lorenz flow, which contracts at the constant rate σ+1+β.", "map": "\\nabla\\cdot\\dot{\\mathbf x}=0\\Rightarrow\\lambda_i=-\\lambda_{2n+1-i};\\quad\\text{Lorenz: }\\nabla\\cdot\\dot{\\mathbf x}=-(\\sigma+1+\\beta)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0466", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "name": "KdV as a Liouville-integrable Hamiltonian field theory", "kind": "identity", "summary": "KdV is a Hamiltonian field equation with the Gardner bracket ∂_x(δ/δu). Its infinitely many conserved quantities from inverse scattering Poisson-commute, and the scattering data serve as action–angle variables (Zakharov–Faddeev). This extends Liouville integrability to infinitely many degrees of freedom.", "map": "u_t=\\partial_x\\frac{\\delta H}{\\delta u},\\ H=\\int\\big(\\tfrac12u_x^2-u^3\\big)dx\\ \\Rightarrow\\ u_t+6uu_x+u_{xxx}=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0467", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "01-classical-mechanics/rigid-body-dynamics/euler-equations-and-tops", "name": "Euler's equations as a Lie–Poisson system on so(3)*", "kind": "identity", "summary": "Reducing T*SO(3) by rotation symmetry gives the Lie–Poisson bracket {L_i,L_j}=−ε_ijk L_k on the body angular momenta, in which Euler's equations are Hamiltonian. |L|² is a Casimir, so trajectories are intersections of the momentum sphere with the energy ellipsoid. The stable and unstable axes follow from the energy–Casimir method.", "map": "\\{F,G\\}=-\\mathbf L\\cdot(\\nabla F\\times\\nabla G),\\ \\dot{\\mathbf L}=\\mathbf L\\times\\mathsf I^{-1}\\mathbf L,\\ C=|\\mathbf L|^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0468", "a": "01-classical-mechanics/analytical-mechanics/lagrangian-mechanics", "b": "01-classical-mechanics/newtonian-mechanics/conservation-laws", "name": "Cyclic coordinates and Noether's conserved momenta", "kind": "identity", "summary": "In Lagrangian mechanics the Newtonian conservation laws of momentum, angular momentum and energy follow from invariance under translations, rotations and time translations. A coordinate absent from L has a conserved conjugate momentum, and an L with no explicit time dependence conserves the energy function h.", "map": "\\frac{\\partial L}{\\partial q_k}=0\\Rightarrow p_k=\\frac{\\partial L}{\\partial\\dot q_k}=\\text{const};\\ \\frac{\\partial L}{\\partial t}=0\\Rightarrow h=\\dot q_kp_k-L=\\text{const}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0469", "a": "01-classical-mechanics/analytical-mechanics/variational-principles", "b": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "name": "Kelvin's circulation theorem from relabelling symmetry", "kind": "identity", "summary": "Ideal barotropic flow follows from Hamilton's principle written in fluid-particle labels. The action is invariant under mass-preserving relabelling of parcels, and Noether's theorem for this infinite-dimensional symmetry gives Kelvin's circulation theorem and the conservation of potential vorticity.", "map": "\\delta\\!\\int\\!dt\\!\\int\\!d^3a\\,\\rho_0\\big[\\tfrac12|\\dot{\\mathbf x}|^2-e(\\rho)\\big]=0\\Rightarrow\\frac{d}{dt}\\oint_{C(t)}\\mathbf u\\cdot d\\mathbf l=0", "breaks": "Viscosity and non-conservative forcing destroy the variational structure and with it the theorem.", "confidence": "established", "strength": 3}
{"id": "C0470", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics", "name": "Elastic P, S and Rayleigh waves", "kind": "identity", "summary": "Navier's equations of linear elasticity admit compressional (P) and shear (S) waves, with speeds set by the Lamé moduli, plus Rayleigh surface waves at ≈0.92 c_S for Poisson ratio 0.25. Acoustics in solids is linear elastodynamics, the basis of seismology and ultrasonic testing.", "map": "\\rho\\ddot{\\mathbf u}=(\\lambda+2\\mu)\\nabla(\\nabla\\cdot\\mathbf u)-\\mu\\nabla\\times\\nabla\\times\\mathbf u,\\ c_P=\\sqrt{(\\lambda+2\\mu)/\\rho},\\ c_S=\\sqrt{\\mu/\\rho}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0471", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "01-classical-mechanics/rigid-body-dynamics/euler-equations-and-tops", "name": "Kirchhoff's kinetic analogy: elastic rod and spinning top", "kind": "analogy", "summary": "Kirchhoff showed that the equilibrium equations of a thin inextensible elastic rod are those of a heavy top, with arclength in place of time. Curvature–twist maps to angular velocity, bending and twisting stiffnesses map to moments of inertia, and end tension maps to gravity. The planar elastica is the pendulum equation, and helical rods are steady precessions.", "map": "s\\leftrightarrow t,\\ \\boldsymbol\\kappa(s)\\leftrightarrow\\boldsymbol\\omega(t),\\ (B,B,C)\\leftrightarrow(I_1,I_1,I_3),\\ \\mathbf F\\leftrightarrow Mg\\hat{\\mathbf z};\\ EI\\theta''+P\\sin\\theta=0", "breaks": "Rod shapes solve boundary-value problems in arclength (clamped or loaded ends), while tops solve initial-value problems in time. The analogy holds only for the statics of inextensible, unshearable rods and fails with self-contact, extensibility or shear.", "confidence": "established", "strength": 3}
{"id": "C0472", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "name": "KdV solitons from shallow-water Euler flow", "kind": "historical", "summary": "Scott Russell's 1834 solitary wave in a canal is an exact solution of the Korteweg–de Vries equation. KdV is derived from the ideal Euler equations for long, small-amplitude waves in shallow water, where weak nonlinearity balances weak dispersion. Deep-water waves instead give the nonlinear Schrödinger equation, envelope solitons and rogue-wave models.", "map": "\\eta_t+c_0\\eta_x+\\frac{3c_0}{2h}\\eta\\eta_x+\\frac{c_0h^2}{6}\\eta_{xxx}=0,\\quad c_0=\\sqrt{gh}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0473", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics", "name": "Sound as linearized compressible Euler flow", "kind": "identity", "summary": "Linearizing the compressible Euler and continuity equations about a uniform state gives the acoustic wave equation with c²=(∂p/∂ρ)_s. In a moving irrotational background the same perturbations propagate on Unruh's acoustic metric, the basis of analogue-gravity horizons. Viscosity and heat conduction add classical sound absorption.", "map": "\\partial_t^2\\rho'=c^2\\nabla^2\\rho',\\ c^2=(\\partial p/\\partial\\rho)_s;\\quad ds^2\\propto-c^2dt^2+(d\\mathbf x-\\mathbf v\\,dt)^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0474", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "01-classical-mechanics/rigid-body-dynamics/euler-equations-and-tops", "name": "Arnold: rigid body and ideal fluid as geodesics on groups", "kind": "identity", "summary": "Arnold (1966) showed that Euler's rigid-body equations are geodesic flow on SO(3) for the inertia metric, and that Euler's incompressible ideal-fluid equations are geodesic flow on the group of volume-preserving diffeomorphisms for the kinetic-energy metric. Both reduce to the same Euler–Arnold (Lie–Poisson) form, so energy–Casimir stability methods and curvature-based unpredictability estimates carry over between them.", "map": "\\text{top: }G=SO(3),\\ \\langle\\omega,\\mathsf I\\omega\\rangle;\\quad\\text{fluid: }G=\\mathrm{SDiff}(M),\\ \\int|\\mathbf u|^2dV;\\quad \\dot m=\\mathrm{ad}^*_{u}m", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0475", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "01-classical-mechanics/nonlinear-dynamics-and-chaos/bifurcations-and-routes-to-chaos", "name": "Convection as the testbed for routes to chaos", "kind": "mechanism", "summary": "Convection sets in at Ra_c≈1708 through a pitchfork bifurcation of the conducting state. In small-aspect-ratio cells, Libchaber and Maurer observed period-doubling cascades with ratios approaching Feigenbaum's δ, and other cells showed quasiperiodic and intermittent routes. Together these confirmed bifurcation universality in a real fluid.", "map": "\\delta=\\lim_{n\\to\\infty}\\frac{\\mu_n-\\mu_{n-1}}{\\mu_{n+1}-\\mu_n}=4.6692\\ldots,\\quad Ra_c\\approx1708\\ \\text{(rigid plates)}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0476", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos", "name": "Lorenz equations: a truncated Rayleigh–Bénard model", "kind": "historical", "summary": "Lorenz's three ODEs are a three-mode Galerkin truncation (after Saltzman) of 2D Boussinesq convection: x is the roll amplitude, y and z are temperature modes, ρ=Ra/Ra_c and σ is the Prandtl number. The strange attractor of this truncation launched modern chaos theory.", "map": "\\dot x=\\sigma(y-x),\\ \\dot y=x(\\rho-z)-y,\\ \\dot z=xy-\\beta z;\\quad \\rho=Ra/Ra_c,\\ \\sigma=Pr", "breaks": "Real convection near ρ≈28 is three-dimensional and far from three-mode; the equations are exact only for analogues such as the chaotic waterwheel and the single-mode laser.", "confidence": "established", "strength": 3}
{"id": "C0477", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation", "name": "Convection rolls as the paradigm of pattern formation", "kind": "shared object", "summary": "Rayleigh–Bénard convection above Ra_c≈1708 is the archetypal stationary pattern-forming instability (rolls, hexagons, Eckhaus and zigzag instabilities, spiral-defect chaos); near onset the roll envelope obeys the Ginzburg–Landau (Newell–Whitehead–Segel) amplitude equation, also derivable from the Swift–Hohenberg model.", "map": "\\partial_tA=\\epsilon A+\\xi_0^2\\partial_x^2A-g|A|^2A,\\quad \\epsilon=(Ra-Ra_c)/Ra_c", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0478", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/instabilities-and-convection", "b": "01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations", "name": "Faraday waves: Mathieu instability of a shaken fluid", "kind": "mechanism", "summary": "Shaking a liquid layer vertically modulates the effective gravity, so each surface-wave mode obeys a damped Mathieu equation (Benjamin–Ursell 1954). Above threshold the surface responds subharmonically, at half the drive frequency, and forms stripes, squares, hexagons and quasipatterns.", "map": "\\ddot a_k+\\gamma\\dot a_k+\\omega_k^2\\big[1-F\\cos\\Omega t\\big]a_k=0,\\ \\omega_k^2=gk\\tanh kh,\\ F=A\\Omega^2/g\\Rightarrow\\omega\\approx\\Omega/2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0479", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics", "b": "01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos", "name": "Chaotic advection: the stream function as Hamiltonian", "kind": "identity", "summary": "Tracer motion in a 2D incompressible flow is a one-degree-of-freedom Hamiltonian system, with the stream function as H and (x,y) as the conjugate pair. Time-periodic stirring makes it non-autonomous, so even laminar Stokes flows mix chaotically (Aref's chaotic advection). The KAM islands that survive stay unmixed, which sets the design principle of microfluidic mixers.", "map": "\\dot x=\\partial_y\\psi(x,y,t),\\ \\dot y=-\\partial_x\\psi(x,y,t)\\ \\leftrightarrow\\ \\dot q=\\partial_pH,\\ \\dot p=-\\partial_qH", "breaks": "Steady 3D flows are volume-preserving but not in general Hamiltonian; molecular diffusion eventually leaks across KAM-island barriers.", "confidence": "established", "strength": 3}
{"id": "C0480", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics", "b": "01-classical-mechanics/rigid-body-dynamics/rotational-dynamics-and-inertia-tensor", "name": "Falling cat and microswimmers: holonomy in shape space", "kind": "analogy", "summary": "A cat reorients with zero angular momentum, and a Stokes swimmer advances with zero inertia; both do it by cycling their shape. The net rotation or displacement is the holonomy of a connection on shape space, set to leading order by the area the stroke encloses (Shapere–Wilczek). Purcell's scallop theorem says a reciprocal, zero-area stroke gives no net motion.", "map": "\\Delta g=\\oint\\mathcal A(s)\\,ds=\\iint_S\\mathcal F+\\ldots;\\quad\\text{reciprocal stroke (zero area)}\\Rightarrow\\Delta g=0", "breaks": "The cat's connection comes from conserved (zero) angular momentum and its inertia tensor, an inertial constraint; the swimmer's comes from the viscous force-free and torque-free conditions, a dissipative one. The cat cannot shift its centre of mass, and the swimmer's displacement is independent of stroke rate only because inertia is absent.", "confidence": "established", "strength": 2}
{"id": "C0481", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "01-classical-mechanics/nonlinear-dynamics-and-chaos", "name": "Dynamical-systems routes to turbulence", "kind": "method transfer", "summary": "Bifurcation theory replaced Landau's picture of turbulence as an endless sequence of Hopf bifurcations. Ruelle and Takens predicted a strange attractor after only a few, which Gollub and Swinney confirmed in Taylor–Couette flow. Subcritical pipe-flow transition (Reynolds) is now framed through unstable exact coherent states, edge states and transient chaos.", "map": "\\text{Landau: }T^1\\to T^2\\to\\cdots\\to T^{\\infty};\\quad\\text{Ruelle–Takens: }T^1\\to T^2\\ (\\to T^3)\\to\\text{strange attractor}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0482", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos", "name": "Turbulence as high-dimensional deterministic chaos", "kind": "mechanism", "summary": "Turbulent flow is deterministic Navier–Stokes dynamics with positive Lyapunov exponents, so it is unpredictable beyond a few eddy times. The attractor dimension grows like the number of Kolmogorov-scale degrees of freedom, and the largest Lyapunov exponent scales with the inverse Kolmogorov time.", "map": "N_{\\rm dof}\\sim(L/\\eta)^3\\sim Re^{9/4},\\quad \\lambda_{\\max}\\sim\\tau_\\eta^{-1}", "breaks": "Low-dimensional attractor tools describe transition and small domains, not the developed multiscale cascade, which needs statistical (Kolmogorov) descriptions.", "confidence": "established", "strength": 3}
{"id": "C0483", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics", "name": "Lighthill's acoustic analogy: sound from turbulence", "kind": "mechanism", "summary": "Lighthill rearranged the exact flow equations into a wave equation driven by the turbulent Reynolds stress, which acts as a quadrupole source. It predicts that jet-noise power scales as U^8, with the radiated fraction of flow power ∝ Mach^5. This acoustic analogy founded aeroacoustics.", "map": "\\partial_t^2\\rho-c_0^2\\nabla^2\\rho=\\partial_i\\partial_jT_{ij},\\ T_{ij}\\approx\\rho u_iu_j;\\quad P_{\\rm ac}\\propto\\rho_0U^8L^2/c_0^5", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0484", "a": "01-classical-mechanics/newtonian-mechanics/central-forces-and-orbits", "b": "01-classical-mechanics/oscillations-and-waves/harmonic-and-damped-oscillators", "name": "Bertrand's theorem and the Kepler–oscillator duality", "kind": "duality", "summary": "Bertrand's theorem: among central potentials, only 1/r and r² make every bounded orbit close. The two are dual. The conformal map z=w² with a time reparametrization (Bohlin, Levi-Civita; Kustaanheimo–Stiefel in 3D) sends centred oscillator ellipses to focal Kepler ellipses and exchanges the roles of energy and coupling constant.", "map": "z=w^2,\\ dt\\propto|z|\\,d\\tau:\\ \\ddot z=-kz/|z|^3\\ (E<0)\\ \\leftrightarrow\\ w''=-\\omega^2w,\\ \\omega^2\\propto-E", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0485", "a": "01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics", "b": "01-classical-mechanics/nonlinear-dynamics-and-chaos/deterministic-chaos", "name": "Poincaré's three-body homoclinic tangle", "kind": "historical", "summary": "While correcting his 1889–90 prize memoir on the restricted three-body problem, Poincaré found that the stable and unstable manifolds of periodic orbits intersect transversally and fold into homoclinic tangles, the first recognition of deterministic chaos. Modern integrations show the inner Solar System is chaotic, with a Lyapunov time of ~5 Myr (Laskar).", "map": "W^s(\\gamma)\\pitchfork W^u(\\gamma)\\neq\\emptyset\\Rightarrow\\text{Smale horseshoe, positive topological entropy}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0486", "a": "01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics", "b": "01-classical-mechanics/nonlinear-dynamics-and-chaos/kam-theory-and-hamiltonian-chaos", "name": "Planetary stability: surviving tori and resonances", "kind": "shared object", "summary": "KAM theory grew out of the perturbed Kepler problem. For small planetary masses most quasi-periodic orbits survive as invariant tori (Arnold's planetary theorem), while mean-motion and secular resonances carve out chaotic zones such as the Kirkwood gap at the 3:1 resonance with Jupiter. Hénon and Heiles showed that a third integral breaks down for galactic orbits.", "map": "n_{\\rm ast}:n_{\\rm J}=3:1\\ (\\text{Kirkwood gap at }a\\approx2.50\\,\\mathrm{AU})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0487", "a": "01-classical-mechanics/newtonian-mechanics/few-body-and-celestial-mechanics", "b": "01-classical-mechanics/rigid-body-dynamics/gyroscopes-and-precession", "name": "Gyroscopic stabilization: L4/L5 and the fast top", "kind": "mechanism", "summary": "The triangular Lagrange points L4/L5 are maxima of the rotating-frame effective potential, yet they are linearly stable below Routh's mass ratio because the Coriolis force is gyroscopic. The same mechanism holds a fast top upright. By the Kelvin–Tait–Chetaev theorem, dissipation destroys such gyroscopic stability; drag, for example, makes Trojan orbits drift away.", "map": "M\\ddot{\\mathbf q}+G\\dot{\\mathbf q}+K\\mathbf q=0,\\ G^T=-G;\\quad \\mu<\\tfrac12\\big(1-\\sqrt{23/27}\\big)\\approx0.0385", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0488", "a": "01-classical-mechanics/newtonian-mechanics/non-inertial-frames", "b": "01-classical-mechanics/rigid-body-dynamics/euler-equations-and-tops", "name": "Euler's equations: Newton's law in the body frame", "kind": "identity", "summary": "Euler's equations are dL/dt=τ written in the co-rotating principal-axis frame using the transport theorem. The gyroscopic term ω×(Iω) is the rotational counterpart of the Coriolis and centrifugal terms that a particle feels in a rotating frame.", "map": "\\left(\\frac{d\\mathbf L}{dt}\\right)_{\\rm s}=\\left(\\frac{d\\mathbf L}{dt}\\right)_{\\rm b}+\\boldsymbol\\omega\\times\\mathbf L=\\boldsymbol\\tau", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0489", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/bifurcations-and-routes-to-chaos", "b": "01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations", "name": "Driven nonlinear oscillators: bifurcations to chaos", "kind": "mechanism", "summary": "The Mathieu instability tongues are bifurcations of the oscillator's rest state. The driven Duffing oscillator shows saddle-node (jump) bifurcations and hysteresis in its response curve. The driven damped pendulum and Duffing oscillator reach chaos through period-doubling cascades with Feigenbaum's universal ratio δ≈4.669.", "map": "\\ddot x+\\gamma\\dot x+\\omega_0^2x+\\beta x^3=F\\cos\\Omega t;\\quad \\delta=4.6692\\ldots", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0490", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/bifurcations-and-routes-to-chaos", "b": "01-classical-mechanics/rigid-body-dynamics/euler-equations-and-tops", "name": "Tennis-racket instability and the sleeping-top threshold", "kind": "mechanism", "summary": "Linearizing Euler's equations about a principal axis gives centres for the largest and smallest moments and a saddle for the intermediate one, whose heteroclinic orbits are the Dzhanibekov flips. A sleeping heavy top loses stability when its spin falls below threshold, through a Hamiltonian–Hopf (Krein collision) bifurcation.", "map": "\\ddot{\\delta\\omega}_1=\\frac{(I_2-I_3)(I_1-I_2)}{I_1I_3}\\Omega^2\\,\\delta\\omega_1;\\quad I_3^2\\omega_3^2>4Mg\\ell I_1", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0491", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems", "b": "01-classical-mechanics/oscillations-and-waves/coupled-oscillators-and-normal-modes", "name": "FPUT chain: normal modes, recurrence and solitons", "kind": "historical", "summary": "The Fermi–Pasta–Ulam–Tsingou anharmonic chain failed to share energy among its normal modes and showed near-recurrence. Zabusky and Kruskal took its continuum limit to the KdV equation and found solitons that pass through each other, which founded soliton theory. The chain lies close to the integrable Toda lattice.", "map": "\\ddot u_n=(u_{n+1}-2u_n+u_{n-1})[1+\\alpha(u_{n+1}-u_{n-1})]\\ \\to\\ u_t+uu_x+\\delta^2u_{xxx}=0", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0492", "a": "01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation", "b": "01-classical-mechanics/oscillations-and-waves/parametric-and-nonlinear-oscillations", "name": "Limit-cycle oscillators, entrainment and Arnold tongues", "kind": "mechanism", "summary": "A self-sustained (van der Pol) oscillator has a neutrally stable phase, so weak periodic forcing or coupling can lock it. The phase difference obeys the Adler equation, and the locking regions in the drive-amplitude–detuning plane are Arnold tongues. Populations of such oscillators show the Kuramoto synchronization transition.", "map": "\\dot\\phi=\\Delta\\omega-K\\sin\\phi\\ (\\text{locked if }|\\Delta\\omega|<K);\\quad \\dot\\theta_i=\\omega_i+\\frac{K}{N}\\sum_j\\sin(\\theta_j-\\theta_i)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C0493", "a": "01-classical-mechanics/analytical-mechanics/canonical-transformations-and-hamilton-jacobi", "b": "02-electromagnetism-and-optics/classical-optics/fourier-optics-and-imaging", "name": "Linear canonical transforms in Fresnel optics", "kind": "identity", "summary": "Paraxial propagation through any ABCD system is the Collins integral, which is the wave (metaplectic) representation of the linear canonical transformation given by the symplectic ray matrix. Free space acts as a Fresnel transform and a thin lens as a quadratic phase. A graded-index medium, whose ray Hamiltonian is a harmonic oscillator, performs a fractional Fourier transform that becomes the full Fourier transform after a quarter period.", "map": "U_2(x)\\propto\\int U_1(x')\\,e^{\\frac{i\\pi}{\\lambda B}(Ax'^2-2xx'+Dx^2)}dx';\\ \\text{GRIN }n=n_0(1-\\tfrac12g^2r^2):\\ \\text{FT at }L=\\frac{\\pi}{2g}", "breaks": "The correspondence is exact only in the paraxial limit. Aberrations make the ray map nonlinear, and the wave propagator then stops being a simple metaplectic integral.", "confidence": "established", "strength": 2}
{"id": "C0494", "a": "01-classical-mechanics/analytical-mechanics/canonical-transformations-and-hamilton-jacobi", "b": "02-electromagnetism-and-optics/classical-optics/geometric-optics", "name": "Eikonal equation is the Hamilton–Jacobi equation", "kind": "identity", "summary": "The wavefronts S=const of the eikonal equation |∇S|²=n² are level sets of Hamilton's characteristic function, and rays are its characteristics. Hamilton built this characteristic-function method for optics and carried it over to dynamics in 1834–35. Schrödinger later completed this optico-mechanical analogy into wave mechanics.", "map": "|\\nabla S|^2=n^2(\\mathbf r)\\ \\leftrightarrow\\ |\\nabla W|^2=2m(E-V);\\quad \\text{rays}\\parallel\\nabla S\\ \\leftrightarrow\\ \\mathbf p=\\nabla W", "breaks": "Both solutions become multivalued at caustics and focal points. There geometric optics fails, and diffraction (or Maslov phases, in semiclassics) must be added.", "confidence": "established", "strength": 3}
{"id": "C0495", "a": "01-classical-mechanics/analytical-mechanics/hamiltonian-mechanics", "b": "02-electromagnetism-and-optics/classical-optics/geometric-optics", "name": "Ray optics as Hamiltonian flow; étendue as Liouville", "kind": "identity", "summary": "If the optical axis z is taken as time, rays obey Hamilton's equations with H=−√(n²−p²) and transverse momentum p=n sinθ. Paraxial ABCD matrices are symplectic in the reduced variables (y, nθ). Conservation of étendue and radiance is Liouville's theorem, and it caps solar concentration at n²/sin²θ_sun.", "map": "H=-\\sqrt{n^2(\\mathbf q,z)-\\mathbf p^2};\\ M^TJM=J\\ (\\det M=1\\text{ in }(y,n\\theta));\\ n^2\\,dA\\,d\\Omega=\\text{const}", "breaks": "Liouville's theorem holds only for lossless systems without scattering. Diffraction blurs the phase-space picture at the scale of λ, where the Wigner function replaces the ray density.", "confidence": "established", "strength": 3}
{"id": "C0496", "a": "01-classical-mechanics/analytical-mechanics/lagrangian-mechanics", "b": "02-electromagnetism-and-optics/electrodynamics/potentials-and-gauge-invariance", "name": "Charged-particle Lagrangian and minimal coupling", "kind": "identity", "summary": "The Lorentz force follows from Lagrange's equations with the velocity-dependent potential U=q(φ−v·A), and the canonical momentum p=mv+qA differs from the kinetic momentum. A gauge transformation adds the total derivative q dχ/dt to L and leaves the motion unchanged. This is the classical root of gauge invariance and of the Aharonov–Bohm phase q∮A·dl/ħ.", "map": "L=\\tfrac12mv^2-q\\phi+q\\mathbf v\\cdot\\mathbf A;\\ \\mathbf p=m\\mathbf v+q\\mathbf A;\\ H=\\frac{(\\mathbf p-q\\mathbf A)^2}{2m}+q\\phi;\\ L\\to L+q\\frac{d\\chi}{dt}", "breaks": "Classically only the fields matter. That the potentials themselves have physical effects (the Aharonov–Bohm effect) appears only in quantum mechanics.", "confidence": "established", "strength": 3}
{"id": "C0497", "a": "01-classical-mechanics/analytical-mechanics/variational-principles", "b": "02-electromagnetism-and-optics/classical-optics/geometric-optics", "name": "Fermat's principle and the principle of least action", "kind": "identity", "summary": "Light rays make the optical path stationary in the same way that mechanical trajectories make the action stationary. In Maupertuis' form δ∫p ds=0, ray optics maps onto mechanics with the refractive index in the role of momentum, so Snell's law becomes conservation of momentum parallel to the interface.", "map": "\\delta\\int n\\,ds=0\\ \\leftrightarrow\\ \\delta\\int\\sqrt{2m(E-V)}\\,ds=0;\\quad n(\\mathbf r)\\leftrightarrow|\\mathbf p(\\mathbf r)|", "breaks": "The map holds at fixed energy, which means a single frequency. The particle's speed is proportional to n, while light's phase velocity is c/n. Hamilton and de Broglie resolved this mismatch by distinguishing phase velocity from group velocity.", "confidence": "established", "strength": 3}
{"id": "C0498", "a": "01-classical-mechanics/analytical-mechanics/variational-principles", "b": "02-electromagnetism-and-optics/electrodynamics/relativistic-electrodynamics", "name": "Maxwell's equations from a field action", "kind": "method transfer", "summary": "Extending Hamilton's principle to fields, the inhomogeneous Maxwell equations come out as the Euler–Lagrange equations of the covariant action, and the homogeneous pair is the Bianchi identity of F=dA. Noether's theorem applied to this action gives the energy–momentum tensor. Gauge invariance of the coupling forces charge conservation.", "map": "S=\\int\\Big(-\\frac{1}{4\\mu_0}F_{\\mu\\nu}F^{\\mu\\nu}-A_\\mu J^\\mu\\Big)d^4x\\ \\Rightarrow\\ \\partial_\\mu F^{\\mu\\nu}=\\mu_0J^\\nu,\\ \\partial_\\mu J^\\mu=0", "breaks": "The canonical Noether tensor is neither symmetric nor gauge invariant and needs the Belinfante improvement. The action also does not settle radiation reaction for point charges.", "confidence": "established", "strength": 2}
{"id": "C0499", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "02-electromagnetism-and-optics/classical-optics/polarization-and-crystal-optics", "name": "Photoelasticity: stress made visible by birefringence", "kind": "method transfer", "summary": "Stress makes a transparent solid birefringent in proportion to the difference of principal stresses (the stress-optic law, Brewster 1816). Viewed between crossed polarizers, a loaded model shows isochromatic fringes of σ1−σ2 and isoclinics along the principal directions, the classic tool of experimental stress analysis. The same photoelastic tensor drives acousto-optic modulators.", "map": "\\Delta n=C(\\sigma_1-\\sigma_2),\\quad \\delta=\\frac{2\\pi t}{\\lambda}C(\\sigma_1-\\sigma_2),\\quad I\\propto\\sin^22\\theta\\,\\sin^2\\frac{\\delta}{2}", "breaks": "The method gives only stress differences and directions integrated through the thickness. Separating the individual principal stresses, or handling 3D bodies, needs extra methods such as stress freezing or scattered-light photoelasticity.", "confidence": "established", "strength": 3}
{"id": "C0500", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/elasticity", "b": "02-electromagnetism-and-optics/electrodynamics/maxwells-equations", "name": "Elastic-solid aether and the Maxwell stress tensor", "kind": "historical", "summary": "Fresnel's transverse light waves led Cauchy, Green and MacCullagh to model light as waves in an elastic solid, and MacCullagh's rotationally elastic aether gave equations equivalent to Maxwell's in vacuum. Maxwell expressed electromagnetic forces as stresses in a medium. That is the origin of the stress tensor whose divergence gives the force density.", "map": "T_{ij}=\\varepsilon_0\\big(E_iE_j-\\tfrac12\\delta_{ij}E^2\\big)+\\frac{1}{\\mu_0}\\big(B_iB_j-\\tfrac12\\delta_{ij}B^2\\big)\\ \\leftrightarrow\\ \\sigma_{ij}", "breaks": "An ordinary elastic solid also carries longitudinal waves, which light lacks; this problem sank most elastic-aether theories. Relativity later removed the medium altogether.", "confidence": "established", "strength": 2}
{"id": "C0501", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/magnetostatics", "name": "Vortex Biot–Savart law: vorticity as current", "kind": "identity", "summary": "An incompressible velocity field obeys ∇·u=0 and ∇×u=ω, the same equations as B with source μ0J. Vortex lines therefore induce velocity by the Biot–Savart law: a line vortex acts like a straight wire and a vortex ring like a current loop. Maxwell's 1861 molecular-vortex model ran the analogy the other way, to picture magnetic fields.", "map": "\\mathbf u=\\frac{1}{4\\pi}\\int\\frac{\\boldsymbol\\omega'\\times\\mathbf R}{R^3}dV'\\ \\leftrightarrow\\ \\mathbf B=\\frac{\\mu_0}{4\\pi}\\int\\frac{\\mathbf J'\\times\\mathbf R}{R^3}dV',\\ \\mathbf R=\\mathbf r-\\mathbf r'", "breaks": "Vorticity is carried along and stretched by the velocity it induces (Helmholtz's laws), so vortex dynamics is nonlinear, whereas currents are prescribed. Parallel vortices of the same sign orbit each other instead of attracting the way parallel currents do.", "confidence": "established", "strength": 3}
{"id": "C0502", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "02-electromagnetism-and-optics/photonics-and-lasers/integrated-and-fiber-photonics", "name": "Analogue event horizons in flows and optical fibres", "kind": "analogy", "summary": "Sound in an irrotational flow travels on an effective acoustic metric, with a horizon where the flow outruns sound. In a fibre, the Kerr index front of a soliton moving at the group velocity acts as a horizon for probe light. Both therefore serve as analogue-gravity platforms for Hawking-type mode conversion.", "map": "ds^2\\propto-(c_s^2-v^2)dt^2-2\\mathbf v\\cdot d\\mathbf x\\,dt+d\\mathbf x^2;\\quad \\text{horizon at }|v|=c_s", "breaks": "Both rely on dispersion near the horizon. The fibre horizon is a moving index perturbation in a dispersive medium, not a flow, and claims of spontaneous Hawking-like emission in optics remain debated.", "confidence": "current research", "strength": 2}
{"id": "C0503", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/ideal-and-viscous-flow", "b": "02-electromagnetism-and-optics/photonics-and-lasers/nonlinear-optics", "name": "Hydrodynamics of light via the Madelung transform", "kind": "analogy", "summary": "Writing the paraxial Kerr field as √ρ e^{iφ} turns the NLS into continuity and Euler equations for a compressible fluid. The nonlinearity supplies a pressure, and diffraction supplies a dispersive 'quantum pressure'. Defocusing media then show superfluid-like flow of light, optical vortices, and dispersive shock waves similar to undular bores.", "map": "A=\\sqrt\\rho\\,e^{i\\phi},\\ \\mathbf v=\\nabla_\\perp\\phi/k:\\ \\ \\partial_z\\rho+\\nabla_\\perp\\!\\cdot(\\rho\\mathbf v)=0,\\ \\ \\partial_z\\mathbf v+(\\mathbf v\\cdot\\nabla)\\mathbf v=-\\nabla(P_{NL}+Q)", "breaks": "Propagation distance plays the role of time, and the fluid is inviscid with dispersion as its only regularization, so its shocks are oscillatory rather than viscous. Absorption and nonlocal nonlinearity break the analogy.", "confidence": "current research", "strength": 2}
{"id": "C0504", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/low-reynolds-number-and-microfluidics", "b": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "name": "Optical tweezers: Rayleigh-dipole force in a Stokes fluid", "kind": "method transfer", "summary": "A small dielectric bead is a Rayleigh scatterer. Its induced dipole is pulled up the intensity gradient while radiation pressure pushes it along the beam. In water it moves as an overdamped Brownian particle with Stokes drag, so the trap stiffness can be calibrated from the Lorentzian corner frequency. This makes tweezers a force probe for microfluidics and biophysics.", "map": "\\mathbf F_{grad}=\\frac{\\alpha'}{4}\\nabla|\\mathbf E_0|^2,\\quad \\gamma=6\\pi\\eta a,\\quad f_c=\\frac{\\kappa}{2\\pi\\gamma}", "breaks": "Beads comparable to λ need Mie or ray-optics force calculations. Near walls the Stokes drag increases (Faxén corrections).", "confidence": "established", "strength": 2}
{"id": "C0505", "a": "01-classical-mechanics/continuum-and-fluid-mechanics/turbulence", "b": "02-electromagnetism-and-optics/classical-optics/coherence-and-statistical-optics", "name": "Atmospheric seeing: Kolmogorov turbulence limits coherence", "kind": "mechanism", "summary": "Kolmogorov scaling of temperature fluctuations makes the refractive-index structure function grow as r^(2/3), so starlight picks up a phase structure function proportional to (r/r0)^(5/3). The Fried parameter r0 sets the spatial coherence length and limits telescope resolution to about λ/r0. The result is speckle, which motivated speckle interferometry and adaptive optics.", "map": "D_n(r)=C_n^2r^{2/3},\\ \\ D_\\phi(r)=6.88\\Big(\\frac{r}{r_0}\\Big)^{5/3},\\ \\ r_0=\\Big[0.423k^2\\sec\\zeta\\!\\int C_n^2dh\\Big]^{-3/5}", "breaks": "Real atmospheric turbulence has finite outer and inner scales and is intermittent, so the 5/3 law fails at the largest and smallest separations.", "confidence": "established", "strength": 3}
{"id": "C0506", "a": "01-classical-mechanics/newtonian-mechanics/central-forces-and-orbits", "b": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/electrostatics-and-boundary-value-problems", "name": "Inverse-square law: Kepler orbits and Coulomb fields", "kind": "identity", "summary": "Newtonian gravity and electrostatics share Poisson's equation and the 1/r Green's function. Gauss's law, the shell theorem and the conserved Runge–Lenz vector therefore carry over between them. Rutherford scattering is the hyperbolic Kepler orbit in a repulsive Coulomb field.", "map": "\\nabla^2\\Phi=4\\pi G\\rho\\ \\leftrightarrow\\ \\nabla^2\\phi=-\\rho/\\varepsilon_0;\\ GMm\\leftrightarrow-\\frac{qQ}{4\\pi\\varepsilon_0};\\ \\frac{d\\sigma}{d\\Omega}=\\Big(\\frac{k}{4E}\\Big)^2\\frac{1}{\\sin^4(\\theta/2)}", "breaks": "Gravity has only one sign of charge, so it has no screening, no dipole radiation and no gravitational conductor. Gravitational charge also equals inertial mass, which has no electric counterpart.", "confidence": "established", "strength": 2}
{"id": "C0507", "a": "01-classical-mechanics/newtonian-mechanics/central-forces-and-orbits", "b": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "name": "Larmor radiation and the collapse of classical atoms", "kind": "historical", "summary": "An electron on a classical Kepler orbit around a nucleus radiates at the Larmor rate and spirals inward within about 10⁻¹¹ s. This failure of Rutherford's planetary atom motivated Bohr's stationary orbits. The same radiative decay of orbits shapes cyclotron and synchrotron motion.", "map": "P=\\frac{q^2a^2}{6\\pi\\varepsilon_0c^3},\\quad t_{fall}=\\frac{a_0^3}{4r_e^2c}\\approx1.6\\times10^{-11}\\,\\text{s}", "breaks": "In quantum mechanics there is no continuous inspiral. Stationary states replace it, and radiation occurs only in transitions at discrete frequencies.", "confidence": "established", "strength": 2}
{"id": "C0508", "a": "01-classical-mechanics/newtonian-mechanics/conservation-laws", "b": "02-electromagnetism-and-optics/electrodynamics/maxwells-equations", "name": "Field momentum restores momentum conservation", "kind": "mechanism", "summary": "Magnetic forces between moving charges violate Newton's third law, so mechanical momentum alone is not conserved. Maxwell's theory restores conservation of linear and angular momentum by giving the field a momentum density ε0E×B and a stress tensor. Feynman's disk paradox and hidden momentum are standard examples.", "map": "\\frac{d}{dt}\\Big(\\mathbf p_{mech}+\\varepsilon_0\\!\\int\\mathbf E\\times\\mathbf B\\,dV\\Big)_i=\\oint T_{ij}\\,da_j", "breaks": "Inside matter, how momentum splits between the field and the medium is ambiguous; this is the Abraham–Minkowski controversy.", "confidence": "established", "strength": 3}
{"id": "C0509", "a": "01-classical-mechanics/newtonian-mechanics/kinematics-and-newtons-laws", "b": "02-electromagnetism-and-optics/electrodynamics/relativistic-electrodynamics", "name": "Galilean kinematics vs Lorentz-covariant electrodynamics", "kind": "historical", "summary": "Maxwell's equations are not invariant under Galilean boosts, as the magnet-and-conductor asymmetry and the fixed speed of light show. Resolving this clash with Newtonian kinematics produced the Lorentz transformations and Einstein's 1905 relativity. Under relativity, Newton's second law becomes the covariant Lorentz-force equation.", "map": "x'=x-vt\\ \\to\\ x'=\\gamma(x-vt),\\ t'=\\gamma(t-vx/c^2);\\quad \\frac{dp^\\mu}{d\\tau}=qF^{\\mu\\nu}u_\\nu", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C0510", "a": "01-classical-mechanics/newtonian-mechanics/non-inertial-frames", "b": "02-electromagnetism-and-optics/classical-optics/polarization-and-crystal-optics", "name": "Foucault pendulum and Rytov rotation: one holonomy", "kind": "identity", "summary": "Each day, the Foucault pendulum's swing plane turns by the solid angle 2π(1−cosϑ) enclosed by the local vertical, where ϑ is the colatitude; this is parallel transport on a sphere. The polarization of light in a helically coiled fibre rotates by the solid angle swept by its propagation direction (the Rytov–Vladimirskii rotation, observed by Tomita and Chiao). Both are the same geometric phase.", "map": "\\Delta\\varphi=\\Omega_{solid}=2\\pi(1-\\cos\\vartheta)\\ \\ (\\equiv-2\\pi\\cos\\vartheta\\ \\mathrm{mod}\\ 2\\pi)", "breaks": "The pendulum carries a classical vector across Earth's surface. For photons the rotation is a helicity-dependent Berry phase ±σΩ, with opposite signs for the two circular polarizations.", "confidence": "established", "strength": 2}
{"id": "C0511", "a": "01-classical-mechanics/newtonian-mechanics/non-inertial-frames", "b": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/magnetostatics", "name": "Larmor's theorem: Coriolis force mimics a magnetic field", "kind": "identity", "summary": "In a frame rotating at Ω, the Coriolis force 2m v×Ω has the same form as the magnetic force q v×B. Rotating at Ω=−qB/2m therefore removes a weak uniform field to first order, which explains the Larmor precession of orbits and atomic diamagnetism. Conversely, rotating neutral systems can simulate magnetic fields.", "map": "2m\\,\\mathbf v\\times\\boldsymbol\\Omega\\ \\leftrightarrow\\ q\\,\\mathbf v\\times\\mathbf B:\\quad \\mathbf B_{eff}=\\frac{2m}{q}\\boldsymbol\\Omega,\\quad \\boldsymbol\\Omega_L=-\\frac{q\\mathbf B}{2m}", "breaks": "The equivalence holds only to first order. The rotating frame adds a centrifugal force of order Ω² with no magnetic counterpart, which must be small or cancelled by a trap.", "confidence": "established", "strength": 3}