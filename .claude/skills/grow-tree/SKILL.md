---
name: grow-tree
description: Grow or reshape the branched physics knowledge tree — add a new topic or subfield, split an overgrown node, add verified landmark references, fix cross-links — then fetch its literature and re-verify. Use when a question exposed a missing topic, when the user says "add a branch/topic for…", "this field is missing", "split", "reorganize the tree", or when a review needs a home.
argument-hint: "[what to add or change]"
allowed-tools: Read Grep Glob Write Edit Bash(python -I scripts/physlib.py *)
---
# Grow the knowledge tree

Change: $ARGUMENTS

Small, additive changes (new topic, new landmark, new cross-link) you may make directly. Moves, renames, merges and deletions change paths other notes link to — describe the plan and get the user's go-ahead first. For bulk work, delegate to `knowledge-curator`.

## Add a node
1. **Check it doesn't exist:** grep `TREE.md` and `library/index.json` for the concept and synonyms.
2. **Pick the parent** (deepest node that truly contains it). Topics live at depth 3; deeper branches are allowed when a topic grows large.
3. **Scaffold:**
   `python -I scripts/physlib.py new-node <field>/<subfield>/<slug> --title "…" --summary "…" --query "phrase; alternative"`
   Slugs are lowercase-hyphenated. Override `--source inspire` for HEP/nuclear/gravity/astro topics; `--arxiv "<cats>"` if the parent's categories don't fit.
4. **Write the note** following `docs/CONVENTIONS.md`: Scope, Core ideas, Key equations, Landmarks (verified), Open questions, See also (link existing nodes with correct relative paths).
5. **Update the parent README** topic list.
6. **Fetch literature:** `python -I scripts/physlib.py fetch --node <path>`.
7. **Verify:** `python -I scripts/physlib.py verify knowledge/<path>/README.md` and `python -I scripts/physlib.py tree --check`.

## Split a node
Create children with `new-node`, move content into them, leave the parent as an overview with links, update every inbound link (`grep -rn "<old path>" knowledge/`), re-fetch, verify, `tree --check`.

## Report
List created/edited paths, verification result and anything left for the user to decide.
