#!/usr/bin/env python3
"""Exact certificate for a local collapsed support-six closure realization.

This script proves, using only Fraction arithmetic for every logical test, that the
K6-minus-perfect-matching six-face closure system with three +x and three -x
anchors has a strict solution near the recorded rational center.  It uses a
Banach contraction bound for ten solved train angles after two train angles are
fixed, then certifies the six convex pentagon turn-gap conditions and records the
discrete topology of the natural internal-side pairing.

What it does NOT prove: global stopped-train/rhombus integrability, a source-point
embedding, compatibility with diameter bars, or global minimum-diameter optimality.
"""
from fractions import Fraction as Q
from math import factorial

EDGES=((0,1),(0,2),(0,4),(0,5),(1,2),(1,3),(1,5),(2,3),(2,4),(3,4),(3,5),(4,5))
FIXED={(0,1):Q('-0.69671336'),(0,2):Q('1.75049398')}
VAR_EDGES=tuple(e for e in EDGES if e not in FIXED)
X0=tuple(Q(s) for s in (
'2.731156095605589','-2.3067260211240153','-0.9986998192961997','-2.2337034767798927',
'1.730504059203213','1.682595595587784','-2.1244160181617695','2.044414508054986',
'-0.7537438854643705','2.6878789475216607'))
SIGNS=(1,1,1,-1,-1,-1)
R=Q(1,10**10)

C_STR='''
-0.70847640713042048262776766555645295,-0.78228216536756258738286763061632807,0,0,0,0,0,0,0,0
0.96776079158546005241704648198656015,-0.42112142664850907474503065366449648,0,0,0,0,0,0,0,0
0.015775497438969041051505412552354763,0.017418914973177584105508433859326571,-0.19815962710880811240145406789473162,1.230196948909585277668344734963005,-0.59878120722553610168515010568753564,0.0052702990719238528815161540245911592,-0.66864891609850884972622681849350808,0.62760327878315822986663176446855813,-0.46260468430820760350046567371963678,0.22558620834709404666927693991280199
0.0086267815686398745132399175441568184,0.0095254793211854430649684618427279142,0.10861581061090835997565223358389139,-0.67429900210455897048215069312194046,-0.32744163549360424977309057855223819,0.0028820466087225837825830445988193287,-0.36564857416417638405441442861325536,0.34320289542504152724503971749917358,-0.2529739286888261108111888820221264,0.12336111440142617640443801837688645
0.020321834719834714072654202292092868,0.022438868406732317156292178696915898,-1.0949288233735164048460130231537281,0.50930463352823228759451469264302062,-0.77134383709016456510163024978846827,0.0067891454502834463183099111389987462,-0.86134670625248688963020961376609101,0.80847213537319631168410528880035456,-0.59592263074444657146226811625034123,0.29059785016854833562132637052102388
-0.023062596649248495255783842754976309,-0.025465150094195908802335699914572719,0.28969454496482695015034531150427676,-1.7984558738384897427883539345639807,0.023771043963479979986903407064347311,-1.3854865348343828953361215217706807,0.97751467499492592459887645777750212,-0.91750902501289039331317189440469319,0.67629342805372464949036815199562409,-0.32979015418498043905293484335419737
-0.011350552484574350631234055813599431,-0.012532999950859945364928907704405671,0.14257688269570025542575347210594226,-0.88513310524641145987592257099331779,0.61153326643076561989208376347467047,-1.6134049845033157472595794664274709,0.48109637399972008438007534010559325,-0.45156382439783966953569494027739123,0.33284647721342535250680681938768428,-0.16231045059249496846534592026991718
-0.069912121431616626800284972820618587,-0.077195239232429646946443384764724797,0.23645477722055750300517672316442535,-1.4679374892651672175350029102051226,1.0141893941212341864734128210287956,-2.6757305179093631093502370935466306,0.79786802590229765406473554185548762,-0.74889015301829266513076255932461821,2.0501207641350721806109640506816327,-0.99972824643244251765942964029617701
-0.047486013918445805736919696772395152,-0.052432884735366605305541446315543457,0.011912289738144768425192092667529006,-0.073952816243169403653466742115475898,0.90716137161008810953045982118968428,-1.4642414526086228590851344502535564,0.65815418833844812121263303087422829,0.75374143010884851940121250983213126,1.3924919047898736988160834847782368,-0.67903974951166962421857562612711115
-0.76487639178067293995088626950006923,-0.84455763661098931081116205813465871,0.20338962394596834625869333104204897,-1.262665349490236731072624737064017,0.87236807775678804112317076611924817,-2.3015640885559662669162331231584836,0.68629646503361874156765823647634669,-0.64416751646828965479286184708377925,1.2350332580381294304210400547418314,-1.7148189782799875557408790345363269
'''.strip()
C=tuple(tuple(Q(x) for x in line.split(',')) for line in C_STR.splitlines())
assert len(C)==10 and all(len(row)==10 for row in C)

