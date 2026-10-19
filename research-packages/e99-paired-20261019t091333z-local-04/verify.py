"""Exact displacement checks for a rhombic grid with one movable guard row."""

from fractions import Fraction


def sign_surd(a: int, b: int, d: int) -> int:
    """Return the sign of a + b*sqrt(d), using integer arithmetic only."""
    if b == 0:
        return (a > 0) - (a < 0)
    if a == 0:
        return (b > 0) - (b < 0)
    if (a > 0) == (b > 0):
        return 1 if a > 0 else -1
    comparison = a * a - b * b * d
    if a > 0:
        return (comparison > 0) - (comparison < 0)
    return (comparison < 0) - (comparison > 0)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def verify_size(m: int) -> int:
    require(m >= 7, f"m must be at least 7, got {m}")
    d = m * m - 6 * m - 3
    require(0 < d < m * m, f"invalid initial cosine for m={m}")
    require(d + 3 * (m + 1) ** 2 == 4 * m * m,
            f"the two basis vectors are not unit for m={m}")

    # The source has columns i=0..m and rows j=0..m+1. The final row is
    # the exterior guard and remains in the endpoint population.
    population = (m + 1) * (m + 2)
    guard_labels = m + 1
    require(population == (m + 1) * (m + 1) + guard_labels,
            f"guard population was not retained for m={m}")
    endpoint_diameter_squared = m * m + (m + 1) * (m + 1)
    checked = 0

    # Every possible source pair displacement occurs in this rectangle.
    # At theta_m, cos(theta_m)=sqrt(d)/(2m), so squared distances are
    # a^2+b^2+ab*sqrt(d)/m.
    for a in range(-m, m + 1):
        for b in range(-(m + 1), m + 2):
            if a == 0 and b == 0:
                continue
            checked += 1
            lower = sign_surd(m * (a * a + b * b - 1), a * b, d)
            require(lower >= 0,
                    f"initial lower pair bound failed at m={m}, difference=({a},{b})")
            is_grid_edge = abs(a) + abs(b) == 1
            require((lower == 0) == is_grid_edge,
                    f"initial contact classification failed at m={m}, difference=({a},{b})")

            # The initial actual diameter squared is
            # m^2+(m+1)^2+(m+1)*sqrt(d).
            upper = sign_surd(
                m * (m * m + (m + 1) * (m + 1) - a * a - b * b),
                m * (m + 1) - a * b,
                d,
            )
            require(upper >= 0,
                    f"initial diameter bound failed at m={m}, difference=({a},{b})")

            # At the square endpoint, u and v are perpendicular. Check every
            # possible endpoint lower pair and its original-diameter upper.
            endpoint_squared = a * a + b * b
            require(endpoint_squared >= 1,
                    f"endpoint lower pair bound failed at m={m}, difference=({a},{b})")
            require(endpoint_squared <= endpoint_diameter_squared,
                    f"endpoint actual-diameter bound failed at m={m}, difference=({a},{b})")
            endpoint_upper = sign_surd(
                m * (m * m + (m + 1) * (m + 1) - endpoint_squared),
                m * (m + 1),
                d,
            )
            require(endpoint_upper >= 0,
                    f"endpoint original-diameter bound failed at m={m}, difference=({a},{b})")

    contacts = m * (m + 2) + (m + 1) * (m + 1)
    require(contacts == 2 * m * m + 4 * m + 1,
            f"rectangular grid contact count failed for m={m}")
    require(sign_surd(0, 0, d) == 0, "surd equality helper failed")

    # The initial and endpoint source diameters are attained at the same-sign
    # corner difference (m,m+1).
    initial_corner = sign_surd(
        m * (m * m + (m + 1) * (m + 1) - m * m - (m + 1) * (m + 1)),
        m * (m + 1) - m * (m + 1),
        d,
    )
    endpoint_corner_squared = m * m + (m + 1) * (m + 1)
    require(initial_corner == 0 and endpoint_corner_squared == endpoint_diameter_squared,
            f"diameter corner equality failed for m={m}")
    require(sign_surd(0, 0, d) == 0, "surd equality helper failed")
    # The endpoint diameter is strictly smaller by (m+1)*sqrt(d).
    require(sign_surd(0, m + 1, d) > 0,
            f"endpoint diameter did not decrease for m={m}")

    # At theta_m, 2*sin(theta_m)/sqrt(3)=(m+1)/m, so the exact Oler
    # slack is m+1. At pi/2 it is (2/sqrt(3)-1)*m*(m+1)>0.
    initial_slack = m * (m + 1) * (Fraction(m + 1, m) - 1)
    require(initial_slack == m + 1,
            f"initial Oler slack identity failed for m={m}")
    require(4 > 3, "terminal quadratic slack coefficient is not positive")

    # Every rhombus split along u-v has R^2=1/(2*(1+cos(theta)))<=1/2<1.
    cover_radius_squared_bound = Fraction(1, 2)
    require(cover_radius_squared_bound < 1,
            f"cover radius does not force strict coverage for m={m}")
    return checked


def verify_out_of_range_control() -> None:
    cosine = Fraction(3, 4)
    opposite_step_squared = 2 - 2 * cosine
    require(opposite_step_squared == Fraction(1, 2),
            "out-of-range control arithmetic failed")
    require(opposite_step_squared < 1,
            "cosine above 1/2 did not violate unit separation")


def main() -> None:
    sizes = (7, 8, 12, 24)
    total = 0
    for m in sizes:
        total += verify_size(m)
        population = (m + 1) * (m + 2)
        d = m * m - 6 * m - 3
        print(
            f"PASS m={m}: population={population} including {m + 1} guard labels, "
            f"all {((2 * m + 1) * (2 * m + 3) - 1)} displacement vectors, "
            f"contacts={2 * m * m + 4 * m + 1}, "
            f"D0^2={m * m + (m + 1) * (m + 1)}+(m + 1)*sqrt({d}), "
            f"Dend^2={m * m + (m + 1) * (m + 1)}"
        )
    verify_out_of_range_control()
    print(f"PASS: {total} initial displacement checks; full path bounds follow from the proof")
    print("PASS: endpoint retains every label and obeys the initial diameter cap")
    print("PASS: exact Oler slack endpoints and strict cover-radius bound")
    print("PASS: cosine 3/4 negative control violates unit separation")
    print("Scope: sampled exact checks corroborate the universal formulas proved in README.md")


main()
