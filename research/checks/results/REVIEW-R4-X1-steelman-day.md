# REVIEW R4 X1: Day-side steelman

Reviewed: `research/checks/results/R4-X1-critic-arithmetic.md` (cited as X1 with its line numbers), `research/checks/x1_critic_arithmetic.py` (docstring), the critic and ally claim files, and the Day claim files with internal error verdicts (A3a, A5e, B6a, C6, G, G1a; non-sequiturs A2e, A5d, B3e, C, F1a and others). Raw sources were not needed beyond one read-only grep of `sources/raw/critics/ca-part3.html` (Camestros 1051). Nothing else edited, nothing committed. 2026-10-09.

## Verdict in brief

X1 is careful, mostly correct arithmetic, and unusually open about its own gaps (it names the 38,400 asymmetry, the Hancock 76.8 policy question, and the missed keruru band). It is **not yet a like-for-like standard**, for three reasons:

1. The "strict standard used for Day" is stated, then applied only to the two largest slips. At least five more critic slips fail it on X1's own tables, and Day's equally small slips (A5e, G1a, G) carry `arithmetic-error`.
2. The other half of the standard, `non-sequitur`, was never operationalised. All 67 pre-registered predictions are arithmetic letters (R/P/N). At least four critic conclusions do not follow from their authors' own stated premises on X1's own numbers (B5f, A3d, C5, the "match" claims). Only H5 (already coded) is retained.
3. "Errors cluster in fidelity, not arithmetic" is partly produced by the filing rule: unit, basis and unstated-input slips on the critic side go to fidelity or `immaterial`, while the same class on the Day side (A3a, A5e, G1a, C6) went to `arithmetic-error`.

Net: X1 closes **less** of the 0-versus-22 gap than its section 10 says ("Partly"). The honest conclusion is that the gap is at least partly a vocabulary and materiality artefact, which is what R5 draft 4.3 item 3 suspected. X1 does not decide the question.

Day-side credit I do not claim: A2h is a real, uncorrected, tenfold Day slip (38,400 vs 3,840) with no Day-side node. That is against Day and is correctly flagged by X1 (line 139).

---

## Findings

### 1. MAJOR: The stated "strict" standard is applied to 2 slips; at least 5 more critic slips fail it by X1's own tables

X1 line 7: "Under the strict standard used for Day ("any stated number that does not follow from the author's own inputs is an arithmetic-error, material or not") the critic and ally side gets **2 arithmetic-error suggestions (B5a comment-level, C5) and keeps 1 non-sequitur (H5)**".

X1 section 7, line 106 then lists as "Immaterial (no conclusion changes)": "Mansfield "about 10 times" (15.5x); Hancock "4e-5" for 4.6e-5, ... Nesslig20 0.51 for 0.50, 0.33 for 0.3333, "1/Ne" for "1/(2Ne)", the Barrick year; Camestros 1500 for 15,000 and 1051 for 1050 ... keruru's inconsistent Ne/N ratio ...".

"Material or not" in line 7 and "immaterial, so no verdict" in line 106 cannot both be the Day standard. Day's own verdicts do not use a materiality gate:

