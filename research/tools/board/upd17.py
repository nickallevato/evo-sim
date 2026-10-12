# 2026-10-12: rules RD/RH6; B9, RHclose, RHclose-critics, A2e-alpha addendum, GAP05 integrated; refresh 2026-10-12 (DN6, CSAC2005 methods);
# pre-registered not yet run: L1b, L5, L1c, FMnull; two figures (dN/dS predictions, mesa index null range)
import math
p = 'status.html'; s = open(p).read()

def fig_dnds():
    x = lambda v: 40 + v * 520
    r = lambda a, b, y, h, cls, t: ('<rect x="%.1f" y="%d" width="%.1f" height="%d" rx="3" class="%s"><title>%s</title></rect>'
                                    % (x(a), y, x(b) - x(a), h, cls, t))
    o = ['<svg class="fig" viewBox="0 0 600 205" role="img" aria-labelledby="f1t f1d" xmlns="http://www.w3.org/2000/svg">',
         '<title id="f1t">dN/dS: what each side predicts</title>',
         '<desc id="f1d">Horizontal axis from 0 to 1. Pre-registered L1c outcome bands for pooled dN/dS on all genes: critic band below 0.40, middle band 0.40 to 0.65, Day band at or above 0.65. Markers: the Chimpanzee Sequencing and Analysis Consortium 2005 value 0.23 and Day 2026 value 0.7989. Registered, not yet run.</desc>',
         '<text x="40" y="16" class="lbl b">L1c registered outcome bands (pooled dN/dS, all genes)</text>']
    o.append(r(0, 0.40, 28, 26, 'bc', 'Critic band: below 0.40 (also needs the CSAC-style subset below 0.40)'))
    o.append(r(0.40, 0.65, 28, 26, 'bm', 'Middle: 0.40 to under 0.65 (neither side range)'))
    o.append(r(0.65, 1.0, 28, 26, 'bd', 'Day band: 0.65 or above (plus nonsynonymous fraction and method-drop conditions)'))
    o.append('<text x="%.1f" y="45" class="lbl on" text-anchor="middle">CRITIC &lt; 0.40</text>' % x(0.20))
    o.append('<text x="%.1f" y="45" class="lbl on" text-anchor="middle">MIDDLE</text>' % x(0.525))
    o.append('<text x="%.1f" y="45" class="lbl on" text-anchor="middle">DAY &#8805; 0.65</text>' % x(0.825))
    o.append('<text x="40" y="76" class="lbl m">Predictions fixed in advance</text>')
    o.append(r(0.20, 0.35, 82, 10, 'pc', 'Critic prediction: 0.20 to 0.35 on all genes'))
    o.append('<text x="%.1f" y="91" class="lbl m">critic 0.20&#8211;0.35</text>' % (x(0.35) + 6))
    o.append(r(0.65, 1.0, 98, 10, 'pd', 'Day prediction: 0.65 or above on all genes (about 0.80)'))
    o.append('<text x="%.1f" y="107" class="lbl m" text-anchor="end">Day &#8805; 0.65 (about 0.80)</text>' % (x(0.65) - 6))
    # axis
    o.append('<line x1="40" y1="150" x2="560" y2="150" class="ax"/>')
    for v in (0, 0.2, 0.4, 0.6, 0.8, 1.0):
        o.append('<line x1="%.1f" y1="150" x2="%.1f" y2="155" class="ax"/><text x="%.1f" y="168" class="lbl m" text-anchor="middle">%s</text>' % (x(v), x(v), x(v), ('%g' % v)))
    for v, lab, cls, anchor in ((0.23, 'CSAC 2005: 0.23', 'mc', 'start'), (0.7989, 'Day 2026: 0.7989', 'md', 'end')):
        o.append('<line x1="%.1f" y1="118" x2="%.1f" y2="150" class="%s"/><circle cx="%.1f" cy="150" r="5" class="%sf"><title>%s</title></circle>' % (x(v), x(v), cls, x(v), cls, lab))
        o.append('<text x="%.1f" y="130" class="lbl b" text-anchor="%s">%s</text>' % (x(v) + (-6 if anchor == 'end' else 6), anchor, lab))
    o.append('<text x="300" y="192" class="lbl m" text-anchor="middle">pre-registered (536b19b), not yet run &#183; pooled dN/dS</text>')
    o.append('</svg>')
    return ''.join(o)

