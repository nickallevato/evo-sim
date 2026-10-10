# R4-B3m: Day's "median factor of 25 across 55 vertebrates" recomputed from Bergeron 2023

Status: **awaiting combined review** (low-stakes tier: fidelity re-computation of a cited number). Script `research/checks/b3m_bergeron_median.py`; pre-registered 5ca5f2e; post hoc diagnostics 382b580. Raw: `raw/b3m_main.out`, `raw/b3m_posthoc.out`. Run locally (< 2 s).

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
- **External: proposed `contested`, leaning against "falsified".** The table's substitution rates are chronos terminal-edge rates with lambda = 0, i.e. with no penalty on rate variation between edges. Applied over the whole lineage they would account for only about 21 Myr of the 416 Myr root depth (PH1). The lineage-average rate from the same tree gives k/μ about 1.9 (PH2; crude, because root-to-tip saturates, the root is placed by the authors, and one root age is used). So the factor 25 depends on which estimator of k is used, not on a measured 25-fold gap. Bergeron draw equality lines and report a positive association (Fig. 2); they do not report a 25-fold gap. Not resolved here: whether Fig. 2's axes rescale the column, and why the terminal rates sit above the lineage average (short terminal durations under lambda = 0, recent rate increases, or both).
- Direction: k > μ per year. That does not fit the purifying-selection explanation (k < μ) that steelman-critic #6 offered. A residual of about 2x on the lineage-average basis fits ancestral per-year rates being higher (smaller, shorter-generation ancestors) as easily as it fits Day's reading.

## Who this helps
- **Day:** his number and species count are reproduced exactly from the source he cites; the R4-B3 "no source" premise (P6) was already withdrawn, and this check confirms the figure itself.
- **Critics:** the 25 comes from per-edge chronos rates fitted without smoothing. A lineage-average k from the same tree is within a factor of about 2 of μ. So "falsified directly" rests on a choice of estimator, not on a robust 25-fold gap. The critics' steelman had the direction wrong (k > μ, not k < μ).

## Open
Read Bergeron's Fig. 2 axis scaling and the Extended Data Fig. 6 UCE-vs-WGA comparison. Re-run chronos with lambda > 0 (needs R and `ape`, on workhorse) to test PH1 directly (pre-register).
