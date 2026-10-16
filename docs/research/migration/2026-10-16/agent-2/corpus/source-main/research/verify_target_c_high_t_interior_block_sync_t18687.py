#!/usr/bin/env python3
"""Regression checks for interior-block synchronization of the high-t train path."""

from fractions import Fraction as Q
import math

rho = Q(1019, 5_000_000)  # 0.0002038 selected O-O path density
r = Q(817, 1250)          # 0.6536 crossing-neighbor floor per selected row
T = Q(6121, 2000)         # 3.0605 complete-train/right-endpoint ceiling


def coeffs(N: int):
    assert N >= 8
    a = rho / N
    b = r - T / (N - 3)
    return a, b, a * b

# Positivity starts at N=8 under the safe displayed constants.
for N in range(8, 80):
    assert coeffs(N)[1] > 0

# The product a_N b_N is maximized at integer N=14.
products = {N: coeffs(N)[2] for N in range(8, 1000)}
Nbest = max(products, key=products.get)
assert Nbest == 14
# Continuous derivative numerator is -(6536 x^2 -100426 x+150639),
# whose large positive root lies strictly between 13 and 14.
disc = 100426**2 - 4 * 6536 * 150639
root_hi = (100426 + math.sqrt(disc)) / (2 * 6536)
assert 13 < root_hi < 14

# N=14 product-optimized scaffold.
a14, b14, prod14 = coeffs(14)
assert a14 == Q(1019, 70_000_000)
assert b14 == Q(41291, 110_000)
assert 1.4557e-5 < float(a14) < 1.4558e-5
assert 0.37537 < float(b14) < 0.37538
assert 5.4643e-6 < float(prod14) < 5.4644e-6

# One consistent orientation retains asymptotically half the B shore.
b14_plus = b14 / 2
oriented_prod = a14 * b14_plus
assert 0.18768 < float(b14_plus) < 0.18769
assert 2.7321e-6 < float(oriented_prod) < 2.7323e-6

# 90% post-synchronization purification on each train shore.
eps = Q(1, 10)
a90 = (1 - eps) * a14
b90 = (1 - eps) * b14_plus
prod90 = a90 * b90
assert 1.3101e-5 < float(a90) < 1.3102e-5
assert 0.16891 < float(b90) < 0.16893
assert 2.2130e-6 < float(prod90) < 2.2132e-6

Cphase = math.pi**2 * math.sqrt(3.0) * (2.0 + math.sqrt(3.0)) / 12.0
avg_coeff = Cphase / float(oriented_prod)
angle90 = 21.0 * avg_coeff
assert 1.945e6 < avg_coeff < 1.947e6
assert 4.08e7 < angle90 < 4.09e7

c = math.sqrt(3.0) / 2.0
row_span90 = c * float(b90)
col_span90 = c * float(a90)
assert 0.14628 < row_span90 < 0.14630
assert 1.1345e-5 < col_span90 < 1.1348e-5

# N=8 is the diameter-heavy endpoint of the positive family.
a8, b8, _ = coeffs(8)
assert a8 == Q(2038, 80_000_000)
assert b8 == Q(83, 2000)  # 0.0415
assert float(a8) == 2.5475e-5
assert float(b8) == 0.0415
host8 = a8 / 2
dest8 = a8 / 4
assert float(host8) == 1.27375e-5
assert float(dest8) == 6.36875e-6

# Coarse block/hub sanity: after excluding endpoint blocks and at most one
# hub-straddling block, at least N-3 eligible blocks remain. Every eligible block
# has a whole neighboring block on the outward side from the hub.
for N in range(8, 25):
    for hub_block in list(range(N)) + [None]:
        excluded = {0, N - 1}
        if hub_block is not None:
            excluded.add(hub_block)
        eligible = [j for j in range(N) if j not in excluded]
        assert len(eligible) >= N - 3
        for j in eligible:
            if hub_block is None:
                assert j > 0 and j < N - 1
            elif j < hub_block:
                assert j - 1 >= 0
            elif j > hub_block:
                assert j + 1 <= N - 1

print('PASS: high-t interior-block synchronization regressions')
print('best integer block count =', Nbest)
print('continuous product maximizer =', root_hi)
print('N=14 row/diameter density =', float(a14))
print('N=14 transverse density =', float(b14))
print('N=14 oriented transverse density =', float(b14_plus))
print('N=14 raw grid product =', float(prod14))
print('N=14 oriented product =', float(oriented_prod))
print('N=14 90% row density =', float(a90))
print('N=14 90% column density =', float(b90))
print('N=14 90% grid product =', float(prod90))
print('N=14 90% angle coefficient =', angle90)
print('N=14 90% row metric span =', row_span90)
print('N=14 90% column metric span =', col_span90)
print('N=8 row/diameter density =', float(a8))
print('N=8 transverse density =', float(b8))
print('N=8 fixed-host rail density =', float(host8))
print('N=8 fixed-destination rail density =', float(dest8))
