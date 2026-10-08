---
id: E9
title: "Good et al. 2017: LTEE trajectories are inconsistent with sweep-by-sweep 'periodic selection'; clades coexist; whole-population fixations lag the number of adaptive mutations in some populations"
side: literature
branch: E
parent: A2
edges: [{type: attacks, target: A2}, {type: supports, target: E6}]
load_bearing: false  # Governs how LTEE G_f may be read; Day now builds on the same dataset (Z23105291). Alone it does not change ROOT.
sourcing: firsthand
status: extracted
verdicts:
  internal: n/a
  fidelity: n/a   # this file records the source itself; Day's use is judged in E (E8) and E6 (E9)
  external: pending
---

## Statement (verbatim)
> "We find that the trajectories in Fig. 1 are inconsistent with a "periodic selection" model in which individual driver mutations fix in a sequence of discrete selective sweeps."

Source: Good et al. 2017, [The dynamics of molecular evolution over 60,000 generations](https://pmc.ncbi.nlm.nih.gov/articles/PMC5788700/), Nature 551:45, Results (quote in `sources/quotes-literature.md`).

> "The number of fixed mutations closely tracks Mp(t) in some populations (e.g. Ara+2 and Ara+4), but there is a marked deficit of fixations in others (e.g. Ara-6)."

Source: same, Results.

> "This striking separation of timescales between inter- and intra-clade fixations cannot be explained by clonal interference"

Source: same, Results.

## Formal statement
Qualitative: clade structure (two coexisting lineages in nine of twelve populations per Z23105291's reading of the same data) means pooled frequency ≥95% does not imply whole-population fixation. Relevant parameters: `ltee.whole_pop_fixations_lineage_aware` (5,496), `ltee.gens_per_fixation` (E6). The "≥95% rule" is not in the main text (fidelity ledger: "unverified" until the SI is read).

## Assumptions
- Stated: LTEE metagenomic time series of all 12 populations, ~500-generation resolution.
- Implicit: that Day's "fixed" in G_f corresponds to the authors' haplotype-state calls.

## Responses
- Against: none directly.
- In support: Day's own Z23105291 (E6) adopts the authors' lineage-aware state; E5 (the Ara+5/Ara-2 numbers) is consistent with the deficit noted here.
- Weaknesses in the responses: the repo lacks the SI and the data files; nothing here tests the 5,496 count.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Good 2017 | quotes above | accurate as quotes; Day's earlier use of "≥95%" unverified (ledger) |

## Pre-registered prediction
- Under the literature: strict whole-population counts are lower than pooled-≥95% counts in populations with surviving minor clades.
- Under Day's earlier use: ≥95% pooled frequency counts as fixation (Z23003785); superseded by E6.
- Result that would change a verdict: an SI statement of a 95% threshold in Good 2017 (then the earlier Day use is accurate to the source, and its overcounting is a Good-et-al.-compatible definition issue).

## Check
Script: none (needs SI access). · Result: not run · Review: pending

## Simulator variables implied
Clade structure, minor-lineage frequency at end, counting rule.
