# Harvest log: Vox Day corpus (R1 pass 2)

Run date 2026-10-07. Agent slice: Day's blog + Zenodo. All requests to voxday.net were serial with >=1 s spacing (User-Agent `Mozilla/5.0`); Zenodo API with default curl UA (the `Mozilla/5.0` UA was blocked there with HTTP 403 "unusual traffic" on first try, then default UA worked; no rate-limit abuse, ~45 requests). No Wayback saves, no posting, no contact. Amazon returned a bot-check page (not bypassed).

## Counts
| item | count |
|---|---|
| Zenodo records by "Day, Vox" (API total) | 39 |
| Zenodo records downloaded | 28 (+2 earlier versions found via `/versions`: 18202768, 18517618) |
| Zenodo files downloaded | 32 (30 files of the 28 records incl. 2 second files [addendum, xlsx], plus 2 files of prior versions); by type: 10 pdf + 1 xlsx + 18 docx + 3 odt |
| Zenodo records listed but not downloaded (philosophy/theology) | 11 |
| Blog posts on `/tag/evolution/` dated >= 2019-01-01 (pages 1-18, 172 posts) | 172 |
| Blog posts on `/tag/evolution/` dated < 2019-01-01 (pages 18-25, not fetched) | 72 |
| Additional untagged candidates found by search/tag/archive (not in evolution tag, >= 2019) | 81 fetched |
| Total blog posts fetched and triaged | 253 |
| Kept (relevant; HTML+txt in `sources/raw/day/`) | 154 |
| Excluded (fetched, triaged out; reasons below) | 99 |

Relevance rule used: kept if the post contains math/claims/numbers on evolution, fixation, Kimura, Haldane, LTEE, MITTENS, Probability Zero, Bernoulli, Hard Limits, aDNA, d coefficient, Wistar, sequence space, or is a direct response to a critic or a debate record. Triage was by keyword counts (see kw lists in method) plus manual reading of the first ~300 characters of low-scoring posts. Excluded = news link-posts, politics, fiction, bare quotations, personal gossip, promo, praise.

## Method
1. `/tag/evolution/page/N/` N=1..26 (26 is 404; pages 18-25 are pre-2019 and only listed). Page 17 ends 2019-01-30, page 18 begins 2018-09-25 ... so the 2019-01-01 boundary lies inside page 17/18.
2. `/tag/science/page/1..24/` (24 pages, reaching 2023-12-19; 240 posts scanned for keyword hits): no additional relevant post. `/tag/mittens/page/1..3/`: nothing new. `/tag/probability-zero/` is 404.
3. Site search (`/?s=` and `/page/N/?s=`): MITTENS (7 pages), Kimura (6), fixation (8), Probability Zero (10), Haldane (3), Bernoulli (3), LTEE (3), Lenski (3), Wistar (2), ancient DNA (4), effective population (3), molecular clock (3), Frozen Gene (4), Darwin (6), HARDCODED, Irrelevance of Acclaim, Historic Rigor, PZ Print Editions, Rejection. Candidate URLs not already in the evolution tag were fetched (79 + 2 added by hand: 2026-05-18 gatekeepers-confession, 2026-05-02 decay-function).
4. Gap windows via month archives (`/2026/06/`, `/07/`, `/08/`, `/09/` all pages): see below.
5. Posts fetched with `curl -sL -A 'Mozilla/5.0'`; text extracted by a script kept outside `sources/raw/` and run with `python3 -I`.
6. Raw index pages (tag/search/archive HTML) are kept in `sources/raw/day/tags/` for audit.

## Named items requested
| item | result |
|---|---|
| Q&A https://voxday.net/2026/01/19/probability-zero-qa/ | fetched, kept (B2026-01-19-probability-zero-qa) |
| "HARDCODED" 2026-05-01 | https://voxday.net/2026/05/01/hardcoded-2/ kept; also an earlier "HARDCODED" post 2025-12-27 kept |
| "The Irrelevance of Acclaim" 2026-05-14 | https://voxday.net/2026/05/14/the-irrelevance-of-acclaim/ kept (mentions Kimura/Haldane once each; award discussion) |
| "Rejection" 2026-01-12 | https://voxday.net/2026/01/12/rejection/ kept (journal rejection of main MITTENS paper, per post) |
| "Historic Rigor" 2026-01-16 | https://voxday.net/2026/01/16/historic-rigor/ kept (AI-system rigor ratings of PZ) |
| "PZ Print Editions" | https://voxday.net/2026/02/02/pz-print-editions/ kept |
| Not requested but found untagged: "The Education of a Population Geneticist" (2026-10-01), "Response to Dennis McCarthy, Round 2" (2026-02-04), "Dennis McCarthy's Round 2" (02-03), "The Reproducibility Crisis in Action" (02-03), "Clones and the Frozen Gene" (04-10), "Anti-Natalism and d" (04-14), "Scientist Wanted" (01-14) | kept. The 2026-02-04 post contains the F_max formula and the 2026-10-01 post the k = 32.3 mu claim |

