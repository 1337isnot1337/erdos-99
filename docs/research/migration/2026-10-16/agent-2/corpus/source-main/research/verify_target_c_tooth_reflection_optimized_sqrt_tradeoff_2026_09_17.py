import math
import random

h = math.sqrt(303.0) / 52.0
k_inf = 1.0 / (2.0 * h)
c_inf = 1.0 / math.sqrt(2.0 + h / 2.0)
match_lam2 = c_inf / 4.0
slack_lam2 = 2.0 * h / c_inf
cross_inc = c_inf / 4.0

assert abs(c_inf - 0.679255355387642) < 1e-15
assert abs(match_lam2 - 0.1698138388469105) < 1e-15
assert abs(slack_lam2 - 0.9856322270615415) < 1e-15
assert abs(cross_inc - match_lam2) < 1e-15

assert abs(1.0 - 2.0 * c_inf * c_inf - c_inf * c_inf / (4.0 * k_inf)) < 1e-15
y0 = c_inf / (2.0 * k_inf)
q0 = 1.0 + k_inf * y0 * y0 - c_inf * (2.0 * c_inf + y0)
assert abs(q0) < 2e-15

for D in (10**4, 10**6, 10**8, 10**12):
    Df = float(D)
    tau = 1.0 / (Df + math.sqrt(Df * Df - 1.0))
    abar = Df * tau
    tbar = h + Df ** (-1.0 / 3.0)
    A = abar * (1.0 - tbar / (2.0 * Df))
    k = A / tbar
    c = 1.0 / math.sqrt(2.0 + 1.0 / (4.0 * k))

    assert tau > 0.0
    # In exact arithmetic abar>1/2; at very large D binary64 rounds it to 1/2.
    assert abar >= 0.5
    assert k > 0.0
    assert c > 0.0
    assert abs(tau * (Df + math.sqrt(Df * Df - 1.0)) - 1.0) < 1e-14

    rng = random.Random(D)
    rootD = math.sqrt(Df)
    for _ in range(10000):
        m = rng.random() * 5.0 * rootD
        lhs = Df + k * m * m - c * rootD * (2.0 * c * rootD + m)
        rhs = k * (m - c * rootD / (2.0 * k)) ** 2
        scale = max(1.0, abs(lhs), abs(rhs))
        assert abs(lhs - rhs) <= 1e-10 * Df + 1e-12 * scale
        assert lhs >= -1e-9 * Df

    for _ in range(10000):
        s = rng.random() * 2.0 * c * rootD
        m = rng.random() * 5.0 * rootD
        assert Df + k * m * m + 1e-8 * Df >= c * rootD * (s + m)

D = 10**12
Df = float(D)
tau = 1.0 / (Df + math.sqrt(Df * Df - 1.0))
tbar = h + Df ** (-1.0 / 3.0)
k = (Df * tau * (1.0 - tbar / (2.0 * Df))) / tbar
cD = 1.0 / math.sqrt(2.0 + 1.0 / (4.0 * k))
assert abs(cD - c_inf) < 2e-5

print('PASS: optimized FREE square-root tradeoff arithmetic')
print(f'h_*={h:.15f}')
print(f'k_inf={k_inf:.15f}')
print(f'c_opt={c_inf:.15f}')
print(f'Lambda=2 matching coefficient={match_lam2:.15f}')
print(f'Lambda=2 slack coefficient={slack_lam2:.15f}')
print(f'braid/diameter crossing coefficient={cross_inc:.15f}')
print(f'finite c_D at D=1e12={cD:.15f}')
