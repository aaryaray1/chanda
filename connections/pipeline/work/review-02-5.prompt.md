You are the em-optics-physicist, the specialist for 02 (Electromagnetism and Optics) in this physics knowledge base.

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

## Field overview · `knowledge/02-electromagnetism-and-optics`

> **Specialist:** `em-optics-physicist` · **arXiv:** physics.class-ph, physics.optics, physics.app-ph · **Literature source:** OpenAlex + arXiv

#### What this field studies
Maxwell's four equations, with the Lorentz force law, describe all classical electric, magnetic and optical phenomena — from capacitors to radio, from rainbows to lasers. Light is an electromagnetic wave; optics is electromagnetism at wavelengths from ~400 to ~700 nm (and beyond). Modern photonics engineers light in structured materials, generates attosecond pulses, and carries the world's data through optical fibre.

#### Conventions used in this branch
- **SI units** by default ($\epsilon_0$, $\mu_0$, $c^2=1/\epsilon_0\mu_0$). Jackson and many plasma/astro texts use **Gaussian** units: $\mathbf F=q(\mathbf E+\frac{\mathbf v}{c}\times\mathbf B)$, $\nabla\cdot\mathbf E=4\pi\rho$. Always state which.
- Time-harmonic fields as $\mathrm{Re}[\mathbf E_0e^{i(\mathbf k\cdot\mathbf r-\omega t)}]$ (physics convention); engineers use $e^{j\omega t}$ — signs of imaginary parts flip.
- Refractive index $n=\sqrt{\epsilon_r\mu_r}$; complex $\tilde n=n+i\kappa$ with absorption.

#### Historical spine
1785 Coulomb's law · 1820 Ørsted, Biot–Savart, Ampère · 1831 Faraday's induction · 1865 Maxwell's dynamical theory · 1887 Hertz detects radio waves · 1897 Larmor formula · 1905 special relativity from electrodynamics · 1934 Cherenkov radiation · 1948 holography · 1960 the laser · 1961 second-harmonic generation · 1966 low-loss optical fibre proposed · 1985 chirped-pulse amplification · 2000 negative-index metamaterials · 2001 attosecond pulses · 2009 topological photonic edge states · 2023 Nobel Prize for attosecond physics.

#### Canonical textbooks
- Griffiths, *Introduction to Electrodynamics* — undergraduate standard.
- Jackson, *Classical Electrodynamics* — the graduate reference (Gaussian in 2nd ed., SI in early chapters of 3rd).
- Zangwill, *Modern Electrodynamics* — modern graduate alternative.
- Hecht, *Optics*; Born & Wolf, *Principles of Optics*; Saleh & Teich, *Fundamentals of Photonics*; Boyd, *Nonlinear Optics*; Siegman, *Lasers*.

#### Live frontiers
- Attosecond science and petahertz electronics.
- Integrated photonics for quantum and AI hardware; frequency microcombs.
- Topological, non-Hermitian and time-varying photonic media.

#### How the specialist works here
Exploit symmetry (Gauss, Ampère), choose the right potential formulation and gauge, check boundary conditions at every interface, verify with energy conservation (Poynting) and limiting cases ($\omega\to0$, far field, $v\ll c$), and be explicit about units.

## Classical optics · `knowledge/02-electromagnetism-and-optics/classical-optics`

#### Overview
When wavelengths are small compared with apertures, light travels as rays (geometric optics). When they are not, interference and diffraction take over (wave optics). Fourier optics treats imaging as linear filtering of spatial frequencies, sets the diffraction limit, and explains how super-resolution techniques evade it.

#### Key equations
$$n_1\sin\theta_1=n_2\sin\theta_2,\qquad \frac1{s_o}+\frac1{s_i}=\frac1f,\qquad \theta_{\min}\approx1.22\frac{\lambda}{D},\qquad d\sin\theta=m\lambda$$

#### Connections
- [Quantized light and photon statistics](knowledge/04-quantum-physics/quantum-optics/quantized-light-and-photon-statistics/README.md) · [Medical imaging](knowledge/11-interdisciplinary-physics/medical-physics/medical-imaging/README.md)

### Coherence and statistical optics · `knowledge/02-electromagnetism-and-optics/classical-optics/coherence-and-statistical-optics`

**Scope.** First-order coherence $g^{(1)}(\tau)$, coherence time and length, Wiener–Khinchin theorem, spatial coherence and van Cittert–Zernike theorem, stellar interferometry, speckle statistics, Hanbury Brown–Twiss intensity interferometry, optical coherence tomography, partially coherent beams.

**Core ideas.**
- Coherence time $\tau_c\sim1/\Delta\nu$: narrow spectra mean long coherence.
- The spatial coherence of light from an incoherent source is the Fourier transform of its intensity distribution — how stellar diameters are measured.
- HBT correlations revealed photon bunching and launched quantum optics.

**Key equations.**
$$S(\omega)=\int g^{(1)}(\tau)e^{i\omega\tau}d\tau,\qquad \ell_c=c\,\tau_c\approx\frac{\lambda^2}{\Delta\lambda}$$

**See also.** [Photon statistics](knowledge/04-quantum-physics/quantum-optics/quantized-light-and-photon-statistics/README.md)

### Fourier optics and imaging · `knowledge/02-electromagnetism-and-optics/classical-optics/fourier-optics-and-imaging`

**Scope.** Lenses as Fourier transformers, 4f systems and spatial filtering, point-spread function, OTF/MTF, Abbe and Rayleigh resolution limits, phase-contrast (Zernike) microscopy, holography, adaptive optics, computational imaging, STED, PALM/STORM, structured illumination, interferometric synthesis imaging.

**Core ideas.**
- A lens's back focal plane holds the Fourier transform of the input field.
- Far-field imaging resolution is limited to ~$\lambda/(2\,\text{NA})$ (Abbe).
- Super-resolution exploits nonlinear switching or single-molecule localization, not better lenses.

**Key equations.**
$$U_f(u,v)\propto\iint U_0(x,y)\,e^{-i\frac{2\pi}{\lambda f}(ux+vy)}dx\,dy,\qquad d_{\text{Abbe}}=\frac{\lambda}{2n\sin\alpha}$$

**See also.** [Black-hole imaging (VLBI)](knowledge/05-relativity-and-gravitation/black-holes/black-hole-imaging-and-astrophysical-black-holes/README.md) · [Medical imaging](knowledge/11-interdisciplinary-physics/medical-physics/medical-imaging/README.md)

### Geometric optics · `knowledge/02-electromagnetism-and-optics/classical-optics/geometric-optics`

**Scope.** Fermat's principle, Snell's law, total internal reflection, thin and thick lenses, mirrors, magnification, ABCD ray-transfer matrices, telescopes and microscopes, chromatic and Seidel aberrations, gradient-index optics, mirages, rainbows, gravitational lensing analogy.

**Core ideas.**
- Valid when $\lambda\ll$ all relevant lengths; it is the eikonal (short-wavelength) limit of wave optics.
- Paraxial systems compose by matrix multiplication.
- Rainbows: minimum-deviation rays in water drops (~42°), dispersed by wavelength.

**Key equations.**
$$\begin{pmatrix}y_2\\\theta_2\end{pmatrix}=\begin{pmatrix}1&0\\-1/f&1\end{pmatrix}\begin{pmatrix}y_1\\\theta_1\end{pmatrix},\qquad \frac{1}{f}=(n-1)\left(\frac{1}{R_1}-\frac{1}{R_2}\right)$$

**See also.** [Variational principles](knowledge/01-classical-mechanics/analytical-mechanics/variational-principles/README.md)

### Interference and diffraction · `knowledge/02-electromagnetism-and-optics/classical-optics/interference-and-diffraction`

**Scope.** Young's double slit, thin-film interference and anti-reflection coatings, Michelson, Mach–Zehnder and Fabry–Pérot interferometers, finesse, Huygens–Fresnel principle, single-slit and circular-aperture diffraction (Airy pattern), gratings and resolving power, Fresnel zones, Babinet's principle.

**Core ideas.**
- Interference needs coherence; fringe visibility measures it.
- Fraunhofer (far-field) diffraction pattern = Fourier transform of the aperture.
- A grating with $N$ illuminated lines resolves $\lambda/\Delta\lambda=mN$.

**Key equations.**
$$I(\theta)=I_0\left[\frac{\sin(\beta)}{\beta}\right]^2,\ \beta=\frac{\pi a\sin\theta}{\lambda};\qquad T_{\text{FP}}=\frac{1}{1+F\sin^2(\delta/2)}$$

**See also.** [Gravitational-wave interferometers](knowledge/05-relativity-and-gravitation/gravitational-waves/ground-based-detections/README.md) · [Fourier optics](knowledge/02-electromagnetism-and-optics/classical-optics/fourier-optics-and-imaging/README.md)

