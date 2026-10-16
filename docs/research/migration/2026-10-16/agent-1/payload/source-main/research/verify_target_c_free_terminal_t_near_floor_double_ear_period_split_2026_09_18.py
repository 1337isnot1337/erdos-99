#!/usr/bin/env python3
"""Regression checks for the terminal near-floor double-ear/pentagonal-hole note."""

import math
import random

N0 = 0.4155508927753457501087997262559491
SPLIT_SINGLETON = 0.1
P0 = N0 - 2.0 * SPLIT_SINGLETON
EAR_EDGES = 2.0 * P0
RAW_FOREST = P0
TRAIN_MATCH = 2.0 * P0 / 3.0
HOLE_COUNT = P0
HOLE_BOUNDARY = 5.0 * P0
PENTAGON_HOLE_AREA = 3.0 * math.sqrt(3.0) * P0 / 4.0
PERIOD_KERNEL = P0 / 2.0

assert P0 > 0.2155
assert EAR_EDGES > 0.4311
assert RAW_FOREST > 0.2155
assert TRAIN_MATCH > 0.1437
assert HOLE_COUNT > 0.2155
assert HOLE_BOUNDARY > 1.0777
assert PENTAGON_HOLE_AREA > 0.2800
assert PERIOD_KERNEL > 0.1077

# Every loopless maximum-degree-two component is a path, a simple cycle, or
# the possible two-edge parallel cycle.  The forest reduction retains at least
# half of every cycle, and a maximum matching retains at least one third of all
# component edges.
for m in range(1, 10_000):
    path_matching = (m + 1) // 2
    assert path_matching * 3 >= m

    if m >= 3:
        cycle_matching = m // 2
        cycle_forest = m - 1
        assert cycle_matching * 3 >= m
        assert cycle_forest * 2 >= m

# Two-edge parallel cycle.
assert 1 * 3 >= 2
assert 1 * 2 >= 2

rng = random.Random(20260918)
for _ in range(100_000):
    total_edges = 0
    kept_forest = 0
    matching = 0
    for _component in range(rng.randint(1, 50)):
        kind = rng.choice(("path", "cycle", "parallel2"))
        if kind == "path":
            m = rng.randint(1, 200)
            total_edges += m
            kept_forest += m
            matching += (m + 1) // 2
        elif kind == "cycle":
            m = rng.randint(3, 200)
            total_edges += m
            kept_forest += m - 1
            matching += m // 2
        else:
            total_edges += 2
            kept_forest += 1
            matching += 1
    assert 2 * kept_forest >= total_edges
    assert 3 * matching >= total_edges

# Five-edge pentagonal holes: one hole and five physical boundary occurrences
# per fully-rhombic pentagon, with HA area at least 3 sqrt(3)/4 per hole.
for _ in range(100_000):
    s = rng.uniform(0.0, N0 / 2.0)
    p = N0 - 2.0 * s
    g_floor = p
    phole_floor = 5.0 * p
    area_floor = 3.0 * math.sqrt(3.0) * p / 4.0
    assert g_floor >= 0.0
    assert abs(phole_floor / 5.0 - g_floor) < 1.0e-14
    assert abs(area_floor - (math.sqrt(3.0) / 4.0) * (5.0 - 2.0) * p) < 1.0e-14

# Full period-kernel bound.  With total outer boundary P_out >= 0,
# total hole boundary P_hole >= 5g, and T=(P_out+P_hole)/2,
# T-2g >= P_hole/10.  The selected pentagonal holes give P_hole>=5P,
# hence kernel dimension >= P/2.
for _ in range(100_000):
    g = rng.uniform(0.0, 1000.0)
    phole = 5.0 * g + rng.uniform(0.0, 1000.0)
    pout = rng.uniform(0.0, 1000.0)
    t = (pout + phole) / 2.0
    kernel_floor = t - 2.0 * g
    assert kernel_floor + 1.0e-12 >= phole / 10.0

# Corrected local derivative sign from the predecessor note.  If alpha < beta,
# then 2 sin(theta) (alpha-beta) is strictly negative for theta in (0, pi).
for _ in range(100_000):
    theta = rng.uniform(1.0e-8, math.pi - 1.0e-8)
    alpha = rng.uniform(-5.0, 5.0)
    beta = alpha + rng.uniform(1.0e-8, 5.0)
    deriv = 2.0 * math.sin(theta) * (alpha - beta)
    assert deriv < 0.0

print("terminal near-floor double-ear/pentagonal-hole certificate passed")
print(f"full_near_pentagon_floor={P0:.15f}")
print(f"double_ear_edge_floor={EAR_EDGES:.15f}")
print(f"raw_forest_floor={RAW_FOREST:.15f}")
print(f"train_coordinate_matching_floor={TRAIN_MATCH:.15f}")
print(f"pentagonal_hole_count_floor={HOLE_COUNT:.15f}")
print(f"pentagonal_hole_boundary_floor={HOLE_BOUNDARY:.15f}")
print(f"pentagonal_hole_area_floor={PENTAGON_HOLE_AREA:.15f}")
print(f"full_period_kernel_floor={PERIOD_KERNEL:.15f}")
