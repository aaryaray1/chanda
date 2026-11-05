---
title: Foundations — Mathematics, Computation and Measurement
summary: The shared toolkit of every branch — mathematical methods, symmetry, computational physics, measurement and statistics, units and constants, and the history and philosophy of physics.
arxiv: math-ph physics.comp-ph physics.data-an physics.hist-ph physics.ed-ph
source: openalex
agent: foundations-physicist
---
# Foundations — Mathematics, Computation and Measurement

> **Specialist:** `foundations-physicist` · **arXiv:** math-ph, physics.comp-ph, physics.data-an, physics.hist-ph, physics.ed-ph · **Literature source:** OpenAlex + arXiv

## What this field studies
Every physics branch rests on the same foundations: the mathematics used to state laws, the symmetries that constrain them, the numerical methods that solve them when pen and paper fail, the statistics that connect them to data, the units in which results are reported, and the history and philosophy that explain why physics looks the way it does. Questions about *how* to solve, estimate, measure or reason belong here; questions about a specific system belong to its field.

## Branch map
| Branch | What it covers |
|---|---|
| [Mathematical methods](mathematical-methods/README.md) | Linear algebra and Hilbert spaces, ODEs/PDEs and Green's functions, complex analysis, tensors and geometry |
| [Symmetry and group theory](symmetry-and-group-theory/README.md) | Lie groups, Noether's theorem, discrete symmetries, spontaneous symmetry breaking |
| [Computational physics](computational-physics/README.md) | Numerical ODE/PDE methods, Monte Carlo, molecular dynamics, tensor networks, machine learning |
| [Measurement and data analysis](measurement-and-data-analysis/README.md) | Uncertainty propagation, statistical inference, detectors and instrumentation |
| [Units, constants and dimensional analysis](units-and-constants/README.md) | The 2019 SI, CODATA constants, scaling arguments, natural and Planck units |
| [History and philosophy of physics](history-and-philosophy-of-physics/README.md) | How physics developed, conceptual foundations, physics education research |

## Conventions used across the knowledge base
- **SI units by default.** Natural units ($\hbar=c=1$) in particle physics, geometrized units ($G=c=1$) in GR, Gaussian units in some EM and plasma texts — always state the system and convert when comparing.
- **Constants:** CODATA 2022 values from NIST, stored in [codata-2022.md](units-and-constants/codata-2022.md) and searchable with `python -I scripts/physlib.py constants <name>`.
- **Uncertainties:** quote standard (1σ) uncertainties as $x = 1.234(5)$ or $1.234\pm0.005$; state whether statistical, systematic or combined.
- **Vectors** bold or with arrows; Einstein summation over repeated indices unless noted.

## Historical spine
1687 *Principia* · 1736–1788 Euler and Lagrange's analytical mechanics · 1822 Fourier analysis · 1828 Green's functions · 1854 Riemannian geometry · 1873 Lie groups · 1918 Noether's theorem · 1925–32 Hilbert space QM (von Neumann) · 1946 ENIAC; 1953 Metropolis Monte Carlo · 1960 Wigner's "unreasonable effectiveness" · 1972 "More is different" · 2019 SI redefinition · 2024 Nobel Prize for physics-inspired neural networks.

## Canonical textbooks
- Boas, *Mathematical Methods in the Physical Sciences* — undergraduate standard.
- Arfken, Weber & Harris, *Mathematical Methods for Physicists*; Riley, Hobson & Bence, *Mathematical Methods for Physics and Engineering*.
- Georgi, *Lie Algebras in Particle Physics*; Zee, *Group Theory in a Nutshell for Physicists*.
- Press et al., *Numerical Recipes*; Newman, *Computational Physics*; Landau & Binder, *A Guide to Monte Carlo Simulations in Statistical Physics*.
- Taylor, *An Introduction to Error Analysis*; Barlow, *Statistics*; Sivia & Skilling, *Data Analysis: A Bayesian Tutorial*.
- Kuhn, *The Structure of Scientific Revolutions*; Pais, *Subtle is the Lord*; Maudlin, *Philosophy of Physics* (2 vols.).

## How the specialist works here
Pick the right tool before computing: exploit symmetry, nondimensionalize, estimate orders of magnitude, then solve analytically or numerically with an explicit check (convergence, conservation laws, known limits). For data questions, write the likelihood first.
