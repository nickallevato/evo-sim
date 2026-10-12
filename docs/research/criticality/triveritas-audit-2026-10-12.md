# Triveritas audit, 2026-10-12: the audit judged by Vox Day's own criterion

*Criticality layer, component ii, part 2 of 2. Part 1 (what the Triveritas is, its versions, its strengths and failure modes, and the protocol used here) is [`triveritas-method.md`](triveritas-method.md). The earlier pass this one runs parallel to is [`METHOD-AUDIT-2026-10-12.md`](METHOD-AUDIT-2026-10-12.md) (findings MA-01 to MA-20). Findings here use the prefix `TV-`.*

**Status of this document, read first.** It was written by a Claude Opus instance launched from inside the project's own session. That is the same AI model family as the audited work, as the method audit, and as "Claude Athos", the listed co-author of the Triveritas papers. It is not an independent party. Under Day's own protocol "The authors did not score their own work." (Q224), and the one outside applier found excluded the model that composed his study (Q256). This pass breaks both rules. It also was not blind: the applier had read the method audit and the claim files first. Read every placement below as a self-assessment that a rater outside this model family has yet to check (TV-11).

**No verdict, rule, vocabulary or claim file was changed.** This is a lens, not a re-score.

Quotes followed by a Q-id are verbatim from [`sources/quotes-day.md`](../sources/quotes-day.md) (Q195 to Q271, cut by script from text fetched 2026-10-12). Counts marked "measured" were taken by script from claim-file front matter at commit `348ae2f`. Nothing was re-run or re-derived.

---

## Executive summary

**The test.** "The Triveritas holds that a claim merits warranted assent if and only if it satisfies three jointly necessary conditions: logical validity (L), mathematical coherence (M), and empirical anchoring (E)." (Q203). Each leg exists in more than one version in Day's texts (part 1, table 1.2), so each is applied under every version and every result is reported.

**Result for the audit's method as a whole.**

| Leg | Weakest version of the test | Strongest version of the test |
|---|---|---|
| **L** | L-a (valid inference, no fallacy): passes check by check as far as anyone has looked; fails for three rule-level patterns that are circular (TV-08, TV-04) | L-b (one principle, nothing ad hoc): **fails**. The verdict rule is a growing set of case-driven clauses with no stopping condition (TV-02) |
| **M** | M-a (the numbers work): passes at check level, not verified outside this model family; failed for the published summary statistics until 2026-10-12 | M-c (a quantitative structure that derives its own thresholds): **fails**. Thresholds are free parameters and no function leads from node verdicts to a conclusion (TV-05) |
| **E** | E-a (tied to observation, not refuted): passes, weakly, because no outsider has yet tried to refute it | E-b and E-c (a tested prediction on evidence the claimant does not control): passes for about ten checks; **fails** for the audit's claims about itself and for its load-bearing external verdicts (TV-01, TV-03, TV-04) |

By Day's rule a failure on any leg withholds assent. So, by the audited party's own criterion, **the audit's tallies and self-descriptions do not yet merit warranted assent, and its weakest leg is E in the specific sense of independence**: "E demands that a claim make contact with observations the claimant does not control." (Q212). That is the same place the method audit put its one CRITICAL finding (MA-01).

**Result for all three parties, same readings** (section 4). Day's root claim, the critics' positive thesis and the audit each fail the conjunction as things stand, and each fails most clearly on E: Day because his decisive results are unreleased or confirmed by his own companion papers; the critics, on this repository's record, because their central result is supported on theory and not on processed data; the audit because it reviews itself. The Triveritas does not rank the three.

**Agreement with the method audit.** Of the twenty MA findings the Triveritas agrees with twelve, agrees in part with five, disagrees with one (MA-08, on the remedy) and does not reach two. Inside two findings it otherwise agrees with, it rejects one remedy (section 6). It adds eight remediation items the existing proposals do not contain (section 7.1).

**What is sound, by this test.** Quote handling (machine-checked against hashed text the audit does not control); the checks that processed public data; the long pre-registered runs with reported misses; the practice of leaving a verdict `pending` until a like-for-like test exists; the three-column split, which already separates L and M on the author's own basis from E.

---

## 1. How the test was applied

Protocol: part 1, section 2.7. In brief: pass or fail per leg before any number (Q227); every definitional version reported; a target with no mathematics is reported both as "not applicable" (reading N1, from Q197) and as failing M (reading N2, from Q244); anchor placements are bands between Day's named anchors and are indicative only; no composite decides anything; no verdict moves.

Three kinds of target: the method as a whole (as Day treated his own paper, Q224); seven verdicts, each read as the claim "statement X has status V"; and the Day and critic claims those verdicts are about.

---

## 2. The method as a whole

### 2.1 Logical validity

**Criterion, version a.** "The conclusions must follow from the premises; the inferences must be valid; the reasoning must be free from fallacy." (Q196)

- *Check level.* Each check states its premises (verbatim quote, formal statement), its derivation is a script, and its reviews look for invalid steps. This pass did not re-derive any. Not shown to fail; not shown to pass by anyone outside the model family.
- *Rule level, three circular patterns.* (i) Rule RH6 decides whether a statement is scored by first computing how far it is from true, so the tag depends on the result it is meant to precede (MA-02). (ii) Evaluative statements are scored against the audit's own verdict table (MA-02). (iii) 26 of 52 decided `supported` or `contradicted` external verdicts rest on simulation or standard theory, which is the matter in dispute (proposal b; MA-05). Each is a fallacy in the plain sense of Q196.
- *Project level.* No inference from node verdicts to a conclusion has been written (MA-11), so there is nothing yet to be valid or invalid. The self-descriptions "neutral", "pre-registered" and "three reviews" did not follow from the practice (MA-04, MA-20); two were corrected on 2026-10-12.

