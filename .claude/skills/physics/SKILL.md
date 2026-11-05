---
name: physics
description: The physics agent's main pipeline — routes a physics question through the branched knowledge tree (12 fields → subfields → topics), pulls verified literature, checks the math, and answers at the asker's level with real citations. Use this for ANY physics question or task — concepts, problems, derivations, current research, fact-checks ("is it true that…"), comparisons across fields — even when the word "physics" never appears (black holes, quantum computers, lasers, MRI, climate, fusion, the LHC, superconductors, dark matter…).
argument-hint: "[question]"
allowed-tools: Read Grep Glob Bash(python -I scripts/physlib.py *)
---
# Physics pipeline

Question: $ARGUMENTS

You run this as the **orchestrator**: specialists and the connections analyst report to you, and you write the answer. The dispatch rules and brief templates are in `.claude/agents/physics-orchestrator.md`. Read that file once per session before your first consultation, unless you are already running as that agent.

Work through these stages. Skip a stage only when it clearly adds nothing (a one-line factual answer does not need a referee), and say what you skipped if the answer is research-level.

## 1. Classify
- **Field(s)** — match against `TREE.md` (read it; it is the map). Note every field the question touches.
- **Level** — school, intro undergrad, advanced undergrad, graduate, research. Infer from wording; when unclear, aim for advanced undergrad and offer to go up or down.
- **Task type** → which tool does the heavy lifting:

| Task | Primary route |
|---|---|
| Explain a concept | `explain-concept` skill |
| Solve a problem / compute a number | `solve-problem` skill |
| Check a derivation, formula or claim | `derive-check` skill or `derivation-checker` agent |
| Find papers / what's new / reading list | `paper-search` skill or `paper-scout` agent |
| Survey a topic in depth | `literature-review` skill |
| Deep single-field question | that field's specialist agent (table in `CLAUDE.md`), briefed per the orchestrator file |
| Cross-field question | the relevant specialists **in parallel**, then `connections-analyst` with their reports, then synthesize |
| "How is X related to Y", analogies, unification | `connections-analyst` first, then the specialists on each side to check the physics |

## 2. Route into the tree
- Open the node(s): `knowledge/<field>/<subfield>/<topic>/README.md`, plus the field `README.md` for conventions (units, metric signature).
- If no node fits, answer anyway and note the gap for stage 7.

## 3. Ground
- Consultations: if stage 1 picked agents, brief them now, in parallel where they are independent. Ground the answer in their expert reports, and integrate several reports through `connections-analyst`, following §2–4 of the orchestrator file.
- Textbook-level material: your own knowledge is fine; cite a canonical text or a landmark from the README if helpful.
- Research-level, recent, quantitative or contested claims: take sources from the node's `papers.md`, grep `library/papers.jsonl`, or search (`python -I scripts/physlib.py search "…"`). Read abstracts with `physlib.py paper <id>`; read full text (`physlib.py fulltext <id>` then Read the PDF) when the claim depends on details.
- Constants: `python -I scripts/physlib.py constants "<name>"`.

## 4. Draft
Lead with the direct answer. Then the reasoning: physical picture → key equation(s) in LaTeX → limiting cases or numbers → caveats. Keep the asker's level throughout.

## 5. Verify
- Math and numbers: dimensions, limits, sympy re-derivation (`derive-check`), or delegate to `derivation-checker` for anything non-trivial. Approximation coefficients and scaling exponents must be derived (e.g. `sympy.series`), never recalled, and must agree with any numbers in the answer.
- Citations: pipe every citation line of the answer through `python -I scripts/physlib.py verify --stdin <<'EOF'` … citation lines … `EOF`; fix or drop anything that is NOT_FOUND or mismatched.
- High-stakes, long or controversial answers: send the draft to the `referee` agent and address critical/major issues.

## 6. Answer — format
```
**Answer.** <one to three sentences>

<explanation at the asker's level, with equations>

**Key equation(s).** $$…$$
**Confidence.** established | current research | speculative — with one line on why
**Sources.** Author et al. (Year). "Title". *Venue*. [arXiv:…](…) — one line each, only verified
**Go deeper.** links to the relevant knowledge/ nodes
```
Drop sections that would be empty; never pad.

## 7. Grow the tree
If the question exposed a missing topic or an outdated note, say so and offer to fix it with `grow-tree` / `knowledge-curator`. Small additions (a new topic note, a verified landmark) can be made directly; reorganizations need the user's go-ahead.
