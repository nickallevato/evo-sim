# REVIEW R4 X1: independent audit of the single verdict rule

Reviewer: independent agent, 2026-10-09. Scope: check whether `R4-X1-verdict-rule.md` was applied evenly in `R4-X1-rescore.md`, which reports 18/82 Day numeric nodes with an internal error verdict against 0/31 critic nodes. No claim file, script or other result file was edited. Nothing was committed.

## 0. Method, and how blind it was

1. I read `AGENTS.md` and the rule file only. Then I listed the nodes:
   - the 16 Day `non-sequitur` nodes, plus A3a, B6a, C6 and G;
   - every node with `side: critic` (51 files), including all candidates named in `REVIEW-R4-X1-steelman-day.md`. From that review I took only the node IDs, not its text.
2. I scored each node from its claim file (Statement quotes plus Formal statement), applying R1, S, SC, N, F and U as written. Where a claim file was not enough to apply a clause, I grep'd the raw source (read-only). I did this for the Bernoulli paper, the Weasel post, the d-k post and Reddit thread 1wss2wj.
3. I saved my verdicts to the session scratchpad (`blind.txt`) before opening `R4-X1-rescore.md`. Section 3 compares the two.

**Limits on blindness.** I was blind to the rescore table's reasons, but not to the current verdicts, for two reasons:
- **The claim files carry them.** Each file's front matter holds the current verdict and its comment.
- **The rule file states 15 of them.** Its "test run" table gives the intended outcomes for B5f, A3d, C5, B5c, B5e, B6a, C, A5d, A2e, G2g, B9, B3e, C2b, C2c, F1a and B3c.

So this audit is a check of reasoning against the rule's text. It is not an unprimed re-extraction. The two places where I disagree with the rule file's own stated outcomes (A3a, and the clause cited for B6a) show the priming did not settle everything.

## 1. Blind verdicts

Clause codes follow the rule file. NS = `non-sequitur`, AE = `arithmetic-error`.

### 1a. Day nodes (20)

