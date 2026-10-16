#!/usr/bin/env python3
import math

h_star = math.sqrt(303.0) / 52.0
gate_bound = 1.0 + h_star
root3 = math.sqrt(3.0)
assert gate_bound < root3

for i in range(1, 1000):
    t = i / 1000.0
    weighted_variance_lower = 1.0 - t * (1.0 - t)
    assert weighted_variance_lower >= 0.75 - 1e-15
    assert math.sqrt(weighted_variance_lower) >= root3 / 2.0 - 1e-12

assert gate_bound < 2.0
assert abs(gate_bound - 1.3347479843371002) < 1e-15

print('inactive-chain face-localization certificate: PASS')
print(f'gate_bound={gate_bound:.15f}')
print(f'sqrt3={root3:.15f}')
print(f'margin={root3-gate_bound:.15f}')
