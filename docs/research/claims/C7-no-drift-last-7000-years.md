---
id: C7
title: "Day: 'genetic drift isn't happening at all over the last 7000 years', from the aDNA near-zero fixation counts"
side: day
branch: C
parent: C
edges: [{type: depends-on, target: C}, {type: supports, target: B2}]
load_bearing: false  # comment-level restatement of C
sourcing: firsthand
status: reviewed
verdicts:
  internal: non-sequitur   # reading-dependent (RD, owner 2026-10-11; value = the reading under which the quoted statement is most defensible, i.e. closest to literally true (D-15), here the fixation reading): fixation reading -> non-sequitur (the count is true; the inference 'so drift is not happening' is the non-sequitur at C: few or no fixations from intermediate frequency in ~280 generations is what neutral drift predicts at N_e ~ 1e4, claim C, R4 C1/C1b); strict allele-frequency drift reading -> n/a (rhetoric, unscored); census reading -> pending a sourced census (flips at about 8.2e5)
  fidelity: n/a
  external: contradicted   # reading-dependent (RD): fixation reading -> the count itself is supported (P about 1e-17 for a fixation from p0 = 0.5 in 280 generations), the conclusion 'drift isn't happening' is contradicted: R4 C1d measures F_adj 0.002-0.014 between AADR bins (28-250 generations), far from zero (attribution to drift vs admixture, structure and composition stays open, B2e); strict reading -> n/a (rhetoric); census reading -> pending
verdict_scope:
  internal: "Scope: the fixation reading governs - the count is true and the inference \"so drift is not happening\" is the non-sequitur at C; the strict allele-frequency drift reading is `n/a` (rhetoric, unscored) and the census reading is pending a sourced census (flips at about 8.2e5)"
  external: "Scope: the fixation reading governs - the count itself is supported (P about 1e-17 for a fixation from p0 = 0.5 in 280 generations) and the conclusion \"drift isn't happening\" is contradicted by R4 C1d (F_adj 0.002-0.014 between AADR bins, 28-250 generations), with attribution to drift vs admixture, structure and composition left open at B2e; strict reading `n/a` (rhetoric), census reading pending"
---

## Statement (verbatim)
> "And we've now got hard evidence that genetic drift isn't happening at all over the last 7000 years, and that there is a hard population limit on the neutral pipeline."

Source: [Vox Day, comment on McCarthy, "Why Probability Zero is Wrong About Evolution"](https://dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1/comment/335823489), 2026-09-13, comment id 335823489 (Q96).


RH tag: **reading-dependent** (R4 RHclose, owner rule 'remotely close' 2026-10-11, RD). Fixation reading ('drift is not producing fixations'): dialectic, literally true as a count. Strict allele-frequency drift reading (F_drift 0.0070-0.0139 over 280 generations at N_e 1e4-2e4, 23-46x the 3e-4 edge): rhetoric. Census reading (HL l.101-118 variance frame): pending a sourced European census; dialectic iff the census is at least about 8.2e5 held for 7,000 y (the repo's sourced Holocene N_e point the other way).
## Formal statement
From "~0 fixations from intermediate frequency in ~7,000 years" (C) to "no drift". `derived:` neutral fixation time from frequency x is of order 4N_e x-weighted, i.e. tens of thousands of generations at N_e ~ 1e4, against ~280 generations in the window, so ~0 completions from <50% is the neutral expectation (C's internal verdict).

## Assumptions
- Stated: the aDNA counts (C) and the Hard Limits ceiling (B2).
- Implicit: drift is detected only by completed fixations.

## Responses
- Against: claim C internal "non-sequitur" (neutral also predicts ~0); C5b and B2e (keruru: measurable temporal frequency change gives N_e ~ 8,000-10,000).
- In support (for Day): admixture dominates frequency change in the window, so drift is hard to isolate there (C1c in progress).
- Weaknesses in the responses: keruru's draft lacks ancestry control (RF-16 note).

## Primary literature
None cited.

## Pre-registered prediction
Covered by C1/C1b/C1c.

## Check
R4 C1d (research/checks/results/R4-C1d.md §4, review #10, 2026-10-09): on the real AADR genotypes allele frequencies change between dated bins (F_adj 0.002-0.014 across 28-250 generations; keruru's temporal N_e replicates within 1-8%), so "no drift" in the sense of no frequency movement is contradicted. Whether the movement is drift or admixture/composition is open: composition among five regions explains 6-17% of the BA-to-Medieval F, and within-region N_e (3.4k-14.6k) does not move toward a no-drift reading. C1c: the stasis edge (N_e -> infinity) gives about 2-5 post-6000 events against 21 observed; Day's other position (C5a, N_e near 2) predicts no polymorphism and is excluded by the measured F.

None separate. Precedes Day's Z23046531 counts (2026-09-29: 1 and 3 completions). From the 2026-10-09 corpus refresh (D-5a).

## Simulator variables implied
Admixture pulses; sampling depth per time bin (C1c).

R4 RHclose (research/checks/results/R4-RHclose.md; combined review `REVIEW-R4-RHclose-combined.md`; fix pass 3c0dccb, post hoc `rhclose_posthoc.py`; integrated 2026-10-11). Readings of Q96 "genetic drift isn't happening at all", one RH tag per reading, none picked (RD):
| Reading | Result | RH tag | Internal / external |
|---|---|---|---|
| R3 Fixation count (verdict field; most defensible reading, D-15) | P(fixation from p0 = 0.5 in 280 gen) <= 1e-17 at N_e 1e4-2e4; p0 = 0.9 upper bound 2e-3 / 3e-5 | dialectic (true as a count; also the neutral expectation, claim C row) | non-sequitur (inference to 'no drift', X1 row C) / contradicted (conclusion; the count itself is supported) |
| R1 Strict allele-frequency drift (registered) | F_drift 0.0070-0.0139 in 280 gen, 23-46x the 3e-4 edge (growth rows 40x and 17x; 10x edge leaves 7.0x) | rhetoric | n/a / n/a (the C1d measurement and the C-basis non-sequitur move to the dialectical core, C and B2) |
| R2 Census frame | census about 8.2e5 needed (N_e 466,597); about 2.4e5 for the 1e-3 edge; census unsourced | pending (dialectic iff census >= 8.2e5 for 7,000 y; not adopted, the repo's Holocene N_e point the other way) | pending / pending |
The second clause ("a hard population limit on the neutral pipeline") is tagged B2 (current-size confinement, `holds`). Practical effect: C keeps its own `non-sequitur` (X1 row C) and B2 its `holds` under every reading; only this duplicate node moves. Ledger entry: `ledgers/slips.md` RH-25.
