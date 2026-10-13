---
id: A4d
title: "MITTENS 3.0 drops d and uses 252,000 nominal generations"
side: day
branch: A
parent: A4
edges: [{type: revises, target: A4}, {type: supersedes, target: A}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds   # R4 VID-01-score (2026-10-13): re-verified against a re-fetched, sha256-matched MITTENS 3.0 (22bb4ef8...). Exhaustive token search of body + addendum: 0 standalone `d`, 0 "0.45", 0 "450,000", 0 "selective turnover"; "252,000" 10x, never multiplied. The GGR-13/GGR-14 charge is contradicted under its reading (b) and governed by reading (a). Not reading-dependent: the text settles it under every reading
  fidelity: n/a
  external: pending
---

## Statement (verbatim)
> Applied to human-chimpanzee divergence (205 million required fixations on the human lineage across 252,000 available generations), the shortfall is 1,075,000-fold for non-mutators and 104,873-fold across all twelve populations including hypermutators.

Source: [MITTENS 3.0, Zenodo 23003785](https://zenodo.org/records/23003785) (key Z23003785), 2026-09-28 (modified 2026-10-04), p.1 (abstract). The 3.0 text has no d term. Originally searched "turnover" and "d ="; re-verified 2026-10-13 (R4 VID-01-score) against a re-fetched copy whose sha256 matches the pinned `bib-day.md` value, with the search widened to "turnover", "d =", "d=", "0.45", "Bio-Cycle", "overlapping generations", "450,000", "225,000", "202,500", "252,000", "selective turnover", "d coefficient", and a standalone-`d` regex over the body **and** the addendum: no d term in either. Quote re-verified verbatim.


RH tag (2026-10-10 pass): dialectic (stated as a checkable claim or derivation; no rhetorical device scored).
## Formal statement
F_max(3.0) = 252,000 / 1,322 = 190.6, with no d. `derived:` had d = 0.45 been applied: 252,000 x 0.45 = 113,400; /1,322 = 85.8; shortfall 205e6/85.8 = 2.39e6 (2.2x larger than 1.075e6). Dropping d is therefore conservative with respect to the claim. The versions ledger notes d = 0.45 in both Zenodo papers of Dec 2025 computed on different loci (A4a).

## Assumptions
- Stated: none (d is not mentioned).
- Implicit: nominal generations are the right unit; or the d correction is subsumed into the empirical G_f (the LTEE is asexual and discrete).

## Responses
- Against: Hössjer (HO-01, HO-04) still uses d = 0.45 in his reproduction (published 2026-09-14, before 3.0).
- In support: Camestros's objection to d (A4b) no longer applies to the 3.0 numbers.
- Weaknesses in the responses: the 3.0 paper offers no reason for dropping d; the human-derived rate (A5e) is calculated using the "Bio-Cycle correction for overlapping generations", so the correction is still invoked in 3.0 elsewhere. **Locator corrected 2026-10-13 (R4 VID-01-score):** this line previously said "the later 'Appendix D' human-derived rate", which reads as though MITTENS 3.0 contains an Appendix D. It does not — the paper runs s1-s9 plus a separate addendum. The citation sits in the **body**, s8.6: "The human-derived fixation rate, calculated independently from human parameters alone using Kimura's fixation time formula and the Bio-Cycle correction for overlapping generations, yields approximately one fixation per 27,600 effective generations (Day and Athos 2025, Appendix D)." The Appendix D is *Day and Athos 2025*'s, not 3.0's.
- From the critics (GG-4, 2026-10-13): the panel grants Day's stated intent at the d step - "Remember how D was one earlier? This goes back to the whole he's trying to give conventional science the bestcase scenario numbers" (GGR-46, t=01:51:34). Credit to Day on the charity question; the panel disputes the variable, not the intent. (Belongs in A4's Responses too; A4 was outside the scoring task's file list.)

## Primary literature
| (none cited in the claim) | n/a | n/a |

## Pre-registered prediction
Arithmetic only (above).

## Check
Arithmetic audit (python3 -I, scratch). Review: pending.

R4 VID-01-score (`research/checks/results/R4-VID-01-score.md`, 2026-10-13; predictions pre-registered
at commit `e857d1f` before the text was re-fetched). The Gutsick Gibbon roundtable (GG-4, video
`AqC1ZM4icms`) says Day "is still using the de coefficient in mittens" (GGR-13, t=01:50:52) and
"he calculates it at 450,000 generations and then he multiplies it by the D coefficient in order to
cut it almost in half to like 225,000 generations or whatever and he's still using that number for
all his math" (GGR-14, t=01:51:14). The MITTENS 3.0 text had been lost from `sources/raw/`; it was
re-fetched read-only into its own new directory, its sha256 matched the pinned `bib-day.md` value
(`22bb4ef8...`; addendum `d55e8a03...`), and the search above was re-run over body and addendum.
**Result: no d term anywhere.** 0 standalone `d` tokens, 0 "0.45", 0 "450,000", 0 "225,000",
0 "202,500", 0 "selective turnover"; "252,000" occurs 10 times and is never multiplied by anything
("The divergence time is 6.3 million years. At 25 years per human generation, this provides 252,000
generations", s7.1). The single "turnover" hit is "not gross turnover" (s4.2), unrelated.
**Verdict unchanged: `internal: holds`,** now verified against a hash-matched text rather than
resting on a search of a file the audit no longer had.

Readings of the critic statement GGR-13/GGR-14 (rule RD; the three readings were recorded by lead
ruling R-3 with no winner declared, and are settled here):

| Reading | "mittens" denotes | Against the verified 3.0 text | Verdict of the quoted statement |
|---|---|---|---|
| (a) | the pre-3.0 / *Probability Zero* line | 450,000 x 0.45 = 202,500, "like 225,000 or whatever"; this is the audit's own TW-01 figure (`A-mittens-formula.md`; A4 `derived:`) | accurate |
| (b) | the MITTENS 3.0 body | contradicted: no d, no 0.45, 252,000 used uncut | contradicted |
| (c) | 3.0 "including Appendix D" | 3.0 has no Appendix D; s8.6 of the body cites *Day and Athos 2025*, Appendix D, for a rate built on the Bio-Cycle overlap correction, so an overlap correction **is** still in play - but not as a multiplier on generations | partly accurate |

Governing reading under RD (the reading under which the *quoted statement* is most defensible, not
the one best for either side): **(a)**, corroborated by the host's own narration in the same segment,
"He kind of throws the D coefficient off to the side. It no longer seems nearly as important as it
was in probability zero" (t=01:49:52). Under (a) there is no conflict with this claim.

**This verdict is not counted as reading-dependent**, and no `reading-dependent:` comment is added.
Rule RD governs a verdict that *depends* on how a quote is read; this one does not: the re-fetched
text settles that 3.0 has no d term under every reading. What is reading-dependent is the critic
statement GGR-13/GGR-14, which has no claim file of its own, so its Readings table is recorded here.
The scoring task flagged this as a deliberate departure from its own registration for its three
reviewers to rule on; if they rule otherwise the change is one comment line and one count.

For the critics, recorded as prominently: reading (c) is partly right and this claim's own
Weaknesses line already said so - Day drops d from the generation count while the rate he cites at
s8.6 is still computed with a "Bio-Cycle correction for overlapping generations", and 3.0 nowhere
explains that. GGR-14's arithmetic (450,000 x 0.45) is exactly the audit's TW-01.

## Simulator variables implied
- d toggle (already specified in A4).
