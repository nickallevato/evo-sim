---
id: B4a
title: "Pairwise divergence = 2 mu T + theta_anc: two-lineage forward simulation with incomplete lineage sorting"
side: literature  # audit check (two-lineage simulation on CSAC 2005 / Day's IR §3 formulas); 'audit' is not an allowed side in lint_research.py
branch: B
parent: B4
edges: [{type: depends-on, target: B6}, {type: depends-on, target: B1b}, {type: attacks, target: B1a}]
load_bearing: true  # decides whether fixed-difference deficits (B1) apply to the observable that is actually compared (sequence divergence)
sourcing: firsthand
status: reviewed
verdicts:
  internal: "holds"   # forward sim matches formula within ~0.3%; msprime agrees
  fidelity: "accurate"   # CSAC polymorphic share matches poly-but-diff
  external: "contested"   # overshoots 1.23% by ~25% at HCB node; half at Ne 1e4; (mu, T, Ne_anc) underdetermined; Yoo mu unrecorded
---

## Statement (verbatim)
> t 1 is constant across loci (,6-7 million years38), t 2 is a random variable that fluctuates across loci (with a mean that depends on population size and here may be on the order of 1-2 million years39)

Source: [Chimpanzee Sequencing and Analysis Consortium 2005, Nature 437:69-87](https://www.nature.com/articles/nature04072), 2005, Main text, "Genome-wide rates" (extraction renders "~" as ","; t1 = time since speciation, t2 = ancestral coalescence time)

> where D is the number of neutral differences and the factor of 2 accounts for both lineages.

Source: [Z22903977, The Intrinsic Irrelevance of Kimura's Substitution Rate (Day & Athos)](https://zenodo.org/records/22903977), Zenodo 2026-09-22 (v1), §5 The Circularity

> Under coalescent theory, the expected pairwise divergence contributed by ancestral polymorphism is θ = 4Nₑμ per site.

Source: [Z22903977, The Intrinsic Irrelevance of Kimura's Substitution Rate (Day & Athos)](https://zenodo.org/records/22903977), Zenodo 2026-09-22 (v1), p.3 (§3)

## Formal statement
E[d] = 2μT + 4Nₑ,anc μ per site (T in generations; coalescence in the ancestor at mean 2Nₑ,anc generations), where d is the difference between one haplotype from each species (includes polymorphism); fixed differences are the subset fixed in both.

**Derived illustration (python3 -I; μ = 1.2e-8 pedigree, 25 y/gen, T = 252,000, L = 3.2e9):** 2μT = 6.05e-3 per site (19.4M sites). θ_anc = 4Nₑμ: Nₑ = 1.0e4 → 4.8e-4 (1.5M sites); 1.32e5 (Yoo HCG) → 6.3e-3 (20.3M); 1.98e5 (Yoo HCB) → 9.5e-3 (30.4M). Totals: 0.65%, 1.24%, 1.56% vs observed 1.23% (CSAC, including polymorphism; fixed ≤ 1.06%). With Nₑ = 1e4, matching 1.23% requires T ≈ 492,500 generations (12.3 My at 25 y). These are illustrations of how the ancestral term depends on the Nₑ input, not verdicts.

**Proposed check B4a (not yet run; pre-registered here):** forward Wright–Fisher, ancestral Nₑ ∈ {1e4, 3e4, 1.32e5, 1.98e5} for 8Nₑ generations (equilibrium), split into two lineages (Nₑ = 1e4 each, constant), run T ∈ {50k, 100k, 252k} generations, plus a third outgroup lineage for ILS; sample one genome per species and n = 10 per species; report (i) mean pairwise d vs 2μT + θ_anc, (ii) fixed vs polymorphic fraction of d, (iii) fraction of gene trees discordant with the species tree vs (2/3)exp(−T_int/2Nₑ,anc), (iv) the B1b-style fixed-substitution count per lineage.

## Assumptions
- Stated: Day (IR): ancestral polymorphism is a rounding error (θ = 0.35% of 410M, Nₑ = 10⁴).
- Implicit: Day: Nₑ,anc = 10⁴; critics: Nₑ,anc ≈ 1.3–2×10⁵ (Yoo), which makes θ_anc a first-order term.

## Responses
- Against: n/a (check proposal)
- In support: n/a
- Weaknesses in the responses: Yoo 2025's Nₑ,anc derives from coalescent inference with its own μ and generation time assumptions (see B3h).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Chimpanzee Sequencing and Analysis Consortium 2005 | "we estimate that polymorphism accounts for 14-22% of the observed divergence rate" | verified (ledger) |
| Yoo 2025 | Nₑ,anc = 198,000 (HCB) and 132,000 (HCG) | verified (ledger) |
| Scally 2012 | "In 30% of the genome, gorilla is closer to human or chimpanzee than the latter are to each other" | context for ILS |

## Pre-registered prediction
Written **before** the check runs.
- Under the claimant's model: (Day) ancestral term negligible; fixed count is lowered by the empty-pipe correction.
- Under the opposing model: (standard theory, CSAC) pairwise divergence includes a coalescent term that does not depend on fixation latency; the fixed-substitution count is not the observable.
- Result that would change a verdict: If the simulated d matches 2μT + θ_anc to within SE and the fixed-count deficit does not alter d, Day's empty-pipe correction does not apply to the observable (B1a internal verdict stands, relevance falls). If d falls below the standard prediction by about μL·4Nₑ, Day is supported.

## Check
R4 B4a (`b4a_two_lineage_ils.py`, seed 20261009, burn-in 20 N_sim; research/checks/results/R4-B1c-B4a.md): forward simulation gives d - 2muT = theta_anc within ~0.3% in every row; msprime agrees. CSAC's 14-22% polymorphic share matches the poly-but-diff column (config B, human 1e4 / chimp 4.6e4: 22-25%), so there is no tension. At the relevant node (HCB, Ne_anc = 1.98e5) d = 1.55-1.56%, ~25% above observed 1.23%; at Day's Ne = 1e4, d = 0.65%, about half (Day-side point). The data fix only 2muT + 4Ne_anc*mu (a 3-parameter fit), and Yoo's own mu is not recorded, so the Ne_anc rescaling is open. ILS discordance and outgroup not run. Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)
Earlier note: Script: proposed `research/checks/b4a_two_lineage_ils.py` (not yet written) · Result: none. Required by REVIEW.md review #3 (B1b caveat) and queued.

## Simulator variables implied
- ancestral Nₑ
- post-split Nₑ per lineage
- T
- μ
- sample sizes
- outgroup branch length
- observable (pairwise | fixed | ILS fraction)
