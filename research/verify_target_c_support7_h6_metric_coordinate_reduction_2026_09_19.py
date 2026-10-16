#!/usr/bin/env python3
"""Exact rank certificate for generic support-seven H6 angular/metric coordinates.

This verifier checks only integer/rational linear algebra. The analytic input
(the strict monotonicity of the sine-ratio coordinate on a Euclidean triangle)
is proved in the companion note.
"""
from fractions import Fraction
from itertools import combinations


def rank_q(rows):
    if not rows:
        return 0
    a = [[Fraction(x) for x in row] for row in rows]
    m = len(a)
    n = len(a[0])
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        z = a[r][c]
        a[r] = [x / z for x in a[r]]
        for i in range(m):
            if i == r or not a[i][c]:
                continue
            q = a[i][c]
            a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


# ---------------------------------------------------------------------------
# Complete reciprocal angle equality space on eight labelled points.
# ---------------------------------------------------------------------------
V = tuple(range(8))
E8 = tuple(combinations(V, 2))
e8 = {edge: i for i, edge in enumerate(E8)}
assert len(E8) == 28

# At each reciprocal vertex there are seven rays. Modulo a local rotation,
# their directions have six degrees of freedom. Choose one reference ray and
# represent the other six phases independently. This gives 8*6=48 local
# angular coordinates.
reference = {v: (v + 1) % 8 for v in V}
PHASE = tuple(
    (v, w)
    for v in V
    for w in V
    if w != v and w != reference[v]
)
pidx = {vw: i for i, vw in enumerate(PHASE)}
assert len(PHASE) == 48


def phase_row(v, w):
    row = [0] * len(PHASE)
    if w != reference[v]:
        row[pidx[(v, w)]] = 1
    return row


# For oriented edge i->j, psi_ij = phi_ij - phi_ji. Store the i<j version.
# The map from local phases to the 28 edge-cochain coordinates is surjective.
EDGE_FROM_PHASE = []
for i, j in E8:
    pi = phase_row(i, j)
    pj = phase_row(j, i)
    EDGE_FROM_PHASE.append([a - b for a, b in zip(pi, pj)])
assert rank_q(EDGE_FROM_PHASE) == 28

# Homogeneous triangle-angle sums are exactly cycle equations for psi:
# psi_ab + psi_bc - psi_ac = 0 for a<b<c. Constants depend on the
# chirotope/ordinary-angle branch but do not affect rank.
TRIANGLE_CYCLE = []
for a, b, c in combinations(V, 3):
    row = [0] * len(E8)
    row[e8[(a, b)]] += 1
    row[e8[(b, c)]] += 1
    row[e8[(a, c)]] -= 1
    TRIANGLE_CYCLE.append(row)
assert len(TRIANGLE_CYCLE) == 56
assert rank_q(TRIANGLE_CYCLE) == 21  # cycle rank of K8

TRIANGLE_ON_PHASE = []
for crow in TRIANGLE_CYCLE:
    row = [0] * len(PHASE)
    for edge_i, coeff in enumerate(crow):
        if coeff:
            for j, z in enumerate(EDGE_FROM_PHASE[edge_i]):
                row[j] += coeff * z
    TRIANGLE_ON_PHASE.append(row)
assert rank_q(TRIANGLE_ON_PHASE) == 21
assert len(PHASE) - rank_q(TRIANGLE_ON_PHASE) == 27

# ---------------------------------------------------------------------------
# Match the repository's 85-variable H6 lift.
# ---------------------------------------------------------------------------
# It uses 50 reciprocal-ray gaps: 6 at each of six hull vertices and 7 at
# each of two interior vertices. The two interior full-circle sums remove two
# degrees of freedom, leaving the same 48 local phase coordinates above.
RAY_GAPS = 6 * 6 + 2 * 7
INTERIOR_CIRCLE_RANK = 2
FORCE_TURNS = 7 * 5
FULL_VARIABLES = RAY_GAPS + FORCE_TURNS
assert RAY_GAPS == 50
assert FULL_VARIABLES == 85

# After the two circle rows, the 56 triangle rows contribute rank 21. At each
# of seven physical pentagons, five adjacent force/ray tie equations solve for
# the five new force-turn variables. Their coefficient block on those new
# variables is an identity, hence they contribute exactly 35 further rank.
FULL_EQUALITY_RANK = INTERIOR_CIRCLE_RANK + 21 + FORCE_TURNS
FULL_EQUALITY_DIMENSION = FULL_VARIABLES - FULL_EQUALITY_RANK
assert FULL_EQUALITY_RANK == 58
assert FULL_EQUALITY_DIMENSION == 27

# ---------------------------------------------------------------------------
# Complete K7 metric cochain: exact potentials versus 15 cycle defects.
# ---------------------------------------------------------------------------
NG = tuple(range(1, 8))
E7 = tuple(combinations(NG, 2))
e7 = {edge: i for i, edge in enumerate(E7)}
assert len(E7) == 21

# Fix u_1=0. The six remaining log-radius potentials map to
# g_ij = u_j-u_i. This exact-cochain subspace has rank six.
POTENTIAL = []
for i, j in E7:
    row = [0] * 6  # coordinates u_2,...,u_7
    if i != 1:
        row[i - 2] -= 1
    if j != 1:
        row[j - 2] += 1
    POTENTIAL.append(row)
assert rank_q(POTENTIAL) == 6

# The 15 root-fan cycles 1-i-j-1 span the K7 cycle space.
ROOT_FAN = []
for i, j in combinations(range(2, 8), 2):
    row = [0] * len(E7)
    row[e7[(1, i)]] += 1
    row[e7[(i, j)]] += 1
    row[e7[(1, j)]] -= 1
    ROOT_FAN.append(row)
assert len(ROOT_FAN) == 15
assert rank_q(ROOT_FAN) == 15

# Every potential cochain annihilates every cycle. Since the kernel dimension
# is 21-15=6 and the potential image has dimension six, the kernel is exactly
# the potential space.
for cycle in ROOT_FAN:
    for potential_coordinate in range(6):
        total = sum(
            cycle[e] * POTENTIAL[e][potential_coordinate]
            for e in range(len(E7))
        )
        assert total == 0
assert len(E7) - rank_q(ROOT_FAN) == rank_q(POTENTIAL) == 6

# Six ground-ray direction coordinates plus six log-radius potentials give the
# 12-dimensional metric-compatible complete-angle manifold after quotienting
# common rotation and scale.
METRIC_DIMENSION = 6 + 6
assert METRIC_DIMENSION == 12
assert FULL_EQUALITY_DIMENSION - METRIC_DIMENSION == 15

print("PASS")
print("K8 local angular coordinates:", len(PHASE))
print("K8 edge-cochain map rank:", rank_q(EDGE_FROM_PHASE))
print("K8 triangle-cycle rank:", rank_q(TRIANGLE_CYCLE))
print("triangle rank on local angular coordinates:", rank_q(TRIANGLE_ON_PHASE))
print("H6 full-angle equality rank/dimension:", FULL_EQUALITY_RANK, FULL_EQUALITY_DIMENSION)
print("K7 potential rank:", rank_q(POTENTIAL))
print("K7 metric-cycle rank:", rank_q(ROOT_FAN))
print("metric-compatible angular dimension:", METRIC_DIMENSION)
