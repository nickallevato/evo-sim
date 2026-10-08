import json,re,hashlib
D='/home/na/projects/evo-sim/docs/research/sources'
R='/home/na/projects/evo-sim/sources/raw/day'
z=open('zenodo_table.md').read(); b=open('blog_table.md').read()
hdr='| key | type | date | title | URL | version | local path | sha256 | access | branch | notes |\n|---|---|---|---|---|---|---|---|---|---|---|\n'
def sh(p): return hashlib.sha256(open(f'{R}/{p}','rb').read()).hexdigest()
extra=[
 ('V2019-02-07-gariepy-debate','video','2019-02-07','Vox Day vs JF Gariepy debate on evolution/mathematics (The Public Space)','https://youtu.be/Aaqec_0FPqA','live stream','-','-','not-fetched (URL recorded only)','A,G','Link given in blog post B2019-02-07-evolution-debate-tonight ("Here is the link to the debate"). Duration/timestamps not checked. Day: "more of a mutual exploration than a debate per se".'),
 ('T2021-11-11-gariepy-debate-transcript','blog','2021-11-11','The JFG-VD Debate (complete transcript of the 2019 debate)','https://voxday.net/2021/11/11/the-jfg-vd-debate/','-','sources/raw/day/blog-2021-11-11-the-jfg-vd-debate.html',sh('blog-2021-11-11-the-jfg-vd-debate.html'),'ok','A,G','Same file as B2021-11-11-the-jfg-vd-debate. No separate 2021 video debate was found in the harvested posts; the 2021 item is this transcript (posted ~2.75 y after the 2019-02-07 debate) plus B2021-11-14-why-i-insist-on-written-debates.'),
 ('V2019-01-30-darkstream','video','2019-01-30','Darkstream on evolution (referenced in "The Vox delusion?")','https://youtu.be/LGKg2nr9uHY','-','-','-','not-fetched','A','Link only.'),
 ('V2019-02-15-darkstream','video','2019-02-15','Darkstream, Feb 14 2019 (referenced in "Dumbing it down for the biologists")','https://youtu.be/OVRUc-uhweQ','-','-','-','not-fetched','A','Link only.'),
 ('K-PZ-1e','book','2026-01-06 (blog announcement)','PROBABILITY ZERO: The Mathematical Impossibility of Evolution by Natural Selection (1st ed., ebook)','https://www.amazon.com/dp/B0GF8RQFY4','1st edition (~76,000 words per 2nd-ed intro)','-','-','blocked (Amazon returned bot-check page, 3.8 KB, discarded)','A-H','ASIN B0GF8RQFY4 (from blog links). Price: blog 2026-05-20/26 "$0.99" Based Book Sale (ebook). Not purchased. Paywalled; book-only claims are secondhand.'),
 ('K-PZ-2e','book','2026-05-23 (blog announcement)','PROBABILITY ZERO 2nd edition (ebook updated; hardcover/paperback "next week" per post)','https://www.amazon.com/dp/B0GF8RQFY4','2nd edition (~100,000 words)','-','-','paywalled','A-H','Same ASIN as 1st ed ebook ("update your Kindle edition"). 2nd-ed introduction quoted in blog B2026-05-23-probability-zero-2nd-edition: replaces 40M bp with 410M bp; new appendices include Z23003785-era and Z19984826 papers.'),
 ('K-PZ-hc','book','2026-02-02 (blog)','PROBABILITY ZERO hardcover (English)','https://www.amazon.com/dp/3039440675/','hardcover; Castalia AG (Switzerland)','sources/raw/day/book/ndm-probability-zero.html',sh('book/ndm-probability-zero.html'),'ok (shop page); item sold out as of 2026-10-07','A-H','Identifier in URL is ISBN-10 3039440675 (inferred from Amazon dp URL, not verified; ISBN-13 not published on pages fetched). NDM Express page https://ndmexpress.com/products/probability-zero: Hardcover $29.99 USD, "Sold out".'),
 ('K-PZ-signed','book','2026-05-23 (blog)','PROBABILITY ZERO Signed Special Edition (leatherbound, Castalia Library)','https://ndmexpress.com/products/probability-zero-signed-special-edition','2nd-ed text, limited','sources/raw/day/book/ndm-probability-zero-signed-special-edition.html',sh('book/ndm-probability-zero-signed-special-edition.html'),'ok (shop page); "Sold out"','A-H','$250.00 USD.'),
 ('K-PZ-fr','book','2026-02-02 (blog)','Probabilite zero: l\'Impossibilite mathematique de l\'evolution par selection naturelle (French, Editions Alpines)','https://www.amazon.com/dp/3039440683','French hardcover','-','-','not-fetched','A-H','Identifier in URL 3039440683 (ISBN-10, inferred). German translation "nearly complete" per post 2026-02-02.'),
 ('K-TFG','book','2026-01-29 (blog)','THE FROZEN GENE: The End of Human Evolution (separate book; sequel to PZ)','https://www.amazon.com/dp/B0GJTQ44XQ','1st ed ebook; print edition planned (post 2026-04-13: "Probably in May"); 2nd ed "eventually" (post 2026-09-28)','-','-','blocked/not-fetched (Amazon bot-check on same host)','A,B,H','ASIN B0GJTQ44XQ; NDM page https://ndmexpress.com/products/the-frozen-gene (not fetched). Per blog, source of Ch.2 "Minimum Selection Coefficients Required for Speciation" (not on Zenodo) and the main-MITTENS journal rejection letter (post 2026-01-12). Price not recorded.'),
 ('K-HARDCODED','book','2025-12-27 / 2026-05-01 (blog)','HARDCODED: AI and the End of the Scientific Consensus (companion volume)','https://www.amazon.com/dp/B0GZ5MD66S','-','-','-','not-fetched','misc','Out of scope except as the venue for AI-referee experiment papers; posts B2025-12-27-hardcoded and B2026-05-01-hardcoded-2 kept.'),
]
ex='\n'.join('| '+' | '.join(str(c).replace('|','/') for c in r)+' |' for r in extra)
intro="""# Bibliography: Vox Day corpus (blog, Zenodo, book, video)

Harvest date: 2026-10-07 (pass 2, Day slice). Raw copies live in `sources/raw/day/` (gitignored; untrusted data, never executed). sha256 is of the downloaded original file (blog = the saved HTML page, which includes sidebar/comments so it can change on re-fetch).

Conventions:
- `Z<id>` Zenodo record id (suffix `-f2` = second file in the record). 39 records returned by the API query for creator "Day, Vox", plus 2 earlier versions found via the `/versions` endpoint (Z18202768, Z18517618). Text extraction: `pdftotext -layout` for PDF; regex-based XML text pull for docx/odt (superscripts rendered `^{..}`, subscripts `_{..}`; equation objects in docx may be flattened). Locators for docx are paragraph indexes in the `.txt`, not pages.
- `B<date>-<slug>` blog post; text extraction `.txt` beside each `.html`.
- Branch letters (A rate limit, B neutral theory, C aDNA, D sequence space/Wistar, E LTEE/punctuated equilibrium, F Kimura irrelevance, G Bernoulli/parallelism, H cost of selection) are PROVISIONAL: for blog rows they are keyword-count heuristics (top 3 by hits), for Zenodo rows hand-assigned from titles/abstracts. `misc` = no branch keyword hit.
- Zenodo records are CC-BY-4.0 open access; philosophy/theology records are listed but not downloaded.

## Zenodo (all co-authored "Athos, Claude"; none peer-reviewed)

"""+hdr+z+"""

## Books, videos, transcript

"""+hdr+ex+"""

## Blog posts kept (154)

"""+hdr+b+"\n"
open(f'{D}/bib-day.md','w').write(intro)
print(len(intro))
