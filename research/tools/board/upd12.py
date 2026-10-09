# 2026-10-09: C1c (review #9), C1d (review #10) and D1 (review #11) integrated; A3 load-bearing; X1, GAP-07c, XT, D15, Holocene N_e, mapping in progress
p = 'status.html'; s = open(p).read()
R = [
 ('<i style="width:94%"></i></div><span>~94%, H3, four gaps and GAP-07b reviewed; D, C1c running</span>',
  '<i style="width:96%"></i></div><span>~96%, 27 checks reviewed (C1c, C1d, D1 added); X1, GAP-07c, XT, D15 in progress</span>'),
 ('<span><b>271</b> typed objections</span><span><b>192</b> dated argument versions</span>',
  '<span><b>293</b> typed objections</span><span><b>196</b> dated argument versions</span>'),
 ('<b>101</b> holds · <b>17</b> non-sequitur · <b>6</b> arithmetic error · <b>57</b> pending',
  '<b>102</b> holds · <b>17</b> non-sequitur · <b>6</b> arithmetic error · <b>56</b> pending'),
 ('<b>24</b> supported · <b>102</b> contested · <b>9</b> contradicted · <b>5</b> untestable · <b>52</b> pending',
  '<b>26</b> supported · <b>103</b> contested · <b>11</b> contradicted · <b>4</b> untestable · <b>48</b> pending'),
 ('"no drift in 7,000 years")</li>',
  '"no drift in 7,000 years")</li>\n'
  '      <li><b>Done:</b> reviews #9–#11 (C1c, C1d, D1): C1c\'s "thousands" from capture heterogeneity withdrawn (design flaw); C1d ran Day\'s documented two-period pipeline (3.6× off), a library-type damage test (not damage) and keruru\'s census sensitivity; D1 shown along an axis of readings, two fired pre-registered triggers acknowledged, "Day\'s m ≈ 1" (the audit\'s own wording) and pooled counts withdrawn</li>\n'
  '      <li><b>Done:</b> A3 (the required-fixation count) marked load-bearing: 31 nodes including ROOT</li>'),
 ('<span class="f">Verdict: not reproducible, cannot adjudicate. The model misses Day\'s own table, so it isn\'t a valid null. Likely cause found: real ancient samples give only a few calls per site in old bins. Lowering per-site coverage drops the neutral count from ~6,500 to ~120 and moves events into the oldest bin, the same direction as Day\'s table. A direction, not yet a reproduction.</span>',
  '<span class="f">Verdict: not reproducible, cannot adjudicate. Its suspected cause (few calls per site in old bins) was refuted by C1c: mean depth is 49 / 62 / 282 chromosomes in the three oldest bins. Superseded by C1c and C1d.</span>'),
 ('<li data-s="run"><span class="id">C1c</span><span class="claim"><span class="c">Day\'s "21" with real per-site coverage and ancestry turnover</span><span class="f">Running (pre-registered): per-site, per-bin call depth from AADR plus the steppe and Anatolian farmer pulses.</span></span></li>',
  '<li data-s="ok"><span class="id">C1c</span><span class="claim"><span class="c">Day\'s "21" with real per-site coverage and ancestry turnover (reviewed)</span><span class="f">Model-conditional. At the textbook Nₑ ≈ 10⁴ neutral predicts 1,500–3,900 post-6000 events, 70–190× the 21 (for Day); closed Nₑ ~10⁵ or growth to 10⁶ gives 15–67 (for the critics). Day\'s d = 0.45 gives 739. No setting reproduces his table. Turns on the Holocene Nₑ, which nobody has sourced (retrieval running).</span></span></li>\n'
  '        <li data-s="ok"><span class="id">C1d</span><span class="claim"><span class="c">Day\'s statistic on the real AADR genotypes (reviewed)</span><span class="f">His stated method gives 62,757 eligible / 4,957 post-6000 events (v62) against 22,428 / 21; his own documented two-period pipeline reproduces his sample and SNP count but is 3.6× off on events; no code found. The excess is 98% transitions but not damage (library test). For Day: start table to 0.4 points; transversions alone 36–44. keruru\'s Nₑ replicates within 4% (his sampling term is halved, a minor slip); Day\'s Nₑ ≈ 2 is excluded. C6 and C7 now contradicted as stated.</span></span></li>'),
 ('<li data-s="ok"><span class="id">C6</span><span class="claim"><span class="c">The 630 comparator</span><span class="f">Day\'s comparison and this audit\'s earlier rescaling are both wrong. About 1,500–1,850 fixations are expected on an ascertained panel.</span></span></li>',
  '<li data-s="ok"><span class="id">C6</span><span class="claim"><span class="c">The 630 comparator, and the 21 itself</span><span class="f">Day\'s comparison and this audit\'s earlier rescaling are both wrong. About 1,500–1,850 fixations are expected on an ascertained panel. External verdict now <i>contradicted</i> as stated (C1d); his best reading is "underspecified", and it reopens as contested if he documents a pipeline.</span></span></li>'),
 ('<li data-s="run"><span class="id">D1</span><span class="claim"><span class="c">Spike: interchangeable routes per needed change</span><span class="f">Running (pre-registered): RNA folding (ViennaRNA neutral networks) and deep mutational scans (MaveDB / ProteinGym), measured against G1\'s 12–17 threshold; engages Day\'s "DMS shows ruggedness" (D2h).</span></span></li>',
  '<li data-s="ok"><span class="id">D1</span><span class="claim"><span class="c">Spike: interchangeable routes per needed change (reviewed)</span><span class="f">Per locus, about 1–6 routes (exact RNA structure 1.5–2.3; beneficial per protein site 0.21): below G1\'s flip, so Day\'s multiplication holds there. Per gene, a shared pool of ~51 beneficial mutations clears the flip for ~10 needed changes, not 25+. For Day: GB1 95% nonfunctional and rugged at single-letter steps; "reduce or destroy" holds as worded (61%). For the critics: 71% of singles keep function, "destroy" rare (2%), GB1 one connected network. Prevalence among random sequences (Axe, Taylor) untouched.</span></span></li>'),
 ('<li data-s="todo"><span class="id">D-sim</span><span class="claim"><span class="c">Sequence-space search simulations</span><span class="f">Specified; follows the D1 spike.</span></span></li>',
  '<li data-s="run"><span class="id">D15</span><span class="claim"><span class="c">Hössjer: coordinated regulatory changes take far more than 9 My</span><span class="f">Running (pre-registered): Durrett–Schmidt / Lynch / Behe–Snoke baselines, then forward simulation over the number of mutations, target redundancy and intermediate fitness.</span></span></li>\n'
  '        <li data-s="todo"><span class="id">D-sim</span><span class="claim"><span class="c">Per-sequence prevalence and multi-mutant decay</span><span class="f">Axe / Taylor / Keefe–Szostak (literature and fidelity); ProteinGym multi-mutants; a noise null for the beneficial proxy.</span></span></li>'),
 ('Eight dated milestone posts, linked from the handoff.', 'Nine dated milestone posts, linked from the handoff.'),
 ('271 objections typed undermining / undercutting / rebutting, a genealogy of 192 dated versions',
  '293 objections typed undermining / undercutting / rebutting, a genealogy of 196 dated versions'),
 ('<li><b>Running now</b> (pre-registered; three reviews each when done): D spike (RNA folding + deep mutational scans: routes per needed change vs G1\'s 12–17), C1c (Day\'s aDNA "21" with real per-site coverage and ancestry turnover).</li>\n'
  '    <li>Queued from GAP-07b and the refresh: the polymorphic share of the alignment differences (GAP-07c), a T2T re-run, and an independent replication of keruru\'s measured Nₑ (B2e) before the Hard Limits verdict can move.</li>',
  '<li><b>In progress:</b> X1, an arithmetic audit of every critic and ally number plus one written verdict rule applied to both sides (fix pass done; a blind audit of the rule\'s application running); GAP-07c, the polymorphic share (15.6% of human-derived differences; reviews running); XT, core results re-run in fwdpy11; D15, Hössjer\'s regulatory waiting time; the Holocene Nₑ retrieval that decides the C1c reading; mapping the 41 unplaced critic and ally arguments.</li>\n'
  '    <li>Queued: a transversion-matched neutral model for Day\'s 21; a T2T re-run of the event count; the remaining load-bearing claims without a reviewed check (R5 draft).</li>'),
]
for a, b in R:
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)
open(p, 'w').write(s)
print("ok")

# second pass: R3 load-bearing count (A3 promoted)
s = open(p).read()
a, b = '<span>30 load-bearing nodes</span>', '<span>31 load-bearing nodes</span>'
assert s.count(a) == 1, a
open(p, 'w').write(s.replace(a, b))
print("ok 2")
