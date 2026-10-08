---
id: D6
title: "Wright: by the principle of twenty questions, fewer than 1250 steps suffice to reach a specified 250-residue protein; this is closer to natural selection than random typing"
side: literature
branch: D
parent: D
edges: [{type: attacks, target: D3},{type: attacks, target: D}]
load_bearing: false  # D is not required for ROOT
sourcing: firsthand
status: extracted
verdicts:
  internal: holds      # 250 x 5 = 1250 >= log2(20^250) = 1080.5 bits; the analogy is internally valid as a statement about information per selected step
  fidelity: n/a      # Wright's own words; page is 117 (Day-adjacent sources and the task cite 118)
  external: contested      # needs a per-step fitness signal; Eden replied (p.8) that Wright misunderstood his path-length argument
---

## Statement (verbatim)
> "Natural selection may appear to be a vacuous and tautological principle if only a single step is considered, but considered over a long succession of little steps, it is the only guiding principle that has stood up under experiment. Eden refers to the 10 350 proteins, each consisting of 250 amino acids. He seems to imply that it would require something like this number of operations of natural selection to arrive at a particular useful one. On the principle of the children's game of twenty questions in which it is possible to arrive at the correct one of about a million objects by a succession of 20 yes-orono answers, it would require less than 1250 questions to arrive at a specified one of these proteins. While this is not a perfect analogy to natural selection, it is enormously more like natural selection than the typing at random of a library of 1,000 volumes with its infinitesimal chance of arriving at any sensible result."

Source: Sewall Wright, 'Comments on the Preliminary Working Papers of Eden and Waddington', in Moorhead & Kaplan (eds), *Mathematical Challenges to the Neo-Darwinian Interpretation of Evolution*, Wistar Institute Monograph No. 5 (1967; symposium 25-26 Apr 1966), local copy = 1985 Liss reprint scan, OCR text; page = printed folio (page numbers from the PDF text layer headers; OCR garbles noted in place), p.117 (first page of Wright's comments; the PDF text layer prints folio 117 at the foot and the book's index lists 'twenty questions' at pp.8 and 117; the label 'p.118' in earlier notes is one page too high). OCR: 'yes-orono' = 'yes-or-no'; '10 350' = 10^350 (the figure in Eden's working paper, D3, not the 10^325 of the talk).

Eden's reply, p.8: > "Of course, he is correct, but I believe he has misunderstood my argument."

Day's rebuttal (quoting Wright in the same post): > "The previous die has no effect on the subsequent one and there is no cumulative result."

Source: [Evolutionists are Retarded](https://voxday.net/2024/07/13/evolutionists-are-retarded/), 2024-07-13, para 9.

## Formal statement
Information bound: identifying one of 20^250 sequences needs log2(20^250) = 250*log2(20) = 1080.5 bits, i.e. at most 1080.5 binary questions when each answer is an independent bit; Wright's 1250 = 250 residues x 5 questions per residue (5 > log2 20 = 4.32). Each question must be answered by an oracle that retains the result: in selection terms, a per-step fitness signal that keeps correct choices. Day's dice reply is correct for independent unretained trials; Wright's analogy is explicitly of retained answers.

## Assumptions
- Stated: the analogy is 'not a perfect analogy to natural selection'.
- Implicit: an environment answers each question (fitness differences exist at each residue), and the answers are independent per residue.

## Responses
- Against: Eden (D3b, p.8): path-length is the issue; Day: dice have no cumulative effect (applies to unretained trials); Day D2i: designed fitness functions.
- In support: Rosenhouse (D1); Day concedes selection is the reply by labelling it 'cumulative selection' and arguing it is not 'massively parallel fixation' (G).
- Weaknesses: the analogy establishes only that large spaces can be searched in ~log steps when an oracle exists; the existence and smoothness of the oracle is D2h.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Wistar p.117 | quoted above | primary |

## Pre-registered prediction
Written before the arithmetic. Under Wright: 250*log2(20) < 1250. Under Eden: the relevant quantity is path length on the fitness surface, not the information bound. Result that would change a verdict: none for the arithmetic; for the analogy, D2h.

## Check
S1 (done): `python3 -I -c "import math;print(250*5, 250*math.log2(20))"` -> 1250, 1080.5. Reconciles.

## Simulator variables implied
Per-residue fitness signal availability; oracle noise; number of generations per retained bit.
