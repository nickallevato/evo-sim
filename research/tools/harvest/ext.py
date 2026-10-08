import sys,zipfile,re,html,subprocess
src,dst=sys.argv[1:3]
if src.endswith('.pdf'):
    subprocess.run(['pdftotext','-layout',src,dst],check=True); sys.exit()
z=zipfile.ZipFile(src)
def clean(x): return html.unescape(re.sub(r'<[^>]+>','',x))
out=[]
if src.endswith('.docx'):
    x=z.read('word/document.xml').decode('utf8','replace')
    for p in re.findall(r'<w:p[ >].*?</w:p>',x,flags=re.S):
        p=re.sub(r'<w:tab/>','\t',p)
        t=''
        for r in re.findall(r'<w:r[ >].*?</w:r>|<m:t(?: [^>]*)?>[^<]*</m:t>',p,flags=re.S):
            txt=''.join(clean(m) for m in re.findall(r'<(?:w|m):t(?: [^>]*)?>[^<]*</(?:w|m):t>',r)) if r.startswith('<w:r') else clean(r)
            if 'w:val="superscript"' in r and txt: txt='^{'+txt+'}'
            elif 'w:val="subscript"' in r and txt: txt='_{'+txt+'}'
            t+=txt
        # footnote-free; equation text is concatenated
        out.append(t)
elif src.endswith('.odt'):
    x=z.read('content.xml').decode('utf8','replace')
    x=re.sub(r'<text:(?:tab|s)[^>]*/>',' ',x)
    for p in re.findall(r'<text:(?:p|h)[ >].*?</text:(?:p|h)>',x,flags=re.S):
        out.append(clean(p))
    for n in z.namelist():
        if re.match(r'Object \d+/content.xml',n):
            m=z.read(n).decode('utf8','replace')
            a=re.findall(r'<annotation[^>]*>(.*?)</annotation>',m,flags=re.S)
            out.append('[MATH '+n+'] '+(clean(a[0]) if a else clean(m)))
open(dst,'w').write('\n'.join(out))
