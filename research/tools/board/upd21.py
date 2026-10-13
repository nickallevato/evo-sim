# 2026-10-13: board patch after the 2026-10-13 batch (HF ph, L1b, L1c, FMnull, L5: run, reviewed #66-#80, fix-passed,
# integrated) and criticality pass vii (MA-21..MA-30). Counts from the files of record: lint_research.py (verdicts, claims),
# argmap_check.py (defeaters, lineage), ROADMAP.md (parsed at run time), PREREG-STATUS.md, HANDOFF.md (reading-dependent).
# Run from docs/research/. Patches status.html in place; each step asserts its anchor so it cannot apply twice.
import re, collections
p = 'status.html'; s = open(p).read()
assert 'upd21' not in s

def sub1(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:70])
    s = s.replace(old, new, 1)

# ---- header, pipeline, headline counts
sub1('status as of 2026-10-12', 'status as of 2026-10-13')
sub1('<span>204 claim files</span>', '<span>233 claim files</span>')
i = s.index('<div class="stage now"><b>R4 Math checks</b>'); j = s.index('</div>\n', s.index('</span>', i))
old = s[i:j]
new = ('<div class="stage now"><b>R4 Math checks</b><div class="bar"><i style="width:99%"></i></div><span>~99%, 59 checks reviewed; '
       'the 2026-10-13 batch (HF post hoc <code>ph</code>, L1b, L1c, FMnull, L5) is run, reviewed (#66-#80), fix-passed and integrated; '
       'criticality pass vii done; next: milestone post, then R5 prerequisites (ROADMAP)</span>')
s = s[:i] + new + s[j:]
sub1('<span><b>419</b> typed objections</span><span><b>232</b> dated argument versions</span>',
     '<span><b>462</b> typed objections</span><span><b>243</b> dated argument versions</span>')
sub1('<b>7</b> reading-dependent (4 verdicts, 3 RH tags)',
     '<b>10</b> reading-dependent verdicts (6 claims carry a reading-dependent verdict field, 3 more a reading-dependent RH tag; HANDOFF)')
sub1('<b>114</b> contested · <b>18</b> contradicted · <b>6</b> untestable · <b>49</b> pending',
     '<b>115</b> contested · <b>18</b> contradicted · <b>6</b> untestable · <b>48</b> pending')
sub1('<b>10</b> misread · <b>58</b> unverifiable · <b>11</b> pending',
     '<b>11</b> misread · <b>58</b> unverifiable · <b>10</b> pending')

# ---- jobs list: HF done, five new Done lines
old_hf = [l for l in s.split('\n') if '<b>In progress:</b> HF (H follow-ups)' in l]
assert len(old_hf) == 1
done = '''      <li><b>Done:</b> reviews #66-#69 (HF, H follow-ups; three reviews plus a combined review of the post hoc run <code>ph</code>, 410 jobs, 454.8 CPU-hours, 0 cross-host mismatches): soft selection and truncation sustain at least 0.8-1.6 substitutions per generation at R of 1.111 or more, but cannot go extinct in-model and the cost is not reduced, only not charged; the softJ failures were a fill lag (80 of 80 long-burn pass); mix boundary about 1.3-1.7x the hard cap at h = 0.3; Day's 1/300 conservative at R = 1.111; H, H8, H5 external stay contested</li>
      <li><b>Done:</b> reviews #70-#72 (L1b, T2T rerun of the dN/dS check; load-bearing; fix pass 098ac12): band CRITIC; on hs1 / mPanTro3 pooled dN/dS is 0.271 (all genes), 0.238 (one2one), 0.209 (syntenic); 0.214-0.283 over 32 filter stacks, none near 0.65; the gene-set effect in Day's direction is real (+14%, not 0.80); a naive position-by-position extraction reads 0.853 (an audit miss, credited to neither side); DN1 external contradicted (reading-dependent)</li>
      <li><b>Done:</b> reviews #73-#75 (L1c, alignment method against dN/dS; load-bearing; fix pass 140a69a): band CRITIC; the audit's protein-guided arms lower pooled dN/dS by only 2.3-5.8% (the claim needs 71%), in Day's direction in every arm; the held CSAC 2005 Methods show the 13,454-gene set came from a genome alignment, not a protein-guided one; DN6 external contested (reading b2), fidelity misread (reading a), reading-dependent; the 1.40% of codons Cactus does not align are not tested</li>
      <li><b>Done:</b> reviews #76-#79 (FMnull, neutral-null calibration of "more than 80 times more variable"; fix pass 2802425): no verdict value moves; Day's sentence is true of the held alignment at windows of 1 Mb or more in all ten cells and as true of chimpanzee, bonobo and gorilla as of human; where true at 1 Mb or less the measured index sits inside or below the mechanistic neutral band; the check has little power against small planted blocks, and S2 as registered could not fire (an audit defect, not counted against Day)</li>
      <li><b>Done:</b> review #80 (L5, ancient-DNA zero-fixation power; combined; fix pass 0b0431c): band CRITIC; at Day's required rate the expected count of his zero statistics is effectively 0 for s up to 1e-2 (registered scope; the same at 0.02), so the zero says nothing there; at s of 0.05 or more the panel registers hundreds to thousands of events, so his zero excludes strong-sweep rescue of the required rate; C external stays contested (reading-dependent), C1a sign untested</li>
      <li><b>Done:</b> criticality pass vii (method audit of this batch, 2026-10-13): MA-21 to MA-30, see the Criticality section; integrator fixes applied the same day</li>'''
