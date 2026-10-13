# Correctness review 2 of claim B `verdicts.internal` (O5 1/6, D-21)

Date 2026-10-13. Reviewer: fresh reviewer instance (Paperclip EVO-59), skill `review-correctness`, brief `research/checks/briefs/O5-reviews-reviewer.md` (f9e254d). Labels: BLOCKER / MAJOR / MINOR / NOTE.

**Independence.** I did not author R4-B2, R4-RHclose, the integration or the O5 revert. I have written none of the other five O5 reviews. The subject line of f66ce55 (the critic-side steelman of this field) appeared in `git log` when I started. I did not open that file.

**Question (brief).** The question is not whether the superseded `non-sequitur` was right. It is whether the evidence on record carries `verdicts.internal` of B to `non-sequitur` under rule C, rule RD (D-15 wording) and the scoping the claim file states. I set no verdict.

**Read.** Claim file `claims/B-neutral-theory-cannot-rescue.md` (all 91 lines). `R4-B2.md` Rule N section (l.21-57, 90). `R4-RHclose.md` Part 2 and Review resolution (l.54-198). `rhclose.py` docstring l.78-86. `REVIEW-R4-RHclose-combined.md` MAJOR-2 and MAJOR-3. `R4-X1-verdict-rule.md` rules C, SC, N, RH, RD. `quotes-day.md` Q140, Q151-Q158. `ledgers/slips.md` RH-10 and RH-26, and `ledgers/versions.md` l.33. `DECISIONS.md` D-12, D-15, D-21 and O-5. The diff of 3f881b0 for B. Raw outputs `raw/rhclose.out` and `raw/rhclose_posthoc.out`.

## 1. Recomputation (independent, stdlib, under a second)

I used the exact Kimura (1955) series for an empty start, F(x) = 1 + Σ(-1)^i(2i+1)e^{-i(i+1)x/4} with x = T/N_e, and the delivered share D(x) = (1/x)∫₀ˣF. Hand-checked to three terms for 4.55, 4.41, 2.6 and 1.4.

| Row (g = 25 y) | x | F | D | On record | Match |
|---|---|---|---|---|---|
| HL N_e 57,143 (4·1e5/7), 6.5 My | 4.550 | 0.69703 | 0.25564 | 0.697 / 0.256 | yes |
| same, 6.3 My | 4.410 | 0.67594 | 0.24196 | 0.676 / 0.242 | yes |
| H8 2 My | 1.400 | 0.02547 | 0.00337 | 0.025 (claim), 0.026 (R4-RHclose l.79, R4-B2 l.37) / 0.003 | 0.026 is a double rounding (NOTE-14) |
| Takahata 1e5 held, 6.5 My | 2.600 | 0.28077 | 0.06487 | 0.281 / 0.065 | yes |
| Takahata 1e5 held, 6.3 My | 2.520 | 0.25954 | 0.05836 | not reported | new |
| Takahata 1e5, 6.5 My, g 20 / g 29 | 3.25 / 2.24 | 0.447 / 0.187 | 0.125 / 0.038 | not reported | new (MINOR-6) |
| Yoo 1.98e5 held, 6.5 My | 1.313 | 0.01749 | 0.00218 | 0.018 / 0.002 (R4-RHclose table only) | yes |
| Ratios against the 0.30 edge | | 0.697/0.30 = **2.32**; 0.676/0.30 = 2.25 | | "0.697 … 2.25x" (claim l.12) | **no** (MINOR-8) |

Every number in the Readings table reproduces. The arithmetic is not in question. The problem is the mapping from readings to the verdict.

**Source check.** The repo's local text (`sources/raw/day/zenodo-22129121.txt`, sha256 3182a5b6…) is not present on this workstation or on na-workhorse. I fetched it fresh into `sources/raw/b-corr2-2026-10-13/`. The Zenodo record 22129121 was created 2026-08-27, and `Hard_Limits_Fixation_Drift.pdf` has md5 4f66a658…0abc (equal to Zenodo's checksum) and sha256 66aa8be6…19bf. `pdftotext` gives `hl.txt` (sha256 9cfb86be…70fc7, 636 lines). Its line numbers differ from the local text, so **"HLf l.N" below means the fresh text**. The following are all present verbatim: Q140, Q151, Q152, Q155, Q156, Q157, Q158, "lineage duration … six and a half million years" (HLf l.350-352), "thirty-five percent fill across two million years even when granted the entire lineage" (HLf l.583-584) and "a partly-filled pipe inherited from a lower-census past" (HLf l.586).

