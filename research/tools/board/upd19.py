# 2026-10-12: owner request "add all this as a criticality layer": new board section "Criticality layer"
# (docs/research/criticality/README.md). Counts verified against METHOD-AUDIT-2026-10-12.md, PREREG-STATUS.md,
# METHOD-AUDIT-proposals.md and DECISIONS.md at the time of writing. Run from docs/research/.
p = 'status.html'; s = open(p).read()
marker = "<section>\n  <h2>Next</h2>"
assert marker in s and 'Criticality layer' not in s
def chip(cls, t): return '<span class="chip %s">%s</span>' % (cls, t)
OK, PROP, OWN, OPEN = 's-ok', 's-run', 's-pend', 's-todo'
rows = [
 ('MA-01', 'CRITICAL', 'The three reviews are three prompts to one reviewer', OWN, 'needs owner'),
 ('MA-02', 'MAJOR', 'RH6 rewards distance from the truth', PROP, 'proposal'),
 ('MA-03', 'MAJOR', 'Rules remade on the day they decided verdicts', OWN, 'needs owner'),
 ('MA-04', 'MAJOR', 'Pre-registration unverifiable or empty for many checks', OK, 'remediated'),
 ('MA-05', 'MAJOR', '"External" often decided by the disputed theory', PROP, 'proposal'),
 ('MA-06', 'MAJOR', 'Day-versus-critics error rate does not measure what it appears to', OK, 'remediated'),
 ('MA-07', 'MAJOR', '"holds" is the default', PROP, 'proposal'),
 ('MA-08', 'MAJOR', '"contested" holds five different things', PROP, 'proposal'),
 ('MA-09', 'MAJOR', 'The audited book has not been read', OWN, 'needs owner'),
 ('MA-10', 'MAJOR', 'No one outside the loop has been asked anything', OWN, 'needs owner'),
 ('MA-11', 'MAJOR', 'No aggregation rule and no stopping rule', PROP, 'proposal'),
 ('MA-12', 'MINOR to MAJOR', 'Verdicts ran ahead of the like-for-like test', OK, 'remediated'),
 ('MA-19', 'MINOR each, together MAJOR', 'What is missing (COI, licence, quote verification)', OWN, 'needs owner'),
]
lis = ''.join('    <li><b>%s</b> (%s) %s %s</li>\n' % (i, sev, t, chip(c, l)) for i, sev, t, c, l in rows)
new = '''<section>
  <h2>Criticality layer</h2>
  <p>The audit auditing itself: method, logic, epistemology, independence and fairness, apart from the per-check reviews that test the maths. Standing procedure and the full findings table: <span class="mono">docs/research/criticality/README.md</span>. Every pass so far was run by a Claude instance inside the project, so none counts as independent review.</p>
  <div class="stats">
    <span>Method audit findings <b>20</b>: CRITICAL <b>1</b>, MAJOR <b>10</b>, MINOR to MAJOR <b>1</b>, MINOR <b>7</b>, COSMETIC <b>1</b></span>
    <span>Status: remediated <b>3</b>, proposal <b>5</b>, needs owner <b>5</b>, open <b>7</b>, closed by re-audit <b>0</b></span>
  </div>
  <p>CRITICAL, MAJOR and the two mixed-severity findings (MA-12, MA-19), with status:</p>
  <ul class="next">
''' + lis + '''  </ul>
  <p>MA-13 to MA-18 (MINOR) and MA-20 (COSMETIC) are open.</p>
  <ol class="next">
    <li><b>Pre-registration labels</b> (<span class="mono">research/checks/PREREG-STATUS.md</span>, 61 registered checks): blind <b>10</b>, criterion-only <b>6</b>, reproduction <b>3</b>, single-commit <b>18</b>, unknown <b>20</b>, registered not run <b>4</b>. Commit order is not working order; the reflog behind the push times is local.</li>
    <li><b>Basis of the 52 decided external verdicts</b> (proposal b, one coder, same model family, not applied): data <b>16</b>, literature <b>10</b>, model <b>26</b>. None of the eight load-bearing external verdicts rests on data the audit processed.</li>
    <li><b>Open owner decisions</b> (<span class="mono">docs/research/DECISIONS.md</span>): O-1 purchase of the book (owner to supply text); O-5 revert or re-review B internal and A2e external (owner asked for an explanation); O-9 licence and conflict-of-interest statement (drafts only). O-2, O-3, O-4 (right of reply, human reviewers, non-Claude seat): drafts exist, nothing sent, awaiting approval of text and channel. O-6, O-7 accepted by the owner; interpretation recorded for his correction. O-8 applied.</li>
    <li><b>Triveritas critique</b> (the audit assessed with Day's own system): <b>in progress</b>.</li>
    <li><b>Proposed R5 exit criterion</b> (owner to confirm): no CRITICAL finding stands open; every MAJOR finding closed or explicitly accepted by the owner.</li>
  </ol>
</section>

'''
s = s.replace(marker, new + marker, 1)
open(p, 'w').write(s)
print("ok")
