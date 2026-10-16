#!/usr/bin/env python3
"""Finite arithmetic check for the six-no-root deletion-shadow synchronization lemma.

This script does not prove the linear-algebra step k(A)=k(B)-1. It checks the
remaining finite implication from the already-proved deletion-shadow theorem
and five-no-root boundary bands:

* D(B) in {-2,-1};
* every five-no-root deletion A has D(A)=D(B)+2;
* k(A)=k(B)-1;
* p(A)<=p(B);
* a negative six-no-root defect obeys p(B)<3*k(B)-6;
* D(B) == 6+p(B) (mod 3).

Under those constraints the only possible (D(B),k(B),p(B),k(A),p(A)) tuples
are the six synchronized boundary cases asserted in the companion note.
"""

FIVE_BOUNDARY = {
    0: {(3, 4), (4, 7), (5, 10)},
    1: {(3, 5), (4, 8), (5, 11)},
}

EXPECTED = {
    (-2, 4, 4, 3, 4),
    (-2, 5, 7, 4, 7),
    (-2, 6, 10, 5, 10),
    (-1, 4, 5, 3, 5),
    (-1, 5, 8, 4, 8),
    (-1, 6, 11, 5, 11),
}


def enumerate_cases():
    out = set()
    for d_b in (-2, -1):
        d_a = d_b + 2
        for k_b in range(7):
            k_a = k_b - 1
            for p_b in range(32):
                if not (p_b < 3 * k_b - 6):
                    continue
                if (d_b - (6 + p_b)) % 3:
                    continue
                for kbnd, p_a in FIVE_BOUNDARY[d_a]:
                    if kbnd != k_a:
                        continue
                    if p_a > p_b:
                        continue
                    out.add((d_b, k_b, p_b, k_a, p_a))
    return out


def main():
    got = enumerate_cases()
    assert got == EXPECTED, (got, EXPECTED)
    assert all(p_b == p_a for _d, _k, p_b, _ka, p_a in got)
    assert all(k_b >= 4 for _d, k_b, _p, _ka, _pa in got)
    print("PASS: six-no-root deletion shadows synchronize to six boundary cases")
    for case in sorted(got):
        print(case)


if __name__ == "__main__":
    main()
