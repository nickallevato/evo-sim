---
id: B3h
title: "Ne ≈ 10,000 is derived from theta = 4 Ne mu, which \"presupposes k = mu\""
side: day
branch: B
parent: B3
edges: [{type: attacks, target: B7c}]
load_bearing: false  # blocks critics' use of Nₑ ≈ 10⁴ (keruru's 10⁻²⁹, Mansfield's inputs); not a step in MITTENS counts
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: n/a
  external: contested
---

## Statement (verbatim)
> The arithmetic holds given one number: Nₑ ≈ 10,000 — which comes from θ = 4Nₑμ, which presupposes k = μ, the identity under test.

Source: [Day, "The Response to the Retraction" (blog)](https://voxday.net/2026/08/27/the-response-to-the-retraction/), 2026-08-27, ¶3 of extracted text

> The standard N₂ ≈ 10,000 is itself problematic, as it is derived from genetic diversity via θ = 4N₂μ — a formula that presupposes k = μ.

Source: [Z18525547, The N/N_e Distinction and the Recalibration of the Human-Chimpanzee Divergence (Day & Athos)](https://zenodo.org/records/18525547), Zenodo 2026-02-08 (v1)

## Formal statement
Nₑ(coalescent) = π/(4μ) from observed diversity π and a per-generation μ. Whether this "presupposes k = μ" depends on how μ was obtained: a pedigree μ (Kong 2012, Keightley 2012) is measured directly; a phylogenetic μ (divergence ÷ dated split) does use k = μ. IR §5 itself says μ "was initially estimated phylogenetically" and was later replaced by the pedigree estimate.
**Internal tension:** Z22129121 states "The equilibrium heterozygosity relation θ = 4Nₑμ is untouched." (same author, 2026-08-27).

## Assumptions
- Stated: The Nₑ ≈ 10⁴ input to keruru's calculation is circular.
- Implicit: μ in θ = 4Nₑμ is a clock-calibrated rate.

## Responses
- Against: Pedigree μ is independent of divergence dating (Keightley 2012).
- In support: Day: Charlesworth (2009) flagged the circularity (not retrieved).
- Weaknesses in the responses: Day cites Charlesworth 2009 without a quote in the corpus; keruru "had no answer" per Day via keruru (secondhand, B7c).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Keightley 2012 | μ ≈ 1.1×10⁻⁸ from sequencing relatives | verified-partial (abstract) |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: Nₑ from diversity inherits any clock error in μ.
- Under the opposing model: With pedigree μ, Nₑ (diversity) contains no divergence data.
- Result that would change a verdict: Showing that a given Nₑ estimate used a phylogenetic μ.

## Check
Script: none.

## Simulator variables implied
- μ source (pedigree | phylogenetic)
- Nₑ source (diversity | drift variance | PSMC)
