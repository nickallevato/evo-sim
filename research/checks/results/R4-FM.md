# R4-FM: Day's "mesas" (The Fourth Mechanism) replicated on the T2T ape alignment against a heterogeneous-μ null

Status: **run complete, awaiting three reviews** (load-bearing tier: correctness, steelman-day, steelman-critic). Script `research/checks/fm_mesa_replication.py`; pre-registered d723064 (docstring P1-P9, grid, mesa rule and verdict mapping fixed before any data analysis). Run on na-workhorse 2026-10-10: extract 4,144 s (5,366,631 MAF blocks, 24 chromosomes), then analyse. Raw: `raw/fm_main.out`, `raw/fm_analyse.json`, `raw/fm_main.host`, `raw/fm_maf.md5`. The per-1-kb bin file `fm_bins.npz` (74 MB) stays on workhorse, not committed. No post hoc changes.

Data: the T2T Primate Consortium 8-way Progressive Cactus alignment exported as an hs1 (T2T-CHM13)-referenced MAF (`8-t2t-apes-2023v2.hs1.maf.gz`, cgl.gi.ucsc.edu; md5 df51e5c3…53b, matches the published .md5). These are the data Day names (Q171). Lineages are counted by parsimony on CHM13 coordinates, with gorilla and Sumatran orangutan as outgroups and hs1 = hg38 required: H (human since the human-chimp ancestor), C (chimp), B (bonobo), G (gorilla terminal), and DHC (unpolarised human-chimp differences). Filters: F0 = all; F1 = no paralogous rows; F2 = F1 without soft-masked repeats; F3 = F2 without CpG. Autosomes unless stated.

## Headline numbers (autosomes)

| W | filter | φ H | φ C | φ G | φ DHC | φ_res H / C (het-μ null) | φ_HC (H vs C split) |
|---|---|---|---|---|---|---|---|
| 1 kb | F0 | 3.25 | 2.59 | 2.07 | 9.5 | 2.67 / 2.09 | 1.31 |
| 10 kb | F0 | 10.4 | 7.3 | 5.9 | 44.7 | 6.15 / 3.97 | 2.72 |
| 100 kb | F0 | 36.9 | 25.7 | 18.4 | 210 | 16.2 / 8.2 | 8.54 |
| 1 Mb | F0 | **136** | **125** | **93** | **826** | 34.3 / 18.8 | 24.1 |
| 100 kb | F1 | 18.4 | 19.2 | | 49.3 | 4.48 / 4.08 | 2.71 |
| 10 kb | F2 | 3.46 | 3.33 | 2.80 | 7.0 | 1.67 / 1.55 | 1.33 |
| 100 kb | F2 | 14.3 | 14.7 | 12.5 | 38.0 | **2.68 / 2.41** | **1.81** |
| 1 Mb | F2 | 89.4 | 89.5 | 85.1 | 253 | 5.21 / 5.70 | 3.49 |
| 100 kb | F3 | 10.9 | 11.6 | | 27.0 | 2.33 / 2.14 | 1.65 |

φ is the dispersion index against a uniform-rate binomial; φ = 1 means no overdispersion. Mean densities: H 0.0049-0.0051, C 0.0052-0.0058, G 0.0070-0.0077 per core column. The human branch is the shortest of the three.

Mesas (rule: ≥ 3 consecutive windows at ≥ 1.5x the lineage mean with Poisson p < 1e-3):

| cell | H mesas | C mesas | B | G | H-mesa windows inside C mesas (C genome share) | H-specific / C-specific | het-μ null H mesas (5 reps) | uniform null | H mesas with excess > 191 / > 840 | C mesas > 191 / > 840 | H mesas' share of DHC |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F0 10 kb | 794 | 601 | 613 | 316 | 32% (1.0%) | 35 / 70 | 393-423 | 0 | 227 / 30 | 198 / 14 | 2.5% |
| F0 100 kb | 33 | 31 | 33 | 19 | 49% (0.6%) | 1 / 8 | 20-23 | 0 | 33 / 32 | 31 / 29 | 1.25% |
| F2 10 kb | 193 | 167 | 180 | 129 | 42% (0.56%) | 2 / 2 | 91-115 | 0 | 26 / 1 | 22 / 1 | 1.3% |
| F2 100 kb | 18 | 17 | 18 | 11 | 53% (0.78%) | 0 / 0 | 11-14 | 0 | 18 / 10 | 17 / 5 | 1.75% |

Covariates (100 kb, F2, Spearman with H density): C 0.84, G 0.66, H-G/C-G discordance density 0.76, CpG-column fraction 0.19, GC 0.12, hs1≠hg38 0.14. chrX (F2, 100 kb): φ H 19.8, C 19.1; φ_res 2.74 / 2.10; φ_HC 1.43.

## Against the predictions

