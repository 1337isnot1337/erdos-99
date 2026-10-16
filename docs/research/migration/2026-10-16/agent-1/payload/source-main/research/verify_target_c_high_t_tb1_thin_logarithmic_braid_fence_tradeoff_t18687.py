#!/usr/bin/env python3
"""Regression certificate for the logarithmic THIN braid/fence tradeoff."""
from math import sqrt, log

p0 = 1609/2500
q0 = p0 - 1.02/sqrt(3)
Tstar = 6121/2000
Cstar = 5*(Tstar/q0)**2
logC = log(Cstar)

assert abs(q0 - 0.05470272542658161) < 1e-15
assert abs(Cstar - 15650.810858588804) < 1e-8
assert abs(logC - 9.658278006676504) < 1e-12
assert abs(1/logC - 0.1035381254617777) < 1e-15
assert abs(1/(2*logC) - 0.05176906273088885) < 1e-15
assert abs(1/(4*logC) - 0.025884531365444424) < 1e-15

# Exponent identity: k=c log D costs D^(c log Cstar).
for target_exp in [0.9, 0.75, 0.5, 0.25]:
    c = (1-target_exp)/logC
    recovered = 1-c*logC
    assert abs(recovered-target_exp) < 1e-14
    assert 0 < c < 1/logC

# Logarithmic widths satisfy the finite matching and subset-error conditions.
# Evaluate in log-coordinates for large representative D values.
for L in [100, 400, 1600, 6400]:  # L=log D
    c = 1/(2*logC)
    k = c*L
    # k^2 D^(-1/4) -> 0 and k^2/D -> 0.
    assert 2*log(k) - L/4 < 0
    assert 2*log(k) - L < 0

print('THIN logarithmic braid/fence tradeoff certificate: PASS')
print(f'q0={q0:.15g}')
print(f'Cstar={Cstar:.15g}')
print(f'logCstar={logC:.15g}')
print(f'c_max={1/logC:.15g}')
print(f'c_half={1/(2*logC):.15g}')
print(f'c_three_quarter={1/(4*logC):.15g}')
