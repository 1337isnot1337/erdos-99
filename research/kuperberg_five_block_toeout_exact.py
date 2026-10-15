#!/usr/bin/env python3
"""Exact truncated-series audit for the toe-out Kuperberg five-block variant.

Mathematical statement tested
-----------------------------
In the paper normalization (nearest-neighbor center distance 2), use the same
five-block partition as `kuperberg_five_block_exact.py`, but translate the blocks by

    B1 = (-a,-b),  B2 = (-c,-e),  B3 = (0,v),
    B4 = ( c,-e),  B5 = ( a,-b).

The promoted Section 160 proof defines a,b,c,e,v analytically by five exact active
contact equations.  This script substitutes the claimed Taylor series through order
d^5 and, in exact Q(sqrt(3)) arithmetic, checks every nearest-neighbor contact crossing
a moved/moved or moved/fixed boundary.  It verifies:

* the five defining active-contact families vanish through order d^5;
* every other cross-boundary nearest-neighbor margin has a strictly positive leading
  coefficient;
* the middle-block lift is
      v = (sqrt(3)/9)d^4 - (2/9)d^5 + O(d^6).

The script verifies finite interface algebra only.  It does not prove the implicit-
function existence theorem, non-neighbor clearance, recursive containment, exterior
compatibility in a Target A monomer domain, or global minimum-diameter optimality.

Arithmetic is exact and uses only the Python standard library.

Run:
    python3 research/kuperberg_five_block_toeout_exact.py
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, Tuple

ORDER = 5


@dataclass(frozen=True)
class Surd:
    """a + b*sqrt(3), with rational a,b."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    @staticmethod
    def coerce(value: object) -> "Surd":
        if isinstance(value, Surd):
            return value
        return Surd(Fraction(value), Fraction(0))

    def __add__(self, other: object) -> "Surd":
        other = Surd.coerce(other)
        return Surd(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self) -> "Surd":
        return Surd(-self.a, -self.b)

    def __sub__(self, other: object) -> "Surd":
        return self + (-Surd.coerce(other))

    def __rsub__(self, other: object) -> "Surd":
        return Surd.coerce(other) - self

    def __mul__(self, other: object) -> "Surd":
        other = Surd.coerce(other)
        return Surd(
            self.a * other.a + 3 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> "Surd":
        q = Fraction(other)
        return Surd(self.a / q, self.b / q)

    def __bool__(self) -> bool:
        return self.a != 0 or self.b != 0

    def is_manifestly_positive(self) -> bool:
        # This is enough for every leading coefficient produced below.
        return self.a >= 0 and self.b >= 0 and bool(self)


SQRT3 = Surd(Fraction(0), Fraction(1))


class Series:
    """Truncated power series in d with coefficients in Q(sqrt(3))."""

    def __init__(self, coeffs: Dict[int, object] | None = None):
        data = [Surd() for _ in range(ORDER + 1)]
        for degree, value in (coeffs or {}).items():
            if not 0 <= degree <= ORDER:
                raise ValueError("degree outside truncation order")
            data[degree] = Surd.coerce(value)
        self.coeffs = tuple(data)

    @staticmethod
    def const(value: object) -> "Series":
        return Series({0: value})

    @staticmethod
    def variable() -> "Series":
        return Series({1: 1})

    def __add__(self, other: object) -> "Series":
        if not isinstance(other, Series):
            other = Series.const(other)
        return Series(
            {k: self.coeffs[k] + other.coeffs[k] for k in range(ORDER + 1)}
        )

    __radd__ = __add__

    def __neg__(self) -> "Series":
        return Series({k: -self.coeffs[k] for k in range(ORDER + 1)})

    def __sub__(self, other: object) -> "Series":
        if not isinstance(other, Series):
            other = Series.const(other)
        return self + (-other)

    def __rsub__(self, other: object) -> "Series":
        return Series.const(other) - self

    def __mul__(self, other: object) -> "Series":
        if not isinstance(other, Series):
            other = Series.const(other)
        out = {k: Surd() for k in range(ORDER + 1)}
        for i in range(ORDER + 1):
            for j in range(ORDER + 1 - i):
                out[i + j] = out[i + j] + self.coeffs[i] * other.coeffs[j]
        return Series(out)

    __rmul__ = __mul__

    def key(self) -> tuple:
        return tuple((c.a, c.b) for c in self.coeffs)

    def leading_term(self) -> tuple[int, Surd] | None:
        for degree, coefficient in enumerate(self.coeffs):
            if coefficient:
                return degree, coefficient
        return None


D = Series.variable()
A = Series(
    {
        2: Fraction(1, 4),
        3: -SQRT3 / 24,
        4: Fraction(1, 24),
        5: -SQRT3 / 144,
    }
)
B = Series(
    {
        1: 1,
        2: -SQRT3 / 12,
        3: Fraction(1, 24),
        5: Fraction(-1, 144),
    }
)
C = Series(
    {
        2: Fraction(1, 2),
        3: -SQRT3 / 6,
        4: Fraction(5, 24),
        5: -SQRT3 / 18,
    }
)
E = Series(
    {
        2: SQRT3 / 6,
        3: Fraction(-1, 6),
        4: SQRT3 / 72,
        5: Fraction(1, 18),
    }
)
V = Series(
    {
        4: SQRT3 / 9,
        5: Fraction(-2, 9),
    }
)

ZERO = Series.const(0)
TRANSLATIONS = {
    1: (-A, -B),
    2: (-C, -E),
    3: (ZERO, V),
    4: (C, -E),
    5: (A, -B),
    "U": (ZERO, ZERO),
    "L": (ZERO, ZERO),
}


def five_blocks(n: int) -> Dict[Tuple[int, int], int]:
    if n < 3:
        raise ValueError("n must be at least 3")
    a = n - 1
    blocks: Dict[Tuple[int, int], int] = {}
    for j in range(a + 1):
        for i in range(0, a - j + 1):
            blocks[(i, j)] = 1
        for i in range(a + 1 - j, a + 2):
            blocks[(i, j)] = 2
        if j <= a - 1:
            for i in range(a + 2, 2 * a + 2 - j):
                blocks[(i, j)] = 3
        for i in range(2 * a + 2 - j, 2 * a + 3):
            blocks[(i, j)] = 4
        for i in range(2 * a + 3, 3 * a + 4 - j):
            blocks[(i, j)] = 5
    return blocks


def position(
    index: Tuple[int, int], label: int | str
) -> Tuple[Series, Series]:
    i, j = index
    x = Series.const(2 * i + j)
    y = Series.const(SQRT3 * j)
    if j >= 0:
        y = y + D
    tx, ty = TRANSLATIONS[label]
    return x + tx, y + ty


def squared_margin(
    p: Tuple[int, int],
    p_label: int | str,
    q: Tuple[int, int],
    q_label: int | str,
) -> Series:
    px, py = position(p, p_label)
    qx, qy = position(q, q_label)
    dx, dy = px - qx, py - qy
    return dx * dx + dy * dy - 4


def enumerate_margin_series(n: int = 6) -> Dict[tuple, int]:
    blocks = five_blocks(n)
    neighbors = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
    seen = set()
    margins: Dict[tuple, int] = {}

    for p, p_label in blocks.items():
        for di, dj in neighbors:
            q = (p[0] + di, p[1] + dj)
            edge_key = tuple(sorted((p, q)))
            if edge_key in seen:
                continue
            seen.add(edge_key)

            if q in blocks:
                q_label: int | str = blocks[q]
            else:
                q_label = "U" if q[1] >= 0 else "L"

            if p_label == q_label:
                continue

            margin = squared_margin(p, p_label, q, q_label)
            margins[margin.key()] = margins.get(margin.key(), 0) + 1

    return margins


def main() -> None:
    assert V.coeffs[4] == SQRT3 / 9
    assert V.coeffs[5] == Surd(Fraction(-2, 9), Fraction(0))

    for n in (3, 4, 6, 10):
        margins = enumerate_margin_series(n)
        # Five active polynomial families coalesce to the zero truncated series.
        # The remaining ten polynomial families stay distinct after substitution.
        assert len(margins) == 11, (n, len(margins))

        zero_key = ZERO.key()
        assert zero_key in margins

        positive_families = 0
        for key in margins:
            if key == zero_key:
                continue
            series = Series(
                {
                    k: Surd(Fraction(a), Fraction(b))
                    for k, (a, b) in enumerate(key)
                }
            )
            leading = series.leading_term()
            assert leading is not None
            degree, coefficient = leading
            assert degree in (1, 2), (n, degree, coefficient)
            assert coefficient.is_manifestly_positive(), (n, degree, coefficient)
            positive_families += 1

        assert positive_families == 10

    print("Toe-out Kuperberg five-block exact series audit: PASS")
    print("Checked n = 3, 4, 6, 10")
    print("Five active contact families vanish through d^5")
    print("Ten remaining margin families have positive leading coefficient")
    print("v = (sqrt(3)/9)d^4 - (2/9)d^5 + O(d^6)")


if __name__ == "__main__":
    main()
