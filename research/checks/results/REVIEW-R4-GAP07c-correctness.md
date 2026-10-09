# REVIEW R4 GAP-07c: correctness

Reviewer: correctness pass. Date: 2026-10-09. Scope: `R4-GAP07c.md`, `gap07c_polymorphic_share.py` (078850b), `gap07c_posthoc_toplevel.py`, `raw/gap07c_*`, with `R4-GAP07b-alignment.md` and `gap07b_alignment_count.py` / `gap07b_posthoc_polarize.py` for context.

**Verdict.** No BLOCKER. The SNV measurement (s_H = 15.6%, pooled 8.25%, the SNV part of the corrected ratio) reproduces independently and I found no allele, strand, coordinate or arithmetic error in it. There are 2 MAJOR findings, both about what the indel and SV numbers are and how they are described, not about the headline ratio. Neither moves the ratio by more than 0.02. There are 8 MINOR findings and 2 NITs.

## What I checked and how (evidence for the "no error" parts)

All spot checks were read-only and ran on `na-workhorse` (1 process, `nice -n 19`, scratch in `/tmp`, removed afterwards; nothing committed) or locally (`nice`). Scripts were written fresh and share no code with GAP-07c, except where stated.

| item | check | result |
|---|---|---|
| Pre-registration integrity | `git diff 078850b -- gap07c_polymorphic_share.py` empty; md5 c5211f89... equals `gap07c.host`; post hoc script committed 02:50:47, its output file stamped 02:50:52; main report 02:49:50 | holds. The post hoc script was committed before it ran. |
| Site list, chr21 | Re-derived every SNV column from the raw `hg38.panTro6.net.axt.gz` (pure Python, own 1-based to 0-based conversion, rev-comp already in axt) | 588,978 sites; positions, hg38 base and chimp base agree with `snv_chr21.npz` for all of them; 0 duplicate positions |
| Gorilla reuse, chr21 | Re-derived the gorilla base at each hg38 position from the raw `hg38.gorGor6.net.axt.gz` | 0 mismatches with stored `gb`. Polarization H/C/third/unpol = 266,749 / 284,546 / 7,915 / 29,768. Neither axt has overlapping target intervals on chr21, so "last write wins" cannot matter. |
| Polarization code | `polcls` in `report_stage`: gorilla = chimp base -> H, gorilla = hg38 base -> C, else third, none -> unpol | correct (hb != cb always, so the classes are exclusive) |
| Allele matching, chr21 | Independent dict join of 1,045,269 phase-3 chr21 records (`AC/AN`), ALT == chimp base | `pc` agrees at all 588,978 sites (0 mismatches at 1e-6); in-mask flag agrees at all sites; no record whose REF differs from the hg38 base; independent s_H(chr21) = 16.69% (report: 16.7%), s_C = 1.08% |
| Multiallelic handling | Counted ALT fields with a comma in the chr21 extract | 0. The phase-3 file is biallelic only (README: "restricted to biallelic"), so multiallelic sites are absent and counted fixed. Small and documented. The NYGC file (multiallelics split) agrees within 0.05 points on s_H. |
| Coordinate system | VCF header: calls made directly on GRCh38; no liftover is involved; VCF contig names have no `chr` and the code strips/adds it correctly. REF == hg38 base for 4,925,478 of 4,925,478 matched records; an off-by-one would give ~25-30% | consistent with the hg38 net/axt (same assembly, same coordinates) |
| Indel matching, chr21 | Brute-force re-match (net length d = qSz - tSz, |pos - tS| <= 2, max AF) on 20,000 random events vs stored `obs[w=2]` | 0 mismatches. Left-anchor convention is right: a deletion's 0-based start tS equals the VCF 1-based anchor pos, and an insertion junction tS equals it too (so w = 0 already hits the left-normalised case). Sign convention is right (VCF ALT length minus REF = chimp minus hg38). |
| Fixed-event arithmetic | Recomputed every row of §0 and §5 from the report JSON | (a) 19.266 M / 10.64; (b) 17.8785 M / 11.466; (b) SNV only 18.106 M / 11.32; (c) 16.292 M / 12.58; T = 0.001 / 0.05 rows 17.551 / 18.238 M; top-level row 16.701 M / 12.275. 21.051 M raw = (37,767,396 + 4,301,652 + 33,466) / 2. All reproduce. |
| Coding bug and fix | Post hoc JSON: top-level 33,183,899 + nested 2,288,258 = 35,472,157, "neither" = 0 | The diagnosis (level-1 range contains the nested fills) is right and the fix (level-1 range minus the union of all level >= 2 fill ranges, indent counted from the raw line) is right. The bug touched only the two secondary report rows. |
| Scorecard vs docstring | Compared Q0-Q10 text, points and bands | The text matches (one wording issue, MINOR-2). Q5 is reported as missed, honestly. |

