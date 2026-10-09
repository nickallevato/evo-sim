---
id: C5b
title: "A temporal-method Ne from ancient genomes (8,139 over 102 generations; 9,835 over 250) agrees with the canonical ~10,000 without presupposing the clock"
side: critic  # keruru rule (opponents/keruru.md): 2026-08-31 post
branch: C
parent: C5
edges: [{type: attacks, target: C5a}, {type: attacks, target: C4}]  # judgement (kept): C5b agrees N_e changed (it 'roughly doubles') but its window averages (8,139; 9,835) answer C4's use against C5; main target is C5a
load_bearing: false  # Answers the circularity objection to C5; ROOT unaffected.
sourcing: firsthand
status: reviewed
verdicts:
  internal: holds   # slip ledger (X1 rule: <25% and no flip): the sampling correction 1/(2S) with S an allele count under-corrects pseudo-haploid bins by half, a 7-19% effect on the two headline windows (0.7-26.5% across windows) in the conservative direction (R4 C1d)
  fidelity: n/a
  external: supported   # as a lower-bound variance N_e of the sampled series: R4 C1d replicates his values to within 4% (7,812 / 9,672 vs 8,139 / 9,835; within 1-8% for all seven windows) in two AADR releases; corrected 9.7k / 10.5k; it is a lower bound on a drift N_e; C5a's N_e near 2 is excluded
---

## Statement (verbatim)
> "The temporal method takes allele frequencies from two dated ancient samples, the sample sizes, and the generations between them. No mutation rate. No coalescent. No substitution identity."

Source: keruru, [Kimura and the Red Flock](https://claudekeruru.substack.com/p/kimura-and-the-red-flock), 2026-08-31, section "What we found" (first finding). Author status: formerly built on Day, now an independent critic.

> "Applied to seventeen thousand ancient genomes: Bronze Age to Medieval West Eurasia gives Nₑ = 8,139 over 102 generations on 1.1 million autosomal positions. Early Neolithic to present gives 9,835 over 250."

Source: same post, same section.

> "Drift is slowing, not accelerating."

Source: same post, same section (second finding): "Anchoring every comparison on one early bin gives a trajectory rather than a point: effective size roughly doubles from the Neolithic to the present across the well-powered bins."

## Formal statement
Temporal-method Ne from allele-frequency change F between two dated samples with sizes S0, St and t generations apart: Ne is approximately t/(2 [F - 1/(2 S0) - 1/(2 St)]) (Waples-type estimator; the post names the method but gives no formula, so this is the repo's reading, not a quote). Inputs: AADR v62-type data (about 17,000 ancient genomes), 1.1 million autosomal positions; 102 and 250 generations.

derived: E[F] is about t/(2 Ne). For Ne = 9,835 and t = 250 this is 250/(2 x 9,835) = 0.0127. For Ne = 2 (Day's C5a figure) it is 250/4 = 62, i.e. saturated: every intermediate locus would be lost or fixed within the window, which is not what Z23046531 reports (17,806 newly 100% loci out of 1,143,671, almost all from the 90-99% band). The Ne-near-2 reading is therefore incompatible with the window's own fixation counts unless the frequency change is dominated by admixture rather than drift. Arithmetic holds; the interpretation is pending.

## Assumptions
- Stated: the temporal method needs no mutation rate or coalescent.
- Implicit: a closed population over the interval (Z23046531 §1 and Z18525185 §5.1 describe Anatolian and steppe replacement in the window; admixture inflates F and lowers Ne); linkage correction: the same author states elsewhere that per-SNP independence was assumed and then withdrawn, reporting that the effective number of tests is "far below the nominal one"; sample-size bias for the earliest bins; the earlier Z18320599 caution that drift-variance derived Ne values cannot be read as population sizes.

## Responses
- Against: Day's Z18320599 Limitations paragraph (C4) and Day's C5a Ne near 2.
- In support: the direction (drift variance falling over time) matches Day's C4 paper.
- Weaknesses in the responses: the numbers and code are the author's statement; the code is said to be deposited on Zenodo and was not retrieved; the posts were produced largely with LLM assistance (opponents/keruru.md).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Waples 1989 / Nei & Tajima 1981 (temporal method) | not cited by name in the post | unverified |
| Mallick 2024 / AADR | about 1.23 million SNP target set | accurate |

## Pre-registered prediction
- Under the claimant's model (critic): a temporal-method Ne on the same data is of order 1e4, stable across windows, with the apparent ratio of 3-5 in drift variance explained by sample composition.
- Under the opposing model (Day): the temporal method yields Ne of order unity to hundreds because admixture and replacement dominate the frequency change; the estimator is invalid across a replacement.
- Result that would change a verdict: a re-run on a restricted continuous region (for example Britain-Ireland, as in Z18320599) with an explicit admixture correction; if Ne remains of order 1e4, circularity is answered; if it collapses, Day's turnover reading is supported for that window.

## Check
R4 C1d (research/checks/results/R4-C1d.md §4, review #10, 2026-10-09): keruru's recipe on the real v66.p1 genotypes gives 7,812 (BA to Medieval; his 8,139, -4%) and 9,672 (Early Neolithic to Modern; his 9,835, -1.7%); the other five windows agree within 1-8%. His sampling term is 1/(2S) with S an allele count, half the standard 1/n for pseudo-haploid bins (his code comments, adna_validate.r L45-46, adna_temporal_ne.r L14); corrected values are 9,665 and 10,508 (Nei-Tajima Fc agrees within 0.3%, near-tautologically). The estimate is a lower bound on a drift N_e; ancestry-informativeness strata barely change F in the BA-to-Medieval window (0.96) and composition among five regions explains 6-17% of it. Credit: replication in two releases; his own disclosure that his biases run downward; his §6.1 simulations.

Script: none yet (spec: part of `research/checks/c4_drift_variance_null.py`; temporal-method estimator on simulated closed and admixed populations with the real sample sizes). · Result: not run · Review: pending

## Simulator variables implied
Temporal-method Ne estimator, interval t, sample sizes, admixture fraction, linkage blocks.
