# Quote-miss diagnosis: the 4 standing `argmap_check.py` errors (EVO-78)

**Date:** 2026-10-14. **Branch:** `research`, reproduced at `e2bc2f1` (the ticket cites `18dbaec`; both give the same 4 errors, 0 warnings).
**Scope of the original pass: diagnose and propose only.** Findings are numbered QM-01..QM-04.
**Resolved 2026-10-14** — the owner ruled on all three questions (EVO-78) and the remedies were applied; see "Resolution" at the foot of this note. `argmap_check.py` now reports **0 errors, 0 warnings**. The diagnosis above the Resolution section is left as written at diagnosis time.

Classification vocabulary from the ticket: **(a)** transcription or typography drift; **(b)** a paraphrase that was never a verbatim quote; **(c)** a pointer to a source line that has since changed.

## Method

1. Reproduced the lint on a clean tree (`research/.venv/bin/python -I research/tools/argmap_check.py`).
2. Read the matcher: `find_quote()` (`argmap_check.py:200`) normalises with `norm()` (`:94`), which NFKC-folds, maps curly quotes/dashes to ASCII via `_FOLD` (`:85`), strips blockquote markers and markdown emphasis, and collapses whitespace. It then tries, in order: `quote_source` if given; each `claim_ids` file; `repo_corpus()`; `raw_corpus()`.
3. `repo_corpus()` (`:135`) = `docs/research/claims/*.md` + `docs/research/sources/quotes-*.md` + `docs/research/ledgers/*.md` + `research/checks/RESULTS.md` + `REVIEW.md` + `research/checks/results/*.md`. It does **not** include `docs/research/argmap/NOTES.md`, `docs/research/opponents/*.md` or `docs/arguments/`.
4. For each failing quote, binary-searched the longest prefix that *is* present, in `repo_corpus()` and in every file of `raw_corpus()` (62 files), to locate the exact point of divergence.
5. `git log -S` on each quote string to date its introduction.

## QM-00 (precondition): two facts that bear on all four

- **The ticket's curly-apostrophe hypothesis is ruled out.** `_FOLD` already maps `U+2019 → '`, so `doesn’t` and `doesn't` are the same string to the matcher. The Dembski quote's divergence point is at character 8 (`The scal` | `ing element…`), i.e. the capital-T `The` — nowhere near the apostrophe. No miss in this set is caused by quote-mark typography.
- **All three distinct quote strings were introduced in one commit, `9a2148b`** ("R4 E and G1 checks, argument map, gap hunt, and claim-file corrections" — the original argmap build) and have never matched since. **Classification (c) is therefore ruled out for all four**: no source line changed under them; they were never verifiable. These are original-construction defects that predate every integration that has reported them.
- Secondary observation: `sources/raw/` currently holds only the 2026-10-13 fetch directories. The local copies named in `bib-day.md` and `quotes-day.md` (`sources/raw/day/zenodo-18525185.txt`, `sources/raw/refresh-2026-10-09/dembski-interview/`) are gone, so `raw_corpus()` cannot attest anything from Day's Zenodo papers or the Dembski interview today. This is expected under hard rule 3 (raw is gitignored and transient) and is *not* the cause of the errors — but it does mean that remedying QM-02 and QM-03 by re-filing needs a re-fetch, not a local grep.

---

## QM-01 — defeater `d176`: "Multiple mutational paths can lead to similar phenotypes."

**Classification: (a) typography drift — one trailing period. Lowest severity of the four.**

Evidence. The longest matching prefix is **56 of 57 characters**: everything up to `…similar phenotypes` is present in the corpus; the final `.` is not. The string is attested verbatim (without the terminal period) in two corpus members:

- `docs/research/claims/G3b-day-either-specific-or-interchangeable.md:32` — `…which Bowers raises ("Multiple mutational paths can lead to similar phenotypes").`
- `research/checks/results/R4-G1.md:292` — `…Modern population genetics does not require pre-specified targets … Multiple mutational paths can lead to similar phenotypes".`

