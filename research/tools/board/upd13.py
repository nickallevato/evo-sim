# 2026-10-09: X1 (review #12, with a blind rule audit) and GAP-07c (review #13) integrated; mapping round; Holocene N_e retrieved; XT and D15 running
p = 'status.html'; s = open(p).read()
R = [
 ('<i style="width:96%"></i></div><span>~96%, 27 checks reviewed (C1c, C1d, D1 added); X1, GAP-07c, XT, D15 in progress</span>',
  '<i style="width:97%"></i></div><span>~97%, 29 checks reviewed (X1, GAP-07c added); every critic and ally argument mapped; XT, D15 running</span>'),
 ('<span><b>204</b> claims (day 112 · critic 51 · ally 15 · lit 26)</span><span><b>293</b> typed objections</span><span><b>196</b> dated argument versions</span>',
  '<span><b>217</b> claims (day 115 · critic 61 · ally 15 · lit 26)</span><span><b>335</b> typed objections</span><span><b>203</b> dated argument versions</span>'),
 ('<b>102</b> holds · <b>17</b> non-sequitur · <b>6</b> arithmetic error · <b>56</b> pending',
  '<b>109</b> holds · <b>18</b> non-sequitur · <b>2</b> arithmetic error · <b>64</b> pending'),
 ('<b>26</b> supported · <b>103</b> contested · <b>11</b> contradicted · <b>4</b> untestable · <b>48</b> pending',
  '<b>26</b> supported · <b>103</b> contested · <b>11</b> contradicted · <b>6</b> untestable · <b>59</b> pending'),
 ('<b>36</b> accurate · <b>33</b> partial · <b>9</b> misread · <b>35</b> unverifiable · <b>11</b> pending',
  '<b>39</b> accurate · <b>34</b> partial · <b>9</b> misread · <b>53</b> unverifiable · <b>22</b> pending'),
 ('      <li><b>Done:</b> A3 (the required-fixation count) marked load-bearing: 31 nodes including ROOT</li>',
  '      <li><b>Done:</b> A3 (the required-fixation count) marked load-bearing: 31 nodes including ROOT</li>\n'
  '      <li><b>Done:</b> review #12 (X1, three reviews plus a blind audit of the verdict rule) and review #13 (GAP-07c): one rule now scores both sides; three Day error verdicts withdrawn under it (A3a, G, F), one added (A5h, the §6.4 38,400 slip), one critic claim now "doesn\'t follow" (B5c); the audit\'s own keruru figure found 41× low and corrected</li>\n'
  '      <li><b>Done:</b> mapping: every critic and ally argument attached ("mapped" ratified); 12 new claims from the Hancock video (pending review); 27 objections and 3 untested Hancock-slip rows added; Holocene Nₑ literature retrieved (does not decide C1c)</li>'),
 ('<span class="f">hg38 vs panTro6 (non-T2T): 37.8M SNVs + 4.3M indel events = 42.1M, 21.05M per lineage. 205M is 9.7× (bracket ~7–14×). For Day: his SNV-only 17.5M brackets the polymorphism-corrected count (16.4–18.1M), and his base-pair total is the right order for non-aligned sequence. His stated position is a weighting claim; as a weight 205M needs ~3,250 SNV-equivalents per large event (untested).</span></span></li>',
  '<span class="f">hg38 vs panTro6 (non-T2T): 37.8M SNVs + 4.3M indel events = 42.1M, 21.05M per lineage. 205M is 9.7× (bracket ~7–14×). For Day: his SNV-only 17.5M brackets the polymorphism-corrected count (16.4–18.1M), and his base-pair total is the right order for non-aligned sequence. His stated position is a weighting claim; as a weight 205M needs ~3,250 SNV-equivalents per large event (untested).</span></span></li>\n'
  '        <li data-s="ok"><span class="id">GAP-07c</span><span class="claim"><span class="c">How many differences are still variable in humans (reviewed)</span><span class="f">1000 Genomes: 15.6% of human-lineage single-letter differences still polymorphic (CSAC 14–22%); indels 7–9%, SVs ~7%; chimp side assumed. Fixed events 17.2–17.9M per lineage, so 205M is 10.6–12.6× fixed events (about 8–13× combined). For Day: 84% fixed; large variants mostly fixed. Like for like, his 17.5M is 10% above the fixed single-letter count.</span></span></li>'),
 ('<section>\n  <h2>What everyone missed</h2>',
  '<section>\n  <h2>Auditing the audit: one rule for both sides (X1)</h2>\n'
  '  <p>The audit\'s first synthesis counted 22 of Day\'s 112 claims with an "arithmetic error" or "doesn\'t follow" verdict and 0 of the critics\' 51. X1 recomputed every critic and ally number, wrote one verdict rule for both sides (one slip test, the author\'s own basis, a 25% line, charity tried everywhere), re-scored every numeric claim, and had the rule checked blind.</p>\n'
  '  <ol class="next">\n'
  '    <li><b>Primary measure</b> (claims with a number in the author\'s quoted words): Day 13 of 81, critics 1 of 20, p = 0.29.</li>\n'
  '    <li><b>Formal-statement measure:</b> 16 of 82 vs 1 of 31, p = 0.038. <b>All claims:</b> 18 of 114 vs 1 of 51, p = 0.008. Per 10,000 quoted words: Day 22.7, critics 10.0.</li>\n'
  '    <li><b>Sensitivity:</b> if three close critic calls went the other way, 16 of 82 vs 4 of 31, p = 0.58. Day\'s errors hold up under any reading; the audit cannot claim critics err less per argument.</li>\n'
  '  </ol>\n'
  '</section>\n\n'
  '<section>\n  <h2>What everyone missed</h2>'),
 ('205M base pairs ≈ 9.7× the 21M events per lineage in the human–chimp alignment (bracket ~7–14×);',
  '205M base pairs ≈ 9.7× the 21M events per lineage in the human–chimp alignment (bracket ~7–14×), and 10.6–12.6× the fixed events once still-variable sites are removed (GAP-07c);'),
 ('<li>Nine dated milestone posts, linked from the handoff.</li>', '<li>Ten dated milestone posts, linked from the handoff.</li>'),
 ('293 objections typed undermining / undercutting / rebutting, a genealogy of 196 dated versions',
  '335 objections typed undermining / undercutting / rebutting, a genealogy of 203 dated versions'),
 ('<li><b>In progress:</b> X1, an arithmetic audit of every critic and ally number plus one written verdict rule applied to both sides (fix pass done; a blind audit of the rule\'s application running); GAP-07c, the polymorphic share (15.6% of human-derived differences; reviews running); XT, core results re-run in fwdpy11; D15, Hössjer\'s regulatory waiting time; the Holocene Nₑ retrieval that decides the C1c reading; mapping the 41 unplaced critic and ally arguments.</li>',
  '<li><b>In progress</b> (one at a time, on na-workhorse): XT, core results re-run in fwdpy11; D15, Hössjer\'s regulatory waiting time.</li>\n'
  '    <li><b>Queued:</b> C1e (the C1c model on each published Holocene trajectory); Mansfield\'s supply argument; latency vs throughput (the in-transit count is assumed, not measured); Hancock\'s standing-variation prediction; reviews of the 12 new mapping claims.</li>'),
]
for a, b in R:
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)
open(p, 'w').write(s)
print("ok")