| Node | Blind verdict | Clause and one-line reason |
|---|---|---|
| A2e | NS | N2b/N2a: the paragraph that calls the LTEE the ceiling claims "effectively unlimited mutation supply". The paper's own per-genome supply figures (4.1e-4 vs 38.4) contradict this, and its own mutator rows run 8.5-17x above the "ceiling". Counter-reading: if "ceiling" means the non-mutator class only, this is N1 (external). |
| A5d | NS | N2d: "not bottlenecked by mutation supply" is drawn from a positive response, a = 0.47-0.61. The clause names this case. A charitable "not solely supply-limited" reading would be `holds`, but the rule's text rules that reading out. |
| B3e | NS | N2b: the 8.25 uses supply proportional to Ne and P_fix = 1/(2N). This is the reverse of the same post's k = mu(N/Ne). Per SC, it is scored on the version quoted; it was withdrawn later (B3g). |
| C2b | NS (weak) | N2a: under the post's own regression, k falls as d rises, so k tends to 0.10 mu at d = 1. The same paragraph says k = mu "applies with *increasing* accuracy the further back you go" (raw text, ¶9). Caveats: that sentence is not in the Statement quotes (an S1 gap). The fit itself was run by an unidentified "doctor" (U), so only Day's interpretation can be scored. The quoted ¶9 conclusion (k <= 0.5 mu in the modern period) does follow within the data range. |
| C2c | NS | N2a: under the paper's own recursion only s*d is identified. The s-ratio is therefore constant for any d, so "a fitting artifact would produce inconsistent ratios" fails on the author's own model. |
| F1a | NS | N2b/N2d: Day's own text says the six/seven-fixation figure "comes from the beneficial fixation time". Dividing a window by a latency, with no width factor, is the serial assumption by definition. His Bernoulli paper applies a width factor (230) to the same step. |
| B3c | NS | N2a: "not ... a boundary effect" fails on the paper's own formula. Extending the cohort window moves 0.743 across 0.60-0.87. The 1/N_i-at-birth mechanism point is external (N1) and is not the basis. |
| **F** | **holds** | The quoted chain is internally consistent: k = mu gives the rate "once the process is running", 4Ne is the "startup cost", and 1/2N "says nothing about when". The latency-as-throughput step is F1a's, which is already NS. The current basis ("as a throughput bound (F1, F2)") rests on simulations, which makes it external (N1). |
| C2 | NS (weak) | N2d: "independently converge on d ~ 0.45, consistent with Neolithic demographic structure" is stronger than the premises support. The author's own sensitivity paragraph shows d moving as 1/s, so the convergence reflects the chosen s values. The current comment's other basis ("d = 1 for discrete generations fails on own formula") comes from C2a's derivation, not from C2's quotes, and C2a is recorded as `holds`. |
| C7 | NS | N2a: on Day's own Ne (1e4, or 3,300), neutral drift predicts about 0 completions from intermediate frequency in about 280 generations. Zero completions is therefore not evidence that drift is absent. |
| G3b | NS | N2d: a dilemma with a middle case. "Interchangeable, therefore neutral noise" equates interchangeability with neutrality. |
| C | NS | N2a/N3: on Day's own Ne = 1e4 the neutral expectation for this statistic is about 0 from below 50%. The 15,556 comparator counts genome-wide new substitutions; the omitted panel and ascertainment term reverses the comparison. |
| Gc | NS | N2c: 230 is exactly the C that makes (300,000/440) x C equal 157,000. The paper uses 157,000 throughout as "the 157,000 parallel fixations required" (raw ¶169), reached by "working backward from the constraint" (¶111), and then says it "appears to match the requirement". The current comment's "circular *if* fitted" can be made unconditional. |
| B9 | NS | N2a: "extinct within centuries" conflicts with the same comment's "~one million years apiece" per neutral fixation. The Q105 basis in the current comment is weaker: premise 1 (selection off) makes harmful mutations effectively neutral, so Q105 does not contradict it. |
| G2g | NS | N2d: the quoted Bernoulli premise, p^n, has no timing term. It cannot rule out parallel fixation while allowing sequential fixation, so "therefore sequential" does not follow. The second sentence ("180 where 205 million are required") holds a fortiori per ¶25. |
| D9a | NS | N2d: "demonstrates the precise opposite" (of viability) is drawn from comparing an algorithm's runtime with a different population model. Day's own ¶7 concedes the Weasel "doesn't make sense" as a model. The current comment's basis (an exploratory, uncommitted 12-offspring truncation run) is a different model from Day's, which makes it external (N1); it should not be the basis. |
| **A3a** | **holds** (ledger) | R1, "most charitable reading of an ambiguous referent". Yoo reports SDRs per lineage, so read 187 Mb that way. The pairwise total is then 35M + 2 x 187M = 409M, about 410M (epsilon 0.2%), and per lineage 17.5M + 187M = 204.5M, about 205M. The claim file records this reading itself (Fun-Friendship4898). Ledger: "14.9%" with 410M implies 2.75 Gb against a 3.1 Gb genome (11%). Kept: fidelity `misread` (187 and 410 are not in Yoo) and external `contested` (units, A3x). |
| B6a | AE | R1b: "less than half" is 0.6. On IR's own table the empty-pipe removal is 1.2M, so the sign of "the net adjustment still reduces" flips (N2a). Not N3 with Yoo's Ne_anc: Day did include the term, at Ne = 1e4, so a different Ne_anc is a contested premise value (N1). |
| C6 | AE | R1a: the abstract's "99.8% within a single 2,000-year window" is 53.6% in the paper's own table (86%). The 630-vs-21 comparison also omits the paper's own panel fraction (scaled 5.2 < 21), which flips the comparison (R1b/N3). |
| G | AE | R1a: the printed "(1.01)^1474 ~ 14.7" equals 2.34e6. The stated conclusion (shortfall > 100x) survives on the additive or log scale (107). R1a has no "conclusion survives" escape; see section 5. |

Blind Day tally: 18 of 20 are errors (15 NS and 3 AE); F and A3a are `holds`.

### 1b. Critic nodes (51 files)

