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

---

## Addendum 2 (L-R11 to L-R16): the lead answers the question L-R6 sent to the owner

Written 2026-10-14 after the D-24 fresh-reviewer check (EVO-75, `7471d60`) and after the
owner's reply on the EVO-1 question card, resolved 2026-10-14 01:34 UTC. The owner's answer,
verbatim:

> "if you need to ask me then you need to decide or leave it open and / or explore both
> possible sides or interrpetations"

That is a standing instruction, recorded as **D-28**. It withdraws the premise of L-R6:
a registered "owner decision" is not a reason to stop. The lead decides, or records both
readings and lets neither set the field. **No verdict field moves on this commit.**

### L-R11. L-R6 is withdrawn. The question is answered here, and the answer is no.
The registered question (docstring l.124-125) is "owner decision whether Day's model implies
s >= s\* (his own beneficial s input is 1e-3)", where s\* <= 0.05 on B10 at 25 y and 0.03 at
20 y (L-R7/S4). Equivalently, under the plausibility criterion of L-R7 ("an s given by Day,
or by the mainstream model the comparator stands for"): is R-d — s >= s\* for all 15,556
substitutions per window — a plausible reading of Q275?

**Ruling: no.** Three grounds, each from the record as it already stands:

1. **Day gives the 15,556 no s, and both s values he does give are below s\*.** Q44 is
   s = 1e-3 (`R4-L5.md` l.5); the second is 0.01 (Q26 note on Z18167588 s7.8, L-R7/S6).
   s\* is 0.03 to 0.05. No quote in the corpus attaches any s to the comparator.
2. **The mainstream model the comparator stands for supplies a strong class, but not for
   the 15,556.** The remapped strong class is 28% of F_ii = 4.489, i.e. about **1.26
   substitutions per window** under an ASSUMED mapping (EVO-75 recomputation table, row 11),
   against the 15,556 R-d needs. A strong class covering 0.008% of the required count does
   not make "all 15,556 are strong" a reading the model gives.
3. **R-d contradicts a figure Day states himself.** R-d needs the 15,556 to complete as
   strong sweeps inside 280 generations: about **28,000 concurrent sweeps at s >= 0.05**
   (`R4-L5.md` section 11 item 7, registered as review C10), rising as 1/s to roughly 37,000
   at s = 0.03. Day's own pipeline figure is "**approximately 230 simultaneous sweeps**"
   (Q25, derived at s = 0.01: Q26, Q27). R-d is therefore not merely unsupported in Day's
   corpus; it is about **100 to 160 times** a number he publishes. `R4-L5.md` l.385 already
   says it: that reading "is one no source holds; 15,556 concurrent strong sweeps are
   outside the regime of the model that produced the number."

### L-R12. The strongest case for "yes", and why it does not carry.
It deserves stating, because it is the better argument and it nearly persuaded me. Day's
**test** is ancient-DNA sweep detection. That test can only bite if the substitutions it
looks for are strong enough to leave a signature; at the s values Day states it has no power
(the audit's own finding: <= 5.9e-16 at s <= 0.01). So Day's *argument* needs s >= s\* to be
non-vacuous, and a reading on which his argument works is the one a charitable reader should
take. On that reading the field would be `supported`, not `contradicted` — this is the whole
of what a "yes" is worth, and it is worth a lot.

It does not carry, for two reasons.

- **It is charity to the arguer, which rule RD excludes in terms.** RD takes "the reading
  under which the speaker's *quoted statement* is most defensible … **It is not the reading
  that yields the best verdict for the speaker.**" The "yes" case reasons from what Day's
  conclusion requires back to what his premise must have been. That is the inference RD's
  second sentence forbids, and the lead applied the first sentence against Day in L-R1 on
  this same check. It cannot be applied in his favour here on the opposite ground.
- **It is self-defeating as a defence.** Adopting it concedes that at every s Day states,
  his own evidence shows nothing, and buys `supported` only with a premise that conflicts
  with his Q25 figure by two orders of magnitude. A defence that trades a stated figure for
  an unstated one is not a stronger reading of the statement; it is a different statement.

**This ruling is the one that keeps me honest in both directions.** In B internal I admitted
a Day-favourable reading (S\_L) because Day's own text supplied it, against my own earlier
ruling. The test is the same here and gives the opposite answer for the same reason: S\_L was
in Day's text at HL l.247-253; s >= s\* for the 15,556 is in no text, and collides with Q25.
Supplied by the source, admitted; required by the conclusion, refused.

### L-R13. R-d is not buried. It is recorded with its verdict, as RD requires.
"No" means R-d does not set the field. Under RD every plausible reading is recorded with its
verdict and R-d stays in claim C's Readings table and comment as **s >= s\*, `supported`,
does not set the field (L-R11)**, with the three grounds above named in one line so a reader
can reopen it. The owner's "explore both possible sides" is met on the record, not by leaving
the field undecided: an undecided field would itself be a choice, and the one L-R2 shows is
unavailable, since `contested` smuggles R-d's verdict in through a disjunction.

**What would reopen it (replacing L-R10's second clause):** a quote in which Day attaches an
s at or above 0.03 to the comparator; or a mainstream source that puts the *bulk* of the
required substitutions in a strong class; or a resolution of Q25 showing "approximately 230
simultaneous sweeps" is not Day's figure for the comparator's regime.

### L-R14. L-R2 is re-grounded, as MAJOR-1 asks.
The fresh reviewer is right that RD's extended-reading bullet does not bar R-d: R-d fixes the
same unstated parameter as R-a and R-b and is not "a different object, or a wider claim"
(S5, accepted in L-R7). The clause in L-R2 citing that bar is **withdrawn**. L-R2's
conclusion stands on the ground the reviewer identifies and L-R11 now supplies: R-d fails the
plausibility criterion, so R-c's admissible disjuncts are R-a and R-b alone, both
`contradicted`, and the disjunction argument goes through. NOTE-14 is accepted: R-c is not
exactly R-a/R-b ∪ R-d — the gap at s = 0.02, and 0.03 to 0.05 in hard mode at 25 y, lies in
neither, and behaves like R-b (<= 9.6e-7 at 25 y). The fix pass states the gap rather than
the union.

### L-R15. L-R5 is corrected, not defended (MAJOR-2 accepted).
The reviewer is right and the ruling was wrong: claim C's formal statement fixes the
comparator's **object**, not its **s**, and s is the dimension in dispute. A2e's formal
statement named its own disputed dimension ("of any effect size"); C's does not, so RD's
`SCOPED` clause does not apply on the ground L-R5 gave. The reading-dependent count still
does not rise, but for a different and weaker reason: **every admissible reading (R-a, R-b,
R-e, and the s = 0.02 gap) returns `contradicted`**, so there is no dependence to report —
and that reason rests on L-R11, where L-R5's did not. The fix pass carries the corrected
wording and `R4-X1-verdict-rule.md`'s RD paragraph gains no new instance.

### L-R16. What moves now, and what still gates it.
The value L-R4 gave — `contradicted`, scoped — is unchanged by this addendum. Its chain is
now L-R11 → L-R14 → L-R15, not the chain L-R2 and L-R5 originally gave. L-R4's **wording**
does not survive the check: MAJOR-3 (the field word on a claim titled by the observation),
MINOR-4 (Z50/Z10 carry no inference in their source), MINOR-5 (the clock qualifier
understates — the zero holds at 20 y too), MINOR-6, MINOR-7, MINOR-8 (the x100 bracket rests
on an ASSUMED mapping; R-e is a reading, not an s, and takes its own clause), MINOR-9,
MINOR-11 are all accepted and go to the fix pass.

**Integration still does not fire on this commit.** The gate is no longer the owner question;
it is one bounded fresh-reviewer check of L-R11 to L-R15 alone — the D-24 safeguard, because
L-R11 decides the governing reading. That check is asked to attack L-R11 first, in the form
"is there any text in the corpus that attaches s >= 0.03 to the comparator, and is the Q25
figure read correctly?", and L-R15 second. If it returns a BLOCKER on L-R11 the question goes
to the owner with both branches costed, not to another reviewer.
