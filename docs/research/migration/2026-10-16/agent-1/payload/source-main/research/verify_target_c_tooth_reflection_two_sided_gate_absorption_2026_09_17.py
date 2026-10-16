import math

h = math.sqrt(303.0) / 52.0

# Matching coefficients from a D-O(sqrt D) count of lower-gate edges.
for K in (0.4, 0.5, 1.0, 2.0, 10.0):
    coeff = 0.5 - h / (2.0 * K)
    if K > h:
        assert coeff > 0
assert abs((0.5 - h / 2.0) - 0.3326260078314499) < 1e-14
assert abs((0.5 - h / 4.0) - 0.41631300391572495) < 1e-14

# The near-opposite threshold lies below the source width W>D-h for large D,
# while every absorbed guard below threshold stays >1 from q after terminal motion.
for D in (1e8, 1e12, 1e14):
    e = D ** (-1.0 / 3.0)
    delta = 0.9 * h  # representative admissible excess; inequalities are monotone in delta
    t = delta + e
    L = D + delta
    T = D - 1.0 - 2.0 * e
    assert 1.0 + 2.0 * e > h
    qproj_before = 1.0 + delta + 2.0 * e  # algebraically L-T
    assert qproj_before > 1.0 + t
    qproj_after = qproj_before - t
    assert qproj_after > 1.0

# Sign regression for activation-time strictification.
# Lower gate: first hit from above gives N.d >= 0, so d + theta*Delta*N opens.
# Upper gate: first hit from below for a convex quadratic forces N.d < 0;
# sufficiently small theta shortens it.
for nd_lower in (0.0, 0.1, 0.9):
    theta, ds = 1e-4, 0.2
    lower_sq = 1.0 + 2.0 * theta * ds * nd_lower + (theta * ds) ** 2
    assert lower_sq > 1.0
for nd_upper in (-1e-3, -0.1, -10.0):
    ds = 0.2
    theta = min(1e-4, -nd_upper / ds)
    upper_delta_sq = 2.0 * theta * ds * nd_upper + (theta * ds) ** 2
    assert upper_delta_sq < 0.0

print('PASS: two-sided inactive gate absorption / near-opposite matching arithmetic')
print(f'h_*={h:.15f}')
print(f'K=1 matching coefficient={0.5-h/2:.15f}')
print(f'K=2 matching coefficient={0.5-h/4:.15f}')
