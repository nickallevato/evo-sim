p='status.html'; s=open(p).read()
old_h2=s[s.index('<li data-s="pend"><span class="id">H2</span>'):]
old_h2=old_h2[:old_h2.index('</li>')+5]
s=s.replace(old_h2,'''<li data-s="pend"><span class="id">H2</span><span class="claim"><span class="c">Hard vs soft selection (Nunney 2003)</span><span class="f">Corrected model: soft selection is 1.5–2.8× <em>slower</em> than hard at equal mutation supply, so the critics' "soft selection removes the cost" did not reproduce. Haldane's 300 is a bounding case; the human value is undetermined, so H is neither refuted nor binding.</span></span></li>''')
s=s.replace('<li>Fix and rerun H / C2 (mutation timing; H1, H8 claim ratios)</li>','<li><b>Done:</b> H / C2 fixed and rerun; H1, H8 ratios corrected (17.1×)</li>')
s=s.replace('<li>Haldane\'s cost is real under hard selection</li>','<li>Haldane\'s cost is real under hard selection, and soft selection does not remove it in these models</li>')
open(p,'w').write(s)
