import math

h = math.sqrt(303.0) / 52.0
c = 1.0 / math.sqrt(1.0 + h / 2.0)
endpoint_coeff = 2.0 * c
threshold_ratio = math.pi / (2.0 * c * c)

assert abs(h - 0.33474798433710024) < 1e-15
assert abs(c - 0.925539574680581) < 1e-15
assert abs(endpoint_coeff - 1.851079149361162) < 2e-15
assert abs(threshold_ratio - 1.833706778894253) < 2e-15

# Finite regression for SE.13. If t <= C sqrt(D) and lambda=K/sqrt(D),
# the bad-ear coefficient is sqrt(2*pi*C/K).
for C in (2.0, 5.0, 20.0):
    K = 2.0 * threshold_ratio * C
    bad_coeff = math.sqrt(2.0 * math.pi * C / K)
    assert bad_coeff < endpoint_coeff
    good_coeff = endpoint_coeff - bad_coeff
    assert good_coeff > 0.0

# The exact threshold K/C = pi/(2 c^2) is where the lower coefficient vanishes.
K_over_C = threshold_ratio
assert abs(math.sqrt(2.0 * math.pi / K_over_C) - endpoint_coeff) < 2e-15

# In the sublinear regime lambda=sqrt(t/D), the normalized bad-ear count is
# sqrt(2*pi)*(t/D)^(1/4), which tends to zero.
for ratio in (1e-2, 1e-4, 1e-8, 1e-12):
    normalized_bad = math.sqrt(2.0 * math.pi) * ratio ** 0.25
    if ratio <= 1e-8:
        assert normalized_bad < 0.03

# Synthetic finite bookkeeping for the special-side budget SE.5.
# H >= q+N and per(K) <= pi D imply X_K <= t-N; then sum s_v <= N+X_K <= t.
for D in (10_000, 10**6, 10**8):
    root = math.sqrt(D)
    N = math.floor(endpoint_coeff * root)
    # Give the terminal deficit a conservative extra sqrt(D) margin.
    t = N + math.floor(0.7 * root)
    q = math.pi * D - t
    H = math.ceil(q) + N
    # Use the largest perimeter allowed by Cauchy for the algebraic worst case.
    X_upper = math.pi * D - H
    assert X_upper <= t - N + 1.0
    sum_s_upper = N + X_upper
    assert sum_s_upper <= t + 1.0

print("PASS: block-superbraid shallow-ear arithmetic")
print(f"h_*={h:.15f}")
print(f"c_blk={c:.15f}")
print(f"endpoint coefficient={endpoint_coeff:.15f}")
print(f"K/C positivity threshold={threshold_ratio:.15f}")
