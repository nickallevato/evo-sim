"""QM-03/QM-04 (EVO-78): locate Day's answer to DE-01 in the re-fetched Dembski
interview and machine-check the argmap quote as a verbatim substring.

Read-only. Operates on sources/raw/qm03-dembski-2026-10-14/dembski-interview.html
(gitignored). Prints the paragraph index of the answer under the same <p>-counting
convention used for the DE-01..DE-03 filings, and the substring test result.
"""
import html
import re
import sys
import unicodedata

PATH = "sources/raw/qm03-dembski-2026-10-14/dembski-interview.html"
QUOTE = (
    "The scaling element doesn’t apply at all, it is entirely irrelevant, "
    "because sexual reproductive capacity is the real limit on humans and other "
    "non-bacteria."
)
DE01 = "A critic could accept the logic of using experimental evolution as a benchmark"

raw = open(PATH, encoding="utf-8", errors="replace").read()
doc = raw

paras = re.findall(r"<p\b[^>]*>(.*?)</p>", doc, re.S)
texts = [unicodedata.normalize("NFKC", html.unescape(re.sub(r"<[^>]+>", "", p))).strip()
         for p in paras]

for i, t in enumerate(texts, 1):
    if DE01 in t:
        print(f"DE-01 question at <p> index {i}")
    if QUOTE in t:
        print(f"answer containing the argmap quote at <p> index {i}")
        print(f"answer full text:\n{t}")

flat = "\n".join(texts)
print(f"verbatim substring test: {QUOTE in flat}")
sys.exit(0 if QUOTE in flat else 1)
