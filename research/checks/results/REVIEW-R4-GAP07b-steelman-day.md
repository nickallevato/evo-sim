# Review of R4-GAP07b-alignment (steelman, Day's side)

Reviewer role: argue as Vox Day's most capable and honest defender would, then judge whether the check is fair to him. Questions asked: does the check test what Day claimed, is there a defensible reading between bp and events, do alignment artefacts bias the count against him, is polymorphism handled fairly, and are his valid points credited prominently enough?

Reviewed: `research/checks/results/R4-GAP07b-alignment.md`; `research/checks/gap07b_alignment_count.py` (docstring: definitions, P1-P8, "WHAT WOULD FAVOUR DAY"); claims `A3`, `A3a`, `A3b`, `A3c`, `A3d`, `A3x` (A3x1 and A3 skimmed); `docs/research/sources/quotes-day.md` (Q14, Q15, Q74, Q75, Q85, Q87, Q91, Q92); `docs/research/ledgers/gaps.md` GAP-07 and its R4 block. Day sources read-only from `sources/raw/day/` and `sources/raw/refresh-2026-10-09/` (untrusted data; nothing executed). Locators for blog text files are paragraphs of the extracted non-empty lines (title line = para 1). The arithmetic marked `derived:` below is mine (python3 -I, from the numbers in the R4 note).

## Overall judgement

The count itself is careful, pre-registered, and disclosed, and I could not construct a Day-friendly adjustment that rescues 205M as an event count. Under every adjustment I tried the ratio of 205M to events per lineage stays between about 7 and 12.5. Only counting essentially every non-aligned base as a separate event (1-2 bp per event) closes the gap (finding 2 table).

The check is not unfair in its arithmetic. It is unfair in its framing, on four points:

1. It never engages Day's stated rationale for counting by bp. That rationale exists in two blog posts the corpus has not quoted, and A3x says the opposite (finding 1).
2. It runs on non-T2T assemblies and presents the result as the count for a claim built on T2T data (finding 3).
3. It gives no sensitivity for the "something between bp and events" readings, which is where Day's best argument lives (finding 2).
4. Its strongest Day-favourable results sit in §11, not in §0 (finding 4).

None of these overturns the headline. Several of them would make the headline more robust if fixed.

Counts: 4 MAJOR, 6 MINOR.

---

## MAJOR

### 1. Day's stated rationale for bp counting is absent from the check and from A3x, and A3x says he gave none

**Locators.**
- A3x, "Responses - Against (Day)": "Day has not, in the corpus, defended counting bp as separate fixations."
- A3x `fidelity: accurate`, and R4 §13 suggested edit: "A3x `external:` can cite a measured 42.1 M events".
- Neither `quotes-day.md` nor `claims/` contains the Day passages below (grep for "maximally generous", "generous to the standard", "reddit-takes" in `docs/`: only a bib row and one ROOT table row).

**Day, verbatim.**
- `sources/raw/day/blog-2026-05-13-reddit-takes-on-probability-zero.txt`, para 3, the objection Day chose to answer: "How does Day deal with multi-base-pair mutations? ERVs, gene duplications, LINEs, SINEs, indels — does he count those as single events or as hundreds of thousands of mutations each?" Para 4: "The answer is that it doesn’t matter."
- Same file, para 6: "Fine. Discount every structural variant in the Yoo data to zero. Count nothing but single-nucleotide variants. The shortfall on the SNV-only subset is still four to five orders of magnitude. Going the other direction — counting every base pair in every structural variant as a separate mutation — pushes the shortfall to six orders of magnitude. The conclusion holds either way. Counting structural variants as single events is the maximally generous treatment, and the model still fails."
- `sources/raw/day/blog-2026-04-28-less-than-zero-3.txt`, para 19: "A point mutation requires one mutation event and one fixation event. A 50,000 base pair insertion or a chromosomal inversion requires the entire structural rearrangement to occur as a single low-probability event and then to fix. Counting these by base pair, as the gap-divergence figure does, is generous to the standard model. Counting them by independent fixation events would be more devastating still."
- Same file, para 18: "the requirement on the human lineage rises from 20 million fixations to roughly 207 million."
- Same blog family, Objection 11 (`blog-2026-05-13-...txt`, para 51): "Counted as a single event, you still need it to fix, and chromosome fusions create immediate meiotic incompatibility with the rest of the population".

