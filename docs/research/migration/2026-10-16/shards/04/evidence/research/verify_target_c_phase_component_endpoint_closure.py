#!/usr/bin/env python3
"""Check the scalar margin in the Target C phase-component endpoint theorem.

The mathematical inequality is proved in
docs/reports/target_c_phase_component_endpoint_closure_2026-09-12.md.  This script
checks only its displayed Section-118 endpoint arithmetic: the wrapping-carrier area
floor, the principal-route upper currency, the correlated bad-train density, and the
strict contradiction when the total number of inverse-diameter phase windows is at
most three.

It uses binary64 arithmetic for diagnostics.  It intentionally omits the global
phase-window premise, KKT realizability, source optimality, and contact-isolated
source points outside the carrier.  A passing run is not a C-II or Level-I proof.
"""

from __future__ import annotations

import math


PI = math.pi
SAFE_SIGMA = 8.8e-3
SAFE_AREA = 0.4703752868004241
SAFE_BAD = 0.1162704799276074
SAFE_THETA = 2.7047792352154936


def main() -> None:
    area = SAFE_AREA
    theta = SAFE_THETA
    sigma = SAFE_SIGMA
    chord_sum = math.sin(theta / 2.0) + 2.0 * math.sin(theta)
    route_upper = chord_sum + (16.0 / 3.0) * sigma
    endpoint_lower = 4.0 * math.sqrt(area)

    print(f"endpoint_lower={endpoint_lower:.16f}")
    print(f"principal_chord_sum={chord_sum:.16f}")
    print(f"principal_route_upper={route_upper:.16f}")
    print(f"bad_train_density={SAFE_BAD:.16f}")

    margins = []
    for windows in range(4):
        margin = endpoint_lower - route_upper - 2.0 * SAFE_BAD * windows
        margins.append(margin)
        print(f"windows={windows} margin={margin:.16f}")

    # The theorem uses windows <= 3; the displayed endpoint has a strict margin.
    assert margins[3] > 0.17
    assert margins[3] > 0.0

    # The route currency is below the full train endpoint lower bound even before
    # leakage is charged.  This guards against a sign reversal in PC.8.
    assert endpoint_lower > route_upper

    # Section-118's relaxed scalar quantities are reproduced here as fixed values;
    # retain the expected ordering in the theorem's endpoint arithmetic.
    assert 0.0 < SAFE_BAD < 0.2
    assert 0.0 < sigma < 0.01
    assert theta > PI / 2.0


if __name__ == "__main__":
    main()
