---
id: ROOT-H
title: "Ola Hossjer: agrees with Day's conclusion after rescaling, but advocates 'uncommon descent' and limits the endorsement to the main argument"
side: ally
branch: ROOT
parent: ROOT
edges: [{type: supports, target: ROOT},{type: revises, target: A5}]
load_bearing: false  # Hossjer's agreement is conditional on the Haldane step (H), which he asserts without calculation
sourcing: firsthand
status: extracted
verdicts:
  internal: pending      # his rescaled gap is ~2x; the further step to ROOT relies on an uncomputed cost-of-selection argument (HO-03)
  fidelity: n/a      # the quotes are Hossjer's own words in a reviewed PDF/Substack post; fidelity applies to his reading of Day, covered in branch A5
  external: contested      # depends on H and A5 checks
---

## Statement (verbatim)
> "I agree with this conclusion, also after adjusting the MITTENS equation for the different mutation rates of humans and E. coli."

Source: Hossjer, [MITTENS - Convincing Arguments Against Neo-Darwinism](https://billdembski.substack.com/api/v1/file/f5a8533e-7b7c-407b-880b-1ecbd256784c.pdf) (PDF), 2026-09-14, p.3 (quotes-critics HO-06).

> "which still is less than 20 million, but only by a factor of 2."

Source: same, p.3 (HO-02): the rescaled upper bound (~10 million) is within 2x of the 20 million required.

> "I rather advocate uncommon descent between the two species."

Source: Dembski Substack, [A Review of Vox Day's Main Argument in PROBABILITY ZERO](https://billdembski.substack.com/p/a-review-of-vox-days-main-argument), 2026-09-14, para 75 (HO-10).

> "Note that his positive remarks apply to Vox Day’s main argument, not to the book as a whole."

Source: same, para 34 (HO-07); text by Dembski, not Hossjer.

## Formal statement
Hossjer's chain: `F_max(127) -> x(1.25e-8/1e-10) = 15,800 -> x(3e9/4.6e6) = ~1.0e7` vs 2.0e7 required; then the Haldane cost step (HO-03) is said to cut the adaptive share (asserted, not computed). Neutral version: `F = L*d*mu*t = 3e9*0.45*1.25e-8*450,000 = 7.6e6` (HO-04). Recomputed: 15,800*(3e9/4.6e6) = 1.03e7; 3e9*0.45*1.25e-8*4.5e5 = 7.59e6; without d: 1.69e7 (balance ledger).

## Assumptions
- Stated: he agrees with Day's conclusion about natural selection; both calcs assume parallel fixation between loci; common descent is not needed for his view (uncommon descent).
- Implicit: d = 0.45 applies inside both of his rates. The input contributes a factor 1/0.45 = 2.22; his gaps are 1.94× (eq. 2.4) and 2.63× (eq. 3.1), and without d they become 22.9M (above 20M) and 16.9M (1.19× short); corrected 2026-10-08 from "creates the 2.2x gap"; the cost step reduces adaptive fixations (HO-03).

## Responses
- Against: the Day-side numbers collapse from ~10^6 to ~2 after rescaling, per Hossjer himself (concedes most of A5; balance ledger).
- In support: Day's own response to Dembski's question (DE-01) says the scaling element 'doesn't apply at all' without equations (opponents/bill-dembski.md).
- Weaknesses: the agreement 'also after adjusting' and the 2x gap are in tension in the same review; the sentence 'I agree with this conclusion' refers to the pre-scaling bound. Endorsement does not extend to the book (HO-07).

## Primary literature
| Cited work | What it actually says | Fidelity |
|---|---|---|
| Haldane 1957 (via Nunney 2003) | ~1 substitution per 300 generations; Nunney 2003: cost 'substantially less', soft selection 'eliminates' it | verified via Nunney only (ledger) |

## Pre-registered prediction
Written before the arithmetic check. Under the claimant: Hossjer's rescaled bound reproduces to 2 sig figs. Under the opposing model: any inclusion of d in a neutral rate is non-standard (k = mu per generation) and removing it makes the neutral figure 1.7e7, i.e. 0.85 of required (no gap). Result that would change a verdict: a computed cost-of-selection bound (H) that cuts adaptive substitutions by >10x while the neutral share stays small.

## Check
Arithmetic: `python3 -I -c "print(15800*3e9/4.6e6, 3e9*0.45*1.25e-8*450000, 3e9*1.25e-8*450000)"` -> 1.03e7, 7.59e6, 1.69e7. Reconciles with HO-01/02/04 notes.

## Simulator variables implied
mu_human vs mu_E.coli, genome length scaling, d (turnover) placement, parallel-fixation switch, cost-of-selection (hard vs soft selection) switch.
