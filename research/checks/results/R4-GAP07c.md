# R4 GAP-07c: how much of the human-chimp difference is still polymorphic in humans? A direct measurement

Date: 2026-10-09. Revised 2026-10-09 after two reviews (`REVIEW-R4-GAP07c-correctness.md`, `REVIEW-R4-GAP07c-steelman.md`; Day-side and critic-side in one file); see §10 "Review resolution". THROWAWAY research check, not product code. Follows `R4-GAP07b-alignment.md` (hg38 vs panTro6, 37.77 M SNV columns, 4.30 M indel events, 21.05 M events per lineage, 205 M / 21.05 M = 9.74). Answers GAP-07b review items Day-6 (the 0.78-0.86 fixed share was an SNV estimate applied to everything) and Crit-7 (the population-frequency intersection was proposed, not run).

**Tag used throughout:** **[PH]** = post hoc (computed or chosen after the main run; numbers marked [PH] come from `gap07c_posthoc_toplevel.py` or `gap07c_posthoc_review.py`, both committed before they were run). Untagged numbers are from the pre-registered script's main run. Figure: `R4-GAP07c-polymorphic-share.png`.

## 0. Headline

**Definition of "fixed".** A divergent SNV is *fixed in humans* if the allele equal to the chimp base has a frequency below 1% in the human panel (so the hg38 allele is at 99% or more), and *polymorphic* if that allele is at 1% or more. It is not a statement about the ancestor (§6).

**Measured (human lineage only).** Of the divergent SNV sites that gorilla polarization marks as human-derived, **84.4% are fixed in humans and 15.6% are not** (autosomes, strict mask; 14.9% not fixed over all sites). The per-chromosome range is 14.8-16.7%. The NYGC 30x call set (same people, independent calling pipeline) gives 16.06% against 16.11% from phase 3 on chr21+22. At chimp-derived sites the human panel shows 1.0%; pooled over all sites 8.25%. Indels and SVs are less polymorphic than SNVs in the same panel (§4), but not by the factor the first version of this note gave.

**The chimp lineage is NOT measured.** No chimpanzee population data were used. Rows marked "chimp assumed" below assume a chimp-lineage share; rows marked "human data only" do not. The corrected ratio depends on this assumption, and nothing in this check says which direction the true chimp share lies (§7, caveat 1).

### The bracket (205 M / fixed events per lineage) [PH]

Fixed events per lineage = (SNVs x (1 - s_snv) + indel events x (1 - s_ind) + 33,466 other events) / 2. The last column also corrects the SNV part of Day's own numerator by the same SNV share (205 M = 17.5 M SNV + 187.5 M structural bp; numerator 205 - 17.5 x s_snv; Day-2).

