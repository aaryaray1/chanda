# Frontier work log and queue (autonomous run, 2026-11-20 → 2026-11-22)

**Mandate.** On 2026-11-20 (~23:30 CET) the user asked for work to continue overnight and through the weekend, until the end of Sunday 2026-11-22, resuming after usage limits reset, with the rest of the week's budget. Each loop iteration reads this file first, takes the top open item, works on it, and logs the result here before scheduling the next wake-up.

## Standing rules
- **Commits:** commit only frontier work (pre-registrations, analyses, results, cards, this log), using `git -c user.name="Aarya Ray Chaudhuri" -c user.email="aaryaray2502@gmail.com"` and the session attribution lines. **Never push.**
- **Pre-registration first:** a test's plan and code are committed *before* its data are read. Deviations are reported in the results.
- **Registry changes:** only through `connections_pipeline.py apply-audit`, and only after recomputing the flagged claim myself (sympy or numpy) and confirming it against the cited source. Record each change below.
- **Off limits:** never print secrets. Do not edit `~/.config/chanda`, `~/.claude`, `.claude/settings.json`, or the systemd units.
- **Citations:** every cited paper passes `physlib.py verify`. Label confidence. Flag contested claims.
- **Quota:** the pipeline audit runs on its own (cap raised to 10 units a day on 2026-11-20; set `audit.per_day` back to 2 after Sunday if any packets remain). Interactive work uses the main session. Subagents are kept for referee passes and specialist checks.

## Queue (top = next)
1. **Audit follow-up (recurring):** after each batch of audit packets, run `audit-report`. Check each `error`, and each arithmetic mismatch, by hand: recompute, read the source. Apply verified fixes with `apply-audit`. Log false alarms as auditor errors.
2. **Test track, T04 and later** (T03 done). Next idea: published *forecasts* tested on data collected after them, outside pulsar glitches. Candidates: Solar Cycle 25 amplitude forecasts against SILSO sunspot numbers (check prior art first, since evaluations probably exist), and GW population predictions against GWTC-4. Then screen the 489 open cross-branch registry records that contain numbers (confidence *current research* or *proposed*, not contested). Look for claims testable on public data reachable without keys (list in `PLAN.md`). Shortlist 5; for the best 2–3, run F2 card → F3 prior art → F4 pre-registration commit → F5 run → results commit.
3. **Frontier track:** F2 hypothesis cards for the top low-overlap link-prediction candidates (`candidates.jsonl`, branch 00 excluded), with F3 prior art on the specific claim. Promote any P-type claim to a sympy check.
4. **Map track (F0):** the 18 well-charted pairs (> 50 joint arXiv papers) are probably missing connections. Draft records with verified sources into `connections/frontier/map-additions.jsonl` for review. They do not go into the registry without the user's OK, because there is no pipeline path for additions yet.
5. **T01 prior art, the gap the referee found:** screen the *abstracts* of all INSPIRE and ADS citers of arXiv:1809.03064, not only titles. Add anything relevant to the results' prior-art section.
6. **Sunday wrap-up:** a summary at the top of this file, then a final report to the user.

## Done
- 2026-11-20:
  - T01 pre-registered (`bf6476f`) and run (`f752941`): P1 survives, P2 inconclusive;
  - T02 pre-registered (`ca28318`), to be tested later;
  - audit stage built and running (2/20 packets);
  - C2021 fixed via `apply-audit`;
  - analogue-gravity node added.
  - T03 pre-registered (`883d299`) and scored (`20a58fe`).
- 2026-11-20 (late): T01 referee (F6) applied (`020a9f1`); T03 reading corrected (`611eea7`).

## Log
- **2026-11-20 23:50:**
  - T02 pre-registered (`ca28318`). It uses glitches unseen in the 2026-11-20 snapshot, not only glitches after that date, because southern-pulsar glitches after about 2018 are largely uncatalogued.
  - T03 (Melatos & Drummond 2019 next-glitch forecasts): all 3 pass at two sigma. The HP baseline fails on J0631+1036 (z = +5.7). Committed `883d299` and `20a58fe`.
  - Audit cap raised to 10 a day. The T01 referee is running.
- **2026-11-20 23:58:**
  - The T01 referee returned: no fatal issues, arithmetic reproduced exactly, 8 major issues of framing, power and selective reporting. All fixed in `020a9f1`.
  - The fixes: a reproducible `posthoc` subcommand, both data snapshots archived, novelty downgraded to *partly known* (Zhu et al. 2025 on the Crab), no registry change.
  - Key new fact: one 2.2×10⁻⁹ Crab glitch at MJD 57839.8 flips the 2018 backward hint from r₋ = 0.69 to −0.07.
  - T03 reading corrected (`611eea7`).
  - Lesson for later results: report every post-hoc variant, quantify power, and separate catalogue revisions from new data.
- **2026-11-21 00:35:** audit follow-up. 6/20 packets done (237 records).
  - **Hand-checked all 7 flags:** 3 were real and are now fixed in the registry, 4 were the auditor's mistakes.
    - **Fixed:** C2021 (wrong factor in the Unruh formula), C0657 (Lighthill pressure missing 1/c₀²; units checked with sympy), C0064 (centrifugal sign convention).
    - **Dismissed:** C0229 (unit slip in the auditor's expression), C0455 (order-of-magnitude claim held to a 15% tolerance), C0865 (no stated number to compare), C0245 (the auditor's group-velocity derivation was wrong; sympy).
  - **Improvements:** `brief-audit.md` now lists those four false-alarm patterns. `audit-report` now keeps hand reviews: `audit-manual.jsonl` overrides the model, and the report lists fixed and dismissed records separately.
  - The pipeline code changes are uncommitted, per the commit rule.
