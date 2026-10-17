#!/usr/bin/env python3
from collections import Counter
from hashlib import sha1
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations
from pathlib import Path

HERE=Path(__file__).resolve().parent
BASE=HERE/"verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus1_d0p2_selected_pair_orientation_2026_09_28.py"
EXPECTED_BASE_BLOB="867e8e583f6073c92b1f7afbf2aaf536e2567fa9"
raw=BASE.read_bytes()
assert sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()==EXPECTED_BASE_BLOB
sp=spec_from_file_location("base",BASE); m=module_from_spec(sp); sp.loader.exec_module(m)

SUPPORTS=[
("S2",[((0,1,2,3),3),((0,1,2,4),3),((0,1,3,4),2),((0,2,3,4),1)]),
("S3",[((0,1,2,3),3),((0,1,2,4),3),((0,1,3,4),2),((0,2,3,5),1)]),
("S4",[((0,1,2,3),3),((0,1,2,4),3),((0,1,3,5),2),((0,2,3,4),1)]),
("S5",[((0,1,2,3),3),((0,1,2,4),2),((0,1,3,4),2),((0,2,3,4),2)]),
("S6",[((0,1,2,3),3),((0,1,2,4),2),((0,1,3,4),2),((0,2,3,4),1),((1,2,3,4),1)]),
("S7",[((0,1,2,3),3),((0,1,2,4),2),((0,1,3,4),2),((0,2,3,5),2)]),
("S8",[((0,1,2,3),2),((0,1,2,4),3),((0,1,3,5),3),((0,1,4,5),1)]),
]
EXPECTED={
"S2":(9,531,0,0,0),"S3":(9,1296,189,117,72),"S4":(9,1314,180,54,126),
"S5":(27,1593,0,0,0),"S6":(81,4755,0,0,0),"S7":(27,4158,621,0,621),
"S8":(9,1134,117,9,108)}
REQ=((7,4),(6,3),(4,2),(3,1))

def structural_ok(tm,em,rt):
    rm=tm&~em; r=rm.bit_count()
    return max(0,r-5)<=min(r,m.h_rank(rm),rt-5)

def extension_possible(U):
    extra=4-len(U)
    for z,need in REQ:
        for Z in combinations(range(9),z):
            rr=m.exact_rank([tuple(row[i] for i in Z) for row in U])
            if rr+extra<need: return False
    return True

def run(name,rep):
    c=Counter()
    for ext in m.oriented_exts(rep):
        c["o"]+=1
        T=tuple(sorted({b for e in ext for b,v in enumerate(m.QCOMP[e]) if v!=(0,0)}))
        tm=sum(1<<b for b in T); rt=m.h_rank(tm)
        V=[m.empty_key(ext,b) for b in T]
        states=[((),0)]
        for j,b in enumerate(T):
            add=[]
            for U,em in states:
                U2=m.union_key(U,V[j])
                if len(U2)<=4: add.append((U2,em|(1<<b)))
            states+=add
        c["e"]+=len(states)
        for U,em in states:
            if not structural_ok(tm,em,rt): continue
            c["s"]+=1; c[len(U)]+=1
            if extension_possible(U): c["p"]+=1
    got=(c["o"],c["e"],c["s"],c[3],c[4])
    assert got==EXPECTED[name],(name,got,c)
    assert c["p"]==0,(name,c)
    print(name,dict(c))

for name,rep in SUPPORTS: run(name,rep)
print("PASS: corrected E_b<=P certificate closes S2--S8")