| row | basis | s_snv | s_ind | fixed per lineage | **205 M / fixed** | numerator corrected |
|---|---|---|---|---|---|---|
| raw count (GAP-07b) | none | 0 | 0 | 21.05 M | **9.74** | 9.74 |
| (a) pooled share, pooled indel share, in mask | **human data only** (chimp credited with nothing) | 8.25% | 5.28% | 19.38 M | **10.58** | 10.50 |
| **human lineage alone**, check's own conventions | **human data only**; no chimp assumption | 15.59% | 10.12% | 17.22 M | **11.90** | 11.75 |
| chimp share 0.5x human | chimp assumed | 11.7% | 7.6% | 18.68 M | 10.97 | 10.87 |
| (b) chimp share = human share (AF >= 1%) | chimp assumed | 15.59% | 10.12% | 17.89 M | **11.46** | 11.31 |
| (b) with measured third/unpolarized shares | chimp assumed | 15.23% | 10.12% | 17.96 M | 11.42 | 11.27 |
| (b) at AF >= 10% (Day's operational "fixed" is above 90%, Q55) | chimp assumed | 12.57% | 8.15% | 18.50 M | **11.08** | 10.96 |
| (b) at AF >= 5% | chimp assumed | 13.69% | 8.90% | 18.27 M | 11.22 | 11.09 |
| (b) at AF >= 0.1% | chimp assumed | 17.33% | 11.14% | 17.54 M | 11.69 | 11.52 |
| (b) "seen at any frequency" | chimp assumed | 20.01% | 11.79% | 17.02 M | **12.05** | 11.84 |
| (b) top-level fills only (35,017,058 SNVs) | chimp assumed | 15.69% | 10.12% | 16.71 M | **12.27** | 12.10 |
| (c) chimp share 2x human | chimp assumed | 23.4% | 15.2% | 16.31 M | 12.57 | 12.32 |
| (c) as registered (2 x s_H on all events) | chimp assumed | 31.2% | 20.2% | 14.73 M | 13.92 | 13.55 |
| measured counterpart of GAP-07b's combined critic row (<2%-divergent records, SNV share only; indels unchanged) | chimp assumed | 15.70% | 0 | 16.40 M | 12.50 | 12.33 |
| same, with the measured indel share | chimp assumed | 15.70% | 10.12% | 16.18 M | 12.67 | 12.50 |
| *GAP-07b combined critic rows, for comparison (assumed CSAC share 0.86 / 0.78)* | assumed | 14% / 22% | 0 | 16.69 / 15.34 M | 12.29 / 13.37 | not applied |

- **Bracket: 10.6-12.6 over the corrections this check measures; 11.1-12.1 over the threshold (AF >= 10% to seen at any frequency); 12.3-12.7 on the critic-favourable cuts (top-level fills, <2% records).** The row that needs no chimp assumption, the human lineage alone, is 11.9 (11.75 with the numerator correction), the same events as GAP-07b's 20.28 M human-lineage count (10.11 raw).
- GAP-07b's Day-favourable rows (repeat-unit and slippage, 7.2-9.5) re-expressed with the symmetric correction (x1.18, hand scaling in the script) become 8.4-11.1. So the combined bracket of GAP-07b, "about 7 to 14", becomes **about 8 to 13**. All of these rows are post hoc.
- **Day's numerator** also contains polymorphism in its SNV part. Correcting it lowers each ratio by 0.1-0.4 (11.46 to 11.31 on (b)).

**Bottom line.** 84.4% of human-derived divergent SNVs are fixed in humans and 15.6% are not, a number consistent with the human half of CSAC's both-species "14-22%" (we measured one species; the other is assumed). Counting only what is fixed raises 205 M / events from 9.7 to about 11.5 (human lineage alone 11.9; 11.1-12.1 over thresholds; 10.6-12.6 over treatments); the order of magnitude does not move. SVs at or above 50 bp are less polymorphic than SNVs (6.8% net on the human lineage against 15.6%, about 2.3 times lower; pooled over both lineages 1.7%), which is consistent with Day's "post-divergence" remark but cannot test it (§4). Like for like, Day's SNV-only 17.5 M per lineage is **9.8% above** the measured fixed SNVs (15.94 M) and 2.2% below all fixed events (17.89 M); the near-match with the all-events figure is two offsetting errors (§5).

## 1. Method and pre-registration

- **Script:** `research/checks/gap07c_polymorphic_share.py`, committed as **078850b** before any allele frequency was computed. `git diff 078850b` for that file is empty (md5 c5211f89...). Predictions Q0-Q10, definitions and the Day-vs-critics criteria are in its docstring. Disclosure there: only VCF headers, five-line previews and file sizes were seen before registering.
- **Stages:** `sites` (local; SNV and indel site lists from GAP-07b's axtNet, gorilla work files and chain events; reproduces 37,767,396 SNVs and 4,301,652 indel events exactly, Q0 held); `afq` (workhorse; streams a VCF, joins to the site lists); `report` (local).
- **Post hoc:** `gap07c_posthoc_toplevel.py` (committed after the main run, before its own run); `gap07c_posthoc_review.py` (commit **ae42a91**, before its run; review fix pass; ran on the workhorse); `gap07c_figure.py` (presentation only). See §8.
- **Resource choice.** Primary: 1000 Genomes phase-3 integrated biallelic SNV+INDEL set on GRCh38, sites-only VCF (0.98 GB; 2,548 samples; AC/AN; md5 equals the project manifest) with the project's GRCh38 strict accessibility mask (128 MB). It is the smallest public set with per-site AC/AN on GRCh38 and a matching mask. The NYGC 30x panel (3,202 samples including the phase-3 individuals plus relatives, SNV+indel+SV in one file, about 28 GB because only genotype columns are bulky; no sites-only copy) was fetched for **chr21 and chr22 only** (0.87 GB; the server gave 0.2-0.8 MB/s) as a cross-check and an SV sample. Same people, different sequencing and calling pipeline: it tests the calling and resource choice, not the sampling of humans. gnomAD v4 genome sites (hundreds of GB) were not used. Phase 3 has no chrY, and its chrX has only 107 k records, so **chrX and chrY are excluded from the shares**; the autosomal shares are applied to all 37.77 M SNVs (X is 4% and Y 2% of the sites).
- **Data handling.** Downloads on `na-workhorse` only (`sources/raw/1kg-*`), never executed, read through `gzip -dc` and Python parsing. Host and md5s: `results/raw/gap07c.host`. GAP-07b's site lists were derived locally and rsynced; only derived outputs came back. The post hoc review stage ran on the workhorse after the first local attempt exhausted the workstation's memory.

### Definitions that matter

- `p_chimp` = AC/AN of the VCF record whose ALT equals the chimp base (0 if none). Sites absent from the VCF count as fixed; this is why the share is measured inside the strict mask (central) and over all sites (floor).
- **Polarization** (SNVs) is GAP-07b's: gorilla base = chimp base means human-derived (H), = hg38 base means chimp-derived (C). Its accuracy is not measured here (GAP-07b's caveat applies; the H/C split is near symmetric, 16.4 M vs 17.4 M, and the C-derived 1.0% is a usable sanity bound).
- **Indels** are the 4.30 M chain-gap events matched to a VCF indel record of the same net length within +-2 bp, net of a +-10 kb shifted null. **Lineage polarization of indels uses GAP-07b's symmetric post hoc rule** (`gap07b_posthoc_polarize.polar`, window 2/5/10/20, events up to 50 bp); the as-run rule in the main script (a copy of GAP-07b's pre-registered rule, which GAP-07b withdrew for per-lineage claims because it treats human-only and chimp-only gaps asymmetrically, human share of polarized 0.33) was replaced in the [PH] pass (§4).
- **SVs >= 50 bp** (NYGC chr21+22 only): deletion records with reciprocal overlap >= 50%, insertion records within 100 bp with SVLEN within 0.5-2x.

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
| Q8 | human-lineage indel net share 4-12% (point 7%); > 50 bp <= 10% (point 4%) | indel as run **9.5%** (10.6% in mask); with the symmetric rule [PH] **7.4-8.7%** (9.5-10.5% in mask). SV pooled 1.7%; **human lineage 6.8% net** (n = 450) | **held** (inside the bands; indel point missed high, SV point missed high on the human lineage and low on the pool) |
| Q9 | (b) 18.1 M (17.0-19.6), ratio 11.3 (10.5-12.1); (a) 19.3 M, 10.6 (10.3-11.1); (c) 15.2 M (13.0-17.5), 13.5 (11.7-15.8) | (b) 17.89 M, 11.46; (a) 19.27 M, 10.64 (main run; 19.38 M, 10.58 with the pooled indel share [PH]); (c) 16.31 M, 12.57 | **held** (all inside their bands). The (c) point is a registration slip, not a miss: the registered 15.2 M / 13.5 corresponds to 2 x s_H on all events (14.73 M / 13.9 [PH]); (c) as defined and coded is 1.5 x s_H. The registered (b) point 18.1 M / 11.3 equals the SNV-only row (18.11 M / 11.32), not the indel-inclusive central row. |
| Q10 | Day's 17.5 M inside the (a)-(c) range of fixed events | 16.31-19.27 M contains 17.5 M | **held** (all-events basket; like-for-like see §5) |

