---
id: H4
title: "Worden's O(1) bits per generation is exactly the Haldane-scale limit, and the square-root argument for parallel fixation concerns purging, not fixing, mutations"
side: day
branch: H
parent: H
edges: [{type: supports, target: H}]  # H4 -> G1 removed 2026-10-08: G1 is Day's own claim; H4 answers commenter 'Eugine' at Tree of Woe (sqrt(N) argument), who has no node (argmap registry x:eugine-sqrtN)
load_bearing: false  # A short reply to a commenter; the quantitative claim ("exactly the same") is asserted, not derived. Only relevant if parallel fixation is used to escape H.
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: unverifiable
  external: contested
---

## Statement (verbatim)
> "Worden’s O(1) bits per generation. Yudkowsky doesn’t refute it. And O(1) bits per generation is exactly the the same as the Haldane-scale limit."

Source: Day, [A First Challenge](https://voxday.net/2026/01/10/a-first-challenge/), B2026-01-10-a-first-challenge, posted 2026-01-10, para 9 (the "the the" is in the source). Day is answering a commenter, "Eugine", at Tree of Woe ("An atheist named Eugine at Tree of Woe", ¶2) who cited a LessWrong summary ("Speed limit and complexity bound for evolution").

> "Haldane’s limit isn’t about purging bad mutations, it is about the cost of substituting good ones. Each beneficial fixation still requires selective deaths to drive it to fixation."

Source: same post, para 7.

> "The sqrt(N) trick helps with mutational load, not with the speed of adaptation."

Source: same post, para 8.

## Formal statement
Worden 1995 (as paraphrased by Day; the text was not retrieved): the information gain from selection is bounded by O(1) bits per generation. Day's equivalence: Haldane's limit (one substitution per 300 generations) equals O(1) bits/generation. The sqrt(N) argument (Yudkowsky/LessWrong summary, via the commenter): with truncation selection on total mutational load, the population can purge of order sqrt(N) mutations per generation; Day: this concerns deleterious load, not beneficial fixation.

derived (R2, units): O(1) bits per generation, with the constant unspecified, equals Haldane's 1/300 substitutions per generation (0.0033/gen) only if each substitution carries about 300 bits (if one substitution is one bit the limit is 300 times faster). The equivalence is therefore not established by the sentence quoted; it depends on how many bits a substitution represents. Link to H: the Haldane argument counts deaths (30 N per substitution), the Worden argument counts information; they coincide numerically only under a stated conversion that Day's post does not give.

## Assumptions
- Stated: Haldane's limit is about substituting good mutations; the sqrt(N) trick requires truncation selection and random mating.
- Implicit: O(1) is the same order as 1/300; truncation selection on total mutation count is what the opposing argument needs (Day lists the objections: phenotype, structured mating).

## Responses
- Against: the commenter's LessWrong source (not retrieved); Nunney (H2) for the cost; Keightley (H7), who discusses quasi-truncation selection (Crow & Kimura 1979) as a candidate load-reducing mechanism for deleterious mutations.
- In support: Day's reading that purging and fixing are different problems is consistent with Nesslig20's separation of cost from drift (H6).
- Weaknesses in the responses: Worden 1995 and the LessWrong post are not in the corpus; no critic engaged Day's reply.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Worden 1995, "A speed limit for evolution" (J Theor Biol) | not retrieved | unverifiable |
| LessWrong summary (Yudkowsky) | not retrieved | unverifiable |
| Maynard Smith 1968 (truncation selection) | not retrieved | unverified |

## Pre-registered prediction
- Under the claimant's model: with beneficial substitution under hard selection, the information gain per generation is bounded by O(1) bits and the substitution rate by about one per 300 generations.
- Under the opposing model: truncation or soft selection lets many loci move at once without paying 30 N deaths each; the O(1) bits bound applies to the selective-variance budget, which sets an upper limit on the sum of s_i per generation, not on the number of substitutions when s_i are small and many loci move together.
- Result that would change a verdict: the Worden paper's bound in its own units, with the per-substitution information content (log2 of the frequency change from p = 1/(2N) to 1, about log2(2N)) shown explicitly; and the H simulation with an explicit sum-of-s accounting.

## Check
Script: `research/checks/h_cost_of_selection.py` (planned, H). · Result: not run · Review: pending

## Simulator variables implied
Number of concurrent sweeps, sum of s_i, selection mode (truncation versus proportional), mating structure.
