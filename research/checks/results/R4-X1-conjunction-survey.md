# R4 X1: pre-adoption survey for the B-R33 conjunction rule (EVO-95)

**Status: survey and proposal only. Nothing in this file is adopted. No claim file is edited by it.**

B-R33 (lead ruling 2026-10-18, `docs/research/DECISIONS.md` final section, commit 44a1c60) is
scoped to B1e-Q2's integration under D-24. As a general clause of the verdict rule it is a rule
change and runs the O-6 freeze procedure: written proposal, 24-hour cooling-off, and a
three-review re-score of every load-bearing verdict it would move. This file is **step 3** (the
survey of what adoption would move) and **step 4** (the determination on load-bearing verdicts).
Step 5 (the clause in `R4-X1-verdict-rule.md`, the vocabulary note, the DECISIONS.md adoption row)
is drafted in section 6 below and **not applied**.

Script: `research/tools/conjunction_survey.py` (read-only; `--tier 0|1|2|3|4`). Run 2026-10-18.
Corpus: 234 claim files in `docs/research/claims/` (`_TEMPLATE.md` excluded).

## 1. The clause being surveyed

Verbatim from B-R33: "a claim asserts all of its Statement quotes, so each verdict field takes the
value of its weakest conjunct, and the `verdict_scope` entry names the carrying quote first and
then every other quote with its value and status". Scales, weakest first: external `contradicted`
< `contested` < `supported`; fidelity `misread` < `partial` < `accurate`; internal
`arithmetic-error` / `non-sequitur` < `holds`. "`unverifiable`, `untestable` and `pending` are not
points on these scales; an unscored conjunct is recorded in the scope line."

The clause bites only where a claim has **more than one Statement quote** *and* **differing
per-quote verdicts are on record**. Where no per-quote verdicts were ever assigned there is
nothing to conjoin and the field stands as it is.

## 2. Mechanical screen

| tier | test | n |
|---|---|---|
| T0 | claims scored | 234 |
| T1 | more than one verbatim Statement quote block | 174 |
| T2 | per-quote language anywhere in the file (wordlist in the script) | 15 |
| T3 | of T2, where the per-quote line is not only an RH tag | 11 |
| T4 | multi-quote Statement of mixed provenance (a quote marked `secondhand`, not accessed, unretrieved, paraphrase) | 19 |
| — | load-bearing claims in the corpus | 33 |
| — | load-bearing claims with more than one Statement quote block | 31 |