**Pre-registered criteria.** "Favours Day": s_H <= 8% (symmetric ratio <= 10.3) or near-zero indel/SV shares. "Favours critics": s_H >= 14% (symmetric ratio >= 11.3) with an indel share like the SNV share. Outcome: s_H and the symmetric ratio sit on the critics' side of the SNV criterion (15.6%, 11.5). The SV share meets "near zero" only in the pool (1.7%; on the human lineage it is 6.8%); the indel share is intermediate (7.4-10.5% against 14.9-15.6%). The surprise triggers (ratio < 8 or > 15, s_H > 30%) did not fire. The Q5 miss and the point misses are listed in §7.

## 3. SNVs: frequency bands

Autosomes, strict mask, % of sites by the **frequency in humans of the chimp-matching allele**. For human-derived sites this is the ancestral allele, so the derived (hg38) allele is at 99% or more in the first three columns and is the minority allele only in the 50-99% columns (`raw/gap07c_report.out`):

| group | n | not seen | (0, 0.1%) | [0.1%, 1%) | [1%, 10%) | [10%, 50%) | [50%, 90%) | [90%, 99%) | >= 99% | **>= 1%** |
|---|---|---|---|---|---|---|---|---|---|---|
| all sites, in mask | 26.27 M | 87.5 | 2.9 | 1.4 | 1.8 | 3.0 | 2.6 | 0.7 | 0.2 | **8.25** |
| human-derived, in mask | 12.67 M | 80.0 | 2.7 | 1.7 | 3.0 | 5.6 | 5.2 | 1.3 | 0.4 | **15.59** |
| chimp-derived, in mask | 12.79 M | 94.9 | 3.1 | 1.0 | 0.5 | 0.3 | 0.1 | 0.0 | 0.0 | **0.99** |

