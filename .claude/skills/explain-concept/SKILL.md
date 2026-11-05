---
name: explain-concept
description: Teach a physics concept clearly at a chosen level — school, introductory or advanced undergraduate, graduate or research — with intuition, the precise statement, key equations, a worked micro-example, common misconceptions and self-check questions, grounded in the knowledge tree. Use whenever the user asks "explain", "what is", "how does … work", "ELI5", "intuition for", "I don't get …", or is studying for an exam, even if they don't name a level.
argument-hint: "[concept] [level: school|intro|undergrad|grad|research]"
allowed-tools: Read Grep Glob Bash(python -I scripts/physlib.py *)
---
# Explain a concept

Request: $ARGUMENTS

## Before writing
1. Find the concept in `TREE.md` and read the topic README (and its parent subfield README for context and prerequisites).
2. Decide the level. If unstated, infer from wording; default to introductory undergraduate and offer to adjust.
3. Identify the one or two prerequisite ideas the learner must already have; if they probably lack them, include a two-line refresher.

## Structure (adapt length to level)
1. **One-sentence core idea** — what the concept *is*, without jargon.
2. **Picture / intuition** — an analogy or thought experiment. Label analogies as analogies and say where they break.
3. **Precise statement** — the definition or law, with the key equation in LaTeX and every symbol defined with units.
4. **Worked micro-example** — a short calculation with real numbers (CODATA constants via `physlib.py constants`) that shows the concept doing work.
5. **Common misconceptions** — two or three, each with why it's wrong (field specialists' "Pitfalls" lists in `.claude/agents/` and `knowledge/00-foundations/history-and-philosophy-of-physics/physics-education-research/README.md` help).
6. **Check yourself** — two or three questions of rising difficulty, answers hidden at the end under "Answers".
7. **Where next** — links to related nodes in `knowledge/`.

## Level guide
| Level | Math | Tone |
|---|---|---|
| school | arithmetic, simple algebra; no calculus | concrete, everyday examples |
| intro | algebra, basic calculus, vectors | build from Newton/Maxwell basics |
| undergrad | ODEs/PDEs, linear algebra, QM formalism | derivations welcome |
| grad | field theory, group theory, advanced methods | concise, cite primary literature |
| research | whatever the frontier uses | current debates, recent papers with verified citations |

## Teaching principles (from physics education research)
- Confront the likely misconception directly rather than only stating the right idea.
- Prefer one well-chosen example over three superficial ones.
- Ask the learner to predict before revealing results when the format allows.
