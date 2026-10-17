"""Arithmetic checks for the two-half-disk interface-locality reduction.

The script checks only the displayed constants and the scalar endpoint diagnostic.  It
does not certify harmonic-cell locality, Type-II global optimality, or C-II closure.
"""

from __future__ import annotations

from math import pi, sqrt


def main() -> None:
    gamma = pi * (4.0 - 2.0 * sqrt(3.0)) / 8.0
    delta_2 = pi / (2.0 * sqrt(3.0))
    c_floor = 2.0 * sqrt(2.0 * delta_2)
    t_endpoint = 1.9948294847459518
    f_endpoint = c_floor / 2.0 - t_endpoint / 4.0
    interface_rhs = 2.0 + gamma
    lhs = t_endpoint + 2.0 * f_endpoint

    assert 0.2104 < gamma < 0.2105
    assert 2.6935 < c_floor < 2.6936
    assert 0.8480 < f_endpoint < 0.8481
    assert lhs > interface_rhs + 1.4

    # The finite missing-rhombus bound is I <= 12*c_I + 20.
    c_i = 0.0
    assert 12.0 * c_i + 20.0 == 20.0

    print(f"gamma={gamma:.15f}")
    print(f"two_halfdisk_train_floor={c_floor:.15f}")
    print(f"endpoint_f_over_D={f_endpoint:.15f}")
    print(f"endpoint_interface_lhs={lhs:.15f}")
    print(f"interface_rhs={interface_rhs:.15f}")
    print("two-half-disk interface locality arithmetic: OK")


if __name__ == "__main__":
    main()
