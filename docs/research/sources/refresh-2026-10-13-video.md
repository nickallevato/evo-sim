# Source refresh 2026-10-13 (video slice): the Gutsick Gibbon roundtable

Run under brief `research/checks/briefs/VID-01-operator.md` (check VID-01), procedure `HOWTO-refresh.md`.
Read-only fetches. No comment, no contact with the author, no archive snapshot (rule 6).
Everything below comes from the fetched text (rule 8): the video postdates the model cutoff.

## Gate: captions

**The gate opened.** At the 2026-10-13 morning fetch the video had no caption track (`QUEUE.md`,
"unreviewed critic reply"). At the fetch logged here, **2026-10-13 21:51 UTC**, the watch page carried
one caption track: `English (auto-generated)`, `kind: asr`, `vssId: a.en`, no human track and no other
language. The brief's stop condition (still no captions -> record the dated negative result and stop)
therefore did not apply, and the harvest ran. No audio was transcribed by this audit.

Method: `curl` of the watch page into `sources/raw/vid01-2026-10-13/` (its own new directory, rule 4),
then `research/.venv/bin/yt-dlp --skip-download --write-auto-subs --sub-langs en --sub-format vtt
--write-info-json`. The signed `timedtext` URL on the watch page returned 0 bytes when fetched directly;
yt-dlp's own player request returned the track. **Tooling note:** `yt-dlp` was absent from
`research/.venv` (`HOWTO-refresh.md` §5 assumes it) and was reinstalled into it with
`pip install --no-deps yt-dlp` (2026.8.19, no new transitive packages; `requirements.txt` is unchanged
and still pins the numeric stack). Recorded here so the next refresh does not repeat the diagnosis.

## The source

| field | value (from `AqC1ZM4icms.info.json`) |
|---|---|
| id / URL | `AqC1ZM4icms` / https://www.youtube.com/watch?v=AqC1ZM4icms |
| title | Six Scientists Roast One Racist Loser (Heartwarming) (Four Hours) (Hopecore) |
| channel | Gutsick Gibbon |
| published | 2026-10-13T11:00:40-07:00 = 18:00:40 UTC |
| duration | 15,242 s = 4:14:02 |
| counters at access | 18,566 views, 2,046 likes, 656 comments |
| chapters | none |
| participants (description) | Grayson, Zach (Hancock), Jon, Dan, Maddie, in order of appearance, plus the host |
| access | 2026-10-13 21:51 UTC |
| sha256 (en.vtt) | `aacdd0d9a93fa9dc368de9808df5536e7daee45bfc69c975fd44ff2bc72d4c14` |

Bib row: `bib-critics.md` key **GG-4**. Quotes: `quotes-critics.md` section `YT-AqC1ZM4icms`,
**GGR-01..GGR-40**, each machine-checked as an exact substring of the local transcript
(`research/tools/harvest/verify_vid01.py`, 42 of 42 PASS including the two rhetoric lines).
Rhetoric: `ledgers/slips.md` **RH-31** (the title) and **RH-32**.

## What it covers

| Segment | Topic | Audit branch |
|---|---|---|
| t=00:48-00:52 | no single average fixation rate; DFE; "biology has exceptions" | G1, A |
| t=01:06-01:09 | the core equation is "divergence time over generation length" times fixations per generation; "just a division"; 40 unlisted errors asserted; MITTENS 3.0 is 17 pages | A, epistemic |
| t=01:22-01:24 | the appendix paper judged against journal standards (12-14 references) | epistemic |
| t=01:36-01:40 | an LLM asked to "peer review" MITTENS 3.0; its five points read aloud and endorsed; Haldane's dilemma "not so much of a dilemma anymore" | A, F, B5 |
| t=01:44 | hearsay that MITTENS was submitted to Nature and rejected without revisions | epistemic |
| t=01:48-01:56 | first edition vs MITTENS 3.0: census-vs-N_e arguments dropped, averaging error and Bernoulli barrier omitted, 40 My -> 410 My differences; the d coefficient; the Bernoulli barrier defined only via a relayed Reddit comment | versions, A4, A4d, A4e, G |
| t=02:06-02:18 | the LTEE rate cannot be carried to humans (asexual, non-recombining); Day's drift-or-selection dichotomy read from the book and answered with within-genome heterogeneity of dN/dS and heterozygosity | A2e, A5c, A5f, B, B9 |
| t=03:43-03:47 | the s6.4 slip on screen: 38,400 vs 3,840; and the objection that s6.4 is not a genetic-load model at all | A5h |

