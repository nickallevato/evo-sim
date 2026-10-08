---
id: B4b
title: "CHLCA recalibrated from 6.5 Mya to 68 kya (census 600,000; Biraben 2003)"
side: day
branch: B
parent: B4
edges: [{type: revises, target: B4}]
load_bearing: false  # extreme end of the recalibration; superseded by the 2026-05-07 revision (B4c)
sourcing: firsthand
status: extracted
verdicts:
  internal: holds
  fidelity: unverifiable
  external: contested
---

## Statement (verbatim)
> recalibrates the CHLCA from 6.5 Mya to 68 kya

Source: [Z18637333, The End of Evolutionary Deep Time (Day & Athos)](https://zenodo.org/records/18637333), Zenodo 2026-02-14 (v1), ¶6 of extracted text. abstract

> At the midpoint of 600,000, the consensus molecular clock date of 6.5 Mya compresses to 68 kya.

Source: [Z18637333, The End of Evolutionary Deep Time (Day & Athos)](https://zenodo.org/records/18637333), Zenodo 2026-02-14 (v1), ¶105 of extracted text

## Formal statement
Same Eq. (7) with N_h = 600,000 (Biraben 2003), N_c = 300,000, Nₑ,h = 3,300, Nₑ,c = 33,000: N_h/Nₑ,h = 181.8, N_c/Nₑ,c = 9.1; t = 2 × 6.5 My / 190.9 = 68.1 kya ✓ (derived). Alternate census 100–300k: 330–130 kya ✓ (paper "130–330 kya").
Differences from Z18525547 (one week earlier): human census 600,000 vs 50–100k; clock date 6.5 vs 6–7 (9); outputs 68 kya vs 198–741 kya.

## Assumptions
- Stated: Census 500,000–700,000 for the whole Homo ergaster/erectus lineage (Biraben 2003) is the right N for mutation supply.
- Implicit: Same as B4; plus that a census spanning many contemporaneous subspecies all contribute to the ancestral lineage's supply while drift acts at Nₑ,h = 3,300.

## Responses
- Against: See B4 and B3g.
- In support: n/a
- Weaknesses in the responses: Biraben (2003) not retrieved; the ≤ definition claim is incorrect (see B4).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Biraben 2003 (as cited) | 500,000–700,000 total hominids (as cited by Day) | unverified |
| Sjödin et al. 2012 (as cited) | 100,000–300,000 H. sapiens census (as cited by Day) | unverified |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: 68 kya.
- Under the opposing model: No recalibration (B3g).
- Result that would change a verdict: n/a

## Check
Script: none. Arithmetic computed in python3 -I.

## Simulator variables implied
- census N per lineage
