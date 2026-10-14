# R4 B internal: readings, per-reading N2b derivations and the proposed field comment (fix pass, O5, D-21)

Status: **fix pass, 2026-10-14** (Paperclip EVO-70, analyst). The field `verdicts.internal` of claim B **stays `pending`**. This file carries what the move will use: the Readings table, one N2b derivation per reading, and the field comment. The move itself happens at integration, after a fresh reviewer has checked the lead's rulings B-R4 and B-R5 (D-24).

- Reviews answered: `research/checks/REVIEW-R4-B-internal-correctness-2.md` (124ce23), `-steelman-day.md` (f5104a4), `-steelman-critic.md` (f66ce55).
- Binding rulings: `research/checks/briefs/O5-reviews-reviewer.md`, addendum Part 1, B-R1 to B-R10 (35b196a). Where I disagree with one, I say so in "Points for the fresh reviewer". I have not departed from any of them.
- Prior write-ups this rests on: `R4-B2.md` (Rule N), `R4-RHclose.md` Part 2 and its review resolution. This file adds no registered prediction and changes none.
- **Source text.** `sources/raw/b-steelday-2026-10-13/hl.txt` (gitignored; fetched by the Day-side reviewer from Zenodo 22129121). Its sha256 is `3182a5b6cd3a8ac822017d6d7f509c234ab147b334546d62f88623142d9dbfe2`, the hash of the audit's local text `sources/raw/day/zenodo-22129121.txt`. So **"HL l.N" below is the line numbering the claim file and `quotes-day.md` use.** PDF sha256 `66aa8be6…55719bf` (matches `bib-day.md`). I read it with `grep` and `sed`. Every quote below was checked against it on 2026-10-14.
- **Numbers.** Kimura (1955) series for an empty start, F(x) = 1 + Σ(−1)^i(2i+1)e^{−i(i+1)x/4}, D(x) = (1/x)∫₀ˣF, x = T/(g N_e), N_e = 4·1e5/7 = 57,143, g = 25 y unless stated. I re-ran it as a local check of under a second (stdlib, `research/.venv/bin/python -I -c`, not committed). It matches both reviewers to all digits shown: F 0.69703 / 0.67594 / 0.02547 / 0.28077 / 0.44703 (g 20) / 0.18686 (g 29) / 0.01749, D 0.25564 / 0.24196 / 0.00337 / 0.06487 / 0.12497 / 0.03790 / 0.00218. **Post hoc and new in this file:** only the shortfall factors 1/F and 1/D in the C row (trivial division of recorded values).

## 1. What is scored, and on which quote (B-R2, B-R7 aggregation rule)

**Aggregation rule (B-R7, answering correctness NOTE-12).** An internal field takes the governing reading of the Statement quote that asserts the node's own claim. The node's other Statement quotes are reported with their own verdicts.

| Statement quote | Status | Tag | Internal | Ground |
|---|---|---|---|---|
| 1. Blog 2026-02-04 ¶60, both sentences ("There is absolutely nothing … The one is far too weak … and the second is flat-out wrong") | Statement | rhetoric (RH-10; the second sentence to be added to RH-10, B-R7) | **no verdict** (RH2) | Excluded on **RH2**, not SC (correctness MINOR-9). SC would score a dialectic slip "on the version quoted". "Revised in HL" (HL l.425-428, Q155) stays as a versions note. Day-side F3 alternative, recorded: if the second sentence were dialectic it would be scored on its Feb basis (Q39 → B3a, internal `holds (algebra)`, fidelity `misread`, external `contradicted`, retracted in B3g). |
| 2. HL abstract, "The domain of k = μ is confined to demographic conditions that no non-endangered species is capable of meeting." (HL l.25-27) | Statement | dialectic | `holds` **at B2**, not re-scored here | This is B2's own quote. Copying B2's verdict into the parent would score a narrower claim than B's (critic MINOR-4). |
| 3. Q157, HL l.453-456 | **Statement quote by lead ruling B-R2, 2026-10-13** (was "Candidate") | reading-dependent (section 2) | **sets the field** | The only Statement quote that asserts B's own claim, the lineage-level closure of the neutral channel. |
| Q158, HL l.464-467 ("the pipe was nearly empty") | **not** a Statement quote (B-R2) | n/a | cannot set the field | Context only. No verdict in this file is set from its wording. |

