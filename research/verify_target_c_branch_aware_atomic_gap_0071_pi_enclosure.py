#!/usr/bin/env python3
"""Independent exact check of the pi enclosure used by the g=0.0071 certificate."""

from fractions import Fraction as F


def dec(s: str) -> F:
    a, b = s.split('.', 1)
    return F(int(a + b), 10 ** len(b))


def atan_bounds(inv: int, terms: int = 60):
    """Alternating-series enclosure for atan(1/inv)."""
    x = F(1, inv)
    x2 = x * x
    power = x
    partial = F(0)
    for n in range(terms):
        term = power / F(2 * n + 1)
        partial += term if n % 2 == 0 else -term
        power *= x2

    next_term = power / F(2 * terms + 1)
    other = partial + (next_term if terms % 2 == 0 else -next_term)
    return min(partial, other), max(partial, other)


atan5_lo, atan5_hi = atan_bounds(5)
atan239_lo, atan239_hi = atan_bounds(239)

# Machin: pi = 16 atan(1/5) - 4 atan(1/239).
machin_lo = 16 * atan5_lo - 4 * atan239_hi
machin_hi = 16 * atan5_hi - 4 * atan239_lo

PI_LO = dec('3.141592653589793238462643383279502884197169399375105820974944')
PI_HI = PI_LO + F(1, 10**60)

assert PI_LO < machin_lo < machin_hi < PI_HI
assert machin_hi - machin_lo < F(1, 10**85)

print('PASS Machin enclosure for g=0.0071 certificate')
print('Machin width <', float(machin_hi - machin_lo))
print('lower safety margin =', float(machin_lo - PI_LO))
print('upper safety margin =', float(PI_HI - machin_hi))
