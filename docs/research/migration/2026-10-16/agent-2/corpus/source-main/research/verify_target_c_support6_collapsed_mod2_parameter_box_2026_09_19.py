#!/usr/bin/env python3
"""Exact interval-Newton extension of the collapsed mod-2 obstruction."""
from fractions import Fraction as Q
from math import factorial
import runpy

BASE = runpy.run_path("research/verify_target_c_support6_collapsed_mod2_cycle_obstruction_2026_09_19.py")
EDGES = BASE["EDGES"]
VAR_EDGES = BASE["VAR_EDGES"]
X0 = BASE["X0"]
C = BASE["C"]
PI = BASE["PI"]
TWO_PI = BASE["TWO_PI"]
SIGNS = BASE["SIGNS"]
FIXED = BASE["FIXED"]

P_RADIUS = Q(1, 10000)
X_RADIUS = Q(1, 1000)

def add(a, b): return (a[0] + b[0], a[1] + b[1])
def sub(a, b): return (a[0] - b[1], a[1] - b[0])
def scale(c, a): return (c*a[0], c*a[1]) if c >= 0 else (c*a[1], c*a[0])
def absup(a): return max(abs(a[0]), abs(a[1]))
def mul(a, b):
    q = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return min(q), max(q)
def power(a, n):
    z = (Q(1), Q(1))
    for _ in range(n): z = mul(z, a)
    return z

def sincos_interval(x, n=45):
    ss = (Q(0), Q(0)); cc = (Q(0), Q(0))
    for k in range(n + 1):
        ss = add(ss, scale(Q(-1 if k & 1 else 1) / factorial(2*k + 1), power(x, 2*k + 1)))
        cc = add(cc, scale(Q(-1 if k & 1 else 1) / factorial(2*k), power(x, 2*k)))
    m = max(abs(x[0]), abs(x[1]))
    rs = m**(2*n+2) / factorial(2*n+2)
    rc = m**(2*n+1) / factorial(2*n+1)
    return (ss[0]-rs, ss[1]+rs), (cc[0]-rc, cc[1]+rc)

center = dict(FIXED)
center.update(dict(zip(VAR_EDGES, X0)))
P = {e: (center[e]-P_RADIUS, center[e]+P_RADIUS) for e in EDGES if e in FIXED}
AX = dict(P)
AX.update({e: (center[e]-X_RADIUS, center[e]+X_RADIUS) for e in VAR_EDGES})
def edge_radius(e): return P_RADIUS if e in FIXED else X_RADIUS
def sincos_lipschitz(c, r):
    (si, ci) = BASE["sincos_interval"](c)
    return (si[0]-r, si[1]+r), (ci[0]-r, ci[1]+r)
SC_F = {e: sincos_lipschitz(center[e], P_RADIUS if e in FIXED else Q(0)) for e in EDGES}
SC_J = {e: sincos_lipschitz(center[e], edge_radius(e)) for e in EDGES}

FV = []
for i in range(5):
    fx = (Q(SIGNS[i]), Q(SIGNS[i])); fy = (Q(0), Q(0))
    for e in EDGES:
        u, v = e
        if i == u: sg = 1
        elif i == v: sg = -1
        else: continue
        si, ci = SC_F[e]
        fx = add(fx, scale(Q(sg), ci)); fy = add(fy, scale(Q(sg), si))
    FV.extend((fx, fy))

J = [[(Q(0), Q(0)) for _ in range(10)] for __ in range(10)]
for col, e in enumerate(VAR_EDGES):
    si, ci = SC_J[e]; u, v = e
    for i in (u, v):
        if i >= 5: continue
        sg = Q(1 if i == u else -1)
        J[2*i][col] = scale(-sg, si)
        J[2*i+1][col] = scale(sg, ci)

def matvec(M, v):
    out = []
    for row in M:
        z = (Q(0), Q(0))
        for c, a in zip(row, v): z = add(z, scale(c, a))
        out.append(z)
    return out

CF = matvec(C, FV)
Y = max(absup(z) for z in CF)
ZMAT = []
for i in range(10):
    row = []
    for j in range(10):
        z = (Q(1 if i == j else 0), Q(1 if i == j else 0))
        for k in range(10): z = sub(z, scale(C[i][k], J[k][j]))
        row.append(z)
    ZMAT.append(row)
