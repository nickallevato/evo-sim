---
id: D9
title: "Under N = 10,000 weasels, 12 offspring and s = 0.001, each Weasel letter takes 20,000 generations to fix and the 27-letter phrase 540,000 generations"
side: day
branch: D
parent: D
edges: [{type: depends-on, target: D2i},{type: supports, target: D}]  # D9 -> D was typed attacks; Day's target is Dawkins's Weasel, which has no node (argmap registry x:dawkins-weasel). Judgement: D9 read as support for D's 'time insufficient' premise (2026-10-08)
load_bearing: false  # illustrative; ROOT does not depend on the Weasel recomputation
sourcing: firsthand
status: extracted
verdicts:
  internal: holds      # 27 x 20,000 = 540,000; (2/s)ln(2N) = 19,807 for s = 0.001 and 396 for s = 0.05; but it assumes letters fix one after another and uses a deterministic sweep time
  fidelity: n/a      # Day's own calculation; no source
  external: contested      # conditional fix time is ~8,500 not ~20,000 (B0.4); parallel loci would complete in ~13,000; the Weasel as published is a different algorithm (D9a)
---

## Statement (verbatim)
> "If we apply Dawkins’s proposed 5% advantage to the population in the correct manner, we assume a selection advantage of five percent. Or s=.05. With the appropriate reproductive limit of 12 rather than 100, that means it will take 400 generations for the initial letter M to propagate throughout the species, and 11,000 generations for all 27 letters required to complete the phrase to do so."

> "However, Dawkins’s 5% probability was referring to the initial mutation, not the actual selection advantage, which is usually much more subtle, around s=0.001. And this gives us 20,000 generations for the initial letter M and 540,000 generations to complete the full phrase."

> "First, note that Dawkins’s “population of 100” is really just one weasel that has 100 kits a year, where you keep those with the desired letter and kill the others. That’s not a species. A real weasel has about six kits, up to twice a year. So plug in the real animal, with a minimum population of 10,000 so it’s not going extinct,"

> "A phrase letter initially appears in one weasel out of 10,000. For that letter to count toward completing the phrase, all 10,000 weasels have to end up carrying it. And the only way that happens is the slow way: that one weasel’s descendants slightly out-breeding everyone else’s, litter after litter after litter, until the whole population has it. That process is called fixation."

