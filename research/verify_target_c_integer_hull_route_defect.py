"""Exact arithmetic checks for the integer hull-route defect reduction.

The geometric inputs are the canonical Type-II loaded-hull route inequalities.
This script checks only the finite decompositions and the displayed endpoint
constants; it makes no global-minimality claim.
"""

from decimal import Decimal, getcontext


getcontext().prec = 50


def main() -> None:
    # IR.3 is the coefficient identity
    # (ell-s)=(ell-ceil(s))+(ceil(s)-s), term by term.
    assert Decimal(1) - Decimal("0.4") == (
        Decimal(1) - Decimal(1) + Decimal(1) - Decimal("0.4")
    )

    # IR.7 on representative side lengths.  Integer routes dominate chords.
    sides = [Decimal("1.4"), Decimal("2.2"), Decimal("3.0"), Decimal("1.0")]
    routes = [2, 3, 3, 1]
    u = (routes[0] - 2) + (routes[1] - 2) + (routes[2] - 2) + (routes[3] - 1)
    long_excess = sum(max(s - 2, Decimal(0)) for s in sides if s > 1)
    assert Decimal(u) >= long_excess

    # IR.9: the signed excess above two is paid by u_B.
    perimeter = sum(sides)
    q = Decimal(len(sides))
    m = Decimal(sum(s > 1 for s in sides))
    assert Decimal(u) >= max(perimeter - q - m, Decimal(0))
    # IR.7a: the gap between integer slack and metric long-side excess
    # is itself bounded by the total outer detour.
    gap = Decimal(u) - long_excess
    detour = Decimal(sum(routes)) - perimeter
    assert Decimal(0) <= gap <= detour

    pi = Decimal("3.1415926535897932384626433832795028841971693993751")
    sqrt3 = Decimal(3).sqrt()
    delta2 = pi / (Decimal(2) * sqrt3)
    pure_floor = Decimal(4) * delta2.sqrt() - pi
    assert Decimal("0.6676") < pure_floor < Decimal("0.6678")

    print("integer hull-route defect arithmetic: PASS")
    print(f"pure-tooth detour floor = {pure_floor}")


if __name__ == "__main__":
    main()
