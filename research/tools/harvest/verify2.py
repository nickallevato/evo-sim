exec(open('verify.py').read().split("bad=0;tot=0")[0])
import glob,re,os
miss=0
for fn in sorted(glob.glob(R+'/docs/research/claims/[AG]*.md')):
    t=open(fn,encoding='utf-8').read()
    body=t.split('## Formal statement')[1]
    body='\n'.join(l for l in body.split('\n') if not l.startswith('> '))
    for m in re.finditer(r'["“]([^"“”\n]{25,}?)["”]',body):
        q=m.group(1)
        qq=norm(q).replace('...','').replace('…','')
        parts=[p.strip(' .,;') for p in re.split(r'\s?\[[^\]]*\]\s?|…',norm(q)) if len(p.strip())>12]
        ok=all(p in C for p in parts) if parts else True
        if not ok:
            miss+=1; print(os.path.basename(fn),'::',q[:160])
print('missing',miss)
