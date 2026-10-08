---
id: D12
title: "Keefe & Szostak: four ATP-binding proteins from a library of 6 x 10^12 random 80-mers; frequency similar to RNA libraries"
side: literature
branch: D
parent: D
edges: [{type: attacks, target: D}]
load_bearing: false  # not a premise of ROOT
sourcing: firsthand
status: extracted
verdicts:
  internal: n/a      # 
  fidelity: unverifiable      # abstract only; the numerical frequency is not in the abstract and the full text (PMC4476321) was not read
  external: contested      # binding is not catalysis; function is weak ATP binding after enrichment
---

## Statement (verbatim)
> "Starting from a library of 6 x 1012 proteins each containing 80 contiguous random amino acids, we selected functional proteins by enriching for those that bind to ATP. This selection yielded four new ATP-binding proteins that appear to be unrelated to each other or to anything found in the current databases of biological proteins. The frequency of occurrence of functional proteins in random-sequence libraries appears to be similar to that observed for equivalent RNA libraries."

Source: Keefe AD, Szostak JW (2001) Functional proteins from a random-sequence library, Nature 410:715-718, abstract (`sources/raw/sources/abs/KeefeSzostak2001.txt`; PubMed 11287961). Extraction: '1012' = 10^12.

## Formal statement
Library size M = 6e12; selected functional (ATP-binding) clones = 4. Derived lower bound (this file): if all four were present in the starting library, the frequency of ATP binding among random 80-mers is >= 4/6e12 = 6.7e-13. The paper's own estimate of the frequency is not in the corpus: unsourced here. 20^80 = 1.2e104 sequences in the full 80-residue space (derived).

## Assumptions
- Stated: in vitro selection by mRNA display; ATP binding; unrelated to known proteins.
- Implicit: weak binding counts as function; selection recovers all binders present.

## Responses
- Against (for D): functional proteins from a random library at a frequency orders above the 10^-65 to 10^-77 scale.
- In support (for D): binding is not catalysis; Taylor 2001 (D11) says the ATP-binding case is far easier than catalysis ('many orders of magnitude' smaller library).
- Weaknesses: full text unread.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Keefe & Szostak 2001 abstract | quoted above | accurate |

## Pre-registered prediction
No separate check. Action: read PMC4476321 for the stated frequency.

## Check
Arithmetic only: 4/6e12 = 6.7e-13.

## Simulator variables implied
Functional frequency f for binding vs catalysis.
