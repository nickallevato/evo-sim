# R4 GAP-07b: direct count of human-chimp divergence events from a real whole-genome alignment

Date: 2026-10-09. THROWAWAY research check, not product code. Replaces the rate-based estimate of GAP-07 (`R4-GAPS-04-07-02.md`) with a count taken from the UCSC hg38 vs panTro6 alignment. No review has been done yet.

## 0. Bottom line

**Events (primary chromosomes chr1-22, X, Y; both lineages plus ancestral polymorphism):**

| quantity | count | note |
|---|---|---|
| SNV differences | **37.77 M** | 33.77 M if alignment records with >2% divergence are dropped |
| Indel events (chain gaps inside the net) | **4.30 M** | 2.17 M human-only + 2.09 M chimp-only + 35 k both-sided |
| Nested (non-colinear) fills + unaligned segments | 32 k + 7 k | about 0.1% of events |
| **Total events** | **42.1 M** | 38.1 M with the <2%-divergence SNV set |
| **Per lineage** (total / 2) | **21.1 M** (19.1 M) | polarized SNV split is 49% human / 51% chimp |

**Base pairs next to events (post hoc, §6).** The bp figure depends on what you count. Events stay at 42 M throughout:

| bp measure | bp | bp / event | 410 M / bp |
|---|---|---|---|
| SNV + sequence outside every aligned block (human + chimp placed) | 261 M | 6.2 | 1.6 |
| SNV + that + non-colinear nested aligned bases (Yoo-style "non-1:1") | 523 M | 12.4 | 0.78 |
| main-run F0 ladder L3 (raw chain-gap bp, many aligned elsewhere or N) | 714 M | 17.0 | 0.57 |

**Day's 205 M per lineage is 9.7 times the measured events per lineage** (21.05 M; 10.8 times on the <2% set; 11.3-12.5 times if only the 78-86% fixed share of the differences is counted). The 410 M base-pair figure is of the same order as base pairs in the alignment-defined divergent regions (261-523 M), so the number is reproducible as bp but not as events.

Predictions: events held (P2 total, P4); SNV count, gap bp and the lowest bp/event band missed (§2).

## 1. Scripts, pre-registration and disclosure

- **Pre-registered script:** `research/checks/gap07b_alignment_count.py`, committed as **3c847b8** before the main run. Predictions P1-P8 and the Day-vs-critics criteria are in its docstring. `git diff 3c847b8` for that file is empty after the run.
- **Main-run outputs:** committed as **51cea1f**; `results/raw/gap07b_{net,chain,gor,axt,report}.{json,out}`, `gap07b_run.start/.end` (00:51:23 to 01:01:12, 9 min 49 s wall, local, `nice -n 19`, single process).
- **Post hoc scripts and outputs** (labelled post hoc in their docstrings), committed as **c1727f0**:
  - `gap07b_posthoc_blocks.py` (exact aligned blocks; "clean" gap bp);
  - `gap07b_posthoc_polarize.py` (symmetric indel polarization; replaces a flawed pre-registered rule, §7);
  - `gap07b_posthoc_ladder.py` (arithmetic only).
- **Disclosure of what was seen before registering:** first ~3 KB of the axt file; first ~30 net lines; chain header; record count (157,734) and chromosome order of the pan axt; file sizes and md5; hg38 N total 161.6 Mb; centromere-model total 59.5 Mb. A smoke test on a truncated prefix showed two design facts, which changed the design before registration. (i) Net `gap` lines are intervals on the human side, so chimp-only insertions never appear; the chain file is therefore the complete indel list. (ii) axt records break at chain gaps >100 bp. No smoke-test number set any prediction. I did glance at the smoke tables after writing the predictions and did not change them.
- **The workhorse was not used.** It was busy ("chain-end" not yet in `h3fp.host` when I checked), and the full run needed ten minutes of one niced core locally.

## 2. Scorecard against the pre-registered predictions

