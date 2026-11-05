---
title: Kinetic theory, Vlasov and Landau damping
summary: Collisionless plasma kinetics — the Vlasov–Maxwell system, Landau damping, velocity-space instabilities, Fokker–Planck collisions and gyrokinetics.
query: Vlasov equation; Landau damping; plasma kinetic theory
---
# Kinetic theory, Vlasov and Landau damping
> [Plasma Physics](../../README.md) › [Plasma fundamentals](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Klimontovich and BBGKY derivations, Vlasov–Poisson and Vlasov–Maxwell systems, linear response and the plasma dielectric function, Landau contour and damping, nonlinear Landau damping (Mouhot–Villani), Bernstein–Greene–Kruskal modes, Lenard–Balescu and Fokker–Planck collision operators, particle-in-cell simulation, gyrokinetic reduction.

**Core ideas.**
- Without collisions, waves still damp: resonant particles near the phase velocity exchange energy with the wave.
- Damping depends on the slope of the distribution at $v=\omega/k$; a positive slope (beam) drives instability instead.
- Landau damping is phase mixing — reversible in principle (plasma echoes).

**Key equations.**
$$\frac{\partial f}{\partial t}+\mathbf v\cdot\nabla f+\frac{q}{m}(\mathbf E+\mathbf v\times\mathbf B)\cdot\nabla_{\mathbf v}f=0,\qquad \gamma\approx\frac{\pi}{2}\frac{\omega_p^3}{k^2}\frac{\partial f_0}{\partial v}\Big|_{v=\omega/k}$$

**Landmark.** Malmberg & Wharton (1964) — see [subfield landmarks](../README.md).

**See also.** [Kinetic theory and Boltzmann equation](../../../03-thermodynamics-and-statistical-mechanics/non-equilibrium-statistical-mechanics/kinetic-theory-and-boltzmann-equation/README.md) · [Gyrokinetics](../../magnetic-confinement-fusion/turbulent-transport-and-gyrokinetics/README.md)
