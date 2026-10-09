---
id: D15
title: "Hössjer (prediction): the waiting time for several genes to change expression through coordinated regulatory mutations 'far exceeds 9 million years'; for an orphan gene, 'many orders of magnitude larger'"
side: ally
branch: D
parent: D
edges: [{type: supports, target: D}]  # judgement: D holds the corpus's target-search / waiting-time arguments. Hössjer's conclusion is uncommon descent (HO-10), not Day's guided common descent
load_bearing: false  # a stated prediction with no numbers; ROOT does not depend on it
sourcing: firsthand
status: extracted
verdicts:
  internal: pending      # no calculation is given; the cited model "has not yet been applied to humans and chimps"
  fidelity: pending      # Hössjer, Bechly & Gauger 2021 (J. Theor. Biol. 524:110657) not retrieved
  external: pending      # no parameters stated (number of genes, binding-site length, N, mu)
---

## Statement (verbatim)
> Although this mathematical model has not yet been applied to humans and chimps, my prediction is that the waiting time for several genes to change expression (so that their expressions match that of humans rather than chimps) far exceeds 9 million years.

Source: [Hössjer, MITTENS - Convincing Arguments Against Neo-Darwinism (PDF attached to Dembski post)](https://billdembski.substack.com/api/v1/file/f5a8533e-7b7c-407b-880b-1ecbd256784c.pdf), 2026-09-14, PDF p.8 (the sentence follows the model description that begins on p.7), §6 "Functional differences and uncommon descent" (HO-12). Local copy `sources/raw/critics/hossjer-mittens-review.pdf`.

> the waiting time for evolution (guided or not) to produce an orphan gene is most likely many orders of magnitude larger than 9 million years.

Source: same PDF, p.8, §6 (HO-13).

The model he refers to (p.7, the sentence continuing on p.8 after the footnotes): "In collaboration with the late Günter Bechly and Ann Gauger, in 2021 I developed a mathematical model for the time it would take for several genes to change expression through coordinated mutations, when new binding sites appear and transcription factors can recognize and attach to these new binding sites." His footnote 14 cites Hössjer, Bechly & Gauger (2021), "On the waiting time until coordinated mutations get fixed in regulatory sequences", *Journal of Theoretical Biology* 524, 110657.

## Formal statement
Prediction: E[T_wait(coordinated binding-site changes at several genes)] ≫ 9 My (450,000 generations at 20 y, the 2019 / book figures Hössjer uses). No number of genes, binding-site length, population size, mutation rate or selection model is given in the review, so no value can be computed from the text. The 9 My is Day's "generous" book figure. Hössjer's footnote 1 gives 6–8 My as the common view, and MITTENS 3.0 uses 6.3 My (A1). A shorter window makes the prediction easier to satisfy.

## Assumptions
- Stated: the target is coordinated expression change at "several genes" (a network; "often (close to) irreducibly complex", p.8); evolution "typically proceeds in small incremental steps" whose intermediates "would most likely have low fitness" (p.8).
- Implicit: a pre-specified target (the human expression state), as in the specific-vs-any question (G3); low-fitness intermediates; no standing variation in binding sites.

## Responses
- Against: none in the corpus. No critic engages Hössjer's waiting-time prediction or his 2021 model. The gaps ledger (S24) records that the waiting-time literature in the corpus (Hancock 2024, on Behe & Snoke, Lynch and Sanford 2015) predates MITTENS and does not address Hössjer 2021.
- In support: none beyond Hössjer. Day does not cite this prediction. Day's own view is guided common descent (HO-10 context), and Hössjer's "(guided or not)" for orphan genes applies to that view as well.
- Weaknesses: stated as a prediction, not computed ("has not yet been applied to humans and chimps"). The target is specified in advance, the same issue G3 raises for Day's Darwillion. The intermediate-fitness premise is asserted.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Hössjer, Bechly & Gauger 2021, J. Theor. Biol. 524:110657 | not retrieved | pending |
| Ruiz-Orera et al. 2015, PLoS Genet. 11:e1005721 (orphan genes, his fn. 13) | not retrieved | pending |

## Pre-registered prediction
No check is specified. A check would need the 2021 model's parameters, applied to a human-lineage N, μ and window: the number of genes, the binding-site length and the required matches. It would compare E[T_wait] with 252,000–450,000 generations.
- Under the claimant's model: E[T_wait] ≫ 450,000 generations.
- Under the opposing model: not stated by any critic in the corpus.
- Result that would change a verdict: a computed E[T_wait] from the 2021 model with human parameters.

## Check
None.

## Simulator variables implied
Number of target genes; binding-site length and number of acceptable motifs; N; μ; fitness of intermediates (neutral vs deleterious); recombination.