**Argument.**
- On the question "does Day say fixations means events or that bp is the right unit?", the honest answer is neither. Day says an SV is one event needing one fixation (04-28 para 19). He uses base pairs as a proxy for the difficulty of that event, and calls the proxy generous. He also presents 205M as the upper bracket of a two-row range, with the SNV-only count as the lower.
- His rationale is a weighting claim: a large rearrangement is a rarer event and harder to fix than a point mutation (underdominance, meiotic incompatibility), so a bp count understates its cost.
- The R4 text and A3x treat the 205M as an unexplained unit error. That is the critic framing. Day's framing is "range plus weighting", and the check tests neither part of it.

**Counterpoints that hold against Day.**
- The weighting is asserted, never quantified (finding 2 supplies the quantity he would need).
- "Discount every SV to zero" is not the event treatment. It drops about 4.3M indel events (10% of all events), so the "maximally generous" row is the SNV floor, not the event count.
- The weight applies to ~1,000 inversions and fusions, not to the 1-10 bp indels that are 89% of events.

**Fix.**
- Add the four passages to `quotes-day.md` as new Q-entries (branch A3, A3x).
- Rewrite A3x "Responses - Against (Day)": Day gave the weighting rationale on 2026-04-28 and 2026-05-13 and set 205M as the upper bracket.
- R4 §11: add "Day's position as he stated it" to the Day block.
- In R4 §0, one sentence: the 9.7x tests "events as the unit", and Day's stated position is that bp are a generous proxy for harder-than-point events, which §6 and the new table in finding 2 address.

### 2. No sensitivity for the readings between bp and events, which is where Day's best argument lives

**Locator.** R4 §6 ladder (bp per event 6.2, 12.4, 17.0); §11 "Neither side"; caveat 6 ("Events are not fixations"). The ladder shows bp per event but not what unit or weight is needed to reach 205M. P5's pre-registered L3 target "bp/event 7-18" is exactly the quantity Day would dispute, so the check does not stress it.

**Argument.** The honest Day reading is "something between", so the check should say what it takes to close the gap. Using the R4 numbers (`derived:`):

