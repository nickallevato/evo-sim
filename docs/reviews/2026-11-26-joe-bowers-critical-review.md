# Review: "A Critical Review of Probability Zero" (Joe Bowers, via Day's repost) and Day's point-by-point reply

_Not an audit check; no claim file, verdict or count changed._ <!-- D-41: one neutral review per source; both sides at equal depth (hard rule 1) -->

**Source.** Joe Bowers (the name as Day gives it; nothing else is known of him), seven numbered points and a summary, known only through Day's repost with his reply on Vox Popoli: [voxday.net/2026/03/04/a-critical-review-of-probability-zero/](https://voxday.net/2026/03/04/a-critical-review-of-probability-zero/), published 2026-03-04T17:40Z (page metadata; modified three seconds later, no later edit), public, about 1,420 words (Bowers about 770, Day about 650). Fetched read-only 2026-11-26 into gitignored `sources/raw/jb-1-2026-11-26/`, `vd-bowers-repost.html` sha256 `b721c9b8035220c065016c548e632c74aa248b3a45db96fe9e48749031289563`. The hash differs from the bibliography's earlier copy (`f7bb3f68…`, site chrome). All four quotes on file (BO-01 to BO-04) are exact substrings of the fetched text, at the paragraphs the quotes file gives. Bibliography key JB-1 (`docs/research/sources/bib-critics.md`); source map [`bowers-jb1.md`](../research/math/sources/bowers-jb1.md). No new maths object: Bowers states no numbers, and every number in Day's reply is already asserted in a record (M-001, M-801, M-802). Comments are off-site ("DISCUSS ON SG") and were not fetched; Day's reply does not continue there.

**The original.** One search pass on 2026-11-26 (three queries: the title Day reports, the name with "point-by-point rebuttal", and BO-02 verbatim) found no copy of Bowers's review outside the repost, as the bibliography's earlier search had found. So this page cannot say whether the repost is complete or verbatim.

**Rule U, inverted.** Bowers's words reach us only through Day. Each Bowers line is scored as reposted and marked secondhand, and Day's repost is not scored as a misquote. Day's replies are his own words and are scored as firsthand. Locators: `jb1@pN` is paragraph N of the post. p1 is Day's introduction, p2-p8 are Bowers's points 1-7, p9 is Bowers's summary, p10-p16 are Day's replies to points 1-7, p17 is his reply to the summary, and p18-p19 are his close.

---

## 1. The argument

Bowers says *Probability Zero* models evolution wrongly, in seven ways. It prices pre-targeted mutations fixed in sequence (1), it uses fixation probability 1/N instead of 2s (2), it multiplies independent probabilities in a strict order (3), it uses low Nₑ (4), it equates a tiny number with impossibility on an incomplete model (5), it says no new information can arise (6), and it needs many coordinated mutations for complex traits (7). His summary:

> "In short, Probability Zero reaches its conclusion by modeling evolution as a blind, single-threaded, neutral lottery with fixed targets and no recombination." (jb1@p9, secondhand)

Day answers each point. He says MITTENS counts observed fixed differences and asks whether the mechanism can produce that many in the time, so pathways and targets don't enter. He says the framework assumes selection, not drift, and that Bowers "has confused fixation probability with fixation rate" (jb1@p11, BO-03). He says recombination does not speed any single allele, that his Nₑ is the field's standard figure, that the listed mechanisms are handled in the book, that he never argued against new information, and that regulatory changes are substitutions too. He closes:

> "Not a single calculation. Not a single specific engagement with any of my actual numbers." (jb1@p18, BO-04)

Bowers writes against the book. He quotes no page of it, and the review names no equation, number or chapter. Day writes against Bowers's text as he reposted it.

## 2. The maths, located and rebuilt

There is little maths on either side. Bowers gives two symbols (2s, 1/N) and no calculation. Day's reply cites four numbers from his own work (300 generations, Nₑ ≈ 10,000, 220,000×, "five-order-of-magnitude") and computes nothing. The table locates each formula either side relies on and the library object that already holds it.

