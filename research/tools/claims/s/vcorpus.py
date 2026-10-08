import os, re, json, html, glob, unicodedata
R='/home/na/projects/evo-sim/sources/raw'
S=os.environ.get("EVO_WORK","work")+'/txt'
def norm(t):
    t=html.unescape(t)
    t=unicodedata.normalize('NFKC',t)
    for a,b in (('’',"'"),('‘',"'"),('“','"'),('”','"'),('–','-'),('—','-'),('−','-'),('­',''),('​','')):
        t=t.replace(a,b)
    t=re.sub(r'\s+',' ',t)
    return t
def strings(o):
    if isinstance(o,str): yield o
    elif isinstance(o,dict):
        for v in o.values(): yield from strings(v)
    elif isinstance(o,list):
        for v in o: yield from strings(v)
_cache=None
def corpus():
    global _cache
    if _cache is not None: return _cache
    files=[]
    for pat in ('day/*.txt','critics/*.json','critics/*.html','critics/*.xml','critics/yt/*.transcript.txt','critics/yt/*.info.json','sources/txt/*.txt','sources/abs/*.txt','sources/manual/*.txt'):
        files+=glob.glob(os.path.join(R,pat))
    files+=glob.glob(S+'/*.txt')
    out={}
    for f in files:
        try: raw=open(f,errors='ignore').read()
        except Exception: continue
        if f.endswith('.json'):
            try: raw=' \n '.join(strings(json.loads(raw)))
            except Exception: pass
            raw=raw.replace('\\n',' ')
        if f.endswith(('.json','.html','.xml')):
            raw=re.sub(r'<script.*?</script>',' ',raw,flags=re.S); raw=re.sub(r'<[^>]+>',' ',raw)
        out[f]=norm(raw)
    _cache=out; return out
def find(q):
    n=norm(q); hits=[]
    for f,t in corpus().items():
        if n in t: hits.append(os.path.relpath(f,R) if f.startswith(R) else f)
    return hits
