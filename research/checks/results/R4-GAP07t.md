# R4 GAP-07t: human-chimp divergence events re-counted on the T2T ape alignment (hs1 vs mPanTro3)

**Status: reviewed, fix pass done, integrated.** Tier: low-stakes re-confirmation of GAP-07b (one combined review, `REVIEW-R4-GAP07t-combined.md`), unless the reviewer judges that the A3 node moves. Integrated.

## Files
- Script `research/checks/gap07t2t_event_counts.py`, pre-registered at **547bcd5**. Before the commit only the synthetic `selftest` was run, and it passed.
- Run on na-workhorse, one process, `extract` hs1 2026-10-10 19:41-20:30 -06:00 (2,972 s, 5,366,631 blocks), then `extract` chimp, then `report`.
  - The first launch waited on a `pgrep` that matched its own command line. It was killed and relaunched without the wait (logged in `raw/gap07t.host`). Nothing else was changed.
- Raw outputs (chimp pass: `raw/gap07t_chimp.json`):
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
| A5 | chimp-referenced pass within 10% | 24.03 M vs 24.14 M (ratio 0.996); F1 19.77 vs 19.75 M | **Holds** |
| A6 | polymorphism-corrected 17.5-22.5 M | 18.83-22.23 M | **Holds** |

The pre-registered verdict clause said D1 + D2 together "would mean the T2T assemblies move the event count materially (> 25%, rule R1) toward Day's 205 M". D1 and D2 hold, but the move is +14.7%, below R1's 25%. **So the event count is not materially moved under R1.** The D1/D2 thresholds were set too close to GAP-07b to separate "some increase" from "a material increase". That is a design weakness in this audit's own predictions; it is not counted for or against either side.

## Chimp-referenced pass (A5)
`raw/gap07t_report.out`, second block. F0 primary:
- 42.69 M SNV, 4.20 M in-block indels and 1.17 M inter-block indels: **24.03 M events per lineage** (ratio 8.53).
- F1: 19.77 M per lineage. F2: 8.42 M per lineage.
- Chimp bp in blocks with no human row: 242.3 M (against 80.3 M for hs1), the chimp-only sequence that the hs1 projection cannot see. It adds bp but not aligned events.
- **Post hoc disclosure (labelling bug; the counts are unaffected):** in the chimp-referenced pass the script's SNV lineage fields are swapped. `snv_h` tests gorilla == other row, and in that pass the other row is human, so `snv_h` counts chimp-derived SNVs. The indel lineage code handles the swap correctly; the SNV code does not. Read correctly:
  - F0: human-derived 18.64 M, chimp-derived 21.03 M (human share 0.470).
  - F1: 16.48 / 16.93 M (human share 0.493).
  - Both passes give the reference lineage the larger F0 share (hs1 pass: human 0.520; chimp pass: chimp 0.530). This is the reference-projection bias FM's mirror found. The F1 shares agree (0.494 and 0.493).

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

## Review resolution (post hoc, 2026-10-10; answers `REVIEW-R4-GAP07t-combined.md`; no rerun, script and raw outputs untouched)
- **MINOR-1 (swap not fully propagated): extended.**
  - (a) The strict (orangutan-agreeing) SNV figures in the chimp pass are swapped too. Raw report line 41 prints "strict 16.86 / 15.04 M" for F0 and line 42 "14.19 / 13.77 M" for F1, in "h/c" order. Read correctly (human-derived / chimp-derived): **F0 strict 15.04 / 16.86 M; F1 strict 13.77 / 14.19 M; F2 6.29 / 6.40 M.** The hs1-pass strict figures (16.48 / 15.40 M F0) are correct as printed.
  - (b) **`raw/gap07t_report.out` lines 40-43 (second block, the chimp-referenced pass) print the SNV lineage fields swapped: READ AS SWAPPED.** That covers "SNV human / chimp", the "human share" (0.530, 0.507, 0.504 are chimp shares; human shares are 0.470, 0.493, 0.496) and the strict h/c order. Indel fields in that block are correct. Event totals, F-filter totals and the hs1 block (lines 19-21) are unaffected. The raw file is deliberately not edited; the report code is not changed.
- **MINOR-2 (F1 vs unfiltered): reworded.** The statement "almost all of the T2T increase sits in duplicated or N-containing blocks" compared the T2T F0/F1 split with GAP-07b's single unfiltered count. It is **not shown**. What is shown: on T2T, F0 24.14 M vs F1 19.75 M per lineage, so duplicated or N-containing blocks hold 8.8 M of 48.3 M primary events within T2T itself. That the hg38-to-T2T rise (+3.1 M per lineage) is concentrated there is *consistent with* the addition of satellites and segmental duplications, and F1 (19.75 M) being 6% below GAP-07b's unfiltered 21.05 M is not a like-for-like comparison (GAP-07b has no F1 equivalent). A like-for-like test would need a GAP-07b F1-style rerun; not done.
- **MINOR-3 (host record): added.** Appended to `raw/gap07t.host` (post hoc): chimp MAF `sources/raw/fm-mirror-2026-10-10/pantro.maf.gz` md5 bc332f336d3e6466e810b53be5b546a8 (md5sum run on na-workhorse 2026-10-10, matches the docstring prefix), host na-workhorse; chimp-pass extract 20:30:36 to 21:20:44 -06:00 (3,007 s, 5,987,942 blocks) from `gap07t.out` timestamps.
- **MINOR-4 (Day-side steelman): added.** The pre-registered critic band (17.9-24.2 M) was set at 21.05 M +/-15%, and the result is at its edge. Two successive assembly upgrades (hg38 to T2T) both pushed counts up. Unaligned sequence (80.3 M hs1 bp with no chimp row; 242.3 M chimp bp with no human row) is excluded from events, so 24.14 M is closer to a floor than a ceiling for what whole-genome comparison implies. The critic reading of "events not bp" holds while the quantitative centre has moved toward Day.
- **MINOR-5 (critic-side steelman): added.** The ratio of 205 M bp to events per lineage ranges from **8.49 (F0 raw, least critic-favourable) through 9.2-10.9 (polymorphism-corrected) to 10.4 (F1 single-copy)**. The Interpretation's "8.5x (10.4x in single-copy blocks)" should be read with that 9.2-10.9 band beside it.
- **NITs:** NIT-2 the 22.23 M pooled row (GAP-07c, human data only) is higher than the share-based 20.52 M because pooled uses a different weighting; see GAP-07c write-up for the construction. NIT-3 the A3 quote is in `quotes-day.md` under Q12 (Z18165980 para 34); the "Z18168236 s2.1" locator in the docstring is unconfirmed and Q12 is the citation to use. NIT-5/6 (paralog overcount, chimp polymorphism likely higher so ratio higher) accepted; both lean toward the critic side and are bounded by the 14.7% move.
- **Verdict:** unchanged. R1 not triggered (+14.7%); A3 magnitude re-confirmed. Status: reviewed, fix pass done, integrated.
