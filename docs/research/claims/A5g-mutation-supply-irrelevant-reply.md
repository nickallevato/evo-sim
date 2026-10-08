---
id: A5g
title: "Day: the E. coli study is cited for its fixation rate, not its mutation rate; no human or mammalian fixation has been observed faster than 1,600 generations"
side: day
branch: A
parent: A5
edges: [{type: attacks, target: A5}]
load_bearing: false
sourcing: firsthand
status: checked
verdicts:
  internal: pending
  fidelity: n/a
  external: pending
---

## Statement (verbatim)
> I didn’t cite the E. coli study for its mutation rate but for its fixation rate: 25 mutations fixed in 40,000 generations, yielding an average of 1,600 generations per fixed mutation.

Source: [An Inspiring Critique](https://voxday.net/2026/01/27/an-inspiring-critique/) (key B2026-01-27-an-inspiring-critique), blog, 2026-01-27, ¶22.

> No one has ever observed any human or even mammalian fixation faster than 1,600 generations.

Source: [An Inspiring Critique](https://voxday.net/2026/01/27/an-inspiring-critique/) (key B2026-01-27-an-inspiring-critique), blog, 2026-01-27, ¶23.

## Formal statement
Claim (two parts): (i) G_f is an observed fixation rate and need not be scaled by μ; (ii) no mammalian fixation faster than 1,600 generations has been observed. Part (ii) is an observational-absence claim: 1,600 generations at 25 y is 40,000 years, longer than the observation window for any directly observed human allele-frequency change; `derived:` 1,600 x 25 = 40,000 y. It cannot distinguish a slow rate from lack of observation time.
Day's example in the same post: CCR5-delta32 "the fastest we could get, in theory, is 2,278 generations" and a further 37,800 generations by drift (not checked here).
Tension with the Day corpus: Z23003785 s4.3 uses the mutation supply (4.1e-4 per genome per generation) to separate neutral hitchhikers from sweeps (A2f, A5c): the LTEE count is partly a function of μ.

## Assumptions
- Stated: fixation rate is the measured quantity; mutation supply is not what limits it.
- Implicit: the response of fixation rate to μ is nil or small (A5d); the observed mammalian record is informative.

## Responses
- Against: A5, A5a, A5b, A5c all argue the rate depends on supply; A5d's own data show a positive response; Tenaillon (6 mutator populations carry 96.5% of point mutations) shows that supply and fixation counts are linked in the LTEE.
- In support: Camestros (CA-10): the number was intended as an average, not a time for an individual chromosome. Sublinear scaling (A5d).
- Weaknesses in the responses: the critics do not show an observed mammalian fixation faster than 1,600 generations either; the repo has no mammalian fixation data. Day's observational-absence claim is unfalsifiable on human timescales.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Tenaillon 2016 | six populations carry 96.5% of point mutations through hypermutability | verified |

## Pre-registered prediction
Not run. Prediction (Day): the response of fixation rate to supply is small. Prediction (critics): it is large with recombination. Covered by A-sim (file A) and by the exponent in A5b.

## Check
No script. Review: pending.

## Simulator variables implied
- Supply–rate relation as a user-chosen function (see A5b).