s = s.replace(old_hf[0], done, 1)

sub1('Open: L1b T2T rerun.', 'L1b T2T rerun done 2026-10-13 (DN1 external contradicted, reading-dependent; the registered condition on L1b discharged).')

# ---- refresh 2026-10-12 section: DN6 now decided; critic-reply sentence
sub1('(b) "Such pipelines in general bias dN/dS downward": pending, L1c decides. The verdict field takes (b), the reading most defensible to Day.',
     '(b) "Such pipelines in general bias dN/dS downward": decided by L1c (2026-10-13): the audit\'s arms move the estimate 2-6% against the 71% needed, in Day\'s direction; external contested (reading b2, the field), material artefact behind the published 0.23 contradicted (b1). The field takes (b), the reading most defensible to Day.')
sub1('No critic or ally has replied to the FM or dN/dS posts yet (critics refresh, same day).',
     'No written critic or ally reply to the FM or dN/dS posts had appeared at that refresh; a long video reply appeared on 2026-10-13 (next section).')

# ---- the registered-not-run section becomes a results section; new refresh section
i = s.index('<section>\n  <h2>Pre-registered, not yet run</h2>'); j = s.index('  <figure class="f">', i)
batch = '''<section>
  <h2>Registered 2026-10-11 to 2026-10-13: run, reviewed, integrated</h2>
  <p>Predictions were committed before each run (labels per check in <span class="mono">research/checks/PREREG-STATUS.md</span>: all of this batch is labelled blind by the tool, with caveats the label misses, MA-25). Two commits are post hoc and labelled so. Results, one line each:</p>
  <ol class="next">
    <li><b>HF <code>ph</code></b> (hf_posthoc.py, 5c30ed9; post hoc, 410 jobs on na-workhorse and builder): the softJ failures were a fill lag; no K effect up to lam 1.6 on the late trace window. HF verdict values unchanged. Open: long burn at lam 0.8 and 1.6 for R = 1.05.</li>
    <li><b>L1b</b> (0fe3c7f): T2T rerun. Band CRITIC. V0 all genes 0.271, one2one 0.238, syntenic 0.209; none of 32 filter stacks near 0.65. Audit miss: a naive extraction reads 0.853.</li>
    <li><b>L1c</b> (536b19b, amended pre-run 0e0e840): alignment method. Band CRITIC. Protein-guided arms lower pooled dN/dS 2.3-5.8% (71% needed); the 0.23 was not made by a protein-guided alignment (CSAC 2005 Methods); the 1.40% unaligned codons are untested.</li>
    <li><b>FMnull</b> (48241c7, amended cc5e6dd, 408ba53): neutral-null calibration. No verdict value moves; "more than 80" is true of the alignment at 1 Mb or more in every lineage and measured index is inside or below the neutral band where true at 1 Mb or less; low power against small planted blocks. Open: criterion S4 unrun; Poisson GLM re-estimate.</li>
    <li><b>L5</b> (0e6da82): ancient-DNA power. Band CRITIC. Zero fixations carry no information on the required rate at s of 1e-2 or below (also at 0.02); at s of 0.05 or more they exclude strong-sweep rescue. C external contested (reading-dependent). Open: random-SNP comparator for C1a's sign.</li>
  </ol>
'''
s = s[:i] + batch + s[j:]
sub1('Registered, not yet run.</desc>', 'Registered before the run; results in the list above.</desc>')
sub1('Not yet run.</figcaption>', 'Registered before the run; see the L1c result above.</figcaption>')

