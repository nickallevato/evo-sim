# Method audit, 2026-10-12: a review of how the audit works, not of what it found

*Scope: technique, logic, epistemology and process of the evo-sim research phase at commit `c0c16b2` (branch `research`). No mathematics was re-run or re-derived. Counts marked "measured" were taken by me from the claim-file front matter, the review files and `git log`; counts marked "sample" cover only the items named.*

**Status of this document, read first.** It was commissioned as a "neutral third-party" review, and it is not one. It was written by a Claude Opus instance launched from inside the project's own session, with the project's `AGENTS.md` loaded. Finding MA-01 (reviews by the same model family are not independent) applies to this file in full. Treat it as one more internal review with a different brief, and discount it accordingly.

---

## Executive summary

**Judgement.** Check by check, the work is careful, self-critical and well disclosed. Its claims about itself ("neutral", "pre-registered", "three reviews", "one rule for both sides") are not yet sound. One model family extracts, checks, reviews, adjudicates the reviews, changes the rules and counts the results, under one owner. The write-ups are a usable provisional record; the verdict tallies are not publishable.

**Five most serious weaknesses**
1. Reviews are not independent: same model family, not blind, author-adjudicated; no post-run review has blocked a check (MA-01).
2. Rule RH6 rewards being far from true, and rules were redefined the day they were applied, moving two load-bearing Day verdicts outside the three-review tier (MA-02, MA-03).
3. Pre-registration is unverifiable for the early rounds and carries no weight for at least thirteen later checks (MA-04).
4. External verdicts often rest on the disputed theory or on simulation, against rule E1; `contested` takes 66% of decided external verdicts; 44% of `holds` are defaults (MA-05, MA-07, MA-08).
5. No outside contact: the book is unread; no right of reply, human expert, or registered rule from node verdicts to a conclusion (MA-09 to MA-11).

**Five real strengths**
1. Limits are disclosed prominently (`HANDOFF.md` l.94-107; X1).
2. Quotes are machine-checked against hashed raw text; misses are printed.
3. Long runs and the UATV note are genuinely pre-registered; missed predictions are reported.
4. Internal validity is scored on the author's own basis, apart from fidelity and realism.
5. Pre-run design reviews; cross-host and cross-tool replication.

---

## What was measured

All from `docs/research/claims/*.md` front matter at `c0c16b2` (233 files; Day 130, critic 61, literature 27, ally 15).

| Measure | Day | Critics | Allies | Literature |
|---|---|---|---|---|
| Internal `holds` | 66 | 50 | 6 | 9 |
| Internal `non-sequitur` + `arithmetic-error` | 17 + 2 | 1 + 0 | 1 + 0 | 0 |
| Error share of decided internal verdicts | 19/85 = 22% | 1/51 = 2% | 1/7 | 0/9 |
| Internal `pending` | 35 (27%) | 8 (13%) | 5 | 4 |
| Fidelity `misread` / `partial` / `accurate` / `unverifiable` | 9 / 23 / 9 / 39 | 0 / 10 / 17 / 14 | 0 / 1 / 5 / 4 | 1 / 5 / 13 / 1 |
| External `contradicted` / `supported` / `contested` | 16 / 10 / 65 | 1 / 16 / 26 | 0 / 0 / 10 | 1 / 8 / 13 |
| Status `reviewed` | 46 (35%) | 14 (23%) | 2 | 8 |
| Status `checked` or `reviewed` | 74 (57%) | 24 (39%) | 4 (27%) | 9 |
| `holds` sitting on a file still at status `extracted` | 21 of 66 | 28 of 50 | 3 of 6 | 6 of 9 |
| `load_bearing: true` | 24 | 5 | 1 | 3 |

