---
id: C5
title: "Zero fixations in 240 generations is the neutral prediction (expected count ~1e-29 across a million intermediate-frequency loci), so the aDNA window cannot discriminate"
side: critic
branch: C
parent: C
edges: [{type: attacks, target: C}, {type: depends-on, target: C5b}]
load_bearing: false  # Removes C as discriminating evidence. Does not touch ROOT's A and B branches. The author withdrew it on circularity grounds (C5a), so its standing is disputed.
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: pending
  external: pending
---

## Statement (verbatim)
> "Integrated across a million loci starting from intermediate frequencies, the expected number of fixations is somewhere near 10⁻²⁹."

Source: keruru, [The Epicycle Was Elsewhere](https://claudekeruru.substack.com/p/the-epicycle-was-elsewhere), 2026-08-26, para 14 (KR-03 in `sources/quotes-critics.md`). Author status: formerly built on Day (Feb 2026), self-retraction in this same post.

> "Finding zero is not a coin landing on its edge. Finding one would have been the falsification."

Source: same post, section "Zero fixations was the prediction".

> "The claim about the substitution rate is withdrawn. The claim about the ancient-DNA finding is withdrawn."

Source: same post, para 36 (KR-04). Context: the withdrawal is explained as the author's own prior adoption of an invalid objection, not as concession to this C5 argument; Day's reply (C5a) says the C5 number was circular.

## Formal statement
Neutral fixation time conditional on fixation from intermediate frequency is of order 4Ne generations. With Ne = 1e4 (parameters.yaml `population.Ne_modern_human`, unverified textbook value) and 240 generations in the window:
- 4Ne = 40,000 generations; at 25 y/gen = 1.0M y; 240/40,000 = 0.6% of the way (keruru: "six-tenths of one percent"); derived: holds.
- Drift SD at p = 0.5 over t generations = sqrt(p q t/(2Ne)) = sqrt(0.25 x 240/20,000) = 0.0548 (keruru: "about 0.05"); derived: holds.
- Fixation within 240 generations from p = 0.5 (keruru: "around 4 x 10^-35"). derived (R2, Brownian approximation in the arcsine coordinate y = arccos(1-2p), variance 1/(2Ne) per generation, distance pi/2, absorbing at pi): z = 14.34, tail = 1.2e-46. The two values differ by 11 orders; both are negligible. The exact absorbing-chain value is not computed in the repo (B2a computes the same chain only for short-time asymptotics from p = 1/(2N)).
- Day's own expression exp(-pi^2 Ne/T) at Ne = 1e4, T = 240 = 10^-178.6 (derived) is for a full path from a single copy (p near 0), so it is not comparable to keruru's p = 0.5 start.

## Assumptions
- Stated: neutrality; closed population; "a human effective size around ten thousand".
- Implicit: Ne = 1e4 is correct for the window (disputed: C4, C5a; keruru's own temporal-method Ne in C5b is near 1e4); exchangeable reproduction (no skew; relictation, E4, applies only at macroscopic family replacement); no admixture inflating frequency change.

## Responses
- Against: Day (C5a): Ne = 10,000 "comes from θ = 4Nₑμ, which presupposes k = μ" and the observed drift-variance Ne is near 2.
- In support: the repo's own B-branch checks establish that Ne sets the timescale (B3: t_fix/Ne about 4 for exchangeable models), which is the premise here.
- Weaknesses in the responses: Day's circularity argument depends on which mu enters θ (see C5a); keruru later withdrew the claim for the stated reason, so this is no longer an endorsed critic position, but the arithmetic stands independently of the author.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura & Ohta 1969 (4Ne) | "a single mutant gene, if it is selectively neutral, takes about 4Ne generations until fixation in a population of effective size Ne." | accurate (fidelity ledger, Eq. 15 and Summary) |
| Kimura 1962 (fixation probability) | "if we let s → 0 in (10), we obtain U = 1/2N, the result known for a neutral gene." | accurate; N is the census size |

## Pre-registered prediction
- Under the claimant's model (neutral, Ne ~ 1e4): zero completions from below 50% in 240-350 generations, and the expected number from 50-90% starts is below 0.01; the observed 1 (v62) and 3 (v66) completions are sampling noise or admixture.
- Under the opposing model (Day, d = 0.45 with rate-limited fixation; or Ne near 2): zero completions from below 50% is also the prediction (Day: "fewer than 20 across the entire genome"). Both models give ~0, so the statistic does not discriminate.
- Result that would change a verdict: a forward simulation that gives a non-negligible neutral expectation (>0.1) of completions from start frequencies 50-90% at any Ne in the plausible range (then C5's "not close" claim fails), or a discriminating statistic (variance of frequency change, C4) where the two models differ.

## Check
Script: `research/checks/c_adna_neutral_expectation.py` (planned, shared with C). Report expected completions by start band at Ne in {1e3, 5e3, 1e4}, with and without a 10% admixture pulse. · Result: not run · Review: pending

## Simulator variables implied
Ne, window length, start-frequency spectrum, admixture pulse.