refresh = '''<section>
  <h2>Refresh 2026-10-13: a critic video reply exists (unreviewed)</h2>
  <p>Dated 2026-10-13 (about 18:55-19:40 UTC; <span class="mono">docs/research/sources/refresh-2026-10-13.md</span>). <b>Gutsick Gibbon posted a 4:14:03 video, "Six Scientists Roast One Racist Loser" (id AqC1ZM4icms), about 18:00 UTC.</b> It is not reviewed: no captions existed at fetch, so whether it addresses the dN/dS posts or "The Fourth Mechanism" is unknown. Harvest is queued; until then this audit says "no written critic reply found; a video reply exists and is unreviewed".</p>
  <ol class="next">
    <li>No release of Q176's per-gene table, gene list, code or window size by Day; "The Method is the Conclusion" had a typo fix only.</li>
    <li>Four new Day posts tagged evolution. "A Shot Fired" (text under the name "Claude Athos") restates the 1,322 to 1,587 generations-per-fixation change as an immediate adoption (Q283; to be checked against the versions ledger) and gives a new figure, 10^(-78,000,000), for modern humans (Q284; unchecked, now in parameters.yaml as a quoted figure).</li>
    <li>Zenodo record 22903977 was silently retitled "k != mu: The Finite-Time Collapse of Neutral Substitution Theory" with its file replaced; it adds a closed form F(T) = exp(-pi^2 N_e / T) (Q286). A derivation check is queued; claims citing the old text will pin the old md5.</li>
  </ol>
</section>

'''
k = s.index('<section>\n  <h2>Registered 2026-10-11 to 2026-10-13')
s = s[:k] + refresh + s[k:]

# ---- criticality
sub1('<span>Method audit findings <b>20</b>: CRITICAL <b>1</b>, MAJOR <b>10</b>, MINOR to MAJOR <b>1</b>, MINOR <b>7</b>, COSMETIC <b>1</b></span>',
     '<span>Method audit findings <b>30</b> (MA-01 to MA-30): CRITICAL <b>1</b>, MAJOR <b>14</b>, MINOR to MAJOR <b>1</b>, MINOR <b>12</b>, COSMETIC <b>2</b></span>')
sub1('<p>MA-13 to MA-18 (MINOR) and MA-20 (COSMETIC) are open.</p>',
     '''<p>MA-13 to MA-18 (MINOR) and MA-20 (COSMETIC) are open.</p>
  <p><b>Pass vii, 2026-10-13</b> (<span class="mono">docs/research/criticality/METHOD-AUDIT-2026-10-13.md</span>; the batch audit of HF <code>ph</code>, L1b, L1c, FMnull, L5): MA-21 to MA-30, <b>0 CRITICAL, 4 MAJOR, 5 MINOR, 1 COSMETIC</b>. 24 steelman rulings tabulated: Day 5, critic 5, split 14. Closed by the pass: <b>MA-12</b>, <b>ST-08</b>, <b>ST-09</b>.</p>
  <ul class="next">
    <li><b>MA-21</b> (MAJOR) One instance is author, briefer and judge: the lead wrote the scoring and the rulings, and briefed reviewers with the issues it suspected</li>
    <li><b>MA-22</b> (MAJOR) "Extended reading" and "registered wording governs" are applied case by case, with results in view</li>
    <li><b>MA-23</b> (MAJOR) L5 had one review while carrying a registered verdict flip (that review then found 7 MAJOR)</li>
    <li><b>MA-24</b> (MAJOR) Day-side outcomes were unreachable in parts of three of four new checks (repeats ST-05)</li>
  </ul>
  <p>Integrator fixes from MA-25, MA-26 and MA-28 were applied on 2026-10-13 (prereg table regenerated with a row for <code>ph</code> and notes for L1c and L5; scope of claim C restored to s of 1e-2 or below; DN1's superseded sentence marked; the L1c reviews' single authorship noted); MA-29 and the remainder stay on the roadmap (B56 to B61).</p>''')
sub1('(<span class="mono">research/checks/PREREG-STATUS.md</span>, 61 registered checks): blind <b>10</b>, criterion-only <b>6</b>, reproduction <b>3</b>, single-commit <b>18</b>, unknown <b>20</b>, registered not run <b>4</b>.',
     '(<span class="mono">research/checks/PREREG-STATUS.md</span>, 62 registered checks, regenerated 2026-10-13): blind <b>15</b>, criterion-only <b>6</b>, reproduction <b>3</b>, single-commit <b>18</b>, unknown <b>20</b>, registered not run <b>0</b>.')
sub1('Concordance with the 20 MA findings', 'Concordance with the first 20 MA findings')

# ---- roadmap, parsed from ROADMAP.md (all rows, all statuses)
sec = None; cnt = collections.defaultdict(collections.Counter); owner = []
for l in open('ROADMAP.md').read().splitlines():
    m = re.match(r'## ([A-E])\.', l)
    if m: sec = m.group(1)
    if re.match(r'\| [A-E]\d+ \|', l):
        cells = [x.strip() for x in l.strip('|').split('|')]
        cnt[sec][cells[3]] += 1
        if cells[3] == 'needs owner': owner.append((cells[0], cells[1]))