| # | prediction | observed | verdict |
|---|---|---|---|
| P1 | SNV 27-35 M (point 30 M) | **37.77 M** (33.77 M in records <2% divergence) | **missed** (+8% over band top); divergence per valid column 1.346% (band 1.15-1.35%, edge), Ts/Tv 2.053 (band 2.0-2.2) held |
| P2 | indel events 3.5-6.5 M total | **4.30 M** | **held** (point 5 M was 16% high) |
| P2 | CSAC "~5 M in each species" vs 5 M total; falsifier total >8 M | total 4.30 M; per species 2.17 M / 2.09 M | **held** for "5 M is the two-lineage total" |
| P2 | size mix: 1 bp 40-55% | 40.8% | held |
| | 2-10 bp 35-45% | 48.4% | missed |
| | 11-50 bp 6-10% | 8.2% | held |
| | 51-1000 bp 2-4% | 2.1% | held (edge) |
| | >1000 bp 0.05-0.3% (3-15 k) | 0.54% (23,249) | missed |
| | both-sided <8% | 0.8% | held |
| P3 | gap bp 60-110 Mb | **597 Mb** raw (270 Mb without flagged-N gaps; 192 Mb "clean", §6) | **missed** by a wide margin |
| P3 | events >50 bp <5% of events but >50% of bp | 2.6% of events, 97.2% of bp | held |
| P4 | total events 33-45 M (point 38 M) | 42.1 M | held (point 11% low) |
| P4 | per lineage 16-23 M | 21.05 M | held |
| P4 | fills + unaligned <5% of events | 0.1% | held |
| P5 | L1 = 30 M | 37.77 M | missed (as P1) |
| P5 | L2 bp 100-170 Mb | 634 / 307 / 151 / 114 Mb (F0/F1/F2/F3) | missed for F0, F1; held for F2, F3 |
| P5 | L3 bp 300-700 Mb | 714 / 387 / 231 / 194 Mb | held F1 only (F0 just above, F2, F3 below) |
| P5 | L2 bp/event 3-5 | 15.1 / 7.3 / 8.2 / 6.6 | missed |
| P5 | **L3 bp/event 7-18** | **17.0 / 9.2 / 12.5 / 11.3** | **held under all four filters** |
| P5 | unaligned human bp overlap with centromere models >30% | 85% (59.5 of 69.9 Mb outside fills) | held |
| P6 | polarizable SNV >=85%; human-derived 47-51%; third 1-5% | 95.2%; 48.6% of (human+chimp derived); 1.2% | held |
| P6 | indel human share 40-52% | **33%** as pre-registered; 38-52% post hoc depending on window (§7) | missed as run; method-limited |
| P7 | F1 changes SNV <1%, indel events <3% | 0% and 0.02% | held |
| P7 | F2 removes 35-55% of SNV, 20-45% of indel events | 55.7% and 60.5% | missed (slightly, clearly) |
| P7 | F3 cuts total events 40-60% | 59% (42.07 to 17.24 M) | held |
| P7 | L3 bp/event within 6-25 under every filter | 9.2-17.0 | held |
| P8 | unaligned share of human non-N 5-12% | 2.4% outside net fills; 4.6% outside aligned blocks (post hoc); 9.0% incl. non-colinear nested fills (post hoc) | pre-registered definition missed |
| P8 | nested inversion fills >=10 kb: 200-1,500 | 453 | held |

The criteria stated in advance as "favours Day" (events per lineage near 100 M; bp/event at L3 <=3 under every filter; one lineage carrying far more than half) were **not met**. The criteria for "favours critics" (15-30 M per lineage; L3 bp/event near 10, robust to masking) were **met**.

## 3. Data and provenance

All files from `https://hgdownload.soe.ucsc.edu/goldenPath/`, saved under `sources/raw/ucsc-2026-10-09/` (gitignored, untrusted, never executed; scripts live outside; run with `research/.venv/bin/python -I`). md5 values match UCSC's `md5sum.txt` where listed.

