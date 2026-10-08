---
id: D2a
title: "Ulam: 'What I am going to do will come to Eden's conclusions'; Ulam is an ally of Eden, not of the biologists"
side: day
branch: D
parent: D2
edges: [{type: attacks, target: D4a},{type: depends-on, target: D4}]
load_bearing: false  # D is not required for ROOT
sourcing: firsthand
status: extracted
verdicts:
  internal: n/a      # fidelity question first
  fidelity: partial      # quoted sentence not found; nearest text says the opposite about magnitude; substance (Ulam finds the rate problem real) supported at pp.24-25
  external: contested      # 
---

## Statement (verbatim)
> "Ulam explicitly states: “What I am going to do will come to Eden’s conclusions.”"

> "He also says, in the discussion, “In contrast to the tone of the discussion I took, personally, I believe that the numbers I took are very optimistic”—meaning he believes the real situation for neo-Darwinism is worse than his model suggests"

Source: [The Best They've Got I](https://voxday.net/2026/10/05/the-best-theyve-got-i/), 2026-10-05, voxday.net, para 9, Day's quotations of the Wistar transcript.

What the volume contains (Moorhead & Kaplan (eds), *Mathematical Challenges to the Neo-Darwinian Interpretation of Evolution*, Wistar Institute Monograph No. 5 (1967; symposium 25-26 Apr 1966), local copy = 1985 Liss reprint scan, OCR text; page = printed folio (OCR garbles noted in place)):

> "will not come to be as fantastically small as in Professor" [page break, p.22 -> p.23] > "Eden's conclusions; but we will come to that later."
— Ulam, p.22-23. Raw text lines 2008-2011.

> "This calculation is illustrating something that I think Professor Eden had in mind."
— Ulam, p.24.

> "In contrast to the tone of the discussion I, personally, believe that the numbers I took are very optimistic rather than the opposite."
— Ulam, p.25.

## Formal statement
Day's claim: Ulam's computation reaches Eden's conclusion. Ulam's text: his 'final probabilities, even if we assume some values from the present guesses, will not come to be as fantastically small as in Professor Eden's conclusions' (p.22-23), yet the calculation 'is illustrating something that I think Professor Eden had in mind' (p.24) and he 'personally' believes the numbers 'very optimistic rather than the opposite' (p.25). Ulam's own result is a rate, 10^13 generations (D4), not Eden's 10^-273.

## Assumptions
- Stated: Ulam's contribution should be read as supporting Eden.
- Implicit: the direction of the disagreement (evolution too slow) is the relevant parallel; magnitudes need not match.

## Responses
- Against: the verbatim sentence Day attributes to Ulam is not in the OCR text of the volume: searches for 'come to Eden', 'Eden's conclusions', 'conclusions' return only the p.22-23 passage above, which states that Ulam's probabilities will NOT be as small as Eden's. Day's quote looks like a splice of 'What I am going to do will con-[sist]' (p.21-22) with 'come to ... Eden's conclusions' (p.22-23). OCR error cannot be excluded for a spliced sentence of this length, but the physical copy Day says he consulted would settle it.
- In support: pp.24-25 support the substance: Ulam says his calculation illustrates what Eden had in mind and that his numbers are optimistic. Day's own quotation of p.25 differs from the printed text ('discussion I took, personally, I believe' vs 'discussion I, personally, believe').
- Weaknesses: Rosenhouse's reading (Ulam 'was not challenging the fundamental soundness') is also a reading, not a quote; both sides interpret.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Wistar p.22-23 | 'will not come to be as fantastically small as in Professor Eden's conclusions' | contradicts the magnitude implied by Day's sentence |
| Wistar p.24 | calculation 'illustrating something that I think Professor Eden had in mind' | supports direction |
| Wistar p.25 | 'numbers I took are very optimistic rather than the opposite' | supports direction |

## Pre-registered prediction
Written before the text search was repeated on the PDF text layer. Under Day's reading: a sentence equivalent to 'comes to Eden's conclusions' exists. Under the critic reading: Ulam's tone is exploratory ('schematic', 'start the discussion', p.22). Result that would change the verdict: a physical-copy check of pp.21-23 or the original 1967 printing (the local file is the 1985 Liss reprint scan).

## Check
Text search: python3 -I over `Wistar1967.txt` and `pdftotext -layout` of the PDF: no 'come to Eden'; only the p.22-23 sentence. Script: ad hoc, not committed.

## Simulator variables implied
None.
