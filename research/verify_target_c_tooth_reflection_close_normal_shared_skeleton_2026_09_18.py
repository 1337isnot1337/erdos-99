#!/usr/bin/env python3
"""Regression checks for close-normal heavy reuse and opposite-trunk geometry."""

from __future__ import annotations

import math
import random


def check_circular_pigeonhole() -> None:
    random.seed(7)
    for r in (2, 3, 10, 100):
        for _ in range(200):
            angles = sorted(random.random() * 2.0 * math.pi for _ in range(r + 1))
            gaps = [angles[i + 1] - angles[i] for i in range(r)]
            gaps.append(2.0 * math.pi - angles[-1] + angles[0])
            assert min(gaps) <= 2.0 * math.pi / (r + 1) + 1e-12


def check_opposite_cone() -> None:
    for theta in (0.01, 0.05, 0.2, 0.8):
        a = theta / 2.0
        n1 = (math.cos(a), math.sin(a))
        n2 = (math.cos(a), -math.sin(a))
        for frac in (0.1, 0.3, 0.5, 0.7, 0.9):
            phi = math.pi / 2.0 - a + frac * theta
            u = (math.cos(phi), math.sin(phi))
            p1 = u[0] * n1[0] + u[1] * n1[1]
            p2 = u[0] * n2[0] + u[1] * n2[1]
            assert p1 > 0.0
            assert p2 < 0.0
            assert p1 <= math.sin(theta) + 1e-12
            assert -p2 <= math.sin(theta) + 1e-12


def check_close_pair_asymptotics() -> None:
    h_star = math.sqrt(303.0) / 52.0
    for m in (1e4, 1e8, 1e12):
        theta = 2.0 * math.pi / math.sqrt(m)
        slack_bound = 2.0 * h_star * math.sin(theta)
        stretch = 1.0 / math.cos(theta / 2.0)
        assert slack_bound < 5.0 / math.sqrt(m)
        assert stretch - 1.0 < 6.0 / m


def check_pair_incidence_constant() -> None:
    # If E_h >= (alpha/2)D heavy edges are assigned among C(m,2) pairs,
    # one pair receives at least alpha D/(m(m-1)) > alpha D/m^2.
    for m in (3, 10, 100, 1000):
        alpha = 0.6
        d = 1e9
        e_h = alpha * d / 2.0
        assigned = e_h / (m * (m - 1) / 2.0)
        assert assigned >= alpha * d / (m * m)


def main() -> None:
    check_circular_pigeonhole()
    check_opposite_cone()
    check_close_pair_asymptotics()
    check_pair_incidence_constant()
    print("PASS: close-normal shared-pair and opposite-trunk certificate")


if __name__ == "__main__":
    main()
