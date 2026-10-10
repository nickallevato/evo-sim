---
id: B2b
title: "Census ceiling X = (Vk + 2) G / 16 from 4Ne < G"
side: day
branch: B
parent: B2
edges: [{type: supports, target: B2}]
load_bearing: true  # X is the ceiling quoted in the abstract and in Day's blog replies
sourcing: firsthand
status: extracted
verdicts:
  internal: holds
  fidelity: unverifiable
  external: contested
---

## Statement (verbatim)
> Nₑ = (4N − 2) / (Vₖ + 2)

Source: [Z22129121, The Hard Limits of Fixation Through Genetic Drift (Day & Athos)](https://zenodo.org/records/22129121), Zenodo 2026-08-27 (v1), p.4 (§The Census Ceiling)

> For a large, long-lived vertebrate the effective ceiling falls to about ten thousand individuals.

Source: [Z22129121, The Hard Limits of Fixation Through Genetic Drift (Day & Athos)](https://zenodo.org/records/22129121), Zenodo 2026-08-27 (v1), p.1 (abstract)

> The human’s is thirty-five thousand as a species, a hundred thousand as a lineage. The elephant’s is twenty-eight thousand.

Source: [Z22129121, The Hard Limits of Fixation Through Genetic Drift (Day & Athos)](https://zenodo.org/records/22129121), Zenodo 2026-08-27 (v1), p.6

## Formal statement
4Nₑ < G with Nₑ = (4N−2)/(Vₖ+2) ≈ 4N/(Vₖ+2) ⇒ N < (Vₖ+2)G/16 = X. G = T_years / g_years.

**Arithmetic audit (derived, python3 -I):**
| Species | T (My), g (y), Vₖ | G | X recomputed | Day's X | census / X |
|---|---|---|---|---|---|
| Homo sapiens (lineage) | 6.5, 25, 5 | 260,000 | 113,750 | 114,000 | 8.2e9/113,750 = 72,088 (Day 72,000) |
| H. sapiens (species window) | 2.0, 25, 5 | 80,000 | 35,000 | 35,000 | 234,286 |
| Loxodonta | 2.0, 22, 3 | 90,909 | 28,409 | 28,000 | 14.6 (Day 15) |
| Mus musculus | 1.5, 0.5, 25 | 3.0e6 | 5.06e6 | 5.1e6 | 1,975 |
| D. melanogaster | 5.0, 0.08, 400 | 6.25e7 | 1.57e9 | 1.57e9 | 637 |
Table 2 (Vₖ halved/doubled) also reproduces: human 22,500/60,000; elephant 19,886/45,455; mouse 2.72e6/9.75e6; fly 7.89e8/3.13e9.
Discrepancies: (i) the abstract's "about ten thousand" is 3.5–11× below the table's human ceilings (35,000–114,000) and 2.8× below the elephant's; (ii) with Vₖ = 5 Wright's formula gives Nₑ = 0.57 N, so the paper treats census 8.2e9 as Nₑ ≈ 4.7e9, whereas Z18525547 and the Q&A use Nₑ = 3,300–10,000 for the same census (N/Nₑ = 800,000 in the 2026-04-30 post); (iii) mouse and fly Vₖ and census values are flagged "original estimates pending a proper source".

## Assumptions
- Stated: Variance Nₑ is the relevant quantity; the lineage duration is the window; Vₖ is the least certain input (sensitivity table given).
- Implicit: Panmictic, constant size over G; mean time is the criterion (the tail is handled in B2a); Wright's formula applies with a single Vₖ for the species.

## Responses
- Against: "Genetic drift happens in every population and his claim otherwise is mystifying. Population size only affects which alleles are effectively neutral." ([Mansfield (@brianmansfield6912), YouTube comments under Examining Origins video jDxFtCOGZ3A](https://www.youtube.com/watch?v=jDxFtCOGZ3A), comments retrieved 2026-10-07; terminus ante quem 2026-10-01: Day quotes this comment in "The Education of a Population Geneticist", ¶8 (added 2026-10-08), comment UgyhNduYke46IStQ5pd4AaABAg (Mansfield))
- In support: HL pre-empts three objections (window, parallelism, demes) in the text; Maruyama's invariance is cited for demes.
- Weaknesses in the responses: Mansfield addresses Day's earlier blog sentence, not this derivation. Neither side has checked the Vₖ = 5 value for humans against Hill (1972) or the demographic literature (not retrieved).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Wright (Nₑ formula) | Nₑ = (4N−2)/(Vₖ+2) as printed in HL p.4; original not retrieved | unverified |
| Hill 1972 (human Vₖ route per HL) | not retrieved | unverified |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: Every listed vertebrate census exceeds its X.
- Under the opposing model: If Nₑ/N is the empirical 0.1 (Frankham) or the human ≈ 10⁻³ ratio, the ceiling inequality is evaluated at different Nₑ and the comparison changes only by the factor Nₑ/N used.
- Result that would change a verdict: A sourced Vₖ(human) and an independent Nₑ(t) would settle the inputs; no check is queued for this sub-claim beyond B2a/B1c.

## Check
Script: none specific (arithmetic only). Audit computed with python3 -I in this session. Related: B3a (Nₑ vs N).

R4 B2b (research/checks/results/R4-B2b.md; review #21, 2026-10-09): simulated N_e (Cannings, Mendelian segregation, iid offspring variance) matches Wright's (4N-2)/(V_k+2) to within 2.2% at V_k = 1, 2, 5, 10, so X = (V_k+2)G/16 is correct algebra. The abstract's "about ten thousand" is reached only at V_k = 0 with the 2-My window; N_e/N = 1e-3 would need V_k about 4,000. Inputs (human V_k, G window) not tested. Verdicts unchanged.

## Simulator variables implied
- Vₖ
- generation time
- lineage duration
- census N
- Nₑ/N mapping (Wright formula | fixed ratio | user)
