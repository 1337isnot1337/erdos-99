#!/usr/bin/env python3
"""Regression checks for the terminal-or-fixed-aperture corridor theorem."""

from fractions import Fraction as Q
import itertools
import math

c = Q(113, 5_000_000)
nu = c / 2
assert nu == Q(113, 10_000_000)
assert float(nu) == 1.13e-5

# Coupled host-margin constant.
c_H = 0.453819885927
gamma_H = math.asin(c_H)

# Terminal-dominant branch: M=(nu-o(1))D gives two C67 gaps per TT cell.
terminal_angle = 2 * gamma_H + 2 * float(nu)
terminal_chord = math.sin(gamma_H + float(nu))
assert 0.94211 < terminal_angle < 0.94213
assert 0.45382 < terminal_chord < 0.45384

# Full-parent aperture nu gives one common central disk and the endpoint-separation
# scale from the wide-dipole central-diamond theorem.
central_disk = 0.5 * math.sin(float(nu) / 2)
endpoint_sep = math.sin(float(nu) / 2)
assert 2.8249e-6 < central_disk < 2.8251e-6
assert 5.6499e-6 < endpoint_sep < 5.6501e-6

# Exact block-packing inequality. If a binary interval has L good positions and H
# holes, cutting each good run into m-blocks gives
# K*m >= L-(H+1)(m-1).
def packed_blocks(bits, m):
    runs = []
    cur = 0
    for bit in bits:
        if bit:
            cur += 1
        elif cur:
            runs.append(cur)
            cur = 0
    if cur:
        runs.append(cur)
    return sum(run // m for run in runs)

for n in range(1, 13):
    for bits in itertools.product((0, 1), repeat=n):
        L = sum(bits)
        H = n - L
        for m in range(1, n + 1):
            K = packed_blocks(bits, m)
            assert K * m >= L - (H + 1) * (m - 1)

# A fixed safe aperture rho*=nu/2 is eventually available on every non-TT cell.
# The compressed-force mass is therefore at most this fixed factor times the
# original switching KKT mass.
rho_safe = float(nu) / 2
coeff_factor = 2 / math.sin(rho_safe)
assert 353_900 < coeff_factor < 354_100

# Dense-grid flank constant inherited by the hole-free exact-phase block.
q0 = 0.6536 - 1.02 / math.sqrt(3)
assert 0.06470 < q0 < 0.06471

# Sample the slow-block schedule
# m=min(sqrt(D/(H+1)),sqrt(D/(T+1))).  For H=o(D), T=o(D), m grows while
# mH/D and mT/D vanish.  These finite samples are non-load-bearing regression
# checks of the stated algebraic schedule.
for D in (10**8, 10**10, 10**12):
    H = int(D ** 0.55)
    T = int(D ** 0.60)
    m = max(1, int(min(math.sqrt(D / (H + 1)), math.sqrt(D / (T + 1)))))
    assert m >= 1
    assert m * (H + 1) / D < 0.03
    assert m * (T + 1) / D < 0.03

print("PASS: terminal saturation or fixed-aperture vanishing-mass corridor")
print("nu =", float(nu))
print("2 gamma_H + 2 nu =", terminal_angle)
print("terminal chord coefficient =", terminal_chord)
print("common central-disk coefficient =", central_disk)
print("pair endpoint-separation coefficient =", endpoint_sep)
print("safe compressed-force factor =", coeff_factor)
print("common flank density q0 =", q0)