**T1 overcounts heavily and is not the candidate set.** A second quote block in a Statement
section is usually not a second asserted proposition. The five other things it is: a version note
quoting both the superseded and the current wording of the same sentence (B1e quotes 1-2); a
primary-literature quote placed beside the claim it is scored against (D7 quote 2 is Kimura 1962
p.716; D14 quote 2 is Eden p.9; D5 quotes 2-4 are Schützenberger's own text); the critic's words
and the Day text they are about in one node (B6b, A5f); a restatement of the same proposition from
a second locator in the same source (B2b, C2b, DN3, A6); and a formula with the definition and
worked illustration that fix its reading, all from one section (B2a's three quotes are all
Z22129121 §The Second Objection).

**T4 exists because T2's wordlist misses the case that matters most.** A4g records differing
per-quote fidelity without using any of the trigger words — the comment reads "Zenodo abstract
quote accurate; book/slide wording secondhand". A wordlist screen cannot be the whole survey, so
every T1 claim of mixed provenance was read by hand as well.

## 3. Hand adjudication

Every T3 and T4 claim was read in full (Statement section, front-matter comments, `verdict_scope`).

### 3.1 T3: per-quote language, adjudicated

| claim | LB | what the per-quote line is | conjunction bites? |
|---|---|---|---|
| B1e | no | the originating case; internal scope names the unexamined 2026-08-23 blog quote | **yes — EVO-12, already applied, out of scope here** |
| B | **yes** | RH tag: quote 1 rhetoric (finality claim, RH-10), quotes 2-3 dialectic | no value move; see 3.3 |
| B5j | no | RH tag: quote 3 rhetoric (RH-19), quotes 1-2 dialectic | no value move (rule RH) |
| D13 | no | RH tag: quote 1 rhetoric (RH-14), quotes 2-3 dialectic; the second hit is about unexamined *responses*, not a Statement quote | no |
| D2k | no | RH tag: quote 1 rhetoric (RH-17), quotes 2-3 dialectic | no value move (rule RH) |
| G4 | no | RH tag: quote 1 rhetoric (RH-9), quote 2 dialectic | no value move (rule RH) |
| ROOT-EP | no | RH tag: quote 2 rhetoric (RH-16), quotes 1 and 3 dialectic; the "not examined" hit is about Hössjer's publication record, not a quote | no value move (rule RH) |
| ROOT-T | no | RH tag: quote 1 rhetoric (RH-13), quote 2 dialectic | no value move (rule RH) |
| ROOT-PG | no | RH tag on quote 3 is reading-dependent; the existing scope line already states "ROOT-PG's three verdicts are unchanged under every reading" | no — already recorded |
| A5h | no | "not examined" describes a seeded sample in a ledger note, not a Statement quote | no |
| B6b | no | "second quote above" is a derivation locator in the Formal statement | no |
| C5a | no | "same paragraph as the first quote" is a source locator | no |
| F | **yes** | "quote 2 states 'rate × (window − startup)'" supports the single internal verdict; the window/latency step is attributed to F1a and scored there | no |
| F1a | **yes** | quotes 2 and 3 are cited in a derived reconstruction; no per-quote verdict is assigned, and internal is already `non-sequitur`, the floor of its scale | no |
| H2 | **yes** | "the abstract quote" is a source locator (read from an abstract) | no |

Rule RH is what disposes of the seven RH-tag rows: a quote tagged `rhetoric` "is not
literal-fact-checked and changes no verdict". A rhetoric conjunct therefore has no value on any
scale and cannot be the weakest conjunct. Under B-R33 it is an unscored conjunct and belongs in the
scope line — bookkeeping, not a value move.

### 3.2 T4: mixed provenance, adjudicated

None of the 19 is load-bearing. Eighteen carry a **claim-wide** fidelity verdict set by rule F or
rule U (an uncited or unretrievable input, or a relay of an unidentified author) rather than a
per-quote split: B5d, C2b, D1c, D7a, D7b, D8, H3, ROOT-T `unverifiable`; A4f, A5f, D5, D7
`partial`; D14 `accurate`; B3f, B5j, C5a, G4, ROOT-COV `n/a`. In each the extra quote is primary
literature, the relayed source, or the critic's words, and the single verdict already covers the
whole node.

**A4g is the one genuine case.** Three Statement quotes all asserting that standard models assume
complete generational replacement: quote 1 is Day's own Zenodo abstract (firsthand, recorded
`accurate`), quotes 2 and 3 are Duffy's slide read aloud in a video with the book text not accessed
(both marked `secondhand`). The field is `unverifiable`, and the comment records the split
explicitly. `load_bearing: false`.

### 3.3 B and the publication hold

B is load-bearing and carries an RH split, so adoption would add scope-line text to a node whose
internal value is `pending` under D-21 and whose B-R11..B-R19 re-ruling is held un-integrated under
B-R20/B-R21 (ruled B-R22, 2026-10-18). **B is not touched by this adoption.** Its scope lines wait
for the hold to lift, and that is recorded here so the omission is not read later as an oversight.

## 4. Finding: the clause is incomplete for off-scale conjuncts (A4g)

B-R33 says an off-scale conjunct (`unverifiable`, `untestable`, `pending`) "is recorded in the scope
line". It does not say what the field then shows. Two readings, and they disagree on A4g:

- **Literal.** The field takes the weakest conjunct *that has a value on the scale*; the off-scale
  conjunct is demoted to the scope line. A4g fidelity becomes `accurate` (quote 1), with quotes 2-3
  recorded as secondhand in scope. **This is a verdict value move**, and it moves the field
  *upward* — the opposite of the cost B-R33 records against itself ("it makes a node's field worse
  as quotes are attached").
- **Off-scale dominates.** A field cannot show a scored value while a Statement conjunct of the same
  field is unscored; the field takes the off-scale value and the scope line names both. A4g
  fidelity stays `unverifiable`. **Nothing moves.**

Off-scale-dominates is what the corpus already does everywhere outside B1e: B2, B2b and E6 (all
load-bearing) show fidelity `unverifiable` across a multi-quote Statement under rule F; so do D8,
D10, H3, D7a, D7b, C2b, B5d, A3d and ROOT-T. It is also the reading that keeps rule F and rule U
intact — rule U assigns `unverifiable` to a *node* for a relay, and the literal reading would let a
single firsthand quote beside the relay scrub that.

B1e's internal is not a counter-example. There the second quote was **unexamined** (no verdict had
been reached), and an absence is not a finding: the scored conjunct set the field and the scope line
recorded the gap. A conjunct scored `unverifiable` is different — that is a positive finding that
the claim's support cannot be checked. The sub-rule below writes that distinction down.

**Proposed sub-rule B-R33a (off-scale conjuncts).** Where a Statement conjunct of a field is scored
`unverifiable` or `untestable`, the field takes that value and the scope line names the carrying
quote and every other conjunct with its value. Where a conjunct is merely **unexamined** or
`pending`, the field takes the weakest *scored* conjunct and the scope line records the unexamined
quote as a gap. Both sides, all three fields.

**This amendment restarts its own cooling-off.** The sub-rule is material — without it A4g moves —
so under O-6 it needs its own 24 hours. Written 2026-10-18 07:59 UTC, so the earliest adoption of
B-R33 *as amended* is **2026-10-19 07:59 UTC**, seven minutes after the clock on B-R33 itself
(2026-10-19 07:52 UTC). Adopting the unamended clause earlier is not worth the inconsistency it
would book against A4g for seven minutes.

## 5. Step 4 determination: no load-bearing verdict moves

**No load-bearing verdict value moves under adoption, amended or unamended.** The three-review
re-score of O-6 is therefore not triggered. The 33 load-bearing claims, all checked:

A, A2e, A3, B, B1, B1c, B2, B2b, B3, B3a, B3g, B4a, B5, B6, B7, C2, C2a, E5, E6, F, F1, F1a, F2,
F3a, FM10, H, H1, H2, H5, H8, ROOT-EM (`ROOT-excluded-mechanisms`), ROOT-FM, ROOT-NM
(`ROOT-no-mechanism-suffices`).

Four are in T3 (B, F, F1a, H2) and each is adjudicated to no move in 3.1. None is in T4. The two
with a single Statement quote block (A, FM10) cannot conjoin at all. For the remaining 27 no
per-quote verdict is on record, so there is no conjunct set to take a weakest member of.

The one scope-line (not value) consequence on a load-bearing node is B's RH split, deferred to the
B-R20/B-R21 hold per 3.3.

**Limitation, stated plainly.** This survey finds where the clause bites **today**, against the
per-quote verdicts now on record. It is not a prediction about later checks. B1e's own history is
the warning: its second Statement quote sat unexamined for weeks and the conjunction question only
arose once B1e-Q2 scored it. Any future check that scores a second Statement quote of a
load-bearing claim puts that claim's field back under this clause, and under O-6 that check's own
registration carries the verdict-field flip and gets three reviews on the existing rules. No
re-survey is owed before then.

## 6. Drafted adoption text (not applied)

Held for 2026-10-19 07:59 UTC, and for EVO-94 (section 7). Three edits, in this order.

### 6.1 `research/checks/results/R4-X1-verdict-rule.md`, new section after RD

