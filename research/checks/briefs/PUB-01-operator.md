# PUB-01 — board patch `upd23` and first publication of the static page

**Role:** operator. **Written by:** lead, 2026-10-13. **Authority:** D-26 (owner, 2026-10-13 22:33 UTC, "Publish a static page"), D-27 (cap of one agent). **Cap:** you are the only agent running; do not spawn work for anyone else.

## Why this exists

The owner was asked how to publish the status board now that no agent in this runtime can write to the claude.ai Artifact. He answered: publish a static page. GitHub Pages is already enabled on `nickallevato/evo-sim` — legacy build, source `master` `/docs`, HTTPS enforced — so the board's public address is already live:

> https://nickallevato.github.io/evo-sim/research/status.html (returns 200 as of 2026-10-13 22:40 UTC)

What is served there is `master`'s copy of `docs/research/status.html`, which is upd21-era. The current board on `research` is `4df7485` (upd22). **It must not be published as it stands:** upd22 was written before the O-5 revert (`2740ded`), so it still shows B internal as `non-sequitur` and A2e external as `contradicted`. Both are now `pending`. Publishing it would put two superseded verdicts on a public page.

## What to do

1. **Read the files of record first**, not the board: the claim front matter for B and A2e, `research/tools/argmap_check.py` output, `research/tools/lint_research.py` output, and the roadmap statuses. Every number you put on the page must come from one of those, as upd22 did.
2. **Write `research/tools/board/upd23.py`** in the same shape as `upd22.py`. It must, at minimum:
   - set B internal and A2e external to `pending` on the page, with the same superseded-value presentation the claim files use;
   - regenerate the verdict tallies, the reading-dependent count, the objections and versions counts and the roadmap statuses from the files of record;
   - keep `ph2` shown as running (due 2026-10-16 02:00–08:00 −06:00);
   - note the four known `argmap_check.py` quote-not-found errors (`L-adna-630-21-2026`, `L-dembski-scaling-reply-2026`, `d129`, `d176`) wherever the page reports the audit's own errors. Do not fix them in this task.
3. **Run it, commit the patch script and the patched page together** on `research`, push to both remotes.
4. **Publish.** Bring `docs/research/status.html` to `master` so Pages rebuilds. Publish **the board file only** — do not merge the rest of `research` into `master` in this task; batch 15 is not closed and the write-ups behind it have not finished their reviews. A single-file cherry-pick or a `master` commit that takes `research`'s copy of that one path is what is wanted. Push `master` to both remotes.
5. **Verify, do not assume.** After the Pages build settles, fetch the public URL and confirm (a) HTTP 200, (b) the page shows B internal and A2e external as `pending`, (c) the upd23 label is present. Record the HTTP code, the build conclusion from `gh api repos/nickallevato/evo-sim/pages/builds/latest`, and the three checks in your report.

## Constraints

- You are the only writer on `docs/research/status.html` and on `master` for the duration of this task.
- No computation on this workstation; this is a bookkeeping and publication task, nothing runs on a host.
- **No verdict value may move in this task.** You are copying the files of record onto the page, not deciding anything. If a figure on the page and a file of record disagree and you cannot tell which is right, leave the page as the file of record says and write the disagreement in your report for the lead.
- Hard rule 6 still stands: publishing this page is authorised by D-26 and is the only outward action in scope. Do not announce it anywhere, do not post it, do not contact anyone.
- If `master` turns out to be protected or the push is refused, stop and report; do not force anything.

## Report (300 words, to the task)

What moved on the page and the file of record behind each change; the two reverted fields confirmed as `pending`; the commit on `research` and the commit on `master`; the public URL with its HTTP code and the Pages build conclusion; anything you found that the lead should rule on. No verdict value in your report is a decision — the rulings on B internal, A2e external and L5 are the lead's and are not yet made.
