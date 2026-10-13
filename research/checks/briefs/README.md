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

Tier source: the `load_bearing: true` set in `docs/research/hierarchy.yaml` (33 nodes),
per the review-tier rule in `AGENTS.md`. Every combined-tier brief carries an escalation
clause naming the verdicts that would make it load-bearing; an agent that reaches one stops
and reports rather than applying the move.