**L-a: pass at check level (unverified), fail at rule level.**

**Criterion, version b.** "does the theory have a single unifying principle from which its predictions follow, or is it a collection of independent accommodations?" (Q231)

- *For the audit.* It has a unifying idea: judge each claim three ways (on its author's own basis, against its sources, against the world) and use one rule for every party. That idea is principled and predates the results.
- *Against.* The verdict rule says in its opening lines that revision 1 was written after the verdicts were known. Revision 2 added and revised clauses in answer to a rule audit (C is marked new, R1c revised); RH was added on 2026-10-09 and RH6 and RD on 2026-10-11, the last two on the day they decided load-bearing verdicts (MA-03). The rule now has about fifteen clauses and sub-clauses (R1, R1c, R1d, S, SC, N, N2b, N3, F, U, C, RH1 to RH6, RD). The 25% line sits in a gap in the observed slips (MA-14). Each RH6 check supplies its own edge (MA-02). One tier was lowered after registration (D-16). Day's L scale has anchors for exactly this: "No principled stopping condition: there is always room for another epicycle." (L ~ 35, "The L Scale") and a framework that "can accommodate any historical event after the fact" (L ~ 45, same post). With several readings per quote and a free edge per reading, the method audit's words are "some reading reaches any verdict".
- *Stopping condition.* None until the owner accepted a corpus freeze on 2026-10-12 (O-7, interpretation still to be confirmed).

**L-b: fail.** Indicative band on Day's L scale: between the L ~ 45 anchor (real principle, "undermined by accommodative flexibility") and the L ~ 60 anchor ("significant unresolved internal tensions"). A Day-side reader could argue for the L ~ 35 anchor (a patchwork); an audit-charitable reader for L ~ 65, whose anchor is a theory that "itself identifies where" its assumptions fail, since the audit publishes its own limits.

### 2.2 Mathematical coherence

**Criterion, version a.** "If a theory makes numerical predictions or depends on rates, probabilities, or magnitudes, those numbers must work." (Q197)

- Check outputs are seeded and re-runnable; one check reproduced 696 jobs on two hosts with no mismatch (method audit, U-3). Not re-run here.
- The audit's numbers about itself did not all work: totals differed by one from the claim files in five cells; a Fisher test was applied to units that are not independent; "131 hold" counted 58 defaults (MA-20, MA-06, MA-07). The comparative rates and p-values were removed on 2026-10-12.

**M-a: pass at check level (unverified outside the family); failed, now partly repaired, for summary statistics.**

**Criterion, version b.** "the operations it performs are well-defined, its parameters are finite and computable in principle, and its mathematical predictions do not contradict its own axioms" (Q205)

- The RH6 band is multiplicative (within 3x) and is applied to absolutes such as "not at all" and "nearly empty". Three times zero is zero, so the operation is not well-defined at the values it is used on, and each check invents an edge (MA-02). This is a failure of M-b in its own terms.
- Worth recording for symmetry: Day's sensitivity analysis has the same defect. His band is plus or minus 20% of the score, so the decisive score for evolution moves "from 4 to 6" (Q268).

**M-b: fail for RH6; otherwise not examined.**

**Criterion, version c.** "does the theory have a well-defined mathematical structure whose predictions are derived from its own principles, or is the quantitative apparatus absent, ad hoc, or internally contradictory?" (Q234); the AI rater's short form is "formal consistency + no free parameters" (Q247, relay).

- Free parameters set by the author of each check or rule: the 25% materiality line; the 3x band (first 10x); the edges 3e-4, 0.30 and floor(N/3); the 25% "charity haircut" in A2e; the tier boundary.
- No function connects node verdicts to a top-level statement (MA-11). Day's M ~ 10 anchor reads "Measurements taken but no mathematical function connects them to the theoretical claims." ("The M Scale").
- No error model: the reviews' catch rate has never been measured (MA-01), so no probability of error can be attached to "reviewed".
- Under version c the audit's best quantitative work does not count as M at all: "statistical comparisons ... are empirical data analysis and belong to E, not M" (Q230). Re-computation is E.

**M-c: fail at project level.** Indicative band for the project-level scheme: between the M ~ 25 anchor ("free parameters fitted independently to each phenomenon") and the M ~ 50 anchor ("The math works; the parameters float."), both from "The M Scale". The individual checks, where they derive a registered band from a stated model, sit higher; that was not assessed check by check.

### 2.3 Empirical anchoring

**Criterion, version a.** "must be confirmed or at least not refuted by what we observe" (Q199)

- Quotes are checked by machine against hashed copies of texts the audit did not write. Sixteen external verdicts rest on data the audit processed itself (proposal b).
- "Not refuted" is cheap here: nobody outside has been asked (MA-10).

**E-a: pass, weakly.**

**Criterion, version b.** "it makes at least one prediction that has been tested against observation and not refuted", on data other than "data already used to construct the claim" (Q206)

- *Checks.* The pre-registration table lists 61 registered checks: 10 blind, 6 criterion-only, 3 reproductions, 18 single-commit, 20 unknown, 4 not yet run (criticality README). Ten blind predictions clear the bar of "at least one". Several registered predictions missed and the misses were reported (H8: K1 miss), which is what an anchored claim looks like. On Day's tally version of E (Q237, Q238) the anchored share is 10 of 57 run.
- *The audit's claims about itself.* That it is even-handed, that its reviews catch errors, that another rater would reach the same verdicts: no prediction has been stated and none tested. The seeded-error test and the blind re-derivation are specified and not run (proposal f). The one agreement figure was not blind (MA-19).
- *The external column.* "no load-bearing external verdict rests on data the audit processed" (criticality README, on proposal b). Day made this exact objection to a critic: keruru's argument is "incorrect due to his failure to anchor the abstract mathematical elements in material reality" (Q251). The same sentence applies to every `supported` or `contradicted` that rests on a Wright-Fisher simulation, whichever side it favours.

**E-b: pass by the minimum bar for about ten checks; fail for the audit's self-claims and for the load-bearing external verdicts.**

**Criterion, version c.** "Any system of claims that cannot, even in principle, be constrained by something external to its own stipulations is epistemically inert." (Q211)

| The audit controls | The audit does not control |
|---|---|
| Every reviewer (one model family, briefed by the project) | Day's and the critics' texts, hashed |
| The verdict rule and each change to it | Public datasets (ancient-DNA genotypes, genome alignments) |
| Which checks are load-bearing and which tier they get | Published literature values |
| Whether its own attacks are `upheld` (MA-15) | The public repository and its history (local reflog only; no third-party timestamp) |
| The truth standard for evaluative statements (MA-02) | |
| Its simulations and their unsourced parameters (MA-16) | |

- **Reading P ("even in principle").** Pass. The repository is public, the checks run, ROOT has a stated falsifier, the right-of-reply letters and reviewer briefs are drafted.
- **Reading A (as practised to 2026-10-12).** Fail. Nothing outside has yet constrained anything: no author contacted, no human specialist, no other model family, and "No finding is closed" (criticality README).
- Day's E scale offers both placements. For confirmation by reviewers who share the author's expectations: "Over 100 papers were published confirming the phenomenon, all from laboratories primed to expect it." (Q240, the E ~ 10 anchor). For cross-tool and cross-host replication: "The convergence of independent methods is the strongest form of empirical anchoring short of direct experimental control." (Q239, the E ~ 65 anchor). The first describes the review process; the second describes the best of the data checks.
- Day's own mathematics says why three same-family reviews are not three filters: the multiplication of error rates "assumes the three filters are probabilistically independent" (Q208).

**E-c: reading-dependent. Pass in principle, fail in practice to date.**

### 2.4 Conjunction

"warranted = (L > threshold) and (M > threshold) and (E > threshold)" (Q228). The method fails at least one version of every leg, and fails the strong version of all three. Day's rule against compensation applies: "I do not care how strong you are on two dimensions." (Q219). The audit's real strengths (disclosure, quote checking, executable checks) do not offset an unmet leg.

For readers who want Day's arithmetic: with bands of roughly 45 to 60 (L), 25 to 50 (M, project level) and 30 to 60 (E, between the "naive observation" anchor at E ~ 30 and the "multiple independent experimental methods" anchor at E ~ 60, both from "The E Scale"), the mean runs from about 33 to 57, under the 60 mark throughout and under the 50 mark for most of the range. **This number is indicative only**: it is self-scored, the scale is ordinal by its author's account ("The actual numbers are irrelevant.", Q241), and Day's own eight papers scored 90 to 94 from raters he chose (Q267), so the scale's behaviour in friendly and unfriendly hands is unknown.

---

## 3. Seven verdicts, with the Day and critic claims beside them

Selection: the examples named in the brief, both sides, five of the seven touching a load-bearing node. Not a random sample. For each row the audit's verdict is read as a claim and tested on L, M and E; then the same legs are applied to the Day claim and to the critic's counterpart.

Abbreviations: N1 = no mathematics, M not applicable (Q197); N2 = no mathematics, fails M (Q244).

### 3.1 B, internal: `non-sequitur` (Day: neutral theory cannot rescue the shortfall; load-bearing)

| | L | M | E |
|---|---|---|---|
| **Audit's verdict** | Each reading's inference is valid (rule N2b against Day's own Hard Limits text). Which reading fills the field was settled by redefining "most charitable" four minutes after integration, with the outcomes known (MA-03, D-15). L-a pass per reading; **L-b fail** (ad hoc selection) | Fill values 0.256, 0.281, 0.025, 0.697 are computed; the 0.30 edge that separates them is the author's (MA-02). **M-c fail** (free parameter) | Premise is Day's text, which the audit does not control: E-c pass for the premise. No blind second rater; file status `extracted`; no three-review set. **E-b fail** |
| **Day's claim** | By the audit's record the conclusion needs an empty pipe that his own text excludes: L-a fail if that record stands, open if B is re-opened (O-5) | B1 and B2 arithmetic `holds` on his basis: M-b pass | No tested prediction on independent data recorded; external `contested`: E-b not shown |
| **Critic counterpart** (B7, k = μ, 1/(2N)) | Valid from Wright-Fisher premises: pass | Pass | `supported` on theory (proposal b), not on processed data: E-b not shown on this record |

Readings: on Day's flux reading (fill 0.697) the audit's own rule tags the sentence rhetoric and the node `holds`. The Triveritas has no rhetoric tag (TV-08), so on that reading it would score the literal claim and ask for E.

### 3.2 A2e, external: `contradicted` (scoped) (Day: the LTEE rate is a ceiling; load-bearing)

| | L | M | E |
|---|---|---|---|
| **Audit's verdict** | Valid as scoped (per-generation count, any effect size, coding only, model-inferred alpha); the single word in the field drops the scope (MA-08). Moved on a post hoc addendum whose review found "the trigger and blockers were set by the author who scored them" (MA-03). **L-b fail** | 798 against a flip of 191 (4.2x) after a 25% haircut in Day's favour; 11 to 21x on the paper's own base. M-a pass (unverified); one free parameter | Basis is published estimates (literature), which the audit does not control: E-c pass. The estimates are model-inferred, and the comparison was not registered before it was made: **E-b fail** |
| **Day's claim** | Audit: his own figures give a supply ratio of 93,659 while the text lists "effectively unlimited mutation supply" as an LTEE advantage; mutator lines in the same experiment exceed the ceiling. **L-a fail** on his own text (file status `reviewed`) | Rate arithmetic holds: pass | A ceiling is refuted by one case above it. Day: "one counterexample is sufficient to negate E" (Q242). On the audit's record (A2d) the counterexample is inside the LTEE: **E fail** by veto |
| **Critic counterpart** (A2i, Matev: per-year, not per-generation) | `holds` at status `extracted`, a default (MA-07) | A units argument without numbers: N1 n/a, N2 fail | `pending` |

### 3.3 C7, internal `non-sequitur`, external `contradicted` (Day: "genetic drift isn't happening at all over the last 7000 years")

| | L | M | E |
|---|---|---|---|
| **Audit's verdict** | Fixation reading: the count is true, the inference to "no drift" does not follow. Strict reading: tagged rhetoric and unscored (RH6) | Expected completions from intermediate frequency in about 280 generations at N_e near 1e4: about zero. Edge 3e-4 is the author's | **Data the audit processed** (F_adj 0.002 to 0.014 between ancient-DNA time bins): E-c pass, the strongest in this sample; attribution to drift against admixture left open |
| **Day's claim** | L-a fail (from few fixations to no drift) | A comment with no calculation: "Numbers are mentioned. Mathematics is not performed." (Q236): N2 fail | The counts are real; the conclusion is contradicted by measured frequency change: E fail by veto |
| **Critic counterpart** | None. The audit made the counter-argument itself and filed it under `side: literature` (C1; MA-15) | | |

This is the one sampled verdict where, in Day's phrase, "the logic, the math, and the empirical evidence all triangulate" (Q248). On the strict reading the two systems disagree: RH6 excuses a statement 23 to 46 times off as rhetoric; the Triveritas would fail it on E (TV-08).

### 3.4 DN6: `pending` on all three columns (Day: protein-guided alignment biases dN/dS downward)

| | L | M | E |
|---|---|---|---|
| **Audit's verdict** | Withholding is what the test prescribes for an untested claim; Day's demarcation version allows "or could satisfy upon testing" (Q220). The fidelity field takes the reading kinder to Day although the other reading is contradicted by the cited paper's methods text (RD) | Nothing computed yet | A test (L1c) is registered and not run: the only row here where the audit has a prediction on the table **before** the result. E-b in proper form, outcome unknown |
| **Day's claim** | A coherent mechanism with an observable: L-b pass (credit) | No excluded-codon count, no example gene: N2 fail; on N1, not yet applicable | The mechanism was built to explain the gap between his 0.80 and the published 0.23, and that gap is its only support: "not merely consistency with data already used to construct the claim" (Q206). **E-b fail** until an independent test or a release |
| **Critic counterpart** | None published as of 2026-10-12 | | |

The Triveritas sides with MA-12 here: DN1 to DN3 were marked `contradicted` before the like-for-like run, and an untested chain has not terminated.

### 3.5 B5c, internal `non-sequitur`, external `contradicted` (Hancock: about 76.8 fixed per generation, about 38 million)

| | L | M | E |
|---|---|---|---|
| **Audit's verdict** | Changed from `holds` by rule revision 2 (omitted ancestral term). It depends on the 25% line (MA-14), but the margin is +39% to +46%, so any line up to about 39% gives the same result | 58.6M against 40M and 42.07M: computed | Basis theory, also data (proposal b). Source is a video's auto-captions (MA-09), a weaker tie to the text than a document |
| **Hancock's claim** | His conclusion is the match; with the term he omits there is no match: L-a fail on the audit's record | Slip corrected in the same video (credit); corrected arithmetic consistent | In form this is what E-b asks for: a rate and a time from independent sources, compared with an observed count. On the audit's accounting it misses, so by Day's veto it fails; the audit's corrected split is the audit's own contribution (MA-15) |
| **Day counterpart** (B3a, k = μN/N_e; withdrawn in B3g) | Algebra holds; premise withdrawn by Day himself (credit) | Pass on its basis | `contradicted`; his retraction is one of two Day nodes that pass all three audit columns (TV-06) |

### 3.6 G2e, internal `holds` (Myers: evolution is "massively parallel"); RH-20 "I debunked ..." unscored

| | L | M | E |
|---|---|---|---|
| **Audit's verdict** | `holds` on a file at status `extracted`: no check, no review (MA-07) | None | None. **Not warranted on any leg**; the right word is the method audit's `unexamined` |
| **Myers's claim** | True as a description of populations. His "debunked" rests on describing MITTENS 3.0 as serial, which its text denies (slip ledger S-G2e-1) | No mathematics: N1 n/a; **N2 fail** ("simply does not show up", Q244) | No tested prediction |
| **Day counterpart** (G2g, "fixation must be sequential") | `non-sequitur`; Day concedes the all-cause rate is faster | | Secondhand (book appendix, unread) |

Here the Triveritas is harder on the critic than the audit is. The audit gives a default `holds` and excuses "debunked" as rhetoric; Day's test fails the post on M (under N2) and E. That helps Day's side, and it is the precision asymmetry of MA-06 seen from the other end.

### 3.7 H8, internal `holds`, external `contested` (Day: Kimura's Fixation Calculator, Term 3; load-bearing)

| | L | M | E |
|---|---|---|---|
| **Audit's verdict** | `contested` here means conditional on K (tested to 64,000) and on the survival horizon: an honest conditional that one word hides (MA-08, MA-16) | Term 3 reproduced within the materiality rule. Registered predictions at K = 64,000: one miss, one indeterminate, one hit, one hit or marginal miss, all reported (credit) | **Simulation only**, with unsourced parameters. A simulation is specified by the claimant: E-c fail. The verdict stands on L and M and, correctly, does not claim more than `contested` |
| **Day's claim** | The step from s_max of about 1 to a bound on summed selection is contradicted under soft selection and holds under hard selection only through the death budget (audit record): L conditional | 8.3e-12 follows from his inputs: M-b pass. Inputs s_max and d = 0.45 are free | No observation is offered for the predicted rate: **E-b fail** (untested). This is the profile Day assigns to string theory: strong L and M, "Effective composite for warranted assent: 0" (Q223) |
| **Critic counterpart** (H2a, Hancock: the cost applies to hard selection only) | `holds`, `accurate` to Nunney 2003, status `extracted` | N1 or N2 | `contested`; no human hard/soft split is sourced |

### 3.8 What the seven show

- One verdict of seven (C7, fixation reading) stands on all three legs. One (DN6) is correctly withheld. Three (B, A2e, H8) stand on L and M with E unmet or model-based, and two of those three were moved under a lower review tier than the project's rule requires. One (B5c) is robust to the audit's own free parameter. One (G2e) is an unexamined default.
- On the audit's record the Day claims in the sample fail L in four of seven (B, A2e, C7, G2g) and have E failed or unmet in six (all but G2g, which is secondhand and was not assessed); the critic claims mostly have no mathematics at all, which the audit's rule records as `holds` and Day's test records as an empty M.
- The legs do separate. That is the best evidence in this pass that the Triveritas measures something the three-column scheme reports less clearly: which kind of support a verdict has.

---

## 4. The same test on the two top-level positions

Stated as the method audit's mirror-tree remedy would state them (MA-13).

| | L | M | E |
|---|---|---|---|
| **Day: no mechanism suffices (ROOT)** | One simple principle (rate times time against requirement): L-b favourable. Two load-bearing steps carry `non-sequitur` on the audit's record (A2e, B), one of them under dispute (O-5). Day's own Triveritas papers give the logic of evolution as satisfied, unsound, 60 and 40 in turn (Q216, Q200, Q222, Q233) | Much of his arithmetic `holds` on his own basis (method audit: 66 internal `holds`, 21 of them on files never checked). Parameters have moved between versions (refresh watch list). He withdrew one formula himself (B3g) | His recent evidence is unreleased: no code, gene list or coordinates for the dN/dS and "Fourth Mechanism" results (watch list), so nobody else can observe it. In the Triveritas papers the confirming outcome for evolution's M failure is his own companion work (Q217). By Q212 that is not anchoring. **E not met** |
| **Critics: standard mechanisms suffice** | k = μ is a valid theorem and a single principle: pass | Individual critic computations are mixed (B5c double count; several one-line claims with no mathematics) | On this repository's record the central result is `supported` on theory. The quantities that would anchor the positive thesis (adaptive fraction, ancestral N_e fit, the soft-selection premise) sit in the gaps ledger, not in checked nodes (MA-13). **E not shown here**; the wider literature was not searched in this pass |
| **The audit** | Section 2 | Section 2 | Section 2 |

Under Day's criterion none of the three top-level positions merits assent yet. This is not a tie and not a ranking: the Triveritas says each "is false or unwarranted" (Q214) until its missing leg is supplied, and "unwarranted" is all that follows. What each party would have to do is concrete: Day, release code and data; the critics (or the audit on their behalf, labelled as such), put the positive thesis's quantities through data checks; the audit, get outside raters.

A caution that cuts toward the critics: Day's M ~ 5 for evolution depends on ruling population genetics "not part of the modern synthesis" (Q269) and on the MITTENS result itself (Q222). The Triveritas verdict on evolution is therefore not independent evidence about evolution; it is branch A restated. A caution that cuts toward Day: his tool scores intelligent design lower than evolution (Q221), and nothing in this pass shows him applying it selectively.

---

## 5. Findings

Severity as in the method audit. "Helps" says whose position the finding strengthens if acted on.

### TV-01. By Day's corollary the audit is self-sealing in practice
- **Severity:** CRITICAL. **Category:** E-c, independence. **Concordance:** agrees with MA-01.
- **Evidence.** Section 2.3, table and readings. Every confirming act (review, steelman, adjudication, `upheld`) is performed by the party whose claim it confirms.
- **Why the Triveritas adds something.** It supplies the audited party's own words for the defect (Q211, Q212, Q240) and his own mathematics for why three same-family reviews do not multiply (Q208).
- **Remedy.** As MA-01. In addition, adopt the two rater rules Triveritas users already apply: the composing model does not score (Q224, Q256); one model family per leg, no overlap, human scores first and blind (Kererū's design, Q255 to Q257).
- **Helps:** both sides.

### TV-02. The verdict rule is a set of accommodations, with no test for overfitting
- **Severity:** MAJOR. **Category:** L-b. **Concordance:** new as a whole; MA-02, MA-03 and MA-14 found three of the clauses one at a time.
- **Evidence.** Section 2.1. About fifteen clauses and sub-clauses, each added after a case that needed it; no record of which case prompted which clause; no clause has been tested on claims it was not written for. Day's Mathematical Proof names the pattern: "Overfitting is the canonical failure mode of M ∩ E without L." (section 2.3 of Zenodo 18724454).
- **Remedy.** (i) A clause-provenance table: for each clause of X1, the date, the case that prompted it and the verdicts it moved (no-decision fix). (ii) A hold-out test: apply the frozen rule to claim nodes extracted after the freeze of the rule, or to a blind re-extracted sample, and report how often a rater needs a clause that does not exist (proposal).
- **Helps:** both. Day-side: shows whether clauses were fitted against him. Critic-side: shows whether RH and C were fitted for him.

### TV-03. The audit has made no prediction about itself that could fail
- **Severity:** MAJOR. **Category:** E-b. **Concordance:** new; extends MA-01 remedies 1 and 2, MA-11 (b), MA-19.
- **Evidence.** Section 2.3. The seeded-error test and the blind re-derivation are designed, with no stated result that would count against the audit. The right-of-reply drafts state no expectation.
- **Remedy.** Before any of the three is run, register for each: the predicted result, the result below which the audit withdraws a stated claim (for example, stops publishing tallies), and who decides. One paragraph in each protocol (proposal; numbers to be set by someone other than the author of the checks).
- **Helps:** both.

### TV-04. Load-bearing external verdicts are mathematics without anchoring, the fault Day charges to a critic
- **Severity:** MAJOR. **Category:** E-b, L-a (question-begging). **Concordance:** agrees with MA-05 and MA-16.
- **Evidence.** Section 2.3; Q251. Applies to verdicts favouring critics (B7 `supported` on theory) as much as to those against Day.
- **Why the Triveritas adds something.** Day cannot object to the standard, having used it; and the critics cannot object that it is aimed at them, because it removes the model-based `contradicted` verdicts against Day as well.
- **Remedy.** Proposal b (`external_basis`), in its "relabel" strength.
- **Helps:** Day on the model-based `contradicted` verdicts; critics where Day's claims rest on calculation alone (H8).

### TV-05. Thresholds are free parameters; the multiplicative band is undefined where it is used
- **Severity:** MAJOR. **Category:** M-b, M-c. **Concordance:** agrees with MA-02 and MA-14; the per-verdict listing is new.
- **Evidence.** Section 2.2; sections 3.1, 3.2, 3.3.
- **Remedy.** (i) Proposal d. (ii) For each load-bearing verdict, list the author-chosen constants it depends on and the value at which it flips, as the write-ups already do for simulation parameters (no-decision fix where the numbers exist). Section 3.5 shows the form: B5c holds for any materiality line up to about 39%. (iii) Use absolute, not proportional, bands near zero. The same advice applies to Day's plus or minus 20% (Q268).
- **Helps:** both.

### TV-06. Three columns allow the trade-off the Triveritas forbids
- **Severity:** MAJOR. **Category:** conjunction. **Concordance:** partly disagrees with the method audit, which calls the three-column split "the best idea in the method" and faults only the counting (MA-07, MA-15).
- **Evidence (measured).** Nodes with internal `holds` and external `supported` and fidelity `accurate` or `n/a`: 14 of 233. Day 2 of 130 (A1 and B3g, the second being his own retraction); critics 11 of 61, six of them at status `checked` or `reviewed`; allies 0 of 15; literature 1 of 27 (C1, raised by the audit). Against 131 internal `holds`. At least one of the 14 (B7) is `supported` on theory by proposal b's coding, so the count on data is lower.
- **Reading.** The hostile biologist's line in the method audit, that "Holds, misread, contradicted" is three words for wrong, is the Triveritas view. The method audit's reply, that scoring on the author's own basis is what stops the audit from asserting the consensus, also stands. Both can be served.
- **Remedy.** Keep the three columns; add a derived, non-editable conjunction flag per node (all three met; met on data), and never publish a count of one column without it (proposal). This does not move any verdict.
- **Helps:** critic-side against Day's 66 `holds`; Day-side against the critics' 50.

### TV-07. Claims without mathematics pass by default
- **Severity:** MINOR to MAJOR. **Category:** M, symmetry. **Concordance:** new remedy for MA-06 (mechanism 2) and MA-07.
- **Evidence.** Sections 3.2, 3.6, 3.7 (A2i, G2e, H2a: `holds`, status `extracted`, no mathematics). The same applies to Day's comment-level claims (C7).
- **Remedy.** A front-matter field `quantitative: derivation | numbers-only | none`, set mechanically at extraction, reported beside every `holds` (proposal). Under reading N1 it is information; under N2 it is a fail on M. The audit need not choose.
- **Helps:** Day-side mostly (critics' one-line claims are exposed); also exposes Day's own unquantified lines.

### TV-08. The Triveritas has no rhetoric exemption; RH6 and the Triveritas are both Day's and they conflict
- **Severity:** MAJOR. **Category:** L-a, E. **Concordance:** agrees with MA-02.
- **Evidence.** Sections 3.1, 3.3, 3.6. The Triveritas is "scoped to claims about reality" (Q213) with no carve-out for register. The audit adopted Day's dialectic and rhetoric distinction by owner directive and gave it the power to switch scoring off.
- **Remedy.** MA-02 remedy 2 (always publish the literal reading and its distance, whatever the tag).
- **Helps:** critics on C7; Day on Myers's "debunked".

### TV-09. Day's Triveritas claims about evolution are in the corpus and unaudited
- **Severity:** MINOR. **Category:** coverage. **Concordance:** new.
- **Evidence.** Three Zenodo papers and the Treatise serial score or classify evolution (Q200, Q207, Q216, Q217, Q222, Q233, Q269 to Q271). The bibliography had them as "out-of-scope: philosophy/theology". Four versions of the L result in four weeks; two incompatible grounds for the M result (part 1, section 2.5, item 2).
- **Remedy.** Rows in `ledgers/versions.md`; one claim node for "the Modern Synthesis fails the Triveritas on M", depending on branches A, G and H, with both readings of Q269 (proposal; the material predates the corpus freeze).
- **Helps:** neither in advance.

### TV-10. Verdicts carry no as-of date
- **Severity:** MINOR. **Category:** E, dynamics. **Concordance:** new; adjacent to MA-11 and MA-12.
- **Evidence.** Day: "The criterion is dynamic, not permanent." (Zenodo 18924026, section 3.4). Kererū reports an essay the human rater passed whose central prediction had been falsified by the time the models scored it (his finding 4, "Temporal Decay Is Real"). Claim-file verdicts are dated only in free-text comments.
- **Remedy.** An `as_of` date per verdict column and a note of the event that would re-open it (the template's "Result that would change a verdict" line, missing from 91 files per MA-07).
- **Helps:** both.

### TV-11. This application is itself outside Day's protocol
- **Severity:** CRITICAL for the standing of this document; no effect on any verdict. **Category:** independence.
- **Evidence.** Status paragraph. The applier chose among three versions of each leg, placed the bands, and is of the family that both wrote the audit and co-wrote the Triveritas papers.
- **Remedy (owner).** Run Day's own protocol on the audit: give a fixed packet (the methods-and-limitations page, the verdict rule, the seven verdicts of section 3 with their sources, and the three scale posts) to the raters Day himself used, Grok and Gemini (Q224), and to at least one other non-Claude model, one family per leg, with the instruction to score L, M and E under each version in part 1, table 1.2. Include the Triveritas result in the right-of-reply letter to Day and ask him to score the audit himself.
- **Helps:** both.

---

## 6. Concordance with the method audit

| MA finding | Triveritas leg | Result | Note |
|---|---|---|---|
| MA-01 reviews are one reviewer | E-c | **agrees** (TV-01) | Day's practice would accept other-vendor AI raters as independent (Q225); the method audit says that only reduces correlated error. The stricter view is the method audit's |
| MA-02 RH6 rewards distance from truth | L-a, M-b, E | **agrees** (TV-05, TV-08) | The Triveritas would go further and drop the rhetoric exemption for any claim about reality |
| MA-03 rules remade the day they decided verdicts | L-b | **agrees** (TV-02) | |
| MA-04 pre-registration unverifiable or empty | E-b | **agrees** in definition (Q206) | Day's practice is looser: he accepts backtesting as "a very reasonable test" (Q254). Commit timing and labels are not covered |
| MA-05 external decided by the disputed theory | E-b, L-a | **agrees** (TV-04) | **Rejects** remedy 2 (declare standard theory the default): the Triveritas grants no default; every position owes all three legs |
| MA-06 comparative error rate | M-a | **agrees in part**: the statistic fails M-a; volume, precision and scrutiny effects are not covered | |
| MA-07 `holds` is the default | L, M | **agrees**; adds TV-06, TV-07 | **Rejects** the method audit's defence of reporting the columns separately: by the non-compensation rule a node is reported by its conjunction as well |
| MA-08 `contested` holds five things | E | **disagrees on the remedy** (agrees the category is uninformative) | The Triveritas has no middle category: an unanchored claim is "unwarranted", whoever made it. It would not split `contested` four ways but replace it with "not warranted: missing leg X" |
| MA-09 the book is unread | E-a | **agrees** | Applies to this pass too: *Veriphysics: The Treatise* was not read |
| MA-10 no one outside has been asked | E-c for the checking function | **agrees in part**: outside checking yes; fairness and right of reply are not covered | |
| MA-11 no aggregation rule, no stopping rule | L-b, M-c | **agrees** | Day's own aggregation (mean, veto, three pass marks) is no model to copy |
| MA-12 verdicts ahead of the like-for-like test | E | **agrees** (section 3.4) | |
| MA-13 one decomposition; mirror tree | symmetry of burden | **agrees** (section 4) | |
| MA-14 the 25% line | M-c, L-b | **agrees**; section 3.5 shows one verdict robust to it | |
| MA-15 category leaks; audit as party | E-c | **agrees in part**: the audit judging its own attacks is a self-sealing step; the coding of `side` is not covered | |
| MA-16 from simulation to hominids | E | **agrees** (TV-04) | |
| MA-17 presentation manufactures symmetry | none | **not covered** | The non-compensation rule points the same way, weakly |
| MA-18 budget decides depth | none | **not covered** | |
| MA-19 what is missing | M (error rate), E (TV-03) | **agrees in part**: error rate and reliability yes; threat model, COI, licence are not covered | |
| MA-20 documents disagree with practice | L-a (contradiction) | **agrees in part**: the contradictions yes; stale counts and tables are not covered | |

**Counts (one primary result per MA finding).** Agrees: 12 (MA-01, 02, 03, 04, 05, 07, 09, 11, 12, 13, 14, 16). Agrees in part: 5 (MA-06, 10, 15, 19, 20). Disagrees: 1 (MA-08, on the remedy). Not covered: 2 (MA-17, MA-18). Remedies rejected inside findings otherwise agreed: 2 (MA-05 remedy 2; column-wise reporting under MA-07). New from the Triveritas, with no MA counterpart: TV-02 (as a whole), TV-03, TV-06, TV-07, TV-09, TV-10. TV-11 concerns this document only.

**What the method audit found that the Triveritas cannot see at all:** fidelity to sources, fairness to named people, conflicts of interest, presentation, budget. A project judged only by the Triveritas would not have been told to buy the book for the reason MA-09 gives, or to write to the people it names.

---

## 7. Remediation

### 7.1 What the Triveritas adds beyond the existing proposals (a) to (f)

1. **Clause-provenance table and hold-out test for the verdict rule** (TV-02).
2. **Registered predictions and failure thresholds for the audit's own tests** (seeded-error, blind re-derivation, right of reply) before they are run (TV-03).
3. **A conjunction flag per node**, and no single-column tallies (TV-06).
4. **A `quantitative` field per claim** (TV-07).
5. **Per-verdict list of author-chosen constants with flip values**, extended from simulation parameters to rule thresholds; absolute bands near zero (TV-05).
6. **An `as_of` date per verdict** (TV-10).
7. **Claim node and version rows for Day's Triveritas verdict on evolution** (TV-09).
8. **Rater rules borrowed from Triveritas users** for the non-Claude seat: composing model excluded, one family per leg, human blind first (TV-01), and **Day's own two raters** among those asked (TV-11).

### 7.2 Split three ways

**No-decision fixes (change no rule, vocabulary or verdict).**
- Clause-provenance table for X1 (TV-02 i).
- Flip-value notes for the load-bearing verdicts where the write-up already has the numbers (TV-05 ii).
- `versions.md` rows for the four Triveritas versions on evolution; add `veriphysics.substack.com` to the refresh watch list (TV-09).
- Done by this pass: bibliography rows for the ten papers corrected from "out of scope".

**Proposals (held back; to be specified with the counts they move, under the rule-freeze procedure).**
- Hold-out test of the frozen rule (TV-02 ii). Moves no count by itself.
- Prediction and threshold paragraphs in proposals f1, f2 and the right-of-reply protocol (TV-03). Moves no count.
- Conjunction flag (TV-06): adds a derived field; the headline would read 14 of 233, not 131 `holds`.
- `quantitative` field (TV-07): adds a field; under reading N2 it would recast an unknown number of `holds`; to be counted before any decision.
- `as_of` field (TV-10).
- One new Day claim node (TV-09).
- `external_basis` in relabel strength (TV-04), already proposal b.

**Owner decisions (proposed as O-10 to O-12; `DECISIONS.md` was not edited by this pass).**
- O-10. Send the Triveritas packet to non-Claude raters, including Grok and Gemini, under the rater rules in 7.1 item 8 (TV-11). This is the same authorisation as O-4 with a second packet.
- O-11. Include this document's result in the right-of-reply letter to Day and invite him to score the audit with his own tool (TV-11). Needs the same lifting of hard rule 6 as O-2.
- O-12. Decide whether the Triveritas stays a standing lens of the criticality layer (re-run at each pass, by an outside rater when one exists) or is a one-off.

---

## 8. What was not examined

- No derivation, simulation or count behind any verdict was re-run. The seven verdicts were read from claim-file front matter, statements and verdict comments, not from the full write-ups or reviews.
- The seven are a chosen sample, not a random one; 226 other claim files were not put through the test.
- The critics' positive thesis was assessed only as recorded in this repository. No literature search was made for data-based tests of it.
- The anchor bands are the applier's judgement against Day's scales, with no second rater.
- Whether Day would accept any of the readings used here is unknown. He has not been asked (hard rule 6).
- Part 1, section 3 lists what was not read of the Triveritas corpus, including the Treatise itself.
