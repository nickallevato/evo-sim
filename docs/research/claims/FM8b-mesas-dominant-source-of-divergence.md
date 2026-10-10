---
id: FM8b
title: "Day, 'The Fourth Mechanism' FM8(b): the mesa signature is 'the dominant source of genomic divergence between humans and the great apes'"
side: day
branch: ROOT
parent: ROOT-FM
edges: [{type: supports, target: ROOT-FM}]
load_bearing: false  # one of three dialectic claims in Q169; no fraction given
sourcing: firsthand
status: reviewed
verdicts:
  internal: n/a   # no derivation or fraction stated
  fidelity: n/a
  external: contradicted   # R4 FM: for single-nucleotide divergence on alignable sequence, human mesas hold 1.25-2.5% of human-chimp differences. Structural, indel and SD divergence not measured (silent). Alternative: contested (if structural divergence is held to dominate)
---

## Statement (verbatim)
> what the data establish beyond any dispute is that a) the mesa signature exists, b) that it is the dominant source of genomic divergence between humans and the great apes, and, c) no account of speciation is complete without it.

Source: [Day, "The Fourth Mechanism" (blog)](https://voxday.net/2026/10/10/the-fourth-mechanism/), 2026-10-10, ¶7 (Q169, FM8). Rule RH: mixed; "beyond any dispute" is rhetorical intensifier (ledger RH-7); (a), (b), (c) are dialectic. (a) is supported (see FM4); this file carries (b).

## Formal statement
Fraction of human-chimp single-nucleotide differences inside human mesas (denominator: the cell's used windows).

## Assumptions
- Implicit: "genomic divergence" is single-nucleotide divergence; structural divergence (Yoo 2025 SDRs, 327 Mb per lineage) is outside the check.

## Responses
- Against (critic): 1.25-2.5% is not dominant.
- In support (Day): the claim may refer to total (structural) divergence, on which this check is silent.

## Primary literature
Yoo et al. 2025 (SDR average 327 Mb per lineage; fidelity ledger).

## Pre-registered prediction
`fm_mesa_replication.py` (d723064) DHC share.

## Check
R4 FM. Defeater d396.

## Simulator variables implied
- divergence partition: SNV vs structural
