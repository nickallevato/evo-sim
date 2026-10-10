# R4 B5b: Mansfield's supply argument with a sourced neutral fraction

**Status: run, written up, reviewed (combined, `REVIEW-R4-B5b-combined.md`), fix pass done.** Everything here is dialectic (rule RH): arithmetic on stated inputs.

## Files
- Script: `research/checks/b5b_mansfield_supply.py`, pre-registered at **b707415** (before the run, unedited since; md5 in `raw/b5b.host`).
- Run: na-workhorse, one process, under a second, 2026-10-09. Outputs `results/raw/b5b.{out,json,host}`.
- Claim: B5b (Mansfield, YouTube comment under jDxFtCOGZ3A: "If even just 2 of these 100 are neutral - which is certainly way under the actual proportion - then in a population of size N there are about 2*N new neutral alleles introduced each generation.", and "So, the expectation is that there will be on average 1 neutral fixation every generation if just 2% of new mutations are neutral."). The claim file's open item was "a sourced neutral fraction".

## Inputs (all from the repo)
- Mutations per zygote: 100 (Mansfield) and 76.8 (6.4e9 x 1.2e-8, Kong 2012 mu from `parameters.yaml`; Hancock's first-pass figure).
- Neutral fraction: Mansfield's 0.02, and the sourced complement of Rands et al. 2014 (PLoS Genet 10:e1004525): "8.2% (7.1-9.2%) of the human genome is presently subject to negative selection" (`ledgers/gaps-review.md` C16, verified verbatim). Not under negative selection is 0.918 (0.908-0.929). This is an **upper bound** on the neutral share: unconstrained is not the same as neutral (positively selected and nearly neutral sites sit inside it), and mutability is taken as uniform.
- Requirements: Day 20M over 450,000 generations (2019 count) and 17.5M over 252,000 (3.0). Measured per lineage: GAP-07b 21.05M events, GAP-07c fixed events 17.2-17.9M.

## Results (supply S = n_dn x f / 2 x G per lineage)
| Case | S | vs 20M (450k gen) | vs 17.5M (252k gen) |
|---|---|---|---|
| Mansfield as written (100, f = 0.02) | 0.45M / 0.25M | 0.022 (44.4x short) | 0.014 (69.4x short) |
| 100 per zygote, f = 0.918 (0.908-0.929) | 20.66M (20.43-20.90) / 11.57M (11.44-11.71) | 1.033 (1.022-1.045) | 0.661 (0.654-0.669) |
| Kong 76.8, f = 0.918 | 15.86M / 8.88M | 0.793 | 0.508 |
| Kong 76.8, f = 1.0 | 17.28M / 9.68M | 0.864 | 0.553 |

- **Needed neutral fraction:** 0.889 for 20M at 450k with 100 per zygote; 1.389 for 17.5M at 252k (impossible); with Kong's 76.8 both exceed 1 (1.157, 1.808).
- **Against measured events at 252,000 generations:** the sourced-f supply (8.8-11.7M) is 0.42-0.56 of the 21.05M events and 0.49-0.68 of the fixed events (17.2-17.9M).
- **Identity:** 2 neutral per zygote x N zygotes x 1/(2N) = 1 exactly, for N = 10 to 1e6. Mansfield's arithmetic is right as an identity.

## Predictions versus results
P1 (identity) met. P2 (44.4x, 69.4x, needed f 0.889 and 1.389) met exactly. P3 (20.66M, covers 20M by 3.3%; 11.57M, 0.66x of 17.5M) met. P4 (15.86M / 0.79x; 8.89M / 0.51x) met. P5 (supply 0.42-0.55 of 21.05M; 0.50-0.67 of fixed events) met at the mid f; the full f range gives 0.42-0.56 and 0.49-0.68, a rounding-size spill outside the pre-registered brackets that used the mid value only. P6 met. No prediction failed.

## What this does and does not settle
- **Settles:** B5b's illustration is right as an identity and wrong in magnitude at f = 0.02 (44x to 69x short, as the claim file said). Replacing 0.02 with the sourced upper bound lifts the supply to the 2019-edition requirement (20M over 450,000 generations, covered by about 3%) and **only** with Mansfield's 100 per zygote. With Kong's 76.8 even f = 1 does not reach 20M.
- **Does not settle:** at the 3.0 count (252,000 generations) the pure k = mu supply with the sourced f covers 0.51-0.66 of Day's 17.5M and about half of the measured fixed events. That gap is the clock and ancestral-polymorphism question (B4a, GAP-06), not the neutral fraction. Whether the requirement is adaptive or neutral is not tested here; "unconstrained" is an upper bound on neutral, and the neutral-substitution rate also assumes a full pipe (B1c), which this arithmetic does not examine.
- The 450,000 generation count is the 2019 edition's (`parameters.yaml` day_2019, unverified there); the match at 450k therefore speaks to the older number, which Day has since replaced by 252,000.

## Who this helps
- **Critics (Mansfield):** the "way under the actual proportion" remark is vindicated in direction and size: a sourced neutral share of about 0.9 is 45x his illustrative 0.02, and with it his supply identity covers 20M at the 2019 generation count. Day's §6.4 line that no independent neutral-fraction estimate exists is again contradicted (ledger gaps.md), here with a number.
- **Day:** the cover is thin and depends on the larger of two mutation counts. With Kong's measured-scale 76.8 per zygote (and Hancock's own haploid 38.4) the neutral supply falls short of 20M even at f = 1, and at his current 252,000 generations it covers about half of 17.5M, so the critics' supply route does not by itself dispose of the requirement; the residual is a clock or ancestral term (B4a), which his own k = mu route undershoots by about 2x (GAP-07b). The sourced fraction is an upper bound, not a measurement of neutrality.

## Review resolution
- MINOR-1, MINOR-2: every use of f = 0.918 is an **upper bound** on the neutral share (positively selected and nearly neutral sites are inside it) with uniform mutability assumed (CpG hypermutability, concentrated in constrained regions, is not modelled; sign unknown). MINOR-3: the 450,000-generation match (20M covered by 3%) is the 2019 count and is not to be quoted without the 252,000 row (0.66x). MINOR-4: requirements are read per lineage (20M and 17.5M are one lineage's differences), as in GAP-07b/c. MINOR-5: Mansfield's 2% was an illustration; the vindication of "way under" is by an estimate he did not cite.
- No new run; no verdict change (B5b internal holds, external contested).
