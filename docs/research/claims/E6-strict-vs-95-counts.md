---
id: E6
title: "LTEE whole-population fixations are 5,496 by a strict lineage-aware definition against 8,679 by the naive ≥95% first-crossing rule; the later data paper says fixation events and intervals are not well-defined"
side: day
branch: E
parent: A2
edges: [{type: revises, target: A2}]  # supersedes the Z23003785 (2026-09-28) figure of 1,322 gen/fix, which the later paper does not restate
load_bearing: true  # Changes G_f for MITTENS: 1,322 (≥95% snapshot, Z23003785) to about 1,587 (strict non-mutator, derived). If the strict counts are right, the headline LTEE rate used in the shortfall slows by ~20%.
sourcing: firsthand
status: extracted
verdicts:
  internal: holds
  fidelity: unverifiable
  external: pending
---

## Statement (verbatim)
> "By this strict definition the twelve populations contain 5,496 whole-population fixations across 723,000 population-generations. A naive rule that counts the first time a mutation's pooled frequency reaches 95% — the method of most quick analyses, including an earlier draft of our own — returns 8,679."

Source: [Fixation in the LTEE](https://zenodo.org/records/23105291), Z23105291, 2026-10-02, Abstract (Q56, Q57).

> "The 37% difference is almost entirely composed of within-lineage sweeps: mutations fixed within one of two coexisting lineages, which read as ≥95% of pooled sequencing reads without ever being carried by the whole population."

Source: Z23105291, Abstract.

> "In a second section we show that the number of fixation events and the interval between them are not well-defined quantities in this system: because sweeps overlap and nest under clonal interference, every reasonable rule for grouping fixations into events yields a different count (a 2–3× range)."

Source: Z23105291, Abstract.

> "The average across all five non-mutator populations at 60,000 generations is 45.4 fixations, yielding a cumulative rate of 1,322 generations per fixation."

Source: [MITTENS 3.0](https://zenodo.org/records/23003785), Z23003785, 2026-09-28 (modified 2026-10-04), §4.1, p.6 (Q58). This is the superseded figure; the later paper does not restate 1,322.

## Formal statement
Counting rules: (i) strict whole-population: the authors' lineage-aware haplotype state 2 at the final time point (plus major-branch fixations in Ara+1 and Ara+3 dated from minor-branch extinction); (ii) naive first-crossing: first sample with pooled frequency ≥95%, no depth filter, no confirmation; (iii) Z23003785's snapshot count of mutations at ≥95% at each 10K timepoint.

Table 1 (Z23105291), strict / within-lineage / first-crossing by population: Ara+2 66/0/66; Ara+4 73/0/80; Ara+5 14/105/63; Ara-5 9/173/96; Ara-6 27/107/59 (non-mutators); Ara+1 98/50/115; Ara+3 1,572/447/1,838; Ara+6 1,601/1,756/2,594; Ara-1 268/1,692/621; Ara-2 94/1,816/1,094; Ara-3 796/0/820; Ara-4 878/1,020/1,233. Totals 5,496 / 7,166 / 8,679; "inflation removed" 3,183.

derived (R2 recompute, python3):
- Column sums: strict 5,496; within-lineage 7,166; first-crossing 8,679; difference 3,183; generation sum 723,000 (all hold).
- (8,679 - 5,496)/8,679 = 36.7% (the paper's "37% difference" is the share of the naive count removed). Relative to the strict count the naive rule overcounts by 8,679/5,496 - 1 = 57.9%. The parameters.yaml / ledger wording "the ≥95% rule inflates counts 37%" is therefore the share removed, not the inflation (note for the ledger; not changed here).
- Non-mutators (5): strict total 189, mean 37.8, 60,000/37.8 = 1,587 gen/fix (parameters.yaml `ltee.gens_per_fixation.day_23105291_strict_nonmutator`; holds); first-crossing total 364, mean 72.8, 60,000/72.8 = 824; Z23003785 snapshot: mean 45.4, 1,322. Three rules, three rates: 824, 1,322, 1,587 gen/fix.
- Z23105291's own cross-check rule differs from Z23003785's: it "is known to miss genuine whole-population fixations whose pooled frequency dips below 95% after fixing" (in Ara-3 it misses 111 of 796).
- Mutators (7): strict total 5,307 over 424,500 population-generations = 0.0125 per generation; non-mutators 189 over 298,500 = 0.000633; ratio 19.7 (E7).
- whole_pop_fixations_lineage_aware in `parameters.yaml` (5,496 over 723,000) is verified to the Table 1 sums.

## Assumptions
- Stated: state 2 is "the authors' lineage-aware inference that every cell carries the mutation, not a direct per-cell observation"; validated against clone genomes ("present in sequenced clones in 98% of checkable cases").
- Implicit: that Good et al.'s state calls are right (the Good SI was not retrieved by the repo; fidelity ledger: "unverified"); that the 12 populations at unequal endpoints (57,500-63,500) can be summed ("not strictly on a common footing", Z23105291).

## Responses
- Against: none yet (this is Day's own correction). Mansfield/Hancock-type critics would note the paper concedes the G_f measurement problem.
- In support: the critics' point E5 (Ara-2, Ara+5) is consistent with the corrected counts.
- Weaknesses in the responses: no outside review of Z23105291.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Good 2017 | "This striking separation of timescales between inter- and intra-clade fixations cannot be explained by clonal interference" | consistent with the data paper's separation of whole-population fixations from within-lineage sweeps; the ≥95% rule itself not in the main text (ledger) |

## Pre-registered prediction
- Under the claimant's model (Z23105291): strict whole-population counts total 5,496; mutator/non-mutator ratio is sublinear (about 20x for a ~100x rate; E7).
- Under the opposing model (Z23003785's ≥95% snapshot): 1,322 gen/fix.
- Result that would change a verdict: re-derivation of the strict counts from the Good 2017 repository files (not available in the repo's raw set) that reproduces Table 1 exactly (then fidelity: accurate), or fails (then the strict count is not reproducible).

## Check
Script: none yet (spec: `research/checks/e6_ltee_counts.py`, planned; read `LTEE-metagenomic` data_files, apply state 2 and ≥95% rules, compare with Table 1). · Result: not run (the Table 1 sums above are arithmetic on the paper's own table) · Review: pending

R4 E5/E6 (research/checks/results/R4-E5E6.md; review #19, 2026-10-09): Table 1 sums and all derived figures reproduce from the raw text. Non-mutator G_f is 1,322 (snapshot), 824 (first crossing), 1,587 (strict, +20.1% on 1,322) and 523 (strict plus within-lineage); a 3.04x spread, which bears out the abstract's own statement that counts are rule-dependent. No Good 2017 files in the repo, so the state calls are not re-derived (fidelity stays unverifiable; external pending). Verdicts unchanged.

## Simulator variables implied
Counting rule, endpoints per population, lineage structure, mutator classification.