| file | md5 |
|---|---|
| hg38/vsPanTro6/hg38.panTro6.net.axt.gz (1.6 GB) | a6a9564a020342dcac87dc59775b34f9 |
| hg38/vsPanTro6/hg38.panTro6.net.gz | 713b0fd20d33849c42ca60f39444f898 |
| hg38/vsPanTro6/hg38.panTro6.all.chain.gz | f84aed5fad3a60a8fb18cfab49e81875 |
| hg38/vsGorGor6/hg38.gorGor6.net.axt.gz (1.5 GB) | aac35865d02e1b9d30e5842347aa1595 |
| hg38/vsGorGor6/hg38.gorGor6.net.gz (not used) | 842e79d63cc0c427a581e60baf4285be |
| hg38 / panTro6 `database/gap.txt.gz`, hg38 `centromeres.txt.gz`, `bigZips/*.chrom.sizes` | in `sources/raw/ucsc-2026-10-09/meta/` |

Sources of the comparisons: CSAC 2005 and Yoo 2025 quotes are from `docs/research/sources/quotes-literature.md`.

**Scope and definitions.** Human target = primary chromosomes only (hg38 ALT contigs duplicate primary sequence). SNV = column with A/C/G/T in both species that differ (N excluded). Indel event = one chain gap (dt, dq) inside a netted alignment, located by chain id and t-range, so chimp-only insertions are included. Validation of that list: chain gaps of 1 bp 1,754,185 against axt in-record gap runs 1,754,112; 2-10 bp 2,080,225 against 2,079,277; human-containing net gap lines 894,824 against chain human-only 894,751 + 73 both-sided (1 bp).

## 4. SNVs

| filter | SNVs | share of F0 |
|---|---|---|
| F0 raw (N columns excluded by construction: 2,094 of 2.82 G columns) | 37,767,396 | 1.000 |
| records with <2% divergence only (post hoc, from the main-run table) | 33,765,842 | 0.894 |
| F2 not lowercase (repeat-masked) in either species | 16,722,020 | 0.443 |
| F3 = F2 + not within 5 columns of a gap + records <5% divergent | 15,557,169 | 0.412 |

- 2.805 G valid columns; 1.346% differ (1.248% of unmasked columns). 51.8% of valid columns are soft-masked and they carry 55.7% of the SNVs.
- The 4.0 M extra SNVs, compared with CSAC's 35 M, sit in alignment records of 2.6%, 6.8% and 14.2% divergence (mean 1.25% in the <2% class): nested/rearranged fills, paralog and duplicate alignments, and ancestral polymorphism. CSAC's 35 M and 1.23% match the <2% class well.
- Adjacent mismatch pairs: 1,443,846 (so multi-nucleotide runs shave about 1.4 M off a "mismatch runs" count; not applied).
- **Polymorphism:** CSAC says 14-22% of differences are polymorphic, not fixed. Fixed SNVs would be 29.5-32.5 M (F0) or 26.3-29.0 M (<2% set). This is not measured here.

## 5. Indel events by size class

| size class | human-only | chimp-only | both-sided | all | share of events | bp (raw) | share of bp |
|---|---|---|---|---|---|---|---|
| 1 | 894,751 | 859,361 | 73 | 1,754,185 | 0.408 | 1.75 M | 0.003 |
| 2-10 | 1,048,210 | 1,031,067 | 948 | 2,080,225 | 0.484 | 8.2 M | 0.014 |
| 11-50 | 185,074 | 159,466 | 9,409 | 353,949 | 0.082 | 7.1 M | 0.012 |
| 51-1000 | 37,241 | 36,567 | 16,236 | 90,044 | 0.021 | 22.9 M | 0.038 |
| >1000 | 6,576 | 8,201 | 8,472 | 23,249 | 0.0054 | 556.7 M | 0.933 |
| all | 2,171,852 | 2,094,662 | 35,138 | **4,301,652** | 1 | 596.7 M | 1 |

