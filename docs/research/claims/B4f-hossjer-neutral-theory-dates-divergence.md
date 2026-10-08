---
id: B4f
title: "Hossjer (ally): neutral theory cannot explain common ancestry because it is used to date the divergence"
side: ally
branch: B
parent: B4
edges: [{type: supports, target: B4d}]
load_bearing: false  # cited by Day (IR §5) as an independent confirmation; no calculation
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: unverifiable
  external: contested
---

## Statement (verbatim)
> the neutral theory of evolution cannot explain common ancestry between humans and chimps at all based on genome-wide nucleotide differences between the two species, since the neutral theory is used in the first place to date the assumed time of divergence.

Source: [Hossjer, "MITTENS - Convincing Arguments Against Neo-Darwinism" (PDF attached to Dembski post)](https://billdembski.substack.com/api/v1/file/f5a8533e-7b7c-407b-880b-1ecbd256784c.pdf), 2026-09-14, PDF p5, §3

> I agree with this conclusion, also after adjusting the MITTENS equation for the different mutation rates of humans and E. coli.

Source: [Hossjer, "MITTENS - Convincing Arguments Against Neo-Darwinism" (PDF attached to Dembski post)](https://billdembski.substack.com/api/v1/file/f5a8533e-7b7c-407b-880b-1ecbd256784c.pdf), 2026-09-14, PDF p3 (scope: the MITTENS selection argument, not the neutral calculation)

## Formal statement
Hössjer's neutral calculation (his Eq. 3.1): F_hum = L·d·μ·t_div = 3e9 × 0.45 × 1.25e-8 × 450,000 = 7.6M (derived: 3e9 × 1.25e-8 = 37.5; × 0.45 = 16.9; × 450,000 = 7.59e6 ✓) per lineage, "very close to the second extended MITTENS equation". His E. coli check: 1/(L·μ) = 1/(4.6e6 × 1e-10) = 2,170 generations vs Day's 1,600 (derived ✓). He uses 2Nμd × 1/(2N) = dμ (census N), i.e. he does not adopt B3a.

## Assumptions
- Stated: The rate is dμ for neutral sites; the date depends on the neutral rate.
- Implicit: Date = D/(2μ); μ has been adjusted (phylogenetic → pedigree).

## Responses
- Against: Day's own IR gives Hössjer as a corroborating reviewer of B4d; Hössjer notes that the dating point "is not addressed in Vox Day's book".
- In support: Day (IR §5).
- Weaknesses in the responses: Hössjer's 7.6M includes the d = 0.45 factor in the neutral supply; without it 16.9M vs 20M (balance ledger). His d use is Day's turnover coefficient (branch A4), not a neutral-theory result.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Keightley 2012 | pedigree μ ≈ 1.1e-8 | verified-partial |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: Neutral theory cannot support common descent by itself.
- Under the opposing model: The dating circularity concerns the age, not whether the count of differences is neutral-compatible.
- Result that would change a verdict: n/a

## Check
Script: none (arithmetic only).

## Simulator variables implied
- μ
- d (A4)
