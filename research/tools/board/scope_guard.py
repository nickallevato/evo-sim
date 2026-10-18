"""Board scope guard (B-R21 item 3; EVO-84, re-cut by the B-R28 ruling of 2026-10-18).

status.html is hand-patched prose (board/updN.py), not generated from claim front matter, so
there is no generator to change. This guard enforces "value and scope together, or neither"
(B-R21) and the B-R20/B-R21 publication hold. For every claim field whose comment carries a
scope (lint_research.SCOPE_RE):

  * value stated with no scope cue at all in the same entry -> VIOLATION. This is the hazard
    B-R21 named: "a bare `holds` on a public page is a Day-favourable claim the audit does not
    make."
  * value stated with a scope cue but not the verbatim `verdict_scope` line -> REVIEW. The
    page is hand-written prose and will paraphrase; a human checks the paraphrase against the
    ruled scope before publishing. Not an exit-1 failure (B-R28: a verbatim-substring test on
    prose reported 9 entries that do state their scope in their own words).
  * value stated, `none:` scope (B-R22 / B-R27: the scope belongs to a superseded value, or
    the reading-dependence is on a rhetoric tag and not on the value) -> nothing required;
    there is no scope to render and rendering one would be false.
  * current value `pending` or `n/a` -> no verdict to scope. Instead the hold check: an entry
    that states the id with another value of that field's vocabulary must mark it
    `superseded` / `pending` / `withdrawn` / `held`, or it publishes a value the audit has
    pulled (B-R20/B-R21: no board publication may show B internal or A2e external as current).

B-R28 also narrowed the match, which reported 22 of 22 as noise on 2026-10-17. The value
itself must sit within 120 characters of the id with no sentence break (the old test accepted
the *field name* near the id and then found the value anywhere in the entry), `pending` no
longer counts as a stated value, and a one- or two-character id must be quoted as a claim
reference *and* carry a field name between it and the value - board prose uses bare "A", "B",
"C" and "H" for reading labels and as ordinary text. Run before every board publication;
exit 1 on a VIOLATION, 0 on REVIEW lines alone.
"""
import os, re, sys, glob, html
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "research", "checks"))
import lint_research as L

VOCAB = {"internal": L.V_INT, "fidelity": L.V_FID, "external": L.V_EXT}
MARKED = re.compile(r"supersede|pending|withdraw|\bheld\b|on hold", re.I)
CUE = re.compile(r"scope|scoped|reading|conditional on|only under|under the|as worded", re.I)
FIELD = r"(?:internal|fidelity|external)"
WINDOW = 120


def states(text, cid, val):
    """True if the entry states `cid` and `val` together: the id, then the value within WINDOW
    characters of running text with no sentence break. A one- or two-character id must be
    quoted as a claim reference and must carry a field name before the value."""
    any_mid = r"[^.]{0,%d}?" % WINDOW
    field_mid = r"[^.]{0,%d}?(?<![\w-])%s(?![\w-])[^.]{0,%d}?" % (WINDOW, FIELD, WINDOW)
    if len(cid) <= 2:
        # a bare "A" / "B" / "C7" is also a reading label and ordinary prose: take it as a claim
        # reference only where it opens the entry, or where a field name stands before the value
        heads = [(r"^", any_mid), (r"(?:[\[\(,;:]\s*|\bclaim\s+|\bnode\s+)", field_mid)]
    else:
        heads = [(r"(?<![\w-])", any_mid)]
    return any(re.search(r"%s%s(?![\w-])%s(?<![\w-])%s(?![\w-])" % (lead, re.escape(cid), mid, re.escape(val)), text)
               for lead, mid in heads)


page = html.unescape(open(os.path.join(ROOT, "docs", "research", "status.html"), encoding="utf-8").read())
lis = [re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", li)).strip()
       for li in re.findall(r"<li\b.*?</li>", page, re.S)]

bad, review, checked = [], [], 0
for p in sorted(glob.glob(os.path.join(L.CLAIMS, "*.md"))):
    if os.path.basename(p).startswith("_"):
        continue
    fm, _ = L.parse(p)
    if not fm or "id" not in fm:
        continue
    cid, vs = str(fm["id"]), fm.get("verdict_scope") or {}
    for k, c in fm["_comments"].items():
        if not L.SCOPE_RE.search(c):
            continue
        val = str((fm.get("verdicts") or {}).get(k, "")).split()[0]
        scope = vs.get(k) if isinstance(vs.get(k), str) else None
        if val in L.NO_VALUE:
            # nothing to scope; the field's other values are pulled and may not be stated bare
            for other in sorted(VOCAB[k] - L.NO_VALUE):
                for text in lis:
                    if states(text, cid, other) and not MARKED.search(text):
                        bad.append(f"{cid}.{k} is {val}, so {other!r} is pulled: stated on the page "
                                   f"without 'superseded' or 'pending': {text[:100]!r}")
            continue
        if scope is None or L.NO_SCOPE_RE.match(scope):
            continue   # ruled: this value carries no scope (B-R22 / B-R27), so none is required
        want = re.sub(r"\s+", " ", scope)
        for text in lis:
            if not states(text, cid, val):
                continue
            checked += 1
            if want in text:
                continue
            (review if CUE.search(text) else bad).append(
                f"{cid}.{k}={val}: {'paraphrased, not the ruled scope line' if CUE.search(text) else 'stated bare, no scope at all'}: {text[:100]!r}")

print(f"scope guard: {checked} page entries state a scoped claim field with its value; "
      f"{len(bad)} violations, {len(review)} to review by hand")
for r in review:
    print("REVIEW", r)
for b in bad:
    print("VIOLATION", b)
sys.exit(1 if bad else 0)
