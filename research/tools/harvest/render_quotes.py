import os
import json,sys,collections
sys.path.insert(0,os.environ.get("EVO_WORK","work")+'')
from quotes_data import SRC
rows=json.load(open(os.environ.get("EVO_WORK","work")+'/qrows.json'))
g=collections.OrderedDict()
for r in rows: g.setdefault(r[1],[]).append(r)
out=['# Verbatim quotes: critics, allies and adjacent commentators','',
'Harvested 2026-10-07 (R1 pass 2, critics/allies slice). Every quote is <=60 words and was machine-checked as an exact substring (after whitespace and curly-quote normalisation) of the local raw copy listed in `bib-critics.md`.','',
'**Locator conventions.** `para N` = Nth text block of the article body in reading order (blocks split at paragraph/heading/list-item boundaries; footnotes come last). `t=HH:MM:SS` = start of the ~20 s auto-caption chunk containing the quote; auto-captions contain recognition errors (e.g. "hloid" = "haploid") that are preserved verbatim. `PDF pN` = page N. `post/comment <id>` = Reddit/Discourse/YouTube object id. `PS` = Peaceful Science.','',
'**Tags.** `secondhand` = the quoted words were spoken/written by someone other than the source author (shown in the Speaker field) or the source is a repost. Branch IDs refer to `docs/research/hierarchy.yaml` (A..H); `adhom` = about the person/process, not the math; `epistemic` = a statement of the speaker\'s own competence or method.','',
'Notes beginning "Check:" or containing "=" record arithmetic re-done by the harvester from the quoted numbers only; they are not verdicts (R4 does verdicts).','']
for k,rs in g.items():
    lab,url,date=SRC[k]
    out+=[f'## {k}: {lab}',f'URL: {url}  ',f'Date: {date}','']
    for qid,src,loc,br,who,q,note,fl in rs:
        tag=' `secondhand`' if fl=='second' else ''
        out.append(f'- **{qid}** | {loc} | branch {br} | {who}{tag}')
        out.append(f'  > "{q}"')
        if note: out.append(f'  - note: {note}')
    out.append('')
open('/home/na/projects/evo-sim/docs/research/sources/quotes-critics.md','w').write('\n'.join(out))
print(len(rows))
