#!/usr/bin/env python3
"""Independent complete signed nested-chain census, m=1,...,6.

Abstract integer interval chains only; no source realization or all-size claim.
"""
import json

def require(condition):
    if not condition:
        raise RuntimeError("finite chain census or control failed")
rows=[]
for m in range(1,7):
 stack=[((0,m),)];chains=[]
 while stack:
  chain=stack.pop();chains.append(chain);a,b=chain[-1]
  for c in range(a,b):
   for d in range(c+1,b+1):
    if (c,d)!=(a,b):stack.append(chain+((c,d),))
 def strong(pos,neg):
  masks=[1<<i for i in range(m+1)]
  for a,b in pos:masks[a]|=1<<b
  for a,b in neg:masks[b]|=1<<a
  for k in range(m+1):
   for i in range(m+1):
    if masks[i]>>k&1:masks[i]|=masks[k]
  return all(x==(1<<(m+1))-1 for x in masks)
 count=0
 for pos in chains:
  for neg in chains:
   if strong(pos,neg):
    require(pos==neg and [b-a for a,b in pos]==list(range(m,0,-1)))
    count+=1
 require(count==2**(m-1))
 sample=tuple((0,b) for b in range(m,0,-1));require(strong(sample,sample))
 require(not strong(sample,sample[1:]))
 rows.append(dict(m=m,chains=len(chains),pairs=len(chains)**2,strong=count))
print(json.dumps({"scope":"complete abstract finite census, no geometric source or all-size theorem", "cases":rows, "pairs":sum(x["pairs"] for x in rows), "strong":sum(x["strong"] for x in rows), "removal_controls":"pass"},indent=2))
