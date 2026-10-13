# Harvest log: primary literature (R1 pass 2), 2026-10-07

Rules followed: legal open-access copies only; ~1 s between requests per host; no Wayback snapshots created (one existing capture was *read*); nobody contacted; bot challenges (Cloudflare) not circumvented; downloaded files never executed (text extracted with `pdftotext`, `python3 -I`, `openpyxl` in `research/.venv`, which had `openpyxl` and `pypdf` added).

## Obtained (full text, local under `sources/raw/sources/`)
- Europe PMC `fullTextXML` (OA subset): Bergeron 2023, Yoo 2025, Kong 2012, Tenaillon 2016, Good 2017 (author manuscript), Mathieson 2015, Fu 2015, Mallick 2024, Scally 2012.
- arXiv: Chalub 2022 (2208.00148v1).
- Publisher OA PDF: Zeng 2021 (nature.com), CSAC 2005 (nature.com served the PDF without login).
- Institutional repositories: Langergraber 2012 (libra.unine.ch bitstream; PNAS PDF), Balloux & Lehmann 2012 (serval/iris.unil.ch).
- Nunney 2003: live `sekj.org` PDF links 404; read from an **existing** Internet Archive capture of the publisher's free PDF (timestamp 20250719055704). No snapshot was created.
- Yoo 2025 supplements from `static-content.springer.com/esm/...`: MOESM1 (SI, 174 pp.), MOESM2 (reporting summary), MOESM3 (peer-review file), MOESM4 (supplementary tables xlsx). The Europe PMC `supplementaryFiles` zip endpoint truncated twice (stream stalls at ~37-40 MB); Springer's static files worked.
- Wistar 1967 (1985 Liss reprint): full OCR'd scan at dynamics.org (Altenberg library). **Rights unverified**; archive.org only has a borrow-only record (`mathematicalchal0000unse_p3g3`). Treated as local-analysis copy; do not redistribute.

## Abstract-only (paywalled or full text not retrievable)
- Barrick 2009 (Nature paywalled; abstract via Europe PMC). A HAL/ISTEX link led to an institutional-login page and was not used.
- Axe 2004 (JMB paywalled), Kimura 1968 (Nature preview, one sentence), Keefe & Szostak 2001 (PubMed abstract; HHMI manuscript PMC4476321 exists but Europe PMC XML returned 500).
- Maruyama 1970 (no abstract), Cannings 1974, Maruyama 1974, Frankham 1995, Haldane 1957: record only.

## OA exists but automated download blocked (not bypassed)
PMC article pages and PDFs (`pmc.ncbi.nlm.nih.gov`, `europepmc.org/backend/ptpmcrender`) now return a "Just a moment..." JavaScript challenge; Europe PMC `fullTextXML` returns HTTP 500 for papers not in its OA text subset; `academic.oup.com`, `pnas.org`, `ias.ac.in`, an instructor-hosted UBC copy (403) were also refused. Affected: **Kimura 1962 (PMC1210364), Kimura & Ohta 1969 (PMC1212239), Keightley 2012 (PMC3276617), Haak 2015 (PMC5048219), Prado-Martinez 2013 (PMC3822165), Taylor 2001 (PMC58511)**. Abstracts for the last four came from the Europe PMC search API. These six are the best candidates for a **manual download by the user** from a normal browser (PMC pages are public).

## Not found
- **"Chalub 2012"**: no such paper found. arXiv author listing for Chalub returned Chalub & Souza 2009 (TPB 76:268, "From discrete to continuous evolution models"), 2009 (CMS 7:489), 2014 (J Math Biol 68:1089, frequency-dependent Wright-Fisher), 2017 (J Math Biol 75:1735), and arXiv "Fixation in large populations: a continuous view of a discrete problem". None downloaded; none appears to treat substitution rate with mutation.
- **Kimura 1983 p.44 quote** ("2Nv new, distinct mutants"): Google Books API returned a quota-exhausted error; no snippet available. Web searches found only textbook paraphrases.
- **Good 2017 bioRxiv preprint**: Europe PMC preprint search returned nothing; used the PMC author manuscript.
- **"187 Mb" / "410 Mb" in Yoo 2025**: text search of main text, SI (MOESM1), peer-review file (MOESM3) for `187`, `410` found only unrelated hits (Cell 187 volume number). Table sums computed from MOESM4 (see quotes file) show no match. SI figures/images were not OCR'd, so a figure-embedded number is not excluded.
- **Wright's Ne = (4N-2)/(Vk+2) original**, **Kimura's reply to Haldane**, **ReMine 2005**, **Schrago 2014**: not searched in depth or not found; citation details for these in the bibliography are from memory and labelled unverified.
- **Supplementary information** for Mathieson 2015, Good 2017, Tenaillon 2016, Bergeron 2023 (human mu), CSAC 2005: not retrieved. Mathieson's LCT/SLC24A5 s values are therefore still unverified (they are not in the main text).
- Mainstream counter-estimate for branch D: Taylor 2001 and Keefe & Szostak 2001 are only abstract-level here; neither abstract states a per-sequence functional fraction directly comparable to Axe's 1e-77.

