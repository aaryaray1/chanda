# Architecture

The physics agent is Claude Code configured by files in this folder. There is no server and no database. The "agent" is a hierarchy: an orchestrator (the main session) that consults 12 branch specialists and a cross-branch connections analyst, plus pipeline workers and skills. They all operate on a markdown knowledge tree, with one Python toolkit for everything that touches the network or needs checking.

```
  user question
       │
       ▼
  ┌────────────────────────────────────────────────────────────────┐
  │ physics-orchestrator (main session: CLAUDE.md + physics skill) │
  │ classify → decide skillset → brief → collect → integrate →     │
  │ verify → answer → grow                                         │
  └──────┬───────────────────────┬────────────────────────┬────────┘
         │ briefs (parallel)     │ reports to integrate   │ checks
         ▼                       ▼                        ▼
  12 field specialists     connections-analyst      paper-scout · derivation-checker
  each preloads its        preloads codex-atlas,    referee · knowledge-curator
  codex-<NN-field>         loads any codex on       (and the skills: explain-concept,
  (whole branch)           demand; project memory    solve-problem, derive-check, …)
         │ expert reports        │ synthesis + labelled connections
         └──────────► orchestrator ◄────────┘
                           │
   ┌───────────────────────┴──────────────────────────────────────────────────────────┐
   │ knowledge/  NN-field/ subfield/ topic/ {README.md curated · papers.md generated} │
   │ connections/ {concepts.md · themes/*.md}  curated                                │
   │ generated: TREE.md · CONNECTIONS.md · library/{papers.jsonl, index.json,         │
   │            connections.json, codata.json, verify-cache} · .claude/skills/codex-* │
   └──────────────────────────────────────────────────────────────────────────────────┘
                      ▲                         ▲
                      │ fetch / verify / tree    │ search / paper / fulltext / constants / connections
              ┌───────┴─────────────────────────┴───────┐
              │ scripts/physlib.py  (stdlib-only toolkit)│
              └───────┬───────────┬───────────┬──────────┘
                      ▼           ▼           ▼            ▼            ▼
                    arXiv    INSPIRE-HEP   OpenAlex    Crossref/doi   NIST CODATA
                                              │ budget spent
                                              ▼
                                       Semantic Scholar
```

## Layers

| Layer | Files | Role |
|---|---|---|
| Brain | `CLAUDE.md` | Identity, folder map, chain of command, routing table, pipeline, evidence rules, toolkit cheat-sheet. Loaded every session. |
| Orchestrator | `.claude/agents/physics-orchestrator.md` | Dispatch rules (which expertise a question needs), brief templates, report reconciliation, synthesis. It is the main session's system prompt with `claude --agent physics-orchestrator` (or `"agent"` in settings); a plain session reads it via the pointer in `CLAUDE.md`. Its `Agent(...)` allowlist names the 17 agents it may call. |
| Pipelines | `.claude/skills/*/SKILL.md` (8) | Reusable procedures; `physics` is the entry point and dispatches to the others. |
| Specialists | `.claude/agents/<field>.md` (12) | One per top-level branch. Each preloads its **branch codex** (`skills: codex-<NN-field>`): every curated note of the branch, its literature index and its bridges, about 30–50k tokens. It also knows its conventions, pitfalls and trusted sources, and returns a fixed 8-part *expert report* to the orchestrator. Runs in its own context, in parallel for cross-field questions. |
| Connections analyst | `.claude/agents/connections-analyst.md` | Sees every branch at once: it preloads `codex-atlas` (roster, field map with key equations, link matrix, structural gaps, concept index, latent bridges, themes) and loads any branch codex on demand. It integrates specialist reports, tests and classifies connections (identity, mechanism, analogy, duality, method transfer, shared object, historical) and keeps `memory: project` of settled connections. |
| Codices | `.claude/skills/codex-*/SKILL.md` (13, generated) | Knowledge packs preloaded into agents. `tree` regenerates them from the notes, so editing a note updates the next consultation. |
| Connections | `connections/` + `CONNECTIONS.md` + `library/connections.json` | Curated concept lexicon and theme notes, plus the generated cross-branch graph. |
| Pipeline workers | `.claude/agents/{paper-scout,derivation-checker,referee,knowledge-curator}.md` | Literature, math verification, adversarial review, tree maintenance. |
| Knowledge | `knowledge/` + `TREE.md` | Three-level branched tree: 12 fields → 69 subfields → 316 topics. Each node: curated `README.md` (frontmatter = config) and generated `papers.md`. |
| Library | `library/` | `papers.jsonl` (every fetched paper, deduplicated by arXiv id/DOI), `index.json` (node metadata), `codata.json`, `verify-cache.json`, `verification-report.md`, fetch logs, `fulltext/` PDFs. |
| Toolkit | `scripts/physlib.py` | Search, fetch, verify, tree (+ codices + atlas), connections, constants, full text, new nodes, status, hook handler. |
| Guard rails | `docs/claude-settings.example.json` | Optional hooks: SessionStart status line; PostToolUse checks on every edited knowledge note. |

