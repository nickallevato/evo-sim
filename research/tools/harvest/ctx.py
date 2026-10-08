import sys,re
f,pat=sys.argv[1],sys.argv[2]; w=int(sys.argv[3]) if len(sys.argv)>3 else 250; mx=int(sys.argv[4]) if len(sys.argv)>4 else 8
t=open('/home/na/projects/evo-sim/sources/raw/sources/txt/'+f+'.txt',errors='ignore').read()
t=re.sub(r'\s+',' ',t)
n=0;last=-10**9
for m in re.finditer(pat,t,re.I):
    if m.start()<last+w: continue
    last=m.start()
    s=max(0,m.start()-w);e=min(len(t),m.end()+w)
    print(f'[{m.start()}] ...{t[s:e]}...\n');n+=1
    if n>=mx:break
print('hits shown',n)
