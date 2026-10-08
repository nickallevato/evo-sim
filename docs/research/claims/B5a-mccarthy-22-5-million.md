---
id: B5a
title: "McCarthy: 100 mutations/newborn × N = 10,000 over 9 My gives 450 billion mutations; × 1/20,000 = 22.5 million fixed"
side: critic
branch: B
parent: B5
edges: [{type: attacks, target: B1}, {type: attacks, target: B3a}]
load_bearing: false  # illustrative expectation using Day's own inputs; load rests on N = Nₑ and all-neutral
sourcing: firsthand
status: extracted
verdicts:
  internal: holds
  fidelity: n/a
  external: contested
---

## Statement (verbatim)
> 50,000 x 9 million = 450 billion new mutations altogether.

Source: [McCarthy, "Why Probability Zero is Wrong About Evolution" (free repost)](https://dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1), 2026-09-11 (original paid post 2026-01-26), para 50

> 450 billion x 1/20,000 = 22.5 million fixed mutations.

Source: [McCarthy, "Why Probability Zero is Wrong About Evolution" (free repost)](https://dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1), 2026-09-11 (original paid post 2026-01-26), para 52

> 400 billion x 1/20,000 =20 million fixations. So when we apply the time available to the numbers we land on the exact correct result.

Source: [McCarthy, "Vox Day Responds"](https://dennismccarthy.substack.com/p/vox-day-responds), 2026-09-17, para 21 (time-adjusted version: subtracts the last 50,000 generations)

## Formal statement
**Arithmetic audit (derived, python3 -I):** 100 × 10,000 / 20 y = 50,000 new mutations per year ✓; × 9×10⁶ y = 4.5×10¹¹ ✓; × 1/(2 × 10,000) = 22.5×10⁶ ✓. Per generation: 100 × 10⁴ = 10⁶; × 450,000 generations = 4.5×10¹¹ ✓; per lineage 50 fixed per generation × 450,000 = 22.5M ✓. Time-adjusted: (450,000 − 50,000) × 50 = 20.0M ✓ (as quoted by Day, 2026-02-04); using Day's own correction E[F] ∝ T − 4Nₑ with 4Nₑ = 40,000: (450,000 − 40,000) × 50 = 20.5M (derived).
Sensitivity (derived): with a neutral fraction f, count = f × 22.5M; f = 0.89 is needed for 20M. With 70 SNV-type mutations per newborn (Keightley 2012 "~70") the ceiling at f = 1 is 35 × 450,000 = 15.75M < 20M.
Comparator: McCarthy's "20 million observed" is the per-lineage half of Day's 2019 40M total; SNV-only 17.5M per lineage (Z23003785).

## Assumptions
- Stated: Day's own inputs (100 mutations/person, Nₑ = N = 10,000, 9 My, 20 y).
- Implicit: N = Nₑ; all mutations neutral ("only 3% of new mutations are deleterious", uncited); 100 per newborn counts all de novo events (SNV and others); the start state is full.

## Responses
- Against: Day (R2 2026-02-04): same model with the correct Nₑ and N gives 8.25 (B3e; sign problem, now withdrawn B3g); Day (IR): subtract 4Nₑ (B1a, a 9% effect at these inputs).
- In support: RESULTS B0.5; Hössjer's Eq. 3.1 gives 7.6M with his own d and L (B5h).
- Weaknesses in the responses: Expected value only (derived: Poisson sd ≈ 4.7 thousand, immaterial). Uncited 3% figure; 60–100 range, not a point value; N = Nₑ.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Keightley 2012 | "an average of ~70 new mutations arise in the human diploid genome per generation" | verified-partial (abstract only) |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: (McCarthy) ≈ 20–22.5M fixed on one lineage under neutral drift.
- Under the opposing model: (Day) 8.25 (B3e) or an empty-pipe deficit (B1a: 20.5M with McCarthy's inputs, a 9% reduction).
- Result that would change a verdict: B1c if the start state is empty/expanded; a sourced neutral fraction.

## Check
Script: none (arithmetic). See B5 for the identity check.

## Simulator variables implied
- new mutations per newborn
- neutral fraction
- N, Nₑ
- window T
