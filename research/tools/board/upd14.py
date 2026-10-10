# 2026-10-10: XT, G2c restore, D15, H8/H5, A2e, B3g, F3a, B2/B, B3 integrated (reviews #22-#42); Day's "The Fourth Mechanism" (ROOT-FM) scored; post 11
p = 'status.html'; s = open(p).read()
R = [
 ('<i style="width:97%"></i></div><span>~97%, 29 checks reviewed (X1, GAP-07c added); every critic and ally argument mapped; XT, D15 running</span>',
  '<i style="width:98%"></i></div><span>~98%, 45 checks reviewed (XT, D15, H8/H5, A2e, B2/B, B3, B3g, F3a added); next: mesa replication (ROOT-FM), median-25 recomputation</span>'),
 ('<span><b>217</b> claims (day 115 · critic 61 · ally 15 · lit 26)</span><span><b>335</b> typed objections</span><span><b>203</b> dated argument versions</span>',
  '<span><b>218</b> claims (day 116 · critic 61 · ally 15 · lit 26)</span><span><b>386</b> typed objections</span><span><b>219</b> dated argument versions</span>'),
 ('<b>109</b> holds · <b>18</b> non-sequitur · <b>2</b> arithmetic error · <b>64</b> pending',
  '<b>113</b> holds · <b>18</b> non-sequitur · <b>2</b> arithmetic error · <b>61</b> pending'),
 ('<b>26</b> supported · <b>103</b> contested · <b>11</b> contradicted · <b>6</b> untestable · <b>59</b> pending',
  '<b>29</b> supported · <b>102</b> contested · <b>12</b> contradicted · <b>6</b> untestable · <b>57</b> pending'),
 ('<b>39</b> accurate · <b>34</b> partial · <b>9</b> misread · <b>53</b> unverifiable · <b>22</b> pending',
  '<b>40</b> accurate · <b>34</b> partial · <b>10</b> misread · <b>52</b> unverifiable · <b>22</b> pending'),
 ('      <li><b>Done:</b> mapping: every critic and ally argument attached',
  '      <li><b>Done:</b> reviews #22-#25: XT (fwdpy11) replicates 1/2N, N<sub>e</sub> sets time, Kimura u and the B1c excess; some numeric rows show an unexplained U-dependent deficit (no verdict change); independent re-reviews of E5/E6, F1a, B2b (F1a: near-circular design noted)</li>\n'
  '      <li><b>Done:</b> reviews #26-#34 (D15, H8/H5, A2e; Opus, 0 blockers, 21 MAJOR answered): D15 scorecard re-scoped to Hössjer\'s own premises; H8 \'slower than 1/300\' made conditional on K (K = 16,000 run: 2 misses, 1 indeterminate, 1 hit); A2e flip point κ* 3.9-13,050 and the total-throughput basis added</li>\n'
  '      <li><b>Done:</b> reviews #35-#42 (B3g, F3a, B2/B, B3): B3d internal holds on Day\'s basis (the arithmetic-error draft was challenged under the author-basis rule), fidelity misread, external contradicted; B2 internal holds; B stays pending (RH tag of the peroration open); F3a internal holds</li>\n'
  '      <li><b>Done:</b> mapping: every critic and ally argument attached'),
 # nodes
 ('<span class="c">Hard Limits: P(fix within G) ≈ exp(−π²Nₑ/G)</span><span class="f">The exponent is correct. It bounds how long one allele takes, not the total rate of substitutions.</span>',
  '<span class="c">Hard Limits: P(fix within G) ≈ exp(−π²Nₑ/G) (reviewed against its own text)</span><span class="f">Internal holds: the exponent, the X algebra and Day\'s WF demonstration (exact mean 396.5 vs 391) reproduce; the asymptotic law understates the exact F by a 17.8-47× prefactor. On HL\'s own 6.5 My window and B1d the pipe is granted full. The peroration (B) stays pending on its RH tag.</span>'),
 ('<span class="c">k = μ · N / Nₑ</span><span class="f">Refuted: neutral fixation probability is 1/N in census terms, so k = μ.</span>',
  '<span class="c">k = μ · N / Nₑ and k = 32.3μ</span><span class="f">N/Nₑ leg refuted and withdrawn by Day (2026-08-27, B3g): k = μ. 32.3 reproduces from his inputs (32.93: 205 M bp over a point-mutation rate; holds on his basis) but events give 2.3-3.4 and like-for-like bp 0.4-0.6, so externally contradicted; Yoo attribution misread.</span>'),
 ('<li data-s="run"><span class="id">D15</span><span class="claim"><span class="c">Hössjer: coordinated regulatory changes take far more than 9 My</span><span class="f">Running (pre-registered): Durrett–Schmidt / Lynch / Behe–Snoke baselines, then forward simulation over the number of mutations, target redundancy and intermediate fitness.</span></span></li>',
  '<li data-s="ok"><span class="id">D15</span><span class="claim"><span class="c">Hössjer: coordinated regulatory changes take far more than 9 My (reviewed)</span><span class="f">714-cell sweep. Inside his stated premises (specific target, neutral or valley intermediates; 96 cells) P(done in 9 My) = 0: holds, fidelity accurate. Outside them it flips: +1% beneficial intermediates reach 9 My in 57-77% of runs at Nₑ = 1e4 and 100% at 1e5; also redundant sites, a non-specific gene set, and his Table 5 d_max = 1 rows. External contested (provisional); no critic engages it.</span></span></li>'),
 ('<span class="c">Hössjer\'s 15,800</span><span class="f">10.5× Haldane\'s own figure. Day\'s Term 3 differs from Haldane\'s cost by 17.1× at the same d.</span>',
  '<span class="c">Hössjer\'s 15,800; Haldane\'s 1/300 in Haldane\'s regime (H8/H5, reviewed)</span><span class="f">10.5× Haldane\'s own figure; Term 3 differs by 17.1× at the same d. 1/300 confirmed at R = 1.111, D = 30 (K = 1,000); budget size is ln R (16-21× from R = 1.111 to 3); 15,800 payable from R ≈ 2-2.7 (hard). Day\'s upper bound holds; his s_i sum fails under soft selection. \'Slower than 1/300\' is conditional on K, tested to 16,000.</span>'),
 ('    <details class="br" open>\n      <summary><span class="bid">B</span>',
  '    <details class="br" open>\n      <summary><span class="bid">B</span>'),
]
for a, b in R:
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)

