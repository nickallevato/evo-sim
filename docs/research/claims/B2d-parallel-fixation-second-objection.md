---
id: B2d
title: "Second objection: fixations run in parallel; steady-state flux is mu regardless of transit; the pipeline cannot fill"
side: day
branch: B
parent: B2
edges: [{type: supports, target: B2}, {type: attacks, target: F1}]
load_bearing: false  # Day concedes the throughput point; the live dispute is the fill state (B1c)
sourcing: firsthand
status: extracted
verdicts:
  internal: holds
  fidelity: n/a
  external: pending
---

## Statement (verbatim)
> At steady state the total flux out is μ per site regardless of how long any individual site took to traverse.

Source: [Z22129121, The Hard Limits of Fixation Through Genetic Drift (Day & Athos)](https://zenodo.org/records/22129121), Zenodo 2026-08-27 (v1), §The Second Objection

> “Nothing finishes in the species lifetime” is simply wrong as a claim about throughput, and the drift limit does not depend on it.

Source: [Z22129121, The Hard Limits of Fixation Through Genetic Drift (Day & Athos)](https://zenodo.org/records/22129121), Zenodo 2026-08-27 (v1), §The Second Objection

> The correct interpretation is narrower: the pipeline cannot fill.

Source: [Z22129121, The Hard Limits of Fixation Through Genetic Drift (Day & Athos)](https://zenodo.org/records/22129121), Zenodo 2026-08-27 (v1), §The Second Objection

## Formal statement
Day's position, in glossary terms: **throughput** at steady state = μ; the claim is about **fill state** (transient), not about latency bounding throughput. This is the same logical point as Mansfield's time between successive fixations (F1), accepted in this paper and restated in the Education post as an analogy about a machine running multiple jobs simultaneously (F1a).

## Assumptions
- Stated: Many pipes in parallel, each on its own 4Nₑ delay.
- Implicit: The pipes start empty (B1c) or are refilled only by ancestral conditions (B1d).

## Responses
- Against: "Obviously, mutations, whether neutral or not, do not have to increase in frequency throughout a population one at a time." ([McCarthy, "Vox Day Responds"](https://dennismccarthy.substack.com/p/vox-day-responds), 2026-09-17, para 22 (McCarthy))
  "The time it takes for one allele to get fixed is not important, it is the time BETWEEN successive fixations that is important." ([Mansfield (@brianmansfield6912), YouTube comments under Examining Origins video jDxFtCOGZ3A](https://www.youtube.com/watch?v=jDxFtCOGZ3A), comments retrieved 2026-10-07, comment UgyhNduYke46IStQ5pd4AaABAg.AbQefbrLxzSAbR9n0iZNuQ (Mansfield))
- In support: RESULTS F1 confirms that, without interference, many fixations are in flight at once and rate = 2N·U_b·u regardless of latency.
- Weaknesses in the responses: Critics' replies (written before HL, 2026-08-27) do not engage the "cannot fill" restatement; HL does not engage the equilibrium-start result of RESULTS B1.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| none cited | n/a | n/a |

## Pre-registered prediction
Written **before** the check runs.
- Under the claimant's model: Throughput is μ only once the pipe is full; before that it is μ·F(T).
- Under the opposing model: If the ancestral pipe was full (equilibrium), μ·T is delivered over T.
- Result that would change a verdict: B1c.

## Check
Related done checks: `research/checks/b1_start_state.py`, `research/checks/f1_throughput.py` (see B1, F1).

## Simulator variables implied
- pipe state at t=0
- number of independent loci
