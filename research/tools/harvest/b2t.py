import sys,re,html,glob,os
# extract entry-content text from a voxday post html
for f in sys.argv[1:]:
    s=open(f,errors='replace').read()
    m=re.search(r'<h1 class="entry-title"[^>]*>(.*?)</h1>',s,re.S)
    title=html.unescape(re.sub('<[^>]+>','',m.group(1))) if m else ''
    a=s.find('class="entry-content"')
    if a<0: a=s.find('entry-content')
    if a>=0: a=s.find('>',a)+1
    b=s.find('<footer class="entry-meta"',a)
    if b<0: b=s.find('class="entry-meta"',a)
    body=s[a:b] if a>=0 else s
    body=re.sub(r'<script.*?</script>|<style.*?</style>','',body,flags=re.S)
    body=re.sub(r'<br\s*/?>|</p>|</div>|</li>|</h\d>|</blockquote>','\n',body)
    body=re.sub(r'<img[^>]*alt="([^"]*)"[^>]*>',r'[IMG: \1]',body)
    body=re.sub(r'<a [^>]*href="([^"]*)"[^>]*>(.*?)</a>',lambda m:m.group(2)+' [URL: '+m.group(1)+']',body,flags=re.S)
    body=re.sub(r'<[^>]+>','',body)
    body=html.unescape(body)
    body=re.sub(r'[ \t]+',' ',body); body=re.sub(r'\n\s*\n+','\n\n',body).strip()
    out=sys.argv[0]
    open(f[:-5]+'.txt','w').write('TITLE: '+title+'\n\n'+body+'\n')
