---
id: B6c
title: "Hancock: a serial one-at-a-time model predicts no genetic variation among individuals except the sweeping allele"
side: critic
branch: B
parent: B6
edges: [{type: attacks, target: B1}, {type: attacks, target: G2g}]  # judgement (2026-10-08): Hancock attacks a strictly serial model; G2g is Day's 'fixation must be sequential' (Appendix A); G1 (Day) denies seriality, so the old B6c -> G1 target was mis-aimed
load_bearing: false  # an empirical-consequence argument; not quantified on screen
sourcing: firsthand
status: extracted
verdicts:
  internal: holds   # R4 X1 rule rev 2 (was pending): conditional prediction is correct; applicability to Day is G2/F1a
  fidelity: n/a
  external: pending
---

## Statement (verbatim)
> there would basically be no genetic variation amongst individuals except for the mutation that's increasing in frequency

Source: [Gutsick Gibbon + Zach Hancock, "No, Vox Day's AI-Generated Books Did Not Debunk Evolution" (auto-captions)](https://www.youtube.com/watch?v=_Vu0ZVVjwHc), 2026-10-03, t=01:33:59 (auto-caption)

> it assumes that each mutation has to both arise and go to fixation before the next

Source: [Gutsick Gibbon + Zach Hancock, "No, Vox Day's AI-Generated Books Did Not Debunk Evolution" (auto-captions)](https://www.youtube.com/watch?v=_Vu0ZVVjwHc), 2026-10-03, t=01:31:58 (continues "mutation can occur." in the 01:32:18 chunk; Hancock responds to the 180-interval, 252,000/1,400 presentation; the attribution to Day's own equation is tested in F1a)

## Formal statement
Under strictly serial fixation (one allele at a time), heterozygosity would be ≈ 0 except at the single segregating site. Observed neutral diversity: θ = 4Nₑμ ≈ 4.8×10⁻⁴ per site at Nₑ = 10⁴, μ = 1.2×10⁻⁸ (derived), i.e. ≈ 1.5×10⁶ segregating differences per genome pair at 3.2×10⁹ sites. Day does not claim a serial model for neutral fixation (B2d: "Fixations run in parallel" is conceded), so the prediction applies to the reading in F1, not to Day's stated position.

## Assumptions
- Stated: MITTENS encodes sequential fixation.
- Implicit: F_max = t/(g G_f) is a serial-throughput bound.

## Responses
- Against: Day (EDU): G_f is a throughput measurement that already includes parallelism (F1a).
- In support: Observed standing variation (π > 0).
- Weaknesses in the responses: The attribution rests on Hancock's reading; Day's Q&A computes 19,800 "generations per fixation" from a latency formula (F1a), which supports the serial reading for that figure.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| none cited | n/a | n/a |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: (Hancock) serial model predicts no standing variation.
- Under the opposing model: (Day) not a serial model.
- Result that would change a verdict: F1a quote analysis.

## Check
Script: none.

R4 X1 (research/checks/results/R4-X1-rescore.md; rule research/checks/results/R4-X1-verdict-rule.md rev 2; review #12, 2026-10-09): under the single both-sides rule this node is holds / n/a. conditional prediction is correct; applicability to Day is G2/F1a Charitable reading tried: tried the conditional reading.

## Simulator variables implied
- standing variation display
- serial vs parallel throughput mode
