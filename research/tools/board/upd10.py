# 2026-10-09: GAP-04/07/02 (review #6) and H3 (review #7) integrated; four side checks in flight (196 claims)
p = 'status.html'; s = open(p).read()
R = [
 ('status as of 2026-10-08</div>', 'status as of 2026-10-09</div>'),
 ('<span>194 claim files</span>', '<span>196 claim files</span>'),
 ('<i style="width:88%"></i></div><span>~88%, E and G1 reviewed; H, D, C1b left</span>',
  '<i style="width:93%"></i></div><span>~93%, H3 and three gaps reviewed; D, C1c, GAP-07b running</span>'),
 ('<span><b>194</b> claims (day 106 · critic 47 · ally 15 · lit 26)</span><span><b>238</b> typed objections</span><span><b>178</b> dated argument versions</span>',
  '<span><b>196</b> claims (day 108 · critic 47 · ally 15 · lit 26)</span><span><b>258</b> typed objections</span><span><b>185</b> dated argument versions</span>'),
 ('<b>95</b> holds · <b>15</b> non-sequitur · <b>6</b> arithmetic error · <b>55</b> pending',
  '<b>96</b> holds · <b>15</b> non-sequitur · <b>6</b> arithmetic error · <b>56</b> pending'),
 ('<b>21</b> supported · <b>101</b> contested · <b>9</b> contradicted · <b>5</b> untestable · <b>47</b> pending',
  '<b>22</b> supported · <b>102</b> contested · <b>9</b> contradicted · <b>5</b> untestable · <b>47</b> pending'),
 ('<b>37</b> accurate · <b>31</b> partial · <b>9</b> misread · <b>35</b> unverifiable · <b>9</b> pending</span>',
  '<b>37</b> accurate · <b>32</b> partial · <b>9</b> misread · <b>35</b> unverifiable · <b>9</b> pending</span>'),
 ('verdicts applied to 16 claims</li>',
  'verdicts applied to 16 claims</li>\n'
  '      <li><b>Done:</b> review #6 (GAP-04/07/02): a cap bracket R/4–R/2–simulated max replaces a single cap; "supply-infeasible" and the scan "tension" withdrawn; Day\'s all-fixations model shown alongside</li>\n'
  '      <li><b>Done:</b> review #7 (H3): long-run runs on na-workhorse replace the 10k window ("1/300 reproduced" withdrawn); every verdict made conditional on hard vs soft selection; the K = 1000 hard-load extinction found to be an artefact</li>'),
 ('<li data-s="ok"><span class="id">H8</span><span class="claim"><span class="c">Hössjer\'s 15,800</span><span class="f">10.5× Haldane\'s own figure. Day\'s Term 3 differs from Haldane\'s cost by 17.1× at the same d.</span></span></li>',
  '<li data-s="ok"><span class="id">H8</span><span class="claim"><span class="c">Hössjer\'s 15,800</span><span class="f">10.5× Haldane\'s own figure. Day\'s Term 3 differs from Haldane\'s cost by 17.1× at the same d.</span></span></li>\n'
  '        <li data-s="ok"><span class="id">H3</span><span class="claim"><span class="c">Cost of selection at human scale (reviewed; conditional on hard adaptive selection + soft load)</span><span class="f">Day\'s structure holds: concurrent sweeps share one budget. At Haldane\'s assumed R ≈ 1.1 the long-run rate is ≈ 1/530–1/1,050, below 1/300. The budget is ln R, not 10%: 10³ / 10⁴ adaptive substitutions need R ≈ 1.2 / 3.0, so a coding-only count fits; a 1% adaptive non-coding share does not. Day\'s 17.5M–205M fail under any cost model. The flip (0.01–0.6% non-coding) is below what any α estimate resolves, and R is unsourced, so H stays open.</span></span></li>'),
 ('<li><b>GAP-04 finite-map cap</b> (both): Weissman &amp; Barton 2012. About 4× over the cap if every difference were adaptive; negligible at realistic adaptive rates.</li>',
  '<li><b>GAP-04 finite-map cap</b> (both; checked): Day\'s 17.5–20M is 6.5–9.1× over R/4 and 3.3–4.5× over R/2 if all adaptive, but 0.54–0.76 of the simulated maximum; the adaptive count stays under the cap until 13–27% of differences are adaptive.</li>\n'
  '    <li><b>GAP-07 event counts</b> (critics, modestly; checked): 205M base pairs ≈ 9–11× the event count; Day\'s SNV-only magnitudes corroborated. A direct alignment count is running.</li>\n'
  '    <li><b>GAP-02 sweep window</b> (both; checked): Day\'s 3,200 sweeps predict ≤ ~98 detectable today; the top of his range (32,000) ~1,000–3,250. Verdict pending (range-dependent).</li>'),
 ('<li><b>GAP-02 sweep signatures</b> (both), <b>GAP-03</b>', '<li><b>GAP-03</b>'),
 ('<b>GAP-07</b> indel/SV event counts (critics, modestly).</li>', 'open.</li>'),
 ('<li>Seven dated milestone posts, linked from the handoff.</li>', '<li>Eight dated milestone posts, linked from the handoff.</li>'),
 ('238 objections typed undermining / undercutting / rebutting, a genealogy of 178 dated versions',
  '258 objections typed undermining / undercutting / rebutting, a genealogy of 185 dated versions'),
 ('<li><b>H at human scale</b>, bounded by the adaptive fraction (GAP-01: 10³–10⁶ selected changes), with a Nei / Felsenstein analytic cross-check.</li>\n    <li>Quick gap checks: Weissman–Barton finite-map cap (GAP-04), indel/SV event counts (GAP-07), sweep-scan windows (GAP-02).</li>\n    <li>D (sequence space): how many interchangeable routes per needed change. Then C1b call depth, H confidence intervals, Yoo\'s μ.</li>',
  '<li><b>Running now</b> (pre-registered; three reviews each when done): D spike (RNA folding + deep mutational scans: routes per needed change vs G1\'s 12–17), C1c (Day\'s aDNA "21" with real per-site coverage and ancestry turnover), GAP-07b (direct event count from the human–chimp alignment), corpus refresh since 2026-10-07.</li>\n'
  '    <li>H follow-ups: soft-selection rate limit and epistasis at human R; a sourced beneficial DFE; confidence intervals on T50. Then Yoo\'s μ / GAP-06.</li>'),
]
for a, b in R:
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)
open(p, 'w').write(s)
print("ok")
# second pass: in-flight checks shown as running
s = open(p).read()
R2 = [
 ('<li data-s="todo"><span class="id">D-sim</span><span class="claim"><span class="c">Sequence-space search simulations</span><span class="f">Specified, not started.</span></span></li>',
  '<li data-s="run"><span class="id">D1</span><span class="claim"><span class="c">Spike: interchangeable routes per needed change</span><span class="f">Running (pre-registered): RNA folding (ViennaRNA neutral networks) and deep mutational scans (MaveDB / ProteinGym), measured against G1\'s 12–17 threshold; engages Day\'s "DMS shows ruggedness" (D2h).</span></span></li>\n'
  '        <li data-s="todo"><span class="id">D-sim</span><span class="claim"><span class="c">Sequence-space search simulations</span><span class="f">Specified; follows the D1 spike.</span></span></li>'),
 ('<li data-s="ok"><span class="id">C6</span>',
  '<li data-s="run"><span class="id">C1c</span><span class="claim"><span class="c">Day\'s "21" with real per-site coverage and ancestry turnover</span><span class="f">Running (pre-registered): per-site, per-bin call depth from AADR plus the steppe and Anatolian farmer pulses.</span></span></li>\n'
  '        <li data-s="ok"><span class="id">C6</span>'),
]
for a, b in R2:
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)
open(p, 'w').write(s)
print("ok2")
# third pass: keep side-panel lists top-aligned when the neighbouring panel grows
s = open(p).read()
a = '.side{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:14px 16px;display:grid;gap:10px;min-width:0}'
assert s.count(a) == 1
s = s.replace(a, a[:-1] + ';align-content:start}')
open(p, 'w').write(s)
print("ok3")
