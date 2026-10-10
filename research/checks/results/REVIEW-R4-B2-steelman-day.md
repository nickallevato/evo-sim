# Review of R4-B2: Day-side steelman

Reviewer role: argue for Day as strongly as honesty allows, then judge fairness. Date: 2026-10-10. Targets: `results/R4-B2.md`, `research/checks/b2_hard_limits_internal.py` (3d07343, unchanged), `results/raw/b2_hard_limits.out`, the HL text `sources/raw/day/zenodo-22129121.txt` (read by line range, as data), claim files B, B2, B1c and B1d, `R4-X1-verdict-rule.md`, and `quotes-day.md` Q29-Q34. The numbers that are not in R4 (diffusion F and its time average) come from the scratch series evaluation described in `REVIEW-R4-B2-correctness.md`. No repo run.

## Verdict in brief
On the mechanics the check is fair to Day, and it says so. The definition, the exponent, the 7.8e7 arithmetic, the X algebra and his 600,000-run demonstration all hold. P6 is reported honestly as a failed prediction that went against the audit's prior. The unfair part is the rule-N section. It scores a sentence Day did not write in HL. It describes the field's 1e4 as "the ancestral N_e HL itself cites", when HL rejects that kind of N_e by name. It also does not RH-tag the peroration sentences that a critic would need to score.

## The strongest honest Day-side case
1. **HL is a narrow paper, and it says so.** In the abstract (l.22-24): "What substitution these abundant populations show is not produced at their current size; it is residual drainage from the smaller populations they descend from." At l.425-428: "This hard limit to fixation does not kill neutral theory ... Drift does fix neutral alleles, although only in populations small enough and stable enough". At l.437-441: "Every divergence ... is reading a rate that was loaded, at least partially, under population conditions that ended in the Holocene." Read on its own words, HL's thesis is a domain restriction on k = mu at current size, and B2 holds on it. The drainage paragraph (H7) is not something the audit found against Day. It is Day's own stated thesis.
2. **The exponent is right, and the demonstration is real.** The chain gives 9.3 expected against 6 seen, and 0.53 against 0. Day's mean of 391 is 1.4 standard errors from the exact 396.5 (correctness review, "not wrong"). The left tail of the conditional fixation time is exponentially thin, as Day said, against the critics' linear intuition (B2a credited the exponent as well).
3. **"Generous" was correct, and conservative.** At his own H8 input the exact F is 0.029 against his linear 0.35. The delivered fraction from an empty start is 0.003. Day conceded twelve times (by count, about a hundred times) more fill than the law gives.
4. **Day's endorsed variance N_e is not 1e4.** HL l.101-118 says the coalescent N_e is "circular reasoning ... a thermometer calibrated against itself", and that "We therefore use the variance Nₑ". The field's ancestral 1e4 is a diversity/coalescent estimate. H9's "not by accident" fits that section: a gene-tree-depth N_e lands at the lineage ceiling by construction. Day's own variance input is a census of about 1e5 with V_k = 5 (H8; B1d ¶31: "at the ancestral census of ~100,000"). Under rule C, that is the input to score him on.

## What does not survive scrutiny (the critic's side of this steelman)
- **Day's own later text gives up the empty start at the H8 input.** B1d (blog 2026-10-01 ¶36): "At the time of the CHLCA split, we can assume that it was full and 228,000 generations long". 228,000 = 4 x 57,143, which is exactly H8's census. The 3% (or 0.3%) "nearly empty" pipe is therefore not Day's position, and it cannot be offered on his behalf.
- **HL's own lineage window undoes H8's 2 My.** l.244-253 accepts the first objection ("The objection is valid"), and Table 1 (l.157) runs humans at 6.5 My. At census 1e5 over 6.5 My, F = 0.70 (time average 0.26 from empty). H8's census sits at the lineage ceiling (X = 114,000), where l.361-363 says the pipe "substantially fills". So the most coherent reading of HL is not the one most helpful to B.
- **l.453-457 is hard to read as current-size only.** "Both the priced channel and the free channel shut inside the same lineage duration" names the lineage, not the current census. The charitable tag below is the best Day can get. It is an argument about genre, not about the numbers.

## Findings

### D1 (MAJOR). The provisional non-sequitur scores a paraphrase; HL's verbatim B-quote holds; the Feb quote is not answerable to HL
Locator: R4 "Rule N" section and "Who this helps", critic side.

Problem. "Cannot rescue the shortfall" is the claim title. B's HL Statement is the abstract sentence, which R4 itself scores `holds` for B2. B's other Statement, "the second is flat-out wrong" (blog 2026-02-04 ¶60), predates HL. Under N2b, "own text" is the same source and the texts the claim cites. The X1 rule dropped B3c's cross-document basis for exactly this reason. HL l.425-428 is a later softening of that blog line. Rule SC says a later-source correction is scored on the version quoted, with the note "corrected in X". That makes it a versions-ledger entry, not an error in HL.

