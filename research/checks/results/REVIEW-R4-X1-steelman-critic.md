# REVIEW R4 X1: critic-side steelman of the critic and ally arithmetic audit

Reviewed: `research/checks/results/R4-X1-critic-arithmetic.md` (cited below as "X1 line N"), `research/checks/x1_critic_arithmetic.py`, the critic claim files (B5a, B5b, B5c, B5e, C5, A5c, A3d), `docs/research/sources/quotes-critics.md`, and the raw texts under `sources/raw/` (read only: McCarthy post and comment JSON, Peaceful Science topics 18094 and 18095, keruru's "The Epicycle Was Elsewhere"). Written 2026-10-09. No other file edited, nothing committed.

## Verdict on fairness

X1 is fair in method and in most of its 45 rows. The recomputations are real, the pre-registration miss is reported, the repo's own 1.2e-46 is named as wrong, the Day-side counterpart (s6.4's 38,400) is flagged as an open policy question, and the critics' pivotal results are verified. I found no row where the arithmetic itself is wrong.

It is not fair in four places, all in the step from "recomputed" to "suggested verdict":
1. B5a is made an `arithmetic-error` on the strength of a comment that is not among the claim's statements, for a slip below X1's own 2x materiality line (finding 1).
2. C5 is made an `arithmetic-error` for a deep-tail approximation whose method is not on record, and the label is stronger than the repo's accepted C1c fix-pass wording (finding 2).
3. The "material or not" strict rule is applied to critics in the suggested-changes table while the larger, better-documented Day-side slip is left as a question, so the 0 to 2 versus 22 comparison is not like-for-like (finding 3).
4. B5c's fidelity is downgraded for a unit reading of Day's 205M that X1 cannot tie to the video and that is not in the claim's statements (finding 4).

The informal-source fidelity downgrades (B5b, B5e, A5c) are a category mismatch and are not applied to Day's uncited inputs (finding 5).

## Findings

### 1. MAJOR. B5a `arithmetic-error` is scored from a statement the claim does not contain, and it is immaterial by X1's own rule

**Where.** X1 line 46 (row B5a), line 123 (suggested), line 7 (headline), lines 96 and 113.

**What X1 says.** "arithmetic-error (comment-level; the post figure holds)" and, for M03, "a plain slip (75% off; the 35M headline vs 180 is unaffected)".

**Evidence.**
- B5a's three verbatim statements (claim file `B5a-mccarthy-22-5-million.md`, "Statement") are the post's "450 billion new mutations", "22.5 million fixed mutations" and "20 million fixations". All three are right by X1's own recomputation. The 35M sits in a different comment, RF-6, comment 340149310 under "Vox Day Responds". RF-6 is already flagged in `quotes-critics.md` ("ARITHMETIC FLAG (harvester, derived) ... Critic-side slip"). It is not a B5a statement.
- X1's own materiality definition (line 13) is "changes a headline or a conclusion by more than ~2x, or carries an argument". The script's pre-registration records 35M versus 20M as "factor 1.75". The comment's sentence is "That's 35 million right there, not 180"; both 20M and 35M are four orders above 180, so no argument rests on the digit. By X1's rule this is immaterial, yet it earns the one verdict word that the repo uses for Day's A3a ("stated parts do not sum to 410M").
- M02, the 25 y / 20 y mix, is not comment-only. The same passage is in the post "Vox Day Responds" (para 21), which is B5a's third quote, so X1's "post figure holds" is inconsistent with its own M02 locator. More important, the 25 y is not McCarthy's input. He introduces it with "Anyway, using his numbers", after quoting Day's own reply: "At 25 years per generation, that's 1,000,000 years per neutral fixation." The 50,000/yr comes from the earlier 20 y inputs, which are also Day's (9 My, 100 per newborn). The mix reflects Day's drifting inputs. The effect is 2.4% on the 20 y reading and 20% on the 25 y reading, both under 2x.
- Of the six Day-side arithmetic-error nodes (A3a, B6a, A5e, C6, G1a, G-bernoulli-barrier), the five whose sources I checked (B6a, A5e, C6, G1a, G-bernoulli-barrier) cite papers or a blog post (Zenodo 22903977, 23003785, 18525185, 18167588; a voxday.net post); A3a is a MITTENS paper claim. None of them rests on a comment-thread reply, so the comment-level rule appears to be new and to apply only to critics. I did not find Day's own comment and reply statements scored this way.

