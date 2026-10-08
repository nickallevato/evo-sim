import sys,json,re,html
# usage: h2t.py file.json|html  -> text with paragraph numbers
p=sys.argv[1]
raw=open(p,encoding='utf8',errors='replace').read()
if p.endswith('.json'):
    d=json.loads(raw); raw=d.get('body_html') or ''
raw=re.sub(r'<(script|style)[^>]*>.*?</\1>','',raw,flags=re.S)
raw=re.sub(r'</(p|h\d|li|div|blockquote|tr)>','\n\n',raw)
raw=re.sub(r'<br\s*/?>','\n',raw)
t=re.sub(r'<[^>]+>','',raw); t=html.unescape(t)
paras=[x.strip() for x in re.split(r'\n\s*\n',t) if x.strip()]
for i,x in enumerate(paras,1): print(f'[{i}] {x}')
