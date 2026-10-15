#!/usr/bin/env python3
"""Numerical sanity checks for Target C Section 120.

This is only a regression for the local anisotropic return formula.  The theorem itself
is finite and proved symbolically in target_c_section120_anisotropic_two_arc_return.md.
"""

import math


def local_cost(q_angle: float, u_angle: float, v_angle: float) -> float:
    return 4.0 - 2.0 * (
        abs(math.cos(q_angle - u_angle)) + abs(math.cos(q_angle - v_angle))
    )


def main() -> None:
    universal = 4.0 - 2.0 * math.sqrt(3.0)
    averaged = 4.0 - 8.0 / math.pi

    assert averaged > universal

    # Grid-check the universal pointwise bound for strict-rhombus projective angles
    # phi in [pi/3, pi/2]. Equality is approached only at phi=pi/3.
    minimum = 10.0
    argmin = None
    for i in range(501):
        phi = math.pi / 3.0 + (math.pi / 2.0 - math.pi / 3.0) * i / 500.0
        for j in range(2000):
            q = math.pi * j / 2000.0
            c = local_cost(q, 0.0, phi)
            if c < minimum:
                minimum = c
                argmin = (phi, q)
    assert minimum >= universal - 1e-12
    assert abs(minimum - universal) < 1e-6

    # Uniform directional averaging is independent of the two train directions.
    for phi in (math.pi / 3.0, 1.2, math.pi / 2.0):
        n = 200000
        mean = sum(local_cost(math.pi * j / n, 0.0, phi) for j in range(n)) / n
        assert abs(mean - averaged) < 2e-5

    print(f"universal_constant={universal:.16f}")
    print(f"uniform_direction_average={averaged:.16f}")
    print(f"grid_minimum={minimum:.16f}")
    print(f"grid_argmin_phi={argmin[0]:.16f}")
    print(f"grid_argmin_q={argmin[1]:.16f}")


if __name__ == "__main__":
    main()
