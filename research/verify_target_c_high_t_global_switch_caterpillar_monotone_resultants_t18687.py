#!/usr/bin/env python3
"""Regression checks for the one-sided switch/common-resultant ordering theorem.

The geometric caterpillar assertion is proved in the companion note from the common
train-cut bipartition plus the straight-line thrackle theorem.  This script checks the
interval-support and positive-functional/telescoping algebra on deterministic random
models.
"""

from random import Random

rng = Random(20260917)

for r in range(2, 20):
    # Selected cuts are 0,...,r with a common hub strictly beyond the block.
    hub = r + 3
    switches = []
    for start in range(r):
        # Several diameter intervals may start at one interface; every one must
        # reach at least the hub and hence cross the hubward selected cut r.
        for _ in range(1 + rng.randrange(5)):
            end = hub + rng.randrange(5)
            switches.append((start, end))

    # Each interval has one unique start tag and contains the same hubward cut.
    assert all(a < r <= b for a, b in switches)
    by_start = {i: [] for i in range(r)}
    for h, (a, b) in enumerate(switches):
        by_start[a].append(h)
    all_tags = [h for i in range(r) for h in by_start[i]]
    assert len(all_tags) == len(set(all_tags)) == len(switches)

    # Synthetic oriented switch vectors all lie in one open half-plane phi=x>0.
    vectors = []
    weights = []
    for _ in switches:
        x = rng.uniform(0.01, 3.0)
        y = rng.uniform(-4.0, 4.0)
        vectors.append((x, y))
        weights.append(rng.uniform(0.01, 2.0))

    increments = []
    for i in range(r):
        gx = sum(weights[h] * vectors[h][0] for h in by_start[i])
        gy = sum(weights[h] * vectors[h][1] for h in by_start[i])
        assert gx > 0
        increments.append((gx, gy))

    # Construct resultants with F_i-F_{i+1}=G_i.
    F = [(0.0, 0.0)] * (r + 1)
    fx = fy = 0.0
    F[r] = (fx, fy)
    for i in range(r - 1, -1, -1):
        fx += increments[i][0]
        fy += increments[i][1]
        F[i] = (fx, fy)

    # One common scalar coordinate is strictly monotone, and every contiguous
    # chord has the same positive orientation.
    assert all(F[i][0] > F[i + 1][0] for i in range(r))
    for p in range(r):
        for q in range(p + 1, r + 1):
            chord = (F[p][0] - F[q][0], F[p][1] - F[q][1])
            assert chord[0] > 0
            telescoped = (
                sum(increments[i][0] for i in range(p, q)),
                sum(increments[i][1] for i in range(p, q)),
            )
            assert abs(chord[0] - telescoped[0]) < 1e-10
            assert abs(chord[1] - telescoped[1]) < 1e-10

print("PASS: one-sided common-cut interval support and monotone resultant algebra")
