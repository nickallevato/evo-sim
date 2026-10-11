---
id: DN5
title: "CSAC 2005 (as relayed by Day): human-chimp Ka/Ks = 0.23 on 13,454 orthologous genes"
side: literature
branch: ROOT
parent: DN1
edges: []
load_bearing: false
sourcing: secondhand
status: extracted
verdicts:
  internal: n/a
  fidelity: pending   # CSAC 2005 text not read for this value; only Day's relay (rule U: relays are not scored internal)
  external: pending   # R4 L1 fix pass, proposed for integration: supported (in kind): an independent pipeline gives 0.207 on Ensembl one2one genes (release 116) and 0.200 with CSAC-like quality filters; fidelity waits for CSAC 2005 and an independent ML estimate to be fetched (critic-side review #3)
---

## Statement (verbatim)
> When the same 2005 Consortium reported the canonical Ka/Ks ratio, which is advertised as the measure of natural selection's strength in coding sequences, they reported 0.23.

Source: Day's relay, [Day, "How Biologists Keep 'Proving' Selection"](https://voxday.net/2026/10/11/how-biologists-keep-proving-selection/), 2026-10-11, ¶5 (Q173 note). Primary: CSAC 2005, Nature 437:69 (not read for this value).

## Formal statement
Ka/Ks = 0.23 over 13,454 human-chimp 1:1 orthologs (CSAC 2005, per Day).

## Assumptions
- Implicit: 1:1 orthologs with complete, well-aligned CDS.

## Responses
- Against (Day, DN3): the 13,454 set is curated and excludes a third of genes.
- In support (audit, R4 L1): the value reproduces in kind on an independent pipeline.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| CSAC 2005 | not read | pending |

## Pre-registered prediction
L1 critic side: O121 in 0.20-0.30.

## Check
R4 L1 (`research/checks/results/R4-L1.md`; reviews a352991; fix pass).

## Simulator variables implied
- none
