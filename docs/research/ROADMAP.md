# Roadmap: everything outstanding

*Written 2026-10-12 at the owner's request ("plans or roadmap for the other suggestions and things tbd"). One table per area; each row is one open item with its source, status, blocker, next step, who acts and a rough cost. No dates: order and dependencies only. Sources of truth are linked in each section; when a row and its source disagree, the source wins and this file is wrong.*

<p align="center"><img src="../img/audit-roadmap.svg" alt="Roadmap: four lanes (compute and checks, criticality remediation, owner decisions, outside inputs) feeding the R5 draft, a criticality pass on it, the research-phase exit and the simulator phase" width="900"></p>

**Status vocabulary.** `running` = a job is executing now. `queued` = specified and pre-registered (or ready to be), waiting on a named predecessor. `proposal` = written up in [`criticality/METHOD-AUDIT-proposals.md`](criticality/METHOD-AUDIT-proposals.md), held back, not applied. `needs owner` = only the owner can act. `tbd` = no spec, owner or blocker yet. `done` = shown only where an owner decision is recorded as applied.

**Who.** *owner* = Nick; *agent* = a Claude instance in the project's session; *outside* = a person or party not yet approached (nothing has been sent to anyone: hard rule 6). **Cost** is a rough guide: *tokens* = agent time (S/M/L), *CPU-h* = compute (free per the owner; tokens are the scarce resource), *owner min* = owner time.

**Where the plan sits.** Stages and exit criteria: [`PLAN.md`](PLAN.md). Method audit findings and their status: [`criticality/README.md`](criticality/README.md). Owner decisions: [`DECISIONS.md`](DECISIONS.md). Queue detail: [`research/checks/QUEUE.md`](../../research/checks/QUEUE.md).

---

## A. Compute and checks, in flight or queued

Source: `QUEUE.md`. Everything below is launched from na-workhorse or builder, never the workstation. Load-bearing checks get three reviews; low-stakes one combined review (AGENTS.md).

