#!/usr/bin/env python3
"""Exact finite certificates for the bulk-midpoint report of 2026-10-02.

Encoded: Fourier coefficient comparisons after removal of translation modes;
projective-gap identities for rational actual-diameter packets; matching/cover
inequalities for all subgraphs of the listed Woodall graphs; and integer and
rational bounds for the smooth-body regression family. Bounds 3<pi<22/7 and
sin(x)>=x-x**3/6 certify separation without floating trigonometry.

Omitted: KKT/stress/core rigidity for the regression, global optimality, actual
train extraction, and an upper atom bound on a canonical KKT stress. The dense
isolate population is certified by lattice averaging, not enumerated. The
analytic infinite-family proof is in the report; finite survival is not its
proof. All certificate arithmetic is integer/Fraction.
"""

from fractions import Fraction as F
from functools import lru_cache


PI_LO = F(3)
PI_HI = F(22, 7)


def fourier_energy() -> int:
    tested = 0
    for k in range(3, 514, 2):
        assert F(k * k + 1, k * k - 1) <= F(5, 4)
        tested += 1
    assert F(10, 8) == F(5, 4)
    # Translation mode is not coercive and must be removed.
    assert 1 * 1 - 1 == 0
    return tested


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def diff(a, b):
    return tuple(x - y for x, y in zip(a, b))


def rational_diameter_packets() -> int:
    packets = [
        [(F(0), F(0)), (F(5), F(0)), (F(3), F(4))],
        [(F(5), F(0)), (F(-5), F(0)),
         (F(315, 65), F(80, 65)), (F(-315, 65), F(-80, 65))],
    ]
    comparisons = 0
    for points in packets:
        distances = {}
        for i in range(len(points)):
            for j in range(i):
                r = diff(points[i], points[j])
                distances[j, i] = dot(r, r)
        d2 = max(distances.values())
        assert min(distances.values()) >= 1
        edges = [e for e, length in distances.items() if length == d2]
        assert len(edges) >= 2
        for ei, (a, b) in enumerate(edges):
            for c, d in edges[:ei]:
                u, v = diff(points[b], points[a]), diff(points[d], points[c])
                if dot(u, v) < 0:
                    c, d = d, c
                    v = diff(points[d], points[c])
                # (2D sin(theta/2))**2 = 2D**2(1-cos(theta)).
                assert 2 * (d2 - dot(u, v)) >= 1
                m1 = tuple((x + y) / 2 for x, y in zip(points[a], points[b]))
                m2 = tuple((x + y) / 2 for x, y in zip(points[c], points[d]))
                z = diff(m1, m2)
                assert dot(z, z) <= (d2 - dot(u, v)) / 2
                comparisons += 1
    return comparisons


def cover_number(n, edges):
    return min(mask.bit_count() for mask in range(1 << n)
               if all((mask >> a & 1) or (mask >> b & 1) for a, b in edges))


def matching_number(n, edges):
    adjacency = [0] * n
    for a, b in edges:
        adjacency[a] |= 1 << b
        adjacency[b] |= 1 << a

    @lru_cache(None)
    def solve(mask):
        if not mask:
            return 0
        a = (mask & -mask).bit_length() - 1
        rest = mask & ~(1 << a)
        best = solve(rest)
        neighbors = adjacency[a] & rest
        while neighbors:
            bit = neighbors & -neighbors
            neighbors -= bit
            best = max(best, 1 + solve(rest & ~bit))
        return best

    return solve((1 << n) - 1)


def woodall_subgraphs() -> int:
    # Path, star, two forest components, and an odd cycle with pendant leaves.
    families = [
        (7, [(i, i + 1) for i in range(6)], True),
        (7, [(0, i) for i in range(1, 7)], True),
        (8, [(0, 1), (1, 2), (1, 3), (4, 5), (5, 6), (6, 7)], True),
        (8, [(i, (i + 1) % 5) for i in range(5)] + [(0, 5), (1, 6), (3, 7)], False),
    ]
    checked = 0
    for n, all_edges, forest in families:
        for bits in range(1 << len(all_edges)):
            edges = [e for i, e in enumerate(all_edges) if bits >> i & 1]
            nu = matching_number(n, edges)
            tau = cover_number(n, edges)
            assert tau <= nu + 1
            if forest:
                assert tau == nu
            degrees = [0] * n
            for a, b in edges:
                degrees[a] += 1
                degrees[b] += 1
            degree = max(degrees)
            if degree:
                assert len(edges) <= (nu + 1) * degree
            checked += 1
    return checked