- **Comparison with CSAC 2005:** 4.3 M against "~5 million indel events"; human-only 2.17 M and chimp-only 2.09 M. CSAC's sentence "~5 million events in each species" therefore overstates a per-species count; the figure is a two-lineage total. This also fits the R4 reading that indel:SNV is 0.114 here (4.30/37.77), against 0.14 from CSAC counts and 0.04-0.125 from germline rates.
- Small events dominate counts (89% are 1-10 bp) and large events dominate bp (93% of raw gap bp from 0.5% of events).

## 6. Base pairs next to events

**Raw gap bp is not a clean measure.** The post hoc block analysis (`gap07b_posthoc_blocks.py`) splits each chain gap into N, aligned-elsewhere, and "clean" bases:

| size class | events | raw bp | N bp | aligned elsewhere | clean bp |
|---|---|---|---|---|---|
| 1 | 1,754,185 | 1.75 M | 0 | 0.04 M | 1.71 M |
| 2-10 | 2,080,225 | 8.18 M | 0 | 0.18 M | 8.00 M |
| 11-50 | 353,949 | 7.07 M | 0.0003 M | 0.21 M | 6.86 M |
| 51-1000 | 90,044 | 22.9 M | 0.02 M | 2.85 M | 20.1 M |
| >1000 | 23,249 | 556.7 M | 44.9 M | 356.0 M | 155.8 M |
| all | 4,301,652 | 596.7 M | 44.9 M | 359.3 M | **192.4 M** |

- Of the 557 Mb in events >1 kb, 64% is sequence aligned elsewhere in the net (rearranged or duplicated material, already counted as nested fills) and 8% is assembly N.
- Clean gap bp by kind: human-only 37.5 Mb, chimp-only 59.8 Mb (CSAC: ~32 Mb and ~35 Mb; the larger chimp-specific figure here includes all sizes), both-sided 95.1 Mb (35 k events averaging 2.7 kb).
- Events >1 kb by size: 1-10 kb 20,928 (clean 57.0 Mb); 10-100 kb 1,905 (32.3 Mb); 100 kb-1 Mb 359 (28.6 Mb); >1 Mb 71 (37.9 Mb of 300.7 Mb raw). The largest event is 25.2 Mb, almost all aligned elsewhere.

**Sequence not in any aligned block** (non-N bases):

| genome | non-N | outside all aligned blocks | share | of which in hg38 centromere models |
|---|---|---|---|---|
| human primary | 2,937.7 Mb | 134.5 Mb | 4.6% | 59.5 Mb (outside fills; 85% of the 69.9 Mb there) |
| chimp placed | 2,803.6 Mb | 88.6 Mb | 3.2% | n/a |
| chimp unplaced scaffolds | 215.0 Mb | 187.0 Mb | 87% | n/a |
| non-colinear nested fills (aligned bases, both syn/nonSyn/inv) | | 131.3 Mb | 4.5% of human non-N | |

**The ladder (events and bp, both genomes, primary chromosomes).** Events are SNV + indel events + 32,045 nested fills + 7,452 outside-fill unaligned segments = 42,108,545.

| bp measure | bp | bp / event | 410 M / bp |
|---|---|---|---|
| SNV only | 37.8 M | 0.90 | 10.9 |
| SNV + outside aligned blocks (human + chimp placed) | 260.8 M | 6.19 | 1.57 |
| SNV + outside aligned blocks + non-colinear nested aligned (human 265.8 M, chimp 219.9 M non-1:1; Yoo-style) | 523.5 M | 12.43 | 0.78 |
| main-run L3, F0 (SNV + raw gap bp + unaligned outside fills) | 714.4 M | 16.97 | 0.57 |
| main-run L3, F1 / F2 / F3 | 387 / 231 / 194 M | 9.20 / 12.51 / 11.25 | |

