#!/usr/bin/env python3
from math import ceil

def profiles(D, k):
    out = []
    for d in range(10):
        p = D - 9 - 3*d + 3*k
        if p >= 0:
            out.append((d, p))
    return out

def weights(D, rank):
    return tuple(ceil((3*j-D)/2) for j in range(1, rank+1))

def main():
    for D in (-2, -1):
        for k in range(4):
            assert profiles(D, k) == []

    assert profiles(-2, 4) == [(0, 1)]
    assert profiles(-1, 4) == [(0, 2)]

    assert weights(-2, 5) == (3, 4, 6, 7, 9)
    assert weights(-1, 5) == (2, 4, 5, 7, 8)

    cmax = 15 - 4
    assert cmax == 11

    hmax_m2 = max(h for h in range(36) if 36 >= h + 2*max(0, h-12))
    hmax_m1 = max(h for h in range(36) if 36 >= h + max(0, h-13))
    assert hmax_m2 == 20
    assert hmax_m1 == 24

    print("PASS: nine-no-root k=4 arithmetic/code/touch reduction")
    print("D=-2", profiles(-2,4), weights(-2,5), hmax_m2)
    print("D=-1", profiles(-1,4), weights(-1,5), hmax_m1)

if __name__ == "__main__":
    main()
