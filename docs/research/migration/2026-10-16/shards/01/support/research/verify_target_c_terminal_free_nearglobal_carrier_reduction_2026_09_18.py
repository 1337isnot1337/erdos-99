#!/usr/bin/env python3
"""Arithmetic/regression checks for the terminal FREE near-global-carrier reduction.

The proof is analytic. This script checks the reported constants and stress-tests the
two scalar inequalities used in the stability calculation.
"""

import math
import random

PI = math.pi
SQRT3 = math.sqrt(3.0)
C0 = PI * (2.0 - SQRT3) / 20.0
T_NG = 2.0 + C0
S2 = math.sqrt(PI / (2.0 * SQRT3))
G_MATCH = 0.007707
MU_STAR = PI / 2.0 + (2.0 / 5.0) * S2 + G_MATCH / 5.0
EPS0 = 0.00659
T0 = MU_STAR + EPS0
C_FLOOR = T0 - 1.0 - C0


def H(lam: float) -> float:
    return 2.0 * lam + 4.0 * lam * math.sqrt(max(0.0, 1.0 - lam * lam))


def cap_from_chord(x: float) -> float:
    if x == 1.0:
        return PI / 8.0
    return 0.25 * (math.asin(x) - x * math.sqrt(max(0.0, 1.0 - x * x)))


AREA_FLOOR = PI / 4.0 - cap_from_chord(C_FLOOR)
TRAIN_FLOOR = 2.0 * AREA_FLOOR
ATTACH_FLOOR = AREA_FLOOR / 3.0

assert abs(C0 - 0.042089360723846655) < 2e-16
assert abs(T_NG - 2.0420893607238466) < 3e-16
assert abs(T0 - 1.9598528495404797) < 3e-15
assert abs((T_NG - T0) - 0.08223651118336694) < 3e-15
assert abs(C_FLOOR - 0.9177634888166330) < 3e-15
assert abs(AREA_FLOOR - 0.5859125225433389) < 3e-15
assert abs(TRAIN_FLOOR - 1.1718250450866778) < 4e-15
assert abs(ATTACH_FLOOR - 0.19530417418111296) < 3e-15

assert C0 > 0.04208
assert T_NG > 2.04208
assert T_NG - T0 > 0.08223
assert C_FLOOR < 0.91777
assert AREA_FLOOR > 0.5859
assert TRAIN_FLOOR > 1.1718
assert ATTACH_FLOOR > 0.1953

# The proof establishes H(lambda)>2 symbolically on lambda in [sqrt(3)/2,1).
lo = math.sqrt(3.0) / 2.0
for i in range(1, 500_000):
    lam = lo + (1.0 - lo) * i / 500_000.0
    if lam < 1.0:
        assert H(lam) > 2.0

# A'(x)=x^2/(2 sqrt(1-x^2)) is increasing. Stress-test the resulting
# superadditivity A(x)+A(y)<=A(x+y) for x+y<1.
rng = random.Random(0xE99)
for _ in range(300_000):
    total = rng.random() * 0.999999
    x = rng.random() * total
    y = total - x
    assert cap_from_chord(x) + cap_from_chord(y) <= cap_from_chord(total) + 2e-15

# Stress-test finite approximants to the countable gap family.
for _ in range(100_000):
    budget = rng.random() * C_FLOOR
    n = rng.randint(1, 12)
    raw = [rng.expovariate(1.0) for _ in range(n)]
    scale = budget / sum(raw)
    xs = [v * scale for v in raw]
    lhs = sum(cap_from_chord(x) for x in xs)
    rhs = cap_from_chord(sum(xs))
    assert lhs <= rhs + 4e-15
    assert PI / 4.0 - lhs >= AREA_FLOOR - 4e-15

print("near-global-carrier reduction certificate: PASS")
print(f"c0                 = {C0:.15f}")
print(f"t_NG               = {T_NG:.15f}")
print(f"terminal t0        = {T0:.15f}")
print(f"low-band width     = {T_NG - T0:.15f}")
print(f"C(K) at t0 <=      = {C_FLOOR:.15f}")
print(f"carrier area >=    = {AREA_FLOOR:.15f} D^2")
print(f"local trains >=    = {TRAIN_FLOOR:.15f} D")
print(f"attachments >=     = {ATTACH_FLOOR:.15f} D")
