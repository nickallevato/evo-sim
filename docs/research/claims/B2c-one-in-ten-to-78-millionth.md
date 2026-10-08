---
id: B2c
title: "\"One in ten to the seventy-eight-millionth\": exp(-pi^2 Ne/G) for humans and the many-loci rescue"
side: day
branch: B
parent: B2
edges: [{type: supports, target: B2}, {type: depends-on, target: B2a}]
load_bearing: false  # rhetorical headline number; the load is carried by B2a and B1c
sourcing: firsthand
status: extracted
verdicts:
  internal: holds
  fidelity: unverifiable
  external: contested
---

## Statement (verbatim)
> Carry the exponent to the species in question. For modern humans, Nₑ across the four hundred generations of the current-census era gives Nₑ/T ≈ 1.8 × 10⁷, so the probability that a neutral mutation arising now fixes within that era is of order exp(−π² · 1.8 × 10⁷) — about one in ten to the seventy-eight-millionth.

Source: [Z22129121, The Hard Limits of Fixation Through Genetic Drift (Day & Athos)](https://zenodo.org/records/22129121), Zenodo 2026-08-27 (v1), §The Second Objection

> Ten to the fourteenth against a probability of exp(−π²Nₑ/G) leaves the expected number of completed fixations at ten to the minus seventy-eight-million all the same.

Source: [Z22129121, The Hard Limits of Fixation Through Genetic Drift (Day & Athos)](https://zenodo.org/records/22129121), Zenodo 2026-08-27 (v1), §The Second Objection

## Formal statement
**Arithmetic audit (derived, python3 -I):**
- Nₑ = 7.3e9 (HL Table 3, "census scale"), T = 400: Nₑ/T = 1.825e7 (Day 1.8e7); π² × 1.825e7 = 1.80e8 nats = 7.82e7 decades, i.e. 10^−78,000,000 (matches).
- Destined-to-fix input: 30 × 400 = 12,000 ("some ten thousand"); raw 10^14. Neither moves a 10^7.8e7 exponent.
- **Window mismatch:** the abstract says "within the generations its lineage will ever have" (G), but the computation uses a 400-generation era. With the lineage window G = 260,000 and the same Nₑ: π²Nₑ/G = 2.77e5 nats = 1.2e5 decades; with Wright Nₑ = 4.69e9: 7.7e4 decades; with Yoo ancestral Nₑ (1.98e5 / 1.32e5) and G = 260,000: exp(−7.5) = 5.4e−4 / exp(−5.0) = 6.7e−3; with Nₑ = 1.0e4 (Day's value in IR and the Q&A): exp(−0.38) = 0.68 (outside T ≪ 4Nₑ, so only indicative).
- The raw count is consistent with 8e9 individuals × ~100 new mutations × 400 generations = 3.2e14 (derived), i.e. "about ten to the fourteenth".

## Assumptions
- Stated: Nₑ at census scale for humans; the era of the current census is 400 generations; the one-in-2N chance is already folded into k = μ.
- Implicit: Only mutations arising in the era contribute (ancestral fill is "drainage"); the asymptotic regime T ≪ 4Nₑ holds (400 ≪ 2.9e10, true).

## Responses
- Against: RESULTS B2a/F1: this is a per-allele latency statement; for an equilibrium ancestral population the flux is μ (B1, B2d).
- In support: The arithmetic is internally consistent.
- Weaknesses in the responses: The headline combines two Nₑ conventions: census-scale Nₑ here versus Nₑ = 10⁴ for ancestral humans elsewhere in Day's work. A critic-side counter would need the ancestral fill state (B1c), not a different exponent.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| none cited | n/a | n/a |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: The probability that a neutral mutation arising now fixes within 400 generations is ≈ 10^−7.8e7.
- Under the opposing model: Same exponent; irrelevant to the 252,000-generation divergence, which is dominated by ancestral Nₑ (1.3e5–2e5, Yoo).
- Result that would change a verdict: B1c with Nₑ(t) showing the census-scale era is ≤400 of 252,000 generations would confirm irrelevance for the count; showing a long census-scale era would support relevance.

## Check
Script: none (arithmetic). Audit computed with python3 -I in this session.

## Simulator variables implied
- window T for the exponent
- Nₑ used in the exponent
- era length at current size
