---
id: D4b
title: "Mayr and Wald on Ulam: gamma = 1e-6 is unreasonably low (mutants often have a 30 percent advantage); improvements can go on simultaneously"
side: literature
branch: D
parent: D4
edges: [{type: attacks, target: D4}]
load_bearing: false  # D is not required for ROOT
sourcing: firsthand
status: extracted
verdicts:
  internal: n/a      # 
  fidelity: n/a      # the claims are Mayr's; no citation is given at the symposium for the 30 percent figure
  external: contested      # the empirical distribution of selection coefficients is the question (cf. A4, Zeng 2021 in the fidelity ledger)
---

## Statement (verbatim)
> "DR. MAYR: This gamma you chose is really quite unreasonable. Fisher and Wright also took extremely low gammas when they started; but the recent work indicates that very often a mutant has a 30 percent advantage-in other words, up to 70 percent advantage."

> "DR. MAYR: Couldn't they all go on simultaneously? DR. ULAM: This is extremely unlikely. DR. MAYR: No, no. DR. ULAM: Look, there will be only ten individuals which received an improvement in one generation."

> "DR. WALD: It is very good. You have exaggerated the difficulties, so your argument is going to be a minimum."

Source: discussion following Ulam, in Moorhead & Kaplan (eds), *Mathematical Challenges to the Neo-Darwinian Interpretation of Evolution*, Wistar Institute Monograph No. 5 (1967; symposium 25-26 Apr 1966), local copy = 1985 Liss reprint scan, OCR text; page = printed folio (page numbers from the PDF text layer headers; OCR garbles noted in place), p.24 (Mayr, Ulam, Wald).

## Formal statement
Mayr: gamma ~ 0.3 (not 1e-6); with Ulam's M = 1e11 and p0 = 1e-10, t_sweep = ln(1e10)/0.3 = 77 generations (recomputed 76.8), so 10^6 serial improvements need 7.7e7 generations (7.7e7 < 3.65e11 available one-day generations). Simultaneity: if improvements at different loci proceed in parallel, T ~ t_sweep (+ waiting), independent of n up to interference limits.

## Assumptions
- Stated: recent work indicates mutants often have large advantages; simultaneous sweeps are possible.
- Implicit: gamma is a typical rather than a selected-for (survivorship-biased) value; the 30 percent comes from cases where the mutant 'gets incorporated', i.e. observed substitutions are selected for being large.

## Responses
- Against: Ulam (p.24): simultaneous sweeps 'extremely unlikely' because only ten individuals carry the improvement per generation; Day (blog 2025-12-27, 'Hardcoded'; 2026-09-30) argues the average rate is indifferent to parallel vs serial (G1).
- In support: Wald: Ulam's numbers are a minimum difficulty.
- Weaknesses: both gamma values are assertions at the symposium. Mayr's 30% is an upward-selected value (substitutions observed because they were large), the same reasoning applied by critics to Day's Zeng 2021 s = 0.001 (fidelity ledger).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Wistar p.24 | quoted above | primary |

## Pre-registered prediction
Written before the Ulam simulation. Under Mayr: completion time ~ 77 + small for parallel sweeps at gamma = 0.3. Under Ulam: ~10^13 for gamma = 1e-6 serial. These do not conflict: they differ in gamma by 3e5. A check can distinguish only the serial-vs-parallel question at fixed gamma (see D4).

## Check
See D4 (specification only).

## Simulator variables implied
gamma distribution (including survivorship-biased tail); simultaneity switch.
