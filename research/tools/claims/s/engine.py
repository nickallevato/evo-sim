import sys, os, re
sys.path.insert(0,os.path.dirname(__file__))
import vcorpus
OUT='/home/na/projects/evo-sim/docs/research/claims'
BAD=[]
SRC={}
def src(key,title,url,date): SRC[key]=(title,url,date)
def para(file,text):
    """n-th non-empty line of raw day txt containing text"""
    p=os.path.join(vcorpus.R,file)
    n=vcorpus.norm(text)
    i=0
    for line in open(p,errors='ignore'):
        if line.strip():
            i+=1
            if n in vcorpus.norm(line): return i
    return None
def ver(text):
    hits=vcorpus.find(text)
    if not hits:
        n=re.sub(r'\s+','',vcorpus.norm(text))
        for f,t in vcorpus.corpus().items():
            if n in re.sub(r'\s+','',t): hits.append(os.path.relpath(f,vcorpus.R)+' [spacing-normalised]')
    if not hits: BAD.append(text)
    return hits
def Q(key,text,loc='',sh=None,file=None,note='',frags=None):
    """returns (quote block, source line)"""
    if frags:
        for fr in frags: ver(fr)
        note=(note+'. ' if note else '')+'OCR text layer of a scanned PDF: mathematical symbols and some spacing are repaired in this quote (fragments checked verbatim against the raw extraction; full sentence as in quotes-literature.md)'
    else: hits=ver(text)
    t,u,d=SRC[key]
    if file and not loc:
        p=para(file,text)
        loc=f'¶{p} of extracted text' if p else ''
    s=f'Source: [{t}]({u}), {d}'+(f', {loc}' if loc else '')
    if sh: s+=f'. **secondhand** ({sh})'
    if note: s+=f'. {note}'
    return f'> {text}\n\n{s}'
def rq(key,text,loc='',sh=None,file=None):
    """inline quote for responses: bullet-friendly"""
    hits=ver(text)
    t,u,d=SRC[key]
    if file and not loc:
        p=para(file,text); loc=f'¶{p}' if p else ''
    tag=f' [secondhand: {sh}]' if sh else ''
    return f'"{text}" ([{t}]({u}), {d}{", "+loc if loc else ""}){tag}'
def lit_row(work,quote,fid): return f'| {work} | {quote} | {fid} |'
import re as _re
def prose_check(c):
    miss=[]
    for k in ('formal','a_stated','a_impl','against','support','weak','p_claim','p_opp','p_change','check'):
        for m in _re.finditer(r'"([^"\n]{14,})"',c.get(k,'')):
            s=m.group(1)
            if not vcorpus.find(s): miss.append((c['id'],k,s[:100]))
    return miss
def render(c):
    fm=['---',f"id: {c['id']}",'title: '+__import__('json').dumps(c['title'],ensure_ascii=False),f"side: {c['side']}",f"branch: {c['branch']}",f"parent: {c['parent']}"]
    fm.append('edges: ['+', '.join('{type: %s, target: %s}'%(a,b) for a,b in c.get('edges',[]))+']')
    fm.append(f"load_bearing: {'true' if c['lb'][0] else 'false'}  # {c['lb'][1]}")
    fm.append(f"sourcing: {c['sourcing']}")
    fm.append(f"status: {c.get('status','extracted')}")
    v=c['v']
    fm+= ['verdicts:',f'  internal: {v[0]}',f'  fidelity: {v[1]}',f'  external: {v[2]}','---','']
    body=['## Statement (verbatim)']
    body+= [q+'\n' for q in c['quotes']]
    body+=['## Formal statement',c['formal'].strip(),'']
    body+=['## Assumptions','- Stated: '+c['a_stated'].strip(),'- Implicit: '+c['a_impl'].strip(),'']
    body+=['## Responses','- Against: '+c['against'].strip(),'- In support: '+c['support'].strip(),'- Weaknesses in the responses: '+c['weak'].strip(),'']
    body+=['## Primary literature','| Cited work | What it actually says (quote) | Fidelity |','|---|---|---|']
    body+= c['lit'] if c['lit'] else ['| none cited | n/a | n/a |']
    pn=c.get('prereg_note')
    if not pn and c['check'].strip().startswith('Script: none') and 'proposed' not in c['check'][:60]:
        pn='No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side\'s model implies.'
    body+=['','## Pre-registered prediction','Written **before** the check runs.' if not pn else pn,
      '- Under the claimant\'s model: '+c['p_claim'].strip(),'- Under the opposing model: '+c['p_opp'].strip(),'- Result that would change a verdict: '+c['p_change'].strip(),'']
    body+=['## Check',c['check'].strip(),'','## Simulator variables implied']+['- '+x for x in c['sim']]
    return '\n'.join(fm+body)+'\n'
ALL=[]
def add(**c): ALL.append(c)
def write_all():
    os.makedirs(OUT,exist_ok=True)
    for c in ALL:
        for m in prose_check(c): print('  PROSE-UNVERIFIED:',m)
        fn=os.path.join(OUT,f"{c['id']}-{c['slug']}.md")
        open(fn,'w').write(render(c))
    print(len(ALL),'files; unverified quotes:',len(BAD))
    for b in BAD: print('  MISSING:',b[:140])
