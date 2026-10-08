import re,glob,sys
kws=['fixation','fixed mutation','Kimura','Haldane','LTEE','Lenski','MITTENS','Probability Zero','PROBABILITY ZERO','Bernoulli','Hard Limit','aDNA','ancient DNA','selective turnover','Wistar','sequence space','Bio-Cycle','generations','N_e','effective population','molecular clock','McCarthy','Mansfield','Chalub','retract','Gariepy','JF ']
rows=[]
for f in sorted(glob.glob('blog/*.txt')):
    t=open(f).read()
    c={k:len(re.findall(re.escape(k),t)) for k in kws}
    tot=sum(c.values())
    nums=len(re.findall(r'\d[\d,]{3,}',t))
    rows.append((f[10:-4],len(t),tot,nums,{k:v for k,v in c.items() if v}))
for r in rows: print(r[0],r[1],r[2],r[3],' '.join(f'{k}:{v}' for k,v in list(r[4].items())[:6]))
