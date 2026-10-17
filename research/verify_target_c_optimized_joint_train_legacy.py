#!/usr/bin/env python3
"""Scalar/count regression for the historical optimized joint-train candidate (original Section-112 label).

This checks the explicit numerical margins of that historical candidate. It does not certify the
geometric Section-107 area theorem or the Section-104 leakage theorem.
"""

from __future__ import annotations

import math

PI = math.pi
THETA8 = 2.702908029648367683220623341533134077952
MU8 = 0.9760407652670519820547242095879740469844
SIGMA_TARGET = 4.5e-4
R = 0.472
C_T = 1.827
SHORE = 0.085
ENDPOINT_DENSITY = 2.0 * SHORE
H = 0.0278
RHO = 0.0415
K = 5000.0
M = 500.0
C_PHASE = 5.317


def sigma(theta: float) -> float:
    return 3.0 * theta - 2.0 * PI - math.sin(theta / 2.0) - 2.0 * math.sin(theta)


def root(target: float) -> float:
    lo = THETA8
    hi = THETA8 + 0.1
    for _ in range(160):
        mid = (lo + hi) / 2.0
        if sigma(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def w(h: float) -> float:
    return PI / 3.0 - math.acos((1.0 + h) / 2.0)


def main() -> None:
    theta16 = root(SIGMA_TARGET)
    mu16 = math.sin(theta16 / 2.0)
    U = 3.0 * theta16 - 2.0 * PI
    train_ceiling = U + 2.0 * SIGMA_TARGET

    assert abs(theta16 - 2.7030037360312496) < 5e-15
    assert abs(mu16 - 0.9760511764172872) < 5e-15
    assert mu16 - MU8 > 1.041e-5
    assert abs(sigma(theta16) - SIGMA_TARGET) < 5e-15

    # Exact Section-82/89 ledger leaves a fixed train-budget margin.
    assert train_ceiling < C_T
    shore_limit = R / (3.0 * C_T)
    assert SHORE < shore_limit

    # Finite joint-shore extraction. The O(D) phase cut is absorbed by retaining
    # 0.4719 D^2 from the 0.472 D^2 rhombus floor for sufficiently large D.
    retained = 0.4719
    good_internal = (1.0 - 1.0 / M) * (retained - C_PHASE / K) / 3.0
    bad_bin_capacity = SHORE * C_T
    assert good_internal > bad_bin_capacity
    assert good_internal - bad_bin_capacity > 0.0013

    # Section-104 leakage with h=0.0278.
    leakage = w(H) + (1.0 / H + 169.0 / 6.0) * SIGMA_TARGET
    principal_per_corridor = (ENDPOINT_DENSITY - leakage) / 3.0
    assert principal_per_corridor > RHO

    # Exact-cosine projection contradiction.
    delta = math.acos(1.0 - SIGMA_TARGET / RHO)
    geometric_floor = THETA8 / 2.0 - PI / 3.0 - (73.0 / 6.0) * SIGMA_TARGET
    margin = geometric_floor - 2.0 * delta
    assert margin > 0.0039

    print(f"theta_16={theta16:.16f}")
    print(f"mu_16={mu16:.16f}")
    print(f"mu_16-mu_8={mu16 - MU8:.16e}")
    print(f"train_ceiling={train_ceiling:.16f}")
    print(f"shore_limit={shore_limit:.16f}")
    print(f"good_internal_density={good_internal:.16f}")
    print(f"bad_bin_capacity={bad_bin_capacity:.16f}")
    print(f"leakage={leakage:.16f}")
    print(f"principal_per_corridor={principal_per_corridor:.16f}")
    print(f"projection_delta={delta:.16f}")
    print(f"geometric_floor={geometric_floor:.16f}")
    print(f"final_margin={margin:.16f}")


if __name__ == "__main__":
    main()
