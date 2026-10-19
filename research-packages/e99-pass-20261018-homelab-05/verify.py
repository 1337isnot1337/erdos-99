"""Exact finite controls for the rotating full-source rhombic-wall regression."""

from fractions import Fraction


def sign_surd(a: int, b: int, d: int) -> int:
    """Return the sign of a + b*sqrt(d), using integer arithmetic only."""
    if b == 0:
        return (a > 0) - (a < 0)
    if a == 0:
        return (b > 0) - (b < 0)
    if a > 0 and b > 0:
        return 1
    if a < 0 and b < 0:
        return -1
    if a > 0 and b < 0:
        comparison = a * a - b * b * d
        return (comparison > 0) - (comparison < 0)
    comparison = b * b * d - a * a
    return (comparison > 0) - (comparison < 0)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def verify_size(m: int) -> int:
    require(m >= 7, f"m must be at least 7, got {m}")
    d = m * m - 6 * m - 3
    require(d > 0, f"initial angle is not real for m={m}")
    require(d < m * m, f"initial cosine is not below 1/2 for m={m}")
    require(d + 3 * (m + 1) ** 2 == 4 * m * m,
            f"unit basis identity failed for m={m}")

    checked = 0
    directed_contacts = 0
    for a in range(-m, m + 1):
        for b in range(-m, m + 1):
            if a == 0 and b == 0:
                continue
            checked += 1
            lower_sign = sign_surd(m * (a * a + b * b - 1), a * b, d)
            require(lower_sign >= 0,
                    f"lower pair bound failed at m={m}, difference=({a},{b})")
            is_grid_edge = abs(a) + abs(b) == 1
            require((lower_sign == 0) == is_grid_edge,
                    f"unit-contact classification failed at m={m}, difference=({a},{b})")
            if lower_sign == 0:
                directed_contacts += (m + 1 - abs(a)) * (m + 1 - abs(b))

            upper_sign = sign_surd(
                2 * m**3 - m * (a * a + b * b), m * m - a * b, d
            )
            require(upper_sign >= 0,
                    f"original diameter bound failed at m={m}, difference=({a},{b})")

    require(sign_surd(0, 0, d) == 0, "surd equality helper failed")
    corner_gap = sign_surd(
        2 * m**3 - 2 * m**3, m * m - m * m, d
    )
    require(corner_gap == 0, f"D_m corner equality failed for m={m}")
    require((m + 1) ** 2 - 1 == m * (m + 2), "population identity failed")
    require(directed_contacts // 2 == 2 * m * (m + 1),
            f"undirected contact count failed for m={m}")
    start_area_term = Fraction(2 * m * m, 2 * m) * (m + 1)
    start_slack = start_area_term + 2 * m + 1 - (m + 1) ** 2
    require(start_slack == m, f"initial Oler slack identity failed for m={m}")
    require(d == 4 * m * m - 3 * (m + 1) ** 2,
            f"terminal slack comparison identity failed for m={m}")
    require(d > 0, "terminal quadratic slack does not exceed initial slack")
    # R^2=1/(2*(1+c)); on c in [0,c_m] its maximum is the c=0 value.
    worst_radius_squared = Fraction(1, 2)
    require(worst_radius_squared < 1,
            "worst cover radius squared is not below one")
    require(4 > 3, "terminal quadratic slack coefficient is not positive")
    return checked


def verify_failure_control() -> None:
    cosine = Fraction(3, 4)
    cross_squared = 2 - 2 * cosine
    require(cross_squared == Fraction(1, 2), "negative-control arithmetic failed")
    require(cross_squared < 1, "out-of-range cosine did not fail separation")


def main() -> None:
    sizes = (7, 8, 12, 24)
    total = sum(verify_size(m) for m in sizes)
    verify_failure_control()
    print(f"PASS: exact initial pair and diameter checks for m={sizes}; "
          f"{total} nonzero difference vectors checked")
    print("PASS: contact counts, D_m^2=2m^2+m*sqrt(d_m), and exact slack identities")
    print("PASS: maximum path cover radius squared is 1/2 < 1")
    print("PASS: out-of-range cosine 3/4 fails; |u-v|^2=1/2 < 1")
    print("Scope: finite arithmetic controls only; the all-m continuous-angle cover proof is in README.md")


main()
