# 2026-10-13: board patch after the bookkeeping pass BK-01. Adds Q93close and B2f (integrated 2026-10-13 after upd21 was written;
# defeaters d470-d475) and brings counts to the files of record: lint_research.py (verdicts, claims), argmap_check.py
# (defeaters 468, lineage 246 nodes), ROADMAP.md (parsed at run time), claim files (reading-dependent fields: 8 claims,
# 12 verdict fields, plus 3 RH tags). No verdict value moves. The claim count stays 233 (234 files include _TEMPLATE.md).
# Run from docs/research/. Patches status.html in place; each step asserts its anchor so it cannot apply twice.
import re, collections
p = 'status.html'; s = open(p).read()
assert 'upd22' not in s and 'upd21 applied' in s

def sub1(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:70])
    s = s.replace(old, new, 1)

# ---- headline counts
sub1('<span><b>462</b> typed objections</span><span><b>243</b> dated argument versions</span>',
     '<span><b>468</b> typed objections</span><span><b>246</b> dated argument versions</span>')
sub1('standard forms, 419 objections typed undermining / undercutting / rebutting, a genealogy of 232 dated versions since 1966',
     'standard forms, 468 objections typed undermining / undercutting / rebutting, a genealogy of 246 dated versions since 1966')
sub1('<b>131</b> holds · <b>19</b> non-sequitur · <b>2</b> arithmetic error · <b>52</b> pending · <b>10</b> reading-dependent verdicts (6 claims carry a reading-dependent verdict field, 3 more a reading-dependent RH tag; HANDOFF)',
     '<b>132</b> holds · <b>19</b> non-sequitur · <b>2</b> arithmetic error · <b>51</b> pending · <b>15</b> reading-dependent verdicts (8 claims carry a reading-dependent verdict field, 12 fields in all, 3 more claims a reading-dependent RH tag; counted from the claim files)')
sub1('<b>115</b> contested · <b>18</b> contradicted · <b>6</b> untestable · <b>48</b> pending',
     '<b>116</b> contested · <b>18</b> contradicted · <b>6</b> untestable · <b>47</b> pending')

# ---- Q93close and B2f, two more results lines
i = s.index('<li><b>L5</b> (0e6da82)'); j = s.index('</li>\n', i) + 6
add = '''    <li><b>Q93close</b> (0ee6292; reviewed #81, fix-passed df9c6c6): the "remotely close" test on Day's "In any population over 10,000, neutral substitution will not fixate at all", 25 readings. Tag reading-dependent, value dialectic. TRUE 4, CLOSE 2, OFF-10x 6, OFF 13 (a row count, not a vote); true on the 7,000-year window his next sentence invokes, close (2.0x) on 10,000 as N<sub>e</sub> with Hard Limits' own window, false with no window. No verdict moves; B2b gets a Readings table.</li>
    <li><b>B2f</b> (4213c5e, criterion-only label; reviewed #82, combined, fix-passed de3c1a2): the "closed form" F(T) = exp(-pi^2 N<sub>e</sub>/T) added to Zenodo 22903977 on 2026-10-13. The exponent is exact in the short-time limit and the derivation route he describes is real apart from the word "eigenvalue"; as a literal equality with no domain it is more than 25% off at each of the paper's three N<sub>e</sub> values. Reading-dependent: A (a relay of Hard Limits' asymptote) sets B1e's fields, <code>holds</code> / <code>partial</code> / <code>contested</code>; B (literal equality) <code>non-sequitur</code> / <code>misread</code> / <code>contradicted</code>. No claim node; no verdict on B1, B1a, B2 or B moves.</li>
'''
s = s[:j] + add + s[j:]
sub1('<h2>Registered 2026-10-11 to 2026-10-13: run, reviewed, integrated</h2>', '<h2>Registered 2026-10-11 to 2026-10-13: run, reviewed, integrated</h2>')

# ---- Next: refresh follow-ups done, ph2 running
sub1('pin the old md5 in claims citing the replaced Zenodo paper (22903977); a pre-registered derivation check of F(T) = exp(-pi^2 N_e / T) with both sides\' predictions.</li>',
     'add the Q283 restatement row to the versions ledger (Q283 against the dates of the "G_f" and "Day\'s own adoption of 1,587" rows). Done 2026-10-13: the old md5 pinned in the claims citing Zenodo 22903977, and the derivation check of F(T) (B2f).</li>')
sub1('HF long burn at lam 0.8 and 1.6 for R = 1.05.</li>',
     'HF long burn at lam 0.8 and 1.6 for R = 1.05 (run <code>ph2</code>, 31 jobs on na-workhorse, launched 2026-10-13, expected done about 2026-10-16; not collected).</li>')

# ---- roadmap table, parsed from ROADMAP.md
sec = None; cnt = collections.defaultdict(collections.Counter)
for l in open('ROADMAP.md').read().splitlines():
    m = re.match(r'## ([A-E])\.', l)
    if m: sec = m.group(1)
    if re.match(r'\| [A-E]\d+ \|', l):
        cells = [x.strip() for x in l.strip('|').split('|')]
        cnt[sec][cells[3]] += 1
tot = collections.Counter()
for k_ in cnt: tot.update(cnt[k_])
stat = ['running', 'queued', 'proposal', 'needs owner', 'tbd', 'done']
assert set(tot) <= set(stat), tot
N = sum(tot.values())
assert N == 120 and tot['needs owner'] == 34, (N, tot)   # unchanged; only statuses in section A moved
trs = ''.join('      <tr><th scope="row">%s</th><td>%d</td>%s</tr>\n' % (k_, sum(cnt[k_].values()), ''.join('<td>%d</td>' % cnt[k_][x] for x in stat)) for k_ in 'ABCD')
trs += '      <tr><th scope="row">All</th><td><b>%d</b></td>%s</tr>\n' % (N, ''.join('<td><b>%d</b></td>' % tot[x] for x in stat))
i = s.index('<table class="rm">'); i = s.index('<tbody>\n', i) + 8; j = s.index('    </tbody>', i)
assert s[i:j] != trs
s = s[:i] + trs + s[j:]

s = s.replace('</footer>', '</footer>\n<!-- upd22 applied 2026-10-13 -->', 1)
open(p, 'w').write(s)
