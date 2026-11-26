# Review: 'Why "Probability Zero" is Wrong About Evolution' (Dennis McCarthy, Substack) and his replies in the comment thread

_Not an audit check; no claim file, verdict or count changed._ <!-- D-41: one neutral review per source; both sides at equal depth (hard rule 1) -->

**Source.** Dennis McCarthy (byline of his Substack *All The Mysteries That Remain*), [dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1](https://dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1), `post_date` 2026-09-11 (API JSON; a free repost of a paid post of 2026-01-26), public, 3,662 words (API `wordcount`). His replies in the post's comment thread run from 2026-09-12 to 2026-09-16; one reply the brief names (RF-6, 2026-09-18) sits in the thread of his next post, "Vox Day Responds", and is read only for that reply and the Day comment it quotes. Fetched 2026-11-26 into gitignored `sources/raw/mccarthy-mc1-2026-11-26/`, `post.json` sha256 `54df56b3d6a7f0b8b12ef1823151f35976ad51d937316df318be479028836ead`, `comments.json` sha256 `e7a91ff112c935c566680858f73851763076cdb4e26a865be445d617f1dd5616`. The post hash differs from the 2026-10-07 bib hash; that copy is not held, so the text could not be diffed, but the post's `updated_at` (2026-09-14) predates the first fetch and every MC-1, MC-1c and RF quote on file is an exact substring of the new text. Bibliography keys MC-1, MC-1c (`docs/research/sources/bib-critics.md`); source map [`mccarthy-mc1.md`](../research/math/sources/mccarthy-mc1.md). Locators: `L<n>` is a line of the post text, `#<id>` a comment id. The post's exponents are flattened in the HTML ("(1/20,000)20,000,000"); I read them as powers, as the thread does. Day's book, which McCarthy quotes at length, is not held by the audit, so the fidelity of those block quotes is unverifiable here; where this page discusses Day's book statements, it takes them as McCarthy quotes them.

---

## 1. The argument

McCarthy answers Vox Day's book *Probability Zero* directly, quoting it in block quotes. He takes its "two principal mathematical arguments" in turn. Against the Darwillion he argues that p^n prices a named list of mutations, while history needs any 20 million out of a far larger pool:

> "What Vox Day calculated—(1/20,000)20,000,000 —are the odds that a particular group or a pre-specified list of 20 million mutations (or 20 million mutations in a row) would all become fixed." (L48)
> "450 billion x 1/20,000 = 22.5 million fixed mutations." (L53)

Against MITTENS he argues that an E. coli fixation rate cannot cap human fixations because E. coli has a far smaller per-genome mutation supply:

> "As clear, the expected rate of fixed mutations has to be determined according to the particular circumstances of the population in question—its genome size, mutation rate, etc." (L63)

In the thread Day objects that the count leaves out the fixation time and assumes neutrality; McCarthy answers with a lag-adjusted count (#337116873, RF-7) and, in the next thread, restates it against MITTENS 3.0's 180 (RF-6). Who is argued against: Day's own book, quoted directly, not a third party's relay of it (rule U; Day's blog reply "Do Try to Keep Up, Dennis" reproduces McCarthy's rendering of the formula, Q71). The audit does not hold the book, so the fidelity of the block quotes cannot be checked here.

## 2. The maths, located and rebuilt

**Model.** The post's count is the textbook neutral expectation: new mutations per year × years × the neutral fixation probability 1/(2N), with every mutation treated as neutral and no transit time. The thread adds a lag: mutations from the last 4Nₑ generations have not had time to fix. Selection, the neutral share and the size history are left out. The MITTENS part has no model of its own; it argues that the LTEE figure does not transfer.

| Step | Equation (author's) | Inputs | Library object | Check |
|---|---|---|---|---|
| Day's supply (quoted) | 100 × 10,000 per generation; "about 50,000 per year" | L35 | M-914 | holds; 50,000/y implies 20 y generations |
| Day's need (quoted) | 2.2 per year; "one in 23,000, or 0.004%" | L36 | M-914 | holds (1 in 22,727; 0.0044%) |
| Darwillion (quoted) | (1/20,000)^20,000,000 = 10^−86,000,000; two lineages 10^−172,000,000 | L39, L42 | M-703, M-914 | holds as rounding (86,020,600; 172,041,200) |
| Specific vs any | "some 20 million out of an enormous pool" | L49 | M-704 | holds: P_any ≈ 1, 2×10⁷ is 527 SD below the mean |
| Neutral count | 50,000 × 9 million = 450 billion; × 1/20,000 = 22.5 million | L51, L53 | M-212 | holds |
| LTEE (quoted) | 40,000/25 = 1,600; 450,000/1,600 = 281.25 | L56, L58 | M-001 | holds |
| Genome ratio | 3.1×10⁹ / 4.6×10⁶ "roughly 690" | L61 | M-007 | 674 (2%; rounding) |
| E. coli supply | "over 99.9%"; "every 1000-2400 divisions" | L61, L75 | M-007, M-914 | 99.959% and 2,439 hold; the 1,000 end has no source in the post |
| Lag (thread) | 9×10⁶/25 = 360,000; −40,000 = 320,000 generations; 50,000 × 8×10⁶ = 400 billion; × 1/20,000 = 20 million | #337116873 | M-201, M-914 | holds as written; mixed basis (below) |
| RF-6 | "400 billion x 1/20000 = 35 million" | #340149310 | M-914 | slip: 20 million |
| Day's transit (thread) | 4 × 10,000 = 40,000 generations; × 25 y = 1,000,000 years | #337074301 | M-203, M-914 | holds |

**Numbers, recomputed** from the authors' inputs only:
- Day's quoted need is 2×10⁷ / 9×10⁶ = 2.22 fixations a year, one in 22,727 mutations. His quoted fixation probability is one in 20,000, which gives 50,000/20,000 = 2.5 a year, 12.5% above the need (M-914).
- The neutral count: 4.5×10¹¹ × 1/20,000 = 22.5 million, 12.5% above the 20 million required (M-212, M-914).
- The lag: the 50,000 a year rests on 20-year generations (L35), the lag on 25-year generations (#337116873). On one basis the count is 16.0 million (25 y, −20%) or 20.5 million (20 y, +2.5%) (M-914).
- RF-6: 4×10¹¹ / 20,000 = 2×10⁷, not 3.5×10⁷. Against F_max = 180 the ratio is 111,111, not 194,444 (M-914).
- Per-genome mutation supply, human over E. coli, at his 60–100 de novo mutations: 146,341–243,902 (M-914; M-007 gives 93,659 at 38.4).

The arithmetic holds apart from one slip (RF-6) and one mixed basis (RF-7). The open questions are about what the count measures, not about the sums.

## 3. What holds

**For McCarthy (critic side).**
- *Specific against any* is correct and is settled maths. P = p^n is the probability that a named list all fixes; history needs at least 20 million of 450 billion, and at his inputs that is about certain (M-704; claim G3: internal `holds`, fidelity `accurate`).
- *The count is Day's own.* Day's passage as McCarthy quotes it computes a need of 1 in 22,727, then a fixation probability of 1 in 20,000. On those inputs the expected count already meets the need, before the p^n step (M-914). McCarthy finishes Day's arithmetic; he does not change the inputs.
- *The thread answer to the time objection is sound in form.* Subtracting the 4Nₑ transit from the window is the leading-order empty-start correction μL(T − 4Nₑ) (M-201), and it leaves 16–20.5 million.
- *The supply point is real.* Per genome, a newborn human carries about 10⁵ times more new mutations than an E. coli division (M-914, M-007; claim A5: internal `holds`, external `contested`).

**For Day.**
- *"you left Kimura's time component out of your response"* (#337074301) is correct of the post: L53 has no time term. McCarthy accepts the point and corrects for it.
- *"1/2Nₑ is the fixation probability for a neutral mutation"* (#337302874, Q105) is correct. The post's count assumes neutrality; its footnote says so ("This probability refers to neutral mutations, which do indeed describe the vast majority of mutations", L74), without a source.
- *Day's LTEE figure is a fixation throughput, not a mutation rate* ("I didn't cite the E. coli study for its mutation rate but for its fixation rate", claim A5g). McCarthy's L61 argues from mutation rate; the step to fixation rate needs the premise that fixation scales with supply (M-713).
- *Charity.* McCarthy's L10 ("The book deserves to be addressed on its own terms") sets a standard both sides later break in the thread (§6).

## 4. What fails

### Errors (rule R1: correcting it moves the stated conclusion by >25% or flips it)
None found at the error level under the most defensible readings. RF-6 is reading-dependent (§5, §7). The RF-7 mixed basis moves the lag-adjusted count by −20% or +2.5% (M-914), under the 25% line.

### Non-sequiturs and hidden premises (rules N, U)
- **Premises 1–3 to "evolution is certain" (L18) and "there is no brake" (L29).** These establish allele-frequency change. Day's argument is a rate: enough fixations in the time. *Implicit:* no qualitative wall implies no rate limit. The opening sections do not touch the quantitative claim; L48–L64 do.
- **Mutation rate to fixation rate (L61–L64).** *Implicit:* the per-generation fixation rate is set by mutation supply. That holds for neutral fixation (k = μ) and for adaptive sweeps when supply limits them; Day's G_f counts LTEE fixations of all causes, which the LTEE papers describe as mostly beneficial in the non-mutator lines (M-504, blocked on full texts; M-713). The premise is the transfer question (claim A5, `contested`), not a refutation of it.
- **"basically what you'd predict" (L54).** *Implicit:* almost every new mutation is neutral, and transit time can be ignored. The second premise is repaired in the thread; the first is asserted (L74).
- **"not 180" (RF-6).** Compares a neutral count with MITTENS' selection ceiling. Day's framing is in the comment RF-6 replies to: "I have directly challenged natural selection" (#340102853). On Day's framing, 20 million neutral fixations do not answer a ceiling on selected ones; on the critics' framing, the 180 is a total that must include them. This is the A/B branch split of the audit, not settled here.
- **Day: "1,000,000 years per neutral fixation" (#337074301).** As a transit time per allele it holds (M-203). As a throughput (one fixation per million years) it is the serial reading (M-706), which Day disowns in the next reply: parallel drift is a defence "so obvious that I devoted Chapter 10 to it" (#337302874). Under the parallel reading the time costs only the lag McCarthy computes.
- **Day: "My improbability equation is irrelevant, as it even says in the book" (Q90) against McCarthy: "nowhere does it say this equation is irrelevant" (#338774739).** The book is not held, and McCarthy allows that it may have been amended. Both are fidelity claims the audit cannot check (M-705, blocked on the book).

## 5. Slips (rules R1, SC; ledger level)

- **RF-6 (#340149310):** "400 billion x 1/20000 = 35 million point mutations fixing alone. That's 35 million right there, not 180." The product is 20 million; four days earlier he wrote the same product as 20 million (#337116873). 35 million is the SNV count he cites elsewhere (#337048907). **R1 check** (M-914): the stated conclusion is the comparison "not 180". Corrected, the ratio to 180 falls from 194,444 to 111,111 and the inequality holds by five orders of magnitude: no flip, so **ledger**. Read instead as a headline total, "35 million right there" moves by −42.9% under correction, which R1(i) would score as an error. The comparison reading is the more defensible one (§7). Not SC: the correction is in another thread.
- **RF-7 (#337116873):** "neutral mutations that have occurred in the last 40,000 years have not had time to fix yet": the lag is 40,000 *generations* (1 million years at his 25 years). And the 50,000 a year rests on 20-year generations while the lag uses 25. One basis gives 16.0 or 20.5 million against his "exact correct result" of 20 million: −20% / +2.5%, **ledger** (M-914).
- **L61:** "roughly 690 times" for 674 (2%, rounding; not ledgered). "every 1000-2400 divisions": 2,439 follows from his footnote (L75); the 1,000 end is unsourced.
- **L3:** "Population Zero" for *Probability Zero*.
- Day's quoted figures ("one in 23,000", 10^−86,000,000, 10^−172,000,000) are rounding.

## 6. Rhetoric (rule RH)

| Quote (locator) | Device | Audience | Function | Dialectical core | Better answer (aimed at the move, never at the person) |
|---|---|---|---|---|---|
| "it directly refutes the core claims of Vox Day’s best-selling book Probability Zero" (L2) | decisiveness claim | general readers | sets the stakes | L48–L64 | Specific vs any (M-704) settles the Darwillion; the LTEE transfer stays contested (A5). Claim only what is settled. |
| "The book is first and foremost what I like to call an end-around." (L30) | label | readers | frames PZ as dodging the evidence | none: PZ's maths stands or falls on its own | Answer the maths (as L48–L64 then do); the other evidence is a separate argument. |
| "so have these aliens been hovering over every region on Earth in their biolabs for the last 3.5 billion years" (#335611009) | ridicule by reductio | thread readers | burden shift onto Day's alternative | Day's alternative must cover all lineages, not only great apes | State the scope question once: which lineages does the hypothesis cover, and what would it predict? |
| "Darwin was innumerate, by his own admission. Dawkins is observably innumerate." (#336073436) | ad hominem (competence) | Day's readers | discredit the field | none; the empirical core is the claim about economists and physicists | Name the computation biologists get wrong; McCarthy's Pew figures (#336202654) answer the head-count claim, but neither settles the maths. |
| "Genetic drift is now deader than dead." (#335155894, Q88) | finality | thread readers | close the neutral route | the census ceiling X = (Vₖ + 2)·G/16 (M-205) | Point to the ceiling's derivation and its test (B2), not to the verdict. |
| "But I understand the relevant math on a level that very few, if any, biologists do." (#335823489) | self-authority | thread readers | ethos | none | Let the numbers carry it: show the step McCarthy's count gets wrong. |
| "What is 410 million divided by 6 million?" / "Can you do that math?" (#337035111) | Socratic test, condescension | thread readers | moves the target from 20 million fixations to 410 million base pairs | base pairs against mutation events (M-011) | Say which unit the requirement counts and why (claim A3x); the division (68.3) answers nothing until then. |
| "Yes, there has been sufficient time, as I keep showing." (#338863905) | reassertion | thread readers | holds ground | #337116873 | Cite the lag calculation and its basis (16–20.5 million). |

The same standard applies to both sides. Rhetoric changes no verdict.

## 7. Verdicts under the audit's rule (informal; not entered in any claim file)

| Statement (locator) | Reading | Internal | Fidelity | External | Note |
|---|---|---|---|---|---|
| "only that some 20 million out of an enormous pool of candidate mutations become fixed" (L49) | as stated | holds | accurate (book secondhand) | contested | as claim G3 |
| "450 billion x 1/20,000 = 22.5 million fixed mutations" … "basically what you'd predict" (L53–L54) | neutral count on Day's quoted inputs | holds | accurate | contested | as claim B5a; neutral share and time are the disputes |
| "the expected rate of fixed mutations has to be determined according to the particular circumstances" (L63) | fixation scales with supply (implicit premise) | holds | accurate (L57 states Day's fixation-rate claim) | contested | as claim A5 |
| | "E. coli does not exhibit the highest mutation rate per generation" (L61) read as a rebuttal of a mutation-rate claim | non-sequitur | misread | n/a | Day claimed a fixation rate; less defensible reading |
| "400 billion x 1/20,000 =20 million fixations … the exact correct result" (#337116873) | as written | holds | n/a | contested (B1b `pending`) | mixed basis, ledger |
| "That's 35 million right there, not 180." (#340149310) | comparison with 180 | holds | n/a | contested (A/B split) | **reading-dependent**; field value under this reading; slip ledgered |
| | headline total | arithmetic-error (−42.9%) | n/a | n/a | less defensible reading |
| "that's 1,000,000 years per neutral fixation" (Day, #337074301) | transit time per allele | holds | n/a | supported (M-203) | reading-dependent |
| | throughput, one at a time | non-sequitur | n/a | n/a | M-706; Day disowns this reading (#337302874) |
| "My improbability equation is irrelevant, as it even says in the book." (Day, Q90) | as stated | n/a | unverifiable | n/a | book not held (M-705) |

Rule RD: where the verdict depends on the reading, every plausible reading is listed; the value goes with the reading under which the statement is most defensible. Day's "3x more harmful" reductio in the same thread is claim B9 and is not rescored here.

## 8. Day-side steelman

- **The count measures neutral drift, which MITTENS does not claim to limit.** Day's core argument is about natural selection (#340102853: "I have directly challenged natural selection"); MITTENS' 180 is a selection ceiling. A neutral count of 20 million, however right, does not show selection did the work; it moves the dispute to branch B (drift), where Day has separate arguments: the fill state (B1, B1c open), the census ceiling (M-205, Q93) and the load reductio (B9). RF-6's "not 180" compares across that line.
- **The neutral share is an input, and McCarthy asserts his.** 1/(2N) applies to neutral mutations only. If three of four new mutations are harmful, as Day asserts (Q105), the expectation is 5.6 million, or 5.0 million after the lag: about a quarter of the requirement (M-914). McCarthy's "vast majority" (L74) is no better sourced in this exchange than Day's 3:1.
- **The time objection bites more than the reply admits.** On one consistent basis the lag-adjusted count is 16 million at Day's 25-year generations, 20% short of the requirement he calls "the exact correct result". The empty-start correction is the leading term only; Day's fill-state objection says the pipeline could not fill at all above his ceiling, and McCarthy does not engage it in this thread.
- **The LTEE objection argues against a mutation rate Day did not claim.** Day cited a fixation throughput (A5g). The LTEE's fixations are described as mostly beneficial (M-504), so the 690-fold genome ratio scales neutral supply directly and sweep throughput only where supply limits it (M-713, M-103).
- **The Darwillion's role is unsettled.** Day says the book calls the improbability equation irrelevant to the proof; if so, McCarthy's main target is a scale illustration. The audit does not hold the book (M-705), so McCarthy's contrary quote is no stronger than Day's claim.
- **Slips are on the critic side too.** 35 million for 20 million (RF-6), years for generations and a mixed generation length (RF-7), an unsourced 1,000 (L61).

## 9. Critic-side steelman

- **The Darwillion answers the wrong question, and that is settled.** p^n is the chance of a named list; history needs any 20 million of 450 billion, which is about certain at Day's inputs (M-704; G3 internal `holds`, fidelity `accurate`). Whatever the book now says, the "Verdict" McCarthy quotes ties "one in one Darwillion" to "mathematically impossible" (L46–L47); Day's thread reply says the equation is irrelevant, not that the quote is wrong (Q90).
- **Day's own inputs give the count.** His quoted need, 1 in 22,727, is easier than his quoted fixation probability, 1 in 20,000: on his inputs about 2.5 neutral fixations arise a year against 2.22 needed (M-914). McCarthy does not change Day's numbers; he declines the p^n step.
- **The time objection was answered with Day's own correction.** μL(T − 4Nₑ) is the same leading-order correction the audit derives for Day's empty-start case (M-201). It leaves 16–20.5 million, the same order as the requirement and five orders of magnitude above 180. Read as a throughput, "1,000,000 years per neutral fixation" is the serial reading Day himself rejects (M-706).
- **The neutral-share counter is uncited, and its claim was checked.** Day's 3:1 is uncited in the thread (Q105). In claim B9 the audit scored the reductio built on it: fidelity `unverifiable`, external `contradicted`, scoped to its premises as worded (premise 2 against dN/dS of about 0.21–0.27). A quarter-share would leave a 4-fold gap after the lag (5.0 against 20 million), not a factor of 10^86,000,000.
- **The supply point stands as a transfer argument.** A 10⁵-fold per-genome supply gap (M-914, M-007) is a reason to doubt that a clonal bacterium's fixation rate bounds humans; the library's verdict is that the supply scaling favours the critic on transfer (M-713), and A5 internal `holds`.
- **The slips do not move the conclusions.** RF-6's correction leaves "not 180" by five orders of magnitude; RF-7's basis leaves 16–20.5 million. McCarthy opens by granting Day intelligence and good faith (L10) and engages the maths.

## 10. Bottom line

McCarthy's arithmetic holds apart from one ledger slip (RF-6: 35 million for 20 million) and one mixed generation basis (RF-7: 16–20.5 million rather than exactly 20). His strongest point is settled: the Darwillion prices a named list, and on Day's own quoted inputs the expected neutral count meets the requirement. Day's thread replies add two valid corrections, the transit time and the neutral share; the first leaves the count at 16–20.5 million against 20 million required, and the second is an input neither side sources here. Both remaining questions are already open in the audit: whether a neutral count can answer a selection ceiling (branches A against B) and whether the LTEE rate transfers to humans (A5). The exchange adds the lag calculation and its basis to the library (M-914) and settles nothing new beyond it.
