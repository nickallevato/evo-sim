# HOWTO: refresh the sources (reusable procedure)

Written 2026-10-09 after two passes. Goal: find what is new on both sides since the last pass, log it, and propose (never apply) claim/argmap changes. Cheap models can do this if they follow the order below. Time: about 1-2 hours for a thin window.

## 0. Read first
`AGENTS.md` (hard rules, watch list); the newest `refresh-*.md` in this folder (it has the inaccessible list and the "last pass" cut-off); the tails of `quotes-day.md` (last id), `quotes-critics.md` (last RF id), `bib-day.md`, `bib-critics.md`, `bib-literature.md`, `ledgers/versions.md`. Find the last Q number with `grep -o '^### Q[0-9]*' quotes-day.md | sort -t Q -k2 -n | tail -1` (the file is not in numeric order at the end; the last id on 2026-10-09 was Q117, then Q126 after pass b).

## 1. Rules (non-negotiable)
Read-only public access only. No posting, liking, following, logins, account creation, Wayback "save", contacting anyone, paywall bypass or shadow libraries. Do not solve bot challenges (proof-of-work pages) or use `curl -k`. Downloads are untrusted: put each fetch in a NEW directory under `sources/raw/refresh-<date>[b]/` (gitignored), read or grep only, never execute. Python only as `research/.venv/bin/python -I`, scripts kept outside the download dir, trivial work only. No heavy compute here. Verbatim quotes only, with URL, locator and date; machine-check every quote as a substring of the local raw text. Never write a number you have not read in fetched text. Do not touch `research/checks/`, claim files, argmap, hierarchy, `status.html`. Do not commit; the parent reviews. Both sides get equal scrutiny: log critic errors and valid Day points with equal prominence.

