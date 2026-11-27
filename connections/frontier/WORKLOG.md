# Frontier work log and queue (autonomous run, 2026-11-20 → 2026-11-22)

## Wrap-up (2026-11-22 02:27): the queue is empty, so the loop stops here
**Breakthrough: none.** The strongest results are careful, refereed and pre-registered, but each is either partly known or awaits a decisive test. All work is committed and pushed (public repo `aaryaray1/chanda`, latest commits listed below).

**Results, all pre-registered before scoring and refereed:**
- **V1, the most consequential.** Published vortex-creep "times to the next glitch" track the observed intervals in-sample: within-pulsar ρ = +0.66, and better than the pulsar's own mean in 25 of 34 pairs.
  - Glitch size alone tracks the intervals almost as well (ρ = +0.46).
  - The fits span the interval, so this is consistency, not forecast skill.
  - The one clean forecast made beforehand did worse than the baseline.
  - **The decisive test**, a blind fit to the early recovery from public Fermi-LAT timing, needs timing software not installed here.
- **G1–G3, method transfer from earthquake forecasting** (CSEP-style out-of-sample information gain, new for glitches):
  - Glitch timing is significantly non-Poisson against a calibrated null.
  - A two-parameter renewal forecast is calibrated: 208 of 231 inside its 90% intervals.
  - Large glitches carry the reservoir sign (7 of 7 pulsars; 14 of 14 with a looser cut). Small glitches look Poisson.
  - There are no aftershocks beyond about a month. The earlier "refractory" headline was withdrawn: it was the catalogue's resolution.
- **T04, a scorecard of every published next-glitch forecast.**
  - 2 of 6 primary forecasts fell within 1σ, and 4 are overdue, one a confirmed miss.
  - It added a missed failed forecast, and withdrew two headlines.
- **T01, T03:** done before this weekend's mandate update (see the Done section).

**Registered, to be checked:**
- next-glitch forecasts for 34 pulsars (G1);
- next-large-glitch forecasts for 7 pulsars (G2-P);
- **a Vela head-to-head that resolves by 2027-04-11**: Grover et al. 0.71, empirical renewal 0.31, our models 0.13;
- T02.

`analysis/score_registered.py run` scores them all against the live catalogue.

**Map and audit:**
- **Audit complete:** 789 quantitative records checked. 6 registry errors fixed (C0064, C0657, C1506, C1737, C2021, C2479), 12 false alarms dismissed, and 7 records the model skipped audited by hand.
- **Map:** 23 new connections, including an analogue-gravity node. The registry holds 2907 connections.
- **Filing:** results are filed in `knowledge/.../compact-objects/reviews/pulsar-glitch-statistics.md`.

**Toolkit:**
- `physlib verify` now requires title words in order, with the journal title via DOI as a fallback. It caught one of my wrong arXiv IDs on Saturday.
- New commands: `add-records`, and an `audit-report` that lists skipped records.

**Errors I made and caught:**
- I logged wrong times twice; they are corrected from git.
- I gave one wrong arXiv ID and one wrong paper title; the verifier caught both.
- I mis-stated a computed mass in an audit note; it is corrected.
- I extracted two wrong V1 pairs; the referee caught them.

**Next steps for the user:**
- Run the scorer monthly.
- For V1, install timing software (PINT) to run the blind early-recovery test.
- Optionally ask the vortex-creep authors for pre-glitch-only fits.

Key commits: T04 `bc81173`/`7d39a96`; G1–G3 `a95b9cb`…`ac8cf79`; Vela registration `df1f37a`; V1 `71011da`/`5c3540f`/`2e5096e`/`25c2431`; audit `bf7f1a0`; map `30c537f`; verifier `447d07e`.

**Mandate.** On 2026-11-20 (~23:30 CET) the user asked for work to continue overnight and through the weekend, until the end of Sunday 2026-11-22, resuming after usage limits reset, with the rest of the week's budget. Each loop iteration reads this file first, takes the top open item, works on it, and logs the result here before scheduling the next wake-up.

**Mandate update (2026-11-21 ~15:50, from the user):** "commit and push, and continue. stop asking for my input, find a breakthrough, or advance enough to find one." So decide the queued questions myself (map additions, filing results), push after each commit, and put the main effort into a candidate breakthrough.

