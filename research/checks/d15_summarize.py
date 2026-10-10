"""D15 sweep summarizer (POST HOC; written after the sweep was collected and seen; descriptive tables only, no new simulation).
Run: research/.venv/bin/python -I research/checks/d15_summarize.py  (cwd = repo root). Reads results/raw/d15_sweep.jsonl."""
import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "results", "raw"))
# ---- part a ----
import json
import json,collections
R=[json.loads(l) for l in open('d15_sweep.jsonl')]
print(len(R), sum(not r['complete_at_900My'] for r in R),'incomplete')
print('hit guard (sec>=1490):',sum(r['sec']>=1490 for r in R), 'max sec',max(r['sec'] for r in R))
print(sorted(set(r['kmult'] for r in R)), sorted(set(r['F'] for r in R)))
def key(r):return (r['Ne'],r['F'],r['m'],r['rho'])
# table: p9 by Ne,F,m (rho0) across kmult
for Ne in (1e4,1e5):
  for F in ['N','V4','V3','V2','Fin2','Fin3','S2','S3']:
    for rho in (0,1):
      for m in (1,2,3,4):
        rs=sorted([r for r in R if r['Ne']==Ne and r['F']==F and r['m']==m and r['rho']==rho],key=lambda r:r['kmult'])
        if rs: print(int(Ne),F,'rho',rho,'m',m,' '.join(f"{r['kmult']:g}:{r['p9']:.2f}{'' if r['complete_at_900My'] else '*'}" for r in rs))
# ---- part b ----
import json
import json,math
R=[json.loads(l) for l in open('d15_sweep.jsonl')]
d={(r['Ne'],r['F'],r['m'],r['rho'],round(r['kmult'],3)):r for r in R}
def g(*k):return d.get(k)
print("neutral rho0: Ne kmult m: p9 p90 p900 med mean_fin chain ratio(mean_fin/chain) nfin")
for Ne in (1e4,1e5):
  for k in (1.0,30.0,100.0):
    for m in (1,2,3,4):
      r=g(Ne,'N',m,0,round(k,3))
      if r: print(int(Ne),k,m,r['p9'],r['p90'],r['p900'],r['median'] and round(r['median']),r['mean_fin'] and round(r['mean_fin']),round(r['pred_chain']),r['mean_fin'] and round(r['mean_fin']/r['pred_chain'],2),r['n_fin'],r['f'])
# kmult 1 summary: any cell with p9>0.05 or p90>0.05
print("kmult=1 cells with p9>0.05:")
for r in R:
  if abs(r['kmult']-1)<1e-6 and r['p9']>0.05: print(' ',int(r['Ne']),r['F'],r['m'],r['rho'],r['p9'],r['p90'])
print("kmult=1/12 p9>0.05:",[(int(r['Ne']),r['F'],r['m'],r['rho'],r['p9']) for r in R if r['kmult']<0.1 and r['p9']>0.05])
print("kmult=3 p9>=0.5:",[(int(r['Ne']),r['F'],r['m'],r['rho'],r['p9']) for r in R if abs(r['kmult']-3)<1e-6 and r['p9']>=0.5])
print("kmult<=3 neutral/valley p9>=0.5:",[r for r in R if r['kmult']<=3.01 and r['F'] in('N','V4','V3','V2') and r['p9']>=0.5])
print("kmult<=3 neutral/valley p90>0.05:",[(int(r['Ne']),r['F'],r['m'],r['rho'],r['kmult'],r['p90']) for r in R if r['kmult']<=3.01 and r['F'] in('N','V4','V3','V2') and r['p90']>0.05])
# P7 rho
import statistics
print("P7: rho1/rho0 mean_fin ratio where both complete & n_fin>=30")
for key,r in d.items():
  Ne,F,m,rho,k=key
  if rho==0 and (Ne,F,m,1,k) in d:
    r1=d[(Ne,F,m,1,k)]
    if r['n_fin']>=30 and r1['n_fin']>=30 and r['mean_fin'] and r1['mean_fin']:
      q=r1['mean_fin']/r['mean_fin']
      if q>1.25 or q<0.6: print(' ',int(Ne),F,m,k,round(q,2),r['n_fin'],r1['n_fin'])
