# R4 GAP-07t: human-chimp divergence events re-counted on the T2T ape alignment (hs1 vs mPanTro3)

**Status: hs1-referenced pass run and written up; chimp-referenced pass (A5) pending collection; awaiting review.** Tier: low-stakes re-confirmation of GAP-07b (one combined review, `REVIEW-R4-GAP07t-combined.md`), unless the reviewer judges that the A3 node moves. Not integrated.

## Files
- Script `research/checks/gap07t2t_event_counts.py`, pre-registered at **547bcd5**. Before the commit only the synthetic `selftest` was run, and it passed.
- Run on na-workhorse, one process, `extract` hs1 2026-10-10 19:41-20:30 -06:00 (2,972 s, 5,366,631 blocks), then `extract` chimp, then `report`.
  - The first launch waited on a `pgrep` that matched its own command line. It was killed and relaunched without the wait (logged in `raw/gap07t.host`). Nothing else was changed.
- Raw outputs:
  - `raw/gap07t_hs1.json`: per-chromosome-class totals.
  - `raw/gap07t_report_hs1.out`: hs1 report.
  - `raw/gap07t_report.out`: both passes, when collected.
- Data: the T2T Primate Consortium Cactus alignment (8-t2t-apes-2023v2), hs1-referenced MAF (md5 df51e5c3...), already on workhorse from FM. Untrusted; read as text only.
- Target (A3, Day 2025): "Genetic divergence: ~40 million single-nucleotide variants; ~20 million fixations required on human lineage." RH tag: dialectic.

## Results (hs1 reference, F0 = all columns, primary = autosomes + X + Y)
| quantity | GAP-07b (hg38/panTro6) | **GAP-07t (hs1/mPanTro3)** | change |
|---|---|---|---|
| SNV columns | 37.77 M | **42.87 M** | +13.5% |
| indel events (in-block 4.26 M + inter-block <= 100 kb 1.14 M) | 4.30 M | **5.40 M** | +25.7% |
| events per lineage | 21.05 M | **24.14 M** | +14.7% |
| 205 M / events per lineage | 9.74 | **8.49** | -12.8% |
| SNV share of events | 0.90 | 0.888 | |

- **By filter (primary):**
  - F1 (no N, single-copy blocks): 35.11 M SNV, 39.49 M events, **19.75 M per lineage** (ratio 10.38).
  - F2 (F1 and non-repeat): 14.61 M SNV, 8.41 M per lineage.
  - So almost all of the T2T increase sits in duplicated or N-containing blocks. F0 minus F1 is 8.8 M events, consistent with newly assembled satellites and segmental duplications.
  - Caveat: inter-block events are not filtered by F1/F2 (by design: no row-level flags). That makes F1/F2 slight overcounts, by at most 1.14 M events.
- **By chromosome class (F0):** autosomes 22.52 M per lineage; X 1.00 M; Y 0.62 M. Y has 19.9 M aligned columns with 1.11 M SNVs (5.6%), the ampliconic/heterochromatic Y.
- **Lineage split:**
  - SNVs: human-derived 20.72 M, chimp-derived 19.11 M (human share 0.520 F0, 0.494 F1); third 0.56 M; unpolarised 2.49 M.
  - Indels: human share 0.462 (F0), 0.436 (F1).
- **Indel sizes (F0, in-block):** 1 bp 39.7%; 2-10 bp 49.1%; 11-50 bp 7.9%; 51-1,000 bp 3.0%; > 1,000 bp 0.2%. In-block indel bp total: 77.8 M.
- Reference bp in blocks with no chimp row: 80.3 M. Discontinuities > 100 kb or non-collinear: 310,288.
- **Polymorphism-corrected per lineage** (no chimp population data; refresh 10b s6: chimp VCFs not located):

| basis | per lineage | 205 M / that |
|---|---|---|
| GAP-07c human shares, chimp assumed equal | 20.52 M | 9.99 |
| GAP-07c pooled, human data only | 22.23 M | 9.22 |
| CSAC fixed 0.86 | 20.76 M | 9.88 |
| CSAC fixed 0.78 | 18.83 M | 10.89 |

