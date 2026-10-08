import os
import re,sys
sys.path.insert(0,os.environ.get("EVO_WORK","work")+'')
from quotes_data import SRC,Q
D=os.environ.get("EVO_WORK","work")+'/src/'
def norm(s):
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')
    return re.sub(r'\s+',' ',s).strip()
cache={}
def blocks(k):
    if k in cache: return cache[k]
    out=[]
    for line in open(D+k+'.txt',encoding='utf8'):
        m=re.match(r'\[([^\]]+)\] ?(.*)',line.rstrip('\n'))
        if m: out.append((m.group(1),norm(m.group(2))))
        elif out: out[-1]=(out[-1][0],out[-1][1]+' '+norm(line))
    cache[k]=out; return out
rows=[];bad=[]
for (qid,src,br,who,q,note,fl) in Q:
    nq=norm(q); loc=None
    bl=blocks(src)
    for i,(lab,txt) in enumerate(bl):
        if nq in txt: loc=lab;break
        if src.startswith('YT-') and i+1<len(bl) and nq in txt+' '+bl[i+1][1]: loc=lab;break
    if loc is None: bad.append((qid,src,q[:70])); continue
    n=len(q.split())
    if n>60: bad.append((qid,'LEN',n))
    if src.startswith('YT-'): loc='t='+loc
    elif src.startswith('YTC'): loc=loc
    elif src=='HO-pdf': loc='PDF '+loc
    elif src.startswith(('RE-','PS-')): loc=loc
    else: loc='para '+loc
    rows.append((qid,src,loc,br,who,q,note,fl))
print('ok',len(rows),'bad',bad)
import json
json.dump(rows,open(os.environ.get("EVO_WORK","work")+'/qrows.json','w'))
