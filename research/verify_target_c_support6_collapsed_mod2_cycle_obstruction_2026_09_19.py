#!/usr/bin/env python3
"""Exact certificate for a second collapsed support-six root cell and its mod-2 train obstruction.

Logical tests use Fraction arithmetic.  The script:
  1. certifies a regular local solution of the six collapsed pentagon closures by a
     Banach contraction on a 1e-10 box after fixing two train angles;
  2. certifies the strict contact-pentagon turn inequalities and the full face
     rotation system on that box;
  3. certifies exactly which train-pair crossings can occur in three selected
     pairs of edge-disjoint relation cycles; and
  4. checks the resulting three mod-2 plane-intersection equations XOR to 0=1.

This excludes the entire certified parameter box from any global stopped-train
realization.  It does not classify all collapsed support-six cells.
"""
from fractions import Fraction as Q
from math import factorial

EDGES=((0,1),(0,2),(0,4),(0,5),(1,2),(1,3),(1,5),(2,3),(2,4),(3,4),(3,5),(4,5))
FIXED={(0,1):Q('-1.93018848'),(0,2):Q('1.02838679')}
VAR_EDGES=tuple(e for e in EDGES if e not in FIXED)
X0=tuple(Q(s) for s in (
'-2.2622479662783364','2.1256745629003877','-1.0409722289425172','2.8026180119778759',
'-2.7238097420853755','1.2700445670047056','-1.8490278001261384','2.1429491086277803',
'0.46329367519815784','-2.041770793051696'))
SIGNS=(1,1,1,-1,-1,-1)
R=Q(1,10**10)

C_STR='''
0.5558431732014259551988288876600563526154,-0.8967564909385432603272647611447609961033,0,0,0,0,0,0,0,0
-0.6727600573844125797506876551778987050056,-0.8127285785692304198590818486991338431835,0,0,0,0,0,0,0,0
-0.008229595974752052650602607286600687075406,0.01327702482276643843051022741974520613439,0.05631425300801447958454204467670933809131,0.02499879435262573196263602426370198372751,-0.3475856678380201403300020501774270087481,-1.264079454742543351386530048330314457417,0.05263713727926352253794206603743077721447,0.02629528518136375198066545522124215494841,0.03071907611408935742658421474970964482054,0.06032901394797075822484799800804466940463
-0.01191142163613433634095084556747679016553,0.01921701153040598214483125616425240878016,-1.249737964298717418643036580760963261127,-0.5547785985854517543103270327264908701181,-0.5030914588028412293141400368767790496349,-1.8296139218993539010682525258744135499,0.07618638117544811183545760968627291731536,0.0380594903806386955502638613779708975926,0.04446243399919107275319873906482825987041,0.08731951413303255804532199135792325250804
0.007740263755751443028318981021129729924724,-0.01248757221316293061774693740062502911314,1.320673344212644595430106164712924510241,-0.5078350484711714463159637489297892898321,0.326918205345596346589331915311049669981,1.188917222419115571341308168484829366207,-0.04950733026738551173506763802834029775113,-0.02473176611110488448685984508301771711558,-0.02889251819719125188856700958695000736043,-0.05674184753593201901988862800862989388406
-0.2642084164049660621742532384814694523811,0.4262544253392999138441155082546174526215,1.807950190255166900143990460492204874754,0.802577901540260874035936922155087813735,1.03782766954128446990068823652109131217,2.117496521608752679810550034744665026665,1.689897624052443481090790555754210799932,0.844201304413905728729616839700611308217,0.9862256274095775321342216557241044938564,1.936842742628891445022532025177497416735
-0.2698272935690134155528596693329745903611,0.435319508462700788253840755714918486774,1.846399571149184737350879004225134849548,0.8196461944610342609252029433264397084713,1.758958350596761643913623629487119615078,0.9689446320126527956162476584722753614187,1.725836400335831077867965177574660629034,0.8621547954335094798850036568182986229658,1.00719952646946309116060547239612787962,1.978033260345888111331191794306505471468
-0.2005203379564360066655837044891086407006,0.3235047641080986968731281194777693599463,0.4093612359812716650075969937461195513606,0.1817219763667311804855586387930088676512,0.3899748330160823783785417617764323949814,0.2148226084732283713840672589867608621716,0.3826314374105007631854391547676641494036,0.191146465900758039113682684728701133281,0.7484935521749324083273791075043845921755,1.469962110234713792422667211212683469057
-0.1962980989413599941517674096758128143847,0.3166929142453833723180878223502077162266,2.163966623230651808995617102482356131077,0.9606192697324824614213412132812663912773,1.110075261243024247193034170777536928654,2.760049020367866923209021479124203324318,0.7108706635527247685857332726300228387117,1.472957124717160226623491325881332159042,0.7327329629462605575795919321535620838404,1.43900998120995149420764391834381967783
0.3785233918355786486564795723097631707788,-0.6106817983309505981637244076409842818975,1.606086961274804991717246593907475471497,0.71296759723738944991566768294433131814,1.530026391070169911046150446054525673389,0.8428345435025005327744906935549806803465,1.501215329110832330528069178399164229631,0.7499436184793319970509628547006286680698,1.502793156786277561920428524899762123823,0.7474936134929480724409245340211782604456
'''.strip()
C=tuple(tuple(Q(x) for x in line.split(',')) for line in C_STR.splitlines())
assert len(C)==10 and all(len(row)==10 for row in C)

