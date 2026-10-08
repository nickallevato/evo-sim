---
id: E5
title: "MITTENS 3.0's own tables give -906 'true fixations' in Ara-2 and take Ara+5 from 38 to 0; a count cannot be negative, so the estimator is an artefact"
side: critic
branch: E
parent: A2
edges: [{type: attacks, target: A2}, {type: attacks, target: E7}]
load_bearing: true  # The 1,322 generations/fixation figure (A2) averages Ara+5's 0 at 60K and the mutator 104.7 averages Ara-2's -906. If these cells are artefacts, the two headline LTEE rates in MITTENS 3.0 move; Day's later Z23105291 replaces them with lineage-aware counts.
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: accurate
  external: pending
---

## Statement (verbatim)
> "Their correction formula then produces minus 906 “true fixations” in Ara−2."

Source: Dumb-and-Dumber, [r/DebateEvolution, "New anti-evolution paper today from Vox Day"](https://www.reddit.com/r/DebateEvolution/comments/1wss2wj/), 2026-09-28 (RE-1), post 1wss2wj (quote RE-03).

> "Their Ara+5 count drops from 38 such mutations at 30,000 generations to zero at 60,000."

Source: same post (RE-04).

> "A count of fixed mutations cannot be negative; the negative value comes from the paper’s own correction"

Source: Sparky_6_4 (AI-assisted), [KITTENS](https://www.reddit.com/r/DebateEvolution/comments/1wxgsjm/), 2026-10-04, post 1wxgsjm (RE-10).

## Formal statement
Checked against the targets (MITTENS 3.0, Z23003785, 2026-09-28, record modified 2026-10-04):
- §5.1 table: Ara-2 "Point mutator (~100×)  −906  N/A"; §5.2: "Despite a 100-fold elevated mutation rate, Ara-2 achieved negative net fixations at 50,000 generations: −906 by clone-pair analysis. The sharing rate between its two clones at 50K was 4.2%".
- §4.1 table: Ara+5 at 10K/20K/30K/40K/50K/60K = 16, 13, 38, 34, 14, 0; text: "Ara+5 drops from 38 fixations at 30,000 generations to zero at 60,000 generations".
Both critic statements are accurate to the paper.

derived (R2 recompute):
- Mean over the seven mutator populations with Ara-2 = -906: (110 + 932 + 803 + 978 - 906 + 273 + 1,153)/7 = 477.6, so 50,000/477.6 = 104.7 gen/fix (paper: 104.7; holds). Excluding Ara-2: 708.2, 70.6 gen/fix; the "100x gives 8.5x" ratio becomes 893/70.6 = 12.6x (E7).
- Non-mutator row at 60K: 64 + 68 + 0 + 60 + 35 = 227; /5 = 45.4; 60,000/45.4 = 1,321.6 (paper 1,322; holds). Excluding the Ara+5 zero: 56.75, 60,000/56.75 = 1,057 gen/fix (derived).
- Z23105291 Table 1 lists Ara+5 with last sampled generation 57,500. Z23003785's cell at 60K is therefore beyond Ara+5's last sample. Whether the zero is a missing-sample treatment is not stated in the extracted text of either paper (hypothesis, no verdict).
- Day's later data paper gives Ara+5 14 whole-population fixations (strict), 105 within-lineage sweeps, 63 first-crossing; Ara-2 94, 1,816, 1,094.

## Assumptions
- Stated (Day, Z23003785 §4.1): Ara+5's drop is "not [an] outlier"; "it stalls, reverses, and in some populations collapses entirely". The paper offers the Ara-2 figure as evidence that hypermutation "broke" the mechanism.
- Implicit (critics): the estimator, not the biology, produces the negative value; (Day) that a snapshot count at ≥95% frequency can fall and that its fall measures reversal rather than a changing denominator or missing sample.

## Responses
- Against: Day's Z23003785 reading above (collapse as a biological result). Day's own later correction: the whole-population strict definition (E6) abandons the clone-pair n = 2 method for the metagenomic state calls.
- In support: Day's Z23105291 abstract states that "the number of fixation events and the interval between them are not well-defined quantities in this system" and that the "≥95% rule" overcounts (E6). Good 2017 (E9) reports "a marked deficit of fixations in others (e.g. Ara-6)" and clade coexistence.
- Weaknesses in the responses: the Reddit posts do not diagnose the cause (n = 2 clone-pair "correction" versus a snapshot rule); KITTENS is AI-assisted and cites literature from memory (self-disclosed, RE-11).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Good 2017 | "The number of fixed mutations closely tracks Mp(t) in some populations (e.g. Ara+2 and Ara+4), but there is a marked deficit of fixations in others (e.g. Ara-6)." | accurate for the deficit; the ≥95% rule is not in the main text (ledger: unverified) |
| Consuegra 2021; Wielgoss 2013 (mutator classification) | not retrieved | unverified |

## Pre-registered prediction
- Under the critic's model: a count of fixations at a single time cannot be negative; any negative estimate comes from the correction formula applied to an unstructured-sample assumption violated by lineage coexistence; mutator throughput from strict counts is at least that implied by the non-negative clone-pair populations.
- Under Day's Z23003785 model: the negative value shows that very high mutation supply produces competing lineages with no net fixation.
- Result that would change a verdict: the clone-pair "true fixation" formula (not given in the extracted text; Z23003785 §3-§5 needs a close read) implemented on the Good 2017 clone genomes, returning a value <0 only when the sharing rate is near the random-sampling floor (then it is an estimator boundary effect, as the critics say).

## Check
Script: none yet (spec: re-implement the Z23003785 clone-pair correction on the published clone genomes; print per-population values; compare with Z23105291 Table 1). · Result: not run · Review: pending

## Simulator variables implied
Counting rule (snapshot, first crossing, strict whole-population), sampling endpoint per population, lineage structure, clone sample size.
