---
name: refresh-knowledge
description: Maintain the physics knowledge base — report status, complete partial literature fetches, pull the latest papers for a branch or the whole tree, update CODATA constants, re-verify every citation and rebuild the tree index. Use when the user asks to update, refresh, sync or check the knowledge base or papers, when status shows partial/missing nodes, or periodically before a big research session.
argument-hint: "[optional: branch path, or 'all']"
allowed-tools: Read Grep Glob Bash(python -I scripts/physlib.py *)
---
# Refresh the knowledge base

Scope: $ARGUMENTS (empty = health check + complete partial nodes)

## 1. Status
`python -I scripts/physlib.py status` — fields/topics/papers, last refresh dates, partial and missing nodes, last verification result.

## 2. Literature
| Situation | Command |
|---|---|
| Nodes never fetched | `python -I scripts/physlib.py fetch --missing` |
| Partial nodes (API budget ran out earlier) | `python -I scripts/physlib.py fetch --partial` (subfield reviews first: add `--level subfield`) |
| Refresh one branch | `python -I scripts/physlib.py fetch --node <path>` |
| Refresh everything (~30–40 min, uses API budget) | `python -I scripts/physlib.py fetch` |

Run long fetches in the background and tell the user. If OpenAlex reports budget exhaustion, Semantic Scholar fills those sections (labelled as fallback). Nodes stay `partial` only if both fail. Suggest setting `OPENALEX_API_KEY` (free, 10× budget — see `docs/SOURCES.md`) to keep OpenAlex as the primary source.

## 3. Constants
`python -I scripts/physlib.py constants --update` — re-pulls the NIST CODATA table (new adjustments appear every four years; 2022 is current).

## 4. Verify and rebuild
- `python -I scripts/physlib.py verify` — all curated notes (fast; cached).
- `python -I scripts/physlib.py verify --all --recheck` — also every `papers.md` entry, ignoring the cache (slow; do occasionally).
- `python -I scripts/physlib.py tree --check` — structure and links. It also regenerates the 12 branch codices preloaded into the specialists and the cross-branch atlas (`CONNECTIONS.md`, `codex-atlas`), so run it after every fetch. Otherwise the agents keep the old literature index.

## 5. Report
Summarize: papers added, nodes still partial, verification failures (with paths) and suggested fixes.
