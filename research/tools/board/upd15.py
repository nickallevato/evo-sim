# 2026-10-10: FM mesa replication (reviews #43-#47), B3m (#48), H8 kscale64 (#49) integrated; post 12
p = 'status.html'; s = open(p).read()
R = [
 ('<span>~98%, 45 checks reviewed (XT, D15, H8/H5, A2e, B2/B, B3, B3g, F3a added); next: mesa replication (ROOT-FM), median-25 recomputation</span>',
  '<span>~98%, 47 checks reviewed (FM mesa replication, B3m, H8 kscale64 added); next: XT follow-up, review of the 12 mapping claims, RH pass</span>'),
 ('<span><b>218</b> claims (day 116 · critic 61 · ally 15 · lit 26)</span><span><b>386</b> typed objections</span><span><b>219</b> dated argument versions</span>',
  '<span><b>225</b> claims (day 123 · critic 61 · ally 15 · lit 26)</span><span><b>401</b> typed objections</span><span><b>222</b> dated argument versions</span>'),
 ('<b>113</b> holds · <b>18</b> non-sequitur · <b>2</b> arithmetic error · <b>61</b> pending',
  '<b>115</b> holds · <b>18</b> non-sequitur · <b>2</b> arithmetic error · <b>62</b> pending'),
 ('<b>29</b> supported · <b>102</b> contested · <b>12</b> contradicted · <b>6</b> untestable · <b>57</b> pending',
  '<b>32</b> supported · <b>106</b> contested · <b>13</b> contradicted · <b>6</b> untestable · <b>56</b> pending'),
 ('<b>40</b> accurate · <b>34</b> partial · <b>10</b> misread · <b>52</b> unverifiable · <b>22</b> pending',
  '<b>41</b> accurate · <b>34</b> partial · <b>10</b> misread · <b>54</b> unverifiable · <b>22</b> pending'),
 ('      <li><b>Done:</b> mapping: every critic and ally argument attached',
  '      <li><b>Done:</b> reviews #43-#47 (FM mesa replication; Opus, then a combined re-review and a light review): the description replicates but the pattern is shared across lineages; mirror test: the unmasked human excess follows the reference; chrX F1 hotspot is one window; \'sharp boundaries\' indeterminate; FM10 external contested (leaning critic), internal pending</li>\n'
  '      <li><b>Done:</b> reviews #48-#49 (B3m, H8 kscale64): \'median 25\' reproduces exactly from Bergeron 2023 Table 9 (terminal-branch vs lineage-average about 1.9×, gap unexplained); \'slower than 1/300\' shows no K trend to 64,000, the horizon matters</li>\n'
  '      <li><b>Done:</b> mapping: every critic and ally argument attached'),
 ('<h2>Day\'s "The Fourth Mechanism" (2026-10-10, ROOT-FM)</h2>',
  '<h2>Day\'s "The Fourth Mechanism" (2026-10-10, ROOT-FM): replicated</h2>'),
 ('Verdicts pending / pending / pending; a replication is queued.</li>',
  'Verdicts pending / pending / pending before the replication.</li>\n'
  '    <li><b>Replication (R4 FM, reviews #43-#47):</b> on the public T2T 8-way alignment, overdispersion above 80× (φ 93-136 at 1 Mb for human, chimp and gorilla) and clustering replicate, but they are shared across lineages; a shared-rate null reproduces 64-69% of human mesas; human mesas hold 1.25-2.5% of human-chimp SNV differences. Mirror test: the unmasked human excess follows the reference. One chrX F1 window (57.3 Mb, centromeric transition region) crosses Day\'s pre-registered 3× cut and is of unknown cause. \'Sharp boundaries\' indeterminate; a 2.3-2.7 residual is unattributed. ROOT-FM pending / pending / contested (leaning critic); FM10 internal pending on rule N2d.</li>'),
 ('<li>Eleven dated milestone posts, linked from the handoff.</li>', '<li>Twelve dated milestone posts, linked from the handoff.</li>'),
 ('386 objections typed undermining / undercutting / rebutting, a genealogy of 219 dated versions',
  '401 objections typed undermining / undercutting / rebutting, a genealogy of 222 dated versions'),
 ('    <li><b>Next check:</b> per-lineage mesa replication against a heterogeneous-μ neutral null (ROOT-FM, load-bearing tier, pre-register first); recompute "median 25 across 55 vertebrates" from Bergeron 2023 open data; XT follow-up (U-scaling rerun or SLiM).</li>\n',
  '    <li><b>Open:</b> FM10 internal (rule N2d); cause of the chrX 57.3 Mb window; the B3m 2-vs-25 gap; the Hard Limits peroration RH tag (owner); XT follow-up (U-scaling rerun or SLiM).</li>\n'),
]
for a, b in R:
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)
open(p, 'w').write(s)
print("ok")
