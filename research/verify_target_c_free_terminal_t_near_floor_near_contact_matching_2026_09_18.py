#!/usr/bin/env python3
"""Regression certificate for the terminal t-near-floor near-contact matching.

This checks only the algebra/numerics introduced in
`target_c_free_terminal_t_near_floor_near_contact_matching_2026-09-18.md`.
It does not re-prove the audited train-orbit, outer-atom, or local pentagon lemmas.
"""

import math
import random

PI = math.pi
SQRT3 = math.sqrt(3.0)
DELTA2 = PI / (2.0 * SQRT3)
S2 = math.sqrt(DELTA2)
G = 0.007707
C0 = 2.0 * S2 + G
MSTAR = 4.0 * S2 + 2.0 * G
MU_STAR = PI / 2.0 + 2.0 * S2 / 5.0 + G / 5.0
T_GAP = 0.00659
ETA_T = 1.0e-4
E = T_GAP + ETA_T
DET = 1.0e-5


def close(x, y, tol=5e-13):
    assert abs(x - y) <= tol * max(1.0, abs(x), abs(y)), (x, y)


close(DELTA2, 0.9068996821171089)
close(S2, 0.9523128068639574)
close(C0, 1.9123326137279146)
close(MSTAR, 3.8246652274558293)
close(MU_STAR, 1.9532628495404796)
close(MU_STAR + T_GAP, 1.9598528495404797)

# Concrete live window.
A_STAR = 5.0 * E - 2.0 * DET
W_STAR = 4.0 * DELTA2 / (C0 + A_STAR)
OMEGA = (3.0 * (PI + DET) ** 2 * DET) ** (1.0 / 3.0)
NEAR = (
    -4.0 * MSTAR / 5.0
    - 8.0 * A_STAR / 5.0
    + 4.0 * DET / 5.0
    + 8.0 * DELTA2 / (C0 + A_STAR)
    - 3.0 * OMEGA
)
MATCH = NEAR / 9.0

close(A_STAR, 0.03343)
close(W_STAR, 1.8643583310313038, tol=2e-5)  # displayed theorem uses W(e), this is endpoint-optimized W
close(OMEGA, 0.06665119212714724)
close(NEAR, 0.4155508927753455)
close(MATCH, 0.04617232141948283)
assert NEAR > 0.4155
assert MATCH > 0.0461

# The note also displays the simpler orbit floor W(e)=4 Delta2/(C0+5e).
W_E = 4.0 * DELTA2 / (C0 + 5.0 * E)
close(W_E, 1.8643391624917125)

# Why r=0 is worst at fixed delta under a+2(r+delta)<=5e:
# move r -> r-h and a -> a+2h.  The explicit linear part changes by -2h,
# while 8 Delta2/(C0+a) strictly decreases.  So the objective strictly falls.
for a in (0.0, 0.005, 0.02, 0.033):
    deriv_per_h = -2.0 - 16.0 * DELTA2 / (C0 + a) ** 2
    assert deriv_per_h < 0.0

# With r=0 and a=5e-2delta, the one-variable objective is decreasing on
# 0<delta<=DET.  A coarse analytic bound is already overwhelming:
#   positive derivative terms <= 4 + 16 Delta2/C0^2,
# while 3 omega'(delta) >= omega(delta)/delta, whose minimum on this tiny
# interval is bounded below using delta=DET and pi+delta>=pi.
pos_deriv_upper = 4.0 + 16.0 * DELTA2 / C0**2
cusp_deriv_lower = (3.0 * PI**2) ** (1.0 / 3.0) * DET ** (-2.0 / 3.0)
assert cusp_deriv_lower > pos_deriv_upper

# Direct deterministic grid check of the one-variable monotonicity and the full
# feasible scalar bound.
def omega(delta):
    if delta == 0.0:
        return 0.0
    return (3.0 * (PI + delta) ** 2 * delta) ** (1.0 / 3.0)


def exact_lower(a, r, delta):
    B = MSTAR + 2.0 * a - delta
    p5 = MSTAR / 5.0 + 2.0 * a / 5.0 - delta / 5.0 - 6.0 * r / 5.0
    W = 4.0 * DELTA2 / (C0 + a)
    return p5 - B + 2.0 * W - 3.0 * omega(delta)

prev = None
for j in range(1, 1001):
    delta = DET * j / 1000.0
    a = 5.0 * E - 2.0 * delta
    val = exact_lower(a, 0.0, delta)
    if prev is not None:
        assert val < prev + 1e-13
    prev = val
assert prev >= NEAR - 2e-12

# Random feasible regression: the optimized closed-form lower bound must never
# exceed the unreduced expression.
rng = random.Random(20260918)
worst = float("inf")
for _ in range(300_000):
    delta = rng.random() * DET
    rmax = max(0.0, 2.5 * E - delta)
    r = rng.random() * rmax
    amax = max(0.0, 5.0 * E - 2.0 * (r + delta))
    a = rng.random() * amax
    val = exact_lower(a, r, delta)
    worst = min(worst, val)
    assert val + 2e-12 >= NEAR

# Recheck the finite sixth-root count pattern used by the inherited five-root
# closure lemma: among the 252 weak compositions of five into six bins, exactly
# the six rotations of (2,0,1,1,1,0) have zero sixth-root sum.
roots = [complex(math.cos(j * PI / 3.0), math.sin(j * PI / 3.0)) for j in range(6)]


def comps(rem, k, prefix=()):
    if k == 1:
        yield prefix + (rem,)
        return
    for x in range(rem + 1):
        yield from comps(rem - x, k - 1, prefix + (x,))

solutions = []
for c in comps(5, 6):
    z = sum(cj * rj for cj, rj in zip(c, roots))
    if abs(z) < 1e-9:
        solutions.append(c)
base = (2, 0, 1, 1, 1, 0)
rotations = {base[i:] + base[:i] for i in range(6)}
assert len(solutions) == 6
assert set(solutions) == rotations

print("terminal t-near-floor near-contact certificate passed")
print(f"t_floor={MU_STAR + T_GAP:.15f}")
print(f"window_top={MU_STAR + T_GAP + ETA_T:.15f}")
print(f"W(e)={W_E:.15f}")
print(f"outer_atom_cap={OMEGA:.15f}")
print(f"near_pentagon_floor={NEAR:.15f}")
print(f"matching_floor={MATCH:.15f}")
print(f"random_min={worst:.15f}")
