#!/usr/bin/env python3
"""Exact certificates for a two-wave odd-shell fold and two isolate blockers.

The infinite-family argument is in the report. Directed integer intervals
certify the displayed finite shells; polynomial arithmetic proves contact
identities. Cloud separation uses the positive integral triangular-lattice
norm, rather than extrapolating pair samples. No global optimum is asserted.
"""
from fractions import Fraction as F
from itertools import combinations
from math import isqrt
import json
import verify_target_c_odd_shell_single_vertex_barriers_2026_10_06 as I


def poly_add(a, b):
    c = [F(0)] * max(len(a), len(b))
    for j, x in enumerate(a):
        c[j] += x
    for j, x in enumerate(b):
        c[j] += x
    while c and not c[-1]:
        c.pop()
    return c


def poly_scale(a, s):
    return [x * s for x in a]


def poly_mul(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            c[j + k] += x * y
    while c and not c[-1]:
        c.pop()
    return c


def contact_identities():
    one, c, a, b, side = [F(1)], [F(1), F(-2)], [F(1), F(-4)], [
        F(1), F(-12), F(16)], [F(0), F(4)]
    aa, bb = poly_mul(a, a), poly_mul(b, b)
    af = poly_add(poly_add(aa, one), poly_scale(poly_mul(a, c), -2))
    ab = poly_add(poly_add(aa, bb), poly_scale(poly_mul(poly_mul(a, b), c), -2))
    ff = poly_scale(poly_add(one, poly_scale(c, -1)), 2)
    assert af == ab == ff == side
    assert poly_add(poly_scale(poly_mul(a, c), 2), [-F(1)]) == b
    assert F(1) - 12 * F(1, 36) + 16 * F(1, 36) ** 2 > F(2, 3)
    return 4


def rotation(p, c, s):
    return (I.sub(I.mul(c, p[0]), I.mul(s, p[1])),
            I.add(I.mul(s, p[0]), I.mul(c, p[1])))


def distance(p, q):
    return I.distance_bounds(p, q)


def case(q, pi_lo, pi_hi):
    sa = I.trig_interval(pi_lo / q, pi_hi / q, True)
    ca = I.trig_interval(pi_lo / q, pi_hi / q, False)
    c2 = I.trig_interval(2 * pi_lo / q, 2 * pi_hi / q, False)
    s2 = I.trig_interval(2 * pi_lo / q, 2 * pi_hi / q, True)
    radius = I.inv(I.scale(sa, 2))
    assert radius[0] > 10 * I.Q
    inv_r = I.inv(radius)
    t = I.mul(sa, sa)
    a = I.sub(I.rat(1), I.scale(t, 4))
    b = I.add(I.sub(I.rat(1), I.scale(t, 12)), I.scale(I.mul(t, t), 16))
    assert b[0] > I.rat(F(2, 3))[1]
    assert a[0] > b[1]
    # D=1/(2 sin(alpha/2)).
    sh = I.trig_interval(pi_lo / (2 * q), pi_hi / (2 * q), True)
    diam = I.inv(I.scale(sh, 2))
    dsq = I.mul(diam, diam)
    units = []
    p = (I.rat(1), I.rat(0))
    for _ in range(q):
        units.append(p)
        p = rotation(p, c2, s2)
    wall = [I.p_mul(p, radius) for p in units]
    m = (q - 1) // 2
    factors = [a if j % 2 == 0 else b for j in range(q)]
    factors[-2:] = [I.rat(1), I.rat(1)]
    moved = [I.p_mul(p, factor) for p, factor in zip(wall, factors)]
    counts = dict(old_noncontact_pairs=0, old_nondiameter_pairs=0,
                  new_noncontact_pairs=0, new_upper_pairs=0,
                  old_blocker_wall_pairs=0, blocker_endpoint_pairs=0,
                  collided_endpoint_incidences=0, blocked_rotated_folds=0)
    unit_sq = I.Q ** 2
    for j, k in combinations(range(q), 2):
        gap = min(k - j, q - (k - j))
        old, new = distance(wall[j], wall[k]), distance(moved[j], moved[k])
        if gap == 1:
            assert old[0] <= unit_sq <= old[1]
            assert new[0] <= unit_sq <= new[1]
        else:
            assert old[0] > unit_sq
            assert new[0] > unit_sq
            counts["old_noncontact_pairs"] += 1
            counts["new_noncontact_pairs"] += 1
        if gap == m:
            assert old[0] <= dsq[1] * I.Q and old[1] >= dsq[0] * I.Q
        else:
            assert old[1] < dsq[0] * I.Q
            counts["old_nondiameter_pairs"] += 1
        assert new[1] < dsq[0] * I.Q
        counts["new_upper_pairs"] += 1

    # Identical paired midpoint construction to Audit.65, but only two sides.
    delta = I.scale(I.mul(inv_r, inv_r), F(1, 100))
    root = I.root(I.sub(I.mul(I.add(I.rat(1), delta),
                                 I.add(I.rat(1), delta)), I.rat(F(1, 4))))
    br = I.sub(I.mul(radius, ca), root)
    assert br[0] > I.sub(radius, I.rat(2))[1]
    # Unit midpoint directions on sides (0,1) and (2,3).
    direction = (ca, sa)
    blockers = [I.p_mul(direction, br)]
    direction = rotation(rotation(direction, c2, s2), c2, s2)
    blockers.append(I.p_mul(direction, br))
    blocker_pair = distance(*blockers)
    assert blocker_pair[0] > unit_sq and blocker_pair[1] < dsq[0] * I.Q
    for z in blockers:
        for p in wall:
            bounds = distance(z, p)
            assert bounds[0] > unit_sq and bounds[1] < dsq[0] * I.Q
            counts["old_blocker_wall_pairs"] += 1

    # Every cyclic cut leaves exactly two consecutive vertices fixed.
    for cut in range(q):
        endpoint = [I.p_mul(wall[j], factors[(j - cut) % q]) for j in range(q)]
        witness = False
        for z in blockers:
            for p in endpoint:
                bounds = distance(z, p)
                assert bounds[1] < dsq[0] * I.Q
                counts["blocker_endpoint_pairs"] += 1
                if bounds[1] < unit_sq:
                    witness = True
                    counts["collided_endpoint_incidences"] += 1
        assert witness
        counts["blocked_rotated_folds"] += 1

    # Optional quadratic population of strict interior contact isolates.
    ell = F(1) + F(1, q * q)
    rho_lower = F(I.sub(radius, I.rat(3))[0], I.Q)
    bound = int(2 * rho_lower / ell) + 2
    cloud = []
    for i in range(-bound, bound + 1):
        for j in range(-bound, bound + 1):
            norm = i * i + i * j + j * j
            if ell * ell * norm < rho_lower * rho_lower:
                cloud.append((i, j))
    assert cloud
    # For every nonzero integral difference, the norm is a positive integer:
    # 4 norm=(2i+j)^2+3j^2. Thus all cloud pairs are strictly >1.
    assert ell > 1 and all(i * i + i * j + j * j >= 0 for i, j in cloud)
    assert I.sub(radius, I.rat(3))[0] > 0
    # Cloud-wall and cloud-blocker separation follows from these radial gaps.
    assert I.sub(br, I.rat(rho_lower))[0] > I.Q
    # Each cloud norm is strictly less than rho_lower, so equality here
    # still gives a strictly greater-than-three wall/cloud radial gap.
    assert I.sub(radius, I.rat(rho_lower))[0] >= 3 * I.Q
    assert 2 * rho_lower < F(diam[0], I.Q)
    assert I.add(br, I.rat(rho_lower))[1] < diam[0]
    assert I.add(radius, I.rat(rho_lower))[1] < diam[0]
    assert I.add(I.mul(radius, a), br)[1] < diam[0]
    # A conservative analytic Oler/translation-average population margin.
    # M-n >3*pi*R-(61/4)*pi-3>0 for R>10, pi>3.
    margin = I.sub(I.scale(I.mul(I.enclose(pi_lo, pi_hi), radius), 3),
                   I.add(I.scale(I.enclose(pi_lo, pi_hi), F(61, 4)), I.rat(3)))
    assert margin[0] > 0
    return dict(q=q, wall_contacts=q, actual_diameter_pairs=q,
                blockers=2, deep_contact_isolates=len(cloud),
                full_source_population=q + 2 + len(cloud),
                certified_population_margin_lower=str(F(margin[0], I.Q)), **counts)


def main():
    # Machin identity with alternating-series rational remainder bounds.
    x, y = I.atan_interval(F(1, 5)), I.atan_interval(F(1, 239))
    pi_lo, pi_hi = 16 * x[0] - 4 * y[1], 16 * x[1] - 4 * y[0]
    assert F(3) < pi_lo < pi_hi < F(22, 7)
    cases = [case(q, pi_lo, pi_hi) for q in (65, 101, 201)]
    print(json.dumps(dict(status="PASS", polynomial_identities=contact_identities(),
                          interval_arithmetic="canonical Audit.65 directed integer intervals",
                          cases=cases), indent=2))


if __name__ == "__main__":
    main()
