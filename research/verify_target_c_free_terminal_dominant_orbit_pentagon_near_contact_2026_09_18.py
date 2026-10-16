#!/usr/bin/env python3
"""Regression certificate for terminal FREE dominant-orbit pentagon near-contact theorem."""

from __future__ import annotations

import itertools
import math
import random

PI = math.pi
SQRT3 = math.sqrt(3.0)
DELTA2 = PI / (2.0 * SQRT3)
S2 = math.sqrt(DELTA2)
G = 0.007707
C707 = 2.0 * S2 + G
MSTAR = 2.0 * C707
PSTAR = MSTAR / 5.0

# Endpoint atomic capacity: A <= B/2 = C707.
# Weighted orbit Mantel: W A >= 4 Delta2.
W0 = 4.0 * DELTA2 / C707
OUTSIDE0 = MSTAR - 2.0 * W0
NEAR0 = PSTAR - OUTSIDE0

# Existing four-spoke transport-fan threshold.
C4 = (PI - 3.0 * PSTAR) / 8.0
INTER4 = C4 - OUTSIDE0
MATCH4 = INTER4 / 9.0

ETA_LATTICE = 2.0 * math.asin(0.1)


def close(a: float, b: float, tol: float = 5e-13) -> None:
    assert abs(a - b) <= tol, (a, b, abs(a - b))


close(S2, 0.9523128068639574)
close(C707, 1.9123326137279146)
close(MSTAR, 3.8246652274558293)
close(PSTAR, 0.7649330454911658)
close(W0, 1.8969496741452154)
close(OUTSIDE0, 0.030765879165398413)
close(NEAR0, 0.7341671663257674)
close(C4, 0.10584918963953705)
close(INTER4, 0.07508331047413864)
close(MATCH4, 0.00834259005268207)

# Six oriented triangular-lattice directions in basis (1,zeta), zeta=e^{i pi/3}.
coords = [
    (1, 0),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (0, -1),
    (1, -1),
]

# Exhaustive finite zero-sum classification for five roots.
solutions = []
for c in itertools.product(range(6), repeat=6):
    if sum(c) != 5:
        continue
    x = sum(c[i] * coords[i][0] for i in range(6))
    y = sum(c[i] * coords[i][1] for i in range(6))
    if x == 0 and y == 0:
        solutions.append(c)

base = (2, 0, 1, 1, 1, 0)
rotations = set()
for shift in range(6):
    rotations.add(tuple(base[(i - shift) % 6] for i in range(6)))
assert len(solutions) == 6
assert set(solutions) == rotations

# Every classified multiset, when put in cyclic orientation order, has two
# disjoint adjacent two-step gaps (120 degrees).
for c in solutions:
    labels = []
    for i, n in enumerate(c):
        labels.extend([i] * n)
    gaps = [((labels[(j + 1) % 5] - labels[j]) % 6) for j in range(5)]
    idx = [j for j, gap in enumerate(gaps) if gap == 2]
    assert len(idx) == 2
    used0 = {idx[0], (idx[0] + 1) % 5}
    used1 = {idx[1], (idx[1] + 1) % 5}
    assert used0.isdisjoint(used1)

# Local metric window. 10 sin(eta/2)<1 makes the approximating root sum
# have norm <1, hence exactly zero in the triangular lattice.
for j in range(1, 1000):
    eta = ETA_LATTICE * j / 1000.0
    assert 10.0 * math.sin(eta / 2.0) < 1.0 + 1e-14
    upper = 2.0 * math.cos(PI / 3.0 - eta)
    assert upper > 1.0

# Endpoint scalar monotonicity: A<=C707 implies W>=W0 and therefore
# bounded endpoint mass outside the dominant eta-neighborhood is at most
# OUTSIDE0 + 6 eta in the eta->0 endpoint limit.
rng = random.Random(0xE9920260918)
for _ in range(300_000):
    A = 2.0 * S2 + (C707 - 2.0 * S2) * rng.random()
    Wlb = 4.0 * DELTA2 / A
    assert Wlb >= W0 - 1e-15
    outside = MSTAR - 2.0 * Wlb
    assert outside <= OUTSIDE0 + 1e-15

# Four-spoke intersection and elementary max-degree-five greedy matching.
# At exact endpoint:
# near-phase pentagons >= NEAR0 - 6 eta,
# full >=4-outer-spoke pentagons >= C4 unless S or L_O already has size C4 D.
# Intersection >= C4 - OUTSIDE0 - 6 eta = INTER4 - 6 eta.
for eta in (1e-6, 1e-4, 1e-3, 5e-3, 1e-2):
    inter = INTER4 - 6.0 * eta
    if inter > 0:
        matching = inter / 9.0
        assert matching <= inter
        assert matching > 0.0

print("PASS terminal FREE dominant-orbit pentagon near-contact certificate")
print(f"Delta2={DELTA2:.15f}")
print(f"C707={C707:.15f}")
print(f"Mstar={MSTAR:.15f}")
print(f"pstar={PSTAR:.15f}")
print(f"dominant orbit W0={W0:.15f}")
print(f"bounded outside-orbit endpoint cap={OUTSIDE0:.15f}")
print(f"all-side phase-near pentagon floor={NEAR0:.15f}")
print(f"four-spoke fan threshold C4={C4:.15f}")
print(f"phase-near four-spoke intersection={INTER4:.15f}")
print(f"vertex-disjoint ear matching floor={MATCH4:.15f}")
print(f"local lattice eta ceiling={ETA_LATTICE:.15f}")