def fig_mesa():
    L = lambda v: 60 + math.log10(v) / 4 * 500
    o = ['<svg class="fig" viewBox="0 0 600 262" role="img" aria-labelledby="f2t f2d" xmlns="http://www.w3.org/2000/svg">',
         '<title id="f2t">Mesa index: no-selection range vs Day\'s 80</title>',
         '<desc id="f2d">Logarithmic axis from 1 to 10,000. Hand-estimated neutral ranges of the overdispersion index for 100 kb and 1 Mb windows. 100 kb: registered 5.7 to 133, sourced 48 to 163. 1 Mb: registered 24 to 740, sourced 280 to 970. Vertical markers at 80 and at 6,400, the standard-deviation-ratio reading. Hand estimates, before the run.</desc>']
    rows = [('100 kb', 'registered', 5.7, 133, 30, 'bp'), ('100 kb', 'sourced', 48, 163, 52, 'bs'),
            ('1 Mb', 'registered', 24, 740, 96, 'bp'), ('1 Mb', 'sourced', 280, 970, 118, 'bs')]
    for w, k, a, b, y, cls in rows:
        o.append('<rect x="%.1f" y="%d" width="%.1f" height="16" rx="3" class="%s"><title>%s window, %s parameter set: about %g to %g (hand estimate, pre-run)</title></rect>' % (L(a), y, L(b) - L(a), cls, w, k, a, b))
        o.append('<text x="56" y="%d" class="lbl m" text-anchor="end">%s %s</text>' % (y + 12, w, k))
        o.append('<text x="%.1f" y="%d" class="lbl on" text-anchor="middle">%g&#8211;%g</text>' % ((L(a) + L(b)) / 2, y + 12, a, b))
    for v, lab, cls, dy in ((80, 'Day: &gt; 80', 'md', 0), (6400, '6,400 (SD-ratio reading)', 'md2', 0)):
        o.append('<line x1="%.1f" y1="20" x2="%.1f" y2="170" class="%s"/>' % (L(v), L(v), cls))
    o.append('<text x="%.1f" y="14" class="lbl b" text-anchor="end">80 (Day, as stated)</text>' % (L(80) + 40))
    o.append('<text x="%.1f" y="14" class="lbl b" text-anchor="end">6,400 (SD ratio)</text>' % (L(6400) + 20))
    o.append('<line x1="60" y1="176" x2="560" y2="176" class="ax"/>')
    for v in (1, 10, 100, 1000, 10000):
        o.append('<line x1="%.1f" y1="176" x2="%.1f" y2="181" class="ax"/><text x="%.1f" y="194" class="lbl m" text-anchor="middle">%s</text>' % (L(v), L(v), L(v), format(v, ',')))
    o.append('<text x="310" y="214" class="lbl m" text-anchor="middle">overdispersion index (variance / Poisson variance), log scale</text>')
    o.append('<text x="310" y="232" class="lbl m" text-anchor="middle">hand estimates, pre-run &#183; no selection, human-lineage unit with masking, exposure 1</text>')
    o.append('<text x="310" y="250" class="lbl m" text-anchor="middle">fm_mesa_null.py at cc5e6dd (brackets 48241c7; sourced set cc5e6dd); the script table governs</text>')
    o.append('</svg>')
    return ''.join(o)

CSS = '''.fig{width:100%;height:auto;max-width:640px;display:block}
.fig .lbl{font:400 11px var(--body);fill:var(--fg)} .fig .lbl.m{fill:var(--muted)} .fig .lbl.b{font-weight:600} .fig .lbl.on{fill:var(--fg);font-size:10.5px}
.fig .ax{stroke:var(--muted);stroke-width:1}
.fig .bc{fill:var(--run-bg);stroke:var(--run)} .fig .bm{fill:var(--todo-bg);stroke:var(--todo)} .fig .bd{fill:var(--pend-bg);stroke:var(--pend)}
.fig .pc{fill:var(--run)} .fig .pd{fill:var(--pend)}
.fig .mc{stroke:var(--run);stroke-width:2} .fig .mcf{fill:var(--run)} .fig .md{stroke:var(--pend);stroke-width:2} .fig .mdf{fill:var(--pend)} .fig .md2{stroke:var(--pend);stroke-width:2;stroke-dasharray:5 3}
.fig .bp{fill:var(--run-bg);stroke:var(--run)} .fig .bs{fill:var(--ok-bg);stroke:var(--ok)}
figure.f{margin:10px 0;padding:12px 14px;background:var(--panel);border:1px solid var(--line);border-radius:8px}
figure.f figcaption{font-size:.88rem;color:var(--muted);margin-top:6px;max-width:70ch}
footer{color:var(--muted);font-size:.82rem}'''

