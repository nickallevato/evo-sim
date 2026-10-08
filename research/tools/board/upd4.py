p='status.html'; s=open(p).read()
c1=s[s.index('<li data-s="pend"><span class="id">C1</span>'):]
c1=c1[:c1.index('</li>')+5]
s=s.replace(c1,c1+'''
        <li data-s="pend"><span class="id">C1b</span><span class="claim"><span class="c">Day's exact time-binned statistic (new check)</span><span class="f">Simulating his stated procedure gives thousands of post-7000 BP events under neutral theory (~11,000 at Nₑ = 10k) <em>and</em> under his own d = 0.45 model (1,250–7,800). His published 21 matches neither, and no reading reproduces his own table, so the paper's figure can't be reproduced from its stated method. A gap this large may mean the model misses part of his pipeline; flagged for review before anything is concluded.</span></span></li>''')
s=s.replace('<li><b>New:</b> Day\'s exact time-binned aDNA statistic (settles the C1 disagreement)</li>','<li><b>Done:</b> Day\'s exact aDNA statistic (surprising result; needs its own review)</li>')
open(p,'w').write(s)
