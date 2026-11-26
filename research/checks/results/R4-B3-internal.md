# R4 B3-internal: rule RD on the B3 umbrella's internal verdict

**Status: write-up only; awaiting one combined review (D-40). No verdict field moves here.** Brief: `research/checks/briefs/B3-analyst-1.md` (3f0c53e). Gap item B3, field `verdicts.internal` of `docs/research/claims/B3-k-neq-mu-values-umbrella.md` (l.12, `pending`: "components differ ... no single value").

## Files and inputs
- No script, no run and no fetch. This is a reading analysis of component verdicts that are already settled. Nothing here was registered in advance, so no prediction is scored. Every verdict below is cited as it stands at 3f0c53e and is **not re-scored**.
- Rule text: `R4-X1-verdict-rule.md` RD (l.196-202), S1 (l.40), SC (l.47), row F (l.79). D-15 (`DECISIONS.md` l.31).
- Prior write-ups: `R4-B3.md` ("What this means for B3"), `R4-B3g.md` (l.20, "What the concession removes"). Versions ledger l.19, l.35. Standard form B3 (`argmap/standard-forms.md` l.118-126).

## What B3 scores (rule S1)
S1 scores a node "on its verbatim Statement quotes and the derivation chain in its Formal statement". B3 quotes three statements (claim file l.17-29). All three carry one RH tag, `dialectic` (l.31; R4-B3 status line).

