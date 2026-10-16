#!/usr/bin/env python3
"""Exact finite certificates for joint contact gains and overlap depth.

Encodes full-source distances, binary rigid owner translations, all old unit
contacts, singleton feasibility, and triangle absence in safe endpoint packets.
Checks the parallel interpolation identity and its sharp 1/4 deficit bound.
The owner-return packet has a connected conflict path and actual old contacts.
Omits actual O-O cut topology, vertex KKT, diameter ONE-SIGN hypotheses,
quadratic population, and global minimum-diameter optimality. Finite samples
corroborate the analytic proof; they do not prove the universal source theorem.
"""

from fractions import Fraction as F
from itertools import combinations, product


def add(p, q):
    return p[0] + q[0], p[1] + q[1]


def sub(p, q):
    return p[0] - q[0], p[1] - q[1]


def norm2(p):
    return p[0] ** 2 + p[1] ** 2


def distances(points):
    return {ij: norm2(sub(points[ij[0]], points[ij[1]]))
            for ij in combinations(range(len(points)), 2)}


def contacts(points):
    return {ij for ij, d in distances(points).items() if d == 1}


def triangle_free(edges, n):
    return not any({(i, j), (i, k), (j, k)} <= edges
                   for i, j, k in combinations(range(n), 3))


def moved(points, owners, delta, bits):
    return [add(p, delta[i]) if bits[i] else p
            for p, i in zip(points, owners)]


def check_safe_packet(delta):
    # In the joint state x-y=(1,0); each owner carries a vertical unit dimer.
    r = add((F(1), F(0)), sub(delta[1], delta[0]))
    points = [r, add(r, (F(0), F(1))),
              (F(0), F(0)), (F(0), F(-1))]
    owners = [0, 0, 1, 1]
    old_c = contacts(points)
    assert old_c == {(0, 1), (2, 3)}
    assert triangle_free(old_c, 4)
    old_diameter2 = max(distances(points).values())
    for bits in product((0, 1), repeat=2):
        p = moved(points, owners, delta, bits)
        assert min(distances(p).values()) >= 1
        assert old_c <= contacts(p)
        assert triangle_free(contacts(p), 4)
    final = moved(points, owners, delta, (1, 1))
    assert contacts(final) == old_c | {(0, 2)}
    assert max(distances(final).values()) < old_diameter2
    return r


def check_depth_samples():
    tested = 0
    for ai in range(1, 31):
        for bi in range(1, 31):
            a, b = F(ai, 100), F(bi, 100)
            for ti in range(-20, 21):
                r = F(199, 200), F(ti, 100)
                if norm2(r) <= 1:
                    continue
                ra, rb = add(r, (F(0), a)), sub(r, (F(0), b))
                if min(norm2(ra), norm2(rb)) < 1:
                    continue
                s = add(r, (F(0), a - b))
                depth_bound = min(a, b) * abs(a - b)
                assert norm2(s) > 1 - depth_bound
                assert depth_bound <= max(a, b) ** 2 / 4
                if a >= b:
                    identity = (b / a * norm2(r)
                                + (a - b) / a * norm2(ra) - b * (a - b))
                else:
                    identity = (a / b * norm2(r)
                                + (b - a) / b * norm2(rb) - a * (b - a))
                assert identity == norm2(s)
                tested += 1
    assert tested > 1000
    return tested


def check_sharpness():
    ratios = []
    for denominator in (50, 100, 1000):
        t = F(1, denominator)
        x, b = (1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)
        assert x * x + b * b == 1
        a = 2 * b
        for k in (2, 10, 100, 10000):
            c = x + (1 - x) / k
            r = c, -b
            assert norm2(r) > 1
            assert norm2(add(r, (F(0), a))) > 1
            assert norm2(sub(r, (F(0), b))) > 1
            s = add(r, (F(0), a - b))
            eta = 1 - norm2(s)
            assert 0 < eta < b * b == a * a / 4
            ratio = eta / (b * b)
            if k == 10000:
                assert ratio > F(999, 1000)
            ratios.append(ratio)
    return len(ratios)


