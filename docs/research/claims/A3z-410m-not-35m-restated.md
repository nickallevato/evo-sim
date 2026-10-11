---
id: A3z
title: "Day 2026-10-11: Yoo 2025 implies 410 million total genomic differences, not 35 million; the SI's divergence numbers sit on sheets 14, 19 and 24 and are not additive"
side: day
branch: A
parent: A3a
edges: [{type: supports, target: A3a}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds   # on his own numbers 35/410 = 8.5% ('less than a tenth' holds); 'nearly 10x' understates 14.9/1.23 = 12.1 (slip, ledger, R1 not triggered); R4 L7 fix pass: the Zenodo s7.1 component list (35 M + 1,140 + 187 Mb = 222 M) is A3a's statement, scored there (rule C, ledger); this post calls the pieces non-additive, so that sum is not its derivation (rule S)
  fidelity: partial   # R4 L7 fix pass (reviewed a183774): locator and 'no consolidated total' accurate; (mean SNV + mean gap divergence, sheet 14) x hs1 length (sheet 19) = 404-413 M bp, route unconfirmed (one clean route, computed before pre-registration; medians give 82 M; matches within 2% of 410 M are common, primitive-pool ratio 1.3-1.7); his printed components sum to 222 M; 14.9% reproduced only approximately (15.05%, at 436.5 M)
  external: contested   # R4 L7 fix pass (as for A3a): 410 M is a base-pair measure; T2T events (GAP-07t, 48.3 M, both lineages) are 8.5x lower in a different unit
---

## Statement (verbatim)
> the real number turned out to involve an estimated 410 million total genomic differences, not 35 million

> The divergence numbers don't appear in the paper, but are buried on pages 14, 19, and 24 and have to be located and identified before one realizes that they aren't additive and no total is either calculated or provided.

Source: [Day, "How Biologists Keep 'Proving' Selection"](https://voxday.net/2026/10/11/how-biologists-keep-proving-selection/), 2026-10-11, ¶2 and ¶19 (Q179). RH tag: dialectic for the number; the Kevin Hart / LeBron James analogy (¶3) and "quietly excluded" are rhetoric (RH-24).

## Formal statement
D_total = 410e6 (bp) against CSAC's 35e6 SNVs; 35/410 = 0.085.

## Assumptions
- Implicit: "differences" in base pairs and SNV counts are commensurable.

## Responses
- Against (critic, A3x): base pairs in structural variants are not events.
- In support (Day): the SI reports SNV and gap divergence separately with no consolidated total (verified, R4 L7).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Yoo 2025 SI Table III.14 | mean SNV divergence 0.01463, mean gap divergence 0.12473 (human-chimp, autosomes) | R4 L7 |

## Pre-registered prediction
`research/checks/l7_410m_accounting.py`.

## Check
R4 L7 (`research/checks/results/R4-L7.md`; combined review a183774; fix pass with post hoc `l7_posthoc_baserate.py`, 42df167). **Integrated 2026-10-11 (review #60):** internal holds, fidelity partial, external contested.

## Simulator variables implied
- `required_fixations` unit selector (bp / events), as A3x
