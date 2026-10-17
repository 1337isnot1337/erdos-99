#!/usr/bin/env python3
"""Exact ground-only 3+4 sign-pattern classification for support seven.

The script proves two finite classifications for seven strictly ordered unit rays
u_1,...,u_7 with minority sign class P of size three and signed equilibrium

    sum_{i in P} u_i = sum_{i not in P} u_i.

1. If the seven rays lie in an open semicircle, exactly 21 of the 35 minority
   index patterns are possible.
2. If their total angular width is < 2*pi/3 (the H6 ground bound), exactly 13
   patterns are possible.

The impossibility side rechecks the existing pivot/matching and H6 bisector
certificates. The realizability side gives exact witnesses, using rational
half-angle points and one quadratic extension Q(sqrt(q)) per witness.

No floating point is used.
"""

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations, permutations

I = tuple(range(1, 8))
ALL = {frozenset(c) for c in combinations(I, 3)}


def key(P):
    return "".join(str(i) for i in sorted(P))


# ---------------------------------------------------------------------------
# Existing impossibility mechanisms.
# ---------------------------------------------------------------------------

def has_pairing_certificate(P):
    P = frozenset(P)
    M = frozenset(I) - P
    for pivot in M:
        rest = tuple(sorted(M - {pivot}))
        for perm in permutations(sorted(P)):
            if all((pivot < m < n) or (n < m < pivot)
                   for m, n in zip(rest, perm)):
                return True
    return False


def max_interior_block_excess(P):
    P = frozenset(P)
    s = {i: (1 if i in P else -1) for i in I}
    vals = []
    for a in range(2, 7):
        total = 0
        for b in range(a, 7):
            total += s[b]
            vals.append(total)
    return max(vals)


PAIRING_BAD = {P for P in ALL if has_pairing_certificate(P)}
BISECTOR_BAD = {P for P in ALL if max_interior_block_excess(P) <= 1}
H6_BAD = PAIRING_BAD | BISECTOR_BAD
SEMICIRCLE_GOOD = ALL - PAIRING_BAD
H6_GOOD = ALL - H6_BAD

assert {key(P) for P in PAIRING_BAD} == {
    "123", "124", "125", "127", "134", "135", "137",
    "157", "167", "357", "367", "457", "467", "567",
}
assert len(PAIRING_BAD) == 14
assert len(BISECTOR_BAD) == 18
assert len(PAIRING_BAD & BISECTOR_BAD) == 10
assert {key(P) for P in BISECTOR_BAD - PAIRING_BAD} == {
    "126", "136", "146", "147", "246", "247", "257", "267",
}
assert {key(P) for P in H6_GOOD} == {
    "145", "156", "234", "235", "236", "237", "245",
    "256", "345", "346", "347", "356", "456",
}
assert len(SEMICIRCLE_GOOD) == 21
assert len(H6_GOOD) == 13


# ---------------------------------------------------------------------------
# Exact arithmetic in Q(sqrt(q)), q>0 rational.
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class QS:
    a: Q
    b: Q
    q: Q

    def _coerce(self, other):
        if isinstance(other, QS):
            assert other.q == self.q
            return other
        return QS(Q(other), Q(0), self.q)

    def __add__(self, other):
        other = self._coerce(other)
        return QS(self.a + other.a, self.b + other.b, self.q)

    __radd__ = __add__

    def __neg__(self):
        return QS(-self.a, -self.b, self.q)

    def __sub__(self, other):
        return self + (-self._coerce(other))

    def __rsub__(self, other):
        return self._coerce(other) - self

    def __mul__(self, other):
        other = self._coerce(other)
        return QS(
            self.a * other.a + self.b * other.b * self.q,
            self.a * other.b + self.b * other.a,
            self.q,
        )

    __rmul__ = __mul__

    def __eq__(self, other):
        try:
            other = self._coerce(other)
        except (AssertionError, TypeError, ValueError):
            return False
        return self.a == other.a and self.b == other.b

    def sign(self):
        """Exact sign of a+b*sqrt(q)."""
        assert self.q > 0
        a, b, q = self.a, self.b, self.q
        if b == 0:
            return (a > 0) - (a < 0)
        if a == 0:
            return (b > 0) - (b < 0)
        sa = (a > 0) - (a < 0)
        sb = (b > 0) - (b < 0)
        if sa == sb:
            return sa
        cmp = a * a - b * b * q
        if cmp == 0:
            return 0
        return sa if cmp > 0 else sb


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1]


