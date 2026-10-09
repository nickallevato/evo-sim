---
id: A5h
title: "A 100-fold mutator gives about 38,400 new mutations per individual per generation, so its carriers are 'functionally dead' (s6.4)"
side: day
branch: A
parent: A5d
edges: [{type: supports, target: A5d}]
load_bearing: false
sourcing: firsthand
status: reviewed
verdicts:
  internal: arithmetic-error   # R4 X1 rule rev 2, R1(ii) and S3: 3.2e9 x 1.2e-8 x 100 = 3,840, not 38,400 (10x). The 10% deleterious count is then 384, not 3,840, so the downstream fitnesses are 0.999^384 = 0.68 (printed 0.02) and 0.99^384 = 0.021 (printed 1e-17); both move by more than 25%
  fidelity: n/a   # own arithmetic; inputs are standard values (genome size, human mu), exempt under rule F
  external: pending   # whether a 100x mutator is purged at once in a sexual population is untested here; at the corrected numbers fitness is 0.68 (s = 0.001) or 0.021 (s = 0.01)
---

## Statement (verbatim)
> A 100-fold increase in mutation rate in the human genome would produce approximately 38,400 mutations per individual per generation (3.2 × 10⁹ bp × 1.2 × 10⁻⁸ × 100). At a conservatively estimated 10% deleterious fraction, this means 3,840 deleterious mutations per individual per generation.

> At an extremely conservative s = 0.001 — far milder than most measured deleterious effects — fitness equals (0.999)^3,840 ≈ 0.02, a 98% fitness reduction. At a more realistic s = 0.01, fitness equals (0.99)^3,840 ≈ 10⁻¹⁷. Every individual carrying the supermutator allele is functionally dead.

Source: [MITTENS 3.0: The Mathematical Impossibility of the Post-Darwinian Polythesis](https://zenodo.org/records/23003785), Vox Day and Claude Athos, Zenodo 23003785 v1, 2026-09-28, s6.4 "The Breeding Reality Principle" (local text `sources/raw/day/zenodo-23003785.txt` lines 458-466; quoted verbatim, line breaks removed).

## Formal statement
`derived:` (R4 X1) 3.2e9 x 1.2e-8 x 100 = 3,840 mutations per haploid genome per generation, not 38,400 (a factor of 10; the printed formula and the printed product disagree). The 10% deleterious fraction is then 384, not 3,840. Day's exponentiation is right for the numbers he printed: 0.999^3,840 = e^-3.84 = 0.0215 and 0.99^3,840 = 1.7e-17. With the corrected count: 0.999^384 = 0.68 and 0.99^384 = 0.021. (A diploid reading, 6.4e9 bp, gives 7,680 and 768, still 5x below the printed 38,400 and 3,840.)

## Assumptions
- Stated: 100-fold mutator; 10% of new mutations deleterious; multiplicative fitness; s = 0.001 or 0.01 per deleterious mutation.
- Implicit: every carrier carries the full load in one generation (no accumulation dynamics); the per-site rate scales linearly with the mutator effect.

## Responses
- Against: Dumb-and-Dumber, r/DebateEvolution post 1wss2wj (RE-02, claim A2h): "Section 6.4 also makes a tenfold arithmetic mistake: 3.2 billion × 1.2 × 10⁻⁸ × 100 is 3,840 mutations per haploid genome, not 38,400." The audit confirms the arithmetic (A2h holds / accurate).
- In support: none located. At the corrected numbers the s = 0.01 case is still a 98% fitness reduction (0.021), so the direction of "strong selection against supermutators in sexual populations" survives at s = 0.01, but not "functionally dead" at s = 0.001 (0.68).
- Weaknesses in the responses: A2h does not state the corrected downstream fitnesses.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| none cited in s6.4 for these numbers | | n/a |

## Pre-registered prediction
Not applicable (arithmetic node created in the R4 X1 re-score; no simulation).

## Check
R4 X1 (research/checks/results/R4-X1-rescore.md; rule research/checks/results/R4-X1-verdict-rule.md rev 2; review #12, 2026-10-09): node created under rule S3 (a slipped number that carries an argument and that no node held). Under R1 the printed product is off by 900% and the slip moves the downstream numbers the same source states (0.02 to 0.68; 1e-17 to 0.021), so `arithmetic-error`. Before this node existed the slip was recorded only as the critic claim A2h (holds), with no Day-side verdict, which the X1 Day-side steelman review flagged as an asymmetry.

## Simulator variables implied
- `mutator_fold` (rate multiplier), `deleterious_fraction`, `s_del`, fitness model (multiplicative), recombination (mutator decoupling).
