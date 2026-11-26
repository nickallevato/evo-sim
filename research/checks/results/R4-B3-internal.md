# R4 B3-internal: rule RD on the B3 umbrella's internal verdict

**Status: write-up with fix pass 1 applied (2026-11-26); awaiting lead review. No verdict field moves here.** Brief: `research/checks/briefs/B3-analyst-1.md` (3f0c53e). Review: `REVIEW-R4-B3-internal-combined.md` (38e19ef). Fix-pass brief and lead ruling: `research/checks/briefs/B3-analyst-2.md` (177c68f). Gap item B3, field `verdicts.internal` of `docs/research/claims/B3-k-neq-mu-values-umbrella.md` (l.12, `pending`: "components differ ... no single value").

## Files and inputs
- No script, no run and no fetch. This is a reading analysis of component verdicts that are already settled. Nothing here was registered in advance, so no prediction is scored. Every verdict below is cited as it stands at 3f0c53e (rechecked at 177c68f) and is **not re-scored**.
- Rule text: `R4-X1-verdict-rule.md` RD (l.196-202), S1 (l.40), SC (l.47), N2b (l.63), row F (l.79), C (l.15-17). D-15 (`DECISIONS.md` l.31).
- Prior write-ups: `R4-B3.md` ("What this means for B3"), `R4-B3g.md` (l.20, "What the concession removes"). Versions ledger l.19, l.35. Standard form B3 (`argmap/standard-forms.md` l.118-126).

## What B3 scores (rule S1)
S1 scores a node "on its verbatim Statement quotes and the derivation chain in its Formal statement". B3 quotes three statements (claim file l.17-29). All three carry one RH tag, `dialectic` (l.31; R4-B3 status line).

