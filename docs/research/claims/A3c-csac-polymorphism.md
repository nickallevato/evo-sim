---
id: A3c
title: "The 35M SNV and 5M indel counts are human–chimp genome differences that include polymorphism"
side: literature
branch: A
parent: A3
edges: [{type: revises, target: A3}]
load_bearing: false
sourcing: firsthand
status: reviewed
verdicts:
  internal: n/a
  fidelity: partial
  external: supported   # R4 GAP-07c: human half measured, 15.6% of human-derived divergent SNVs still polymorphic (consistent with CSAC's 14-22%); chimp side not measured; sorted ancestral variation not measured
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
- Against (Day, on ancestral polymorphism): "Under coalescent theory, the expected pairwise divergence contributed by ancestral polymorphism is θ = 4Nₑμ per site." (Z22903977 p.3, Q37); "Their inflated ILS figure does not rescue anything. It simply distributes the fixation requirement across both lineages instead of consolidating it on one." ([Less Than Zero 3](https://voxday.net/2026/04/28/less-than-zero-3/), 2026-04-28, ¶24 of extracted text). His position is that sorted ancestral variants still need to fix. (This line replaced "none in the Day corpus addresses polymorphism" on 2026-10-09, after the GAP-07c Day-side steelman review.) The 2025 and 3.0 papers still use 35M as required fixations.
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

R4 GAP-07b (research/checks/results/R4-GAP07b-alignment.md): with CSAC's fixed share (0.78-0.86) applied to SNVs only, measured fixed events per lineage are 16.9-18.4M; applied to all events, 16.4-18.1M (post hoc). The 14-22% is an SNV estimate; the polymorphic share of indels and SVs is unmeasured, and Day holds that SVs are 'with very few exceptions, post-divergence' (Q100). Proposed follow-up GAP-07c: intersect the alignment differences with population allele frequencies to measure the polymorphic share directly. Review: `research/checks/REVIEW.md` (review #8, 2026-10-09).

R4 GAP-07c (research/checks/results/R4-GAP07c.md; reviews REVIEW-R4-GAP07c-{correctness,steelman}.md; review #13, 2026-10-09): 15.6% of human-derived divergent SNVs have the chimp allele at >= 1% in 1000 Genomes (14.8-16.7% per chromosome; NYGC 16.06% vs phase 3 16.11% on chr21+22, same people, independent pipeline), consistent with the human half of CSAC's 14-22%. The chimp side is not measured. SVs >= 50 bp on the human lineage: 6.8% net (n = 450; short-read set, lower bound). Indels on the human lineage: 7.4-8.7% (9.5-10.5% in mask). Sorted ancestral variation is not measured. 84.4% of human-derived SNV differences are fixed.

## Simulator variables implied
- `fixed_fraction_of_observed` toggle on the requirement.
