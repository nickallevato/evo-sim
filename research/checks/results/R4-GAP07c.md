# R4 GAP-07c: how much of the human-chimp difference is still polymorphic in humans? A direct measurement

Date: 2026-10-09. THROWAWAY research check, not product code. Follows `R4-GAP07b-alignment.md` (hg38 vs panTro6, 37.77 M SNV columns, 4.30 M indel events, 21.05 M events per lineage, 205 M / 21.05 M = 9.74). Answers GAP-07b review items Day-6 (the 0.78-0.86 fixed share was an SNV estimate applied to everything) and Crit-7 (the population-frequency intersection was proposed, not run).

**Tag used throughout:** **[PH]** = post hoc. Untagged numbers are from the pre-registered script's main run. Figure: `R4-GAP07c-polymorphic-share.png`.

## 0. Headline

**Measured (human lineage only).** Of the divergent SNV sites that gorilla polarization marks as human-derived, **15.6%** (autosomes, strict mask; 14.9% over all sites) still have the chimp-matching allele at 1% or more in the 1000 Genomes phase-3 panel, so they are not fixed in humans. The per-chromosome range is 14.8-16.7%. The same figure from the independent NYGC 30x panel on chr21+22 is 16.06% against 16.11% from phase 3 on the same chromosomes. At chimp-derived sites the human panel shows 1.0%, and over all sites pooled it shows 8.2%.

**The chimp lineage is NOT measured.** No chimpanzee population data were used. The "symmetric" treatment assumes the chimp lineage has the same polymorphic share as the human lineage. This is an assumption and the corrected ratio depends on it.

| treatment of the chimp lineage | s (SNV) | fixed events per lineage | 205 M / fixed |
|---|---|---|---|
| raw count (GAP-07b) | 0 | 21.05 M | **9.74** |
| (a) human data only: pooled share, chimp lineage credited with no polymorphism of its own (Day-favourable bound) | 8.2% | 19.27 M | **10.64** |
| **(b) symmetric (central):** chimp share := human-lineage share 15.6%; indel share 10.6% (measured, net of null) | 15.6% | **17.88 M** | **11.47** |
| (b) SNV only, indels counted fixed | 15.6% | 18.11 M | 11.32 |
| (b) at AF >= 0.1% / >= 5% | 17.3% / 13.7% | 17.55 / 18.24 M | 11.68 / 11.24 |
| (c) chimp share 2x human (arbitrary sensitivity) | 23.4% | 16.29 M | 12.58 |
| (b) on top-level fills only [PH] | 15.7% | 16.70 M | 12.27 |

**Bottom line.** The CSAC range (14-22%) is confirmed for the human lineage at AF >= 1%, at the low end (15.6%). Under the symmetric reading the ratio rises from 9.7 to about 11.5 (range 10.6-12.6 over the treatments, 11.2-11.7 over thresholds). The order of magnitude does not move. Indels and SVs are less polymorphic than SNVs (human-lineage indels 9.5%, SVs at or above 50 bp about 1.7%), which supports Day's "post-divergence" remark for SVs and makes GAP-07b's "same share for all events" row slightly too generous to the critics (by about 0.1 in ratio). Day's SNV-only 17.5 M per lineage is within 2% of the symmetric measured fixed events (17.88 M).

## 1. Method and pre-registration

