#!/usr/bin/env python3
"""Verify each VID-01 quote is an exact substring of the local transcript.

Normalisation: drop the "[hh:mm:ss] " locator and the "&gt;&gt;" speaker markers,
collapse whitespace, normalise curly quotes. Prints PASS/FAIL per quote plus the
timestamp of the caption chunk in which the quote starts.
Read-only; the transcript is untrusted data and is never executed.

Post hoc (fix pass 2026-10-13; review MINOR-10, lead ruling R-5). The original run
read its quote list from `sources/raw/vid01-2026-10-13/all.txt`, inside the
gitignored fetch directory, so the pass count could not be reproduced from the
repository. The default list is now read from the committed files of record:
every blockquote in the `YT-AqC1ZM4icms` section of `quotes-critics.md` (the GGR
quotes) plus the quoted strings in the `RH-32` row of `ledgers/slips.md`. Only the
transcript itself still comes from the fetch directory, which is the point of the
check. A path may still be passed as argv[1] to verify an arbitrary list (this
reproduces the original 42-line run from `all.txt` byte for byte).

Expected at the fix-pass commit: 48 of 48 PASS (46 GGR quotes, GGR-01..GGR-46,
plus the two RH-32 lines). The original harvest commit 6d090de gave 42 of 42.
"""
import re
import sys

PATH = "sources/raw/vid01-2026-10-13/AqC1ZM4icms.transcript.txt"
QUOTES_MD = "docs/research/sources/quotes-critics.md"
SECTION = "## YT-AqC1ZM4icms"
SLIPS_MD = "docs/research/ledgers/slips.md"
SLIP_ROWS = ("RH-32",)


def norm(s):
    s = s.replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("&gt;&gt;", " ").replace(">>", " ")
    return re.sub(r"\s+", " ", s).strip()


def load():
    stamps, chunks = [], []
    for line in open(PATH, encoding="utf-8", errors="replace"):
        m = re.match(r"^\[(\d\d:\d\d:\d\d)\] (.*)$", line.rstrip("\n"))
        if not m:
            continue
        stamps.append(m.group(1))
        chunks.append(norm(m.group(2)))
    # character offset of each chunk inside the joined text
    joined, offsets, pos = [], [], 0
    for c in chunks:
        offsets.append(pos)
        joined.append(c)
        pos += len(c) + 1
    return " ".join(joined), stamps, offsets


def from_quotes_md(path=QUOTES_MD, heading=SECTION):
    """Blockquote lines of one section of a quotes file, outer quotes stripped."""
    out, inside = [], False
    for line in open(path, encoding="utf-8"):
        if line.startswith("## "):
            inside = line.startswith(heading)
            continue
        if not inside:
            continue
        m = re.match(r"\s*> (.*)$", line.rstrip("\n"))
        if m:
            out.append(m.group(1).strip().strip('"'))
    return out


def from_slips_md(path=SLIPS_MD, rows=SLIP_ROWS):
    """Quoted strings in the quote cell (3rd column) of the named slip rows."""
    out = []
    for line in open(path, encoding="utf-8"):
        for rid in rows:
            if line.startswith("| " + rid + " |"):
                out += re.findall(r'"([^"]+)"', line.split("|")[3])
    return out


if len(sys.argv) > 1:
    QUOTES = [line.strip() for line in open(sys.argv[1], encoding="utf-8") if line.strip()]
else:
    QUOTES = from_quotes_md() + from_slips_md()

text, stamps, offsets = load()
bad = 0
for q in QUOTES:
    nq = norm(q)
    i = text.find(nq)
    if i < 0:
        bad += 1
        print("FAIL", q[:70])
        continue
    k = max(j for j, off in enumerate(offsets) if off <= i)
    print("PASS", stamps[k], "|", q[:70])
print("---", len(QUOTES) - bad, "of", len(QUOTES), "verified")
sys.exit(1 if bad else 0)
