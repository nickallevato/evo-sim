# Review 1 (correctness): R4 VID-01-score

Reviewer: `reviewer` (Opus), fresh instance, did not author the work and wrote neither steelman.
Task EVO-76, review 1 of 3. Brief: `research/checks/briefs/VID-01-score-reviews-reviewer.md` (`d7d2f7d`).
Under review: `research/checks/results/R4-VID-01-score.md` (registration `e857d1f`, post hoc `31d7f0d`)
and the three claim files it touched. Lead rulings R-1..R-7 (`VID-01-operator.md`) treated as binding
and not reopened; the three-review tier is not re-litigated.

**Counts: 0 BLOCKER, 4 MAJOR, 5 MINOR, 7 NOTE.**
**Findings that would move a verdict field: none.** A4d `internal: holds`, A5h `internal:
arithmetic-error` / `external: pending` and Ge `internal: holds` all survive recomputation. MAJOR-1..3
change what A4d's R4 paragraph may assert about the *governing reading* and its corroboration;
MAJOR-4 changes what the Ge move may claim to have established, not the value it established.

## What I recomputed (everything; nothing relayed)

Method: both PDFs re-hashed; the PDF text **re-extracted independently** by `pdftotext` in three modes
(`-layout`, `-raw`, default) into `/tmp` (scripts outside the fetch directory, hard rule 4; nothing
executed; nothing from `sources/raw/` committed, hard rule 3); every registered token re-searched in
all modes; all 46 GGR quotes machine-checked against the transcript with whitespace normalisation and
caption-chunk timestamps; all arithmetic recomputed in `research/.venv/bin/python -I`.

- **G0 reproduced.** `sha256sum main.pdf` = `22bb4ef8eae7d5c4756987e5418bf26d795ac65e58f36072c393735bdf7a37b2`,
  `addendum.pdf` = `d55e8a030716a0b913082dd04fd5d8967695775814265d348886d314d8df0ce7` — identical to
  `bib-day.md` rows Z23003785 / Z23003785-f2. md5s `7ca0bc6a…` / `a8b66c5e…`, sizes 114,352 / 43,698 B
  and `"modified": "2026-10-04T18:19:52.351587+00:00"` all match `record.json`. **G0 PASS, confirmed.**
- **No false zero.** My own `pdftotext -layout` output is **byte-identical** to the committed
  `main.txt` (both sha256 `0287f54bf381e288f8e8397a15c7b3ab404ad7b109f18d295a41fe35a6dd5b42`) and
  `addendum.txt` (`ac4e70e7…`), so the text under search is faithful to the hash-matched PDF. `-raw`
  and default extraction give the **same counts**. The six lines in `main.txt` and one in
  `addendum.txt` that end in a hyphen are `cross-`, `post-`, `non-`, `60,000-`, `beneficial-`, `17-`,
  `non-` — **no number is hyphenated across a line break**, and no `0.45`, `45 %`, `.45` or `0,45`
  exists in any form. The swallowed-`d` failure mode the brief names is ruled out.
- **Q1/Q4 token table: every row verified.** `turnover` 1 (main:274, "not gross turnover"); `d =`
  case-sensitive 0 in both files, the two case-insensitive addendum hits are `SD = 28.5` / `SD = 720.0`;
  `d=`, `0.45`, `Biocycle`, `450,000`, `450000`, `225,000`, `202,500`, `selective turnover`,
  `d coefficient`, `0.4`, `generation length` all 0; `Bio-Cycle`/`bio-cycle`/`overlapping generations`
  1, same sentence, main:652 (§8.6, heading "Bacteria and Humans Are Incomparable" at main:642);
  `252,000` **8 occurrences in main (lines 25, 280, 488, 517, 524, 599, 654, 676) + 2 in addendum
  (39, 75) = 10, none multiplied**; `coefficient` 2 (main:463, addendum:66); `load` **0** in both
  files; `Bernoulli` exactly 1 (main:55) and it is the only `barrier`; `Bernoullian`, `Averaging`,
  `averaging problem`, `law of large numbers` 0; `coefficient of variation` 1 (addendum:66).