def iadd(a,b): return (a[0]+b[0],a[1]+b[1])
def isub(a,b): return (a[0]-b[1],a[1]-b[0])
def smul(c,a): return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
def absup(a): return max(abs(a[0]),abs(a[1]))
def abslow(a):
    if a[0] <= 0 <= a[1]: return Q(0)
    return min(abs(a[0]),abs(a[1]))

def sincos_interval(x,n=45):
    s=Q(0); c=Q(0)
    for k in range(n+1):
        s += (-1 if k&1 else 1)*x**(2*k+1)/factorial(2*k+1)
        c += (-1 if k&1 else 1)*x**(2*k)/factorial(2*k)
    rs=abs(x)**(2*n+2)/factorial(2*n+2)
    rc=abs(x)**(2*n+1)/factorial(2*n+1)
    return (s-rs,s+rs),(c-rc,c+rc)

def atan_inv_interval(n, terms):
    x=Q(1,n); s=Q(0)
    for k in range(terms): s += (-1 if k&1 else 1)*x**(2*k+1)/(2*k+1)
    nxt=(-1 if terms&1 else 1)*x**(2*terms+1)/(2*terms+1)
    return (min(s,s+nxt),max(s,s+nxt))
a5=atan_inv_interval(5,40); a239=atan_inv_interval(239,12)
PI=(16*a5[0]-4*a239[1],16*a5[1]-4*a239[0])
assert PI[0] > Q(333,106) and PI[1] < Q(355,113)
TWO_PI=smul(Q(2),PI)

A=dict(FIXED); A.update(dict(zip(VAR_EDGES,X0)))
SC={e:sincos_interval(A[e]) for e in EDGES}
FV=[]
for i in range(5):
    fx=(Q(SIGNS[i]),Q(SIGNS[i])); fy=(Q(0),Q(0))
    for e in EDGES:
        u,v=e
        if i==u: sg=1
        elif i==v: sg=-1
        else: continue
        si,ci=SC[e]
        fx=iadd(fx,smul(Q(sg),ci)); fy=iadd(fy,smul(Q(sg),si))
    FV.extend((fx,fy))

J=[[(Q(0),Q(0)) for _ in range(10)] for __ in range(10)]
for col,e in enumerate(VAR_EDGES):
    si,ci=SC[e]; u,v=e
    for i in (u,v):
        if i>=5: continue
        sg=Q(1 if i==u else -1)
        J[2*i][col]=smul(-sg,si)
        J[2*i+1][col]=smul(sg,ci)

def matvec_interval(M,v):
    out=[]
    for row in M:
        z=(Q(0),Q(0))
        for c,a in zip(row,v): z=iadd(z,smul(c,a))
        out.append(z)
    return out
CF=matvec_interval(C,FV); Y=max(absup(z) for z in CF)
ZMAT=[]
for i in range(10):
    row=[]
    for j in range(10):
        z=(Q(1 if i==j else 0),Q(1 if i==j else 0))
        for k in range(10): z=isub(z,smul(C[i][k],J[k][j]))
        row.append(z)
    ZMAT.append(row)
Z0=max(sum(absup(a) for a in row) for row in ZMAT)
CN=max(sum(abs(c) for c in row) for row in C)
Z=Z0+4*CN*R
assert Z<1 and Y+Z*R<R

ROOT_ANGLE={e:((A[e]-R,A[e]+R) if e in VAR_EDGES else (A[e],A[e])) for e in EDGES}
def pi_mult(k): return smul(Q(k),PI)
def raw_face_angle_interval(i,e):
    u,v=e; a=ROOT_ANGLE[e]
    return a if i==u else iadd(a,PI)
def midpoint(a): return (a[0]+a[1])/2

FACE_ORDERS=[]; gap_min=[]; gap_max=[]; two_min=[]; two_max=[]
for i in range(6):
    vals=[(((Q(0),Q(0)) if SIGNS[i]>0 else PI),'a')]
    for e in EDGES:
        if i not in e: continue
        a=raw_face_angle_interval(i,e)
        candidates=[]
        for k in range(-2,3):
            b=iadd(a,pi_mult(2*k))
            if b[0]>=0 and b[1]<TWO_PI[0]: candidates.append(b)
        assert len(candidates)==1
        vals.append((candidates[0],e))
    vals.sort(key=lambda z:midpoint(z[0]))
    for j in range(4): assert vals[j][0][1] < vals[j+1][0][0]
    FACE_ORDERS.append(tuple(label for _a,label in vals))
    gaps=[]
    for j in range(4): gaps.append(isub(vals[j+1][0],vals[j][0]))
    gaps.append(isub(iadd(vals[0][0],TWO_PI),vals[-1][0]))
    assert all(g[0]>0 for g in gaps)
    tw=[iadd(gaps[j],gaps[(j+1)%5]) for j in range(5)]
    assert all(3*g[1] < 2*PI[0] for g in gaps)
    assert all(3*t[0] > 2*PI[1] for t in tw)
    assert all(t[1] < PI[0] for t in tw)
    gap_min.append(min(g[0] for g in gaps)); gap_max.append(max(g[1] for g in gaps))
    two_min.append(min(t[0] for t in tw)); two_max.append(max(t[1] for t in tw))

