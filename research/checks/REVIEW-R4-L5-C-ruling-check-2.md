# Bounded D-24 check of the lead's Addendum 2 (L-R11 to L-R15), L5 / claim C external

Date 2026-10-14. Reviewer: a fresh reviewer instance (Paperclip EVO-82), using the skill `review-correctness`. Labels: BLOCKER / MAJOR / MINOR / NOTE. **This review sets no verdict.** It is bounded to the two questions of the brief (L-R11/L-R12 first, then L-R14/L-R15). EVO-75's findings (`REVIEW-R4-L5-C-external-ruling-check.md`, 7471d60) are taken as accepted and are not re-reviewed.

> **BLOCKER on L-R11/L-R12.** The "no" does not stand on the grounds it gives. Ground 3 fails: Q25's 230 is Day's figure for what selection can *achieve*, not for the regime the comparator *requires*. That is the lead's own third reopen condition (L-R13), and it has now been met. Ground 1 misstates the corpus. L-R12 refuses the "yes" case with a use of rule RD that B-R13 did not make, and it cites L-R1 for a use that L-R1 never made. Under D-24 and L-R16 the question goes to the owner with both branches costed (section 4). This review does not say which branch is right. Section 4 does show that a symmetric RD analysis may give the same field value by a different route.

**Independence.** I wrote none of: `R4-L5.md`, its fix passes, the L5 reviews, EVO-75's check, the lead's rulings L-R1 to L-R16 or B-R11 to B-R19.

**Read.** Brief `briefs/L5-reviews-reviewer.md` l.54-288 (Addenda 1-2, at 44ee590). `briefs/O5-reviews-reviewer.md` l.300-374 (B-R11 to B-R14, commit 9f863fd). `R4-X1-verdict-rule.md` RD l.196-202. `R4-L5.md` l.186-204, 285-287, 352-363, 400, 428-429, 488. `l5_adna_power.py` l.74-78, 187, 554. Claim C l.1-59. `quotes-day.md` discrepancy table, Q07-Q12, Q25-Q28, Q44-Q46, Q275-Q278, and a grep of the whole file for "selection coefficient", "s =", "strong". `REVIEW-R4-L5-C-external-ruling-check.md` l.1-35 (the recomputation table).

**Held source text read** (`sources/raw/day/` is not on this workstation or on na-workhorse, so I fetched again, each fetch into the new directory `sources/raw/l5-rulingcheck2-2026-10-14/`, which is gitignored):

| Source | File | sha256 | Matches bib? |
|---|---|---|---|
| Z18167588 (Bernoulli Barrier), Zenodo API | `zenodo-18167588.docx` | `dc0fbe5aac02abbd…ee75b02fb` | **yes** (bib-day l.19) |
| same, text (document.xml, tags stripped, one non-empty paragraph per line) | `bern.txt` | `55df820e…0dd031` | n/a; paragraph count reproduces Q25 ¶6 and Q26 ¶111 |
| Blog 2026-01-19 Q&A (Q44) | html `059185b3…dd9ad51f`; `qa.txt` `4c63e828…f90e8fcd` | — | no (WordPress page; bib has be64641e… and 1da3902a…). The Q44 text is present verbatim |
| Blog 2026-01-14 (Q275-Q278), held copy `sources/raw/l5-steelcrit-2026-10-13/` | html `5a90f2e7…03a2452`; `blog.txt` `a023833f…bd6900f8` | — | no (quotes-day records 5303e993… from the 2026-10-07 fetch). Q275 and Q276 are present verbatim |

**Recomputation** (local, stdlib, one line of arithmetic, not committed).

| Quantity | Ruling says | Recomputed |
|---|---|---|
| Concurrent sweeps, 15,556 per window, `tfix = 4 ln(Ne s)/s`, Ne = 1e4 (script l.554, l.187) | ~28,000 at s ≥ 0.05; "rising as 1/s to roughly 37,000 at s = 0.03" | 25 y: **27,621** at 0.05, **42,251** at 0.03. 20 y: 22,097 at 0.05, 33,801 at 0.03 |
| Ratio to 230 | "about 100 to 160 times" | 25 y: 120 to **184**; 20 y: 96 to 147 |
| Transit time at s = 0.01, (2/s) ln 9 | 440 | 439.4 (holds) |
| (300,000/440) x 230 | 157,000 | 156,818 (holds) |
| F_ii = 0.135 x 29,925 x 7,000 / 6.3e6 | 4.489 | 4.48875 (holds); strong class 28% = 1.257; 1.257/15,556 = **0.0081%** (holds) |
| s implied by Day's "1,600 generations per fixation" via his own t ≈ (2/s) ln(2Ne) (Q45), Ne = 1e4 | — | **0.0124** |
| Deterministic s floor for a <10% → >90% crossing (log-odds change ln 81 at s/2 per generation) | — | 0.0251 in 350 generations (20 y); 0.0314 in 280 (25 y) |

