import math
import random

h = math.sqrt(303.0) / 52.0
two_h = 2.0 * h
root3 = math.sqrt(3.0)

assert 1.0 + h < root3
assert abs((1.0 + h) - 1.3347479843371002) < 1e-15
assert abs(two_h - 0.6694959686742005) < 1e-15

# Synthetic regression for the support-progress pigeonhole.
# Lower gains are positive; upper gains are each strictly below their Delta.
rng = random.Random(20260917)
for _ in range(1000):
    U = rng.randrange(0, 12)
    M = max(U + 1, 2)
    runs = U + 1
    lower_runs = []
    for _r in range(runs):
        lower_runs.append([0.01 + rng.random() for _ in range(rng.randrange(1, 20))])
    G_low = sum(sum(r) for r in lower_runs)
    max_span = max(sum(r) for r in lower_runs)
    assert max_span + 1e-14 >= G_low / (U + 1)
    assert max_span + 1e-14 >= G_low / M

# Run edge-count inequality: span <= edge_count + total original unit slack.
for _ in range(1000):
    n = rng.randrange(1, 100)
    sigmas = [0.01 * rng.random() for _ in range(n)]
    # Pick legal N-projections no larger than the original edge lengths.
    gains = [(1.0 + sigmas[i]) * rng.random() for i in range(n)]
    span = sum(gains)
    total_slack = sum(sigmas)
    assert span <= n + total_slack + 1e-12
    assert n >= span - total_slack - 1e-12

# Leading scales in the two choices recorded in the theorem.
for D in (1e8, 1e12, 1e16):
    t = h + D ** (-1.0 / 3.0)

    for alpha in (0.5, 0.25):
        M = D ** alpha
        span_scale = D / M
        matching_scale = D / (4.0 * M)
        excess = 2.0 * t * M / D
        assert span_scale > 2.0
        assert matching_scale > 0.0
        assert excess < root3 - 1.0

    M = D ** 0.25
    assert abs((D / M) / D ** 0.75 - 1.0) < 1e-12
    assert abs((D / (4.0 * M)) / D ** 0.75 - 0.25) < 1e-12
    assert (2.0 * t * M / D) * D ** 0.75 < two_h + 2.1 * D ** (-1.0 / 3.0)

print('PASS: upper-poor FREE deep-face run arithmetic')
print(f'1+h_*={1.0+h:.15f}')
print(f'sqrt(3)={root3:.15f}')
print(f'2h_*={two_h:.15f}')
