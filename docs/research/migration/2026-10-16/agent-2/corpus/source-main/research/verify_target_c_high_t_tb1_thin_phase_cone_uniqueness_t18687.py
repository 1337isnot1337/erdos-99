from math import cos, log, pi

# PU.1 midpoint-packing expression at the THIN shell scale.
A = 0.25
L = 10.0
limit = 2 * A + L * L
for D in (10**3, 10**4, 10**5, 10**6):
    value = D * D - (D - A / D) ** 2 * cos(L / D) ** 2
    assert value < limit + 1
    assert abs(value - limit) < 1


# Ideal train-step sectors on RP^1 after setting the row transverse phase to 0.
# Row steps occupy the middle sector; the two possible column phases occupy the
# other two sectors.  Their interiors are disjoint and cover RP^1 away from the
# three boundary directions.
sectors = [(0, pi / 3), (pi / 3, 2 * pi / 3), (2 * pi / 3, pi)]
for j, (a, b) in enumerate(sectors):
    x = (a + b) / 2
    membership = [lo < x < hi for lo, hi in sectors]
    assert sum(membership) == 1
    assert membership[j]


# Half-exponent macroscopic-guard theorem followed by the three-sector split
# and the sixteen-word guard-incidence split.
c = 1 / (2 * log(5))
coefficient = c / (3 * 16)
assert 0.006 < coefficient < 0.007
assert abs((1 - c * log(5)) - 0.5) < 1e-15


print("PASS: THIN phase-cone uniqueness regressions")
print("packing limit =", limit)
print("half-exponent sector+incidence coefficient =", coefficient)
