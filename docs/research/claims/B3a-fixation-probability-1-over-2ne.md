---
id: B3a
title: "k = 2N mu × 1/(2Ne) = mu N/Ne: supply uses census N, fixation probability uses Ne"
side: day
branch: B
parent: B3
edges: [{type: supports, target: B3}]
load_bearing: true  # the N/Nₑ leg of B3 and of the recalibration (B4) rests on it; withdrawn by Day 2026-08-27 (B3g)
sourcing: firsthand
status: reviewed
verdicts:
  internal: holds
  fidelity: misread
  external: contradicted
---

## Statement (verbatim)
> k = 2Nμ × 1/(2N_{e}) = μ × (N/N_{e}) (1)

Source: [Z18525547, The N/N_e Distinction and the Recalibration of the Human-Chimpanzee Divergence (Day & Athos)](https://zenodo.org/records/18525547), Zenodo 2026-02-08 (v1), ¶10 of extracted text

> This cancellation is invalid. The mutation supply term uses census N (every individual can mutate), while the fixation probability is governed by effective population size N_{e} (drift operates on N_{e}, not N).

Source: [Z18525547, The N/N_e Distinction and the Recalibration of the Human-Chimpanzee Divergence (Day & Athos)](https://zenodo.org/records/18525547), Zenodo 2026-02-08 (v1), ¶4 of extracted text. abstract

> k = 2Nμ × 1/(2Nₑ) = μ(N/Nₑ)

Source: [Day, "Response to Dennis McCarthy, Round 2" (blog)](https://voxday.net/2026/02/04/response-to-dennis-mccarthy-round-2/), 2026-02-04, ¶29 of extracted text

## Formal statement
Day: k = (2Nμ)·P_fix with P_fix = 1/(2Nₑ) ⇒ k/μ = N/Nₑ.
Critics/literature: P_fix = p₀ = 1/(2N) (initial frequency; martingale property) ⇒ k/μ = 1 for any N, Nₑ.

Glossary: N = census diploids; Nₑ = effective size (variance); neutral P_fix = starting frequency, Nₑ governs the timescale (glossary).
**Internal consistency:** Day's own Z22129121 (2026-08-27) states "the neutral fixation probability exactly 1/(2N)" and "Every neutral mutation begins as a single copy in a single individual, at a frequency of 1/(2N)." (B7). The conclusion k = μN/Nₑ follows algebraically from its premise; the premise conflicts with Day's later texts and with Kimura 1962/1969 (B7a, B7b).
Empirical hint on direction: Keightley 2012 reports that pedigree μ ≈ 1.1e-8 is "about twofold lower than estimates based on the human-chimp divergence" (k > μ by ~2, far from 15–800,000; generation-time and calibration issues not separated).

## Assumptions
- Stated: "The mutation supply term uses census N (every individual can mutate), while the fixation probability is governed by effective population size N_{e}".
- Implicit: A new mutant's fixation probability depends on Nₑ rather than on its starting frequency. In an exchangeable model P_fix = p₀ exactly.

## Responses
- Against: "The fixation probability of a single new mutant in both chains: exactly 1/(2N_census), to fifteen decimal places." ([keruru, "The Epicycle Was Elsewhere"](https://claudekeruru.substack.com/p/the-epicycle-was-elsewhere), 2026-08-26, para 9 (keruru; exact Markov chains incl. a sweepstakes model; code not retrieved))
  "50,000 x 9 million = 450 billion new mutations altogether." ([McCarthy, "Why Probability Zero is Wrong About Evolution" (free repost)](https://dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1), 2026-09-11 (original paid post 2026-01-26), para 50 (McCarthy)) (uses N = Nₑ)
- In support: Day (2026-04-30, Grok exchange, B3f): LLM concedes both propositions and computes 800,000μ from them. Hössjer's review uses 2Nμ × 1/(2N) = μ (rate dμ), i.e. does not adopt B3a.
- Weaknesses in the responses: keruru's chains were not retrieved; the sweepstakes parent is drawn uniformly at random (Day's objection: "his sweepstakes parent is drawn uniformly at random — setting the one parameter in dispute, the covariance between who breeds and what they carry, to zero by fiat", [The Response to the Retraction](https://voxday.net/2026/08/27/the-response-to-the-retraction/), 2026-08-27, ¶3; locator fixed 2026-10-08, previously "RESP"). Day repeats the covariance objection against Chalub on 2026-09-21 ("Where the Errors Hide", ¶10–12; B3g). The 2026-04-30 LLM exchange is not independent evidence (it derives 800,000μ from stipulated premises).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura 1962 | "The probability of fixation of an individual mutant gene is obtained from (8) by putting p = 1/(2N)." and "if we let s → 0 in (10), we obtain U = 1/2N, the result known for a neutral gene" (N = "the number of reproducing individuals") | verified-misread for 1/(2Nₑ) (ledger). Caution: the 1962 model has a single N serving as both counting and variance size, so it does not itself separate census from Nₑ |
| Kimura & Ohta 1969 | "the remaining minority (fraction 1/2N) spread over the entire population (i.e. reach fixation)" alongside Nₑ for the time | supports critics (ledger) |

## Pre-registered prediction
Pre-registered predictions (copied from RESULTS B3): P1 P_fix = 1/M for every Nₑ; P2 t_fix scales with Nₑ. Day's model predicts P_fix = 1/(2Nₑ).
- Under the claimant's model: (RESULTS B3, P1 as the critics' side) —
- Under the opposing model: P_fix = 1/(2N) = 1/M independent of Nₑ; t_fix ∝ Nₑ.
- Result that would change a verdict: A non-exchangeable neutral setting (B3b) in which the long-run neutral rate is not μ per generation would restore part of B3; a corrected P_fix = 1/(2Nₑ) in any exchangeable model would overturn the check.

## Check
Script: `research/checks/b3_N_vs_Ne.py` (seed 13) · Result: both predictions confirmed. M = 400, 10⁶ replicates. Nₑ = 200/160/100/40/19: P_fix = 0.00250/0.00252/0.00257/0.00248/0.00257 vs 1/(2N) = 0.00250; Day 1/(2Nₑ) = 0.00249/0.00312/0.00498/0.01235/0.02676; t_fix/Nₑ ≈ 3.95–4.07. Review #2: P_fix = 1/M is a theorem in this class (frequency is a martingale), so the run verifies the code; the verdict is provisional until B3b. Review: `research/checks/REVIEW.md#2026-10-07--correctness-review-2-sonnet-on-b0b3`

## Simulator variables implied
- Nₑ/N via offspring variance
- exchangeable vs non-exchangeable reproduction
- sweepstakes events

R4 P1 (research/checks/results/R4-P1.md): in an exchangeable low-N_e model P_fix = 1/(2N), not 1/(2N_e) (exact; machine-checked at M = 100, alpha = 0.25 and 1). The test does not cover non-exchangeable (fitness-linked) offspring variance (review MINOR-4); Day's own 2026-08-27 concession (B3g) is the stronger support. Verdicts unchanged.
