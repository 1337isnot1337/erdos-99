#!/usr/bin/env python3
"""Exact interval certificate for the collapsed support-six Jordan obstruction.

Rechecks, throughout the rigorous radius-1e-10 local root box:
  * the counterclockwise side orders at F0,F1,F2;
  * fifteen strict no-crossing inequalities |u.v|>11/20.

The topological Jordan-separation argument using those certified facts is in
`target_c_support6_collapsed_global_train_obstruction_2026-09-19.md`.
All logical comparisons here use Fraction arithmetic. No floating point is used.
"""
from fractions import Fraction as Q
from math import factorial

R = Q(1, 10**10)
CENTERS = {
    (0, 1): Q('-0.69671336'),
    (0, 2): Q('1.75049398'),
    (0, 4): Q('2.731156095605589'),
    (0, 5): Q('-2.3067260211240153'),
    (1, 2): Q('-0.9986998192961997'),
    (1, 3): Q('-2.2337034767798927'),
    (1, 5): Q('1.730504059203213'),
    (2, 3): Q('1.682595595587784'),
    (2, 4): Q('-2.1244160181617695'),
    (3, 4): Q('2.044414508054986'),
    (3, 5): Q('-0.7537438854643705'),
    (4, 5): Q('2.6878789475216607'),
}
FIXED = {(0, 1), (0, 2)}


def iadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def imul(a, b):
    vals = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return (min(vals), max(vals))


def smul(c, a):
    return (c*a[0], c*a[1]) if c >= 0 else (c*a[1], c*a[0])


def midpoint(a):
    return (a[0] + a[1]) / 2


def sincos_interval(x, n=45):
    s = Q(0)
    c = Q(0)
    for k in range(n + 1):
        s += (-1 if k & 1 else 1) * x**(2*k + 1) / factorial(2*k + 1)
        c += (-1 if k & 1 else 1) * x**(2*k) / factorial(2*k)
    rs = abs(x)**(2*n + 2) / factorial(2*n + 2)
    rc = abs(x)**(2*n + 1) / factorial(2*n + 1)
    return (s-rs, s+rs), (c-rc, c+rc)


def atan_inv_interval(n, terms):
    x = Q(1, n)
    s = Q(0)
    for k in range(terms):
        s += (-1 if k & 1 else 1) * x**(2*k + 1) / (2*k + 1)
    nxt = (-1 if terms & 1 else 1) * x**(2*terms + 1) / (2*terms + 1)
    return (min(s, s+nxt), max(s, s+nxt))


# Machin enclosure for pi, copied from the audited local-root certificate.
a5 = atan_inv_interval(5, 40)
a239 = atan_inv_interval(239, 12)
PI = (16*a5[0] - 4*a239[1], 16*a5[1] - 4*a239[0])
TWO_PI = smul(Q(2), PI)
assert PI[0] > Q(333, 106) and PI[1] < Q(355, 113)

# ---------------------------------------------------------------------------
# 1. Recheck the side orders throughout the root box.
# ---------------------------------------------------------------------------
ANGLE = {
    e: ((x, x) if e in FIXED else (x-R, x+R))
    for e, x in CENTERS.items()
}


def normalize_2pi(a):
    candidates = []
    for k in range(-2, 3):
        b = iadd(a, smul(Q(2*k), PI))
        if b[0] >= 0 and b[1] < TWO_PI[0]:
            candidates.append(b)
    assert len(candidates) == 1
    return candidates[0]


expected_orders = {
    0: ('a', '02', '04', '05', '01'),
    1: ('a', '15', '01', '13', '12'),
    2: ('a', '23', '12', '24', '02'),
}

for face in range(3):
    vals = [((Q(0), Q(0)), 'a')]
    for e, a in ANGLE.items():
        if face not in e:
            continue
        lo, hi = e
        occurrence = a if face == lo else iadd(a, PI)
        occurrence = normalize_2pi(occurrence)
        vals.append((occurrence, ''.join(map(str, e))))

    vals.sort(key=lambda z: midpoint(z[0]))
    for j in range(4):
        assert vals[j][0][1] < vals[j+1][0][0]
    got = tuple(label for _interval, label in vals)
    assert got == expected_orders[face], (face, got)

print('PASS: certified side orders at F0,F1,F2 are unchanged throughout the root box')

# ---------------------------------------------------------------------------
# 2. Recheck the no-crossing projective-angle inequalities.
# ---------------------------------------------------------------------------
SC = {}
for e, center in CENTERS.items():
    si, co = sincos_interval(center)
    if e not in FIXED:
        # sin and cos are 1-Lipschitz in the angle.
        si = (si[0]-R, si[1]+R)
        co = (co[0]-R, co[1]+R)
    SC[''.join(map(str, e))] = (si, co)


def dot_interval(label1, label2):
    s1, c1 = SC[label1]
    s2, c2 = SC[label2]
    return iadd(imul(c1, c2), imul(s1, s2))


def abs_lower(a):
    if a[0] <= 0 <= a[1]:
        return Q(0)
    return min(abs(a[0]), abs(a[1]))


cycle = ('01', '12', '02')
no_cross_pairs = []
for i in range(3):
    for j in range(i + 1, 3):
        no_cross_pairs.append((cycle[i], cycle[j]))
for spoke_or_bridge in ('04', '15', '23', '34'):
    for t in cycle:
        no_cross_pairs.append((spoke_or_bridge, t))

assert len(no_cross_pairs) == 15
for a, b in no_cross_pairs:
    d = dot_interval(a, b)
    assert abs_lower(d) > Q(11, 20), (a, b, d)

print('PASS: all 15 required train pairs satisfy |u.v| > 11/20 > 1/2')
print('PASS: the full certified collapsed root box is excluded by the Jordan train-cycle obstruction')
