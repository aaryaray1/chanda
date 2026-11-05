---
title: Machine learning in high-energy physics
summary: Deep learning for jet tagging, fast simulation, triggering, anomaly detection and simulation-based inference.
query: machine learning; deep learning; jet tagging; anomaly detection
arxiv: hep-ex hep-ph physics.data-an
---
# Machine learning in high-energy physics
> [Particle Physics](../../README.md) › [Collider & experimental](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Graph neural networks and transformers on particle clouds (ParticleNet, ParT), b-tagging, generative models for calorimeter simulation, FPGA inference in triggers, weakly/unsupervised anomaly detection, simulation-based (likelihood-free) inference, foundation models for jets.

**Core ideas.**
- Events are naturally sets/graphs of particles; permutation-invariant architectures fit the data.
- Classifier outputs approximate likelihood ratios (Neyman–Pearson), connecting ML to optimal statistics.
- Systematic uncertainties and simulation–data mismatch are the main obstacles to trusting ML in final results.

**Key equations.**
$$s^*(x)=\frac{p(x|S)}{p(x|S)+p(x|B)}\ \Rightarrow\ \frac{s^*}{1-s^*}=\frac{p(x|S)}{p(x|B)}$$

**See also.** [Machine learning for physics](../../../00-foundations/computational-physics/machine-learning-for-physics/README.md) · [Jets](../jets-and-qcd-phenomenology/README.md)