SEC = ('''<section>
  <h2>Rules and integrations (2026-10-11 to 2026-10-12)</h2>
  <ol class="next">
    <li><b>Rule RD (reading-dependent verdicts, owner 2026-10-11):</b> where a verdict depends on how a quote is read, every plausible reading is recorded with its verdict; the claim file's field takes the reading under which the quoted statement is most defensible, and such verdicts are counted separately. Now <b>7 reading-dependent verdicts</b>: 4 claims carry a verdict (DN6 external, B9 internal, C7 internal and external, B internal) and 3 a rhetoric tag with no verdict change (Hancock RH-15, Myers RH-20, Mansfield RH-18). <b>RH6</b>: the standing test for unclear dialectic/rhetoric tags, both sides, is "remotely close" under the most charitable reading with a 3x band fixed in advance.</li>
    <li><b>B9</b> ("infertile and gone extinct within centuries"): "centuries" holds on Lynch's upper decline rate and on Day's own premise 2 (12-970 y), millennia on Lynch's central rate; the literal fixation reading gives 1.0-1.6 million y. Tagged dialectic; external contradicted, scoped.</li>
    <li><b>RHclose</b> (C7 and the Hard Limits peroration): the tag depends on the reading; the fixation-count reading of C7 is dialectic (non-sequitur at the conclusion), strict drift is rhetoric; the peroration is rhetoric on the 6.5 My fill (0.697) and dialectic on the delivered share (0.256) and Takahata Ne (0.281).</li>
    <li><b>RHclose-critics</b> (same test on the critics): Hancock RH-15 dialectic or rhetoric by reading; Myers RH-20 rhetoric on MITTENS 3.0 "sequential" (his Appendix A chain is dialectic and a non-sequitur); Mansfield RH-18 dialectic on existence and scaling. For Day: the applied math has covered 3-4 of Hancock's 10 classes. For critics: the printed formula really has no selection term.</li>
    <li><b>A2e-alpha addendum</b> (Uricchio 2019 full text): human-lineage bias-corrected alpha 0.135 gives 798 on the most Day-charitable row, 4.2x the 191 flip; A2e external is contradicted for the any-effect-size count, contested for strong-only and fitness-weighted readings (scoped, not reading-dependent).</li>
    <li><b>GAP05</b> (slightly deleterious fixations, Kim 2017 DFE): about 15,000-21,000 coding fixations per lineage; log-fitness decline 0.29-0.43 on the pre-registered base, about 0.8-1.1 on a divergence-calibrated base (post hoc), against ln 3 = 1.10; the DFE reproduces dN/dS 0.21-0.25 with no fitted parameter. For Day: the premise is supported. For critics: no pre-registered row reaches ln 3.</li>
  </ol>
</section>

<section>
  <h2>Refresh 2026-10-12: "The Method is the Conclusion"</h2>
  <p>Day's follow-up (voxday.net, 2026-10-12 14:12 UTC; Q180-Q192) moves the explanation for 0.80 versus 0.23 from gene curation to a "circular reasoning problem" in protein-guided CDS alignment, and adds a four-row gene-set table. No code, gene list or per-gene table is posted. No critic or ally has replied to the FM or dN/dS posts yet (critics refresh, same day).</p>
  <ol class="next">
    <li><b>New claim DN6</b> (protein-guided alignment biases dN/dS down), two readings. (a) "This is how the Consortium's 0.23 was produced": external contradicted, fidelity misread. (b) "Such pipelines in general bias dN/dS downward": pending, L1c decides. The verdict field takes (b), the reading most defensible to Day.</li>
    <li><b>CSAC 2005 methods text:</b> for the 13,454-gene set the human-chimp comparison came from the genome alignment, not a protein-guided realignment (Clustal W only on a 7,043-gene lineage-specific subset), and K_A/K_S for a set is pooled. A point for the critics. A point for Day: the 13,454 genes were selected for "high-quality sequence alignments covering virtually the entire coding region", so alignment quality did select the genes, though Q186 itself rules out gene selection as the cause.</li>
    <li><b>Credit to Day:</b> a falsifiable mechanism naming the deciding observable, and he revised his explanation after his own gene-set test did not separate the values.</li>
  </ol>
</section>

<section>
  <h2>Pre-registered, not yet run</h2>
  <p>Predictions are committed before any run. Order after the HF <code>ph</code> run: L1b, then L1c, then FMnull. L5 is also registered.</p>
  <ol class="next">
    <li><b>L1b</b> (0fe3c7f): T2T rerun of the dN/dS check.</li>
    <li><b>L5</b> (0e6da82): ancient-DNA zero-fixation power analysis (neutral, mainstream and Day-required rates under the panel's ascertainment).</li>
    <li><b>L1c</b> (536b19b): does the alignment method move human-chimp dN/dS from 0.80 to 0.23? Pre-run review: 1 BLOCKER, 9 MAJOR; fix pass in progress.</li>
    <li><b>FMnull</b> (48241c7, plus a post hoc sourced parameter set at cc5e6dd): what overdispersion index a no-selection model gives at Day's window sizes. Pre-run review: 10 MAJOR; fix pass queued.</li>
  </ol>
  <figure class="f">''' + fig_dnds() + '''
    <figcaption>What each side predicts for pooled dN/dS (all genes). Both values are published numbers; the bands are the registered L1c outcomes, with further conditions beyond the edges shown. Day's mechanism needs the unguided value high and the guided-and-trimmed value low; the critic band is the textbook range. Not yet run.</figcaption>
  </figure>
  <figure class="f">''' + fig_mesa() + '''
    <figcaption>Day's "more than 80 times" overdispersion sits inside the registered no-selection band at both window sizes, which is the critic expectation; at 1 Mb it falls below the sourced band, and the reading as a ratio of standard deviations (6,400) sits above every band shown. The bands rest on partly unsourced brackets and a window size Day has not stated. Hand estimates, not run results.</figcaption>
  </figure>
</section>

<section>
  <h2>What everyone missed</h2>''')

