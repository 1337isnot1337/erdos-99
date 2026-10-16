#!/usr/bin/env python3
"""Exact finite certificates for fan-flip blockers and local fan ladders.

Uses only fractions and integers. It checks explicit sources, not global
optimality or completion of the local stresses at the carrier/end vertices.
"""

if not __debug__:
    raise RuntimeError("Certificate assertions are required; run Python without -O.")

from fractions import Fraction as F
from math import isqrt


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def scale(a, t):
    return a[0] * t, a[1] * t


def norm2(a):
    return a[0] ** 2 + a[1] ** 2


def rotate(a, c, s):
    return c * a[0] - s * a[1], s * a[0] + c * a[1]


def fan(q, half_length):
    # eps=sin(x), tau=cos(x), central unit-chord step=2x.
    eps = F(2 * q, q * q + 1)
    tau = F(q * q - 1, q * q + 1)
    diameter = 1 / (2 * eps)
    c, s = tau * tau - eps * eps, 2 * eps * tau
    p = (diameter, F(0))
    for _ in range(half_length):
        p = rotate(p, c, -s)
    points = [p]
    for _ in range(2 * half_length + 1):
        points.append(rotate(points[-1], c, s))
    assert eps * eps + tau * tau == 1
    assert all(norm2(p) == diameter * diameter for p in points)
    assert all(norm2(sub(a, b)) == 1 for a, b in zip(points, points[1:]))
    return diameter, eps, tau, points


def source_check(source, diameter):
    contacts, diameters = set(), set()
    pairs = 0
    for i, a in enumerate(source):
        for j in range(i):
            d2 = norm2(sub(a, source[j]))
            assert 1 <= d2 <= diameter * diameter, (i, j, d2)
            if d2 == 1:
                contacts.add((j, i))
            if d2 == diameter * diameter:
                diameters.add((j, i))
            pairs += 1
    for i, j in contacts:
        assert not any((min(i, k), max(i, k)) in contacts
                       and (min(j, k), max(j, k)) in contacts
                       for k in range(len(source)) if k != i and k != j)
    return contacts, diameters, pairs


def strict_carrier_competitor(source, diameter, contacts):
    """Certify nonglobality of these fixtures by moving their isolated carrier."""
    assert source[0] == (0, 0)
    limits = [F(1, 100)]
    for p in source[1:]:
        assert p[0] > 0 and norm2(p) > 1
        limits.extend([p[0], (norm2(p)-1)/(4*(2*abs(p[0])+1))])
    step = min(limits)
    assert step > 0
    competitor = list(source)
    competitor[0] = (step, F(0))
    new_contacts, new_diameters, pairs = source_check(competitor, diameter)
    assert new_contacts == contacts and not new_diameters
    return pairs


