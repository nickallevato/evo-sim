# Bounded D-24 check of the lead's re-ruling B-R11 to B-R19 (and B-R20/B-R21), B internal

Date 2026-10-14. Reviewer: a fresh reviewer instance (Paperclip EVO-83), using the skill `review-correctness`. Labels: BLOCKER / MAJOR / MINOR / NOTE. **This review sets no verdict.** It is bounded by B-R19 to two questions: Q1, is S_L wrongly admitted (B-R12); Q2, is B-R21 sufficient. The findings of `REVIEW-R4-B-internal-ruling-check.md` (ccdb989) are taken as accepted and are not re-reviewed. Files read: O5 brief at `9f863fd` / `787a2da` (B-R1 to B-R21), `R4-B-internal.md` at `722769f` (sections 3a, 6), `L5-reviews-reviewer.md` L-R11 to L-R14, `REVIEW-R4-L5-C-ruling-check-2.md` (a2ce060), RD in `R4-X1-verdict-rule.md` l.196-202, `DECISIONS.md` D-15, commit `3f881b0`, and the tools named in section 2.

> **No BLOCKER.** S_L is supplied by the source. HL states S_L's proposition in its own words at l.166-169, l.247-253 and l.436-438, so the lead's own test admits it. B-R12's second ground is false, though: Q157's list of inputs fits C exactly as well as S_L. The B and L5 rulings agree in outcome but not in their stated grounds. L-R12 is the one that has to move, and B's admission survives whichever branch the owner takes on EVO-82. B-R21 is not sufficient. As worded, its lint trigger cannot fire. Its render rule covers only the board. Bare tallies and two public generated pages stay open. The hold in B-R21(5) makes none of this live today.

Counts: 0 BLOCKER, 6 MAJOR (1, 4, 5, 6, 7, 8), 2 MINOR (2, 9), 3 NOTE (3, 10, 11).

## 1. Question 1: is S_L wrongly admitted?

Source: `sources/raw/b-steelday-2026-10-13/hl.txt`, 467 lines, **sha256 `3182a5b6cd3a8ac822017d6d7f509c234ab147b334546d62f88623142d9dbfe2`** (the same text the lead and ccdb989 used). I read l.1-20, 40-56, 90-137, 145-170, 214-224, 240-258, 320-372 and 410-467 directly.

### 1(a) Does HL apply the lineage duration to the census against the ceiling?
**Yes.** l.247-253: "Use the lineage duration, the full continuous ancestry, which in the case of the human lineage is roughly six and a half million years … The human ceiling rises accordingly, from thirty-five thousand to about one hundred fourteen thousand. And then note that we are still eight billion strong, which puts us seventy-two thousand times over the enlarged ceiling." The duration enters G, G enters X = (Vₖ+2)·G/16, and the current census is compared against X. That is S_L, and the lead is not reading a different computation into the passage. Table 1 does the same computation (l.150-157: "The human row uses the lineage duration … 114,000 | 8.2 × 10⁹ | 72,000×").

**MINOR-2 (B-R11 / SL1, "the only place HL introduces and applies 'lineage duration'").** This is false as worded. HL uses the exact term at l.130 (it defines G as "the lineage duration in generations"), at l.150 (Table 1) and at l.248. It also gives the ceiling "as a lineage" at l.222. All of these are census-against-ceiling, so the substance gets stronger. But HL also applies "the lineage" in the C sense: at l.416-417 the ancestral fill is "thirty-five percent fill across two million years even when granted the entire lineage", and at l.432-433 it writes "once the lineage has accumulated the drift exposure ∫ dt/4Nₑ(t)". *Fix:* say "every use of the exact term 'lineage duration' (l.130, l.150, l.248) is the G of the census ceiling; HL uses 'the lineage' in the completion sense at l.416-417 and l.433".

### 1(b) Does Q157's paragraph name S_L's inputs and not C's?
What is there, verbatim (l.458-460): "It takes Kimura's own fixation time, Wright's own effective size, and the field's own census, generation, and reproductive-variance figures". The quote in B-R12 is accurate.

**MAJOR-1 (B-R12, "Not a different object", second sentence: "They are not the inputs of C").** This is false. The list does not tell the two readings apart:
- C's verdict, as the lead computes it in B-R15, uses a census (hominid 1e5), a generation count (G at 6.5 / 6.3 My) and reproductive variance (through X = 113,750 / 110,250). It also uses HL's 4Nₑ fixation-time criterion (l.97-98). These are the same five inputs.
- HL's own completion-sense computation uses "a census near a hundred thousand held static for the full two million years" (l.364-365).
- Where HL says "the field's own" of a census figure, it attaches the phrase to the **ancestral** number: 10,000 "is also, not by accident, the size the field's own methods assign to the ancestral human population" (l.55). Read as written, "the field's own census … figures" is at least as close to C's input as to 8.2e9.

