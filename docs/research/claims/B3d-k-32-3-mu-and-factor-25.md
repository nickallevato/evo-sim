---
id: B3d
title: "k = 32.3 mu (Bergeron pedigree rate vs Yoo required rate) and the median factor 25 across 55 vertebrates"
side: day
branch: B
parent: B3
edges: [{type: supports, target: B3}]
load_bearing: false  # cited as direct empirical falsification of k = μ after the N/Nₑ retraction, but no derivation is shown
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: unverifiable
  external: contested
---

## Statement (verbatim)
> comparing Bergeron’s (2023) pedigree-measured mammalian mutation rate against the required substitution rate from Yoo et al. (2025) gives k = 32.3μ, not k = μ.

Source: [Day, "The Education of a Population Geneticist" (blog)](https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/), 2026-10-01, ¶7 of extracted text

> The textbook k = μ identity is still falsified — both directly (pedigree μ and phylogenetic k disagree by a median factor of 25 across 55 vertebrates)

Source: [Day, "A Retraction and a Revision" (blog)](https://voxday.net/2026/05/07/a-retraction-and-a-revision/), 2026-05-07, ¶5 of extracted text

## Formal statement
No derivation appears in any harvested text (not in Zenodo; book not checked). Parameters: Bergeron 2023 mammal mean 7.97e-9 (`mutation.mu_per_site_per_gen`, main text; human value in SI Table 8, not retrieved); required rate from Yoo 2025 (not found in Yoo: 410 Mb or 187 Mb, fidelity ledger).

**Reconstruction attempts (derived, python3 -I):** brute force over required ∈ {17.5M, 20M, 35M, 40M, 187M, 205M, 410M}, generations ∈ {146,250 … 450,000}, L ∈ {2.9–6.4 Gb}, μ ∈ {7.97e-9 … 1.5e-8}, with and without halving: only four coincidental hits within ±0.15 of 32.3, all using non-natural input pairs (e.g. 410M, 325,000 gens, L = 3.0e9, μ = 1.3e-8). The closest natural reconstruction: 205M / 252,000 = 813.5 required fixations per generation; Bergeron mammal μ × 3.1e9 = 24.7 mutations per generation; ratio 32.9 (with L = 3.2e9: 31.9). **Implication:** the ratio uses the 205M count (bp/events issue, A3x); with the SNV-only 17.5M the same arithmetic gives 69.4/24.7 = 2.8; 205M/17.5M = 11.7 (the "11.7" bases-vs-events factor in the balance ledger).
The "median factor of 25 across 55 vertebrates" cites no source in the post; Bergeron 2023 reports "40-fold variation among species" in pedigree rates (a different quantity). Pedigree μ is per generation and phylogenetic k per year/per generation depends on generation-time assumptions.

## Assumptions
- Stated: Pedigree μ and phylogenetic (required) rate should coincide under k = μ.
- Implicit: The "required substitution rate" is the observed difference count divided by T and L (it counts differences including polymorphism, structural variants and ancestral coalescence), compared with a per-site-per-generation pedigree μ.

## Responses
- Against: Hancock and Nesslig20 compute the neutral count from pedigree μ and find agreement within a factor ~2 (B5c, B5e); Hancock's count reaches ≈19M vs 35M SNVs (B5c).
- In support: Keightley 2012: pedigree μ is "about twofold lower than estimates based on the human-chimp divergence"; keruru (KR-05): "closer to twice that".
- Weaknesses in the responses: Hancock's comparison uses SNVs only and mixed haploid/diploid bases (B5c); neither side has isolated the effect of ancestral coalescence and calibration choice on the "twofold".

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Bergeron 2023 | "The average pedigree-based mutation rates per generation for each species ... show 40-fold variation among species." | verified-accurate (ledger) for the 40-fold figure only |
| Yoo 2025 | no 410 Mb or 187 Mb; SDR average 327 Mb per lineage | not-found (ledger) |
| Keightley 2012 | "μ is about 1.1 × 10(-8), which is about twofold lower than estimates based on the human-chimp divergence" | verified-partial (abstract only) |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: k = 32.3μ.
- Under the opposing model: Using SNV-only fixed differences and ancestral-coalescence accounting, k/μ is of order 1–3, not 30.
- Result that would change a verdict: Day supplying the derivation; or a reproduction using stated inputs. B4a will separate the ancestral-coalescence term.

## Check
Script: none; reconstruction search computed with python3 -I in this session (not committed).

## Simulator variables implied
- required-rate basis (SNV | events | bp)
- μ source (pedigree | phylogenetic)
- L haploid
