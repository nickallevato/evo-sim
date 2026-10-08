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
