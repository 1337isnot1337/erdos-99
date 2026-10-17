#!/usr/bin/env python3
"""Non-load-bearing arithmetic regression for flat-center degree trichotomy."""
import math

for eps in (1e-6, 1e-4, 1e-2, 0.1):
    assert eps < math.pi / 3
    # Four exterior gaps (> pi/3 each) cannot fit into pi+eps.
    assert 4 * math.pi / 3 > math.pi + eps
    # Degree-four exterior gaps pi/3+eta_i with eta_i <= eps produce near-unit pairs.
    dmax = 2 * math.sin((math.pi / 3 + eps) / 2)
    assert dmax > 1
    assert dmax <= 1 + eps + 1e-15
    # Degree-three balance: exterior gaps B,C lie in (pi/3,2pi/3+eps).
    denom = math.sin(math.pi / 3 - eps)
    ratio = math.sin(eps) / denom
    assert ratio > 0
    assert ratio < 2 * eps

print("PASS flat-center contact-degree trichotomy arithmetic")
print("example epsilon=0.01 hidden-pair max:",
      2 * math.sin((math.pi / 3 + 0.01) / 2))
print("example epsilon=0.01 third-weight ratio bound:",
      math.sin(0.01) / math.sin(math.pi / 3 - 0.01))