- **§8.6 locator correction verified** (brief item 8). `Appendix` occurs three times in `main.txt`:
  653 (the §8.6 citation), 724 (reference list) and 738 (`Yoo D, et al.`). There is **no Appendix
  heading in 3.0**. The reference at main:723–724 reads "Day V, Athos C. The Human-Derived Fixation
  Rate: An Independent Confirmation of MITTENS. **In Probability Zero, Appendix D.** Castalia AG
  (2025)." So the cited Appendix D is *Probability Zero*'s, as A4d's corrected Weaknesses line says.
- **All quoted passages are exact.** A4d's Statement, both A5h Statement blocks, G1's §8.1 Statement,
  Ge's §1 Bernoulli clause, the §8.6 sentence, the §2 "No recombination overhead" bullet, §6.4's
  "(1 − s)^3,840 …" and §7.1's "The divergence time is 6.3 million years…" each occur **exactly once**
  in the hash-matched text, verbatim as quoted.
- **All 46 GGR quotes** (not only the 19 the brief named) are exact substrings of
  `AqC1ZM4icms.transcript.txt` (vtt sha256 `aacdd0d9a93fa9dc368de9808df5536e7daee45bfc69c975fd44ff2bc72d4c14`,
  as recorded), each in the caption chunk its `t=` names, none ambiguous (no duplicate match).
  Independent of `verify_vid01.py`.
- **Arithmetic, all correct:** 3.2e9 × 1.2e-8 × 100 = 3,840; 10 % → 384; 0.999^384 = 0.68100;
  0.99^384 = 0.021082; e^−384 = 1.7018e−167; 384·log₁₀e = 166.769; 252,000/1,322 = 190.620;
  252,000 × 0.45 = 113,400, /1,322 = 85.779, 205e6/85.779 = 2.3899e6 (2.22× the 1.0754e6);
  450,000 × 0.45 = 202,500. Day's printed 0.02 and 1e−17 are 0.999^3,840 = 0.02145 and
  0.99^3,840 = 1.734e−17, i.e. internally consistent with the *uncorrected* count — A5h's
  `internal: arithmetic-error` is right and untouched.
- **Pre-registration integrity.** `e857d1f` changed one file (the results file, 233 insertions, no
  claim files). The `e857d1f → 31d7f0d` diff of the results file is a **single hunk at line 231 with
  zero deleted lines**: the Predictions, the band tables and the Q1–Q5 criteria are byte-identical to
  what was registered. **No band was widened and no prediction re-scored after the fact.**

---

## MAJOR

