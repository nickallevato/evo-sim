---
id: B5h
title: "Hossjer (ally): neutral fixation rate is d × mu per site; 3e9 × 0.45 × 1.25e-8 × 450,000 = 7.6 million"
side: ally
branch: B
parent: B5
edges: [{type: supports, target: B5}, {type: attacks, target: B3a}]
load_bearing: false  # the ally-side acceptance of 2Nμ × 1/(2N) = μ; leaves a ≈2.6× gap to 20M with d = 0.45
sourcing: firsthand
status: extracted
verdicts:
  internal: holds
  fidelity: accurate
  external: contested
---

## Statement (verbatim)
> equation (5) is based on the neutral theory of evolution.

Source: [Hossjer, "MITTENS - Convincing Arguments Against Neo-Darwinism" (PDF attached to Dembski post)](https://billdembski.substack.com/api/v1/file/f5a8533e-7b7c-407b-880b-1ecbd256784c.pdf), 2026-09-14, PDF p5 (§3; his neutral count is PDF "(5)", numbered 3.1 in the text)

> which still is less than 20 million, but only by a factor of 2.

Source: [Hossjer, "MITTENS - Convincing Arguments Against Neo-Darwinism" (PDF attached to Dembski post)](https://billdembski.substack.com/api/v1/file/f5a8533e-7b7c-407b-880b-1ecbd256784c.pdf), 2026-09-14, PDF p3 (Eq. 2.4, the genome-length scaling of MITTENS)

## Formal statement
Hössjer (Eq. 3.1): F_hum = L·d·μ·t_div = 3×10⁹ × 0.45 × 1.25×10⁻⁸ × 450,000 = 7.6M (derived ✓ 7.59M); without d: 16.9M vs 20M (balance ledger). He writes 2Ndμ × 1/(2N) = dμ (overlapping generations with turnover d), so the N-independent neutral rate, not N/Nₑ. E. coli neutral check: 1/(4.6e6 × 1e-10) = 2,170 vs Day's 1,600 (derived ✓).

## Assumptions
- Stated: Neutral rate dμ per nucleotide; fixation independent between nucleotides.
- Implicit: Nucleotides independent (no linkage); d = 0.45 reduces the neutral supply (A4), which Day applies to selection and Hössjer carries into the neutral calculation.

## Responses
- Against: Day (B4d) notes his support for the dating circularity; Day does not rely on this calculation.
- In support: B5, B5a, B5f.
- Weaknesses in the responses: d inside a neutral rate is not a standard neutral result (turnover coefficient A4 unverified); his "factor of 2" gap arises from d; he asserts but does not compute the cost-of-selection step (branch H).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| none cited | n/a | n/a |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: 7.6M neutral fixations on one lineage (with d).
- Under the opposing model: (Day) steady state not reached.
- Result that would change a verdict: A4.

## Check
Script: none (arithmetic).

## Simulator variables implied
- d (turnover) in the neutral supply
- L
- μ
