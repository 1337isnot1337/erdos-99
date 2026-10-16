#!/usr/bin/env python3
"""Arithmetic checker for the seven-row functional target in C:(5,12,12).

This does not perform the finite cover scan.  It checks the exact threshold
forced by the already-established replacement-functional accounting once a
good d6=5 pair shadow is lifted through one restored external row.
"""


def required_extra_rank(t, defect, p, deficiency):
    # D >= t + p + 3*d - 3*s.
    numerator = t + p + 3 * deficiency - defect
    return (numerator + 2) // 3


def main():
    D8 = -1
    p8 = 12
    d6 = 5

    # Established good-pair deletion arithmetic.
    D6 = D8 + 4
    p6 = p8
    assert D6 == 3
    s6 = required_extra_rank(6, D6, p6, d6)
    assert s6 == 10
    # A rank-one six-row canonical relation matrix has c+5 rows and rank c-d.
    six_functional_quotient_dimension = 5 + d6
    assert six_functional_quotient_dimension == 10
    assert s6 == six_functional_quotient_dimension

    # Restore one member of the deletion pair.  The selected pair is
    # p-retaining, so each intermediate one-row deletion is p-retaining.
    D7 = D8 + 2
    p7 = p8
    # Deficiency monotonicity from d6=5, combined with the established
    # seven-row alternatives d7 in {4,5}, forces d7=5.
    d7 = 5
    assert D7 == 1
    s7 = required_extra_rank(7, D7, p7, d7)
    assert s7 == 11
    seven_functional_quotient_dimension = 6 + d7
    assert seven_functional_quotient_dimension == 11
    assert s7 == seven_functional_quotient_dimension

    print("PASS: C:(5,12,12), d6=5 forces full seven-row functional rank")
    print("six_row", {"D": D6, "p": p6, "d": d6, "required_extra": s6})
    print("seven_row", {"D": D7, "p": p7, "d": d7, "required_extra": s7})
    print("seven_functional_quotient_dimension", seven_functional_quotient_dimension)
    print("finite_target", "exclude every qualifying d7=5 lift with extra rank 11")


if __name__ == "__main__":
    main()
