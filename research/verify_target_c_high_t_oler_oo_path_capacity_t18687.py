#!/usr/bin/env python3
"""Regression checks for the Oler O--O path-capacity theorem."""

from fractions import Fraction
import math

Astar = 14.0 / (3.0 * math.sqrt(3.0))
Bstar = 1.0 + 5.0 * math.pi / (3.0 * math.sqrt(3.0))

assert 2.69 < Astar < 2.70
assert 4.02 < Bstar < 4.03

Tstar = Fraction(6121, 2000)
assert Astar < float(Tstar)
ratio = float(Tstar) / Astar
assert 1.13 < ratio < 1.14

gamma7 = Fraction(113, 640_000_000)
chat = float(gamma7) / (48.0 * Astar)
expected = 113.0 * math.sqrt(3.0) / 143_360_000_000.0
assert abs(chat - expected) < 1e-24
assert 1.36e-9 < chat < 1.37e-9

old = float(gamma7 / (48 * Tstar))
assert chat > old

print("Oler O--O path capacity certificate: PASS")
print("A* =", Astar)
print("B* =", Bstar)
print("T*/A* =", ratio)
print("c_hat =", chat)