def iadd(a,b): return (a[0]+b[0],a[1]+b[1])
def isub(a,b): return (a[0]-b[1],a[1]-b[0])
def smul(c,a): return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
def absup(a): return max(abs(a[0]),abs(a[1]))

def sincos_interval(x,n=45):
    # Taylor polynomials at 0 with Lagrange remainders (all derivatives bounded by 1).
    s=Q(0); c=Q(0)
    for k in range(n+1):
        s += (-1 if k&1 else 1)*x**(2*k+1)/factorial(2*k+1)
        c += (-1 if k&1 else 1)*x**(2*k)/factorial(2*k)
    rs=abs(x)**(2*n+2)/factorial(2*n+2)
    rc=abs(x)**(2*n+1)/factorial(2*n+1)
    return (s-rs,s+rs),(c-rc,c+rc)

def atan_inv_interval(n, terms):
    x=Q(1,n); s=Q(0)
    for k in range(terms):
        s += (-1 if k&1 else 1)*x**(2*k+1)/(2*k+1)
    nxt=(-1 if terms&1 else 1)*x**(2*terms+1)/(2*terms+1)
    return (min(s,s+nxt),max(s,s+nxt))
a5=atan_inv_interval(5,40); a239=atan_inv_interval(239,12)
PI=(16*a5[0]-4*a239[1],16*a5[1]-4*a239[0])
assert PI[0] < PI[1]
assert PI[0] > Q(333,106) and PI[1] < Q(355,113)

A=dict(FIXED); A.update(dict(zip(VAR_EDGES,X0)))
SC={e:sincos_interval(A[e]) for e in EDGES}
# F(x0), using faces 0..4. Face 5 follows from global cancellation.
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

# J(x0) interval.
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
CF=matvec_interval(C,FV)
Y=max(absup(z) for z in CF)

# I-CJ interval.
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
# Each scalar closure row has at most 4 variable-edge entries; each J entry is 1-Lipschitz in its angle.
Z=Z0+4*CN*R
assert Z < 1
assert Y+Z*R < R

# Certify all six local pentagons are strict, convex, and chord-free throughout the root ball.
# Build angle intervals modulo 2*pi for each face. Edge angle is A[e] at lower endpoint, A[e]+pi at upper.
# Root variables range X0 +/- R. Fixed parameters are exact.
ROOT_ANGLE={e:((A[e]-R,A[e]+R) if e in VAR_EDGES else (A[e],A[e])) for e in EDGES}

def add_interval(a,b): return iadd(a,b)
def pi_mult(k): return smul(Q(k),PI)

def raw_face_angle_interval(i,e):
    u,v=e; a=ROOT_ANGLE[e]
    if i==u: return a
    if i==v: return add_interval(a,PI)
    raise ValueError

