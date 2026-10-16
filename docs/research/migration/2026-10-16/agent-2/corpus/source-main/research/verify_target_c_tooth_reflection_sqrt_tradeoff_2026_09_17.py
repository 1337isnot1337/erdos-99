import math

h = math.sqrt(303.0) / 52.0
a = 49.0 / 100.0
lam = math.sqrt(8.0 / 3.0)
coef_super = math.sqrt(3.0 / 8.0)
coef_thick = math.sqrt(a / (4.0 * h))
coef_match = coef_thick / 4.0
coef_slack = 2.0 * h / coef_thick

assert a < 0.5
assert abs(h - 0.33474798433710024) < 1e-15
assert abs(coef_super - 0.6123724356957945) < 1e-15
assert abs(coef_thick - 0.6049354828317218) < 1e-15
assert coef_thick < coef_super
assert abs(coef_match - 0.15123387070793046) < 1e-15
assert abs(coef_slack - 1.1067229277744943) < 1e-15

# The 0.49/D thin threshold lies strictly above sqrt(D^2-1).
for D in (2.0, 10.0, 1e3, 1e9):
    gap = 1.0 - 2.0 * a + a * a / (D * D)
    assert gap > 0.0

# Thin-dominant split: if s >= 3U/4, parity gives >=3U/8 braid edges.
# Threshold U=lambda sqrt(D) balances that against lower progress D/U.
assert abs((3.0 / 8.0) * lam - coef_super) < 1e-15
assert abs(1.0 / lam - coef_super) < 1e-15

# Thick-dominant asymptotic: m > U/4 and b_j >= a_D/Delta_j.
# Thus B >= a U^2/(16h), so max lower-run span has currency
# D/U + [a/(16h)]U, whose minimum is coef_thick*sqrt(D).
beta = a / (16.0 * h)
assert abs(2.0 * math.sqrt(beta) - coef_thick) < 1e-15

# Finite-scale regression with the exact a_D and t_D terms.
for D in (1e8, 1e12, 1e16):
    t = h + D ** (-1.0 / 3.0)
    aD = a * (1.0 - t / (2.0 * D))
    betaD = aD / (16.0 * t)

    # Search over U/sqrt(D) on a broad logarithmic grid. Ignore the explicit
    # O(sqrt(D)) theorem error here; this checks the load-bearing coefficient.
    vals = []
    for k in range(-200, 201):
        u = 10.0 ** (k / 100.0)  # U/sqrt(D)
        val = (1.0 + betaD * u * u) / (u + D ** -0.5)
        vals.append(val)
    finite_min = min(vals)
    assert finite_min > 0.99 * coef_thick

    # Reciprocal-time lower bound on synthetic equal-increment thick gates.
    U = max(4, int(round(math.sqrt(D))))
    m = max(1, U // 4)
    Delta = t / m
    rho = a / D
    # Exact b from the gate identity.
    b = (2.0 * D * rho - rho * rho + Delta * Delta) / (2.0 * Delta)
    lower = aD / Delta
    assert b + 1e-12 >= lower
    B = m * b
    assert B + 1e-8 >= aD * m * m / t

# Run matching constants: span c sqrt(D), total slack <=h+o(1),
# half the edges have excess <=2h/(c sqrt(D)), then parity halves again.
for D in (1e8, 1e12):
    t = h + D ** (-1.0 / 3.0)
    run_edges = coef_thick * math.sqrt(D) - t
    threshold = 2.0 * t / run_edges
    assert run_edges / (4.0 * math.sqrt(D)) > 0.99 * coef_match
    assert threshold * math.sqrt(D) < 1.01 * coef_slack

print('PASS: FREE square-root face/superdiameter tradeoff arithmetic')
print(f'h_*={h:.15f}')
print(f'thick-run coefficient={coef_thick:.15f}')
print(f'super-braid coefficient={coef_super:.15f}')
print(f'run matching coefficient={coef_match:.15f}')
print(f'run good-edge slack coefficient={coef_slack:.15f}')
