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
  internal: non-sequitur   # few or no fixations from intermediate frequency in ~280 generations is what neutral drift predicts at N_e ~ 1e4 (claim C, R4 C1/C1b); it does not imply no allele-frequency drift
  fidelity: n/a
  external: contradicted   # for 'no allele-frequency movement': R4 C1d measures F_adj 0.002-0.014 between AADR bins (28-250 generations), far from zero; attribution to drift vs admixture, structure and composition stays open (B2e)
---

## Statement (verbatim)
> "And we've now got hard evidence that genetic drift isn't happening at all over the last 7000 years, and that there is a hard population limit on the neutral pipeline."

Source: [Vox Day, comment on McCarthy, "Why Probability Zero is Wrong About Evolution"](https://dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1/comment/335823489), 2026-09-13, comment id 335823489 (Q96).

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
