#!/usr/bin/env python3
"""Arithmetic certificate for maximal replacement-functional rank in the
remaining eight-no-root k=6 Target-C layer.

The companion proof note derives the rank-uniform replacement-functional bound

    D >= t + p + 3*d - 3*s,

where t is the number of no-root rows, p is the selected incomplete-root cost,
d is virtual-canonical complete-row deficiency, and s is the extra rank of the
replacement functionals modulo the canonical relation row space.

If the coefficient-constraint space has rank r, the canonical relation matrix
has c+(t-r) rows and rank c-d, so its functional quotient has dimension

    (t-r) + d.

This checker verifies that every still-surviving global eight-row k=6 profile
must attain that entire quotient, and that the forced D=-2,p=8 clean seven-row
shadow must likewise attain its entire seven-dimensional quotient.
"""


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def quotient_dim(t: int, coefficient_rank: int, deficiency: int) -> int:
    return (t - coefficient_rank) + deficiency


def required_extra_rank(D: int, t: int, p: int, deficiency: int) -> int:
    return ceil_div(t + p + 3 * deficiency - D, 3)


def lower_bound(t: int, p: int, deficiency: int, extra_rank: int) -> int:
    return t + p + 3 * deficiency - 3 * extra_rank


def verify_global_dminus2_branch():
    # The preceding reduction forces exactly this profile.
    D, t, p, r, d, q = -2, 8, 8, 2, 2, 8
    qdim = quotient_dim(t, r, d)
    req = required_extra_rank(D, t, p, d)
    assert qdim == 8
    assert req == qdim
    assert q == qdim
    assert lower_bound(t, p, d, qdim - 1) == 1 > D
    assert lower_bound(t, p, d, qdim) == D
    return {
        "D": D,
        "p": p,
        "d": d,
        "q": q,
        "quotient_dim": qdim,
        "required_extra_rank": req,
    }


def verify_clean_seven_shadow():
    # Every three-clean deletion in the forced D=-2 branch has
    # D_7=0, p_7=8, coefficient rank 2, d_7=2 and q_7>=7.
    D, t, p, r, d = 0, 7, 8, 2, 2
    qdim = quotient_dim(t, r, d)
    req = required_extra_rank(D, t, p, d)
    assert qdim == 7
    assert req == qdim
    assert lower_bound(t, p, d, qdim - 1) == 3 > D
    assert lower_bound(t, p, d, qdim) == D
    return {
        "D": D,
        "p": p,
        "d": d,
        "quotient_dim": qdim,
        "required_extra_rank": req,
    }


def verify_global_dminus1_profiles():
    # These are exactly the profiles left by the preceding k=6 reduction.
    profiles = [
        (1, 7, 5),
        (1, 8, 7),
        (2, 8, 7),
        (2, 9, 9),
        (3, 9, 9),
    ]
    out = []
    for d, q, singleton_min in profiles:
        D, t, p, r = -1, 8, 9, 2
        qdim = quotient_dim(t, r, d)
        req = required_extra_rank(D, t, p, d)
        assert qdim == 6 + d
        assert req == qdim
        assert q >= req
        assert lower_bound(t, p, d, qdim - 1) == 2 > D
        assert lower_bound(t, p, d, qdim) == D
        out.append((d, q, singleton_min, qdim, req))
    return out


def verify_rank_ceiling_identity():
    # The quotient ceiling itself follows directly from row counts:
    # c+n total canonical relation rows, rank c-d, so codimension n+d.
    checks = []
    for t in (7, 8):
        for r in (1, 2):
            if r >= t:
                continue
            n = t - r
            for d in range(1, 6):
                for c in (d, d + 1, d + 7, 35):
                    if c < d:
                        continue
                    total_rows = c + n
                    canonical_rank = c - d
                    codim = total_rows - canonical_rank
                    assert codim == n + d == quotient_dim(t, r, d)
                    checks.append((t, r, d, c, codim))
    return len(checks)


def main():
    count = verify_rank_ceiling_identity()
    branch_a = verify_global_dminus2_branch()
    clean7 = verify_clean_seven_shadow()
    branch_b = verify_global_dminus1_profiles()

    print("PASS: eight-no-root k=6 maximal functional-rank arithmetic")
    print("rank_ceiling_checks", count)
    print("global_Dminus2_profile", branch_a)
    print("clean_seven_shadow", clean7)
    print("global_Dminus1_profiles", branch_b)
    print("global_Dminus2_eight_functionals_must_be_independent", True)
    print("clean_seven_shadow_must_fill_rank7_quotient", True)
    print("all_remaining_global_Dminus1_profiles_fill_their_quotient", True)


if __name__ == "__main__":
    main()
