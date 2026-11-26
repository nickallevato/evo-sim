# Review: "Vox Day Responds" (Dennis McCarthy, Substack) and his replies in the comment thread

_Not an audit check; no claim file, verdict or count changed._ <!-- D-41: one neutral review per source; both sides at equal depth (hard rule 1) -->

**Source.** Dennis McCarthy (byline of his Substack *All The Mysteries That Remain*), [dennismccarthy.substack.com/p/vox-day-responds](https://dennismccarthy.substack.com/p/vox-day-responds), `post_date` 2026-09-17 (API JSON; a free repost of a paid post of 2026-02-03, which is out of scope), public, 4,174 words (API `wordcount`). His 26 replies in the post's comment thread run from 2026-09-17 to 2026-11-01. Fetched 2026-11-26 into gitignored `sources/raw/mccarthy-mc2-2026-11-26/`, `post.json` sha256 `2f4dd85499c6840bb583bf7dcc76262647f0117ef553f49b80746c8a7b81ffa6`; the thread is item 1's held copy `comments-vdr.json` sha256 `4bdd3432f791d126f36c1ac7fe3c4401eb460063963f9d5a8ee5a5a22bb8c51d` (hash rechecked). Bibliography keys MC-2, MC-2c (`docs/research/sources/bib-critics.md`); source map [`mccarthy-mc2.md`](../research/math/sources/mccarthy-mc2.md). Locators: `L<n>` is a line of the post text, `#<id>` a comment id in this thread, `mc1c#<id>` a comment in the thread of his earlier post.

**Version.** The post was edited after the audit first filed it: `updated_at` is 2026-10-31T16:37, and the hash differs from the 2026-10-07 bib hash. The earlier text is not held, so the two versions cannot be compared. Four of the five quotes on file (MC-08, MC-10, MC-11, MC-12) are word for word in the current text. MC-09 ("400 billion x 1/20,000 =20 million fixations … the exact correct result") is not; it is word for word in McCarthy's comment mc1c#337116873, and with the owner's approval (EVOA-107) the quotes file now points there. Where MC-09 was filed, the post now gives 18 and 16 million (L16). **This page reviews the post as it reads today and does not claim McCarthy corrected himself**; only the times are known: the edit came 15 minutes after a reply in which he gives the same rate (#375157428).

Speciation, fossils and biogeography (L23–L95) carry no maths and are out of scope. Day's book is not held; where McCarthy quotes it, or Day's comments from the earlier thread, this page checks the quote against the held comment where one exists and otherwise takes it as quoted (rule U).

---

## 1. The argument

McCarthy answers Day's replies to his first post ([item 1](2026-11-26-dennis-mccarthy-probability-zero-wrong.md)), quoting each and setting "His mistake" under it. Four are mathematical: the Darwillion again (L8–L9), Day's 4Nₑ time objection (L10–L17), the neutral share (L18–L19) and the 410 million base-pair figure (L20–L21). A fifth paragraph argues the divergence dates are themselves derived from Kimura's theory (L22). On the time objection he rebuilds the count per generation:

> "Over 360,000 generations, that gives 18 million expected substitutions in the long-term neutral model. Over 320,000 generations gives 16 million substitutions." (L16)
> "Across the genome as a whole, only 3% of new mutations are deleterious." (L19, MC-10)
> "The 410 million base pair difference refers to structural variation, which includes duplications, insertions, etc., in which a single mutational event can cause hundreds, thousands, or even millions of base-pair differences." (L21, MC-11)

In the thread he argues with Dene Scoggins over whether he has misread Day (serial fixation, the "law of large numbers", population growth, Haldane), and with Day, who restates his thesis as one about natural selection and quotes the MITTENS 3.0 abstract (#340102853).

Who is argued against: Day, through McCarthy's quotations of Day (rule U). Two of these can be checked against held comments. The 4Nₑ quote (L10) matches mc1c#337074301 word for word. The neutral-share quote (L18) matches mc1c#337302874 in its words, but McCarthy's ellipsis cuts two things from that comment: Day's qualifier "Which doesn't matter when I'm just pointing out the scale of the improbability, but when you're trying to prove that yes, it is actually possible, then you have to run the real numbers.", and, later in the same comment, his denial that he assumes serial fixation (parallel drift is a defence "so obvious that I devoted Chapter 10 to it"). The 410 Mb quote (L20) is from the book's second-edition introduction, which the audit does not hold.

## 2. The maths, located and rebuilt

**Model.** The model is the same textbook neutral count as item 1, now per generation: 2Nₑ gene copies × new neutral mutations per copy × 1/(2Nₑ) × generations. The window is 9 My at 25 years, with or without the 4Nₑ lag. Every new mutation is treated as neutral in the count (L13), though L19 puts the deleterious share at 3%. The thread adds the throughput argument: transit time is not the interval between fixations.

| Step | Equation (author's) | Inputs | Library object | Check |
|---|---|---|---|---|
| Darwillion (relayed) | (1/20,000)^20,000,000 = 10^−86,000,000 | L8 | M-703 | rounding (86,020,600); answered by specific vs any, [item 1](2026-11-26-dennis-mccarthy-probability-zero-wrong.md) §3 |
| Neutral count, post text | 400 billion × 1/20,000 = 20 million | L9 | M-914, M-915 | holds as written; 400 billion is the 20-year supply (item 1's mixed basis) |
| Day's transit (relayed) | 4 × 10,000 = 40,000 generations × 25 y = 1,000,000 years | L10 | M-203, M-914 | holds |
| Per-generation count | 20,000 × 50 = 1,000,000; × 1/20,000 = 50 per generation | L12–L15 | M-212, M-915 | holds |
| Revised totals | 360,000 × 50 = 18 million; 320,000 × 50 = 16 million | L16 | M-914, M-915 | holds; 25 y throughout |
| Throughput (thread) | "approximately two million … per million years" while each takes "one million years" | #375157428 | M-706, M-915 | holds: 50 × 40,000 = 2×10⁶/My; about 2×10⁶ alleles in transit at once |
| Neutral share | Day: 3 harmful : 1 neutral; McCarthy: 3% deleterious, the 3:1 only in coding (1.5%) | L18–L19 | M-222, M-915 | both uncited; 4.0–4.5 million against 15.5–17.5 million |
| 410 Mb (relayed) | "13.8 percent", "410 million base pairs", "10x increase" | L20 | M-009, M-011, M-915 | 410/35 = 11.7; 13.8% implies a 2.97×10⁹ base |
| MITTENS 3.0 (Day) | 252,000/1,400 = 180; "0.000088%" of 205 million | #340102853 | M-711, M-915 | holds (0.0000878%; shortfall 1,138,889) |
| Kelvin (Day) | 20 million to 4.54 billion years, "a factor of 227x" | #339543355 | M-915 | holds |
| k = μ at any N | doubling N halves p_fix and doubles supply | #375855613 | M-209, M-208 | holds at equilibrium; lags after a size change |
| Day's "Corrected Calculation Using Actual Values" (Matev quoting Day's blog) | 330,000 × 400,000 = 132 billion × 1/16×10⁹ = 8.25; "133x to 2,424,242x" | #345248135 | M-209, M-212, M-915 | 8.25 and 2,424,242 hold; "133x" does not reproduce; the N/Nₑ step is the retracted one (M-209) |

**Numbers, recomputed** from the authors' inputs only (each asserted in `records/M-915.py` unless another record is named):
- 2Nₑ × 50 = 10⁶ new neutral mutations per generation; × 1/20,000 = 50 fixations per generation.
- 360,000 × 50 = 18 million (−10% against the 20 million required); 320,000 × 50 = 16 million (−20%). The 16 million is the single-basis figure item 1 computed (M-914).
- The same post's L9 still has 400 billion × 1/20,000 = 20 million. 400 billion is 25% above the post's own 320,000 × 10⁶ = 3.2×10¹¹; put on L16's basis, L9 falls 20%.
- 50 × 40,000 generations per My = 2×10⁶ fixations per million years. With a mean transit of 1 My, about 2×10⁶ alleles bound for fixation are in transit at any time (rate × time in system). × 9 My = 18 million, × 8 My = 16 million.
- Neutral share: at MC-10's 3% deleterious, 0.97 × 18 / 16 million = 17.46 / 15.52 million. At Day's 3:1 (share 1/4), 4.5 / 4.0 million. The two inputs differ 3.88-fold, and the choice moves the count by −74%. McCarthy's scope claim is consistent with his own figure: 1.5% coding × 3/4 = 1.125% of all new mutations, under 3%.
- Day's figures as relayed: 410/35 = 11.7 ("10x"); 410×10⁶/0.138 = 2.97×10⁹, the base the 13.8% implies; on McCarthy's 3.2×10⁹ (L19) it is 12.8%.
- Thread: 400/6 = 66.7, against the 410/6 = 68.3 Day asked for (M-914); 4.54×10⁹/2×10⁷ = 227; 180/205×10⁶ = 0.0000878%; 1.32×10¹¹/1.6×10¹⁰ = 8.25; 2×10⁷/8.25 = 2,424,242. "133x" does not follow from the inputs quoted (the "original" 4×10¹¹ × 1/20,000 = 2×10⁷ against 2×10⁷ is a factor of 1).

The arithmetic holds. The post keeps one leftover from the old basis (L9 against L16). The neutral share is decisive, and neither side cites a source for its figure.

## 3. What holds

**For McCarthy (critic side).**
- *The revised count is right and on one basis.* 50 a generation, 16–18 million over the window, within 20% of the 20 million required (M-915). This is item 1's lag calculation with the generation length fixed at 25 years throughout.
- *Transit time is not throughput.* Two million fixations per million years with each taking a million years means about two million alleles in transit at once. "1,000,000 years per neutral fixation" read as one fixation per million years is the serial reading (M-706). Matev (#375583044) states the error the same way.
- *Base pairs are not mutation events* (MC-11). The audit agrees: claim A3x is internal `holds`, external `supported` (R4 GAP-07b counts 42.1 million events, 21.05 million per lineage). A requirement stated in base pairs does not feed an event-count model (M-011).
- *k = μ does not depend on N* (#375855613): "when the population doubles the probability that any mutation will fix is cut in half—but the number of mutations double and this cancels out". This is the standard result (M-209; claim B7 external `supported`). Matev's reductio of Day's k = μN/Nₑ, that the summed fixation probability 2N/(2Nₑ) exceeds one (#345248135), is the same object.
- *Haldane's cost is a cost of selection* (#375371851): neutral substitutions pay none (M-801 is a beneficial-substitution budget).

**For Day.**
- *The neutral share decides the count, and McCarthy's 3% has no source.* Day's 3:1 has none either (B9 fidelity `unverifiable`). Under Day's input the 16–18 million becomes 4.0–4.5 million, a fifth of the requirement (M-915). The post moves the burden to Day without meeting it. There is common ground here: a 3:1 ratio in coding sequence is roughly what the coding dN/dS of about 0.21–0.27 the audit used in B9 implies (if synonymous sites are neutral, about three in four amino-acid changes are removed). So both figures can be true at once, and the open question is the non-coding share.
- *Day denies the serial view McCarthy attributes to him.* The comment McCarthy quotes at L18 is the one in which Day writes that parallel drift is "so obvious that I devoted Chapter 10 to it" (mc1c#337302874). L11 repeats the charge without that sentence; Scoggins points this out (#375077052).
- *Day's thesis is about natural selection, and the post's evidence sections do not reach it.* "no vertebrate mammalian species has ever originated through evolution by natural selection, by genetic drift, or any combination thereof" (#339391408). Pattern evidence (L2–L4, fossils, islands) shows ancestry, not that a mechanism was fast enough. Scoggins: "No one here is denying ancestral taxa, only the pace, the rate" (#364174390). The walk analogy (#339391408) makes the same valid point.
- *Population growth matters in a narrower form than Scoggins puts it.* k = μ holds once a size has been held for about 4Nₑ generations; after a change, the rate delivered lags (M-208; B1b external `pending`). McCarthy's "independent of population size" is the equilibrium statement.
- *Day's own arithmetic in the thread holds*: 227 for Kelvin, and 180, 0.0000878% and 1,138,889 for MITTENS (M-711, M-915).

## 4. What fails

### Errors (rule R1: correcting it moves the stated conclusion by >25% or flips it)
None in the arithmetic of the post or of McCarthy's replies. The one flip in the exchange is an input, not a slip: the neutral share moves the count by −74% (3% against 3:1, M-915). Both inputs are uncited (rule F), so neither side's figure is scored as an error here; both are `unverifiable`. Day's "133x" (in a quote by Matev of a Day blog post the audit does not hold) does not reproduce from the inputs quoted with it. It is not scored (rule U).

### Non-sequiturs and hidden premises (rules N, U)
- **"a few pages in a textbook … would need to be revised" (L6) against "population geneticists actually use Kimura’s neutral-theory result to date the human–chimpanzee divergence" (L22).** *Implicit* in L6: nothing else rests on the equation. By L22, the 6–9 My dates do too, so a wrong equation would move the time window that every count in the exchange uses. The two lines pull against each other within the post (rule N). L6 holds if read narrowly (the evidence for common descent would stand).
- **"he incorrectly claims only one mutation can fix at a time" (L11).** As a claim about what Day believes, it is contradicted by the comment McCarthy quotes at L18 (fidelity). As a claim about what Day's "1,000,000 years per neutral fixation" implies if read as throughput, it holds (M-706). The page takes the second, more defensible reading (§7).
- **"20 million mutations that have been observed" (L9).** 20 million is Day's required count (M-008), not an observed tally of fixations. The library puts fixed SNVs at 13.7–15.1 million per lineage once polymorphism is removed (M-008).
- **The Iceland analogy (#340149310, #340151868).** *Implicit:* standing variation that spreads in a founder population stands in for new mutations fixing. It shows that allele frequencies change together. It does not show concurrent fixation of new mutations, which the 2×10⁶-in-transit figure shows directly.
- **"never once challenged natural selection or rate of beneficial mutations" (#339603943).** Contradicted by the MITTENS abstract Day quotes two replies later ("natural selection can accomplish at most 180 fixations", #340102853) and by McCarthy's own reply of the same day: "Vox is literally claiming evolution by natural selection has never occurred" (#339324948). It holds only for the equations McCarthy rebutted, whose 1/20,000 is the neutral fixation probability.
- **Day: "Kimura and neutral theory don't even begin to enter into it" (#340102853).** Of the MITTENS bound, this holds: F_max has no mutation rate, population size or selection term (M-713). Of Day's case in this exchange, it does not: the Darwillion's 1/20,000 and the 4Nₑ reply are neutral-theory quantities Day put forward himself (rule N).
- **Scoggins: growth drives fixation "toward zero" (#375422209).** *Implicit:* supply does not grow with N. It does (2Nμ), and the two cancel. What survives is the transient (M-208).
- **Scoggins's "law of large numbers" against drift (#375229688, #375301394).** The Bernoulli Barrier is an argument about the fitness differential under selection (M-701, M-702), so it does not bear on neutral drift. McCarthy's challenge to explain it (#375243661) was answered with PZ p. 159, and his next reply does not take up those numbers. The library's answer is M-701: 14.7 and 1,570 are additive quantities printed as ratios.
- **"It has already been demonstrated that Haldane's limit does *not* set a ceiling" (#375371851).** No source is given (rule F); the library's object is M-803 (Nunney 2003).

## 5. Slips (rules R1, SC; ledger level)

- **L9 against L16 (same post).** L9's 400 billion × 1/20,000 = 20 million keeps the 20-year supply; L16 uses 25 years throughout and gets 16 million. **R1 check** (M-915): the stated conclusion is the match with the 20 million required; on L16's basis L9 moves −20%, within 25%: **ledger**. The same post carries the consistent figure (rule SC, ledger either way). The 20 million reappears five hours after the edit at #375371851.
- **MC-09.** Not in the current post; word for word at mc1c#337116873, where item 1 recorded it (RF-7: mixed basis, ledger). No correction is claimed (see Version).
- **"divide 400 million by 6 million" (#339716645)** for Day's 410 million (−2.4%; the reply is rhetoric).
- **L21:** "apply exclusively to the roughly 35 million single nucleotide differences" leaves out the 5 million indel events in Day's 2025 count (M-008). No conclusion moves.
- **L13:** "Assume 50 new neutral mutations per gene copy" treats all 100 new mutations per person as neutral, while L19 says 3% are deleterious: 18 against 17.46 million (−3%).
- **Day's text as relayed (L20):** "10x" for 410/35 = 11.7; "13.8 percent" implies a 2.97×10⁹ base, against 12.8% on 3.2×10⁹. The book is not held (fidelity `unverifiable`); not scored.

## 6. Rhetoric (rule RH)

| Quote (locator) | Device | Audience | Function | Dialectical core | Better answer (aimed at the move, never at the person) |
|---|---|---|---|---|---|
| "The more opaque and technical the argument, the better, because it dazzles naive believers." (L3) | motive attribution | general readers | discounts the maths before it is read | rate against pattern (§3) | Say once that pattern evidence and a rate bound are different questions, then answer the rate (L12–L17 do). |
| "And, of course, Day has not shown that Kimura’s equation is wrong. The errors he points out are all his own." (L7) | turn-around | readers | frames the exchange | Day's k = μN/Nₑ and its later concession (M-209) | Cite the concession and the cancellation; let the record carry it. |
| "But does he seriously think that only one mutation out of many millions can sweep through a population at a time?" (L11) | incredulous question | readers | ridicules a view Day disowns | M-706 | Quote Day's Chapter 10 sentence, then show the 2×10⁶-in-transit figure: whatever he intends, a 4Nₑ transit costs only the lag. |
| "Are you actually arguing God (or aliens) just keep zapping increasingly more modern animals into existence" (#338945912) | false alternative, ridicule | thread | shifts the burden | Scoggins's "rather what causal mechanism is feasible" (#338940602) is the rate question | Grant the distinction and answer the rate with the count. |
| "ZERO known facts contradict evolutionary theory." (#344346806) | universal claim | thread | reassurance | none | Name the specific claim and the specific check. |
| "And do you really think I can’t divide 400 million by 6 million?" (#339716645) | indignant question | thread | rejects the test | Day's question presupposes base pairs as events (M-011) | Answer the unit: 410 million base pairs is not 410 million mutation events (A3x). |
| "I am specifically and literally claiming that no vertebrate mammalian species has ever originated through evolution by natural selection, by genetic drift, or any combination thereof." with the New York–Los Angeles walk (#339391408) | analogy (Day) | thread | separates "it happened" from "how" | valid: pattern evidence does not test a rate | Hold the analogy to its premise: the walk is impossible only if the speed limit is right, which is the open question (A, B). |
| "All of that evidence can, must, and will be tossed aside." (#339661243) | finality (Day) | thread | puts the model above the data | the maths, which is what is in dispute | Say what observation would count against the model. |
| "It's now evident that you're simply not tall enough for this ride." (#340154038) | ad hominem (competence) (Day) | thread | ends the exchange | none in the comment | Name the step in McCarthy's maths that fails. |
| "In fact, it made them approximately ten times more conclusive." (L20, Day relayed) | amplification | readers | upgrades the conclusion | 410 Mb as a requirement (M-011) | State the requirement in events and recompute. |
| "you haven’t in fact read his argument, as he explicitly argues the opposite" (#375077052, Scoggins) | competence charge | thread | fidelity | correct as to Day's stated view (mc1c#337302874) | Quote the denial; the substance is M-706. |
| "Well go ahead, right here and now, explain that." (#375243661) | challenge | thread | shifts the burden | the Bernoulli Barrier (M-701) | Engage the p. 159 numbers once Scoggins gives them. |

The same standard applies to all sides. Rhetoric changes no verdict.

## 7. Verdicts under the audit's rule (informal; not entered in any claim file)

| Statement (locator) | Reading | Internal | Fidelity | External | Note |
|---|---|---|---|---|---|
| "Over 360,000 generations, that gives 18 million … Over 320,000 generations gives 16 million substitutions." (L16) | as stated | holds | n/a | contested | as claim B5a; neutral share open |
| "400 billion x 1/20,000 = 20 million mutations that have been observed" (L9) | as written | holds | n/a | contested | slip against L16 (−20%), ledger |
| "he incorrectly claims only one mutation can fix at a time" (L11) | Day's "per neutral fixation" read as throughput implies serial fixation | holds | partial | contested (G2) | **reading-dependent**; field value under this reading |
| | Day believes only one can fix at a time | n/a | misread | n/a | Day denies it (mc1c#337302874) |
| "approximately two million neutral mutations become fixed per million years" (#375157428) | as stated | holds | accurate (relay of mc1c#337074301) | contested (G2) | M-706 |
| "Across the genome as a whole, only 3% of new mutations are deleterious." (L19, MC-10) | as stated | n/a | unverifiable (rule F) | pending | uncited; not checked here |
| "There are 3x more harmful mutations than neutral ones." (L18, Day relayed) | as relayed | n/a | relay accurate; Day's statement unverifiable | as B9 (contradicted, scoped) | rule U; the relay's ellipsis drops Day's scope qualifier |
| "The 410 million base pair difference refers to structural variation" (L21, MC-11) | as stated | holds | accurate (L20 relay) | supported | as claim A3x |
| "population geneticists actually use Kimura’s neutral-theory result to date the human–chimpanzee divergence." (L22, MC-12) | as stated | holds | n/a | contested | as B4d; uncited |
| "But even if the equation were wrong, it would just mean that a few pages in a textbook … would need to be revised." (L6) | the evidence for common descent would stand | holds | n/a | n/a | **reading-dependent**; field value |
| | nothing else would change | non-sequitur | n/a | n/a | against L22 (rule N) |
| "never once challenged natural selection or rate of beneficial mutations" (#339603943) | the equations McCarthy rebutted use neutral-theory quantities | holds | partial | n/a | **reading-dependent**; field value |
| | Day never argued against natural selection | n/a | misread | n/a | #340102853; #339324948 |
| "Yes, when the population doubles … this cancels out." (#375855613) | at equilibrium | holds | n/a | supported | as B7; transient M-208 |
| "Kimura and neutral theory don't even begin to enter into it." (Day, #340102853) | of the MITTENS bound | holds | n/a | n/a | **reading-dependent**; M-713; field value |
| | of Day's case in this exchange | non-sequitur | n/a | n/a | Darwillion and 4Nₑ reply (rule N) |
| "That's only a factor of 227x." (Day, #339543355) | as stated | holds | n/a | n/a | M-915 |

Rule RD: where the verdict depends on the reading, every plausible reading is listed; the value goes with the reading under which the statement is most defensible. Points already scored in item 1 (specific against any, the RF-7 lag, the RF-6 slip, Day's 4Nₑ transit) are not rescored here.

## 8. Day-side steelman

- **The neutral share decides the count, and the critic's figure has no source.** At 3:1 the revised 16–18 million is 4.0–4.5 million, a fifth of the requirement; at 3% it is 15.5–17.5 million. The input moves the result by −74% (M-915). McCarthy answers Day's uncited ratio with an uncited 3% and an uncited coding-only scope. On this exchange alone, neither figure is better supported (rule F), and a count that depends on it is not settled.
- **McCarthy misstates Day, and his quotation hides the correction.** The comment McCarthy quotes at L18 contains Day's denial of serial fixation and his pointer to Chapter 10. The ellipsis removes it, along with Day's qualifier that neutrality "doesn't matter when I'm just pointing out the scale of the improbability". L11 then repeats the serial charge. Scoggins says so twice (#375077052); McCarthy's answer (#375157428) re-quotes the 4Nₑ passage but not the denial.
- **The target is natural selection, and the critic concedes it in one place and denies it in another.** Day's thesis (#339391408) and the MITTENS abstract (#340102853) are about natural selection. A neutral count, however right, does not show that selection produced the adaptive differences (the A/B split, [item 1](2026-11-26-dennis-mccarthy-probability-zero-wrong.md) §4). McCarthy writes both "Vox is literally claiming evolution by natural selection has never occurred" (#339324948) and "never once challenged natural selection" (#339603943).
- **A critic restates the circularity charge.** MC-12 says the 6–9 My dates come from the neutral clock. If so, a neutral count reproducing the requirement over those dates confirms nothing independently. That is Day's B4d point (external `contested`), and it also cuts against L6: if the equation were wrong, the dates would move too.
- **Growth bites where the theory says it does.** k = μ at any N is the equilibrium result. After a size change the delivered rate lags for about 4Nₑ generations (M-208), and whether the human lineage had such a change at the relevant size is open (B1b, B1c). McCarthy answers the equilibrium question and leaves the transient alone.
- **The critic's slips persist after the edit.** L9 keeps the 20-year 400 billion beside L16's 25-year basis, and the 20 million comes back at #375371851. He writes "400 million" for Day's 410, and the speciation figures (sticklebacks, apple-maggot flies, Tragopogon) are uncited.

## 9. Critic-side steelman

- **The serial reading is answered with a number.** Two million fixations per million years, with each taking a million years, puts about two million alleles in transit at once (M-915, M-706). Whatever Day means by "1,000,000 years per neutral fixation", the transit costs only the 4Nₑ lag, which leaves 16 million. Day's denial of serialism (Chapter 10) does not supply a different calculation of throughput.
- **The revised arithmetic is clean, on one basis, and close to the requirement.** It gives 50 a generation and 16–18 million, against the 20 million required, −10% to −20% (M-915). The library's own figure for fixed SNVs per lineage, once polymorphism is removed, is 13.7–15.1 million (M-008). The count is the same order as the requirement, and five orders above MITTENS' 180.
- **The unit point is settled in the critic's favour.** 410 million base pairs mostly reflects structural events, each of which changes many bases. The audit's A3x is internal `holds`, external `supported`, with 21.05 million events per lineage by direct count (R4 GAP-07b). Day's "ten times more conclusive" rests on the unit change.
- **k = μ is the standard result, and Day's alternative was retracted.** The cancellation McCarthy states (#375855613) is claim B7 (external `supported`). Matev shows Day's k = μN/Nₑ gives a fixation probability above one (M-209). Day's "Corrected Calculation Using Actual Values" (8.25) uses that N/Nₑ step and applies today's 8 billion to every mutation since the split (RF-3); his "133x" does not reproduce.
- **Day's 3:1 is uncited too, and McCarthy's scope reading is consistent.** 1.5% × 3/4 = 1.1% ≤ 3% (M-915). A coding dN/dS of about 0.21–0.27, the range the audit used in B9, fits a 3:1 ratio in coding. Even at Day's share the gap is four- to five-fold, not the 1,139,000-fold of MITTENS or 10^−86,000,000.
- **Haldane and the Bernoulli Barrier are about selection.** Neutral substitutions pay no cost of selection (M-801). The "law of large numbers" argument is about the fitness differential among genotypes (M-701), not drift, and the library finds its 14.7 and 1,570 are additive differences printed as ratios.

## 10. Bottom line

As it reads today, the post's arithmetic holds. On one 25-year basis the expected neutral count is 16–18 million against 20 million required, and the thread's two-million-in-transit figure is the clearest answer yet to the serial reading of 4Nₑ. One leftover from the old basis remains (L9: 20 million), a ledger slip. The post was edited on 2026-10-31; MC-09 now points to the comment where it still appears word for word, and this page claims no correction. Day's side gains two points: the neutral share decides the count (4.0–4.5 million at his 3:1), and neither side sources its figure; and McCarthy's serial charge leaves out Day's denial, which sits in the comment he quotes. The critics' side gains the unit point (A3x) and k = μ (B7), both already settled in the audit. What remains open is the same as in item 1: the non-coding neutral share, and whether a neutral count can answer a selection bound (A against B). The exchange adds M-915 to the library and settles nothing new beyond it.