## MAJOR

**M1. The indel lineage split uses GAP-07b's withdrawn pre-registered polarization rule, and the write-up describes it as reliable.**
- Evidence. `gap07c_polymorphic_share.py::polarize_events` is a verbatim copy of the as-run rule of `gap07b_alignment_count.py`. GAP-07b's own text (`gap07b_posthoc_polarize.py` docstring; R4-GAP07b §7 and its correctness review M1/M2) says that rule treats human-only and chimp-only gaps asymmetrically, gives an implausible 33% human share, "is NOT used for headline per-lineage claims", and was replaced by a symmetric window rule. GAP-07c's counts show exactly that artefact: 1,157,500 human-lineage vs 2,349,089 chimp-lineage events (human share of polarized 0.33).
- R4-GAP07c §7 caveat 8 calls it "GAP-07b's (reliable <= 50 bp, human share skewed as run)". GAP-07b's reliable rule is the post hoc one, not this one. The headline 10.6% indel share (human lineage, in mask), the "9.5% vs 1.8%" lineage contrast, and the scorecard line for Q8 all come from the withdrawn rule.
- Sensitivity (my run, local, same indel-AF arrays, GAP-07b post hoc rule, events <= 50 bp, w = 2 / 5 / 10 / 20, net of the same null): human-lineage share 8.7 / 8.3 / 7.9 / 7.4% (in mask 10.5 / 10.1 / 9.7 / 9.5%) against 9.6% (in mask 10.7%) as run; human share of polarized 0.38 / 0.43 / 0.48 / 0.52 against 0.33; chimp-lineage share 1.8 / 1.5 / 1.2 / 1.2%.
- Effect on the result: with the in-mask 9.5% (w = 20) the (b) ratio goes from 11.466 to 11.450. The number is robust; the description is not.
- Required: say in §1/§7 that the as-run rule was used, that GAP-07b withdrew it for per-lineage claims, and give the range above. Do not call it "reliable".

**M2. The SV share (1.7%) is compared with the wrong SNV denominator, and the scorecard's "net 1.2%" is not in any output.**
- The 1.7% (n = 4,623, chr21+22) pools every event >= 50 bp, both lineages and unpolarized. R4 §0, §4 and §6 set it against "15.6% of SNVs", which is the human-lineage-only share. By the check's own reasoning in §3 ("why the pooled share is half the human-lineage share") the like-for-like SNV figure for a pooled set is 8.25%, and the human-lineage SV figure is the one to set against 15.6%.
- From the stored `sv_chr21/22.npz` (the `pol` field is there, unused by the report), at AF >= 1%: human lineage n = 450, obs 6.89%, null 0.11%, net **6.8%**; chimp lineage n = 2,305, net 1.1%; unpolarized n = 1,868, net 1.1%; all, net 1.68%. By size within the human lineage: 50-100 bp 3.8% (n = 186), 100-1000 bp 9.6% (n = 219), > 1 kb 6.7% (n = 45). With n = 450 the 95% interval on 6.9% is roughly 4.5-9.3%.
- So SVs are less polymorphic than SNVs (6.8% vs 15.6%, about 2.3x lower, not 9x) and are close to the human-lineage indel share (7.4-10.6%). "Day's Q100 is supported" and "indels and SVs are less polymorphic ... so the CSAC share should not be applied" are over-credited by a factor of about 2 in the contrast. The SV matcher is also a recall-limited lower bound (R4 says so), which cuts the other way.
- Scorecard Q8 states "> 50 bp 1.7% (net 1.2%)". The report JSON gives obs 1.73%, null 0.05%, net 1.68%. "1.2%" is not reproducible from any output (it is near the chimp/unpolarized nets of 1.1%).
- Effect on the ratio: nil (events >= 50 bp are 104 k of 4.30 M). It is an interpretation and labelling error on the Day-side credit.
- Required: report the human-lineage SV share next to 15.6%, drop or re-source "net 1.2%", and soften the Q100 wording.