## Extraction notes
- Two-column PDFs were re-extracted without `-layout` to restore reading order before quoting.
- All 75 quotes in `quotes-literature.md` were machine-verified as substrings of the normalised extracted text; known extraction artefacts are noted per quote (lost superscripts in the Wistar OCR, "~" rendered as "," in CSAC, a control character replacing the s-hat symbol in Zeng).
- One discrepancy in a source recorded, not resolved: Yoo SI Note III text "(0.15-0.16%)" vs Table III.14 value 0.0146 for human-chimp autosome SNV divergence.

## Refresh 2026-10-09b (foundational and tool literature, second pass)
Run 2026-10-09 evening. Rules as above: legal open copies only, 1 s spacing, nothing created on third-party services, no bypass. Raw files `sources/raw/refresh-2026-10-09b/lit/` (gitignored).

### Method
1. Europe PMC REST search (`/europepmc/webservices/rest/search?query=TITLE:"..."`) to resolve titles to PMCIDs and DOIs, then `resultType=core` to check journal, volume, pages.
2. Full text: Europe PMC `fullTextXML` works only for OA-subset articles (Lynch 2016, Baumdicker 2022, Kong 2012); the other PMCIDs returned HTTP 500 (150-byte body; deleted, not kept). NCBI `efetch.fcgi?db=pmc&id=NNN&retmode=xml` returned the full text only for NIH author manuscripts (Messer & Petrov 2013; SLiM 4) and metadata plus abstract for the rest.
3. arXiv: the arXiv API search by title failed for most titles; `all:Durrett AND all:regulatory AND all:waiting` found math/0702883, downloaded as PDF and converted with `pdftotext`.
4. Tool metadata: GitHub REST API repo descriptions (SLiM, msprime, fwdpy11).
5. Every quote machine-checked as a substring of the extracted text.

### Obtained
Full text: Durrett & Schmidt 2007 (arXiv), Messer & Petrov 2013, Lynch 2016, SLiM 4 (Haller & Messer 2023), msprime 1.0 (Baumdicker 2022). Abstract only: Durrett & Schmidt 2008, Behe & Snoke 2004, Lynch 2010, Hermisson & Pennings 2005, Desai & Fisher 2007, Lesecque 2012, Moorjani 2016, Razeto-Barry 2012. Record only: Jonsson 2017, Charlesworth 2009 and 2013, Kondrashov 1995, Hossjer et al 2021, Kimura & Maruyama 1969.

### Not obtained
- bioRxiv full text (Moorjani preprint): HTTP 429.
- fwdpy11 documentation: `fwdpy11.readthedocs.io` "Project not found"; only the GitHub description was read. (Try `molpopgen.github.io/fwdpy11` next time.)
- Hermisson & Pennings 2005, Behe & Snoke 2004, Durrett & Schmidt 2008, Lynch 2010, Desai & Fisher 2007: full text exists on PMC but is behind the PMC bot challenge; Europe PMC returned 500. A user-downloaded copy (as for Kimura 1962) would let these be quoted beyond the abstract.
- Haldane 1957, Kimura 1983, Felsenstein 1971/1972, Ewens 1970: no OA text found (see PA-01, PA-07, PA-08).
- Muller's ratchet: no primary source added (searches by title returned no open full text; candidates for a later pass are Haigh 1978 and Lynch & Gabriel 1990, citations not verified here).

### Findings that affect existing ledgers
- D15: the Durrett & Schmidt 2007 abstract gives 100,000 years (6-letter word) and 60,000 years (7/8 match) per their model; their 2008 abstract gives >100 million years for a particular two-step human regulatory change. Both are Day-side-usable and critic-side-usable depending on the question; D15 should cite them as baselines, not verdicts.
- H10: Lynch 2016 supports the direction of Day's "selection ended" claim; Lesecque 2012 supports the critics' point that a large deleterious load per genome is tolerable under relative-fitness selection. Neither addresses the "3x drift-fixed" figure.

