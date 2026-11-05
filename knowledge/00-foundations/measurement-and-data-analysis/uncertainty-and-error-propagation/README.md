---
title: Uncertainty and error propagation
summary: Quantifying and combining measurement uncertainties — statistical vs. systematic, the GUM framework, correlations and significant figures.
query: measurement uncertainty; error propagation
---
# Uncertainty and error propagation
> [Foundations](../../README.md) › [Measurement and data analysis](../README.md) · Literature: [papers.md](papers.md)

**Scope.** Random vs. systematic errors, Type A and Type B evaluations (GUM), standard and expanded uncertainty, linear error propagation with covariances, Monte Carlo propagation, weighted means, outlier handling, significant figures in reporting.

**Core ideas.**
- Independent uncertainties add in quadrature; correlated ones need the covariance matrix.
- Relative uncertainties add in quadrature for products and quotients.
- The weighted mean of measurements $x_i\pm\sigma_i$ has weights $1/\sigma_i^2$; a large $\chi^2$/dof signals underestimated errors.

**Key equations.**
$$\bar x=\frac{\sum x_i/\sigma_i^2}{\sum1/\sigma_i^2},\qquad \sigma_{\bar x}=\left(\sum\frac1{\sigma_i^2}\right)^{-1/2},\qquad \frac{\sigma_{xy}}{xy}=\sqrt{\left(\frac{\sigma_x}{x}\right)^2+\left(\frac{\sigma_y}{y}\right)^2}$$

**See also.** [Statistical inference](../statistical-inference-in-physics/README.md) · [Fundamental constants](../../units-and-constants/fundamental-constants/README.md)