## MINOR

**m1. Treatment (a) mixes conventions.** (a) is defined as "chimp lineage credited with no polymorphism of its own", and its SNV share is the pooled 8.25%. Its indel share is the human-lineage 10.6%. The consistent pooled indel share is 5.3% in mask (4.1% over all events). Using 5.3% gives 19.38 M and a ratio of 10.58 instead of 10.64. Small, and in the Day-favourable direction the row is meant to bound. Also, the word "bound" in "Day-favourable bound" is ambiguous (it is the lowest ratio, not a limit).

**m2. The (c) pre-registered point is inconsistent with (c) as defined and coded.** (c) is "chimp share twice the human one", coded as s = 1.5 x s_H (pooled). The registered point (15.2 M, ratio 13.5) corresponds to 2 x s_H on all events (s about 30%: 15.1 M, 13.6). At the registered s_H = 15% the defined (c) gives 16.6 M and 12.4. The scorecard says "(c) point missed" and §7.9 counts it as a miss, but it is an arithmetic slip in the registration, not an empirical miss: observed 16.29 M / 12.58 against the right prediction 16.6 M / 12.4. State this. (Q9 (b) point 18.1 M / 11.3 equals the SNV-only row of the output, not the central indel-inclusive (b); both are in band, so no verdict changes.)

**m3. The hand-derived "human lineage alone, about 11.9 [15.52 M + 1.68 M fixed]" does not follow the check's own conventions.** The 1.68 M is reproduced by (human-polarized + all unpolarized indel events, scaled to 4.30 M = 1.808 M) x (1 - 7.07%), i.e. all unpolarized assigned to the human lineage and the w = 0 share. The SNV half uses "polarized + half of unpolarized" and the central w = 2 in-mask 10.6% (R4 §5, and `lineages_snv`). With the same convention as the SNVs: 1.357 M, total about 16.9 M, ratio **12.1**. It is tagged "by hand", but it should be recomputed or dropped. It also uses the M1 polarization.

**m4. Top-level row (16.70 M / 12.27) has no script output.** I reproduced it (35,017,058 x (1 - 15.69%) + 4,301,652 x (1 - 10.6%) + 33,466, halved). The post hoc JSON stops at fixed SNVs and its `note` says indels are "added separately". Add the arithmetic to the output or the post hoc docstring. It reuses all 4.30 M indels (also nested) with the same GAP-07b convention, which is fine. Separately, the committed `raw/gap07c_report.out/.json` still contain the two duplicated "top-level fills" rows (n equal to the unrestricted rows); R4 §8 explains them, but a note in the raw file or a header in `gap07c_report.out` would prevent misuse.

**m5. The NYGC panel is "independent" in calling pipeline, not in people.** The 3,202 NYGC samples include the 2,504 phase-3 individuals (plus 698 relatives), and the phase-3 file has 2,548. The 16.06% vs 16.11% agreement tests the resource and calling choice (a real and useful test), not sampling. Reword in §0/§6. The NYGC "filtered" panel also lacks many ultra-rare variants (band (0, 0.1%): 1.9% vs 2.7% in phase 3, on the same chromosomes), so only the AF >= 1% comparison is like-for-like. Phase-3 README text says N = 5,248; the file itself is NS = 2,548, AN = 5,096, as R4 states.