Fix. Withdraw "non-sequitur (provisional), against H7". Score B's HL quote `holds`, note "revised in HL l.425-428" on the Feb quote, and leave B internal `pending` unless l.453-457 is added under S1 and scored (D3). Same as correctness finding 1.

### D2 (MAJOR). "The ancestral N_e HL itself cites (1e4)" misattributes an endorsement
Locator: "Who this helps", critic side ("at the ancestral N_e HL itself cites (1e4) the pipe is 95-100% full"), and the Rule N table row "H9 field value".

Problem. HL mentions 1e4 as "the size the field's own methods assign" (H9). HL also gives the abstract's rounded "about ten thousand" ceiling (Q29), which B2b already found does not match its tables (35,000-114,000). HL's only stated N_e for scoring drift is the variance N_e (l.101-118), and its only hominid census is H8's 1e5. Calling 1e4 "HL's" input makes the critic row look internal when it is the external value that B1c and B4a test.

Fix. Relabel the row "field (coalescent) value, mentioned in HL, not HL's variance input". In "Who this helps", replace "HL itself cites" with "HL mentions as the field's figure". Move the 1e4 and 2.5e4 rows to the external discussion, or label them as such.

### D3 (MINOR). The peroration sentences carry B in HL but are not RH-tagged; Day's charitable tag is `rhetoric`
Locator: R4 opening paragraph (RH tags only "atoms" and "the window ... is empty").

Problem. l.453-467 ("And now the neutral channel closes ... the pipe that would finish them never fills"; "the pipe was nearly empty") sits in the closing section, "The Question No One Asked". It is figurative (channel, pipe, shut) and addressed to readers, and it restates without new numbers. Under RH1 with rule C on kind, it can be tagged `rhetoric`, with device metaphor/peroration and audience the general reader. Its function is to join the neutral and adaptive channels into one closure. Its dialectical core is the current-size claim already scored as B2 `holds`. If tagged that way, nothing in HL that is dialectic asserts that ancestral drainage falls short, so B (HL) holds. The critic steelman argues `dialectic` (F2 there). The write-up should record both and pick one.

Fix. Add the RH1 tag for l.453-457 and l.464-467, with the four RH2 entries if `rhetoric`.

### D4 (MINOR). "Best case" in H8 has a charitable reading the write-up does not try
Locator: Rule N section, "census 1e5, which is less favourable for filling than 1e4".

Problem. The write-up implies that Day mislabelled a less favourable census as "best case". HL l.371-377 says constant size is "the generous case", because expansion lengthens transit. "Best case" can modify "held static for the full two million years" (no expansion, the full span), not the census figure. Rule C requires this reading to be tried and recorded.

Fix. Record the reading. It does not change the numbers.

### D5 (MINOR). P6 credit is right in substance, but the headline should give the Day credit its correct content
Locator: QUEUE and commit wording "P6 failed in Day's favour (best-case fill 3%)"; R4 "Who this helps", Day side.

Problem. What favours Day is that his "generous" label is confirmed and that his concession (35%) was larger than the truth. The "3% loaded pipe" itself is not a Day-side gain, because Day abandons the empty start at that input (B1d) and HL accepts the 6.5 My window (see the critic's side above and steelman-critic F1). As phrased, the headline invites a reading that the critic reviewer will rightly attack, and that weakens the real credit.

Fix. Change it to "P6 failed in Day's favour: his linear bound is generous (exact 0.029 vs 0.35 at his 2 My input)".

### D6 (MINOR). Record that B2's current-size reading is Day's text, not audit charity
Locator: R4 "Reading" paragraph ("holds for current sizes under rule C").

Fix. Cite abstract l.22-24 as the basis. Rule C is not needed for this reading, and saying so credits Day more accurately.

### D7 (MINOR). The time-average point cuts both ways and should be stated both ways
From an empty start, at N_e = 1e4 over 2 My, only 51% of mu*T is delivered, not 95% (correctness finding 2). That favours Day on any empty-start reading. Pre-window fill (B1d, B1c) reverses it. The write-up should show both.

## View of the verdicts
- B2 internal `holds`: agreed (D6).
- B2a-type mechanics (P2-P5): `holds`, with full credit to Day.
- B internal: `pending`, not `non-sequitur`. If l.453-457 is added and tagged `rhetoric`, the HL basis gives `holds`. If tagged `dialectic`, the critic F2 argument applies, and the reading (2 My vs 6.5 My) decides it.
- P6: a genuine Day-side credit for the "generous" label, not for an empty ancestral pipe.