| reading | extra events added to the 42.1M | per-lineage events | 205M / that |
|---|---|---|---|
| events as measured | 0 | 21.1M | 9.7x |
| non-aligned bp (223 Mb outside aligned blocks) counted as 171 bp units (alpha-satellite HOR monomer, A3a) | +1.3M | 21.7M | 9.4x |
| same, 32 bp units (Yoo's smaller unit in A3a) | +7.0M | 24.5M | 8.4x |
| non-aligned plus non-colinear nested (486 Mb), 171 bp units | +2.8M | 22.5M | 9.1x |
| same, 32 bp units | +15.2M | 28.6M | 7.2x |
| same, 6 bp units | +81M | 61.5M | 3.3x |
| same, 2 bp units | +243M | 142.5M | 1.4x |
| same, 1 bp (full bp reading) | +486M | 263.9M | 0.8x |

Weighting reading: events above 50 bp number 113,293 (90,044 + 23,249, R4 §5), i.e. 56.6k per lineage. To reach 205M per lineage with all other events at weight 1, each such event must count about 3,250 SNV-equivalents on average. A 51-1000 bp event averages 254 bp, so the weighting cannot be bp-proportional there. It would need to be a fixation probability thousands of times below a point mutation for events of a few hundred bp.

**Reading of the table.**
- Day's number reappears only if almost every non-aligned base counts separately. At any repeat-unit size of 32 bp or more the ratio is 7-9x.
- That is a stronger statement of the result than the single 9.7x, and it answers the "something between" question directly instead of leaving it as an aside.
- Standard theory also bounds the weighting. A neutral allele fixes with probability 1/(2N) regardless of length. A selected insertion sweeps as one allele. Day's own G_f counts events: `zenodo-23003785.txt` lines 88-94 (s2): "IS-element insertions are mutations that fix". The rate in the denominator of his shortfall is therefore per event, not per bp, which is the unit-mismatch point already in GAP-07.
- The one real basis for a penalty is underdominant rearrangements (inversions, fusions), and these are about 10^3 events, not 10^5.
- I also tried the segmental-duplication or gene-conversion argument for Day. It cuts the other way: a conversion tract turns one event into many mismatches, so the 37.8M SNV "columns" overstate events, not understate them.

**Fix.** Insert the table above (or an equivalent) in R4 §6, with the weight figure, and cite it in §0. Keep the "what would change this verdict" sentence: a published measurement that fixation of 1 kb to 100 kb insertions is thousands of times slower than point substitutions, in the same assay as G_f.

### 3. The test is run on hg38 vs panTro6, not on the T2T data Day's number comes from, and the headline does not say so

**Locators.** R4 §0 ("Day's 205 M per lineage is 9.7 times the measured events per lineage"); §3 (hg38, panTro6); §6 (human N 161.6 Mb; centromere models 59.5 Mb; unaligned 134.5 Mb human, 88.6 Mb chimp placed); caveat 3; §13 edits for A3x and A3a. Day: `quotes-day.md` Q15 / `zenodo-23003785.txt` s7.1: "Yoo et al.'s complete telomere-to-telomere assemblies reveal substantially more divergence". Q91: "using the telomere-to-telomere genome assemblies of Yoo et al. (2025)".

**Argument.**
- Day's claim is explicitly about complete T2T assemblies: 04-28 para 5 says the 35M SNV figure "was only the divergence in the portion of the genomes that aligned cleanly".
- hg38 and panTro6 are not T2T. The regions where Yoo reports the new divergence (centromeric satellite, acrocentric arms, large SDs, heterochromatic caps) are the ones hg38/panTro6 resolve worst. The check counts them as 7,452 unaligned segments plus 32,045 nested fills, a very small number of events for 224 to 486 Mb.
- Events inside those regions (monomer-level changes, copy-number steps in arrays) are mostly not enumerable here. Caveat 3 concedes the direction ("critic-favouring").
- Yet §13 proposes to write "a measured 42.1 M events" into A3x and to say the A3x pre-registered 40M +/- 30% is "met". That prediction was about the T2T comparison. The 42.1M is a count for a different pair of assemblies and is a lower bound where repeats dominate.
- The sensitivity range in finding 2 bounds this, and it is not a large effect. But the labelling matters: the text should not imply the T2T event count was measured.

**Fix.**
- Label every headline as "hg38 vs panTro6 (non-T2T)".
- Report 9.7x with a bracket (7.2x to 9.7x from the unit table) rather than a point.
- In A3x and A3a, state that the measured count is on non-T2T assemblies, so it is a lower bound for repeat-rich sequence, and that A3x's prediction is "met on the available alignment" rather than on Yoo's data.
- Recommended follow-up (not run): repeat on CHM13/hs1 against the Yoo chimp assembly (mPanTro3). That removes the largest gap between the test and the claim.

### 4. Day's valid points are in §11, not §0, and the strongest one is undersold

**Locators.** R4 §0 (bold "9.7 times", then one sentence on bp); §11 bullets 1-5; §13. A3b `external: contested`: "only the 205M bp headline falls".

**Argument.** The pre-eminent finding for Day is not "the base-pair figure is real". It is that his own lower bracket is, to within 20%, the event count. The measured numbers are:

- SNV 37.77M is 90% of the 42.1M events (`derived:`).
- Day's 17.5M SNV-only per lineage versus the measured 21.05M per lineage: 83%.
- Day's SNV-only shortfall at the same rates therefore rises, not falls. At 1,322 gen/fix: 21.05M / 190.6 = **110,400-fold** (his 91,600). At the mutator rate (2,407 achievable): **8,750-fold** (his 7,271). At the strict 1,587 rate (Q85): **132,600-fold** versus 110,200 on 17.5M (`derived:`).
- Day's two-row bracket (SNV-only 17.5M and bp 205M) contained the right unit in the lower row. Only the upper row fails as an event count.
- The symmetry of the lineages (49/51) supports his "apportion symmetrically" step (A3d). That is in §11 but not in §0.
- Day's choice of the larger 410M also does not depend on polymorphism for SVs: 04-28 para 25 says "Structural variation is, with very few exceptions, post-divergence" (see finding 6).

§11 bullet 2 says the SNV-only variant "is a floor and not the event count" and that "The shift is about 12-20% and does not rescue the unit argument". That wording reads as a rebuttal of Day, when the measured shift strengthens his fallback. A reader of §0 alone will conclude only that his headline is 9.7x too big.

**Fix.**
- Add a short "What survives for Day" box to §0: (a) the bp magnitude (261-523 Mb) matches 410M; (b) SNV-only is an event count to within 17-20%; (c) his SNV-only shortfall rises to 110,000-fold on the measured count; (d) the 49/51 symmetry; (e) polymorphism is counted in the Day-favourable direction.
- A3b: add the 110,400 and 8,750 numbers under "Check" with the caveat that the shortfall itself rests on G_f (branches A2, A5).

---

## MINOR

### 5. The pre-registered "favours Day" criteria could not be met by Day's actual position

**Locator.** Script docstring, "WHAT WOULD FAVOUR DAY (the unit of 'required fixations' is a bp)"; R4 §2 last paragraph ("The criteria stated in advance as 'favours Day' ... were not met").

**Argument.** The criteria are events per lineage of about 100M or more, bp/event at L3 of 3 or less, and lineage asymmetry. Day's position (finding 1) predicts none of these. He does not claim events are ~100M; he claims bp are a generous weight for the events. A result of "criteria not met" is therefore almost guaranteed and carries little information about Day.

The prediction his position does make is "base pairs in divergent regions are of the order of 410M". That prediction was tested (P5, §6 ladder, 261-523 Mb) and came out confirmed for the two-genome total, but the scorecard does not mark it as a Day-side success. P5's "L3 300-700M ... held F1 only" and "bp/event 7-18 held under all four filters" are presented as critic-side results.

**Fix.** In §2 reword the last paragraph to "the criteria for favouring a literal events-near-205M reading were not met; the criterion 'bp in divergent regions are of order 410M' was met (261-523 Mb)". Add a "Day (stated position)" column to the scorecard.

### 6. Polymorphism is handled in the Day-favourable direction, but the band quoted for the fixed-only case assumes an SNV fraction for all event types

**Locators.** R4 §0 ("11.3-12.5 times if only the 78-86% fixed share of the differences is counted"); §4 polymorphism bullet; script docstring ("Day-favouring bias if polymorphic differences are counted as required fixations, a critic-favouring one if not"). Day, 04-28 para 25: "Structural variation is, with very few exceptions, post-divergence".

**Assessment.**
- Fair on direction: leaving polymorphism in raises the event count and lowers the ratio, so the headline 9.7x is the Day-favourable value. The docstring wording is confusing, because "Day-favouring" there means Day-favourable for the opposite quantity. The result note states the direction correctly in §0 and §4.
- Overapplied: 11.3-12.5 applies the CSAC 14-22% SNV polymorphism fraction to all events including indels and SVs (0.78-0.86 times 21.05M gives 16.4-18.1M). If I apply it to SNVs only, the band is 11.1-12.1 (`derived:`). Day's claim that most SVs are post-divergence points the same way; the polymorphic share of SV events is unmeasured.
- Fixed share is a legitimate adjustment in Day's own frame, because differences that still segregate within a species do not need fixation. Ancestral polymorphism that sorted after the split does (04-28 para 24: ILS "distributes the fixation requirement across both lineages"). The check correctly does not subtract that.

**Fix.** Quote the bracket as "9.7x (polymorphism included, the Day-favourable value) to about 11-12.5x (SNV polymorphism fraction applied to events; the polymorphic share of indels and SVs is unmeasured)". Replace the docstring sentence with a one-line statement of the sign.

### 7. Artefacts: the report states one direction (fragmentation inflates) and underweights the opposite ones

**Locators.** R4 §8 last bullet; caveat 2; caveat 3.

**Argument.** Fragmentation does bias toward Day, as stated. The opposite-direction items that the report mentions only in passing or not at all:
- Chain gaps count net length change. Two opposite slippage steps in a microsatellite show as zero or one gap. Indels are 4.3M of the events; even doubling them moves 9.7x to 8.8x, and tripling to 8.1x (`derived:`).
- Complex "both-sided" gaps (35,138) count as one event where two lineages each changed; it adds 0.1%.
- Chimp-specific duplications absent from the net are only partly captured by the 32k nested fills.
- 44.9 Mb of chain-gap bp is assembly N and 356 Mb is aligned elsewhere. The report treats these as already counted (nested fills), which is a modelling choice.
- SNVs in records over 2% divergence (4.0M) are in the headline total. That is Day-favourable and the report does show it.

None changes the order of magnitude. A short table of directions would be fairer than the single sentence.

**Fix.** Add a "direction of each artefact" table to §8 listing each item above with sign and an indicative bound.

### 8. Unit usage in Day's own editions cuts against him, and the check could say so while still being fair

**Locators.** `sources/raw/day/blog-2026-05-23-probability-zero-2nd-edition.txt`, para 4: "All of the mathematics that I utilized in the first edition of this book were based on the observed divergence of 40 million base pairs between the two lineages published in the 2005 paper." Para 6: "This 10x increase in the number of observed differences between the two genomes". `blog-2026-04-28-less-than-zero-3.txt`, para 5: "approximately 35 million single nucleotide differences and 5 million indels affecting roughly 90 million base pairs of sequence. Forty million differences out of three billion base pairs." Q91: "approximately 410 million total genomic differences ... approximately 205 million fixations".

**Argument.** The first-edition 40M is 35M SNVs plus 5M indel events, not 40M bp (Day himself says the indels span about 90M bp). So "40 million base pairs" in his words is an event count, and the "10x increase" compares a 40M event count with a 410M figure that includes bp. This is the most direct internal evidence that the unit changed between editions. The measured 42.1M events is within 5% of his first-edition 40M. The check does not point this out, and it should. It also shows Day uses "base pairs", "differences", and "fixations" interchangeably, so the report should not claim his unit is bp as a stated rationale. The accurate statement is that his wording is inconsistent and his stated rationale is the weighting argument in finding 1.

**Fix.** Add one sentence to §11 under "Neither side" quoting these paragraphs, and cite the 42.1M against 40M as "no T2T increase in events on these assemblies; the 10x increase is in bp".

### 9. The two coincidences with Day's numbers are flagged once but not both

**Locator.** R4 §6, "A numeric coincidence, flagged": 134.5 + 88.6 + 187.0 = 410.09 Mb.

**Argument.** The report is right that the sum mixes three components and should be treated as chance. The same table also contains 187.0 Mb as the unaligned share of the chimp unplaced scaffolds, which equals Day's "approximately 187 megabases" (Q15) to three digits. The report does not mention that second match, and a reader who finds it later may read it as evidence. Both are almost certainly chance (Yoo's 187 is a T2T SDR total, and A3a records that no pair or sum of Yoo's SDR totals gives it), but the flag should cover both, and the conclusion remains "not used as evidence".

**Fix.** Add one sentence naming the 187.0 Mb match to the flagged coincidence paragraph.

### 10. Minor edits to prominence and wording

- R4 §0 and the title use "Day's 205M is 9.7 times the measured events per lineage". Day's 205M is "required fixations" and the check measures events; caveat 6 already says "Events are not fixations". Put that sentence next to the headline rather than in §10.
- "Neither side" in §11 says the bp-per-event statement used by critics needs its definition (6 to 17). That is fair and should also be in §0, since the ladder range 0.57 to 1.6 for 410M/bp is the Day-side reading of the same table.
- §13 suggests citing "a measured 42.1 M events" in A3x. Prefer "42.1M events (hg38 vs panTro6; both lineages plus polymorphism), 21.1M per lineage".

---

## Answers to the specific questions

1. **Does it test what Day claimed?** Partly. It tests whether the number of events equals 205M, which Day did not claim. It reproduces his bp magnitude. It does not test his stated rationale (weighting, upper bracket), which finding 2 turns into a falsifiable quantity.
2. **Does Day say fixations means events or that bp is the right unit?** Neither exactly. On 2026-04-28 he says an SV is one event and one fixation, and that bp counting is generous. On 2026-05-13 he calls 205M the upper bracket and SNV-only the lower one. His first-edition "40M base pairs" was an event count.
3. **Is there a defensible reading between bp and events?** A weighting reading exists in principle (underdominant rearrangements). It does not extend to the 113k events above 50 bp at the weight needed (about 3,250 SNV-equivalents each), and repeat-unit readings give 7-9x.
4. **Do alignment artefacts bias against Day?** The non-T2T assemblies and the net-length treatment of tandem repeats bias against him; fragmentation and the 2%+ divergence SNVs bias toward him. The net effect is bounded at roughly 7-10x.
5. **Is "includes polymorphism" handled fairly?** Yes on direction. The 11.3-12.5x band over-applies an SNV fraction (finding 6).
6. **Are Day's points credited prominently?** Not enough; see finding 4.
