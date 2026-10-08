---
id: E1
title: "LTEE fixation counts include hitchhiked neutral and mildly deleterious mutations, so G_f is not a measure of beneficial-sweep throughput (Barrick 2009)"
side: critic
branch: E
parent: A2
edges: [{type: attacks, target: A2}]
load_bearing: false  # Affects how G_f (A2) is read (all-cause versus beneficial-only); Day already reports an "all-cause" and a "beneficial-only" figure, so ROOT is not changed by the wording alone.
sourcing: firsthand
status: draft
verdicts:
  internal: pending
  fidelity: pending
  external: pending
---

## Statement (verbatim)
Attribution gap: the hierarchy (v1, pass 1) lists this under a critic called "Taylor", with "Barrick 2009 45 muts/20k". No critic quotation under that name exists in `sources/quotes-critics.md` or the R1 critic corpus, and Taylor 2001 in `bib-literature.md` is a protein-design paper. No verbatim critic statement has been located; the unsourced attribution is carried in `PLAN.md` only. What the repository does hold are the literature statement and Day's own wording:

> "Such clock-like regularity is usually viewed as the signature of neutral evolution, but several lines of evidence indicate that almost all of these mutations were beneficial."

Source: Barrick et al. 2009, [Nature 461:1243](https://www.nature.com/articles/nature08480), Abstract (Europe PMC copy; full text paywalled).

> "The real, updated 60-generation LTTE numbers are: 4,615 generations per beneficial fixation (natural selection) 1,322 generations per all-cause fixation (natural selection + neutral theory + everything else)"

Source: Day, [The Temperature Rises](https://voxday.net/2026/09/27/the-temperature-rises/), B2026-09-27-the-temperature-rises, 2026-09-27, ¶13 (quote Q61). Day's own text distinguishes beneficial-only from all-cause G_f.

## Formal statement
G_f(all-cause) = generations / (fixed mutations of any fitness effect); G_f(beneficial) = generations / (fixed beneficial). The MITTENS rate argument applies G_f to the number of differences to be explained, which includes neutral changes. Parameters: `ltee.gens_per_fixation.day_mittens3_nonmutator` = 1,322 (all-cause, >=95% snapshot rule); `ltee.gens_per_fixation.day_ns_only_parallel_max` = 4,615 (blog only; Z23003785 gives about 1,408 per beneficial fixation by clone pair).
derived: 4,615/1,322 = 3.5; the implied beneficial share of all-cause fixations = 1,322/4,615 = 29% (if the two blog numbers share a time base; the sources do not state this).

## Assumptions
- Stated (Barrick abstract): "almost all" of the early fixed mutations were beneficial; Tenaillon 2016 (E8): non-mutators "support a model where most fixed mutations are beneficial ... and neutral mutations accumulate at a constant rate".
- Implicit: that hitchhiker mutations counted in G_f are the ones a critic would call "free" in the human comparison, and that the all-cause G_f is the right one to compare with 17.5-205M total differences (Day uses the all-cause figure for the comparison with all differences).

## Responses
- Against: Day (blog 2026-09-27): reports both figures; the all-cause rate is the one used for the total-difference comparison.
- In support: Day's own distinction.
- Weaknesses in the responses: the beneficial-only figure 4,615 appears only in blog posts (parameters.yaml note); the repo has no verbatim critic to attribute this to.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Barrick 2009 | "Although adaptation decelerated sharply, genomic evolution was nearly constant for 20,000 generations." | accurate to its abstract; the "45 mutations in 20,000 generations" detail is not in the abstract (unverified) |
| Tenaillon 2016 | "neutral mutations accumulate at a constant rate" (non-mutators) | verified (fidelity ledger) |

## Pre-registered prediction
- Under the critic's model: a large share of LTEE fixations are hitchhikers or neutral, so all-cause G_f says little about how fast beneficial alleles fix.
- Under Day's model: all-cause G_f is the correct quantity for total differences, and beneficial-only G_f (about 4,615) is slower still.
- Result that would change a verdict: a fitness-effect classification of the 5,496 whole-population fixations of Z23105291 (beneficial / neutral / deleterious) showing the beneficial share (not derivable from the repo's sources).

## Check
Script: none (data classification required; planned only if the Good 2017 SI is obtained). · Result: not run · Review: pending

## Simulator variables implied
Fraction of fixations beneficial / neutral / deleterious, counting rule (all-cause versus beneficial).
