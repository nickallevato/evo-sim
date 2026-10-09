# Review of R4-C1d: Day-side steelman

Reviewer role: argue for Day as strongly as honesty allows, then judge fairness. Date: 2026-10-09. Targets: `results/R4-C1d.md` (line numbers below refer to it), `research/checks/c1d_aadr_real.py`, `results/raw/c1d_v62_posthoc.txt`, claim files C, C1a, C5a, C6, C7, B2e, `sources/quotes-day.md`. Day's text was read from `sources/raw/day/zenodo-18525185.txt` and `zenodo-23046531.txt` (read only, never executed); the Zenodo search artefacts in `sources/raw/day-scripts-search-2026-10-09/` and the AADR `.anno` files in `sources/raw/aadr-anno-2026-10-09/` were read as text. I ran no genotype extraction and edited no other file. Everything below is either quoted or a ratio/count of existing outputs (the one fresh count, anno row numbers, is flagged in F5).

## Verdict in brief

The check is mostly fair. It pre-registered, reported its own failed predictions (P3, P5, P6, P14), credits Day in section 8, does not claim to show that Day used a different pipeline (line 143), and its suggested claim edits (line 123) carry the transversion result. The numbers I could re-derive from its tables hold.

Four things are not fair or not finished, in order of weight:

1. **Damage is the one lever the check's own prior named and the 120-cell grid left out.** "Not reproduced under any reading" is true of the readings tried. The damage-aware readings were only tried at the extreme (transversions only, post hoc), and that reading does not reproduce Day either, in a way that is informative about what he did (F1).
2. **The "scripts not found" finding is attached to the wrong paper** (F2). The sentence about scripts is in Z23046531 (two-period statistic). The paper that holds the "21" (Z18525185) makes no code claim.
3. **Day's own later paper is an unused calibration** for the eligible count, with a documented filter (F3).
4. **The damage-immune comparison against neutral is left in two opposite directions** within section 8 (F4). It is the best Day-side result in the check and sits in a parenthetical.

## The strongest honest Day-side case

1. The 4,957 (or 3,649) is not a clock result. It is 97.7% transitions, against a panel that is 77.6% transitions; 98.1% of the events have a minor allele at 1-5% in the older bins, and 4,177 of the 4,957 land in the 0-500 BP bin, where the minor allele is absent from 901 of 901 chromosomes (R4 lines 9, 56-64). That is an old-versus-modern data-quality asymmetry. No one, including Day, would defend a "fixation" that is a 97% allele reading 100% in the best-called bin.
2. In the one class immune to deamination (transversions), the literal statistic gives 36 (autosomes) to 113 on v62, 44-66 on v66, against Day's 21: a factor 1.7-5.4. The same class gives a pre-7000 BP share of 0.98-0.99 against his 0.9986 (line 9). In that class his qualitative claim ("essentially all fixations before 7,000 BP") is nearly right; in the all-site class it is 91%.
3. The rough neutral comparator for that class in R4's own words is "roughly 900 expected against 36-113 seen" (line 131). If that holds up, the damage-immune class shows a deficit of 8-25 fold against neutral at Ne 1e4, and the critics' "neutral predicts thousands" (C1b/C1c) was predicting the damage artefact.
4. Day's eligible count is not an outlier among Day's runs. His Feb 2026 run gives 22,428 and his Sept 2026 two-period run (also v62, also January 2026 data) gives 17,806 "newly reaching 100%" (F3). The check's all-site count is 62,757 (54,243 autosomal). Two runs of one pipeline that agree with each other and sit 2.4-3.5x below the reconstruction point to a systematic processing difference, and the largest known systematic difference in ancient-DNA genotype data is damage and quality treatment.
5. His method text is short (a one-sentence fixation rule). It is not a complete specification, and the generating scripts, if they exist, were presumably written with an AI co-author ("Athos, Claude" is a creator name on 38 records). A statistic reconstructed from three paragraphs of prose matching to within a factor of 3 on eligibility and failing on the tail is the usual outcome of an underspecified pipeline; it does not show the original is wrong.

