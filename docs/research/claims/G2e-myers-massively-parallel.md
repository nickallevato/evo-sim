---
id: G2e
title: "Myers: evolution is a property of populations and involves massively parallel action on many traits and individuals"
side: critic
branch: G
parent: G2
edges: [{type: attacks, target: G2g}]
load_bearing: false
sourcing: firsthand
status: extracted
verdicts:
  internal: holds   # against the Dec 2025 abstract / Appendix A serial chain only, within this model (soft, multiplicative, free recombination); not applicable to G_f arithmetic (G1)
  fidelity: partial   # RD (2026-10-11): the RH-20 reading-dependence does not change this field (no claim node for PZ-04); see the Readings table
  external: contested
---

## Statement (verbatim)
> This is not how evolution works. Evolution is a property of populations and involves massively parallel action on multiple traits and individuals at once.

Source: [PZ Myers, "Vox Day’s amazing ego, and Bill Dembski don't care"](https://freethoughtblogs.com/pharyngula/2026/10/02/vox-days-amazing-ego-and-bill-dembski-dont-care/), 2026-10-02, para 5 (PZ-01).

> My criticism was that his math was invalid and that he thinks evolution is a simple serial process (the same thing Zach Hancock pointed out)

Source: [PZ Myers, "Vox Day responds to my criticism…"](https://freethoughtblogs.com/pharyngula/2026/10/04/vox-day-responds-to-my-criticism-of-his-refutation-of-evolution/), 2026-10-04, para 2 (PZ-05).


RH tag: PZ-01 dialectic (checkable claim); RH-20 ('I debunked Vox Day's stupid evolution "disproof" in one fairly short written post', PZ-04, ledger RH-20): **reading-dependent** (R4 RHclose-critics, RD, 2026-10-11); PZ-03 (citation count) dialectic and correct. Readings table in the R4 paragraph below.
## Formal statement
No numbers given. Qualitative statement of the parallel-action premise.

## Assumptions
- Stated: population-level parallel action.
- Implicit: that Day's math is serial (G2).

## Responses
- Against (Day): [They Never Stop Lying](https://voxday.net/2026/10/01/they-never-stop-lying/) (blog, 2026-10-01) ¶4, ¶19, ¶22: parallelism is built into G_f.
- In support: Good 2017: "multiple beneficial variants simultaneously competing for dominance in each population".
- Weaknesses in the responses: Myers says "Even worse, 7 of those citations are to the LTEE, and contradict his conclusions" (PZ-03; the count was checked in R4 RHclose-critics 2026-10-11: 11 entries, 7 LTEE-related, 2 ape-genome, exact match; 'contradict his conclusions' is evaluative and unscored); no calculation; Myers states elsewhere that he is "not a population geneticist" (PZ-06). The post addresses the paper as published 2026-10-02, before Day's clarifications of ¶22.

## Primary literature
| (none cited in the claim) | n/a | n/a |

## Pre-registered prediction
No prediction.

## Check
No script.

R4 G1 (research/checks/results/R4-G1.md): p^n is timing-independent, so a serial reading adds nothing to the Bernoulli arithmetic; the critique lands on the Appendix A chain (G2g), not on G_f (G1). Review: `research/checks/REVIEW.md` (review #5, 2026-10-08).

## Simulator variables implied
- None.

R4 RHclose-critics (research/checks/results/R4-RHclose-critics.md; integrated 2026-10-11). Myers, RH-20 / PZ-04 (2026-10-03 post, para 1) and PZ-03. Operational test: do the audit's own verdicts support the literal content (ADVERSE = internal non-sequitur/arithmetic-error, external contradicted, or fidelity misread; remotely close = share >= 1/3 over the units the reading names)? Readings (RD; the verdict-field reading is the one most charitable to Myers, M3):
| Reading of "the disproof" | Units and result | RH tag |
|---|---|---|
| M3 (extended: the Appendix A chain of Day's 2026-10-01 blog, "fixation must be sequential") | {G2g} non-sequitur, 1/1; the post does not quote Appendix A; Day's blog concedes the wording | dialectic (extended reading; cannot set the headline) |
| M2 (in-scope: the MITTENS 3.0 method the post names, 252,000 gen, 205M, 1,075,000-fold) | {A, G1} both `holds`: 0/2; MITTENS 3.0 s8.1 "The 45.4 fixations ... were not fixed one at a time" | rhetoric |
| M1 (Day's whole argument) | engaged {G2g, A, G1}; 0/24 load-bearing nodes adverse | uninformative (one post engages at most about 3 nodes, so it cannot return dialectic; a design property) |
| PZ-03 citation count (CX) | 11 / 7 / 2, exact; strict LTEE-population papers 6, still in band | dialectic, count correct (the earlier "not independently checked" note is closed) |
Headline: reading-dependent (rhetoric on the in-scope MITTENS 3.0 reading, dialectic on the Appendix A reading). Myers's description of MITTENS 3.0 as a sequential calculation is entered in the slip ledger with both readings (`ledgers/slips.md`, S-G2e-1): R1 error on the literal reading, slip on the conditional reading ("That's true, if each trait has to wait ..."). Credit to Myers: his objection is correct against Appendix A's serial chain (G2g non-sequitur) and the citation count is exact. Credit to Day: the post's maths are about 12% of its 1,686 words and do not engage the paper's G_f parallel counting, so 'debunked' is not supported on the in-scope method reading.
