import re,glob,html
pat=re.compile(r'entry-title"><a href="(https://voxday.net/(\d{4})/(\d\d)/(\d\d)/([^"/]*)/?)"[^>]*>(.*?)</a>')
kws=['fixation','fixed mutation','Kimura','Haldane','LTEE','Lenski','MITTENS','Probability Zero','PROBABILITY ZERO','Bernoulli','Hard Limit','aDNA','ancient DNA','selective turnover','Wistar','sequence space','generations','effective population','molecular clock','Darwin','evolution','mutation']
seen={}
for f in sorted(glob.glob('/home/na/projects/evo-sim/sources/raw/day/tags/arch/a-*.html')):
    s=open(f,errors='replace').read()
    ms=list(pat.finditer(s))
    for i,m in enumerate(ms):
        seg=s[m.end():(ms[i+1].start() if i+1<len(ms) else len(s))]
        seg=html.unescape(re.sub('<[^>]+>',' ',seg))
        sc={k:len(re.findall(re.escape(k),seg)) for k in kws}
        seen[m.group(1)]=(f'{m.group(2)}-{m.group(3)}-{m.group(4)}',html.unescape(re.sub('<[^>]+>','',m.group(6))),{k:v for k,v in sc.items() if v})
for u,(d,t,sc) in sorted(seen.items(),key=lambda x:x[1][0]):
    inwin=('2026-06-21'<=d<='2026-08-22') or ('2026-08-28'<=d<='2026-09-10')
    if inwin: print(d,u.split('/',3)[3],'|',t,'|',sc)
print(len(seen))
