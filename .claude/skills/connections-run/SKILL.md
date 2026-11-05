---
name: connections-run
description: Advance the multi-session connection-discovery pipeline by one budgeted run (discovery sets, specialist review packets, or the final merge), or report its progress. Use when the user asks to continue or resume the connection work, check how far it has got, or after a usage-limit reset.
argument-hint: "[status | run [units] | dry]"
allowed-tools: Read Bash(python -I scripts/connections_pipeline.py *) PowerShell
---
# Connection pipeline: one run

Request: $ARGUMENTS (empty = status, then one run)

The plan, pacing and files are in `connections/pipeline/PLAN.md`. The work runs in fresh headless sessions launched by the runner, never inside this conversation. That keeps each unit small, so it doesn't eat the usage quota.

1. Health check:
   - Linux server (where review runs): `python3 -I scripts/connections_runner.py --health`;
   - Windows: `powershell -NoProfile -ExecutionPolicy Bypass -File scripts/schedule_connections.ps1`.

   Both cover the schedule, the sign-in, the executables, whether a run is active, and `doctor` (stage, progress, cooldown, pause or stage gate, blocked units, stalls). Report any FAIL or WARN with the fix it names. A `HANDOFF` or "gated" line means this stage belongs to another machine or a later date (`stage_gate` in `config.json`): don't override it unless the user asks.
2. Unless the user only wants status, run one pass:
   - on Linux: `python3 -I scripts/connections_runner.py` (add `--units N` if the user gave a number, or `--dry-run` for "dry");
   - on Windows, in PowerShell: `powershell -NoProfile -ExecutionPolicy Bypass -File scripts/run_connections.ps1` (`-Units N`, `-DryRun`);
   - long passes: run it in the background and report when it finishes;
   - a pass that logs `another run is active` means the scheduled run is already working: don't start another.
3. Read the new lines at the end of `connections/pipeline/runs.log` and summarise them:
   - units done or failed, with record or verdict counts;
   - any usage-limit cooldown, transient error, recovered or orphaned unit, `blocked:` or `ALERT` line;
   - the snapshot size.
4. Blocked units: show their notes (`status`) and the newest file in `connections/pipeline/work/failed/`, then offer `python -I scripts/connections_pipeline.py reset --exhausted`. To stop the pipeline for a while, use `pause [--hours N]` / `resume` rather than unregistering the task.
5. When the stage is `done`, point the user to `connections/map.html` and the registry summary in `CONNECTIONS.md`.
