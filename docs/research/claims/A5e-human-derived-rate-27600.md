---
id: A5e
title: "A rate derived from human parameters alone gives one fixation per 27,600 effective generations, so 8 are achievable"
side: day
branch: A
parent: A5
edges: [{type: attacks, target: A5b}, {type: depends-on, target: A4}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: holds   # R4 X1 rule rev 2 (was arithmetic-error): R1b: 9.13 vs 8 is 12%, 205M shortfall moves 12%, conclusion unchanged -> ledger
  fidelity: unverifiable
  external: pending
---

## Statement (verbatim)
> yields approximately one fixation per 27,600 effective generations (Day and Athos 2025, Appendix D). Applied to 252,000 generations provides 8 achievable fixations against the 205 million required.

Source: [MITTENS 3.0, Zenodo 23003785](https://zenodo.org/records/23003785) (key Z23003785), 2026-09-28 (modified 2026-10-04), p.15 (s8.6). The derivation is in the book appendix, not harvested.

## Formal statement
G_f(human) = 27,600 effective generations per fixation; achievable = 252,000 / 27,600.
`derived:` (python3 -I) 252,000/27,600 = 9.13, not 8 (8 x 27,600 = 220,800, which would correspond to t_div = 5.5 My at 25 y, 220,000 generations). A 12% discrepancy in the paper's own sentence; immaterial to the 205M shortfall, but the figure does not reconcile. For scale: Day's Q&A formula (2/s) ln(2Ne) with s = 0.001, Ne = 10,000 gives 19,807 (Q44-Q46); 27,600/19,807 = 1.39; the reason for the ratio is not stated in the paper.
Method flag: the text says the rate was "calculated … using Kimura's fixation time formula and the Bio-Cycle correction". If a fixation time (latency) is inverted into a rate, the calculation takes the serial form; the repo check F1 shows latency and throughput differ (see Check).

## Assumptions
- Stated: human parameters alone; Kimura fixation time; Bio-Cycle correction for overlapping generations.
- Implicit: a fixation time t_fix sets the rate 1/t_fix (serial form); s = 0.001 beneficial (Zeng 2021 coefficient is for negative selection: ledger misread).

## Responses
- Against: KITTENS (A5b §11) says "§8.2 and Appendix D revert to the interval form for drift". Mansfield (MF-04): "The time it takes for one allele to get fixed is not important, it is the time BETWEEN successive fixations that is important." (F branch).
- In support: none beyond Day.
- Weaknesses in the responses: Appendix D itself was not retrieved by either side in the corpus; the critics' characterization is of the 3.0 text, not the appendix.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Zeng et al. 2021 | "predicted mean selection coefficient of ~0.001" for negative selection on trait variants | verified-misread when used as a beneficial s |
| Kimura & Ohta 1969 | "takes about 4Ne generations until fixation"; no recombination discussed | t_fix accurate; recombination attribution misread |

## Pre-registered prediction
Linked result: F1 (research/checks/RESULTS.md): steady-state rate = 2N·U_b·u(s) independent of latency; simulated 0.3972 ± 0.0018 vs predicted 0.3960; t_fix = 847 generations but G_f = 3 generations; in-transit count ≈ 336 (computed, not measured). Caveat in RESULTS.md: parameters unrealistic (0.4 substitutions per generation, no interference or cost), so pipelining is shown possible, not feasible at realistic parameters. B0.4 result: (2/s)ln(2N) overshoots the diffusion mean fixation time by 1.6–2.2x (at Day's N=1e4, s=0.001: 19,807 vs 8,480).

## Check
Link: `research/checks/RESULTS.md` F1, B0.4. Arithmetic audit (python3 -I, scratch). Review: pending.

R4 X1 (research/checks/results/R4-X1-rescore.md; rule research/checks/results/R4-X1-verdict-rule.md rev 2; review #12, 2026-10-09): under the single both-sides rule this node is holds / unverifiable. R1b: 9.13 vs 8 is 12%, 205M shortfall moves 12%, conclusion unchanged -> ledger Charitable reading tried: tried t_div = 5.5 My: reproduces '8' only at another input; 12% -> ledger.

## Simulator variables implied
- Selectable rate model: aggregate throughput vs 1/t_fix; Bio-Cycle toggle.
