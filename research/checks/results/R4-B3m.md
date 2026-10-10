# R4-B3m: Day's "median factor of 25 across 55 vertebrates" recomputed from Bergeron 2023

Status: **combined review done** (`REVIEW-R4-B3m-combined.md`, b30137d); fix pass below (Review resolution). Low-stakes tier: fidelity re-computation of a cited number. Script `research/checks/b3m_bergeron_median.py`; pre-registered 5ca5f2e; post hoc diagnostics 382b580. Raw: `raw/b3m_main.out`, `raw/b3m_posthoc.out`. Run locally (< 2 s).

Target: B3d sub-statement (Q69, blog 2026-05-07 ¶5): "pedigree μ and phylogenetic k disagree by a median factor of 25 across 55 vertebrates"; source named in ¶3 (Q161): Bergeron et al. 2023.

Inputs (untrusted, read only, not executed): Bergeron 2023 Supplementary Tables (`41586_2023_5752_MOESM5_ESM.xlsx`, Nature static content, open access; sha256 `5bb7ed86…75b56`), Table 9; the authors' GitHub repo `lucieabergeron/vertebrate_rate` (tarball sha256 `fb30af08…08d35`): `time_tree.r` (ape::chronos, lambda = 0, relaxed, 14 calibrations in Ma; the Table 9 rates are `attr(chr, "rate")` for terminal edges) and `tree_rooted.nwk` (IQ-TREE UCE tree, substitutions/site). Saved under `sources/raw/b3m-bergeron-*-2026-10-10/` (gitignored).

Disclosure: before pre-registration the first data row of Table 9 (red panda) was seen while listing headers; the predictions say so.

## Results

| basis (all species with both values) | n | median k/μ | IQR |
|---|---|---|---|
| B1 UCE column (per Myr → per yr) / μ_yearly_modelled | **55** | **25.4** | 13.3-62.6 |
| B2 UCE / μ_yearly (observed) | 68 | 28.3 | 12.6-83.9 |
| B3 WGA (MultiZ) / μ_yearly_modelled | 55 | 23.8 | 13.5-51.4 |
| B4 per generation (k × gen time / μ_gen_modelled) | 55 | 25.4 | (= B1) |
| B5 mismatched (per-yr k / per-gen μ) | 55 | 5.8-6.0 | |
| Non-domesticated subset, B1 | 46 | 25.7 | 13.2-62.9 |
| U: crude lineage-average rate (IQ-TREE root-to-tip / 416 Myr) | | 0.00213 /Myr vs column median 0.043 (20x) | |
| PH1 (post hoc): implied depth = root-to-tip / column | 67 | 21.4 Myr (416 expected for a lineage-average rate) | 8.1-55.5 |
| PH2 (post hoc) B6: lineage-average k / μ_yearly_modelled | 55 | **1.85** | 1.06-2.98 |
| A5: rescaling of the column that makes the B1 median equal 1 | 55 | 1 / 25.4 = **0.039** (column ÷ 25.4) | |

The crude 1.9 (row U, ratio of the root-to-tip rate to the median μ) is in the pre-registered main run; PH2 only refines it to a per-species median (1.85). The A5 factor is the reciprocal of the B1 median; the main run printed "see table" for it. It is the same order as PH1's depth ratio (416 / 21.4 = 19.4): the column would have to be about 20-25x smaller to sit on μ, which is roughly what averaging over the whole lineage does.

Exactly 55 of the 68 species have modelled rates, so Day's "55" is the comparison set, not the Methods phrase "(55 species)" (75% completion threshold).

## Against the predictions

