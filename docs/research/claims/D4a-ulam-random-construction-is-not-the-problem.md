---
id: D4a
title: "Ulam: Eden's first minutes concern random construction of molecules, 'this is not the problem at all'; a mathematical treatment must include selection"
side: literature
branch: D
parent: D4
edges: [{type: attacks, target: D3},{type: attacks, target: D}]
load_bearing: false  # D is not required for ROOT
sourcing: firsthand
status: extracted
verdicts:
  internal: holds      # Ulam's sentence supports the critics' reading that the random-assembly size comparison is not the right model
  fidelity: accurate      # the quote as used by Rosenhouse (via Day) matches p.21
  external: contested      # Eden replied that Wright's analogue misunderstood his path-length argument; Ulam then does a rate calculation that he says illustrates what Eden had in mind
---

## Statement (verbatim)
> "But, I believe that the comments of Professor Eden, in the first five minutes of his talk at least, refer to a random construction of such molecules and even those of us who are in the majority here, the non-mathematicians, realize that this is not the problem at all."

> "A mathematical treatment of evolution, if it is to be formulated at all, no matter how crudely, must include the mechanism of the advantages that single mutations bring about and the process of how these advantages, no matter how slight, serve to sieve out parts of the population, which then get additional advantages. It is the process of selection which might produce the more complicated organisms that exist today."

Source: Ulam, in Moorhead & Kaplan (eds), *Mathematical Challenges to the Neo-Darwinian Interpretation of Evolution*, Wistar Institute Monograph No. 5 (1967; symposium 25-26 Apr 1966), local copy = 1985 Liss reprint scan, OCR text; page = printed folio (page numbers from the PDF text layer headers; OCR garbles noted in place), p.21 (both sentences; the first is the start of the talk's discussion of Eden). Context sentence immediately before: > "It appears, naIvely at least, that no matter how large the probability of a single mutation is, should it be even as great as one-half, you would get this probability raised to a millionth power, which is so very close to zero that the chances of such a chain seem to be practically nonexistent." — Ulam presents that chain-probability argument as naive; he then says it is not the problem.

Day's account of this passage (The Best They've Got I, 2026-10-05 — in Best They've Got I): 'But the transcript shows Ulam was agreeing with Eden's broader point while noting that the first five minutes of Eden's talk addressed a preliminary issue that was not the central problem.'

## Formal statement
Ulam's logical position: (i) the product-of-probabilities chain argument ('probability raised to a millionth power ... practically nonexistent') is naive (his word); (ii) the random-construction framing of Eden's opening is 'not the problem'; (iii) a mathematical treatment must include the mechanism of advantage and selection; (iv) his own rate calculation (D4) then shows a time problem. In notation: Ulam rejects `P(random assembly) = A^-L` and the multiplicative chain `p^n` as models, and replaces them with a rate model T = n * t_sweep.

## Assumptions
- Stated: selection must be included.
- Implicit: the rate model is the right quantity (not the probability of assembly).

## Responses
- Against: Day: Ulam 'agreed with Eden's broader point' (D2a); the text is compatible (his rate calc 'is illustrating something that I think Professor Eden had in mind', p.24). Day's reading of Rosenhouse's use of this quote as showing Ulam 'criticising Eden' is correct only for the random-construction framing.
- In support: Rosenhouse (via Day); Wright (D6).
- Weaknesses: it is notable that Day's own papers also use a product-of-probabilities argument (the Bernoulli Barrier 10^-47,262 and the Spetner chain D7a, which Day calls correct), i.e. the reading of Ulam (i) that 'the chain argument is naive' is in tension with D7a.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Wistar p.21 (Ulam) | quoted above | accurate |

## Pre-registered prediction
No separate check (textual).

## Check
Textual audit, p.21.

## Simulator variables implied
None.
