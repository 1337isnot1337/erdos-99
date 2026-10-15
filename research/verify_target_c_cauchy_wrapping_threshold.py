#!/usr/bin/env python3
"""Numerical regression for the Cauchy wrapping-threshold candidate."""

import math


def main() -> None:
    mu_4 = 0.9362157414095831661
    mu_5 = math.sqrt(1.0 - (math.pi / 9.0) ** 2)
    theta_5 = 2.0 * math.asin(mu_5)

    assert abs(mu_5 - 0.9370981976747776) < 5e-15
    assert mu_5 > mu_4
    assert abs(9.0 * math.cos(theta_5 / 2.0) - math.pi) < 5e-15
    assert abs(4.5 * math.sin(theta_5) - math.pi * mu_5) < 5e-14

    print(f"theta_5={theta_5:.16f}")
    print(f"mu_5={mu_5:.16f}")
    print(f"mu_5-mu_4={mu_5 - mu_4:.16e}")


if __name__ == "__main__":
    main()
