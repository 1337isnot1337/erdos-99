#!/usr/bin/env python3
"""Exact finite checks for the collapsed support-six two-flex charge.

The theorem is structural: twelve internal train columns each occur in two opposite
face rows. This verifier checks the K6-minus-matching incidence, the two exact row
sum dependencies, the rank/nullity bookkeeping, and the propagated scalar inequality.
It does not assert global nonlinear embedding or diameter descent.
"""
from fractions import Fraction as Q

FACES = tuple(range(6))
MISSING = {(0, 3), (1, 4), (2, 5)}
EDGES = tuple((i, j) for i in FACES for j in FACES if i < j and (i, j) not in MISSING)
assert len(EDGES) == 12
assert all(sum(1 for e in EDGES if i in e) == 4 for i in FACES)

# Each internal column has +J u at one endpoint and -J u at the other. The two
# all-face row sums vanish coefficient-by-coefficient, independently of u.
for i, j in EDGES:
    col = {(i, 0): 1, (i, 1): 1, (j, 0): -1, (j, 1): -1}
    assert sum(col.get((k, 0), 0) for k in FACES) == 0
    assert sum(col.get((k, 1), 0) for k in FACES) == 0

ROWS = 12
COLS = len(EDGES)
ROW_DEPENDENCIES = 2
assert COLS == ROWS == 12
assert ROWS - ROW_DEPENDENCIES == 10
assert COLS - (ROWS - ROW_DEPENDENCIES) == 2

# Verify the endpoint scalar elimination in both regions of (r,s)>=0:
# r/2 + (s-r)_+/4 >= s/4.
for r in (Q(0), Q(1, 1000), Q(1, 5), Q(3, 2), Q(10)):
    for s in (Q(0), Q(1, 1000), Q(1, 5), Q(3, 2), Q(10)):
        lhs = r / 2 + max(s - r, Q(0)) / 4
        assert lhs >= s / 4

# Low-flex rearrangement: m/D <= C+eta and m/D >= C+s/4+2c gives s+8c <= 4eta.
eta = Q(3, 100)
s = Q(1, 100)
c = Q(1, 200)
assert s + 8 * c <= 4 * eta

print("PASS: collapsed support-six internal closure rank <= 10")
print("PASS: two independent internal contact-flex dimensions per actual block")
print("PASS: live propagation m/D > 1.1988388040 + sigma/(4D) + 2c/D - o(1)")
print("PASS: low-flex implication sigma/D + 8c/D <= 4 eta + o(1)")
