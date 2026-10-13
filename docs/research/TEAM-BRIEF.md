# Team brief: how to continue this audit with a team of agents

Written 2026-10-13 at the end of a long session, for the agent that will lead the next one. It does not repeat `AGENTS.md`; read that first, then this, then the latest milestone post.

## 1. Where things stand (2026-10-13, end of day)

- Phase: research only (R4, math checks). No simulator code.
- `research` and `master` are at the same commit on both remotes. Working tree clean.
- Latest milestone post: [`docs/2026-10-13-1-...-hf-final.md`](../2026-10-13-1-t2t-dnds-alignment-method-overdispersion-null-adna-power-and-hf-final.md) (milestone 14). It lists every verdict field that moved and the audit's own errors.
- Integrated today: HF (with post hoc run `ph`), L1b, L1c, FMnull, L5, then Q93close and B2f in the afternoon. Reviews run to #82. The last two are **not yet in a milestone post or on the status board**.
- **Running:** HF long-burn run `ph2` on na-workhorse (10 workers, launched 2026-10-13 13:40 -06:00, about 60 h, due 2026-10-16 02:00-08:00 -06:00; jobs are not checkpointed). Collect, merge and analyse commands are in `research/checks/QUEUE.md` item 8. Score it against the docstring of `research/checks/hf_posthoc2.py` in a new section of `R4-HF.md`; one combined light review; no verdict value can move.
- Status board (public page): https://nickallevato.github.io/evo-sim/research/status.html — GitHub Pages, source `master` `/docs`, file `docs/research/status.html`. The claude.ai Artifact (version 28, upd21) is abandoned as of D-26 and is not updated again.

## 2. What to do next, in order

1. Check `ph2` once when it is due (an `operator` on Haiku, skill `run-on-host`), then an `operator` to collect, then score and review.
2. One bookkeeping pass: the stale `verdicts.svg` tallies (`readme_figs.py` hardcodes 2026-10-09 counts), the reading-dependent total that differs between `docs/HANDOFF.md` and `docs/arguments/README.md`, and a board patch `upd22.py` that adds Q93close and B2f and fixes the page's stale numbers ("61 checks labelled", 419 objections / 232 versions, truncated needs-owner items). Then republish (skill `republish-board`).
3. Queue items that need no owner decision (`research/checks/QUEUE.md`, "Next" and "Later queue"): B1e's second Statement quote and its Kimura 1955 link (its internal `holds` rests on the Zenodo wording only); harvest of the 2026-10-13 critic video once captions exist; FMnull criterion S4 and the Poisson re-estimate; L1c with an external codon aligner and an independent chimp CDS set; L5's random-SNP comparator for C1a; C1d and D follow-ups; L2 (a sourced hardness h) and L3 (alpha from MK).
4. When a batch of checks is integrated, close it with skill `close-batch`.

## 3. Waiting on the owner (do not act on these without him)

