---
id: B3e
title: "Day (2026-02-04): \"corrected\" McCarthy calculation gives 8.25 fixations, shortfall 2,424,242x"
side: day
branch: B
parent: B3
edges: [{type: attacks, target: B5a}, {type: depends-on, target: B3a}]
load_bearing: false  # rebuttal of McCarthy using B3a; falls with B3a
sourcing: firsthand
status: extracted
verdicts:
  internal: non-sequitur
  fidelity: n/a
  external: contradicted
---

## Statement (verbatim)
> Expected fixations: 132 billion × 1/16,000,000,000 = 8.25 fixations

Source: [Day, "Response to Dennis McCarthy, Round 2" (blog)](https://voxday.net/2026/02/04/response-to-dennis-mccarthy-round-2/), 2026-02-04, ¶58 of extracted text

> Thus the shortfall increases from 133x to 2,424,242x when we go from the theoretical to the actual.

Source: [Day, "Response to Dennis McCarthy, Round 2" (blog)](https://voxday.net/2026/02/04/response-to-dennis-mccarthy-round-2/), 2026-02-04, ¶59 of extracted text

## Formal statement
Inputs in the post: Nₑ = 3,300 ("actual ancient effective population size"), N = 8×10⁹, 100 mutations per individual, 400,000 generations, P_fix = 1/2N = 1/(1.6×10¹⁰).

**Arithmetic audit (derived, python3 -I):** 100 × 3,300 = 330,000 per generation ✓; × 400,000 = 1.32×10¹¹ ✓; × 1/1.6×10¹⁰ = 8.25 ✓; 20×10⁶/8.25 = 2,424,242 ✓; 20×10⁶/150,000 = 133.3 ✓.
**Direction check:** the result uses supply ∝ Nₑ and fixation probability ∝ 1/N, i.e. k/μ = Nₑ/N = 4.1×10⁻⁷. The same post's equation is k = μ(N/Nₑ) (B3a), which with the stated N and Nₑ gives k/μ = 2.4×10⁶ (supply from census 8×10⁹, fixation 1/(2Nₑ)); applying that to McCarthy's 20M would give a count ≫ 20M, not 8.25. So the figure does not follow from the post's own equation.
Other items: the "150,000 fixed differences" for McCarthy's model from P(unchanged) = exp(−2NₑμT) is not reproduced by the stated formula (exp(−3×10⁻⁴ × 4×10⁵) = e⁻¹²⁰); N = 8×10⁹ is applied to all 400,000 generations although census-scale N spans a few hundred; Nₑ = 3,300 is a drift-variance estimate from aDNA (branch C; Day later calls Nₑ ≈ 10⁴ circular, B3h).

## Assumptions
- Stated: Supply from 100 × Nₑ individuals; fixation probability 1/(2N) with current N.
- Implicit: Current census applies to all generations; Nₑ = 3,300 is independent of the clock.

## Responses
- Against: "450 billion x 1/20,000 = 22.5 million fixed mutations." ([McCarthy, "Why Probability Zero is Wrong About Evolution" (free repost)](https://dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1), 2026-09-11 (original paid post 2026-01-26), para 52 (McCarthy))
- Against (added 2026-10-09, corpus refresh): Matev, comment on McCarthy "Vox Day Responds" (comment id 345248135, 2026-09-25; RF-3): "He is using a fixation probability of one over sixteen-billion for every single mutation under consideration, including the ones introduced in the first generation after the split." (1/(2 x 8e9) = 1/16e9: the present census applied to mutations that arose when N was far smaller.)
- In support: Day's reproduction of McCarthy's 20M under McCarthy's inputs is arithmetically correct (400e9/20,000 = 20M).
- Weaknesses in the responses: McCarthy uses N = Nₑ = 10,000 and treats all mutations as neutral (B5a). The sign problem above is on Day's side.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| none cited | n/a | n/a |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: 8.25 expected fixations.
- Under the opposing model: With P_fix = 1/(2N) and supply ∝ N: k = μ, 20M-scale counts.
- Result that would change a verdict: n/a (arithmetic and direction audit).

## Check
Script: none. Audit computed with python3 -I in this session. Superseded in principle by Day's own 2026-08-27 concession (B3g).

## Simulator variables implied
- supply N
- fixation-probability N
- window length
