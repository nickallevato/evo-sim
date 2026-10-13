# Steelman review (Day side) of claim B, internal field (O5 2/6, D-21)

**This review argues Day's side as hard as it can be argued honestly. It does not set a verdict.** Where it conflicts with the critic-side steelman, the lead rules (D-24).

- Reviewer: fresh reviewer instance (Paperclip EVO-60), 2026-10-13. It authored none of R4-B2, R4-RHclose, the O5 revert or the other five O5 reviews.
- Disclosure: the subject lines of commits 124ce23 (correctness-2) and f66ce55 (steelman-critic) were visible in `git log` at session start. Neither file was opened. Where a finding below overlaps those subject lines, it was derived independently from the files cited.
- Brief: `research/checks/briefs/O5-reviews-reviewer.md` (f9e254d). Question: does the evidence on record carry B internal to `non-sequitur` under rule C, rule RD and the stated scoping?
- Files read (by line range): claim `docs/research/claims/B-neutral-theory-cannot-rescue.md` (all 91 lines); `research/checks/results/R4-B2.md` l.13-57; `R4-RHclose.md` l.14-26, l.54-198; `R4-X1-verdict-rule.md` l.7-62, l.171-202; `ledgers/slips.md` RH-10, RH-26; `ledgers/versions.md` l.33; `sources/quotes-day.md` Q06, Q07, Q34, Q39, Q140, Q151, Q152, Q155, Q156, Q157, Q158; `DECISIONS.md` D-15, D-21.
- Source text: the local HL copy named in quotes-day (`sources/raw/day/zenodo-22129121.txt`) is no longer on disk. I re-fetched it read-only into `sources/raw/b-steelday-2026-10-13/` (gitignored): Zenodo record 22129121, file `Hard_Limits_Fixation_Drift.pdf`, md5 `4f66a65883c63524837e304c59cf0abc` (matches the Zenodo checksum), sha256 `66aa8be6687e6fb9bf9a82bf07bf5f1eb4006a17c9e645fcfdeda661355719bf`. `pdftotext -layout` gives 467 lines, and the claim file's line numbers match it (Q157 at l.453-456, Q158 at l.466-467, l.249, l.416). All "HL l.N" citations below use that text.
- Recomputation (post hoc, by hand, mine; no script; Kimura 1955 conditional series at p → 0, F(x) = 1 + Σ(−1)^i (2i+1) e^{−i(i+1)x/4}, and D = (1/x)∫₀ˣF): F(4.55) = 0.697, D(4.55) = 0.256, F(1.40) = 0.025. These agree with R4-RHclose. The arithmetic is not in dispute. What is in dispute is the mapping from readings to verdicts.

## Summary for the lead

On the record as it stands, the superseded value `non-sequitur` is **not carried**. The N2b derivation exists for one reading only: fill = flux F over HL's 6.5 My lineage duration (R4-B2 l.25). That is the reading R4-RHclose tags `rhetoric`, which releases it. The derivation was then applied to the four "dialectic" readings without being redone for each. Done for each, it gives non-sequitur on HL's 2 My window (genuinely), `holds` on S and on D, and no derivation on Takahata-1e5. Under rule RD as written (l.198: "most defensible (closest to literally true, best supported)") the governing reading is S. S is literally true by the audit's own B2 verdict, and it needs no premise HL excludes. Its verdict is `holds`, scoped to the current-size confinement. The "non-sequitur at lineage level" given to S in the Readings table scores a wider claim, which RD l.202 bars from setting the field. **What the Day side says the evidence carries: `holds`, scoped to B2 (current size), never displayed bare. The lineage-level shortfall is carried by no scored B quote** (RH3 under F-6.5; not asserted under S). The lead's suspicion is answered in F3: the blog line and the abstract line carry the same internal value, and neither carries non-sequitur. The field turned on a third quote.

## Findings

### F1 BLOCKER: the non-sequitur is derived for one reading and asserted for four
*Attaches to:* claim file l.12 ("D, Takahata N_e = 1e5 held, S and HL's 2 My window make 'nearly empty' literally close -> dialectic -> non-sequitur (R4-B2 Rule N, N2b within HL ...)"), l.81-84; R4-RHclose l.170.

