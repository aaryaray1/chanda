# Connection-discovery plan (multi-session)

**Goal.** Find, check and plot every genuine connection between the notes of the 12 branches: all 66 branch pairs, plus the links *within* each branch between its subfields. The results feed `connections/registry.jsonl`, which in turn feeds the interactive map (`connections/map.html`, `map.svg`), the branch codices preloaded into the specialists, the analyst's atlas and `CONNECTIONS.md`.

**Why it is split into many small runs.** The first attempt ran 12 long-lived analyst agents in parallel inside one huge session. Every turn re-read hundreds of thousands of tokens, so it hit the 5-hour limit four times and then the weekly limit. Now:
- every unit of work is one fresh headless `claude -p` session with a small context;
- the pipeline pre-builds each unit's material (node list, links, concepts, or the codex sections a packet needs) and sends it with the brief on stdin, so a unit is one turn plus at most 3 README reads;
- sessions run lean: no MCP servers, no skills, no user plugins or hooks, only Read/Grep/Glob. That cuts the fixed overhead per turn from ~48k to ~13k tokens;
- a few units run per run;
- runs are spaced out and capped per day;
- all state lives in this folder, so nothing depends on a session surviving.

## Stages
| Stage | Unit of work | Who does it | Count |
|---|---|---|---|
| 1. Discovery | one set: a branch pair `A-B`, or `A-within` | a plain session following `brief-discovery.md` | 78 sets (27 were done by the first attempt) |
| 2. Review | one packet of ≤ `review_chunk` connections touching a branch | that branch's specialist, given only the codex sections for the packet's nodes (no literature lists), following `brief-review.md` | ~40–70 packets |
| 3. Finalize | applies verdicts (confirm, revise, reject, add); marks cross-branch disagreements as *contested*; verifies every citation against arXiv/Crossref; writes the registry; rebuilds the tree, codices, atlas and map | local Python, no model calls | 1 |

The order is strict. Review packets are built automatically when the last discovery set lands, and finalize runs automatically when the last packet is reviewed.

