#!/usr/bin/env python3
"""Exact arithmetic certificate for the one-row near-unit LOWER theorem.

The companion proof is symbolic. This script checks every rational margin used in
the nonincident-face and one-endpoint-incidence contradictions. The diagonal/row
angle gap is exact from the strict rhombus angle interval and needs no floating-point
decision.
"""
from fractions import Fraction as Q


eps = Q(1, 20)
ell_max = Q(21, 20)

# Nonincident crossed face.
delta = 4 * eps + 4 * eps * eps
assert delta == Q(21, 100)

# Every rhombus vertex has |a| <= 63/100, hence |b| > 3/4, while
# the upper distance window gives |b| <= 11/10.
x_abs_max = Q(21, 40) + Q(21, 200)
assert x_abs_max == Q(63, 100)
assert 1 - x_abs_max * x_abs_max > Q(9, 16)
assert 1 + delta == Q(121, 100)

# Two vertices in the same sign strip would be closer than one.
same_sign_d2 = delta * delta + Q(7, 20) ** 2
assert same_sign_d2 == Q(833, 5000)
assert same_sign_d2 < 1

# One-endpoint incidence. The proof uses sqrt(1159)>34 and sqrt(3)/2>6/7.
assert 1159 > 34 * 34
assert Q(3, 4) > Q(36, 49)
cos_floor = -Q(21, 80) + Q(6, 7) * Q(17, 20)
assert cos_floor == Q(261, 560)
assert cos_floor > Q(13, 28)

# Thus e.(u+v)>13/14 and |u+v|<=ell. The opposite face vertex is <1
# from the other source endpoint even under a deliberately loose rational bound.
far_vertex_d2 = 2 * ell_max * ell_max - Q(13, 7)
assert far_vertex_d2 == Q(487, 1400)
assert far_vertex_d2 < 1

print("one-row LOWER classification certificate: PASS")
print("epsilon cap =", eps, "; length cap =", ell_max)
print("nonincident same-sign vertex diameter^2 bound =", same_sign_d2, "=", float(same_sign_d2))
print("one-endpoint opposite-vertex distance^2 bound =", far_vertex_d2, "=", float(far_vertex_d2))