### MAJOR-1 — "the host's own narration" uses an attribution the audit itself withdrew
The write-up (Q1 Day-side prediction, the governing-reading paragraph, "Who this helps / For the
critics") and `A4d`'s committed R4 paragraph call the t=01:49:52 line "**the host's own** narration".
That line sits in the **GGR-11 turn**, and `quotes-critics.md` line 806 records that GGR-11 was
re-attributed to `panel` in the EVO-69 fix pass precisely because no name is spoken for that speaker;
its note says only "it is probably the host". I checked the turn: it starts at t=01:47:28
(">> Zach is identifying something weird here with Vox's work") and runs unbroken to t=01:51:34 with
no `>>` marker; the names spoken inside it (Zach, Mattie, Grayson) are all third parties. So the
write-up asserts, as corroboration for a Day-favourable reading, an attribution the audit struck
three days earlier under its own MINOR-1 rule.
**Fix:** in the write-up and in A4d, replace "the host's own narration" with "the narration in the
same segment (GGR-11's turn, t=01:49:52; speaker unnamed, `panel`)".

### MAJOR-2 — the narration is evidence for "(a)/(b)", not for (a); the write-up narrows it
`quotes-critics.md`, GGR-13 note, says verbatim: "The host's own narration in the same segment is
**evidence for (a)/(b) over (c)**". The write-up and A4d both compress this to "agrees with (a)" /
"corroborated by". The transcript cuts the other way on the speaker's referent: the narration is
explicitly *about 3.0* — "**In mittens 3.0**, he completely retracts all of his arguments … He kind of
throws the D coefficient off to the side. It no longer seems nearly as important as it was in in
probability zero" (t=01:49:52) — and GGR-13 is the **direct answer to it**, elicited two chunks later
by "Does that sound right to you, especially Grayson?" (t=01:50:52), to which the reply opens "Yeah, I
I think that he's Yeah, this he's still using the de coefficient in mittens". In context the exchange
reads as the panellist *disagreeing* with the narration about 3.0, which is evidence for (b) as the
intended referent, not for (a).
This does not change the governing reading — RD picks by defensibility, not by intent — but the
corroboration sentence is wrong as written and is doing Day-side work.
**Fix:** restore "(a)/(b) over (c)" and delete the claim that the narration corroborates (a); state
instead that (a) governs on defensibility alone (RD), no corroboration required.

### MAJOR-3 — reading (a) is declared governing without addressing RD's extended-reading clause
`R4-X1-verdict-rule.md` §RD, final bullet: "**Extended readings (a different object, or a wider
claim) are reported with their own verdicts but cannot set the verdict field or the headline tag.**"
Reading (a) is a different object from readings (b) and (c): the pre-3.0 / *Probability Zero* corpus
rather than the paper under discussion. The write-up makes (a) governing and builds a headline on it
("on the governing reading the 'still using d' charge is not about MITTENS 3.0 at all"; "For Day" in
the summary) without citing or distinguishing that bullet — and lead ruling R-3 had declared no winner
among the three. No verdict field is set by the choice (A4d's field is set by the 3.0 text), so this
is not a BLOCKER, but the headline framing in a committed claim file rests on an unaddressed rule.
**Fix:** add one paragraph ruling on the bullet — either that "mittens" is itself the ambiguous object
so (a) is a reading of the quote rather than an extension of it, or that (c) governs among the in-scope
readings with (a) recorded as an extended reading — and make the write-up's and A4d's headline match
whichever is chosen.

### MAJOR-4 — the Ge move tests a *token*, and the audit holds two incompatible glosses of what the token names
Ge `internal` moved `pending` → `holds` on a name search: `Averaging` / `averaging problem` /
`law of large numbers` = 0. That is decisive only if "the Averaging Problem" is a named argument.
The audit's own files gloss it two ways and the write-up never says which it tested:
(i) `G2g-appendix-a-fixation-must-be-sequential.md` line 29 — "(**Averaging Problem: polygenic rescue
impossible**)"; (ii) Ge's own Formal statement, quoting Day's ¶22 in the *same blog post as the Ge
Statement* — "**the math is an average of 12 different populations**".
Under (i) the result is solid and I strengthened it: `polygenic` occurs **0 times** in body and
addendum. Under (ii) the nearest substantive material sits inside the very addendum the search
covered and is not mentioned: the addendum is titled "Per-Population Dispersion and Best-Case
Robustness", reports SD/SEM/range instead of the mean (add:32, 66) and says at §3 (add:83–84) "**These
are not averages. They are the best data point in each category, chosen to be as generous as possible
to the standard model.**" That is 3.0 *answering* an averaging objection, not *deploying* the
Averaging Problem, so I do not think `holds` is wrong — but "the Averaging Problem is **absent
outright** (0 hits)" and "confirmed verbatim and **exhaustively**" overstate what a token search over
a two-gloss term establishes, on the one field this pass moved.
**Fix:** in the write-up's Q4 and in Ge's R4 paragraph, name the gloss being tested, add the
`polygenic` 0-hit as the decisive negative under gloss (i), quote add:83–84 and state in one sentence
why answering an averaging objection is not retaining the Averaging Problem. Keep `internal: holds`.

## MINOR

### MINOR-1 — the standalone-`d` regex result is stated under the wrong case convention
The Q1 table is headed "**Case-insensitive** over `main.txt` … and `addendum.txt`" and then says the
post hoc regex `(^|[^A-Za-z])d([^A-Za-z]|$)` "returns **0 in both files**". Case-*sensitively* that is
right (0 lowercase `d` tokens, which I confirm in all three extraction modes). Case-insensitively it
returns **3** in `main.txt`: `Appendix D)` (653), `Appendix D.` (724), `Yoo D, et al.` (738) — none a
coefficient. A4d's verdict comment inherits the same wording ("0 standalone `d`").
**Fix:** "case-sensitive lowercase `d` token: 0 in both files; case-insensitively 3 in main, all
`Appendix D` citations (653, 724) or an author initial (738), none a coefficient."

### MINOR-2 — what changed in A5h's Responses is mis-described
Q2 says the objection "is added to A5h's Responses, **which until now said 'In support: none
located'**", and the Predictions section says "Responses: 'In support: none located.'". A5h's Responses
already carried an **Against** entry (RE-02 / A2h, the same 10× slip), and the two new entries are
also **Against**; the "In support: none located" line is untouched in the committed file and refers to
support *for Day's claim*, which this objection is not.
**Fix:** "added under **Against**, where only RE-02 / A2h stood; 'In support: none located' is
unchanged."

### MINOR-3 — the second half of the infinitesimal-model answer is never graded
The registration defines answer (ii) as GGR-43/GGR-44 "**with GGR-27..GGR-29 as its second point**",
and the write-up's closing note says the Q3 scoring "turns on their content" — but the Q3 grading table
grades GGR-43/GGR-44 only. I verified from the transcript that GGR-43 (02:13:47), GGR-44 (02:14:07),
"the second thing is that…" (02:14:48) and GGR-27..GGR-29 (02:15:08, 02:15:49) are **one unbroken turn**
with no `>>` between them, so the registration's definition is right and the second point is in scope.
On content it is *adjacent*: dN/dS and heterozygosity varying across one genome answers the
drift-vs-selection dichotomy (GGR-22..GGR-24), not the CV→variance step.
**Fix:** add a third row grading GGR-27..GGR-29 *adjacent* and state that the overall grade for answer
(ii) is unchanged at *on point* (set by its stronger half).

### MINOR-4 — band 4a was applied to one clause of a two-clause Statement without saying so
Registered band 4a reads "… **Ge's Statement true as stated** → `internal` moves". Ge's Statement has
two clauses and only the first was verified; the second ("both of them remain entirely correct") is
routed to `external`, left `pending`, with a `contested` proposal held back. I think the routing is
right (a correctness-of-BB claim is an external question, and G's `external` is already `contested`),
and the claim file records it, but the scoring table calls Q4 "**4a exactly**" without the scope split.
**Fix:** scoring table — "4a, applied to the omission clause (rule S scope); the second clause is an
external question, field unchanged."

### MINOR-5 — "1.03 ± 0.02" cites a figure R4-G1 reports in two senses
Q3 and A4d-adjacent text say "under **free recombination joint fixation is 1.03 ± 0.02 × p²**".
In `R4-G1.md`, 1.03 appears as a **dispersion index** (line 175 "K is Poisson-like (dispersion 1.03)";
line 213 table) while the **measured free-recombination pair ratio at 1 M was 1.015 ± 0.022** (lines
172, 252). The "1.03 ± 0.02" form appears only in R4-G1's own Ga summary row (line 318), which the
write-up is faithfully following.
**Fix:** cite the source explicitly ("R4-G1 summary row Ga") or use the measured 1.015 ± 0.022.
The linked 0.84 / 0.65, clonal 0 and λ band 12.3–17.2 all check out (R4-G1 lines 165–166, 39, 129).

## NOTE

- **NOTE-1 — ruling on the declined RD instruction (brief item, requested explicitly): the analyst is
  right, and the defect is the registration's.** `R4-X1-verdict-rule.md` §RD opens "Where a verdict or
  an RH tag **depends on** how a quote is read", and the quote whose verdict A4d's fields score is
  A4d's own Statement — a verbatim 3.0 passage with no reading ambiguity. The same bullet adds: "A
  claim whose **formal statement fixes the reading** (A2e, a count) is **`SCOPED`, not
  reading-dependent**." A4d's Formal statement is exactly such a fix: "F_max(3.0) = 252,000 / 1,322 =
  190.6, **with no d**". A4d is `SCOPED`. Adding `reading-dependent:` and a separate count to A4d would
  mis-state the audit's own count of reading-dependent verdicts. **No `reading-dependent:` comment;
  no count.** Severity of the departure: **NOTE, no fix to the verdict.** One-line fix to the prose:
  cite the `SCOPED` clause by name in A4d and in the write-up, and record band 1b's RD instruction as a
  **second pre-registration defect** beside the non-exhaustive band table, rather than as a miss the
  analyst is charged with. (Per D-24 the lead rules if a steelman disagrees.)
- **NOTE-2 — the MINOR-1 extension checks out** (brief item 4). GGR-11: turn t=01:47:28–01:51:34,
  unbroken, no name spoken for the speaker (Zach, Mattie and Grayson are all addressed or discussed) —
  `panel` correct, and the note's "probably the host" is the right level of commitment (see MAJOR-1 for
  where the write-up exceeds it). GGR-27..GGR-29: one turn with GGR-43/GGR-44, the speaker identified
  only by a role ("the pop gen answer") and a channel ("I have a video of it on my channel called Do
  Genes?"), and addressing Erica — `panel` correct. The nearest names, two turns later at t=02:16:09
  ("Isaac", "Zach"), belong to a different speaker and a different topic. **The extension is sound; no
  finding against it.**
- **NOTE-3 — Q3's criterion was applied as written.** "Meets" requires engaging CV(K)→0 ⟹ (Fisher)
  d(w̄)/dt → 0; neither answer does, and the write-up says so. G's own `derived:` lines check out
  (Bin(157,000, ½): Var = n/4 = 39,250, SD 198.1, CV 0.2524 %, matching G lines 26 and 30), as do G5
  `internal: holds`, G1 `holds`/`contested` and G `external: contested`. Whether the height is right
  for a video roundtable is review 3's question, not mine.
- **NOTE-4 — A4d's Statement occurs exactly once.** The write-up's integrity by-product says "main.txt:25,
  abstract; **also at 675–676**". Lines 675–676 are a **variant** ("the shortfall is 1,075,000-fold **at
  the non-mutator rate**") not the quoted sentence ("**for non-mutators**"). Fix: "and in a variant
  wording at 675–676".
- **NOTE-5 — scoring table otherwise correct.** Every row matches the byte-identical registered text;
  the two self-reported misses are real misses and nothing else was re-scored. "hit, refined" (Q3 band)
  is a non-standard label; suggest "hit" plus the refinement in prose.
- **NOTE-6 — brief item 6 arithmetic.** 252,000/1,322 = 190.6, 252,000 × 0.45 = 113,400 and
  205e6/85.8 = 2.39e6 are not in the write-up; they live in A4d's **Formal statement**, which I
  recomputed: all three correct, and "2.2x larger" (2.3899e6/1.0754e6 = 2.22) is right.
- **NOTE-7 — hard rules observed.** Fetch in its own new directory, both dirs `git check-ignore`-clean
  (`.gitignore:2:sources/raw/`), PDFs `chmod 444`, nothing executed, no raw content in any commit, no
  workhorse use. The derived `main.txt`/`addendum.txt` are mode 644 rather than 444; harmless, noted
  only because the write-up says "`chmod 444`" of the fetch.

## Wrong numbers (old → right)

| Where | Old | Right |
|---|---|---|
| Q1 table, `d =` row (MINOR-1) | standalone-`d` regex "returns 0 in both files" under a case-insensitive heading | 0 case-sensitive; **3** case-insensitive in main (653, 724, 738), none a coefficient |
| Q3 / R4-G1 citation (MINOR-5) | "1.03 ± 0.02" presented as the measured free-recombination joint-fixation ratio | R4-G1's measured pair ratio is **1.015 ± 0.022**; 1.03 is the dispersion index (the "1.03 ± 0.02" form is R4-G1's own Ga summary row) |

No other number in the write-up or in the three claim files is wrong. Every token count, every
locator, every hash, every quote and every arithmetic result above reproduced on recomputation.
