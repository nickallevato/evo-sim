"""Board scope guard (B-R21 item 3; EVO-84).

status.html is hand-patched prose (board/updN.py), not generated from claim front matter, so
there is no generator to change. This guard enforces "value and scope together, or neither":
for every claim field that carries a scope (comment matches lint_research.SCOPE_RE), each
<li> on the page that names the claim id as a whole word AND states that field's value must
also contain the field's verdict_scope text. A scoped field with no verdict_scope entry
cannot appear at all. Exit 1 on any violation. Run before every board publication.
"""
import os, re, sys, glob, html
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "research", "checks"))
import lint_research as L

page = html.unescape(open(os.path.join(ROOT, "docs", "research", "status.html"), encoding="utf-8").read())
lis = re.findall(r"<li\b.*?</li>", page, re.S)
bad, checked = [], 0
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
        for li in lis:
            text = re.sub(r"<[^>]+>", " ", li)
            # the id, then (within 160 chars, same entry) the field name or the value
            m = re.search(r"(?<![\w-])%s(?![\w-])[^.]{0,160}?(?<![\w-])(%s|%s)(?![\w-])" % (re.escape(cid), re.escape(k), re.escape(val)), text)
            if not m or not re.search(r"(?<![\w-])%s(?![\w-])" % re.escape(val), text):
                continue
            checked += 1
            scope = vs.get(k)
            if not scope or re.sub(r"\s+", " ", scope) not in re.sub(r"\s+", " ", text):
                bad.append(f"{cid}.{k}={val}: stated on the page without its scope: {text.strip()[:90]!r}")
print(f"scope guard: {checked} page entries name a scoped claim field with its value; {len(bad)} without the scope")
for b in bad:
    print("VIOLATION", b)
sys.exit(1 if bad else 0)
