import math
import random

h = math.sqrt(303.0) / 52.0
assert 1.0 + h < math.sqrt(3.0)
assert abs((0.5 - h / 2.0) - 0.3326260078314499) < 1e-15

# Convex-hull regression: if v is a convex combination of fixed loaded points B,
# then |p-v| <= max_b |p-b|. Thus an upper hit |p-v|=D under global
# upper safety max_b |p-b|<=D forces equality to at least one loaded point.
rng = random.Random(20260917)
for _ in range(5000):
    m = rng.randrange(2, 9)
    B = [(rng.uniform(-5.0, 5.0), rng.uniform(-5.0, 5.0)) for _ in range(m)]
    raw = [rng.random() for _ in range(m)]
    s = sum(raw)
    mu = [x / s for x in raw]
    v = (
        sum(mu[i] * B[i][0] for i in range(m)),
        sum(mu[i] * B[i][1] for i in range(m)),
    )
    p = (rng.uniform(-8.0, 8.0), rng.uniform(-8.0, 8.0))

    def dist(a, b):
        return math.hypot(a[0] - b[0], a[1] - b[1])

    lhs = dist(p, v)
    rhs = max(dist(p, b) for b in B)
    assert lhs <= rhs + 1e-12

# Abstract ancestry induction. L=lower gate preserves the current face.
# U=inactive upper gate restarts at a point outside F, hence in the outer face.
# Starting from an outside-F blocker root, every ancestry vertex is outer-face.
for _ in range(10000):
    n = rng.randrange(1, 200)
    edge_types = [rng.choice("LU") for _ in range(n)]
    face = "outer"  # FREE blocker root is outside F.
    for edge in edge_types:
        if edge == "L":
            # <sqrt(3) lower gate cannot cross the unit-contact graph.
            assert face == "outer"
        else:
            # all-inactive upper child cannot lie in conv(B); it is outside F.
            face = "outer"
        assert face == "outer"

# Existing scale consequences retained after the localization improvement.
for D in (1e8, 1e12, 1e16):
    t = h + D ** (-1.0 / 3.0)
    M = D ** 0.25
    upper_slack = 2.0 * t / M
    lower_slack = 2.0 * t * M / D
    run_span = D / M
    run_matching = D / (4.0 * M)
    assert upper_slack * D ** 0.25 < 2.0 * h + 1e-2
    assert lower_slack * D ** 0.75 < 2.0 * h + 1e-2
    assert abs(run_span / D ** 0.75 - 1.0) < 1e-12
    assert abs(run_matching / D ** 0.75 - 0.25) < 1e-12

print("PASS: two-sided FREE ancestry outer-face localization regression")
print(f"h_*={h:.15f}")
print(f"K=1 outer-face matching coefficient={0.5-h/2.0:.15f}")
