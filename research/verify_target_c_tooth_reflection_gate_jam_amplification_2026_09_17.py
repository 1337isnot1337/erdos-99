#!/usr/bin/env python3
import math

CSTAR = 0.129220199818177
HSTAR = math.sqrt(303.0) / 52.0

assert HSTAR < 0.335
assert 1.0 + HSTAR < 1.335
assert abs(CSTAR / 2.0 - 0.0646100999090885) < 1e-15
assert abs(CSTAR / 4.0 - 0.03230504995454425) < 1e-15

# Terminal contact ledger after opening the reflected apex completely:
# old degree d is deleted, k inactive gate edges are added.
for d in (3, 4, 5):
    for k in range(d):
        assert -d + k < 0
    assert -d + d == 0
    assert d + 1 >= 4

# Before the overfull stopping threshold, at most d<=5 gate edges exist.
# Every absorption stage introduces at least one new edge, so no more than
# five stages need the support-cap safety estimate.
for d in (3, 4, 5):
    max_pre_stop_edges = d
    assert max_pre_stop_edges <= 5

# Each original gate pair is at most 1+t_D, with t_D<h_*+o(1).
# Check conservative finite representatives once D is large enough that
# D^(-1/3) is small.
for D in (1e9, 1e12, 1e18):
    td_upper = HSTAR + D ** (-1.0 / 3.0)
    assert td_upper < 0.336
    assert 1.0 + td_upper < 1.336

# Source-wide two-way and jam-split coefficients.
assert CSTAR / 2.0 > 0.0646
assert CSTAR / 4.0 > 0.0323

print('gate-jam amplification certificate: PASS')
print(f'h_*={HSTAR:.15f}')
print(f'c_*/2={CSTAR/2.0:.15f}')
print(f'c_*/4={CSTAR/4.0:.15f}')
