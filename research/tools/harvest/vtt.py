import sys,re
# output: one line per ~cue with start time, dedup rolling captions
lines=open(sys.argv[1],encoding='utf8').read().split('\n')
out=[];last='';t=None
for i,l in enumerate(lines):
    m=re.match(r'(\d\d):(\d\d):(\d\d)\.\d+ --> ',l)
    if m: t=f'{m.group(1)}:{m.group(2)}:{m.group(3)}'; continue
    if not l.strip() or l.startswith(('WEBVTT','Kind:','Language:')) or '-->' in l: continue
    txt=re.sub(r'<[^>]+>','',l).strip()
    if txt and txt!=last and t:
        out.append((t,txt)); last=txt
# merge into ~ 30s chunks
chunks=[];cur=None
for t,txt in out:
    s=sum(int(x)*m for x,m in zip(t.split(':'),(3600,60,1)))
    if cur is None or s-cur[0]>=20:
        cur=[s,t,txt]; chunks.append(cur)
    else: cur[2]+=' '+txt
for s,t,txt in chunks: print(f'[{t}] {txt}')
