---
id: G1b
title: "Samson (ally): the total number of mutations separating species includes all of them, parallel or sequential; total divided by time is the rate"
side: ally
branch: G
parent: G1
edges: [{type: supports, target: G1}]
load_bearing: false
sourcing: firsthand
status: extracted
verdicts:
  internal: holds
  fidelity: n/a
  external: n/a
---

> **Mapping (2026-10-09): no attack warranted.** This node is mapped under the ratified definition (argmap/NOTES.md judgement call 12) with no defeater row, because it is an accounting identity both sides accept (the total separating species includes every fixation, however ordered); its weakness (an average required rate is not an upper bound on the achievable rate) is carried by A2e/A5 rows d003 and d008.


## Statement (verbatim)
> The total number of mutations separating species includes all of them. Parallel, sequential, or however else. Hence the word “total”.

Source: [Uncle John’s Band, "Not a Chance"](https://unclejohnsband.substack.com/p/not-a-chance), 2026-01-24, para 20 (UJ-01).

> And dividing “total” by “amount of time” gives a simple, unweighted average number. The rate.

Source: same post, para 20 (UJ-02).

## Formal statement
Observed divergence D over time T gives an average realised rate D/T regardless of how events overlapped. `derived:` 205e6/252,000 = 813 per generation (both lineages combined 1,627); 17.5e6/252,000 = 69.4 per generation per lineage. These are the average rates that the evolutionary process must have realised, whatever the pipeline structure.

## Assumptions
- Stated: all differences are counted, no matter how they arose.
- Implicit: the realised average required rate says nothing about whether the achievable rate (G_f-based) can match it.

## Responses
- Against: the quote file notes: an observed average divergence rate is not an upper bound on achievable rate. That is, the realised average (69 per generation) is a requirement, and the question of whether it can be met is the A5/A2e question.
- In support: it is correct that required count over time is an average whatever the overlap structure; Day uses the same point (G1).
- Weaknesses in the responses: it supports only the accounting identity, not the transfer of LTEE G_f.

## Primary literature
| (none cited in the claim) | n/a | n/a |

## Pre-registered prediction
No prediction; accounting identity.

## Check
Arithmetic audit (python3 -I, scratch).

## Simulator variables implied
- Display required average rate per generation next to achievable rate.