## Why it is built this way
- **Markdown tree, frontmatter as config.** The tree is browsable by humans and by the agent with plain Read/Grep. Each node's `query`, `arxiv` categories and `source` (inherited down the tree) drive literature fetching, so adding a branch is just adding a folder.
- **Generated vs. curated split.** `papers.md` can be regenerated any time without touching curated notes; curated notes are never overwritten by scripts.
- **Verification as a first-class step.** Language models can hallucinate references. Every arXiv id and DOI in curated notes is checked against arXiv/OpenAlex/Crossref, and the quoted title and year must match the record. The cache makes re-checks cheap.
- **Stdlib-only, isolated Python.** `physlib.py` needs no installs and runs with `python -I` (isolated mode), so downloaded data can't influence imports.
- **Polite networking.** One arXiv request per 3 s and INSPIRE spacing are enforced across processes via a lock-file throttle in the system temp dir; OpenAlex budget exhaustion is detected and degrades gracefully to `partial` nodes.

## The hierarchy
1. **Decide the skillset.** The orchestrator classifies the question (fields, level, task, stakes) and picks the smallest team:
   - itself, for textbook material;
   - one specialist, for deep single-branch work;
   - several specialists in parallel, then the analyst, for cross-branch work;
   - the analyst first, for "how is X related to Y".
2. **Brief.** Each agent starts cold, so the orchestrator sends a structured brief: QUESTION · LEVEL · YOUR PART · CONTEXT · CONSTRAINTS · RETURN. Each specialist gets only its own part.
3. **Report.** Specialists answer from their preloaded codex and return an expert report: answer, reasoning, numbers, verified sources, confidence, *bridges*, *hand-offs*, *tree gaps*. Specialists never call each other. The orchestrator relays hand-offs in a second round.
4. **Integrate.** The connections analyst receives the reports and returns a synthesis. It covers shared structure, labelled connections with symbol maps and failure points, tensions between reports, and proposed cross-links.
5. **Answer and grow.** The orchestrator verifies (derivation-checker, `verify --stdin`, referee when warranted), writes one answer, and offers to file tree gaps and new bridges through knowledge-curator.

## Connections layer
`tree` builds the cross-branch graph from three sources:
- **Explicit cross-links** in the curated notes, excluding parent/child structure.
- **The concept lexicon** (`connections/concepts.md`, about 80 concepts), matched against every note.
- **Shared literature** in `papers.jsonl`.

From these it derives:
- a field-by-field **link matrix**;
- **structural gaps** (field pairs with at most one link);
- the **concept index**;
- **latent bridges**: unlinked note pairs scored by IDF-weighted cosine similarity of their rare shared concepts, a lead list for the analyst rather than a finding;
- the list of curated **themes**.

Outputs: `CONNECTIONS.md` (human), `library/connections.json` (data), `codex-atlas` (analyst preload). Query with `physlib.py connections <node|field|title> [other]`.

## Connection discovery (multi-session)
`connections/pipeline/PLAN.md` holds the plan. The work runs in stages:
1. **Discovery:** one fresh headless session per branch-pair set.
2. **Review:** the branch specialist (`--agent`, codex preloaded) checks a packet of connections touching its branch.
3. **Finalize:** local, no model calls. It applies verdicts, flags contested links, verifies citations, writes `connections/registry.jsonl`, and rebuilds the codices, atlas and map.

