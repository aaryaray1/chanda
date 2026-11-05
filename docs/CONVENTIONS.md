# Conventions

Rules for everything in `knowledge/`. The toolkit, the hooks and the `knowledge-curator` agent all assume them.

## Tree layout
```
knowledge/
  NN-field-slug/                 depth 1 — field (12 of them, 00–11)
    README.md                    field overview, branch map, conventions, history, textbooks, frontiers
    subfield-slug/               depth 2 — subfield
      README.md                  overview, topic list, spine, key equations, landmark papers, open problems
      papers.md                  generated: key reviews
      topic-slug/                depth 3 — topic (deeper "branch" levels allowed when a topic grows)
        README.md                compact note
        papers.md                generated: foundational · rising · latest
        reviews/<slug>.md        literature reviews (optional)
```
- Slugs: lowercase, hyphen-separated, descriptive (`neutrino-oscillations`, not `nu-osc`). Fields keep their two-digit prefix.
- Directories named `_templates`, `reviews`, `notes`, `assets` are not nodes.

## Frontmatter (every README)
```yaml
---
title: Neutrino oscillations                 # required
summary: One sentence, shown in TREE.md      # required
query: neutrino oscillation; neutrino mixing # required for topics; phrases separated by ';', no commas
arxiv: hep-ph hep-ex                         # optional, space-separated categories; inherited by children
source: inspire                              # optional: inspire | openalex; inherited (default openalex)
agent: particle-physicist                    # field level; inherited
openalex_filter: primary_topic.field.id:31|25  # optional OpenAlex filter override; inherited
---
```
- `query` feeds all three APIs: arXiv `ti:/abs:` phrase search, OpenAlex `title_and_abstract.search`, INSPIRE `t …`. Keep phrases 1–4 words and specific.
- Use `source: inspire` for particle, nuclear, gravitation and most astrophysics (citation counts are meaningful there); `openalex` elsewhere.
- OpenAlex field ids: 31 Physics & Astronomy, 25 Materials, 16 Chemistry, 17 Computer Science, 19 Earth & Planetary, 13 Biochemistry/Genetics/Mol. Bio, 27 Medicine, 22 Engineering, 21 Energy, 26 Mathematics, 12 Arts & Humanities, 33 Social Sciences.

## Topic note layout
```markdown
# <Title>
> [Field](../../README.md) › [Subfield](../README.md) · Literature: [papers.md](papers.md)

**Scope.** What the topic covers (concepts, methods, experiments, named results).

**Core ideas.**
- Three or so bullets a student should walk away with.

**Key equations.**
$$…$$

**Landmark.** Author (Year). "Exact title". *Venue* vol, page. [doi:…](https://doi.org/…)   ← or "see subfield landmarks"

**Open questions.** …

**See also.** [Related node](../../../NN-field/subfield/topic/README.md) · …
```
Subfield and field READMEs use `##` sections (Overview, Topics, Conceptual spine, Key equations, Landmark papers, Open problems, Connections; fields add Branch map, Conventions, Historical spine, Canonical textbooks, Live frontiers, How the specialist works here).

## Citations
- Format: `Author et al. (Year). "Exact title". *Venue* vol, page. [arXiv:ID](https://arxiv.org/abs/ID)` or `[doi:DOI](https://doi.org/DOI)`. Example: ATLAS Collaboration (2012). "Observation of a new particle in the search for the Standard Model Higgs boson with the ATLAS detector at the LHC". *Phys. Lett. B* 716, 1. [arXiv:1207.7214](https://arxiv.org/abs/1207.7214)
- The verifier pairs each ID with the **last quoted title and parenthesized year written before it on the same line**, so keep that order.
- Year rules: DOI records must match within ±1 year; arXiv records may be up to 5 years older than the cited (journal) year. For special cases write the year so it isn't parsed — `(1997; published 2003)`, `(1916; English translation 1999)` — and explain in the text.
- Prefer the DOI for papers posted to arXiv long after publication (the arXiv date would be misleading).
- Journal and arXiv titles sometimes differ for the same paper (common for *Nature*/*Science*): quote the title of the identifier you link, or the verifier will flag `TITLE_MISMATCH`.
- DOIs containing `<`, `>` or parentheses are fine in the link text; percent-encode `<`/`>` in the URL.
- Run `python -I scripts/physlib.py verify <file>` after adding references; zero failures before finishing.

## Units, notation, math
- SI unless the field README says otherwise; always name the system when using natural ($\hbar=c=1$), geometrized ($G=c=1$), atomic or Gaussian units.
- Metric signature: $(-,+,+,+)$ in relativity notes, $(+,-,-,-)$ in particle-physics notes — each field README states its choice.
- LaTeX: inline `$…$`, display `$$…$$`. Avoid `[x](y)` patterns inside math (markdown may read them as links); the link checker strips math, renderers may not.
- Constants: CODATA 2022 (`codata-2022.md`, `physlib.py constants`).

## Cross-links
- Relative paths only, always to a `README.md` (or a sibling file such as `papers.md`, `codata-2022.md`).
- From a topic: sibling `../other-topic/README.md`; parent `../README.md`; field `../../README.md`; another field `../../../NN-field/subfield/topic/README.md`.
- `python -I scripts/physlib.py tree --check` must report 0 structural problems.

## Connections (`connections/`)
The cross-branch layer sits beside the tree, not inside it. Adding to it never restructures `knowledge/`.
- **`connections/concepts.md`** is the curated lexicon: a three-column table, `| Concept | Terms | Unifying idea |`.
  - Terms are lowercase and `;`-separated, and match at the start of a word (`turbulen` catches *turbulence*).
  - Math is stripped before matching, and en/em dashes count as hyphens.
  - Prefer multi-word terms. One generic word (`energy`, `field`) floods the index.
- **`connections/themes/<slug>.md`** holds a curated theme note for one major bridge.
  - Frontmatter: `title`, `summary`, `fields` (space-separated two-digit codes, e.g. `05 03 04`) and `kind` (identity | mechanism | analogy | duality | method transfer | shared object | historical).
  - Sections: **The bridge** (with a confidence label), **How each branch sees it** (one bullet per field, linking its nodes as `../../knowledge/…/README.md`), **Shared structure** (equations plus a symbol map), **Where it breaks**, **Landmarks** (verified citations), **Open questions**.
- A connection that lives between two specific notes belongs in those notes' *Connections* / *See also* lines. A theme is for a bridge that spans three or more notes or several fields.
- After editing either kind of file, run `verify` on it and `tree --check`. That rebuilds `CONNECTIONS.md`, `library/connections.json` and the `codex-atlas` skill.

## Generated files (never hand-edit)
`TREE.md`, `CONNECTIONS.md`, every `papers.md`, `library/index.json`, `library/connections.json`, `library/papers.jsonl`, `library/verify-cache.json`, `library/verification-report.md`, `library/fetch-log.json`, `knowledge/00-foundations/units-and-constants/codata-2022.md`.

The connection registry `connections/registry.jsonl` is written by `scripts/connections_pipeline.py`, from analyst discovery plus specialist review. `connections/map.html` and `map.svg` are drawn by `physlib.py plot` and `tree`. Edit neither by hand; the pipeline state lives in `connections/pipeline/`.

Also generated: `.claude/skills/codex-*/SKILL.md`, the 12 branch codices plus `codex-atlas`. `tree` writes them from the notes, and each is preloaded into an agent. Edit the notes, never the codices.
