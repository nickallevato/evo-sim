---
id: A3d
title: "Hancock: the achievable count should be doubled, since fixation happens in both lineages (a \"classic factor of two error\")"
side: critic
branch: A
parent: A3
edges: [{type: attacks, target: A3}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds
  fidelity: partial
  external: n/a
---

## Statement (verbatim)
> this basic math is off by a factor of two

Source: [Gutsick Gibbon and Zach Hancock video](https://www.youtube.com/watch?v=_Vu0ZVVjwHc), 2026-10-03, t=01:37:07 (GG-02; auto-caption). In the same passage: "So at at least this should be two times this ... So this really should be at least 360".

## Formal statement
Hancock's point: the achievable count (180 on Duffy's slide = 252,000/1,400) should be 2x180 = 360 because fixation accrues in both lineages.

`derived:` this changes the shortfall only if the required count is the total divergence. In MITTENS the required count is already per lineage (2025: 40M/2 = 20M; 3.0: 410M/2 = 205M; 2019: the post doubles the achievable instead, 562 = 2 x 281). The ratio R_total/(2F) = (R_total/2)/F is invariant, so the 3.0 shortfall (205e6/191) is unchanged by Hancock's correction. If Duffy's slide compared 180 with a total (both-lineage) count, the slide would be off by 2x; the slide text is not in the repo.

## Assumptions
- Stated: fixation is happening in both lineages since the split.
- Implicit: the required count on the slide was a two-lineage total (not shown).

## Responses
- Against (Day): MITTENS counts per lineage, halving 410M to 205M (Z23003785 s7.1).
- In support: the 2019 post doubles achievable (562 = 2 x 281.25), consistent with Hancock's accounting.
- Weaknesses in the responses: the repo cannot confirm which comparison Duffy's slide made. Hössjer notes (HO-05 context) both lineages in his own accounting; no one disputes the factor of two as a principle.

## Primary literature
| (none cited in the claim) | n/a | n/a |

## Pre-registered prediction
Arithmetic; no pre-registration needed beyond the invariance statement above.

## Check
Arithmetic only. Review: pending.

R4 GAP-07b (research/checks/results/R4-GAP07b-alignment.md): the gorilla-polarized SNV split is 48.6% human-derived / 51.4% chimp-derived (95% of SNVs polarizable), which supports 'apportion symmetrically'. The indel split is consistent with 50/50 only for events <= 50 bp (38-52% human depending on window); above ~100 bp the polarization rule cannot see the gorilla state, so support for symmetry comes from SNVs. Review: `research/checks/REVIEW.md` (review #8, 2026-10-09).

## Simulator variables implied
- A "per lineage / both lineages" accounting toggle.
