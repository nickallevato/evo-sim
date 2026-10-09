---
id: H6
title: "Nesslig20: Haldane's reproductive cost limit applies to selection but not to drift, so it cannot bound neutral fixations"
side: critic
branch: H
parent: H
edges: [{type: attacks, target: H}, {type: supports, target: H1}]
load_bearing: false  # Fixes the scope of H: the limit is a bound on selected substitutions. Consistent with Day's own 2026-05-07 narrowing (H1). It does not dispute the limit for selected changes.
sourcing: firsthand
status: reviewed
verdicts:
  internal: "holds"
  fidelity: partial
  external: "supported"   # cost bounds selected substitutions; neutral k = U (B0.5). R4 H3: his Matheson 2025 pointer is the right source for the missing selective-death share
---

## Statement (verbatim)
> "noted that selection has a limit, since it imposes a reproductive cost."

Source: Nesslig20, [Response to Will Duffy | PART I - Population Genetics](https://discourse.peacefulscience.org/t/18094), Peaceful Science, 2026-10-05, post 1, section 2.1 "Neutral Theory".

> "Haldane argued that a reasonable 10% of the population can be culled per generation."

Source: same post, §2.1.

> "Haldane’s reproductive cost limit does not apply to drift, but can it account for most of the genomic differences between humans and chimps?"

Source: same post, §2.1 (PS-04 in `sources/quotes-critics.md`).

## Formal statement
Nesslig20 restates Haldane: cost of fixation 30 N_e deaths; 10% of the population can be culled per generation; 30 N_e/(0.1 N_e) = 30/0.1 = 300 generations per beneficial mutation. He then argues the limit does not apply to neutral fixations and computes the neutral count separately (PS-01, PS-02: "[ μ_G = 75 ]" per generation, "~37.8 million", 2 x 75 x 6.3e6/25; the balance ledger notes the factor-of-2 and diploid/haploid slip).
derived: 30/0.1 = 300 (holds). The same ratio results with N or N_e because the factor cancels; Haldane's cost in Nunney's reading is 30N, with N the population size, so the use of N_e is a notational departure with no numerical effect on the 300 (fidelity: partial).

## Assumptions
- Stated: neutral theory handles most fixations; selected fixations obey the cost limit.
- Implicit: that the remaining fixations after the neutral count are within the cost limit; he states "There are other solutions that allow selection to exceed the limit argued by Haldane" and does not use them ("I will stick with neutral theory for now").

## Responses
- Against: Day, in Z19984826 §6.4 (before the retraction): "The defense is partially correct and entirely fails to deliver k = μ." There Day answers the neutral escape by the Term 2 polymorphism ceiling and by the claim that "most substitutions are neutral" is itself downstream of k = μ (H8). After 2026-05-07 (H1) Day concedes Term 3's scope limit.
- In support: Day's retraction (H1) agrees the cost bound is "a constraint on selectively driven substitutions alone".
- Weaknesses in the responses: Nesslig20's neutral rate calculation has its own factor-of-two and ploidy slips (balance ledger); he also states he does not know what d means and ignores it ("I am guessing that it is similar to Haldane's limit of 10%"), although d is defined in Z18166234 (C2a).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Haldane 1957 (via Nunney) | "a typical allelic substitution required about 30N genetic deaths" | the cost is in units of N, not N_e; partial |
| Kimura 1968 | "Calculating the rate of evolution in terms of nucleotide substitutions seems to give a value so high that many of the mutations involved must be neutral ones." | accurate (abstract) |

## Pre-registered prediction
- Under the claimant's model (Nesslig20): neutral fixations are not charged to the cost budget; selected fixations are bounded by about 300 generations each in series.
- Under the opposing model (Day, before the retraction): total k is bounded by the cost term (retracted).
- Result that would change a verdict: none beyond H's check; H6 is a scope statement.

## Check
R4 H/H1 (research/checks/results/R4-H-C2.md): consistent with neutral k = U (B0.5, z = +0.13 / -0.64) and with Day's own 2026-05-07 narrowing (H1). The scope point says nothing about the cost of selected substitutions, which remains open (H). Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)
Earlier note: Script: none (scope claim; covered by H and H1). · Result: not run · Review: pending

R4 H3 (research/checks/results/R4-H3-human.md): 'does not apply to drift' holds. Nesslig20's pointer to Matheson et al. 2025 ('other solutions that allow selection to exceed the limit') is the right source for the missing selective-death share (8.5-95% in one plant; no human value; unrepresentative by the authors' caveat). Matheson's k = 1.1 mapping matches H3's R ~ 1.1. No adaptive count is given. Review: `research/checks/REVIEW.md` (review #7, 2026-10-09).

## Simulator variables implied
Fraction of fixations neutral versus selected; selective mortality budget.
