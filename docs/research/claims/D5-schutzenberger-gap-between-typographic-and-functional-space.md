---
id: D5
title: "Schützenberger: there is a considerable gap in neo-Darwinian theory, between the space of sequences and the space of organisms, which cannot be bridged within current biology"
side: literature
branch: D
parent: D
edges: [{type: supports, target: D},{type: attacks, target: D1b}]
load_bearing: false  # D is not required for ROOT
sourcing: firsthand
status: extracted
verdicts:
  internal: pending      # a conceptual argument (matching between spaces), not a calculation; internal validity depends on whether evolution can generate the matching
  fidelity: partial      # Day's Best I quotation alters the wording ("we believe that this gap cannot be bridged" vs "we believe this gap to be of such a nature that it cannot be bridged")
  external: contested      # Lewontin, Waddington, Levins, Fraser replied at pp.76-80
---

## Statement (verbatim)
> "I intend to restrict my argument to show the existence of a serious gap in the current theory of evolution."

> "Thus, to conclude, we believe that there is a considerable gap in the neo-Darwinian theory of evolution, and we believe this gap to be of such a nature that it cannot be bridged within the current conception of biology."

Source: Schützenberger, 'Algorithms and the Neo-Darwinian Theory of Evolution', in Moorhead & Kaplan (eds), *Mathematical Challenges to the Neo-Darwinian Interpretation of Evolution*, Wistar Institute Monograph No. 5 (1967; symposium 25-26 Apr 1966), local copy = 1985 Liss reprint scan, OCR text; page = printed folio (page numbers from the PDF text layer headers; OCR garbles noted in place), p.73 and p.75.

> "Their experience is quite conclusive to most of the observers: without some built-in matching, nothing interesting can occur."

> "We do not know any general principle which would explain how to match blueprints viewed as typographic objects and the things they are supposed to control."

Source: same, p.75.

Day's rendering:

> "concluded that “there is a considerable gap in the neo-Darwinian theory of evolution, and we believe that this gap cannot be bridged within the current conception of biology.”"

Source: The Best They've Got I, 2026-10-05, para 11 (the quotation marks enclose a paraphrase; the printed sentence is above).

## Formal statement
Schützenberger's structure: three spaces (typographic/genotype, phenotype/function, parameter/epigenetic), with relations between them given only by assumptions (his words: 'a topology'); the claim is that no principle is known that matches typographic proximity to functional proximity; programs written by random typographic changes do not compute; artificial-intelligence experience says 'without some built-in matching, nothing interesting can occur'. The probabilistic figures (D5a) are illustrative.

## Assumptions
- Stated: the gap exists and the matching mechanism is unknown; 'I intend to restrict my argument to show the existence of a serious gap'.
- Implicit: random typographic changes are the only variation process; the matching cannot be itself produced by selection (the 'Ashby trap', p.79).

## Responses
- Against: Lewontin (p.76, p.79): known cases where single amino-acid changes alter but do not destroy enzymes; Levins (p.79): 'its topology is, itself, a product of evolution'; Waddington (p.78): typographic errors are absorbed by the logic of paragraphs; Fraser (p.80): a genetic system with multiple pathways reaches rational information fast; Ulam (p.76) replies that Darwinian theory is admittedly incomplete, which he says is not an objection to the scheme (paraphrase; the OCR interleaves two columns there).
- In support: Day (D, D2); Rosenhouse's 'Kansas vs New Jersey' reply (via Day) is a rebuttal at the codon level only (D2 context).
- Weaknesses: Schützenberger asks for a mechanism and a general principle; neither side supplies a measurement. This is the same open item as D2h. Fraser's and Lewontin's replies are descriptive. Schützenberger himself says (p.73) that his restricted aim is the 'existence of a serious gap'.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Wistar p.76 (Ulam) | quoted in Responses | primary |

## Pre-registered prediction
Written before any check. Under the claimant: on empirically measured landscapes, adaptive walks without a pre-built matching reach high-fitness sequences rarely. Under the opposing model: they reach them readily when single-substitution neighbors are mostly functional. Result that would change a verdict: the p(neighbor functional) estimate (D2h).

## Check
Specification: D, step S2/S3.

## Simulator variables implied
Genotype-phenotype map smoothness; epigenetic-parameter space.
