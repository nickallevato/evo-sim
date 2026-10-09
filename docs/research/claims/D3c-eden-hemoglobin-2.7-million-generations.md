---
id: D3c
title: "Eden calculated that hemoglobin alpha-to-beta conversion takes a time that 'vastly exceeds the time available' (Day) versus 2.7 million generations, 'not implausible' (Eden)"
side: day
branch: D
parent: D3
edges: [{type: supports, target: D2g},{type: depends-on, target: D3b}]  # D3c -> D2g was typed attacks; Day's account of Eden backs D2g. Eden's own 'not implausible' is recorded as the fidelity verdict, not as an edge (fixed 2026-10-08)
load_bearing: false  # D is not required for ROOT
sourcing: firsthand
status: extracted
verdicts:
  internal: pending      # Eden's 2.7e6 cannot be reproduced from the printed inputs
  fidelity: misread      # Eden's printed result is "a little large but not implausible"; the "vastly exceeds" conclusion appears only for the unspecified longer meandering path, for which Eden gives no estimate
  external: contested      # 
---

## Statement (verbatim)
> "Eden then considered the specific case of hemoglobin. The alpha chain contains 141 amino acids and the beta chain contains 146 amino acids. A minimum of 120 point mutations would be required to convert alpha to beta if evolution proceeded from one chain to the other, or from a common ancestor to both, then each step along the path must have been independently viable. But the path requires traversing sequence space through intermediate forms, and Eden calculated that even under generous assumptions about mutation rates and selection coefficients, the time required to do so vastly exceeds the time available."

Source: [Vox Day Interview on Evolutionary Theory](https://billdembski.substack.com/p/vox-day-interview-on-evolutionary) (Dembski Substack), 2026-09-28, appended chapter 'From Probability Zero (2nd ed.) on 1966 Wistar Symposium, Chapter 6: The 1966 Meeting of the Minds' (primary Day text, posted with Day's permission), section 'The Arguments', Eden paragraph.

Primary text:

> "On this basis we would expect on the order of 2,700,000 generations to be required for one hemoglobin chain to transform to the other. This is a little large but not implausible."

Source: Eden, 'Inadequacies of Neo-Darwinian Evolution as a Scientific Theory', in Moorhead & Kaplan (eds), *Mathematical Challenges to the Neo-Darwinian Interpretation of Evolution*, Wistar Institute Monograph No. 5 (1967; symposium 25-26 Apr 1966), local copy = 1985 Liss reprint scan, OCR text; page = printed folio (page numbers from the PDF text layer headers; OCR garbles noted in place), p.8. Eden's inputs: 120 point mutations between alpha and beta by a unique path; 420 nucleotides; mutation rate 10^-6; population 10^6; 8-9 amino acids reachable per step; 20 generations to convert the population under strongest selection. He then argues the path likely meandered and gives no estimate (D3b).

## Formal statement
Eden's stated model: T = 120 * (t_wait + 20), t_wait unspecified. Tried reconstructions (this file): t_wait = 420 sites x 8.5 amino acids = 3,570 gen per step gives T = 4.3e5; with 3 nucleotide alternatives per site 1.3e6; Eden prints 2.7e6 (22,500 gen per step). The formula is not given, so the figure is not reproduced; the printed value is within a factor ~2-6 of simple reconstructions.

## Assumptions
- Stated: unique path, 8-9 reachable amino acids, mu = 1e-6, N = 1e6, strongest selection.
- Implicit: each step requires a specific mutation to arise and sweep before the next (serial), no standing variation.

## Responses
- Against: Eden's own text calls the result 'a little large but not implausible'; the 'vastly exceeds' claim attaches in Eden to the (uncomputed) meandering path.
- In support: Day's reading is that Eden's later qualitative remark (paths 'many powers of 10 greater') implies the conclusion.
- Weaknesses: Day's rendition of residue counts (141) differs from Eden (140, 146), minor. The serial assumption is the same as the Ulam/Day 'single file' assumption (G).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Wistar p.8 (Eden) | 2.7e6 generations 'a little large but not implausible' | accurate |

## Pre-registered prediction
Written before the reconstruction. Under Eden: 120*(t_wait+20) = 2.7e6 for t_wait ~ 2.25e4 gen. Under simple reconstructions: 4e5 to 1.3e6. The reconstruction does not reproduce the printed number; the discrepancy is under 1 order of magnitude. Result that would change a verdict: Eden's unpublished formula or a reconstruction that reaches 2.7e6.

## Check
Arithmetic: `python3 -I -c "print(120*(420*8.5+20), 120*(420*8.5*3+20))"` -> 430,800; 1,287,600. Not committed.

## Simulator variables implied
Specific-step waiting time model; serial vs parallel; reachable-alternatives count (8-9 amino acids); mutation rate; N.
