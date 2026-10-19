"""Exact independent replay for the finite phase-grid audit."""

from fractions import Fraction as F
import json


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def q(a: int, b: int, cosine: F) -> F:
    return F(a * a + b * b) + 2 * cosine * a * b


def labels(m: int, n: int):
    return [(i, j) for i in range(m + 1) for j in range(n + 1)]


def pair_ledger(m: int, n: int, cosine: F):
    points = labels(m, n)
    return {
        (p, r): q(p[0] - r[0], p[1] - r[1], cosine)
        for index, p in enumerate(points)
        for r in points[index + 1 :]
    }


def active_pairs(ledger):
    diameter_squared = max(ledger.values())
    active = {pair for pair, value in ledger.items() if value == diameter_squared}
    return diameter_squared, active


def unit_pairs(ledger):
    return {pair for pair, value in ledger.items() if value == 1}


def check_general_integer_box() -> int:
    """Check the exact pair bounds and active sets over a bounded family."""
    checked = 0
    c0_values = (F(1, 100), F(7, 25), F(49, 100))
    for m in range(1, 9):
        for n in range(1, 9):
            for c0 in c0_values:
                require(0 < c0 < F(1, 2), "fixture cosine is outside the open angle range")
                # q and H are affine in cosine. Endpoint checks certify each
                # full path interval for this finite label box.
                for cosine in (F(0), c0, F(1, 2)):
                    diameter_bound = m * m + n * n + 2 * m * n * cosine
                    for a in range(-m, m + 1):
                        for b in range(-n, n + 1):
                            if a == 0 and b == 0:
                                continue
                            value = q(a, b, cosine)
                            require(value >= 1, f"lower-pair violation: m={m}, n={n}, a={a}, b={b}, c={cosine}")
                            require(value <= diameter_bound, f"upper-pair violation: m={m}, n={n}, a={a}, b={b}, c={cosine}")
                            checked += 1
                    ledger = pair_ledger(m, n, cosine)
                    actual_diameter, actual_active = active_pairs(ledger)
                    require(actual_diameter == diameter_bound, "grid diameter formula mismatch")
                    expected = {((0, 0), (m, n))}
                    if cosine == 0:
                        expected.add(((0, n), (m, 0)))
                    require(actual_active == expected, "active-corner pair set mismatch")
    return checked


def check_affine_continuations(m: int, n: int, c0: F) -> int:
    """Endpoint checks for all-pair lower/upper affine functions on both paths."""
    checked = 0
    h = lambda c: F(m * m + n * n) + 2 * m * n * c
    intervals = ((c0, F(0)), (c0, F(1, 2)))
    for c_left, c_right in intervals:
        for a in range(-m, m + 1):
            for b in range(-n, n + 1):
                if a == 0 and b == 0:
                    continue
                for cosine in (c_left, c_right):
                    value = q(a, b, cosine)
                    require(value >= 1, "path endpoint violates a lower pair constraint")
                    require(value <= h(cosine), "path endpoint violates the diameter bound")
                # Both q(c)-1 and H(c)-q(c) are affine in c; nonnegative at
                # both interval endpoints, they are nonnegative throughout.
                checked += 1
    return checked


