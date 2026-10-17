#!/usr/bin/env python3
"""Exact sanity checks for the persistent-endpoint-dispersion note.

This is a certificate for the finite algebra in PE.3--PE.13 and a numerical
check of the elementary cone estimate used in PE.22. It does not prove the
upstream persistent-stress or C67 geometric theorems.
"""
from fractions import Fraction as F
from math import pi, sin


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def scale(c, a):
    return (c * a[0], c * a[1])


def norm2(a):
    return a[0] * a[0] + a[1] * a[1]


# Three rational unit directions and positive rational KKT weights.
v = [(F(1), F(0)), (F(3, 5), F(4, 5)), (F(3, 5), F(-4, 5))]
beta = [F(1, 5), F(1, 7), F(1, 11)]
assert all(norm2(u) == 1 for u in v)
p = sum(beta)
V = (
    sum(w * u[0] for w, u in zip(beta, v)),
    sum(w * u[1] for w, u in zip(beta, v)),
)
a2 = norm2(V)

# PE.4: exact pairwise direction energy.
Q = sum(
    beta[i] * beta[j] * norm2(sub(v[i], v[j]))
    for i in range(len(v))
    for j in range(len(v))
)
assert Q == 2 * (p * p - a2)

# Realize every direction as an actual diameter of one diameter-2 finite set:
# x_h=-v_h, y_h=v_h all lie on the unit circle.
D = F(2)
x = [scale(F(-1), u) for u in v]
y = list(v)
for i in range(len(v)):
    assert norm2(sub(y[i], x[i])) == D * D
for z in x + y:
    for w in x + y:
        assert norm2(sub(z, w)) <= D * D

# PE.6 pairwise endpoint bounds and PE.7 converse second-moment bound.
for i in range(len(v)):
    for j in range(len(v)):
        dv2 = norm2(sub(v[i], v[j]))
        dx2 = norm2(sub(x[i], x[j]))
        dy2 = norm2(sub(y[i], y[j]))
        assert dx2 <= D * D * dv2
        assert dy2 <= D * D * dv2
        assert D * D * dv2 <= 2 * (dx2 + dy2)

# PE.9 endpoint-energy sandwich.
E = sum(
    beta[i]
    * beta[j]
    * (norm2(sub(x[i], x[j])) + norm2(sub(y[i], y[j])))
    for i in range(len(v))
    for j in range(len(v))
)
diff = p * p - a2
assert D * D * diff <= E <= 4 * D * D * diff

# PE.3 and PE.10--PE.13 barycentric identities/bounds.
xbar = scale(
    F(1, 1) / p,
    (
        sum(w * z[0] for w, z in zip(beta, x)),
        sum(w * z[1] for w, z in zip(beta, x)),
    ),
)
ybar = scale(
    F(1, 1) / p,
    (
        sum(w * z[0] for w, z in zip(beta, y)),
        sum(w * z[1] for w, z in zip(beta, y)),
    ),
)
assert sub(ybar, xbar) == scale(D / p, V)

var = sum(
    w * (norm2(sub(xx, xbar)) + norm2(sub(yy, ybar)))
    for w, xx, yy in zip(beta, x, y)
)
assert E == 2 * p * var
sigma = var / (p * D * D)
rho2 = a2 / (p * p)
assert F(1, 2) * (1 - rho2) <= sigma <= 2 * (1 - rho2)

# PE.22 uses sin(theta/2)>=theta/pi for 0<theta<=1.
for k in range(1, 1001):
    theta = k / 1000.0
    assert sin(theta / 2.0) + 1e-15 >= theta / pi

# Balanced PS1 core choice theta=e^(1/3): the discarded-mass bound, relative
# support-size bound, and relative cluster radius all tend to zero with e.
prev = None
for exponent in range(1, 13):
    e = 10.0 ** (-exponent)
    theta = e ** (1.0 / 3.0)
    discarded_bound = (pi * pi / 2.0) * e ** (1.0 / 3.0)
    relative_count_bound = 2.0 * theta
    relative_cluster_radius = 2.0 * theta
    triple = (discarded_bound, relative_count_bound, relative_cluster_radius)
    if prev is not None:
        assert all(a < b for a, b in zip(triple, prev))
    prev = triple

print("persistent endpoint dispersion certificate: PASS")
print("p =", p)
print("|V|^2 =", a2)
print("Q =", Q)
print("E =", E)
print("Sigma =", sigma)
print("rho^2 =", rho2)
