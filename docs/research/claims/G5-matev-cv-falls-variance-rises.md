---
id: G5
title: "Matev: the Bernoulli Barrier's coefficient of variation falls as loci are added, but the variance of the beneficial-allele count rises, and selection responds to variance"
side: critic
branch: G
parent: G
edges: [{type: attacks, target: G}]
load_bearing: false  # restates a defect the audit's G derivation already records
sourcing: firsthand
status: extracted
verdicts:
  internal: holds   # K ~ Bin(n, p): Var = np(1-p) rises with n; CV = sqrt((1-p)/(np)) falls as 1/sqrt(n)
  fidelity: n/a
  external: n/a   # a mathematical point; G's own derivation states the same (Var n/4 = 39,250 at n = 157,000), and R4 G1 found no ~230 sweep cap under multiplicative fitness
---

## Statement (verbatim)
> "While this coefficient of variation does go to zero as n increases, the variance of the beneficial allele count of an individual just increases as n increases."

Source: [Matev, comment on McCarthy, "Why Probability Zero is Wrong About Evolution"](https://dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1/comment/338963242), 2026-09-17, comment id 338963242 (RF-1). Target: the Bernoulli Barrier paper (Z18167588), claim G.

## Formal statement
For n loci each carried with probability p, the count K ~ Binomial(n, p): E[K] = np, Var[K] = np(1-p), CV = sqrt((1-p)/(np)). `derived:` (python3 -I) n = 157,000, p = 0.5: Var = 39,250, SD = 198.1, CV = 198.1/78,500 = 0.252% (G's figures). Doubling n doubles Var and divides CV by sqrt(2). Under multiplicative fitness w = (1+s)^K, Var(ln w) = Var[K] (ln(1+s))^2, which also rises with n. Fisher's theorem relates the response to additive genetic variance in (log) fitness, not to the CV of the count.

## Assumptions
- Stated: free recombination and unlinked loci (as in the paper).
- Implicit: the paper's "fitness variance decreases" (s7.6) refers to the CV; Matev's same comment adds that fitness is written multiplicatively but evaluated additively in the paper's fitness ratio (not checked here against Z18167588).

## Responses
- Against: none located from Day.
- In support: claim G, Formal statement (`derived:` line on absolute variance, n/4 = 39,250); R4 G1 (no cap near 230 under multiplicative fitness, soft selection, free recombination).
- Weaknesses in the responses: Matev's additive-vs-multiplicative point and his "required population presupposes the extremes exist" point are stated without equations; not verified against the paper text.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Fisher 1930 | not retrieved (see G) | unverified |

## Pre-registered prediction
Not run (arithmetic only).

## Check
Arithmetic (python3 -I). From the 2026-10-09 corpus refresh (C-1). Proposed follow-up: check Matev's additive-vs-multiplicative claim against the Z18167588 fitness-ratio equation.

## Simulator variables implied
Fitness model (additive vs multiplicative) as an explicit option.
