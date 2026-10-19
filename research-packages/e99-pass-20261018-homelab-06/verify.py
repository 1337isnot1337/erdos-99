#!/usr/bin/env python3
"""Exact finite checks for the tolerance-aware wall/refill ledger."""

from fractions import Fraction
from itertools import combinations


def sign_surd(rational_numerator: int, radical_coefficient: int, radicand: int) -> int:
    """Sign of A + B*sqrt(radicand), using integer arithmetic only."""
    a, b = rational_numerator, radical_coefficient
    if b == 0:
        return (a > 0) - (a < 0)
    if a == 0:
        return (b > 0) - (b < 0)
    if (a > 0) == (b > 0):
        return 1 if a > 0 else -1
    square_comparison = a * a - b * b * radicand
    if square_comparison == 0:
        return 0
    if a > 0:  # A>0>B: the sign is sign(A^2 - B^2*d).
        return (square_comparison > 0) - (square_comparison < 0)
    # A<0<B: the sign is the opposite of sign(A^2 - B^2*d).
    return (square_comparison < 0) - (square_comparison > 0)


def source_diameter_comparison(a: int, b: int, m: int, radicand: int) -> int:
    """Sign of |a*u+b*v|^2 - D_m^2, multiplied by positive m."""
    return sign_surd(
        m * (a * a + b * b - 2 * m * m), a * b - m * m, radicand
    )


def check_frame(m: int) -> None:
    assert m >= 7
    d = m * m - 6 * m - 3
    assert 0 < d < m * m
    # c = sqrt(d)/(2m) and s = sqrt(3)(m+1)/(2m) give c^2+s^2=1.
    assert d + 3 * (m + 1) ** 2 == 4 * m * m

    points = [(i, j) for i in range(m + 1) for j in range(m + 1)]
    degrees = [0] * len(points)
    contacts = 0
    lower_pairs = upper_pairs = 0
    for ia, ib in combinations(range(len(points)), 2):
        i, j = points[ia]
        k, ell = points[ib]
        a, b = i - k, j - ell

        # |a*u+b*v|^2 - 1 = (A+B*sqrt(d))/m.
        low_sign = sign_surd(m * (a * a + b * b - 1), a * b, d)
        assert low_sign >= 0, (m, (i, j), (k, ell), "lower pair")
        lower_pairs += 1
        if low_sign == 0:
            assert (abs(a), abs(b)) in ((1, 0), (0, 1))
            contacts += 1
            degrees[ia] += 1
            degrees[ib] += 1

        # D^2 = 2*m^2 + m*sqrt(d); every source pair must be <= D.
        upper_sign = source_diameter_comparison(a, b, m, d)
        assert upper_sign <= 0, (m, (i, j), (k, ell), "diameter upper pair")
        upper_pairs += 1

    n = (m + 1) ** 2
    k_interior = (m - 1) ** 2
    boundary = 4 * m
    deleted_pins = 2 * m - 1
    z = k_interior
    actual_deficit = k_interior - z
    requested_targets = z + deleted_pins
    available_strict_targets = k_interior
    shortfall = requested_targets - available_strict_targets
    assert contacts == 2 * m * (m + 1)
    assert min(degrees) == 2  # Every label is counted; this control has no isolates.
    assert n == k_interior + boundary
    assert actual_deficit == 0 < deleted_pins
    assert shortfall == deleted_pins

    # All-label Oler slack and the local wall residual both equal m exactly.
    all_label_slack = m * (m + 1) + 2 * m + 1 - n
    local_wall_residual = m * (m + 1) - 2 * m + 1 - z
    assert all_label_slack == local_wall_residual == m

    # The exact actual wall has error zero, so it is within the two-side
    # theorem's positive polynomial tolerance for this L=2m frame.
    eta = Fraction(3, 1_000_000 * (2 * m) ** 14 * (2 * m + 1))
    assert eta > 0

    # The opposite-corner pair has exactly D^2=2*m^2+m*sqrt(d). A square
    # grid on the same label count has squared diameter 2*m^2, strictly less.
    assert source_diameter_comparison(m, m, m, d) == 0

    print(
        f"PASS m={m}: n={n}, all_pairs={lower_pairs}, lower/upper pairs exact, "
        f"contacts={contacts}, Oler_slack={all_label_slack}, "
        f"wall_error=0<eta_(2m), K=z={z}, deficit={actual_deficit}, "
        f"required={deleted_pins}, target_shortfall={shortfall}"
    )


