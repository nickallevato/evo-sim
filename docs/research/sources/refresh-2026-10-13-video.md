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
**GGR-01..GGR-46** (GGR-41..GGR-46 appended by the fix pass of 2026-10-13), each machine-checked as an
exact substring of the local transcript (`research/tools/harvest/verify_vid01.py`, **48 of 48 PASS**
including the two rhetoric lines; 42 of 42 at the harvest commit `6d090de`).
Rhetoric: `ledgers/slips.md` **RH-31** (the title) and **RH-32**.

## What it covers

| Segment | Topic | Audit branch |
|---|---|---|
| t=00:48-00:52 | no single average fixation rate; DFE; "biology has exceptions" | G1, A |
| t=01:06-01:09 | the core equation is "divergence time over generation length" times fixations per generation; "just a division"; 40 unlisted errors asserted; MITTENS 3.0 is 17 pages | A, epistemic |
| t=01:22-01:24 | the appendix paper judged against journal standards (12-14 references) | epistemic |
| t=01:36-01:40 | an LLM asked about MITTENS 3.0; it reviewed the Haldane-1,600 version from its own recollection ("as I recall, the estimate is a Haldane style ceiling of roughly 1,600 selected ... fixations", t=01:37:03); its five points read aloud and endorsed; Haldane's dilemma "not so much of a dilemma anymore" | A, F, B5 |
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

So the newest and longest critic reply to date (six panellists, described in the title as scientists;
the audit has an independent record of one PhD among them, Hancock) still leaves untouched:

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
   **Revised 2026-10-13 (fix pass; review MINOR-4, lead ruling R-3).** The earlier sentence here - that
   this is "as likely to be a critic-side error as a Day-side one" - is **withdrawn**: the audit's own
   files do not support a symmetric prior, and a bare appeal to balance is not evidence. Grayson says
   "in mittens", not "in Mittens 3.0", so the referent is unsettled and three readings are recorded
   (rule RD; full text and citations in the GGR-13 note):
   (a) "mittens" = the pre-3.0 / *Probability Zero* line - **no conflict**, and 450,000 x 0.45 = 202,500
   is exactly the Tree of Woe figure the audit already records (`A-mittens-formula.md` TW-01; A4
   `derived:`);
   (b) = the MITTENS 3.0 body - **contradicted by A4d** (252,000 nominal generations, no d term);
   (c) = 3.0 including Appendix D - **partly right**, since A4d's own Weaknesses line records that the
   Appendix D rate still cites the "Bio-Cycle correction for overlapping generations" (A5e).
   The host's own narration in the same segment ("He kind of throws the D coefficient off to the side.
   It no longer seems nearly as important as it was in probability zero", t=01:49:52) agrees with A4d.
   No winner is declared here and **A4d is not touched**; the analyst scoring task decides.
2. **A new objection at A5h** (GGR-33, GGR-34): s6.4 is "not the genetic load calculation", because
   mutational load goes as (1-mu)^loci, not (1-s)^loci. A5h's "Responses" currently lists only the
   arithmetic (RE-02 / A2h) and records "In support: none located". The modelling objection is new to
   the corpus and is a candidate external-verdict input for A5h.
   **Both halves added 2026-10-13 (fix pass; review MINOR-5 and NOTE-3, lead ruling R-2), neither
   applied.** (i) *For the critics:* equilibrium mutational load is a function of U and not of s
   (Haldane 1937; Muller 1950, L ~ 1 - e^-U), so the objection is right in standard theory and the
   s-dependence of "functionally dead" is Day's model's, not biology's. (ii) *Its cost to the critics:*
   the quoted s6.4 text does not call itself a load calculation - it computes a carrier's fitness from
   its own deleterious count, (1-s)^n, and the word "load" does not occur in it - and on the panel's own
   e^-U, at A5h's corrected U = 384, carrier fitness is e^-384 ~ 1.7e-167 (post hoc, this fix pass;
   arithmetic only, 384 x log10 e = 166.8), independent of s. Adopting the objection therefore
   *strengthens* the "functionally dead" direction and removes the s = 0.001 escape A5h records
   (0.999^384 = 0.68). It bears on the model, not on the conclusion's direction. **A5h's fields are not
   touched here** and no verdict moves; the analyst scoring task decides.
3. **Independent confirmation of the 38,400 slip** (GGR-01, GGR-31, GGR-32) by a six-person panel that
   reached it on its own. One panellist says "3,800", corrected in the room to 3,840 - the audit's value.