- **Thresholds on s_H:** 0.1% 17.3%; 0.5% 16.2%; 1% 15.6%; 2% 14.9%; 5% 13.7%; 10% 12.6%; seen at all 20.0%. The ratio effect is in the bracket above (11.1 at 10%, 12.05 at "seen").
- **Where the polymorphic sites sit.** Most are common: 5.6% + 5.2% of human-derived sites have the chimp allele at 10-90%, so the derived (hg38) allele is at 10-90%. The >= 99% band (0.4%) is hg38's own rare alleles. Sanity check: 15.59% of 12.67 M is about 1.98 M sites; the panel holds 9.26 M common (>= 1%) SNVs in the mask, of which hg38 carries the derived allele with probability near the mean derived frequency (about 0.2), which gives roughly the same number.
- **Subsets of H-derived sites (in mask):** CpG 15.9% vs non-CpG 15.5%; transitions 15.6% vs transversions 15.6%; lowercase (repeat) 15.6% vs not 15.6%; near a gap 11.8% (n = 195 k). Nested-fill SNVs (2.29 M of 35.47 M) are less polymorphic (12.8% vs 15.7% for top-level) [PH]. Third-state and unpolarized sites (1.81 M of 37.77 M): 6.3% and 8.6% [PH].
- **Why the pooled share is half the human-lineage share.** About half of the divergent SNVs are chimp-derived; the human panel says little about whether those are fixed in chimps (it shows only shared or recurrent variation, 1.0%). The 8.25% is the human data's lower bound on the total polymorphic share and the 15.6% is its measurement on the half it can address. CSAC's 14-22% is a both-species estimate; the measurement is consistent with its human half, and with it as a total only through the symmetric assumption.

## 4. Indels and SVs [PH]

**Indel polarization (Corr-M1).** With GAP-07b's symmetric rule (events up to 50 bp; net of the +-10 kb null; match w = 2; T = 1%), human-lineage share by polarization window:

| rule window | human-lineage events | human share of polarized | human-lineage share, all sites | in mask | chimp-lineage share (all / mask) |
|---|---|---|---|---|---|
| 2 | 1.39 M | 0.38 | 8.7% | 10.5% | 1.8% / 1.9% |
| 5 (central) | 1.56 M | 0.43 | 8.3% | 10.1% | 1.5% / 1.5% |
| 10 | 1.75 M | 0.48 | 7.9% | 9.7% | 1.2% / 1.2% |
| 20 | 1.91 M | 0.52 | 7.4% | 9.5% | 1.2% / 1.1% |
| as-run rule (withdrawn) | 1.16 M | 0.33 | 9.5% | 10.6% | 1.8% |

The human-lineage indel share is **7.4-8.7% (9.5-10.5% in mask)**, the central value for the ratio is 10.12% (w = 5, in mask), and the pooled share over all events (in mask) is 5.3%. By size (human lineage, in mask): 1 bp 12.0%, 2-10 bp 8.6%, 11-50 bp 6.9%. The polarization of events above 50 bp is unresolved in GAP-07b and is not used for indels; per-lineage indel counts rest on the symmetric rule only up to 50 bp and are not "reliable" beyond that.

**Chance matches (Corr-m6).** The +-10/+-20 kb shifted null gives 0.03-0.07%. Harder controls at the same position window (human lineage, all sites): sign-flipped net length 0.41-0.49% (size 1: 0.89%), net length +-1: 0.23-0.45%; chimp lineage: -d 0.69%, d+-1 0.25-0.28%. Positional chance matches therefore run at up to 0.5-0.9 points, about ten times the shifted null but still small against the observed 8-10%; the net shares above are overstated by at most that. Sequence content is not compared.

**SVs at or above 50 bp (NYGC chr21+22; Corr-M2).**

| events | n | polymorphic at AF >= 1% | 95% interval on the observed share |
|---|---|---|---|
| all (pooled over lineages) | 4,623 | 1.73% (net 1.68%) | 1.4-2.1% |
| **human lineage** (as-run polarization) | 450 | **6.89% (net 6.78%)** | 4.9-9.6% |
| chimp lineage | 2,305 | 1.17% (net 1.13%) | 0.8-1.7% |
| unpolarized | 1,868 | 1.18% (net 1.12%) | 0.8-1.8% |
| human lineage, 50-100 / 100-1000 / >= 1000 bp | 186 / 219 / 45 | 3.8% / 9.6% / 6.7% | wide |

