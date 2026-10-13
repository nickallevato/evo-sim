# Brief VID-01 (operator): harvest the 2026-10-13 critic video, once captions exist

Lead: Big Sim. Written 2026-10-13, before the task was created (MA-21).
Skill to load: `.claude/skills/source-refresh/SKILL.md`, following
`docs/research/sources/HOWTO-refresh.md`.

## Goal

Bring the first critic reply that exists since the audit began into the sources of record,
verbatim and dated, so that the next milestone post can state what it says.

**Target.** Gutsick Gibbon, "Six Scientists Roast One Racist Loser", YouTube id
`AqC1ZM4icms`, 4:14:03, posted 2026-10-13 about 18:00 UTC (`QUEUE.md`, "unreviewed critic
reply" entry).

## Gate: captions

At the 2026-10-13 fetch the video had **no captions**. This task starts with one read-only
check for captions. **If there are still none, stop**: write the dated negative result into
the refresh file, report it, and do not transcribe the audio yourself (a 4-hour
machine transcript is neither verbatim nor cheap, and nothing in the audit may rest on it).
Re-check is a later task, not a poll.

## What the lead has already seen

- The entry in `QUEUE.md` and the standing constraint that **no milestone post may say
  "no critic reply"** while this is unharvested. That constraint holds whether or not
  captions appear.
- Four hours of video is far more than the audit needs. Harvest **only** passages that
  bear on a claim in `docs/research/claims/` — the mathematics, the counts, the aDNA panel,
  dN/dS, the Fourth Mechanism — with a timestamp locator for each.
- Rule RH applies to the critic side exactly as to Day: tag each quoted statement
  `dialectic` or `rhetoric` before scoring. The title is rhetoric; that changes no verdict
  and is recorded in `ledgers/slips.md` with its device, audience and dialectical core.

## Files you may write

- `docs/research/sources/refresh-2026-10-<dd>-video.md` (new file, dated the day you run it)
- `docs/research/sources/bib-critics.md` (one row: id, url, title, date, duration, sha256
  of the caption file, access date)
- `docs/research/sources/quotes-critics.md` (new Q ids, appended, never renumbered)
- `docs/research/ledgers/slips.md` (RH rows only)
- `docs/research/sources/harvest-log-*.md` for the run log

Nothing else. No claim file, no verdict, no `QUEUE.md` edit — scoring the quotes against
claims is a separate analyst task that this one unblocks.

## Review tier

**Low-stakes: one combined review**, `REVIEW-R4-VID-01-combined.md` (correctness plus both
steelman sections). This is a harvest, not a check; no verdict can move in it. If a quote
you harvest plainly contradicts an existing audit verdict, record it and say so in the
report — do not apply it.

## Constraints

- `AGENTS.md` hard rules. **Rule 4**: the download is untrusted data, fetched into its own
  new directory under the gitignored `sources/raw/`, read or grepped, never executed.
  **Rule 3**: no full text or caption file in git — link, short quotes and sha256 only.
  **Rule 6**: read-only fetches; no comment, no contact with the author, no Wayback
  snapshot.
- **Rule 8**: this video postdates the model cutoff. Every word about it must come from the
  fetched text. Nothing from memory, nothing from a summarizer, nothing from a third-party
  recap of the video.
- Verbatim quotes only, each with a timestamp and the access date (rule 2).
- No computation on this workstation beyond the fetch and grep. `na-workhorse` is busy with
  `ph2` until 2026-10-16: launch nothing there.
- Commit with explicit paths, never `git add -A`. End each commit message with exactly:
  `Co-Authored-By: Paperclip <noreply@paperclip.ing>`
- `git pull --rebase origin research` before each push; push `origin research` only.
- You are the only agent touching `quotes-critics.md` and `slips.md` while this runs.

## Report format (at most 300 words)

Commits; whether captions existed; a table of Q ids harvested with timestamp, the claim
each bears on and its RH tag; anything that looks like it contradicts an audit verdict;
failures; next step.

---

# Addendum: lead rulings before the fix pass (Big Sim, 2026-10-13)

The harvest ran and was committed (`6d090de`). The combined review is
`research/checks/results/REVIEW-R4-VID-01-combined.md` (commit `38a1950`): 0 BLOCKER,
1 MAJOR, 10 MINOR, 7 NOTE. Its integrity findings are accepted in full — all four hashes
match, the transcript re-derives from the hashed captions, 42/42 quotes are exact
substrings, the gate and the negative scan hold.

These rulings are written before the fix pass, per step 4 of the lifecycle (D-24). They
bind the fix pass; the fix pass answers **every MAJOR and MINOR by id** in a "Review
resolution" section appended to `docs/research/sources/refresh-2026-10-13-video.md`.

**R-1 (MAJOR-1, controlling).** The mischaracterisation is conceded. The panel's reply to
the Bernoulli barrier is to be harvested on its substance (the recombination and
infinitesimal-model material the review names), as new appended GGR ids, and the
"without a derivation" wording struck from refresh item 4 and from the GGR-19 note.
A harvest that records one side's dismissal and omits the other side's argument fails
hard rule 1 whichever side it favours. This is the one finding that must be fully closed
before any analyst scores from this record.

**R-2 (MINOR-5 vs NOTE-3: the A5h modelling objection).** The Day-side and critic-side
sections conflict only in emphasis, not in fact; both halves are correct and both are
recorded. The ruling: the critics' point (equilibrium load does not depend on *s*;
Haldane 1937, Muller 1950) and its cost to them (on their own e^-U the "functionally dead"
direction strengthens, and the s = 0.001 escape A5h records disappears) go into the same
note, in that order, neither applied. **No verdict moves in this task.** A5h's fields are
not touched; the analyst scoring task decides.

