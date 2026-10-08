---
id: H7
title: "Keightley 2012: a genome-wide deleterious mutation rate of U = 2.2 is higher than humans could tolerate under hard selection but tolerable under selection on relative fitness"
side: literature
branch: H
parent: H
edges: [{type: attacks, target: H}, {type: attacks, target: H5}]
load_bearing: false  # Bears on the hard-selection premise of the cost argument and on the genetic-entropy statement in Hössjer's PDF (HO-11); it is a literature constraint on the regime, not a direct test of Haldane's number.
sourcing: firsthand
status: reviewed
verdicts:
  internal: n/a
  fidelity: n/a
  external: "supported"   # hard selection at U = 2.2 needs ~18 offspring per female; does not decide hard vs soft
---

## Statement (verbatim)
> "A genome-wide deleterious mutation rate of 2.2 seems higher than humans could tolerate if natural selection is “hard,” but could be tolerated if selection acts on relative fitness differences between individuals or if there is synergistic epistasis."

Source: Keightley PD. 2012, [Rates and fitness consequences of new mutations in humans](https://pmc.ncbi.nlm.nih.gov/articles/PMC3276617/), Genetics 190(2):295-304, Abstract; checked against the user-downloaded full text `sources/raw/sources/manual/Keightley2012.txt`.

> "I argue that in the foreseeable future, an accumulation of new deleterious mutations is unlikely to lead to a detectable decline in fitness of human populations."

Source: same, Abstract.

> "Direct estimates from genome sequencing of relatives suggest that μ is about 1.1 × 10(-8), which is about twofold lower than estimates based on the human-chimp divergence. This implies that an average of ~70 new mutations arise in the human diploid genome per generation."

Source: same, Abstract (Europe PMC copy; quote in `sources/quotes-literature.md`).

## Formal statement
Kondrashov-Crow method: U = (mutational target sites) x mu x (mean selective constraint per site); abstract: "estimates are U ≈ 2.2 for the whole diploid genome per generation and 0.35 for mutations that change an amino acid of a protein-coding gene" (the extracted text drops the "≈"). Under hard selection ("one deleterious mutation, one genetic death"), mean fitness relative to a mutation-free genotype W̄ = e^(-U).
derived (R2): e^-2.2 = 0.1108 (paper 0.11; holds); e^-0.35 = 0.7047 (paper 0.7; holds); with 20 offspring per female, 20 x (1 - 0.1108) = 17.8 selective deaths (paper "18"; holds).
Link: `mutation.mu_per_site_per_gen.keightley_2012` = 1.1e-8 and `mutation.new_mutations_per_genome.common_citation`: 70 per diploid genome (abstract; the full text uses the same value in the U calculation; the text extraction renders the exponent as "1028", so the numeric check rests on the abstract). Link to H: this is a statement about the *deleterious* side of Haldane's cost: the same argument ("one genetic death per substitution") applied to deleterious mutations yields an implausible load under hard selection, from which the paper concludes that much human selection acts on relative fitness. The paper does not address beneficial substitutions or Haldane's 1957 limit.

## Assumptions
- Stated: the Kondrashov-Crow method is "somewhat problematic" because of weakly selected noncoding sites; selection hard or soft ("pure hard and soft selection is unlikely").
- Implicit (for use against H): that a regime of relative-fitness selection for deleterious variation also applies to beneficial substitutions; Nunney (H2) argues that directional environmental change is likely to give hard selection for adaptation.

## Responses
- Against: Day's s_max ≈ 1 ceiling (H8) is not engaged with Keightley.
- In support: Nunney's treatment of soft selection (H2) is the same distinction.
- Weaknesses in the responses: neither side has quantified the hard-soft mixture for beneficial substitutions.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kondrashov & Crow 1993; Wallace 1970, 1975 (hard vs soft) | cited by Keightley | not retrieved |
| Muller 1950; Crow 1970 (genetic load and the cost of natural selection) | cited by Keightley | not retrieved |

## Pre-registered prediction
- Under the literature: for U = 2.2 the hard-selection mean fitness is 0.11, which is implausible; real populations tolerate U by relative-fitness selection.
- Under Day's H (hard selection at s_max near 1 or 10% mortality): the same hard accounting for beneficial substitutions yields the 300-generation limit.
- Result that would change a verdict: a joint model (the H simulation) where both deleterious load U = 2.2 and beneficial substitutions share one reproductive budget; if feasible rates of beneficial substitution remain above Haldane's under that joint load, H fails for humans.

## Check
R4 H7 (`h_keightley_load.py`, K = 1000, 6 reps; research/checks/results/R4-H-C2.md) and H2 (research/checks/results/R4-H2-hard.md): hard multiplicative selection at U = 2.2, s = 0.05 goes extinct for Fmax = 4-20 and persists at 30 (N/K 0.174 vs predicted 0.188; ratchet regime) and 60 (0.344 vs 0.353); threshold 2e^U = 18.1 offspring per female. Soft selection persists at every Fmax. In H2 the combined condition is lam*D + U < ln R. This supports Keightley's statement but does not decide whether human selection is hard or soft (Day-side use: a hard-selection population at U = 2.2 is near its limit). Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)
Earlier note: Script: `research/checks/h_cost_of_selection.py` (planned; extend with a deleterious load term U). · Result: not run · Review: pending

## Simulator variables implied
Deleterious mutation rate U, beneficial substitution rate, hard/soft mixing fraction, synergistic epistasis, offspring number.