EXPECTED=(
 ('a',(0,2),(0,5),(0,4),(0,1)),
 ('a',(0,1),(1,3),(1,5),(1,2)),
 ('a',(2,3),(1,2),(0,2),(2,4)),
 ((3,5),(3,4),'a',(2,3),(1,3)),
 ((0,4),(2,4),'a',(4,5),(3,4)),
 ((1,5),(4,5),'a',(3,5),(0,5)),
)
assert tuple(FACE_ORDERS)==EXPECTED

def neighbor_rotation(i):
    return tuple(e[1] if e[0]==i else e[0] for e in FACE_ORDERS[i] if e!='a')
ROT={i:neighbor_rotation(i) for i in range(6)}
assert ROT=={
 0:(2,5,4,1), 1:(0,3,5,2), 2:(3,1,0,4),
 3:(5,4,2,1), 4:(0,2,5,3), 5:(1,4,3,0),
}

def absdot_interval(e,f):
    d=A[e]-A[f]
    _s,c=sincos_interval(d)
    rho=(R if e in VAR_EDGES else 0)+(R if f in VAR_EDGES else 0)
    c=(c[0]-rho,c[1]+rho)
    return (abslow(c),absup(c))

def cycle_edges(seq):
    return tuple(tuple(sorted((seq[i],seq[(i+1)%len(seq)]))) for i in range(len(seq)))
def cross_pairs(C,D): return tuple((e,f) for e in cycle_edges(C) for f in cycle_edges(D))

EQ_SPECS=(
 ((0,1,2),(2,3,4),frozenset({((0,2),(3,4))}),0),
 ((0,2,4),(3,4,5),frozenset({((0,2),(3,4)),((0,4),(3,4))}),0),
 ((0,4,5),(2,3,4),frozenset({((0,4),(3,4))}),1),
)
weak_forbidden=Q(1); weak_allowed=Q(1)
for CYC,DYC,allowed,rhs in EQ_SPECS:
    got=set()
    for e,f in cross_pairs(CYC,DYC):
        lo,hi=absdot_interval(e,f)
        pair=(e,f)
        if hi < Q(1,2):
            got.add(pair); weak_allowed=min(weak_allowed,Q(1,2)-hi)
        else:
            assert lo > Q(1,2), (CYC,DYC,e,f,float(lo),float(hi))
            weak_forbidden=min(weak_forbidden,lo-Q(1,2))
    assert got==set(allowed), (CYC,DYC,got,allowed)

def local_alternation(C,D,v):
    def neighbors(seq):
        k=seq.index(v); return {seq[k-1],seq[(k+1)%len(seq)]}
    a=neighbors(C); b=neighbors(D); assert not (a&b)
    bits=[0 if w in a else 1 if w in b else 2 for w in ROT[v]]
    bits=[x for x in bits if x<2]
    assert len(bits)==4
    return int(all(bits[k]!=bits[(k+1)%4] for k in range(4)))

def parity_rhs(C,D):
    common=set(C)&set(D)
    out=0
    for v in common: out ^= local_alternation(C,D,v)
    return out
for CYC,DYC,_allowed,rhs in EQ_SPECS:
    assert parity_rhs(CYC,DYC)==rhs

lhs=frozenset(); rr=0
for _C,_D,vars_,rhs in EQ_SPECS:
    lhs=lhs.symmetric_difference(vars_); rr ^= rhs
assert lhs==frozenset() and rr==1

print('PASS: exact collapsed support-six mod-2 cycle obstruction certificate')
print('radius',float(R))
print('Y',float(Y),'Z0',float(Z0),'C_norm_inf',float(CN),'Z',float(Z))
print('mapping_margin',float(R-(Y+Z*R)))
print('face_orders',FACE_ORDERS)
print('min_turn_gap',min(map(float,gap_min)),'max_turn_gap',max(map(float,gap_max)))
print('min_adjacent_two_turn',min(map(float,two_min)),'max_adjacent_two_turn',max(map(float,two_max)))
print('crossing_margin_allowed',float(weak_allowed),'crossing_margin_forbidden',float(weak_forbidden))
print('parity_equations: x_02_34=0; x_02_34 xor x_04_34=0; x_04_34=1')
print('PASS: XOR of the three plane-intersection equations is 0=1')
