#!/usr/bin/env python3
"""Regression checks for saturation-to-common-grid synchronization."""

from decimal import Decimal, getcontext
from fractions import Fraction as Q

getcontext().prec = 60

alpha = Q(7, 625_000)   # 0.0000112 safe A_0 row density
beta = Q(783, 10_000)   # 0.0783 B_0 column density
one_side_rows = alpha / 2
sync_rows = alpha / 4
nested_sync = alpha / 8
one_destination = alpha / 16

assert float(alpha) == 0.0000112
assert one_side_rows == Q(7, 1_250_000)
assert sync_rows == Q(7, 2_500_000)
assert nested_sync == Q(7, 5_000_000)
assert one_destination == Q(7, 10_000_000)
assert beta == Q(783, 10_000)

# Finite median-index lemma. For any row subset on one pre-hub side, the last
# floor(R/2) rows have at least floor(R/2) earlier internal birth regions.
for k in range(3, 18):
    universe = list(range(1, k))
    for mask in range(1, 1 << len(universe)):
        rows = [universe[j] for j in range(len(universe)) if mask & (1 << j)]
        R = len(rows)
        L = R // 2
        if L == 0:
            continue
        hubward = rows[-L:]
        j0 = hubward[0]
        earlier_regions = list(range(1, j0))
        assert len(hubward) == L
        assert len(earlier_regions) >= L
        # A one-sided support [i+1,b], b>=k, contains every retained hubward row.
        for i in earlier_regions:
            for j in hubward:
                assert i < j < k

D = Decimal
root8_3 = D(3) ** (D(1) / D(8))

def dec(q: Q) -> Decimal:
    return D(q.numerator) / D(q.denominator)

sync_disjoint = dec(sync_rows) / (D(4) * root8_3)
nested_disjoint = dec(nested_sync) / (D(4) * root8_3)
destination_disjoint = dec(one_destination) / (D(4) * root8_3)

assert D('6.1017e-7') < sync_disjoint < D('6.1019e-7')
assert D('3.0508e-7') < nested_disjoint < D('3.0510e-7')
assert D('1.5254e-7') < destination_disjoint < D('1.5255e-7')

# Product size stays quadratic after synchronization.
product = dec(sync_rows) * dec(beta)
assert D('2.1923e-7') < product < D('2.1925e-7')

print('PASS: high-t saturation-to-common-grid synchronization regressions')
print('A0 row density =', float(alpha))
print('one-side A0 row density =', float(one_side_rows))
print('synchronized E0/A1 density =', float(sync_rows))
print('nested synchronized density =', float(nested_sync))
print('one-destination synchronized density =', float(one_destination))
print('B0 column density =', float(beta))
print('synchronized A1 x B0 product coefficient =', product)
print('E0 disjoint coefficient =', sync_disjoint)
print('nested synchronized disjoint coefficient =', nested_disjoint)
print('one-destination synchronized disjoint coefficient =', destination_disjoint)
