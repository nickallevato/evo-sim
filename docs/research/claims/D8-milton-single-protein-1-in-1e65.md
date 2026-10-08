---
id: D8
title: "Richard Milton: the probability of a single protein forming by chance is 1 in 10^65"
side: ally
branch: D
parent: D
edges: [{type: supports, target: D}]
load_bearing: false  # not a premise of ROOT
sourcing: secondhand
status: extracted
verdicts:
  internal: n/a      # no derivation
  fidelity: unverifiable      # Milton's 1992 book not retrieved; the blockquote is an unattributed summary
  external: pending      # no model stated
---

## Statement (verbatim)
> "When he examines the probability calculations for even a single protein forming by chance (1 in 10^65), he finds odds so astronomical that they’re equivalent to winning the lottery every week for a thousand years with the same numbers."

> "Richard Milton’s Shattering the Myths of Darwinism arrived in 1992 like a stone through the stained glass window of scientific orthodoxy."

Source: voxday.net, [The Foundation of Sand](https://voxday.net/2025/10/02/the-foundation-of-sand/), 2025-10-02 (post id 68823), as reproduced in the tag archive page `sources/raw/day/tags/evo-11.html`; the passage is a blockquote that Day introduces as 'a death that has been in the making for at least the last 30 years' and which is not attributed to an author in the extracted text. `secondhand`: it summarises Milton, *Shattering the Myths of Darwinism* (1992). Day's own sentence closing the post:

> "It was obvious from the time of the 1967 symposium held by the Wistar Institute that evolution was not a real science."

## Formal statement
Single stated number: P(single protein by chance) = 10^-65, no length, function or fold stated. Candidate reconstruction (this file; not in the source): a specific 50-residue sequence has probability 20^-50 = 10^-65.05 (50*log10(20) = 65.05), so the figure is consistent with a specific 50-mer; no source says this.

## Assumptions
- Stated: 'even a single protein forming by chance'.
- Implicit: a specific sequence; random assembly (the model Ulam called 'not the problem', D4a).

## Responses
- Against: Taylor 2001 and Keefe & Szostak 2001 (D11, D12) measured frequencies of function in random libraries, which are not 10^-65-scale; Axe 2004 (D10) is lower for a 150-residue domain.
- In support: n/a.
- Weaknesses: unsourced; the model is the one Ulam and Eden's own reply treat as not the real argument. Note Day writes '1967 symposium' where the meeting was 25-26 April 1966 (the proceedings are 1967).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Milton 1992 | not retrieved | unverifiable |

## Pre-registered prediction
No check (no definition of the event). Action: obtain Milton 1992 and the page.

## Check
None.

## Simulator variables implied
Sequence length and function definition would be needed.