## Refresh 2026-10-10b
Europe PMC REST (search + abstracts + `fullTextXML` for OA-subset papers), Crossref, NCBI efetch (stub only for author manuscripts), plain curl for the UCSC/CGL index and GitHub README. 8 OA full texts saved (Gayà-Vidal, Boyko, Galtier, Moutinho, Keightley 2005, Enard, Kim 2017, Tataru 2017), 12 abstracts, local Yoo SI re-read (MOESM1 lines 1456-1478). Failures: Uricchio 2019 and Hernandez 2011 return a 150-byte stub from `fullTextXML` (deleted); ENA portal API returned HTTP 500; arXiv API and Project Euclid returned empty. 31 quotes machine-checked, 0 failures. Pitfall: zsh treats `echo ==X` as an error (already in HOWTO).

## Refresh 2026-10-10c (A2e-alpha fix pass, critic review C2)
One file, plain curl (HTTP 200, `application/vnd.ms-excel`, 8,986,624 bytes) from the publisher's open-access ESM link for Gayà-Vidal & Albà 2014, BMC Genomics 15:599 (CC BY 4.0; the PMC XML lists it as `12864_2014_6322_MOESM1_ESM.xls`, "Additional file 1 ... (XLS 9 MB)"): `https://static-content.springer.com/esm/art%3A10.1186%2F1471-2164-15-599/MediaObjects/12864_2014_6322_MOESM1_ESM.xls`. Saved to a new dir `sources/raw/a2e-alpha-gv-supp-2026-10-10/` (gitignored). sha256 `7b6cb765ad5f3e58a464def105a439c795f74341720c9d1fce53619ccf46c3b9`. Read as data with xlrd 2.0.1 (installed outside the repo; nothing in the file executed). 17 sheets (README, S1-S15). Validated: reproduces GV Table 1 and the Methods totals (ΣDn 18,936, ΣDs 34,241) exactly; Table 1's accelerated-set N at DAF ≥ 15% prints "15" where the sheets give 155 (source typo). Used by `research/checks/a2e_alpha_gv_acc.py` (post hoc). No quotes taken from it (numeric tables only).

## Refresh 2026-10-12
Plain curl, two fetches into `sources/raw/csac2005-nature-2026-10-12/` and one into `sources/raw/blosum62-ncbi-2026-10-12/`. (1) Nature article page for CSAC 2005, listing the supplementary files (MOESM1-14; S23 = MOESM6). (2) `..._MOESM6_ESM.xls` (HTTP 200, CFB/Excel 97, 3.57 MB, last saved 2005-07-14): sheet title "Human-chimpanzee orthologs"; extracted by `strings` + regex (no xlrd installed; file never executed) 13,454 unique `NM_` RefSeq ids, 13,454 occurrences, matching the paper's 13,454. Columns visible in the strings: HGNC symbol, NM_ accession (unversioned), 2004-era description. Whether chimp-side ids are also present was not parsed (strings only). (3) NCBI BLOSUM62 for the L1c pre-run check. Failures: none. Not used: shadow libraries.

**Refresh 2026-10-12c-lit (FMnull variance components).** Plain `curl` to Europe PMC (`/search?query=DOI:...` to find PMCIDs; `/{PMCID}/fullTextXML`), each into its own directory under `sources/raw/refresh-2026-10-12c-lit/` (gitignored). Obtained full text (XML, converted to text outside the download dir with `research/.venv/bin/python -I`): Smith2018 (238,907 B), Phung2016 (216,446 B), DuretArndt2008 (256,178 B), McVicker2009 (200,187 B), Hobolth2007 (108,140 B), plus MasseyKoren2022 (65,272 B; replication-timing T2T profiles, found while looking for the lifted-map question). Not obtained: Hodgkinson & Eyre-Walker 2011 (Nat Rev Genet, not open; abstract from the Europe PMC record only); Hwang & Green 2004 (PNAS: pnas.org gives a Cloudflare "Just a moment" 403, Europe PMC fullTextXML gives HTTP 500; abstract from the Europe PMC record only; no bypass attempted). 38 quotes machine-checked as substrings (0 failures). Pitfall: wide-context regex `.{0,N}` in grep on a one-line text file hangs (killed); use a Python context finder. Extraction artefacts: figure legends lose superscripts (McVicker Figure S6 "212 and 222 bp" = 2^12 and 2^22). Numbers living only in figures or tables (Smith 100-kb CV, McVicker B distribution and Fig 3 ratios, Hobolth Table 2 tract lengths) were not recorded.

