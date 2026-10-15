"""Exact base-point audit for the 2026-09-09 near-chain vertex regressions.

Run: python3 research/nearchain_vertex_regressions.py
Arithmetic: symbolic Q(sqrt(3)), with exact sign comparisons; no floats.
Checks every pair and every triangle in the two explicitly listed patches.
The report proves the positive-parameter families by analytic displacement
bounds and gives positive equilibrium at the distinguished vertex. This script
does NOT certify equilibrium at other vertices, a global KKT stress, a diameter
endpoint, global optimality, or the infinite-cardinality Erdos conjecture.
"""

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations


@dataclass(frozen=True)
class Qsqrt3:
    """An exact element a+b*sqrt(3), with rational a,b."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __add__(self, other):
        other = as_q(other)
        return Qsqrt3(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Qsqrt3(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-as_q(other))

    def __rsub__(self, other):
        return as_q(other) - self

    def __mul__(self, other):
        other = as_q(other)
        return Qsqrt3(self.a * other.a + 3 * self.b * other.b,
                      self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = as_q(other)
        den = other.a * other.a - 3 * other.b * other.b
        assert den != 0
        return self * Qsqrt3(other.a / den, -other.b / den)

    def __pow__(self, exponent):
        assert exponent >= 0
        result = Qsqrt3(1)
        for _ in range(exponent):
            result *= self
        return result

    def __eq__(self, other):
        other = as_q(other)
        return self.a == other.a and self.b == other.b

    def is_nonnegative(self):
        """Certified sign using only rational comparisons."""
        if self.b == 0:
            return self.a >= 0
        if self.a >= 0 and self.b >= 0:
            return True
        if self.a <= 0 and self.b <= 0:
            return False
        # The remaining cases compare |a| with |b|*sqrt(3).
        return 3 * self.b * self.b >= self.a * self.a if self.b > 0 else \
            self.a * self.a >= 3 * self.b * self.b

    def __repr__(self):
        return f"Qsqrt3({self.a!r}, {self.b!r})"


def as_q(value):
    return value if isinstance(value, Qsqrt3) else Qsqrt3(Fraction(value))


Rational = lambda numerator, denominator=1: Qsqrt3(Fraction(numerator, denominator))
sqrt3 = Qsqrt3(b=Fraction(1))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def audit(name, rays, sectors, opening_pairs):
    points = [(0, 0)] + rays
    edges = {tuple(sorted((0, i + 1))) for i in range(len(rays))}
    for i, j in sectors:
        s = len(points)
        points.append(add(rays[i], rays[j]))
        edges.update({tuple(sorted((i + 1, s))), tuple(sorted((j + 1, s)))})
    opening_pairs = {tuple(sorted(pair)) for pair in opening_pairs}
    separated = 0
    for i, j in combinations(range(len(points)), 2):
        squared = sum((x - y) ** 2 for x, y in zip(points[i], points[j]))
        if (i, j) in edges or (i, j) in opening_pairs:
            assert squared == 1, (name, i, j, squared)
        else:
            assert as_q(squared - 2).is_nonnegative(), (name, i, j, squared)
            separated += 1
    for triple in combinations(range(len(points)), 3):
        assert not all(pair in edges for pair in combinations(triple, 2))
    print(f"{name}: {len(points)} points, {len(edges)} permanent unit pairs, "
          f"{len(opening_pairs)} opening pairs, {separated} other pairs with d^2>=2; "
          "permanent graph triangle-free")


def main():
    h = sqrt3 / 2
    audit("degree five", [(1, 0), (Rational(1, 2), h),
                          (-Rational(1, 2), h), (-1, 0), (-Rational(1, 2), -h)],
          [(i, (i + 1) % 5) for i in range(5)],
          [(1, 2), (2, 3), (3, 4), (4, 5), (0, 10)])
    audit("degree three", [(1, 0), (-1, 0), (0, -1)],
          [(1, 2), (2, 0)], [])
    # Pair displacement bounds: 16/100 and 4/100, respectively.
    assert (Rational(29, 25) ** 2).a < 2
    assert (Rational(26, 25) ** 2).a < 2
    print("Exact pair-margin checks passed. Parameter-family proof is in the report.")


if __name__ == "__main__":
    main()
