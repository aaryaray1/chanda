# Specialist review: week of 2026-11-09

Stage 2 of `PLAN.md`, run on the Linux laptop by `chanda-pipeline.timer`. All 59 packets run under the tightened `brief-review.md`. The 12 packets reviewed on Windows on 2026-11-05 under the old brief were queued again on 2026-11-06. Their old verdicts (89% confirm, 10% revise, 0.6% reject) are kept in `review/old-brief/` for comparison.

## Timeline at the current config (4 units per run, every 2 h at :13, at most 30 a day)
| When | What runs | Specialists |
|---|---|---|
| Thu 11-05 to Sun 11-08 | Setup and checks (below). The timer fires but gets `WAIT` from the stage gate. | none |
| Mon 11-09, 00:13 to about 14:30 | 8 runs, 30 packets (`00-1` to `05-5`), then capped until midnight | foundations, classical, em-optics, statistical, quantum, relativist |
| Tue 11-10, 00:13 to about 14:30 | 8 runs, 29 packets (`06-1` to `11-5`) | particle, nuclear, condensed-matter, astro, plasma, applied |
| Tue 11-10, after the last packet | Finalize runs automatically with no model calls. It applies verdicts, marks cross-branch disagreements *contested*, verifies citations (arXiv/Crossref), and rebuilds the registry, map, codices and `CONNECTIONS.md`. On `DONE` the timer disables itself. | none |
| Wed 11-11 to Fri 11-13 | Follow-up steps, which need your OK (below) | as needed |

Cost: about $0.80 a packet at API prices (Opus, medium effort; the stricter brief adds some output), so about $47 in all, roughly $24 on each day. It comes out of the same **Claude Pro** subscription the Discord agent uses. Discovery hit the 5-hour usage limit 6 times. When that happens the pipeline cools down and resumes by itself, so expect the end to slip into Wednesday rather than fail. To spread the work out, set `max_units_per_day` to 10 in `config.json`; the last packet then lands on Sat 11-14.

## Before Monday
1. Setup green: `python3 -I scripts/connections_runner.py --health --test-discord` shows no FAIL, and the test message arrives.
2. Dry run: `python3 -I scripts/connections_runner.py --dry-run` builds the next prompts without spending anything.
3. Done 2026-11-05: `brief-review.md` was tightened. A spot check of 30 confirmed records showed sound physics but loose labels: about a quarter had a wrong kind (mostly `identity`), an inflated strength, an overclaim or filler. 6 of the 7 rejections were duplicates, which finalize now drops cleanly (`duplicate_of`) instead of marking them *contested*. Expect more revisions and a slightly higher cost per packet (more output).
4. Done 2026-11-06: the 12 old-brief packets were queued again. A packet counts as done when `review/review-<packet>.jsonl` exists, so the old files were moved to `review/old-brief/`. `reset` alone does not re-queue a finished packet.

## While it runs
- Each run posts a digest to Discord: packets reviewed, confirmed/revised/rejected/new, samples. Alerts post at most once per problem per day.
- Usage limit: it cools down to the reset time and books a one-off resume. Sign-in expired, blocked unit or stall: an alert says what to do.
- Pause with `python -I scripts/connections_pipeline.py pause --hours N` and undo with `resume`. Retry blocked units with `reset --exhausted`.
- A missed run (laptop off) is caught up on boot (`Persistent=true`).

## After finalize (needs your OK)
1. Read the *contested* connections and `rejected.json`, and settle the contested ones with the two specialists involved, or with `connections-analyst`.
2. Run a `knowledge-curator` batch edit that writes confirmed cross-links into each note's *Connections* line, then `verify` and `tree --check`.
3. Write theme notes in `connections/themes/` for the biggest new bridges.
4. Commit. The Discord agent picks up the rebuilt codices at its next 05:00 restart.