**Refresh 2026-10-12d-lit (L1c pre-run amendments).** Plain `curl` into the new directory `sources/raw/gencode-v35-refseq-2026-10-12/` (gitignored): `gencode.v35.metadata.RefSeq.gz` from the EBI GENCODE FTP (HTTP 200, 788,122 B, sha256 `02c7a3e7...9edb`; read with `zcat` and `research/.venv/bin/python -I` only). Read, not stored: the PAL2NAL page (bork.embl.de/pal2nal) and a mirror of the Gblocks documentation (home.cc.umanitoba.ca/~psgendb/doc/Castresana/Gblocks_documentation.html), to check two from-memory statements of the L1c pre-run review. Failures: the two original Gblocks hosts (no answer), NCBI BLAST help (browser check). Correction to the 2026-10-12 entry above: the `strings` + regex extraction of S23 produced 1,272 accessions with one digit too many (the following string's length byte, where it is an ASCII digit); the count 13,454 was right, the ids were not. A header-anchored parse of the .xls bytes gives 13,454 six-digit accessions, 13,386 with a symbol. The held list is left as fetched-derived and is not used.

## Criticality pass iii (AMSTAR 2 and ROBIS instruments), 2026-10-12
Fetched about 23:14 UTC (17:14 -06:00) with plain `curl -sS -L --max-time 60`, serial, 1 s spacing, seven requests, each into its own new directory under `sources/raw/crit3-amstar-robis-2026-10-12/` (gitignored). Nothing posted, archived or sent; no login; no bot challenge solved. Purpose: the two appraisal instruments applied to this audit in `docs/research/criticality/amstar2-robis-2026-10-12.md`. Bib rows: `bib-literature.md`, section "Criticality pass iii"; quotes: `quotes-literature.md`, same section name.

| Target | URL | Result |
|---|---|---|
| AMSTAR 2 paper, Europe PMC | `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5833365/fullTextXML` | 200, `application/xml`, 110,773 B, sha256 `a38ebd06...272e1` |
| AMSTAR 2 paper, publisher page | `https://www.bmj.com/content/358/bmj.j4008` | **403**, 5,411 B "Just a moment..." challenge page. Not bypassed; stub and its directory deleted. The Europe PMC XML is the same article |
| AMSTAR 2 checklist | `https://amstar.ca/docs/AMSTAR-2.pdf` | 200, PDF 1.5, 4 pp., 265,991 B, sha256 `318ba413...1f05` |
| AMSTAR 2 guidance | `https://amstar.ca/docs/AMSTAR%202-Guidance-document.pdf` | 200, PDF 1.5, 8 pp., 1,652,308 B, sha256 `d08d0bb4...f6f5` |
| ROBIS paper, Europe PMC | `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4687950/fullTextXML` | 200, `application/xml`, 78,704 B, sha256 `18be2acc...c1b9` |
| ROBIS tool (form) | `https://www.bristol.ac.uk/media-library/sites/social-community-medicine/robis/ROBIS%201.2%20Clean.pdf` | 200, PDF 1.5, 3 pp., 241,004 B, sha256 `6052c8cd...65a0` |
| ROBIS guidance | `https://www.bristol.ac.uk/media-library/sites/social-community-medicine/robis/robisguidancedocument.pdf` | 200, PDF 1.5, 39 pp., 713,379 B, sha256 `d6990091...c365` |

Extraction (files read as data, never executed; scripts kept in the session scratch directory, outside the download directory): `pdftotext -layout` and plain `pdftotext` for the PDFs; a 12-line tag stripper run as `research/.venv/bin/python -I` for the XML. Text files are in `txt/` beside the fetch directories. 77 quotes machine-checked as substrings after whitespace and curly-quote normalisation, 0 misses.

Not fetched or not read: the BMJ web appendices (the paper's "Supplementary appendix 1" is its guidance; the amstar.ca guidance PDF was used and was not compared with it); the ROBIS publisher page; the worked examples in the ROBIS guidance (read only as far as the rating rules); PRISMA 2020 (the flow in the pass is "PRISMA-style" as a layout only, and no PRISMA wording is relied on). No item or signalling-question wording in the pass is from memory.

## Criticality pass iv (severe testing: Mayo's texts), 2026-10-12
Fetched 23:38 to 23:45 UTC (17:38 -06:00) with plain `curl -sS -L --max-time 60` (90 for the two PDFs), serial, each kept file in its own new directory under `sources/raw/crit4-severe-testing-2026-10-12/` (gitignored). Nothing posted, archived or sent; no login; no bot challenge met or solved; TLS verification left on. Purpose: the severity requirement applied in `docs/research/criticality/severe-testing-2026-10-12.md`. Bib rows: `bib-literature.md`, section "Criticality pass iv"; quotes: `quotes-literature.md`, same section name.

| Target | URL | Result |
|---|---|---|
| Mayo & Cox 2006, arXiv | `https://arxiv.org/pdf/math/0610846` | 200, PDF 1.4, 22 pp., 252,964 B, sha256 `e8389c2f...a3a4` |
| Mayo & Spanos 2006, author's old site | `https://www.phil.vt.edu/dmayo/personal_website/2006Mayo_Spanos_severity.pdf` | **curl error 60** (certificate does not match the host). Not overridden. Over `http://` the same path returns the department's HTML home page (200, 122,957 B), not the paper. Stubs and directories deleted |
| Mayo & Spanos 2011, author's old site | `https://www.phil.vt.edu/dmayo/personal_website/Error_Statistics_2011.pdf` | **curl error 60**, as above. Not retried over http |
| Mayo 2018 excerpt, guessed URL | `https://errorstatistics.com/2019/03/28/severity-strong-vs-weak-excursion-1-continues/` | **404** (104,145 B error page). Deleted. The right date was found through the blog's own search |
| Mayo & Spanos 2006, guessed upload path | `https://errorstatistics.files.wordpress.com/2012/08/2006mayo_spanos_severity.pdf` | **404**. Deleted |
| Europe PMC search for open Mayo papers | `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=AUTH:"Mayo DG" AND (severity OR "severe testing" OR significance)&format=json` | 200, JSON 6,792 B. Read for PMCIDs, then deleted (found PMC9096069 and PMC9300112; only the first was fetched) |
| Blog search | `https://errorstatistics.com/?s=severity+strong+vs+weak` | 200, HTML 152,594 B. Read for post URLs, then deleted |
| Mayo & Hand 2022, Europe PMC | `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9096069/fullTextXML` | 200, XML, 185,664 B, sha256 `24cb0059...8cf0` |
| Mayo 2018 excerpt (blog, strong vs weak) | `https://errorstatistics.com/2019/10/10/severity-strong-vs-weak-excursion-1-continues/` | 200, HTML, 179,741 B, sha256 `da8d10b8...f867` |
| Mayo 2018 notes (blog, mementos) | `https://errorstatistics.com/2018/10/16/tour-guide-mementos-excursion-1-tour-i-of-how-to-get-beyond-the-statistics-wars/` | 200, HTML, 184,358 B, sha256 `bc118ed2...783d` |
| Author's publications page | `https://errorstatistics.com/mayo-publications/` | 200, HTML, 146,601 B, sha256 `4b276253...b085`. Read for PDF links |
| Mayo & Spanos 2006, author-posted | `https://errorstatistics.com/wp-content/uploads/2016/03/2006mayo_spanos_severe_testing2.pdf` | 200, PDF 1.4, 336,595 B, sha256 `2e7681ae...0b71` |
| Mayo & Spanos 2011, author-posted | `https://errorstatistics.com/wp-content/uploads/2015/11/error_statistics_2011.pdf` | 200, PDF 1.5, 523,799 B, sha256 `6930621e...e6d2` |

Extraction (files read as data, never executed; scripts kept in the session scratch directory, outside the download directory, run as `research/.venv/bin/python -I`): `pdftotext -layout` for the three PDFs; a tag stripper for the XML and the two blog pages. Text files are in `txt/` beside the fetch directories. 27 quotes machine-checked as substrings after whitespace, curly-quote and ligature normalisation, 0 misses (the checker re-reads the quotes from `quotes-literature.md`, not from the extraction step).

Not fetched or not read: Mayo 2018 (the book; only the author's two posts of notes and an excerpt); Mayo 1996, *Error and the Growth of Experimental Knowledge*; Mayo 2008 on double counting and Mayo 1991 on novel evidence (both listed on the publications page, not fetched); the publisher pages for the 2006 and 2011 texts; Popper 1959 and any Bayesian primary text (the pass's remarks on Popper and on Bayesian confirmation beyond the quoted Mayo passages are from memory and are marked so there); Lakens 2019 on pre-registration and severity (from memory, marked). PMC9300112 (Mayo 2022, Conserv Biol) was listed by the search and not fetched.