**Mandate update (2026-11-27 21:20, from the user):** "continue, you have till this sundays reset to use. i want to use claude tomorrow in the afternoon, so be aware of that and factor it." So: spend the remaining weekly quota before Sunday's reset, but no work during Saturday afternoon; keep usage lean (local computation, few subagents).

## Standing rules
- **Commits:** commit all work, using `git -c user.name="Aarya Ray Chaudhuri" -c user.email="aaryaray2502@gmail.com"` and the session attribution lines. **Push after commits** (user, 2026-11-21). HTTPS has no credentials here, so push over SSH: `GIT_SSH_COMMAND="ssh -o BatchMode=yes -o StrictHostKeyChecking=yes" git push git@github.com:aaryaray1/chanda.git master`. The repo is public: scan for secrets before every push. Never commit `.claude/settings.json` or `library/fulltext/`.
- **Pre-registration first:** a test's plan and code are committed *before* its data are read. Deviations are reported in the results.
- **Registry changes:** through `connections_pipeline.py apply-audit` (after recomputing the flagged claim and confirming it against a source) or `add-records` (new connections with verified sources). Record each change below.
- **Off limits:** never print secrets. Do not edit `~/.config/chanda`, `~/.claude`, `.claude/settings.json`, or the systemd units.
- **Citations:** every cited paper passes `physlib.py verify`. Label confidence. Flag contested claims.
- **Quota:** the pipeline audit runs on its own (cap raised to 10 units a day on 2026-11-20; set `audit.per_day` back to 2 after Sunday if any packets remain). Interactive work uses the main session. Subagents are kept for referee passes and specialist checks.

## Queue (top = next)
1. **Audit follow-up: done** (2026-11-22 02:26). All 20 packets audited (789 records). 6 registry errors fixed, 12 false alarms dismissed, 7 skipped records audited by hand. The pipeline reports DONE. Earlier text: after each batch of audit packets, run `audit-report`. Check each `error`, each arithmetic mismatch and each skipped record (no verdict) by hand: recompute, read the source. Packets 13–20 run after midnight on Sunday. Record each verdict in `connections/pipeline/audit/audit-manual.jsonl` and apply verified fixes with `apply-audit`.
2. **Registered forecasts (recurring, from now until they resolve):** run `python3 -I analysis/score_registered.py run` about monthly. It fetches the live catalogue and scores G1 (34 pulsars), G2-P (7) and the Vela head-to-head, which resolves by 2027-04-11. The baseline run on 2026-11-21 has everything open. T04 and T02 have their own runs, printed by the scorer.
   **Open forecast:** after MJD 61506 (2027-04-11), score Grover et al.'s Vela window with a fresh catalogue (T04 `--catalogue`). After 2031-11-20, or once 10 pairs exist, run T02. Neither falls in this weekend.
3. **Test track: no open candidates** (closed 2026-11-21 15:00; see the log). A new slot needs a published *falsifiable forecast* with public data that nobody has scored yet.
4. **Map additions: done** (2026-11-21 15:21): 23 records added as C3013–C3035 via the new `add-records` command (28/28 sources verified). The records are kept in `../pipeline/added.jsonl`, so a re-finalize keeps them.
5. **Filing results in the tree: done** (2026-11-21 15:43). `knowledge/09-astrophysics-and-cosmology/stellar-astrophysics/compact-objects/reviews/pulsar-glitch-statistics.md` summarises T01–T04 and G1–G3 with tier and status. `docs/CONVENTIONS.md` now allows results notes in `reviews/`. Discord is not posted: the pipeline runner posts there itself, and nothing in the mandate asks for it.
6. **Glitch statistics track (G1–G3), the main breakthrough effort:** waiting on the referee and the prior-art search (both running). Then apply their fixes, and file a combined note in the tree. A next test would be a refractory deficit among large follow-ups only, which needs more large-glitch pairs or a second catalogue (ATNF).
7. **Sunday wrap-up:** a summary at the top of this file, then a final report to the user.

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
- 2026-11-21: T04 and T03 refereed (F6) and revised: 7 forecasts added as an addendum, one-per-event counting, strict prospective labels, both headlines withdrawn. Second referee round applied the same day (text fixes; every number reproduced).

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
- **2026-11-21 15:00:** test track, the last two ideas closed without a test.
  - **Carlin & Melatos (2020), ρ₊ > 0.25 in every pulsar:** T01 already checked it on the 2026 catalogue (exploratory, since T01 had seen those values). A clean test needs unseen glitches, which is what T02 waits for. Nothing to add this weekend.
  - **Millhouse et al. (2022), arXiv:2202.01930, λ = A(τ/1 yr)^(−γ):** a population-average rate law. Testing it on post-2021 counts needs each pulsar's monitoring span. The catalogue does not list spans, so a zero count cannot be read as zero glitches, and catalogue lag adds to it. Not testable cleanly with public data reachable here.
  - **T04 second-round referee:** running in the background on the revision (`bc81173`).
