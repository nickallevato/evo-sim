# 2026-10-11: A2e-alpha, GAP-06, GAP-07t (#51-#55), refresh + test-methods review, Day's dN/dS post: L1, L6, L7 (#56-#60); HF in progress; post 13
p = 'status.html'; s = open(p).read()
R = [
 ('<span>~98%, 47 checks reviewed (FM mesa replication, B3m, H8 kscale64 added); next: XT follow-up, review of the 12 mapping claims, RH pass</span>',
  '<span>~98%, 48 checks reviewed (A2e-alpha, GAP-06, GAP-07t, L1, L6, L7 added); HF post hoc run <code>ph</code> in progress (workhorse + builder, ~31 h); next: L1b T2T rerun, HF integration</span>'),
 ('<span><b>225</b> claims (day 123 · critic 61 · ally 15 · lit 26)</span><span><b>401</b> typed objections</span><span><b>222</b> dated argument versions</span>',
  '<span><b>232</b> claims</span><span><b>419</b> typed objections</span><span><b>232</b> dated argument versions</span>'),
 ('<b>115</b> holds · <b>18</b> non-sequitur · <b>2</b> arithmetic error · <b>62</b> pending',
  '<b>130</b> holds · <b>19</b> non-sequitur · <b>2</b> arithmetic error · <b>52</b> pending'),
 ('<b>32</b> supported · <b>106</b> contested · <b>13</b> contradicted · <b>6</b> untestable · <b>56</b> pending',
  '<b>34</b> supported · <b>115</b> contested · <b>16</b> contradicted · <b>6</b> untestable · <b>49</b> pending'),
 ('<b>41</b> accurate · <b>34</b> partial · <b>10</b> misread · <b>54</b> unverifiable · <b>22</b> pending',
  '<b>43</b> accurate · <b>38</b> partial · <b>10</b> misread · <b>58</b> unverifiable · <b>12</b> pending'),
 ('      <li><b>Done:</b> mapping: every critic and ally argument attached',
  '      <li><b>Done:</b> reviews #51-#55 (GAP-06, GAP-07t, A2e-alpha): T2T events 24.14 M per lineage (+14.7%, 205 M bp is 8.5x raw); Yoo mu and g move no number by 25%; bias-corrected alpha (Boyko, Eyre-Walker) all above the ~191 flip, so A2e external is contested, leaning contradicted; Gayà-Vidal 29-49 and the "100-fold disagreement" withdrawn</li>\n'
  '      <li><b>Done:</b> reviews #56-#60 (L1 load-bearing, L6, L7 combined): Day\'s dN/dS 0.80 not reproduced (Ensembl one2one 0.207, all genes 0.271, 32 filter stacks 0.23-0.28); "ten of twelve" and 410 M (as bp) reproduce; frame-error attribution, 0.70-0.91, the 0.83 base rate withdrawn as audit errors</li>\n'
  '      <li><b>In progress:</b> HF (H follow-ups): main run finished, three reviews done (0 BLOCKER, 10 MAJOR); post hoc run <code>ph</code> (410 jobs) on na-workhorse + builder, ~31 h. Findings provisional until scored.</li>\n'
  '      <li><b>Done:</b> mapping: every critic and ally argument attached'),
 ('<section>\n  <h2>What everyone missed</h2>',
  '<section>\n  <h2>Day\'s dN/dS post (2026-10-11): checked</h2>\n'
  '  <p>"How Biologists Keep \'Proving\' Selection" reports dN/dS 0.80 on 20,400 GENCODE v46 genes against the Consortium\'s 0.23 on 13,454, and adds LTEE and Yoo 2025 claims. Day\'s own test (Q176: same pipeline, two gene sets) is valid and discriminating; the audit ran its analogue. Milestone 13.</p>\n'
  '  <ol class="next">\n'
  '    <li><b>L1 (dN/dS, load-bearing):</b> Nei-Gojobori pooled 0.207 on Ensembl one2one genes, 0.271 on all genes (0.447 on the rest); 32 filter stacks give 0.23-0.28; 0.80 is not reproduced. A gene-set effect exists in Day\'s direction (+0.06, +31%, material). His single-SNV count (2.52 nonsynonymous per synonymous vs 0.85 on correct CDS) points to an unidentified extraction or alignment problem. DN1, DN2 contradicted; DN3 holds / pending / contradicted; DN4 non-sequitur (rule N); DN5 supported. Open: L1b T2T rerun.</li>\n'
  '    <li><b>L6 ("ten of twelve"):</b> reproduces on his rule, 10 of 12 populations; 28 of 29 cells match. Good\'s own fixed calls never fall, but the fixed state is never left. Of 972 exits, 34% return, 62% hover, 4.6% are lost. E10 holds / partial / contested.</li>\n'
  '    <li><b>L7 (410 M vs 35 M):</b> reproduces as base pairs (404.2-412.7 M, SI III.14 x III.19), about 8.5x the T2T event count; Day\'s locator is accurate. A3z holds / partial / contested.</li>\n'
  '    <li><b>Audit corrections:</b> the frame-error attribution, the 0.70-0.91 figure, the 0.83 base rate, the Gayà-Vidal 29-49 count and the "100-fold disagreement" are withdrawn.</li>\n'
  '  </ol>\n</section>\n\n<section>\n  <h2>What everyone missed</h2>'),
 ('<li>Twelve dated milestone posts, linked from the handoff.</li>', '<li>Thirteen dated milestone posts, linked from the handoff.</li>'),
 ('401 objections typed undermining / undercutting / rebutting, a genealogy of 222 dated versions',
  '419 objections typed undermining / undercutting / rebutting, a genealogy of 232 dated versions'),
 ('    <li>Queued: a transversion-matched neutral model for Day\'s 21; a T2T re-run of the event count; the remaining load-bearing claims without a reviewed check (R5 draft).</li>',
  '    <li>Queued: <b>L1b</b> T2T rerun of the dN/dS check (after HF <code>ph</code>); fetch tasks (CSAC 2005 and an independent ML dN/dS; Good 2017 SI 5.2; Uricchio full text; Day\'s per-gene table); a transversion-matched neutral model for Day\'s 21; the remaining load-bearing claims without a reviewed check (R5 draft).</li>'),
 ('    <li>H follow-ups: soft-selection rate limit and epistasis at human R; a sourced beneficial DFE; confidence intervals on T50. Then Yoo\'s μ / GAP-06.</li>',
  '    <li><b>In flight:</b> HF post hoc run <code>ph</code> (long burn, cap release, mix boundary, noisy truncation) on workhorse + builder, ~31 h; then score, fix pass and integrate HF.</li>'),
]
for a, b in R:
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)
open(p, 'w').write(s)
print("ok")
