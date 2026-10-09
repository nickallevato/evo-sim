# 2026-10-09: GAP-07b (review #8) and the 2026-10-09 corpus refresh integrated; D1 and C1c still running (204 claims)
p = 'status.html'; s = open(p).read()
R = [
 ('<span>196 claim files</span>', '<span>204 claim files</span>'),
 ('<i style="width:93%"></i></div><span>~93%, H3 and three gaps reviewed; D, C1c, GAP-07b running</span>',
  '<i style="width:94%"></i></div><span>~94%, H3, four gaps and GAP-07b reviewed; D, C1c running</span>'),
 ('<span><b>196</b> claims (day 108 · critic 47 · ally 15 · lit 26)</span><span><b>258</b> typed objections</span><span><b>185</b> dated argument versions</span>',
  '<span><b>204</b> claims (day 112 · critic 51 · ally 15 · lit 26)</span><span><b>271</b> typed objections</span><span><b>192</b> dated argument versions</span>'),
 ('<b>96</b> holds · <b>15</b> non-sequitur · <b>6</b> arithmetic error · <b>56</b> pending',
  '<b>101</b> holds · <b>17</b> non-sequitur · <b>6</b> arithmetic error · <b>57</b> pending'),
 ('<b>22</b> supported · <b>102</b> contested · <b>9</b> contradicted · <b>5</b> untestable · <b>47</b> pending',
  '<b>24</b> supported · <b>102</b> contested · <b>9</b> contradicted · <b>5</b> untestable · <b>52</b> pending'),
 ('<b>37</b> accurate · <b>32</b> partial · <b>9</b> misread · <b>35</b> unverifiable · <b>9</b> pending</span>',
  '<b>36</b> accurate · <b>33</b> partial · <b>9</b> misread · <b>35</b> unverifiable · <b>11</b> pending</span>'),
 ('the K = 1000 hard-load extinction found to be an artefact</li>',
  'the K = 1000 hard-load extinction found to be an artefact</li>\n'
  '      <li><b>Done:</b> review #8 (GAP-07b): a single 9.7× replaced by a stated bracket (~7–14×); Day\'s own weighting rationale (04-28, 05-13) added and tested; "SNV-only is a floor" withdrawn; the audit\'s own 22.5M upper bound retired; critics\' numbers graded against the measurement</li>\n'
  '      <li><b>Done:</b> corpus refresh since 2026-10-07: both sides quiet; 8 new claims from comment threads and one Zenodo draft, 4 per side (Matev ×3 and keruru; Day\'s 2nd-edition 1,400 / 1,587, "selection ended ~1800", "extinct within centuries", "no drift in 7,000 years")</li>'),
 ('<span class="f">"410 Mb" not found in Yoo 2025 (average is 327 Mb per lineage). 205M counts base pairs, not mutation events.</span></span></li>',
  '<span class="f">"410 Mb" not found in Yoo 2025 (average is 327 Mb per lineage). 205M counts base pairs, not mutation events.</span></span></li>\n'
  '        <li data-s="ok"><span class="id">GAP-07b</span><span class="claim"><span class="c">Direct event count from the human–chimp alignment (reviewed)</span><span class="f">hg38 vs panTro6 (non-T2T): 37.8M SNVs + 4.3M indel events = 42.1M, 21.05M per lineage. 205M is 9.7× (bracket ~7–14×). For Day: his SNV-only 17.5M brackets the polymorphism-corrected count (16.4–18.1M), and his base-pair total is the right order for non-aligned sequence. His stated position is a weighting claim; as a weight 205M needs ~3,250 SNV-equivalents per large event (untested).</span></span></li>'),
 ('<li><b>GAP-07 event counts</b> (critics, modestly; checked): 205M base pairs ≈ 9–11× the event count; Day\'s SNV-only magnitudes corroborated. A direct alignment count is running.</li>',
  '<li><b>GAP-07 event counts</b> (critics, modestly; checked, then counted directly): 205M base pairs ≈ 9.7× the 21M events per lineage in the human–chimp alignment (bracket ~7–14×); Day\'s SNV-only figure is close to the event count. Next: GAP-07c (polymorphic share) and a T2T re-run.</li>'),
 ('258 objections typed undermining / undercutting / rebutting, a genealogy of 185 dated versions',
  '271 objections typed undermining / undercutting / rebutting, a genealogy of 192 dated versions'),
 ('<li><b>Running now</b> (pre-registered; three reviews each when done): D spike (RNA folding + deep mutational scans: routes per needed change vs G1\'s 12–17), C1c (Day\'s aDNA "21" with real per-site coverage and ancestry turnover), GAP-07b (direct event count from the human–chimp alignment), corpus refresh since 2026-10-07.</li>',
  '<li><b>Running now</b> (pre-registered; three reviews each when done): D spike (RNA folding + deep mutational scans: routes per needed change vs G1\'s 12–17), C1c (Day\'s aDNA "21" with real per-site coverage and ancestry turnover).</li>\n'
  '    <li>Queued from GAP-07b and the refresh: the polymorphic share of the alignment differences (GAP-07c), a T2T re-run, and an independent replication of keruru\'s measured Nₑ (B2e) before the Hard Limits verdict can move.</li>'),
]
for a, b in R:
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)
open(p, 'w').write(s)
print("ok")
