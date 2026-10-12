# 2026-10-12: owner request "update diagrams and readmes with logic/systems/triver and plans or roadmap":
# adds (1) the systems diagram (inline SVG, themed from the page's CSS variables) and (2) a compact roadmap section
# (counts by status, needs-owner list) to docs/research/status.html, and replaces the "Triveritas: in progress" line
# in the Criticality section. Counts are parsed from docs/research/ROADMAP.md at run time. Run from docs/research/.
import re, collections
p = 'status.html'; s = open(p).read()
marker = "<section>\n  <h2>Next</h2>"
assert marker in s and 'Roadmap: everything outstanding' not in s

# ---- roadmap counts, parsed from ROADMAP.md
sec = None; cnt = collections.defaultdict(collections.Counter); owner = []
for l in open('ROADMAP.md').read().splitlines():
    m = re.match(r'## ([A-E])\.', l)
    if m: sec = m.group(1)
    if re.match(r'\| [A-E]\d+ \|', l):
        cells = [x.strip() for x in l.strip('|').split('|')]
        cnt[sec][cells[3]] += 1
        if cells[3] == 'needs owner': owner.append(cells[0])
tot = collections.Counter()
for k in cnt: tot.update(cnt[k])
N = sum(tot.values())
assert N == 62 and tot['needs owner'] == 17 and len(owner) == 17, (N, tot)
short = {
 'B7': 'stale "most charitable" comments (after O-5)', 'B20': 'Triveritas findings need an outside rater',
 'C1': 'O-1 buy the book and say how to supply the text', 'C2': 'O-2 approve right-of-reply text and channel',
 'C3': 'O-3 approve the reviewer brief; someone to approach', 'C4': 'O-4 run or give access to the non-Claude packet',
 'C5': 'O-5 revert B and A2e or re-review (explanation asked)', 'C6': 'O-6 confirm the rule-freeze reading',
 'C7': 'O-7 confirm the corpus-freeze reading', 'C9': 'O-9 licence choice and COI facts',
 'C10': 'go-ahead for proposals a, b, c', 'C11': 'confirm the proposed R5 exit criterion',
 'C13': 'Q157/Q158 and the four unclear RH tags', 'C14': 'O-10 (proposed) Triveritas packet to non-Claude raters',
 'C15': 'O-11 (proposed) tell Day the result, invite him to score', 'C16': 'O-12 (proposed) Triveritas as standing lens or one-off',
 'D4': 'paywalled full texts (list in ROADMAP D4)'}
assert set(short) == set(owner), set(owner) ^ set(short)
stat = [('running', 's-run'), ('queued', 's-run'), ('proposal', 's-pend'), ('needs owner', 's-data'), ('tbd', 's-todo'), ('done', 's-ok')]
def chip(c, t): return '<span class="chip %s">%s</span>' % (c, t)
trs = ''.join('      <tr><th scope="row">%s</th><td>%d</td>%s</tr>\n' % (k, sum(cnt[k].values()), ''.join('<td>%d</td>' % cnt[k][x] for x, _ in stat)) for k in 'ABCD')
trs += '      <tr><th scope="row">All</th><td><b>%d</b></td>%s</tr>\n' % (N, ''.join('<td><b>%d</b></td>' % tot[x] for x, _ in stat))
head = ''.join('<th scope="col">%s</th>' % x for x, _ in stat)
lis = ''.join('    <li><b>%s</b> %s</li>\n' % (i, short[i]) for i in owner)

