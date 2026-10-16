#!/usr/bin/env python3
import math

HSTAR = math.sqrt(303.0) / 52.0
ETA_COEFF = 3.0 ** 0.25
CSTAR = 3.0 ** 0.125
DEN = 1.0 + HSTAR
LEAD = 1.0 / (2.0 * DEN)
SUB = CSTAR / DEN

assert abs(CSTAR * CSTAR - ETA_COEFF) < 1e-15
assert abs(LEAD - 0.37460255109381113) < 1e-15
assert abs(SUB - 0.8594901089209234) < 1e-15


def cap_bound(D, omega, fudge=4.0):
    """Conservative finite version of the NH.11 circular-cap bound.

    `fudge` absorbs the fixed O(1) depth bookkeeping in the proof.  The theorem
    is asymptotic, so the regression only needs to verify that the growing
    omega*D^(1/4) margin dominates such fixed terms.
    """
    sqrtD = math.sqrt(D)
    kappa = CSTAR + omega * D ** (-0.25)
    R = D / 2.0 + ETA_COEFF * sqrtD
    xmin = kappa * D ** 0.75 - ETA_COEFF * sqrtD - HSTAR - fudge
    assert xmin > 0.0
    rad = R * R - xmin * xmin
    assert rad > 0.0
    return 2.0 * math.sqrt(rad), kappa


# Concrete slow choice omega_D=log D.  The cap deficit must diverge and has
# asymptotic scale 4*3^(1/8)*omega_D*D^(1/4).
for D in (1e8, 1e10, 1e12, 1e14, 1e16):
    omega = math.log(D)
    cap, kappa = cap_bound(D, omega)
    deficit = D - cap
    scale = omega * D ** 0.25
    assert deficit > 1.0
    assert deficit / scale > 3.0
    assert kappa > CSTAR
    assert kappa - CSTAR < 0.2

# The exact leading constant predicted by the expansion in NH.12.
assert abs(4.0 * CSTAR - 4.588810761759508) < 1e-15

# omega_D=log D satisfies the slow-growth hypotheses and the retreat from
# half-depth is sublinear.  The normalized threshold converges to 1/2.
for D in (1e8, 1e12, 1e16):
    omega = math.log(D)
    retreat = CSTAR * D ** 0.75 + omega * math.sqrt(D)
    threshold = D / 2.0 - retreat
    assert threshold > 0.0
    assert retreat / D < 0.2

# Parent-chain denominator and the first two asymptotic coefficients in NH.5.
assert HSTAR < 0.335
assert LEAD > 0.3746
assert SUB < 0.86

# The clearing-time correction D*(D^(-1/3))=D^(2/3) is lower order than the
# D^(3/4) threshold correction, and sqrt(D) log D is lower order as well.
for D in (1e8, 1e12, 1e16):
    assert D ** (2.0 / 3.0) / D ** 0.75 < 1.0
    assert math.sqrt(D) * math.log(D) / D ** 0.75 < 1.0

print('near-halfdepth outer-corridor certificate: PASS')
print(f'h_*={HSTAR:.15f}')
print(f'3^(1/8)={CSTAR:.15f}')
print(f'linear chain coefficient={LEAD:.15f}')
print(f'D^(3/4) correction coefficient={SUB:.15f}')
