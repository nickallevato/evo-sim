import re,sys
L=open('/home/na/projects/evo-sim/sources/raw/sources/txt/Wistar1967.txt',encoding='utf8',errors='replace').read().split('\n')
def page(i):
    for j in range(i,min(i+120,len(L))):
        if re.fullmatch(r'\s*\d{1,3}\s*',L[j]): return L[j].strip(), j+1
    return None
for pat in sys.argv[1:]:
    for i,l in enumerate(L):
        if pat.lower() in l.lower():
            print(pat,'| line',i+1,'| page(approx)',page(i)); 
