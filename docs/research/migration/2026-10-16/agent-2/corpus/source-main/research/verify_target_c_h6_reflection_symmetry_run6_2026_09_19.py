#!/usr/bin/env python3
"""Scratch exact audit: reflect every committed adaptive/two-face H6 exclusion."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import contextlib, importlib.util, io
HERE=Path(__file__).resolve().parent

def load(name,fn):
    s=importlib.util.spec_from_file_location(name,HERE/fn); m=importlib.util.module_from_spec(s)
    with contextlib.redirect_stdout(io.StringIO()): s.loader.exec_module(m)
    return m
E2=load('e2','verify_target_c_support7_h6_two_face_23_extension2_2026_09_19.py')
A,O,K=E2.A,E2.O,E2.BRANCH_KEYS
B=O.tri.base
R={0:0,1:5,2:4,3:3,4:2,5:1,6:6,7:7}
T=1e-8

def ed(a,b): return (a,b) if a<b else (b,a)
def sig(st):
    _,g,missing,raws,chi,pat,signs=st
    return (g,tuple(sorted(missing)),tuple(tuple(x) for x in raws),tuple(pat),tuple(sorted(signs.items())))
def reflect_state_sig(st):
    _,g,missing,raws,chi,pat,signs=st
    rr=[None]*6
    for v in range(6):
        rv=R[v]
        rr[rv]=tuple(R[x] for x in reversed(raws[v]))
    rr=tuple(rr)
    assert rr in B.ORDER_TYPES
    chi2=B.ORDER_TYPES[rr]
    # A reflection reverses every oriented triple.
    for a,b,c in combinations(range(8),3):
        assert B.chi_value(chi2,R[a],R[b],R[c]) == -B.chi_value(chi,a,b,c)
    mm=frozenset(ed(R[a],R[b]) for a,b in missing)
    ss={ed(R[a],R[b]):z for (a,b),z in signs.items()}
    pp=tuple(sorted(8-p for p in pat))
    return (g,tuple(sorted(mm)),rr,pp,tuple(sorted(ss.items())))

def exact_one(system,face):
    certs=[]
    for o,s in K:
        cl=A.BRANCH[(face,o,s)]; mar,res=O.numerical_candidate(system,cl)
        if mar is None or mar>T:return None
        c=A.exactify_support(system,cl,res)
        if c is None:return None
        certs.append(c)
    return certs

def exact_pair(system,faces):
    a,b=faces; dead={}; certs=[]
    for f in faces:
        d=set()
        for i,(o,s) in enumerate(K):
            cl=A.BRANCH[(f,o,s)]; mar,res=O.numerical_candidate(system,cl)
            if mar is None:return None
            if mar<=T:
                c=A.exactify_support(system,cl,res)
                if c is not None:d.add(i);certs.append(c)
        dead[f]=d
    la=[i for i in range(20) if i not in dead[a]]; lb=[i for i in range(20) if i not in dead[b]]
    for ia in la:
        oa,sa=K[ia]
        for ib in lb:
            ob,sb=K[ib]; cl=A.BRANCH[(a,oa,sa)]+A.BRANCH[(b,ob,sb)]
            mar,res=O.numerical_candidate(system,cl)
            if mar is None or mar>T:return None
            c=A.exactify_support(system,cl,res)
            if c is None:return None
            certs.append(c)
    return la,lb,certs

def main():
    states=O.tri.collect_survivors(); assert len(states)==14174
    sm={sig(st):i for i,st in enumerate(states)}; assert len(sm)==len(states)
    # Check reflection is an involution on all 14,174 generic states.
    refl_idx=[]
    for i,st in enumerate(states):
        j=sm[reflect_state_sig(st)]; refl_idx.append(j)
    assert all(refl_idx[refl_idx[i]]==i for i in range(len(states)))

    prev=O.complete_angle_survivors(states); assert len(prev)==5692
    qof={idx:q for q,idx in enumerate(prev)}
    assert len(qof)==5692

    sources=[]
    for q,idx,f,pat in A.CANDIDATES:sources.append((q,(f,)))
    for q,idx,pair,g,pat in E2.T.CANDIDATES:sources.append((q,tuple(pair)))
    for q,*rest in E2.E.CANDIDATES:sources.append((q,(2,3)))
    for q,*rest in E2.CANDIDATES:sources.append((q,(2,3)))
    known={q for q,_ in sources}; assert len(known)==135

    proposed={}
    for q,faces in sources:
        idx=prev[q]; ridx=refl_idx[idx]; assert ridx in qof
        rq=qof[ridx]
        rfaces=tuple(R[f] for f in faces)
        if rq not in known:proposed.setdefault(rq,rfaces)
    print('symmetry-new proposed:',len(proposed))

    out=[]; failed=[]; forced=Counter(); total_certs=0
    for q in sorted(proposed):
        faces=proposed[q]; idx=prev[q]; st=states[idx]
        system=O.C.build_system(st)
        assert A.survives_previous_order_hull(system)
        if len(faces)==1:
            cs=exact_one(system,faces[0])
            if cs is None: failed.append((q,idx,faces)); continue
            live=()
        else:
            ex=exact_pair(system,faces)
            if ex is None: failed.append((q,idx,faces)); continue
            la,lb,cs=ex; live=(len(la),len(lb))
        total_certs+=len(cs)
        for v,d in cs:forced['zero' if v==0 else 'negative']+=1
        pat=''.join(map(str,st[5]))
        out.append((q,idx,faces,st[1],pat,live,len(cs),max(d for _,d in cs)))
    print('exact symmetry-new:',len(out))
    print('failures:',len(failed),failed)
    print('graphs:',dict(Counter(states[prev[q]][1] for q,*_ in out)))
    print('patterns:',dict(Counter(''.join(map(str,states[prev[q]][5])) for q,*_ in out)))
    print('certificates:',total_certs,dict(forced))
    for x in out:print('EXACT',repr(x))
if __name__=='__main__':main()
