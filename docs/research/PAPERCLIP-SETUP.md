# Paperclip setup for the evo-sim team (2026-11-01)

The exact configuration of the new Paperclip company, and how to migrate from the old one ("Evosim Labs", prefix EVO). Field names come from the server's own OpenAPI spec (instance commit `0a99c83`). Why each control matters: [`OPERATING-PROCESS.md`](OPERATING-PROCESS.md); the history: [`PROCESS-REVIEW-2026-10-31.md`](PROCESS-REVIEW-2026-10-31.md).

## Design in one line
The repo (`gap-blockers.yaml`) is the queue. Paperclip holds only the one task that is running. Each task ends in a review stage by the Lead, and that review is when the Lead picks the next task.

## 1. Company
`POST /api/companies` `{name: "Evo-sim Audit", description: "Neutral two-sided audit of Vox Day's mathematical case against evolution. Work comes only from the exit gap (repo docs/research/OPERATING-PROCESS.md)."}`
then `PATCH /api/companies/{id}` `{requireBoardApprovalForNewAgents: true}`.
No budget: Paperclip records no cost for these Claude runs, so a budget would never stop anything. The limits below do that job. The issue prefix is assigned by Paperclip.

## 2. Agents (`POST /api/companies/{id}/agents`)
Common to all four:
```json
{
  "adapterType": "claude_local",
  "adapterConfig": {"maxTurnsPerRun": 300, "timeoutSec": 7200, "graceSec": 15,
                    "dangerouslySkipPermissions": true},
  "runtimeConfig": {"heartbeat": {"enabled": false, "wakeOnDemand": true,
                    "maxConcurrentRuns": 1, "cooldownSec": 600}},
  "permissions": {"canCreateAgents": false, "canCreateSkills": false}
}
```
`runtimeConfig.aiConnection` is copied from the old agent with the same role, so the Claude login carries over.

| name | role | model | effort | reportsTo | instructions file (`instructionsBundle.files["AGENTS.md"]`) |
|---|---|---|---|---|---|
| Lead | general | claude-opus-5-5 | high | (none) | pointer to `.claude/agents/lead.md` |
| Analyst | researcher | claude-opus-5-5 | high | Lead | pointer to `.claude/agents/analyst.md` |
| Reviewer | qa | claude-opus-5-5 | high | Lead | pointer to `.claude/agents/reviewer.md` |
| Operator | devops | claude-sonnet-5-5 | medium | Lead | pointer to `.claude/agents/operator.md` |

Pointer text (the role name is substituted):
> You work on the evo-sim audit in /home/na/projects/evo-sim, branch `research`. Start every run with `git pull --rebase origin research`. Then read AGENTS.md, docs/research/OPERATING-PROCESS.md and .claude/agents/<role>.md, and follow them; they override any default skill. End every commit with the attribution lines your issue gives you, plus a `Gap:` trailer.

Paperclip's default skills stay. Agents are created **paused** and resumed together once setup is checked. After that they stay active: with the timer off and no issue assigned, an agent never runs.

## 3. Goal and project
- `POST /api/companies/{id}/goals` `{title: "Close the exit gap", level: "company", status: "active", description: "research/tools/exit_gap.py lists the open items; PLAN.md exit criteria."}`
- `POST /api/companies/{id}/projects` `{name: "evo-sim audit", status: "in_progress", goalId, leadAgentId: <Lead>, workspace: {name: "evo-sim", sourceType: "local_path", cwd: "/home/na/projects/evo-sim", isPrimary: true}, executionWorkspacePolicy: {enabled: true, defaultMode: "shared_workspace", sharedWorkspaceConcurrency: "serialize"}}`

`serialize` makes runs in the shared checkout go one at a time, which enforces the cap of one agent at a time (D-22) at the platform level.

## 4. Routines (two), with `concurrencyPolicy: "skip_if_active"` and `catchUpPolicy: "skip_missed"`
| title | agent | trigger (`POST /api/routines/{id}/triggers`) |
|---|---|---|
| Weekly status to the owner | Lead | schedule `0 17 * * 5`, America/Denver |
| Weekly source refresh (log only) | Operator | schedule `0 8 * * 0`, America/Denver |

There is no host-watch routine (long runs aren't polled) and no backstop routine.

## 5. Issues the Lead creates (one at a time)
Every worker issue carries:
```json
"executionPolicy": {"mode": "normal", "commentRequired": true, "maxReviewRounds": 1,
  "stages": [{"type": "review", "participants": [{"type": "agent", "agentId": "<Lead>"}]}]}
```
The Lead appends a second stage, `{"type": "approval", "participants": [{"type": "user", "userId": "<owner>"}]}`, when the task moves a verdict field, changes a rule or publishes anything.

## 6. Migration, in order
1. Repo: `.claude/agents/lead.md`; the old company's in-flight work goes into `gap-blockers.yaml` (L3 into the A2e row) and QUEUE.md "Parked at the Paperclip migration". Done in commit with this file.
2. Server clone: `git pull` in `/home/na/projects/evo-sim`; `git config core.hooksPath .githooks`.
3. Old company: agents stay paused; every open issue → `cancelled` with the comment "Migrated: see QUEUE.md 'Parked at the Paperclip migration' / gap-blockers.yaml"; routines archived; company `status: "archived"`. Nothing is deleted.
4. New company: sections 1-4, then resume all four agents. Nobody pauses or resumes agents in normal running; pausing is the owner's emergency brake.
5. Kickoff: the owner creates one issue for the Lead: "Run the loop once." The expected first task is the operator task on the `verify:` rows.

## 7. Check on the first task
- The reviewer starts a fresh session on a new issue. The server source keys Claude sessions by issue (`agentTaskSessions.taskKey = issue.id`), but this hasn't been seen working yet.
- The review stage reassigns to the Lead and wakes it.
- `serialize` holds a second run until the first ends.

Record what you see in `ops-notes.md` (at most five lines each).