*Evidence.* R4-B2's dialectic branch (l.25) derives N2b for a statement that "makes a checkable claim ('inside the same lineage duration', which HL Table 1 sets at 6.5 My)". It then cites HL text about the flux fill (H7 "short enough to fill", l.363 "the pipe substantially fills, and Kimura's rate is approached"). That is the F-over-6.5-My reading. R4-RHclose MAJOR-3 (l.170) then states "If the owner chooses dialectic: B internal = non-sequitur per R4-B2 Rule N" for every dialectic reading at once. Rule N2b (verdict rule l.54) needs, for each reading, a premise that "the author's own text contradicts or excludes". Done per reading:

| Reading | Premise Q157/Q158 then needs | Does HL's own text exclude it? | Verdict the record supports |
|---|---|---|---|
| F, 6.5 My (registered) | lineage flux fill ≤ ~0.30 | Yes. l.249-252 accepts 6.5 My; l.222 puts the human lineage ceiling at 1e5 = H8's census, so the lineage sits at its X, where l.362-363 says "the pipe substantially fills" (F 0.70) | N2b would be carried, **but the tag is rhetoric** (0.697, 2.25x the edge), so `holds` scoped / RH3 |
| D, delivered share, 6.5 My | delivered share ≤ ~0.30 over the lineage | **No.** HL's own model at HL's own input and window gives D = 0.256 (recomputed above). The texts cited (Q140 drainage, Q151 "short enough to fill", Q152 "substantially fills", Q156 "at least partially") speak of the flux or of a non-zero load. None says more than 30% of μT was delivered | at most a ledgered overstatement ("never" vs 0.26), not N2b. Under R1, correcting "nearly empty" to 0.26 delivered leaves "cannot be finished" standing (74% undelivered): no flip |
| S, current size | today's pipe (4Nₑ at current census) is empty | **No.** HL states the same thing in the body, l.353-357: "The channel is not slow, it is empty. The small number of fixations we observe are just drainage ...". The drainage is conceded in the same breath, so no lineage premise is needed | `holds` (= B2, R4-B2 l.46) |
| 2 My (l.416 "the entire lineage") | the window is 2 My | Yes. l.249-252 adopts the 6.5 My lineage ("The objection is valid, the correction triples the ceiling") | N2b carried: **non-sequitur** |
| Takahata Nₑ = 1e5 held | an Nₑ HL does not use | not derivable as N2b. HL's Nₑ is the variance Nₑ (l.101-118: 57,143 from census 1e5, V_k 5). "Takahata" does not occur in HL (grep count 0) | not derived (see F5) |

So the record carries non-sequitur on one reading (2 My) of the four, plus F-6.5 if that reading were dialectic, which the registered band says it is not.

*Fix.* Replace the single arrow "dialectic -> non-sequitur" with a per-reading N2b derivation in the Readings table (claim l.78-84). Each row should cite the HL line that excludes the premise of that reading, or say that none does. Until then the field cannot be moved to `non-sequitur` on this record.

### F2 MAJOR: under RD as written, the governing reading is S, and S gives `holds` (scoped)
*Attaches to:* claim file l.12, l.83, l.85 ("the dialectic readings D, 1e5, S and 2 My are the closest to literally true"); verdict rule l.198, l.202.

*Evidence.* RD l.198 fixes the field at the reading under which the quoted statement is "most defensible (closest to literally true, **best supported**)". Ranked by both criteria:
- **S** is not merely close to literally true. It is true by the audit's own verdict (B2 `holds`, R4-B2 l.46, on HL abstract l.22-25). It is also the best-supported reading, because it is the paper's own repeated usage: "it is empty" (l.354), and "look at the near end" (l.466), the near end being where today's population feeds the pipe (l.39, l.82-84). No HL text excludes it.
- **2 My** makes "nearly empty" literally true (F 0.025), but only by needing a window HL itself rejected (l.249-252). A reading under which the statement needs a premise its own source excludes is not the "best supported" reading by construction. So it cannot be "most defensible", whatever its closeness to literal truth.
- **D** is close (0.256), and F1 finds no exclusion, but it carries the textual cost noted in "What this costs Day".
- **1e5** rests on an input that is not the author's (F5).