| id | prediction | result | score |
|---|---|---|---|
| D1 (Day) | a matched-basis median in [20, 30] over 55 species | B1 25.4, n = 55 (B3 23.8, B4 25.4) | **hit** |
| C1 (critic, steelman #6) | any ~25 gap from constrained sites or yr/gen mismatch, direction k < μ | direction is k > μ; the yr/gen mismatch gives ~6, not 25 | **miss** |
| A1 | B1 > 1, in [10, 40] | 25.4 | hit |
| A2 | B3 > 1, in [5, 40] | 23.8 | hit |
| A3 | column ≥ 10x the crude per-Myr rate (unit or chronos-estimator artefact) | 20x | hit |
| A4 | 55 ≠ the comparison count; matches the Methods phrase | 55 = species with modelled rates | **miss** (Day-favourable) |

## Reading
- **Fidelity: proposed `accurate`.** The median 25 and the 55 species are both in Bergeron's published table on a matched per-year (equivalently per-generation) basis. Day reports the number correctly. Rule C: his reading is the plain one.
- **External: proposed `contested`.** The 25 is a property of the tabulated rate, and the tabulated rate is not a lineage-average rate. The table's substitution rates are chronos terminal-edge rates with lambda = 0 (no penalty on rate variation between edges); they are the rates Bergeron publish, so Day's reading is the plain one. Applied over the whole lineage they would account for only about 21 Myr of the 416 Myr root depth (PH1). A lineage-average rate from the same tree gives k/μ about 1.9 (PH2). Because root-to-tip distances saturate, that figure is a **lower bound** on a lineage-average k, not an estimate: a lineage-average k is at least about 2x μ. **The gap between about 2 and 25 is unexplained here, not shown to be an artefact.** Candidate causes, none tested: short terminal durations under lambda = 0; recent rate increases; and, on the critics' side, segregating polymorphism and not-yet-fixed variants that inflate k on short terminal branches (μ is a per-generation germline rate; terminal k is not purely fixed differences). Bergeron draw equality lines and report a positive association (Fig. 2); they do not report a 25-fold gap. Not resolved: whether Fig. 2's axes rescale the column.
- Direction: k > μ per year. That does not fit the purifying-selection explanation (k < μ) that steelman-critic #6 offered. A residual of about 2x on the lineage-average basis fits ancestral per-year rates being higher (smaller, shorter-generation ancestors) as easily as it fits Day's reading.

## Who this helps
- **Day:** his number and species count are reproduced exactly from the source he cites; the R4-B3 "no source" premise (P6) was already withdrawn, and this check confirms the figure itself.
- **Critics:** the 25 comes from per-edge chronos rates fitted without smoothing. A lineage-average k from the same tree is within a factor of about 2 of μ. So "falsified directly" depends on which rate is called k; on the lineage-average basis the gap is at least about 2x (lower bound), and what lies between 2 and 25 is unexplained. The critics' steelman had the direction wrong (k > μ, not k < μ).

## Review resolution (combined review, b30137d)
| finding | resolution |
|---|---|
| MAJOR-1 A5 never reported | Reported: 1 / 25.4 = 0.039 (the column divided by 25.4 puts the B1 median on μ); added to the results table and tied to PH1 (factor 19.4). No rerun: the factor is the reciprocal of the printed B1 median. |
| MAJOR-2 PH2 used as an estimate; "leaning against falsified" | Reworded: PH2 is a lower bound (root-to-tip saturates); "a lineage-average k is at least about 2x μ; the gap between 2 and 25 is unexplained, not shown to be an artefact". "Leaning against falsified" removed from the Reading and from Who this helps. |
| MINOR-1 main-run 1.9 vs post hoc 1.85 | Clause added under the table. |
| MINOR-2 unmatched species | The run printed 67 of 68 matched but not which species failed; the name is not recorded. Left open (one-line diagnostic, not run in this pass). PH2 uses n = 55 through the same match. |
| MINOR-3 reptile n = 2 | The group split is not quoted in the write-up; it stays in the raw output only. |
| MINOR-4 soft predictions after seeing the red-panda row | Agreed: A1 and A4's non-trivial content is the direction (k > μ) and the count (55), not the magnitude, since the red-panda row (k/μ about 22) was seen before pre-registration. |
| MINOR-5 "audit swapped the estimator" | Reading now leads with "the 25 is a property of the tabulated rate, and the tabulated rate is not the lineage-average rate"; Day's reading is the plain one. |
| MINOR-6 polymorphism on short terminal branches | Added as a candidate cause (critic side). |
| MINOR-7 critics' broader claim rests on a lower bound | Stated: PH2 supports "no robust 25-fold gap" only as a lower bound; the critic steelman C1 direction was wrong (miss). |

Proposed after the fix pass: fidelity **`accurate`** (number and count reproduced from the cited table); external **`contested`** (the 25 holds for the published terminal-edge rates; a lineage-average k is at least about 2x μ; the 2-vs-25 gap is unexplained).

## Open
Read Bergeron's Fig. 2 axis scaling and the Extended Data Fig. 6 UCE-vs-WGA comparison. Re-run chronos with lambda > 0 (needs R and `ape`, on workhorse) to test PH1 directly (pre-register).
