---
id: E5
title: "MITTENS 3.0's own tables give -906 'true fixations' in Ara-2 and take Ara+5 from 38 to 0; a count cannot be negative, so the estimator is an artefact"
side: critic
branch: E
parent: A2
edges: [{type: attacks, target: A2}, {type: attacks, target: E7}]
load_bearing: true  # The 1,322 generations/fixation figure (A2) averages Ara+5's 0 at 60K and the mutator 104.7 averages Ara-2's -906. If these cells are artefacts, the two headline LTEE rates in MITTENS 3.0 move; Day's later Z23105291 replaces them with lineage-aware counts.
sourcing: firsthand
status: reviewed   # reviews #19, #23 (VERIFY-operator-1, 2026-11-01)
verdicts:
  internal: holds   # R4 X1 rule rev 2 (was pending): arithmetic reproduces; artefact-vs-biology is external
  fidelity: accurate
  external: supported   # R4 E5-external (A2 | G5, as registered; REVIEW-R4-E5-external-combined cf1fbf1; fix pass 1, lead ruling K-1); was pending; scoped, see verdict_scope
verdict_scope:
  external: "Scope: A2 | G5 as registered. The -906 is the n = 2 clone-pair correction, not a fixation count; Ara-2 is positive under every rule on record (s3.2 snapshot 708 at 50K / 730 at 60K, Good HMM 939 / 977, Day's Z23105291 strict 94 and first-crossing 1,094). Day's pair is likely a cross-clade pair (Z23105291 Ara-2 94 whole-population / 1,816 within-lineage), so this is not a finding that Ara-2's sub-population structure is an artefact. Ara+5's 0 at 60K is beyond the last sample (57,500, F95 14); that diagnosis is the audit's, not RE-04's."
---

## Statement (verbatim)
> "Their correction formula then produces minus 906 “true fixations” in Ara−2."

Source: Dumb-and-Dumber, [r/DebateEvolution, "New anti-evolution paper today from Vox Day"](https://www.reddit.com/r/DebateEvolution/comments/1wss2wj/), 2026-09-28 (RE-1), post 1wss2wj (quote RE-03).

> "Their Ara+5 count drops from 38 such mutations at 30,000 generations to zero at 60,000."

Source: same post (RE-04).

> "A count of fixed mutations cannot be negative; the negative value comes from the paper’s own correction"

Source: Sparky_6_4 (AI-assisted), [KITTENS](https://www.reddit.com/r/DebateEvolution/comments/1wxgsjm/), 2026-10-04, post 1wxgsjm (RE-10).


RH tag (2026-10-10 pass): dialectic (stated as a checkable claim or derivation; no rhetorical device scored).
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

R4 X1 (research/checks/results/R4-X1-rescore.md; rule research/checks/results/R4-X1-verdict-rule.md rev 2; review #12, 2026-10-09): under the single both-sides rule this node is holds / accurate. arithmetic reproduces; artefact-vs-biology is external Charitable reading tried: attempted: no ambiguous referent.

R4 E5/E6 (research/checks/results/R4-E5E6.md; review #19, 2026-10-09): recount from the papers' own tables. Ara+5 reads 0 under the 60K snapshot but 14 (strict), 63 (first crossing) and 119 (strict plus within-lineage) elsewhere, and Ara-2 is 94 (strict), never negative; so the zero is specific to the snapshot construction, as the critics said. The clone-pair formula behind -906 is not in the extracted text and was not recomputed; the artefact-vs-biology verdict stays pending. Verdicts unchanged. Charitable reading tried: attempted: no ambiguous referent.

R4 E5-external (research/checks/results/R4-E5-external.md; review #98, combined, D-40, REVIEW-R4-E5-external-combined cf1fbf1; fix pass 1 3269481, lead ruling K-1 in briefs/E5-analyst-3.md; registration e5_external.py 4cfe7e5, run raw 0bfdfbf, 2026-11-26): external `pending` -> `supported`, scoped (see `verdict_scope`; not reading-dependent). Bands A2 | G5 as registered. Day side: the correction formula is right in kind (under a neutral SFS with n = 2, (P1+P2)/2 is the expected count of shared-but-unfixed sites); his data handling reproduces every measured cell (Ara+5 at 50K, four of five 60K non-mutator cells); Ara-2's sub-population structure is real (94 whole-population against 1,816 within-lineage in his Z23105291; the pair is likely cross-clade), and Ara+5's fall from 38 to 14 is real by his rule. Critic side: RE-10 (a count of fixed mutations cannot be negative) holds for Ara-2 under every counting rule on record; RE-03 (the -906 comes from the correction) holds; RE-04 (Ara+5 38 -> 0) is right about the cell, but the 0 is a G5 non-measurement (no sample at 60K; last sample 57,500, F95 14), the audit's diagnosis, not RE-04's. This is not a finding that the Ara-2 structure is an artefact. Open: the Tenaillon 2016 `.gd` files (owner-approved fetch only).

## Simulator variables implied
Counting rule (snapshot, first crossing, strict whole-population), sampling endpoint per population, lineage structure, clone sample size.