## 2. Findings

### BLOCKER-1: reading S is mapped to `non-sequitur` with no derivation, against the record's own analysis (claim l.12, l.83)
- **The record.** The registration says the opposite: `rhclose.py` l.83-84 reads "if the owner prefers S, the line restates B2, which holds, and B's verdict is the same as under the rhetoric tag". R4-RHclose l.110 says the same. The RHclose review (MAJOR-2 iii) concludes: "Under S the line restates a true B2 and would be dialectic and true." The fix pass (R4-RHclose MAJOR-3 answer, l.170) then put S into one bucket, "If the owner chooses dialectic: B internal = `non-sequitur`", and derived nothing for S. The claim file carries "S … non-sequitur at lineage level; B2 itself holds" (l.83).
- **"Lineage level" is unscored.** The only lineage-level conclusion left once Q157 is read as S is B's title, "cannot rescue the shortfall". Rule S1 leaves the title unscored (R4-B2 l.22; claim l.75). Under the rhetoric reading the same title gets "no dialectical support offered" (RH3, l.80). Under S it gets `non-sequitur`. The same unscored text is treated two different ways.
- **Under D-15, S is the strongest candidate for the field value.** D-15 defines the field value as the reading under which the quoted statement is "most defensible (closest to literally true, best supported)".
  - Under S the statement is literally true. It is B2, which `holds`.
  - S is consistent with HL's own drainage concessions, because those concern the far end of the pipe. S has textual support in Q157's own neighbourhood. HLf l.521-522, two paragraphs before the "fill" definition, reads: "So the neutral substitutions these species exhibit today are not being seeded at their current size at all. The channel is not slow, it is empty." Q158 reads "look at the near end". The abstract has "not produced at their current size" (Q140).
  - Under S, Q157 also reads coherently: at current census the pipe cannot fill within the lineage duration, which is B2's X ceiling with T = 6.5 My.
  - Rule C requires the scorer to try this charitable referent *before* a mismatch (N2b) is scored against the author.
- **Fix.** Do one of the following:
  - (a) Derive a non-sequitur under S. Name the clause of Q157, its reading and the HL sentence it contradicts. Or show that S is not a plausible reading, and explain why the RHclose fix pass accepted it as one (MAJOR-2 table).
  - (b) Map S to `holds`, scoped to the B2 statement. B's lineage-level title then has no support from the Statement quotes, the same wording as RH3 uses under the rhetoric reading. Then rank S against the empty-start readings under D-15 and record the ranking.

  Until one of these is done, the record does not carry `non-sequitur` as the field value.

### MAJOR-2: the N2b premise was derived for one reading in R4-B2 and carried to four readings without re-derivation (claim l.12; R4-B2 l.25)
- **Where the derivation came from.** R4-B2's dialectic reading is the lineage reading over 6.5 My that "uses the body's numbers" (l.25). That is the reading RHclose later scored as F 0.697, which is *rhetoric*. The derivation, "needs an empty lineage pipe, which HL's own text excludes", was written for that reading. After RHclose split the readings, the claim file attached it unchanged to D, Takahata 1e5, S and 2 My.
- **Readings D and 1e5.** On these readings the fill clause is close to literally true *on HL's own model from an empty start at the CHLCA*. N2b therefore needs HL text that excludes that empty start for the human lineage. The cited texts do not supply it:
  - Q140 is generic ("the smaller populations they descend from").
  - Q151's context is mice and fruit flies (HLf l.521-528).
  - Q152 is conditional ("When Nₑ is of the same order as T").
  - Q156 places the loading "under population conditions that ended in the Holocene", that is, inside the window.
- **HL's human-specific text is compatible with these readings.** HL calls the hominid pipe "a partly-loaded pipe, the near-ceiling regime" under a "generous" linear bound of about 35% (HLf l.532-534). It also calls it "a partly-filled pipe inherited from a lower-census past" (HLf l.586).
  - Both are compatible with "never fills" and with D 0.256.
  - The in-window loading at HL's own hominid census (1e5) is already inside the empty-start D.
  - Pre-CHLCA fill is granted only in B1d, a later and separate Day text. The file's own temporal rule (the Feb quote is "not answerable to HL") cuts the same way here: HL is not answerable to B1d.
  - Without excluding text, the fill-state dispute is N1 (external; B1c/B4a), not N2b.
