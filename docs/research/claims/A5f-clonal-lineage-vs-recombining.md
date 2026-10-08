---
id: A5f
title: "The LTEE is nonrecombining, one clone, one environment; sex and population-size variability change the fixation rate in mammals"
side: critic
branch: A
parent: A5
edges: [{type: attacks, target: A2e}]
load_bearing: false
sourcing: firsthand
status: reviewed
verdicts:
  internal: "holds"
  fidelity: partial
  external: "supported"   # direction (R_int 0.09 clonal vs 0.97 free); magnitude at LTEE scale extrapolated
---

## Statement (verbatim)
> It follows largely nonrecombining bacteria descended from one clone, repeatedly transferred into the same glucose-limited environment.

Source: [r/DebateEvolution, Dumb-and-Dumber](https://www.reddit.com/r/DebateEvolution/comments/1wss2wj/), 2026-09-28 (RE-07).

> Fixation rate in single cell organism is not equal to fixation rate in mammal. And there is two reasons for it. One is sexual reproduction. The second is variability of population size.

Source: [Whopping the floor](https://voxday.net/2019/02/11/whopping-the-floor/), 2019-02-11, ¶4 (GA-01). Gariépy's words as transcribed and posted by Day: secondhand.

## Formal statement
Claim: rate_human(recombining) ≠ rate_LTEE(asexual), direction unspecified by the quotes. The KITTENS text (A5b) argues the LTEE is where "interference is worst", so the LTEE rate is a lower bound for recombining genomes. Day's side (blog 2026-10-01): "recombination is a double-edged sword that also breaks linkage, imposes segregation costs, and exposes deleterious recessives".

## Assumptions
- Stated: the asexual setting differs from a sexual one; the direction of the effect is argued by KITTENS (interference reduces rate in clonal populations) and by Day (recombination hurts).
- Implicit: effects can be summed into a single factor.

## Responses
- Against (Day): [They Never Stop Lying](https://voxday.net/2026/10/01/they-never-stop-lying/) ¶6: "he also assumes that recombination will help speed up the fixation rate, which it won't"; Bowers reply (2026-03-04, point 3): "Recombination reshuffles existing variation; it does not accelerate the rate at which any individual allele increases in frequency. Kimura and Ohta (1969) established that expected time to fixation does not depend on recombination rate." The Bernoulli paper (Z18167588 s7.3) repeats this, citing Hartfield and Bataillon (2020). Z18165980 lists "recombination requirements" and Hill-Robertson interference as mechanisms that reduce fixation probabilities under concurrent fixation.
- In support: Good et al. 2017: the separation of timescales between inter- and intra-clade fixations "cannot be explained by clonal interference" (so clonal interference does not explain at least that observation); KITTENS §8: "in a 3-gigabase genome with several crossovers per meiosis, selected sweeps at distant loci proceed nearly independently, whereas the LTEE genome is one linkage group."
- Weaknesses in the responses: Kimura & Ohta 1969 is a single-locus model and the word "recombination" does not occur in it (ledger: misread/misattribution), so the cited authority does not address the point; the Hartfield and Bataillon citation was not retrieved. KITTENS gives no simulation. The Day-side statement that recombination is a cost does not quantify it, and the Z18167588 paper elsewhere (s7.10) distinguishes the Bernoulli Barrier from Hill-Robertson interference.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura & Ohta 1969 | "recombination" appears 0 times; a single-locus model | verified-misread (misattribution) |
| Good et al. 2017 | "This striking separation of timescales between inter- and intra-clade fixations cannot be explained by clonal interference" | verified; limited scope |

## Pre-registered prediction
No check run. Proposed A-sim arm: recombination on/off at fixed supply. Prediction (critics): rate per generation higher with free recombination. Prediction (Day): no gain, or net loss, from segregation cost. Result that would change a verdict: a monotone dependence of fixation rate on recombination rate in simulation at human-scale supply.

## Check
R4 F2 (research/checks/results/R4-F2-A.md): direction supported: recombination raises the rate (R_int clonal 0.088 vs free 0.975 at 2N*U_b = 32; fwdpy11 agrees at three points). The magnitude at LTEE scale (1.5-172x) is extrapolated, not simulated. Day's "double-edged sword" (recombination also breaks favourable combinations) is not tested (single s, no epistasis). Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)
Earlier note: Script: none. Review: pending.

## Simulator variables implied
- Recombination rate (0 to free), mating system toggle, population-size variability.