Q157 verbatim (HL l.453-456): "And now the neutral channel closes on the same window for an entirely independent reason. The adaptive substitutions cannot be paid for; the neutral substitutions cannot be finished, because the pipe that would finish them never fills. Both the priced channel and the free channel shut inside the same lineage duration."

**Literal band on Q157's own words (B-R2; correctness MAJOR-3).** `R4-RHclose.md` l.70 registered one band, F ≤ 0.10, for the pooled phrase "never fills / nearly empty". Here it is applied to "never fills" alone. Under the **degree sense** of "fills", "never fills" claims at most a negligible fill, a claim at least as strong as "nearly empty". A band of F ≤ 0.10 (3x edge 0.30) is therefore no stricter on Q157 than on Q158, and it errs in Day's favour if anything. Under the **completion sense** (row C) the band does not apply: the clause is literal, and its truth condition is F short of 1.

## 2. Readings table (replaces claim file l.78-84 at integration)

Window 6.5 My (HL's "lineage duration", l.247-249) unless stated; HL's own variance N_e 57,143 unless stated. "Governing" = sets the field under D-15 and B-R5.

| # | Reading of Q157 | Value | Tag | N2b derivation (section 3) | Verdict | Governing? |
|---|---|---|---|---|---|---|
| **C** | **Completion:** "never fills" = never reaches the k = μ steady state ("filled across its support", l.432) | F 0.697 (6.3 My 0.676; 2 My 0.025; 1e5 0.281; Yoo 0.0175), all < 1; the clause is literally true in every window on HL's input | dialectic (B-R1) | **derived**: C1-C4 | **non-sequitur** (N2b; N2a supporting) | **yes** (B-R5) |
| F | Degree: end-of-window flux F at HL's lineage duration | 0.697, **2.32x** the 0.30 edge (6.3 My: 0.676, 2.25x) | rhetoric (RH6) | not needed; rhetoric is not literal-fact-checked (RH2) | **n/a** (core at B2 `holds`; lineage conclusion: "no dialectical support offered", RH3) (B-R6) | no |
| 2My | Degree, on H8's 2 My window (HL l.416 calls it "the entire lineage") | F 0.025 (D 0.003) | dialectic | **derived**: the excluded premise is the **window**. HL l.252-253: "The objection is valid, the correction triples the ceiling", adopting 6.5 My (l.247-249), which is the defined term Q157 uses. HL's own contrary usage is recorded: l.416-417, "the one that reached thirty-five percent fill across two million years even when granted the entire lineage". That ambiguity is HL's, not the audit's (critic NOTE-10). | non-sequitur | **no**: needs a window its source gave up (B-R3) |
| D | Delivered share (1/T)∫F as the measure of "fills" | 0.256 (6.3 My 0.242) | dialectic (inside the 3x edge) | **N2b not shown.** No cited HL text says more than 30% of μT was delivered. HL fixes "fill" as F (l.361: "The exponent also fixes what the 'fill' means"), so D is a **different object**: an extended reading under RD l.202. Its measure is a **cross-document measure (Q34, Z22903977, 2026-09-22)**, from a later paper. | no verdict derived (Day-side F1: at most a ledgered overstatement under R1; critic side: non-sequitur via partial-load texts, not shown for the empty-start D) | **no** (extended, cross-document) |
| 1e5 | Takahata N_e = 1e5 held for the whole lineage | F 0.281 at g 25; **0.447 at g 20 (1.49x the edge, rhetoric); 0.187 at g 29** | dialectic at g 25 and 29, rhetoric at g 20 | **N2b not shown.** External input: "Takahata" does not occur in HL (grep count 0). HL argues for the variance N_e (l.101-118). | none derived | **no** (external input, N1) |
| Yoo | Yoo HCB ancestral N_e 1.98e5 held (a pre-split N_e) | F 0.0175, D 0.0022 | dialectic | **N2b not shown.** External input, not HL's. | none derived | **no** (external input, N1) |
| fieldNe | Sourced field N_e, R4-RHclose rows (b)-(d): 1e4, 1.62e4, Takahata two-epoch | F ≥ 0.999, D 0.74-0.85 | rhetoric (degree sense); under C the clause is false at these inputs | not an internal question: whether HL's premise N_e is right is N1, external (B1c, B4a) | n/a (internal) | **no** (external inputs) |
| S | Current size ("near end"), a reading of **Q158's** framing, restating B2 | n/a | dialectic | derivation as a reading of Q158: it restates B2, which HL keeps (abstract l.24-27; l.353-354, "The channel is not slow, it is empty") | `holds`, scoped to B2 | **no**: not a reading of Q157's sentence, which uses the defined term "inside the same lineage duration" (B-R2, B-R4) |

Considered and **not admitted** as a plausible reading, recorded for the fresh reviewer (section 5, P1):

| # | Reading of Q157 | Value | Tag | Inference | Verdict | Status |
|---|---|---|---|---|---|---|
| C′ | Completion, weak inference: "cannot be finished" = not all of μT completes; "closes / shut" = falls below k = μ | as C | dialectic | the inference would follow from F < 1 and HL's own k(T) = μ·F(T) | would be `holds` | judged implausible on HL's own usage (C2, C3), so not a governing candidate; the B-R9 overturn test |

## 3. N2b derivation for the governing reading C (B-R3, B-R5)

**C0. The sense of "fills" is HL's own.** HL uses "fill" in the completion sense in its own statement of the argument: l.271, "The correct interpretation is narrower: the pipeline cannot fill"; l.274-276, "A population reaches the k = μ flux only after it has spent enough time to load every one of its pipes from empty … not 'what is the delivery rate of a full pipe' but 'is this pipe full'"; l.432, "k = μ holds only once the fixation-time distribution has filled across its support"; l.438, "the only census population that fills the pipe in time". HL also uses the degree sense (l.363, "the pipe substantially fills"; l.416, "thirty-five percent fill"). Both are HL's. C is not an import. Operationally, "filled" = F close to 1. The clause is true on HL's input for any threshold between 0.70 and 0.999 (post hoc; no threshold was registered, and none is needed at these values).

**C1. The clause is true; the field turns on the inference.** On every window and N_e in HL's own text, F < 1 (0.697 at 6.5 My, 0.676 at 6.3 My, 0.025 at 2 My). The inference Q157 draws from it is "the neutral substitutions cannot be finished", "the neutral channel closes", "both the priced channel and the free channel shut inside the same lineage duration".

**C2. What "closed / shut" means in HL's own sentence pair.** Q157 asserts that both channels "shut" in parallel. The paragraph immediately before defines what "closed" means for the first channel, HL l.445-448: "The adaptive channel … was already closed by Haldane's dilemma …: selection can provide only an insignificant trickle of adaptive substitutions over many generation, orders of magnitude short of what the functional genome requires." HL's own vocabulary also opposes "empty" to "slow": l.354, "The channel is not slow, it is empty"; l.209, "The window is not narrow. It is empty." So the conclusion needs the premise **P\*: the neutral channel, partly filled, delivers an insignificant trickle, orders of magnitude short of k = μ.**

**C3. HL's own text excludes P\* at HL's own inputs and window.**
- HL's own model, l.287-291: "k(T) = μ · F(T) … Before then, k is μ cut down by however little of the distribution has yet come due." At HL's own N_e and its accepted 6.5 My, k(T) = 0.697 μ at the end of the window, a shortfall of **1.43x** (post hoc). The delivered share is 0.256, a shortfall of **3.9x** (post hoc). At 6.3 My the figures are 1.48x and 4.1x. Neither is "orders of magnitude". (This is also N2a: HL's own equation gives another value.)
- HL on hominids specifically, l.363-366 (Q153): "Grant the ancestral hominids their best case … even the generous linear bound T/4Nₑ stands at about thirty-five percent — a partly-loaded pipe, the near-ceiling regime the small population occupies"; l.419: "a partly-filled pipe inherited from a lower-census past"; l.439-441 (Q156): "reading a rate that was loaded, at least partially, under population conditions that ended in the Holocene".
- HL on what a partly loaded pipe does, l.355-356 (Q151): "drainage: the completions of mutations that entered the pipe long ago". The context is mice and fruit flies (correctness MAJOR-2), so it is cited for the mechanism, not for the human case. The human case rests on l.363-366 and l.419.
- HL l.268-270: "'Nothing finishes in the species lifetime' is simply wrong as a claim about throughput, and the drift limit does not depend on it." HL itself separates "finishing" from "filling". Q157's "cannot be finished, because … never fills" puts back the link HL set aside.

**C4. Verdict on C.** The conclusion needs P\*, and HL's own text and equation exclude P\*: N2b within HL, with N2a supporting (critic MAJOR-1 adds N2d: stronger than the premises support; that is not needed). **`non-sequitur`.** Shortfalls of orders of magnitude appear only on readings that are not governing: 2 My (D 297x short) and Yoo (459x). Takahata 1e5 is 15x short on D, about one order.

This lands on the value superseded on 2026-10-13 on a **different basis**. The old basis, the pooled "nearly empty" band with one R4-B2 derivation carried to four rows, does not survive the reviews and is not restated here (B-R5).

## 4. Proposed field comment (for integration only, after the fresh-reviewer check)

```yaml
  internal: non-sequitur   # reading-dependent: set on Q157 (B Statement quote by lead ruling B-R2, 2026-10-13) under its governing reading C (D-15, B-R5): 'never fills' = never reaches the k = mu steady state (HL l.271-276, l.432); clause literally true on HL inputs in every window (F 0.697 at 6.5 My; 0.676 at 6.3 My; 0.025 at 2 My) -> dialectic -> non-sequitur (N2b within HL: 'closes'/'shut' needs a partly filled pipe to deliver 'an insignificant trickle ... orders of magnitude short', HL's own sense of 'closed', l.445-448; HL's own k(T) = mu F(T), l.287-291, gives 0.70 mu (delivered 0.26), and HL calls the hominid pipe 'partly-loaded' l.366, 'partly-filled' l.419, 'loaded, at least partially' l.440). Other readings (R4-B-internal.md section 2): F degree sense 0.697 (2.32x the 0.30 edge) rhetoric -> n/a (core B2 holds; lineage conclusion 'no dialectical support offered', RH3); 2 My window F 0.025 dialectic -> non-sequitur, not governing (needs the window HL gave up, l.252; HL's own l.416 'entire lineage' recorded); D 0.256 (cross-document measure, Q34), Takahata 1e5 (F 0.281; 0.447 at g 20, 0.187 at g 29), Yoo 1.98e5 (0.0175): N2b not shown, not governing (extended / external, N1); S (Q158 'near end') holds scoped to B2, not governing (B-R2, B-R4). Quote 1 rhetoric (RH2, RH-10): no verdict; quote 2 is B2's (holds at B2). Against this value, stated openly: the cleanest internal contradiction on record is on reading F, which RH6 tags rhetoric and so releases, while the readings left dialectic are those where N2b was weakest (correctness NOTE-11); and N2b penalises an author for his own concessions: drainage, partial load, 'substantially fills' (critic NOTE-9). Basis: lead rulings B-R1..B-R10 (35b196a); fresh-reviewer check <commit>.
```

Until then the field reads `pending` with the D-21 comment. The superseded comment (claim l.12) has no source to restate: its "D, 1e5, S and 2 My ... -> non-sequitur" mapping and its "recorded alongside: ... holds" do not survive (B-R3, B-R6). Keep it only as a dated superseded line.

## 5. Points for the fresh reviewer (B-R9 asks for B-R4, then B-R5)

- **P1 (B-R9, first condition: the reading C′).** The strongest Day-side reply to B-R5 that I can build from Q157's own words: under the completion sense, "the pipe that would finish them" is the full pipe, so "cannot be finished" = the k = μ complement cannot all complete, and "closes" = k = μ is not available, which is HL's domain claim (l.430-432). That inference follows from F < 1. I do not admit C′ as plausible, for three reasons: (i) HL defines "closed" two lines earlier as "an insignificant trickle … orders of magnitude short" (l.445-448), and Q157 asserts that the two channels "shut" in parallel; (ii) HL opposes "empty" to "slow" and "narrow" (l.354, l.209), so its closure words are not degree words; (iii) the lines after Q157 present it as a calculation with a hard result (l.456-464). If the fresh reviewer finds C′ plausible, D-15 would favour it ("closest to literally true") and B-R5 would be overturned. This is the point to attack.
- **P2 (B-R4).** I agree with B-R4. "Inside the same lineage duration" is HL's defined term (l.247-249). S drops it. The Day-side steelman's own cost item 3 concedes that S "fits Q157 less well than Q158".
- **P3 (B-R8, flagged, not applied).** Under B-R6 the F row gives `n/a`, not `non-sequitur`. "Same value under every derived reading" is therefore exact only for the **dialectic** readings of Q157 (C and 2 My). The bookkeeping task should decide whether a field with the readings {non-sequitur, n/a (rhetoric)} still counts as reading-dependent. I change no count.

## Who this helps

- **Critic side.** The field's proposed value is `non-sequitur` on a reading under which Day's clause is **true**: the error is the inference "closes / shut", not the pipe arithmetic. HL's own equation and its hominid passages supply the refutation. The Day-favourable "recorded alongside: holds" is gone (B-R6). D, 1e5 and Yoo, which the old comment counted as carrying the field, are not needed.
- **Day side.** This credit is as prominent as the critic side's.
  - The clause "never fills" is **literally true** on HL's inputs in every window. Day's mechanics stand: k(T) = μF(T) < μ from any start that is not full.
  - B2 `holds` and the current-size confinement (S) `holds`.
  - The old basis, "nearly empty" scored as near-literal on four readings, is withdrawn as underived. Three of the four rows the superseded comment listed (D, 1e5, S) now carry **no** non-sequitur.
  - The error is narrow (critic NOTE-8). It says nothing on whether partial delivery suffices for the observed divergence. That question is external and pending (B1c, B4a).
  - Day's later text (B1d, blog 2026-10-01) grants a full CHLCA pipe (critic NOTE-7). That is cross-document and moves nothing here, but it shows the empty-start premise is not one Day holds.
- **Both / the audit's own errors.**
  - One N2b derivation, written for one reading in R4-B2, was carried to four readings (all three reviews).
  - S was given "non-sequitur at lineage level" with no derivation, against the registration's own `rhclose.py` l.83-84 (correctness BLOCKER-1).
  - The field rested on a "Candidate" quote, read through a quote outside the Statement (correctness MAJOR-3).
  - Wrong numbers: "0.697, 2.25x" should be 2.32x; F at 2 My "0.026" should be 0.025 (double rounding).
  - Quote 1 was excluded on SC instead of RH2.
  - The D-21 question mis-signed B's direction. The lead has already corrected this in `DECISIONS.md` l.106.

## Review resolution (fix pass, 2026-10-14)

No verdict value changes. Everything below that touches a shared file is a **proposal for integration** (section 6).

### Correctness review 2 (`REVIEW-R4-B-internal-correctness-2.md`)
- **BLOCKER-1** (S mapped to non-sequitur with no derivation). **Accepted in part, under B-R4.**
  - Done, following the reviewer's option (b): S is mapped to `holds`, scoped to B2, and "non-sequitur at lineage level" is removed.
  - Not accepted: the reviewer's ranking of S "at or near the top" under D-15. Per B-R4, S reads Q158's framing, not Q157's sentence, so it is not a candidate for Q157's field. The D-15 ranking is recorded in section 2: C governs, and S, 2 My, D, 1e5 and Yoo do not, each with its reason.
  - Why the RHclose fix pass admitted S: as a reading of the pooled Q157/Q158 phrase, before B-R2 separated the quotes.
- **MAJOR-2** (one N2b derivation carried to four readings). **Accepted.** Section 2 gives each row its own derivation or "N2b not shown":
  - C: section 3.
  - 2 My: the window premise.
  - D, 1e5 and Yoo: N2b not shown. The reviewer is right that Q140, Q151, Q152 and Q156 do not exclude an empty start for the human lineage.
  - C does not need that exclusion. It needs only P\* ("closed" = orders of magnitude short) to be excluded, and HL's own k(T) = μF(T) and l.363-366 do that.
- **MAJOR-3** (Candidate Statement; Q158 outside the Statement). **Accepted.**
  - Q157 is adopted by B-R2 (2026-10-13). Q158 is not adopted, and no verdict is set from its wording.
  - The band is applied to Q157's own words, justified in section 1.
  - Claim l.29 and l.32: proposal 6a.
- **MINOR-4** (completion reading missing). **Accepted.** Row C added, and it governs (B-R1, B-R5). The reviewer's N2a test against HL's own F (0.70, "substantially fills") is used in C3.
- **MINOR-5** (2 My: wrong excluded premise). **Accepted.** The premise is now the window (l.247-253). HL's contrary l.416-417 is quoted in the row.
- **MINOR-6** (D and 1e5 status). **Accepted.** D is extended (a different object, l.361) and cross-document (Q34). 1e5 is an external input (N1) and not governing. Its g sensitivity is recorded: F 0.447 at g 20 (rhetoric), 0.187 at g 29.
- **MINOR-7** (rows missing). **Accepted.** Yoo and the field-N_e rows are added.
- **MINOR-8** (2.32x). **Accepted.** Proposal 6e.
- **MINOR-9** (quote 1 on SC). **Accepted.** The ground is RH2. RH-10 is to cover the second sentence, with "revised in HL" kept as a versions note: proposals 6b and 6c.
- **MINOR-10** (D-21 direction). **Accepted. Already done by the lead** (`DECISIONS.md` l.106; brief Part 3). No action here.
- NOTE-11 is in the field comment (B-R10). NOTE-12: the aggregation rule is stated in section 1. NOTE-13 (HL l.448-452, "The two arguments do not overlap") is recorded; it bears on B's title, not on the field. NOTE-14: 0.025, proposal 6e.

### Steelman, Day side (`REVIEW-R4-B-internal-steelman-day.md`)
- **F1 BLOCKER** (non-sequitur derived once, asserted four times). **Accepted.** Section 2 follows the reviewer's per-reading table, with these differences:
  - S is `holds` but is recorded as a Q158 reading (B-R4).
  - D is "N2b not shown". The reviewer's "ledgered overstatement, no flip" is recorded as the Day-side position in the row.
  - C is added, and it governs (B-R5).
- **F2 MAJOR** (S governs, giving `holds`). **Not accepted, by ruling B-R4.**
  - Recorded as the Day side's position: under D-15, S is literally true (it is B2) and best supported, and "lineage level" is a wider claim that RD l.202 bars.
  - The ruling's answer: the lineage-level claim is Q157's own words ("inside the same lineage duration", a defined term). It is not a wider claim added by the scorer. A reading that drops that clause reads a different statement.
  - I agree with the ruling (P2). The fresh reviewer is asked to attack it first (B-R9).
- **F3 MAJOR** (the field turned on a third quote). **Accepted.** Section 1 states that the field rests on Q157 alone, and why S1 and RH3 force that choice (critic MINOR-4 makes the same point).
  - (a) Accepted as proposal 6b: RH-10 is extended to the second sentence.
  - The Day side's "internal on its own Feb basis" is recorded as the dialectic alternative. Under the RH2 tag that B-R7 confirms, quote 1 carries no verdict.
- **F4 MINOR** (Q157 status stated two ways). **Accepted.** Q157 was adopted by lead ruling B-R2 on 2026-10-13 (35b196a). l.29 and l.32 are to be brought into line: proposal 6a.
- **F5 MINOR** (1e5 cannot govern). **Accepted.** The row is kept, marked "not governing (external input, N1)", and removed from the readings said to carry the field.
- F6 is done by the lead (`DECISIONS.md` l.106). F7: a dated pointer line in `R4-RHclose.md` l.117, proposal 6e. The "What this costs Day" items 1-7 are carried in Who this helps and in rows F, 2 My and S.

### Steelman, critic side (`REVIEW-R4-B-internal-steelman-critic.md`)
- **MAJOR-1** (tag keyed to Q158; every reading of Q157 is non-sequitur). **Accepted in part.**
  - Accepted: the completion reading is added and governs (B-R1, B-R5). Q157 is scored on its own words. "Recorded alongside: holds" is dropped (B-R6).
  - Not accepted: "non-sequitur on F, D, 1e5, 2 My and the completion reading alike". D, 1e5 and Yoo have N2b not shown (B-R3). F remains a degree-sense reading of **Q157's** "never fills", at 2.32x the edge, so it is rhetoric and gives `n/a` (B-R5, B-R6). It is not moved to Q158.
- **MAJOR-2** (RH3 extracts the wrong core; the core is the lineage closure). **Not accepted, by ruling B-R6.** Under rhetoric the field is `n/a`, with the core at B2 `holds` and the lineage conclusion marked "no dialectical support offered". That is the reviewer's own stated fallback ("or at worst `n/a`").
  - The self-classification evidence (HL l.456-464: "There is no algebra error to defend …") is used in support of the **dialectic** tag of row C (P1 iii), where it does bear.
  - The steelmen conflict here. The lead's ruling is applied, not chosen by me.
- **MINOR-3** (like-for-like with C7: `n/a`). **Accepted** (B-R6).
- **MINOR-4** (answer the lead's suspicion on the record). **Accepted.** Section 1, one line per quote.
- **MINOR-5** (2.32x). **Accepted.**
- **MINOR-6** (D is a later paper's measure). **Accepted.** D is labelled "cross-document measure (Q34, Z22903977)". It is not listed first and does not govern.
- NOTE-7 is in Who this helps (Day side). NOTE-8 is in Who this helps. NOTE-9 is in the field comment (B-R10). NOTE-10 is in the 2 My row. NOTE-11 (quote 1 escapes) is recorded: critics get no internal verdict on "flat-out wrong", and HL's "The identity is not false" (l.430) is a versions entry.

### Steelman conflicts without a ruling
None. Every conflict between the two steelmen falls under B-R4 (S), B-R5 (governing reading) or B-R6 (rhetoric value).

## 6. Proposals for integration (operator, one at a time; none applied here)

- **6a. Claim file `B-neutral-theory-cannot-rescue.md`.**
  - l.29: replace "**Candidate Statement**; rule RH tag reading-dependent" with "Statement quote (lead ruling B-R2, 2026-10-13, 35b196a); RH tag reading-dependent". Q158 is not added.
  - l.32: "quotes 2-3 dialectic" becomes "quote 2 dialectic; quote 3 (Q157) reading-dependent (RH-26)".
  - l.78-85: the Readings table from section 2, and the R4 paragraph rewritten to match.
  - l.12-13: **only after the fresh-reviewer check**, the section 4 comment. Until then, `pending`.
- **6b. `ledgers/slips.md`.**
  - RH-10 (l.69): quote both sentences.
  - RH-26 (l.85) and the l.101 row: the tag is per reading of Q157 (C dialectic, F rhetoric, 2 My dialectic); remove "S" and "D … dialectic" as tags of Q157; Q158 is noted as context.
  - The core stays B2 per B-R6.
- **6c. `ledgers/versions.md` l.33.** Change the ground from "not answerable to HL (N2b) … SC" to "excluded as rhetoric (RH2); revised in HL (versions note)".
- **6d. Argmap.** One defeater for the C reading (critic side: HL's own k = μF(T) and its partial-load text against "closes / shut"). One for the Day side: the clause is literally true, and S/B2 holds. Note the reading dependence.
- **6e. Write-ups, number corrections.**
  - `R4-RHclose.md` l.16, l.79, l.119 and `R4-B2.md` l.37: 0.026 → 0.025. P6 at l.97 is registered wording and stays.
  - `R4-RHclose.md` l.160: "rhetoric (2.32x the edge; 6.3 My: 2.25x)".
  - `R4-RHclose.md` l.117: add a dated pointer: "superseded: D-15 (2026-10-11), D-21 (2026-10-13); see R4-B-internal.md".
- **6f. Counts (B-R8).** No change in this pass. One bookkeeping task after integration (P3).