## What does not survive scrutiny (the critic's side of this steelman)

- **His text says nothing about damage, UDG, transversions, quality or contamination.** The only sample criterion in Z18525185 is "European" plus dates. A filter that determines the headline by a factor of 100 and is absent from the method section is a documentation failure on Day's side, not a vindication. The most this steelman can reach is "underspecified and possibly damage-filtered", not "correct".
- **The start table matches all-site, not transversion-only.** v62 all-site gives 79.0 / 19.8 / 0.7 / 0.5 against Day's 79.2 / 20.2 / 0.5 / 0.2. Transversions-only give 92.3 / 5.1 / 1.3 / 1.3 (all chromosomes) and 99.0 / 0.8 / 0.1 / 0.0 (autosomes) (`c1d_v62_posthoc.txt` section B). A pure transversion filter is therefore not what Day ran. The 10000+ bin in the transversion class holds 85% of events (5,382 of 6,306) against Day's 18.6%. So the damage hypothesis has to be "an intermediate filter", which is exactly what was not tested.
- **Admixture and the real minor alleles.** The 1-5% older-bin minor alleles could be real (recurrent CpG transitions, true low-frequency variants since lost). R4 says this (line 66, 145). Nothing here separates the two.

## Findings

### F1 (MAJOR) The damage lever is missing from the grid, and "not reproduced under any reading" is stronger than the evidence

R4 line 8: "No configuration of the 120 tried on V1 (eligibility E1/E2/E1p x dating T2/T1 x min-calls 1, 5, 10, 20, 50 x two tracked rules x all/autosomal SNPs; 12 more on the PASS-only sample V2) came within 10% of his eligible count together with S21 within 50% of 21."

The grid has no dimension for substitution class, library type or damage rate. The script's own prior anticipated that dimension. Docstring P3: "real AADR carries damage/contamination errors that C1c showed inflate eligible 4-27x". The C1c Day-side review's F7 and R4-C1c line 197 deferred an "Anno-derived eps (damage-rate, library-type columns) and a transversions-only variant" to a new design. C1d ran the transversion variant post hoc (line 65) and did not run the anno-derived one, although the columns are in the local anno: header column 34 "Damage rate in first nucleotide on sequences overlapping 1240k targets (merged data)" and column 38 "Library type (minus=no.damage.correction, half=damage.retained.at.last.position, plus=damage.fully.corrected, ds=..., ss=...)".

The reading R4 did run is the extreme one, and it fails Day's table (eligible 6,306-9,260 against 22,428; 10000+ share 85% against 18.6%; start 92-99% against 79.2%). Day's eligible count lies between the transversion-only count (6-9k) and the all-site count (63k), and so does the start-table-compatible region. A filter that masks transitions only for non-UDG libraries, or drops individuals above a damage rate, would land in between. That is untested, not refuted. R4 line 66 says as much ("Not isolated further") but the headline (lines 8, 137 "false under his own rule") is stated without that qualification.

Specific overstatements to correct:
- Line 137: "His own statement 'essentially zero fixations in the subsequent 7,000 years' is false under his own rule on real data: the literal statistic gives 4-5 thousand post-6000 BP events." "His own rule" is the reconstructed all-site rule; in the transversion class the count is 36-113. Say "under the all-site literal reading".
- Line 8 and the summary "Day's 21 does not reproduce under any reading": the TV-only reading is 1.7-5.4x from 21 and it is outside the 120-cell grid.

Fix (post hoc, each labelled, prediction written before the run, per rule 5):
1. Library-type-aware readings: mask transitions in individuals whose library type is "minus" (and a variant for "half"), keep them for "plus"; run the E1/T2 statistic and the start table.
2. A damage-rate readings: drop individuals with first-nucleotide damage above a stated threshold (two thresholds).
3. Event attribution: for the 4,177 events in the 0-500 BP bin, report what share of the older-bin minor-allele copies come from non-UDG individuals, against the share of such individuals in those bins. This is the discriminating test between damage and real variation, and it needs only a new group definition (about 2 minutes of extraction on workhorse).
4. State the outcome as one of: reproduces under a documented-class filter; does not; ambiguous.
5. In the brief, replace "not reproduced under any reading" with "not reproduced by the all-site literal reading or by any of the 132 grid cells; the transversion-only class is within 1.7-5.4x of 21 but misses his eligible count, profile and start table; intermediate damage-aware readings were not run".

