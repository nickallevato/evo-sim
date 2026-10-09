---
id: G1a
title: "Day: in Ara+2, 66 fixations were 14 fixation events, all sequential; zero parallel fixations in any LTEE population"
side: day
branch: G
parent: G1
edges: [{type: depends-on, target: G1}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds   # R4 X1 rule rev 2 (was arithmetic-error): R1b, charitable reading (5.3 fixations per event): 74 vs 66 is 12% -> ledger; 5.3 basis unstated (F)
  fidelity: unverifiable   # R4 X1 rule rev 2 (was n/a): rule F (uncited/unretrievable input) or S/U; see R4-X1-rescore.md
  external: contested
---

## Statement (verbatim)
> There were 14 fixation events and every single one of them was sequential. The smallest gap between fixations was 1,500 generations. The largest gap was 9,500 generations.

Source: [Snikker-Snak](https://voxday.net/2026/10/01/snikker-snak/) (key B2026-10-01-snikker-snak), blog, 2026-10-01, ¶12.

> Each selective serial fixation carried along an average of 5.3 neutral mutations to fixation with it.

Source: [Snikker-Snak](https://voxday.net/2026/10/01/snikker-snak/) (key B2026-10-01-snikker-snak), blog, 2026-10-01, ¶13.

## Formal statement
Ara+2: 66 fixations (Z23105291 Table 1: 66 in 60,500 gens; blog: 66 in 60,000, 909 gens/fixation); 14 sweep events; claimed 5.3 hitchhikers per event.
`derived:` (python3 -I) 66/14 = 4.71 fixations per event, i.e. (66 − 14)/14 = 3.71 hitchhikers per event; 5.3 x 14 = 74, not 66; 66/5.3 = 12.5 events. The claim of 5.3 neutral mutations per selective fixation does not reconcile with 66 and 14 (unless 5.3 is an average over all populations, which the sentence does not say). 60,000/14 = 4,286 gens per sweep event in Ara+2; compare 909 per fixation (all-cause) and the blog's "SERIAL natural selection rate … ~24,500" (A2f) and 4,615 (A2f).
Definition used: two fixations are "parallel" if they occur in the same 500-generation slice; sweeps whose fixation times are ≥1,500 generations apart can still overlap in time during their rise.

## Assumptions
- Stated: data in 500-generation slices.
- Implicit: "parallel" means fixation events in the same time slice, not overlapping sweeps.

## Responses
- Against: s8.1 of Z23003785 (Day's own paper, three days earlier): "The 45.4 fixations … were not fixed one at a time in strict sequence. They were fixed in parallel, with multiple sweeps competing and completing simultaneously." Good 2017: "multiple beneficial variants simultaneously competing for dominance in each population". The two Day statements (s8.1 vs blog 2026-10-01) differ on whether within-population parallelism occurred.
- In support: none from critics; the claim is Day's empirical report from public data.
- Weaknesses in the responses: no critic has recounted Ara+2; the repo does not have the 500-generation slice data; the 5.3 does not reconcile as stated.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Good et al. 2017 | "The number of fixed mutations closely tracks Mp(t) in some populations (e.g. Ara+2 and Ara+4)" | verified |
| Tenaillon et al. 2016 | "Some others-including Ara-4, which became hypermutable, and Ara+2, which did not-are more linear in structure, without deep branches among the sequenced clones." | verified; consistent with serial sweeps in Ara+2 |

## Pre-registered prediction
Not run. Prediction (Day): recounting Ara+2 from the Good 2017 trajectories gives 14 events and ≥1,500-generation gaps. Prediction (critics): sweep durations exceed the gaps, so the sweeps overlap in time. Result that would change a verdict: sweep-interval overlap computed from the trajectories.

## Check
Arithmetic audit (python3 -I, scratch). Raw trajectories not in repo. Review: pending.

R4 X1 (research/checks/results/R4-X1-rescore.md; rule research/checks/results/R4-X1-verdict-rule.md rev 2; review #12, 2026-10-09): under the single both-sides rule this node is holds / unverifiable. R1b, charitable reading (5.3 fixations per event): 74 vs 66 is 12% -> ledger; 5.3 basis unstated (F) Charitable reading tried: tried 5.3 fixations per event (not hitchhikers): 74 vs 66 = 12% -> ledger.

## Simulator variables implied
- Counting of overlapping sweeps vs fixation-time gaps in the LTEE preset.
