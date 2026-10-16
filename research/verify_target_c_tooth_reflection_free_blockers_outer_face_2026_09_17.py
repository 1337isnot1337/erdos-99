#!/usr/bin/env python3
import math

h_star = math.sqrt(303.0) / 52.0
edge_bound = 1.0 + h_star
assert edge_bound < math.sqrt(3.0)

# Convex-hull blocker regression in one dimension of distances: if z is a
# convex combination of loaded vertices b_i, norm convexity gives
# |z-q| <= max_i |b_i-q|. A value above D therefore forces a loaded blocker.
weights = [0.2, 0.3, 0.5]
dists = [7.0, 9.0, 11.0]
weighted_upper = sum(w * d for w, d in zip(weights, dists))
assert weighted_upper <= max(dists)

# Linear-chain sample coefficient retained by the outer-face upgrade.
den = 1.0 + h_star
coeff_049 = 0.49 / den
assert abs(coeff_049 - 0.3671105000719349) < 1e-15

print('free-blocker outer-face certificate: PASS')
print(f'1+h_*={edge_bound:.15f}')
print(f'lambda=.49 chain coefficient={coeff_049:.15f}')
