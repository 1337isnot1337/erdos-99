#!/usr/bin/env python3
"""Asymptotic arithmetic regressions for bilateral birth loading."""

from math import pi, sin, sqrt


def L(D: float) -> float:
    eta0 = (3.0 ** 0.25) * sqrt(D)
    return sqrt(D * eta0 + eta0 * eta0)


def same_side_bound(D: float, rho: float) -> float:
    denom = D * sin(rho / 2.0) - 2.0 * L(D)
    if denom <= 0.0:
        return float("inf")
    return pi * D / denom


# Use visible angular scales to verify convergence to pi/sin(rho/2).
for rho in (0.05, 0.1, 0.2):
    target = pi / sin(rho / 2.0)
    vals = [same_side_bound(D, rho) for D in (1e12, 1e16, 1e20)]
    assert vals[0] > vals[1] > vals[2] > target
    assert (vals[-1] - target) / target < 0.001

# At the much smaller proof scales the asymptotic threshold is enormous but
# still independent of D, which is exactly the theorem's point.
c0 = 113.0 / 20_000_000.0
rho = c0 / 32.0
target = pi / sin(rho / 2.0)
assert target > 1e7
assert target < 1e8

# L_D/D -> 0 with D^(-1/4) order.
for D in (1e8, 1e12, 1e16):
    assert L(D) / D < 0.02

print("PASS: bilateral wide-dipole birth-loading regressions")
print(f"rho=c0/32={rho:.12g}")
print(f"asymptotic_same_side_cap={target:.12g}")
print(f"L(1e16)/D={L(1e16)/1e16:.12g}")
