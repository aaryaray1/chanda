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
1. **Audit follow-up (recurring):** after each batch of audit packets, run `audit-report`. Check each `error`, and each arithmetic mismatch, by hand: recompute, read the source. Record each verdict in `connections/pipeline/audit/audit-manual.jsonl` and apply verified fixes with `apply-audit`.
2. **Open forecast:** after MJD 61506 (2027-04-11), score Grover et al.'s Vela window with a fresh catalogue (T04 `--catalogue`). After 2031-11-20, or once 10 pairs exist, run T02. Neither falls in this weekend.
3. **Test track (lower yield; see the 00:32 log entry):** only a published *falsifiable forecast* with public data that nobody has scored yet is worth a slot. Ideas still unchecked: Millhouse et al. (2022) glitch-rate law against post-2021 glitch counts (beware catalogue lag), and Carlin & Melatos (2020) ρ₊ > 0.25 on unseen glitches (T02 machinery).
4. **Map additions:** `map-additions.jsonl` (23 records) awaits the user's OK. Next step if approved: a pipeline path to add records (an `add-records` command, which writes and verifies sources like finalize does).
5. **Sunday wrap-up:** a summary at the top of this file, then a final report to the user.

## Done
- 2026-11-20:
  - T01 pre-registered (`bf6476f`) and run (`f752941`): P1 survives, P2 inconclusive;
  - T02 pre-registered (`ca28318`), to be tested later;
  - audit stage built and running (2/20 packets);
  - C2021 fixed via `apply-audit`;
  - analogue-gravity node added.
  - T03 pre-registered (`883d299`) and scored (`20a58fe`).
- 2026-11-21: T04 forecast scorecard pre-registered (`5b6f6a8`) and scored; T03 framing corrected (retrospective, not prospective).
- 2026-11-21: map additions drafted (23 records, `map-additions.jsonl`); frontier track screened (no new claims).
- 2026-11-20 (late): T01 referee (F6) applied (`020a9f1`); T03 reading corrected (`611eea7`).
- 2026-11-21: T04 and T03 refereed (F6) and revised: 7 forecasts added as an addendum, one-per-event counting, strict prospective labels, both headlines withdrawn.

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
- **2026-11-21 00:32:** test, frontier and map tracks.
  - **Solar Cycle 25 forecasts:** dropped. Evaluations exist (Jouve et al. 2025 validation; a 2026 review of solar-cycle prediction).
  - **The glitch ↔ earthquake "time-predictable" model link:** published (Zhou et al. 2026, arXiv:2609.38837), but missing from the map, so it became a map addition.
  - **Frontier track:** read the top 24 low-overlap link-prediction pairs. All are textbook links or known analogies (CMB recombination, neutron transport, Mathieu/Hill in preheating and accelerators, the photon ring as an unstable orbit), so no specific uncharted claim. Closed.
  - **Map track:** drafted `connections/frontier/map-additions.jsonl`, 23 records:
    - the 18 well-charted missing pairs;
    - glitches ↔ time-predictable earthquakes;
    - four analogue-gravity links (acoustic metric, BEC Hawking radiation, fibre horizons, Weyl anomaly).

    Every source is verified (27/27), the schema passes `connections_pipeline.py check`, and every formula was hand-checked (the Hawking–Page temperature fixed to state AdS₄ and AdS₅). Not in the registry: awaiting the user's OK.
- **2026-11-21 00:33:** T01 prior art closed.
  - Screened the abstracts of all 39 INSPIRE citers of arXiv:1809.03064. No per-glitch test of P1 or P2 on post-2018 data, so the narrow verdict stands.
  - Added to the results: Liu et al. (2019), no backward correlation in B1737−30, consistent with P1 (in-sample); and Carlin, Melatos & Wheatland (2023), the forward correlation absent in solar flares.
  - ADS citers outside INSPIRE are not screened.
