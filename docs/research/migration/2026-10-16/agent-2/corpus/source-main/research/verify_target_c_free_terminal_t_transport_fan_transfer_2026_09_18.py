#!/usr/bin/env python3
"""Regression checks for exact-t transfer of the terminal transport/fan ladder.

Checks the displayed constants and the defect-coefficient domination used to pass from
`a+2(r+delta)<=5 epsilon` to the uniform `-3 epsilon` loss for k=1,2,3,4.
This is a scalar regression aid; the endpoint-multigraph and geometric fan lemmas are
proved in the companion notes.
"""

from decimal import Decimal, getcontext
from fractions import Fraction
import random

getcontext().prec = 60

PI = Decimal("3.14159265358979323846264338327950288419716939937510")
SQRT3 = Decimal(3).sqrt()
S2 = (PI / (Decimal(2) * SQRT3)).sqrt()
GAP = Decimal("0.007707")
MSTAR = Decimal(4) * S2 + Decimal(2) * GAP
PSTAR = MSTAR / Decimal(5)
MUSTAR = PI / Decimal(2) + Decimal(2) * S2 / Decimal(5) + GAP / Decimal(5)
EPS = Decimal("0.00710")

expected = {
    1: Decimal("0.1785348619758701904978025519576178167"),
    2: Decimal("0.1636756862927590972711139315910183831"),
    3: Decimal("0.1407115056915874077389587910244556221"),
    4: Decimal("0.1005241896395369510576872950329707903"),
}

for k in range(1, 5):
    c = (
        PI
        - Decimal(k - 1) * PSTAR
        - Decimal(3 * (6 - k)) * EPS
    ) / Decimal(20 - 3 * k)
    assert abs(c - expected[k]) < Decimal("1e-36")

assert Decimal("1.95326284") < MUSTAR < Decimal("1.95326286")
assert Decimal("1.96036284") < MUSTAR + EPS < Decimal("1.96036286")

# Exact rational stress-test of the coefficient step in fan-ladder equation (4.2).
# For nonnegative a,r,delta satisfying
#       a + 2(r+delta) <= 5 epsilon,
# the residual defect correction for k=1..4 is at least -3 epsilon.
rng = random.Random(0xE9900710)
EPS_Q = Fraction(71, 10000)
checked = 0
for _ in range(100000):
    r = Fraction(rng.randrange(0, 10000), 1000000)
    delta = Fraction(rng.randrange(0, 10000), 1000000)
    budget = 5 * EPS_Q - 2 * (r + delta)
    if budget < 0:
        continue
    a = budget * Fraction(rng.randrange(0, 1001), 1000)
    assert a + 2 * (r + delta) <= 5 * EPS_Q

    for k in range(1, 5):
        correction = (
            Fraction(k + 4, 5 * (6 - k)) * delta
            - Fraction(6, 5) * r
            - Fraction(2 * (k - 1), 5 * (6 - k)) * a
        )
        assert correction >= -3 * EPS_Q
    checked += 1

print("PASS exact-t terminal fan-transfer regression")
print("mu_star", MUSTAR)
print("epsilon", EPS)
print("window_upper", MUSTAR + EPS)
for k in range(1, 5):
    print("k", k, "C_k", expected[k], "spokes", Decimal(k) * expected[k])
print("random_feasible_defect_samples", checked)