4. **The clearest critic statement of the Bernoulli barrier so far** (GGR-18, GGR-19), relayed from a
   Reddit commenter with a master's in mathematics: a coefficient of variation going to zero as n grows,
   so by Fisher's fundamental theorem the rate of increase in mean fitness goes to zero. Branch G has had
   no such formulation from the critic side.
   **Rewritten 2026-10-13 (fix pass; review MAJOR-1, lead ruling R-1).** The harvest said the panel
   "rejects it ('that's preposterous', t=01:57:03) without a derivation, which is the weaker half of the
   exchange". That is **wrong against the critics** and is struck, with "the weaker half" and "without a
   derivation" as an evaluation of their reply. From the transcript: "that's preposterous" answers a
   *panellist's own* reconstruction of the barrier offered seconds earlier (t=01:56:41, the law of large
   numbers and "selection becomes less and less efficient"), which its author labels at once "I could be
   wrong about that but that's me trying to steal man V" - not the relayed Reddit formulation of
   GGR-18/GGR-19. The panel then answers twice, and both answers are now harvested:
   **recombination** (GGR-41, GGR-42, t=01:57:03-01:57:44: "you can get two beneficial mutations that
   occur separately and they can recombine together and then you can select for both at the same time
   and they can achieve fixation together"), and the **infinitesimal model** of quantitative genetics
   (GGR-43, GGR-44, t=02:13:47-02:14:28), introduced in terms as "the pop gen answer to go back to
   Bernoli's law if you want to know how it is that variance and fitness can be maintained even if you
   have very very ... low fitness impacts of each individual mutation". GGR-27..GGR-29 are the *second*
   point of that same answer; the harvest recorded the second and omitted the first. Neither answer is a
   derivation and neither takes up the coefficient-of-variation step in its own terms, but each names a
   standard mechanism or model. How far they meet GGR-19 is for the analyst scoring branch G; this
   record no longer prejudges it.
5. **Credit to Day, recorded** (GGR-04, and GGR-45, GGR-46 added by the fix pass under review MINOR-7):
   the panel's mathematician says the division "you did the division correctly" (GGR-04 - under rule RD
   the governing reading is the literal concession, so the credit stands, with the ironic reading
   recorded beside it, lead ruling R-4); the panellist who is harshest on the appendix paper's standard
   calls Day's own AI-peer-review exercise good and its review fair ("genuinely this was a good exercise
   and the response the review that he got was quite fair I think", GGR-45, t=01:22:28); and the panel
   records that the d = 1 choice is Day conceding the best case to the other side ("Remember how D was
   one earlier? This goes back to the whole he's trying to give conventional science the bestcase
   scenario numbers", GGR-46, t=01:51:34).
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

## Review resolution (fix pass, 2026-10-13)

Review: `research/checks/results/REVIEW-R4-VID-01-combined.md` (commit `38a1950`; combined low-stakes
tier), against harvest commit `6d090de`. Counts there: 0 BLOCKER, 1 MAJOR, 10 MINOR, 7 NOTE. Lead
rulings R-1..R-7 are in the addendum to `research/checks/briefs/VID-01-operator.md` (commit `3792a6b`),
written before this pass; they bind it and are not reopened. Every MAJOR and MINOR is answered by id
below; NOTEs are answered only where a ruling directs. **No verdict field, claim file or `QUEUE.md`
entry was touched** - everything here is a proposal for the analyst scoring task. New quotes were
appended with fresh ids (GGR-41..GGR-46); nothing was renumbered. Files written: the five harvest files,
`research/tools/harvest/verify_vid01.py` and its re-run output.

The review's integrity findings are accepted in full and needed no change: four matching sha256s, the
transcript re-deriving from the hashed captions, every quote an exact substring, the captions gate and
the negative keyword scan.

| id | severity | verdict | what changed |
|---|---|---|---|
| MAJOR-1 | MAJOR | **accepted in full** (ruling R-1) | Refresh item 4 rewritten and the GGR-19 note corrected: "without a derivation ... the weaker half of the exchange" struck; "that's preposterous" shown to answer a panellist's own steelman at t=01:56:41, not the relayed Reddit formulation. The panel's two substantive answers are now harvested as **GGR-41, GGR-42** (recombination, t=01:57:03 and t=01:57:44) and **GGR-43, GGR-44** (the infinitesimal model, "the pop gen answer to go back to Bernoli's law", t=02:13:47 and t=02:14:07). GGR-27's note now records that GGR-27..GGR-29 were the *second* point of that answer. |
| MINOR-1 | MINOR | **accepted**, and extended | GGR-08 and GGR-31 were contradicted by the cited turns and are now `panel`, each with the contradiction in its note. GGR-26, GGR-33/34, GGR-38/39, GGR-40 are now `panel` with the unnamed-speaker reasoning in the note. *Extension beyond the ids the review named* (flagged for the next reviewer): GGR-11 and GGR-27..GGR-29 rest on the same unsupported pattern - a role, a channel or who is being addressed, never a name - and are now `panel` too. GGR-10, GGR-13 and GGR-30 keep `(inferred)`: a name is spoken in the adjacent turn in each case ("what do you think, Dr. Hancock?"; "especially Grayson?"; "what Grayson is saying here"). The section preamble now states this audit. |
| MINOR-2 | MINOR | **accepted** | The `quotes-critics.md` section header said "39 of 39 PASS, plus 3 added after". It now reads 48 of 48 PASS (46 GGR quotes plus the two RH-32 lines), with the harvest-commit figure of 42 of 42 kept for the record. |
| MINOR-3 | MINOR | **accepted** | The blank line that orphaned RH-31 and RH-32 from the slips table was deleted; the two rows now render inside the table. |
| MINOR-4 | MINOR | **accepted** as the ruling frames it (R-3) | The framing "as likely to be a critic-side error as a Day-side one" is **withdrawn** as unsupported by the audit's own files. Refresh item 1 and the GGR-13 note now record three readings under rule RD - (a) pre-3.0, no conflict, matches TW-01; (b) the 3.0 body, contradicted by A4d; (c) 3.0 with Appendix D, partly right via the Bio-Cycle line in A4d's own Weaknesses - each with its source file, plus the host's 01:49:52 narration. **No winner declared; A4d untouched.** |
| MINOR-5 | MINOR | **accepted in part** (ruling R-2) | Both halves now sit in one note, in the ruling's order: the critics' point first (equilibrium load depends on U, not s; Haldane 1937, Muller 1950), then its cost to them (the quoted s6.4 text never calls itself a load calculation; on the panel's own e^-U at the corrected U = 384 carrier fitness is e^-384 ~ 1.7e-167, so the "functionally dead" direction strengthens and the s = 0.001 escape A5h records, 0.68, disappears). Recorded in refresh item 2 and the GGR-34 note. Not accepted as a verdict move: **A5h's fields are untouched.** |
| MINOR-6 | MINOR | **accepted** | The GGR-09 note now records the LLM's own stated target, verbatim at t=01:37:03 (the Haldane-1,600 framing, one substitution per 300 generations), against MITTENS 3.0's G_f = 1,322 and 252,000 generations (A4d); which of its five points reach 3.0 (4 and 5) and which do not (1-3); and the persona prompt at t=01:36:23-01:36:43. The segment table row no longer says the LLM "peer reviewed MITTENS 3.0". |
| MINOR-7 | MINOR | **accepted** | Both missed credits to Day are harvested: **GGR-45** (t=01:22:28, "genuinely this was a good exercise and the response the review that he got was quite fair I think") and **GGR-46** (t=01:51:34, "Remember how D was one earlier? This goes back to the whole he's trying to give conventional science the bestcase scenario numbers"). Refresh item 5 now lists all three credits. |
| MINOR-8 | MINOR | **accepted** (ruling R-4) | GGR-04 gets a readings line: literal concession (`dialectic`, credit to Day stands) and bathos (`rhetoric`), with the field taking the literal reading because that is the reading under which the *statement* is most defensible - under the ironic reading it asserts nothing - not because it favours a side. GGR-03, GGR-35 and GGR-39 keep `dialectic` with their devices named (diminution, hyperbole of accumulation, hyperbole) and their checkable cores identified. GGR-40 is now `secondhand, dialectic`. |
| MINOR-9 | MINOR | **accepted as written** (ruling R-6) | RH-31's dialectical-core cell and the refresh's negative-scan paragraph no longer say "credentialed". Both now say "six panellists, described in the title as scientists", and RH-31 records the description's "We're apologizing to our doctoral committees with this one" and that only Hancock's PhD is on the audit's record. This finding costs the critics and is applied for the reason the Day-side findings are. |
| MINOR-10 | MINOR | **accepted**; the scope half is ratified, not fixed (ruling R-5) | The file is ratified as in-scope (a script outside the fetch directory is what rule 4 requires; the brief's list did not anticipate it). The reproducibility half is fixed: `verify_vid01.py` now reads its default quote list from the committed `YT-AqC1ZM4icms` blockquotes and the `RH-32` row, so the count is reproducible from the repository alone, with `argv[1]` still reproducing the original 42-line run. Committed (`81c9f07`) and pushed before it ran (hard rule 5); docstring prediction 48/48. |
| NOTE-3 | NOTE | recorded (ruling R-2) | Folded into MINOR-5 above, as the ruling directs: the critics' strongest form of the objection and its cost to them in the same note, neither applied. |
| NOTE-4 | NOTE | recorded, bounded (ruling R-7) | RH-31's dialectical-core column now notes that the body contains ad hominem of the kind Day's lines are ledgered for, with two verbatim locators (t=00:00:00, t=03:47:47). Nothing more; a wider rhetoric harvest of the four hours is a separate task. |
| NOTE-6 | NOTE | **not this pass** (ruling R-7) | The unpinned `yt-dlp` (2026.8.19, `--no-deps`) is a `requirements.txt` / `HOWTO-refresh.md` §5 matter for the bookkeeping task. It stays recorded in the method paragraph above and in the harvest log. |
| NOTE-7 | NOTE | no change needed | 4:14:02 is the metadata value and is what this record, the bib row and the quotes header already say; 4:14:03 is a rounding in the brief, which this pass may not edit. |
| NOTE-1, NOTE-2, NOTE-5 | NOTE | no action | NOTE-1 (entries not in time order): ids must not be renumbered, and the review itself asks for no fix. NOTE-2: the qbg dates are not re-verifiable on this workstation; the caveat is now in the GGR-40 note. NOTE-5 (GGR-12 vs GGR-20 on whether the Bernoulli barrier is in MITTENS 3.0): settling it needs the 3.0 text, which is not on this workstation; it stays an item for the analyst. |

**Post hoc computation (fix pass).** Two runs of `research/tools/harvest/verify_vid01.py`, local,
one process, seconds (`na-workhorse` is busy with `ph2`; nothing was launched there). Output:
`research/checks/results/raw/verify_vid01-fixpass.out`. **48 of 48 PASS**, matching the docstring
prediction, and each of the 46 GGR entries' recorded `t=` equals the caption-chunk start the verifier
prints (checked by comparison, 0 mismatches). The back-compatibility path on the original `all.txt`
still returns 42 of 42. The only other arithmetic in this pass is 384 x log10 e = 166.8, i.e.
e^-384 ~ 1.7e-167, in refresh item 2.

**What this fix pass found for each side, and against the audit itself.**
- *For the critics:* their reply to the Bernoulli barrier was real and substantive (recombination; the
  infinitesimal model) and the record had erased it; their A5h modelling objection is right in standard
  theory (NOTE-3).
- *For Day:* three statements of credit from the panel are now on the record, not one; the LLM
  "peer review" that the panel endorses was of the Haldane-1,600 version, not of MITTENS 3.0; the
  d-coefficient charge has a reading under which it is simply the audit's own TW-01 figure; and the
  A5h objection, if adopted, costs the critics their own s = 0.001 escape.
- *Both / the audit's own errors:* every finding above is an error of this audit's harvest, not of
  either side - one evaluative sentence written against the critics without reading their answer
  (MAJOR-1), nine speaker attributions asserted beyond the evidence (MINOR-1, two of them contradicted
  by the very turns cited), a stale pass count (MINOR-2), a broken table (MINOR-3), an appeal to balance
  used as if it were evidence (MINOR-4), an unsourced credential claim (MINOR-9), and a verifier that
  could not be rerun from the repository (MINOR-10). The harvest's integrity held; its judgement did not.

**Apparent contradictions with existing audit verdicts (recorded, not applied).** Unchanged in
substance from the harvest, now with readings: (i) GGR-13/GGR-14 against **A4d** (`holds`, "no d term
in MITTENS 3.0") under reading (b) only; readings (a) and (c) do not contradict it. (ii) GGR-33/GGR-34
against the model behind **A5h**, though not against its direction (see item 2). Both are for the
analyst scoring task; no claim file was opened in this pass.
