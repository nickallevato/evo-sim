# Brief L5-reviews (reviewer): the two reviews L5 is missing under the new tier rule

Lead: Big Sim. Written 2026-10-13, before the tasks were created (MA-21).
Skill to load: `.claude/skills/review-check/SKILL.md`.
Authority: owner decision **D-23** of 2026-10-13, verbatim: "Three reviews" — a check that
is not marked load-bearing but whose registration carries a verdict-field flip, or whose
node is a listed feeder of a load-bearing node, gets three reviews. That supersedes D-16,
which had lowered L5's tier to one combined review after registration.

## Standing of this task

L5's pre-registered docstring asked for three reviews. On 2026-10-11 the tier was lowered
to one (D-16); the one that was done found 7 MAJOR and the C-external flip was withheld.
The owner's answer of 2026-10-13 restores three for exactly this case. **The lead reads
that as giving L5 its two missing reviews before the withheld flip can be integrated. The
owner was not asked that sub-question and may overrule it**; if he does, these two tasks
are dropped and nothing else changes.

## The two reviews

| # | Review | File |
|---|---|---|
| 1 | steelman-day | `REVIEW-R4-L5-steelman-day.md` |
| 2 | steelman-critic | `REVIEW-R4-L5-steelman-critic.md` |

The correctness review exists (the one with 7 MAJOR). Read it; do not redo it. Your job is
the side you are given, argued as hard as it can be argued honestly, on the write-up as it
now stands after its fix pass.

The live question behind both: the registered arithmetic excludes a Day-side outcome at
s ≤ 0.01 and allows one at s ≥ 0.03, and the C external `contested` → `contradicted` flip
was withheld on rule RD (an extended reading cannot set the field). Day side: is the
withheld flip rightly withheld, and is the s range the registration used fair to him?
Critic side: does the evidence carry the flip under the as-written reading, and was
withholding it over-cautious?

## Rules

- You write **only your own review file**. No claim file, no ledger, no `QUEUE.md`.
- BLOCKER / MAJOR / MINOR, each with file and line.
- First line says which side you are steelmanning.
- Conflicts between the two steelmen are ruled by **the lead** (D-24), who writes the
  ruling into the brief before any fix pass. Make your case; do not split the difference.
- One agent at a time (D-22): these two run one after another, not together.
- Report ≤ 300 words.

## After both

The flip stays withheld until the lead has ruled on the two steelmen and a fix pass has
answered every MAJOR and MINOR. Integration is a separate task.

---

# Addendum: lead ruling before the fix pass (Big Sim, 2026-10-13)

Under D-24, written and committed before any fix pass. Reviews in hand:
`results/REVIEW-R4-L5-steelman-day.md` (c2a92b4), `results/REVIEW-R4-L5-steelman-critic.md`
(12aa4f3), plus the earlier combined review `results/REVIEW-R4-L5-combined.md`.

This is the genuine split of the three O-5/L5 sets: the Day side holds that the withheld
C-external flip was rightly withheld; the critic side holds that withholding was
over-cautious and the field takes `contradicted` (scoped), with 6 MAJOR behind it. I rule
mostly for the critic side on the rules, and for the Day side on the wording of the scope.
**No field moves on this commit.** The flip is applied only after the fix pass, the
fresh-reviewer check D-24 requires, and the owner question in L-R6.

### L-R1. The weak-test caveat is not a ground for withholding (critic K-1 accepted).
The pre-run note registered the opposite: "That move stays a proposal for the three
reviews; the write-up reports the severity limit beside it", and the same item says the
caveat "does not weaken the low-s result itself". "Report beside it" became "withhold
because of it" after the result was seen. That is registered wording narrowed after the
fact, and it is the kind of move this audit exists to catch when Day does it. Reason 1 is
struck from `R4-L5.md` §8 and from claim C l.89. The severity limit stays, stated beside
the move as registered.

### L-R2. R-c cannot set the field (critic K-2 accepted).
R-c ("sweeps of unstated s") is not a fourth meaning of Q275. It is the undecided
disjunction of R-a/R-b (s low → `contradicted`, scoped) and R-d (s ≥ s* → `supported`,
which the same table marks extended and which RD bars from setting the field). Letting
R-c return `contested` puts R-d's verdict into the field through the back door that RD's
extended-reading bullet exists to close. A disjunction cannot carry a verdict that none of
its admissible disjuncts carries.

### L-R3. R-c is relabelled; R-e is the literal object (critic K-3 accepted, with its concession).
The post contains no "sweep", no "selection coefficient", no "beneficial", no "adaptive";
Q275's object is a substitution total, and claim C's own formal statement has said so since
2026-10-07, four days before L5 was registered. R-c is relabelled "plausible:
selection-driven reading from the post's framing; s unstated" — plausible it is, the
framing and Day's A6 passage support it, and the critic side concedes that. But it is not
"the literal state of the source", and that label is what made it look like the
conservative default. R-e is labelled "literal: the derivation's own object; claim C's
formal statement since 2026-10-07".

