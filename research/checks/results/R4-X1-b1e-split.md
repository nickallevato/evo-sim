# R4 X1: the B1e split, decided and designed (EVO-96, B-R33's countermeasure)

**Status: decision and design. Nothing in this file is applied.** No claim file, `hierarchy.yaml`
entry, argmap file, count or board page is edited by it. Written 2026-10-18 by the lead (Big Sim).

B-R33 (`docs/research/DECISIONS.md`, 2026-10-18, commit 44a1c60) records the split as the
countermeasure to the conjunction rule and names B1e as the candidate: "where a claim's Statement
quotes assert propositions that do not stand or fall together, the claim is split into one node per
proposition. B1e is such a candidate and is **not** split in EVO-12 (a split touches
`hierarchy.yaml`, the argmap and the board); the lead files it separately." This file is that
separate filing: section 1 corrects the premise the task was written on, section 2 decides, sections
3-8 design, section 9 rules the tier, section 10 sets the execution order and the gates.

## 1. The task's premise is stale: B1e's external field no longer has a weakest conjunct

EVO-96's description reads: "Under the conjunction rule its external field is carried by QB at
`contradicted` while the Zenodo statement is `contested`, which is accurate but coarse." That was
true of **B-R32**, which ruled QB's external value `contradicted` under reading R-A. It is no longer
the record. **B-R35** (`DECISIONS.md`, 2026-10-18, after the D-24 fresh-reviewer check
`results/REVIEW-R4-B1e-Q2-ruling-check.md`, EVO-94) accepted that review's MAJOR RC-1 in full and
re-ruled QB's external under R-A to **`contested`, the registered value**, with `supported` barred
on P3 with P4.

The live record in `claims/B1e-chalub-2022-reading.md` front matter is therefore:

| field | Zenodo conjunct (Q292/Q288/Q286, governing reading A) | QB conjunct (Q297, governing reading R-A) | field value | carried by |
|---|---|---|---|---|
| internal | `holds` | `holds` | `holds` | neither alone (B-R35, RC-5) |
| fidelity | `partial` | `partial` | `partial` | neither alone |
| external | `contested` | `contested` | `contested` | neither alone |

All six conjuncts match their field. **There is no coarseness left to fix on any value today, and no
quote carries any field.** The whole of the task's stated motivation has been removed by B-R35.

This matters in both directions and is recorded as such: it removes the only argument for the split
that cost nothing to state, and it also removes the only way the split could have been read as
smuggling a value move. **Designed as below, the split moves no verdict value and no governing
reading.** That fact, not the task's premise, is what section 9's tier ruling rests on.

## 2. Decision: split, on grounds independent of the conjunction rule

**Ruled: yes, split.** Not because the fields disagree — they agree — but because the node fails the
B-R33 separability test on its content, and because two defects that have nothing to do with CJ are
fixed by the same edit. Each ground is stated so that a reviewer can reject it on its own.

**G1. The two propositions do not stand or fall together, and nothing about them is shared except
the cited author.** They have different sources (Zenodo 22903977, a paper of Day & Athos, against
voxday.net 2026-08-23, a blog post), different subject matter (the finite-time convergence of
Chalub's Gegenbauer expansion and the relayed asymptote F(T) = exp(−π²Nₑ/T), against the provenance
of the 1/(2N) boundary condition in Chalub's integral constraints), different scoring checks (B2f
against B1e-Q2), and disjoint reading sets (A/B against R-A/R-A0/R-B/R-C). No premise is common: the
asymptote proposition would survive intact if Chalub's boundary split turned out to be derived
rather than imported, and the provenance proposition would survive intact if the asymptote relay
turned out exact.

