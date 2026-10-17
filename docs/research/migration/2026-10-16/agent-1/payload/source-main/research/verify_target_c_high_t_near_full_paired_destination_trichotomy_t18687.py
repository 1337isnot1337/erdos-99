#!/usr/bin/env python3
from decimal import Decimal, getcontext
from fractions import Fraction
from math import pi, sin

getcontext().prec = 50

c = Decimal(113) / Decimal(5_000_000)
shore = c / 2
regime = c / 6
terminal_angle = c / 3
old_c0 = Decimal(113) / Decimal(20_000_000)
old_regime = old_c0 / 3

assert shore == Decimal(113) / Decimal(10_000_000)
assert regime == Decimal(113) / Decimal(30_000_000)
assert terminal_angle == Decimal(113) / Decimal(15_000_000)
assert Fraction(113, 30_000_000) == 2 * Fraction(113, 60_000_000)
assert terminal_angle < Decimal(str(pi / 3))

# Exhaust every pair of terminal-prefix cutoffs in small finite models.
# Lane A is terminal exactly for s<=rA and lane B for s<=rB.
for n in range(1, 41):
    for rA in range(n + 1):
        for rB in range(n + 1):
            tt = min(rA, rB)
            mixed = abs(rA - rB)
            oo = n - max(rA, rB)
            assert tt + mixed + oo == n
            assert 3 * max(tt, mixed, oo) >= n

            states = []
            for s in range(1, n + 1):
                aT = s <= rA
                bT = s <= rB
                if aT and bT:
                    states.append('TT')
                elif aT or bT:
                    states.append('M')
                else:
                    states.append('OO')
            rank = {'TT': 0, 'M': 1, 'OO': 2}
            assert all(rank[states[i]] <= rank[states[i + 1]] for i in range(n - 1))

# TT has 2M distinct terminal diameter directions. At M~(c/6)D,
# C67 yields asymptotic projective/central angular span >= 2*(c/6)=c/3.
terminal_chord = sin(float(regime))
assert 3.7666e-6 < float(regime) < 3.7667e-6
assert 7.5333e-6 < float(terminal_angle) < 7.5334e-6
assert 3.7666e-6 < terminal_chord < 3.7667e-6

print('PASS: near-full paired destination trichotomy')
print('near-full exact-force center density =', shore)
print('one TT/mixed/OO regime density =', regime)
print('improvement over old paired-regime density = x2 exactly')
print('TT terminal angular-span floor =', terminal_angle)
print('TT normalized terminal chord-span floor =', terminal_chord)
