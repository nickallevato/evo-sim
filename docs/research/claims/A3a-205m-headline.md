---
id: A3a
title: "Required fixations rise to 205M: 410M genomic differences from Yoo 2025, halved per lineage"
side: day
branch: A
parent: A3
edges: [{type: supersedes, target: A3}, {type: depends-on, target: A3x1}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds   # R4 X1 rule rev 2 (was arithmetic-error): charity (rule 3): 187 Mb read as SDRs per lineage, the pairwise total is 35M + 1,140 + 2 x 187M = 409.0M vs 410M (0.24%) and per lineage 204.5M vs 205M, so ledger (literal sum 222M, 46%/85%). Fidelity misread (187 ...
  fidelity: misread   # Yoo 2025 gives 327 Mb average SDR per ape lineage; 410/187 not found (A3x1)
  external: contested   # contradicted if 205M is read as an event count (R4 GAP-07b: measured ~21M events per lineage, hg38 vs panTro6, non-T2T; bracket 7-14x). Day's stated reading (04-28 ¶19, 05-13 ¶4-6; Q99, Q101-Q103) is a weighting claim with a range; it is untested, and as a weight it would need ~3,250 SNV-equivalents per >50 bp event, against his own event-counting G_f. Base-pair magnitude of non-1:1 sequence is the same order (201-523 Mb, assembly dependent) but not a fixation count
---

## Statement (verbatim)
> approximately 35 million SNVs, 1,140 interspecific inversions, and approximately 187 megabases of structurally divergent regions, for a total of approximately 410 million genomic differences. Apportioned symmetrically to the human lineage this yields approximately 205 million required fixations.

Source: [MITTENS 3.0, Zenodo 23003785](https://zenodo.org/records/23003785) (key Z23003785), 2026-09-28 (modified 2026-10-04), p.11 (s7.1).

> the genetic difference between chimps and humans turned out to be 14.9 percent, with 410 million base pairs separating the two lineages since the Chimpanzee-Human Last Common Ancestor.

Source: [Probability Zero 2nd edition](https://voxday.net/2026/05/23/probability-zero-2nd-edition/) (key B2026-05-23), blog, 2026-05-23, ¶6.

## Formal statement
R_2026 = 410e6 / 2 = 205e6 per lineage (`divergence.required_fixations.day_2026`, derived: 410e6 bp / 2).

`derived:` the stated components do not sum to the stated total: 35e6 + 1,140 + 187e6 = 222,001,140, not 410e6; the text does not show the arithmetic and mixes units (SNVs, events, megabases). 410e6 = 14.9% of 2.75e9 bp (410/0.149 = 2,752 Mb), whereas a haploid human genome is 3.1–3.2e9 bp (0.149 x 3.1e9 = 462e6). The only reconciling arithmetic in the repo is 410/35 = 11.7 (the KITTENS ratio, A5b). Yoo 2025 SDR averages 327 Mb per lineage (x2 = 654 Mb); no pair or sum of the Yoo SDR totals gives 187 or 410 (closest: 412.1, flagged a coincidence).
Version arithmetic that does reconcile: 1,075,000 = 205e6 / 190.6 (1,075,437); 17.5e6 SNV-only: 91,806 (paper 91,600).

Reconciling reading (R4 X1 rule C, 2026-10-09): if Day's 187 Mb is read as SDRs per lineage, the pairwise total is 35M + 1,140 + 2 x 187M = 409.0M (0.24% from 410M), and per lineage 204.5M vs 205M. On that reading the parts sum; the literal list (222M) does not. Under the single both-sides rule this is a ledger slip (internal holds). The fidelity (187 and 410 not in Yoo) and the unit question (bp vs events, A3x) are unaffected.

## Assumptions
- Stated: complete T2T assemblies reveal more divergence than the 2005 draft; each affected base counts as a required fixation.
- Implicit: a structural variant of length n bp requires n separate fixations (A3x); the 410M figure comes from Yoo 2025.

## Responses
- Against: McCarthy (MC-11), Dumb-and-Dumber (RE-05), Hancock (GG-10–GG-12), Sparky_6_4 (RE-08) argue the count mixes bases and events (A3x). Mansfield (MF-06): numbers he has seen are ~25 million, not 200 million. Fun-Friendship4898 (Reddit 1wv4zeg, comment pdbyv0a; verified in `sources/raw/critics/arctic-tree-1wv4zeg.json`) reconstructs the total: "multiplying 187Mb by 2, then adding the 35 million SNVs onto it", and notes "a good chunk of those 35 million SNVs are already contained within those SDRs" (R4 GAP-07 credit).
- In support: Day concedes in s7.3: "This is a legitimate methodological concern" and runs MITTENS on SNVs alone (A3b).
- Weaknesses in the responses: the critics' event-count alternative (about 40M) is itself derived from the 2005 consortium counts, not recomputed from Yoo 2025; Hancock (GG-10) only "suspects" the 205M includes gap divergence.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Yoo et al. 2025 | "We catalogued all structurally divergent regions (SDRs) among the ape genomes and found an average of 327 Mb of sequence (10%) per ape lineage"; "we curated 1,140 interspecific inversions" | **not-found** for 410 Mb and 187 Mb (ledger); see A3x1 |

## Pre-registered prediction
Not run. Prediction (claimant): a lineage-aware count of independent fixed mutational events from Yoo 2025 exceeds 100M. Prediction (critic): it is within 1.5x of 40M events (35M SNV + ~5M indels + ~1,140 inversions + other SV events).
- Result that would change a verdict: a published count of fixed SV events in human–chimp comparisons.

## Check
Arithmetic audit (python3 -I, scratch): the 410M total does not reconcile with its stated parts. Review: pending.

R4 GAP-07 (research/checks/results/R4-GAPS-04-07-02.md): 205M is a base-pair figure; events per lineage are 18-22.5M (calibrated / CSAC-observed), ~9-11x lower (>= 8x at observation-consistent inputs). Under k = mu, de novo SVs alone deliver 0.35-0.92 Gb per lineage, the same order as SDR base pairs (Yoo human-lineage 148-184 Mb, Day's 187 Mb, cross-ape 327 Mb); the agreement is order-of-magnitude only, since SDRs are dominated by centromeres, acrocentric arms and heterochromatic caps. On a repeat-unit reading (Yoo's 171/32 bp satellite units) the count is 21-30M. Review: `research/checks/REVIEW.md` (review #6, 2026-10-08).

R4 GAP-07b (research/checks/results/R4-GAP07b-alignment.md): direct count from the UCSC hg38 vs panTro6 net/chain/axtNet alignment (non-T2T; both lineages plus polymorphism): 37.77M SNVs + 4.30M indel events = 42.10M events, 21.05M per lineage; 205M is 9.7x raw (pre-registered), bracket about 7-14x (Day-favourable repeat-unit and slippage readings 7.2-9.5; critic-favourable human-lineage, top-level-fill, <2%-divergence and polymorphism corrections 10.1-13.4, all post hoc). Day's stated position is a range (SNV-only lower, bp upper) with a weighting claim (Q99: SVs fix 'as a single low-probability event'; bp counting 'is generous to the standard model'); as a weight, 205M needs ~3,250 SNV-equivalents per event above 50 bp. Bases outside every aligned block are 261 Mb (201 Mb without hg38 centromere models), so 410M is not an invented magnitude, but the check does not show 410 Mb *differ*. The 410.09 Mb and 187.0 Mb matches among component sums are at the chance base rate (3 hits in 3,458 subsets). Review: `research/checks/REVIEW.md` (review #8, 2026-10-09).

R4 X1 (research/checks/results/R4-X1-rescore.md; rule research/checks/results/R4-X1-verdict-rule.md rev 2; review #12, 2026-10-09): under the single both-sides rule this node is holds / misread. charity (rule 3): 187 Mb read as SDRs per lineage, the pairwise total is 35M + 1,140 + 2 x 187M = 409.0M vs 410M (0.24%) and per lineage 204.5M vs 205M, so ledger (literal sum 222M, 46%/85%). Fidelity misread (187 and 410 not in Yoo) and external contested (bp vs events, A3x) are separate and unchanged Charitable reading tried: tried 187 Mb per lineage: pairwise 409.0M, per lineage 204.5M reproduce 410M/205M (0.24%) -> holds + ledger.

## Simulator variables implied
- `required_fixations` presets: events (about 40M total, 20M per lineage), SNV only (17.5M), bp-affected (205M).
