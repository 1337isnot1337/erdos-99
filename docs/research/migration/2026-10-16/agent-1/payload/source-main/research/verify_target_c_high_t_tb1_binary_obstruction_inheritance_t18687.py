from math import cos, sin, pi, sqrt
from random import Random

# Regression certificate for
# target_c_high_t_tb1_binary_obstruction_inheritance_t18687_2026-09-17.md
#
# The proof is analytic.  This script checks the interpolation identity, the
# explicit D^-2 shell estimates on a large deterministic sample, and the
# superdiameter-threshold consequence.

Q = 5.0
C = 3.0
rng = Random(20260917)


def sq(v):
    return v[0] * v[0] + v[1] * v[1]


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul(s, a):
    return (s * a[0], s * a[1])


# Exact interpolation identity used in (BI.13):
# |(1-t)x+t y|^2=(1-t)|x|^2+t|y|^2-t(1-t)|x-y|^2.
for _ in range(10_000):
    x = (rng.uniform(-3, 3), rng.uniform(-3, 3))
    y = (rng.uniform(-3, 3), rng.uniform(-3, 3))
    t = rng.random()
    z = add(mul(1 - t, x), mul(t, y))
    rhs = (1 - t) * sq(x) + t * sq(y) - t * (1 - t) * sq(
        (x[0] - y[0], x[1] - y[1])
    )
    assert abs(sq(z) - rhs) < 1e-10


for D in (100.0, 300.0, 1000.0):
    # From (BI.19): A0=|r|^2-1.
    lower_A_bound = (2 * C * Q + Q * Q) / (D * D) + (Q * Q * C * C) / (
        D**4
    )

    # From (BI.27): B0=D^2-|r|^2.
    upper_B_bound = 2 * C * Q / D + (Q * Q * C * C) / (D**4)

    for _ in range(120_000):
        qi = max(1e-12, rng.random() * Q / D)
        qj = max(1e-12, rng.random() * Q / D)

        # Put both oriented axes into one O(1/D) cone.  The construction below
        # is stricter than the theorem assumption |wi-wj|<=C/D.
        ai = rng.uniform(-C / (4 * D), C / (4 * D))
        aj = rng.uniform(-C / (4 * D), C / (4 * D))
        wi = (cos(ai), sin(ai))
        wj = (cos(aj), sin(aj))
        assert sqrt(sq((wi[0] - wj[0], wi[1] - wj[1]))) <= C / D + 1e-12

        di = (-qi * wi[0], -qi * wi[1])
        dj = (qj * wj[0], qj * wj[1])

        # Probe arbitrary pair directions in both boundary regimes.
        for regime in (0, 1):
            if regime == 0:
                ell = 1.0 + rng.random() * 2 * Q / D
            else:
                ell = D - rng.random() * 2 * Q / D

            th = rng.random() * 2 * pi
            r = (ell * cos(th), ell * sin(th))

            f00 = sq(r)
            f10 = sq(add(r, di))
            f01 = sq(add(r, dj))
            f11 = sq(add(add(r, di), dj))

            # The inheritance lemma compares 11 to the singleton attached to
            # the larger exact-swap magnitude.
            fs = f10 if qi >= qj else f01
            if not (1.0 < f00 < D * D and 1.0 < fs < D * D):
                continue

            if f11 <= 1.0:
                A0 = f00 - 1.0
                assert A0 <= lower_A_bound + 1e-9

            if f11 >= D * D:
                B0 = D * D - f00
                assert B0 <= upper_B_bound + 1e-7
                xi = D - sqrt(f00)
                # In the upper-blocking regime |r|=D-O(D^-1), so for the
                # tested range D+|r|>=D and the length deficit inherits one
                # additional factor 1/D.
                assert xi <= upper_B_bound / D + 1e-7


# Any fixed K/D^2 upper shell eventually lies above the sharp geometric
# thrackle threshold sqrt(D^2-1).
K = 2 * C * Q + 1.0
for D in (1000.0, 10_000.0, 100_000.0):
    if D > 2 * K:
        assert D - K / (D * D) > sqrt(D * D - 1.0)


print("PASS: TB1 binary obstruction inheritance regressions")
print(f"Q={Q:g}, C={C:g}, K_super={K:g}")
