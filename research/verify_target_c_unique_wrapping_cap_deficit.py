#!/usr/bin/env python3
"""Scalar regression for canonical Target C Section 103.

This checks only the explicit cap-deficit and local constants. It does not certify the
convex-geometric uniqueness or the cutoff/diagonal argument.
"""

from __future__ import annotations

import math

PI = math.pi
THETA8 = 2.7029080296483676832206233415
MU8 = 0.9760407652670519820547242096


def cap_capacity(mu: float) -> float:
    theta = 2.0 * math.asin(mu)
    k = math.floor(2.0 * PI / theta)
    r = 2.0 * PI - k * theta
    return (2.0 * PI - k * math.sin(theta) - math.sin(r)) / 8.0


def main() -> None:
    assert abs(math.sin(THETA8 / 2.0) - MU8) < 5e-15
    c8 = cap_capacity(MU8)
    gamma8 = PI / 4.0 - c8
    assert abs(c8 - 0.583078407956923) < 5e-15
    assert abs(gamma8 - 0.202319755440525) < 5e-15

    # One concrete fixed neighborhood in which the coarse Section-103 constants hold.
    theta_hi = THETA8 + 0.03
    mu_hi = math.sin(theta_hi / 2.0)
    gamma_hi = PI / 4.0 - cap_capacity(mu_hi)
    alpha_hi = (3.0 * theta_hi - 2.0 * PI) / 2.0
    assert mu_hi < 0.979195
    assert gamma_hi > 0.1905
    assert alpha_hi < 0.958

    c_phase = PI**2 * math.sqrt(3.0) * (2.0 + math.sqrt(3.0)) / 12.0
    assert c_phase < 5.317

    print(f"mu8={MU8:.16f}")
    print(f"C(mu8)={c8:.16f}")
    print(f"Gamma(mu8)={gamma8:.16f}")
    print(f"mu(theta8+0.03)={mu_hi:.16f}")
    print(f"Gamma(theta8+0.03)={gamma_hi:.16f}")
    print(f"alpha_ceiling(theta8+0.03)={alpha_hi:.16f}")
    print(f"C_phase={c_phase:.16f}")


if __name__ == "__main__":
    main()
