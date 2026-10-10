---
id: B2
title: "Hard Limits: drift cannot complete fixations above a census ceiling; the domain of k = mu is empty for large vertebrates"
side: day
branch: B
parent: B
edges: [{type: supports, target: B}, {type: depends-on, target: B2a}, {type: depends-on, target: B2b}, {type: depends-on, target: B2c}]
load_bearing: true  # with B1 it is the other route by which the neutral escape is closed; if both fail ROOT as worded fails
sourcing: firsthand
status: reviewed
verdicts:
  internal: holds   # R4 B2: the HL abstract confines the claim to current size (l.23-25, Q140: "not produced at their current size; it is residual drainage from the smaller populations they descend from"), so "The domain of k = mu is confined to demographic conditions that no non-endangered species is capable of meeting" holds on HL's own text; rule C not needed. Definition k(T) = mu F(T), F = P(tau <= T | fixation) (Q147); abstract and l.329-331 unconditional wording is rule C, 1/(2N) gap R1-immaterial
  fidelity: unverifiable   # R4 B2: unchanged (uncited inputs, rule F).
  external: contested
---

## Statement (verbatim)
> Checking them yields a hard ceiling on population size, X = (Vₖ + 2)·G/16 — reproductive variance and lineage generations alone, with no mutation rate, no coalescent quantity, and no fitted constant.

Source: [Z22129121, The Hard Limits of Fixation Through Genetic Drift (Day & Athos)](https://zenodo.org/records/22129121), Zenodo 2026-08-27 (v1), p.1 (abstract)

> The domain of k = μ is confined to demographic conditions that no non-endangered species is capable of meeting.

Source: [Z22129121, The Hard Limits of Fixation Through Genetic Drift (Day & Athos)](https://zenodo.org/records/22129121), Zenodo 2026-08-27 (v1), p.1 (abstract)


RH tag (2026-10-10 pass): dialectic (stated as a checkable claim or derivation; no rhetorical device scored).
## Formal statement
Summary (the pieces are B2a, B2b, B2c, B2d): 4Nₑ < G ⇒ N < X = (Vₖ+2)G/16; above X, P(τ ≤ G | fixation) ~ exp(−π²Nₑ/G).

The paper contains no reference list in the harvested copy (balance ledger), and cites Kimura & Ohta 1969, Wright, Hill 1972 and Maruyama 1970/74 in the text only. `parameters.yaml` has no entries for Vₖ or census N; propose `new: population.Vk_human = 5` (HL Table 1) and `new: population.census_human = 8.2e9` (HL Table 1).

## Assumptions
- Stated: k = μ is accepted ("this paper accepts it throughout"); the mean fixation time 4Nₑ is the transit time; Nₑ is the variance effective size; Wright's Nₑ = (4N−2)/(Vₖ+2).
- Implicit: A mean time (4Nₑ) is a deadline unless the tail is quantified (addressed by B2a); the lineage window G is the relevant window (but the paper's 78-million exponent uses a 400-generation window, B2c); the pipe is empty at the start of the window (B1c/B1d).

## Responses
- Against: "Genetic drift happens in every population and his claim otherwise is mystifying. Population size only affects which alleles are effectively neutral." ([Mansfield (@brianmansfield6912), YouTube comments under Examining Origins video jDxFtCOGZ3A](https://www.youtube.com/watch?v=jDxFtCOGZ3A), comments retrieved 2026-10-07; terminus ante quem 2026-10-01: Day quotes this comment in "The Education of a Population Geneticist", ¶8 (added 2026-10-08), comment UgyhNduYke46IStQ5pd4AaABAg (Mansfield; replying to a Day blog sentence about drift at large N, not to HL))
  RESULTS B2a: the exponent is a per-allele latency tail, not a throughput bound.
- In support: RESULTS B2a: the exponent −π² is the correct leading-order short-time asymptotic. Day's own simulation reproduces the mean time (391 vs 400).
- Weaknesses in the responses: Mansfield's comment predates HL and is aimed at a different statement. Day's abstract summary "about ten thousand" is not what the paper's table gives (35,000–114,000, B2b). The two sides have not met on the fill-state question (B1c).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura & Ohta 1969 | "takes about 4Ne generations until it spreads to the whole population" (p.766) | accurate |
| Maruyama 1970/1974 (cited by HL, third objection) | not retrieved (abstract only for 1970) | unverified |

## Pre-registered prediction
Written **before** the check runs.
- Under the claimant's model: k(T) = μF(T) with F exponentially small for T ≪ 4Nₑ.
- Under the opposing model: For a population at equilibrium the flux is μ regardless of transit time (B1, B1b).
- Result that would change a verdict: See B2a (exponent), B2b (ceiling inputs), B1c (fill state).

## Check
See child claims. Script: `research/checks/b2a_hard_limits_chain.py`, `research/checks/b2a_scaling.py` · Result: see B2a. Review: `research/checks/REVIEW.md#2026-10-07--review-3-sonnet-correctness--two-sided-steelman-of-b1b-b2a-f1`

R4 B2 (`research/checks/results/R4-B2.md`; pre-registered 3d07343; three load-bearing reviews #37-#39 at f55e1ca; fix pass 45edb6f; post hoc `b2_posthoc.py`): P1 holds (definition found, Reading 1); P2 holds (the exact 2N = 200 chain reproduces Day's WF demonstration: conditional mean 396.5 vs 391, 1.4 SE; 9.3 of 3,000 expected by t = 100, Day's six inside the Poisson range); P3 holds (the asymptotic law understates the exact F by a power-law prefactor, 17.8-47x at T = 2N_e to N_e, not an order-one constant; Day's 'two orders' is slip S-B2-1, about 11 decimal orders at H5, R1-immaterial); P4 holds (7.8e7 decimal orders); P5 holds. P6 failed on two sub-parts (exact F 0.029 vs the 0.05-0.30 range, ratio 33 vs 50): Day's linear bound was 'generous', as he said (0.029 vs 0.35). P7's numeric part failed (F = 0.95 at 1e4, 2 My). Flux and delivered fraction (1/T)int F: H8 census 1e5 over 2 My 0.026 / 0.003; over HL's own accepted 6.5 My window 0.70 / 0.26; field N_e 1e4 over 2 My 0.95 / 0.51. Day side: definition, exponent, X algebra and the 600,000-run demonstration all hold; HL argues its variance N_e (l.101-118, Q142), so the field's 1e4 is not HL's input. Critic side: HL concedes the steady-state flux (Q146), the drainage (Q140), a partial ancestral load (Q156) and 'pipe substantially fills' (Q152); the critics' latency-not-throughput reply (B2a) was right on the mechanics; on HL's own 6.5 My window the H8 input fills to 0.70, and Day's later reply (B1d, Q160) grants a full pipe at the split. Slips S-B2-1..4 and RH-8 in the ledger. Verdict change: internal pending -> holds.

## Simulator variables implied
- Vₖ
- G (lineage generations)
- census N and Nₑ definition (variance/coalescent)
- window T
- fill state