def check_owner_return():
    c = 1 - F(1, 10**8)
    amplitudes = [F(1, 1000), F(3, 1000), F(5, 1000)]
    delta = [(F(0), a) for a in amplitudes]
    points, owners = [], []
    row_owners = [0, 1, 2, 0]
    for j, owner in enumerate(row_owners):
        p = j * c, -amplitudes[owner]
        points.extend((p, add(p, (F(0), F(1)))))
        owners.extend((owner, owner))
    old_c = {(2 * j, 2 * j + 1) for j in range(4)}
    assert contacts(points) == old_c
    assert min(distances(points).values()) >= 1
    for bits in product((0, 1), repeat=3):
        p = moved(points, owners, delta, bits)
        assert old_c == contacts(p)
        if sum(bits) <= 1:
            assert min(distances(p).values()) >= 1
    final = moved(points, owners, delta, (1, 1, 1))
    overlaps = {ij for ij, d in distances(final).items() if d < 1}
    expected = {(2 * j + row, 2 * (j + 1) + row)
                for j in range(3) for row in (0, 1)}
    assert overlaps == expected
    for i, j in overlaps:
        oi, oj = owners[i], owners[j]
        r = sub(points[i], points[j])
        a, b = amplitudes[oi], amplitudes[oj]
        assert norm2(r) > 1
        assert norm2(add(r, delta[oi])) > 1
        assert norm2(sub(r, delta[oj])) > 1
        eta = 1 - norm2(sub(final[i], final[j]))
        assert eta == 1 - c * c
        assert 0 < eta < min(a, b) * abs(a - b)
    # The bottom-row conflict path contracts to a directed owner triangle.
    arcs = [(row_owners[j], row_owners[j + 1]) for j in range(3)]
    assert arcs == [(0, 1), (1, 2), (2, 0)]
    coefficients = [0, 0, 0]
    for i, j in arcs:
        coefficients[i] -= 1
        coefficients[j] += 1
    assert coefficients == [0, 0, 0]
    assert 3 * (1 - c) > 0


def check_protected_axial_chain():
    # Nonglobal three-point chain. Every adjacent gap stays positive here.
    potentials = [F(i, 100) for i in range(-2, 3)]
    checked = 0
    for xi in product(potentials, repeat=3):
        points = [(F(i) + xi[i], F(0)) for i in range(3)]
        lower = norm2(sub(points[1], points[0])) >= 1
        lower &= norm2(sub(points[2], points[1])) >= 1
        upper = norm2(sub(points[2], points[0])) <= 4
        assert (lower and upper) == (xi[0] == xi[1] == xi[2])
        checked += 1
    return checked


def main():
    r = check_safe_packet([(F(0), F(1, 100)), (F(0), F(9, 10))])
    assert norm2(r) > F(5, 4) ** 2 and abs(r[1]) > F(1, 8)
    nonparallel = [(F(-1, 5000), F(1, 1000)),
                   (F(1, 5000), F(2, 1000))]
    kappa, a_star = F(1, 4), F(1, 400)
    assert a_star / 2 + kappa < F(1, 2)
    for delta in nonparallel:
        assert norm2(delta) <= a_star * a_star
        # |delta/|delta|-(0,1)|<=kappa, squared without a radical.
        assert delta[1] > 0
        assert delta[1] ** 2 >= (1 - kappa * kappa / 2) ** 2 * norm2(delta)
    check_safe_packet(nonparallel)
    n = check_depth_samples()
    sharp = check_sharpness()
    check_owner_return()
    axial = check_protected_axial_chain()
    print(f"PASS: 2 safe full-source packets; {n} exact depth/interpolation "
          f"states; {sharp} sharpness packets; connected owner-return "
          "with preserved dimers and singleton feasibility; "
          f"{axial} protected axial states")


if __name__ == "__main__":
    main()
