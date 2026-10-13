# Brief O5-reviews (reviewer): the six reviews that bring B internal and A2e external back

Lead: Big Sim. Written 2026-10-13, before the tasks were created (MA-21).
Skill to load: `.claude/skills/review-check/SKILL.md`.
Authority: owner decision **D-21** of 2026-10-13: "Put them back to `pending` until three
reviews are done".

## What is being reviewed

Both fields are `pending` as of the O5-revert pass. Three reviews each, six in all, each
its own task, each its own file. Under the cap of one agent (D-22) they run **one after
another**, not in parallel.

| # | Target | Review | File |
|---|---|---|---|
| 1 | B internal | correctness | `REVIEW-R4-B-internal-correctness-2.md` |
| 2 | B internal | steelman-day | `REVIEW-R4-B-internal-steelman-day.md` |
| 3 | B internal | steelman-critic | `REVIEW-R4-B-internal-steelman-critic.md` |
| 4 | A2e external | correctness | `REVIEW-R4-A2e-external-correctness-2.md` |
| 5 | A2e external | steelman-day | `REVIEW-R4-A2e-external-steelman-day.md` |
| 6 | A2e external | steelman-critic | `REVIEW-R4-A2e-external-steelman-critic.md` |

The question in each case is **not** "is the superseded value correct?" but the tier
question the single review never answered: does the evidence on record carry the field to
that value, under rule C (most charitable defensible reading), rule RD (every plausible
reading recorded) and the scoping the file states?

- **B internal** was `non-sequitur` on the N2b argument within Hard Limits, with reading F
  (flux fill 0.697) recorded alongside as `holds`, scoped to the B2 statement. The 2026-02
  blog quote predates Hard Limits by seven months and is not answerable to it.
- **A2e external** was `contradicted`, scoped to the per-generation count of adaptive
  coding fixations of any effect size on model-inferred alpha, resting on Uricchio 2019's
  lower 95% HPD with a 25% charity haircut. The strong-only and fitness-weighted readings
  stayed `contested`. Note that the scoping itself was accepted by the owner in D-12; the
  scoping is not reopened, only whether the evidence carries the value inside it.

## Rules for the reviewer

- You write **only your own review file**. You do not touch the claim file, the ledgers or
  `QUEUE.md`. You do not set a verdict; you say what the evidence carries.
- Severity labels as standing: BLOCKER / MAJOR / MINOR, each with the file and line it
  attaches to.
- A steelman review argues **one side as hard as it can be argued honestly**, and says so
  in its first line. Do not hedge to the middle.
- Where the Day-side and critic-side steelman conflict, **the lead rules** (owner,
  2026-10-13, D-24) and writes the ruling into the brief before the fix pass. Your job is
  to make your side's best case, not to pre-settle the conflict.
- You are a fresh instance with no memory of the authoring run. Do not go looking for the
  other reviews of the same field; if you have already written one of the six, say so.
- Token budget: grep by id, never read the big files whole. Report ≤ 300 words.

## What the lead already suspects

Stated here deliberately, because O-26's sub-question on whether briefs may name the
lead's suspicions is **still open** and until it is answered the standing practice is to
name them in the brief where they exist, so that they are on record rather than steering
the review silently:

- For A2e: the 25% charity haircut on N2 and the choice of the lower HPD rather than the
  point estimate are the two steps a Day-side steelman should attack hardest.
- For B: whether the 2026-02 blog sentence and the Hard Limits abstract sentence can carry
  one internal field at all, or whether the field is being set by the one of the two that
  suits the result.

## Deliverable per task

One review file, committed, named above. Then stop. The fix pass and any move off
`pending` are separate tasks and need all three reviews of that field in hand.

---

# Addendum: lead rulings before the fix pass (Big Sim, 2026-10-13)

Written under D-24 ("Me, the lead") and committed **before** any fix pass starts, per
lifecycle step 4. The three reviews of each field are in hand:

- B internal: `REVIEW-R4-B-internal-correctness-2.md` (124ce23), `-steelman-day.md`
  (f5104a4), `-steelman-critic.md` (f66ce55).
- A2e external: `REVIEW-R4-A2e-external-correctness-2.md` (2662fed), `-steelman-day.md`
  (2897d2f), `-steelman-critic.md` (5258b36).

Neither field moves off `pending` on this commit. These rulings tell the fix pass what to
write; each field moves only after the fix pass answers every MAJOR and MINOR **and** a
fresh reviewer has checked the ruling itself, which D-24 requires because both rulings
change the governing reading of a verdict field.

