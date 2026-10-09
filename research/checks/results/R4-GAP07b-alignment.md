# R4 GAP-07b: direct count of human-chimp divergence events from a real whole-genome alignment

Date: 2026-10-09. Revised 2026-10-09 after three reviews (`REVIEW-R4-GAP07b-correctness.md`, `-steelman-day.md`, `-steelman-critic.md`, committed f8625f6); see §14 "Review resolution". THROWAWAY research check, not product code.

**Tag used throughout:** **[PH]** = post hoc (computed or chosen after the main run). Untagged numbers are from the pre-registered script's main run. Data are **hg38 vs panTro6 (non-T2T)** and every ratio below is for that pair of assemblies.

## 0. Headline: one point in a bracket

**Events (primary chromosomes chr1-22, X, Y; hg38 vs panTro6; both lineages plus ancestral polymorphism).** The headline total is the pre-registered main-run number, 42,102,514 (`gap07b_report.out`, L3 F0).

| quantity | count | note |
|---|---|---|
| SNV differences | **37.77 M** | 35.02 M in top-level (colinear) fills, 2.75 M in nested fills [PH]; 33.77 M in alignment records <2% divergent [PH] |
| Indel events (chain gaps inside the net) | **4.30 M** | 2.17 M extra-human-base + 2.09 M extra-chimp-base + 35 k both-sided |
| Nested fills + unaligned segments | 32,045 + 1,421 | 0.08% of events |
| **Total events** | **42.10 M** | 21.05 M per lineage (total / 2) |

**Raw ratio (pre-registered quantity): Day's 205 M per lineage = 9.7 times the measured events per lineage.**

**Events are not fixations, and events are not selected.** This check counts mutational events that separate two assemblies. It does not say how many of them had to pass through selection, how many could fix neutrally, or what any fixation weighs (branches A5, B, G, H; `R4-GAPS-04-07-02.md` two-model framing). The ratio below is the *unit* mismatch only; it is not to be multiplied by a neutral-fraction or rate factor (§11, scoping table).

### The bracket (205 M / events per lineage)

