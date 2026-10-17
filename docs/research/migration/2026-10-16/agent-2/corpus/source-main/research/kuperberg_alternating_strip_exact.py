#!/usr/bin/env python3
"""Exact Q(sqrt(3)) audit of the alternating-strip gap-widening candidate.

The report `docs/reports/target_a_alternating_strip_quadratic_gain_2026-10-02.md`
proves the general inequalities. This script independently reconstructs finite
strip footprints and checks every original nearest-neighbor constraint with at
least one moved endpoint, including within-block contacts. It uses no floating
point arithmetic. It does not prove global optimality, exterior compatibility in
an arbitrary source, or the recursive support bound.
"""

from __future__ import annotations

from fractions import Fraction
from math import ceil

from kuperberg_five_block_exact import Surd


ROOT3 = Surd(Fraction(0), Fraction(1))
NEIGHBORS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))


def sign(x: Surd) -> int:
    """Compare a+b*sqrt(3) with zero using rational squares only."""
    a, b = x.a, x.b
    if not a:
        return (b > 0) - (b < 0)
    if not b:
        return (a > 0) - (a < 0)
    if a > 0 and b > 0:
        return 1
    if a < 0 and b < 0:
        return -1
    delta = a * a - 3 * b * b
    return ((delta > 0) - (delta < 0)) * (1 if a > 0 else -1)


def strip_blocks(n: int, r: int) -> dict[tuple[int, int], int]:
    """2r+1 upward triangles, 2r downward triangles; middle one shorter."""
    assert n >= 3 and r >= 1
    a, base = n - 1, 0
    blocks = {}
    for k in range(2 * r + 1):
        size = a - 1 if k == r else a
        for j in range(size + 1):
            for i in range(base, base + size - j + 1):
                assert (i, j) not in blocks
                blocks[i, j] = 2 * k + 1
        if k < 2 * r:
            for j in range(a + 1):
                for i in range(base + size + 1 - j, base + size + 2):
                    assert (i, j) not in blocks
                    blocks[i, j] = 2 * k + 2
        base += size + 2
    return blocks


def translations(r: int, d: Fraction) -> dict[int, tuple[Surd, Surd]]:
    assert 0 < d <= Fraction(1, 8) and r * d <= 2
    eps = d * d / 16
    c = 2 * r * eps
    gain = Surd(Fraction(0), c * c / 6)  # c^2/(2 sqrt(3))
    out = {2 * r + 1: (Surd(), gain)}
    for ell in range(1, 2 * r + 1):
        a = ell * eps
        ty = Surd(-d, a / 3) if ell % 2 else Surd(Fraction(0), -a / 3)
        out[ell] = (Surd(-a), ty)
        out[4 * r + 2 - ell] = (Surd(a), ty)
    return out


def position(p: tuple[int, int], label: int, d: Fraction,
             shifts: dict[int, tuple[Surd, Surd]]) -> tuple[Surd, Surd]:
    i, j = p
    tx, ty = shifts.get(label, (Surd(), Surd()))
    return Surd(2 * i + j) + tx, Surd(d if j >= 0 else 0, Fraction(j)) + ty


def stage_shifts(r: int, d: Fraction, stage: int, s: Fraction
                 ) -> dict[int, tuple[Surd, Surd]]:
    """The explicit integrated path; stage 3 at s=1 is the endpoint."""
    final = translations(r, d)
    out = {}
    middle = 2 * r + 1
    for ell, (tx, ty) in final.items():
        is_up = ell % 2 and ell != middle
        if stage == 1:
            out[ell] = (Surd(), s * ty if is_up else Surd())
        elif stage == 2:
            out[ell] = (s * tx, ty if is_up else s * ty if ell != middle else Surd())
        else:
            assert stage == 3
            out[ell] = (tx, s * ty if ell == middle else ty)
    return out


def verify(n: int, r: int, d: Fraction, stage: int = 3,
           s: Fraction = Fraction(1)) -> int:
    blocks = strip_blocks(n, r)
    shifts = stage_shifts(r, d, stage, s)
    a = n - 1
    width = (2 * r + 1) * (n + 1) - 3
    # The union is exactly a trapezoid, a property used by the nesting proof.
    assert set(blocks) == {(i, j) for j in range(a + 1)
                          for i in range(width - j + 1)}
    # At r=1 this is the existing canonical five-block partition.
    if r == 1:
        from kuperberg_five_block_exact import five_blocks
        assert blocks == five_blocks(n)
    for p, label in blocks.items():
        reflected = (width - p[0] - p[1], p[1])
        assert blocks[reflected] == 4 * r + 2 - label
    seen = set()
    for p, lp in blocks.items():
        for di, dj in NEIGHBORS:
            q = p[0] + di, p[1] + dj
            edge = tuple(sorted((p, q)))
            if edge in seen:
                continue
            seen.add(edge)
            pp = position(p, lp, d, shifts)
            qq = position(q, blocks.get(q, 0), d, shifts)
            dx, dy = pp[0] - qq[0], pp[1] - qq[1]
            margin = dx * dx + dy * dy - 4
            assert sign(margin) >= 0, (n, r, d, p, q, lp, blocks.get(q, 0), margin)
    return len(seen)


def main() -> None:
    checked, cases = 0, 0
    for d in [Fraction(1, q) for q in (8, 9, 12, 16, 24, 32, 64)]:
        for r in sorted({1, 2, ceil(1 / d), int(2 / d)}):
            for n in (3, 4, 7):
                checked += verify(n, r, d)
                cases += 1
    for d in (Fraction(3, 25), Fraction(5, 64), Fraction(7, 100)):
        for r in (1, ceil(1 / d)):
            for n in (3, 6):
                checked += verify(n, r, d)
                cases += 1
    path_cases = 0
    for d, r, n in ((Fraction(1, 8), 8, 3), (Fraction(3, 25), 9, 5)):
        for stage in (1, 2, 3):
            for s in (Fraction(0), Fraction(1, 3), Fraction(2, 3), Fraction(1)):
                checked += verify(n, r, d, stage, s)
                path_cases += 1
    print(f"PASS: {cases} exact strip endpoints; {path_cases} path samples; "
          f"{checked} nearest-neighbor constraints.")
    print("General all-n/all-r inequalities and non-neighbor clearance are proved in the report.")
    print("No global-optimality or arbitrary-source embedding claim is certified.")


if __name__ == "__main__":
    main()
