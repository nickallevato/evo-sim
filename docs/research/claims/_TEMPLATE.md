---
id: X0
title: ""
side: day | critic | ally | literature
branch: A | B | C | D | E | F | G | H
parent: ROOT
edges: []            # e.g. [{type: attacks, target: B1}, {type: supersedes, target: A3-v2}]
load_bearing: false  # does ROOT fail if this claim fails?
sourcing: firsthand | secondhand
status: draft        # draft | extracted | checked | reviewed
verdicts:
  internal: pending      # holds | arithmetic-error | non-sequitur | pending | n/a
  fidelity: pending      # accurate | partial | misread | unverifiable | pending | n/a
  external: pending      # supported | contested | contradicted | untestable | pending | n/a
---

## Statement (verbatim)
> quote

Source: [title](url), date, version, locator (paragraph, page or equation)

## Formal statement
Equation, with every parameter named. Values are taken from `parameters.yaml` keys.

## Assumptions
- Stated:
- Implicit:

## Responses
- Against:
- In support:
- Weaknesses in the responses:

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|

## Pre-registered prediction
Written **before** the check runs.
- Under the claimant's model:
- Under the opposing model:
- Result that would change a verdict:

## Check
Script: `research/checks/...` · Result: · Review: `research/checks/REVIEW.md#...`

## Simulator variables implied