def cross(u, v):
    return u[0] * v[1] - u[1] * v[0]


def rational_unit(t):
    """Unit vector at canonical angle theta=2*atan(t), t rational."""
    t = Q(t)
    den = 1 + t * t
    return ((1 - t * t) / den, 2 * t / den)


# Each row gives:
#   pattern P (the +1 minority class),
#   two same-sign positions whose unit vectors are solved exactly,
#   rational half-angle parameters t_i at the other five positions.
# Positions are 1-based.
#
# The first 13 witnesses satisfy width < 2*pi/3. The final eight satisfy
# width < pi but (for these chosen witnesses) width > 2*pi/3.
WITNESSES = {
    "145": ((2, 6), {1: Q(-5, 9), 3: Q(-1, 2), 4: Q(1, 8), 5: Q(3, 8), 7: Q(4, 7)}),
    "156": ((4, 7), {1: Q(1, 7), 2: Q(1, 6), 3: Q(1, 5), 5: Q(2, 5), 6: Q(2, 3)}),
    "234": ((2, 3), {1: Q(-2, 9), 4: Q(4, 7), 5: Q(2, 3), 6: Q(3, 4), 7: Q(6, 7)}),
    "235": ((1, 6), {2: Q(-7, 9), 3: Q(-2, 3), 4: Q(-4, 7), 5: Q(-1, 2), 7: Q(-3, 10)}),
    "236": ((1, 4), {2: Q(5, 8), 3: Q(7, 9), 5: Q(7, 6), 6: Q(9, 7), 7: Q(13, 9)}),
    "237": ((4, 6), {1: Q(-1, 3), 2: Q(2, 7), 3: Q(4, 9), 5: Q(5, 7), 7: Q(4, 5)}),
    "245": ((3, 6), {1: Q(-1, 9), 2: Q(1, 3), 4: Q(5, 8), 5: Q(3, 4), 7: Q(6, 5)}),
    "256": ((2, 6), {1: Q(-11, 9), 3: Q(-1), 4: Q(-6, 7), 5: Q(-5, 8), 7: Q(1, 8)}),
    "345": ((2, 7), {1: Q(-13, 9), 3: Q(-7, 9), 4: Q(-3, 5), 5: Q(-4, 9), 6: Q(-2, 7)}),
    "346": ((2, 7), {1: Q(3, 7), 3: Q(7, 10), 4: Q(6, 7), 5: Q(7, 6), 6: Q(11, 8)}),
    "347": ((1, 2), {3: Q(1, 7), 4: Q(2, 9), 5: Q(7, 6), 6: Q(11, 9), 7: Q(9, 7)}),
    "356": ((2, 7), {1: Q(-8, 7), 3: Q(-8, 9), 4: Q(-2, 3), 5: Q(-4, 7), 6: Q(-1, 2)}),
    "456": ((2, 7), {1: Q(3, 5), 3: Q(4, 5), 4: Q(8, 9), 5: Q(1), 6: Q(11, 10)}),

    "126": ((3, 5), {1: Q(-11, 9), 2: Q(-10, 9), 4: Q(-6, 7), 6: Q(0), 7: Q(3, 4)}),
    "136": ((1, 6), {2: Q(-2, 3), 3: Q(-4, 7), 4: Q(-1, 2), 5: Q(-2, 5), 7: Q(1)}),
    "146": ((3, 5), {1: Q(-8, 9), 2: Q(-5, 7), 4: Q(0), 6: Q(3, 10), 7: Q(9, 10)}),
    "147": ((1, 4), {2: Q(-8, 7), 3: Q(-1), 5: Q(4, 9), 6: Q(4, 7), 7: Q(2, 3)}),
    "246": ((2, 4), {1: Q(-5, 6), 3: Q(-2, 9), 5: Q(2, 9), 6: Q(4, 9), 7: Q(5, 7)}),
    "247": ((4, 7), {1: Q(-10, 9), 2: Q(-1, 3), 3: Q(-1, 10), 5: Q(2, 5), 6: Q(4, 7)}),
    "257": ((2, 5), {1: Q(-2, 3), 3: Q(2, 3), 4: Q(9, 10), 6: Q(7, 6), 7: Q(4, 3)}),
    "267": ((2, 7), {1: Q(-7, 8), 3: Q(4, 7), 4: Q(3, 4), 5: Q(5, 6), 6: Q(7, 8)}),
}