R = [
 ('<span>~98%, 53 checks reviewed (A2e-alpha, GAP-06, GAP-07t, L1, L6, L7 added); HF post hoc run <code>ph</code> in progress (workhorse + builder, ~31 h); next: L1b T2T rerun, HF integration</span>',
  '<span>~98%, 54 checks reviewed (B9, RHclose, RHclose-critics, A2e-alpha addendum, GAP05 integrated); HF post hoc run <code>ph</code> in progress (workhorse + builder; workhorse rebooted 2026-10-12 and relaunched); L1b, L5, L1c, FMnull pre-registered; next: L1b, L1c, FMnull</span>'),
 ('<span><b>232</b> claims</span>', '<span><b>233</b> claims</span>'),
 ('<b>130</b> holds · <b>19</b> non-sequitur · <b>2</b> arithmetic error · <b>52</b> pending',
  '<b>131</b> holds · <b>19</b> non-sequitur · <b>2</b> arithmetic error · <b>52</b> pending · <b>7</b> reading-dependent (4 verdicts, 3 RH tags)'),
 ('<b>34</b> supported · <b>115</b> contested · <b>16</b> contradicted · <b>6</b> untestable · <b>49</b> pending',
  '<b>34</b> supported · <b>114</b> contested · <b>18</b> contradicted · <b>6</b> untestable · <b>49</b> pending'),
 ('<b>43</b> accurate · <b>38</b> partial · <b>10</b> misread · <b>58</b> unverifiable · <b>12</b> pending',
  '<b>44</b> accurate · <b>39</b> partial · <b>10</b> misread · <b>58</b> unverifiable · <b>11</b> pending'),
 ('status as of 2026-10-10</div>', 'status as of 2026-10-12</div>'),
 ('footer{color:var(--muted);font-size:.82rem}', CSS),
 ('<section>\n  <h2>What everyone missed</h2>', SEC),
 ('    <li>Queued: <b>L1b</b> T2T rerun of the dN/dS check (after HF <code>ph</code>); fetch tasks',
  '    <li>Queued: <b>L1b</b>, <b>L1c</b>, <b>L5</b> and <b>FMnull</b> (registered, after HF <code>ph</code>; order L1b, L1c, FMnull); fetch tasks'),
]
for a, b in R:
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)
open(p, 'w').write(s)
print("ok")