Source: [Probability Weasel](https://voxday.net/2026/09/12/probability-weasel/), 2026-09-12, voxday.net, paras 11, 12, 9, 10.

For comparison, Day on MITTENS (different claim): > "The MITTENS calculation does not assume sequential fixation."

Source: [The Education of a Population Geneticist](https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/), 2026-10-01.

## Formal statement
Parameters (Day's stated): N = 10,000 weasels; offspring 12 (not used in the formulas given); selection coefficient s = 0.05 (Dawkins 'advantage') or 0.001; L = 27 letters to be fixed. Per-letter time t_letter = (2/s)*ln(2N) (the deterministic logistic sweep time; this reproduces Day's figures: s = 0.05: 396 ~ '400'; s = 0.001: 19,807 ~ '20,000'). Total T = 27*t_letter serial: s = 0.05: 10,696 (Day '11,000'; 27*400 = 10,800); s = 0.001: 534,788 (Day '540,000' = 27*20,000). Ratio to Dawkins's 50 generations: 540,000/50 = 10,800 = 10^4.03 (Day: 'about 11,000x', 'four orders of magnitude'). All Day figures reconcile with these formulas. B0.4 shows (2/s)ln(2N) overshoots the mean time of an allele conditioned on fixing by ~2.3x at N = 1e4, s = 1e-3 (8,480 diffusion; 8,532 stochastic approximation).

## Assumptions
- Stated: (i) each letter must reach fixation in a population of 10,000; (ii) s = 0.001 is the 'actual selection advantage'; (iii) letters fix sequentially (sum over 27, 'all 27 letters required to complete the phrase'); (iv) 12 offspring is the reproductive limit.
- Implicit: no mutation-supply limit (a letter 'initially appears in one weasel'); no parallel fixation (contradicts the stance in D9's comparison quote, where Day says MITTENS 'does not assume sequential fixation'); haploid or genic, N is the size for the 2N copies in 20,000 = (2/s)ln(2N) (matches 2N = 20,000 copies); the Weasel 'target' fitness is replaced by a constant s.

## Responses
- Against: (a) 8,525 +- 39 generations is the simulated mean conditional fixation time at N = 1e4, s = 1e-3 (exploratory run, below; B0.4 gives 8,480 diffusion): the per-letter figure is overstated 2.3x. (b) Independent loci complete in parallel: the maximum over 27 loci has mean ~13,100 generations (exploratory), 41x below 540,000. (c) The published Weasel is a truncation-selection algorithm, not an s = 0.001 population (D9a). (d) Mutation supply: with realistic u the waiting time for each specific letter dominates: W = 1/(2N*u*2s); for u = mu/3 = 4e-9 per copy per generation, W = 6.25e6 per letter and the parallel maximum of 27 is H27 x W = 2.4e7 (derived), which exceeds 540,000; with Dawkins-like u = 0.05/27 per copy, W = 13.5 and the parallel completion ~53. So the figure depends on which of the two limits (sweep time vs mutation waiting) governs, which Day does not address.
- In support: Day's seriality is the same assumption as Ulam's (D4); if fixations are strictly sequential the sum is right.
- Weaknesses: both the Day and critic sides here are model-dependent; the exploratory numbers are not pre-registered.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Dawkins (as quoted in Day's post, from approxion.com) | 'a random sequence of 28 letters ... chooses the one which, however slightly, most resembles the target phrase' | secondhand quote |
| Kimura & Ohta 1969 | t_bar = 4Ne for neutral; conditional sweep times for beneficial: see B0.4 | accurate (ledger) |

## Pre-registered prediction
Written before the formal check (which is specified, not run). The numbers below in 'Check' were from a scratch run made while drafting and are exploratory, not pre-registered; the formal check is pre-registered here.
- Under the claimant's model (Day): letters fix serially, total T = 27*t_letter with t_letter = (2/s)ln(2N): 534,788-540,000 generations.
- Under the opposing model: independent loci each follow a conditional sweep time (mean ~8,500, sd ~1,900 at N = 1e4, s = 1e-3); the phrase completes at the maximum over 27 independent loci: ~13,000 (+ mutation waiting). Under a strictly serial rule the total would be 27 x 8,500 = 230,000.
- Result that would change a verdict: (i) a simulation with 27 linked, selected loci at s = 0.001 whose completion time exceeds ~10x the independent-locus maximum would support Day's seriality; (ii) any realistic u that makes mutation waiting dominate would support the 'longer than 540,000' direction; (iii) a completion time near 540,000 under any parallel implementation would support Day.

## Check
Exploratory scratch run (python3 -I, venv numpy, `research/checks/wf.py single_locus`, seed 20261007; not committed): N = 10,000 diploid (2N = 20,000 copies), genic s, start at one copy, conditional on fixation:
- s = 0.001: 2,409 fixations of 1.2e6 replicates (P_fix 0.00201; Kimura 0.00200); mean fixation time **8,525 +- 39**, sd 1,914. Serial 27 letters: mean total 230,053. Parallel, maximum of 27 independent draws (bootstrap): mean **13,092** (5th-95th percentile 10,992-15,417).
- s = 0.05: 5,656 fixations of 60,000 replicates (P_fix 0.0943; Kimura 0.0952); mean **332**; diffusion 326; Day's 396. Serial 27: 8,956; parallel max of 27: 422 (5th-95th 380-477).
Does not include mutation waiting, linkage or the 12-offspring rule (which Day's formulas do not use). Does it reconcile with Day? The per-letter time does not (8.5k vs 20k); the serial sum does not (230k vs 540k); the arithmetic of 27 x 20,000 does.
Formal check specification (later module, not run): WF with 2N = 20,000 copies, 27 loci, s in {0.001, 0.05}, mutation u from {0.05/27, 1.2e-8/3}, recombination r in {0, 0.5 free}, outputs: time to all-27 fixed; compare serial vs parallel predictions.

## Simulator variables implied
N, s, L=27 loci, offspring number (12), mutation supply u per letter, recombination r (linkage), serial/parallel switch, deterministic vs conditional-sweep time, truncation vs fitness-proportional selection.
