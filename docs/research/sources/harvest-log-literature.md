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
