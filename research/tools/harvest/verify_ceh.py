import re,sys,glob,json,os,html
R='/home/na/projects/evo-sim'
def norm(s):
    s=html.unescape(s)
    s=s.replace('‘',"'").replace('’',"'").replace('“','"').replace('”','"').replace('­','').replace('‑','-')
    s=s.replace('ﬁ','fi').replace('ﬂ','fl')
    s=re.sub(r'\s+',' ',s).strip()
    s=re.sub(r'(?<=\w)- (?=[a-z])','-',s)
    return s
corp={}
for f in glob.glob(R+'/sources/raw/day/*.txt')+glob.glob(R+'/sources/raw/sources/txt/*.txt')+glob.glob(R+'/sources/raw/sources/manual/*.txt')+glob.glob(R+'/docs/research/sources/quotes-*.md')+glob.glob(R+'/sources/raw/sources/abs/*.txt')+[os.environ.get("EVO_WORK","work")+'/ceh/hossjer.txt']:
    try: corp[f]=open(f,errors='ignore').read()
    except: pass
for f in glob.glob(R+'/sources/raw/critics/*.json'):
    try: d=json.load(open(f))
    except: continue
    body=(d.get('body_html') if isinstance(d,dict) else '') or ''
    if not body and isinstance(d,dict) and 'post_stream' in d:
        body='\n'.join(p['cooked'] for p in d['post_stream']['posts'])
    if body: corp[f]=re.sub(r'<[^>]+>','\n',body)
for f in glob.glob(R+'/sources/raw/critics/*.html'):
    corp[f]=re.sub(r'<[^>]+>','\n',open(f,errors='ignore').read())
normc={f:norm(t) for f,t in corp.items()}
def paras(f): return [x for x in open(f,errors='ignore').read().split('\n') if x.strip()]
def locate(q):
    nq=norm(q); return nq,[f for f,t in normc.items() if nq in t]
bad=0
for fn in sys.argv[1:]:
    txt=open(fn).read()
    m=re.search(r'## Statement \(verbatim\)(.*?)\n## Formal',txt,re.S)
    sec=m.group(1) if m else ''
    for line in sec.split('\n'):
        if line.startswith('> "'):
            q=line[3:]
            if q.endswith('"'): q=q[:-1]
            segs=[s for s in re.split(r'\s*(?:\[…\]|…)\s*',q) if s.strip()]
            ok=True; info=[]
            for s in segs:
                nq,h=locate(s)
                if not h: ok=False; info.append(('MISSING',s[:90]))
                else: info.append(os.path.basename(h[0]))
            if not ok: bad+=1; print('FAIL',os.path.basename(fn),info)
            else:
                loc=''
                for f in locate(segs[0])[1]:
                    if '/raw/day/' in f and f.endswith('.txt'):
                        for i,p in enumerate(paras(f),1):
                            if norm(segs[0]) in norm(p): loc=f'{os.path.basename(f)} para {i}'; break
                        break
                print('ok',os.path.basename(fn),loc or info[0])
print('BAD',bad)
