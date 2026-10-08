---
id: B4d
title: "Dating by k = mu is circular: the divergence date is derived from the identity it is cited to confirm"
side: day
branch: B
parent: B4
edges: [{type: supports, target: B4}]
load_bearing: false  # rhetorical support for the irrelevance claim; MITTENS counts do not use it
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: partial
  external: contested
---

## Statement (verbatim)
> The circularity is complete. The divergence date was calculated from k = μ. The mutation rate was adjusted to keep the date consistent with k = μ.

Source: [Z22903977, The Intrinsic Irrelevance of Kimura's Substitution Rate (Day & Athos)](https://zenodo.org/records/22903977), Zenodo 2026-09-22 (v1), §5 The Circularity

> The identity is its own evidence. At no point does an independent measurement enter the loop.

Source: [Z22903977, The Intrinsic Irrelevance of Kimura's Substitution Rate (Day & Athos)](https://zenodo.org/records/22903977), Zenodo 2026-09-22 (v1), §5

## Formal statement
T = D/(2μ) (IR §5). Claim: μ was phylogenetically calibrated, then replaced by pedigree μ with the date pushed back "to maintain consistency".
Analysis (derived reasoning): a date from pedigree μ and generation time is independent of the fossil calibration but not of the *assumption* k = μ per generation; and the older direction is what Keightley 2012 reports (pedigree μ about twofold below divergence-based rates). Langergraber 2012 derives "at least 7-8 million years" without fossil calibration, using pedigree μ and wild-chimp generation times, so the loop is not closed by a measurement of the date.

## Assumptions
- Stated: The molecular clock's sole use is calibration; it is circular.
- Implicit: The mutation rate used in recent dating is not independently measured.

## Responses
- Against: "the neutral theory of evolution cannot explain common ancestry between humans and chimps at all based on genome-wide nucleotide differences between the two species, since the neutral theory is used in the first place to date the assumed time of divergence." ([Hossjer, "MITTENS - Convincing Arguments Against Neo-Darwinism" (PDF attached to Dembski post)](https://billdembski.substack.com/api/v1/file/f5a8533e-7b7c-407b-880b-1ecbd256784c.pdf), 2026-09-14, PDF p5 (Hössjer, an ally, makes the same point; B4f))
- In support: Keightley 2012 (the rate fell, the date rose).
- Weaknesses in the responses: Both McCarthy (B4e) and Hössjer (B4f) state the dependence; none of the three give a dated-values chain with references.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Keightley 2012 | "Direct estimates from genome sequencing of relatives suggest that μ is about 1.1 × 10(-8), which is about twofold lower than estimates based on the human-chimp divergence." | verified-partial (abstract only) |
| Langergraber 2012 | "We date the human-chimpanzee split to at least 7-8 million years and the population split between Neanderthals and modern humans to 400,000-800,000 y ago." | verified; Day cites it as 6–7 My (misread, ledger) |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: The date of ~6–8 My carries no independent evidence for k = μ.
- Under the opposing model: Fossil-calibrated and pedigree-based dates agree within a factor ~1.5; the agreement is evidence for the assumption.
- Result that would change a verdict: Showing a date-independent test of k = μ (e.g., Ne-independent comparison of closely related pairs with known split dates).

## Check
Script: none.

## Simulator variables implied
- μ source
- generation time
- calibration