tot = collections.Counter()
for k_ in cnt: tot.update(cnt[k_])
N = sum(tot.values())
stat = ['running', 'queued', 'proposal', 'needs owner', 'tbd', 'done']
assert set(tot) <= set(stat), tot
oid = [o[0] for o in owner]
assert 'C27' in oid and 'C30' in oid
def shorten(t):
    t = re.sub(r'\*\*|`', '', t)
    t = re.split(r'; concordance|\. Owner said|\(proposed|\(pass vii|\. ', t)[0]
    return (t[:110].rstrip(' ,;:') + ('...' if len(t) > 110 else ''))
lis = ''.join('    <li><b>%s</b> %s</li>\n' % (i_, shorten(t)) for i_, t in owner)
trs = ''.join('      <tr><th scope="row">%s</th><td>%d</td>%s</tr>\n' % (k_, sum(cnt[k_].values()), ''.join('<td>%d</td>' % cnt[k_][x] for x in stat)) for k_ in 'ABCD')
trs += '      <tr><th scope="row">All</th><td><b>%d</b></td>%s</tr>\n' % (N, ''.join('<td><b>%d</b></td>' % tot[x] for x in stat))
i = s.index('<h2>Roadmap: everything outstanding</h2>'); i = s.index('<p>', i); j = s.index('</section>', i)
road = ('<p>One table of every open item, with source, status, blocker, next step, who and cost: <span class="mono">docs/research/ROADMAP.md</span> (%d rows in sections A to D; section E is the ordered path to R5 and the simulator phase). No dates: order and dependencies only.</p>\n'
        '  <table class="rm">\n    <thead><tr><th scope="col">Section</th><th scope="col">Rows</th>%s</tr></thead>\n    <tbody>\n%s    </tbody>\n  </table>\n'
        '  <p>A compute and checks; B criticality remediation; C owner decisions; D outside inputs. Nothing has been sent to anyone. New open owner decisions from pass vii: <b>O-24</b> (raise the two-subagent cap?), <b>O-25</b> (review tier when a registration carries a verdict flip), <b>O-26</b> (who rules conflicts between steelman reviews; whether briefs name suspected issues), <b>O-27</b> (fairer Day-side criterion for FM10, proposal l).</p>\n'
        '  <p><b>Needs the owner (%d):</b></p>\n  <ul class="next">\n%s  </ul>\n') % (N, ''.join('<th scope="col">%s</th>' % x for x in stat), trs, tot['needs owner'], lis)
s = s[:i] + road + s[j:]

# ---- Next
i = s.index('<h2>Next</h2>'); i = s.index('<ol class="next">', i); j = s.index('</ol>', i) + 5
nxt = '''<ol class="next">
    <li><b>Now:</b> milestone post for the 2026-10-13 batch (written by the lead, not this patch); a criticality pass has been run (pass vii).</li>
    <li><b>Queued, 2026-10-13 refresh:</b> harvest the Gutsick Gibbon video AqC1ZM4icms once captions exist (a critic reply exists, unreviewed); check Q283 (the 1,587 "adoption") against the versions ledger; pin the old md5 in claims citing the replaced Zenodo paper (22903977); a pre-registered derivation check of F(T) = exp(-pi^2 N_e / T) with both sides' predictions.</li>
    <li><b>Open follow-ups from the fix passes:</b> FMnull criterion S4 and the Poisson GLM re-estimate; L1c external codon-aware aligner on an independent chimp CDS; L5 random-SNP comparator for C1a's sign; HF long burn at lam 0.8 and 1.6 for R = 1.05.</li>
    <li><b>Open:</b> FM10 internal (rule N2d); cause of the chrX 57.3 Mb window; the B3m 2-vs-25 gap; the Hard Limits peroration RH tag (owner); XT follow-up (U-scaling rerun or SLiM).</li>
    <li><b>Queued:</b> reviews of the 12 new mapping claims; E leftovers, GAP-03; fetch tasks (CSAC 2005 and an independent ML dN/dS; Good 2017 SI 5.2; Uricchio full text; Day's per-gene table); a transversion-matched neutral model for Day's 21; the remaining load-bearing claims without a reviewed check (R5 draft).</li>
    <li><b>Owner:</b> O-24 to O-27 and the earlier open decisions (Roadmap section above).</li>
    <li>R5: final verdicts, sensitivity table, simulator variable list.</li>
  </ol>'''
s = s[:i] + nxt + s[j:]
s = s.replace('</footer>', '</footer>\n<!-- upd21 applied 2026-10-13 -->', 1) if '</footer>' in s else s + '\n<!-- upd21 applied 2026-10-13 -->\n'
open(p, 'w').write(s)
print('ok', N, dict(tot))