**Fix.**
- Keep B5a `internal: holds`. Add a comment: "RF-6 (comment 340149310) prints '400 billion x 1/20000 = 35 million' (2.0e7; factor 1.75; immaterial; same thread gives 20M); comment 337116873 and post para 21 mix Day's 25 y with the 20 y-derived 50,000/yr (2.4% to 20%)".
- If the project wants the slip counted, make RF-6 its own claim file or argmap node, tagged comment-level and immaterial. Do not put it on B5a or F1b.
- Reword X1 line 7 to say "two immaterial comment-level slips" and remove B5a from the arithmetic-error tally in lines 1, 123 and 157.

### 2. MAJOR. C5 `arithmetic-error` rests on a method that is not on record, and it reverses the accepted C1c wording

**Where.** X1 line 58, line 125, lines 101 and 109.

**What X1 says.** "arithmetic-error (immaterial: direction conservative)". The definition at line 11 is "arithmetic-error if a stated number is wrong from the author's own stated inputs".

**Evidence.**
- keruru states a method only as "Running the absorption probabilities at that scaling". X1 itself says "his code not retrieved" (line 57). A 14-sigma tail has no unique textbook value. The script prints one-boundary Gaussian 6.2e-47, reflection-doubled 1.24e-46 and exact 5.1e-45 (`raw/x1_results.out` line 58), and X1 reports the exact value moving with M (5.1e-44 at 2N = 5,000 down to 3.2e-45 at 40,000). I ran common variance conventions (Gaussian at p = 0.5): p(1-p)t/(2Ne) gives 3e-20, p(1-p)t/(4Ne) gives 2e-38, and 4e-35 corresponds to z = 12.3. keruru's value sits inside this convention-dependent band, so the discrepancy cannot be called arithmetic from his stated inputs. "Not reproduced" is correct; "arithmetic-error" is not shown.
- The repo's own approach treated the same gap as negligible. The C5 claim file says "The two values differ by 11 orders; both are negligible". The C1c fix pass (`R4-C1c.md` line 135) proposed "internal `holds` for the statistic it addresses (intermediate starts); comment that the three figures do not agree". X1 reverses that without saying it does.
- The repo's own number in that same sentence was off by 41x against the exact chain, and by about 17x against X1's extrapolated diffusion limit (about 2e-45). The two numbers are different in magnitude of error but of the same kind (a deep-tail approximation), and only one is labelled an error.
- X1's §7 item 1 says the "stated *mechanism* ... depends on a spectrum he does not state" and §10 says "keruru's '1e-29' is a stated spectrum-free number that depends on the spectrum's top edge". keruru states the spectrum: "starting from intermediate frequencies". X1's own table (line 58, `x1_results.out` K-03c and K-03d) gives uniform 0.1 to 0.9 as 2.6e-4 total expected fixations over a million loci, and uniform 0.5 to 0.9 as 5.3e-4. Zero is still the prediction by 3 to 4 orders. keruru's sentence "Only alleles already above about 0.99 have any meaningful chance at all" is confirmed by X1 (0.9: 3.7e-8; 0.95: 2.2e-4; 0.99: 0.19). The 1.3e3 figure needs loci to reach 0.99, which is not "intermediate". The "mechanism" slip therefore does not "carry an argument" on X1's own numbers, and keruru's 1e-29 is internally consistent as 1e6 x 4e-35.
- keruru withdrew the aDNA claim in the same post (KR-04), and C5 is `load_bearing: false`.

**Fix.**
- C5 internal: `holds` for the conclusion ("zero is the neutral prediction from intermediate starts"), with a comment: "per-locus tail 4e-35 not reproduced (exact WF 5.1e-45; method unstated, deep-tail values vary by tens of orders with the variance convention); 1e-29 = 1e6 x 4e-35; 0.99 statement reproduces". Or keep `pending`. Do not use `arithmetic-error`.
- Reword X1 lines 109 and 152: "the count is dominated by the top edge of the start spectrum; for 'intermediate' = 0.1 to 0.9 it is 2.6e-4, so zero is still expected".
- Say in the C5 row that this reverses the C1c fix-pass wording and why.

### 3. MAJOR. The strict "material or not" rule is applied one-sidedly in the suggested-changes table, and the headline comparison mixes denominators

**Where.** X1 line 7, lines 119-137, line 139, line 157.

