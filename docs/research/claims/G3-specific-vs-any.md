---
id: G3
title: "Specific-vs-any: the product of per-site probabilities prices a pre-specified list of 20 million mutations; evolution requires only that some 20 million out of an enormous candidate pool fix"
side: critic
branch: G
parent: G
edges: [{type: attacks, target: Ga}, {type: attacks, target: G4}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds
  fidelity: accurate
  external: contested
---

## Statement (verbatim)
> What Vox Day calculated—(1/20,000)20,000,000 —are the odds that a particular group or a pre-specified list of 20 million mutations (or 20 million mutations in a row) would all become fixed.

Source: [Dennis McCarthy, Why Probability Zero is Wrong About Evolution (free repost)](https://dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1), 2026-09-11 (orig. 2026-01-26), para 47 (MC-01). Exponent flattened in the HTML source.

> But our evolutionary history does not require that an exact group of 20 million mutations become fixed—only that some 20 million out of an enormous pool of candidate mutations become fixed.

Source: same post, para 48 (MC-02).

## Formal statement
P_specific(n) = Π p_i = p^n for a pre-specified set; P_any(≥ k of M) = P(Binomial(M, p) ≥ k).
`derived:` (python3 -I) With McCarthy's inputs (M = 4.5e11 new mutations in 9 My, p = 1/20,000 = 5e-5): mean M·p = 22.5e6, SD = √(M p (1−p)) = 4,743; k = 20e6 is 527σ below the mean, so P_any(≥ 20e6) ≈ 1 under that model, while P_specific = (5e-5)^(2e7) = 10^−86,020,600 (log10 = 2e7 x −4.30103). The two numbers answer different questions. McCarthy's M p = 22.5M is his neutral model (k = μ with all mutations neutral), which Day disputes (B3, B5); whether p = 1/20,000 is the fixation probability of a *new neutral* mutation (1/2N) or a beneficial one (2s) differs between Day's papers (Ga uses 0.02).

## Assumptions
- Stated: the event of interest is the existence of 20 million differences, not a specific list.
- Implicit (McCarthy): the supply M·p reaches 20M, i.e. neutral substitution at rate μ; all mutations treated alike.

## Responses
- Against (Day): G3b: "Either the specific fixations matter — in which case the Darwillion applies — or they’re interchangeable — in which case they’re neutral noise that can’t explain the observed functional divergence." The Darwillion is "nothing more than a rhetorical absurdity" (G4).
- In support: Camestros (G3a lottery analogy); Mansfield (MF-02, MF-03) the same point in terms of expected neutral fixations per generation; Day's own concession that the Darwillion is rhetorical (G4).
- Weaknesses in the responses: McCarthy's count of 22.5M rests on k = μ; his version (MC-04) is "equivalent to k=mu with all mutations treated as neutral" (quotes-file note), which does not reproduce selection; Mansfield's illustration (2% neutral gives 1 fixation per generation) comes out ~44x short of 20M over 450,000 generations (20e6/450,000 = 44). Day's dilemma uses "can’t explain the observed functional divergence" without defining the functional fraction.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura 1962 / Kimura & Ohta 1969 | neutral fixation probability 1/2N | verified (see B-claims) |

## Pre-registered prediction
Not run in this branch. Prediction (critics): under a neutral model with k = μ and M mutations, P_any ≈ 1 for 20M; this is B5 and was checked at B0.5 (neutral k = U at equilibrium for any N; simulated 0.05018 vs 0.05 at N = 50). Prediction (Day): the any-20M reading does not apply to functional divergence; not formalised.

## Check
Link: `research/checks/RESULTS.md` B0.5 (neutral k = U). Arithmetic audit (python3 -I, scratch). Review: pending.

## Simulator variables implied
- Event definition: specific list / any k of M / any k of M functional.