**m6. Indel chance-match control is weaker than the text implies, and the lower indel share has a recall explanation.** The +-10 kb shifted null gives 0.01-0.08%. Controls I ran on chr21 at AF >= 1%, w = 2, events <= 50 bp: for human-lineage events, same d 11.4%, shifted null 0.04%, sign-flipped (-d) 0.39%, same sign with d +-1 0.53%; chimp lineage 1.77 / 0.04 / 0.45 / 0.51%. So positional chance matches are about 10x the shifted null but still <= 0.5 points (size 1: -d 0.7-0.8%), and the net share is overstated by at most that. Sequence content is still not compared (caveat 7 says so). What is not discussed: short-read indel/SV calling recall is lower than SNV recall, so part of "indels (and SVs) are less polymorphic than SNVs" (§0, §6 Day) is detection. Combine with M1/M2 when rewording.

**m7. Unquantified approximations in the central (b) row, each small.** (i) The share s_H is applied to third-state and unpolarized SNVs (1.81 M of 37.77 M), whose measured shares are 6.3% and 8.6%: using about 7.5% adds 0.073 M fixed events per lineage and lowers the ratio from 11.47 to about 11.42. (ii) chrX and chrY (6% of sites) get the autosomal share; haploid/low-Ne sites should have lower diversity, so this also errs toward a slightly higher fixed count. (iii) In the "(b) at AF >= 0.1% / >= 5%" rows only the SNV share changes; the indel share stays at the T = 0.01 value (`s_ind_central`). Label the rows or vary both. None of these changes any conclusion; the stated range 11.2-11.7 is not widened by more than 0.05.

**m8. The T = 0.01 choice makes "fixed" mean "derived allele >= 99%".** §1 defines this correctly. §6 and the Day section ("84% of human-derived SNVs are fixed in humans") would be clearer as "have the chimp allele at < 1%"; the 4.4-point "seen at all" gap (Q5) is the part that is rare but not fixed. Not an error.

## NIT

- N1. "Day's 17.5 M ... within 2% of 17.88 M" is 2.2%.
- N2. Gorilla polarization accuracy (incomplete lineage sorting regions, assembly error) is not measured here; GAP-07b says the same. The C-derived share (1.0%) is a usable sanity bound, and the H/C split is near symmetric (16.4 M vs 17.4 M), but R4 should link the caveat rather than call polarization "GAP-07b's" only.

## Points answered directly

- **Allele matching.** Correct: strand (axt already reverse-complemented to the + strand of hg38), orientation (ALT = chimp base, REF = hg38 base, 100% REF agreement on 4.93 M matched records, 0 REF mismatches on all of chr21), "allele equal to chimp base" logic, and zero-based/one-based handling are all right. Multiallelics are absent in phase 3 (not handled, by design) and split in NYGC. No liftover is involved; the VCF is native GRCh38.
- **Gorilla polarization reuse.** Applied correctly for SNVs (independent chr21 reproduction, 0 mismatches). Reused incorrectly for indels (M1).
- **Indel matching.** Net length, position and sign are correct and reproduce by brute force. The shifted-position null is valid but understates the chance rate (m6).
- **Fixed-event arithmetic.** (a), (b), (c) and top-level rows reproduce. (a) mixes conventions (m1); the (c) prediction is mis-registered (m2).
- **Coding bug and post hoc fix.** Handled properly: found from identical n, diagnosed correctly, fixed in a labelled post hoc script committed before its run, headline unaffected. Needs only the small documentation additions in m4.
- **Scorecard and labelling.** The scorecard matches the docstring (Q5 miss reported). Corrections needed: Q8 "net 1.2%" (M2), the (c) "miss" (m2), and the SV/indel descriptions (M1, M2). Post hoc items are labelled; the only unlabelled derived numbers are the m3 and m4 hand calculations, which are tagged as by hand or post hoc.

## Reproducing my checks

Scripts are in the session scratchpad only (not committed): independent site and gorilla re-derivation from the raw axtNet (chr21), independent VCF join and brute-force indel match (chr21, workhorse, scratch removed), re-polarization with `gap07b_posthoc_polarize.polar` (autosomes, local), SV share by `pol` from `sources/raw/gap07c-af-nygc/sv_chr2{1,2}.npz`. I can add any of them to `research/checks/` as post hoc scripts if the fix pass wants them.