**R-3 (MINOR-4: the GGR-13/14 *d*-coefficient "conflict").** Record all three readings
under rule RD with their sources (`A-mittens-formula.md` TW-01; A4 `derived:`; A4d and its
Weaknesses line on Appendix D) and the host's own 01:49:52 narration. Do **not** declare a
winner and do not touch A4d. The framing "as likely a critic-side error as a Day-side one"
is withdrawn as unsupported by our own files; the readings replace it.

**R-4 (MINOR-8: GGR-04's RH tag).** Governing reading is the literal concession, so the
credit to Day stands; the ironic reading is recorded beside it. This follows rule RD as
written (the most defensible reading of the quoted statement), not a preference for the
reading that favours either side.

**R-5 (MINOR-10: scope of `research/tools/harvest/verify_vid01.py`).** The file is
**ratified** as in-scope: it is correct practice under hard rule 4 (script outside the
fetch directory) and the brief's file list did not anticipate it. The reproducibility half
of the finding stands and must be fixed: make the verifier read its quote list from the
`YT-AqC1ZM4icms` section of `quotes-critics.md`, so that the pass count is reproducible
from the repository alone without the gitignored fetch directory. Re-run it and record the
new count (42 plus whatever MINOR-7 and R-1 add).

**R-6 (MINOR-9: "credentialed").** Accepted as written. This finding costs the critics and
is applied for the same reason the Day-side findings are: hard rule 1 cuts both ways.

**R-7 (NOTE-4, NOTE-6: out of scope here).** The body's ad hominem lines may be noted in
RH-31's dialectical-core column, nothing more; a wider rhetoric harvest is a separate task.
The unpinned `yt-dlp` is a `requirements.txt` / `HOWTO-refresh.md` matter for the
bookkeeping task, not for this fix pass.

## Files the fix pass may write

The five harvest files, plus `research/tools/harvest/verify_vid01.py` (R-5) and the raw
output of its re-run. Still **no claim file, no verdict field, no `QUEUE.md` edit.**
New quotes are appended with fresh ids; nothing is renumbered.
