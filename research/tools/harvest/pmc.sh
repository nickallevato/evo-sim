#!/bin/bash
# usage: pmc.sh key PMCID
cd /home/na/projects/evo-sim/sources/raw/sources
curl -s -m 60 -o xml/$1.xml "https://www.ebi.ac.uk/europepmc/webservices/rest/$2/fullTextXML"
python3 -I - "$1" <<'PY'
import sys,re,xml.etree.ElementTree as ET
k=sys.argv[1]
try:
    t=ET.parse(f"xml/{k}.xml")
    out=[]
    for el in t.getroot().iter():
        pass
    txt="\n".join(" ".join("".join(p.itertext()).split()) for p in t.getroot().iter() if p.tag in("p","title","article-title","abstract","label","caption") )
    open(f"txt/{k}.txt","w").write(txt)
    print(k,len(txt))
except Exception as e: print(k,"FAIL",e, open(f"xml/{k}.xml").read()[:200])
PY
sleep 1
