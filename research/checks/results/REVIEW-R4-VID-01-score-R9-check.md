# Fresh-reviewer check of lead ruling R-9 (R4 VID-01-score) — EVO-76

Lifecycle step 4, "where the ruling moves the governing reading of a verdict field, a fresh
reviewer checks it before integration". Reviewer: fresh instance; did not write the check, the
write-up, the fix pass or any of the three reviews. Date 2026-10-14.

**Narrow scope, as briefed.** Two questions only: (1) is R-9 correct, (2) was it applied faithfully
with nothing else moving. The rest of the check, rulings R-1..R-8 and R-10..R-15 are not reopened.
Everything below was recomputed from the primary files, not taken from the write-up.

**Verdict: R-9 is SOUND and was applied faithfully. 0 BLOCKER, 0 MAJOR, 1 MINOR, 2 NOTE.
Nothing here blocks integration.**

## 1. Is R-9 correct?

**Rule text.** `research/checks/results/R4-X1-verdict-rule.md` line 202 reads, verbatim:
"- Extended readings (a different object, or a wider claim) are reported with their own verdicts
but cannot set the verdict field or the headline tag." R-9's quotation is exact, the line number is
right, and the bullet is in §RD (lines 196-202), which governs reading-dependent verdicts. ✔

**Is reading (a) a different object?** Yes, and on the transcript's own usage rather than on the
audit's say-so. `sources/raw/vid01-2026-10-13/AqC1ZM4icms.transcript.txt` line 313 has the panel
draw exactly this contrast — "The arguments that show up in probability zero's first edition are
not the same arguments that show up in Mittens 3.0" — and line 317 applies it to d itself: "In
mittens 3.0 … He kind of throws the D coefficient off to the side. It no longer seems nearly as
important as it was in in probability zero." GGR-13 (line 320) is the *solicited reply* to that
turn ("Does that sound right to you, especially Grayson?" → "he's still using the de coefficient in
mittens"). The referent under dispute is the paper the speaker is being asked about, and "still"
marks persistence *into* it. Relocating "mittens" to the pre-3.0 / *Probability Zero* line is
therefore a change of object, not a scope of the same one.

**Robust under the alternative construal.** If one resists "different object" and reads "mittens"
as the MITTENS corpus across versions, that is "a wider claim" — the *second* disjunct of the same
bullet, with the same consequence. R-9 does not depend on which disjunct you pick. This is worth
recording because it is the strongest objection available to R-9 and it fails either way.

**Is (c) the right reading to install?** Yes. Among the in-scope readings, RD line 198 takes "the
reading under which the speaker's *quoted statement* is most defensible". (b) grades GGR-13
`contradicted`; (c) grades it `accurate`. (c) is more defensible for the speaker and is correctly
installed. I confirmed the two facts R-8 rests on (R-8 itself not reopened): `C2-bio-cycle-d.md`
line 3 defines Bio-Cycle as `g_eff = d x g_nominal`, and `sources/raw/vid01-score-2026-10-13/`
`main.txt:653-654` reads "approximately one fixation per 27,600 effective generations (Day and
Athos 2025, Appendix D). Applied to 252,000 generations provides 8 achievable fixations against the
205 million required." `effective generation` occurs once in `main.txt` and zero times in
`addendum.txt`, as claimed.

**NOTE-1 (in R-9's favour, not raised by the three reviews).** The *pre-registration* already
mapped the band that was hit to governing reading (c): write-up line 88, band **1b**, "Governing RD
reading: (c) 3.0-including-Appendix-D". The outcome was 1b′ (line 285), 1b's near-neighbour. So the
departure from registration was the original write-up's choice of (a) as governing; R-9 restores
the pre-registered mapping rather than introducing a new one. That strengthens R-9 beyond the
ground the lead gave for it.

## 2. Was it applied faithfully, and did anything else move?

| Item checked | Where | Result |
|---|---|---|
| (a) kept in the Readings table, `accurate` / `accurate` | write-up line 306; `A4d` line 77 | ✔ both |
| (a)'s TW-01 cross-reference kept | same rows | ✔ both; and the reference resolves — `A-mittens-formula.md` line 39 gives TW-01 "202,500 generations", `450,000 x 0.45 = 202,500` |
| (a) marked extended / may not govern, citing RD line 202 | write-up lines 302, 306, 322-327; `A4d` lines 73, 77, 82-88 | ✔ both |
| (c) marked governing among in-scope readings | write-up line 308; `A4d` line 79 | ✔ both |
| Headline wording identical in the two files | write-up line 799 / `A4d` line 12 | ✔ "3.0 contains no `d` term and applies no d multiplier to its generation count; an overlap correction survives by citation inside the §8.6 rate" |
| **`A4d` `internal: holds` did not move** | `A4d` line 12 | ✔ `git diff 3f40a4c 83f4f4d` on that file shows the comment rewritten and the **value unchanged**; all three reviews had agreed it survives |
| `reading-dependent:` question unmoved by R-9 | `A4d` lines 95-102 | ✔ still `SCOPED` under RD line **198** (the Formal statement fixes the reading), no `reading-dependent:` comment. This rests on 198, which R-9 does not touch; the change of governing reading did not leak into it |
| Counts unmoved | `docs/HANDOFF.md` line 91; `docs/arguments/README.md` line 105 | ✔ both still read 8 claims / 12 verdict fields / 15 with RH tags, and A4d is not among them. Neither file is in `88c444d` or `83f4f4d` |
| Independent token recount (3.0) | fetch dir | ✔ "252,000" = 8 in `main.txt` + 2 in `addendum.txt` = the "10x" claimed; 0 hits for `252000` |

**MINOR-1 — stale self-locators after the fix pass.** The write-up at line 799 and in the Review
resolution at line 983 says the "clean of the d coefficient" headline "is replaced at write-up lines
**477 and 502**". The fix pass grew the file; lines 477 and 502 now sit in the Q3 recombination
material. The substantive fix is done (the phrase survives only in retrospective "the earlier form
was…" sentences), so this is wording, not a missed correction. Replace the two line numbers with
section names, or drop them. Cosmetic; does not block integration.

**NOTE-2 — vocabulary, flagged forward, not a finding against this fix pass.** The Readings table
grades the critic statement `accurate` / `partly accurate` / `contradicted`, mixing the fidelity
and external vocabularies, and "partly accurate" is not in AGENTS.md's fidelity list (the term
there is `partial`). This descends from R-8 and from the original R-3 table, not from R-9, and
GGR-13/14 has no claim file, so no field is mis-typed today. It matters only if this grade is ever
lifted into a verdict field or a count — worth one line at integration.

## Bottom line

R-9 is sound on the rule text, on the transcript, and under both disjuncts of the bullet it cites;
it is also the reading the registration itself named for this band. It was applied in both files
without collateral movement: `A4d` `internal: holds` stands, the SCOPED finding stands, the counts
stand, and reading (a) survives in the table with its verdict and its cross-reference exactly as
the ruling required. Integration may proceed.
