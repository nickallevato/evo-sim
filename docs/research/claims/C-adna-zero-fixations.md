---
id: C
title: "European aDNA shows ~zero fixations from intermediate frequency across ~1.1-1.2M SNPs in ~7,000 years (blog: 0 of 1,211,499; Zenodo: 1 and 3 of 1,143,671)"
side: day
branch: C
parent: ROOT
edges: [{type: supports, target: ROOT}, {type: depends-on, target: C2}, {type: depends-on, target: C4}, {type: attacks, target: C5}]
load_bearing: false  # ROOT does not rest on C: the MITTENS rate argument (A) and the neutral-theory argument (B) are computed without it. C is offered as empirical confirmation of d (C2) and of "evolution is inoperative" and is cited as such, so a failed C weakens only that supporting leg.
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: n/a
  external: pending
---

## Statement (verbatim)
Version A (blog, 2026-01-14, AADR v62.0):
> "The observed fixation count was zero. Not a single allele in 1.2 million crossed from rare (<10% frequency) to fixed (>90% frequency) in seven thousand years."

Source: [Empirically Impossible](https://voxday.net/2026/01/14/empirically-impossible/), B2026-01-14-empirically-impossible, posted 2026-01-14, para 5 of extracted text (quote Q55 in `sources/quotes-day.md`).

Version B (Zenodo preprint, 2026-09-29):
> "of 1,143,671 autosomal SNPs analyzed, one changed from above 10% starting frequency to fixation or loss. In the replication (AADR v66.p1, analyzed September 29, 2026), three did."

Source: [Allele Frequency Trajectories in the European Ancient DNA Record](https://zenodo.org/records/23046531), Z23046531, 2026-09-29, Abstract (Q52).

> "Across 1.14 million autosomal loci and 7,000 years of European prehistory, zero alleles moved from below 50% starting frequency to regional fixation, and zero moved from below 10% to fixation, in either run."

Source: Z23046531, §4 Discussion, p.6 (Q53).

Day's stated prediction of the two models (blog version):
> "predicts that fixation events should be rare, fewer than 20 across the entire genome."

Source: B2026-01-14-empirically-impossible, para 4 (the 15,500 figure is in the same paragraph).

## Formal statement
Observable: n_fix = number of autosomal panel SNPs whose focal allele is below a start-frequency threshold in a Neolithic European sample (6000-8000 BP) and at 100% (Zenodo) or >90% (blog) in a present-day European sample. Window = 7,000 y = 350 generations at 20 y/gen (blog), g_eff = 350 x d (parameters.yaml: `selection.turnover_d` = 0.45).

Counts reported (all quoted from the sources above and Z23046531 §3):

| Quantity | Blog (Jan 2026) | Z23046531 v62.0 | Z23046531 v66.p1 |
|---|---|---|---|
| SNPs analysed | 1,211,499 | 1,143,671 | 1,143,230 |
| Neolithic / modern n | 1,112 / 645 | 1,372 / 680 | 395 / 441 |
| Fixation definition | <10% to >90% | to exactly 100% (or 0%) in modern sample | same |
| Completions from start <50% | 0 | 0 | 0 |
| Completions from 50-90% start | not reported | 1 (rs10917702, 77.9% to 100%) | 3 (69.2%, 80.9%, 88.5% to 100%) |
| Newly 100% (almost all from 90-99%) | not reported | 17,806 | 3,469 |

Version changes: the claim moved from "zero" (blog) to "1 and 3" (Zenodo) with a different SNP filter (minimum 100 genotyped samples per period), different sample sizes (the paper attributes the v62/v66 difference to annotation-file format) and a different fixation criterion. No overlap exists between the v62 and v66 anomalous loci (Z23046531 §3.5). A third, earlier aDNA fixation paper (Z18525185, Feb 2026) reports 22,428 fixed alleles on 8,738 samples; see C6.

derived: 350 x 0.45 = 157.5, matching the blog's "approximately 158 real generations" (holds).
derived: Day's modern-synthesis expectation = 20,000,000 / 9,000,000 y = 2.22 fixations/y; x 7,000 y = 15,556, matching "approximately 15,500" (holds). This is a genome-wide, new-mutation substitution count; the panel is 1,143,671 / 3.1e9 = 0.037% of the genome (derived; genome size from MC-05/CSAC2005 order of magnitude, not a repo parameter). Scaling the 15,556 by that fraction gives 5.7 expected panel-site events (derived), versus the observed 0-3; see C1 and C6.

## Assumptions
- Stated: "The fixation events reported here are regional fixation events within the European subpopulation, not species-wide fixation events." Admixture "would be expected to introduce apparent frequency changes from intermediate starting values; the observed pattern is therefore conservative with respect to admixture" (Z23046531 §1).
- Implicit: (i) counts of frequency completions at panel SNPs measure the same thing as the "~20 million fixations" of the MITTENS required count (new substitutions along a lineage versus frequency changes in standing variation; see C1); (ii) the Neolithic sample is ancestral to the modern sample (Z23046531 §1 itself cites steppe admixture, and Z18525185 §5.1 cites Anatolian replacement); (iii) "100% in a sample of 441-680 diploids" equals fixation in the population (sampling noise is not modelled); (iv) d = 0.45 (C2) applies to this window.

## Responses
- Against: keruru (C5): zero is the neutral expectation for this window (Ne ~1e4), so the data cannot discriminate. 1240k ascertainment (C1).
- In support: none independent found. Day's own reply to keruru is C5a.
- Weaknesses in the responses: C5's number rests on Ne ~ 10,000 (Day's circularity objection, C5a; keruru's own temporal-method Ne in C5b is a partial answer). C1 is an analyst-raised point with no published critic; its direction of bias is contestable (C1a).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Mallick 2024 (AADR) | "We process these bams to produce genotypes at a set of about 1.23 million SNPs that have been assayed for nearly all published individuals with ancient DNA data." | accurate for the 1,233,013 SNP count Day quotes; the panel's design is the issue (C1) |
| Mathieson 2015 (panel) | "The targeted sites include nearly all SNPs on the Affymetrix Human Origins and Illumina 610-Quad arrays, 49,711 SNPs on chromosome X and 32,681 on chromosome Y, and 47,384 SNPs with evidence of functional importance." | see C1 |

## Pre-registered prediction
Written before any check runs.
- Under the claimant's model: with effective generations 157.5, fewer than 20 genome-wide completions and zero from intermediate frequency; observed 0 (blog), 1 and 3 (Z23046531) are described as confirming. Day's modern-synthesis comparator is 15,556 genome-wide, with no panel scaling shown.
- Under the opposing model (neutral drift, Ne of order 1e4, 350 generations): expected completions from a 50-90% start are effectively zero (keruru: ~1e-29 across a million loci from intermediate frequency), so 0 is expected and 1 or 3 are anomalies attributable to sampling noise or admixture, not to a rate. Both models therefore predict ~0 for the headline statistic.
- Result that would change a verdict: a forward Wright-Fisher run (scaling validated first, per README rule 6) with a panel-like start-frequency spectrum in which the neutral expected count of 50-90% completions is clearly distinguishable from the d = 0.45 expectation; or evidence that the 1 and 3 observed loci are produced by sampling noise at n = 441-680.

## Check
Script: none yet (spec: `research/checks/c_adna_neutral_expectation.py`, planned). Spec: forward Wright-Fisher, N in {1e4, 2e3}, 350 and 157 generations, start frequencies drawn from the Z23046531 Neolithic-bin spectrum, sample n = 441 / 680 diploids at both ends, count loci at 100%; report the expected count by start band. Validate scaling against an unscaled run first. · Result: not run · Review: pending

## Simulator variables implied
Nominal generations in window, d, Ne (time series), start-frequency spectrum, sample size per period, fixation criterion (population vs sample), admixture fraction, panel ascertainment rule.
