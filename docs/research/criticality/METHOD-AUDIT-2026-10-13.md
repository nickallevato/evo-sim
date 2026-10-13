# Method audit, 2026-10-13: the batch of 2026-10-13 (HF `ph`, L1b, L1c, FMnull, L5)

**Status of this document, read first.** The reviewer is a fresh instance of the same model (Claude Opus) that did the work, launched from inside the project's session with `AGENTS.md` loaded and briefed by the lead. It is **not blind** (the brief listed the process facts the lead already thought were weak, and this file follows that list), it took no part in the checks, and it is **not the integrator**. Finding MA-01 applies to it in full. It is criticality pass vii, required by the standing procedure before the next milestone post.

*Scope: commits `d0d8493..cb5ed16` on branch `research` (about 60 commits, all dated 2026-10-13, plus the registrations of 2026-10-11 and 10-12 they rest on). Method: commit and push times (`git log`, the local reflog of `origin/research`), the host records `research/checks/results/raw/*.host`, script md5s recomputed from git blobs, the five write-ups read by section (bands, prediction tables, verdict proposals, "Who this helps", "Review resolution"), review headers, the claim-file diffs of the four integration commits, and three quotes checked against the held texts. No check was re-run and no number in a write-up was re-derived. Counts marked "measured" are mine. No claim file, write-up, script, queue or argmap file was edited.*

---

## Executive summary

**Sound.**
- **Registration order holds for all four new checks.** Every script and the pre-run note reached `origin/research` before its launch, by the reflog and the host records, and the md5 in each host record equals the md5 of the git blob it names (10 of 10 recomputed). Post hoc scripts are labelled post hoc in their commit subjects and each was pushed before its run.
- **The reviews found real errors, in both directions, including the lead's.** The lead's V3 bias direction was reversed by review; two figures in the audit's own claim text were found wrong by two orders; a credit to Day was withdrawn; a Day clause the lead's draft had dropped was restored.
- **No verdict was moved on a weak test.** L5's registered flip against Day was withheld; FMnull proposes no move and says first that its observed outcome is the weakly tested one; L1b refused to narrow or to broaden its registered sentence after the result.
- **The audit's own errors are in the claim files**, under "Both" or "Against the audit", not only in the write-ups.
- **Rulings on steelman conflicts show no tilt by side**: of 24 conflicts, 5 went to Day's reviewer, 5 to the critics', 14 were split (table in section 2).
- Q272 to Q274 are verbatim at the stated locators.

**Not sound.**
- **One instance is author, briefer and judge (MA-21).** The lead wrote the `ph` scoring, the pre-run notes, both launch fixes and every ruling between the steelman reviews, and briefed each reviewer with its own suspicions. The briefs are not in the repository. The rulings reached the claim files 4 to 8 minutes after each fix pass was committed, read by nobody but the integrator.
- **Four verdict fields were set by an undefined test (MA-22).** Which reading is "extended" (and so cannot set a field) decided DN1, DN6 external, DN6 fidelity and C external. The rule gives no operational test; the lead applied one case by case. The outcomes do not lean one way (two harsher for Day, three milder, one milder for a critic claim), but they are not reproducible from the rule text.
- **L5 had one review although it carried a registered verdict flip (MA-23)**, and the lead's own pre-run note said the flip "stays a proposal for the three reviews".
- **Day-side outcomes were unreachable in parts of three of the four new checks (MA-24)**, one day after the severe-testing pass named the defect. "No verdict moved toward Day" cannot be read as "Day's side was tested and lost" for those parts.
- Smaller: the `blind` label overstates L1c, FMnull and L5; `ph` has no pre-registration row and its push is not shown to precede its launch; one agent wrote both L1c steelmen; the two-subagent cap was exceeded without a recorded decision; two small drifts in claim files.

**Counts.** 10 findings, MA-21 to MA-30: CRITICAL 0, MAJOR 4, MINOR 5, COSMETIC 1. MA-01 (CRITICAL, 2026-10-12) stands and this batch is a further instance of it.

---

## 1. Pre-registration integrity

Times are -06:00. "Pushed" is the first reflog entry of `origin/research` containing the commit (local reflog: evidence of a push, not an outside timestamp).

