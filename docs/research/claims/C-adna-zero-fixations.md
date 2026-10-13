---
id: C
title: "European aDNA shows ~zero fixations from intermediate frequency across ~1.1-1.2M SNPs in ~7,000 years (blog: 0 of 1,211,499; Zenodo: 1 and 3 of 1,143,671)"
side: day
branch: C
parent: ROOT
edges: [{type: supports, target: ROOT}, {type: depends-on, target: C2}, {type: depends-on, target: C4}, {type: attacks, target: C5}]
load_bearing: false  # ROOT does not rest on C: the MITTENS rate argument (A) and the neutral-theory argument (B) are computed without it. C is offered as empirical confirmation of d (C2) and of "evolution is inoperative" and is cited as such, so a failed C weakens only that supporting leg.
sourcing: firsthand
status: reviewed
verdicts:
  internal: "non-sequitur"   # neutral also predicts ~0 from <50% and 0.04-0.11 from 50-90%
  fidelity: n/a
  external: "contested"   # reading-dependent: contested under R-c (the source states no s: zero excludes the 15,556 required rate only if its sweeps had s >= s*; s* = 0.03 to 0.05 on the blog statistic B10, 0.05 on Z50, 0.1 on Z10); contradicted (scoped: the inference from zero to a refuted required rate fails for s <= 1e-2) under R-a (s = 1e-3, Q44, another post) and R-b; supported (scoped) under the extended reading R-d (s >= 0.05), which no source gives; observation not in question; Readings table in the R4 L5 paragraph (R4 L5, integrated 2026-10-13, reviews #80). Other notes: observed 1 and 3 mildly above neutral at Ne 1e4, equal at Ne ~7k; admixture not modelled; R4 C1c/C1d do not address this intermediate-start statistic (their 21-class events start at >=95%); C1d reproduces the completions in kind (2 and 0 from Neolithic MAF >=10% vs Day's 1 and 3), with his event total 3.6x below the reproduction
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


RH tag (2026-10-10 pass): dialectic (stated as a checkable claim or derivation; no rhetorical device scored).
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

