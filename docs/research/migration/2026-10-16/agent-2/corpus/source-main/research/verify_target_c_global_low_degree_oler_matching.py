#!/usr/bin/env python3
"""Exact outward arithmetic for the global low-degree Oler/matching theorem."""
from fractions import Fraction as Q
from math import isqrt


def atan_inv_bounds(q, n):
    s = Q(0)
    for k in range(n):
        term = Q(1, (2*k+1)*q**(2*k+1))
        s += term if k % 2 == 0 else -term
    nxt = Q(1, (2*n+1)*q**(2*n+1))
    return (s, s+nxt) if n % 2 == 0 else (s-nxt, s)


def sqrt_bounds(lo, hi, scale):
    a = isqrt((lo.numerator*scale*scale)//lo.denominator)
    b = isqrt((hi.numerator*scale*scale)//hi.denominator)
    return Q(a, scale), Q(b+1, scale)


a5l, a5h = atan_inv_bounds(5, 90)
a239l, a239h = atan_inv_bounds(239, 25)
pil, pih = 16*a5l-4*a239h, 16*a5h-4*a239l
SCALE = 10**100
n3 = isqrt(3*SCALE*SCALE)
s3l, s3h = Q(n3, SCALE), Q(n3+1, SCALE)
Dl, Dh = pil/(2*s3h), pih/(2*s3l)
sDl, _ = sqrt_bounds(Dl, Dh, SCALE)
C707 = 2*sDl + Q(7707, 1000000)

# Universal Type-II endpoint is t<=pi+o(1). For r=22,
# L_22(pi) = [(19/2) C707 - (23/4) pi] / 18.
# The pi coefficient is negative, so use the outward upper bound pih.
face_floor = (Q(19, 2)*C707 - Q(23, 4)*pih) / 18
assert face_floor > Q(57, 10000)

# One selected hidden-pair occurrence per face. Endpoint occurrence degree is <=5,
# hence the conflict graph of pair occurrences has degree <=8 and greedy matching
# loses at most a factor 9.
matching_floor = face_floor / 9
assert matching_floor > Q(63, 100000)

for endpoint_degree in range(1, 6):
    assert 2*(endpoint_degree-1) <= 8

print('C707 lower =', float(C707))
print('universal degree<=22 face floor/D >', float(face_floor))
print('endpoint-disjoint matching floor/D >', float(matching_floor))
print('safe displayed matching floor =', float(Q(63, 100000)))
print('PASS global low-degree Oler matching arithmetic')