### F2 (MAJOR) "Scripts not found" is attached to the wrong paper, the search is Zenodo-only, and one saved artefact is a 404

What the check says: line 7 "Day's scripts: not found. The Z23046531 sentence 'Analysis scripts are available from the authors at Zenodo' has no target." Line 17: "the Z23046531 data-availability sentence is unfulfilled as of 2026-10-09." Line 137: "the scripts he cites are not on Zenodo."

What Day's papers say:
- Z23046531 §5 (Data Availability): "Analysis scripts are available from the authors at Zenodo." This paper's statistic is the two-period comparison (Neolithic 6000-8000 BP against date = 0), not the 11-bin "21" statistic. R4 line 18 itself says "The two-period statistic of Z23046531 is a different quantity and is not computed here."
- Z18525185 (the "21" paper), Appendix B, in full: "Analysis was performed on the Allen Ancient DNA Resource (AADR) v62.0, publicly available at the Reich Lab website." It makes no code claim. A search of the extracted text finds no "script", "code" or "github" in it.

So the finding "Day's cited Zenodo scripts do not exist" does not apply to the statistic C1d reconstructs. At most it says: the later paper promises scripts for a different statistic and none are on the records searched. The reconstruction itself was necessary because Day never promised code for the 21.

Coverage problems:
- Only Zenodo was searched (creator filters and resource type). No GitHub, OSF, Hugging Face, Gist, Day's Substack or AI Central. The only "github" hits in Day's own text are links to the third-party LTEE repository (`zenodo-23003785.txt` line 161, `zenodo-23105291.txt` line 54, Good et al.), so GitHub is not Day's demonstrated habit, but also not excluded. (Searching is inbound; contacting the authors is not allowed under rule 6.)
- The wording is ambiguous: "available from the authors at Zenodo" can mean "on request from the authors" or "deposited at Zenodo". R4 reads it only as the second.
- Record 23046531 is 10 days old (published 2026-09-29, `rec23046531.json`). A pending revision is not ruled out.
- The "versions" lookup saved as `versions23046530.json` is `{"status": 404, "message": "Not found."}`. It was requested for the concept id 23046530. The record's own `links.versions` is `https://zenodo.org/api/records/23046531/versions`. R4 line 15 lists "versions" among the things searched; the saved artefact does not show that.

Fix: change lines 7, 17 and 137 to "no code was found on the Zenodo records searched; Z23046531 promises scripts for its two-period statistic; Z18525185 (the 21) promises none". Re-run the versions request on the record's own link and save it. Search GitHub and the blog sources for the creator names and the 22,428 string, record the date, and set a re-check date. Remove "do not exist" wherever it appears downstream (RESULTS.md, REVIEW.md, the claim paragraph).

### F3 (MAJOR) Day's own two-period run is an unused, independently documented calibration for the 22,428

R4 line 18 sets Z23046531 aside. But the later paper gives (Q54, Z23046531 §3.3, p.4): "The true fixation check identified 17,806 loci newly reaching 100% and 8 loci newly reaching 0% in the modern period." with 17,805 of the 17,806 starting at 90-99% (Table 3). "Newly reaching 100%" is the same event as the E1 eligibility rule in the script (modern 100%, Neolithic below 100%). Its documented procedure, unlike Z18525185's:
- §2.3: "SNPs were required to have a minimum of 100 genotyped samples in each period." and autosomes only (1,143,671 SNPs);
- §2.2: "a Neolithic period (6000-8000 BP) and a modern period (date = 0, i.e., present-day)", 1,372 and 680 samples, v62.0 analysed January 22, 2026.

