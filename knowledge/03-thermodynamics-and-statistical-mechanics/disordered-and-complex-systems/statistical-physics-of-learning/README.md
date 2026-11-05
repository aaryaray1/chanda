---
title: Statistical physics of learning
summary: Neural networks and inference through statistical mechanics — Hopfield networks, Boltzmann machines, perceptron capacity, and theory of deep learning.
query: Hopfield network; Boltzmann machine; statistical mechanics of learning
---
# Statistical physics of learning
> [Thermodynamics and Statistical Mechanics](../../README.md) › [Disordered and complex systems](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Hopfield associative memory and its storage capacity, Boltzmann machines and energy-based models, Gardner's perceptron capacity, teacher–student models, phase transitions in inference (replica, cavity, approximate message passing), double descent, neural tangent kernel and mean-field limits, diffusion models as non-equilibrium physics, modern Hopfield networks and attention.

**Core ideas.**
- Memories as energy minima: Hopfield networks store $\sim0.138N$ random patterns before catastrophic failure.
- Learning is inference in high dimensions — sharp phase transitions separate learnable from unlearnable regimes.
- Overparameterized networks interpolate data yet generalize; statistical physics gives exact asymptotics in solvable models.

**Key equations.**
$$E=-\frac12\sum_{ij}w_{ij}s_is_j,\ w_{ij}=\frac1N\sum_\mu\xi_i^\mu\xi_j^\mu;\qquad \alpha_c^{\text{Hopfield}}\approx0.138,\ \alpha_c^{\text{perceptron}}=2$$

**Landmarks.** Hopfield (1982); Ackley, Hinton & Sejnowski (1985) — see [subfield landmarks](../README.md).

**See also.** [Machine learning for physics](../../../00-foundations/computational-physics/machine-learning-for-physics/README.md) · [Spin glasses](../spin-glasses/README.md)