Z0 = max(sum(absup(a) for a in row) for row in ZMAT)
CN = max(sum(abs(c) for c in row) for row in C)
Z = Z0 + 4*CN*X_RADIUS
assert Z < 1
assert Y + Z*X_RADIUS < X_RADIUS, (float(Y), float(Z), float(Y + Z*X_RADIUS))

def pi_mult(k): return scale(Q(k), PI)
def raw_face(i, e): return AX[e] if i == e[0] else add(AX[e], PI)
def mid(a): return (a[0] + a[1]) / 2

FACE_ORDERS = []
gap_min = []; gap_max = []; two_min = []; two_max = []
for i in range(6):
    vals = [(((Q(0), Q(0)) if SIGNS[i] > 0 else PI), 'a')]
    for e in EDGES:
        if i not in e: continue
        a = raw_face(i, e); candidates = []
        for k in range(-2, 3):
            b = add(a, pi_mult(2*k))
            if b[0] >= 0 and b[1] < TWO_PI[0]: candidates.append(b)
        assert len(candidates) == 1
        vals.append((candidates[0], e))
    vals.sort(key=lambda z: mid(z[0]))
    for j in range(4): assert vals[j][0][1] < vals[j+1][0][0]
    FACE_ORDERS.append(tuple(label for _a, label in vals))
    gaps = [sub(vals[j+1][0], vals[j][0]) for j in range(4)]
    gaps.append(sub(add(vals[0][0], TWO_PI), vals[-1][0]))
    assert all(g[0] > 0 for g in gaps)
    tw = [add(gaps[j], gaps[(j+1) % 5]) for j in range(5)]
    assert all(3*g[1] < 2*PI[0] for g in gaps)
    assert all(3*t[0] > 2*PI[1] for t in tw)
    assert all(t[1] < PI[0] for t in tw)
    gap_min.append(min(g[0] for g in gaps)); gap_max.append(max(g[1] for g in gaps))
    two_min.append(min(t[0] for t in tw)); two_max.append(max(t[1] for t in tw))

EXPECTED = (
 ('a',(0,2),(0,5),(0,4),(0,1)),
 ('a',(0,1),(1,3),(1,5),(1,2)),
 ('a',(2,3),(1,2),(0,2),(2,4)),
 ((3,5),(3,4),'a',(2,3),(1,3)),
 ((0,4),(2,4),'a',(4,5),(3,4)),
 ((1,5),(4,5),'a',(3,5),(0,5)),
)
assert tuple(FACE_ORDERS) == EXPECTED

def absdot(e, f):
    d = center[e] - center[f]
    _s, c = sincos_lipschitz(d, edge_radius(e) + edge_radius(f))
    lo = Q(0) if c[0] <= 0 <= c[1] else min(abs(c[0]), abs(c[1]))
    return lo, max(abs(c[0]), abs(c[1]))

def edge_seq(seq):
    return tuple(tuple(sorted((seq[i], seq[(i+1) % len(seq)]))) for i in range(len(seq)))

EQ_SPECS = (
 ((0,1,2),(2,3,4),frozenset({((0,2),(3,4))}),0),
 ((0,2,4),(3,4,5),frozenset({((0,2),(3,4)),((0,4),(3,4))}),0),
 ((0,4,5),(2,3,4),frozenset({((0,4),(3,4))}),1),
)
for ca, cb, allowed, rhs in EQ_SPECS:
    got = set()
    for e in edge_seq(ca):
        for f in edge_seq(cb):
            lo, hi = absdot(e, f)
            if hi < Q(1, 2): got.add((e, f))
            else: assert lo > Q(1, 2), (e, f, float(lo), float(hi))
    assert got == set(allowed), (ca, cb, got, allowed)

print('PASS: exact two-parameter collapsed mod-2 obstruction box')
print('parameter_radius', float(P_RADIUS), 'solved_radius', float(X_RADIUS))
print('Y', float(Y), 'Z0', float(Z0), 'C_norm_inf', float(CN), 'Z', float(Z))
print('mapping_margin', float(X_RADIUS - Y - Z*X_RADIUS))
print('min_turn_gap', float(min(gap_min)), 'max_turn_gap', float(max(gap_max)))
print('min_adjacent_two_turn', float(min(two_min)), 'max_adjacent_two_turn', float(max(two_max)))
print('face_orders', FACE_ORDERS)
print('parity_equations: x_02_34=0; x_02_34 xor x_04_34=0; x_04_34=1')
print('PASS: every closure point in the parameter box is globally excluded by XOR 0=1')
