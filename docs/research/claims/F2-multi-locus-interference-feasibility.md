---
id: F2
title: "Feasibility of pipelining: multi-locus sweeps under linkage, interference and cost (proposed check)"
side: day
branch: F
parent: F
edges: [{type: depends-on, target: F1}, {type: depends-on, target: F1a}]
load_bearing: true  # Day's strongest remaining form of the throughput argument rests on parallel width being capped at ~230 or by cost
sourcing: firsthand
status: reviewed
verdicts:
  internal: "holds"   # interference exists (clonal R_int 0.09-0.65)
  fidelity: n/a
  external: "contested"   # no collapse to 272 active loci with free recombination (soft) or below ln R/D (hard); human scale and hard+linkage untested; tight linkage supports Day
---

## Statement (verbatim)
> the "active zone" of intermediate-frequency alleles imposes a hard limit on pipeline capacity of approximately 230 simultaneous sweeps.

Source: [Z18167588, The Bernoulli Barrier (Day & Athos)](https://zenodo.org/records/18167588), Zenodo 2026-01-04 (record modified 2026-01-07), ¶6 of extracted text. abstract

> molecular evolution continues to be characterized by signatures of rapid adaptation, with multiple beneficial variants simultaneously competing for dominance in each population

Source: [Good et al. 2017, The dynamics of molecular evolution over 60,000 generations, Nature 551:45-50](https://pmc.ncbi.nlm.nih.gov/articles/PMC5788700/), 2017, Abstract

## Formal statement
Claim: the number of simultaneous sweeps is bounded (230 in Z18167588; obtained by working backward from the constraint, no derivation shown) or capped by the cost of selection (branch H); critics: independent loci pipeline freely (F1). Good 2017 shows overlapping sweeps in the LTEE.
**Proposed check F2 (not yet run; pre-registered here):** forward Wright–Fisher with L loci, Poisson beneficial-mutation supply U_b per genome per generation, selection coefficient s, soft selection (fixed N), recombination r ∈ {0.5 (free), 0.01, 0 (asexual)}; N ∈ {1,000, 10,000}; s ∈ {0.001, 0.01}; U_b ∈ {0.001, 0.01, 0.1}. Report R = (observed substitutions/generation)/(2N·U_b·u(s)), and the time-averaged number of sweeping loci n_sw.
- Predictions: (a) r = 0.5, U_b = 0.01, N = 1000, s = 0.01: R ≈ 1 (RESULTS F1: 0.3972 vs 0.3960). (b) r = 0, and N·U_b·s large: R < 1 (clonal interference), with n_sw bounded by ≈ the number of segregating beneficial lineages. (c) With realistic human values (N ≈ 10⁴, s ≈ 0.001–0.01, U_b per genome from a stated DFE) R is the quantity that tests Day's ~230 cap and the cost-of-selection cap; no prediction is pre-registered for the cap itself because its derivation is not in the corpus.
- Would change the verdict: R ≥ 0.5 at human-like parameters falsifies a binding cap of order 230 for the neutral-plus-beneficial count; R ≪ 0.5 with r = 0.5 and soft selection would support Day.

## Assumptions
- Stated: Day: parallel width limited to ~230 sweeps.
- Implicit: Hard selection (cost) applies (H); linkage as in asexuals for the LTEE, but humans recombine.

## Responses
- Against: Camestros / Myers / Hancock (serial reading; no numbers on the cap).
- In support: Good 2017 (LTEE interference).
- Weaknesses in the responses: The LTEE is asexual and largely nonrecombining (Reddit RE-07, A5), so LTEE interference does not transfer to humans without the check.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Good 2017 | "This striking separation of timescales between inter- and intra-clade fixations cannot be explained by clonal interference" | verified (ledger) |

## Pre-registered prediction
Written **before** the check runs.
- Under the claimant's model: Parallel width is capped.
- Under the opposing model: Parallel width in free-recombination populations is limited only by cost/variance, not by interference.
- Result that would change a verdict: See Formal statement.

## Check
R4 F2 (`f2_multilocus.py` seed 4242 with crc32-derived seeds, `f2_fwdpy11.py`; research/checks/results/R4-F2-A.md) and H2 (`h2_hard_selection_multilocus.py`; research/checks/results/R4-H2-hard.md). Soft selection, N = 1000, s = 0.01: clonal R_int falls 0.645 -> 0.088 as 2N*U_b goes 0.1 -> 32; a 0.1 M map gives 0.204; one 1.5 M linkage group 0.572 at 208 active loci; free recombination 0.975 +/- 0.005 at 272 active loci, linear in supply; fwdpy11 agrees. Day's cap (R < 0.5 by ~230 loci) is not reproduced for r = 1/2 in the tested regime. Hard selection (H2, free recombination, imposed demand): rate = demand until total log-load exceeds ln R; ~255 open loci persist at R >= 10, ~90 at R = 2. Untested: human-scale active loci (~1e4-1e5 by Little's law), hard selection combined with linkage, N = 1e4, DFE. Credit to Day: interference is real under tight linkage. Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)
Earlier note: Script: proposed `research/checks/f2_multilocus.py` (not yet written) · Result: none. Queued in REVIEW.md.

## Simulator variables implied
- number of loci
- recombination rate
- soft vs hard selection
- selection coefficient distribution
- U_b