| id | Item | Source | Status | Blocker | Next step | Who | Cost |
|---|---|---|---|---|---|---|---|
| A1 | HF post hoc run `ph` (cap release, long burn, mix boundary, noisy truncation; 83 cells, 410 jobs). A host reboot lost shard `wh`; relaunched | QUEUE item 8 | running | CPU time (about 94 CPU-h left at the 2026-10-12 13:44 note) | Check once when due; merge on workhorse (`missing 0, extra 0, mismatches 0`); analyse; score against the docstring; fill the "pending post hoc" items; one combined review; integrate | agent | 94 CPU-h; tokens M |
| A2 | L1b: T2T rerun of the dN/dS check (L1). Closes MA-12 when it reports | QUEUE later queue; MA-12 | queued | Launch after A1 | Launch the pre-registered `l1b_t2t_dnds.py`; collect; write up; three reviews | agent | CPU-h tens; tokens L |
| A3 | L1c: alignment method versus dN/dS ("protein-guided alignment gaps out divergent codons", Q180-Q186) | QUEUE later queue | queued | A1 and A2 (reads L1b's segment dump) | Launch after L1b; write up; three reviews | agent | CPU-h tens; tokens L |
| A4 | FMnull: neutral-null calibration of Day's "more than 80 times more variable" (FM3, Q164; FM10 premise) | QUEUE later queue (L4, mechanistic form) | queued | Launch after A1 | Launch pre-registered `fm_mesa_null.py`; write up; three reviews (load-bearing) | agent | CPU-h tens; tokens L |
| A5 | L5: aDNA zero-fixation power analysis (Day's statistics, four Holocene trajectories, three models) | QUEUE later queue; D-16 | queued | Launch after A1 | Launch pre-registered `l5_adna_power.py`; write up; one combined review (owner, D-16) | agent | CPU-h tens; tokens M |
| A6 | Q93 closeness re-test ("In any population over 10,000, neutral substitution will not fixate at all.") under the C7 standard and the 4N_e window; all readings, 3x band | QUEUE item 15 | queued | Pre-register first | Write and commit the script with predictions; run; one combined review | agent | trivial CPU; tokens S-M |
| A7 | Census-size source fetch. Named in the owner's brief; **no QUEUE entry or spec found** | brief 2026-10-12 | tbd | No spec | Owner or agent to say what is wanted (likely census N versus N_e inputs for B3, C7 and A6); then add to QUEUE | owner, then agent | tokens S |
| A8 | C1d follow-ups: transversion-restricted, SFS-matched neutral model; what the transition excess is | QUEUE next 5 | queued | Pre-registration; Holocene N_e not decided by the literature | Specify and pre-register | agent | CPU-h small; tokens M |
| A9 | D follow-ups: ProteinGym multi-mutant decay; noise null for the beneficial proxy; per-sequence prevalence (D10-D12) | QUEUE next 6 | queued | Public data fetch; Axe/Taylor full texts paywalled (D4) | Pre-register; run | agent | CPU-h small; tokens M-L |
| A10 | GAP-07 follow-ups: chimp-population polymorphism; a long-read SV set (T2T event counts are done, GAP-07t) | QUEUE next 7 | queued | Data availability | Fetch; pre-register; run | agent | CPU-h small; tokens M |
| A11 | L2: hardness h in humans (viability versus fertility; density dependence). h is the key unsourced H-branch parameter | QUEUE later queue; refresh 10b s6 | tbd | Full texts of Stearns 2010 and Byars 2010 (D4); no decomposition in the abstracts | Owner supplies texts, or agent searches OA cohort data | owner, agent | tokens M |
| A12 | L3: bias-corrected human-chimp alpha from MK with demographic correction | QUEUE later queue | tbd | Polymorphism data; Uricchio 2019 text is now in hand | Spec and pre-register | agent | CPU-h small; tokens M |
| A13 | L4: FM overdispersion against a heterogeneity-aware null; pending Day's code or window size (FM10) | QUEUE later queue | tbd | Day's method not released; A4 is the mechanistic form | Wait on A4; revisit if Day releases | outside (Day), agent | tokens M |
| A14 | L-follow-ups: (a) CSAC 2005 text plus an independent ML dN/dS; (b) clade-level HMM states of Good 2017 (SI 5.2 is fetched: F absorbing by design) for E10; (c) Day's per-gene table when released (Q176) | QUEUE later queue; refresh 10b | tbd | (a) needs an ML estimator run; (c) needs Day's release | Pre-register (a); watch for (c) | agent | tokens S-M |
| A15 | E leftovers, GAP-03; XT follow-up (U-scaling rerun or SLiM) | QUEUE next 12; XT | tbd | No spec | Specify or drop (owner call) | owner, agent | tokens M |
| A16 | Sourced human beneficial DFE and M (none exists); H3 stays conditional until then | QUEUE item 8 | tbd | Literature gap | Look for a source; otherwise keep the bracket | agent | tokens S |
| A17 | Integration of HF after A1 (claim files, argmap, board, milestone post) | QUEUE item 8; AGENTS lifecycle step 6 | queued | A1 | One Sonnet agent at a time on shared files | agent | tokens M |
| A18 | Source refresh before each milestone post (HOWTO-refresh); material after 2026-10-12 is logged, not scored, under O-7 as read | `HOWTO-refresh.md`; O-7 | tbd | O-7 interpretation unconfirmed | Run one before the next post; log only | agent | tokens S |

---

## B. Criticality remediation

Source: [`criticality/README.md`](criticality/README.md) findings table and [`METHOD-AUDIT-proposals.md`](criticality/METHOD-AUDIT-proposals.md). Rule and vocabulary changes follow the rule-freeze procedure (O-6): written proposal naming the verdicts it moves, 24-hour cooling-off, three-review re-score of each load-bearing verdict moved, then a new rule revision. Findings whose blocker is an owner decision (MA-01, MA-03, MA-09, MA-10, MA-19) are carried in sections C and D and not repeated here. Triveritas-added items are B18 to B20.

| id | Item | Source | Status | Blocker | Next step | Who | Cost |
|---|---|---|---|---|---|---|---|
| B1 | Proposal (a): `unexamined` for `holds` nobody checked (6, 24, 36 or 58 internal `holds` move, by definition chosen) | MA-07 | proposal | Owner go-ahead (C10); rule-freeze | On go-ahead, apply with lint rule; re-score any load-bearing node moved | agent | tokens M |
| B2 | Proposal (b): `external_basis` field (data, literature, model); 52 decided external verdicts coded 16 data, 10 literature, 26 model (one coder, same model) | MA-05 | proposal | Owner go-ahead (C10) | Apply; second coder if an outside reader exists (D2) | agent | tokens M |
| B3 | Proposal (c): split `contested` four ways (all 114 re-coded; trial classification in the file) | MA-08 | proposal | Owner go-ahead (C10) | Apply; recount tallies | agent | tokens M-L |
| B4 | Proposal (d): RH6 revision (up to 7 RH tags re-decided; B, B9, C7 may move) | MA-02 | proposal | Owner decision; three-review re-score | Decide; re-score B, B9, C7 | owner, agent | tokens L |
| B5 | Proposal (e): ROOT aggregation rule and stopping rule (governs R5; moves no verdict) | MA-11 | proposal | O-7 interpretation; draft ahead of R5 | Confirm O-7; adopt before R5 draft | owner, agent | tokens S |
| B6 | Proposal (f): seeded-error test and blind re-derivation on five checks (D15, A2e, HF and others) | MA-01 | proposal | Planter and blind re-deriver should not be the integrating instance; ideally non-Claude (D3) | Run with the non-Claude seat, else same-model with that disclosed | agent, outside | tokens L |
| B7 | Stale "most charitable to Day" comments in C7 and B9; revert or re-review of B and A2e (O-5) | MA-03 | needs owner | O-5 (C5) | After O-5, fix the comments (no-decision fix) | agent | tokens S |
| B8 | Forward pre-registration rule (pushed timestamps, partitioning bands) not adopted | MA-04 | tbd | Owner choice | Decide whether to adopt for new checks | owner | owner min |
| B9 | MA-12 closure: DN1-DN3 verdicts are conditional on L1b | MA-12 | queued | A2 | Re-state verdicts when L1b reports | agent | tokens S |
| B10 | MA-13 mirror tree (one decomposition from the first summary pass) | MA-13 | tbd | No action yet | Decide whether to build a critic-drawn decomposition | agent | tokens L |
| B11 | MA-14 the 25% materiality line was set in the gap of observed slips | MA-14 | tbd | None | Sensitivity statement or leave disclosed | agent | tokens S |
| B12 | MA-15 category leaks (`side: audit` unspecified; A4 internal outside vocabulary passes lint) | MA-15 | tbd | None | Specify and tighten lint (a vocabulary change: follow O-6) | agent | tokens S |
| B13 | MA-16 from "the simulation shows" to hominids | MA-16 | tbd | Disclosed only | Add scoped wording where used | agent | tokens S |
| B14 | MA-17 presentation manufactures symmetry (partly touched by O-8) | MA-17 | tbd | None | Re-read front pages for symmetry cues | agent | tokens S |
| B15 | MA-18 budget decides depth (no mechanical tier test) | MA-18 | tbd | None | Specify a mechanical tier test | agent | tokens S |
| B16 | MA-19 residual: one-command quote verification not built | MA-19 | tbd | None | Build a script that checks every quote against saved text | agent | tokens M |
| B17 | MA-20 documents disagree with practice: residual items (README status table, totals off by one) not re-checked | MA-20 | tbd | None | Re-check after the next count refresh | agent | tokens S |
| B18 | Triveritas no-decision fixes: clause-provenance table for the verdict rule (TV-02); flip-value notes for the load-bearing verdicts where write-ups already have the numbers (TV-05); `versions.md` rows for the four Triveritas versions on evolution and `veriphysics.substack.com` on the refresh watch list (TV-09). Done by that pass: bibliography rows for the ten papers corrected | `triveritas-audit-2026-10-12.md` 7.2 | tbd | None; change no rule, vocabulary or verdict | Do at once, naming the TV ids in the commit | agent | tokens M |
| B19 | Triveritas proposals, held back: hold-out test of the frozen rule (TV-02); prediction and failure-threshold paragraphs for proposal f and the right-of-reply protocol (TV-03); conjunction flag per node, so the headline reads 14 of 233 not 131 `holds` (TV-06); `quantitative` field per claim (TV-07); `as_of` date per verdict (TV-10); a claim node for Day's Triveritas verdict on evolution (TV-09). Counts for the `quantitative` field not yet taken | `triveritas-audit-2026-10-12.md` 7.1, 7.2 | proposal | Rule-freeze procedure (C6); specify each with the counts it moves | Write specs in the proposals file before any is applied | agent | tokens L |
| B20 | Triveritas findings TV-01 to TV-11 (2 CRITICAL, 6 MAJOR, 1 MINOR to MAJOR, 2 MINOR); concordance with MA: agrees 11, in part 3, partly disagrees 3, not covered 6. TV-01 repeats MA-01; TV-11 (the application is itself not independent) stands until a rater outside this model family scores the audit | `triveritas-audit-2026-10-12.md` 5, 6 | needs owner | Outside rater (C4, C14, D3) | Register TV ids in the criticality README table; closure only by re-audit | owner, outside | tokens S |
| B21 | Closure by re-audit: no finding is closed in the sense of "re-audited and confirmed fixed" (0 of 20 MA, 0 of 11 TV) | criticality README | tbd | A pass by a reviewer who did not do the integration | Run a fresh pass when remediation is applied | agent, outside | tokens L |
| B22 | Record in the audit file any named outside reviewer (none recorded yet) | criticality README | tbd | D1-D3 | Record by name and role when one exists | agent | tokens S |
---

## C. Owner decisions O-1 to O-9 and related

Source: [`DECISIONS.md`](DECISIONS.md), "Owner replies to O-1 to O-9" (the owner's words, 2026-10-12: "where buy pdf of prob zero? 1-4 we can get moving. 5 i dont get. 6-7 seem poltical an dits fine. 8 is fine? why? and 9 seems fine"). Status is the recorded state, not a guess.

| id | Item | Source | Status | Blocker | Next step | Who | Cost |
|---|---|---|---|---|---|---|---|
| C1 | O-1 buy *Probability Zero* and supply the text. Listings in `sources/bib-day.md` (grep `K-PZ`): Kindle ASIN B0GF8RQFY4; hardcover and signed edition listed sold out on 2026-10-07; **no PDF or DRM-free edition recorded**; no DRM bypass | MA-09; O-1 | needs owner | Purchase; **how the text is supplied** (legitimate export, scan of own copy, typed excerpts) | Owner buys and says how to supply; `secondhand` nodes are then re-sourced | owner | owner min; tokens M |
| C2 | O-2 right of reply to Day and each named critic (drafts exist; 21-day window suggested) | MA-10; `outreach/right-of-reply-*.md` | needs owner | Approval of exact text and **channel** per recipient; no contact channel recorded for Day; lifts hard rule 6 for this purpose only | Owner edits and approves, then sends or says who sends | owner | owner min |
| C3 | O-3 recruit a human population geneticist and one reader per camp | MA-01, MA-10; `outreach/reviewer-brief.md` | needs owner | Owner approves the brief; someone to approach | Owner picks and sends | owner | owner min |
| C4 | O-4 non-Claude review seat (packet drafted; seeded draw D15, A2e, HF) | MA-01; `outreach/non-claude-review-packet.md` | needs owner | No non-Claude model is installed here; owner must run the packet or give access | Owner runs or provides access | owner | owner min; tokens S |
| C5 | O-5 revert B (internal) and A2e (external) to `pending` or their pre-2026-10-11 values, or re-review. **Owner said he did not understand the question; an explanation was asked for** | MA-03 | needs owner | Explanation delivered; decision not made; B and A2e keep current values | Owner decides after reading the plain-language explanation | owner | owner min |
| C6 | O-6 verdict-rule freeze (rev 3) and 24-hour cooling-off. Accepted ("fine"). Interpretation (recorded for correction): the freeze starts once proposals a-c are applied or declined | MA-03, MA-10 | needs owner | Owner to confirm the reading | Confirm or correct the reading in `DECISIONS.md` | owner | owner min |
| C7 | O-7 corpus freeze at 2026-10-12, later material logged but not scored until R5 is drafted (except replies under C2 and releases a registered check awaits). Accepted; interpretation to confirm | MA-11 | needs owner | Owner to confirm the reading | Confirm or correct | owner | owner min |
| C8 | O-8 drop comparative error rates and Fisher p-values from public pages | MA-06 | done | None. Applied 2026-10-12 (`8b6f95b`); owner asked "why?", answered in `DECISIONS.md` | Revert with `git revert` if the owner wishes | owner | none |
| C9 | O-9 LICENSE and conflict-of-interest statement. Accepted in principle | MA-19; `outreach/coi-and-licence-draft.md` | needs owner | **Licence choice** and **COI facts** (who pays, relation to either camp, the project icon) in the owner's own words; no LICENSE file yet | Owner supplies both; agent adds LICENSE and fills the "Interests" paragraph | owner | owner min |
| C10 | Go-ahead for proposals (a), (b), (c) (the content of rule rev 3) | O-6; proposals file | needs owner | Owner go-ahead; C6 reading | Owner says apply, decline or amend each | owner | owner min |
| C11 | Confirm the proposed R5 exit criterion: no CRITICAL finding open, every MAJOR closed or accepted by the owner | PLAN.md l.229 | needs owner | Owner confirmation | Confirm, amend or reject | owner | owner min |
| C12 | Whether "Claude Athos" (the AI co-author credited on Day's Triveritas papers and in the audit's own same-family disclosure) is a separate recipient of the right of reply, or addressed only through Day | owner's brief; `METHODS-AND-LIMITATIONS.md` | tbd | No recorded decision; the draft letters name Day and critics only | Owner decides; agent adds or omits a draft | owner | owner min |
| C13 | Q157/Q158 RH tags and the four unclear tags (B9, C7, ROOT, ROOT-M) left for the owner in the RH pass; may be superseded by proposal (d) | QUEUE next 13; slips ledger | needs owner | Owner tagging or the RH6 revision (B4) | Decide, or fold into B4 | owner | owner min |

| C14 | O-10 (proposed by the Triveritas pass; **not yet in `DECISIONS.md`**): send the Triveritas packet to non-Claude raters (named in the pass: Grok, Gemini) under its rater rules (composing model excluded, one family per leg, human blind first). Same authorisation as O-4 with a second packet | TV-01, TV-11 | needs owner | Owner approval; no packet text exists beyond the pass's section 7 | Owner approves; agent adds the entry to `DECISIONS.md` and drafts the packet | owner | owner min; tokens M |
| C15 | O-11 (proposed, not yet recorded): include the Triveritas result in the right-of-reply letter to Day and invite him to score the audit with his own tool. Needs hard rule 6 lifted as for C2 | TV-11 | needs owner | C2 | Owner decides with C2 | owner | owner min |
| C16 | O-12 (proposed, not yet recorded): keep the Triveritas as a standing lens of the criticality layer (re-run at each pass, by an outside rater when one exists) or treat it as a one-off | TV pass 7.2 | needs owner | Owner choice | Decide; if standing, add to the standing procedure | owner | owner min |
---

## D. Outside inputs

Nothing here has been requested. Each item needs a prior owner approval in section C.

| id | Item | Source | Status | Blocker | Next step | Who | Cost |
|---|---|---|---|---|---|---|---|
| D1 | Human population geneticist on the five checks that carry the most: B3/B7 (k = mu), B4a (ancestral polymorphism), H8/HF (cost of selection), A2e, GAP-07 counts | O-3; MA-01 | tbd | C3 | Recruit; their view recorded in a separate section of the audit file | outside | owner min; their time |
| D2 | One reader from each camp as adversarial collaborators on the rule text and load-bearing list; disagreement recorded, not resolved by the owner | O-3; MA-10 | tbd | C3 | Recruit | outside | their time |
| D3 | Non-Claude model for one review seat on load-bearing checks (also runs B6, and the Triveritas packet if C14 is approved) | O-4; MA-01 | tbd | C4 | Run packet; record family and version | owner, outside | tokens S |
| D4 | Paywalled or blocked full texts for the owner to supply: Bakewell 2007 (PNAS); Byars 2010 (PNAS, free); Stearns 2010 (Nat Rev Genet); Eyre-Walker 2006; Huber 2017; Zoonomia 2023 (Science); a sourced noncoding DFE (e.g. a conserved-noncoding DFE paper); an independent genome-wide human-chimp dN/dS; Hodgkinson and Eyre-Walker 2011 (Nat Rev Genet); Hwang and Green 2004 (bot challenge); Axe 2004, Keefe-Szostak 2001, Taylor 2001 (abstracts only). No bypass | `refresh-2026-10-11b-lit.md` "Needs the owner"; `refresh-2026-10-12c-lit.md`; `refresh-2026-10-10b.md` | needs owner | Owner obtains legitimate copies | Owner supplies files into a new `sources/raw/` directory (gitignored) | owner | owner min |
| D5 | Day's replies and releases: right-of-reply answer; FM10 method and window size; per-gene table (Q176); any code | C2; A13; A14 | tbd | C2; Day's choice | Watch the refresh log; score only what O-7 allows | outside | none |
| D6 | Critics' replies (McCarthy, Mansfield, Hancock and others) | C2 | tbd | C2 | As D5 | outside | none |

---

## E. Path to R5 and the simulator phase

Exit criteria (from `PLAN.md` "Exit the research phase when"): every load-bearing claim has a reviewed check and three verdicts; every critic and ally argument is mapped; the gap list is closed or recorded as inaccessible; the variable list is final; and, proposed, a criticality pass on the R5 draft with no CRITICAL finding open and every MAJOR closed or owner-accepted. Branches may graduate independently.

1. **Finish and integrate the compute in A** (A1 first; then A2 to A6 as they launch). Exit: each load-bearing node has a reviewed check; HF verdicts integrated.
2. **Owner decisions that unblock the rest** (C5, C6, C7, C10, C11; C1 and C9 in parallel). Exit: each recorded in `DECISIONS.md` with the owner's words.
3. **Apply proposals a-c, and d if chosen, under the rule freeze** (B1-B4): cooling-off, three-review re-score of every load-bearing verdict moved, new rule revision.
4. **Outside seats, if approved** (C2-C4, D1-D3): send; record replies verbatim; run B6.
5. **Close or accept every CRITICAL and MAJOR finding** (section B and the five owner-blocked ones). Exit: the register in `criticality/README.md` shows none open, or the owner's acceptance in `DECISIONS.md`.
6. **Draft R5** (`R5-draft.md`): verdicts per branch, balance ledger, sensitivity table that becomes the simulator variable list (N, N_e, mu, L, s distribution, dominance, recombination, generation time, start state, demography, T, divergence-counting rule, mutator alleles), using the ROOT aggregation and stopping rule (B5).
7. **Criticality pass on the R5 draft**, by a reviewer who did not integrate it, with its findings kept in their own section (and the Triveritas critique re-run on the R5 text). Exit: criterion in step 5 met on the draft.
8. **Exit the research phase, then the simulator phase:** brainstorming, spec, plan. No simulator code before step 7 (AGENTS.md).

---

## Counts

Rows by section and status (counted from the tables above on 2026-10-12; section E is a sequence, not rows).

| Section | Rows | running | queued | proposal | needs owner | tbd | done |
|---|---|---|---|---|---|---|---|
| A | 18 | 1 | 9 | 0 | 0 | 8 | 0 |
| B | 22 | 0 | 1 | 7 | 2 | 12 | 0 |
| C | 16 | 0 | 0 | 0 | 14 | 1 | 1 |
| D | 6 | 0 | 0 | 0 | 1 | 5 | 0 |
| **All** | **62** | 1 | 10 | 7 | 17 | 26 | 1 |

Needs-owner rows (17): B7, B20, C1, C2, C3, C4, C5, C6, C7, C9, C10, C11, C13, C14, C15, C16, D4.