## What it does not cover (keyword scan of the full transcript)

Scanned the 4-hour transcript for the audit's other branches. Counts are matching 20 s chunks, not
occurrences. Hits: `mesa` 0, `sigill` 0,
`overdisper` 0, `1240` 0 (the 1240k panel), `Reich` 0, `relict` 0, `ancient DNA|aDNA` 0,
`chromosome` 0, `GENCODE|consortium` 0, `20,400|13,454` 0, `CCR5` 0, `Holocene` 0,
`fourth mechanism` 0, `Kimura` 0 as spelled (the captions render it "Kamura", 7 chunks),
`dN/dS` 1 (as "DNDs", t=02:15:08, used for within-genome heterogeneity, not for Day's 0.80).

So the newest, longest and most credentialed critic reply to date still leaves untouched:

- **branch C** (aDNA zero fixations, the 1240k ascertainment argument),
- **branch DN** (genome-wide dN/dS = 0.80 on 20,400 genes; the 13,454-gene Consortium set),
- **branch FM** (the Fourth Mechanism: mesas, sigillation, overdispersion),
- **branch D** (sequence space, Eden/Schutzenberger/Wistar).

This extends, rather than closes, the dialectical gap recorded in `refresh-2026-10-12-critics.md`:
"the critic corpus ... has so far addressed Day's fixation-rate and MITTENS arguments, not genome-wide
dN/dS or substitution-density mesas". The gap now has one more, much larger, data point.
The standing constraint still holds in the other direction: **no milestone post may say "no critic
reply"** - there is one, it is four hours long, and it is now in the sources of record.

## Items for the analyst task this unblocks

Recorded, not applied. A harvest moves no verdict (brief, review tier).

1. **Apparent conflict with A4d** (GGR-13, GGR-14). The video says Day "is still using the d
   coefficient in mittens" and computes 450,000 generations x d -> "like 225,000". Claim A4d records
   that the MITTENS 3.0 text has **no** d term (searched "turnover" and "d ="), internal `holds`, and
   that 3.0 prints 252,000 nominal generations (not 450,000 x 0.45 = 202,500). Either the panel is
   describing an earlier version, or A4d's text search missed something. The video gives no locator.
   Under the balance rule this is as likely to be a critic-side error as a Day-side one, and it must be
   scored as such either way.
2. **A new objection at A5h** (GGR-33, GGR-34): s6.4 is "not the genetic load calculation", because
   mutational load goes as (1-mu)^loci, not (1-s)^loci. A5h's "Responses" currently lists only the
   arithmetic (RE-02 / A2h) and records "In support: none located". The modelling objection is new to
   the corpus and is a candidate external-verdict input for A5h.
3. **Independent confirmation of the 38,400 slip** (GGR-01, GGR-31, GGR-32) by a six-person panel that
   reached it on its own. One panellist says "3,800", corrected in the room to 3,840 - the audit's value.
4. **The clearest critic statement of the Bernoulli barrier so far** (GGR-18, GGR-19), relayed from a
   Reddit commenter with a master's in mathematics: a coefficient of variation going to zero as n grows,
   so by Fisher's fundamental theorem the rate of increase in mean fitness goes to zero. Branch G has had
   no such formulation from the critic side. The panel rejects it ("that's preposterous", t=01:57:03)
   without a derivation, which is the weaker half of the exchange.
5. **Credit to Day, recorded** (GGR-04): the panel's mathematician says the division "you did the
   division correctly".
6. **Three Day quotes relayed from the book** (GGR-22..GGR-24), including "Natural selection must be
   effectively turned off" and the 75%-harmful step. They bear on B9 and on the drift/selection
   dichotomy. They are relays (rule U) and must be re-quoted from Day's own text before any use.
7. **Unverifiable as stated**: "40 errors" (GGR-05) is a count with no list; the Nature rejection
   (GGR-40) is explicitly hearsay and the speaker does not know which version was submitted.

## Not done here

- Comments (656 at access) were not pulled; the brief did not ask for them and no quote above depends on
  them. A later refresh can add them with the cap used for GG-1.
- No scoring, no claim-file edit, no `QUEUE.md` edit (brief: files I may write).
- No run on `na-workhorse` (busy with `ph2` until 2026-10-16).
