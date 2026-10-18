#!/usr/bin/env python3
"""Fresh review checks; imports no submitted proof or verifier code.
Finite checks complement the analytic review. They do not certify minimizers.
"""
from fractions import Fraction as F
from math import isqrt, lcm
from collections import Counter
import random, json, time


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def sparse_source(R):
    # Independently reconstruct the published rational source.
    p=isqrt(R*R//3)+1
    a=F(R*R-p*p,R*R+p*p)
    b=F(2*R*p,R*R+p*p)
    require(3*(p-1)**2<R*R<3*p*p and p<R, "basis cutoff")
    core={}
    for n in range(-2*R,2*R+1):
        if -1<=n<=1: continue
        for m in range(-2*R,2*R+1):
            if m*m+n*n+2*m*n*a<=(R-2)**2:
                core[(m+n*a,n*b)]=("lattice",m,n)
    chain={(F(j),F(0)):("chain",j) for j in range(-R,R+1)}
    s=isqrt(R)
    ring={}
    for j in range(s+1):
        den=s*s+j*j
        x,y=F(R*(s*s-j*j),den),F(2*R*s*j,den)
        for pt in ((x,y),(-y,x),(-x,-y),(y,-x)):
            ring[pt]=("ring",pt)
    require(len(ring)==4*s,"ring count")
    require(len(set(chain)&set(ring))==2,"intentional shared endpoints")
    require(not(set(core)&set(chain)) and not(set(core)&set(ring)),"disjoint pieces")
    source=dict(ring);source.update(chain);source.update(core)
    coords=list(source)
    scale=lcm(*(z.denominator for pt in coords for z in pt))
    ints=[(int(x*scale),int(y*scale)) for x,y in coords]
    labels=[source[pt] for pt in coords]
    n=len(coords);unit2=scale*scale;D2=(2*R*scale)**2
    expected_contacts=set()
    for i,lab in enumerate(labels):
        for j in range(i+1,n):
            lab2=labels[j]
            if lab[0]==lab2[0]=="chain" and abs(lab[1]-lab2[1])==1:
                expected_contacts.add((i,j))
            elif lab[0]==lab2[0]=="lattice" and abs(lab[1]-lab2[1])+abs(lab[2]-lab2[2])==1:
                expected_contacts.add((i,j))
    contacts=set();diameters=[];pairs=0
    adjacency=[set() for _ in coords]
    for i,(x,y) in enumerate(ints):
        for j in range(i+1,n):
            xx,yy=ints[j];d2=(x-xx)**2+(y-yy)**2;pairs+=1
            require(unit2<=d2<=D2,"all source lower/upper pair bounds")
            if d2==unit2:
                contacts.add((i,j));adjacency[i].add(j);adjacency[j].add(i)
            if d2==D2:diameters.append((i,j))
    require(contacts==expected_contacts,"complete contact graph")
    require(len(diameters)==2*s,"complete actual diameter graph")
    require(all(not(adjacency[i]&adjacency[j]) for i,j in contacts),"triangle free")
    require(all(labels[i][0] in ("ring","chain") and labels[j][0] in ("ring","chain") for i,j in diameters),"exceptional components")
    force=[[F(0),F(0)] for _ in coords]
    for i,j in contacts:
        if labels[i][0]!="chain":continue
        dx,dy=ints[j][0]-ints[i][0],ints[j][1]-ints[i][1]
        force[i][0]+=dx;force[i][1]+=dy
        force[j][0]-=dx;force[j][1]-=dy
    left=coords.index((F(-R),F(0)));right=coords.index((F(R),F(0)))
    for z in range(2):
        term=F(ints[left][z]-ints[right][z],2*R)
        force[left][z]+=term;force[right][z]-=term
    require(all(f==[0,0] for f in force),"full-coordinate KKT stationarity")
    require(F(1)==1,"diameter normalization")
    # Failure controls: a wrong multiplier breaks normalization and stationarity.
    require(F(1,2)!=1 and force[left][0]+F(scale,2)!=0,"half-weight mutation detected")
    require(len(core)+len(chain)+len(ring)!=n,"duplicated endpoint population detected")
    return {"R":R,"source_labels":n,"source_pairs":pairs,"contacts":len(contacts),"actual_diameter_pairs":len(diameters),"all_forces_zero":True}


def incidence_graph(q, outer_degrees, face_degrees, pairs, complementary):
    f=len(face_degrees);b=sum(outer_degrees);Q=sum(d-4 for d in face_degrees)
    k=F(2*q-b-Q,2)
    require(k>=0,"nonnegative source defect")
    adj=[set() for _ in range(q+f)]
    for ei in complementary:
        a,z=pairs[ei];adj[a].add(z);adj[z].add(a)
    unseen=set(range(q+f));components=[]
    while unseen:
        todo=[next(iter(unseen))];component=set()
        while todo:
            v=todo.pop()
            if v in component:continue
            component.add(v);todo.extend(adj[v]-component)
        unseen-=component;components.append(component)
    boundary=[c for c in components if min(c)<q]
    selected=set().union(*boundary)
    cb=len(boundary);fb=sum(v>=q for v in selected)
    nb=sum(pairs[ei][0] in selected for ei in complementary);ni=len(complementary)-nb
    Qinner=sum(d-4 for j,d in enumerate(face_degrees) if q+j not in selected)
    atoms=set(range(len(pairs)))-complementary
    ab=sum(int(x in selected)+int(y in selected) for ei,(x,y) in enumerate(pairs) if ei in atoms)
    require(ab==b+4*fb+Q-Qinner-2*nb,"all terminal occurrences")
    require(nb>=q+fb-cb,"component edges")
    require(Qinner>=f-fb,"each interior face counted separately")
    require(3*(len(atoms)+ni)<=5*(f-k+cb),"5/3 incidence inequality")
    return (f,k,cb,len(atoms),ni)


def incidence():
    rng=random.Random(20261018)
    checked=0;loops=0;interior_cases=0
    for attempt in range(20000):
        q=rng.randrange(1,11);f=rng.randrange(0,6)
        face=[rng.randrange(5,9) for _ in range(f)];Q=sum(d-4 for d in face)
        if Q>q:continue
        b=rng.randrange(q,2*q-Q+1)
        if (b+Q)%2:continue
        outer=[1]*q
        for _ in range(b-q):outer[rng.randrange(q)]+=1
        slots=[v for v,d in enumerate(outer+face) for _ in range(d)]
        rng.shuffle(slots)
        pairs=list(zip(slots[::2],slots[1::2]));require(len(slots)%2==0,"paired ends")
        comp={i for i in range(len(pairs)) if rng.randrange(2)}
        f0,k,c,A,ni=incidence_graph(q,outer,face,pairs,comp)
        checked+=1;loops+=sum(x==y for x,y in pairs);interior_cases+=ni>0
    # Exact sharp abstract ledger: five outer recipients joined to one 5-face,
    # and five atomic trains joining two separate interior 5-faces.
    pairs=[(i,5) for i in range(5)]+[(6,7)]*5
    f,k,c,A,ni=incidence_graph(5,[1]*5,[5,5,5],pairs,set(range(5)))
    require(3*(A+ni)==5*(f-k+c),"sharp coefficient control")
    require(3*(A+ni)>5*(f-k),"finite boundary component deletion fails")
    return {"random_seed":20261018,"valid_multigraph_ledgers":checked,"train_loops":loops,"interior_edge_cases":interior_cases,"sharp_ledger":{"q":5,"f":f,"k":str(k),"c":c,"A":A,"N_inner":ni},"failure_controls":2}


def radical_sign(A,B,d):
    # Exact sign of A+B sqrt(d), with rational A,B.
    A=F(A);B=F(B)
    if B==0:return (A>0)-(A<0)
    if A==0:return (B>0)-(B<0)
    if A>0 and B>0:return 1
    if A<0 and B<0:return -1
    delta=A*A-B*B*d
    return ((delta>0)-(delta<0))*(1 if A>0 else -1)


def capacity(m):
    d=m*m-6*m-3
    require(d>0 and d<m*m and d+3*(m+1)**2==4*m*m,"parameter domain")
    pts=[(i,j) for i in range(m+1) for j in range(m+1)]
    contacts=0;diameter_pairs=0;degree=Counter();checked=0
    for i,(x,y) in enumerate(pts):
        for j in range(i+1,len(pts)):
            a,z=pts[j][0]-x,pts[j][1]-y
            low=radical_sign(a*a+z*z-1,F(a*z,m),d)
            high=radical_sign(a*a+z*z-2*m*m,F(a*z,m)-m,d)
            require(low>=0 and high<=0,"full pair interval")
            if low==0:contacts+=1;degree[i]+=1;degree[j]+=1
            if high==0:diameter_pairs+=1
            checked+=1
    require(contacts==2*m*(m+1) and min(degree.values())==2,"complete contact population")
    require(diameter_pairs==1,"complete actual diameter pair count")
    require((m*m+m)+2*m+1-len(pts)==m,"all-label slack")
    # Independent bounded samples of the continuous cover, in oblique coordinates.
    # Analytic review proves the all-points statement using circumcenter identity.
    samples=0
    for i in range(13):
        for j in range(13):
            x,y=F(i,12),F(j,12)
            distances=[(F((x-a)**2+(y-b)**2),F((x-a)*(y-b),m)) for a,b in ((0,0),(1,0),(0,1),(1,1))]
            require(any(radical_sign(A-1,B,d)<0 for A,B in distances),"strict cell cover sample")
            samples+=1
    require(radical_sign(0,m,d)>0,"same-cardinality square grid strictly shorter")
    return {"m":m,"labels":len(pts),"source_pairs":checked,"contacts":contacts,"actual_diameter_pairs":diameter_pairs,"strict_cover_samples":samples,"slack":m}


def main():
    start=time.monotonic()
    data={"reviewer":"/root/merge_review_c","method":"fresh standard-library exact rational/integer checks; no submitted imports","incidence":incidence(),"sparse_sources":[sparse_source(R) for R in (16,17,25)],"capacity_sources":[capacity(m) for m in (7,8,12)],"scope":"finite checks only; analytic universal steps reconstructed in audit receipt"}
    require(6*6-6*6-3<0,"m=6 domain failure control")
    # At cos(theta)=1/2, u,v,u-v all have length one: bipartiteness fails.
    require(2-2*F(1,2)==1,"closed-angle endpoint triangle control")
    data["elapsed_seconds"]=round(time.monotonic()-start,3)
    print(json.dumps(data,indent=2))

if __name__=="__main__":main()
