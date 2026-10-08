import re,html,os
S1='\u2063'; S2='\u2064'
R='/home/na/projects/evo-sim/sources/raw/'
OUT='/home/na/projects/evo-sim/docs/research/claims/'
def norm(s): return re.sub(r'\s+',' ',s).strip()
_cache={}
def load(key):
    if key in _cache: return _cache[key]
    if key=='W': raw=open(R+'sources/txt/Wistar1967.txt',encoding='utf8',errors='replace').read()
    elif key.startswith('b:'): raw=open(R+'day/blog-'+key[2:]+'.txt',encoding='utf8').read()
    elif key.startswith('z:'): raw=open(R+'day/zenodo-'+key[2:]+'.txt',encoding='utf8').read()
    elif key=='milton': 
        t=open(R+'day/tags/evo-11.html',encoding='utf8').read(); i=t.find('Richard Milton'); t=t[i-100:i+9000]
        raw=html.unescape(re.sub(r'<[^>]+>',' ',t))
    elif key=='ca4':
        t=open(R+'critics/ca-part4.html',encoding='utf8',errors='replace').read()
        raw=html.unescape(re.sub(r'<[^>]+>',' ',re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)))
    elif key=='qc': raw=open('/home/na/projects/evo-sim/docs/research/sources/quotes-critics.md',encoding='utf8').read()
    elif key=='taylor': raw=open(os.environ.get("EVO_WORK","work")+'/w/taylor.txt',encoding='utf8').read()
    elif key=='dint': raw=open(os.environ.get("EVO_WORK","work")+'/dembski_int.txt',encoding='utf8').read()
    elif key=='k62': raw=open(R+'sources/manual/Kimura1962.txt',encoding='utf8',errors='replace').read()
    elif key=='whop': raw=open(os.environ.get("EVO_WORK","work")+'/dl/whoppers.txt',encoding='utf8').read()
    elif key=='axe': raw=open(R+'sources/abs/Axe2004.txt',encoding='utf8').read()
    elif key=='keefe': raw=open(R+'sources/abs/KeefeSzostak2001.txt',encoding='utf8').read()
    elif key=='mitt3': raw=open(R+'day/zenodo-23003785.txt',encoding='utf8').read()
    elif key=='book': 
        t=open(R+'day/book/ndm-probability-zero.html',encoding='utf8',errors='replace').read()
        raw=html.unescape(re.sub(r'<[^>]+>',' ',re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)))
    else: raise KeyError(key)
    _cache[key]=(raw,norm(raw)); return _cache[key]
def ex(key,a,b=None):
    """verbatim extract (whitespace-normalised) from a..b inclusive; asserts presence"""
    raw,n=load(key)
    i=n.find(norm(a)); assert i>=0,(key,'start not found',a)
    if b is None: j=i+len(norm(a))
    else:
        k=n.find(norm(b),i); assert k>=0,(key,'end not found',b); j=k+len(norm(b))
    return S1+n[i:j]+S2
def para(key,a):
    """paragraph number (non-empty lines after TITLE) in blog/zenodo text containing anchor"""
    raw,_=load(key); n=0
    for line in raw.split('\n'):
        if not line.strip(): continue
        if line.startswith('TITLE:'): continue
        n+=1
        if norm(a) in norm(line): return n
    return None
def lineno(key,a):
    raw,_=load(key)
    for i,l in enumerate(raw.split('\n')):
        if norm(a) in norm(l): return i+1
    return None
S1='\u2063'; S2='\u2064'
def q(s): return '> "'+s.replace(S1,'').replace(S2,'')+'"'
def fix(t):
    t=re.sub(r'(^|\n\n)\u2063(.*?)\u2064',lambda m: m.group(1)+'> "'+m.group(2)+'"',t,flags=re.S)
    return t.replace(S1,'').replace(S2,'')
FM="""---
id: {id}
title: "{title}"
side: {side}
branch: {branch}
parent: {parent}
edges: {edges}
load_bearing: {lb}  # {lbwhy}
sourcing: {sourcing}
status: extracted
verdicts:
  internal: {vi}      # {vi_why}
  fidelity: {vf}      # {vf_why}
  external: {ve}      # {ve_why}
---
"""
def write(slug,id,title,side,branch,parent,edges,lb,lbwhy,sourcing,vi,vi_why,vf,vf_why,ve,ve_why,statement,formal,assump,responses,lit,prereg,check,simvars):
    statement,formal,assump,responses,lit,prereg,check,simvars=[fix(x) for x in (statement,formal,assump,responses,lit,prereg,check,simvars)]
    body=FM.format(id=id,title=title.replace('"',"'"),side=side,branch=branch,parent=parent,edges=edges,lb=lb,lbwhy=lbwhy,sourcing=sourcing,vi=vi,vi_why=vi_why,vf=vf,vf_why=vf_why,ve=ve,ve_why=ve_why)
    body+="\n## Statement (verbatim)\n"+statement.strip()+"\n\n## Formal statement\n"+formal.strip()+"\n\n## Assumptions\n"+assump.strip()+"\n\n## Responses\n"+responses.strip()+"\n\n## Primary literature\n"+lit.strip()+"\n\n## Pre-registered prediction\n"+prereg.strip()+"\n\n## Check\n"+check.strip()+"\n\n## Simulator variables implied\n"+simvars.strip()+"\n"
    open(OUT+slug+'.md','w',encoding='utf8').write(body)
    print('wrote',slug+'.md',len(body))
