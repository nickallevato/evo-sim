---
id: E
title: "Punctuated equilibrium's peripatric mechanism sits where hypermutation is favoured: 6 of 12 LTEE populations became mutators and a founder event has a ~2.3% chance of producing a repair-deficient homozygote"
side: day
branch: E
parent: ROOT
edges: [{type: supports, target: ROOT}, {type: depends-on, target: E7}, {type: depends-on, target: E8}]
load_bearing: false  # Scoped by its own authors as a hazard to one mechanism of PE (peripatric model) and "does not claim that every conceivable version of punctuated change is thereby refuted". ROOT (common descent cannot be reached in time) does not require E.
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: pending
  external: pending
---

## Statement (verbatim)
> "Six of the twelve populations independently evolved hypermutator phenotypes through destruction of DNA repair systems: four via mismatch repair defects (mutS/mutL) and two via oxidative damage repair defects (mutT)."

Source: [Punctuated Equilibrium and the Hypermutation Hazard](https://zenodo.org/records/23020792), Z23020792, 2026-09-28, Abstract.

> "The compound probability, a founder event capturing two or more carriers, multiplied by the conditional probability of producing a homozygote, is approximately 0.06 × 0.39 ≈ 2.3% per founder event."

Source: Z23020792, §5.1 (quote Q73 gives the short form "is approximately 0.06 × 0.39 ≈ 2.3% per founder", p.7).

> "This paper does not claim that every conceivable version of punctuated change is thereby refuted."

Source: Z23020792, §7 Conclusion.

> "The hypermutation hypothesis that elevated mutation rates could accelerate evolution to the degree the fossil record requires asks us to accept that the mechanism universally recognized as lethal at the tissue level in mammals would be constructive at the species level."

Source: Z23020792, §7.

## Formal statement
H_event = P(founder sample contains >= 2 defective copies) x P(at least one homozygote | >= 2 copies).
Parameters in the paper: Lynch carrier frequency 1/280, p = 0.0036 per diploid; founder N = 100; "approximately 5-6%" for >= 2 carriers (binomial n = 100); q = 0.01 after conditioning on two carriers; 100 offspring/generation for 50 generations; Poisson 1 - e^(-0.5) = 39%. Hypermutation incidence 6/12 with "exact binomial 95% confidence interval ... approximately 21-79%".

derived (R2 recompute, python3 stdlib):
- Binomial n = 100, p = 0.0036: P(>= 2 carriers) = 0.0509 (paper: "5-6%", used 0.06). With 0.0509: 0.0509 x 0.3935 = 2.0%, not 2.3% (0.06 x 0.39 = 2.34% holds as the paper's own product).
- q = 0.01 gives q^2 = 1e-4; x 100 offspring x 50 generations = 0.5; 1 - e^(-0.5) = 0.3935 (holds).
- Clopper-Pearson 95% interval for 6/12: 0.211 to 0.789 (paper "21-79%": holds).
- Mutator count: this paper says six (Ara-1, -2, -3, -4, +3, +6). Z23003785 and Z23105291 use seven mutator populations (adding Ara+1, an IS-element mutator of about 5x per Z23003785 §5.1). Tenaillon 2016 lists the same six as this paper (E8).
- Decomposition: the later simulation (Z23034852, E3) reports P(>= 2 copies) = 5.1% and P(homozygote | >= 2 copies) = 14.7% at N = 100, which multiply to 0.75%, not 2.3%. The mechanism "two carriers are the minimum required to produce a homozygous offspring" (§5.1) is thus not what produces most of the simulated 2.3% (see E3).
- Parameters mapping: no entry in `parameters.yaml` yet; proposed `ltee.mutator_populations` (6 vs 7), `pe.lynch_carrier_freq` = 1/280 (source: Day; Win et al. not retrieved).

## Assumptions
- Stated: the model targeted is "the Mayr/Gould peripatric model ... driven by successive fixation of new mutations in small founder populations under intense selection"; founder populations of N_e 100-1,000 for mammals; random mating within a closed isolate; effects of hypermutation in bacteria generalise (the paper says "The direction of extrapolation is toward greater severity").
- Implicit: that one homozygous CMMRD-equivalent individual in a founder population is a failure of the speciation mechanism (the paper itself says "Whether it is evolutionarily consequential depends on how many founder events PE's model posits ... questions that warrant formal demographic modeling"); that mutator hitchhiking carries over from asexual bacteria to sexual vertebrates (E3 concedes it is "not load-bearing"); that the mismatch-repair carrier frequency of a modern outbred human sample applies to ancestral isolates.

## Responses
- Against: no critic in the corpus engaged this paper. The paper's scope statement (above) concedes alternative mechanisms (standing variation, polygenic shifts).
- In support: none outside Day; Tenaillon 2016 supports the six-mutator count (E8).
- Weaknesses in the responses: not engaged.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Tenaillon 2016 | "six populations (Ara-1, Ara-2, Ara-3, Ara-4, Ara+3 and Ara+6) had 96.5% of the point mutations, having evolved hypermutable phenotypes" | accurate for the six; the mutS/mutL versus mutT split is not in the quoted passage (unverified) |
| Good 2017 | hypermutator phenotypes (cited) | not checked for the gene split |
| Oliver 2000; LeClerc 1996 (clinical mutators) | not retrieved | unverified |
| Wimmer 2014 (CMMRD) | not retrieved | unverified |
| Eldredge & Gould 1972; Mayr 1954 | the peripatric mechanism | not retrieved; the paper itself says the genetic mechanism is "Mayr's" |

## Pre-registered prediction
Written before any check runs.
- Under the claimant's model: Wright-Fisher founder simulation (N = 100 diploids, q = 1/560 per allele, s_hom = 0.95, s_het = 0.05, G = 50) gives P(>= 1 homozygote) about 2.3% per founder event, and the cumulative risk over 100 independent events exceeds 90%.
- Under the opposing model: the simulation gives the same per-event number within binomial error (50,000 replicates, SE about 0.07 points); the opposition is about consequence: one homozygote (removed by selection, s_hom = 0.95) in an isolate of 100 does not stop speciation, so the relevant per-event failure probability (persistence of the isolate or of the adaptive process) is far below 2.3%.
- Result that would change a verdict: (a) an independent simulation giving P(hom) outside 2.3 +/- 0.3% (then E and E3 are numerically wrong); (b) a demographic model with explicit fitness loss showing that founders carrying one homozygote fail to establish more than a small fraction of the time (then the hazard is consequential), or almost never (then it is not).

## Check
Script: none yet (spec: `research/checks/e_founder_hazard.py`, planned; independent WF with 50,000 replicates, seed fixed, binomial draws of 2N alleles from q = 0.0018, three selection regimes of Z23034852 Table 4, G in {50, 100, 200}, N in {50, 100, 200, 500}; add a consequence model: fraction of replicates in which mean fitness falls below 0.5 or the isolate dies out). · Result: not run · Review: pending

## Simulator variables implied
Founder size N, source allele frequency q, selection against homozygotes and heterozygotes, generations, number of founder events, mutator invasion (independent module), definition of failure.
