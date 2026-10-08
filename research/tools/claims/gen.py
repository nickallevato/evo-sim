import os
OUT='/home/na/projects/evo-sim/docs/research/claims'
made=[]
def edges_s(e):
    if not e: return '[]'
    return '[' + ', '.join('{type: %s, target: %s}'%(t,g) for t,g in e) + ']'
def claim(id,slug,title,side,branch,parent,edges,lb,sourcing,status,v,statement,formal,assump,resp,lit,pre,check,sim,lbnote=''):
    fm=f'''---
id: {id}
title: "{title.replace(chr(92),chr(92)*2).replace(chr(34),chr(92)+chr(34))}"
side: {side}
branch: {branch}
parent: {parent}
edges: {edges_s(edges)}
load_bearing: {'true' if lb else 'false'}{('   # '+lbnote) if lbnote else ''}
sourcing: {sourcing}
status: {status}
verdicts:
  internal: {v[0]}
  fidelity: {v[1]}
  external: {v[2]}
---
'''
    body=f'''
## Statement (verbatim)
{statement.strip()}

## Formal statement
{formal.strip()}

## Assumptions
{assump.strip()}

## Responses
{resp.strip()}

## Primary literature
{lit.strip()}

## Pre-registered prediction
{pre.strip()}

## Check
{check.strip()}

## Simulator variables implied
{sim.strip()}
'''
    fn=f'{OUT}/{id}-{slug}.md'
    open(fn,'w',encoding='utf-8').write(fm+body)
    made.append((id,side,v))
def q(text,src):
    return f'> {text}\n\nSource: {src}\n'
NOLIT='| (none cited in the claim) | n/a | n/a |'
LITH='| Cited work | What it actually says (quote) | Fidelity |\n|---|---|---|\n'