So there are two Day runs on the same release, 22,428 and 17,806 (a 26% difference with different samples), against 62,757 all-site (54,243 autosomal) here. The comparison matters for the "irreproducible" label: if a documented filter set (autosomes, 100 genotyped per period, date = 0 moderns) brings the reconstruction to about 18k, then the discrepancy is a processing choice that Day documents in one paper and omits in the other. If it does not, the discrepancy is larger than a filter and the case against the reconstruction being his pipeline is stronger. Either outcome is informative, and neither is available from the present write-up.

My expectation is that the 100-sample filter alone changes little (eligible alleles come from well-called sites), which would leave the gap unexplained. That is a reason to run it, not to skip it.

Fix: run the Z23046531 §2.2-2.4 procedure on v62.0.p1 and v66.p1, as a labelled post hoc step (or a new pre-registered mini-check), with modern = date 0 and a second variant with the 0-500 BP bin. Compare to 17,806 / 17,805 (v62) and 3,469 / 3,466 (v66); report in the section 3 table. Note that Day's v66 run used 395 Neolithic and 441 modern samples (his own §2.2, attributed to an annotation-format ID-matching problem), so the v66 figure of 3,469 is not a like-for-like target and should not be used to score the reconstruction.

### F4 (MAJOR) The best Day-side finding is stated in opposite directions within section 8

Line 131 (Day / allies): "Taken at face value that residual is small compared with the thousands the neutral expectation gives at textbook N_e under C1c's assumptions (rough, panel share of transversions about 22%: roughly 900 expected against 36-113 seen; not run as a calibrated comparison)."

Line 140 (Critics, "cuts against critics"): "'21 is a deficit against neutral thousands' is not supported either, because the thousands are mostly an error-class artefact."

These can both be true only if the damage-immune class has a neutral expectation that nobody has computed. The first says the damage-immune class is 8-25 fold below neutral at Ne 1e4 (3,925 x 0.22 = 863, against 36-113). The second says there is no deficit. Facts that bear on which is right, all from existing outputs:
- C1b/C1c's 3,925 (R0, Ne 1e4) is an error-free neutral count (R4-C1c line 70 attributes the eligible inflation to eps, not S21). The real all-site count is 4,957, which agrees with it only because the real excess is in a class the model does not represent (line 120: "the transition-class concentration in the real events is something the model does not represent"). The agreement at about 4,000 is then partly coincidence, as line 120 itself says.
- The transversion class has 6,306-9,260 eligible alleles. A class-independent neutral model at 22% would give about 3.3k eligible (15.2k x 0.22). So the class is richer in eligible than the model predicts but poorer in post-6000 events by 8-25x. Both facts are Day-relevant and neither is discussed.
- The model uses a flat site frequency spectrum and ignores 1240k ascertainment; both change a transversion-only expectation.

Not fair to either side as written. Fix: either run C1c's model with eligible matched to the transversion class (6.3-9.3k) and compare S21 (36-113), or state in both bullets that the damage-immune comparison against neutral is open, with the 863 figure as an unreliable upper bracket. Add the sentence to the brief; it is the only result in the check that bears directly on whether a deficit exists.

### F5 (MINOR) The v62.0.p1 versus v62.0 comparison is mostly fair; the check can quantify it and misses the larger composition issue

The caveat (lines 21, 143) is that the p1 patch (June 2026) is not the original v62.0 (September 2024). Two checks from existing files:
- Day, Z23046531 §2.1: "contained 17,629 individuals and 1,233,013 SNPs on the 1240k capture panel". The local p1 anno has 17,468 rows (count by csv parse of `v62.0.p1_1240k_public.anno`, excluding header): a difference of 161. The same paper states for v66: "Version 66.p1 is identical to v66.0 except for the removal of 161 Papuan modern individuals for data access compliance." The v66.p1 anno has 23,089 rows, equal to Day's count for v66.p1. This is an inference (same patch tag, same count, same reason), not a proof for v62, but it suggests the p1 patch removed 161 non-European modern individuals and the SNP file md5 is the same one for both releases (`50f66178...`). That is a small effect on a European sample and no effect on the 1,233,013 SNPs.
- So the version objection is weak. The check is fair to compare against p1, and should say why.