| Quote | Words | Source | Component that scores it | Component internal (as it stands) | In force? |
|---|---|---|---|---|---|
| B3-1 | "census populations exceed diversity-derived N_{e} by 19- to 46-fold" | Z18429937, 2026-01-29 (no Q-id) | **None as quoted.** B3-1 is a reported ratio with no k/μ and no Q-id (S1, l.40: "A sentence that carries a verdict must be quoted in the Statement"). The ratio itself is "untouched and external" (R4-B3g l.20). Its k/μ use is B3a's formula k = μN/Nₑ, which Z18429937 applies according to versions ledger l.19, but no sentence of Z18429937 that does so is quoted at B3 | B3a `holds` (B3a l.12) scores Q38 (Z18525547 eq. 1) and Q39 (blog 2026-02-04), B3a l.17-27, not B3-1 | No. Withdrawn by Day on 2026-08-27 (**B3g** `holds` / `accurate` / `supported`). Under SC it is scored on the version quoted, with the note "corrected in B3g" (X1 l.47). Day restated "1/2Nₑ is the fixation probability" on 2026-09-15 (Q105, versions ledger l.19); whether the route is in force is B3g's call, and no reading below moves either way |
| B3-2 | "it yields k = 0.743μ, confirming Balloux and Lehmann's finding" (Q41) | Z18525262, 2026-02-08 | **B3c** | `non-sequitur` (N2a: 0.743 is a property of the four-cohort window; the paper's own growth ratio gives 0.60-0.87; B3c l.12) | Yes |
| B3-3 | "gives k = 32.3μ, not k = μ" (Q43) | blog 2026-10-01 | **B3d** | `holds` (32.93 from Day's own inputs, 1.95% off; B3d l.12) | Yes |

Not quoted, so under S1 none of these sets B3:
- The other values in the Formal statement table: 800,000 (**B3f** `holds`, status `extracted`), 15.2-30.3 and 9.1-30.3 (B4 `holds`), "median 25" (B3m `n/a`), ≈0.5 (Q42, no claim file) and 1 (B3g).
- **B3b** (`holds / partial / supported`): an edge of B3 (`depends-on B3b`, claim l.7), referred to by B3-2's "confirming Balloux and Lehmann's finding" (Q41), and premise P2 of the standard form (l.121).

All of them appear only in the extended row R-x below. The standard form's premise set (P1-P4, with B3b and "median 25") is not the same as the node's three quotes.

## 1. Readings table
No row sets the field (§2, §3). R-a and R-b have equal standing: they read every quote the same way and differ only in how the quotes are joined. The table is kept as the record an owner rule on umbrella aggregation would use.

| Id | Reading of the three quotes taken together as one internal claim | RH tag | B3 internal under this reading | Component verdicts it rests on |
|---|---|---|---|---|
| R-a | **Convergent.** The quoted values are independent routes to "k ≠ μ", each offered alone in its own source. The node's conclusion follows if at least one route follows from its author's own material. The standard form has recorded "Inference: convergent" since 9a2148b (2026-10-08) | dialectic | holds | B3d `holds` (B3-3) **alone**. B3-1 as quoted: a ratio, no k/μ, no Q-id (S1); its k/μ use (B3a) is not quoted at B3 (versions ledger l.19). B3c's `non-sequitur` (B3-2) defeats its own route, not the conclusion |
| R-b | **Conjunctive.** Each quoted value follows from its source's own material. This is S1's scoring of the node on its verbatim Statement quotes (l.40), of which B3-2 is one | dialectic | non-sequitur | B3c `non-sequitur` (B3-2); B3d `holds` (B3-3). B3-1 as quoted carries no k/μ and sets nothing (S1) |
| R-b″ | **Conjunctive on direction.** Each quoted route gives the direction k ≠ μ (B3-2 read as "k < μ") | dialectic | not scored here | Whether the direction survives N2a belongs to B3c; B3c l.12 records 0.60-0.87 on the paper's own ratio, all below 1. Not re-scored |
| R-c | **Extended (a wider claim): the values form one mutually consistent k/μ.** No quote asserts this | dialectic | n/a: not scored. Different sources and windows: N2b own-text scope (X1 l.63; B3c's cross-document basis was dropped) and charity (rule C: 0.743 and 32.3 have different referents); versions ledger l.35 | versions ledger l.35 |
| R-a′ | Sensitivity: R-a restricted to the routes still in force after B3g (B3-2, B3-3) | dialectic | holds | B3d |
| R-b′ | Sensitivity: R-b restricted to the routes in force | dialectic | non-sequitur | B3c |
| R-x | Extended (other objects): every value in the Formal statement table, plus B3b | dialectic | convergent: holds (B3a, B3b, B3d, B3f, B4); conjunctive: non-sequitur (B3c); ≈0.5 unscored | as listed |

Dropping the withdrawn leg moves no reading (R-a = R-a′, R-b = R-b′). B3g bears on B3's external field, not its internal field.

## 2. Field value
**Proposed: `pending`.** Reason: **the verdict depends on how the node aggregates its quotes, not on how any quote is read; no current rule sets it.** Neither R-a nor R-b sets the field. R-b″, R-c and R-x are recorded and set nothing. This follows the lead's ruling (brief B3-analyst-2, for C-1 / K-1).

The grounds below are kept as a record of the argument's structure. None of them is a ranking under RD.
1. **Text (D-1's ground).** The quotes' own words: B3-3 says "not k = μ"; B3-2 offers 0.743 as "confirming Balloux and Lehmann's finding", which is a k ≠ μ result (B3b); B3-1 states only that N exceeds Nₑ. The three come from three sources eight months apart, none cites another, and the two in force point in opposite directions (0.743 < 1 < 32.3). This describes a convergent argument. But RD ranks readings of a quote (l.197-198), and these words are read the same way under R-a and R-b, so the text gives no ranking between them.
2. **The "convergent" label (K-3).** The standard form recorded "Inference: convergent" at 9a2148b (2026-10-08), before RD (2026-10-11). At that commit B3a was `holds`, B3c `non-sequitur`, and B3 internal was set to `pending`. At 32df9cf (2026-10-10) B3d was `holds` and B3 stayed `pending` ("components differ ... no single value"). Twice, with a holding route available, the audit did not read "convergent" as setting the field. The standard form is a "Steelman source", charitable to Day by design, with a different premise set (P1-P4). The label is evidence about the argument's structure, not an independent warrant for a verdict.
3. **Counting note (K-2; not a ground).** Whatever the field, B3c's defect is counted once in the X1 error tallies. An umbrella value is reported as reading-dependent, scoped or `pending`, never as a new error. This is not a reason to prefer a reading: RD l.198 excludes grounds about the resulting verdict. Row F (l.79) does not support R-a: F `holds` because F did not quote F1a's step, while B3 does quote B3-2, so row F read correctly fits scoring B3-2 at B3.

What `pending` says: the audit has no rule for joining an umbrella's quotes. It is not a judgement against Day (K-5). It withholds an internal credit that B3d earned on Day's own arithmetic (D-3); the cause is the audit's missing rule, not his error. External stays `contradicted` (B3 l.14).

## 3. Applicability: RD, SCOPED, or neither
**RD as written does not rank joinings.** Its trigger is written for one quote: "where a verdict ... depends on how a quote is read" (l.197). Its criterion ranks readings by how defensible "the speaker's *quoted statement*" is (l.198). Under R-a and R-b every quoted sentence is read the same way and is exactly as defensible, so l.198 gives no ranking (C-1). No line of X1 mentions umbrellas or aggregation. Using RD to choose a joining would also empty D-15's guard: a disjunction is always at least as defensible as a conjunction, so "most defensible" would always pick the joining best for the speaker, and every umbrella with one holding quoted child would hold (K-1). The B umbrella's RD precedent ranked readings of one quote ("nearly empty"), not joinings.

R-b is not an extended reading (D-1 declined by the lead). It is not a "wider claim" the audit assembled (l.202): it scores the node on its verbatim Statement quotes (S1, l.40), and B3-2 is one of them. The disjunction drops B3-2's quoted claim.

B3 is not `SCOPED`. Its Formal statement (l.32-44) is a table of values and statuses that names no single proposition, so it fixes neither R-a nor R-b. Writing "k ≠ μ, convergent" into it by a lead ruling (the first draft's fallback, C-1 fix (a)) was declined by the lead: it makes the same choice of joining by fiat. Choosing how an umbrella aggregates its children is new process machinery and needs an owner decision (OPERATING-PROCESS, "Don't open new process machinery"; ROADMAP B5, the ROOT aggregation proposal, is related). B3 is therefore neither reading-dependent nor scoped, and is not added to the reading-dependent count.

## 4. Who this helps
- **Day side.**
  - `pending` is not a verdict against him. Its only ground is that the audit has no aggregation rule (K-5).
  - It costs him a credit his own arithmetic earned: 32.3 follows from his inputs (B3d `holds`, 32.93, 1.95% off), and under the convergent reading the standard form records, the umbrella would hold (D-3).
  - The 0.743 defect is not charged again at B3. `pending` adds no error (counting note, §2 point 3).
  - Withdrawing the N/Nₑ leg costs him nothing under any reading (R-a = R-a′, R-b = R-b′). The audit does not penalise the self-correction.
  - His quotes' own words support a convergent structure: B3-3 says "not k = μ", and B3-2 is offered as confirming a k ≠ μ result (§2 point 1).
  - Recorded, not scored: every window B3c reports (0.60-0.87) keeps k below μ, so the direction reading R-b″ is open (D-2).
- **Critic side.**
  - `pending` is not `holds`: the umbrella gets no internal credit. Under the conjunctive reading R-b, which scores each quote as S1 does, the family fails internally on 0.743 (B3c).
  - The one quoted route that holds, 32.3, is externally `contradicted`: 2.25-3.38 per event, and a residual of 0.87-1.65 after the ancestral term (B3d, R4-B3). Its Yoo attribution is `misread` (A3x1).
  - B3-2's "confirming Balloux and Lehmann" is `misread`, sign opposite (B3c l.13).
  - B3-1 as quoted carries no k/μ, and its route was withdrawn by its own author (B3g).
  - The in-force values point in opposite directions. That is recorded and not scored (N2b own-text scope; rule C).
  - The ruling blocks a defensibility ranking over joinings, which would always hand the speaker the best of his quoted children (K-1). That guard applies to every side's umbrellas.
- **Both / the audit's own errors.**
  - The field has stayed `pending` from R4 B3 (2026-10-10) to now because the audit has no way to aggregate an umbrella's quotes. This write-up does not close that gap; it records the readings an owner rule would use.
  - The first draft (26dabc8) proposed `holds` under an extension of RD (C-1, K-1), wrote "as quoted" into a B3-1 mapping that does not hold (C-2), cited rule C for a scoping exemption (C-3), used the row-F double count as a ground (K-2), and left out B3b (C-4).
  - B3-1 has no Q-id in `quotes-*.md`, and the Z18429937 sentence that uses the ratio as k/μ is not quoted at B3 (S1 says the claim file should add it).
  - The Formal statement lists five values that are not quoted at the node, and the standard form's premise set differs from the quotes.
  - The title's "and their status" mixes the audit's inventory with Day's claim.

## 5. Proposed claim-file text (for the operator, after review; not applied)
Comment for l.12 (value unchanged):
```
  internal: pending   # R4 B3-internal (2026-11-26): the verdict depends on how the node aggregates its three quotes, not on how any quote is read; no current rule sets it (RD ranks readings of one quote; lead ruling, brief B3-analyst-2). A convergent joining would credit one quoted route only, B3-3 / 32.3 (B3d), whose external value is contradicted; that is not a finding that the values are consistent or that k != mu is shown. A conjunctive joining fails on B3-2 / 0.743 (B3c non-sequitur). B3-1 states only the N/N_e ratio; its k/mu use (B3a) is not quoted here (S1). Pending withholds an internal credit B3d earned on Day's own arithmetic; the reason is the audit's missing aggregation rule, not his error. Readings table in R4-B3-internal.md.
```
Readings table for the R4 paragraph:

| Reading | Tag | B3 internal |
|---|---|---|
| R-a convergent (some quoted route follows; rests on B3d alone) | dialectic | holds |
| R-b conjunctive (each quoted value follows) | dialectic | non-sequitur |
| R-b″ conjunctive on direction | dialectic | not scored (B3c's call) |
| R-c one consistent k/μ (extended) | dialectic | not scored (N2b own-text scope; rule C) |
| Field | | pending: no rule ranks joinings (R-a and R-b equal) |

Counts: B3 is **not** added to the reading-dependent verdicts (RD l.201) and is not scoped; it stays among the `pending` internal fields.

## Open (after fix pass 1)
1. Applicability: settled by the lead ruling (RD does not rank joinings; the value is `pending`). The aggregation rule itself is for the owner (one line on the owner card; ROADMAP B5 is related).
2. R-b″ is now a recorded row, unscored. Scoring it would need B3c re-scored against the direction rather than the number 0.743; out of scope.
3. S1 (l.40) asks for the verdict-bearing sentence to be quoted. The sentence in Z18429937 that uses B3-1's ratio as k/μ is not quoted at B3.

## Things that looked wrong
- B3-1 carries no k/μ in its own words. Its mapping to B3a comes from R4-B3g l.20 and versions ledger l.19, while B3a's own quotes come from Z18525547 and the 2026-02-04 blog. No B3-1 Q-id was found (grep of `quotes-*.md`).
- The brief names B3f and B3g as components. B3f is not quoted at B3, and its status is `extracted`, not `reviewed`. B3g is a withdrawal, not a route. Neither changes R-a or R-b.
- The component verdicts match the B3 claim file's l.12 comment. No contradiction was found, so the brief's stop condition did not apply. Fix pass 1 rechecked the cited lines (claim l.7, l.12-31; X1 l.15-17, 40, 63, 79, 196-202; B3b l.12-14; versions ledger l.19, l.35; standard form l.118-126; B3 and component fields at 9a2148b and 32df9cf): all match.

## Review resolution (fix pass 1, 2026-11-26)
Review: `REVIEW-R4-B3-internal-combined.md` (38e19ef). Lead ruling (brief B3-analyst-2): for C-1 / K-1, the proposal becomes `pending`; D-1 and the SCOPED route are declined. I agree with the ruling and have applied it. No component was re-scored, and no verdict field moves.

| Id | Severity | Resolution | What changed |
|---|---|---|---|
| C-1 | MAJOR | **Accepted**, fix (b) per the ruling | §2 proposes `pending` with §3's reason. §3 now says RD as written does not rank joinings. The SCOPED fix (a) is recorded as declined by the lead (choosing a joining by fiat; needs an owner rule) |
| C-2 | MAJOR | **Accepted** | B3-1 row: "none as quoted", a ratio with no k/μ and no Q-id (S1); B3a's `holds` scores Q38/Q39. R-a and R-b rows and §5 changed as the review asks. R-a states that it rests on B3d alone (wrong items 1, 2) |
| C-3 | MINOR | **Accepted** | R-c and §4: "N2b own-text scope (X1 l.63) and charity (rule C); versions ledger l.35" (wrong item 3) |
| C-4 | MINOR | **Accepted** | B3b (`holds / partial / supported`) added to the not-quoted list and to R-x, with the note that the standard form's premise set differs from the quotes (wrong item 5) |
| D-1 | MAJOR | **Not accepted**, per the ruling | R-b scores the node on its verbatim quotes (S1, l.40), so it is not an extended reading (l.202). D-1's ground (the quotes' own words) is kept in §2 point 1 as a record of structure, not as a ranking |
| D-2 | MINOR | **Accepted** | R-b″ added as a recorded, unscored row; in the §5 table and §4 Day side |
| K-1 | MAJOR | **Accepted** (C-1's fix, counted once) | §3 sets out the D-15 point; §4 critic side records the guard. The aggregation rule is one line for the owner card, not proposed here |
| K-2 | MAJOR | **Accepted** | §2 point 3 is now a counting note, not a ground, with the row-F precedent read the review's way (wrong item 4) |
| K-3 | MINOR | **Accepted** | §2 point 2 adds the 9a2148b and 32df9cf facts (checked with `git show`) and the "Steelman source" point |
| K-4 | MINOR | **Accepted**, adapted to `pending` | §5 comment rewritten: no `reading-dependent:` prefix and no `holds` value; it names the aggregation gap, the D-3 cost to Day, the one-route limit and the external `contradicted` limit |

Notes: C-5 applied as one clause (B3-1 row, Q105). D-3 recorded in §2, §4 and §5. D-4 and K-5 recorded in §4. Wrong item 6 is applied by C-1.
