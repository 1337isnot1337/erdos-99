#!/usr/bin/env python3
from collections import Counter
from itertools import product

STATES = tuple(product(range(3), repeat=4))
T12 = (0, 2, 1)
T02 = (2, 1, 0)

def identity(s):
    return s

def a(s):
    A, B, C, D = s
    return T12[A], T12[B], D, C

def b(s):
    A, B, C, D = s
    return B, A, T02[C], T02[D]

def ab(s):
    return a(b(s))

def main():
    effective = (identity, a, b, ab)
    fixed_effective = Counter(sum(g(s) == s for s in STATES) for g in effective)
    assert fixed_effective == Counter({3: 2, 81: 1, 9: 1})
    fixed_full = Counter({k: 2 * v for k, v in fixed_effective.items()})
    assert fixed_full == Counter({3: 4, 81: 2, 9: 2})
    assert sum(k * v for k, v in fixed_full.items()) // 8 == 24
    unseen = set(STATES)
    sizes = Counter()
    while unseen:
        s = min(unseen)
        orbit = {g(s) for g in effective}
        unseen -= orbit
        sizes[len(orbit)] += 1
    assert sizes == Counter({4: 17, 2: 6, 1: 1})
    print("PASS support4: 81 raw orientations -> 24 symmetry classes", dict(sorted(sizes.items())))

if __name__ == "__main__":
    main()
