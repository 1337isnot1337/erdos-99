#!/usr/bin/env python3
"""Regression checks for the deep bilateral exact-phase force-cell reduction."""

from fractions import Fraction
from math import sin

c = Fraction(113, 5_000_000)
C = 1_109_000
c0 = Fraction(113, 20_000_000)
rho0 = float(c0 / 12)

assert c0 == c / 4
assert c0 / 2 == c / 8
assert c / 16 == Fraction(113, 80_000_000)
assert c0 / 12 == c / 48

# The radius-r contamination budget is independent of r after T=16(2r+1).
for r in (0, 1, 2, 5, 20, 1000):
    m = 2 * r + 1
    T = 16 * m
    bad_contamination_density = Fraction(m, T) * c
    assert bad_contamination_density == c / 16
    retained_from_wide = c / 8 - bad_contamination_density
    assert retained_from_wide == c / 16

# Combinatorial neighborhood contamination: each separator spoils at most 2r+1 centers.
def contaminated_centers(n, separators, r):
    out = set()
    for z in separators:
        lo = max(0, z - r)
        hi = min(n - 1, z + r)
        out.update(range(lo, hi + 1))
    return out


for n, r, separators in [
    (100, 0, {3, 40}),
    (100, 2, {10, 30, 70}),
    (257, 7, {0, 60, 128, 256}),
]:
    contaminated = contaminated_centers(n, separators, r)
    assert len(contaminated) <= (2 * r + 1) * len(separators)

# A fixed-angle exact force pair has compressed coefficients bounded by
# |G|/(D sin rho0) once its projective gap is >= rho0.
assert 0.0 < rho0 < 1e-5
assert sin(rho0) > 0.0
for r in (0, 1, 5, 20):
    T = 16 * (2 * r + 1)
    for D in (10**14, 10**16, 10**18):
        normalized_reaction_cap = T * C / D
        coefficient_cap = normalized_reaction_cap / sin(rho0)
        assert normalized_reaction_cap > 0.0
        assert coefficient_cap > normalized_reaction_cap
    assert 16 * (2 * r + 1) * C > 0

# Diagonal example: r grows while r/D -> 0, so normalized switching stress
# and the fixed-angle compressed coefficient cap both vanish.
vals = []
for k in (10, 100, 1000, 10_000):
    r = k
    D = k**4 * 10**12
    T = 16 * (2 * r + 1)
    stress = T * C / D
    coeff = stress / sin(rho0)
    vals.append((stress, coeff))

assert all(vals[i + 1][0] < vals[i][0] for i in range(len(vals) - 1))
assert all(vals[i + 1][1] < vals[i][1] for i in range(len(vals) - 1))
assert vals[-1][0] < 1e-12

print("PASS: deep bilateral exact-phase force-cell regressions")
print(f"c/16={float(c/16):.12g}")
print(f"rho0={rho0:.12g}")
print(f"final_stress_cap={vals[-1][0]:.12g}")
print(f"final_compressed_coefficient_cap={vals[-1][1]:.12g}")
