---
id: D2g
title: "No biologist at Wistar produced a single calculation that contradicted the mathematicians' conclusions"
side: day
branch: D
parent: D
edges: [{type: supports, target: D},{type: attacks, target: D1}]
load_bearing: false  # D is not required for ROOT
sourcing: firsthand
status: extracted
verdicts:
  internal: pending      # depends on what counts as a calculation that "contradicts"
  fidelity: partial      # the transcript contains numbers from biologists (Wright pp.117, 119; Mayr pp.24, 30); whether they "contradict" is interpretive
  external: contested      # 
---

## Statement (verbatim)
> "Eden calculated the size of sequence space. No one calculated a smaller space. Ulam calculated a rate. No one calculated a faster rate. Schützenberger asked for a mechanism. No one demonstrated one."

Source: [The Best They've Got I](https://voxday.net/2026/10/05/the-best-theyve-got-i/), 2026-10-05, voxday.net, para 26.

> "Rosenhouse never acknowledges that not one biologist at the conference produced a single calculation that contradicted the mathematicians’ conclusions"

Source: same, para 26.

Biologist numbers in the volume (Moorhead & Kaplan (eds), *Mathematical Challenges to the Neo-Darwinian Interpretation of Evolution*, Wistar Institute Monograph No. 5 (1967; symposium 25-26 Apr 1966), local copy = 1985 Liss reprint scan, OCR text; page = printed folio (OCR garbles noted in place)):

> "it would require less than 1250 questions to arrive at a specified one of these proteins."
— Sewall Wright, p.117 (arithmetic: 250 residues x 5 yes/no answers; recomputed 250*5 = 1250; the information bound log2(20^250) = 1080 bits).

> "In a population as large as the human species, 3 x 10 9 , a mutation rate of 10 5 at each locus implies that all single step mutations from the common alleles will recur in every generation."
— Wright, p.119 (mutation supply; arithmetic 3e9 x 1e-5 = 3e4 new mutants per locus per generation).

> "What is surprising is how fast rational information is produced by the machine within the meaning of the original context."
— Alex Fraser, p.80, describing his computer experiments on a genetic system (qualitative statement of a simulation result; no numbers in this turn).

## Formal statement
Universal over biologist contributions B at Wistar: for all b in B, not (b is a calculation and b contradicts C_Eden/C_Ulam/C_Schützenberger). Counter-examples need (i) a calculation, (ii) bearing on a conclusion. Candidates: Fraser's simulation result (p.80), Bossert's and Lewontin's computer models (Day concedes Lewontin's simulations are 'technically impressive' but 'missed the point', ch.6); Wright's 1250-question bound (bears on the 'typing at random' reading of Eden, which Eden said at p.8 was a misreading); Wright's mutation-supply figure (bears on Ulam's 'ten individuals per generation'); Mayr's gamma (30 percent, no source) vs Ulam's 1e-6.

## Assumptions
- Stated: no calculation contradicted a conclusion.
- Implicit: a numerical analogy (Wright) is not a calculation about biology; unsourced estimates (Mayr) do not count.

## Responses
- Against: the three items above. Whether they 'contradict' is the open point: Wright's 1250 vs 10^325 contradicts the reading that selection needs ~10^325 steps; Eden's reply (p.8) accepts the arithmetic ('Of course, he is correct') and re-bases the argument on path length. So at least one contradiction of one reading of Eden was calculated and conceded.
- In support: no biologist computed the time to fix 10^6 successive improvements (Ulam, p.24) or the path-length distribution (Eden p.8, which Eden himself says he cannot compute).
- Weaknesses: both statements are about a 60-year-old transcript; and the universal claim is contestable by a single counter-example. Day's own post of 2024-07-13 reproduces Wright's 1250-question passage (as an example of an 'attempt' that fails), so the existence of Wright's calculation is not in dispute.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Wistar p.117 (Wright) | quoted above | accurate |
| Wistar p.119 (Wright) | quoted above | accurate |
| Wistar p.8 (Eden) | 'Of course, he is correct, but I believe he has misunderstood my argument.' | accurate |

## Pre-registered prediction
Written before the arithmetic. Under Day's claim: no biologist number contradicts the conclusions as stated. Under the critic's claim: Wright's calculation contradicts the random-assembly reading, and Mayr's gamma contradicts Ulam's gamma. Result that would change a verdict: Eden's agreement that Wright's arithmetic is correct (found, p.8) moves the fidelity verdict to partial; internal verdict depends on whether Eden's revised argument (path length) was ever quantitatively answered at Wistar (not found).

## Check
Arithmetic: `python3 -I -c "import math;print(250*5, 250*math.log2(20), 3e9*1e-5)"` -> 1250, 1080.5, 30000.0. Reconciles with Wright's 1250 (rounded up from 1080.5 bits).

## Simulator variables implied
None.
