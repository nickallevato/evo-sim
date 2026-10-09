---
id: B3i
title: "Matev: if every allele at a site had fixation probability 1/(2N_e), the 2N alleles' probabilities would sum to N/N_e > 1 when N > N_e, which is not a probability"
side: critic
branch: B
parent: B3a
edges: [{type: attacks, target: B3a}]
load_bearing: false  # a reductio of B3a; same conclusion as B7, B3g
sourcing: firsthand
status: extracted
verdicts:
  internal: holds   # exactly one of the 2N copies present now is ancestral to the eventual population, so the per-copy probabilities sum to 1 and the neutral value is 1/(2N)
  fidelity: n/a
  external: supported   # B7 / R4 B3: neutral fixation probability is 1/(2N) of census copies; Day conceded on 2026-08-27 (B3g)
---

## Statement (verbatim)
> "the probability that some allele from this set will eventually fix would be 2N/(2Nₑ) = N/Nₑ, which is greater than one and therefore not even a valid probability when N > Nₑ."

Source: [Matev, comment on McCarthy, "Vox Day Responds"](https://dennismccarthy.substack.com/p/vox-day-responds/comment/345248135), 2026-09-25, comment id 345248135 (RF-2).

## Formal statement
At a neutral site with 2N gene copies, let u_i be the probability that copy i's descendants eventually fix. The events are mutually exclusive and exhaustive (with no further mutation), so sum_i u_i = 1, and by exchangeability u_i = 1/(2N). If u_i = 1/(2N_e) the sum is N/N_e, which exceeds 1 whenever N > N_e. `derived:` e.g. N = 1e6, N_e = 1e4: sum = 100.

## Assumptions
- Stated: all alleles at the site are neutral.
- Implicit: exchangeable copies (no heritable variance in offspring number tied to the allele); this is the standard neutral model and the one the Kimura identity uses.

## Responses
- Against: Day's 2026-09-21 objection that real populations have "covariance between who breeds and what they carry" (versions.md "N vs Nₑ in k") would break exchangeability; the reductio then applies only within the exchangeable model, which is the model k = mu is stated in.
- In support: B7, B7a, B7b (literature: 1/(2N)); B3g (Day's concession); B7c (keruru's retraction, same point).
- Weaknesses in the responses: Day restated "1/2Nₑ is the fixation probability for a neutral mutation" on 2026-09-15 (Q105), after the concession; Matev's comment (2026-09-25) postdates both.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura & Ohta 1969 | see B7b | accurate |

## Pre-registered prediction
Not run; the identity is exact. R4 B3 already measured k = mu across N and V_k.

## Check
Covered by R4 B3 / B7 (k = mu independent of N_e). From the 2026-10-09 corpus refresh (C-2).

## Simulator variables implied
None new.
