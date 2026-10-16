#!/usr/bin/env python3
"""Fast scratch exact scan of complete-angle q=525..999 at faces (2,3)."""
from collections import Counter
from pathlib import Path
import contextlib, importlib.util, io
HERE=Path(__file__).resolve().parent

def load(name,fn):
    s=importlib.util.spec_from_file_location(name,HERE/fn); m=importlib.util.module_from_spec(s)
    with contextlib.redirect_stdout(io.StringIO()): s.loader.exec_module(m)
    return m
E=load('e2','verify_target_c_support7_h6_two_face_23_extension2_2026_09_19.py')
A,O,K=E.A,E.O,E.BRANCH_KEYS
T=1e-8

def exact_cell(system):
    dead={}; certs=[]
    for f in (2,3):
        d=set()
        for i,(o,s) in enumerate(K):
            cl=A.BRANCH[(f,o,s)]; mar,res=O.numerical_candidate(system,cl)
            if mar is None: return None,('solver-local',f,i,res.message)
            if mar<=T:
                c=A.exactify_support(system,cl,res)
                if c is not None: d.add(i); certs.append(c)
        dead[f]=d
    live={f:[i for i in range(20) if i not in dead[f]] for f in (2,3)}
    for i in live[2]:
        o2,s2=K[i]
        for j in live[3]:
            o3,s3=K[j]; cl=A.BRANCH[(2,o2,s2)]+A.BRANCH[(3,o3,s3)]
            mar,res=O.numerical_candidate(system,cl)
            if mar is None:return None,('solver-pair',i,j,res.message)
            if mar>T:return None,('feasible',i,j,mar)
            c=A.exactify_support(system,cl,res)
            if c is None:return None,('exactify',i,j,mar)
            certs.append(c)
    return (len(live[2]),len(live[3]),certs),None

def main():
    states=O.tri.collect_survivors(); assert len(states)==14174
    prev=O.complete_angle_survivors(states); assert len(prev)==5692
    known={q for q,*_ in A.CANDIDATES}|{q for q,*_ in E.T.CANDIDATES}|{q for q,*_ in E.E.CANDIDATES}|{q for q,*_ in E.CANDIDATES}
    out=[]; fail=[]; num=0
    for q in range(525,1000):
        if q in known: continue
        idx=prev[q]; st=states[idx]; sys=O.C.build_system(st)
        # Cheap numerical test first: if any product of numerically-live local branches is feasible, skip.
        live={}
        bad=False
        for f in (2,3):
            a=[]
            for i,(o,s) in enumerate(K):
                mar,res=O.numerical_candidate(sys,A.BRANCH[(f,o,s)])
                if mar is None: bad=True; break
                if mar>T:a.append(i)
            if bad:break
            live[f]=a
        if bad:continue
        for i in live[2]:
            o2,s2=K[i]
            for j in live[3]:
                o3,s3=K[j]; mar,res=O.numerical_candidate(sys,A.BRANCH[(2,o2,s2)]+A.BRANCH[(3,o3,s3)])
                if mar is None or mar>T: bad=True; break
            if bad:break
        if bad:continue
        num+=1
        ex,why=exact_cell(sys)
        if ex is None: fail.append((q,idx,why)); continue
        # Only count cells that survived the older order-hull stage; this is expensive, so do it after exact pair closure.
        if not A.survives_previous_order_hull(sys): continue
        l2,l3,cs=ex; pat=''.join(map(str,st[5])); forced=Counter('zero' if v==0 else 'negative' for v,_ in cs)
        out.append((q,idx,st[1],pat,l2,l3,len(cs),dict(forced),max(d for _,d in cs)))
    print('numerical candidates before order-hull duplicate removal:',num)
    print('exact new-compatible candidates:',len(out))
    for x in out:print('EXACT',repr(x))
    print('failures:',len(fail))
    for x in fail:print('FAIL',repr(x))
if __name__=='__main__':main()
