---
name: weekly-digest
description: Sunday routine (Operator). Refresh the watch list read-only, map every new argument into the math map, write the weekly digest (each person's new arguments, summary, math references, new/variant math), regenerate the person pages. Starts no work itself; new math becomes open objects the Lead schedules.
---
# Weekly argument digest (owner, 2026-11-01, D-39)

1. **Refresh** per `docs/research/sources/HOWTO-refresh.md` and the `source-refresh` skill: read-only, each fetch in its own new directory under `sources/raw/`, sha256 recorded, nothing executed, no contact, no posting, no Wayback, no paywall bypass. Write `docs/research/sources/refresh-YYYY-MM-DD.md` as usual.
2. **Map** each new item (post, paper, video window) with the `deref-source` skill: `docs/research/math/sources/<source-id>.md`, plus new or changed objects in `docs/research/math/objects.yaml`.
   - Reuse an existing object whenever the maths is the same. If only an input differs (a parameter value, an edition), add an object with `variant_of: M-NNN`.
   - New objects are `status: open`. Never resolve anything here.
   - **Link every object to the claims it bears on:** `used_by` lists the hierarchy node ids (grep `docs/research/claims/`). If no existing claim fits, leave `used_by: []` and add `new_claim: "<one-line proposed claim, speaker, side>"` so the Lead can decide. An object with neither is an error (first digest, 2026-11-01: all 19 objects were unlinked).
   - Locators are real: a line number, timestamp or paragraph, never `LNone`.
   - Speakers must resolve in `docs/research/math/people.yaml`. Add new people there (name, side, aliases).
3. **Pages:** `research/.venv/bin/python -I research/tools/people_pages.py`, then `research/tools/math_map.py --lint` (0 errors).
4. **Digest:** `docs/digest/YYYY-MM-DD.md` (the Sunday's date), at most 150 lines:
   ```
   # Week to YYYY-MM-DD
   One-paragraph summary: who said what new, which math it touches, what is new math.
   ## <Person> (<side>) — <source title, date>
   "<verbatim quote>" (<locator>)
     Summary: <one line, neutral>
     Math: M-NNN <short> (<status>) · NEW M-NNN … · VARIANT M-NNN of M-MMM (<what differs>)
     Arithmetic: <reproduces / does not, one line> (only if a number was stated)
   ## Nothing new from: <people on the watch list with no new item>
   ## New math this week
   | Object | Kind | Settle by | Rests under | Raised by |
   ```
   Both sides get the same treatment: same fields, same neutral wording. Rhetoric is listed with its RH tag, not argued.
5. **Commit** with explicit paths and `Gap: upkeep` (plus `Gap: X-MATHMAP` when objects were added). Post the digest's summary paragraph and its path as the routine issue's closing comment, then close the issue.

Do not: score verdicts, create Paperclip issues (the Lead schedules open objects in its loop), edit claim files, or run checks.
