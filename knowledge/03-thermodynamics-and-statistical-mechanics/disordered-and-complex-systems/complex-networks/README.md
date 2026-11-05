---
title: Complex networks
summary: Statistical physics of networks — random graphs, small worlds, scale-free degree distributions, robustness and spreading processes.
query: complex networks; scale-free network; small-world network
---
# Complex networks
> [Thermodynamics and Statistical Mechanics](../../README.md) › [Disordered and complex systems](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Erdős–Rényi graphs and the giant-component transition, small-world networks, preferential attachment and scale-free distributions, clustering and community detection, robustness to random failure vs. targeted attack, epidemic thresholds (SIR/SIS), synchronization on networks, multilayer networks.

**Core ideas.**
- A few shortcuts make path lengths logarithmic in network size (small-world effect).
- Preferential attachment yields $P(k)\sim k^{-3}$; hubs make networks robust to random loss but fragile to attack.
- In scale-free networks with $\gamma\le3$ the epidemic threshold vanishes as $N\to\infty$.

**Key equations.**
$$P(k)\sim k^{-\gamma},\qquad \lambda_c=\frac{\langle k\rangle}{\langle k^2\rangle}$$

**Landmarks.** Watts & Strogatz (1998); Barabási & Albert (1999) — see [subfield landmarks](../README.md).

**See also.** [Synchronization](../../../01-classical-mechanics/nonlinear-dynamics-and-chaos/synchronization-and-pattern-formation/README.md) · [Percolation](../percolation/README.md)