def midpoint(a): return (a[0]+a[1])/2
# Normalize each side angle into [0,2*pi) using exact interval containment.
TWO_PI=smul(Q(2),PI)
face_gap_upper=[]; face_two_gap_upper=[]; face_min_gap=[]; FACE_ORDERS=[]
for i in range(6):
    vals=[]
    # anchor: +x angle 0 for + signs; -x angle pi for - signs.
    vals.append(((Q(0),Q(0)) if SIGNS[i]>0 else PI, 'anchor'))
    for e in EDGES:
        if i not in e: continue
        a=raw_face_angle_interval(i,e)
        # Normalize with an integer multiple of 2*pi. Candidate selection is
        # followed by exact interval containment, so no floating-point branch
        # enters the proof.
        candidates=[]
        for k in range(-2,3):
            b=add_interval(a,pi_mult(2*k))
            if b[0] >= 0 and b[1] < TWO_PI[0]:
                candidates.append(b)
        assert len(candidates)==1
        a=candidates[0]
        vals.append((a,str(e)))
    vals.sort(key=lambda z: midpoint(z[0]))
    FACE_ORDERS.append(tuple(label for _a,label in vals))
    # rigorous order separation
    for j in range(4): assert vals[j][0][1] < vals[j+1][0][0]
    gaps=[]
    for j in range(4): gaps.append(isub(vals[j+1][0],vals[j][0]))
    gaps.append(isub(add_interval(vals[0][0],TWO_PI),vals[-1][0]))
    assert all(g[0]>0 for g in gaps)
    gmax=max(g[1] for g in gaps); gmin=min(g[0] for g in gaps)
    g2max=max((iadd(gaps[j],gaps[(j+1)%5]))[1] for j in range(5))
    assert 3*gmax < 2*PI[0]  # every exterior turn < 2pi/3
    assert g2max < PI[0]     # every two consecutive turns sum < pi
    face_gap_upper.append(gmax); face_two_gap_upper.append(g2max); face_min_gap.append(gmin)

# The verified cyclic orders also define an orientable side-pairing surface:
# pair each internal train side with its opposite occurrence and leave the six
# anchor sides unpaired. Record the topology as an exact discrete regression.
parent={(i,k):(i,k) for i in range(6) for k in range(5)}
def find(x):
    while parent[x] != x:
        parent[x]=parent[parent[x]]; x=parent[x]
    return x
def union(a,b):
    a,b=find(a),find(b)
    if a!=b: parent[b]=a
occ={}
for i,order in enumerate(FACE_ORDERS):
    for k,label in enumerate(order):
        if label != 'anchor': occ.setdefault(label,[]).append((i,k))
assert all(len(v)==2 for v in occ.values()) and len(occ)==12
for label,pair in occ.items():
    (i,k),(j,m)=pair
    union((i,k),(j,(m+1)%5)); union((i,(k+1)%5),(j,m))
Vclasses={find(x) for x in parent}
bedges=[]
for i,order in enumerate(FACE_ORDERS):
    k=order.index('anchor')
    bedges.append((find((i,k)),find((i,(k+1)%5)),i))
adj={}
for a,b,i in bedges:
    adj.setdefault(a,[]).append((b,i));adj.setdefault(b,[]).append((a,i))
assert all(len(v)==2 for v in adj.values())
seen=set(); bcomps=[]
for a in adj:
    if a in seen: continue
    stack=[a];seen.add(a); faces=set()
    while stack:
        x=stack.pop()
        for y,i in adj[x]:
            faces.add(i)
            if y not in seen: seen.add(y);stack.append(y)
    bcomps.append(frozenset(faces))
assert set(bcomps)=={frozenset((0,2,5)),frozenset((1,3,4))}
Vn=len(Vclasses); En=18; Fn=6; bn=len(bcomps); chi=Vn-En+Fn
assert Vn==8 and bn==2 and chi==-4
g=(2-bn-chi)//2
assert 2-2*g-bn==chi and g==2

print('PASS: exact collapsed support-six local closure realization certificate')
print('radius', float(R))
print('Y', float(Y))
print('Z0', float(Z0))
print('C_norm_inf', float(CN))
print('Z', float(Z))
print('mapping_margin', float(R-(Y+Z*R)))
print('pi_interval_width', float(PI[1]-PI[0]))
print('min_face_turn_gap', min(float(x) for x in face_min_gap))
print('max_face_turn_gap', max(float(x) for x in face_gap_upper), 'vs 2pi/3 lower', float(2*PI[0]/3))
print('max_face_two_turn_sum', max(float(x) for x in face_two_gap_upper), 'vs pi lower', float(PI[0]))
print('face_orders', FACE_ORDERS)
print('translation_surface_topology', {'V':Vn,'E':En,'F':Fn,'b':bn,'g':g,'boundary_face_sets':sorted(map(sorted,bcomps))})
