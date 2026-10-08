---
id: C3
title: "CCR5-delta32 under the strongest observed selection implies about 300 generations per fixation, later 2,278; humans do not fixate faster than 1,600 generations"
side: day
branch: C
parent: C
edges: [{type: supports, target: A2}, {type: supports, target: A}]
load_bearing: false  # Anecdotal check on the claim that G_f = 1,600 is a ceiling for humans; MITTENS 3.0 relies on the LTEE measurement, not on CCR5.
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: n/a
  external: pending
---

## Statement (verbatim)
> "A linear extrapolation, which would be generous, as the rate of spread typically slows as a mutation approaches fixation due to diminishing selective advantage, shows that a Europe-wide fixation would require approximately 300 generations, or roughly 6,000-7,500 years."

Source: [Darwin and the Black Death](https://voxday.net/2025/12/18/darwin-and-the-black-death/), B2025-12-18-darwin-and-the-black-death, posted 2025-12-18, ¶5 of extracted text.

> "This represents a fixation rate of approximately one mutation per 300 generations under extremely strong selective pressure within a geographically concentrated population."

Source: same post, ¶6.

> "Even if we very generously extrapolate from the existing CCR5-delta32 mutation that underwent the most intense selection pressure ever observed, the fastest we could get, in theory, is 2,278 generations"

Source: [An Inspiring Critique](https://voxday.net/2026/01/27/an-inspiring-critique/), B2026-01-27-an-inspiring-critique, posted 2026-01-27, ¶23.

> "it will require another 37,800 generations in the event that it happens to hit on its 10 percent chance of completing fixation from its current percentage of the global population."

Source: same post, ¶24.

## Formal statement
Observation: CCR5-delta32 at about 10% in Europeans after 27-34 generations (Dec 2025 post). Linear extrapolation: 10% in 30 generations gives 100% at 300 generations (derived: 30 x 10 = 300; at 20 y/gen this is 6,000 y, matching "6,000-7,500 years"; holds). Global rescaling in the Dec 2025 post gives 840 generations (50M deaths, 35.7% European share) and 1,440 (25M deaths, 400M world); the Jan 2026 post gives 2,278. Each of the three rescalings is stated without its arithmetic (the post lists assumptions but no formula), so the repo does not reproduce 840, 1,440 or 2,278 (no verdict).

Parameter link: this is a G_f estimate for humans, to compare with `ltee.gens_per_fixation` (1,600 / 1,322). The Dec 2025 post's own ratio "roughly five times faster than the bacterial rate" (1,600/300 = 5.3, derived) is reversed in Jan 2026 (2,278 generations, slower than bacteria).

## Assumptions
- Stated: the allele rose from a single copy under Black Death selection (1347-1351).
- Implicit: a linear extrapolation of an observed frequency is a fixation time (the Dec 2025 post concedes it is not); the event was a selective sweep and not partly drift or earlier; the frequency "after roughly 30 generations" is dominated by the 1347-1351 pulse and so is not a constant rate; that the Black Death selected CCR5-delta32 at all (the post says "scientific researchers ... propose").

## Responses
- Against: none located in the critic corpus (the example is not engaged). McCarthy's general objection is that mutations fix in parallel and per-genome supply is large (MC-03, MC-04).
- In support: none.
- Weaknesses in the responses: not engaged.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| none cited in either post for the CCR5 selection history | n/a | n/a |

## Pre-registered prediction
- Under the claimant's model: a single allele under the strongest recorded human selection would need at least 300 generations (or 840-2,278 globally) to fix.
- Under the opposing model: an allele with s of 0.1-0.3 for a few generations then removed has a trajectory unrelated to a fixation time; for a deterministic sweep with s = 0.1 from p = 1e-4 to 0.9 takes about (1/s) ln(p/(1-p) ratio) = 10 x (ln 9 + ln 9999) = 114 generations (derived from the haploid logistic; shown for scale only), so the "300 generations" is consistent with s of about 0.04 and is not a rate limit.
- Result that would change a verdict: a documented selection history (s, duration) for CCR5-delta32 that fixes the sweep time under a standard model and shows whether the 10% frequency is the end of a pulse.

## Check
Script: none (outside the first-wave checks). If run: deterministic logistic with a pulse of selection of stated length. · Result: not run · Review: pending

## Simulator variables implied
s as a function of time (pulse), p(t), generation length, geographic partitioning (European fraction of species).
