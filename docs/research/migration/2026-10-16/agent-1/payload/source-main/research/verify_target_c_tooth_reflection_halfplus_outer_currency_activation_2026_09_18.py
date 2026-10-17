#!/usr/bin/env python3
"""Arithmetic/regression checks for the half-plus outer-currency/contact-activation note."""

import math
import random

h = math.sqrt(303.0) / 52.0
c = 0.129220199818177
delta = 2.0 * (1.0 - math.cos(c / 2.0))

assert 0.3347 < h < 0.3348
assert 0.00417 < delta < 0.00418


def coeffs(K: float, J: float):
    assert K > h and J > h
    alpha = 1.0 - h / K
    mu = 1.0 + delta * alpha / 4.0 - h / J
    matching = mu / 2.0
    activation = matching / 6.0
    return alpha, mu, matching, activation


alpha400, mu400, m400, a400 = coeffs(400.0, 400.0)
assert abs(mu400 - 1.0002055102299623) < 1e-14
assert abs(m400 - 0.5001027551149811) < 1e-14
assert abs(a400 - 0.08335045918583019) < 1e-14

mu_inf = 1.0 + delta / 4.0
m_inf = 0.5 + delta / 8.0
a_inf = m_inf / 6.0
h_if_zext_sublinear = math.sqrt(3.0) * mu_inf / 2.0

assert abs(mu_inf - 1.0010432532581182) < 1e-14
assert abs(m_inf - 0.5005216266290591) < 1e-14
assert abs(a_inf - 0.08342027110484318) < 1e-14
assert abs(h_if_zext_sublinear - 0.8669288876085498) < 1e-14

# For J=400 the short-edge graph is below the sharp sqrt(2) crossing threshold
# once D exceeds this finite arithmetic threshold.
D0_400 = 400.0 / (math.sqrt(2.0) - 1.0)
assert 965.0 < D0_400 < 966.0
for D in (1000.0, 1e4, 1e6, 1e12):
    assert 1.0 + 400.0 / D < math.sqrt(2.0)

# OP algebra: Z_in <= 2 H/sqrt(3) - U/2 and 2M <= Z_in+Z_ext
# implies Z_ext + 2H/sqrt(3) - U/2 >= 2M.
rng = random.Random(20260918)
for _ in range(200000):
    H = rng.random() * 1000.0
    U = rng.random() * min(100.0, 4.0 * H / math.sqrt(3.0))
    zin_cap = 2.0 * H / math.sqrt(3.0) - U / 2.0
    zin = rng.random() * max(0.0, zin_cap)
    zext = rng.random() * 1000.0
    M = rng.random() * (zin + zext) / 2.0
    lhs = zext + 2.0 * H / math.sqrt(3.0) - U / 2.0
    assert lhs + 1e-12 >= 2.0 * M

print("half-plus outer-currency/contact-activation certificate: PASS")
print(f"h_* = {h:.15f}")
print(f"delta_* = {delta:.15f}")
print(f"mu_400 = {mu400:.15f}")
print(f"matching_400 = {m400:.15f}")
print(f"activation_400 = {a400:.15f}")
print(f"mu_inf = {mu_inf:.15f}")
print(f"activation_inf = {a_inf:.15f}")
print(f"sublinear-Z_ext H_out coefficient = {h_if_zext_sublinear:.15f}")
print(f"J=400 short-edge threshold D > {D0_400:.6f}")