# A2e node: append after A4
a = '    <details class="br" open>\n      <summary><span class="bid">B</span>'
i = s.index(a)
j = s.rindex('      </ul>', 0, i)
s = s[:j] + ('        <li data-s="ok"><span class="id">A2e</span><span class="claim"><span class="c">LTEE-to-human transfer sensitivity (reviewed)</span>'
 '<span class="f">Per generation, supply-limited: F ≤ 0.104 at κ = 1; at κ = 93,659 capped F 1.98-7.1. Flip point κ* 3.9-13,050 (central 217), a threshold on supply × beneficial fraction × effect size the check cannot set; decoupled effect sizes close the gap in 6 of 96 cells. On Day\'s total-throughput basis F = 50,765, conditional on k = μ. Internal non-sequitur, external contested (two dependencies).</span></span></li>\n') + s[j:]

# new section before "What everyone missed"
sec = ('<section>\n  <h2>Day\'s "The Fourth Mechanism" (2026-10-10, ROOT-FM)</h2>\n'
 '  <p>Day published the result of his T2T ape-genome analysis: substitution density is "massively overdispersed" and clusters into "mesas" with a human-lineage excess; sigillation (deliberate genomic modification) is proposed as a possible fourth mechanism, and selection and drift "can still be considered viable" [sic; in context "can no longer"]. Scored against the pre-registration committed before it appeared.</p>\n'
 '  <ol class="next">\n'
 '    <li><b>Released:</b> the data are public (T2T Primate Consortium; Progressive Cactus). <b>Not released:</b> code, mesa coordinates, window size, dispersion statistic, per-lineage counts, the "Haldane" figure, any Zenodo record.</li>\n'
 '    <li><b>Pre-registration score:</b> form A (T2T comparative genomics) partial hit; adaptive-share headline, total re-size and forward simulations missed; the predicted gap between "mesas exist" and "selection and drift not viable" is a hit pending the data; the note\'s "conclusively proven" prediction was too harsh (Day hedges). The note\'s form list lacked a distribution-of-substitutions variant.</li>\n'
 '    <li><b>For Day:</b> testable on public data, hedged, revises relictation downward. <b>For the critics:</b> overdispersion is the standard mark of mutation-rate heterogeneity, alignment error and ILS; only a human-specific excess discriminates; units not stated. Verdicts pending / pending / pending; a replication is queued.</li>\n'
 '  </ol>\n</section>\n\n<section>\n  <h2>What everyone missed</h2>')
a = '<section>\n  <h2>What everyone missed</h2>'
assert s.count(a) == 1
s = s.replace(a, sec)

R2 = [
 ('<li>Ten dated milestone posts, linked from the handoff.</li>', '<li>Eleven dated milestone posts, linked from the handoff.</li>'),
 ('335 objections typed undermining / undercutting / rebutting, a genealogy of 203 dated versions',
  '386 objections typed undermining / undercutting / rebutting, a genealogy of 219 dated versions'),
 ('<li><b>In progress</b> (one at a time, on na-workhorse): XT, core results re-run in fwdpy11; D15, Hössjer\'s regulatory waiting time.</li>\n'
  '    <li><b>Queued:</b> C1e (the C1c model on each published Holocene trajectory); Mansfield\'s supply argument; latency vs throughput (the in-transit count is assumed, not measured); Hancock\'s standing-variation prediction; reviews of the 12 new mapping claims.</li>',
  '    <li><b>Next check:</b> per-lineage mesa replication against a heterogeneous-μ neutral null (ROOT-FM, load-bearing tier, pre-register first); recompute "median 25 across 55 vertebrates" from Bergeron 2023 open data; XT follow-up (U-scaling rerun or SLiM).</li>\n'
  '    <li><b>Queued:</b> reviews of the 12 new mapping claims; the RH pass (including the Hard Limits peroration tag); E leftovers, GAP-03.</li>'),
]
for a, b in R2:
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)
open(p, 'w').write(s)
print("ok")