| id | Day side | critic side | audit numeric | result | score |
|---|---|---|---|---|---|
| P1 FM3 "> 80x" | φ_H ≥ 80 at some W | yes, for every lineage | φ ranges by W; φ_H/φ_C in [0.5, 2] | F0 1 Mb: H 136, C 125, B 123, G 93, DHC 826; φ_H/φ_C 1.09-1.43 | **Day hit, critic hit**; audit hit except 1 Mb H (136, below the 200-4000 range) |
| P2 FM4 clustering | lag-1 > 0.2 | same | H and C within 0.1 | 10 kb F0: 0.45 / 0.44 / 0.45 / 0.47 | hit (both sides) |
| P3 het-μ null | φ_res H/C > 3 | φ_res(H) ≤ 0.3 φ(H); ratio in [0.5, 2] | φ_res 1.5-15; ratio 0.6-1.6 | F2 100 kb: 2.68 vs 4.29 bound; ratio 1.11 | **critic hit, Day miss**; audit hit |
| P4 human specificity | φ_HC > 10; H/C-specific > 3 | φ_HC 1-5; ratio [0.5, 2] | 0.6-1.7 | φ_HC 1.81; specific mesas 0 / 0 (F2 100 kb; ratio undefined), 2 / 2 (F2 10 kb), 1 / 8 and 35 / 70 (F0) | **critic hit on φ_HC; Day miss**; the ratio is indeterminate at the registered cell (0/0) and ≤ 1 in every other cell |
| P5 null reproduction | M/obs < 0.2 | ≥ 0.5 | 0.4-1.2 | 12.4 / 18 = 0.69; uniform null 0 | **critic hit, Day miss**; audit hit; both sides right that the uniform null gives none |
| P6 FM5 Haldane / MITTENS | some H mesa > 840 | yes, and C too, ratio [0.5, 2] | ≥ 10 H; ratio 0.5-2 | F0 100 kb: H 32, C 29 (ratio 0.91) | **hit for both**: Day's sentence is literally true; it is equally true of the chimp lineage |
| P7 FM8b "dominant source" | > 50% of DHC in H mesas | < 20% | 2-15% | 1.25% (F0 100 kb), 1.3-2.5% elsewhere | **critic hit, Day miss**; audit miss (lower than predicted) |
| P8 covariates | H mesas do not track other lineages | (H, C) > 0.6, (H, G) > 0.5 | ranges | 0.84 / 0.66; GC and CpG positive | critic hit; audit hit |
| P9 masking | | φ(F0)/φ(F2) > 2 (DHC, 100 kb) | | 210 / 38 = 5.5 | hit |

## Reading (proposed verdicts for the reviews)
- **FM3 (overdispersion "more than 80 times"): reproduced as a description.** It is reproduced only against a uniform-rate null, at about 1 Mb windows (or ~100 kb for unpolarised human-chimp differences), and for every lineage alike. Against a null in which the rate varies along the genome and is shared by the lineages, the human residual is 2.7, against 2.4 for chimp (F2, 100 kb). Internal: `holds` on the uniform-rate basis. External: the 80x compares with a null nobody uses (critic steelman point 1 confirmed).
- **FM4 (clustering, "mesas"): supported as a description; shared, not human-specific.** About half of the human-mesa windows lie inside chimp mesas, against a 0.6-0.8% background (about 60-90x enrichment). The heterogeneous-μ null reproduces about 70% of the human mesas. H density correlates with C at 0.84 and with G at 0.66.
- **FM5 (one mesa exceeds MITTENS and Haldane): literally true and non-discriminating.** At 100 kb (F0) 32 human mesas carry an excess > 840 substitutions, and so do 29 chimp, 31 bonobo and 19 gorilla mesas. Haldane's and MITTENS' caps bound *selected* substitutions; a neutral excess that every lineage shows does not test selection. Proposed: internal non-sequitur (rule N) for the inference to "selection cannot", external `contradicted` for any human-specific reading.
- **FM8b ("dominant source of genomic divergence"): contradicted.** Human mesas hold 1.25-2.5% of human-chimp differences.
- **FM10 ("neither selection nor drift viable"): not supported by these data.** Every pre-registered discriminating cell (P3, P4, P5, P7) falls on the critics' side. Proposed external: `contradicted` for the mesa route to FM10. The verdict mapping is the one pre-registered.
- **Day-side point to record:** in the unmasked data (F0) the human residual is about twice the chimp residual (16.2 vs 8.2 at 100 kb; 34 vs 19 at 1 Mb), and φ_HC reaches 8.5-24. This excess vanishes once paralogous rows are removed (F1: 4.48 vs 4.08). An unmasked analysis of the kind Day describes would therefore see a real human-heavy signal, located in duplicated and repeat sequence. That is where reference-assembly differences (CHM13 is T2T-complete, as are the apes, but SD collapse and paralog placement differ by species) and real structural evolution both concentrate. This check does not separate the two; it shows the signal is not in single-copy sequence. Even in F0, chimp-specific mesas outnumber human-specific ones (8 vs 1 at 100 kb; 70 vs 35 at 10 kb).

## Who this helps
- **Day:** the data he named do show strong overdispersion: above 80x at 1 Mb against a uniform rate, for every lineage. They show contiguous high-density blocks, and mesas whose excess exceeds both 191 and 840 substitutions. His three descriptive statements (FM3, FM4, FM5 as literally worded) replicate. In unmasked sequence the human lineage is the most overdispersed. His invitation to replicate (FM10) was workable with public data: one 3.4 GB file and about 70 minutes on 1 core.
- **Critics:** every discriminating test lands on their side. The pattern is shared across human, chimp, bonobo and gorilla. It is reproduced by a shared variable-rate null. It is not human-specific in single-copy sequence, and it accounts for about 1-2% of human-chimp divergence, not most of it. The Haldane/MITTENS comparison applies a selection cap to neutral variation.

## Caveats (pre-registered or noted now)
- Parsimony with two outgroups; no ancestral reconstruction from the HAL. CHM13 is one haplotype; hg38 agreement removes only part of human polymorphism.
- No recombination or replication-timing map. The covariates are GC, CpG, discordance and hs1≠hg38.
- The mesa rule and the windows are this audit's. Day's are unreleased, so a different rule could give different counts. It would not change the per-lineage symmetry, which holds in every cell of the grid.
- The heterogeneous-μ null borrows the rate from the other lineages, so it assumes the variation is shared. That is the hypothesis under test, and it is the right null for "human-specific". It is not an independent mechanistic model of μ.
- The F0 human-heavy residual needs a follow-up (pre-register): split F0 by SD annotation, by CHM13-only (non-GRCh38) sequence, and by ape-assembly flagged regions.
