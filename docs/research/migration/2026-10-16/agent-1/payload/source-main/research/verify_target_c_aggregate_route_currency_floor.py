"""Exact arithmetic checks for the aggregate route-currency floor.

The geometric inputs are audited separately in the companion note.  This script
checks only the outward-safe numerical margin and the finite ledger substitution.
It does not certify a global minimizer or a C-II closure.
"""

from fractions import Fraction as F


def main() -> None:
    # Safe lower/upper enclosures used in the note.
    s_star_lo = F(27985, 10000)
    pi_lo = F(314159, 100000)
    pi_hi = F(314160, 100000)
    sqrt3_hi = F(173206, 100000)

    c0_lo = pi_lo / 2 * (2 - sqrt3_hi)
    route_lo = 2 * s_star_lo + c0_lo - pi_hi
    assert route_lo > F(28762, 10000)

    # The exact finite cancellation used in the face identity.  The values are
    # arbitrary admissible ledgers, not a geometric example.
    q, k, e_bb, c_att, delta_r, f, d_sigma = map(
        F, (19, 3, 11, 7, 2, 5, 4)
    )
    assert c_att <= e_bb
    E = 4 * delta_r + 4 * f + 2 * (q - k - e_bb + c_att) - 2 * d_sigma
    E_upper = 4 * delta_r + 4 * f + 2 * (q - k) - 2 * d_sigma
    assert E <= E_upper

    # Substituting P_exc=Q+4f and Q=2(q-k)-per(F)-D*delta gives the
    # normalized algebra in (AR.7).  Use D=1 for this symbolic check.
    per_f, outer_delta = F(3), F(1, 5)
    Q = 2 * (q - k) - per_f - outer_delta
    P_exc = Q + 4 * f
    rhs = P_exc + per_f + outer_delta - 2 * d_sigma
    assert 4 * f + 2 * (q - k) - 2 * d_sigma == rhs

    print("aggregate route-currency floor arithmetic: PASS")
    print(f"safe_route_floor_lower={float(route_lo):.7f}")
    print("certified_safe_route_floor=2.8762")


if __name__ == "__main__":
    main()
