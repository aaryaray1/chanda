---
name: literature-review
description: Produce a structured, fully cited literature review of a physics topic — history, current understanding, open problems and a key-papers table — from verified arXiv/INSPIRE/OpenAlex sources, reviewed by the referee agent and saved into the knowledge tree under the topic's reviews/ folder. Use when the user asks for a review, survey, state-of-the-art summary, "overview of research on…", background section for a report or thesis, or a deep dive into a field's literature.
argument-hint: "[topic] [optional: depth, audience]"
allowed-tools: Read Grep Glob Write Edit Bash(python -I scripts/physlib.py *)
---
# Literature review

Topic: $ARGUMENTS

## 1. Scope
- Pin the topic to one node in `TREE.md` (create it with `grow-tree` if missing). Read the node and its parent README.
- Split the topic into 3–6 subquestions (history/foundations, theory, experiment, current debates, applications).

## 2. Gather (in parallel)
Launch one `paper-scout` per subquestion in a single message. Ask each for: 3–6 foundational papers, 2–4 reviews, 3–6 recent papers (last 2 years), each with a one-line contribution, all verified.

## 3. Read
For the 5–10 most important papers, read beyond the abstract (`physlib.py fulltext`, then Read; or WebFetch the arXiv abs page). Note quantitative results with their uncertainties.

## 4. Synthesize — template
```
---
title: Review — <topic>
date: <today>
node: <knowledge path>
---
# <Topic>: a review
## Summary (5 sentences)
## 1. Background and history
## 2. Theoretical framework
## 3. Experimental/observational status
## 4. Open problems and active debates
## 5. Outlook
## Key papers
| Paper | Year | Contribution |
## References
- Author et al. (Year). "Title". *Venue*. [arXiv/doi link]
```
Every factual claim beyond textbook level carries a citation. Distinguish consensus from debate explicitly.

## 5. Check
- `python -I scripts/physlib.py verify <draft file>` — zero failures required.
- Send the draft to the `referee` agent; fix critical and major issues.

## 6. File
- Save to `knowledge/<node>/reviews/<slug>.md`.
- Add a "**Reviews.** [title](reviews/<slug>.md)" line to the node README.
- `python -I scripts/physlib.py tree --check`.
- Report the path and the three most important findings to the user.
