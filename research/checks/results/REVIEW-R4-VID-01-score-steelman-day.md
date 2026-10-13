# Review 2 (steelman, Day's side): R4 VID-01-score

Reviewer: `reviewer` (Opus), fresh instance. Did not author the work, did not write the correctness
review, has not read the critic-side steelman. Task EVO-76, review 2 of 3.
Brief: `research/checks/briefs/VID-01-score-reviews-reviewer.md` (`d7d2f7d`).
Under review: `research/checks/results/R4-VID-01-score.md` (registration `e857d1f`, post hoc
`31d7f0d`) and `A4d`, `A5h`, `Ge`. Lead rulings R-1..R-7 binding and not reopened. A5h's
`internal: arithmetic-error` and A4d's verified absence of a d term are not contested here and are
not contestable: I re-hashed both PDFs myself (`22bb4ef8…`, `d55e8a03…`, matching `bib-day.md`
rows 50/51) and re-ran the token searches.

**Counts: 0 BLOCKER, 4 MAJOR, 5 MINOR, 6 NOTE.**
**Findings that would move a verdict field: none.** A4d `internal: holds`, A5h
`internal: arithmetic-error` / `external: pending` and Ge `internal: holds` are all correct on
Day's side of the argument as well as on the audit's. MAJOR-1 changes the *grade of a critic
statement* in A4d's Readings table; MAJOR-2 and MAJOR-3 change what the write-up may assert and
what it must record for symmetry; MAJOR-4 is a disagreement with the correctness review.

This is the strongest honest case for Day, not an advocacy brief. Where the honest case is weak I
say so, in the same place (MINOR-1, MINOR-2, and the "cost to Day" paragraphs under MAJOR-1 and
MAJOR-2).

---

## MAJOR

