curl -s -m 30 "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=$1&format=json&resultType=lite&pageSize=3" | python3 -c "
import sys,json
d=json.load(sys.stdin)
for r in d['resultList']['result']: print(r.get('pmcid'),r.get('doi'),r.get('isOpenAccess'),r.get('title','')[:80],r.get('journalTitle'),r.get('pubYear'))
"
