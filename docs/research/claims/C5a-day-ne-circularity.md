---
id: C5a
title: "Day: Ne = 10,000 comes from theta = 4 Ne mu, which presupposes k = mu; the drift-variance Ne near 2 shows the aDNA signal is a population turnover"
side: day
branch: C
parent: C5
edges: [{type: attacks, target: C5}, {type: depends-on, target: C4}]
load_bearing: false  # Defends C against C5. If it fails, C is not discriminating but ROOT is unaffected.
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: n/a
  external: pending
---

## Statement (verbatim)
> "The arithmetic holds given one number: Nₑ ≈ 10,000 — which comes from θ = 4Nₑμ, which presupposes k = μ, the identity under test."

Source: [The Response to the Retraction](https://voxday.net/2026/08/27/the-response-to-the-retraction/), B2026-08-27-the-response-to-the-retraction, posted 2026-08-27, para 3.

> "As it happens, I ran it while writing the first edition of PZ: the Allen Ancient DNA Resource, 1,372 Neolithic against 680 modern Europeans, has rs35619459 moving 29.3% → 91.3%, a twelve-sigma excursion against his own stated expectation, and a drift-variance Nₑ near 2 rather than ten thousand."

Source: same post, para 4.

> "He has retracted an empirical falsification of the clock by feeding in a parameter that the clock manufactures"

Source: same post, para 3 (same paragraph as the first quote). Also quoted by keruru in [Kimura and the Red Flock](https://claudekeruru.substack.com/p/kimura-and-the-red-flock), 2026-08-31, para 5 (KR-06, tagged `secondhand` there); the firsthand source is the blog post.

## Formal statement
Claim 1 (circularity): Ne is estimated from heterozygosity theta = 4 Ne mu; the clock requires k = mu; therefore Ne from theta presupposes the clock. Formally, theta = 4 Ne mu uses the per-generation mutation rate mu, not the substitution rate. Whether the estimate presupposes k = mu depends on the source of mu:
- pedigree mu (parameters.yaml `mutation.mu_per_site_per_gen.pedigree_human` = 1.2e-8, Kong 2012): a direct count of new mutations in trios, independent of k = mu;
- phylogenetic mu (divergence divided by a fossil date): the Keightley 2012 abstract says the direct pedigree value "is about twofold lower than estimates based on the human-chimp divergence", i.e. the two sources differ by a factor of about 2 (this would change Ne by about 2x, not by a factor of 5,000).

Claim 2 (excursion): locus rs35619459 moves from 29.3% to 91.3% between a Neolithic sample (n = 1,372) and a modern sample (n = 680).
derived: change = 0.620. keruru's stated drift SD over 240 generations at p = 0.5 is about 0.05, so 0.620/0.05 = 12.4 "sigma" (holds as arithmetic; with the exact SD 0.0548 it is 11.3). Sampling error alone at these n: sqrt(0.293 x 0.707/2,744 + 0.913 x 0.087/1,360) = 0.0116, i.e. 54 SE; so the locus moved by far more than chance sampling.
Claim 3: a drift-variance Ne near 2. Z18320599's own Limitations section says the absolute Ne values from drift variance (0.3 to 1.4) "are not interpretable as true effective population sizes".

## Assumptions
- Stated: the 12-sigma is computed against keruru's expectation; the signal "is the size of a population turnover".
- Implicit: a single locus is an outlier of a drift distribution (a genome-wide scan of 1.14M loci would yield some extreme single-locus excursions even under drift: Bonferroni scale roughly 1e6 tests; at 12 sigma this is still extreme, but linkage correlation and admixture are not modelled; keruru's own note says per-SNP significance assuming independence is "unreliable" because loci sit in linkage blocks); that the Ne near 2 is a population-level quantity (Day's earlier paper says it is not).

## Responses
- Against: keruru's later temporal-method result (C5b) of Ne = 8,139 (102 generations) and 9,835 (250 generations) obtained "No mutation rate. No coalescent. No substitution identity", offered as the answer to this circularity charge.
- In support: Day's own C4 drift-variance data, in which the Ne proxy varied 3.3-4.6x.
- Weaknesses in the responses: C5b assumes a closed population (Day's own Z23046531 §1 and Z18525185 §5.1 describe replacement of Neolithic by later ancestry), so a temporal-method Ne across a replacement window is not an Ne of a single population.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Keightley 2012 (mu source) | "Direct estimates from genome sequencing of relatives suggest that μ is about 1.1 × 10(-8), which is about twofold lower than estimates based on the human-chimp divergence." | accurate (abstract; full text now in `sources/raw/sources/manual/Keightley2012.txt`); the ledger marks it partial pending the numeric check |
| Charlesworth 2009 (the circularity "flagged ... in 2009", per Day) | not quoted by Day | not retrieved; unverified |

## Pre-registered prediction
- Under the claimant's model: heterozygosity-derived Ne depends on the phylogenetic mu, so Ne = pi/(4 mu) shifts with the calibration; the aDNA drift variance gives Ne of order unity, so the neutral expectation of C5 fails.
- Under the opposing model: pedigree mu gives Ne of order 1e4 independent of k = mu, and drift variance in the aDNA series is dominated by admixture and structure, not by Ne.
- Result that would change a verdict: Ne(theta; pedigree mu) versus Ne(theta; phylogenetic mu) differing by about 2x only (the Keightley numbers) would show the circularity is a factor of 2, not a refutation; a forward simulation with an admixture pulse reproducing a 29% to 91% excursion at some locus among 1.14M under Ne = 1e4 would show that the single-locus excursion is explicable without Ne near 2.

## Check
Script: none yet (spec: part of `research/checks/c4_drift_variance_null.py`; add a genome-wide max-excursion statistic and admixture pulse). · Result: not run · Review: pending

## Simulator variables implied
mu source (pedigree versus phylogenetic), Ne estimator, admixture pulse, number of loci scanned, linkage blocks.