### MAJOR-1 — reading (c) is graded "partly accurate"; it rescues none of the quoted statement
The Readings table (write-up Q1; `A4d` line 68) grades reading (c) **partly accurate** because
"an overlapping-generations correction **is** still in play in 3.0". Scored against the quoted
statement, as rule S and rule RD require ("the reading under which the speaker's *quoted statement*
is most defensible"), (c) rescues nothing. GGR-13/GGR-14 assert four things:

| Proposition in the quote | Against the hash-matched 3.0 text |
|---|---|
| "he's still using the de coefficient in mittens" | no `d` token, no `0.45`, no `selective turnover` (re-verified) |
| "he calculates it at 450,000 generations" | `450,000` 0 hits; main:488 "The divergence time is 6.3 million years. At 25 years per human generation, this provides 252,000 generations" |
| "he multiplies it by the D coefficient … to cut it almost in half to like 225,000" | `225,000`, `202,500` 0 hits; nothing multiplies 252,000 |
| "he's still using that number for all his math" | `252,000` 10× and uncut, including inside §8.6 itself |

The last row is the one the write-up does not use and should. §8.6's own sentence applies the
cited rate to the **full, uncut** count: "Applied to 252,000 generations provides 8 achievable
fixations against the 205 million required" (main:653–654). I checked whether a d could be hiding
in that step: 113,400 / 27,600 = 4.1, against the printed 8; 252,000 / 27,600 = 9.13 (A5e already
records the printed 8 as unreconciled). **The printed number is inconsistent with any application
of d = 0.45 to the generation count.** So under reading (c) the quoted statement is contradicted
too; what survives is an *adjacent* observation about the provenance of a cited rate, which is a
different proposition from the one the panel stated.

**Fix:** regrade (c) in the write-up and in `A4d` as "**contradicted as to the quoted statement**;
one adjacent point survives", and move the adjacent point into the sentence where it already lives
(A4d's Weaknesses line), with the §8.6 "Applied to 252,000 generations" clause added as the reason.

**What this costs Day, recorded in the same finding.** The adjacent point is real and in places
stronger than the write-up says, and the fix pass must not use MAJOR-1 to delete it:
- `effective generations` occurs **exactly once** in body and addendum (main:653), in that
  sentence. "Effective generations" is Bio-Cycle vocabulary: `C2-bio-cycle-d.md` defines the model
  as `g_eff = d × g_nominal`. A rate quoted per *effective* generation divided into a *nominal*
  count is a unit mismatch on its face, and 3.0 nowhere reconciles it — which is plausibly why the
  printed 8 reconciles with neither 9.13 nor 4.1.
- Day gives no reason for dropping d, having built an entire paper (Z18203514) on the claim that
  population genetics cannot handle overlapping generations. GGR-13's reasoning ("if he's
  retracting the claim about … effective population size, then … there shouldn't be any d
  coefficient at all") is sound, and 3.0 in fact contains no d — the critic's own stated
  expectation is met, which is a point for the critics' reasoning and for Day's text at once.

### MAJOR-2 — the Q3 "refinement" overstates R4-G1 against Day's §2 bullet
The write-up (Q3, and "For the critics") says the panel's recombination answer is "**on point
against a premise MITTENS 3.0 actually uses**", that "`R4-G1.md` is on their side of it", and that
"Day's own stated direction holds only in the linked and clonal cases". I re-read `R4-G1.md`
lines 160–176 and the §2 bullet (main:128–131). Three corrections, all checkable:

1. **The human-relevant density is where Day's direction holds.** R4-G1's own line 174: "157,000
   loci over a genome of about 35 M is about 4,500 loci/M, **between the two tight maps**" — i.e.
   between 1,000 loci/M (pair ratio **0.842 ± 0.020**) and 10,000 loci/M (**0.652 ± 0.018**), both
   sub-multiplicative, Day's direction. The same line calls free recombination "optimistic for
   humans at high concurrency". Citing the free row as "on their side of it" without the human
   density is a selective use of the audit's own run.
2. **The pre-registered linkage row did not show interference.** R4-G1 records "Pre-registered
   prediction failed at 1 M … 1.015 ± 0.022", and labels the 0.05 M and 0.005 M rows **post-hoc**.
   The write-up quotes 0.84 / 0.65 without the post-hoc label (hard rule 5 bookkeeping, and here
   the unlabelled post hoc numbers happen to run *for* Day — the label is owed either way).
3. **The bullet does not assert what the statistic tests.** §2 says "a beneficial mutation that
   arises in one individual **stays linked to that individual's entire genome**" — a statement
   about linkage retention and hitchhiking throughput in a clonal sweep, which is textbook-true.
   R4-G1's pairwise joint-fixation ratio tests a different proposition (whether two *separately
   arising* beneficials fix jointly above or below p²). Scoring the bullet with a statistic of the
   audit's choosing, rather than the one the bullet states, is the kind of substitution hard rule 1
   exists to catch.
4. **3.0 already internalises clonal interference.** It appears at main:13, 43, 65, 109, 272, 378,
   573, 689 and addendum:35 ("a demonstration of what clonal interference does to fixation counts
   … it reverses them"), and §9 states the conclusion the panel's objection is supposed to attack:
   "fixation is bottlenecked by sweep dynamics, not mutation supply". The paper's claim is a
   measured net throughput that already nets interference out, not a theoretical claim that
   clonality maximises pairwise joint fixation. So the panel's recombination point is *adjacent*
   (as graded) and is also, on this premise, answered in advance in the text.

**Fix:** rewrite the refinement to state both directions — the free-recombination row (1.03 ± 0.02)
is the critics' half; the human-density rows (0.84 / 0.65, post hoc) are Day's half; §2's bullet
states linkage retention, which is not what the ratio measures; 3.0 discusses clonal interference
in nine places.

**What this costs Day.** R4-G1 line 173 stands and must stay: "a clonal-derived rate is plausibly a
**lower** bound for a recombining population", and the clonal row's joint fixation is 0. If the
LTEE rate is a floor rather than a ceiling for recombining humans, the "most generous possible
assumption" framing at §8.6 is weakened. That is the critics' strongest form of this objection and
the write-up is right to record it.

### MAJOR-3 — every unapplied proposal in "Open" runs against Day; two symmetric items were available
"Open" items 1–3 are: Ge `external` → `contested`; a new critic-side node; a defeater pair against
§2's bullet. All three, if applied, worsen a Day node. The pass found Day-side material of the same
kind and left it unrecorded:

- **A5h's Responses still reads "In support: none located."** This pass located, for the first
  time, external material bearing on the conclusion's *direction*: the critics' own standard-theory
  formula (GGR-34, Haldane 1937 / Muller 1950) applied to A5h's corrected U = 384. The field
  correctly stays `pending` under the registered criterion (band 2b licenses nothing else), but the
  Responses line is now inaccurate as written, and the asymmetry is visible: a critic objection
  that fails the criterion is still added to Responses, while supporting material that fails the
  same criterion is not.
- **A4d's Responses has no entry for the panel's own narration.** t=01:49:52 (GGR-11's turn) says
  of 3.0 "He kind of throws the D coefficient off to the side", and the panel's summary of 3.0 at
  t=01:48:29–01:50:32 nowhere mentions d in the generation count. That is a **critic-side
  corroboration of A4d's central fact**, from a hostile source, and it belongs in A4d's Responses
  (In support), not only in a reading argument the correctness review proposes to delete (see
  NOTE-2).
- **No Day-side defeater is proposed** although the pass establishes one: Q4 shows the Bernoulli
  Barrier is absent from 3.0, so the panel's GGR-41..GGR-44 replies, and branch G's attacks
  generally, do not reach the headline argument of the current paper. The write-up states this
  ("Note on the target") but routes only the critic-side defeater pair to `defeaters.yaml`.

**Fix:** add the three items to "Open" (two Responses corrections and one Day-side defeater
proposal), no field moves. None of them requires a band that was not registered, because none of
them moves a verdict field.

### MAJOR-4 — the correctness review's MINOR-5 "correction" is itself wrong; do not apply it
`REVIEW-R4-VID-01-score-correctness.md` MINOR-5 and its "Wrong numbers" table say the write-up's
"free recombination … 1.03 ± 0.02 × p²" should be the "measured free-recombination pair ratio
**1.015 ± 0.022**", and that 1.03 is "the dispersion index". Reading `R4-G1.md` line 160–166, the
columns are `Recombination | Reps | P_fix ÷ Kimura | Dispersion of K | P(specified pair)/p² |
P(triple)/p³`, and the rows are:

```
 free              4000   1.019   1.029   1.029 ± 0.022   1.04 ± 0.08
 linked 1 M …      4000   1.002   1.015   1.015 ± 0.022   1.01 ± 0.07
```

The free row's **pair ratio** is 1.029 ± 0.022 — the write-up's "1.03 ± 0.02" is correct as cited.
1.015 ± 0.022 is the **linked 1 M** pair ratio, not the free one; the two numbers coincide with
their own dispersion indices, which is what the correctness review appears to have tripped on.
**Fix:** decline MINOR-5's substitution. If a tightening is wanted, cite "R4-G1 free-recombination
row, 1.029 ± 0.022"; do not write 1.015 into the write-up or any claim file.

## MINOR

### MINOR-1 — the "load occurs 0 times" rebuttal is weaker than the write-up weights it (against Day)
Q2 and A5h's Weaknesses line give first place among the costs to the critics to: GGR-33's premise
"is an attribution the source does not carry; the word 'load' occurs zero times". Under rule C the
most defensible reading of GGR-33 is about the *quantity* ("This is supposed to be a genetic load
that he's **calculating**"), not about Day's vocabulary; §6.4 computes an individual's fitness from
its deleterious-mutation count, which is the quantity load theory handles. A word count does not
answer a conceptual attribution, and leading with it invites the symmetric charge the audit makes
against Day (literal-fact-checking the wrong object, rule RH5).
**Fix:** keep the verified fact (it is useful, and it disposes of "*the* genetic load calculation"
as a claim about Day's text), but demote it below cost (ii), which is the one that bites.

### MINOR-2 — "clean of the d coefficient by an exhaustive token search" is broader than what was tested
A token search is exhaustive over tokens, not over the concept. The one occurrence of "effective
generations" (main:653) is a d-dependent unit imported by citation, and the search did not and
could not reach *Day and Athos 2025*, Appendix D, which is not in the corpus. The narrow claim is
fully supported and is the one A4d's Formal statement needs: **3.0's own generation count is
252,000, uncut, used uncut everywhere including §8.6.**
**Fix:** in the write-up's "For Day" bullet and in A4d, replace "clean of the d coefficient" with
the narrow claim plus "the cited §8.6 rate is expressed in Bio-Cycle 'effective generations' and
its own appendix is outside the fetched corpus".

### MINOR-3 — the GGR-04 credit is stated more broadly than the quote, which puts it at risk
Q5 says "The panel's mathematician **checked Day's arithmetic at this step and found it correct**".
GGR-01 is from the **same caption chunk** (t=01:06:15): Day "is off by his multiplication of three
numbers by a factor of 10". The credit is for the division — the core MITTENS F_max step — and
stating it that precisely makes it unassailable; stating it as "his arithmetic" makes it easy to
strike. The governing literal reading under R-4 and RD is correctly applied (under the bathos
reading the sentence asserts nothing, so it cannot be the more defensible reading); no change
there.
**Fix:** "the panel's mathematician concedes the division at the core MITTENS step is done
correctly (GGR-04), while flagging a separate 10× multiplication slip (GGR-01, same chunk)".

### MINOR-4 — the Ge `external` → `contested` proposal would double-count G's verdict
The second clause of Ge's Statement ("both of them remain entirely correct") is a claim *about* G,
whose `external` is already `contested`, and the proposal's own stated ground is that it "inherits"
that. Recording `contested` at both G and Ge adds a second contested verdict against Day for one
contested proposition, in counts (HANDOFF, README, argmap) that do not distinguish inherited from
independent verdicts.
**Fix:** either decline the proposal, or apply it with an explicit `inherited-from: G` note and
exclude it from independent verdict counts. The integration task should not apply it silently.

### MINOR-5 — a fourth credit candidate was not harvested, and it bears on a live premise
At t=01:39:30 a panellist reads, from the AI peer review of MITTENS that the panel itself calls
fair (GGR-45) and whose five numbered points Dr Hancock endorses at t=01:38:50 ("these are the five
things that I probably would have said as well"): "**The closest thing to a fair point is that the
adaptive fraction is the legitimate open empirical question and the sweep based estimates can vary
a lot.**" No GGR id covers t=01:39:00–01:40:00. It bears on branch A/G (what fraction of the
410M differences were adaptive), which is the premise Day's shortfall rests on.
**Fix:** flag for the harvest (not for this pass, which may not write `quotes-critics.md`) with its
limiting frame intact — it is the AI review's wording, read aloud, and the same sentence says the
argument "collapses into a much weaker claim" and supports "more research, not the conclusion that
natural selection is mathematically impossible". Recorded as a *half* credit, which is what it is.

## NOTE

- **NOTE-1 — Ge `internal: holds` is better supported than the write-up's token count, and the
  correctness review's two-gloss worry (its MAJOR-4) resolves in Day's favour under both glosses.**
  Under gloss (i) (a named argument) the token search decides, and `polygenic` is 0. Under gloss
  (ii) (Day's ¶22, "the math is an average of 12 different populations") the addendum is positive
  evidence of *omission by replacement*: it is titled "Per-Population Dispersion and Best-Case
  Robustness", reports each population separately, and says at §3 (add:83–84) "**These are not
  averages. They are the best data point in each category, chosen to be as generous as possible to
  the standard model**", then gives the best-case shortfalls (717,000× at Ara+4; 35,277× at the
  best mutator). Day did not merely delete the Averaging Problem; he replaced it with a
  per-population analysis that makes the objection moot — which is exactly what the Ge Statement
  says ("renders those complicating elements moot to such an extent that I omitted both"). On the
  §1 clause: it narrates the polythesis's "characteristic rhetorical structure" in the past tense
  of a dialectic, deploys nothing (no p^n, no number, no derivation anywhere in the paper), and
  "parallel fixation" is handled empirically 13 times over. Rule C is not even strained.
  **Suggested addition, not a correction:** cite add:83–84 in Ge's R4 paragraph.
- **NOTE-2 — partial disagreement with correctness MAJOR-1/MAJOR-2.** On the attribution the
  correctness review is right: GGR-11 is `panel`, no name is spoken in that turn, and "the host's
  own narration" overstates it (the wording originates in `quotes-critics.md`'s GGR-13 note, which
  is outside this pass's file list, so the write-up and A4d can be fixed but the quotes file is an
  integration item). On the remedy it is wrong to say "**delete** the claim that the narration
  corroborates": the narration corroborates **A4d's fact** (3.0 drops d) from a hostile source,
  whatever it shows about the referent of GGR-13. Re-label, do not delete — and see MAJOR-3, which
  asks for it in A4d's Responses.
- **NOTE-3 — on correctness MAJOR-3 (RD's extended-reading bullet).** Day's side has an honest
  answer: the ambiguous object is a word *in the quote*. The same speaker says "**Mittens 3.0**"
  when he means 3.0 (t=01:48:29 "the arguments that show up in Mittens 3.0"; t=01:49:52 "In mittens
  3.0, he completely retracts…") and GGR-13 says "in mittens". A reading of an ambiguous
  designator in the quoted words is a reading, not an extension. **But Day's position does not
  depend on winning that argument**: if the lead rules (a) an extended reading, the in-scope
  readings are (b) and (c), and with MAJOR-1 applied both grade the quoted statement
  **contradicted**. The headline changes from "the charge is not about 3.0" to "the charge is false
  of 3.0", which is no weaker for Day. The lead should not read Day's side as needing (a).
- **NOTE-4 — the Q2 strengthening claim should name its regime.** e^−U = e^−384 ≈ 1.70e−167 is the
  mutation–selection-balance mean fitness of a lineage that keeps the supermutator allele, not the
  one-generation fitness of a first-generation carrier (under Day's own multiplicative model that
  carrier is 0.999^384 = 0.681 at s = 0.001). Relativised to wild type (U ≈ 3.84, e^−3.84 = 0.0215)
  the equilibrium ratio is e^−380 = 9.29e−166, so the direction survives relativisation and the
  write-up's conclusion stands; stating the regime makes it unanswerable rather than arguable.
- **NOTE-5 — hard rule 1 prominence is satisfied at Q5.** The three credits are in the body with
  reasons, the "For Day" list carries six items against the "For the critics" seven, and the
  audit's own errors are listed separately rather than netted against either side. The registered
  Q5 prediction (≥1 credit bears on a Responses section) is a genuine hit: GGR-46 is in A4d's
  Responses in the committed file.
- **NOTE-6 — recomputed with no finding.** Both PDF sha256s (re-run by me), `252,000` 10× and never
  multiplied, `450,000` / `225,000` / `202,500` / `0.45` / `d=` 0, `turnover` 1 (main:274, "not
  gross turnover"), `Bernoulli` exactly 1 (main:55), `Averaging` / `law of large numbers` 0,
  `load` 0, `effective generations` 1, GGR-04/11/13/14/45/46 verbatim in the transcript at their
  `t=` chunks, 252,000/27,600 = 9.13, 113,400/27,600 = 4.11, 0.999^384 = 0.681, e^−380 = 9.29e−166.
  No hard-rule problem: nothing from `sources/raw/` is quoted here beyond short passages, nothing
  executed, no workhorse use.

---

## Summary for the lead

Day's side comes out of this pass **better than the write-up states**, by one grade at Q1 (MAJOR-1)
and by a corrected use of the audit's own run at Q3 (MAJOR-2), and it is owed two Responses
corrections and one defeater proposal for symmetry (MAJOR-3). No verdict field moves on this
reading of the evidence, and none should: A4d `holds`, A5h `arithmetic-error` / `pending`, Ge
`holds` are all right. The honest costs to Day are the §8.6 unit mismatch and the unexplained
retirement of d (MAJOR-1, MINOR-2), the weakness of the "load occurs 0 times" rebuttal (MINOR-1),
and R4-G1's clonal-floor observation (MAJOR-2). One finding is against the correctness review and
must be resolved before the fix pass runs (MAJOR-4).
