#!/usr/bin/env python3
"""Sanity checks for the finite oblique-lattice comparison in OL.1.

The proof in the corresponding report is analytic.  This script is deliberately
non-load-bearing: it checks the displayed real constants at high precision and
keeps the boundary-scale distinction between fixed/mesoscopic shear and the
vanishing-shear regression explicit.
"""

from decimal import Decimal, getcontext
from fractions import Fraction
import math

getcontext().prec = 80


def dec_sqrt(x: Decimal) -> Decimal:
    return x.sqrt()


sqrt3 = dec_sqrt(Decimal(3))
a0 = sqrt3 / Decimal(2)
rho = Decimal(1) / sqrt3


def threshold(theta: Decimal, D: Decimal) -> tuple[Decimal, Decimal, bool]:
    s = Decimal(str(math.sin(float(theta))))
    c = Decimal(str(math.cos(float(theta))))
    kappa = dec_sqrt(a0 / s)
    cover = dec_sqrt(Decimal(2) - Decimal(2) * c) / (Decimal(2) * s)
    margin = (Decimal(1) - kappa) * D
    required = Decimal(2) * kappa * cover + Decimal(2) * rho
    return margin, required, margin > required


def main() -> None:
    # Exact polynomial identity used to remove the square root from the
    # Voronoi-radius parallel-body bound.
    for D in [0, 1, 7, 100, 1000000]:
        for r in [Fraction(1, 3), Fraction(7, 10), Fraction(2, 1)]:
            lhs = (Fraction(D, 2) + r) ** 2
            rhs = Fraction(D * D, 4) + D * r + r * r
            assert lhs == rhs

    # Decimal angles are used only for a sanity check.  The theorem uses the
    # exact symbolic quantity sin(theta) and is not certified by these values.
    pi = Decimal(str(math.pi))
    tests = [
        ("fixed", pi / Decimal(3) + Decimal("0.10"), Decimal(1000)),
        ("mesoscopic", pi / Decimal(3) + Decimal("0.01"), Decimal(1000)),
        ("boundary", pi / Decimal(3) + Decimal("0.0001"), Decimal(1000)),
        ("vanishing", pi / Decimal(3) + Decimal("0.000001"), Decimal(2000)),
    ]
    for name, theta, D in tests:
        margin, required, passes = threshold(theta, D)
        print(
            f"{name}: D={D} margin={margin:.18E} "
            f"required={required:.18E} strict={passes}"
        )

    # For theta = pi/3 + R^-2 and D approximately 2R, the threshold margin
    # tends to zero while the required constant tends to 4 + 2/sqrt(3).
    for R in [10, 20, 40, 80, 160]:
        theta = pi / Decimal(3) + Decimal(1) / Decimal(R * R)
        margin, required, passes = threshold(theta, Decimal(2 * R))
        assert not passes
        print(
            f"vanishing-shear R={R}: margin={margin:.18E} "
            f"required={required:.18E} strict={passes}"
        )

    print("PASS: oblique-lattice comparison sanity checks")
    print("Scope: exact analytic theorem OL.1; decimals are non-load-bearing")


if __name__ == "__main__":
    main()
