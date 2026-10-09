---
id: C4
title: "Drift variance (hence Ne) varied 3.3-fold (pan-European) to 4.6-fold (Britain-Ireland) across the Holocene, so Ne cannot be treated as constant"
side: day
branch: C
parent: C
edges: [{type: supports, target: C}, {type: attacks, target: C5}]
load_bearing: false  # Supports the claim that a constant Ne = 10,000 should not be applied to the 7,000-year window; ROOT does not depend on it.
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: pending
  external: pending   # R4 C1d: keruru's windowed trajectory replicates (7.8k-10.5k across windows, trajectory shape held, P13), so the variation C4 claims is not contradicted; a sourced Holocene European N_e is a recorded retrieval gap (gaps.md, in progress)
---

## Statement (verbatim)
> "Drift variance, corrected for sampling error, varied 3.3-fold between Early Neolithic (maximum) and Medieval (minimum) periods in the pan-European dataset."

Source: [Temporal Variation in Effective Population Size Across the Holocene](https://zenodo.org/records/18320599), Z18320599, 2026-01-10, Abstract, ¶5 of docx text extraction.

> "The single-population analysis yielded a 4.6-fold variation in drift variance, indicating that the pan-European estimate was conservative."

Source: same, Abstract.

> "The absolute Nₑ values estimated from drift variance (ranging from approximately 0.3 to 1.4) are not interpretable as true effective population sizes."

Source: same, Limitations.

> "Effective population size varied by at least 3.3-fold, and likely more than 4-fold, across the European Holocene."

Source: same, Conclusion.

Day's later use (blog, 2026-08-27): "a drift-variance Nₑ near 2 rather than ten thousand" (see C5a).

## Formal statement
For adjacent 500-year bins, Var_drift = Var_obs - [p(1-p)/(2 n1) + p(1-p)/(2 n2)] (sampling correction; p the average frequency); the "Ne" proxy is inversely proportional to Var_drift. Pan-European: min 0.00150 (750-1250 BP), max 0.00495 (7250-7750 BP, n 442 to 153), ratio 3.30; recent bin 250-750 BP 0.00750 (5.01x min) flagged as an outlier from migration. Britain-Ireland: min 0.00330, max 0.01514 (n 14 to 15), ratio 4.59.

derived: 0.00495/0.00150 = 3.30 (holds); 0.01514/0.00330 = 4.59 (holds); 0.00750/0.00150 = 5.0 (holds).
Link to parameters.yaml: `population.Ne_modern_human` = 1.0e4 (textbook, unverified) is the value Day says should not be treated as constant. The paper gives no absolute Ne.

## Assumptions
- Stated: loci outside LCT, SLC24A5, SLC45A2, HERC2, HLA, EDAR, TLR1/6/10 are neutral; drift variance changes reflect Ne and not migration ("residual population structure and migration" are acknowledged).
- Implicit: that the variance of allele-frequency change between adjacent time bins, taken across samples from many sites and cultures, is a drift measure; the bins' earliest samples are n = 14-15 (Britain) and 153 (pan-European); the drift-variance ratio converts proportionally to an Ne ratio (it does not if migration or structure change across bins). The paper itself says the 5-fold recent outlier "likely reflects post-Medieval migration events ... introducing population structure rather than drift", which is the same artefact class at lower magnitude.

## Responses
- Against: keruru's temporal-method Ne (C5b) gets 8,139 (102 generations) and 9,835 (250 generations) using a similar approach, and finds drift slowing as the population grew, which agrees in direction with this paper's falling drift variance.
- In support: keruru agrees Ne varied over the window ("effective size roughly doubles from the Neolithic to the present"); the paper's own title claim is thus not disputed in direction.
- Weaknesses in the responses: no one disputes that Ne varied; the disagreement is about magnitude and about what an Ne of order 1e4 versus ~2 means (C5a).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura 1983 / Crow & Kimura 1970 (cited in the Introduction for "probability of fixation ... is 1/(2N_e)") | the paper writes "The probability of fixation for a neutral allele is 1/(2N_{e})" | misread: Kimura 1962 p.716 applies the formula "by putting p = 1/(2N)" and obtains "U = 1/2N" for a neutral gene (fidelity ledger, B3/B7) |
| Takahata 1993; Harpending 1998 | long-term human Ne approximately 10,000, "reflects the harmonic mean" | not retrieved |

## Pre-registered prediction
- Under the claimant's model: bin-to-bin drift variance varies at least 3x across the Holocene, not explained by sampling error; Ne proxy varies by the inverse.
- Under the opposing model: variation of this size is produced by migration, admixture and sampling heterogeneity (changing cohort composition across bins) alone. For scale: at constant Ne = 1e4 and 20 generations per 500-year bin (25 y/gen), a locus with p(1-p) near 0.2 has expected drift variance 20 x 0.2/(2 x 1e4) = 2e-4 per bin pair, which is about 7x below the paper's minimum (0.0015) and 25x below its maximum (0.00495) (derived; the paper's averaging and its MAF > 0.05 filter are not fully specified, so this is a rough comparison). The absolute level therefore also points to extra variance from structure or admixture, or to a smaller Ne, and the repo does not yet distinguish these.
- Result that would change a verdict: a simulation with constant Ne = 1e4, sample sizes matching each bin, and the Britain/pan-European admixture history reproduces a 3-5x range of apparent drift variance (verdict: artefact) or does not (verdict: real variation, magnitude pending).

## Check
R4 C1c/C1d (research/checks/results/R4-C1c.md §2; research/checks/results/R4-C1d.md §4): the Holocene N_e trajectory is the load-bearing, unsourced input to the C1c reading of Day's 21 (deficit at N_e <= ~5e4; neutral-compatible at closed N_e >= ~1e5 or growth to 1e5-1e6). C1d's temporal estimates (lower bounds on drift N_e) are 6.4k-10.5k by window and release; within-region BA-to-Medieval values 3.4k-7.2k (Scandinavia 14.6k). A literature retrieval of IBD and aDNA demographic estimates is in progress (gaps.md).

Script: none yet (spec: `research/checks/c4_drift_variance_null.py`, planned): simulate bins with Ne constant at 1e4 and with the paper's reported n per bin; add a migration pulse of 10-50% in a Bronze-Age bin; estimate Var_drift with Day's correction; report the ratio. · Result: not run · Review: pending

## Simulator variables implied
Ne(t), sample size per bin, migration pulses, bin width, sampling-variance correction.
