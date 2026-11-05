---
title: Measurement and data analysis
summary: How physical quantities are measured and inferred — uncertainty propagation, statistical inference, detectors and instrumentation.
query: measurement uncertainty; statistical data analysis physics
arxiv: physics.data-an physics.ins-det
---
# Measurement and data analysis

> Part of [Foundations](../README.md) · Key reviews: [papers.md](papers.md)

## Overview
A measurement is only as meaningful as its uncertainty. This branch covers the statistics of estimating parameters and testing hypotheses (frequentist and Bayesian), propagating errors, separating statistical from systematic effects, and the instruments that transduce physical quantities into data.

## Topics
- [Uncertainty and error propagation](uncertainty-and-error-propagation/README.md) — Type A/B uncertainties, GUM, covariance.
- [Statistical inference in physics](statistical-inference-in-physics/README.md) — likelihoods, Bayesian inference, hypothesis tests, discovery significance.
- [Detectors and instrumentation](detectors-and-instrumentation/README.md) — sensors, noise, amplifiers, lock-in detection.

## Conceptual spine
1. Model the measurement: $x=\mu+\text{noise}$; write the likelihood $L(\theta)=p(\text{data}|\theta)$.
2. Estimate (maximum likelihood or posterior), then quote an interval with its coverage or credibility.
3. Systematics enter as nuisance parameters — profile or marginalize them.
4. Blind analyses and pre-registration prevent bias; replication is the final check.

## Key equations
$$\sigma_f^2=\sum_{i,j}\frac{\partial f}{\partial x_i}\frac{\partial f}{\partial x_j}V_{ij},\qquad \chi^2=\sum_i\frac{(y_i-f(x_i;\theta))^2}{\sigma_i^2},\qquad q_0=-2\ln\frac{L(0,\hat{\hat\theta})}{L(\hat\mu,\hat\theta)}$$

## Landmark papers
- Feldman & Cousins (1998). "Unified approach to the classical statistical analysis of small signals". *Phys. Rev. D* 57, 3873. [arXiv:physics/9711021](https://arxiv.org/abs/physics/9711021)
- Read (2002). "Presentation of search results: the CLs technique". *J. Phys. G* 28, 2693. [doi:10.1088/0954-3899/28/10/313](https://doi.org/10.1088/0954-3899/28/10/313)
- Cowan, Cranmer, Gross & Vitells (2011). "Asymptotic formulae for likelihood-based tests of new physics". *Eur. Phys. J. C* 71, 1554. [arXiv:1007.1727](https://arxiv.org/abs/1007.1727)

## Open problems
- Reproducibility and the "look-elsewhere effect" in large searches.
- Uncertainty quantification for machine-learned analyses.

## Connections
- [Collider and experimental physics](../../06-particle-physics/collider-and-experimental-particle-physics/README.md) · [Units and constants](../units-and-constants/README.md)
