---
title: Statistical inference in physics
summary: Frequentist and Bayesian methods for parameter estimation, confidence intervals, hypothesis testing and discovery claims.
query: Bayesian inference; profile likelihood; confidence intervals
---
# Statistical inference in physics
> [Foundations](../../README.md) › [Measurement and data analysis](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Likelihood principle, maximum-likelihood estimators, Fisher information and Cramér–Rao bound, Neyman confidence belts, Feldman–Cousins, CLs, profile likelihood and Wilks' theorem, Bayesian posteriors and priors, MCMC sampling, model comparison (Bayes factors, AIC/BIC), look-elsewhere effect, simulation-based inference.

**Core ideas.**
- Frequentist intervals have guaranteed coverage; Bayesian intervals express degrees of belief given a prior — report which.
- Wilks: $-2\ln\lambda$ is asymptotically $\chi^2$-distributed, giving fast significance estimates.
- Searching many places inflates false positives; correct for trials.

**Key equations.**
$$p(\theta|D)=\frac{p(D|\theta)p(\theta)}{p(D)},\qquad \mathrm{Var}(\hat\theta)\ge\frac{1}{I(\theta)},\qquad Z=\sqrt{q_0}$$

**Landmarks.** Feldman & Cousins (1998); Cowan et al. (2011) — see [subfield landmarks](../README.md).

**See also.** [Cosmological parameter inference](../../../09-astrophysics-and-cosmology/cosmology/flrw-cosmology-and-expansion-history/README.md)