| Run | Registered or amended (pushed) | Launch (host record) | Lead | Result commit | md5 in host record = git blob |
|---|---|---|---|---|---|
| L1b main | script `0fe3c7f` 10-11 20:06; pre-run note `5e64f0a` pushed 10-13 10:52:25 | 10:53:21 | 56 s | `c168b65` 10:59 | yes (`aef21cb3`) |
| L1c main + transfer | `536b19b` 10-12 11:58; amended pre-run `0e0e840` 10-12 15:07 | 10:59:22 | 19 h 52 min | `90b32ba` 11:21; transfer `9d61b8a` 11:34 | yes (`2692334e`) |
| FMnull chain | `48241c7` 10-12 12:16; amended pre-run `cc5e6dd`, `408ba53` (15:18:53) | 11:06:42 | 19 h 48 min | `29245a8` 11:30 | yes (`0b25eaf7`) |
| L5 main | `0e6da82` 10-11 20:28; note `5e64f0a`; launch fixes `369354d` 10:56:10, `30e1302` 11:00:31 | 11:02:33 (queued behind L1c) | 2 min | `f99d925` 12:17 | yes (`89607a4b`) |
| HF `ph` | `5c30ed9` committed 10-11 11:44:14; first push containing it 11:53:58 (`f6933d6`) | "11:53" | not shown | `13820e5` 10-13 10:52 | yes (`5f571634`) |
| L1b X1 breakdown (post hoc) | `9c4a359` 11:27:28 | 11:27:38 | 10 s | in fix pass `098ac12` | yes |
| L1c `transfer-excl` (post hoc) | `6c5d8cf` 12:06:09 | 12:06:17 | 8 s | `40e4021` 12:23 | yes (`c61c39ba`) |
| FMnull `simphase` (post hoc) | `57f2834` 12:16:13 | 12:16:22 | 9 s | `fee27c3` 12:21 | yes (`2f993ddc`) |
| FMnull `p45fix` (post hoc) | `3d508ef` 12:17:14 | no host record (local, 1.1 s) | not shown | `70eb15b` 12:17:30 | n/a |
| L5 `l5_posthoc_v3` (post hoc) | `c9f3d69` 12:49:14 | workstation, 50 s | at most 110 s | `10dfbcb` 12:51 | n/a |

