import json,sys
tot=0
for p in (1,2):
    d=json.load(open(f'z/p{p}.json'))
    if p==1: print('total',d['hits']['total'])
    for r in d['hits']['hits']:
        m=r['metadata']
        cr='; '.join(c.get('name') or c['person_or_org']['name'] for c in m['creators'])
        fs=[(f['key'],f['size']) for f in r.get('files',[])]
        print(r['id'],'|',r.get('doi'),'|',m['title'],'|',m.get('publication_date'),'|',m.get('version'),'|',cr,'|',fs)