- Decided external verdicts: 172, of which `contested` 114 (66%).
- `holds` at status `extracted`: 58 of 131 (44%).
- My parse differs from the `HANDOFF.md` totals by one in five cells (internal pending 52 vs 51; fidelity accurate 44 vs 43, partial 39 vs 38, pending 11 vs 12; external pending 49 vs 48). Not chased; see MA-20.
- Review files: 91 `REVIEW-*.md`. 33 carry an explicit zero-BLOCKER statement. The only numbered BLOCKER in any of them is in the pre-run review of L1c. The review log records one BLOCKER in 65 reviews (review #2, an import bug).
- Review tiers since tiering began (review #14 on, from `REVIEW.md` headings): 24 single combined or light reviews; 8 three-review sets (D15, H8, A2e, B2/B, B3, FM, A2e-alpha, L1), plus HF reviewed and not yet logged.

**Commit timing, pre-registration commit to the commit that adds the result write-up** (`git log`, committer time; words are lines added to `results/R4-*.md` in the result commit):

| Check | Tier | Pre-reg | Result | Gap | Write-up added |
|---|---|---|---|---|---|
| A2e-alpha, Uricchio addendum | low | `7d68de9` | `0dc6e76` | 25 s | ~950 words |
| B3g | low | `ef6e8aa` | `157aab9` | 30 s | ~760 |
| B3 | load-bearing | `04f96bd` | `abb66a0` | 36 s | ~750 |
| GAP05 | low | `b59f2e5` | `314a743` | 36 s | ~1,630 |
| F3a | low | `f9c8ed9` | `06286c2` | 41 s | ~790 |
| B9 | low | `e95f0d3` | `c7a1f12` | 51 s | ~1,480 |
| B2/B | load-bearing | `3d07343` | `e448cb2` | 61 s | ~1,280 |
| B3m | low | `5ca5f2e` | `52bee7e` | 62 s | ~860 |
| RHclose-critics | low | `8aef421` | `a48ac8a` | 74 s | ~2,460 |
| RHclose | low | `7185f1e` | `0cdc47d` | 84 s | ~2,570 |
| A2e-alpha + GAP-06 | load-bearing / low | `49824e0` | `4a37912` | 94 s | ~2,220 |
| P1 | low | `c17b44a` | `f8bffe6` | 127 s | ~1,870 |
| B5b + F1b | low | `b707415` | `6412660` | 260 s | ~1,690 |

For B9, RHclose, GAP05 and RHclose-critics the `origin/research` reflog shows no push between the pre-registration commit and the result commit, so no outside timestamp separates them.

Contrast, where the gap is real: H8 (`acd3a9e`), A2e (`7593be2`), D15 (`b74b6d6`), FM (`d723064`, pushed 14:21, write-up 15:31), HF (`8bd9d29`, main results the next day), L1b, L5, L1c and FMnull (pushed, not yet run), and the UATV note (`9c97fcd`, pushed 14:48:45 before the broadcast).

---

## Findings

### MA-01. The three reviews are three prompts to one reviewer
- **Severity:** CRITICAL. **Category:** independence of verification.
- **Evidence.**
  - Every check, review, steelman, "independent re-review" (#23-#25) and "blind audit" is a Claude instance. `HANDOFF.md` l.97-98 says so ("AI reviewing AI"; "no human population geneticist has checked the simulations").
  - Reviewers read `AGENTS.md` and the finished write-up with its proposed verdicts. The one review that tried to be blind (`REVIEW-R4-X1-rule-audit.md` §0) reports that it was not: claim-file front matter carries the current verdicts and the rule file states 15 intended outcomes.
  - Reviews are advisory. The check's author writes the "Review resolution" and may decline (`R4-X1-verdict-rule.md` §9: items 6, 10 declined; 7, 18, 21 partly applied). A re-review of a fix pass appears for FM (#46, #47); it is not the norm. No reviewer signs off.
  - No post-run review has blocked a check on substance (counts above). `HANDOFF.md` l.19 says "A check counts only after it passes all three"; nothing has ever failed.
  - Early reviews were done by the cheaper model on the stronger model's work (`PLAN.md` l.11; reviews #1-#13 "Sonnet"), a choice driven by the token budget (`AGENTS.md` l.18-22).
  - Day's papers list a co-author from the same model family ("Claude Athos", `HANDOFF.md` l.97), and at least one critic source is AI-assisted (KITTENS, `balance.md`). The auditor, part of the audited material and all reviewers share training data.
- **Why it matters.** Independent review works because reviewers' errors are uncorrelated. Role prompts change what a reviewer looks for; they do not change what it knows, what it finds plausible, or which derivation slips it tends to make. A shared wrong belief about, say, the behaviour of a diffusion approximation would pass correctness, steelman-Day and steelman-critic alike. The reviews do catch real defects (the FMnull and L1c pre-run reviews are good), so they are worth having. What they cannot support is the inference "three reviews passed, therefore probably right". A zero failure rate is uninformative without a measured catch rate.
- **Priors.** The model's training corpus is overwhelmingly mainstream on evolution. `PLAN.md` l.273 records that pass-1 assessments "lean toward the mainstream". The counterweight (balance ledger, steelman-Day role) is applied by the same model.
- **Who raises it:** everyone. Day-side: "an establishment-trained model marks its own homework." Critic-side: "an eager-to-please model splits the difference." **Fair.**
- **Remedy.**
  1. *Seeded-error test (days, cheap).* Take five reviewed write-ups, plant known defects of graded subtlety in copies (a unit slip, a swapped basis, a band moved after the run, a misquoted source), run the standard review prompts, report the catch rate. This turns "0 BLOCKER" into a number.
  2. *Truly blind re-derivation.* For the ten most consequential nodes, give a fresh agent only the verbatim quote, the raw source and the data. No claim file, no write-up, no `AGENTS.md`. Compare verdicts and report agreement as inter-rater reliability.
  3. *Different model families* for one review seat on load-bearing checks. This reduces, and does not remove, correlated error.
  4. *One human population geneticist* on the five checks that carry the most (B3/B7 k = μ, B4a ancestral polymorphism, H8/HF cost, A2e, GAP-07 counts). Owner action.
  5. Stop writing "passes all three". Write "reviewed three ways by the same model family; author-resolved".

### MA-02. RH6 rewards distance from the truth
- **Severity:** MAJOR. **Category:** verdict rule, logic.
- **Evidence.**
  - `R4-X1-verdict-rule.md` l.194: an unclear statement is `dialectic` if "remotely close" (within 3x) under the most charitable reading, else `rhetoric`. Rhetoric "changes no verdict" (l.185).
  - Outcomes: Day's Q157/Q158 "nearly empty" is `rhetoric` on the reading where it is furthest off (fill 0.697) and unscored there; on the readings where it is close (0.256, 0.281, 0.025) it is `dialectic` and then `non-sequitur` (`claims/B-neutral-theory-cannot-rescue.md` l.12, Readings table). Myers's "I debunked..." scores 0/24 and 0/2 on the audit's own record, so it is `rhetoric` and unscored (`R4-RHclose-critics.md`, RH-20). Hancock's "can't do any of this" is `dialectic` on the reading where it is true and `rhetoric` on the reading where Day's own texts contradict it.
  - `R4-RHclose-critics.md`, "Verdict effects" table, says it itself: rhetoric "releases 'debunked' from a 0/24 audit record"; l.52 adds that the rule "is not symmetric in default".
  - The band is multiplicative, and the statements it is used on are absolutes ("not at all", "nearly empty", "none", "can't do any"). Three times zero is zero, so each check invents an edge: 3e-4 for F_drift, 0.30 for fill, floor(N/3) for counts (`REVIEW-R4-RHclose-combined.md` MINOR-4: "the band 0.10 and the edge 0.30 are the author's"; `R4-RHclose-critics.md` Caveats: "H2 is within one class of the edge").
  - For evaluative claims the truth standard is the audit's own verdict table (`R4-RHclose-critics.md` l.70), which is circular: the audit's unreviewed defaults (MA-07) decide whether a critic's summary of the dispute is "remotely close".
- **Why it matters.** Under RH6 a statement can be scored only if it is nearly right. A speaker who overstates by 2x is exposed to `non-sequitur`; one who overstates by 20x is excused as a rhetorician. That inverts the ordinary relation between error size and accountability, and it makes the tag a function of the verdict it is supposed to precede (RH1 says "classify before scoring"). Genre is a property of the speech act in its context: who is addressed, whether a derivation is attached, whether the author relies on the sentence later. It cannot be read off the arithmetic distance.
- **A second problem.** The dialectic/rhetoric distinction is Day's own framework, adopted by owner directive (rule l.173). An audit that imports the subject's exemption category will be accused by critics of handing him an escape hatch, and by Day's readers of deciding for him which of his sentences he meant. RH2's "answer with better rhetoric" also asks the auditor to write persuasion (`ledgers/slips.md`, Counter column, one per entry RH-1 to RH-26). An auditor who drafts ripostes has stepped into the debate.
- **Who raises it:** methodologist (the inversion); critic-side ("C7's 'drift isn't happening at all' gets a rhetoric reading"); Day-side ("closeness got B a non-sequitur"). **Fair.**
- **Remedy.**
  1. Tag genre on contextual criteria fixed in advance and blind to the number: is a derivation attached; does the author cite the sentence as a premise elsewhere; is it in a peroration, title or taunt; did the author gloss it. Record the criteria met.
  2. Decouple reporting from genre: for every tagged statement, publish the literal reading and its distance from the mark whatever the tag. A rhetoric tag then changes the node verdict column only, never whether the number is shown.
  3. Replace the 3x band on absolutes with an explicit per-quantity threshold stated in the rule, not in each check.
  4. Do not score evaluative claims against the audit's own tallies. Mark them "not checkable here".
  5. Keep the counters out of the audit record, or move them to a clearly separate commentary file.

### MA-03. Rules were made and remade on the day they decided verdicts
- **Severity:** MAJOR. **Category:** process integrity, forking paths.
- **Evidence (all 2026-10-11, `git log`).**
  - 18:53 B9 pre-registers the first "remotely close" criterion with a 10x band, the numbers already known (`b9_relaxed_load.py` docstring, "DISCLOSURE"). The review calls the criterion loose (MAJOR-3); the band becomes 3x.
  - 20:26-20:45 RHclose and RHclose-critics apply the rule to C7, B and three critics, each with author-chosen edges.
  - 21:20 `e03f516` writes RD and RH6 into the verdict rule; `db2d16d` integrates five checks.
  - 21:24 `3f881b0` redefines "most charitable" from "most charitable to the speaker" to "the reading under which the quoted statement is most defensible". Effect, in the commit message: "B internal holds -> non-sequitur". B is `load_bearing: true`. The commit is four minutes after integration, authored by the bookkeeping model, with no review file.
  - A2e (`load_bearing: true`) moved from `contested` to `contradicted` (scoped) on a post hoc addendum with one combined review (#64), whose MAJOR-2 reads "the trigger and blockers were set by the author who scored them".
  - `AGENTS.md` l.22 requires three reviews for checks that "move a ROOT-path node". RHclose, the Uricchio addendum and the RD redefinition all moved one under the low-stakes tier or under none.
  - L5's tier was cut from the pre-registered three reviews to one after registration (`QUEUE.md` l.66).
  - Owner decisions are cited as "in chat" (`R4-B9.md`; rule l.194-198). The chat is not in the repo.
  - `AGENTS.md` l.46 still says the verdict field "takes the reading most charitable to the speaker"; the front-matter comments of C7 and B9 still say "most charitable to Day". The rule text says the opposite.
- **Why it matters.**
  - RD multiplies readings; the verdict field then needs a selection rule; the selection rule is "most defensible", which is the auditor's judgement of defensibility under another name. The readings table is honest. The single value that flows into the tallies and the board is a choice.
  - With n readings per quote and a free edge per reading, some reading reaches any verdict. Reporting all readings is the right response. Promoting one to the headline, by a rule revised after seeing which verdict each definition gives, is a forking path.
  - The two definitions of charity are both defensible. The objection is to the order of events: the definition changed after the outcome under each was on the table, and the outcome that changed was adverse to the audited party on a load-bearing node.
- **Who raises it:** Day-side most sharply; any methodologist. **Fair.** (An unfair version, "the owner rigged it", is not supported: the same evening B9 moved to `holds` in Day's favour and the other readings are recorded.)
- **Remedy.**
  1. Freeze the verdict rule. Version it (rev 3), and require that a rule change is committed with a list of every verdict it would move, before it is applied, and reviewed at the load-bearing tier if any moved node is load-bearing.
  2. For reading-dependent nodes, put `reading-dependent` in the verdict field itself and keep them out of every tally. That removes the selection rule.
  3. Re-open B and A2e under the tier the project's own rule requires.
  4. Keep a dated `DECISIONS.md` with the owner's words verbatim.
  5. Fix `AGENTS.md` l.46 and the stale front-matter comments.

### MA-04. Pre-registration: real for long runs, unverifiable or empty for the rest
- **Severity:** MAJOR. **Category:** pre-registration.
- **Evidence.**
  - *Early rounds.* Rounds 1 and 2 and E/G1 were each committed as one commit containing scripts, results, reviews and merged verdicts (`3d888e9`, `36a7ff9`, `a89d06c` with 93 files, `9a2148b`). Their write-ups say "pre-registered" (`R4-B1c-B4a.md`, `R4-H2-hard.md`, `R4-E.md`). The first commit made as a pre-registration is `0061b28` (10-08 21:39). So for about nineteen checks, among them the core of branches B, F and H, git cannot show the order. Round 2 has partial cover: the claim files with prediction sections (`ad44c23`, 10-07 20:13) precede `a89d06c`. Round 1 (`3d888e9`, 18:53) precedes the claim files.
  - *Tight gaps.* Table above: eleven checks with a full write-up committed 25-94 s after the pre-registration, two more inside five minutes. Two are load-bearing (B2/B, B3). Whatever happened in the working tree, a commitment made seconds before the result, by the party that then reports the result, with no outside timestamp, binds nothing.
  - *Disclosed non-blindness.* B9 ("The numbers below are known in advance"), RHclose, RHclose-critics ("Not blind"), L7 ("sheet 14/19 values were seen during derivation"), GAP05 ("NOT blind to the DFE"), FMnull P4/P5 (`REVIEW-R4-FMnull-prerun.md` MAJOR-5: "informed, not predictive").
  - *Bands not exhaustive.* `REVIEW-R4-L1c-prerun.md` MAJOR-2 finds unregistered outcome regions, two of them Day-favourable, that "would be interpreted after the data are seen".
  - *Post hoc discipline is good.* Labels are granular and honest (`df43563` "exploratory, NOT pre-registered"; `cedc86a` reports a missed band; `1f3dd12` rows omitted from the registered list).
  - *"Post hoc, pre-run, no data seen".* `REVIEW-R4-L1c-prerun.md` MAJOR-4 states the limit itself: L1 on hg38 already makes one band the expected one.
- **Why it matters.** Pre-registration protects against choosing the criterion after seeing the outcome. For the long runs it does that. For sub-second arithmetic it cannot, and the project knows it (the B9 write-up says the scores "carry no evidential weight"). The defect is in the label. `HANDOFF.md` l.18 tells outside readers "The prediction is written down before the run", without the distinction. A reader who counts "pre-registered" checks is misled about how many were tests.
- **Who raises it:** methodologist; either camp when a result goes against it. **Fair.** The stronger claim, that results were written before the registrations, is **not established**: the timing is compatible with an agent that writes the docstring, runs, writes up and then commits in two steps.
- **Remedy.**
  1. Three labels in place of one: `blind-prereg` (pushed to the public remote before any run, with the push time recorded), `criterion-prereg` (numbers known, criterion fixed), `reproduction` (no prediction at stake). Relabel every check; publish the three counts.
  2. For `blind-prereg`, push before launching and record the remote's commit time in the `.host` file. A signed tag or an OpenTimestamps proof costs nothing.
  3. Mark the round-1 and round-2 checks "predictions not verifiable from history".
  4. Require registered bands to partition the outcome space; add an explicit "outside every band" rule.

### MA-05. "External" is often decided by the theory in dispute
- **Severity:** MAJOR. **Category:** inference, question-begging.
- **Evidence.**
  - `PLAN.md` l.240: "Simulations settle (a) and (b). Only data settles (c)."
  - 52 claim files carry a decided `supported` or `contradicted` external verdict. Reading the verdict comments (a reading, not a coded count), roughly twenty rest on forward simulation or standard theory with no observation: B6 ("full pipe gives k = mu ... (forward sim)"), B3i and B7 (1/2N), B3c and C2c (artefact shown by simulation or identity), H1 and H6 ("neutral k = U (B0.5)"), B6c/G2c ("as a conditional"), F1b, A5f, B9 ("premise 1 false under standard theory").
  - `PLAN.md` l.14: "Where standard theory makes a firm prediction ... we state it as the null hypothesis."
- **Why it matters.**
  - In a Wright-Fisher forward simulation the neutral rate k = μ is a theorem of the sampling scheme. Simulating it confirms the code. It is strong evidence on *internal* questions (does Day's formula follow from Wright-Fisher-type premises he himself uses). It is no evidence that real hominid populations satisfy those premises. Recording the result as `external: supported` moves a model-internal fact into the column that is supposed to be about the world.
  - Making standard theory the null assigns the burden of proof to the heterodox party. That is how working science operates and is defensible. It is a stance, and it sits oddly beside "We are neutral" in the same paragraph.
  - Duhem-Quine applies both ways. Day's 0.80 dN/dS against the audit's 0.21-0.27 is a clash between two pipelines with many auxiliaries (assembly, annotation, aligner, frame handling, estimator). The audit handles this case well: L1 isolates gene set and estimator, and L1c is designed to test Day's proposed auxiliary. The same care is not visible where the auxiliary is the population model itself.
- **Who raises it:** Day-side first ("you assumed Kimura to refute me"); a careful methodologist. **Fair** for the nodes listed. **Unfair** as a blanket charge: many external verdicts rest on data the audit processed itself (GAP-07b/c/t counts, C1d on AADR genotypes, L1 on public alignments, FM).
- **Remedy.**
  1. Add a field `external_basis: data | simulation | theory | literature` to every decided external verdict. Lint that `supported`/`contradicted` requires `data`, or downgrade to a new value `model-consistent` / `model-inconsistent`.
  2. State the stance once: "The audit treats standard population genetics as the default model and asks whether Day's argument defeats it. It does not test standard theory against a rival of equal standing."
  3. For each load-bearing node whose external verdict is model-based, name the observation that would bear on the model's applicability.

### MA-06. The Day-versus-critics error rate does not measure what it appears to
- **Severity:** MAJOR. **Category:** symmetry, aggregation.
- **Evidence.** 19/85 against 1/51 (measured). Four mechanisms inflate the gap independently of anyone's competence:
  1. *Volume.* The rule admits it (l.63): N2b "exposes authors who have written more"; "the Day error count partly measures output volume".
  2. *Precision.* R1 scores a slip only against a "stated conclusion". An author who asserts no match "holds" by construction (l.30, keruru's "an unreconciled twofold"). Sharp, checkable claims are exposed; vague ones are not. Critics here are mostly commenters with one-line claims.
  3. *Scrutiny.* Day's nodes are checked or reviewed at 57%, critics' at 39% (measured). Twenty-four Day nodes are load-bearing against five critic nodes, and load-bearing status buys three reviews. `R5-draft.md` §4.3 items 1-2 (as of 10-09, before X1 added critic checks): fifteen of twenty-four checks target a Day claim, one a critic claim; audit attacks on Day are upheld at 44%, on critics at 14%.
  4. *Routing.* Critic defects tend to land in the external column (`R5-draft.md` §4.3 item 3) or the slip ledger; node extraction from comment threads is "outside the rule" (l.43).
- **Credit.** X1 found most of this, re-scored, and wrote that the gap "is **not robust**" (l.120). That sentence is the correct conclusion. Yet `HANDOFF.md` and the README still lead with the tallies and Fisher p-values, and p = 0.008 is in the table. Fisher's test assumes independent, exchangeable units. Claim nodes are neither: they are nested in authors, documents and derivation chains, and their granularity was chosen by the auditor.
- **Who raises it:** Day-side ("you looked harder at me"); critic-side ("he made more errors, and you are explaining it away"). **Fair** against any comparative use of the rate. **Unfair** against the individual Day error verdicts, most of which rest on his own tables and text.
- **Remedy.** Drop the comparative rates and all p-values from public pages. Report, per side, the list of error verdicts with their basis, and the scrutiny each side received (checks, reviews, words read). If a rate is wanted, compute it per audited derivation step on a matched sample: the n most-developed arguments from each side, each given the same tier.

### MA-07. `holds` is the default, so "131 hold" says little
- **Severity:** MAJOR. **Category:** verdict semantics, aggregation.
- **Evidence.** 58 of 131 `holds` sit on files at status `extracted`, meaning no check and no review (critics 28 of 50; Day 21 of 66). `holds` also covers "the algebra is right on a premise the author later withdrew" (B3a: holds / misread / contradicted) and "the arithmetic is right for an empty start that did not obtain" (B1c). 91 of 233 claim files lack the template's "Result that would change a verdict" line.
- **Why it matters.** The vocabulary has no value for "not examined, no defect noticed". A reader of "131 hold, 19 non-sequitur" will read 131 validations. Only 73 sit on files that reached `checked` or `reviewed`. Validity, soundness and persuasiveness are kept apart in the three-column design, which is good; the tally then collapses them again by counting only the first.
- **Who raises it:** critic-side ("you credit Day with 66 holds for arithmetic on false premises"); Day-side ("critics get 28 free holds"). **Fair.**
- **Remedy.** Add `unexamined`. Lint: `holds` requires a `Check` entry or an explicit one-line derivation reviewed by a second agent. Publish tallies only for nodes at `reviewed`, and never one column without the other two.

### MA-08. `contested` holds five different things
- **Severity:** MAJOR. **Category:** verdict vocabulary.
- **Evidence.** 114 of 172 decided external verdicts. In the files it means, variously: disputed in the literature (D10); true only in the tested regime (F1, H5); conditional on an unsourced parameter (A2e's other scopes, H); leaning one way but short of decisive ("contested, leaning critic", FM10; "contested leaning contradicted", A2e before 10-11); and "depends on the flagged N_e ≈ 1e4" (rule F).
- **Why it matters.** A category that takes two-thirds of the mass carries no information, and it blunts both ways. It lets the audit avoid saying that a Day claim is very probably false, and avoid saying that a critic's claim is unsupported. `HANDOFF.md` notes that the largest category is contested and offers no decomposition. The risk on one side is false balance; on the other, the appearance that most of Day's case is "still in play".
- **Who raises it:** critic-side strongly ("false balance by vocabulary"); methodologist. **Fair.**
- **Remedy.** Split into `conditional:<parameter>` with the flip value, `regime-limited`, `disputed-in-literature` with the two sources, and `undetermined`. Allow an optional lean with the evidence that would settle it. Re-code the 114.

### MA-09. The audited book has not been read
- **Severity:** MAJOR. **Category:** sources.
- **Evidence.** `HANDOFF.md` l.101: "*Probability Zero* has not been purchased". Book-only claims are `secondhand` (Day 7 files, critics 8, allies 4, measured). Appendix A's "fixation must be sequential" is known only through Day's own later quotation (`argmap/NOTES.md`, Ambiguities). A4g and D2l exist through slides read aloud in a critic's video (judgement call 15). Hancock's video is used through auto-captions. X, Gab, Telegram and SocialGalactic are unreachable (`HOWTO-refresh.md` l.26-30). McCarthy's paid posts and Rosenhouse ch. 6 are unread (`balance.md`, Coverage gaps).
- **Why it matters.** The project describes itself as an audit of *Probability Zero* and audits the Zenodo papers and blog instead. Those may be the better statement of the mathematics, but the book is the version most readers hold, and its text is the referent of several critic claims. Verbatim discipline on the texts that were read does not cover a primary text that was not.
- **Other source risks, lower.** Quote selection is by agent (substring checks prove the words exist, not that the passage is representative). The pass-2 harvest and the extraction of 193 claims were committed between 18:48 and 20:13 on 10-07, with no later sampling audit of extraction accuracy. `parameters.yaml` has 30 entries `verified: false` against 25 `true`.
- **Who raises it:** Day-side, first sentence of any reply. **Fair.**
- **Remedy.** Owner buys both editions (hours, small cost); re-source the `secondhand` nodes. Draw a random sample of 30 claim files and have a blind agent re-extract from the raw source; report agreement on quote choice, context and the formal statement. Until the book is read, describe the object of audit as "Day's Zenodo papers and blog posts".

### MA-10. No one outside the loop has been asked anything
- **Severity:** MAJOR. **Category:** governance, right of reply.
- **Evidence.** `HANDOFF.md` l.104: "None of the authors on either side has been contacted". Hard rule 6 forbids contact without approval. The repo is public and verdicts on named living people (Day, Hancock, Myers, McCarthy, Mansfield, Hössjer) are published as they are made. One owner makes every rule decision. 307 commits in six days; on 10-11 five checks went from registration to integration, with two rule changes, between 18:53 and 21:24.
- **Why it matters.** An audit earns standing by exposing itself to the audited. Publishing `non-sequitur` and `misread` against named people with no notice and no reply is a fairness problem on its own. It is also the cheapest independent review available: each author will find the audit's errors about himself faster than any reviewer. At the observed pace the owner cannot have read what he is approving; his decisions rest on the agents' summaries, which is the summariser risk of hard rule 2 moved up to governance.
- **Who raises it:** both camps; any research-integrity reviewer. **Fair.**
- **Remedy (owner).**
  1. Before R5, send each named author the verdicts on his own claims with locators, a fixed reply window (say 21 days), and a commitment to publish replies verbatim beside the verdict.
  2. Recruit one Day-side and one critic-side reader as adversarial collaborators on the rule text and the load-bearing list. Disagreement is recorded, not resolved by the owner.
  3. A cooling-off rule: no rule change and no load-bearing verdict move is integrated on the day it is proposed.

### MA-11. No rule connects node verdicts to a conclusion, and no stopping rule exists
- **Severity:** MAJOR. **Category:** missing design.
- **Evidence.** `HANDOFF.md` l.135-138: "Whether the audit's conclusions bear on the root claim as a whole" is "not yet decided". The exit criteria (`PLAN.md`, "Exit the research phase when") are coverage criteria. The queue grows as Day publishes (FM, L1, L1b, L1c, L6, L7 and FMnull follow his posts of 10-10 to 10-12). ROOT's own file has a falsifier ("refuted if any single mechanism class ... is shown ... to deliver the required F_req within T"), which is good, and which is defined in terms of forward simulation under `parameters.yaml`.
- **Why it matters.** With 33 load-bearing nodes, three verdict columns, reading-dependent values and a majority of `contested`, almost any top-level sentence can be written after the fact. The aggregation rule is the single most consequential analytic choice and the only one not yet registered. An audit that follows its subject's daily output with no stopping rule can also be steered by that output.
- **Who raises it:** methodologist. **Fair.**
- **Remedy.** Before R5, commit and push: (a) the mapping from node verdicts to each admissible top-level statement, including "undetermined"; (b) what the audit would have to see to conclude "Day's root claim stands on branch X"; (c) a corpus freeze date and a rule for later material (appendix only).

### MA-12. Some verdicts ran ahead of the like-for-like test
- **Severity:** MINOR to MAJOR. **Category:** burden of proof, unverifiable ≠ false.
- **Evidence.** DN1, DN2, DN3 are `external: contradicted` ("verdict set at integration") on hg38/panTro5 with knownCanonical genes. Day's stated pipeline is T2T with GENCODE v46. The like-for-like rerun L1b is registered and not run. The Day-side steelman asked whether the verdicts were "premature, given that his T2T / GENCODE v46 pipeline has not been rerun" (`REVIEW-R4-L1-steelman-day.md`, header).
- **Handled well elsewhere.** FM10 stays `pending` "until Day releases his method" (owner decision 10-10). C6 is "contradicted as stated, under his described method". GAP-05 is credited to Day as "his best point". This is the right treatment of unreleased code: score the description, not the absent artefact.
- **Who raises it:** Day-side. **Fair** for DN1-DN3 as labelled.
- **Remedy.** `contradicted (on hg38; T2T rerun pending)` or `pending` until L1b reports. General rule: where a like-for-like replication is registered, no external verdict before it runs.

### MA-13. One decomposition, drawn from the first summary pass
- **Severity:** MINOR. **Category:** selection.
- **Evidence.** Branches A-H come from `PLAN.md` "Argument hierarchy (v1)", written from the read-only pass-1 harvest that the same file calls summariser-affected (l.273). The tree is rooted at Day's claim; critics' statements enter as attackers. "Load-bearing" is defined relative to that root and assigned by agents (`hierarchy.yaml`), then extended as results came in (A3, ROOT-FM, FM10). Tier assignment is discretionary: the L1 reviewer overrode the write-up's own "low-stakes" proposal.
- **Why it matters.** Rooting at the challenger's claim is natural for an audit of that claim, and it means "equal scrutiny" cannot mean equal depth. A mirror tree rooted at the critics' positive thesis (standard mechanisms account for the observed divergence in the time available) would make their quantitative commitments load-bearing: the adaptive fraction, the ancestral N_e fit, the soft-selection premise. The gaps ledger shows the audit sees these (GAP-01, GAP-05, GAP-06). They are filed as gaps, not as the other side's burdens.
- **Who raises it:** Day-side. **Partly fair.**
- **Remedy.** Build the mirror tree (a day's work, mostly re-pointing existing nodes), mark its load-bearing nodes, and report check and review coverage for both trees side by side.

### MA-14. The 25% line was placed in the gap of the observed slips
- **Severity:** MINOR. **Category:** verdict rule.
- **Evidence.** Rule l.36, justification (2): "The slips found fall into two groups with a gap: 12 to 13% ... and then 33% or more." Justification (1) appeals to the spread of biological inputs. The rule opens by saying revision 1 "was written ... after the verdicts were known" (l.3-5).
- **Why it matters.** A threshold chosen where the data are sparse is a post hoc cut. The sensitivity line (10% turns three slips into errors, two Day's and one critic's) shows the practical effect is small, and it is disclosed. Justification (1) is a category mistake: uncertainty in μ has no bearing on whether an author's arithmetic moved his own conclusion. The honest justification is "a convention, checked for sensitivity".
- **Who raises it:** either. **Fair but small.**
- **Remedy.** Say "convention". Keep the sensitivity row. Report every slip's epsilon in the ledger so a reader can apply another line.

### MA-15. Category leaks in the three-verdict scheme
- **Severity:** MINOR. **Category:** coherence.
- **Evidence.** Audit-raised nodes are coded `side: literature` because the lint has no `audit` value (B1c, B4a, C1; `argmap/NOTES.md` judgement call 3), so "literature" tallies mix published papers with the audit's own results. Defeater `audit_status: upheld` is assigned by the audit about attacks many of which the audit itself made (108 of 271 defeaters as of the 10-09 draft; `R5-draft.md` §4.1).
- **Why it matters.** The trichotomy is the best idea in the method. It stays clean only if the auditor is visibly a party when it acts as one.
- **Who raises it:** methodologist. **Fair.**
- **Remedy.** Add `side: audit`. Report audit-made attacks separately from attacks found in the corpus.

### MA-16. From "the simulation shows" to claims about hominids
- **Severity:** MINOR (well disclosed). **Category:** model dependence.
- **Evidence.** `HANDOFF.md` l.105 states the tested regimes. `QUEUE.md` L2: hardness h is "the key unsourced parameter"; R is "unsourced"; no sourced human beneficial DFE exists. `REVIEW-R4-FMnull-prerun.md` finds unsourced brackets, an artefact term of unknown size and asymmetric scoring, before the run.
- **Why it matters.** Where the deciding parameter is unsourced, the verdict should be the conditional itself. The write-ups mostly do this ("flips at an adaptive non-coding share of about 0.01-0.6%"); the single-word verdict column then loses it (MA-08).
- **Remedy.** As MA-08, plus a per-check table "parameter, source or UNSOURCED, range, effect on verdict".

### MA-17. Presentation manufactures symmetry
- **Severity:** MINOR. **Category:** presentation.
- **Evidence.** The README scorecard pairs "Where Day holds up" with "Where the critics hold up", twelve rows each. The rows are not of equal weight: "N_e really does set the fixation timescale" faces "k = μ for any N_e", which removes a branch. Section titles follow a "right, but" pattern ("Day's formula is right, but its premise is not"). `R5-draft.md` §4.4 offers equal MAJOR counts from the two steelman reviewers as evidence of balance; two role-prompted reviewers asked to find problems will each find a handful.
- **Why it matters.** Equal row counts read as an even contest. If the load-bearing verdicts are not even, the format misstates them; if they are, it should be shown by weight. Either way the format should not carry the message.
- **Who raises it:** critic-side ("false balance"); Day-side ("my column is consolation prizes"). **Fair.**
- **Remedy.** Order the scorecard by load-bearing node, one row per node, both sides' best point and the current verdict in the same row. Drop MAJOR-count parity as a balance measure.

### MA-18. Budget decides depth
- **Severity:** MINOR. **Category:** process.
- **Evidence.** `AGENTS.md` l.18-22: tiers, model choice and report length are set by a token budget. 24 of 32 review units since tiering are single reviews.
- **Why it matters.** Triage is legitimate. The choice of what is low-stakes is made by the agent whose work is reviewed, and MA-03 shows it failing in the direction that saved effort.
- **Remedy.** Tier is set by a mechanical test before the check is written (does any proposed verdict move touch a `load_bearing: true` node), recorded in the registration, and cannot be lowered afterwards.

### MA-19. What is missing
- **Severity:** MINOR each; together MAJOR. **Category:** missing elements.
  - **Threat model.** No statement of what kinds of error the method is built to catch (arithmetic, misquotation, wrong model, biased selection, fabricated source, tampered download) and which it cannot.
  - **Priors.** No statement of what the owner and the model believed at the start. The icon note in `HANDOFF.md` l.107 is the nearest thing.
  - **Error rate of the audit.** Corrections of the audit's own errors are logged (a 41x error in the keruru tail; three withdrawn findings), but there is no estimate of how many remain. The seeded-error test in MA-01 would give one.
  - **Inter-rater reliability.** One measurement exists, 90% on Day nodes and 100% on critic nodes, and it was not blind.
  - **Conflicts of interest.** None stated: who pays, the owner's relation to either camp, that the auditing model's vendor is neither party.
  - **Reproducibility for an outsider.** Raw sources are gitignored (rightly) with hashes; there is no one-command refetch-and-verify, no licence file, and compute instructions assume the owner's hosts.
  - **A single limitations section.** The material exists in `HANDOFF.md`; it is not on the README or the status board.
- **Remedy.** The "Methods and limitations" text below; `make verify-quotes`; a LICENSE; a `COI.md`.

### MA-20. Documents disagree with practice
- **Severity:** COSMETIC, except the first item.
  - `HANDOFF.md` l.19 "Every check gets three reviews" has been untrue since 10-09. This is a methods claim in the document addressed to outside assessors. Fix today.
  - `HANDOFF.md` l.18 "The prediction is written down before the run": see MA-04.
  - `AGENTS.md` l.46 against the rule text on RD (MA-03).
  - `docs/research/README.md` Status table still says 193 claims and lists round-2 work as current.
  - Verdict totals differ by one from the claim files in five cells.

---

## Criticisms a hostile reader will make that are unfair

| Id | Criticism | From | Why unfair | Pre-empt by |
|---|---|---|---|---|
| U-1 | "The audit exists to debunk Day." | Day-side | It credits him on B1's formula, the Hard Limits exponent, the LTEE rate, Haldane's regime, the critics' double count, GAP-05; it withdrew three of its own findings against him. | Lead with the list of points decided for him, by node. |
| U-2 | "The audit exists to launder Day." | Critic-side | It records `misread` on nine Day citations and `contradicted` on sixteen Day claims, and states that 205M counts base pairs. | Order the scorecard by weight (MA-17). |
| U-3 | "An AI cannot do mathematics, so nothing here counts." | Either | The checks are executable, seeded and re-runnable; HF reproduced 696 jobs across two hosts with 0 mismatches. The right objection is correlated review (MA-01). | Publish the seeded-error catch rate. |
| U-4 | "Claude co-wrote Day's papers, so the audit is compromised in his favour." | Critic-side | Shared model family cuts both ways and is disclosed. No evidence of deference appears in the verdicts. | Keep the disclosure; add a different-family reviewer. |
| U-5 | "Pre-registration was faked." | Either | Not shown. The long runs are registered for real; the short ones disclose non-blindness in their own docstrings. | Relabel (MA-04). |
| U-6 | "The cross in the icon shows the agenda." | Critic-side | A logo is not a method. | A COI statement that addresses it in one sentence. |
| U-7 | "Rule changes prove the owner steers the outcome." | Day-side | The same evening's changes moved B9 for Day and B against him, and all readings are kept. | Freeze the rule; decision log (MA-03). |
| U-8 | "Treating Day's arguments at all is false balance." | Critic-side | An audit of a published argument on its own basis is a normal scholarly act, and the internal/external split prevents granting his premises. | State the stance (MA-05, remedy 2). |

---

## Hostile reviews

### (a) A sharp reader on Day's side

> You call this an audit of *Probability Zero* and you have not opened it. You read my blog comments, promoted some of them to "claims" by a process you admit is "outside the rule", and scored a combox aside from September as a node.
>
> Your judges are one judge. Every "steelman for Day" is the same establishment-trained machine wearing my hat for ten minutes, and then the author of the check decides whether my steelman's objections are "applied" or "declined". In sixty-five reviews the only thing that ever blocked a check was an import bug.
>
> When your simulation of a Wright-Fisher population returns k = μ you write "external: supported" beside my critic's name. That is a theorem of the program. You tested your code and called it nature. Your own plan says only data settles the external column.
>
> On the evening of 11 October you invented a rule about my rhetoric, applied it, found that it gave my neutral-theory claim a "holds", and four minutes after integrating it you redefined "charitable" so the same claim became "non-sequitur". The commit says so. You did this to a load-bearing node with no review. The same night you declared my LTEE ceiling "contradicted" on one review whose own finding was that the author set the trigger and then scored it.
>
> You have marked my dN/dS result "contradicted" using a different assembly and a different gene set from mine, while your own like-for-like rerun sits in the queue.
>
> You publish all of this about me by name and have never written to me.

**Which points land.** The book (MA-09). The single judge and author-adjudicated reviews (MA-01). The simulation-as-external point, for the nodes it applies to (MA-05). The 10-11 sequence on B and A2e (MA-03); this is the most damaging passage because the commit log confirms it line by line. DN1-DN3 before L1b (MA-12). No right of reply (MA-10). **What does not land:** the implication of intent. The alternative readings are preserved, B9 moved his way the same night, and comment-derived nodes exist on the critics' side too (A2i, B3i, G5).

### (b) A sharp evolutionary biologist who thinks the audit grants Day too much

> This project spends hundreds of compute hours establishing that the neutral substitution rate is the mutation rate, which has been in textbooks since 1968, and then files the result under "where the critics hold up" as though it were a contribution by a YouTube commenter.
>
> Its favourite word is "contested". Two-thirds of its external verdicts are "contested", including claims no working population geneticist contests. A reader counting cells will conclude the field is evenly split on whether evolution is mathematically possible. Its front page gives Day twelve wins and his critics twelve wins.
>
> It scores "internal validity" on the author's own basis, so Day earns sixty-six "holds", many for arithmetic performed correctly on premises that are false or that he has withdrawn. "Holds, misread, contradicted" is three words for "wrong".
>
> When Day says drift "isn't happening at all", the audit runs a calculation to decide whether he was speaking literally, and concludes that on one reading he was only being rhetorical, so the sentence is not scored. A scientist does not get to be 23 times off and exempt.
>
> The audit follows his blog day by day and builds a new pre-registered study for each post. He produces a claim in an afternoon with no code and no data; the audit answers with a registered study, a multi-host run and three reviews. That asymmetry of effort is the whole strategy of the genre, and the audit has no stopping rule against it.
>
> And it invents "gaps" in the mainstream account and credits them to him as his "best point", though he never made the argument.

**Which points land.** `contested` as a sink (MA-08). The paired scorecard (MA-17). `holds` on withdrawn or false premises being counted as a tally (MA-07). The rhetoric exemption for large errors (MA-02); note it protects Myers's "debunked" by the same mechanism. No stopping rule (MA-11). **What does not land:** re-deriving textbook results is the correct method when the textbook is what is disputed, and it belongs in the internal column where it is decisive. Scoring on the author's own basis is what stops the audit from simply asserting the consensus; the fault is in the counting. The gaps ledger credits by who is helped and says plainly when no party made the argument (`balance.md`, "Credit goes to whoever made the argument").

---

## Remediation plan

### Quick wins (hours)
1. Correct `HANDOFF.md` l.18-19 and `AGENTS.md` l.46; fix the stale "most charitable to Day" comments in C7 and B9 (MA-20, MA-03).
2. Remove Fisher p-values and comparative error rates from README, HANDOFF and the board; keep X1's "not robust" sentence (MA-06).
3. Label DN1-DN3 as conditional on the hg38 pipeline until L1b reports (MA-12).
4. Mark round-1 and round-2 checks "prediction order not verifiable from history"; relabel the thirteen tight-gap checks `criterion-prereg` or `reproduction` (MA-04).
5. Re-open B (internal) and A2e (external) at the three-review tier, or revert them to their pre-10-11 values until that is done (MA-03).
6. Start `DECISIONS.md` with the 10-09 to 10-11 owner decisions, verbatim where the owner can supply the words.
7. Add LICENSE and `COI.md`; put the limitations text below on the README.
8. Describe the object of audit as the Zenodo papers and blog until the book is read (MA-09).

### Structural fixes (days)
1. Seeded-error test of the review pipeline; publish the catch rate (MA-01).
2. Blind re-derivation of ten load-bearing nodes from quote and raw source only; report agreement (MA-01, MA-19).
3. Blind re-extraction of a random 30 claim files (MA-09).
4. Verdict vocabulary rev 3: `unexamined`; `contested` split four ways; `external_basis` field with lint; `side: audit`; `reading-dependent` as a field value excluded from tallies (MA-05, MA-07, MA-08, MA-15, MA-03).
5. RH rev 2: genre by contextual criteria fixed in advance; literal distance always reported; no multiplicative band on absolutes; no scoring against the audit's own tallies (MA-02).
6. Three-level pre-registration labels with pushed timestamps; bands must partition outcomes (MA-04).
7. Mechanical tier test fixed at registration (MA-18).
8. The mirror tree and a two-tree coverage table (MA-13).
9. Register the aggregation rule, the falsifier for the audit's own conclusion, and a corpus freeze date before any R5 text is drafted (MA-11).
10. One-command quote verification for outsiders (MA-19).

### Only the owner can do
1. Buy and supply *Probability Zero*, both editions.
2. Decide on right of reply and send the notices (MA-10). This requires lifting hard rule 6 for that purpose.
3. Recruit a human population geneticist for the five heaviest checks, and one reader from each camp for the rule text and the load-bearing list.
4. Authorise a non-Claude model for one review seat.
5. Adopt the cooling-off rule and the rule freeze.
6. Write the priors and COI statement in his own words.
7. Decide whether the audit continues to track Day's new posts or freezes its corpus.

### Proposed text: "Methods and limitations"

> **What this is.** An examination of the mathematical arguments in Vox Day's Zenodo papers and blog posts on evolution (2019 to the freeze date), and of the published replies to them. The book *Probability Zero* [has / has not] been read; claims known only from it are marked secondhand.
>
> **Who did it.** AI agents (Anthropic's Claude models) directed by one person, [name]. Every check, every review and every "steelman" was produced by the same model family. Reviews were not blind to the proposed verdicts, and the author of each check decided how to answer its reviews. No human specialist has checked the simulations [update when true]. Some of Day's papers credit a co-author from the same model family.
>
> **Stance.** Standard population genetics is treated as the default model. The audit asks whether Day's arguments defeat it and whether his critics' replies are themselves correct. It does not test standard theory against a rival of equal standing.
>
> **Verdicts.** Each claim is judged three ways: whether it follows from its author's own premises; whether its citations say what is claimed; whether its premises fit the world. A verdict in the third column is marked by its basis (data, simulation, theory, literature); only data-based verdicts speak about real genomes. "Holds" means examined and found to follow; unexamined claims are marked so. Tallies across claims are not comparable between sides, because the sides wrote different amounts, at different precision, and received different depths of checking. We do not report an error rate for either side.
>
> **Pre-registration.** [n1] checks had predictions pushed to the public repository before any run. [n2] fixed their criteria in advance with the numbers already known. [n3] are reproductions with nothing at stake. The first [n4] checks were committed together with their results and their order cannot be verified.
>
> **Rules.** The verdict rule was written after the first verdicts were known and was revised on [dates]. Each revision and the verdicts it moved are listed in [file]. The rule is frozen as of [date].
>
> **Known error.** In a seeded-error test the review process caught [k] of [n] planted defects. [m] of the audit's own published statements have been withdrawn or corrected; they are listed in [file].
>
> **Right of reply.** The authors examined were sent the verdicts on their claims on [date]. Replies are published unedited at [path]. [Or: have not been contacted.]
>
> **Not covered.** [Platforms and paid sources not reached; regimes not simulated; parameters with no published source.]
>
> **Interests.** [Owner's statement.]

---

## What I did not examine

- The correctness of any derivation, simulation or number. Nothing was re-run.
- Most of the material: I read the rule file in full; method sections of `AGENTS.md`, `PLAN.md`, `HANDOFF.md`, `argmap/NOTES.md`, `R5-draft.md` §4 and header, `QUEUE.md`; the balance and slips ledgers; front matter of all 233 claim files by script and the verdict blocks of about fifteen by eye (ROOT, A2e, B, B3a, B5c, B7, B9, C7, F1, FM10, G2e, H5, B1c, D10, DN1-DN3); the B9 script docstring, write-up and review in full; RHclose-critics write-up, RHclose review, FMnull pre-run review, the head of the L1c pre-run review, headers of the L1 and HF three-review sets and of HF's write-up, and the X1 rule audit's method section. GAP05, L1 and HF bodies, the fidelity, versions and gaps ledgers, and the early write-ups were grepped, not read.
- The raw sources. No quote was compared with its original.
- The status board (`status.html`), the milestone posts beyond titles and two grep hits, the explainers, the argument-map renders, and `defeaters.yaml`.
- The harvest and lint tools, and whether the lint enforces what the README says it enforces.
- Chat transcripts in which owner decisions were made; they are not in the repo.
- Whether the timing table reflects agent working order or only commit order. It cannot be told from git.
- The classification of the roughly twenty model-based external verdicts in MA-05 is my reading of one-line comments, not a coded count.
- Anything on na-workhorse or builder.
