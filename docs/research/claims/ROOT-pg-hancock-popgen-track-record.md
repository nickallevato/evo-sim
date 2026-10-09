---
id: ROOT-PG
title: "Hancock / Gutsick Gibbon: population genetics has a record of quantitative predictions that Day's model lacks; a challenger must survive that record"
side: critic
branch: ROOT
parent: ROOT
edges: [{type: attacks, target: ROOT}]   # flipped 2026-10-09 at integration (mapping proposals)
load_bearing: false  # inductive burden-of-proof argument; no number
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: pending
  external: pending
---

## Statement (verbatim)
> any new idea must run the gauntlet and be able to survive the theoretical edifice of population genetics

Source: [Gutsick Gibbon + Zach Hancock, No, Vox Day's AI-Generated Books Did Not Debunk Evolution](https://www.youtube.com/watch?v=_Vu0ZVVjwHc), 2026-10-03, t=00:27:23 (Hancock, auto-caption; spelling as captioned).

> And what this shows us is that this math is not arbitrary.

Source: same, t=00:23:55 (after the examples at t=00:22:54: the speaker's account of Haldane estimating the human mutation rate from hemophilia, and of the peppered moth selection strength confirmed by later field work; the caption renders Haldane as "Holding").

> The blunt fact of the matter is Vox Day's math can't do any of this.

Source: same, t=00:26:41 (host, after listing papers shown on screen on Drosophila, blowflies, crickets, mosquitoes, finches and sticklebacks; titles are not in the captions).

## Formal statement
Inductive: P(standard pop-gen predicts allele-frequency change and mutation-rate-scale quantities correctly | past record) is high; Day's F_max model makes no allele-frequency predictions; so a conflict between them is evidence against the model. Not formalised.

## Assumptions
- Stated: the record cited (hemophilia mutation rate, peppered moth, agriculture, Drosophila) is the relevant reference class; Day's math must reproduce those results to be taken seriously (t=00:24:58).
- Implicit: success at the scale of allele-frequency dynamics within a few generations transfers to the 6.3 My divergence count; Day's claim is about the standard theory, not about one model.

## Responses
- Against (Day): his claim is a rate limit, tested on its own data (the LTEE rate; aDNA fixation counts C, C6, C7), not a competing allele-frequency theory.
- In support: the repo's own checks reproduce textbook baselines first (B0), and the neutral count k = mu holds (B5); the aDNA completion counts are at or mildly above the neutral expectation (R4 C1b, per refresh-2026-10-09).
- Weaknesses in the responses: the speaker's examples were not retrieved or checked here; the record concerns microevolutionary scale; Day does make a testable prediction (zero completions, C), and the audit has tested it, so "Day's math makes no predictions" is only partly right. The same standard applies to the critics' side: B5c reproduces the observed ~35-40M SNV differences only with the SV-inclusive halving (19.4M on the SNV-only haploid count vs 38.3M), and no critic model has been checked against indel or SV event counts (GAP-07b).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Haldane (hemophilia mutation rate; peppered moth selection strength), Kettlewell, Majerus | not retrieved; named by the speaker (captioned "Holding") | pending |

## Pre-registered prediction
No check; this is a burden-of-proof argument.
- Under the claimant (Hancock): conflicts between Day's model and the standard theory resolve in favour of the standard theory.
- Under the opposing model (Day): the conflicts are in the inputs (unit, ceiling, start state), not in the theory.
- Result that would change a verdict: a documented case where F_max-type reasoning predicts a measured fixation count and the standard model does not.

## Check
None.

## Simulator variables implied
- None; suggests a validation panel of published pop-gen predictions (the textbook baselines B0 are the repo's version).
