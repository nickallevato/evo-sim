# A2e-analyst-2: fix pass 1 on R4-L3 (asymptotic MK alpha), with the lead's rulings

**Role:** analyst. **Written by:** lead, 2026-11-01. **Authority:** `docs/research/gap-blockers.yaml`, row A2e; D-40 (one combined review; for L3 "short critics' section, then move on"). EVOA-8 was cancelled after its reviewer had already committed the critic-side review (eb593b4, in scope), so that file serves as the critic section. No further review runs on L3.

## Gap item
A2e. Field: `verdicts.external` of `docs/research/claims/A2e-ltee-as-ceiling.md` (`pending`). **It does not move in this task**; section 6 stays a proposal for integration.

## Deliverable
`research/checks/results/R4-L3.md` with a new section "Review resolution (fix pass 1, 2026-11-01)" that answers every MAJOR and MINOR by id, plus the edits in place. Reviews: `REVIEW-R4-L3-correctness.md` (8432a1c: MINOR-1..4), `REVIEW-R4-L3-steelman-day.md` (fb8b66d: D1-D7), `REVIEW-R4-L3-steelman-critic.md` (eb593b4: SC1-SC6). NOTEs are optional.

## Rulings (one per conflict; final, D-38; disagree once in the report and the owner decides)
- **R1, D1 + SC1 (what B5 means).** Take both. Section 7 gets D1's post hoc precision paragraph (B6 needed P ≤ -0.107; B2 needed P > 0.072, B1 P ≥ 0.107). Section 8: remove "no band below B5 was reached" from the critic bullet. Day bullet 1 gets D1's "the best outcome its precision allowed for the Day side" and SC1's "an outcome the critics' neutral-theory position (unscored) also predicts; it does not separate the ceiling from that position". The headline gets SC1's line. The critic bullet "gets no confirmation" becomes SC1's wording.
- **R2, D4 + SC2 (0.096).** One sentence in section 7 item 3 and section 8: "0.096 lies 0.004 above the gene-bootstrap upper bound and inside the MC envelope only through its tail above alpha = 1; the comparison is across estimators, and HM7 predicts aMK below ABC-MK, so it is weak evidence against ABC-MK (post hoc)." SC2's 72% weakly-adaptive quote and "ABC-MK 0.135 vs aMK 0.076 on the same samples" go into sections 6 and 8 as the critics' strongest case.
- **R3, D5 + SC3 (the strike and the 0.096 gap).** The strike stands as registered; no hedge. Text: "Struck, as registered (B5). 0.076 is not reproduced as a point by L3's pipeline (same 661 samples and divergence basis, different gene set) and lies inside L3's bootstrap interval." The "second-order Day point" moves to "Both / the audit's own errors" in SC3's wording (it weakens L3's point as much as 0.076).
- **R4, D6 + SC3 (the audit's missed expectation).** Add D6's Day bullet as a plain fact (Q2 and Q8 missed, DS/DS+ hit) and keep the "Both" entry; one clause notes that pipeline spread (R3) bears on that miss.
- **R5, D2 (Gayà-Vidal) + SC2.** Accept D2: delete the GV clause from the critic bullet; add the Day bullet with D2's honest limit (≥ 80% class 0.020, about h). GV's standing in R4-A2e-alpha is for integration.
- **R6, D3 + SC6 (scope of the Day credit).** Take both: SC6's narrower wording of the Day bullet (coding only, 19,504 transcripts, a coding count bounds the genome-wide count from below only), plus D3's subset sentence in the headline and section 6, weakened by HM7.
- D7, SC4, SC5: accept as written. Correctness MINOR-2..4: answer in text. **MINOR-1** (hand-patched `sites.vcf.gz`): the run stands; record that the host provenance is a separate operator task, not done here.

Reviewer numbers are quoted labelled "post hoc (reviewer)". You may recheck them by arithmetic on the committed json (one local `research/.venv/bin/python -I` process, <500 MB, <1 min); no runs, no fetches, no new script. Registered sections keep their registered wording; additions are separate sentences labelled post hoc.

## Allowed paths
- `research/checks/results/R4-L3.md`

Grep the quotes files, `REVIEW.md` and `HANDOFF.md` by id; never read them whole. Do not edit the reviews, the script, raw outputs, claim files, `gap-blockers.yaml`, `QUEUE.md`, `REVIEW.md`, `DECISIONS.md` or R4-A2e-alpha.md.

## Skill
`fix-pass` (`.claude/skills/fix-pass/SKILL.md`).

## Budget
At most 2 commits. Fix passes on L3: this is 1 of 2.

## Stop when
- the fix pass is committed and pushed to `research`; OR
- an input is missing or a reviewer number does not reproduce (report it with both values; don't choose); OR
- the work would need a path outside the list, a run or a fetch.

## Not in scope
Integration, the MINOR-1 provenance task, A2e part (1), GV's standing, the publication hold, tooling, other nodes. Ideas: one line in the report.

## Commit trailer
`Gap: A2e`, then the attribution lines your issue gives you. Explicit paths; `git pull --rebase origin research` before `git push origin research`. Not to `master`.

## Report (≤ 300 words, as the issue comment)
Commit(s); a table of finding id → accepted / in part / not accepted; any reviewer number that did not reproduce; any ruling you disagree with (once); next step.
