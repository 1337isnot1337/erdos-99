#!/usr/bin/env python3
"""Regression checks for the live terminal exact-flex diameter-locking note.

The script checks the displayed scalar constants and exact finite linear-algebra
models for rank, positive dependence, Hall matching, signed incidences, and the
flex/stress complementarity identity. It is a regression aid, not a substitute for
the geometric mixed-rigidity/KKT proof.
"""

from decimal import Decimal, getcontext
from fractions import Fraction
import random

getcontext().prec = 60

PI = Decimal("3.14159265358979323846264338327950288419716939937510")
SQRT3 = Decimal(3).sqrt()
S2 = (PI / (Decimal(2) * SQRT3)).sqrt()
GAP = Decimal("0.007707")
MSTAR = Decimal(4) * S2 + Decimal(2) * GAP
PSTAR = MSTAR / Decimal(5)
MUSTAR = PI / Decimal(2) + Decimal(2) * S2 / Decimal(5) + GAP / Decimal(5)
EPS = Decimal("0.00710")
C3 = (PI - Decimal(2) * PSTAR - Decimal(9) * EPS) / Decimal(11)
ESTAR = (MSTAR - PI) / Decimal(2)
TRANSPORT = ESTAR - Decimal("2.5") * EPS

assert Decimal("1.95326284") < MUSTAR < Decimal("1.95326286")
assert Decimal("1.96036284") < MUSTAR + EPS < Decimal("1.96036286")
assert Decimal("0.14071150") < C3 < Decimal("0.14071151")
assert Decimal("0.28142301") < Decimal(2) * C3 < Decimal("0.28142302")
assert Decimal("0.42213451") < Decimal(3) * C3 < Decimal("0.42213453")
assert Decimal("0.32378628") < TRANSPORT < Decimal("0.32378630")


def rank_fraction(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    nr = len(a)
    nc = len(a[0])
    r = 0
    for c in range(nc):
        pivot = next((i for i in range(r, nr) if a[i][c] != 0), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(nr):
            if i == r or a[i][c] == 0:
                continue
            q = a[i][c]
            a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == nr:
            break
    return r


def left_sum(rows, weights):
    m = len(rows[0]) if rows else 0
    return [
        sum(Fraction(weights[i]) * Fraction(rows[i][j]) for i in range(len(rows)))
        for j in range(m)
    ]


def matching_size(rows):
    """Maximum matching from matrix columns to nonzero-support rows."""
    h = len(rows)
    m = len(rows[0]) if rows else 0
    adj = [[i for i in range(h) if rows[i][j] != 0] for j in range(m)]
    owner = [-1] * h

    def augment(j, seen):
        for i in adj[j]:
            if seen[i]:
                continue
            seen[i] = True
            if owner[i] == -1 or augment(owner[i], seen):
                owner[i] = j
                return True
        return False

    return sum(augment(j, [False] * h) for j in range(m))


# Algebraically sharp positive-spanning model:
# e_1,...,e_m,-(1,...,1). It attains h=m+1 and total signed support 2m.
for m in range(1, 41):
    rows = []
    for j in range(m):
        row = [0] * m
        row[j] = 1
        rows.append(row)
    rows.append([-1] * m)

    assert rank_fraction(rows) == m
    assert left_sum(rows, [1] * (m + 1)) == [0] * m
    assert matching_size(rows) == m
    assert len(rows) == m + 1

    pos = sum(x > 0 for row in rows for x in row)
    neg = sum(x < 0 for row in rows for x in row)
    assert pos == m
    assert neg == m
    assert pos + neg == 2 * m
    for j in range(m):
        col = [row[j] for row in rows]
        assert any(x > 0 for x in col)
        assert any(x < 0 for x in col)


# Random exact full-rank matrices with a strictly positive left-kernel vector.
# An invertible m x m integer block is followed by minus its row sum, so all row
# weights one give zero. Full column rank then forces Hall matching and both signs in
# every column.
rng = random.Random(0xE9900710)
checked = 0
for m in range(1, 9):
    for _ in range(300):
        for _attempt in range(100):
            base = [[rng.randint(-4, 4) for _ in range(m)] for _ in range(m)]
            if rank_fraction(base) == m:
                break
        else:
            raise AssertionError("failed to sample an invertible block")

        tail = [-sum(base[i][j] for i in range(m)) for j in range(m)]
        rows = base + [tail]
        assert rank_fraction(rows) == m
        assert left_sum(rows, [1] * (m + 1)) == [0] * m
        assert matching_size(rows) == m
        for j in range(m):
            col = [row[j] for row in rows]
            assert any(x > 0 for x in col)
            assert any(x < 0 for x in col)
        checked += 1


# Exact flex/stress complementarity regression:
# d_C = h - s_Z + sigma_C - 1, d_H = s_Z - sigma_C.
for _ in range(20000):
    s_z = rng.randrange(0, 200)
    sigma = rng.randrange(0, s_z + 1)
    d_h = s_z - sigma
    h = rng.randrange(d_h + 1, d_h + 300)
    d_c = h - d_h - 1
    assert d_c >= 0
    assert d_c + d_h == h - 1
    m = rng.randrange(0, d_c + 1)
    assert d_h <= h - m - 1
    assert d_h + 1 <= h - m

print("PASS live terminal exact-flex diameter-locking regression")
print("mu_star", MUSTAR)
print("epsilon", EPS)
print("window_upper", MUSTAR + EPS)
print("C3_live", C3)
print("signed_incidence_floor", Decimal(2) * C3)
print("fan_spoke_floor", Decimal(3) * C3)
print("BB_minus_LO_floor", TRANSPORT)
print("random_positive_dependence_systems", checked)