**What X1 says.** "Under the strict standard used for Day ... the critic and ally side gets 2 arithmetic-error suggestions" and, at line 139, "Policy question for the lead ... Apply the same rule to Day's slips. One is currently logged only on the critic side: s6.4's 38,400".

**Evidence.**
- The s6.4 slip is 10x (3,840 printed as 38,400), is confirmed against raw Z23003785 by X1, and feeds "0.02 and 1e-17 figures built on it". That is larger than every critic slip X1 found and sits in Day's own paper. It is the target of a critic's correct catch (A2h) and has no Day-side node. X1 raises it only as a question; the §9 table of "suggested verdict changes" has no Day row.
- The comparison "0 to 2 ... against 22 of 112 for Day" (line 157) compares verdicts that include immaterial slips on the critic side with an unaudited-for-materiality Day count. X1 admits the denominators are not comparable but still headlines the numbers. A3a, A5e, G1a, C6 and the others were not re-read for materiality in this check. If any of the six Day `arithmetic-error` nodes is an immaterial slip, the like-for-like count changes. The repo's own tolerance for Day is visible: `A-mittens-formula.md` accepts 91.4 printed as 91 and 91,806 printed as 91,600 as "Yes (rounding)".
- Tolerance is not stated and not uniform. Camestros's "1051 fixed mutations in Day's model" is called immaterial in line 87 (and §7) although the same line says "with d = 0.45: 472", a 2.2x difference, above X1's own 2x line. Mansfield's "about 10 times" (15.5x, 55% off) is immaterial; McCarthy's 1.75x is an error.
- X1 sections 7 lists Nesslig20's 0.51 for 0.503, 0.33 for 0.3333 and a Barrick year as critic "slips"; there is no matching list of Day's rounding or typo-level slips.

**Fix.**
- Add to §9 the Day-side rows that the same rule produces (at minimum: s6.4 38,400 and the 0.02 and 1e-17 numbers built on it), or hold the two critic labels until both land in the same integration.
- Report every slip on both sides in one table with relative error and a stated tolerance (for example: "arithmetic-error needs a printed number that differs from the author's own inputs by more than rounding, with the method on record"), and split all 22 + 2 by material / immaterial.
- Replace the "0 to 2 against 22 of 112" sentence in lines 1 and 157 with that table.

### 4. MAJOR. B5c fidelity downgrade for the 205M "unit slip" is out of the claim's scope and not established

**Where.** X1 line 48, line 126 (`holds / partial`), line 111 (§7 item 3), line 151.

**What X1 says.** "**Unit slip:** '407 per generation' divides Day's per-lineage 205M by both lineages' generations; per lineage it is 813, so the gap to 76.8 is 10.6x" and, in §10 (Day), "Hancock misreads the unit of Day's 205M".

**Evidence.**
- B5c's verbatim statements are 76.8, the diploid/haploid correction, 152 and "about 38 million". The 205M and 407 appear only in the claim file's "Formal statement" paragraph (written by the harvester), not in a statement. The 205M reading belongs to A3x / A3d.
- The verbatim line is "when you divide this out over 200 205 million you get something like 407" (GG-11, `quotes-critics.md`). The auto-caption is garbled around "200". X1 line 161 itself says "GG-12 and the '5x' cannot be tied to the full sentence". The "about 5x" is the harvest note's phrasing, not Hancock's. The repo's balance ledger already records this ("His 205M→407/gen halves an already per-lineage figure"), so this is not a new X1 finding.
- On the premise Hancock appears to hold (205M is a two-lineage total, which he treats as a count of "differences", GG-10), 205e6/(2 x 252,000) = 407 against a per-lineage 76.8 is a consistent comparison, and his ~5x equals 205M against his two-lineage 38.7M. X1 judges that premise against MITTENS 3.0 text, but the ledger says "Hancock's video answers the Duffy version (22 Sep), not MITTENS 3.0", and A3d says "the repo cannot confirm which comparison Duffy's slide made" and "the slide text is not in the repo".
- The error, if it is one, runs against the critic's interest and X1 says it "does not affect the shortfall ratio" (line 111).
- Credit missing: Hancock's substantive point on 205M ("suspects 205M includes gap divergences and is not a point-mutation count", GG-10) is what GAP-07/07b support (205M is a base-pair figure; 21.05M events per lineage; 9.7x raw, bracket 7-14x). His event-basis supply 2 x 252,000 x 76 = 38.3M also sits within 10% of the direct alignment count of 42.1M events (GAP-07b). X1 mentions the 40M comparison only in a table cell.