> ## CJ. Conjunction: a claim with more than one Statement quote (adopted YYYY-MM-DD, B-R33 + B-R33a)
>
> A claim asserts all of its Statement quotes. Each verdict field therefore takes the value of its
> **weakest conjunct**, and the `verdict_scope` entry names the carrying quote first, then every
> other quote with its value and status. Scales, weakest first: external `contradicted` <
> `contested` < `supported`; fidelity `misread` < `partial` < `accurate`; internal
> `arithmetic-error` / `non-sequitur` < `holds`.
>
> - **CJ1.** Taking the better conjunct is barred: it masks a verdict already reached. Averaging to
>   `contested` is barred: it invents a dispute the quotes do not have.
> - **CJ2 (off-scale, B-R33a).** `unverifiable`, `untestable` and `pending` are not points on these
>   scales. A conjunct **scored** `unverifiable` or `untestable` sets the field, and the scope line
>   names the carrying quote and every other conjunct with its value (rules F and U reach the node,
>   not one quote of it). A conjunct that is merely **unexamined** or `pending` does not set the
>   field: the field takes the weakest scored conjunct and the scope line records the unexamined
>   quote as a gap.
> - **CJ3 (rhetoric).** A quote tagged `rhetoric` under rule RH has no value on any scale and is
>   never the weakest conjunct; it is recorded in the scope line as unscored (rule RH: rhetoric
>   changes no verdict).
> - **CJ4 (order with RD).** Readings first, then quotes. Rule RD fixes each quote's governing
>   reading (the reading under which that quoted statement is most defensible); CJ then conjoins the
>   per-quote values. A node can be both reading-dependent and conjoined — B1e is.
> - **CJ5 (the countermeasure is the split).** CJ makes a node's field worse as quotes are attached.
>   Where a claim's Statement quotes assert propositions that do not stand or fall together, the
>   claim is split into one node per proposition rather than conjoined. A split touches
>   `hierarchy.yaml`, the argmap and the board, so it is filed as its own task.
> - Applied to Day, critics and allies alike.
>
> **Test cases.** (i) B1e: external `contested` (QB, reading R-A) with the blog quote
> `contradicted` → `contradicted`, carrier QB named first. (ii) B1e internal: `holds` scored, blog
> quote unexamined → `holds` under CJ2, the gap in the scope line. (iii) A4g fidelity: quote 1
> `accurate` firsthand, quotes 2-3 `secondhand`/`unverifiable` → `unverifiable` under CJ2, all three
> named. (iv) B: quote 1 `rhetoric`, quotes 2-3 dialectic → the dialectic quotes conjoin, quote 1
> recorded unscored under CJ3. (v) A claim whose two quotes are both `partial` → `partial`, both
> named (B1e fidelity).

### 6.2 Vocabulary section note

One line beside the three vocabularies: the values are listed weakest-first for CJ, and
`unverifiable` / `untestable` / `pending` are off-scale, governed by CJ2.

### 6.3 `docs/research/DECISIONS.md`

An adoption row dated on adoption: B-R33 generalised from B1e-Q2 to the verdict rule as rule CJ,
amended by B-R33a; O-6 discharged (proposal 2026-10-18, cooling-off to 2026-10-19 07:59 UTC, survey
in this file, no load-bearing verdict moved, no three-review re-score owed); and the note that CJ
sets no value on any claim other than B1e today.

## 7. Dependency: EVO-94 gates adoption

EVO-94 is the D-24 fresh-reviewer check on B-R31..B-R33 — an instance with no part in B1e-Q2
checking the rulings themselves. It was in progress while this survey was written. **B-R33 must not
be generalised before that review reports.** If the fresh reviewer faults how B-R33 reaches the
field, the clause drafted in 6.1 changes with it. Adoption needs both: the cooling-off expired and
EVO-94 clear on B-R33.

## 8. Who this helps

**Day's side.** The off-scale sub-rule (B-R33a) is the clause that *costs* Day a field: without it
A4g's fidelity would rise from `unverifiable` to `accurate` on the strength of his own Zenodo
abstract, and the survey proposes to bar that. The reason is symmetric, not adverse: rule U's
`unverifiable` for relays protects critic-side nodes (B5d, D8, ROOT-COV) by the same mechanism, and
CJ5 records that conjunction is the wrong tool where propositions are separable — the split, which
is the remedy that can *raise* a Day node's field, is named as the countermeasure rather than left
implicit. CJ3 also keeps rhetoric out of the scales, which matters most for the nodes where Day's
quoted rhetoric sits beside his dialectic (B, G4, D13).

**Critics' side.** The clause closes the masking SC6 objected to: a claim does not keep the better
of two verdicts once the worse one has been reached. It is drafted to apply to critic-side and
ally-side nodes identically, and the RH rows in 3.1 include four critic or ally nodes (B5j, D2k,
ROOT-EP, ROOT-PG) alongside Day's.

**The audit.** The survey's main product is the negative result in section 5 — the clause moves no
load-bearing verdict, so no re-score is owed — and the limitation that bounds it: the result is
about today's record, not about checks not yet run.