## Scoring of the pre-registered predictions (hs1 pass)
| ID | Prediction | Result | Score |
|---|---|---|---|
| D1 (Day) | SNV >= 40 M and events per lineage >= 22 M | 42.87 M; 24.14 M | **Holds** |
| D2 (Day) | 205 M / events <= 9 | 8.49 | **Holds** |
| C1 (critics) | events per lineage 17.9-24.2 M; ratio 8.5-11.5 | 24.14 M (inside, at +14.7%); 8.49 (0.01 below the band) | **Events hold; ratio misses marginally** |
| C2 (critics) | SNV share >= 85%; median indel 1-2 bp | 0.888; median in the 2-10 bp class (1 bp share 39.7%) | **SNV share holds; median indeterminate at class resolution** |
| A1 | SNV F0 38-46 M; F1 33-42 M; F2 15-25 M | 42.87 / 35.11 / 14.61 M | **F0, F1 hold; F2 misses (just below)** |
| A2 | indel events 3.5-6.0 M; median 1-2 bp; >= 40% 1 bp | 5.40 M; indeterminate; 39.7% | **Count holds; 1-bp share misses marginally** |
| A3 | per lineage 21-26 M; ratio 7.9-9.8 | 24.14 M; 8.49 | **Holds** |
| A4 | SNV human share (F1) 0.46-0.54; indel 0.40-0.60 | 0.494; 0.436 | **Holds** |
| A5 | chimp-referenced pass within 10% | pending | pending |
| A6 | polymorphism-corrected 17.5-22.5 M | 18.83-22.23 M | **Holds** |

The pre-registered verdict clause said D1 + D2 together "would mean the T2T assemblies move the event count materially (> 25%, rule R1) toward Day's 205 M". D1 and D2 hold, but the move is +14.7%, below R1's 25%. **So the event count is not materially moved under R1.** The D1/D2 thresholds were set too close to GAP-07b to separate "some increase" from "a material increase". That is a design weakness in this audit's own predictions; it is not counted for or against either side.

## Interpretation
- **On the T2T assemblies, human-chimp divergence is 24.1 M events per lineage** (19.7 M in single-copy, N-free blocks; 18.8-22.2 M after polymorphism correction). GAP-07b's hg38/panTro6 count was 21.05 M. Day's "~20 million fixations required on human lineage" (A3) stays within R1 on every reading (-6% to +21%). A3 internal and its magnitude are re-confirmed on the newer assemblies.
- **The T2T assemblies add about 15% more events, mostly in duplicated and satellite sequence** (F0 vs F1). The bp-versus-events point of A3x stands: 205 M bp per lineage is 8.5x the event count (10.4x in single-copy blocks).
- **Lineage symmetry:** the human share is 0.49-0.52 for SNVs and 0.44-0.46 for indels. Neither lineage carries a disproportionate share, which matches GAP-07b and FM's non-human-specific result.

## Who this helps
- **Day side:**
  - The newer assemblies raise the event count (+14.7%), so his ~20 M per lineage is, if anything, low.
  - With the T2T count the MITTENS shortfall rises: 24.14 M / 190.6 is about 126,700 against 104,900 for 20 M.
  - His A3 figure is re-confirmed as a magnitude.
- **Critic side:**
  - The count stays an events count of about 20-24 M per lineage.
  - The 205 M bp figure remains 8.5-10.4x the event count.
  - The extra T2T divergence sits mostly in duplicated and satellite regions, where alignment is least reliable.
  - The lineages are symmetric, with no human-specific excess.
- **Both:** Nothing moves past R1. The open part is chimp-side polymorphism: no chimp population VCF was found, so the correction assumes the human share.

## Caveats for the reviewer
- The hs1 projection drops chimp-only sequence that is not aligned to hs1 (80.3 M hs1 bp have no chimp row; the converse needs the chimp pass, A5).
- Inter-block events are a proxy for chain gaps inside nets: collinear, same chimp sequence and strand, <= 100 kb. Capping at 1 kb or 10 kb changes them by < 5% (1.095 / 1.122 / 1.144 M).
- First-row choice in duplicated blocks (F0) counts paralogous alignments.
- Gorilla-only polarisation, as in GAP-07b. The strict orangutan-agreeing variant gives 16.48 / 15.40 M (F0).
