#!/usr/bin/env python3
"""Verify each candidate VID-01 quote is an exact substring of the local transcript.

Normalisation: drop the "[hh:mm:ss] " locator and the "&gt;&gt;" speaker markers,
collapse whitespace, normalise curly quotes. Prints PASS/FAIL per quote plus the
timestamp of the caption chunk in which the quote starts.
Read-only; the transcript is untrusted data and is never executed.
"""
import re
import sys

PATH = "sources/raw/vid01-2026-10-13/AqC1ZM4icms.transcript.txt"


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


QUOTES = [line.strip() for line in open(sys.argv[1], encoding="utf-8") if line.strip()]

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