| Node(s) | Blind verdict | Clause and reason |
|---|---|---|
| B5f | holds | The Statement quote ("about 9.7 million") is the original poster's, Dumb-and-Dumber. In the raw post it is called "an illustration, not a prediction", and the poster declines a "precisely 1.8-fold gap" (N4). The "gap is under a factor of two", "It needs the elapsed time ...", and the CHLCA full-pipe premise come from a different author: comment pcug1j0 by justatest90 in the same thread. On that author's stated full-pipe premise the conclusion follows (N1). **Attribution error in the claim file:** quote 2 and the "under a factor of two" text are not Dumb-and-Dumber's. B5's "In support" quote repeats the misattribution. |
| A3d | holds (internal); fidelity misread or unverifiable | Hancock's conclusion (180 should be 360) is recoverable, so N5 does not apply. It follows on his premise that the requirement is a two-lineage total, which he also uses in the same video (205e6/(2 x 252,000) = 407, B5c). Whether that premise misreads Day's per-lineage 205M (Q15) is fidelity (N1). The slide is absent, so fidelity is `unverifiable`; it would be `misread` if the slide shows the book's "180 ... where 205 million are required". |
| C5 | pending | R1c: 1e-29 (at p = 0.5) reproduces at Ne of about 7,500-7,600 (-25%) under a Brownian approximation. R1c's own text says "or `pending` if the method is unretrieved", and the method is unretrieved. The conclusion ("finding one would have been the falsification") follows on his premises for loci below about 0.85. |
| B5c | holds | SC: 76.8 was corrected on screen, so it goes to the ledger. The retained 76 = 152/2 (an event count including SVs) gives 38.3M. N3: the conclusion "no shortfall" survives the ancestral term on either basis. However, on Hancock's own *event* basis, adding that term gives about 61M against the measured 42.1M events (+45%). If "matches" is taken as the conclusion, N3 gives NS (see section 5). |
| B5e | holds | 75 is defined per haploid genome (§2.1). The ancestral term gives 58-68M, against his own stated 31-62M (1-2%) range: survives at Yoo HCG Ne, borderline at HCB. Fidelity `unverifiable`: 75 is a non-standard uncited value. |
| B5a | holds | Arithmetic exact. "Exact correct result" survives the omitted terms at his own Ne (the ancestral term is about 1.5M, 7%). The comment-level 35M is a ledger entry (S2). |
| B5b, A5b | holds | N4: flagged illustrations. The arithmetic reproduces (A5b within 2%). |
| B5d | n/a (not scored) | U: an unidentified population geneticist relayed by the host. Arithmetic 7.2M exact. Fidelity `unverifiable`. |
| A5c | holds; ledger 13% | "four e-5" for 4.6e-5. Fidelity `unverifiable`: 1e-11 is non-standard. |
| A5 | holds | 690 vs 674 is 2.4% (rounding). |
| A2c, E5 | holds | -906 is in the paper, and a negative count is not a count. |
| B2e | holds | "Three orders" vs 700-820x is 2.85-2.9 decades. The draft ratio is stated three ways with [CHECK] marks, so it goes to the ledger (R1d). |
| B4g | holds | No match or negligibility assertion (N3). The 2x reproduces (2.4e-8 vs 1.2e-8). |
| B6c, G2c | holds; fidelity partial | Conditional on his stated premise ("before the next mutation can occur"). Whether MITTENS is serial is fidelity (N1). |
| G2, G2a, G2e, G2f | holds; fidelity partial | The serial reading of G_f is a fidelity question (N1). |
| C5b | holds | The arithmetic and logic follow. External is pending. |
| A2d, A2h, A2i, A3x, A5f, B3i, B5, B5g, B6, B6b, B7, B7c, F1, F1b, F4, G1c, G2d, G3, G3a, G5, H6, A4b | holds | Exact identities, valid analogies, or qualitative points with no internal defect. |
| B4e, D1d | n/a | No argument to score (a position or coverage statement). |
| D1, D1a, D1b, D1c | pending | N5: secondhand, and the book is unread. |
| E1 | not scoreable | The file states there is no critic quotation. It should not count in any critic denominator. |

Blind critic tally: 0 errors.

## 2. Agreement rate per side

