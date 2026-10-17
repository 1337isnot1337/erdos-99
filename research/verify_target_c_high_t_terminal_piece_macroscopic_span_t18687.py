#!/usr/bin/env python3
"""Regression checks for terminal-piece macroscopic-span theorem."""

from fractions import Fraction as Q
import math
import random

# Current density constants from the physical-piece theorem.
c0 = Q(113, 20_000_000)
s0 = 7 * c0 / 16
mu0 = s0 / 6
assert mu0 == Q(791, 1_920_000_000)

lam = Q(5085, 1_000_000_000)  # 5.085e-6 exactly in decimal notation
mu_deep = lam / 3
assert float(mu_deep) == 1.695e-6

chord0 = float(mu0) / math.pi
angle0 = 2 * math.asin(chord0)
chord_deep = float(mu_deep) / math.pi
angle_deep = 2 * math.asin(chord_deep)

assert 1.311e-7 < chord0 < 1.312e-7
assert 2.622e-7 < angle0 < 2.624e-7
assert 5.395e-7 < chord_deep < 5.396e-7
assert 1.0790e-6 < angle_deep < 1.0792e-6

# Exact midpoint-transfer identity and lower bound on random synthetic data.
rng = random.Random(20260917)
for _ in range(5000):
    xa = (rng.uniform(-10, 10), rng.uniform(-10, 10))
    xb = (rng.uniform(-10, 10), rng.uniform(-10, 10))
    ma = (rng.uniform(-2, 2), rng.uniform(-2, 2))
    mb = (rng.uniform(-2, 2), rng.uniform(-2, 2))
    ya = (2 * ma[0] - xa[0], 2 * ma[1] - xa[1])
    yb = (2 * mb[0] - xb[0], 2 * mb[1] - xb[1])
    dx = math.hypot(xa[0] - xb[0], xa[1] - xb[1])
    dm = math.hypot(ma[0] - mb[0], ma[1] - mb[1])
    dy = math.hypot(ya[0] - yb[0], ya[1] - yb[1])
    assert dy + 1e-12 >= dx - 2 * dm

# Cauchy perimeter inequality on random cyclic point sets on ellipses.
# This is only a regression sanity check; the proof uses Cauchy's formula.
for _ in range(1000):
    n = rng.randint(3, 30)
    a = rng.uniform(1, 20)
    b = rng.uniform(0.1, a)
    angles = sorted(rng.uniform(0, 2 * math.pi) for _ in range(n))
    pts = [(a * math.cos(t), b * math.sin(t)) for t in angles]
    per = sum(
        math.hypot(pts[(i + 1) % n][0] - pts[i][0], pts[(i + 1) % n][1] - pts[i][1])
        for i in range(n)
    )
    diam = max(
        math.hypot(pts[j][0] - pts[i][0], pts[j][1] - pts[i][1])
        for i in range(n) for j in range(i + 1, n)
    )
    assert per <= math.pi * diam + 1e-10


# Direction-packing sharpening.
dir_chord0 = math.sin(float(mu0) / 2)
dir_angle0 = float(mu0)
dir_chord_deep = math.sin(float(mu_deep) / 2)
dir_angle_deep = float(mu_deep)
assert 2.0598e-7 < dir_chord0 < 2.0600e-7
assert 8.4749e-7 < dir_chord_deep < 8.4751e-7
assert dir_chord0 > chord0
assert dir_chord_deep > chord_deep

# Exhaustive discrete sanity checks for the short-diameter circle-packing lemma.
# This does not replace the proof in the Markdown note; it checks finite circular
# models with arbitrary point placement, including wraparound configurations.
from itertools import combinations
for N in range(9, 19):
    for sep in range(1, max(2, N // 6)):
        def gd(a, b):
            q = abs(a - b)
            return min(q, N - q)
        for m in range(2, min(6, N) + 1):
            target = (m - 1) * sep
            if target >= N / 3:
                continue
            for pts in combinations(range(N), m):
                if min(gd(a, b) for a, b in combinations(pts, 2)) < sep:
                    continue
                d = max(gd(a, b) for a, b in combinations(pts, 2))
                assert d >= target, (N, sep, m, pts, d, target)

# Finite-D error has the asserted o(D) scale.
eta_const = 3 ** 0.25
for D in (10**4, 10**6, 10**8, 10**10, 10**12):
    eta = eta_const * math.sqrt(D)
    L = math.sqrt(D * eta + eta * eta)
    assert L / D > 0
    # L/D decreases at the D^{-1/4} scale.
    if D >= 10**6:
        prevD = D // 100
        preveta = eta_const * math.sqrt(prevD)
        prevL = math.sqrt(prevD * preveta + preveta * preveta)
        assert L / D < prevL / prevD

print("PASS: terminal-piece macroscopic-span regressions")
print("unconditional terminal density =", float(mu0))
print("unconditional limiting chord-span coefficient =", chord0)
print("unconditional limiting angular-span lower bound =", angle0)
print("deep terminal density =", float(mu_deep))
print("deep limiting chord-span coefficient =", chord_deep)
print("deep limiting angular-span lower bound =", angle_deep)
print("C67 unconditional chord-span coefficient =", dir_chord0)
print("C67 unconditional angular-span coefficient =", dir_angle0)
print("C67 deep chord-span coefficient =", dir_chord_deep)
print("C67 deep angular-span coefficient =", dir_angle_deep)
