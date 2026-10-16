import math

h = math.sqrt(303.0) / 52.0
coef_lower_slack = 2.0 * h
coef_upper_braid = 1.0 / (128.0 * h)

assert abs(h - 0.33474798433710024) < 1e-15
assert abs(coef_lower_slack - 0.6694959686742005) < 1e-15
assert abs(coef_upper_braid - 0.02333845270337043) < 1e-15

# Balanced scale U = D^(2/3).
# Exact conflict-radius formula uses delta = 2 t_D / U.
ratios = []
for D in (1e6, 1e9, 1e12, 1e18):
    U0 = D ** (2.0 / 3.0)
    t = h + D ** (-1.0 / 3.0)

    # Lower branch at M=D^(2/3).
    M = U0
    lower_span = (D - math.sqrt(D)) / M
    lower_matching = lower_span / 4.0
    lower_excess = 2.0 * t * M / (D - math.sqrt(D))
    assert lower_span / D ** (1.0 / 3.0) > 0.99
    assert lower_matching / D ** (1.0 / 3.0) > 0.24
    assert lower_excess * D ** (1.0 / 3.0) < 2.0 * h + 0.1

    # Upper branch.
    delta = 2.0 * t / U0
    R2 = 2.0 * D * delta - delta * delta
    assert R2 <= 4.0 * t * D / U0 + 1e-12
    R = math.sqrt(R2)
    conflict_degree = 2.0 * (2.0 * R + 1.0) ** 2
    good_matching = U0 / 4.0 - 1.0
    braid = good_matching / (conflict_degree + 1.0)
    ratio = braid / D ** (1.0 / 3.0)
    ratios.append(ratio)
    assert delta * D ** (2.0 / 3.0) < 2.0 * h + 0.1
    assert braid > 0.0

assert ratios[-1] > 0.99 * coef_upper_braid

# The explicit CR.9 lower bound is monotone in U over the upper branch.
for D in (1e6, 1e9, 1e12):
    t = h + D ** (-1.0 / 3.0)
    U0 = D ** (2.0 / 3.0)
    prev = None
    for mult in (1.0, 1.5, 2.0, 4.0, 8.0, 16.0):
        U = mult * U0
        val = (U / 4.0 - 1.0) / (
            2.0 * (4.0 * math.sqrt(t * D / U) + 1.0) ** 2 + 1.0
        )
        if prev is not None:
            assert val > prev
        prev = val

# Variable-U scaling in the o(D) range: lower currency D/U,
# upper currency U^2/D, equal at U=D^(2/3).
for D in (1e9, 1e12):
    U = D ** (2.0 / 3.0)
    low = D / U
    high = U * U / D
    assert abs(low / D ** (1.0 / 3.0) - 1.0) < 1e-10
    assert abs(high / D ** (1.0 / 3.0) - 1.0) < 1e-10

print('PASS: FREE cube-root face/braid tradeoff arithmetic')
print(f'h_*={h:.15f}')
print(f'2h_*={coef_lower_slack:.15f}')
print(f'upper-braid coefficient={coef_upper_braid:.15f}')
