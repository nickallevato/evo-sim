# Brief B1e-Q2 (analyst): B1e's second Statement quote and the Kimura (1955) link

Lead: Big Sim. Written 2026-10-13, before the task was created (MA-21).
Skill to load: `.claude/skills/design-check/SKILL.md` (one skill; design and pre-register,
then the write-up is a later task in the same lifecycle).

## Goal

Close the two gaps the B2f integration left open on `docs/research/claims/B1e-chalub-2022-reading.md`
(its "Fields set by this integration" paragraph names both):

1. **The 1/(2N) quote.** The second Statement quote is the 2026-08-23 blog sentence,
   "Chalub shows that the 1/(2N) is an assumption imported from the Wright-Fisher model.
   It is not a result produced by the mathematics."
   (voxday.net/2026/08/23/chalub-and-the-kimura-cancellation/, ¶5 of extracted text).
   B2f did not examine it. Score it: is 1/(2N) an input Chalub assumes, a consequence of
   the diffusion limit he derives, or a boundary/initial condition? Fidelity against
   Chalub 2022 verbatim, internal against Day's own derivation.
2. **Is Chalub's Gegenbauer expansion the Kimura (1955) series?** This decides how far the
   credit B2f gave Day for the derivation route reaches. If it is the same series under a
   change of variables, the route is standard and old; if it is a distinct solution, the
   relay is a fair description of a 2022 result. Settle it from the two papers'
   mathematics, not from either author's description of the other.

## What the lead has already seen