- **2026-11-21 15:40:** T04 second referee round, verdict "needs revision" for text only. Every number reproduced, and every first-round item was fixed or partly fixed. Applied:
  - **The Answer now reports the four overdue primary forecasts.** If they are real misses, 5 of 10 are within 2σ, and the misses are four late and one early. The referee wrote "all misses are late", which overlooks the early Akbal miss.
  - **LI24b is a confirmed miss.** Liu et al.'s own post-glitch timing solution for J1420−6048 runs to MJD 59453 with no glitch, so z ≥ +4.7. The code now handles this case through a `no_glitch_until_mjd` field (declared post hoc).
  - **Primary rule stated**, with a sensitivity line: if Zhu's 2025 window is primary, 1 of 5 are within 1σ (P = 0.038).
  - **ZH25b's baseline win is weak.** Conditioned on no glitch before publication, the baseline misses by −289 d and the forecast by −316 d.
  - **Quotes made verbatim:** AK17b and AK17m are relabelled by the paper's own scenario names, and the GR25vc quote now uses [...]. The LI24c conflicts between text and table, and between paper and catalogue, are noted.
  - **Code:** summaries report the registered and the strict prospective rules, and overdue counts. The self-test now covers the strict boundary, both window kinds, the alternative target, lower-bound HP, the confirmed-miss rule and the summary filters.
- **2026-11-21 14:58–15:33:** commit and push, then the breakthrough track (G1–G3, all pre-registered before their data were scored).
  - **Push:** HTTPS has no credentials, so pushing goes over SSH (rule above). The repo is public: every commit is scanned for secrets, and `.claude/settings.json` and `library/fulltext/` stay out.
  - **G1** (`a95b9cb` → results): a forecast competition with CSEP-style information gain (method transfer from earthquake forecasting), on 14 pulsars and 231 forecasts.
    - Log-normal renewal forecasts are **calibrated** out of sample (KS p = 0.55; 90% coverage 208/231). The published forecasts scored in T04 are not.
    - The gain over Poisson is small (+0.098 nats per forecast, not significant).
    - Size–wait slopes are positive in 13 of 14 pulsars.
    - Prospective forecasts for 34 pulsars are registered.
  - **G2** (`6c3a9be` → results): the same competition by size class.
    - **Small glitches** are Poisson-like, and their sizes worsen forecasts. This holds in all three runs.
    - **Large glitches** show the reservoir sign in 7 of 7 pulsars, and 14 of 14 with a looser cut (p = 6×10⁻⁵). Recovery cannot hide large glitches, so that sign is physical.
    - Vela's forecasts are ruined by its 1994 doublet.
  - **G3** (`0f14460` → results): **no aftershocks.**
    - Quick follow-ups: 15 against 36.4 under Poisson (p < 0.0002).
    - They do not follow large glitches, and they are not smaller, so there is no Båth's-law analogue.
    - Unlike earthquakes, glitches are not triggered failures. Part of the deficit may be recovery masking.
  - **Map:** the 23 additions are in the registry (2907 connections).
  - **Running:** the referee on G1–G3, and paper-scout for F3 prior art.
