---
id: A4e
title: "Hancock: overlapping generations are handled by effective size and the Moran model; Kimura did not 'revise' Wright-Fisher; a century of theory covers it"
side: critic
branch: A
parent: A4
edges: [{type: attacks, target: A4g}]   # flipped 2026-10-09 at integration (mapping proposals)
load_bearing: false  # answers the Duffy/book version (d = 0.45, 20 -> 25 generations); MITTENS 3.0 dropped d (A4d)
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: pending
  external: pending
---

## Statement (verbatim)
> And the Moran model is the model of overlapping generations.

Source: [Gutsick Gibbon + Zach Hancock, No, Vox Day's AI-Generated Books Did Not Debunk Evolution](https://www.youtube.com/watch?v=_Vu0ZVVjwHc), 2026-10-03, t=00:43:38 (auto-caption; spelling as captioned). Hancock (population geneticist, self-described credentials at t=00:09:31).

> And you just scale that effective population size by the slowdown of drift due to overlapping generations.

Source: same, t=00:48:29.

> it's a correction factor that enables you to take the census population size and correct it for the observed rate of genetic drift

Source: same, t=01:00:59 (describing effective population size).

> That's not what Kamura did.

Source: same, t=00:51:57 (the sentence begins on the previous caption line: "Kamura doesn't have a subsequent revision of the right fisher model"). At t=00:54:02: "he takes the right fiser model which is a binomial ial sampling model. That is to say, it's a discrete time stairstep model. And he smooths it out and basically converts it to a continuous time model."

## Formal statement
Hancock's formula (t=01:00:18-01:00:38, speaker-stated, not verified here): Nₑ = (age at reproduction / age at death) × N, with about 25 and 75-80 y for humans, so Nₑ/N is about 0.31-0.33 (`derived:` 25/80 = 0.3125; 25/75 = 0.3333). Day's d = 0.45 (A4) is the same order but a different quantity: d rescales the per-generation response to selection, Nₑ rescales the rate of drift. Neither is shown to substitute for the other in the repo.

## Assumptions
- Stated: WF is discrete and non-overlapping; overlap is absorbed by Nₑ in WF formulas, or modelled directly (Moran); the correction is "really easy" and known since the 1960s-70s (t=01:03:23).
- Implicit: the Nₑ correction suffices for the quantity Day's d corrects (the time-scale of selective sweeps); Hancock states selection efficiency depends on Nₑ (t=01:16:26).

## Responses
- Against (Day): d is derived from life tables (C2, C2a) and R4 C2 found d*s exact for hazard-scale s; MITTENS 3.0 dropped d (A4d).
- In support: R4 C2: g_eff = d*g is standard theory with generation length T/d, so the field does carry the correction; Camestros's "d is undefined" was retracted (A4b), a separate point.
- Weaknesses in the responses: speaker's recollection of citations (Felsenstein 1972, "might be 74" as the speaker says; Hill; Moran 1962) not checked; Hancock answers Duffy's slide version of the book, not MITTENS 3.0 (balance ledger); he does not test that Nₑ rescales the sweep time.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Moran; Felsenstein; Hill; Kimura (Kolmogorov backward equation) | not retrieved; named by the speaker | pending |

## Pre-registered prediction
No check run. Proposed: A4-sim (already listed in A4): age-structured Moran model with a human life table; compare sweep time and fixation probability with discrete WF at Nₑ = N*b/d and at generation length T/d.
- Under the claimant (Hancock): with the Nₑ correction, WF formulas give the right answer for drift; the sweep time follows once generation length is set by turnover.
- Under the opposing model (Day): sweep time is slower by d on top of any Nₑ change when s is hazard-scale.
- Result that would change a verdict: a ratio of age-structured to Nₑ-corrected WF sweep time away from 1 by more than 10%.

## Check
None. Partly covered by R4 C2 (`research/checks/c2_overlap_vs_standard.py`).

## Simulator variables implied
- Nₑ/N ratio under overlap (b/d), generation length, life table; compare drift-rescaled and selection-rescaled runs.
