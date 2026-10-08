---
id: E4
title: "Relictation: when one family replaces more than ~10% of a population, t̄ = 4Ne breaks (up to +7% to +25% at 2N = 20-50); fixation probability stays 1/(2N)"
side: day
branch: E
parent: E
edges: [{type: depends-on, target: B3}, {type: depends-on, target: F}]
load_bearing: false  # Narrow, self-bounded regime (macroscopic family replacement, small N). Day's own abstract says "Below 10% replacement, the formula holds". It does not affect ROOT.
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: pending
  external: pending
---

## Statement (verbatim)
> "When that compression fails and a single family can replace more than ~10% of the population, the formula t̄ = 4Nₑ breaks in quantifiable ways. Below 10% replacement, the formula holds to within the few-percent finite-size offset of the Wright-Fisher chain itself, and the mechanism remains diffusive drift."

Source: [Relictation: A Third Evolutionary Mechanism](https://zenodo.org/records/23188201), Z23188201, 2026-10-06 (record modified 2026-10-07), Abstract (Q72 gives the first clause, p.1).

> "The fixation probability p = 1/(2N) is protected by the martingale property and holds exactly regardless of offspring distribution."

Source: Z23188201, Abstract.

> "Classified by cause, relictation is technically a form of non-diffusive drift, but it is produced by a very different and much faster process"

Source: Z23188201, Abstract.

> "The mechanism is not untheorized. It is under-applied."

Source: Z23188201, §1.

## Formal statement
Cannings jackpot model: each generation, with probability p_jackpot, one random individual survives and its offspring replace round(f x 2N) other gene copies; remaining copies reproduce deterministically. Exact (2N+1) x (2N+1) transition matrix; fixation probability from the linear system; conditional mean time from the Doob h-transform; Ne = variance effective size from the one-generation variance of frequency change.

Table (paper; ratio t̄/4Ne at 2N = 20 / 30 / 50): f = 5%: 0.950 / 0.983 / 0.993; 10%: 0.968 / 0.999 / 1.033; 20%: 1.003 / 1.048 / 1.100; 30%: 1.035 / 1.091 / 1.160; 50%: 1.071 / 1.146 / 1.239; 60%: 1.068 / 1.148 / 1.249; 80%: 0.976 / 1.060 / 1.173; 90%: 0.950 / 0.966 / 1.023; 98%: 0.500 / 0.500 / 0.500. Plain Wright-Fisher baseline: 0.932 / 0.952 / 0.970.

derived: peak ratio over WF baseline = 1.071/0.932 = 1.149, 1.146/0.952 = 1.204, 1.249/0.970 = 1.288 (paper: "~15%, ~21%, and ~29%"; holds). Peak excess over 1.0: 7.1%, 14.6%, 24.9% (paper "~7% ... ~15% ... ~25%"; holds). The 98% row is 0.5 (complete replacement: one event takes half of 4Ne).
Link to repo checks: B3 (RESULTS.md) found P_fix = 1/M and t_fix/Ne of 3.95-4.07 for exchangeable Cannings models with offspring variance up to 10.7 at M = 400. That model had no macroscopic family replacement; it neither supports nor contradicts the relictation table, which is at 2N = 20-50 only.

## Assumptions
- Stated: population small enough that one family is a macroscopic fraction (a family of 6 in a population of 20 is 30%; "in a population of 20,000 is noise"); fixation probability protected by the martingale property.
- Implicit: that the trend "keeps growing with population size" (abstract) extrapolates from 2N = 20-50 to larger N at constant replacement fraction f; that realistic vertebrate bottlenecks have f above 10% in several consecutive generations; that the Scandinavian wolf (Viluma 2022) haplotype loss "consistent with relictation dynamics" is not equally explained by ordinary drift at tiny N.

## Responses
- Against: none located. The paper itself places the mechanism in the multiple-merger literature (Möhle & Sagitov 2001; Eldon & Wakeley 2006; Donnelly & Kurtz 1999; Pitman 1999; Schweinsberg 2000), so a critic would say the content is established theory applied to a regime; the paper agrees ("not a claim to have discovered a new force of nature").
- In support: the paper's own exact chain; the repo's B3 result on 1/(2N).
- Weaknesses in the responses: not engaged. Note for B3/B7: this paper states (as Day's own position, 2026-10-06) that p = 1/(2N) "holds exactly regardless of offspring distribution", which is the position the critics took against k = mu N/Ne (B7).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura & Ohta 1969 (t̄ = 4Ne) | "a single mutant gene, if it is selectively neutral, takes about 4Ne generations until fixation in a population of effective size Ne." | accurate (fidelity ledger) |
| Chalub 2022 (Gegenbauer expansion, martingale constraint) | "we consider a population of two types evolving without mutation or selection, the so-called neutral evolution" | verified-partial: math as stated; no mutation or selection (ledger) |
| Möhle & Sagitov 2001; Eldon & Wakeley 2006; Schweinsberg 2000 | multiple-merger coalescents | not retrieved |
| Viluma et al. 2022 (Scandinavian wolf) | "lost 10-24% of its founding haplotypes ... within five generations" per Day | not retrieved; unverified |

## Pre-registered prediction
Written before any check runs.
- Under the claimant's model: the exact-chain ratio t̄/4Ne at fixed f = 50% rises with N beyond 2N = 50 (about 1.24 at 50), reaching 1.3 or more at 2N = 100-200; the ratio at f = 5% stays within the WF baseline offset.
- Under the opposing model (diffusion/Kingman plus standard multiple-merger theory): at fixed f the ratio converges to a constant of order 1.2-1.3 and does not "keep growing"; at 2N >= 1,000 with realistic vertebrate variance, f is below 1% and the 4Ne formula holds.
- Result that would change a verdict: exact chains at 2N = 100, 200, 400 (sparse solver) show the ratio at f = 50% continuing to rise (supports "keeps growing") or flattening (does not).

## Check
Script: none yet (spec: `research/checks/e4_relictation_chain.py`, planned; reproduce the table at 2N = 20 / 30 / 50 first, then extend to 2N = 100-400; seedless, exact). · Result: not run · Review: pending

## Simulator variables implied
Replacement fraction f, jackpot probability, population size 2N, Ne from frequency-change variance, haplotype-block structure.
