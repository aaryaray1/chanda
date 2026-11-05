---
name: find-connections
description: Find and explain connections between or within branches of physics. Covers "how is X related to Y", analogies and where they break, unifying principles, and what one field's methods can do for another. Can also run a discovery pass over the knowledge tree's structural gaps and latent bridges. Use for any question about what links, unifies or parallels two topics or fields, and when asked to look for missing cross-links.
argument-hint: "[X and Y | discover [field code or node]]"
allowed-tools: Read Grep Glob Bash(python -I scripts/physlib.py *)
---
# Find connections

Request: $ARGUMENTS

You are the orchestrator here. Read `.claude/agents/physics-orchestrator.md` for the brief templates, unless you are already running as that agent. Which agent does what:
- `connections-analyst` maps and tests the bridge.
- The field specialists check each side.
- You verify and answer.

## Mode A — bridge: "X and Y", "how is X related to Y"
1. **Locate.** Run `python -I scripts/physlib.py connections "<X>" "<Y>"`. It shows the explicit cross-links, shared concepts, latent candidates, shared papers and curated themes. Read any matching `connections/themes/*.md`.
2. **Map.** Brief `connections-analyst` with `ASK: bridge X ↔ Y` and paste the query output into CONTEXT.
3. **Check each side.** Brief the specialists of the two branches in parallel. YOUR PART: "Here is the claimed correspondence <mapping>. Is it right from your branch's side, and where does it fail?" If the analyst's connection kind was *identity*, *duality* or *mechanism*, require each side's governing equation.
4. **Answer.** Give the kind of connection, the shared equations side by side with a symbol map, what each branch contributes, where it breaks, a confidence label and verified sources (`verify --stdin`).
5. **Offer to file.** Missing cross-links go through `knowledge-curator`. A major bridge deserves a theme note (`connections/themes/<slug>.md`, per `docs/CONVENTIONS.md` § Connections).

## Mode B — discover: "discover", "discover 08", "discover <node>"
1. **Candidates.** Run `python -I scripts/physlib.py connections <field|node>` for a target, or read *Structural gaps* and *Latent bridges* in `CONNECTIONS.md` for a whole-tree pass. Take the top 10–15.
2. **Test.** Brief `connections-analyst` with `ASK: discover` and the candidate list. It keeps only connections that hold up physically, labelled by kind and confidence, with proposed cross-links.
3. **Spot-check.** Anything labelled *proposed* goes to the relevant specialists, in parallel.
4. **Report.** Table: candidate · verdict (confirmed / refuted / open) · kind · why · proposed cross-link (source README → target README).
5. **File with consent.** Ask the user before filing. A few cross-links are a small change; a batch is a reorganization. On approval, `knowledge-curator` adds the links to the notes' *Connections* / *See also* sections. Then run `python -I scripts/physlib.py tree --check` and `verify` on the touched files, which also rebuilds the atlas.

## Rules
- Concept co-occurrence and shared papers are leads, not evidence. Every connection you assert must survive the analyst's test and the specialists' check.
- Analogies must say where they break.
