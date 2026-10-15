#!/usr/bin/env python3
"""Certify a full-source shell fold with transported Audit.65 collar isolates.

Uses exact contact identities and directed intervals from the two-wave
fold/Audit.65 checkers. All wall/collar pairs are checked explicitly; all
deep-cloud pairs are covered by exact lattice norms and radial bounds.
No fixture is claimed globally optimal.
"""
from fractions import Fraction as F
from itertools import combinations
import json
import verify_target_c_two_wave_shell_fold_2026_10_08 as W

I = W.I


def case(q, pi_lo, pi_hi):
    sa = I.trig_interval(pi_lo / q, pi_hi / q, True)
    ca = I.trig_interval(pi_lo / q, pi_hi / q, False)
    s2 = I.trig_interval(2 * pi_lo / q, 2 * pi_hi / q, True)
    c2 = I.trig_interval(2 * pi_lo / q, 2 * pi_hi / q, False)
    radius = I.inv(I.scale(sa, 2))
    inv_r = I.inv(radius)
    assert radius[0] > 10 * I.Q
    t = I.mul(sa, sa)
    a = I.sub(I.rat(1), I.scale(t, 4))
    b = I.add(I.sub(I.rat(1), I.scale(t, 12)), I.scale(I.mul(t, t), 16))
    target = I.sub(I.scale(radius, 2), inv_r)
    target_sq = I.mul(target, target)
    sh = I.trig_interval(pi_lo / (2 * q), pi_hi / (2 * q), True)
    diam = I.inv(I.scale(sh, 2))
    dsq = I.mul(diam, diam)
    assert target[1] < diam[0]

    p, units = (I.rat(1), I.rat(0)), []
    for _ in range(q):
        units.append(p)
        p = W.rotation(p, c2, s2)
    wall = [I.p_mul(p, radius) for p in units]
    factors = [a if j % 2 == 0 else b for j in range(q)]
    factors[-2:] = [I.rat(1), I.rat(1)]
    endpoint = [I.p_mul(p, f) for p, f in zip(wall, factors)]

    delta = I.scale(I.mul(inv_r, inv_r), F(1, 100))
    paired_radius = I.sub(I.mul(radius, ca), I.root(I.sub(
        I.mul(I.add(I.rat(1), delta), I.add(I.rat(1), delta)), I.rat(F(1, 4)))))
    single_radius = I.sub(I.sub(radius, I.rat(1)), delta)
    shift = I.scale(inv_r, 4)
    radii = []
    direction = (ca, sa)
    for _ in range((q - 1) // 2):
        wall.append(I.p_mul(direction, paired_radius))
        endpoint.append(I.p_mul(direction, I.sub(paired_radius, shift)))
        radii.append(paired_radius)
        direction = W.rotation(W.rotation(direction, c2, s2), c2, s2)
    wall.append(I.p_mul(units[-1], single_radius))
    endpoint.append(I.p_mul(units[-1], I.sub(single_radius, shift)))
    radii.append(single_radius)
    for rad in radii:
        assert I.sub(rad, shift)[0] > I.sub(radius, I.rat(F(3, 2)))[1]

    unit_sq = I.Q ** 2
    counts = dict(old_noncontact_pairs=0, new_noncontact_pairs=0,
                  strict_endpoint_upper_pairs=0, old_nondiameter_pairs=0)
    for j, k in combinations(range(len(wall)), 2):
        old = I.distance_bounds(wall[j], wall[k])
        new = I.distance_bounds(endpoint[j], endpoint[k])
        gap = min(k - j, q - (k - j)) if k < q else None
        if gap == 1:
            # Equality is independently given by the polynomial identities.
            assert old[0] <= unit_sq <= old[1]
            assert new[0] <= unit_sq <= new[1]
        else:
            assert old[0] > unit_sq and new[0] > unit_sq
            counts["old_noncontact_pairs"] += 1
            counts["new_noncontact_pairs"] += 1
        if gap == (q - 1) // 2:
            assert old[0] <= dsq[1] * I.Q and old[1] >= dsq[0] * I.Q
        else:
            assert old[1] < dsq[0] * I.Q
            counts["old_nondiameter_pairs"] += 1
        assert new[1] < target_sq[0] * I.Q
        counts["strict_endpoint_upper_pairs"] += 1

    ell = F(1) + F(1, q * q)
    rho = F(I.sub(radius, I.rat(3))[0], I.Q)
    bound = int(2 * rho / ell) + 2
    cloud = [(i, j) for i in range(-bound, bound + 1)
             for j in range(-bound, bound + 1)
             if ell * ell * (i * i + i * j + j * j) < rho * rho]
    assert ell > 1 and len(set(cloud)) == len(cloud) > 0
    # Positive integral lattice norm certifies all distinct cloud/cloud pairs.
    assert 2 * rho < F(target[0], I.Q)
    assert I.add(radius, I.rat(rho))[1] < target[0]
    assert I.sub(I.mul(radius, b), I.rat(rho))[0] > I.Q
    for rad in radii:
        new_rad = I.sub(rad, shift)
        assert I.sub(rad, I.rat(rho))[0] > I.Q
        assert I.sub(new_rad, I.rat(rho))[0] > I.Q
        assert I.add(rad, I.rat(rho))[1] < target[0]
        assert I.add(new_rad, I.rat(rho))[1] < target[0]
    return dict(q=q, transported_collar_isolates=len(radii),
                retained_deep_isolates=len(cloud), retained_wall_contacts=q,
                full_source_population=len(wall) + len(cloud),
                deep_cloud_pairs_certified=len(cloud) * (len(cloud) - 1) // 2,
                cloud_wall_collar_pairs_certified=len(cloud) * len(wall), **counts)


def main():
    x, y = I.atan_interval(F(1, 5)), I.atan_interval(F(1, 239))
    pi_lo, pi_hi = 16 * x[0] - 4 * y[1], 16 * x[1] - 4 * y[0]
    assert F(3) < pi_lo < pi_hi < F(22, 7)
    assert W.contact_identities() == 4
    assert F(3, 2) - F(27, 48 * 400) > F(7, 5)
    assert F(7, 5) * (1 - F(3, 20)) > 1
    assert F(8, 5) / 10 - F(5, 2) / 100 > 0
    print(json.dumps(dict(status="PASS", contact_identities=4,
                          cases=[case(q, pi_lo, pi_hi) for q in (65, 101, 201)]),
                     indent=2))


if __name__ == "__main__":
    main()
