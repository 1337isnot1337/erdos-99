#!/usr/bin/env python3
"""Exact finite checks for the contact rhombic-grid regression.

All sign decisions are integer comparisons. The universal geometric proof and
the continuous triangle-cover argument are in the paired report; this script
checks finite source-pair ledgers at several exact parameter values.
"""

from __future__ import annotations


def check_parameter(m: int) -> tuple[int, int]:
    assert m >= 7
    d = m * m - 6 * m - 3
    assert d > 0
    assert d < m * m
    assert 3 * (m + 1) ** 2 < 4 * m * m
    assert d + 3 * (m + 1) ** 2 == 4 * m * m

    # Check every integer difference vector in the source index range.
    unit_vectors: set[tuple[int, int]] = set()
    vector_checks = 0
    for a in range(-m, m + 1):
        for b in range(-m, m + 1):
            if a == 0 and b == 0:
                continue
            vector_checks += 1
            if a == 0 or b == 0:
                q_minus_one = a * a + b * b - 1
                assert q_minus_one >= 0
                is_unit = q_minus_one == 0
            elif a * b > 0:
                # The positive radical term makes the squared norm > 1.
                assert a * a + b * b > 1
                is_unit = False
            else:
                r, s = abs(a), abs(b)
                # m*(r^2+s^2-1) > r*s*sqrt(d), checked by squaring
                # two strictly positive sides in Q(sqrt(d)).
                left = m * (r * r + s * s - 1)
                right_coefficient = r * s
                assert left > 0
                assert left * left > right_coefficient**2 * d
                is_unit = False
            if is_unit:
                unit_vectors.add((a, b))

    assert unit_vectors == {(-1, 0), (1, 0), (0, -1), (0, 1)}

    points = [(i, j) for i in range(m + 1) for j in range(m + 1)]
    contact_count = 0
    pair_checks = 0
    for index, (i, j) in enumerate(points):
        for k, ell in points[index + 1 :]:
            a, b = k - i, ell - j
            pair_checks += 1
            is_unit = (a, b) in unit_vectors
            if is_unit:
                contact_count += 1
                assert ((i + j) & 1) != ((k + ell) & 1)
    assert pair_checks == len(points) * (len(points) - 1) // 2
    assert contact_count == 2 * m * (m + 1)
    assert all(
        sum((abs(i - k) + abs(j - ell) == 1) for k, ell in points) >= 2
        for i, j in points
    )

    # Exact Oler slack after division by a0=sqrt(3)/2.
    q_over_a0 = m * m + m
    p_over_2 = 2 * m
    n = (m + 1) ** 2
    slack = q_over_a0 + p_over_2 + 1 - n
    assert slack == m

    # D^2 = 2m^2 + m sqrt(d), with sqrt(2)m < D < sqrt(3)m.
    # These bounds reduce to 0 < d < m^2, already checked above.
    assert d > 0 and d < m * m
    return vector_checks, pair_checks


def main() -> None:
    for m in (7, 8, 12, 24):
        vector_checks, pair_checks = check_parameter(m)
        n = (m + 1) ** 2
        contacts = 2 * m * (m + 1)
        print(
            f"PASS m={m}: n={n}, difference_vectors={vector_checks}, "
            f"source_pairs={pair_checks}, contacts={contacts}, Oler_slack={m}; "
            "exact integer/radical comparisons"
        )
    print("PASS finite algebraic checks; universal claims are proved in the report")


if __name__ == "__main__":
    main()
