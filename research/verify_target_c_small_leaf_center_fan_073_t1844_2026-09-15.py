#!/usr/bin/env python3
"""Exact Fraction certificate for a >0.73D center fan on one small-leaf O-O train.

Upstream exact certificates supply the safe rounded constants, valid for t<=1.844:
  W <= 1.915963,
  E_dom >= 0.9068958,
  C > 0.8538,
  z_V > 0.616.
The present certificate proves the remaining finite optimization only.
"""

from fractions import Fraction as Q

W = Q(1915963, 1_000_000)
E = Q(9068958, 10_000_000)
a = Q(616, 1000)
L = Q(73, 100)
Cmin = Q(4269, 5000)  # 0.8538
Cmax = Q(1063, 1000)  # 1.063
Vmin = a / 2           # z_V<=2V and z_V>a


def add(p, q):
    n = max(len(p), len(q))
    out = [Q(0)] * n
    for i, x in enumerate(p):
        out[i] += x
    for i, x in enumerate(q):
        out[i] += x
    return out


def mul(p, q):
    out = [Q(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] += x * y
    return out


def scale(p, s):
    return [s * x for x in p]


def deriv(p):
    return [Q(i) * p[i] for i in range(1, len(p))]


def ev(p, x):
    total = Q(0)
    for c in reversed(p):
        total = total * x + c
    return total


# Generic center capacity forces C<Cmax.
assert Cmax * (W - Cmax) < E

# Since V>0.308, the ordering boundary U<=C never truncates the adverse total mass W.
# Also the correlation bound y<=h/b always beats the trivial y<=CV.
Hmax = W * W / 4 - E
dmin = 2 * Cmin + Vmin - W
assert dmin > 0
assert Vmin * dmin > Hmax

# For fixed C, after taking adverse W and E, average center degree per retained V-pair is
#   R(C,V) >= C - C H(C)/[(2C+V-W)(a-V)],
# where H(C)=C(W-C)-E.  The denominator in V is concave, so its minimum on
# V in [a/2,(W-C)/2] occurs at one of the endpoints.
X = [Q(0), Q(1)]
Hp = [-E, W, -Q(1)]

# Low endpoint V=a/2.
Nlo = add(
    mul(mul([-L, Q(1)], [Vmin - W, Q(2)]), [a - Vmin]),
    scale(mul(X, Hp), -1),
)

# Balanced endpoint V=(W-C)/2.
Nhi = add(
    mul(
        mul([-L, Q(1)], [-W / 2, Q(3, 2)]),
        [(2 * a - W) / 2, Q(1, 2)],
    ),
    scale(mul(X, Hp), -1),
)

dNlo = deriv(Nlo)
d2Nlo = deriv(dNlo)
dNhi = deriv(Nhi)
d2Nhi = deriv(dNhi)

# Both derivative polynomials are strictly increasing on the whole feasible C interval.
assert ev(d2Nlo, Cmin) > 0 and ev(d2Nlo, Cmax) > 0
assert ev(d2Nhi, Cmin) > 0 and ev(d2Nhi, Cmax) > 0

# Unique minima are bracketed by short rational intervals.
lo_a, lo_b = Q(8810, 10000), Q(8811, 10000)
hi_a, hi_b = Q(9033, 10000), Q(9034, 10000)
assert Cmin < lo_a < lo_b < Cmax
assert Cmin < hi_a < hi_b < Cmax
assert ev(dNlo, lo_a) < 0 < ev(dNlo, lo_b)
assert ev(dNhi, hi_a) < 0 < ev(dNhi, hi_b)

# A derivative-Lipschitz interval bound certifies positivity at each minimum.
lo_min_lower = ev(Nlo, lo_a) - max(abs(ev(dNlo, lo_a)), abs(ev(dNlo, lo_b))) * (lo_b - lo_a)
hi_min_lower = ev(Nhi, hi_a) - max(abs(ev(dNhi, hi_a)), abs(ev(dNhi, hi_b))) * (hi_b - hi_a)
assert lo_min_lower > 0
assert hi_min_lower > 0

# Endpoints are positive too, so N>0 everywhere.
assert ev(Nlo, Cmin) > 0 and ev(Nlo, Cmax) > 0
assert ev(Nhi, Cmin) > 0 and ev(Nhi, Cmax) > 0

print("PASS: one retained smallest-leaf O-O train has >0.73D center crossings")
print("Hmax =", float(Hmax))
print("uniform denominator lower =", float(dmin))
print("Vmin*dmin-Hmax =", float(Vmin * dmin - Hmax))
print("low-endpoint minimum lower polynomial margin =", float(lo_min_lower))
print("balanced-endpoint minimum lower polynomial margin =", float(hi_min_lower))
print("generic capacity excess at C=1.063 =", float(E - Cmax * (W - Cmax)))
