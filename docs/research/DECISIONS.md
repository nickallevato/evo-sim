# Owner decisions log

*Started 2026-10-12 in answer to finding MA-03 (remedy 4) of [`criticality/METHOD-AUDIT-2026-10-12.md`](criticality/METHOD-AUDIT-2026-10-12.md).*

**How to read this.** The owner's decisions were given in chat, and the chat is not in the repository. Every row below was reconstructed from committed text: commit messages, `(user, date)` notes in `AGENTS.md`, `QUEUE.md`, the verdict rule file and claim-file comments. The "Decision" column is therefore an agent's record of what the owner said, not the owner's words. Where the committed text quotes or paraphrases the owner it is given in quotation marks with its file. The last column says how good the evidence is:

- **recorded same day**: a commit of that date attributes the decision to the owner or user.
- **recorded later**: the attribution appears only in a later commit.
- **unevidenced (chat only)**: the repository says a decision was made but not what was said, or the attribution rests on one agent's word with nothing else to check it against.

By that standard every row is weaker than a verbatim record. From now on, new rows should carry the owner's own words, pasted, with the date.

## Decisions

| # | Date | Decision | Where recorded | What it changed | Evidence |
|---|---|---|---|---|---|
| D-01 | 2026-10-07 | The owner supplies PDFs of Kimura 1962 and Kimura & Ohta 1969. | Commit `dea3da5` ("from user-downloaded PDFs") | Fidelity ledger rows for both papers verified against full text. | recorded same day |
| D-02 | by 2026-10-07 | The owner decides whether to buy *Probability Zero*; until then book-only claims are `secondhand`. | `PLAN.md` l.277 ("the user decides whether to buy it") | Book-only claims (Day 7, critics 8, allies 4 files) stay `secondhand`. Still open, see O-1. | recorded; no decision yet |
| D-03 | by 2026-10-09 | No outward actions without approval (no Wayback saves, contact, posting); no paywall bypass. | `AGENTS.md` hard rule 6, first written in `eb1943f` (2026-10-09 01:13); `HOWTO-refresh.md` l.9 | No author has been contacted; no right of reply. | unevidenced (chat only): the rule is not attributed to the owner in any commit |
| D-04 | 2026-10-09 | Rule RH: rhetoric is handled rhetorically. Tag each quoted statement `dialectic` or `rhetoric` before scoring; rhetoric is not literal-fact-checked and changes no verdict; "Rhetoric is answered with better rhetoric". | Commit `2d13149` (14:43, "user directive"); `R4-X1-verdict-rule.md` l.171, l.185 ("user directive 2026-10-09"); `docs/research/README.md` rule 8 | New section RH in the verdict rule after the X1 reviews; rhetoric ledger in `ledgers/slips.md` (RH-1 on); RH pass over all Statement quotes on 10-10 (`b2396ec`). | recorded same day |
| D-05 | 2026-10-09 | Token budget: never read the big files whole; model by task (Sonnet, Haiku, Opus); subagent reports of 300 words or fewer; do not poll long runs. | Commit `d439337` (16:17, "user directive"); `AGENTS.md` "Token budget (user directive, 2026-10-09)" | `AGENTS.md` cut from 13.1 to 8.2 KB; queue moved to `QUEUE.md`. | recorded same day |
| D-06 | 2026-10-09 | Review tiers: three reviews for load-bearing checks (those that move a ROOT-path node), one combined review for low-stakes checks. | Same commit and section as D-05 | From review #14 on, most checks get one combined review (24 single reviews against 8 three-review sets by the audit's count). | recorded same day |
| D-07 | 2026-10-09 | No computation on the workstation; heavy runs go to `na-workhorse`. | `AGENTS.md` "How to run" ("it ran out of RAM on 2026-10-09"); the sentence first appears in commit `d439337` | Run procedure (commit, rsync, launch over ssh, collect). | unevidenced (chat only): the text gives the reason, not an owner attribution |
| D-08 | 2026-10-09 | Workhorse limits: keep the host near full, at most 11 busy processes in total across agents, RAM under about 12 GB; launch asynchronously and return. | Commit `16d521d` (17:40, "user directive"); `AGENTS.md` step 2 ("user, 2026-10-09") | Launch procedure. | recorded same day |
| D-09 | 2026-10-10 | FM10 stays `pending` until Day releases his method. | Commit `ea8adb8` (17:48, "FM10 owner decision (pending until Day releases method)"); `QUEUE.md` l.10 ("flagged for the user") | FM10 internal verdict left `pending`. | recorded same day |
| D-10 | 2026-10-11 | The "remotely close" test for B9: grade Q104 `dialectic` if the literal claim is remotely close when mathed out under the most charitable reading, `rhetoric` if not. | `R4-B9.md` l.19 ("Owner decision (2026-10-11, in chat)"); commit `e95f0d3` (18:53, "owner rule 2026-10-11") | B9 pre-registered and run under this criterion with a 10x band; the review tightened the band to 3x. | recorded same day; the owner's wording is paraphrase |
| D-11 | 2026-10-11 | At most two subagents at a time. | Commit `366a217` (20:20); `AGENTS.md` "Current state" ("user, 2026-10-11") | Concurrency limit for agents. | recorded same day |
| D-12 | 2026-10-11 | A2e external: the owner accepts the scoping (`contradicted`, scoped). | `claims/A2e-ltee-as-ceiling.md` l.14 ("owner accepted the scoping 2026-10-11"); commit `3b55d1d` (20:34, "scoped contradicted PROPOSED, owner confirmation required") | A2e external moved from `contested` to `contradicted` (scoped) on a post hoc addendum with one combined review (#64). Audit MA-03 asks for this to be re-opened, see O-5. | recorded same day; the confirmation itself is chat only |
| D-13 | 2026-10-11 | Rule RD: where a verdict or RH tag depends on how a quote is read, do not pick one reading; record every plausible reading with its verdict. The verdict field takes the most charitable reading (rule C); such verdicts are counted separately. | Commit `e03f516` (21:20, "owner decisions 2026-10-11"); `R4-X1-verdict-rule.md` l.196-198; `QUEUE.md` l.64 ("Owner directive 2026-10-11") | Readings tables in B9, C7, B and three critic entries; B9 internal moved to `holds` on reading A. | recorded same day |
| D-14 | 2026-10-11 | Rule RH6: the "remotely close" test becomes the standing criterion for unclear RH tags on both sides; band fixed in advance (3x); all plausible readings reported. | Same commit as D-13; `R4-X1-verdict-rule.md` l.194 ("owner decision, 2026-10-11; standing criterion for unclear tags, both sides") | Applied in R4-B9, R4-RHclose, R4-RHclose-critics. | recorded same day |
| D-15 | 2026-10-11 | RD consistency fix approved: "most charitable" means the reading under which the quoted statement is most defensible (closest to literally true), not the reading that gives the speaker the best verdict. | Commit `3f881b0` (21:24, "owner-approved RD consistency fix"); `R4-X1-verdict-rule.md` l.198; `QUEUE.md` l.64 | **B internal `holds` -> `non-sequitur`** (B is load-bearing); A2e marked SCOPED, no longer reading-dependent. Committed four minutes after integration, with no review file (audit MA-03). | recorded same day; the approval itself is chat only |
| D-16 | 2026-10-11 | L5's review tier is one combined review, not the three its pre-registered docstring states. | `QUEUE.md` l.66 ("Process notes (owner, 2026-10-11)") | L5's tier lowered after registration; the script was not edited. | recorded same day |
| D-17 | 2026-10-11 | H8 extra replicates at K = 16k/64k skipped for now; H4 (provenance of Day's s and N_e for Hancock's "predict" reading) skipped. | `QUEUE.md` l.66 (same note) | Two queue items dropped. | recorded same day |
| D-18 | 2026-10-12 | A review of the method was commissioned as a "neutral third-party" review. | `criticality/METHOD-AUDIT-2026-10-12.md` l.5; commit `640aafa` | The method audit; quick fixes `255c9b8`. The audit states it is not third-party (written by a Claude instance inside the project's session). | recorded same day; commissioning words are chat only |
| D-19 | 2026-10-12 | Rule and vocabulary changes proposed by the audit are held back and prepared as proposals only; items that change no rule, vocabulary or verdict are carried out. | This file; [`criticality/METHOD-AUDIT-proposals.md`](criticality/METHOD-AUDIT-proposals.md); the commits that add them | `DECISIONS.md`, `criticality/METHODS-AND-LIMITATIONS.md`, `research/checks/PREREG-STATUS.md`, DN1-DN3 comments. | unevidenced (chat only): relayed to the agent that wrote this file as its brief |
| D-20 | 2026-10-13 | The audit is run out of Paperclip. The owner ticked seven of nine options on the plan card of task EVO-1, verbatim: "Hire three agents: operator, analyst, reviewer"; "Make the project and a new checkout"; "Daily watch of the runs and the hosts"; "Weekly source refresh"; "Weekly status report to you"; "Start the work that is already in the queue"; "Post a card with your open decisions". Left unticked: a second reviewer seat, and a backup of the 26 GB raw corpus off `na-workhorse`. | Paperclip task EVO-1; checkbox card resolved 2026-10-13 21:11 UTC; this row | Three standing agents hired against the role paragraphs in `.claude/agents/` (Operator on Sonnet, Analyst and Reviewer on Opus); this checkout at `/home/na/projects/evo-sim` on branch `research`, `origin` pushing to gitea and GitHub; three routines; the queued work started. The unticked options are not refusals, only not-now: O-26 keeps its interim handling (the lead writes each steelman ruling into the brief before the fix pass), and `sources/raw` stays single-copy on `na-workhorse`. | recorded same day; the option labels are the owner's ticked choices, pasted |
| D-21 | 2026-10-13 | **O-5 answered.** Question put to the owner, verbatim: "Two results moved in Day's favour on 2026-10-11 after only one review. The rule asks for three reviews for results of this importance. What do I do?" Owner's chosen option, verbatim: **"Put them back to `pending` until three reviews are done"**. | Paperclip task EVO-1; question card resolved 2026-10-13 21:22 UTC; this row; the O-5 row in "Owner replies to O-5 and O-24 to O-27" below | B internal (`non-sequitur`) and A2e external (`contradicted`, scoped) go back to `pending`, each with the superseded value and its basis kept in the claim file, until three reviews (correctness, steelman-day, steelman-critic) are done on each. Both reverts remove a Day-favourable value, so neither is applied by the lead alone: each is an integration task with a committed brief. | recorded same day; the option label is the owner's ticked choice, pasted |
| D-22 | 2026-10-13 | **O-24 answered.** Question put to the owner, verbatim: "How many agents may work at the same time? Your rule of 2026-10-11 says two. On 2026-10-13 three agents ran at the same time." Owner typed his own answer, verbatim: **"our agents cacn run 1 concurrency"**. | Paperclip task EVO-1; question card resolved 2026-10-13 21:22 UTC; this row; `AGENTS.md` "Current state"; `docs/research/TEAM-BRIEF.md` | The concurrency cap drops from two (D-11) to **one**: one agent works at a time, the rest wait. D-11 is superseded. The three that ran on 2026-10-13 are recorded as the excess MA-30 found, now closed by a lower cap rather than a higher one. Consequences: tasks are released one at a time, never in a batch; the operator's routines R1 and R2 count as an agent while they run; parallel steelman reviews are impossible, so the three reviews of a load-bearing check run one after another. | recorded same day; the owner's own words, pasted with his spelling |
| D-23 | 2026-10-13 | **O-25 answered.** Question put to the owner, verbatim: "A check is not marked important, but it changes an important result. How many reviews does it get?" Owner's chosen option, verbatim: **"Three reviews"**. | Paperclip task EVO-1; question card resolved 2026-10-13 21:22 UTC; this row; the tier rule in `AGENTS.md` | The tier rule gains a clause: a check whose registration carries a verdict-field flip, or whose node is a listed feeder of a load-bearing node (`R5-draft.md` 1.3), gets three reviews even where `hierarchy.yaml` does not mark it `load_bearing`. This is a tier change, so standing procedure item 3 applies: a criticality pass. It also supersedes D-16 (L5's tier lowered to one combined review, owner 2026-10-11), because L5 is the very case the question described. L5 has one review of the three; the lead's reading is that it gets the two missing ones before its C-external flip is integrated. The owner was not asked that sub-question and may overrule it. | recorded same day; the option label is the owner's ticked choice, pasted |
| D-24 | 2026-10-13 | **O-26 answered.** Question put to the owner, verbatim: "Two reviewers argue one for each side of a question. Who decides between them?" Owner's chosen option, verbatim: **"Me, the lead"**. | Paperclip task EVO-1; question card resolved 2026-10-13 21:22 UTC; this row; lifecycle steps 4 and 5 of `AGENTS.md` | The lead rules a Day-side / critic-side steelman conflict, as on 2026-10-13. The safeguard stays and is now the rule, not an interim: the ruling is written down and committed in the brief **before** the fix pass, and where it moves the governing reading of a verdict field a fresh reviewer task checks it before integration. The second reviewer seat is not hired (D-20). Two sub-questions of O-26 were not put to the owner and stay open: whether a reviewer's brief may name the issues the lead already suspects, and whether one agent may write both steelman reviews. | recorded same day; the option label is the owner's ticked choice, pasted |
| D-25 | 2026-10-13 | **O-27 answered.** Question put to the owner, verbatim: "The test for claim FM10 used a rule that was hard on Day's side. A fairer rule is written and ready. Do I use it?" Owner's chosen option, verbatim: **"Yes. Use the fairer rule"**. | Paperclip task EVO-1; question card resolved 2026-10-13 21:22 UTC; this row; `ROADMAP.md` B60 / C30 | Proposal (l) (`criticality/METHOD-AUDIT-2026-10-13.md` section 7b) is taken up under the rule-freeze procedure of O-6 (accepted 2026-10-12, "6-7 seem poltical an dits fine"): the written proposal exists; the 24-hour cooling-off runs from 2026-10-13 21:22 UTC, so the earliest pre-registration is 2026-10-14 21:22 UTC; then pre-registration, run, three reviews. It may move FM10 external and ROOT-FM external (both load-bearing) and FM3's annotation. FM10 **internal** stays `pending` under D-09 until Day releases his method; D-25 does not touch it. The data have been seen, which is a stated weakness of the re-score and goes in the write-up's limitations. | recorded same day; the option label is the owner's ticked choice, pasted |

### Decisions the repository mentions but does not record

- **"Owner choices" in the RHclose-critics fix pass** (commit `3c0dccb`, 20:45 on 10-11). The commit message names them; which choices the owner made is not stated there. unevidenced (chat only).
- **Compute hosts other than workhorse** (`builder` and others, named in `AGENTS.md` "Current state"). The limits on them are not in any committed file. unevidenced (chat only).
- **The 25% materiality line, the load-bearing list and the branch decomposition** were set by agents (rule file l.3-5, l.36; `hierarchy.yaml`; `PLAN.md`). No commit attributes them to the owner. They are listed here so that a reader does not assume they were owner decisions.

## Open decisions for the owner

These are the items the method audit says only the owner can settle, with the finding each comes from. Nothing below has been decided.

| # | Decision needed | Audit finding | If yes, what changes |
|---|---|---|---|
| O-1 | Buy *Probability Zero*, both editions, and supply the text. | MA-09 | The `secondhand` nodes are re-sourced. Until then the object of audit is "Day's Zenodo papers and blog posts". |
| O-2 | Give the audited authors a right of reply: send each named author the verdicts on his own claims with locators and a fixed reply window (the audit suggests 21 days), and publish replies verbatim beside the verdict. This needs **hard rule 6 lifted for that purpose**. | MA-10 | First contact with anyone outside the project. |
| O-3 | Recruit a human population geneticist for the five checks that carry the most (B3/B7 k = μ, B4a ancestral polymorphism, H8/HF cost, A2e, GAP-07 counts), and one reader from each camp as adversarial collaborators on the rule text and the load-bearing list, their disagreement recorded and not resolved by the owner. | MA-01, MA-10 | The first review not done by the auditing model family. |
| O-4 | Authorise a model from a different family for one review seat on load-bearing checks. | MA-01 | Reduces, without removing, correlated reviewer error. |
| O-5 | **Answered 2026-10-13, see D-21: "Put them back to `pending` until three reviews are done".** Revert B (internal) and A2e (external) to `pending`, or to their values before 2026-10-11, until each has had the three reviews that the tier rule requires for a load-bearing node. | MA-03 | Two load-bearing Day verdicts move back; both moves are in Day's favour until re-reviewed. |
| O-6 | Freeze the verdict rule (version it as rev 3; any later change is committed with the list of verdicts it would move before it is applied) and adopt a cooling-off rule: no rule change and no load-bearing verdict move is integrated on the day it is proposed. | MA-03, MA-10 | Ends same-day rule changes. Proposals (a) to (d) in `criticality/METHOD-AUDIT-proposals.md` would be the content of rev 3. |
| O-7 | Decide whether the audit keeps following Day's new posts or freezes its corpus at a date, with later material in an appendix only. | MA-11 | A stopping rule becomes possible; see proposal (e). |
| O-8 | Drop the Day-versus-critic comparative error rates and all Fisher p-values from the public pages (README, `HANDOFF.md`, status board); keep the sentence that the gap is not robust. | MA-06 | Public tallies change presentation; no verdict changes. |
| O-9 | Add a LICENSE, and a conflict-of-interest and priors statement in the owner's own words (who pays, relation to either camp, the project icon). | MA-19 | Fills the "Interests" paragraph of `criticality/METHODS-AND-LIMITATIONS.md`. |
| O-24 | **Answered 2026-10-13, see D-22: "our agents cacn run 1 concurrency" (cap of one, D-11 superseded).** Proposed 2026-10-13 by criticality pass vii. Is the cap of two concurrent subagents (D-11, `AGENTS.md` "Current state") raised permanently, and to what number? On 2026-10-13 three ran at once after the owner asked in chat whether another could be used; that exchange is not in the repository, and D-11 still reads two. | MA-30 | `AGENTS.md` and D-11 state the new number, or the cap of two is confirmed and the 2026-10-13 excess is recorded as a one-off. |
| O-25 | **Answered 2026-10-13, see D-23: "Three reviews".** Proposed 2026-10-13 by pass vii. Which review tier applies when a check's registration carries a verdict-field flip, or its node is a listed feeder of a load-bearing node, although `hierarchy.yaml` does not mark it load-bearing? L5 registered three reviews and the flip of C external; the owner's process note of 2026-10-11 set one combined review; one was done and found 7 MAJOR; the flip was withheld. | MA-23 | If three: the tier rule in `AGENTS.md` gains the clause (a tier change calls for a criticality pass, standing procedure item 3), and the owner says whether L5 gets its two missing reviews. If one: the L5 note becomes the rule. No verdict value moves either way. |
| O-26 | **Answered in part 2026-10-13, see D-24: "Me, the lead". The two sub-questions below (what a brief may name; one agent for both steelmen) were not put to the owner and stay open.** Proposed 2026-10-13 by pass vii. Who rules a conflict between the Day-side and critic-side steelman reviews: the author of the write-up (the lead, as on 2026-10-13), a separate instance that wrote neither, or the owner? With it: may a reviewer's brief name the issues the lead already suspects, or does one reviewer per check go in unbriefed; and may one agent write both steelman reviews (done for L1c to save tokens)? | MA-21, MA-26 | The lifecycle in `AGENTS.md` (steps 4 and 5) states the answer. Briefs are committed beside reviews in any case (no decision needed). No verdict moves. |
| O-27 | **Answered 2026-10-13, see D-25: "Yes. Use the fairer rule".** Proposed 2026-10-13 by pass vii. Take up proposal (l), a fairer Day-side criterion for FM10 (`criticality/METHOD-AUDIT-2026-10-13.md` section 7b), under the rule-freeze procedure of O-6, or leave FMnull's criteria as run with the S2 defect on record? | ST-10; MA-24; FMnull critic-side review K12 | If taken up: written proposal (exists), 24-hour cooling-off, pre-registration, three reviews. It could move FM10 external and ROOT-FM external (both load-bearing) and FM3's annotation. If not: nothing changes. |

*O-10 to O-23 were proposed by criticality passes ii to vi on 2026-10-12 and are carried in [`ROADMAP.md`](ROADMAP.md) section C (rows C14 to C26); they have not been entered in this table. O-24 to O-27 continue that numbering so that no id is used twice.*

## Owner replies to O-1 to O-9

Recorded 2026-10-12, in the owner's own words as relayed to the agent that wrote this section (the chat itself is not in the repository). The full reply, verbatim:

> "where buy pdf of prob zero? 1-4 we can get moving. 5 i dont get. 6-7 seem poltical an dits fine. 8 is fine? why? and 9 seems fine"

Nothing below goes beyond those words except where a cell says "parent agent's reading, owner to correct".

| # | Date | Owner's words | Recorded as | Status | What happens next |
|---|---|---|---|---|---|
| O-1 | 2026-10-12 | "where buy pdf of prob zero?" | Approved in principle; the owner will purchase. The owner asked where to buy a PDF. | Open: owner to purchase | Listings already recorded in [`sources/bib-day.md`](sources/bib-day.md) (grep `K-PZ`): Amazon Kindle ebook, ASIN B0GF8RQFY4 (1st edition; the 2nd edition is the same ASIN, an update of the Kindle edition); hardcover (Castalia AG, Amazon dp 3039440675, NDM Express, listed "sold out" on 2026-10-07); Signed Special Edition (leatherbound, NDM Express, $250, "sold out"). **No PDF or DRM-free edition is recorded anywhere in the repository.** The audit will not bypass DRM (hard rule 6). How the owner supplies the text once bought (a legitimate export, a scan of the owner's own copy, or typed excerpts) is for the owner to say. |
| O-2 | 2026-10-12 | "1-4 we can get moving" | Prepare the right-of-reply process. | Drafts only | Drafts in [`outreach/`](outreach/): `right-of-reply-day.md`, `right-of-reply-critics.md`. **Nothing is sent until the owner approves the exact text and the channel for each recipient.** Hard rule 6 stands until then. |
| O-3 | 2026-10-12 | "1-4 we can get moving" | Prepare the human-reviewer recruitment. | Drafts only | [`outreach/reviewer-brief.md`](outreach/reviewer-brief.md). Nothing is sent; no person has been approached. |
| O-4 | 2026-10-12 | "1-4 we can get moving" | Prepare the non-Claude review seat. | Drafts only | [`outreach/non-claude-review-packet.md`](outreach/non-claude-review-packet.md). No non-Claude model is installed on this machine; the owner must run the packet or provide access. |
| O-5 | 2026-10-12 | "5 i dont get" | The owner did not understand the question. | **Open: an explanation was asked for** | Not decided, not applied. B (internal) and A2e (external) keep the values they have. A plain-language explanation is in the agent report that accompanies this commit. |
| O-6 | 2026-10-12 | "6-7 seem poltical an dits fine" | Accepted ("fine"). | Accepted; interpretation below | **Parent agent's reading, owner to correct:** the verdict-rule freeze takes effect once the three audit-remediation proposals (a) `unexamined`, (b) `external_basis`, (c) the `contested` split in [`criticality/METHOD-AUDIT-proposals.md`](criticality/METHOD-AUDIT-proposals.md) are applied or declined. After that, any rule change needs a written proposal, a 24-hour cooling-off, and a three-review re-score of every load-bearing verdict it moves. |
| O-7 | 2026-10-12 | "6-7 seem poltical an dits fine" | Accepted ("fine"). | Accepted; interpretation below | **Parent agent's reading, owner to correct:** the corpus freezes at 2026-10-12. Material dated after that is logged in the refresh files but not scored until R5 is drafted, except (i) replies received under the right-of-reply process and (ii) code or data releases that a registered check is waiting on. |
| O-8 | 2026-10-12 | "8 is fine? why?" | Accepted ("fine"), with a question mark and a "why?". Applied now on the parent agent's instruction. | Applied; the "why" is answered here and in the report | Day-versus-critic comparative error rates and all Fisher p-values removed from README, HANDOFF, `arguments/README.md` and the status board (`research/tools/board/upd18.py`). Why: the rate compares unequal things (volume, claim precision, share checked, routing; MA-06), and the test assumes independent exchangeable units that claim nodes are not. Per-side raw counts stay. If the owner wanted the question answered before this was applied, the change can be reverted with `git revert`. |
| O-9 | 2026-10-12 | "9 seems fine" | Accepted in principle. | Waiting on the owner | Drafts in [`outreach/coi-and-licence-draft.md`](outreach/coi-and-licence-draft.md). The licence choice and the conflict-of-interest facts are still needed from the owner; no LICENSE file has been added. |


## Owner replies to O-5 and O-24 to O-27

Given 2026-10-13 on the question card of Paperclip task EVO-1 and resolved at 21:22 UTC. Unlike every row above, these are **not** reconstructed from commit text: the questions and the owner's answers are stored by the control plane with the owner's user id and a timestamp, and the option labels below are pasted from that record. Four were ticked options written by the lead in plain language; O-24 the owner typed himself.

| # | Question as put to the owner, verbatim | Owner's answer, verbatim | Recorded as | What happens next |
|---|---|---|---|---|
| O-5 | "Two results moved in Day's favour on 2026-10-11 after only one review. The rule asks for three reviews for results of this importance. What do I do?" | "Put them back to `pending` until three reviews are done" | D-21 | B internal and A2e external revert to `pending`, superseded values kept in the claim files; three reviews each, run one after another under the new cap; the stale "most charitable to Day" comments in C7 and B9 (ROADMAP B7) are fixed in the same pass. |
| O-24 | "How many agents may work at the same time? Your rule of 2026-10-11 says two. On 2026-10-13 three agents ran at the same time." | "our agents cacn run 1 concurrency" | D-22 | Cap of one. `AGENTS.md` and `TEAM-BRIEF.md` updated; tasks released one at a time; routines count against the cap. |
| O-25 | "A check is not marked important, but it changes an important result. How many reviews does it get?" | "Three reviews" | D-23 | The tier rule in `AGENTS.md` gains the flip-or-feeder clause; a criticality pass is due for the tier change; the lead reads it as giving L5 its two missing reviews before the C-external flip is integrated, which the owner may overrule. |
| O-26 | "Two reviewers argue one for each side of a question. Who decides between them?" | "Me, the lead" | D-24 | Lifecycle steps 4 and 5 of `AGENTS.md` say the lead rules, writes the ruling in the brief before the fix pass, and sends a fresh reviewer at it where it moves a verdict field's governing reading. Two sub-questions stay open. |
| O-27 | "The test for claim FM10 used a rule that was hard on Day's side. A fairer rule is written and ready. Do I use it?" | "Yes. Use the fairer rule" | D-25 | Proposal (l) runs the freeze procedure: cooling-off to 2026-10-14 21:22 UTC, then pre-registration, run, three reviews. FM10 internal stays `pending` under D-09. |

**What these answers did not settle.** The lead put five questions, not seven: the two O-26 sub-questions (may a brief name the issues the lead suspects; may one agent write both steelman reviews) were left out to keep the card short, and the O-25 sub-question about L5's two missing reviews was not asked. The lead's readings of all three are stated in D-23 and D-24 and are marked as the lead's, not the owner's.

**Correction to the premise of the O-5 question (recorded 2026-10-13 by the lead).** The question put to the owner said "Two results moved in Day's favour on 2026-10-11", and the effect column of D-21 says "Both reverts remove a Day-favourable value". **Both statements are wrong, in the same direction.** On 2026-10-11 B internal moved `holds` → `non-sequitur` and A2e external moved `contested` → `contradicted`: both moves were **against** Day, and each revert to `pending` therefore removed a value unfavourable to him. For B there was a Day-favourable step (`pending` → `holds`, the RHclose integration) but it stood for four minutes before D-15 superseded it; that intermediate step is the only thing the question's wording fits. Three of the six O-5 reviews found this independently (`REVIEW-R4-B-internal-correctness-2.md` MINOR-10, `-steelman-day.md` F6, `REVIEW-R4-A2e-external-steelman-critic.md` MINOR-3). **D-21 stands**: the tier rule asks for three reviews whichever way a value moved, so the owner's answer does not depend on the premise. The correction is recorded rather than quietly fixed, and the owner was told in the task thread of EVO-1. No public account of these reverts may say they removed a Day-favourable value.

## Owner replies on publication and concurrency

Given 2026-10-13 on a second question card of Paperclip task EVO-1 and resolved at 22:33 UTC. As with D-21 to D-25, the questions, the owner's answers and the timestamp are stored by the control plane with the owner's user id; the option labels below are pasted from that record.

| # | Question as put to the owner, verbatim | Owner's answer, verbatim | Recorded as | What happens next |
|---|---|---|---|---|
| O-28 | "The new board page is committed to the repository (`docs/research/status.html`, commit `4df7485`), but no agent in this runtime can write to the claude.ai artifact. The artifact page still shows the old numbers. How do you want to publish the board?" | "Publish a static page" | **D-26** | The board is published as a static page, not as a claude.ai artifact. GitHub Pages is already enabled on `nickallevato/evo-sim` (legacy build, source `master` `/docs`, HTTPS enforced), so the board's public address is **https://nickallevato.github.io/evo-sim/research/status.html** and it already returns 200. What is served there is `master`'s copy, which is upd21-era and therefore stale. Publication from here is a two-step standing procedure: (i) a board patch on `research` that brings the page to the files of record, (ii) the page reaching `master` so Pages rebuilds. The claude.ai artifact is abandoned as the board's home and is not updated again. |
| O-29 | "Your rule D-22 lets only one agent run at a time. Eleven reviews are in the queue. One at a time makes the work about two times slower, but the cost per hour is lower and the risk of two agents in the same file is zero. Do you want to keep the limit of one?" | "Keep one" | **D-27** | D-22 is confirmed with the cost stated and understood. The cap of one stands in `AGENTS.md` and `TEAM-BRIEF.md`; it is no longer a provisional reading. Routines count against it. The lead releases one task at a time. |

**A correction the lead owes the owner on D-26.** The board committed at `4df7485` was written *before* the O-5 revert (`2740ded`) and therefore still shows B internal as `non-sequitur` and A2e external as `contradicted`. Publishing it unchanged would put two superseded verdicts on a public page. The board patch in step (i) above must be re-run against the current files of record first; that is the content of the next released task.

## Lead decisions and incidents, 2026-10-14

**The cap of one broke twice, and parking was the wrong mechanism (incident, 2026-10-13
23:50 to 2026-10-14 01:10 UTC).** D-22/D-27 allow one agent run at a time. On two separate
occasions three and then two runs were live at once: EVO-10 with two runs on EVO-21
(00:23), then the B1e-Q2 fix pass with the L5 ruling check (01:0x). Nothing released them.
The lead's mechanism was **parking** — moving a queued task to `backlog` — and parking does
not hold: when a task's own lifecycle blocker reaches `done`, the runtime re-readies the
task and starts it. Parking also cannot stop a run already in flight; there is no
run-cancel endpoint available to the lead, which was checked twice.

**Mechanism adopted in its place: a lane token.** A permanent issue, *LANE TOKEN - release
gate, never close* (`36f51809-27fb-47ab-9376-c9932d50f151`, status `backlog`, assigned to
the lead), is carried in the `blockedByIssueIds` of every queued worker task. Because the
token is never `done`, `issue_blockers_resolved` can never fire for those tasks, so no task
can start itself when its real blocker finishes. The lead releases work by removing the
token id from exactly one task. 20 of the 27 queued worker tasks carry the token as of
01:15 UTC; the remaining 7 are downstream of tasks that do carry it, so every lane head is
held. They are gated on the next wake (a run may make at most 20 cross-issue writes).

**Four board discrepancies, found during the publication pass (EVO-68) and still open.**
Recorded here so they are not lost: (i) the Rule RD paragraph says "7 reading-dependent
verdicts" against a headline of 15 — the standing `HANDOFF.md` / `arguments/README.md`
disagreement, now visible on the public page; (ii) B's reading-dependent field count was
not recounted after the O-5 revert; (iii) the ROADMAP "Counts" table is stale; (iv) the
`republish-board` skill still documents the abandoned claude.ai Artifact route that
`AGENTS.md` and `TEAM-BRIEF.md` no longer carry. All four are bookkeeping, none moves a
verdict.

**B internal: the lead's ruling was overturned by the D-24 check and re-ruled.** The fresh
reviewer (EVO-73, `ccdb989`) found B-R4's ground false on HL's text. The lead accepts it,
withdraws B-R4 and B-R5 as governing, and rules the field to `holds` scoped to the census
ceiling at G, with the node-level claim taking RH3 — a **Day-favourable** move on a
load-bearing field, made under the owner's charity rule (RD, 2026-10-11). The reasoning is
B-R11 to B-R19 in `research/checks/briefs/O5-reviews-reviewer.md`, Addendum 2, committed
before the fix pass. One further fresh-reviewer check is bounded by B-R19; if it returns a
BLOCKER the question goes to the owner rather than to another reviewer.

## D-28. The owner stops taking registered owner questions back (2026-10-14)

Put to the owner on the EVO-1 question card as the L5 / claim C pre-registration's own
MIDDLE clause: "Day says the Modern Synthesis needs about 15,500 fixations in each
7,000-year period. He does not say how strong the selection on those fixations is. Day's
own data can only show such fixations if the selection strength s is about 0.03 or more.
Weaker fixations are invisible to his test, so a result of zero tells you nothing about
them. Does Day's argument need those 15,500 fixations to be strong (s of 0.03 or more)?"

Owner's answer, verbatim (control plane, resolved 2026-10-14 01:34 UTC, stored with the
owner's user id):

> "if you need to ask me then you need to decide or leave it open and / or explore both
> possible sides or interrpetations"

**Standing rule.** A clause in a registration that names "an owner decision" is a flag, not
a stop. The lead rules on it, or records every plausible reading with its verdict and lets
none of them set the field; in both cases the reasoning is written and committed before any
fix pass, and the D-24 fresh-reviewer safeguard applies where the ruling decides a governing
reading. A question reaches the owner only where it is a question of **policy or of outward
action** — what the audit's rules should be, what may be published, what may be spent — and
not where it is a question of **fact or of reading**, which is the audit's own work. This
supersedes the practice in L-R6, where the lead sent a reading question to the owner because
the registration had labelled it one. It does not touch hard rule 6 (no outward action
without the owner's word) or the rule-freeze procedure of O-6.

**Applied the same day, in full, in the open.** L-R11 to L-R16
(`research/checks/briefs/L5-reviews-reviewer.md`, Addendum 2) answer the question **no**:
Day attaches no s to the comparator and the two s values he does state (1e-3 at Q44; 0.01 at
the Q26 note) are below s\*; the mainstream model's strong class covers about 1.26
substitutions per window, not 15,556; and the reading needs roughly 28,000 to 37,000
concurrent sweeps against Day's own published "approximately 230 simultaneous sweeps" (Q25).
The best case for "yes" — that Day's test is vacuous unless the substitutions are strong, so
a charitable reader should supply the strength — is stated in full at L-R12 and refused
because rule RD takes the most defensible reading of the **quoted statement** and is "not the
reading that yields the best verdict for the speaker". Under the owner's "explore both
possible sides", R-d is **kept on the record with its verdict** (`supported`, does not set
the field) in claim C's Readings table, with what would reopen it. No verdict field moved on
the ruling commit; integration is gated on one bounded D-24 check.

## The B1e-Q2 fix pass was silently reverted by the lead's own commit, and is restored

**Incident, 2026-10-14.** Commit `9f863fd` (the B internal re-ruling) was made from a second
worktree on the `research` branch while the shared checkout at `/home/na/projects/evo-sim`
held the EVO-11 B1e-Q2 fix pass staged and uncommitted. The worktree carried the
pre-fix-pass blob, so `9f863fd` committed `research/checks/results/R4-B1e-Q2.md` **back** to
its `e2bc2f1` state: 87 lines answering 11 MAJOR and 10 MINOR review items vanished from
HEAD while surviving only in the shared checkout's index. Restored byte-identical to
`3c9df34`'s blob in commit `34535d2`, pushed to both remotes. Nothing was re-authored and no
verdict value moved.

This is the hazard the 01:08 UTC report named and claimed to have cleaned; the claim was
wrong — the cleanup restored the index, not HEAD, and HEAD was the thing that had lost the
work. **Standing rule:** the lead does not commit to `research` from a second worktree while
a shared checkout is dirty. Either commit in the shared checkout, or give the worktree a
detached head and cherry-pick. Every commit made from a worktree is checked with
`git show --stat` against the files it was meant to touch before it is pushed.

**Addendum to the lane-token mechanism (2026-10-14).** A task created with
`blockedByIssueIds` set is returned by the control plane with status **`todo`**, not
`blocked`: the blocker is attached but the status is not recomputed on creation. A task left
in that state is startable, which is the likeliest root cause of the earlier
"nothing released them" incidents. Creating a gated task therefore takes **two** writes -
create, then `PATCH {"status":"blocked"}` - and the second is verified by a GET, not assumed.
Releasing takes two writes in the other order: clear `blockedByIssueIds`, then set `todo`;
a single combined PATCH is rejected with 409 "Issue follow-up blocked by unresolved
blockers". The gate was also audited task by task on this wake: of 36 blocked tasks, every
lane head carries the token, and the one task that did not and would have started itself
when `ph2` landed (EVO-77) now does.

## 2026-10-14 — verdict scopes do not survive the tooling (lead ruling B-R20/B-R21)

Every scope and qualifier this audit has attached to a verdict is a **YAML inline comment**
in the claim front matter (A2e's `external: pending   # SUPERSEDED ... SCOPED ...` is the
pattern). `lint_research.py` parses that block with `yaml.safe_load` (l.25-30), which
discards comments. So the scope reaches no consumer: not the linter, not `hierarchy.yaml`,
not the public board. Only the bare value travels. Found by the EVO-80 fix pass (its finding
6g) and verified at the source by the lead before being recorded.

**Standing rule.** A verdict value that carries a scope must also carry a machine-readable
`verdict_scope:` entry keyed by field name; `lint_research.py` errors when a scoped value
has none, and carries it into `hierarchy.yaml`; the board renders value and scope together
or renders neither. Until that is in place, **no board publication may show B internal or
A2e external**, and B internal's scoped `holds` may not be integrated — independently of
what the B-R19 bounded check returns. A bare `holds` on a public page is a Day-favourable
claim the audit does not make. The board as published today shows both fields as `pending`,
which is bare and correct, so nothing public is currently wrong and nothing is being pulled.

This is a tooling decision, not a verdict decision, so it is the lead's under D-28.

## 2026-10-18 — the 14 unresolved verdict scopes, ruled (lead ruling B-R22..B-R30)

EVO-84 made verdict scopes machine-readable and populated 12 of them verbatim. It left **14
fields** where `lint_research.py` sees a scope in the comment and finds no `verdict_scope`
entry, and it gated `--write-hierarchy` behind them. All 14 are ruled below (EVO-91). Every
question in them is a question of **reading or of tooling**, not of policy or of outward
action, so they are the lead's under D-24 and D-28; none went to the owner.

**Nothing moved.** The lint's verdict tallies are character-for-character what they were
before the ruling (`internal:holds=133`, `external:contested=116`, and so on), and the
regenerated `hierarchy.yaml` is node-for-node identical to the committed one outside the
`verdict_scope` key (checked by loading both and comparing every node with the key dropped).
Each ruled line is composed from the claim file's own comment: it names the governing reading
already on the record and adds no reasoning. **No governing reading moved, so the D-24
fresh-reviewer safeguard is not triggered.**

**B-R22. A `pending` value has no scope (A2e external, B internal — the B-R21 pair).** In both
files the SCOPED / reading-dependent text describes the value D-21 **superseded**; the current
value is `pending`. Two ways to clear the lint were available: lift the superseded text out of
the front matter so the comment scan stops seeing it, or record the ruling as data in place.
The second is taken. Moving the text would move history out of the place reviewers read it,
and the file of record should say what was pulled. The entry therefore reads `none:` (B-R23)
and states that the scope belongs to the superseded value and may not be shown as a current
one. **This does not lift the B-R20/B-R21 hold.** The tooling half of the hold's condition is
now met — scope is data, the linter errors without it, `hierarchy.yaml` carries it, the guard
checks the page — but publication is outward action, so showing B internal or A2e external
still needs the owner's word under hard rule 6, and B internal's scoped `holds` is still
un-integrated and still behind D-21's three reviews.

**B-R23. The `none:` convention.** A `verdict_scope` entry beginning `none:` means "the current
value carries no scope", and must say why. The entry is still **required**: the ruling belongs
on the record as data, not as an absence that the next reader has to re-derive. No consumer may
render a `none:` entry as a scope on the value. Implemented as `NO_SCOPE_RE` in
`lint_research.py`, honoured by `scope_guard.py`. Four fields use it: A2e external and B
internal (B-R22), B5 external and ROOT-PG internal (B-R27).

**B-R24. A4d internal: the bare "SCOPED" tag now has its sentence.** The comment tags the value
SCOPED and never says what the scope is; the scope is in the finding. Ruled: `holds` is scoped
to what a token search can establish — the absence of the symbol `d` and of any d multiplier on
the generation count in the re-fetched, sha256-matched MITTENS 3.0 (`22bb4ef8…`), reading (c)
governing — and **not** to the absence of an overlap correction, which survives by citation
inside the s8.6 rate. Reading (a) stays an extended reading and may not set the field or the
headline (rule RD line 202). This is the distinction the VID-01-score fix pass already drew in
prose; it is now data.

**B-R25. The nine multi-reading fields.** B1e fidelity, B1e external, B9 internal, C external,
C7 internal, C7 external, DN1 external, DN6 fidelity, FM3 external record several readings and
no single plain sentence to copy. Ruled: where the comment offers no sentence, the scope line is
written in one fixed shape — **the governing reading first, then every other reading with its
verdict and its status** (extended, untested, not field-setting, carried at another node) —
composed only from what the comment already says. No reading is added, dropped or re-ranked.
This is deliberately a *restatement* and not a *decision*: the alternative, picking one reading
per field as "the" scope, would move governing readings on nine fields, three of them on
load-bearing branches, which is a verdict decision and not a tooling one.

**B-R26. The lint test is not narrowed.** `SCOPE_RE` matching prose is generous on purpose. A
false positive costs one recorded `none:` line; a false negative puts an unscoped value on a
public page, which is the failure B-R20 found. Narrowing the test on phrases like "unchanged
under every reading" would put the gate back into prose parsing — the thing that failed. The
test stands as EVO-84 wrote it.

**B-R27. B5 external and ROOT-PG internal are not scoped values.** In both, the
reading-dependence is on a **rhetoric tag** — Mansfield RH-18 on B5, quote 3 on ROOT-PG — and
the comment itself says the verdicts are unchanged under every reading. These are the two
probable false positives EVO-84 flagged, and they are false positives. Under B-R26 the test is
not changed; under B-R23 each gets a `none:` entry naming the tag.

**B-R28. The board scope guard's threshold was wrong, and is re-cut.** Asked whether the guard
can be leaned on: not as written on 2026-10-17. It reported **22 of 22** page entries as
violations and every one was noise. Three causes: it accepted the *field name* near the claim
id and then looked for the value anywhere in the same `<li>`; it counted `pending` as a stated
value, so prose like "Open owner decisions … O-1 … pending" matched; and one-letter ids matched
ordinary text and reading labels ("B (literal equality) non-sequitur" is *reading* B). Re-cut:
the value must sit within 120 characters of the id with no sentence break; `pending` and `n/a`
are not values; a one- or two-character id counts as a claim reference only where it opens the
entry or carries a field name before the value; `none:` scopes require nothing of the page; and
the report is now two-tier — **VIOLATION** (exit 1) where a scoped value is stated with no
scope cue at all, **REVIEW** (exit 0) where the entry carries a scope in its own words but not
the verbatim line, because the page is hand-written prose and will paraphrase. A verbatim
substring test on prose reported nine entries that do state their scope. On the live page the
re-cut guard reports 3 violations and 9 review lines.

**B-R29. The EVO-84 `hierarchy.yaml` stands, and is regenerated anyway.** It was written by a
run that bypassed the error gate, so it was not trustworthy on its face. Checked rather than
assumed: outside `verdict_scope` it is identical to the file the clean run now writes, node for
node. So nothing was wrong in it; it was only missing the 14 entries. It is regenerated under a
passing gate in the ruling commit (12 scope entries -> 26), which is now the file of record.

**B-R30. Finding, not yet fixed: the published board states three scoped verdicts bare.** The
re-cut guard's three violations are one bullet — "H, H8, H5 external stay contested" in the
reviews #66-#69 entry — which gives no hint that all three are conditional on K (tested to
64,000) and on the survival horizon. This is the B-R21 hazard on the live page, in the critics'
favour this time rather than Day's. It is **not** patched here: `status.html` is patched by
`board/upd<N+1>.py` as its own task against the current files of record, and the guard now
blocks publication until it is. Queued in `research/checks/QUEUE.md`.

## 2026-10-18 — the release order of the seven queue heads (D-29)

A sequencing decision, not a verdict decision, so it is the lead's under D-28. Recorded
because it governs the next six releases and because the earlier lane note that "the queue is
empty" (2026-10-14) was wrong and should not be the standing record.

**The state it rules on.** Seven chain heads are gated on nothing but the LANE TOKEN, i.e.
each is releasable the moment the lane frees: EVO-12 (integrate B1e-Q2), EVO-15 (FMnull-S4),
EVO-22 (L1c-b), EVO-29 (L5-C1a), EVO-36 (C1d-D), EVO-50 (L3), EVO-77 (L2 Open 7). Everything
behind them is gated on its own predecessor as well, so the chains self-order; only the order
*among the seven* was open. Five of the seven put work on `na-workhorse`.

**D-29a. Two scarce resources, not one, and they are not the same resource.** D-22/D-27 cap
*agent runs* at one. It does not cap the compute host, which runs on its own once a job is
launched — `ph2` cost 591 CPU-h of host time and almost none of it needed an agent awake. The
cost of getting this wrong is measured in days: a launch-and-collect task that sits
`in_progress` waiting on the host holds the single agent lane for the whole run, so every
cheap bookkeeping task behind it waits on a job that needs no agent at all. Ruling: **the host
gets loaded first, and the lane is not held while the host works.** Order below follows from
that and nothing else.

**D-29b. The launch half and the collect half are separate lane occupants.** The five compute
tasks are each written as "launch and collect". They are not run that way. The released agent
checks `uptime`, rsyncs the pre-registered script, launches with `< /dev/null`, records the
hostname and md5s in `research/checks/results/raw/<x>.host`, reports, and **hands the lane
back** — it does not wait. The collect becomes its own task, created at that point and woken
when the run is done, which is the pattern `ph2` already proved (routine R1 moved EVO-4 from
`backlog` to `todo` when the run finished). No agent polls a running job.

**D-29c. The order.** FMnull-S4 (EVO-15) first: it is the only *load-bearing* tier among the
launches whose design is pre-registered and whose inputs are settled, it feeds the FMnull
criteria that D-25's fairer FM10 rule bears on, and its cooling-off expired on 2026-10-14. Then,
while the host is busy, the lane takes the work that needs no host: EVO-12 (integrate B1e-Q2,
shared-file bookkeeping, closes a chain whose fix pass is already done and unblocks EVO-7's
check) and EVO-92 (the B-R30 board patch, which the re-cut guard now blocks publication on).
Then the remaining host work, as the host frees: EVO-50 (L3, load-bearing, but likelier to
stall on sourcing public polymorphism data than on compute), EVO-29 (L5-C1a), EVO-22 (L1c-b),
EVO-36 (C1d-D), EVO-77 (L2 Open 7, tool validation, lowest stakes of the five and it moves no
verdict field on its own). This order is a default, not a freeze: a result that moves a
governing reading re-opens it.

**What D-29 does not touch.** No verdict field, no tier, and not the B-R20/B-R21 publication
hold, which stands on its own terms — its tooling condition is met as of B-R22..B-R29, but
showing B internal or A2e external is outward action and needs the owner's word under hard
rule 6.

## 2026-10-18 — the four open B1e-Q2 rulings (lead rulings B-R31..B-R34)

Verdict rulings under D-24 (where the Day-side and critic-side steelman conflict, the lead
rules and writes the ruling into the brief, committed, before the fix pass — here, before the
remainder of the integration, the fix pass having closed with the conflicts recorded and
unchosen). Full reasoning, with the basis for each, is in
`research/checks/briefs/B1e-Q2-analyst.md`, section "Lead rulings, 2026-10-18"; this section
is the record of what was ruled. Paperclip: EVO-12, parent check EVO-7, reviews EVO-10, fix
pass EVO-11.

**B-R31 (ruling 2: R-A plausibility; D3 against SC4).** R-A stays a plausible reading of QB
and keeps governing. RD ranks readings by the defensibility of the quoted statement, not by
what the author meant, and Day's own sentence "The diffusion has to be provided as an assumed
condition that is supplied in order to solve the equation." (blog .txt l.11) states R-A's
gloss in his own words. R-B keeps its row — fidelity `misread`, external `contradicted` —
marked plausible and not field-setting. SC4's conditional fidelity move does not fire; QB's
fidelity stays `partial`. The withdrawn "not because the author meant it" stays withdrawn.

**B-R32 (ruling 1: R-A external; D1 `supported` against SC1 `contradicted`).** `contradicted`,
moved from the registered `contested`. Basis, registered items only: P3 with P4 give the
classical solution's own integrated outflux at x = 1 as ∫x p^I, computed from r alone — for a
one-copy start, the 1/(2N) itself; P5's alternative splits need non-local booking, which is a
mis-booking of the flux and not a rival model of fixation; what the diffusion takes from
outside is the meaning of its own absorbing boundaries, which Day's governing Zenodo sentence
itself names. P6b is **out** of this field's basis (it tests Wright-Fisher exclusivity, which
R-A's gloss sets aside; all three reviews asked for this). `supported` is barred by D1's own
appended derivation (the weak form of (7) on [0, 1] yields both conservation laws from φ = 1
and φ = x) and by SC3 (iii) (the second law is conservation of ϕ, the diffusion's own
stationary backward equation): the input is not imported from any discrete process. What
survives for Day: P5 as an identity that hit for him, with its booking qualifier; fidelity
`partial`, not `misread`, on Chalub's own framing (C1, C2, C13); and the presentation point
(D5, SC8). **A fresh reviewer checks B-R31..B-R33 before the rest of the integration is
written** (D-24). The escalation clause does not fire: B1, B1a, B2 and B are untouched.

**B-R33 (ruling 1c: two Statement quotes in one field; SC6, D1 "Open").** The conjunction
rule: a claim asserts all of its Statement quotes, so each verdict field takes the value of
its weakest conjunct, and the `verdict_scope` entry names the carrying quote first and then
every other quote with its value and status (B-R25's shape, extended from readings to
quotes). Weakest first: external `contradicted` < `contested` < `supported`; fidelity
`misread` < `partial` < `accurate`; internal `arithmetic-error` / `non-sequitur` < `holds`.
`unverifiable`, `untestable` and `pending` are not points on these scales; an unscored
conjunct is recorded in the scope line. Taking the better conjunct was SC6's objection
(it masks a verdict already reached); averaging to `contested` would invent a dispute the two
quotes do not have. Cost recorded against the rule: it makes a node's field worse as quotes
are attached, so the countermeasure is the split — where a claim's Statement quotes assert
propositions that do not stand or fall together, the claim is split into one node per
proposition. B1e is such a candidate and is **not** split in EVO-12 (a split touches
`hierarchy.yaml`, the argmap and the board); the lead files it separately. Applied to B1e:
external `contested` → `contradicted` (carrier QB), fidelity `partial` unmoved (both
conjuncts `partial`), internal `holds` unmoved but its scope line rewritten, the blog quote
now having been examined. As a *general* clause of the verdict rule this is a rule change and
runs the O-6 freeze procedure (this section is the written proposal; 24-hour cooling-off; a
three-review re-score of any load-bearing verdict it would move). It moves none here: B1e is
`load_bearing: false`. Until the freeze procedure completes, no other claim's fields are
recomputed under it.

**B-R34 (the P7 ruling).** Option (b): the registered P7 value item was mis-specified by the
audit. The call stays **MISS, band X** in every tally as the audit's own miss, and the
licensed move (B1e fidelity `partial` → `misread`) is void and not applied. Basis, registered:
coef_err 0.0 over n = 0..200; the three binary-exact x agree to ≤ 1.12e-138; the committed
script compares `mp.mpf(x)/4` from a Python float against `F_dec(str(x))`, an exact decimal
(C2, reproduced by two reviewers from the float offsets alone). Second and independent ground
(D2): band X maps to `misread`, which the rule defines as the cited source being in hand and
contradicting the reading; a mismatch with the *audit's* B2f series could only show that
B2f's credit is not extended. Precedent adopted in SC7's symmetric wording, verbatim: "a
registered band reached only through an audit argument mismatch, shown by registered items,
is ruled mis-specified whichever side it favours." Option (c) declined. (b) voids the X move
and does **not** register the E line: the identity of Chalub's b(t; x0)/x0 with the
eigen-series B2f used stays post hoc and descriptive, credited to both sides, setting no
field. P8 stays band U and the Chalub-link fidelity stays `partial` on the ledger basis.

**What these four do not touch.** No load-bearing node, no tier (C1 settled the tier
independently: three reviews, done), nothing on a published page, and not the B-R20/B-R21
publication hold.

## 2026-10-18 — EVO-94 rejected B-R32's value; re-ruled (lead ruling B-R35)

The D-24 fresh-reviewer check of B-R31..B-R33 (`research/checks/results/REVIEW-R4-B1e-Q2-ruling-check.md`,
EVO-94, 009d5b6) confirmed **B-R31**, confirmed **B-R33**'s rule with two corrections
(RC-5, RC-6), and **rejected B-R32's value** on one MAJOR (RC-1), with MINORs RC-2, RC-3 and
NOTEs RC-4, RC-7, RC-8. It found no wrong number.

**B-R35 (re-ruling of B-R32).** The lead accepts RC-1 in full. **QB's external value under
R-A is `contested`, the registered value; no verdict value moves anywhere in B1e.** RC-1 is
right on two independent grounds. (i) B-R32's basis (3) argued that the most defensible
reading of "the mathematics" cannot be narrower than a diffusion with absorbing boundaries —
which is R-B's registered gloss, not R-A's "PDE (7) on the open interval". B-R32 therefore
named R-A as governing and scored the field on R-B's content, a re-ranking of readings that
B-R31 and RD forbid; RC-8 states the inconsistency (B-R31 and basis (3) cannot both stand),
and dropping (3) is the fix that keeps B-R31. Without (3), registered items (1) and (2) show
that the number is the classical solution's own outflux and that a free split needs non-local
booking, but they do not exclude non-local booking under a reading whose subject is (7) on
the open interval. (ii) Consistency of scrutiny: the Zenodo conjunct in this same claim is
`contested` because it is false under one premise and true under another, and A3a external is
`contested` with a `contradicted` reading recorded beside it. `contradicted` here would hold
Day's quote to a stricter standard than the audit applied to the sentence in the same file
(hard rule 1).

Also ruled: basis (3) is **withdrawn** as a basis for QB's reading (RC-2 — Q288 is the Zenodo
wording of 2026-10-13, QB is the blog of 2026-08-23, and rule S scores a node on its own
quotes; (3) survives only as context bearing on R-B). `supported` **stays barred**, re-based
on **P3 with P4** rather than on D1's weak-form derivation and SC3 (iii), which are R-B's
hinge and do not score R-A (RC-4). The identities the basis uses are named (RC-3): P4 extended
to all t by C_n^{3/2}(1) = λ_n/2 (C3), b(0) = 0 from Chalub's printed b(t), and b(∞) = ∫x p^I
= x0 for a delta start. R-A0 and R-B stay `contradicted`, R-C stays `supported` (trivially,
D7), none field-setting. SC1's case is not discarded: it moves into the scope line as the
false half (the value is the classical solution's own outflux) and as the audit's recorded
lean (a boundary convention is not "an assumption imported from the Wright-Fisher model"),
rather than into a value that settles the open point between R-A and R-B. **B-R33** stands
with RC-5's corrections and, with this re-ruling, moves **no** B1e value (external
`contested`/`contested`, fidelity `partial`/`partial`, internal `holds`/`holds`), so RC-7's
O-6 timing question does not arise in EVO-12; general adoption stays EVO-95 and the split
stays EVO-96. **B-R34** is untouched (out of the check's remit, moves no field).

Because B-R35 keeps every registered value, **no further fresh-reviewer check is due** under
D-24, and EVO-12's remaining pass may be written. The three `verdict_scope` lines the
integrator writes are in `research/checks/briefs/B1e-Q2-analyst.md` §B-R35 and **supersede**
B-R33's drafted lines. Nothing publishes; the B-R20/B-R21 hold is untouched.

**Recorded cost to each side.** Critics lose a `contradicted` that SC1 argued well; the false
half and the lean both stay on the record. Day gains no truth: `supported` stays barred, R-C's
`supported` is trivial, fidelity stays `partial`, and B-R31 does not find that Day meant R-A.

**Process note.** B-R32 was the first lead ruling overturned by a D-24 check. The check cost
one agent run and caught an inconsistency between two rulings written in the same pass by the
same lead. That is the case for D-24, and it is recorded in favour of keeping the fresh check
mandatory whenever a ruling moves a governing value.

## 2026-10-18 — how a queued task is gated, corrected (D-30), and a timer backstop (D-31)

Lane mechanics, not verdicts. Recorded because the standing record was wrong on a point of
fact and because the error silently breached D-22 twice.

**D-30. Creating a task dispatches a run, and gating it afterwards does not stop that run.**
The rule carried from EVO-1 was "gating takes two writes: create, then set `blocked`, then
read back — a task created with blockers comes back `todo` and is startable". That understates
it. A task created in `todo` **gets an agent run immediately**, and the later `blocked` write
does not kill the run already in flight. The evidence, from 2026-10-18:

- **EVO-92** created 07:37:20, gated 07:37:28, and its agent posted a finished board patch at
  07:38:12 — real work on `board/upd24.py` while **EVO-15's launch run was also live**. Two
  agent runs at once, breaching the D-22/D-27 cap with nobody choosing to breach it.
- **EVO-93** created 07:42:49, gated 07:42:57, and its agent checked `na-workhorse` at
  07:43:01 before reporting "too early to collect". Harmless, by luck of what the task asked.

Both outcomes were benign; the mechanism is not. A board patch running unsupervised alongside
a compute launch is the exact collision the cap exists to prevent. Two lane reports (07:39 and
07:44) described those tasks as quietly gated and were wrong.

**The rule, from now on: a queued task is created in `backlog`, with the LANE TOKEN already in
`blockedByIssueIds` in the same write.** `backlog` does not dispatch — EVO-6, EVO-96 and
EVO-97 all sat there for hours with no run. Verified on **EVO-98**, created 08:21 this way and
read back `backlog`, `blockedBy: [EVO-79]`, **no active run**. That is one write, not the three
I expected. Release is unchanged and still takes two writes: remove the token, then set
`in_progress`, then read back — a single PATCH carrying both is still rejected with `Issue
follow-up blocked by unresolved blockers`.

**D-31. A 4-hourly routine now backstops the blocker-edge wake.** EVO-85 waits on
`issue_blockers_resolved`, which fires only when a blocker reaches `done`. It does not fire for
a **cancelled** blocker, and it does not fire for a blocker whose **run dies while the issue
stays `in_progress`** — that is the EVO-84 failure that left the lane stalled and the host idle
from 2026-10-14 to 2026-10-17. `monitorNextCheckAt` is not writable through the API and there
is no monitor endpoint, so the edge was the only wake available. Routines are: routine
`ceca443d` ("Lane stall backstop"), schedule trigger `35 2,6,10,14,18,22 * * *` UTC, first fire
2026-10-18 10:35, `concurrencyPolicy: skip_if_active`. Its run issue is instructed to **check
for a live agent run first and close immediately, writing nothing, if one exists** — the
backstop is not an exception to the D-22 cap — and to clear a dead blocker and report on
EVO-85 rather than release anything itself. Releases stay on EVO-85. This bounds stall
detection at four hours instead of unbounded, at six wakes a day instead of the ~96 that the
old 15-minute cadence cost, which is what produced the three consecutive terminal limit
failures on 2026-10-14 03:21-03:23.

**What this does not touch.** No verdict field, no tier, no review tier, and not the
B-R20/B-R21 publication hold.

**D-32. Correction to D-30: `backlog` is not a gate. The token is the gate.** D-30 above says
"`backlog` does not dispatch — EVO-6, EVO-96 and EVO-97 all sat there for hours with no run".
The observation was right and the inference was wrong. Those three sat without a run because
**the lane was occupied the whole time**, not because `backlog` holds anything. The evidence,
2026-10-18: **EVO-96** was in `backlog` with an empty blocker list, and it started at
**08:24:37.442Z** — the previous run ended at 08:24:37.119Z, so it was dispatched within a third
of a second of the lane freeing. It then ran a full design pass on the B1e split, work that two
lane reports had described as deliberately held back until EVO-95 settles, and parked itself
`in_review` on an owner question card. Nothing was applied and the work is sound, but nobody
chose to run it.

So D-30's one-write recipe stands only because of the half that does the work: **the LANE TOKEN
in `blockedByIssueIds`.** `backlog` is cosmetic. The rule, restated: **every task that is not
meant to run next carries the token, whatever its status** — and in particular every *chain
head*, i.e. every task whose only blockers are `done` or absent. A task gated solely by its
predecessor is fine: when the predecessor completes, the chain advances one task, which respects
the cap and is how the lane has always worked. A head with no predecessor and no token is an
unowned auto-start.

Swept all 36 open issues on 2026-10-18 08:3x. Two ungated heads existed: **EVO-96**, now gated
and released only after CJ adoption, and **EVO-6**, now gated — that one matters, because its
close-batch step publishes, and publication is outward action needing the owner's word under
hard rule 6. Everything else is gated by the token or by a `blocked` predecessor.

**D-33. EVO-96's two questions ruled by the lead; the owner card withdrawn.** EVO-96 asked the
owner (a) when to execute the split and (b) whether the tier is one review or three. Neither is
policy and neither is outward action, so under D-28 both are the lead's and the card
(`eac10104`) was withdrawn rather than answered — the owner has one real card pending, the CJ
adoption confirmation on EVO-95, and a second slot should not be spent on internal sequencing.
Rulings: **(a) after CJ adoption**, earliest release 2026-10-19 07:59 UTC, because the split is
CJ's named remedy and a shift in clause CJ5 moves the design's scope lines; **(b) one combined
review**, because neither D-23 trigger fires — no check registration, no verdict value or
reading moves, B1e not in the R5-draft 1.3 feeder list — with the binding condition that the
review's first job is to test the no-value-moves claim, and that finding any moved value or
reading escalates to the three-review tier **before** any edit. The "expect three reviews"
phrase in EVO-96's description is superseded.

**What D-32 and D-33 do not touch.** No verdict field, no governing reading, and not the
B-R20/B-R21 publication hold.

**D-34. Amendment to D-31: the backstop routine may release exactly one task, EVO-93, and
nothing else.** D-31 says "releases stay on EVO-85". That holds for every ordering decision, but
it leaves one hole that showed up the same morning it was written. EVO-85's only wake is
`issue_blockers_resolved`, which needs a blocker to complete. When the lane is already free and
what the queue is actually waiting on is a **clock** — the FMnull-S4 host job finishing at about
10:30 — there is no blocker to complete and therefore no wake. Re-tested both candidate fields at
08:4x: `monitorNextCheckAt` and `monitorWakeRequestedAt` each accept a PATCH with HTTP 200 and
leave the field `null`, so an agent cannot arm an issue monitor at all. Without an amendment the
collect would sit token-gated with an idle host until the 14:35 tick.

So routine `ceca443d` (revision 4) now carries a release exception guarded by three conditions,
all of which must hold: no agent run live anywhere in the company, the `fmnull_s4.py sim`
processes gone from na-workhorse, and EVO-93 `blocked` with EVO-79 as its only unresolved
blocker. It then releases **EVO-93 alone** and reports on EVO-85. Every other queued task, every
ordering question, and anything that is not EVO-93 stays EVO-85's call. The D-22/D-27 one-run cap
is untouched — the first condition is the same live-run check the routine already did, and it
still closes writing nothing if a run exists.