---

## 1. Question 1: is L-R11's "no" right?

### 1(a) Is there any text that attaches s ≥ 0.03 to the comparator or to the 15,556?

I found none that attaches it **to the 20 million / 15,556 (Q275)**. I did find text that attaches s ≥ 0.03 to Day's **divergence-requirement model** in the same paper the ruling relies on for its 0.01, and text that attaches "strong selection" to the 20 million. Ground 1 does not survive as worded.

What the corpus holds, by item:

- **Q44 (Q&A, ¶ in `qa.txt` l.774-782).** Verbatim as recorded. Context the ruling does not use, and it strengthens ground 1: Day introduces s = 0.001 as "the existing scientific consensus to derive a best possible estimate for the rate of fixations in humans". Then: "19,800 > 1,600. So using the 1,600 generations rate was extremely generous to the Modern Synthesis model." This is Day's own s for the fixations the Modern Synthesis needs. It is below s\*.
- **Q09 (Z18165980 ¶37) and Z18167588 §6.2 (`bern.txt` l.62-64).** Day applies "~1,600 generations per fixation **under strong selection**" to the 20 million. At his own Ne = 10,000 his formula (Q45) gives s ≈ 0.012 for that fixation time. Day calls this rate "extremely generous" (Q&A). So the corpus attaches a *qualitative* "strong selection" to the comparator, and Day's own arithmetic puts it below s\*. The ruling's sentence "No quote in the corpus attaches any s to the comparator" leaves this out.
- **Q25, Q26, Q27, and the Q26 note (Z18167588).** Verbatim at `bern.txt` l.6, l.111 and l.114-115. The note's "t_transit ≈ (2/s) × ln(9) ≈ 440 generations with s = 0.01" is at l.107-108. The paper's model "assumes a uniform selection coefficient of s = 0.01 for illustrative purposes" (l.85). That s belongs to the **157,000** loci "required to account for human-chimpanzee divergence" (l.6, l.169), not to the 20 million.
- **Z18167588 §7.5 (`bern.txt` l.86-88). Not in `quotes-day.md` and not cited by the ruling.** Verbatim: "Lactase persistence … exhibits selection coefficients estimated at s = 0.014–0.15, with most estimates clustering around s = 0.01–0.05". And: "**Even granting the most extreme documented selection coefficient of s = 0.19** … With s = 0.19 per locus, only 5–10 loci can be under simultaneous selection—far fewer than the 100 permitted when s = 0.01." Day therefore runs his divergence-requirement model at s = 0.19 per locus, as a case he grants for argument.

