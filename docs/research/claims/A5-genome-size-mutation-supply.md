---
id: A5
title: "The LTEE rate does not transfer to humans: the human genome is ~690x larger and has far more new mutations per generation"
side: critic
branch: A
parent: A2
edges: [{type: attacks, target: A2e}]  # A5 -> A2 removed 2026-10-08: A5 grants the LTEE measurement and attacks its transfer to humans, which is A2e
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds
  fidelity: n/a
  external: contested
---

## Statement (verbatim)
> The human nuclear genome contains approximately 3.1 billion base pairs, roughly 690 times larger than the compact E. coli genome of about 4.6 million base pairs.

Source: [Dennis McCarthy, Why Probability Zero is Wrong About Evolution (free repost)](https://dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1), 2026-09-11 (orig. paid 2026-01-26), para 60 (MC-05).

> As clear, the expected rate of fixed mutations has to be determined according to the particular circumstances of the population in question—its genome size, mutation rate, etc.

Source: same post, para 62 (MC-07).

## Formal statement
supply_ratio = (μ_human · L_human) / (μ_E · L_E).
`derived:` (python3 -I) 3.1e9/4.6e6 = 674 (McCarthy states "roughly 690"; 690 follows from a 4.5 Mb E. coli genome, 3.1e9/4.5e6 = 689; a 2% discrepancy with his own stated inputs). Per-site rate ratio 1.2e-8/8.9e-11 = 135 (8.9e-11 is the Wielgoss 2011 figure via McCarthy; not in the quote files). Per-genome ratio 38.4/4.1e-4 = 93,659 using the numbers in MITTENS 3.0 (4.1e-4 from s4.3; 38.4 = 3.2e9 x 1.2e-8 from the s6.4 product, where the paper prints only the 100x value 38,400). Neutral expectation for supply scaling alone: E. coli 4.1e-4 per generation vs human 38.4 per haploid genome per generation.

## Assumptions
- Stated: the expected fixation rate depends on genome size and mutation rate.
- Implicit: fixation rate of adaptive mutations scales (linearly or otherwise) with supply; recombination and clonal interference do not reverse the direction.

## Responses
- Against (Day): blog 2026-01-27 ¶22: "I didn't cite the E. coli study for its mutation rate but for its fixation rate" (A5g); 3.0 s5.1 mutators give only sublinear gains (A5d).
- In support: Hössjer (A5a), Sparky_6_4 (A5b), Hancock (A5c), Dembski (interviewer, DE-01) asks the question to Day; Duffy concedes "the mammal fixation rate is slower" (DU-06) without numbers.
- Weaknesses in the responses: McCarthy's uncited "60 to 100 de novo mutations" is a diploid per-newborn count (MC-06) while the E. coli figure is haploid per division; the 690 factor has a 2% internal discrepancy; the critic gives no dependence of adaptive fixations on supply.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kong et al. 2012 | "with an average father's age of 29.7, the average de novo mutation rate is 1.20×10-8 per nucleotide per generation" | verified (abstract) |
| Keightley 2012 | "μ is about 1.1 × 10(-8) … an average of ~70 new mutations arise in the human diploid genome per generation" | verified-partial (abstract) |

## Pre-registered prediction
See A5b for the scaling arithmetic and the proposed A-sim (pre-registered in file A).
- Under the claimant's (critic's) model: the rate scales with supply to within a factor 2 at least.
- Under Day's model: the LTEE rate is a ceiling (A2e).

## Check
Arithmetic audit (python3 -I, scratch). Review: pending.

## Simulator variables implied
- `mu_per_site_per_gen`, `genome_length`, `new_mutations_per_genome` as inputs to the supply term.
