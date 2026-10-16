import math, random
h=math.sqrt(303.0)/52.0
k=1.0/(2.0*h)

def root_eq(y):
    return math.sqrt(2.0)*h*y**3-(1.0-y*y)**2
lo,hi=0.0,1.0
for _ in range(200):
    mid=(lo+hi)/2.0
    if root_eq(mid)<0: lo=mid
    else: hi=mid
y=(lo+hi)/2.0
a_star=(1-y*y)/2.0
A=math.sqrt(2.0*(1.0-2.0*a_star))/4.0
C=a_star/h
K=A*C/(A+C)
c_univ=2.0*math.sqrt(K)
r=math.sqrt(K/k)
bE=1.0/math.sqrt(K)
t1=2.0*(1.0-r)/math.sqrt(k*r*(2.0-r))
t2=2.0*(1.0-r)/math.sqrt(K)

def b0(t):
    return t/(2.0*(1.0-r))
def bH(t):
    return math.sqrt(t*t/4.0+1.0/k)
def Q(t,b):
    return (1.0+max(K*b*b,k*max(0.0,b-t/2.0)**2))/b
def bstar(t):
    if t<=t1: return bH(t)
    if t<=t2: return b0(t)
    return bE
def L(z,t):
    if z<=0: return math.inf
    return Q(t,min(z,bstar(t)))
def g(t):
    return k*(math.sqrt(t*t+4.0/k)-t)
def Cjoint(t): return Q(t,bstar(t))

assert abs(h-0.33474798433710024)<3e-15
assert abs(k-1.4936609730157075)<3e-15
assert abs(K-0.18864061345631405)<3e-15
assert abs(c_univ-0.8686555438292305)<3e-15
assert abs(r-0.35537885451617746)<3e-15
assert abs(bE-2.3024086062739517)<3e-15
assert abs(t1-1.3798433975544506)<3e-15
assert abs(t2-2.968362546296252)<3e-15

assert abs(b0(t1)-bH(t1))<3e-15
assert abs(b0(t2)-bE)<3e-15

for t in (0.1,0.5,1.0,1.5,2.0,2.5,3.0,5.0):
    b00=b0(t)
    for f in (0.25,0.75,1.0,1.25,2.0):
        b=max(1e-9,b00*f)
        q=Q(t,b)
        if b<=b00+1e-14:
            q2=1.0/b+K*b
        else:
            q2=(1.0+k*(b-t/2.0)**2)/b
        assert abs(q-q2)<3e-14*max(1.0,q)

rng=random.Random(20260918)
for _ in range(400000):
    z=0.02+4.98*rng.random()
    t=5.0*rng.random()
    m=z*rng.random()
    Mmax=min(t/2.0,z-m)
    M=Mmax*rng.random()
    cap=m+M
    if cap<=0: continue
    b=cap*(1e-8+(1-1e-8)*rng.random())
    val=(1.0+max(K*b*b,k*m*m))/b
    assert val+3e-12*max(1.0,val)>=L(z,t)

for t in [0.0,0.2,0.5,1.0,t1,1.5,2.0,2.5,t2,3.0,5.0]:
    bs=bstar(t)
    qstar=Q(t,bs)
    prev=float('inf')
    for j in range(1,10001):
        b=bs*j/10000.0
        q=Q(t,b)
        assert q<=prev+2e-10*max(1.0,q)
        prev=q
    for j in range(1,10001):
        b=bs*(1.0+2.0*j/10000.0)
        assert Q(t,b)+2e-12*max(1.0,Q(t,b))>=qstar

for t in [0.0,0.3,1.0,t1]:
    assert abs(Cjoint(t)-g(t))<3e-14
for t in [1.5,2.0,2.5,t2]:
    hyb=2.0*(1.0-r)/t+K*t/(2.0*(1.0-r))
    assert abs(Cjoint(t)-hyb)<3e-14
for t in [t2,3.0,5.0,10.0]:
    assert abs(Cjoint(t)-c_univ)<3e-14

assert abs(Cjoint(2.0)-0.9372591000062873)<3e-15
assert Cjoint(2.0)>max(g(2.0),c_univ)+0.06

z0=1.0/math.sqrt(k)
assert abs(z0-0.8182273331258255)<3e-15
for z in [0.1,0.3,0.5,0.8]:
    assert abs(L(z,0.0)-(1.0/z+k*z))<3e-15
for z in [z0,1.0,2.0,5.0]:
    assert abs(L(z,0.0)-2.0*math.sqrt(k))<3e-15

L05=L(0.5,0.0)
assert abs(L05-2.7468304865078537)<3e-15
assert abs(L05/4.0-0.6867076216269634)<3e-15
assert abs(2.0*h/L05-0.2437339952220187)<3e-15

print('PASS: sharp joint terminal/external FREE face minimax')
print(f'h_*={h:.15f}')
print(f'k_inf={k:.15f}')
print(f'K_inf={K:.15f}')
print(f'c_univ={c_univ:.15f}')
print(f'r={r:.15f}')
print(f't1={t1:.15f}')
print(f't2={t2:.15f}')
print(f'C_joint(2)={Cjoint(2.0):.15f}')
print(f'L(0.5,0)={L05:.15f}')
