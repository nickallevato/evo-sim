# 2026-10-13: board patch before the first public publication (D-26). Brings the page to the files of record after the
# O-5 revert (2740ded, D-21): B internal and A2e external are `pending` (superseded values kept in the claim files);
# verdict tallies from lint_research.py (internal 132/18/2/52, external 34/116/17/6/48); roadmap counts parsed from the
# row statuses of ROADMAP.md (rows with a decided / unblocked / go-ahead status get their own column; the owner list is
# cut to the rows still `needs owner`); argmap_check.py counts unchanged (468 defeaters, 246 lineage nodes) and its four
# known quote-not-found errors noted on the page, not fixed here. Reading-dependent count (8 claims, 12 fields, 3 RH tags)
# is not recounted: the claim files carry the same reading-dependent comment lines before and after the revert.
# ph2 stays shown as running. No verdict value moves except the two reverts the files of record already hold.
# Run from docs/research/. Patches status.html in place; each step asserts its anchor so it cannot apply twice.
import re, collections
p = 'status.html'; s = open(p).read()
assert 'upd23' not in s and 'upd22 applied' in s

def sub1(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:70])
    s = s.replace(old, new, 1)

# ---- verdict tallies (lint_research.py)
sub1('<b>19</b> non-sequitur · <b>2</b> arithmetic error · <b>51</b> pending', '<b>18</b> non-sequitur · <b>2</b> arithmetic error · <b>52</b> pending')
sub1('<b>18</b> contradicted · <b>6</b> untestable · <b>47</b> pending', '<b>17</b> contradicted · <b>6</b> untestable · <b>48</b> pending')

# ---- the two reverted fields, wherever the page states them as current
sub1('Internal non-sequitur, external contested (two dependencies).',
     'Internal non-sequitur; external <b>pending</b> since 2026-10-13 (D-21; the earlier value, contradicted in scope, is kept in the claim file as superseded).')
sub1('4 claims carry a verdict (DN6 external, B9 internal, C7 internal and external, B internal) and 3 a rhetoric tag with no verdict change (Hancock RH-15, Myers RH-20, Mansfield RH-18).',
     '4 claims carry a verdict (DN6 external, B9 internal, C7 internal and external, B internal) and 3 a rhetoric tag with no verdict change (Hancock RH-15, Myers RH-20, Mansfield RH-18). <b>Since 2026-10-13 (D-21) B internal is <span class="mono">pending</span>; its reading-dependent value, non-sequitur, is kept in the claim file as superseded.</b>')
sub1('A2e external is contradicted for the any-effect-size count,',
     'A2e external (<b>pending</b> since 2026-10-13, D-21; the value below is superseded) was contradicted for the any-effect-size count,')
sub1('O-5 revert or re-review B internal and A2e external (owner asked for an explanation);',
     'O-5 answered 2026-10-13 (D-21): B internal and A2e external are back to <span class="mono">pending</span> until three reviews are done (the three reviews each are not yet weighed; no ruling made);')

# ---- audit's own errors
sub1('<span><b>246</b> dated argument versions</span>',
     '<span><b>246</b> dated argument versions</span><span>argmap_check.py: <b>4 known errors</b>, all quote-not-found (<span class="mono">L-adna-630-21-2026</span>, <span class="mono">L-dembski-scaling-reply-2026</span>, d129, d176); not yet fixed</span>')

# ---- roadmap table and owner list, parsed from ROADMAP.md
sec = None; cnt = collections.defaultdict(collections.Counter); need = []
base = ['running', 'queued', 'proposal', 'needs owner', 'tbd', 'done']
for l in open('ROADMAP.md').read().splitlines():
    m = re.match(r'## ([A-E])\.', l)
    if m: sec = m.group(1)
    if re.match(r'\| [A-E]\d+ \|', l):
        cells = [x.strip() for x in l.strip('|').split('|')]
        st = cells[3]
        if st not in base:
            assert st.startswith('**'), st
            st = 'decided'
        cnt[sec][st] += 1
        if st == 'needs owner': need.append(cells[0])
stat = base[:4] + ['decided'] + base[4:]
tot = collections.Counter()
for k_ in cnt: tot.update(cnt[k_])
assert set(tot) <= set(stat), tot
N = sum(tot.values()); assert N == 120, N
trs = ''.join('      <tr><th scope="row">%s</th><td>%d</td>%s</tr>\n' % (k_, sum(cnt[k_].values()), ''.join('<td>%d</td>' % cnt[k_][x] for x in stat)) for k_ in 'ABCD')
trs += '      <tr><th scope="row">All</th><td><b>%d</b></td>%s</tr>\n' % (N, ''.join('<td><b>%d</b></td>' % tot[x] for x in stat))
sub1('<th scope="col">needs owner</th><th scope="col">tbd</th>', '<th scope="col">needs owner</th><th scope="col">decided / go-ahead</th><th scope="col">tbd</th>')
i = s.index('<table class="rm">'); i = s.index('<tbody>\n', i) + 8; j = s.index('    </tbody>', i)
s = s[:i] + trs + s[j:]
assert tot['needs owner'] == len(need) == 28, (tot, need)
i = s.index('<p><b>Needs the owner (34):</b></p>'); j = s.index('</ul>', i)
blk = s[i:j]
keep = [ln for ln in blk.split('\n') if not re.match(r'\s*<li><b>([A-D]\d+)</b>', ln) or re.match(r'\s*<li><b>([A-D]\d+)</b>', ln).group(1) in need]
assert sum('<li>' in x for x in keep) == 28
s = s[:i] + '\n'.join(keep).replace('(34)', '(%d)' % len(need)) + s[j:]

s = s.replace('<!-- upd22 applied 2026-10-13 -->', '<!-- upd23 applied 2026-10-13 -->\n<!-- upd22 applied 2026-10-13 -->', 1)
open(p, 'w').write(s)
