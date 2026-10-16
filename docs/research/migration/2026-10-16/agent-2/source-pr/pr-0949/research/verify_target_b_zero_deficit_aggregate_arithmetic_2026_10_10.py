#!/usr/bin/env python3
"""Exact endpoint arithmetic for the covered-grain aggregate bound.

This certifies the rational evaluation of the four breakpoints in the
piecewise-convex allocation function and its absolute/relative consequences in
docs/reports/target_b_atomic_mantel_equality_gap_2026-10-10.md. It assumes the
analytic share caps and does not verify their geometric hypotheses or prove
Target B shell stability. Machin intervals reject the former false decimal
chain without relying on floating-point approximations.
"""

if not __debug__:
    raise SystemExit("Run without -O: this exact checker requires assertions")

from fractions import Fraction
from math import isqrt


def max_square_sum(cap: Fraction, total: Fraction) -> Fraction:
    """Maximum sum of squares with item cap > 1/2 and total <= 1."""
    if total <= cap:
        return total * total
    return cap * cap + (total - cap) ** 2


def allocation_bound(low_total: Fraction) -> Fraction:
    low_cap = Fraction(2375, 3829)
    high_cap = Fraction(25, 39)
    high_weight = Fraction(88, 361)
    return (
        Fraction(1, 4) * max_square_sum(low_cap, low_total)
        + high_weight * max_square_sum(high_cap, 1 - low_total)
    )


def atan_bracket(x: Fraction, terms: int):
    partial = sum((-1)**k*x**(2*k+1)/Fraction(2*k+1) for k in range(terms))
    following = (-1)**terms*x**(2*terms+1)/Fraction(2*terms+1)
    return min(partial, partial+following), max(partial, partial+following)


def constant_controls():
    upper = Fraction(1324, 10000)
    absolute = Fraction(26167, 10000)
    relative = Fraction(10304, 10000)
    assert Fraction(1103, 1000)*upper*absolute**2 < 1
    assert upper*relative**2 < Fraction(9, 64)

    # Machin: pi/4=4 atan(1/5)-atan(1/239). The tangent is exactly one;
    # the angle is between zero and 4/5, fixing the branch of arctan.
    t = Fraction(1, 5)
    twice = 2*t/(1-t*t)
    four = 2*twice/(1-twice*twice)
    assert (four-Fraction(1, 239))/(1+four/Fraction(239)) == 1
    al, ah = atan_bracket(t, 24)
    bl, bh = atan_bracket(Fraction(1, 239), 10)
    assert 0 < 4*al-bh < 4*ah-bl < Fraction(4, 5)
    pi_lo, pi_hi = 16*al-4*bh, 16*ah-4*bl
    scale = 10**25
    root = isqrt(3*scale*scale)
    sqrt3_hi = Fraction(root+1, scale)
    assert Fraction(root, scale)**2 <= 3 < sqrt3_hi**2
    c_hi = 2*sqrt3_hi/pi_lo
    # x0^2=64/(9c): 2.6167 is BELOW 1.0304*x0. It cannot be the
    # intermediate term of the report's former chained inequality.
    assert absolute**2 < relative**2*64/(9*c_hi)
    print("PASS: exact absolute bound >2.6167 and relative bound >1.0304*x0")
    print("PASS: rational enclosures reject the former 2.6167 >1.0304*x0 chain")


def main() -> None:
    low_cap = Fraction(2375, 3829)
    breakpoints = sorted(
        {Fraction(0), Fraction(1), low_cap, Fraction(14, 39)}
    )
    values = [(x, allocation_bound(x)) for x in breakpoints]
    for x, value in values:
        print(f"x={x}: C(x)={value} = {float(value):.12f}")

    maximum = max(value for _, value in values)
    assert maximum == Fraction(72689, 549081)
    assert maximum < Fraction(1324, 10000)
    assert Fraction(1, 2) < low_cap < Fraction(25, 39)
    print(f"maximum={maximum} < 0.1324")
    constant_controls()


if __name__ == "__main__":
    main()
