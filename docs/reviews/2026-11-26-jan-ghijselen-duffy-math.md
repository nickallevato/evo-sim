# Review: "Will Duffy's math on Gutsick Gibbon's channel." (Jan Ghijselen, YouTube) and Day's reply

_Not an audit check; no claim file, verdict or count changed._ <!-- D-41: one neutral review per source; both sides at equal depth (hard rule 1) -->

**Source.** Jan Ghijselen (channel name; handle @DeDzjang), [www.youtube.com/watch?v=nTVRiEcswI8](https://www.youtube.com/watch?v=nTVRiEcswI8), uploaded 2026-09-28 (video metadata), public, 4:53, about 380 spoken words (auto-captions). Fetched read-only 2026-11-26 with the pinned yt-dlp (no video) into gitignored `sources/raw/jg-1-2026-11-26/`, `nTVRiEcswI8.en.vtt` sha256 `0c9c3ea39028a2ec6d7f8a989b61c98dda8def3e764578ef95b49e69638e8822`, byte-identical to the copy the bibliography hashed on 2026-10-13. Comments, capped at 300, in `comments/nTVRiEcswI8.info.json` sha256 `51d19e3a013e1eae60807b411a4d03e8e4cff2c3e0234aa45f3344bc053e9b87`: 124 comments, 44 by Ghijselen, 12 of which state an argument or number and are reviewed here. Bibliography key JG-1 (`docs/research/sources/bib-critics.md`); source map [`ghijselen-jg1.md`](../research/math/sources/ghijselen-jg1.md); new maths object M-918, whose record asserts every number below that no earlier record holds. Day's reply, [Math Teacher Can't Math](https://voxday.net/2026/09/30/math-teacher-cant-math/) (2026-09-30), is quoted only where claim files hold its words verbatim (G2a, A2f), because no copy is on this disk and the brief allowed no fetch of it.

**Captions.** The text is automatic speech recognition. Its garbles are transcription, not the speaker's slips: "25 years times 1,000 400" is "times 1,400" split across two cues. All three quotes on file (DZ-01 to DZ-03) are exact substrings of the captions. DZ-01 and DZ-02 begin one 20-second chunk later than the quotes file says (t=00:04:14 and 00:01:06, not 00:03:52 and 00:00:44). Locators here are cue starts (`jg1@MM:SS`), comment ids (`jg1c#…`) and Day's paragraphs (`B2026-09-30@pN`).

**Rule U.** Ghijselen answers Will Duffy's presentation of the MITTENS arithmetic, not a Day text: "if we take the reasoning of Will Duffy" (jg1@00:20). The audit does not hold Duffy's words for the three lines Ghijselen attributes to him (Duffy's stream is the next review, GG-1). So each attributed line is checked against Day's own text: the 3.0 definition of G_f (G1), Duffy's live restatement DU-03, and the book's Appendix A chain as Day quotes it (G2g).

---

## 1. The argument

Ghijselen sets out Duffy's formula: 6,300,000 years divided by a 25-year generation and by 1,400 generations per fixation, times d = 1, gives 180 fixations. He reads 25 × 1,400 = 35,000 years as the time "for one gene to mutate and fixate" and says the formula assumes the next fixation starts only when the last one ends. Then he gives a reductio. On that reasoning, the New York marathon, with 60,000 runners taking 4 hours each, would take 240,000 hours (27 years) to finish. Runners run in parallel, "Well, the same goes with mutation and fixation."

> "It would have to take 25 * 1400 is 35,000 years for one gene." (jg1@02:33)

> "Of course you say that's not possible, they run parallel. Well, the same goes with mutation and fixation." (jg1@04:14, DZ-01)

He closes by saying a proper count needs "stochastics" and "the logarithm" (jg1@04:31), and gives none. In the comments he concedes the input and moves the target: "That number is not wrong per se. It is the formula whereby the result becomes one fixated gene per 35000 years" (jg1c#AbQQxek5pWp).

Day answered two days later. He transcribed the marathon passage (B2026-09-30@p6, accurate against the captions), titled the post "Math Teacher Can’t Math", and replied:

> "The math is not wrong because parallel fixation is clearly and specifically included in the calculation." (B2026-09-30@p7)

## 2. The maths, located and rebuilt

Both sides use one formula, F_max = t_div · d / (g · G_f) (M-001). The dispute is what G_f measures. On the **aggregate reading** G_f = T_obs / n_obs, the number of generations an observed population took per completed fixation, counted over a window whatever the overlap (Day's 3.0, G1 q1: 60,000/45.4 = 1,322). On the **serial reading** G_f is t_fix, the time one allele takes from origin to fixation. The two counts coincide only if fixations never overlap (M-706). Ghijselen takes the serial reading; Day's 3.0 text takes the aggregate one; the book's Appendix A, as Day quotes it, takes the serial one ("Therefore fixation must be sequential", G2g q1).

| Step | Equation (author's) | Inputs | Library object | Check |
|---|---|---|---|---|
| Duffy's count (jg1@01:03-01:49) | 6.3e6 × 1 / (25 × 1,400) | t_div 6.3e6 y, g 25 y, G_f 1,400 (2nd-edition value, M-003), d = 1 | M-711, M-001, M-110 (records) | 180 exactly: holds |
| Years per fixation (jg1@02:33, 03:04) | 25 × 1,400; 6.3e6 / 180 | as above | new M-918 | 35,000 both ways: holds. It is the mean spacing on the aggregate reading and one allele's time on the serial one |
| Marathon, serial total (jg1@03:32-04:14) | 60,000 × 4 h | 60,000 runners, 4 h each | new M-918 | 240,000 h = 10,000 d = 27.38 y ("27"): holds |
| Marathon, aggregate analogue | time per finisher at the line, W / n | constructed bound: all finish within the same 4 h | new M-918, M-706 | 0.24 s per finisher, concurrency 4 h / 0.24 s = 60,000; the serial count in 4 h is 1, the aggregate 60,000 |
| Rate vs latency (comments) | "one fixation every 35000 years" ⇒ serial | none | M-115 (record) | an average spacing holds at any overlap (3,600 s / 360 cars = 10 s per car): the inference fails |
| Logarithm (jg1c#AbOZjfoynVk) | 200 → 2e6 base pairs is "only 4 times longer" | 200, 2e6 | new M-918 | 2e6/200 = 1e4 and log10 1e4 = 4; the time ratio is 1e4 (exponent reading) or 2.738 (concurrent reading), never 4 |
| Neutral time (jg1c#AbPZ3OnnqSO) | "more than 10 000 generations" | Nₑ = 10,000 | M-914, M-918 | 4Nₑ = 40,000: consistent |

**Numbers, recomputed** from the authors' inputs only (each asserted in the record named):
- 6.3e6 / 25 = 252,000; 252,000 / 1,400 = 180; with the 3.0 value 1,322, 190.6 (M-711).
- 25 × 1,400 = 35,000 y; 6.3e6 / 180 = 35,000 y (M-918).
- 60,000 × 4 = 240,000 h; / 24 = 10,000 d; / 365.25 = 27.38 y; "27" is 1.4% low (M-918).
- At the bound where all 60,000 finish within one 4 h window: 4 h / 60,000 = 0.24 s per finisher; concurrency 60,000; serial count 1 against aggregate 60,000 (M-918).
- 2e6 / 200 = 1e4; log10 1e4 = 4; ln(2e6) / ln(200) = 2.738; for exponential durations H_2e6 / H_200 = 2.566 (M-918).
- 4Nₑ = 40,000 at Nₑ = 10,000 (M-918; 4 × 1e4 is M-914's).

Every number in the video reproduces. The one number in the comments that does not ("only 4 times") is a separate claim, scored in §4. The video's dispute is about what the model measures, not its arithmetic.

## 3. What holds

- **The video's arithmetic, all of it.** 180, 35,000 years, 240,000 hours, 10,000 days, 27 years (M-711, M-918). Ghijselen restates Duffy's 180 correctly, which the claim file G2b already records as "verified by an opposing critic".
- **The marathon is exact on the serial reading.** If G_f were one allele's time and fixations ran back to back, the count would be T/t_fix and the analogy's factor of n (240,000 h against 4 h) is what overlap buys (M-706: the aggregate count exceeds the serial one by the mean concurrency). His definitions in the comments, "Parallel is all marathon runners running simultaneously. Serial is that a runner only starts to run after another runner has already finished." (jg1c#AbOZjfoynVk), are M-706's two schedules.
- **The serial reading is in Day's own text.** The book's Appendix A, as Day quotes it, says "Therefore fixation must be sequential" and attaches the 180 to that (G2g q1). Day's 3.0 paper divides 252,000 by drift fixation times (66,000 and 20,000, giving 3.8 and 12.6) in s8.2, and his comment on McCarthy's post gives "1,000,000 years per neutral fixation" (4 × 10,000 × 25; mc1c#337074301, M-914). Those are serial readings. Day's ¶25 of 2026-10-01 concedes the Appendix A wording "could have worded it better" (G2g q2).
- **Mutation does run in parallel** (jg1c#AbLX0qTkveZ: about 60 new mutations per child; M-914 holds 60-100). Nobody disputes it; the dispute is fixation.
- **Day's transcription of the argument is accurate.** B2026-09-30@p6 matches the captions apart from punctuation and a repeated "marathon of New York NYC" (G2a).
- **Day's p7 holds for the 3.0 formula.** On G_f = T_obs / n_obs, T/G_f counts every fixation the observed window completed, overlapping or not, so no parallelism factor is owed (G1: holds; M-706). Duffy said the same live: "the number he's using in the math is already parallel fixation." (DU-03).
- **Day keeps "serial" and "all-cause" apart.** In the same post he gives "The SERIAL natural selection rate for the LTEE at 60k generations is ~24,500 generations per fixation" (B2026-09-30@p23, A2f), a different number from the all-cause 1,322. That number has no derivation in the corpus (M-004, blocked), but it shows his 1,322 is not meant as a serial rate.
- **Kimura's neutral rate is the right place to look.** Ghijselen's comment that Kimura showed "the time period of 6 mio years is more than enough time" (jg1c#AbTSnGMwWgS) agrees with the library's neutral count on Day's quoted inputs: 22.5M, or 16-20.5M lag-adjusted, against 20M (M-914). He gives no number himself.

## 4. What fails

### Errors (rule R1: correcting it moves the stated conclusion by >25% or flips it)

- **Ghijselen, "only 4 times longer" (jg1c#AbOZjfoynVk).** "the difference in fixation time between 200 and 2 million basepairs is not a factor of 10^4th (10000) longer, but only 4 times longer." The 4 is log10 of the ratio (log10 1e4), not a ratio of times. Reading A, where the base pairs are an exponent as he says ("the number of basepairs is the exponent"): ln(pⁿ) = n ln p is linear in n, so the ratio stays 1e4, and correcting 4 to 1e4 flips "only 4 times". Reading B, the most charitable (rule C): all the changes run at once and the completion time grows as ln k. Then the ratio is ln(2e6)/ln(200) = 2.738 (2.566 for exponential durations), and correcting 4 to 2.738 moves the stated number by −31.5%, past the 25% line. Under reading B the correction helps his conclusion ("far less than 1e4"), which survives. Under either reading the stated number is an arithmetic error. Reading B also needs all 2e6 changes segregating at once, which he supports only with "the data on sexual replication in animals with varying reproduction rates" and no source (rule F).
- **The video: none found.** Every number reproduces.
- **Day's reply: none found** in the held text. Its only numbers are Ghijselen's, transcribed accurately, and the 24,500 of p23, which has no derivation to check (M-004).

### Non-sequiturs and hidden premises (rules N, U)

- **The marathon against T/G_f.** Premises: runners overlap; fixations overlap. Conclusion: "that math is clearly uh wrong" (jg1@04:23). Implicit premise: 1,400 generations is one allele's time from origin to fixation, the analogue of 4 h per runner. On the aggregate reading the analogue of G_f is the time per finisher at the line, 0.24 s at the bound where all finish within the same 4 h, and the window divided by that time gives 60,000 finishers, the right count (M-706, M-918). The analogy therefore fits only the serial reading. Against Day's 3.0 formula it is a non-sequitur. Against the book's Appendix A chain, which calls the 180 sequential, it holds (G2g). So the claim file G2a's verdict (internal holds, fidelity partial) is the reading under which the statement is most defensible.
- **"That means you only consider one fixation every 35000 years. This means serial, not parallel." (jg1c#AbQMQjXiOHQ).** A mean spacing between completions says nothing about how long each takes or how many run at once. Duffy's highway is the counter-example: 3,600 s / 360 cars = 10 s per car, while each car takes 100 s on the road and ten overlap at a time (M-115). The step from "one every 35,000 years" to "serial" is the non-sequitur. The error he names, "it being a multiplication in the nominator" (jg1c#AbQQxek5pWp), is the product g × G_f, which only converts generations per fixation to years per fixation.
- **"To use a fraction to calculate this won’t cut it, cause it can not account for changes that run parallel over time." (jg1c#AbOED9OvX2Z).** A window divided by an observed throughput accounts for any overlap the observation contains (M-706). What a fraction cannot do is carry the overlap from one regime to another: that is the transfer question (M-103), a different objection.
- **"it’s only valid for neutral mutations in a group of non sexually reproducing organisms." (jg1c#AbOED9OvX2Z).** "non sexually reproducing" is right: the LTEE is clonal (M-103; A5f). "only … neutral" is not: the all-cause 1,322 includes beneficial sweeps (M-004).
- **Relays (rule U).** "he says it takes 1,400 generations to fix one gene" (jg1@01:26) and "the reasoning is you can only mutate and fixate another gene when this time period is over" (jg1@02:46) are Ghijselen's account of Duffy. Against Day's 3.0 definition and Duffy's DU-03 they misread. Against the book's Appendix A chain, which is the source of the 1,400 and the 180 (M-003), they are accurate. Whether Duffy presented the chain is for the GG-1 review. Per rule U, neither line is scored as Duffy's claim.
- **Day, p7 against the book.** "parallel fixation is clearly and specifically included in the calculation" holds for the 3.0 T/G_f. If the calculation meant is the book's 180, Day's own Appendix A says "fixation must be sequential" (G2g q1). That chain is a non-sequitur as quoted (G2g internal non-sequitur), and Day later said it could have been worded better (G2g q2). This is a tension between Day's sources (book, blog, paper), not within the reply, so it is noted, not scored. Hidden premise in p7: the 1,400 Duffy presented is the same kind of quantity as the 3.0 throughput.

## 5. Slips (rules R1, SC; ledger level)

- **"genes" for fixed mutations** (jg1@00:20 "the total number of genes fixated", jg1@00:46 "180 genes mutated and changed"; jg1c#AbLX0qTkveZ "60 genes"). Duffy's own word is "fixed mutations" (DU-02), and the 205M is a base-pair count. Check: no number moves, and the marathon point does not depend on the unit. Ledger.
- **"one gene out of 180 genes"** (jg1@01:52) contradicts his own "180 genes" before and after. Check: he computes with 180 throughout. Ledger.
- **"27 years"** for 27.38 (jg1@04:09): 1.4% low. Below any threshold.
- **"nominator"** for the denominator of F_max (jg1c#AbQMQjXiOHQ, AbQQxek5pWp). Check: the product he means, g × G_f, is right. Ledger.
- **"6.300,000. Sorry. 6,300,000"** (jg1@00:57): a decimal-point convention, corrected on the spot (rule SC). Not a slip.
- **ASR garbles** ("times 1,000 400") are transcription, not slips.
- **Day:** no slip in the held lines.

## 6. Rhetoric (rule RH)

| Quote (locator) | Device | Audience | Function | Dialectical core | Better answer (aimed at the move, never at the person) |
|---|---|---|---|---|---|
| "I am a math teacher in secondary education." (jg1@00:10, DZ-03) | credential (ethos) at the opening | viewers of the Duffy-Gutsick Gibbon exchange | authority for the critique | none; the argument is the marathon | "Whatever the credential, the question is a reading of the source: is 1,400 the time one fixation takes, or the spacing between completions?" |
| "Devastating results, says Will Duffy" (jg1@01:52) | irony: the opponent's word repeated to mock it | viewers | set up the reductio | Duffy's count of 180 | "Test the premise instead: 1,400 is not the fastest observed throughput; point-mutator lines run at 43-183 generations per fixation (M-711)." |
| "Vox’ 7th grade math, riddled with calculation errors" (jg1c#AbPL4ON-POa) | belittling label, unspecified charge | a commenter and readers | rank the opponent below the field | "calculation errors", none named; the 180 he presents reproduces (M-711) | "Name the error. The arithmetic holds; the open question is whether a clonal-flask throughput transfers to a recombining lineage (M-103)." |
| "If you want to know more about maths: ask a math teacher." (jg1c#AbQ_ZrVnAua) | appeal to the speaker's credential | a commenter who disputed him | close the exchange | none | "Show the step: write the count as T/G_f and say what G_f measures." |
| "Math Teacher Can’t Math" (B2026-09-30@title) | ridicule that turns the critic's credential (DZ-03) against him | Day's readers | discredit the critic before the argument | p7: G_f already includes parallel fixation | "The 1,400 is a count over a window, so its marathon analogue is runners per hour at the finish line, not hours per runner. That answers the analogy without a headline about the man." |

The captions carry the recogniser's tags "[sighs and gasps]" (jg1@00:46) and "[snorts]" (jg1@02:46, 02:59). They are not words and are not scored. In the comments Ghijselen says Day called for his firing; the audit holds no copy of that text, so it is not scored.

Rhetoric changes no verdict. Both sides use the credential: Ghijselen as his warrant, Day as his target. Both have a dialectical core beside it. Ghijselen's is that dividing a window by a per-allele time assumes seriality. Day's is that his G_f is not a per-allele time.

## 7. Verdicts under the audit's rule (informal; not entered in any claim file)

| Statement (locator) | Reading | Internal | Fidelity | External | Note |
|---|---|---|---|---|---|
| "The length of a generation for humans is 25 years times 1,000 400" with "we reach the number 180" (jg1@01:15, 01:40, DZ-02) | as stated | holds | accurate | n/a | M-711; as G2b |
| "So, he says it takes 1,400 generations to fix one gene." (jg1@01:26) | an average: one fixation per 1,400 generations | n/a | accurate | n/a | **reading-dependent**; field value; G1 q1, DU-03 |
| | a latency: one allele takes 1,400 generations | n/a | partial | n/a | misreads 3.0 and DU-03; matches Appendix A (G2g) |
| "the reasoning is you can only mutate and fixate another gene when this time period is over." (jg1@02:46) | of the book's 180 (Appendix A) | n/a | accurate | n/a | **reading-dependent**; field value; whether Duffy presented the chain is GG-1 |
| | of the formula T/G_f with the 3.0 G_f | n/a | misread | n/a | G1 q1; DU-03 |
| "It would have to take 25 * 1400 is 35,000 years for one gene." (jg1@02:33) | as arithmetic | holds | accurate | n/a | M-918; "for one gene" is the serial reading (row above) |
| "Of course you say that's not possible, they run parallel. Well, the same goes with mutation and fixation." with "So, that math is clearly uh wrong." (jg1@04:14, 04:23, DZ-01) | against the serial reading (Appendix A chain) | holds | partial | n/a | **reading-dependent**; field value; as G2a |
| | against T/G_f with G_f = T_obs / n_obs | non-sequitur | misread | n/a | implicit premise G_f = t_fix (M-706, M-918) |
| "we would really need stochastics. And we have to use the logarithm." (jg1@04:31) | as stated | n/a | n/a | contested | no model given; M-101 (an average needs none), M-103 (transfer needs one) |
| "That means you only consider one fixation every 35000 years. This means serial, not parallel." (jg1c#AbQMQjXiOHQ) | 35,000 y is each fixation's duration, one completing every 35,000 y | holds | partial | n/a | **reading-dependent**; field value; spacing = duration is M-706's back-to-back case; misreads 3.0, matches Appendix A |
| | 35,000 y is the spacing between completions | non-sequitur | misread | n/a | M-115: a spacing says nothing about overlap |
| "…not a factor of 10^4th (10000) longer, but only 4 times longer." (jg1c#AbOZjfoynVk) | concurrent completion, time ∝ ln k | arithmetic-error | unverifiable | n/a | **reading-dependent**; field value; 4 → 2.738, −31.5% (R1), in his favour; premise uncited (rule F) |
| | base pairs as the exponent of pⁿ | arithmetic-error | unverifiable | n/a | 4 → 1e4, flips |
| "it’s only valid for neutral mutations in a group of non sexually reproducing organisms." (jg1c#AbOED9OvX2Z) | valid only for a clonal regime | holds | partial | contested | **reading-dependent**; field value; M-103, A5f; "neutral" misdescribes the all-cause count (M-004) |
| | valid only for neutral change | non-sequitur | misread | n/a | the 1,322 includes beneficial sweeps |
| "That is precisely where Kimura showed the time period of 6 mio years is more than enough time…" (jg1c#AbTSnGMwWgS) | as stated | holds | n/a | contested | M-914 (22.5M; 16-20.5M lag-adjusted; Day's quarter-neutral 5.6M); M-111 |
| "I know babies differ in plusminus 60 genes from their parents. This alone shows mutation runs parallel…" (jg1c#AbLX0qTkveZ) | of mutation | holds | n/a | supported | not in dispute; "genes" is a slip (§5) |
| "It would mean that if you have the Marathon of New York…" (B2026-09-30@p6) | as a transcription | n/a | accurate | n/a | matches jg1@03:21-03:56 |
| "The math is not wrong because parallel fixation is clearly and specifically included in the calculation." (B2026-09-30@p7) | of the 3.0 T/G_f | holds | n/a | contested | **reading-dependent**; field value; as G1 (holds, contested on transfer) |
| | of the book's 180 as Appendix A presents it | non-sequitur | n/a | n/a | Day's own "fixation must be sequential" (G2g) |

Rule RD: where the verdict depends on the reading, every plausible reading is listed, and the field value (the first row) takes the reading under which the statement is most defensible. Seven statements are reading-dependent: six Ghijselen, one Day. For the "4 times" row the internal verdict is the same under both readings; only the size of the correction differs. Rhetoric rows (§6) carry no verdict.

**Candidates for claim files** (not applied; for the lead): G2a's Statement locator t=00:03:52 should be t=00:04:14, and G2b's DZ-02 locator t=00:00:44 should be t=00:01:06 (and DZ-01 and DZ-02 in `quotes-critics.md`). G2a's "Weaknesses in the responses" quotes the comments without a locator; the comment id is jg1c#AbLX0qTkveZ. G2a could also record Ghijselen's concessions "the marathon comparison isn’t perfect" (jg1c#AbOZjfoynVk) and "That number is not wrong per se" (jg1c#AbQQxek5pWp). G2b's implicit d = 1 is stated in the source ("times one because D is substituted by one", jg1@01:40).

## 8. Day-side steelman

Ghijselen's analogy misses the formula it attacks. MITTENS's G_f is a count over a window, T_obs / n_obs, not a per-allele time. It records every fixation the LTEE populations completed, however many overlapped (G1 q1, M-706). Its marathon analogue is the time per finisher at the finish line, 0.24 s at the bound where all finish within one 4 h window, not 4 h per runner. A window divided by that gives 60,000 finishers, the right count at any overlap (M-918). Duffy made exactly this point live ("the number he's using in the math is already parallel fixation", DU-03), and Day's p7 makes it again. Ghijselen's own comments give the rest away. He grants "That number is not wrong per se" and places the error in "a multiplication in the nominator", the product g × G_f, which only converts generations to years. He infers seriality from "one fixation every 35000 years", which is a rate, and a rate is silent on overlap (M-115: 360 cars in 3,600 s is 10 s per car although each spends 100 s on the road). The "absurdity" he points to, one fixation per 35,000 years, is not a reductio of MITTENS. It is MITTENS's conclusion restated: at the observed throughput a human lineage gets 180 fixations in 6.3 My. To answer it one must show that the human throughput is higher, and the video does not try. Everything he computes reproduces (M-711, M-918), so "riddled with calculation errors" has no instance. The one new number he offers, "only 4 times longer", is wrong under every reading (1e4, or 2.738). He concedes he is "not schooled on this subject" and that "the marathon comparison isn’t perfect", and the promised stochastics never arrive. Day transcribed the argument accurately (p6) and keeps "SERIAL" (p23, ~24,500) separate from the all-cause 1,322. Mutation in parallel, the 60 new mutations per child, is common ground. MITTENS counts fixations, not mutations.

## 9. Critic-side steelman

The serial reading is not Ghijselen's invention. It is how Day's book presents the very numbers Duffy showed. The 1,400 and the 180 come from the second edition (M-003), and the book's Appendix A, as Day himself quotes it, says "Therefore fixation must be sequential" and attaches the 180 to that (G2g q1). Day's s8.2 divides the window by drift fixation times (252,000 / 66,000 and / 20,000), and his comment on McCarthy's post prices "1,000,000 years per neutral fixation" (mc1c#337074301, M-914). Those are serial calculations in Day's own text. Day later conceded the Appendix A wording "could have worded it better" (G2g q2). So against the book, the marathon lands, and the claim file G2a scores it internal holds. DU-03 was said live, after the challenge, and does not rewrite the book. Even on the aggregate reading the critic's point survives in a stronger form. The throughput was measured in a clonal flask with no recombination, and how much overlap a population sustains is exactly what differs between regimes. The audit's own runs find free recombination keeps concurrent sweeps near full speed (R_int 0.975) where clonal linkage cuts them to 0.088 (R4 F2-A; A5f). Ghijselen's "non sexually reproducing organisms" (jg1c#AbOED9OvX2Z) is that objection in plain words, and "Never can an average account for variety" (jg1c#AbRnhzCYTin) is M-101's critic position: one G_f from one regime is a transfer assumption, not a constant. Nor is 1,400 the fastest observed, since point-mutator lines run at 43-183 generations per fixation (M-711). His Kimura comment points where the library's neutral count lands: on Day's quoted inputs about 22.5M, 16-20.5M lag-adjusted, against 20M required (M-914). Day's reply does not say which text the 180 he defends belongs to. It answers with a headline about the man ("Math Teacher Can’t Math") and a sentence ("clearly and specifically included") that his own Appendix A contradicts.

## 10. Bottom line

The video's arithmetic is right throughout. Its one argument, the marathon, is valid against a serial count and misses an aggregate one. Which of the two MITTENS is depends on the text: Day's 3.0 definition and Duffy's live reply say aggregate, and the book's Appendix A, which supplied the 1,400 and the 180, says sequential. The comments add a concession ("not wrong per se") and an inference from a mean spacing to seriality that fails (M-115). They also add one number, "only 4 times", that is wrong under every reading. Day's reply transcribes the argument accurately and is right for the 3.0 formula, but it does not engage his own book's wording and leads with ridicule. The critics may fairly take the serial wording in Day's book and the transfer question (M-103, A5f). Day may fairly take the throughput definition, the reproduced 180 and the misplaced analogy. Nothing here is new maths beyond M-706 and M-115. The new object M-918 holds only the arithmetic.
