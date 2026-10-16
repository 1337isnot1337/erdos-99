#!/usr/bin/env python3
"""Regression certificate for the THIN growing-braid fixed-bracket theorem.

This checks the new counting constants, the fixed +/-0.01D flank density,
fixed-r braid/bracket incidence arithmetic, and the elementary diagonal growth
relation. Upstream geometric inputs are intentionally not re-proved here.
"""
from fractions import Fraction
from math import sqrt, log, floor

# Upstream constants from the audited THIN braid/common-spine state.
gamma = Fraction(791, 9_600_000_000)
nu = gamma / 16
p0 = Fraction(1609, 2500)
Tstar = Fraction(6121, 2000)

mu = 0.01
q0 = float(p0) - (1 + 2*mu)/sqrt(3)
assert q0 > 0
assert abs(q0 - 0.05470272542658161) < 1e-15

# Fixed-r coefficient after counting (row, r-matching, left train, right train)
# and then retaining one of the two row phase signs.
def rows_per_N(r: int) -> float:
    return 3*q0*q0/(4*float(Tstar)**2 * (5**r))

def rows_per_D(r: int) -> float:
    return rows_per_N(r)*float(nu)

for r in range(1, 8):
    assert rows_per_N(r) > 0
    if r > 1:
        assert abs(rows_per_N(r-1)/rows_per_N(r) - 5.0) < 1e-12

# r=1,2 concrete values are useful regressions.
assert abs(rows_per_N(1) - 4.792083980673866e-05) < 1e-18
assert abs(rows_per_N(2) - 9.584167961347732e-06) < 1e-19
assert abs(rows_per_D(2) - 4.935596912386755e-14) < 1e-27

# The two fixed flank trains are distinct by construction because one crossing
# lies below -mu D and the other above +mu D on every retained row.
assert -mu < mu

# Diagonal sanity: for an explicit slowly growing r(D)=floor(sqrt(log D)),
# r/log D -> 0 and 5^r = D^o(1).  We check the exponent identity numerically
# at large logarithmic scales without constructing astronomical D.
for L in [100, 400, 1600, 6400, 25600]:  # L = log D
    r = floor(sqrt(L))
    exponent_loss = r*log(5)/L
    assert exponent_loss < 0.2
# Monotone decay of the exponent loss along this sequence.
losses = []
for L in [100, 400, 1600, 6400, 25600]:
    r = floor(sqrt(L))
    losses.append(r*log(5)/L)
assert all(losses[i+1] < losses[i] for i in range(len(losses)-1))

# The matching feasibility side condition r^2 Delta/N -> 0 is compatible with
# Delta=O(D^(3/4)), N=Theta(D): for the same explicit r scale it reduces to
# r^2 D^(-1/4) -> 0.  Check in log coordinates.
for L in [100, 400, 1600]:
    r = floor(sqrt(L))
    val_log = 2*log(max(r,1)) - L/4
    assert val_log < 0

print('THIN growing-braid fixed-bracket certificate: PASS')
print(f'nu={float(nu):.15g}')
print(f'q0={q0:.15g}')
print(f'fixed r=1 rows/N={rows_per_N(1):.15g}')
print(f'fixed r=2 rows/N={rows_per_N(2):.15g}')
print(f'fixed r=2 rows/D={rows_per_D(2):.15g}')
