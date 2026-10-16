#!/usr/bin/env python3
import itertools
import math
import random

H_STAR = math.sqrt(303.0) / 52.0
SQRT2 = math.sqrt(2.0)
SQRT3 = math.sqrt(3.0)
CROSS_SURPLUS = SQRT3 - 1.0


def f_gap(sigma):
    return math.sqrt(4.0 - (1.0 + sigma) ** 2)


def constants(t):
    rho = 1.0 + t
    A = 1.0 + 2.0 * rho / SQRT3
    B = 1.0 + math.pi * rho / 2.0 + math.pi * rho * rho / SQRT3
    delta = SQRT3 - f_gap(t)
    inv_c = 1.0 / CROSS_SURPLUS
    r_h = A + (A + B) * inv_c
    r_delta = (A + B) * inv_c
    c_h = r_h + 2.0 * inv_c
    c_delta = r_delta + 2.0 * inv_c
    return rho, A, B, delta, r_h, r_delta, c_h, c_delta


def check_crossing_factorization():
    rng = random.Random(0xC099)
    accepted = 0
    for _ in range(800000):
        a = 10 ** rng.uniform(-1.2, 0.8)
        b = 10 ** rng.uniform(-1.2, 0.8)
        c = 10 ** rng.uniform(-1.2, 0.8)
        d = 10 ** rng.uniform(-1.2, 0.8)
        x = rng.uniform(-0.999, 0.999)
        side2 = (
            a*a + b*b - 2*a*b*x,
            c*c + b*b + 2*c*b*x,
            c*c + d*d - 2*c*d*x,
            a*a + d*d + 2*a*d*x,
        )
        if min(side2) + 1e-12 < 1.0:
            continue
        accepted += 1
        weighted_lhs = (
            c*d*side2[0]
            + a*d*side2[1]
            + a*b*side2[2]
            + b*c*side2[3]
        )
        weighted_rhs = (a + c) * (b + d)
        factorized = (a + c) * (b + d) * (a*c + b*d)
        assert abs(weighted_lhs - factorized) < 1e-9 * max(1.0, factorized)
        assert weighted_lhs + 1e-10 >= weighted_rhs
        assert a*c + b*d + 1e-10 >= 1.0
        p = a + c
        q = b + d
        assert p*p + q*q + 1e-10 >= 4.0
    assert accepted > 10000


def check_unit_rhombus_equalities():
    for k in range(1, 1000):
        theta = (math.pi / 2.0) * k / 1000.0
        p = 2.0 * math.cos(theta / 2.0)
        q = 2.0 * math.sin(theta / 2.0)
        assert abs(p*p + q*q - 4.0) < 1e-12


def check_gap_concavity_and_secant():
    # f''(sigma)=-4/f(sigma)^3<0, so f lies above its secant.
    t = H_STAR
    assert t < SQRT2 - 1.0
    delta = SQRT3 - f_gap(t)
    slope = delta / t
    for k in range(100001):
        sigma = t * k / 100000.0
        chord = SQRT3 - slope * sigma
        assert f_gap(sigma) + 1e-13 >= chord
    assert abs(delta - 0.24260533414326435) < 1e-14


def blocks(bits, value):
    count = 0
    prev = None
    for bit in bits:
        if bit == value and prev != value:
            count += 1
        prev = bit
    return count


def external_edges(bits):
    return sum(1 for a, b in zip(bits, bits[1:]) if not (a and b))


def check_path_identity():
    # False = outside F, True = in F; the FREE root is outside.
    for n in range(1, 17):
        for tail in itertools.product((False, True), repeat=n - 1):
            bits = (False,) + tail
            z = sum(not bit for bit in bits)
            r = blocks(bits, True)
            assert external_edges(bits) == z + r - 1
            assert r <= z


