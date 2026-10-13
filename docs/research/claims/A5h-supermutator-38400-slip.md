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
  external: pending   # whether a 100x mutator is purged at once in a sexual population is untested here; at the corrected numbers fitness is 0.68 (s = 0.001) or 0.021 (s = 0.01). R4 VID-01-score (2026-10-13) considered the GG-4 modelling objection (GGR-33/34) and did NOT move this field: the criterion registered in advance was that external moves to contested only if a located objection weakens the conclusion's direction, and this one, adopted at its strongest, strengthens it (e^-384 ~ 1.7e-167, independent of s)
---

## Statement (verbatim)
> A 100-fold increase in mutation rate in the human genome would produce approximately 38,400 mutations per individual per generation (3.2 × 10⁹ bp × 1.2 × 10⁻⁸ × 100). At a conservatively estimated 10% deleterious fraction, this means 3,840 deleterious mutations per individual per generation.

> At an extremely conservative s = 0.001 — far milder than most measured deleterious effects — fitness equals (0.999)^3,840 ≈ 0.02, a 98% fitness reduction. At a more realistic s = 0.01, fitness equals (0.99)^3,840 ≈ 10⁻¹⁷. Every individual carrying the supermutator allele is functionally dead.

Source: [MITTENS 3.0: The Mathematical Impossibility of the Post-Darwinian Polythesis](https://zenodo.org/records/23003785), Vox Day and Claude Athos, Zenodo 23003785 v1, 2026-09-28, s6.4 "The Breeding Reality Principle" (local text `sources/raw/day/zenodo-23003785.txt` lines 458-466; quoted verbatim, line breaks removed).


RH tag (2026-10-10 pass): dialectic (stated as a checkable claim or derivation; no rhetorical device scored).
## Formal statement
`derived:` (R4 X1) 3.2e9 x 1.2e-8 x 100 = 3,840 mutations per haploid genome per generation, not 38,400 (a factor of 10; the printed formula and the printed product disagree). The 10% deleterious fraction is then 384, not 3,840. Day's exponentiation is right for the numbers he printed: 0.999^3,840 = e^-3.84 = 0.0215 and 0.99^3,840 = 1.7e-17. With the corrected count: 0.999^384 = 0.68 and 0.99^384 = 0.021. (A diploid reading, 6.4e9 bp, gives 7,680 and 768, still 5x below the printed 38,400 and 3,840.)

## Assumptions
- Stated: 100-fold mutator; 10% of new mutations deleterious; multiplicative fitness; s = 0.001 or 0.01 per deleterious mutation.
- Implicit: every carrier carries the full load in one generation (no accumulation dynamics); the per-site rate scales linearly with the mutator effect.

## Responses
- Against: Dumb-and-Dumber, r/DebateEvolution post 1wss2wj (RE-02, claim A2h): "Section 6.4 also makes a tenfold arithmetic mistake: 3.2 billion × 1.2 × 10⁻⁸ × 100 is 3,840 mutations per haploid genome, not 38,400." The audit confirms the arithmetic (A2h holds / accurate).
- Against (modelling, added 2026-10-13 from GG-4): the Gutsick Gibbon panel, "This is supposed to be a genetic load that he's calculating. This is not the genetic load calculation. You wouldn't use a selection coefficient. Famously, what you would use is the mutation rate" (GGR-33, t=03:46:03) and "what the genetic load is based on one minus mu raised to the number of lossi, not one minus s raised to the number of lossi" (GGR-34). **Right in standard theory:** equilibrium mutational load is a function of the genome-wide deleterious rate U and not of the per-mutation selection coefficient (Haldane 1937; Muller 1950, L ~ 1 - e^-U), so the s-dependence of "functionally dead" is a property of this model, not of biology. A valid critic-side point, recorded as such.
- Against (arithmetic, independent): the same panel reaches 3,840 on its own, without reference to this audit - "these three numbers multiplied together do not equal 38,400 like he says ... It's like 3,800 when you multiply those three numbers" (GGR-31, t=03:44:42), corrected in the room to "the answer is 3,840" (GGR-32, t=03:46:25). Independent corroboration of `internal: arithmetic-error`.
- In support: none located. At the corrected numbers the s = 0.01 case is still a 98% fitness reduction (0.021), so the direction of "strong selection against supermutators in sexual populations" survives at s = 0.01, but not "functionally dead" at s = 0.001 (0.68).
- Weaknesses in the responses: A2h does not state the corrected downstream fitnesses. The GGR-33/GGR-34 modelling objection carries two costs to the critics: (i) its premise - "This is supposed to be a genetic load that he's calculating" - is an attribution the source does not carry; **the word "load" occurs zero times in MITTENS 3.0 and its addendum** (verified 2026-10-13 against the sha256-matched text), and s6.4's own words are "Under multiplicative fitness, the fitness of such an individual is (1 - s)^3,840 where s is the average selection coefficient against each deleterious mutation" - a per-carrier fitness from its own deleterious count, not a population load; and (ii) on the panel's own L ~ 1 - e^-U, at the corrected U = 384 a carrier's fitness is e^-384 ~ 1.7e-167 (384 x log10 e = 166.8), independent of s, so adopting the objection **strengthens** the "functionally dead" direction and removes the s = 0.001 escape this node records (0.999^384 = 0.68).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| none cited in s6.4 for these numbers | | n/a |

## Pre-registered prediction
Not applicable (arithmetic node created in the R4 X1 re-score; no simulation).

## Check
R4 X1 (research/checks/results/R4-X1-rescore.md; rule research/checks/results/R4-X1-verdict-rule.md rev 2; review #12, 2026-10-09): node created under rule S3 (a slipped number that carries an argument and that no node held). Under R1 the printed product is off by 900% and the slip moves the downstream numbers the same source states (0.02 to 0.68; 1e-17 to 0.021), so `arithmetic-error`. Before this node existed the slip was recorded only as the critic claim A2h (holds), with no Day-side verdict, which the X1 Day-side steelman review flagged as an asymmetry.

R4 VID-01-score (`research/checks/results/R4-VID-01-score.md`, 2026-10-13; predictions pre-registered
at `e857d1f`). Scored the GG-4 modelling objection (GGR-33, GGR-34) against this node under a
criterion fixed before the evidence was read: `external` moves `pending` -> `contested` **iff** a
located objection bears on the conclusion of the quoted statement ("every individual carrying the
supermutator allele is functionally dead") in a direction that **weakens** it; an objection that
bears only on the model while leaving or strengthening the direction is recorded in Responses and
the field stands. **Outcome: nothing moves, and that is the result.** The objection is right in
standard theory (recorded for the critics, above) and, adopted at its strongest, strengthens Day's
stated direction (recorded above as its cost). `internal: arithmetic-error` is untouched - the 10x
slip is Day's own arithmetic on his own printed inputs and no modelling objection reaches it; the
Statement was re-verified **verbatim** against the re-fetched, sha256-matched 3.0 text (s6.4
"The Breeding Reality Principle"), the local copy cited in the Source line having been lost.
`external: pending` is unchanged, now with a located objection on the record where "In support:
none located" stood alone.

## Simulator variables implied
- `mutator_fold` (rate multiplier), `deleterious_fraction`, `s_del`, fitness model (multiplicative), recombination (mutator decoupling).
