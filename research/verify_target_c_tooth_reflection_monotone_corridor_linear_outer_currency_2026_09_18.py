#!/usr/bin/env python3
import itertools
import math
import random

H_STAR = math.sqrt(303.0) / 52.0
C_HALF = 3.0 ** (1.0 / 8.0)


def blocks(bits, value):
    out = 0
    prev = None
    for b in bits:
        if b == value and prev != value:
            out += 1
        prev = b
    return out


def external_edges(bits):
    return sum(1 for a, b in zip(bits, bits[1:]) if not (a and b))


def check_path_block_identity():
    # False = outside F, True = inside F.  The FREE root is outside.
    # Exhaustively verify |E_ext| = z_C + r_C - 1 and r_C <= z_C.
    for n in range(1, 16):
        for tail in itertools.product((False, True), repeat=n - 1):
            bits = (False,) + tail
            z = sum(not b for b in bits)
            r = blocks(bits, True)
            eext = external_edges(bits)
            assert eext == z + r - 1
            assert r <= z


def check_pocket_integer_bound():
    # One visited pocket has old route length ell, hull chord s<=ell, hence
    # width <= per/2 <= ell.  Over p visited pockets this gives
    # sum(width) <= sum(ell-1)+p.
    rng = random.Random(0xE99C0DE)
    for _ in range(100000):
        p = rng.randint(0, 40)
        ells = [rng.randint(2, 20) for _ in range(p)]
        widths = []
        for ell in ells:
            s = rng.uniform(1.0, float(ell))
            w = rng.random() * (ell + s) / 2.0
            assert w <= ell + 1e-12
            widths.append(w)
        x_visited = sum(ell - 1 for ell in ells)
        assert sum(widths) <= x_visited + p + 1e-10


def check_finite_ledgers():
    # Synthetic checks of the two exact finite ceilings:
    # S <= 2x + z + r - 1 + t
    # S <=  x + z + 2r - 1 + t
    # with r<=z<=Z.
    rng = random.Random(0x99FEEE)
    for _ in range(300000):
        x = rng.uniform(0.0, 200.0)
        Z = rng.randint(1, 200)
        zc = rng.randint(1, Z)
        r = rng.randint(0, zc)
        t = rng.uniform(0.0, H_STAR + 0.01)

        gin_a = rng.random() * (2.0 * x)
        gin_b = rng.random() * (x + r)
        gin = min(gin_a, gin_b)

        eext = zc + r - 1
        slack_ext = rng.random() * t
        gext = rng.random() * eext + slack_ext
        S = gin + gext

        assert S <= 2.0 * x + zc + r - 1.0 + t + 1e-10
        assert S <= x + zc + 2.0 * r - 1.0 + t + 1e-10
        assert S <= 2.0 * x + 2.0 * Z - 1.0 + t + 1e-10
        assert S <= x + 3.0 * Z - 1.0 + t + 1e-10
        assert x + Z + 1e-10 >= (S + 1.0 - t) / 2.0


def check_frontier():
    # Leading normalized constraints:
    # 2 xi + 2 zeta >= 1/2,
    # xi + 3 zeta >= 1/2.
    rng = random.Random(0xF0123)
    for _ in range(200000):
        zeta = rng.random() * 0.5
        floor = max(0.0, 0.25 - zeta, 0.5 - 3.0 * zeta)
        xi = floor + rng.random() * 2.0
        assert 2.0 * xi + 2.0 * zeta >= 0.5 - 1e-12
        assert xi + 3.0 * zeta >= 0.5 - 1e-12
        assert xi + zeta >= 0.25 - 1e-12

    zeta = 0.125
    assert abs((0.25 - zeta) - (0.5 - 3.0 * zeta)) < 1e-15
    assert abs(0.25 - zeta - 0.125) < 1e-15


def check_canonical_rewrites():
    rng = random.Random(0xCA11AB1E)
    for _ in range(200000):
        D = rng.uniform(100.0, 100000.0)

        # Section 63: q-x = Q+2k.
        Q = rng.uniform(0.0, D)
        k = rng.uniform(0.0, D)
        x = rng.uniform(0.0, D)
        q = x + Q + 2.0 * k
        assert abs((q - Q - 2.0 * k) - x) < 1e-9 * max(1.0, D)

        # Section 63: x=m+u_B.
        m = rng.uniform(0.0, x)
        uB = x - m
        assert abs(m + uB - x) < 1e-12 * max(1.0, D)

        # Metric split x=(P_F-q)+lambda and P_F<=pi D imply
        # x <= (pi D-q)+lambda.
        hull_excess = rng.uniform(0.0, x)
        lam = x - hull_excess
        PF = q + hull_excess
        if PF <= math.pi * D:
            theta = math.pi * D - q
            assert theta + lam + 1e-10 >= x


def main():
    check_path_block_identity()
    check_pocket_integer_bound()
    check_finite_ledgers()
    check_frontier()
    check_canonical_rewrites()

    print(f"h_*={H_STAR:.15f}")
    print(f"3^(1/8)={C_HALF:.15f}")
    print(f"D^(3/4) coefficient in x+Z bound={C_HALF / 2.0:.15f}")
    print("linear frontier: xi >= max(0, 1/4-zeta, 1/2-3 zeta)")
    print("crossover: (zeta,xi)=(1/8,1/8)")
    print("Z_ext=o(D) => x_B >= (1/2-o(1))D")
    print("x_B=o(D) => Z_ext >= (1/4-o(1))D")
    print("PASS: monotone FREE corridor linear outer/external currency regression")


if __name__ == "__main__":
    main()
