import sys,re,glob
pat=sys.argv[1]
for f in sorted(glob.glob(sys.argv[2])):
    n=0
    for line in open(f,encoding='utf-8',errors='replace'):
        if line.strip():
            n+=1
            if re.search(pat,line):
                i=re.search(pat,line).start()
                print(f,'¶%d'%n,line.strip()[max(0,i-60):i+260].replace('\n',' '))
