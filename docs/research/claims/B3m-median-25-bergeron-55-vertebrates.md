---
id: B3m
title: "Day: 'a median factor of 25 across 55 vertebrates' (Bergeron et al. 2023, k/mu); recomputed from Bergeron's Table 9"
side: day
branch: B
parent: B3d
edges: [{type: supports, target: B3d}]
load_bearing: false  # cited as direct empirical falsification of k = mu; the 25 is a property of the tabulated terminal-edge rates
sourcing: firsthand
status: reviewed
verdicts:
  internal: n/a   # a reported statistic, no derivation by Day
  fidelity: accurate   # R4 B3m: median 25 (reproduced 25.4) and n = 55 are in Bergeron's published table on a matched per-year (equivalently per-generation) basis
  external: contested   # the 25 holds for the published terminal-edge (chronos lambda = 0) rates, but a lineage-average k from the same tree is at least about 2x mu (PH2, a LOWER bound); the 2-vs-25 gap is unexplained, not shown to be an artefact
---

## Statement (verbatim)
> The new validation work which uses Bergeron et al. (2023) on pedigree mutation rates and fossil-calibrated substitution rates for 55 vertebrate species

Source: Day, blog 2026-05-07 ¶3 (Q161; locator in `quotes-day.md` line 1201), with the "median factor of 25" figure as carried in B3d.


RH tag (2026-10-10 pass): dialectic (stated as a checkable claim or derivation; no rhetorical device scored).
## Formal statement
k/mu per species = tabulated substitution rate over pedigree mutation rate; median over 55 species (matched per-year or per-generation).

## Assumptions
- Implicit: the tabulated rate is a lineage-average rate; PH1 shows it covers about 21 Myr of a 416 Myr root depth.

## Responses
- Against (critic): the 25 is a terminal-edge artefact (short durations, rate variation under lambda = 0), not a lineage-average k.
- In support (Day): the number and the count reproduce exactly from the cited table; the critics' lineage-average estimate is itself above mu (about 2x, a lower bound).

## Primary literature
Bergeron et al. 2023, Table 9 (rates for 55 vertebrates; pedigree mu).

## Pre-registered prediction
`research/checks/b3m_bergeron_median.py` (5ca5f2e); post hoc diagnostics PH1, PH2 (382b580).

## Check
R4 B3m (`research/checks/results/R4-B3m.md`), review #48 (combined, low-stakes). A5: rescaling factor 1/25.4 reported. Open: which species failed the tree match (67 of 68). Defeaters d404-d406.

## Simulator variables implied
- per-species mu and k; tree-based lineage-average rate vs terminal-edge rate
