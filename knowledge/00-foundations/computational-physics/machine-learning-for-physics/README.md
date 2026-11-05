---
title: Machine learning for physics
summary: Neural networks as tools for physics — surrogates, physics-informed networks, neural quantum states, symbolic regression and ML-assisted discovery.
query: physics-informed neural network; machine learning physics; neural quantum states
openalex_filter: primary_topic.field.id:31|17
---
# Machine learning for physics
> [Foundations](../../README.md) › [Computational physics](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Physics-informed neural networks (PINNs), neural operators, equivariant networks, neural-network quantum states, generative models for sampling (normalizing flows), symbolic regression, ML for experiment control, and the statistical physics of learning (Hopfield, Boltzmann machines).

**Core ideas.**
- Build symmetries and conservation laws into architectures (equivariance) rather than hoping the network learns them.
- PINNs penalize the PDE residual in the loss, combining data and equations.
- ML outputs are hypotheses: validate against held-out physics (limits, conservation, independent simulations).

**Key equations.**
$$\mathcal L=\frac1N\sum_i|u_\theta(x_i)-u_i|^2+\lambda\frac1M\sum_j|\mathcal N u_\theta\,(x_j)|^2$$

**Landmarks.** Carleo et al. (2019) — see [subfield landmarks](../README.md) · Raissi, Perdikaris & Karniadakis (2019). "Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations". *J. Comput. Phys.* 378, 686. [doi:10.1016/j.jcp.2018.10.045](https://doi.org/10.1016/j.jcp.2018.10.045)

**See also.** [Statistical physics of learning](../../../03-thermodynamics-and-statistical-mechanics/disordered-and-complex-systems/statistical-physics-of-learning/README.md) · [ML in HEP](../../../06-particle-physics/collider-and-experimental-particle-physics/machine-learning-in-hep/README.md)