| Side | Nodes compared with the rescore | Exact internal-verdict agreement | Agreement on error vs no error |
|---|---|---|---|
| Day | 20 | 18/20 = 90% | 18/20 = 90% |
| Critic | 35 rows in the rescore table | 31/35 = 89% | 35/35 = 100% |
| Critic, not in the rescore | 16 (A2i, A5f, B5g, G1c, G2d, G2e, G2f, G3a, A4b, B4e, E1, D1, D1a-D1d) | no rescore row; none is an error in either the current files or my scoring | - |

Where we agreed on the verdict but cited a different clause (A2e, B3e, B9, C2, C7, D9a, G2g, G), section 1a records my basis. The differences that matter for future readers:
- **B3c:** the "companion paper" basis is outside the rule's definition of own text, which covers companion text only "where the claim cites it".
- **B9:** the Q105 basis does not hold up.
- **C2:** "d = 1 discrete" belongs to C2a, not C2.
- **D9a:** the exploratory run is external.
- **G:** the rescore reason "107 vs hundreds of orders" restates a framing that G's own claim file withdrew after R4 G1. 107 is valid as a log ratio.

## 3. Disagreements, and which reading the rule's text supports

| Node | Rescore | Blind | Which reading the text supports |
|---|---|---|---|
| **A3a** (Day) | AE: parts sum to 222M, not 410M (85%), "propagates to 205M" | holds + ledger | **Blind.** The epsilon definition requires "the most charitable reading of an ambiguous referent". Yoo's SDR metric is per lineage, so "187 Mb of SDRs" is ambiguous between per lineage and pairwise. The per-lineage reading reproduces 410M and 205M to 0.2%, and the claim file already records it. The rescore applied the same charity to critics: B5e's unstated basis is read so "the product stands as written", and B5c's 205M-unit question is moved to A3d (fidelity). A reader who treats "for a total of" as a strict sum of the three listed items gets 85%, so this is a judgement call. The rule's text favours the charitable reading, and the rescore does not record trying it. |
| **F** (Day) | NS, N2d: "a latency bound is not a throughput bound (own 'rate x (window - startup)')" | holds | **Blind.** S1 scores the Statement quotes and the Formal-statement derivation. No F quote asserts that latency bounds throughput; quote 2 says the opposite, which is the very "rate x (window - startup)" the rescore cites. The Formal statement attributes the "window ÷ latency" form to F1a, which is already NS. Scoring F as NS counts F1a's defect twice. F is not in the numeric denominator, so the 18/82 is unchanged. Day's all-file count falls by 1. |
| A3d (critic) | pending / unverifiable, "N2b/F" | holds / unverifiable | **Blind on internal.** N2b needs the author's own text to contradict the premise; Hancock's own text does not (he uses the two-lineage reading in B5c too). N5 covers truncated or unrecoverable conclusions, and "should be at least 360" is recoverable. The open question is whether he misread the comparator, which is fidelity. Neither verdict is an error. |
| C5 (critic) | holds / unverifiable via R1c | pending | **Blind.** R1c says "holds (or pending if the method is unretrieved)", and the rescore's own reason says "method unretrieved". Neither verdict is an error. |
| B5d (critic) | pending (N5, truncated) | n/a (U) | **Blind, narrowly.** U covers "a passage whose author is not identified", and B5d is that case. N5 also fits. Neither verdict is an error. |
| C5b (critic) | pending ("estimator is C1d") | holds | **Rescore, arguably.** The internal chain follows, but the estimator's validity is under check. Neither verdict is an error. |

Both Day disagreements lower Day's count. No disagreement raises a critic's.

## 4. Does the 18/82 vs 0/31 gap survive?

**Yes, in direction and in significance, under my scoring.**

| Scenario | Day | Critic | Fisher exact p |
|---|---|---|---|
| X1 as published | 18/82 = 22.0% | 0/31 | 0.003 |
| Blind scoring: A3a out (F is not numeric) | 17/82 = 20.7% | 0/31 | 0.003 |
| Blind scoring, critic denominator without E1 (no quote) and B5d (U) | 17/82 | 0/29 | 0.006 |
| Day low bound: also drop the four weakest Day calls (C2, C2b, B9, G2g) | 13/82 = 15.9% | 0/31 | 0.018 |
| Critic high bound: C5, B5c, A3d, B5f scored as errors under the alternative readings in sections 1b and 5 | 17/82 | 4/31 = 12.9% | 0.42 |

