---
id: B
title: "Neutral theory (k = mu) cannot rescue the shortfall"
side: day
branch: B
parent: ROOT
edges: [{type: supports, target: ROOT}, {type: depends-on, target: B1}, {type: depends-on, target: B2}, {type: depends-on, target: B3}, {type: depends-on, target: B4}, {type: attacks, target: B5}, {type: attacks, target: B6}, {type: attacks, target: B7}]
load_bearing: true  # ROOT as worded ("no evolutionary mechanism") fails if neutral drift can supply the fixations
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: partial
  external: contested
---

## Statement (verbatim)
> There is absolutely nothing Dennis McCarthy or anyone else can do at this point to salvage either natural selection or neutral theory as an adequate engine for evolution and the origin of species. The one is far too weak to account for the empirically observed genetic changes and the second is flat-out wrong.

Source: [Day, "Response to Dennis McCarthy, Round 2" (blog)](https://voxday.net/2026/02/04/response-to-dennis-mccarthy-round-2/), 2026-02-04, ¶60 of extracted text

> The domain of k = μ is confined to demographic conditions that no non-endangered species is capable of meeting.

Source: [Z22129121, The Hard Limits of Fixation Through Genetic Drift (Day & Athos)](https://zenodo.org/records/22129121), Zenodo 2026-08-27 (v1), p.1 (abstract)

## Formal statement
Branch summary (verdicts as of this extraction; "pending" = no repo check yet):
| Claim | Side | Internal | Fidelity | External | Check |
|---|---|---|---|---|---|
| B1 empty pipeline / E[F(T)] | day | holds (empty start) | n/a | contested | B1 done; B1c queued |
| B1d Day's later full-but-short-pipe reply | day | pending | n/a | pending | arithmetic only |
| B2 Hard Limits | day | pending (children: B2a holds, B2b holds, B2c holds) | unverifiable | contested | B2a done |
| B3a k = μN/Nₑ | day | holds (algebra) | misread | contradicted (exchangeable class) | B3 done; B3b queued |
| B3g Day's retraction of B3a | day | holds | accurate | supported | blog 2026-08-27 |
| B3b/B3c Balloux–Lehmann, RRME 0.743 | day | pending | partial | pending | B3b queued |
| B3d k = 32.3μ | day | pending | unverifiable | contested | no derivation |
| B4 clock recalibration | day | holds (arithmetic) | unverifiable | contested | B4a queued |
| B5 k = μ identity (critics) | critic | holds | accurate | contested | B0.5 done |
| B6 ancestral pipe full / polymorphism | critic | holds | n/a | pending | B1c, B4a queued |
| B7 1/(2N) | critic | holds | accurate | supported (exchangeable) | B3 done |
| F1 latency ≠ throughput | critic | holds | n/a | contested (feasibility) | F1 done; F2 queued |
Arithmetic findings on both sides are in the child files (McCarthy 22.5M ✓, Mansfield 1/gen ✓ and 44× short, Hancock 76.8 → 19.4M (SNV haploid) vs 38.3M (SV-inclusive halved), relayed 7.2M ✓, Day 8.25 ✓ but sign-inconsistent, 800,000μ ✓, 228,000 ✓ (Vₖ = 5) with 29 billion not reproducible at the same ratio, 19,800 ✓ as a latency, k = 32.3μ not reproducible).

## Assumptions
- Stated: k = μ is a steady-state identity (B1), domain-limited (B2), mis-derived (B3), or its dates circular (B4).
- Implicit: The start state and demography decide B1/B2; Day withdrew the N/Nₑ leg (B3g) and later conceded a full ancestral pipe (B1d).

## Responses
- Against: B5 (critics): k = μ applies; B6: ancestral pipe full and polymorphism; B7: P_fix = 1/(2N).
- In support: Hössjer agrees the dating of divergence leans on neutral theory (B4f).
- Weaknesses in the responses: Day's own Hard Limits paper accepts k = μ "throughout" and Day conceded the Nₑ equivocation; the surviving B-branch arguments (B1d, B2, B3b/c/d) have not been tested against a sourced demography (B1c) or a B&L-style simulation (B3b).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura 1962; Kimura & Ohta 1969 | see B7a, B7b | accurate for 1/2N and 4Nₑ |
| Balloux & Lehmann 2012 | see B3b | verified-partial |

## Pre-registered prediction
Written **before** the check runs.
- Under the claimant's model: Neutral drift cannot supply the fixations in the available time.
- Under the opposing model: Neutral drift supplies μ per site per generation once the pipeline is full; the pipeline was full (B6) and the window is long relative to transit (B5f).
- Result that would change a verdict: B1c and B3b results.

## Check
See B1c, B3b, B4a (proposed) and the done checks B1, B1b, B2a, B3.

## Simulator variables implied
- fill state
- Nₑ(t)
- overlap and N(t) fluctuation
- neutral fraction
