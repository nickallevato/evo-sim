---
id: DN4
title: "Day: at dN/dS = 0.80 natural selection is not the primary mechanism of adaptive evolution"
side: day
branch: ROOT
parent: ROOT-FM
edges: [{type: supports, target: ROOT-FM}, {type: depends-on, target: DN1}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: non-sequitur   # R4 L1 fix pass (reviews a352991, correctness and critic-side), (N2d, own source): ¶6 defines the ratio as purifying removal ('If natural selection is purifying and removes harmful mutation then Ka/Ks should be well below 1.0'), ¶20 reads 0.80 that way, ¶21 concludes about adaptive evolution. Charitable reading 'most coding substitutions are not selection-driven' follows from 0.80 but equally from 0.23 under neutral theory, so it does not carry the stated words
  fidelity: n/a   
  external: contested   # R4 L1 fix pass; verdict set at integration: (not contradicted merely because premise DN1 is): on the literal words, adaptive change is selection-driven and human alpha estimates (A2e-alpha, bias-corrected ~9-13%) show it occurs; on the charitable reading the same estimates agree most coding substitutions are not adaptive
---

## Statement (verbatim)
> At dN/dS = 0.80, natural selection is not the primary mechanism of adaptive evolution.

> A dN/dS of 0.80 means purifying selection is removing only about 20% of nonsynonymous mutations. At that level, selection is barely distinguishable from neutral evolution.

Source: [Day, "How Biologists Keep 'Proving' Selection"](https://voxday.net/2026/10/11/how-biologists-keep-proving-selection/), 2026-10-11, ¶21 and ¶20 (Q177). RH tag: dialectic. "We already have fairly good evidence showing that it is not the secondary mechanism either. It may not even be the tertiary one." is rhetoric (RH-23).

## Formal statement
P1 dN/dS = 0.80 genome-wide (DN1). P2 [implicit] the dN/dS average measures how much selection shapes coding change. C selection is not the primary mechanism of adaptive evolution.

## Assumptions
- Implicit: P2. Under the standard reading, 1 - dN/dS is the fraction of nonsynonymous changes removed by purifying selection (Day uses this reading himself, ¶20); adaptive evolution is a different quantity (alpha, McDonald-Kreitman).

## Responses
- Against (audit steelman for the critics, x:dnds-steelman-critic; no critic has replied): even at 0.80, purifying selection removes ~20% of amino-acid changes, and dN/dS says nothing about which fixed changes were adaptive; alpha estimates (A2e-alpha) address that.
- In support (Day): his reading of 1 - dN/dS as the purged fraction is the textbook reading, and it is applied consistently to both 0.23 and 0.80.
- Weaknesses in the responses: the critic-side steelman is the audit's.

## Primary literature
McDonald and Kreitman 1991; Messer and Petrov 2013 (abstract level, test-methods review entry 9).

## Pre-registered prediction
None (not computed).

## Check
R4 L1 fix pass (`research/checks/results/R4-L1.md`, Verdicts section): rule N scored from Day's own ¶6, ¶20 and ¶21 of the same post; no computation. Day-side charitable reading recorded (steelman-day #7). **Integrated 2026-10-11:** internal non-sequitur (N2d, own source), fidelity n/a, external contested (not scored contradicted merely because DN1 is).

## Simulator variables implied
- per-site selection classes (neutral, purifying, adaptive) needed to separate dN/dS from alpha

## R-refresh 2026-10-12
Q187-Q190 ("only 20 percent are actually eliminated"; canonical evidence "incorrect"; coding sequences "evolving near-neutrally"; separate from MITTENS) repeat the DN4 inference on 0.7989. Q187 arithmetic holds (1 - 0.7989 = 20.1%; 77/20.1 = 3.8) under the standard simplification. Verdicts unchanged (internal non-sequitur, external contested). Credit: Day concedes purifying selection exists and scopes the result as separate from MITTENS (Q190). The Q188 wording ("therefore incorrect") rests on DN1/DN6 and is dialectic; its reading under "the dN/dS average" is defensible if 0.80 stands, as a statement about adaptive evolution it is the DN4 non-sequitur. reading-dependent, as already recorded in the verdict comments; no change.
