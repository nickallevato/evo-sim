import sys,re
p=sys.argv[1]
raw=open(p,encoding='utf8',errors='replace').read()
m=re.search(r'class="[^"]*entry-content[^"]*"',raw)
s=m.start() if m else 0
e=re.search(r'class="[^"]*(sharedaddy|entry-footer|post-meta|comments-area|jp-relatedposts)',raw[s:])
raw=raw[s:s+(e.start() if e else len(raw))]
open('/tmp/art.html','w').write(raw)
