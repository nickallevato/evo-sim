# Process review, 2026-10-13 to 2026-10-19

This review covers the 134 commits from `9806966` (team set up) to `9cf7521`. It looks at what the autonomous team did and whether that work moved the audit toward its exit criteria (`PLAN.md`). It feeds [`OPERATING-PROCESS.md`](OPERATING-PROCESS.md). Counts come from `git log` and `hierarchy.yaml`. Nothing below changes a verdict.

## Headline

**The exit gap did not shrink.** There are 33 load-bearing nodes. 14 of them were open (not `reviewed`, or carrying a `pending` field) at `dfbcbc1` (2026-10-09), at `9806966` (2026-10-13) and at `9cf7521` (2026-10-19), and they were the same 14 nodes each time. Two fields went back to `pending` on purpose (D-21 revert of B internal and A2e external), and neither has come back out.

## Where the effort went

| Kind of work | Evidence | Moved a gap field? |
|---|---|---|
| Checks on nodes that aren't load-bearing, or on fields already set | B1e-Q2 (B1e not load-bearing), VID-01-score (Ge), L5 and L5-C1a (C, C1a), C1d-fu, D-fu, L1c-b (pre-registered; C1d-fu, D-fu and L1c-b have no write-up); L2 (H, H5, H8 external already `contested`, while their gap is fidelity); FMnull-S4 (ROOT-FM external already `contested`, while its gap is internal and fidelity) | no |
| Checks on the gap | L3 (A2e alpha; collected, not written up); D-21 re-reviews of B and A2e | not yet |
| Ruling recursion | 36 commits mention a ruling, 7 are fresh checks of rulings. B internal went ruling B-R1..10, fix pass, check (BLOCKER), re-ruling B-R11..19, fix pass 2, check EVO-83 (MAJOR), and is still `pending`. L5 went L-R1..10, fix pass 2, check, L-R11..16, fix pass 3, check EVO-82 (BLOCKER on L-R11/L-R12). | no |
| Debugging the orchestrator inside the audit | D-29 to D-37 and amendments: lane tokens, `backlog` gating, monitors, `skip_if_active`, routine backstops. `DECISIONS.md` grew by 688 lines, mostly about Paperclip mechanics, not the audit. | no |
| Process machinery | `verdict_scope` field, lint error and board `scope_guard.py` (B-R20..B-R30, about 5 commits, all "no verdict value moves"); 20 briefs, 2,787 lines (one is 462 lines) | no |
| Source refreshes | 5 commits in 5 days (10-14, an addendum, 10-15, 10-17 plus a fix, 10-18), all "logged, not scored" under the O-7 freeze. The owner had ticked **weekly** (D-20). | no |
| Figure literals | EVO-85, 97, 98, 99: four tasks to make `readme_figs.py` read counts instead of literals; each found that "figure already matches". | no |
| Incidents | `9f863fd` silently reverted a fix pass (`3c9df34`), and it was restored in `34535d2`. `.claude/` settings blocked `git pull --rebase` (`7477e6b`). | no |

18 of the 134 commit subjects say outright that no verdict value moved.

## Duplication

- Counts are kept by hand in `README.md`, `docs/HANDOFF.md`, `docs/arguments/README.md`, the board and `readme_figs.py`, and they drift. BK-01 and EVO-97/98/99 each re-derived them.
- The same rule appears in `AGENTS.md`, `TEAM-BRIEF.md`, the agent files, the skills and `DECISIONS.md`. The concurrency cap is stated in at least four places and changed twice (D-11, then D-22).
- `ROADMAP.md` carries 60+ "B" proposal rows from criticality passes. Each is a standing invitation to new work, and none is on the gap.
- Refresh 10-14 was followed by an addendum correcting it, and refreshes were then repeated with nothing to score.

## Why it happened (process causes)

1. **No computed goal.** The queue was a list of interesting things, so any plausible check looked like progress. Fix: `exit_gap.py`, and a `Gap:` trailer on every commit.
2. **No stop rule when blocked.** Most gap items wait on the owner or on Day (FM10 internal, the fidelity fields, X-GAPS). The team filled the wait with off-gap work. Fix: when nothing is workable, send one owner card and stop.
3. **Unbounded recursion.** Ruling, then check, then re-ruling, then check, with no limit. Fix: one ruling and one check, then the owner.
4. **Meta-work is captured as decisions.** Each orchestrator surprise became a D- entry and a rule. Fix: put those in `ops-notes.md`, five lines each, and stop when the orchestrator blocks work.
5. **Triggers ignored.** The owner ticked a weekly refresh and the team ran it daily. Fix: a trigger for each recurring task in the limits table.

## What worked, and stays

Pre-registration before runs; committed briefs; a fresh reviewer for each review; post hoc work labelled; one agent on shared files; a measured smoke before a long run (D-36); and recording every reading (RD) instead of asking the owner.
