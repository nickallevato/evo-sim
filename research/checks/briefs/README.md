# Agent briefs

One file per brief, `<check-id>-<role>.md`, committed **before** the agent is spawned (method audit MA-21, 2026-10-13: briefs were not in git and could not be audited). A brief states the goal, the files, what the lead had already seen, the constraints and the report format. See `.claude/skills/check-lifecycle/SKILL.md`.

Briefs for the 2026-10-13 batch were not saved; they exist only in that session's transcript.

## Index

| Brief | Role | Skill | Review tier |
|---|---|---|---|
| `BK-01-operator.md` | operator | republish-board | n/a (bookkeeping) |
| `B1e-Q2-analyst.md` | analyst | design-check | combined (escalates on B1/B1a/B2/B) |
| `VID-01-operator.md` | operator | source-refresh | combined (harvest only) |
| `FMnull-S4-analyst.md` | analyst | design-check | **three** (FM3, FM10 load-bearing) |
| `L1c-b-analyst.md` | analyst | design-check | combined (escalates on DN6 move, A2e/A3) |
| `L5-C1a-analyst.md` | analyst | design-check | combined (escalates on C1a move, C flip) |
| `C1d-D-analyst.md` | analyst | design-check | combined x2 (escalates on D, C2/C2a) |
| `L2-analyst.md` | analyst | design-check | **three** (H, H1, H5, H8 load-bearing) |
| `L3-analyst.md` | analyst | design-check | **three** (A2e load-bearing) |
| `O5-revert-operator.md` | operator | integrate-result | n/a (carries out D-21) |
| `O5-reviews-reviewer.md` | reviewer | review-check | **three each** on B internal and A2e external (D-21) |
| `L5-reviews-reviewer.md` | reviewer | review-check | the two L5 is missing under D-23 |
| `FM10-fair-criterion-analyst.md` | analyst | design-check | **three** (FM10, ROOT-FM load-bearing; D-25) |

Tier source: the `load_bearing: true` set in `docs/research/hierarchy.yaml` (33 nodes),
per the review-tier rule in `AGENTS.md`. **Since D-23 (owner, 2026-10-13) the escalation
clause is the rule, not a judgement call:** three reviews also where a registration carries
a verdict-field flip, or the node is a listed feeder of a load-bearing node (`R5-draft.md`
1.3). The briefs above that were written earlier the same day are read subject to that, and
under D-22 the three reviews of a check run one after another, never in parallel. Every combined-tier brief carries an escalation
clause naming the verdicts that would make it load-bearing; an agent that reaches one stops
and reports rather than applying the move.