def blocked_fan(q, half_length):
    d, eps, tau, p = fan(q, half_length)
    # Strict rational overestimate of sqrt(3)/2 within 1/Q.
    raw = 100 * d * d
    denominator = (raw.numerator + raw.denominator - 1) // raw.denominator
    h = F(isqrt(3 * denominator * denominator) // 2 + 1, denominator)
    assert h * h > F(3, 4)
    assert (h - 1 / denominator) ** 2 < F(3, 4)
    z = []
    for j in range(0, len(p), 2):
        midpoint = scale(add(p[j], p[j + 1]), F(1, 2))
        z.append(scale(midpoint, 1 - h / (d * tau)))
    source = [(F(0), F(0))] + p + z
    contacts, diameters, pairs = source_check(source, d)
    n = len(p)
    assert contacts == {(i + 1, i + 2) for i in range(n - 1)}
    assert diameters == {(0, i + 1) for i in range(n)}
    assert all(norm2(sub(p[j], z[j // 2])) == h * h + F(1, 4)
               for j in range(n))
    flipped = [scale(x, 1 - 1 / (d * d)) for x in p]
    for j in range(1, n - 1):
        assert norm2(sub(flipped[j], p[j - 1])) == 1
        assert norm2(sub(flipped[j], p[j + 1])) == 1
        assert norm2(sub(flipped[j], z[j // 2])) < 1
        assert norm2(sub(p[j], z[j // 2])) > 1
        assert all(norm2(sub(flipped[j], a)) < d * d for a in source)
        # Repair the nonglobal blocked-fan regression by co-moving its isolated
        # blocker. This preserves all contacts and removes precisely one diameter.
        repaired = list(source)
        displacement = sub(flipped[j], p[j])
        repaired[j + 1] = flipped[j]
        repaired[n + 1 + j // 2] = add(z[j // 2], displacement)
        new_contacts, new_diameters, _ = source_check(repaired, d)
        assert new_contacts == contacts
        assert new_diameters == diameters - {(0, j + 1)}
    strict_pairs = strict_carrier_competitor(source, d, contacts)
    return pairs, n - 2, len(z), strict_pairs


def positive_ladder(q, half_length):
    d, eps, tau, p = fan(q, half_length)
    v = (F(1), F(0))
    z = [sub(a, v) for a in p]
    n = len(p)
    source = [(F(0), F(0))] + p + z
    contacts, diameters, pairs = source_check(source, d)
    expected = {(i + 1, i + 2) for i in range(n - 1)}
    expected |= {(n + i + 1, n + i + 2) for i in range(n - 1)}
    expected |= {(i + 1, n + i + 1) for i in range(n)}
    assert contacts == expected
    assert diameters == {(0, i + 1) for i in range(n)}
    row_weights = [1 / (b[1] - a[1]) for a, b in zip(p, p[1:])]
    total_weight = max(row_weights) + 1
    outer_weights = [total_weight - w for w in row_weights]
    beta = total_weight / (d * d)
    equilibria = 0
    for i in range(1, n - 1):
        inner_reaction = add(scale(sub(z[i], z[i - 1]), row_weights[i - 1]),
                             scale(sub(z[i], z[i + 1]), row_weights[i]))
        gamma = inner_reaction[0]
        assert gamma > 0 and inner_reaction[1] == 0
        assert sub(inner_reaction, scale(v, gamma)) == (0, 0)
        outer_reaction = add(scale(sub(p[i], p[i - 1]), outer_weights[i - 1]),
                             scale(sub(p[i], p[i + 1]), outer_weights[i]))
        outer_reaction = add(outer_reaction, scale(v, gamma))
        assert outer_reaction == scale(p[i], beta)
        equilibria += 2
    strict_pairs = strict_carrier_competitor(source, d, contacts)
    return pairs, equilibria, n, strict_pairs


def exact_constants():
    # D>=4: all nonfan blockers lie strictly in conv(a,p_-,p_+).
    assert F(40, 63) < F(693, 1024)
    assert F(63, 64) ** 2 < F(63, 64)
    # A cap x >= c of B(0,D) lies in B((c,0),sqrt(D^2-c^2)).
    # c > sqrt(3)D/2 makes its diameter < D. The rational c=7D/8
    # specialization gives the certified squared ratio 15/16 < 1.
    assert 4 * (1 - F(7, 8) ** 2) == F(15, 16) < 1
    count = 0
    for q in (20, 40, 80, 160, 320, 640):
        d, eps, tau, p = fan(q, 2)
        invd2 = 1 / (d * d)
        radius = d - 1 / d
        gap2 = 2 * tau * (1 - invd2)
        lens_radius = (3 - invd2) / (2 * d)
        assert 1 - (gap2 / 2) ** 2 == lens_radius ** 2
        assert d - radius * (1 - invd2 / 2) == lens_radius
        assert 2 * lens_radius < 1
        assert (1 - invd2) * (3 - invd2) > 2
        for j in range(1, len(p) - 1):
            pflip = scale(p[j], 1 - invd2)
            assert norm2(sub(pflip, p[j - 1])) == 1
            assert norm2(sub(pflip, p[j + 1])) == 1
            assert pflip == sub(add(p[j - 1], p[j + 1]), p[j])
            count += 1
    return count


def main():
    identities = exact_constants()
    blocked_pairs = flips = blockers = ladder_pairs = equilibria = strict_pairs = 0
    configurations = [(20, 1), (40, 2), (80, 3), (160, 4), (320, 8), (640, 16)]
    for q, half_length in configurations:
        pairs, nflip, nz, competitor_pairs = blocked_fan(q, half_length)
        blocked_pairs += pairs
        strict_pairs += competitor_pairs
        flips += nflip
        blockers += nz
        pairs, neq, _, competitor_pairs = positive_ladder(q, half_length)
        ladder_pairs += pairs
        strict_pairs += competitor_pairs
        equilibria += neq
    print(f"PASS: {identities} exact flip identities; {len(configurations)} rational "
          f"blocked-fan sources ({blocked_pairs} pair bounds, {flips} strictly blocked "
          f"internal flips, {blockers} isolated blockers); {len(configurations)} "
          f"positive local ladders ({ladder_pairs} pair bounds, {equilibria} exact "
          "positive interior equilibrium identities).")
    print(f"PASS: {2*len(configurations)} explicit strict carrier competitors; "
          f"{strict_pairs} complete pair bounds, all old contacts preserved")
    print("Scope: no global-optimality certificate; local ladder endpoint/carrier "
          "equilibrium and canonical ZR/ZF rank are not encoded; C-II/Level I remain open.")


if __name__ == "__main__":
    main()
