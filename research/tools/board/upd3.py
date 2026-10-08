p='status.html'; s=open(p).read()
anchor=s.index('<li data-s="pend"><span class="id">H8</span>')
s=s[:anchor]+'''<li data-s="pend"><span class="id">H-hard</span><span class="claim"><span class="c">Many simultaneous sweeps under hard selection (new check)</span><span class="f">Populations sustain 0.03–0.4 substitutions per generation (9–120× Haldane's 1/300) until total selective cost exceeds ln R, then go extinct. Day's ~230 concurrent sweeps persist when R ≥ 5 and fail at R = 2. With Keightley's deleterious load (U = 2.2) R needs to be about 10–20. Day's cap returns only if R ≈ e^U. Free recombination and an imposed opportunity rate favour the critics.</span></span></li>
        '''+s[anchor:]
g_old=s[s.index('<li data-s="pend"><span class="id">G</span>'):]
g_old=g_old[:g_old.index('</li>')+5]
s=s.replace(g_old,'''<li data-s="pend"><span class="id">G</span><span class="claim"><span class="c">~230 simultaneous sweeps cap</span><span class="f">No collapse at ~260–270 open loci under soft selection, or under hard selection when R ≥ 5. Under hard selection with R = 2 the population fails at ~167. The cap depends on reproductive excess and load.</span></span></li>''')
s=s.replace('<li><b>New:</b> hard selection with many loci at scale (the test both steelmen asked for)</li>','<li><b>Done:</b> hard selection with many loci (needs its own review)</li>')
open(p,'w').write(s)
