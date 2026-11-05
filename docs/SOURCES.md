# Data sources

All literature in this knowledge base comes from public scholarly APIs queried live by `scripts/physlib.py`. Nothing is scraped from publisher sites.

| Source | Used for | Access | Limits the toolkit respects |
|---|---|---|---|
| **arXiv API** (`export.arxiv.org/api/query`) | Latest preprints; ID verification (`id_list`); full-text PDFs (`arxiv.org/pdf/…`) | Free, no key | One request per 3 s, enforced across all processes; back-off on 429/503 |
| **INSPIRE-HEP** (`inspirehep.net/api/literature`) | Citation-ranked papers and reviews for particle, nuclear, gravitational and astro physics and accelerators | Free, no key | ~0.35 s spacing, shared across processes |
| **OpenAlex** (`api.openalex.org/works`) | Citation-ranked papers and reviews in all other fields; DOI metadata for verification; open-access PDF links | Free; **daily budget** (≈100 searches/day per IP without a key, ~10× with a free key) | Stops at the first "budget exhausted" reply and switches to Semantic Scholar |
| **Semantic Scholar** (`api.semanticscholar.org/graph/v1`) | Stand-in for OpenAlex once its budget is spent (fetch and `search`); `search --source semanticscholar` on demand | Free, no key (optional `S2_API_KEY` for a dedicated rate) | 1.1 s spacing shared across processes; back-off on 429 (the no-key pool is shared by everyone) |
| **Crossref** (`api.crossref.org/works/<doi>`) | DOI verification fallback (titles, years) | Free, no key | Polite spacing |
| **doi.org handle API** | Last-resort DOI existence check | Free | — |
| **NIST CODATA** (`physics.nist.gov/cuu/Constants/Table/allascii.txt`) | All 355 CODATA 2022 constants | Free | Pulled once; `constants --update` to refresh |

## What "citations" means
- **INSPIRE** counts citations from INSPIRE-indexed (mostly HEP/astro) literature — authoritative within HEP, undercounted elsewhere.
- **OpenAlex** counts citations across all indexed scholarship — comparable across fields, occasionally noisy for very old papers.
- **Semantic Scholar** also counts across all scholarship; its numbers are usually close to OpenAlex's but not identical, so compare rankings, not raw counts, across sources.
- Counts are snapshots from the fetch date shown in each `papers.md`. Each section's `*Source:*` line names the API that actually filled it.

## Semantic Scholar fallback
When OpenAlex reports its daily budget exhausted, `fetch` fills the Foundational, Rising and Key-reviews sections from Semantic Scholar's bulk search (`"phrase" | "phrase"` over title and abstract, sorted by citation count). Rising lists put title matches first, as the OpenAlex path does, because recent papers with low citation counts that only mention a phrase in passing would otherwise crowd them out. The node's OpenAlex field filter is mapped to Semantic Scholar fields of study, e.g. `31|25` → Physics, Materials Science. Those sections are labelled `Semantic Scholar (fallback: OpenAlex budget exhausted)`. A node is `partial` only if both sources failed; `fetch --partial` retries it. `search` makes the same swap and prints a note. An optional `S2_API_KEY` (free, <https://www.semanticscholar.org/product/api>) is sent as the `x-api-key` header and gives a rate limit not shared with other users. Set it the same way as `OPENALEX_API_KEY`.

## Getting the free OpenAlex API key (recommended)
The shared no-key budget runs out after ~100 searches per day — less than one full refresh. Semantic Scholar covers the gap, but OpenAlex stays the primary source for non-HEP nodes (field-level topic classification, open-access PDF links). With a key:

1. Register at <https://openalex.org/settings/api> with your email (or `POST https://api.openalex.org/api-keys` with `{"email": "…"}`) and click the activation link they email you.
2. Make the key available to the toolkit without committing it anywhere public — either:
   - in your shell profile: `export OPENALEX_API_KEY=…` (PowerShell: `setx OPENALEX_API_KEY …`), or
   - in `.claude/settings.local.json` (personal, not shared): `{"env": {"OPENALEX_API_KEY": "…"}}`.
3. Complete the partial nodes: `python -I scripts/physlib.py fetch --partial --level subfield` then `python -I scripts/physlib.py fetch --partial`.

Optional: `PHYSLIB_MAILTO` adds a contact address to OpenAlex requests (their "polite pool"); it is never set by default.

## Full texts
`physlib.py fulltext <arXiv id or DOI>` saves PDFs to `library/fulltext/` for reading with Claude's Read tool. arXiv PDFs are for personal research use under arXiv's terms; DOIs are downloaded only when OpenAlex lists an open-access PDF. Delete `library/fulltext/` freely — nothing depends on it.

## Known environment quirk
This machine's Python 3.10 ships OpenSSL 1.1.1, whose trust store rejects some new Let's Encrypt chains ("Root YE", used by physics.nist.gov). The toolkit then retries the same URL with `curl`, which validates against the Windows certificate store. TLS verification is never disabled.
