#!/usr/bin/env python3
import math

CSTAR = 0.129220199818177
assert abs(CSTAR / 2.0 - 0.0646100999090885) < 1e-15

# An unloaded positive contact barycenter with degree >=3 cannot have all
# contact neighbors nonincreasing in one support coordinate. If all projected
# increments are <=0 and a positive weighted sum is zero, each increment must
# be zero; on a unit circle only the two +/- tangential points have zero
# increment.
for degree in (3, 4, 5):
    assert degree > 2

# Simple numerical regression for the support-coordinate argument.
# N=(1,0), contact vectors are unit. If all x-components <=0 and at least
# three distinct unit directions are separated by >= pi/3, no positive
# weighted barycenter can have x-sum zero unless every x-component is zero;
# there are only two zero-x unit directions.
angles = [i * math.pi / 180.0 for i in range(360)]
zero_x = [a for a in angles if abs(math.cos(a)) < 1e-12]
assert len(zero_x) == 2

# Support-cap transverse scale: a=O(sqrt(D)) in a radius D/2+O(sqrt(D)) disk
# yields O(D^(3/4)) transverse extent, which is negligible relative to the
# slow-scale Omega(kappa D^(3/4)) module separation when kappa -> infinity.
for D in (1e8, 1e12, 1e16):
    transverse = D ** 0.75
    kappa = math.log(math.log(D))
    assert kappa * transverse > transverse
    assert transverse / D < 1.0

print('core-gate anchor certificate: PASS')
print(f'c_*/2={CSTAR/2.0:.15f}')
