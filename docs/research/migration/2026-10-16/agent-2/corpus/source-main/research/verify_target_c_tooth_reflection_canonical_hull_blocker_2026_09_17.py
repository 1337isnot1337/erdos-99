#!/usr/bin/env python3
import math

eta = 3.0 / 26.0
c = 49.0 / 52.0
h = math.sqrt(303.0) / 52.0
C = math.sqrt(303.0) / 26.0
base_cap = 49.0 * math.sqrt(303.0) / 1352.0
rho = 0.129220199818177
span = 2.0 * rho

assert abs(c * c + h * h - 1.0) < 1e-14
assert abs(C * C - 303.0 / 676.0) < 1e-14
assert C < 1.0
assert base_cap < 1.0
assert math.asin(h) < math.pi / 6.0
assert span > 0.2584

# Check the exact cap algebra over a deterministic parameter grid.
alpha_max = math.asin(h)
for ia in range(1, 81):
    alpha = alpha_max * ia / 80.0
    ca = math.cos(alpha)
    ha = math.sin(alpha)
    for it in range(ia):
        theta = alpha * it / ia
        capacity = ha * math.cos(theta) - ca * math.sin(theta)
        assert abs(capacity - math.sin(alpha - theta)) < 1e-12
        assert capacity > 0.0
        for frac in (0.05, 0.25, 0.5, 0.9):
            gap = frac * capacity
            sp = ha * math.cos(theta) - gap
            depth_x = sp + ha * math.cos(theta)
            depth_base = sp + ca * math.sin(theta)
            assert sp >= ca * math.sin(theta) - 1e-12
            assert 0.0 <= depth_x < 2.0 * ha + 1e-12
            assert depth_x <= C + 1e-12
            assert depth_base < math.sin(2.0 * alpha) + 1e-12
            assert depth_base <= base_cap + 1e-12
            assert gap < ha + 1e-12

# Check the normalized-direction perturbation bound used to replace an arbitrary
# upper blocker by the farthest reflected blocker.
for D in (10.0, 100.0, 1000.0, 1000000.0):
    assert D > 2.0 * C
    angle_bound = 2.0 * math.asin(C / (D - C))
    assert angle_bound > 0.0
    assert angle_bound * D < 2.4 * C

print('canonical reflection hull-blocker certificate: PASS')
print(f'eta={eta:.15f}')
print(f'reflection displacement={C:.15f}')
print(f'base cap ceiling={base_cap:.15f}')
print(f'normal span floor={span:.15f} rad')
