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
