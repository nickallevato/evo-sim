---
id: A5b
title: "KITTENS: the 1.075M shortfall factors into 94,000 (mutation-supply ratio) x 11.7 (bases counted as events)"
side: critic
branch: A
parent: A5
edges: [{type: attacks, target: A2e}, {type: attacks, target: A3a}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds
  fidelity: accurate
  external: contested
---

## Statement (verbatim)
> The claimed shortfall is 94,000 × 11.7, or about 1.1 million.

Source: [r/DebateEvolution, Sparky_6_4 (AI-assisted), "KITTENS: rebuttal to Vox Day's MITTENS 3.0 by Clauwd Meowgorithm"](https://www.reddit.com/r/DebateEvolution/comments/1wxgsjm/), 2026-10-04, s3 "The headline shortfall decomposes into two artifacts". Verified in raw copy `sources/raw/critics/arctic-title-Vox%20Day.json`.

> Once one scales the LTEE rate for the mutation supply per genome and counts SNVs as events, the achievable number (17.9 million) is about equal to the required number (17.5 million).

Source: same post (RE-08).

> I present this as an illustration, not as a proof that adaptive fixations scale linearly with mutation rate.

Source: same post (RE-09).

## Formal statement
Shortfall = R/F with F = N_gen/G_f. KITTENS: S = (U_h/U_E) · (R_205/R_SNV) where U_h = 3.2e9 · 1.2e-8 = 38.4 (KITTENS cites s6.3–6.4; the paper prints the product only for the 100x case, 38,400), U_E = 4.1e-4 (s4.3), R_205 = 205e6, R_SNV = 17.5e6.
`derived:` (python3 -I) U_h/U_E = 93,659; R_205/R_SNV = 11.714; product = 1,097,143 vs paper 1,075,000 (2.1% above, from rounding F = 190.6). 191 x 93,659 = 17.89e6 ("17.9 million", reproduces); 17.89/17.5 = 1.02. Table inputs found in Z23003785: 4.1e-4, 191, 17.5M, 205M, 1,075,000. The 38.4 is not printed in the paper; it is the 1x value of the product 3.2e9 x 1.2e-8 printed in s6.4 as 38,400 for 100x.
**Sensitivity (derived, this audit, not in KITTENS):** KITTENS assumes fixation rate ∝ supply (exponent 1). Day's own mutator data (A5d) give a response of 8.5x (clone-pair) to 16.9x (metagenomic) for 100x supply, an exponent a = ln(f)/ln(100) of 0.47 to 0.61. Applying that exponent to a 93,659-fold supply gives a factor of 206 to 1,136, achievable 39,370 to 217,006, and a shortfall against 17.5M of 445x to 81x (against 205M: 5,207x to 945x). Extrapolating an exponent measured over 100x to 94,000x is itself an assumption; mutator lines also carry deleterious load and are asexual.

## Assumptions
- Stated: only the paper's own numbers; a linear-scaling illustration (RE-09). AI-assisted; citations from memory (RE-11).
- Implicit: units of U_h (per haploid genome) match U_E; the SNV-only requirement is the right event count; linear scaling.

## Responses
- Against (Day): Z23003785 s5.1 and s8.6: a 100x mutation increase gives 8.5x–17x, "Supermutation does not scale linearly"; s8.6 Appendix D gives 27,600 generations per fixation from human parameters (A5e).
- In support: Hössjer's independent calculation reaches within 2x (A5a); Day concedes the SNV-only variant is legitimate (A3b).
- Weaknesses in the responses: with the sublinear exponent the gap reopens to 81x–445x for SNV-only, so the parity conclusion rests on linear scaling; the critic did not verify Day's mutator exponent; the critic's 94,000 treats LTEE and human U as the same kind of quantity (haploid-genome new mutations per generation).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Wielgoss 2011 (via McCarthy; not in repo) | E. coli per-site rate 8.9e-11 | unverified |
| Kong 2012 | 1.20e-8 per nucleotide per generation | verified (abstract) |

## Pre-registered prediction
Pre-registered here, check not yet run (A-sim, see file A).
- Under the critic's model: forward simulation with human-scale supply and free recombination fixes ≥ 1e7 adaptive substitutions per 252,000 generations at the same s as the LTEE.
- Under Day's model: fixations saturate at ~190 per 252,000 generations regardless of supply.
- Third possibility (this audit): sublinear scaling with exponent 0.5–0.6, leaving a 80–450x gap.
- Result that would change a verdict: measured response exponent of fixation rate to supply in a recombining simulation.

## Check
Arithmetic audit (python3 -I, scratch): decomposition reproduces; sensitivity computed in the scratch session. Review: pending.

## Simulator variables implied
- Exponent a in rate ∝ U^a as a user parameter (0.5 / 0.6 / 1).