## Pacing (edit `config.json`)
| Key | Default | Meaning |
|---|---|---|
| `units_per_run` | 4 | units per scheduled run |
| `interval_hours` | 2 | how often the scheduled task fires (re-register after changing it) |
| `max_units_per_day` | 30 | hard daily cap, so the week's quota isn't spent in a day |
| `cooldown_minutes` | 60 | after a usage limit whose reset time can't be read, skip runs for this long (a readable reset time is used instead) |
| `transient_cooldown_minutes` | 15 | after an overload, network or rate-limit error |
| `max_attempts` | 4 | give up on a unit after this many failed tries (limit, sign-in and transient errors don't count) |
| `last_attempt_model` | `{"discovery": "opus", "review": ""}` | model for a unit's final attempt, so a unit Sonnet keeps failing gets a stronger try before it blocks |
| `max_budget_usd` | `{"discovery": 1.5, "review": 8}` | per-unit spending cap passed to `claude --max-budget-usd`; a runaway guard about 10× a normal unit |
| `unit_timeout_minutes` | 45 | a unit's whole process tree is killed after this |
| `stale_running_hours` | 3 | fallback only: when a unit marked running counts as abandoned outside the runner |
| `stall_hours` | 24 | alert if no unit has completed for this long (outside pauses and cooldowns) |
| `review_chunk` | 100 | connections per review packet |
| `model` | `{"discovery": "sonnet", "review": ""}` | per stage; `""` is the session default (Opus). Discovery runs on Sonnet because every record is reviewed afterwards |
| `effort` | `{"discovery": "medium", "review": "medium"}` | per stage; less thinking means fewer output tokens |
| `stage_gate` | `{"review": {"platform": "linux", "not_before": "2026-11-09T00:00"}}` | per stage: which OS may run it (`linux`, `win32`) and the earliest start. Another OS gets `HANDOFF` and its runner removes its own schedule; before the date, runs wait |

At the defaults, discovery finishes in about 2 days and review in about 2–3 more. Lower `max_units_per_day` or `units_per_run` if other work shares the same quota. Each unit's token use is logged in `runs.log`, so you can see what a run costs.

**Sign-in.** Interactive logins expire. For the unattended task, run `claude setup-token` once and store the token as the user environment variable `CLAUDE_CODE_OAUTH_TOKEN`. If the sign-in lapses anyway, the runner logs it and stops without spending attempts.

## Automation
Discovery ran on Windows. From 2026-11-09, review runs on the Linux server: see `docs/SERVER.md`. There, `scripts/connections_runner.py` is the runner and `chanda-pipeline.timer` (systemd, user) the schedule. It does the same steps as the Windows runner below, with these differences:
- the lock is an `flock` on `.run.flock`, which the kernel releases when the runner dies;
- orphans are found via `/proc`;
- the one-off resume is a `systemd-run` timer;
- alerts and a findings digest go to Discord;
- `DONE` disables the timer;
- `--health` is the health check.

The Windows runner:
- `scripts/run_connections.ps1` does one budgeted run:
  1. takes a kernel mutex. Windows releases it the moment a runner dies, so a crash never leaves a lock that blocks later runs;
  2. kills orphaned unit sessions left by a dead runner, and resets units it left marked `running`;
  3. asks the pipeline for the next units (`next` stops early on a pause, cooldown, daily cap or blocked units);
  4. writes each unit's prompt to `work/<unit>.prompt.md` and runs it as a lean headless session (`--permission-mode dontAsk`, Read/Grep/Glob only, `--max-budget-usd`, killed at the timeout);
  5. ingests stdout and stderr separately. Ingest classifies the session as OK, FAILED, LIMIT, AUTH or TRANSIENT, files the records and logs the token use;
  6. on a usage limit, cools down until the reset time it reads from the message and, if that is before the next scheduled run, books a one-off `PhysicsConnectionsPipeline-Resume` task for just after the reset;
  7. writes a snapshot if anything changed, then runs `doctor --alerts` and raises a desktop notification, at most once per problem per day, for anything that needs you.
- `scripts/schedule_connections.ps1 -Register` creates the Windows scheduled task `PhysicsConnectionsPipeline`. It runs the runner every `interval_hours` for up to a year while you are logged in. `-Unregister` removes it and any pending resume task. With no switch it prints a full health check. The runner removes the task by itself when the pipeline reports `DONE`.
- Everything is logged to `connections/pipeline/runs.log` (rotated to `runs.log.1` at 2 MB).

## Safeguards
| Risk | Guard |
|---|---|
| a run dies mid-unit (crash, kill, shutdown) | mutex frees at once; next run reaps the orphan session and resets the unit, refunding the attempt (twice at most) |
| two runs at once (schedule + manual) | the mutex; the second run exits |
| usage limit | cooldown to the parsed reset time; attempt refunded; one-off resume task |
| sign-in expired | attempt refunded; desktop alert with the fix |
| overload / network / rate limit | attempt refunded (6 times at most per unit), 15-min cooldown |
| runaway session | `--max-budget-usd` per unit, timeout kills the process tree, daily unit cap |
| a unit keeps failing | last attempt on `last_attempt_model`; then `BLOCKED` + alert instead of a silent stall |
| malformed model output | JSON objects are extracted from fences or pretty-printed text; stderr kept apart; failed outputs archived in `work/failed/` |
| corrupt or half-written state | atomic writes with retries (OneDrive), `state.json.bak` one save behind, automatic restore |
| bad `config.json` | invalid values fall back to defaults with a logged warning |
| planner messages mistaken for units | `next` tags every line (`UNIT`, `INFO`, `WAIT`, `HANDOFF`, `BLOCKED`, `CAPPED`, `DONE`) |
| two machines working on diverging copies of the state | `stage_gate.platform`: the other OS gets `HANDOFF` and removes its own schedule |
| unit sessions billed to an API key or seeing the bot token | the Linux runner drops `ANTHROPIC_API_KEY` and `DISCORD_*` from the unit environment |
| registry damage | snapshot refuses to shrink the registry by >10%; finalize refuses to drop >50% without `--force` |
| citations dropped during a network outage | finalize probes arXiv and Crossref first and retries next run instead of dropping sources |
| silent stalls | `doctor` flags blocked units, no completions in `stall_hours`, no runs logged, budget hits, invalid batch files; the health check also shows the task, its expiry, token, executables and lock |

## Manual control
```powershell
python -I scripts/connections_pipeline.py status          # stage, progress, pending units
python -I scripts/connections_pipeline.py doctor          # health check of state, outputs and progress
powershell -File scripts/schedule_connections.ps1          # doctor plus task, token, executables and lock
python -I scripts/connections_pipeline.py next            # what the next run would do
powershell -File scripts/run_connections.ps1 -Units 2      # one run now
powershell -File scripts/run_connections.ps1 -DryRun       # show the prompts without running
python -I scripts/connections_pipeline.py pause --hours 6 --reason "exam week"   # or plain `pause`; undo with `resume`
python -I scripts/connections_pipeline.py reset --exhausted [--cooldown]        # retry blocked units; clear a cooldown
python -I scripts/connections_pipeline.py snapshot        # interim registry + map from what exists
```
On the Linux server:
```bash
python3 -I scripts/connections_runner.py --health        # timer, sign-in, executables, lingering, agent, Discord, lock, then doctor
systemctl --user start chanda-pipeline.service           # one run now (or: python3 -I scripts/connections_runner.py --units 2)
python3 -I scripts/connections_runner.py --dry-run       # show the prompts without running
```
Inside an interactive Claude session, `/connections-run` does the same as one runner pass.

## Files
`state.json` holds unit status, attempts, notes, cooldown and pause; `state.json.bak` is the previous save. Alongside it:
- `discovery/batch-*.jsonl`: raw analyst records;
- `review/packet-*.jsonl`, `review/review-*.jsonl`: packets and verdicts;
- `merged.jsonl`: deduplicated, with IDs;
- `rejected.json`: connections the specialists rejected, with reasons;
- `work/*.out.txt`, `work/*.err.txt`: each unit's last stdout and stderr; `work/failed/`: the 40 most recent failed outputs;
- `run.lock`: who holds the run (informational; the real lock is the mutex on Windows, `.run.flock` on Linux); `alerts.json`: which alerts were shown today.

## After it finishes
The registry holds every connection with:
- its kind and strength;
- its confidence: *established*, *current research*, *proposed* or *contested*;
- which specialists checked it;
- its verified sources.

The map shows them all. Next steps that need your OK:
- Write the confirmed cross-links into the notes' *Connections* lines (a batch edit through `knowledge-curator`).
- Write theme notes for the biggest new bridges.
