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

# Addendum 2: re-ruling on B internal after the D-24 fresh-reviewer check (Big Sim, 2026-10-14)

The D-24 safeguard did its job and it went against me. The fresh-reviewer check
`REVIEW-R4-B-internal-ruling-check.md` (ccdb989, EVO-73) returns **1 BLOCKER, 1 MAJOR,
2 MINOR, 3 NOTE** and finds that **B-R4's stated ground is false on HL's text**. I accept
it. These rulings supersede B-R4 and B-R5 as governing rulings. They are written before
the second fix pass, per D-24 and lifecycle step 4, and **no verdict field moves on this
commit**.

I checked the BLOCKER against the source myself rather than taking the review's word for
it. Local text `sources/raw/b-steelday-2026-10-13/hl.txt`, sha256 `3182a5b6…`, the same
hash the review used. I read l.95-99, l.126-136, l.245-258, l.350-366, l.436-442 and
l.450-462 directly.

### B-R11. B-R4 is withdrawn. Its ground is false.
B-R4 said a current-size reading "drops Q157's own defined term 'inside the same lineage
duration'" and is therefore a reading of a different statement. That is true of the
Day-side steelman's version of S ("near end", Q158). It is **not** true of the version the
correctness review had already put and the check calls **S_L**: *at the current census the
pipe cannot fill inside the lineage duration*. S_L keeps the term, in the sense HL itself
fixes for it:

- l.97-98: the criterion is `4 Nₑ < G`, "where G is the number of generations the lineage
  has been available";
- l.133-135: "Above the census X, a population is too large for a neutral allele to cross
  it by drift **in the time its lineage has existed**";
- l.247-253: "Use the lineage duration … roughly six and a half million years … The human
  ceiling rises … to about one hundred fourteen thousand. And then note that we are still
  eight billion strong, which puts us seventy-two thousand times over the enlarged
  ceiling."

l.247-253 is the only place HL introduces and applies "lineage duration", and it applies
it to **the census against the ceiling**. S_L is therefore not a narrower statement
substituted for Day's; it is Day's own computation. B-R4 reasoned from a reviewer's
concession (Day-side cost item 3) instead of from the source's own definitions. That is
the error the check names, and it is mine.

### B-R12. S_L is not an extended reading, so RD's last bullet does not bar it from setting the field.
This is the question B-R11 leaves open and it decides the field, so I rule on it
explicitly. RD l.202 bars "extended readings (a different object, or a wider claim)" from
setting the verdict field. S_L is neither:

- **Not wider.** S_L restricts the substitutions in question to those seeded at the current
  census. It claims less than the lineage-actual reading C, not more.
- **Not a different object.** Q157's own paragraph names S_L's inputs. l.456-461, running
  on from the quoted sentence without a break: "It takes Kimura's own fixation time,
  Wright's own effective size, and **the field's own census**, generation, and
  reproductive-variance figures, and it asks … how long is the pipe." Census, generation
  time and reproductive variance are the inputs of `X = (Vₖ + 2)·G/16` and of the census
  comparison, which is S_L. They are not the inputs of C.

RD bars extended readings because they let a speaker be credited for a claim he did not
make. A *narrowing* reading carries the mirror risk: crediting the speaker with a true but
weaker claim than the one doing the work in his argument. RD handles that risk with
scoping and RH3, not with exclusion — which is exactly what B-R14 does below.

### B-R13. Under D-15/RD the governing reading of Q157 is S_L, and the field is `holds`, scoped.
RD fixes the test: the field takes the reading under which **the quoted statement is most
defensible — closest to literally true, best supported** — and explicitly not the reading
that is most natural, nor the one best for the speaker.

- Under **S_L** the clause is literally true. At the census, Nₑ/G is of order 2e4, so
  F ≈ 0; HL's own form of it is 8 billion against a ceiling of 113,750, "seventy-two
  thousand times over" (l.251-253). The inference also follows on HL's own words: the
  closure vocabulary is used of the census regime and nowhere else — "the neutral
  substitutions these species exhibit today are not being seeded at their current size at
  all. The channel is not slow, **it is empty**" (l.353-354).
- Under **C** the clause is false in the governing window (B-R15).

So S_L is the most defensible reading and it governs. **Field: `holds`**, reading-dependent,
set on Q157 under S_L. This meets B-R9's first overturn condition, which I wrote as the
thing that would overturn B-R5, and it has been met.

I record plainly what this ruling costs: it moves B internal from the superseded
`non-sequitur` to `holds`, which is a **Day-favourable** move on a load-bearing internal
field, made by me, on the charity rule the owner approved on 2026-10-11. I could keep
`non-sequitur` only by ruling S_L implausible, and after reading HL myself I cannot: at
l.247-253 S_L is Day's own answer to the lineage objection, and at l.456-461 Q157's own
paragraph names its inputs. Ruling it implausible would be deciding the field first and
finding the reason afterwards, which is the thing this audit exists to catch.

### B-R14. The `holds` is never displayed bare, and the node-level claim takes RH3.
Conditions on B-R13, all mandatory for the fix pass:

- the value is written `holds` **scoped to the census ceiling at G = the lineage duration
  (B2's content)**, and the scope travels with it into every table, tally and board row;
- the Readings table records, not governing: **C** (lineage-actual, completion sense)
  `non-sequitur` on the B-R15 basis; **2 My** `non-sequitur`; **F** `n/a` (B-R6);
  **D**, **1e5**, **Yoo** "N2b not shown";
- B's own title claim — that neutral theory cannot rescue the shortfall over the lineage —
  is asserted by **no** governing reading, and takes RH3 "no dialectical support offered".
  S_L is a counterfactual about a census the species has held for about 400 generations
  (l.330) and says nothing about whether drift produced the observed divergence;
- HL's own drainage concession stays on the record beside it: "The small number of
  fixations we observe are just drainage: the completions of mutations that entered the
  pipe long ago" (l.354-356).

### B-R15. MAJOR-2 is accepted. B-R5's basis is withdrawn; its value under C survives on a corrected one.
"The clause is literally true on HL's inputs in every window" is **false** and must not be
restated. HL's operational test for filling is `4Nₑ < G` (l.97-98), and HL says of the
region below the ceiling that "fixation can, at least in theory, potentially complete"
(l.135) and "the only census population that fills the pipe in time is one too small to
sustain a viable species" (l.437-438). The hominid census of 1e5 is **below** HL's own X
(113,750 at 6.5 My; 110,250 at 6.3 My), x = 4.55 > 4. By HL's own criterion that pipe
fills, so "never fills" is false there. The clause is true under C only at 2 My, Yoo and
Takahata 1e5 — all non-governing rows. Under C the verdict stays `non-sequitur` on a
**stronger** basis: N2b now bites on the clause as well as on the inference.

### B-R16. MINOR-3 and MINOR-4 accepted.
MINOR-3: the 6.5 My exclusion is cited to k(T) = μF(T) (l.287-291), l.362-363, l.419 and
l.439-441. l.363-366 ("thirty-five percent — a partly-loaded pipe") is cited only a
fortiori, with HL's own disavowal of that linear bound (l.302, "an overstatement, and a
vast one") noted beside it. MINOR-4: B-R2 stands as written — Q157 adopted, Q158 refused —
but it is struck as a ground for anything about S_L, which does not rest on Q158.

### B-R17. NOTE-6: O-6 applies to the B-R7 aggregation rule.
"An internal field takes the governing reading of the Statement quote that asserts the
node's own claim" is new rule text, not an application of an existing rule. It therefore
goes through O-6: a written proposal, the 24-hour cooling-off, and a re-score of any
load-bearing verdict it moves. It moves nothing in B (every reading in play is of Q157),
so this re-ruling does not depend on it, but it may not be applied anywhere else until the
O-6 process has run. The fix pass states it as a **proposal**, not as a rule.

### B-R18. NOTE-7 accepted: B stays reading-dependent in value, so B-R8 does not arise.
The derived readings are now {`holds` (S_L), `non-sequitur` (C, 2 My), `n/a` (F)}. No
reading-dependent count changes. The 7-against-15 disagreement already on the public board
is untouched by this ruling and stays a separate bookkeeping item.

### B-R19. One more fresh-reviewer check, and then it stops.
D-24 asks for a fresh-reviewer check whenever a ruling changes the governing reading, and
this one does. But this ruling *adopts* a fresh reviewer's finding, so a further check
risks an unbounded regress of checks on checks. The bound: **one** check, scoped to two
questions and no others — (a) is S_L wrongly admitted, i.e. is B-R12's extended-reading
ruling wrong; (b) is the scoping in B-R14 sufficient to stop a bare `holds` travelling. If
it returns no BLOCKER, the fix pass and the integration proceed. If it returns a BLOCKER,
the field stays `pending` and the question goes to the owner, not to another reviewer.

## Addendum 3 (lead, 2026-10-14, release wake) — the scope cannot travel, and I verified it myself

### B-R20. The fix pass's finding 6g is correct, and it is wider than B.
EVO-80 reported that `lint_research.py` loads claim front matter with `yaml.safe_load`
(l.25-30), which discards YAML comments. I checked the file rather than take the report:
the parse is `yaml.safe_load(m.group(1))` on the front-matter block, and comments are gone
before any consumer sees them. Every scope this audit has ever written is a YAML inline
comment — A2e's `external: pending   # SUPERSEDED ... SCOPED ...` is the pattern. So:

- the scope on a verdict is **invisible** to `lint_research.py`, to `hierarchy.yaml` and to
  the public board; only the bare value travels;
- this is **not** specific to B. A2e external's certainty qualifier (A-R7) has the same gap,
  and so does every earlier scoped value on the board today.

B-R14's first condition — "the scope travels with it into every table, tally and board row"
— is therefore **not satisfiable with the present tooling**. B-R19(b) asks exactly this
question, and the honest answer available to me now is no.

### B-R21. The ruling: a machine-readable scope field, and a publication hold until it exists.
This is a tooling decision, not a verdict decision, so under D-28 it is mine.

1. Claim front matter gains a sibling map, `verdict_scope:`, keyed by field name
   (`internal`, `fidelity`, `external`), holding the one-line scope as data. The YAML
   comment stays as the long-form reasoning; the new field is what travels.
2. `lint_research.py` **errors** if a field's value is scoped in the comment but has no
   `verdict_scope` entry, and carries the entry into `hierarchy.yaml`.
3. The board renders the value and its scope together, or renders neither.
4. **Standing hold, effective now:** no board publication may show B internal or A2e
   external until (1)-(3) are in place. The board today shows both as `pending`, which is
   bare and correct, so nothing public is wrong at this moment and nothing must be pulled.
5. B internal's `holds` may **not** be integrated before this lands, independently of what
   the B-R19 check returns. A bare `holds` on a public page is a Day-favourable claim the
   audit does not make.

I am not waiting on the owner for this. It changes no verdict and publishes nothing; it
stops a publication that would have misstated one.