## Part 1. B internal

### B-R1. The completion reading is admitted and must be in the Readings table.
Two reviewers reached it independently (correctness MINOR-4; critic MAJOR-1): read "the
pipe that would finish them never fills" with HL's own domain sentence ("k = μ holds only
once the fixation-time distribution has filled across its support"), "fills" means
reaching the k = μ steady state. On that reading the clause is literally true on HL's own
inputs in every window (F = 0.697, 0.676, 0.281, 0.025, all < 1). Rule RD requires every
plausible reading to be recorded; this one is absent. Add it, tag `dialectic`.

### B-R2. Q157 is adopted as a B Statement quote. Q158 is not, and cannot set B's field.
The field has been resting on a quote the claim file still calls "**Candidate** Statement"
(all three reviews flag this). I adopt Q157 as a Statement quote of B, by this ruling,
dated 2026-10-13, recorded as the lead's decision and not reconstructed from a commit.
Q158 ("the pipe was nearly empty") is **not** quoted in B's Statement block and is not
adopted. Consequences the fix pass must carry:
- the literal band is applied to **Q157's own words** ("never fills"), not to the pooled
  phrase "never fills / nearly empty" that `R4-RHclose.md` l.70 scored;
- Q158 may be cited as context for a reading, but no verdict may be set from its wording;
- claim file l.29 and l.32 are brought into line (correctness MAJOR-3, Day-side F4).

### B-R3. No reading carries a verdict without its own N2b derivation.
All three reviews agree the N2b premise was derived once, for F over 6.5 My, and then
carried to four readings. The fix pass writes one derivation per row, each naming the HL
line that excludes that reading's premise, or records "N2b not shown".
- **D (delivered share)**: N2b not shown. HL's own model at HL's own input gives D = 0.256;
  no cited HL text says more than 30% of μT was delivered. Also marked "cross-document
  measure (Q34, Z22903977)" — a later paper's quantity (critic MINOR-6, Day-side cost 4).
- **Takahata 1e5**: N2b not shown, and marked **not governing** (external input, N1).
  "Takahata" does not occur in HL; the internal field asks whether HL's conclusion follows
  from HL's own premises (Day-side F5; uncontested by the critic side).