- A5e (`arithmetic-error`): "252,000/27,600 = 9.13, not 8 ... A 12% discrepancy in the paper's own sentence; immaterial to the 205M shortfall, but the figure does not reconcile." The file calls the slip immaterial and still codes it `arithmetic-error`.
- Critic counterpart A5c, Hancock: "you only expect four e to the neg5 mutations to fix per generation" and "like 22,000 generations". X1 row (line 41): 4.6e6 x 1e-11 = 4.6e-5, so "4e-5" is "13% low". Also 1/4e-5 = 25,000, not his "22,000". Verdict: `holds`, immaterial. That is the same size (12 vs 13 percent) and the same form (a stated figure that does not reconcile with the author's own sentence) as A5e.
- G (`arithmetic-error`): claim file R4 G1 note says the "(1.01)^1474 = 14.7x" is "still false as written, but 14.7 is recoverable (14.74 additive, 14.67 log)". A recoverable notation slip carries an error verdict. Critic counterpart, Nesslig20 Part II (X1 line 86): "P_fix = 1/Ne = 0.00005" with Ne = 1e4 is "arithmetic fine; symbol slip". Factor-2 formula slip, also recoverable: not coded.
- G1a (`arithmetic-error`): "5.3 x 14 = 74, not 66 ... unless 5.3 is an average over all populations, which the sentence does not say". A number that reconciles only under an unstated basis. Critic counterpart B5c/B5e (the "38M matches" statements): reconciles only on an event or haploid basis the speaker did not label (X1 line 48, line 50: "The basis of 75 is not stated"). Verdict: `holds`.
- C6 (`arithmetic-error`): abstract misdescribes its own table ("the table itself is internally consistent") and "Five different "fold" figures appear". Critic counterpart B2e, keruru: "The draft states the ratio three ways (1e-4, 4e-4, 8e-4)" (an 8x spread), `holds`; Camestros "1500/35" (numerator off 10x), `immaterial`.

Mitigations I accept: Hancock's wording is auto-caption (the transcript may read "4.6"), keruru's draft carries `[CHECK]` flags, and Camestros's 1051 line is hedged ("I may well be misreading it"). But Day's A5e, G1a, and G also have mitigating texts in their files, and none was excused.

**Fix:** Either (a) recode the Day side on X1's materiality rule (A5e, G1a, G, and the abstract-misdescription part of C6 become `holds` plus comment), or (b) apply the strict rule to the critics: A5c (4e-5), B5e (1/Ne), B2e (three ratios), Mansfield (10 vs 15.5), Camestros 1500/35 become `arithmetic-error` with an immaterial comment, giving at least 7, not 2. Whichever rule is chosen, R5 4.1 must use it for both columns. State the resulting like-for-like rate: Day's 6 arithmetic-error among 81 files with a `derived:` or "Arithmetic audit" block (7%), versus a strict-rule 7 among about 45 numeric critic and ally files (16%). I computed the 81 by grep; X1 line 157 says the like-for-like count "was not computed".

### 2. MAJOR: The non-sequitur test was not run on the critics

X1 section 2 defines `non-sequitur` ("if the conclusion does not follow from the author's own premises"), but the script's 67 predictions are only R/P/N arithmetic outcomes. The write-up retains one critic-side non-sequitur (H5), which was already coded. Day received 16 non-sequitur verdicts, many of the form "the conclusion is stronger than the premise supports" (A5d: "'not bottlenecked by mutation supply' does not follow from a positive sublinear response"; A2e "ceiling"; Gc "the 'match' is circular if fitted"). The same test on X1's own numbers:

**2a. B5f (Dumb-and-Dumber).** Claim file: "The gap is under a factor of two" and "takes the neutral fixation time as 4Ne ("40,000-132,000 generations") and notes 252,000 is well above it". His premise: "It needs the elapsed time to be long compared with the fixation time." X1 line 51 recomputes his own lag: "8.14M or 4.61M, gap 2.2x or 3.8x". So "under a factor of two" fails with the lag he himself states, and 132,000 is 52% of 252,000, which is not "long compared with". X1 verdict: `holds / accurate`, "Immaterial". The 2.2x to 3.8x gap is larger than the "factor of two" that the conclusion is about, and Day's B1a subtraction is exactly the lag Day is criticised for being "circular" about (B3h). **Fix:** `non-sequitur` (or `pending` with comment) for the "under a factor of two" sentence.

**2b. A3d (Hancock, "this basic math is off by a factor of two" ... "this really should be at least 360").** X1 line 35: "205e6/191 = 1.073M and 410e6/(2 x 191) = 1.073M (invariant). Day's text: "apportioned symmetrically to the human lineage" (confirmed)". So against MITTENS 3.0 the correction changes nothing, and X1 section 10 says "Hancock misreads the unit of Day's 205M". Verdict `holds / partial`. A conclusion that does not follow (against the 3.0 text) is a `non-sequitur`, and a misreading of an explicit sentence is `misread`, not `partial` (compare A3a/A3x1 `misread`, Zeng s `misread`). The only defence (Duffy's slide compared 180 with a two-lineage total; "the slide text is not in the repo") makes it unverifiable, not `holds`. **Fix:** internal `pending` or `non-sequitur`, fidelity `misread` for the 3.0 target; flag the slide as the open item.

**2c. C5 (keruru).** Claim: "Finding zero is not a coin landing on its edge. Finding one would have been the falsification." and "expected number of fixations is somewhere near 10^-29". X1's own table (line 58): "uniform 0.1 to 0.9: 2.6e-4; uniform 0.1 to 0.99: 1.3e3" and "the expected count is set by the frequency spectrum's top edge". An expectation that spans 5e-39 to 1.3e3 depending on an unstated spectrum cannot support "finding one would have been the falsification". The repo's own C1c (`R4-C1c.md` "Result in brief" 3) finds the neutral model at Ne = 1e4 gives "1.5k-3.9k (70-190x Day's 21)". Day's aDNA umbrella `C` is `non-sequitur` for the mirror-image defect: "neutral also predicts ~0 from <50% and 0.04-0.11 from 50-90%". X1 labels C5 "immaterial: direction conservative" in the main table but lists it in section 7 as slip number 1 under "Slips that carry (part of) an argument". Those two statements contradict each other. Also, "conservative" relative to which conclusion? The slip makes the per-locus figure too large, so it is conservative only for "zero is expected" at p = 0.5, and not for the integrated count. **Fix:** drop "immaterial"; code C5 `arithmetic-error` (per-locus) plus `non-sequitur` (the integrated "10^-29 so the window cannot discriminate" step, absent a stated spectrum).

**2d. The "38M matches" claims (B5c, B5e; B5f's 9.7M vs 17.5M).** X1 section 6 (line 97): the double count "lands on the right value for the wrong reason ... Both authors flag part of the issue". Day's B6a is `arithmetic-error` plus `contradicted` for the same term, and Day's Gc is `non-sequitur` for a "match" that is "circular if fitted". The B5f claim file itself says "the 17.5M comparator includes polymorphism and ignores the ancestral term", i.e. an observed total that contains the ancestral term is compared with a supply that excludes it. This is an internal defect (a comparison of unlike quantities inside the author's own argument), not only an external one. The R5 draft asked exactly this (4.3 item 3: "R5 should decide whether B5c, B5e and B5b should be re-read under the internal column"). X1 answers `holds / partial` for all three without an inferential test. **Fix:** explicit sentence-level verdict: "match" statement `non-sequitur` on the SNV basis (the double count), `holds` on the event basis; say which basis each author used, or say it is not stated (Nesslig20).

**2e (minor, see finding 8).** McCarthy's "exact correct result" and G3's "527 sd" use the top of his own range.

### 3. MAJOR: Hancock's unit misreading is filed `partial`; X1's own text calls it a misread

X1 section 10 (line 151): "Hancock misreads the unit of Day's 205M (Day's text is explicit: apportioned symmetrically)". X1 section 7 (line 111): the 407 per generation "halves an already per-lineage figure", so the gap is 10.6x, not "about 5x". Suggested verdicts: A3d `partial`, B5c `partial`. In the Day column, the same class of event, a source sentence misread, is `misread` (A3x1/A3a, F3a Zeng 2021, Langergraber 2012). Two details soften this: (i) the error runs against Hancock's own interest, and (ii) the repo holds only auto-captions. Both are true, and neither changes the vocabulary: `misread` describes what he did to the text, whoever it helps. The repo's own harvest note ("~5x the 76.8 neutral supply", `quotes-critics.md` GG-11) has carried the understated 5x into the corpus, so it should be corrected there too, but that is the lead's file.

**Fix:** A3d and B5c fidelity `misread` (unit of Day's 205M), with the comment that the correction is 2x against Hancock; keep A5c `partial` (uncited low input) since there is no source sentence to misread.

### 4. MAJOR: The headline credit is over-stated: "34 of 45 reproduce clean" and "pivotal identities verify exactly"

a. **Count.** The same X1 table (section 4, column "Suggested internal / fidelity") has 10 `partial`, 4 `unverifiable`, 2 `pending`, plus B5a and C5 as arithmetic errors, i.e. 17 rows carrying some flag in the suggested-verdict column. Only 16 of the 45 are `holds / accurate` (A2c, A2d, A2h, A5, A5b, B5, B5f, B5h, B6b, B7, B7c, D14, E5, F4, G2b, G3); 10 more are `holds / n/a` (fidelity not scored). "34 clean" (line 7) means "the arithmetic reproduces", which is the narrow axis the review set out to test, but section 1 presents it as the headline for the whole side. The table gives about 28 clean on any column at most, and 16 on both.

b. **Pre-registration weight.** Script docstring: "Predictions that lean on claim-file arithmetic are marked `[cf]` (40 of 67) and are not independent" (X1 line 163). So "67 of 67 match" is mostly claim-file arithmetic being re-run by the same pipeline, and of the 26 `[new]` predictions the one genuinely independent numeric band was missed (keruru, 41x). The scorecard is not evidence of calibration.

c. **Credit for what Day accepts.** X1 section 10 (line 144): "The core identities hold exactly: k = mu (sympy, and exact chains), P_fix = 1/(2N_census) ...". B5's own claim file records: "Acceptance by Day's side: Z22129121 "this paper accepts it throughout"; blog 2026-08-27 (B3g)", and B3g is Day's concession that Ne does not enter the Kimura identity. Verifying an identity that both sides accept is real work but is not a point for either side. The disputed step is applicability to the 252,000-generation window from a contracted ancestral population, where the repo's own B1c finds "per-lineage excess 1.9-4.0x" and the B5 claim file says "The critics' stated totals assume stationarity". F1 is marked "exact at steady state (full pipe, B6)" in the same way, and B6 says the full pipe "needs 4 Ne_anc generations before the split (4e4 to 7.9e5)". The credit text should say the identity is exact and conceded, and that the premise it needs (stationarity) is the open item.

**Fix:** report both axes (arithmetic reproduces: 34 of 45; holds and accurate: 16 of 45), mark the credit for k = mu and P_fix as "undisputed identity, no side gains", and move the pre-registered-match statement to "40 of 67 predictions were copied from claim-file arithmetic".

### 5. MAJOR: "Fidelity, not arithmetic" is partly the filing rule

X1 line 7: "The errors found are real but small and cluster in the **fidelity column** (basis, units, uncited or low inputs), not in arithmetic from stated inputs." Day's `arithmetic-error` verdicts include the same kinds of slip: A3a (basis: 410M mixes bp and events; and the parts do not sum), G1a (basis: 5.3 reconciles only if it is a different average), C6 (denominator and unit of the 630), A5e (rounded count). Had they been filed by X1's rule, A3a, G1a, A5e, and the "630 denominator" part of C6 would be `fidelity` (basis/unit) or `immaterial`, and the Day column would shrink from 6 `arithmetic-error` to about 2 (B6a, and the abstract/table mismatch in C6). Conversely, filed by Day's rule, the critic basis and unit rows (B5c 407, B5e 75, A5c 1e-11, B2e) become `arithmetic-error`. Either filing is defensible. The claim "cluster in fidelity" is true only for the critic filing.

**Fix:** drop the cluster sentence or rewrite it as: "by the rule X1 applied to critics, the Day column would show N fewer arithmetic errors". Add a two-column recode table in R5 (Day nodes recoded by X1's rule; critic nodes recoded by Day's rule), so the reader can see which way the optical gap moves.

### 6. MAJOR (reverse check): Day nodes marked error that X1's standard would call immaterial

X1 asked the reverse question only for s6.4. Applying X1's own gate ("material only if it changes a headline or a conclusion by more than ~2x, or carries an argument", X1 line 13):

| Day node | Day verdict basis | X1 gate |
|---|---|---|
| A5e | 9.13 vs "8", 12%, "immaterial to the 205M shortfall" (claim file) | immaterial: would be `holds` plus comment |
| G1a | 5.3 x 14 = 74 vs 66, 12%; reconciles if 5.3 is an all-population average | immaterial or fidelity |
| G | "(1.01)^1474 = 14.7x" notation, 14.7 recoverable (R4 G1 note: "14.7 is recoverable ... the audit's earlier 'mixed scales / 10^672' framing is withdrawn") | immaterial; the open issue is best/worst vs all/none, which is external |
| A3a | "stated parts do not sum to 410M", yet X1 itself credits the Reddit reconstruction "2 x 187 + 35 = 409M" as reproducing Day's total (X1 line 145, R05) | the number reproduces under a unit reading; the defect is basis (`fidelity: misread`, already coded), so `arithmetic-error` double-counts |
| C6 | abstract's "single 2,000-year window" vs table 53.6% (prose mislabel; "the table itself is internally consistent"); the "630 vs 21" denominator point is better filed non-sequitur or external | one part immaterial |
| B6a | "less than half" is 0.6 (20%) and the sign flips on IR's own table | carries the argument (the 1.2M vs 2.4M removal flips "net reduces"): stays |

A Day-side consistency point that cuts the other way and should be recorded: H1 (Term 3 retraction, 7.7 corrected to 17.1) is `holds` with an arithmetic comment, i.e. a self-corrected Day slip got the same pass as Hancock's 76.8. So the self-correction policy is applied on both sides; A5e, G1a, and G were not self-corrected.

**Fix:** report that 3 of Day's 6 `arithmetic-error` verdicts (A5e, G1a, G) are immaterial under X1's gate, and that A3a duplicates a fidelity verdict. This should appear in R5 4.1 next to the 22.

### 7. MINOR: Four `pending` to `holds` upgrades rest on premises the claim itself leaves open

- B6c and G2c (Hancock, "serial predicts no variation"): X1 says "whether Day's model is serial is G1/F1a". Day's F1a says it is not. Upgrading to `holds` is a conditional ("if serial then no variation"), true as logic. Day's G2g got `non-sequitur` because "the premise fails". Treat the conditional the same way on both sides: `holds` for the conditional, with the premise recorded as contested, which G2c's current `pending` already does implicitly. Suggest keeping `pending` with the comment unless the premise is settled.
- B4g (keruru, "fossil-calibrated rate is about twice the pedigree rate"): X1 line 44: "the factor 2 disappears once the ancestral term is subtracted". The claim file's own implicit assumption is "All divergence is accumulated after the split; ancestral coalescence ignored." That is the same omission Day is faulted for in B6a/B1a. `holds / unverifiable` is generous; `pending` stands until B4a is applied.
- E5: `holds / accurate` is fine, but the claim is "-906 is not a count", whose artefact reading X1 itself labels external.

**Fix:** leave B6c, G2c, B4g at `pending` with X1's comment; E5 as suggested.

### 8. MINOR: Correct critic results credited without their stated sensitivities

- G3 "credit: Day's 10^-86,000,000 is exact" and "20M is 527 sd below": that sd depends on McCarthy's 22.5M mean. X1's own M06 (script) and B5a row (line 46): "His own 60 to 100 range with 97% non-deleterious gives 13.1 to 21.8M, so 22.5M uses the top of his range". At 13.1M the mean sits below 20M and "P_any of at least 20M" is about 0. The sensitivity is carried in B5a and not in the G3 or F1b rows. Same for "exact correct result" (McCarthy "Vox Day Responds"): 20.0M from a 13.1M to 21.8M range is not "exact".
- B5b: Mansfield's 1 per generation is exact; the 44x shortfall is "the illustration's own limit" (X1 line 47), but X1 then notes the share needed is 0.89 and "way under the actual proportion" has no figure. A claim whose illustration reaches only 2.2% of the needed total (450,000 of 20M) and whose closure needs a share nobody cites is not "credit: exact"; it is an exact identity with an uncited premise. Already `partial`, so this is a wording point.
- B3i/B7c/G5 are genuinely correct and I do not dispute the credit.

**Fix:** carry the 13.1 to 21.8M range into the G3 and F1b rows; reword the Mansfield credit.

### 9. MINOR: Camestros's 1051 is 472 if d applies

X1 section 5 (line 87): "450,000/428.6 = 1,050 (one off; d omitted, with d = 0.45: 472)", labelled "immaterial slips". Under X1's own gate (">~2x") 1,051 vs 472 is 2.2x. Camestros's line is hedged and exploratory ("I may well be misreading it"), and he does not state d for that line, so I do not argue arithmetic-error. Record it as "model omits d: 2.2x" rather than a typo.

### 10. MINOR: Allies and the Day column are mixed in the denominator

X1 counts "critic and ally" claims together (66 files). The R5 comparison is Day (112) vs critics (51) vs allies (15). Allies are Day-aligned, so their slips (Hössjer 15,875 vs 15,800 rounding, D8's lottery analogy 10^-424,764 off, H5 non-sequitur) are Day-side evidence. D8's analogy is the largest numeric discrepancy in the whole X1 table (about 420,000 orders), is on Day's blog, and is `n/a` because "the speaker is unclear". That favours the critics' count of Day-side weakness, not Day's, and I report it because the steelman should not hide it. The recoded Day-side count should include D8 as an ally node if the lead wants the full column.

---

## What X1 gets right (fairness, for the Day-side record)

- It reproduces and credits several Day-side-relevant facts: the 38,400 slip is real (A2h), Day's per-lineage 205M reading is confirmed against Hancock, Hössjer's d is carried into his neutral supply (so the ally result is less independent than framed), Mansfield's 44x is the illustration's own limit, and "ancestral polymorphism is a rounding error" is wrong at Yoo's Ne_anc but not at Ne = 1e4 (section 10 "Neither side").
- It labels McCarthy's 35M, the 25 y / 20 y mix, and keruru's probabilities as real slips on the critic side and suggests recoding two of them. It reports the missed pre-registered band and does not hide the policy question.
- Its statement that the denominators are not comparable is correct and should be kept, but it would be stronger with the computed like-for-like rate suggested in finding 1.

## Overall

X1 is fair about what it computed and unfair only by omission and filing. Its arithmetic is sound. Its conclusions on balance ("Partly" closes the gap; "cluster in fidelity") do not follow from its tables once the strict rule is applied evenly and the non-sequitur half is run. The balance gap should be reported as unresolved, with: the strict-rule recount (at least 7 critic slips, not 2), the materiality-rule recode of Day (3 of 6 arithmetic-errors immaterial), and the sentence-level non-sequitur candidates (B5f, A3d, C5, the "match" statements).
