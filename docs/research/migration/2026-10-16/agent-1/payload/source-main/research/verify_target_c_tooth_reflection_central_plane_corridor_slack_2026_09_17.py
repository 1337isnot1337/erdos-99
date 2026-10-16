import math

h = math.sqrt(303.0) / 52.0
lead_k1 = 0.25 - h / 2.0
lead_k2 = 0.25 - h / 4.0
lead_k4h = 0.25 - h / (2.0 * (4.0 * h))

assert abs(lead_k1 - 0.08262600783144988) < 1e-14
assert abs(lead_k2 - 0.16631300391572494) < 1e-14
assert abs(lead_k4h - 0.125) < 1e-14

# Final quarter-depth-to-center slab: Delta=1/4, K=2.
slab = (0.25 - h / 2.0) / 2.0
assert abs(slab - 0.04131300391572494) < 1e-14

# Any K_D -> infinity drives the path-matching coefficient to 1/4.
for K in (1, 2, 5, 10, 100, 1000):
    coeff = 0.25 - h / (2.0 * K)
    assert coeff < 0.25 and coeff > 0
assert 0.25 - h / (2.0 * 1000) > 0.2498

print('PASS: central-plane corridor telescoping-slack refinement')
print(f'h_*={h:.15f}')
print(f'K=1 matching coefficient={lead_k1:.15f}')
print(f'K=2 matching coefficient={lead_k2:.15f}')
print(f'K=4h_* matching coefficient={lead_k4h:.15f}')
print(f'quarter-depth-to-center K=2 coefficient={slab:.15f}')