**Answers.**
- *Committed and pushed before launch?* Yes for L1b, L1c, FMnull, L5 and four of the five post hoc runs. Not shown for `ph` (push at 11:53:58 against a launch recorded to the minute as 11:53; the host record also places the smoke at "~11:42 ... after the 5c30ed9 commit", two minutes before that commit's timestamp) and for `p45fix` (16 s between script commit and output commit, no host record).
- *Are the post hoc labels right?* Yes. Each launch fix and each analysis script says "post hoc" in the subject, and the two L5 fixes say "pre-run, no task result seen".
- *Could a result have influenced them?* **L5 launch fixes: no route found.** `l5_launch1_failed.out` ends in a pickling error before any task; `l5_launch2_failed.out` ends at the first binomial draw of one task; both show only the seeded selftest lines. The fixes touch dispatch and a clamp at x = 1. What the lead did see was the selftest V3 miss, and it then wrote a reading of it into the pre-run note that was wrong in direction (MA-27). **`p45fix`, `fixpass`, X1 breakdown, `l5_posthoc_v3`: yes by construction**, since each reproduces numbers a reviewer had already computed; all four are labelled descriptive and none scores a prediction. **`simphase`** carried predictions in its docstring and overturned a registered hit (P8 (ii)); **`transfer-excl`** disclosed a 30-gene smoke seen before its commit.
- *`PREREG-STATUS.md`.* Regenerated to scratch with `research/tools/prereg_status.py` (not committed: the file is outside this pass's write scope). Result: **L1b `blind`, L1c `blind`, FMnull `blind`, L5 `blind`; HF `ph` has no row** (the tool lists one row per main script; post hoc scripts are excluded by its limit 4). Counts move from blind 10 / registered-not-run 4 to **blind 14 / registered-not-run 0** (total 61). The committed file is stale.

The `blind` label is the tool's and it reads only the first commit of each script. See MA-25 for what it misses.

## 2. Symmetry of treatment

### 2.1 Rulings on conflicts between the steelman reviews (measured from each "Review resolution")

| Check | Conflict | Day reviewer asked | Critic reviewer asked | Ruling | To |
|---|---|---|---|---|---|
| L1b | Registered CRITIC sentence | qualified wording wherever it appears (D3) | no post hoc narrowing (K1) | kept as registered; not broadened either | critic |
| L1b | Where X1 (0.853) is credited | (draft had it under Day) | under Critics (K2) | under "Both", both halves | split |
| L1b | DN1 readings | Readings table; "conditional on L1c" in the field (D1) | A is the reading | table added; field wording not changed | Day in part |
| L1b | Left-out codons | report and bound them (D3) | | reported, 0.56 to 0.85 | Day |
| L1b | R1 label on the gene-set credit | keep "material" (D4) | "not material" on T2T (K6) | no label either way | split |
| L1c | DN6 external field | b2 `contested`, not strengthened | b1 `contradicted` may set it (K1) | b2 sets it; b1 recorded | Day |
| L1c | DN6 fidelity | two readings, broad `partial` (D8) | `misread`, stated first (K2) | `misread`; broad recorded | critic |
| L1c | Cactus as prior filter (reading d) | open for about 10% (D2) | cannot reopen 0.80 (K3) | recorded, extended, "not tested" | split |
| L1c | Clustering regime | open in 2,765 genes (D4) | bounded where 0.23 lives | two halves | split |
| L1c | PAF2 "stress" label | label alone decides Reading A (D3) | adversarial by registration | both stated; dose-response not run | split |
| L1c | Transfer hit | equal weight | not a prediction (K5) | hit, labelled not blind | split |
| L1c | Register loss as source of 0.80 | "which input is right" (D7) | undersold (K4) | own section; "candidate error class" | split |
| FMnull | F0 cells (D3a / K5) | count them | projection artefact | neither side, counted separately | split |
| FMnull | φ_HC above bound at F0 (D6a / K5) | Day point | projection effect | projection effect | critic |
| FMnull | φ_HC above bound at F2 (D6a / K10) | exceeds bound | lambda_M 0.04 to 0.07 absorbs it | both, always together | split |
| FMnull | Power (D2 / K6, K13) | little power below dominant | data bound the mechanism | both ways, one section | split |
| FMnull | Gate scope, small-W class (D5 / K7) | UNTESTED, conditional | extended, not a Day point | scoping accepted, conditional once, neutral | split |
| FMnull | R2 and P3 (D4 / K8) | units both ways | class of a number | under "Both" | split |
| FMnull | Criteria wording (D6b / K6) | none could fire | data bound | reworded to the simulations | split |
| L5 | Unreachable DAY band (K3) | limit on Day's side | registration defect only | limit stays on Day's side | Day |
| L5 | "Weakly tested" as a Day point (K1) | | remove | removed | critic |
| L5 | Is R-c the audit's construction (K5) | | drop R-c, flip | R-c kept, no flip | Day |
| L5 | C1 to `contested` for selection-driven completions (D5 i) | log for the owner | | readings recorded, field unchanged | critic |
| L5 | The word `contradicted` under R-a, R-b (D6) | wrong word | registered word | kept in the table, not in the field | split |

**Tally: 24 conflicts; Day 5, critic 5, split 14.** HF `ph` had no steelman conflict to rule on. No systematic tilt.

**MAJOR findings by side, as answered (measured).** Day-side MAJORs 17: accepted in full 9, in part 8, rejected 0. Critic-side MAJORs 15: accepted in full 11, in part 4, rejected 0. The gap (53% against 73% in full) is small in count and the parts refused on Day's side are mostly requests to change registered wording or a field after the result (L1b D1, D3) or to run a new arm (L1c D3). It is recorded, not tested; MA-06 applies to any rate drawn from it.

### 2.2 Registered predictions hit and missed (from the write-ups' own tables)

| Check | "Day side" | "Critic side" | Audit's own |
|---|---|---|---|
| HF `ph` (all post hoc, after `hf_main` was seen) | 1 of 4 | 3 of 3 (one on a 4-of-8 tie) | 10 of 15 |
| L1b | 1 of 5 | 6 of 6 | 11 of 12 parts, plus carry-over 3 of 3 |
| L1c | 4 of 14 (1 of the 4 not blind; 1 of the 14 scored "empty", 9 misses) | 14 of 15; 4 more fail on the invalid registered arm | 12 hits, 5 misses, 1 split |
| FMnull | none scored: the "sides" in P1 to P8 are audit gloss (rule S) | none scored | P1, P2, P3, P6 hit; P7 two parts hit, one reading-dependent; P8 one miss, one hit only on the grid, one hit; P4, P5 no credit |
| L5 | band 0 of 1 | band 1 of 1 | 2 of 8 in full, 6 missed in part |
| **Sum** | **6 of 24** | **24 of 25** | |

**What these counts can be used for.** (i) A record that the audit's own predictions failed in both directions (X1 at 0.853 and L5's P4, P5 toward Day; L5's P3b, P7b and `ph` PN3 toward the critics), which is evidence the runs were not steered to an expected answer. (ii) Input to the severity question of section 3.

**What they cannot be used for.** Any statement about Day's or the critics' accuracy. Every "Day side" and "critic side" prediction was written by the audit, not by Day or a critic. L1b's critic bands were written with L1's 0.271 and 0.207 in hand. Rows are not independent. Day's own later post contradicts one of "his" L1b hits. L1b and FMnull say this in the text; L1c, L5 and `ph` do not say it beside their tallies (MA-29). Under MA-06 and O-8 none of these ratios belongs on a public page.

## 3. Outcome pattern

Three bands are CRITIC (L1b, L1c, L5). FMnull has no band: "Neither clause is met. No verdict move is proposed." `ph` has none. No verdict value moved toward Day; one moved off `pending` against him (DN6 fidelity `misread`) and one to the middle (DN6 external `contested`).

| Check | Day-side outcome reachable? | How the batch handled it | Scoped to what was tested? |
|---|---|---|---|
| L1b (ST-08) | **Yes.** DAY and DAY-VALUE needed 0.65 on his named assemblies; L1 on hg38 made that unlikely, not impossible. LOCATED missed by 5.9 points of share | Two unclassified regions assigned before launch, the larger "most favourable to him"; pushed 56 s before launch | Yes: "this alignment", annotation and estimator named; GENCODE v46 (his stated annotation) still open |
| L1c | **Partly.** DAY band reachable in principle (the synthetic cells show the mechanism can be large). But the amended Reading A could only give `supported` or `contested`, the registered one only `supported`, and the amended "x <= 3" clause could not be met even in the cell built for it | Disclosed under "Against the audit"; DN6 not to be strengthened past `contested` without an external aligner | Yes, three scope qualifiers on every sentence |
| FMnull (ST-10) | **Only for a dominant mechanism at 100 kb on masked sequence.** S2 could not be met by any planted model off the window grid; S3 untestable; S4 not run | Severity limit is section 1 of the write-up; power stated both ways (6a); S2 recorded as a defect on Day's side; tree-incongruence (ST-10's remedy asked for it first) **not measured** | Yes; no defeater against FM10 licensed |
| L5 (ST-09) | **No at s <= 0.01** (the registered arithmetic excludes it); yes at s >= 0.03 | Pre-run note items 1 to 5 before launch; flip withheld | Yes in the write-up; one drift in the claim file (MA-28) |
| HF `ph` | n/a (post hoc by its own docstring) | Marginal calls marked marginal | Yes after the fix pass |

So: ST-08 was closed before launch as its remedy asked. ST-09 was answered before launch and its consequence (a weak test moves nothing) was honoured. ST-10 was answered in the write-up except for the tree-incongruence statistic, and the "not discriminating" ratio (band width above 9) was chosen in the fix pass, after the results. Finding MA-24 records what remains.

## 4. Verdict moves, withheld and applied

| Move | Rule text | Consistent? |
|---|---|---|
| **L5: C external `contested` to `contradicted` withheld** | RD: the field takes the reading under which the quoted statement is most defensible; extended readings cannot set it. The source states no s (Q275 to Q278 checked against the held text for the comparator sentence) | **Yes**, and the weak-test reason was written before launch (pre-run note item 5). It departs from the registered move, in Day's favour. `contradicted` (scoped) is recorded under R-a and R-b |
| **DN6 external `pending` to `contested`** | RD; registered move sentence "CRITIC with flag small/moderate -> contested" | **Yes** by the four textual grounds in the write-up. The stricter reading b1 (`contradicted`) is recorded. DN6 is `load_bearing: false`, so the 24-hour cooling-off of O-6 does not bind; it was integrated 8 minutes after the fix pass |
| **DN6 fidelity `pending` to `misread`** | Fidelity `misread`: "the cited source text is in hand and contradicts the reading" | **Yes** on the strict reading: Q274 says "conserved enough to survive protein alignment" (verbatim, ¶14) and the held CSAC text gives a BLASTZ genome alignment. The broad reading (`partial` / `unverifiable`) is recorded. Under RD's "most defensible" test the broad reading has a case; the write-up rejects it on Q186's own words. Licensed by text held before the run |
| **DN1 to DN3: "conditional on L1b" removed** | Registered CRITIC sentence | **Yes.** `grep` finds no "conditional on L1b" in any DN file. Residue: DN1's comment still carries the superseded sentence "L1b overturns only if ..." after the discharge (MA-28) |
| **DN1 field stays `contradicted` (reading A over B)** | RD, extended readings | Arguable both ways, as the write-up itself says ("the choice is the owner's"); integrated as A with no recorded decision (MA-22) |
| **C1 (a critic claim) stays `supported`** | RD | Yes: the as-written reading sets the field; the wider reading (`contested`) is recorded |

**Equal strictness.** Reading choices in this batch, by whose statement and which way the chosen reading falls against the alternative: Day, harsher: DN1, DN6 fidelity. Day, milder: DN6 external, C external, FM3. Critic, milder: C1. No critic statement received the harsher of two readings; there was one critic case. The pattern is not one-sided, and the sample is six.

## 5. Independence and review quality

- **Briefing with suspicions.** The briefs are not in git, so their effect cannot be measured. What can be seen: reviews went beyond anything a brief could have named (the V3 reversal needed a reviewer run; the claim-text figures needed a recount from 91 files; the P4/P5 cell sets). The risk that remains is the usual one: a reviewer told where to look spends its effort there.
- **One agent, both L1c steelmen.** The critic-side file says it was written after the Day-side one and takes the correctness rulings as given. Its conflict table was drawn up by an author who had argued both sides. Outcome measures do not show a cost (four MAJORs each; rulings 1, 1 and 5 split), but L1c carries the batch's only applied verdict moves (MA-26).
- **L5 tier.** One review for a check with a registered flip; 7 MAJOR found by that one review (MA-23).
- **Integration by a smaller model.** Nine claim-file edits sampled against their write-ups (H, H8 from `06978f1`; DN1, DN3, DN6 from `cf03b3b`; FM3, FM10, ROOT-FM from `7c0e33e`; C, C1 from `cb5ed16`). Verdict values, readings tables, scope qualifiers and both sides' paragraphs match the fix-pass text in all nine. Two drifts (MA-28). The fix pass for `ph` says its corrections "override the text above where they differ"; the H and H8 comments carry the corrected wording (1.3 to 1.7x; "cannot go extinct in this model"; 2.6 to 3.5x marginal).
- **Quotes.** Q272 ("98.8% of coding positions are found.", ¶12, followed without a space by the next sentence, as the entry says), Q273 (¶11, first sentence) and Q274 (¶14, first two sentences) are exact substrings of the held body texts at the stated non-empty-paragraph numbers. Q275's comparator sentence is present once in the held text.

## 6. The audit's own errors in this batch

| Error | Caught by | Favoured, before caught | Visible in a claim file? |
|---|---|---|---|
| FMnull label bug (`1Mb` / `1000kb`): twenty 1-Mb cells dropped from P4, P5 since registration | write-up author, confirmed by review | neither clearly (P4 gorilla BELOW 8 to 3 after the fix, P5 two more BELOW; no credit rides on either) | yes: FM3, FM10, ROOT-FM "Both" |
| FMnull P8 (ii) hit only with blocks on the window grid; P8 (i) hand estimate wrong | review, `simphase` | the audit's own prediction record | yes |
| FMnull criterion S2 unreachable | Day-side review | critics (a Day-side criterion that could not fire) | yes: FM10, ROOT-FM |
| L5 launch bugs (pickling; `sel` above 1) | the launches | nobody; no result existed | yes: C "Both" |
| L5 V3 bias direction stated as "toward Day's band" by the lead before the run | combined review, post hoc rerun | critics (it made CRITIC look conservative and hid an understatement of Z50, Z10 that runs against Day) | yes: C; dated correction appended to the pre-run note |
| L5 "more than 15 orders of magnitude" printed as a margin | review | critics | yes: C |
| L5 credit "240 to 670 times" as a test of C1a's sign | review | Day | withdrawn; C1a comment says sign not tested |
| Claim text "5.7 expected panel-site events" (C) and "4.8 events" (C1), low by two orders, standing since before the batch | L5 review | critics (overstated what the panel hides) | yes: dated corrections in C and C1; slip S-L5-1 |
| L5 P7 registered MIDDLE against its own band rule; DAY band half unreachable | ST-09, before launch | mixed; the unreachable half is against Day | yes: C |
| L1b prediction A4 (X1 0.28 to 0.60; observed 0.853) | the run | critics (L1's "in most genes" inference, now withdrawn) | yes: DN1 "Both" |
| L1c registered protein arm invalid (BLOCKER-1); amended Reading A cannot be `contradicted`; "x <= 3" unreachable | pre-run review; post-run reviews | mixed: Reading A structure for Day, x clause against him, invalid arm against the critics' tally | yes: DN6 "Against the audit" |
| `ph` draft by the lead: Day-1 clause dropped; 4-of-8 tie scored without a flag; smallest ratio as headline; "near Haldane's" true at one R | combined review | first two critics, last two Day | no (write-up only); the corrected text is what the claim files carry |
| Cost estimates (L1b 1 to 2 h against 4 min; FMnull `analytic` under 1 min against 11 min 26 s) | the runs | nobody | no; FMnull's is in the write-up (section 9 item 4), L1b's only in a commit subject |

**Direction, counted loosely (13 rows):** before being caught, five errors leaned to the critics, one to Day, three were mixed and four leaned to neither. All were found by the audit's own reviews. This is a small sample and the classification is mine; it is consistent with ST-04's observation that the untested risk leans one way, and it is not evidence of intent.

## 7. Items handed over by the FMnull reviews

### 7a. Record beside ST-10 (no decision; changes no rule)

1. **The undecided margin is symmetric about the stacked upper corner.** The zone runs from N_hi / 3 to 3 N_hi, centred on N_hi, which is every component at its upper end at once, at exposure 1 and upper divergence. A value at the null's own centre scores CRITIC, and one at three times the centre is usually still CRITIC or MARGINAL-IN. Under SOURCED the central neutral simulation is itself MARGINAL-IN at 100 kb against the registered band.
2. **The margin is taken on the value, not on the excess.** For φ_HC, whose Poisson floor is 1, three times the value asks for far more than three times the signal (at 10 kb, own exposure: 3.97, an excess 9.2 times the bound's).
3. **Criterion S2 was unreachable.** No planted model, including the one of the size Q169 (b) asserts (audit gloss), meets "φ_HC > 3x its neutral upper bound" at 100 kb once blocks are off the window grid or the SOURCED bound is used. This is a defect of the audit's criteria, on Day's side. "S2 unmet" is not to be counted against him.
4. The "not discriminating" ratio (band width above 9) was fixed in the fix pass, after the results; it is a reporting convention of R4-FMnull and not a rule.

Source: `R4-FMnull.md` section 9 item 15, section 7 (S2 row), section 1. Mirrored in the README's ST table note.

### 7b. Proposal (l): a fairer Day-side criterion for FM10. **Proposal only. Not applied.**

It changes scoring criteria, so the rule-freeze procedure of `DECISIONS.md` (O-6) applies: this written proposal, no integration on the day it is proposed, a three-review re-score of every load-bearing verdict it moves, then a rule revision number. Origin: critic-side review of FMnull (K12), accepted "as a proposal only".

**Criterion.**
1. State the alternative before the run at two sizes: the size Day asserts and one tenth of it. (Day has stated no size. The audit's gloss of Q169 (b) is f e > 1. Under rule S a gloss is not his statement, so the size should come from his release or from the right of reply, O-2; failing that it is labelled audit gloss.)
2. Compute an interval for the one-lineage excess variance (excess over the Poisson floor, not the value) on both references, human-referenced and chimp-referenced (R4-FM's mirror construction), so that the reference-projection effect is seen and not scored.
3. **DAY** if the interval excludes the whole neutral lineage-specific range. **CRITIC** if the interval's upper end is 3x below the stated alternative. Otherwise undecided, reported with the interval.
4. Before the run, report for each planted model whether it would score DAY (the reachability line the severe-testing pass asked for).

**Verdicts it could move.** FM10 external (`contested`, `load_bearing: true`) and through it ROOT-FM external (`contested`, load-bearing); FM3 external's annotation ("anomalous" or "unremarkable" against the neutral band; value `supported` stays a description). FM10 internal is `pending` by owner decision and is not touched. No count moves until a run is scored under it.

**Who it helps.** Day: a criterion that a mechanism of the size he asserts could meet, and a margin on the signal. Critics: a CRITIC class that means "the data exclude the stated alternative", in place of "inside a wide band". Risk: the neutral lineage-specific range (lambda_M) has no sourced upper end, so DAY may again be unreachable unless that range is sourced first; the interval method must be fixed before the data are looked at again, and these data have already been seen.

---

## Findings

Severity: CRITICAL, MAJOR, MINOR, COSMETIC.

### MA-21. One instance is author, briefer and judge
- **Severity:** MAJOR. **Category:** independence.
- **Evidence.** The lead wrote the `ph` scoring (`edfe33c`), the pre-run note (`5e64f0a`), both L5 launch fixes and the V3 reading (`369354d`, `30e1302`), and every ruling quoted as "the lead's ruling" in `R4-L1b.md`, `R4-L1c.md`, `R4-FMnull.md` and `R4-L5.md` ("Review resolution"). Each reviewer was a same-model instance briefed by the lead, and the briefs named the issues it suspected; no brief is in git, and none of the batch's eleven review files mentions its brief (`grep -ci '\bbrief'`: 0 in each). Fix pass to integration: L1c `140a69a` 12:23:45 to `cf03b3b` 12:31:36; FMnull `2802425` 12:32:34 to `7c0e33e` 12:36:27; L5 `0b0431c` 12:55:53 to `cb5ed16` 13:00:05. No one reviewed a fix pass or its rulings. Where the lead's own text was reviewed, it was corrected: `ph` scoring, 2 MAJOR and 9 MINOR; the V3 direction, reversed.
- **Not shown.** That any ruling was wrong. Section 2.1 finds no tilt.
- **Remedy.** No decision: commit each reviewer brief beside its review from now on. Owner decision (O-26): whether rulings between steelman reviews are made by an instance other than the author of the write-up, and whether briefs may name suspected issues or one reviewer per check goes in unbriefed. Outside reviewer as MA-01.
- **Who it helps.** Both. Day's side: the rulings that refused post hoc changes to registered wording were made by the party that wrote the registration. Critics' side: the same party withheld a registered flip against Day.

### MA-22. "Extended reading" and "registered wording governs" are applied case by case
- **Severity:** MAJOR. **Category:** rule application.
- **Evidence.** RD: "Extended readings (a different object, or a wider claim) are reported with their own verdicts but cannot set the verdict field." No test for "a different object" is given. In this batch: DN1 reading B (a report of his computation) is ruled extended, and the write-up says of the opposite view "stated because it is arguable ... the choice is the owner's" (`R4-L1b.md`, proposed moves), then it is integrated as A with no entry in `DECISIONS.md`. In L5, R-a imports s from a different post (Q44) and is "plausible", while R-d imports an s no source gives and is "extended". In L1c, reading d is extended because Day's own post exempts the step (Q273). In L1b the ruling is "registered wording stays registered"; in L5 the registered flip is withheld on a readings analysis made after the run (foreshadowed by the pre-run note, item 5).
- **Effect.** Four verdict fields rest on these calls (DN1 external, DN6 external, DN6 fidelity, C external; section 4). Their direction is mixed. They are not reproducible from the rule text by a second reader.
- **Remedy.** No decision: a register of every RD field choice with the alternative reading and its verdict (the data are already in the claim files; one table). Proposal (m), held back under the freeze: an operational test for "extended" (for example: a reading is extended if it needs a premise not in the same source, or changes the grammatical object of the quoted sentence), and a stated order of precedence between a registered move and RD. Second rater on the four choices when O-3 or O-4 is granted.
- **Who it helps.** Both. Day: DN1 could carry `untestable` under B. Critics: C external could carry `contradicted` (scoped) and DN6 external `contradicted` under b1.

### MA-23. L5 had one review while carrying a registered verdict flip
- **Severity:** MAJOR. **Category:** review tier.
- **Evidence.** `l5_adna_power.py` registers three reviews and the move "C external `contested` -> `contradicted`". `QUEUE.md` (owner process note, 2026-10-11) sets one combined review. The lead's pre-run note of 2026-10-13, item 5: "That move stays a proposal for the three reviews." One review was done (`d7f70ec`), and it found 7 MAJOR and 10 MINOR, among them the V3 reversal, the grounds of E <= 1, and the two claim-text figures. C is `load_bearing: false` in `hierarchy.yaml`, and `R5-draft.md` section 1.3 lists it among feeder nodes with sharp flip points.
- **Effect.** None on a verdict value: the flip was withheld. The tier rule has no clause for a low-tier check that proposes a flip, and a note written the same morning promised a tier that was not applied.
- **Remedy.** Owner decision (O-25). No decision: the pre-run note's "three reviews" is recorded here as not done; the note itself is not edited.
- **Who it helps.** Day chiefly (a flip against him would have rested on one review). Critics: the critic-side case for the flip (review K5) was argued in one section of one file.

### MA-24. Day-side outcomes were unreachable in parts of three of four new checks
- **Severity:** MAJOR. **Category:** check design, severity. Repeats ST-05 one day after it was filed.
- **Evidence.** L5: DAY needs median E >= 3 at s = 0.003 and 0.01, excluded by the registered arithmetic (pre-run note item 3). FMnull: S2 unreachable; S3 untestable; S4 not run; "no Day-side criterion could have been met by a mechanism smaller than the one Q169 (b) asserts" (`R4-FMnull.md` section 7). L1c: amended Reading A has no `contradicted`, registered Reading A no value but `supported` (this one favours Day); the amended "x <= 3" clause unreachable. L1b is the exception: both holes were assigned before launch. L1c and FMnull had pre-run design reviews; L1b and L5 had a note by the lead only, while `README.md` row 3 says "new checks get a pre-run design review".
- **Effect.** All disclosed, and no verdict was moved on the strength of an unreachable outcome. The sentence "three CRITIC bands and nothing moved toward Day" is true and is not a score.
- **Remedy.** No decision: the milestone post states, per check, which Day-side outcomes were reachable (table in section 3). Proposal already filed (B36, reachability line in every registration): this pass adds four instances. Proposal (l) for FMnull.
- **Who it helps.** Day. Critics in one instance (L1c's Reading A).

### MA-25. The `blind` label overstates three of the four, and `ph` is outside the table
- **Severity:** MINOR. **Category:** pre-registration.
- **Evidence.** `prereg_status.py` takes the first commit of each script. L1c was amended before the run (`0e0e840`) after a selftest miniature had shown one transfer outcome (write-up: the Day-side transfer hit is "not blind"). FMnull was amended twice (`cc5e6dd`, `408ba53`); P4 and P5 are "informed, not predictive". L5 ran with two post hoc fixes and a selftest already seen. `ph`: 455 CPU-hours, scored predictions, no row; push not shown to precede launch; the host record's smoke time precedes the commit time by about two minutes; the smoke probed `ph`-type cells for 1,500 generations (`hf_ph_smoke_wh.out`). `p45fix`: order not shown. The committed `PREREG-STATUS.md` still reads "registered, not run" for all four.
- **Remedy.** No decision, for the integrator (outside this pass's write scope): regenerate `PREREG-STATUS.md`; add notes to the tool's hand dictionary for L1c and L5 as FMnull already has; add a row or a stated exclusion for `ph`. Launch times to the second in host records.
- **Who it helps.** Both.

### MA-26. One agent wrote both L1c steelman reviews
- **Severity:** MINOR. **Category:** review independence.
- **Evidence.** Lead's process record; `REVIEW-R4-L1c-steelman-critic.md` header ("This file was written after the Day-side ..."); commits `02b87c6` 11:58 and `8742998` 12:00. L1c is the check that moved DN6 off `pending` in two fields.
- **Remedy.** No decision: the L1c entry in the review log should say so (integrator). Owner decision folded into O-26.
- **Who it helps.** Both; the direction of any effect is unknown.

### MA-27. The lead fixed a reading before the run and it was wrong
- **Severity:** MINOR. **Category:** pre-run notes.
- **Evidence.** `R4-L1b-L5-prerun-notes.md`, launch-failure section: "a bias toward Day's band", "Reading fixed here, before any task result". Reversed by review C3 and `l5_posthoc_v3.py`; dated correction appended (`cb5ed16`), earlier text kept.
- **Point.** A pre-run note protects against fitting the reading to the result. It does not make the reading right, and a wrong pre-fixed reading carries the authority of having been fixed in advance. The first draft of `R4-L5.md` used it three times (the three sentences withdrawn under review item C3).
- **Remedy.** No decision: pre-run notes state readings as "expected, to be checked", and a pre-run note that interprets a failed validation is reviewed before launch when the check proposes a verdict move.
- **Who it helps.** Day in this instance.

### MA-28. Two drifts between write-up and claim file
- **Severity:** MINOR. **Category:** integration.
- **Evidence.** (i) `claims/C-adna-zero-fixations.md`, critics' sentence: "at s <= 0.02, which includes Q44's 1e-3, the zero carries no information on the required rate". The registered scope is s <= 1e-2 and the fix pass kept it there, with s = 0.02 "descriptively the same" (K2). `QUEUE.md` repeats 0.02. (ii) `claims/DN1-dnds-080-on-20400-genes.md`, external comment: after "the MA-12 condition on L1b ... is discharged" it still carries "Open: the alignment-level route ... L1b overturns only if ...".
- **Remedy.** No decision, for the integrator: restore "s <= 1e-2 (descriptively the same at 0.02)" in C and the queue line; cut the superseded sentence in DN1.
- **Who it helps.** (i) Day. (ii) Neither.

### MA-29. Side tallies without the gloss sentence
- **Severity:** MINOR. **Category:** presentation. Repeats MA-06.
- **Evidence.** Section 2.2. `R4-L1b.md` ("It is not a scoreboard of independent tests") and `R4-FMnull.md` section 5 ("audit gloss, not statements of Day or of any critic") say what the tallies are. `R4-L1c.md` l.378, `R4-L5.md` section 3 and the `ph` section give counts by side without it. DN1's claim text says "All six critic-side predictions hit."
- **Remedy.** No decision: no side tally in the milestone post, README or board without the sentence that the predictions are the audit's; integrator adds the sentence to DN1.
- **Who it helps.** Day.

### MA-30. Process and documents out of step
- **Severity:** COSMETIC, with one item for the owner. **Category:** process. Repeats MA-20.
- **Evidence.** Three subagents ran at once against D-11's two, after an owner question in chat that is not recorded in `DECISIONS.md`. A waiter queued L5 behind L1c on the compute host; it is recorded in one line of `raw/l5.host` and no script is in git, and the pre-run note says the run "moves to builder with 4 workers" while it ran on na-workhorse with 8. `README.md` l.63 says every check is reviewed three times. README component row for `PREREG-STATUS.md` gives stale counts (corrected in this pass's README edit).
- **Remedy.** Owner decision (O-24). No decision: host records state where a run finally ran when the plan changes (L5's does).
- **Who it helps.** Neither.

---

## Concordance with earlier passes

- **Repeats.** MA-21 repeats MA-01 (and TV-01, AR-13, ST-13, AS-13, GR-13) with new evidence on briefs and on fix-pass rulings. MA-22 repeats MA-03 and AS-04 (criteria settled with results in view) in a new form: no rule was changed, a rule's undefined term was applied. MA-24 repeats ST-05. MA-25 repeats MA-04 and agrees with ST-01 that the label is not severity. MA-29 repeats MA-06. MA-30 repeats MA-20.
- **New.** MA-23 (tier against a registered flip), MA-26, MA-27, MA-28.
- **Closed by this pass.** **MA-12**: L1b reported; DN1 to DN3 no longer carry the condition; the registered sentence was applied as written. Residue, not blocking: Day's stated annotation is GENCODE v46 and L1b ran v35 (open in the write-up), and the stale sentence in MA-28 (ii). **ST-08**: both regions assigned in a note pushed before launch; neither was reached. **ST-09**: answered before launch as its remedy asked; the consequence was honoured.
- **Remediated, not closed.** **ST-10**: severity limit leads the write-up, widths and sourced shares are given, power is stated both ways; tree-incongruence was not measured and the "not discriminating" ratio was set after the results. Record 7a added.
- **Disagrees with.** ST-07 said no miss had yet changed a load-bearing verdict value in Day's favour; that is still true, but this batch has a counter-instance of the mechanism: a registered move against Day was withheld on the audit's own severity note. MA-04's forward rule ("pushed timestamps") was met for all four checks and, as ST-01 predicted, raised the `blind` count by four without making L5's DAY band reachable.

## Remediation

**No-decision fixes done in this pass** (inside `docs/research/criticality/` and `ROADMAP.md` only): this file; README component row, findings table, concordance, MA-12 and ST-08 to ST-10 statuses, the ST-10 record, the stale `PREREG-STATUS.md` counts in the component row; ROADMAP rows; `DECISIONS.md` open items.

**No-decision fixes listed for the integrator** (outside this pass's write scope; change no rule, vocabulary or verdict):
1. Regenerate `research/checks/PREREG-STATUS.md`; hand notes for L1c and L5; a row or stated exclusion for `ph` (MA-25).
2. `claims/C-adna-zero-fixations.md` and the `QUEUE.md` L5 line: "s <= 1e-2 (descriptively the same at 0.02)" (MA-28 i).
3. `claims/DN1-...md`: cut the superseded "L1b overturns only if ..." sentence; add the gloss sentence to "All six critic-side predictions hit" (MA-28 ii, MA-29).
4. `REVIEW.md` entry for L1c: both steelmen by one agent (MA-26).
5. Commit reviewer briefs beside reviews from the next check on (MA-21).
6. Milestone post: reachability per check (section 3 table); no side tally without the gloss sentence; FMnull described as "no class, no move", not as a CRITIC band (MA-24, MA-29).
7. A register of RD field choices (MA-22).

**Proposals, held back** (rule-freeze procedure): (l) fairer Day-side criterion for FM10, section 7b; (m) operational test for "extended reading" and precedence between a registered move and RD, MA-22. Verdicts (m) could move: DN1 external, DN6 external, C external (none load-bearing by `hierarchy.yaml`), and any earlier reading-dependent field re-read under it.

**Owner decisions, added to `DECISIONS.md` as open:** O-24 (subagent cap), O-25 (review tier when a check proposes a verdict flip), O-26 (who rules steelman conflicts; briefs; one agent for both steelmen), O-27 (whether to take up proposal (l)).

## What I did not examine

The arithmetic of any check. The argmap entries d445 to d469. DN2, DN5 and C1a edits beyond their verdict lines. The review briefs (not in git). Whether three subagents ran at once (taken from the lead's account; commit times are consistent with it). The `ph` raw rows. Whether reviewer numbers recomputed in the fix passes are right.
