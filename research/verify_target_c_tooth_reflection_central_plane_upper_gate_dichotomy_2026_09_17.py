import math

h = math.sqrt(303.0) / 52.0
C = 17.0 / 50.0
c = 3.0 ** (1.0 / 8.0)
rho = 0.129220199818177

assert h < C < 1.0
assert 1.0 / (2.0 * (1.0 + h)) > 0.3746
assert abs(rho / 4.0 - 0.03230504995454425) < 1e-15
assert abs(2.0 * c - 2.294405380879754) < 1e-12

# Eventually t_D <= h + D^{-1/3} < C.
gap = C - h
D0 = math.ceil(gap ** -3)
assert D0 < 7_000_000

# Fixed-slack midpoint radius and the tangent-line crossing calculation.
# For a pair of gate chords from slow-scale modules, each midpoint lies within
# L(D) of the full-source circumcenter.  The event equation and pre-center
# stopping rule give a normal component at most 2L(D)+O(1), hence tangent
# angular error asymptotic to 2*c*D^{-1/4}.
for D in (1e8, 1e12, 1e16, 1e20):
    eta = (3.0 ** 0.25) * math.sqrt(D)
    L = math.sqrt(D * eta + eta * eta + D * C / 2.0)
    # Conservative projective tangent error from |N.r| <= 2L + C.
    ratio = (2.0 * L + C) / (D - C)
    assert 0.0 < ratio < 1.0
    tang = math.asin(ratio)
    scaled = tang * D ** 0.25
    assert scaled < 2.40

    kappa = math.log(D)
    normal_gap = 2.0 * kappa * D ** -0.25
    line_gap = normal_gap - 2.0 * tang
    assert line_gap > 0.0

    # Supporting-line intersection is inside both finite segments once kappa grows.
    cross_dist = 2.0 * L / math.sin(line_gap)
    assert cross_dist < (D - C) / 2.0

    # Both original endpoints of a fixed-slack pair have radius D/2 + O(sqrt D).
    radial_lower = D - C - (D / 2.0 + eta)
    assert abs(radial_lower - (D / 2.0 - eta - C)) < max(1e-5, 1e-12 * D)

# Algebra of the first upper-gate event:
# D^2 = ell^2 - 2 tau <N,r> + tau^2, ell <= D
# -> <N,r> <= tau/2.  Check a range of feasible synthetic choices.
D = 1e9
for tau in (0.01, 0.1, 0.2, 0.33):
    for deficit in (1e-6, 0.01, min(0.1, tau / 2.0)):
        ell = D - deficit
        nproj = (ell * ell + tau * tau - D * D) / (2.0 * tau)
        assert nproj <= tau / 2.0 + 1e-7

print('PASS: central-plane / upper-gate reflection dichotomy arithmetic')
print(f'h_*={h:.15f}')
print(f'C_gate={C:.15f}, eventual D threshold < {D0}')
print(f'2*3^(1/8)={2*c:.15f}')
print(f'corridor leading coefficient={1/(2*(1+h)):.15f}')
print(f'four-way density coefficient={rho/4:.15f}')