**MAJOR-1 (ground 1 misstates the corpus).** "Both s values he does give are below s\*" is false. Z18167588 §7.5 gives 0.014-0.15, 0.01-0.05 and 0.19, and applies 0.19 to the same model whose 0.01 admits R-b. None of these is attached to the 15,556. The 0.19 is a concession, not an assertion. But the s = 0.01 that admits R-b is also stated "for illustrative purposes" and is attached to the 157,000, not to the 15,556. As the criterion of L-R7/S5 is written ("an s given by Day"), it either admits values Day gives in other contexts or it does not:
- If it does, R-a (Q44) and R-b (Z18167588's 0.01) qualify, and so does s ≥ 0.03 (§7.5).
- If it requires attachment to the 15,556, then R-b's 0.01 fails as well. R-a then survives only on the Q&A's "rate of fixations in humans", which is the strongest attachment the corpus holds.

*Fix:* the lead states which test applies and applies it once to R-a, R-b, the gap and R-d. The test that best fits the record is "the s Day himself asserts for the fixations the Modern Synthesis needs, as opposed to an s he concedes for argument". On that test, ground 1 holds on Q44 plus the Q&A context, and on the "extremely generous" 1,600 (s ≈ 0.012). §7.5 must then be recorded as the concessive s ≥ 0.03 case and set aside on that stated ground, not left out.

### 1(b) Is Q25 read correctly?

- **Day's own figure:** yes. "approximately 230 simultaneous sweeps" (l.6, abstract). The same paper's body says "200–300" and derives nothing: "Working backward from the constraint" (l.111).
- **Derived at s = 0.01:** only loosely. The text derives no 230. The paper's model is "a uniform selection coefficient of s = 0.01" (l.85), and the transit time beside it is at s = 0.01. "Stated inside a model whose s is 0.01" is accurate; "derived at s = 0.01" is not.
- **A figure about the comparator's regime: no. Ground 3 fails.** The 230 is Day's cap on what selection **can achieve** (the "pipeline capacity", l.112). The comparator is what the Modern Synthesis **requires** (Q275: "The Modern Synthesis requires …"). Day's whole method sets the requirement above his caps. That gap is his argument, not evidence that he reads the requirement differently. The same paper, l.63-64: "Maximum fixations = 100 × (202,500 / 1,600) ≈ 12,656. The human lineage requires 20 million fixations. The combined constraints produce a shortfall exceeding three orders of magnitude." On that pattern, a reading under which the requirement exceeds 230 by 100 to 180 times is exactly what Day would say the Modern Synthesis needs and cannot have. So "R-d contradicts a figure Day states himself" does not show that R-d is not Day's reading.
- **Day's strong-s figure is not 230.** §7.5 says strong selection "permits … fewer parallel loci" (l.88): 5-10 at s = 0.19, from Σs ≤ 1-2 (l.60, l.87). That would give about 20-67 at s = 0.03-0.05. If ground 3 were kept, it compares R-d with Day's s = 0.01 figure when his own strong-s figure is 4 to 10 times lower. That error is in the ruling's favour, but it is still the wrong figure.

**MAJOR-2 (ground 3 fails; L-R13's third reopen condition is met).** L-R13 says the question reopens on "a resolution of Q25 showing 'approximately 230 simultaneous sweeps' is not Day's figure for the comparator's regime". It is Day's figure for the regime of *achievable* sweeps, not for the *required* count. *Fix:* withdraw ground 3. Withdraw L-R12's second bullet as well, because it rests on the same "conflicts with his Q25 figure". Also withdraw R4-L5 l.400's "outside the regime of the model that produced the number", which is circular: the model that produced 20 million is the long-run substitution count, i.e. R-e. Record that the reopen condition fired and how it was resolved.

**MINOR-3 (numbers in ground 3 and in R4-L5 l.363).** With the script's own `tfix = 4 ln(Ne s)/s`, the concurrent count at s = 0.03 (25 y) is **42,251**, not "roughly 37,000". The scaling is not 1/s; a 1/s scaling from 27,621 would give 46,000. The ratio to 230 is 120 to **184**, not 100 to 160. At the post's own 20-y clock it is 22,097 to 33,801 (96 to 147). *Fix:* correct these if anything of ground 3 is kept, e.g. in the S7 non-independence caveat. Q27's locator in `quotes-day.md` is ¶63. On the same count that reproduces Q25 ¶6 and Q26 ¶111, the quote is at ¶114-115; ¶63 is the §6.2 "12,656" line (NOTE-9).

### 1(c) Is the strong-class figure the right quantity?

**MINOR-4.** Only partly. F_ii counts **adaptive nonsynonymous** substitutions: Uricchio's α x 29,925 nonsynonymous counts (script l.74-75). The 15,556 is a **genome-wide** count of all substitutions. The right quantity for R-d is the number of the genome-wide 15,556 that the mainstream model puts at s ≥ s\*. The 1.26 is wrong on both sides of that:
- **Too low** as a genome-wide adaptive count, because non-coding adaptive substitutions are left out.
- **Too high** as a count at s ≥ s\*, because the ASSUMED mapping puts the whole strong class at s = 1e-2 < s\*. On that mapping the mainstream count at s ≥ s\* is **0**, and 1.26 is a ceiling only if the class were moved up.

Ground 2 survives in direction: for R-d to hold, non-coding strong substitutions would have to outnumber the coding strong class by about 1.2e4 times. But the repo holds no number for the non-coding part. *Fix:* write ground 2 as "the coding strong class is ≤ 1.26 per window (0 at s ≥ s\* under the ASSUMED mapping); the repo has no genome-wide strong-class figure", and name the gap. A sourced genome-wide adaptive-substitution estimate would close it (L-R13's second reopen condition is the same thing).

### 1(d) Does L-R12 refuse the "yes" case on a rule the repo holds?

Rule RD (`R4-X1-verdict-rule.md` l.198), verbatim: "The claim file's verdict field takes the value under the **most charitable reading** (rule C, the same for Day, critics and allies), defined as the reading under which the speaker's *quoted statement* is most defensible (closest to literally true, best supported): the classical principle of charity. It is **not** the reading that yields the best verdict for the speaker."

**BLOCKER-5 (asymmetric use of RD's second sentence; false precedent).**
- **L-R1 never applied RD.** L-R1 (brief l.67-74) is about registered wording narrowed after the result was seen ("report beside it" became "withhold because of it"). It contains no reading, no charity and no RD, and it ruled against the audit's withholding, not against Day. The claim "the lead applied the first sentence against Day in L-R1 on this same check" is false.
- **B-R13 used the sentence neutrally.** It quotes RD as fixing the field on "the quoted statement is most defensible … explicitly not the reading that is most natural, nor the one best for the speaker" (O5 brief l.347-349). It then admits S_L, a reading that is both most defensible and best for Day ("a Day-favourable move … on the charity rule", l.363-365). There the sentence was not a bar.
- **L-R12 uses the same sentence as a bar** on readings "reason[ed] from what Day's conclusion requires back to what his premise must have been". RD does not say that. What separates the two cases is whether the source supplies the reading, which is a plausibility test (L-R7/S5, L-R11), not RD's second sentence.
- **Applied the B way, the textual test is not one-sided.** The post (held `blog.txt`; Q275 at ¶4, then ¶5) puts the 15,500 "fixations per 7,000-year period" against "Not a single allele in 1.2 million crossed from rare (<10% frequency) to fixed (>90% frequency) in seven thousand years". It introduces that count with "To test these competing predictions". The post's own paragraphs thus fix what the comparator is held to: crossings within the window. A crossing in 350 generations needs s ≥ 0.025 deterministically (0.031 in 280). B-R12 admitted S_L because "Q157's own paragraph names its inputs" and the reading "is Day's own computation". The post's own computation names the test the 15,556 is held to in the same way. "s ≥ s\* for the 15,556 is in no text" (L-R12) is therefore too strong. The text does not state an s, but it does operationalise the comparator in a way that entails one near s\*.
- **The other side.** Day's Q&A gives the fixations the Modern Synthesis needs s = 0.001 and calls the 1,600-generation rate "extremely generous". That supports reading the post's crossing test as Day's conflation (R-e, the existing internal `non-sequitur`) rather than as his s. Both readings have text. L-R12's "supplied by the source, admitted; required by the conclusion, refused" sorts them as if only one did.

*Fix:* strike the L-R1 precedent. Replace L-R12's first bullet with the RD test applied as in B-R13: is R-d (or "R-d′, the comparator as the post's own crossing test operationalises it") plausible on the source's own text? If so, under which reading are the **quoted statements** (claim C's Statement carries both Q275 and Q276) most defensible? That question has not been asked. See NOTE-6 for why the answer may not favour R-d.

**NOTE-6 (the symmetric RD analysis the ruling does not do; offered, not ruled).** Under R-d, Q276's inference follows. But Q275, "The Modern Synthesis requires … approximately 15,500 fixations per 7,000-year period", becomes an attribution to the mainstream of about 15,500 strong crossings per window. Ground 2's own evidence speaks against that attribution: a coding strong class of ≤ 1.26, 0 at s ≥ s\* as mapped. Day's own Q&A also gives the Modern Synthesis's fixations s = 0.001. So R-d does not make the quoted statements more defensible; it moves the failure from Q276 to Q275. Under R-e, Q275 is literally true and Q276 fails. If the lead holds this, R-d's tabled verdict "`supported`" (L-R12, L-R13, R4-L5 l.363) applies to the narrow inference only. The comparative claim of Q276 ("over the Modern Synthesis expectation") would then fail on its premise under R-d too. That is a symmetric ground on which R-d need not set the field, and it would replace the asymmetric one. It is the lead's call.

---

## 2. Question 2: L-R14 and L-R15

**MAJOR-7 (L-R14/L-R15: the admissible set is drawn at the verdict boundary, not at a source).** L-R14 keeps L-R2 by making R-c's admissible disjuncts "R-a and R-b alone". L-R15 then counts "the s = 0.02 gap" (and 0.03-0.05 in hard mode at 25 y) as **admissible**. Yet R4-L5's own gap row (l.361) says "no source gives the 15,556 an s here". On the L-R7/S5 criterion the gap fails exactly as R-d does. R4-L5 l.285 admits it on a different ground: R-c "covers every s the source leaves open. Its admissible part is s below s\*". The source leaves s ≥ s\* open in the same way. So the admissible part is cut at s\*, the point where the verdict flips, and not at any s a source gives. Each of the two moves (gap in, R-d out) goes against Day.
- On the stated criterion, **L-R2's conclusion survives**: drop the gap and keep only R-a and R-b, which are both `contradicted`. The disjunction argument then goes through, conditional on MAJOR-1's test.
- On the "every s the source leaves open" ground, it **does not survive** without NOTE-6's analysis of R-d.

*Fix:* L-R14/L-R15 pick one admissibility test and apply it to the gap and to R-d alike. Under S5 the gap is recorded as a non-admissible sensitivity, like R-d.

**MINOR-8 (L-R15's "every admissible reading returns `contradicted`" holds only inside the zero-statistics scope).** For R-a, R-b and R-e on the zero statistics, and for the gap on the zero statistics (EVO-75 table: ≤ 9.64e-7 at s = 0.02, 25 y; 0.0435 at 20 y), it holds. It does not hold for the readings as such. Day's reported M10 excludes the required rate at s = 0.02 standing, 25 y (E 25.2, P(X ≤ 1) = 2.98e-10). It does so also at s = 0.01 standing, const, 20 y (E 10.3, P = 3.8e-4), and at s = 0.02 hard, 20 y (P = 1.74e-6), all from EVO-75's recomputation. Claim C's title carries the Zenodo counts that M10 reads. The scope rule (inference = Q276, blog zero statistics) is principled. But "no dependence to report" is true only because the field is scoped. *Fix:* write "every admissible reading returns `contradicted` **on the zero statistics that carry Q276's inference**; under R-b at 20 y and in the gap at s = 0.02, Day's reported M10 does exclude the required rate". The reading-dependent count can stay flat on that stated scope.

**NOTE-9 (bookkeeping).** Q27's locator is ¶63 in `quotes-day.md`; it should be ¶114-115 (MINOR-3). The 2026-01-14 blog copy held for L5 (`l5-steelcrit-2026-10-13`) hashes to `5a90f2e7…`, not the `5303e993…` recorded beside Q275-Q278. The quoted text is identical. `sources/raw/day/` is missing from this workstation and from na-workhorse, so "the held corpus" cannot be checked against the hashes in `bib-day.md` without fetching again.

---

## 3. Counts

1 BLOCKER (5), 3 MAJOR (1, 2, 7), 3 MINOR (3, 4, 8), 2 NOTE (6, 9).

**Wrong numbers (old -> right):** concurrent sweeps at s = 0.03, 25 y: ~37,000 -> 42,251. Ratio to 230: 100-160x -> 120-184x at 25 y (96-147x at 20 y). Scaling "as 1/s" -> 4 ln(Ne s)/s. "Both s values he gives" (2) -> at least five in the corpus (1e-3, 0.01, 0.014-0.15, 0.01-0.05, 0.19), of which two are asserted for the fixations Day attributes to the Modern Synthesis (1e-3, and about 0.012 implied by his "generous" 1,600 generations). Q27 locator ¶63 -> ¶114-115.

## 4. Both branches, costed (for the owner, per L-R16)

| | Branch NO (R-d does not set the field), rebuilt | Branch YES (R-d plausible) |
|---|---|---|
| Ground | Ground 3 withdrawn. Ground 1 restated with an attachment test (MAJOR-1) and §7.5 recorded as concessive. Ground 2 restated as coding-only (MINOR-4). L-R12 bullet 1 replaced by RD as applied in B-R13 (BLOCKER-5), e.g. NOTE-6. Gap handled like R-d (MAJOR-7) | The post's own crossing test (¶4-¶5) taken as supplying the comparator's s, as S_L was taken from HL's own computation |
| Field | `contradicted`, scoped (unchanged value) | If NOTE-6 is adopted: still `contradicted`, scoped, with the failure moved to Q275's attribution under R-d; count flat. If R-d is held `supported` and most defensible: `supported`, scoped; reading-dependent count +1 |
| Work | One lead paragraph. Fix-pass edits to R4-L5 l.287, 361-363, 400 and Readings table; Q27 locator. No compute | The same paragraph, plus a ruling on Q275 under R-d. If `supported`: claim C field and comment, defeaters d467-d469, counts, board. Optional post hoc: a sourced genome-wide strong-class bound (closes MINOR-4 either way) |
| Risk | Low if every test is applied once to R-a, R-b, the gap and R-d | The B-R13 precedent then binds every later case where a test design implies an unstated parameter |

Integration of L5 / claim C external should not fire until the lead has answered BLOCKER-5 and MAJOR-1, 2 and 7.