assert set(WITNESSES) == {key(P) for P in SEMICIRCLE_GOOD}


def solve_pair(pattern, pair, fixed_t, require_h6_width):
    P = {int(ch) for ch in pattern}
    s = {i: (1 if i in P else -1) for i in I}
    a, b = pair
    assert a < b and s[a] == s[b]
    sigma = s[a]
    assert set(fixed_t) == set(I) - {a, b}

    fixed = {i: rational_unit(t) for i, t in fixed_t.items()}
    sx = sum(Q(s[i]) * fixed[i][0] for i in fixed)
    sy = sum(Q(s[i]) * fixed[i][1] for i in fixed)
    R = (-sx / sigma, -sy / sigma)
    r2 = R[0] * R[0] + R[1] * R[1]
    assert 0 < r2 < 4

    q = (Q(4) - r2) / r2
    assert q > 0

    # If J(x,y)=(-y,x), the two unit vectors whose sum is R are
    # R/2 +/- sqrt(q) J R / 2.
    rx, ry = R
    plus = (
        QS(rx / 2, -ry / 2, q),
        QS(ry / 2,  rx / 2, q),
    )
    minus = (
        QS(rx / 2,  ry / 2, q),
        QS(ry / 2, -rx / 2, q),
    )

    def promote(u):
        return (QS(u[0], Q(0), q), QS(u[1], Q(0), q))

    # Exact comparison of canonical half-angle coordinates t=y/(1+x).
    def half_angle_order(u, v):
        # positive iff t(v)-t(u)>0, once both 1+x denominators are positive
        return (v[1] * (1 + u[0]) - u[1] * (1 + v[0])).sign()

    if half_angle_order(plus, minus) > 0:
        lower, upper = plus, minus
    else:
        lower, upper = minus, plus

    vec = {i: promote(u) for i, u in fixed.items()}
    vec[a], vec[b] = lower, upper

    # Unit length and canonical chart (-pi,pi).
    for i in I:
        assert dot(vec[i], vec[i]) == 1
        assert (1 + vec[i][0]).sign() > 0

    # Exact signed equilibrium.
    zero = QS(Q(0), Q(0), q)
    ex = zero
    ey = zero
    for i in I:
        ex += s[i] * vec[i][0]
        ey += s[i] * vec[i][1]
    assert ex == 0 and ey == 0

    # Strict linear angular order theta_1<...<theta_7.
    for i in range(1, 7):
        assert half_angle_order(vec[i], vec[i + 1]) > 0

    # The endpoint cross sign proves total width in (0,pi).
    assert cross(vec[1], vec[7]).sign() > 0

    width120 = (dot(vec[1], vec[7]) + Q(1, 2)).sign()
    if require_h6_width:
        # In a (0,pi) span, dot>-1/2 is exactly width<2*pi/3.
        assert width120 > 0
    else:
        # These eight witnesses deliberately sit outside the H6 width regime.
        assert width120 < 0

    return q


RADICANDS = {}
for pattern, (pair, fixed_t) in sorted(WITNESSES.items()):
    RADICANDS[pattern] = solve_pair(
        pattern,
        pair,
        fixed_t,
        require_h6_width=(pattern in {key(P) for P in H6_GOOD}),
    )

assert len(RADICANDS) == 21

print("support-seven ground sign classification: PASS")
print("open-semicircle impossible:", len(PAIRING_BAD))
print("open-semicircle realizable:", len(SEMICIRCLE_GOOD))
print("H6-width impossible:", len(H6_BAD))
print("H6-width realizable:", len(H6_GOOD))
print("H6 patterns:", " ".join(sorted(key(P) for P in H6_GOOD)))
