#!/usr/bin/env python3
"""Exact corroboration of the harmonic cubic-window report (2026-10-02).

Encoded: rational radius/normal-angle margins, conservative bump constants,
fixed-length antipodal interval selection, exponent arithmetic, and complete
square / regular-pentagon-star contact-diameter stress data in Q(sqrt(5)).
Omitted: the general constant-width completion theorem, Sobolev support-energy
proof, harmonic trapping, the canonical ZF/fat-hull/diameter ledgers, source
global optimality, and all other C-II branches. Positive output certifies only
these finite algebraic checks. The report's geometric theorems have analytic
proofs; this program is not a Level I or global-optimality certificate.

Dependency-free. No floating-point arithmetic is used.
"""

from dataclasses import dataclass
from fractions import Fraction as F


@dataclass(frozen=True)
class Q5:
    """a+b*sqrt(5), with exact rational coefficients."""

    a: F = F(0)
    b: F = F(0)

    @staticmethod
    def coerce(x):
        return x if isinstance(x, Q5) else Q5(F(x))

    def __add__(self, other):
        q = self.coerce(other)
        return Q5(self.a + q.a, self.b + q.b)

    __radd__ = __add__

    def __neg__(self):
        return Q5(-self.a, -self.b)

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        q = self.coerce(other)
        return Q5(self.a * q.a + 5 * self.b * q.b,
                  self.a * q.b + self.b * q.a)

    __rmul__ = __mul__

    def __truediv__(self, other):
        q = self.coerce(other)
        denominator = q.a * q.a - 5 * q.b * q.b
        assert denominator
        return self * Q5(q.a / denominator, -q.b / denominator)

    def __bool__(self):
        return bool(self.a or self.b)


ZERO = Q5()


def matrix_rank(matrix):
    rows = [[Q5.coerce(x) for x in row] for row in matrix]
    rank = 0
    for col in range(len(rows[0])):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        value = rows[rank][col]
        rows[rank] = [x / value for x in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][col]:
                value = rows[i][col]
                rows[i] = [x - value * y for x, y in zip(rows[i], rows[rank])]
        rank += 1
    return rank


def stress_matrix(size, contacts, diameters):
    matrix = [[ZERO for _ in range(size)] for _ in range(size)]
    for edges, sign in ((contacts, 1), (diameters, -1)):
        for i, j, weight in edges:
            value = sign * weight
            matrix[i][i] += value
            matrix[j][j] += value
            matrix[i][j] -= value
            matrix[j][i] -= value
    return matrix


def check_equilibrium(matrix, gram):
    size = len(matrix)
    assert all(sum(row, ZERO) == ZERO for row in matrix)
    for i in range(size):
        for j in range(size):
            assert sum((matrix[i][k] * gram[k][j] for k in range(size)), ZERO) == ZERO


def check_constants():
    # 3^(1/4)<4/3; safe radius fraction at D>=4096.
    assert F(4, 3) ** 4 > 3
    assert F(1, 2) + F(4, 3 * 64) == F(25, 48)
    assert F(48 * 3, 2 * 23 * 4096) < F(1, 1000)
    # For L<=sqrt(D)/100 and D>=65536:
    assert F(48, 200 * 23 * 256) < F(1, 1000)
    normal_cosine = F(23, 25) * F(999, 1000) - F(10, 25) * F(1, 1000)
    assert normal_cosine == F(22967, 25000)
    assert 4 * normal_cosine ** 2 > 3
    assert 1 - F(1, 1000) ** 2 > F(999, 1000) ** 2
    assert F(10, 25) ** 2 > 1 - F(23, 25) ** 2

    # Secant upper bound obtained using cos(a)>=1-a^2/2.
    for length in range(2, 1003):
        a = F(1, 8 * length)
        assert a <= F(1, 16)
        assert (a * a / 2) / (1 - a * a / 2) <= a * a
        diameter = 10000 * length * length
        k_lower = a ** 3 / 3
        assert 4 * length * a * a <= diameter * k_lower
        assert diameter ** 2 * k_lower / 8 == F(diameter ** 2, 12288 * length ** 3)
    assert 267 * 9216 == 2460672
    assert 800 * 9216 == 7372800
    # Comparable-diameter attachment load yields constant clustering.
    for m in range(1, 10002):
        length = 2 * m + 2
        assert F(3 * (132 * length + 1), m + 3) < 800
    # pi>3 and sqrt(3)>17/10 prove C0>25^3.
    assert F(17, 10) ** 2 < 3
    assert 3072 * 3 * F(17, 10) > 25 ** 3
    assert 65536 > 4 ** 6

    # D=t^5 and M=t^2: each term has leading order t^3=D^(3/5).
    for t in (10201, 20000, 100000, 1000000):
        diameter = t ** 5
        m = t ** 2
        assert (m + 2) ** 2 * 10000 <= diameter
        assert F(m ** 4, diameter) == t ** 3
        assert F(diameter, m) == t ** 3
    # Final square-root summation. D=(400*2^J)^2 gives the endpoint
    # cutoff exactly; the small bands use the geometric cube sum.
    for j in range(1, 31):
        root = 400 * 2 ** j
        diameter = root ** 2
        assert diameter >= 262144
        for k in range(j + 1):
            m = 2 ** k
            assert 2 * m + 2 <= F(root, 100)
        geometric_sum = sum(2 ** (3 * k) for k in range(j + 1))
        assert geometric_sum < F(8, 7) * 2 ** (3 * j)
        assert F(64 * geometric_sum, diameter) < F(512 * root, 7 * 400 ** 3)
        assert 2 ** (j + 1) > F(root, 400)
    return normal_cosine


