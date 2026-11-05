---
title: Stochastic processes and Langevin dynamics
summary: Random processes in physics — Brownian motion, Langevin and Fokker–Planck equations, master equations, first-passage and escape rates.
query: Langevin equation; Fokker-Planck equation; Brownian motion
---
# Stochastic processes and Langevin dynamics
> [Thermodynamics and Statistical Mechanics](../../README.md) › [Non-equilibrium](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Random walks and diffusion, Wiener process, Itô vs. Stratonovich calculus, Langevin and overdamped Langevin equations, Ornstein–Uhlenbeck process, Fokker–Planck and Smoluchowski equations, master equations and detailed balance, Kramers escape rate, first-passage times, Lévy flights and anomalous diffusion.

**Core ideas.**
- Brownian motion: $\langle x^2\rangle=2Dt$; Einstein's relation links $D$ to friction and temperature (used by Perrin to measure $N_A$).
- Fokker–Planck describes the evolving probability density for the same physics as Langevin trajectories.
- Barrier crossing rates are Arrhenius-like: $k\propto e^{-\Delta U/k_BT}$.

**Key equations.**
$$\frac{\partial P}{\partial t}=-\frac{\partial}{\partial x}\left[\frac{F(x)}{\gamma}P\right]+D\frac{\partial^2P}{\partial x^2},\qquad k_{\text{Kramers}}=\frac{\omega_0\omega_b}{2\pi\gamma}e^{-\Delta U/k_BT}$$

**See also.** [Lindblad dynamics (quantum analogue)](../../../04-quantum-physics/open-and-many-body-quantum-dynamics/lindblad-master-equations/README.md) · [Single-molecule biophysics](../../../11-interdisciplinary-physics/biophysics/single-molecule-biophysics/README.md)