- **Yoo-style analogue.** My human "non-1:1" total (unaligned + non-colinear) is 265.8 Mb, 9.05% of the genome; Yoo reports 327 Mb (10%) per ape lineage on T2T assemblies, a different and stricter definition. Direction and order agree; they are not the same quantity.
- **A numeric coincidence, flagged.** Human unaligned (134.5) + chimp placed unaligned (88.6) + chimp unplaced scaffolds unaligned (187.0) = 410.09 Mb. This sum mixes three arbitrary components and uses assembly-fragment artefacts (the 187 Mb is mostly unplaced scaffolds without a human partner). Day's 410 M is a different construction (Yoo T2T: 35 M SNV + 2 x 187 Mb per the critic reconstruction in A3a). I treat the match as chance, and note it only so nobody finds it later and reads it as evidence.
- **Reading.** Day's bp number is of the right magnitude for "differing sequence", but each unaligned or non-colinear stretch is one structural event: 42 M events, not 410 M.

## 7. Lineage split

| item | human | chimp | unpolarized / third |
|---|---|---|---|
| SNV (F0, gorilla outgroup) | 17,277,924 (48.0%) | 18,252,738 (50.8%) | 1,808,787 + 427,947 (third state 1.2% of polarizable) |
| human share of (human+chimp derived) | 0.486 (F2 0.490; F3 0.496) | | |
| per-lineage events (SNV + indel, unpolarized split 50/50) | 19.9 M | 22.1 M | mean 21.0 M |

- **SNV polarization** (gorilla base equals chimp base, or equals human base) is reliable. The chimp branch is slightly longer.
- **Indel polarization as pre-registered was flawed** and is reported as a defect. The rule required exact base-by-base agreement with the gorilla alignment for human-only gaps but a +-2 window for chimp-only gaps. Two independent pairwise alignments place gaps in repeats differently, so exact agreement fails more often. Result: human-only gaps scored 25% human-lineage at 1 bp, chimp-only gaps 46%, with an overall 33% human share, which is a method artefact.
- **Post hoc symmetric rule** (`gap07b_posthoc_polarize.py`; one rule, same window both sides) gives human share of polarized single-sided indels of **0.378 / 0.423 / 0.474 / 0.516 for window w = 2 / 5 / 10 / 20**; 91% polarizable. The split is therefore consistent with 50/50 but the method cannot say better than "38-52% human". Events >50 bp polarize unreliably (human share 0.0-0.19 in the 51-1000 and >1000 classes for all w).
- Consequence: per-lineage events are about 21 M (19.9-22.1 M under the SNV split plus symmetric indels). Halving the total, as Day does, is supported to within the method's resolution (A3d).

## 8. Masking and artefact sensitivity

| filter | SNVs | indel events | total events (+ fills + segments) | L3 bp / event |
|---|---|---|---|---|
| F0 raw | 37.77 M | 4,301,652 | 42.11 M | 16.97 |
| F1 no assembly-N in event | 37.77 M | 4,300,949 | 42.10 M | 9.20 |
| F2 + not repeat-masked | 16.72 M | 1,699,274 | 18.45 M | 12.51 |
| F3 + no TRF, unplaced-chimp, adjacent opposite gap; SNV not near gap, records <5% | 15.56 M | 1,680,903 | 17.27 M | 11.25 |

- **N and gap artefacts:** SNV and event counts do not move. They only move raw bp (597 to 270 Mb).
- **Repeat masking** removes 56% of SNVs and 61% of indel events. This is the bulk of the genome (hg38 is about 50% masked), not a pure artefact filter: masked sequence carries real differences, including Alu/CpG sites. It is a lower bound for "unique sequence" events.
- The key ratio, 205 M per lineage against events per lineage, stays 9.7 (F0), 10.8 (<2% SNV set), 22.2 (F2) and 23.7 (F3).
- Alignment-fragmentation effect (one true event split into several chain gaps) could not be measured; it biases event counts up, i.e. toward Day.

