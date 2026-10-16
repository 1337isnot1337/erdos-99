#!/usr/bin/env python3
"""Exact finite certificates for seven-ray ground sign obstructions.

Layer 1: for ordered rays theta_1<...<theta_7 spanning less than pi, a 3+4
signed unit-vector equilibrium is impossible whenever the four-element class
has an unpaired pivot p and the other three majority indices can be matched to
the three minority indices so that each majority index lies strictly between p
and its matched minority index. Dotting with u_p makes every term positive.

Layer 2: in H6 the span is less than 2pi/3. Projection on the cone bisector
makes the cosine values a unimodal sequence with endpoint value c>1/2. A
layer-cake/contiguous-block bound excludes additional sign patterns.

The script performs only exact finite combinatorics; no floating point or
optimization is used.
"""
from itertools import combinations, permutations

V = tuple(range(1, 8))


def closer_by_order(m, n, p):
    """Order alone forces |theta_m-theta_p| < |theta_n-theta_p|."""
    return (p < m < n) or (n < m < p)


def certificates(minority):
    minority = tuple(sorted(minority))
    majority = tuple(i for i in V if i not in minority)
    out = []
    for p in majority:
        rem = tuple(i for i in majority if i != p)
        for q in permutations(minority):
            pairs = tuple(zip(rem, q))
            if all(closer_by_order(m, n, p) for m, n in pairs):
                out.append((p, pairs))
    return out


bad = {}
for P in combinations(V, 3):
    cs = certificates(P)
    if cs:
        bad[P] = cs

EXPECTED = {
    (1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 2, 7),
    (1, 3, 4), (1, 3, 5), (1, 3, 7),
    (1, 5, 7), (1, 6, 7),
    (3, 5, 7), (3, 6, 7),
    (4, 5, 7), (4, 6, 7), (5, 6, 7),
}
assert set(bad) == EXPECTED
assert len(bad) == 14


def reflect(P):
    return tuple(sorted(8 - i for i in P))

assert {reflect(P) for P in EXPECTED} == EXPECTED
reps = []
seen = set()
for P in sorted(EXPECTED):
    if P in seen:
        continue
    orb = {P, reflect(P)}
    seen |= orb
    reps.append(min(orb))
assert len(reps) == 7

SPARSE = {
    (1, 2, 3): (7, ((4, 1), (5, 2), (6, 3))),
    (1, 2, 4): (7, ((3, 1), (5, 2), (6, 4))),
    (1, 2, 5): (7, ((3, 1), (4, 2), (6, 5))),
    (1, 2, 7): (5, ((3, 1), (4, 2), (6, 7))),
    (1, 3, 4): (7, ((2, 1), (5, 3), (6, 4))),
    (1, 3, 5): (7, ((2, 1), (4, 3), (6, 5))),
    (1, 3, 7): (5, ((2, 1), (4, 3), (6, 7))),
}
for P, cert in SPARSE.items():
    assert cert in bad[P]

assert (1, 3, 7) in bad
assert (1, 5, 7) in bad
assert reflect((1, 3, 7)) == (1, 5, 7)

print("PASS: seven-ray open-semicircle pairing obstruction")
print("excluded 3-subsets:", len(bad), "= 7 reflection classes")
print("patterns:", " ".join("".join(map(str, p)) for p in sorted(bad)))


# H6-specific width < 2pi/3. With beta the cone bisector and
# c=cos(phi/2)>1/2, the projected cosine sequence is unimodal. After
# normalization y_i=(cos(theta_i-beta)-c)/(1-c), every superlevel set is a
# contiguous block of the interior indices 2,...,6. If every such block has
# signed excess at most 1, then the signed projection is at most 1-2c<0.
def max_interior_block_excess(minority):
    minority = set(minority)
    s = {i: (1 if i in minority else -1) for i in V}
    vals = [0]
    for a in range(2, 7):
        for b in range(a, 7):
            vals.append(sum(s[i] for i in range(a, b + 1)))
    return max(vals)


bisector_bad = {
    P for P in combinations(V, 3)
    if max_interior_block_excess(P) <= 1
}
EXPECTED_BISECTOR = {
    (1, 2, 4), (1, 2, 5), (1, 2, 6), (1, 2, 7),
    (1, 3, 5), (1, 3, 6), (1, 3, 7),
    (1, 4, 6), (1, 4, 7), (1, 5, 7), (1, 6, 7),
    (2, 4, 6), (2, 4, 7), (2, 5, 7), (2, 6, 7),
    (3, 5, 7), (3, 6, 7), (4, 6, 7),
}
assert bisector_bad == EXPECTED_BISECTOR
assert len(bisector_bad) == 18
assert {reflect(P) for P in bisector_bad} == bisector_bad

NEW_H6 = bisector_bad - EXPECTED
EXPECTED_NEW_H6 = {
    (1, 2, 6), (1, 3, 6), (1, 4, 6), (1, 4, 7),
    (2, 4, 6), (2, 4, 7), (2, 5, 7), (2, 6, 7),
}
assert NEW_H6 == EXPECTED_NEW_H6

H6_BAD = EXPECTED | bisector_bad
H6_REMAIN = set(combinations(V, 3)) - H6_BAD
EXPECTED_H6_REMAIN = {
    (1, 4, 5), (1, 5, 6),
    (2, 3, 4), (2, 3, 5), (2, 3, 6), (2, 3, 7),
    (2, 4, 5), (2, 5, 6),
    (3, 4, 5), (3, 4, 6), (3, 4, 7), (3, 5, 6),
    (4, 5, 6),
}
assert H6_REMAIN == EXPECTED_H6_REMAIN
assert len(H6_BAD) == 22 and len(H6_REMAIN) == 13
assert {reflect(P) for P in H6_BAD} == H6_BAD
assert {reflect(P) for P in H6_REMAIN} == H6_REMAIN

print("H6 width<2pi/3: bisector excludes 18 patterns, 8 new beyond pairing")
print("H6 combined exclusions: 22/35; remaining:",
      " ".join("".join(map(str, p)) for p in sorted(H6_REMAIN)))