| Quote | Words | Source | Component that scores it | Component internal (as it stands) | In force? |
|---|---|---|---|---|---|
| B3-1 | "census populations exceed diversity-derived N_{e} by 19- to 46-fold" | Z18429937, 2026-01-29 (no Q-id) | the ratio itself: none ("untouched and external", R4-B3g l.20). Its use as a k/μ factor: **B3a** (k = μN/Nₑ; versions ledger l.19 lists Z18429937 among the sources of that formula) | B3a `holds` (B3a l.12) | No. Withdrawn by Day on 2026-08-27 (**B3g** `holds` / `accurate` / `supported`). Under SC it is scored on the version quoted, with the note "corrected in B3g" (X1 l.47) |
| B3-2 | "it yields k = 0.743μ, confirming Balloux and Lehmann's finding" (Q41) | Z18525262, 2026-02-08 | **B3c** | `non-sequitur` (N2a: 0.743 is a property of the four-cohort window; the paper's own growth ratio gives 0.60-0.87; B3c l.12) | Yes |
| B3-3 | "gives k = 32.3μ, not k = μ" (Q43) | blog 2026-10-01 | **B3d** | `holds` (32.93 from Day's own inputs, 1.95% off; B3d l.12) | Yes |

The Formal statement table lists more values, but none of them is quoted in the Statement, so under S1 none sets B3: 800,000 (**B3f** `holds`, status `extracted`), 15.2-30.3 and 9.1-30.3 (B4 `holds`), "median 25" (B3m `n/a`), ≈0.5 (Q42, no claim file) and 1 (B3g). They appear only in the extended row R-x below.

## 1. Readings table
| Id | Reading of the three quotes taken together as one internal claim | RH tag | B3 internal | Component verdicts it rests on |
|---|---|---|---|---|
| **R-a** | **Convergent.** The quotes are independent routes to "k ≠ μ", each offered alone in its own source. The node's conclusion follows if at least one route follows from its author's own material. This is the inference the standard form has recorded since 9a2148b (2026-10-08): "Inference: convergent" | dialectic | **holds** | B3d `holds` (B3-3). B3a `holds` (B3-1, as quoted; corrected in B3g). B3c's `non-sequitur` (B3-2) defeats its own route, not the conclusion |
| R-b | **Conjunctive.** Each quoted value follows from its source's own material | dialectic | non-sequitur | B3c `non-sequitur` (B3-2); B3a, B3d `holds` |
| R-c | **Extended (a wider claim): the values form one mutually consistent k/μ.** No quote asserts this | dialectic | n/a: not scored. 0.743 and 32.3 measure different windows (rule C; versions ledger l.35). The cross-document basis is not used (B3c l.12) | versions ledger l.35 |
| R-a′ | Sensitivity: R-a restricted to the routes still in force after B3g (B3-2, B3-3) | dialectic | holds | B3d |
| R-b′ | Sensitivity: R-b restricted to the routes in force | dialectic | non-sequitur | B3c |
| R-x | Extended (other objects): every value in the Formal statement table | dialectic | convergent: holds (B3a, B3d, B3f, B4); conjunctive: non-sequitur (B3c); ≈0.5 unscored | as listed |

Dropping the withdrawn leg moves no reading (R-a = R-a′, R-b = R-b′). B3g bears on B3's external field, not its internal field.

## 2. Field value
**Proposed: `holds`, reading-dependent, under R-a.** R-b (`non-sequitur`) is recorded beside it. R-c and R-x are extended readings: they are reported but cannot set the field (RD l.202).

Why R-a is the reading under which the quoted statements are most defensible (D-15: "closest to literally true, best supported"), and not just the reading with the best verdict for Day:
1. **Text.** Three sources, eight months apart, each give their own value and draw their own conclusion. B3-3 ends "not k = μ". None cites or needs another, and they cannot need each other because they disagree in direction (0.743 < 1 < 32.3). The only claim they share is "k ≠ μ". A reader who joins independent supports for one conclusion reads them as convergent unless one premise needs another. R-b scores a conjunction that no source states.
2. **Not chosen by verdict.** The convergent classification was recorded on 2026-10-08. That was before RD (2026-10-11) and before anyone asked what B3's value should be. The ground is structural.
3. **Counting.** Under R-b, B3-2 would be charged twice, at B3c and again at B3. X1 row F (l.79) removed such a double count: "already `non-sequitur` there, so F counted it twice". The precedent is analogous, not identical: F did not quote F1a's step, while B3 does quote B3-2.

What `holds` says: Day's quoted case for k ≠ μ contains at least one route that follows from his own inputs. It says nothing about the world: external stays `contradicted` (B3 l.14). It adds no new finding beyond B3d and B3a.

## 3. Applicability: RD, SCOPED, or neither
RD's trigger is written for one quote: "where a verdict ... depends on how a quote is read" (l.197). Here no single quote's reading is in doubt, because each one is fixed in its component file. What is in doubt is how to read the node's Statement block (three quotes under one RH tag and one verdict field) as one statement. I read RD as covering this case: S1 treats the block as the node's statement, and the node's verdict depends on how that block is read. B3 is not `SCOPED`. Its Formal statement (l.32-44) is a table of values and statuses that names no single proposition, so it fixes neither R-a nor R-b. The case against applying RD is real. Under R-a and R-b every quoted sentence is read the same way and is exactly as defensible. The readings differ only in how the audit joins them, so RD can rank them only through the structural argument in §2 (point 1), not through any quote's words. **If the review finds that argument insufficient, RD cannot set the field, and the proposal falls back to `pending`** with the reason "the verdict depends on how the node aggregates its quotes, not on how any quote is read; no current rule sets it". In that case, what can set it is a Formal statement that names the node's proposition (for example the standard form's C with "Inference: convergent"). That would make B3 SCOPED (RD l.198). It is a claim-file edit that needs one lead ruling in the fix-pass brief, not a new rule.

## 4. Who this helps
- **Day side.**
  - Under the reading the audit's own standard form already uses, his case for k ≠ μ has an internally sound route. 32.3 is his arithmetic on his own inputs (B3d). The N/Nₑ algebra was internally valid as quoted (B3a), and he withdrew it himself (B3g).
  - The 0.743 defect is charged once, at B3c, not again at B3.
  - Withdrawing a leg costs him no internal value here (R-a′). The audit does not penalise the self-correction.
  - Not re-scored, recorded for the review: every window B3c reports (0.60-0.87) keeps k below μ (Open 2).
- **Critic side.**
  - `holds` is internal only. The one route in force that holds, 32.3, is externally `contradicted`: 2.25-3.38 per event, and a residual of 0.87-1.65 after the ancestral term (B3d, R4-B3). Its Yoo attribution is `misread` (A3x1).
  - B3-1's route was withdrawn by its own author (B3g).
  - Under the conjunctive reading (R-b) the family fails internally on 0.743.
  - The in-force values point in opposite directions. That is recorded under rule C and not scored.
  - So `holds` must not be shown as "the family is consistent" or "k ≠ μ is shown". It rests on a single in-force route.
- **Both / the audit's own errors.**
  - The field stayed `pending` from R4 B3 (2026-10-10) to now because the audit had no way to aggregate an umbrella's quotes. This is the gap the fallback in §3 names.
  - B3-1 has no Q-id in `quotes-*.md`.
  - The Formal statement lists five values that are not quoted at the node.
  - The title's "and their status" mixes the audit's inventory with Day's claim.

## 5. Proposed claim-file text (for the operator, after review; not applied)
Comment for l.12:
```
  internal: holds   # reading-dependent: holds under R-a (convergent, standard-forms.md B3: the three quotes are independent routes to k != mu; B3-3 / 32.3 holds on Day's inputs, B3d; B3-1's N/N_e route holds as quoted, B3a, corrected in B3g); non-sequitur under R-b (each quoted value holds; B3-2 / 0.743 is a window property, B3c); R-c (one consistent k/mu) extended, not scored (rule C, versions ledger). No reading moves if the withdrawn leg is dropped. Readings table in the R4 B3-internal paragraph (R4-B3-internal.md).
```
Readings table for the R4 paragraph:

| Reading | Tag | B3 internal |
|---|---|---|
| R-a convergent (some quoted route follows): field | dialectic | holds |
| R-b conjunctive (each quoted value follows) | dialectic | non-sequitur |
| R-c one consistent k/μ (extended) | dialectic | not scored (rule C) |

Counts: add B3 to the reading-dependent verdicts (RD l.201).

## Open (for the review)
1. Applicability (§3): can RD's criterion rank readings that differ only in how the quotes are joined? If it cannot, the value is `pending` and a lead ruling on the Formal statement is the route.
2. A reading R-b″, "each route gives the direction k ≠ μ", would need B3c re-scored against the direction rather than the number 0.743. That is out of scope and not done.
3. S1 (l.40) asks for the verdict-bearing sentence to be quoted. B3-1 states only a ratio; the sentence in Z18429937 that uses it as k/μ is not quoted at B3.

## Things that looked wrong
- B3-1 carries no k/μ in its own words. Its mapping to B3a comes from R4-B3g l.20 and versions ledger l.19, while B3a's own quotes come from Z18525547 and the 2026-02-04 blog. No B3-1 Q-id was found (grep of `quotes-*.md`).
- The brief names B3f and B3g as components. B3f is not quoted at B3, and its status is `extracted`, not `reviewed`. B3g is a withdrawal, not a route. Neither changes R-a or R-b.
- The component verdicts match the B3 claim file's l.12 comment. No contradiction was found, so the brief's stop condition did not apply.
