---
name: paper-search
description: Find, fetch and read real physics papers — most-cited classics, recent arXiv preprints, review articles, or a specific paper's content — via arXiv, INSPIRE-HEP and OpenAlex with verified citations, and file them into the knowledge tree. Use whenever the user asks for papers, sources, references, a reading list, "what's the latest on…", "who first showed…", "find the paper where…", or needs evidence for a research-level claim.
argument-hint: "[topic, question or paper id]"
allowed-tools: Read Grep Glob Bash(python -I scripts/physlib.py *) Bash(grep *)
---
# Paper search

Request: $ARGUMENTS

For broad or multi-part searches delegate to the `paper-scout` agent (several in parallel for distinct subtopics). For a quick lookup, do it directly:

## 1. Local first
- Locate the node in `TREE.md`; read its `papers.md` (foundational, rising, latest) and README landmarks.
- `grep -i "<term>" library/papers.jsonl | head -20` — every paper fetched so far, with abstracts.

## 2. Live search (keep it to a few calls — arXiv allows one request per 3 s)
| Need | Command |
|---|---|
| Classics / most cited (non-HEP) | `python -I scripts/physlib.py search "<phrase>" --source openalex --sort cited -n 8` |
| Classics (HEP, nuclear, GR, astro) | `... --source inspire --sort cited` |
| Reviews | add `--reviews` |
| Recent preprints | `... --source arxiv --sort recent --days 90 --cat <arXiv category>` |
| Recent and relevant | `... --source arxiv --sort relevance --since 2025` |
| One paper's abstract | `python -I scripts/physlib.py paper <arXiv id or DOI>` |
| Full text | `python -I scripts/physlib.py fulltext <id>` → Read the saved PDF (use `pages` for long ones) |

Queries are short phrases; separate alternatives with `;`; avoid commas. If OpenAlex's daily budget is exhausted, `search` switches to Semantic Scholar automatically and prints a note. `--source semanticscholar` asks for it directly.

## 3. Verify and present
- Verify the citation lines with `python -I scripts/physlib.py verify --stdin <<'EOF'` … citation lines … `EOF` (checks existence, exact title and year).
- Present: `Author et al. (Year). "Title". *Venue*. [arXiv:…](…)` + one line on relevance; group as classics / reviews / recent; end with a short synthesis.
- To keep results: re-run the search with `--save <node path>` so they enter `library/papers.jsonl`.