**Correction (2026-10-13, R4 L5 review C-D5; the figure above is kept as first written):** the "5.7 expected panel-site events" is an error of the audit's, from uniform scaling. In the L5 model the swept standing-variant site is on the panel in 8.8% to 24.7% of completions (hard mode at s <= 0.01: 0.5% to 6.5%), so at 15,556 completions 1,376 to 3,836 swept sites sit on the panel (hard mode at s <= 0.01: 76 to 1,010), about two orders more than 5.7. The error overstated what the panel hides. Logged in `ledgers/slips.md` (S-L5-1).

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
R4 C1d (research/checks/results/R4-C1d.md §3.6, review #10): Day's documented two-period pipeline (Z23046531) was run on the real genotypes. Sample (1,377 Neolithic / 683 modern vs his 1,372 / 680) and tested SNP count (1,143,870 vs 1,143,671) reproduce; completions from Neolithic MAF >= 10% reproduce in kind (2 on v62, 0 on v66; Day 1 and 3); the event total does not (63,631 vs 17,814). The 21-statistic results (C1c, C1d) concern alleles already near fixation and do not by themselves change this claim's verdicts.

R4 C1 (`c1_ascertainment_sim.py`, exact WF chain; research/checks/results/R4-B3b-C1.md): this is Z23046531's two-period statistic (not the Z18525185 21-count, see C6/C1b). Under neutrality at Ne = 1e4 the expected events from <50% are ~0 and from 50-90% are 0.04 (v62) / 0.11 (v66); new-in-window mutations fixing inside 280 generations: 5e-151 per site. So the headline does not discriminate. Observed 1 and 3 are above the Ne = 1e4 expectation (P(>=3 | 0.11) = 2e-4; critic reading: faster than neutral, not a stopped clock) and equal expectation at Ne ~ 7,000; the tail is extremely Ne-sensitive and Ne = 1e4 is an unverified input (Day-side reading). Admixture not modelled. Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)
Earlier note: Script: none yet (spec: `research/checks/c_adna_neutral_expectation.py`, planned). Spec: forward Wright-Fisher, N in {1e4, 2e3}, 350 and 157 generations, start frequencies drawn from the Z23046531 Neolithic-bin spectrum, sample n = 441 / 680 diploids at both ends, count loci at 100%; report the expected count by start band. Validate scaling against an unscaled run first. · Result: not run · Review: pending

R4 C1e (research/checks/results/R4-C1e.md; 2026-10-09): does not address this intermediate-start statistic; see C6 for the 21. Verdicts unchanged.

R4 L5 (research/checks/results/R4-L5.md; pre-registered 0e6da82, pre-run notes 5e64f0a, fix pass 0b0431c; combined review #80 `REVIEW-R4-L5-combined.md`; integrated 2026-10-13). Power analysis of Day's zero-reported statistics at his required rate (comparator "approximately 15,500 fixations per 7,000-year period", Q275; inference "decisively favors the MITTENS prediction", Q276; framing Q277, Q278; the only beneficial s in his corpus is Q44's 1e-3, another post). Band CRITIC. **No verdict value moves; the registered field flip to `contradicted` is withheld** (the weak-test caveat of the pre-run notes, and reading R-c unresolved: the source states no s). **Readings of the inference from zero to a refuted rate (rule RD; all tags dialectic):**

| Reading | Status | What the 15,556 are | Expected count of the zero statistics (25 y) | External under this reading |
|---|---|---|---|---|
| R-a | plausible; s imported from Q44 (another post) | sweeps at s = 1e-3 | 0 in every cell, mode, design and statistic | `contradicted` (scoped): the inference fails; zero is what the required rate itself predicts. The observation stands |
| R-b | plausible | sweeps at any s <= 1e-2 (registered scope) | at most 5.9e-16 in any cell; E <= 1 by sweep-time arithmetic and a direct trajectory bound; descriptively the same at s = 0.02 | `contradicted` (scoped), as R-a |
| **R-c** | plausible; the literal state of the source; **sets the field** | sweeps of unstated s | crossover s* (hard / standing): B10 0.05 / 0.03 to 0.05; Z50 0.05 / 0.05; Z10 0.1 / 0.1 (Z columns understated at s >= 0.05) | **`contested`**: zero excludes the required rate only if its sweeps had s >= s* |
| R-d | extended (no source gives the 15,556 s >= 0.05; cannot set the field) | strong sweeps, s >= 0.05 | 286 to 3,924 (B10 medians); P(0) < 1e-69; assumes independent sweeps | `supported` (scoped) |
| R-e | plausible; the text's own derivation | total substitutions at the long-run rate | neutral model: 0 | unchanged; the existing internal `non-sequitur` |

The field takes R-c: under R-a, R-b and R-e the inference fails outright; under R-c it holds on a condition the source leaves open; R-d would make it true but is an extended reading. This is the count's +1 reading-dependent external verdict.

**Who this helps.** *Day:* the observation stands (every model reproduces the zero). The test could not have come out DAY at s <= 0.01 (the registered arithmetic excluded it), so "not DAY" carries no information against him. Two of his statistics (Z50, Z10) run low at s >= 0.05 because the hitchhiking formula understates monomorphy of linked SNPs in the modern sample (0.90 explicit against 8.5e-5 at 2N = 2,000; 0.48 against 1.2e-6 at 2N = 20,000), against Day on those statistics. The panel registers sweeps at s >= 0.05 (hundreds to thousands of events at the required rate), and his zero there excludes any rescue of the required rate by strong sweeps. *Critics:* at s <= 1e-2 (the registered scope; this includes Q44's 1e-3), the zero carries no information on the required rate; descriptively the same at s = 0.02, where the simulated expected count of his zero-reported statistics is still effectively 0 (at most 1e-6 in any 25-y cell, 0.044 in the 20-y cells; R4-L5 point 1; corrected 2026-10-13, MA-28 i) (the window is 280 generations; a sweep at s <= 0.01 takes about 1,000); the mainstream model predicts about zero (at most 4.7e-31 at 25 y; 4.75e-18 at 100 times the rate and 20 y); no simulated completion at s <= 0.02 began below 50% at 7,500 BP. *Both / the audit's own errors:* two launch bugs (fixed pre-run), the P7 registration inconsistency (ST-09), the V3 bias direction stated wrongly before the run and withdrawn after the review (reproduced post hoc: 0.0093 against 0.0083), the "5.7" figure above, the "more than 15 orders of magnitude" printed as a margin, six of eight predictions missed in part. Open: C1a's sign untested (no random-SNP comparator); D3 a partial sensitivity; which of B10 / Z50 / Z10 is primary (the band does not depend on it); sweeps at F = 15,556 and s >= 0.05 are not independent.

## Simulator variables implied
Nominal generations in window, d, Ne (time series), start-frequency spectrum, sample size per period, fixation criterion (population vs sample), admixture fraction, panel ascertainment rule.
