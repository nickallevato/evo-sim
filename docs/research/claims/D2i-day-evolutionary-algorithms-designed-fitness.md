---
id: D2i
title: "Every evolutionary algorithm has a programmer-designed fitness function, supplying the mapping Schützenberger said biology lacks"
side: day
branch: D
parent: D2
edges: [{type: attacks, target: D1b},{type: depends-on, target: D5}]
load_bearing: false  # D is not required for ROOT
sourcing: firsthand
status: extracted
verdicts:
  internal: holds      # valid against an existence-proof reading; silent on plausibility readings
  fidelity: n/a      # 
  external: contested   # biological fitness feedback exists (survival/reproduction) but the sequence-to-fitness map is not designed; whether it is smooth is the open question; R4 D1: the spike's RNA walks are known-target and illustrate the objection; on the measured GB1 landscape uphill walks are not trapped at poor optima
---

## Statement (verbatim)
> "every evolutionary algorithm ever written has a programmer-designed fitness function that does exactly what Schützenberger said biology lacks: it provides the mapping between typographic changes and functional outcomes."

> "Dawkins’s WEASEL program is the perfect example: it works because Dawkins specified the target string, the fitness function, and the selection rule."

Source: [The Best They've Got II](https://voxday.net/2026/10/06/the-best-theyve-got-ii/), 2026-10-06, voxday.net, para 7.

## Formal statement
Evolutionary-algorithm success is conditional on a fitness mapping F: sequence -> reproductive success with exploitable gradient. Day: programmers supply F; biology must supply F too, so the algorithms show nothing about the origin of F. Dawkins's Weasel uses F = number of letters matching a fixed target (known endpoint), which Day also criticises in his Weasel post (D9: 'the target phrase is known from the start, which is not the case in the evolutionary context').

## Assumptions
- Stated: designed F is what Schützenberger said biology lacks.
- Implicit: biological F is not simply 'designed'; it is the survival and fertility consequence of the sequence, which exists whether or not it is smooth. The dispute is whether natural F gives local gradients.

## Responses
- Against: Wright (D6) says his analogy is 'not a perfect analogy to natural selection'; Weasel's own defenders (not in corpus) typically note it illustrates cumulative selection, not target-free evolution. Computational biology uses empirically measured landscapes (not in corpus).
- In support: Schützenberger, p.75: 'without some built-in matching, nothing interesting can occur' (observation about AI programs).
- Weaknesses: the point is correct about Weasel and equally shows Day's own Weasel recomputation (D9) inherits the target-known feature he rejects.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Schützenberger (Wistar p.75) | 'Their experience is quite conclusive to most of the observers: without some built-in matching, nothing interesting can occur.' | accurate |

## Pre-registered prediction
Written before any check. Under Day: evolutionary algorithms on empirical landscapes without built-in gradient fail to find high-fitness sequences. Under the opposing model: they succeed whenever measured landscapes have local gradients (low K). Result that would change a verdict: success/failure on DMS-derived landscapes (D2h step S2/S3).

## Check
R4 D1 (research/checks/results/R4-D1-spike.md, review #11, 2026-10-09): the spike's RNA walks use a known target structure and so illustrate Day's objection; the discriminating test is a measured landscape (GB1), where uphill walks end well above WT and are not trapped at poor optima, though rarely at the top.

Specification only: reuse the S2/S3 module.

## Simulator variables implied
Landscape provenance (designed vs empirical) switch in the simulator.
