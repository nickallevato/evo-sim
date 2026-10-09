---
id: A4g
title: "Day: standard fixation models (Wright-Fisher and Kimura's revision) treat a generation as the whole population replaced; real populations overlap"
side: day
branch: A
parent: A4
edges: [{type: supports, target: A4}]
load_bearing: false  # premise behind the correction d (A4) and Duffy's 20 -> 25 example (A4c); MITTENS 3.0 dropped d (A4d)
sourcing: firsthand  # Zenodo text is Day's own; the book wording (two standard models) is secondhand via the Gutsick Gibbon video
status: extracted
verdicts:
  internal: pending
  fidelity: pending
  external: pending
---

## Statement (verbatim)
> Researchers modeling allele frequency change in humans and other long-lived species routinely use discrete-generation equations, implicitly assuming that the entire gene pool is replaced each generation. This assumption is false

Source: [Day & Athos, The Selective Turnover Coefficient: Distinguishing Selection from Drift in Age-Structured Populations](https://zenodo.org/records/18166234) (key Z18166234), pub. 2025-12-24, abstract paragraph (line 15 of the extracted text `sources/raw/day/zenodo-18166234.txt`).

> the generational models including the right fisher model that underlies most fixation theory assumes that the entire parental generation is completely replaced by the offspring generation.

Source: Gutsick Gibbon + Zach Hancock video, [No, Vox Day's AI-Generated Books Did Not Debunk Evolution](https://www.youtube.com/watch?v=_Vu0ZVVjwHc), 2026-10-03, t=00:41:55 (auto-caption; spelling as captioned). Read aloud by the host from Duffy's slide, which quotes *Probability Zero*; the book text was not accessed. `secondhand`.

> In standard fixation models, a generation represents the entire population

Source: same video, t=00:59:16 (Duffy's slide as read by the host; `secondhand`). Duffy's slide, as the host reads it at t=00:51:35: "the two standard models the right fisher model and its subsequent revision by Kamura" (captions; the quotation continues "a generation represents the entire population").

## Formal statement
Premise of A4: Wright-Fisher (WF) and Kimura's diffusion treat generations as non-overlapping, so the per-generation response to selection is overstated in age-structured species by the factor d (A4). Not an equation of its own.

## Assumptions
- Stated: WF and Kimura's model are "the two standard models" and both assume complete replacement.
- Implicit: no standard treatment already corrects for overlap (the correction d is new); the correction acts on the time-scale of selection, not only on drift.

## Responses
- Against: Hancock (A4e): the Moran model is the classic overlapping-generations model, Kimura's diffusion is a continuous-time smoothing of WF (not a revision of it), and effective size absorbs overlap (Felsenstein, early 1970s, and Hill, per the speaker).
- In support: the WF model as classically defined is discrete and non-overlapping (conceded by Hancock at t=00:42:37); R4 C2 found that d*s is exact for hazard-scale s (A4 Check).
- Weaknesses in the responses: Hancock's Nₑ route corrects the rate of drift; whether it also fixes the time-scale of a selective sweep when s is hazard-scale was not tested (R4 C2 factor 1 for per-generation s).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Moran (1962 per the speaker), Felsenstein (early 1970s per the speaker), Hill, Kimura | not retrieved (named by Hancock only) | pending |

## Pre-registered prediction
No check. A textbook-level fidelity item: does Kimura's diffusion count as a "revision" of WF, and what do the standard texts say about overlapping generations.
- Under the claimant's model: standard fixation theory is a discrete non-overlapping abstraction.
- Under the opposing model: overlap is handled by Nₑ or the Moran model within the standard theory.
- Result that would change a verdict: a textbook statement that the standard fixation-time and probability results assume non-overlap without an Nₑ correction (supports Day), or the converse.

## Check
None. Related: R4 C2 (`research/checks/results/R4-H-C2.md`).

## Simulator variables implied
- Life table, generation time, Nₑ/N ratio; a toggle between non-overlapping and age-structured dynamics.
