---
id: D2e
title: "Waddington's summary ('the meaningful section is quite large') is an empirical assertion with no data or calculation"
side: day
branch: D
parent: D2
edges: [{type: attacks, target: D1},{type: supports, target: D}]
load_bearing: false  # D is not required for ROOT
sourcing: firsthand
status: extracted
verdicts:
  internal: holds      # Day's point that the summary supplies no data is borne out by the passage
  fidelity: partial      # quote accurate (p.93); Day omits the same speaker's concession that the meaningful space is a minute fraction of the total
  external: contested      # 
---

## Statement (verbatim)
> "Waddington asserts that “the meaningful section” of explored sequence space “is quite large in comparison with all the things that could conceivably be made out of it in single steps.” This is an empirical claim. He provides no data to support it. He provides no calculation. He simply asserts it."

Source: [The Best They've Got I](https://voxday.net/2026/10/05/the-best-theyve-got-i/), 2026-10-05, voxday.net, para 31.

Primary text (Moorhead & Kaplan (eds), *Mathematical Challenges to the Neo-Darwinian Interpretation of Evolution*, Wistar Institute Monograph No. 5 (1967; symposium 25-26 Apr 1966), local copy = 1985 Liss reprint scan, OCR text; page = printed folio (OCR garbles noted in place)):

> "In the part which it has explored, which is the only part that is relevant to a consideration of evolution, biologists are asserting that the meaningful section of it is quite large in comparison with all the things that could conceivably be made out of it in single steps. It is a much larger fraction than is the space of meaningful strings of English words. I think this is the point."

> "We are asserting that it is a large fraction of the total space which could be made from the nucleotides involved, but stiIl we are saying that the meaningful space is a minute fraction of the total nucleotide space."
— The Chairman, C. H. Waddington, summing up on the Schützenberger question, p.93. Preceding sentence: > "Therefore, life has only explored a minute fraction of the total nucleotide space." (the OCR attributes the summary to 'the Chairman, DR. WADDINGTON'.)

## Formal statement
Waddington's statement has two parts. (1) Life explored only 'a minute fraction of the total nucleotide space', exploring 'sequentially from the last position to some neighboring position'. (2) In the explored region, the meaningful section 'is quite large in comparison with all the things that could conceivably be made out of it in single steps' (a local-density claim), 'a much larger fraction than ... meaningful strings of English words'. Part (1) concedes Eden's premise; part (2) is the topology horn (D3b) in biologists' form. In notation: local functional fraction f_local >> global fraction f_global.

## Assumptions
- Stated: local density of function around explored sequences is high.
- Implicit: exploration proceeds by single steps from functional starting points, so f_local, not f_global, governs the search.

## Responses
- Against: Day: no data, no calculation (accurate for this passage). Waddington adds a footing: 'they would have eaten anything else before it had a chance to get going', i.e. an early-life narrative.
- In support: the principle is the standard 'evolution does not sample uniformly' reply.
- Weaknesses: the concession ('minute fraction of the total') is omitted in Day's account, which makes the rebuttal seem to deny Eden's premise; and Waddington's claim is as unsupported as Day alleges.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Wistar p.93 (Waddington) | meaningful space 'a minute fraction of the total nucleotide space' (concession) | accurate; omitted by Day |

## Pre-registered prediction
Written before any check. Under Day's reading: no number in the passage (confirmed by reading). Under the critic's reading: the claim is the topology horn and is testable (D2h). Result that would change a verdict: DMS-based estimate of f_local.

## Check
Textual (above). Quantitative follow-up in D2h.

## Simulator variables implied
f_local vs f_global; step-wise exploration constraint.