The ground fails. B-R12's first bullet ("not wider") and B-R11's term argument do not depend on it, so the admission does not fall with it (see 1c). *Fix:* strike the sentence in B-R12 and SL2. Re-ground "not a different object" on what HL itself says (NOTE-3).

### 1(c) Is S_L supplied by the source or required by the conclusion? (the L-R12 test)
**Supplied.** HL states S_L's proposition in its own words three times, none of them in the quoted sentence and none of them derived from it:
- l.166-169: "A neutral mutation arising in any of these populations today cannot reach fixation by drift before the lineage carrying it is either extinct or no longer recognizable as the same species."
- l.251-253 (above): the census is "seventy-two thousand times over the enlarged ceiling".
- l.436-438: "the only census population that fills the pipe in time is one too small to sustain a viable species". The verb "fills" is predicated of a *census population*, 15 lines before Q157's "the pipe that would finish them never fills".

**Not required by the conclusion.** S_L does not deliver B's title claim. B-R14 records that it is "asserted by no governing reading" (RH3), and S_L "says nothing about whether drift produced the observed divergence". A reading reverse-engineered from Day's conclusion would deliver that conclusion. S_L does the opposite: it makes the sentence true at the cost of Day's node-level claim. That is charity to the statement, which is exactly what RD l.198 asks for. I therefore cannot say S_L is a reading the source does not supply, and the field does not return to `non-sequitur` on this ground.

**NOTE-3.** Neither B-R11 nor SL1 cites l.166-169 or l.436-438, and they are the strongest textual support for S_L. *Fix:* add both to SL1. The l.436-438 one in particular, because it uses Q157's own verb with a census subject.

**MAJOR-4 (the record of D-15 is reversed without saying so).** The owner-approved text of RD reads: "Effect: B internal moves from `holds` to `non-sequitur`" (`R4-X1-verdict-rule.md` l.198). The D-15 row in `DECISIONS.md` says the same. In `3f881b0` the S (current size) row was **on the table** and was scored `non-sequitur`, because its inference was read at lineage level ("it needs an empty lineage pipe that HL's own text … excludes"). B-R13 brings `holds` back on the same field. It does not state that this reverses the recorded effect of an owner decision. It also does not state that the whole difference from the 2026-10-11 S row lies in SL4, which reads the *inference* ("cannot be finished", "closes") at census level as well as the clause. That is a defensible reading step: l.353-354, "The channel is not slow, it is empty", is census-regime closure vocabulary. But it is the step the owner's approval was recorded against, and a reader of D-15 today would conclude the opposite. Not a BLOCKER: D-15 approved a definition, its effect column applied that definition to the readings available then, and D-28 makes reading questions the lead's. *Fix:* (i) B-R13 gains one sentence naming the reversal and SL4 as its sole ground. (ii) A dated note goes under D-15 in `DECISIONS.md`, and the owner is told, as Part 3 of the O5 brief did for D-21. (iii) The effect parenthesis at RD l.198 is annotated by the freeze procedure, because it is rule-file text. Until then it contradicts the field.

### 1(d) Charity symmetry: B-R12/B-R13 against L-R12
**MAJOR-5. The outcomes are consistent. The stated grounds are not. L-R12 has to move, and B does not.**
- Take the test strictly: "the source states the reading's proposition". It admits S_L (1c: three verbatim statements). It does not admit R-d: no text states s ≥ s\* for the comparator, and EVO-82 found only an s *entailed* by the post's crossing test (its BLOCKER-5).
- Take the test loosely, as B-R11 words it: "S_L is Day's own computation". It admits R-d as well, because the post's own crossing test is Day's own computation of what the 15,556 are held to. EVO-82 already made this argument. B-R11's wording is therefore the precedent L-R12 cannot answer.
- L-R12's first ground ("charity to the arguer") is a correct use of RD's second sentence. But it is not the ground B-R13 gave for admitting S_L, so the two rulings cite RD differently. The consistent statement: admit a reading when the source states its proposition, and let the field go to the reading under which the *whole* quoted statement is most defensible. Under that, S_L governs Q157, and R-d does not govern C, by EVO-82 NOTE-6 (R-d moves the failure from Q276 to Q275).
- **B is robust to both branches** of the owner question EVO-82 costed. Strict test: S_L is admitted (stated) and R-d is refused. Loose test: both are admitted, and only L5 moves. B internal's admission moves under neither.

