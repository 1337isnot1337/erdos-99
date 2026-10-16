#!/usr/bin/env python3
"""Regression checks for the high-t region-saturation nested-rail amplification."""

from decimal import Decimal, getcontext
from fractions import Fraction as Q
import math

getcontext().prec = 60

rho = Q(1, 5000)
one_hub_side = rho / 2
one_birth_host = rho / 4
one_destination = rho / 8

assert one_hub_side == Q(1, 10_000)
assert one_birth_host == Q(1, 20_000)
assert one_destination == Q(1, 40_000)

# The previous unconditional blocker-fork nested rail.
old_nested = Q(791, 640_000_000)
ratio = one_birth_host / old_nested
assert ratio > Q(4045, 100)
assert ratio < Q(4046, 100)

# Internal-region count: after excluding an internal hub, the larger strict
# side always contains at least (m-2)/2 internal nonhub regions.
for m in range(3, 100):
    for k in range(m + 1):
        left = len([i for i in range(1, m) if i < k])
        right = len([i for i in range(1, m) if i > k])
        assert left + right >= m - 2
        assert max(left, right) * 2 >= m - 2

# Nested-support combinatorics: increasing birth tags plus nonincreasing death
# tags force strict nesting, including repeated death tags.
for k in range(2, 12):
    births = list(range(0, k))
    for shift in range(4):
        deaths = [k + shift + (len(births) - 1 - j) // 2 for j in range(len(births))]
        assert all(a >= b for a, b in zip(deaths, deaths[1:]))
        supports = [set(range(i + 1, b + 1)) for i, b in zip(births, deaths)]
        for a, b in zip(supports, supports[1:]):
            assert b < a

D = Decimal
root8_3 = D(3) ** (D(1) / D(8))

def dec(q: Q) -> Decimal:
    return D(q.numerator) / D(q.denominator)

# C67 partner-collision thinning: Delta(H) <= (4*3^(1/8)+o(1))D^(3/4).
all_side_disjoint = dec(one_hub_side) / (D(4) * root8_3)
nested_disjoint = dec(one_birth_host) / (D(4) * root8_3)
destination_disjoint = dec(one_destination) / (D(4) * root8_3)

assert D('2.17920e-5') < all_side_disjoint < D('2.17923e-5')
assert D('1.08960e-5') < nested_disjoint < D('1.08962e-5')
assert D('5.4480e-6') < destination_disjoint < D('5.4481e-6')

# Direction-packing span for a one-destination linear subrail.
mu = dec(one_destination)
span_angle = mu
span_chord = D(str(math.sin(float(mu) / 2)))
assert span_angle == D('0.000025')
assert D('1.2499999999e-5') < span_chord < D('1.2500000001e-5')

print('PASS: high-t region-saturation nested-rail amplification regressions')
print('path density rho =', float(rho))
print('one hub-side switching density =', float(one_hub_side))
print('one birth-host nested density =', float(one_birth_host))
print('one physical-destination density =', float(one_destination))
print('improvement over previous unconditional nested rail =', float(ratio))
print('one-hub-side disjoint coefficient =', all_side_disjoint)
print('nested disjoint coefficient =', nested_disjoint)
print('one-destination disjoint coefficient =', destination_disjoint)
print('one-destination angular-span floor =', span_angle)
print('one-destination chord-span coefficient =', span_chord)
