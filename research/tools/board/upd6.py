import re
p='status.html'; s=open(p).read()
def rep(idv,new):
    global s
    i=s.index(f'<span class="id">{idv}</span>'); a=s.rindex('<li',0,i); b=s.index('</li>',i)+5
    s=s[:a]+new+s[b:]
rep('H-hard','''<li data-s="pend"><span class="id">H-hard</span><span class="claim"><span class="c">Many simultaneous sweeps under hard selection (new check, reviewed with fixes)</span><span class="f">The limit is ln R / D (reproductive excess over cost per substitution), not a fixed 1 in 300. Populations sustained 9–120× Haldane's rate at R ≥ 1.3. Haldane's own case (R ≈ 1.1, diploid D ≈ 20–30) gives ≈ 1/300 and was not tested, so "1/300 falsified" is withdrawn; "10% is not a general bound" stands. Day's ~230 sweeps persist at R ≥ 5, fail at R = 2. Model favours critics (free recombination, imposed opportunity rate).</span></span></li>''')
rep('C1b','''<li data-s="pend"><span class="id">C1b</span><span class="claim"><span class="c">Day's exact time-binned statistic (new check, reviewed)</span><span class="f">Verdict: not reproducible, cannot adjudicate. The model misses Day's own table, so it isn't a valid null. Likely cause found: real ancient samples give only a few calls per site in old bins. Lowering per-site coverage drops the neutral count from ~6,500 to ~120 and moves events into the oldest bin, the same direction as Day's table. A direction, not yet a reproduction.</span></span></li>''')
s=s.replace('<li><b>Running:</b> review of the two new checks (hard selection, C1b)</li>','<li><b>Done:</b> review of the two new checks; both stand with wording fixes</li>')
s=s.replace("<li><b>Done:</b> Day's exact aDNA statistic (surprising result; needs its own review)</li>","<li><b>Done:</b> Day's exact aDNA statistic (reviewed: not reproducible, cannot adjudicate)</li>")
s=s.replace('<li><b>Done:</b> hard selection with many loci (needs its own review)</li>','<li><b>Done:</b> hard selection with many loci (reviewed)</li>')
open(p,'w').write(s)
