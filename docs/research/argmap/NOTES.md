# Argument map data: method, counts, judgement calls

*Draft 2026-10-08, built against commit 7cc7b27 (branch `research`). Data only; the renderer is separate. Nothing here changes a verdict: every `audit_status` is read from the current claim-file verdicts or from `research/checks/RESULTS.md`, and is provisional until R5. Integration fixes were applied on 2026-10-08 (edges, side labels and sources; each item is marked "fixed 2026-10-08" under "Errors and inconsistencies"). The counts below were re-run after them.*

Files:
- `standard-forms.md`: premise–conclusion reconstructions. Full forms for ROOT and the other 30 load-bearing nodes (A3 promoted 2026-10-09); one-row mini-forms for every other claim a defeater targets.
- `defeaters.yaml`: every attack, typed (undermining / undercutting / rebutting), with first date, locator, audit status and counters.
- `lineage.yaml`: dated versions of arguments and numbers, linked by descent, revision, borrowing, reply, citation and (inferred) resemblance.
- `research/tools/argmap_check.py`: the checker (verbatim quotes, ids, dates, edge coverage). Run `research/.venv/bin/python -I research/tools/argmap_check.py`.

## Counts (checker output, 2026-10-08, after the integration fixes)

**Update 2026-10-09 (R4 C1c, C1d and D1 integration).** The checker now reports 293 defeaters, 196 lineage nodes and 122 standard forms, 0 errors, 0 warnings. A3 promoted to load-bearing (ROOT P1 and A P4 rest on it; full standard form added, mini-form row removed); mini-forms B2e and C5b added. Added: d279–d280 (chk:C1c against chk:C1b's call-depth inference, upheld, and C6's inference, partly), d281–d286 (chk:C1d against C6 C and C7 C, upheld; C5a P2, upheld; keruru's C5b P2 sampling correction, partly, a slip-ledger item; B2e C, partly; and the audit's own chk:C1c error-term reading, partly), d287–d291 (chk:D1 against D2h C, G3b's inference, Ga's inference (the one-specific-outcome reading), G3 P2 (the plenty-of-alternatives reading) and D1a C; all partly), d292–d300 (reviews #9–#11 against chk:C1c, chk:C1d, chk:D1; all upheld and applied). Status updates from the new verdicts: d061 (C5b → C5a) partly → upheld; d267 (B2e → B2b) untested → partly; d083, d166, d069 (D2h ↔ D1a, D1a → D) untested → partly; d275 (C5b → C7) basis updated. Registry ids chk:C1c, chk:C1d, chk:D1 and rev:R4-{C1c,C1d,D1}-{correctness,steelman-day,steelman-critic}; lineage nodes L-audit-c1c-2026, L-audit-c1d-2026, L-audit-d1-first-2026 (the first-pass 'Day's m ≈ 1' wording, retracted; quote from git e70363d) and L-audit-d1-2026. Counters recomputed mechanically (only rows whose attacker is a new target changed). Grounded labels (accepted/rejected/undecided): as argued 111/105/2, audited strict 162/56/0, audited lenient 120/98/0.

**Update 2026-10-09 (R4 GAP-07b and corpus-refresh integration).** The checker now reports 271 defeaters, 192 lineage nodes and 120 standard forms, 0 errors. Added: d266–d269 (new critic claims from the 2026-10-09 refresh: Matev A2i → A2e, B3i → B3a, G5 → G; keruru B2e → B2b, `untested`; all `hierarchy_edge: true`), d270–d273 (chk:GAP07b against A3a P2, the critics' rate route B5f, A3x P1 and the audit's own chk:GAP07 P1, the last retiring its 22.5M upper bound), d274 (B7a against Day's new B9) and d275 (C5b against Day's new C7), d276–d278 (review #8 against chk:GAP07b, all upheld and applied); mini-forms A3x, B9, C7; registry ids chk:GAP07b and rev:R4-GAP07b-{correctness,steelman-day,steelman-critic}; lineage nodes L-day-bp-generous-2026, L-day-bp-range-2026, L-audit-gap07b-2026, L-day-gf-1587-2026, L-day-1-over-2ne-restated-2026, L-matev-n-over-ne-2026, L-keruru-measured-ne-draft-2026. Counters recomputed mechanically: d006 (attacker A3x) gained d272; d039, d040 (attacker B5f) gained d271; d250 (attacker chk:GAP07) gained d273. Grounded labels (accepted/rejected/undecided): as argued 102/102/2, audited strict 154/52/0, audited lenient 111/95/0.

**Update 2026-10-09 (R4 H3 integration).** The checker now reports 258 defeaters, 185 lineage nodes and 117 standard forms, 0 errors. Added: d259–d262 (attacker chk:H3 against H P2, G2's inference, H8 P1 and H5 P4; all `partly`, all conditional on hard adaptive treadmill selection with a soft deleterious load), d263–d265 (review #7 against chk:H3, all upheld and applied), registry ids chk:H3 and rev:R4-H3-{correctness,steelman-day,steelman-critic}, and lineage nodes L-audit-h3-2026 and L-audit-h3-1-300-2026 (the pre-review "1/300 reproduced" wording, replaced). Counters recomputed mechanically: d107, d108 (attacker G2) gained d260; d118 (attacker H) gained d259. Grounded labels (accepted/rejected/undecided): as argued 95/99/2, audited strict 146/50/0, audited lenient 104/92/0.

**Update 2026-10-08 (R4 GAP-04/07/02 integration).** The checker now reports 251 defeaters (238 before this integration; the 238 already included the R4 E and G1 rows d240–d245), 183 lineage nodes and 117 standard forms, 0 errors. Added: d246–d253 (attackers chk:GAP04, chk:GAP07, chk:GAP02, and Day's new claim A6 against the registry id x:darwinzdf42-hitchhiking), d254–d258 (review #6 against the three checks), the A6 mini-form, and lineage nodes L-pan-sweeps-2026, L-sweep-signatures-2026, L-audit-gap04-2026, L-audit-gap07-2026, L-audit-gap02-2026. Counters were recomputed mechanically (only rows with attacker A5b gained a counter, d249). The side/type/status tables below are as of the integration fixes and were not re-broken-down.

| | count |
|---|---|
| Standard forms | 30 full (ROOT + 29 other load-bearing nodes) + 83 mini-forms = 113 |
| Defeaters | 232 (115 represent hierarchy `attacks` edges; 117 come from Responses sections, Day's counters, audit checks and reviews). Before the fixes: 239 and 124. Seven placeholder or duplicate rows were deleted (d001, d009, d042, d057, d088, d110, d124) |
| Lineage nodes | 178 (233 parent links, 46 of them inferred, on 45 nodes) |
| Verbatim quotes checked | 178 lineage + 19 defeater quotes, all found |

**Defeaters by attacker side and type** (side = hierarchy side of the attacking node, or registry side):

| attacker side | undermining | undercutting | rebutting | total | upheld | partly | not upheld | untested |
|---|---|---|---|---|---|---|---|---|
| Day | 27 | 19 | 16 | 62 | 7 | 30 | 14 | 11 |
| critics | 32 | 15 | 22 | 69 | 24 | 34 | 0 | 11 |
| allies | 0 | 0 | 2 | 2 | 1 | 0 | 0 | 1 |
| literature (incl. the audit-raised nodes B1c, B4a, C1; see judgement 3) | 12 | 8 | 3 | 23 | 5 | 16 | 1 | 1 |
| audit (checks, R2 arithmetic/fidelity, reviews) | 43 | 32 | 1 | 76 | 41 | 35 | 0 | 0 |
| **total** | 114 | 74 | 44 | 232 | 78 | 115 | 15 | 24 |

Targets: Day 134, critics 66, the audit's own checks 16, literature 12, allies 4. Two targets are registry ids: x:dawkins-weasel (literature) and x:eugine-sqrtN (critic). The audit's 76 attacks fall on Day (40), critics (17), the audit's own checks (16, all from the four review rounds), allies (2) and literature (1). Day-side claims are 106 of 194 hierarchy nodes and carry most load-bearing numbers, which is the main reason more defeaters target them. 11 defeaters are Day against Day (self-revisions and unreconciled statements). Before the fixes this was 19; it included five mis-aimed edges (H, H4, H9 → G1; D9, D9a → D), two mis-typed ones (C2 → C2c, D3c → D2g) and B1c → B1a, now audit-side.

**Lineage nodes by side and fate:**

| side | alive | revised | dormant | superseded | conceded | retracted | total |
|---|---|---|---|---|---|---|---|
| Day | 40 | 20 | 16 | 2 | 4 | 1 | 83 |
| critics | 42 | 1 | 2 | 0 | 0 | 1 | 46 |
| allies | 7 | 0 | 0 | 1 | 0 | 2 | 10 |
| literature | 17 | 0 | 1 | 0 | 0 | 0 | 18 |
| audit | 16 | 0 | 0 | 0 | 0 | 5 | 21 |

Kinds: 58 argument, 54 reply, 36 value, 17 revision, 8 concession (Day 5, critics 3), 5 retraction (audit 3, Day 1, keruru 1, labelled critic under the keruru rule). Relations: responds-to 79, descends 58, cites 33, revises 32, resembles 25, borrows 6.

The Day column is larger because Day's numbers have many dated versions (the versions ledger); the critics' arguments mostly appear once. Day's "revised" count is a count of versions, not of errors.

## Method

### Standard forms (diagram A)
1. **Scope.** Every node with `load_bearing: true` in `hierarchy.yaml` (30, including ROOT and ROOT-M) has a full form. Every other claim that a defeater targets has a mini-form (premises the defeater needs, conclusion, inference type).
2. **Steelman.** Each form is built from the author's own strongest dated statement in the claim file. Day's arguments are written as Day would accept them; the critics' as they would. Implicit premises are taken from the claim files' "Assumptions → Implicit" lines and marked `[implicit]`. Where an author later withdrew a premise (B1's empty start, B3a's 1/(2Nₑ), H8's cap on total k, keruru's N/Nₑ endorsement, KITTENS's linearity), the premise stays in the form as made and the withdrawal is recorded as a self-defeater. This keeps the same rule for both sides.
3. **Inference types.** deductive, arithmetic (a deductive special case), statistical, analogical, abductive. Mixed arguments name the weakest link.
4. **Citations.** Every premise links to the claim file holding the verbatim quote.

### Defeaters (diagram A)
1. **Coverage.** One defeater for each of the 115 `attacks` edges (124 before the 2026-10-08 fixes) in `hierarchy.yaml` (`hierarchy_edge: true`), plus attacks described in the claim files' Responses sections, Day's counter-attacks, attacks made by the audit's own checks, and the reviews that corrected the audit's checks.
2. **Typing rule, applied identically to all sides.**
   - *undermining*: denies a premise. `target_part` = the premise label.
   - *undercutting*: grants the premises and denies that they support the conclusion (e.g. latency vs throughput, specific list vs any list, divergence vs fixed-count). `target_part: inference`.
   - *rebutting*: argues directly for the negation of the conclusion (e.g. a competing count). `target_part: C`.
   When an attack could be read two ways, the narrower reading is used: if the attacker names a premise, it is undermining; if it grants the numbers, undercutting.
3. **first_date** is the earliest dated source in the corpus that makes the attack, which can be earlier than the target (pre-emptive replies are noted). For literature used by the audit against a claim (Kimura 1962, Nunney 2003, Keightley 2012, Good 2017), `first_date` is the publication date and `by` names who applied it. Where only a bound is known (Mansfield's undated YouTube comments) the bound is used and `date_note` says so.
4. **audit_status** says whether the *attack* survives the audit so far:
   - `upheld`: the attacker's verdicts hold and the attacked part is contradicted / misread / non-sequitur / arithmetic-error, or a reviewed check confirms the attack;
   - `partly`: the attack holds in part, in a tested regime only, or the attacker's own verdict is contested;
   - `not_upheld`: a check or verdict goes against the attack (or the attacker withdrew it);
   - `untested`: no check and pending verdicts.
   `audit_basis` names the verdict or RESULTS section used. (`audit_basis` is an added field, outside the requested schema.)
5. **counter** is computed mechanically: every defeater whose `target` equals this defeater's `attacker`. It lists attacks on the attacking claim (or check) *as a whole*. It does not claim that each counter touches the premise the defeater relies on. Self-revisions such as `B1d → B1` therefore also appear as counters to the attacks B1 makes.
6. **Id registry.** Attackers that are not hierarchy nodes use registered ids: `x:` (a corpus statement with no claim node), `chk:` (an audit check), `rev:` (an audit review). The table below is read by the checker.

### Lineage (diagram B)
1. Each node is one dated version of an argument or number, with a verbatim quote of ≤ 30 words checked by the script.
2. **Relations:** `descends` (same side, continues the argument), `revises` (same author changes it), `borrows` (takes a point from the other side; used only across sides), `responds-to`, `cites` (the source names the parent), `resembles` (no source states the link).
3. **inferred.** A link is `inferred: true` when no source states it (all `resembles`; some `responds-to`, `borrows`, `cites` where the timing and content match but the text names no one). The node-level `inferred` is true whenever any of its parent links is inferred, and `why` gives the reason. The checker enforces this.
4. **Dates** come from the sources. `date_note` flags dates that are announcement dates (Probability Zero 1st edition, 2026-01-06), bounds (Mansfield, ≤ 2026-10-01), month-only (Kimura 1962-06, Kimura & Ohta 1969-03, Wistar 1966-04) or year-only literature.
5. **fate** describes what later happened to *that version*: `alive` (still asserted), `revised` (changed by its author), `retracted`, `conceded` (given up to the other side), `superseded` (replaced by later data without explicit withdrawal), `dormant` (not restated, not withdrawn). The audit's own withdrawn wording is recorded the same way.
6. **Pre-2019 ancestors** appear only when a corpus source cites them (Haldane 1957, Kimura 1962, Kimura 1968, Kimura & Ohta 1969, the 1966 Wistar papers, CSAC 2005, Barrick 2009, Balloux & Lehmann 2012, Langergraber 2012, Tenaillon 2016, Good 2017, Milton 1992). Nunney 2003, Keightley 2012, Axe 2004, Taylor 2001 and Keefe & Szostak 2001 are cited by no corpus author (only by the audit), so they are not lineage nodes; they appear in `defeaters.yaml` as literature applied by the audit.

## Id registry

| id | side | what it is | source |
|---|---|---|---|
| x:Z23003785-s5.2 | day | MITTENS 3.0 §5.2: Ara−2's −906 read as a biological collapse | https://zenodo.org/records/23003785 §5.2 (2026-09-28) |
| x:CA-06 | critic | Camestros: 35 fixed by 15,000 generations, ~429 gens/fixation (with a typo) | Camestros 2026-01-27/28 para 28 |
| x:day-dembski-scaling | day | Day's answer to Dembski's scaling question (DE-01) | Dembski Substack interview, 2026-09-28 |
| x:day-clue | day | "confused mutations with fixations" | voxday.net 2026-09-22 ¶17 |
| x:errors-hide | day | "Where the Errors Hide" (Day–Athos exchange): P(fix) = x₀ called wrong for real populations | voxday.net 2026-09-21; raw `sources/raw/day/blog-2026-09-21-where-the-errors-hide.txt` |
| x:day-TNSL | day | "They Never Stop Lying" ¶4: none of Day's math assumes serial fixation | voxday.net 2026-10-01 |
| x:day-math-teacher | day | "Math Teacher Can't Math" ¶7: parallel fixation included in the rate | voxday.net 2026-09-30 |
| x:BO-paths | critic | Bowers Point 1: multiple mutational paths can lead to similar phenotypes | Day's repost, voxday.net 2026-03-04 |
| x:dawkins-weasel | literature | Dawkins's Weasel program (1986): cumulative selection reaches a 28-letter target in about 50 generations; quoted in Day's post from approxion.com (secondhand) | voxday.net 2026-09-12 "Probability Weasel" (added 2026-10-08) |
| x:eugine-sqrtN | critic | Commenter "Eugine" at Tree of Woe: "Vox is wrong about parallel fixation" (sqrt(N) / LessWrong speed-limit summary; recombination), known only as quoted by Day | voxday.net 2026-01-10 "A First Challenge" ¶2–¶3 (added 2026-10-08) |
| x:darwinzdf42-hitchhiking | critic | DarwinZDF42: selective sweeps fix many loci at once, mostly neutral (hitchhiking as a source of fixations) | Reddit r/DebateEvolution 1wv4zeg comment pd99y5x and 1wss2wj comment pcovtvf (raw `sources/raw/critics/arctic-tree-1wv4zeg.json`, `arctic-tree-1wss2wj.json`) (added 2026-10-08) |
| chk:B0 | audit | textbook baselines | research/checks/RESULTS.md §B0 |
| chk:B0.4 | audit | beneficial fixation time | RESULTS §B0.4 |
| chk:B1 | audit | empty vs full pipeline | RESULTS §B1 |
| chk:B1c | audit | sourced Nₑ histories | RESULTS §B1c |
| chk:B2a | audit | Hard Limits tail (exact chain) | RESULTS §B2a |
| chk:B3 | audit | N vs Nₑ in fixation probability | RESULTS §B3 |
| chk:B3b | audit | Balloux–Lehmann and RRME 0.743 | RESULTS §B3b/B3c |
| chk:B4a | audit | two-lineage divergence with ILS | RESULTS §B4a |
| chk:C1 | audit | 1240k ascertainment | RESULTS §C1 |
| chk:C1b | audit | Day's binned 21-count | RESULTS §C1b |
| chk:C2 | audit | turnover coefficient d | RESULTS §C2 |
| chk:F1 | audit | latency vs throughput | RESULTS §F1 |
| chk:F2 | audit | multi-locus interference | RESULTS §F2/A-sim |
| chk:A-sim | audit | LTEE scaling simulation | RESULTS §F2/A-sim |
| chk:H | audit | cost of selection (Haldane, Nunney, Keightley) | RESULTS §H |
| chk:H2-hard | audit | hard-selection multilocus treadmill | RESULTS §H2-hard |
| chk:R2-arith | audit | R2 arithmetic recomputations recorded in claim files and the balance ledger | claim files "derived" lines; ledgers/balance.md (2026-10-07) |
| chk:R2-fidelity | audit | R1–R2 fidelity checks of cited sources | ledgers/fidelity.md; claim-file literature tables (2026-10-07) |
| chk:R2-term3-ratio | audit | R2 note comparing Term 3 with Haldane + d (7.7×, corrected to 17.1×) | git ad44c23 claims/H8 line 41 |
| chk:E | audit | founder hazard (LTEE mutators) | RESULTS §E; results/R4-E.md |
| chk:E4 | audit | relictation exact chain | RESULTS §E; results/R4-E.md |
| chk:G1 | audit | Bernoulli barrier: specific vs any, many-locus response | RESULTS §G1; results/R4-G1.md |
| chk:GAP04 | audit | Weissman–Barton finite-map limit vs F2 and human requirements (R/4–R/2–simulated envelope) | RESULTS §GAP-04/07/02; results/R4-GAPS-04-07-02.md §1 (added 2026-10-08) |
| chk:GAP07 | audit | indel/SV event counts from germline rates (k = μ) vs Day's base-pair totals | RESULTS §GAP-04/07/02; results/R4-GAPS-04-07-02.md §2 (added 2026-10-08) |
| chk:GAP02 | audit | sweep-scan detection window: expected detectable completed sweeps (power-1 upper bound) | RESULTS §GAP-04/07/02; results/R4-GAPS-04-07-02.md §3 (added 2026-10-08) |
| chk:H3 | audit | cost of selection at human scale: hard adaptive treadmill, soft/hard load, long-run φ, finite supply (all conditional) | RESULTS §H3; results/R4-H3-human.md (added 2026-10-09) |
| chk:GAP07b | audit | direct count of divergence events from the UCSC hg38–panTro6 alignment (non-T2T): SNVs, indel events, bp ladder, bracket 7–14× | RESULTS §GAP-07b; results/R4-GAP07b-alignment.md (added 2026-10-09) |
| chk:C1c | audit | Day's 11-bin aDNA statistic under real AADR call depth and an ancestry-replacement WF model (N_e axis; model-conditional) | RESULTS §C1c; results/R4-C1c.md (added 2026-10-09) |
| chk:C1d | audit | Day's 11-bin and two-period aDNA statistics on the real AADR v62.0.p1 / v66.p1 genotypes; replication of keruru's temporal N_e | RESULTS §C1d; results/R4-C1d.md (added 2026-10-09) |
| chk:D1 | audit | sequence-space spike: alternatives per needed change from RNA neutral networks (ViennaRNA), ProteinGym DMS and the GB1 landscape, against G1's flip | RESULTS §D1; results/R4-D1-spike.md (added 2026-10-09) |
| chk:ROOT-M-survey | audit | keyword survey of computed vs asserted exclusions | claims/ROOT-excluded-mechanisms.md |
| chk:D9-exploratory | audit | exploratory Weasel runs (not pre-registered) | claims/D9, D9a Responses |
| rev:review-2 | audit | correctness review #2 | research/checks/REVIEW.md (2026-10-07) |
| rev:review-3 | audit | review #3 (correctness + two-sided steelman) | REVIEW.md (2026-10-07) |
| rev:R4-correctness | audit | review #4, correctness | research/checks/results/REVIEW-R4-correctness.md (2026-10-08) |
| rev:R4-new | audit | review #4, new checks | results/REVIEW-R4-new.md |
| rev:R4-steelman-day | audit | review #4, Day-side steelman | results/REVIEW-R4-steelman-day.md |
| rev:R4-steelman-critic | audit | review #4, critic-side steelman | results/REVIEW-R4-steelman-critic.md |
| rev:R4-GAPS-correctness | audit | review #6, correctness (GAP-04/07/02) | results/REVIEW-R4-GAPS-correctness.md (2026-10-08) |
| rev:R4-GAPS-steelman-day | audit | review #6, Day-side steelman (GAP-04/07/02) | results/REVIEW-R4-GAPS-steelman-day.md (2026-10-08) |
| rev:R4-GAPS-steelman-critic | audit | review #6, critic-side steelman (GAP-04/07/02) | results/REVIEW-R4-GAPS-steelman-critic.md (2026-10-08) |
| rev:R4-H3-correctness | audit | review #7, correctness (H3) | results/REVIEW-R4-H3-correctness.md (2026-10-08) |
| rev:R4-H3-steelman-day | audit | review #7, Day-side steelman (H3) | results/REVIEW-R4-H3-steelman-day.md (2026-10-08) |
| rev:R4-H3-steelman-critic | audit | review #7, critic-side steelman (H3) | results/REVIEW-R4-H3-steelman-critic.md (2026-10-08) |
| rev:R4-GAP07b-correctness | audit | review #8, correctness (GAP-07b) | results/REVIEW-R4-GAP07b-correctness.md (2026-10-09) |
| rev:R4-GAP07b-steelman-day | audit | review #8, Day-side steelman (GAP-07b) | results/REVIEW-R4-GAP07b-steelman-day.md (2026-10-09) |
| rev:R4-GAP07b-steelman-critic | audit | review #8, critic-side steelman (GAP-07b) | results/REVIEW-R4-GAP07b-steelman-critic.md (2026-10-09) |
| rev:R4-C1c-correctness | audit | review #9, correctness (C1c) | results/REVIEW-R4-C1c-correctness.md (2026-10-09) |
| rev:R4-C1c-steelman-day | audit | review #9, Day-side steelman (C1c) | results/REVIEW-R4-C1c-steelman-day.md (2026-10-09) |
| rev:R4-C1c-steelman-critic | audit | review #9, critic-side steelman (C1c) | results/REVIEW-R4-C1c-steelman-critic.md (2026-10-09) |
| rev:R4-C1d-correctness | audit | review #10, correctness (C1d) | results/REVIEW-R4-C1d-correctness.md (2026-10-09) |
| rev:R4-C1d-steelman-day | audit | review #10, Day-side steelman (C1d) | results/REVIEW-R4-C1d-steelman-day.md (2026-10-09) |
| rev:R4-C1d-steelman-critic | audit | review #10, critic-side steelman (C1d) | results/REVIEW-R4-C1d-steelman-critic.md (2026-10-09) |
| rev:R4-D1-correctness | audit | review #11, correctness (D1) | results/REVIEW-R4-D1-correctness.md (2026-10-09) |
| rev:R4-D1-steelman-day | audit | review #11, Day-side steelman (D1) | results/REVIEW-R4-D1-steelman-day.md (2026-10-09) |
| rev:R4-D1-steelman-critic | audit | review #11, critic-side steelman (D1) | results/REVIEW-R4-D1-steelman-critic.md (2026-10-09) |

## Judgement calls

1. **Self-defeat recorded as defeat.** When an author withdraws or revises a premise (Day: B1d, B3g, H1, A3b, E6; keruru: B7c; KITTENS: RE-09; Hancock's on-screen correction; Camestros CA-03), the later statement is entered as a defeater of the earlier one (`B1d → B1 P3` etc.) and, in the lineage, as `revises` / `concession` / `retraction`. The same rule is applied to the audit's own withdrawn wording (7.7×, "literal 1/300 falsified", "soft within 15% of hard", "does not rescue Day", the CSAC "tension").
2. **Literature used by the audit.** Nunney 2003, Keightley 2012, Good 2017, Kimura 1962, Taylor 2001 and Keefe & Szostak 2001 are entered as attackers with `by` naming the literature and the audit that applied it. No critic in the corpus cites Nunney or Keightley (balance ledger), so those attacks are not credited to critics.
3. **Audit-raised nodes (B1c, B4a, C1).** `lint_research.py` allows only `day | critic | ally | literature` as sides, with no `audit`. Since 2026-10-08, nodes raised or answered by the audit therefore carry `side: literature` and a front-matter comment saying they are audit nodes. B1c was `day` before (its quotes are Day's, but the node is the audit's question and check). C1 was `critic` before (no published critic made the point). B4a was already `literature`. The defeaters keep the hierarchy attacker id and name the audit in `by`. Counts by side therefore show these three under literature.
4. **Edges that look mis-typed or mis-targeted** (as built; see Errors item 5 for what was fixed on 2026-10-08). Four judgement-call edges kept their `edge_flag` (d062 C5b→C4, d097 E1→A2, d105 F4→F, d118 H→G2). The 17 flagged rows as originally built: d001 A2c→A2b, d009 A5→A2, d020 B1c→B1a, d042 B5g→F1, d049 B6c→G1, d057 C2→C2c, d062 C5b→C4, d088 D3c→D2g, d095 D9→D, d096 D9a→D, d097 E1→A2, d105 F4→F, d110 G2c→G2, d113 G2f→G3, d118 H→G1, d120 H4→G1, d124 H9→G1. Six of these (B5g→F1, C2→C2c, G2c→G2, D9→D, D9a→D, G2f→G3) contain no attack at all and are marked `not_upheld`/`untested` for that reason.
5. **Mansfield's comments** are undated YouTube comments. Day quotes and answers them in his post of 2026-10-01, so 2026-10-01 is used as a terminus ante quem (`date_note`). The video was posted 2026-09-23.
6. **Secondhand and AI-produced text.** Grok's 800,000μ (B3f), Athos's sentence in "Where the Errors Hide", Gariépy's 2019 words, Bowers's review and Rosenhouse's book are all known only through Day's reposts or third parties. They are entered with that noted in `date_note`/`label`; their side is that of the person whose argument it is.
7. **keruru's side (rule fixed 2026-10-08, stated in `opponents/keruru.md`).** Statements dated before the 2026-08-26 retraction post are `ally`; statements in that post and later are `critic`. Claims B7c and B4g moved from `ally` to `critic`. Lineage nodes L-keruru-chains-2026, L-keruru-retraction-2026 and L-keruru-adna-zero-2026 moved from `ally` to `critic`. L-keruru-endorse-2026 and L-keruru-nne-2026 stay `ally`. The retraction node is now `critic` because its content argues against Day's N/Nₑ and aDNA claims. Before this, the map labelled one post (2026-08-26) both ally and critic.
8. **`borrows` vs `resembles`.** `borrows` is used only when the borrowing text states or plainly adopts the other side's point (Day's 08-27 concession, "The Response to the Retraction"; the 10-01 full-pipe concession answering Mansfield; KITTENS reusing Day's SNV-only count). Where only timing and content match (3.0 §7.3 after McCarthy's bp-vs-events point; Relictation's martingale statement after keruru), the link is `borrows` with `inferred: true` or `resembles`.
9. **Pre-emptive replies.** Several replies predate the attack they answer (A5d before KITTENS; Day's TNSL "none of my math assumes serial" before Hancock's video; C1a before C1; B2d before Mansfield/McCarthy). They are recorded with their own dates; the checker allows a defeater to predate its target, but not a lineage child to predate a descends/revises/borrows/responds-to parent.
10. **audit_status is about the attack, not the target.** A Day defeater on a critic claim marked `not_upheld` means the audit's verdicts go against that attack, not that the critic is right on everything. Most of Day's `not_upheld` counters (14 after the 2026-10-08 fixes) rest on premises he later withdrew himself (N/Nₑ, empty start).
11. **counter is mechanical** (see Method). It over-counts where a check or claim is attacked on a point unrelated to the defeater it is listed under.

## Ambiguities left open

- Whether 3.0 §7.3 (SNV-only concession) was in the 2026-09-28 version of Z23003785 or added by the 2026-10-04 modification (not diffed).
- The date of the Probability Zero 1st edition text (2026-01-06 is the blog announcement; Camestros's transcription of the formula is 2026-01-24/25).
- Appendix A of the book ("Therefore fixation must be sequential") is known only through Day's 2026-10-01 quotation; its own date is unknown.
- The aDNA "21" exists in Z18525185 text (line 263 "We observe 21") but the C6 claim counts it from bins; the lineage quotes the paper's own sentence.
- Whether the Bowers review's "1/N" refers to any Day text (d105, flagged).

## Errors and inconsistencies spotted in existing files (listed by the argmap build; fixed 2026-10-08 as marked)

1. **Missing post-concession source.** No claim file covers Day's "Where the Errors Hide" (2026-09-21; `sources/raw/day/blog-2026-09-21-where-the-errors-hide.txt` ¶11–12; listed in bib-day.md). In it the Athos text Day posts says "P(fix) = x₀ is a wrong answer to the real question" for real populations, 25 days after Day's 2026-08-27 concession that the fixation probability is 1/(2N). B3g's Weaknesses and the versions.md "N vs Nₑ in k" row omit it; Z23188201 (2026-10-06) then restates 1/(2N) "regardless of offspring distribution". **Fixed 2026-10-08:** claims/B3g now has a "Later statement in tension with the concession" block with Day's words (¶8, Q76) and Athos's (¶10, ¶12, Q77–Q78), Athos's opposite ¶4 line, and two readings: withdrawal, or the no-covariance model is valid but real populations violate it. A Responses line notes that the covariance objection is already in the 08-27 post (¶3), so the concession was qualified from the start. versions.md "k/μ" and "N vs Nₑ in k" rows now include the post. quotes-day.md has Q76–Q78 and discrepancy row 18. bib-day.md already listed the post. (¶ counts use the quotes-day convention: TITLE = ¶1. "¶11–12" above counted the same way; the "P(fix) = x₀ is a wrong answer" sentence is ¶10.)
2. **"2.2×" Hössjer gap does not reproduce.** claims/A5a line 41, ledgers/balance.md line 46 and claims/H5 line 36 say Hössjer's "2.2× gap" comes from d inside the neutral rate. The neutral count with d is 7.59M (20/7.59 = 2.6×); the quoted "only by a factor of 2" is Hössjer's Eq. 2.4 selection scaling (≈10.3M, 20/10.3 = 1.9×). Two different gaps appear to be conflated, and neither is 2.2. **Fixed 2026-10-08** (recomputed from the PDF, `sources/raw/critics/hossjer-mittens-review.pdf` pp.3–5): eq. 2.4 gives 15,800 × 3e9/4.6e6 = 10.30M, so 20/10.30 = 1.94 ("only by a factor of 2"). Eq. 3.1 gives 3e9 × 0.45 × 1.25e-8 × 450,000 = 7.59M, so 20/7.59 = 2.63. The 2.2 was d's own factor, 1/0.45 = 2.22. Without d: 16.9M (1.19× short) and 22.9M (above 20M). Corrected in claims/A5a l.41, ledgers/balance.md l.46, claims/H5 l.36, claims/ROOT-h l.39 and opponents/ola-hossjer.md (the same error appeared there too).
3. **versions.md, aDNA row** goes 0 (blog 2026-01-14) → 1/3 (Z23046531, 2026-09-29) and omits the 21-count of Z18525185 (2026-02-08), which sits between them (claims/C6). (The task brief's "0 → 1/3 → 21" is also not chronological.) **Fixed 2026-10-08:** row now reads 0 (2026-01-14) → 21 vs ~630 (Z18525185, 2026-02-08) → 1/3 (Z23046531, 2026-09-29), noting that the 21 is not reproducible (C1b).
4. **versions.md, CHLCA row** omits MITTENS 2025's 6–7 My and the return to 6.3 My in MITTENS 3.0 (2026-09-28) after the 2026-05-07 250 kya–1.3 Mya statement (claims/A1c records the tension). **Fixed 2026-10-08:** row now reads 9 My (2019) → 6–7 My (Z18165980) → 200–580 kya → 68 kya → 68–330 kya → 250 kya–1.3 Mya → 6.3 My (Z23003785). The chains in claims/A1c and B4c were updated to match.
5. **Hierarchy edges**: the 17 flagged rows above (six carry no attack content: B5g→F1, C2→C2c, G2c→G2, D9→D, D9a→D, G2f→G3; three are Day-on-Day edges into G1 from H, H4, H9 that probably meant the critics' parallel-fixation reply). **Fixed 2026-10-08** in claim front-matter (each changed edge has a one-line comment): A2c→A2b and A5→A2 removed (no source; A2e already carries A5's attack). B5g→F1 and G2c→G2 retyped `supports`; C2→C2c retyped `depends-on`; D3c→D2g retyped `supports`. D9→D and D9a→D retyped `supports` (judgement); their real target, Dawkins's Weasel, is registry id x:dawkins-weasel. H9→G1 became H9→A5f (the recombination objection; d128 now represents it). H→G1 became H→G2 (judgement: Z18168236 §2.3 answers an unnamed objection). H4→G1 removed: H4 answers commenter "Eugine" at Tree of Woe (x:eugine-sqrtN; claims/H4 previously named Tree of Woe himself). B6c→G1 became B6c→G2g and G2f→G3 became G2f→Ga (judgement). Kept with comments: B1c→B1a (B1c is now audit-side), C5b→C4, E1→A2, F4→F. defeaters.yaml: d001, d009, d042, d057, d088, d110 and d124 deleted. d049, d113 and d118 retargeted. d095, d096 and d120 retargeted to registry ids (`hierarchy_edge: false`). Counters recomputed mechanically.
6. **Side labels**: C1 is `critic` but claims/C1 says no published critic made the point (audit-raised); B4a is `literature` but is an audit check; B1c is `day` but is a start-state question node answered by the audit; keruru is `ally` in B7c/B4g and `critic` in C5/C5b. **Fixed 2026-10-08:** C1 and B1c are now `literature` with an "audit" comment, because the lint has no `audit` side (judgement 3). B4a keeps `literature`, with the comment added. keruru follows the date rule in judgement 7 and `opponents/keruru.md`.
7. **E1** is a `critic` attacker with no verbatim critic statement (claims/E1 says so; the "Taylor" attribution is carried only in PLAN.md). **Fixed 2026-10-08:** corpus searched (raw critics, "hitchhik"). The nearest text is KITTENS §4 ("Neutral variants rise only by hitchhiking"), which makes a different point (the LTEE cannot see drift). E1 is now `sourcing: secondhand` with an UNSOURCED comment, because the lint allows no `unsourced` value. d097 `by` was updated.
8. **claims/B3** formal-statement table marks k ≈ 0.5μ "not verified (blog only)", but quotes-day.md Q42 is an exact-match verified quote of that blog sentence. **Fixed 2026-10-08:** the row now cites Q42 (¶9) as verified. The figure's derivation is still not given in the post.
9. **claims/B3a** Responses cite "Day's objection, RESP" (keruru's sweepstakes parent drawn uniformly at random). No matching sentence was found in the raw text of "The Response to the Retraction" (2026-08-27); the reproductive-covariance argument appears in the 2026-09-21 post (about Chalub). Locator unverified. **Fixed 2026-10-08, and the note above was wrong:** the sentence is in the 08-27 post at ¶3 (raw line 4): "his sweepstakes parent is drawn uniformly at random — setting the one parameter in dispute, the covariance between who breeds and what they carry, to zero by fiat." claims/B3a, B7 and B3g now cite it.
10. **Mansfield comment dates**: claim files give "comments retrieved 2026-10-07" only. Day's post of 2026-10-01 quotes them, which gives a sourced terminus ante quem the claim files could carry. **Fixed 2026-10-08:** a terminus ante quem 2026-10-01 (with ¶) was added to each claim-file citation of a comment Day quotes in that post (¶8, ¶12, ¶30): B1, B1c, B1d, B2, B2b, B5, B5b, B6. The "time BETWEEN successive fixations" comment (F, F1, F1a, B2d) is not quoted there, so those keep "retrieved 2026-10-07" (video posted 2026-09-23).

11. **Unmapped ally argument (from `ledgers/gaps.md`).** Hössjer's waiting-time prediction ("far exceeds 9 million years") had no node. **Fixed 2026-10-08:** new claim D15 (ally, branch D, supports D, verdicts pending), with quotes HO-12 and HO-13 in quotes-critics.md. The sentence is on PDF p.8; the model description starts on p.7.

## Patterns seen in the genealogy (for the renderer's captions; descriptive, not verdicts)

- **Fixation probability, Day's line:** 1/(2Nₑ) from 2026-01-29 (`L-nne-2026-01`, `L-day-k-nne-blog-2026`), shared within the week by keruru (`L-keruru-nne-2026`), "an assumption imported from Wright–Fisher" (`L-chalub-2026`, 08-23), keruru's retraction (`L-keruru-retraction-2026`, 08-26), Day's concession the next day (`L-day-concession-2026-08-27`) alongside Hard Limits using 1/(2N) (`L-hl-uses-1-over-2n-2026`), the 09-21 post calling P(fix) = x₀ wrong for real populations (`L-errors-hide-2026`), and Relictation's "holds exactly regardless of offspring distribution" (`L-relictation-2026`, 10-06). k ≠ μ values continue separately (0.743 dormant; median 25 → 32.3).
- **Start state, conceded within one post:** `L-ir-empty-2026` (09-22) → `L-mansfield-full-2026` → `L-edu-empty-2026` (10-01 ¶22) → `L-edu-full-short-2026` (10-01 ¶31). Its ancestor on the critics' side is Camestros's ancestral-polymorphism point (`L-camestros-all-post-split-2026`, 01-25), which resembles CSAC 2005; the audit then credits Day's (T − 4Nₑ)/T for new mutations (`L-audit-b1c-2026`) and the Nₑ,anc = 1e4 half-divergence point (`L-audit-b4a-2026`).
- **Unit errors on both sides:** base pairs counted as fixation events (`L-pz2-410m-2026` → `L-req-205m-2026`, answered by `L-mccarthy-bp-events-2026` and conceded as a variant in `L-snv-only-2026`), and divergence-including-polymorphism matched to a neutral fixation count (`L-hancock-38m-2026`, `L-nesslig-37.8m-2026` → `L-audit-double-count-2026`).
- **Serial vs parallel, from 1966:** `L-wistar-ulam-1966` and Mayr's "Couldn't they all go on simultaneously?" (`L-wistar-mayr-1966`) resemble the 2019–2026 exchange (`L-mittens-2019`, `L-camestros-reads-serial-2026`, `L-mccarthy-parallel-2026`, `L-myers-parallel-2026`, `L-hancock-serial-2026`). On Day's side three descriptions coexist: parallel (`L-3-0-parallel-2026`, 09-28), all-sequential in Ara+2 (`L-ara2-sequential-2026`, 10-01) and Appendix A "must be sequential" (`L-appendixA-sequential-2026`, then `L-worded-better-2026`).
- **CHLCA path is not monotone:** 9 My (2019) → 6–7 My (2025) → 200–580 kya (02-08) → 68 kya (02-14, later disowned) → 250 kya–1.3 Mya (05-07) → 6.3 My again in MITTENS 3.0 (09-28) with no reconciling text.
- **Fast self-correction on G_f:** 1,600 (2019) → 1,400 (book) → 1,322 (09-28) → strict counts "including an earlier draft of our own" (10-02), four days after the critics' −906 post.
- **The audit's own descent:** 7.7× → 17.1×; "literal 1/300 falsified" → "10% is not a general bound"; "soft within 15% of hard" withdrawn; "does not rescue Day" withdrawn → "cannot adjudicate". These corrections moved in both directions (some toward Day, some toward the critics).

