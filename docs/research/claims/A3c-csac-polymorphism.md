---
id: A3c
title: "The 35M SNV and 5M indel counts are human–chimp genome differences that include polymorphism"
side: literature
branch: A
parent: A3
edges: [{type: revises, target: A3}]
load_bearing: false
sourcing: firsthand
status: extracted
verdicts:
  internal: n/a
  fidelity: partial
  external: supported
---

## Statement (verbatim)
> The differences between one copy of the human genome and one copy of the chimpanzee genome include both the sites of fixed divergence between the species and some polymorphic sites within each species.

Source: Chimpanzee Sequencing and Analysis Consortium 2005 (key CSAC2005), main text, "Nucleotide divergence".

> we estimate that polymorphism accounts for 14-22% of the observed divergence rate

Source: same, "Genome-wide rates".

> Single-nucleotide substitutions occur at a mean rate of 1.23% between copies of the human and chimpanzee genome, with 1.06% or less corresponding to fixed divergence between the species.

Source: same, Introduction findings.

## Formal statement
`divergence.snv_divergence_fraction.csac_2005_total` = 0.0123; `.csac_2005_fixed_max` = 0.0106; proposed key `divergence.fixed_fraction_of_observed` = 0.78–0.86.
`derived:` 0.0106/0.0123 = 0.862; 35e6 x 0.78–0.86 = 27.3e6–30.2e6 fixed SNV differences; per lineage 13.7e6–15.1e6.

## Assumptions
- Stated: one copy per species.
- Implicit (in uses by both sides): reference-genome differences equal fixed differences; Nesslig20 (PS-03) states this point in the form "not all of the differences they identified between genomes are actually fixed in either the human or chimp populations".

## Responses
- Against: none in the Day corpus addresses polymorphism in the 35M count (the 2025 and 3.0 papers use 35M as required fixations).
- In support: Nesslig20 (PS-03, critic) and Camestros (CA-04: "treating ALL the genetic differences … as mutations that initially only occurred after the point of divergence") both press ancestral polymorphism.
- Weaknesses: the effect is 14–22%, not an order of magnitude. Yoo 2025 SNV divergence is internally inconsistent (0.15–0.16% in SI text vs 1.46% in Table III.14, unresolved).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| CSAC2005 | above | verified-partial (as used by Day and by critics) |
| Yoo2025 | SNV divergence 0.15–0.16% (text) vs 1.46% (Table III.14) | discrepancy, unresolved |

## Pre-registered prediction
Prediction: removing polymorphism lowers the SNV requirement by 14–22% (derived above); it does not change the verdict on the shortfall unless A5 closes the remaining gap, where it would matter (KITTENS: 17.9M vs 17.5M).

## Check
No script. Review: pending.

## Simulator variables implied
- `fixed_fraction_of_observed` toggle on the requirement.
