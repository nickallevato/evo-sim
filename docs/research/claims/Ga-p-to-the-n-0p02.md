---
id: Ga
title: "P(all) = p^n: 0.02^20,000,000 ≈ 10^−34,000,000 for 20 million fixations at p = 0.02"
side: day
branch: G
parent: G
edges: [{type: depends-on, target: G3}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds
  fidelity: accurate
  external: contested   # arithmetic holds, but it prices pre-specified arisings, not the event required; 'forces sequential fixation' (Dec 2025 abstract) is a non-sequitur
---

## Statement (verbatim)
> For n = 20,000,000 fixations (human-chimp divergence, human lineage) and p = 0.02: P(all) ≈ 0.02^20,000,000 ≈ 10^−34,000,000

Source: [MITTENS 2025, Zenodo 18165980](https://zenodo.org/records/18165980) (key Z18165980), pub. 2025-12-28 (modified 2026-01-06), ¶24 (Results).

## Formal statement
P(all) = p^n with n = `divergence.required_fixations.day_2025` = 2.0e7 and p = 0.02.
`derived:` log10(0.02^(2e7)) = 2e7 x (−1.69897) = −33,979,400 → 10^−33,979,400, which rounds to the stated 10^−34,000,000 (0.06% difference in the exponent). The value p = 0.02 = 2s for s = 0.01 (Kimura 1962, "approximately twice the selection coefficient"; used as P_escape in Z18167588 s7.9). Pass-1 attributed this number to Z18167588; it is in Z18165980. Z18167588 uses n = 157,000, p = 0.5 (Gb).
Compare Darwillion (McCarthy's rendering, G4): (1/20,000)^(2e7) = 10^−86,020,600. The two use different p (0.02 vs 5e-5).

## Assumptions
- Stated: independence of the n fixation events; each has probability p; "simultaneous success".
- Implicit: the n events are a pre-specified set (G3); p is the per-new-mutation fixation probability for a beneficial mutation, whereas the n loci being fixed are not mutations that all must arise at a given time.

## Responses
- Against: McCarthy (G3): a specific set; the probability of any 20M is near 1 given the supply. Camestros (G3a): lottery analogy.
- In support: Day (G3b): either specific fixations matter (Darwillion applies) or they are interchangeable neutral noise.
- Weaknesses in the responses: the critics' "any 20M" estimate uses neutral k = μ (B-branch) which Day disputes; Day's dilemma does not address selection acting on many possible beneficial sites.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura 1962 | "approximately twice the selection coefficient" | verified-accurate |

## Pre-registered prediction
Covered in G3 (specific-vs-any) and G-sim. Result recorded above.

## Check
Arithmetic audit (python3 -I, scratch). Review: pending.

R4 G1 (research/checks/results/R4-G1.md): independence holds with free recombination (joint/product 1.03 +/- 0.02); joint < product when linked (0.84 / 0.65) or clonal (0), Day's stated direction. p^n is timing-independent. Review: `research/checks/REVIEW.md` (review #5, 2026-10-08).

## Simulator variables implied
- None directly.
