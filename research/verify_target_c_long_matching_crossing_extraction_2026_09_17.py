import math
import random

h = math.sqrt(303.0) / 52.0
root3 = math.sqrt(3.0)

# Long-matching conflict radius: if every edge has length >= L,
# any non-properly-crossing matching partner must have a cross endpoint
# within R = sqrt(D^2-L^2).
for D in (100.0, 1e4, 1e8):
    for A in (0.25, 0.5, 1.0, 3.0, 10.0):
        L = D - A / D
        R2 = 2.0 * A - A * A / (D * D)
        assert R2 > 0.0
        R = math.sqrt(R2)
        # Sharp rectangle model: long opposite sides L, connector R,
        # diagonals exactly D.
        assert abs((L * L + R * R) - D * D) < 1e-10 * D * D

# Recover the sharp superdiameter threshold: R<1 iff L>sqrt(D^2-1).
for D in (2.0, 10.0, 1e3):
    threshold = math.sqrt(D * D - 1.0)
    eps = 1e-6
    L_hi = threshold + eps
    L_lo = threshold - eps
    assert D * D - L_hi * L_hi < 1.0
    assert D * D - L_lo * L_lo > 1.0

# Unit-disk packing bound used for conflict degree.
def disk_capacity_bound(R: float) -> float:
    return (2.0 * R + 1.0) ** 2

for R in (0.1, 0.5, 1.0, 2.0, 10.0):
    assert disk_capacity_bound(R) >= 1.0

# FREE upper-gate application at the balanced U = D^(2/3) scale.
# Good upper edges: >= U/2; parity matching: >= U/4; deficit <= 2t/U.
# R^2 <= 4tD/U. Conflict degree <= 2(2R+1)^2.
limit_coeff = 1.0 / (128.0 * h)
assert abs(limit_coeff - 0.02333845270337043) < 1e-15
assert abs(2.0 * h - 0.6694959686742005) < 1e-15

ratios = []
for D in (1e6, 1e9, 1e12, 1e18):
    U = D ** (2.0 / 3.0)
    t = h + D ** (-1.0 / 3.0)
    delta = 2.0 * t / U
    R2 = 2.0 * D * delta - delta * delta
    R = math.sqrt(R2)
    max_conflict_degree = 2.0 * (2.0 * R + 1.0) ** 2
    matching = U / 4.0
    crossing = matching / (max_conflict_degree + 1.0)
    ratio = crossing / (D ** (1.0 / 3.0))
    ratios.append(ratio)
    assert delta * D ** (2.0 / 3.0) < 2.0 * h + 2.1 * D ** (-1.0 / 3.0)
    assert crossing > 0.0

assert ratios[-1] > 0.99 * limit_coeff

# The exact extraction lower bound is monotone in U: numerator grows and
# the conflict radius/degree shrink as U grows.
for D in (1e6, 1e9):
    t = h + D ** (-1.0 / 3.0)
    prev = None
    for mult in (1.0, 2.0, 4.0, 8.0, 16.0):
        U = mult * D ** (2.0 / 3.0)
        delta = 2.0 * t / U
        R = math.sqrt(max(0.0, 2.0 * D * delta - delta * delta))
        degree = 2.0 * (2.0 * R + 1.0) ** 2
        val = (U / 4.0 - 1.0) / (degree + 1.0)
        if prev is not None:
            assert val > prev
        prev = val

# Synthetic bounded-conflict graph regression: greedy independent set has
# size at least n/(Delta+1).
rng = random.Random(20260917)
for _ in range(200):
    n = rng.randrange(10, 100)
    Delta = rng.randrange(1, 8)
    # Build a graph by adding edges only while both degrees stay <= Delta.
    adj = [set() for _ in range(n)]
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    rng.shuffle(pairs)
    for i, j in pairs:
        if len(adj[i]) < Delta and len(adj[j]) < Delta and rng.random() < 0.08:
            adj[i].add(j)
            adj[j].add(i)
    remaining = set(range(n))
    chosen = []
    while remaining:
        v = min(remaining)
        chosen.append(v)
        remaining.discard(v)
        remaining.difference_update(adj[v])
    actual_Delta = max((len(a) for a in adj), default=0)
    assert len(chosen) + 1e-12 >= n / (actual_Delta + 1.0)

print('PASS: long-matching crossing extraction arithmetic')
print(f'h_*={h:.15f}')
print(f'2h_*={2*h:.15f}')
print(f'balanced crossing coefficient={limit_coeff:.15f}')
