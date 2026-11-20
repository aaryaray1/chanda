# Pre-registration T02 · Do the new forward glitch correlations persist? (registered now, tested later)

**Registered:** 2026-11-20, together with `../analysis/t02_forward_persistence.py` and `../data/t02/snapshot-2026-11-20.json`.
**Motivation:** T01's exploratory finding (`../results/T01-glitch-correlations.md`). In the 2026-11-20 Jodrell Bank catalogue, a glitch's size predicts the wait to the *next* glitch, at single-test three sigma, in:
- J1341−6220: ρ₊ = 0.62, N = 33;
- J1413−6141: ρ₊ = 0.82, N = 14;
- J1801−2304: ρ₊ = 0.71, N = 15.

J1048−5832 is close behind (ρ₊ = 0.76, p = 0.004). These came out of 10 pulsars examined after the fact, so they must be confirmed on data not yet seen.

## Hypothesis
In glitches that are *not* in the 2026-11-20 catalogue snapshot, size and forward waiting time are positively rank-correlated in these four pulsars, taken together.

## Definitions (fixed)
- **Snapshot:** the Jodrell Bank catalogue fetched 2026-11-20 22:15 UTC (SHA-256 `e811419f…aabeb4`). Its epochs for the four pulsars and the control are stored in `snapshot-2026-11-20.json`.
- **New pair:** a consecutive pair (glitch *i*, glitch *i+1*) in the catalogue at test time, where:
  - at least one of the two epochs differs by more than 2 days from every snapshot epoch of that pulsar;
  - glitch *i* has a positive Δν/ν.

  "New" means unseen, not recent. These pulsars are southern, and their glitches after about 2018 are largely uncatalogued. If later published at their historical rates, they would add about 20 glitches: J1341−6220 ≈ 10, J1413−6141 ≈ 7, J1801−2304 ≈ 3, J1048−5832 ≈ 1.
- **Gap rule:** pairs whose wait exceeds 5 × the pulsar's snapshot median wait are dropped as observing gaps. The medians are 253 d (J1341−6220), 333 d (J1413−6141), 822 d (J1048−5832) and 773 d (J1801−2304). The rule was added after T01 showed that a single 6-year gap can dominate a correlation.
- **Statistic:** ranks are computed within each pulsar's new pairs only. This removes any drift of glitch sizes or waits over the decades, such as better detection. The pooled correlation is ρ̄ = Σₖ Σᵢ z(rank sᵢₖ) z(rank Δtᵢₖ) / n, over pulsars with ≥ 3 new pairs. p-values come from 100,000 permutations within each pulsar, seed 20261122.

## When the test is run
- **The test date:** run `t02_forward_persistence.py run` once a year. **The test is the first run at which it reports `due`:** ≥ 10 pooled new pairs, or, on or after 2031-11-20, ≥ 6. Later runs are reported as updates, never as a re-test. That rules out stopping early whenever the result happens to look good.
- **If too little data arrives:** a run on or after 2031-11-20 with fewer than 6 pairs reports *insufficient data*.

## Decision rule
- **persists:** ρ̄ > 0 with one-sided p < 0.05;
- **reversed:** ρ̄ < 0 with one-sided p < 0.05;
- **inconclusive:** otherwise.

**Control,** not part of the test: J0537−6910's new pairs are reported. Its correlation has held across RXTE and NICER data.

## Limitations
- **Data depend on others publishing:** the test needs these glitches to be published and catalogued.
- **Revised values:** catalogue revisions of old sizes are used as they stand at test time.
- **Small samples:** three or four pulsars with a few new pairs each give modest power. A real but weak correlation (ρ ≈ 0.3) could still read as *inconclusive*.