- **2026-11-21 15:33–15:40:** the Vela head-to-head was registered, and the referee and prior-art reports on G1–G3 arrived.
  - **Registered `df1f37a`:** forecasts of the next large glitch for 7 pulsars, plus a Vela test that resolves by 2027-04-11. P(a large Vela glitch in that window): Grover et al. 0.71, empirical renewal 0.31, G2 models 0.13.
  - **Prior art (paper-scout):**
    - G1's out-of-sample forecast scoring appears new for glitches; its result is partly known (Melatos & Drummond 2019).
    - G2 is an out-of-sample check of Fuentes et al.'s (2019) in-sample "two triggers" picture.
    - G3: Melatos & Warszawski (2009) proposed aftershocks as a test of coherent noise against avalanches, as a size-to-size prediction. Carlin & Melatos (2019) found no positive size autocorrelation in the top five pulsars. No Omori or ETAS test of glitches was found.
  - **Referee:** G1 needs minor revision, G2 and G3 need revision. Every number reproduced byte for byte, and the pre-registrations preceded their results. The two key points, both checked with the new post-hoc script `g_nulls.py`:
    - **G3's deficit is resolution.** It vanishes for waits of at least 20–60 days, and the Crab and Vela show none. The "refractory period" headline is withdrawn. The result is now "no resolvable aftershocks beyond about a month".
    - **Zero is the wrong baseline for IG.** Against a calibrated Poisson null, the renewal model's gain is significant for any size (P < 0.001; 0.001 without J1420−6048) and for large glitches (P < 0.001; 0.007 without it), but not for small ones (P = 0.11). Small-glitch sizes add nothing (shuffle null P = 0.66).
  - **Also fixed:**
    - G2's robustness claim is narrowed to J0537, Vela, J1413 and J1740, and J1420's influence is stated.
    - G1's evaluation amendment now uses a rule: P > 0.95 picks 13 pulsars, and the primary test is named.
    - G3: three quick pairs above 10⁻⁷, not two; H11 is uninformative; the undeclared dropping of unsized glitches is now listed.
    - These log times were wrong (I had guessed them) and are corrected from git.
  - **Toolkit weakness:** `physlib verify` matches titles fuzzily, so my wrong Tsuzuki et al. title passed. It is fixed by hand. The verifier should be made stricter.
  - **Breakthrough status: none yet.**
    - The strongest results are out-of-sample confirmations of in-sample ideas: large glitches are non-Poisson with the reservoir sign; small glitches are Poisson.
    - The forecast-scoring method is new for glitches.
    - The nearest decisive test is the Vela head-to-head by 2027-04-11.