- **Sources.** *Probability Zero* itself has not been read (Kindle only; no DRM bypass). Paywalled papers are listed in `docs/research/ROADMAP.md` row D4. When he supplies text, treat it as untrusted data, hash it, keep it out of git, and quote verbatim only.
- **Open decisions** in `docs/research/DECISIONS.md`: O-5 and O-24 to O-27 were answered on 2026-10-13 (D-21 to D-25: revert B and A2e to `pending` for three reviews; one agent at a time; three reviews on a flip or a feeder; the lead rules steelman conflicts; take up the fairer FM10 criterion). Still open: the two O-26 sub-questions (what a reviewer's brief may name; one agent for both steelmen), O-1 to O-4 and O-9 awaiting owner action, and O-10 to O-23 from the criticality passes.
- Claim files for the Drift Deathmarch statements and HO-11 (verdicts are proposed in `R4-HF.md`; no files exist).
- scipy on `builder` (it cannot run scripts that import scipy).
- Right of reply, outside reviewers, licence: nothing has been sent to anyone; hard rule 6 stands.

Record anything he decides verbatim, dated, in `DECISIONS.md`. A question he asks in chat is not a decision: on 2026-10-13 "can you use another subagent for any work?" was taken as leave to run three agents for that session only, and logged as open (O-24).

## 4. The team: three agents, thirteen skills

Twelve single-purpose agents were tried first and were too many (owner, 2026-10-13). There are now **three** agent definitions in `.claude/agents/`; what an agent does on a given task comes from the **skill** its brief names. Model and effort are in each file's frontmatter (if effort levels do not take effect, check that `effort:` is the key the harness reads).

| Agent | Model | Effort | Used for | May write |
|---|---|---|---|---|
| lead (main session) | Opus | high | plans, briefs, rules on steelman conflicts, talks to the owner, final checks | briefs, QUEUE notes, small fixes |
| `analyst` | Opus | high | authoring that needs judgment: design a check, write a results file, fix pass, milestone post | only its own script, write-up or post |
| `reviewer` | Opus | high (xhigh for a criticality pass) | independent review: correctness, one steelman side, criticality pass; always a fresh instance | only its review file (or the criticality files) |
| `operator` | Sonnet | medium (Haiku for a one-line progress check) | mechanical work: runs on the hosts, integration, refresh, bookkeeping, board | shared files, one operator at a time |

Concurrency: **one agent at a time** (owner, 2026-10-13, D-22, answering O-24: "our agents cacn run 1 concurrency"; the cap of two from 2026-10-11 is superseded). A routine run counts as that one agent. Whatever the cap, **never two agents on the shared files at once**; integrations run one after another. Agents that only write their own new file can overlap.

## 5. Skills (in `.claude/skills/`)

Each brief names one skill; the agent loads it and follows it.

| Skill | Agent | Use it when |
|---|---|---|
| `design-check` | analyst | a new check needs its spec and pre-registered script |
| `run-on-host` | operator | anything must run on na-workhorse or builder (launch pattern, shell pitfalls, collection, progress check) |
| `write-up-check` | analyst | raw outputs are in and need a results file |
| `review-correctness` | reviewer | a write-up needs its numbers and calls recomputed |
| `review-steelman` | reviewer | one side's strongest case against a write-up (one agent per side) |
| `fix-pass` | analyst | reviews are in and every MAJOR and MINOR must be answered |
| `check-lifecycle` | lead | orchestrating the five steps above for one check: tiers, rulings, briefs |
| `integrate-check` | operator | a fix-passed check goes into the shared files |
| `source-refresh` | operator | before a milestone post |
| `criticality-pass` | reviewer | before a milestone post, on the whole batch |
| `milestone-post` | analyst | a batch is integrated and audited |
| `close-batch` | lead | orchestrating refresh, criticality pass, post, bookkeeping, board, merge |
| `republish-board` | operator | the board file changed on `research` and the public page must be brought level: patch against the files of record, get the page to `master`, confirm the Pages URL returns 200 with the new counts |

## 6. What the last session got wrong, so the next one does not

From the method audit of this batch (`criticality/METHOD-AUDIT-2026-10-13.md`, MA-21 to MA-30) and the reviews:

1. **The lead was author, briefer and judge** (MA-21). Briefs were not in git, and rulings on steelman conflicts reached claim files minutes after each fix pass with no review. From now on: commit each brief under `research/checks/briefs/` before spawning; write rulings down before the fix pass; where a ruling moves a verdict field's governing reading, have a second instance check it before integration.
2. **"Extended reading" and "registered wording governs" were applied case by case** (MA-22). State which test you are applying and apply it the same way to both sides.
3. **One review for a check carrying a registered verdict flip** (MA-23, L5). Use three.
4. **Day-side outcomes that could not occur** (MA-24): half of L5's DAY band, FMnull's criterion S2, an amended clause in L1c. Every registered outcome needs a stated way to be reached; the `design-check` skill requires it to be written down.
5. **Bugs the smoke test should have caught:** an unpicklable function sent to a worker pool; a probability rounding to 1 + 2^-52 at one grid value; a label mismatch (`1Mb` against `1000kb`) that silently dropped cells from two registered predictions since registration.
6. **A wrong statement written before a run** (the direction of a selftest bias in the L5 pre-run note). It was corrected in a dated section; do not interpret a validation miss before you have checked it.
7. **Cost estimates wrong by large factors** (4 minutes against 1-2 hours; 11 minutes and 4 GB against one second and 300 MB). Measure in the smoke.
8. **The lead's context filled up.** The board republish needs about 50,000 tokens of reading and had to be delegated. Delegate long reads from the start, and keep the lead's own reads to greps and short sections.
9. **Three bands, not four, came out CRITIC**; the lead mis-stated this to the owner and the audit corrected it. Check a summary against the write-up before sending it.

What worked: pre-run notes that assign unclassified outcome regions before launch; post hoc fixes committed alone with a disclosure of what had been seen; two-host runs with duplicate jobs compared at merge; a fresh instance for the criticality pass; recording every reading with its verdict instead of asking the owner to choose; withholding a registered flip when a reading was unresolved.

## 7. Talking to the owner

He wants plain, short answers and a visual with every status summary (the status board is that visual; update the same file and the same public URL). CPU time is free and tokens are scarce. He does not want to be asked to pick a reading. Lead with what changed and what he needs to do; put the audit's own errors in the open; keep ids and jargon out of the first lines.