def circle_distance(x, y, period=12):
    delta = (x - y) % period
    return min(delta, period - delta)


def check_antipodal_selection():
    # Exhaust all start subsets on a circle of circumference 12, intervals
    # of length 2. Endpoint-only intersections have zero measure.
    cases = 0
    for mask in range(1, 1 << 12):
        starts = [i for i in range(12) if mask & (1 << i)]
        if any(circle_distance(x, y) < 2
               for i, x in enumerate(starts) for y in starts[i + 1:]):
            continue
        graph = {x: {y for y in starts if y != x and
                     circle_distance(x, (y + 6) % 12) < 2}
                 for x in starts}
        assert all(len(neighbors) <= 2 for neighbors in graph.values())
        assert all(x in graph[y] for x in starts for y in graph[x])
        remaining = set(starts)
        kept = []
        while remaining:
            x = min(remaining)
            kept.append(x)
            remaining.discard(x)
            remaining.difference_update(graph[x])
        assert 3 * len(kept) >= len(starts)
        for i, x in enumerate(kept):
            for y in kept[i + 1:]:
                assert circle_distance(x, y) >= 2
                assert circle_distance(x, (y + 6) % 12) >= 2
        cases += 1
    return cases


def check_regressions():
    # Square, centered at zero, in cyclic order.
    gram = [[Q5(F(1, 2) if i == j else
                 -F(1, 2) if (i - j) % 4 == 2 else F(0))
             for j in range(4)] for i in range(4)]
    contacts = [(i, (i + 1) % 4, Q5(F(1, 2))) for i in range(4)]
    diameters = [(0, 2, Q5(F(1, 2))), (1, 3, Q5(F(1, 2)))]
    omega = stress_matrix(4, contacts, diameters)
    check_equilibrium(omega, gram)
    assert matrix_rank(omega) == 1
    assert sum((w for _, _, w in contacts), ZERO) == Q5(2)
    assert sum((w for _, _, w in diameters), ZERO) == Q5(1)

    # Pentagon plus its center. Vertex 5 is the center. Outer Gram matrix
    # uses cos(72 degrees) and cos(144 degrees), avoiding sine radicals.
    cosine = {0: Q5(1), 1: Q5(F(-1, 4), F(1, 4)),
              2: Q5(F(-1, 4), F(-1, 4))}
    gram = [[ZERO for _ in range(6)] for _ in range(6)]
    for i in range(5):
        for j in range(5):
            delta = (i - j) % 5
            gram[i][j] = cosine[min(delta, 5 - delta)]
    d_squared = Q5(F(5, 2), F(1, 2))
    short_squared = Q5(F(5, 2), F(-1, 2))
    assert 2 - 2 * cosine[1] == short_squared
    assert 2 - 2 * cosine[2] == d_squared
    assert 2 ** 2 < 5 < 3 ** 2  # 2<sqrt(5)<3: short^2>1, D^2<4.
    contacts = [(5, i, d_squared / 5) for i in range(5)]
    diameters = [(i, (i + 2) % 5, Q5(F(1, 5))) for i in range(5)]
    omega = stress_matrix(6, contacts, diameters)
    check_equilibrium(omega, gram)
    assert matrix_rank(omega) == 3
    assert sum((w for _, _, w in contacts), ZERO) == d_squared
    assert sum((w for _, _, w in diameters), ZERO) == Q5(1)
    # Analytic Schur/Fourier eigenvalues: translation/coordinates zero,
    # the two remaining outer modes positive sqrt(5)/5. Center pivot D^2>0.
    nonaffine_eigenvalue = (d_squared - short_squared) / 5
    assert nonaffine_eigenvalue == Q5(F(0), F(1, 5))

    # Regular unit pentagon: c_I=0, whereas two disjoint actual diameter
    # edges form a selected forest with two nontrivial components.
    radius_squared = Q5(1) / short_squared
    gram = [[radius_squared * cosine[min((i - j) % 5, (j - i) % 5)]
             for j in range(5)] for i in range(5)]
    actual_diameter_squared = d_squared / short_squared
    assert actual_diameter_squared == Q5(F(3, 2), F(1, 2))
    contacts = [(i, (i + 1) % 5, actual_diameter_squared / 5) for i in range(5)]
    diameters = [(i, (i + 2) % 5, Q5(F(1, 5))) for i in range(5)]
    omega = stress_matrix(5, contacts, diameters)
    check_equilibrium(omega, gram)
    assert matrix_rank(omega) == 2
    assert sum((w for _, _, w in contacts), ZERO) == actual_diameter_squared
    forest = [(0, 2), (1, 3)]
    assert all((j - i) % 5 == 2 for i, j in forest)
    assert len({v for edge in forest for v in edge}) == 4
    return 3


def main():
    margin = check_constants()
    intervals = check_antipodal_selection()
    regressions = check_regressions()
    print(f"PASS: normal cosine {margin}; 1001 bump scales; "
          f"10001 dyadic capacities; 30 square-root sums; "
          f"{intervals} antipodal interval families; {regressions} exact stress sources")
    print("Scope: finite arithmetic corroboration; no global-optimality or Level I certificate")


if __name__ == "__main__":
    main()