- **Fix.** Re-derive N2b for each reading. For D and 1e5, cite human-lineage HL text that excludes the empty start, or record "N2b not shown" for these rows.

### MAJOR-3: the field is set by a "Candidate Statement" plus a quote outside the Statement (claim l.27-29; R4-B2 l.24)
- The field rests on Q157 alone. Quote 1 is rhetoric (l.32). Quote 2, the abstract, holds as B2 on every reading.
- Q157 is still labelled "**Candidate Statement**" (l.29). R4-B2 l.24 says it "must be added to B's Statement under S1 and RH-tagged before it can be scored".
- The band "never fills / nearly empty" and the S referent ("near end") come from Q158, which is not a B Statement quote.
- **Fix.**
  - Confirm Q157 as a Statement quote, or keep the field `pending`.
  - Either add Q158 to the Statement, or confine the readings to Q157's own words ("never fills", "lineage duration") and justify applying the F <= 0.10 band to "never fills".

### MINOR-4: a plausible reading of Q157's own words is not recorded (claim l.78-84)
- HL defines filling as reaching the k = μ flux (local l.272-275, cited in R4-RHclose l.59). Read that way, "never fills" means "F never reaches about 1".
  - The fill clause is then literally true at HL's input (0.70 < 1) and false at field N_e (F = 1.000).
  - The inference "cannot be finished" can then be tested by N2a against HL's own F. A 0.70 flux by Q152's own standard is "substantially fills", and Kimura's rate is approached. That test favours the critics, depending on how "cannot be finished" is read.
- RD requires every plausible reading to be recorded. **Fix:** add this row with its tag and verdict.

### MINOR-5: the 2 My reading cites the wrong excluded premise (claim l.84)
- On 2 My, N2b can be derived, but through HL's defined "lineage duration". HL accepts 6.5 My: "The objection is valid, the correction triples the ceiling" (HLf l.350-356). Q157 uses that defined term.
- The cited ancestral-fill quotes are not the excluded premise for this reading.
- Rule C must also weigh HL's own contrary usage: "two million years even when granted the entire lineage" (HLf l.583-584). HL's own figure for that window is about 35% ("partly-loaded"). The exact value is 0.025.
- **Fix:** cite the window premise and address that usage.

### MINOR-6: D and Takahata 1e5 as readings (claim l.81-82)
- **D.** HL fixes what fill means: "The exponent also fixes what the 'fill' means" (HLf l.530). That is F. D is Day's quantity from a different paper (Q34, Intrinsic Irrelevance). RD bars "extended readings (a different object…)" from setting the field. The record must say whether D is a plausible reading or an extended one.
- **Takahata 1e5.** This is an external input that HL does not state. R4-RHclose first excluded it as "not a lineage value". Its tag also depends on g: F 0.447 at g 20 (rhetoric) and 0.187 at g 29.
- **Fix:** state the status of each, with the g sensitivity.

### MINOR-7: the Readings table is incomplete (claim l.78-84)
- Missing rows:
  - Yoo 1.98e5 held: F 0.0175, D 0.0022, dialectic.
  - Sourced field N_e rows (b)-(d): F of about 1.00, rhetoric.
- Both are in R4-RHclose l.74-82 and absent from the claim file and the MAJOR-2 table. Neither changes the field.
- **Fix:** add both rows.

### MINOR-8: wrong ratio (claim l.12, l.80; R4-RHclose l.160)
"0.697, 2.25x the 0.30 edge": 0.697/0.30 = 2.32. The ratio 2.25 belongs to 0.676 (`raw/rhclose.out` l.74). **Fix:** use "2.32x (6.3 My: 2.25x)".

### MINOR-9: wrong exclusion ground for quote 1 (claim l.12; versions.md l.33)
- The claim file excludes the Feb blog line as "not answerable to HL under N2b (versions ledger SC)". But SC (X1 l.47) says a slip corrected in a later, separate source "is scored on the version quoted, with the note 'corrected in X'". SC does not exclude it.
- The valid ground is RH2: quote 1 is tagged rhetoric (l.32, RH-10). However, RH-10 (slips.md l.69) quotes only the first sentence. "The one is far too weak … the second is flat-out wrong" has no tag.
- **Fix:** cite RH2 as the ground, extend RH-10 to cover the second sentence, and keep "revised in HL" as a versions note.

