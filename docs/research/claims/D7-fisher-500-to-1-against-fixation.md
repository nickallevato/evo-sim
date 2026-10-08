---
id: D7
title: "Fisher: a mutation with a 0.1% benefit has 500 to 1 odds against surviving; only 1 in 500 takes over the population"
side: day
branch: D
parent: D
edges: [{type: supports, target: D7a}]
load_bearing: false  # this is a premise of the Spetner chain (D7a), not of ROOT; Day's MITTENS papers use Kimura's 2s separately
sourcing: secondhand
status: extracted
verdicts:
  internal: holds      # 2s for s = 0.001 is 1/500; exact Kimura value for N = 1e4 is 0.00200
  fidelity: partial      # the 2s formula is verified (Kimura 1962 p.716), but Kimura credits the approximation to Haldane (1927) and the general formula to Fisher (1930) and Wright (1931); Day's attribution to Fisher alone is unverified
  external: supported      # for large N, additive (genic) selection, new mutant in one copy; standard result
---

## Statement (verbatim)
> "Sir Ronald Fisher, a world expert on the mathematics of evolution, has shown that the odds of the survival of a single mutation with a survival benefit of 0.1% greater than the rest of the population is 500 to 1 against – because the majority of mutants are eradicated by random effects. In other words, only 1 in 500 mutants with a positive benefit of 0.1% will end up taking over the entire population."

Source: [Every Critique is Correct](https://voxday.net/2024/04/25/every-critique-is-correct/), 2024-04-25, voxday.net, para 2. `secondhand`: Day reproduces the argument from darwinsmaths.com (link in the post's first sentence) and from Spetner (named in the following paragraph); neither retrieved.

Primary check text:

> "For a positive s and very large N we obtain the known result that the probability of ultimate survival of an ad- vantageous mutant gene is approximately twice the selection coefficient (HAL- DANE 1927)."

Source: Kimura, Genetics 47:713, 1962, p.716 (user-downloaded copy; `sources/raw/sources/manual/Kimura1962.txt`).

## Formal statement
P_fix = 2s for small s and large N (Haldane 1927, via Kimura 1962); Kimura's diffusion value: u(p) = (1 - e^(-4Nsp))/(1 - e^(-4Ns)) with p = 1/(2N). For s = 0.001: 2s = 0.002 = 1/500, i.e. odds 499 to 1 against. Recomputed: for N = 10,000, u = (1 - e^-0.002)/(1 - e^-40) = 0.001998 (from `research/checks/wf.py kimura_u`; a 1.2e6-replicate simulation gave 0.00201). Reconciles.

## Assumptions
- Stated: s = 0.001; survival odds; 'the majority of mutants are eradicated by random effects'.
- Implicit: s is a mean benefit for a new mutant; N large; heterozygote advantage s (genic); one copy.

## Responses
- Against: none on the number. Dependence on s: Zeng 2021 (the cited source for 0.001 elsewhere, fidelity ledger) reports ~0.001 as a mean for negative selection.
- In support: Kimura 1962 p.716.
- Weaknesses: attribution; and the figure applies to a single new copy. Standing variation, soft sweeps and larger s change it (ROOT-M row 3).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura 1962 p.716 | 'probability of ultimate survival of an advantageous mutant gene is approximately twice the selection coefficient (HALDANE 1927)' | accurate for the formula; credits Haldane 1927, formula to Fisher 1930/Wright 1931 |
| Fisher 1930 | not retrieved | unverified |

## Pre-registered prediction
Written before the computation. Prediction (Day): 1/500. Prediction (standard theory): 2s = 1/500; Kimura u within 1% of 2s at N = 1e4, s = 1e-3. Result that would change a verdict: Kimura u deviating from 2s by more than 5% at the stated parameters (it does not).

## Check
`python3 -I` with `research/checks/wf.py kimura_u(10000,0.001)` -> 0.001998 (reconciles with 2s = 0.002).

## Simulator variables implied
N, s, initial frequency 1/(2N), P_fix.
