---
id: B3f
title: "k = 800,000 mu from N = 8e9 and Ne = 1e4 (Day-Grok exchange, 2026-04-30)"
side: day
branch: B
parent: B3
edges: [{type: supports, target: B3a}]
load_bearing: false  # illustrative arithmetic from stipulated premises; withdrawn with B3a
sourcing: secondhand
status: extracted
verdicts:
  internal: holds
  fidelity: n/a
  external: contradicted
---

## Statement (verbatim)
> This equals 800,000 μ, not μ.

Source: [Day, "Conceding the Math" (blog; contains a Day-Grok exchange)](https://voxday.net/2026/04/30/conceding-the-math/), 2026-04-30, ¶36 of extracted text. **secondhand** (text produced by the AI system Grok, posted by Day; the premises were stipulated by Day's prompt)

> The cancellation requires N = N_e, which I have already conceded does not hold in real populations.

Source: [Day, "Conceding the Math" (blog; contains a Day-Grok exchange)](https://voxday.net/2026/04/30/conceding-the-math/), 2026-04-30, ¶33 of extracted text. **secondhand** (Grok, as posted by Day)

## Formal statement
k = (2Nμ)/(2Nₑ) with N = 8×10⁹, Nₑ = 10⁴ ⇒ 8×10⁵ μ (derived: 8e9/1e4 = 800,000 ✓). The computation is conditional on two propositions: supply uses census N, and fixation probability uses Nₑ, which the same post says the AI conceded. Not independent evidence for either premise.

## Assumptions
- Stated: Two conceded propositions (supply = census N; fixation probability = Nₑ).
- Implicit: The AI's earlier statements reflect knowledge, not agreement; the exchange is a leading chain.

## Responses
- Against: keruru and Day (B3g) later agree P_fix = 1/(2N).
- In support: Arithmetic only.
- Weaknesses in the responses: An LLM transcript is not a literature source.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| none cited | n/a | n/a |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: k/μ = 800,000.
- Under the opposing model: k/μ = 1 (B3a).
- Result that would change a verdict: B3a.

## Check
Script: none. Arithmetic computed in python3 -I.

## Simulator variables implied
- N/Nₑ ratio
