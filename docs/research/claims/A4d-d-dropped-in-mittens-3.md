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
  internal: holds   # R4 VID-01-score (2026-10-13), fix pass under lead rulings R-8/R-9/R-10/R-13: re-verified against a re-fetched, sha256-matched MITTENS 3.0 (22bb4ef8...). Token search of body + addendum: 0 lowercase `d` tokens case-sensitively (case-insensitively 3 in main, all "Appendix D" citations or an author initial, none a coefficient), 0 "0.45", 0 "450,000", 0 "selective turnover"; "252,000" 10x, never multiplied, and s8.6 applies its cited rate to the full 252,000. **3.0 contains no d term and applies no d multiplier to its generation count; an overlap correction survives by citation inside the s8.6 rate** (a token search establishes the absence of the symbol, not the absence of the correction). GGR-14's elaboration is contradicted under both in-scope readings; GGR-13's core assertion is accurate as to the s8.6 step. Reading (c) governs among in-scope readings; reading (a) is an extended reading and may not set the field or headline (rule RD line 202). SCOPED, not reading-dependent (rule RD line 198: the Formal statement fixes the reading)
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
- In support (hostile source; **added 2026-10-13 in the R4 VID-01-score fix pass, Day-side steelman MAJOR-3, hard rule 1**): a panellist's own summary of 3.0 corroborates this claim's central fact - "In mittens 3.0, he completely retracts all of his arguments with regard to the census population size versus the effective population size" (GGR-11, t=01:49:52) and, in the same turn, "He kind of throws the D coefficient off to the side. It no longer seems nearly as important as it was in probability zero". Speaker **unnamed** (`panel`; the turn runs t=01:47:28-01:51:34 unbroken with no name spoken for the speaker), **not** "the host" - the earlier wording here asserted an attribution the audit itself struck on 2026-10-13 (EVO-69 fix pass, MINOR-1). This turn is **not** corroboration for reading (a) of GGR-13/GGR-14: the panellist is speaking about 3.0 and GGR-13 is the solicited reply disagreeing with him ("Does that sound right to you, especially Grayson?"). What it shows is that **the panel is internally split about 3.0** - which is itself a point for Day, and is why it sits under In support.

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
**Result: no d term in the text and no d multiplier on the generation count.** 0 lowercase `d`
tokens case-sensitively (case-insensitively 3 in main.txt - "Appendix D)" 653, "Appendix D." 724,
"Yoo D, et al." 738: two citations and an author initial, none a coefficient; correction made in
the fix pass, correctness MINOR-1), 0 "0.45", 0 "450,000", 0 "225,000",
0 "202,500", 0 "selective turnover"; "252,000" occurs 10 times and is never multiplied by anything
("The divergence time is 6.3 million years. At 25 years per human generation, this provides 252,000
generations", s7.1). The single "turnover" hit is "not gross turnover" (s4.2), unrelated. **What a
token search can and cannot establish (R-13):** it establishes the absence of the *symbol* d, not
the absence of the *correction* - s8.6 imports a Bio-Cycle-corrected rate by citation to a document
outside the fetched corpus (see the Readings table and the Weaknesses line).
**Verdict unchanged: `internal: holds`,** now verified against a hash-matched text rather than
resting on a search of a file the audit no longer had.

Readings of the critic statement GGR-13/GGR-14 (rule RD; the three readings were recorded by lead
ruling R-3 with no winner declared, and are settled here):

**Revised 2026-10-13 in the fix pass under lead rulings R-8, R-9 and R-10.** The two quoted
sentences are scored as **separate propositions** (they are not the same assertion), and reading (a)
is **struck as governing** while keeping its verdict.

| Reading | "mittens" denotes | Against the verified 3.0 text | GGR-13 "still using the de coefficient in mittens" | GGR-14 "calculates it at 450,000 ... multiplies it by the D coefficient ... still using that number for all his math" |
|---|---|---|---|---|
| (a) — **extended reading, may not govern (rule RD line 202)** | the pre-3.0 / *Probability Zero* line, **a different object** from the paper under discussion | 450,000 x 0.45 = 202,500, "like 225,000 or whatever"; this is the audit's own TW-01 figure (`A-mittens-formula.md`; A4 `derived:`) | accurate | accurate |
| (b) | the MITTENS 3.0 body | no lowercase `d` token, no 0.45, 252,000 used uncut, including at s8.6 ("Applied to 252,000 generations provides 8 achievable fixations", main:653-654) | contradicted | contradicted |
| (c) — **governs among in-scope readings** | 3.0 as it stands, **including what it incorporates by citation** | 3.0 has no Appendix D of its own; s8.6 of the body cites *Day and Athos 2025*, Appendix D, for a rate "calculated ... using Kimura's fixation time formula and the **Bio-Cycle correction for overlapping generations**", quoted in "**effective generations**" - the unit `C2-bio-cycle-d.md` defines as `g_eff = d x g_nominal`. "effective generation" occurs exactly once in body and addendum, main:653 | **accurate** as to that step: the d correction is still in play in 3.0, inside the 27,600 rate | **contradicted**: `450,000`, `225,000`, `202,500`, `0.45` are 0 hits and 252,000 is never cut |

**Governing reading: (c)**, giving the quoted statement the headline grade **`partial`** (fidelity vocabulary; "partly accurate" in the R-8 wording, normalised at integration) -
accurate core, inaccurate elaboration. Rule RD line 202: "Extended readings (a different object, or
a wider claim) are reported with their own verdicts but cannot set the verdict field or the headline
tag." Reading (a) is a different object, so it is recorded above with its `accurate` verdict and is
**struck as governing**; (b) and (c) are the same object at two scopes and (c) is the scope under
which the quoted statement is most defensible. The earlier version of this paragraph made (a)
governing and cited "the host's own narration" as corroboration; **both are withdrawn** (R-9, R-10)
- see the Responses entry above for what that turn is and what it actually shows.