- **2 My**: the non-sequitur is real but the cited excluded premise is wrong. The excluded
  premise is the *window*: HL accepts 6.5 My ("The objection is valid, the correction
  triples the ceiling"). The row must also record HL's own contrary usage at l.416
  ("thirty-five percent fill across two million years even when granted the entire
  lineage"), which is HL's ambiguity, not the audit's (critic NOTE-10). **Not governing**:
  a reading that needs a window its own source gave up is not the "best supported" reading
  under D-15.

### B-R4. Reading S cannot govern Q157's field. This is the pivot, and it goes against the Day-side steelman.
The Day-side case is that under D-15 the governing reading is S (current size), which is
literally true because it is B2, and that the "non-sequitur at lineage level" given to S
scores a wider claim that RD l.202 bars. I rule against it, for one reason: **S is a
reading of Q158's "near end" framing, not a reading of Q157's sentence.** Q157 uses HL's
own defined term "inside the same lineage duration" (HL fixes it at roughly 6.5 My). A
reading that drops that clause is not a more charitable reading of the statement; it is a
reading of a different statement — and with B-R2 the statement it belongs to is not a B
Statement quote. The Day-side steelman's own cost item 3 concedes the point ("S is
narrow and fits Q157 less well than Q158"). D-15 chooses among readings of the quoted
statement; it does not license replacing the statement with a narrower one its author did
not make in that sentence.
What this ruling does **not** say: it does not say B2 is wrong (B2 `holds`, unchanged), and
it does not say the current-size confinement is unsupported. S is recorded as a reading of
Q158 with `holds` scoped to B2, marked "not governing for B internal (B-R2, B-R4)".

### B-R5. The governing reading is the completion reading, and under it the field is `non-sequitur`.
With S, D, 1e5 and 2 My non-governing or underived, the readings left on Q157's own words
are F (degree sense; F = 0.697 is 2.32x the 0.30 edge, so `rhetoric` under RH6) and C (the
completion sense, B-R1). Under D-15 ("closest to literally true, best supported") C
governs: the clause is literally true on HL's inputs in every window, and HL's own domain
sentence supplies the sense. Under C the clause is true, so the field turns on the
inference Q157 draws from it — "cannot be finished", "the neutral channel closes", "both
shut inside the same lineage duration". HL's own text excludes that inference: a partly
loaded pipe finishes a fraction, and HL says so of hominids specifically ("a partly-loaded
pipe", "partly-filled pipe inherited from a lower-census past", "loaded, at least
partially", and Q151's "completions of mutations that entered the pipe long ago"). That is
N2b, derived on this reading and for this reading. **Field: `non-sequitur`.**

This lands on the same value as the superseded one, on a different and now-derived basis.
The old basis — the pooled "nearly empty" band, and one derivation carried to four rows —
does not survive these reviews and must not be restated.

### B-R6. Any surviving rhetoric reading gives `n/a`, not `holds`.
Like for like with C7, which went rhetoric and from `non-sequitur` to `n/a` with its core
scored at C (critic MINOR-3). B under rhetoric is `n/a` (core at B2 `holds`; the lineage
conclusion: "no dialectical support offered", RH3). The bare "recorded alongside: holds"
comes out of the field comment.

### B-R7. Accepted without further argument (fix pass carries them out).
2.32x not 2.25x; F at 2 My is 0.025 not 0.026; quote 1 is excluded on **RH2**, not SC, and
RH-10 is extended to cover its second sentence with "revised in HL" kept as a versions
note; the missing Readings rows (Yoo 1.98e5; sourced field N_e) are added; the g
sensitivity on the 1e5 row (F 0.447 at g 20, 0.187 at g 29) is recorded; the aggregation
rule (NOTE-12) is stated: an internal field takes the governing reading of the Statement
quote that asserts the node's own claim, and other Statement quotes are reported with
their own verdicts.

### B-R8. Bookkeeping consequence, flagged not applied.
If B-R5 holds after the fresh-reviewer check, B internal has the same value under every
derived reading and stops being reading-dependent in value. That changes the
reading-dependent counts in `HANDOFF.md`, `arguments/README.md` and the argmap README —
the same counts the public board already shows disagreeing (7 against 15). Do not change
any count in the fix pass; it is one bookkeeping task after integration.

### B-R9. What would overturn B-R5.
A plausible reading of Q157's own words under which the clause is true **and** the
inference follows; or HL text that makes the completion sense of "fills" implausible; or a
ruling by the owner that a narrower reading may replace the quoted statement (B-R4). The
fresh reviewer is asked to attack B-R4 and B-R5 in that order.

### B-R10. Recorded against this ruling.
Correctness NOTE-11 stands and is not hidden: the cleanest internal contradiction on
record is on the F reading, which RH6 tags rhetoric and so releases, while the readings
left dialectic are the ones where N2b was weakest. And critic NOTE-9: N2b penalises an
author for his own concessions. Both belong in the claim comment, not only here.

## Part 2. A2e external

The three reviews agree on the direction: inside the D-12 scope every bias-corrected,
human-branch estimate on record clears Day's own flip of 191, the lowest cell being 798
(4.2x) and the floor without the haircut 1,065 (5.6x). They disagree about the *basis* and
about how much weight the word `contradicted` can carry. The scoping is not reopened
(D-12).

### A-R1. The 25% haircut is withdrawn as a correction and as a "charity".
Both steelmen attacked it from opposite sides and reached the same place: the source's 25%
is BGS acting on the realised human rate, and 0.135 is already fitted under that model, so
applying 0.75 again either double-counts the effect or, on the other reading, is a required
correction and not a charity at all. Either way `R4-A2e-alpha.md` l.173 ("the 0.75 haircut
covers it either way") is wrong and comes out. **Basis becomes the lower 95% HPD on N2:
1,065 (5.6x).** The 798 row is kept as a further Day-favourable sensitivity, labelled "an
unsourced further 25% cut; the source's 25% is BGS acting on the realised rate".

### A-R2. The owner is told that the D-12 summary misdescribed the stack.
The summary that carried D-12 said "every Day-charitable choice stacked". One element of
that stack had no source behind it, and none of the adjustments Day would actually ask for
(model error; gene-set transfer) was in it. D-12 itself is not reopened — the scoping
stands and the correction raises the count rather than lowering it — but the owner gets the
correction in plain words, not a quiet edit.

### A-R3. N2 stays the verdict denominator; the paper's own base is reported beside it.
The critic side asks for the like-for-like own-base rows (2,873–4,040; 15–21x) to be the
basis. I rule against: P4 of the registration bars the own-count rows from the verdict, the
denominator is genuinely unreconciled, and N2 is the Day-favourable floor — using the
larger base would widen the stated margin in the audit's own favour on a number the record
cannot yet reconcile. The own-base rows are reported, with "unreconciled" replaced by
"larger gene set; the candidate gene-count scaling (unverified) puts N1–N3 below it", and
with the claim file and the Readings table quoting the **same** rows (correctness MINOR-1).

### A-R4. "Bias-corrected" is restored to the basis, and this is not a narrowing of the D-12 scope.
The correctness review put this to the lead. Ruling: naming the basis "bias-corrected
estimates" states which evidence carries the value; it does not change the scope, which
stays the per-generation count of adaptive coding fixations of any effect size on
model-inferred alpha. The field must name what it sets aside and why — Gayà-Vidal's 0.2%
(29–49), an uncorrected MK value its own authors flag as a possible underestimate, and
Eyre-Walker & Keightley, abstract only — rather than leaving a reader of the field to find
an in-scope estimate on Day's side of the flip with no explanation.

### A-R5. The value is `contradicted`, scoped, carried with an explicit certainty qualifier.
The Day-side steelman's MAJOR-3 asks for `contested, leaning contradicted` on the ground
that the move rests on one post hoc source, read before "registration", gathered with no
search strategy. I rule: the value is `contradicted` **inside the D-12 scope**, because
that word describes the direction and margin of the evidence on record, and the margin is
4.2x at its narrowest with no Day-favourable adjustment on record reaching 191. The process
weaknesses are real and go to certainty, so they are carried **in the field text**, not
only in the GRADE table: "single post hoc source for the HPD, in-model interval,
very-low GRADE certainty, evidence set gathered with no search strategy (AR-05)". A field
that states its own weakness is honest; a field that moves to `contested` because the
process was weak would misreport what the numbers say.

### A-R6. "Three estimators" becomes "two data sets, one model family".
Both steelmen and the correctness review make the same point: ABC-MK and aMK are the same
data in the same paper, and all of it is MK/SFS logic. `R4-A2e-alpha.md` l.165 and l.186
are corrected, and the 82% artefact share required at the lower HPD is recorded beside the
margin.

### A-R7. The registration is relabelled a reproduction.
Table 1, its HPDs and the counts were filed 33 minutes before the "pre-registration"
(a44767f) and are quoted in the docstring itself. P2–P5 and blockers (3)–(4) could not
have failed. The docstring is corrected in a post hoc commit, `PREREG-STATUS.md` l.98 is
changed to say only the milestone-13 trigger predates the table, and the claim comment
calls the move "a reproduction of a published interval against Day's own 191", not a
pre-registered test.

### A-R8. Accepted without further argument.
Boyko is "pooled over both lineages; lower CL 599 at a 50% human share, 299 (1.57x) at
25%"; the non-VIP gene-set sensitivity (0.09 → 998, 5.2x) is added; "posterior mean" and
"lower edge of the 95% HPD" replace "point estimate"; the strong-only row carries "marginal
interval; the strong and weak components are not separately identified, and the total
excludes 0"; the script's dead source path is pointed at a directory holding the registered
sha256 (both re-fetches match it); D6 ("model inference, not observed") is stated for both
sides of the inequality or dropped.

### A-R9. What would overturn A-R5.
A human-lineage, bias-corrected alpha whose upper bound is below about 1.72% on N2 (0.64%
on the paper's own base). None is on record and none was searched for; the structured
two-directional search stays open as RG-03 and is the one piece of work that could move
this field.

## Part 3. A correction that belongs to the owner, not to a fix pass

Three of the six reviews found the same thing independently (correctness MINOR-10,
Day-side F6, critic MINOR-3): the question put to the owner on 2026-10-13 said "Two
results moved in Day's favour on 2026-10-11", and D-21's effect column says "Both reverts
remove a Day-favourable value". That is wrong for both fields. B internal went
`holds` → `non-sequitur` and A2e external went `contested` → `contradicted`; both moves
were **against** Day, and both reverts removed a value unfavourable to him. (For B, the
Day-favourable step `pending` → `holds` existed for four minutes before D-15 superseded
it.) The owner's answer does not depend on the direction — the tier rule asks for three
reviews either way — so D-21 stands. But the premise as put was wrong, the lead put it,
and the owner is told rather than left with the record as it reads. `DECISIONS.md` carries
the correction.
