p='status.html'; s=open(p).read()
# all R4 pend nodes are now reviewed
import re
for idv in ['A2','A4','B1c','B3b','B4','C1','C1b','C2','C6','F2','G','H-hard','H1','H2','H8']:
    s=s.replace(f'<li data-s="pend"><span class="id">{idv}</span>',f'<li data-s="ok"><span class="id">{idv}</span>')
s=s.replace('<li><b>Running:</b> merge into RESULTS.md, claim verdicts, ledgers; then commit</li>','<li><b>Done:</b> merged and committed (54 verdict fields across 33 claims)</li>')
s=s.replace('~80%, merging reviewed results','~80%, round 2 reviewed and committed')
s=s.replace('status as of 2026-10-07','status as of 2026-10-08')
s=s.replace('C6 "does not rescue Day"','C6')
tally='''  <div class="stats">
    <span>Verdicts so far, internal: <b>89</b> holds · <b>14</b> non-sequitur · <b>6</b> arithmetic error · <b>61</b> pending</span>
    <span>External: <b>21</b> supported · <b>97</b> contested · <b>9</b> contradicted · <b>5</b> untestable · <b>50</b> pending</span>
    <span>Citation fidelity: <b>35</b> accurate · <b>31</b> partial · <b>9</b> misread · <b>35</b> unverifiable</span>
  </div>
</section>

<section>
  <h2>Review round for R4</h2>'''
s=s.replace('</section>\n\n<section>\n  <h2>Review round for R4</h2>',tally,1)
nxt=s[s.index('<ol class="next">'):]; nxt=nxt[:nxt.index('</ol>')+5]
s=s.replace(nxt,'''<ol class="next">
    <li>Remaining checks: E (founder hazard, relictation), G1 (specific vs any outcome), D (sequence space).</li>
    <li>Follow-ups: C1b with realistic per-site call depth; H at realistic human reproductive excess and hard-selected load; confidence intervals on H; Yoo's mutation rate for rescaling ancestral Nₑ.</li>
    <li>R5: final verdicts, sensitivity table, simulator variable list.</li>
  </ol>''')
open(p,'w').write(s)
