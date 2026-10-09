---
id: D4
title: "Ulam: 10^6 successive improvements each needing ~10^7 generations to spread requires about 10^13 generations"
side: literature
branch: D
parent: D
edges: [{type: supports, target: D},{type: depends-on, target: D4b}]
load_bearing: false  # D is not required for ROOT; this is the historical precursor of the serial-sweep rate argument (branch A/G)
sourcing: firsthand
status: extracted
verdicts:
  internal: holds      # arithmetic reproduces to order of magnitude (logistic: 2.3e7 per sweep, 2.3e13 total) given the serial assumption
  fidelity: n/a      # Ulam's own claims; Day's ch.6 description ("a sequence of ten improvements") differs from the printed 10^6
  external: contested   # serial assumption and gamma = 1e-6 are disputed in the volume (Mayr, p.24); R4 D1: serial assumption not tested; the shared-pool table (k = 25 needed changes from 51 beneficial SNVs succeeds with P 0.07 at s = 0.01) is the stepping-stone logic
---

## Statement (verbatim)
> "Let us assume that we have 1011 individuals. Each lives one day and let us say that the chance of a favorable mutation or "improvement" is 10- 10 per individual."

> "y is, of course, a small number and with a tiny advantage given by this one improvement, let us say y is 10- 6 , it will take about 106 generations before most of the population is endowed with this improvement."

> "In 10 6 generations, most of the population will have this advantage even with this small value of y. In 10 7 generations, say, almost all individuals will have it. Now, remember that we want not just one improvement but, say, 106 in succession. So we need about, say, 10 13 generations and not much more."

Source: Ulam, 'How to Formulate Mathematically Problems of Rate of Evolution?', in Moorhead & Kaplan (eds), *Mathematical Challenges to the Neo-Darwinian Interpretation of Evolution*, Wistar Institute Monograph No. 5 (1967; symposium 25-26 Apr 1966), local copy = 1985 Liss reprint scan, OCR text; page = printed folio (page numbers from the PDF text layer headers; OCR garbles noted in place), p.24. OCR: '1011' = 10^11, '10- 10' = 10^-10, '106' = 10^6, 'y' = gamma. The same page contains Ulam's remark: > "Of course it could mean that I am taking such naive schemes too seriously." (p.24).

Day's chapter 6 summary of Ulam: 'Suppose evolution requires a sequence of ten improvements ... Ulam worked through the arithmetic and showed that even under optimistic assumptions, the time required grows rapidly.' (see [Vox Day Interview on Evolutionary Theory](https://billdembski.substack.com/p/vox-day-interview-on-evolutionary) (Dembski Substack), 2026-09-28, appended chapter 'From Probability Zero (2nd ed.) on 1966 Wistar Symposium, Chapter 6: The 1966 Meeting of the Minds' (primary Day text, posted with Day's permission)).

## Formal statement
Ulam's scheme (p.24): population M = 1e11, generation = 1 day; favourable-mutation probability alpha = 1e-10 per individual, so 10 carriers per generation (p0 = 1e-10); advantage gamma = 1e-6 (offspring 1 + gamma). Time for the improvement to spread: Ulam: ~10^6 generations to 'most', ~10^7 to 'almost all'; for n = 10^6 improvements in succession: ~10^13 generations. Recomputed (deterministic logistic): t(p0 -> 0.5) = ln(1e10)/gamma = **2.30e7** generations; t(p0 -> 0.99) = **2.76e7**; times 1e6 = **2.3-2.8e13**. Ulam's '10^6 to most' understates the logistic result by 23x; his '10^7 for almost all' understates by 2.8x; his total 10^13 is within a factor of 2-3. Time available in the scheme: 'one billion years' x 365.25 = 3.65e11 one-day generations; shortfall 10^13/3.65e11 = 27x (2.3e13: 63x).

## Assumptions
- Stated: single-locus-at-a-time ('specific loci which determine the eye'), improvements 'in succession', each must spread through the population before the next; gamma and alpha are unknown, 'to give you some numbers'.
- Implicit: no simultaneous sweeps (disputed by Mayr, 'Couldn't they all go on simultaneously?', Ulam: 'extremely unlikely'); no recombination between loci; genic selection; the 10^6 count of required improvements.
- Ulam disclaims: 'not to put any credence whatsoever on the value of these parameters' (p.22) and 'it could mean that I am taking such naive schemes too seriously' (p.24).

## Responses
- Against: Mayr (D4b): gamma is 'really quite unreasonable'; 'very often a mutant has a 30 percent advantage'; improvements can proceed simultaneously. Wald: 'You have exaggerated the difficulties, so your argument is going to be a minimum' (p.24). Levins (p.24): 'Why don't we challenge the model after we disagree with the results?'.
- In support: Day (D2a, ch.6); the serial sweep model is the ancestor of MITTENS (A): same structure with gamma replaced by measured G_f.
- Weaknesses: the argument is wholly conditional on serial sweeps; the disagreement is the same as branch G (serial vs parallel).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Wistar p.24 | quoted above | primary |

## Pre-registered prediction
Written before the Ulam simulation spec. Under Ulam's model (serial): total time T = n * t_sweep(gamma, N, alpha) with t_sweep ~ ln(1/p0)/gamma. Under the opposing model (Mayr): improvements at different loci proceed simultaneously; total time ~ t_sweep + waiting for the last arrival, with total mutation supply across 10^6 loci of order 10^7 carriers per generation if alpha applies per locus (Ulam's alpha is 'per individual' for 'an improvement'; whether it applies to each of 10^6 loci is ambiguous in the text, Medawar asks 'In one locus?', Ulam: 'specific loci'). Result that would change a verdict: a WF simulation of n loci with independent sweeps at gamma = 1e-6, M = 1e11 (scaled) showing whether the completion time is ~n*t_sweep (serial) or ~t_sweep*(1 + small) (parallel).

## Check
R4 D1 (research/checks/results/R4-D1-spike.md, review #11, 2026-10-09): Table C models k needed changes in one gene drawing on a shared pool of beneficial SNVs (median 51): P(success) 0.999 for k = 10, 0.074 for k = 25, 4e-20 for k = 50 at s = 0.01 and T = 3e5; at s = 0.001 even k = 10 gives 1e-4. The serial assumption itself is not tested.

Specification (later module): scaled WF with n in {10,100,1000} loci, gamma scaled, tracks completion time; compares serial prediction n*t_sweep with parallel max; checks Hill-Robertson interference at gamma*M scales. Arithmetic done: `python3 -I -c "import math;print(math.log(1e10)/1e-6, math.log(1e10*99)/1e-6)"` -> 2.30e7, 2.76e7. (Scratch.)

## Simulator variables implied
Population size M; generations per day; alpha (per locus vs per individual); gamma; number of loci n; serial/parallel switch; recombination rate.
