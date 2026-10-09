---
id: H9
title: "Kimura and Ohta (1969) established that the expected time to fixation does not depend on recombination rate"
side: day
branch: H
parent: H
edges: [{type: supports, target: H}, {type: attacks, target: A5f}]  # was attacks G1 (Day's own claim). H9 dismisses the recombination objection, which is A5f (Gariepy 2019; Bowers point 3) (fixed 2026-10-08)
load_bearing: false  # Used to dismiss the recombination objection in the Haldane and Bernoulli papers. The conclusion (recombination does not speed fixation of a single allele) may stand on other grounds; this file concerns the citation.
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: misread
  external: pending
---

## Statement (verbatim)
> "More fundamentally, Kimura and Ohta (1969) established that the expected time to fixation does not depend on recombination rate."

Source: [Independent Confirmation of Haldane's Limit](https://zenodo.org/records/18168236), Z18168236, 2026-01-05, §5.2 "The Recombination Objection", line 74 of the text extraction. The same passage appears in the Bernoulli Barrier paper (Z18167588, §7.3).

## Formal statement
Claim: T_fix (neutral or selected single-locus) is independent of the recombination rate r. Kimura & Ohta 1969 derive the mean fixation time for one locus in a diffusion model; their quoted result is t̄ about 4Ne for a neutral mutant ("a single mutant gene, if it is selectively neutral, takes about 4Ne generations until fixation in a population of effective size Ne"). Recombination requires at least two loci.
derived (R2, searched): the word "recombin" occurs 0 times and "linkage" 0 times in the full text of Kimura & Ohta 1969 (`sources/raw/sources/manual/KimuraOhta1969.txt`).
Parameter link: none. The substance (recombination does not change the fixation time of an isolated allele) is a property of single-locus models; it does not extend to linked loci, where recombination affects interference (Hill-Robertson, cited by Day in the reference list of Z18168236).

## Assumptions
- Stated: recombination "reshuffles existing variation; it does not create new variation or accelerate the rate at which any individual allele increases in frequency".
- Implicit: that a single-locus fixation-time result covers the many-locus problem; that clonal interference is absent in sexual populations (it is reduced, which is the opposing point).

## Responses
- Against: the fidelity ledger ("verified-misread (misattribution)"); E7's discussion of clonal interference versus recombination; Hill & Robertson (cited by Day, not quoted).
- In support: none beyond Day's own text.
- Weaknesses in the responses: the ledger entry shows the citation is a misattribution; it does not test the physical claim, which is partly true for a single locus.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura & Ohta 1969 | "a single mutant gene, if it is selectively neutral, takes about 4Ne generations until fixation in a population of effective size Ne." | single-locus result; no statement on recombination (word absent): misread |
| Hill & Robertson 1966 (in Day's reference list) | "The effect of linkage on limits to artificial selection" (title) | not retrieved |

## Pre-registered prediction
- Under the claimant's model: the mean fixation time of a beneficial allele is the same at r = 0 and r = 0.5 for a single locus embedded in a background of other segregating loci.
- Under the opposing model (Hill-Robertson): with other loci under selection, the fixation probability and time of a beneficial allele depend on r; tight linkage slows and reduces fixation when competing sweeps are present.
- Result that would change a verdict: a two-locus (or n-locus) simulation with both loci under positive selection (F2 interference) comparing fixation times at r = 0, 0.01, 0.5; the single-locus control must return the Kimura-Ohta diffusion value (B0.4).

## Check
Script: none yet (spec: part of F2 interference simulation, `research/checks/f2_interference.py`, queued). · Result: not run · Review: pending

## Simulator variables implied
Recombination rate r, number of selected loci, N, s.