## 9. Comparison with the literature figures

| item | this check | CSAC 2005 / Yoo 2025 |
|---|---|---|
| SNV differences | 37.8 M (33.8 M in records <2% divergence) | ~35 M (CSAC) |
| divergence | 1.35% (1.25% in <2% records) | 1.23% (CSAC) |
| Ts/Tv | 2.05 | not quoted in `quotes-literature.md` |
| indel events | 4.30 M total (2.17 + 2.09 M) | ~5 M (CSAC; "in each species" wording resolved as a total) |
| species-specific indel sequence | clean 37.5 Mb human, 59.8 Mb chimp (all sizes) | ~32 Mb, ~35 Mb (CSAC) |
| non-1:1 / unaligned share | 9.05% human (incl. non-colinear), 7.8% chimp placed | 10% average SDR per ape lineage (327 Mb); 12.5-27.3% failed to align or not 1:1 (Yoo) |
| inversion-type events | 453 nested inversion fills >=10 kb (net) | 1,140 curated across six apes (Yoo) |

## 10. Caveats

1. **One genome copy each.** SNV and indel counts are differences between one human haplotype (hg38, a mosaic) and one chimp (panTro6), so they include polymorphism and assembly errors. CSAC puts polymorphism at 14-22% of the SNV divergence. No attempt was made to subtract it.
2. **Alignment-defined events.** A "chain gap" is what the aligner and chainer decided. Fragmentation of one event into several gaps inflates counts; merging of nearby events deflates them. Repeat-heavy regions are the main risk, which is why F2 is shown, but F2 is a bound for unique sequence and not a correction.
3. **Net scope.** The net picks the best chimp match per human base. Segmental-duplication content, multi-copy sequence and centromeres align poorly or not at all; their events are under-counted (critic-favouring direction) while their bp are over-represented in "unaligned" (Day-favouring direction).
4. **bp definitions differ.** The post hoc bp ladder uses my choices (aligned blocks, nested fills, placed chimp only). Yoo's SDR definition is different and on T2T assemblies. The two should not be equated.
5. **Indel polarization is weak** (§7). SNV polarization is sound. No large-event (inversion, translocation) polarization was attempted.
6. **Events are not fixations.** An event list says how many mutational events separate the two copies, not how many selected fixations are required. This check is neutral on whether each event has to pass through selection (branch A vs B and the two-model framing in `R4-GAPS-04-07-02.md`).
7. **Pre-registered mis-specifications** are reported as such: the indel polarization rule, the P3 band for gap bp (set without anticipating that two-thirds of large-event bp are aligned elsewhere) and the P1 SNV band (set without anticipating 4 M SNVs in >2%-divergence records).
8. The chimp side of the chain pass covers only chains used by the net on the human primary chromosomes; chimp bases aligned only to hg38 ALT or unplaced contigs count as unaligned.
9. Not reviewed. The independent reviews that the other R4 checks received are pending.

## 11. Who this helps

**Critics, on the unit argument (strongly).** The central claim of A3x is confirmed with a measurement and without a rate model: there are 42 M mutational events between the two assemblies, 21 M per lineage; 205 M is 9.7 times that. The critics' informal figures (Mansfield's ~25 M, 40 M from CSAC, 17.5-20 M per lineage) are in the right region; the measured 21 M per lineage is above the lowest of them. The bp-versus-events distinction (McCarthy, Fun-Friendship4898, Neukamm via Nesslig20) is the right one.

