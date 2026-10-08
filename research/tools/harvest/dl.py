import json,subprocess,os,time,sys
R='/home/na/projects/evo-sim/sources/raw/day'
skip={18888781,18724496,18724487,18788051,18727817,18717939,19022126,18911901,18724454,18924026,18930279}
rows=json.load(open('zrows.json'))
for r in rows:
    if r['id'] in skip: continue
    for i,(k,sz,ck,url) in enumerate(r['files']):
        ext=k.rsplit('.',1)[1]
        out=f"{R}/zenodo-{r['id']}" + ("" if i==0 else f"-f{i+1}") + "." + ext
        subprocess.run(['curl','-sL',url,'-o',out],check=True)
        print(out,os.path.getsize(out),sz,ck)
        time.sleep(1.2)
