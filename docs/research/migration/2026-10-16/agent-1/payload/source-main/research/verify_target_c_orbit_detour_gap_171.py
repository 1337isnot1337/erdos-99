#!/usr/bin/env python3
"""Finite arithmetic checks for proof-only Target C Section 171."""

from math import pi, sqrt

DELTA2 = pi / (2 * sqrt(3))
S = sqrt(DELTA2)
G = 0.0004
C146 = (4 / 9) * (pi + S)
EPS = 0.00137
T0 = C146 + EPS
A0 = 2 * S + G
D0 = ((9 / 2) * EPS - G) / 2

assert abs(D0 - 0.0028825) < 1e-15

K = (81 * (pi + D0) ** 2 * D0) ** (1 / 3)
B = 10 * T0 - 5 * pi - 5 * D0
RHS = 8 * DELTA2 / A0
MARGIN = RHS - (B + K)

# Uniform derivative lower bound from Section 171.27--28.
KPRIME_LB = (81 ** (1 / 3) / 3) * pi * (pi + D0) ** (-1 / 3) * D0 ** (-2 / 3)
FPRIME_LB = -5 + KPRIME_LB - 16 * DELTA2 / A0 ** 2

assert 152.69 < KPRIME_LB < 152.70
assert FPRIME_LB > 143.6
assert 2.48645 < B < 2.48647
assert 1.32165 < K < 1.32166
assert 3.80845 < RHS < 3.80846
assert MARGIN > 0.00034

# Verify the claimed safe endpoint lies below the first zero of the same endpoint
# envelope. Bisection is implemented directly to keep this standard-library-only.
def endpoint_margin(eps: float) -> float:
    d = ((9 / 2) * eps - G) / 2
    if d < 0:
        return -1.0
    t = C146 + eps
    a0 = 2 * S + G
    b = 10 * t - 5 * pi - 5 * d
    k = (81 * (pi + d) ** 2 * d) ** (1 / 3)
    return b + k - 8 * DELTA2 / a0

lo, hi = 0.00137, 0.00138
assert endpoint_margin(lo) < 0
assert endpoint_margin(hi) > 0
for _ in range(80):
    mid = (lo + hi) / 2
    if endpoint_margin(mid) < 0:
        lo = mid
    else:
        hi = mid
root = (lo + hi) / 2
assert 0.0013709 < root < 0.0013711

print(f"Delta2={DELTA2:.15f}")
print(f"C146={C146:.15f}")
print(f"T0={T0:.15f}")
print(f"d0={D0:.15f}")
print(f"Bedge={B:.15f}")
print(f"Kedge={K:.15f}")
print(f"RHS={RHS:.15f}")
print(f"margin={MARGIN:.15f}")
print(f"Fprime_lower={FPRIME_LB:.15f}")
print(f"endpoint_root={root:.15f}")
print("Section 171 arithmetic checks: PASS")