**Day, on several points that the critics have not conceded.**
- The base-pair figure is real. Alignment-defined divergent sequence is 260-520 Mb across the two genomes, so 410 M is not an invented magnitude, and Yoo's finding of divergence well beyond SNVs is reproduced in a simpler data set (non-1:1 fraction 9% of the human genome).
- The SNV-only variant (17.5 M per lineage, A3b) leaves out the indel events: about 2.2 M per lineage on the measured data, so 19.1-21.1 M per lineage is the event total. The shift is about 12-20% and does not rescue the unit argument, but it shows the SNV-only figure is a floor and not the event count.
- The measured total (42.1 M) is within 5% of the 40 M used in A3x (35 M SNV + 5 M indel), so the critics' arithmetic holds up; it was nevertheless built on a total (5 M) that CSAC's own wording made ambiguous.
- The lineages are close to symmetric (SNV 49/51 human/chimp), so Day's own "apportion symmetrically" step (A3a, A3d) is supported; any critic arguing that the human lineage carries much less than half would not find support here.
- The measurement does not show that events are not selected, or that neutral fixation of most of them is possible; that is branch B and H, outside this check.

**Neither side, as stated.** The "bp per event is 10" statement used by critics needs its definition: 6 (strict unaligned) to 17 (raw gap bp). The order of magnitude holds under every mask, but the exact ratio does not.

## 12. Reproduce

```
cd ~/projects/evo-sim; D=sources/raw/ucsc-2026-10-09; M=$D/meta; R=research/checks/results/raw
py(){ nice -n 19 research/.venv/bin/python -I research/checks/gap07b_alignment_count.py "$@"; }
py net   --net $D/pan/hg38.panTro6.net.gz --t-sizes $M/hg38_bigZips_hg38.chrom.sizes --q-sizes $M/panTro6_bigZips_panTro6.chrom.sizes \
         --t-gaps $M/hg38_database_gap.txt.gz --q-gaps $M/panTro6_database_gap.txt.gz --t-cen $M/hg38_database_centromeres.txt.gz \
         --work $D/work/ev --out $R/gap07b_net.json
py chain --chain $D/pan/hg38.panTro6.all.chain.gz --work $D/work/ev --out $R/gap07b_chain.json
py gor   --axt $D/gor/hg38.gorGor6.net.axt.gz --t-sizes $M/hg38_bigZips_hg38.chrom.sizes --work $D/work/gor
py axt   --axt $D/pan/hg38.panTro6.net.axt.gz --t-sizes $M/hg38_bigZips_hg38.chrom.sizes --events $D/work/ev --work $D/work/gor --out $R/gap07b_axt.json
py report --net-json $R/gap07b_net.json --axt-json $R/gap07b_axt.json --out $R/gap07b_report.json
# post hoc
research/.venv/bin/python -I research/checks/gap07b_posthoc_blocks.py --chain $D/pan/hg38.panTro6.all.chain.gz --work $D/work/ev \
   --t-sizes ... --q-sizes ... --t-gaps ... --q-gaps ... --out $R/gap07b_posthoc_blocks.json
research/.venv/bin/python -I research/checks/gap07b_posthoc_polarize.py --ev $D/work/ev --gor $D/work/gor --out $R/gap07b_posthoc_polarize.json
research/.venv/bin/python -I research/checks/gap07b_posthoc_ladder.py $R
```

Output files: `results/raw/gap07b_report.out` (main tables), `gap07b_posthoc_blocks.out`, `gap07b_posthoc_polarize.out`, `gap07b_posthoc_ladder.out`.

## 13. Suggested edits for the lead (not applied)

- A3x `external:` can cite a measured 42.1 M events (21.1 M per lineage), 205 M = 9.7x; the rate-based 9-11x range is consistent.
- A3x "Pre-registered prediction: 40M ± 30%" is met (42.1 M).
- A3b: the SNV-only concession leaves about 20% of events out (indels, ~2.2 M per lineage).
- A3c: the net SNV count includes 4 M SNVs in >2%-divergence alignments (paralog/nested/polymorphic); 14-22% polymorphism would lower fixed counts to ~26-32 M.
- The CSAC "~5 M in each species" ambiguity is resolved: 4.3 M total.
