# Review of R4 B5b (combined, low-stakes tier)

Date 2026-10-09. Method: read `R4-B5b.md` and `raw/b5b.out`; arithmetic re-derived by hand, nothing rerun. Labels: MAJOR (changes a conclusion), MINOR (fix or caveat), NOTE.
No ROOT-path node moves (B5b is not load-bearing; B5, B1, B3a verdicts unchanged), so the combined tier applies.

## 1. Correctness
Re-derived: 100 x 0.918 / 2 x 450,000 = 20.66M; 100 x 0.918 / 2 x 252,000 = 11.57M; needed f = 20M / (50 x 450,000) = 0.889 and 17.5M / (50 x 252,000) = 1.389; 76.8 x 0.918 / 2 x 450,000 = 15.86M; 6.4e9 x 1.2e-8 = 76.8. All agree.
- **MINOR-1.** "Not under negative selection = 0.918" is an upper bound on the *neutral* share; it also contains positively selected and nearly-neutral sites, and the 8.2% is a model-based estimate (Rands 2014) whose CI is for that model only. The write-up says this once; the table heading should carry "upper bound" too.
- **MINOR-2.** Uniform mutability is assumed (CpG sites are about 10x hypermutable and sit disproportionately in constrained regions). Direction is unsigned for the neutral rate; say so.
- **MINOR-3.** The match at 450,000 generations is to the 2019 count (`day_2019`, unverified in `parameters.yaml`), which Day has replaced. The headline "covers 20M by 3%" must be stated next to the 252,000 row (0.66x), as the table does; do not quote it alone.
- **NOTE-1.** P5's full-f spill outside the brackets (0.42-0.56 vs 0.42-0.55) is disclosed and is rounding.

## 2. Day-side steelman
- The write-up credits the thin cover and the Kong 76.8 shortfall. Fair.
- **MINOR-4.** Day can say the requirement is 20M *adaptive-plus-neutral differences between two lineages*, each lineage carrying half; the table is per lineage, so the comparison basis is right, but the write-up should state that the 20M is read per lineage (as GAP-07b/c do), otherwise a reader may halve or double it.
- **NOTE-2.** Mansfield's identity does not address whether the neutral rate equals the observed *fixed* rate (GAP-07c: fixed events 17.2-17.9M vs sourced supply 8.8-11.7M, i.e. 0.49-0.68). That is a point for Day and is in the write-up.

## 3. Critic-side steelman
- **MINOR-5.** "Way under the actual proportion" is vindicated in size, but the write-up should add that Mansfield's illustration used 2%, not a sourced share, and the vindication is by an independent estimate he did not cite.
- **NOTE-3.** The critics' fuller reply to the 252,000 shortfall is polymorphism/ancestral terms (GAP-07c: 10-12x between 205M and fixed events), which the write-up cites. Fair.

## Verdict on B5b
Sound; 0 MAJOR, 5 MINOR (wording only). No claim verdict changes: B5b internal holds, external stays contested.
