#!/usr/bin/env python3
"""Regression certificate for full-shore deep force-block retuning."""

from fractions import Fraction
from math import ceil

C = 1_109_000
c = Fraction(113, 5_000_000)
c0 = Fraction(113, 20_000_000)
b = Fraction(1567, 10_000)

assert c == 4 * c0
assert c / 2 == 2 * c0
assert float(c / 2) == 1.13e-5


def lower_density(r: int, eta0: Fraction, etar: Fraction, rho: Fraction) -> Fraction:
    m = 2 * r + 1
    return c / 2 - eta0 - etar - 2 * m * rho


# FS.36--FS.38: the three chosen losses sum exactly to epsilon.
for r in range(8):
    m = 2 * r + 1
    eps = c / 37
    eta0 = eps / 4
    etar = eps / 4
    rho = eps / (4 * m)
    assert lower_density(r, eta0, etar, rho) == c / 2 - eps

    T0 = 1 + ceil(float(4 * c / eps))
    Tr = max(T0, 1 + ceil(float(4 * m * c / eps)))
    assert c / T0 < eta0
    assert m * c / Tr < etar


# FS.40--FS.45: 90% of c/2 retained, uniformly for fixed r.
for r in range(12):
    m = 2 * r + 1
    eta0 = c / 80
    etar = c / 80
    rho = c / (80 * m)
    T0 = 81
    Tr = 80 * m + 1

    assert c / T0 < eta0
    assert m * c / Tr < etar
    assert lower_density(r, eta0, etar, rho) == Fraction(9, 20) * c
    assert Fraction(9, 20) * c == Fraction(1017, 100_000_000)
    assert abs(float(rho) - 2.825e-7 / m) < 1e-20

assert 81 * C == 89_829_000

K81 = 81 * C / float(b) + 3.004e6
assert 5.762e8 < K81 < 5.763e8


# A forbidden interface contaminates at most m=2r+1 radius-r centers.
def contaminated_centers(n: int, r: int, forbidden: set[int]) -> set[int]:
    out = set()
    for i in range(r, n - r):
        if any(j in forbidden for j in range(i - r, i + r + 1)):
            out.add(i)
    return out


for n in range(1, 15):
    max_r = min(4, max(1, (n + 1) // 2))
    for r in range(max_r):
        m = 2 * r + 1
        for mask in range(1 << n):
            forbidden = {j for j in range(n) if (mask >> j) & 1}
            assert len(contaminated_centers(n, r, forbidden)) <= m * len(forbidden)


# Conservative union bound used in the proof: center-bad deletions are charged once,
# window-forbidden interfaces are charged at most m times, and the shore ends cost 2r.
for n in range(1, 13):
    max_r = min(3, max(1, (n + 1) // 2))
    for r in range(max_r):
        m = 2 * r + 1
        eligible = set(range(r, max(r, n - r)))
        end_loss = n - len(eligible)
        assert end_loss <= min(n, 2 * r)
        for mask in range(1 << n):
            center_bad = {j for j in range(n) if (mask >> j) & 1}
            narrow = {j for j in range(n) if (3 * j + mask) % 5 == 0}
            sep = {j for j in range(n) if (5 * j + 2 * mask) % 7 == 0}
            window_forbidden = narrow | sep
            deleted_eligible = (
                (center_bad & eligible)
                | contaminated_centers(n, r, window_forbidden)
            )
            assert len(deleted_eligible) <= min(
                len(eligible),
                len(center_bad) + m * len(window_forbidden),
            )

print("PASS: full-shore deep force-block retuning arithmetic and covering bounds")
print(f"c/2 = {float(c/2):.12g}")
print(f"90% retained density = {float(Fraction(9,20)*c):.12g}")
print(f"T0=81 grid coefficient = {K81:.6f}")
print(f"T0=81 center reaction cap = {81*C}")