## Gap windows (archive scan, all pages of each month)
| window | posts found on voxday.net | relevant to evolution/MITTENS/Kimura/fixation | note |
|---|---|---|---|
| 2026-06-21 to 2026-08-22 | 156 | 0 (one passing "Kimura" mention in "Augmentation, Not Replacement" 2026-07-21, excluded) | Posts are politics, war, football, AI project, fiction. Last pre-gap evolution post 2026-06-20 "Another Failed Critique"; next 2026-08-23 "Chalub and the Kimura Cancellation" |
| 2026-08-28 to 2026-09-10 | 38 | 0 | Next evolution post 2026-09-11 "Do Try to Keep Up, Dennis" |
Posts inside the windows were scanned from archive-page text for 22 keywords, not individually saved.

## Not found / inaccessible
- Amazon product pages (PZ, TFG): bot-check, no price/ISBN-13 obtained; sale price ($0.99 ebook, May 2026) and hardcover $29.99 / signed $250 (both "sold out" on 2026-10-07) from blog and NDM Express pages.
- Book *Probability Zero* (both editions) and *The Frozen Gene*: not purchased; claims known only from the book are `secondhand`. The 2nd-edition introduction text is quoted in a blog post.
- 2021 "debate" with Gariepy: no separate 2021 debate located; the 2019-02-07 live debate (YouTube https://youtu.be/Aaqec_0FPqA, not fetched) had its full transcript posted 2021-11-11. Day says he no longer does video debates (2021-11-14).
- k = 32.3 mu derivation: none in the corpus harvested.
- Hard Limits (Z22129121) and aDNA (Z23046531) PDFs: no reference list located in the extracted text (to be confirmed by a human reading the PDF).
- Zenodo multi-version records: only two prior versions exist in the result set (Bio-Cycle, RRME). MITTENS 3.0 (Z23003785) record was modified 2026-10-04 after its 2026-09-28 creation, and Z18165980 / Z19984826 were not checked for later revisions; record `modified` dates are in `zenodo-search-p*.json`.
- Blog comments sections are inside the saved HTML but were not triaged.
- Wistar/Ulam/Schutzenberger material beyond the blog mentions (2026-01-25 "A 60-Year-Old Book Review", 2026-10-05/06 "The Best They've Got") was not extracted into quotes (branch D not in the required quote list).

## Zenodo records skipped (philosophy/theology; listed in bib-day.md)
18888781, 18724496, 18724487, 18788051, 18727817, 18717939, 19022126, 18911901, 18724454, 18924026, 18930279.

## Excluded blog posts (fetched, triaged out) - one-word reason
| date | URL | found via | reason |
|---|---|---|---|
| 2019-01-18 | https://voxday.net/2019/01/18/unauthorized-science/ | search | offtopic |
| 2019-01-26 | https://voxday.net/2019/01/26/tens-continues-to-degrade/ | evotag | news |
| 2019-03-19 | https://voxday.net/2019/03/19/migration-is-genetic-genocide/ | search | offtopic |
| 2019-06-18 | https://voxday.net/2019/06/18/stop-eating-people/ | search | offtopic |
| 2019-06-27 | https://voxday.net/2019/06/27/seriously-stop-eating-people/ | search | offtopic |
| 2019-09-26 | https://voxday.net/2019/09/26/mailvox-are-they-that-stupid/ | search | offtopic |
| 2020-03-18 | https://voxday.net/2020/03/18/a-darwinian-theory-proved/ | evotag | news |
| 2020-06-13 | https://voxday.net/2020/06/13/canceling-darwin/ | search | offtopic |
| 2020-09-07 | https://voxday.net/2020/09/07/cancelling-darwin/ | search | offtopic |
| 2020-11-16 | https://voxday.net/2020/11/16/or-what/ | search | offtopic |
| 2021-01-20 | https://voxday.net/2021/01/20/failure-has-consequences/ | search | offtopic |
| 2021-02-11 | https://voxday.net/2021/02/11/amazon-shows-its-allegiance/ | search | offtopic |
| 2021-02-19 | https://voxday.net/2021/02/19/the-third-world-comes-to-texas/ | search | offtopic |
| 2021-05-04 | https://voxday.net/2021/05/04/genetically-modified-inferiors/ | evotag | offtopic |
| 2021-05-13 | https://voxday.net/2021/05/13/canceling-biology/ | search | offtopic |
| 2021-05-27 | https://voxday.net/2021/05/27/techno-babylon-or-the-religion-of-science/ | search | offtopic |
| 2021-07-01 | https://voxday.net/2021/07/01/silenced-by-self-darwining/ | search | offtopic |
| 2021-08-17 | https://voxday.net/2021/08/17/mailvox-sink-the-ships-and-save-the-street/ | search | offtopic |
| 2021-10-12 | https://voxday.net/2021/10/12/mailvox-dying-suddenly/ | search | offtopic |
| 2021-10-30 | https://voxday.net/2021/10/30/anti-effective/ | search | offtopic |
| 2022-01-20 | https://voxday.net/2022/01/20/evil-always-eats-its-own/ | evotag | offtopic |
| 2022-02-06 | https://voxday.net/2022/02/06/darwin-was-an-anti-christian-psyop/ | evotag | rhetoric |
| 2022-04-21 | https://voxday.net/2022/04/21/why-do-you-hate-science/ | evotag | empty |
| 2022-04-23 | https://voxday.net/2022/04/23/all-ur-biogods-are-belong-to-us/ | evotag | quote-only |
| 2022-07-12 | https://voxday.net/2022/07/12/evolutionary-epicycles-and-episyntheses/ | evotag | news |
| 2022-08-11 | https://voxday.net/2022/08/11/depopulation-vectors/ | search | offtopic |
| 2023-03-02 | https://voxday.net/2023/03/02/the-end-of-the-involuntary-non-european/ | search | offtopic |
| 2023-04-04 | https://voxday.net/2023/04/04/another-nail-in-darwins-coffin/ | evotag | news |
| 2023-07-17 | https://voxday.net/2023/07/17/theyre-going-to-need-an-older-universe/ | evotag | cosmology |
| 2023-08-04 | https://voxday.net/2023/08/04/one-race-the-canine-race/ | evotag | rhetoric |
| 2023-08-14 | https://voxday.net/2023/08/14/sf-is-dying-and-la-is-next/ | evotag | offtopic |
| 2023-08-17 | https://voxday.net/2023/08/17/then-they-came-for-wranglerstar/ | search | offtopic |
| 2023-10-06 | https://voxday.net/2023/10/06/perhaps-she-just-evolved/ | evotag | personal |
| 2023-10-10 | https://voxday.net/2023/10/10/green-flag-or-neoclown-bait/ | search | offtopic |
| 2023-10-25 | https://voxday.net/2023/10/25/us-specops-kia-in-gaza/ | search | offtopic |
| 2023-11-29 | https://voxday.net/2023/11/29/stumbling-toward-2033/ | search | offtopic |
| 2024-01-31 | https://voxday.net/2024/01/31/artificial-bafflegarble/ | evotag | offtopic |
| 2024-04-16 | https://voxday.net/2024/04/16/evolution-by-dark-selection/ | evotag | news |
| 2024-05-13 | https://voxday.net/2024/05/13/history-is-incomplete/ | evotag | offtopic |
| 2024-05-28 | https://voxday.net/2024/05/28/the-feast-of-st-harambe/ | search | offtopic |
| 2024-07-09 | https://voxday.net/2024/07/09/mailvox-poland-makes-a-move/ | search | offtopic |
| 2024-11-22 | https://voxday.net/2024/11/22/the-rhetoric-of-london-larry/ | search | offtopic |
| 2025-01-25 | https://voxday.net/2025/01/25/keep-your-pillows-fluffy/ | search | offtopic |
| 2025-04-08 | https://voxday.net/2025/04/08/the-last-librarian/ | search | offtopic |
| 2025-06-22 | https://voxday.net/2025/06/22/another-nail-in-the-coffin/ | evotag | news |
| 2025-07-17 | https://voxday.net/2025/07/17/about-that-analytical-thinking/ | evotag | news |
| 2025-08-07 | https://voxday.net/2025/08/07/a-new-evolutionary-epicycle/ | evotag | news |
| 2025-08-18 | https://voxday.net/2025/08/18/the-kenobi-years/ | evotag | offtopic |
| 2025-09-26 | https://voxday.net/2025/09/26/its-not-getting-easier/ | evotag | news |
| 2025-10-02 | https://voxday.net/2025/10/02/the-foundation-of-sand/ | evotag | link-only |
| 2025-10-07 | https://voxday.net/2025/10/07/genetic-aberrations/ | evotag | news |
| 2025-11-07 | https://voxday.net/2025/11/07/death-and-the-darwinian/ | search | ai-rhetoric |
| 2025-11-22 | https://voxday.net/2025/11/22/ai-hallucinations-are-wikislop/ | search | ai-rhetoric |
| 2025-12-17 | https://voxday.net/2025/12/17/a-historic-honor/ | evotag | praise |
| 2025-12-19 | https://voxday.net/2025/12/19/he-just-gets-it/ | evotag | ai-praise |
| 2025-12-26 | https://voxday.net/2025/12/26/how-ai-killed-scientistry/ | search | ai-rhetoric |
| 2025-12-28 | https://voxday.net/2025/12/28/more-bass-more-better/ | search | offtopic |
| 2026-01-10 | https://voxday.net/2026/01/10/the-bullies-of-iu/ | search | offtopic |
| 2026-01-15 | https://voxday.net/2026/01/15/the-intellectual-razor/ | search | offtopic |
| 2026-01-17 | https://voxday.net/2026/01/17/enjoy-the-audio/ | search | offtopic |
| 2026-01-22 | https://voxday.net/2026/01/22/more-books-more-better/ | search | offtopic |
| 2026-01-23 | https://voxday.net/2026/01/23/cooking-with-or-getting-cooked/ | search | offtopic |
| 2026-01-23 | https://voxday.net/2026/01/23/yeah-so-about-that-3/ | evotag | meme |
| 2026-01-26 | https://voxday.net/2026/01/26/why-the-economy-is-collapsing/ | search | offtopic |
| 2026-01-29 | https://voxday.net/2026/01/29/karma-is-a-bitch/ | search | offtopic |
| 2026-02-01 | https://voxday.net/2026/02/01/an-interesting-week-ahead/ | search | offtopic |
| 2026-02-07 | https://voxday.net/2026/02/07/veriphysics-the-treatise-006/ | search | offtopic |
| 2026-02-08 | https://voxday.net/2026/02/08/ricardos-deliberate-deception/ | search | offtopic |
| 2026-02-11 | https://voxday.net/2026/02/11/book-review-the-frozen-gene/ | evotag | bookreview |
| 2026-02-13 | https://voxday.net/2026/02/13/veriphysics-the-treatise-012/ | search | offtopic |
| 2026-02-17 | https://voxday.net/2026/02/17/veriphysics-the-treatise-016/ | search | offtopic |
| 2026-02-18 | https://voxday.net/2026/02/18/veriphysics-as-requested/ | search | offtopic |
| 2026-02-19 | https://voxday.net/2026/02/19/the-infamous-a-review/ | search | offtopic |
| 2026-02-21 | https://voxday.net/2026/02/21/the-undefeatable-trilemma/ | search | offtopic |
| 2026-02-25 | https://voxday.net/2026/02/25/veriphysics-the-treatise-023/ | search | offtopic |
| 2026-02-26 | https://voxday.net/2026/02/26/veriphysics-and-the-fall-of-man/ | search | offtopic |
| 2026-02-27 | https://voxday.net/2026/02/27/biostellar-space-fleet-academy/ | search | offtopic |
| 2026-02-27 | https://voxday.net/2026/02/27/veriphysics-the-treatise-024/ | search | offtopic |
| 2026-03-01 | https://voxday.net/2026/03/01/jerry-pournelle-would-be-pleased/ | search | offtopic |
| 2026-03-15 | https://voxday.net/2026/03/15/a-true-soulsigma-fan/ | search | offtopic |
| 2026-03-26 | https://voxday.net/2026/03/26/the-cruel-equations/ | search | offtopic |
| 2026-03-29 | https://voxday.net/2026/03/29/truly-hard-science-fiction/ | search | offtopic |
| 2026-04-29 | https://voxday.net/2026/04/29/john-scalzi-killed-science-fiction/ | search | offtopic |
| 2026-05-02 | https://voxday.net/2026/05/02/the-decay-function-of-professional-science/ | search | offtopic |
| 2026-05-15 | https://voxday.net/2026/05/15/owen-on-tucker/ | search | offtopic |
| 2026-05-17 | https://voxday.net/2026/05/17/science-is-garbage/ | search | rhetoric |
| 2026-05-18 | https://voxday.net/2026/05/18/the-gatekeepers-confession/ | search | offtopic |
| 2026-05-20 | https://voxday.net/2026/05/20/based-books-2026/ | search | offtopic |
| 2026-05-24 | https://voxday.net/2026/05/24/the-atheists-genetic-fallacy/ | evotag | rhetoric |
| 2026-05-26 | https://voxday.net/2026/05/26/were-number-two/ | search | offtopic |
| 2026-06-03 | https://voxday.net/2026/06/03/on-the-print-edition/ | search | offtopic |
| 2026-06-13 | https://voxday.net/2026/06/13/books-and-more-books/ | search | offtopic |
| 2026-07-21 | https://voxday.net/2026/07/21/augmentation-not-replacement/ | search | offtopic |
| 2026-08-22 | https://voxday.net/2026/08/22/the-satanic-inversion-of-frozen/ | search | offtopic |
| 2026-09-12 | https://voxday.net/2026/09/12/the-uncomfortable-conclusion/ | evotag | rhetoric |
| 2026-09-24 | https://voxday.net/2026/09/24/mailvox-they-lost-the-atheists/ | evotag | mailbag-rhetoric |
| 2026-09-30 | https://voxday.net/2026/09/30/no-one-is-ready-for-it/ | search | promo |
| 2026-10-02 | https://voxday.net/2026/10/02/repent-richard/ | search | offtopic |
| 2026-10-03 | https://voxday.net/2026/10/03/better-than-a-phd/ | evotag | link-only |

## Pre-2019 evolution-tag posts (not fetched)
| date | URL | found via | reason |
|---|---|---|---|
| 2007-08-09 | https://voxday.net/2007/08/09/revising-revision-again/ | evotag | pre2019 |
| 2009-10-12 | https://voxday.net/2009/10/12/so-much-for-fossil-record/ | evotag | pre2019 |
| 2009-10-14 | https://voxday.net/2009/10/14/mailvox-new-find/ | evotag | pre2019 |
| 2009-11-03 | https://voxday.net/2009/11/03/mailvox-materialist-writes-back/ | evotag | pre2019 |
| 2009-11-12 | https://voxday.net/2009/11/12/darwins-killer-disciples/ | evotag | pre2019 |
| 2010-01-09 | https://voxday.net/2010/01/09/economics-and-evolution/ | evotag | pre2019 |
| 2010-02-24 | https://voxday.net/2010/02/24/idol-crumbles/ | evotag | pre2019 |
| 2010-02-27 | https://voxday.net/2010/02/27/question-for-ed-brayton/ | evotag | pre2019 |
| 2010-02-28 | https://voxday.net/2010/02/28/unfalsifiable-science/ | evotag | pre2019 |
| 2010-03-19 | https://voxday.net/2010/03/19/mailvox-book-for-suckers/ | evotag | pre2019 |
| 2010-03-21 | https://voxday.net/2010/03/21/of-mice-and-gods/ | evotag | pre2019 |
| 2010-03-31 | https://voxday.net/2010/03/31/science-teacher-responds/ | evotag | pre2019 |
| 2010-04-07 | https://voxday.net/2010/04/07/evolution-finally-observed/ | evotag | pre2019 |
| 2010-08-05 | https://voxday.net/2010/08/05/darwinianism-and-evolution/ | evotag | pre2019 |
| 2010-09-03 | https://voxday.net/2010/09/03/applying-science-to-string-theory/ | evotag | pre2019 |
| 2010-11-11 | https://voxday.net/2010/11/11/ignoring-elephan-2/ | evotag | pre2019 |
| 2011-08-01 | https://voxday.net/2011/08/01/when-im-wrong-it-proves-im-rig/ | evotag | pre2019 |
| 2011-08-12 | https://voxday.net/2011/08/12/lecturing-butterfly-collector/ | evotag | pre2019 |
| 2011-08-27 | https://voxday.net/2011/08/27/mailvox-concerning-questions/ | evotag | pre2019 |
| 2011-08-28 | https://voxday.net/2011/08/28/seculars-are-seriously-insane/ | evotag | pre2019 |
| 2011-09-01 | https://voxday.net/2011/09/01/formidable-defender-of-darwin/ | evotag | pre2019 |
| 2011-09-04 | https://voxday.net/2011/09/04/mailvox-skeptics-case/ | evotag | pre2019 |
| 2011-09-06 | https://voxday.net/2011/09/06/they-cant-read-they-cant-write/ | evotag | pre2019 |
| 2011-09-07 | https://voxday.net/2011/09/07/questions-for-evolutionists/ | evotag | pre2019 |
| 2011-09-14 | https://voxday.net/2011/09/14/of-snakes-and-science-fads/ | evotag | pre2019 |
| 2011-09-16 | https://voxday.net/2011/09/16/mailvox-scientists-wanted/ | evotag | pre2019 |
| 2011-10-29 | https://voxday.net/2011/10/29/they-just-never-learn/ | evotag | pre2019 |
| 2012-01-18 | https://voxday.net/2012/01/18/climate-change-is-new-evolution/ | evotag | pre2019 |
| 2012-03-18 | https://voxday.net/2012/03/18/myth-of-evolution-my/ | evotag | pre2019 |
| 2012-06-06 | https://voxday.net/2012/06/06/end-of-evolution-debate/ | evotag | pre2019 |
| 2012-07-10 | https://voxday.net/2012/07/10/so-much-for-science-is-settled_10/ | evotag | pre2019 |
| 2012-10-02 | https://voxday.net/2012/10/02/mailvox/ | evotag | pre2019 |
| 2012-10-11 | https://voxday.net/2012/10/11/evolution-and-potential-rabbi/ | evotag | pre2019 |
| 2012-10-13 | https://voxday.net/2012/10/13/mailvox-education-and-evolutionis/ | evotag | pre2019 |
| 2012-10-14 | https://voxday.net/2012/10/14/mailvox-alternative-mechanis/ | evotag | pre2019 |
| 2012-10-18 | https://voxday.net/2012/10/18/my-question-for-richard-dawkins/ | evotag | pre2019 |
| 2013-02-01 | https://voxday.net/2013/02/01/the-ripped-life/ | evotag | pre2019 |
| 2013-02-15 | https://voxday.net/2013/02/15/falsification/ | evotag | pre2019 |
| 2013-03-07 | https://voxday.net/2013/03/07/genotribes-and-superracis/ | evotag | pre2019 |
| 2013-04-19 | https://voxday.net/2013/04/19/pz-myers-throws-out-darwin/ | evotag | pre2019 |
| 2013-04-20 | https://voxday.net/2013/04/20/mailvox-rhetoric-is-not-science/ | evotag | pre2019 |
| 2013-04-22 | https://voxday.net/2013/04/22/mike-williams-is-too-real-smar/ | evotag | pre2019 |
| 2013-04-24 | https://voxday.net/2013/04/24/a-biologist-seeks-to-dumb-down-science/ | evotag | pre2019 |
| 2013-04-24 | https://voxday.net/2013/04/24/mailvox-evolution-and-slippery-slope/ | evotag | pre2019 |
| 2013-04-26 | https://voxday.net/2013/04/26/west-hunter-abuses-eo-wilson/ | evotag | pre2019 |
| 2013-08-16 | https://voxday.net/2013/08/16/mailvox-what-color-amused/ | evotag | pre2019 |
| 2013-10-29 | https://voxday.net/2013/10/29/in-defense-of-intelligent-design/ | evotag | pre2019 |
| 2013-11-22 | https://voxday.net/2013/11/22/fred-on-limits-of-human-knowledge/ | evotag | pre2019 |
| 2013-11-25 | https://voxday.net/2013/11/25/mailvox-response-to-fred/ | evotag | pre2019 |
| 2013-12-05 | https://voxday.net/2013/12/05/the-outdated-neo-darwinists/ | evotag | pre2019 |
| 2013-12-09 | https://voxday.net/2013/12/09/fred-meets-evolutionists-wins/ | evotag | pre2019 |
| 2014-01-02 | https://voxday.net/2014/01/02/mailvox-atheist-philosophy-in-action/ | evotag | pre2019 |
| 2014-01-10 | https://voxday.net/2014/01/10/more-highly-evolved/ | evotag | pre2019 |
| 2014-01-24 | https://voxday.net/2014/01/24/the-implications-of-complexity/ | evotag | pre2019 |
| 2014-01-29 | https://voxday.net/2014/01/29/mailvox-pressing-for-ki/ | evotag | pre2019 |
| 2014-02-07 | https://voxday.net/2014/02/07/a-nightmare-for-science/ | evotag | pre2019 |
| 2014-03-12 | https://voxday.net/2014/03/12/the-mysteries-of-tens/ | evotag | pre2019 |
| 2014-07-30 | https://voxday.net/2014/07/30/fred-calls-out-derbyshire-and-darwinists/ | evotag | pre2019 |
| 2014-08-16 | https://voxday.net/2014/08/16/lamarck-lives/ | evotag | pre2019 |
| 2015-01-23 | https://voxday.net/2015/01/23/evolution-is-random-process/ | evotag | pre2019 |
| 2015-01-23 | https://voxday.net/2015/01/23/explaining-probability/ | evotag | pre2019 |
| 2015-01-29 | https://voxday.net/2015/01/29/probability-and-belief/ | evotag | pre2019 |
| 2015-03-12 | https://voxday.net/2015/03/12/evolution-and-problem-of-time/ | evotag | pre2019 |
| 2015-06-01 | https://voxday.net/2015/06/01/evolution-or-equality/ | evotag | pre2019 |
| 2015-06-04 | https://voxday.net/2015/06/04/post-evolutionary-man/ | evotag | pre2019 |
| 2015-06-17 | https://voxday.net/2015/06/17/mailvox-how-to-teach-evolution/ | evotag | pre2019 |
| 2017-03-27 | https://voxday.net/2017/03/27/a-theory-falsified/ | evotag | pre2019 |
| 2018-05-28 | https://voxday.net/2018/05/28/dawkins-syndrome/ | evotag | pre2019 |
| 2018-08-03 | https://voxday.net/2018/08/03/evolution-evaluated/ | evotag | pre2019 |
| 2018-08-23 | https://voxday.net/2018/08/23/scientistry-in-action/ | evotag | pre2019 |
| 2018-09-24 | https://voxday.net/2018/09/24/the-pseudoscience-of-darwin/ | evotag | pre2019 |
| 2018-09-25 | https://voxday.net/2018/09/25/the-darwinian-fraud/ | evotag | pre2019 |


## Refresh 2026-10-09 (corpus refresh, Day slice)
Run date 2026-10-09. Last prior harvest 2026-10-07 (latest dated item then: blog 2026-10-07 "An Epic Test", Zenodo 23188201 of 2026-10-06). Requests were serial with at least 1 s spacing; `curl -A 'Mozilla/5.0'` for voxday.net, Substack public JSON API for newsletters, Zenodo REST API (page size 25). Nothing posted, archived on Wayback, or sent. Raw copies: `sources/raw/refresh-2026-10-09/` (gitignored). Each fetch is in its own subdirectory; text was extracted with `research/.venv/bin/python -I` and read or grepped only.

### Counts
| item | count |
|---|---|
| New Day blog posts dated after 2026-10-07 | 2 (2026-10-08 "Not Just the Evo-Avengers" kept; "Black Britons and White Japanese" excluded) |
| Day blog posts dated 2026-10-02..07 not triaged on 2026-10-07 (fetched now) | 11 (1 kept as low-value: "Better than a PhD"; 10 excluded) |
| New Zenodo records by "Day, Vox" | 0 (API total still 39; newest 23188201, 2026-10-06) |
| Zenodo records changed since the local copy | 0 (md5 identical for Z23188201, Z23003785 and its addendum, Z23105291, Z23046531, Z22903977, Z22129121) |
| Day posts on other venues fetched (not previously in bib) | 5 newsletter posts (AI Central 1; Sigma Game 4) |
| Day comment threads harvested for the first time | 4 Substack threads (Dembski interview, Hossjer review, McCarthy x2; includes pre-2026-10-07 backfill from 2026-09-12 onward) |
| New quotes | 18 (Q79-Q96) |

### Method
1. `/tag/evolution/` page 1 (latest 13 posts through 2026-10-08) and `/2026/10/` pages 1-3 (23 unique URLs; pages 4-5 are 404). Compared every URL with `bib-day.md` and the 2026-10-07 exclusion list; fetched the 12 not present.
2. voxday.net site search (`/?s=`) for MITTENS, Kimura, fixation, "Probability Zero", evolution, Mansfield, McCarthy, Hancock, Gutsick, Dembski, Hossjer, population genetics, aDNA, Haldane, mutation, genome, Athos, neutral. The newest hits dated 2026-09-25 onward are all already in `bib-day.md` or listed below. No untagged post touching MITTENS, fixation, Haldane or aDNA was found beyond those.
3. Front page on 2026-10-09: no post dated 2026-10-09 yet.
4. Zenodo: `creators.name:"Day, Vox"` sorted newest, two pages; also `creators.name:"Athos, Claude"` (38 hits, all of them Day co-authored), `"Vox Day"` (5 hits: none by Day; one is a 2026-02-18 record by Camestros Felapton, "Vox Day and Baron Muenchhausen: Trilemmas and Right-Wing Epistemology", a philosophy item, out of scope).
5. Day's other venues: Sigma Game archive (100 posts listed through 2026-10-08; three touch evolution: 09-22, 10-02, 10-05, plus the 2026-01-30 series announcement), AI Central (cross-post of 2026-10-03). Substack comment threads under McCarthy's and Dembski's posts, where Day replied in person.

### Excluded posts (fetched 2026-10-09, triaged out)
| Post | Reason |
|---|---|
| 2026-10-02 "Repent, Richard" | Atheism/Dawkins; one assertion ("proven that evolution by natural selection never happened") with no math |
| 2026-10-02 "Sign Up Now for Unlimited" | promo |
| 2026-10-03 "The Scholars' Revolt" | politics/books |
| 2026-10-04 "Back to the 70s" | politics/culture |
| 2026-10-05 "An Epic Day" | Castalia House translation announcement |
| 2026-10-05 "Skol, But" | off-topic |
| 2026-10-05 "Watering the Desert" | EU/Ukraine |
| 2026-10-06 "Let Them Take Out LA" | politics (cited by a Reddit commenter, not math) |
| 2026-10-06 "Lockdown Fakery Incoming" | 18 words, link only |
| 2026-10-08 "Black Britons and White Japanese" | politics |
| Sigma Game 2026-10-05 "What We Think We Know" | evolutionary psychology list; only consequence statement, no math |
| Sigma Game 2026-01-08 "Gamma Doubts", 2026-01-30 "The Mathematics of Evolution" | pre-harvest backfill; no new numbers (covered by existing Q-series and claim B3g); hashed and listed in bib |

### Not fetched or not read (with reasons)
- socialgalactic.com micropost links (the Vibe Patrol music video of "Better than a PhD", `728e642c-...`; the micropost under the 10-08 post, `bef3d348-...`): `curl` fails TLS verification (certificate chain not verifiable). Not bypassed (no `-k`). Logged as inaccessible.
- The "Vibe Patrol" music video itself: not located.
- Amazon book pages: not attempted again (bot check on 2026-10-07).
- Sigma Game posts "Working with the Sigma", "SSH is Not Evolutionary Psychology" (2026-01-07): search results only; not read (evopsych/SSH).
- wholereason.com, audaxconsilium "Scorched & Salted" (2026-02-18): skimmed grep only; ally summaries, no new numbers. Not in bib.
- Day's X, Gab, YouTube (banned per his own comments), Rumble: not accessed.
- Probability Zero book (paid, 2nd edition): still not accessed. The 2nd-edition abstract is known only through Day's own quotation of it (Q91).

### Findings that affect existing ledgers
- `ledgers/versions.md`: three rows added (2nd-edition numbers 180 / 1,400 / 1,139,000-fold; Day's own adoption of 1,587; "selection ceased ~1800" claim; Darwillion status in comments).
- Day's 2026-10-07 "An Epic Test" (already in the corpus) announces a new unpublished disproof and an unpublished "epic data analysis"; Q84 records "Reverse-MITTENS", a term not defined in any harvested text. Nothing to check until it is published.

## Refresh 2026-10-09b (second pass, same day; Day slice plus social media)
Run 2026-10-09 evening (about 19:55 UTC and later), after the 2026-10-09 morning pass. Raw files: `sources/raw/refresh-2026-10-09b/` (gitignored). Requests serial, 1 s spacing. Nothing posted, archived, or sent.

### Counts
| item | count |
|---|---|
| New Day blog posts since the previous pass (dated 2026-10-09) | 4: "The Irrelevance of EES" (kept), "Mailvox: Invoking the Triveritas" (kept), "The Scholars' Revolt Spreads" (excluded, Belgian riots), "RIP Mike Ditka" (excluded, not fetched) |
| Day blog posts 2026-10-06 not previously fetched | "No Reconciliation" was already in bib-day (2026-10-07 pass); re-read, no change |
| New Zenodo records by "Day, Vox" | 0 (API total 39; newest 23188201 created 2026-10-06, modified 2026-10-07) |
| Zenodo files with changed checksums | 0 (all file checksums in the 39 records identical to the 2026-10-09 morning listing; no download needed because the API returns md5 per file) |
| Newsletter posts (Sigma Game / AI Central) dated after the previous pass | Sigma Game 10-07 "The Predatory Parents", 10-08 "The Boomer Contract", 10-09 "Abandoning the Ethics of Consent": titles only, not evolution (not fetched). AI Central 10-09 "Drop the Sample, Get the Sound": not evolution (not fetched) |
| Backfill found | Sigma Game 2026-01-09 "We Knew How This Would Go" (not in bib before): two quotes, Q125-Q126 |
| New quotes | 9 (Q118-Q126) |

### Method
1. Zenodo: `curl "https://zenodo.org/api/records?q=creators.name:%22Day,%20Vox%22&size=25&page=N&sort=newest"` (pages 1 and 2). **Pitfall:** with a browser `User-Agent` header Zenodo returned `403 Forbidden` ("unusual traffic"); plain `curl` with the default agent worked. Compared record ids, `modified` dates and per-file `checksum` fields with `refresh-2026-10-09/zenodo-list/list1.json` and `list2.json` in a ten-line script.
2. voxday.net: `/feed/` (RSS, newest 10 posts) and `/tag/evolution/`; extracted all 2026/10 links and compared with `bib-day.md`. Fetched the four unseen 2026-10-09 URLs with `curl -A 'Mozilla/5.0'`.
3. Substack archive API (`/api/v1/archive?sort=new&limit=8`) for sigmagame, substack.aicentral.blog; comment APIs are in the critics log.
4. Social media: see the critics log (X, Gab, Telegram, Bluesky, Mastodon, Rumble, Locals).

### Kept posts
| Post | Why kept |
|---|---|
| 2026-10-09 "The Irrelevance of EES" (tags evolution, science, technology, UATV) | Day's answer to Hilbert's EES argument: calls EES irrelevant, claims "natural selection is empirically irrelevant" and announces the 96-core simulation resource (Q122-Q124). Reposts three Hilbert comments from the Dembski thread (RF-18; relay) |
| 2026-10-09 "Mailvox: Invoking the Triveritas" | New numeric argument: the Yoo 2025 total (410 Mb) "can't possibly be correct" (7e9 x 0.0857 = 599.9e6), the CSAC 8.57 percent size claim, and Day's explanation for halving (Q118-Q121) |

### Excluded
- "The Scholars' Revolt Spreads" (2026-10-09): Belgian student riots, off topic.
- "RIP Mike Ditka" (2026-10-09): off topic, not fetched.

### Not fetched or not read
- X/Twitter (@voxday): see the critics log "Social media" table (JS shell only).
- The UATV broadcast of 2026-10-09 evening (where Day says he will discuss the simulation resource): not available yet; check on the next refresh.
- Day's Darkstream / Rumble / Locals: Rumble `/user/VoxDay` returned 404; `voxday.locals.com` redirects (302, no content).

### Findings that affect existing ledgers
- `ledgers/versions.md`: 2 rows added (Yoo 410 Mb handling restated with the 8.57 percent argument; "40 million fixations" in 2026-01).
- New unpublished-result pointer: Q123 "natural selection is empirically irrelevant", Q124 hardware; no data yet.