- **2026-11-21 00:41:** T04, a scorecard of published next-glitch forecasts.
  - **Pool:** 12 forecasts, taken from the *first* arXiv versions of 5 papers.
    - Akbal et al. (2017), v1, forecast 2018-06-17 ± 164 d; v3 rewrote it after the outcome.
    - Gügercinoğlu et al. (2020), v1: Vela, J2111+4606, J2229+6114; v2 adds J1023−5746.
    - Zhu et al. (2025), v1: Crab.
    - Grover et al. (2025), v1: Vela, still open.
    - Melatos & Drummond (2019).
  - **Pre-registered** in `5b6f6a8`.
  - **Calibration:** 3 of 7 numeric forecasts within 1σ (binomial p = 0.15), 6 of 7 within 2σ, mean z = −0.06.
  - **Against the renewal baseline:** the forecasts were closer in 4 of 7. For Vela, the baseline beat both prospective vortex-creep forecasts.
  - **Not scored:** two γ-ray pulsars lack catalogue coverage (unresolved). The Grover et al. Vela window is pending until 2027-04-11.
  - **Deviation:** J2229+6114's anchor matched by identity (MJD 58396 in the paper, 58424 in the catalogue).
  - **Correction:** found that T03's forecasts were retrospective, not prospective; T03 is corrected.
- **2026-11-21 14:40:** T04 and T03 refereed (F6) and revised.
  - **Interruption:** the monthly spend limit stopped the session at 00:59, mid-revision. The loop's retries at 01:13 and 01:34 hit the same limit, and a laptop restart ended the session. Resumed at 14:23 from this log and the session transcript.
  - **Referee verdict:** "needs revision", with one fatal issue. A failed forecast was missing: Zhu et al. (2026), arXiv:2601.12130, a major Crab glitch by August 2026. I had skipped it because it was withdrawn. The withdrawal was administrative: a duplicate of arXiv:2506.02925, whose 2026-06-18 revision drops the forecast without comment.
  - **Added as an addendum** (outside the registered pool): ZH26 (false), AK17m (Akbal's third scenario), LI24a–c (Liu et al. 2024, Table 4: one pending, two overdue or not catalogued), GR25vc (Grover's vortex-creep forecast), and GU20e (a postdiction, listed and not counted).
  - **One forecast per event:** 2 of 6 within 1σ (P = 0.085), 5 of 6 within 2σ. Post hoc, Σz² = 18.9 on 6 (p = 0.004), or p = 0.18 without the one 3.4σ miss. The forecast beat the renewal baseline in 3 of 6.
  - **Withdrawn headlines:** "roughly calibrated" and "a naive renewal baseline beats the Vela forecasts", both from the title of `b121af9`.
  - **Other fixes:** AK17's prospective label (v1 came out about 6 h after the glitch); GU20c's bound had passed before publication; the registered *overdue* verdict is restored for GU20b and GU22d; GR25 is relabelled as Bayesian; T03's "honest uncertainties" is softened.
  - **Prior art:** none of the 97 INSPIRE citers of the six forecast papers scores the forecasts. OpenAlex returned 503 and Semantic Scholar was rate-limited, so neither was searched.
- **2026-11-21 14:50:** audit follow-up, packets 7–12 (12/20 done; today's cap of 10 is used, and the last 8 run on Sunday).
  - **Hand-checked 4 flags:** 2 were real and are fixed with `apply-audit`, 2 were the auditor's mistakes.
    - **Fixed C1737** (proton radius): the map had m_r³c⁴/(ħc)², which is a mass. The c⁶ form gives 5.1975 meV/fm² for the muonic-hydrogen 2S shift (sympy, CODATA 2022).
    - **Fixed C1506** (Kondo): for H = J S·s with s = σ/2, scaling is dg/d ln D = −g² and T_K ~ D e^(−1/g) (Affleck 2008, arXiv:0809.3474, eqs 1.15–1.25). The record had the Pauli-convention factors. The auditor had called this *minor*.
    - **Dismissed:** C1107 (eB = m_π² is 3.3×10¹⁴ T; "~10¹⁴ T" is the literature's order of magnitude) and C1178 (the Earth-twin contrast is 1–2×10⁻¹⁰ at quadrature; the auditor used full phase).
  - **Skipped records:** the model silently returned no verdict for 5 records (C0493 and C0536 in packet 3, C0656 and C0706 in packet 4, C2013 in packet 12). All 5 were audited by hand, and all are correct. `audit-report` now lists any record in a finished packet that has no verdict.
  - **Brief:** `brief-audit.md` gains one false-alarm pattern (wrong observing geometry) and one under-call (a convention mismatch that changes an exponent is an `error`).
  - Registry and pipeline changes are uncommitted, per the commit rule.