- B2f (`research/checks/results/R4-B2f.md`, integrated `de3c1a2`, review #82) found the
  exponent exact in the short-time limit and the described route real apart from the word
  "eigenvalue"; as an equality the form is low by (4πNₑ/T)^1.5 e^(T/16Nₑ).
- B1e's current fields: internal `holds`, fidelity `partial`, external `contested`, all
  reading-dependent (rule RD). Quotes Q286, Q288 and the ledger rows are already in
  `quotes-day.md`; the blog quote in the Statement block has no Q id yet — assign one.
- The Zenodo file was replaced on 2026-10-13; the first Statement sentence is superseded.
  The blog quote is not affected by that replacement.
- Chalub 2022 verbatim rows are already in the claim file's source table (lines 55-57).

## Review tier

**Low-stakes: one combined review**, `REVIEW-R4-B1e-Q2-combined.md`, with a correctness
section and both steelman sections. B1e is not load-bearing.

**Superseded 2026-10-14 (REVIEW C1): three reviews, as three files, and they were done.**
D-23 sets the tier from the registration as committed, which carries a verdict-field flip
line (B1e fidelity `partial` → `misread`), not from the outcome. The three files are
`REVIEW-R4-B1e-Q2-correctness.md`, `-steelman-day.md`, `-steelman-critic.md`. Do not write a
combined review for this check.

**Escalation clause, stated in advance** (it is the claim file's own condition): this check
becomes load-bearing and needs **two further reviews** (three in total) if your result
would change a verdict value or a defeater on **B1, B1a, B2 or B**, if Reading B is adopted
as field-setting on B1e, or if Day is found to have derived a number from F(T). If you
reach any of those, stop, write what you have, and report it to the lead; do not apply the
move yourself.

## Files you may write

- `research/checks/<id>.py` only if a computation is needed (it probably is not; this is a
  mathematics-and-text check). If you write one, pre-register it per the skill.
- `research/checks/results/R4-B1e-Q2.md`
- `research/checks/briefs/` — nothing; the brief is the lead's.

Not yours in this task: claim files, `QUEUE.md`, `REVIEW.md`, `RESULTS.md`, ledgers,
quotes files, the argmap data. Integration is a separate task.

## Constraints

- `AGENTS.md` hard rules and token budget apply. Verbatim quotes with locator and date
  (rule 2). No full texts in git (rule 3). No outward actions (rule 6).
- Chalub 2022 and Kimura 1955: use the held copies under `sources/raw/` if present; read or
  grep, never execute. No paywall bypass, no shadow libraries. If Kimura (1955) is not
  obtainable within the rules, say so and score the link `unverifiable` rather than
  guessing.
- No computation on this workstation beyond a trivial check (one process, under 500 MB,
  under a minute). `na-workhorse` is busy with `ph2` until 2026-10-16: launch nothing there.
- Rules S, C and RD in `R4-X1-verdict-rule.md` govern the scoring; record every plausible
  reading with its verdict.
- Commit with explicit paths, never `git add -A`. End each commit message with exactly:
  `Co-Authored-By: Paperclip <noreply@paperclip.ing>`
- `git pull --rebase origin research` before each push; push `origin research` only.

## Lead rulings, 2026-10-18 (D-24; lead rulings B-R31..B-R34)

Written after the fix pass (EVO-11) and the three reviews, for the remainder of the EVO-12
integration. Sources read for these rulings: `results/R4-B1e-Q2.md` (fix-passed),
`REVIEW-R4-B1e-Q2-correctness.md` (C2, C4), `-steelman-day.md` (D1, D2, D3, D6, D7),
`-steelman-critic.md` (SC1, SC2, SC3, SC4, SC6, SC7), the registration docstring, the
claim file, `R4-X1-verdict-rule.md` (C, RD, S, the fidelity and external vocabularies) and
`DECISIONS.md` (B-R20..B-R30, O-6). The rulings are also recorded in `DECISIONS.md`.
Nothing here is a new computation; every mathematical fact cited is either a registered
printed item or a stated identity.

### B-R31 (ruling 2, taken first because 1 depends on it). R-A stays a plausible reading and keeps governing QB.

D3 and SC4 conflict and the lead rules. **Ruling: R-A is plausible; it remains the
governing reading of QB. R-B is recorded as a plausible alternative that does not set a
field.**

Basis. RD admits every *plausible* reading and sets the field by the one under which the
quoted statement is most defensible — not by the reading the author most likely meant.
SC4's evidence (QB's own two preceding sentences, blog .txt l.7, where "the mathematics" is
glossed by "the diffusion machinery" the literature uses) is good evidence about what Day
meant, which is not what RD ranks on. Against it stands Day's own sentence eleven lines
later, "The diffusion has to be provided as an assumed condition that is supplied in order
to solve the equation." (blog .txt l.11, D3): a condition "supplied in order to solve the
equation" is by construction outside the equation, which is R-A's gloss. A reading the
author's own text states in those words is plausible. So R-A survives the plausibility test
and, being the more defensible of the two, governs.

What this ruling does **not** do. It does not find that Day meant R-A; the fix pass already
withdrew that sentence and it stays withdrawn. It does not rank R-B as implausible: R-B
keeps its row, with fidelity `misread` and external `contradicted`, marked *plausible, not
field-setting*. SC4's conditional effect (fidelity `partial` → `misread`) therefore does not
fire, and QB's fidelity stays `partial` on the basis D6 and SC3 restated.

### B-R32 (ruling 1). QB's external value under R-A is `contradicted`. `supported` is not open.

> **SUPERSEDED in part by B-R35 (below), 2026-10-18, after the EVO-94 fresh-reviewer check.**
> The value is **not** `contradicted`: it stays at the registered `contested`. Basis (3) is
> withdrawn as a basis for QB's reading. The bar on `supported` stands, re-based on P3 with
> P4. Read this section for the record; the integrator writes B-R35's values and scope lines,
> not this section's.

D1 (`supported`) and SC1 (`contradicted`) conflict and the lead rules. **Ruling: R-A
external is `contradicted`, moved from the registered `contested`.** Both steelmen's
positions stay on the record in the write-up; this is a ruling, not an average of them.

Basis, from registered items only (reviewer post hoc computations concur but are not the
basis):
1. P3 (b(∞) = 4/9 = ∫x p^I, b(0) = 0) with P4 (b′ = −J(1), an identity, worst_rel 4.98e-64)
   gives the integrated outflux of the **classical solution alone** at x = 1 as ∫x p^I.
   That number is computed from r, with no constraint and no point mass entering (SC1
   recomputed it from the coefficients alone to 20 digits; the two-registered-item route is
   what the ruling rests on). For a one-copy start that number *is* the 1/(2N).
2. P5 (HIT) shows alternative splits exist, but, as the fix pass conceded to SC2, only if
   mass leaving at x = 1 may be booked at x = 0 or the reverse. Non-local booking is not a
   rival model of fixation; it is a mis-booking of the flux.
3. What the diffusion does need from outside is that mass leaving at x = i stays at x = i —
   the meaning of the boundary states. That is not a premise about reproduction and not a
   Wright-Fisher import. Day's own description of the model in the governing Zenodo sentence
   is "the neutral Kimura diffusion equation **with absorbing boundaries**" (Q288), so the
   most defensible reading of "the mathematics" cannot be narrower than a diffusion whose
   boundaries are absorbing.

Consequence for QB's two sentences. Under R-A, sentence 2 ("It is not a result produced by
the mathematics") is false by (1) and (3); sentence 1 ("an assumption imported from the
Wright-Fisher model", R-A's gloss "enters from the discrete process") is false because the
input the diffusion needs is its own boundary semantics, not anything taken from the
discrete process. Under a reading narrower still, in which even local booking counts as an
outside import, sentence 2 could be true but sentence 1 remains false. QB is a conjunction
of two sentences, so on every plausible reading at least one conjunct is false and under
the governing reading both are. `contradicted`, and `supported` is barred.

Why `supported` is barred, explicitly (answering D1). D1's two strong points are accepted
as far as they go: an equivalence does not say which side is the premise, and P6b tests
Wright-Fisher exclusivity, a meaning R-A sets aside. P6b is accordingly **out** of this
field's basis, as all three reviews asked. But D1's own appended derivation — the weak
(generator-dual) form of (7) on [0, 1] yields both conservation laws from φ = 1 and φ = x —
is precisely what defeats `supported`: the laws are consequences of the diffusion's own
generator, so the needed input is not "imported from" any discrete process. SC3 (iii)
reaches the same place from Chalub's text, the second law being conservation of ϕ with
ϕ″ + ψϕ′ = 0, the diffusion's own stationary backward equation. Two steelmen on opposite
sides independently derived the fact that bars the Day-side value.

What survives for Day, and must stay in the write-up and the ledger at integration: P5 with
its booking qualifier, as an identity that hit for him; Chalub's own framing ("had to be
introduced into the model", C2; "derived directly from the discrete process", C1, C13), on
which QB's fidelity stays `partial` rather than `misread`; and the presentation point
(D5, SC8) that Chalub imposes the ϕ-law before computing any coefficient. Day loses this
field on the mathematics, not on his reading of Chalub.

This moves a governing reading's value, so under D-24 a **fresh reviewer** checks B-R31,
B-R32 and B-R33 before the rest of the integration is written. The escalation clause does
not fire: B1, B1a, B2 and B are untouched, B2f's Reading B is not adopted, and nothing here
has Day deriving a number from F(T).

### B-R33 (ruling 1c). Two Statement quotes in one claim: the conjunction rule, with the carrier named in the scope line.

The rule file has no clause (SC6 grepped for one; so did I). **Ruling, for this
integration: a claim asserts all of its Statement quotes, so each verdict field takes the
value of its weakest conjunct, and the `verdict_scope` entry names which quote carries the
value and gives every other quote's value.** Orderings, weakest first: external
`contradicted` < `contested` < `supported`; fidelity `misread` < `partial` < `accurate`;
internal `arithmetic-error` / `non-sequitur` < `holds`. `unverifiable`, `untestable` and
`pending` are not points on these scales: a field with an unscored conjunct records that in
the scope line and takes its value from the scored ones.

Why this and not the alternatives. Taking the better conjunct is what SC6 objected to: it
silently masks a verdict the audit has actually reached. Averaging into `contested` would
invent a dispute where there is none — the two quotes are not in conflict with each other,
they are different statements with different verdicts. The conjunction rule follows from
what a claim node is, applies identically to Day, critics and allies, and leaves no value
hidden, because B-R25's scope shape already carries the per-reading detail and now carries
the per-quote detail in the same fixed order: carrier first, then the rest with their
verdicts and status.

Its known cost, recorded against it: a node gets a worse field the more quotes are attached
to it, which is an incentive to split claims rather than argue them. The countermeasure is
the split, not a softer rule: **where a claim's Statement quotes assert propositions that do
not stand or fall together, the claim is split into one node per proposition.** B1e is a
candidate (its title is literally the conjunction of an asymptote relay and the 1/(2N)
import), but splitting a node touches `hierarchy.yaml`, the argmap and the board, so it is
**not** done in EVO-12; the lead files it as its own task.

Scope of this ruling. It governs B1e-Q2's integration now, under D-24. As a *general*
clause of the verdict rule it is a rule change and goes through the O-6 freeze procedure
(written proposal — this section — then 24-hour cooling-off, then a three-review re-score of
any load-bearing verdict it would move). It moves no load-bearing verdict here: B1e is
`load_bearing: false`. Until the freeze procedure completes, no other claim's fields are
recomputed under it.

Applied to B1e (**superseded by B-R35's three lines below**; kept for the record):
- **external: `contested` → `contradicted`.** Carrier: the blog quote QB. Scope line, in
  B-R25's shape: `Scope: the value is carried by the 2026-08-23 blog quote (1/(2N)
  "imported"), `contradicted` under governing reading R-A (B-R32: P3 with P4 give the
  classical solution's own integrated outflux at x = 1 as ∫x p^I; P5's free split needs
  non-local booking; R-A0 and R-B are `contradicted` too, not field-setting); the Zenodo
  statement is `contested` under its governing reading (A) - the exponent is supported in
  logarithms (exact as T/Nₑ → 0) and "every application of k = μ ... is guaranteed to be
  incorrect" is contested on the start state only (scored at B1, B1c, B6a) - and reading (B)
  is `contradicted` by the exact diffusion at every T (B-R33, conjunction rule)`.
- **fidelity: `partial`, value unmoved.** Both conjuncts are `partial`. The scope line gains
  QB: `partial` under R-A, narrowed from "the Moran and the Wright-Fisher processes" (C3,
  C13) to Wright-Fisher and "derived directly from the discrete process" (C1) relabelled
  "assumption" (D6, SC3); `misread` under R-A0 and R-B, not field-setting; the Chalub-link
  half stays `partial` on the ledger basis, P8 band U.
- **internal: `holds`, value unmoved.** The existing scope line is now wrong on its face —
  the blog quote *has* been examined. Replace it: QB's internal is `holds` under every
  reading (T2, B3d; nothing in the post contradicts QB), and the Zenodo statement's `holds`
  is reading (A) with reading (B) `non-sequitur`, as the comment already says.
- No other claim file's fields move.

### B-R34 (the P7 ruling). Option (b): the value item was mis-specified by the audit. No field moves.

All three reviews recommend (b) and none recommends (a). **Ruling: (b).** The registered
P7 call stays **MISS, band X** in every tally and is counted as the audit's own miss, never
against Day. The licensed X move (B1e fidelity `partial` → `misread`) is **void and is not
applied.**

Basis, registered: coef_err printed 0.0 over n = 0..200, so given the coefficient item the
value item could differ only through numerics; the three binary-exact x (0.25, 1, 4) agree
to ≤ 1.12e-138; and the committed script passes `t = mp.mpf(x) / 4` from a Python float on
one side against `F_dec(str(x))`, an exact decimal, on the other (C2). Two reviewers
reproduced all three failing figures from the float offsets alone (C2, SC1). The post hoc
script's H1 and H2 hold and are confirmation, not the basis.

Second ground, independent of the bug (D2): band X maps to fidelity `misread`, and the
rule defines `misread` as "the cited source text is in hand and contradicts the reading".
A mismatch between Chalub's b(t) and the **audit's** B2f series would show that B2f's route
credit is not extended; it could not show that Chalub's text contradicts Day's description
of it. The X line is a non-sequitur inside the registration, quite apart from the float
path. Any later re-registration under option (c) maps X to "B2f credit not extended;
Chalub-link fidelity unchanged (`partial`)", never to `misread`.

Precedent, adopted in SC7's symmetric wording, verbatim: "a registered band reached only
through an audit argument mismatch, shown by registered items, is ruled mis-specified
whichever side it favours."

What (b) does **not** establish. It voids the X move; it does not register the E line.
Chalub's b(t; x0)/x0 equalling the eigen-series B2f used (mode n = term n + 1) stays a post
hoc, descriptive result, credited to **both** sides (both predicted E) and setting no field.
P8 stays band U, so the Chalub-link fidelity stays `partial` on the ledger basis and the
"old" half of the question stays `unverifiable`. Option (c) is declined as adding nothing:
the post hoc docstring pre-stated H1 at the registered 1e-30 band before it ran.

### B-R35 (re-ruling of B-R32, 2026-10-18, after EVO-94). RC-1 is accepted: QB's external value under R-A is `contested`, the registered value. No verdict value moves anywhere in B1e.

The D-24 fresh-reviewer check (`results/REVIEW-R4-B1e-Q2-ruling-check.md`, EVO-94, 009d5b6)
confirmed B-R31, confirmed B-R33's rule with two corrections, and **rejected B-R32's value**
on one MAJOR (RC-1). The lead accepts RC-1 in full, and RC-2, RC-3, RC-5 and RC-6 with it.

**Why RC-1 is right.** B-R32's basis (3) argued that "the most defensible reading of 'the
mathematics' cannot be narrower than a diffusion whose boundaries are absorbing". As the
reviewer shows, that *is* R-B's registered gloss ("the neutral diffusion model with its
boundary behaviour", docstring l.198), not R-A's ("PDE (7) on the open interval", l.196). So
B-R32 named R-A as governing and then scored the field on R-B's content. That is a
re-ranking of readings, which B-R31 and RD forbid; RC-8 states the inconsistency plainly —
B-R31 and basis (3) cannot both stand. Dropping (3) is the fix that keeps B-R31 as ruled.
Without (3), items (1) and (2) show that the *number* is the classical solution's own
outflux and that a free split needs non-local booking; they do not exclude non-local booking
under a reading whose subject is (7) on the open interval, which says nothing about where
mass that has left the interval is booked. And RC-1 (d) is decisive on consistency: the
Zenodo conjunct in this very claim is `contested` because it is false under one premise and
true under another, and A3a external is `contested` with a `contradicted` reading recorded
beside it. Filing QB `contradicted` would hold Day's quote to a stricter standard than the
audit applied to the sentence in the same file. Equal scrutiny is hard rule 1.

**The ruling.**
1. **QB external under R-A: `contested`** — the registered value. No field move, so under
   D-24 no further fresh-reviewer check is required before integration (RC-1 fix, RC-7).
2. **Basis (3) is withdrawn** as a basis for QB's reading (RC-2). Q288 is the Zenodo wording
   of 2026-10-13; QB is the blog of 2026-08-23, and rule S scores a node on its own Statement
   quotes and their derivation. (3) may stay as context — "Day's later Zenodo wording names
   absorbing boundaries" — and it bears on R-B, not on QB's governing reading.
3. **`supported` stays barred, re-based on P3 with P4** (RC-4), not on D1's weak-form
   derivation or SC3 (iii), which are R-B's hinge and do not score R-A. The value *is*
   produced by the classical solution's outflux, so sentence 2 has a genuinely false half
   under every reading. R-A0 and R-B stay `contradicted`; R-C stays `supported` (trivially,
   D7). None of the three is field-setting.
4. **The two identities are named** (RC-3): P4 is extended to all t by the mode-wise identity
   C_n^{3/2}(1) = λ_n/2 (correctness C3), b(0) = 0 comes from Chalub's printed b(t), and
   b(∞) = ∫x p^I = x0 for a delta start (Chalub §3) is what makes the number the 1/(2N) for a
   one-copy start. All three are analytic; none needs a run.
5. **SC1's case is not discarded**; it moves into the scope line as the false half and the
   lean (RC-1 (b), steelman paragraph): frequency 1 *is* fixation, so the only thing (7)
   needs from outside is the meaning of the boundary states, which carries no number. That a
   boundary convention is not "an assumption imported from the Wright-Fisher model" is
   recorded as the audit's lean, not as a value that settles the open point between R-A and
   R-B.
6. **B-R33 stands as a rule**, with RC-5's two corrections. With (1) applied it moves **no**
   B1e value — external `contested`/`contested`, fidelity `partial`/`partial`, internal
   `holds`/`holds` — so the O-6 timing question RC-7 raises does not arise in EVO-12. General
   adoption remains EVO-95 under the freeze procedure; the split remains EVO-96.
7. **B-R34 is untouched** by the check (it was out of its remit and moves no field).

**Applied to B1e — the three lines the integrator writes, values and scopes together (B-R21).
These supersede B-R33's drafted lines above.**

- **external: `contested`, value unmoved.** Both conjuncts are `contested`, so no single
  quote carries the value. Scope line, RC-6's proposed text with RC-5 (i) and (ii) already in
  it, verbatim:
  `Scope: both Statement quotes are contested under their governing readings, so no single quote carries the value (B-R33, conjunction rule): the 2026-08-23 blog quote (1/(2N) "imported") under R-A - true that (7) on the open interval with probability conservation alone leaves the split free unless mass leaving at one end may be booked at the other (P5), the laws being added from the discrete process (C1, C2); false that the value is an input, the classical solution's own integrated outflux at x = 1 being ∫x p^I (P3 with P4) - with R-A0 and R-B contradicted and R-C supported (trivially), none field-setting; the Zenodo statement under its reading (A) - the exponent is supported in logarithms (exact as T/Nₑ → 0) and "every application of k = μ ... is guaranteed to be incorrect" is contested on the start state only (true from an empty start, the paper's premise; from a stationary start the flux is exactly μ; scored at B1, B1c, B6a) - with reading (B) contradicted by the exact diffusion at every T`
- **fidelity: `partial`, value unmoved.** Both conjuncts are `partial`. The line gains QB and
  **R-C**, and the words "the Chalub link itself ... is unchecked" are **replaced**, not
  appended to (RC-5): QB is `partial` under R-A, narrowed from "the Moran and the
  Wright-Fisher processes" (C3, C13) to Wright-Fisher and with "derived directly from the
  discrete process" (C1) relabelled "assumption" (D6, SC3); `misread` under R-A0 and R-B and
  `partial` under R-C (D7), none field-setting; the Chalub-link half stays `partial` on the
  ledger basis, P8 band U, the P7 value item having been ruled mis-specified (B-R34) and the
  E-line identity being post hoc and descriptive.
- **internal: `holds`, value unmoved.** Both conjuncts are `holds`, so neither alone carries
  the value (RC-5): QB `holds` under every reading (R-A, R-A0, R-B, R-C; T2, B3d), and the
  Zenodo statement `holds` under reading (A) with reading (B) `non-sequitur`. "Was not
  examined" is dropped — the blog quote has now been examined.
- No other claim file's fields move, and no verdict *value* moves in B1e.

### What the integrator does with these

1. The fresh-reviewer check on B-R31..B-R33 is **done** (EVO-94, 009d5b6) and its MAJOR is
   answered by B-R35. Because B-R35 keeps every registered value, no further check is due.
   Write **B-R35's** three lines, not B-R33's drafted ones.
2. Then, in EVO-12's remaining pass: the verdict comments and `verdict_scope` entries from
   B-R35, the defeaters on both sides (on the critic side, that the 1/(2N) is the classical
   solution's own integrated outflux at x = 1, P3 with P4 — a defeater of the "not a result
   produced by the mathematics" half, not of the whole quote; on the Day side, P5 with its
   booking qualifier and Chalub's own framing, C1, C2, C13), the lineage node, the mini-form,
   and the count refresh. `lint_research.py` rejects a verdict entry with no scope, so no
   field is touched without its scope line in the same edit (B-R21). No verdict *value*
   changes, so the counts should not move; if a count does move, stop and report.
3. Nothing publishes. B1e external appearing on the board is a later, gated task
   (EVO-92 / B-R30), not this one. The B-R20/B-R21 hold on B internal and A2e external is
   untouched by all five rulings.

## Report format (at most 300 words)

Commits; a results table (each registered prediction, Day-side and critic-side, hit or
miss); the proposed verdict for each of the two questions and whether the escalation clause
fired; failures; next step.
