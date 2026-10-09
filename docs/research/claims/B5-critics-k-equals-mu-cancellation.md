---
id: B5
title: "Critics: 2N mu new mutations × 1/(2N) fixation probability = mu substitutions per generation, independent of N"
side: critic
branch: B
parent: B
edges: [{type: attacks, target: B1}, {type: attacks, target: B2}, {type: attacks, target: B3a}]
load_bearing: true  # if the steady-state identity applies to the 252,000-generation window, B1, B2 and B3 yield no deficit (subject to B1c)
sourcing: firsthand
status: reviewed
verdicts:
  internal: holds
  fidelity: accurate
  external: "contested"   # exact at steady state; transient and overlap effects (B1c, B3b)
---

## Statement (verbatim)
> and then what you're left with is a neutral substitution rate that's equal to the mutation rate

Source: [Gutsick Gibbon + Zach Hancock, "No, Vox Day's AI-Generated Books Did Not Debunk Evolution" (auto-captions)](https://www.youtube.com/watch?v=_Vu0ZVVjwHc), 2026-10-03, t=01:48:19 (Hancock; auto-caption; derivation via Taylor expansion of the Kimura fixation probability)

> Genetic drift happens in every population and his claim otherwise is mystifying. Population size only affects which alleles are effectively neutral.

Source: [Mansfield (@brianmansfield6912), YouTube comments under Examining Origins video jDxFtCOGZ3A](https://www.youtube.com/watch?v=jDxFtCOGZ3A), comments retrieved 2026-10-07; terminus ante quem 2026-10-01: Day quotes this comment in "The Education of a Population Geneticist", ¶8 (added 2026-10-08), comment UgyhNduYke46IStQ5pd4AaABAg (Mansfield)

> ignores that neutral mutations fix at approximately the mutation rate

Source: [r/DebateEvolution, Dumb-and-Dumber, "New anti-evolution paper today from Vox Day"](https://www.reddit.com/r/DebateEvolution/comments/1wss2wj/), 2026-09-28, comment pcovtvf by DarwinZDF42 (score 27), reply under r/DebateEvolution post 1wss2wj

## Formal statement
k = (2Nμ_site-or-genome) × (1/2N) = μ per generation (diploid, census N, neutral). In genome terms k = μ_G = μ_site × L_haploid. Glossary sense: **throughput** at steady state; the identity says nothing about how long an individual fixation takes or whether the window is long enough (B1).
Acceptance by Day's side: Z22129121 "this paper accepts it throughout"; blog 2026-08-27 (B3g).

## Assumptions
- Stated: Neutral; constant size at equilibrium; census N in supply and in P_fix.
- Implicit: The ancestral population was at equilibrium at the split (B1c); the 252,000-generation window is long relative to the transit (B1: 4Nₑ = 40,000–132,000 for Nₑ = 10⁴–3.3×10⁴).

## Responses
- Against: Day (B1, B2): steady state not reached; k(T) = μF(T).
- In support: "It needs the elapsed time to be long compared with the fixation time." ([r/DebateEvolution, justatest90, comment pcug1j0 under "New anti-evolution paper today from Vox Day"](https://www.reddit.com/r/DebateEvolution/comments/1wss2wj/new_antievolution_paper_today_from_vox_day/pcug1j0/), 2026-09-29; RE-16. Attribution corrected 2026-10-09, R4 X1 section 8: this is justatest90's comment, not the OP Dumb-and-Dumber. The commenter accepts the 4Nₑ time and argues 252,000 is long compared with it)
  Related checks (below).
- Weaknesses in the responses: The Reddit author uses Nₑ ≈ 10⁴–3.3×10⁴ for 4Nₑ, which is the quantity Day calls circular (B3h). Mansfield's and Darwin's comments are one-liners.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura 1962 | "if we let s → 0 in (10), we obtain U = 1/2N, the result known for a neutral gene." | verified-accurate (ledger; see B7a) |
| Tenaillon 2016 | "neutral mutations accumulate at a constant rate" (non-mutator LTEE populations) | verified (ledger) |

## Pre-registered prediction
Pre-registered prediction (copied from RESULTS B0.5; the check has run).
- Under the claimant's model: (Critic) at equilibrium the neutral substitution rate equals the mutation input U for any N.
- Under the opposing model: (Day, k = μ accepted at steady state) same value; the dispute is the start state and window (B1, B2).
- Result that would change a verdict: A scenario in B1c where the human-lineage window is not long relative to transit would reduce the applicability; the identity itself is not in doubt.

## Check
Script: `research/checks/baseline_textbook.py` (seed 20261007) · B0.5 result: neutral k at equilibrium, N=50: 0.05018, N=200: 0.04964, vs U = 0.05 (z = +0.13, −0.64); holds for both N, consistent with k = U for any N. Review #2: B0.5 holds. Review: `research/checks/REVIEW.md#2026-10-07--correctness-review-2-sonnet-on-b0b3`

R4 B1c/B3b (research/checks/results/R4-B1c-B4a.md, R4-B3b-C1.md): k = mu holds exactly at steady state with discrete generations (controls 1.000), but not exactly with overlapping generations plus fluctuation (B3b, small) and not over a finite window after a contraction (B1c, per-lineage excess 1.9-4.0x). The critics' stated totals assume stationarity. Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)

## Simulator variables implied
- mutation input per generation (U)
- N
- equilibrium vs non-equilibrium start
