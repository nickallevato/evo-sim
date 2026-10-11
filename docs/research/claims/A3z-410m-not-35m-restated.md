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
  internal: holds     # on his own numbers 35/410 = 8.5% ('less than a tenth' holds); 'nearly 10x' understates 14.9/1.23 = 12.1 (slip, ledger, R1 not triggered)
  fidelity: pending   # R4 L7 (awaiting review): 410 M reconstructs from sheet 14 (mean SNV + gap divergence 13.94%) x hs1 length (sheet 19) = 404-413 M bp; route unconfirmed (base rate 0.83); 14.9% not reproduced. Proposed partial
  external: pending   # the bp-vs-events point (A3x) applies: 410 M bp vs 48.3 M T2T events (8.5x); proposed contested as for A3a
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
R4 L7 (`research/checks/results/R4-L7.md`, awaiting review).

## Simulator variables implied
- `required_fixations` unit selector (bp / events), as A3x
