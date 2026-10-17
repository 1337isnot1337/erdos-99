import math
import random

h = math.sqrt(303.0) / 52.0

# Sharp optimizer.  With y=sqrt(1-2a), stationarity is
# sqrt(2)*h*y^3=(1-y^2)^2.  The left side is increasing and the right side decreasing.
def root_eq(y):
    return math.sqrt(2.0) * h * y**3 - (1.0 - y*y)**2

lo, hi = 0.0, 1.0
for _ in range(200):
    mid = (lo + hi) / 2.0
    if root_eq(mid) < 0.0:
        lo = mid
    else:
        hi = mid
y = (lo + hi) / 2.0
a = (1.0 - y*y) / 2.0
A_inf = math.sqrt(2.0 * (1.0 - 2.0*a)) / 4.0
C_inf = a / h
K_inf = A_inf * C_inf / (A_inf + C_inf)
c = 2.0 * math.sqrt(K_inf)

assert 0.0 < a < 0.5
assert abs(root_eq(y)) < 2e-15
assert abs(y - 0.7460656369283891) < 3e-15
assert abs(a - 0.22169303269731855) < 3e-15
assert abs(A_inf - 0.2637740355411623) < 3e-15
assert abs(C_inf - 0.6622684618589598) < 3e-15
assert abs(K_inf - 0.18864061345631405) < 3e-15
assert abs(c - 0.8686555438292305) < 3e-15
assert abs(c / 4.0 - 0.21716388595730762) < 3e-15
assert abs(2.0*h/c - 0.7707266400705975) < 3e-15

# Global optimizer regression.
def asymptotic_K(aa):
    A = math.sqrt(2.0*(1.0-2.0*aa))/4.0
    C = aa/h
    return A*C/(A+C)

for j in range(1, 200000):
    aa = 0.5*j/200000.0
    assert asymptotic_K(aa) <= K_inf + 2e-12

# Finite-D coefficients.
for D in (1e4, 1e6, 1e9, 1e12):
    L0 = D - a/D
    numer = 2.0*(1.0 - 2.0*a + a*a/(D*D))
    delta = math.sqrt(numer) / L0
    A_sharp = L0*delta/4.0
    A_flat = L0*delta/(2.0*math.pi)
    C = (a - a*a/(2.0*D*D))/(h + D**(-1.0/3.0))
    K = A_sharp*C/(A_sharp+C)
    assert delta > 0.0 and A_flat > 0.0 and A_sharp > A_flat and C > 0.0 and K > 0.0
    if D >= 1e9:
        assert abs(D*delta - math.sqrt(2.0*(1.0-2.0*a))) < 3e-6
        assert abs(A_sharp-A_inf) < 2e-12
        assert abs(C-C_inf) < 3e-3
        assert abs(K-K_inf) < 3e-4

# Lemma UF.1 random regression.
rng = random.Random(20260918)
D = 100.0
for _ in range(250000):
    L1 = D - rng.random()*a/D
    L2 = D - rng.random()*a/D
    theta = rng.random() * (math.pi/2.0)
    v = (math.cos(theta), math.sin(theta))
    aa = L1/2.0
    cc = L2/2.0
    mx = (rng.random()-0.5) * 2.0
    my = (rng.random()-0.5) * 2.0
    pts1 = [(-aa, 0.0), (aa, 0.0)]
    pts2 = [(mx-cc*v[0], my-cc*v[1]), (mx+cc*v[0], my+cc*v[1])]
    ds = [math.hypot(x1-x2, y1-y2)
          for x1,y1 in pts1 for x2,y2 in pts2]
    if min(ds) >= 1.0 and max(ds) <= D:
        assert math.cos(theta) <= (D*D-1.0)/(L1*L2) + 2e-12

# Exact layer-cake inequality on random delta-separated projective sets.  Build sets
# greedily, then compare sum sin(phi) to cos(L)*delta*(p-1)^2/4.
def pdist(x, z):
    d = abs(x-z) % math.pi
    return min(d, math.pi-d)

for p in range(1, 50):
    delta = 0.01
    for _ in range(100):
        tangent = rng.random()*math.pi
        pts = []
        attempts = 0
        while len(pts) < p and attempts < 200000:
            x = rng.random()*math.pi
            if all(pdist(x,z) >= delta for z in pts):
                pts.append(x)
            attempts += 1
        assert len(pts) == p
        phis = [pdist(x,tangent) for x in pts]
        L = delta*(p-1)/2.0
        rhs = math.cos(L)*delta*(p-1)**2/4.0
        assert sum(math.sin(phi) for phi in phis) + 1e-12 >= rhs

# Extremal near-tangent configurations approach coefficient 1 in sin(phi)/phi.
for p in (10, 100, 1000):
    delta = 1e-7
    tangent = 0.0
    pts = [0.0]
    k = 1
    while len(pts) < p:
        pts.append((k*delta) % math.pi)
        if len(pts) < p:
            pts.append((-k*delta) % math.pi)
        k += 1
    phis = [pdist(x,tangent) for x in pts]
    linear = sum(phis)
    sine = sum(math.sin(phi) for phi in phis)
    assert sine/linear > 1.0 - 1e-8

# Weighted Cauchy and exact run-span minimization.
for _ in range(100000):
    t = rng.random()*1e5
    p = rng.random()*1e5
    lhs = C_inf*t*t + A_inf*p*p
    rhs = K_inf*(t+p)*(t+p)
    assert lhs + 1e-8*max(1.0,lhs) >= rhs

for D in (1e4, 1e6, 1e10):
    x = -1.0 + math.sqrt(1.0 + D/K_inf)
    f = (D + K_inf*x*x)/(x+1.0)
    exact = 2.0*K_inf*(math.sqrt(1.0 + D/K_inf)-1.0)
    assert abs(f-exact) < 1e-10*max(1.0, exact)
    assert f/math.sqrt(D) < c + 1e-8
    assert f/math.sqrt(D) > c - 0.01

# At the D^(5/8) cutoff the local angular radius tends to zero, while the robust
# large-block branch is already super-square-root.
for D in (1e8, 1e12, 1e16):
    delta = math.sqrt(2.0*(1.0-2.0*a+a*a/(D*D))) / (D-a/D)
    Bcut = D**(5.0/8.0)
    L = delta*Bcut/2.0
    assert L < 0.02
    assert Bcut/math.sqrt(D) == D**(1.0/8.0)

print('PASS: sharp universal FREE square-root face-run arithmetic')
print(f'h_*={h:.15f}')
print(f'a_*={a:.15f}')
print(f'A_inf={A_inf:.15f}')
print(f'C_inf={C_inf:.15f}')
print(f'K_inf={K_inf:.15f}')
print(f'c_univ={c:.15f}')
print(f'Lambda=2 matching coefficient={c/4.0:.15f}')
print(f'Lambda=2 slack coefficient={2.0*h/c:.15f}')
