import re,glob,json,html,os,sys
R='/home/na/projects/evo-sim'
def norm(s):
    s=html.unescape(s)
    s=s.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"').replace('\u2013','-').replace('\u2014','-').replace('\u2212','-').replace('\u00a0',' ').replace('\u2011','-')
    s=re.sub(r'\s+',' ',s)
    return s.lower()
corp=[]
def strs(o):
    if isinstance(o,str): yield o
    elif isinstance(o,dict):
        for v in o.values(): yield from strs(v)
    elif isinstance(o,list):
        for v in o: yield from strs(v)
files=glob.glob(R+'/docs/research/sources/quotes-*.md')+glob.glob(R+'/sources/raw/day/*.txt')+glob.glob(R+'/sources/raw/critics/*.html')+glob.glob(R+'/sources/raw/critics/*.vtt')+glob.glob(R+'/sources/raw/critics/yt/*.vtt')+glob.glob(R+'/sources/raw/sources/**/*.txt',recursive=True)
for f in files:
    try: t=open(f,encoding='utf-8',errors='ignore').read()
    except: continue
    if f.endswith('.html'): t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S); t=re.sub(r'<[^>]+>',' ',t)
    if f.endswith('.vtt'): t=re.sub(r'<[^>]+>','',t); t=re.sub(r'\d\d:\d\d:\d\d\.\d+ --> .*','',t)
    corp.append(norm(t))
for f in glob.glob(R+'/sources/raw/critics/*.json'):
    try: d=json.load(open(f,encoding='utf-8'))
    except Exception as e: continue
    corp.append(norm(' '.join(strs(d))))
C=' || '.join(corp)
bad=0;tot=0
for fn in sorted(glob.glob(R+'/docs/research/claims/[AG]*.md')):
    t=open(fn,encoding='utf-8').read()
    st=t.split('## Statement (verbatim)')[1].split('## Formal statement')[0]
    for line in st.split('\n'):
        if line.startswith('> '):
            q=norm(line[2:]); tot+=1
            qq=q.replace('...','').strip()
            if qq not in C:
                # try YT caption joined without line breaks
                bad+=1; print('MISSING',os.path.basename(fn),'::',line[:200])
print(tot,'quotes;',bad,'missing')
print('fake in C:', norm('Supermutation does not scale quadratically') in C, '| real:', norm('The claimed shortfall is 94,000 × 11.7, or about 1.1 million.') in C, len(C))