**Fix.**
- B5c fidelity `n/a` (or `accurate` for the 76 / 152 / 38M statements). Move the 205M unit question to A3x or A3d as "reading of Day's 205M: unit unverifiable (video is auto-caption only; version answered not established)".
- Delete "Hancock misreads the unit of Day's 205M" from §10 (Day), or soften it to "if Hancock read 205M as a two-lineage total, the per-lineage gap is 10.6x; the transcript and version are unavailable".
- Add a credit bullet for GG-10 and the event-basis agreement with the direct count.

### 5. MAJOR. Uncited inputs in informal sources become `partial` on the critic side, which is the wrong word and is not applied to Day

**Where.** X1 lines 47, 50, 49 and 126-129.

**What X1 says.** B5b "holds / partial (100 per zygote and the neutral share are uncited)", B5e "holds / **partial** (basis of 75 unstated, uncited)", but B5d "holds / unverifiable (relayed, 30 per generation uncited)".

**Evidence.**
- In the repo, `fidelity` is "inputs cited and read correctly". B5b's own claim file says "Primary literature: none cited | n/a | n/a", so nothing was cited to be read partially. Uncited inputs are `unverifiable` (the word X1 uses for B5d and the repo uses for Day's A5e: "derivation is in the book appendix, not harvested"). X1 uses two different words for the same defect inside one table.
- The standard is a peer-review one. B5b is a YouTube comment under a video; X1 itself says the 2% is an illustration with "way under the actual proportion". Nesslig20 describes his post as "this rough calculation". Hancock calls his own calculation "back of the napkin" (GG-16). Meanwhile 48 Day-side claim files carry fidelity `n/a` and the balance ledger records that Day's Hard Limits and aDNA papers "have no references"; those uncited inputs did not trigger `partial`. I did not audit every Day file, but the rule is stated for critics only.
- A5c: Hancock's "four e to the neg5" is spoken auto-caption for 4.6e-5 (22,000 gens is 1/4.6e-5), so the "13% low" is truncation in speech. The 1e-11 input being 8.9x below the measured rate was already in the balance ledger ("below the measured 8.9e-11") and the claim file. And the sub-argument's conclusion survives the correction: at 8.9e-11 the all-neutral ceiling is 2,439 generations per fixation, and the LTEE's observed 1,322 is still 1.8x faster than that ceiling. X1's §10 phrase "fits Day's hitchhiker reading" is an external judgement made in a fidelity check.

**Fix.**
- B5b, B5e: `n/a` with a comment "input uncited"; or `unverifiable`, consistently with B5d. Reserve `partial` for a cited work read with some error.
- A5c: keep `holds`; add "1e-11 vs measured 8.9e-11 (already recorded); at 8.9e-11 the neutral ceiling is 2,439 gens, still 1.8x slower than observed 1,322".
- Before landing any of these, run the same "uncited input to `partial`/`unverifiable`" sweep over Day-side numeric nodes, or state that it was not done.

### 6. MINOR. Nesslig20's 75: the basis is stated; the derivation is not

**Where.** X1 line 50, line 99, line 112 (§7 item 4).