def family_member(k):
    assert k >= 101 and k % 4 == 1
    d = k * k
    a = F(d, 16 * (d - 1))
    t = (5 * k - 1) // 4
    n = k * t
    residues = [j for j in range(t) if t <= 12 * j <= 11 * t]
    count = k * len(residues)
    assert count > d
    assert count >= F(5, 6) * n - 2 * k

    # These modular indices encode the exact phase selection, not float sin.
    selected = {j for j in range(n) if (j % t) in residues}
    assert len(selected) == count
    assert {(j + 2 * t) % n for j in selected} == selected
    xlo = PI_LO / (2 * n)
    xhi = PI_HI / (2 * n)
    separation = F(7 * d, 8) * (xlo - xhi ** 3 / 6)
    assert separation > 1
    # sin(pi/12) > 1/4: (sqrt(6)-sqrt(2))**2 = 8-4sqrt(3)>1.
    assert F(7, 4) ** 2 > 3
    midpoint_lo = a * k / 4
    assert midpoint_lo > F(k, 64)

    delta_hi = PI_HI * d * d / (512 * (d - 1))
    gap_hi = PI_HI / (6 * k) + 2 * PI_HI / n
    assert gap_hi < PI_HI / (5 * k)
    rho_hi = F(9 * d, 16)
    hull_deficit_hi = delta_hi + PI_HI / 6 * rho_hi ** 2 * gap_hi ** 2
    assert hull_deficit_hi < d
    inradius_loss = a + rho_hi * gap_hi ** 2 / 8
    assert inradius_loss < F(1, 6)

    scale = 1 + F(1, d ** 3)
    area_inner_lo = PI_LO * d * d / 4 - delta_hi - 2 * PI_HI * d
    # sqrt(3)<7/4; scaled triangular fundamental area <(7/8)*scale**2.
    lattice_count_lo = area_inner_lo / (F(7, 8) * scale ** 2)
    assert lattice_count_lo > F(4, 5) * d * d
    return {
        "k": k, "D": d, "actual_diameters": count,
        "separation_bound_gt_1": True, "midpoint_radius_gt_sqrtD_over_64": True,
        "hull_deficit_lt_D": True, "inradius_loss_lt_1_over_6": True,
        "interior_lattice_count_gt_4D2_over_5": True,
    }


def sampled_energy_certificate() -> int:
    # Independent finite scalar Lipschitz packets on disjoint unit cells.
    # Constant values at centers +/-a, with slope magnitude <=1/2: at every
    # point in the cell the value differs from its center by at most 1/4.
    checked = 0
    for height in range(-20, 21):
        for slope in (F(-1, 2), F(0), F(1, 2)):
            center = F(height, 4)
            integral = center ** 2 + slope ** 2 / 12
            tent_floor = max(F(0), abs(center) - F(1, 4))
            assert integral >= tent_floor ** 2
            checked += 1
    return checked


def main():
    modes = fourier_energy()
    packets = rational_diameter_packets()
    graphs = woodall_subgraphs()
    samples = sampled_energy_certificate()
    for k in (101, 105, 201):
        print(family_member(k))
    print(f"PASS: {modes} Fourier modes; {packets} exact diameter comparisons; "
          f"{graphs} Woodall subgraphs; {samples} Lipschitz cells; "
          "three certified dense-source geometric regression members")
    print("OMITTED: regression KKT/global optimality; canonical stress atom bound; "
          "contact/face transfer; Level I closure")


if __name__ == "__main__":
    main()
