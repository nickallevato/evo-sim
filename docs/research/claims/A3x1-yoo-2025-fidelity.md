---
id: A3x1
title: "Yoo 2025 reports 327 Mb average SDR per lineage; the 410 Mb and 187 Mb figures are not in it"
side: literature
branch: A
parent: A3x
edges: [{type: supports, target: A3x}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: n/a
  fidelity: misread
  external: supported
---

## Statement (verbatim)
> We catalogued all structurally divergent regions (SDRs) among the ape genomes and found an average of 327 Mb of sequence (10%) per ape lineage

Source: Yoo et al. 2025 (key Yoo2025), main text, "Divergence and selection".

> 12.5-27.3% of an ape genome failed to align or was inconsistent with a simple one-to-one alignment

Source: same.

> we curated 1,140 interspecific inversions, of which 522 are newly discovered

Source: same, "Structural variation".


RH tag (2026-10-10 pass): dialectic (literature source, no side).
## Formal statement
`divergence.structurally_divergent_Mb_per_lineage.yoo_2025` = 327. `derived:` 327 x 2 = 654 Mb (both lineages, if additive); 410/327 = 1.25. Brute-force search over SDR totals (Table V.24: human h1/h2 147.8/183.6 Mb; chimp h1/h2 288.9/308.2 Mb) found no combination giving 187 or 410 (closest 412.1 = HSA h2 + PAB h1, flagged as coincidence). 1,140 inversions is across six apes versus the human reference. Ledger status: **not-found** (the figures are absent from main text, SI text and tables). Classified here as `misread` for the fidelity verdict on Day's citation because Yoo supplies a different, specific, sourced figure (327 Mb); the ledger label remains not-found.

## Assumptions
- Stated by Yoo: SDRs are average per lineage; gap divergence is reported in megabases.
- Implicit: whether SDR megabases are fixed differences or include polymorphism between haplotypes.

## Responses
- Against (Day): Day may have derived 410M from sources outside Yoo 2025 (the 2nd-edition post reports 14.9% and 410M bp); the repo cannot exclude this.
- In support (critics): the figure is not in Yoo.
- Weaknesses in the responses: the harvest of Yoo SI is complete only to the extent of the downloaded files; supplementary tables other than 14, 24, 67 were not searched cell-by-cell.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Yoo2025 | above | Day's 410 Mb / 187 Mb: not-found |

## Pre-registered prediction
No prediction. Result recorded.

## Check
Brute-force table search done in R1 (ledger). Review: pending.

R4 L7 (research/checks/results/R4-L7.md; awaiting review, 2026-10-11): Day's new locator (Q179 post: 'pages 14, 19, and 24') points to Tables III.14, III.19 and V.24. Mean SNV + mean gap divergence (III.14, human-chimp, 13.94%) x hs1 autosome length (III.19) = 404.2 M bp (A+X 412.7 M), within 2% of 410 M; three routes land within 2% and matches near 410 M are common (see the fix pass below), so the route is unconfirmed. 14.9% is not reproduced exactly (nearest 15.05%, at 436.5 M). After review: the 410 M label moves from not-found to 'reconstructible (bp), route unconfirmed'; 187 Mb stays not-found. Fix pass (review a183774): the reconstruction needs the mean gap divergence (medians give 82 M); the pre-registered base-rate test was replaced post hoc by a primitive-pool test (410 M at the 92nd-100th percentile of random targets, ratio 1.3-1.7: matches are common, so a match does not identify a route); A3x1's verdicts unchanged.

## Simulator variables implied
- None.
