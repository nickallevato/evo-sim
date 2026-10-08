p='status.html'; s=open(p).read()
def rep(idv,new):
    global s
    i=s.index(f'<span class="id">{idv}</span>'); a=s.rindex('<li',0,i); b=s.index('</li>',i)+5
    s=s[:a]+new+s[b:]
rep('B1c','''<li data-s="pend"><span class="id">B1c</span><span class="claim"><span class="c">Sourced human Nₑ history</span><span class="f">Rerun with full burn-in: every sourced history gives 1.9–4.0× more fixed substitutions per lineage than U·T, matching the analytic formula (3.986 vs 3.984). Day's (T−4Nₑ)/T is right for new mutations alone (0.84). The excess includes alleles fixing in both lineages, so it is not a human–chimp difference count.</span></span></li>''')
rep('B4','''<li data-s="pend"><span class="id">B4</span><span class="claim"><span class="c">Divergence including ancestral polymorphism</span><span class="f">Simulation matches 2μT + θ_anc to 0.3%. At the correct human–chimp ancestor (Nₑ 198k) predicted divergence is 1.55%, about 25% above the observed 1.23%; at Day's Nₑ = 10k it is 0.65%, about half. Observed sits between; it is a 3-parameter fit (μ, T, ancestral Nₑ). The CSAC polymorphic share (14–22%) matches the model (6–25%), so there is no tension.</span></span></li>''')
s=s.replace('<li>Fix and rerun B1c / B4 (20N burn-in, correct ancestral node, CSAC comparison)</li>','<li><b>Done:</b> B1c / B4 rerun with 20N burn-in; correct ancestral node; CSAC tension resolved</li>')
s=s.replace('<li><b>Done:</b> review of the two new checks; both stand with wording fixes</li>','<li><b>Done:</b> review of the two new checks; both stand with wording fixes</li>\n      <li><b>Running:</b> merge into RESULTS.md, claim verdicts, ledgers; then commit</li>')
s=s.replace('Review round for R4 (in progress)','Review round for R4')
s=s.replace('~75%, fixes + 2 new checks running','~80%, merging reviewed results')
s=s.replace('<i style="width:75%"></i>','<i style="width:80%"></i>')
open(p,'w').write(s)
