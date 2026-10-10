---
id: D15
title: "Hössjer (prediction): the waiting time for several genes to change expression through coordinated regulatory mutations 'far exceeds 9 million years'; for an orphan gene, 'many orders of magnitude larger'"
side: ally
branch: D
parent: D
edges: [{type: supports, target: D}]  # judgement: D holds the corpus's target-search / waiting-time arguments. Hössjer's conclusion is uncommon descent (HO-10), not Day's guided common descent
load_bearing: false  # ROOT does not depend on it; R5-draft lists 30 load-bearing nodes and D15 is not among them (its one ally node is H5). R4-D15 was reviewed at the three-review tier by choice, which does not change this flag (reconciled at integration 2026-10-10)
sourcing: firsthand
status: reviewed
verdicts:
  internal: holds        # computed by this audit (R4-D15), not by the author, on his own 2021 model: for a specific target (d_max = 0, new site) with non-beneficial intermediates, 96/96 in-scope cells give p9 = 0 and p90 <= 0.017. Rule basis R4-X1 s0 + C + N1. Alternative recorded (critic m3): n/a under a strict S1 reading (Statement plus derivation only; no derivation is given), with the sweep moved to external; same evidence either way. N2d answered: his Table 5 d_max = 1 rows are sites already present; from an absent start they give 114-172 My
  fidelity: accurate     # his p.7 description of his own 2021 model checked against the paper (local PDF); he does not attribute the 'far exceeds' figure to the paper. Critic alternative: partial (the paper's d_max = 1 rows give ~1 My and are not mentioned); a scope point carried in the internal comment and external column. Reviewers may prefer partial; disagreement recorded
  external: contested    # PROVISIONAL. Supported under the claimant's stated premises (specific target, non-beneficial intermediates); contested because those premises are unsourced on both sides and the answer flips under beneficial intermediates (S2/S3), redundant sites (kmult >= 10) or a non-specific gene set (any m of M >= ~1,000). A sensitivity of this audit's grid, not a sourced rebuttal: no critic in the corpus engages HO-12. N_e = 1e5 cells carry the R4-X1 F contested-standard flag. Day-steelman option (a) supported (conditional) not adopted (premises unsourced). Literature leads in gaps RG-02 could move it
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
R4 D15 (research/checks/results/R4-D15.md; script `research/checks/d15_waiting_time.py` pre-registered b74b6d6 (post hoc f=3 amendment 639b94b); 714-cell sweep on na-workhorse, 2026-10-09/10; three Opus reviews #26-#28, no BLOCKER; fix pass 3b88bbb adds the post hoc analysis `d15_posthoc.py`): Hössjer's 2021 model is reproduced against his tables (about 0.3%). **In scope** (his stated premises: several genes m >= 2, a specific site kmult <= 1, neutral or valley intermediates; 96 cells, both N_e, both rho): 96 of 96 exceed 9 My (p9 = 0), 96 of 96 far exceed it (p90 <= 0.017), at 20 y and at 25 y per generation. **Outside that scope the answer flips**: +1% per-step intermediates (S2) reach 9 My in 57-77% of replicates at kmult = 1, N_e = 1e4 (100% at kmult >= 3 and at N_e = 1e5); redundant sites (kmult >= 10, a non-specific site class); a non-specific gene set (any m of M, closed form PH-F, matters from M of order 1,000); and his own Table 5 d_max = 1 rows (sub-9-My) describe sites already present (from an absent start they give 114-172 My). At N_e = 1e5 neutral cells carry an omitted fixation sojourn of about 4N_e generations (about 10 My); the chain-vs-simulation excess is that sojourn, not an f = 10 artefact. The three inputs that decide it, none supplied by any source in the corpus: equivalent sites (kmult / d_max), whether intermediates were beneficial, and which genes. Tag (rule RH): HO-12 is dialectic. Literature leads (Stone & Wray 2001; MacArthur & Brookfield 2004; Durrett & Schmidt 2007; Khaitovich et al. 2004; Schmidt et al. 2010) are unverified titles from a reviewer's memory, recorded in `ledgers/gaps.md` RG-02, not relied on. Not stored: per-replicate times (other windows cannot be computed without a rerun). Optional runs proposed, not launched. Reviews: `results/REVIEW-R4-D15-{correctness,steelman-day,steelman-critic}.md`.

## Simulator variables implied
Number of target genes; binding-site length and number of acceptable motifs; N; μ; fitness of intermediates (neutral vs deleterious); recombination.
