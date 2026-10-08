import re,glob,json,os
exc={ # slug-prefix : reason
'2019-01-26-tens':'news','2020-03-18':'news','2021-05-04':'offtopic','2022-01-20':'offtopic','2022-02-06':'rhetoric','2022-04-21':'empty','2022-04-23':'quote-only',
'2023-07-17':'cosmology','2023-08-04':'rhetoric','2023-08-14':'offtopic','2023-10-06':'personal','2024-01-31':'offtopic','2024-04-16':'news','2023-04-04':'news',
'2022-07-12':'news','2024-05-13':'offtopic','2025-06-22':'news','2025-07-17':'news','2025-08-07':'news','2025-08-18':'offtopic','2025-09-26':'news','2025-10-07':'news',
'2025-12-17':'praise','2025-12-19':'ai-praise','2026-01-23':'meme','2026-02-11':'bookreview','2026-05-24':'rhetoric','2026-09-12-the-uncomfortable':'rhetoric','2026-09-24':'mailbag-rhetoric','2026-10-03-better':'link-only','2025-10-02':'link-only',
}
extra_keep=['2025-12-27-hardcoded','2026-01-12-rejection','2026-01-14-scientist-wanted','2026-01-16-historic-rigor','2026-02-02-pz-print-editions','2026-02-03-dennis','2026-02-03-the-repro','2026-02-04-response','2026-04-10-clones','2026-04-14-anti','2026-05-01-hardcoded-2','2026-05-14-the-irrelevance','2026-10-01-the-education']
extra_exc_reason={'veriphysics':'offtopic','karma':'offtopic','decay-function':'offtopic','science-is-garbage':'rhetoric','ricardos':'offtopic','gatekeepers':'offtopic','augmentation':'offtopic','no-one-is-ready':'promo'}
evo=set(os.path.basename(u) for u in [])
evo_urls=set(open('evo_urls.txt').read().split())
def slugfile(u):
    d=re.sub(r'https://voxday.net/(\d{4})/(\d{2})/(\d{2})/.*',r'\1-\2-\3',u); s=re.sub(r'https://voxday.net/\d{4}/\d{2}/\d{2}/([^/]*)/?',r'\1',u)[:60]
    return f'blog-{d}-{s}'
res=[]
for u in sorted(evo_urls|set(open('extra_urls.txt').read().split()),key=lambda u:re.sub(r'.*net/','',u)):
    sf=slugfile(u); base=sf[5:]; src='evotag' if u in evo_urls else 'search'
    keep=True; reason=''
    if u in evo_urls:
        for k,r in exc.items():
            if base.startswith(k): keep=False; reason=r
    else:
        keep=any(base.startswith(k) for k in extra_keep)
        if not keep:
            reason='offtopic'
            for k,r in extra_exc_reason.items():
                if k in base: reason=r
            if base.startswith('2025-11-07') or base.startswith('2025-11-22') or base.startswith('2025-12-26'): reason='ai-rhetoric'
    res.append((sf,u,src,keep,reason))
json.dump(res,open('class.json','w'))
print(len(res),sum(1 for r in res if r[3]),sum(1 for r in res if not r[3]))
print([r[0] for r in res if r[2]=='evotag' and not r[3]])
