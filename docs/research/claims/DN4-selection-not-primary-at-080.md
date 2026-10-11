---
id: DN4
title: "Day: at dN/dS = 0.80 natural selection is not the primary mechanism of adaptive evolution"
side: day
branch: ROOT
parent: ROOT-FM
edges: [{type: supports, target: ROOT-FM}, {type: depends-on, target: DN1}]
load_bearing: false
sourcing: firsthand
status: extracted
verdicts:
  internal: pending   # rule-N candidate: dN/dS averages purifying constraint over all nonsynonymous changes; it does not measure the adaptive fraction alpha (A2e-alpha) or the rate of beneficial fixations. Not scored until checked against Day's own material (rule N needs the author's own premises)
  fidelity: n/a
  external: pending   # premise DN1 not reproduced on hg38 (R4 L1, awaiting review)
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
None run. Rule N grep of Day's corpus pending.

## Simulator variables implied
- per-site selection classes (neutral, purifying, adaptive) needed to separate dN/dS from alpha