**Evidence.** The post (topic 18094, §2.1) defines "the neutral mutation rate per haploid genome per generation [μ_G]", then "Estimates vary from 100 to 200 per generation. Let's assume a conservative neutral mutation rate of [μ_G = 75]". So the basis (per haploid genome) is stated; what is missing is how 75 relates to 100-200. Two readings are natural: 75 as a haploid event count (150 per newborn, inside Hancock's 98-206 range, which X1 itself notes), or 75 below the quoted range, which is what "conservative" says. The 18.9M alternative needs a third reading (75 as a zygote count) that contradicts the post's own definition. X1 also calls "75 ... 1.95x the SNV pedigree haploid value", but Nesslig20's comparator is "1-2% difference ... due to single-nucleotide differences" (31-62M), an event-versus-SNV mixing X1 already assigns to the B5c / B4a double count.

**Fix.** Change line 50 and line 99 to "basis stated (per haploid genome, §2.1); derivation of 75 from the 100-200 range not given; 18.9M is the zygote-count alternative the text does not support". Move B5e from `partial` to `n/a` / `unverifiable` as in finding 5. Remove §7 item 4's "2x" unless the zygote reading is shown to be the natural one.

### 7. MINOR. Attribution slips inside X1: a hypothetical objector's words, and allies counted in the critic tally

**Where.** X1 line 86 and line 106 (§7), line 7.

**Evidence.**
- "P_fix = 1/Ne = 0.00005" in Part II is inside the sentence "Someone might say: 'But wait! ... The probability would be [P_fix = 1/N_e = 0.00005] even if it was entirely neutral'". It is the objector's formulation that Nesslig20 then rebuts (Texas sharpshooter), not his own claim. Listing it as a Nesslig20 symbol slip (line 106) misattributes it. The same applies to using "1/500" as k in a stated-for-argument reductio ("for the sake of the argument").
- Of the 45 rows, 35 are critic claims and 10 are ally claims (A4c, A5a, B5h, D8, D14, G1b, G2b, H5, ROOT-H, ROOT-K). The "2 do not reproduce" are C5 (critic) and D8 (ally; a Milton blockquote on Day's blog with no identified author and "no calculation depends on it", line 60). The headline "critic numbers" therefore includes one ally-side rhetorical blockquote. Conversely B5a, whose labelled verdict is `arithmetic-error`, is counted among the 9 "flagged" rather than the 2 "not reproduce", so the headline and the verdict table disagree.

**Fix.** Report critics and allies separately in lines 1 and 157 (critic-only: 35 rows, one numeric non-reproduction, C5, and the immaterial 35M comment slip; ally-only: D8, H5). Remove the Nesslig20 "1/Ne" slip from §7.

### 8. MINOR. Credit order, and a missing credit line

**Where.** X1 line 7 (§1), lines 143-147 (§10).

**Evidence.** The §1 paragraph spends its last third on "2 arithmetic-error suggestions ... against 0 / 0 recorded now", and only closes with "The critics' pivotal identities (k = mu, P_fix = 1/(2N_census), Matev's N/Ne reductio) verify exactly." Credit appears in full in §10, but §10 follows the table, and the §10 "Day (credited too)" list has four bullets of critic weakness against one "Neither side". Missing credits I found: (a) Hancock's GG-10 suspicion and event-basis agreement (finding 4); (b) Nesslig20's exact CDF percentiles matched an exact Wright-Fisher recursion to 0.002 (in §10, but not in §1); (c) keruru's 0.99 statement reproduced exactly (K-03c = R in the script, absent from the C5 row's comment); (d) McCarthy's 22.5M, 527-sd and 10^-86,020,600 are exact (G3), which sits next to, not behind, the 35M comment slip in the B5a row.

**Fix.** Lead §1 with the identities and the 34 clean rows, then the slips. Add (a), (c) to the C5 and B5c rows. Keep the Day-credit list but state its counterpart for each bullet.

### 9. MINOR. The repo's own errors are owned, but not at the same level and not in the places they live

**Where.** X1 lines 22, 58, 101, 125, 155.

**Evidence.** X1 does own the 41x miss ("The audit's own earlier C5 number (1.2e-46) was 41x too low and is corrected here") and reports its own missed band and discarded first draft (§3). Credit for that. Gaps: (a) the 1.2e-46 is cited as live in the C5 claim file line 34, `R4-C1c.md` lines 135 and 160, and `REVIEW-R4-C1c-steelman-critic.md` lines 142 and 150, but X1 lists only "replace the repo's derived 1.2e-46" in a table cell; there is no list of locators. (b) X1 §3 says "the diffusion limit is probably about 2e-45", so against the limit the repo is about 17x low, but §6 and §10 use 41x. State both and say that the exact value depends on M. (c) The C1c fix pass's `holds` wording (finding 2) is reversed without a note. (d) The repo error and keruru's are described with different words (the repo's is "corrected", keruru's is an `arithmetic-error`).

**Fix.** Add a locator list for 1.2e-46, give 41x (exact at 2N = 20,000) and about 17x (limit), and write the audit's own deep-tail error next to the keruru row in the same wording.

## What X1 gets right (kept so the fix pass does not over-correct)

- All 67 pre-registered predictions are reported with the miss and the discarded draft.
- 34 of 45 rows reproduce clean, and the critics' pivotal identities verify exactly (sympy and exact chains).
- It names the specific critic catches (Dumb-and-Dumber's 3,840 against Day's printed 38,400, Camestros's "average", Matev's variance, Bowers's 2s).
- The unit and input flags on Hancock are mostly against the arguer's own interest, and X1 says so.
- It raises the Day s6.4 parity question rather than hiding it. The fix is to put it into the suggested-changes table.
