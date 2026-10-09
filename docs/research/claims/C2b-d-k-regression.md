---
id: C2b
title: "Across six countries 1950-2023, d and k are linearly related (d = -2.242k + 1.229, r = -0.991); the k = mu identity never applies and selection is ending"
side: day
branch: C
parent: C2
edges: [{type: supports, target: C2}, {type: supports, target: B3}]
load_bearing: false  # Used to extend d to modern demography and to argue k < mu; MITTENS 3.0 and the main rate argument (A) do not use it.
sourcing: firsthand
status: extracted
verdicts:
  internal: non-sequitur
  fidelity: unverifiable   # R4 X1 rule rev 2 (was n/a): rule F (uncited/unretrievable input) or S/U; see R4-X1-rescore.md
  external: pending
---

## Statement (verbatim)
> "This is a near-perfect linear relationship: d = −2.242k + 1.229."

Source: [The Significance of (d) and (k)](https://voxday.net/2026/02/09/the-significance-of-d-and-k/), B2026-02-09-the-significance-of-d-and-k, posted 2026-02-09, ¶6 of extracted text. Context: the analysis was run by "A doctor who has been following the Probability Zero project" (¶2); the data and fit are secondhand through Day, the interpretation is Day's.

> "The Pearson correlation is r = −0.991 with R² = 0.981, p < 0.001."

Source: same post, ¶6.

> "A beneficial allele with a selection coefficient of s = 0.01—which would be considered strong selection by population genetics standards—would change frequency by Δp ≈ d × s × p(1−p). At d = 0.08 and initial frequency p = 0.01, that works out to a frequency change of approximately 0.000008 per generation."

Source: same post, ¶10.

> "The data show that k in humans has been approximately 0.5μ or less throughout the entire modern period for which we have reliable demographic data"

Source: same post, ¶9 (Q42).

> "while it applies with increasing accuracy the further back you go, it never actually reaches k = μ even under pre-agricultural conditions, since d never reaches 1.0 for any human population."

Source: same post, ¶9 of extracted text (added 2026-10-09 under R4 X1 rule S1: this is the sentence the internal verdict rests on). The regression itself was run by an unidentified "doctor" (¶2); under rule U only Day's interpretation is scored.

## Formal statement
Regression: d = a k + b with a = -2.242, b = 1.229 (k in units of mu: "k converges toward half the mutation rate", ¶5). d from life-table/TFR schedules per country-year (C2a); k from the Z18525262 formula applied to census data (parameters.yaml `rates.day_k_over_mu_0_743` is the 1950-2025 four-generation case).

derived (python3, R2 recompute):
- k = 0 gives d = 1.229 (> 1, outside d in (0,1] as defined in C2a).
- d = 1 (the discrete-generation case, where the post says Kimura's k = mu holds) gives k = (1.229 - 1)/2.242 = 0.102 mu, not mu.
- d = 0 gives k = 0.548 mu; d = 0.45 gives k = 0.347 mu; k = mu gives d = -1.013 (negative).
- k = 0.5 mu (the "ceiling") gives d = 0.108.
- Delta-p example: 0.08 x 0.01 x 0.01 x 0.99 = 7.92e-6, matching "approximately 0.000008" (holds).
- "On the order of a million years": at constant Delta-p = 7.92e-6 per generation, going from p = 0.01 to 0.99 takes 0.99/7.92e-6 = 125,000 generations = 3.1M y at 25 y; with logistic growth at rate d s = 0.0008 the 1%-to-99% time is 2 ln(99)/0.0008 = 11,488 generations = 0.29M y. The post's figure sits between the two readings; neither form is shown.
- The post then calls one million years "roughly two hundred times longer than the entire history of anatomically modern Homo sapiens". 1,000,000/200 = 5,000 y. The age of anatomically modern humans is not a repo parameter (external figure, about 3e5 y, which would give a ratio of about 3); the 200x does not reproduce under that figure.

## Assumptions
- Stated: d falls as TFR falls (r = 0.942 with TFR); k computed from the "overlap-corrected" rule.
- Implicit: that the correlation across 6 countries x 4 time points (24 points) between two quantities computed from the same demographic series is evidence about genetic substitution (it is a relation between two demographic transforms); that the linear form extends outside 1950-2023; that k here is a computed index, not a measured substitution rate.

## Responses
- Against: none found in the critic corpus (not engaged).
- In support: none.
- Weaknesses in the responses: not yet engaged by any critic; the repo's derived points above are the only scrutiny.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Balloux & Lehmann 2012 (k < mu with overlap) | "we show that the substitution rate at neutral genes does depend on population size fluctuations in the presence of overlapping generations" | partial: needs overlap plus fluctuating size; paper gives k = mu(1 - s) for constant survival s and contains no 0.743, 0.5 or 32.3 (fidelity ledger) |
| Kimura & Ohta 1971 / Kimura 1983 | k = mu | accurate as the textbook identity (quoted in Balloux & Lehmann Introduction) |

## Pre-registered prediction
- Under the claimant's model: any demographic transition series with falling TFR gives a linear d-k relation of slope near -2.2 and intercept 1.2.
- Under the opposing model: d and k are both monotone functions of time-ordered demographic variables, so any two such series correlate near |r| = 1 without implying a causal relation; extrapolating the line to the d = 1 end gives k = 0.10 mu, which conflicts with the post's own statement that the identity holds "with increasing accuracy the further back you go".
- Result that would change a verdict: a published data file for the 24 points (not located) that reproduces the fit and shows the fit is not an artefact of shared time-dependence; or a corrected intercept consistent with k = mu at d = 1.

## Check
Script: none yet (spec: recompute the 24 (d, k) pairs from published life tables and census series per Z18525262 eq. 3 once the "doctor's" inputs are obtained; fit; test the d = 1 intercept; compare with a shuffled-year null). · Result: not run · Review: pending

R4 X1 (research/checks/results/R4-X1-rescore.md; rule research/checks/results/R4-X1-verdict-rule.md rev 2; review #12, 2026-10-09): under the single both-sides rule this node is non-sequitur / unverifiable. N2a/N2b: own regression gives k = 0.10 mu at d = 1 and k = mu at d < 0, while para 9 says k = mu 'applies with increasing accuracy the further back you go'. S1 gap: that sentence is not in the Statement; the claim file should add the para 9 quote. U: the regression was run by an unidentified 'doctor'; only Day's interpretation is scored Charitable reading tried: tried reading 'increasing accuracy' as the regression's own d to 1 direction: contradicts the fit (k falls as d rises).

## Simulator variables implied
d(t), N(t) census series, k/mu as an output index.
