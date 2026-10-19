#!/usr/bin/env python3
"""Exact rational controls for the PR #956 boundary-zigzag proof ledger."""

from fractions import Fraction as F


def require(condition, message):
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def row_gain_lower(length):
    return F(length - 59, 19)


def row_count_margin(radius):
    """Margin in (3R/320000 - 2) >= R/160000."""
    return F(radius, 320000) - 2


def main():
    # Height gap: sqrt(3)/2 - 1/2 > 1/3 iff sqrt(3) > 5/3.
    require(3 * 9 > 25, "a0 - 1/2 must exceed 1/3")

    # On the selected arc, the squared lower bound on |f'| is 39999.
    require(F(39999) > 199**2, "the inverse-circle slope must exceed 199")

    # MVT width, less than two units of inward rounding, gives L > 193/3 > 64.
    require(F(193, 3) > 64, "integer interval width must exceed 64")
    require(row_gain_lower(65) == F(6, 19) > 0,
            "length 65 must force a positive integer net gain")

    # Exact endpoint of the claimed radius threshold and a just-below control.
    require(row_count_margin(640000) == 0,
            "R=640000 must be the endpoint where the coarse row bound closes")
    require(row_count_margin(639999) == F(-1, 320000),
            "the coarse implication must fail just below its stated threshold")

    # The global comparison needs a nonempty interval 640000 <= R < D/2.
    require(F(1280001, 2) > 640000,
            "every D just above 1280000 has admissible comparison radii")
    require(F(1280000, 2) == 640000,
            "the strict comparison interval is empty at D=1280000")

    # h=1 cannot guarantee positive gain under the worst-case deletion count;
    # this guards against confusing inserted count with net population change.
    length = 65
    inserted_h1 = (length - 2) // 1 + 1
    require(inserted_h1 - (length + 1) == -2,
            "the packet ledger must subtract deleted labels")

    require(F(3, 4) < 1, "a0 must be below one for K >= Delta - 2")
    print("PASS: exact rational height, slope, width, and row-gain controls")
    print("PASS: radius threshold equality and just-below negative control")
    print("PASS: strict D/2 comparison onset and deletion-ledger negative control")


main()