*Fix:* B-R11's "it is Day's own computation" becomes "HL states it (l.166-169, l.251-253, l.436-438)", so that it cannot be cited as a computation-entailment precedent. L-R12's ground goes to the owner already under EVO-82. This review adds only that B gives no reason to keep it.

## 2. Question 2: is B-R21 sufficient?

I checked each route in the repository at `a2ce060`.

**MAJOR-6 (B-R21(2) cannot fire as worded).** "`lint_research.py` errors if a field's value is scoped in the comment but has no `verdict_scope` entry" needs lint to see the comment. But lint's only parse is `yaml.safe_load(m.group(1))` (`lint_research.py` l.32; B-R20 cites l.25-30), and that drops comments, which is B-R20's own finding. The node writer also copies a fixed key list (l.105: `("id", …, "verdicts")`), so a new `verdict_scope` key would not reach `hierarchy.yaml` either. *Fix:* the trigger scans the **raw** front-matter text for `SCOPED` / `reading-dependent:` on a verdict line. Alternatively, `verdict_scope` becomes mandatory for every field whose value moved after D-21. Either way, `verdict_scope` is added to the l.105 key list.

**MAJOR-7 (B-R21(3) names only the board; three public renderers and three direct readers remain).**
- `research/checks/gen_mermaid.py` l.4, l.14 reads `hierarchy.yaml` and writes `int:{internal}` into `docs/research/hierarchy/branch-B.md` (today `int:pending`, l.5). That page is in `docs/`, and `docs/` is public on GitHub and served by Pages (D-26).
- `research/tools/argmap_render.py` l.337 reads `hierarchy.yaml` for `docs/arguments/`.
- `research/tools/board/snap.py` l.5-7 reads claim front matter **directly**, bypassing `hierarchy.yaml`, and keeps `str(v).split()[0]`. A scope in `hierarchy.yaml` does not reach it.
- `method_audit_stats.py` l.27 and `grade_certainty.py` l.36 (external verdicts, which includes A2e) also read front matter directly into criticality-layer counts.

*Fix:* (3) becomes "every renderer and every reader of verdict values", with this list in it. Lint fails if any generated file under `docs/` shows B internal or A2e external without its scope string.

**MAJOR-8 (tallies travel bare).** Lint's tally is `verdict_counts[(k, str(val).split()[0])]` (l.89-92), printed as `internal:holds=N`. That count is hand-copied into `readme_figs.py` l.130-132 (`("holds", 133, …)`), `README.md`, `docs/HANDOFF.md`, `docs/arguments/README.md` and the board's tally line (`upd23.py` l.3, l.19). Once integrated, B internal adds 1 to an unqualified "holds" count. B-R14 names "every table, tally and board row", and B-R21 contains nothing for tallies. *Fix:* lint counts scoped values separately (`holds (scoped)`), like the separate count RD already requires for reading-dependent verdicts, and `readme_figs.py` draws them as their own bar or omits them with a stated note.

**MINOR-9 (hand-written prose).** Milestone posts, `RESULTS.md`, `REVIEW.md`, `QUEUE.md`, `HANDOFF.md` "Still open", `standard-forms.md` (Bchk row, l.369), `defeaters.yaml` and parent/child claim bodies are written by hand, and no tool closes them. B-R21(4) holds only "board publication". *Fix:* extend the hold in words: no text outside `B-neutral-theory-cannot-rescue.md` states B internal's value without the scope string. The integration review greps `B internal` near `holds` before the push to master.

**NOTE-10.** `argmap_check.py` is not a route. It validates ids and edges (l.15-27) and loads the defeater list files (l.269). It renders no verdict value.

**NOTE-11.** None of MAJOR-6/7/8 is live today. Every route currently shows `pending`, and B-R21(5) bars integrating `holds` before the tooling lands. They decide what "the tooling has landed" has to mean.

## 3. What this decides (B-R19)
No BLOCKER on Q1 or Q2. By B-R19 the fix pass and the integration may proceed, but only after B-R21's tooling lands with the fixes in MAJOR-6/7/8. The fix pass carries MAJOR-1, MAJOR-4, MAJOR-5, MINOR-2 and NOTE-3. MAJOR-4(ii) is a report to the owner and not an owner question. This check is the last one in the chain, and it opens no further check.
