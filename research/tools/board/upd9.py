# 2026-10-08: E and G1 reviewed; argument map, gaps, prior art; corrected tallies (194 claims)
p = 'status.html'; s = open(p).read()
R = [
 ('<span>193 claim files</span>', '<span>194 claim files</span>'),
 ('<i style="width:80%"></i></div><span>~80%, round 2 reviewed and committed</span>',
  '<i style="width:88%"></i></div><span>~88%, E and G1 reviewed; H, D, C1b left</span>'),
 ('<span><b>193</b> claims (day 107 · critic 46 · ally 16 · lit 24)</span>',
  '<span><b>194</b> claims (day 106 · critic 47 · ally 15 · lit 26)</span><span><b>238</b> typed objections</span><span><b>178</b> dated argument versions</span>'),
 ('<b>89</b> holds · <b>14</b> non-sequitur · <b>6</b> arithmetic error · <b>61</b> pending',
  '<b>95</b> holds · <b>15</b> non-sequitur · <b>6</b> arithmetic error · <b>55</b> pending'),
 ('<b>21</b> supported · <b>97</b> contested · <b>9</b> contradicted · <b>5</b> untestable · <b>50</b> pending',
  '<b>21</b> supported · <b>101</b> contested · <b>9</b> contradicted · <b>5</b> untestable · <b>47</b> pending'),
 ('<b>35</b> accurate · <b>31</b> partial · <b>9</b> misread · <b>35</b> unverifiable</span>',
  '<b>37</b> accurate · <b>31</b> partial · <b>9</b> misread · <b>35</b> unverifiable · <b>9</b> pending</span>'),
 ('<li data-s="todo"><span class="id">E</span><span class="claim"><span class="c">Founder hazard 2.3%; relictation exact chains</span><span class="f">Queued.</span></span></li>',
  '<li data-s="ok"><span class="id">E</span><span class="claim"><span class="c">Founder hazard 2.3% per event</span><span class="f">The size holds: 2.0–2.75% in exact models. The route is wrong (one carrier suffices; the 0.39 comes from sampling with replacement), and the errors partly offset. Consequence for real populations untested; Day defers it himself.</span></span></li>\n'
  '        <li data-s="ok"><span class="id">E3</span><span class="claim"><span class="c">Simulation: 2.33%</span><span class="f">Reproduces only under a mean-field selection step; the literal reading gives 2.75%, so the pre-registered falsifier fired. "Independently sufficient" and "minefields" marked overreach.</span></span></li>\n'
  '        <li data-s="ok"><span class="id">E4</span><span class="claim"><span class="c">Relictation exact chains</span><span class="f">Reproduces exactly. The known multiple-merger result: it moves mean fixation time, never P_fix = 1/(2N) or k. keruru reached the same chain on 2026-08-26.</span></span></li>'),
 ('<li data-s="todo"><span class="id">G1</span><span class="claim"><span class="c">0.02^(2×10⁷): specific outcome vs any outcome</span><span class="f">Queued.</span></span></li>',
  '<li data-s="ok"><span class="id">G1</span><span class="claim"><span class="c">0.02^(2×10⁷): specific outcome vs any outcome</span><span class="f">p^n prices one pre-specified list and is timing-independent, so it cannot force sequential fixation. With interchangeable routes, "any" wins above 12–17 successful arisings per needed change; branch D must supply that number. No cap near 230 under multiplicative fitness. The audit withdrew its own "mixed scales" objection to 14.7×.</span></span></li>'),
 ('<li>Six dated milestone posts, linked from the handoff.</li>',
  '<li>Seven dated milestone posts, linked from the handoff.</li>\n    <li><a href="https://github.com/nickallevato/evo-sim/blob/research/docs/arguments/README.md">Argument map</a>: standard forms, 238 objections typed undermining / undercutting / rebutting, a genealogy of 178 dated versions since 1966, and seven gaps nobody closed.</li>'),
 ('<li>Remaining checks: E (founder hazard, relictation), G1 (specific vs any outcome), D (sequence space).</li>\n    <li>Follow-ups: C1b with realistic per-site call depth; H at realistic human reproductive excess and hard-selected load; confidence intervals on H; Yoo\'s mutation rate for rescaling ancestral Nₑ.</li>',
  '<li><b>H at human scale</b>, bounded by the adaptive fraction (GAP-01: 10³–10⁶ selected changes), with a Nei / Felsenstein analytic cross-check.</li>\n    <li>Quick gap checks: Weissman–Barton finite-map cap (GAP-04), indel/SV event counts (GAP-07), sweep-scan windows (GAP-02).</li>\n    <li>D (sequence space): how many interchangeable routes per needed change. Then C1b call depth, H confidence intervals, Yoo\'s μ.</li>'),
]
for a, b in R:
    assert s.count(a) == 1, a[:60]
    s = s.replace(a, b)
# Gaps section after the balance sheet's closing tag, before Readable versions
anchor = '<section>\n  <h2>Readable versions</h2>'
gaps = '''<section>
  <h2>What everyone missed</h2>
  <p>Seven gaps no party (including this audit) had addressed, each backed by re-runnable search counts and fact-checked. Main beneficiary: two-sided 3 · critics 3 · Day 1.</p>
  <ol class="next">
    <li><b>GAP-01 adaptive fraction</b> (both): cuts Day's 17.5M by 20×–6,000×, yet the adaptive count still exceeds Haldane's rate by 1.5–7× on coding sites alone.</li>
    <li><b>GAP-04 finite-map cap</b> (both): Weissman &amp; Barton 2012. About 4× over the cap if every difference were adaptive; negligible at realistic adaptive rates.</li>
    <li><b>GAP-02 sweep signatures</b> (both), <b>GAP-03</b> linkage and the neutral rate (critics), <b>GAP-05</b> slightly harmful fixations (Day), <b>GAP-06</b> μ and generation time in the fit (critics, weakly), <b>GAP-07</b> indel/SV event counts (critics, modestly).</li>
  </ol>
</section>

'''
assert s.count(anchor) == 1
s = s.replace(anchor, gaps + anchor)
open(p, 'w').write(s)
print("ok")
# second pass: open E and G, log review #5
s = open(p).read()
for bid in ('E', 'G'):
    a = f'<details class="br">\n      <summary><span class="bid">{bid}</span>'
    assert s.count(a) == 1, bid
    s = s.replace(a, f'<details class="br" open>\n      <summary><span class="bid">{bid}</span>')
a = '<li><b>Done:</b> merged and committed (54 verdict fields across 33 claims)</li>'
assert s.count(a) == 1
s = s.replace(a, a + '\n      <li><b>Done:</b> review #5 (E, G1, gap ledger): E split into "size holds, route wrong, consequence untested"; G1 reworded ("reverse-engineered" dropped); the audit\'s own 14.7× objection withdrawn; verdicts applied to 16 claims</li>')
open(p, 'w').write(s)
print("ok2")
