#!/usr/bin/env python3
"""Regression checks for dominant-pentagon through-splicing.

The proof is in target_c_dominant_pentagon_through_splicing_2026-09-15.md.
This script checks the six exact triangular-ray closure patterns, the base-pattern
midpoint connectors, the graph contraction algebra, and the displayed current-scale
K_sp value.
"""

from decimal import Decimal, getcontext
from itertools import product

getcontext().prec = 80
D = Decimal

# Six oriented lattice rays in the integer basis a,b with c=b-a.
rays = [
    (1, 0),   # a
    (0, 1),   # b
    (-1, 1),  # c=b-a
    (-1, 0),  # -a
    (0, -1),  # -b
    (1, -1),  # -c
]

patterns = []
for counts in product(range(6), repeat=6):
    if sum(counts) != 5:
        continue
    x = sum(counts[i] * rays[i][0] for i in range(6))
    y = sum(counts[i] * rays[i][1] for i in range(6))
    if x == 0 and y == 0:
        patterns.append(counts)

expected = {
    (0, 1, 1, 1, 0, 2),
    (0, 2, 0, 1, 1, 1),
    (1, 0, 2, 0, 1, 1),
    (1, 1, 0, 2, 0, 1),
    (1, 1, 1, 0, 2, 0),
    (2, 0, 1, 1, 1, 0),
}
assert set(patterns) == expected

# Each solution has projective phase totals 3,1,1 and the size-3 phase has signs 2,1.
for n in patterns:
    phase_totals = [n[i] + n[i + 3] for i in range(3)]
    assert sorted(phase_totals) == [1, 1, 3]
    repeated = phase_totals.index(3)
    assert sorted([n[repeated], n[repeated + 3]]) == [1, 2]

# Base representative a,b,c,-b,-b. Work in exact Cartesian coordinates with sqrt(3).
sqrt3 = D(3).sqrt()
a = (D(1), D(0))
b = (D('0.5'), sqrt3 / D(2))
c = (-D('0.5'), sqrt3 / D(2))
minus_b = (-b[0], -b[1])
edges = [a, b, c, minus_b, minus_b]
pts = [(D(0), D(0))]
for ex, ey in edges:
    x, y = pts[-1]
    pts.append((x + ex, y + ey))
assert abs(pts[-1][0]) < D('1e-70') and abs(pts[-1][1]) < D('1e-70')
mids = [
    ((pts[i][0] + pts[i + 1][0]) / D(2),
     (pts[i][1] + pts[i + 1][1]) / D(2))
    for i in range(5)
]

conn1 = (mids[3][0] - mids[1][0], mids[3][1] - mids[1][1])
conn2 = (mids[4][0] - mids[1][0], mids[4][1] - mids[1][1])
assert abs(conn1[0] - c[0]) < D('1e-70')
assert abs(conn1[1] - c[1]) < D('1e-70')
assert abs(conn2[0] + a[0]) < D('1e-70')
assert abs(conn2[1] + a[1]) < D('1e-70')

# n_b=Jb. Both connectors have dot sqrt(3)/2 with n_b and unit length.
nb = (-b[1], b[0])
for v in [conn1, conn2]:
    dot = v[0] * nb[0] + v[1] * nb[1]
    norm2 = v[0] * v[0] + v[1] * v[1]
    assert abs(dot - sqrt3 / D(2)) < D('1e-70')
    assert abs(norm2 - D(1)) < D('1e-70')

# Graph algebra. With M original vertices and P forest contractions,
# N=M-P quotient vertices. If r<=P quotient vertices are nonsingleton,
# the simple quotient has E<=s^2/4+rs+r(r-1)/2. Its quadratic part at r=P is
# M^2/4-P^2/2.
# Check the exact polynomial identity after dropping only the favorable -P/2 term.
for M, P in [(100, 10), (137, 23), (1000, 167)]:
    N = M - P
    r = P
    s = N - r
    rhs = D(s * s) / D(4) + D(r * s) + D(r * (r - 1)) / D(2)
    relaxed = D(M * M) / D(4) - D(P * P) / D(2)
    assert rhs <= relaxed

# Current branch scale.
pi = D('3.1415926535897932384626433832795028841971693993751058209749445923078164')
Delta2 = pi / (D(2) * sqrt3)
s2 = Delta2.sqrt()
C22 = D(2) * s2 + D('0.00522')
t = D('1.83240')
rad = C22 * C22 / D(2) - D(2) * Delta2
assert rad > 0
Ksp = D(8) * Delta2 / C22 - D(2) * C22 + t - rad.sqrt()
assert D('1.7117') < Ksp < D('1.7119')

print('PASS dominant-pentagon through-splicing regression')
print('six closure patterns =', len(patterns))
print('base connectors =', conn1, conn2)
print('C22 =', C22)
print('K_sp(1.83240, boundary) =', Ksp)