The Readings table (l.83) gives S "non-sequitur at lineage level; B2 itself holds". "Lineage level" is a wider claim than S. RD l.202: "Extended readings (a different object, or a wider claim) are reported with their own verdicts but cannot set the verdict field." The convention applied as written therefore gives `holds` on S. No rule change is needed. The owner's D-15 fix is honoured, and the field happens to land where the F-6.5 rhetoric reading also lands. RD forbids choosing a reading *because* it helps the speaker. It does not forbid the most defensible reading from helping him.

*Fix.* Under the owner's convention the Day side asks that the field carry `holds`, scoped to the current-size confinement (B2, HL abstract l.22-25, l.353-357). Display it with that scope, never bare (R4-RHclose MAJOR-3 is right on that point). Record beside it that the lineage-level shortfall is asserted by no scored B quote under S, and gets RH3 "no dialectical support offered" under F-6.5. Record 2 My → non-sequitur as a non-governing reading.

### F3 MAJOR: the lead's suspicion: the blog line and the abstract line carry one internal value; the field turned on a third quote
*Attaches to:* claim file l.12 (last sentence), l.19-25, l.29, l.32; `ledgers/slips.md` RH-10 (l.69); `ledgers/versions.md` l.33.

*Evidence.* The node was built on two Statement quotes.
- **Quote 2** (HL abstract, l.25-27) is B2's own quote: internal `holds` (R4-B2 l.46).
- **Quote 1** (blog 2026-02-04 ¶60) is tagged rhetoric (claim l.32; RH-10). RH-10, however, quotes only the **first** sentence ("There is absolutely nothing ... origin of species"). The second sentence ("The one is far too weak ... and the second is flat-out wrong") has no tag of its own on record. Read most charitably as part of the same finality wrapper, it is rhetoric and carries no verdict. Read as dialectic, rule SC scores it "on the version quoted, with the note 'corrected in X'" (verdict rule l.47). Its own derivation is in the same post: Q39, ¶29, "k = 2Nμ × 1/(2Nₑ) = μ(N/Nₑ)". From that, "the second [neutral theory] is flat-out wrong" follows, and B3a's internal is `holds (algebra)` (claim l.40). HL l.425-428 softens it later (Q155; versions ledger, SC), and Day retracts the N/Nₑ leg (B3g, `holds`).

So on either tag, quote 1's internal value is *n/a or holds*, and quote 2's is *holds*. The two can carry one field, and neither carries `non-sequitur`. The superseded `non-sequitur` came entirely from **Q157**, which the claim file still labels "**Candidate** Statement" (l.29). R4-B2 l.24 said it "must be added to B's Statement under S1 and RH-tagged before it can be scored". The suspicion is real, but it points at a different quote than the brief names. The field was not set by whichever of the blog and abstract lines suited the result. It was set by the one quote that could yield a negative value, and only through the mapping F1 finds underived.

*Fix.* (a) Tag the second sentence of quote 1 separately in RH-10 and record its internal on its own Feb basis (Q39 → B3a). (b) Say explicitly in l.12 that quotes 1 and 2 carry n/a/holds and holds, so that a reader sees the field rests on Q157 alone.

### F4 MINOR: Q157's status and tag are stated two ways in the same file
*Attaches to:* claim file l.29 vs l.32.

l.29: "Candidate Statement; rule RH tag reading-dependent". l.32 (2026-10-10 pass, never updated): "quotes 2-3 dialectic". Under S1 a node is scored on its Statement quotes. If Q157 is still a candidate, the field rests on quotes 1-2 (F3: n/a and holds). *Fix:* record whether Q157 was admitted, when, and on whose decision. Bring l.32 into line with RH-26 (reading-dependent).

### F5 MINOR: the Takahata-1e5 reading cannot govern an internal field
*Attaches to:* claim file l.82; R4-RHclose l.80, l.162.

Rule C as used in R4-RHclose (l.21) admits "sourced inputs, or inputs the author states in the text at issue", so the row is admissible as a reported reading. But the internal field asks whether HL's conclusion follows from HL's own premises (verdict rule l.9, "author's own inputs"). HL argues explicitly for the variance Nₑ (l.101-118), and with it Nₑ = 57,143, not 1e5. A row that swaps in an external Nₑ tests a contested premise value, which is external under N1 (l.59), not internal consistency. Its F of 0.281 also sits 0.019 under the edge, so it is the least stable "dialectic" call in the table. *Fix:* keep the row, mark it "not governing (external input, N1)", and drop it from the list of readings said to carry `non-sequitur`.