### MINOR-10: B's direction is mis-signed in D-21 (DECISIONS.md l.37, l.59, l.98)
- The record says "Two results moved in Day's favour … Both reverts remove a Day-favourable value." For B, the reverted value is `non-sequitur`, which is against Day.
- The Day-favourable move (pending to holds) was superseded four minutes later by D-15 (3f881b0). The B revert therefore removed a value unfavourable to Day.
- The owner's chosen action does not depend on direction, so the evidence question is unaffected. The premise as put to the owner is wrong for B.
- **Fix:** the lead records the correction and tells the owner.

### NOTE-11: an asymmetry, for the lead
The cleanest internal contradiction on record is on the F reading: HL's own model on HL's own 6.5 My and HL's own census gives 0.70, "substantially fills" by Q152. RH6 tags exactly that reading rhetoric. The readings it keeps dialectic are the ones where N2b is weakest (MAJOR-2). This is the rule working as designed, but it should be visible when the lead rules (D-24).

### NOTE-12: no aggregation rule
X1 does not say how one internal field combines Statement quotes with different verdicts. Here quote 2 holds and Q157 depends on the reading. State the rule.

### NOTE-13: context bearing on B's title
HLf l.611-619, immediately before Q157, reads: "a neutral substitution, having no fitness effect, contributes exactly zero to an adaptive gap by definition. The two arguments do not overlap." The neutral-channel claim is offered as independent of the adaptive shortfall. This matters to how B's title is read. It does not change the internal field.

### NOTE-14: double rounding
F at 2 My = 0.02547. "0.026" in R4-RHclose l.16, l.79, l.119 and in R4-B2 l.37 comes from rounding 0.0255 again. At three decimals it is 0.025.

## 3. The lead's stated suspicion (brief, l.61-63)
- **Do the blog sentence and the abstract sentence carry the field?** Neither does.
  - The blog line is rhetoric. Only its first sentence is in RH-10, and it is excluded on a misapplied SC ground (MINOR-9).
  - The abstract sentence holds as B2 on every reading.
- **What does set the field?** A third quote, Q157, whose Statement status is still "candidate", read through a fourth, Q158, which is outside the Statement (MAJOR-3). The record does not show the field being chosen from the two quotes the suspicion names. The open problem lies elsewhere: in how readings were mapped to verdicts (BLOCKER-1, MAJOR-2).

## 4. What the evidence on record carries, per reading

| Reading | Closeness to literal (D-15) | Tag | Value on record | Derivation on record | Carried by the evidence? |
|---|---|---|---|---|---|
| S, current size | literally true (B2) | dialectic | non-sequitur "at lineage level" | none; registration and RHclose review say holds | **holds, scoped to B2** (BLOCKER-1) |
| 2 My window | F 0.025, inside the literal band | dialectic | non-sequitur | ancestral-fill quotes (wrong premise) | non-sequitur via the defined lineage duration, after the premise fix and weighing HLf l.583-584 (MINOR-5) |
| D, 6.5 My | 0.256, inside the 3x edge only | dialectic | non-sequitur | carried over from R4-B2 | N2b not shown; possibly an extended reading (MAJOR-2, MINOR-6) |
| Takahata 1e5 | 0.281, depends on g | dialectic | non-sequitur | carried over | N2b not shown; external input (MAJOR-2, MINOR-6) |
| F, 6.5 My | 0.697, 2.32x the edge | rhetoric | holds scoped to B2, plus RH3 | yes | yes |
| "never fills" = never reaches k = μ | true at HL's input | dialectic | not recorded | none | open (MINOR-4) |

**Bottom line.** On the record as it stands, the evidence does **not** carry `verdicts.internal` = `non-sequitur` under rules C and RD:
- The D-15 test ("closest to literally true, best supported") puts S at or near the top.
- The record's only derivations for S give `holds` scoped to B2.
- The non-sequitur readings that are derived either need a premise fix (2 My) or have no excluding text (D, 1e5).

The record does not license a bare `holds` either. Moving off `pending` needs BLOCKER-1 and MAJOR-2 resolved, then the lead's ranking of S against 2 My under D-15, written down.

## 5. Counts and wrong numbers
**1 BLOCKER, 2 MAJOR, 7 MINOR, 4 NOTE.**

Wrong numbers (old -> right):
- "0.697, 2.25x the edge" -> 2.32x (claim l.12, l.80; R4-RHclose l.160).
- 2 My F "0.026" -> 0.025 (0.02547) (R4-RHclose l.16, l.79, l.119; R4-B2 l.37).
