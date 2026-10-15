#!/usr/bin/env python3
"""Exact verifier for the Kuperberg five-block gap-widening calculation.

Mathematical statement tested
-----------------------------
This script reconstructs the five triangular blocks in Kuperberg--Kuperberg--
Kuperberg, Section 2.1, in the radius-one / center-distance-two triangular lattice.
After the outer Delta_n blocks move down by the full original gap d, it enumerates
every nearest-neighbor contact crossing a block boundary or the moved/fixed boundary.
Using exact arithmetic in Q(sqrt(3))[d,u,v], it verifies that the complete set of
nonconstant squared-distance margins |p-q|^2-4 is exactly the 12-polynomial list in
`docs/reports/exact_kuperberg_five_block_rate_2026-08-30.md`.

In particular the only controlling margins are

    F_d(u) = u^2 - (2 sqrt(3) + d) u + d^2
    G_u(v) = v^2 - (2 sqrt(3) - u) v + u^2.

The report then solves their small roots exactly and derives the quartic gap gain.
This script verifies the finite contact enumeration, not the analytic root expansion.

Assumptions encoded
-------------------
* the aligned gap geometry and five-block arrangement of Section 2.1;
* the three rigid translation directions shown in Figures 3--4;
* nearest-neighbor lattice contacts, which are the only possible active constraints
  for sufficiently small d (the report separately bounds non-neighbor pairs).

Not encoded / not proved by this script
---------------------------------------
* global optimality of any finite packing;
* exterior compatibility in an Erdős-99 source/scaffold monomer domain;
* optimality of the Kuperberg rearrangement among all possible finite moves;
* the repeated-block support-radius theorem (proved geometrically in the report).

Arithmetic is exact.  No third-party packages are required.

Reproduce
---------
    python3 research/kuperberg_five_block_exact.py
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, Iterable, Tuple


@dataclass(frozen=True)
class Surd:
    """Element a + b*sqrt(3), with exact rational a,b."""

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
        if isinstance(other, Surd):
            den = other.a * other.a - 3 * other.b * other.b
            return Surd(
                (self.a * other.a - 3 * self.b * other.b) / den,
                (self.b * other.a - self.a * other.b) / den,
            )
        q = Fraction(other)
        return Surd(self.a / q, self.b / q)

    def __bool__(self) -> bool:
        return self.a != 0 or self.b != 0


Exponent = Tuple[int, int, int]  # powers of (d,u,v)


class Poly:
    """Sparse polynomial in d,u,v with coefficients in Q(sqrt(3))."""

    def __init__(self, terms: Dict[Exponent, Surd] | None = None):
        self.terms = {e: c for e, c in (terms or {}).items() if c}

    @staticmethod
    def const(value: object) -> "Poly":
        c = Surd.coerce(value)
        return Poly({(0, 0, 0): c} if c else {})

    @staticmethod
    def var(index: int) -> "Poly":
        exponent = [0, 0, 0]
        exponent[index] = 1
        return Poly({tuple(exponent): Surd(Fraction(1), Fraction(0))})

    def __add__(self, other: object) -> "Poly":
        if not isinstance(other, Poly):
            other = Poly.const(other)
        out = dict(self.terms)
        for exponent, coefficient in other.terms.items():
            out[exponent] = out.get(exponent, Surd()) + coefficient
            if not out[exponent]:
                del out[exponent]
        return Poly(out)

    __radd__ = __add__

    def __neg__(self) -> "Poly":
        return Poly({e: -c for e, c in self.terms.items()})

    def __sub__(self, other: object) -> "Poly":
        if not isinstance(other, Poly):
            other = Poly.const(other)
        return self + (-other)

    def __rsub__(self, other: object) -> "Poly":
        return Poly.const(other) - self

    def __mul__(self, other: object) -> "Poly":
        if not isinstance(other, Poly):
            other = Poly.const(other)
        out: Dict[Exponent, Surd] = {}
        for e, c in self.terms.items():
            for f, k in other.terms.items():
                exponent = tuple(e[i] + f[i] for i in range(3))
                out[exponent] = out.get(exponent, Surd()) + c * k
        return Poly(out)

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> "Poly":
        return Poly({e: c / other for e, c in self.terms.items()})

    def key(self) -> tuple:
        return tuple(sorted((e, c.a, c.b) for e, c in self.terms.items()))


D = Poly.var(0)
U = Poly.var(1)
V = Poly.var(2)
SQRT3 = Surd(Fraction(0), Fraction(1))

TRANSLATIONS = {
    1: (Poly.const(0), -D),
    2: (-(U * SQRT3) / 2, -U / 2),
    3: (Poly.const(0), V),
    4: ((U * SQRT3) / 2, -U / 2),
    5: (Poly.const(0), -D),
}


def five_blocks(n: int) -> Dict[Tuple[int, int], int]:
    """Return the exact lattice-index partition B1,...,B5."""
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


def position(index: Tuple[int, int], label: int | str) -> Tuple[Poly, Poly]:
    i, j = index
    x = Poly.const(2 * i + j)
    y = Poly.const(Surd(Fraction(0), Fraction(j)))
    if j >= 0:
        y = y + D
    if isinstance(label, int):
        tx, ty = TRANSLATIONS[label]
        x, y = x + tx, y + ty
    return x, y


def squared_margin(
    p: Tuple[int, int], p_label: int | str,
    q: Tuple[int, int], q_label: int | str,
) -> Poly:
    px, py = position(p, p_label)
    qx, qy = position(q, q_label)
    dx, dy = qx - px, qy - py
    return dx * dx + dy * dy - 4


def enumerate_cross_margin_keys(n: int = 6) -> set[tuple]:
    """Enumerate all nearest-neighbor margins crossing a block/fixed boundary."""
    blocks = five_blocks(n)
    neighbors = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
    seen = set()
    margins = set()

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

            if q_label == p_label:
                continue
            margins.add(squared_margin(p, p_label, q, q_label).key())

    return margins


def expected_margin_keys() -> set[tuple]:
    two_r3 = Poly.const(2 * SQRT3)
    four_r3 = Poly.const(4 * SQRT3)
    f = U * U - (D + two_r3) * U + D * D
    g = V * V - (two_r3 - U) * V + U * U
    expected = [
        D * (D + two_r3),
        D * D,
        Poly.const(0),
        f,
        f + two_r3 * D,
        U * U + U * V + two_r3 * U + V * V,
        D * D - D * U + two_r3 * D + U * U,
        g,
        (D + V) * (D + V + two_r3),
        U * (U + two_r3),
        U * U,
        U * (3 * U + four_r3),
    ]
    return {p.key() for p in expected}


def block_size_counts(n: int) -> Dict[int, int]:
    blocks = five_blocks(n)
    return {label: sum(v == label for v in blocks.values()) for label in range(1, 6)}


def main() -> None:
    for n in (3, 4, 6, 10):
        expected_counts = {
            1: n * (n + 1) // 2,
            2: n * (n + 1) // 2,
            3: n * (n - 1) // 2,
            4: n * (n + 1) // 2,
            5: n * (n + 1) // 2,
        }
        actual_counts = block_size_counts(n)
        assert actual_counts == expected_counts, (n, actual_counts, expected_counts)

        actual = enumerate_cross_margin_keys(n)
        expected = expected_margin_keys()
        assert actual == expected, (
            f"constraint set mismatch for n={n}",
            "missing", expected - actual,
            "extra", actual - expected,
        )

    print("Kuperberg five-block exact audit: PASS")
    print("Checked n = 3, 4, 6, 10")
    print("Distinct cross-boundary nearest-neighbor margins: 12")
    print("Controlling polynomials:")
    print("  F_d(u) = u^2 - (2*sqrt(3)+d)u + d^2")
    print("  G_u(v) = v^2 - (2*sqrt(3)-u)v + u^2")
    print("See docs/reports/exact_kuperberg_five_block_rate_2026-08-30.md")


if __name__ == "__main__":
    main()
