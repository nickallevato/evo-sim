import re,unicodedata,sys,json
R='/home/na/projects/evo-sim/sources/raw/sources/'
SRC={ # key -> list of text files
 'CSAC2005':['txt/CSAC2005.txt'],'Zeng2021':['txt/Zeng2021.txt'],'Bergeron2023':['txt/Bergeron2023.txt'],
 'Yoo2025':['txt/Yoo2025.txt','supp/Yoo2025/MOESM1.txt'],'Langergraber2012':['txt/Langergraber2012.txt'],
 'BallouxLehmann2012':['txt/BallouxLehmann2012.txt'],'Keightley2012':['abs/Keightley2012.txt'],'Kong2012':['txt/Kong2012.txt'],
 'Nunney2003':['txt/Nunney2003.txt'],'Tenaillon2016':['txt/Tenaillon2016.txt'],'Good2017':['txt/Good2017.txt'],
 'Barrick2009':['abs/Barrick2009.txt'],'Mathieson2015':['txt/Mathieson2015.txt'],'Fu2015':['txt/Fu2015.txt'],
 'Haak2015':['abs/Haak2015.txt'],'Mallick2024':['txt/Mallick2024.txt'],'Scally2012':['txt/Scally2012.txt'],
 'PradoMartinez2013':['abs/PradoMartinez2013.txt'],'Chalub2022':['txt/Chalub2022.txt'],'Wistar1967':['txt/Wistar1967.txt'],
 'Axe2004':['abs/Axe2004.txt'],'Taylor2001':['abs/Taylor2001.txt'],'KeefeSzostak2001':['abs/KeefeSzostak2001.txt'],
 'Kimura1968':['abs/Kimura1968.txt'],
}
def norm(s):
    s=unicodedata.normalize('NFKC',s)
    s=s.replace('ʼ',"'").replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('−','-').replace('–','-').replace('—','-').replace('­','')
    s=re.sub(r'-\s+(?=[a-z])','',s) if False else s
    return re.sub(r'\s+',' ',s).strip()
cache={}
def text(k):
    if k not in cache:
        cache[k]=' '.join(norm(open(R+f,errors='ignore').read()) for f in SRC[k])
    return cache[k]
Q=[] # (key, locator, role, params, quote, note)
def q(key,loc,role,params,quote,note=''):
    Q.append((key,loc,role,params,quote,note))
exec(open('entries.py').read())
bad=0
for e in Q:
    key,loc,role,params,quote,note=e
    nq=norm(quote)
    if len(nq.split())>60: print('TOO LONG',key,loc,len(nq.split())); bad+=1
    if nq not in text(key):
        print('NOT FOUND',key,loc,'::',nq[:90]); bad+=1
print('entries',len(Q),'problems',bad)
json.dump([ (e[0],e[1],e[2],e[3],norm(e[4]),e[5]) for e in Q],open('quotes.json','w'))
