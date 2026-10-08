---
id: C1a
title: "Day: panel ascertainment bias would favor detecting recent fixations, not obscure them"
side: day
branch: C
parent: C1
edges: [{type: attacks, target: C1}, {type: supports, target: C6}]
load_bearing: false  # Only defends the aDNA leg (C, C6); ROOT stands or falls without it.
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: n/a
  external: pending
---

## Statement (verbatim)
> "The 1240k panel was designed to capture polymorphisms informative for ancient DNA studies. This could bias toward alleles that are polymorphic in modern Europeans—but such bias would favor detecting recent fixations, not obscure them. The absence of recent fixations despite this bias strengthens our conclusion."

Source: [The Recalibration of the Molecular Clock: Ancient DNA Falsifies the Constant-Rate Hypothesis](https://zenodo.org/records/18525185), Z18525185, 2026-02-08, §9.4 "Ascertainment bias in the SNP panel" (¶261 of the odt text extraction). This is the only place in the Day corpus where ascertainment is addressed; Z23046531 (Sep 2026) does not mention it.

## Formal statement
Claim: let P = panel; if P is enriched for sites polymorphic in modern Europeans, then P is enriched for sites with intermediate modern frequency, which are the only sites from which a completion to fixation can be observed. So an ascertainment effect increases the expected number of observed completions, and an observed count of ~0 is conservative.

The reply asserts a sign without a calculation. It is silent on (a) substitutions of new mutations (C1 point 1) and (b) the Haak 2015 design (discovery in Yoruba and San heterozygotes rather than Europeans).

## Assumptions
- Stated: the panel is biased "toward alleles that are polymorphic in modern Europeans".
- Implicit: that ascertainment tracks European modern polymorphism (Haak 2015 says Yoruba/San discovery); that expected completions rise monotonically with modern intermediate frequency (completions also need a rare allele to have been at intermediate frequency 7,000 y ago, an independent condition).

## Responses
- Against: C1 (the repo's point 1 is not addressed by this reply).
- In support: none outside Day.
- Weaknesses in the responses: no simulation in Z18525185; the claim is a plausibility argument.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| none cited in §9.4 | n/a | n/a |

## Pre-registered prediction
- Under the claimant's model: ascertained-panel neutral expectation of 50-90% completions is higher than for a random site sample.
- Under the opposing model: the expectation is unchanged or lower; new-mutation substitutions on the panel are ~0.
- Result that would change a verdict: the C1 simulation. If ascertained-panel completions from intermediate starts exceed the unascertained rate (even if both are ~0 in absolute terms), C1a's sign is correct for that class; verdict on C1 point 2 then moves toward C1a.

## Check
Script: shared with C1 (`research/checks/c1_ascertainment_sim.py`, planned). · Result: not run · Review: pending

## Simulator variables implied
Ascertainment rule (discovery ancestry and size), start-frequency spectrum of panel sites.
