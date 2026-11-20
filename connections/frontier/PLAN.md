# Frontier plan: from connections to checkable results

Stage 4, after the connection map (stages 1–3, `../pipeline/PLAN.md`). The map holds 2,884 checked connections. This stage uses it to look for links nobody has drawn yet and pushes the best of them to a result that can be checked.

## What counts as a result
A literature-and-compute agent cannot run experiments. It can produce three kinds of evidence that anyone can check:

| Tier | Evidence | How it is checked |
|---|---|---|
| **P · proof** | A precise statement (an identity, a variable map, a bound, a derived consequence), proved symbolically or numerically | sympy/numpy through `derivation-checker`: dimensions, limits, an independent re-derivation |
| **T · test** | A quantitative prediction tested on public data | Pre-registered: the prediction, dataset, statistic and threshold are committed to git **before** the data are read. A refutation counts as a result too |
| **N · novelty** | A documented prior-art search that finds the link or prediction unpublished | Logged queries on arXiv, INSPIRE, OpenAlex and Semantic Scholar, plus the closest papers read |

A **frontier result** is P or T, plus N, and it survives the `referee`. Expect most candidates to turn out to be known, already implied by known work, or wrong. A few novel results that check out is a good outcome. A claim of discovery needs outside experts and usually an experiment; this stage produces the precise, checked claim to take to them.

## Four tracks (learned from the first pass, 2026-11-20)
Link prediction over a map of established physics mostly rediscovers established physics: pairs that are well known but that the map had not linked. So the work runs on four tracks, from most to least reliable:

| Track | What it does | First item |
|---|---|---|
| **Map** (F0) | Adds links the graph predicts and the literature already has. Re-mines the thin branch pairs and adds missing nodes. | Analogue gravity has no node at all. It is the main relativity × condensed-matter bridge: Steinhauer's analogue Hawking radiation (2016; the entanglement claim was disputed) and the gravitational anomaly measured in the Weyl semimetal NbP (Gooth et al. 2017). |
| **Audit** (P) | Recomputes the numeric and formula claims in the 2,884 connections. Reviewers judge prose; arithmetic slips past them. | `results/C2021-unruh-hadronization.md`: the registry formula is off by √(2π), which turns 160 MeV into 64–71 MeV. |
| **Test** (T) | Pre-registered tests, on public data, of cross-branch claims the specialists left at *current research* or *proposed*. 73 such quantitative claims exist. | `cards/T01-pulsar-glitch-avalanches.md`: vortex avalanches versus stress release, on 737 glitches in 226 pulsars. |
| **Frontier** (P/T + N) | Link prediction with an arXiv co-occurrence prefilter, then cards, prior art and a check | Branch 00 (methods) is excluded from the prefilter: abstracts rarely name the method they use, so its pairs look falsely uncharted. |

## Stages
| Step | Unit of work | Who | Cost |
|---|---|---|---|
| **F0 · fill the map** | Pairs the graph predicts strongly that the literature already joins (high arXiv overlap) are missing connections, not discoveries. Confirm them in batches and add them to the registry. Re-run discovery on the 10 thinnest branch pairs, and add missing tree nodes (first: analogue gravity). | specialists on Sonnet/Haiku; `grow-tree` | low |
| **F1 · mine** | `python -I scripts/frontier.py mine --exclude 00` ranks unlinked cross-branch topic pairs by link prediction over the registry. The score is Adamic–Adar weighted by connection kind and strength, and contested links are excluded. `frontier.py novelty` adds arXiv co-occurrence counts of the two nodes' query phrases. First run (118 pairs): the counts only flag the well-charted pairs (> 50 joint papers: 18, sent to the map track). Zero counts are common even for famous links (light scattering ↔ gravitational waves via CMB B-modes has 0), so novelty is judged per claim at F2/F3, never from these counts. | local | free (arXiv, 3 s/query) |
| **F2 · hypothesis card** | For each high-score, low-overlap pair: the specific claim, what it predicts (a quantity, scaling, sign or bound), the check type (P or T), the dataset, and what would refute it. Unphysical candidates are killed here. | the two branch specialists (Sonnet) | ~$0.2/card |
| **F3 · prior art** | Targeted searches; the closest 5–10 papers read. Verdict: known · partly known · not found. | `paper-scout` (Haiku) | low |
| **F4 · pre-register** | The card's prediction, data source, statistic and threshold are committed to git. The commit hash timestamps the prediction. | local | free |
| **F5 · prove or test** | A sympy derivation, a numpy simulation, or an open-data test, run as pre-registered | Opus, interactive, for the few cards that reach here | high |
| **F6 · referee and file** | `referee` attacks the result. Survivors are written up as a review note in the tree with their tier (P/T/N) and status (proved · confirmed · refuted · open), then posted to Discord. | Opus, then `knowledge-curator` | medium |

## Selection rule for F5
Reach for a result only where all of these hold:
- the graph support is real: at least 3 independent bridge topics;
- the specific claim is uncharted: the F3 prior-art search, run on the claim itself and not on the topic names, finds no paper making it;
- both topics are active: at least 300 papers each;
- the check can run here: sympy, numpy, or a public dataset with an API.

## Public data reachable without keys
- **Gravitational waves:** GWOSC (LIGO/Virgo/KAGRA strain data and event catalogues).
- **Astronomy:** NASA Exoplanet Archive (TAP), ATNF Pulsar Catalogue, Gaia archive (TAP), SDSS SkyServer, Fermi-LAT catalogues.
- **Particles and nuclei:** PDG (pdg.lbl.gov), HEPData, IceCube public releases.
- **Atomic physics and constants:** NIST Atomic Spectra Database, plus CODATA, which is already local.
- **Earth and Sun:** USGS earthquake catalogue (ComCat API), NOAA GOES X-ray flare lists.

## Budget on Claude Pro
F0–F1 and F4 cost nothing. A week of F2–F3 is about 20 cards and 8 prior-art checks on Sonnet/Haiku. F5–F6 cover 2–3 candidates a week, interactively on Opus. Automating F2–F3 means adding them as units to `connections_pipeline.py`, which keeps the existing runner, timer, caps and Discord digests. That needs your OK, because it spends quota every day.

For F5 statistics (KS, likelihood ratios, rank correlations), install scipy: `sudo apt install python3-scipy`.

## Files
- `candidates.jsonl`: mined pairs with score, bridges and arXiv counts.
- `arxiv-counts.json`: the query cache.
- `cards/<id>.md`: hypothesis cards, from F2 on.
- `results/<id>.md`: proofs and tests with their pre-registration hash, from F5 on.
