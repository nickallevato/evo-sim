---
id: B5d
title: "Relayed population geneticist: 6 My / 25 y × 30 mutations per generation = 7.2 million differences \"literally no selection required\""
side: critic
branch: B
parent: B5
edges: [{type: attacks, target: B1}, {type: attacks, target: B3a}]
load_bearing: false  # anonymous, relayed, informal; Day's reply is a disagreement about k = μ
sourcing: secondhand
status: extracted
verdicts:
  internal: n/a   # R4 X1 rule rev 2 (was holds): U: unidentified geneticist relayed by the host: not scored internal (also truncated, N5); 30 per generation uncited; excluded from the denominator
  fidelity: unverifiable   # R4 X1 rule rev 2 (was n/a): rule F (uncited/unretrievable input) or S/U; see R4-X1-rescore.md
  external: contested
---

## Statement (verbatim)
> Under neutrality, 6 million years divided by 25 generations um or 25 year generation times 30 mutations per generation is equal to 7.2 million differences. Literally no selection

Source: [Gutsick Gibbon + Will Duffy livestream, Human Evolution #2 (auto-captions)](https://www.youtube.com/live/6jXiwrcC5PQ), 2026-09-22, t=00:48:18 (auto-caption; read aloud by the host Gutsick Gibbon). **secondhand** (an unnamed population geneticist, as relayed by the host; the quote is truncated at "selection")

> The population geneticist on call confused mutations with fixations. 30 mutations cannot fixate per generation.

Source: [Day, "Zero Probability Zero Clue" (blog; relays a Gutsick Gibbon on-air message)](https://voxday.net/2026/09/22/zero-probability-zero-clue/), 2026-09-22, ¶17 of extracted text. Day's reply

## Formal statement
**Arithmetic audit (derived, python3 -I):** 6×10⁶/25 = 240,000 generations; × 30 = 7.2M ✓ (with 6.3 My: 252,000 × 30 = 7.56M, equal to IR's steady-state figure in B1a). Comparators: 7.2M vs SNV-only 17.5M per lineage (Z23003785) = 2.4× short; vs 205M = 28.5× short; vs Day's own IR figure 7.56M (the same quantity). Day's reply "7.2 million is significantly smaller than 410 million" is arithmetically correct (7.2/410 = 1.8%).
"30 mutations cannot fixate per generation" is a statement against the steady-state identity (k = μ means 30 neutral substitutions per generation at equilibrium); Day's own IR uses the same μL ≈ 30 as the steady-state count, so the disagreement is the fill state (B1c), not the arithmetic.

## Assumptions
- Stated: 30 neutral mutations per generation become 30 fixations per generation at steady state.
- Implicit: Per-lineage count; full pipe; the 30 figure is unreferenced (pedigree haploid 38.4, derived).

## Responses
- Against: Day: confused mutations with fixations (reply above); 7.2M < 410M.
- In support: RESULTS B0.5 / B1: the equilibrium-start count equals U·T.
- Weaknesses in the responses: Relayed by a non-expert host mid-stream; no citation; the quote is truncated; Day's own B1a uses the same arithmetic.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| none cited | n/a | n/a |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: 7.2M neutral differences without selection.
- Under the opposing model: (Day) pipeline not full; the real requirement is 17.5M (SNV) or 205M.
- Result that would change a verdict: B1c, B4a.

## Check
Script: none (arithmetic). Locator in Day's post: ¶9 of extracted text.

R4 X1 (research/checks/results/R4-X1-rescore.md; rule research/checks/results/R4-X1-verdict-rule.md rev 2; review #12, 2026-10-09): under the single both-sides rule this node is n/a / unverifiable. U: unidentified geneticist relayed by the host: not scored internal (also truncated, N5); 30 per generation uncited; excluded from the denominator Charitable reading tried: relayed and truncated: no reading recoverable.

## Simulator variables implied
- μL per lineage
- T
