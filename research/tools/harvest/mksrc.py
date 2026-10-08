import json,re,html,subprocess,sys,os
R='/home/na/projects/evo-sim/sources/raw/critics/'
O=os.environ.get("EVO_WORK","work")+'/src/'
def paras_from_html(raw):
    raw=re.sub(r'<(script|style)[^>]*>.*?</\1>','',raw,flags=re.S)
    raw=re.sub(r'</(p|h\d|li|div|blockquote|tr)>','\n\n',raw)
    raw=re.sub(r'<br\s*/?>','\n',raw)
    t=html.unescape(re.sub(r'<[^>]+>','',raw))
    return [x.strip() for x in re.split(r'\n\s*\n',t) if x.strip()]
def art(path):
    raw=open(R+path,encoding='utf8',errors='replace').read()
    m=re.search(r'class="[^"]*entry-content[^"]*"',raw); s=m.start() if m else 0
    e=re.search(r'class="[^"]*(sharedaddy|entry-footer|post-meta|comments-area|jp-relatedposts)',raw[s:])
    return raw[s:s+(e.start() if e else len(raw))]
def w(key,paras):
    with open(O+key+'.txt','w') as f:
        for i,p in enumerate(paras,1): f.write(f'[{i}] '+p.replace('\n',' ')+'\n')
def wj(key,path):
    d=json.load(open(R+path)); w(key,paras_from_html(d['body_html']))
for k,p in {'MC1':'mccarthy-why-probability-zero-is-wrong-about-0d1.json','MC2':'mccarthy-vox-day-responds.json','KR-epi':'ck-the-epicycle-was-elsewhere.json','KR-broken':'ck-the-broken-evolutionary-math.json','KR-flock':'ck-kimura-and-the-red-flock.json','KR-rev':'ck-probability-zero-a-review-too-late.json','DEM-HO':'dembski-hossjer.json','DEM-INT':'dembski-interview.json','KEEN':'keen-natura.json','TOW':'treeofwoe.json','FP':'fandompulse.json','UJB':'ujb-notachance.json','AH':'amhyp.json'}.items(): wj(k,p)
for k,p in {'PZ1':'pz-vox-days-amazing-ego-and-bill-dembski-dont-care.html','PZ2':'pz-can-we-be-done-with-vox-day-now.html','PZ3':'pz-vox-day-responds-to-my-criticism-of-his-refutation-of-evolution.html','CA1':'ca-part1.html','CA2':'ca-part2.html','CA3':'ca-part3.html','CA4':'ca-part4.html','CA5':'ca-part5.html','CA6':'ca-part6.html','BOW':'vd-bowers-repost.html','GAR':'gariepy-whopping.html'}.items(): w(k,paras_from_html(art(p)))
# plain html
for k,p in {'RO-FEL':'felsenstein-rosenhouse-toc.html','RO-PT':'rosenhouse-pt-review.html'}.items():
    raw=open(R+p,encoding='utf8').read(); raw=re.sub(r'<(script|style)[^>]*>.*?</\1>','',raw,flags=re.S)
    t=html.unescape(re.sub(r'<[^>]+>','\n',raw)); w(k,[x.strip() for x in re.split(r'\n\s*\n',t) if x.strip()] if False else [re.sub(r'\s+',' ',t)])
# pdf pages
t=subprocess.run(['pdftotext','-layout',R+'hossjer-mittens-review.pdf','-'],capture_output=True,text=True).stdout
pages=t.split('\f'); 
with open(O+'HO-pdf.txt','w') as f:
    for i,p in enumerate(pages,1): f.write(f'[p{i}] '+re.sub(r'\s+',' ',p)+'\n')
# reddit
def rtree(path):
    d=json.load(open(R+path))['data']; out=[]
    def walk(n):
        c=n.get('data',n); out.append(c)
        for ch in n.get('children') or []: walk(ch)
    for n in d: walk(n)
    return out
posts={}
for f in os.listdir(R):
    if f.startswith('arctic-title'):
        for p in json.load(open(R+f))['data'] or []: posts[p['id']]=p
for pid in ['1wss2wj','1wv4zeg','1wxgsjm','1wvzng3']:
    p=posts[pid]; lines=[f"[post {pid} by {p['author']}] "+p['selftext'].replace('\n',' ')]
    for c in rtree(f'arctic-tree-{pid}.json'): lines.append(f"[comment {c.get('id')} by {c.get('author')} score {c.get('score')}] "+(c.get('body') or '').replace('\n',' '))
    open(O+f'RE-{pid}.txt','w').write('\n'.join(lines)+'\n')
# PS
for tid in ['18094','18095']:
    d=json.load(open(R+f'ps-topic-{tid}.json')); lines=[]
    for p in d['post_stream']['posts']:
        t=html.unescape(re.sub(r'<[^>]+>',' ',p['cooked'])); lines.append(f"[post {p['post_number']} by {p['username']}] "+re.sub(r'\s+',' ',t))
    open(O+f'PS-{tid}.txt','w').write('\n'.join(lines)+'\n')
# YT comments
for v in ['jDxFtCOGZ3A','_Vu0ZVVjwHc','6jXiwrcC5PQ','nTVRiEcswI8']:
    d=json.load(open(R+f'yt/{v}.info.json')); lines=[]
    for c in d.get('comments',[]): lines.append(f"[comment {c['id']} by {c['author']} likes {c.get('like_count')}] "+c['text'].replace('\n',' '))
    open(O+f'YTC-{v}.txt','w').write('\n'.join(lines)+'\n')
    tr=R+f'yt/{v}.transcript.txt'
    if os.path.exists(tr): open(O+f'YT-{v}.txt','w').write(open(tr).read())