def main() -> None:
    m, n, c0 = 2, 1, F(7, 25)
    require(7 * 7 + 24 * 24 == 25 * 25, "the rational basis vector is not unit")

    initial = pair_ledger(m, n, c0)
    initial_diameter, initial_active = active_pairs(initial)
    contacts = unit_pairs(initial)
    expected_contacts = {
        ((i, j), (i + 1, j))
        for i in range(m)
        for j in range(n + 1)
    } | {
        ((i, j), (i, j + 1))
        for i in range(m + 1)
        for j in range(n)
    }
    require(len(initial) == 15, "the six-label source must have fifteen unordered pairs")
    require(initial_diameter == F(153, 25), "wrong initial squared diameter")
    require(initial_active == {((0, 0), (m, n))}, "wrong initial active pair")
    require(min(initial.values()) == 1, "initial source is not unit-separated with contact")
    require(contacts == expected_contacts and len(contacts) == 7, "initial unit-contact set mismatch")

    # The contact graph is bipartite by (i+j) mod 2, so the source has no unit triangle.
    adjacency = {p: set() for p in labels(m, n)}
    for p, r in contacts:
        adjacency[p].add(r)
        adjacency[r].add(p)
    triangle_count = sum(
        1
        for p in labels(m, n)
        for r in adjacency[p]
        for s in adjacency[r]
        if s in adjacency[p] and p < r < s
    )
    require(triangle_count == 0, "initial unit-contact graph contains a triangle")

    perpendicular = pair_ledger(m, n, F(0))
    perpendicular_diameter, perpendicular_active = active_pairs(perpendicular)
    require(perpendicular_diameter == 5, "wrong perpendicular squared diameter")
    require(perpendicular_diameter < initial_diameter, "perpendicular endpoint is not a strict competitor")
    require(min(perpendicular.values()) == 1, "perpendicular endpoint violates unit separation")
    require(
        perpendicular_active == {((0, 0), (m, n)), ((0, n), (m, 0))},
        "wrong perpendicular endpoint active pairs",
    )

    opposite = ((0, n), (m, 0))
    old_opposite_squared = initial[opposite]
    new_opposite_squared = perpendicular[opposite]
    require(old_opposite_squared == F(97, 25), "wrong initially inactive corner pair")
    require(old_opposite_squared < initial_diameter, "inactive pair starts above the diameter")
    require(new_opposite_squared == perpendicular_diameter, "inactive pair does not become co-active at the endpoint")

    contracted = pair_ledger(m, n, F(1, 2))
    contracted_diameter, contracted_active = active_pairs(contracted)
    require(contracted_diameter == 7, "wrong phase-contracted squared diameter")
    require(contracted_diameter > initial_diameter, "canonical defect contraction has wrong diameter sign")
    require(min(contracted.values()) == 1, "phase contraction violates a lower pair bound")
    require(contracted_active == {((0, 0), (m, n))}, "wrong contraction active pair")
    extra_contacts = unit_pairs(contracted) - contacts
    expected_extra = {
        tuple(sorted(((i + 1, j), (i, j + 1))))
        for i in range(m)
        for j in range(n)
    }
    require(extra_contacts == expected_extra and len(extra_contacts) == m * n, "wrong new contacts at sixty degrees")

    # Check every pair at the endpoint values of each path interval. The pair
    # squared lengths and proposed diameter are affine in c=cos(theta), so this
    # exactly checks all intermediate parameter values too.
    path_checks = check_affine_continuations(m, n, c0)
    general_checks = check_general_integer_box()
    require(initial_diameter - perpendicular_diameter == F(28, 25), "wrong strict diameter margin")
    require(contracted_diameter - initial_diameter == F(22, 25), "wrong contraction diameter increase")

    print(
        json.dumps(
            {
                "status": "PASS",
                "six_label_unordered_pairs": len(initial),
                "initial_unit_contacts": len(contacts),
                "initial_unit_triangles": triangle_count,
                "initial_squared_diameter": str(initial_diameter),
                "initial_active_pairs": len(initial_active),
                "perpendicular_squared_diameter": str(perpendicular_diameter),
                "perpendicular_active_pairs": len(perpendicular_active),
                "opposite_corner_squared_distance_initial": str(old_opposite_squared),
                "opposite_corner_squared_distance_perpendicular": str(new_opposite_squared),
                "phase_contracted_squared_diameter": str(contracted_diameter),
                "phase_contracted_new_contacts": len(extra_contacts),
                "strict_squared_diameter_margin": str(initial_diameter - perpendicular_diameter),
                "wrong_sign_squared_diameter_change": str(contracted_diameter - initial_diameter),
                "all_pair_path_endpoint_checks": path_checks,
                "bounded_general_label_difference_checks": general_checks,
                "arithmetic": "exact integers and fractions; no floating point",
            },
            sort_keys=True,
        )
    )


main()
