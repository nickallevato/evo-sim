---
id: A6
title: "Sweep signatures are absent: 3,200+ sweeps over 325,000 generations would saturate selection scans, which find only dozens to hundreds of candidate regions"
side: day
branch: A
parent: A  # branch A, not H: the passage defends MITTENS's all-fixations model (every fixation sweep-carried, hitchhikers included) against the hitchhiking escape; the 3,200 is a sweep count from Day's linkage-block arithmetic, not a cost-of-selection bound (H)
edges: [{type: supports, target: A}]
load_bearing: false  # an empirical corollary offered against the hitchhiking objection; A's arithmetic does not depend on it
sourcing: firsthand
status: checked
verdicts:
  internal: pending   # R4 GAP-02: does not follow at the stated 3,200 with the sourced ~10,000-generation window (<= 98 detectable at power 1, i.e. 'dozens to hundreds'); at the top of Day's own block range (32,000) or N_e 33,000 the upper bound is ~1,000-3,250, so the inference depends on scan power and a comparator that is not threshold-limited (softened from non-sequitur in the review pass)
  fidelity: partial   # per-scan counts accurate (Voight 2006 ~250 per population, abstract; Sabeti 2007 > 300 regions), but the cited scans target incomplete or population-specific sweeps via top-1% lists; the union of nine scans is 5,110 candidate regions, 722 replicated (Akey 2009)
  external: contested   # premise supported: classic sweeps rare (Hernandez 2011 trough test); saturation inference not shown; the constraint bears on hitchhiking-as-main-source of fixations, whoever holds it
---

## Statement (verbatim)
> (4) The genomic signatures are absent. If 3,200+ sweeps occurred in the human lineage over 325,000 generations, approximately one sweep completes every 100 generations.

Source: [The Universal Failure of Fixation: MITTENS Applied Across the Tree of Life](https://zenodo.org/records/18452504), Z18452504, 2026-02-02, §4.3 "Linkage and Hitchhiking", item (4) (raw `sources/raw/day/zenodo-18452504.txt` l.325).

> The human genome does not display these signatures at the required scale. Diversity is relatively uniform across the genome. Tajima's D is close to zero genome-wide.

Source: same, l.330.

> The absence of sweep signatures is not merely an argument from silence. Scans for positive selection in humans (Voight et al. 2006; Sabeti et al. 2007; Pickrell et al. 2009) identify dozens to hundreds of candidate sweep regions—not thousands. If 3,200+ sweeps had occurred, selection scans would be saturated with signals. They are not.

Source: same, l.331.

Context (same section, l.318): "The human genome of 3.2 Gb therefore contains 3,200–32,000 independent linkage blocks. If every sweep fixed all variants in its block, 3,200–32,000 independent sweeps would be required". Item (6), l.333 (not tested): "Fixed differences are distributed across the genome in patterns consistent with site-by-site accumulation, not block-wise replacement."

## Formal statement
Sweeps per generation = K / T = 3,200 / 325,000 ≈ 1 per 100 generations. Day's implicit prediction: the number of sweep signals visible to scans is of order K ("thousands"), so observed counts of "dozens to hundreds" refute K ≥ 3,200.

`derived:` (R4 GAP-02) expected detectable completed sweeps at power 1 = K × W / T, with W ≈ 10,000 generations (Hernandez 2011, citing Przeworski 2002): 98 at K = 3,200; 985 at K = 32,000; 325–3,250 at W = 33,000 (0.25 × 4 × Day's upper N_e of 33,000, MITTENS 3.0 §8.2).

## Assumptions
- Stated: 3,200+ sweeps over 325,000 generations; sweep signatures are reduced diversity, extended haplotype homozygosity, negative Tajima's D and elevated LD near fixed differences.
- Implicit: signatures of completed sweeps persist over the whole lineage (no detection window); scans have high power for every sweep; scan candidate counts are counts of real sweeps (not threshold-limited outlier lists); the cited haplotype scans detect completed lineage-wide sweeps.

## Responses
- Against: no critic has replied to this passage (gaps.md S17). DarwinZDF42 (Reddit [1wv4zeg](https://www.reddit.com/r/DebateEvolution/comments/1wv4zeg/), comment pd99y5x) argues the position the passage targets: "Ignores how selective sweeps cause many fixations, mostly for neutral variation"; also Reddit 1wss2wj, comment pcovtvf: "ignores that selective sweeps result in the fixation of many loci at once, most of them neutral". KITTENS (`sources/raw/critics/arctic-title-MITTENS.json`) answers the hitchhiking premise differently: hitchhiking "is confined to the neighborhood of a sweep".
- In support: Hernandez et al. 2011 ("Classic selective sweeps were rare in recent human evolution"); Yoo et al. 2025 SweepFinder2 finds 11–62 hard-sweep candidates per ape taxon (power-limited).
- Weaknesses in the responses: the critics who lean on hitchhiking have not answered the diversity data; the critics who say most differences fixed by drift do not need to. Day's own block arithmetic here argues that hitchhiking cannot carry the load ("each block must accumulate ~2,000 fixed differences on average", l.322; `derived:` 20M / 3,200–32,000 = 600–6,250 per sweep), a window-free point in his favour against hitchhiking-heavy critics. MITTENS 3.0 §8.2 (2026-09-28) later says of human neutral fixations "The remainder are hitchhikers"; the two statements are in tension (R4 GAP-02 review pass).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Voight et al. 2006 (PLoS Biol 4:e72) | "the strongest ∼250 signals of recent selection in each population"; scan for "variants that have not yet reached fixation" (abstract) | partial: count accurate; incomplete sweeps, not completed ones |
| Sabeti et al. 2007 (Nature 449:913) | "more than 300 strong candidate regions"; XP-EHH detects alleles "risen to near fixation in one but not all populations" | partial: count accurate; population-specific sweeps |
| Pickrell et al. 2009 (Genome Res 19:826) | 1% tail outlier approach; no total count | partial |
| Akey 2009 (Genome Res 19:711; not cited by Day) | "5110 distinct regions were identified in one or more study"; "only 722 regions (14.1%) were identified in two or more studies" | context: "not thousands" incomplete |

## Pre-registered prediction
R4 GAP-02 (`research/checks/gap02_sweep_window.py`, committed b812741 before the run). P1: Day's 3,200 / 325,000 gives 39–98 detectable completed sweeps in a 4,000–10,000-generation window. The falsifier (E > 1,000) could not fail by construction; recorded as an arithmetic consequence of the model, not a test.

## Check
R4 GAP-02 (research/checks/results/R4-GAPS-04-07-02.md): E_detect is an upper bound (power 1). Day's stated 3,200 gives ≈ 98 in the sourced ~10,000-generation window (Hernandez 2011), i.e. "dozens to hundreds"; his block range top (32,000) gives 985, and N_e = 33,000 gives up to 3,250. The cited scans are top-1% lists of mostly incomplete sweeps, so a count comparison is threshold-limited. Hernandez's trough test supports the premise that classic sweeps were rare (< 10% of human-specific amino-acid substitutions strongly favoured). Review: `research/checks/REVIEW.md` (review #6, 2026-10-08).

## Simulator variables implied
Sweep count K, detection window W (statistic- and N_e-dependent), detection power by s (4N_e·s ≳ 400), soft vs hard sweeps, sweep footprint r/s.
