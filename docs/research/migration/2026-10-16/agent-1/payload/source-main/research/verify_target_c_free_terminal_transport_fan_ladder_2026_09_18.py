#!/usr/bin/env python3
"""Regression checks for the terminal FREE transport fan ladder."""

from __future__ import annotations

import math
import random

SQRT3 = math.sqrt(3.0)
S2 = math.sqrt(math.pi / (2.0 * SQRT3))
G = 0.007707
M = 4.0 * S2 + 2.0 * G
PSTAR = M / 5.0
ESTAR = (M - math.pi) / 2.0


def constants() -> None:
    assert abs(S2 - 0.9523128068639574) < 2e-15
    assert abs(M - 3.8246652274558293) < 3e-15
    assert abs(PSTAR - 0.7649330454911658) < 3e-15
    assert abs(ESTAR - 0.3415362869330181) < 3e-15

    expected = {
        1: (0.6283185307179586, 0.18479956785822313),
        2: (0.5941649020246569, 0.1697614005784734),
        3: (0.5372421875358205, 0.14652059660067834),
        4: (0.42339675855814773, 0.10584918963953693),
    }
    for k, (a_ref, c_ref) in expected.items():
        A = (math.pi - (k - 1) * PSTAR) / (6 - k)
        B = 2.0 / (6 - k)
        C = A / (3.0 + B)
        assert abs(A - a_ref) < 3e-15
        assert abs(C - c_ref) < 3e-15

    c3 = expected[3][1]
    c4 = expected[4][1]
    assert abs(3.0 * c3 - 0.43956178980203503) < 4e-15
    assert abs(4.0 * c4 - 0.42339675855814773) < 4e-15


def reduced_stability_checks(trials: int = 500_000) -> None:
    rng = random.Random(0xE99F4A)

    for _ in range(trials):
        eps = rng.random() * 0.2

        # Allocate the stability budget
        #   (2/5)(r+delta) + (1/5)a <= eps.
        wr, wd, wa, slack = [rng.random() for _ in range(4)]
        z = wr + wd + wa + slack
        wr, wd, wa = wr / z, wd / z, wa / z
        r = (5.0 / 2.0) * eps * wr
        delta = (5.0 / 2.0) * eps * wd
        a = 5.0 * eps * wa
        budget = 0.4 * (r + delta) + 0.2 * a
        assert budget <= eps + 2e-15

        f = (M + 2.0 * a - delta - r) / 5.0
        if f < 0.0:
            continue

        # Choose an admissible number n of superpentagonal faces and an outer-loop
        # density ell.  n<=r because every superpentagon contributes >=1 to Q-f.
        n = rng.random() * min(r, f)
        p5 = f - n
        ell = rng.random() * (math.pi + delta) / 2.0
        b = math.pi + delta

        # Worst-case all superpentagon endpoint degree is sent to O.
        super_degree = 5.0 * n + r
        e_bo = b - 2.0 * ell
        e_5o_lb = e_bo - super_degree

        # Exact transport difference E_BB-L=(4f+Q-b)/2.
        qdef = f + r
        diff = (4.0 * f + qdef - b) / 2.0
        diff_reduced = ESTAR + a - delta
        assert abs(diff - diff_reduced) < 3e-14
        assert diff >= ESTAR - 2.5 * eps - 3e-14

        for k in range(1, 5):
            A = (math.pi - (k - 1) * PSTAR) / (6 - k)
            B = 2.0 / (6 - k)

            # Incidence lower bound before replacing n by r.
            y_exact_lb = (e_5o_lb - (k - 1) * p5) / (6 - k)

            # Weaker closed form after n<=r.
            y_closed = (
                b
                - 2.0 * ell
                - (k - 1) * f
                - (7 - k) * r
            ) / (6 - k)
            assert y_exact_lb + 2e-14 >= y_closed

            y_reduced = (
                A
                - B * ell
                + (k + 4) * delta / (5.0 * (6 - k))
                - 1.2 * r
                - 2.0 * (k - 1) * a / (5.0 * (6 - k))
            )
            assert abs(y_closed - y_reduced) < 5e-14
            assert y_reduced + 3e-14 >= A - B * ell - 3.0 * eps

            # Add the exact full-flower loss <=2S and verify the minimax.
            s = rng.random() * max(0.0, p5 / 2.0 + 0.5)
            y_full_lb = y_reduced - 2.0 * s
            Ceps = (A - 3.0 * eps) / (3.0 + B)
            x = max(s, ell, y_full_lb)
            assert x + 5e-14 >= Ceps


def finite_integer_incidence_checks(trials: int = 250_000) -> None:
    """Check the finite face/outer-incidence inequalities on random ledgers."""
    rng = random.Random(0x20260918)
    for _ in range(trials):
        p5 = rng.randint(0, 400)
        nsup = rng.randint(0, 150)
        excesses = [rng.randint(1, 8) for _ in range(nsup)]
        r = sum(excesses)
        f = p5 + nsup
        Q = f + r
        super_degree = sum(5 + x for x in excesses)
        assert super_degree == 5 * nsup + r
        assert nsup <= r if nsup else r == 0

        # Choose outer incidences subject only to face degree capacities.
        pent_o = [rng.randint(0, 5) for _ in range(p5)]
        super_o = [rng.randint(0, 5 + x) for x in excesses]
        e5o = sum(pent_o)
        ebo = e5o + sum(super_o)

        # Add arbitrary outer loops.  This defines b by the exact outer handshake.
        lo = rng.randint(0, 300)
        b = ebo + 2 * lo

        # Pair the remaining bounded incidences abstractly only for handshake algebra.
        bounded_degree = 5 * p5 + super_degree
        rem = bounded_degree - ebo
        if rem < 0 or rem % 2:
            continue
        ebb = rem // 2
        assert 2 * ebb + ebo == 4 * f + Q
        assert ebo + 2 * lo == b
        assert 2 * (ebb - lo) == 4 * f + Q - b

        for k in range(1, 6):
            yk = sum(o >= k for o in pent_o)
            assert e5o <= (k - 1) * p5 + (6 - k) * yk
            rhs = b - 2 * lo - (k - 1) * f - r - (6 - k) * nsup
            assert (6 - k) * yk >= rhs


def main() -> None:
    constants()
    reduced_stability_checks()
    finite_integer_incidence_checks()
    print("terminal FREE transport fan ladder: PASS")
    print(f"s2={S2:.15f}")
    print(f"M*={M:.15f}")
    print(f"p*={PSTAR:.15f}")
    print(f"e*={ESTAR:.15f}")
    for k in range(1, 5):
        A = (math.pi - (k - 1) * PSTAR) / (6 - k)
        B = 2.0 / (6 - k)
        C = A / (3.0 + B)
        print(f"k={k} A={A:.15f} C={C:.15f} kC={k*C:.15f}")


if __name__ == "__main__":
    main()