**What the s8.6 arithmetic settles:** the printed "8 achievable fixations" reconciles with neither
candidate exactly - 252,000/27,600 = 9.13 (a 12% gap `A5e` line 26 already records as unreconciled)
and 113,400/27,600 = 4.11 (off by a factor of two) - so it does not prove the absence of d, but it
is consistent with the **uncut** 252,000 and not with a d-cut count.

**This verdict is not counted as reading-dependent**, and no `reading-dependent:` comment is added.
The reason is named by its clause: rule RD line 198 - "A claim whose **formal statement fixes the
reading** (A2e, a count) is **`SCOPED`, not reading-dependent**" - and this claim's Formal statement
is exactly such a fix ("F_max(3.0) = 252,000 / 1,322 = 190.6, with no d"). What is reading-dependent
is the critic statement GGR-13/GGR-14, which has no claim file of its own, so its Readings table is
recorded here. All three reviews and the lead upheld the scoring task's departure from its own
registration on this point; **the defect was in the registration, not in the execution** (D-24
ruling R-15).

For the critics, recorded as prominently: under the governing reading (c), **GGR-13's core assertion
is accurate, not merely "partly right"**. The single human-derived throughput number in MITTENS 3.0
is, in the paper's own words, computed with the Bio-Cycle correction and expressed in *effective*
generations, so the d correction is still in play in 3.0 by citation, and the paper nowhere
reconciles a rate per effective generation divided into a nominal count. s8.6 answers what the paper
itself calls "the most persistent objection to MITTENS". Day gives no reason for dropping d after
building Z18203514 on the claim that population genetics cannot handle overlapping generations.
GGR-14's arithmetic (450,000 x 0.45) is exactly the audit's TW-01. **Audit error recorded against
itself (R-13):** the scoring task's headline "MITTENS 3.0 is clean of the d coefficient by an
exhaustive token search" overstated what a token search can establish and is corrected in the
verdict comment above; it is **the third standing audit error against the critics from this source**.

## Simulator variables implied
- d toggle (already specified in A4).