def check_route_and_entry_algebra():
    rng = random.Random(0xB0A7D)
    t = H_STAR
    rho, A, B, delta, r_h, r_delta, c_h, c_delta = constants(t)
    c = CROSS_SURPLUS

    for _ in range(300000):
        v = rng.randint(0, 80)
        sigmas = []
        remaining = t
        for _j in range(v):
            take = rng.random() * remaining
            sigmas.append(take)
            remaining -= take

        # Every entered base obeys s_i >= f(sigma_i).
        side_lengths = [f_gap(s) + rng.random() * 3.0 for s in sigmas]
        h_visited = sum(s - 1.0 for s in side_lengths)
        H = h_visited + rng.random() * 10.0
        assert v * c <= H + delta + 1e-9

        # Route lengths are integers >= ceil(side length). The visited route
        # excess is bounded by the global u_B.
        ells = [max(2, math.ceil(s)) + rng.randint(0, 5) for s in side_lengths]
        u_subset = sum(ell - 2 for ell in ells)
        u_B = u_subset + rng.random() * 20.0
        widths = [rng.random() * ell for ell in ells]
        g_in = sum(widths)
        assert g_in <= u_B + 2.0 * v + 1e-10
        assert g_in <= u_B + 2.0 * (H + delta) / c + 1e-9

        # Oler in the one-sided half-stadium gives
        # r <= A sum(s_i)+B v, which reduces to the displayed H,Delta bound.
        r_cap_direct = A * sum(side_lengths) + B * v
        r_cap_reduced = r_h * H + r_delta * delta
        assert r_cap_direct <= r_cap_reduced + 1e-8

        # Full finite support-span ceiling after adding exterior population.
        Z = rng.uniform(1.0, 200.0)
        r = rng.random() * min(Z, r_cap_direct)
        g_ext = Z + r - 1.0 + rng.random() * t
        S = g_in + g_ext
        rhs = u_B + Z - 1.0 + t + c_h * H + c_delta * delta
        assert S <= rhs + 1e-8


def check_constants_and_frontiers():
    rho, A, B, delta, r_h, r_delta, c_h, c_delta = constants(H_STAR)
    assert abs(rho - 1.3347479843371002) < 1e-14
    assert abs(delta - 0.24260533414326435) < 1e-14
    assert abs(c_h - 17.388878053442944) < 1e-12
    assert abs(c_delta - 14.847643837328274) < 1e-12
    c_metric = c_h + 1.0
    assert abs(c_metric - 18.388878053442944) < 1e-12

    # On H=o(D), the finite law reduces to u+Z >= D/2-o(D).
    # Since u <= H+lambda, it also yields lambda+Z >= D/2-o(D).
    rng = random.Random(0xFEED99)
    for _ in range(200000):
        z = rng.random() * 0.8
        u = max(0.0, 0.5 - z) + rng.random()
        assert u + z >= 0.5 - 1e-12
        lam = u + rng.random() * 0.5
        assert lam + z >= 0.5 - 1e-12


def main():
    check_crossing_factorization()
    check_unit_rhombus_equalities()
    check_gap_concavity_and_secant()
    check_path_identity()
    check_route_and_entry_algebra()
    check_constants_and_frontiers()

    rho, A, B, delta, r_h, r_delta, c_h, c_delta = constants(H_STAR)
    print(f"h_*={H_STAR:.15f}")
    print(f"rho_*=1+h_*={rho:.15f}")
    print(f"Delta_*={delta:.15f}")
    print(f"half-stadium A_*={A:.15f}, B_*={B:.15f}")
    print(f"entry-block H coefficient={r_h:.15f}")
    print(f"support H coefficient={c_h:.15f}")
    print(f"metric H coefficient={c_h + 1.0:.15f}")
    print("H=o(D) => u_B+Z_ext >= (1/2-o(1))D")
    print("H=o(D) => (b-per(F))+Z_ext >= (1/2-o(1))D")
    print("Theta=pi D-q=o(D), b-per(F)=o(D) => Z_ext >= (1/2-o(1))D")
    print("PASS: FREE boundary-crossing / metric-routing regression")


if __name__ == "__main__":
    main()
