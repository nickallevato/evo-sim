# Harvest log: critics / allies slice (R1 pass 2)

Run date: 2026-10-07. All fetches were read-only GETs (curl with a generic UA, yt-dlp, WebSearch, WebFetch). 1 s sleep between requests to the same host (comment pulls by yt-dlp ran at its own pace, 2 s between videos). Nothing was posted, commented, archived on Wayback, or sent to anyone. Raw copies live in `sources/raw/critics/` (gitignored, treated as untrusted data, parsed only with `python3 -I`). yt-dlp 2026.08.19 was installed into `research/.venv`.

## Enumeration results
| Target | Result |
|---|---|
| McCarthy Substack | Archive API (2 pages, 73 posts) + RSS enumerated. Posts touching Day/PZ: 2026-01-07 (free), 2026-01-12 (paid, preview), 2026-01-26 (paid, preview; free full repost 2026-09-11), 2026-02-03 (paid, preview; free update 2026-09-17 "Vox Day Responds"), 2026-02-13 (paid, preview), 2026-02-15 (paid, listing only). The 2026-07-24 post is Shakespeare/North, not Day. Day's 2025-08-04 "Mr. McCarthy Responds" is on Day's blog (other agent). |
| Keruru | Domain found via Day's blog post 2026-08-26 ("The Irrelevance of k = mu"): **claudekeruru.substack.com**. `keruru.substack.com` is a different, unrelated newsletter (excluded). 29 posts enumerated; 8 touch evolution/math. keruru is an ally-turned-self-corrector (retracted two claims on 2026-08-26), so classified `adjacent`. |
| Camestros Felapton | Series is 6 parts (2026-01-23 to 01-30); the category feed and a site search show no part 7. Reviews the first-edition text only. |
| PZ Myers | Site search RSS for "Vox Day", "MITTENS", "Probability Zero", "Dembski Vox": exactly the three 2026-10-02/03/04 posts. Comment threads not harvested. |
| Gutsick Gibbon / Hancock | Video found by listing the channel: `_Vu0ZVVjwHc` (2026-10-03, 3:30:28). Not found via yt-dlp `ytsearch` (returned unrelated results). Auto-captions and 2,000 comments captured (cap; YouTube reports ~3,157 comments at the time of the pull). A promised follow-up "roundtable" with credentialed reviewers had not been published as of the pull (per Day-side and GG statements). |
| Will Duffy stream | `6jXiwrcC5PQ` (2026-09-22, 4:57:53): captions + 2,000 comments. Duffy presentation t=00:19:12-00:43:30. |
| Math-teacher video | `nTVRiEcswI8` (2026-09-28): captions + all 115 comments. |
| Davis / Examining Origins | The ID in the task text was truncated (11-char ID required); resolved by listing the channel: `jDxFtCOGZ3A` "Can Evolutionists Finally Face the Math? Challenge Issued!" (2026-09-23). Captions + all 819 comments. Mansfield thread present. |
| Bowers original | NOT FOUND. Only Day's repost (2026-03-04) retrieved. Two web searches (title phrase "Ignorant and Unscientific Drivel", "Joe Bowers Critical Review") returned nothing. |
| Reddit | reddit.com/search.json -> HTTP 403; old.reddit.com search.json/rss -> HTML "Welcome to Reddit" wall (not data, deleted). Workaround: Arctic Shift API (third-party archive) title search for "Vox Day", "MITTENS", "Day's" in r/DebateEvolution after 2025-06-01: 6 threads (1wrw50e, 1wss2wj, 1wv4zeg, 1wvzng3, 1wxgamf, 1wxgsjm). **Limits:** title search only (a body-text search was rate-limited / unsupported), so threads whose titles omit those words are missed. "Probability Zero" title search returned nothing. 1wxgamf (duplicate of 1wxgsjm) not downloaded. |
| Rosenhouse | Chapter scope taken from Felsenstein's annotated TOC (ch.4 Wistar; ch.6 Information & Combinatorial Search). Cambridge TOC PDF and Cambridge Core page failed (curl timeout / HTTP 500; WebFetch error). No Rosenhouse reply to Day found: Panda's Thumb search page returned no "Vox" hit, **but that page may ignore the query, so this is inconclusive**. Rosenhouse Substack feed -> 404. Dembski's "Jason Rosenhouse's Whoppers" is a 2022 post (not on his Substack; Goodreads mirror stub unusable); skipped, pre-dates Day. |
| Moran / Sandwalk | Blogger feed `?q=` ignored the query (identical latest-10 results; 0 mentions of "Vox"). Inconclusive; no Moran post on Day found. File deleted (non-informative). |
| Felsenstein | Only the 2022 Rosenhouse TOC post. No Felsenstein post on Day found (Panda's Thumb search inconclusive, see above). |
| Peaceful Science | Discourse search API: one thread family (Nesslig20 "Response to Will Duffy" Parts I/II, 2026-10-05). Posts from 2019 and 2021 mention Day only incidentally. |
| Zach Hancock | `@talkpopgen` channel listing: no Day-specific video other than the guest spot on Gutsick Gibbon. `zachhancock.substack.com` = "American Nature" newsletter, apparently a different person (no evolution posts since 2025); excluded. Pre-existing 2024 video "Waiting-time? No Problem." downloaded for context only. |
| Gariepy | No independent copy of the 2019/2021 debate or his own write-up found (web search: nothing). Only Day's 2019-02-11 post quoting a Gariepy transcript (secondhand). Gariepy's own channel not fetched. |
| Hossjer | Post EXISTS (https://billdembski.substack.com/p/a-review-of-vox-days-main-argument, 2026-09-14); the PDF with full equations was downloaded. Pass-1 disagreement resolved. |
| Dembski | Interview post found (2026-09-28). Its attached "Mittens 3" PDF (112 KB) was not downloaded. |
| Tipler | No primary Tipler text found; only secondhand (Tree of Woe, Dembski, Myers quoting Day). The foreword/appendix are inside the paid book. |
| Keen | Preface retrieved in full (no equations). |
| Tree of Woe, Fandom Pulse, Uncle John's Band, American Hypnotist | Retrieved in full. Freeze Frame (UJB 2026-02-11) downloaded, not read. |

## Failures and exclusions
- Paywalled McCarthy posts: previews only (listed in bib).
- Reddit direct access blocked; Arctic Shift used instead.
- `ytsearch:` queries returned irrelevant results; channel listings used instead.
- YouTube comment pulls capped at 2,000 for the two large videos; comment order is YouTube's default (top), not exhaustive.
- Auto-captions: speaker labels absent; whiteboard derivations not captured; recognition errors preserved in quotes.
- Day-aligned sites seen in search results but not harvested here (belongs to the Day-corpus agent or low value): sigmagame.substack.com ("The Mathematics of Evolution", "Gamma Doubts"), wholereason.com, kurganfiction.substack.com, audaxconsilium.substack.com ("Scorched & Salted"), Day's "The Best They've Got" (review of Rosenhouse), Day's "Do Try to Keep Up, Dennis".
- Excluded as off-topic/ad hominem only: r/DebateEvolution 1wrw50e (white-supremacy thread) and 1wvzng3 (AI author thread) are downloaded but not mined; most of the GG video t=02:15-03:30 (biography/politics of Day) and Gibbon's Reddit comment replies are not math.
- Not contacted: no one was emailed, commented to, or followed.

## Version note (for the versions ledger)
- Duffy's 2026-09-22 presentation uses 6.3 My, 25 y/gen, 1,400 gens/fixation, d dropped to 1, 252,000 gens, 205M required => 180 fixations. The 2026-10-03 GG video answers that version.
- MITTENS 3.0 (Zenodo 23003785) is dated 2026-09-28 by the Reddit OP (and "now gone" per one comment: unverified). It uses 1,322 gens/fix; 191 achievable vs 205M required; 1,075,000-fold shortfall. Reddit and KITTENS critiques target 3.0 directly; Hancock's video does not (he notes 3.0 is a different argument per KITTENS sec.1, via the KITTENS author's account, secondhand).
- Camestros (2026-01) reads the first edition: 9 My, 20 y, 450,000 gens, 1,600, d=1, 281 fixations.
- Hossjer reads the first edition with d=0.45: 127 fixations.
- Tree of Woe interview (2026-01-08): Day gives 202,500 gens.

## Open items for pass 3 / R2
1. Find Bowers' original review (try Medium, Reddit r/DebateEvolution, X, Quora).
2. Pull the Zenodo MITTENS 3.0 record to confirm Reddit critics' section numbers (4.3, 6.3-6.4, 7.x, 8.2, 8.6).
3. Re-run Arctic Shift body-text search once rate limit clears; harvest 1wxgamf.
4. Download Dembski's attached "Mittens 3" PDF.
5. Capture the Gutsick Gibbon "credentialed roundtable" video when published.
6. Obtain Cambridge TOC PDF for Rosenhouse's remaining chapters (7 Thermodynamics, 8 Epilogue already known from Felsenstein).
7. Read keruru Zenodo deposits (22969407 and 21866797 are other topics; the k=mu simulation deposit is not identified) to check the exact-Markov-chain claim.


## Refresh 2026-10-09 (corpus refresh, critics/allies slice)
Run date 2026-10-09. Last prior harvest 2026-10-07. All fetches were read-only GETs (curl with a generic UA, Substack public API, Zenodo API, yt-dlp flat listings, WebSearch). Nothing was posted, commented, archived on Wayback, or sent to anyone. Raw copies: `sources/raw/refresh-2026-10-09/`.

### Counts
| item | count |
|---|---|
| New critic/ally items with relevant content | 3 sources: Matev comments (new critic), keruru Zenodo 22184713 (new to corpus), EES commenter "Hilbert" in the Dembski thread (new voice) |
| Other new comment threads harvested (backfill) | McCarthy x2 (37 and 75 comments), Dembski interview (74), Hossjer review (18), Reddit 1wws70t (101), 1wxgamf (4) |
| New critic-side posts since 2026-10-07 | 0 (no new post by McCarthy, keruru, Camestros, Pharyngula, Hancock, Gutsick Gibbon, Mansfield, Nesslig20 on this topic found) |
| New quotes | 17 (RF-1 to RF-17) |

### Per-target results
| Target | Result |
|---|---|
| McCarthy Substack | Archive through 2026-10-08: no new evolution post (latest posts: Shakespeare authorship, AI doom, Pinker/Alexander). Comment threads under "Why Probability Zero is Wrong" (37) and "Vox Day Responds" (75) captured for the first time. Both contain extended Day, McCarthy and Matev exchanges. |
| keruru (claudekeruru.substack.com) | Archive through 2026-09-27: no post after "Nobody in the Room". Five previously unlisted posts (07-16 to 08-27) fetched: none touch fixation or Day (AI-authorship essay "Not Fishing, Maxxing" mentions Day's Byron AI posts only). Zenodo deposits found via API: 22184713 (aDNA temporal Ne; directly relevant) and 22121270 (demography; irrelevant). Open item 7 of 2026-10-07: the exact-Markov-chain k = mu simulation deposit is still not identified; 22184713 is the aDNA/Ne deposit. |
| Camestros Felapton | Feed through 2026-10-06; site search for "Vox Day" lists 2026-10-06 "Speaking of failed encyclopedias..." and 2026-08-29 "Milo and the Puppies" among its newest hits (titles only; not read; not about the fixation math by title). Series still 6 parts; MITTENS and "Probability Zero" searches return only parts 1-6. |
| PZ Myers (Pharyngula) | Search feeds for "Vox Day", MITTENS, "Probability Zero", Dembski: only the three known posts (2026-10-02, 10-03, 10-04). |
| Zach Hancock / Gutsick Gibbon | Channel listings (flat): no Day-related video after `_Vu0ZVVjwHc` (2026-10-03). Hancock's newest (2026-10-04) is a course announcement. The promised "credentialed roundtable" is not published. |
| Reddit | `old.reddit.com` search returns 302 to a login wall (not bypassed). Arctic Shift (intermittent timeouts) and PullPush used instead. r/DebateEvolution: new thread 1wws70t (GG video announcement), 1wxgamf harvested; 1wwqzu3, 1wtlmz4, 1wncr1b relate to Duffy/Gould letter, not math (not mined). No new math threads. |
| Peaceful Science (Nesslig20) | **Inaccessible this run:** `discourse.peacefulscience.org` and `peacefulscience.org` do not resolve (DNS ENOTFOUND from both curl and WebFetch). Nesslig20 Part III, if any, not checked. |
| Dembski Substack | Archive: two new posts (2026-10-05 "Darwinism: Scientific Inference or Philosophical Preference?", 10-07 "The Art of Academic Disinvitation") do not mention Day. Comment threads captured. No Hossjer update found. |
| Mansfield | No independent publication found (web search); his statements remain in the YouTube comments and Day's quotations. |
| Tree of Woe, Uncle John's Band, American Hypnotist, Fandom Pulse, Keen | Archives checked through 2026-10-08: no new post on the topic. |
| New critics (searches) | Matev (Substack @ns670106), found via McCarthy's comment threads. Web searches for Moran/Sandwalk, Felsenstein/Panda's Thumb, ReMine/Truman, Bowers, Graur found nothing new. Bowers' original review is still not found (item 1 of 2026-10-07). |
| Zenodo | Search for KITTENS/Day-critique deposits: none. keruru deposits as above. |

### Excluded (with reasons)
| Item | Reason |
|---|---|
| Kurgan Fiction posts 2026-10-01 to 10-06 (5 hashed) | Supporter essays/debate about the Socio-Sexual Hierarchy; no fixation math |
| Rhino UP review 2026-01-09 | Praise review; no numbers |
| gatheringgoateggs "Contra Vox Day" (2024-08-20) | Pre-dates the corpus topic (2024) and is not about evolution math (title match only); not fetched |
| keruru "The Long Generation" (Zenodo 22121270) | Demography/religion methods paper; hashed, not quoted |
| keruru Substack posts 07-16..08-27 (5) | Not about Day's math (see above) |
| Reddit 1wwqzu3, 1wtlmz4, 1wncr1b, 1wvtoiz | Duffy/Gutsick Gibbon personal dispute and Gould-Dawkins letter; ad hominem and biography, no math |
| McCarthy comments by Bryan Wildenthal, Mike, Nathan etc. | Common-descent evidence arguments and religion; off the fixation math |
| ns670106.substack.com | Empty archive (no posts) |

### Inaccessible
- discourse.peacefulscience.org (DNS).
- old.reddit.com search (login wall; not bypassed).
- socialgalactic.com microposts linked from Day's blog (TLS chain not verifiable; not bypassed).
- McCarthy paid posts (unchanged from 2026-10-07; e.g. 2026-10-08 "Exclusive: ... Swordfish" is unrelated).

### Open items carried forward
1. Bowers' original review: still not found.
2. Dembski's attached "Mittens 3" PDF: still not downloaded (the 2026-09-28 interview post JSON is in `sources/raw/critics/`).
3. GG "credentialed roundtable": not published as of 2026-10-09.
4. Cambridge TOC for Rosenhouse chapters 7-8: not retried.
5. Peaceful Science: retry when DNS resolves (Nesslig20 Part III).
6. keruru's k = mu exact-Markov-chain deposit: not identified.
