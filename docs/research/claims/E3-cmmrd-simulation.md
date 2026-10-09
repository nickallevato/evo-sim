---
id: E3
title: "A Wright-Fisher simulation of 50,000 founder events validates the 2.3% CMMRD-equivalent hazard; cumulative risk exceeds 90% over 100 events"
side: day
branch: E
parent: E
edges: [{type: supports, target: E}]
load_bearing: false  # Numerical support for E's headline hazard figure; ROOT does not use it.
sourcing: firsthand
status: extracted
verdicts:
  internal: holds   # only under an inferred mean-field (HW-expected) selection formulation; the literal §3.1 reading gives 2.75%, outside the pre-registered 2.33 +/- 0.15% band (falsifier fired). Table 8 not reproduced by either
  fidelity: unverifiable   # R4 X1 rule rev 2 (was n/a): rule F (uncited/unretrievable input) or S/U; see R4-X1-rescore.md
  external: contested   # overreach: 'independently sufficient' and 'minefields' not supported on the direct-viability endpoint; withdrawal of the hitchhiking pathway credited
---

## Statement (verbatim)
> "At N = 100 founders and G = 50 generations with full selection, the simulation produces P(≥1 CMMRD-equivalent homozygote) = 2.33% — virtually identical to the 2.3% estimate in Day and Athos (2026c)."

Source: [Strong Selection and the Improbability of Punctuated Equilibrium](https://zenodo.org/records/23034852), Z23034852, 2026-09-29, §3.2.

> "Across 100 founder events — a modest number for a model that claims to explain speciation patterns across major clades — the probability that at least one event produces a CMMRD-equivalent homozygote exceeds 90%."

Source: Z23034852, §3.8 (Table 7).

> "The hitchhiking pathway remains a genuine concern for organisms with limited recombination but is not load-bearing for the paper's conclusions."

Source: Z23034852, Abstract.

## Formal statement
Model (§3.1): draw 2N alleles from q = 0.0018 (carrier frequency 1/280); pair into N diploids; then Wright-Fisher with genotype fitness AA = 1, Aa = 1 - s_het, aa = 1 - s_hom; s_hom = 0.95, s_het = 0.05; count aa each generation; replicate 50,000 times (per abstract). Table 2 (G = 50, full selection): N = 50: P(hom) 1.6%, P(>= 2 copies) 1.4%, P(hom | >= 2 copies) 20.6%; N = 100: 2.3%, 5.1%, 14.7%; N = 200: 3.5%, 16.1%, 12.0%; N = 500: 6.0%, 52.8%, 9.4%. Table 4 (N = 100, G = 50): full selection 2.33%; s_het = 0: 3.62%; pure drift 3.94%.

derived (R2 recompute):
- Cumulative risk 1 - (1 - 0.0233)^n: n = 10: 21.0%; 50: 69.2%; 100: 90.5%; 500: 99.999% (paper 21.0, 69.3, 90.6, ~100; holds).
- P(>= 2 copies) at N = 100, q = 0.0018: 200 alleles, P = 5.10% (paper 5.1%; holds). P(>= 1 copy) = 30.3%.
- Joint of the table's own columns: 0.051 x 0.147 = 0.0075, versus the headline 0.0233. So about 68% of the simulated P(hom) arises from founder samples with fewer than 2 copies (single copies drift up and a homozygote arises later), i.e. P(hom | exactly 1 copy) is about (0.0233 - 0.0075)/(0.3025 - 0.051) = 6.3% (derived).
- Z23020792's analytic route requires two carriers and gives the conditional as 39% (E). Z23034852 reports the conditional given >= 2 copies as 14.7%. The headline numbers agree (2.3%); the two decompositions do not.
- Selection effect: (3.94 - 2.33)/3.94 = 41% reduction (paper "approximately 41%"; holds).
- The simulation parameters mirror the first paper's inputs (q, s_hom, s_het); there is no independent estimate of the carrier frequency in non-human mammals.

## Assumptions
- Stated: closed isolate; no gene flow; no inbreeding depression from other loci; "intentionally conservative on the hazard side".
- Implicit: P(>= 1 homozygote) is the right hazard; independence of events for the cumulative figure (paper: "approximately correct when founder events draw from different source populations"); a carrier frequency of 1/280 (modern human) for ancestral mammals; that a CMMRD-equivalent homozygote is a failure of the isolate.

## Responses
- Against: none in the corpus.
- In support: none.
- Weaknesses in the responses: not engaged; the decomposition mismatch above is a repo observation, not a critic's point.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Wimmer 2014; C4CMMRD Consortium (>90% cancer by 20) | not retrieved | unverified |
| Raynes 2011; Raynes & Sniegowski 2018 (mutator hitchhiking) | not retrieved | unverified |
| Lynch 2010; Lynch et al. 1993 (Muller's ratchet) | not retrieved | unverified |

## Pre-registered prediction
Written before any check runs.
- Under the claimant's model: an independent implementation of the §3.1 model reproduces 2.3% at (N = 100, G = 50) and the three-row selection ladder (2.33 / 3.62 / 3.94%) within binomial error.
- Under the opposing model: the same numbers appear (the model is a simple WF chain); the opposition concerns the consequence and the two decompositions.
- Result that would change a verdict: an independent run outside 2.33 +/- 0.15% at 50,000 replicates; or a breakdown of the simulated homozygote events by number of founder copies, showing which pathway (>= 2 copies versus 1 copy) produces them.

## Check
Script: `research/checks/e_founder_hazard.py` (planned, shared with E). Add output: P(hom) split by founder copy count 0 / 1 / >= 2 and time of first homozygote. · Result: not run · Review: pending

R4 E (research/checks/results/R4-E.md): see E. Literal reading 2.75% (+18%), s_hom inert for this metric; mean-field formulation reproduces 2.33%. Cumulative and G-insensitivity results hold. Growth variant raises the hazard (2.75 -> 9.0%). Review: `research/checks/REVIEW.md` (review #5, 2026-10-08).

R4 X1 (research/checks/results/R4-X1-rescore.md; rule research/checks/results/R4-X1-verdict-rule.md rev 2; review #12, 2026-10-09): under the single both-sides rule this node is holds / unverifiable. F: cited literature not retrieved Charitable reading tried: attempted: no ambiguous referent.

## Simulator variables implied
Founder size, q, s_hom, s_het, replicates, generations, event count, copy-number breakdown.