The larger sensitivity is the modern bin: V1 has 524 individuals in 0-500 BP against Day's 625 (16% short, line 28), and that bin holds 4,177 of 4,957 events (84%). Day's Z23046531 defines modern as "date = 0, i.e., present-day"; the 0-500 BP bin of Z18525185 may include 1450-1950 CE individuals. Neither definition was varied for the "21". The 101-individual gap is not explained by the 161.

Fix: add the 17,629 - 17,468 = 161 arithmetic and the v66.p1 match to section 2 as a plausibility argument; add one sensitivity row with the 0-500 bin restricted to date = 0 (and one with a wider lat/long box that adds about 100 moderns); say that the version difference is probably smaller than the modern-bin definition.

### F6 (MINOR) The minimum-calls grid is coarse exactly where the tracked fraction crosses Day's

Line 53: tracked 0.996 / 0.986 / 0.959 / 0.572 at m = 5 / 10 / 20 / 50, and "No setting gives tracked 0.65-0.80 (it jumps from 0.96 to 0.57 between m = 20 and m = 50)". Day's 0.727 lies in that gap. S21 at m = 50 is 3,301 and eligible 58,196, so the conclusion on S21 and eligible does not depend on the gap, but the sentence "no setting" should read "no setting among those tried". Fix: add m = 25, 30, 35, 40 (a table lookup on the retained per-SNP counts), or reword.

### F7 (MINOR) Precision of the headline numbers

- "98% of the post-6000 events are transitions": R4 gives 97.7% for S21 (5000-6000 BP and younger, 4,957) and 97.1% for S23 (6000-7000 and younger, 5,717), v66 98.2% / 97.3% (lines 59-60). "Post-6000" matches S23; say 97% and 98% for S23 and S21.
- "Transversions alone give 36-113, which is 'the same order' as 21": the ratio is 1.7-5.4 (36/21 to 113/21), and v66 gives 44 and 66. The phrase "same order" is defensible, but give the factor. Also the 36 is autosomal and 113 is all chromosomes; Day's Z18525185 uses all 1,233,013 SNPs.
- "Real counts are thousands (S21 3,649-4,957)" is the all-site count only. The transversion class is 36-113. Any one-line summary should carry both, since they differ 40-130 fold.
- "Under any reading" appears in the brief as a statement about the grid (line 8 says "in the grid"); downstream summaries drop that.

### F8 (MINOR) keruru's correction: scope and the quoted range

- The brief (line 11) is accurate that his formula "1/(2 S0) + 1/(2 St)" is right for diploid S and half the standard correction when S is a pseudo-haploid allele count. It applies bin by bin: the Modern bin (mean 476 individuals called) is diploid-dominated, so for windows ending in Modern only one end of the correction is halved; for BA-Medieval both ends are pseudo-haploid. "Off by 2x" is therefore the term in pseudo-haploid bins, not the N_e.
- Line 125: "his numbers rise 8-24% when fixed". From the table on lines 73-79, (B)/(K) is: BA-Med 9,665/7,812 = +23.7%; EN-Modern +8.6%; EN-LN 5,954/4,706 = +26.5%; EN-BA 8,273/6,761 = +22.4%; EN-Iron 11,520/9,691 = +18.9%; EN-Med 9,302/8,410 = +10.6%; EN-Meso 872/866 = +0.7%. So 0.7-26.5%, not 8-24%. Against his published numbers the two headline windows rise 18.7% (9,665/8,139) and 6.8% (10,508/9,835), not 24% and 8.6%; the 24% and 8.6% are relative to this replication's (K).
- This does not help Day: the corrections raise N_e, as R4 says. It matters because a correction that changes a headline by 7-19% against what keruru published, and 1-26% across windows, should be stated that way once.

### F9 (MINOR) Credit to Day is complete in section 8 but not in the brief

