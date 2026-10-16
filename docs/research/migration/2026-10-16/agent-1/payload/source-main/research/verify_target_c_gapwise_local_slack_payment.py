"""Check the displayed arithmetic for the Target-C gapwise local-slack note.

The proposition checked here is the numerical endpoint substitution in
``target_c_gapwise_local_slack_payment_2026-09-12.md``.  It evaluates the
circular-segment function, the audited local coefficient, the four group diameter
floors, and the resulting Section-161 weighted coefficient.

This is floating-point arithmetic on the displayed constants.  It checks no
geometric hypothesis, Type-II limit, harmonic-cell saturation, or global
minimum-diameter implication.  A passing run certifies only the arithmetic values
printed in the note.
"""

from __future__ import annotations

import math


def cap_segment(angle: float) -> float:
    """Area of a radius-1/2 circular segment with central angle ``angle``."""

    return (angle - math.sin(angle)) / 8.0


def main() -> None:
    theta = 2.704779235215494
    sigma = 0.0088
    phi = 2.0 * math.pi - 2.0 * theta
    g1 = theta - 10.0 * sigma / 3.0
    mu = math.sin(theta / 2.0)
    a0 = math.sqrt(3.0) / 2.0
    c_loc = 4.0 * math.sqrt(math.pi) / 5.0 + 2.0 / (5.0 * math.sqrt(a0))
    c_det = math.pi * (2.0 - math.sqrt(3.0)) / 4.0

    groups = [
        (0.4703752868004241, mu),
        (cap_segment(g1), math.sin(g1 / 2.0)),
        (cap_segment(phi), math.sin(phi / 2.0)),
        (cap_segment(phi), math.sin(phi / 2.0)),
    ]

    gains = []
    lambdas = []
    for area, diameter_floor in groups:
        local_area_charge = c_loc * math.sqrt(area)
        gains.append(max(0.0, local_area_charge - diameter_floor))
        lambdas.append(diameter_floor)

    moment_floor = sum(lambdas)
    weighted_floor = 3.0 * moment_floor + 2.0 * sum(gains) + c_det
    extra_large_gap_payment = 2.0 * gains[1]

    assert abs(phi - 0.8736268367485982) < 2e-15
    assert abs(g1 - 2.675445901882161) < 2e-15
    assert abs(mu - 0.9762439137425688) < 2e-15
    assert abs(c_loc - 1.8477910534538295) < 2e-15
    assert abs(moment_floor - 2.795313535512168) < 2e-15
    assert abs(gains[0] - 0.2910434605114113) < 2e-15
    assert abs(gains[1] - 0.0017373475624680) < 2e-15
    assert gains[2] == 0.0 and gains[3] == 0.0
    assert abs(extra_large_gap_payment - 0.0034746951249360) < 2e-15
    assert abs(weighted_floor - 9.181949026303494) < 2e-15

    print("gapwise local-slack arithmetic: OK")
    print(f"phi={phi:.15f} g1={g1:.15f}")
    print(f"moment_floor={moment_floor:.15f}")
    print(f"large_gap_gain={gains[1]:.15f}")
    print(f"weighted_floor={weighted_floor:.15f}")


if __name__ == "__main__":
    main()