| Step | Equation (author's, or the one the claim needs) | Inputs | Library object | Check |
|---|---|---|---|---|
| Fixation probability (Bowers 2) | u ≈ 2s, "not 1/N" | weak selection, diploid | M-113 (record), M-605 | holds (F4: holds / accurate / supported); the neutral value is 1/(2N), so "1/N" is a factor-2 gloss |
| Adaptive rate (Bowers 2, implied) | k_ben = 2N U_b × u; with u = 2s, k_ben = 4N s U_b; with u = 1/(2N), k = U_b | none stated | M-605 | holds as algebra: the ratio is 4Ns, so a neutral u lowers the adaptive rate |
| Product of probabilities (Bowers 2, 3) | P = pⁿ | Day's: p = 0.02, n = 2e7 (Ga); McCarthy's rendering of the Darwillion: p = 1/20,000 (G4) | M-703 (record) | Ga uses 2s at s = 0.01; the Darwillion as rendered uses 1/(2N). pⁿ has no time or order variable (M-706) |
| MITTENS 2025 ceiling (Day p11, p14, p18) | F_max = t_div d / (g G_f); shortfall = 20M / F_max | 146,250 effective generations, G_f = 1,600 | M-001 (record) | F_max = 91 (91.4); 20M/91 = 219,780× ("220,000×"; 2.2 × 10⁵, "five orders"): holds |
| Haldane ceiling (Day p11) | 30N deaths per substitution / 0.1N per generation = 300 generations | 146,250 effective generations | M-801, M-802 (records) | 146,250/300 = 487; 20M/487 = 41,068× (4.1 × 10⁴): holds, but it is a different ceiling from the one above |
| Recombination (Bowers 3, Day p12) | none on either side | R4 F2-A: interference ratio R_int at 2N U_b = 32 | M-604, A5f | Day's per-allele statement holds at one locus; across linked sweeps R_int is 0.088 clonal against 0.975 free (A5f external supported) |
| Nₑ (Bowers 4, Day p13) | none; MITTENS F_max has no Nₑ term | Nₑ ≈ 10,000 | M-001, M-114, M-209 | Nₑ does not enter the MITTENS ceiling, and under neutrality it cancels from k |

**Numbers, recomputed** from the authors' inputs only (each one asserted in the record named):
- 146,250 / 1,600 = 91.4, printed 91 (M-001).
- 20,000,000 / 91 = 219,780, Day's "220,000×" (M-001).
- 146,250 / 300 = 487.5, printed 487; 20,000,000 / 487 = 41,068 (M-802).

The arithmetic Day cites holds. The two ceilings he names in one reply are both his, but they come from different papers and rest on different constants (1,600 against 300 generations per fixation), so they give different shortfalls (219,780 against 41,068). §4 and §5 take up which one the reply means.

## 3. What holds

**For Bowers (secondhand):**
- **2s, not 1/N (BO-01).** It is the textbook value for a new beneficial mutation under weak selection in diploids (M-113; claim F4: holds / accurate / supported).
- **Probability feeds rate.** His point 2 does not confuse the two quantities. It says a neutral fixation probability "artificially suppresses the rate of adaptive change and inflates improbability" (jb1@p3). That is the standard link k = flux × u (M-605).
- **Partial targets for the summary.** Each of the summary's four descriptors has a target in Day's held text (jb1@p9). "Fixed targets" fits the Darwillion (G3, G4). "Single-threaded" fits the Appendix A serial chain (M-706; G2f holds there). "Neutral lottery" fits the Darwillion's 1/20,000 = 1/(2N) (M-703). "No recombination" fits the G_f input, which is a clonal LTEE rate (M-103; A5f fidelity partial, external supported).
- **The recombination point has a computed basis.** It is not Bowers's computation but the audit's. R4 F2-A finds that free recombination keeps parallel sweeps near full speed (R_int 0.975) where clonal linkage cuts them to 0.088 (A5f). That is the effect his point 3 names.
- **The model-dependence point is sound as logic.** "If the model omits … then the resulting “zero” reflects model incompleteness" (jb1@p6) is a valid conditional. The library's catalogue of Day's named mechanisms finds 5 of 18 asserted but not computed (M-901, ROOT-M).

**For Day (firsthand):**
- **Point 1 misses MITTENS.** "MITTENS counts fixed differences between species—observed genomic divergence documented in the literature." (jb1@p10). Specific-vs-any lands on the Darwillion and the Appendix A product, not on a count of any 20M fixations (G3, M-704; [McCarthy item-1 review](2026-11-26-dennis-mccarthy-probability-zero-wrong.md)).
- **Day used 2s.** His own MITTENS 2025 product uses p = 0.02, which is 2s at s = 0.01 (Ga, Z18165980 ¶24), so "He often reduces fixation probability to approximately 1/N" (jb1@p3) is at best partial.
- **2s and the capacity ceiling.** "The 2s approximation the reviewer invokes for fixation probability is irrelevant to the throughput constraint" (jb1@p11) is true of the empirical G_f, in which no u enters (M-001). It is also true of Haldane's budget, which counts deaths per substitution, not s (M-801).
- **Nₑ.** "For humans, Ne ≈ 10,000 is the standard figure used by the field itself" (jb1@p13) is right about the literature (M-114). Nₑ does not appear in F_max at all, so Bowers's point 4 has no target in the MITTENS ceiling.
- **Regulatory changes.** "regulatory changes are themselves substitutions" (jb1@p16) is right as accounting: an observed divergence count already includes regulatory sites.
- **The review has no maths.** "Not a single calculation." (BO-04) and "The reviewer never mentions the 220,000× shortfall, never addresses Haldane’s cost, never engages with the Bio-Cycle model or the d coefficient, never mentions the ancient DNA validation data." (jb1@p18) are both accurate as to the reposted text. "Haldane", "220", "Bio-Cycle", "d coefficient" and "ancient" occur 0 times in p2-p9, and the only maths is the symbols 2s and 1/N.

## 4. What fails

### Errors (rule R1: correcting it moves the stated conclusion by >25% or flips it)

None found on either side. Bowers states no number for a correction to move. Day's numbers reproduce (§2). The one place where two of Day's numbers disagree (the 300-generation ceiling against the 220,000×) is scored in §5 under rule C.

### Non-sequiturs and hidden premises (rules N, U)

**Day, "probability vs rate" (BO-03; F4a).** On the reposted text, Bowers's point 2 is about the value of u and its effect on the adaptive rate and on the product. He does not treat a probability as a rate. So the charge "The reviewer has confused fixation probability with fixation rate" (jb1@p11) does not describe what the repost shows. F4a's own implicit premise, that Bowers's point "concerns probability only", is false on this text. What the reply does answer is narrower: under an empirical G_f or Haldane's death budget, u does not set the ceiling. That answer is sound (§3) but leaves two things open. (a) Under a selection model of adaptive substitution, k_ben = 4N s U_b, so 2s raises the adaptive rate 4Ns-fold over a neutral u (M-605). (b) In the Darwillion's product, p = 1/(2N) is the quantity Bowers names. Under the most defensible reading the reply holds as a statement about the ceiling, and it is a partial misdescription of Bowers (§7).

**Day, "The entire MITTENS framework uses Haldane’s cost of natural selection, which assumes selection is operating." (jb1@p11).** There are two hidden premises. (1) That MITTENS's ceiling is Haldane's. It is not: the 2025 MITTENS ceiling is 146,250 / 1,600 = 91, from the LTEE G_f (M-001), and the reply's own "220,000×" is computed on it. Haldane's 300 generations is the separate Haldane paper's ceiling (487, M-802). (2) Implicit: that the 20M required fixations are all selected. Haldane's cost bounds only selected substitutions (M-801). The 20M is a count of all fixed differences, most of which critics model as neutral (k = μ, M-209, M-914). So the reply answers "you modelled selection as drift" by appealing to a bound that does not cover drift. Bowers's point 2 does not raise neutral fixations, and the reply does not need to answer them. But "assumes selection is operating" does not, by itself, show the 20M can only come from selection. That step is assumed.

**Day, recombination (jb1@p12).** "it does not accelerate the rate at which any individual allele increases in frequency" holds for one allele at one locus. Bowers's point is about throughput: beneficial mutations "arising in different individuals to combine" (jb1@p4). For throughput, interference between linked sweeps is the question, and R4 F2-A finds recombination matters there (A5f external supported; M-604 still open at human scale). Implicit: no interference. The cited authority is also misattributed: "Kimura and Ohta (1969) established that expected time to fixation does not depend on recombination rate." The paper is a single-locus model in which "recombin" occurs 0 times (H9, fidelity misread; `ledgers/fidelity.md`). This reply repeats that citation, and it is not a new finding.

**Bowers, point 1 (jb1@p2).** "The flaw is that he treats evolution as requiring a long chain of specific, pre-targeted mutations that must all occur and fix sequentially." Implicit: the target is the MITTENS count. Against the count it is a non-sequitur (G3). Against the Darwillion and the Appendix A chain it lands. The review does not say which, so it is reading-dependent (§7).

**Bowers, point 4 (jb1@p5).** "He frequently uses conservative or arbitrarily low effective population sizes to restrict mutational supply." Implicit: Nₑ enters Day's ceiling. It does not enter F_max (M-001), and the review names no value it calls arbitrary.

**Bowers, summary to conclusion (jb1@p9).** "When realistic population genetics, parallel mutation, selection coefficients, and genomic mechanisms are included, the “zero” vanishes". This is asserted with no computation. The quantified answers in the library come from other critics and from the audit (M-914, M-604, R4 F2-A), not from this review.

**Unverifiable on both sides.** Bowers's points 6 and 7 attribute positions to the book ("Day argues that new biological information cannot arise via mutation and selection.", jb1@p7; "He assumes that complex traits require many simultaneous coordinated mutations.", jb1@p8). Day denies them ("I never made any such argument. Nothing like this ever appears in the book.", jb1@p15) and says the mechanisms "addressed in the book" (jb1@p14). The book is paywalled and not held. The library holds no Day text claiming that information cannot arise. The coordinated-mutation model it does hold is Hössjer, Bechly and Gauger's (D15), not Day's. Neither side's account of the book can be scored.

## 5. Slips (rules R1, SC; ledger level)

- **Bowers, "1/N".** The neutral fixation probability in a diploid population is 1/(2N), and the Darwillion as rendered uses 1/20,000 = 1/(2N) at N = 10,000. Check: Bowers states no number, so no number moves, and the point (2s against the neutral value) is the same at 1/N or 1/(2N). Ledger.
- **Bowers, "probability zero in mathematics means literal impossibility under the model" (jb1@p6).** True on a finite or countable sample space. On a continuous one, events of probability 0 can occur ("almost never"). Check: the point that "zero" depends on the model does not depend on the gloss. Ledger.
- **Day, which ceiling (jb1@p11 against jb1@p14, jb1@p18).** The reply says "The fixation rate limit of one substitution per 300 generations" is what MITTENS uses. It then cites "the 220,000× shortfall" and a "five-order-of-magnitude shortfall", which are computed on G_f = 1,600 (20M/91 = 219,780, M-001). On the 300-generation limit with the same 146,250 generations, the shortfall is 20M/487 = 41,068 (M-802): four orders, not five, and a move from 219,780 to 41,068, far beyond 25%. R1 check under rule C (most charitable reading): the reply's numbers are MITTENS's, and the 300 sentence misnames the constant behind them. Correcting the sentence moves no number in the source, and the conclusion ("the rate at which fixation can occur is insufficient", jb1@p15) holds on either ceiling (41,068 and 219,780 both far exceed 1). Ledger, as a description slip. Under the other reading, where 300 is the operative limit, the 220,000× would be an R1 error (219,780 to 41,068). That reading is less defensible, because no source derives 220,000 from 300.
- **Day, "Kimura’s algebraic error" (jb1@p13).** Day's N/Nₑ reading of k = μ (M-209). The library records the cancellation as holding, and Day conceded it on 2026-08-27, in a later source, so rule SC does not apply here. Check: the remark is an aside in the microbes paragraph, and the reply's point that the Nₑ figure is standard does not depend on it. Ledger.
- **Day, Nₑ.** On 2026-02-08 (Z18525547; B3h) Day argued that the standard Nₑ = 10,000 presupposes k = μ (M-211). In this reply he relies on it as "the standard figure used by the field itself". This is a tension between sources, not within one, and the reply needs the figure only as a literature value. Noted, not scored.

## 6. Rhetoric (rule RH)

| Quote (locator) | Device | Audience | Function | Dialectical core | Better answer (aimed at the move, never at the person) |
|---|---|---|---|---|---|
| "Ignorant and Unscientific Drivel" (Bowers's title as Day reports it, jb1@p1, secondhand) | epithet in a title | Bowers's readers | dismiss the book before the points | the seven points | "Name the equation and the page; a title is not a counter-calculation." |
| Day's retitling to "A Critical Review of PROBABILITY ZERO", with the insult reported in his first line (jb1@p1) | reframing: neutral heading, the opponent's epithet put up front | Day's readers | make the reviewer look hostile before his points are read | none | "Repost under the author's title and let the points stand or fall on the maths." |
| "That is not how evolution works." (jb1@p9, secondhand) | flat assertion | general readers | close the summary with authority | the four descriptors (§3) | "Say which Day equation has each property: the count does not; the Darwillion does." |
| "the “zero” vanishes" (jb1@p9, secondhand) | metaphor of disappearance | general readers | promise a result not computed | the model-dependence conditional | "Show the number it vanishes to: the neutral count (M-914) or interference (R4 F2-A) are where that is computed." |
| "This is a false and groundless assertion." (jb1@p12) | double negative label | Day's readers | dismiss point 3 | point 3 gives no maths (true) | "Recombination's effect on throughput is computed (R4 F2-A); answer that, not the missing equation." |
| "Where is the math showing that gene duplication closes a five-order-of-magnitude shortfall?" (jb1@p14) | rhetorical question, burden shift | Day's readers | turn missing maths into a concession | Bowers gives no computation (true) | "The burden runs both ways: 5 of the 18 named mechanisms are dismissed without computation (M-901)." |
| "The summary paragraph is the evidence that the reviewer hasn’t even read the book." (jb1@p17) | inference to bad faith | Day's readers | discredit the whole review | the summary does not describe the count (true) | "Point to the count, which none of the four descriptors fits, and grant the Darwillion, which they do." |
| "It is a straw man constructed from standard anti-creationist talking points" (jb1@p17) | genre label | Day's readers | file the review as generic | the review quotes no page (true) | "Generic objections can still be right; the recombination one was computed (A5f)." |
| "Not a single calculation. Not a single specific engagement with any of my actual numbers." (jb1@p18, BO-04) | anaphora | Day's readers | sum up the review as empty | accurate as to the repost (§3) | (accurate; no counter needed) "Then the next step is to supply the calculation for him and see what it shows." |
| "Seven points, zero math, zero engagement with the actual argument." (jb1@p18) | tricolon with numbers | Day's readers | memorable close | as above | as above |
| "It’s just a midwit attacking a figment of his own imagination." (jb1@p19) | epithet | Day's readers | close on the person | none beyond p18 | "Leave the person; the point that stands is that the count, unlike the Darwillion, has no target to pre-specify." |

Rhetoric changes no verdict. Both sides use it at the frame: Bowers in his title and summary, Day in his first and last lines. Both have a dialectical core beside the rhetoric. Bowers's core is that several of Day's own calculations price fixed targets in series. Day's core is that the count does not, and the review shows no number.

## 7. Verdicts under the audit's rule (informal; not entered in any claim file)

| Statement (locator) | Reading | Internal | Fidelity | External | Note |
|---|---|---|---|---|---|
| "The flaw is that he treats evolution as requiring a long chain of specific, pre-targeted mutations that must all occur and fix sequentially." (jb1@p2, secondhand) | of the Darwillion and Appendix A chain | holds | partial | contested | **reading-dependent**; field value; as G3, G2f |
| | of the MITTENS count | non-sequitur | misread | n/a | the count needs any 20M (M-704) |
| "He often reduces fixation probability to approximately 1/N (or similar simplified forms) and then multiplies improbabilities across many required mutations." (jb1@p3, secondhand) | as stated | holds | partial | n/a | Darwillion 1/(2N); Ga uses 2s |
| "The correct approximation for a beneficial mutation is roughly 2s (in diploids under weak selection), not 1/N." (jb1@p3, BO-01) | as stated | holds | accurate | supported | as F4 |
| "By modeling them as near-neutral events, he artificially suppresses the rate of adaptive change and inflates improbability." (jb1@p3, secondhand) | as a statement about the adaptive rate and pⁿ | holds | partial | supported | 4Ns (M-605); applies where Day uses 1/(2N) |
| "Treating it like a serial lottery is a category error." (jb1@p4, BO-02) | as stated | holds | n/a | contested | as G2f (Appendix A chain only) |
| "He frequently uses conservative or arbitrarily low effective population sizes to restrict mutational supply." (jb1@p5, secondhand) | as stated | non-sequitur | unverifiable (no value named) | n/a | Nₑ is not in F_max |
| "But probability zero in mathematics means literal impossibility under the model — not merely “very small.”" (jb1@p6, secondhand) | as stated | holds (finite spaces) | n/a | contested | slip at ledger level (§5) |
| "Day argues that new biological information cannot arise via mutation and selection." (jb1@p7, secondhand) | as stated | n/a | unverifiable | n/a | book not held |
| "In short, Probability Zero reaches its conclusion by modeling evolution as a blind, single-threaded, neutral lottery with fixed targets and no recombination." (jb1@p9, secondhand) | of Day's held corpus around the book | holds | partial | contested | **reading-dependent**; field value; each descriptor has a target (§3) |
| | of the MITTENS count | non-sequitur | misread | n/a | none fits T/G_f |
| "The reviewer is attacking a model I don’t use." (jb1@p10) | of the MITTENS count | holds | accurate (of point 1) | n/a | **reading-dependent**; field value |
| | of the book as a whole | non-sequitur | partial | n/a | Darwillion, Ga (G4, Ga) |
| "The entire MITTENS framework uses Haldane’s cost of natural selection, which assumes selection is operating." (jb1@p11) | MITTENS = the book's whole case, incl. the Haldane paper | holds | partial | contested | **reading-dependent**; field value; implicit premise: the 20M are selected (§4) |
| | MITTENS = the F_max formula | non-sequitur | misread | n/a | the ceiling is G_f = 1,600, not 300 (M-001, M-802) |
| "The reviewer has confused fixation probability with fixation rate. These are two different things." (jb1@p11, BO-03) | u does not set the G_f or Haldane ceiling | holds | partial | supported | **reading-dependent**; field value; Bowers's paraphrase accurate, "confused" not shown |
| | Bowers treated a probability as a rate | non-sequitur | misread | n/a | jb1@p3 links them through the rate |
| "Recombination reshuffles existing variation; it does not accelerate the rate at which any individual allele increases in frequency." (jb1@p12) | one allele, one locus | holds | n/a | supported | **reading-dependent**; field value |
| | as an answer to throughput (point 3) | non-sequitur | n/a | contradicted (direction) | R4 F2-A: R_int 0.088 clonal against 0.975 free (A5f) |
| "Kimura and Ohta (1969) established that expected time to fixation does not depend on recombination rate." (jb1@p12) | as stated | n/a | misread | pending | as H9 |
| "For humans, Ne ≈ 10,000 is the standard figure used by the field itself—it’s not my invention." (jb1@p13) | as stated | holds | accurate | supported | M-114 |
| "Each of these is addressed in the book, several of them in complete chapters dedicated to them." (jb1@p14) | as stated | n/a | unverifiable | n/a | book not held; 5 of 18 asserted in held papers (M-901) |
| "Calling them “regulatory” rather than “structural” does not exempt them from the fixation throughput constraint." (jb1@p16) | as accounting | holds | n/a | supported | an observed count includes them |
| "This bears no resemblance to anything in the book." (jb1@p17) | of the MITTENS count | holds | accurate | n/a | **reading-dependent**; field value |
| | of Day's held corpus | non-sequitur | misread | n/a | §3, four targets |
| "Not a single calculation. Not a single specific engagement with any of my actual numbers." (jb1@p18, BO-04) | as stated, of the repost | holds | accurate | n/a | as the quotes-file note |

Rule RD: where the verdict depends on the reading, every plausible reading is listed, and the field value takes the reading under which the statement is most defensible. Seven of the rows above are reading-dependent: two Bowers, five Day.

**Candidates for claim files** (not applied; for the lead): F4a's implicit premise ("Bowers's point concerns probability only") and its note ("depends on the unretrieved original") can now be stated from the reposted text, which shows point 2 linking u to the adaptive rate. F4a's internal `holds` survives only under reading (a) above. G2f's formal statement could quote point 3's full text (jb1@p4), which gives the recombination ground for "serial lottery".

## 8. Day-side steelman

Bowers's review never touches the calculation the book is built on. MITTENS asks whether the observed count of fixed differences can be produced in the time available, and a count of any 20M fixations has no targets to pre-specify, no path to narrow and no order to impose (G3, M-704, M-115). The review names no equation, page or number, so its seven points cannot be placed on any of Day's formulas, and Day's "Not a single calculation" is literally true (BO-04). Where the review does name maths it is weaker than it sounds. Day's MITTENS 2025 product already uses p = 0.02, the 2s value at s = 0.01 (Ga). The "1/N" is half-wrong even as a gloss, since the neutral value is 1/(2N). And Nₑ, the subject of point 4, does not appear in F_max at all (M-001); under neutrality it cancels from k (M-209). The capacity point stands. The empirical G_f is measured throughput, and Haldane's budget counts deaths per substitution, not s, so swapping 1/(2N) for 2s moves neither ceiling. "Probability vs rate" is the right distinction for the question MITTENS asks (M-605). The review's mechanism list (point 5) is a list, not a rescue: no number is attached to any item, so "the zero vanishes" is a promise. Points 6 and 7 attribute positions that no held Day text contains (the library holds no "no new information" claim from Day, and the coordinated-mutation model is Hössjer's, D15), and Day denies them. Regulatory change is substitution, and an observed divergence count already includes it, so evo-devo cannot lower the count. Rhetorically, the review opens with "Ignorant and Unscientific Drivel" and closes with "That is not how evolution works.", and it backs neither with arithmetic. A reader who wants the critic's case at its best must go to McCarthy's neutral count (M-914) or the audit's interference runs (R4 F2-A), not to this review.

## 9. Critic-side steelman

Bowers's summary describes real features of Day's calculations, even if not of the T/G_f count. The Darwillion prices a pre-specified list of 20M fixations at 1/20,000 each, which is a neutral fixation probability multiplied across required mutations, exactly what point 2 says (G4, M-703). The Appendix A chain is the "serial lottery" of point 3, and G2f holds there. The G_f input is a clonal, non-recombining LTEE rate (M-103; A5f). On the reposted text, Bowers does not confuse probability with rate. He says a neutral u "suppresses the rate of adaptive change", which is k = flux × u, and the 4Ns-fold gap is standard algebra (M-605). Day's reply answers a different point. Its defence, that "The entire MITTENS framework uses Haldane’s cost", misnames its own ceiling: the "220,000×" it cites comes from G_f = 1,600 (M-001), not from Haldane's 300 (M-802). And Haldane's cost bounds only selected substitutions (M-801). Invoking selection does not show that the 20M fixed differences required selection, and the neutral expectation on Day's own quoted inputs is of the order of the count (M-914). The recombination reply proves too little: "any individual allele" is a single-locus statement, while Bowers spoke of beneficial mutations from different individuals combining. The audit's own simulation finds free recombination keeps concurrent sweeps near full speed (R_int 0.975) where clonal linkage cuts them to 0.088 (R4 F2-A). The authority the reply cites for recombination, Kimura and Ohta 1969, does not mention it (H9). The "Kimura's algebraic error" aside is a reading Day himself later conceded (M-209). Bowers's model-dependence point is sound logic, and the held papers leave 5 of 18 named mechanisms uncomputed (M-901). "Bears no resemblance to anything in the book" overstates the case: each of the four descriptors fits a Day calculation.

## 10. Bottom line

Neither side does any new maths. Bowers's two formulas (2s, and its link to the adaptive rate) are textbook-correct. His claims about the book are partly right, since the Darwillion and the Appendix A chain have the features he names, and partly wrong, since the MITTENS count has none of them and he never names which calculation he means. Day's reply is right that the review gives no calculation, that the count has no pre-specified targets, that Nₑ does not enter F_max, and that 2s does not move an empirical or Haldane ceiling. It is wrong that Bowers "confused" probability with rate. It misnames its own ceiling (300 against the 1,600 behind its 220,000×). It answers a throughput point about recombination with a single-allele fact and a misattributed citation. The critics may fairly take the Darwillion-and-chain targets, the probability-to-rate link and the recombination result. Day may fairly take the untouched count, the absence of numbers and his own use of 2s.