The brief (lines 7-12) credits Day only by the transversion sentence at the end of item 3 and the "three orders not established" in item 6. Wins that are in section 8 or section 3 and absent from the brief:
- The start table reproduces to within 0.4 points on v62 (line 52), the only quantity that does, and (with the caveat the check gives) it matches the all-site set, not a transversion subset.
- His section 4.3 claim, "This confirms that essentially all "fixations" were completion events for alleles already near fixation—not new substitutions traversing the frequency spectrum", is confirmed: 98.8% of v62 eligible alleles start at 95-100% (line 132). The check shows that his qualitative description is right even where the count is not reproduced. It also shows, in the opposite direction, that near-fixation completion is what the critics said it was.
- The transversion class's pre-7000 share (0.98-0.99) is closer to his 0.9986 than the all-site 0.91.
- keruru's "three orders of magnitude" is not established, and his sampling correction is off (halved) for pseudo-haploid bins.
- Day's N_e near 2 (C5a) is excluded; this goes the other way and is correctly stated (line 85).

Fix: add one sentence "Day-side results" to the brief with the first three, and keep the exclusion of N_e near 2 next to them for symmetry.

### F10 (MINOR) Hard rule 2: the method sentences driving C1d are not in `quotes-day.md`

`quotes-day.md` holds Q52-Q55 (Z23046531 and the blog). The Z18525185 sentences used in the script docstring (section 3.1 sample, 3.3 fixation rule, 3.4 timing, 4.1 "insufficient coverage in intermediate time bins", 4.3 near-fixation, Appendix B) are not there, nor is Z23046531 section 5 ("Analysis scripts are available from the authors at Zenodo.") or section 2.3. C6 cites Z18525185 for the numbers but not for the method. Fix: add Q-entries with locators (section number, `zenodo-18525185.txt`), and one for each of the Z23046531 sentences in F2 and F3, so the reconstruction rests on registered quotes.

## Fairness judgement by question

- **Damage and filtering.** Partly fair. The transition-dominated excess is most plausibly mostly an old-versus-modern quality artefact, and the check says so with the right hedges (lines 66, 145). But Day's text gives no filter, transversion-only does not reproduce his table either, and the intermediate readings that could were not run. The label "irreproducible" is accurate for the readings tried; "false" (line 137) is not warranted for the damage-immune class. See F1, F4.
- **Version.** Fair. The patch difference is probably 161 non-European modern individuals; the modern-bin definition is the larger issue. See F5.
- **Scripts not found.** Not fair as framed. Wrong paper, Zenodo-only, one 404 artefact. "Not found on the records searched" is correct; "do not exist" is not supported. See F2.
- **Credit.** Present but buried; the brief should carry it. The start-table match, the transversion order of magnitude, keruru's correction and the unestablished "three orders" are all there, in sections 3 and 8. See F9.

## Summary for the integrator

| ID | Severity | Where | One-line fix |
|---|---|---|---|
| F1 | MAJOR | brief item 2, lines 8, 66, 137 | Add library-type and damage-rate readings (post hoc, labelled); reword "any reading" and "false under his own rule" |
| F2 | MAJOR | lines 7, 17, 137, section 1 | Scripts promise is in Z23046531, not Z18525185; search beyond Zenodo; redo versions lookup; "not found on records searched" |
| F3 | MAJOR | line 18, section 3 | Run Z23046531 section 2.2-2.4 as a calibration for 17,806 / 22,428 |
| F4 | MAJOR | lines 131, 140 | Resolve or flag the damage-immune comparison with neutral (863 vs 36-113) in one direction |
| F5 | MINOR | lines 21, 28, 143 | 17,629 - 17,468 = 161; vary the 0-500 BP definition |
| F6 | MINOR | line 53 | Add m = 25-40 or reword "no setting" |
| F7 | MINOR | brief, lines 9, 59-60 | 97.1% / 97.7%; factor 1.7-5.4; carry both classes in any one-liner |
| F8 | MINOR | lines 11, 125 | Scope of the 2x; range 0.7-26.5%; 18.7% / 6.8% against published |
| F9 | MINOR | brief | Add a short Day-side results sentence |
| F10 | MINOR | `quotes-day.md` | Register the Z18525185 method quotes and the two Z23046531 sentences |
