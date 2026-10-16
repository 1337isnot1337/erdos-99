#!/usr/bin/env python3
"""Exact S7 orbit count for seven no-root K8 four-cycles.

A no-root four-cycle is a simple 4-cycle on vertices {1,...,7}; there are
C(7,4)*3 = 105. S7 relabels these 105 objects. Burnside's lemma counts
orbits of unordered t-subsets exactly. For each vertex permutation, the number
of invariant t-subsets is the coefficient of x^t in

    product_C (1 + x^{|C|}),

where C ranges over cycles of the induced permutation on the 105 four-cycles.
All arithmetic is integral. As cross-checks, t=5 and t=6 reproduce the
independently committed orbit counts used by the five- and six-no-root audits.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import comb, factorial

VERTICES = tuple(range(1, 8))


def edge(a, b):
    return (a, b) if a < b else (b, a)


def cycle_key(order):
    return tuple(sorted(edge(order[i], order[(i + 1) % 4]) for i in range(4)))


def four_cycles():
    out = set()
    for quad in combinations(VERTICES, 4):
        a, b, c, d = quad
        out.add(cycle_key((a, b, c, d)))
        out.add(cycle_key((a, b, d, c)))
        out.add(cycle_key((a, c, b, d)))
    result = tuple(sorted(out))
    assert len(result) == comb(7, 4) * 3 == 105
    return result


CYCLES = four_cycles()
INDEX = {c: i for i, c in enumerate(CYCLES)}


def vertex_cycle_type(perm):
    mapping = {VERTICES[i]: perm[i] for i in range(7)}
    seen = set()
    lengths = []
    for v in VERTICES:
        if v in seen:
            continue
        cur = v
        length = 0
        while cur not in seen:
            seen.add(cur)
            cur = mapping[cur]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def induced_permutation(perm):
    mapping = {VERTICES[i]: perm[i] for i in range(7)}
    image = []
    for c in CYCLES:
        mapped = tuple(sorted(edge(mapping[a], mapping[b]) for a, b in c))
        image.append(INDEX[mapped])
    assert sorted(image) == list(range(105))
    return tuple(image)


def induced_cycle_lengths(image):
    seen = [False] * len(image)
    lengths = []
    for start in range(len(image)):
        if seen[start]:
            continue
        cur = start
        length = 0
        while not seen[cur]:
            seen[cur] = True
            cur = image[cur]
            length += 1
        lengths.append(length)
    assert sum(lengths) == 105
    return tuple(sorted(lengths))


def fixed_subset_count(induced_lengths, t):
    coeff = [0] * (t + 1)
    coeff[0] = 1
    for length in induced_lengths:
        for j in range(t, length - 1, -1):
            coeff[j] += coeff[j - length]
    return coeff[t]


def class_size(cycle_type):
    counts = Counter(cycle_type)
    denominator = 1
    for length, multiplicity in counts.items():
        denominator *= (length ** multiplicity) * factorial(multiplicity)
    return factorial(7) // denominator


def main():
    by_type = defaultdict(list)
    burnside = {5: 0, 6: 0, 7: 0}

    for perm in permutations(VERTICES):
        ctype = vertex_cycle_type(perm)
        lengths = induced_cycle_lengths(induced_permutation(perm))
        fixed = {t: fixed_subset_count(lengths, t) for t in burnside}
        by_type[ctype].append((lengths, fixed))
        for t in burnside:
            burnside[t] += fixed[t]

    assert sum(len(v) for v in by_type.values()) == factorial(7) == 5040

    expected_fixed7 = {
        (1, 1, 1, 1, 1, 1, 1): 22760723700,
        (2, 1, 1, 1, 1, 1): 4646900,
        (2, 2, 1, 1, 1): 256500,
        (2, 2, 2, 1): 256500,
        (3, 1, 1, 1, 1): 1683,
        (3, 2, 1, 1): 41,
        (3, 2, 2): 51,
        (3, 3, 1): 0,
        (4, 1, 1, 1): 100,
        (4, 2, 1): 100,
        (4, 3): 1,
        (5, 1, 1): 0,
        (5, 2): 0,
        (6, 1): 0,
        (7,): 15,
    }

    rows = []
    for ctype in sorted(by_type, reverse=True):
        records = by_type[ctype]
        size = len(records)
        assert size == class_size(ctype)
        fixed_values = {
            t: {record[1][t] for record in records}
            for t in burnside
        }
        assert all(len(values) == 1 for values in fixed_values.values())
        fixed = {t: fixed_values[t].pop() for t in burnside}
        assert fixed[7] == expected_fixed7[ctype]
        rows.append((ctype, size, fixed[5], fixed[6], fixed[7]))

    assert len(rows) == 15
    for t in burnside:
        assert burnside[t] % factorial(7) == 0

    orbits = {t: burnside[t] // factorial(7) for t in burnside}

    assert comb(105, 5) == 96560646
    assert comb(105, 6) == 1609344100
    assert comb(105, 7) == 22760723700

    assert burnside[5] == 103073040
    assert orbits[5] == 20451
    assert burnside[6] == 1642591440
    assert orbits[6] == 325911
    assert burnside[7] == 22912414560
    assert orbits[7] == 4546114

    print("PASS: exact S7 orbit count for seven no-root four-cycle subsets")
    print("no_root_four_cycles", len(CYCLES))
    print("seven_subsets", comb(105, 7))
    print("S7_orbits_seven_subsets", orbits[7])
    print("burnside_sum_seven", burnside[7])
    print("crosscheck_S7_orbits_six_subsets", orbits[6])
    print("crosscheck_burnside_sum_six", burnside[6])
    print("crosscheck_S7_orbits_five_subsets", orbits[5])
    print("crosscheck_burnside_sum_five", burnside[5])
    print("cycle_type class_size fixed_5_subsets fixed_6_subsets fixed_7_subsets")
    for ctype, size, fixed5, fixed6, fixed7 in rows:
        print(ctype, size, fixed5, fixed6, fixed7)


if __name__ == "__main__":
    main()
