# Physics agent

A Claude Code agent that knows physics end to end: a branched knowledge base covering **12 fields → 69 subfields → 316 topics**, ~3 000 real papers pulled live from arXiv, INSPIRE-HEP and OpenAlex (with Semantic Scholar as a fallback), all 355 CODATA 2022 constants and a hierarchy of agents: an **orchestrator** that splits each question between **12 field specialists** (each preloaded with its whole branch), a **connections analyst** that sees all branches at once, and 4 pipeline agents. It has 9 skills, and every curated citation is machine-verified against the original records.

## Quick start
```bash
cd chanda
claude --agent physics-orchestrator     # or plain `claude`: CLAUDE.md makes the main session the orchestrator
```
Then just ask. Examples:
- `Why does the muon g−2 anomaly matter, and is it still an anomaly?`
- `/explain-concept Berry phase undergrad`
- `/solve-problem A 2 kg mass on a spring with k = 50 N/m is pulled 10 cm and released with 0.3 N·s/m damping. How long until the amplitude halves?`
- `/derive-check E = mc^2/sqrt(1 - v^2/c^2) reduces to mc^2 + mv^2/2 at low speed`
- `/paper-search latest results on neutrinoless double-beta decay`
- `/literature-review moiré superconductivity`
- `/grow-tree add a topic on time-of-flight mass spectrometry under 11-interdisciplinary-physics/chemical-physics`
- `/find-connections pairing in superconductors and in atomic nuclei`
- `/find-connections discover 08`
- `/refresh-knowledge`

You don't need to name skills or agents. The orchestrator decides which expertise a question needs. It answers textbook questions itself and briefs one specialist for deep single-branch work. For cross-branch questions it consults several specialists in parallel and hands their reports to the connections analyst to integrate. Each answer ends with a line saying who was consulted.

## What's inside
| Path | Contents |
|---|---|
| `TREE.md` | The full map of the tree with one-line summaries and paper counts |
| `knowledge/` | `00-foundations` · `01-classical-mechanics` · `02-electromagnetism-and-optics` · `03-thermodynamics-and-statistical-mechanics` · `04-quantum-physics` · `05-relativity-and-gravitation` · `06-particle-physics` · `07-nuclear-physics` · `08-condensed-matter` · `09-astrophysics-and-cosmology` · `10-plasma-physics` · `11-interdisciplinary-physics` |
| each node | `README.md` — curated: scope, core ideas, key equations, verified landmark papers, open questions, cross-links · `papers.md` — generated: foundational (most cited), rising (last ~2 years), latest (arXiv, last 12 months) |
| `library/` | `papers.jsonl` (all papers, searchable), `codata.json`, `index.json`, verification report, fetch logs |
| `.claude/agents/` | `physics-orchestrator` (top of the hierarchy) · 12 specialists (`particle-physicist`, `quantum-physicist`, `relativist`, …) · `connections-analyst` · `paper-scout`, `derivation-checker`, `referee`, `knowledge-curator` |
| `.claude/skills/` | `physics`, `explain-concept`, `solve-problem`, `derive-check`, `paper-search`, `literature-review`, `find-connections`, `grow-tree`, `refresh-knowledge`, plus 13 generated codices (`codex-<NN-field>` per branch and `codex-atlas`) preloaded into the agents |
| `CONNECTIONS.md` · `connections/` | Generated cross-branch atlas (link matrix, structural gaps, concept index, latent bridges) · curated concept lexicon and theme notes on major bridges |
| `scripts/physlib.py` | The toolkit (Python stdlib only) |
| `docs/` | `ARCHITECTURE.md` (design + pipelines), `CONVENTIONS.md` (note and citation format), `SOURCES.md` (APIs, budgets, API key) |

## How it stays truthful
- Every arXiv ID and DOI in the curated notes is checked against arXiv / OpenAlex / Crossref, **including the quoted title and year** (`python -I scripts/physlib.py verify`). Current status: see `library/verification-report.md`.
- Every entry in a `papers.md` came from a live API record, so it exists; its *relevance* is algorithmic.
- The agent is instructed never to cite anything it hasn't verified, to label claims as established / current research / speculative, and to run math through dimensional, limit and sympy checks.

## Toolkit
```bash
python -I scripts/physlib.py status
python -I scripts/physlib.py search "quantum error correction" --source arxiv --sort recent -n 5
python -I scripts/physlib.py paper 1602.03837
python -I scripts/physlib.py fulltext 1602.03837
python -I scripts/physlib.py constants "electron mass"
python -I scripts/physlib.py verify
python -I scripts/physlib.py tree --check
python -I scripts/physlib.py fetch --partial            # finish nodes whose lists are still pending
python -I scripts/physlib.py new-node <path> --title … --summary … --query …
```

## One-time setup you may want
1. **Free OpenAlex API key** — the shared no-key budget is ~100 searches/day. When it runs out, refreshes fall back to Semantic Scholar (labelled in each `papers.md`); with a key, OpenAlex stays the primary source. See `docs/SOURCES.md`.
2. **Hooks, permissions and the orchestrator as default.** Copy `docs/claude-settings.example.json` to `.claude/settings.json`. You get a status line at session start, automatic checks (and codex/atlas rebuilds) whenever a note is edited, no permission prompts for the toolkit and paper APIs, and `"agent": "physics-orchestrator"`, so a plain `claude` starts as the orchestrator.
3. **sympy** is installed for symbolic checks (`pip install --user sympy` if you move machines).

## Limits
- The notes are curated summaries, not textbooks; the agent's depth comes from the model plus the cited literature.
- Literature lists are snapshots (dated in each `papers.md`); run `/refresh-knowledge` to update.
- Full-text reading is limited to open-access papers (all of arXiv, plus OA journal articles).
