import sys,re
f=sys.argv[1]; pat=re.compile(sys.argv[2]); ctx=int(sys.argv[3]) if len(sys.argv)>3 else 0
t=open(f'/home/na/projects/evo-sim/sources/raw/day/zenodo-{f}.txt',errors='replace').read()
pages=t.split('\f')
n=0
for pi,pg in enumerate(pages,1):
    lines=pg.split('\n')
    for i,l in enumerate(lines):
        if pat.search(l):
            n+=1
            c=' | '.join(x.strip() for x in lines[max(0,i-ctx):i+ctx+1])
            print(f'[p{pi} l{i+1}]',re.sub(r'\s+',' ',c)[:int(sys.argv[4]) if len(sys.argv)>4 else 400])
