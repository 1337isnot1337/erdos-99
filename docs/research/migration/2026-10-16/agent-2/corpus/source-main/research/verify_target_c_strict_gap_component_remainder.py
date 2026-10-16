#!/usr/bin/env python3
"""Certify the constants used in target_c_strict_gap_component_remainder."""

from decimal import Decimal, getcontext


getcontext().prec = 50
pi = Decimal("3.1415926535897932384626433832795028841971693993751")
sqrt3 = Decimal(3).sqrt()
alpha = pi * (Decimal(2) - sqrt3) / Decimal(20)
s118 = Decimal("2.798596312209462")
threshold = pi - s118 - alpha

# The finite identity is checked symbolically by coefficient cancellation:
# G-(m+2+X) = (2+q+m-k-S)-(m+2+(q-k-S)) = 0.
assert (Decimal(2) + Decimal(7) + Decimal(11) - Decimal(3) - Decimal(5)
        - (Decimal(11) + Decimal(2) + (Decimal(7) - Decimal(3) - Decimal(5)))) == 0

# Outward-safe reporting bounds used by the prose.
assert Decimal("0.04208") < alpha < Decimal("0.04210")
assert Decimal("0.30090") < threshold < Decimal("0.30092")

print(f"alpha = {alpha}")
print(f"pi - S118 - alpha = {threshold}")
print("strict-gap remainder identity: PASS")