- **Like for like**, SVs (human lineage) at 6.8% are about **2.3 times** less polymorphic than SNVs (15.6%), and close to the human-lineage indel share (7.4-10.5%). The first version of this note set the pooled 1.7% against the human-lineage 15.6% (a factor 9), which mixed denominators. Phase 3 has few indels above 50 bp (0.03% matched on the same chromosomes), so the NYGC set is the only SV evidence.
- **"Consistent with" Day's Q100, not "supports".** Day: "ILS cannot sort what was never segregating. Structural variation is, with very few exceptions, post-divergence" (04-28 ¶25). A panel of today's humans cannot test this: an ancestral SV that sorted looks fixed, as does a post-divergence one. Short-read SV and indel recall is lower than SNV recall and falls with size, so part or all of the lower share is detection; purifying selection on large indels does the same. Non-matches (repeats, multi-allelic STRs) count as fixed, so every indel and SV share here is a lower bound. A long-read SV set on the same events would separate these readings (follow-up, not run).
- Applying the SNV share to all events (GAP-07b's critic row) moves the ratio from 11.46 to 11.54 only; the indel and SV question is one of credit, not of size.

## 5. Corrected ratio: what changed against GAP-07b, and Day's 17.5 M

- GAP-07b's critic rows (assumed share 0.86 / 0.78 on SNVs: 11.14 / 12.13; on all events 11.32 / 12.48) are matched by measured counterparts: 0.844 on SNVs gives 11.32; with the measured indel share 11.46; the combined <2%-records row 12.50-12.67 against GAP-07b's 12.29-13.37.
- **Like for like (SNV-only):** Day's SNV-only 17.5 M per lineage (35 M / 2, polymorphism included) against 15.94 M measured fixed SNVs per lineage (37.77 M x (1 - 0.156) / 2; symmetric): **+9.8%**. The raw SNV count per lineage is 18.88 M, so the polymorphism correction takes the SNV-only requirement from 7.3% below to 9.8% above Day's figure.
- **All events:** 17.5 M against 17.89 M (symmetric, SNV + indel) is **-2.2%**. That close match is two offsetting errors (omitted indels, included polymorphism), as GAP-07b said, now measured.
- **Shortfall at the MITTENS rate** (GAP-07b: 91,800 on 17.5 M; scaling by proportion, hand-derived): about **83,600 on SNV-only fixed events (-8.9%)**, and about 93,800 on all fixed events. Both bases are stated because the first is Day's own variant and the second the event count. The rate side is outside this check.

## 6. Who this helps

**Critics (on the polymorphism point).**
- The polymorphism correction is real and has the size CSAC gave for the human half: 15.6% of human-derived differences still segregate at AF >= 1% (17.3% at 0.1%, 20% seen at all). Nesslig20 (PS-03; Peaceful Science topic 18094, post 1): "since they use one (or a few) reference genomes, not all of the differences they identified between genomes are actually fixed in either the human or chimp populations." This is what the measurement supports. GAP-07b's critic-favourable rows (11.1-12.5) were about right; measured counterparts are 11.3-12.7.
- The result is stable across resources (NYGC 16.06% vs phase 3 16.11% on the same chromosomes; same people, independent calling pipeline).
- The human lineage alone, which needs no chimp assumption and is Day's own lineage, gives 11.9, higher than the symmetric headline.

**Day.**
- 84.4% of human-derived SNVs are fixed in humans. The ratio moves from 9.7 to 10.6-12.6, not to 1.
- His reply to the ancestral-variation objection is a separate set of variants. Day (Z22903977 p.3, Q37): "Under coalescent theory, the expected pairwise divergence contributed by ancestral polymorphism is θ = 4Nₑμ per site." (04-28 ¶24): "Their inflated ILS figure does not rescue anything. It simply distributes the fixation requirement across both lineages instead of consolidating it on one." The 15.6% measures only what still segregates. Sorted ancestral variants are fixed now, count as fixed here, and are not measured; Camestros (CA2 ¶46, CA-04): "So Day is treating ALL the genetic differences between chimps and humans as mutations that initially only occurred after the point of divergence of the two species." is the objection that this check does not address (a mutation-supply question for A5, not a fixation count). The audit's A3c "Against: none in the Day corpus addresses polymorphism" is stale: Q37 and the 04-28 passage do address ancestral polymorphism, though not the segregating-now share.
- SVs at or above 50 bp are less polymorphic than SNVs (6.8% human-lineage), consistent with his "post-divergence" remark, but the data cannot test it (§4). Applying the CSAC SNV share to indels and SVs, as GAP-07b's critic row did, over-corrects slightly (0.1 in ratio).
- On the human data only, the pooled share is 8.25% and the ratio 10.58 (a). The critic-side 11.5 depends on a chimp assumption; the human-lineage row (11.9, no assumption) does not.
- His SNV-only 17.5 M is 9.8% above the measured fixed SNVs, and the SNV-only shortfall falls about 9%, which is not a flaw of his framing but a measured correction on the SNV basis.

**Neither.**
- **This check does not move the unit result.** 205 M (bp) against 17-19 M fixed events per lineage stays at 11-12, far from 1. Polymorphism is a 10-20% correction; the unit mismatch is the 10x.
- It does not test selection. A fixed difference is not a selected one (branches A5, B, G, H).
- No chimp data: the direction of the true chimp share is unknown. The human panel is species-wide, while panTro6 is a single reference; a matching chimp standard is either species-wide (probably a higher share, towards the 2x row) or reference-subspecies-wide (lower), so the 0.5x row (10.97) and the 2x row (12.57) bound the plausible directions; neither is a measurement.

## 7. Caveats

1. **Chimp lineage unmeasured.** Great Ape Genome Project / de Manuel 2016 variation is in older chimp assemblies or raw reads and needs a liftover and large downloads; not attempted. Which direction the true share lies is unknown (§6, "Neither").
2. **Chromosomes.** chrX (phase 3 has only 107 k X records; the NYGC X file is 2.5 GB, not fetched) and chrY (no panel) excluded; autosomal shares applied to 6% of the sites. Effect on the ratio below 0.1 in either direction (reviewer estimate); not modelled. The third-state and unpolarized shares (6.3%, 8.6%) give 11.42 instead of 11.46 [PH].
3. **Biallelic panel, short reads, strict mask.** Multi-allelic sites are absent from phase 3 (NYGC chr21+22, which splits them, agrees to 0.05 points on s_H). Shares outside the mask (6.5% pooled vs 8.25% inside) and for indels and SVs are lower bounds. Sites outside the VCF count as fixed.
4. **Panel size and the threshold.** The share at AF >= 1% is stable; at lower thresholds it grows with sample size (17.3% at 0.1%, 20% seen at all in 2,548 people). 1000 Genomes is a small, geographically uneven sample; a larger panel would sit further up this gradient. The Q5 miss (+4.4 points) is this gradient. The "seen at all" row (12.05) is the other end of the threshold range from Day's 10% (11.08).
5. **hg38 is a mosaic reference.** Its private alleles (0.4% of human-derived sites, p_chimp >= 99%) count as polymorphic. Small.
6. **Alignment artefacts** (GAP-07b's) carry over: paralog/nested alignments, qDup, non-T2T assemblies.
7. **Indel and SV matching** uses net length and position, not sequence; chance matches run at 0.2-0.9 points (§4); recall of short-read calls is a competing explanation for the lower indel and SV shares.
8. **Polarization.** Indel polarization is GAP-07b's symmetric post hoc rule, reliable to 50 bp, window-dependent (7.4-8.7%); the SV lineage split uses the as-run rule and is unresolved above 50 bp.
9. **Prediction record.** One miss (Q5, +4.4 points against <= 3); the SV and indel points were missed within their bands; the (c) point is a registration slip (§2).

## 8. Post hoc

1. **Top-level flag fix [PH].** The main-run "top-level fills" flag was true for every SNV (a level-1 fill's range contains its nested fills), so two rows of the main report equalled the unrestricted rows; found by seeing identical n. `gap07c_posthoc_toplevel.py` (committed before it was run) recomputes it: 33.18 M top-level and 2.29 M nested of 35.47 M autosomal SNVs (93.5%, as GAP-07b's 92.7%); top-level human-derived s = 15.69%, nested 12.75%. The duplicated rows were removed from the committed raw reports with a labelled note (original in bd26aaa); the top-level ratio (12.27) is a script output of the review pass.
2. **Review fix pass [PH]** (`gap07c_posthoc_review.py`, ae42a91, committed before it ran; stage `ctl` on the workhorse, stage `report` on the workhorse): symmetric indel polarization, SV by lineage with Wilson intervals, chance-match controls, the bracket table, the threshold rows with indel shares varied, third/unpolarized shares, numerator correction, the like-for-like SNV-only comparison. Outputs `raw/gap07c_posthoc_review.{json,out}`, `raw/gap07c_posthoc_ctl.out`.
3. The "human lineage 11.9" of the first version was by hand and is replaced by the script row (11.90, with the raw 10.11 reproducing GAP-07b's 20.28 M human-lineage events). The correctness review's 12.1 used a smaller human-lineage indel count (1.36 M); the script's convention (human-polarized plus half of all unpolarized events, scaled to 4.30 M) gives 1.88 M events and reproduces GAP-07b's raw figure.
4. Figure script is presentation only. No allele-frequency-dependent change was made to the main script after the run.

## 9. Files

`research/checks/gap07c_polymorphic_share.py` (078850b), `gap07c_posthoc_toplevel.py`, `gap07c_posthoc_review.py` (ae42a91), `gap07c_figure.py`; `results/raw/gap07c.host`, `gap07c_report.{json,out}` (autosomes, phase 3; top-level rows removed), `gap07c_report_p3_chr21_22.*` and `gap07c_report_nygc_chr21_22.*` (cross-check), `gap07c_posthoc_toplevel.json`, `gap07c_posthoc_review.{json,out}`, `gap07c_posthoc_ctl.out`, `gap07c_baseline_*.json`, `gap07c_afq_*.out`, `gap07c_sites*.{out,json}`; `results/R4-GAP07c-polymorphic-share.png`. Site lists, AF and control arrays are in gitignored `sources/raw/gap07c-*`.

Not edited (lead to integrate): claim files (A3, A3b, A3c, A3x), `ledgers/gaps.md` GAP-07, the argmap, README, RESULTS.md, REVIEW.md. Suggested claim edits:
- **A3c** (external stays `supported`; fidelity `partial`; add a Check paragraph and move status past "extracted"): "R4 GAP-07c: 15.6% of human-derived divergent SNVs have the chimp allele at >= 1% in 1000 Genomes (14.8-16.7% per chromosome; NYGC 16.06% vs phase 3 16.11% on chr21+22; consistent with the human half of CSAC's 14-22%); the chimp side is not measured; SVs >= 50 bp 6.8% net on the human lineage (n = 450). Sorted ancestral variation is not measured." Replace "Against: none in the Day corpus addresses polymorphism" with Q37 (Z22903977 p.3) and 04-28 ¶24.
- **A3b** (external stays `supported`, with the correction): Day's SNV-only 17.5 M is 9.8% above the measured fixed SNVs (15.94 M) and 2.2% below all fixed events (17.89 M); the SNV-only shortfall falls about 9% (about 83,600) and is about 93,800 on all fixed events.
- **A3x** (external stays `supported`): 205 M is 9.7x raw and 10.6-12.6x fixed events (human lineage alone 11.9; 11.1-12.1 over thresholds); combined with GAP-07b the bracket is about 8-13. The SV and indel polymorphic shares are measured (6.8% / 7.4-10.5%, lower bounds).
- **A3** (external stays `contested`; internal `holds`; fidelity `partial`): fixed events per lineage 17.2-17.9 M (human lineage alone 17.22 M, symmetric 17.89 M) against 21.05 M raw; polymorphism share measured on the human side, chimp side assumed; open items: chimp panel, T2T re-run, long-read SV set.

## 10. Review resolution

Status: applied / partly applied / declined (with reason). Finding ids: `Corr-M1, M2, m1-m8, N1, N2` (correctness); `GD-1..6` (Day side); `GC-1..6` (critic side).

### Correctness review

| id | status | resolution |
|---|---|---|
| Corr-M1 | applied | §1, §4, §7: the as-run indel polarization (GAP-07b's withdrawn pre-registered rule) is replaced by GAP-07b's symmetric rule; human-lineage indel share 7.4-8.7% (9.5-10.5% in mask) over windows 2-20, central 10.12%; "reliable" wording removed (reliable to 50 bp only, window-dependent); the as-run row is shown for comparison. The ratio moves by 0.01 (11.47 to 11.46). |
| Corr-M2 | applied | §4: like-for-like human-lineage SV share 6.9% (net 6.8%, n = 450, 95% interval 4.9-9.6%), about 2.3x below SNVs; the "net 1.2%" is dropped (the pooled net is 1.68%); "supports Day's Q100" is now "consistent with", with short-read recall and the sorted-variant limit as competing explanations; scorecard Q8 and §0 corrected. |
| Corr-m1 | applied | (a) uses the pooled indel share (5.28%): 19.38 M, 10.58. "Bound" replaced by "human data only". The main run's 10.64 is shown in the scorecard. |
| Corr-m2 | applied | §2 Q9: the (c) point was mis-registered (2 x s_H on all events), (c) as defined is 1.5 x s_H; the row for the registered definition (13.92) is in the bracket; "(c) point missed" removed from §7. The Q9 (b) point equals the SNV-only row; stated. |
| Corr-m3 | applied | The hand-derived 11.9 is replaced by a script row with the check's own conventions: 11.90 (raw 10.11 reproduces GAP-07b's 20.28 M human-lineage events). The correctness review's 12.1 (1.36 M human indel events) is not reproduced; the difference is stated in §8.3. |
| Corr-m4 | applied | The top-level row (12.27) and the combined-critic counterparts are script outputs of `gap07c_posthoc_review.py`; the duplicated top-level rows are removed from the raw reports with a labelled header (original in bd26aaa). |
| Corr-m5 | applied | §0, §1, §6: the NYGC panel is "same people, independent calling pipeline"; the phase-3 sample counts (NS = 2,548) are stated; only the AF >= 1% comparison is like-for-like (the ultra-rare bands differ by call set). |
| Corr-m6 | applied | §4: chance-match controls genome-wide (-d 0.41-0.69%, d+-1 0.23-0.45%, shifts 0.03-0.07%); the net indel shares are overstated by at most that; recall explanation added; sequence content not compared (stated). |
| Corr-m7 | applied | Bracket rows: third/unpolarized shares (11.42), indel share varied with the threshold; X/Y effect stated (below 0.1, reviewer estimate; not modelled). |
| Corr-m8 | applied | "Fixed" defined in §0 as "chimp allele < 1% in humans"; §6 wording changed ("fixed" no longer read as "derived allele at 99% or more" in the Day section). |
| Corr-N1 | applied | 2.2% (not 2%). |
| Corr-N2 | applied | §1 definitions: polarization accuracy is unmeasured, linked to GAP-07b's caveat, with the H/C symmetry and the 1.0% C-derived bound as sanity checks. |

### Day-side review

| id | status | resolution |
|---|---|---|
| GD-1 | partly applied | Headline is a bracket with chimp-assumed and human-data-only rows marked; a 0.5x row added; "commonly reported to be higher" removed (unchecked) and replaced by "direction unknown; depends on the standard" (§6). Declined: citing a checked chimp diversity number (needs the chimp data and the subspecies of the reference, not obtained). |
| GD-2 | applied | The numerator's SNV part is corrected by the same share in every bracket row (11.46 to 11.31 on (b)). |
| GD-3 | applied | Day's 10% threshold row (11.08, indel share varied too) added with its origin (Q55); band columns relabelled as the frequency of the chimp-matching (ancestral for human-derived) allele with the derived-allele reading spelled out (§3). |
| GD-4 | applied | The 84.4% fixed complement is in the headline and bottom line; "confirmed" replaced by "consistent with the human half of CSAC's range". |
| GD-5 | applied | See Corr-m1. |
| GD-6 | applied | §6 quotes Q37 and 04-28 ¶24 and states that the 15.6% measures only what still segregates; the A3c "Against: none" is flagged as stale in the suggested edits (not edited here). |

### Critic-side review

| id | status | resolution |
|---|---|---|
| GC-1 | partly applied | "seen at any frequency" (12.05) and AF >= 10% (11.08) rows added; the headline reads as a threshold range 11.1-12.1; NYGC described as the same cohort at 30x (tests calling, not sampling). Declined: a larger or more diverse panel on one chromosome (not run; proposed as a follow-up in §7.4). |
| GC-2 | applied | §4, §0, §2: "consistent with" Day's Q100; the SV share meets "near zero" only in the pool, the indel share is intermediate; recall and size-decay competing explanations stated. Declined: long-read SV set on the same events (follow-up, not run). |
| GC-3 | applied | §0 bracket table, parallel to GAP-07b's, with the human-lineage row (11.90), top-level (12.27), 2x (12.57), the measured counterparts of GAP-07b's combined critic rows (12.50-12.67 against 12.3-13.4), and the Day-favourable rows re-expressed (8.4-11.1). Combined bracket about 8-13. |
| GC-4 | applied | §5 and §0: like-for-like SNV-only 17.5 M against 15.94 M (+9.8%), all-events -2.2% as two offsetting errors; shortfall 83,600 (SNV-only, -8.9%) and 93,800 (all events). |
| GC-5 | applied | Verbatim quotes with locators for Nesslig20 (PS-03; topic 18094 post 1), Camestros (CA-04; CA2 ¶46), and Day (Q37; 04-28 ¶24); CA-04 is scoped as not measured here. |
| GC-6 | applied | Caveat 2: effect below 0.1 in either direction (reviewer estimate). |
