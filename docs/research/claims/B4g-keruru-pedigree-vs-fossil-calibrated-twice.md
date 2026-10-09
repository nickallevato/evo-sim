---
id: B4g
title: "keruru: fossil-calibrated rate is about twice the pedigree rate (unreconciled)"
side: critic  # keruru rule (opponents/keruru.md): statement is in the 2026-08-26 retraction post. Was 'ally' until 2026-10-08.
branch: B
parent: B4
edges: [{type: supports, target: B4d}]
load_bearing: false  # auxiliary; magnitude (×2) is far from Day's ×15–150 and ×32.3
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: unverifiable
  external: contested
---

## Statement (verbatim)
> Calibrating against the fossil-dated human–chimpanzee split gives something closer to twice that.

Source: [keruru, "The Epicycle Was Elsewhere"](https://claudekeruru.substack.com/p/the-epicycle-was-elsewhere), 2026-08-26, para 21 (context: pedigree rate ~1.2e-8; author calls this unreconciled)

## Formal statement
Pedigree μ ≈ 1.2e-8 (Kong 2012) vs a fossil-calibrated phylogenetic rate ≈ 2× (keruru; Keightley 2012 reports the same twofold). With 6.3 My and 25 y/generation, the observed 1.23% difference gives a rate of 1.23%/(2 × 252,000) = 2.4e-8 per generation (derived, includes polymorphism and ancestral coalescence), i.e. 2× the pedigree rate. Subtracting the ancestral term θ_anc = 6.3e-3 (Nₑ = 1.32e5, B4a) leaves 5.97e-3/(2 × 252,000) = 1.2e-8, equal to pedigree μ (derived, one-point illustration).

## Assumptions
- Stated: The ×2 discrepancy is unreconciled.
- Implicit: All divergence is accumulated after the split; ancestral coalescence ignored.

## Responses
- Against: Ancestral coalescence (B4a) can account for the ×2 if Nₑ,anc ≈ 1.3×10⁵.
- In support: Keightley 2012.
- Weaknesses in the responses: The derived one-point reconciliation depends on Nₑ,anc and on μ, T, g; it is a proposal for B4a, not a result.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Keightley 2012 | see B4d | verified-partial |

## Pre-registered prediction
Written **before** the check runs.
- Under the claimant's model: There is an unreconciled ×2.
- Under the opposing model: Ancestral polymorphism and generation-time conventions account for it.
- Result that would change a verdict: B4a.

## Check
Script: proposed B4a.

## Simulator variables implied
- θ_anc term
- generation time