| reading | status | what it assumes | cuts toward | events per lineage | ratio |
|---|---|---|---|---|---|
| **raw pooled (headline)** | pre-registered | events as counted; polymorphism, nested and paralog alignments included; mean of the two lineages | (reference) | 21.05 M | **9.74** |
| *Day-favourable side* | | | | | |
| non-aligned bp (223 Mb outside aligned blocks) counted as 171-bp units added to the events | [PH] | an alpha-satellite-like repeat unit per extra event | Day | 21.70 M | 9.45 |
| same, 32-bp units | [PH] | Yoo's smaller unit (A3a) | Day | 24.54 M | 8.35 |
| non-aligned plus nested aligned bp (486 Mb) as 171 / 32-bp units | [PH] | same, nested aligned sequence also counted | Day | 22.47 / 28.64 M | 9.12 / 7.16 |
| indel events x2 (x3) | [PH] | microsatellite slippage and opposite steps merged by net-length accounting; unmeasured | Day | 23.20 (25.35) M | 8.84 (8.09) |
| non-T2T assemblies | label | repeat-rich sequence (centromeres, SDs, satellites) is under-resolved, so events there are under-counted; direction known, size unmeasured | Day | not quantified | (the two rows above bound it) |
| *Critic-favourable side* | | | | | |
| human lineage alone (gorilla outgroup; indels <=50 bp polarized) | [PH] | Day's 205 M is the human half; 9.94-10.21 over the window and rule choices | critics | 20.27 M | 10.11 |
| SNVs from top-level colinear fills only | [PH] | nested/paralog alignments are not required changes | critics | 19.68 M | 10.42 |
| adjacent mismatches merged (MNV runs) | [PH] | 1.44 M adjacent pairs are one event each | critics | 20.33 M | 10.08 |
| records <2% divergent only | [PH] (threshold chosen after the SNV count missed CSAC's 35 M) | drops 4.0 M SNVs in paralog/nested/low-identity records | critics | 19.05 M | 10.76 |
| fixed share 0.86 / 0.78 applied to SNVs only | [PH] | CSAC's 14-22% polymorphic share is an SNV estimate; indels unchanged | critics | 18.41 / 16.90 M | 11.14 / 12.13 |
| same share applied to all events | [PH] | indels and SVs are as polymorphic as SNVs (unmeasured; Day, Q100, says SVs are post-divergence) | critics | 18.10 / 16.42 M | 11.32 / 12.48 |
| <2% records and fixed share on SNVs (not additive) | [PH] | overlapping corrections; upper end | critics | 16.69 / 15.34 M | 12.29 / 13.37 |

**Bracket: about 7 to 14.** The Day-favourable adjustments reach 7.2-9.5, the critic-favourable ones 10.1-13.4, and the raw 9.7 lies between them. Alignment fragmentation (merging chain gaps closer than 1 / 10 / 50 aligned bp) does not move the raw ratio (9.74, 9.76, 9.86; [PH]), so the bracket is not driven by it. The ratio falls to about 5 only if every 6 bp of non-aligned sequence is its own event, and to about 1.5 only if every 1 to 2 bp is (§6).

**The masked rows are a different thing.** Under repeat masking the ratio reads 22 (F2) and 24 (F3). Those rows divide Day's whole-genome 205 M by events found in roughly half the genome (unique sequence), so they are a unique-sequence bound and not "the ratio stays" or "the ratio doubles" (§8).

### Direction of each artefact

| artefact | effect on the event count | the artefact favours | size / bound |
|---|---|---|---|
| non-T2T assemblies (repeats, centromeres, SDs under-resolved) | undercount | Day (raw ratio too high) | unmeasured; repeat-unit rows bound it to ratio 7.2-9.5 [PH]; follow-up: CHM13/hs1 vs mPanTro3 |
| ancestral and within-species polymorphism in the counts | overcount of fixed differences | Day (raw ratio too low) | fixed-share rows: 11.1-12.5 [PH]; CSAC estimate, SNV only |
| SNVs in paralog / nested / >2%-divergent alignments (4.0 M) | overcount | Day | ratio 10.4-10.8 [PH] |
| qDup (query-duplicated top fills, 6% of chimp span per the correctness review) | SNV overcount, unquantified | Day | not measured |
| alignment fragmentation | overcount | Day | merge <=50 bp: ratio 9.74 to 9.86 [PH] |
| adjacent mismatches counted separately | overcount | Day | 10.08 [PH] |
| net-length accounting of tandem-repeat steps | undercount | critics (raw ratio too high) | x2 indels: 8.84 [PH]; assumption |
| both-sided gaps as one event | undercount, <=0.1% | critics | negligible |
| mean of the two lineages instead of the human one | none (see human-lineage row) | Day (raw ratio slightly low) | 10.11 [PH] |
| N runs | none (columns with N are excluded, 2,094 of 2.82 G) | neutral | none |
| repeat masking (F2, F3) | removes real events | not an artefact filter | unique-sequence bound |

### What survives for Day

Day's stated position is a **range with a weighting claim**, not a literal "205 M events" (§11): SNV-only is the lower bracket, every bp of every structural variant counted separately the upper one. Against that position:

- **SNV-only is close to the event count.** Day's 17.5 M per lineage is 83% of the measured events per lineage (21.05 M); SNVs are 90% of all events (37.77 / 42.10 M). With the CSAC fixed share applied (0.78-0.86), measured fixed events per lineage are 16.4-18.1 M [PH], which **brackets** his 17.5 M. The SNV-only row is therefore neither a floor nor a ceiling: the omitted indels (about 10-12% of the SNV-only figure) and the included polymorphism (14-22% of SNV differences) roughly cancel.
- **The SNV-only shortfall rises on the measured count.** At MITTENS 3.0 s7.3 rates (1,322 gen/fix) the shortfall is 91,800 on 17.5 M (Day prints 91,600), 99,100 on the measured SNV/2 (18.9 M), and 110,400 on measured events per lineage (21.05 M) [PH]. With the polymorphism-corrected 16.4-18.1 M it is 86,100-95,000. The same factor applies to the mutator-rate row (7,300 to 7,900-8,800). The rate side (G_f) is outside this check.
- **The base-pair magnitude is of the right order for non-1:1 sequence, with two caveats.** Bases outside every aligned block (human plus chimp placed) are 261 M; removing hg38 centromere models gives 201 M. The 523 M "Yoo-style" row also counts aligned nested sequence (131.3 Mb per genome), which is conserved sequence in a new place or orientation, and double counts 2.75 M SNVs lying inside it (§6). The 261 M row contains 59.5 Mb of hg38 centromere models; "not aligned" is a statement about two assemblies, not a measurement of sequence difference. 410 M is therefore not an invented magnitude, but this check does not show that 410 M bases *differ*.
- **The first-edition "40 million" was an events figure.** Day's own text calls it "35 million single nucleotide differences and 5 million indels affecting roughly 90 million base pairs" (Q97) and the second edition says the first edition "were based on the observed divergence of 40 million base pairs" (Q75). The measured 42.1 M events (non-T2T) is within 5% of it; the "10x increase" (Q74) is an increase in bp, not in events.
- **Day's weighting claim is untested here and needs a very large weight** (§6 and §11): about 3,250 SNV-equivalents per event above 50 bp, if every other event counts 1.

The bracket is for the unit argument only. It does not test whether any of these events must be selected (Day: structural variants "fix" as single low-probability events; critics: most are neutral).

## 1. Scripts, pre-registration and disclosure

- **Pre-registered script:** `research/checks/gap07b_alignment_count.py`, committed as **3c847b8** before the main run. Predictions P1-P8 and the Day-vs-critics criteria are in its docstring. `git diff 3c847b8` for that file is empty.
- **Main-run outputs:** committed as **51cea1f** (`results/raw/gap07b_{net,chain,gor,axt,report}.*`; 00:51:23 to 01:01:12, local, `nice -n 19`, one process).
- **Post hoc, first pass:** `gap07b_posthoc_{blocks,polarize,ladder}.py`, committed as **c1727f0** (labelled post hoc in their docstrings).
- **Post hoc, review-fix pass:** `gap07b_posthoc_review.py` (committed as **3798b92** before it was run) and `gap07b_posthoc_review2.py` (committed as **fbbc580** before it was run). Outputs `results/raw/gap07b_posthoc_review*`. Run local, `nice -n 19`, one process (the workhorse is busy).
- **Disclosure of what was seen before registering:** first ~3 KB of the axt file; first ~30 net lines; chain header; record count (157,734) and chromosome order; file sizes and md5; hg38 N total 161.6 Mb; centromere-model total 59.5 Mb. A smoke test on a truncated prefix showed two design facts, which changed the design before registration: (i) net `gap` lines are human-side intervals, so chimp-only insertions never appear and the chain file is the complete indel list; (ii) axt records break at chain gaps >100 bp. The author states that the predictions were written before the smoke tables were looked at and were not changed afterwards; **git cannot verify the order** (predictions and script are one commit), so that rests on the author's word. The smoke prefix was the chr1 start (subtelomeric), which could not have moved P1-P8 much.

## 2. Scorecard against the pre-registered predictions

Columns: prediction, observed, verdict, and whether the outcome bears on Day's stated position (range with weighting, §11) or on the critics' (event count). Post hoc numbers are tagged.

| # | prediction | observed | verdict | bears on |
|---|---|---|---|---|
| P1 | SNV 27-35 M (point 30 M) | **37.77 M** ([PH] 33.77 M in records <2% divergent, a threshold chosen after this miss; 35.02 M in top-level fills) | **missed** (+8% over band top) | neutral |
| P1 | divergence 1.15-1.35%; Ts/Tv 2.0-2.2 | 1.346% (edge); 2.053 | held | neutral |
| P2 | indel events 3.5-6.5 M total | **4.30 M** | **held** (point 5 M was 14% high) | critics (event count) |
| P2 | CSAC "~5 M in each species" vs total; falsifier total >8 M | total 4.30 M; 2.17 M extra-human-base, 2.09 M extra-chimp-base | **held**: 5 M is a two-lineage total | critics |
| P2 | size mix: 1 bp 40-55% | 40.8% | held | |
| | 2-10 bp 35-45% | 48.4% | missed | |
| | 11-50 bp 6-10% | 8.2% | held | |
| | 51-1000 bp 2-4% | 2.1% | held (edge) | |
| | >1000 bp 0.05-0.3% (3-15 k) | 0.54% (23,249) | missed | |
| | both-sided <8% | 0.8% | held | |
| P3 | gap bp 60-110 Mb | **597 Mb** raw (270 Mb without events touching N; 192 Mb "clean" [PH]) | **missed** (band set without anticipating that 64% of >1 kb gap bp is aligned elsewhere) | Day-neutral |
| P3 | events >50 bp <5% of events but >50% of bp | 2.6% of events, 97.2% of bp | held | critics (unit) |
| P4 | total events 33-45 M (point 38 M) | 42.1 M | held (point 11% low) | critics |
| P4 | per lineage 16-23 M | 21.05 M | held | critics |
| P4 | fills + unaligned <5% of events | 0.08% | held | |
| P5 | L1 = 30 M | 37.77 M | missed (as P1) | |
| P5 | L2 bp 100-170 Mb | 634 / 307 / 151 / 114 Mb (F0-F3) | missed F0, F1; held F2, F3 | |
| P5 | L3 bp 300-700 Mb | 714 / 387 / 231 / 194 Mb | held F1 only | |
| P5 | L2 bp/event 3-5 | 15.1 / 7.3 / 8.2 / 6.6 | missed | |
| P5 | **L3 bp/event 7-18** | **17.0 / 9.2 / 12.5 / 11.3** | **held under all four** (spread 1.85x; "near 10" is loose) | Day-side too (bp magnitude) |
| P5 | unaligned human bp overlapping centromere models >30% | 85% (59.5 of 69.9 Mb outside fills) | held | critics (FF4898, §11) |
| P6 | polarizable SNV >=85%; human-derived 47-51%; third 1-5% | 95.2%; 48.6% of (human+chimp derived); 1.2% | held | neutral |
| P6 | polarizable fraction 60-90% of single-sided indels | 86.4% as run; 91% [PH] (just outside) | held as run | |
| P6 | indel human share 40-52% | **33%** as run (method artefact); 38-52% [PH] depending on window, <=50 bp only (§7) | missed as run; method-limited | |
| P7 | F1 changes SNV <1%, indel events <3% | 0% and 0.02% | held | |
| P7 | F2 removes 35-55% of SNV, 20-45% of indel events | 55.7% and 60.5% | missed | |
| P7 | F3 cuts total events 40-60% | 59% (42.07 to 17.24 M) | held | |
| P7 | L3 bp/event within 6-25 under every filter | 9.2-17.0 | held (but see §8: the filters barely act on the term that drives L3) | |
| P8 | human unaligned share of non-N 5-12% | 2.4% outside net fills; 4.6% outside aligned blocks [PH]; 9.0% with nested fills [PH] | pre-registered definition missed | |
| P8 | chimp unaligned share 5-12% | 0.36% (outside net fills, 10.1 / 2,804 Mb); 3.2% outside aligned blocks [PH]; 7.8% with nested fills [PH] | pre-registered definition missed | |
| P8 | nested inversion fills >=10 kb: 200-1,500 | 453 | held | |

Pre-registered criteria for "favours Day" (events per lineage ~100 M; L3 bp/event <=3 under every filter; a lineage carrying far more than half) were **not met**. For "favours critics" (15-30 M per lineage; L3 bp/event near 10, robust to masking) they were met, with "near 10" loose (9.2-17.0). Those Day criteria test a literal events-near-205 M reading, which is not Day's stated position (§11). The prediction that his position does make, that bp in non-1:1 regions are of the order of 410 M, was met in a qualified way (201-523 M, §6). The misses were not one-directional: SNV count +8% (neutral), indel total 14% under the point and 2-10 bp share high (neutral), raw gap bp (neutral), repeat-masking sensitivity (neutral); fragmentation is Day-favouring (§0).

## 3. Data and provenance

All files from `https://hgdownload.soe.ucsc.edu/goldenPath/`, saved under `sources/raw/ucsc-2026-10-09/` (gitignored, untrusted, never executed; scripts live outside; run with `research/.venv/bin/python -I`). md5 values match UCSC's `md5sum.txt`.

| file | md5 |
|---|---|
| hg38/vsPanTro6/hg38.panTro6.net.axt.gz (1.6 GB) | a6a9564a020342dcac87dc59775b34f9 |
| hg38/vsPanTro6/hg38.panTro6.net.gz | 713b0fd20d33849c42ca60f39444f898 |
| hg38/vsPanTro6/hg38.panTro6.all.chain.gz | f84aed5fad3a60a8fb18cfab49e81875 |
| hg38/vsGorGor6/hg38.gorGor6.net.axt.gz (1.5 GB) | aac35865d02e1b9d30e5842347aa1595 |
| hg38/vsGorGor6/hg38.gorGor6.net.gz (not used) | 842e79d63cc0c427a581e60baf4285be |
| hg38 / panTro6 `database/gap.txt.gz`, hg38 `centromeres.txt.gz`, `bigZips/*.chrom.sizes` | in `sources/raw/ucsc-2026-10-09/meta/` |

**Scope and definitions.** Human target = primary chromosomes only (hg38 ALT contigs duplicate primary sequence). SNV = column with A/C/G/T in both species that differ (N excluded). Indel event = one chain gap (dt, dq) inside a netted alignment, located by chain id and t-range, so chimp-only insertions are included. Validation (reproduced independently by the correctness review): 1 bp chain gaps 1,754,185 against axt in-record gap runs 1,754,112; 2-10 bp 2,080,225 against 2,079,277 (the excess is the 73 and 948 both-sided gaps of those sizes, which axt does not show as gap runs); human-containing net gap lines 894,824 against chain extra-human-base 894,751 + 73 both-sided.

## 4. SNVs

| filter | SNVs | share of F0 |
|---|---|---|
| F0 raw (N columns excluded by construction: 2,094 of 2.82 G columns) | 37,767,396 | 1.000 |
| top-level (colinear) fills only [PH] | 35,017,058 | 0.927 |
| records with <2% divergence only [PH; threshold chosen after the CSAC miss, so agreement with CSAC is by construction, not independent] | 33,765,842 | 0.894 |
| F2 not lowercase (repeat-masked) in either species | 16,722,020 | 0.443 |
| F3 = F2 + not within 5 columns of a gap + records <5% divergent | 15,557,169 | 0.412 |

- 2.805 G valid columns; 1.346% differ (1.248% of unmasked columns). 51.8% of valid columns are soft-masked and carry 55.7% of the SNVs.
- **Nested fills [PH]:** 131.3 M valid columns with 2.75 M SNVs, divergence 2.09% against 1.31% in top-level fills. These are the rearranged/duplicated alignments; the 4.0 M SNVs in records >2% divergent (2.6%, 6.8%, 14.2% classes) are a different cut (paralog, low-identity and nested records).
- **Match to CSAC:** the top-level-fill count (35.02 M) matches CSAC's ~35 M independently of any divergence threshold; this is the cleaner comparison.
- Adjacent mismatch pairs: 1,443,846 (MNV runs would shave 1.4 M off a runs count; bracket row above).
- **Polymorphism:** CSAC says 14-22% of the differences are polymorphic. Fixed SNVs would be 29.5-32.5 M (F0) or 26.3-29.0 M (<2% set). Not measured here. Pre-split and within-species polymorphic differences are not post-split fixations because they were segregating in the ancestor or still segregate; differences that sorted into reciprocal fixation after the split (ILS) *are* required fixations (Day, 04-28 ¶24, makes this point). A direct measurement is feasible (intersect human-derived SNVs with population allele frequencies, GAP-07c, not run).

## 5. Indel events by size class

| size class | extra human bases | extra chimp bases | both-sided | all | share of events | bp (raw) | share of bp |
|---|---|---|---|---|---|---|---|
| 1 | 894,751 | 859,361 | 73 | 1,754,185 | 0.408 | 1.75 M | 0.003 |
| 2-10 | 1,048,210 | 1,031,067 | 948 | 2,080,225 | 0.484 | 8.2 M | 0.014 |
| 11-50 | 185,074 | 159,466 | 9,409 | 353,949 | 0.082 | 7.1 M | 0.012 |
| 51-1000 | 37,241 | 36,567 | 16,236 | 90,044 | 0.021 | 22.9 M | 0.038 |
| >1000 | 6,576 | 8,201 | 8,472 | 23,249 | 0.0054 | 556.7 M | 0.933 |
| all | 2,171,852 | 2,094,662 | 35,138 | **4,301,652** | 1 | 596.7 M | 1 |

- "Extra human bases" (human-only gap) is a human insertion or a chimp deletion; it is not a per-species count. Only the sum, 4.30 M, is a two-lineage total without polarization.
- **CSAC 2005:** 4.3 M against "~5 million indel events". CSAC's "~5 million events in each species" cannot be read as per species (that would be about 10 M, 2.3x the measurement); the 5 M is a two-lineage total, 14% above the measurement.
- **Size spectrum against the critics' claim [PH-neutral, from the main run]:** McCarthy (MC-11): "a single mutational event can cause hundreds, thousands, or even millions of base-pair differences." The chain gaps: 11-50 bp 353,949; 51-1000 bp 90,044; 1-10 kb 20,928; 10-100 kb 1,905; 100 kb-1 Mb 359; >1 Mb 71; largest 25.2 Mb (§6). That is a direct confirmation of the range.
- Small events dominate counts (89% are 1-10 bp) and large events dominate bp (93% of raw gap bp from 0.5% of events).
- **Double representation (correctness m7):** 19,111 net gap lines contain child fills, so those events are also counted as nested fills (upper bound 0.05% of events); about 1,000 both-sided gaps of 1-10 bp are not visible as axt gap runs, so their mismatches also appear as SNVs. Neither affects the ratio.

## 6. Base pairs next to events

**Raw gap bp is not a clean measure.** Post hoc block analysis [PH] (`gap07b_posthoc_blocks.py`) splits every chain gap into N, aligned-elsewhere, and "clean" bases:

| size class | events | raw bp | N bp | aligned elsewhere | clean bp |
|---|---|---|---|---|---|
| 1 | 1,754,185 | 1.75 M | 0 | 0.04 M | 1.71 M |
| 2-10 | 2,080,225 | 8.18 M | 0 | 0.18 M | 8.00 M |
| 11-50 | 353,949 | 7.07 M | 0.0003 M | 0.21 M | 6.86 M |
| 51-1000 | 90,044 | 22.9 M | 0.02 M | 2.85 M | 20.1 M |
| >1000 | 23,249 | 556.7 M | 44.9 M | 356.0 M | 155.8 M |
| all | 4,301,652 | 596.7 M | 44.9 M | 359.3 M | **192.4 M** |

- Of 557 Mb in events >1 kb, 64% is sequence aligned elsewhere in the net (already counted as nested fills) and 8% is assembly N.
- Clean gap bp: extra-human 37.5 Mb, extra-chimp 59.8 Mb (CSAC: ~32 and ~35 Mb for human-specific and chimp-specific indel sequence; the lineage comparison needs polarization, which fails above ~100 bp, §7), both-sided 95.1 Mb (35 k events averaging 2.7 kb).
- Events >1 kb: 1-10 kb 20,928 (clean 57.0 Mb); 10-100 kb 1,905 (32.3 Mb); 100 kb-1 Mb 359 (28.6 Mb); >1 Mb 71 (37.9 Mb of 300.7 Mb raw).

**Sequence not in any aligned block** (non-N bases) [PH]:

| genome | non-N | outside all aligned blocks | share | notes |
|---|---|---|---|---|
| human primary | 2,937.7 Mb | 134.5 Mb | 4.6% | at least 59.5 Mb is hg38 centromere model |
| chimp placed | 2,803.6 Mb | 88.6 Mb | 3.2% | |
| chimp unplaced scaffolds | 215.0 Mb | 187.0 Mb | 87% | unplaced scaffolds, mostly without a human partner |
| nested fills (aligned bases per genome) | | 131.3 Mb (inv 80.7, nonSyn 35.6, syn 15.0) | 4.5% of human | aligned, conserved sequence in a new place or orientation |

**Ladder: events and bp, both genomes, primary chromosomes.** Events (main-run definition) are 42,102,514. The post hoc ladder file counts 6,031 unplaced-scaffold segments as events (42,108,545) while excluding their bp; the headline uses the main-run number. All bp rows below are [PH] except the last two.

| bp measure | bp | bp / event | 410 M / bp | what it measures |
|---|---|---|---|---|
| bases that differ (lower bound): SNV + human outside blocks minus centromere models + chimp placed outside blocks | 201 M | 4.8 | 2.04 | counts neither centromere models nor aligned nested sequence |
| SNV + outside blocks (human + chimp placed) | 261 M | 6.2 | 1.57 | includes 59.5 Mb of centromere models; "not aligned" is a statement about assemblies |
| Yoo-style: above + aligned nested sequence on both sides, SNVs inside nested fills not double counted | 521 M (523 M as first published) | 12.4 | 0.79 | includes aligned conserved sequence; the first-published 523 M counted 2.75 M SNVs twice |
| same without syntenic ("syn") nested fills | 491 M | 11.7 | 0.84 | UCSC "syn" fills are colinear with the parent |
| main-run L3 F0 (SNV + raw gap bp + unaligned outside fills; pre-registered) | 714 M | 17.0 | 0.57 | raw gap bp, 64% of its >1 kb part aligned elsewhere |
| main-run L3 F1 / F2 / F3 | 387 / 231 / 194 M | 9.2 / 12.5 / 11.3 | | see §8 |

Reading: bp in non-1:1 regions are of the order of 10^8 per genome pair (201-523 M by definition, 714 M raw), with 42 M events behind them. McCarthy (MC-11), the r/DebateEvolution commenter (RE-05) and Fun-Friendship4898 had already said that the bases exist and the events are few; the check confirms that first half. It does not show that 410 M bases *differ*: most of the nested bases are aligned and nearly identical, and the centromere component is an assembly artefact of hg38 vs panTro6.

**Yoo comparison.** My human "non-1:1" total (unaligned 134.5 + nested aligned 131.3 = 265.8 Mb, 9.05% of non-N human) against Yoo's 327 Mb (10%) per ape lineage on T2T assemblies: the SDR definition in the paper's supplement (Fun-Friendship4898, Reddit 1wv4zeg pdebkr5) is "sequences that were not aligned or aligned of identity <85%", a different, stricter definition. Order and direction agree; the quantity is not the same, and it says nothing about how many mutations produced it.

**Numeric coincidences, flagged.** (i) Human unaligned (134.5) + chimp placed unaligned (88.6) + chimp unplaced scaffolds unaligned (187.0) = 410.09 Mb. (ii) The 187.0 Mb term also equals Day's "approximately 187 megabases" (Q15) to three digits. Both are almost certainly chance: the sum mixes three arbitrary components, the 187.0 is mostly unplaced scaffolds without a human partner, and Day's 410 is a different construction (Yoo T2T: 35 M + 2 x 187 Mb per the critic reconstruction in A3a). Base rate [PH]: 14 components from this note, 3,458 subsets of 2-5, 3 land within +-0.1% of 410 (410.1, 409.6, 410.4), the density predicts about 3. A3a records a second coincidence (412.1 Mb in Yoo's tables). Neither is evidence.

### Test of Day's weighting reading [PH]

Day's stated rationale (§11) is that a large rearrangement is a rarer event than a point mutation, so a bp count is a generous proxy. What weight would 205 M require?

| reading | extra events added to the 42.1 M | events per lineage | 205 M / that |
|---|---|---|---|
| events as measured | 0 | 21.05 M | 9.7x |
| 223 Mb non-aligned as 171-bp units | +1.3 M | 21.70 M | 9.45x |
| 223 Mb non-aligned as 32-bp units | +7.0 M | 24.54 M | 8.35x |
| non-aligned + nested aligned (486 Mb) as 171-bp units | +2.8 M | 22.47 M | 9.12x |
| 486 Mb non-aligned + nested as 32-bp units | +15.2 M | 28.64 M | 7.16x |
| 486 Mb as 6-bp units | +81.0 M | 61.5 M | 3.3x |
| 486 Mb as 2-bp units | +242.9 M | 142.5 M | 1.4x |
| 486 Mb as 1-bp units (full bp reading) | +485.7 M | 263.9 M | 0.78x |

(The added-event column is for the genome pair, added to the 42.1 M total; events per lineage are (42.1 M + added) / 2. Non-aligned only, 6 / 2 / 1-bp units give 5.17 / 2.67 / 1.55x. Values from `gap07b_posthoc_review_arith.out`.)

- **Weight needed.** There are 113,293 events above 50 bp (56,646 per lineage). If every other event counts 1, each of these must count **about 3,250** SNV-equivalents to reach 205 M per lineage; for the 23,249 events above 1 kb, **about 15,800** each. A 51-1000 bp event averages 255 raw bp, so the needed weight is about 13 times its bp, not bp-proportional.
- **Day's own event counting.** G_f in MITTENS 3.0 counts events: "IS-element insertions are mutations that fix" (`zenodo-23003785.txt` lines 88-94, s2). The rate in the denominator of the shortfall is per event; the numerator would have to be per event too. MITTENS 3.0 s7.3 itself says SVs "should not each count as a single fixation event in the same sense as a point mutation. This is a legitimate methodological concern" (lines 531-533). A weight above 1 would need a measurement that fixation of 1 kb to 100 kb insertions is thousands of times slower than point substitutions in the same assay as G_f.
- **Where a weight has a basis.** Underdominant rearrangements (inversions, fusions; Day 05-13 ¶51 "chromosome fusions create immediate meiotic incompatibility") are of the order of 10^3 events, not 10^5; they cannot carry 184 M of the 205 M.

## 7. Lineage split

| item | human | chimp | unpolarized / third |
|---|---|---|---|
| SNV (F0, gorilla outgroup) | 17,277,924 (48.0%) | 18,252,738 (50.8%) | 1,808,787 + 427,947 (third state 1.2% of polarizable) |
| human share of (human+chimp derived) | 0.486 (F2 0.490; F3 0.496) | | |

- **SNV polarization** is mechanically correct (the correctness review reproduced it on chr21) and symmetric to first order. Its accuracy against the true branch assignment was not measured: assembly errors, ancestral polymorphism sorting into either lineage (14-22% of differences) and incomplete lineage sorting all feed the 48.6 / 51.4 split. "The chimp branch is slightly longer" is a reading, not a finding.
- **Indel polarization as pre-registered was flawed** (exact base-by-base agreement for human-only gaps, +-2 window for chimp-only gaps): 33% human share, a method artefact.
- **Symmetric post hoc rule, and its limit (correctness M1) [PH].** The rule (same window w both sides; `gap07b_posthoc_polarize.py`) cannot see gorilla indels longer than about 100 bp: net-axt records break at chain gaps >100 bp, so a long gorilla gap is "not aligned" (code 255) rather than a gap column, and a gorilla insertion longer than that is in no record. "No signal" is read as chimp lineage. For events >50 bp the rule is blind and the pre-registered rule is also biased, so **indel lineage claims are restricted to <=50 bp events (4.19 M of 4.30 M, 97.4%)**. Human share of polarized <=50 bp events is 0.382 / 0.428 / 0.480 / 0.523 for w = 2 / 5 / 10 / 20, 91% polarizable; above 50 bp 0.11-0.14 (rule blind) and 0.09-0.44 by kind and size under the pre-registered rule, so the >50 bp split (113,293 events) is unresolved. Assigning those events 50/50 changes the per-lineage totals by 0.1%; the worst case (all to one lineage) by 0.27%.
- **Per-lineage events, recomputed with the stated rule (correctness M2) [PH]** (SNV: polarized plus half of unpolarized and third; indels: polarized plus half of unpolarized and complex):

| rule | w = 2 | w = 5 | w = 10 | w = 20 |
|---|---|---|---|---|
| human lineage, all sizes | 20.07 M | 20.25 M | 20.45 M | 20.61 M |
| chimp lineage, all sizes | 22.00 M | 21.82 M | 21.62 M | 21.46 M |
| human lineage, <=50 bp polarized, >50 bp split 50/50 | 20.10 M | 20.27 M | 20.47 M | 20.63 M |
| 205 M / human lineage (<=50 bp) | 10.20 | 10.11 | 10.01 | 9.94 |

  The 19.9 M human and 22.1 M chimp of the first version of this note came from the flawed pre-registered indel rule (`gap07b_report.out`) and are withdrawn. The lineages are near symmetric; the mean stays 21.05 M. The support for halving the total comes from the SNV split (90% of events), not from the indel polarization.

## 8. Masking and artefact sensitivity

| filter | SNVs | indel events | total events (+ fills + segments) | L3 bp / event |
|---|---|---|---|---|
| F0 raw | 37.77 M | 4,301,652 | 42.10 M | 16.97 |
| F1 no assembly-N in event | 37.77 M | 4,300,949 | 42.10 M | 9.20 |
| F2 + not repeat-masked | 16.72 M | 1,699,274 | 18.45 M | 12.51 |
| F3 + no TRF, unplaced-chimp, adjacent opposite gap; SNV not near gap, records <5% | 15.56 M | 1,680,903 | 17.27 M | 11.25 |

- **N (correctness M3).** F1 removes whole *events* that touch at least one N, not N bases. The net has 680 flagged gap lines (137 tN, 557 qN); their whole span is 327.1 Mb, of which only about 40-45 Mb is N. So of the fall in raw gap bp from 597 to 270 Mb, about 280 Mb is non-N material (mostly sequence aligned elsewhere), and N accounts for roughly 12% of it. Event counts do not move.
- **One-sided flags.** Chimp-only gaps (dt = 0) have no net gap line, so they carry no N, repeat or TRF flag at any size and pass every filter (their raw bp, 96.7 Mb, exceeds the extra-human 52.0 Mb). F1-F3 bp are filtered on one side only.
- **A constant term.** The unaligned term in L3 (80.0 Mb outside fills) is identical in F0-F3: no filter touches it, and it is 41% of F3's 194 Mb. P7's "bp/event stays 6-25 under every filter" is true as computed, but the filters barely act on the term that drives L3.
- **Repeat masking removes 56% of SNVs and 61% of indel events.** That is half the genome (hg38 is about 50% soft-masked), including real differences at Alu and CpG sites; F2/F3 are unique-sequence counts, not artefact corrections. Against Day's whole-genome 205 M the ratio reads 22.2 (F2) and 23.7 (F3); this is **a unique-sequence bound, not "the ratio stays" and not "the ratio doubles"**.
- Fragmentation: merging chain gaps closer than 1 / 10 / 50 aligned bp [PH] removes 160 / 89,133 / 520,696 events and moves the raw ratio 9.74 to 9.74 / 9.76 / 9.86 (same-chain adjacency approximated by file order).

## 9. Comparison with the literature figures

| item | this check | CSAC 2005 / Yoo 2025 |
|---|---|---|
| SNV differences | 37.8 M (35.0 M in top-level fills [PH]; 33.8 M in records <2% divergent [PH]) | ~35 M (CSAC) |
| divergence | 1.35% (1.25% in <2% records) | 1.23% (CSAC) |
| Ts/Tv | 2.05 | not quoted in `quotes-literature.md` |
| indel events | 4.30 M total (2.17 + 2.09 M) | ~5 M (CSAC; "in each species" wording resolved as a total) |
| species-specific indel sequence | clean 37.5 Mb extra-human, 59.8 Mb extra-chimp (all sizes, unpolarized) | ~32 Mb, ~35 Mb (CSAC) |
| non-1:1 / unaligned share | 9.05% human (incl. nested fills), 7.8% chimp placed [PH] | 10% average SDR per ape lineage (327 Mb); 12.5-27.3% failed to align or not 1:1 (Yoo) |
| inversion-type events | 453 nested inversion fills >=10 kb (human-chimp net) | 1,140 curated across six apes (Yoo) |

## 10. Caveats

1. **One genome copy each; non-T2T.** Counts are differences between one hg38 haplotype and one panTro6 assembly, so they include polymorphism, assembly errors and mosaic structure. Repeat-rich sequence (centromeres, satellites, SDs) is under-resolved; that undercount favours Day and is only bounded, not measured (§0 table).
2. **Alignment-defined events.** Fragmentation and merging of events are partly bounded (§8); repeat-heavy regions remain the main risk.
3. **Net scope.** The net picks the best chimp match per human base. "Unaligned" is a statement about the two assemblies and the aligner; it is not a measurement of sequence difference (panTro6 is not T2T; hg38 centromere models have no chimp counterpart in the assembly).
4. **bp definitions differ.** The bp rows use my choices. Yoo's SDR definition is different and on T2T assemblies.
5. **Indel polarization is weak and restricted to <=50 bp** (§7). No large-event polarization.
6. **Events are not fixations, and events are not selected** (§0). The check is neutral on branches A5, B and H.
7. **Pre-registered mis-specifications** are reported as such: the indel polarization rule, the P3 gap-bp band, the P1 SNV band, and the P8 definition of unaligned.
8. The chain pass covers chains used by the net on human primary chromosomes; chimp bases aligned only to hg38 ALT or unplaced contigs count as unaligned.
9. Independent reviews: three, resolved in §14. A re-run on T2T assemblies (CHM13/hs1 vs the Yoo chimp assembly) and a population-frequency measurement of the polymorphic share (GAP-07c) are the two follow-ups that would most reduce the bracket; neither was run.

## 11. Where the result leaves each side

### Day's position as he stated it

Day's stated rationale for counting by bp is a **weighting claim with a range**, not an assertion that 205 M events occurred:

- 04-28 ¶19 (Q99): "A point mutation requires one mutation event and one fixation event. A 50,000 base pair insertion or a chromosomal inversion requires the entire structural rearrangement to occur as a single low-probability event and then to fix. Counting these by base pair, as the gap-divergence figure does, is generous to the standard model. Counting them by independent fixation events would be more devastating still."
- 05-13 ¶4-¶6 (Q101-Q103): "The answer is that it doesn't matter." ... "Fine. Discount every structural variant in the Yoo data to zero. Count nothing but single-nucleotide variants. The shortfall on the SNV-only subset is still four to five orders of magnitude. Going the other direction ... pushes the shortfall to six orders of magnitude. The conclusion holds either way. Counting structural variants as single events is the maximally generous treatment, and the model still fails."
- 04-28 ¶25 (Q100): "Structural variation is, with very few exceptions, post-divergence".
- MITTENS 3.0 s7.3 (Q16) calls the objection "a legitimate methodological concern" and runs SNV-only.

Reading: SNV-only is the lower bracket, bp the upper; the real cost of a large event lies between and is said to be at least that of a point mutation. The earlier statement in A3x that "Day has not, in the corpus, defended counting bp as separate fixations" is superseded.

**What the measurement says about that position.**
- The event count lies between Day's rows, near the lower one: on a log scale 21.05 M is 0.08 dex above his SNV-only 17.5 M and 0.99 dex below 205 M.
- "Discount every SV to zero" is the SNV floor, not the event count: it drops the 4.3 M indel events (10% of events), which are mostly small (89% are 1-10 bp), not structural variants.
- The weighting reading needs about 3,250 SNV-equivalents per event above 50 bp, 13 times more than bp-proportional for a typical 255-bp event (§6). Untested by this check; no measurement of such a weight exists in the corpus.
- Internal inconsistencies in Day's wording: 05-13 ¶5 (Q102) says "approximately 35 million single-nucleotide variants on the human lineage" and "Total: about 205 million" while ¶7 gives 410 M total and 205 M per lineage; 04-28 ¶18 (Q98) gives 415 M / 207 M; "40 million base pairs" in 2nd edition ¶4 (Q75) is the first edition's events figure (Q97). These support the reading that he uses "base pairs", "differences" and "fixations" interchangeably, which is the unit mismatch itself.

### Scoping table: unit, type, rate

| layer | measured here? | statement | do not multiply |
|---|---|---|---|
| unit (events vs bp) | yes | 205 M vs 21.05 M events per lineage: 9.7x raw; bracket about 7-14x | |
| type (neutral vs adaptive) | no | Day concedes the neutral majority qualitatively (`gaps.md` line 250); his reply keeps 200,000 fixations at 99% neutral (Z18165980 l.66). 21 M is an upper bound on required selected fixations, not an estimate of them | the ratios are separate; do not multiply them |
| rate (k = mu, branch B) | no | the k = mu route undershoots the measured counts about 2x (below) | |

### Critics: independent numbers graded against the measurement

Consistency check, not a test of k = mu. Measured: 42.1 M events, 21.05 M per lineage; SNV 37.77 M total, 17.3 M human-derived; polymorphism-corrected fixed events 16.4-18.1 M per lineage [PH].

| critic | quoted number | locator | vs measured |
|---|---|---|---|
| McCarthy | "450 billion x 1/20,000 = 22.5 million fixed mutations." | MC-04 (para 52) | +7% (per lineage) |
| Mansfield | "The numbers I've seen give this number around 25 million give or take, not 200 million." | MF-06 (uncited; per-lineage vs total not stated, per lineage assumed) | +19% per lineage, or -41% if a total |
| Nesslig20 | "the expected number of fixed neutral mutations that separates humans and chimps is ~37.8 million" | PS-02 (a k = mu total) | -0.1% vs 37.77 M SNVs, -10% vs 42.1 M events; inputs carry the PS-01 flag (75 is a per-diploid count) |
| Hancock | "we'll say about 38 million." | GG-09, t=01:56:15 | same as Nesslig20 |
| Dumb-and-Dumber | "or about 9.7 million over its proposed 252,000 generations." | RE-06 (human lineage, k = mu) | **-44% vs 17.3 M human-derived SNVs, -54% vs 21.05 M events** |

Four independent critic routes land within 7-19% of the measurement per lineage (McCarthy +7%, Mansfield +19% with per-lineage assumed) or within 10% of the event total (Nesslig20 and Hancock, 0.1% of the SNV total); the 9.7 M rate route (justatest90 and Wrevellyn give the same) is about 1.8-2.2x low. The rate-based k = mu estimate in R4-GAPS (9.6-10.4 M) is that same route; the calibrated and CSAC-observed event routes (18-22 M per lineage) agree with the direct count, the k = mu route does not. The tension is the clock question (B4a / GAP-06) and favours Day on that sub-point; this check does not resolve it. The earlier "rate-based 9-11x range" folded these two routes together; 205 M / 9.6-10.4 M would be about 20x.

Hancock's GG-10 "the number is 205 million differences, right?" (suspecting 205 M includes gap divergence): the check confirms that 205 M cannot be a count of point mutations (37.8 M SNVs measured) and is reproducible only as bases in non-1:1 regions. His 38 M (GG-09) is the figure that compares with the measured SNV total; 205 M does not.

### Critics' arguments the measurement tests

- **McCarthy MC-11 and Neukamm (via Nesslig20, Peaceful Science 18094 post 1: "one InDel can affect many base-pairs, ranging from 10s to 10s of thousands or even 100s of thousands of bp"):** confirmed by the size spectrum in §5 (largest 25.2 Mb; 71 events over 1 Mb). Neukamm's quote is not in `quotes-critics.md`.
- **Fun-Friendship4898 (Reddit 1wv4zeg, pdbyv0a):** "Within any given SDR, the true nucleotide difference might be tiny, like a 1-Mb inversion is a single mutational event. Or the difference might be undefined because orthology cannot be established. Or maybe a good chunk of those 35 million SNVs are already contained within those SDRs." Supported: SNVs inside nested fills are 2.75 M, counted twice in the first published 523 M row (corrected to 521 M), and 85% of the unaligned human sequence outside the net fills is centromere model, an independent route to the comment pdebkr5 point ("over half of these human SDRs are classified as centromere and acrocentric"). Not in `quotes-critics.md`; verified in `sources/raw/critics/arctic-tree-1wv4zeg.json`.
- **Hancock GG-10:** above.

### What the critics conceded already, and what stands

The critics already stated that the base pairs exist and are structural (MC-11, RE-05: "bases affected by a rearrangement are not separate mutation events: one structural change can affect millions of bases"); the check confirms rather than adds a point to Day on the existence of the bp. The lineage symmetry was never disputed (A3d: Hancock's factor of two is on the achievable side and cancels; justatest90, RF-11). For the ledger:

- **Gains for the critics' side:** the unit argument (9.7x raw, 7-14x in the bracket); the 40 M used in A3x holds (42.1 M); critic estimates by the neutral-supply route land within 0-19% of the measurement.
- **Not a win for the critics:** the SNV total (37.8 M) is above CSAC's 35 M; the 9.7 M rate route is half the measurement; polymorphism and the non-T2T repeat undercount cut in opposite directions; the neutral fraction is untested.
- **Gains for Day:** see "What survives for Day" (§0).

### Attribution of errors, both sides

- **CSAC 2005:** "~5 million events in each species" is ambiguous in its own text; the measurement resolves it as a total.
- **The audit's own R4-GAPS:** the per-species reading produced the 22.5 M upper bound per lineage (17.5 M + 5 M), which this measurement retires. No critic in `quotes-critics.md` read the 5 M per species.
- **A3x:** adds "1,140 inversions" to the human-chimp total; 1,140 is Yoo's six-ape curated count (A3x1); the human-chimp net has 453 nested inversion fills >=10 kb. Effect on the 40 M: none.
- **Critic slips on this thread (already noted in `quotes-critics.md`):** RF-6 McCarthy "400 billion x 1/20000 = 35 million" (the arithmetic gives 20 M); MF-03 Mansfield (1 neutral fixation per generation gives about 450,000, not 20 M); PS-01 Nesslig20 (75 is a per-diploid-offspring count); GG-11 Hancock 407 per generation is arithmetic on Day's number, not an event count.
- **Offsetting components:** the 42.1 M vs A3x's 40.0 M agreement combines SNV +8% and indel -14%; neither component alone is within 5%.
- **Day:** 04-28 ¶18 / 05-13 ¶5-¶7 wording above; A3a's 35 M + 187 + 1,140 does not sum to 410 M.

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
# post hoc (first pass)
research/.venv/bin/python -I research/checks/gap07b_posthoc_blocks.py --chain $D/pan/hg38.panTro6.all.chain.gz --work $D/work/ev ... --out $R/gap07b_posthoc_blocks.json
research/.venv/bin/python -I research/checks/gap07b_posthoc_polarize.py --ev $D/work/ev --gor $D/work/gor --out $R/gap07b_posthoc_polarize.json
research/.venv/bin/python -I research/checks/gap07b_posthoc_ladder.py $R
# post hoc (review-fix pass)
research/.venv/bin/python -I research/checks/gap07b_posthoc_review.py arith --raw $R --ev $D/work/ev --out $R/gap07b_posthoc_review_arith.json
research/.venv/bin/python -I research/checks/gap07b_posthoc_review.py nested --net $D/pan/hg38.panTro6.net.gz --axt $D/pan/hg38.panTro6.net.axt.gz --out $R/gap07b_posthoc_review_nested.json
research/.venv/bin/python -I research/checks/gap07b_posthoc_review2.py $R
```

Output files: `gap07b_report.out`, `gap07b_posthoc_{blocks,polarize,ladder}.out`, `gap07b_posthoc_review_arith.out`, `gap07b_posthoc_review_nested.out`, `gap07b_posthoc_review2.out`.

## 13. Suggested claim-file edits (for the lead; not applied)

Vocabulary: internal `holds | arithmetic-error`; fidelity `accurate | partial | misread`; external `supported | contested | contradicted`.

- **A3x** (bp vs events): external `supported` (keep). Comment: measured 42.1 M events (hg38 vs panTro6, non-T2T; both lineages plus polymorphism), 21.05 M per lineage; 205 M is 9.7x raw, bracket about 7-14x (Day-favourable 7.2-9.5 from repeat-unit and slippage sensitivities; critic-favourable 10.1-13.4 from human-lineage, top-level-fill, <2% and polymorphism corrections). Fidelity: suggest `partial` (the critics' reading matches Day's 2nd-edition wording "base pairs" but not his stated weighting rationale, Q99, Q101-Q103). Replace "Day has not, in the corpus, defended counting bp as separate fixations" with Day's weighting rationale (Q99, Q101-Q103) and the numerical test (about 3,250 SNV-equivalents per event above 50 bp). The "Pre-registered prediction 40 M +/- 30%" is met by 42.1 M on the available (non-T2T) alignment, not on Yoo's data. Replace "1,140 inversions" in the sum by the human-chimp net count (453 at >=10 kb) or drop it; retire the "(22.5M upper bound)" in the Check block; note CSAC "5 M in each species" resolved as a total (4.30 M measured).
- **A3a** (205M headline): internal `arithmetic-error` (keep); fidelity `misread` (keep). External: suggest `contradicted` for the reading "205 M required fixations = events" (9.7x raw, 7-14x bracket); comment that the base-pair magnitude of non-1:1 sequence is of the same order (201-523 M, assembly dependent, includes 59.5 Mb centromere models and aligned nested sequence) and that Day's stated weighting reading (Q99, Q101-Q103) is untested and needs about 3,250 SNV-equivalents per large event. If the lead prefers to keep a single hedged word, `contested` with that comment is the alternative.
- **A3b** (SNV-only): internal `holds`; fidelity `partial`; external suggest `supported`. Comment: 17.5 M is 83% of measured events per lineage and brackets the polymorphism-corrected fixed events (16.4-18.1 M); the two omissions (indels, about 10-12%; polymorphism, 14-22% of SNV differences) roughly cancel; the SNV-only shortfall rises to about 99,000 on the measured SNV/2 and 110,000 on measured events (86,000-95,000 with the polymorphism correction), all at G_f 1,322 (branches A2, A5 untouched). Do not write "the SNV-only figure is a floor" or "leaves about 20% of events out".
- **A3** (30M then 20M): internal `holds`; fidelity `partial`; external `contested` (keep): the 20 M per-lineage magnitude is corroborated by the event count (19.7-21.1 M raw; 16.4-18.1 M fixed), but the polymorphism share and the T2T question remain.
- **A3c:** add the measured polymorphism-corrected bracket and the statement that the 14-22% is an SNV estimate (indel/SV share unmeasured; Day Q100 says SVs are post-divergence). Propose GAP-07c (population-frequency intersection).
- **A3d:** the lineage split is 48.6 / 51.4 (SNV); support for "apportion symmetrically" comes from the SNV split, not from indels.
- **gaps.md GAP-07:** replace the "~20x rate-based / ~10x observed" line by the direct count; record that the k = mu route is about 2x below the measurement.

## 14. Review resolution

Finding ids: `Corr-M1..M3`, `Corr-m1..m10` (correctness review); `Day-1..Day-10`; `Crit-1..Crit-12`. Status: applied / partly applied / declined (with reason).

### Correctness review

| id | status | resolution |
|---|---|---|
| Corr-M1 | applied | §7: the 100 bp blindness and its cause stated; indel lineage claims restricted to <=50 bp (97.4% of events); >50 bp reported as unresolved with both rules; impact bounded (0.1%, worst case 0.27% of per-lineage events) |
| Corr-M2 | applied | §7: per-lineage figures recomputed with the stated symmetric rule for w = 2/5/10/20 and both size variants; 19.9 / 22.1 M withdrawn |
| Corr-M3 | applied | §8: F1 is event-level (327.1 Mb span, 40-45 Mb N, about 12%); one-sided flags stated; constant 80.0 Mb term (41% of F3) stated; "stays" removed; masked rows called a unique-sequence bound |
| Corr-m1 | applied | "~20% -> ~10-12%" fixed everywhere (§0, §11 text, §13); the A3b edit now says so |
| Corr-m2 | applied | headline uses the main-run 42,102,514; the 42,108,545 post hoc ladder number is disclosed as a different construction (§6) |
| Corr-m3 | applied | all post hoc numbers tagged [PH] in §0, §2, §4; the 2% threshold stated as chosen after the CSAC miss |
| Corr-m4 | applied | two omitted sub-predictions added to §2 (P6 polarizable fraction; P8 chimp share) |
| Corr-m5 | applied | §1: smoke-test ordering stated as unverifiable from git; "near 10" noted as loose (9.2-17.0) in §2 |
| Corr-m6 | applied | "extra human / extra chimp bases" replaces "per species/human-only" throughout |
| Corr-m7 | applied | §5: double-representation quantified (0.05%, about 1,000 events) |
| Corr-m8 | applied | §6: syn nested fills separated (491 M without syn) and SNV double count removed (521 M); original 523 M labelled as first published |
| Corr-m9 | partly applied | qDup SNV overcount added to the direction table and §0; not quantified (needs a record-level qDup join); top-level-fill SNV count (35.02 M) reported as a partial bound |
| Corr-m10 | applied | §7 wording: "mechanically correct, symmetric to first order; accuracy not measured"; "chimp branch is longer" marked as a reading |

### Steelman-Day review

| id | status | resolution |
|---|---|---|
| Day-1 | applied | Day's rationale verified in `sources/raw/day` (04-28 ¶18, ¶19, ¶25, ¶5; 05-13 ¶4-¶6) and added as Q97-Q103 in `quotes-day.md`; §11 reframes Day's position as a weighting claim with a range and tests it (3,250 SNV-equivalents per large event; G_f counts events, MITTENS 3.0 lines 88-94 and s7.3); §13 supersedes A3x's "Day has not defended" |
| Day-2 | applied | §6: repeat-unit table (171, 32, 6, 2, 1 bp; non-aligned and +nested) and weight figure; recomputed by script (`gap07b_posthoc_review_arith.out`); cited in §0. Added-event counts differ slightly from the review's table because the script uses the whole genome pair |
| Day-3 | applied | "hg38 vs panTro6 (non-T2T)" label on every headline; ratio reported as a bracket; A3x/A3a edits say "available alignment, not Yoo's data"; T2T re-run named as the follow-up, not run |
| Day-4 | applied | §0 "What survives for Day" box (83-90%, shortfall rising to 99,100 / 110,400, bp magnitude with the 523 M and 261 M caveats, first-edition 40 M, symmetric split) |
| Day-5 | applied | §2 last paragraph reworded; a "bears on" column added; Day's actual prediction (bp of the order of 410 M) scored as met in a qualified way. The pre-registered docstring is unchanged (cannot be) |
| Day-6 | applied | §0/§4: fixed share applied to SNVs only (11.1-12.1) and to all events (11.3-12.5), stated separately with the assumption; the confusing docstring sentence is left as registered and the sign is stated in §0 and §4 |
| Day-7 | applied | direction-of-each-artefact table in §0 (net-length slippage x2 8.84, x3 8.09; both-sided gaps; nested handling; >2% SNVs) |
| Day-8 | applied | §0 and §11: first-edition 40 M quoted (Q97, Q75), 42.1 M measured; "10x increase" is in bp |
| Day-9 | applied | §6 coincidence paragraph names both matches (410.09 Mb sum and the 187.0 Mb term) and adds a base rate (3 of 3,458 subsets, about 3 expected) |
| Day-10 | applied | "events are not fixations" placed beside the headline; ladder range reported with 410 M / bp in §0 box and §6; §13 wording "42.1 M events (hg38 vs panTro6; both lineages plus polymorphism), 21.05 M per lineage" |

### Steelman-critic review

| id | status | resolution |
|---|---|---|
| Crit-1 | applied | §0 bracket table: raw 9.74, human lineage 10.11, <2% 10.76, fixed 11.1-12.5, combined 12.3-13.4 (non-additive), with the SNV-only application of the polymorphism fraction stated; §13 text "about 10x raw, 11-14x" replaced by "7-14x bracket" because the Day-side adjustments are included |
| Crit-2 | applied | §0, §11, §13: "SNV-only is a floor" removed; fixed events 16.4-18.1 M bracket 17.5 M; omissions roughly cancel |
| Crit-3 | applied | §0 and §6 relabelled "bases in non-1:1 or non-aligned regions (alignment-defined, not necessarily differing)"; "bases that differ" row (201 M) added; nested identity (divergence 2.09% vs 1.31%) and SNV overlap (2.75 M) reported; "Yoo reproduced" sentence removed |
| Crit-4 | applied | §11 retitled "Where the result leaves each side"; credits for MC-11/RE-05 facts removed; the symmetric split is not presented as a Day win |
| Crit-5 | applied | §11 critic scoreboard (McCarthy, Mansfield, Nesslig20, Hancock, Dumb-and-Dumber); "rate-based 9-11x" corrected; k = mu route about 2x low stated; labelled consistency, not a test of k = mu |
| Crit-6 | applied | §11 attribution of errors: CSAC ambiguity; audit's retired 22.5 M; A3x 1,140 vs 453; critic slips RF-6, MF-03, PS-01, GG-11; offsetting SNV +8% / indel -14% |
| Crit-7 | partly applied | reason pre-split/within-species polymorphic sites are not post-split fixations stated (§4); applying 0.78-0.86 to indels stated as an assumption; the population-frequency intersection (GAP-07c) proposed, not run (needs a new data set, out of scope for this pass) |
| Crit-8 | applied | gap-merge (1/10/50), MNV-merged rows computed and shown; both-sided gaps (0.1% of events, 95 Mb of clean bp) stated in §0 table and §6 |
| Crit-9 | applied | §11 scoping table unit / type / rate with "do not multiply" |
| Crit-10 | applied | base rate for the 410.09 Mb coincidence computed by script; A3a's 412.1 cross-referenced |
| Crit-11 | applied | "bp per event is 10" attribution corrected (the 10.25 is the audit's A3x ratio); informal figures labelled by owner (Mansfield uncited; 40 M and 22.5 M are the audit's reconstructions); size spectrum cited against MC-11 and Neukamm |
| Crit-12 | partly applied | FF4898 centromere/acrocentric credit and Hancock GG-10 added in §11; the one-line direction summary of the misses added to §2; Neukamm and FF4898 quotes are verbatim from `sources/raw/critics` and are not in `quotes-critics.md` (not edited here; lead to add) |

Commit hashes: `gap07b_posthoc_review.py` 3798b92 and `gap07b_posthoc_review2.py` fbbc580 (both committed before they were run); the fix-pass outputs, this note and the Q97-Q103 quotes are in the commit that follows them (see `git log`).
