---
id: A2b
title: "Day revises his own counting rule: the ≥95% rule gives 8,679 fixations, the strict (lineage-aware) rule gives 5,496"
side: day
branch: A
parent: A2
edges: [{type: revises, target: A2}, {type: supersedes, target: A2}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds
  fidelity: unverifiable
  external: pending
---

## Statement (verbatim)
> By this strict definition the twelve populations contain 5,496 whole-population fixations across 723,000 population-generations.

Source: [LTEE fixation data paper, Zenodo 23105291](https://zenodo.org/records/23105291) (key Z23105291), 2026-10-02, p.1 (abstract).

> A naive rule that counts the first time a mutation's pooled frequency reaches 95% — the method of most quick analyses, including an earlier draft of our own — returns 8,679.

Source: [LTEE fixation data paper, Zenodo 23105291](https://zenodo.org/records/23105291) (key Z23105291), 2026-10-02, p.1.

## Formal statement
Whole-population fixations over 12 populations: strict 5,496 vs naive (≥95%) 8,679 (`ltee.whole_pop_fixations_lineage_aware.day_23105291`).

`derived:` 5,496/8,679 = 0.633 (the strict count is 36.7% lower; equivalently the naive count is 57.9% higher). The version ledger and `parameters.yaml` phrase this as "inflates counts 37%"; the precise statement is that the strict count is 37% *lower*. Non-mutator per-population strict counts 66, 73, 14, 9, 27 (sum 189, mean 37.8) give G_f = 60,000/37.8 = 1,587 versus the 3.0 value 1,322 (45.4 fixations): 17% fewer fixations, 20% slower rate. Ara+2: 3.0 §4.1 lists 64 (≥95% rule); Table 1 of Z23105291 lists 66 (strict), so the strict rule can raise a count as well as lower it.

## Assumptions
- Stated: lineage-aware fixation is the stricter definition; the 3.0 paper (published four days earlier) used the pooled ≥95% rule.
- Implicit: that Good 2017's lineage calls (SI, not retrieved) are the correct reference; that the 12-population totals map onto the 5-population non-mutator average without further adjustment.

## Responses
- Against: Good 2017 reports clade coexistence (main text), which is the reason a pooled 95% rule can over-count (ledger); no critic has engaged Z23105291.
- In support: Day's own revision is in the direction that strengthens MITTENS (G_f 1,322 → 1,587; shortfall x1.2).
- Weaknesses: the 1,322 headline has not been restated in the later paper (versions ledger). The two papers coexist as published Zenodo records, and the abstracts disagree about the number of fixations a defensible rule returns.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Good et al. 2017 | clade structure; "inconsistent with a "periodic selection" model" | main text verified; "≥95%" and lineage calls unverified (SI) |

## Pre-registered prediction
Not run. Prediction (claimant): strict recount reproduces 5,496. Prediction (alternative): any defensible rule moves the non-mutator G_f by less than a factor 2, so the debate is not about this.
- Result that would change a verdict: a recount of the Good 2017 raw trajectories.

## Check
Arithmetic audit (python3 -I, scratch). Raw trajectories not available in the repo. Review: pending.

## Simulator variables implied
- Counting-rule toggle: pooled ≥95% / lineage-aware / clone-pair.