### F6 NOTE: the D-21 question's framing does not fit B
*Attaches to:* `DECISIONS.md` l.37 ("Both reverts remove a Day-favourable value").

On 2026-10-11, B moved from pending to `holds` (RHclose integration) and four minutes later to `non-sequitur` (D-15, l.31). The value the O5 revert removed was the one **against** Day. The question put to the owner ("Two results moved in Day's favour on 2026-10-11") is accurate for the intermediate step only. The decision itself ("Put them back to `pending`") is unaffected. But any public account of the revert should not say it removed a Day-favourable value for B. No action is asked of this review. The note is for the lead.

### F7 NOTE: "Who this helps" in R4-RHclose still credits Day with a move the record no longer has
*Attaches to:* R4-RHclose l.117 ("B internal moves from pending to `holds`").

Superseded twice (D-15, then D-21). This is no harm to Day as such, but a reader comparing that file with the claim file sees a credit and then a reversal, with no pointer between them. *Fix* at integration: a dated pointer line.

## What this costs Day (stated as prominently as the above)

1. **On his own definitions, his peroration is wrong by about 7x.** HL defines "lineage duration" (l.248-249: "Use the lineage duration ... roughly six and a half million years") and "fill" (l.360: "The exponent also fixes what the 'fill' means"; l.272-275; Table 3, "flux/μ"). On those definitions, at HL's own Nₑ, the lineage pipe ends about 70% full (F 0.697), against "never fills" (literal band ≤ 0.10). Day's best case keeps `holds` only because the registered 3x band tags that reading rhetoric. The reading that takes Day at his own word is the one that releases him.
2. **The band decides it.** Under B9's 10x band (R4-RHclose l.17), F-6.5 would be dialectic. N2b would then be well derived: HL accepts the 6.5 My window (l.252), puts the human lineage ceiling at the 1e5 census (l.222), and says a lineage at its X "substantially fills" (l.362-363). That is a clean non-sequitur. The Day-side case rests on the tighter band, which was adopted to answer a review (B9 MAJOR-3), not to help Day, but it helps him here.
3. **S is narrow and fits Q157 less well than Q158.** Q157's "two channels" frame (l.444-452) and "inside the same lineage duration" point at the lineage's human–chimp differences, not at today's census. S is strongest for Q158 ("near end", l.466). And under S, HL concedes that the substitutions we see *are* neutral drainage (l.355-356, abstract l.23-25). The `holds` it gives says nothing about whether drift can account for the lineage count, which is what B's title asserts.
4. **D is a weaker reading of "fills" than its number suggests.** HL itself ties "fill" to the exponent (l.360), that is F. The delivered-share measure is Day's own, but from a later paper (Q34, Z22903977, 2026-09-22). D is admissible as a reading, but HL's own definitions disfavour it.
5. **The lineage conclusion has no dialectical support in HL** under any reading that gives `holds`: RH3 under F, not asserted under S. HL concedes the steady-state throughput (l.267-268), the drainage (abstract) and a partial load (l.366 "partly-loaded", l.419 "partly-filled", l.440 "at least partially").
6. **Quote 1's basis was misread and retracted.** If its second sentence is dialectic, its internal is `holds` on Q39's algebra, but B3a's fidelity is `misread` and its external `contradicted` (claim l.40), and Day withdrew it (B3g).
7. **The 2 My non-sequitur is real.** HL's own l.416-417 ("thirty-five percent fill across two million years even when granted the entire lineage") reuses the window HL had just given up. That reading is non-governing, but it is a genuine internal slip in HL, and it is already in the ledger (R4-B2 l.30).

## Counts
1 BLOCKER (F1), 2 MAJOR (F2, F3), 2 MINOR (F4, F5), 2 NOTE (F6, F7). Post hoc numbers in this file: the three hand recomputations listed in the header (they confirm R4-RHclose and change nothing).
