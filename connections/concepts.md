---
title: Cross-branch concept lexicon
summary: Curated list of concepts that recur across branches, with the terms used to detect them in the notes. Drives the concept index and the latent-bridge candidates in CONNECTIONS.md.
---
# Cross-branch concept lexicon

Curated, edit freely. `python -I scripts/physlib.py tree` scans every note in `knowledge/` for each concept's terms and rebuilds the concept index, the field-by-field bridge counts and the *latent bridge* candidates in `CONNECTIONS.md`, `library/connections.json` and the `codex-atlas` skill.

How terms match: lowercase, separated by `;`. Each term matches at the start of a word, so `turbulen` also catches *turbulent* and *turbulence*. Math is stripped first, and en/em dashes count as hyphens. Prefer multi-word terms, because a bare common word inflates the index.

| Concept | Terms | Unifying idea |
|---|---|---|
| Spontaneous symmetry breaking | spontaneous symmetry breaking; spontaneously broken; goldstone; order parameter; broken symmetry | A ground state with less symmetry than the laws; gapless Goldstone modes or, with gauge fields, massive ones |
| Higgs–Anderson mechanism | higgs mechanism; anderson-higgs; meissner; london penetration; massive photon | Gauge field acquires mass by eating the Goldstone mode — the same physics in superconductors and electroweak theory |
| Gauge symmetry | gauge invarian; gauge theor; gauge field; gauge symmetr; yang-mills; gauge boson; minimal coupling | Redundancy of description that fixes the form of interactions |
| Noether symmetries and conservation | noether; conserved current; conservation law; conserved quantit | Continuous symmetry ⇔ conserved charge |
| Discrete symmetries | parity; time reversal; time-reversal; charge conjugation; cpt; cp violation | P, T, C and their violations constrain dynamics from nuclei to topological insulators |
| Group theory and representations | lie group; lie algebra; irreducible representation; su(2); su(3); so(3); lorentz group; poincaré group; poincaré symmetry | Symmetry groups label states and organize multiplets |
| Renormalization group | renormalization group; renormalisation group; running coupling; beta function; wilsonian; coarse-grain | How physics changes with scale; fixed points control long-distance behavior |
| Universality and scaling | universality; critical exponent; scaling law; scale invarian; conformal; self-similar; power law | Microscopically different systems share exponents near fixed points |
| Phase transitions and criticality | phase transition; critical point; critical phenomen; quantum critical; first-order transition; continuous transition | Non-analytic change of state; fluctuations at all scales near criticality |
| Effective field theory | effective field theor; effective theor; chiral perturbation; low-energy theor; separation of scales; integrating out | Physics at one scale described without knowing the next, with controlled corrections |
| Mean-field and self-consistent theories | mean-field; mean field; hartree-fock; hartree; self-consistent; random phase approximation | Replace fluctuating neighbours by their average; exact in high dimension or large N |
| Density functional methods | density functional; kohn-sham; thomas-fermi; energy density functional | Ground-state properties from the density alone — electrons, nuclei, classical fluids |
| Path integrals and imaginary time | path integral; functional integral; wick rotation; imaginary time; euclidean action | Quantum amplitudes as sums over histories; Wick rotation maps QFT onto statistical mechanics |
| Partition functions and ensembles | partition function; boltzmann factor; canonical ensemble; grand canonical; microcanonical; gibbs distribution | Thermodynamics from counting states |
| Entropy and information | entropy; information theor; shannon; landauer; mutual information; maxwell's demon | Entropy as missing information, from heat engines to black holes and qubits |
| Entanglement | entanglement; entangled; bell inequalit; bell test; nonlocal | Correlations without a classical description; organizes many-body states and spacetime |
| Holography and gauge/gravity duality | holograph; ads/cft; gauge/gravity; anti-de sitter; maldacena | A gravity theory in the bulk equals a quantum field theory on the boundary |
| Black-hole thermodynamics | hawking radiation; bekenstein; black-hole entropy; black hole entropy; unruh; information paradox | Black holes have temperature and entropy; links gravity, quantum fields and thermodynamics |
| Analogue gravity | analogue gravity; analog gravity; acoustic black hole; sonic horizon; analogue horizon; analog horizon | Wave propagation in flowing media mimics curved spacetime |
| Quasiparticles and collective modes | quasiparticle; collective excitation; collective mode; phonon; magnon; plasmon; exciton; polariton | Interacting systems behave like gases of emergent particles |
| Bose–Einstein condensation and superfluidity | bose-einstein; superfluid; condensate; bec | Macroscopic occupation of one quantum state — cold atoms, helium, neutron stars, superconductors |
| Pairing and BCS physics | cooper pair; bcs; pairing; pairing gap; bogoliubov | Attractive interactions pair fermions and open a gap — metals, nuclei, neutron stars, cold atoms |
| Fermi surfaces and degenerate matter | fermi liquid; fermi surface; fermi energy; fermi sea; degeneracy pressure; degenerate matter; degenerate electron; pauli exclusion | Pauli blocking sets the low-energy physics of electrons, nucleons and compact stars |
| Topological invariants | topological invariant; chern number; chern; winding number; z2 invariant; homotopy; topological order; topological phase | Integer-valued properties robust to smooth deformation |
| Berry and geometric phases | berry phase; berry curvature; berry connection; geometric phase; pancharatnam; aharonov-bohm; hannay | Holonomy of a state transported around a loop in parameter space |
| Topological defects | vortex; vortices; domain wall; monopole; skyrmion; cosmic string; disclination; dislocation | Order-parameter singularities classified by homotopy — from liquid crystals to the early universe |
| Solitons and nonlinear waves | soliton; solitary wave; kink; nonlinear schrödinger; korteweg | Shape-preserving waves where nonlinearity balances dispersion |
| Tunnelling and instantons | tunnelling; tunneling; instanton; wkb; barrier penetration | Classically forbidden transitions dominated by Euclidean saddle points |
| Anomalies | chiral anomaly; axial anomaly; quantum anomal; anomaly inflow; anomaly cancellation | A classical symmetry broken by quantization; links particle physics to topological matter |
| Anyons and fractional statistics | anyon; fractional statistics; fractional charge; braiding; non-abelian | Exchange statistics beyond bosons and fermions in two dimensions |
| Dirac, Weyl and Majorana fermions | majorana; dirac fermion; dirac cone; dirac point; weyl fermion; weyl semimetal; dirac equation | Relativistic wave equations reappear as emergent low-energy physics in solids |
| Confinement and chiral symmetry breaking | confinement; asymptotic freedom; chiral symmetry breaking; quark-gluon plasma; color superconduct | QCD's strong coupling generates hadron masses and new phases of matter |
| Vacuum energy and fluctuations | vacuum energy; vacuum fluctuation; zero-point; casimir; cosmological constant; false vacuum | The quantum vacuum has structure, with measurable and cosmological consequences |
| Inflation and early-universe physics | inflation; reheating; baryogenesis; primordial; phase transition in the early universe | Field theory and statistical physics applied to the first instants |
| Green's functions and propagators | green's function; green function; propagator; response function; spectral function | Response to a point source; the same object in electrostatics, QFT and many-body theory |
| Linear response and fluctuation–dissipation | fluctuation-dissipation; linear response; kubo; green-kubo; onsager; susceptibilit | Response to a small push is fixed by equilibrium fluctuations |
| Dispersion relations and causality | kramers-kronig; causality; analyticity; dispersion relation | Causality makes response functions analytic, linking absorption and refraction |
| Scattering theory | cross section; scattering amplitude; s-matrix; born approximation; partial wave; optical theorem; rutherford; form factor | Probing structure by what comes out — from atoms to quarks to galaxies |
| Waves and wave equations | wave equation; group velocity; phase velocity; wave packet; standing wave; helmholtz | One mathematics for sound, light, matter waves and gravitational waves |
| Oscillators and resonance | harmonic oscillator; resonance; resonant; normal mode; coupled oscillator | The universal small-oscillation model and its quantum version |
| Variational principles | least action; stationary action; variational principle; variational method; fermat's principle; euler-lagrange; lagrangian | Laws as extremum conditions; the action is the common language of all branches |
| Hamiltonian structure and phase space | hamiltonian; symplectic; poisson bracket; phase space; liouville | Phase-space geometry underlies classical, statistical and quantum dynamics |
| Chaos and nonlinear dynamics | chaos; chaotic; lyapunov; strange attractor; bifurcation; ergodic; kam | Deterministic unpredictability; ergodicity as the bridge to statistical mechanics |
| Instabilities | instabilit; unstable mode; growth rate | Small perturbations that grow — fluids, plasmas, stars, lasers |
| Turbulence and cascades | turbulen; kolmogorov; energy cascade; inertial range; intermittency | Multiscale chaotic flow in fluids, plasmas, astrophysics and wave systems |
| Hydrodynamics and continuum descriptions | hydrodynamic; navier-stokes; euler equation; viscosity; viscous; continuity equation; conservation equations | Long-wavelength dynamics of conserved densities — from water to quark–gluon plasma |
| Kinetic theory and transport | boltzmann equation; kinetic theory; vlasov; collision integral; transport coefficient; mean free path; relaxation time | Distribution-function dynamics between microscopic and hydrodynamic scales |
| Diffusion, Brownian motion and stochastic processes | brownian; random walk; diffusion; langevin; fokker-planck; stochastic process; noise | Random microscopic kicks produce universal macroscopic laws |
| Non-equilibrium fluctuation theorems | jarzynski; crooks; fluctuation theorem; stochastic thermodynamics; entropy production | Exact relations for driven small systems |
| Disorder and localization | anderson localization; localization; disorder; random potential; many-body localization | Interference in random media halts transport — electrons, light, sound, cold atoms |
| Glasses, spin glasses and rugged landscapes | spin glass; glass transition; energy landscape; replica; frustration; frustrated | Many competing minima — glasses, proteins, optimization, neural networks |
| Ising and lattice models | ising; potts; heisenberg model; hubbard; xy model; lattice model; tight-binding | Minimal models whose behavior is universal across physics and beyond |
| Monte Carlo and stochastic sampling | monte carlo; metropolis; markov chain; importance sampling | Sampling replaces exact enumeration in statistical, quantum and particle physics |
| Tensor networks and entanglement-based numerics | tensor network; dmrg; matrix product; peps; mera | Compressing quantum states by their entanglement structure |
| Machine learning and physics | machine learning; neural network; deep learning; boltzmann machine; hopfield | Learning machines as statistical-physics systems, and as tools for physics |
| Spin and angular momentum | spin-orbit; angular momentum; spinor; spin-1/2; magnetic moment; g-factor | Rotational structure and its coupling to motion and fields |
| Magnetism and exchange | exchange interaction; ferromagnet; antiferromagnet; magnetization; superexchange; magnetic order | Quantum exchange produces collective magnetic order |
| Equations of state | equation of state | Pressure–density relations connect microphysics to stars, nuclei and the cosmos |
| Compact objects | neutron star; white dwarf; black hole; compact object; chandrasekhar; pulsar | Matter at extreme density and gravity — where nuclear, particle, GR and astro meet |
| Nucleosynthesis | nucleosynthesis; r-process; s-process; big bang nucleosynthesis; bbn | How the elements formed, linking nuclear rates to stellar and cosmic histories |
| Neutrinos | neutrino | Weakly interacting probes from reactors, the Sun, supernovae and the early universe |
| Dark matter | dark matter; wimp; axion; dark photon | Unseen mass connecting cosmology, particle physics and precision detectors |
| Hydrostatic and virial equilibrium | hydrostatic equilibrium; virial; jeans; gravitational collapse | Balance of pressure and gravity from stars to clouds to clusters |
| Radiation, blackbody and radiative transfer | radiative transfer; opacity; blackbody; black-body; planck spectrum; stefan-boltzmann; planck's law | Matter–light equilibrium, from the CMB to climate |
| Radiation by accelerated charges | synchrotron; bremsstrahlung; larmor; cherenkov; čerenkov; dipole radiation; free-electron laser | One radiation formula powering light sources, astrophysical emission and diagnostics |
| Lasers, coherence and stimulated emission | laser; coherence; coherent state; stimulated emission; population inversion | Phase-coherent light from stimulated emission; coherence as an order parameter |
| Interference and diffraction | interferen; diffraction; interferometer; interferometr | Phase-sensitive superposition, used from crystallography to gravitational-wave detection |
| Magnetohydrodynamics, dynamos and reconnection | magnetohydrodynamic; mhd; dynamo; magnetic reconnection; reconnection; alfvén; alfven | Conducting fluids carry and amplify magnetic fields — lab, solar, galactic |
| Plasma oscillations, screening and Landau damping | landau damping; debye; plasma frequency; plasma oscillation; screening | Collective long-range Coulomb physics in plasmas, metals and quark matter |
| Decoherence and open quantum systems | decoherence; open quantum system; lindblad; master equation; measurement problem; dissipation | How environments make quantum systems look classical |
| Quantum simulation and cold atoms | quantum simulat; optical lattice; cold atom; ultracold; feshbach | Engineered quantum systems emulate models from condensed matter, nuclear and high-energy physics |
| Precision measurement and sensing | atomic clock; optical clock; precision measurement; quantum sensing; squeez; quantum metrology; standard quantum limit | Pushing measurement to fundamental limits to test fundamental physics |
| Statistical inference | statistical inference; likelihood; bayesian; p-value; confidence interval; look-elsewhere | How evidence is weighed — from discovery claims to cosmological parameters |
| Dimensional analysis and scaling arguments | dimensional analysis; buckingham; dimensionless; similarity; order-of-magnitude | Units constrain physics before any equation is solved |
| Elasticity and continuum mechanics | elastic; stress tensor; strain; elasticity; young's modulus | Continuum response of solids — from metals to neutron-star crusts and cells |
| Heat engines and efficiency limits | carnot; heat engine; efficiency limit; shockley-queisser; thermoelectric | Thermodynamic bounds on converting energy |
| Gravitational waves | gravitational wave; gravitational-wave | Ripples of spacetime as a new messenger |
| Active matter and collective behavior | active matter; flocking; collective behavio; self-propelled; swarm; motility | Energy-consuming agents form ordered, flowing phases — from bacteria to birds |
| Emergence | emergen | The whole has laws its parts do not — the organizing theme of many-body physics |
| Dualities | duality; dual description; t-duality; s-duality; electric-magnetic; bulk-boundary; bulk–boundary; kramers-wannier | Two descriptions of one physics, often weak ↔ strong coupling |
