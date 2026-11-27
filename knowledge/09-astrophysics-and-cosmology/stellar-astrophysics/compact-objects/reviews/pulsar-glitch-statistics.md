# Pulsar glitch statistics: correlations, forecasts and predictability (project results)
> [Compact objects](../README.md) · Results from this project's frontier stage ([plan](../../../../../connections/frontier/PLAN.md)). Each was pre-registered (plan committed before scoring) and refereed.

**Scope.** What the public glitch catalogues say about how glitches are triggered and how far ahead they can be forecast. Glitches are sudden spin-ups of a neutron star, thought to come from superfluid vortices unpinning in the crust. Data: the Jodrell Bank glitch catalogue (snapshot 2026-11-20; 736 glitches in 225 pulsars).

**Results.** *Tier T* means a pre-registered test on public data.

| Test | Question | Status | Result |
|---|---|---|---|
| [T01](../../../../../connections/frontier/results/T01-glitch-correlations.md) | Do the 2018 size–waiting-time correlations hold on newer glitches? | T · partly known | The predicted absence of a backward correlation holds in 10 pulsars. Whether forward correlations scale with spin-down is inconclusive. |
| [T03](../../../../../connections/frontier/results/T03-glitch-epoch-forecasts.md) | Did the 2019 state-dependent Poisson forecasts come true? | T · out-of-sample | All 3 fell within 2σ. The uncertainties were wide. |
| [T04](../../../../../connections/frontier/results/T04-glitch-forecast-scorecard.md) | How good are published next-glitch forecasts? | T · refereed twice | 2 of 6 resolved primary forecasts fell within their 1σ. Four are overdue, and one of those is a confirmed miss. Too few to judge calibration. |
| [G1](../../../../../connections/frontier/results/G1-glitch-predictability.md) | How predictable are glitches, out of sample? | T · method new, result partly known | A two-parameter renewal forecast is calibrated: 208 of 231 inside its 90% interval. Timing departs significantly from Poisson (calibrated null, post hoc), but the forecast gain is small, about 0.1 nats per forecast. |
| [G2](../../../../../connections/frontier/results/G2-two-glitch-populations.md) | Large glitches predictable, small ones Poisson? | T · partly known | Large glitches (Δν/ν ≥ 10⁻⁷) are non-Poisson, with longer waits after bigger glitches (robust in J0537−6910, Vela, J1413−6141 and J1740−3015). Small glitches are consistent with Poisson, and their sizes add nothing. |
| [G3](../../../../../connections/frontier/results/G3-glitch-aftershocks.md) | Do glitches have earthquake-like aftershocks? | T · partly known | None resolvable beyond about a month. The apparent deficit at shorter waits is the catalogue's time resolution. |
| [V1](../../../../../connections/frontier/results/V1-vortex-creep-interglitch.md) | Do vortex-creep "times to the next glitch" track the observed intervals? | T · meta-analysis, refereed | In-sample, yes: 35 published pairs, within-pulsar ρ = +0.66, and better than the pulsar's own mean in 25 of 34. But glitch size alone tracks the intervals almost as well, the fits span the interval, and the one clean forecast made beforehand did worse than the baseline. Consistency, not yet forecast skill. |
| [B1](../../../../../connections/frontier/results/B1-blind-vela-recovery.md) | Does Vela's early post-glitch recovery forecast its next glitch? (blind, Fermi-LAT photons) | T · pre-registered | No: the linear-recovery relation, measured from data within 410 d after each glitch, beats Vela's own mean interval in 2 of 5 and predicts every next glitch early (5 of 5). |

**Reading.**
- **Two kinds of glitch.** The time-domain data favour one reservoir with two kinds of trigger: deterministic for large glitches and random for small ones. Fuentes, Espinoza & Reisenegger (2019) proposed this in-sample, and G2 confirms it out of sample at one fixed threshold.
- **Model forecasts.** Published model forecasts have so far not been shown to beat a simple statistical forecast that is honest about its uncertainty.
- **No aftershocks.** Glitches show no aftershock clustering at the catalogue's resolution. Earthquakes show such clustering, and so do repeating fast radio bursts on sub-second scales (Totani & Tsuzuki 2023).

**Registered forecasts, to be checked.**
- **G1:** next-glitch forecasts for 34 pulsars.
- **G2-P:** next-large-glitch forecasts for 7 pulsars, with a **Vela head-to-head** that resolves by 2027-04-11 ([registration](../../../../../connections/frontier/prereg/G2P-large-glitch-forecasts.md)). The probability of a large Vela glitch by then: Grover et al. 0.71, Vela's own past waits 0.31, our models 0.13.
- **T02:** whether three forward correlations persist on unseen glitches.

**Open questions.**
- Does a refractory interval exist among *large* follow-ups only, where recovery masking cannot act? This needs more large-glitch pairs, or a merged catalogue.
- Is the large-glitch reservoir signal one law across pulsars, or several pulsar-specific ones?

**Key sources.**
- Melatos & Warszawski (2009). "Superfluid vortex unpinning as a coherent noise process, and the scale invariance of pulsar glitches". *ApJ* 700, 1524. [arXiv:0904.2998](https://arxiv.org/abs/0904.2998)
- Fuentes, Espinoza & Reisenegger (2019). "Glitch time series and size distributions in eight prolific pulsars". *A&A* 630, A115. [arXiv:1907.09887](https://arxiv.org/abs/1907.09887)
- Melatos & Drummond (2019). "Pulsar glitch activity as a state-dependent Poisson process: parameter estimation and epoch prediction". *ApJ* 885, 37. [arXiv:1910.05503](https://arxiv.org/abs/1910.05503)
- Carlin & Melatos (2019). "Autocorrelations in pulsar glitch waiting times and sizes". *MNRAS* 488, 4890. [arXiv:1907.09143](https://arxiv.org/abs/1907.09143)
- Middleditch et al. (2006). "Predicting the Starquakes in PSR J0537-6910". *ApJ* 652, 1531. [arXiv:astro-ph/0605007](https://arxiv.org/abs/astro-ph/0605007)
- Basu et al. (2022). "The Jodrell Bank Glitch Catalogue: 106 new rotational glitches in 70 pulsars". *MNRAS* 510, 4049. [arXiv:2111.06835](https://arxiv.org/abs/2111.06835)
- Totani & Tsuzuki (2023). "Fast radio bursts trigger aftershocks resembling earthquakes, but not solar flares". *MNRAS* 526, 2795. [arXiv:2306.13612](https://arxiv.org/abs/2306.13612)
