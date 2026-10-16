#!/usr/bin/env python3
"""Exact all-permutation threshold paths used in polynomial wall rigidity.

No floating rank or singular value is used. The quantitative projection,
stress continuation and arbitrary-cloud classification are analytic.
"""
from itertools import permutations
import json


def plus(dst,src,scale=1):
    for key,value in src.items():
        dst[key]=dst.get(key,0)+scale*value
        if dst[key]==0:del dst[key]


def linear_case(pi):
    m=len(pi)
    def alpha(r):return {} if r in (0,m) else {('a',r):1}
    def t(r):
        d=alpha(r+1).copy();plus(d,alpha(r),-1);return d
    def s(r,j):
        if j==0 or r==m:return {}
        if j==r:return {key:-value for key,value in alpha(r).items()}
        return {('s',r,j):1}
    paths=[]
    for threshold in range(1,m):
        total={};prev=0
        for r,rank in enumerate(pi,1):
            selected=int(rank<threshold);j=prev+selected
            row=s(r,j).copy();plus(row,s(r-1,prev),-1)
            if selected:plus(row,t(r-1))
            plus(total,row);prev=j
        expected={}
        for r,rank in enumerate(pi):
            if rank<threshold:plus(expected,t(r))
        assert total==expected
        paths.append(total)
    g={}
    for r,rank in enumerate(pi):plus(g,t(r),12*(2*rank-(m-1)))
    pathnormal={}
    for path in paths:plus(pathnormal,path,-24)
    assert pathnormal==g
    return len(paths)


def check(m):
    count=0;coverage=0;linear=0;minweight=None;maxweight=0
    for pi in permutations(range(m)):
        count+=1
        weak=set()
        for r in range(2,m+1):
            newrank=sorted(pi[:r]).index(pi[r-1])+1
            for j in range(1,r):
                weak.add((r,j,'B' if newrank<=j else 'A'))
        weights={}
        for threshold in range(1,m):
            selected=0
            for r,rank in enumerate(pi,1):
                enters=rank<threshold;selected+=enters
                if 0<selected<r:
                    key=(r,selected,'B' if enters else 'A')
                    assert key in weak
                    weights[key]=weights.get(key,0)+2
        assert set(weights)==weak
        assert all(2<=w<=2*(m-1) for w in weights.values())
        minweight=min(weights.values()) if minweight is None else min(minweight,min(weights.values()))
        maxweight=max(maxweight,max(weights.values()))
        coverage+=len(weak)
        if m<=6:linear+=linear_case(pi)
    return {'M':m,'permutations':count,'active_weak_rows_covered':coverage,
            'exact_subset_path_linear_identities':linear,
            'min_scaled_normal_weight':minweight,'max_scaled_normal_weight':maxweight}


if __name__=='__main__':
    cases=[check(m) for m in range(2,9)]
    print(json.dumps({'classification':'exact finite exhaustive path/normal certificates',
          'scope':'all permutations M=2,...,8; universal polynomial estimates are analytic',
          'cases':cases},sort_keys=True))
