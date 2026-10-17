#!/usr/bin/env python3
import math

HSTAR = math.sqrt(303.0) / 52.0
DEN = 1.0 + HSTAR
LIMIT = 1.0 / (2.0 * DEN)

assert HSTAR < 0.335
assert abs(LIMIT - 0.37460255109381113) < 1e-15

# Fixed fractional caps strictly below half-depth have diameter < D.
for lam in (0.01, 0.10, 0.25, 0.40, 0.49, 0.499):
    rho = 2.0 * math.sqrt(lam - lam * lam)
    assert 0.0 < rho < 1.0

# At lambda=1/2 the circular-cap estimate reaches D exactly, explaining the
# natural endpoint of this safety argument.
rho_half = 2.0 * math.sqrt(0.5 - 0.25)
assert abs(rho_half - 1.0) < 1e-15

# Linear parent-chain coefficients.
examples = {
    0.25: 0.18730127554690557,
    0.49: 0.3671105000719349,
}
for lam, expected in examples.items():
    coeff = lam / DEN
    assert abs(coeff - expected) < 1e-15
    assert coeff < LIMIT

# A parent gate changes original support depth by at most 1+t_D, whose
# asymptotic upper envelope is 1+h_*.
for D in (1e9, 1e12, 1e18):
    td_upper = HSTAR + D ** (-1.0 / 3.0)
    assert 1.0 + td_upper < 1.336

# Numerical disk-cap regression: R=D/2+O(sqrt D), support offset
# H-c=D/2-O(sqrt D). For any fixed lambda<1/2 the asymptotic chord margin is
# linear in D and dominates the sqrt(D) errors.
for lam in (0.25, 0.40, 0.49):
    rho = 2.0 * math.sqrt(lam - lam * lam)
    margin = 1.0 - rho
    assert margin > 0.0
    D = 1e16
    assert margin * D > 100.0 * math.sqrt(D)

print('linear inactive-chain certificate: PASS')
print(f'h_*={HSTAR:.15f}')
print(f'limit chain coefficient={LIMIT:.15f}')
print(f'lambda=1/4 coefficient={0.25/DEN:.15f}')
print(f'lambda=0.49 coefficient={0.49/DEN:.15f}')