### L-R4. The field takes `contradicted`, scoped — with the Day side's narrowing.
Under R-e the Modern Synthesis's own expectation for the zero-reported statistics is zero,
equal to the observation, so Q276's comparative inference ("decisively favors the MITTENS
prediction over the Modern Synthesis expectation") is contradicted by external evidence
and not merely a non-sequitur. Under R-a and R-b it fails too. But the critic side's
proposed scope wording says more than the run shows, and the Day side's S2 is right about
why: at Day's own 20-year clock his **reported M10** (1 and 3 changes) already excludes the
required rate at s = 0.01 standing/const, and at 25 y at s = 0.02. So the scope names the
statistics and the clock:

> `contradicted` — scoped: the inference from the zero-reported statistics to a refuted
> required rate fails for s ≤ 1e-2 at Day's current 25-year generation, including his only
> stated s for a fixation (1e-3, Q44) and the comparator as derived (a genome-wide
> new-mutation substitution count, the formal statement). The observation stands. Day's
> reported M10 is not in this scope and does bite: on the validated design it excludes the
> required rate at s = 0.02 (standing, 25 y, reference cell) and at s = 0.01 (standing,
> const, 20 y). Other scopes: selection-driven reading, s unstated (R-c), contested; s ≥ s*
> (R-d), supported, extended.

"At low s Day's data neither show nor exclude the required rate on any of his statistics"
(`R4-L5.md` l.182, l.331) is false as written and is corrected to name the statistics and
the clock.

### L-R5. Reading-dependence: SCOPED, not reading-dependent (critic K-4 accepted).
RD's own clause — a claim whose formal statement fixes the reading is `SCOPED` — applies
here, because claim C's formal statement fixed the comparator before the run. The
reading-dependent count does not rise. The A2e precedent is cited for the *logic* only;
A2e's own field is `pending` under D-21 and nothing here depends on its value.

### L-R6. One question goes to the owner, and it is not mine to answer.
The registration attached an owner decision to the MIDDLE wording: "owner decision whether
Day's model implies s ≥ s* (his own beneficial s input is 1e-3)". `DECISIONS.md` has no
such decision; the fix pass and integration answered it themselves with "s unstated".
D-24 gives the lead steelman conflicts, not registered owner questions. So the question is
put to the owner as registered. Under L-R2 it no longer sets the field, but an owner who
holds that R-c governs would keep C external at `contested`, and that is his to say.
**Integration waits on this answer.** Everything else in the fix pass does not.

### L-R7. Day-side findings accepted in full.
S3 (the scoreboard's Day "miss" and critic "hit" were both fixed by the registration's own
P3 arithmetic, and the Day band is the audit's construction because Day states no s — both
rows carry the qualifier); S4 (printed crossovers are grid **ceilings** and V3 pushes them
up — write "s* ≤ 0.05 (between 0.03 and 0.05 on B10)", and "20 y (Day 2019)" rather than
"his own 20-year generation", since his current value is 25 y); S5 (one stated criterion
for "plausible", applied to R-a, R-b and R-d alike); S6 (Day's corpus has a second
beneficial s, 0.01, Q26 note on Z18167588 s7.8 — this helps R-b and is recorded because
the corpus must be stated accurately in both directions); S7 (the non-independence caveat
extends to low s: ~110,000 concurrent sweeps at s = 0.01 and ~1.1e6 at s = 0.001, against
Day's own "approximately 230 simultaneous sweeps", so R-a/R-b's "zero is what the required
rate itself predicts" carries "if the rate is attainable at that s as independent sweeps,
which L5 does not test"); S9 (call it "the required rate Day attributes to the Modern
Synthesis" at first use).

### L-R8. The C1a Readings table (S8) — the one point the Day side wins outright on substance.
Rule RD requires every plausible reading recorded, and C1a has four with no table. The fix
pass writes it. On which reading is most defensible, the Day-side reviewer is right:
reading (i), "not obscure", read absolutely, is the clause that answers the critics' own
"the panel obscures fixations", and on it L5 found **Day's sign** for strong sweeps, as did
the audit's own missed predictions P4 and P5. Record (i) as the governing reading of that
clause, with (ii) supported, (iii) wrong, (iv) not computed. The separate C1a random-SNP
comparator task stands.

### L-R9. Recorded against this ruling.
Critic K-9: the critics' registered mechanism was half wrong — only the window-length half
held, and the audit's own two-order error had flattered the ascertainment half. K-10: the
scope must stay s ≤ 1e-2 for the zero statistics, and the blog's relaxed ">50 percentage
points" statistic was never modelled. K-11: integration touches claim C's field and
comment, the reading-dependent counts and defeaters d467–d469. And the Day side's S1(a),
which no fix pass should drop: under R-a the audit imports s = 1e-3 from an argument in
which Day uses it to show a fixation takes ~19,800 generations — in his own frame the
required rate at that s is unattainable, not invisible.

### L-R10. What would overturn L-R4.
A source that gives the 15,556 an s, or an owner ruling that R-c governs (L-R6), or HL-side
evidence that claim C's formal statement does not fix the comparator. The fresh reviewer is
asked to attack L-R2 and L-R4 in that order.
