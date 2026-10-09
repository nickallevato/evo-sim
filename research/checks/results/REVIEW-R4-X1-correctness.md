# Correctness review of R4 X1 (arithmetic audit of critic and ally claims)

Reviewer: correctness pass, 2026-10-09. Read: `R4-X1-critic-arithmetic.md`, `x1_critic_arithmetic.py` (pre-registered `fa0bc9b`; `git diff fa0bc9b HEAD` on it is empty), the two post hoc scripts and their `.out` files, `raw/x1_results.{out,json}`, the critic and ally claim files, `quotes-critics.md`, and read-only greps of `sources/raw` (McCarthy comments JSON, Peaceful Science topics 18094 and 18095, keruru's "Epicycle" post, Day's Z23003785 and Z19984826 text, Camestros part 3, McCarthy's Wielgoss quote). Scratch work is in `/tmp/claude-1000/-home-na-projects-evo-sim/1a09d35c-0829-4a9e-9e1c-591add0b31de/scratchpad` (`wf_indep.py`, `wfrepo.py`, `wf2.py`, `spec.py`). No file other than this one was edited and nothing was committed.

**Overall.** No BLOCKER. The arithmetic is sound: I found no row that fails to reproduce from the numbers the author prints. The weak points are (a) the C5 `arithmetic-error` suggestion, which rests on an Ne reading that the numbers themselves contradict; (b) the unsupported "event basis is fine" rescue of Hancock's 38M; (c) the unstated tolerance between `holds` and `arithmetic-error`; and (d) a few headline counts and labels that do not match the tables beneath them. Section 1 lists what I reproduced, so that credit is recorded.

## 1. What reproduced (so the findings below are read against it)

- **keruru C5, exact Wright-Fisher.**
  - I re-implemented the recursion independently (gammaln binomial rows, my own band). At 2N = 20,000 and 240 generations it gives 5.119e-45 (p = 0.5), 5.883e-113 (0.1), 3.733e-8 (0.9) and 0.1906 (0.99), identical to X1 to four digits.
  - The repo's own function gives the same, and the spectrum integrals (4.9e-41, 2.6e-4, 1.3e3, 5.3e-4) also match.
  - Repo 1.24e-46 against 5.12e-45 is 41.3x; keruru 4e-35 against 5.12e-45 is 9.9 orders. Both statements in X1 stand.
- **Diffusion limit.** I computed it exactly from the Kimura spectral series, u(x,tau) = x + sum_n (-1)^n (2n+1)/n * x(1-x) P_{n-1}^{(1,1)}(1-2x) exp(-n(n+1)tau/2) at 300 digits, with tau = t/(2N) = 0.012. It gives 1.79e-45 at p = 0.5 and 5.8e-114 at p = 0.1. X1's post hoc claim that the limit is "probably about 2e-45" is correct, so the "41x" is a finite-2N figure and about 15x against the limit. X1 states this properly.
- **McCarthy.**
  - Comment 337116873 reads verbatim as quoted, with "Nine million years divided by 25 = 360,000" and "50,000 x 8,000,000".
  - Comment 340149310 prints "400 billion x 1/20000 = 35 million". 4e11/2e4 = 2.0e7, so M03 is a plain slip.
  - 25 y throughout gives 16.0M; 20 y throughout gives 20.5M. The percentages (2.4% and 20%) are right. The 13.1 to 21.8M range for 60 to 100 x 0.97 is right.
- **Hancock.**
  - 4.6e6 x 1e-11 = 4.6e-5, giving 21,739 generations. 205e6/504,000 = 406.7 and 205e6/252,000 = 813. 813/76.8 = 10.6.
  - Day's text does say "Apportioned symmetrically to the human lineage ... approximately 205 million" (Z23003785 line 487). The 38,400 is printed at line 459 and should be 3,840 (A2h is right).
- **Hancock's 8.9e-11.** It is in McCarthy's free post as a Wielgoss 2011 quote: "8.9 x 10^-11 per bp per generation (95% CI 4.0-14 x 10^-11) ... total genomic rate 0.00041 per generation".
- **38M double count.** 2 x 1.2e-8 x 252,000 x 3.2e9 = 19.35M, and 4 x 1.32e5 x 1.2e-8 x 3.2e9 = 20.28M.
- **Nesslig20.**
  - The CDF percentiles reproduce (3.479, 8.188, 11.408 and 16.013 Ne; F(4Ne) = 0.6063).
  - The "100 to 200 per generation" and mu_G = 75 text matches.
  - The lottery numbers match.
  - The Barrick "2019" year and the "0.33" for 1/3 are as X1 says.
- **Smaller checks.**
  - Camestros "1500÷35≈429" and "1051" are verbatim.
  - Day's table mean 477.6 includes the -906.
  - G3 (10^-86,020,600; 527 sd), G5 (39,250; 0.252%), F4 (0.02017) and Hössjer's chain all recompute.
- **Claim coverage.** The 45 plus 21 claim IDs equal the 66 critic and ally files exactly. The 67 docstring prediction rows are there, and the main script is unchanged since the pre-registration commit.

## 2. Findings

### 1. MAJOR: the C5 `arithmetic-error` suggestion depends on an Ne reading that the author's numbers do not follow, and X1 does not disclose the sensitivity

X1 says keruru's 4e-35 is "10 orders too large from the author's own inputs" and suggests `arithmetic-error` (§4 C5, §6, §9). The stated input is "a human effective size around ten thousand" (4Ne about 40,000), and the model is only "running the absorption probabilities at that scaling". The code was not retrieved.

The result is steeply sensitive to the copy number 2N, because log P is about -(const x 2N). I computed the diffusion limit and exact WF at other values:

| 2N | diffusion p=0.5 | diffusion p=0.1 | exact WF p=0.5 | exact WF p=0.1 |
|---|---|---|---|---|
| 15,000 | 2.6e-34 | 9.9e-86 | 5.7e-34 | 5.6e-85 |
| 15,365 | 4.0e-35 (keruru's value) | | | |
| 16,278 (= 2 x 8,139) | 3.6e-37 | **6.02e-93** (keruru: 6e-93) | 8.6e-37 | 4.0e-92 |
| 20,000 | 1.8e-45 | 5.8e-114 | 5.1e-45 | 5.9e-113 |

keruru's p = 0.1 figure matches the diffusion value at 2Ne = 16,278 to three digits. The root of the equation is exactly 2 x 8,139, his own temporal Ne in C5b. His p = 0.5 figure matches the diffusion limit at 2N of about 15,400. Both published values are therefore consistent with an Ne of 7,700 to 8,400 and are 2 orders or less from X1's own numbers at that Ne, not 10 orders. This is not proof of what he ran, since the p = 0.5 value does not hit the same Ne. But it undercuts "wrong from the author's own stated inputs" as the label.

A 20% change in Ne closes the whole gap, and "around ten thousand" is an approximate input. The post also uses 4Ne = 40,000 in its narrative, which is an internal inconsistency worth recording instead.

Recommendation:
- Record C5 as "not reproduced at the stated Ne = 1e4 (5.1e-45); both published values reproduce within about 2 orders at Ne about 8k; model and Ne unspecified; code not retrieved".
- If the lead still wants `arithmetic-error`, say it is conditional on the Ne = 1e4 reading.
- The conclusion (zero is expected unless loci start above about 0.9) is unaffected either way, as X1 says.
- Replacing the repo's 1.2e-46 by 5.1e-45 (or 1.8e-45 for the limit) is correct.

### 2. MAJOR: "on an event basis the 38M comparison is fine" is asserted, not computed, and contradicts X1's own double-count logic

X1 §4 B5c, §6 and §10 say the "38M matches 35 to 40M" is "right on an event basis" because Hancock's retained 76 is 152/2 (the 98 to 206 range) and 2 x 252,000 x 76 = 38.3M "compares correctly to the 40M event total". The SNV-basis arithmetic is right (19.35M + 20.3M = 39.6M). The event-basis rescue has two unexamined problems:

- **The observed total contains ancestral polymorphism.** The 40M events (35M SNV + about 5M indel events) include polymorphic ancestral differences, as the SNV case does. The 76 per generation has no ancestral term, so it is post-split supply only. The same double-count logic that X1 applies to SNVs applies here.
- **The null overshoots the non-SNV events.** The 76 events per haploid genome per generation exceed the SNV pedigree rate of 38.4 by 37.6 per generation. Over 2 x 252,000 lineage-generations that is about 19M non-SNV events in the null, against about 5M observed indel events (GAP-07b measured 4.30M). So the match to 40M is plausibly a second coincidence, not a clean confirmation.

I could not check what the 98 to 206 range counts, because the source is garbled in the captions ("Perky? et al.", GG-06 note). It may include STRs and other classes that are not in the 5M. X1 should either run the like-for-like comparison or drop "fine" and write "not tested; the same double-count caveat applies". This affects the "Who this helps" credit to Hancock and the Day-side B6a point ("ancestral is half").

Related, minor: the existing claim file B5c says ancestral is "about 15M" (the residual 35 - 19.4), while X1 says "about 20M" (a Yoo HCG prediction at Ne_anc = 1.32e5). X1 §6 calls the double count "Confirmed" as if new, but the claim file already records it. X1 should present 15 to 20M and note that 39.6M overshoots 35M SNV by 13%.

### 3. MAJOR: the boundary between `holds` and `arithmetic-error` uses an unstated tolerance, and X1 does not apply "the rule used for Day" consistently

§2 and §1 say the rule is "any stated number that does not follow from the author's own inputs is an arithmetic-error, material or not". In practice:

- **Given `holds` despite failing the literal rule:**
  - McCarthy's "roughly 690" for 3.1e9/4.6e6 = 674 (2.4%). The harvest note itself calls it "a 2% discrepancy with his own stated inputs".
  - Hancock's "4e-5" for his own 4.6e-5 (13%).
  - Nesslig20's 0.51 for 0.503 (1.4%) and 0.33 for 0.3333.
  - KITTENS 94,000 for 91,600 (2.6%).
  - Hössjer 15,800 for 125 x 127 = 15,875.
  - Mansfield "about 10 times" for 15.5x.
  - Camestros 1500 for 15,000 and 1051 for 1050.
- **Given `arithmetic-error`:** McCarthy's M03 (75% off, clear) and the C5 per-locus value (see finding 1). B5a's suggestion also leans on M02 (the 25 y / 20 y mix), which is a 2.4% effect on the 20 y reading and relies on the origin of "50,000" in a different document (McCarthy's post); the comment itself gives no unit for it. M03 alone supports the verdict.
- **Self-correction.** Hancock's 76.8 is excused as "self-corrected on screen". X1's §9 raises this as a policy question for the lead, which is right, but the headline count "2 suggestions" silently chooses one side of it.
- **Day side.** The existing Day `arithmetic-error` verdicts (A3a, A5e, B6a, C6, G, G1a) are all large. I found none for a rounding-size slip, so there is no evidence the "material or not" rule was ever applied at the 2% level to Day either. X1 itself notes that s6.4's 38,400 is not logged as a Day arithmetic-error anywhere.

Recommendation: state a tolerance (for example, more than about 5% or a changed digit is an error; below that is a rounding note, same for both sides), list the sub-threshold slips in a fixed table for both sides, and give the Day-side 38,400 the same treatment as McCarthy's M03. Without this the 2-versus-0 headline (and the 22/112 comparison in §10) cannot be read as like for like.

### 4. MINOR: the headline "34 clean / 9 flagged / 2 do not reproduce" does not match the suggested verdicts

- The 9 flagged are the claims with a `P` row (B5a, B5b, B5c, A5c, B5e, A5b, B2e, A4c, D14).
- B5a also has an `N` row (M03) and a suggested `arithmetic-error`, the same verdict C5 gets, yet C5 is counted under "do not reproduce" and B5a is not.
- A5 has an `N` row (M04) but is counted clean.
- D8's `N` depends on an odds figure (1 in 1.4e8) that is not in the source text, so it is an assumed input. D8 is also "not scored internal" in the same table.

Define the classes by suggested verdict, or by row letters, and use one definition.

### 5. MINOR: the scorecard understates the pre-registered misses and credits hedged predictions

- **Misses.**
  - "One pre-registered numeric band was missed" is true of the 1e-47..1e-45 band, but the K-03 pre-registration also predicted "0.99 a few %" (exact 0.19) and "million loci at p = 0.5 gives ~1e-40" (exact 5.1e-39, 50x off).
  - It also predicted "within a factor 10 of the Brownian value", the same miss as the band.
  - The table lists two of these. The 1e-40 miss is missing.
- **Hedged predictions.**
  - "67 of 67 match" includes six predictions with two letters (H01, H05, H07, N09, G06, K-03).
  - Examples are "R arithmetic; P fidelity" and "R / P". The recorded outcome is then one of the two.
  - They should be reported separately from the single-letter ones.
- **Count.** `[cf]` appears on 39 rows of the docstring (X1 says 40, with N10 tagged both ways).

### 6. MINOR: post hoc rows are not tagged where they enter the tables

B5d, B6 (post hoc script `1f3dd12`) and the Camestros [3] arithmetic (`eb7617a`) are in the 45-claim table and the 34/9/2 counts. The 67 pre-registered predictions do not cover them. §1 mentions the three post hoc scripts, which is the correct disclosure. But the table rows are not marked, so a reader cannot tell which of the 45 were pre-registered. Tag them (for example, "post hoc") and give the counts with and without.

### 7. MINOR: A5c details

- The script gives 2,443 generations (1/(4.6e6 x 8.9e-11)) and §4 prints 2,439. 2,439 is 1/0.00041, Wielgoss's own stated genomic rate, so it is defensible, but say so.
- X1 does not report Wielgoss's 95% CI of 4.0 to 14e-11. It gives a neutral expectation of 1,550 to 5,400 generations. Against the observed 1,322 that is 1.2x to 4x, not "1.8x". The 1e-11 is also below the CI's lower bound.
- Day's own Z19984826 uses 8.9e-11 for the LTEE, so the inconsistency is between Hancock and the input Day uses.
- The input slip was already recorded in A5c's Weaknesses and in the GG-08 note ("with 8.9e-11 ... about 2,500"), so "input slip" is a quantification, not a new finding.

### 8. MINOR: §10 states a reading of Hancock's 407 as fact

§10 says "Hancock misreads the unit of Day's 205M". §4 and §11 say his 407 cannot be tied to the full sentence. 407 = 205M/(2 x 252,000) is a strong inference, since only the verbatim "divide this out over ... 205 million you get something like 407" is available. The 76 = 152/2 reading likewise rests on the harvest note, not the quoted caption (GG-06). Say "inferred from" in both places.

### 9. MINOR: Nesslig20 slips are partly inferred

- **"1/Ne = 0.00005".** The "symbol slip" for 1/(2Ne) assumes Ne = 1e4 from Part I. Part II (topic 18095) does not restate Ne. If Ne = 2e4 there, it is consistent.
- **"0.51".** His own "70 million" tickets gives 0.503, so 0.51 is a rounding up, as X1 says.
- **The 75.** X1 correctly leaves 75 undecided, but the harvest note already says "75 is a per-diploid-offspring de novo count; stated as per haploid genome". X1 should reference that note, since it is the repo's existing reading.

### 10. MINOR: raw-output wording and D8

- **The `G07` row.** The note in `x1_results.out` says the Milton analogy is off "by ~5 orders of magnitude of exponent". The exponents 424,764 and 65 differ by a factor of about 6,500, i.e. 3.8 orders of magnitude. The write-up's "about 420,000 orders of magnitude" is correct. The raw note is wrong (the pre-registered docstring says "10^-424,000", which matches).
- **Odds assumption.** The 1.4e8 lottery odds are an assumption (they could equally be 2.9e8), not a stated input. The analogy is rhetorical and the row should say so.
- **E1.** E1 was listed as a claim with no number, although its formal statement uses "45 mutations / 20k". That arithmetic is covered under N06 (20,000/45 = 444), so nothing is lost, but the 21-file "no number" list was apparently split by title.

## 3. Verdict rules summary

- **Internal-verdict rule.** B5a (`arithmetic-error`, comment-level) is supported by M03 alone; M02 should not carry it (finding 3). C5 is not supported as stated (finding 1). H5 unchanged is consistent. The `pending` to `holds` changes for B4g, B6c, G2c and E5 follow from reproducing arithmetic and are consistent with each other.
- **Scope of `arithmetic-error`.** It should be reserved for errors from the author's own inputs. M03 qualifies. M02 qualifies only with the cross-document 20 y reading. C5 qualifies only at Ne = 1e4. Hancock's 1e-11, the 205M unit, Nesslig20's 75 and the 38M comparison are correctly kept in the fidelity column.

## 4. Quote readings

Every quote I checked is verbatim and correctly read: McCarthy (both comments), keruru ("around 4 x 10^-35 ... 6 x 10^-93 ... only alleles already above about 0.99 ... near 10^-29"), Hancock GG-04 to GG-12 against `quotes-critics.md`, Nesslig20 ("100 to 200 per generation ... mu_G = 75 ... 37,800,000"), Mansfield MF-03 and MF-06, Camestros part 3, Day's "apportioned symmetrically" and 38,400, and the Wielgoss quote. I did not check Mansfield's "genome only about 10 times", Bowers's original (not available), or the Hössjer PDF beyond the quote file.
