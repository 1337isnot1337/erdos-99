from math import cos, sin, pi, sqrt
from random import Random

# Regression certificate for
# target_c_high_t_tb1_two_swap_truth_table_t18687_2026-09-17.md

Q = 5.0
C = 3.0
rng = Random(17092026)


def sq(v):
    return v[0] * v[0] + v[1] * v[1]


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


# Check the two-singleton interpolation identity and shell estimates on a
# deterministic sample of finite configurations.
for D in (100.0, 300.0, 1000.0):
    for _ in range(150_000):
        qi = max(1e-12, rng.random() * Q / D)
        qj = max(1e-12, rng.random() * Q / D)

        ai = rng.uniform(-C / (4 * D), C / (4 * D))
        aj = rng.uniform(-C / (4 * D), C / (4 * D))
        wi = (cos(ai), sin(ai))
        wj = (cos(aj), sin(aj))
        assert sqrt(sq((wi[0] - wj[0], wi[1] - wj[1]))) <= C / D + 1e-12

        a = (-qi * wi[0], -qi * wi[1])
        b = (qj * wj[0], qj * wj[1])

        lam = qj / (qi + qj)
        mu = qi / (qi + qj)
        e = (lam * a[0] + mu * b[0], lam * a[1] + mu * b[1])
        h = qi * qj / (qi + qj)
        e_expected = (h * (wj[0] - wi[0]), h * (wj[1] - wi[1]))
        assert sqrt(sq((e[0] - e_expected[0], e[1] - e_expected[1]))) < 1e-12
        assert sqrt(sq(e)) <= C * Q / D**2 + 1e-12

        for regime in (0, 1):
            if regime == 0:
                ell = 1.0 + rng.random() * 2 * Q / D
            else:
                ell = D - rng.random() * 2 * Q / D

            th = rng.random() * 2 * pi
            r = (ell * cos(th), ell * sin(th))
            r10 = add(r, a)
            r01 = add(r, b)

            f0 = sq(r)
            f10 = sq(r10)
            f01 = sq(r01)

            if f0 > 1.0 and f10 <= 1.0 and f01 <= 1.0:
                assert sqrt(f0) - 1.0 <= C * Q / D**2 + 1e-9

            if f0 < D * D and f10 >= D * D and f01 >= D * D:
                B0 = D * D - f0
                Bbound = (
                    2 * C * Q / D
                    + Q * Q / D**2
                    + C * C * Q * Q / D**4
                )
                assert B0 <= Bbound + 1e-7
                assert D - sqrt(f0) <= Bbound / D + 1e-7

            # A local O(D^-1) move cannot encounter opposite global boundaries.
            if D - 1.0 > 2 * Q / D:
                assert not (f10 <= 1.0 and f01 >= D * D)
                assert not (f01 <= 1.0 and f10 >= D * D)


# Logical reduction of the qi>qj non-shell truth table.  The geometric input is:
# (a) 10 and 01 both bad => shell; (b) 11 bad with 10 safe => shell.
all_patterns = [
    set(),
    {"10"},
    {"01"},
    {"11"},
    {"10", "01"},
    {"10", "11"},
    {"01", "11"},
    {"10", "01", "11"},
]
allowed_qi_gt = [set(), {"10"}, {"01"}, {"10", "11"}]

for bad in all_patterns:
    shell = False
    if "10" in bad and "01" in bad:
        shell = True
    if "11" in bad and "10" not in bad:
        shell = True
    if not shell:
        assert bad in allowed_qi_gt


print("PASS: TB1 two-swap truth-table regressions")
