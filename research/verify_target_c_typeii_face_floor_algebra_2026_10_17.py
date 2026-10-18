#!/usr/bin/env python3
"""Independent exact checks for the Type-II separate-face floor algebra.

This finite checker verifies the recipient-incidence inequalities over every
admissible integer count ledger in the declared small domain and the exact
rational certificate used for the strict one-cell threshold comparison.  It
does not verify the weak-limit, atom-selection, disk-limit, or source-optimality
arguments in the accompanying audit note.
"""

from fractions import Fraction
from math import pi, sqrt


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def check_ledgers(max_q=6):
    checked = 0
    by_q = {}
    for q in range(1, max_q + 1):
        count = 0
        # b+Q=2(q-k), with k>=0.  Since b,Q are integral, k is exact
        # (possibly half-integral) in this finite arithmetic audit.
        for b in range(0, 2 * q + 1):
            for Q in range(0, 2 * q - b + 1):
                k = Fraction(2 * q - b - Q, 2)
                for f in range(Q + 1):
                    for f_boundary in range(f + 1):
                        # Each exceptional face contributes at least one unit
                        # of degree excess, separately on both sides.
                        for Q_inner in range(f - f_boundary, Q - f_boundary + 1):
                            Q_boundary = Q - Q_inner
                            boundary_occurrences = b + 4 * f_boundary + Q_boundary
                            inner_occurrences = 4 * (f - f_boundary) + Q_inner
                            for c_boundary in range(1, q + f_boundary + 1):
                                min_edges = q + f_boundary - c_boundary
                                if min_edges > boundary_occurrences // 2:
                                    continue
                                # Both endpoint budgets are largest at the
                                # minimum edge count.  The inner edge count
                                # cancels from (atomic trains + N_inner).
                                a_boundary_max = boundary_occurrences - 2 * min_edges
                                require(
                                    a_boundary_max
                                    <= 2 * f_boundary
                                    - Q_inner
                                    - 2 * k
                                    + 2 * c_boundary,
                                    "boundary incidence upper bound failed",
                                )
                                require(
                                    3 * f_boundary
                                    >= f + 2 * k - 2 * c_boundary,
                                    "separate-face lower bound failed",
                                )
                                combined_budget = Fraction(
                                    a_boundary_max + inner_occurrences, 2
                                )
                                require(
                                    combined_budget
                                    <= 2 * f
                                    - f_boundary
                                    - k
                                    + c_boundary,
                                    "combined endpoint budget failed",
                                )
                                require(
                                    3 * combined_budget
                                    <= 5 * (f - k + c_boundary),
                                    "5/3 coefficient consequence failed",
                                )
                                count += 1
        by_q[q] = count
        checked += count
    return checked, by_q


def main():
    checked, by_q = check_ledgers()

    # sqrt(3) < 7/4 is immediate from squaring.  Archimedes' bound
    # pi < 22/7 then gives 25*pi*sqrt(3) < 137.5 < 162.
    require(Fraction(7, 4) ** 2 > 3, "sqrt(3) rational upper bound failed")
    rational_margin = Fraction(162) - Fraction(25 * 22, 4)
    require(rational_margin == Fraction(49, 2), "wrong exact comparison margin")
    require(rational_margin > 0, "strict collar inequality failed")

    s2 = sqrt(pi / (2 * sqrt(3)))
    face_floor = 6 * s2 / 5
    metric_floor = pi + face_floor
    loaded_chain_floor = metric_floor / 2
    collar_threshold = 2 * pi / 3
    require(loaded_chain_floor > collar_threshold, "displayed constants disagree")

    print({
        "status": "PASS",
        "ledger_domain": (
            "1 <= q <= 6; all integral (b,Q,f,f_boundary,Q_inner,c_boundary) "
            "satisfying the source identity, face excess bounds, and a nonempty "
            "boundary-edge-count interval"
        ),
        "incidence_ledgers_checked": checked,
        "ledgers_by_q": by_q,
        "exact_strict_comparison": "162 - 25*(22/7)*(7/4) = 49/2 > 0",
        "display_only_approximations": {
            "s2": f"{s2:.12f}",
            "6s2/5": f"{face_floor:.12f}",
            "pi/2+3s2/5": f"{loaded_chain_floor:.12f}",
            "2pi/3": f"{collar_threshold:.12f}",
        },
        "scope": "finite incidence arithmetic and rational threshold certificate only",
    })


if __name__ == "__main__":
    main()
