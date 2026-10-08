---
id: G2
title: "Hancock: the formula assumes each mutation must arise and go to fixation before the next can occur"
side: critic
branch: G
parent: A
edges: [{type: attacks, target: A}, {type: attacks, target: G1}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: pending
  fidelity: partial
  external: contested
---

## Statement (verbatim)
> it assumes that each mutation has to both arise and go to fixation before the next mutation can occur.

Source: [Gutsick Gibbon and Zach Hancock, "No, Vox Day's AI-Generated Books Did Not Debunk Evolution"](https://www.youtube.com/watch?v=_Vu0ZVVjwHc), 2026-10-03, t=01:31:58 (GG-01; auto-caption).

## Formal statement
Serial reading: N_fix(T) = T / t_fix where t_fix is the time for one allele to fix. Aggregate reading: N_fix(T) = T/G_f, G_f = observed T/n. The two coincide only if fixations do not overlap.
`derived:` (python3 -I) 252,000/1,400 = 180 (Duffy, DeDzjang); 252,000/66,000 = 3.8 and 252,000/20,000 = 12.6, the "4–13 neutral fixations" in Z23003785 s8.2 (a time/fixation-time division for drift); 252,000/27,600 = 9.1 (A5e).

## Assumptions
- Stated: sequential waiting.
- Implicit: that Day's G_f is a per-allele fixation time. Day's papers define it as a measured throughput (G1).

## Responses
- Against (Day): [They Never Stop Lying](https://voxday.net/2026/10/01/they-never-stop-lying/) (blog, 2026-10-01) ¶4: "No, literally none of my math assumes serial fixation. Not MITTENS …"; Z23003785 s8.1.
- In support: Day's own statements that read as serial (Appendix A passage "Therefore fixation must be sequential … yields 180 fixations", G2g; blog 2019 "average fixed mutation propagation time", GA-02; Q&A "t ≈ 19,800 generations per fixation", s8.2 4–13 neutral fixations; s8.6 "one fixation per 27,600 effective generations"). KITTENS §11: "§8.2 and Appendix D revert to the interval form for drift."
- Weaknesses in the responses: Hancock's statement is about MITTENS as presented by Duffy (MITTENS 2.x with 180); the video answers the Duffy version of 22 Sep, not MITTENS 3.0 (balance ledger). Day says the 3.0 rate is already a throughput. Neither side has measured within-population overlap (G1a).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Good et al. 2017 | "inconsistent with a “periodic selection” model" | verified |

## Pre-registered prediction
Linked result: F1 (research/checks/RESULTS.md, seed 31, N = 1000, s = 0.01, U_b = 0.01, independent loci, no interference, no cost): predicted steady-state rate 0.3960 per generation, simulated 0.3972 ± 0.0018; t_fix = 847 generations but G_f = 1/rate = 3 generations; in-transit count ≈ 336, computed from Little's law (not measured). Review #3 caveats: the regime is unrealistic (20 new beneficial mutations per generation), so pipelining is shown to be possible, not feasible; feasibility is the F2/H question.
- Result applied: as logic, dividing elapsed time by fixation latency is not a throughput bound (F1 verdict). Whether MITTENS does so is a reading question (G1 vs G2g); the repo has no check that settles it.

## Check
Link: `research/checks/RESULTS.md` F1. Review: pending.

## Simulator variables implied
- Toggle: serial (T/t_fix) vs aggregate (T/G_f) in F_max.