**G2. Each of B1e's two edges is carried by exactly one of the two quotes, so the node's edges are
false as recorded.** `supports B1` ("k = mu is a steady-state identity; finite-time count differs")
is carried entirely by the Zenodo asymptote quote; the 1/(2N) provenance claim says nothing about
steady state against finite time. `supports B7` ("Neutral fixation probability is 1/(2N) ... not
1/(2Ne)") is carried entirely by QB; the asymptote quote says nothing about the value of P_fix. Both
B1 and B7 are `load_bearing: true`. As the node stands, each load-bearing parent is told it is
supported by a node half of whose Statement is irrelevant to it. This is an argmap defect that
exists whether or not CJ is ever adopted.

**G3. The title is a literal conjunction and reads as one.** "Chalub 2022 shows k = mu is an
asymptote / 1/(2N) is imported from Wright-Fisher" — the slash is the conjunction. Every field's
comment now has to carry nine readings across two propositions (A, B, R-A, R-A0, R-B, R-C plus the
superseded-wording note), and the three `verdict_scope` lines run to 90, 120 and 190 words to keep
them apart. The external scope line is the longest single field in the corpus.

**G4. The equality of the six conjuncts is a coincidence of labels, not a finding, and it is
fragile.** The claim file says so in terms, of B1e-Q2's registered values: "the match is a
coincidence of labels, not one verdict covering both quotes." One open item can break it now —
Kimura (1955) primary text, an owner decision on outside input, with P8 at band U — and the
conjunction survey's own limitation says the same thing generally: "Any future check that scores a
second Statement quote of a load-bearing claim puts that claim's field back under this clause." Each
such future check on B1e would arrive carrying a verdict-field flip and three reviews, on a node
where the flip is an artefact of two propositions sharing one field.

**What is given up, recorded against the decision.** The split costs a day of bookkeeping and buys
no value movement today; it adds a 235th claim to a public count that is already two behind
(the board says 233 against a live 234); and it is irreversible in the sense that merging the nodes
back would need its own task. A reviewer who weighs G1-G4 as cosmetic should say so, because on the
record of section 1 that is an honest reading and the decision then goes the other way.

**The alternative considered and declined.** Leave B1e conjoined and add a per-quote table to the
Statement section. Declined on G2: a table inside the node cannot make the `supports B7` edge
honest, because the edge is a property of the node, not of a quote. The hierarchy cannot express
"this node supports B7 through its fourth quote only".

## 3. Design: the two nodes

### 3.1 B1e, narrowed (the Zenodo asymptote relay)

- **id** `B1e` (kept: it is the node B2f scored, and `chk:B2f`, d473, review #82, the lineage node
  and the mini-form all point at it).
- **title** `Chalub 2022's expansion converges to the steady state only as t -> infinity; the
  finite-time completion fraction is F(T) = exp(-pi^2 Ne/T)`
- **side** `day`; **branch** `B`; **parent** `B1`; **sourcing** `firsthand`; **status** `reviewed`.
- **edges** `[{type: supports, target: B1}]` — the `supports B7` edge moves to B1f.
- **load_bearing** `false`, unchanged, with its existing comment.
- **verdicts** `internal: holds`, `fidelity: partial`, `external: contested` — **every value
  unchanged, and reading A still governs all three.** The comments keep their reading-A/reading-B
  text exactly, and lose only the B-R35 sentences about the QB conjunct and about the superseded
  "was not examined by B2f" wording.
- **verdict_scope** drops the conjunction half of each line and keeps the RD half. Draft of the
  three, in full, in section 7.1.
- **Quotes** Q292 (the 2026-09-22 wording, with the version note), Q288, Q286. Front-matter and
  Statement-section references to Q289, Q291, Q293, Q294, Q295 stay as they are: they are cited in
  the readings and the R4 B2f section, not Statement quotes.
- **Sections kept** Version note; Primary literature rows 1 and 3 (row 3, "Finally, the
  time-dependent fixation probability is given by", is the row the asymptote reading is scored
  against); R4 B2f in full, with the readings table and "What Reading A costs".
- **Sections moved out** Formal statement, second sentence onward; the derived-reasoning note;
  Assumptions (both); Responses "Weaknesses"; Pre-registered prediction (all three bullets);
  Simulator variables implied; R4 B1e-Q2 in full, with the QB readings and the B-R31..B-R35 record;
  the Locator note; Primary literature row 2.
- **Statement sentence after the split** the first sentence of the Formal statement becomes "Chalub
  2022: PDE for a two-allele neutral population 'without mutation or selection', classical solution
  decays; Day's reading: the expansion reaches the steady state only in the limit, and the
  finite-time completion fraction is exp(−π²Nₑ/T)."

### 3.2 B1f, new (the 1/(2N) provenance claim)

- **id** `B1f`. Next free id in the B1 subtree (B1a-B1e exist). Chosen over a B7-series id so that
  the Chalub cluster stays under B1 and so that `chk:B1e-Q2`'s own id keeps pointing at a node whose
  id it names.
- **title** `Chalub 2022 shows the 1/(2N) is an assumption imported from Wright-Fisher, not a result
  produced by the mathematics`
- **side** `day`; **branch** `B`; **parent** `B1`; **sourcing** `firsthand`; **status** `reviewed`.
- **edges** `[{type: supports, target: B7}]`, inherited from B1e. Parent and edges are independent
  in this schema and the precedent is B7 itself (parent B3, edges `attacks B3a` / `supports B5`), so
  a Day-side node parented under B1 and supporting the critic-side B7 needs no new convention. It
  supports B7 in the sense the claim file already records: Day's own post states "Impose that
  assumption and the fixation probability comes out equal to the starting frequency", which concedes
  the value while disputing its provenance.
- **load_bearing** `false`, with the comment `# cited as support, not as a step in any calculation`
  carried over from B1e. B1e's non-load-bearing status was never contingent on the asymptote half:
  no calculation in the corpus takes a step through either proposition.
- **verdicts** `internal: holds`, `fidelity: partial`, `external: contested` — **the same three
  values B1e shows today**, now carried by QB alone under its governing reading R-A, which is
  unchanged. This is the heart of the design: the split is a re-homing, not a re-scoring. B-R35
  fixed every one of these values 2026-10-18 and none of them is reopened here.
- **verdict_scope** the RD lines only. Draft in section 7.2.
- **Quotes** Q297 (QB) as the single Statement quote; Q298 (the containing paragraph), Q303 (the
  circularity sentence, D5) and Chalub's own text Q304-Q311 (C1, C13, C2, C3, C4, C7, C9, C12) in
  the body, as the claim file already cites them. Q299-Q302 do not move: they are already scored at
  B3c, B3e, B6 and B3a.
- **Primary literature** Chalub 2022 rows 1 and 2 ("without mutation or selection"; "Its solution is
  required to satisfy not only the equation but a series of conservation laws formulated as integral
  constraints", `accurate`). Row 1 is duplicated on both nodes; it fixes the model class for both
  propositions and is the cheapest honest way to keep each node readable on its own.
- **file** `docs/research/claims/B1f-chalub-1-over-2n-imported.md`, built from `_TEMPLATE.md` with
  the sections listed as moved in 3.1.

## 4. Defeaters: one each, no new defeater, no re-numbering

The two defeaters that target the B1e **node** split one per proposition, which is the sharpest
single piece of evidence for G1:

| id | attacker | target now | target after | why |
|---|---|---|---|---|
| d473 | `chk:B2f` | `B1e` | `B1e` | B2f scored the Zenodo asymptote only; the note already says "Targets B1e only (not load-bearing)" |
| d490 | `chk:B1e-Q2` | `B1e` | **`B1f`** | its locator is R4-B1e-Q2 P3, P4 — the classical solution's own integrated outflux at x = 1, a defeater of the "not a result produced by the mathematics" half only, in B-R35's own words |

d474 and d475 target `chk:B2f`, and d491 targets `chk:B1e-Q2`; all three are check-node defeaters and
are untouched. `hierarchy_edge: false` stays correct on d473 and d490 after the move: neither B1e nor
B1f is load-bearing and no value moves. **No `dNNN` is added and none is renumbered.** The d490 note
gains one clause recording the re-home and this file as its locator.

## 5. Argmap, lineage and standard forms

- `argmap/NOTES.md`: add a registry row for `B1f` with this file as the locator and the date; amend
  the `chk:B1e-Q2` row (line 286) to name B1f as the node it scores, leaving its id unchanged; leave
  the `chk:B2f` row and the four `rev:` rows alone.
- Lineage: B1e's lineage node keeps its history (it is the same node, narrowed). B1f gets a new
  lineage node whose first entry is the split, dated, with B1e named as the node it was carved from,
  so the provenance of its three values is traceable to B2f's registration and B-R35 rather than
  appearing to be set by this file.
- `standard-forms.md`: B1e's mini-form loses its second premise; B1f gets a mini-form whose premises
  are QB, Chalub C1/C2/C13 and the P5 identity, with P3-with-P4 as the recorded defeater.
- `defeaters.yaml`: the single `target:` edit in section 4, plus the note clause.

## 6. Counts and the board

| counter | now | after | where |
|---|---|---|---|
| claim files (scored, `_TEMPLATE.md` excluded) | 234 | **235** | `lint_research.py`, `docs/arguments/README.md`, `README.md`, `docs/HANDOFF.md`, the systems figure via `readme_figs.py` |
| claims carrying a reading-dependent verdict | 8 | **9** | `status.html` line 138 — both nodes are reading-dependent |
| typed objections | 468 | 468 | unchanged (section 4) |
| verdict tallies by value | — | unchanged in **distribution shape only if counted per node**: one more `holds`, one more `partial`, one more `contested` | `lint_research.py`, board tallies |

The third row is the one a reviewer should press on. The split does not move a value, but it does add
a node, so the per-node tallies the board prints each go up by one. That is a count change, not a
verdict change, and the board patch must say so in those words or it will read as three new findings.
The board's claim figure is currently **233** against a live 234, so the patch that lands the split
also clears that existing lag; both are count corrections and belong in one patch note.

## 7. Drafted `verdict_scope` lines (not applied)

### 7.1 B1e after the split

> **internal** "Scope: reading-dependent (rule RD). Reading A, a relay of Hard Limits' short-time
> asymptote, governs and is `holds`, with ledger slips S-B2f-1..4; reading B, the literal equality
> with no domain, is `non-sequitur` against the paper's own F_X integral, mean 4Nₑ and SD (Q293,
> Q294). The 1/(2N) provenance claim and its quote QB (Q297) are no longer in this node's Statement:
> they are B1f (split YYYY-MM-DD, R4-X1-b1e-split.md)."
>
> **fidelity** "Scope: reading-dependent (rule RD), value unmoved. Reading A governs - Hard Limits
> is cited and relayed with its domain omitted, `partial`; reading B is `misread`. The Chalub-link
> half stays `partial` on the ledger basis, P8 band U, the P7 value item having been ruled
> mis-specified (B-R34) and the E-line identity being post hoc and descriptive."
>
> **external** "Scope: reading-dependent (rule RD). Reading A governs - the exponent is supported in
> logarithms (exact as T/Nₑ → 0) and 'every application of k = μ ... is guaranteed to be incorrect'
> is `contested` on the start state only (true from an empty start, the paper's premise; from a
> stationary start the flux is exactly μ; scored at B1, B1c, B6a); reading B is `contradicted` by the
> exact diffusion at every T."

Each is the B-R35 line with the conjunction clause and the QB clause removed and nothing else
changed. The fidelity line keeps its P8/P7 sentence because the Chalub-link question (whether
Chalub's expansion is the Kimura 1955 series) is about the asymptote relay's own route and stays
with B1e.

### 7.2 B1f, new

> **internal** "Scope: reading-dependent (rule RD), carried by the single Statement quote QB (Q297).
> `holds` under every registered reading (R-A, R-A0, R-B, R-C; T2, B3d) - R4 B1e-Q2, value set by
> B-R35 2026-10-18 and not reopened by the split."
>
> **fidelity** "Scope: reading-dependent (rule RD). R-A governs and is `partial`: QB narrows
> Chalub's 'the Moran and the Wright-Fisher processes' (C3, C13) to Wright-Fisher and relabels
> 'derived directly from the discrete process' (C1) as 'assumption' (D6, SC3). `misread` under R-A0
> and R-B, `partial` under R-C (D7), none field-setting."
>
> **external** "Scope: reading-dependent (rule RD). R-A governs and is `contested` (the registered
> value, B-R35 accepting EVO-94's RC-1): true that Kimura's equation (7) on the open interval with
> probability conservation alone leaves the fixation/loss split free unless mass leaving at one end
> may be booked at the other (P5, an identity), the two laws being added from the discrete process
> (C1, C2); false that the value is an input, the classical solution's own integrated outflux at
> x = 1 being ∫x p^I (P3 with P4), which is why `supported` (D1) is barred. R-A0 and R-B
> `contradicted`, R-C `supported` (trivially), none field-setting."

Under CJ as drafted, each line is now a single-conjunct scope line and CJ never fires on either
node. That is CJ5 working as written, and it is the only sense in which this split depends on CJ at
all: CJ5 names the split as the remedy, but G1-G4 do not need CJ to be adopted to be true.

## 8. Who this helps

**Day's side.** The split is the one remedy in B-R33 that can *raise* a Day node's field, and it
removes the mechanism that would have lowered one: as long as the two propositions share a field,
any later check that scores the blog sentence down drags the Zenodo paper's verdict with it, and any
later check that scores the Zenodo relay down drags the blog sentence's with it. Day is entitled to
have his paper judged on the paper and his blog post judged on the blog post. Concretely, the open
Kimura (1955) item (P8, band U) bears only on B1e's relay route; after the split it cannot reach the
1/(2N) argument, which is the half B-R35 found Day's strongest ground on (P5 with its non-local-
booking qualifier, and Chalub's own "had to be introduced into the model", Q306).

**Critics' side.** The split does not undo what SC6 won. B-R33's bar on taking the better conjunct
stays, and the split is not a route around it: it is available only where the propositions are
separable on their content, which is CJ5's wording and is why G1 is argued on sources, subject
matter, checks and readings rather than on the values. The critics' own defeater against the "not a
result produced by the mathematics" half (d490, P3 with P4) gets a cleaner target after the move: it
now attacks the node that asserts that half and nothing else. And the critics gain the honest edge:
B7, a critic node marked load-bearing, is currently recorded as supported by a node half of which is
about a different subject.

**The audit.** The main product is section 1 — the task's own premise was overtaken by B-R35 seven
hours after it was filed, and the split as designed moves no value and no governing reading. The
second is section 4: the two node-targeting defeaters split one per proposition without a new id or
a renumber, which is independent evidence for separability that nobody designed. The limitation: the
split buys no value movement today and its case rests on G2 and G4, an argmap defect and a
prediction about later checks. That is a thinner case than the task assumed and a reviewer may rule
it insufficient.

## 9. Tier: D-23's literal triggers do not fire, and the ruling is put back to the owner

EVO-96's description says "it carries a verdict-field flip in substance — expect three reviews, and
confirm the tier against D-23." Confirming it, honestly, gives a different answer:

- **D-23 trigger 1, "a check's registration carries a verdict-field flip":** does not fire. There is
  no check and no registration; and after B-R35, no field of either node changes value or governing
  reading (sections 3.1, 3.2, 7). The task's "flip in substance" was written when the external field
  was expected to go `contested` → `contradicted` under B-R32.
- **D-23 trigger 2, "its node is a listed feeder of a load-bearing node (`R5-draft.md` 1.3)":** does
  not fire. 1.3's list is G/G1, A3/A3a/A3x, C/C6/C1c, E, A6/GAP-02, D. B1e is not in it.
- **The load-bearing test in `AGENTS.md`** ("they move a ROOT-path node"): does not fire. Neither
  node is `load_bearing`, and no value on B1, B7, B or ROOT moves.
- **What does point upward:** the split rewrites the carriage of all six verdict fields, re-homes a
  defeater, changes both edges of a node feeding two load-bearing parents (B1, B7), and moves two
  public counters.

On the letter of the rules this is **one combined review** — AGENTS.md's low-stakes tier is
"re-confirmations, bookkeeping, tool validation", and a change that moves no value and no reading is
bookkeeping. On the substance a reviewer could reasonably want three. The lead's ruling is **one
combined review (`REVIEW-R4-X1-b1e-split-combined.md`, a correctness section and both steelman
sections, same severity labels), with the D-24 fresh-reviewer check firing automatically if
execution moves any value or any governing reading** — which, as designed, it does not, so the
combined review's first job is to check exactly that claim. Because the owner's own task text said
three, this ruling is **put to the owner before execution** and is not acted on until answered. If
the answer is three, the three run one after another under the one-agent cap (D-22).

## 10. Execution order and the gates

Two gates, both from EVO-96's own text, and their current state:

1. **EVO-12 complete** — **met.** Integrated 2026-10-18, bookkeeping only, commit 3c9df34 fix pass;
   B1e's fields were not touched by this file.
2. **EVO-95 settled on whether the conjunction rule is general** — **not met.**
   `results/R4-X1-conjunction-survey.md` is a survey and proposal only; its §4 amendment B-R33a
   restarted the O-6 cooling-off, so the earliest adoption of CJ as amended is **2026-10-19
   07:59 UTC**, about 23 hours after this file was written. Its other dependency, EVO-94 clear on
   B-R33, is met (EVO-94 confirmed B-R33's rule with RC-5's and RC-6's corrections; only B-R32's
   value was rejected).

Execution is therefore **held to 2026-10-19 07:59 UTC or later**, after CJ is adopted. The split is
CJ5's remedy and should not land before the rule whose remedy it is; and if the combined review of
CJ's adoption text changes CJ5, section 7's single-conjunct scope lines change with it.

Order once both gates are clear and the tier is answered:

1. Commit this file (done, pre-registration of the design in the B-R33 sense: the design is fixed
   before the edit).
2. Review per section 9; the lead rules any steelman conflict in writing before the fix pass (D-24).
3. Fix pass answering every MAJOR and MINOR.
4. Edit, one agent, one commit, explicit paths: `claims/B1e-chalub-2022-reading.md` narrowed; new
   `claims/B1f-chalub-1-over-2n-imported.md`; `defeaters.yaml` d490 target and note;
   `argmap/NOTES.md` rows; lineage node; `standard-forms.md`.
5. `lint_research.py --write-hierarchy`, `argmap_check.py`, `argmap_render.py`, `readme_figs.py`;
   `git checkout` SVGs whose only change is random ids; refresh the counts in section 6's four
   files.
6. `REVIEW.md`, `QUEUE.md`, `RESULTS.md`.
7. **Board: its own task, under the publication gate.** `board/updN.py` against the current files of
   record, then `scope_guard.py`, then publish per D-26. The patch carries section 6's count
   changes and the existing 233 → 235 correction, with the note that no verdict value moved. The
   **B-R20/B-R21 hold** and the open **B-R30** item (EVO-92) both still bind: nothing is published
   while they stand, and no board written before a verdict field moved is published.
