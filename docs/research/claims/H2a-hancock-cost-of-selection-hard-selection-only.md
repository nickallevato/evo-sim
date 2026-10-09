---
id: H2a
title: "Hancock: Haldane's cost of selection applies only to hard (viability) selection; under soft selection it largely disappears, and the allele need not start rare"
side: critic
branch: H
parent: H
edges: []  # PROPOSED: [{type: attacks, target: H}]; left empty until defeater dNEW-24 in argmap/mapping-proposals-2026-10-09.md is pasted (argmap_check edge coverage)
load_bearing: false  # restates H2 (Nunney 2003) and H3 in a critic's words; Day's H1 already limits the cost bound to adaptive substitutions
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: pending
  external: pending
---

## Statement (verbatim)
> the cost of selection is only applicable for hard selection models where selection's effect is independent of the genotypes

Source: [Gutsick Gibbon + Zach Hancock, No, Vox Day's AI-Generated Books Did Not Debunk Evolution](https://www.youtube.com/watch?v=_Vu0ZVVjwHc), 2026-10-03, t=02:07:18 (auto-caption; spelling as captioned; the sentence continues "of anyone else around you"). Illustration at t=02:06:57-02:07:18: bunnies with thicker fur surviving a cold snap (hard) versus a wolf that can only eat so many bunnies, so one only has to outrun the others (soft).

> the frequency doesn't have to be very low. It could have been a neutral alil and so it could have been at intermediate frequencies, right?

Source: same, t=02:12:32 (Hancock; the sentence begins "Um, another really key answer to it is that").

> that's important in populations that are really small in size and most of the issues come from uh being poorly adapted to your environment.

Source: same, t=02:08:20 (Hancock on when the cost matters; the sentence begins on the previous caption line, t=02:08:00: "I think that like holding's cost is one of those things").

## Formal statement
No equation. Haldane's cost: about 30N selective deaths per substitution; at most ~10% of mortality selective gives ~1 substitution per 300 generations (H). Hancock's two replies: (1) the budget exists only if selection is hard viability selection; (2) the cost is smaller if the favoured allele starts at intermediate frequency (standing variation).

## Assumptions
- Stated: the human lineage's selection is substantially soft (competition between individuals who are already well adapted, t=02:08:42).
- Implicit: the adaptive substitutions Day counts are not hard-selected; the deleterious load is also soft or tolerable (H7).

## Responses
- Against (Day): the reproductive ceiling is "the total selective deaths per generation remains constrained by what the population can bear" (Duffy's slide, t=02:11:10, `secondhand`); H1 (2026-05-07) already restricts the cost to adaptive substitutions.
- In support: Nunney 2003 (H2): soft selection reduces or eliminates the cost, but only where selection is driven by intraspecific competition; R4 H, H2-hard and H3: the 10% is not a general bound, the cap is ln R / D under hard selection, and the human-scale result is conditional on hard adaptive selection with a soft deleterious load.
- Weaknesses in the responses: Hancock gives no quantitative human-lineage estimate of the hard/soft split; the "small populations" remark is not derived (it is consistent with Nunney's dependence on M = 2Ku, H2 P2, but he does not cite it); the standing-variation reply lowers the cost of the first sweep but not of a continuing treadmill (H3).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Haldane 1957; Nunney 2003 | see H, H2 | accurate (H2) |

## Pre-registered prediction
No new check; R4 H, H2-hard and H3 already test the regime.
- Under the claimant (Hancock): any substitution cap is not binding for soft or standing-variation selection.
- Under the opposing model (Day): a population-wide budget on selection holds for the tested hard-selection treadmill.
- Result that would change a verdict: an estimate of the soft fraction of human adaptive selection (not in the corpus).

## Check
None new. Related: `research/checks/results/R4-H3-human.md`.

## Simulator variables implied
- Hard/soft selection switch, starting frequency of the favoured allele, M = 2Ku.