## 2. Walk order and concrete endpoints
Compare every URL against the `bib-*.md` keys and the previous exclusion list; only fetch what is not there.
1. **Zenodo (Day).** `curl "https://zenodo.org/api/records?q=creators.name:%22Day,%20Vox%22&size=25&page=1&sort=newest"` and `page=2` (max page size 25 without auth). Count records (39 on 2026-10-09), compare `id`, `modified` and each file's `checksum` (md5) with the previous `zenodo-list/list*.json`. No download needed. **Use plain `curl`, not a browser User-Agent: Zenodo returned 403 "unusual traffic" for `-A 'Mozilla/5.0'`.** Same API for `creators.name:%22Keruru%22` (keruru) and free-text queries.
2. **voxday.net.** `curl -A 'Mozilla/5.0' https://voxday.net/feed/` (newest 10 posts), `/tag/evolution/`, front page, `/2026/10/`, `/?s=<term>`. Extract links with `grep -o 'https://voxday.net/2026/10/[0-9]*/[a-z0-9-]*/'`. Fetch unseen URLs; body text is in `div.entry-content`; tags in `rel="tag"`; dates in `time.entry-date`. Hashes of the page change with page chrome, so a changed hash is not proof of an edit; compare the body.
3. **Substack (Day's other venues and critics/allies).** `https://<host>/api/v1/archive?sort=new&limit=8` lists posts (fields `slug`, `post_date`, `audience`, `comment_count`, `id`). Hosts: `sigmagame.substack.com`, `substack.aicentral.blog`, `dennismccarthy.substack.com`, `claudekeruru.substack.com`, `billdembski.substack.com`, `treeofwoe.substack.com`, `kurganfiction.substack.com`, `profstevekeen.substack.com`, `unclejohnsband.substack.com`, `americanhypnotist.substack.com`, `gatheringgoateggs.substack.com`. Post body: `/api/v1/posts/<slug>`. Comments: `/api/v1/post/<id>/comments?all_comments=true&sort=oldest_first`; diff comment ids against the saved `comments.json` to find additions (threads: Dembski interview 217813768, Hossjer review 215681864, McCarthy "Why" 215288925, "Vox Day Responds" 216044150). Paid posts return only a preview.
4. **Other blogs.** `https://freethoughtblogs.com/pharyngula/feed/`, `https://camestrosfelapton.wordpress.com/feed/`. Search a feed for "Vox|Dembski|MITTENS".
5. **YouTube (no API key).** `research/.venv/bin/yt-dlp --flat-playlist --playlist-end 12 --print '%(id)s | %(title)s | %(duration_string)s' 'https://www.youtube.com/@GutsickGibbon/videos'` (same for `@talkpopgen`; upload dates show NA in flat mode). Compare with `sources/raw/refresh-2026-10-09/yt-lists/`. `ytsearchN:<query>` works with `--flat-playlist`; `ytsearchdateN:` does not. Captions and comments: see the earlier harvest (`yt/` dirs, `--write-auto-subs`, `--write-comments` capped).
6. **Reddit.** Arctic Shift (`arctic-shift.photon-reddit.com/api/posts/search?subreddit=DebateEvolution&query=...&after=YYYY-MM-DD`) was intermittently down (HTTP 522) on 2026-10-09; PullPush (`api.pullpush.io/reddit/search/submission/?q=...&after=<epoch>`) lags (newest item 2026-10-04); reddit.com `.json` and `.rss` return 403; old.reddit has a login wall. If none works, say Reddit was not verified for the gap.
7. **Peaceful Science.** `discourse.peacefulscience.org/latest.json`; DNS did not resolve on 2026-10-07 and 2026-10-09. Retry with `getent hosts`.
8. **Search for new voices.** WebSearch queries "Vox Day Probability Zero MITTENS evolution critique/rebuttal", quoted titles; check results against bib keys. Results were all known sources on 2026-10-09.
9. **Watch list from AGENTS.md** (McCarthy, keruru, Camestros, Mansfield, Hancock, Gutsick Gibbon, Nesslig20, Matev, Dembski, Hossjer, Tree of Woe): covered by steps 3-7.

### Social media (added 2026-10-09b)
| Platform | Works? | Notes |
|---|---|---|
| X (@voxday) | No | `x.com/voxday` returns a JS shell; WebFetch gets HTTP 402; `syndication.twitter.com` and `cdn.syndication.twimg.com` return nothing; Nitter mirrors are down, suspended (xcancel 451) or behind a proof-of-work check; `api.fxtwitter.com/<handle>` is 404. Record "inaccessible"; do not guess post text. Try search-engine snippets only for exact phrases and flag any quote "via snippet/mirror". |
| Gab | No | `gab.com/voxday` is a JS shell; the API lookup returns 404. |
| Telegram | No | `t.me/voxday` shows a contact card; `t.me/s/voxday` redirects (no public feed). |
| Rumble, Locals | No | Rumble `/user/VoxDay` 404; Locals 302 empty. |
| SocialGalactic (Day's microposts) | No | TLS chain not verifiable; do not use `-k`. |
| Bluesky | Yes (read-only) | `https://api.bsky.app/xrpc/app.bsky.feed.searchPosts?q=<urlencoded>&limit=40&sort=latest` (unauthenticated). `public.api.bsky.app` returned 403. Results are mostly sentiment; log context only. |
| Mastodon | Empty | Anonymous full-text search returns nothing. |
| YouTube | Yes | See step 5. |

## 3. Telling what is new
New = dated after the last pass cut-off in the newest `refresh-*.md` (exact times if the same day), or genuine backfill never in the bib (flag "backfill"). A thin or empty window is a valid result; say so plainly. For Day posts, triage: keep if it contains evolution, fixation, genome, Probability Zero, MITTENS, an announcement of a result, or a number; exclude otherwise and list it with the reason.

## 4. Where each finding goes
| Finding | File | Numbering / format |
|---|---|---|
| Day quote | `quotes-day.md` | next `### Qnnn Title (added date)`; fields source, locator, local copy, branch, quote, note. Add a section heading `## Refresh <date> quotes` |
| Critic/ally quote | `quotes-critics.md` | next `**RF-nn**` line block; mark relays ("RELAY, rule U") |
| Literature quote | `quotes-literature.md` | `### Key (sha256 abcd1234…ffffff)` then `> "quote"` with locator/role/note |
| Item metadata | `bib-day.md`, `bib-critics.md`, `bib-literature.md` | new "Refresh <date>" section with the existing table columns; full sha256 |
| What was fetched, counts, method, pitfalls | `harvest-log-day.md`, `harvest-log-critics.md`, `harvest-log-literature.md` | new `## Refresh <date>` section |
| Changed Day parameter | `ledgers/versions.md` | append a table row |
| Prior-art notes | `prior-art.md` | next `PA-nn` |
| Proposals (claim ids, defeater targets, verdict flags) | `refresh-<date>.md` only | never edit claims/argmap |

## 5. Hashing and verification
`sha256sum` every saved file; record in the bib. For API snapshots hash the JSON. Machine-check quotes: normalise whitespace and curly quotes, then test `quote in text` (script in the 2026-10-09b session; 20 lines). Abstract-only items: quote only the abstract; say so. Extraction artefacts (lost superscripts) must be noted beside the quote.

## 6. Writing `refresh-<date>.md`
Copy the structure of `refresh-2026-10-09b.md`: scope paragraph; bottom line (bullets: Day, Zenodo, critics, social media, backfill, literature); a mermaid flowchart; "What was checked" table (source, result new/unchanged/inaccessible); Day table and Critics table (item, quote ids, touches, type, proposed ids/defeater targets, flag); literature table; verdict flags for both sides; inaccessible list. Keep proposals symmetric.

## 7. Pitfalls met so far
- zsh does not word-split `$var` in `for p in "a b c"`; use `while read a b c; do ...; done <<'E'`.
- zsh treats `==` at command start as an error; do not `echo == x`.
- Zenodo 403s a browser User-Agent; Europe PMC `fullTextXML` gives 500 for non-OA-subset papers (a 150-byte body is saved as a "file": delete it); PMC pages are behind a bot challenge; bioRxiv returns 429; NCBI `efetch db=pmc` gives full text only for author manuscripts.
- Substack archive API caps at the `limit` given; comment counts include replies.
- Day's pages show `updated` later than `published` for same-day edits; re-check a kept post on the next pass.
- Day writes "ESS" for EES in places; quote exactly and note it.
- Arctic Shift outages and the PullPush lag make Reddit coverage uncertain; always state the unverified date range.