### Polarization and crystal optics · `knowledge/02-electromagnetism-and-optics/classical-optics/polarization-and-crystal-optics`

**Scope.** Linear, circular and elliptical polarization, Jones vectors and matrices, Stokes parameters and the Poincaré sphere, Malus's law, polarizers, wave plates, uniaxial and biaxial crystals, birefringence, optical activity and Faraday rotation, Pockels and Kerr effects, liquid-crystal displays.

**Core ideas.**
- Any polarization is a superposition of two orthogonal states — the same math as a qubit.
- Anisotropic crystals have direction-dependent index; a quarter-wave plate converts linear to circular polarization.
- Faraday rotation is non-reciprocal (enables optical isolators); optical activity is reciprocal.

**Key equations.**
$$I=I_0\cos^2\theta,\qquad \Gamma=\frac{2\pi}{\lambda}(n_e-n_o)d,\qquad \theta_F=VBL$$

**See also.** [Liquid crystals](knowledge/08-condensed-matter/soft-matter/liquid-crystals/README.md) · [Qubits and entanglement](knowledge/04-quantum-physics/quantum-information-and-computation/entanglement-theory/README.md)

## Electrodynamics · `knowledge/02-electromagnetism-and-optics/electrodynamics`

#### Overview
Faraday's induction and Maxwell's displacement current couple $\mathbf E$ and $\mathbf B$ into self-sustaining waves travelling at $c=1/\sqrt{\epsilon_0\mu_0}$. Maxwell's theory was the first relativistic field theory, the first gauge theory, and the model for every field theory since.

#### Key equations
$$\nabla\cdot\mathbf E=\frac\rho{\epsilon_0},\quad\nabla\cdot\mathbf B=0,\quad\nabla\times\mathbf E=-\frac{\partial\mathbf B}{\partial t},\quad\nabla\times\mathbf B=\mu_0\mathbf J+\mu_0\epsilon_0\frac{\partial\mathbf E}{\partial t}$$
$$\mathbf S=\frac{1}{\mu_0}\mathbf E\times\mathbf B,\qquad u=\frac{\epsilon_0}{2}E^2+\frac{1}{2\mu_0}B^2,\qquad \frac{\partial u}{\partial t}+\nabla\cdot\mathbf S=-\mathbf J\cdot\mathbf E$$

#### Open problems
- Consistent classical treatment of radiation reaction (runaway solutions of Abraham–Lorentz–Dirac; Landau–Lifshitz approximation) — now tested with ultra-intense lasers.
- The Abraham–Minkowski controversy over light's momentum in media.

#### Connections
- [Special relativity](knowledge/05-relativity-and-gravitation/special-relativity/README.md) · [Gauge theories](knowledge/06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills/README.md) · [Plasma waves](knowledge/10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities/README.md)

### Electromagnetic waves and waveguides · `knowledge/02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides`

**Scope.** Wave equation in vacuum and media, plane waves, energy and intensity, Fresnel equations, Brewster's angle, total internal reflection and evanescent waves, conductors and skin depth, dispersion, rectangular and circular waveguides (TE/TM modes, cutoff), cavities and Q, transmission lines, antennas in brief.

**Core ideas.**
- In vacuum $\mathbf E\perp\mathbf B\perp\mathbf k$, $|E|=c|B|$.
- Waveguides have cutoff frequencies; below cutoff modes are evanescent.
- Good conductors exclude fields beyond a skin depth $\delta=\sqrt{2/\mu\sigma\omega}$.

**Key equations.**
$$r_s=\frac{n_1\cos\theta_i-n_2\cos\theta_t}{n_1\cos\theta_i+n_2\cos\theta_t},\qquad \tan\theta_B=\frac{n_2}{n_1},\qquad \omega_{mn}^{\text{cut}}=c\pi\sqrt{\frac{m^2}{a^2}+\frac{n^2}{b^2}}$$

**See also.** [Integrated and fiber photonics](knowledge/02-electromagnetism-and-optics/photonics-and-lasers/integrated-and-fiber-photonics/README.md) · [Mechanical waves](knowledge/01-classical-mechanics/oscillations-and-waves/mechanical-waves-and-acoustics/README.md)

### Maxwell's equations · `knowledge/02-electromagnetism-and-optics/electrodynamics/maxwells-equations`

**Scope.** Differential and integral forms, Faraday's law and Lenz's rule, displacement current, continuity equation, Poynting theorem, Maxwell stress tensor and field momentum, radiation pressure, Maxwell's equations in matter, magnetic monopoles (duality).

**Core ideas.**
- The displacement current makes Ampère's law consistent with charge conservation — and predicts EM waves.
- Fields carry energy, momentum and angular momentum; light exerts pressure $I/c$ (absorbed) or $2I/c$ (reflected).
- With magnetic monopoles the equations would be symmetric; Dirac showed their existence would quantize electric charge.

**Key equations.**
$$\oint\mathbf E\cdot d\mathbf l=-\frac{d\Phi_B}{dt},\qquad \frac{\partial\rho}{\partial t}+\nabla\cdot\mathbf J=0,\qquad \mathbf g=\epsilon_0\mathbf E\times\mathbf B$$

**Landmark.** Maxwell (1865) — see [subfield landmarks](knowledge/02-electromagnetism-and-optics/electrodynamics/README.md).