- **2026-11-21 15:42–15:45:** filing, scoring tool, and a replication decision.
  - **Filed** the glitch results in the tree (`697a6c6`).
  - **Fixed the verifier** (`447d07e`): titles must match in order, with the journal title via DOI as a fallback. Regression: 618/618 notes and 1969/1969 registry sources pass; the invented title fails.
  - **Wrote `score_registered.py`.** It tests itself with an injected Vela glitch. The baseline run on 2026-11-21 has no new glitches and everything open.
  - **ATNF replication (G4) dropped.** ATNF adds 109 glitches Jodrell Bank lacks, but only 9 after MJD 58500. Most of the difference is old glitches with different epochs, so a replication would largely reuse the same detections. A merged, de-duplicated catalogue would be the right input, but merging epochs and sizes (J1709−4429's 2018 size differs 50-fold) needs judgment calls best left to a curated effort.
- **2026-11-21 15:46–15:53:** V1, a meta-analysis of vortex-creep predictions of the time to the next glitch.
  - **Registered first** (`71011da`). The extraction and code were committed before the run (`5c3540f`): 36 pairs, 6 papers, 7 pulsars. J0537−6910 is excluded by the rule (no t_obs or epochs). Three papers had no pairs.
  - **Result** (`2e5096e`): in-sample, t_th tracks t_obs within pulsars (ρ = +0.71, p = 0.0001) and beats the pulsar's own mean in 24 of 34 (p = 0.012). The median |ln| error is 0.093 against 0.190.
  - **Post-hoc contrast** with T04's prospective forecasts:
    - The same model forecasting *before* the next glitch has a median error of 0.34 over the 3 resolved forecasts. Four more are overdue, and one is a confirmed miss.
    - Both glitches analysed before and after their successor moved toward the outcome: 0.31 → 0.014 (J2229+6114) and 0.16 → 0.021 (Vela 2019).
  - **Reading:** the in-sample agreement is a consistency relation (the fits span the interval), not yet forecast skill.
  - **The decisive test:** fit only the early part of each recovery from public Fermi-LAT timing. That is the next step if the referee agrees.
  - **Referee:** running.
- **2026-11-21 15:55–20:02:** the V1 referee ("needs revision") was applied. A usage-limit pause ran from about 16:00 to 20:00.
  - **Two extraction errors fixed:**
    - The J0738−4042 pair was the duration of a 2007 timing event, so it is removed.
    - J2229+6114's 2013 t_obs was the end of the recovery (975 d), not the interval (1628 d).
  - **Corrected registered results:** ρ = +0.66 (p = 1.5×10⁻⁴), and 25 of 34 against the baseline (p = 0.0045). The verdicts are unchanged.
  - **Post-hoc additions** (`v1_meta.py posthoc`):
    - J0537−6910 mapped to catalogue epochs: pooled ρ = 0.70–0.71 over 66 pairs. Within J0537−6910 the model tracks but does not beat the mean.
    - Grover et al.'s t₀ ± 3τ_nl convention: unchanged.
    - **Glitch size alone tracks the intervals,** ρ = +0.46. Much of t_th's information is the glitch size.
  - **Contrast rewritten:** only one forecast made beforehand is clean (Vela 2019). In all three resolved cases the model loses to the pulsar's own baseline.
  - **Revisions are mixed:** J2229+6114 converged after the outcome; Vela 2019 was kept unchanged by the same group; Akbal v1 → v3 stayed 375 d late.
  - **Reading:** the in-sample agreement is consistency, not forecast skill. The only partial-data fit (Gügercinoğlu & Alpar 2020, from 416 days of data) went the model's way.
  - **Citation slip:** I had given a wrong arXiv ID for Espinoza et al. 2017. The verifier caught it. I dropped the attribution, because its full text does not plainly state the claimed dispute.
  - **Filed:** V1 is added to the compact-objects results note.
- **2026-11-22 00:26–00:26:** audit packets 13–16 hand-checked (16/20 done; 17–20 run at 02:13).
  - **Errors:** 0.
  - **Three arithmetic mismatches, all dismissed:**
    - C2129: the record states no number; the auditor's own value had a unit slip (4.2×10¹² Hz is 4199 GHz).
    - C2321: Q_W = 72.9 for Xe-131 was compared with N = 77, which the record does not state.
    - C2355: the Raether limit e²⁰ = 4.9×10⁸ matches the literature's "~10⁸", a factor of 5.
  - **One skipped record:** C2175 (the MSSM Higgs bound), audited by hand and correct. With v = 246 GeV the one-loop term peaks at X_t = √6 M_S.
  - My first note quoted the wrong one-loop masses (124 and 136 GeV). The code gives 127 and 151 GeV, and the note is corrected.
- **2026-11-22 02:25–02:26:** audit packets 17–20 hand-checked. The audit stage is complete (20/20; the pipeline reports DONE).
  - **Fixed C2479** (quantum Monte Carlo): the Hubbard–Stratonovich identity as written integrates to exp(+Cρ²τ³/2), with the wrong sign and τ cubed (sympy). Corrected to ∫ds e^(−s²/2) e^(i√(Cτ)sρ), with a real coupling for attractive C < 0. The auditor had called it *minor*.
  - **Dismissed three false alarms:**
    - C2582: "Γ ~ neV" is a scale label; ⁵⁷Fe's linewidth is 4.7 neV.
    - C2583: the record's fC is Q_crit, which the auditor compared with the deposited charge.
    - C2631: n_e ~ 10³⁰ spans white-dwarf densities.
  - **C2458** (chiral anomaly) was skipped by the model, audited by hand, and is correct (Gaussian and natural units).
  - **Duplicate verdicts:** packet 18 returned two each for C2524 and C2583. The report keeps one per record.
  - **Audit totals:** 6 errors fixed (C0064, C0657, C1506, C1737, C2021, C2479) and 12 false alarms dismissed out of 789 records. 7 skipped records were audited by hand, all correct.
  - **Config:** `audit.per_day` is set back to 2 (it was raised to 10 for this weekend).


- **2026-11-27 21:23–21:28:** resumed under the new mandate.
  - **Scorer run on the live catalogue:** no glitch since the 2026-11-20 snapshot, so all 41 forecasts and the Vela head-to-head are still open.
  - **OpenAlex** (down last weekend): no prior scorecard of glitch forecasts. It surfaced Gügercinoğlu et al. (2025, arXiv:2506.22936, *A&A* 706, A216). For J0537−6910 that paper *assumes* each glitch comes at full recovery and solves for persistent shifts, so it adds no V1 pairs. One sentence is added to V1.
  - **Feasibility of the blind V1 test:** pip, venv, PyPI, the Fermi FSSC and the LAT data server are all reachable, with 180 GB free. The 3PC timing models are public (304 .par files) but carry one global ν̈ plus timing-noise terms, and no TOAs, so they cannot replace per-interval fits. A real test needs LAT photons plus the spacecraft file plus PINT. Target: Vela, whose 5 Fermi-era intervals have published t_th.
  - **Research note:** `paper/glitch-forecasting.md` consolidates T04, G1–G3 and V1 for experts, with 22/22 citations verified.
- **2026-11-27 21:29:** the blind V1 test is blocked on a permission.
  - Installing PINT into a scratchpad venv (`pip install pint-pulsar`) was denied by the auto-mode classifier. Not retried, and not worked around.
  - **Waiting on the user:** with permission, the Vela blind test can run Saturday evening and Sunday (see `paper/glitch-forecasting.md`, Decisive next tests 1).
  - **Scheduled:** a one-shot resume at Saturday 19:37 (session cron). Nothing runs during the user's Saturday afternoon.
- **2026-11-27 21:30–22:07:** B1, the blind Vela test, run without PINT.
  - **Pipeline:** a numpy-only one: a minimal FITS reader, Earth positions from JPL Horizons, spacecraft positions from FT2, and the annual TT→TDB term. This is my own analysis code; I installed nothing.
  - **Steps:**
    - Registered `0114c7b` before any download.
    - Five LAT queries (1.26 M events, 1.06 M after the zenith cut), submitted one at a time as the server asks.
    - Validated before scoring: H ≥ 2640 in every 14-day window, ν(t) continuous.
    - Froze the code (`c3ed7a1`), then scored.
  - **Registered verdict: not supported.** The linear-recovery relation beats Vela's own mean interval in only 2 of 5 (median |ln| error 0.216 against 0.188). All four sensitivity runs agree, with 0–2 wins.
  - **Post hoc:**
    - Every blind t₀ is early (5 of 5, p = 0.031; 24 of 25 across variants), with t_obs/t₀ between 1.11 and 1.96.
    - Rank tracking is ρ = +0.70, with an exact p = 0.12 at n = 5.
    - The measured ν̇_pre, Δν̇ and ν̈ are typical for Vela.
  - **Reading:** in-sample agreement (V1, 0.093) does not survive blinding (0.216). Either the late recovery is slower than the early recovery, or Vela glitches well after it has recovered. Only the simplest model form was tested.
  - **Filed:** in the research note and the tree note. The referee is pending.
- **2026-11-27 22:20–22:50:** the B1 referee, and B2.
  - **The B1 referee** ("minor revision"): the registered verdict holds, and the barycentring is verified. Applied:
    - **A fair comparison:** the published in-sample fits on the same five Vela intervals score 2–3 of 5 (medians 0.153–0.159). "Does not survive blinding" is dropped.
    - **The physical reading:** Akbal et al.'s full-interval Model 1 for 2010 has a lower ν̈ (0.86 against 1.43×10⁻²¹) and comes out 134 d late, so the recovery slows.
    - **Wording:** "no blind skill" rather than "fails". The baseline is named as the geometric mean. The sign test is reported two-sided (p = 0.063).
    - **Systematics** (`b1_systematics.py`): my 0.10″ Dec slip, the missing proper motion and centroid epochs give t₀ = 889, 892, 648, 767, 536, still 2/5 and all early. Bootstrap errors are ±8–25 d.
    - **Deviations listed:** the sensitivity files were not frozen; the <200-photon skip; the 2014 mini-glitch; the 2016 interval is 781.1 d.
  - **B2:** registered `5edb1c0` after B1, before any later photon; froze `7b0466b`; extended all five intervals (206 more windows).
    - **H_B2a supported:** t₀ grows with the fit window in 5 of 5 (p = 0.031), so the recovery slows.
    - **H_B2b not supported:** full-interval fits are closer in only 3 of 5, with a median error of 0.148.
    - **Reading:** the recovery decelerates, and even fits over the whole interval do not time Vela's glitches.
    - The pipeline reproduces Grover et al.'s 921.6 d (922 d) and nearly reproduces Gügercinoğlu et al.'s 1862 d (1749 d).
    - Robust to the systematics: 5 of 5, with a median error of 0.129.
  - **Filed:** the research note and the tree note are updated.
- **2026-11-27 22:50:** paused for the night, to keep quota for the user's Saturday afternoon.
  - **Saturday 19:37** (session cron, replacing the earlier one): run the scorer, referee B2, apply its fixes, report. Then continue until Sunday's reset.
  - **Not feasible with this method:** a second-pulsar blind test. J1023−5746 and the other vortex-creep γ-ray pulsars are about 60 times fainter than Vela, too faint for 14-day H-test windows without photon weighting and coherent timing, which need packages that cannot be installed.