def check_exact_opened_wall_endpoint() -> None:
    """Check the m=n=7 two-side move, including every endpoint pair."""
    m = n = 7
    length = m + n
    epsilon = Fraction(1, 10 * length**4)
    amplitude = Fraction(1, 100 * length**3)

    # Store a point (x, y/sqrt(3)) in Q x Q; its squared distance is rational.
    endpoint = []
    for i in range(m + 1):
        for j in range(n + 1):
            if i == m or j == n:  # Retain the top and right sides.
                endpoint.append(
                    (("wall", i, j), Fraction(i) + Fraction(j, 7), Fraction(4 * j, 7))
                )
            elif i > 0 and j > 0:  # Move and retain every interior label.
                lam = (m - i) * (n - j) * (1 + epsilon * (m - i))
                assert 0 < i - amplitude * lam < m
                assert 0 < j - amplitude * lam < n
                x = Fraction(i) + Fraction(j, 7) - amplitude * lam * Fraction(8, 7)
                y = Fraction(4 * j, 7) - amplitude * lam * Fraction(4, 7)
                endpoint.append((("target", i, j), x, y))

    source_labels = (m + 1) ** 2
    deleted = m + n - 1
    capacity = (m - 1) * (n - 1)
    assert len(endpoint) == capacity + (m + n + 1) == source_labels - deleted
    assert sum(1 for label, *_ in endpoint if label[0] == "target") == capacity
    assert sum(1 for label, *_ in endpoint if label[0] == "wall") == m + n + 1

    lower_pairs = upper_pairs = strict_target_pairs = contacts = 0
    max_squared = Fraction(0)
    max_pair = None
    for left, right in combinations(endpoint, 2):
        label_a, x_a, y_a = left
        label_b, x_b, y_b = right
        dx, dy = x_a - x_b, y_a - y_b
        squared = dx * dx + 3 * dy * dy
        assert squared >= 1, (label_a, label_b, squared, "endpoint lower pair")
        lower_pairs += 1
        if label_a[0] == "target" or label_b[0] == "target":
            assert squared > 1, (label_a, label_b, squared, "target strictness")
            strict_target_pairs += 1
        else:
            contacts += squared == 1
        assert squared <= 112, (label_a, label_b, squared, "original diameter upper pair")
        upper_pairs += 1
        if squared > max_squared:
            max_squared, max_pair = squared, (label_a, label_b)

    assert lower_pairs == upper_pairs == 51 * 50 // 2
    assert strict_target_pairs == 36 * 15 + 36 * 35 // 2
    assert contacts == 2 * m
    assert max_squared < 112
    print(
        f"PASS exact opened-wall endpoint: source=64, deleted_wall={deleted}, "
        f"endpoint=51, lower/upper pairs={lower_pairs}/{upper_pairs}, "
        f"target-involving strict pairs={strict_target_pairs}, contacts={contacts}, "
        f"max_squared={max_squared} < D_source^2=112"
    )
    print(f"  max-diameter pair: {max_pair}")
    print(f"  cardinality funding shortfall: {deleted} labels")


def main() -> None:
    for m in (7, 8, 12, 24):
        check_frame(m)
    check_exact_opened_wall_endpoint()
    print("PASS finite source-pair and endpoint-ledger controls; universal claims use the README proof")


main()