A runner does one budgeted run. There are two runners:
- `scripts/connections_runner.py` on the Linux server, fired by a systemd user timer; it posts findings and alerts to Discord;
- `scripts/run_connections.ps1` on Windows, fired by a scheduled task.

Both runners provide:
- a crash-safe lock;
- recovery of orphaned and interrupted units;
- a cooldown until the parsed usage-limit reset;
- per-unit budget caps, and per-run and per-day caps.

The `stage_gate` setting in `config.json` decides which machine runs a stage, and from when. Review is gated to the Linux server. See the safeguards table in `connections/pipeline/PLAN.md` and the server guide in `docs/SERVER.md`. The design keeps each unit's context small, so long jobs survive 5-hour and weekly usage limits.

## Pipelines

### 1. Answer (skill `physics`, run by the orchestrator)
classify (field, level, task) → route via `TREE.md` → read node READMEs → dispatch (direct / specialist / parallel specialists → connections analyst) → ground (papers.md, `papers.jsonl`, live search, full text) → draft → verify (derive-check / derivation-checker, constants, `verify` on citations, referee for high-stakes) → answer with confidence labels → offer tree growth.

### 2. Literature (skills `paper-search`, `literature-review`; agent `paper-scout`)
local first (`papers.md`, `papers.jsonl`) → targeted live searches (cited / reviews / recent) → read abstracts and full texts → rank → verify → present or synthesize → file into `knowledge/<node>/reviews/` → link from the node → `tree --check`.

### 3. Fetch (toolkit, per node)
| Node level | Sections written to `papers.md` | Sources |
|---|---|---|
| Subfield | Key reviews — most-cited review articles | OpenAlex `type:review` or INSPIRE `tc r` |
| Topic | Foundational (6, most cited ever) · Rising (4, most cited in last ~2 years) · Latest (5, arXiv last 365 days by relevance) | OpenAlex or INSPIRE for the first two (per node `source`), arXiv for the third |
For `source: openalex` nodes, Semantic Scholar fills any section OpenAlex can't (budget spent). The section's `*Source:*` line says so. Results are deduplicated within a node and merged into `library/papers.jsonl` across nodes.

### 4. Verify
`collect_refs` scans markdown for `arXiv:` and `doi:` links, pairs each with the quoted title and year written just before it, batch-checks arXiv (`id_list`) and DOIs (OpenAlex → Crossref → doi.org handle API), then flags `NOT_FOUND`, `TITLE_MISMATCH` or `YEAR_MISMATCH` (DOI ±1 yr; arXiv −1…+5 yr to allow publication lag). A cited title matches its record if it is identical after normalization, is a ≥4-word prefix of it (long titles are legitimately truncated), or ≥85% of its content words appear in the record while covering ≥30% of the record's words — so a real ID paired with an invented or different title fails. Journal and arXiv titles sometimes differ for the same paper; cite the identifier whose title you quote. Full scans write `library/verification-report.md`; `verify <file>` and `verify --stdin` only print.

### 5. Grow
`grow-tree` / `knowledge-curator`: check for duplicates → `new-node` (breadcrumb + template) → write the note → update parent → `fetch --node` → `verify` → `tree --check`.

### 6. Maintain (skill `refresh-knowledge`)
`status` → `fetch --missing` / `--partial` / `--node` → `constants --update` → `verify [--all --recheck]` → `tree --check`.

## Failure modes and how they're handled
| Failure | Handling |
|---|---|
| OpenAlex daily budget exhausted | `BudgetExhausted` raised once; remaining OpenAlex calls skipped; Semantic Scholar fills those sections (labelled as fallback). Only if it also fails is the node marked `partial: true`; `fetch --partial` completes it later. |
| arXiv/INSPIRE/Semantic Scholar 429 or 5xx | Back-off that grows with each attempt (20 s × attempt for 429), five attempts; the cross-process throttle prevents self-inflicted 429s. |
| Python TLS store rejects a valid chain (seen with NIST's Let's Encrypt "Root YE") | Fallback to `curl`, which verifies with the Windows trust store. Verification is never disabled. |
| Hallucinated or mistyped citation | `verify` fails it; the PostToolUse hook lists unverified IDs after every edit. |
| Broken cross-links | `tree --check` and the hook report them (math is stripped before link parsing). |
