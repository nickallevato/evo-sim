import json,re
R='/home/na/projects/evo-sim/sources/raw/day'
res=json.load(open('class.json'))
sha={l.split()[1]:l.split()[0] for l in open('blogsha.txt')}
manual={'2019-02-07-maximal-mutations':'2019 MITTENS origin post (bacteria/mammals/CHLCA tables; 562)','2021-11-11-the-jfg-vd-debate':'Transcript of 2019-02-07 Gariepy debate','2026-01-19-probability-zero-qa':'Q&A: t=19,800; d integral; CpG','2026-02-04-response-to-dennis-mccarthy-round-2':'First appearance of F_max formula in corpus','2026-05-07-a-retraction-and-a-revision':'Retraction of Term 3 (Kimura calculator)','2026-10-01-the-education-of-a-population-geneticist':'k=32.3 mu first appearance; response to critic','2026-09-28-mittens-3-0':'Announces Zenodo 23003785','2026-09-27-the-temperature-rises':'4,615 NS-only','2026-10-01-snikker-snak':'909 gen/fix Ara+2; sequential-fixation claim','2026-01-08-88-million-x':'Dawkins quoting Haldane 11,739/321,444','2026-01-14-empirically-impossible':'aDNA zero fixations in 1.2M loci (AADR v62.0)','2025-05-28-haldane-vs-kimura':'Haldane 300 vs Kimura 2-yr table','2026-05-23-probability-zero-2nd-edition':'2nd edition intro; 410M bp','2026-02-02-pz-print-editions':'Print editions/ISBN-10 link','2026-05-02-kimuras-fixation-calculator':'Announces Zenodo 19984826'}
def branch(t):
    c={}
    for k,pat in {'H':r'Haldane|cost of selection','G':r'Bernoulli','C':r'ancient DNA|aDNA|AADR','D':r'Wistar|sequence space|Weasel|Ulam','E':r'LTEE|Lenski|punctuated|hypermut','B':r'Kimura|k ?= ?μ|N_e|Nₑ|effective population|molecular clock|Chalub','A':r'MITTENS|fixed mutation|generations per fixation|Selective Turnover'}.items():
        n=len(re.findall(pat,t)); 
        if n: c[k]=n
    return ','.join(k for k,_ in sorted(c.items(),key=lambda x:-x[1])[:3]) or 'misc'
out=[]
for sf,u,src,keep,reason in res:
    if not keep: continue
    t=open(f'{R}/{sf}.txt').read()
    title=t.split('\n')[0][7:].strip()
    d=sf[5:15]; key='B'+sf[5:]
    out.append('| '+' | '.join([key,'blog',d,title.replace('|','/'),u,'WordPress page, fetched 2026-10-07',f'sources/raw/day/{sf}.html',sha[f'{sf}.html'],'ok',branch(t),manual.get(sf[5:],'')+('; found via '+src if src=='search' else '')])+' |')
open('blog_table.md','w').write('\n'.join(out)); print(len(out))
