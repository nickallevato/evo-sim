import json,re,os,glob,hashlib
R='/home/na/projects/evo-sim/sources/raw/day'
rows=json.load(open('zrows.json'))
skip={18888781,18724496,18724487,18788051,18727817,18717939,19022126,18911901,18724454,18924026,18930279}
branch={22903977:'B,F',23003785:'A,E',18403579:'B',22129121:'B',18320599:'C,B',18441321:'A',18168236:'H',18203514:'A,C',18202768:'A,C',18382379:'B',18452504:'A',18166426:'A,C',18470617:'A,E',23105291:'A,E',18525262:'B',18517618:'B',18209114:'A,C',18166234:'A,C',18165980:'A,G',19984826:'B,F,H',18525185:'B',23020792:'E',23034852:'E',18637297:'B',18637333:'B,A',18525547:'B',18429937:'B',23046531:'C',18167588:'G',23188201:'B,F'}
notes={18165980:'First MITTENS paper: p^n with p=0.02, n=2e7; d=0.45; G_f=1600; 91 fixations. Docx; para refs = line numbers of .txt',
23003785:'MITTENS 3.0; Zenodo record modified 2026-10-04 (created 2026-09-28) - same record id, content may have been revised after first fetch; 2 files (main + addendum)',
18167588:'Bernoulli Barrier: n=157,000, p=0.5, 14.7x vs 1,570x, ~230 simultaneous sweeps. Does NOT contain 0.02^(2e7)',
22129121:'Hard Limits; no reference list found in text (check)',
22903977:'E[F(T)]=muL int F_X; approx muL(T-4Ne)',
18168236:'Haldane 300; 487 with d',
18525262:'RRME k=0.743 mu; two versions (18517618 2026-02-07, identical file sha256)',
18517618:'Earlier version of 18525262; byte-identical file',
18202768:'Earlier version of 18203514 (Bio-Cycle); file BioCycle_(004).docx',
23105291:'LTEE data paper; 5,496 whole-population fixations/723,000 pop-gens; 2 files (pdf + xlsx)',
23046531:'aDNA AADR v62.0 and v66.p1; reports 1 (v62) and 3 (v66) completions from MAF>=10%',
18166234:'d definition integral',
18525547:'k = mu N/Ne; recalibrate CHLCA 6.5 Mya -> 68 kya',
18429937:'k = mu N/Ne preprint',
19984826:'Kimura calculator (3-term min). Day blog 2026-05-07 retracts Term 3 use',
}
sha={}
for l in open('zsha.txt'): h,f=l.split(); sha[f]=h
for f in ['zenodo-18202768.docx','zenodo-18517618.docx']: sha[f]=hashlib.sha256(open(f'{R}/{f}','rb').read()).hexdigest()
out=[]
def row(*c): out.append('| '+' | '.join(str(x).replace('|','/') for x in c)+' |')
allrows=list(rows)+[dict(id=18202768,concept='18202767',vi=0,last=False,created='2026-01-09',files=[('BioCycle_(004).docx',16171,'','')],title='The Bio-Cycle Fixation Model: Empirical Validation of a Generation Overlap Correction for Allele Frequency Dynamics',date='2025-12-25',doi='10.5281/zenodo.18202768'),
 dict(id=18517618,concept='18517617',vi=0,last=False,created='2026-02-07',files=[('RRME_Paper_002.docx',13901,'','')],title='The Real Rate of Molecular Evolution',date='2026-02-07',doi='10.5281/zenodo.18517618')]
allrows.sort(key=lambda r:r['date'])
for r in allrows:
    i=r['id']; 
    for k,(fn,sz,ck,url) in enumerate(r['files']):
        ext=fn.rsplit('.',1)[1]; loc=f"zenodo-{i}"+("" if k==0 else f"-f{k+1}")+"."+ext
        key=f'Z{i}'+('' if k==0 else f'-f{k+1}')
        if i in skip:
            row(key,'zenodo',r['date'],r['title'],f'https://zenodo.org/records/{i}','concept '+str(r['concept']),'-','-','not-downloaded (out-of-scope: philosophy/theology)','-','listed only; file '+fn)
            break
        ver=f"v{r['vi']+1} of concept {r['concept']}"+("" if r['last'] else " (superseded)")
        n=notes.get(i,'')
        if k>0: n='Additional file of '+f'Z{i}: '+fn
        else: n=(n+'; ' if n else '')+f'orig. file {fn} ({sz} B); DOI {r["doi"]}; text: {loc.rsplit(".",1)[0]}.txt' if ext!='xlsx' else f'orig. file {fn} ({sz} B)'
        row(key,'zenodo',r['date'],r['title'],f'https://zenodo.org/records/{i}',ver,'sources/raw/day/'+loc,sha[loc],'ok',branch.get(i,''),n)
z='\n'.join(out)
open('zenodo_table.md','w').write(z)
print(len(out))