Two caveats belong next to the headline:
1. **Day's errors are mostly robust.** 13 of the 17 rest on the author's own table, equation or same-paragraph text (N2a/N2b/N2c), and would survive any reasonable reading.
2. **The critic zero holds only under the rule's tie-breaks.** It depends on four calls, and each goes the critic's way by a specific clause:
   - N1 for B5f's premise;
   - R1c for C5;
   - the choice of basis in N3 for B5c;
   - routing A3d to fidelity.

   I judge the rule's text supports the non-error reading in all four, so this is not misapplication. But if all four went the other way, the difference would no longer be statistically significant (p = 0.42). The honest headline is "a robust Day-side error count against a critic-side zero that rests on four tie-breaks".

## 5. Does the rule bite one side harder? Clause by clause

**N1 ("a false or contested premise is external").**
- *Who it shields.* Critics argue in short, single-document form. Their typical defect is a contested premise or a misreading of Day: full pipe (B5f), N = Ne with all sites neutral (B5a), 205M read as a two-lineage total (A3d, B5c), MITTENS read as serial (G2, G2a, G2e, B6c, G2c). N1 moves every one of these to external or fidelity.
- *Who is caught by its counterpart.* N2b catches contradictions with "the author's own text", and Day's typical arguments are multi-step and spread across many documents (39 Zenodo records plus blog replies). The more an author writes, the more exposure under N2b. Examples: B3e against B3a, C2b against its own paragraph, B9 against its own comment.
- *Is that bias?* Not by itself; self-contradiction is a real defect. But it does mean the 18/82 partly measures output volume. Two mitigations:
  - enforce the definition's "where the claim cites it" (B3c's companion-paper basis violates it);
  - test critics against their own other statements with the same diligence. Hancock's 205M two-lineage reading in B5c bears directly on his A3d doubling, and was not used.
- *N1 also shields Day,* when it is applied as written: B6a's Ne_anc, D9a's model choice, B3c's mechanism. The **rule file's test table** applies N3 with Yoo's Ne_anc against B6a ("at Yoo's Ne the term is 58 to 87% of 35M"). That is a contested premise value, so under N1 it is external. The rescore's actual reason (own table, R1b) is correct. The rule file's example should be corrected so later scorers do not copy it.

**N3 (omitted terms) together with R1a (size).**
- *The asymmetry.* N3 has a "conclusion survives, so holds" escape. R1a has none. Day's typical slip is a printed number in a long derivation: G's (1.01)^1474, where the conclusion survives on the log scale. Critics' typical slip is an omitted term in a short identity (ancestral polymorphism in B5c and B5e). The same "does the conclusion survive?" test therefore rescues the second form but not the first.
- *A free parameter.* N3 does not say which "conclusion" is tested: the literal match, or what the match is offered for. For B5c the rescore tested "neutral supply suffices" on the SNV basis (39.6M vs 35-37.8M). Hancock's retained figure, however, is an event count (152/2). On his own basis, the same term turns his "match" into a 45% overshoot.

**R1c (input looseness, plus or minus 25%).**
- Applied to a tail probability, a 25% change in Ne moves the result by more than 10 orders of magnitude. For exponentially sensitive outputs R1c can therefore rescue almost any figure.
- It was applied only to keruru's C5. It would equally rescue Day's exp(-pi^2 Ne/T) figures.
- Its own "pending if the method is unretrieved" was not applied.

