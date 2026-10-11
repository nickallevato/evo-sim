---
id: E10
title: "Day: ten of the twelve LTEE populations show intervals where fixations are being undone faster than new ones complete"
side: day
branch: E
parent: A2
edges: [{type: supports, target: A2}, {type: depends-on, target: E9}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds   # R4 L6 fix pass (reviewed a183774): Day's sign-only rule (>=95% snapshot count falls between 10K marks) reproduces 10 of 12 exactly, 28 of 29 tabulated cells; threshold-sensitive: 7 of 12 at a net fall of >= 5, 6 of 12 at >= 10
  fidelity: partial   # R4 L6 fix pass: 'fixations' names a >=95% snapshot statistic; Good 2017's well-mixed fixed calls never fall because the fixed state is never left in the published output (0 exits in 34,118 paths), i.e. by definition
  external: contested   # R4 L6 fix pass: near-fixed mutations do reverse (34% dip and return, 62% hover 0.5-0.95, 4.6% lost by clade displacement); Good's well-mixed calls cannot fall by construction; clade-level states (FM/Fm) not read
---

## Statement (verbatim)
> In fact, ten of the twelve populations even show intervals where fixations are being undone faster than any new ones complete.

Source: [Day, "How Biologists Keep 'Proving' Selection"](https://voxday.net/2026/10/11/how-biologists-keep-proving-selection/), 2026-10-11, ¶4 (Q178). RH tag: dialectic. The paragraph's "set the narrative" framing of Barrick 2009 is rhetoric (RH-24).

Antecedent: Day, MITTENS 3.0 (Zenodo 23003785, 2026-09-28), s5.3: "Ten of twelve populations — mutator and non-mutator alike — show at least one 10,000-generation interval where fixations are being undone faster than new ones complete." (raw `sources/raw/day/zenodo-23003785.txt` l.379-381).

## Formal statement
For population p and marks t = 10K..60K, F_p(t) = number of mutations at >= 95% frequency (Z23003785 s4.1). Claim: #{p : exists t with F_p(t+10K) < F_p(t)} = 10 of 12.

## Assumptions
- Stated (s4.1): ">=95% population frequency" counts as fixed.
- Implicit: a fall in F means fixed mutations were lost.

## Responses
- Against (critic, A2c): the snapshot estimator is not a count of fixations (Ara+5 38 -> 0; Ara-2 -906).
- Against (audit, R4 L6, fix pass): Good's HMM fixed counts never fall, but by construction (the fixed state is never left), so this is a definitional point, not a measured absence of reversals.
- In support (Day): the snapshot falls are real data features; clonal interference displaces near-fixed sweeps (Good 2017's coexistence).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Good et al. 2017 | "long-term quasi-stable coexistence arises spontaneously in most populations" (abstract; test-methods review entry 1) | partial (see fidelity comment) |

## Pre-registered prediction
`research/checks/l6_ltee_undone.py` (0b478dd).

## Check
R4 L6 (`research/checks/results/R4-L6.md`; combined review a183774; fix pass with post hoc `l6_posthoc_absorbing.py`, 10cfe1e). **Integrated 2026-10-11 (review #59):** internal holds, fidelity partial, external contested; open: Good 2017 SI 5.2 and the clade-level HMM states.

## Simulator variables implied
- fixation definition selector (snapshot threshold vs absorbing fixation)
