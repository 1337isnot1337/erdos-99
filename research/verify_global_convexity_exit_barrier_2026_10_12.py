#!/usr/bin/env python3
"""Certify a dense odd-rim trap and an independent strict-D replacement.

All arithmetic uses integer outward-rounded intervals or exact Fractions.
The unbounded construction and the barrier for all continuous motions are proved
in the associated report; this finite certificate does not prove those theorems.
"""

from __future__ import annotations

# This certificate uses assertions as executable checks. Fail closed under -O.
if not __debug__:
    raise SystemExit("certificate requires assertions; run without -O")


import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import factorial, isqrt

SCALE = 10**60


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


@dataclass(frozen=True)
class Interval:
    lo: int
    hi: int

    def __post_init__(self) -> None:
        assert self.lo <= self.hi

    @staticmethod
    def exact(value: int | Fraction) -> Interval:
        value = Fraction(value)
        return Interval(
            (value.numerator * SCALE) // value.denominator,
            ceil_div(value.numerator * SCALE, value.denominator),
        )

    def __add__(self, other: Interval) -> Interval:
        return Interval(self.lo + other.lo, self.hi + other.hi)

    def __neg__(self) -> Interval:
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other: Interval) -> Interval:
        return self + (-other)

    def __mul__(self, other: Interval) -> Interval:
        products = (
            self.lo * other.lo, self.lo * other.hi,
            self.hi * other.lo, self.hi * other.hi,
        )
        return Interval(min(products) // SCALE, ceil_div(max(products), SCALE))

    def divided_by(self, positive: int) -> Interval:
        assert positive > 0
        return Interval(self.lo // positive, ceil_div(self.hi, positive))

    def reciprocal(self) -> Interval:
        assert self.lo > 0
        return Interval(SCALE**2 // self.hi, ceil_div(SCALE**2, self.lo))

    def squared(self) -> Interval:
        low = 0 if self.lo <= 0 <= self.hi else min(self.lo**2, self.hi**2)
        high = max(self.lo**2, self.hi**2)
        return Interval(low // SCALE, ceil_div(high, SCALE))


ONE = Interval.exact(1)
ZERO = Interval.exact(0)


def arctan_bounds(denominator: int, terms: int = 90) -> tuple[Fraction, Fraction]:
    partial = sum(
        (Fraction((-1)**k, (2*k+1)*denominator**(2*k+1)) for k in range(terms)),
        Fraction(0),
    )
    next_sum = partial + Fraction(
        (-1)**terms, (2*terms+1)*denominator**(2*terms+1)
    )
    return min(partial, next_sum), max(partial, next_sum)


def pi_interval() -> Interval:
    # Machin's identity, with the alternating-series remainder enclosed exactly.
    a_lo, a_hi = arctan_bounds(5)
    b_lo, b_hi = arctan_bounds(239)
    return Interval(
        Interval.exact(16*a_lo - 4*b_hi).lo,
        Interval.exact(16*a_hi - 4*b_lo).hi,
    )


PI = pi_interval()
root3_floor = isqrt(3 * SCALE**2)
ROOT3 = Interval(root3_floor, root3_floor + 1)


def trig(x: Interval, sine: bool) -> Interval:
    assert 0 <= x.lo <= x.hi < 7*SCALE
    terms = 80
    x2 = x.squared()
    term = x if sine else ONE
    result = term
    for k in range(1, terms):
        divisor = (2*k)*(2*k+1) if sine else (2*k-1)*(2*k)
        term = (-(term * x2)).divided_by(divisor)
        result = result + term
    power = 2*terms+1 if sine else 2*terms
    # Taylor's theorem: all real derivatives of sin and cos have magnitude <=1.
    remainder = ceil_div(7**power * SCALE, factorial(power))
    return Interval(result.lo - remainder, result.hi + remainder)


Point = tuple[Interval, Interval]


def squared_distance(p: Point, q: Point) -> Interval:
    return (p[0] - q[0]).squared() + (p[1] - q[1]).squared()


def lattice_indices(radius2: Interval, spacing: Fraction) -> list[tuple[int, int]]:
    # |i|,|j| <= 2r/(sqrt(3)*spacing) < 2r for spacing >=1.
    bound = 2 * (isqrt(ceil_div(radius2.hi, SCALE)) + 1)
    sites = []
    for i in range(-bound, bound + 1):
        for j in range(-bound, bound + 1):
            norm = Interval.exact(spacing**2 * (i*i + i*j + j*j))
            if norm.hi < radius2.lo:
                sites.append((i, j))
            else:
                assert norm.lo > radius2.hi, ("unresolved boundary", i, j)
    return sites


def lattice_point(i: int, j: int, spacing: Fraction) -> Point:
    return (
        Interval.exact(spacing * (i + Fraction(j, 2))),
        Interval.exact(spacing * Fraction(j, 2)) * ROOT3,
    )


def q_geometry(q: int) -> tuple[Interval, Interval, Interval]:
    radius = (Interval.exact(2) * trig(PI.divided_by(q), True)).reciprocal()
    diameter = (Interval.exact(2) * trig(PI.divided_by(2*q), True)).reciprocal()
    exit_diameter = Interval.exact(q) * (
        Interval.exact(2*(q-1)) * trig(PI.divided_by(2*(q-1)), True)
    ).reciprocal()
    assert exit_diameter.lo > diameter.hi
    return radius, diameter, exit_diameter


def certify(q: int) -> dict[str, int | str | list[dict[str, int]]]:
    assert q >= 101 and q % 2 == 1
    radius, diameter, exit_diameter = q_geometry(q)
    spacing = 1 + Fraction(1, q*q)
    interior = lattice_indices((radius - Interval.exact(2)).squared(), spacing)
    rim: list[Point] = []
    for j in range(q):
        angle = Interval.exact(2*j) * PI.divided_by(q)
        rim.append((radius * trig(angle, False), radius * trig(angle, True)))
    points = rim + [lattice_point(i, j, spacing) for i, j in interior]
    diameter2 = diameter.squared()
    contacts = diameter_pairs = pair_count = 0
    lower_gap = upper_gap = 10**100
    for i, j in combinations(range(len(points)), 2):
        d2 = squared_distance(points[i], points[j])
        offset = min(j-i, q-(j-i)) if j < q else -1
        if offset == 1:
            # Exact equality follows from the defining radius/chord identity.
            assert d2.lo <= SCALE <= d2.hi
            contacts += 1
        else:
            assert d2.lo > SCALE, ("lower pair", i, j)
            lower_gap = min(lower_gap, d2.lo - SCALE)
        if offset == (q-1)//2:
            # Exact equality follows from the odd-rim maximum-chord identity.
            assert d2.lo <= diameter2.hi and d2.hi >= diameter2.lo
            diameter_pairs += 1
        else:
            assert d2.hi < diameter2.lo, ("upper pair", i, j)
            upper_gap = min(upper_gap, diameter2.lo - d2.hi)
        pair_count += 1
    assert contacts == diameter_pairs == q
    assert pair_count == len(points)*(len(points)-1)//2

    # A centered lattice already supplies a concrete better full-cardinality set
    # for this fixture; no translation-averaging search is needed here.
    available = lattice_indices(diameter2.divided_by(4), Fraction(1))
    assert len(available) >= len(points)
    replacement = available[:len(points)]
    max_replacement_d2 = 0
    replacement_pairs = 0
    for (i, j), (k, ell) in combinations(replacement, 2):
        u, v = i-k, j-ell
        d2 = u*u + u*v + v*v
        assert d2 >= 1
        max_replacement_d2 = max(max_replacement_d2, d2)
        replacement_pairs += 1
    assert max_replacement_d2*SCALE < diameter2.lo
    assert replacement_pairs == pair_count

    # Finite checks of the claimed asymptotic barrier coefficient; the analytic
    # expansion in the report, rather than these examples, proves the limit.
    barrier_checks = []
    for odd in (5, 7, 101, 1001, 10001):
        _, d, b = q_geometry(odd)
        gap = b - d
        ratio = gap * Interval.exact(12*odd*odd) * PI.reciprocal()
        assert ONE.lo < ratio.lo < ratio.hi < 2*SCALE
        barrier_checks.append({
            "q": odd,
            "barrier_lower_times_1e12": gap.lo // (SCALE // 10**12),
        })
    return {
        "arithmetic": "outward-rounded integer intervals at scale 10^60",
        "q": q,
        "source_labels": len(points),
        "source_contact_isolates": len(interior),
        "source_pairs_checked": pair_count,
        "actual_unit_contacts": contacts,
        "actual_diameter_pairs": diameter_pairs,
        "inactive_lower_squared_gap_floor_times_1e12": lower_gap // (SCALE // 10**12),
        "inactive_upper_squared_gap_floor_times_1e12": upper_gap // (SCALE // 10**12),
        "available_replacement_sites": len(available),
        "retained_replacement_labels": len(replacement),
        "replacement_pairs_checked": replacement_pairs,
        "replacement_max_squared_diameter": max_replacement_d2,
        "strict_squared_diameter_margin_floor_times_1e12": (
            diameter2.lo - max_replacement_d2*SCALE
        ) // (SCALE // 10**12),
        "convexity_exit_barrier_lower_times_1e12": (
            exit_diameter.lo - diameter.hi
        ) // (SCALE // 10**12),
        "barrier_examples": barrier_checks,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--q", type=int, default=101)
    args = parser.parse_args()
    print(json.dumps(certify(args.q), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
