import re,sys,html,glob
seen={}
pat=re.compile(r'entry-title"><a href="(https://voxday.net/(\d{4})/(\d\d)/(\d\d)/([^"/]*)/?)"[^>]*>(.*?)</a>')
for n in range(1,26):
    for m in pat.finditer(open(f'{sys.argv[1]}{n}.html',errors='replace').read()):
        seen.setdefault(m.group(1),(f'{m.group(2)}-{m.group(3)}-{m.group(4)}',html.unescape(re.sub('<[^>]+>','',m.group(6))),n))
for u,(d,t,n) in sorted(seen.items(),key=lambda x:x[1][0]): print(d,n,u,'|',t)
