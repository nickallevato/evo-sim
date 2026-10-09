---
id: A4f
title: "Hancock: Day's selective turnover coefficient d has no counterpart in population genetics, is not a selection coefficient, and would cancel if it were a generation count"
side: critic
branch: A
parent: A4
edges: [{type: attacks, target: A4}]   # flipped 2026-10-09 at integration (mapping proposals)
load_bearing: false  # MITTENS 3.0 dropped d (A4d); applies to the book and 2.x versions
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: pending
  external: pending
---

## Statement (verbatim)
> I don't know what D is like there is no equivalent term in population genetics.

Source: [Gutsick Gibbon + Zach Hancock, No, Vox Day's AI-Generated Books Did Not Debunk Evolution](https://www.youtube.com/watch?v=_Vu0ZVVjwHc), 2026-10-03, t=01:20:50 (auto-caption; spelling as captioned; the sentence begins "Yeah").

> if you plugged in 25 there then you also have 25 in the denominator and cancel

Source: same, t=01:21:10 (the sentence continues on the next caption line: "and then you would end up with divergence time divided by fixation rate").

> In population genetics, selection coefficients tend to describe fitness differences between genotypes, whereas day selection coefficient seems to just be a summation of background demographies within populations.

Source: same, t=01:23:35 (host, summarising). The definition itself was relayed in the same video by a friend reading the book: "D is defined as the fraction of the population replaced per time unit" (t=01:22:54) and "per year and he provides no citation for that" (t=01:23:14; the value, captioned "0225", is on the previous line). `secondhand` twice (a text message about page 153 of the book, as read by the host).

## Formal statement
F_max = (t_div x d)/(g_len x G_f) (A). Hancock's hypothetical: if d were a generation count (25) it would cancel g_len = 25 and leave t_div/G_f. Day's d is dimensionless, d = T x (mean mortality force) = 0.45 for humans (A4, ¶51 of Z18166234), so the hypothetical is not Day's d; the cancellation point does show that d and g_len are not independent if d is defined through T. `derived:` with g_len = 25, d = 0.45 gives 0.018/y of mean mortality force (0.45/25), consistent with a mean hazard of order 2% per year (not checked against a life table here).

## Assumptions
- Stated: d must be defined and justified; as presented by Duffy it was not defined on the slide (t=01:22:14).
- Implicit: that the book's definition (fraction of the population replaced per time unit) is the same as the d in the Zenodo paper (T x mean mortality force); that a "selection coefficient" must be a fitness difference between genotypes.

## Responses
- Against (Day): d is defined (Z18166234 ¶33, ¶51; book Ch. 13 and App. A per A4b); d is a ratio of actual to discrete-model allele-frequency change, not a selection coefficient; R4 C2 found d*s exact for hazard-scale s.
- In support: Camestros made the "undefined" point first (A4b) and withdrew it when the definition was located; Hancock's "no equivalent term" survives that withdrawal because it concerns the concept, not the missing definition.
- Weaknesses in the responses: Hancock's critique rests on Duffy's slide and a relayed page number; the cancellation example is a hypothetical, not Day's equation; he says he "ignores" d in the rest of his derivation (t=01:22:34), so nothing downstream depends on it.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Z18166234 s2.3 | d = (Actual allele frequency change per generation) / (Change predicted by discrete-generation model) | accurate (A4) |

## Pre-registered prediction
No new check. A4's R4 C2 already tested the definition.
- Under the claimant (Hancock): no population-genetic quantity equals d.
- Under the opposing model (Day): d is a unit conversion between hazard-scale s and per-generation s (R4 C2).
- Result that would change a verdict: a standard-theory term identical to d (e.g. a generation-time conversion) would support Day's reading that d is bookkeeping, not a new force.

## Check
None beyond R4 C2.

## Simulator variables implied
- None beyond A4.
