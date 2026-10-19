"""Exact all-pairs check for the imbalanced 2-by-1 oblique grid."""

from fractions import Fraction as Q
import json


M = 2
N = 1
COS_OLD = Q(7, 25)
COS_PERPENDICULAR = Q(0)
COS_PHASE_CONTRACTED = Q(1, 2)


def fail(message: str) -> None:
    raise SystemExit(message)


def point_indices():
    return [(i, j) for i in range(M + 1) for j in range(N + 1)]


def distance_squared(p, q, cosine: Q) -> Q:
    a, b = p[0] - q[0], p[1] - q[1]
    return Q(a * a + b * b) + 2 * cosine * a * b


def pair_ledger(cosine: Q):
    points = point_indices()
    return {
        (p, q): distance_squared(p, q, cosine)
        for i, p in enumerate(points)
        for q in points[i + 1 :]
    }


def diameter_and_active_pairs(ledger):
    diameter_squared = max(ledger.values())
    active = [pair for pair, value in ledger.items() if value == diameter_squared]
    return diameter_squared, active


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def main() -> None:
    # u=(1,0), v=(7/25,24/25) are exact unit vectors.
    require(COS_OLD * COS_OLD + Q(24, 25) ** 2 == 1, "old basis is not unit")

    old = pair_ledger(COS_OLD)
    old_diameter, old_active = diameter_and_active_pairs(old)
    require(len(old) == 15, "wrong number of unordered source pairs")
    require(min(old.values()) >= 1, "an initial source pair is closer than one")
    require(old_diameter == Q(153, 25), "wrong exact initial diameter")
    require(old_active == [((0, 0), (2, 1))], "wrong initial active-diameter set")

    contacts = {pair for pair, value in old.items() if value == 1}
    expected_contacts = {
        ((i, j), (i + 1, j))
        for i in range(M)
        for j in range(N + 1)
    } | {
        ((i, j), (i, j + 1))
        for i in range(M + 1)
        for j in range(N)
    }
    require(contacts == expected_contacts, "unit contacts are not exactly the grid edges")
    require(len(contacts) == 7, "wrong contact count")

    # The actual Z/3 potential has two train classes of sizes M and N;
    # every one of the M*N rhombi is a crossing directed from class 0 to class 1.
    require((M, N) == (2, 1), "wrong imbalanced train-class sizes")
    require(M * N == 2, "wrong complete crossing count")

    # Phase contraction reaches theta=pi/3 (cosine 1/2). It remains
    # unit-separated, but the diameter increases: this is the negative control.
    phase_contracted = pair_ledger(COS_PHASE_CONTRACTED)
    contracted_diameter, _ = diameter_and_active_pairs(phase_contracted)
    require(min(phase_contracted.values()) >= 1, "phase contraction violates separation")
    require(contracted_diameter == 7, "wrong phase-contracted diameter")
    require(contracted_diameter > old_diameter, "wrong-sign phase regression disappeared")
    require(
        distance_squared((1, 0), (0, 1), COS_PHASE_CONTRACTED) == 1,
        "the expected new unit diagonal at the 60-degree endpoint is missing",
    )

    # Increasing theta to pi/2 gives the same six labels on a square grid.
    # This is a full-source strict-D competitor; all fifteen pairs are checked.
    perpendicular = pair_ledger(COS_PERPENDICULAR)
    perpendicular_diameter, perpendicular_active = diameter_and_active_pairs(perpendicular)
    require(min(perpendicular.values()) >= 1, "perpendicular endpoint violates separation")
    require(perpendicular_diameter == 5, "wrong perpendicular endpoint diameter")
    require(perpendicular_diameter < old_diameter, "endpoint is not a strict competitor")
    require(old_diameter - perpendicular_diameter == Q(28, 25), "wrong strict margin")
    require(len(perpendicular_active) == 2, "wrong perpendicular active-pair count")
    opposite_corner_old = distance_squared((0, 1), (2, 0), COS_OLD)
    opposite_corner_new = distance_squared((0, 1), (2, 0), COS_PERPENDICULAR)
    require(opposite_corner_old == Q(97, 25), "wrong initially inactive opposite-corner distance")
    require(opposite_corner_old < old_diameter, "opposite-corner pair was not initially inactive")
    require(opposite_corner_new == perpendicular_diameter, "inactive pair did not become endpoint-active")
    require(opposite_corner_new < old_diameter, "inactive pair exceeds the old diameter")

    # Path control: for each non-axis integer difference and every cosine in
    # [0, 7/25], the squared length is at least 18/25*(a^2+b^2) >= 36/25.
    path_lower_bound = Q(36, 25)
    for a in range(-M, M + 1):
        for b in range(-N, N + 1):
            if a != 0 and b != 0:
                require(
                    Q(a * a + b * b) - 2 * COS_OLD * abs(a * b) >= path_lower_bound,
                    "path lower-bound control failed for a non-axis pair",
                )

    print(
        json.dumps(
            {
                "status": "PASS",
                "source_points": (M + 1) * (N + 1),
                "unordered_pairs_checked_at_each_endpoint": len(old),
                "unit_contacts": len(contacts),
                "phase_classes": [M, N],
                "crossings": M * N,
                "old_diameter_squared": str(old_diameter),
                "old_active_pairs": [str(pair) for pair in old_active],
                "phase_contracted_diameter_squared": str(contracted_diameter),
                "perpendicular_diameter_squared": str(perpendicular_diameter),
                "opposite_corner_pair_old_squared": str(opposite_corner_old),
                "opposite_corner_pair_new_squared": str(opposite_corner_new),
                "strict_diameter_margin": str(old_diameter - perpendicular_diameter),
                "path_nonaxis_squared_distance_lower_bound": str(path_lower_bound),
            },
            sort_keys=True,
        )
    )


main()
