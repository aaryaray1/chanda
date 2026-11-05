---
title: Mathematical methods
summary: The mathematics physicists use daily — linear algebra and Hilbert spaces, differential equations and Green's functions, complex analysis and special functions, tensors and differential geometry.
query: mathematical methods; differential geometry; special functions
source: inspire
arxiv: math-ph
---
# Mathematical methods

> Part of [Foundations](../README.md) · Key reviews: [papers.md](papers.md)

## Overview
Most of physics reduces to a few mathematical structures: vector spaces and their operators (quantum mechanics, normal modes), linear differential equations and their Green's functions (electrostatics, waves, diffusion), analytic functions (dispersion relations, contour integrals), and tensors on manifolds (relativity, continuum mechanics). Fluency here is what makes the rest of the tree readable.

## Topics
- [Linear algebra and Hilbert spaces](linear-algebra-and-hilbert-spaces/README.md) — eigenproblems, spectral theorem, function spaces.
- [Differential equations and Green's functions](differential-equations-and-greens-functions/README.md) — ODEs, PDEs, Sturm–Liouville, propagators.
- [Complex analysis and special functions](complex-analysis-and-special-functions/README.md) — residues, dispersion relations, Bessel/Legendre/Hermite.
- [Tensors and differential geometry](tensors-and-differential-geometry/README.md) — index notation, manifolds, curvature, forms.

## Conceptual spine
1. Linearity → superposition → expand in eigenfunctions of a self-adjoint operator.
2. Green's function = response to a point source; solution = source convolved with it.
3. Analyticity ↔ causality (Kramers–Kronig).
4. Coordinate-free (tensor) statements are the ones with physical meaning.

## Key equations
$$\mathcal L G(\mathbf x,\mathbf x')=\delta(\mathbf x-\mathbf x'),\qquad u(\mathbf x)=\int G(\mathbf x,\mathbf x')f(\mathbf x')\,d\mathbf x'$$
$$\oint_Cf(z)\,dz=2\pi i\sum\mathrm{Res}f,\qquad \mathrm{Re}\,\chi(\omega)=\frac1\pi\,\mathcal P\!\!\int\frac{\mathrm{Im}\,\chi(\omega')}{\omega'-\omega}d\omega'$$

## Landmark papers
- Wigner (1960). "The unreasonable effectiveness of mathematics in the natural sciences". *Commun. Pure Appl. Math.* 13, 1. [doi:10.1002/cpa.3160130102](https://doi.org/10.1002/cpa.3160130102)

## Open problems
- Rigorous foundations for quantum field theory (constructive QFT, path-integral measures).
- Global regularity of 3D Navier–Stokes (Clay problem).

## Connections
- [Symmetry and group theory](../symmetry-and-group-theory/README.md) · [Quantum mechanics formalism](../../04-quantum-physics/quantum-mechanics-core/README.md) · [General relativity](../../05-relativity-and-gravitation/general-relativity/README.md)
