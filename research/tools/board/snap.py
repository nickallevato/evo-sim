import glob,re,yaml,json,sys,os
out={}
for p in glob.glob('/home/na/projects/evo-sim/docs/research/claims/*.md'):
    if os.path.basename(p).startswith('_'): continue
    t=open(p).read(); m=re.match(r"^---\n(.*?)\n---\n",t,re.S); fm=yaml.safe_load(m.group(1))
    v=fm.get('verdicts') or {}
    out[str(fm['id'])]={'side':fm['side'],**{k:str(v.get(k,'')).split()[0] for k in ('internal','fidelity','external')}}
json.dump(out,open(sys.argv[1],'w'),indent=0)
