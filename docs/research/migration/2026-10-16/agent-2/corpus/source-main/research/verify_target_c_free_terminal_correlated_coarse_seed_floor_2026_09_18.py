#!/usr/bin/env python3
"""Exact certificate for the correlated coarse pentagon-seed defect floor."""
from fractions import Fraction
from math import isqrt

Q = Fraction


def atan_inv_bounds(q, terms):
    s = Q(0)
    for j in range(terms):
        t = Q(1, (2*j+1)*q**(2*j+1))
        s += t if j % 2 == 0 else -t
    nxt = Q(1, (2*terms+1)*q**(2*terms+1))
    return (s, s+nxt) if terms % 2 == 0 else (s-nxt, s)


def sqrt_floor(x, scale):
    n = isqrt((x.numerator*scale*scale)//x.denominator)
    y = Q(n, scale)
    assert y*y <= x
    return y


def sqrt_ceil(x, scale):
    n = isqrt((x.numerator*scale*scale)//x.denominator) + 1
    y = Q(n, scale)
    assert y*y >= x
    return y


S = 10**90
a5l, a5h = atan_inv_bounds(5, 100)
a239l, a239h = atan_inv_bounds(239, 30)
pil = 16*a5l - 4*a239h
pih = 16*a5h - 4*a239l

n3 = isqrt(3*S*S)
s3l = Q(n3, S)
s3h = Q(n3+1, S)
d2l = pil/(2*s3h)
d2h = pih/(2*s3l)
s2l = sqrt_floor(d2l, S)
s2h = sqrt_ceil(d2h, S)

g = Q(7707, 10**6)
eps = Q(71, 10000)
delta0 = Q(17609, 10**6)
delta_max = 5*eps/2
Mhi = 4*s2h + 2*g

# K_* = pi - mu_*; lower enclosure uses pi_lo and s2_hi.
Kstar_lo = pil/2 - Q(2, 5)*s2h - g/5

# In (11) the worst correlated defect penalty is
# [35 eps + 10(delta_max - 2 delta0)]/15.
penalty_hi = (35*eps + 10*(delta_max - 2*delta0))/15

x_lo = Kstar_lo - Q(2, 15)*Mhi - penalty_hi
assert x_lo > Q(6734530, 10**7)

# The sharper seventh-decimal statement is also true, but the note keeps a
# larger visible margin.
assert x_lo > Q(6734531, 10**7)

# Updated safe middle/coarse crossing using the separately certified
# correlated degree-weighted line 1.5158692 - (8/15)m.
weighted_safe = Q(15158692, 10**7)
coarse_safe = Q(6734530, 10**7)
m_cross = Q(15, 8)*(weighted_safe - coarse_safe)
assert m_cross == Q(12636243, 8000000)
assert m_cross == Q(1579530375, 10**9)

print('PASS: correlated coarse pentagon-seed floor certified')
print('K_* lower >', float(Kstar_lo))
print('worst correlated defect penalty <', float(penalty_hi))
print('(d_H+p_D)/D >', float(x_lo))
print('safe weighted/coarse crossing m =', float(m_cross))