In both, the sentence's period falls *outside* the closing quotation mark, so the filed text ends at `phenotypes`. `REVIEW-R4-G1-correctness.md:54` records that the reviewer checked this string against the local Bowers source text at the time, listing it among the verified Z-/blog quotes. Verified mechanically: `find_quote("Multiple mutational paths can lead to similar phenotypes", …)` → `repo`.

Not a fidelity problem. But note a **second, weaker point**: the only attestations are audit prose and a claim file, both secondhand (Bowers via Day's 2026-03-04 repost). `quotes-critics.md` BOW section files `BO-01`..`BO-04` and does **not** include this sentence, although it is the sentence `x:BO-paths` (NOTES.md:123) is named for and the one `d176` rests on.

**Proposed remedy (owner's call).**
- Minimal: drop the terminal period from `d176`'s `quote:`. Lint goes green for this id; no verdict field moves; `audit_status: upheld` and `audit_basis` (R4 G1) are unaffected.
- Better, and preferred: also file the sentence as **`BO-05`** in `quotes-critics.md` under the existing BOW heading, with its paragraph locator (Point 1, per `d176`'s own locator) and the `secondhand` tag that `BO-01`/`BO-02` carry, then let `d176` and `L-`/`x:BO-paths` rest on a primary filing rather than on the audit's own write-up. This needs the 2026-03-04 repost text, which is no longer under `sources/raw/`; it belongs in the next source refresh, not in a lint fix.

---

## QM-02 — lineage `L-adna-630-21-2026`: "The clock predicts ~630 fixations per 350 generations. We observe 21."

**Classification: (b) paraphrase — a two-sentence composite, neither half filed as quoted.**

Evidence. Longest matching prefix is **10 of 69 characters** (`The clock `), diverging at `predicts ~630`. The paper's own sentence, as filed in the C6 claim file (`C6-molecular-clock-stopped.md:22`, sourced to **§5.3**), is:

> "The molecular clock predicts approximately 630 fixations per 350 generations (based on k = μ for neutral sites; see Appendix A)."

The node's text differs in three ways from that filing: `The clock` for `The molecular clock`; `~630` for `approximately 630`; the parenthetical dropped. Those are compression, not transcription slips. The node then welds on a **second sentence from a different place in the paper** — `NOTES.md:331` records that `"We observe 21"` is at line 263 of the text extraction, while the §5.3 sentence is elsewhere; the node's own locator says **§9**, which also disagrees with the claim file's **§5.3** for the ~630 half. No quote entry in `quotes-day.md` covers either half: the seven filed Z18525185 quotes are `Q106`–`Q112` (§3.1, §3.3 ×2, §3.4, §4.1, §4.3, Appendix B). `"We observe 21."` is present nowhere in the repo corpus (verified: `find_quote` → `None`); its only record is the ambiguity bullet at `NOTES.md:331`, and `NOTES.md` is not a corpus file.

This is the one of the four that is a **fidelity matter, not a lint matter**: a `day`-side `revision` node presents as a single quotation a sentence Day did not write in that form, stitched to a second sentence from another section. The underlying substance is not in doubt — the ~630 and the 21 are both documented elsewhere in C6, and the node is already `fate: dormant` since 2026-09-29 with `fate_locator` recording that R4 C1b could not reproduce the 21 — so no claim verdict appears to hang on the node's wording. The defect is the presentation.

**Proposed remedy (owner's call).** Three options, in my order of preference:
1. **Repoint at the filed sentence.** Replace the `quote:` with the §5.3 sentence exactly as C6 files it, correct `locator:` from §9 to §5.3, and move the "21 observed" half into `label:` / `fate_locator:` prose where it is already stated. Verified mechanically: the §5.3 sentence resolves to `repo` under `claim_ids: [C6]`. Lint goes green, nothing is asserted that is not filed, and the node keeps its meaning.
2. **File the second half properly, then split or keep both.** Re-fetch Z18525185 at the next source refresh, file `"We observe 21."` as a new `Q`-entry in `quotes-day.md` with its §/¶ locator and sha256-matched local copy, and either give the node the §5.3 quote plus a sibling node for the 21, or leave a single node quoting one sentence only. Strictly better provenance; costs a fetch.
3. **Retract the node.** Defensible if the owner reads a stitched quote on a `day` node as a fidelity breach rather than a sloppy transcription, but it looks disproportionate: the node is already dormant and the facts it carries are filed in C6.

Whichever is chosen, the **§9 vs §5.3 locator discrepancy should be resolved against the paper**, and the `NOTES.md:331` ambiguity bullet updated to say how it was resolved.

---

## QM-03 / QM-04 — lineage `L-dembski-scaling-reply-2026` and defeater `d129` (same string)

> "The scaling element doesn't apply at all, it is entirely irrelevant, because sexual reproductive capacity is the real limit on humans and other non-bacteria."

**Classification: (b) on the evidence available in the repo — unattested, and indistinguishable from "verbatim but never filed" without a re-fetch. The two ids are one defect and should be ruled on together.**

Evidence. Longest matching prefix is **8 of 157 characters**. The full sentence appears in exactly two places in the repository, and both are the argmap nodes themselves (`lineage.yaml:1926`, `defeaters.yaml:1615`) — it has no independent record anywhere. What *is* recorded is a four-word fragment, in two non-corpus files and in one corpus file, always as the audit's own prose rather than as a filed quotation:

- `docs/research/claims/ROOT-h-hossjer-agrees-with-main-argument.md:45` — "Day's own response to Dembski's question (DE-01) says the scaling element 'doesn't apply at all' without equations"
- `docs/research/opponents/bill-dembski.md:19` — same fragment, straight apostrophe (so, again, not a curly-quote problem)
- `lineage.yaml:838` `fate_locator` and `:1920` `label` — the audit's own cross-references

Both of those use a **straight** apostrophe and lowercase `the`, which is the second reason the ticket's typography hypothesis does not hold: the mismatch is wording and capitalisation, not glyphs.

Decisively: `quotes-critics.md` files the Dembski interview as section **DEM-INT** and records **only Dembski's three questions, `DE-01`..`DE-03`** — there is no filed quote of *any* Day answer from that interview. `quotes-day.md`'s Dembski-venue entries (`Q82`, `Q83`, and the `Q`-entries around `:617`) all cite `comments.json` from the Substack **comment threads**, not the interview body. So Day's answer to DE-01 has never been filed under hard rule 2, in either quotes file.

Two readings remain open and the repo cannot separate them:
- **(b-paraphrase):** the sentence is the argmap author's compression of a longer answer, entered at build time as if it were a quotation. Then this is a fidelity breach on a `day`-side node, and `d129` (`undermining`, A5/P2, `audit_status: partly`) rests on words Day may not have used.
- **(b-unfiled-verbatim):** the sentence was copied verbatim from `sources/raw/refresh-2026-10-09/dembski-interview/` at build time and simply never filed in `quotes-*.md`. Then it is a filing gap, not a fidelity breach — but it is still a hard-rule-2 violation, because the locator points at a source with no committed quotation behind it.

The raw directory is gone, so this cannot be settled locally. Note that the node carries `inferred: true` with a `why` about Hössjer, so its *inferential* content is already flagged; what is not flagged is that its quoted content is unsupported.

**Proposed remedy (owner's call).** Sequenced, because the ruling depends on a fact we do not yet have:
1. **Re-fetch first.** Add `https://billdembski.substack.com/p/vox-day-interview-on-evolutionary` to the next source refresh (it is already a bib source; a read-only fetch under `HOWTO-refresh.md`, no new outward action). Extract Day's answer to DE-01 at para 65 ff.
2. **If the sentence is verbatim:** file it as a new `DE-`/`Q`-entry with paragraph locator and date, add `quote_source:` or let it resolve through the quotes file, and both ids go green with no verdict movement. This is a filing gap closed, and it should be logged as such in `ledgers/fidelity.md`.
3. **If it is a compression of a longer answer:** replace both `quote:` fields with the verbatim answer (or the longest verbatim span under the 30-word cap) and keep the compression in `note:`/`label:` where paraphrase is allowed. `d129`'s `note:` already carries the paraphrase ("Scaling is irrelevant because sexual reproductive capacity is the real limit"), so the `quote:` field is the only thing that needs to move.
4. **If Day said no such thing:** retract `d129` and mark the lineage node `retracted` with a `fate_locator` pointing at this note — and in that case the knock-on must be checked, because `ROOT-h-…:45` and `opponents/bill-dembski.md:19` both repeat the fragment, and `A5`/`A5g` would lose a Day-side defeater. **This is the only branch of the four findings that could move an argmap node's existence, and it is squarely the owner's call** — hence no edit here.

Until it is settled, the honest interim description of these two ids is "quoted sentence not attested in any committed source", which is what the lint is correctly saying.

---

## Summary table

| id | node | class | severity | proposed remedy | moves a verdict? |
|---|---|---|---|---|---|
| QM-01 | `d176` | (a) trailing period | low | drop the period; file as `BO-05` at next refresh | no |
| QM-02 | `L-adna-630-21-2026` | (b) two-sentence composite, reworded | medium (fidelity) | repoint at the filed §5.3 sentence; fix §9→§5.3 locator | no (node already dormant) |
| QM-03 | `L-dembski-scaling-reply-2026` | (b) unattested; verbatim-vs-paraphrase undecidable locally | medium–high (fidelity) | re-fetch the interview, then file / repoint / retract | possibly (retraction branch) |
| QM-04 | `d129` | same string as QM-03 | same | rule together with QM-03 | possibly (`A5`/P2 defeater) |

**None of these is caused by L2 (EVO-41)**, confirming the ticket: all three strings date to `9a2148b`.

**What the owner needs to rule on:** QM-01 can be applied as written at any time. QM-02 needs a choice among its three options. QM-03/QM-04 need the re-fetch authorised before any of their branches can be taken — and if the owner prefers, the EVO-6 batch close could proceed with QM-01 and QM-02 applied (2 errors, 0 warnings) and QM-03/QM-04 left red with this note as the standing explanation, rather than closing on a lint that was made green by a guess.

## Suggested lint hardening (not applied, offered for the same ruling)

Two of the four misses are a quotation whose *only* record is the argmap node asserting it. `argmap_check.py` would have caught both at build time if `find_quote()` reported *where* a quote resolved and the check warned when a `day`- or `critic`-side quote resolves only to `research/checks/results/*.md` (the audit's own prose) rather than to `quotes-*.md` or a claim file. That is a real change to the tool's contract and is listed here as a proposal only; it belongs in `METHOD-AUDIT-proposals.md` if the owner wants it.

---

## Resolution (2026-10-14, after the owner's ruling on EVO-78)

The owner ruled: **QM-01** apply the minimal fix; **QM-02** option 1 (repoint at the C6-filed §5.3 sentence); **QM-03/QM-04** authorise the read-only re-fetch. All three were carried out in this commit.

**QM-01 — applied.** Terminal period dropped from `d176`'s `quote:`. No other field touched; `audit_status: upheld` and `audit_basis` (R4 G1) unchanged. The secondary point stands as a to-do: the sentence is still unfiled in `quotes-critics.md` BOW, and should go in as `BO-05` at the next refresh so `d176` and `x:BO-paths` rest on a primary filing rather than on the audit's own write-up.

**QM-02 — applied (option 1).** `L-adna-630-21-2026`'s `quote:` is now the sentence exactly as `C6-molecular-clock-stopped.md:22` files it from §5.3, and `locator:` is corrected from "§9 (line 263 of text extraction)" to "§5.3". The "21 observed" half is no longer presented as quotation; it remains in `label:` ("clock predicts ~630, 21 observed") and in `fate_locator:` ("R4 C1b: 21 not reproducible from the stated procedure"), where prose is allowed. The node stays `fate: dormant` (2026-09-29); no claim verdict field moves. The §9/§5.3 discrepancy is resolved **in favour of §5.3**, on the C6 filing; `NOTES.md:331`'s ambiguity bullet should record that when the argmap notes are next touched. Option 2's stronger remedy — filing `"We observe 21."` as a Q-entry against a re-fetched Z18525185 — is not foreclosed and remains available at the next refresh.

**QM-03 / QM-04 — settled, branch 2 (verbatim; filing gap).** The interview was re-fetched read-only on 2026-10-14 under `HOWTO-refresh.md` (`sources/raw/qm03-dembski-2026-10-14/dembski-interview.html`, sha256 `d84dc78b…4c15a0`, 399,139 bytes; the API slug endpoint 302s to the page, so the page HTML was taken). `research/tools/qm03_locate.py` strips tags, NFKC-normalises and tests the argmap string as a substring:

- **verbatim: True.** The sentence appears exactly as both nodes have it.
- It is sentence 2 of a six-sentence answer at `<p>` index 58, immediately after the DE-01 question at `<p>` index 57. Under the para-65 convention `quotes-critics.md` uses for DE-01..DE-03, that makes the answer **para 66**. The answer opens "No, and that argument is flat-out wrong." and continues "Mutational fixation in humans and other vertebrates can never approach the speed of mutational fixation in bacteria. The defense is dead on arrival."

So the argmap text was correct all along and reading (b-paraphrase) is **ruled out**; the defect was reading (b-unfiled-verbatim), a hard-rule-2 filing gap — a locator with no committed quotation behind it. Closed by filing the sentence as **`Q296`** in `quotes-day.md` (with the local copy, hash, locator and RH tag), adding `DM-1b` to `bib-critics.md`, and refining both nodes' `locator:` to "answer to DE-01, para 66 sentence 2; filed as Q296". No `quote:` text changed on either node, no verdict moves, the `A5`/P2 Day-side defeater `d129` stands at `audit_status: partly`, and the retraction branch is **not** taken. `ROOT-h:45` and `opponents/bill-dembski.md:19` need no correction: their four-word fragment is now backed by Q296.

**A note in Day's favour, recorded with the same prominence as the errors.** Two of the four findings carried a live possibility that the audit had put words in Day's mouth. On the one that could have moved an argmap node's existence, the re-fetch vindicates Day's quoted sentence exactly: the audit's text was his. The remaining fidelity error of this set, QM-02, is also the audit's own and also against Day — a stitched two-sentence "quotation" attributed to his clock paper that he did not write in that form. Both corrections run the same way: against the audit, in Day's favour.

**Ledger.** The four are entered in `docs/research/ledgers/fidelity.md` under "Audit's own fidelity (2026-10-14)", scored with the same vocabulary used for both sides: QM-01 verified-accurate (spurious period), QM-02 **verified-misread**, QM-03/QM-04 verified-accurate (filing gap).

**Still open from this note (neither is a lint error):**
1. File the Bowers sentence as `BO-05` at the next refresh (QM-01's "better" remedy).
2. The lint-hardening proposal below is still a proposal: it was *not* applied. Note that QM-03/QM-04 are exactly the case it would have caught — a quotation whose only record was the node asserting it — and the re-fetch confirms the warning would have been a true positive about provenance even though the text was right. That strengthens the case for it as `METHOD-AUDIT-proposals.md` material.

**EVO-6 batch close.** The middle path described above is no longer needed: the lint is green on the merits, not by a guess, and the batch can close without a standing red.