**See also.** [Noether's theorem](knowledge/00-foundations/symmetry-and-group-theory/noethers-theorem-and-conservation-laws/README.md)

### Potentials and gauge invariance · `knowledge/02-electromagnetism-and-optics/electrodynamics/potentials-and-gauge-invariance`

**Scope.** $\mathbf E=-\nabla V-\partial_t\mathbf A$, $\mathbf B=\nabla\times\mathbf A$, gauge transformations, Coulomb gauge (instantaneous $V$) vs. Lorenz gauge (manifestly covariant), retarded potentials, Jefimenko's equations, minimal coupling $\mathbf p\to\mathbf p-q\mathbf A$, Aharonov–Bohm effect.

**Core ideas.**
- Potentials are not unique: $\mathbf A\to\mathbf A+\nabla\lambda$, $V\to V-\partial_t\lambda$ leaves fields unchanged.
- In Lorenz gauge each potential obeys a wave equation sourced by charges/currents, solved by retarded potentials.
- Gauge invariance of electromagnetism is the prototype for all gauge theories of fundamental forces.

**Key equations.**
$$V(\mathbf r,t)=\frac{1}{4\pi\epsilon_0}\int\frac{\rho(\mathbf r',t_r)}{|\mathbf r-\mathbf r'|}d^3r',\quad t_r=t-\frac{|\mathbf r-\mathbf r'|}{c};\qquad \nabla\cdot\mathbf A+\frac{1}{c^2}\partial_tV=0$$

**See also.** [Geometric phases (AB effect)](knowledge/04-quantum-physics/quantum-mechanics-core/geometric-phases/README.md) · [Gauge theories](knowledge/06-particle-physics/quantum-field-theory/gauge-theories-and-yang-mills/README.md)

### Relativistic electrodynamics · `knowledge/02-electromagnetism-and-optics/electrodynamics/relativistic-electrodynamics`

**Scope.** Four-potential and four-current, $F^{\mu\nu}$ and its dual, covariant Maxwell equations, Lorentz transformation of $\mathbf E$ and $\mathbf B$, invariants $\mathbf E\cdot\mathbf B$ and $E^2-c^2B^2$, covariant Lorentz force, energy–momentum tensor of the field, Lagrangian of electromagnetism.

**Core ideas.**
- Electric and magnetic fields are frame-dependent components of a single tensor; magnetism is what electricity looks like from a moving frame.
- Maxwell's equations are Lorentz-covariant — the historical origin of special relativity.
- Two Lorentz invariants classify fields (e.g., a pure magnetic field cannot be transformed into a pure electric one).

**Key equations.**
$$\partial_\mu F^{\mu\nu}=\mu_0J^\nu,\quad\partial_{[\alpha}F_{\beta\gamma]}=0,\qquad \frac{dp^\mu}{d\tau}=qF^{\mu\nu}u_\nu,\qquad \mathcal L=-\frac{1}{4\mu_0}F_{\mu\nu}F^{\mu\nu}-A_\mu J^\mu$$

**See also.** [Lorentz transformations](knowledge/05-relativity-and-gravitation/special-relativity/lorentz-transformations-and-spacetime/README.md)

## Electrostatics and magnetostatics · `knowledge/02-electromagnetism-and-optics/electrostatics-and-magnetostatics`

#### Overview
When charges and currents don't change in time, electric and magnetic fields decouple. Electrostatics reduces to Poisson's equation for the potential; magnetostatics to Ampère's law for the vector potential. Uniqueness theorems make clever methods (images, separation of variables) rigorous.

#### Key equations
$$\nabla\cdot\mathbf E=\frac{\rho}{\epsilon_0},\quad\nabla\times\mathbf E=0,\quad\nabla^2V=-\frac{\rho}{\epsilon_0};\qquad \nabla\times\mathbf B=\mu_0\mathbf J,\quad \mathbf B(\mathbf r)=\frac{\mu_0}{4\pi}\int\frac{\mathbf J\times\hat{\boldsymbol{\mathscr r}}}{\mathscr r^2}dV'$$

#### Open problems
- Electrostatics is "complete", but computational electrostatics of biomolecules and nanodevices (implicit solvents, image charges at interfaces) remains active.

#### Connections
- [Green's functions](knowledge/00-foundations/mathematical-methods/differential-equations-and-greens-functions/README.md) · [Magnetism (condensed matter)](knowledge/08-condensed-matter/magnetism/README.md)

### Electrostatics and boundary-value problems · `knowledge/02-electromagnetism-and-optics/electrostatics-and-magnetostatics/electrostatics-and-boundary-value-problems`

**Scope.** Coulomb's law, Gauss's law with symmetry, potential and energy, conductors in equilibrium, Dirichlet and Neumann problems, uniqueness theorems, image charges (plane, sphere), separation of variables in Cartesian/spherical/cylindrical coordinates, capacitance, electrostatic energy and forces, Earnshaw's theorem.

**Core ideas.**
- Laplace's equation has no local extrema — so no stable electrostatic trap (Earnshaw); ion traps need RF (Paul) or magnetic fields (Penning).
- Uniqueness lets any guessed solution satisfying the boundary conditions be the solution.
- Energy can be stored in the field: $u=\tfrac12\epsilon_0E^2$.

**Key equations.**
$$\oint\mathbf E\cdot d\mathbf A=\frac{Q_{\text{enc}}}{\epsilon_0},\qquad V(r,\theta)=\sum_\ell\left(A_\ell r^\ell+\frac{B_\ell}{r^{\ell+1}}\right)P_\ell(\cos\theta),\qquad C_{\text{sphere}}=4\pi\epsilon_0R$$

**See also.** [Green's functions](knowledge/00-foundations/mathematical-methods/differential-equations-and-greens-functions/README.md) · [Trapped-ion qubits](knowledge/04-quantum-physics/quantum-information-and-computation/trapped-ion-and-neutral-atom-qubits/README.md)

### Fields in matter · `knowledge/02-electromagnetism-and-optics/electrostatics-and-magnetostatics/fields-in-matter`

**Scope.** Polarization $\mathbf P$ and bound charge, displacement $\mathbf D$, linear dielectrics and susceptibility, Clausius–Mossotti relation, magnetization $\mathbf M$, bound currents, $\mathbf H$ field, dia-/para-/ferromagnetism, hysteresis, boundary conditions at interfaces, frequency-dependent response (Drude, Lorentz models).

**Core ideas.**
- Matter responds to fields by forming dipoles; their averaged effect is captured by $\epsilon$ and $\mu$.
- Free charges source $\mathbf D$; free currents source $\mathbf H$.
- At interfaces: tangential $\mathbf E$ and normal $\mathbf B$ are continuous; normal $\mathbf D$ and tangential $\mathbf H$ jump by free surface charge/current.

**Key equations.**
$$\mathbf D=\epsilon_0\mathbf E+\mathbf P=\epsilon\mathbf E,\qquad \mathbf H=\frac{\mathbf B}{\mu_0}-\mathbf M,\qquad \epsilon(\omega)=1-\frac{\omega_p^2}{\omega^2+i\gamma\omega}\ (\text{Drude})$$

**See also.** [Ferromagnetism](knowledge/08-condensed-matter/magnetism/exchange-and-magnetic-order/README.md) · [Metamaterials](knowledge/02-electromagnetism-and-optics/photonics-and-lasers/metamaterials-and-plasmonics/README.md)

### Magnetostatics · `knowledge/02-electromagnetism-and-optics/electrostatics-and-magnetostatics/magnetostatics`

**Scope.** Lorentz force and the Hall effect, Biot–Savart law, Ampère's law with symmetry (wires, solenoids, toroids), vector potential and Coulomb gauge, magnetic dipole moment and torque, magnetic energy and inductance, absence of magnetic monopoles, magnetic levitation.

**Core ideas.**
- $\nabla\cdot\mathbf B=0$ always; $\mathbf B=\nabla\times\mathbf A$.
- Magnetic forces do no work on point charges; they redirect motion.
- A current loop is a magnetic dipole $\mathbf m=I\mathbf a$; torque $\boldsymbol\tau=\mathbf m\times\mathbf B$.

**Key equations.**
$$B_{\text{wire}}=\frac{\mu_0I}{2\pi s},\qquad B_{\text{solenoid}}=\mu_0nI,\qquad \mathbf B_{\text{dip}}=\frac{\mu_0}{4\pi r^3}[3(\mathbf m\cdot\hat{\mathbf r})\hat{\mathbf r}-\mathbf m]$$

**See also.** [Single-particle motion in plasmas](knowledge/10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts/README.md) · [Fields in matter](knowledge/02-electromagnetism-and-optics/electrostatics-and-magnetostatics/fields-in-matter/README.md)

### Multipole expansions · `knowledge/02-electromagnetism-and-optics/electrostatics-and-magnetostatics/multipole-expansions`

**Scope.** Cartesian and spherical multipoles, dipole and quadrupole moments, interaction energies of multipoles with external fields, multipole radiation, nuclear quadrupole moments, gravitational multipoles (Earth's $J_2$), fast multipole method.

**Core ideas.**
- Far from a localized source the $\ell$-th multipole falls as $r^{-(\ell+1)}$; the lowest non-vanishing one dominates.
- The dipole moment is origin-independent only if total charge vanishes.
- Symmetry kills multipoles: a sphere has only a monopole; a centrosymmetric charge distribution has no dipole.

**Key equations.**
$$V(\mathbf r)=\frac{1}{4\pi\epsilon_0}\left[\frac Qr+\frac{\mathbf p\cdot\hat{\mathbf r}}{r^2}+\frac12\sum_{ij}Q_{ij}\frac{\hat r_i\hat r_j}{r^3}+\cdots\right],\qquad Q_{ij}=\int\rho(3x_ix_j-r^2\delta_{ij})\,dV$$

**See also.** [Dipole radiation](knowledge/02-electromagnetism-and-optics/radiation-and-scattering/dipole-radiation-and-antennas/README.md) · [Gravitational waves (quadrupole formula)](knowledge/05-relativity-and-gravitation/gravitational-waves/gravitational-wave-theory-and-waveforms/README.md)

## Photonics and lasers · `knowledge/02-electromagnetism-and-optics/photonics-and-lasers`

#### Overview
Photonics controls light the way electronics controls electrons. Lasers provide coherent, intense, tunable light; nonlinear crystals convert its colour; mode-locking and chirped-pulse amplification create femtosecond-to-attosecond pulses at petawatt powers; nanostructured materials (photonic crystals, metamaterials, topological lattices) bend and guide light in ways no natural material can.

#### Key equations
$$\frac{dN_2}{dt}=R_p-\frac{N_2}{\tau}-\sigma\frac{I}{h\nu}(N_2-N_1),\qquad P=\epsilon_0\left(\chi^{(1)}E+\chi^{(2)}E^2+\chi^{(3)}E^3+\cdots\right)$$

#### Open problems
- Efficient, low-loss nonlinear and quantum photonic integrated circuits at scale.
- Electrically pumped lasers on silicon; photonic neural-network accelerators.

#### Connections
- [Quantum optics](knowledge/04-quantum-physics/quantum-optics/README.md) · [Laser–plasma interactions](knowledge/10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions/README.md) · [Attosecond science in AMO](knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/README.md)

### Integrated and fiber photonics · `knowledge/02-electromagnetism-and-optics/photonics-and-lasers/integrated-and-fiber-photonics`

**Scope.** Total-internal-reflection guiding, single- and multi-mode fibres, attenuation (~0.15 dB/km at 1550 nm), chromatic dispersion, erbium-doped amplifiers, silicon, silicon-nitride and thin-film lithium-niobate platforms, ring resonators, Kerr microcombs and dissipative solitons, photonic neural networks, co-packaged optics.

**Core ideas.**
- Low loss in silica made global optical communication possible (Kao, Nobel 2009).
- High-index-contrast chips shrink optical components to micrometres.
- Pumped microresonators generate broadband combs via Kerr solitons — chip-scale frequency metrology.

**Key equations.**
$$V=\frac{2\pi a}{\lambda}\mathrm{NA}<2.405\ (\text{single-mode}),\qquad \mathrm{NA}=\sqrt{n_1^2-n_2^2},\qquad D=-\frac{\lambda}{c}\frac{d^2n}{d\lambda^2}$$

**Landmark.** Kao & Hockham (1966) — see [subfield landmarks](knowledge/02-electromagnetism-and-optics/photonics-and-lasers/README.md).

**See also.** [Quantum communication](knowledge/04-quantum-physics/quantum-information-and-computation/quantum-communication-and-cryptography/README.md) · [Waveguides](knowledge/02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides/README.md)

### Laser physics · `knowledge/02-electromagnetism-and-optics/photonics-and-lasers/laser-physics`

**Scope.** Einstein A and B coefficients, three- and four-level systems, rate equations and threshold, gain saturation, Fabry–Pérot cavities and longitudinal/transverse modes, Gaussian beams, Schawlow–Townes linewidth, Q-switching, mode-locking, semiconductor and fibre lasers, frequency stabilization.

**Core ideas.**
- Gain requires population inversion, impossible in two-level systems in steady state.
- Threshold: round-trip gain equals round-trip loss.
- Mode-locking phase-locks many longitudinal modes into ultrashort pulses; the pulse train's spectrum is a frequency comb.

**Key equations.**
$$\frac{A_{21}}{B_{21}}=\frac{8\pi h\nu^3}{c^3},\qquad \Delta\nu_{\text{FSR}}=\frac{c}{2L},\qquad w(z)=w_0\sqrt{1+(z/z_R)^2},\ z_R=\frac{\pi w_0^2}{\lambda}$$

**See also.** [Cavity QED](knowledge/04-quantum-physics/quantum-optics/cavity-and-circuit-qed/README.md) · [Laser cooling](knowledge/04-quantum-physics/atomic-molecular-and-optical-physics/laser-cooling-and-trapping/README.md)

### Metamaterials and plasmonics · `knowledge/02-electromagnetism-and-optics/photonics-and-lasers/metamaterials-and-plasmonics`

**Scope.** Effective-medium theory, split-ring resonators and negative permeability, negative refraction and the perfect lens, transformation optics and cloaking, metasurfaces and flat lenses, surface plasmon polaritons, localized plasmons in nanoparticles, SERS, photonic bandgaps, epsilon-near-zero media.

**Core ideas.**
- Sub-wavelength resonant structures act as artificial atoms with designer $\epsilon(\omega)$, $\mu(\omega)$.
- Plasmons confine light far below the diffraction limit at the cost of ohmic loss.
- Periodic dielectric structures open photonic band gaps, inhibiting spontaneous emission.

**Key equations.**
$$k_{\text{SPP}}=\frac\omega c\sqrt{\frac{\epsilon_m\epsilon_d}{\epsilon_m+\epsilon_d}},\qquad n<0\ \text{when}\ \epsilon<0,\ \mu<0$$

**See also.** [Fields in matter](knowledge/02-electromagnetism-and-optics/electrostatics-and-magnetostatics/fields-in-matter/README.md) · [Topological photonics](knowledge/02-electromagnetism-and-optics/photonics-and-lasers/topological-photonics/README.md)

### Nonlinear optics · `knowledge/02-electromagnetism-and-optics/photonics-and-lasers/nonlinear-optics`

**Scope.** $\chi^{(2)}$ processes (SHG, sum/difference frequency, OPA/OPO, spontaneous parametric down-conversion), phase matching and quasi-phase matching, $\chi^{(3)}$ processes (Kerr effect, self-focusing, self-phase modulation, four-wave mixing), optical solitons, supercontinuum, stimulated Raman and Brillouin scattering.

**Core ideas.**
- $\chi^{(2)}$ vanishes in centrosymmetric media; $\chi^{(3)}$ is always present.
- Efficient conversion requires phase matching $\Delta k=0$ (birefringence or periodic poling).
- In fibres, Kerr nonlinearity balanced against anomalous dispersion gives solitons.

**Key equations.**
$$n=n_0+n_2I,\qquad \Delta k=k_{2\omega}-2k_\omega,\qquad I_{2\omega}\propto I_\omega^2L^2\,\mathrm{sinc}^2(\Delta kL/2)$$

**Landmark.** Franken et al. (1961) — see [subfield landmarks](knowledge/02-electromagnetism-and-optics/photonics-and-lasers/README.md).

**See also.** [Solitons](knowledge/01-classical-mechanics/nonlinear-dynamics-and-chaos/solitons-and-integrable-systems/README.md) · [Squeezed light](knowledge/04-quantum-physics/quantum-optics/squeezed-light-and-quantum-metrology/README.md)

### Topological photonics · `knowledge/02-electromagnetism-and-optics/photonics-and-lasers/topological-photonics`

**Scope.** Haldane–Raghu proposal, magneto-optic photonic crystals with chiral edge states, valley and spin-Hall photonic insulators, Floquet waveguide lattices, topological lasers, synthetic dimensions, non-Hermitian topological photonics, topological quantum photonic circuits.

**Core ideas.**
- Photonic bands carry Berry curvature and Chern numbers just like electrons.
- Nonzero Chern number guarantees unidirectional edge modes that flow around defects without reflection.
- Photons are bosons without Fermi levels, so topology is probed with excitations at chosen frequencies.

**Key equations.**
$$C=\frac{1}{2\pi}\int_{\text{BZ}}\Omega(\mathbf k)\,d^2k\in\mathbb Z,\qquad N_{\text{edge}}=\Delta C$$

**Landmark.** Ozawa et al. (2019) — see [subfield landmarks](knowledge/02-electromagnetism-and-optics/photonics-and-lasers/README.md).

**See also.** [Topological insulators](knowledge/08-condensed-matter/topological-matter/topological-insulators/README.md) · [Non-Hermitian physics](knowledge/04-quantum-physics/open-and-many-body-quantum-dynamics/non-hermitian-physics/README.md)

### Ultrafast and attosecond optics · `knowledge/02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics`

**Scope.** Time–bandwidth product, dispersion and pulse compression, chirped-pulse amplification (Nobel 2018), pulse characterization (FROG, SPIDER), pump–probe spectroscopy, strong-field ionization, three-step model of high-harmonic generation, attosecond pulse trains and isolated pulses (Nobel 2023), attosecond streaking, petahertz electronics.

**Core ideas.**
- Short pulses need broad spectra: $\Delta t\,\Delta\nu\ge0.44$ (Gaussian).
- CPA stretches, amplifies, then recompresses pulses to avoid damaging the amplifier.
- HHG: electron tunnels out, accelerates in the laser field, recombines — emitting attosecond XUV bursts with a cutoff at $I_p+3.17U_p$.

**Key equations.**
$$U_p=\frac{e^2E_0^2}{4m_e\omega^2},\qquad \hbar\omega_{\max}=I_p+3.17\,U_p$$

**See also.** [Laser–plasma interactions](knowledge/10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions/README.md) · [Reaction dynamics](knowledge/11-interdisciplinary-physics/chemical-physics/reaction-dynamics/README.md)

## Radiation and scattering · `knowledge/02-electromagnetism-and-optics/radiation-and-scattering`

#### Overview
Accelerating charges radiate; the Larmor formula gives the power, and the Liénard–Wiechert potentials give the full fields. Scattering is radiation re-emitted by charges driven by an incident wave — explaining blue skies, white clouds, and how astronomers diagnose plasmas.

#### Key equations
$$P=\frac{q^2a^2}{6\pi\epsilon_0c^3}\ (\text{Larmor}),\qquad P_{\text{rel}}=\frac{q^2\gamma^6}{6\pi\epsilon_0c}\left[\dot{\boldsymbol\beta}^2-(\boldsymbol\beta\times\dot{\boldsymbol\beta})^2\right]\ (\text{Liénard})$$

#### Connections
- [Synchrotron and FEL light sources](knowledge/11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources/README.md) · [High-energy astrophysics](knowledge/09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/README.md) · [Atmospheric physics](knowledge/11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing/README.md)

### Cherenkov and transition radiation · `knowledge/02-electromagnetism-and-optics/radiation-and-scattering/cherenkov-and-transition-radiation`

**Scope.** Cherenkov condition $v>c/n$, emission angle and Frank–Tamm spectrum, Cherenkov detectors (Super-K, RICH, IceCube, imaging atmospheric telescopes), transition radiation and TRDs for electron identification, Smith–Purcell radiation, Askaryan radio emission.

**Core ideas.**
- A uniformly moving charge radiates only if it outruns the phase velocity of light in the medium — an optical "sonic boom".
- The cone angle measures particle velocity, enabling particle identification.
- Transition radiation intensity grows with $\gamma$, distinguishing electrons from hadrons at the same momentum.

**Key equations.**
$$\cos\theta_C=\frac{1}{n\beta},\qquad \frac{d^2N}{dx\,d\lambda}=\frac{2\pi\alpha z^2}{\lambda^2}\left(1-\frac{1}{\beta^2n^2}\right)$$

**See also.** [Neutrino experiments](knowledge/06-particle-physics/neutrino-physics/neutrino-experiments-and-sources/README.md) · [Neutrino astronomy](knowledge/09-astrophysics-and-cosmology/high-energy-astrophysics-and-astroparticle/neutrino-astronomy/README.md)

### Dipole radiation and antennas · `knowledge/02-electromagnetism-and-optics/radiation-and-scattering/dipole-radiation-and-antennas`

**Scope.** Near, intermediate and far zones, oscillating electric dipole fields, $\sin^2\theta$ pattern, magnetic dipole and electric quadrupole radiation, half-wave antenna, radiation resistance, antenna gain and directivity, phased arrays and beam steering, reciprocity.

**Core ideas.**
- Far-field radiated power scales as $\omega^4$ — why short wavelengths scatter more.
- No radiation along the dipole axis; maximum perpendicular to it.
- Arrays shape beams by interference; phase shifts steer them electronically.

**Key equations.**
$$\langle P\rangle=\frac{\mu_0p_0^2\omega^4}{12\pi c},\qquad \frac{d\langle P\rangle}{d\Omega}=\frac{\mu_0p_0^2\omega^4}{32\pi^2c}\sin^2\theta,\qquad R_{\text{rad}}^{\lambda/2}\approx73\ \Omega$$

**See also.** [Multipole expansions](knowledge/02-electromagnetism-and-optics/electrostatics-and-magnetostatics/multipole-expansions/README.md)

### Radiation from moving charges · `knowledge/02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges`

**Scope.** Liénard–Wiechert potentials, velocity and acceleration fields, relativistic beaming, synchrotron radiation spectrum and critical frequency, bremsstrahlung (free–free emission), undulator radiation, Abraham–Lorentz force and radiation reaction, classical electron radius.

**Core ideas.**
- Relativistic charges radiate into a forward cone of half-angle $\sim1/\gamma$.
- Synchrotron loss scales as $\gamma^4/R^2$ — the limit on circular electron accelerators and a key astrophysical emission mechanism.
- Radiation reaction becomes important when the classical electron radius $r_e=e^2/4\pi\epsilon_0m_ec^2\approx2.8$ fm per wavelength is not negligible.

**Key equations.**
$$\omega_c=\frac32\gamma^3\frac{c}{\rho},\qquad \mathbf F_{\text{rad}}=\frac{q^2}{6\pi\epsilon_0c^3}\dot{\mathbf a}\ (\text{Abraham–Lorentz})$$

**See also.** [Future colliders](knowledge/06-particle-physics/collider-and-experimental-particle-physics/future-colliders/README.md) · [Synchrotron light sources](knowledge/11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources/README.md)

### Scattering of light · `knowledge/02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light`

**Scope.** Thomson scattering off free electrons, Rayleigh scattering off small particles and molecules ($\lambda^{-4}$), polarization of skylight, Mie theory for particles comparable to $\lambda$, extinction and optical depth, Compton scattering (quantum), Raman and Brillouin scattering (inelastic), dynamic light scattering, X-ray scattering.

**Core ideas.**
- Small scatterers act as driven dipoles → $\sigma\propto\omega^4$ → blue sky, red sunsets.
- Particles larger than $\lambda$ scatter nearly wavelength-independently → white clouds.
- Thomson cross section $\sigma_T=\frac{8\pi}{3}r_e^2=6.65\times10^{-29}$ m² sets opacity of ionized gas (CMB last scattering, stellar interiors).

**Key equations.**
$$\sigma_{\text{Rayleigh}}=\frac{8\pi}{3}k^4a^6\left|\frac{\epsilon-1}{\epsilon+2}\right|^2,\qquad \lambda'-\lambda=\frac{h}{m_ec}(1-\cos\theta)$$

**Landmark.** Mie (1908) — see [subfield landmarks](knowledge/02-electromagnetism-and-optics/radiation-and-scattering/README.md).

**See also.** [CMB](knowledge/09-astrophysics-and-cosmology/cosmology/cosmic-microwave-background/README.md) · [Crystal structure and diffraction](knowledge/08-condensed-matter/crystals-and-electronic-structure/crystal-structure-and-diffraction/README.md)


---

# Packet 02-5 (69 records)

{"id": "C1211", "a": "02-electromagnetism-and-optics/classical-optics/polarization-and-crystal-optics", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Faraday rotation and magnetized-plasma birefringence", "kind": "mechanism", "summary": "A magnetized plasma is birefringent, with O and X modes and Faraday rotation of linear polarization. Used for polarimetry of tokamak currents and astrophysical fields; matches magneto-optic effects in crystals.", "map": "\\Delta\\psi\\propto\\int n_e B_\\parallel\\,dl", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1212", "a": "02-electromagnetism-and-optics/electrodynamics", "b": "10-plasma-physics/plasma-fundamentals", "name": "Plasma as electrodynamic medium", "kind": "shared object", "summary": "A plasma is a medium with a frequency- and wavevector-dependent dielectric function from free charges. Skin depth, cutoff and reflection by the ionosphere follow from electrodynamics.", "map": "\\epsilon(\\omega)=1-\\omega_p^2/\\omega^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1213", "a": "02-electromagnetism-and-optics/electrodynamics", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Maxwell equations underlying plasma waves", "kind": "identity", "summary": "Plasma waves follow from Maxwell's equations closed with a plasma current response; the dielectric tensor turns the wave equation into the dispersion relations of Langmuir, EM, and whistler modes.", "map": "\\omega^2 = \\omega_p^2 + k^2c^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1214", "a": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "b": "10-plasma-physics/magnetic-confinement-fusion/tokamaks", "name": "Wave heating and current drive", "kind": "method transfer", "summary": "Electron cyclotron, ion cyclotron and lower-hybrid heating rely on waveguide and transmission-line technology, with gyrotrons as sources and wave propagation set by the magnetized-plasma dispersion relation.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1215", "a": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "EM waves in plasma: cutoff and skin depth", "kind": "identity", "summary": "Electromagnetic waves in a plasma have a cutoff at the plasma frequency and evanescent skin depth below it, like waveguide cutoff modes. Plasma-filled waveguides share the same dispersion form.", "map": "\\omega^2=\\omega_p^2+k^2c^2", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1216", "a": "02-electromagnetism-and-optics/electrodynamics/maxwells-equations", "b": "10-plasma-physics/magnetohydrodynamics/ideal-mhd-and-alfven-waves", "name": "MHD as Maxwell with displacement current dropped", "kind": "mechanism", "summary": "MHD uses Ampère's law without displacement current and Faraday's law with Ohm's law. This gives induction equation, frozen-in flux and magnetic pressure and tension from the Maxwell stress tensor.", "map": "\\partial_t\\mathbf{B}=\\nabla\\times(\\mathbf{v}\\times\\mathbf{B})", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1217", "a": "02-electromagnetism-and-optics/electrodynamics/maxwells-equations", "b": "10-plasma-physics/magnetohydrodynamics/magnetic-reconnection", "name": "Magnetic energy release and Poynting flux", "kind": "shared object", "summary": "Reconnection converts stored magnetic energy to flow and heat; field energy density and Poynting flux from Maxwell theory account for energy budgets, and Ohm's law breaks flux freezing.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1218", "a": "02-electromagnetism-and-optics/electrodynamics/potentials-and-gauge-invariance", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Gauge choice in gyrokinetics and Vlasov–Maxwell", "kind": "method transfer", "summary": "Vlasov–Maxwell and gyrokinetic theory use scalar and vector potentials, with Coulomb gauge and Lagrangian/Hamiltonian formulations. Gauge invariance underlies canonical momentum conservation and the ponderomotive force.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1219", "a": "02-electromagnetism-and-optics/electrodynamics/relativistic-electrodynamics", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "E×B drift from field transformation", "kind": "identity", "summary": "The E×B drift is the velocity of the frame where E vanishes, following from the Lorentz transformation of fields. Invariants E·B and E²−c²B² determine when such a frame exists.", "map": "\\mathbf{v}=\\mathbf{E}\\times\\mathbf{B}/B^2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1220", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/electrostatics-and-boundary-value-problems", "b": "10-plasma-physics/plasma-fundamentals/debye-shielding-and-plasma-parameters", "name": "Debye screening as screened Poisson", "kind": "identity", "summary": "Debye shielding is Poisson's equation with a mobile-charge response, giving the screened (Yukawa) potential rather than Coulomb. Conductors in electrostatics are the infinite-density limit.", "map": "\\nabla^2\\phi=\\lambda_D^{-2}\\phi", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1221", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/fields-in-matter", "b": "10-plasma-physics/plasma-fundamentals/dusty-and-strongly-coupled-plasmas", "name": "Dielectric response and screening in dusty plasma", "kind": "analogy", "summary": "Dust grains charge and polarize in the plasma, and screened Coulomb (Yukawa) interactions follow from the dielectric response. Charged dust dynamics ties electrostatics to space plasmas.", "map": "", "breaks": "Dust charge is not fixed; it varies with the plasma currents, and the interaction is non-reciprocal in flowing plasma.", "confidence": "established", "strength": 1}
{"id": "C1222", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/magnetostatics", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Drifts from static field geometry", "kind": "shared object", "summary": "Gradient-B and curvature drifts and magnetic mirrors arise from non-uniform static magnetic fields computed from Biot–Savart and Ampère. Adiabatic invariants link to the magnetic moment of current loops.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1223", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/magnetostatics", "b": "10-plasma-physics/plasma-fundamentals/single-particle-motion-and-drifts", "name": "Magnetic fields and guiding-centre motion", "kind": "shared object", "summary": "Lorentz force in static magnetic fields gives gyration, gradient and curvature drifts, and mirror forces. These follow from magnetostatic field geometry and the dipole moment of gyrating charges.", "map": "\\mu = \\frac{m v_\\perp^2}{2B}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1224", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/multipole-expansions", "b": "10-plasma-physics/space-and-astrophysical-plasmas/magnetospheres-and-space-weather", "name": "Dipole field of planetary magnetospheres", "kind": "shared object", "summary": "Planetary fields are expanded in multipoles, with the dipole dominant. The dipole geometry sets L-shells, mirror points and radiation-belt trapping, with the magnetopause deforming it.", "map": "B=B_0 (R_E/r)^3\\sqrt{1+3\\sin^2\\lambda}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1225", "a": "02-electromagnetism-and-optics/photonics-and-lasers", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "Intense lasers driving plasma", "kind": "shared object", "summary": "High-power laser technology (chirped-pulse amplification, ultrashort pulses) supplies the drivers for laser–plasma physics. The plasma then acts as a nonlinear optical medium.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1226", "a": "02-electromagnetism-and-optics/photonics-and-lasers/integrated-and-fiber-photonics", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "Ponderomotive force and Kerr nonlinearity in filaments", "kind": "analogy", "summary": "Relativistic and ponderomotive self-focusing in plasma parallels Kerr self-focusing and filamentation in fibres and bulk media, with critical power thresholds and soliton-like channels.", "map": "P_{cr}\\propto\\lambda^2/n_2", "breaks": "Plasma nonlinearity is non-local and saturates via cavitation; Kerr nonlinearity is local and bound-electron.", "confidence": "established", "strength": 2}
{"id": "C1227", "a": "02-electromagnetism-and-optics/photonics-and-lasers/laser-physics", "b": "10-plasma-physics/inertial-and-laser-plasmas/plasma-wakefield-acceleration", "name": "Plasma as gain medium and X-ray lasers", "kind": "shared object", "summary": "Laser-produced plasmas serve as gain media for soft X-ray lasers via collisional excitation, and free-electron lasers share synchrotron-radiation physics with plasma-accelerator-driven sources.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1228", "a": "02-electromagnetism-and-optics/photonics-and-lasers/metamaterials-and-plasmonics", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "Surface plasmons and resonance absorption", "kind": "analogy", "summary": "Surface plasmon polaritons in metals and resonance absorption at the critical density in laser plasmas both come from a Drude-type epsilon crossing zero, with a resonant collective electron oscillation.", "map": "\\epsilon(\\omega)=1-\\omega_p^2/(\\omega^2+i\\nu\\omega)", "breaks": "Laser plasma is hot, inhomogeneous and nonlinear with density gradients; metal plasmons are cold, linear, bound to sharp interfaces.", "confidence": "established", "strength": 2}
{"id": "C1229", "a": "02-electromagnetism-and-optics/photonics-and-lasers/metamaterials-and-plasmonics", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Drude metal as cold plasma", "kind": "identity", "summary": "The free-electron Drude dielectric function of metals is the cold-plasma dielectric function. Bulk and surface plasmons are Langmuir-type oscillations, and epsilon-near-zero media exploit the plasma cutoff.", "map": "\\omega_p^2=\\frac{ne^2}{\\epsilon_0 m}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1230", "a": "02-electromagnetism-and-optics/photonics-and-lasers/nonlinear-optics", "b": "10-plasma-physics/inertial-and-laser-plasmas/inertial-confinement-fusion", "name": "Laser beam smoothing and cross-beam energy transfer", "kind": "method transfer", "summary": "Optical frequency conversion (KDP harmonics) and beam smoothing deliver uniform UV drive in ICF. Cross-beam energy transfer is a stimulated Brillouin process.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1231", "a": "02-electromagnetism-and-optics/photonics-and-lasers/nonlinear-optics", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "Parametric instabilities as nonlinear optics", "kind": "mechanism", "summary": "Stimulated Raman and Brillouin scattering and two-plasmon decay are three-wave parametric processes, analogous to optical parametric amplification and stimulated scattering in nonlinear media. Relativistic self-focusing parallels Kerr self-focusing.", "map": "\\omega_0=\\omega_s+\\omega_{pl},\\ \\mathbf{k}_0=\\mathbf{k}_s+\\mathbf{k}_{pl}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1232", "a": "02-electromagnetism-and-optics/photonics-and-lasers/topological-photonics", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Topological waves in magnetized plasma", "kind": "analogy", "summary": "Magnetized plasma, with gyrotropic dielectric tensor, breaks time reversal like magneto-optic photonic crystals. Topological edge modes (Parker et al.) can arise in continuous plasma, analogous to photonic quantum Hall.", "map": "", "breaks": "Plasma is continuous and dispersive, so the topological invariant needs regularization and bulk-edge correspondence is subtle.", "confidence": "current research", "strength": 2}
{"id": "C1233", "a": "02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics", "b": "10-plasma-physics/inertial-and-laser-plasmas", "name": "Plasma physics reliance on CPA lasers", "kind": "historical", "summary": "Chirped-pulse amplification, developed in optics, opened petawatt-class plasma experiments, including wakefield acceleration and ion acceleration.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1234", "a": "02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "Ultrafast pulses and relativistic laser-plasma", "kind": "method transfer", "summary": "Chirped-pulse amplification enabled relativistic intensities. High-harmonic generation on solid-plasma surfaces (relativistic oscillating mirror) is the plasma counterpart of gas-phase attosecond HHG.", "map": "", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1235", "a": "02-electromagnetism-and-optics/radiation-and-scattering/cherenkov-and-transition-radiation", "b": "10-plasma-physics/inertial-and-laser-plasmas/plasma-wakefield-acceleration", "name": "Wakefield as Cherenkov wake", "kind": "mechanism", "summary": "A relativistic driver excites a wake in plasma at phase velocity equal to the driver velocity, a Cherenkov-type process. Transition radiation is used to diagnose the accelerated beams.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1236", "a": "02-electromagnetism-and-optics/radiation-and-scattering/cherenkov-and-transition-radiation", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Cherenkov emission as beam-plasma instability", "kind": "mechanism", "summary": "Wave–particle resonance at ω=k·v is the Cherenkov condition. Landau damping and the beam-plasma instability are the collective version of Cherenkov emission of Langmuir waves.", "map": "\\omega=\\mathbf{k}\\cdot\\mathbf{v}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1237", "a": "02-electromagnetism-and-optics/radiation-and-scattering/dipole-radiation-and-antennas", "b": "10-plasma-physics/plasma-fundamentals/plasma-waves-and-instabilities", "name": "Antenna coupling and heating of plasma", "kind": "method transfer", "summary": "Antenna and waveguide launching of ion-cyclotron, lower-hybrid and helicon waves uses radiation and coupling theory. Cutoffs and resonances in plasma determine accessibility.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1238", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "10-plasma-physics/inertial-and-laser-plasmas/laser-plasma-interactions", "name": "Radiation from laser-driven electrons", "kind": "mechanism", "summary": "Electrons oscillating in intense laser fields emit nonlinear Thomson/Compton radiation and radiation-reaction losses. The Larmor and Liénard formulas govern emission and the damping force in ultra-intense regimes.", "map": "P=\\frac{2}{3}\\frac{e^2}{4\\pi\\epsilon_0 c^3}\\gamma^6\\left[\\dot{\\mathbf{a}}^2-\\ldots\\right]", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1239", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "10-plasma-physics/magnetic-confinement-fusion/tokamaks", "name": "Synchrotron and bremsstrahlung losses in tokamaks", "kind": "shared object", "summary": "Electron cyclotron emission, synchrotron losses and bremsstrahlung from Larmor radiation set power balance and provide temperature diagnostics in fusion plasmas.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1240", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "10-plasma-physics/space-and-astrophysical-plasmas/astrophysical-plasmas-and-shocks", "name": "Synchrotron emission from shock-accelerated electrons", "kind": "shared object", "summary": "Relativistic electrons accelerated at shocks radiate synchrotron emission in amplified fields. Power-law spectra reveal the acceleration process in supernova remnants.", "map": "P\\propto\\gamma^2B^2", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1241", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "10-plasma-physics/inertial-and-laser-plasmas/high-energy-density-physics", "name": "Thomson scattering as plasma diagnostic", "kind": "method transfer", "summary": "Thomson scattering from free electrons is used to measure density, temperature and collective modes in plasmas. X-ray Thomson scattering diagnoses warm dense matter.", "map": "S(k,\\omega),\\ \\alpha=1/(k\\lambda_D)", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1242", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "10-plasma-physics/plasma-fundamentals/kinetic-theory-vlasov-and-landau-damping", "name": "Collective Thomson scattering and the dynamic structure factor", "kind": "mechanism", "summary": "Collective Thomson scattering probes the electron and ion-acoustic fluctuation spectrum, which follows from Vlasov dielectric response. Landau damping shapes resonance widths.", "map": "S(k,\\omega)\\propto \\frac{\\mathrm{Im}\\,\\epsilon^{-1}}{\\ldots}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1243", "a": "02-electromagnetism-and-optics/classical-optics", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Optics and imaging theory in medical imaging", "kind": "method transfer", "summary": "Transfer functions, resolution limits and Fourier-based image formation from optics carry over to radiography, CT and MRI image-quality analysis.", "map": "I(\\mathbf{r})=(O*h)(\\mathbf{r})\\;\\Rightarrow\\;\\tilde I=\\tilde O\\,\\mathrm{MTF}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1244", "a": "02-electromagnetism-and-optics/classical-optics/coherence-and-statistical-optics", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Coherence of X-ray sources", "kind": "shared object", "summary": "Diffraction-limited storage rings and FELs are characterized by transverse and longitudinal coherence, with van Cittert–Zernike propagation and emittance matching the diffraction limit $\\lambda/4\\pi$.", "map": "\\epsilon\\to\\lambda/4\\pi", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1245", "a": "02-electromagnetism-and-optics/classical-optics/coherence-and-statistical-optics", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Intensity interferometry and quantum sensing noise", "kind": "analogy", "summary": "Both rely on correlation measurements: Hanbury Brown–Twiss intensity correlations probe photon statistics, while sensor readout in quantum metrology is limited by shot noise and squeezing.", "map": "", "breaks": "Intensity interferometry exploits classical thermal-light bunching, while quantum sensing gains come from nonclassical entanglement or squeezing.", "confidence": "proposed", "strength": 1}
{"id": "C1246", "a": "02-electromagnetism-and-optics/classical-optics/coherence-and-statistical-optics", "b": "11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics", "name": "Coherence in OCT and speckle", "kind": "shared object", "summary": "OCT depth resolution is set by source coherence length (low-coherence interferometry), and speckle statistics govern both optical and ultrasound image texture.", "map": "l_c=\\frac{2\\ln2}{\\pi}\\frac{\\lambda^2}{\\Delta\\lambda}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1247", "a": "02-electromagnetism-and-optics/classical-optics/fourier-optics-and-imaging", "b": "11-interdisciplinary-physics/biophysics/single-molecule-biophysics", "name": "Super-resolution and single-molecule localization", "kind": "method transfer", "summary": "Single-molecule localization microscopy (PALM/STORM) beats the diffraction limit by fitting the point-spread function of isolated emitters, linking single-molecule fluorescence to Fourier-optics resolution theory.", "map": "\\sigma_{loc}\\approx \\sigma_{PSF}/\\sqrt N", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1248", "a": "02-electromagnetism-and-optics/classical-optics/fourier-optics-and-imaging", "b": "11-interdisciplinary-physics/medical-physics", "name": "Medical imaging as Fourier optics", "kind": "method transfer", "summary": "Medical imaging modalities use transfer-function, sampling and deconvolution ideas first developed in Fourier optics.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1249", "a": "02-electromagnetism-and-optics/classical-optics/fourier-optics-and-imaging", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Fourier imaging: lens, CT and MRI k-space", "kind": "identity", "summary": "A lens performs a spatial Fourier transform; MRI samples k-space directly and CT uses the Fourier slice theorem. Reconstruction is Fourier synthesis with MTF-limited resolution.", "map": "\\tilde f(\\mathbf{k})=\\int f(\\mathbf{r})e^{-i\\mathbf{k}\\cdot\\mathbf{r}}d\\mathbf{r}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1250", "a": "02-electromagnetism-and-optics/classical-optics/fourier-optics-and-imaging", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Image quality via MTF", "kind": "identity", "summary": "Modulation transfer function and noise power spectrum quantify medical image quality exactly as in optical imaging systems.", "map": "\\mathrm{MTF}(\\mathbf{k})=|\\tilde h(\\mathbf{k})|/\\tilde h(0)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1251", "a": "02-electromagnetism-and-optics/classical-optics/geometric-optics", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Beam optics as ray-transfer matrices", "kind": "identity", "summary": "Linear transfer matrices for quadrupoles and drifts mirror ABCD ray matrices; Twiss parameters mirror Gaussian-beam parameters and emittance mirrors etendue.", "map": "\\begin{pmatrix}x\\\\x'\\end{pmatrix}_{out}=M\\begin{pmatrix}x\\\\x'\\end{pmatrix}_{in}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1252", "a": "02-electromagnetism-and-optics/classical-optics/interference-and-diffraction", "b": "11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics", "name": "Interferometry in OCT", "kind": "method transfer", "summary": "OCT uses Michelson low-coherence interferometry to gate backscattered light by path length, and ultrasound beam focusing and arrays rely on the same diffraction and array-factor physics.", "map": "I\\propto 2\\sqrt{I_rI_s}\\cos(2k\\Delta z)", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1253", "a": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "b": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "name": "RF cavities as electromagnetic resonators", "kind": "identity", "summary": "Accelerating RF and SRF cavities are resonant waveguide modes; field patterns, Q factor and wall losses follow from cavity electrodynamics.", "map": "Q=\\omega_0 U/P_{loss}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1254", "a": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Absorption and dielectric response in spectroscopy", "kind": "identity", "summary": "Molecular absorption bands are the imaginary part of the dielectric function; Kramers–Kronig relations link absorption and refractive index.", "map": "n(\\omega)-1=\\frac{2}{\\pi}P\\!\\int\\frac{\\omega'\\kappa(\\omega')}{\\omega'^2-\\omega^2}d\\omega'", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1255", "a": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Reflection and absorption of radiation", "kind": "mechanism", "summary": "Fresnel reflection and absorption set surface albedo and emissivity, and skin-depth-like penetration governs microwave remote sensing.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1256", "a": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/seismology-and-earth-interior", "name": "Seismic and EM wave reflection analogy", "kind": "analogy", "summary": "Seismic P/S reflection and refraction at interfaces follows Snell's law with Zoeppritz amplitudes, paralleling Fresnel coefficients and polarization-dependent reflection.", "map": "", "breaks": "Elastic waves have longitudinal and mode-converted components, so there are more coupled modes than the two EM polarizations.", "confidence": "established", "strength": 2}
{"id": "C1257", "a": "02-electromagnetism-and-optics/electrodynamics/electromagnetic-waves-and-waveguides", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "MRI RF coils and field propagation", "kind": "shared object", "summary": "MRI excitation and detection use RF coils and resonant circuits, and at high field wavelength effects in tissue produce B1 inhomogeneity governed by EM wave propagation.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1258", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/electrostatics-and-boundary-value-problems", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Device electrostatics via Poisson equation", "kind": "identity", "summary": "The depletion region of a p-n junction and MOS gate electrostatics are Poisson boundary-value problems, solved numerically in TCAD.", "map": "\\nabla^2\\phi=-\\rho/\\epsilon", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1259", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/fields-in-matter", "b": "11-interdisciplinary-physics/applied-and-device-physics/quantum-sensing", "name": "Magnetometry and magnetization response", "kind": "shared object", "summary": "NV-centre and atomic magnetometers and SQUIDs measure the B field of magnetized samples, so interpreting signals needs dipole fields and bound-current models.", "map": "", "breaks": "", "confidence": "established", "strength": 1}
{"id": "C1260", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/magnetostatics", "b": "11-interdisciplinary-physics/accelerator-physics/accelerator-technology", "name": "Accelerator magnets from magnetostatics", "kind": "method transfer", "summary": "Dipole and quadrupole magnet design uses magnetostatic field solutions and multipole expansion of the 2D field, with pole shaping setting harmonic content.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1261", "a": "02-electromagnetism-and-optics/electrostatics-and-magnetostatics/multipole-expansions", "b": "11-interdisciplinary-physics/accelerator-physics/beam-dynamics", "name": "Field multipoles and nonlinear beam dynamics", "kind": "mechanism", "summary": "Sextupole and higher multipole errors in magnets drive chromatic and resonant nonlinear beam motion; multipole decomposition of the field organizes these effects.", "map": "B_y+iB_x=B_0\\sum_n (b_n+ia_n)(x+iy)^{n-1}", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1262", "a": "02-electromagnetism-and-optics/photonics-and-lasers/integrated-and-fiber-photonics", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Silicon photonics and electronic fabrication", "kind": "method transfer", "summary": "Silicon photonic chips reuse CMOS lithography and materials platforms from semiconductor devices, merging electronic and photonic components.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1263", "a": "02-electromagnetism-and-optics/photonics-and-lasers/laser-physics", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "FEL as a laser without a bound medium", "kind": "analogy", "summary": "SASE FELs amplify radiation through collective microbunching of free electrons, analogous to gain with stimulated emission in lasers, but with no population inversion.", "map": "P\\propto e^{z/L_g}", "breaks": "Gain comes from classical electron bunching, not quantized level inversion; SASE starts from shot noise, with poor temporal coherence.", "confidence": "established", "strength": 2}
{"id": "C1264", "a": "02-electromagnetism-and-optics/photonics-and-lasers/laser-physics", "b": "11-interdisciplinary-physics/applied-and-device-physics/semiconductor-devices-and-photovoltaics", "name": "Semiconductor diode lasers", "kind": "shared object", "summary": "LEDs and diode lasers realize stimulated emission and population inversion in a p-n junction, with cavity feedback setting threshold and linewidth.", "map": "g_{th}=\\alpha_i+\\frac{1}{2L}\\ln\\frac{1}{R_1R_2}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1265", "a": "02-electromagnetism-and-optics/photonics-and-lasers/nonlinear-optics", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Multidimensional and nonlinear spectroscopy", "kind": "method transfer", "summary": "Coherent Raman, 2D electronic and vibrational spectroscopies are higher-order nonlinear susceptibility measurements, using pulse sequences and phase matching from nonlinear optics.", "map": "P^{(3)}=\\chi^{(3)}E_1E_2E_3", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1266", "a": "02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Attosecond X-ray FELs and HHG", "kind": "shared object", "summary": "Attosecond pulses are produced both by high-harmonic generation and by FEL pulse-shortening schemes; they serve the same time-resolved spectroscopy of electrons.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1267", "a": "02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Femtochemistry with ultrafast pulses", "kind": "method transfer", "summary": "Femtosecond pump-probe pulses resolve nuclear motion through transition states and conical intersections; attosecond pulses extend this to electronic dynamics.", "map": "S(\\tau)=\\int I_{pump}(t)\\,I_{probe}(t-\\tau)\\,dt", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1268", "a": "02-electromagnetism-and-optics/photonics-and-lasers/ultrafast-and-attosecond-optics", "b": "11-interdisciplinary-physics/chemical-physics/reaction-dynamics", "name": "Reaction dynamics probed by ultrafast optics", "kind": "method transfer", "summary": "Reaction dynamics supplies the wave-packet and potential-surface questions that ultrafast optics answers, including coherent control and conical-intersection passage.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1269", "a": "02-electromagnetism-and-optics/radiation-and-scattering", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Radiation theory behind light sources", "kind": "identity", "summary": "Synchrotron, undulator and FEL emission follow from the radiation of relativistic accelerated charges described by Liénard–Wiechert fields.", "map": "\\frac{dP}{d\\Omega}\\propto \\left|\\hat n\\times[(\\hat n-\\boldsymbol\\beta)\\times\\dot{\\boldsymbol\\beta}]\\right|^2/(1-\\hat n\\cdot\\boldsymbol\\beta)^5", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1270", "a": "02-electromagnetism-and-optics/radiation-and-scattering", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Scattering and absorption in climate", "kind": "shared object", "summary": "Rayleigh and Mie scattering and molecular absorption set atmospheric radiative transfer, aerosol forcing, cloud albedo and the greenhouse effect.", "map": "\\frac{dI}{ds}=-\\kappa I+j", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1271", "a": "02-electromagnetism-and-optics/radiation-and-scattering/cherenkov-and-transition-radiation", "b": "11-interdisciplinary-physics/medical-physics/nuclear-medicine-and-pet", "name": "Cherenkov timing in PET", "kind": "method transfer", "summary": "Prompt Cherenkov photons from 511 keV photoelectrons in crystals such as BGO are exploited for sub-100 ps time-of-flight PET timing.", "map": "", "breaks": "", "confidence": "current research", "strength": 1}
{"id": "C1272", "a": "02-electromagnetism-and-optics/radiation-and-scattering/cherenkov-and-transition-radiation", "b": "11-interdisciplinary-physics/medical-physics/radiation-therapy", "name": "Cherenkov light in radiotherapy", "kind": "shared object", "summary": "Cherenkov emission from therapy beams in tissue is used for dose imaging and verification; it is also a nuisance in fibre dosimeters.", "map": "", "breaks": "", "confidence": "current research", "strength": 2}
{"id": "C1273", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "11-interdisciplinary-physics/accelerator-physics", "name": "Accelerator radiation losses and damping", "kind": "mechanism", "summary": "Synchrotron radiation loss limits ring energy and, via radiation reaction, provides damping and quantum excitation that set equilibrium emittance.", "map": "U_0=\\frac{4\\pi}{3}\\frac{r_e E^4}{\\rho\\,(mc^2)^3}", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1274", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Light-source design from radiation formulas", "kind": "method transfer", "summary": "Source brightness and spectra are designed using the classical radiation formulas, with coherent enhancement when bunch length falls below the wavelength.", "map": "P_{coh}\\propto N^2 P_1", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1275", "a": "02-electromagnetism-and-optics/radiation-and-scattering/radiation-from-moving-charges", "b": "11-interdisciplinary-physics/accelerator-physics/synchrotron-and-fel-light-sources", "name": "Liénard–Wiechert to undulator radiation", "kind": "identity", "summary": "Bending-magnet and undulator spectra, critical energy and relativistic beaming derive directly from Larmor/Liénard radiation, with $\\gamma$-boosted forward cones.", "map": "\\omega_c=\\tfrac{3}{2}\\gamma^3 c/\\rho,\\;\\theta\\sim 1/\\gamma", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1276", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "11-interdisciplinary-physics/chemical-physics/molecular-spectroscopy", "name": "Raman scattering as inelastic light scattering", "kind": "mechanism", "summary": "Raman spectroscopy is inelastic scattering from polarizability modulation by molecular vibrations, extending Rayleigh scattering from an induced dipole.", "map": "\\mathbf p=\\alpha(Q)\\mathbf E,\\;\\alpha=\\alpha_0+\\alpha'Q", "breaks": "", "confidence": "established", "strength": 3}
{"id": "C1277", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "11-interdisciplinary-physics/earth-atmosphere-and-climate-physics/climate-physics-and-radiative-forcing", "name": "Aerosol and cloud scattering in forcing", "kind": "mechanism", "summary": "Aerosol direct and cloud albedo effects are Mie scattering with size-dependent efficiency; the sky's blue and clouds' white arise from the same Rayleigh-to-Mie crossover.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1278", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "11-interdisciplinary-physics/medical-physics/medical-imaging", "name": "Compton and Rayleigh scattering in X-ray imaging", "kind": "shared object", "summary": "Compton and Rayleigh scattering govern X-ray attenuation, scatter degradation of radiographs and CT contrast, and dose deposition.", "map": "", "breaks": "", "confidence": "established", "strength": 2}
{"id": "C1279", "a": "02-electromagnetism-and-optics/radiation-and-scattering/scattering-of-light", "b": "11-interdisciplinary-physics/medical-physics/ultrasound-and-biomedical-optics", "name": "Light scattering in tissue and diffuse optics", "kind": "shared object", "summary": "Tissue optics relies on Mie/Rayleigh scattering and the diffusion approximation to radiative transfer to image and measure oxygenation in turbid media.", "map": "\\mu_s'=\\mu_s(1-g)", "breaks": "", "confidence": "established", "strength": 2}