- **Script:** `research/checks/gap07c_polymorphic_share.py`, committed as **078850b** before any allele frequency was computed. `git diff 078850b` for that file is empty (md5 c5211f89...). Predictions Q0-Q10, definitions and the Day-vs-critics criteria are in its docstring. Disclosure there: only VCF headers, five-line previews and file sizes were seen before registering.
- **Stages:** `sites` (local; SNV and indel site lists from GAP-07b's axtNet, gorilla work files and chain events; reproduces 37,767,396 SNVs and 4,301,652 indel events exactly, Q0 held); `afq` (workhorse; streams a VCF, joins to the site lists); `report` (local).
- **Post hoc:** `gap07c_posthoc_toplevel.py` (committed before it was run) and `gap07c_figure.py` (presentation only). See §8.
- **Resource choice.** Primary: 1000 Genomes phase-3 integrated biallelic SNV+INDEL set on GRCh38, sites-only VCF (0.98 GB; 2,548 samples; AC/AN; md5 equals the project manifest) with the project's GRCh38 strict accessibility mask (128 MB). It is the smallest public set with per-site AC/AN on GRCh38 and a matching mask. The NYGC 30x panel (3,202 samples, SNV+indel+SV in one file, about 28 GB because only genotype columns are bulky; no sites-only copy) was fetched for **chr21 and chr22 only** (0.87 GB; the server gave 0.2-0.8 MB/s) as a cross-check and an SV sample. gnomAD v4 genome sites (hundreds of GB) were not used. Phase 3 has no chrY, and its chrX has only 107 k records, so **chrX and chrY are excluded from the shares**; the autosomal shares are applied to all 37.77 M SNVs (X is 4% and Y 2% of the sites).
- **Data handling.** Downloads on `na-workhorse` only (`sources/raw/1kg-*`), never executed, read through `gzip -dc` and Python parsing, one process at a time (two for the NYGC pair). Host and md5s: `results/raw/gap07c.host`. GAP-07b's site lists were derived locally and rsynced; only derived outputs came back.

### Definitions that matter

- A difference is **fixed in humans** if the allele equal to the chimp base has frequency < 1% in the panel (`p_chimp`, AC/AN of the VCF record whose ALT equals the chimp base; 0 if no record), and **polymorphic** if >= 1%. Sites absent from the VCF count as fixed; this is why the share is measured inside the strict mask (central) and over all sites (floor).
- **Polarization** is GAP-07b's: gorilla base = chimp base means human-derived (H), = hg38 base means chimp-derived (C).
- **Indels** are the 4.30 M chain-gap events matched to a VCF indel record of the same net length within +-w bp (w = 0, 2, 5), with a null control at +-10 kb shifts. SVs >= 50 bp (NYGC chr21+22 only): deletion records with reciprocal overlap >= 50%, insertion records within 100 bp.

## 2. Scorecard against the pre-registered predictions

| # | prediction | observed | verdict |
|---|---|---|---|
| Q0 | 37,767,396 SNVs and 4,301,652 indel events reproduced | both exact | **held** |
| Q1 | s_H (human-derived, in mask, p_chimp >= 1%) 15% (10-21%) | **15.59%** (all sites 14.86%) | **held** (point on target) |
| Q2 | pooled share over all SNV sites 8% (5-12%) | **8.25%** in mask; 7.79% all sites | **held** |
| Q3 | s_C (chimp-derived) 1.5% (0.5-4%); s_H/s_C >= 3 | **0.99%**; ratio 15.8 | **held** (low end) |
| Q4 | all-sites share 0-4 points below in-mask | 0.7 points (H); 0.5 (pooled) | **held** |
| Q5 | adding "seen at all" raises s_H by <= 3 points | **+4.4 points** (20.0% seen vs 15.6%) | **missed** |
| Q6 | NYGC chr21+22 s_H within +-3 points of phase 3; per-chromosome spread within +-4 | 16.06% vs 16.11%; 14.8-16.7% | **held** |
| Q7 | >= 99% of matched records have REF = hg38 base | 4,925,478 of 4,925,478 (100%) | **held** |
| Q8 | human-lineage indel net share 4-12% (point 7%); > 50 bp <= 10% (point 4%) | **9.5%** (10.6% in mask), above the point; > 50 bp **1.7%** (net 1.2%), n = 4,623 | **held** (both inside the bands; indel point missed high, SV point missed low) |
| Q9 | (b) 18.1 M (17.0-19.6), ratio 11.3 (10.5-12.1); (a) 19.3 M, 10.6 (10.3-11.1); (c) 15.2 M (13.0-17.5), 13.5 (11.7-15.8) | (b) 17.88 M, 11.47; (a) 19.27 M, 10.64; (c) 16.29 M, 12.58 | **held** (all inside their bands; (c) point missed, ratio 12.6 vs 13.5) |
| Q10 | Day's 17.5 M inside the (a)-(c) range of fixed events | 16.29-19.27 M contains 17.5 M | **held** |

Pre-registered criteria. "Favours Day": s_H <= 8% (symmetric ratio <= 10.3) or near-zero indel/SV shares. "Favours critics": s_H >= 14% (symmetric ratio >= 11.3) with an indel share like the SNV share. Outcome: **s_H and the symmetric ratio sit on the critics' side of the SNV criterion (15.6%, 11.5)**, while the indel and SV shares sit on Day's side (9.5% and 1.7% against 15.6%). The "surprise" triggers (ratio < 8 or > 15, s_H > 30%) did not fire.

## 3. SNVs: frequency bands

Autosomes, strict mask, % of sites by frequency of the chimp-matching allele in humans (`raw/gap07c_report.out`):

| group | n | not seen | (0, 0.1%) | [0.1%, 1%) | [1%, 10%) | [10%, 50%) | [50%, 90%) | [90%, 99%) | >= 99% | **>= 1%** |
|---|---|---|---|---|---|---|---|---|---|---|
| all sites, in mask | 26.27 M | 87.5 | 2.9 | 1.4 | 1.8 | 3.0 | 2.6 | 0.7 | 0.2 | **8.25** |
| human-derived, in mask | 12.67 M | 80.0 | 2.7 | 1.7 | 3.0 | 5.6 | 5.2 | 1.3 | 0.4 | **15.59** |
| chimp-derived, in mask | 12.79 M | 94.9 | 3.1 | 1.0 | 0.5 | 0.3 | 0.1 | 0.0 | 0.0 | **0.99** |

- **Thresholds on s_H:** 0.1% 17.3%; 0.5% 16.2%; 1% 15.6%; 2% 14.9%; 5% 13.7%; 10% 12.6%. Seen at all: 20.0%. The share depends mildly on the threshold and, for lower thresholds, on panel size (2,548 samples).
- **Where the polymorphic sites sit.** Most are common: 5.6% + 5.2% of human-derived sites have the chimp allele at 10-90%. The >= 99% band (0.4%) is hg38's own rare alleles. Sanity check: 15.59% of 12.67 M is about 1.98 M sites; the panel holds 9.26 M common (>= 1%) SNVs in the mask, of which hg38 would carry the derived allele with probability near its mean derived frequency (about 0.2), which gives roughly the same number.
- **Subsets of H-derived sites (in mask):** CpG 15.9% vs non-CpG 15.5%; transitions 15.6% vs transversions 15.6%; lowercase (repeat) 15.6% vs not 15.6%; near a gap 11.8% (n = 195 k). The share is almost uniform across these cuts, so masking or repeat filters do not change it. Nested-fill SNVs (2.29 M of 35.47 M) are slightly less polymorphic (12.8% vs 15.7% for top-level) [PH].
- **Why the pooled share is half the human-lineage share.** Of the 37.77 M divergent SNVs about half are chimp-derived; the human panel says little about whether those are fixed in chimps (it shows only shared or recurrent variation, 1.0%). The 8.2% is therefore the human data's *lower bound* on the total polymorphic share and the 15.6% is its measurement on the half it can address. CSAC's 14-22% is a both-species estimate; the measurement supports its human half and is compatible with it as a total only through the symmetric assumption.
- **Ancestral polymorphism that sorted** (reciprocal fixation after the split) is not polymorphic now and stays in the fixed count, as Day argues (04-28 para 24).

## 4. Indels and SVs

Net of the shifted-position null (null rate 0.01-0.08%; the matches are real), share with a matched record at AF >= 1%, w = 2:

| events | n | share |
|---|---|---|
| all chain-gap events (autosomes) | 4.05 M | 4.1% (5.3% in mask) |
| human-lineage polarized | 1.16 M | **9.5%** (10.6% in mask) |
| chimp-lineage polarized | 2.35 M | 1.8% |
| human lineage, 1 bp / 2-10 bp / 11-50 bp | 0.54 / 0.54 / 0.07 M (in mask) | 11.7% / 7.9% / 6.0% |
| SVs >= 50 bp, NYGC chr21+22 (all / human-only / chimp-only / both-sided) | 4,623 / 1,624 / 1,959 / 1,040 | **1.7% / 2.7% / 1.6% / 0.5%** (null 0.05%) |
| phase-3 same chromosomes, 51-1000 bp / > 1 kb | 3,753 / 816 | 0.03% / 0% (phase 3 has few indels > 50 bp) |

- Applying the size-stratified human-lineage shares to the size mix gives a pooled indel share of 9.1% [PH, by hand]; the central row uses 10.6%. The difference changes the ratio by 0.02.
- The pattern matches the SNV one: polymorphic where the human-derived allele is the hg38 one (9.5% against 1.8%), and falls with size.
- **Day's Q100 ("SVs are, with very few exceptions, post-divergence") is supported** in the sense that only 1.7% of divergent SV events >= 50 bp match a human polymorphic SV, against 15.6% of SNVs. The sample is two chromosomes, the SV call set is from short reads, and non-matches in repeat-rich sequence (where most gap bp lie) count as "fixed". So 1.7% is a lower bound, not a measurement of fixation.
- The 1,000 Genomes indel and SV matching compares net length and position, not sequence. Matches inside tandem repeats may pair different events.

## 5. Corrected ratio: what changed against GAP-07b

| GAP-07b row (assumed CSAC share) | ratio then | measured counterpart now |
|---|---|---|
| fixed share 0.86 / 0.78 on SNVs only | 11.14 / 12.13 | 0.844 (human lineage, measured), **11.32** |
| same share on all events | 11.32 / 12.48 | share on all events (SNV 15.6%, indel 15.6%) **11.54**; with the measured indel share (10.6%) **11.47** |
| Day-favourable "no polymorphism removed" | 9.74 | 9.74 stays the floor; (a) 10.64 |
| top-level fills only, with the CSAC share | not given | **12.27** [PH] |
| human lineage alone, with measured shares | 10.11 (raw) | about 11.9 [PH, by hand: 15.52 M + 1.68 M fixed] |

- At the MITTENS rate (1,322 generations per fixation) the GAP-07b shortfall of 91,800 on 17.5 M scales to about 93,800 on 17.88 M (derived by proportion; 110,400 on the raw 21.05 M). The rate side is outside this check.
- Day's 17.5 M per lineage (35 M / 2, polymorphism included, SNV only) is 2% below the measured symmetric fixed events 17.88 M. This is a near-coincidence of two offsetting errors (omitted indels, included polymorphism), as GAP-07b already said, now measured. With SNV only fixed events are 15.94 M.

## 6. Who this helps

**Critics (on the polymorphism point).**
- The polymorphism correction is real and of the size CSAC gave: 15.6% of human-derived differences are still segregating at AF >= 1% (17.3% at 0.1%, 20% seen at all). Nesslig20 (PS-03) and Camestros (CA-04) were right that the reference-genome differences include differences that are not fixed in the human population. GAP-07b's critic-favourable rows (11.1-12.5) were about right, and 11.3-11.7 is the central measured range.
- The 14-22% is a human-lineage fact here, in a modern, large panel, on the native GRCh38 data. The resource choice is not driving it (NYGC 16.06% vs phase 3 16.11%).

**Day.**
- The polymorphic share is smaller than a reading of "most of the differences" would need: 84% of human-derived SNVs are fixed in humans at AF >= 1%. The ratio moves from 9.7 to about 11.5, not to 100.
- His distinction holds: SVs and indels are less polymorphic than SNVs (SVs >= 50 bp 1.7%; indels 9.5% on the human lineage), so the CSAC SNV share should not be applied to them, and doing so (GAP-07b's critic row) over-corrects slightly.
- Without chimp data the 15.6% cannot be doubled by the human data alone. On the human data only, the pooled share is 8.2% and the ratio 10.6 (treatment (a)). The critic-side 11.5 depends on an assumption.
- His SNV-only 17.5 M per lineage is within 2% of the measured fixed events; its shortfall is not reduced by the correction (shortfall about 93,800 at the MITTENS rate, by proportion from GAP-07b).
- The sorted ancestral polymorphism remains a required fixation on his reading (04-28 para 24); this check does not subtract it.

**Neither.**
- **This check does not move the unit result.** The 205 M (bp) against about 18 M fixed events per lineage stays at 11-12, far from 1. Polymorphism is a 10-15% correction; the unit mismatch is the 10x.
- It does not test selection. A fixed difference is not a selected one (branches A5, B, G, H). Nothing here says how many of the ~18 M fixed events needed selection.
- No chimp data: treatment (b) is an assumption, and chimp diversity is commonly reported to be higher than human (not checked here; a reason for (c), not a measurement).

## 7. Caveats

1. **Chimp lineage unmeasured** (above). Great Ape Genome Project / de Manuel 2016 variation lives in older chimp assemblies and raw reads and needs a liftover and large downloads; not attempted. A chimp panel on panTro6 would settle (a) vs (b) vs (c).
2. **Chromosomes.** chrX (phase 3 has only 107 k X records; the NYGC X file is 2.5 GB, not fetched) and chrY (no panel) excluded; autosomal shares applied to 6% of the sites. Chimp-specific X/Y biology is not modelled.
3. **Biallelic panel, short reads, strict mask.** Multi-allelic sites are absent from phase 3 (NYGC chr21+22, which splits them, agrees to 0.05 points). Short-read calls under-represent repeats and SVs, so shares outside the mask (6.5% pooled vs 8.2% inside) and for SVs are lower bounds. Sites outside the VCF count as fixed.
4. **Panel size and frequency threshold.** The share at AF >= 1% is stable; at lower thresholds it grows with sample size (17.3% at 0.1%, 20% seen at all in 2,548 people). No threshold gives "polymorphic in the species" for the whole of humanity.
5. **hg38 is a mosaic reference.** Its private alleles (0.4% of human-derived sites, p_chimp >= 99%) count as polymorphic. Small.
6. **Alignment artefacts** (GAP-07b's) carry over: paralog/nested alignments, qDup, non-T2T assemblies. Nested-fill SNVs are slightly less polymorphic (12.8%), so their inclusion lowers the share a little.
7. **Allele and sequence identity for indels** is not compared (net length and position only); the null control gives 0.01-0.08% chance matches.
8. **Polarization.** Gorilla polarization labels ~96% of SNVs; the "third" (1.1%) and unpolarized (3.7%) are 6-9% polymorphic. Indel polarization is GAP-07b's (reliable <= 50 bp, human share skewed as run: 1.16 M vs 2.35 M events), so no per-lineage indel counts were made.
9. **Prediction record.** One miss (Q5, +4.4 points against <= 3); the SV point (4%) and the indel point (7%) were missed within their bands; the (c) point was missed within its band.

## 8. Post hoc

1. **Top-level flag fix [PH].** The main-run "top-level fills" flag (a level-1 range test) was true for every SNV because a level-1 fill's range contains its nested fills, so those two rows of `gap07c_report.out` equal the unrestricted rows. Found by seeing identical n. `gap07c_posthoc_toplevel.py` (committed before it was run) recomputes it: 33.18 M top-level and 2.29 M nested of 35.47 M autosomal SNVs (93.5%, as GAP-07b's 92.7%); top-level human-derived s = 15.69%, nested 12.75%. The top-level critic row (12.27) uses 35,017,058 top-level SNVs.
2. Hand-derived numbers in §5 (human lineage 11.9, size-stratified indel share, MITTENS scaling) are marked in place.
3. Figure script `gap07c_figure.py` is presentation only.
4. No AF-dependent change was made to the main script after the run.

## 9. Files

`research/checks/gap07c_polymorphic_share.py` (078850b), `gap07c_posthoc_toplevel.py`, `gap07c_figure.py`; `results/raw/gap07c.host`, `gap07c_report.{json,out}` (autosomes, phase 3), `gap07c_report_p3_chr21_22.*` and `gap07c_report_nygc_chr21_22.*` (cross-check), `gap07c_posthoc_toplevel.json`, `gap07c_baseline_*.json` (all-VCF SNV counts by AF band, in and out of the mask), `gap07c_afq_*.out`, `gap07c_sites*.{out,json}`; `results/R4-GAP07c-polymorphic-share.png`. Site lists and AF arrays are in gitignored `sources/raw/gap07c-*`.

Not edited (lead to integrate): claim files (A3c, A3x, A3a), `ledgers/gaps.md` GAP-07, the argmap, README, RESULTS.md, REVIEW.md. Suggested A3c line: "R4 GAP-07c: 15.6% of human-derived divergent SNVs have the chimp allele at >= 1% in 1000 Genomes (14.8-16.7% per chromosome; NYGC 16.06% vs phase 3 16.11% on chr21+22); chimp side not measured; SVs >= 50 bp 1.7% (n = 4,623, chr21+22)."
