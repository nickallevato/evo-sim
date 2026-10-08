---
id: B7c
title: "keruru (former ally): supply is 2N mu with census N; fixation probability is exactly 1/(2N_census); claim withdrawn"
side: ally
branch: B
parent: B7
edges: [{type: attacks, target: B3a}, {type: supports, target: B7}]
load_bearing: false  # corroborated by Day's own concession (B3g)
sourcing: firsthand
status: reviewed
verdicts:
  internal: holds
  fidelity: accurate
  external: supported
---

## Statement (verbatim)
> Mutation supply is 2Nμ with N the census count — mutations occur in gametes, and every reproducing individual contributes gametes.

Source: [keruru, "The Epicycle Was Elsewhere"](https://claudekeruru.substack.com/p/the-epicycle-was-elsewhere), 2026-08-26, para 6

> The fixation probability of a single new mutant in both chains: exactly 1/(2N_census), to fifteen decimal places.

Source: [keruru, "The Epicycle Was Elsewhere"](https://claudekeruru.substack.com/p/the-epicycle-was-elsewhere), 2026-08-26, para 9

> The claim about the substitution rate is withdrawn. The claim about the ancient-DNA finding is withdrawn.

Source: [keruru, "The Epicycle Was Elsewhere"](https://claudekeruru.substack.com/p/the-epicycle-was-elsewhere), 2026-08-26, para 36

> k = 2Nμ × 1/(2Ne) = (N/Ne)μ

Source: [keruru, "The broken evolutionary math."](https://claudekeruru.substack.com/p/the-broken-evolutionary-math), 2026-02-04, para 28 (the pre-retraction statement, in a post that is "mainly claude" per the author)

## Formal statement
Exact finite Markov chains (Wright–Fisher and a sweepstakes model with Nₑ 5.6× lower at the same census): P_fix = 1/(2N_census) to 15 decimals; code deposited per the author (not retrieved). Martingale argument: neutral frequency is a bounded martingale, so P_fix = p₀. Consistent with `research/checks/b3_N_vs_Ne.py` (RESULTS B3). Second leg (aDNA zero fixations expected under neutrality, ≈10⁻²⁹ expected fixations, Nₑ ≈ 10⁴) is branch C; Day contests it as circular (B3h).

## Assumptions
- Stated: Census N cancels; Nₑ never enters.
- Implicit: Exchangeable offspring law in the chains (Day: sweepstakes parent drawn uniformly at random, setting a covariance to zero).

## Responses
- Against: "And most crucially, his work never contains a census population." ([Day, "The Response to the Retraction" (blog)](https://voxday.net/2026/08/27/the-response-to-the-retraction/), 2026-08-27, Day, 2026-08-27 (on keruru's aDNA leg)); Day (B3h).
- In support: Day concedes the algebra (B3g); B3 check.
- Weaknesses in the responses: LLM-assisted author; the January review (KR-08/KR-09) endorsed the thesis from an LLM transcript and is superseded by this post; chains and code were not retrieved.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura 1962 | U = 1/2N | verified |

## Pre-registered prediction
Pre-registered prediction (copied from RESULTS B3; the check has run).
- Under the claimant's model: (keruru, B3) P_fix = 1/M for every Nₑ.
- Under the opposing model: (Day, Feb) P_fix = 1/(2Nₑ).
- Result that would change a verdict: Obtaining and re-running keruru's chains with a covariance between breeding and carrying.

## Check
Script: `research/checks/b3_N_vs_Ne.py` · Result: see B7. Chains: not retrieved.

## Simulator variables implied
- sweepstakes events
- Nₑ via reproductive skew