**S2/S3 (scope).** The text is symmetric ("whichever side wrote it"). The asymmetry is in which comments became nodes:
- Day's Substack comments became error nodes: C7 and B9 (refresh items D-5a and D-5b).
- The critic comment-nodes from the same refresh (A2i, B3i, G5) are all sound.
- The one critic comment with a large slip (McCarthy's 35M, 75%) stays in the ledger because S3's "feeds an argument" test fails.

This is defensible, but node extraction is not covered by the rule, and that is where any bias would enter.

**F (fidelity exemptions).**
- *The tilt.* The standard-values list (human Ne about 1e4, mu 1.1-1.5e-8, 60-100 de novo mutations, genome size) contains the critics' usual inputs. Day's usual inputs are self-derived or non-standard: G_f, d, 205M, Ne 3,300, the 150M neutral sites. The result moved Day +11 to `unverifiable` and critics +4.
- *The contested exemption.* "Human Ne about 1e4" is exempt even though Day contests it as circular (B3h, C5a). Exempting a contested value from citation sits badly with N1's rule that contested premises are external.
- *Scope.* This affects only fidelity, not the 18/82.

**Denominator.** The "numeric" regex runs on the Formal statement, which contains the *audit's* own `derived:` lines. The critic denominator therefore includes:
- E1, which has no critic quotation;
- A4b, a qualitative point;
- B5d, an unidentified author under U.

Critic numeric files are mostly one-line identities, while Day's are multi-step derivations. A per-file rate does not adjust for the number of steps that could go wrong.

**When the rule was written.** The rule was written in the fix pass, after the verdicts were known. Its N2d examples are Day nodes: "a dilemma with a middle case" is G3b, and "not bottlenecked from a positive response" is A5d. That does not make the rule wrong. It does mean the rescore cannot serve as an independent test, which is why this audit exists.

## 6. Clauses I would revise, and why

1. **R1 epsilon:** require the scorer to record the charitable readings tried, including "parts versus total" readings of lists. Example: A3a.
2. **R1a and N3:** make the two symmetric. Either a printed slip over 25% that neither propagates nor flips the conclusion becomes a ledger entry ("slip; conclusion survives"), or N3 loses its escape. Also define N3's "conclusion" as the author's literal assertion (match or negligibility), tested on the **author's own basis** (B5c: events).
3. **R1c:** do not apply it to outputs that are exponentially sensitive to the loosened input, or test the conclusion rather than the printed figure. Enforce its own "pending if the method is unretrieved" (C5).
4. **N1 and N3 boundary:** an "omitted term" is a term absent from the author's model, not a different value for a term the author included (B6a's Ne_anc). Any external value used in N3 must be the same for every node it is applied to (one Ne_anc for B6a, B5c, B5e).
5. **N2b:** keep "own text" to the same source and to texts the claim cites (B3c's companion-paper basis fails this). Record cross-document inconsistency as a separate flag counted for both sides, and apply it to critics' other statements, such as Hancock B5c against A3d.
6. **S1, for the claim files:** the sentence that carries a verdict must be quoted in the Statement. Missing at present: C2b's "increasing accuracy the further back"; B5f's CHLCA premise, which belongs to a different author. Otherwise a blind scorer cannot apply the rule. Fix the B5f/B5 attribution (justatest90, comment pcug1j0, not Dumb-and-Dumber).
7. **U:** apply it consistently. B5d (relayed, unidentified) should be `n/a`. C2b's regression (an unidentified "doctor") should be excluded, leaving only Day's interpretation to score.
8. **Denominator:** define "numeric" by the author's quoted text, not by the audit's `derived:` lines. Drop E1 (no quote) and U-excluded nodes. Report the count of derivation steps per side beside the per-file rate.
9. **F:** remove "human Ne about 1e4" from the exempt standard values, or mark it as contested-standard, since one side disputes it.
10. **Bookkeeping:**
    - F's NS duplicates F1a's.
    - G's rescore reason repeats a withdrawn framing.
    - C2's "d = 1" basis belongs to C2a, which is itself `holds`.

    Each should be fixed at integration.

## 7. Bottom line

- **Application.** The rule was applied with about 90% agreement on both sides. No case was found where the rule's text required a critic error that the rescore withheld.
- **Disagreements.** The two that change a count both remove Day errors: A3a by the rule's own charity clause, and F by S1. The numeric figure goes from 18/82 to 17/82. Both rest on the rule's text.
- **The gap.** It survives: 17/82 against 0/31, p = 0.003.
- **What the headline should carry.** Its strength rests on Day's own-text contradictions, which are robust. The critic zero rests on four tie-breaks (N1, R1c, the N3 basis, and routing A3d to fidelity), each of which favours the critics' typical argument form. The rule as written also tilts in form: N3 has an escape that R1a lacks, R1c rescues exponentially sensitive figures, and the F exemptions match the critics' inputs.
