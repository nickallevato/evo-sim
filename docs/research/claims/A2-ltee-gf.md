---
id: A2
title: "G_f from the LTEE: 1,322 generations per fixation (non-mutators, 60,000 generations)"
side: day
branch: A
parent: A
edges: [{type: supports, target: A}, {type: depends-on, target: A2a}, {type: depends-on, target: A2g}]
load_bearing: false
sourcing: firsthand
status: reviewed
verdicts:
  internal: holds
  fidelity: unverifiable
  external: "contested"   # order of magnitude reproducible; calibration underdetermined (R4 A-sim)
---

## Statement (verbatim)
> The result for non-mutator populations is 1,322 generations per fixation at 60,000 generations — cross- validated at 893 generations per fixation by clone-pair analysis at 50,000 generations.

Source: [MITTENS 3.0, Zenodo 23003785](https://zenodo.org/records/23003785) (key Z23003785), 2026-09-28 (modified 2026-10-04), p.1 (abstract). PDF hyphenation "cross- validated" preserved.

## Formal statement
G_f = (generations in window) / (fixations in window) = 60,000 / 45.4 = 1,321.6   (`ltee.gens_per_fixation.day_mittens3_nonmutator`)

`derived:` G_f across versions (all recomputed, python3 -I):

| Version | G_f | Basis | Reconciles? |
|---|---|---|---|
| 2019 (B2019-02-07) and 2025 (Z18165980, Z18168236) | 1,600 | 25 mutations / ~40,000 gens (40,000/25 = 1,600) | Yes (arithmetic). Citation differs: "NATURE, 2009" (2019) vs Good et al. 2017 (2025); see A2a. |
| Book (per Z23003785 s3.3) | 1,400 | "taken from Good et al.’s published summary" | not derivable here |
| 3.0 clone-pair (50,000 gens) | 893 | 50,000 / 56.0 = 892.9 | Yes |
| 3.0 metagenomic (60,000 gens) | 1,322 | 60,000 / 45.4 = 1,321.6 | Yes |
| Z23105291 strict | 1,587 | 60,000 / 37.8 (189 fixations over 5 populations, 189/5 = 37.8) | Yes (derived in `parameters.yaml`) |
| Ara+2 | 909 or 917 | 60,000/66 = 909.1 (blog) vs 60,500/66 = 916.7 (Table 1) | Yes; the inputs differ by 500 gens |

The headline changed from 1,600 to 1,322 to 1,587 within nine months; the direction of the later correction (1,587) increases the shortfall by 1,587/1,322 = 1.20x.

## Assumptions
- Stated: LTEE non-mutator populations are the measuring instrument; the count is "all-cause" fixations (beneficial plus hitchhikers plus everything else); the rate already includes parallelism (G1).
- Implicit: the count is not sensitive to the fixation-calling rule (but see A2b), and 60,000 generations is a stationary window (Day's own s4 text says "The rate is slowing." after the per-milestone table).

## Responses
- Against: Camestros (CA-07): "Day simply has not shown that. He has one estimate for his Gf term that he claims, without demonstrating it, to be a particularly fast fixation rate." See A2d. Dumb-and-Dumber (RE-03, RE-04): estimator problems (A2c). Scaling to humans (A5 family).
- In support: Camestros (CA-10) concedes it is an average. Tenaillon 2016 independently reports constant-rate accumulation of neutral mutations in non-mutator lines (A2g).
- Weaknesses in the responses: critic arguments on the estimator target the clone-pair and the mutator-corrected columns more than the non-mutator metagenomic headline; no critic recomputed 45.4. On Day's side, three different counting rules are in use within one week of publication (A2b).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Good et al. 2017 | "molecular evolution continues to be characterized by signatures of rapid adaptation, with multiple beneficial variants simultaneously competing for dominance in each population"; the "≥95%" rule is not in the main text | unverified (SI not retrieved) |
| Tenaillon et al. 2016 | "neutral mutations accumulate at a constant rate" in populations that kept the ancestral mutation rate | verified |
| Barrick et al. 2009 | "genomic evolution was nearly constant for 20,000 generations" | verified (abstract only) |

## Pre-registered prediction
No check has run. Component of the pre-registration: the metagenomic count depends on a calling rule; the lineage-aware count in Z23105291 is the stricter alternative.
- Under the claimant's model: G_f is stable (1,300–1,600) across counting rules and windows.
- Under the opposing model: G_f depends on the rule (1,322 vs 1,587, A2b) and on estimator artefacts (A2c) at the 20–50% level, which is immaterial next to a million-fold shortfall; the dispute is therefore about transfer (A5), not the measurement.
- Result that would change a verdict: a recount from the raw Good 2017 data giving G_f outside 900–2,500 for non-mutators.

## Check
Arithmetic audit (python3 -I, scratch) reconciles every G_f row. No recount from raw LTEE data has been run. Review: pending.

R4 A-sim (research/checks/results/R4-F2-A.md): G_f of order 1,300-1,600 is reproducible in a clonal fixed-s model at Ne = 3.3e7 (unsourced assumption), but the calibration is underdetermined (U_b spans 3 orders of magnitude: 6.7e-7 / 8.4e-9 / 6.3e-10 for s = 0.003 / 0.01 / 0.03) and a single-s fit conflates neutral and adaptive fixations (neutral expectation ~54% of 1/1322). G_f is a statement about an Ne*U_b*s combination, not a universal constant. Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)

## Simulator variables implied
- LTEE preset library: G_f by population and counting rule (≥95% pooled vs lineage-aware), mutator flag, window length.
