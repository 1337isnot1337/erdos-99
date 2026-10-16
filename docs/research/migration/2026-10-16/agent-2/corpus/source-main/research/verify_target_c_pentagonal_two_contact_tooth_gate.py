#!/usr/bin/env python3
"""Arithmetic and equality-model regression for the pentagonal two-contact tooth gate."""
from decimal import Decimal, getcontext

getcontext().prec = 70
D = Decimal
PI = D('3.141592653589793238462643383279502884197169399375105820974944592307816')
SQRT3 = D(3).sqrt()
DELTA2 = PI / (D(2) * SQRT3)
FSTAR = DELTA2.sqrt() - PI / D(4) + D('0.00021')

PAIR = FSTAR / D(9)
TRIPLE = FSTAR / D(13)
PAIR_ALT = FSTAR / D(10)
TRIPLE_ALT = FSTAR / D(14)
WHOLE_FACE = FSTAR / D(21)

assert D('0.16712464346650') < FSTAR < D('0.16712464346652')
assert D('0.0185694') < PAIR < D('0.0185695')
assert D('0.0128557') < TRIPLE < D('0.0128558')
assert D('0.0167124') < PAIR_ALT < D('0.0167125')
assert D('0.0119374') < TRIPLE_ALT < D('0.0119376')
assert TRIPLE > WHOLE_FACE

# Equality pentagon from the trapezoid classification.
pts = [
    (D(0), D(0)),
    (D(1), D(0)),
    (D(2), D(0)),
    (D(3) / D(2), SQRT3 / D(2)),
    (D(1) / D(2), SQRT3 / D(2)),
]

def d2(i, j):
    dx = pts[i][0] - pts[j][0]
    dy = pts[i][1] - pts[j][1]
    return dx * dx + dy * dy

# Cyclic boundary edges are all unit.
for i in range(5):
    assert abs(d2(i, (i + 1) % 5) - D(1)) < D('1e-60')

# The two leaf teeth are (m,l,b)=(1,0,4) and (m,r,a)=(1,2,3).
for tooth in ((1, 0, 4), (1, 2, 3)):
    x, y, z = tooth
    assert abs(d2(x, y) - D(1)) < D('1e-60')
    assert abs(d2(y, z) - D(1)) < D('1e-60')
    assert abs(d2(x, z) - D(1)) < D('1e-60')

MAX_FACE_OCC_AT_VERTEX = 5
PAIR_CONFLICT = 2 * (MAX_FACE_OCC_AT_VERTEX - 1)
TRIPLE_CONFLICT = 3 * (MAX_FACE_OCC_AT_VERTEX - 1)
assert PAIR_CONFLICT == 8
assert TRIPLE_CONFLICT == 12

print('PASS pentagonal two-contact tooth gate regression')
print('f_star=', FSTAR)
print('endpoint_disjoint_pair_floor_if_X_sublinear=', PAIR)
print('vertex_disjoint_tooth_floor_if_X_sublinear=', TRIPLE)
print('unweighted_pair_tradeoff_threshold=', PAIR_ALT)
print('unweighted_tooth_tradeoff_threshold=', TRIPLE_ALT)
print('whole_pentagon_floor=', WHOLE_FACE)