# ---- inline systems diagram, recoloured through CSS variables
svg = open('../img/audit-systems.svg').read().strip()
svg = svg.replace('<svg xmlns="http://www.w3.org/2000/svg" ', '<svg class="sysfig" xmlns="http://www.w3.org/2000/svg" ', 1)
svg = re.sub(r' width="1010" height="640"', '', svg, count=1)
assert 'class="sysfig"' in svg
css = '''<style>
.sysfig{width:100%;height:auto;display:block;font-size:12px}
.sysfig text{fill:var(--fg)}
.sysfig [fill="#6e7681"]{fill:var(--muted)} .sysfig [stroke="#6e7681"]{stroke:var(--muted)}
.sysfig rect[fill="#3b82f6"]{fill:var(--run)} .sysfig rect[stroke="#3b82f6"]{stroke:var(--run)}
.sysfig rect[fill="#e8833a"]{fill:var(--bad)} .sysfig rect[stroke="#e8833a"]{stroke:var(--bad)}
.sysfig rect[fill="#22c55e"]{fill:var(--ok)} .sysfig rect[stroke="#22c55e"]{stroke:var(--ok)}
.sysfig rect[fill="#8b5cf6"]{fill:var(--accent)} .sysfig rect[stroke="#8b5cf6"]{stroke:var(--accent)}
.sysfig rect[fill="#eab308"]{fill:var(--pend)} .sysfig rect[stroke="#eab308"]{stroke:var(--pend)}
.sysfig path[stroke="#eab308"]{stroke:var(--pend)} .sysfig path[fill="#eab308"]{fill:var(--pend)}
.sysfig text[fill="#8b5cf6"]{fill:var(--accent)}
table.rm{border-collapse:collapse;font-size:.88rem} table.rm th,table.rm td{border:1px solid var(--line);padding:4px 10px;text-align:right} table.rm th[scope=row],table.rm thead th:first-child{text-align:left}
</style>
'''
diagram = '''<section>
  <h2>How the audit fits together</h2>
  <p>Sources, quotes, claims with three verdicts, argument map, checks, reviews, verdict rule, ledgers, synthesis and simulator spec, with the criticality layer drawn over all of it. Blue: pipeline; red-brown: Day-side sources and hard rules; green: synthesis; violet: criticality layer; amber: feedback and proposals. Source of the figure: <span class="mono">research/tools/readme_figs.py</span> (<span class="mono">docs/img/audit-systems.svg</span>); the verdict-logic and roadmap figures are beside it.</p>
  <figure class="f">%s
    <figcaption>Every pass of the criticality layer so far was run by Claude inside the project; none is outside review.</figcaption>
  </figure>
</section>

''' % svg
roadmap = '''<section>
  <h2>Roadmap: everything outstanding</h2>
  <p>One table of every open item, with source, status, blocker, next step, who and cost: <span class="mono">docs/research/ROADMAP.md</span> (%d rows in sections A to D; section E is the ordered path to R5 and the simulator phase). No dates: order and dependencies only.</p>
  <table class="rm">
    <thead><tr><th scope="col">Section</th><th scope="col">Rows</th>%s</tr></thead>
    <tbody>
%s    </tbody>
  </table>
  <p>A compute and checks; B criticality remediation; C owner decisions; D outside inputs. One job is running (the HF post hoc run); ten items are queued behind it or behind a pre-registration. Nothing has been sent to anyone.</p>
  <p><b>Needs the owner (%d):</b></p>
  <ul class="next">
%s  </ul>
</section>

''' % (N, head, trs, tot['needs owner'], lis)

# ---- Triveritas line in the criticality section
old = "<li><b>Triveritas critique</b> (the audit assessed with Day's own system): <b>in progress</b>.</li>"
assert old in s
new = ("<li><b>Triveritas critique</b> (the audit assessed with Day's own test: logic, mathematics and empirical anchoring must all hold, Q203): "
       "<b>done 2026-10-12</b>, findings TV-01 to TV-11 (2 CRITICAL, 6 MAJOR, 1 MINOR to MAJOR, 2 MINOR); no verdict, rule or claim changed. "
       "By that test the audit's tallies do not yet merit assent, chiefly on independence (the same weakness as MA-01); Day's root claim and the critics' positive thesis also fail the conjunction as things stand. "
       "Concordance with the 20 MA findings: agrees 11, in part 3, partly disagrees 3, not covered 6. Same model family, not blind, outside Day's own protocol (TV-11). "
       "Files: <span class=\"mono\">docs/research/criticality/triveritas-method.md</span>, <span class=\"mono\">triveritas-audit-2026-10-12.md</span>.</li>")
s = s.replace(old, new, 1)
# css goes in head
assert '</style>' in s
i = s.index('</style>')
s = s[:i] + css.replace('<style>\n', '').replace('</style>\n', '') + s[i:]
s = s.replace(marker, diagram + roadmap + marker, 1)
open(p, 'w').write(s)
print("ok", N, dict(tot))