# summary of ratio dist
qs=[]
for key,r in d.items():
  Ne,F,m,rho,k=key
  if rho==0 and (Ne,F,m,1,k) in d:
    r1=d[(Ne,F,m,1,k)]
    if r['n_fin']>=30 and r1['n_fin']>=30: qs.append((r1['mean_fin']/r['mean_fin'],F,k,m,Ne))
print(len(qs),'pairs; >1.25:',sum(q[0]>1.25 for q in qs),'<0.8:',sum(q[0]<0.8 for q in qs))
print('neutral pairs',[ (round(q[0],2),q[2],q[3],int(q[4])) for q in qs if q[1]=='N'])
# valley vs neutral
print("valley mean_fin/N mean_fin, Ne=1e4 rho0 kmult 30/100:")
for F in('V4','V3','V2'):
  for k in (30.0,100.0):
    for m in (2,3,4):
      a=g(1e4,F,m,0,k);b=g(1e4,'N',m,0,k)
      print(F,k,m,a['n_fin'],a['mean_fin'] and round(a['mean_fin']),b['mean_fin'] and round(b['mean_fin']),round(a['pred_chain']) if a['pred_chain']<1e30 else '>1e30',a['complete_at_900My'])
print("V Ne=1e5 n_fin:",[(F,m,k,g(1e5,F,m,0,k)['n_fin']) for F in('V4','V3','V2') for m in(2,) for k in (1.0,30.0,100.0)])
inc=[(int(r['Ne']),r['F'],r['m'],r['rho'],round(r['kmult'],2),r['n_fin']) for r in R if not r['complete_at_900My']]
print(len(inc),inc)
# S2 Ne1e5 kmult 1 mean
for F in('S2','S3','Fin2','Fin3'):
  for Ne in(1e4,1e5):
    for m in (1,2,4):
      r=g(Ne,F,m,0,1.0)
      if r: print(F,int(Ne),m,'kmult1 p9',r['p9'],'p90',r['p90'],'mean',r['mean_fin'] and round(r['mean_fin']),'chain',round(r['pred_chain']) if r['pred_chain']<1e30 else 'big')
# ---- part c ----
import json
R=[json.loads(l) for l in open('d15_sweep.jsonl')]
inc=[r for r in R if not r['complete_at_900My']]
print(sorted(set(round(r['min_censor_clock']/1e6,2) if r['min_censor_clock'] else None for r in inc)))
print(min((r['min_censor_clock'] or 1e18) for r in inc), 'T9=3.6e5 T90=3.6e6')
# incomplete cells with kmult==... any at Ne=1e5? and of the 28 which have min clock < 3.6e6
print([ (r['F'],r['m'],r['kmult'],r['min_censor_clock']) for r in inc if (r['min_censor_clock'] or 1e18)<3.6e6])
# kmult 1 neutral/valley: how many reps finished by 900My
print([(int(r['Ne']),r['F'],r['m'],r['n_fin']) for r in R if r['kmult']==1.0 and r['F'] in('N',) ])
# fraction of 714 where p9<=0.05
print(sum(r['p9']<=0.05 for r in R), sum(r['p9']>=0.5 for r in R), sum(r['p90']<=0.05 for r in R))
for Ne in (1e4,1e5):
  for F in ('N','V4','V3','V2','Fin2','Fin3','S2','S3'):
    rs=[r for r in R if r['Ne']==Ne and r['F']==F]
    print(int(Ne),F,len(rs),'holds(p9<=.05)',sum(r['p9']<=0.05 for r in rs),'fails(p9>=.5)',sum(r['p9']>=0.5 for r in rs),'far(p90<=.05)',sum(r['p90']<=0.05 for r in rs))
