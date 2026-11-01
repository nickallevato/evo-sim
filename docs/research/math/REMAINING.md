# What is left: the map (2026-10-31)

Mapped, not done. **Measured** means counted from the files of record today. **Projected** means extrapolated from the branch A pilot (`pilot/RESULT-sonnet-deref.md`) and labelled as such. Update this file whenever a phase finishes.

## Where we are (measured)
| Measure | 10-09 | 10-10 | 10-11 | 10-13 | 10-31 |
|---|---|---|---|---|---|
| Nodes | 217 | 225 | 232 | 234 | 234 |
| Pending verdict fields | 145 | 109 | 111 | 111 | **111** |
| Load-bearing nodes open (of 33) | 14 | 14 | 14 | 14 | **14** |

- Pending fields: 52 internal, 49 external, 10 fidelity.
- By side: 54 Day, 15 critic, 7 ally, 6 literature. Most of this is because Day makes more claims. Check balance at exit.
- Node status: 122 `extracted` (never checked), 41 `checked`, 70 `reviewed`.
- The last team commit was 2026-10-19.
- **There is no schedule, so "behind" can only be a rate:** the count has not moved since 2026-10-11.

## The phases
| # | Phase | Size | Who | CPU | Blocked by |
|---|---|---|---|---|---|
| P1 | **Backfill the math map**: deref branches B, C, D, E, F, G, H and ROOT (191 nodes), then one merge pass per branch | about 0.45M Sonnet tokens plus 8 merge passes (projected) | Sonnet `deref-source`; Opus merge or spot check (seeded 8 per branch) | none | — |
| P1b | Deref the new and unmapped sources: vid02 (pilot done, merge it); *Probability Zero* 2nd edition | one per source | Sonnet | none | **owner** (book text) |
| P2 | **Settle the derivation and lookup objects** (pure maths and sourced numbers) | projected about 60-90 open objects (branch A: 14 of 42) | Opus designs, Sonnet looks up; combined review | none (local seconds) | some `outside` (branch A: 5) |
| P3 | **Compute manifest**: each simulation or regression object pre-registered, smoke-measured, then run as one campaign | branch A: 2 objects, about 310 CPU-h unmeasured (M-003 LTEE-to-recombining transfer, M-040 sweep-scan power). Projected 10-15 objects and 1,000-3,000 CPU-h in all | Opus designs; operator runs | na-workhorse (11 cores, about 260 CPU-h/day), builder for overflow, dh01 small | — |
| P4 | Roll-ups: ROOT, ROOT-M, ROOT-FM from settled objects | 3 nodes | Opus plus three reviews | none | P2, P3 |
| P5 | R5: the sensitivity table, which becomes the simulator variable list; criticality pass; exit | — | Opus | small | P4 |

**Reading it:** compute is not the constraint. Even the projected high end of P3 is about 12 days on na-workhorse alone, and less with builder. The constraint is P1 and P2: turning words into objects and settling the cheap ones. That is token work, and the pilot shows Sonnet can do most of it.

## Known blockers that only the owner can clear
- *Probability Zero* 2nd edition text. The critics used a 1st-edition ePub (vid02 00:32:25); the audit may not.
- Paywalled papers (ROADMAP D4).
- Publication holds (B-R20/B-R21).
- FM10 internal waits on Day releasing his method (outside, not the owner).

## How this ties to the team process
The exit gap (`research/tools/exit_gap.py`) stays the gate. Once P1 is merged, `objects.yaml` becomes the list `exit_gap.py` counts: an item is closed when its objects are resolved and its claim fields are set. Until then the gap counts nodes.
