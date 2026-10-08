---
id: B4
title: "Molecular clock recalibration: CHLCA collapses from 6-7 Mya to 200-580 kya via N/Ne"
side: day
branch: B
parent: B
edges: [{type: supports, target: B}, {type: depends-on, target: B3a}]
load_bearing: false  # a consequence of B3a, which Day withdrew on 2026-08-27; MITTENS counts (A) use 252,000 generations regardless
sourcing: firsthand
status: extracted
verdicts:
  internal: holds
  fidelity: unverifiable
  external: contested
---

## Statement (verbatim)
> The consensus molecular clock estimate of 6–7 Mya collapses to 200–580 kya, with the most plausible demographic parameters yielding 200–360 kya.

Source: [Z18525547, The N/N_e Distinction and the Recalibration of the Human-Chimpanzee Divergence (Day & Athos)](https://zenodo.org/records/18525547), Zenodo 2026-02-08 (v1), ¶4 of extracted text. abstract

> t_{actual} = t_{clock} × 2 / [(N_{h}/N_{e,h}) + (N_{c}/N_{e,c})]          (7)

Source: [Z18525547, The N/N_e Distinction and the Recalibration of the Human-Chimpanzee Divergence (Day & Athos)](https://zenodo.org/records/18525547), Zenodo 2026-02-08 (v1), ¶141 of extracted text

## Formal statement
D = μ t [(N_h/N_e,h) + (N_c/N_e,c)] (Eq. 6) set equal to the clock's D = 2μ t_clock ⇒ Eq. (7). Inputs: Nₑ,h = 3,300 (aDNA drift variance, branch C), Nₑ,c = 33,000 (F_ST across chimp subspecies), census N_h ∈ {50k, 100k}, N_c ∈ {300k, 1M}.

**Arithmetic audit (derived, python3 -I):** Table 2 of the paper reproduces: (100k,300k): N/Nₑ = 30.3 + 9.1 → 305/355/457 kya for clock 6/7/9 My ✓; (100k,1M): 198/231/297 ✓; (50k,300k): 494/577/741 ✓ (paper 494/577/741); (50k,1M): 264/308/396 ✓. "200–580 kya" is the 6–7 My clock range (min 198, max 577); the 9 My column reaches 741.
**Input sensitivity (derived):** the two parameter sets Day uses for the same human census range disagree: here Nₑ,h = 3,300 for N = 100,000 (N/Nₑ = 30), while Z22129121 and the 2026-10-01 post imply Nₑ = 0.57 N (57,000). With Yoo 2025 ancestral Nₑ (198,000 / 132,000) and census 100,000 the ratio is 0.51 / 0.76 per lineage and Eq. (7) gives 12.5 / 8.3 My (older, not younger) for a 6.3 My clock. Also, Eq. (7) assumes constant N/Nₑ over the whole window.
The paper's later claim "Ne ≤ N by definition" (Z18637333) is not a definition: Wright's formula Nₑ = (4N−2)/(Vₖ+2) gives Nₑ ≈ 2N at Vₖ = 0.

## Assumptions
- Stated: k = μ(N/Nₑ) (B3a), with clock-independent Nₑ.
- Implicit: Constant N/Nₑ over millions of years; one census figure per lineage; the same fixation-probability premise that Day retracted on 2026-08-27 (B3g).

## Responses
- Against: "the neutral theory of evolution cannot explain common ancestry between humans and chimps at all based on genome-wide nucleotide differences between the two species, since the neutral theory is used in the first place to date the assumed time of divergence." ([Hossjer, "MITTENS - Convincing Arguments Against Neo-Darwinism" (PDF attached to Dembski post)](https://billdembski.substack.com/api/v1/file/f5a8533e-7b7c-407b-880b-1ecbd256784c.pdf), 2026-09-14, PDF p5 (Hössjer; he agrees the dating is neutral-theory based, but takes k = dμ with census N))
- In support: Keightley 2012: pedigree μ about twofold lower than divergence-based estimates (k > μ in direction, ×2 not ×15–150); keruru (KR-05): "closer to twice that".
- Weaknesses in the responses: Hössjer does not adopt k = μN/Nₑ; keruru's observation is about a factor 2 and he calls it unreconciled. The dependence on Z18525547's Nₑ,h = 3,300 is branch C.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Frankham 1995 (cited for N > Nₑ) | not retrieved | unverified |
| Takahata 1993; Harpending 1998 (cited for Nₑ ≈ 10⁴) | not retrieved | unverified |
| Langergraber 2012 | "We date the human-chimpanzee split to at least 7-8 million years" | verified-misread when cited as 6–7 My (ledger) |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: Divergence time 15–150× shorter than the clock date.
- Under the opposing model: With P_fix = 1/(2N) the clock rate is μ and Eq. (7) reduces to t_actual = t_clock.
- Result that would change a verdict: A reproduction of the Nₑ,h = 3,300 estimate from drift variance under a model that includes structure (branch C).

## Check
Script: none (arithmetic audit above, python3 -I). Direct simulation of two-lineage divergence: B4a (proposed).

## Simulator variables implied
- t_clock
- census N per lineage
- Nₑ per lineage
- N/Nₑ held constant or varying
